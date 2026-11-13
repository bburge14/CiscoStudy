# CPU, Memory & Performance

"The server is slow" is three different problems wearing the same complaint: the
CPU is saturated, memory is exhausted and swapping, or the disks can't keep up.
This lesson teaches the metrics that tell these apart and the tools that expose
them, so you can name the bottleneck instead of guessing.

## Load average: the first signal

`uptime` and the top line of `top` show three **load averages** — the 1-, 5- and
15-minute figures:

```
$ uptime
 10:14:02 up 7 days,  load average: 0.52, 2.10, 3.85
```

Load average is roughly the number of processes **runnable or waiting** (including
those blocked on disk) over that window. The number means nothing without the
**core count**: a load of `4.0` is full utilization on a 4-core box but means a
backlog on a 2-core box. The three values show *trend* — here load is **falling**
(15-min 3.85 → 1-min 0.52), so the spike has passed.

## top: the live dashboard

`top` (or the friendlier `htop`) is the go-to live view. Read the CPU summary
line:

| Field | Meaning |
|-------|---------|
| `us` | User-space CPU time |
| `sy` | Kernel/system CPU time |
| `id` | Idle |
| `wa` | **I/O wait** — CPU idle *because it's waiting on disk* |
| `st` | Steal — time a VM's CPU was taken by the hypervisor |

Inside `top`, press `P` to sort by CPU, `M` to sort by memory. Each process shows
**VIRT** (total virtual memory mapped), **RES** (resident — real RAM in use, the
number that usually matters) and **SHR** (shared).

> Learn to read the CPU line as a diagnosis: high **`us`/`sy`** with high load =
> **CPU-bound**. High **`wa`** = the CPU is fine but **starved by slow disk I/O**.
> High **`st`** on a VM = a noisy neighbor on the host.

## Memory and swap

`free -h` summarizes memory:

```
$ free -h
               total   used   free   shared  buff/cache   available
Mem:            15Gi   4.2Gi  380Mi    210Mi       10Gi       10Gi
Swap:          2.0Gi   128Mi  1.9Gi
```

The trap is the **`free`** column: it looks tiny because Linux deliberately uses
spare RAM for **`buff/cache`** (disk caching), which is **reclaimable** the moment
an application needs it. The number that actually matters is **`available`** —
memory that can be given to new processes without swapping. Here 10 GiB is
available, so memory is healthy despite only 380 MiB "free."

**Swap** is disk used as overflow memory. A little swap in use is normal; the
danger sign is **active, continuous swapping** (thrashing), which `vmstat` exposes
through its `si`/`so` (swap-in/swap-out) columns:

```
$ vmstat 2
 r  b   swpd   free   buff  cache   si   so    bi    bo   us sy id wa
 2  1  65536  40000  1200  90000  420  380   900  1100   10  4 20 66
```

Non-zero, sustained `si`/`so` means the system is memory-bound and paging to disk
— devastating for performance. If memory runs out entirely, the kernel's **OOM
killer** terminates a process to recover, logging `Out of memory: Killed process`
to `dmesg`/the journal.

## I/O: when the disks are the limit

High `wa` points at storage. **`iostat -x 2`** breaks it down per device:

- **`%util`** — how busy the device is; near 100% means saturated.
- **`await`** — average time (ms) a request waited; rising await signals a
  struggling disk.
- **`r/s`, `w/s`, `tps`** — reads, writes and transactions per second.

**`iotop`** shows which *processes* are driving the I/O, the same way `top` does
for CPU.

## Snapshots vs. history

`top`, `vmstat` and `iostat` show the system *right now*. But incidents are often
over by the time you log in, so you also need history. **`sar`** (from the
`sysstat` package) reports **collected** CPU, memory, swap, I/O and network
statistics at intervals throughout the day, letting you answer "what was the load
at 3 a.m.?" after the fact. **`pidstat`** breaks the same resource use down
**per process**. Enabling `sysstat` data collection before trouble strikes is what
makes post-incident analysis possible.

## Pinning down the bottleneck

Put the signals together:

| Symptom | Bottleneck | Confirm with |
|---------|-----------|--------------|
| High load, high `us`/`sy`, low `wa` | **CPU** | `top`, `mpstat`, `vmstat` (`r` high) |
| Low `available`, sustained `si`/`so` | **Memory** (swapping) | `free -h`, `vmstat` |
| High `wa`, high `%util`/`await` | **Disk I/O** | `iostat -x`, `iotop` |

Once you've found the offending process, you can lower its priority with
**`renice`**, cap resources with `ulimit` or cgroups, or fix the underlying cause
(a runaway query, a memory leak, a slow disk).

## Exam focus

- **Load average** (1/5/15 min from `uptime`/`top`) counts runnable + waiting
  processes; interpret it **relative to core count**, and read the three values as
  a trend.
- In `top`, **`us`/`sy`** = CPU busy (CPU-bound), **`wa`** = waiting on disk
  (I/O-bound), **`st`** = VM steal. Sort with `P` (CPU) / `M` (memory); **RES** is
  real RAM used.
- `free -h`: ignore the small **`free`** number — **`buff/cache` is reclaimable**
  and **`available`** is the true measure of free memory.
- Sustained **`si`/`so`** in `vmstat` = active swapping (thrashing) = memory-bound.
  The **OOM killer** kills a process when memory is exhausted (seen in `dmesg`).
- **`iostat -x`** for disk: **`%util`** (saturation), **`await`** (latency);
  **`iotop`** finds the process causing I/O.
- Classify first — CPU vs memory vs I/O — then act (`renice`, `ulimit`, or fix the
  root cause).
