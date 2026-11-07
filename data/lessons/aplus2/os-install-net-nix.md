# OS Installation, Networking & macOS/Linux

This lesson covers three practical skills a technician uses constantly: **getting
an OS onto a machine**, **plugging that machine into a network**, and **working on
the other two desktop families — macOS and Linux**. They look unrelated, but each
is mostly a short list of "when you see *this*, choose *that*."

## Installing Windows

### How the installer gets there (boot methods)

Before Setup can run, the PC has to boot the installer from somewhere:

- **USB flash drive** — the common modern method (bootable media).
- **Optical disc** — DVD, older but still tested.
- **Network / PXE** — the PC boots off a **deployment server** over the LAN with no
  local media at all. This is how you image **many** machines with blank drives.
- **Internet-based** — download and install over the internet.
- **Internal/external drive** — boot an image from another attached disk.

### Install types — the one the exam cares about

| Type | What it does |
|------|--------------|
| **Clean install** | wipes the target and installs fresh |
| **In-place upgrade** | installs over the existing Windows, **keeping apps + files** |
| **Repair install** | reinstalls Windows components to fix corruption, keeping data |
| **Image deployment** | lays down a prebuilt image (fast, identical PCs) |
| **Recovery partition** | restores from a hidden partition the vendor shipped |
| **Remote network (PXE)** | pulls the install from a server over the network |
| **Unattended** | Setup runs from an **answer file**, no prompts |

Two stems recur. "Windows is corrupted but the user must **keep all installed
applications and personal files**" → an **in-place upgrade / repair install** (not
a clean install, which would erase everything). "Deploy Windows to **50 PCs** with
blank drives and **no media**, pulling the image **over the network**" → a
**network (PXE) image deployment**. "Run Setup **without prompting** — auto-supply
language, key, partition choices, and account" → an **unattended installation**
driven by an answer file.

### GPT vs MBR partitioning

When you partition the target drive you pick a partition **style**, and this is a
guaranteed exam point:

> **MBR** tops out at **2 TB** and **4 primary partitions**, and goes with legacy
> **BIOS**. **GPT** supports drives **larger than 2 TB** and up to **128
> partitions**, and is **required for UEFI + Secure Boot**.

So a **clean install on a 4 TB drive** that must **boot UEFI with Secure Boot** has
exactly one right answer for partition style: **GPT** (MBR literally can't address
the whole 4 TB, and Secure Boot needs UEFI/GPT). After partitioning, you **format**
the volume — **NTFS** for a Windows system drive.

Finally, Windows updates come as small, frequent **quality updates** and larger,
twice-a-year **feature updates** (new build/features). Know the two terms apart.

## Windows networking

### Workgroup vs domain

- A **workgroup** is **peer-to-peer**: every PC keeps its **own** local accounts,
  there's no central control, and it suits small/home setups.
- A **domain** is **centralized**: an Active Directory **domain controller** holds
  the accounts and pushes policy, so settings apply to **every** PC. A 500-employee
  company that wants **central logon accounts and policies from a server** needs a
  **domain**.

### Network location profiles

Windows tags each network with a **profile** that decides how exposed you are:

- **Public** — assume hostile (coffee shop, airport). The PC is **not
  discoverable** and file/printer **sharing is off**. Pick this on untrusted Wi-Fi.
- **Private** — a trusted home/office LAN; discovery and sharing are allowed.
- **Domain** — applied automatically when the PC is on its corporate domain.

> On a coffee-shop network you want to be invisible → choose the **Public** profile.

### Sharing files and printers

To let others on a **trusted (Private) LAN** reach a printer attached to a Windows
PC, open **Network and Sharing Center → Advanced sharing settings** and turn on
**two** things: **Network discovery** (so the PC is visible) and **File and printer
sharing** (so the share is reachable). Both are required — discovery alone makes it
visible but not usable.

### Mapping a network drive

To attach a shared folder as a drive letter from the command line, use **`net
use`** with the **UNC path** (`\\server\share`):

```
net use S: \\fileserver\projects
```

That maps `\\fileserver\projects` to drive **S:**. (You can also do it in File
Explorer with *Map network drive*.)

### Remote access, briefly

