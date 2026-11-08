"""CompTIA CySA+ CS0-003 — Domain 1.0 Security Operations authored item pool.

Original, analyst-level practice items for CertLab's CySA+ track, mapped to the
public CS0-003 objectives (Domain 1.0, the heaviest domain at 33%). Items are
NEW scenarios written for this bank, never copied from any real exam.

build_content.py auto-discovers tools/content_cysa_*.py and shuffles the A/B/C/D
order per item (seeded by id), so the keyed answer below is not positionally
biased. CySA+ is analyst-level, so difficulty leans 2-3 (interpretation and
response, not rote definitions).

Subtopics covered (all five of Domain 1.0):
  so_system_network_analysis  — endpoint/network/log indicators, ports, baselines
  so_threat_intel             — TTPs, IOC vs IOA, Pyramid of Pain, ATT&CK, sharing
  so_threat_hunting           — hypothesis-driven hunts, TTP focus, detections
  so_malicious_activity       — scanning/C2/exfil, persistence, email, obfuscation
  so_tools_automation         — SIEM/SOAR/EDR, packet & email analysis, scripting
"""

QUESTIONS = [
    # ===== so_system_network_analysis ======================================
    {
        "id": "cysa-so-001", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Investigating a suspected macro attack, an analyst wants the full command line of "
                "every process launched on a Windows host. Which Security event ID should they review?",
        "options": [
            {"id": "A", "text": "4688 (a new process has been created)"},
            {"id": "B", "text": "4624 (an account was successfully logged on)"},
            {"id": "C", "text": "4663 (an attempt was made to access an object)"},
            {"id": "D", "text": "4720 (a user account was created)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 4688 logs process creation; with 'Include command line in process-creation "
                       "events' enabled it captures the full command line, exposing encoded or living-off-the-"
                       "land invocations.",
            "distractors": {
                "B": "4624 records a successful logon session, not process execution or its command line.",
                "C": "4663 records an attempt to access an object such as a file, not process creation.",
                "D": "4720 records creation of a user account, unrelated to spawned-process command lines.",
            },
            "exam_pattern": "Need the command line of spawned Windows processes = Event ID 4688 (with command-line auditing).",
        },
        "references": ["CS0-003 1.1 - Logging/endpoint telemetry (Windows Event IDs)"],
    },
    {
        "id": "cysa-so-002", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 1, "type": "mcq",
        "stem": "Reviewing an external scan, an analyst finds a company server accepting inbound "
                "connections from the internet on TCP 3389. Which exposed service creates this risk?",
        "options": [
            {"id": "A", "text": "Remote Desktop Protocol (RDP)"},
            {"id": "B", "text": "Secure Shell (SSH)"},
            {"id": "C", "text": "Server Message Block (SMB)"},
            {"id": "D", "text": "Domain Name System (DNS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TCP 3389 is RDP; exposing it to the internet invites credential brute-forcing and is a "
                       "common ransomware initial-access vector.",
            "distractors": {
                "B": "SSH listens on TCP 22, not 3389.",
                "C": "SMB uses TCP 445 (and legacy 139), not 3389.",
                "D": "DNS uses UDP/TCP 53, not 3389.",
            },
            "exam_pattern": "3389 = RDP; internet-exposed RDP is a top initial-access risk.",
        },
        "references": ["CS0-003 1.1 - Common ports and protocols"],
    },
    {
        "id": "cysa-so-003", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A workstation that normally uploads under 10 MB daily sends 4 GB over HTTPS to an "
                "unfamiliar host at 3 a.m. Which analytic approach best flags this as suspicious?",
        "options": [
            {"id": "A", "text": "Compare current flow volume against the host's established baseline"},
            {"id": "B", "text": "Verify the destination's TLS certificate is valid"},
            {"id": "C", "text": "Confirm the destination port is 443"},
            {"id": "D", "text": "Check that endpoint antivirus signatures are current"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anomaly detection compares observed behavior to a learned baseline; a large off-hours "
                       "transfer that deviates sharply from normal volume is a strong exfiltration indicator "
                       "regardless of the protocol used.",
            "distractors": {
                "B": "A valid certificate does not make a 400x volume spike to an unknown host benign; attackers use valid TLS.",
                "C": "Port 443 being 'expected' is exactly why exfiltration hides there; the port alone proves nothing.",
                "D": "Current AV signatures do nothing to explain anomalous data-egress volume.",
            },
            "exam_pattern": "Deviation from an established baseline (volume/time) = anomaly worth investigating, even over normal ports.",
        },
        "references": ["CS0-003 1.1 - Baselines and anomaly detection"],
    },
    {
        "id": "cysa-so-004", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "After an IOC is published, an analyst must find which internal hosts contacted a "
                "malicious IP over the past 30 days, but full packet storage is unavailable. Which source fits?",
        "options": [
            {"id": "A", "text": "NetFlow/flow records"},
            {"id": "B", "text": "Full packet captures"},
            {"id": "C", "text": "EDR memory dumps"},
            {"id": "D", "text": "Email gateway logs"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Flow records store compact connection metadata (source, destination, ports, bytes, "
                       "timestamps) at low storage cost, making them ideal for long-retention retrospective "
                       "lookups of who contacted a given IP.",
            "distractors": {
                "B": "Full packet capture is storage-heavy and rarely retained for 30 days; it is also unnecessary when only connection metadata is needed.",
                "C": "EDR memory dumps show host process state, not a month of network conversations.",
                "D": "Email gateway logs cover mail flow, not arbitrary IP-to-IP connections.",
            },
            "exam_pattern": "Historical 'who talked to this IP' with limited storage = NetFlow/flow data, not full pcap.",
        },
        "references": ["CS0-003 1.1 - Network telemetry (flow vs. full capture)"],
    },
    {
        "id": "cysa-so-005", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An EDR alert shows winword.exe spawning cmd.exe, which then launched powershell.exe. "
                "Which observation most strongly suggests a malicious document executed?",
        "options": [
            {"id": "A", "text": "The anomalous parent-child process lineage"},
            {"id": "B", "text": "The absolute path of powershell.exe"},
            {"id": "C", "text": "The size of the Word document"},
            {"id": "D", "text": "The user's group membership"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A productivity app such as Word spawning a shell and then PowerShell is an abnormal "
                       "process lineage characteristic of malicious macros; normal editing never creates that chain.",
            "distractors": {
                "B": "PowerShell's standard path is not itself suspicious; the spawning relationship is the indicator.",
                "C": "Document size does not indicate whether a macro executed.",
                "D": "Group membership affects privileges, not whether the process chain is anomalous.",
            },
            "exam_pattern": "Office app -> shell -> PowerShell lineage = malicious-macro behavior.",
        },
        "references": ["CS0-003 1.2 - Host indicators (process lineage)"],
    },
    {
        "id": "cysa-so-006", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "mcq",
        "stem": "While building an incident timeline, an analyst finds firewall, IDS, and server events "
                "appear out of order even though all were captured. What must be corrected to fix correlation?",
        "options": [
            {"id": "A", "text": "Clock/time synchronization across sources (NTP)"},
            {"id": "B", "text": "The SIEM dashboard's color scheme"},
            {"id": "C", "text": "The firewall's NAT rules"},
            {"id": "D", "text": "The analyst's search query syntax"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reliable cross-source correlation depends on synchronized clocks; without consistent NTP, "
                       "timestamps drift and events are sequenced incorrectly, corrupting the timeline.",
            "distractors": {
                "B": "Dashboard styling has no effect on event ordering.",
                "C": "NAT rules translate addresses; they do not alter log timestamps.",
                "D": "A query issue would not selectively reorder events that were captured correctly; skewed clocks would.",
            },
            "exam_pattern": "Events out of order across devices = time-synchronization (NTP) problem.",
        },
        "references": ["CS0-003 1.1 - Log correlation and time synchronization"],
    },
    {
        "id": "cysa-so-007", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 3, "type": "mcq",
        "stem": "Traffic to an external host uses TCP 443, but the payload does not follow TLS and "
                "resembles an interactive shell. Which technique best identifies the true protocol?",
        "options": [
            {"id": "A", "text": "Application-layer deep packet inspection"},
            {"id": "B", "text": "Trusting the port number to name the service"},
            {"id": "C", "text": "Reverse DNS lookup on the destination"},
            {"id": "D", "text": "Counting the number of packets exchanged"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Port numbers are only conventions; adversaries tunnel other protocols over 443 to blend in. "
                       "Deep packet inspection examines the actual payload structure to reveal the real application-layer protocol.",
            "distractors": {
                "B": "Mapping 443 to 'HTTPS' is exactly the assumption the attacker exploits; the port does not prove the protocol.",
                "C": "Reverse DNS names the host, not the protocol riding the connection.",
                "D": "Packet counts reveal volume, not protocol identity.",
            },
            "exam_pattern": "Payload does not match the port's expected protocol = inspect at the application layer (DPI); do not trust the port.",
        },
        "references": ["CS0-003 1.2 - Protocol analysis (port vs. payload)"],
    },
    {
        "id": "cysa-so-008", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 3, "type": "mcq",
        "stem": "To detect unauthorized persistence on a server, an analyst wants to know what changed "
                "since deployment. Which comparison most directly surfaces unexpected startup items?",
        "options": [
            {"id": "A", "text": "Diff current autoruns/services against the known-good gold-image baseline"},
            {"id": "B", "text": "Reboot the server and time how long boot takes"},
            {"id": "C", "text": "Confirm the operating-system license is activated"},
            {"id": "D", "text": "Read the server's physical asset tag"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Comparing current auto-start entries, services, and scheduled tasks against a trusted gold-image "
                       "baseline reveals additions an attacker made for persistence that would otherwise blend in.",
            "distractors": {
                "B": "Boot time is a crude metric and will not identify which startup entries were added.",
                "C": "License activation is unrelated to persistence artifacts.",
                "D": "An asset tag identifies hardware, not software changes.",
            },
            "exam_pattern": "Find unauthorized persistence = diff current configuration against a known-good baseline.",
        },
        "references": ["CS0-003 1.1 - Configuration baselines and integrity"],
    },
    {
        "id": "cysa-so-009", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_system_network_analysis", "difficulty": 2, "type": "multi",
        "stem": "An analyst is cataloging data sources and must label the host-based (endpoint) ones. "
                "Which TWO are endpoint telemetry sources rather than network telemetry? (Choose two.)",
        "options": [
            {"id": "A", "text": "Sysmon process-creation logs"},
            {"id": "B", "text": "The Windows Security event log"},
            {"id": "C", "text": "NetFlow records from a core router"},
            {"id": "D", "text": "Firewall allow/deny logs"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Sysmon and the Windows Security event log are generated on the endpoint and describe host "
                       "activity (process creation, logons), making them host/endpoint telemetry.",
            "distractors": {
                "C": "NetFlow is collected from network devices and describes conversations between hosts, not on-host activity.",
                "D": "Firewall logs are network telemetry recording perimeter traffic decisions, not endpoint events.",
            },
            "exam_pattern": "Host telemetry = generated ON the endpoint (Sysmon, Security log); network telemetry = flows, firewall, taps.",
        },
        "references": ["CS0-003 1.1 - Host vs. network telemetry sources"],
    },

    # ===== so_threat_intel =================================================
    {
        "id": "cysa-so-010", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants its detections to be the hardest for an adversary to evade. Per the Pyramid "
                "of Pain, detecting which indicator type is costliest for the adversary to change?",
        "options": [
            {"id": "A", "text": "TTPs (tactics, techniques, and procedures)"},
            {"id": "B", "text": "File hash values"},
            {"id": "C", "text": "IP addresses"},
            {"id": "D", "text": "Domain names"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In the Pyramid of Pain, TTPs sit at the apex; changing core behaviors forces the adversary "
                       "to retool and relearn, far harder than swapping a hash, IP, or domain.",
            "distractors": {
                "B": "Hashes sit at the bottom - trivial to change by altering a single byte.",
                "C": "Adversaries rotate IP addresses easily, so blocking them causes little pain.",
                "D": "Domains are cheap to register and rotate, causing only minor disruption.",
            },
            "exam_pattern": "Pyramid of Pain apex = TTPs; detecting behavior hurts adversaries most.",
        },
        "references": ["CS0-003 1.4 - Pyramid of Pain"],
    },
    {
        "id": "cysa-so-011", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 3, "type": "mcq",
        "stem": "A detection fires on the behavioral sequence of credential dumping followed by lateral "
                "movement, before any known-bad file is seen. Is this primarily an IOC or an IOA, and why?",
        "options": [
            {"id": "A", "text": "An IOA, because it detects adversary behavior/intent in progress"},
            {"id": "B", "text": "An IOC, because a known file hash matched"},
            {"id": "C", "text": "An IOA, because it simply lists a blocked IP address"},
            {"id": "D", "text": "An IOC, because it is a signature of previously seen malware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Indicators of attack describe adversary actions and intent (here, dumping credentials then "
                       "moving laterally) and can catch novel tooling, unlike static indicators of compromise.",
            "distractors": {
                "B": "No hash match is involved; the detection is behavioral, not a file artifact.",
                "C": "A blocked IP is a static IOC, not what fired here, and the scenario describes behavior.",
                "D": "A malware signature is an IOC; this detection is behavior-based and tool-agnostic.",
            },
            "exam_pattern": "Behavior/intent in progress = IOA; static artifact (hash/IP/domain) = IOC.",
        },
        "references": ["CS0-003 1.4 - Indicators of compromise vs. indicators of attack"],
    },
    {
        "id": "cysa-so-012", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 1, "type": "mcq",
        "stem": "A hospital wants to exchange vetted threat information with peer organizations in its own "
                "industry sector. Which type of body is purpose-built for this sharing?",
        "options": [
            {"id": "A", "text": "An ISAC (Information Sharing and Analysis Center)"},
            {"id": "B", "text": "A content delivery network (CDN) provider"},
            {"id": "C", "text": "A public certificate authority (CA)"},
            {"id": "D", "text": "A managed print service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ISACs are sector-specific communities (for example H-ISAC for health, FS-ISAC for finance) "
                       "that enable trusted sharing of threat intelligence among members of the same industry.",
            "distractors": {
                "B": "A CDN distributes web content; it is not a threat-sharing community.",
                "C": "A certificate authority issues digital certificates, unrelated to intel sharing.",
                "D": "A print service has no role in threat-intelligence exchange.",
            },
            "exam_pattern": "Sector-based trusted threat sharing = ISAC.",
        },
        "references": ["CS0-003 1.4 - Intelligence sharing (ISAC)"],
    },
    {
        "id": "cysa-so-013", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "An analyst maps observed activity to MITRE ATT&CK and files it under the Exfiltration "
                "tactic. In ATT&CK terms, what does the corresponding technique describe?",
        "options": [
            {"id": "A", "text": "The specific method used to achieve the tactic's goal"},
            {"id": "B", "text": "The adversary's overall strategic objective"},
            {"id": "C", "text": "The legal attribution of the actor"},
            {"id": "D", "text": "The monetary cost of the breach"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In ATT&CK a tactic is the adversary's goal (the 'why', e.g., Exfiltration) and a technique is "
                       "the 'how' - the specific method used to accomplish that goal, such as exfiltration over a C2 channel.",
            "distractors": {
                "B": "The overall goal is the tactic, not the technique.",
                "C": "ATT&CK catalogs behavior, not legal attribution.",
                "D": "Breach cost is a business-impact metric, not an ATT&CK technique.",
            },
            "exam_pattern": "ATT&CK: tactic = why/goal; technique = how/method.",
        },
        "references": ["CS0-003 1.4 - MITRE ATT&CK (tactics vs. techniques)"],
    },
    {
        "id": "cysa-so-014", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A CISO requests long-horizon analysis of adversary trends and motivations to guide "
                "multi-year security investment. Which category of threat intelligence best serves this?",
        "options": [
            {"id": "A", "text": "Strategic intelligence"},
            {"id": "B", "text": "Tactical intelligence"},
            {"id": "C", "text": "Technical indicators"},
            {"id": "D", "text": "Raw packet captures"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Strategic intelligence is high-level, largely non-technical analysis of trends, motivations, "
                       "and risk that informs executive decisions and long-term investment.",
            "distractors": {
                "B": "Tactical intelligence focuses on adversary TTPs for defenders and SOC operations, not executive strategy.",
                "C": "Technical indicators are atomic, short-lived artifacts for detection, not strategic planning.",
                "D": "Raw packet captures are operational data far below the strategic altitude a CISO needs.",
            },
            "exam_pattern": "Executive trends / long-term investment = strategic intel; SOC TTPs = tactical.",
        },
        "references": ["CS0-003 1.4 - Threat-intelligence levels (strategic/tactical/technical)"],
    },
    {
        "id": "cysa-so-015", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 3, "type": "mcq",
        "stem": "A single, unverified post on an open forum claims a named nation-state hit your industry. "
                "How should an analyst weight this before alerting leadership to the attribution?",
        "options": [
            {"id": "A", "text": "Assign low confidence and corroborate before attributing"},
            {"id": "B", "text": "Immediately attribute the activity to that nation-state"},
            {"id": "C", "text": "Discard all single-source reporting as useless"},
            {"id": "D", "text": "Raise the organization's threat level to maximum at once"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A lone uncorroborated open-source claim warrants low confidence; responsible analysis seeks "
                       "corroboration and avoids premature attribution, which can misdirect response and damage credibility.",
            "distractors": {
                "B": "Attributing from one unverified source is premature and risks acting on false information.",
                "C": "Single-source tips still have value as leads; they are triaged by confidence, not discarded outright.",
                "D": "Maxing the threat level on one unverified post is a disproportionate overreaction.",
            },
            "exam_pattern": "Uncorroborated single source = low confidence; corroborate before attributing.",
        },
        "references": ["CS0-003 1.4 - Confidence levels and attribution"],
    },
    {
        "id": "cysa-so-016", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "An intrusion shows months of stealthy dwell time, custom malware, and patient espionage "
                "against intellectual property. Which threat-actor profile does this best match?",
        "options": [
            {"id": "A", "text": "Nation-state / advanced persistent threat (APT)"},
            {"id": "B", "text": "Opportunistic script kiddie"},
            {"id": "C", "text": "Hacktivist seeking publicity"},
            {"id": "D", "text": "Accidental insider"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Long dwell time, custom tooling, heavy resourcing, and espionage goals are hallmarks of an "
                       "advanced persistent threat, typically nation-state sponsored.",
            "distractors": {
                "B": "Script kiddies use off-the-shelf tools opportunistically and lack the patience and custom capability shown.",
                "C": "Hacktivists seek visibility and disruption, not stealthy long-term espionage.",
                "D": "An accidental insider causes unintentional harm, not a sustained custom-malware campaign.",
            },
            "exam_pattern": "Stealth + persistence + custom tools + espionage = nation-state/APT.",
        },
        "references": ["CS0-003 1.4 - Threat actors and motivations"],
    },
    {
        "id": "cysa-so-017", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "multi",
        "stem": "A SOC wants to automate ingestion of a partner's machine-readable threat intelligence. "
                "Which TWO standards are designed specifically for expressing and exchanging CTI? (Choose two.)",
        "options": [
            {"id": "A", "text": "STIX"},
            {"id": "B", "text": "TAXII"},
            {"id": "C", "text": "SNMP"},
            {"id": "D", "text": "SMTP"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "STIX is the standardized language for representing threat intelligence, and TAXII is the "
                       "transport protocol for sharing STIX content between systems - together they enable automated CTI exchange.",
            "distractors": {
                "C": "SNMP manages and monitors network devices; it is not a CTI standard.",
                "D": "SMTP transports email, not structured threat intelligence.",
            },
            "exam_pattern": "Structured CTI exchange = STIX (language) + TAXII (transport).",
        },
        "references": ["CS0-003 1.4 - Intelligence standards (STIX/TAXII)"],
    },
    {
        "id": "cysa-so-018", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "An open threat feed keeps flagging IP addresses that were sinkholed months ago, generating "
                "false positives. Which intelligence quality issue does this illustrate?",
        "options": [
            {"id": "A", "text": "Poor timeliness / aging of indicators"},
            {"id": "B", "text": "Excessive data encryption"},
            {"id": "C", "text": "Insufficient network bandwidth"},
            {"id": "D", "text": "A broken TAXII transport"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Indicators have a limited useful life; feeds that fail to age out stale IOCs lose timeliness "
                       "and relevance, producing false positives on infrastructure that is no longer malicious.",
            "distractors": {
                "B": "Encryption strength has nothing to do with stale-indicator false positives.",
                "C": "Bandwidth does not affect whether an indicator is still current.",
                "D": "The feed is delivering data fine; the problem is indicator freshness, not transport.",
            },
            "exam_pattern": "Stale indicators causing false positives = timeliness/relevance (aging) problem.",
        },
        "references": ["CS0-003 1.4 - Intelligence quality (timeliness/relevance)"],
    },

    # ===== so_threat_hunting ===============================================
    {
        "id": "cysa-so-019", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A team proactively searches for undetected adversaries by forming and testing a specific "
                "assumption about attacker behavior, rather than waiting for alerts. What is this called?",
        "options": [
            {"id": "A", "text": "Hypothesis-driven threat hunting"},
            {"id": "B", "text": "Signature-based alerting"},
            {"id": "C", "text": "Vulnerability scanning"},
            {"id": "D", "text": "Patch management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat hunting is proactive and hypothesis-driven: the hunter states a testable assumption "
                       "(e.g., 'an adversary is using WMI for lateral movement') and investigates telemetry to prove or disprove it.",
            "distractors": {
                "B": "Signature-based alerting is reactive, firing only on known patterns - the opposite of proactive hunting.",
                "C": "Vulnerability scanning finds weaknesses, not active adversary behavior.",
                "D": "Patch management remediates vulnerabilities; it does not hunt for intruders.",
            },
            "exam_pattern": "Proactive + testable assumption about attacker behavior = hypothesis-driven hunting.",
        },
        "references": ["CS0-003 1.4 - Threat hunting (hypothesis-driven)"],
    },
    {
        "id": "cysa-so-020", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "When scoping a hunt, a team prioritizes adversary behaviors over lists of file hashes and "
                "IP addresses. Why is focusing on TTPs more durable?",
        "options": [
            {"id": "A", "text": "Behaviors are costlier for adversaries to change than atomic indicators"},
            {"id": "B", "text": "Behaviors are easier to paste into a blocklist"},
            {"id": "C", "text": "Hashes never change between malware builds"},
            {"id": "D", "text": "IP addresses uniquely identify an adversary forever"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TTPs reflect how adversaries operate and are expensive to alter, so detections built on behavior "
                       "remain effective even when the attacker swaps hashes, IPs, or domains.",
            "distractors": {
                "B": "Ease of blocklisting describes atomic IOCs, not the durability of behavioral detection.",
                "C": "Hashes change with every recompile or minor edit, making them fragile.",
                "D": "Adversaries rotate IPs constantly; an IP does not permanently identify anyone.",
            },
            "exam_pattern": "Hunt behaviors (TTPs) for lasting detections; IOCs are ephemeral.",
        },
        "references": ["CS0-003 1.4 - Threat hunting focus (TTPs over IOCs)"],
    },
    {
        "id": "cysa-so-021", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "A hunt lead wants to visualize which MITRE ATT&CK techniques the team can currently detect "
                "and where the blind spots are. Which approach fits best?",
        "options": [
            {"id": "A", "text": "Build an ATT&CK Navigator coverage heatmap of existing detections"},
            {"id": "B", "text": "Count the total alerts fired last month"},
            {"id": "C", "text": "Measure average CPU load on the SIEM"},
            {"id": "D", "text": "Tally the number of firewall rules"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mapping current detections onto an ATT&CK Navigator layer produces a coverage heatmap that "
                       "highlights which techniques are covered and which gaps warrant new hunts and analytics.",
            "distractors": {
                "B": "Raw alert counts say nothing about which techniques are or are not covered.",
                "C": "SIEM CPU load is an operational metric, not detection coverage.",
                "D": "Firewall rule counts do not map to adversary techniques or detection gaps.",
            },
            "exam_pattern": "Detection coverage/gaps across techniques = map to ATT&CK (Navigator heatmap).",
        },
        "references": ["CS0-003 1.4 - ATT&CK-driven hunting and coverage"],
    },
    {
        "id": "cysa-so-022", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A completed hunt finds no active compromise but reveals that a key lateral-movement "
                "technique was invisible to current tooling. What is the primary value delivered?",
        "options": [
            {"id": "A", "text": "A new detection/analytic closes a visibility gap"},
            {"id": "B", "text": "The hunt failed and should not be repeated"},
            {"id": "C", "text": "The environment is now permanently secure"},
            {"id": "D", "text": "No action is warranted since nothing was found"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hunt that finds nothing still delivers value by exposing visibility gaps; converting the hunt "
                       "logic into a durable detection improves future coverage even without an active incident.",
            "distractors": {
                "B": "Discovering a blind spot is a successful outcome, not a failure.",
                "C": "No single hunt makes an environment permanently secure; threats evolve.",
                "D": "Finding a visibility gap demands action - building the missing detection.",
            },
            "exam_pattern": "No compromise found but a gap exposed = turn the hunt into a new detection.",
        },
        "references": ["CS0-003 1.4 - Threat hunting (improving detections)"],
    },
    {
        "id": "cysa-so-023", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "While hunting, a team discovers forgotten internet-facing servers running unused services. "
                "Beyond detection, which hunt outcome does hardening or removing these represent?",
        "options": [
            {"id": "A", "text": "Reducing the organization's attack surface"},
            {"id": "B", "text": "Increasing adversary dwell time"},
            {"id": "C", "text": "Expanding the blast radius"},
            {"id": "D", "text": "Lowering log retention"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Identifying and decommissioning or hardening exposed, unnecessary services shrinks the attack "
                       "surface - an intended secondary benefit of proactive hunting.",
            "distractors": {
                "B": "Removing exposure reduces, not increases, the opportunity for dwell time.",
                "C": "Closing exposures shrinks the blast radius rather than expanding it.",
                "D": "Attack-surface reduction is unrelated to shortening log retention.",
            },
            "exam_pattern": "Hunt finds and removes needless exposure = attack-surface reduction.",
        },
        "references": ["CS0-003 1.4 - Threat hunting (attack-surface reduction)"],
    },
    {
        "id": "cysa-so-024", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A hunt program is founded on the premise that adversaries may already be inside and evading "
                "existing controls. Which mindset does this reflect?",
        "options": [
            {"id": "A", "text": "Assume-breach"},
            {"id": "B", "text": "Implicit trust"},
            {"id": "C", "text": "Security through obscurity"},
            {"id": "D", "text": "Default-allow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat hunting adopts an assume-breach posture: rather than trusting that controls kept everyone "
                       "out, hunters actively look for adversaries presumed to already be present.",
            "distractors": {
                "B": "Implicit trust is the opposite stance and undermines hunting.",
                "C": "Security through obscurity hides details; it is not a hunting premise.",
                "D": "Default-allow is a permissive access posture, not a hunting mindset.",
            },
            "exam_pattern": "Hunting presumes intruders are already present = assume-breach.",
        },
        "references": ["CS0-003 1.4 - Threat hunting (assume-breach)"],
    },
    {
        "id": "cysa-so-025", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "To find anomalies across thousands of endpoints, a hunter aggregates one data field and "
                "investigates its rarest values. Which analytic technique is being used?",
        "options": [
            {"id": "A", "text": "Frequency analysis (stacking / least-frequency of occurrence)"},
            {"id": "B", "text": "Signature matching"},
            {"id": "C", "text": "Full-disk encryption"},
            {"id": "D", "text": "Round-robin load balancing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Stacking counts how often each value occurs across hosts so the hunter can examine the long-tail "
                       "outliers - rare parent-child pairs or unusual binaries - that often reveal malicious activity.",
            "distractors": {
                "B": "Signature matching detects known patterns, not statistically rare outliers.",
                "C": "Full-disk encryption protects data at rest and is unrelated to analytics.",
                "D": "Load balancing distributes traffic; it is not a hunting technique.",
            },
            "exam_pattern": "Aggregate and investigate the rarest values = frequency analysis / stacking (LFO).",
        },
        "references": ["CS0-003 1.4 - Hunting techniques (stacking/frequency)"],
    },
    {
        "id": "cysa-so-026", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A new report details an APT's specific persistence and lateral-movement techniques against "
                "your sector. How should a hunt team best use it?",
        "options": [
            {"id": "A", "text": "Form a hypothesis that those TTPs are present and hunt for them"},
            {"id": "B", "text": "Immediately rebuild every server from scratch"},
            {"id": "C", "text": "Ignore it unless an alert fires"},
            {"id": "D", "text": "Block the entire internet at the firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fresh, relevant intelligence is an ideal seed for an intel-driven hunt: the team hypothesizes the "
                       "described TTPs may be present and searches telemetry for that specific behavior.",
            "distractors": {
                "B": "Rebuilding all servers is disproportionate and does not confirm whether the TTPs are present.",
                "C": "Waiting for an alert abandons the proactive value of the intelligence.",
                "D": "Blocking all internet access is operationally untenable and does not test the hypothesis.",
            },
            "exam_pattern": "Relevant CTI on actor TTPs = seed an intel-driven hunt hypothesis.",
        },
        "references": ["CS0-003 1.4 - Intel-driven threat hunting"],
    },
    {
        "id": "cysa-so-027", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_threat_hunting", "difficulty": 2, "type": "multi",
        "stem": "A hunt team is deciding what should inform a high-value, testable hypothesis. Which TWO "
                "inputs are the strongest sources? (Choose two.)",
        "options": [
            {"id": "A", "text": "Recent threat intel on an actor's TTPs targeting your sector"},
            {"id": "B", "text": "An unexplained deviation from your environment's baseline"},
            {"id": "C", "text": "A vendor's product marketing brochure"},
            {"id": "D", "text": "The calendar date of the next compliance audit"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Strong hypotheses are grounded in relevant adversary intelligence and in observed anomalies "
                       "against a known baseline - both point to concrete, testable behaviors to investigate.",
            "distractors": {
                "C": "Marketing material is promotional, not evidence of adversary behavior to hunt.",
                "D": "An audit date is a compliance milestone, not a basis for a behavioral hypothesis.",
            },
            "exam_pattern": "Good hunt hypotheses come from relevant CTI and baseline anomalies.",
        },
        "references": ["CS0-003 1.4 - Forming hunt hypotheses"],
    },

    # ===== so_malicious_activity ===========================================
    {
        "id": "cysa-so-028", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "A host connects to the same external IP every 60 seconds, each time sending a small, "
                "uniform payload, around the clock. Which malicious behavior does this most indicate?",
        "options": [
            {"id": "A", "text": "Command-and-control beaconing"},
            {"id": "B", "text": "A legitimate operating-system update check"},
            {"id": "C", "text": "Normal DNS resolution"},
            {"id": "D", "text": "A printer keep-alive on the LAN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Regular, periodic callbacks of uniform size to a single external host are classic C2 beaconing, "
                       "where an implant checks in with its controller on a fixed interval.",
            "distractors": {
                "B": "OS updates are intermittent and bursty, not a precise per-minute heartbeat to one IP.",
                "C": "DNS resolution targets resolvers with varied queries, not a fixed 60-second uniform callback.",
                "D": "Printer keep-alives stay on the LAN, not to an external IP around the clock.",
            },
            "exam_pattern": "Fixed-interval, uniform callbacks to one external host = C2 beaconing.",
        },
        "references": ["CS0-003 1.2 - Network indicators (C2/beaconing)"],
    },
    {
        "id": "cysa-so-029", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 1, "type": "mcq",
        "stem": "A single internal IP rapidly opens connections to hundreds of different ports across many "
                "hosts within seconds. Which activity does this most likely represent?",
        "options": [
            {"id": "A", "text": "Port/network scanning (reconnaissance)"},
            {"id": "B", "text": "A scheduled nightly backup"},
            {"id": "C", "text": "Routine time synchronization"},
            {"id": "D", "text": "A software license check"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "One source touching many ports and hosts in a short burst is the signature of a scan - "
                       "reconnaissance to enumerate reachable services, often preceding an attack.",
            "distractors": {
                "B": "Backups target specific storage endpoints, not a sweep across many ports and hosts.",
                "C": "Time sync contacts a few NTP servers on UDP 123, not hundreds of ports.",
                "D": "A license check contacts a specific vendor endpoint, not a broad port sweep.",
            },
            "exam_pattern": "One source -> many ports/hosts fast = scanning/recon.",
        },
        "references": ["CS0-003 1.2 - Network indicators (scanning)"],
    },
    {
        "id": "cysa-so-030", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "mcq",
        "stem": "An analyst sees a host issuing a high volume of DNS queries for long, random-looking "
                "subdomains of a single registered domain. Which technique is most consistent with this?",
        "options": [
            {"id": "A", "text": "DNS tunneling for exfiltration or C2"},
            {"id": "B", "text": "Normal content-delivery caching"},
            {"id": "C", "text": "NTP amplification"},
            {"id": "D", "text": "ARP spoofing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encoding data into long, high-entropy subdomain labels and sending many queries to one "
                       "authoritative domain is characteristic of DNS tunneling, used to exfiltrate data or carry C2 past egress filters.",
            "distractors": {
                "B": "CDN caching resolves normal hostnames; it does not produce floods of random high-entropy subdomains.",
                "C": "NTP amplification abuses UDP 123 reflection, not crafted DNS subdomains.",
                "D": "ARP spoofing manipulates layer-2 address mappings on the LAN, unrelated to DNS query content.",
            },
            "exam_pattern": "Many long/random subdomains of one domain = DNS tunneling (exfil/C2).",
        },
        "references": ["CS0-003 1.2 - Network indicators (DNS tunneling/exfiltration)"],
    },
    {
        "id": "cysa-so-031", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "After eradicating malware, an analyst wants to ensure it will not relaunch at logon. Which "
                "host artifact is a common persistence mechanism to inspect first?",
        "options": [
            {"id": "A", "text": "A Run/RunOnce registry key or a new scheduled task"},
            {"id": "B", "text": "The desktop wallpaper setting"},
            {"id": "C", "text": "The display resolution"},
            {"id": "D", "text": "The recycle-bin size limit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Autostart locations such as the Run/RunOnce registry keys and scheduled tasks are frequent "
                       "persistence mechanisms that relaunch malware at logon or on a trigger and must be checked during eradication.",
            "distractors": {
                "B": "Wallpaper settings do not execute code at startup.",
                "C": "Display resolution has no bearing on program persistence.",
                "D": "Recycle-bin size does not relaunch software.",
            },
            "exam_pattern": "Relaunch-at-logon persistence = Run keys, scheduled tasks, services, startup folder.",
        },
        "references": ["CS0-003 1.2 - Host indicators (persistence)"],
    },
    {
        "id": "cysa-so-032", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "mcq",
        "stem": "A spoofed message passed SPF checks yet DMARC still failed. Which explanation best "
                "accounts for this outcome?",
        "options": [
            {"id": "A", "text": "SPF authenticated the envelope domain, which did not align with the From-header domain"},
            {"id": "B", "text": "DMARC requires the message to be encrypted in transit with TLS"},
            {"id": "C", "text": "SPF and DMARC are the same check, so the result is contradictory"},
            {"id": "D", "text": "DMARC failed only because the message had no attachments"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DMARC requires SPF or DKIM to pass AND to align with the visible From domain. A message can pass "
                       "SPF on its envelope (Return-Path) domain yet fail DMARC when that domain does not align with the spoofed From header.",
            "distractors": {
                "B": "DMARC concerns authentication and identifier alignment, not transport encryption such as STARTTLS.",
                "C": "SPF validates the sending IP/envelope while DMARC adds alignment and policy - distinct checks, so the result is not contradictory.",
                "D": "Attachments have no bearing on DMARC evaluation.",
            },
            "exam_pattern": "SPF pass but DMARC fail = identifier-alignment failure with the From domain.",
        },
        "references": ["CS0-003 1.2 - Email indicators (SPF/DKIM/DMARC)"],
    },
    {
        "id": "cysa-so-033", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "Triaging a suspected phish, an analyst compares the message headers. Which finding most "
                "strongly supports a spoofing attempt?",
        "options": [
            {"id": "A", "text": "The From domain differs from the Return-Path, and Reply-To points to an unrelated address"},
            {"id": "B", "text": "The message contains an image attachment"},
            {"id": "C", "text": "The subject line is written in all capitals"},
            {"id": "D", "text": "The email arrived during business hours"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A mismatch between the displayed From domain and the Return-Path, combined with a Reply-To that "
                       "redirects responses to an unrelated attacker-controlled address, is a hallmark of spoofing.",
            "distractors": {
                "B": "Image attachments are common in legitimate mail and are not themselves proof of spoofing.",
                "C": "A capitalized subject may signal spam tone but does not evidence header spoofing.",
                "D": "Delivery timing does not indicate forgery.",
            },
            "exam_pattern": "From vs. Return-Path mismatch plus a suspicious Reply-To = spoofing indicators.",
        },
        "references": ["CS0-003 1.2 - Email header analysis"],
    },
    {
        "id": "cysa-so-034", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 2, "type": "mcq",
        "stem": "An analyst finds a process launched as 'powershell.exe -nop -w hidden -enc <long Base64 "
                "string>'. Which adversary technique does the -enc argument indicate?",
        "options": [
            {"id": "A", "text": "Command obfuscation / defense evasion via a Base64-encoded command"},
            {"id": "B", "text": "Full-disk encryption of the host"},
            {"id": "C", "text": "TLS certificate pinning"},
            {"id": "D", "text": "Secure password hashing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The -EncodedCommand (-enc) switch runs a Base64-encoded command, which attackers use to obscure "
                       "intent and evade simple string-based detection - an obfuscation/defense-evasion technique.",
            "distractors": {
                "B": "This encodes a command string, not the disk; no volume encryption is involved.",
                "C": "Certificate pinning validates TLS endpoints and is unrelated to PowerShell arguments.",
                "D": "Password hashing protects credentials at rest, not command content passed to PowerShell.",
            },
            "exam_pattern": "powershell -enc <Base64> = obfuscated command (defense evasion).",
        },
        "references": ["CS0-003 1.2 - Obfuscation and defense evasion"],
    },
    {
        "id": "cysa-so-035", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "mcq",
        "stem": "An EDR shows a process named svchost.exe running from C:\\Users\\Public\\ and not spawned "
                "by services.exe. Which malicious technique best explains this?",
        "options": [
            {"id": "A", "text": "Masquerading as a legitimate system process"},
            {"id": "B", "text": "A normal Windows service start"},
            {"id": "C", "text": "A routine certificate renewal"},
            {"id": "D", "text": "A standard user-profile sync"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Genuine svchost.exe runs from System32 and is started by services.exe; a same-named binary "
                       "executing from a user-writable path with the wrong parent is masquerading to blend in with trusted processes.",
            "distractors": {
                "B": "A normal service start originates from System32 under services.exe, not a public user folder.",
                "C": "Certificate renewal does not spawn a mislocated svchost.exe.",
                "D": "Profile sync does not run system-process names from user-writable directories.",
            },
            "exam_pattern": "Legit process name in the wrong path / with the wrong parent = masquerading.",
        },
        "references": ["CS0-003 1.2 - Host indicators (masquerading)"],
    },
    {
        "id": "cysa-so-036", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_malicious_activity", "difficulty": 3, "type": "multi",
        "stem": "An analyst reviews a host where built-in Windows tools were abused to download and run a "
                "payload while evading detection. Which TWO are commonly abused living-off-the-land binaries? (Choose two.)",
        "options": [
            {"id": "A", "text": "certutil.exe"},
            {"id": "B", "text": "mshta.exe"},
            {"id": "C", "text": "notepad.exe"},
            {"id": "D", "text": "winver.exe"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "certutil.exe can download and decode files, and mshta.exe can execute remote HTA/script content; "
                       "both are legitimate signed binaries attackers abuse to operate without dropping obvious malware.",
            "distractors": {
                "C": "notepad.exe is a text editor with no download or script-execution capability to abuse this way.",
                "D": "winver.exe merely displays the Windows version and cannot fetch or run payloads.",
            },
            "exam_pattern": "Signed built-ins abused to download/execute (certutil, mshta, rundll32, regsvr32) = LOLBins.",
        },
        "references": ["CS0-003 1.2 - Living-off-the-land / abused utilities"],
    },

    # ===== so_tools_automation =============================================
    {
        "id": "cysa-so-037", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 1, "type": "mcq",
        "stem": "A team needs one platform to aggregate logs from firewalls, servers, and endpoints and "
                "correlate them to detect multi-stage attacks. Which tool category fits?",
        "options": [
            {"id": "A", "text": "SIEM"},
            {"id": "B", "text": "A label printer"},
            {"id": "C", "text": "A password vault"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM centralizes and normalizes logs from many sources and applies correlation rules to "
                       "surface multi-stage activity that individual devices would miss in isolation.",
            "distractors": {
                "B": "A label printer produces physical labels and has no log-analysis function.",
                "C": "A password vault stores secrets; it does not correlate security events.",
                "D": "A load balancer distributes traffic and does not perform cross-source correlation.",
            },
            "exam_pattern": "Aggregate + correlate logs from many sources = SIEM.",
        },
        "references": ["CS0-003 1.3 - SIEM (correlation)"],
    },
    {
        "id": "cysa-so-038", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "After a SIEM detects phishing, leadership wants containment steps - enrich the IOC, open a "
                "ticket, and isolate the host - to run automatically via a playbook. Which capability provides this?",
        "options": [
            {"id": "A", "text": "SOAR"},
            {"id": "B", "text": "A SIEM dashboard widget"},
            {"id": "C", "text": "A syslog collector"},
            {"id": "D", "text": "A packet broker"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SOAR adds orchestration and automation: playbooks execute response actions (enrichment, "
                       "ticketing, host isolation) automatically, extending the SIEM's detection with action.",
            "distractors": {
                "B": "A dashboard visualizes data; it does not execute automated response playbooks.",
                "C": "A syslog collector forwards logs; it does not orchestrate response.",
                "D": "A packet broker distributes traffic to tools and performs no response automation.",
            },
            "exam_pattern": "Automated response playbooks after detection = SOAR (SIEM detects, SOAR acts).",
        },
        "references": ["CS0-003 1.5 - SOAR / orchestration"],
    },
    {
        "id": "cysa-so-039", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "An analyst must remotely isolate a compromised laptop and kill a malicious process based on "
                "its behavior, not just a signature. Which tool provides this on the endpoint?",
        "options": [
            {"id": "A", "text": "EDR (endpoint detection and response)"},
            {"id": "B", "text": "A network tap"},
            {"id": "C", "text": "A DHCP server"},
            {"id": "D", "text": "A spam filter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR continuously monitors endpoint behavior, detects suspicious activity, and supports response "
                       "actions such as isolating the host and terminating processes remotely.",
            "distractors": {
                "B": "A network tap copies traffic for inspection but cannot act on an endpoint.",
                "C": "A DHCP server assigns IP addresses; it has no endpoint-response role.",
                "D": "A spam filter screens email and cannot isolate a host or kill a process.",
            },
            "exam_pattern": "Behavioral endpoint detection + remote isolate/kill = EDR.",
        },
        "references": ["CS0-003 1.3 - Endpoint security (EDR)"],
    },
    {
        "id": "cysa-so-040", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "An analyst has a packet capture and needs to reassemble a TCP conversation to confirm "
                "credentials were sent in cleartext. Which tool and feature fit best?",
        "options": [
            {"id": "A", "text": "Wireshark's Follow TCP Stream"},
            {"id": "B", "text": "Starting a fresh Wireshark capture on a new interface"},
            {"id": "C", "text": "tcpdump with no filter printing to the console"},
            {"id": "D", "text": "A SIEM correlation rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Wireshark's Follow TCP Stream reassembles a flow's payload into a readable transcript, letting "
                       "the analyst confirm whether credentials traversed the network unencrypted.",
            "distractors": {
                "B": "Starting a new capture does not analyze the existing pcap that already contains the conversation.",
                "C": "tcpdump streaming raw packets to the console is poorly suited to reassembling and reading an application-layer transcript.",
                "D": "A SIEM rule correlates log events, not packet payloads inside a capture file.",
            },
            "exam_pattern": "Reassemble/read a conversation's payload from a pcap = Wireshark Follow TCP Stream.",
        },
        "references": ["CS0-003 1.3 - Packet analysis (Wireshark)"],
    },
    {
        "id": "cysa-so-041", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 3, "type": "mcq",
        "stem": "On a headless Linux server, an analyst must capture only traffic to host 10.0.0.5 on port "
                "443 and save it for later analysis. Which approach is appropriate?",
        "options": [
            {"id": "A", "text": "Run tcpdump with a filter 'host 10.0.0.5 and port 443', writing to a pcap file"},
            {"id": "B", "text": "Open Wireshark's GUI on the server console"},
            {"id": "C", "text": "Disable the server's NIC to force a capture"},
            {"id": "D", "text": "Run a full port scan of 10.0.0.5"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "tcpdump is the right CLI tool for a headless host; a Berkeley Packet Filter ('host 10.0.0.5 and "
                       "port 443') limits capture to the traffic of interest, and -w writes it to a pcap for later analysis.",
            "distractors": {
                "B": "A headless server has no GUI, so launching Wireshark's interface there is not viable.",
                "C": "Disabling the NIC stops traffic entirely, preventing any capture.",
                "D": "A port scan generates traffic and enumerates services; it does not capture the existing conversation.",
            },
            "exam_pattern": "Headless, filtered capture to a file = tcpdump with a BPF filter and -w.",
        },
        "references": ["CS0-003 1.3 - Packet capture (tcpdump/BPF)"],
    },
    {
        "id": "cysa-so-042", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "A SOC automates tier-1 phishing triage with a playbook. Which benefit most directly results "
                "from replacing the manual, repetitive steps?",
        "options": [
            {"id": "A", "text": "Faster, more consistent response with fewer human errors"},
            {"id": "B", "text": "Guaranteed elimination of all false positives"},
            {"id": "C", "text": "No further need for any analysts"},
            {"id": "D", "text": "Automatic repeal of all security policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation executes repetitive steps quickly and identically every time, lowering mean time to "
                       "respond and reducing the human errors that creep into manual, high-volume work.",
            "distractors": {
                "B": "Automation speeds and standardizes triage but does not eliminate false positives, which stem from detection logic.",
                "C": "Automation augments analysts for higher-value work; it does not remove the need for human judgment.",
                "D": "Automation enforces process; it does not repeal security policy.",
            },
            "exam_pattern": "Automation benefits = speed, consistency, fewer errors (lower MTTR).",
        },
        "references": ["CS0-003 1.5 - Benefits of automation/orchestration"],
    },
    {
        "id": "cysa-so-043", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "mcq",
        "stem": "An analyst must check 500 file hashes against a threat-intel API and summarize the hits. "
                "Which approach is most efficient and repeatable?",
        "options": [
            {"id": "A", "text": "Write a script that queries the API and parses the results programmatically"},
            {"id": "B", "text": "Paste each hash into a web form by hand"},
            {"id": "C", "text": "Email the list to the vendor and wait for a reply"},
            {"id": "D", "text": "Reboot the SIEM to refresh its cache"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scripting (for example Python calling the API) automates the bulk lookups and result parsing, "
                       "delivering a fast, consistent, repeatable process that manual effort cannot match at that volume.",
            "distractors": {
                "B": "Manually submitting 500 hashes is slow, error-prone, and not repeatable.",
                "C": "Emailing the vendor introduces delay and provides no structured, immediate result.",
                "D": "Rebooting the SIEM does nothing to enrich external hash reputation.",
            },
            "exam_pattern": "Repetitive bulk enrichment at scale = script against the API.",
        },
        "references": ["CS0-003 1.3 - Scripting/automation for analysis"],
    },
    {
        "id": "cysa-so-044", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 3, "type": "mcq",
        "stem": "A correlation rule floods analysts with alerts from a known-good vulnerability scanner, "
                "causing alert fatigue. Which tuning action best reduces noise without hiding real threats?",
        "options": [
            {"id": "A", "text": "Allow-list the scanner's source and refine the rule's logic/thresholds"},
            {"id": "B", "text": "Disable all logging on the affected sensors"},
            {"id": "C", "text": "Delete the SIEM's correlation engine"},
            {"id": "D", "text": "Raise every rule's severity to critical"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tuning - allow-listing the authorized scanner and tightening rule conditions or thresholds - "
                       "removes predictable benign noise while preserving detection of genuine anomalies.",
            "distractors": {
                "B": "Disabling logging creates blind spots and destroys the evidence trail.",
                "C": "Removing the correlation engine eliminates detection entirely, not just the noise.",
                "D": "Escalating every rule to critical worsens fatigue and buries true positives.",
            },
            "exam_pattern": "Benign source flooding alerts = tune/allow-list that source; do not kill logging.",
        },
        "references": ["CS0-003 1.5 - Tuning / reducing false positives"],
    },
    {
        "id": "cysa-so-045", "exam": "cysa", "domain": "cysa_security_operations",
        "subtopic": "so_tools_automation", "difficulty": 2, "type": "multi",
        "stem": "An analyst received a suspicious attachment and must examine it without endangering the "
                "environment. Which TWO actions are appropriate? (Choose two.)",
        "options": [
            {"id": "A", "text": "Detonate it in an isolated sandbox"},
            {"id": "B", "text": "Compute its hash and check reputation/threat intel"},
            {"id": "C", "text": "Open it on the analyst's own workstation to see what it does"},
            {"id": "D", "text": "Forward it to all staff as a warning with the file attached"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Detonating the file in an isolated sandbox reveals its behavior safely, and hashing it for a "
                       "reputation/threat-intel lookup identifies known-malicious files - both contain risk while yielding intelligence.",
            "distractors": {
                "C": "Opening it on a production workstation risks executing the very malware under investigation.",
                "D": "Forwarding the live attachment to all staff spreads the threat and invites accidental execution.",
            },
            "exam_pattern": "Analyze suspect files safely = sandbox detonation + hash/reputation lookup; never open live.",
        },
        "references": ["CS0-003 1.3 - Email/malware analysis (sandboxing)"],
    },
]
