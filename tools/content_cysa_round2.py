"""CompTIA CySA+ (CS0-003) — Round 2 deepening item pool.

Original, analyst-level practice items authored for CertLab's CySA+ track and
mapped to the public CS0-003 objectives. These are NEW scenarios/concepts that
go DEEPER than round-1 (content_cysa_secops/vulnmgmt/ir/reporting.py); none
duplicate a round-1 concept+scenario.

Framing is strictly DEFENSIVE / blue-team analyst: detection, triage, log /
alert / packet analysis, vulnerability management, incident response, reporting.
No weaponized payloads or working exploit code.

Distribution (~60 items): Security Operations 33%, Vulnerability Management 30%,
Incident Response 20%, Reporting & Communication 17%; every subtopic covered.

IDs reuse the round-1 prefixes with an "r2" segment (cysa-so-r2-###, etc.) and
are unique versus the existing bank. Schema matches round-1 exactly. build_content
auto-discovers content_cysa_*.py and shuffles each item's A/B/C/D order (seeded by
id) before re-keying, so the keys authored here are not positionally biased.

Version-sensitive/numeric facts were web-verified against authoritative sources
(FIRST CVSS v3.1 & TLP 2.0, CISA KEV, NIST SP 800-61/800-126, MITRE ATT&CK,
Microsoft Windows/Sysmon event documentation, SEC Release 33-11216, HHS HIPAA).
"""

