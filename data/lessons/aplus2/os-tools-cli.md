# Windows Tools & the Command Line

Windows ships with a drawer full of small, single-purpose tools, plus a command
line that can do things no amount of clicking will. The exam rarely asks what a
tool *is* — it hands you a symptom and asks **which tool or command you reach
for**. So the goal here is to pair each problem with its instrument.

A good way to think about it:

> **The graphical tools each own one job (drivers, disks, logs, startup). The
> command line is where you repair the OS itself and script repetitive work.**

## The graphical tools, matched to their jobs

Most of these open from the Start search box, from `Win+X`, or by typing their
**`.msc`** name into Run (`Win+R`). Learn the names in both forms.

**Device Manager (`devmgmt.msc`)** manages **hardware and drivers**. A device with
a **yellow exclamation mark** has a driver problem; this is where you go to update
the driver, roll it back, disable the device, or uninstall it. New webcam showing a
yellow `!`? Device Manager.

**Task Manager (`Ctrl+Shift+Esc`)** shows running processes and live performance,
and — importantly for the exam — its **Startup tab** lists each auto-start program
with a **"Startup impact"** rating and lets you **enable/disable** it. That
startup-management job used to live in `msconfig`; in Windows 10/11 it **moved to
Task Manager**.

**System Configuration (`msconfig`)** is the boot-and-startup troubleshooter. Its
**Boot tab** has a **"Safe boot"** checkbox that makes the PC restart straight into
**Safe Mode** next time. Its **General tab** offers *Selective startup* for a
**clean boot** (disable third-party services/startup items to isolate a conflict).

**Event Viewer (`eventvwr.msc`)** is the **log book**. It records **timestamped**
System, Application, and Security entries — Information, **Warning**, and **Error**
levels. After an unexpected reboot or crash, this is where you read what Windows
logged, and when.

**Disk Management (`diskmgmt.msc`)** manages **drives, partitions, and volumes**. A
brand-new SSD that doesn't show up in File Explorer usually needs to be brought
**online**, **initialized**, then have a **partition created and formatted** — all
right here.

**Registry Editor (`regedit`)** edits the **registry**, Windows' central settings
database. Powerful and unforgiving — a bad edit can break the OS — so you back up
(export) a key before changing it.

A few more worth recognizing by name:

| Tool | Opens with | What it's for |
|------|------------|---------------|
| System Information | `msinfo32` | read-only summary of hardware/OS |
| Resource Monitor | `resmon` | deep live view of CPU/disk/net/memory |
| Performance Monitor | `perfmon.msc` | long-term performance counters |
| Local Users and Groups | `lusrmgr.msc` | manage local accounts/groups |
| Task Scheduler | `taskschd.msc` | run tasks on a schedule/trigger |
| Disk Cleanup | `cleanmgr` | reclaim space (temp files, etc.) |
| Certificate Manager | `certmgr.msc` | view/manage certificates |

> **Quick matches:** driver trouble → **Device Manager**; too many startup apps →
> **Task Manager** (Startup tab); force Safe Mode next boot → **msconfig**; read
> crash/error history → **Event Viewer**; new disk not showing → **Disk
> Management**.

## The command line: repair and automation

Open **Command Prompt** or **PowerShell**, and for repair commands run it **as
administrator** ("elevated"). The exam leans on a specific handful.

### Fixing a sick Windows

Three repair commands come as a chain, and the **order matters**:

1. **`sfc /scannow`** — *System File Checker*. Scans **protected system files** and
   repairs corrupted ones from a local cache. First thing to try when Windows acts
   strangely or system DLLs go missing.
2. **`DISM /Online /Cleanup-Image /RestoreHealth`** — repairs the **component
   store** (the cache that `sfc` restores *from*). If `sfc` reports *"found corrupt
   files but was unable to fix some of them,"* the store itself is damaged — run
   **DISM** to repair it, then run `sfc /scannow` again.
3. **`chkdsk`** — *Check Disk*. `chkdsk /f` fixes file-system errors; **`chkdsk /r`
   locates bad sectors and recovers readable information** from a failing drive.

> If `sfc` can't fix everything → repair the store with **DISM**, then re-run
> `sfc`. Physical bad sectors on an aging drive → **`chkdsk /r`**.

### Network commands

- **`ipconfig`** shows IP settings. `ipconfig /flushdns` **clears the DNS resolver
  cache** — the fix when a site moved to a new IP but one PC still hits the old
  address from a stale cached lookup. (`/release` and `/renew` cycle a DHCP lease.)
- **`ping`** tests reachability; **`tracert`** traces the hops to a destination;
  **`nslookup`** queries DNS; **`netstat`** lists active connections;
  **`hostname`** prints the computer name.

### Files and folders

- Navigate with **`cd`** (change directory), list with **`dir`**, make a folder
  with **`md`**, remove one with **`rmdir`** (`rd`).
- Plain **`copy`** moves files but **not** subfolders. To copy a **directory tree
  including all subfolders**, use **`xcopy`** (with `/s` or `/e`) or **`robocopy`**
  — those are the two commands that walk subdirectories. Robocopy is the modern,
  more capable one (resumable, mirroring).

### Policy, disks, and the rest

- **`gpupdate /force`** reapplies **Group Policy** immediately; **`gpresult`** shows
  which policies are currently applied to the user/computer.
- **`diskpart`** is the command-line partition manager; **`format`** formats a
  volume; **`shutdown`** powers off/restarts (handy with switches in scripts);
  **`winver`** reports the exact Windows version/build.
- **`net user`** manages local accounts; **`net use`** maps network drives.
- Stuck on a command's options? Append **`/?`** — for example `robocopy /?` — to
  print its built-in help.

## The whole thing in one paragraph

Each graphical tool owns a lane: **Device Manager** for drivers (the yellow `!`),
**Task Manager** for the Startup tab and live performance, **msconfig** for forcing
**Safe boot** and clean boots, **Event Viewer** for the timestamped error log,
**Disk Management** for bringing a new disk online/initializing/formatting, and
**regedit** for the registry. On the command line, repair Windows with
`sfc /scannow`, escalate to **`DISM ... /RestoreHealth`** when `sfc` can't finish,
and use **`chkdsk /r`** for bad sectors; fix stale name resolution with
`ipconfig /flushdns`; copy whole folder trees with **`xcopy`** or **`robocopy`**;
and manage policy and disks with `gpupdate` / `gpresult` and `diskpart`.

## On the exam

- Memorize the symptom-to-tool pairings: **yellow `!` driver → Device Manager**,
  **disable startup apps → Task Manager**, **Safe boot checkbox → msconfig**,
  **read error/warning history → Event Viewer**, **new disk missing → Disk
  Management**.
- The repair chain is a favorite: **`sfc /scannow`** first; if it **can't fix some
  files**, run **`DISM /Online /Cleanup-Image /RestoreHealth`** then `sfc` again.
- **`chkdsk /r`** = bad sectors / recover readable data; **`ipconfig /flushdns`** =
  clear the cached DNS entry after an IP change.
- "Copy a folder **and all subfolders**" → the two answers are **`xcopy`** and
  **`robocopy`** (plain `copy` won't do subdirectories).
- Know the Run names: `devmgmt.msc`, `diskmgmt.msc`, `eventvwr.msc`, `gpedit.msc`,
  plus `msconfig`, `msinfo32`, `resmon`, `regedit`.
