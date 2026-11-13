# Troubleshooting Methodology & Diagnostic Tools

Troubleshooting is a discipline before it is a toolbox. A methodical approach stops
you from guessing, and the right diagnostic commands turn a vague "it's broken"
into a specific, fixable cause. This lesson covers the structured method Linux+
expects, then the general-purpose tools you reach for first on any problem.

## A structured methodology

CompTIA frames troubleshooting as an ordered process. Follow it in sequence
rather than jumping to a fix:

1. **Identify the problem.** Gather information, ask the user what changed,
   reproduce the issue, and check logs. "What changed recently?" solves a
   surprising share of incidents.
2. **Establish a theory of probable cause.** Form a hypothesis — and *question the
   obvious* first (is it plugged in? is the service running? is the disk full?).
3. **Test the theory.** Confirm or refute the hypothesis. If it's wrong, form a
   new one — or escalate.
4. **Establish a plan of action**, considering the potential side effects of the
   fix.
5. **Implement the solution** (or escalate if it's beyond your scope or access).
6. **Verify full system functionality** and, where possible, put **preventive
   measures** in place so it doesn't recur.
7. **Document** the findings, actions and outcome.

> The highest-value habit is **change the smallest thing, then re-test.** If you
> alter five things at once and the problem goes away, you've learned nothing
> about the cause and may have introduced new issues.

## Logs: the first place to look

Most problems leave a trail in the logs.

- **`journalctl`** reads the systemd journal. Scope it tightly:
  `journalctl -u nginx` (one service), `journalctl -b` (this boot),
  `journalctl -p err` (error priority and worse), `journalctl -f` (follow live),
  `journalctl --since "10 min ago"`.
- **`/var/log/`** holds traditional text logs: `syslog`/`messages` (general),
  `auth.log`/`secure` (authentication), `dmesg`/`boot.log` (startup).
- **`dmesg`** prints the **kernel ring buffer** — the place to see hardware,
  driver and out-of-memory messages (`dmesg -T` adds human timestamps).
- **`tail -f /var/log/syslog`** follows a text log as it grows.

## Text processing: parsing what you find

Logs are huge, so you filter and reshape them with the classic text trio and its
companions:

- **`grep`** finds lines matching a pattern: `grep -i "fail" /var/log/auth.log`,
  `grep -r` recurses, `grep -v` inverts (lines *not* matching),
  `grep -c` counts, `grep -E` enables extended regex.
- **`sed`** is a stream editor for find-and-replace and line edits:
  `sed 's/old/new/g' file` substitutes globally; `sed -n '5,10p'` prints a line
  range.
- **`awk`** processes columns. `awk '{print $1}'` prints the first field of each
  line; `awk -F: '{print $1}' /etc/passwd` sets the field separator to a colon to
  pull out usernames.

```
# Top 5 IPs failing SSH logins:
$ grep "Failed password" /var/log/auth.log \
      | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -5
```

Supporting tools complete the pipeline: `cut` (extract fields/columns), `sort`,
`uniq -c` (collapse and count duplicates — sort first), `wc -l` (count lines) and
`tr` (translate/delete characters).

### Taming the output

Two helpers keep long output usable. **`tee`** writes a pipeline's output to a
file *and* the screen at once, so you can watch a long command while capturing it:
`systemctl status nginx | tee status.txt`. And **`less`** pages through anything
too long to read in one screen (`journalctl | less`), with `/` to search.

When the logs themselves are the problem — growing until they fill the disk —
**`logrotate`** is the answer. Configured in `/etc/logrotate.conf` and
`/etc/logrotate.d/`, it rotates, compresses and prunes log files on a schedule, so
a chatty service can't quietly consume every free byte in `/var/log`.

## Watching what a process does

When a program fails silently, trace it:

- **`strace command`** shows every **system call** a process makes — invaluable
  for "it can't find a file" or "permission denied" where the error is otherwise
  hidden. `strace -p PID` attaches to a running process.
- **`ltrace`** does the same for library calls.
- **`lsof`** lists **open files** (and sockets): `lsof -p PID` for one process,
  `lsof /var/log/app.log` to see who holds a file, `lsof -i :443` for what's using
  a port.
- **`watch -n2 command`** re-runs a command every two seconds so you can watch a
  value change.

## Inventorying the hardware

To see what the system actually has and how the kernel sees it:

| Command | Shows |
|---------|-------|
| `lscpu` | CPU model, cores, architecture |
| `lsblk` | Block devices and partitions as a tree |
| `lspci` | PCI devices (GPU, NICs, controllers) |
| `lsusb` | USB devices |
| `lshw` | A full hardware inventory |
| `free -h` | Memory and swap usage |
| `uptime` | Load averages and how long it's been up |

## Exam focus

- Apply the methodology **in order**: identify → theory of probable cause → test
  the theory → plan → implement (or escalate) → verify + prevent → document.
  Question the obvious and change one thing at a time.
- Logs first: **`journalctl`** (`-u` service, `-b` boot, `-p` priority, `-f`
  follow) for systemd; **`/var/log/`** for text logs (`syslog`/`messages`,
  `auth.log`/`secure`); **`dmesg`** for the kernel ring buffer.
- The text trio: **`grep`** (match lines; `-i`, `-v`, `-r`, `-c`), **`sed`**
  (stream edit / substitute), **`awk`** (columns; `-F` sets the field separator).
  Chain with `sort | uniq -c | sort -rn` to rank.
- **`strace`** traces system calls (great for hidden "file not found"/"permission
  denied"); **`lsof`** lists open files and ports; **`watch`** repeats a command.
- Inventory hardware with `lscpu`, `lsblk`, `lspci`, `lsusb`, `lshw`; `free -h`
  and `uptime` for memory and load at a glance.
