# Boot, Kernel Modules, Processes & systemd Services

This lesson follows a Linux machine from power-on to a running workload. First the
firmware and bootloader hand control to the kernel; the kernel loads *modules* to
drive your hardware; then **systemd** takes over as the first process and launches
every *service*. Along the way you manage the individual *processes* those
services spawn.

## The boot sequence

Power-on proceeds through four clear stages:

1. **Firmware** — **BIOS** (older) or **UEFI** (modern) initializes hardware and
   finds a bootable device. UEFI boots from a GPT-partitioned disk with an EFI
   System Partition (mounted at `/boot/efi`) and can enforce **Secure Boot**,
   which only runs signed bootloaders.
2. **Bootloader** — almost always **GRUB2**. It presents the boot menu and loads
   the kernel. Its runtime config is `/boot/grub2/grub.cfg` (or
   `/boot/grub/grub.cfg`), but you *never* edit that by hand: change
   `/etc/default/grub`, then regenerate with `grub2-mkconfig -o ...` (Red Hat) or
   `update-grub` (Debian).
3. **Kernel + initramfs** — the kernel unpacks a temporary root filesystem, the
   **initramfs**, which contains just enough drivers to find and mount the real
   root filesystem.
4. **init (systemd)** — the kernel starts **PID 1**, systemd, which brings the
   rest of the system up.

## Kernel modules

The kernel is modular: drivers and features load on demand as **kernel modules**
rather than being compiled in. They live under `/lib/modules/$(uname -r)/`, keyed
to the running kernel version (`uname -r`).

- `lsmod` lists currently loaded modules.
- `modprobe e1000e` loads a module *and its dependencies*; `modprobe -r` unloads
  it.
- `modinfo e1000e` shows a module's description, parameters and dependencies.
- `insmod` and `rmmod` are the primitive load/unload tools that ignore
  dependencies — prefer `modprobe`.

Persist choices with config files: `/etc/modules-load.d/*.conf` lists modules to
load at boot, and `/etc/modprobe.d/*.conf` sets options or blacklists a module.

## Processes

A running program is a **process** with a numeric **PID** and a parent
(**PPID**). Everything ultimately descends from PID 1.

- `ps aux` (BSD style) or `ps -ef` (System V style) lists all processes with their
  owners, CPU/memory use and command lines.
- `pstree` draws the parent/child hierarchy; `top` (or `htop`) shows a live,
  sorted view.

### Signals

You control processes by sending **signals**:

| Signal | Number | Effect |
|--------|--------|--------|
| `SIGTERM` | 15 | Polite "please stop" — the default for `kill`; lets the process clean up |
| `SIGKILL` | 9 | Forcible kill the process cannot catch or ignore — last resort |
| `SIGHUP` | 1 | Hang-up; many daemons treat it as "reload your config" |
| `SIGSTOP` / `SIGCONT` | 19 / 18 | Pause and resume |

So `kill 4821` sends SIGTERM; `kill -9 4821` forces it. `killall nginx` and
`pkill -f pattern` act on processes by name instead of PID.

> Reach for `SIGTERM` (the default) first and give the process a moment to exit
> cleanly. Only escalate to `SIGKILL` (`-9`) when it refuses — a killed process
> gets no chance to flush buffers or release locks.

### Jobs and priority

In an interactive shell, append `&` to run a command in the **background**;
`Ctrl+Z` suspends the foreground job; `jobs` lists them; `fg`/`bg` resume a job in
the fore/background. `nohup command &` lets a job survive logout.

**Scheduling priority** is set by *niceness*, from `-20` (most favorable) to `19`
(least). Start a process nicer with `nice -n 10 backup.sh`; change a running one
with `renice -n 5 -p 4821`. Only root can assign a *negative* (higher-priority)
niceness.

## systemd: units, targets and services

Modern distributions use **systemd** as the init system, replacing the older
**SysVinit** scripts. systemd manages everything as **units** — services,
sockets, mounts, timers and more. Unit files shipped by packages live in
`/usr/lib/systemd/system/`; your overrides and custom units go in
`/etc/systemd/system/`, which wins.

### Targets replace runlevels

Where SysVinit had numbered **runlevels**, systemd has named **targets**:

| Target | Old runlevel | Purpose |
|--------|--------------|---------|
| `poweroff.target` | 0 | Halt |
| `rescue.target` | 1 | Single-user maintenance |
| `multi-user.target` | 3 | Full system, no GUI |
| `graphical.target` | 5 | Full system with GUI |
| `reboot.target` | 6 | Reboot |

Check or change the boot default with `systemctl get-default` and
`systemctl set-default multi-user.target`. Switch targets *now* without rebooting
with `systemctl isolate rescue.target`. `emergency.target` is an even more minimal
mode than rescue, with only the root filesystem mounted read-only.

### Managing services

```
$ sudo systemctl start sshd        # start now
$ sudo systemctl stop sshd         # stop now
$ sudo systemctl restart sshd      # stop then start
$ sudo systemctl reload sshd       # re-read config without dropping connections
$ sudo systemctl enable sshd       # start automatically at boot
$ sudo systemctl enable --now sshd # enable AND start in one step
$ systemctl status sshd            # state, PID, recent log lines
```

**`enable` and `start` are independent.** `enable` only sets the boot-time
behavior; `start` affects the current session. Use `enable --now` to do both.
After editing a unit file, run `systemctl daemon-reload` so systemd re-reads it.

systemd also captures logs in the **journal**. `journalctl -u sshd` shows one
service's logs; `journalctl -b` shows the current boot (`-b -1` the previous
boot); `journalctl -f` follows live. Persistent storage across reboots is enabled
by creating `/var/log/journal/` or setting `Storage=persistent` in
`/etc/systemd/journald.conf`.

## Exam focus

- Boot order: **firmware (BIOS/UEFI) → GRUB2 → kernel + initramfs → systemd (PID
  1) → target.** UEFI uses GPT and an EFI System Partition and can enforce Secure
  Boot.
- Edit `/etc/default/grub`, then regenerate the config (`grub2-mkconfig` /
  `update-grub`); never hand-edit `grub.cfg`.
- `modprobe` loads a module *with dependencies* (and `-r` unloads it); `insmod`/
  `rmmod` do not. Modules live under `/lib/modules/$(uname -r)`.
- `kill` defaults to **SIGTERM (15)**; **SIGKILL (9)** is the uncatchable force
  kill; **SIGHUP (1)** often means reload. Niceness runs `-20` (highest priority)
  to `19` (lowest).
- systemd **targets** replace runlevels: `multi-user.target` = 3 (no GUI),
  `graphical.target` = 5 (GUI), `rescue.target` = 1. `systemctl get-default` /
  `set-default` / `isolate`.
- **`enable` ≠ `start`**: enable is boot-time, start is now; `enable --now` does
  both. Run `daemon-reload` after editing a unit.
- Read logs with `journalctl -u <service>` and `journalctl -b`.
