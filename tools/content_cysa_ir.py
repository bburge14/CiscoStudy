"""CompTIA CySA+ (CS0-003) — Domain 3.0: Incident Response and Management (20%).

Original, objective-aligned practice items (never real or memorized exam items),
written at analyst depth: what to DO at each step of the incident lifecycle.
Facts are limited to well-established, current CS0-003 content (NIST SP 800-61
lifecycle, Lockheed Martin Cyber Kill Chain, the Diamond Model, and MITRE ATT&CK).
build_content.py shuffles option order (seeded by question id), so the keyed
answer below is not positionally biased.

Subtopics covered (all three):
  - ir_lifecycle          : IR phases/process, playbooks, team roles (RACI),
                            communication plan, and attack frameworks
                            (Cyber Kill Chain, Diamond Model, MITRE ATT&CK).
  - ir_detection_analysis : validating/scoping alerts, impact, evidence sources
                            (logs, EDR, packet capture), order of volatility,
                            chain of custody, evidence acquisition/forensics.
  - ir_containment_recovery : containment (short/long-term, isolation/segmentation),
                            eradication, recovery (restore/validate/monitor), and
                            post-incident activity (root cause, lessons learned).
"""

QUESTIONS = [
    # ===== ir_lifecycle =====================================================
    {
        "id": "cysa-ir-001", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 1, "type": "mcq",
        "stem": "A security program follows the NIST SP 800-61 incident response life cycle. "
                "Which phase comes immediately AFTER Detection and Analysis?",
        "options": [
            {"id": "A", "text": "Containment, Eradication, and Recovery"},
            {"id": "B", "text": "Preparation"},
            {"id": "C", "text": "Post-Incident Activity"},
            {"id": "D", "text": "Weaponization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The NIST order is Preparation -> Detection and Analysis -> Containment, "
                       "Eradication, and Recovery -> Post-Incident Activity, so Containment "
                       "follows Detection and Analysis.",
            "distractors": {
                "B": "Preparation is the first phase and precedes detection, not follows it.",
                "C": "Post-Incident Activity is the final phase, after recovery -- not right after detection.",
                "D": "Weaponization is a Cyber Kill Chain stage, not a NIST life-cycle phase.",
            },
            "exam_pattern": "Know the four NIST phases in order; the phase after detection is containment/eradication/recovery.",
        },
        "references": ["CS0-003 3.3 -- Incident response life cycle (NIST SP 800-61)"],
    },
    {
        "id": "cysa-ir-002", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Before any incident occurs, a SOC lead wants responders to have repeatable, step-by-step "
                "procedures for specific attack types such as ransomware. Which artifact provides this?",
        "options": [
            {"id": "A", "text": "An incident response playbook (runbook)"},
            {"id": "B", "text": "A chain-of-custody form"},
            {"id": "C", "text": "An after-action report"},
            {"id": "D", "text": "A memorandum of understanding (MOU)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Playbooks/runbooks are built during preparation and give responders repeatable, "
                       "step-by-step procedures tailored to a specific incident type like ransomware.",
            "distractors": {
                "B": "A chain-of-custody form tracks evidence handling during an investigation, not response steps.",
                "C": "An after-action report is produced after an incident, not prepared in advance as procedure.",
                "D": "An MOU is an agreement between parties; it does not define response steps.",
            },
            "exam_pattern": "Prebuilt, per-incident-type, step-by-step procedures = playbook/runbook.",
        },
        "references": ["CS0-003 3.3 -- Preparation phase: playbooks/runbooks"],
    },
    {
        "id": "cysa-ir-003", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An incident response plan assigns duties with a RACI matrix. Which statement best "
                "describes the person designated 'Accountable' for a response task?",
        "options": [
            {"id": "A", "text": "They are ultimately answerable for the outcome and approve its completion"},
            {"id": "B", "text": "They perform the hands-on work of the task"},
            {"id": "C", "text": "They are kept informed of progress after decisions are made"},
            {"id": "D", "text": "They provide input and are consulted before the task is done"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In RACI, the Accountable role is the single person ultimately answerable for the "
                       "outcome who signs off on completion; ideally exactly one person is Accountable per task.",
            "distractors": {
                "B": "Doing the hands-on work describes the Responsible role.",
                "C": "Being kept up to date one-way describes the Informed role.",
                "D": "Providing two-way input describes the Consulted role.",
            },
            "exam_pattern": "RACI = Responsible (does), Accountable (owns/approves), Consulted (input), Informed (updated).",
        },
        "references": ["CS0-003 3.3 -- Incident response team roles (RACI)"],
    },
    {
        "id": "cysa-ir-004", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Attackers have compromised the corporate email system during an active breach. Why should "
                "the IR team's communication plan include an out-of-band channel?",
        "options": [
            {"id": "A", "text": "So responders can coordinate without the attacker reading their messages"},
            {"id": "B", "text": "To speed up email delivery during the incident"},
            {"id": "C", "text": "To satisfy encryption-at-rest requirements for mail"},
            {"id": "D", "text": "To lower the monetary cost of incident communications"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Out-of-band channels (phone, a separate secure messenger) keep response coordination "
                       "private when the primary channel may be monitored by the adversary.",
            "distractors": {
                "B": "The goal is confidentiality of coordination, not faster email.",
                "C": "Out-of-band comms address secure coordination, not mail encryption-at-rest compliance.",
                "D": "Cost is not the driver; preventing adversary eavesdropping is.",
            },
            "exam_pattern": "Primary comms possibly compromised -> use out-of-band so attackers cannot monitor the response.",
        },
        "references": ["CS0-003 3.3 -- Preparation: incident response communication plan"],
    },
    {
        "id": "cysa-ir-005", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Malware on an infected host repeatedly beacons to an external server to receive attacker "
                "instructions. Which Lockheed Martin Cyber Kill Chain phase does this represent?",
        "options": [
            {"id": "A", "text": "Command and Control (C2)"},
            {"id": "B", "text": "Weaponization"},
            {"id": "C", "text": "Reconnaissance"},
            {"id": "D", "text": "Delivery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Beaconing to receive attacker instructions is Command and Control -- the adversary "
                       "establishes a channel to remotely control the compromised host.",
            "distractors": {
                "B": "Weaponization couples an exploit with a payload before delivery; nothing is communicating yet.",
                "C": "Reconnaissance is researching the target before any compromise.",
                "D": "Delivery transmits the weapon to the victim (e.g., a phishing email), not the post-infection channel.",
            },
            "exam_pattern": "Beaconing / receiving commands from an attacker server = Command and Control.",
        },
        "references": ["CS0-003 3.1 -- Attack frameworks: Cyber Kill Chain"],
    },
    {
        "id": "cysa-ir-006", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A defender wants to disrupt an intrusion as early as possible. Among these Cyber Kill "
                "Chain phases, which one occurs earliest?",
        "options": [
            {"id": "A", "text": "Reconnaissance"},
            {"id": "B", "text": "Exploitation"},
            {"id": "C", "text": "Installation"},
            {"id": "D", "text": "Actions on Objectives"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reconnaissance is the first kill-chain phase (gathering target information); disrupting "
                       "earlier phases stops the attack before deeper compromise.",
            "distractors": {
                "B": "Exploitation is phase 4, after reconnaissance, weaponization, and delivery.",
                "C": "Installation is phase 5, after exploitation.",
                "D": "Actions on Objectives is the final phase of the chain.",
            },
            "exam_pattern": "Kill-chain order: Recon -> Weaponize -> Deliver -> Exploit -> Install -> C2 -> Actions on Objectives.",
        },
        "references": ["CS0-003 3.1 -- Attack frameworks: Cyber Kill Chain"],
    },
    {
        "id": "cysa-ir-007", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 3, "type": "mcq",
        "stem": "An analyst documents an intrusion by mapping the adversary, their capability, the "
                "infrastructure used, and the victim. Which framework uses these four core features?",
        "options": [
            {"id": "A", "text": "Diamond Model of Intrusion Analysis"},
            {"id": "B", "text": "Lockheed Martin Cyber Kill Chain"},
            {"id": "C", "text": "MITRE ATT&CK"},
            {"id": "D", "text": "OWASP Top 10"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Diamond Model's four core features -- adversary, capability, infrastructure, and "
                       "victim -- are linked to analyze a single intrusion event.",
            "distractors": {
                "B": "The Cyber Kill Chain describes sequential attack phases, not these four vertices.",
                "C": "ATT&CK catalogs adversary tactics and techniques, not the adversary/capability/infrastructure/victim diamond.",
                "D": "The OWASP Top 10 ranks web application risks, unrelated to intrusion-analysis vertices.",
            },
            "exam_pattern": "Adversary + Capability + Infrastructure + Victim = Diamond Model.",
        },
        "references": ["CS0-003 3.1 -- Attack frameworks: Diamond Model of Intrusion Analysis"],
    },
    {
        "id": "cysa-ir-008", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A threat-intel team wants a standardized, real-world catalog of adversary tactics and "
                "techniques to map observed attacker behavior. Which resource best fits?",
        "options": [
            {"id": "A", "text": "MITRE ATT&CK"},
            {"id": "B", "text": "The Diamond Model"},
            {"id": "C", "text": "NIST SP 800-61"},
            {"id": "D", "text": "A RACI chart"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MITRE ATT&CK is a curated knowledge base of adversary tactics, techniques, and "
                       "procedures (TTPs) drawn from real-world observations, ideal for mapping behavior.",
            "distractors": {
                "B": "The Diamond Model frames a single intrusion's four features; it is not a TTP catalog.",
                "C": "NIST SP 800-61 defines the IR life cycle, not an adversary-technique catalog.",
                "D": "A RACI chart assigns responsibility roles, not attacker techniques.",
            },
            "exam_pattern": "Catalog/matrix of adversary TTPs from real-world observation = MITRE ATT&CK.",
        },
        "references": ["CS0-003 3.1 -- Attack frameworks: MITRE ATT&CK"],
    },
    {
        "id": "cysa-ir-009", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 3, "type": "multi",
        "stem": "In MITRE ATT&CK, a tactic represents the adversary's goal (the 'why'). Select the TWO "
                "items below that are tactics rather than specific techniques.",
        "options": [
            {"id": "A", "text": "Persistence"},
            {"id": "B", "text": "Lateral Movement"},
            {"id": "C", "text": "Spearphishing attachment"},
            {"id": "D", "text": "Pass-the-hash"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Persistence and Lateral Movement are ATT&CK tactics -- high-level categories that "
                       "represent the adversary's goal (the 'why').",
            "distractors": {
                "C": "Spearphishing attachment is a specific technique (a 'how') under the Initial Access tactic.",
                "D": "Pass-the-hash is a specific attacker technique, not one of the high-level tactic categories.",
            },
            "exam_pattern": "Tactic = the goal (why); technique = the method (how).",
        },
        "references": ["CS0-003 3.1 -- MITRE ATT&CK tactics and techniques"],
    },
    {
        "id": "cysa-ir-010", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "To validate its incident response plan without disrupting production, a company gathers "
                "stakeholders to talk through a simulated ransomware scenario. What is this activity called?",
        "options": [
            {"id": "A", "text": "A tabletop exercise"},
            {"id": "B", "text": "A penetration test"},
            {"id": "C", "text": "A full-interruption test"},
            {"id": "D", "text": "A root-cause analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A tabletop exercise is a discussion-based walkthrough of a scenario used to validate "
                       "the IR plan, roles, and decisions without touching live systems.",
            "distractors": {
                "B": "A penetration test actively exploits systems to find weaknesses, not a discussion of the plan.",
                "C": "A full-interruption test actually halts production systems -- the opposite of 'without disrupting production.'",
                "D": "Root-cause analysis investigates why a real incident happened; it is not a planned rehearsal.",
            },
            "exam_pattern": "Discussion-based walkthrough that validates the plan = tabletop exercise.",
        },
        "references": ["CS0-003 3.3 -- Preparation: training and testing (tabletop exercises)"],
    },

    # ===== ir_detection_analysis ===========================================
    {
        "id": "cysa-ir-011", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An analyst must collect digital evidence from a running compromised server. According to "
                "the order of volatility, which source should be collected FIRST?",
        "options": [
            {"id": "A", "text": "The contents of RAM and CPU cache"},
            {"id": "B", "text": "Data on the hard disk drive"},
            {"id": "C", "text": "Archived backup tapes"},
            {"id": "D", "text": "Logs on a remote syslog server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Order of volatility collects the most volatile data first; CPU cache/registers and RAM "
                       "are lost on power-off, so they are captured before disk or archival media.",
            "distractors": {
                "B": "Disk data is far less volatile than memory and is collected after volatile memory.",
                "C": "Archived backup tapes are the least volatile source and are collected last.",
                "D": "Remote syslog data is relatively stable storage, captured after volatile memory.",
            },
            "exam_pattern": "Order of volatility -> capture RAM/cache before disk; archives last.",
        },
        "references": ["CS0-003 3.2 -- Evidence acquisition: order of volatility"],
    },
    {
        "id": "cysa-ir-012", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 1, "type": "mcq",
        "stem": "After imaging a suspect's drive, an investigator records who handled the evidence, when, "
                "and why at every transfer. What does this documentation establish?",
        "options": [
            {"id": "A", "text": "Chain of custody"},
            {"id": "B", "text": "Order of volatility"},
            {"id": "C", "text": "A communication plan"},
            {"id": "D", "text": "A disaster recovery plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Chain of custody is the documented, unbroken record of everyone who handled the "
                       "evidence and when, preserving its integrity and admissibility in court.",
            "distractors": {
                "B": "Order of volatility dictates the sequence of collection, not who handled the evidence.",
                "C": "A communication plan governs incident notifications, not evidence handling.",
                "D": "A disaster recovery plan covers restoring operations, unrelated to evidence tracking.",
            },
            "exam_pattern": "Who touched the evidence, when, and why = chain of custody.",
        },
        "references": ["CS0-003 3.2 -- Evidence acquisition: chain of custody"],
    },
    {
        "id": "cysa-ir-013", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Before and after creating a forensic image of a disk, an analyst computes a SHA-256 hash "
                "of both the original and the copy. What is the main purpose of doing this?",
        "options": [
            {"id": "A", "text": "To prove the image is a bit-for-bit, unaltered copy of the original"},
            {"id": "B", "text": "To encrypt the image so it cannot be read"},
            {"id": "C", "text": "To compress the image and save storage"},
            {"id": "D", "text": "To speed up the imaging process"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matching hash values before and after prove the image is an exact, unaltered copy, "
                       "validating evidence integrity for legal proceedings.",
            "distractors": {
                "B": "Hashing is a one-way integrity check, not encryption; it does not conceal the data.",
                "C": "Hashing does not compress data; the image size is unchanged.",
                "D": "Computing a hash adds work; it does not speed up imaging.",
            },
            "exam_pattern": "Matching hashes before/after = integrity verification of a forensic copy (not encryption).",
        },
        "references": ["CS0-003 3.2 -- Evidence acquisition: data integrity validation"],
    },
    {
        "id": "cysa-ir-014", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An analyst needs a timeline of process execution, file changes, and parent-child process "
                "relationships on an endpoint during an attack. Which data source is BEST?",
        "options": [
            {"id": "A", "text": "Endpoint detection and response (EDR) telemetry"},
            {"id": "B", "text": "A network firewall's allow/deny rule list"},
            {"id": "C", "text": "The building's physical access logs"},
            {"id": "D", "text": "A DHCP lease table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR records detailed host telemetry -- process creation, parent-child chains, and "
                       "file/registry changes -- ideal for reconstructing on-host attacker activity.",
            "distractors": {
                "B": "A firewall rule list shows configured policy, not a timeline of host process execution.",
                "C": "Physical access logs track door entries, not software process activity.",
                "D": "A DHCP lease table maps IPs to MACs; it lacks process-level detail.",
            },
            "exam_pattern": "Host process / parent-child timeline = EDR endpoint telemetry.",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: data sources (EDR)"],
    },
    {
        "id": "cysa-ir-015", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Investigators suspect data was exfiltrated and need to see the actual payloads and "
                "destinations of traffic that left the network. Which evidence source provides this?",
        "options": [
            {"id": "A", "text": "Full packet capture (PCAP)"},
            {"id": "B", "text": "CPU utilization graphs"},
            {"id": "C", "text": "A password policy document"},
            {"id": "D", "text": "Antivirus signature version numbers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Full packet capture records complete traffic contents, letting analysts examine "
                       "payloads, protocols, and destinations to confirm exfiltration.",
            "distractors": {
                "B": "CPU graphs show host load, not what data traversed the network.",
                "C": "A password policy is administrative documentation, not traffic evidence.",
                "D": "AV signature versions indicate update state, not exfiltrated content.",
            },
            "exam_pattern": "Need the actual payload/content of traffic = full packet capture (PCAP).",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: data sources (packet capture)"],
    },
    {
        "id": "cysa-ir-016", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A SIEM fires a 'malware detected' alert. Before escalating, the analyst confirms the file "
                "is truly malicious and present on the host. This validation step chiefly guards against...",
        "options": [
            {"id": "A", "text": "Acting on a false positive"},
            {"id": "B", "text": "Order-of-volatility errors"},
            {"id": "C", "text": "A broken chain of custody"},
            {"id": "D", "text": "Exceeding the data retention policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Validating that an alert reflects real malicious activity prevents wasting response "
                       "effort on a false positive before escalation.",
            "distractors": {
                "B": "Order of volatility concerns evidence collection sequence, not alert validation.",
                "C": "Chain of custody concerns evidence handling, not confirming an alert's accuracy.",
                "D": "Data retention governs how long logs are kept, unrelated to validating an alert.",
            },
            "exam_pattern": "Confirm an alert is real before escalating = rule out false positives (triage/validation).",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: alert validation"],
    },
    {
        "id": "cysa-ir-017", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "mcq",
        "stem": "After confirming one workstation is infected, the analyst queries EDR across the fleet to "
                "find every host showing the same indicators. This activity is BEST described as...",
        "options": [
            {"id": "A", "text": "Scoping the incident"},
            {"id": "B", "text": "Eradicating the malware"},
            {"id": "C", "text": "Performing lessons learned"},
            {"id": "D", "text": "Restoring from backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scoping determines the full extent of an incident -- how many hosts or accounts are "
                       "affected -- by hunting for the same indicators across the environment.",
            "distractors": {
                "B": "Eradication removes the malware; here the analyst is still measuring breadth, not removing anything.",
                "C": "Lessons learned is a post-incident review, not the active search for affected hosts.",
                "D": "Restoring from backup is a recovery action performed after scope and eradication.",
            },
            "exam_pattern": "Finding every affected host / how far it spread = scoping (impact determination).",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: scope and impact"],
    },
    {
        "id": "cysa-ir-018", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A threat feed lists a specific malicious file hash, a command-and-control IP address, and "
                "a suspicious domain. Collectively, how are these artifacts categorized?",
        "options": [
            {"id": "A", "text": "Indicators of compromise (IoCs)"},
            {"id": "B", "text": "Compensating controls"},
            {"id": "C", "text": "Service-level objectives"},
            {"id": "D", "text": "Business impact metrics"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File hashes, malicious IPs/domains, and similar artifacts are indicators of compromise "
                       "-- observable evidence that a system may be breached, used to detect and hunt.",
            "distractors": {
                "B": "Compensating controls are alternative safeguards, not forensic artifacts of an attack.",
                "C": "Service-level objectives are performance targets, unrelated to breach artifacts.",
                "D": "Business impact metrics quantify consequences, not detection artifacts.",
            },
            "exam_pattern": "Hashes, malicious IPs/domains used to detect intrusions = indicators of compromise.",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: indicators of compromise"],
    },
    {
        "id": "cysa-ir-019", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "multi",
        "stem": "An analyst is acquiring evidence from a live, compromised server for a potential legal "
                "case. Which TWO actions best preserve evidentiary integrity?",
        "options": [
            {"id": "A", "text": "Capture volatile memory before powering down the system"},
            {"id": "B", "text": "Generate and record a cryptographic hash of each acquired image"},
            {"id": "C", "text": "Work directly on the original drive to save time"},
            {"id": "D", "text": "Delete suspicious files immediately to stop the attack"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Capturing RAM before shutdown preserves volatile evidence, and hashing each image "
                       "proves it was not altered -- both are core forensic-integrity practices.",
            "distractors": {
                "C": "Analysts work on verified copies, never the original, to avoid altering source evidence.",
                "D": "Deleting files destroys evidence and is an eradication action, not evidence preservation.",
            },
            "exam_pattern": "Preserve evidence = capture volatile data first + hash working copies; never alter the original.",
        },
        "references": ["CS0-003 3.2 -- Evidence acquisition and forensics"],
    },
    {
        "id": "cysa-ir-020", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_detection_analysis", "difficulty": 3, "type": "mcq",
        "stem": "To determine whether a compromised account was used to log in to multiple servers, which "
                "log source should the analyst correlate FIRST?",
        "options": [
            {"id": "A", "text": "Authentication/security event logs from the servers and domain controllers"},
            {"id": "B", "text": "Printer spooler logs"},
            {"id": "C", "text": "HVAC controller logs"},
            {"id": "D", "text": "Marketing web analytics"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authentication and security event logs (including domain-controller logon events) "
                       "reveal where and when an account authenticated, exposing lateral use.",
            "distractors": {
                "B": "Printer spooler logs track print jobs, not account logons.",
                "C": "HVAC logs are facility telemetry, irrelevant to account authentication.",
                "D": "Web analytics measure site visitors, not internal account logins.",
            },
            "exam_pattern": "'Where did this account log in?' = authentication / security event logs (DC logon events).",
        },
        "references": ["CS0-003 3.2 -- Detection and analysis: log analysis"],
    },

    # ===== ir_containment_recovery =========================================
    {
        "id": "cysa-ir-021", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 1, "type": "mcq",
        "stem": "Analysts confirm a workstation is actively infected and spreading, so they disconnect it "
                "from the network to stop the spread. Which IR phase does this action represent?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Recovery"},
            {"id": "D", "text": "Detection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Isolating or disconnecting an affected host to limit damage and prevent spread is "
                       "containment.",
            "distractors": {
                "B": "Eradication removes the malicious artifacts (wiping/cleaning); disconnecting does not remove them.",
                "C": "Recovery restores systems to normal operation, which comes after the threat is removed.",
                "D": "Detection is identifying that an incident occurred, which has already happened here.",
            },
            "exam_pattern": "Isolate/disconnect to stop spread = containment (NOT eradication).",
        },
        "references": ["CS0-003 3.2 -- Containment, eradication, and recovery: containment"],
    },
    {
        "id": "cysa-ir-022", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Right after detecting an intrusion, the team isolates affected hosts to stop damage while "
                "keeping evidence intact, planning a fuller fix later. This is BEST described as...",
        "options": [
            {"id": "A", "text": "Short-term containment"},
            {"id": "B", "text": "Long-term containment"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Lessons learned"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Short-term containment is a rapid, often temporary action (such as isolating hosts) "
                       "that limits immediate damage while preserving evidence, before a durable fix.",
            "distractors": {
                "B": "Long-term containment applies more permanent, sustainable measures (e.g., rebuilt and patched systems) after the immediate threat is checked.",
                "C": "Eradication removes the threat entirely; isolation alone does not.",
                "D": "Lessons learned is a post-incident review, not an immediate containment action.",
            },
            "exam_pattern": "Immediate, temporary damage-limiting = short-term containment; durable fix = long-term.",
        },
        "references": ["CS0-003 3.2 -- Containment: short-term vs long-term"],
    },
    {
        "id": "cysa-ir-023", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "To contain malware spreading across a flat network without taking critical servers fully "
                "offline, which action is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Segment the network to isolate the affected systems"},
            {"id": "B", "text": "Reimage every server in the data center at once"},
            {"id": "C", "text": "Disable logging to reduce noise"},
            {"id": "D", "text": "Publish a lessons-learned report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Network segmentation isolates affected systems and restricts lateral movement while "
                       "unaffected critical services keep running -- an effective containment control.",
            "distractors": {
                "B": "Reimaging everything at once is drastic, disruptive, and premature before scoping -- not a measured containment step.",
                "C": "Disabling logging destroys the visibility needed for investigation and contains nothing.",
                "D": "A lessons-learned report is a post-incident activity, not an active containment control.",
            },
            "exam_pattern": "Limit lateral spread while staying operational = segmentation/isolation (containment).",
        },
        "references": ["CS0-003 3.2 -- Containment: isolation and segmentation"],
    },
    {
        "id": "cysa-ir-024", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 2, "type": "mcq",
        "stem": "After containing a breach, the team removes the malware, deletes attacker-created accounts, "
                "and patches the exploited vulnerability. Which IR phase includes these actions?",
        "options": [
            {"id": "A", "text": "Eradication"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Preparation"},
            {"id": "D", "text": "Post-incident activity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Eradication eliminates the threat and its artifacts -- removing malware and rogue "
                       "accounts and patching the root-cause vulnerability so it cannot be reused.",
            "distractors": {
                "B": "Containment limits spread; it precedes removing artifacts and patching the root cause.",
                "C": "Preparation happens before any incident, building readiness.",
                "D": "Post-incident activity follows recovery; it is review, not the removal of artifacts.",
            },
            "exam_pattern": "Remove malware/rogue accounts + patch the exploited flaw = eradication.",
        },
        "references": ["CS0-003 3.2 -- Containment, eradication, and recovery: eradication"],
    },
    {
        "id": "cysa-ir-025", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A host was compromised by a kernel-level rootkit. To be confident the threat is fully "
                "removed, what is the MOST reliable eradication method?",
        "options": [
            {"id": "A", "text": "Wipe and reimage the system from a known-good baseline"},
            {"id": "B", "text": "Delete the detected files and keep using the system"},
            {"id": "C", "text": "Rename the malicious service and reboot"},
            {"id": "D", "text": "Only update the antivirus signatures"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Kernel rootkits can hide and persist, so wiping and reimaging from a trusted baseline "
                       "is the most reliable way to guarantee complete removal.",
            "distractors": {
                "B": "Deleting visible files may leave hidden rootkit components, so the host cannot be trusted.",
                "C": "Renaming a service does not remove a kernel-level rootkit and leaves the host compromised.",
                "D": "Updating signatures may detect but does not guarantee removal of an entrenched rootkit.",
            },
            "exam_pattern": "Deep/kernel persistence (rootkit) = wipe and reimage from known-good, not clean-in-place.",
        },
        "references": ["CS0-003 3.2 -- Eradication: reimaging"],
    },
    {
        "id": "cysa-ir-026", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 2, "type": "mcq",
        "stem": "After eradicating the threat, the team restores systems from clean backups and closely "
                "watches them for reinfection before declaring normal operations. This monitoring is part of...",
        "options": [
            {"id": "A", "text": "Recovery"},
            {"id": "B", "text": "Detection"},
            {"id": "C", "text": "Weaponization"},
            {"id": "D", "text": "Chain of custody"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recovery restores systems to production and includes validating and monitoring them "
                       "to confirm the threat is gone before returning to normal operations.",
            "distractors": {
                "B": "Detection is identifying the original incident, not post-restoration monitoring.",
                "C": "Weaponization is an attacker kill-chain step, not a defender recovery activity.",
                "D": "Chain of custody concerns evidence handling, not system restoration monitoring.",
            },
            "exam_pattern": "Restore + validate + monitor before the 'all clear' = recovery.",
        },
        "references": ["CS0-003 3.2 -- Containment, eradication, and recovery: recovery"],
    },
    {
        "id": "cysa-ir-027", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "mcq",
        "stem": "During recovery, before reconnecting a rebuilt server to production, the team confirms the "
                "exploited vulnerability is patched and the system is clean. Why is this step critical?",
        "options": [
            {"id": "A", "text": "Restoring a system without fixing the root cause invites immediate reinfection"},
            {"id": "B", "text": "It satisfies the order of volatility"},
            {"id": "C", "text": "It establishes the chain of custody"},
            {"id": "D", "text": "It completes the weaponization phase"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "If the root-cause vulnerability is not remediated, the restored system can be "
                       "compromised again at once; validating before reconnection prevents a repeat incident.",
            "distractors": {
                "B": "Order of volatility governs evidence-collection order, not recovery validation.",
                "C": "Chain of custody tracks evidence handling, not patch verification.",
                "D": "Weaponization is an attacker phase, irrelevant to defender recovery.",
            },
            "exam_pattern": "Validate patch/clean state before reconnecting, or the box gets reinfected = recovery best practice.",
        },
        "references": ["CS0-003 3.2 -- Recovery: validation and monitoring"],
    },
    {
        "id": "cysa-ir-028", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 2, "type": "mcq",
        "stem": "During the post-incident review, the team determines that an unpatched VPN appliance was "
                "the initial entry point. Identifying this underlying reason is called...",
        "options": [
            {"id": "A", "text": "Root-cause analysis"},
            {"id": "B", "text": "Short-term containment"},
            {"id": "C", "text": "Order of volatility"},
            {"id": "D", "text": "A tabletop exercise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Root-cause analysis identifies the fundamental reason an incident occurred (here, the "
                       "unpatched VPN) so the weakness can be fixed and recurrence prevented.",
            "distractors": {
                "B": "Short-term containment is an immediate damage-limiting action during the incident, not post-incident cause analysis.",
                "C": "Order of volatility is an evidence-collection sequence, not cause identification.",
                "D": "A tabletop exercise is a pre-incident rehearsal, not analysis of an actual incident's cause.",
            },
            "exam_pattern": "The underlying reason the incident happened = root-cause analysis (post-incident).",
        },
        "references": ["CS0-003 3.3 -- Post-incident activity: root-cause analysis"],
    },
    {
        "id": "cysa-ir-029", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 2, "type": "mcq",
        "stem": "After an incident is closed, the team holds a lessons-learned meeting and updates its "
                "playbooks based on what went wrong. What is the main purpose of this activity?",
        "options": [
            {"id": "A", "text": "To improve future response and prevent recurrence"},
            {"id": "B", "text": "To assign legal blame to an individual employee"},
            {"id": "C", "text": "To immediately contain the active threat"},
            {"id": "D", "text": "To capture volatile memory from affected hosts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A lessons-learned review examines what happened and feeds improvements into IR plans, "
                       "playbooks, and controls to strengthen future response and reduce recurrence.",
            "distractors": {
                "B": "The goal is process improvement; a blameless review is encouraged, not assigning blame.",
                "C": "Containment happens during the incident; this is a post-incident activity.",
                "D": "Capturing volatile memory is an evidence-acquisition step during analysis, not a lessons-learned goal.",
            },
            "exam_pattern": "Post-incident meeting + update plans/playbooks = lessons learned (continuous improvement).",
        },
        "references": ["CS0-003 3.3 -- Post-incident activity: lessons learned"],
    },
    {
        "id": "cysa-ir-030", "exam": "cysa", "domain": "cysa_incident_response",
        "subtopic": "ir_containment_recovery", "difficulty": 3, "type": "multi",
        "stem": "Closing out a major incident, the IR lead prepares post-incident deliverables. Which TWO "
                "are appropriate outputs of the post-incident activity phase?",
        "options": [
            {"id": "A", "text": "A root-cause analysis / after-action report"},
            {"id": "B", "text": "Updates to IR playbooks and the response plan"},
            {"id": "C", "text": "The initial isolation of infected hosts"},
            {"id": "D", "text": "The first SIEM alert that detected the activity"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Post-incident activity produces a root-cause / after-action report and feeds "
                       "improvements into the IR plan and playbooks for future incidents.",
            "distractors": {
                "C": "Isolating infected hosts is a containment action during the incident, not a post-incident output.",
                "D": "The initial SIEM alert belongs to detection and analysis, not the post-incident phase.",
            },
            "exam_pattern": "Post-incident outputs = after-action/RCA report + updated plans/playbooks.",
        },
        "references": ["CS0-003 3.3 -- Post-incident activity: after-action report"],
    },
]