**Remote Desktop Connection** (`mstsc`) takes full control of a remote host (which
must be Pro/Enterprise). **Remote Assistance (MSRA)** lets a helper *view/assist*
an active user session. A **VPN** tunnels you into the corporate network over the
internet, and **proxy** settings route web traffic through an intermediary.

## macOS and Linux essentials

### macOS features to recognize

| Feature | What it does |
|---------|--------------|
| **Time Machine** | built-in **backup** / restore earlier file versions |
| **FileVault** | **full-disk encryption** |
| **Gatekeeper** | blocks unsigned/un-notarized apps ("unidentified developer") |
| **Spotlight** | system-wide search |
| **Keychain** | stores passwords/certificates |
| **Finder** / **Dock** | file manager / app launcher bar |
| **Disk Utility** | format/partition/repair disks |

Three stems map straight to the table. "Restore a document deleted last week using
Apple's built-in backup" → **Time Machine**. "Built-in **full-disk encryption** on
a MacBook" → **FileVault**. "A downloaded app from an **unidentified developer** is
blocked" → **Gatekeeper**. macOS volumes use the **APFS** file system.

### Linux commands

The Linux command line is fair game on Core 2. The essentials:

| Command | Purpose |
|---------|---------|
| `ls` / `pwd` / `cd` | list files / print working dir / change dir |
| `cp` / `mv` / `rm` | copy / move / remove |
| `chmod` | change file **permissions** |
| `chown` | change file **owner** |
| `su` / `sudo` | switch user / run one command as **root** |
| `apt-get` (`apt`) | install packages on **Debian/Ubuntu** (`yum`/`dnf` on RHEL) |
| `grep` / `find` | search text / find files |
| `ps` / `top` | list processes / live resource view |
| `df` / `man` / `cat` | disk free / manual pages / print a file |

Two favorites. "**Debian/Ubuntu**, install a package **with its dependencies** from
the configured repositories" → **`apt-get install`** (or `apt install`). And
`sudo` is the one you prefix when a command needs root rights, e.g.
`sudo apt install`.

### chmod and the permission numbers

`chmod` can set permissions with **numbers**, and you'll be asked to read them.
Each of the three groups — **owner, group, everyone** — gets a digit that is the
sum of **read = 4, write = 2, execute = 1**:

> `rwx` = 4+2+1 = **7**, `r-x` = 4+0+1 = **5**, `r--` = **4**.

So **`rwxr-xr-x`** (owner full, group and others read+execute) is **`chmod 755`**.
And to simply make a downloaded script runnable, `chmod +x deploy.sh` adds the
execute bit. Linux file systems are typically **ext4** (older: ext3).

## The whole thing in one paragraph

Boot the Windows installer from USB, optical, or the **network (PXE)** for many
machines at once; choose an **in-place upgrade/repair** when apps and files must
survive, a **clean install** to wipe, and an **unattended** install (answer file)
to skip prompts. Partition large or UEFI/Secure-Boot drives as **GPT** (MBR caps at
2 TB / 4 primaries) and format NTFS. On the network, a **workgroup** is
peer-to-peer and a **domain** is centrally managed; set **Public** on untrusted
Wi-Fi; turn on **network discovery + file and printer sharing** to share; and map a
drive with `net use S: \\server\share`. On macOS know **Time Machine** (backup),
**FileVault** (encryption), and **Gatekeeper** (app signing); on Linux know
`chmod`/`chown`, `sudo`, and `apt-get install`, and read `rwxr-xr-x` as `755`.

## On the exam

- **In-place upgrade / repair install** keeps apps and data; **clean install**
  erases; **PXE/network image** deploys to many blank machines; **unattended** uses
  an answer file. Match the stem's constraint to the type.
- **GPT** for drives over **2 TB** and for **UEFI + Secure Boot**; **MBR** is the
  legacy-BIOS, 2 TB / 4-primary limit.
- **Public** profile hides the PC on untrusted networks; sharing needs **both**
  network discovery **and** file and printer sharing turned on.
- `net use <drive>: \\server\share` maps a network drive from the command line.
- macOS: **Time Machine** = backup, **FileVault** = full-disk encryption,
  **Gatekeeper** = signed-app enforcement. Linux: **`apt-get install`** on
  Debian/Ubuntu, `sudo` for root, and **`rwxr-xr-x` = `chmod 755`**.
