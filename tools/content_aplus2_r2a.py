"""CompTIA A+ Core 2 (220-1102) deepening pool — round 2, part A (OS + Security).

Original, objective-aligned items that extend the A+ Core 2 bank toward CCNA-level
depth for two domains:
  * 1.0 Operating Systems (operating_systems) — +29, spread across all 7 subtopics
  * 2.0 Security          (security_a2)       — +21, spread across all 6 subtopics

Same authoring rules as the other pools: original content written to the public
220-1102 objectives, never real exam items. build_content.py shuffles option order
(seeded by id), so the answer key here is not positionally biased. IDs carry a
`-r2-` segment so they can never collide with the first-round aplus2 pools.
"""

QUESTIONS = [
    # =====================================================================
    # 1.0 OPERATING SYSTEMS
    # =====================================================================

    # ----- windows_editions ---------------------------------------------
    {
        "id": "aplus2-os-r2-001", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A technician tries to open the Local Group Policy Editor (gpedit.msc) to "
                "tighten a setting on a user's Windows 11 Home laptop, but Windows reports it "
                "cannot find gpedit.msc. What is the MOST likely reason?",
        "options": [
            {"id": "A", "text": "The Local Group Policy Editor is not included in the Home edition"},
            {"id": "B", "text": "The laptop must be joined to a domain before gpedit will run"},
            {"id": "C", "text": "gpedit.msc only launches from Safe Mode"},
            {"id": "D", "text": "The user is not signed in with a Microsoft account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "gpedit.msc ships only with Pro and higher editions. Windows Home has no "
                       "Local Group Policy Editor, so the file genuinely isn't present.",
            "distractors": {
                "B": "Domain join is itself a Pro+ capability; Home can't join a domain, and gpedit "
                     "is a LOCAL tool that doesn't require one anyway.",
                "C": "gpedit does not depend on Safe Mode — it simply isn't installed in Home.",
                "D": "A Microsoft vs. local account has no bearing on whether gpedit.msc exists.",
            },
            "exam_pattern": "Home edition lacks gpedit.msc, BitLocker, domain join, and the RDP host "
                            "role — those require Pro, Pro for Workstations, or Enterprise.",
        },
    },
    {
        "id": "aplus2-os-r2-002", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A video-editing workstation has 256 GB of RAM installed, but 64-bit Windows Home "
                "cannot use all of it. Which edition change lets Windows address far "
                "more memory (up to 2 TB)?",
        "options": [
            {"id": "A", "text": "Upgrade to Windows Pro"},
            {"id": "B", "text": "Reinstall Windows Home as the 32-bit version"},
            {"id": "C", "text": "No Windows edition supports more than 128 GB of RAM"},
            {"id": "D", "text": "Switch the PC into S mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "64-bit Windows Home caps at 128 GB of RAM; Windows Pro raises the ceiling to "
                       "2 TB (Pro for Workstations and Enterprise go to 6 TB), so a Pro upgrade lets "
                       "the 256 GB be used.",
            "distractors": {
                "B": "32-bit Windows can address only ~4 GB total — far worse, not better.",
                "C": "False — Pro supports 2 TB and Pro for Workstations/Enterprise 6 TB.",
                "D": "S mode locks the PC to Store apps for security; it does not raise RAM limits.",
            },
            "exam_pattern": "64-bit RAM ceilings by edition: Home 128 GB, Pro 2 TB, Pro for "
                            "Workstations/Enterprise 6 TB. 32-bit any edition ≈ 4 GB.",
        },
    },
    {
        "id": "aplus2-os-r2-003", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 1, "type": "multi",
        "stem": "An administrator is choosing Windows editions for office desktops that MUST join "
                "the corporate Active Directory domain. Which TWO editions support joining a "
                "domain? (Choose two.)",
        "options": [
            {"id": "A", "text": "Windows Pro"},
            {"id": "B", "text": "Windows Enterprise"},
            {"id": "C", "text": "Windows Home"},
            {"id": "D", "text": "Windows Home Single Language"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Domain join is available in Pro, Pro for Workstations, and Enterprise. Pro "
                       "and Enterprise are the two listed that qualify.",
            "distractors": {
                "C": "Home cannot join a domain — it must first be upgraded to Pro.",
                "D": "Home Single Language is a Home variant and also cannot join a domain.",
            },
            "exam_pattern": "Domain join = Pro / Pro for Workstations / Enterprise. No Home edition "
                            "can join an Active Directory domain (workgroup only).",
        },
    },
    {
        "id": "aplus2-os-r2-004", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A user bought a PC preloaded with Windows 11 Home and now needs BitLocker and the "
                "ability to join the company domain, WITHOUT reinstalling or losing data. What is "
                "the correct approach?",
        "options": [
            {"id": "A", "text": "Perform an in-place edition upgrade to Windows 11 Pro (e.g., apply a Pro product key)"},
            {"id": "B", "text": "Download a third-party tool to add domain join to Home"},
            {"id": "C", "text": "Enable the features in Control Panel — they are present but hidden in Home"},
            {"id": "D", "text": "Reformat and perform a clean install of Windows Home again"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Home→Pro is an in-place edition upgrade (via the Microsoft Store or by "
                       "changing the product key) that keeps apps, files, and settings while "
                       "unlocking BitLocker, domain join, and gpedit.",
            "distractors": {
                "B": "Domain join is an edition capability, not a feature a third-party utility can bolt on.",
                "C": "These features are absent in Home, not merely hidden — nothing to enable.",
                "D": "Reinstalling Home yields the same missing features and wipes the user's data.",
            },
            "exam_pattern": "To gain Pro-only features without a wipe: in-place edition upgrade "
                            "(change product key / Store). Home never has BitLocker, domain join, or gpedit.",
        },
    },

    # ----- windows_tools ------------------------------------------------
    {
        "id": "aplus2-os-r2-005", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 2, "type": "mcq",
        "stem": "A vendor fix instructs a technician to change a specific value under the "
                "HKEY_LOCAL_MACHINE hive. Which built-in Windows tool edits the registry directly?",
        "options": [
            {"id": "A", "text": "Registry Editor (regedit)"},
            {"id": "B", "text": "Device Manager"},
            {"id": "C", "text": "Event Viewer"},
            {"id": "D", "text": "Disk Management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "regedit opens the registry hives (HKLM, HKCU, etc.) so values can be viewed "
                       "and edited. Best practice is to export/back up the key before changing it.",
            "distractors": {
                "B": "Device Manager manages hardware devices and drivers, not registry values.",
                "C": "Event Viewer displays logged events; it cannot edit the registry.",
                "D": "Disk Management handles partitions and volumes, not registry keys.",
            },
            "exam_pattern": "References to HKEY_/hives/registry values → regedit. Back up the key first.",
        },
    },
    {
        "id": "aplus2-os-r2-006", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 2, "type": "mcq",
        "stem": "The Print Spooler has stopped. A technician needs to start it again and set it to "
                "launch automatically at every boot. Which console is designed for managing this?",
        "options": [
            {"id": "A", "text": "Services (services.msc)"},
            {"id": "B", "text": "Task Scheduler"},
            {"id": "C", "text": "Performance Monitor"},
            {"id": "D", "text": "System Information (msinfo32)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "services.msc lists Windows services and lets you start/stop them and set the "
                       "startup type (Automatic, Manual, Disabled) — exactly what the Print Spooler needs.",
            "distractors": {
                "B": "Task Scheduler runs programs on a schedule/trigger; it doesn't set a service's startup type.",
                "C": "Performance Monitor graphs performance counters; it doesn't control services.",
                "D": "msinfo32 is a read-only system report — it cannot change service state.",
            },
            "exam_pattern": "Start/stop services and set Automatic/Manual/Disabled startup → services.msc "
                            "(also reachable from Task Manager's Services tab).",
        },
    },
    {
        "id": "aplus2-os-r2-007", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 3, "type": "mcq",
        "stem": "A PC's disk sits at 100% activity. A technician wants a LIVE, per-process view that "
                "also shows which specific files each process is reading and writing. Which built-in "
                "tool provides this breakdown?",
        "options": [
            {"id": "A", "text": "Resource Monitor (resmon)"},
            {"id": "B", "text": "System Restore"},
            {"id": "C", "text": "Registry Editor"},
            {"id": "D", "text": "Disk Cleanup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resource Monitor shows real-time CPU, Disk, Network, and Memory activity drilled "
                       "down by process — including the individual files driving disk I/O.",
            "distractors": {
                "B": "System Restore rolls the system back to a restore point; it isn't a monitoring tool.",
                "C": "Registry Editor edits configuration values, not live resource usage.",
                "D": "Disk Cleanup deletes temporary files to free space; it doesn't show live I/O.",
            },
            "exam_pattern": "Live per-process (and per-file) resource drill-down → Resource Monitor. "
                            "Historical counters/logs → Performance Monitor.",
        },
    },
    {
        "id": "aplus2-os-r2-008", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 1, "type": "mcq",
        "stem": "A technician wants a maintenance script to run automatically every night at 2:00 "
                "a.m. Which built-in Windows tool schedules a recurring task like this?",
        "options": [
            {"id": "A", "text": "Task Scheduler"},
            {"id": "B", "text": "Task Manager"},
            {"id": "C", "text": "System Configuration (msconfig)"},
            {"id": "D", "text": "Event Viewer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Task Scheduler creates triggered/recurring jobs — e.g., run a script at 2:00 a.m. "
                       "daily — without anyone being logged on.",
            "distractors": {
                "B": "Task Manager shows and ends currently running processes; it can't schedule future runs.",
                "C": "msconfig configures boot and startup options, not scheduled tasks.",
                "D": "Event Viewer reviews logs after the fact; it doesn't launch scheduled jobs.",
            },
            "exam_pattern": "Future/recurring, time- or event-triggered jobs → Task Scheduler. "
                            "Current processes → Task Manager.",
        },
    },

    # ----- command_line -------------------------------------------------
    {
        "id": "aplus2-os-r2-009", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "multi",
        "stem": "A workstation pulled a bad DHCP lease. From the Windows command line, which TWO "
                "commands TOGETHER drop the current lease and request a fresh one? (Choose two.)",
        "options": [
            {"id": "A", "text": "ipconfig /release"},
            {"id": "B", "text": "ipconfig /renew"},
            {"id": "C", "text": "ipconfig /flushdns"},
            {"id": "D", "text": "ipconfig /displaydns"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "ipconfig /release gives up the current DHCP lease; ipconfig /renew then "
                       "requests a new one from the DHCP server.",
            "distractors": {
                "C": "/flushdns clears the DNS resolver cache — it has nothing to do with the DHCP lease.",
                "D": "/displaydns just prints the contents of the DNS resolver cache.",
            },
            "exam_pattern": "DHCP lease cycle = ipconfig /release then /renew. /flushdns and /displaydns "
                            "act on the DNS cache, not DHCP.",
        },
    },
    {
        "id": "aplus2-os-r2-010", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "mcq",
        "stem": "An administrator changed a Group Policy setting and wants a domain workstation to "
                "re-apply policy immediately rather than wait for the normal refresh. Which command "
                "forces the update?",
        "options": [
            {"id": "A", "text": "gpupdate /force"},
            {"id": "B", "text": "gpresult /r"},
            {"id": "C", "text": "sfc /scannow"},
            {"id": "D", "text": "ipconfig /renew"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "gpupdate applies Group Policy now; the /force switch reapplies ALL policy "
                       "settings instead of only changed ones.",
            "distractors": {
                "B": "gpresult /r reports which policies HAVE applied (RSoP); it doesn't reapply them.",
                "C": "sfc /scannow verifies and repairs protected system files — unrelated to policy.",
                "D": "ipconfig /renew renews a DHCP lease, not Group Policy.",
            },
            "exam_pattern": "Apply policy now = gpupdate (/force to reapply everything). Report what "
                            "applied = gpresult.",
        },
    },
    {
        "id": "aplus2-os-r2-011", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 3, "type": "mcq",
        "stem": "A USB flash drive is stuck in an odd read-only partition state. From the Windows "
                "command line, a technician wants to wipe its partition table and recreate it "
                "cleanly. Which utility manages disks and partitions from the CLI?",
        "options": [
            {"id": "A", "text": "diskpart"},
            {"id": "B", "text": "chkdsk"},
            {"id": "C", "text": "format"},
            {"id": "D", "text": "defrag"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "diskpart is Windows' scriptable partition/volume manager (select disk, clean, "
                       "create partition, assign) — the right tool to clear and rebuild the layout.",
            "distractors": {
                "B": "chkdsk checks an existing volume for file-system errors; it doesn't manage partitions.",
                "C": "format writes a file system to an existing volume but doesn't clean/recreate the partition table.",
                "D": "defrag rearranges fragmented files on a volume; it doesn't touch the partition table.",
            },
            "exam_pattern": "Partition/volume management from the CLI (clean, create, assign) → diskpart; "
                            "chkdsk/format operate WITHIN an existing volume.",
        },
    },
    {
        "id": "aplus2-os-r2-012", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 1, "type": "mcq",
        "stem": "At a Linux shell, a user wants to list the contents of the current directory, "
                "INCLUDING hidden files whose names begin with a dot. Which command does this?",
        "options": [
            {"id": "A", "text": "ls -a"},
            {"id": "B", "text": "pwd"},
            {"id": "C", "text": "cat"},
            {"id": "D", "text": "cd"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ls lists a directory's contents; the -a (all) flag includes hidden dotfiles "
                       "(e.g., .bashrc) that ls hides by default.",
            "distractors": {
                "B": "pwd prints the current working directory path, not its contents.",
                "C": "cat displays (concatenates) the contents of a file, not a directory listing.",
                "D": "cd changes the current directory; it doesn't list anything.",
            },
            "exam_pattern": "ls = list directory; -a shows hidden dotfiles; -l adds the long/detailed format.",
        },
    },
    {
        "id": "aplus2-os-r2-013", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "mcq",
        "stem": "A Linux administrator needs to find every line that contains the word 'error' "
                "inside a large log file. Which command is BEST suited to this text search?",
        "options": [
            {"id": "A", "text": "grep error /var/log/syslog"},
            {"id": "B", "text": "chmod error /var/log/syslog"},
            {"id": "C", "text": "ps aux"},
            {"id": "D", "text": "kill error"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "grep searches text for a pattern and prints matching lines, so "
                       "'grep error /var/log/syslog' lists every line containing 'error'.",
            "distractors": {
                "B": "chmod changes file permissions; 'error' is not a valid permission argument.",
                "C": "ps aux lists running processes, not lines inside a file.",
                "D": "kill terminates a process by PID/name; it performs no text search.",
            },
            "exam_pattern": "Search text for a pattern = grep; pipe other command output into grep to filter it.",
        },
    },

    # ----- os_features --------------------------------------------------
    {
        "id": "aplus2-os-r2-014", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "A user tries to copy a single 6 GB disk-image file to a USB drive formatted as "
                "FAT32 and gets a 'file too large' error, even though the drive shows 50 GB free. "
                "What is the cause and the BEST fix?",
        "options": [
            {"id": "A", "text": "FAT32's 4 GB per-file limit — reformat the drive as exFAT (or NTFS)"},
            {"id": "B", "text": "The USB drive is failing — replace it"},
            {"id": "C", "text": "The file is corrupt — download it again"},
            {"id": "D", "text": "USB 2.0 cannot transfer any file larger than 4 GB"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FAT32 cannot store a single file larger than 4 GB regardless of free space. "
                       "Reformatting as exFAT or NTFS removes that per-file limit.",
            "distractors": {
                "B": "50 GB is free and the error is a file-system limit, not a hardware failure.",
                "C": "A size-limit rejection is not file corruption.",
                "D": "USB version affects transfer SPEED, not the maximum file size.",
            },
            "exam_pattern": "FAT32 = 4 GB max single file (and ~32 GB format volume in Windows). "
                            "exFAT/NTFS remove the 4 GB cap.",
        },
    },
    {
        "id": "aplus2-os-r2-015", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 3, "type": "mcq",
        "stem": "A technician initializes a new 6 TB data drive but can only create a usable "
                "partition of about 2 TB. Which partition style must the disk use to access the "
                "full 6 TB?",
        "options": [
            {"id": "A", "text": "GPT (GUID Partition Table)"},
            {"id": "B", "text": "MBR (Master Boot Record)"},
            {"id": "C", "text": "FAT32"},
            {"id": "D", "text": "A dynamic disk spanned volume is required"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MBR addresses only ~2 TB, which is why the drive is capped. GPT supports "
                       "volumes well beyond 2 TB (and up to 128 partitions), so it exposes the full 6 TB.",
            "distractors": {
                "B": "MBR is the CAUSE of the 2 TB cap, not the fix.",
                "C": "FAT32 is a file system, not a partition style — it doesn't change the 2 TB disk limit.",
                "D": "Spanning isn't needed; GPT alone addresses the whole single disk.",
            },
            "exam_pattern": "MBR = 2 TB and 4 primary partitions max. GPT = >2 TB and up to 128 "
                            "partitions (UEFI required to BOOT from GPT).",
        },
    },
    {
        "id": "aplus2-os-r2-016", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "A technician remotely connects to \\\\PC01\\C$ and reaches the entire C: drive of "
                "that machine. What kind of share is C$?",
        "options": [
            {"id": "A", "text": "A hidden administrative share"},
            {"id": "B", "text": "A normal user share visible to everyone who browses the PC"},
            {"id": "C", "text": "A shared printer queue"},
            {"id": "D", "text": "A HomeGroup folder"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "C$ is a default hidden administrative share (the $ hides it from browsing) that "
                       "maps the root of the C: drive and requires administrative credentials.",
            "distractors": {
                "B": "The trailing $ hides it from normal browsing, and only administrators can use it.",
                "C": "C$ is a disk share of the volume root, not a printer.",
                "D": "HomeGroup was a deprecated consumer sharing feature, unrelated to admin shares.",
            },
            "exam_pattern": "Default hidden admin shares end in $ (C$, ADMIN$, IPC$): hidden from "
                            "browsing and usable only with administrative credentials.",
        },
    },
    {
        "id": "aplus2-os-r2-017", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "A user must set per-user file and folder PERMISSIONS and turn on file-level "
                "ENCRYPTION on a local volume. Which file system supports these features?",
        "options": [
            {"id": "A", "text": "NTFS"},
            {"id": "B", "text": "FAT32"},
            {"id": "C", "text": "exFAT"},
            {"id": "D", "text": "CDFS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Only NTFS provides file/folder permissions, EFS encryption, compression, and "
                       "journaling — the features the user needs.",
            "distractors": {
                "B": "FAT32 has no file-level permissions or encryption.",
                "C": "exFAT is built for flash-media interchange and also lacks permissions/encryption.",
                "D": "CDFS is the read-only file system for optical discs.",
            },
            "exam_pattern": "Permissions + EFS encryption + compression + journaling = NTFS only; "
                            "FAT32/exFAT are 'dumb' interchange file systems.",
        },
    },

    # ----- os_installation ----------------------------------------------
    {
        "id": "aplus2-os-r2-018", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 1, "type": "mcq",
        "stem": "Before performing a CLEAN installation of Windows on an existing PC, which point "
                "must the technician make clear to the user?",
        "options": [
            {"id": "A", "text": "A clean install erases the OS, apps, and data on the target partition — back up first"},
            {"id": "B", "text": "A clean install keeps all installed programs and settings"},
            {"id": "C", "text": "A clean install only changes the Windows edition"},
            {"id": "D", "text": "A backup is never required for a clean install"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A clean install wipes the target partition and starts fresh, so anything on it "
                       "is lost unless backed up first.",
            "distractors": {
                "B": "Keeping apps/settings describes an in-place upgrade or repair install, not a clean install.",
                "C": "Changing the edition is an edition upgrade, not a clean install.",
                "D": "Because the target partition is wiped, backing up the user's data is essential.",
            },
            "exam_pattern": "Clean install = wipe target partition (fresh start). In-place upgrade/repair = "
                            "keep apps, files, and settings.",
        },
    },
    {
        "id": "aplus2-os-r2-019", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 2, "type": "multi",
        "stem": "A technician must start Windows Setup on a PC with a completely blank drive. Which "
                "TWO are valid installation BOOT methods? (Choose two.)",
        "options": [
            {"id": "A", "text": "Boot from a bootable USB flash drive"},
            {"id": "B", "text": "Network (PXE) boot from a deployment server"},
            {"id": "C", "text": "Boot into Safe Mode"},
            {"id": "D", "text": "Run System Restore"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Install media can be launched from a bootable USB drive or over the network via "
                       "PXE — both work on a blank drive with no OS present.",
            "distractors": {
                "C": "Safe Mode boots an ALREADY-installed Windows for troubleshooting; it is not an install source.",
                "D": "System Restore rolls back an installed system to a restore point; it can't install Windows.",
            },
            "exam_pattern": "Install boot methods: USB, optical, external drive, network/PXE. Safe Mode "
                            "and System Restore act on an already-installed OS.",
        },
    },
    {
        "id": "aplus2-os-r2-020", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 3, "type": "mcq",
        "stem": "A Windows 10 PC with a fast CPU and plenty of RAM is refused the Windows 11 "
                "upgrade. Which firmware/security requirement, newly required by Windows 11, MOST "
                "often blocks otherwise-capable machines?",
        "options": [
            {"id": "A", "text": "TPM 2.0 with UEFI Secure Boot"},
            {"id": "B", "text": "A FAT32 system partition"},
            {"id": "C", "text": "Legacy BIOS (CSM) boot mode"},
            {"id": "D", "text": "A 32-bit processor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Windows 11 requires TPM 2.0 and UEFI Secure Boot; these are frequently present "
                       "but disabled in firmware, which is why capable PCs fail the check until they're enabled.",
            "distractors": {
                "B": "Windows uses NTFS for its system partition; a FAT32 system partition isn't a requirement.",
                "C": "Windows 11 requires UEFI, so legacy BIOS/CSM is the opposite of what's needed.",
                "D": "Windows 11 is 64-bit only — a 32-bit CPU can't run it at all, let alone 'satisfy' a requirement.",
            },
            "exam_pattern": "Windows 11 floor: UEFI + Secure Boot, TPM 2.0, 64-bit supported CPU, 4 GB RAM, "
                            "64 GB storage.",
        },
    },
    {
        "id": "aplus2-os-r2-021", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 2, "type": "mcq",
        "stem": "During installation a technician can choose a quick format or a full format of the "
                "target drive. What does a FULL format do that a quick format does not?",
        "options": [
            {"id": "A", "text": "It scans the disk for bad sectors (and more thoroughly clears the volume)"},
            {"id": "B", "text": "It automatically installs the device drivers"},
            {"id": "C", "text": "It converts the disk from MBR to GPT"},
            {"id": "D", "text": "It encrypts the volume with BitLocker"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A full format writes a fresh file system AND scans every sector for bad spots "
                       "(and overwrites the volume on modern Windows); a quick format just rewrites the "
                       "file table, so it's much faster but skips the sector check.",
            "distractors": {
                "B": "Formatting never installs drivers.",
                "C": "Partition style (MBR vs. GPT) is chosen separately; the format type doesn't convert it.",
                "D": "Formatting does not enable BitLocker encryption.",
            },
            "exam_pattern": "Quick format = rewrite file table only (fast). Full format = also scan for "
                            "bad sectors and clear the volume (slow).",
        },
    },

    # ----- networking_os ------------------------------------------------
    {
        "id": "aplus2-os-r2-022", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "A networked printer needs a fixed address, so a technician must assign a static "
                "IPv4 address, subnet mask, and default gateway to a Windows PC. Where is this "
                "configured?",
        "options": [
            {"id": "A", "text": "In the adapter's Internet Protocol Version 4 (TCP/IPv4) properties"},
            {"id": "B", "text": "In Device Manager"},
            {"id": "C", "text": "On Task Manager's Performance tab"},
            {"id": "D", "text": "In Disk Management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Static addressing is set in the network adapter's TCP/IPv4 properties — IP "
                       "address, subnet mask, default gateway, and DNS servers.",
            "distractors": {
                "B": "Device Manager manages the adapter's driver/hardware, not its IP settings.",
                "C": "Task Manager's Performance tab only graphs throughput; it can't set an address.",
                "D": "Disk Management handles partitions and volumes, not IP configuration.",
            },
            "exam_pattern": "Static IP/DNS → adapter properties → TCP/IPv4. Blank/automatic = DHCP; "
                            "DHCP failure yields an APIPA 169.254.x.x address.",
        },
    },
    {
        "id": "aplus2-os-r2-023", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "Company policy routes all web traffic through a proxy server at 10.0.0.5 port 8080. "
                "On a Windows client, where is the proxy server configured?",
        "options": [
            {"id": "A", "text": "Settings > Network & Internet > Proxy"},
            {"id": "B", "text": "Device Manager"},
            {"id": "C", "text": "Disk Management"},
            {"id": "D", "text": "Event Viewer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Windows proxy is set under Network & Internet > Proxy, either manually "
                       "(host:port) or via an automatic configuration script.",
            "distractors": {
                "B": "Device Manager manages hardware and drivers, not web-proxy settings.",
                "C": "Disk Management manages partitions/volumes.",
                "D": "Event Viewer reviews logs; it doesn't configure networking.",
            },
            "exam_pattern": "Windows proxy → Settings > Network & Internet > Proxy (manual host:port or "
                            "auto-config script).",
        },
    },
    {
        "id": "aplus2-os-r2-024", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "A remote user must securely reach the corporate LAN over the public Internet from a "
                "Windows laptop. Which Windows networking feature establishes this encrypted "
                "connection to the company gateway?",
        "options": [
            {"id": "A", "text": "A VPN connection (Settings > Network & Internet > VPN)"},
            {"id": "B", "text": "A mapped network drive"},
            {"id": "C", "text": "A metered connection"},
            {"id": "D", "text": "Airplane mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VPN creates an encrypted tunnel across the Internet into the private LAN; it's "
                       "added under Network & Internet > VPN with the server address and authentication.",
            "distractors": {
                "B": "A mapped drive points to a share but provides no secure tunnel on its own.",
                "C": "A metered connection just flags data-usage limits; it doesn't create a tunnel.",
                "D": "Airplane mode disables the radios — the opposite of connecting.",
            },
            "exam_pattern": "Encrypted tunnel over the Internet into the private network = VPN "
                            "(Network & Internet > VPN).",
        },
    },
    {
        "id": "aplus2-os-r2-025", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "A user tethers a Windows laptop to a cellular hotspot with a capped data plan and "
                "wants Windows to limit background data and defer large updates on that network. "
                "Which setting should be enabled for the connection?",
        "options": [
            {"id": "A", "text": "Set the connection as metered"},
            {"id": "B", "text": "Toggle the network between Public and Private repeatedly"},
            {"id": "C", "text": "Disable the network adapter"},
            {"id": "D", "text": "Turn on Remote Desktop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Marking a connection as metered tells Windows to reduce background data and hold "
                       "back large downloads/updates on that network — ideal for capped cellular plans.",
            "distractors": {
                "B": "The location profile controls discovery/firewall behavior, not data caps.",
                "C": "Disabling the adapter ends connectivity entirely.",
                "D": "Remote Desktop is unrelated to limiting data usage.",
            },
            "exam_pattern": "Capped/cellular link → set it as a metered connection to throttle "
                            "background data and large updates.",
        },
    },

    # ----- macos_linux --------------------------------------------------
    {
        "id": "aplus2-os-r2-026", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "On macOS, which built-in utility securely stores a user's website passwords, Wi-Fi "
                "keys, and certificates?",
        "options": [
            {"id": "A", "text": "Keychain Access"},
            {"id": "B", "text": "Time Machine"},
            {"id": "C", "text": "Mission Control"},
            {"id": "D", "text": "Spotlight"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Keychain Access is the macOS encrypted store for passwords, Wi-Fi keys, and "
                       "certificates.",
            "distractors": {
                "B": "Time Machine is the macOS backup/restore utility.",
                "C": "Mission Control arranges open windows and virtual desktops (Spaces).",
                "D": "Spotlight is the system-wide search feature.",
            },
            "exam_pattern": "macOS: Keychain = credential/cert store; Time Machine = backup; Spotlight = "
                            "search; Mission Control = window/Spaces manager.",
        },
    },
    {
        "id": "aplus2-os-r2-027", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "A Mac user needs to erase and reformat an external drive and run First Aid to repair "
                "directory errors on it. Which built-in macOS tool does this?",
        "options": [
            {"id": "A", "text": "Disk Utility"},
            {"id": "B", "text": "Finder"},
            {"id": "C", "text": "Keychain Access"},
            {"id": "D", "text": "App Store"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Disk Utility formats, partitions, and erases volumes and runs First Aid to "
                       "repair disk/directory errors on macOS.",
            "distractors": {
                "B": "Finder browses files and folders but can't format a volume or run First Aid.",
                "C": "Keychain Access stores credentials, not disk tools.",
                "D": "The App Store installs applications; it doesn't manage disks.",
            },
            "exam_pattern": "macOS Disk Utility ≈ Windows Disk Management + chkdsk: format/partition/erase "
                            "plus First Aid repair.",
        },
    },
    {
        "id": "aplus2-os-r2-028", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 3, "type": "mcq",
        "stem": "A user with an Intel-based Mac wants to install Windows and dual-boot it NATIVELY "
                "alongside macOS. Which Apple utility is designed for this?",
        "options": [
            {"id": "A", "text": "Boot Camp (Boot Camp Assistant)"},
            {"id": "B", "text": "Time Machine"},
            {"id": "C", "text": "FileVault"},
            {"id": "D", "text": "Gatekeeper"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Boot Camp Assistant partitions the disk and installs Windows so an Intel Mac can "
                       "dual-boot it natively (not in a virtual machine).",
            "distractors": {
                "B": "Time Machine backs up and restores files.",
                "C": "FileVault encrypts the macOS startup disk.",
                "D": "Gatekeeper controls which app sources are allowed to run.",
            },
            "exam_pattern": "Native Windows dual-boot on an Intel Mac = Boot Camp (partition + install "
                            "Windows). Apple Silicon Macs don't support Boot Camp.",
        },
    },
    {
        "id": "aplus2-os-r2-029", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "On Linux, a standard user must run a single command that requires root privileges "
                "(for example, installing a package) and gets 'permission denied.' Which command "
                "runs just that command as the superuser?",
        "options": [
            {"id": "A", "text": "sudo"},
            {"id": "B", "text": "pwd"},
            {"id": "C", "text": "ls"},
            {"id": "D", "text": "man"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Prefixing a command with sudo runs that one command with root (superuser) "
                       "privileges, after the user authenticates.",
            "distractors": {
                "B": "pwd prints the current directory path.",
                "C": "ls lists directory contents.",
                "D": "man opens a command's manual page.",
            },
            "exam_pattern": "sudo = run ONE command as root; su = switch to the root (or another) user's "
                            "shell for a session.",
        },
    },

    # =====================================================================
    # 2.0 SECURITY
    # =====================================================================

    # ----- security_concepts_a2 -----------------------------------------
    {
        "id": "aplus2-sec-r2-001", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a batch file to run automatically each time a domain user "
                "logs on — mapping drives and configuring printers. Which Active Directory feature "
                "delivers this?",
        "options": [
            {"id": "A", "text": "A logon script applied through Group Policy"},
            {"id": "B", "text": "Folder redirection"},
            {"id": "C", "text": "BitLocker"},
            {"id": "D", "text": "A local user account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A logon script (delivered via Group Policy) runs automatically at user logon to "
                       "map drives, set printers, and apply environment settings.",
            "distractors": {
                "B": "Folder redirection points folders like Documents to a server share; it doesn't run a script.",
                "C": "BitLocker encrypts the drive; it has nothing to do with logon automation.",
                "D": "A local account isn't managed by AD/Group Policy, so no domain logon script applies.",
            },
            "exam_pattern": "AD/Group Policy tools: logon scripts (run at logon), folder redirection, "
                            "home folder, OUs, and security groups.",
        },
    },
    {
        "id": "aplus2-sec-r2-002", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "After signing in to Windows once in the morning, a user can open the intranet, "
                "email, and the HR portal without re-entering credentials for each. Which concept "
                "provides this?",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO)"},
            {"id": "B", "text": "Multifactor authentication (MFA)"},
            {"id": "C", "text": "Principle of least privilege"},
            {"id": "D", "text": "A hardware security token"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSO lets one authenticated identity access many services without repeated logins "
                       "— one sign-on, many apps.",
            "distractors": {
                "B": "MFA adds a second factor, which means MORE prompts, not fewer, and is a different concept.",
                "C": "Least privilege limits what an account may do; it isn't about avoiding repeated logins.",
                "D": "A hardware token is an MFA device, not the single-sign-on mechanism itself.",
            },
            "exam_pattern": "Authenticate once, reach many services = SSO (convenience/identity). "
                            "Adding factors = MFA (assurance).",
        },
    },
    {
        "id": "aplus2-sec-r2-003", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 1, "type": "mcq",
        "stem": "To deter theft of laptops in an open retail office, which inexpensive PHYSICAL "
                "control secures each laptop to the desk?",
        "options": [
            {"id": "A", "text": "A cable lock (Kensington-style lock)"},
            {"id": "B", "text": "A host-based firewall"},
            {"id": "C", "text": "BitLocker drive encryption"},
            {"id": "D", "text": "A strong login password"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cable lock physically tethers the laptop to a desk or fixture, deterring "
                       "walk-off theft of the hardware.",
            "distractors": {
                "B": "A firewall filters network traffic; it does nothing to stop someone carrying the device away.",
                "C": "BitLocker protects the DATA if stolen but doesn't prevent the physical theft.",
                "D": "A password protects login, not the physical removal of the laptop.",
            },
            "exam_pattern": "Physical theft deterrents = cable/equipment locks, server/USB locks. "
                            "Encryption and passwords protect DATA, not the device's presence.",
        },
    },
    {
        "id": "aplus2-sec-r2-004", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 1, "type": "mcq",
        "stem": "A secure lab door unlocks only after scanning an employee's fingerprint. Which "
                "authentication FACTOR does the fingerprint represent?",
        "options": [
            {"id": "A", "text": "Something you are (biometric)"},
            {"id": "B", "text": "Something you have"},
            {"id": "C", "text": "Something you know"},
            {"id": "D", "text": "Somewhere you are"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A fingerprint is a biometric — 'something you are.'",
            "distractors": {
                "B": "'Something you have' is a token, smart card, or phone.",
                "C": "'Something you know' is a password or PIN.",
                "D": "'Somewhere you are' is a location-based factor (e.g., GPS/geofencing).",
            },
            "exam_pattern": "Factor types: know (password), have (token/card), are (biometric), plus "
                            "somewhere-you-are. Combine DIFFERENT types for MFA.",
        },
    },

    # ----- malware_a2 ---------------------------------------------------
    {
        "id": "aplus2-sec-r2-005", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "A piece of malware spreads by itself from PC to PC across the network with no user "
                "action, consuming bandwidth as it replicates. Which type is it?",
        "options": [
            {"id": "A", "text": "Worm"},
            {"id": "B", "text": "Trojan"},
            {"id": "C", "text": "Keylogger"},
            {"id": "D", "text": "Ransomware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A worm self-replicates and spreads across hosts/networks on its own, without "
                       "needing a user to run it.",
            "distractors": {
                "B": "A trojan disguises itself as legitimate software and requires the user to run it.",
                "C": "A keylogger records keystrokes; it doesn't self-propagate.",
                "D": "Ransomware encrypts data for payment — it's defined by extortion, not self-spread.",
            },
            "exam_pattern": "Self-replicating + spreads with no user interaction = worm. Needs a user/host "
                            "to run = virus/trojan.",
        },
    },
    {
        "id": "aplus2-sec-r2-006", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "A user's banking passwords are stolen even though they never shared their screen. "
                "Investigation finds software secretly recording every keystroke and sending it to "
                "an attacker. Which malware is this?",
        "options": [
            {"id": "A", "text": "Keylogger"},
            {"id": "B", "text": "Rootkit"},
            {"id": "C", "text": "Worm"},
            {"id": "D", "text": "Ransomware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secretly capturing keystrokes to harvest credentials is the definition of a "
                       "keylogger (a form of spyware).",
            "distractors": {
                "B": "A rootkit hides at a privileged level to maintain stealthy access; capturing keystrokes isn't its defining trait.",
                "C": "A worm self-propagates across hosts; it isn't specifically a keystroke recorder.",
                "D": "Ransomware encrypts files and demands payment.",
            },
            "exam_pattern": "Records keystrokes to steal credentials = keylogger/spyware. Hides to keep "
                            "privileged access = rootkit.",
        },
    },
    {
        "id": "aplus2-sec-r2-007", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 3, "type": "multi",
        "stem": "In CompTIA's best-practice malware removal procedure, which TWO actions involve "
                "System Restore on a Windows PC? (Choose two.)",
        "options": [
            {"id": "A", "text": "Disable System Restore BEFORE remediating the malware"},
            {"id": "B", "text": "Re-enable System Restore and create a new restore point AFTER cleaning"},
            {"id": "C", "text": "Permanently disable System Restore on all company PCs"},
            {"id": "D", "text": "Roll the PC back from a restore point as the very first troubleshooting step"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "You disable System Restore before remediation (old restore points can harbor the "
                       "malware) and re-enable it with a fresh restore point once the system is clean.",
            "distractors": {
                "C": "System Restore is re-enabled afterward, not permanently disabled.",
                "D": "The process starts by identifying/verifying symptoms and quarantining — not by "
                     "rolling back (a restore point could reinfect the PC).",
            },
            "exam_pattern": "7 steps: 1 identify/verify symptoms → 2 quarantine → 3 disable System Restore "
                            "→ 4 remediate (update + scan/remove) → 5 schedule scans/updates → 6 re-enable "
                            "System Restore + make a restore point → 7 educate the user.",
        },
    },
    {
        "id": "aplus2-sec-r2-008", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "While remediating an infected Windows PC, a stubborn malware process keeps "
                "relaunching in normal mode and prevents the anti-malware scan from finishing. "
                "Which technique is recommended to complete the removal?",
        "options": [
            {"id": "A", "text": "Boot into Safe Mode (or a preinstallation/recovery environment) and run the scan there"},
            {"id": "B", "text": "Disable the antivirus so Windows starts faster"},
            {"id": "C", "text": "Grant the user's account local administrator rights"},
            {"id": "D", "text": "Permanently turn off Windows Update"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Starting in Safe Mode (or booting a preinstallation/recovery environment) keeps "
                       "the malware from auto-launching, so the anti-malware scan can run and remove it.",
            "distractors": {
                "B": "Disabling the antivirus removes the very tool needed to clean the system.",
                "C": "Giving the account admin rights raises risk and doesn't stop the process relaunching.",
                "D": "Turning off updates leaves the PC more vulnerable and doesn't remove the malware.",
            },
            "exam_pattern": "Remediation = update anti-malware definitions + use scanning/removal "
                            "techniques; for stubborn infections boot Safe Mode or a preinstallation/"
                            "recovery environment.",
        },
    },

    # ----- social_engineering_a2 ----------------------------------------
    {
        "id": "aplus2-sec-r2-009", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 1, "type": "mcq",
        "stem": "Thousands of employees receive an email appearing to come from 'IT Support' with a "
                "link to a fake login page urging them to 'verify your password now.' Which attack "
                "is this?",
        "options": [
            {"id": "A", "text": "Phishing"},
            {"id": "B", "text": "Whaling"},
            {"id": "C", "text": "Tailgating"},
            {"id": "D", "text": "Distributed denial-of-service (DDoS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A mass deceptive email trying to harvest credentials via a fake page is phishing.",
            "distractors": {
                "B": "Whaling targets a specific high-value executive, not a mass audience.",
                "C": "Tailgating is physically following someone through a secured door.",
                "D": "A DDoS floods a service to deny availability; it isn't credential trickery.",
            },
            "exam_pattern": "Mass deceptive email for credentials = phishing. A single targeted exec = "
                            "whaling; a targeted individual/group = spear phishing.",
        },
    },
    {
        "id": "aplus2-sec-r2-010", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 2, "type": "mcq",
        "stem": "An employee receives a TEXT MESSAGE claiming a package is being held and they must "
                "tap a link to pay a small fee, which asks for card details. Which social-"
                "engineering attack is this?",
        "options": [
            {"id": "A", "text": "Smishing"},
            {"id": "B", "text": "Vishing"},
            {"id": "C", "text": "Shoulder surfing"},
            {"id": "D", "text": "Evil twin"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Phishing delivered by SMS/text message is smishing.",
            "distractors": {
                "B": "Vishing is phishing over a voice phone call.",
                "C": "Shoulder surfing is watching someone enter sensitive data.",
                "D": "An evil twin is a rogue Wi-Fi access point impersonating a legitimate SSID.",
            },
            "exam_pattern": "Phishing by channel: email = phishing, SMS/text = smishing, voice call = vishing.",
        },
    },
    {
        "id": "aplus2-sec-r2-011", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 2, "type": "mcq",
        "stem": "In a busy airport, an attacker stands close behind a traveler and watches them type "
                "their laptop password and PIN. Which technique is this, and what is a simple "
                "countermeasure?",
        "options": [
            {"id": "A", "text": "Shoulder surfing — use a privacy screen filter and shield entry"},
            {"id": "B", "text": "Phishing — enable spam filtering"},
            {"id": "C", "text": "Tailgating — install an access control vestibule"},
            {"id": "D", "text": "Dumpster diving — shred documents before disposal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Directly observing someone entering credentials is shoulder surfing; privacy "
                       "filters, positioning, and shielding entry mitigate it.",
            "distractors": {
                "B": "Phishing is deceptive messaging, not visual observation.",
                "C": "Tailgating is following someone through a secured door.",
                "D": "Dumpster diving is scavenging discarded media/paper for information.",
            },
            "exam_pattern": "Watching credential entry over the shoulder = shoulder surfing → privacy "
                            "filter + awareness + positioning.",
        },
    },
    {
        "id": "aplus2-sec-r2-012", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 3, "type": "mcq",
        "stem": "An attacker scatters USB flash drives labeled 'Payroll 2026' in the company parking "
                "lot, hoping an employee plugs one in and runs the malware it carries. Which social-"
                "engineering technique is this?",
        "options": [
            {"id": "A", "text": "Baiting"},
            {"id": "B", "text": "Whaling"},
            {"id": "C", "text": "Vishing"},
            {"id": "D", "text": "On-path (man-in-the-middle) attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leaving tempting infected media for a curious victim to pick up and use is "
                       "baiting. Disabling AutoRun and endpoint controls helps mitigate it.",
            "distractors": {
                "B": "Whaling targets an executive, typically by email.",
                "C": "Vishing uses a voice phone call.",
                "D": "An on-path attack intercepts traffic between two parties; it isn't a dropped-media lure.",
            },
            "exam_pattern": "Leaving infected media/links for a victim to take = baiting → disable "
                            "AutoRun/AutoPlay and use endpoint control.",
        },
    },

    # ----- windows_security ---------------------------------------------
    {
        "id": "aplus2-sec-r2-013", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 2, "type": "mcq",
        "stem": "To limit the damage malware can do, which type of account should employees use for "
                "their DAY-TO-DAY work on a Windows PC?",
        "options": [
            {"id": "A", "text": "A standard user account"},
            {"id": "B", "text": "The built-in Administrator account"},
            {"id": "C", "text": "A guest account for everything"},
            {"id": "D", "text": "A domain controller service account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Daily work should use a standard account so malware runs with limited rights; "
                       "elevate via UAC/Run as administrator only when a task truly needs it.",
            "distractors": {
                "B": "Running as administrator lets malware make system-wide changes with no prompt barrier.",
                "C": "A guest account is too limited for real work and should be disabled, not used daily.",
                "D": "Domain controller service accounts are server infrastructure, not user logins.",
            },
            "exam_pattern": "Least privilege: everyday use = standard account; elevate (UAC / Run as "
                            "administrator) only when required.",
        },
    },
    {
        "id": "aplus2-sec-r2-014", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 2, "type": "mcq",
        "stem": "Windows Defender Firewall applies a different set of rules depending on the network "
                "the PC is connected to. Which set of PROFILES does it use?",
        "options": [
            {"id": "A", "text": "Domain, Private, and Public"},
            {"id": "B", "text": "Red, Yellow, and Green"},
            {"id": "C", "text": "Inbound and Outbound only"},
            {"id": "D", "text": "Home, Work, and School"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Windows Defender Firewall has three network profiles — Domain, Private, and "
                       "Public — each with its own inbound/outbound rules.",
            "distractors": {
                "B": "Red/Yellow/Green is not a Windows firewall concept.",
                "C": "Inbound/Outbound are rule directions WITHIN each profile, not the profiles themselves.",
                "D": "Home/Work/School are not the firewall's profile names.",
            },
            "exam_pattern": "Defender Firewall profiles: Domain (AD network), Private (trusted LAN/home), "
                            "Public (untrusted) — each with its own ruleset.",
        },
    },
    {
        "id": "aplus2-sec-r2-015", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 1, "type": "mcq",
        "stem": "On a standalone Windows 11 PC with no third-party antivirus installed, which "
                "BUILT-IN component provides real-time malware protection?",
        "options": [
            {"id": "A", "text": "Microsoft Defender Antivirus"},
            {"id": "B", "text": "BitLocker"},
            {"id": "C", "text": "Windows Defender Firewall"},
            {"id": "D", "text": "User Account Control (UAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender Antivirus is the built-in real-time anti-malware engine in "
                       "Windows; it protects the PC when no third-party AV is present.",
            "distractors": {
                "B": "BitLocker encrypts the drive at rest — it doesn't scan for malware.",
                "C": "The firewall filters network connections; it isn't a file/malware scanner.",
                "D": "UAC gates privilege elevation; it doesn't detect or remove malware.",
            },
            "exam_pattern": "Built-in Windows roles: Defender Antivirus = real-time AV; Firewall = traffic "
                            "filter; BitLocker = encryption; UAC = privilege gate.",
        },
    },

    # ----- workstation_hardening ----------------------------------------
    {
        "id": "aplus2-sec-r2-016", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Clinic staff keep walking away leaving their sessions open. Which hardening setting "
                "BEST prevents a passerby from using an unattended, logged-in workstation?",
        "options": [
            {"id": "A", "text": "A screen lock that activates after a short idle period and requires the password to resume"},
            {"id": "B", "text": "A faster CPU"},
            {"id": "C", "text": "Disabling the firewall"},
            {"id": "D", "text": "A brighter screen saver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An inactivity screen lock (requiring the password to resume) stops a passerby "
                       "from using a session the user walked away from.",
            "distractors": {
                "B": "CPU speed has nothing to do with securing an unattended session.",
                "C": "Disabling the firewall weakens security and does nothing about physical walk-up access.",
                "D": "A screen saver without a password lock still lets anyone move the mouse and continue.",
            },
            "exam_pattern": "Unattended workstation → auto screen lock + short timeout (and Win+L to lock "
                            "manually).",
        },
    },
    {
        "id": "aplus2-sec-r2-017", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "mcq",
        "stem": "To slow down automated password-guessing (brute-force) attacks against local "
                "accounts, which policy should a technician configure?",
        "options": [
            {"id": "A", "text": "An account lockout threshold that locks the account after a set number of failed logons"},
            {"id": "B", "text": "A longer screen-saver timeout"},
            {"id": "C", "text": "AutoPlay enabled for all drives"},
            {"id": "D", "text": "A shorter minimum password length"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An account lockout threshold locks the account after N failed attempts, throttling "
                       "brute-force guessing.",
            "distractors": {
                "B": "A screen-saver timeout governs idle locking, not failed-logon attempts.",
                "C": "Enabling AutoPlay is a malware vector — it weakens security, not strengthens it.",
                "D": "Shorter passwords are weaker and easier to guess, the opposite of hardening.",
            },
            "exam_pattern": "Throttle brute force with a lockout threshold + duration; pair with password "
                            "length/complexity and MFA.",
        },
    },
    {
        "id": "aplus2-sec-r2-018", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "mcq",
        "stem": "As an account-management hardening measure, a company wants to ensure shift workers "
                "cannot log on to their workstations OUTSIDE their scheduled shift hours. Which "
                "setting accomplishes this?",
        "options": [
            {"id": "A", "text": "Configure logon time restrictions (permitted logon hours) on the user accounts"},
            {"id": "B", "text": "Enable AutoPlay for removable media after hours"},
            {"id": "C", "text": "Grant all shift workers local administrator rights"},
            {"id": "D", "text": "Disable the account lockout policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Logon time restrictions (permitted logon hours) block sign-in outside the "
                       "allowed window, enforcing when each account may be used.",
            "distractors": {
                "B": "AutoPlay is a malware vector and has nothing to do with restricting hours.",
                "C": "Granting admin rights weakens security and doesn't limit when users can log on.",
                "D": "Disabling the lockout policy removes brute-force protection — it reduces security.",
            },
            "exam_pattern": "Account-management hardening: restrict logon hours/times, set lockout "
                            "thresholds and screen-lock timeouts, enforce least privilege, and disable/"
                            "rename default accounts.",
        },
    },

    # ----- data_destruction ---------------------------------------------
    {
        "id": "aplus2-sec-r2-019", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "mcq",
        "stem": "A technician performs a standard (quick) format on a hard drive before donating the "
                "PC and assumes the data is gone. Why is this UNSAFE for sensitive data?",
        "options": [
            {"id": "A", "text": "A standard format only clears the file table; the underlying data is still recoverable with tools"},
            {"id": "B", "text": "Formatting physically destroys the drive platters"},
            {"id": "C", "text": "A quick format permanently encrypts the data"},
            {"id": "D", "text": "Formatting degausses the drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A standard/quick format just resets the file system's index; the actual data "
                       "remains on the platters and can be recovered with widely available tools.",
            "distractors": {
                "B": "Formatting is a logical operation; it does not physically harm the platters.",
                "C": "Formatting doesn't encrypt anything.",
                "D": "Formatting has nothing to do with magnetic degaussing.",
            },
            "exam_pattern": "Quick/standard format is recoverable. For reuse → multi-pass drive wipe/"
                            "overwrite; for disposal → physical destruction.",
        },
    },
    {
        "id": "aplus2-sec-r2-020", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 3, "type": "mcq",
        "stem": "A batch of solid-state drives (SSDs) will be REUSED internally and must be sanitized "
                "so prior data cannot be recovered. Which method is appropriate?",
        "options": [
            {"id": "A", "text": "ATA Secure Erase using the SSD's built-in sanitize command (or the vendor's tool)"},
            {"id": "B", "text": "Degaussing the SSDs"},
            {"id": "C", "text": "A single standard format"},
            {"id": "D", "text": "Waving a strong magnet over each SSD to overwrite it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSDs are sanitized for reuse with ATA Secure Erase (or the manufacturer's secure-"
                       "erase utility), which clears the flash cells using the drive's own command set.",
            "distractors": {
                "B": "Degaussing only affects MAGNETIC media; it does nothing to flash-based SSDs.",
                "C": "A standard format leaves data recoverable.",
                "D": "Magnets don't erase flash memory — this isn't a real sanitization method.",
            },
            "exam_pattern": "SSD sanitize for reuse = ATA Secure Erase / vendor tool. Degaussing works "
                            "only on magnetic HDDs and tape, NOT on SSDs.",
        },
    },
    {
        "id": "aplus2-sec-r2-021", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "multi",
        "stem": "Degaussing uses a strong magnetic field to sanitize media. On which TWO types of "
                "media is degaussing EFFECTIVE? (Choose two.)",
        "options": [
            {"id": "A", "text": "Magnetic hard disk drives (HDDs)"},
            {"id": "B", "text": "Magnetic backup tapes"},
            {"id": "C", "text": "Solid-state drives (SSDs)"},
            {"id": "D", "text": "Optical discs (DVDs/Blu-ray)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Degaussing scrambles the magnetic fields that store data, so it works on magnetic "
                       "HDDs and magnetic tape.",
            "distractors": {
                "C": "SSDs store data in flash cells, which a magnetic field does not erase.",
                "D": "Optical discs store data optically (pits/dye), not magnetically, so degaussing has no effect.",
            },
            "exam_pattern": "Degaussing = magnetic media only (HDDs, tape). SSDs need secure erase; optical "
                            "media must be shredded/physically destroyed.",
        },
    },
]
