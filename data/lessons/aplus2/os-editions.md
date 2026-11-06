# Windows Editions & Core Features

Windows comes in a handful of **editions**, and they are not just different prices
for the same thing. Each edition unlocks a different set of features, and the exam
loves to ask "a PC needs to do *X* — which edition do you need?" So the trick is
not memorizing marketing names; it is knowing **which capability lives in which
edition**.

Here is the one idea to anchor on:

> **Home is the stripped-down consumer edition. The moment a business feature
> appears — joining a domain, BitLocker, Group Policy — you need Pro or higher.**

If you remember that single dividing line, most edition questions answer
themselves.

## The four editions, by what they can do

| Feature | Home | Pro | Pro for Workstations | Enterprise |
|---------|:----:|:---:|:--------------------:|:----------:|
| Join an Active Directory **domain** | ✗ | ✓ | ✓ | ✓ |
| **BitLocker** drive encryption | ✗ | ✓ | ✓ | ✓ |
| **Group Policy Editor** (`gpedit.msc`) | ✗ | ✓ | ✓ | ✓ |
| Host **Remote Desktop** (accept RDP in) | ✗ | ✓ | ✓ | ✓ |
| **Hyper-V** (built-in hypervisor) | ✗ | ✓ | ✓ | ✓ |
| **ReFS**, up to 4 CPU sockets, ~6 TB RAM | ✗ | ✗ | ✓ | ✓ |
| Volume licensing, AppLocker, BranchCache | ✗ | ✗ | ✗ | ✓ |

Read the table top to bottom and you can see the "shape" of each edition.

**Home** is for a single person at home. It can't join a company domain, has no
BitLocker, and has no local Group Policy Editor. A Home PC *can* be the **client**
in a Remote Desktop session (you can reach out from it), but it can't be the
**host** that accepts an incoming connection.

**Pro** is the everyday business edition. It adds the whole "managed by an
organization" toolkit — domain join, BitLocker, `gpedit.msc`, RDP hosting and
Hyper-V. When a question describes a work laptop that must join the domain and be
encrypted, **Pro is the floor**.

**Pro for Workstations** is for heavy engineering/server-class desktops. Its
signature extras are the **ReFS** file system, support for up to **4 physical CPU
sockets**, and enormous RAM (up to ~6 TB). If a stem lists ReFS, 4 sockets, or
multi-terabyte RAM, that is the fingerprint of Pro for Workstations.

**Enterprise** is Pro plus large-organization management features (AppLocker,
BranchCache, DirectAccess) and is sold through **volume licensing**, not at retail.

> **Exam shortcut:** domain join + BitLocker + `gpedit.msc` = at least **Pro**.
> ReFS / 4 sockets / 6 TB RAM = **Pro for Workstations**. Volume-licensed, biggest
> management feature set = **Enterprise**.

## A word about 32-bit vs 64-bit

You'll meet a classic trap: a PC has, say, **16 GB of RAM installed**, but the
System page reports only about **3.5 GB usable**. Nothing is broken — the machine
is running a **32-bit (x86) edition of Windows**, and 32-bit Windows can only
address about **4 GB** of memory total (and shows less as usable).

> A **32-bit** OS maxes out near **4 GB** of addressable RAM. To actually use 8,
> 16, or 32 GB you must install a **64-bit (x64)** edition.

64-bit Windows also runs 32-bit apps fine, but a 32-bit OS cannot run 64-bit apps
and cannot see the extra memory. The fix for "only 3.5 GB usable" is to install
64-bit Windows — you cannot flip a switch; it requires a reinstall.

## File systems: NTFS, FAT32, and exFAT

Formatting a drive means choosing a **file system** — the scheme Windows uses to
lay out files. Three show up constantly, and each has a job.

| File system | File-size limit | Where it shines |
|-------------|-----------------|-----------------|
| **NTFS** | essentially unlimited | the default for the **Windows system drive**; the only one with permissions, encryption, compression and journaling |
| **FAT32** | **4 GB** per file | old and *extremely* compatible, but can't hold a single file over 4 GB |
| **exFAT** | essentially unlimited | the cross-platform pick for **flash drives / external media** shared between Windows and macOS |

**NTFS** is what Windows itself installs onto. It is the only one of the three that
supports **file permissions**, **EFS encryption**, **compression**, and a
**journal** that helps it recover from a crash. If data security or a Windows boot
volume is involved, the answer is NTFS.

**FAT32** is the lowest common denominator — nearly every device on earth can read
it — but it chokes on any single file **larger than 4 GB**. That limit is the
whole reason the exam mentions it.

