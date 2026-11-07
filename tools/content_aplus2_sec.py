"""CompTIA A+ Core 2 (220-1102) — Domain 2.0 Security EXPANSION item pool.

Original, objective-aligned questions that deepen the existing ``security_a2``
bank in content_aplus2.py (items ``aplus2-sec-001``..``aplus2-sec-006``) toward
real-exam depth. Same authoring rules as the other pools: original content
mapped to the public 220-1102 objectives, never real exam items.
build_content.py shuffles option order, so the answer key here is not
positionally biased.

Coverage (24 items, ~4 per subtopic):
  security_concepts_a2   - physical/logical controls, Active Directory
  malware_a2             - malware types, symptoms, 7-step removal order
  social_engineering_a2  - phishing family, vishing, evil twin, dumpster diving
  windows_security       - BitLocker/To Go, EFS, UAC, Defender Firewall
  workstation_hardening  - BIOS/UEFI password, password policy, account mgmt
  data_destruction       - degaussing, physical destruction, wipe-for-reuse
"""

QUESTIONS = [
    # ===== 2.0 Security — security_concepts_a2 ==============================
    {
        "id": "aplus2-sec-101", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "A data center installs a small two-door room at its entrance: the outer door must "
                "close and the person be verified before the inner door will open, specifically to "
                "prevent an unauthorized person from slipping in behind an employee. What is this "
                "physical control called?",
        "options": [
            {"id": "A", "text": "Access control vestibule (mantrap)"},
            {"id": "B", "text": "Bollard"},
            {"id": "C", "text": "Badge reader"},
            {"id": "D", "text": "Cable lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An access control vestibule (formerly 'mantrap') is a two-door area that lets only "
                       "one verified person through at a time, directly preventing tailgating/piggybacking.",
            "distractors": {
                "B": "A bollard is a short, sturdy post that blocks vehicles from an area; it doesn't "
                     "control pedestrian entry one person at a time.",
                "C": "A badge reader authenticates a credential at a door, but by itself does nothing to "
                     "stop a second person from following through the open door.",
                "D": "A cable lock physically tethers a laptop to a desk to deter theft; it isn't an "
                     "entry-control mechanism.",
            },
            "exam_pattern": "Two interlocking doors passing one verified person = access control vestibule "
                            "(mantrap), the countermeasure to tailgating.",
        },
    },
    {
        "id": "aplus2-sec-102", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 3, "type": "mcq",
        "stem": "In an Active Directory domain, an administrator wants each user's Documents folder to "
                "physically reside on a network file server so it is backed up centrally and follows the "
                "user to any domain PC they sign in to. Which feature accomplishes this transparently?",
        "options": [
            {"id": "A", "text": "Folder redirection"},
            {"id": "B", "text": "Login script"},
            {"id": "C", "text": "Home folder"},
            {"id": "D", "text": "Security group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Folder redirection (configured via Group Policy) transparently points known folders "
                       "such as Documents and Desktop to a network location, so the data is centrally stored/"
                       "backed up and available wherever the user logs in.",
            "distractors": {
                "B": "A login script runs commands (e.g., maps drives, sets printers) at sign-in; it doesn't "
                     "relocate the Documents known folder to the server.",
                "C": "A home folder is a designated per-user network storage location (often mapped to a drive "
                     "letter), but it doesn't transparently redirect the Documents known folder itself.",
                "D": "A security group is a collection of accounts used to assign permissions; it has nothing "
                     "to do with relocating a user's folders.",
            },
            "exam_pattern": "Documents/Desktop transparently stored on the server = folder redirection; mapped "
                            "personal drive = home folder; run-at-logon commands = login script.",
        },
    },
    {
        "id": "aplus2-sec-103", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "Company policy states that every user account and service should be granted only the "
                "minimum rights required to do its job, and no more. Which security principle does this "
                "describe?",
        "options": [
            {"id": "A", "text": "Principle of least privilege"},
            {"id": "B", "text": "Implicit deny"},
            {"id": "C", "text": "Access control list (ACL)"},
            {"id": "D", "text": "Mandatory access control (MAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The principle of least privilege grants each user, process, or service only the "
                       "minimum access needed to perform its function, limiting the damage from mistakes or "
                       "compromise.",
            "distractors": {
                "B": "Implicit deny means anything not explicitly permitted is blocked (a common default on "
                     "ACLs/firewalls); it's a default-deny rule, not the idea of minimizing each account's rights.",
                "C": "An ACL is a list defining which subjects may access a resource — a mechanism that can "
                     "enforce least privilege, but not the principle itself.",
                "D": "MAC is an access-control model using labels/clearances assigned by the system; it's a "
                     "model, not the minimize-rights principle.",
            },
            "exam_pattern": "Give only the minimum rights needed = least privilege; 'deny unless explicitly "
                            "allowed' = implicit deny.",
        },
    },
    {
        "id": "aplus2-sec-104", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "security_concepts_a2", "difficulty": 2, "type": "mcq",
        "stem": "For multifactor authentication, a company issues each employee a small physical keyfob "
                "that displays a rotating six-digit one-time code. What category of authentication device "
                "is the keyfob?",
        "options": [
            {"id": "A", "text": "Hard token"},
            {"id": "B", "text": "Soft token"},
            {"id": "C", "text": "Biometric factor"},
            {"id": "D", "text": "Smart card"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hard token is a dedicated hardware device that generates one-time passcodes (e.g., "
                       "an RSA-style keyfob); it's a 'something you have' factor independent of the user's "
                       "phone or PC.",
            "distractors": {
                "B": "A soft token is software-based — an authenticator app running on a phone or computer; "
                     "the standalone hardware keyfob described is a hard token.",
                "C": "A biometric factor is 'something you are' (fingerprint, face, iris); a code-generating "
                     "keyfob measures nothing about the person.",
                "D": "A smart card is a physical card with an embedded chip that must be inserted into or "
                     "tapped on a reader; it doesn't display a rotating numeric code the way an OTP keyfob does.",
            },
            "exam_pattern": "Dedicated hardware OTP device = hard token; authenticator app = soft token; both "
                            "are 'something you have.'",
        },
    },

    # ===== 2.0 Security — malware_a2 ========================================
    {
        "id": "aplus2-sec-105", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 1, "type": "mcq",
        "stem": "A user installs what looks like a free PDF utility, but hidden inside, the program "
                "quietly opens a backdoor that lets an attacker control the PC remotely. The malware does "
                "not self-replicate. Which type of malware is this?",
        "options": [
            {"id": "A", "text": "Trojan"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Boot sector virus"},
            {"id": "D", "text": "Ransomware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A trojan (Trojan horse) disguises itself as legitimate, desirable software to trick the "
                       "user into installing it, then performs malicious actions such as opening a backdoor. It "
                       "does not self-replicate.",
            "distractors": {
                "B": "A worm self-replicates and spreads across networks on its own, with no need to masquerade "
                     "as a wanted program or for the user to run it.",
                "C": "A boot sector virus infects the disk's boot sector/MBR so it loads before the OS; it isn't "
                     "a disguised downloadable utility.",
                "D": "Ransomware encrypts files and demands payment; the described malware grants stealthy remote "
                     "access rather than ransoming data.",
            },
            "exam_pattern": "Disguised as legit software + user-installed + no self-replication = trojan; "
                            "self-spreading over a network = worm.",
        },
    },
    {
        "id": "aplus2-sec-106", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 3, "type": "mcq",
        "stem": "A technician is following CompTIA's best-practice procedure for malware removal. They have "
                "already (1) investigated and verified the malware symptoms and (2) quarantined the infected "
                "system. According to the recommended order, what should they do NEXT?",
        "options": [
            {"id": "A", "text": "Disable System Restore (in Windows)"},
            {"id": "B", "text": "Remediate the system — update anti-malware and scan/remove"},
            {"id": "C", "text": "Schedule scans and run updates"},
            {"id": "D", "text": "Educate the end user"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CompTIA's order is: 1) investigate/verify symptoms, 2) quarantine, 3) DISABLE System "
                       "Restore (Windows), 4) remediate (update anti-malware, then scan and remove), 5) schedule "
                       "scans and run updates, 6) re-enable System Restore and create a restore point, 7) educate "
                       "the end user. After quarantining, step 3 is to disable System Restore so infected restore "
                       "points can't reinfect the system.",
            "distractors": {
                "B": "Remediation (update anti-malware and scan/remove) is step 4 — it comes AFTER disabling "
                     "System Restore, not before.",
                "C": "Scheduling scans and running updates is step 5, performed after remediation.",
                "D": "Educating the end user is the FINAL step (7), done once the system is clean.",
            },
            "exam_pattern": "Order: verify -> quarantine -> disable System Restore -> remediate -> schedule "
                            "scans/updates -> re-enable System Restore -> educate the user.",
        },
    },
    {
        "id": "aplus2-sec-107", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "Malware on a workstation operates at a privileged (kernel) level, actively hides its own "
                "files, processes, and registry keys from the OS and antivirus, and standard scans in normal "
                "Windows fail to detect it. Which type of malware is this?",
        "options": [
            {"id": "A", "text": "Rootkit"},
            {"id": "B", "text": "Spyware"},
            {"id": "C", "text": "Adware"},
            {"id": "D", "text": "Keylogger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A rootkit embeds itself at a privileged level and conceals its presence from the OS and "
                       "security tools, making detection and removal difficult; remediation often needs offline "
                       "scanning, a pre-boot environment, or OS reinstallation.",
            "distractors": {
                "B": "Spyware covertly collects information about the user and their activity; it isn't defined "
                     "by kernel-level stealth and privileged concealment.",
                "C": "Adware displays unwanted advertisements; it's a nuisance, not stealthy privileged code.",
                "D": "A keylogger records keystrokes to capture credentials; it may run hidden, but its defining "
                     "trait is logging input, not kernel-level self-concealment.",
            },
            "exam_pattern": "Hides at privileged/kernel level and evades AV = rootkit; may require an offline/"
                            "pre-boot scan or a reimage to remove.",
        },
    },
    {
        "id": "aplus2-sec-108", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "malware_a2", "difficulty": 2, "type": "mcq",
        "stem": "Several PCs have suddenly become sluggish, their fans run at full speed, and CPU/GPU "
                "utilization sits near 100% even when idle; monitoring shows outbound connections to a "
                "mining pool. Which type of malware is MOST likely present?",
        "options": [
            {"id": "A", "text": "Cryptominer (cryptojacking)"},
            {"id": "B", "text": "Keylogger"},
            {"id": "C", "text": "Ransomware"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cryptominer (cryptojacking malware) hijacks a system's CPU/GPU to mine cryptocurrency "
                       "for the attacker, which shows up as very high processor/GPU usage, heat, fan noise, and "
                       "sluggishness, plus traffic to mining pools.",
            "distractors": {
                "B": "A keylogger quietly records keystrokes; it uses negligible resources and wouldn't peg the "
                     "CPU/GPU at full load.",
                "C": "Ransomware encrypts files and demands payment; it causes a brief spike during encryption, "
                     "not sustained full-load mining with pool connections.",
                "D": "A rootkit hides malware; a cryptominer may use rootkit techniques, but the symptoms here "
                     "(maxed CPU/GPU plus mining-pool traffic) specifically point to a cryptominer.",
            },
            "exam_pattern": "Sustained near-100% CPU/GPU, heat/fans, and mining-pool traffic = cryptominer/"
                            "cryptojacking.",
        },
    },

    # ===== 2.0 Security — social_engineering_a2 =============================
    {
        "id": "aplus2-sec-109", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 2, "type": "mcq",
        "stem": "An attacker crafts a highly targeted email aimed specifically at the company's CFO, "
                "impersonating the CEO and urgently requesting a large wire transfer. The message is "
                "tailored to that one high-level executive. Which attack BEST describes this?",
        "options": [
            {"id": "A", "text": "Whaling"},
            {"id": "B", "text": "Spear phishing"},
            {"id": "C", "text": "Vishing"},
            {"id": "D", "text": "Shoulder surfing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Whaling is a phishing attack that targets a 'big fish' — a high-profile executive such "
                       "as a CEO or CFO — with a message tailored to them, often to authorize fraudulent transfers.",
            "distractors": {
                "B": "Spear phishing targets a specific individual or group; whaling is the specialized subset "
                     "aimed at a senior executive, which best fits targeting the CFO.",
                "C": "Vishing is voice/telephone-based social engineering; this attack arrives by email.",
                "D": "Shoulder surfing is covertly watching someone enter credentials or data; no observation is "
                     "involved here.",
            },
            "exam_pattern": "Phishing aimed at a high-level executive = whaling; tailored to a specific ordinary "
                            "individual = spear phishing; generic mass email = phishing.",
        },
    },
    {
        "id": "aplus2-sec-110", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 1, "type": "mcq",
        "stem": "A user receives a phone call from someone claiming to be the bank's fraud department, "
                "pressuring them to read back their account number and PIN 'to stop a fraudulent charge.' "
                "Which social-engineering attack is this?",
        "options": [
            {"id": "A", "text": "Vishing"},
            {"id": "B", "text": "Smishing"},
            {"id": "C", "text": "Whaling"},
            {"id": "D", "text": "Shoulder surfing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Vishing (voice phishing) uses a phone call to manipulate the victim into revealing "
                       "sensitive information such as account numbers or PINs.",
            "distractors": {
                "B": "Smishing is phishing via SMS/text messages; this attack came over a voice call, not a text.",
                "C": "Whaling targets high-profile executives specifically; the victim here is an ordinary "
                     "account holder.",
                "D": "Shoulder surfing is directly observing someone enter information; the attacker here never "
                     "watches the victim.",
            },
            "exam_pattern": "Phone call tricking you out of info = vishing; text message = smishing; email = phishing.",
        },
    },
    {
        "id": "aplus2-sec-111", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 2, "type": "mcq",
        "stem": "In a coffee shop, an attacker sets up a rogue wireless access point broadcasting the same "
                "SSID as the shop's legitimate Wi-Fi, hoping customers connect to it so their traffic can "
                "be intercepted. What is this attack called?",
        "options": [
            {"id": "A", "text": "Evil twin"},
            {"id": "B", "text": "Tailgating"},
            {"id": "C", "text": "Dumpster diving"},
            {"id": "D", "text": "Shoulder surfing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An evil twin is a rogue wireless access point that mimics a legitimate network's SSID "
                       "to lure victims into connecting, allowing the attacker to intercept or manipulate their "
                       "traffic.",
            "distractors": {
                "B": "Tailgating is physically following an authorized person through a secured door; it isn't "
                     "a wireless attack.",
                "C": "Dumpster diving is searching discarded trash for useful information; no network is involved.",
                "D": "Shoulder surfing is secretly watching someone enter credentials or data; it doesn't "
                     "involve a fake access point.",
            },
            "exam_pattern": "Rogue AP cloning a real SSID to lure clients = evil twin.",
        },
    },
    {
        "id": "aplus2-sec-112", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "social_engineering_a2", "difficulty": 1, "type": "mcq",
        "stem": "An attacker recovers discarded printouts, old account statements, and sticky notes with "
                "passwords from a company's unsecured trash bins to gather information for an attack. Which "
                "social-engineering technique is this?",
        "options": [
            {"id": "A", "text": "Dumpster diving"},
            {"id": "B", "text": "Tailgating"},
            {"id": "C", "text": "Impersonation"},
            {"id": "D", "text": "Phishing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dumpster diving is sifting through an organization's discarded trash to find sensitive "
                       "information (documents, credentials, configurations) that can aid an attack; shredding/"
                       "secure disposal is the countermeasure.",
            "distractors": {
                "B": "Tailgating is following an authorized person through a secured entry; it's about physical "
                     "entry, not scavenging trash.",
                "C": "Impersonation is pretending to be someone (e.g., IT support) to manipulate a victim; no "
                     "direct interaction occurs in dumpster diving.",
                "D": "Phishing uses fraudulent electronic messages to trick victims; dumpster diving is a "
                     "physical information-gathering technique.",
            },
            "exam_pattern": "Harvesting info from the trash = dumpster diving; prevent it with shredding/secure "
                            "disposal.",
        },
    },

    # ===== 2.0 Security — windows_security ==================================
    {
        "id": "aplus2-sec-113", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 2, "type": "mcq",
        "stem": "A company requires that any data copied to USB flash drives be encrypted so a lost drive's "
                "contents cannot be read. Which built-in Windows feature is designed specifically for this?",
        "options": [
            {"id": "A", "text": "BitLocker To Go"},
            {"id": "B", "text": "BitLocker (operating system drive)"},
            {"id": "C", "text": "EFS (Encrypting File System)"},
            {"id": "D", "text": "Microsoft Defender Antivirus"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BitLocker To Go is the Windows feature that encrypts removable drives (USB flash drives, "
                       "external disks), requiring a password or key to unlock them on any PC.",
            "distractors": {
                "B": "Standard BitLocker encrypts fixed internal volumes/the OS drive, not removable USB media — "
                     "that's the To Go variant.",
                "C": "EFS encrypts individual files/folders per user on an NTFS volume; it isn't the feature "
                     "built to encrypt whole removable drives.",
                "D": "Defender Antivirus scans for and removes malware; it provides no drive encryption at all.",
            },
            "exam_pattern": "Encrypt removable/USB drives = BitLocker To Go; fixed/OS volume = BitLocker; per-file "
                            "on NTFS = EFS.",
        },
    },
    {
        "id": "aplus2-sec-114", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 1, "type": "mcq",
        "stem": "When a user tries to install a program, Windows dims the screen and displays a prompt "
                "asking for consent or an administrator password before the system-level change is allowed. "
                "Which security feature is this?",
        "options": [
            {"id": "A", "text": "User Account Control (UAC)"},
            {"id": "B", "text": "BitLocker"},
            {"id": "C", "text": "Microsoft Defender SmartScreen"},
            {"id": "D", "text": "Windows Defender Firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "User Account Control (UAC) prompts for consent or administrator credentials before an "
                       "action that requires elevated privileges, preventing silent system changes by malware or "
                       "standard users.",
            "distractors": {
                "B": "BitLocker encrypts drives; it doesn't produce an elevation consent prompt.",
                "C": "SmartScreen warns about unrecognized downloaded apps and malicious sites; it doesn't gate "
                     "local privilege elevation for every system change.",
                "D": "Windows Defender Firewall filters network traffic; it has nothing to do with the elevation "
                     "prompt.",
            },
            "exam_pattern": "Dimmed screen + consent/admin-password prompt before a system change = UAC.",
        },
    },
    {
        "id": "aplus2-sec-115", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 2, "type": "mcq",
        "stem": "Using only built-in Windows tools, a technician needs to create a rule that blocks inbound "
                "connections on a specific TCP port. Which tool should they configure?",
        "options": [
            {"id": "A", "text": "Windows Defender Firewall (with Advanced Security)"},
            {"id": "B", "text": "Microsoft Defender Antivirus"},
            {"id": "C", "text": "BitLocker"},
            {"id": "D", "text": "Microsoft Defender SmartScreen"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Windows Defender Firewall (with Advanced Security) creates inbound and outbound rules "
                       "that allow or block traffic by port, protocol, program, or address.",
            "distractors": {
                "B": "Defender Antivirus detects and removes malware; it does not create port-based network rules.",
                "C": "BitLocker encrypts drives and has no role in filtering network traffic.",
                "D": "SmartScreen checks the reputation of downloaded apps and websites; it doesn't block traffic "
                     "on specific ports.",
            },
            "exam_pattern": "Allow/block traffic by port/program = Defender Firewall; detect/remove malware = "
                            "Defender Antivirus.",
        },
    },
    {
        "id": "aplus2-sec-116", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "windows_security", "difficulty": 2, "type": "multi",
        "stem": "Which TWO built-in Windows features protect data at rest by encrypting it? (Choose two.)",
        "options": [
            {"id": "A", "text": "BitLocker"},
            {"id": "B", "text": "EFS (Encrypting File System)"},
            {"id": "C", "text": "User Account Control (UAC)"},
            {"id": "D", "text": "Microsoft Defender SmartScreen"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "BitLocker encrypts entire volumes and EFS encrypts individual files/folders on NTFS — "
                       "both provide encryption of data at rest.",
            "distractors": {
                "C": "UAC controls privilege elevation with consent prompts; it does not encrypt any data.",
                "D": "SmartScreen checks the reputation of downloaded apps/websites to warn about threats; it "
                     "provides no encryption.",
            },
            "exam_pattern": "Windows data-at-rest encryption = BitLocker (whole volume) + EFS (per file/folder); "
                            "UAC and SmartScreen don't encrypt.",
        },
    },

    # ===== 2.0 Security — workstation_hardening =============================
    {
        "id": "aplus2-sec-117", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "mcq",
        "stem": "To stop users from changing the boot order or booting from external media to bypass Windows "
                "security on lab PCs, which hardening measure should a technician apply?",
        "options": [
            {"id": "A", "text": "Set a BIOS/UEFI supervisor password"},
            {"id": "B", "text": "Enable BitLocker To Go on all USB drives"},
            {"id": "C", "text": "Disable the Windows Defender Firewall"},
            {"id": "D", "text": "Add all users to the local Administrators group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A BIOS/UEFI supervisor (setup) password prevents unauthorized users from changing "
                       "firmware settings such as boot order or enabling external boot, which would otherwise let "
                       "them bypass the OS and its protections.",
            "distractors": {
                "B": "BitLocker To Go encrypts removable drives; it doesn't stop someone from changing the "
                     "firmware boot order.",
                "C": "Disabling the firewall removes a protective control — it weakens security rather than "
                     "hardening it.",
                "D": "Adding users to Administrators violates least privilege and makes the system less secure, "
                     "not more.",
            },
            "exam_pattern": "Lock down boot order / external boot = BIOS/UEFI (supervisor) password.",
        },
    },
    {
        "id": "aplus2-sec-118", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "multi",
        "stem": "A technician is configuring a password policy to harden user accounts. Which TWO settings "
                "reflect password best practices? (Choose two.)",
        "options": [
            {"id": "A", "text": "Require a minimum length and complexity (mix of character types)"},
            {"id": "B", "text": "Set passwords to expire and require periodic change"},
            {"id": "C", "text": "Store all user passwords in a shared spreadsheet for recovery"},
            {"id": "D", "text": "Disable account lockout so users are never locked out"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Enforcing a minimum length with complexity and requiring periodic expiration/change are "
                       "standard password-hardening practices that resist guessing and limit how long a "
                       "compromised password stays useful.",
            "distractors": {
                "C": "Storing passwords in a shared spreadsheet exposes every credential at once — a severe "
                     "security failure, not a best practice.",
                "D": "Disabling account lockout lets attackers brute-force passwords with unlimited attempts; "
                     "lockout thresholds should be ENABLED.",
            },
            "exam_pattern": "Harden passwords: length + complexity, expiration, history, and account lockout; "
                            "never store them in plaintext or remove lockout.",
        },
    },
    {
        "id": "aplus2-sec-119", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 2, "type": "mcq",
        "stem": "As part of account-management hardening on a new workstation, which action follows best "
                "practice?",
        "options": [
            {"id": "A", "text": "Rename the default Administrator account and disable the Guest account"},
            {"id": "B", "text": "Leave the Guest account enabled for convenience"},
            {"id": "C", "text": "Give every user membership in the Administrators group"},
            {"id": "D", "text": "Keep the manufacturer's default credentials on the device"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Renaming the built-in Administrator account (so attackers can't target a known name) and "
                       "disabling the Guest account reduce the attack surface — core account-management hardening "
                       "steps.",
            "distractors": {
                "B": "Leaving Guest enabled provides an anonymous, low-control foothold; it should be disabled.",
                "C": "Making every user an administrator violates least privilege and lets any user or their "
                     "malware alter the system.",
                "D": "Keeping default credentials is a well-known risk; default usernames/passwords should always "
                     "be changed.",
            },
            "exam_pattern": "Account hardening: rename/secure the default admin, disable Guest, change default "
                            "credentials, apply least privilege.",
        },
    },
    {
        "id": "aplus2-sec-120", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "workstation_hardening", "difficulty": 1, "type": "mcq",
        "stem": "Which ongoing practice BEST protects workstations against exploitation of newly discovered "
                "operating-system and application vulnerabilities?",
        "options": [
            {"id": "A", "text": "Patch/update management — keep the OS and applications current"},
            {"id": "B", "text": "Disabling automatic updates to avoid reboots"},
            {"id": "C", "text": "Running as a local administrator at all times"},
            {"id": "D", "text": "Turning off the host firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Patch (update) management — regularly applying OS and application updates/security "
                       "patches — closes known vulnerabilities before attackers can exploit them, and is a "
                       "fundamental hardening practice.",
            "distractors": {
                "B": "Disabling automatic updates leaves known vulnerabilities unpatched, directly increasing risk.",
                "C": "Running as administrator all the time violates least privilege and lets malware make "
                     "system-wide changes.",
                "D": "Turning off the host firewall removes a protective control and exposes the machine to "
                     "network attacks.",
            },
            "exam_pattern": "Close known vulnerabilities = patch/update management; pair it with least privilege "
                            "and a host firewall.",
        },
    },

    # ===== 2.0 Security — data_destruction ==================================
    {
        "id": "aplus2-sec-121", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to permanently destroy the data on failed magnetic hard disk drives by "
                "exposing them to a powerful magnetic field. Which sanitization method is this?",
        "options": [
            {"id": "A", "text": "Degaussing"},
            {"id": "B", "text": "Low-level formatting"},
            {"id": "C", "text": "Standard (quick) format"},
            {"id": "D", "text": "Secure erase (ATA command)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Degaussing uses a strong magnetic field to scramble the magnetic domains on a hard disk "
                       "drive, destroying the data (and usually the drive). It works only on magnetic media.",
            "distractors": {
                "B": "A low-level format rewrites the drive's low-level structures but uses no magnetic field; "
                     "it's a software/firmware operation and the term is often misused for a full overwrite.",
                "C": "A standard/quick format only clears the file table and leaves the underlying data "
                     "recoverable — it isn't secure destruction.",
                "D": "Secure erase issues a firmware command to wipe a drive's cells (useful for SSDs/HDDs being "
                     "kept for reuse); it's not a magnetic-field method.",
            },
            "exam_pattern": "Strong magnetic field wiping a magnetic HDD = degaussing (no effect on SSDs/flash, "
                            "which have no magnetic domains).",
        },
    },
    {
        "id": "aplus2-sec-122", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "multi",
        "stem": "A drive will NOT be reused and its data must be physically destroyed. Which TWO are physical "
                "destruction methods? (Choose two.)",
        "options": [
            {"id": "A", "text": "Shredding the drive"},
            {"id": "B", "text": "Drilling or hammering through the platters"},
            {"id": "C", "text": "Performing a quick format"},
            {"id": "D", "text": "Deleting the files and emptying the Recycle Bin"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Shredding and drilling/crushing the platters physically destroy the media so the data "
                       "cannot be recovered — appropriate when the drive won't be reused.",
            "distractors": {
                "C": "A quick format only clears the file table; the underlying data remains recoverable, so it "
                     "is neither physical destruction nor secure.",
                "D": "Deleting files and emptying the Recycle Bin removes only pointers to the data, which is "
                     "trivially recoverable.",
            },
            "exam_pattern": "Physical destruction = shred, drill/hammer, incinerate, degauss (magnetic); format/"
                            "delete are NOT secure.",
        },
    },
    {
        "id": "aplus2-sec-123", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 2, "type": "mcq",
        "stem": "After paying a third-party vendor to destroy its decommissioned drives, a company needs "
                "documented proof — for auditors and compliance — that each drive was actually destroyed. "
                "What should the vendor provide?",
        "options": [
            {"id": "A", "text": "A certificate of destruction"},
            {"id": "B", "text": "A standard format log"},
            {"id": "C", "text": "A software license key"},
            {"id": "D", "text": "A drive warranty card"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A certificate of destruction is the formal document a disposal/recycling vendor provides "
                       "attesting that specific media were destroyed, giving an auditable record for compliance "
                       "and chain of custody.",
            "distractors": {
                "B": "A format log wouldn't prove physical destruction, and a quick format isn't secure "
                     "destruction anyway.",
                "C": "A software license key is unrelated to proving that media was destroyed.",
                "D": "A warranty card covers hardware defects, not proof of data destruction.",
            },
            "exam_pattern": "Proof that an outsourced vendor destroyed media = certificate of destruction "
                            "(supports chain of custody/compliance).",
        },
    },
    {
        "id": "aplus2-sec-124", "exam": "aplus2", "domain": "security_a2",
        "subtopic": "data_destruction", "difficulty": 3, "type": "mcq",
        "stem": "A company plans to REUSE a batch of working hard drives internally but must first ensure the "
                "previous department's data cannot be recovered. Which method is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Perform a drive wipe/secure erase that overwrites all sectors"},
            {"id": "B", "text": "Shred the drives"},
            {"id": "C", "text": "Delete the partitions in Disk Management"},
            {"id": "D", "text": "Perform a quick format"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Because the drives will be reused, they should be sanitized (not destroyed): a drive "
                       "wipe/secure erase overwrites every sector so prior data is unrecoverable while keeping the "
                       "drive usable.",
            "distractors": {
                "B": "Shredding destroys the drives — appropriate for disposal, not when the hardware must be "
                     "reused.",
                "C": "Deleting partitions removes volume structures but leaves the underlying data recoverable.",
                "D": "A quick format only clears the file table; the data remains and can be recovered.",
            },
            "exam_pattern": "Reuse the drive -> sanitize (wipe/secure erase/overwrite); dispose of the drive -> "
                            "physically destroy (shred/drill/degauss/incinerate).",
        },
    },
]
