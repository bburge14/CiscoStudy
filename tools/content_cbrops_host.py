"""Cisco CyberOps Associate (CBROPS 200-201) pool - Domain 3: Host-Based Analysis.

Original, objective-aligned practice items for the five Host-Based Analysis
subtopics tracked in CertLab:
  * cbr_endpoint_technologies - host-based IDS/IPS, antimalware, host firewall,
                                application allow/block listing and sandboxing.
  * cbr_os_components          - Windows vs Linux processes, file systems, the
                                registry, services and where configuration lives.
  * cbr_logs_artifacts         - Windows Event Logs, Sysmon and syslog, and
                                interpreting host logs to identify an event.
  * cbr_malware_analysis       - reading sandbox / detonation-chamber output:
                                hashes, URLs, and host/network behavior.
  * cbr_evidence_attribution   - evidence roles (best, corroborative, indirect)
                                and attribution artifacts (IOCs, assets).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item cites the public Cisco 200-201 exam topic it draws on. Blue-team /
analyst depth only, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cbr_endpoint_technologies ========================================
    {
        "id": "cbrops-host-001", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "Software installed on a single server watches that host's log files, file integrity, "
                "and process activity and raises an alert when it sees suspicious behavior, but it does "
                "not block the activity. Which endpoint technology is this?",
        "options": [
            {"id": "A", "text": "Host-based intrusion detection system (HIDS)"},
            {"id": "B", "text": "Network firewall"},
            {"id": "C", "text": "Certificate authority"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A HIDS monitors a single host (logs, file integrity, processes) and alerts on "
                       "suspicious activity; being detection-only, it reports rather than blocks (a HIPS would block).",
            "distractors": {
                "B": "A network firewall filters traffic at the network boundary, not host log/file/process activity.",
                "C": "A certificate authority issues certificates and does no host monitoring.",
                "D": "A load balancer distributes traffic across servers; it is not a host monitoring tool.",
            },
            "exam_pattern": "Monitors one host's logs/files/processes and alerts (no block) = HIDS.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-002", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A control that permits only explicitly approved applications to "
                "execute on an endpoint and blocks everything else by default is called application "
                "______ (the default-deny approach).",
        "correct": ["allowlisting", "allow listing", "allow-listing", "whitelisting", "allowlist", "application allowlisting"],
        "explanation": {
            "correct": "Application allowlisting (whitelisting) is a default-deny control: only approved "
                       "programs run, which stops unknown or unauthorized executables, including much malware.",
            "exam_pattern": "Default-deny, only approved apps run = application allowlisting (vs blocklisting's default-allow).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-003", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "To analyze a suspicious attachment safely, an analyst runs it inside an isolated, "
                "instrumented environment that is kept separate from production systems so its behavior "
                "can be observed without risk. This technique is called:",
        "options": [
            {"id": "A", "text": "Sandboxing"},
            {"id": "B", "text": "Hashing"},
            {"id": "C", "text": "Tunneling"},
            {"id": "D", "text": "Load balancing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sandboxing executes untrusted code in a contained, isolated environment so its "
                       "actions can be watched without exposing real hosts or data.",
            "distractors": {
                "B": "Hashing produces a fingerprint of a file; it does not run the file to observe behavior.",
                "C": "Tunneling encapsulates traffic in another protocol; it is an evasion technique, not analysis isolation.",
                "D": "Load balancing distributes traffic across servers and is unrelated to malware isolation.",
            },
            "exam_pattern": "Run untrusted code in an isolated environment to observe it = sandboxing.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-004", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 1, "type": "mcq",
        "stem": "Which endpoint technology controls inbound and outbound network connections for one "
                "specific computer, allowing or denying traffic based on rules local to that machine?",
        "options": [
            {"id": "A", "text": "Host-based firewall"},
            {"id": "B", "text": "Antivirus signature database"},
            {"id": "C", "text": "SIEM correlation engine"},
            {"id": "D", "text": "Certificate revocation list"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A host-based (personal) firewall enforces allow/deny rules on the connections of the "
                       "single machine it runs on, independent of the network perimeter.",
            "distractors": {
                "B": "An antivirus database identifies malicious files, it does not filter network connections.",
                "C": "A SIEM correlates logs centrally; it does not enforce per-host connection rules.",
                "D": "A CRL lists revoked certificates and has nothing to do with filtering host traffic.",
            },
            "exam_pattern": "Per-machine inbound/outbound connection rules = host-based firewall.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },

    # ===== cbr_os_components =================================================
    {
        "id": "cbrops-host-005", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "mcq",
        "stem": "On a Windows host, an analyst investigating persistence examines a hierarchical "
                "database that stores operating-system and application configuration, including the "
                "auto-start 'Run' keys. Which component is this?",
        "options": [
            {"id": "A", "text": "The Windows Registry"},
            {"id": "B", "text": "The /etc directory"},
            {"id": "C", "text": "The page file"},
            {"id": "D", "text": "The master boot record"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Windows Registry is the central hierarchical configuration store; malware often "
                       "adds auto-start 'Run' key entries there for persistence, so it is a key artifact.",
            "distractors": {
                "B": "/etc holds configuration files on Linux, not Windows.",
                "C": "The page file backs virtual memory on disk; it is not the configuration database.",
                "D": "The master boot record holds boot code and the partition table, not OS configuration settings.",
            },
            "exam_pattern": "Windows central config store with auto-start keys = the Registry.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-006", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "mcq",
        "stem": "An analyst moving from Windows to a Linux host asks where most service and system "
                "configuration is stored, since Linux has no central registry. Which answer is correct?",
        "options": [
            {"id": "A", "text": "In plain-text configuration files, largely under the /etc directory"},
            {"id": "B", "text": "In the Windows Registry hive files"},
            {"id": "C", "text": "Only in volatile RAM, never on disk"},
            {"id": "D", "text": "Inside the NTFS master file table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Linux stores most system and service configuration as human-readable text files, "
                       "predominantly under /etc, rather than in a single binary registry.",
            "distractors": {
                "B": "The registry is a Windows construct; Linux does not use it.",
                "C": "Configuration persists on disk so it survives reboots; it is not kept only in RAM.",
                "D": "The NTFS master file table is a Windows file-system structure, not where Linux configuration lives.",
            },
            "exam_pattern": "Linux config = text files under /etc (no central registry).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-007", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 1, "type": "mcq",
        "stem": "On a Linux host, which command would an analyst use to list the processes currently "
                "running so they can spot an unexpected one?",
        "options": [
            {"id": "A", "text": "ps"},
            {"id": "B", "text": "regedit"},
            {"id": "C", "text": "ipconfig"},
            {"id": "D", "text": "chkdsk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ps (and tools like top) lists running processes on Linux, letting an analyst review "
                       "what is executing and flag anything unexpected.",
            "distractors": {
                "B": "regedit is the Windows Registry editor, not available on Linux and not a process lister.",
                "C": "ipconfig displays network configuration on Windows; it does not list processes.",
                "D": "chkdsk checks a Windows disk for errors; it is unrelated to listing processes.",
            },
            "exam_pattern": "List Linux processes = ps/top (regedit/ipconfig/chkdsk are Windows tools).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-008", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "mcq",
        "stem": "Which file system is the native, default file system used by modern Windows "
                "installations and supports features such as access control lists and journaling?",
        "options": [
            {"id": "A", "text": "NTFS"},
            {"id": "B", "text": "ext4"},
            {"id": "C", "text": "HFS+"},
            {"id": "D", "text": "SMB"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NTFS is the native Windows file system and supports per-file permissions (ACLs), "
                       "journaling, and other features analysts rely on when examining Windows disks.",
            "distractors": {
                "B": "ext4 is a common Linux file system, not the Windows default.",
                "C": "HFS+ is a legacy Apple macOS file system.",
                "D": "SMB is a network file-sharing protocol, not an on-disk file system.",
            },
            "exam_pattern": "Native modern Windows file system = NTFS; Linux commonly ext4.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },

    # ===== cbr_logs_artifacts ===============================================
    {
        "id": "cbrops-host-009", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "In the Windows Security event log, which event ID records a failed logon attempt - the "
                "entry an analyst counts when looking for password-guessing activity?",
        "options": [
            {"id": "A", "text": "4625"},
            {"id": "B", "text": "4624"},
            {"id": "C", "text": "1102"},
            {"id": "D", "text": "7045"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 4625 is 'An account failed to log on'; a burst of 4625 events for one "
                       "account signals password guessing or brute forcing.",
            "distractors": {
                "B": "4624 is a successful logon, the opposite of a failed attempt.",
                "C": "1102 records that the audit/security log was cleared.",
                "D": "7045 marks a new service being installed, not a logon failure.",
            },
            "exam_pattern": "Windows logon: 4624 = success, 4625 = failure.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-010", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "On a Linux server, where would an analyst typically look for authentication and system "
                "log messages generated through the syslog mechanism?",
        "options": [
            {"id": "A", "text": "In files under /var/log (such as auth.log or secure)"},
            {"id": "B", "text": "In the Windows Event Viewer"},
            {"id": "C", "text": "In the HKEY_LOCAL_MACHINE registry hive"},
            {"id": "D", "text": "In the BIOS/UEFI firmware settings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Linux systems write syslog-based messages to text files under /var/log; "
                       "authentication events appear in auth.log (Debian/Ubuntu) or secure (RHEL/CentOS).",
            "distractors": {
                "B": "Event Viewer is the Windows log interface, not used for Linux syslog files.",
                "C": "The registry is a Windows configuration store, not a Linux log location.",
                "D": "BIOS/UEFI settings are firmware configuration, not OS log messages.",
            },
            "exam_pattern": "Linux logs live in /var/log; auth events in auth.log or secure.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-011", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "A Windows endpoint has Sysmon deployed in addition to the default auditing. What extra "
                "visibility does Sysmon provide to an analyst?",
        "options": [
            {"id": "A", "text": "Detailed logs such as process creation with command lines, hashes, and network connections"},
            {"id": "B", "text": "It encrypts all host traffic end to end"},
            {"id": "C", "text": "It replaces the need for any antivirus product"},
            {"id": "D", "text": "It blocks all inbound connections by default"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sysmon records rich endpoint telemetry - process creation with full command line and "
                       "hashes, network connections, image loads, and more - beyond what default Windows logging captures.",
            "distractors": {
                "B": "Sysmon logs activity; it does not encrypt traffic.",
                "C": "Sysmon is a logging/telemetry tool, not a replacement for antivirus prevention.",
                "D": "Sysmon does not filter or block connections; it records them.",
            },
            "exam_pattern": "Sysmon = deep endpoint telemetry (process creation, hashes, net connections) for detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-012", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 3, "type": "mcq",
        "stem": "A Windows Security log shows roughly 200 Event ID 4625 entries for one account within "
                "two minutes, all from the same remote IP, immediately followed by a single Event ID "
                "4624 for that account from the same IP. What does this pattern most likely indicate?",
        "options": [
            {"id": "A", "text": "A successful password brute-force / guessing attack"},
            {"id": "B", "text": "A normal user mistyping their password once"},
            {"id": "C", "text": "The security log being cleared by an administrator"},
            {"id": "D", "text": "A routine scheduled backup completing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Many failed logons (4625) in quick succession followed by a success (4624) from the "
                       "same source is the classic signature of a brute-force attack that finally guessed the password.",
            "distractors": {
                "B": "A single mistype produces one or two failures, not ~200 in two minutes followed by a success.",
                "C": "Clearing the log is event 1102 and would not generate a flood of 4625 failures.",
                "D": "A backup job does not generate repeated failed-logon events for an account.",
            },
            "exam_pattern": "Flood of 4625 then a 4624 from one source = brute force that succeeded.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },

    # ===== cbr_malware_analysis =============================================
    {
        "id": "cbrops-host-013", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A malware sandbox report lists the sample's SHA-256 hash. What is the primary way an "
                "analyst uses this hash value?",
        "options": [
            {"id": "A", "text": "As a unique fingerprint to look the file up against threat-intelligence/IOC feeds"},
            {"id": "B", "text": "To decrypt the malware's encrypted payload"},
            {"id": "C", "text": "To determine the malware's physical location on disk"},
            {"id": "D", "text": "To recover the password the malware used"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cryptographic hash is a unique fingerprint of the file; analysts search it against "
                       "intelligence sources (e.g., VirusTotal, internal IOC lists) to see whether the sample is already known-bad.",
            "distractors": {
                "B": "A hash is one-way; it cannot decrypt anything.",
                "C": "A hash identifies the content, not where the file sits on disk.",
                "D": "A hash does not reveal passwords; it is a fingerprint of the data.",
            },
            "exam_pattern": "File hash = unique IOC to match the sample against known-bad intelligence.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },
    {
        "id": "cbrops-host-014", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A detonation chamber executes a suspicious file and reports the files it created, the "
                "registry keys it modified, and the external hosts it contacted. Which type of malware "
                "analysis produced this report?",
        "options": [
            {"id": "A", "text": "Dynamic (behavioral) analysis"},
            {"id": "B", "text": "Static analysis only"},
            {"id": "C", "text": "Source-code review"},
            {"id": "D", "text": "Penetration testing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dynamic (behavioral) analysis runs the sample in an instrumented sandbox and records "
                       "what it actually does - file, registry, and network activity - at runtime.",
            "distractors": {
                "B": "Static analysis examines the file without executing it, so it would not report runtime behavior like live network callouts.",
                "C": "Source-code review inspects source, which is rarely available for malware and is not what a detonation chamber does.",
                "D": "Penetration testing is authorized offensive assessment, not malware detonation analysis.",
            },
            "exam_pattern": "Runs the sample and records behavior (files/registry/network) = dynamic analysis.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },
    {
        "id": "cbrops-host-015", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 3, "type": "mcq",
        "stem": "In a sandbox report's networking section, after the sample executes it repeatedly "
                "connects outbound to an unfamiliar domain and waits for instructions. What does this "
                "behavior most directly indicate?",
        "options": [
            {"id": "A", "text": "Command-and-control (C2) communication"},
            {"id": "B", "text": "A routine Windows Update check"},
            {"id": "C", "text": "Normal DNS name resolution for the host's time sync"},
            {"id": "D", "text": "The sandbox itself being compromised"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Repeated outbound connections to an unknown host where the sample awaits instructions "
                       "is classic command-and-control (C2) beaconing; the domain/IP becomes a network IOC.",
            "distractors": {
                "B": "Windows Update contacts known Microsoft endpoints, not an unfamiliar attacker-controlled domain.",
                "C": "Time sync (NTP) and benign DNS do not involve waiting for instructions from an unknown host.",
                "D": "The report describes the sample's behavior, not a compromise of the analysis sandbox.",
            },
            "exam_pattern": "Beaconing to an unknown host awaiting commands = C2; capture the domain/IP as an IOC.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },

    # ===== cbr_evidence_attribution =========================================
    {
        "id": "cbrops-host-016", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "mcq",
        "stem": "During an investigation, an analyst preserves the original hard drive and a verified "
                "bit-for-bit forensic image of it. In evidence terms, this most reliable, original-source "
                "material is classified as:",
        "options": [
            {"id": "A", "text": "Best evidence"},
            {"id": "B", "text": "Corroborative evidence"},
            {"id": "C", "text": "Indirect (circumstantial) evidence"},
            {"id": "D", "text": "Hearsay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Best evidence is the original or most authoritative source (such as the original drive "
                       "or a verified image), carrying the greatest reliability in an investigation.",
            "distractors": {
                "B": "Corroborative evidence supports or confirms other evidence; it is not the primary original source.",
                "C": "Indirect (circumstantial) evidence implies a fact without directly proving it.",
                "D": "Hearsay is secondhand information, generally the weakest and least reliable.",
            },
            "exam_pattern": "Original / most reliable source = best evidence.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.4 Identify type of evidence used based on provided logs"],
    },
    {
        "id": "cbrops-host-017", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "mcq",
        "stem": "A firewall log on its own does not prove who ran an attack, but it supports and "
                "strengthens the conclusion already drawn from host and authentication logs. What role "
                "does this firewall log play?",
        "options": [
            {"id": "A", "text": "Corroborative evidence"},
            {"id": "B", "text": "Best evidence"},
            {"id": "C", "text": "The sole conclusive proof"},
            {"id": "D", "text": "An indicator of attack (IOA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Corroborative evidence supports or reinforces other evidence; it adds weight to a "
                       "conclusion but does not stand alone as the primary proof.",
            "distractors": {
                "B": "Best evidence is the original, most authoritative source - the firewall log here is supporting, not primary.",
                "C": "It explicitly does not by itself prove who ran the attack, so it is not sole conclusive proof.",
                "D": "An IOA describes attacker behavior/intent; the question is about the evidentiary role of a supporting log.",
            },
            "exam_pattern": "Supports/strengthens other evidence = corroborative.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.4 Identify type of evidence used based on provided logs"],
    },
    {
        "id": "cbrops-host-018", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Forensic artifacts such as known-malicious file hashes, suspicious "
                "domains, or known-bad IP addresses that signal a system may have been breached are "
                "collectively called indicators of ______ (give the word or the three-letter abbreviation).",
        "correct": ["compromise", "ioc", "iocs", "indicators of compromise"],
        "explanation": {
            "correct": "Indicators of compromise (IOCs) are forensic artifacts - hashes, domains, IPs, file "
                       "names, registry keys - that suggest a host has been breached and are used for detection and hunting.",
            "exam_pattern": "Artifacts that a breach occurred (hashes/domains/IPs) = indicators of compromise (IOC).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.3 Describe the role of attribution in an investigation"],
    },
]
