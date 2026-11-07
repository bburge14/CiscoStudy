"""CompTIA A+ Core 2 (220-1102) — Software Troubleshooting expansion pool.

Original, objective-aligned items that DEEPEN the 3.0 Software Troubleshooting
bank already seeded in content_aplus2.py (ids aplus2-swts-001..005). These are
authored content mapped to the public 220-1102 objectives (3.1 Windows OS
problems, 3.2/3.3 malware & OS-security symptoms, 3.4/3.5 mobile OS & security),
never real exam items. build_content.py shuffles option order, so the answer key
here is not positionally biased.

Subtopics (exactly three): windows_troubleshooting, os_security_troubleshooting,
mobile_os_troubleshooting.
"""

QUESTIONS = [
    # ===== 3.0 Software Troubleshooting — Windows (3.1) ======================
    {
        "id": "aplus2-swts-101", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A desktop that worked yesterday now halts at boot with 'BOOTMGR is missing — "
                "Press Ctrl+Alt+Del to restart.' No hardware was changed and the drive is still "
                "detected in BIOS/UEFI. What is the BEST way to fix it?",
        "options": [
            {"id": "A", "text": "Boot the Windows installation/recovery media into the Windows Recovery "
                                "Environment and run Startup Repair or bootrec /rebuildbcd and bootrec /fixboot"},
            {"id": "B", "text": "Replace the hard drive and reinstall Windows from scratch"},
            {"id": "C", "text": "Reseat the RAM modules"},
            {"id": "D", "text": "Run sfc /scannow from within the running desktop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The boot manager/BCD files are missing or corrupt. Boot into WinRE from "
                       "installation or recovery media and repair the boot files with Startup Repair "
                       "or the bootrec commands (/fixboot, /rebuildbcd). The drive is healthy "
                       "(detected in firmware), so nothing needs replacing.",
            "distractors": {
                "B": "The drive is detected and otherwise fine; replacing it is drastic and destroys data "
                     "when only the boot files are broken.",
                "C": "Reseating RAM addresses memory faults (POST failures/BSODs), not a missing boot manager.",
                "D": "You cannot run sfc from the desktop because the PC won't boot to it, and sfc repairs "
                     "protected system files, not the BCD/boot sector.",
            },
            "exam_pattern": "'BOOTMGR is missing' / 'No OS found' with the drive detected -> boot WinRE and "
                            "rebuild boot files (Startup Repair, bootrec /fixboot and /rebuildbcd).",
        },
    },
    {
        "id": "aplus2-swts-102", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A technician runs sfc /scannow, but it reports 'Windows Resource Protection found "
                "corrupt files but was unable to fix some of them.' The component store itself is "
                "damaged. Which command should be run NEXT so SFC can then succeed?",
        "options": [
            {"id": "A", "text": "DISM /Online /Cleanup-Image /RestoreHealth"},
            {"id": "B", "text": "chkdsk C: /f"},
            {"id": "C", "text": "bootrec /rebuildbcd"},
            {"id": "D", "text": "diskpart clean"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DISM /Online /Cleanup-Image /RestoreHealth repairs the Windows component store "
                       "(WinSxS) using Windows Update as the source; after it completes, re-running "
                       "sfc /scannow can fix the protected files it previously couldn't.",
            "distractors": {
                "B": "chkdsk repairs file-system/disk errors, not a corrupt Windows component store.",
                "C": "bootrec repairs boot configuration data, which is unrelated to SFC's component store.",
                "D": "diskpart clean wipes the partition table and data — destructive and completely wrong here.",
            },
            "exam_pattern": "SFC can't repair -> repair the image with DISM /Online /Cleanup-Image "
                            "/RestoreHealth, then re-run sfc /scannow.",
        },
    },
    {
        "id": "aplus2-swts-103", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "After a sudden power loss, a Windows PC shows repeated errors about missing or corrupt "
                "system DLLs and some built-in apps won't open, but the PC still boots. Which built-in "
                "tool should the technician run FIRST to verify and repair protected OS files?",
        "options": [
            {"id": "A", "text": "sfc /scannow"},
            {"id": "B", "text": "Disk Cleanup"},
            {"id": "C", "text": "format C:"},
            {"id": "D", "text": "Device Manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System File Checker (sfc /scannow) scans all protected operating-system files and "
                       "replaces corrupted ones with known-good cached copies — the right first repair for "
                       "corrupt/missing system files when the OS still boots.",
            "distractors": {
                "B": "Disk Cleanup deletes temporary files to free space; it does not repair system files.",
                "C": "Formatting C: erases the OS and data — far too drastic for repairable file corruption.",
                "D": "Device Manager manages hardware and drivers, not the integrity of system files.",
            },
            "exam_pattern": "Corrupt/missing protected OS files but the PC still boots -> sfc /scannow first "
                            "(then DISM if SFC can't fix them).",
        },
    },
    {
        "id": "aplus2-swts-104", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A Windows 11 laptop became unstable right after a batch of updates and a new application "
                "were installed. The user needs the OS returned to the way it worked yesterday WITHOUT "
                "losing personal documents. What is the BEST option?",
        "options": [
            {"id": "A", "text": "Use System Restore to roll back to a restore point from before the changes"},
            {"id": "B", "text": "Perform a full factory reset that removes everything"},
            {"id": "C", "text": "Run Disk Defragmenter"},
            {"id": "D", "text": "Delete the user's profile"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System Restore reverts system files, drivers, the registry, and installed "
                       "programs/updates to an earlier restore point while leaving personal files intact — "
                       "ideal for undoing recent destabilizing changes.",
            "distractors": {
                "B": "A factory reset that removes everything would wipe the user's documents — the opposite "
                     "of the requirement.",
                "C": "Defragmenting reorganizes files on disk for performance; it does not undo problematic "
                     "updates or applications.",
                "D": "Deleting the profile destroys the user's settings and data and still doesn't roll back "
                     "the system changes.",
            },
            "exam_pattern": "Undo recent bad updates/apps but keep user files -> System Restore (restore "
                            "point); reset/reimage only when restore can't recover it.",
        },
    },
    {
        "id": "aplus2-swts-105", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A workstation reboots instantly whenever a blue screen occurs, so the technician can't "
                "read the STOP code. Which change lets them see the BSOD details on screen before it "
                "reboots?",
        "options": [
            {"id": "A", "text": "In System Properties > Advanced > Startup and Recovery, clear the "
                                "'Automatically restart' checkbox"},
            {"id": "B", "text": "Enable Fast Startup in Power Options"},
            {"id": "C", "text": "Turn on BitLocker"},
            {"id": "D", "text": "Increase the page file size"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Clearing 'Automatically restart' under Startup and Recovery (System failure) keeps "
                       "the blue screen displayed instead of instantly rebooting, so the STOP code/driver "
                       "can be recorded. The same details are also written to Event Viewer and the memory dump.",
            "distractors": {
                "B": "Fast Startup speeds boot via a hybrid shutdown; it has nothing to do with showing "
                     "BSOD details.",
                "C": "BitLocker encrypts the drive; it doesn't affect crash-display behavior.",
                "D": "Enlarging the page file can allow a larger dump, but it does not stop the auto-reboot "
                     "that hides the STOP code.",
            },
            "exam_pattern": "Can't read the STOP code because it reboots instantly -> disable 'Automatically "
                            "restart' (Startup and Recovery), or read the dump/Event Viewer.",
        },
    },
    {
        "id": "aplus2-swts-106", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A PC suffers random freezes the technician suspects are caused by one of many "
                "third-party background services or startup items. Which tool starts Windows with "
                "non-Microsoft services and startup items disabled (a 'clean boot') to isolate the culprit?",
        "options": [
            {"id": "A", "text": "System Configuration (msconfig)"},
            {"id": "B", "text": "Disk Management"},
            {"id": "C", "text": "Resource Monitor"},
            {"id": "D", "text": "Registry Editor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System Configuration (msconfig) performs a clean/diagnostic boot — on the Services "
                       "tab you 'Hide all Microsoft services' and disable the rest, then re-enable items in "
                       "batches to find the offending service.",
            "distractors": {
                "B": "Disk Management handles partitions and volumes, not which services and startup items load.",
                "C": "Resource Monitor shows live CPU/disk/network/memory usage but doesn't disable services "
                     "for a clean boot.",
                "D": "Registry Editor edits registry keys directly; it is not the tool for performing a "
                     "controlled clean boot.",
            },
            "exam_pattern": "Isolate a third-party service/startup conflict -> msconfig clean/diagnostic boot; "
                            "startup apps themselves are managed in Task Manager > Startup.",
        },
    },
    {
        "id": "aplus2-swts-107", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "multi",
        "stem": "A Windows PC has been crashing intermittently over the past week. Which TWO built-in "
                "tools BEST help the technician review a history of the errors and correlate them with "
                "recent software changes? (Choose two.)",
        "options": [
            {"id": "A", "text": "Event Viewer"},
            {"id": "B", "text": "Reliability Monitor"},
            {"id": "C", "text": "Disk Cleanup"},
            {"id": "D", "text": "Disk Management"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Event Viewer logs detailed system/application errors and warnings over time, and "
                       "Reliability Monitor presents a day-by-day stability timeline that lines crashes up "
                       "with installs and updates — together they pinpoint when and why the instability began.",
            "distractors": {
                "C": "Disk Cleanup only deletes temporary files to reclaim space; it keeps no error history.",
                "D": "Disk Management manages partitions and volumes and provides no crash or error log.",
            },
            "exam_pattern": "Review crash history and correlate with changes -> Event Viewer (logs) + "
                            "Reliability Monitor (stability timeline).",
        },
    },

    # ===== 3.0 Software Troubleshooting — OS security (3.2 / 3.3) ============
    {
        "id": "aplus2-swts-108", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "On one PC, typing a well-known banking URL loads a convincing fake site, yet other "
                "computers reach the real site and this PC's DNS settings look normal. Which file has "
                "MOST likely been altered by malware to redirect the domain?",
        "options": [
            {"id": "A", "text": "The hosts file (C:\\Windows\\System32\\drivers\\etc\\hosts)"},
            {"id": "B", "text": "boot.ini"},
            {"id": "C", "text": "pagefile.sys"},
            {"id": "D", "text": "The SAM database"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A malicious entry in the local hosts file maps the bank's domain to an attacker's IP, "
                       "so that one PC is redirected regardless of DNS. Inspect and clean the hosts file and "
                       "scan for malware.",
            "distractors": {
                "B": "boot.ini is a legacy boot-configuration file (pre-Vista); it plays no part in name "
                     "resolution or redirection.",
                "C": "pagefile.sys is virtual-memory swap space; editing it would not redirect a website.",
                "D": "The SAM stores local account password hashes; it doesn't map hostnames to addresses.",
            },
            "exam_pattern": "One PC redirected to a fake site while DNS is fine -> check the hosts file for "
                            "malicious entries.",
        },
    },
    {
        "id": "aplus2-swts-109", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A pop-up covering the screen warns 'Windows detected 5 viruses! Call 1-800-XXX-XXXX or "
                "click here to buy FullCleanPro now.' The user never installed that program. What should "
                "the technician do?",
        "options": [
            {"id": "A", "text": "Treat it as a fake/rogue antivirus (scareware): don't call or pay, and "
                                "remove the malware with legitimate anti-malware (in Safe Mode if needed)"},
            {"id": "B", "text": "Call the number so the viruses get removed quickly"},
            {"id": "C", "text": "Purchase the advertised program to clear the alert"},
            {"id": "D", "text": "Ignore it; genuine Windows Security pop-ups always include a payment link"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Unsolicited 'pay now / call this number' virus warnings are classic rogue "
                       "antivirus/scareware. Don't engage or pay; remove the underlying malware with a "
                       "trusted anti-malware tool, booting to Safe Mode or a preinstallation environment if "
                       "it blocks you.",
            "distractors": {
                "B": "The number reaches the scammers, who will try to extract money or remote access — "
                     "never call it.",
                "C": "Paying rewards the attacker and does not clean the system; the 'product' is fraudulent.",
                "D": "Legitimate Windows Security alerts never demand payment or a phone call; that wording "
                     "is a red flag, not proof of authenticity.",
            },
            "exam_pattern": "'Pay now / call this number' virus warning = rogue AV/scareware -> don't pay or "
                            "call; remove with legitimate anti-malware.",
        },
    },
    {
        "id": "aplus2-swts-110", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user reports constant browser pop-ups, and now Task Manager, Registry Editor, and UAC "
                "prompts are all disabled with 'disabled by your administrator' messages — though no admin "
                "made those changes. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A malware infection that disabled the security/management tools to protect itself"},
            {"id": "B", "text": "A failing hard drive"},
            {"id": "C", "text": "An exhausted laptop battery"},
            {"id": "D", "text": "An outdated graphics driver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Malware commonly disables Task Manager, regedit, and UAC (and throws pop-ups) to keep "
                       "the user from inspecting or stopping it. The combination of symptoms points to "
                       "infection; begin the malware-removal procedure.",
            "distractors": {
                "B": "A failing drive causes slow access, read errors, or boot failure — not disabled "
                     "management tools and pop-ups.",
                "C": "A dead battery powers the device off; it doesn't selectively disable Windows security tools.",
                "D": "An old GPU driver may cause display glitches or BSODs, not disabled Task Manager/regedit/UAC "
                     "with pop-ups.",
            },
            "exam_pattern": "Task Manager/regedit/UAC disabled + pop-ups = compromise -> start malware removal "
                            "(Safe Mode / anti-malware).",
        },
    },
    {
        "id": "aplus2-swts-111", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "After multiple anti-malware scans and removals, a PC keeps getting reinfected and still "
                "behaves abnormally; a rootkit is suspected. Per best practice, what is the MOST reliable "
                "way to return the system to a trusted state?",
        "options": [
            {"id": "A", "text": "Reimage/reinstall the OS from known-good media and restore data from a clean backup"},
            {"id": "B", "text": "Run the same antivirus scan a fourth time"},
            {"id": "C", "text": "Hide the symptoms by disabling the alerts"},
            {"id": "D", "text": "Replace the power supply"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When malware — especially a rootkit — can't be reliably removed and symptoms persist, "
                       "the trustworthy path is to wipe and reimage/reinstall the OS from known-good media and "
                       "restore data from a clean backup.",
            "distractors": {
                "B": "Repeating the same scan that already failed is unlikely to remove a persistent rootkit.",
                "C": "Disabling alerts only hides symptoms while the infection remains active — it fixes nothing.",
                "D": "Replacing the power supply addresses a hardware/power fault, not a software compromise.",
            },
            "exam_pattern": "Persistent/rootkit infection that won't clean -> reimage from known-good media and "
                            "restore from a clean backup.",
        },
    },
    {
        "id": "aplus2-swts-112", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Several of a user's contacts report receiving spam 'from' the user, and the user's Sent "
                "folder contains messages they never wrote. Which response BEST addresses a likely "
                "compromised email account?",
        "options": [
            {"id": "A", "text": "Change the account password to a strong, unique one, enable MFA, and scan "
                                "the device for malware"},
            {"id": "B", "text": "Delete all of the user's contacts"},
            {"id": "C", "text": "Create a brand-new email address and abandon the old one without further action"},
            {"id": "D", "text": "Turn off the computer's firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spam sent from the account and unknown Sent items indicate a hijacked account. Regain "
                       "control by setting a strong, unique password, enabling multifactor authentication, and "
                       "scanning the device for credential-stealing malware.",
            "distractors": {
                "B": "Deleting contacts neither secures the account nor stops the attacker from using it.",
                "C": "Abandoning the address ignores the root cause (stolen credentials/malware) and loses the "
                     "user's history.",
                "D": "Disabling the firewall reduces protection and does nothing to reclaim the compromised account.",
            },
            "exam_pattern": "Account sending spam / unknown Sent mail = hijacked account -> change password, "
                            "enable MFA, scan for malware.",
        },
    },
    {
        "id": "aplus2-swts-113", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Windows Update repeatedly fails to install with an error, and the problem persists across "
                "reboots. Which step is the BEST first fix?",
        "options": [
            {"id": "A", "text": "Run the Windows Update troubleshooter, then reset the update components by "
                                "stopping the services and clearing the SoftwareDistribution cache"},
            {"id": "B", "text": "Reinstall Windows from scratch"},
            {"id": "C", "text": "Replace the system board"},
            {"id": "D", "text": "Disconnect the PC from the Internet permanently"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "For failing updates, start with the built-in Windows Update troubleshooter; if it "
                       "persists, reset the update components by stopping the update services and clearing the "
                       "SoftwareDistribution download cache so the files are re-fetched cleanly.",
            "distractors": {
                "B": "Reinstalling Windows is far too drastic as a first response to an update error.",
                "C": "A failing system board doesn't present as Windows Update errors; replacing it is unjustified.",
                "D": "Disconnecting from the Internet makes updating impossible instead of fixing the failure.",
            },
            "exam_pattern": "Updates fail with an error -> Windows Update troubleshooter, then reset components "
                            "(clear SoftwareDistribution) before any drastic step.",
        },
    },
    {
        "id": "aplus2-swts-114", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "In CompTIA's malware-removal procedure, the technician disables System Restore on a Windows "
                "PC before remediating. Why is this step important?",
        "options": [
            {"id": "A", "text": "Restore points can contain the malware, so a later restore could reinfect "
                                "the system; disabling it purges those infected points"},
            {"id": "B", "text": "System Restore permanently deletes user documents if left enabled"},
            {"id": "C", "text": "System Restore prevents antivirus software from installing"},
            {"id": "D", "text": "Disabling it speeds up the CPU during scanning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Malware can be captured inside restore points; rolling back later would reintroduce the "
                       "infection. Disabling System Restore before remediation purges those infected points, so "
                       "you re-enable it and create a fresh, clean restore point afterward.",
            "distractors": {
                "B": "System Restore does not delete personal documents; it reverts system files and settings, "
                     "not user data.",
                "C": "System Restore does not block antivirus installation.",
                "D": "Toggling System Restore has no effect on CPU speed.",
            },
            "exam_pattern": "Disable System Restore during malware removal so infected restore points can't "
                            "reinfect; re-enable and make a clean point at the end.",
        },
    },

    # ===== 3.0 Software Troubleshooting — Mobile OS & security (3.4 / 3.5) ===
    {
        "id": "aplus2-swts-115", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user's smartphone has a bulging back cover, and the screen is being pushed up by a "
                "swollen battery. What is the correct action?",
        "options": [
            {"id": "A", "text": "Power the device down, stop charging/using it, do NOT puncture it, and have "
                                "the swollen battery safely replaced and recycled"},
            {"id": "B", "text": "Press the battery back into place and keep using the phone"},
            {"id": "C", "text": "Puncture the battery to release the built-up gas"},
            {"id": "D", "text": "Put the phone in a freezer and continue charging it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A swollen lithium-ion battery is a fire/rupture hazard. Power off, stop charging and "
                       "using it, avoid any pressure, and never puncture it; have it replaced and recycled "
                       "through proper channels.",
            "distractors": {
                "B": "Forcing a swollen battery back into place stresses it further and risks rupture or fire.",
                "C": "Puncturing a lithium battery can make it ignite or explode and releases hazardous "
                     "chemicals — extremely dangerous.",
                "D": "Freezing and continuing to charge a damaged battery adds thermal and electrical stress "
                     "and does not make it safe.",
            },
            "exam_pattern": "Swollen/bulging battery -> stop using, power off, do NOT puncture, replace and "
                            "recycle safely.",
        },
    },
    {
        "id": "aplus2-swts-116", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "On an otherwise healthy phone, one app repeatedly crashes or fails to load while every "
                "other app works fine. What is the BEST first troubleshooting step for that app?",
        "options": [
            {"id": "A", "text": "Force close the app and update it; if it still fails, clear its cache/data "
                                "or uninstall and reinstall it"},
            {"id": "B", "text": "Immediately perform a full factory reset of the phone"},
            {"id": "C", "text": "Replace the phone's screen"},
            {"id": "D", "text": "Disable the device's cellular radio"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When a single app misbehaves, target that app: force stop it, install any update, and "
                       "if needed clear its cache/data (Android) or delete and reinstall it. This resolves most "
                       "app-specific corruption without touching the rest of the device.",
            "distractors": {
                "B": "A factory reset wipes the whole device and user data — far too drastic for one "
                     "misbehaving app.",
                "C": "A screen swap is a hardware fix unrelated to a single app crashing.",
                "D": "Turning off cellular doesn't fix app-file corruption and disables connectivity the app "
                     "may need.",
            },
            "exam_pattern": "One app crashing while others work -> update/force stop, then clear its cache/data "
                            "or reinstall; reset the whole device only as a last resort.",
        },
    },
    {
        "id": "aplus2-swts-117", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A smartphone is completely frozen — the touchscreen won't respond and no button brings up "
                "any menu. What should the technician try FIRST?",
        "options": [
            {"id": "A", "text": "Perform a forced restart (soft reset), e.g., holding the power and volume "
                                "buttons until it reboots"},
            {"id": "B", "text": "Factory reset the device from a computer"},
            {"id": "C", "text": "Replace the digitizer"},
            {"id": "D", "text": "Let the battery fully drain over several days"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A forced restart (soft reset) — typically holding power plus a volume button — reboots "
                       "a frozen device without erasing data and clears the temporary hang. It is the correct, "
                       "least-invasive first step.",
            "distractors": {
                "B": "A factory reset erases user data and is unnecessary for a simple freeze; try a forced "
                     "restart first.",
                "C": "Replacing the digitizer assumes a hardware fault before trying the quick software reset.",
                "D": "Waiting days for the battery to drain is impractical; a forced restart recovers it "
                     "immediately.",
            },
            "exam_pattern": "Frozen/unresponsive phone -> forced restart (soft reset) first; factory reset only "
                            "if the freezing keeps recurring.",
        },
    },
    {
        "id": "aplus2-swts-118", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A user can send and receive normal email on their phone but cannot open encrypted (S/MIME) "
                "messages, which show a decryption/certificate error. What is the MOST likely fix?",
        "options": [
            {"id": "A", "text": "Install or renew the user's email encryption certificate (S/MIME digital "
                                "certificate) on the device"},
            {"id": "B", "text": "Increase the screen brightness"},
            {"id": "C", "text": "Clear the phone's call log"},
            {"id": "D", "text": "Toggle auto-rotate off"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Opening S/MIME-encrypted mail requires the user's valid certificate (with its private "
                       "key) on the device. A missing, expired, or not-yet-installed certificate causes the "
                       "decryption error, so install or renew the S/MIME certificate.",
            "distractors": {
                "B": "Screen brightness has nothing to do with decrypting email.",
                "C": "Clearing the call log does not affect email certificates.",
                "D": "Auto-rotate is a display setting unrelated to encryption.",
            },
            "exam_pattern": "Can't open encrypted (S/MIME) email -> missing/expired certificate; install or "
                            "renew the email certificate on the device.",
        },
    },
    {
        "id": "aplus2-swts-119", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user's phone won't connect to a new Bluetooth headset. Both devices are charged and "
                "nearby. Which step is MOST likely to establish the connection?",
        "options": [
            {"id": "A", "text": "Put the headset into pairing/discoverable mode and pair it from the phone, "
                                "removing any stale pairing and entering the PIN if prompted"},
            {"id": "B", "text": "Turn on Airplane mode"},
            {"id": "C", "text": "Permanently disable the phone's Wi-Fi"},
            {"id": "D", "text": "Replace the phone's SIM card"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bluetooth pairing requires the accessory to be in pairing/discoverable mode and within "
                       "range; initiate pairing from the phone, and if a previous or partial pairing exists, "
                       "'forget' it and re-pair (supplying the PIN/passkey if asked).",
            "distractors": {
                "B": "Airplane mode disables the radios, including Bluetooth, preventing any connection.",
                "C": "Disabling Wi-Fi is unrelated to Bluetooth pairing and isn't required.",
                "D": "The SIM card handles cellular service, not Bluetooth pairing.",
            },
            "exam_pattern": "Bluetooth won't connect -> put the accessory in pairing mode, ensure it's in "
                            "range/discoverable, remove any stale pairing and re-pair (enter the PIN).",
        },
    },
    {
        "id": "aplus2-swts-120", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "multi",
        "stem": "Right after a user sideloaded an app from an APK file obtained outside the official store, "
                "their phone shows a spike in data usage, a data-limit notification, and a flood of pop-up "
                "ads. Which TWO actions BEST remediate this likely malicious app? (Choose two.)",
        "options": [
            {"id": "A", "text": "Uninstall the sideloaded/unauthorized app"},
            {"id": "B", "text": "Run a reputable mobile anti-malware scan and review the app's permissions"},
            {"id": "C", "text": "Increase the monthly data-plan allowance"},
            {"id": "D", "text": "Turn off screen auto-rotate"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A sideloaded APK that triggers heavy data use and ad pop-ups is likely malware/adware. "
                       "Remove the offending app and run a reputable mobile anti-malware scan, reviewing and "
                       "revoking suspicious permissions to clean up anything it installed.",
            "distractors": {
                "C": "Raising the data cap just pays for the malware's traffic — it doesn't remove the threat.",
                "D": "Auto-rotate is a display setting and has nothing to do with the malicious app's data/ad "
                     "behavior.",
            },
            "exam_pattern": "High data use + ads after sideloading an APK = mobile malware/adware -> uninstall "
                            "the app and run anti-malware / check permissions (avoid sideloading).",
        },
    },
]