**exFAT** was built to fix FAT32's limits for removable media. It handles huge
files and is read/write on **both Windows and macOS**, which makes it the right
choice for a USB stick that has to carry a 12 GB video between a PC and a Mac.

> A 12 GB file that must move between Windows and macOS on a flash drive → **exFAT**
> (FAT32 can't hold a >4 GB file; NTFS is awkward/read-only by default on macOS).

## NTFS permissions vs. share permissions

When a folder is shared on the network, **two** separate permission sets apply: the
**share permission** (set on the shared folder) and the underlying **NTFS
permission** (set on the file/folder itself). People get this backwards constantly,
so here is the rule in one line:

> **Over the network, the effective permission is the *most restrictive* of the
> share permission and the NTFS permission.** Locally (sitting at the machine),
> only **NTFS** applies — share permissions are ignored.

Work an example. A user's group has **NTFS = Modify** but **Share = Read** on the
same folder. They open it **across the network**. Which wins? You take the more
restrictive of the two, so the user effectively gets **Read**. The generous NTFS
Modify is capped by the stingy Share Read.

Flip it around and the rule still holds: NTFS **Read** with Share **Full Control**
also lands on **Read**, because Read is the tighter of the two.

## UAC: the "are you sure?" prompt

**User Account Control (UAC)** is the feature that **dims the screen** (that's the
*secure desktop*) and asks for consent or an administrator password whenever a
program tries to make a system-level change — installing software, editing
protected settings, and so on. It exists so that even an administrator runs with
standard privileges until a change actually needs elevation, which blunts malware
that tries to silently reconfigure the machine.

> Screen dims + "allow this app to make changes?" prompt = **UAC** doing its job.

## EFS: encrypt a few files, not the whole disk

**EFS (Encrypting File System)** encrypts **individual files or folders** on an
NTFS volume, tied to your Windows user account — only that account can read them.
Contrast it with BitLocker, which encrypts the **entire volume**. If the ask is
"encrypt just these couple of folders so only my account can open them," that's
**EFS**; if it's "encrypt the whole drive," that's **BitLocker**.

## System Restore: a time machine for the OS (not your files)

Before a risky change — a questionable driver, a new app — you want an undo button.
**System Restore** creates a **restore point** and can roll back **system files,
drivers, and the registry** to an earlier moment.

> **System Restore rewinds the *system* (files, drivers, registry) but leaves your
> personal documents alone.** It is not a backup of your data.

So "I want to be able to undo this driver install without losing my files" →
create a restore point first, and use System Restore if it goes wrong.

## The whole thing in one paragraph

Windows editions differ by capability: **Home** is consumer-only (no domain, no
BitLocker, no `gpedit.msc`, can't host RDP), **Pro** adds the business kit (domain
join, BitLocker, Group Policy, RDP host, Hyper-V), **Pro for Workstations** adds
ReFS / 4 sockets / ~6 TB RAM for heavy hardware, and **Enterprise** adds
large-org management via volume licensing. A 32-bit OS can only use ~4 GB of RAM,
so "16 GB installed, 3.5 GB usable" means install 64-bit. For file systems, NTFS
is the secure Windows default, FAT32 can't hold files over 4 GB, and exFAT is the
cross-platform choice for big files on removable media. Network access is governed
by the **most restrictive** of share vs. NTFS permissions (NTFS alone applies
locally); UAC is the elevation prompt that dims the screen; EFS encrypts chosen
files while BitLocker encrypts whole volumes; and System Restore rolls back the
system without touching your documents.

## On the exam

- Map the capability to the edition: **domain join / BitLocker / `gpedit.msc` /
  RDP host / Hyper-V → Pro or higher**; **ReFS, 4 CPU sockets, ~6 TB RAM → Pro for
  Workstations**; **volume-licensed, most features → Enterprise**.
- "RAM installed but not usable" is almost always a **32-bit OS** — the fix is a
  **64-bit** reinstall.
- File-system picks are decided by the clue: **>4 GB file on a flash drive shared
  with macOS → exFAT**; **a single >4 GB file on FAT32 → impossible**; **Windows
  boot/secure volume → NTFS**.
- For share vs. NTFS questions, **take the more restrictive permission** for
  network access; remember share permissions don't apply when you're sitting at the
  machine.
- Know the one-liners cold: **UAC** = elevation/consent prompt, **EFS** = encrypt
  individual files, **BitLocker** = encrypt the whole volume, **System Restore** =
  roll back system/drivers/registry (not personal files).