QUESTIONS = [
    # =====================================================================
    # DOMAIN 1.0 — SECURITY OPERATIONS (20 items)
    # =====================================================================

    # ----- so_system_network_analysis ------------------------------------
    {
        "id": "cysa-so-r2-001", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Investigating possible password guessing against a domain account, an analyst wants to "
                "count each unsuccessful sign-in. Which Windows Security event ID records a failed logon?",
        "options": [
            {"id": "A", "text": "4624 (an account was successfully logged on)"},
            {"id": "B", "text": "4625 (an account failed to log on)"},
            {"id": "C", "text": "4634 (an account was logged off)"},
            {"id": "D", "text": "4648 (a logon was attempted using explicit credentials)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Event ID 4625 records a failed logon attempt; a burst of 4625 events against one account "
                       "is the classic signature of brute-force or password-spraying activity.",
            "distractors": {
                "A": "4624 is a SUCCESSFUL logon, the opposite of the failed attempts being counted.",
                "C": "4634 records a logoff (session end), not a failed authentication.",
                "D": "4648 records a logon using explicit credentials (e.g., runas), not an authentication failure.",
            },
            "exam_pattern": "Repeated failed logons / brute force = Event ID 4625 (4624 = success).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.1 — Analyze log data (Windows Event IDs)",
                       "Microsoft: Windows security audit events (4625 failed logon)"],
    },
    {
        "id": "cysa-so-r2-002", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 3, "type": "mcq",
        "stem": "In a successful logon event (4624), an analyst sees Logon Type 10. Which access method does "
                "this value indicate?",
        "options": [
            {"id": "A", "text": "An interactive logon at the machine's local console"},
            {"id": "B", "text": "A network logon such as an SMB file-share access"},
            {"id": "C", "text": "A remote interactive logon over RDP / Terminal Services"},
            {"id": "D", "text": "A service starting under a service account"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Logon Type 10 is RemoteInteractive — a user logged on remotely using Remote Desktop / "
                       "Terminal Services, a key artifact when tracing RDP-based access.",
            "distractors": {
                "A": "Local console interactive logon is Logon Type 2, not 10.",
                "B": "A network logon (SMB, etc.) is Logon Type 3.",
                "D": "A service logon under a service account is Logon Type 5.",
            },
            "exam_pattern": "Logon Type 10 = RemoteInteractive (RDP); Type 3 = network; Type 2 = console; Type 5 = service.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.1 — Analyze log data (logon types)",
                       "Microsoft: Audit logon events (logon type 10 RemoteInteractive)"],
    },
    {
        "id": "cysa-so-r2-003", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 3, "type": "mcq",
        "stem": "An analyst wants Sysmon to show which process on a host initiated a given outbound TCP "
                "connection. Which Sysmon event ID provides this process-to-connection mapping?",
        "options": [
            {"id": "A", "text": "Event ID 1 (process creation)"},
            {"id": "B", "text": "Event ID 11 (file creation)"},
            {"id": "C", "text": "Event ID 13 (registry value set)"},
            {"id": "D", "text": "Event ID 3 (network connection)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Sysmon Event ID 3 logs TCP/UDP network connections and ties each one to the initiating "
                       "process (ProcessId/ProcessGuid), letting the analyst attribute a connection to a binary.",
            "distractors": {
                "A": "Event ID 1 records a new process's creation details, not its later network connections.",
                "B": "Event ID 11 records file creation, not network activity.",
                "C": "Event ID 13 records a registry value being set, not a network connection.",
            },
            "exam_pattern": "Sysmon EID 3 = network connection linked to its source process; EID 1 = process creation.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.1 — Endpoint telemetry (Sysmon)",
                       "Microsoft Sysinternals: Sysmon events (ID 3 Network connection)"],
    },
    {
        "id": "cysa-so-r2-004", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "fill",
        "stem": "Hunting for lateral movement that abuses Windows file sharing (SMB), an analyst filters flow "
                "records for the standard modern SMB port. Enter the TCP port number.",
        "options": [],
        "correct": ["445"],
        "explanation": {
            "correct": "SMB runs over TCP 445 on modern Windows; it is a frequent lateral-movement and "
                       "ransomware-propagation channel (the legacy NetBIOS session service used TCP 139).",
            "distractors": {},
            "exam_pattern": "SMB = TCP 445 (legacy 139); watch it for lateral movement and worm-like spread.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.1 — Common ports and protocols",
                       "Microsoft: SMB over TCP 445"],
    },

    # ----- so_threat_intel ------------------------------------------------
    {
        "id": "cysa-so-r2-005", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A threat-intel analyst receives a report labeled TLP:RED. Under the Traffic Light Protocol, "
                "how may the analyst share it?",
        "options": [
            {"id": "A", "text": "Only with the specific individuals it was given to; no further disclosure"},
            {"id": "B", "text": "With anyone in their organization and that organization's clients"},
            {"id": "C", "text": "Across the broader security community"},
            {"id": "D", "text": "Publicly, with no restrictions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TLP:RED is limited to the named recipients (or those present in a meeting) and must not be "
                       "shared further; it is the most restrictive Traffic Light Protocol label.",
            "distractors": {
                "B": "Sharing within the organization and with its clients is TLP:AMBER, not RED.",
                "C": "Sharing with the wider community is TLP:GREEN.",
                "D": "Unrestricted sharing is TLP:CLEAR (renamed from TLP:WHITE in TLP 2.0).",
            },
            "exam_pattern": "TLP:RED = named recipients only; AMBER = org/clients; GREEN = community; CLEAR = unrestricted.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Intelligence sharing (TLP)",
                       "FIRST: Traffic Light Protocol (TLP) version 2.0"],
    },
    {
        "id": "cysa-so-r2-006", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A report warns that a specific ransomware crew is actively targeting the company's sector "
                "this month and details the campaign's infrastructure and timing so the SOC can prepare now. "
                "Which category of threat intelligence is this?",
        "options": [
            {"id": "A", "text": "Strategic intelligence"},
            {"id": "B", "text": "Operational intelligence"},
            {"id": "C", "text": "Vendor marketing collateral"},
            {"id": "D", "text": "Compliance documentation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Operational intelligence describes specific, near-term campaigns and adversary operations "
                       "(who, when, how) so defenders can prepare and allocate resources for an impending threat.",
            "distractors": {
                "A": "Strategic intelligence is high-level, long-horizon trends and motivations for executives, not a specific near-term campaign.",
                "C": "Marketing collateral is promotional material, not threat intelligence.",
                "D": "Compliance documentation records regulatory adherence, not adversary campaign details.",
            },
            "exam_pattern": "Specific near-term campaign driving current defensive operations = operational intel; long-term trends = strategic.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Threat intelligence (levels)",
                       "CTI taxonomy: strategic / operational / tactical / technical"],
    },
    {
        "id": "cysa-so-r2-007", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A SOC enriches an indicator using publicly available sources such as WHOIS records, "
                "certificate transparency logs, and public malware repositories. What type of collection is this?",
        "options": [
            {"id": "A", "text": "Open-source intelligence (OSINT)"},
            {"id": "B", "text": "Human intelligence (HUMINT) from a paid informant"},
            {"id": "C", "text": "Signals intelligence intercepted from the adversary"},
            {"id": "D", "text": "Proprietary vendor-only intelligence behind a paywall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Gathering from publicly available data (WHOIS, certificate transparency, public repos) is "
                       "open-source intelligence — collection from freely accessible sources.",
            "distractors": {
                "B": "HUMINT comes from human sources/informants, not public records.",
                "C": "SIGINT is intercepted communications, not public lookups.",
                "D": "Proprietary/closed feeds are paid and non-public — the opposite of OSINT.",
            },
            "exam_pattern": "Enrichment from publicly available data (WHOIS, cert logs, public repos) = OSINT.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Intelligence sources (OSINT vs proprietary/closed)"],
    },
    {
        "id": "cysa-so-r2-008", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 3, "type": "multi",
        "stem": "In MITRE ATT&CK, tactics are the adversary's goals and techniques are the methods. Which TWO "
                "of the following are ATT&CK tactics rather than techniques? (Choose two.)",
        "options": [
            {"id": "A", "text": "Credential Access"},
            {"id": "B", "text": "OS Credential Dumping"},
            {"id": "C", "text": "Exfiltration"},
            {"id": "D", "text": "Exfiltration Over C2 Channel"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Credential Access and Exfiltration are ATT&CK tactics — the adversary's goals (the 'why') "
                       "that head columns of the Enterprise matrix.",
            "distractors": {
                "B": "OS Credential Dumping (T1003) is a specific technique UNDER the Credential Access tactic.",
                "D": "Exfiltration Over C2 Channel (T1041) is a technique UNDER the Exfiltration tactic.",
            },
            "exam_pattern": "ATT&CK tactic = the goal (Credential Access, Exfiltration); technique = the method (T-numbered).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — MITRE ATT&CK",
                       "MITRE ATT&CK: Enterprise tactics (14) and techniques"],
    },

    # ----- so_threat_hunting ---------------------------------------------
    {
        "id": "cysa-so-r2-009", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "With limited time, a hunt team must decide where to search first for a stealthy intruder. "
                "Which approach best focuses the hunt?",
        "options": [
            {"id": "A", "text": "Start with the least important test-lab systems"},
            {"id": "B", "text": "Hunt hosts in random order"},
            {"id": "C", "text": "Wait for an alert to indicate where to look"},
            {"id": "D", "text": "Prioritize the systems holding the organization's most critical data (its 'crown jewels')"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Scarce hunting effort should focus first on the highest-value assets most likely to be "
                       "targeted — the crown jewels — where a compromise would do the most damage.",
            "distractors": {
                "A": "Low-value lab systems are a poor first focus when critical assets are at risk.",
                "B": "Random hunting squanders limited time and lacks a risk rationale.",
                "C": "Waiting for an alert abandons the proactive purpose of hunting.",
            },
            "exam_pattern": "Scope hunts by risk — begin with crown-jewel/high-value assets.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Threat hunting (focusing the hunt)"],
    },
    {
        "id": "cysa-so-r2-010", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "Individually, three observations (a rare parent-child process, a first-seen signed binary, and "
                "an unusual outbound port) each generate too many false positives to alert on alone. How can a "
                "hunter turn them into a reliable detection?",
        "options": [
            {"id": "A", "text": "Alert on each signal separately at maximum severity"},
            {"id": "B", "text": "Correlate the signals so an alert fires only when they co-occur on the same host"},
            {"id": "C", "text": "Disable all three signals to avoid noise"},
            {"id": "D", "text": "Delete the logs that produce the signals"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Combining several low-fidelity signals into a single correlated condition raises confidence: "
                       "the alert fires only when the weak indicators appear together, cutting false positives.",
            "distractors": {
                "A": "Alerting on each weak signal separately recreates the false-positive flood.",
                "C": "Disabling the signals removes visibility entirely.",
                "D": "Deleting logs destroys the evidence and the detection source.",
            },
            "exam_pattern": "Fuse multiple low-fidelity signals into one high-confidence correlated detection.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Threat hunting / detection engineering (signal correlation)"],
    },
    {
        "id": "cysa-so-r2-011", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "A critical, actively exploited vulnerability in the company's VPN appliance is disclosed today. "
                "Before patching completes, what is the most appropriate threat-hunting response?",
        "options": [
            {"id": "A", "text": "Do nothing until the next scheduled vulnerability scan"},
            {"id": "B", "text": "Assume the patch team has it handled and move on"},
            {"id": "C", "text": "Hypothesize the flaw may already have been exploited and hunt telemetry for signs of compromise"},
            {"id": "D", "text": "Immediately shut down the entire corporate network"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An actively exploited flaw on your own technology warrants an assume-breach hunt NOW: form a "
                       "hypothesis that exploitation already occurred and search logs/EDR for indicators, in parallel with patching.",
            "distractors": {
                "A": "Waiting for the next scan ignores possible active compromise in the meantime.",
                "B": "Patching fixes the flaw but does not detect exploitation that already happened.",
                "D": "Shutting down the whole network is disproportionate and does not test the hypothesis.",
            },
            "exam_pattern": "New critical/exploited CVE on your tech = hunt now for prior exploitation (assume breach), not just patch.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Threat hunting (intel-driven, assume breach)"],
    },
    {
        "id": "cysa-so-r2-012", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "After each hunt, a mature team records the hypothesis, data sources queried, the queries used, "
                "and the outcome. What is the primary benefit of documenting hunts this way?",
        "options": [
            {"id": "A", "text": "Hunts become repeatable and measurable, and successful ones can be automated into standing detections"},
            {"id": "B", "text": "It guarantees the environment is now free of all threats"},
            {"id": "C", "text": "It replaces the need for any SIEM or EDR tooling"},
            {"id": "D", "text": "It eliminates the need to ever patch systems"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Documenting the hypothesis, data, queries, and result makes a hunt repeatable and measurable "
                       "and lets the team promote effective hunt logic into automated, continuous detections.",
            "distractors": {
                "B": "Documentation does not guarantee a threat-free environment.",
                "C": "It complements, not replaces, SIEM/EDR tooling.",
                "D": "Hunting and its documentation do not remove the need to patch.",
            },
            "exam_pattern": "Document hunts (hypothesis, data, queries, outcome) for repeatability and automation into detections.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.4 — Threat hunting (documentation, continuous improvement)"],
    },

    # ----- so_malicious_activity -----------------------------------------
    {
        "id": "cysa-so-r2-013", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "EDR flags an unusual process opening a handle to lsass.exe and reading its memory. Which "
                "adversary technique does this most likely indicate?",
        "options": [
            {"id": "A", "text": "Encrypting files for ransom"},
            {"id": "B", "text": "Credential dumping (harvesting credentials from LSASS memory)"},
            {"id": "C", "text": "Defragmenting the disk"},
            {"id": "D", "text": "Rendering a graphics workload"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Local Security Authority Subsystem (lsass.exe) holds credential material in memory; a "
                       "process reading LSASS memory is a hallmark of credential dumping (Credential Access).",
            "distractors": {
                "A": "Ransomware encrypts files on disk; it does not need to read LSASS memory.",
                "C": "Disk defragmentation is routine maintenance and does not access LSASS.",
                "D": "Graphics rendering does not read the LSASS process's memory.",
            },
            "exam_pattern": "Process reading lsass.exe memory = credential dumping (ATT&CK T1003 OS Credential Dumping).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.2 — Indicators of malicious activity (credential dumping)",
                       "MITRE ATT&CK T1003 (OS Credential Dumping, LSASS Memory)"],
    },
    {
        "id": "cysa-so-r2-014", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "mcq",
        "stem": "Just before a suspected exfiltration, an analyst finds a large multi-part .rar archive of "
                "documents created in a server temp directory. Within the attack lifecycle, this step is best "
                "described as...",
        "options": [
            {"id": "A", "text": "Reconnaissance of the target"},
            {"id": "B", "text": "Weaponizing an exploit"},
            {"id": "C", "text": "Collection / staging of data prior to exfiltration"},
            {"id": "D", "text": "Patching a vulnerability"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Bundling and compressing target files into an archive in a temp location is data staging — "
                       "collecting data into a single package to simplify its later exfiltration.",
            "distractors": {
                "A": "Reconnaissance gathers target information; it does not package the victim's files.",
                "B": "Weaponization builds the attack payload, not an archive of stolen data.",
                "D": "Patching is a defensive action, not attacker behavior.",
            },
            "exam_pattern": "Compressing/encrypting data into archives before sending it out = staging/collection ahead of exfiltration.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.2 — Indicators of malicious activity (data staging/exfiltration)",
                       "MITRE ATT&CK T1560 (Archive Collected Data)"],
    },
    {
        "id": "cysa-so-r2-015", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "mcq",
        "stem": "Malware on a host makes DNS lookups for dozens of long, algorithmically generated domain names "
                "each day, most of which fail to resolve, until one succeeds. Which C2 resilience technique is this?",
        "options": [
            {"id": "A", "text": "A single hard-coded C2 IP address"},
            {"id": "B", "text": "Normal corporate DNS caching"},
            {"id": "C", "text": "TLS certificate pinning"},
            {"id": "D", "text": "A domain generation algorithm (DGA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A domain generation algorithm produces many pseudo-random domains so the implant can find a "
                       "live C2 even as domains are taken down; most generated lookups fail (NXDOMAIN) until one resolves.",
            "distractors": {
                "A": "A single hard-coded IP is the opposite of many rotating generated domains.",
                "B": "Benign DNS caching does not produce floods of failing algorithmic domains.",
                "C": "Certificate pinning validates TLS endpoints and is unrelated to DNS generation.",
            },
            "exam_pattern": "Many algorithmic, mostly-failing domain lookups until one resolves = DGA for resilient C2.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.2 — Network indicators (C2/DGA)",
                       "MITRE ATT&CK T1568.002 (Domain Generation Algorithms)"],
    },
    {
        "id": "cysa-so-r2-016", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "A user account authenticates successfully from New York and then, eight minutes later, from "
                "Singapore. Which account-based indicator does this represent?",
        "options": [
            {"id": "A", "text": "Impossible (atypical) travel, indicating likely credential compromise"},
            {"id": "B", "text": "Normal single-session activity"},
            {"id": "C", "text": "A DNS tunneling attempt"},
            {"id": "D", "text": "A disk-encryption event"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "One account signing in from two locations too far apart to travel between in the elapsed "
                       "time is impossible/atypical travel — a strong sign the credentials are being used by someone else.",
            "distractors": {
                "B": "A single user cannot physically be in both cities minutes apart; this is not normal.",
                "C": "DNS tunneling is a data-smuggling technique, unrelated to geographic logon anomalies.",
                "D": "Disk encryption is a host storage event, not an authentication anomaly.",
            },
            "exam_pattern": "Two logins from geographically impossible locations in a short window = impossible/atypical travel.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.2 — Indicators of malicious activity (account anomalies)"],
    },

    # ----- so_tools_automation -------------------------------------------
    {
        "id": "cysa-so-r2-017", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 3, "type": "mcq",
        "stem": "In a saved capture opened in Wireshark, an analyst wants to display only HTTP POST requests. "
                "Which Wireshark DISPLAY filter does this?",
        "options": [
            {"id": "A", "text": "port 80"},
            {"id": "B", "text": "http.request.method == \"POST\""},
            {"id": "C", "text": "tcp dst port 80 and http"},
            {"id": "D", "text": "grep POST capture.pcap"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Wireshark display filters reference dissected protocol fields; http.request.method == \"POST\" "
                       "shows only HTTP requests whose method is POST.",
            "distractors": {
                "A": "'port 80' is capture (BPF) syntax, not a display filter, and does not isolate POST requests.",
                "C": "This mixes BPF and display syntax and is not a valid Wireshark display filter.",
                "D": "grep is a shell text tool, not a Wireshark filter, and cannot parse HTTP methods in a pcap.",
            },
            "exam_pattern": "Wireshark DISPLAY filters use protocol fields (http.request.method == \"POST\"); BPF CAPTURE filters use 'port 80'.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.3 — Packet analysis (Wireshark display filters)"],
    },
    {
        "id": "cysa-so-r2-018", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "A platform builds behavioral baselines for each user and device and alerts when activity "
                "deviates sharply from normal, helping catch compromised accounts and insider threats. Which "
                "capability is this?",
        "options": [
            {"id": "A", "text": "Traditional signature-based antivirus"},
            {"id": "B", "text": "A static firewall ruleset"},
            {"id": "C", "text": "User and entity behavior analytics (UEBA)"},
            {"id": "D", "text": "A network time (NTP) server"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "UEBA profiles normal behavior for users and entities and flags anomalies, making it well "
                       "suited to detecting compromised accounts and insider activity that signatures miss.",
            "distractors": {
                "A": "Signature-based antivirus matches known malware patterns, not per-user behavioral baselines.",
                "B": "A static firewall ruleset enforces fixed policy, not behavioral anomaly detection.",
                "D": "An NTP server synchronizes clocks and performs no analytics.",
            },
            "exam_pattern": "Per-user/entity behavioral baselining with anomaly alerts = UEBA.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.3 — Analysis tools (UEBA/behavioral analytics)"],
    },
    {
        "id": "cysa-so-r2-019", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "A team wants one platform that correlates and responds to threats across endpoints, email, "
                "identity, and cloud workloads, instead of analyzing each in a separate console. Which category fits?",
        "options": [
            {"id": "A", "text": "A standalone antivirus agent"},
            {"id": "B", "text": "A single-host EDR with no other telemetry"},
            {"id": "C", "text": "A label printer"},
            {"id": "D", "text": "Extended detection and response (XDR)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "XDR unifies and correlates telemetry across multiple layers (endpoint, email, identity, "
                       "cloud) into one detection-and-response platform, broadening visibility beyond a single domain.",
            "distractors": {
                "A": "Standalone antivirus covers one endpoint layer, not cross-domain correlation.",
                "B": "Single-host EDR is endpoint-only and does not unify email/identity/cloud telemetry.",
                "C": "A label printer has no security-analytics function.",
            },
            "exam_pattern": "Cross-layer (endpoint + email + identity + cloud) correlated detection/response = XDR.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.3 — Detection/response tools (XDR vs EDR)"],
    },
    {
        "id": "cysa-so-r2-020", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "multi",
        "stem": "An analyst must extract and tally every unique source IP from a 5 GB firewall log. Which TWO "
                "approaches are efficient and repeatable? (Choose two.)",
        "options": [
            {"id": "A", "text": "Apply a regular expression that matches the IPv4 address pattern"},
            {"id": "B", "text": "Manually scroll through all 5 GB and note IPs by hand"},
            {"id": "C", "text": "Write a script that streams the file line by line and aggregates counts"},
            {"id": "D", "text": "Reboot the syslog server to refresh the file"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "A regular expression reliably matches IPv4 strings, and a script that streams the file and "
                       "aggregates counts handles the volume quickly and the same way every time.",
            "distractors": {
                "B": "Reading 5 GB by hand is infeasible, slow, and error-prone.",
                "D": "Rebooting the server does nothing to parse or extract data from the log.",
            },
            "exam_pattern": "Parse/aggregate large logs with regex + scripting (stream and count), not by hand.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 1.3 — Scripting/automation for analysis (regex, log parsing)"],
    },

    # =====================================================================
    # DOMAIN 2.0 — VULNERABILITY MANAGEMENT (18 items)
    # =====================================================================

    # ----- vm_scanning ---------------------------------------------------
    {
        "id": "cysa-vm-r2-001", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_scanning", "difficulty": 2, "type": "mcq",
        "stem": "A federal agency must run automated configuration-compliance checks that different tools can "
                "interpret consistently against a standardized benchmark. Which protocol suite is designed for this?",
        "options": [
            {"id": "A", "text": "SCAP (Security Content Automation Protocol)"},
            {"id": "B", "text": "SMTP"},
            {"id": "C", "text": "SNMPv2c"},
            {"id": "D", "text": "RADIUS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SCAP is a NIST-maintained suite (XCCDF, OVAL, CPE, CVE, CCE, CVSS) that standardizes how "
                       "security-configuration and vulnerability content is expressed, enabling automated, tool-agnostic compliance checking.",
            "distractors": {
                "B": "SMTP transports email; it has no role in compliance content.",
                "C": "SNMP monitors/manages devices, not standardized compliance checklists.",
                "D": "RADIUS provides AAA for network access, not configuration-compliance scanning.",
            },
            "exam_pattern": "Standardized, automated, tool-agnostic compliance/config checking = SCAP (XCCDF/OVAL/CPE/CVE).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.1 — Scanning/compliance (SCAP)",
                       "NIST SP 800-126 — The Technical Specification for SCAP"],
    },
    {
        "id": "cysa-vm-r2-002", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_scanning", "difficulty": 3, "type": "mcq",
        "stem": "An internal scanner on the user VLAN reports a database server segment as 'clean,' but a "
                "firewall between them blocks the scanner's probes. What is the most likely problem?",
        "options": [
            {"id": "A", "text": "The database segment is genuinely free of all vulnerabilities"},
            {"id": "B", "text": "The firewall is dropping probes, so the scan under-reports (false negatives); scan from inside the protected segment"},
            {"id": "C", "text": "The scanner simply needs a faster CPU"},
            {"id": "D", "text": "The database should be deleted"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "If filtering blocks the scanner's packets, the scanner cannot see the hosts' real exposure, so "
                       "a 'clean' result is unreliable (false negatives). Placing a scanner inside the segment restores visibility.",
            "distractors": {
                "A": "A blocked scan cannot prove a host is clean; absence of findings here reflects blocked probes.",
                "C": "CPU speed is irrelevant when probes never reach the targets.",
                "D": "Deleting the database is not a response to a blocked scan.",
            },
            "exam_pattern": "A firewall/segment between scanner and target hides vulnerabilities (false negatives); scan from inside the segment.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.1 — Scanning considerations (scanner placement/segmentation)"],
    },
    {
        "id": "cysa-vm-r2-003", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_scanning", "difficulty": 2, "type": "mcq",
        "stem": "A DevOps team ships applications as container images. Where should vulnerability scanning be "
                "integrated to catch vulnerable packages before containers reach production?",
        "options": [
            {"id": "A", "text": "Only by inspecting the physical data-center perimeter"},
            {"id": "B", "text": "Only after a breach is reported"},
            {"id": "C", "text": "By scanning container images in the registry / CI pipeline before deployment"},
            {"id": "D", "text": "By scanning the office Wi-Fi password"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Scanning images in the registry and CI/CD pipeline (shift-left) catches vulnerable OS packages "
                       "and libraries before the image is deployed, when remediation is cheapest.",
            "distractors": {
                "A": "Physical-perimeter inspection is unrelated to a container image's software contents.",
                "B": "Post-breach scanning is reactive and far too late.",
                "D": "The Wi-Fi password has nothing to do with image vulnerabilities.",
            },
            "exam_pattern": "Scan container images in the registry/CI pipeline (shift-left) before deployment.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.1/2.2 — Scanning (container/image scanning in CI/CD)"],
    },
    {
        "id": "cysa-vm-r2-004", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_scanning", "difficulty": 2, "type": "mcq",
        "stem": "A cloud environment creates and destroys ephemeral instances many times per day, so a monthly "
                "scan always misses most of them. Which scanning strategy best maintains visibility?",
        "options": [
            {"id": "A", "text": "A single annual scan"},
            {"id": "B", "text": "A one-time baseline scan only"},
            {"id": "C", "text": "Disabling scanning in the cloud"},
            {"id": "D", "text": "Continuous / automated scanning triggered as assets are provisioned"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Highly dynamic, short-lived cloud assets require continuous or event-triggered scanning so each "
                       "instance is assessed while it exists, rather than being missed between infrequent scans.",
            "distractors": {
                "A": "An annual scan misses almost all short-lived instances.",
                "B": "A one-time baseline cannot track constant change.",
                "C": "Disabling scanning removes visibility entirely.",
            },
            "exam_pattern": "Dynamic/ephemeral (cloud) assets need continuous/automated scanning, not infrequent scheduled scans.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.1 — Scan frequency (continuous vs periodic; ephemeral assets)"],
    },

    # ----- vm_assessment_tools -------------------------------------------
    {
        "id": "cysa-vm-r2-005", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_assessment_tools", "difficulty": 2, "type": "mcq",
        "stem": "During discovery, an analyst needs to identify the exact service and software version listening "
                "on each open port. Which Nmap option is purpose-built for this?",
        "options": [
            {"id": "A", "text": "-sV (service/version detection)"},
            {"id": "B", "text": "-sn (host discovery only, no port scan)"},
            {"id": "C", "text": "--top-ports 10 with no other flags"},
            {"id": "D", "text": "-oN (write output to a normal-format file)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Nmap -sV probes open ports and fingerprints the service and version behind them, which is "
                       "essential for mapping findings to version-specific vulnerabilities.",
            "distractors": {
                "B": "-sn performs host discovery only and scans no ports or services.",
                "C": "Limiting to the top ports narrows scope but does not fingerprint versions.",
                "D": "-oN only controls output format; it does not perform version detection.",
            },
            "exam_pattern": "Identify service + version on open ports = Nmap -sV.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.2 — Assessment tools (Nmap -sV)"],
    },
    {
        "id": "cysa-vm-r2-006", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_assessment_tools", "difficulty": 2, "type": "mcq",
        "stem": "To respond quickly the next time a vulnerable library is disclosed, a company wants a formal, "
                "machine-readable inventory of every component and dependency inside each application. Which artifact provides this?",
        "options": [
            {"id": "A", "text": "A network topology diagram"},
            {"id": "B", "text": "A software bill of materials (SBOM)"},
            {"id": "C", "text": "A data-flow privacy notice"},
            {"id": "D", "text": "A disaster-recovery runbook"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An SBOM is a formal inventory of an application's components and dependencies; paired with "
                       "software composition analysis, it lets teams instantly see which apps use a newly disclosed vulnerable library.",
            "distractors": {
                "A": "A network diagram maps hosts and links, not software components.",
                "C": "A privacy notice describes data handling, not code dependencies.",
                "D": "A DR runbook covers recovery steps, not a component inventory.",
            },
            "exam_pattern": "Formal inventory of software components/dependencies = SBOM (pairs with SCA).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.2 — Assessment (SBOM / software composition analysis)"],
    },
    {
        "id": "cysa-vm-r2-007", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_assessment_tools", "difficulty": 3, "type": "mcq",
        "stem": "A tester feeds a program large volumes of malformed, unexpected, and random inputs to trigger "
                "crashes or memory errors that reveal vulnerabilities. Which technique is this?",
        "options": [
            {"id": "A", "text": "Static source-code review"},
            {"id": "B", "text": "Software composition analysis"},
            {"id": "C", "text": "Fuzzing (fuzz testing)"},
            {"id": "D", "text": "Hashing the binary"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Fuzzing is a dynamic technique that bombards a running program with malformed/random inputs to "
                       "surface crashes, hangs, and memory-safety flaws that structured tests miss.",
            "distractors": {
                "A": "Static review reads code without executing it; fuzzing runs the program with crafted inputs.",
                "B": "SCA inventories dependencies; it does not send malformed inputs to the running program.",
                "D": "Hashing verifies integrity, not robustness against bad input.",
            },
            "exam_pattern": "Feeding malformed/random inputs to a running program to find crashes = fuzzing (dynamic).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.2 — Assessment techniques (fuzzing/dynamic analysis)"],
    },
    {
        "id": "cysa-vm-r2-008", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_assessment_tools", "difficulty": 3, "type": "mcq",
        "stem": "A lead weighs SAST against DAST. Which statement correctly captures a key trade-off between them?",
        "options": [
            {"id": "A", "text": "SAST needs a running application and cannot see source code"},
            {"id": "B", "text": "DAST pinpoints the exact vulnerable source line but never runs the application"},
            {"id": "C", "text": "SAST and DAST are identical in method and results"},
            {"id": "D", "text": "SAST pinpoints vulnerable code early but tends to produce more false positives, while DAST tests the running app and finds runtime/config flaws without locating the code"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SAST (white-box, no execution) finds issues early and names the code location but is prone to "
                       "false positives; DAST (black-box, running app) finds runtime and configuration flaws but cannot point to the exact source line.",
            "distractors": {
                "A": "This reverses the definitions — SAST analyzes source WITHOUT running the app.",
                "B": "This reverses them — DAST runs the app and does NOT identify source lines.",
                "C": "They are fundamentally different techniques (static white-box vs dynamic black-box).",
            },
            "exam_pattern": "SAST = early, code-level, more false positives; DAST = runtime/black-box, finds config flaws but no code location.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.2 — SAST vs DAST (trade-offs)"],
    },

    # ----- vm_prioritization ---------------------------------------------
    {
        "id": "cysa-vm-r2-009", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_prioritization", "difficulty": 3, "type": "mcq",
        "stem": "Two vulnerabilities are identical except that one needs no special conditions to exploit, while "
                "the other works only if the attacker first wins a timing race condition. How does CVSS v3.1 reflect "
                "the easier one, and what is the score effect?",
        "options": [
            {"id": "A", "text": "Attack Complexity: Low, which raises the base score"},
            {"id": "B", "text": "Attack Complexity: High, which raises the base score"},
            {"id": "C", "text": "Attack Complexity: Low, which lowers the base score"},
            {"id": "D", "text": "Privileges Required: High, which raises the base score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "No special conditions = Attack Complexity: Low, meaning reliably repeatable exploitation, which "
                       "increases the CVSS base score. The race-condition case would be AC:High and score lower.",
            "distractors": {
                "B": "The easy case is AC:Low, not High; AC:High (special conditions) LOWERS the score.",
                "C": "AC:Low raises, not lowers, the base score.",
                "D": "This scenario is about complexity, not privileges, and PR:High actually lowers the score.",
            },
            "exam_pattern": "CVSS AC:Low (no special conditions) = easier = higher score; AC:High (e.g., race condition) lowers it.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.3 — CVSS base metrics (Attack Complexity)",
                       "FIRST CVSS v3.1 Specification"],
    },
    {
        "id": "cysa-vm-r2-010", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_prioritization", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability can be exploited only if a victim opens a malicious document. Which CVSS v3.1 "
                "base metric value captures this, and how does it affect the score versus a flaw needing no victim action?",
        "options": [
            {"id": "A", "text": "User Interaction: None, raising the score"},
            {"id": "B", "text": "User Interaction: Required, lowering the score relative to UI:None"},
            {"id": "C", "text": "Attack Vector: Physical, raising the score"},
            {"id": "D", "text": "Scope: Changed, lowering the score"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Needing a victim to act sets User Interaction: Required, which lowers the base score compared "
                       "with UI:None (no victim action needed), because exploitation depends on someone else's behavior.",
            "distractors": {
                "A": "The flaw needs victim action, so UI is Required, not None.",
                "C": "Requiring a user to open a file is not Attack Vector: Physical, and that would not apply here.",
                "D": "Scope: Changed describes cross-boundary impact, not victim interaction, and does not lower the score for this reason.",
            },
            "exam_pattern": "Needs victim action = UI:Required (lower score); no action needed = UI:None (higher score).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.3 — CVSS base metrics (User Interaction)",
                       "FIRST CVSS v3.1 Specification"],
    },
    {
        "id": "cysa-vm-r2-011", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_prioritization", "difficulty": 3, "type": "mcq",
        "stem": "Beyond the base score, a team wants their CVSS rating to rise when a working, weaponized exploit "
                "becomes publicly available and fall when a vendor patch ships. Which CVSS metric group captures "
                "these conditions that change over time?",
        "options": [
            {"id": "A", "text": "The Base metric group"},
            {"id": "B", "text": "The Confidentiality/Integrity/Availability impact sub-metrics"},
            {"id": "C", "text": "The Temporal metric group (e.g., Exploit Code Maturity, Remediation Level)"},
            {"id": "D", "text": "The Attack Vector metric alone"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Temporal metrics (Exploit Code Maturity, Remediation Level, Report Confidence) adjust the score "
                       "for conditions that change over time — a public weaponized exploit raises it; an official fix lowers it.",
            "distractors": {
                "A": "Base metrics are intrinsic and constant; they do not vary with exploit availability.",
                "B": "CIA impacts are part of the base score and do not track exploit/patch status.",
                "D": "Attack Vector is a single base metric, not the time-varying group.",
            },
            "exam_pattern": "Exploit availability / patch status over time = CVSS Temporal metrics.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.3 — CVSS metric groups (Temporal)",
                       "FIRST CVSS v3.1 Specification"],
    },
    {
        "id": "cysa-vm-r2-012", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_prioritization", "difficulty": 2, "type": "mcq",
        "stem": "Two hosts share the same CVSS base score of 7.5. One is a sandbox holding no data; the other "
                "stores regulated customer financial records. Which factor should raise the second host's remediation priority?",
        "options": [
            {"id": "A", "text": "Nothing — identical base scores must be treated identically"},
            {"id": "B", "text": "The alphabetical order of the hostnames"},
            {"id": "C", "text": "The scanner's plugin ID"},
            {"id": "D", "text": "Asset criticality and data sensitivity (environmental/business context)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Prioritization weighs business context: the host with regulated financial data is a far more "
                       "valuable target with greater impact if exploited, so asset criticality/data sensitivity (CVSS environmental context) elevates its priority.",
            "distractors": {
                "A": "Equal base scores do not mean equal risk; context differentiates them.",
                "B": "Hostname order is arbitrary and irrelevant to risk.",
                "C": "The plugin ID is scan metadata, not a risk factor.",
            },
            "exam_pattern": "Tailor priority with asset criticality/data sensitivity (CVSS Environmental), not base score alone.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.3 — Prioritization (asset criticality, CVSS Environmental)"],
    },

    # ----- vm_mitigation -------------------------------------------------
    {
        "id": "cysa-vm-r2-013", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_mitigation", "difficulty": 2, "type": "mcq",
        "stem": "After mitigating what it can, a company buys a cyber-insurance policy to cover the residual "
                "financial loss from a potential breach. Which risk-response strategy is this?",
        "options": [
            {"id": "A", "text": "Risk transference"},
            {"id": "B", "text": "Risk avoidance"},
            {"id": "C", "text": "Risk acceptance with no action"},
            {"id": "D", "text": "Risk mitigation by patching"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shifting the financial consequences of a risk to a third party (an insurer) is risk "
                       "transference; it addresses the residual risk left after other controls are applied.",
            "distractors": {
                "B": "Avoidance eliminates the risky activity/exposure entirely, not just shifts its cost.",
                "C": "Acceptance retains the loss and takes no action; insurance instead shifts the loss.",
                "D": "The technical mitigation is already done; insurance covers what remains, so this is not patching.",
            },
            "exam_pattern": "Shifting residual financial risk to a third party (insurance) = risk transference.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.5 — Risk response (transfer/avoid/accept/mitigate)"],
    },
    {
        "id": "cysa-vm-r2-014", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_mitigation", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the chance that a bad patch disrupts the whole fleet, an admin deploys a critical "
                "update first to a small pilot group, monitors for problems, then expands to the rest. Which practice is this?",
        "options": [
            {"id": "A", "text": "Deploying to all systems simultaneously"},
            {"id": "B", "text": "Phased (ring / canary) deployment"},
            {"id": "C", "text": "Skipping the patch entirely"},
            {"id": "D", "text": "Rolling the patch back before testing it"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A phased or ring/canary rollout validates the patch on a small group first, limiting the blast "
                       "radius if it causes problems before it reaches the full environment.",
            "distractors": {
                "A": "Simultaneous deployment maximizes the blast radius if the patch is faulty.",
                "C": "Skipping the patch leaves the vulnerability unaddressed.",
                "D": "Rolling back before any testing defeats the purpose of validating the patch.",
            },
            "exam_pattern": "Pilot group first, monitor, then expand = phased/ring (canary) deployment.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.5 — Patch management (phased deployment)"],
    },
    {
        "id": "cysa-vm-r2-015", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_mitigation", "difficulty": 2, "type": "mcq",
        "stem": "Before applying a kernel update to a critical production server, the change ticket documents "
                "the exact steps to restore the previous state if the update fails. What is this element called?",
        "options": [
            {"id": "A", "text": "A chain-of-custody form"},
            {"id": "B", "text": "A data-retention schedule"},
            {"id": "C", "text": "A rollback (backout) plan"},
            {"id": "D", "text": "A vulnerability disclosure policy"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A rollback/backout plan documents how to revert a change if it fails, limiting downtime and "
                       "risk; it is a standard element of change management for critical systems.",
            "distractors": {
                "A": "Chain of custody tracks evidence handling, not change reversal.",
                "B": "A retention schedule governs how long data is kept.",
                "D": "A disclosure policy governs reporting vulnerabilities, not reverting a change.",
            },
            "exam_pattern": "Documented way to revert a failed change = rollback/backout plan (change management).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.5 — Change management (rollback/backout planning)"],
    },

    # ----- vm_secure_coding ----------------------------------------------
    {
        "id": "cysa-vm-r2-016", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_secure_coding", "difficulty": 3, "type": "multi",
        "stem": "Which TWO controls specifically help prevent cross-site request forgery (CSRF)? (Choose two.)",
        "options": [
            {"id": "A", "text": "Per-session anti-CSRF (synchronizer) tokens"},
            {"id": "B", "text": "SameSite cookie attributes"},
            {"id": "C", "text": "Parameterized SQL queries"},
            {"id": "D", "text": "Forcing a longer password minimum length"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Unpredictable per-session anti-CSRF tokens (that attackers cannot guess) and SameSite cookies "
                       "(which stop the browser from sending session cookies on cross-site requests) both defeat CSRF.",
            "distractors": {
                "C": "Parameterized queries prevent SQL injection, not forged cross-site requests.",
                "D": "Password length does not stop a forged request against an already-authenticated session.",
            },
            "exam_pattern": "CSRF defenses = anti-CSRF (synchronizer) tokens + SameSite cookies (not SQLi/password controls).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.4 — Secure coding (CSRF mitigation)",
                       "OWASP CSRF Prevention Cheat Sheet"],
    },
    {
        "id": "cysa-vm-r2-017", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A web app fetches a user-supplied URL on the server side. An attacker supplies "
                "http://169.254.169.254/ and retrieves cloud instance credentials. Which vulnerability class is "
                "this, and a key mitigation?",
        "options": [
            {"id": "A", "text": "Cross-site scripting; fix with output encoding"},
            {"id": "B", "text": "Server-side request forgery (SSRF); validate/allowlist outbound destinations and block the metadata endpoint"},
            {"id": "C", "text": "SQL injection; fix with prepared statements"},
            {"id": "D", "text": "Broken authentication; fix by enforcing MFA"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Coercing the server to request an attacker-chosen URL — here the cloud metadata address "
                       "169.254.169.254 — is SSRF; mitigations include allowlisting outbound destinations and blocking access to the metadata endpoint.",
            "distractors": {
                "A": "XSS executes script in a victim's browser; output encoding does not stop a server-side fetch.",
                "C": "SQL injection targets a database query, not server-side URL fetching.",
                "D": "MFA protects login, not a server making an attacker-controlled outbound request.",
            },
            "exam_pattern": "Server fetches an attacker-controlled URL (e.g., cloud metadata 169.254.169.254) = SSRF; allowlist/block metadata.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.4 — Secure coding (SSRF)",
                       "OWASP Top 10 A10:2021 — Server-Side Request Forgery"],
    },
    {
        "id": "cysa-vm-r2-018", "exam": "cysa", "domain": "cysa_vuln_management",
        "subtopic": "vm_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "A code review finds a database password and an API key written directly into source code and "
                "committed to the repository. What is the best remediation?",
        "options": [
            {"id": "A", "text": "Rename the variables that hold the secrets"},
            {"id": "B", "text": "Add a code comment warning not to share the file"},
            {"id": "C", "text": "Base64-encode the secrets in the source"},
            {"id": "D", "text": "Remove the secrets from code, load them at runtime from a secrets manager/vault, and rotate the exposed credentials"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Hardcoded secrets must be removed from code and version history, supplied at runtime from a "
                       "secrets manager/vault, and rotated, because anything committed to the repo should be treated as compromised.",
            "distractors": {
                "A": "Renaming variables leaves the secrets in the code and its history.",
                "B": "A comment does nothing to protect already-exposed secrets.",
                "C": "Base64 is reversible encoding, not protection; the secret is still exposed.",
            },
            "exam_pattern": "Hardcoded secrets = remove from code, use a secrets manager/vault, and rotate the exposed credentials.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 2.4 — Secure coding (secrets management)",
                       "OWASP Top 10 A02:2021 — Cryptographic Failures (hardcoded credentials)"],
    },

    # =====================================================================
    # DOMAIN 3.0 — INCIDENT RESPONSE AND MANAGEMENT (12 items)
    # =====================================================================

    # ----- ir_lifecycle --------------------------------------------------
    {
        "id": "cysa-ir-r2-001", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A SOC uses the SANS six-step handling process (Preparation, Identification, Containment, "
                "Eradication, Recovery, Lessons Learned). Which step corresponds to NIST's 'Detection and "
                "Analysis' — confirming an event is a real incident and determining its scope?",
        "options": [
            {"id": "A", "text": "Identification"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In the SANS model, Identification is where responders validate that an event is a genuine "
                       "incident and scope it — the same work NIST SP 800-61 places in Detection and Analysis.",
            "distractors": {
                "B": "Containment limits spread AFTER the incident is identified.",
                "C": "Eradication removes the threat after containment.",
                "D": "Recovery restores normal operations near the end of the process.",
            },
            "exam_pattern": "SANS 'Identification' = NIST 'Detection and Analysis' (confirm and scope the incident).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Incident response process (SANS PICERL vs NIST)",
                       "NIST SP 800-61 — Computer Security Incident Handling Guide"],
    },
    {
        "id": "cysa-ir-r2-002", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An adversary emails a weaponized PDF to employees. In the Lockheed Martin Cyber Kill Chain, "
                "transmitting the weaponized payload to the target is which phase?",
        "options": [
            {"id": "A", "text": "Weaponization"},
            {"id": "B", "text": "Delivery"},
            {"id": "C", "text": "Installation"},
            {"id": "D", "text": "Actions on Objectives"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Delivery is the transmission of the weaponized payload to the victim — for example a phishing "
                       "email, malicious link, or infected USB.",
            "distractors": {
                "A": "Weaponization is building/coupling the payload before it is sent, not transmitting it.",
                "C": "Installation is implanting a backdoor after successful exploitation.",
                "D": "Actions on Objectives is the final goal, such as exfiltration.",
            },
            "exam_pattern": "Transmitting the weapon to the victim (phishing email, malicious USB) = Delivery.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.1 — Attack frameworks (Cyber Kill Chain: Delivery)",
                       "Lockheed Martin — Cyber Kill Chain"],
    },
    {
        "id": "cysa-ir-r2-003", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A ransomware outage threatens to halt order processing. Which plan specifically addresses "
                "keeping critical business functions operating during the disruption?",
        "options": [
            {"id": "A", "text": "The incident response plan (IRP)"},
            {"id": "B", "text": "The disaster recovery plan (DRP)"},
            {"id": "C", "text": "The business continuity plan (BCP)"},
            {"id": "D", "text": "The acceptable use policy (AUP)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The business continuity plan keeps critical business functions running (often via alternate "
                       "processes) during a disruption, whereas the DRP focuses on restoring IT systems afterward.",
            "distractors": {
                "A": "The IRP governs detecting and handling the security incident, not sustaining operations.",
                "B": "The DRP focuses on recovering/restoring IT systems and infrastructure after a disaster.",
                "D": "An AUP defines acceptable use of resources and is unrelated to continuity.",
            },
            "exam_pattern": "Keep critical business functions running during disruption = BCP; restore IT after disaster = DRP; handle the incident = IRP.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.3 — Incident management (BCP vs DRP vs IRP)"],
    },
    {
        "id": "cysa-ir-r2-004", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 3, "type": "mcq",
        "stem": "Using the Diamond Model, an analyst starts from a known malicious C2 IP (infrastructure) and "
                "queries passive DNS and registration data to uncover the adversary and additional capabilities. "
                "This analytic move across the model's vertices is called...",
        "options": [
            {"id": "A", "text": "Weaponization"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Order of volatility"},
            {"id": "D", "text": "Pivoting"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Pivoting is the Diamond Model technique of using one known feature (e.g., infrastructure) to "
                       "discover others (adversary, capability, victim), expanding understanding of the intrusion.",
            "distractors": {
                "A": "Weaponization is an attacker Cyber Kill Chain step, not a Diamond Model analytic technique.",
                "B": "Containment is an incident-response action, not Diamond-Model analysis.",
                "C": "Order of volatility governs the sequence of evidence collection, not intrusion analysis.",
            },
            "exam_pattern": "Using one known Diamond vertex (e.g., infrastructure) to discover another (adversary/capability) = pivoting.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.1 — Attack frameworks (Diamond Model: pivoting)"],
    },

    # ----- ir_detection_analysis -----------------------------------------
    {
        "id": "cysa-ir-r2-005", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Before analyzing a suspect hard drive, an examiner connects it through a device that permits "
                "reading but prevents any writes to the original media. What is this device?",
        "options": [
            {"id": "A", "text": "A write blocker"},
            {"id": "B", "text": "A KVM switch"},
            {"id": "C", "text": "A network tap"},
            {"id": "D", "text": "A USB hub"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A write blocker allows read-only access to source media during imaging, preventing any "
                       "modification so the evidence stays forensically sound and admissible.",
            "distractors": {
                "B": "A KVM switch shares a keyboard, video, and mouse across computers; it provides no write protection.",
                "C": "A network tap copies network traffic; it does not protect a disk.",
                "D": "A USB hub only adds ports and offers no write protection.",
            },
            "exam_pattern": "Read-only acquisition that prevents altering the source disk = write blocker.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Forensics/evidence acquisition (write blocker)"],
    },
    {
        "id": "cysa-ir-r2-006", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "mcq",
        "stem": "Per NIST SP 800-61 terminology, a server log shows reconnaissance scanning that suggests an "
                "attack on a web app may be coming. Is this a precursor or an indicator, and why?",
        "options": [
            {"id": "A", "text": "An indicator, because the attack has already succeeded"},
            {"id": "B", "text": "A precursor, because it is a sign that an incident may occur in the future"},
            {"id": "C", "text": "A precursor, because the breach is confirmed and ongoing"},
            {"id": "D", "text": "An indicator, because the system has already been eradicated"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A precursor is a sign that an incident may occur in the future; reconnaissance scanning hints "
                       "at a possible upcoming attack but is not itself evidence that one has happened.",
            "distractors": {
                "A": "Nothing shows the attack succeeded; a sign of a POSSIBLE future attack is a precursor, not an indicator.",
                "C": "A precursor concerns a possible future event, not a confirmed ongoing breach.",
                "D": "Eradication has not occurred, and this is not evidence of a current incident.",
            },
            "exam_pattern": "Precursor = sign an incident MAY occur later; indicator = sign an incident may be occurring or has occurred.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Detection and analysis (precursors vs indicators)",
                       "NIST SP 800-61 — precursors and indicators"],
    },
    {
        "id": "cysa-ir-r2-007", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "mcq",
        "stem": "To prove that a now-deleted malicious executable actually ran on a Windows host, which forensic "
                "artifact is most useful?",
        "options": [
            {"id": "A", "text": "The desktop wallpaper file"},
            {"id": "B", "text": "The printer spooler queue"},
            {"id": "C", "text": "Windows Prefetch files"},
            {"id": "D", "text": "The display driver version"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Prefetch files record program execution (name, run count, timestamps) and persist even after "
                       "the executable is deleted, providing strong evidence that a binary ran.",
            "distractors": {
                "A": "Wallpaper settings do not record program execution.",
                "B": "The print spooler tracks print jobs, not arbitrary program runs.",
                "D": "The display driver version says nothing about what executed.",
            },
            "exam_pattern": "Evidence a program executed (even if deleted) = Prefetch (and related artifacts like Shimcache/Amcache).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Forensic analysis (Windows execution artifacts)"],
    },
    {
        "id": "cysa-ir-r2-008", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "mcq",
        "stem": "An analyst has a RAM image from a compromised host and needs to list the processes that were "
                "running, their network connections, and any injected code at capture time. Which approach fits?",
        "options": [
            {"id": "A", "text": "A disk defragmenter"},
            {"id": "B", "text": "A password manager"},
            {"id": "C", "text": "Recomputing the file's CRC checksum"},
            {"id": "D", "text": "A memory-forensics framework such as Volatility"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Memory-forensics tools like Volatility parse a RAM capture to reconstruct running processes, "
                       "network connections, loaded modules, and injected code that never touch disk.",
            "distractors": {
                "A": "A defragmenter reorganizes disk storage and cannot parse a memory image.",
                "B": "A password manager stores credentials; it does not analyze RAM.",
                "C": "A CRC is an integrity check, not a memory analysis.",
            },
            "exam_pattern": "Analyze a RAM capture (processes, connections, injected code) = memory forensics (e.g., Volatility).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Forensic analysis (memory/RAM analysis)"],
    },

    # ----- ir_containment_recovery ---------------------------------------
    {
        "id": "cysa-ir-r2-009", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "Responders must contain a compromised server that likely holds important volatile evidence. "
                "Which containment action best stops attacker access while preserving that evidence?",
        "options": [
            {"id": "A", "text": "Network-isolate the host (e.g., move it to a quarantine VLAN) while leaving it powered on"},
            {"id": "B", "text": "Immediately pull the power cord"},
            {"id": "C", "text": "Immediately wipe and reimage the disk"},
            {"id": "D", "text": "Leave it fully connected and keep watching"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Isolating the host (quarantine VLAN, port block) cuts off the attacker while keeping the system "
                       "powered on so volatile evidence in RAM is preserved for acquisition.",
            "distractors": {
                "B": "Pulling power destroys volatile memory evidence (running processes, keys, network state).",
                "C": "Wiping/reimaging destroys all evidence and is an eradication step, not evidence-preserving containment.",
                "D": "Leaving it connected allows continued attacker access and ongoing damage.",
            },
            "exam_pattern": "Preserve volatile evidence AND stop access = isolate (quarantine) while powered on; don't power off or wipe first.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Containment strategy (evidence preservation vs damage)"],
    },
    {
        "id": "cysa-ir-r2-010", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "multi",
        "stem": "Investigation confirms an attacker stole domain and service-account credentials. Which TWO "
                "actions most directly remove the attacker's stolen access? (Choose two.)",
        "options": [
            {"id": "A", "text": "Reset/rotate the affected account passwords and disable compromised accounts"},
            {"id": "B", "text": "Invalidate active sessions and tokens (and reset the Kerberos krbtgt where domain-wide compromise is suspected)"},
            {"id": "C", "text": "Change the company logo on the intranet"},
            {"id": "D", "text": "Defragment the domain controller's disk"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Resetting/rotating and disabling the compromised credentials removes the attacker's keys, and "
                       "invalidating live sessions/tokens (and krbtgt for domain-wide compromise) revokes access already granted with them.",
            "distractors": {
                "C": "Changing a logo has no security effect on stolen credentials.",
                "D": "Defragmenting the disk does not revoke any stolen access.",
            },
            "exam_pattern": "Stolen credentials = reset/rotate + disable accounts AND invalidate sessions/tokens (revoke access).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Eradication (credential reset/rotation, session invalidation)"],
    },
    {
        "id": "cysa-ir-r2-011", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "To cut off malware's command-and-control without immediately taking infected endpoints offline, "
                "the team redirects the known malicious C2 domains to a controlled internal address. What is this "
                "containment technique?",
        "options": [
            {"id": "A", "text": "A full-interruption disaster-recovery test"},
            {"id": "B", "text": "A write blocker"},
            {"id": "C", "text": "DNS sinkholing (blocking/redirecting C2 domains)"},
            {"id": "D", "text": "A tabletop exercise"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DNS sinkholing redirects malicious domains to a controlled address, severing the C2 channel and "
                       "letting responders identify infected hosts (which now beacon to the sinkhole) without taking endpoints down.",
            "distractors": {
                "A": "A full-interruption test halts systems to validate DR, not to block C2.",
                "B": "A write blocker is a forensic acquisition device, not a network control.",
                "D": "A tabletop is a discussion-based rehearsal, not an active containment control.",
            },
            "exam_pattern": "Redirect/block malicious C2 domains at DNS/egress to sever C2 = DNS sinkholing (containment).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Containment (DNS sinkhole / egress blocking of C2)"],
    },
    {
        "id": "cysa-ir-r2-012", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "During recovery, the team must restore a server from backup. The initial compromise is estimated "
                "to have occurred three weeks ago. Which backup should they restore from?",
        "options": [
            {"id": "A", "text": "The most recent nightly backup, taken last night"},
            {"id": "B", "text": "Any backup, since all backups are identical"},
            {"id": "C", "text": "No backup — restoration is unnecessary after a breach"},
            {"id": "D", "text": "A verified-clean backup taken before the estimated compromise date, after confirming it is free of attacker artifacts"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Restoration must use a known-good backup from before the compromise and verified clean; a "
                       "backup taken after the intrusion likely contains the attacker's implants and would reinfect the system.",
            "distractors": {
                "A": "Last night's backup is post-compromise and probably contains the attacker's persistence.",
                "B": "Backups differ over time; a post-compromise backup is tainted.",
                "C": "Restoring a clean state is a core recovery step after eradication.",
            },
            "exam_pattern": "Restore from a verified-clean backup predating the compromise; a post-compromise backup can reintroduce the threat.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 3.2 — Recovery (restore from known-good/clean backups)"],
    },

    # =====================================================================
    # DOMAIN 4.0 — REPORTING AND COMMUNICATION (10 items)
    # =====================================================================

    # ----- rc_vuln_reporting ---------------------------------------------
    {
        "id": "cysa-rc-r2-001", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A critical patch requires taking a 24/7 manufacturing line offline for three hours, which would "
                "stop production entirely. Which inhibitor to remediation does this represent?",
        "options": [
            {"id": "A", "text": "Business process interruption"},
            {"id": "B", "text": "Degrading functionality"},
            {"id": "C", "text": "Memorandum of understanding (MOU)"},
            {"id": "D", "text": "Proprietary system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The obstacle is the downtime needed to apply the fix, which halts operations — a business "
                       "process interruption. The patch itself works; the problem is the required outage.",
            "distractors": {
                "B": "Degrading functionality is when the fix itself breaks a needed feature; here the patch works but needs downtime.",
                "C": "An MOU is an inter-party agreement, not a downtime constraint.",
                "D": "Nothing indicates the system is vendor-closed; the blocker is the production outage.",
            },
            "exam_pattern": "Required downtime that halts operations = business process interruption (vs degrading functionality = the fix breaks a feature).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.1 — Inhibitors to remediation (business process interruption)"],
    },
    {
        "id": "cysa-rc-r2-002", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability sits on a 15-year-old application server running an unsupported OS the vendor no "
                "longer updates, and no compatible patch exists. Which inhibitor to remediation best describes the obstacle?",
        "options": [
            {"id": "A", "text": "Service-level agreement (SLA)"},
            {"id": "B", "text": "Legacy system"},
            {"id": "C", "text": "Business process interruption"},
            {"id": "D", "text": "Degrading functionality"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An aged, unsupported platform with no available patch is a legacy-system inhibitor; such systems "
                       "typically require compensating controls (isolation, monitoring) because they cannot be patched.",
            "distractors": {
                "A": "No contractual service level is described; the obstacle is the unsupported platform itself.",
                "C": "The blocker is the obsolete platform, not downtime needed to apply a fix.",
                "D": "No patch exists to break a feature; the system is simply too old/unsupported to patch.",
            },
            "exam_pattern": "Old, unsupported, unpatchable platform = legacy-system inhibitor (handle with compensating controls).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.1 — Inhibitors to remediation (legacy systems)"],
    },
    {
        "id": "cysa-rc-r2-003", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 3, "type": "mcq",
        "stem": "Leadership decides to defer remediating a medium-severity finding for six months. To report this "
                "responsibly, what should the vulnerability report include?",
        "options": [
            {"id": "A", "text": "Simply delete the finding from the report"},
            {"id": "B", "text": "Silently mark it 'fixed' to close it out"},
            {"id": "C", "text": "A documented, approved risk exception naming the risk owner, justification, compensating controls, and an expiration/review date"},
            {"id": "D", "text": "Raise the finding's CVSS score so it appears handled"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Deferred remediation is recorded as a formal, approved risk exception with an accountable owner, "
                       "justification, interim compensating controls, and a review/expiration date — preserving the audit trail and governance.",
            "distractors": {
                "A": "Deleting the finding hides real risk and breaks the audit trail.",
                "B": "Marking an open issue 'fixed' is false reporting.",
                "D": "Inflating the CVSS score does not record or govern the deferral decision.",
            },
            "exam_pattern": "Deferred remediation = documented, time-bound risk exception (owner, justification, compensating controls, expiration).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.1 — Vulnerability reporting (risk exceptions/acceptance documentation)"],
    },

    # ----- rc_incident_reporting -----------------------------------------
    {
        "id": "cysa-rc-r2-004", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A U.S. publicly traded company determines that a cybersecurity incident is material. Under the "
                "SEC cybersecurity disclosure rules, within what timeframe must it generally file a Form 8-K (Item 1.05)?",
        "options": [
            {"id": "A", "text": "Four business days after determining the incident is material"},
            {"id": "B", "text": "Within one hour of any security alert"},
            {"id": "C", "text": "Within 180 days of the incident"},
            {"id": "D", "text": "Only at the next annual 10-K filing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The SEC rule requires an Item 1.05 Form 8-K generally within four business days after the "
                       "registrant determines the incident is material (the clock starts at the materiality determination, not at discovery).",
            "distractors": {
                "B": "No SEC rule imposes a one-hour deadline, and the clock starts at the materiality determination, not any alert.",
                "C": "180 days far exceeds the four-business-day requirement.",
                "D": "Material incidents require a prompt 8-K, not waiting for the annual 10-K.",
            },
            "exam_pattern": "SEC material cyber incident → Form 8-K Item 1.05 within four business days of the materiality determination.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.2 — Legal/regulatory reporting (SEC Form 8-K Item 1.05)",
                       "SEC Release 33-11216 (Cybersecurity Disclosure)"],
    },
    {
        "id": "cysa-rc-r2-005", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A U.S. healthcare provider confirms a breach of unsecured protected health information (PHI) "
                "affecting 4,000 patients. Under the HIPAA Breach Notification Rule, affected individuals must be "
                "notified without unreasonable delay and no later than...",
        "options": [
            {"id": "A", "text": "24 hours after discovery"},
            {"id": "B", "text": "60 calendar days after discovery"},
            {"id": "C", "text": "2 years after discovery"},
            {"id": "D", "text": "Only after law enforcement closes its case"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "HIPAA requires notifying affected individuals without unreasonable delay and no later than 60 "
                       "calendar days from discovery of the breach; breaches affecting 500+ also require notifying HHS and the media.",
            "distractors": {
                "A": "HIPAA does not set a 24-hour individual-notification deadline; 60 days is the outer limit.",
                "C": "Two years far exceeds the 60-day requirement.",
                "D": "Notification cannot wait indefinitely on law enforcement; a limited delay may be requested, but the rule still applies.",
            },
            "exam_pattern": "HIPAA breach → notify individuals without unreasonable delay, at most 60 calendar days from discovery (500+ also notify HHS/media).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.2 — Legal/regulatory reporting (HIPAA Breach Notification Rule)",
                       "HHS — Breach Notification Rule (45 CFR 164.404)"],
    },
    {
        "id": "cysa-rc-r2-006", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "multi",
        "stem": "After a ransomware incident, an organization holds a cyber-insurance policy. Which TWO are valid "
                "reasons to notify the insurance carrier promptly? (Choose two.)",
        "options": [
            {"id": "A", "text": "Timely notice is often a condition of coverage under the policy"},
            {"id": "B", "text": "The insurer may require the use of approved incident-response/forensic vendors"},
            {"id": "C", "text": "The insurer will issue the company's public press release"},
            {"id": "D", "text": "Notifying the insurer removes the need for legal counsel"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Cyber policies commonly make prompt notification a condition of coverage, and insurers often "
                       "direct claimants to pre-approved IR/forensic/legal panel vendors — so the carrier is an important early stakeholder.",
            "distractors": {
                "C": "Public statements are handled by the organization's PR and legal teams, not the insurer.",
                "D": "Legal counsel is still required; the insurer does not replace it.",
            },
            "exam_pattern": "Notify the cyber-insurer promptly — coverage can depend on timely notice and insurers may mandate approved IR vendors.",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.2 — Incident reporting (stakeholder identification; third parties/insurer)"],
    },

    # ----- rc_metrics ----------------------------------------------------
    {
        "id": "cysa-rc-r2-007", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants a metric for the average time from detecting an incident to successfully containing "
                "it (stopping its spread). Which KPI is this?",
        "options": [
            {"id": "A", "text": "Mean time to contain (MTTC)"},
            {"id": "B", "text": "Mean time to detect (MTTD)"},
            {"id": "C", "text": "Scan coverage"},
            {"id": "D", "text": "Mean time between failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mean time to contain measures how quickly the team halts an incident's spread after detection; "
                       "it sits between detection and full remediation on the response timeline.",
            "distractors": {
                "B": "MTTD measures time until detection, which ends where MTTC begins.",
                "C": "Scan coverage measures how much of the estate is scanned, not containment speed.",
                "D": "MTBF is a hardware reliability metric, not an incident-response timing metric.",
            },
            "exam_pattern": "Detection → containment (spread stopped) = mean time to contain (MTTC).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.2 — Metrics and KPIs (MTTC vs MTTD/MTTR)"],
    },
    {
        "id": "cysa-rc-r2-008", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A SOC manager finds analysts are overwhelmed and wants a metric showing how many alerts turn out "
                "to be benign, so detections can be tuned. Which metric fits?",
        "options": [
            {"id": "A", "text": "Scan coverage"},
            {"id": "B", "text": "False-positive rate"},
            {"id": "C", "text": "Mean time to detect"},
            {"id": "D", "text": "Total asset inventory count"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The false-positive rate — the share of alerts that are benign — directly measures detection "
                       "quality and alert fatigue, guiding which rules to tune or suppress.",
            "distractors": {
                "A": "Scan coverage measures how much of the estate is scanned, not alert accuracy.",
                "C": "MTTD measures detection speed, not alert quality.",
                "D": "An asset count is inventory size, unrelated to alert accuracy.",
            },
            "exam_pattern": "Share of alerts that are benign = false-positive rate (drives detection tuning, reduces alert fatigue).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.2 — Metrics and KPIs (false-positive rate / detection quality)"],
    },

    # ----- rc_stakeholder_comm -------------------------------------------
    {
        "id": "cysa-rc-r2-009", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "Scans repeatedly reveal publicly exposed cloud storage buckets created through "
                "infrastructure-as-code (IaC) templates. Which team should the analyst collaborate with to fix the root cause?",
        "options": [
            {"id": "A", "text": "The physical facilities team"},
            {"id": "B", "text": "The accounts-payable team"},
            {"id": "C", "text": "The cloud/DevOps engineering team that owns the IaC templates and pipeline"},
            {"id": "D", "text": "The external media-relations team"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Because the exposure is generated by the IaC templates, fixing the templates and pipeline "
                       "guardrails with the cloud/DevOps team corrects the root cause and stops new buckets from being misconfigured.",
            "distractors": {
                "A": "Facilities manages buildings, not cloud configurations.",
                "B": "Accounts payable handles finances, not infrastructure-as-code.",
                "D": "Media relations handles external messaging, not cloud remediation.",
            },
            "exam_pattern": "Recurring cloud misconfiguration from IaC → collaborate with the cloud/DevOps team to fix the templates/pipeline (root cause).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.1 — Collaboration with internal teams (cloud/DevOps)"],
    },
    {
        "id": "cysa-rc-r2-010", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "An external auditor requests proof that the organization is meeting a regulatory requirement to "
                "remediate critical vulnerabilities on time. What should the security team provide?",
        "options": [
            {"id": "A", "text": "Raw, unexplained packet captures"},
            {"id": "B", "text": "The analysts' personal opinions with no supporting data"},
            {"id": "C", "text": "A copy of the attacker's malware sample"},
            {"id": "D", "text": "Reports mapping remediation evidence (scan results, timelines, documented exceptions) to the relevant compliance controls/requirements"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Auditors and regulators need evidence tied to the specific control/requirement: scan results, "
                       "remediation timelines against SLAs, and any documented exceptions, mapped to the applicable framework.",
            "distractors": {
                "A": "Raw packet captures do not demonstrate remediation compliance.",
                "B": "Unsupported opinions are not audit evidence.",
                "C": "Sharing a malware sample is inappropriate and does not prove compliance.",
            },
            "exam_pattern": "Audience = auditors/regulators → provide evidence mapped to the applicable controls/requirements (scan data, timelines, exceptions).",
        },
        "references": ["CompTIA CySA+ CS0-003 Objective 4.1/4.2 — Stakeholder communication (auditors/regulators; compliance evidence)"],
    },
]
