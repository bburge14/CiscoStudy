"""CompTIA A+ Core 2 (220-1102) — Domain 1.0 Operating Systems EXPANSION pool.

Original, objective-aligned questions that deepen the base ``operating_systems``
bank in ``content_aplus2.py`` (items ``aplus2-os-001``..``aplus2-os-008``) toward
real exam depth. Same authoring rules as the other pools: original content mapped
to the public 220-1102 objectives, never real exam items. build_content.py
shuffles option order, so the answer key here is not positionally biased.

IDs continue from ``aplus2-os-101`` to avoid colliding with the base pool.
"""

QUESTIONS = [
    # ===== windows_editions =================================================
    {
        "id": "aplus2-os-101", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A remote employee must connect INTO their office PC using Remote Desktop "
                "(RDP) so the office machine acts as the host that accepts the incoming "
                "session. What is the MINIMUM Windows 10/11 edition the office PC needs?",
        "options": [
            {"id": "A", "text": "Windows Pro"},
            {"id": "B", "text": "Windows Home"},
            {"id": "C", "text": "Windows Enterprise"},
            {"id": "D", "text": "Windows Pro for Workstations"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Hosting incoming Remote Desktop sessions (the RDP server role) first "
                       "appears in Windows Pro, so Pro is the minimum edition for the office PC.",
            "distractors": {
                "B": "Home can only run the Remote Desktop CLIENT (connect OUT); it cannot accept "
                     "incoming RDP sessions, so it can't be the host.",
                "C": "Enterprise can host RDP but is volume-licensed with extra features — it exceeds the MINIMUM.",
                "D": "Pro for Workstations also hosts RDP but adds server-grade hardware/ReFS support you don't need here.",
            },
            "exam_pattern": "Any Windows edition can be an RDP CLIENT; only Pro and above can be the RDP HOST.",
        },
    },
    {
        "id": "aplus2-os-102", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to run virtual machines using the hypervisor that is built "
                "into Windows rather than installing a third-party product. Their PC currently "
                "runs Windows 11 Home. What is the MINIMUM edition that includes this built-in hypervisor?",
        "options": [
            {"id": "A", "text": "Windows Pro"},
            {"id": "B", "text": "Windows Home"},
            {"id": "C", "text": "Windows Education"},
            {"id": "D", "text": "Windows Enterprise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Client Hyper-V, the hypervisor built into Windows, is available starting in "
                       "Windows Pro (64-bit), so Pro is the minimum edition that provides it.",
            "distractors": {
                "B": "Windows Home does NOT include Hyper-V; the feature isn't present to turn on.",
                "C": "Education includes Hyper-V but is a volume-licensed edition beyond the minimum.",
                "D": "Enterprise also includes Hyper-V but exceeds the minimum Pro requirement.",
            },
            "exam_pattern": "Hyper-V (client) = Pro / Enterprise / Education / Pro for Workstations — never Home.",
        },
    },
    {
        "id": "aplus2-os-103", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 3, "type": "mcq",
        "stem": "A workstation has 16 GB of RAM physically installed, but the System page reports "
                "only about 3.5 GB is usable and the OS cannot address more. Which is the MOST "
                "likely cause?",
        "options": [
            {"id": "A", "text": "A 32-bit (x86) version of Windows is installed"},
            {"id": "B", "text": "The edition is Windows Home, which caps RAM at 4 GB"},
            {"id": "C", "text": "BitLocker reserves the remaining RAM for encryption"},
            {"id": "D", "text": "One memory module is faulty and must be replaced"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A 32-bit edition of Windows can address only about 4 GB of memory total "
                       "(~3.2-3.5 GB usable), so extra installed RAM is ignored. Moving to 64-bit "
                       "Windows removes the limit — which requires a clean install, not an in-place change.",
            "distractors": {
                "B": "Windows Home (64-bit) supports up to 128 GB, not 4 GB — the edition isn't the cap here.",
                "C": "BitLocker encrypts the drive and does not reserve gigabytes of RAM.",
                "D": "A faulty module would reduce total RAM but wouldn't impose a clean ~4 GB addressing ceiling the way an x86 OS does.",
            },
            "exam_pattern": "~4 GB usable ceiling regardless of installed RAM = 32-bit (x86) Windows; 32->64-bit needs a clean install.",
        },
    },
    {
        "id": "aplus2-os-104", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 3, "type": "mcq",
        "stem": "An engineering workstation needs the ReFS file system, support for up to 4 physical "
                "CPU sockets, and very large RAM capacity (up to 6 TB). Which Windows edition is "
                "specifically designed to provide this high-end hardware and resilient-storage support?",
        "options": [
            {"id": "A", "text": "Windows Pro for Workstations"},
            {"id": "B", "text": "Windows Pro"},
            {"id": "C", "text": "Windows Home"},
            {"id": "D", "text": "Windows Enterprise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Pro for Workstations targets high-end hardware: it supports ReFS, up to 4 CPU "
                       "sockets and up to 6 TB of RAM (plus persistent memory and SMB Direct).",
            "distractors": {
                "B": "Pro supports only 2 CPU sockets and up to 2 TB RAM and does not create ReFS volumes.",
                "C": "Home is a consumer edition (1 socket, 128 GB RAM cap) and far below these needs.",
                "D": "Enterprise is volume-licensed for management/security features but still supports only 2 CPU sockets — not the 4-socket workstation hardware.",
            },
            "exam_pattern": "ReFS + 4 CPU sockets + 6 TB RAM = Pro for Workstations; Pro caps at 2 sockets / 2 TB and no ReFS.",
        },
    },

    # ===== windows_tools ====================================================
    {
        "id": "aplus2-os-105", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 2, "type": "mcq",
        "stem": "A technician wants Windows to restart directly into Safe Mode on the next boot "
                "using the built-in GUI utility whose Boot tab has a 'Safe boot' checkbox. Which "
                "tool should they open?",
        "options": [
            {"id": "A", "text": "System Configuration (msconfig)"},
            {"id": "B", "text": "Registry Editor (regedit)"},
            {"id": "C", "text": "Services (services.msc)"},
            {"id": "D", "text": "Task Manager (taskmgr)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System Configuration (msconfig) has a Boot tab with a 'Safe boot' option that "
                       "forces the next restart into Safe Mode.",
            "distractors": {
                "B": "regedit edits the registry directly; it isn't the GUI for choosing a Safe Mode boot.",
                "C": "services.msc starts/stops Windows services — it has no boot-mode setting.",
                "D": "Task Manager manages processes and startup apps; the Safe boot option lives in msconfig, not here.",
            },
            "exam_pattern": "Safe boot / boot options = msconfig (Boot tab). Startup apps moved to Task Manager; services = services.msc.",
        },
    },
    {
        "id": "aplus2-os-106", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 1, "type": "mcq",
        "stem": "After a PC reboots unexpectedly, a technician wants to review timestamped System "
                "and Application error and warning entries that Windows logged. Which built-in tool "
                "displays these logs?",
        "options": [
            {"id": "A", "text": "Event Viewer (eventvwr.msc)"},
            {"id": "B", "text": "Performance Monitor (perfmon)"},
            {"id": "C", "text": "Task Manager (taskmgr)"},
            {"id": "D", "text": "Device Manager (devmgmt.msc)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event Viewer stores Windows Logs (System, Application, Security, etc.) with "
                       "timestamps and severity, the right place to review errors after a crash.",
            "distractors": {
                "B": "Performance Monitor graphs live and logged performance counters, not system event logs.",
                "C": "Task Manager shows current processes and resource use, not the historical event log.",
                "D": "Device Manager manages hardware/drivers; it doesn't display System/Application logs.",
            },
            "exam_pattern": "Review logged events = Event Viewer; live performance = Performance/Resource Monitor; hardware = Device Manager.",
        },
    },
    {
        "id": "aplus2-os-107", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 2, "type": "mcq",
        "stem": "A newly installed second SSD does not appear in File Explorer. Which built-in "
                "Windows tool is used to bring the disk online, initialize it, and create and format "
                "a new volume with a drive letter?",
        "options": [
            {"id": "A", "text": "Disk Management (diskmgmt.msc)"},
            {"id": "B", "text": "Device Manager (devmgmt.msc)"},
            {"id": "C", "text": "System Information (msinfo32)"},
            {"id": "D", "text": "Disk Cleanup (cleanmgr)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Disk Management initializes new disks and creates, formats and assigns drive "
                       "letters to volumes, which makes the SSD usable and visible in File Explorer.",
            "distractors": {
                "B": "Device Manager confirms the disk's driver/hardware is recognized but does not create or format volumes.",
                "C": "System Information (msinfo32) is a read-only summary of the system — it changes nothing on disk.",
                "D": "Disk Cleanup removes temporary files to free space; it doesn't initialize or format disks.",
            },
            "exam_pattern": "Initialize/partition/format/assign letters = Disk Management (GUI) or diskpart (CLI).",
        },
    },
    {
        "id": "aplus2-os-108", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 2, "type": "mcq",
        "stem": "On Windows 10/11, which built-in tool has a Startup tab that shows each startup "
                "program's 'Startup impact' and lets you enable or disable it (functionality that "
                "moved here from System Configuration)?",
        "options": [
            {"id": "A", "text": "Task Manager (taskmgr)"},
            {"id": "B", "text": "System Configuration (msconfig)"},
            {"id": "C", "text": "Registry Editor (regedit)"},
            {"id": "D", "text": "Services (services.msc)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Since Windows 8, startup-app management (with a 'Startup impact' rating) lives on "
                       "the Task Manager Startup tab, where you can disable unneeded auto-start programs.",
            "distractors": {
                "B": "msconfig's Startup tab now just links out to Task Manager; the actual control moved there.",
                "C": "regedit can show Run keys but has no 'Startup impact' rating or simple enable/disable toggle.",
                "D": "services.msc manages background services, which are different from per-user startup applications.",
            },
            "exam_pattern": "Startup apps = Task Manager (Startup tab) in Win8+; msconfig still owns boot options, not startup apps.",
        },
    },

    # ===== command_line =====================================================
    {
        "id": "aplus2-os-109", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "mcq",
        "stem": "A website changed its IP address, but one workstation still connects to the old "
                "address because of a stale cached name resolution. Which command clears the local "
                "DNS resolver cache?",
        "options": [
            {"id": "A", "text": "ipconfig /flushdns"},
            {"id": "B", "text": "ipconfig /release"},
            {"id": "C", "text": "ipconfig /renew"},
            {"id": "D", "text": "ipconfig /all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ipconfig /flushdns empties the local DNS resolver cache, forcing a fresh lookup "
                       "that picks up the new IP address.",
            "distractors": {
                "B": "ipconfig /release drops the current DHCP lease (IP address); it doesn't touch the DNS cache.",
                "C": "ipconfig /renew requests a new DHCP lease; it doesn't clear cached DNS records.",
                "D": "ipconfig /all only displays the full IP configuration; it changes nothing.",
            },
            "exam_pattern": "Stale name resolution = ipconfig /flushdns; DHCP lease issues = /release then /renew.",
        },
    },
    {
        "id": "aplus2-os-110", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "mcq",
        "stem": "A technician suspects an aging hard drive has physical bad sectors. Which command "
                "locates bad sectors and attempts to recover any readable information (while also "
                "fixing file-system errors)?",
        "options": [
            {"id": "A", "text": "chkdsk /r"},
            {"id": "B", "text": "chkdsk /f"},
            {"id": "C", "text": "sfc /scannow"},
            {"id": "D", "text": "format C:"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chkdsk /r locates bad sectors and recovers readable information; it implies /f, "
                       "so it fixes file-system errors too.",
            "distractors": {
                "B": "chkdsk /f fixes file-system errors but does NOT scan the surface for bad sectors.",
                "C": "sfc /scannow repairs protected Windows system files, not disk sectors.",
                "D": "format erases the volume and recreates the file system — it destroys data rather than recovering it.",
            },
            "exam_pattern": "/f = fix file-system errors; /r = /f PLUS locate bad sectors and recover readable data.",
        },
    },
    {
        "id": "aplus2-os-111", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 3, "type": "mcq",
        "stem": "sfc /scannow reports that it found corrupt files but 'was unable to fix some of "
                "them.' Which command repairs the underlying Windows component store so a follow-up "
                "sfc run can succeed?",
        "options": [
            {"id": "A", "text": "DISM /Online /Cleanup-Image /RestoreHealth"},
            {"id": "B", "text": "sfc /verifyonly"},
            {"id": "C", "text": "chkdsk /r"},
            {"id": "D", "text": "bootrec /fixmbr"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DISM /Online /Cleanup-Image /RestoreHealth repairs the component store (the source "
                       "sfc copies known-good files from), so re-running sfc afterward can complete repairs.",
            "distractors": {
                "B": "sfc /verifyonly only checks integrity and reports; it makes no repairs.",
                "C": "chkdsk /r fixes disk/file-system problems and bad sectors, not the Windows image/component store.",
                "D": "bootrec /fixmbr repairs the master boot record for boot problems — unrelated to corrupt system files.",
            },
            "exam_pattern": "sfc can't fix it -> DISM /Online /Cleanup-Image /RestoreHealth, then run sfc /scannow again.",
        },
    },
    {
        "id": "aplus2-os-112", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "multi",
        "stem": "A technician needs to copy a folder AND all of its subfolders from the Windows "
                "command line. Which TWO commands can copy a directory tree including subdirectories? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "robocopy"},
            {"id": "B", "text": "xcopy /E"},
            {"id": "C", "text": "copy"},
            {"id": "D", "text": "move"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "robocopy (robust file copy) copies directory trees and is the modern tool, and "
                       "xcopy /E copies folders including subdirectories (even empty ones).",
            "distractors": {
                "C": "copy transfers individual files only — it cannot recurse into subdirectories.",
                "D": "move relocates files/folders (and deletes the source); it is not a copy command.",
            },
            "exam_pattern": "Copy directory trees = robocopy (preferred) or xcopy /E (/S excludes empty dirs); copy = single files.",
        },
    },

    # ===== os_features ======================================================
    {
        "id": "aplus2-os-113", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 3, "type": "mcq",
        "stem": "A user's group is granted the share permission 'Read' on a folder, while the NTFS "
                "permission for that group on the same folder is 'Modify.' When the user opens the "
                "folder OVER THE NETWORK, what is their effective permission?",
        "options": [
            {"id": "A", "text": "Read"},
            {"id": "B", "text": "Modify"},
            {"id": "C", "text": "Full Control"},
            {"id": "D", "text": "No access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Over the network both share and NTFS permissions apply, and the effective result "
                       "is the MOST RESTRICTIVE of the two. Share Read is more restrictive than NTFS "
                       "Modify, so the user gets Read.",
            "distractors": {
                "B": "Modify is the NTFS level, but the Read share permission caps network access below it.",
                "C": "Full Control is granted by neither permission here.",
                "D": "Access isn't denied — Read is allowed; logging on locally would even bypass the share and give Modify.",
            },
            "exam_pattern": "Share + NTFS over the network = most restrictive wins; local logon ignores share permissions.",
        },
    },
    {
        "id": "aplus2-os-114", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 1, "type": "mcq",
        "stem": "When a standard user launches a program that needs to make system changes, Windows "
                "dims the screen and prompts for administrator approval or credentials before "
                "continuing. Which feature produces this prompt?",
        "options": [
            {"id": "A", "text": "User Account Control (UAC)"},
            {"id": "B", "text": "BitLocker"},
            {"id": "C", "text": "Encrypting File System (EFS)"},
            {"id": "D", "text": "Windows Defender Firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "User Account Control (UAC) uses the secure (dimmed) desktop to request consent or "
                       "admin credentials before an action that requires elevation proceeds.",
            "distractors": {
                "B": "BitLocker encrypts drives; it doesn't produce elevation consent prompts.",
                "C": "EFS encrypts individual files per user; it isn't the elevation prompt mechanism.",
                "D": "Windows Defender Firewall filters network traffic, not application elevation.",
            },
            "exam_pattern": "Dimmed secure desktop + admin consent prompt = UAC (elevation).",
        },
    },
    {
        "id": "aplus2-os-115", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "A user wants to encrypt a few specific files and folders on an NTFS volume so that "
                "only their Windows account can read them, without encrypting the entire drive. Which "
                "feature should they use?",
        "options": [
            {"id": "A", "text": "Encrypting File System (EFS)"},
            {"id": "B", "text": "BitLocker"},
            {"id": "C", "text": "NTFS compression"},
            {"id": "D", "text": "BitLocker To Go"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EFS encrypts individual files/folders on NTFS, tied to the user's account key, so "
                       "only that user can decrypt them — exactly per-file, per-user protection.",
            "distractors": {
                "B": "BitLocker encrypts an ENTIRE volume, not selected files for a single user.",
                "C": "NTFS compression reduces file size; it provides no encryption or access protection.",
                "D": "BitLocker To Go encrypts entire REMOVABLE drives, again not individual files on a fixed disk.",
            },
            "exam_pattern": "Per-file/per-user encryption = EFS (NTFS); whole-volume encryption = BitLocker (removable = BitLocker To Go).",
        },
    },
    {
        "id": "aplus2-os-116", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "Before installing a questionable driver, a technician wants a quick way to later roll "
                "back system files, drivers, and the registry to an earlier point WITHOUT affecting the "
                "user's documents. Which Windows feature provides this?",
        "options": [
            {"id": "A", "text": "System Restore (restore points)"},
            {"id": "B", "text": "File History"},
            {"id": "C", "text": "Reset this PC"},
            {"id": "D", "text": "Disk Cleanup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System Restore (part of System Protection) creates restore points that revert system "
                       "files, drivers, and the registry to an earlier state while leaving personal files alone.",
            "distractors": {
                "B": "File History backs up and restores personal files/versions, not system files or the registry.",
                "C": "Reset this PC reinstalls Windows (optionally removing everything) — far more drastic than a rollback.",
                "D": "Disk Cleanup frees space by deleting temporary files; it can't roll the system back.",
            },
            "exam_pattern": "Roll back system state, keep user files = System Restore point; back up user files = File History.",
        },
    },

    # ===== os_installation ==================================================
    {
        "id": "aplus2-os-117", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 2, "type": "mcq",
        "stem": "Windows is misbehaving due to corrupted system files, but the user must keep all of "
                "their installed applications and personal files. Which installation approach meets "
                "this requirement?",
        "options": [
            {"id": "A", "text": "In-place upgrade (repair installation) of the same Windows version"},
            {"id": "B", "text": "Clean (custom) install"},
            {"id": "C", "text": "Reset this PC choosing 'Remove everything'"},
            {"id": "D", "text": "Format the drive and reinstall Windows"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An in-place upgrade / repair installation reinstalls Windows over itself, refreshing "
                       "system files while preserving installed applications and user data.",
            "distractors": {
                "B": "A clean (custom) install wipes the partition and keeps no apps or settings.",
                "C": "'Remove everything' deletes personal files and apps — the opposite of what's required.",
                "D": "Formatting and reinstalling destroys all apps and data on the volume.",
            },
            "exam_pattern": "Keep apps + files while repairing = in-place upgrade/repair install; clean install = wipe and start fresh.",
        },
    },
    {
        "id": "aplus2-os-118", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 2, "type": "mcq",
        "stem": "An administrator must deploy Windows to 50 new PCs that have blank drives and no "
                "installation media, pulling the OS image from a deployment server over the LAN as "
                "each PC powers on. Which boot method accomplishes this?",
        "options": [
            {"id": "A", "text": "PXE (network) boot"},
            {"id": "B", "text": "Optical (DVD) boot"},
            {"id": "C", "text": "USB flash drive boot"},
            {"id": "D", "text": "Internal recovery partition"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PXE (Preboot eXecution Environment) lets a network-enabled PC boot from a deployment "
                       "server over the LAN, ideal for imaging many machines with no local media.",
            "distractors": {
                "B": "Optical boot requires a disc in each machine and an optical drive — not a network deployment.",
                "C": "USB boot still requires physically inserting media into every PC, defeating 'no media.'",
                "D": "A recovery partition restores a single existing machine; new blank drives have none.",
            },
            "exam_pattern": "Image many diskless/new PCs from a server over the network = PXE boot.",
        },
    },
    {
        "id": "aplus2-os-119", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 3, "type": "mcq",
        "stem": "To make Windows Setup run without prompting a technician — automatically supplying "
                "the language, product key, partition choices, and account settings — which item "
                "provides those answers for an unattended installation?",
        "options": [
            {"id": "A", "text": "An answer file (unattend.xml / autounattend.xml)"},
            {"id": "B", "text": "A WIM image file"},
            {"id": "C", "text": "An FFU image file"},
            {"id": "D", "text": "An ISO disc image"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An unattended install uses an answer file (unattend.xml, named autounattend.xml on "
                       "boot media) that supplies the responses Setup would otherwise prompt for.",
            "distractors": {
                "B": "A WIM (Windows Imaging Format) file stores the captured OS image; it holds files, not the setup answers.",
                "C": "An FFU (Full Flash Update) image is a sector/disk image used to flash a drive — not the answer source.",
                "D": "An ISO is the installation media container; by itself it doesn't automate the prompts.",
            },
            "exam_pattern": "Automate Setup prompts = answer file (unattend.xml/autounattend.xml); WIM/FFU = image formats.",
        },
    },

    # ===== networking_os ====================================================
    {
        "id": "aplus2-os-120", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 1, "type": "mcq",
        "stem": "A user connects a Windows laptop to Wi-Fi at a coffee shop. Which network location "
                "profile should be selected so the laptop is NOT discoverable and file/printer sharing "
                "stays off?",
        "options": [
            {"id": "A", "text": "Public"},
            {"id": "B", "text": "Private"},
            {"id": "C", "text": "Domain"},
            {"id": "D", "text": "Metered"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Public profile hides the device from network discovery and keeps sharing off — "
                       "the correct choice on untrusted networks like a coffee shop.",
            "distractors": {
                "B": "Private is for trusted home/work networks and ENABLES discovery and sharing.",
                "C": "Domain is applied automatically only when the PC is joined to an Active Directory domain.",
                "D": "Metered is a data-usage setting to limit background traffic, not a discovery/sharing profile.",
            },
            "exam_pattern": "Untrusted network = Public (not discoverable); trusted = Private; AD-joined = Domain (automatic).",
        },
    },
    {
        "id": "aplus2-os-121", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "A 500-employee company wants centralized user logon accounts and policies managed "
                "from a server so settings apply to every PC. Which Windows networking model supports "
                "this centralized management?",
        "options": [
            {"id": "A", "text": "Domain (Active Directory)"},
            {"id": "B", "text": "Workgroup"},
            {"id": "C", "text": "HomeGroup"},
            {"id": "D", "text": "Public network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A domain uses Active Directory on a domain controller for centralized accounts and "
                       "Group Policy, scaling to hundreds or thousands of managed PCs.",
            "distractors": {
                "B": "A workgroup is peer-to-peer with separate local accounts on each PC — no central management, best for small groups.",
                "C": "HomeGroup was a simple home file/printer-sharing feature (now removed), not centralized enterprise management.",
                "D": "Public is a firewall/network-location profile, not an account-management model.",
            },
            "exam_pattern": "Centralized accounts + Group Policy on a server = Domain; peer-to-peer local accounts = Workgroup.",
        },
    },
    {
        "id": "aplus2-os-122", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "multi",
        "stem": "A technician wants other users on the trusted (private) LAN to reach a printer that "
                "is attached to a Windows PC. In Advanced sharing settings, which TWO options must be "
                "turned on? (Choose two.)",
        "options": [
            {"id": "A", "text": "File and printer sharing"},
            {"id": "B", "text": "Network discovery"},
            {"id": "C", "text": "Set the network profile to Public"},
            {"id": "D", "text": "Enable a metered connection"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Turning on File and printer sharing exposes the shared printer, and Network discovery "
                       "lets other PCs find the computer on the network so they can connect to it.",
            "distractors": {
                "C": "Setting the profile to Public would HIDE the PC and block sharing — the opposite of the goal.",
                "D": "A metered connection limits background data usage; it has nothing to do with printer sharing.",
            },
            "exam_pattern": "Share on a private LAN = enable Network discovery + File and printer sharing (and allow it through the firewall).",
        },
    },

    # ===== macos_linux ======================================================
    {
        "id": "aplus2-os-123", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "On a Mac, a downloaded app from an 'unidentified developer' is blocked from opening by "
                "default. Which macOS security feature enforces that only signed/notarized or App Store "
                "apps run unless the user overrides it?",
        "options": [
            {"id": "A", "text": "Gatekeeper"},
            {"id": "B", "text": "FileVault"},
            {"id": "C", "text": "Keychain"},
            {"id": "D", "text": "Time Machine"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Gatekeeper checks an app's signature/notarization and, by default, blocks apps from "
                       "unidentified developers until the user explicitly allows them.",
            "distractors": {
                "B": "FileVault is macOS full-disk encryption — it doesn't gate which apps may launch.",
                "C": "Keychain stores passwords, keys and certificates; it isn't the app-launch gatekeeper.",
                "D": "Time Machine is the backup utility, unrelated to app signing checks.",
            },
            "exam_pattern": "macOS app-launch allow/block by signature = Gatekeeper; disk encryption = FileVault.",
        },
    },
    {
        "id": "aplus2-os-124", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "A MacBook user wants built-in full-disk encryption so that data cannot be read if the "
                "laptop is lost or stolen. Which macOS feature provides this?",
        "options": [
            {"id": "A", "text": "FileVault"},
            {"id": "B", "text": "Gatekeeper"},
            {"id": "C", "text": "Disk Utility"},
            {"id": "D", "text": "Mission Control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FileVault encrypts the entire startup disk (XTS-AES), so the data is unreadable without "
                       "the account password/recovery key if the Mac is stolen.",
            "distractors": {
                "B": "Gatekeeper controls which apps are allowed to launch, not disk encryption.",
                "C": "Disk Utility formats, partitions and repairs disks (First Aid); it doesn't encrypt the whole system disk on its own.",
                "D": "Mission Control arranges windows, spaces and desktops — unrelated to encryption.",
            },
            "exam_pattern": "macOS full-disk encryption = FileVault (Windows equivalent = BitLocker).",
        },
    },
    {
        "id": "aplus2-os-125", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "On a Debian/Ubuntu-based Linux system, which command installs a software package along "
                "with its dependencies from the configured repositories?",
        "options": [
            {"id": "A", "text": "apt-get install"},
            {"id": "B", "text": "yum install"},
            {"id": "C", "text": "chmod"},
            {"id": "D", "text": "grep"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "apt-get (or apt) is the package manager for Debian/Ubuntu; 'apt-get install <pkg>' "
                       "downloads and installs a package and its dependencies from the repositories.",
            "distractors": {
                "B": "yum (and dnf) is the package manager for Red Hat/Fedora/CentOS family systems, not Debian/Ubuntu.",
                "C": "chmod changes file permission bits; it installs nothing.",
                "D": "grep searches text within files/output; it is not a package manager.",
            },
            "exam_pattern": "Debian/Ubuntu = apt/apt-get; Red Hat/Fedora/CentOS = yum/dnf.",
        },
    },
    {
        "id": "aplus2-os-126", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 3, "type": "mcq",
        "stem": "On Linux, a script should be readable, writable, and executable by its owner, and only "
                "readable and executable by the group and everyone else (rwxr-xr-x). Which chmod numeric "
                "(octal) mode sets exactly this?",
        "options": [
            {"id": "A", "text": "755"},
            {"id": "B", "text": "644"},
            {"id": "C", "text": "777"},
            {"id": "D", "text": "750"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Each digit sums read(4)+write(2)+execute(1): owner rwx = 7, group r-x = 5, others r-x = 5, "
                       "giving 755 (rwxr-xr-x).",
            "distractors": {
                "B": "644 is rw-r--r-- (no execute for anyone) — the script could not be run.",
                "C": "777 is rwxrwxrwx, granting write to group and others as well — too permissive.",
                "D": "750 is rwxr-x--- which removes all access for 'others,' not read+execute as required.",
            },
            "exam_pattern": "Octal permissions: r=4, w=2, x=1 per owner/group/other. rwxr-xr-x = 755; rw-r--r-- = 644.",
        },
    },
]
