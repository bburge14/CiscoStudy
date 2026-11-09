"""CompTIA SecurityX (CAS-005) pool - Domain 4: Security Operations.

Original, objective-aligned practice items for the five Security Operations
subtopics tracked in CertLab (expert/CASP+-level, scenario and trade-off driven):
  * scx_threat_hunting       - hypothesis-driven hunting, MITRE ATT&CK/TTPs,
                               IOCs vs IOAs, the Pyramid of Pain.
  * scx_incident_response    - NIST SP 800-61 lifecycle, short-term containment
                               and evidence preservation, post-incident activity,
                               preparation (playbooks, out-of-band comms).
  * scx_vuln_management      - CVSS, risk-based prioritization (EPSS, CISA KEV),
                               authenticated scanning, compensating controls.
  * scx_monitoring_detection - SIEM correlation, UEBA/anomaly detection, time
                               synchronization (NTP) for log correlation.
  * scx_forensics            - order of volatility (RFC 3227), chain of custody,
                               sound live-memory and write-blocked disk acquisition.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so authored keys are spread across A-D (not
positionally biased), every wrong option carries a distractor note, and each
item cites the public CAS-005 objective domain it draws on. Expert depth with
BEST-given-constraints framing - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== scx_threat_hunting ===============================================
    {
        "id": "securityx-ops-001", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "A mature SOC wants to proactively search for adversaries that have evaded existing alerts. An "
                "analyst forms the idea, 'If an attacker is using living-off-the-land binaries for persistence, I "
                "should see unusual scheduled-task creation by certain processes,' and then queries telemetry to "
                "prove or disprove it. Which approach is this?",
        "options": [
            {"id": "A", "text": "Signature-based alert triage"},
            {"id": "B", "text": "Hypothesis-driven threat hunting"},
            {"id": "C", "text": "Automated vulnerability scanning"},
            {"id": "D", "text": "Waiting for SIEM alerts to fire"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Proactively forming a testable hypothesis about adversary behavior and querying telemetry to "
                       "confirm or refute it is hypothesis-driven threat hunting - it assumes breach and looks for what alerts missed.",
            "distractors": {
                "A": "Alert triage reacts to signatures that already fired; hunting is proactive and not signature-bound.",
                "C": "Vulnerability scanning finds weaknesses, not active adversary behavior in telemetry.",
                "D": "Waiting for alerts is reactive - the opposite of proactive hunting.",
            },
            "exam_pattern": "Proactive, testable 'if the attacker does X, I'll see Y' + query the data = hypothesis-driven hunting (assume breach).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (hypothesis-driven)"],
    },
    {
        "id": "securityx-ops-002", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A threat-hunting team wants a common, structured knowledge base of real-world adversary tactics "
                "(the 'why') and techniques (the 'how') to map detections and coverage gaps across the attack "
                "lifecycle. Which framework is designed for this?",
        "options": [
            {"id": "A", "text": "MITRE ATT&CK"},
            {"id": "B", "text": "The OWASP Top 10"},
            {"id": "C", "text": "A cloud pricing calculator"},
            {"id": "D", "text": "COBIT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MITRE ATT&CK is a curated knowledge base of adversary tactics (goals) and "
                       "techniques/sub-techniques (methods) based on real-world observations, widely used to map detection coverage and hunt for TTPs.",
            "distractors": {
                "B": "The OWASP Top 10 ranks web application security risks, not the adversary tactic/technique matrix.",
                "C": "A cloud pricing calculator is a cost tool, unrelated to adversary TTP mapping.",
                "D": "COBIT is an IT governance/management framework, not an adversary-behavior knowledge base.",
            },
            "exam_pattern": "Tactics (why) + techniques (how) knowledge base for mapping/hunting = MITRE ATT&CK.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (MITRE ATT&CK, TTPs)"],
    },
    {
        "id": "securityx-ops-003", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "During hunting, Analyst A searches for a specific known-malicious file hash and C2 IP address, "
                "while Analyst B looks for the behavior of 'a process spawning a command shell that then encodes "
                "and beacons out.' How are these BEST categorized, respectively?",
        "options": [
            {"id": "A", "text": "Both are indicators of attack (IOAs)"},
            {"id": "B", "text": "Both are indicators of compromise (IOCs)"},
            {"id": "C", "text": "Analyst A is using indicators of compromise (IOCs); Analyst B is using indicators of attack (IOAs/behaviors)"},
            {"id": "D", "text": "Analyst A is using IOAs; Analyst B is using IOCs"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Static artifacts of a known-bad event (hashes, IPs, domains) are IOCs; focusing on adversary "
                       "behavior/intent regardless of specific artifacts (process lineage, encoding, beaconing) is an IOA. IOAs are more durable because attackers can change hashes and IPs easily.",
            "distractors": {
                "A": "The hash/IP search is artifact-based (an IOC), not behavior-based, so 'both IOA' is wrong.",
                "B": "Analyst B's behavior-based hunt is an IOA, not an IOC, so 'both IOC' is wrong.",
                "D": "This reverses the two - artifacts are IOCs and behaviors are IOAs.",
            },
            "exam_pattern": "IOC = static known-bad artifact (hash/IP/domain); IOA = behavior/intent (harder for the adversary to change).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (IOCs vs IOAs)"],
    },
    {
        "id": "securityx-ops-004", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "Using the Pyramid of Pain to prioritize detections, a team wants to build detections that are "
                "HARDEST for an adversary to change and therefore cause them the most difficulty. Which indicator "
                "type should they focus on?",
        "options": [
            {"id": "A", "text": "File hash values"},
            {"id": "B", "text": "IP addresses"},
            {"id": "C", "text": "Domain names"},
            {"id": "D", "text": "Tactics, techniques, and procedures (TTPs / behaviors)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "In the Pyramid of Pain, hashes/IPs/domains are trivial-to-moderate for adversaries to change, "
                       "while TTPs sit at the top - detecting behaviors forces attackers to change how they operate, which is costly and 'painful.'",
            "distractors": {
                "A": "Hashes are trivial to change (recompile or repack), at the bottom of the pyramid.",
                "B": "IP addresses are easy to rotate, low on the pyramid.",
                "C": "Domains are relatively easy to change - higher than IPs but still far below TTPs.",
            },
            "exam_pattern": "Pyramid of Pain: detect TTPs/behaviors (top) for maximum adversary cost; hashes/IPs/domains are easily swapped.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (Pyramid of Pain, TTPs)"],
    },

    # ===== scx_incident_response ============================================
    {
        "id": "securityx-ops-005", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "Per the NIST SP 800-61 incident-response lifecycle, which sequence of phases is correct?",
        "options": [
            {"id": "A", "text": "Preparation -> Detection & Analysis -> Containment, Eradication & Recovery -> Post-Incident Activity"},
            {"id": "B", "text": "Detection -> Preparation -> Recovery -> Containment"},
            {"id": "C", "text": "Containment -> Preparation -> Detection -> Lessons Learned"},
            {"id": "D", "text": "Eradication -> Detection -> Preparation -> Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NIST SP 800-61 defines four phases: Preparation; Detection & Analysis; Containment, "
                       "Eradication & Recovery; and Post-Incident Activity (lessons learned) - an iterative cycle.",
            "distractors": {
                "B": "Preparation must precede detection, and containment/recovery come after analysis - this order is scrambled.",
                "C": "You cannot contain before preparing and detecting; the order is wrong.",
                "D": "Eradication occurs after detection and containment, not first; this order is invalid.",
            },
            "exam_pattern": "NIST 800-61: Prep -> Detection & Analysis -> Containment/Eradication/Recovery -> Post-Incident (lessons learned).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (NIST SP 800-61 lifecycle)"],
    },
    {
        "id": "securityx-ops-006", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 3, "type": "mcq",
        "stem": "During an active ransomware outbreak spreading via SMB, the IR team must stop the spread "
                "immediately while preserving evidence for later analysis. Which action BEST reflects sound "
                "short-term containment?",
        "options": [
            {"id": "A", "text": "Immediately wipe and reimage every affected host to eradicate the malware"},
            {"id": "B", "text": "Isolate/segment affected hosts from the network (e.g., host isolation, blocking SMB) while preserving volatile evidence before eradication"},
            {"id": "C", "text": "Shut down the entire company network and all logging"},
            {"id": "D", "text": "Do nothing until the full root-cause analysis is complete"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Short-term containment isolates affected systems to stop spread (host isolation, blocking the "
                       "propagation vector) while preserving volatile evidence (memory, logs) for forensics, which precedes eradication and recovery.",
            "distractors": {
                "A": "Immediately wiping hosts destroys forensic evidence and skips containment/analysis - eradication comes after containment and evidence preservation.",
                "C": "Killing all logging destroys the evidence and visibility needed to manage the incident.",
                "D": "Waiting for full root-cause analysis while ransomware spreads allows avoidable damage; containment must happen promptly.",
            },
            "exam_pattern": "Contain first (isolate, stop spread) AND preserve volatile evidence before eradication; don't wipe prematurely.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (containment strategies, evidence preservation)"],
    },
    {
        "id": "securityx-ops-007", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "Two weeks after an incident is resolved, the team holds a blameless review to document root "
                "cause, what worked, and improvements to controls and playbooks. Which NIST SP 800-61 phase is this?",
        "options": [
            {"id": "A", "text": "Detection and Analysis"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Post-Incident Activity (lessons learned)"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A post-resolution review capturing root cause, effectiveness, and improvements is "
                       "Post-Incident Activity (lessons learned), which then feeds back into Preparation.",
            "distractors": {
                "A": "Detection and Analysis is about identifying and scoping the incident, not the after-action review.",
                "B": "Containment limits damage during the incident, not reflection afterward.",
                "D": "Preparation builds capabilities before incidents; the review informs it but is a distinct, later phase.",
            },
            "exam_pattern": "After-action / root-cause / improvements = Post-Incident Activity (lessons learned) -> feeds Preparation.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (post-incident activity)"],
    },
    {
        "id": "securityx-ops-008", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 3, "type": "multi",
        "stem": "An organization is maturing its incident-response preparation. Which TWO measures MOST improve "
                "readiness BEFORE an incident occurs? (Choose two.)",
        "options": [
            {"id": "A", "text": "Maintain tested IR playbooks and run regular tabletop/simulation exercises"},
            {"id": "B", "text": "Wait for a real incident to discover gaps in the process"},
            {"id": "C", "text": "Keep the only copy of the IR plan on a network share that ransomware could encrypt"},
            {"id": "D", "text": "Pre-establish roles, communication plans (including out-of-band channels), and retainer/legal/breach-notification contacts"},
        ],
        "correct": ["A", "D"],
        "explanation": {
            "correct": "Readiness comes from tested playbooks plus exercises, and from pre-established roles, "
                       "out-of-band communications, and pre-arranged legal / IR-retainer / notification contacts - so the team acts quickly and correctly under pressure.",
            "distractors": {
                "B": "Waiting for a real incident to find gaps is reactive and increases damage - the opposite of preparation.",
                "C": "Storing the only IR-plan copy where ransomware can encrypt it means it may be unavailable exactly when needed (keep offline copies).",
            },
            "exam_pattern": "IR preparation = tested playbooks + exercises + defined roles/out-of-band comms + pre-arranged legal/notification contacts; keep offline copies.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (preparation, playbooks, communications)"],
    },

    # ===== scx_vuln_management ==============================================
    {
        "id": "securityx-ops-009", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the acronym: The open framework that produces a standardized 0.0-10.0 "
                "severity score (using Base, Temporal/Threat, and Environmental metric groups) for a vulnerability "
                "is the Common Vulnerability Scoring System, abbreviated ______.",
        "correct": ["cvss"],
        "explanation": {
            "correct": "CVSS provides a standardized severity score from 0.0 to 10.0 using Base, Temporal/Threat, and "
                       "Environmental metric groups; it measures severity but should be combined with exploitability and asset context for true prioritization.",
            "distractors": {},
            "exam_pattern": "Standardized 0-10 vulnerability severity = CVSS; severity alone is not risk - add exploitability + asset context.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (CVSS)"],
    },
    {
        "id": "securityx-ops-010", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A scanner reports 4,000 vulnerabilities, far more than the team can patch at once. Several are "
                "CVSS 9.8 but on isolated test systems with no exploit seen in the wild, while one CVSS 7.5 is on "
                "an internet-facing crown-jewel app and appears on CISA's Known Exploited Vulnerabilities list. "
                "Which prioritization approach is BEST?",
        "options": [
            {"id": "A", "text": "Patch strictly in descending CVSS base-score order"},
            {"id": "B", "text": "Patch the oldest CVEs first regardless of context"},
            {"id": "C", "text": "Patch whatever is easiest to patch first"},
            {"id": "D", "text": "Prioritize by risk: combine severity with real-world exploitability (e.g., EPSS, CISA KEV), asset exposure, and business criticality"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Effective risk-based prioritization blends severity (CVSS) with exploitation likelihood "
                       "(EPSS, CISA KEV / active exploitation), internet exposure, and business criticality - so the actively exploited, internet-facing crown-jewel issue outranks a high-CVSS flaw on an isolated test box.",
            "distractors": {
                "A": "CVSS base score alone ignores exploitability and asset context, misranking real risk.",
                "B": "The age of a CVE is not a sound risk signal by itself.",
                "C": "Ease of patching is operational convenience, not a measure of risk.",
            },
            "exam_pattern": "Prioritize by risk = severity x exploitability (EPSS/KEV) x exposure x business impact, not CVSS alone.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (risk-based prioritization, EPSS, CISA KEV)"],
    },
    {
        "id": "securityx-ops-011", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 2, "type": "mcq",
        "stem": "A team's unauthenticated network scans keep missing patches and producing uncertain"
                "results, because they can only see services from outside the host. Which change will MOST improve "
                "scan accuracy and reduce false positives for host configuration and patch state?",
        "options": [
            {"id": "A", "text": "Use authenticated (credentialed) scanning so the scanner can log in and inspect actual patch levels and configuration"},
            {"id": "B", "text": "Scan less frequently to reduce noise"},
            {"id": "C", "text": "Only scan the perimeter firewall"},
            {"id": "D", "text": "Replace scanning with a one-time annual penetration test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Credentialed (authenticated) scans log into hosts to read exact patch levels, configuration, "
                       "and installed software, giving far more accurate results and fewer false positives than unauthenticated scans that only probe exposed services.",
            "distractors": {
                "B": "Scanning less often reduces visibility and timeliness; it doesn't improve per-scan accuracy.",
                "C": "Scanning only the firewall ignores internal host state entirely.",
                "D": "An annual pen test is point-in-time and doesn't replace continuous, accurate configuration/patch assessment.",
            },
            "exam_pattern": "Accurate patch/config state + fewer false positives = authenticated (credentialed) scanning.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (authenticated vs unauthenticated scanning)"],
    },
    {
        "id": "securityx-ops-012", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A critical vulnerability is found in a legacy medical device that the vendor cannot patch for 9 "
                "months and that cannot be taken offline. Which response BEST manages the risk in the interim?",
        "options": [
            {"id": "A", "text": "Ignore it until the vendor releases a patch"},
            {"id": "B", "text": "Apply compensating controls: isolate/segment the device, restrict access with ACLs/firewalls, add virtual patching/IPS, and increase monitoring until a patch is available"},
            {"id": "C", "text": "Immediately disconnect the device regardless of patient impact"},
            {"id": "D", "text": "Formally accept the risk and take no technical action"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "When patching isn't feasible, compensating controls reduce exposure: network "
                       "segmentation/isolation, strict access controls, virtual patching/IPS, and enhanced monitoring - managing the risk until the device can be remediated.",
            "distractors": {
                "A": "Ignoring a critical, exploitable flaw for months leaves it fully exposed.",
                "C": "Disconnecting a device that cannot be taken offline may cause unacceptable safety/operational impact.",
                "D": "Formal acceptance with no mitigation leaves a known-critical risk unaddressed when controls are available.",
            },
            "exam_pattern": "Can't patch now -> compensating controls (segment, restrict, virtual-patch/IPS, monitor) until remediation.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (compensating controls, risk mitigation)"],
    },

    # ===== scx_monitoring_detection =========================================
    {
        "id": "securityx-ops-013", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to aggregate logs from firewalls, servers, endpoints, and cloud, then "
                "correlate events across them to detect multi-stage attacks and alert in near real time. Which "
                "platform is designed for this?",
        "options": [
            {"id": "A", "text": "A vulnerability scanner"},
            {"id": "B", "text": "A load balancer"},
            {"id": "C", "text": "A SIEM (security information and event management)"},
            {"id": "D", "text": "A password manager"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A SIEM centralizes and normalizes logs from many sources and applies correlation "
                       "rules/analytics to detect multi-stage attacks and generate near-real-time alerts, serving as the SOC's analysis hub.",
            "distractors": {
                "A": "A vulnerability scanner finds weaknesses; it doesn't correlate live multi-source event logs.",
                "B": "A load balancer distributes traffic and is not a log-correlation/detection platform.",
                "D": "A password manager stores credentials, unrelated to event correlation.",
            },
            "exam_pattern": "Aggregate + normalize + correlate multi-source logs with alerting = SIEM.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (SIEM, correlation)"],
    },
    {
        "id": "securityx-ops-014", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 3, "type": "mcq",
        "stem": "A company wants to detect a compromised-but-valid account and a malicious insider by flagging "
                "deviations from each user's and device's normal behavior (e.g., unusual login times, data-access "
                "volumes, or locations), rather than by fixed signatures. Which capability BEST provides this?",
        "options": [
            {"id": "A", "text": "Signature-based IDS"},
            {"id": "B", "text": "A certificate revocation list (CRL)"},
            {"id": "C", "text": "A WAF"},
            {"id": "D", "text": "User and entity behavior analytics (UEBA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "UEBA builds behavioral baselines for users and entities and uses analytics/ML to flag "
                       "anomalies (odd times, volumes, locations), making it well suited to detecting account compromise and insider threats that signatures miss.",
            "distractors": {
                "A": "A signature-based IDS matches known patterns and won't flag novel anomalous behavior by a valid account.",
                "B": "A CRL lists revoked certificates - unrelated to behavioral anomaly detection.",
                "C": "A WAF filters web-application attacks, not user-behavior anomalies across the enterprise.",
            },
            "exam_pattern": "Baseline normal + flag anomalies for insiders/compromised accounts = UEBA (behavioral analytics).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (UEBA, anomaly detection)"],
    },
    {
        "id": "securityx-ops-015", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 2, "type": "mcq",
        "stem": "An analyst correlating logs across firewalls, servers, and endpoints finds that timestamps "
                "disagree by minutes, making it impossible to reconstruct the true event sequence. Which "
                "foundational control MOST directly fixes this?",
        "options": [
            {"id": "A", "text": "Synchronize all systems to a common, reliable time source using NTP (with a consistent reference such as UTC)"},
            {"id": "B", "text": "Increase log retention to one year"},
            {"id": "C", "text": "Encrypt all log files at rest"},
            {"id": "D", "text": "Reduce the number of log sources"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Accurate event correlation and timeline reconstruction require synchronized clocks; using NTP "
                       "against a reliable source (and a consistent reference such as UTC) ensures timestamps line up across systems.",
            "distractors": {
                "B": "Longer retention keeps logs available but does not align mismatched timestamps.",
                "C": "Encryption protects log confidentiality/integrity but does not synchronize clocks.",
                "D": "Fewer log sources reduces visibility and still wouldn't synchronize the remaining clocks.",
            },
            "exam_pattern": "Cross-source correlation/timelines depend on synchronized clocks = NTP (standardize on UTC).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (time synchronization, log correlation)"],
    },

    # ===== scx_forensics ====================================================
    {
        "id": "securityx-ops-016", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: During evidence acquisition, the principle of collecting the most volatile "
                "data (such as CPU registers and RAM) before less volatile data (such as disk and archival media) "
                "is called the order of ______.",
        "correct": ["volatility", "order of volatility"],
        "explanation": {
            "correct": "The order of volatility (per RFC 3227) directs responders to capture the most ephemeral data "
                       "first - registers/cache, then RAM, network state, disk, and finally archival media - so fragile evidence isn't lost.",
            "distractors": {},
            "exam_pattern": "Collect most-ephemeral-first (registers/RAM -> disk -> archives) = order of volatility (RFC 3227).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (order of volatility)"],
    },
    {
        "id": "securityx-ops-017", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 2, "type": "mcq",
        "stem": "For evidence to be admissible, an investigator must document every person who handled a piece of "
                "evidence, plus when and why, from collection all the way to court. Which concept is this?",
        "options": [
            {"id": "A", "text": "Order of volatility"},
            {"id": "B", "text": "Chain of custody"},
            {"id": "C", "text": "Legal hold"},
            {"id": "D", "text": "Data remanence"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Chain of custody is the documented, unbroken record of who collected, handled, transferred, "
                       "and stored evidence (and when and why), preserving its integrity and admissibility.",
            "distractors": {
                "A": "Order of volatility governs the sequence of data collection, not custody documentation.",
                "C": "A legal hold preserves potentially relevant data from deletion; it isn't the handling record for a specific exhibit.",
                "D": "Data remanence is residual data left after deletion, unrelated to custody tracking.",
            },
            "exam_pattern": "Unbroken documented handling record for admissibility = chain of custody.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (chain of custody)"],
    },
    {
        "id": "securityx-ops-018", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 3, "type": "mcq",
        "stem": "An analyst must forensically acquire a running server suspected of hosting only in-memory "
                "(fileless) malware, then image its disk. Which approach BEST preserves evidence integrity?",
        "options": [
            {"id": "A", "text": "Pull the power immediately, then image the disk, skipping memory"},
            {"id": "B", "text": "Copy a few suspicious files out with normal OS tools and call it done"},
            {"id": "C", "text": "Capture volatile memory (RAM) from the live system first, then acquire a disk image using a write blocker and verify both with cryptographic hashes"},
            {"id": "D", "text": "Reboot the server into the OS and run antivirus before imaging"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Fileless malware lives in RAM, so capture volatile memory from the live system first; then "
                       "image the disk through a write blocker and verify the images with cryptographic hashes to prove integrity. This respects the order of volatility and preserves admissibility.",
            "distractors": {
                "A": "Pulling power destroys volatile RAM evidence - exactly where fileless malware resides.",
                "B": "Copying a few files with OS tools alters metadata, misses memory-resident artifacts, and isn't a sound, verifiable acquisition.",
                "D": "Rebooting and running AV changes system state, destroys memory evidence, and can alter or delete artifacts.",
            },
            "exam_pattern": "Live memory first (fileless), then write-blocked, hash-verified disk image = sound acquisition (order of volatility + integrity).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (memory/disk acquisition, write blocker, hashing)"],
    },
]
