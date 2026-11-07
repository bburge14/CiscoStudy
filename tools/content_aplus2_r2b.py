"""CompTIA A+ Core 2 (220-1102) — round-2 expansion pool (part B).

Original, objective-aligned items that DEEPEN two domains of the 220-1102 bank to
help match the depth of the CCNA track:

  * 3.0 Software Troubleshooting  (software_troubleshooting)  -- +15
  * 4.0 Operational Procedures    (operational_procedures)    -- +20

These are authored content mapped to the public 220-1102 objectives (3.1 Windows
OS problems, 3.2/3.3 malware & OS-security symptoms + removal, 3.4/3.5 mobile OS &
security; 4.1 documentation, 4.2 change management, 4.3 backup/recovery, 4.4/4.5
safety & environment, 4.6 incident response + 4.7/4.8 licensing/regulated data,
4.7 communication/professionalism, 4.8 scripting), never real exam items.

Scenarios here are deliberately distinct from the already-seeded aplus2 software
troubleshooting (aplus2-swts-001..005 / -101..120) and operational-procedures
(aplus2-ops-001..007 / -101..124) items. build_content.py shuffles option order,
so the answer key below is not positionally biased. IDs carry a -r2- segment so
they cannot collide with any earlier pool.
"""

QUESTIONS = [
    # =====================================================================
    # 3.0 Software Troubleshooting
    # =====================================================================

    # ----- 3.1 Windows OS problems ---------------------------------------
    {
        "id": "aplus2-swts-r2-001", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Users on a workstation suddenly cannot print, and the technician finds the Print "
                "Spooler service is not running. Which built-in console should be used to start the "
                "service AND set its startup type so it launches automatically at every boot?",
        "options": [
            {"id": "A", "text": "The Services console (services.msc)"},
            {"id": "B", "text": "Device Manager"},
            {"id": "C", "text": "Disk Management"},
            {"id": "D", "text": "Event Viewer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Services console (services.msc) lists Windows services, lets you start/stop "
                       "them, and lets you set the Startup type (Automatic/Manual/Disabled) so the Print "
                       "Spooler comes back on its own at boot.",
            "distractors": {
                "B": "Device Manager manages hardware devices and their drivers, not Windows services.",
                "C": "Disk Management handles partitions and volumes, not service state or startup type.",
                "D": "Event Viewer shows logs that can tell you WHY a service stopped, but it cannot start "
                     "the service or change its startup type.",
            },
            "exam_pattern": "Start/stop a Windows service and set its startup type = Services console "
                            "(services.msc); Task Manager's Services tab can only start/stop, not configure startup.",
        },
    },
    {
        "id": "aplus2-swts-r2-002", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A PC is sluggish and shows 100% disk usage. The technician wants to see, in real time, "
                "exactly which process and which file are driving the disk I/O (not just an overall "
                "percentage). Which built-in tool gives this detailed per-process breakdown?",
        "options": [
            {"id": "A", "text": "Resource Monitor (resmon)"},
            {"id": "B", "text": "Disk Cleanup"},
            {"id": "C", "text": "System Restore"},
            {"id": "D", "text": "Registry Editor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resource Monitor breaks CPU, disk, network, and memory usage down per process — "
                       "including which files/handles a process is reading or writing — so you can pinpoint "
                       "the exact cause of the disk thrashing.",
            "distractors": {
                "B": "Disk Cleanup deletes temporary files to reclaim space; it shows no live resource usage.",
                "C": "System Restore rolls the system back to an earlier point; it does not display live I/O.",
                "D": "Registry Editor edits configuration keys; it is not a performance-monitoring tool.",
            },
            "exam_pattern": "Detailed live per-process CPU/disk/network/memory (which file/handle) = Resource "
                            "Monitor; a quick overview or 'end task' = Task Manager.",
        },
    },
    {
        "id": "aplus2-swts-r2-003", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user who keeps many applications and dozens of browser tabs open repeatedly sees "
                "'Your computer is low on memory' warnings, and the system slows to a crawl. Which action "
                "BEST addresses the low-memory condition?",
        "options": [
            {"id": "A", "text": "Close unneeded programs and either add physical RAM or increase the "
                                "virtual-memory (page file) size"},
            {"id": "B", "text": "Run Disk Cleanup to delete temporary files"},
            {"id": "C", "text": "Defragment the hard drive"},
            {"id": "D", "text": "Lower the display resolution"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Low-memory errors mean RAM (plus page file) is exhausted. Close unneeded programs, add "
                       "more physical RAM, and/or increase the page file (virtual memory) so Windows has more "
                       "room to work.",
            "distractors": {
                "B": "Disk Cleanup frees disk SPACE, which is not the same as memory — it won't stop low-RAM warnings.",
                "C": "Defragmenting reorganizes files on disk for access speed; it adds no memory.",
                "D": "Display resolution has a negligible effect on system RAM pressure.",
            },
            "exam_pattern": "Low-memory errors -> close apps, add RAM, or enlarge the page file (virtual memory); "
                            "free disk space is NOT free memory.",
        },
    },
    {
        "id": "aplus2-swts-r2-004", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A single installed desktop application crashes immediately on launch, while every other "
                "program and the OS run normally. After confirming the app is fully updated, what is the "
                "BEST next step to fix just that one application?",
        "options": [
            {"id": "A", "text": "Repair or reinstall that application, and check Event Viewer for the "
                                "faulting module"},
            {"id": "B", "text": "Perform a clean reinstall of the entire Windows OS"},
            {"id": "C", "text": "Replace the hard drive"},
            {"id": "D", "text": "Roll back the graphics driver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When one app misbehaves but the OS and other apps are fine, the problem is scoped to "
                       "that app. Repair it (or uninstall and reinstall it), and use Event Viewer's "
                       "Application log to identify the faulting module if needed.",
            "distractors": {
                "B": "Reinstalling all of Windows is wildly out of proportion to a single broken application.",
                "C": "Replacing the drive is a hardware action with no evidence of hardware failure here.",
                "D": "A graphics-driver rollback addresses display/BSOD issues, not one application failing to start.",
            },
            "exam_pattern": "One app crashes while the OS/other apps are fine -> update, then repair/reinstall "
                            "that app; read Event Viewer for the faulting module.",
        },
    },
    {
        "id": "aplus2-swts-r2-005", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "After several improper shutdowns, Windows reports file-system errors on the C: volume and "
                "some files fail to open with read errors, yet the drive's SMART status is healthy. Which "
                "command checks and repairs LOGICAL file-system errors on the volume?",
        "options": [
            {"id": "A", "text": "chkdsk C: /f  (add /r to also locate bad sectors)"},
            {"id": "B", "text": "sfc /scannow"},
            {"id": "C", "text": "diskpart clean"},
            {"id": "D", "text": "ipconfig /flushdns"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chkdsk with /f fixes file-system structure errors (lost clusters, cross-linked files, "
                       "a dirty volume); /r additionally scans for and recovers from bad sectors. Logical "
                       "corruption after improper shutdowns is exactly what chkdsk repairs.",
            "distractors": {
                "B": "sfc /scannow repairs protected Windows SYSTEM files, not the file-system structures on the volume.",
                "C": "diskpart clean erases the partition table and all data on the disk — destructive and wrong here.",
                "D": "ipconfig /flushdns clears the DNS resolver cache and has nothing to do with disk file systems.",
            },
            "exam_pattern": "Logical file-system/volume errors -> chkdsk /f (/r for bad sectors); sfc/DISM repair "
                            "OS files, not the file system.",
        },
    },
    {
        "id": "aplus2-swts-r2-006", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "windows_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A user signs in and lands on a blank 'temporary' desktop with none of their files or "
                "settings. Event Viewer logs 'The User Profile Service failed the sign-in. User profile "
                "cannot be loaded.' Each reboot repeats it. What is the appropriate fix?",
        "options": [
            {"id": "A", "text": "Rebuild the user's Windows profile — back up their data, then repair the "
                                "profile (correct the ProfileList registry reference or create a fresh "
                                "profile) and migrate the files in"},
            {"id": "B", "text": "Replace the system board"},
            {"id": "C", "text": "Reinstall the last application the user opened"},
            {"id": "D", "text": "Run the Windows Update troubleshooter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A temporary profile with 'User Profile Service failed the sign-in' means the user's "
                       "profile is corrupt or its ProfileList reference is broken. Back up the user's data, "
                       "then rebuild the profile (fix the registry reference or create a new profile) and copy "
                       "the data back.",
            "distractors": {
                "B": "A corrupt profile is a software/account issue; nothing points to a failed motherboard.",
                "C": "The failure happens at sign-in before apps load, so reinstalling an app does not address it.",
                "D": "Windows Update is unrelated to a corrupt local user profile.",
            },
            "exam_pattern": "Temporary profile / 'User Profile Service failed the sign-in' -> rebuild the Windows "
                            "user profile (fix ProfileList or new profile, then migrate data).",
        },
    },

    # ----- 3.2 / 3.3 Malware & OS-security symptoms + removal ------------
    {
        "id": "aplus2-swts-r2-007", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user's browser home page and default search engine changed on their own, unfamiliar "
                "toolbars appeared, and ad pop-ups now load on almost every site — and the changes return "
                "after being reset. What is the BEST remediation?",
        "options": [
            {"id": "A", "text": "Remove the malicious browser extensions and any PUP (potentially unwanted "
                                "program), reset the browser settings, then run a reputable anti-malware scan"},
            {"id": "B", "text": "Increase the browser's cache size"},
            {"id": "C", "text": "Change the default search engine and ignore the pop-ups"},
            {"id": "D", "text": "Disable HTTPS so pages load faster"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hijacked home page/search, rogue toolbars, and ad pop-ups are classic adware/PUP "
                       "symptoms. Remove the offending extensions and program, reset the browser, and run an "
                       "anti-malware scan so the changes don't keep coming back.",
            "distractors": {
                "B": "Cache size has nothing to do with a browser hijack; it won't remove the adware.",
                "C": "Just switching the search engine leaves the adware installed, so the hijack recurs.",
                "D": "Disabling HTTPS weakens security and does nothing to remove the unwanted software.",
            },
            "exam_pattern": "Browser hijack/redirect + pop-ups/toolbars = adware/PUP -> remove extensions/PUP, "
                            "reset the browser, scan with anti-malware.",
        },
    },
    {
        "id": "aplus2-swts-r2-008", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user's documents now carry a strange new extension and won't open, and a full-screen "
                "note demands cryptocurrency payment within 48 hours for a decryption key. What is the "
                "BEST course of action?",
        "options": [
            {"id": "A", "text": "Do not pay; isolate the machine from the network, remove the malware (or "
                                "reimage), restore the files from a known-good backup, and report the incident"},
            {"id": "B", "text": "Pay the ransom immediately so the files are released"},
            {"id": "C", "text": "Run Disk Defragmenter to rebuild the scrambled files"},
            {"id": "D", "text": "Rename the files back to their original extensions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "This is ransomware. Paying funds criminals with no guarantee of recovery. Isolate the "
                       "host to stop spread, remove the malware or reimage, restore data from a clean backup, "
                       "and report through the proper channels.",
            "distractors": {
                "B": "Paying is discouraged — it funds attackers and often does not restore the data.",
                "C": "Defragmentation reorganizes files on disk; it cannot reverse encryption.",
                "D": "The data is encrypted, not merely renamed — changing the extension back does nothing.",
            },
            "exam_pattern": "Ransomware (encrypted files + ransom note) -> don't pay; isolate, remove/reimage, "
                            "restore from backup, and report.",
        },
    },
    {
        "id": "aplus2-swts-r2-009", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Malware on a PC prevents the installed antivirus from launching or updating, and it closes "
                "the installer for a replacement tool as soon as it opens. Which approach BEST lets the "
                "technician scan and remove the malware?",
        "options": [
            {"id": "A", "text": "Boot into Safe Mode (or use a bootable antivirus / the Windows "
                                "preinstallation recovery environment) so the malware is inactive, then run "
                                "an updated scan"},
            {"id": "B", "text": "Keep retrying the same antivirus in normal mode until it finally opens"},
            {"id": "C", "text": "Delete the System32 folder to remove the infected files"},
            {"id": "D", "text": "Disable the firewall so the antivirus can update"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When malware blocks security tools, start the system in an environment where the malware "
                       "isn't running — Safe Mode, a bootable AV rescue disk, or a preinstallation/recovery "
                       "environment — then run an updated scan so the tool can actually remove it.",
            "distractors": {
                "B": "If the malware blocks the AV in normal mode, repeating the attempt will keep failing.",
                "C": "Deleting System32 destroys Windows itself — catastrophic, not a remediation.",
                "D": "Turning off the firewall lowers protection and does not stop the malware from blocking the AV.",
            },
            "exam_pattern": "Malware blocks your AV -> scan from Safe Mode or a bootable/preinstallation "
                            "environment (malware inactive), then remove.",
        },
    },
    {
        "id": "aplus2-swts-r2-010", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A technician has removed the malware from a PC, confirmed it is clean, updated the "
                "anti-malware definitions, and re-enabled System Restore with a fresh restore point. "
                "According to CompTIA's best-practice malware-removal procedure, what is the FINAL step?",
        "options": [
            {"id": "A", "text": "Educate the end user about safe browsing, email caution, and updates to "
                                "help prevent reinfection"},
            {"id": "B", "text": "Quarantine the infected system"},
            {"id": "C", "text": "Investigate and verify the malware symptoms"},
            {"id": "D", "text": "Disable System Restore"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The seven-step procedure ends with educating the end user, so the behavior that led to "
                       "the infection is less likely to repeat.",
            "distractors": {
                "B": "Quarantining the system is an EARLY step (step 2), done right after verifying symptoms.",
                "C": "Investigating/verifying symptoms is the FIRST step, already completed here.",
                "D": "Disabling System Restore is an early step (step 3); it has already been handled and re-enabled.",
            },
            "exam_pattern": "Malware 7 steps: Investigate -> Quarantine -> Disable System Restore -> Remediate "
                            "-> Schedule scans/update -> Re-enable System Restore -> EDUCATE the end user (last).",
        },
    },
    {
        "id": "aplus2-swts-r2-011", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "os_security_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "Every device on a small office network is being redirected to convincing fake look-alike "
                "sites. The technician checks several PCs and finds each one's hosts file is clean and the "
                "system clocks are correct. Where is the redirection MOST likely configured?",
        "options": [
            {"id": "A", "text": "Malware changed the router's/DHCP DNS server settings, so every client "
                                "resolves names through a rogue DNS server"},
            {"id": "B", "text": "The hosts file on each individual PC"},
            {"id": "C", "text": "The firmware of the users' monitors"},
            {"id": "D", "text": "The keyboard language settings on each PC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When the WHOLE network is redirected but the per-PC hosts files are clean, the common "
                       "point is the router: malware has pointed its DNS (handed out by DHCP) at a rogue server, "
                       "so all clients get poisoned answers. Reset the router's DNS and credentials and update "
                       "its firmware.",
            "distractors": {
                "B": "The hosts files were verified clean, and a hosts-file attack would have to be repeated on "
                     "every single PC — not the likely cause of a network-wide redirect.",
                "C": "Monitors display output; their firmware plays no part in name resolution.",
                "D": "Keyboard language settings have nothing to do with DNS or site redirection.",
            },
            "exam_pattern": "One PC redirected -> check its hosts file; the WHOLE network redirected (hosts files "
                            "clean) -> check the router/DHCP DNS for a rogue DNS server.",
        },
    },

    # ----- 3.4 / 3.5 Mobile OS & security --------------------------------
    {
        "id": "aplus2-swts-r2-012", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "After returning from international travel, a user's phone shows 'No Service' and cannot use "
                "cellular data, although Wi-Fi works normally. Which is the BEST first troubleshooting step?",
        "options": [
            {"id": "A", "text": "Toggle Airplane mode off/on (or restart) to re-register on the carrier, and "
                                "verify cellular data/roaming and the correct APN are enabled; reset network "
                                "settings if it persists"},
            {"id": "B", "text": "Perform a full factory reset of the phone"},
            {"id": "C", "text": "Replace the phone's screen"},
            {"id": "D", "text": "Clear the web browser's cache"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'No Service' after travel is usually a registration/roaming/APN issue. Toggling Airplane "
                       "mode or restarting forces the phone to re-register; confirm cellular data and roaming are "
                       "on and the APN is correct, and reset network settings if needed — all before anything drastic.",
            "distractors": {
                "B": "A factory reset wipes the device and is far too drastic as a first step for a radio-registration issue.",
                "C": "A screen swap is a hardware repair unrelated to cellular registration.",
                "D": "Clearing the browser cache does not restore cellular service.",
            },
            "exam_pattern": "No cellular service -> toggle Airplane mode/restart to re-register, check roaming/APN, "
                            "then reset network settings; factory reset only as a last resort.",
        },
    },
    {
        "id": "aplus2-swts-r2-013", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A user cannot install or update apps; the phone reports 'insufficient storage available,' "
                "and the camera also refuses to save new photos. What is the BEST fix?",
        "options": [
            {"id": "A", "text": "Free up storage — clear app caches, remove unused apps, and offload "
                                "photos/media (or add/clean an SD card where supported)"},
            {"id": "B", "text": "Upgrade to a faster cellular data plan"},
            {"id": "C", "text": "Replace the phone's battery"},
            {"id": "D", "text": "Turn Bluetooth off"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Insufficient storage' means internal storage is full. Clear caches, delete unused apps, "
                       "and move photos/media to the cloud or an SD card so apps can install/update and the camera "
                       "can save again.",
            "distractors": {
                "B": "Data-plan speed is unrelated to how much storage the device has free.",
                "C": "Battery condition affects runtime, not available storage space.",
                "D": "Turning off Bluetooth frees no storage.",
            },
            "exam_pattern": "'Insufficient storage' / can't update or save -> free space (clear caches, remove "
                            "unused apps, offload media, add/clean SD).",
        },
    },
    {
        "id": "aplus2-swts-r2-014", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 3, "type": "multi",
        "stem": "A user notices the camera/microphone indicator turning on by itself and finds an "
                "unfamiliar app that has been granted camera, microphone, location, and contacts access. "
                "Which TWO actions BEST remediate this likely spyware? (Choose two.)",
        "options": [
            {"id": "A", "text": "Revoke the app's unnecessary permissions and uninstall the suspicious app"},
            {"id": "B", "text": "Run a reputable mobile anti-malware scan and review what else the app "
                                "accessed or installed"},
            {"id": "C", "text": "Increase the screen-timeout duration"},
            {"id": "D", "text": "Turn off auto-rotate"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Unauthorized camera/microphone/location activity by an unknown app is a spyware symptom. "
                       "Revoke its permissions and uninstall it, then run a mobile anti-malware scan and review "
                       "what it reached, so nothing it dropped is left behind.",
            "distractors": {
                "C": "Screen-timeout length is a display/power setting with no effect on spyware.",
                "D": "Auto-rotate is a display setting and does nothing to stop unauthorized access.",
            },
            "exam_pattern": "Unauthorized camera/mic/location access by an app = mobile spyware -> revoke "
                            "permissions/uninstall + anti-malware scan and review access (avoid unofficial app sources).",
        },
    },
    {
        "id": "aplus2-swts-r2-015", "exam": "aplus2", "domain": "software_troubleshooting",
        "subtopic": "mobile_os_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A navigation app repeatedly places a user far from their real position and intermittently "
                "reports 'GPS signal lost,' while other phones nearby locate correctly. Which step is MOST "
                "likely to resolve it?",
        "options": [
            {"id": "A", "text": "Enable high-accuracy Location services and grant the app location "
                                "permission, then toggle Location (or restart) to reacquire a fix"},
            {"id": "B", "text": "Increase the ringtone volume"},
            {"id": "C", "text": "Permanently disable mobile data"},
            {"id": "D", "text": "Replace the SIM card"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Poor/incorrect location is usually a Location-services setting or permission problem. "
                       "Turn on high-accuracy location, make sure the app has location permission, and toggle "
                       "Location or restart so the device reacquires a satellite fix.",
            "distractors": {
                "B": "Ringtone volume has nothing to do with GPS positioning.",
                "C": "Disabling mobile data removes assisted-GPS data and does not fix the fix problem.",
                "D": "The SIM provides cellular identity/service, not GPS positioning.",
            },
            "exam_pattern": "GPS inaccurate / 'signal lost' -> enable high-accuracy Location + app permission, "
                            "toggle/restart to reacquire; a clear view of the sky helps.",
        },
    },

    # =====================================================================
    # 4.0 Operational Procedures
    # =====================================================================

    # ----- 4.1 Documentation ---------------------------------------------
    {
        "id": "aplus2-ops-r2-001", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 1, "type": "mcq",
        "stem": "Which document defines the rules employees must follow when using company computers, "
                "email, and the Internet — for example, prohibiting personal peer-to-peer downloads and "
                "non-work use of company systems?",
        "options": [
            {"id": "A", "text": "Acceptable use policy (AUP)"},
            {"id": "B", "text": "Standard operating procedure (SOP)"},
            {"id": "C", "text": "Network topology diagram"},
            {"id": "D", "text": "Incident report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An acceptable use policy (AUP) states what employees may and may not do with company "
                       "resources — devices, email, and Internet access.",
            "distractors": {
                "B": "An SOP is the step-by-step 'how we perform a task' document, not a usage-rules policy.",
                "C": "A topology diagram maps how devices connect on the network.",
                "D": "An incident report records the details of a specific event after it occurs.",
            },
            "exam_pattern": "Rules for how employees may use company resources = AUP; step-by-step task "
                            "instructions = SOP.",
        },
    },
    {
        "id": "aplus2-ops-r2-002", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 1, "type": "mcq",
        "stem": "Before planning a switch replacement, a technician wants documentation that shows how the "
                "network's devices and segments are interconnected. Which document provides this?",
        "options": [
            {"id": "A", "text": "A network topology diagram"},
            {"id": "B", "text": "A password policy"},
            {"id": "C", "text": "A knowledge base article"},
            {"id": "D", "text": "An asset tag"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A network topology diagram depicts how devices and network segments connect (physically "
                       "and/or logically), which is what you need when planning or troubleshooting connectivity.",
            "distractors": {
                "B": "A password policy defines credential rules, not network connections.",
                "C": "A knowledge base article documents a known issue and its fix, not the network layout.",
                "D": "An asset tag is an inventory label on a single device, not a map of the network.",
            },
            "exam_pattern": "How devices/segments interconnect = network topology diagram (physical and/or logical).",
        },
    },
    {
        "id": "aplus2-ops-r2-003", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 2, "type": "mcq",
        "stem": "When an employee leaves the company, IT follows a documented list of tasks: disable the "
                "user's accounts, revoke building and VPN access, and collect issued devices. What is this "
                "document BEST called?",
        "options": [
            {"id": "A", "text": "An end-user termination (offboarding) checklist — a standard operating procedure"},
            {"id": "B", "text": "A change request"},
            {"id": "C", "text": "An incident report"},
            {"id": "D", "text": "A EULA"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A documented set of consistent steps for processing a departing employee is an end-user "
                       "termination (offboarding) checklist — a type of SOP that ensures access is revoked and "
                       "assets are recovered every time.",
            "distractors": {
                "B": "A change request is a proposal to modify a system, not an offboarding procedure.",
                "C": "An incident report documents a specific security/operational event.",
                "D": "A EULA states the legal terms for using software.",
            },
            "exam_pattern": "Steps for staff leaving = end-user termination checklist; for staff joining = "
                            "new-user setup checklist (both are SOPs).",
        },
    },

    # ----- 4.2 Change management -----------------------------------------
    {
        "id": "aplus2-ops-r2-004", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "A change request must list exactly which servers, applications, and user groups the change "
                "will touch. Which element of the change request is this?",
        "options": [
            {"id": "A", "text": "The scope of the change"},
            {"id": "B", "text": "The rollback (back-out) plan"},
            {"id": "C", "text": "The purpose of the change"},
            {"id": "D", "text": "End-user acceptance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The scope defines the boundaries of the change — which systems, applications, and users "
                       "it affects — so everyone understands its reach.",
            "distractors": {
                "B": "The rollback/back-out plan describes how to revert if the change fails, not what it touches.",
                "C": "The purpose explains WHY the change is being made.",
                "D": "End-user acceptance is the affected users agreeing they have reviewed and are ready for the change.",
            },
            "exam_pattern": "Which systems/users are affected = scope; how to undo = rollback plan; why = purpose.",
        },
    },
    {
        "id": "aplus2-ops-r2-005", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "Before approval, the change team evaluates how likely the change is to cause problems and "
                "how severe the impact would be, then labels it low, medium, or high. Which change-request "
                "element is this?",
        "options": [
            {"id": "A", "text": "Risk analysis (assigning a risk level)"},
            {"id": "B", "text": "Sandbox testing"},
            {"id": "C", "text": "The rollback (back-out) plan"},
            {"id": "D", "text": "The responsible staff member"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Weighing likelihood and impact and assigning a low/medium/high rating is the risk "
                       "analysis / risk level — it helps the change board decide and prioritize.",
            "distractors": {
                "B": "Sandbox testing validates the change in an isolated environment; it is not the risk rating itself.",
                "C": "The rollback plan is the documented reversal procedure if the change fails.",
                "D": "The responsible staff member is the person accountable for performing the change.",
            },
            "exam_pattern": "Assess likelihood + impact and rate it low/med/high = risk analysis / risk level.",
        },
    },
    {
        "id": "aplus2-ops-r2-006", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "A formal change request names the specific person who is accountable for carrying out the "
                "change and overseeing its outcome. Which element does this represent?",
        "options": [
            {"id": "A", "text": "The responsible staff member"},
            {"id": "B", "text": "The change advisory board (CAB)"},
            {"id": "C", "text": "The affected end users"},
            {"id": "D", "text": "The backout plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Documented business processes identify a responsible staff member — the individual "
                       "accountable for performing the change and seeing it through.",
            "distractors": {
                "B": "The CAB is the GROUP that reviews and approves/rejects the change, not the individual performing it.",
                "C": "Affected end users are those impacted by the change, not the person accountable for executing it.",
                "D": "The backout plan is the procedure for reverting a failed change.",
            },
            "exam_pattern": "The named individual accountable for performing/overseeing a change = responsible "
                            "staff member (part of documented business processes).",
        },
    },

    # ----- 4.3 Backup and recovery ---------------------------------------
    {
        "id": "aplus2-ops-r2-007", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 1, "type": "mcq",
        "stem": "Which backup type copies ALL selected data every time it runs and allows the simplest, "
                "fastest restore because only that one backup set is needed?",
        "options": [
            {"id": "A", "text": "Full backup"},
            {"id": "B", "text": "Incremental backup"},
            {"id": "C", "text": "Differential backup"},
            {"id": "D", "text": "Synthetic full backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A full backup copies all selected data on every run, so a restore needs only that single "
                       "set — the simplest, fastest recovery, at the cost of the longest backup time and most storage.",
            "distractors": {
                "B": "An incremental copies only changes since the last backup of any type; a restore needs the full "
                     "PLUS every increment in order.",
                "C": "A differential copies changes since the last FULL; a restore needs the full plus the latest differential.",
                "D": "A synthetic full is assembled from existing backups on the backup server, not a fresh copy of all source data.",
            },
            "exam_pattern": "Full = copies everything each run; simplest/fastest restore (one set), slowest backup, most storage.",
        },
    },
    {
        "id": "aplus2-ops-r2-008", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A business takes a FULL backup every Sunday and a DIFFERENTIAL backup each weekday evening. "
                "To fully restore the data on Thursday morning, which backups are required?",
        "options": [
            {"id": "A", "text": "Sunday's full backup plus Wednesday evening's (the most recent) differential — two sets"},
            {"id": "B", "text": "Only Wednesday evening's differential"},
            {"id": "C", "text": "Sunday's full plus every weekday differential, applied in order"},
            {"id": "D", "text": "Only Sunday's full backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A differential holds everything changed since the last FULL, so a restore needs just the "
                       "full plus the single most recent differential — Sunday's full and Wednesday evening's differential.",
            "distractors": {
                "B": "A differential cannot restore on its own; it must be applied on top of the full backup.",
                "C": "Applying every differential in order is how INCREMENTAL chains restore — differentials need only the latest one.",
                "D": "The full alone misses all changes made Monday through Wednesday.",
            },
            "exam_pattern": "Differential restore = last full + the single latest differential. Incremental restore "
                            "= last full + EVERY incremental since.",
        },
    },
    {
        "id": "aplus2-ops-r2-009", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "To avoid the long nightly transfer of a full backup across the network, a backup server "
                "merges the last full backup with all later incrementals into a brand-new full backup on the "
                "backup storage itself — without re-reading all the data from the client. What is the "
                "resulting backup called?",
        "options": [
            {"id": "A", "text": "A synthetic full backup"},
            {"id": "B", "text": "A differential backup"},
            {"id": "C", "text": "An incremental backup"},
            {"id": "D", "text": "The 3-2-1 rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A synthetic full is produced on the backup server by combining an existing full with the "
                       "subsequent incrementals, giving a new full-equivalent restore point without a fresh full "
                       "read from the source.",
            "distractors": {
                "B": "A differential captures changes since the last full, read from the client — it is not assembled from other backups.",
                "C": "An incremental captures only changes since the last backup, read from the client.",
                "D": "3-2-1 is a copies/media/off-site guideline, not a type of backup produced by merging.",
            },
            "exam_pattern": "Synthetic full = a full assembled on the backup server from an existing full + "
                            "increments (no full re-read from the source).",
        },
    },

    # ----- 4.4 / 4.5 Safety & environment --------------------------------
    {
        "id": "aplus2-ops-r2-010", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 3, "type": "mcq",
        "stem": "When servicing the inside of a power supply unit (PSU) or a CRT monitor, technicians are "
                "specifically told NOT to wear a grounded anti-static wrist strap. Why?",
        "options": [
            {"id": "A", "text": "These components store a dangerous high-voltage charge in their capacitors; "
                                "a grounded strap could channel that charge through the technician and cause "
                                "severe shock"},
            {"id": "B", "text": "The wrist strap would generate static electricity that damages the PSU"},
            {"id": "C", "text": "The wrist strap simply slows the technician down"},
            {"id": "D", "text": "PSUs and CRTs are immune to ESD, so a strap is merely unnecessary"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PSUs and CRTs hold a lethal stored charge in their capacitors even when unplugged. A "
                       "grounded wrist strap gives that high voltage a path through you, so the strap is a shock "
                       "hazard here — these units should only be opened by trained personnel.",
            "distractors": {
                "B": "A wrist strap prevents static buildup; it does not generate it. The real danger here is stored high voltage.",
                "C": "Speed is not the issue — the concern is a potentially fatal electrical shock.",
                "D": "The reason is the stored high-voltage shock hazard to the technician, not that the devices are 'immune' to ESD.",
            },
            "exam_pattern": "Never wear a grounded ESD strap inside a PSU or CRT — stored high-voltage/capacitor "
                            "charge is a potentially lethal shock hazard.",
        },
    },
    {
        "id": "aplus2-ops-r2-011", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 2, "type": "mcq",
        "stem": "A server room experiences frequent brief voltage sags (brownouts) and occasional blackouts "
                "that reboot the servers. Which device BOTH keeps the servers running through a sag or outage "
                "AND conditions the power?",
        "options": [
            {"id": "A", "text": "An uninterruptible power supply (UPS) with battery backup and AVR"},
            {"id": "B", "text": "A surge suppressor (surge protector)"},
            {"id": "C", "text": "A standard power strip"},
            {"id": "D", "text": "A KVM switch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A UPS supplies battery power through sags and outages and, with automatic voltage "
                       "regulation (AVR), conditions the incoming power — keeping servers up long enough to ride "
                       "through or shut down cleanly.",
            "distractors": {
                "B": "A surge suppressor only clamps voltage spikes; it has no battery, so it cannot carry a load through a brownout or blackout.",
                "C": "A power strip merely adds outlets and provides no power protection at all.",
                "D": "A KVM switch shares one keyboard/monitor/mouse among computers; it does nothing for power.",
            },
            "exam_pattern": "Ride through brownouts/blackouts + conditioning = UPS (battery + AVR); a surge "
                            "suppressor only stops spikes.",
        },
    },
    {
        "id": "aplus2-ops-r2-012", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 1, "type": "mcq",
        "stem": "A technician must clean thick dust out of dozens of PCs in a dusty warehouse. Which practice "
                "BEST protects the technician from inhaling the airborne particles?",
        "options": [
            {"id": "A", "text": "Wear an air-filtration mask and blow out the dust with compressed air (or an "
                                "ESD-safe vacuum) in a well-ventilated area"},
            {"id": "B", "text": "Wear an anti-static wrist strap"},
            {"id": "C", "text": "Put on cut-resistant gloves"},
            {"id": "D", "text": "Keep a Class C fire extinguisher nearby"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dust is an inhalation hazard, so wear an air-filtration mask (respirator) and clear the "
                       "dust with compressed air or an ESD-safe vacuum in a ventilated space.",
            "distractors": {
                "B": "An anti-static strap prevents ESD damage to components; it does nothing to protect the lungs.",
                "C": "Cut-resistant gloves guard against cuts, not inhaled particles.",
                "D": "A Class C extinguisher is for energized electrical fires — unrelated to dust inhalation.",
            },
            "exam_pattern": "Airborne particulates/dust -> air-filtration mask (PPE) + compressed air/ESD vacuum "
                            "in a ventilated area.",
        },
    },

    # ----- 4.6 Incident response + 4.7/4.8 licensing & regulated data ----
    {
        "id": "aplus2-ops-r2-013", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A hard drive may hold evidence for a legal case. To preserve it, what should the technician "
                "create and then work from, leaving the original drive untouched?",
        "options": [
            {"id": "A", "text": "A bit-for-bit forensic image (copy) of the drive, verified with a hash to prove integrity"},
            {"id": "B", "text": "A quick-formatted clone that skips 'empty' space to save time"},
            {"id": "C", "text": "A ZIP archive of the user's visible documents"},
            {"id": "D", "text": "A Windows System Restore point"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Preserving evidence means capturing a bit-for-bit forensic image (including deleted and "
                       "slack space), hashing it to prove it was not altered, and analyzing the COPY while the "
                       "original is secured under chain of custody.",
            "distractors": {
                "B": "A quick format and skipping unallocated space discards recoverable evidence — it is not a forensic copy.",
                "C": "Zipping only the visible documents misses deleted/hidden data and does not preserve integrity.",
                "D": "A System Restore point reverts Windows settings; it is not an evidence copy of the drive.",
            },
            "exam_pattern": "Preserve evidence -> bit-for-bit forensic image, hash it, analyze the COPY; keep the "
                            "original and chain of custody intact.",
        },
    },
    {
        "id": "aplus2-ops-r2-014", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 1, "type": "mcq",
        "stem": "A spreadsheet contains employees' full names, Social Security numbers, and home addresses. "
                "Which category of regulated data is this?",
        "options": [
            {"id": "A", "text": "PII (personally identifiable information)"},
            {"id": "B", "text": "PHI (protected health information)"},
            {"id": "C", "text": "PCI (payment card data)"},
            {"id": "D", "text": "Public records"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Names, Social Security numbers, and addresses identify a specific person, making this "
                       "personally identifiable information (PII), which must be handled and protected accordingly.",
            "distractors": {
                "B": "PHI is medical/health information specifically (e.g., diagnoses, treatment records).",
                "C": "PCI is cardholder/payment card account data governed by PCI DSS.",
                "D": "Public records are already published and are not sensitive, regulated data.",
            },
            "exam_pattern": "Identity data (name/SSN/address) = PII; medical = PHI; card data = PCI; EU personal data = GDPR.",
        },
    },
    {
        "id": "aplus2-ops-r2-015", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A company serving customers in the European Union must honor requests to erase personal "
                "data and must notify authorities of a data breach within strict timeframes. Which "
                "regulation imposes these requirements?",
        "options": [
            {"id": "A", "text": "The GDPR (General Data Protection Regulation)"},
            {"id": "B", "text": "PCI DSS"},
            {"id": "C", "text": "A EULA"},
            {"id": "D", "text": "An SLA"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The GDPR governs personal data of EU residents, granting rights such as erasure and "
                       "requiring timely breach notification — making it the regulation described.",
            "distractors": {
                "B": "PCI DSS is a payment-card security standard, not an EU personal-data privacy law.",
                "C": "A EULA states the legal terms for using a piece of software.",
                "D": "An SLA is a service-level agreement defining performance metrics between parties.",
            },
            "exam_pattern": "EU personal-data rights (erasure, breach notification) = GDPR; card data = PCI DSS.",
        },
    },

    # ----- 4.7 Communication & professionalism ---------------------------
    {
        "id": "aplus2-ops-r2-016", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 2, "type": "mcq",
        "stem": "Midway through a repair, a technician realizes it will take two days longer than the "
                "estimate already given to the customer. What is the MOST professional action?",
        "options": [
            {"id": "A", "text": "Proactively contact the customer, explain the delay, give a realistic new "
                                "timeline, and offer options"},
            {"id": "B", "text": "Say nothing and hope it is finished before the customer notices"},
            {"id": "C", "text": "Blame the parts supplier and the customer's old equipment"},
            {"id": "D", "text": "Quietly return the device unrepaired to avoid an awkward conversation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Setting and MEETING expectations means communicating status proactively: tell the "
                       "customer about the delay, provide a realistic revised timeline, and offer options so they "
                       "can decide how to proceed.",
            "distractors": {
                "B": "Going silent fails to manage expectations and erodes trust when the deadline passes.",
                "C": "Shifting blame is unprofessional and does nothing to help the customer.",
                "D": "Returning the device unrepaired abandons the job and the customer entirely.",
            },
            "exam_pattern": "Set and MEET expectations: communicate status proactively, give a realistic timeline, "
                            "offer options, and follow up.",
        },
    },
    {
        "id": "aplus2-ops-r2-017", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 2, "type": "multi",
        "stem": "When dealing with a difficult or argumentative customer, which TWO behaviors are MOST "
                "professional? (Choose two.)",
        "options": [
            {"id": "A", "text": "Do not argue with the customer or become defensive"},
            {"id": "B", "text": "Ask open-ended, clarifying questions and restate the issue to confirm your understanding"},
            {"id": "C", "text": "Raise your voice to match the customer's tone so they take you seriously"},
            {"id": "D", "text": "Dismiss the problem as minor so the customer calms down"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "With a difficult customer, avoid arguing or getting defensive, and use clarifying, "
                       "open-ended questions plus a restatement of the issue to show you understand and to de-escalate.",
            "distractors": {
                "C": "Matching the customer's raised voice escalates the conflict rather than resolving it.",
                "D": "Minimizing or dismissing the problem is dismissive and unprofessional, and usually makes things worse.",
            },
            "exam_pattern": "Difficult customers: don't argue/get defensive, don't minimize or dismiss, avoid being "
                            "judgmental; clarify and restate to confirm understanding.",
        },
    },

    # ----- 4.8 Scripting basics ------------------------------------------
    {
        "id": "aplus2-ops-r2-018", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 1, "type": "mcq",
        "stem": "A technician needs a simple script of sequential Command Prompt commands that runs natively "
                "on Windows with no extra interpreter installed. Which file type is the BEST fit?",
        "options": [
            {"id": "A", "text": ".bat (batch file; also .cmd)"},
            {"id": "B", "text": ".sh"},
            {"id": "C", "text": ".py"},
            {"id": "D", "text": ".vbs"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A .bat (or .cmd) batch file runs a sequence of Command Prompt commands natively on "
                       "Windows with nothing extra to install.",
            "distractors": {
                "B": ".sh is a Linux/Unix Bash shell script and does not run natively in Windows Command Prompt.",
                "C": ".py requires the Python interpreter to be installed.",
                "D": ".vbs is a VBScript file — a different Windows scripting language, not a Command Prompt batch file.",
            },
            "exam_pattern": ".bat/.cmd = native Windows batch | .ps1 PowerShell | .sh Bash | .py Python | "
                            ".vbs VBScript | .js JavaScript.",
        },
    },
    {
        "id": "aplus2-ops-r2-019", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants ONE scripting language to run the same automation on Windows, Linux, "
                "AND macOS, with a large library ecosystem for tasks like parsing files and calling web APIs. "
                "Which is the BEST choice?",
        "options": [
            {"id": "A", "text": "Python (.py)"},
            {"id": "B", "text": "Windows batch (.bat)"},
            {"id": "C", "text": "VBScript (.vbs)"},
            {"id": "D", "text": "Bash shell (.sh)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Python runs on Windows, Linux, and macOS and has a vast standard and third-party library "
                       "ecosystem, making it the best single cross-platform choice for general automation.",
            "distractors": {
                "B": "Batch files run only in the Windows Command Prompt.",
                "C": "VBScript is a legacy Windows-only scripting language.",
                "D": "Bash is the Unix/Linux (and macOS) shell and does not run natively on Windows without an added layer.",
            },
            "exam_pattern": "Cross-platform, general-purpose scripting with rich libraries = Python (.py); "
                            ".bat/.vbs are Windows-only and .sh is Unix/Linux/macOS.",
        },
    },
    {
        "id": "aplus2-ops-r2-020", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "multi",
        "stem": "Which TWO tasks are appropriate to automate with a script? (Choose two.)",
        "options": [
            {"id": "A", "text": "Silently install the same application on dozens of workstations"},
            {"id": "B", "text": "Collect a hardware and software inventory from each machine into a report"},
            {"id": "C", "text": "Physically reseat a loose RAM module"},
            {"id": "D", "text": "Replace a cracked laptop screen"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Scripts shine at repeatable software tasks — pushing an application install to many PCs "
                       "and gathering inventory/data from each machine are classic use cases.",
            "distractors": {
                "C": "Reseating RAM is a hands-on hardware task a script cannot perform.",
                "D": "Replacing a screen is a physical repair, not something a script can do.",
            },
            "exam_pattern": "Script use cases: app installation, remap drives, restart machines, automated backups, "
                            "gather info, initiate updates — never physical hardware repairs.",
        },
    },
]
