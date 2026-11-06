"""CompTIA A+ Core 2 (220-1102) item pool — original, objective-aligned questions.

Same authoring rules as the other pools: original content mapped to the public
220-1102 exam objectives, never real exam items. build_content.py shuffles option
order, so the answer key here is not positionally biased.
"""

QUESTIONS = [
    # ===== 1.0 Operating Systems ============================================
    {
        "id": "aplus2-os-001", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_editions", "difficulty": 2, "type": "mcq",
        "stem": "A business laptop must join the company's Active Directory domain, be "
                "encrypted with BitLocker, and have settings pushed via the local Group "
                "Policy Editor. What is the MINIMUM Windows 10/11 edition that supports all three?",
        "options": [
            {"id": "A", "text": "Windows Pro"},
            {"id": "B", "text": "Windows Home"},
            {"id": "C", "text": "Windows Pro for Workstations"},
            {"id": "D", "text": "Windows Enterprise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Domain join, BitLocker, and gpedit.msc all first appear in Windows Pro, "
                       "so Pro is the minimum edition that meets every requirement.",
            "distractors": {
                "B": "Home cannot join a domain, has no BitLocker, and ships without the Local "
                     "Group Policy Editor — it fails all three needs.",
                "C": "Pro for Workstations supports them but adds ReFS, more RAM/CPU sockets and "
                     "server-grade features you don't need — it exceeds the MINIMUM.",
                "D": "Enterprise also qualifies but is volume-licensed with extras (AppLocker, "
                     "DirectAccess); it is more than the minimum.",
            },
            "exam_pattern": "Home = consumer (no domain join, no BitLocker, no gpedit). Pro = business "
                            "baseline. Enterprise/Education = volume-licensed with the extras.",
        },
    },
    {
        "id": "aplus2-os-002", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "windows_tools", "difficulty": 1, "type": "mcq",
        "stem": "After installing a new webcam, a technician sees it listed with a yellow "
                "exclamation mark indicating a driver problem. Which built-in Windows tool "
                "is used to view and manage hardware devices and their drivers?",
        "options": [
            {"id": "A", "text": "Device Manager (devmgmt.msc)"},
            {"id": "B", "text": "Task Manager (taskmgr.exe)"},
            {"id": "C", "text": "Disk Management (diskmgmt.msc)"},
            {"id": "D", "text": "Event Viewer (eventvwr.msc)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Device Manager lists installed hardware and its drivers; a yellow '!' flags "
                       "a device with a driver/resource issue you can update or roll back there.",
            "distractors": {
                "B": "Task Manager shows running processes, startup apps and performance — not hardware drivers.",
                "C": "Disk Management creates/formats partitions and volumes, not device drivers.",
                "D": "Event Viewer displays system/application logs; it records events but doesn't manage devices.",
            },
            "exam_pattern": "Hardware + drivers = Device Manager (devmgmt.msc); yellow '!' = driver/resource problem.",
        },
    },
    {
        "id": "aplus2-os-003", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "command_line", "difficulty": 2, "type": "mcq",
        "stem": "Windows is behaving oddly and a technician suspects corrupted protected system "
                "files. From an elevated Command Prompt, which command scans those files and "
                "automatically repairs them?",
        "options": [
            {"id": "A", "text": "sfc /scannow"},
            {"id": "B", "text": "chkdsk /f"},
            {"id": "C", "text": "diskpart"},
            {"id": "D", "text": "gpupdate /force"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System File Checker (sfc /scannow) verifies the integrity of protected Windows "
                       "system files and replaces corrupted ones from a cached copy.",
            "distractors": {
                "B": "chkdsk /f fixes file-system errors on a disk volume, not corrupted OS system files.",
                "C": "diskpart is an interactive partition/volume manager; it doesn't repair system files.",
                "D": "gpupdate /force reapplies Group Policy settings — unrelated to file corruption.",
            },
            "exam_pattern": "Corrupt system files = sfc /scannow; disk/file-system errors = chkdsk; deeper "
                            "image repair = DISM /Online /Cleanup-Image /RestoreHealth.",
        },
    },
    {
        "id": "aplus2-os-004", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_features", "difficulty": 2, "type": "mcq",
        "stem": "A user needs to copy a single 12 GB video file onto a USB flash drive and read/write "
                "it on both Windows and macOS. Which file system should the drive be formatted with?",
        "options": [
            {"id": "A", "text": "exFAT"},
            {"id": "B", "text": "FAT32"},
            {"id": "C", "text": "NTFS"},
            {"id": "D", "text": "ext4"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "exFAT has no practical 4 GB file-size cap and is read/write on both Windows and "
                       "macOS, making it ideal for large files on cross-platform removable media.",
            "distractors": {
                "B": "FAT32 caps individual files at 4 GB, so it cannot hold a 12 GB file.",
                "C": "NTFS handles large files but macOS mounts it read-only by default, breaking cross-platform write.",
                "D": "ext4 is a Linux file system that Windows and macOS do not natively read or write.",
            },
            "exam_pattern": "exFAT = large files + cross-platform (Win/mac) flash media; FAT32 capped at 4 GB files; NTFS = Windows.",
        },
    },
    {
        "id": "aplus2-os-005", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "os_installation", "difficulty": 2, "type": "mcq",
        "stem": "A technician is performing a clean install of Windows 11 on a new 4 TB drive and wants "
                "to use the entire capacity and boot in UEFI mode with Secure Boot. Which partitioning "
                "scheme must the drive use?",
        "options": [
            {"id": "A", "text": "GPT"},
            {"id": "B", "text": "MBR"},
            {"id": "C", "text": "exFAT"},
            {"id": "D", "text": "Dynamic disk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GPT supports volumes larger than 2 TB and is required to boot Windows in native "
                       "UEFI/Secure Boot mode, so it uses the full 4 TB.",
            "distractors": {
                "B": "MBR tops out at 2 TB and 4 primary partitions, and pairs with legacy BIOS boot — it can't use the full drive.",
                "C": "exFAT is a file system, not a partition scheme, so it doesn't answer this.",
                "D": "Dynamic disk is a Windows disk TYPE (vs basic) for spanning/mirroring; it's unrelated to UEFI booting a 4 TB drive.",
            },
            "exam_pattern": "UEFI + drives > 2 TB = GPT; legacy BIOS/MBR caps at 2 TB and 4 primary partitions.",
        },
    },
    {
        "id": "aplus2-os-006", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "networking_os", "difficulty": 2, "type": "mcq",
        "stem": "From a Windows command line, a technician needs to map the shared folder "
                "\\\\fileserver\\projects to drive letter S:. Which command does this?",
        "options": [
            {"id": "A", "text": "net use S: \\\\fileserver\\projects"},
            {"id": "B", "text": "net user S: \\\\fileserver\\projects"},
            {"id": "C", "text": "nslookup \\\\fileserver\\projects"},
            {"id": "D", "text": "netstat -S \\\\fileserver\\projects"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "net use <drive>: <UNC path> maps a shared network folder to a drive letter from the CLI.",
            "distractors": {
                "B": "net user creates and manages local/domain user accounts — it does not map drives.",
                "C": "nslookup queries DNS name resolution; it can't mount a share.",
                "D": "netstat displays active connections and listening ports; it doesn't map drives.",
            },
            "exam_pattern": "Map a network drive from CLI = net use <letter>: \\\\server\\share.",
        },
    },
    {
        "id": "aplus2-os-007", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 1, "type": "mcq",
        "stem": "A macOS user accidentally deleted a document last week and wants to restore the "
                "earlier version using Apple's built-in backup utility. Which feature should they use?",
        "options": [
            {"id": "A", "text": "Time Machine"},
            {"id": "B", "text": "Spotlight"},
            {"id": "C", "text": "Mission Control"},
            {"id": "D", "text": "Disk Utility"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Time Machine is macOS's automatic backup tool; the user can browse back in time "
                       "to a previous date and restore the deleted file.",
            "distractors": {
                "B": "Spotlight is the system-wide search feature, not a backup/restore tool.",
                "C": "Mission Control arranges open windows, spaces and desktops — it doesn't recover files.",
                "D": "Disk Utility formats, partitions and repairs disks (First Aid); it is not a file backup system.",
            },
            "exam_pattern": "macOS: Time Machine = backups, Spotlight = search, Disk Utility = format/repair, Keychain = passwords.",
        },
    },
    {
        "id": "aplus2-os-008", "exam": "aplus2", "domain": "operating_systems",
        "subtopic": "macos_linux", "difficulty": 2, "type": "mcq",
        "stem": "On a Linux workstation a user downloaded a shell script named deploy.sh and needs to "
                "make it executable before running it. Which command accomplishes this?",
        "options": [
            {"id": "A", "text": "chmod +x deploy.sh"},
            {"id": "B", "text": "chown root deploy.sh"},
            {"id": "C", "text": "grep deploy.sh"},
            {"id": "D", "text": "ls -l deploy.sh"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chmod changes a file's permission bits; +x adds the execute permission so the "
                       "script can be run.",
            "distractors": {
                "B": "chown changes the file's OWNER, not its execute permission.",
                "C": "grep searches for text patterns within files; it doesn't set permissions.",
                "D": "ls -l only LISTS a file's permissions and details — it shows them but changes nothing.",
            },
            "exam_pattern": "chmod = change permissions (+x execute); chown = change owner; ls -l shows permissions.",
        },
    },

    # ===== 2.0 Security =====================================================
    {
        "id": "aplus2-sec-001", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "A secure login requires a password plus a one-time code generated by an authenticator "
                "app on the user's phone. Which two categories of authentication factors does this use?",
        "options": [
            {"id": "A", "text": "Something you know and something you have"},
            {"id": "B", "text": "Something you know and something you are"},
            {"id": "C", "text": "Something you have and somewhere you are"},
            {"id": "D", "text": "Something you are and something you do"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The password is 'something you know' and the authenticator app on the phone is "
                       "'something you have,' so this is true multifactor authentication.",
            "distractors": {
                "B": "'Something you are' is a biometric (fingerprint, face) — no biometric is used here.",
                "C": "'Somewhere you are' is a location/geolocation factor, which isn't part of this login.",
                "D": "'Something you do' is a behavioral factor (gesture, typing rhythm); neither it nor a biometric is used.",
            },
            "exam_pattern": "Factors: know (password/PIN), have (token/phone/smart card), are (biometric). MFA = two or more DIFFERENT categories.",
        },
    },
    {
        "id": "aplus2-sec-002", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "A user's documents are now inaccessible and an on-screen message demands payment in "
                "cryptocurrency in exchange for a key to unlock them. Which type of malware is this?",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Rootkit"},
            {"id": "C", "text": "Keylogger"},
            {"id": "D", "text": "Spyware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ransomware encrypts the victim's files and demands payment (often in cryptocurrency) "
                       "for the decryption key — exactly the behavior described.",
            "distractors": {
                "B": "A rootkit hides itself and maintains stealthy privileged access; it doesn't ransom files.",
                "C": "A keylogger secretly records keystrokes to steal credentials, not encrypt data for ransom.",
                "D": "Spyware covertly gathers information about the user; it doesn't lock files for payment.",
            },
            "exam_pattern": "Files encrypted + payment demand = ransomware; hidden admin-level persistence = rootkit; captured keystrokes = keylogger.",
        },
    },
    {
        "id": "aplus2-sec-003", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 1, "type": "mcq",
        "stem": "An unauthorized person slips through a badge-secured door by walking in closely behind "
                "an employee who just swiped their card. Which attack is this?",
        "options": [
            {"id": "A", "text": "Tailgating"},
            {"id": "B", "text": "Shoulder surfing"},
            {"id": "C", "text": "Phishing"},
            {"id": "D", "text": "Dumpster diving"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tailgating is following an authorized person through a secured entry point without "
                       "presenting your own credentials.",
            "distractors": {
                "B": "Shoulder surfing is secretly watching someone enter a password or PIN, not following them through a door.",
                "C": "Phishing uses fraudulent messages to trick victims into revealing information or clicking links.",
                "D": "Dumpster diving is searching discarded trash for useful information.",
            },
            "exam_pattern": "Following someone through a secure door = tailgating; a mantrap/access control vestibule is the classic countermeasure.",
        },
    },
    {
        "id": "aplus2-sec-004", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 3, "type": "mcq",
        "stem": "A user's account has Full Control NTFS permission on a shared folder, but the Share "
                "permission for their group is set to Read. The user opens the folder from another PC "
                "across the network. What is their effective permission?",
        "options": [
            {"id": "A", "text": "Read"},
            {"id": "B", "text": "Full Control"},
            {"id": "C", "text": "Modify"},
            {"id": "D", "text": "No access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When a resource is reached over the network, Windows applies the MORE restrictive of "
                       "the combined NTFS and Share permissions. Full Control (NTFS) vs Read (Share) resolves to Read.",
            "distractors": {
                "B": "Full Control is only the NTFS side; the Read share permission overrides it for network access.",
                "C": "Modify is neither of the two permissions in play and isn't the intersection of them.",
                "D": "The user does have access — Read — so 'No access' is wrong.",
            },
            "exam_pattern": "Network access: effective permission = the MORE restrictive of combined NTFS vs combined Share. Local access ignores Share permissions.",
        },
    },
    {
        "id": "aplus2-sec-005", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "multi",
        "stem": "A technician is hardening shared lab workstations against malware and unauthorized "
                "access. Which TWO actions improve the security posture? (Choose two.)",
        "options": [
            {"id": "A", "text": "Disable AutoRun/AutoPlay for removable media"},
            {"id": "B", "text": "Enforce a strong password policy with account lockout"},
            {"id": "C", "text": "Disable Windows Defender Firewall on all machines"},
            {"id": "D", "text": "Add every lab user to the local Administrators group"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Disabling AutoRun stops malware on inserted USB drives from launching automatically, and "
                       "a strong password policy with lockout resists guessing/brute-force — both harden the system.",
            "distractors": {
                "C": "Turning off the firewall removes a protective control and WEAKENS security — the opposite of hardening.",
                "D": "Making everyone a local administrator violates least privilege and lets any user (or their malware) change the system.",
            },
            "exam_pattern": "Harden = disable AutoRun, enforce strong passwords/lockout, patch, least privilege. Never 'harden' by disabling the firewall or handing out admin.",
        },
    },
    {
        "id": "aplus2-sec-006", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "mcq",
        "stem": "A hospital must guarantee that data on failed magnetic hard drives is unrecoverable "
                "before the drives leave the building, and the drives will NOT be reused. Which method "
                "is the MOST appropriate?",
        "options": [
            {"id": "A", "text": "Shredding the drives"},
            {"id": "B", "text": "Performing a quick format"},
            {"id": "C", "text": "Deleting the files and emptying the Recycle Bin"},
            {"id": "D", "text": "Overwriting once, then redeploying the drives"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shredding physically destroys the platters so data can never be recovered, and the "
                       "drive is not reused — the right choice when disposal and certainty are required.",
            "distractors": {
                "B": "A quick format only clears the file table; the underlying data remains and is recoverable.",
                "C": "Deleting files and emptying the Recycle Bin removes pointers only — the data is trivially recoverable.",
                "D": "A single overwrite then redeploy is sanitization for REUSE, but the requirement is destruction with the drive not reused and removed from the building.",
            },
            "exam_pattern": "Physical destruction (shred/drill/incinerate/degauss) = unrecoverable & not reused; wiping/overwrite = sanitize for REUSE; format/delete are NOT secure.",
        },
    },

    # ===== 3.0 Software Troubleshooting =====================================
    {
        "id": "aplus2-swts-001", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A Windows PC began throwing frequent blue screens (BSOD/STOP errors) immediately after "
                "the user installed a new graphics driver. What is the BEST first step to resolve it?",
        "options": [
            {"id": "A", "text": "Boot into Safe Mode and roll back the graphics driver in Device Manager"},
            {"id": "B", "text": "Perform a clean reinstall of Windows"},
            {"id": "C", "text": "Replace the motherboard"},
            {"id": "D", "text": "Run a disk defragmentation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The crashes started right after the driver change, so rolling back the driver (from "
                       "Safe Mode if Windows won't stay up) directly undoes the likely cause.",
            "distractors": {
                "B": "Reinstalling Windows is drastic and premature when a simple driver rollback likely fixes it.",
                "C": "Replacing hardware is unjustified; nothing points to a failed motherboard, and the trigger was a driver.",
                "D": "Defragmentation addresses disk fragmentation/performance, not driver-induced STOP errors.",
            },
            "exam_pattern": "BSOD right after a driver/update change -> roll back the driver/update (Safe Mode if needed) before drastic steps.",
        },
    },
    {
        "id": "aplus2-swts-002", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A Windows 10 PC takes a very long time to reach the desktop because too many applications "
                "launch at boot. Which tool lets the technician disable unnecessary startup programs?",
        "options": [
            {"id": "A", "text": "Task Manager, Startup tab"},
            {"id": "B", "text": "Disk Management"},
            {"id": "C", "text": "Device Manager"},
            {"id": "D", "text": "Windows Defender"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In Windows 10/11 the Startup tab of Task Manager lists auto-start programs and lets you "
                       "disable them (msconfig's Startup tab now redirects here).",
            "distractors": {
                "B": "Disk Management handles partitions and volumes, not startup applications.",
                "C": "Device Manager manages hardware and drivers, not which programs launch at boot.",
                "D": "Windows Defender is antivirus/antimalware; it doesn't control the startup program list.",
            },
            "exam_pattern": "Manage startup programs in Win10/11 = Task Manager > Startup (msconfig's old job).",
        },
    },
    {
        "id": "aplus2-swts-003", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "Following CompTIA's best-practice procedure for malware removal, a technician has just "
                "investigated and verified the malware symptoms on a PC. What is the NEXT step?",
        "options": [
            {"id": "A", "text": "Quarantine the infected system"},
            {"id": "B", "text": "Educate the end user"},
            {"id": "C", "text": "Schedule scans and run updates"},
            {"id": "D", "text": "Enable System Restore and create a restore point"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "After verifying symptoms, the next step is to quarantine the infected system so the "
                       "malware cannot spread while you work on it.",
            "distractors": {
                "B": "Educating the end user is the FINAL (7th) step, done after the system is clean.",
                "C": "Scheduling scans and running updates is step 5, part of ongoing remediation — not immediately after identification.",
                "D": "You DISABLE System Restore early (step 3); re-enabling it and creating a restore point is step 6, near the end.",
            },
            "exam_pattern": "Malware 7 steps: Investigate -> Quarantine -> Disable System Restore -> Remediate -> Schedule scans/update -> Re-enable System Restore -> Educate.",
        },
    },
    {
        "id": "aplus2-swts-004", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "On one user's PC, many HTTPS websites throw 'Your connection is not private' / invalid "
                "certificate errors, yet the same sites load fine on other computers. What should the "
                "technician check FIRST?",
        "options": [
            {"id": "A", "text": "The PC's system date and time"},
            {"id": "B", "text": "Whether every one of those websites is down at once"},
            {"id": "C", "text": "Whether the keyboard is failing"},
            {"id": "D", "text": "Whether the router needs a firmware update"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An incorrect system clock makes valid certificates appear expired or not-yet-valid, so "
                       "TLS validation fails across many sites — and the problem is isolated to that one PC.",
            "distractors": {
                "B": "Every one of those sites being down simultaneously is implausible and would affect all computers, not just one.",
                "C": "A failing keyboard has nothing to do with certificate trust errors.",
                "D": "A router firmware issue would affect all devices on the network, not cause cert errors on a single PC.",
            },
            "exam_pattern": "Cert 'not valid / not private' errors on many sites but one PC only -> check that PC's date/time first.",
        },
    },
    {
        "id": "aplus2-swts-005", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A company smartphone suddenly has very poor battery life, feels hot even when idle, and "
                "shows a spike in cellular data usage. The technician suspects a rogue app. What is the "
                "BEST first step?",
        "options": [
            {"id": "A", "text": "Review per-app battery and data usage in Settings and uninstall the suspicious app"},
            {"id": "B", "text": "Replace the phone's battery immediately"},
            {"id": "C", "text": "Perform a factory reset before investigating"},
            {"id": "D", "text": "Permanently disable the cellular radio"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The battery/data usage screens pinpoint which app is consuming resources, so you can "
                       "uninstall the offending app — a targeted, least-invasive first step.",
            "distractors": {
                "B": "Swapping the battery ignores the symptom pattern (overheating + data spike) that points to software.",
                "C": "A factory reset is a last resort and wipes user data; investigate and remove the app first.",
                "D": "Disabling cellular permanently breaks the phone's purpose and doesn't remove the rogue app.",
            },
            "exam_pattern": "Mobile: fast drain + overheating + data spike -> check per-app battery/data usage and uninstall the rogue app before wiping.",
        },
    },

    # ===== 4.0 Operational Procedures =======================================
    {
        "id": "aplus2-ops-001", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 1, "type": "mcq",
        "stem": "A new technician asks for the exact, repeatable step-by-step instructions the team "
                "follows to image and configure a new laptop. Which type of document provides this?",
        "options": [
            {"id": "A", "text": "Standard operating procedure (SOP)"},
            {"id": "B", "text": "Network topology diagram"},
            {"id": "C", "text": "Incident report"},
            {"id": "D", "text": "End-user license agreement (EULA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A standard operating procedure documents the agreed, repeatable steps for a task so "
                       "everyone performs it consistently.",
            "distractors": {
                "B": "A topology diagram maps how devices connect on the network, not how to perform a task.",
                "C": "An incident report records the details of a specific event after it happens.",
                "D": "A EULA states the legal terms for using software; it is not a work procedure.",
            },
            "exam_pattern": "Step-by-step 'how we do X' = SOP; map of the network = topology diagram.",
        },
    },
    {
        "id": "aplus2-ops-002", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "Before a major server upgrade is submitted to the change advisory board, management asks "
                "what the team will do if the upgrade fails in production. Which element of the change "
                "request answers this?",
        "options": [
            {"id": "A", "text": "The rollback (back-out) plan"},
            {"id": "B", "text": "The scope of the change"},
            {"id": "C", "text": "The risk analysis"},
            {"id": "D", "text": "The purpose of the change"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The rollback/back-out plan documents how to revert the systems to their previous working "
                       "state if the change fails.",
            "distractors": {
                "B": "Scope defines which systems/users the change affects, not how to undo it.",
                "C": "Risk analysis weighs the likelihood and impact of problems, but doesn't itself specify the reversal steps.",
                "D": "Purpose explains WHY the change is being made, not what to do if it fails.",
            },
            "exam_pattern": "'What if it breaks?' = rollback/back-out plan. Scope = what's touched; risk analysis = what could go wrong.",
        },
    },
    {
        "id": "aplus2-ops-003", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A company runs a full backup every Sunday. Each weekday it then backs up only the data "
                "changed since the LAST backup of any type and clears the archive bit, keeping nightly "
                "backups as fast as possible. Which backup type runs on weekdays?",
        "options": [
            {"id": "A", "text": "Incremental"},
            {"id": "B", "text": "Differential"},
            {"id": "C", "text": "Full"},
            {"id": "D", "text": "Synthetic full"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An incremental backup captures only what changed since the last backup of ANY type and "
                       "clears the archive bit — fast to back up, but a restore needs the full plus every increment.",
            "distractors": {
                "B": "A differential backs up everything changed since the last FULL and does NOT clear the archive bit, so it grows larger each day.",
                "C": "A full backup copies all data every time — that's the weekly job, not the quick nightly one.",
                "D": "A synthetic full is assembled from existing backups on the backup server; it isn't the daily changed-data job described.",
            },
            "exam_pattern": "Incremental = since last backup (any), fast backup/slow restore, clears archive bit. Differential = since last FULL, grows daily, restore = full + one diff. (See also the 3-2-1 rule.)",
        },
    },
    {
        "id": "aplus2-ops-004", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 2, "type": "multi",
        "stem": "A technician is about to replace RAM and an expansion card inside a desktop. Which TWO "
                "practices help prevent electrostatic discharge (ESD) damage to the components? (Choose two.)",
        "options": [
            {"id": "A", "text": "Wear an anti-static wrist strap connected to a grounding point"},
            {"id": "B", "text": "Store and transport the components in anti-static bags"},
            {"id": "C", "text": "Work while standing on a carpeted floor"},
            {"id": "D", "text": "Touch the gold edge connectors and chips directly to 'ground' them"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "An anti-static wrist strap keeps you at the same potential as the chassis, and anti-static "
                       "bags protect parts from static while handling/storing them — both reduce ESD risk.",
            "distractors": {
                "C": "Carpet generates static charge; working on it INCREASES the chance of ESD, not reduces it.",
                "D": "You should handle cards by their edges and AVOID touching the gold contacts and chips, which is where ESD does its damage.",
            },
            "exam_pattern": "Prevent ESD: anti-static wrist strap + mat, anti-static bags, raise humidity, handle boards by the edges; avoid carpet and touching contacts.",
        },
    },
    {
        "id": "aplus2-ops-005", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A technician discovers illegal content on a company computer that may become evidence in a "
                "legal case. Documenting every person who handles the drive, and when, from seizure "
                "through to court, is known as what?",
        "options": [
            {"id": "A", "text": "Chain of custody"},
            {"id": "B", "text": "Rollback plan"},
            {"id": "C", "text": "Acceptable use policy"},
            {"id": "D", "text": "Knowledge base article"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Chain of custody is the documented, unbroken record of who controlled the evidence and when, "
                       "preserving its integrity and admissibility.",
            "distractors": {
                "B": "A rollback plan is a change-management concept for reverting a failed change.",
                "C": "An acceptable use policy defines how employees may use company resources.",
                "D": "A knowledge base article is reference documentation for solving known issues.",
            },
            "exam_pattern": "First responder: identify, report through proper channels, preserve the data/device, and document the chain of custody.",
        },
    },
    {
        "id": "aplus2-ops-006", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 1, "type": "mcq",
        "stem": "A frustrated customer is venting at length about a recurring problem. Which response best "
                "demonstrates professional communication?",
        "options": [
            {"id": "A", "text": "Listen actively without interrupting, acknowledge the issue, then explain the next steps"},
            {"id": "B", "text": "Interrupt to correct them and point out what they did wrong"},
            {"id": "C", "text": "Put them on hold and complain about the 'silly' issue to a coworker"},
            {"id": "D", "text": "Tell them it's not your department and end the call"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Actively listening, not interrupting, showing empathy, and clearly explaining next steps "
                       "are core professional-communication behaviors.",
            "distractors": {
                "B": "Interrupting and blaming the customer is dismissive and escalates frustration.",
                "C": "Mocking a customer, even on hold, is unprofessional and breaches basic courtesy.",
                "D": "Brushing the customer off and abandoning the call fails to meet or set expectations.",
            },
            "exam_pattern": "Professionalism: actively listen, don't interrupt, be empathetic, avoid jargon, and set/meet expectations.",
        },
    },
    {
        "id": "aplus2-ops-007", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "mcq",
        "stem": "A technician saved an automation script with a .ps1 file extension. Which scripting "
                "environment is this file intended for?",
        "options": [
            {"id": "A", "text": "Windows PowerShell"},
            {"id": "B", "text": "Linux Bash shell"},
            {"id": "C", "text": "Windows batch (Command Prompt)"},
            {"id": "D", "text": "Python interpreter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The .ps1 extension identifies a Windows PowerShell script.",
            "distractors": {
                "B": "Bash shell scripts use the .sh extension.",
                "C": "Windows batch files use .bat (or .cmd), not .ps1.",
                "D": "Python scripts use the .py extension.",
            },
            "exam_pattern": ".ps1 PowerShell | .bat/.cmd batch | .sh Bash | .py Python | .vbs VBScript | .js JavaScript.",
        },
    },
]
