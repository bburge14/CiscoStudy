# Endpoint Technologies & OS Internals

Much of a SOC's work ends up on the endpoint — the laptop or server where an
attacker actually runs code. To investigate there you need two things: a map of
the **defensive technologies** that live on a host (and exactly what each one
does), and a working knowledge of the **operating-system internals** — Windows
and Linux — where attackers hide. This lesson builds both.

## Endpoint protection technologies

Several controls run *on the host itself*. The exam loves to test the precise
difference between them, especially **detect vs. prevent** and **allow vs.
block**.

> A **HIDS** *detects and alerts* on suspicious host activity but does **not**
> block it. A **HIPS** goes further and *actively blocks* the activity in real
> time. That detect-vs-prevent line is the classic exam trap.

- **Host-based IDS (HIDS)** — software on one host that watches its logs, file
  integrity, and process activity and **raises an alert** when it sees something
  suspicious. It observes; it does not stop the action.
- **Host-based IPS (HIPS)** — detects *and* **blocks** in real time, for example
  by terminating a process or dropping a connection as it happens.
- **Antivirus (legacy)** — identifies malware primarily by **matching files
  against a database of known signatures**. Fast and precise for known malware,
  blind to the brand-new (the same signature trade-off from Unit 2).
- **Endpoint Detection and Response (EDR)** — modern agent that continuously
  records endpoint activity (processes, network, file changes) and gives analysts
  detection, investigation, and response — a big step beyond signature antivirus.
- **Host-based firewall** — controls inbound/outbound connections for **one
  specific machine** using local rules.
- **File Integrity Monitoring (FIM)** — computes hashes of critical system files
  and re-checks them, alerting if a protected file changes unexpectedly.

### Allowlisting vs. blocklisting

Two opposite philosophies for controlling what may run:

- **Application allowlisting** (default-**deny**) — only explicitly approved
  programs may execute; everything else is blocked by default. Very strong, more
  administrative effort.
- **Application blocklisting** (default-**allow**) — everything runs *except*
  programs named on a prohibited list. Easier, but anything not on the list — including new malware — runs freely.

### Sandboxing

**Sandboxing** runs code in an **isolated, instrumented environment** separate
from production so its behavior can be watched safely. It appears in two senses:
an analyst detonating a suspicious attachment in a malware sandbox, and the
built-in **application sandboxing** that browsers, Java, and PDF readers use to
contain untrusted content so an exploit can't easily reach the rest of the
system.

## Windows internals for the analyst

You cannot hunt on Windows without knowing where the operating system keeps its
state.

> The **Windows Registry** is a hierarchical database that stores operating-system
> and application configuration — including the auto-start **Run** keys that
> malware abuses for persistence.

Key Windows artifacts and tools:

- **Registry** — configuration store; the `Run`/`RunOnce` keys and service
  entries are prime persistence spots to review.
- **Processes** — the running programs. **Task Manager** gives a quick triage
  view of processes, CPU/memory, services, and startup items.
- **NTFS** — the native, default Windows file system, supporting access control
  lists (ACLs) and **journaling**.
- **Autostart locations** — besides Run keys, attackers persist via a **service
  set to start automatically** or a **Scheduled Task** with a logon or boot
  trigger. When hunting persistence, these are the first places to look.

## Linux internals for the analyst

Linux has no central registry, which changes where you look.

> On Linux, most system and service **configuration lives in plain-text files,
> largely under `/etc`**, and the superuser account **`root` has UID 0** with
> unrestricted privileges.

Key Linux artifacts and commands:

- **`/etc`** — plain-text configuration for the system and services (no registry).
- **`/etc/passwd`** — traditional store of local user accounts: username, UID,
  GID, home directory, and login shell.
- **`root` (UID 0)** — the all-powerful administrative account; watch for
  unexpected UID-0 accounts or privilege escalation to it.
- **`ps`** — lists currently running processes so you can spot an unexpected one.
- **`cron` (crontab)** — schedules commands to run automatically; a common
  **persistence** mechanism worth reviewing.

### Windows vs. Linux at a glance

| Concept | Windows | Linux |
|---------|---------|-------|
| Configuration store | Registry | Plain-text files under `/etc` |
| Default file system | NTFS | ext4 / xfs (and others) |
| Admin account | Administrator | `root` (UID 0) |
| List processes | Task Manager | `ps` |
| Scheduled execution | Scheduled Tasks | `cron` |
| Local accounts | SAM / Registry | `/etc/passwd` (+ `/etc/shadow`) |

Knowing this table turns "the host looks weird" into specific checks: *is there a
new Run key or service? an odd scheduled task or cron job? an unexpected UID-0
account?* Those are the questions host-based analysis answers.

## Exam focus

- **HIDS detects/alerts only; HIPS detects and blocks.** That is the most-tested
  distinction. **EDR** = continuous recording + detection/response, beyond legacy
  antivirus (which works by **signature matching**).
- **Application allowlisting** = default-deny (only approved apps run);
  **blocklisting** = default-allow (everything but the banned list). **FIM**
  watches for changes to critical files via hashing.
- **Sandboxing** = isolated environment to observe/contain untrusted code (both
  malware detonation and in-app containment).
- **Windows**: the **Registry** stores config; **Run keys**, auto-start
  **services**, and **Scheduled Tasks** are persistence spots; **NTFS** is the
  file system; **Task Manager** triages processes.
- **Linux**: config is plain text under **`/etc`**; **`/etc/passwd`** holds
  accounts; **`root` is UID 0**; **`ps`** lists processes; **`cron`** schedules
  jobs (a persistence spot).
