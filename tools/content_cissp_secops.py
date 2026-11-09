"""(ISC)² CISSP pool - Domain 7: Security Operations.

Original, CBK-aligned practice items for the five Security Operations subtopics:
  * cissp_investigations        - order of volatility, chain of custody, forensic
                                  imaging/integrity.
  * cissp_logging_monitoring    - SIEM, egress monitoring/DLP, UEBA.
  * cissp_incident_management   - the (ISC)² incident phases (detection → response
                                  → mitigation → reporting → recovery → remediation
                                  → lessons learned).
  * cissp_dr_recovery           - RAID, backup schemes, DR test types.
  * cissp_change_config_mgmt    - change management/CAB approval, configuration
                                  baselines, emergency change handling.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_investigations =============================================
    {
        "id": "cissp-ops-001", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_investigations", "difficulty": 3, "type": "mcq",
        "stem": "A forensic examiner responds to a live, powered-on system suspected of compromise. "
                "According to the order of volatility, which evidence should be collected FIRST?",
        "options": [
            {"id": "A", "text": "The contents of the hard disk drive"},
            {"id": "B", "text": "Archived backup tapes"},
            {"id": "C", "text": "The contents of volatile memory (RAM) and running-process state"},
            {"id": "D", "text": "Printed documentation near the workstation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The order of volatility dictates collecting the most volatile data first; RAM and "
                       "running-process state disappear when power is lost, so they are captured before disk or archives.",
            "distractors": {
                "A": "Disk contents are far less volatile than RAM and are imaged after volatile data is captured.",
                "B": "Archived backups are among the least volatile sources, collected last.",
                "D": "Printed documents are non-volatile physical evidence gathered later.",
            },
            "exam_pattern": "Order of volatility - collect most volatile first (CPU/cache → RAM → disk → archives).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Order of volatility"],
    },
    {
        "id": "cissp-ops-002", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_investigations", "difficulty": 2, "type": "mcq",
        "stem": "To keep digital evidence admissible, an investigator documents every person who handled "
                "it, along with the date, time, and purpose, from collection through analysis. What is "
                "this documentation called?",
        "options": [
            {"id": "A", "text": "Chain of custody"},
            {"id": "B", "text": "The best evidence rule"},
            {"id": "C", "text": "An acceptable use policy"},
            {"id": "D", "text": "A service-level agreement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The chain of custody records who handled the evidence, when, and why, preserving its "
                       "integrity and admissibility.",
            "distractors": {
                "B": "The best evidence rule concerns presenting original documents, not tracking handling.",
                "C": "An acceptable use policy governs user conduct, not evidence handling.",
                "D": "An SLA defines service levels, unrelated to evidence integrity.",
            },
            "exam_pattern": "Documenting who handled evidence, when, and how = chain of custody (integrity + admissibility).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Chain of custody"],
    },
    {
        "id": "cissp-ops-003", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_investigations", "difficulty": 3, "type": "mcq",
        "stem": "Before analyzing a suspect hard drive, the examiner creates a bit-for-bit forensic "
                "image, calculates a cryptographic hash of both the original and the image, and works only "
                "on the copy. What is the PRIMARY purpose of hashing here?",
        "options": [
            {"id": "A", "text": "To compress the image so it fits on smaller media"},
            {"id": "B", "text": "To encrypt the evidence so others cannot read it"},
            {"id": "C", "text": "To speed up analysis of the copy"},
            {"id": "D", "text": "To prove the image is an exact, unaltered duplicate, preserving evidence integrity"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Matching hashes of the original and the forensic image prove the copy is identical and "
                       "has not been altered, which is essential for evidentiary integrity.",
            "distractors": {
                "A": "Hashing does not compress data.",
                "B": "Hashing is one-way and does not encrypt or conceal the contents.",
                "C": "Hashing verifies integrity; it does not speed up analysis.",
            },
            "exam_pattern": "Matching original and image hashes prove an exact, unaltered copy (work on the copy, preserve the original).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Forensic imaging and integrity"],
    },

    # ===== cissp_logging_monitoring =========================================
    {
        "id": "cissp-ops-004", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A security operations team wants to aggregate logs from many systems, correlate related "
                "events, and generate real-time alerts on suspicious patterns from a single platform. "
                "Which technology provides this?",
        "options": [
            {"id": "A", "text": "A single host-based firewall"},
            {"id": "B", "text": "A SIEM (security information and event management) system"},
            {"id": "C", "text": "A password vault"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A SIEM centralizes log collection, correlates events across sources, and raises "
                       "real-time alerts on suspicious patterns.",
            "distractors": {
                "A": "A host firewall filters traffic on one host and does not correlate enterprise-wide logs.",
                "C": "A password vault stores credentials, not event correlation.",
                "D": "A load balancer distributes traffic; it does not analyze security events.",
            },
            "exam_pattern": "Centralized log aggregation, correlation, and alerting = SIEM.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - SIEM and monitoring"],
    },
    {
        "id": "cissp-ops-005", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to detect and block sensitive data (such as customer records) from "
                "leaving the network via email or web uploads. Which monitoring capability is MOST "
                "directly aimed at this?",
        "options": [
            {"id": "A", "text": "Egress monitoring with data loss prevention (DLP)"},
            {"id": "B", "text": "Ingress filtering of inbound spam only"},
            {"id": "C", "text": "CPU performance monitoring"},
            {"id": "D", "text": "Patch compliance scanning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Egress monitoring with DLP inspects outbound traffic and can detect and block sensitive "
                       "data from leaving the organization.",
            "distractors": {
                "B": "Inbound spam filtering addresses incoming mail, not outbound data exfiltration.",
                "C": "CPU monitoring measures performance, not data movement.",
                "D": "Patch scanning checks software currency, not data leaving the network.",
            },
            "exam_pattern": "Watching outbound traffic to stop data exfiltration = egress monitoring / DLP.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Egress monitoring / DLP"],
    },
    {
        "id": "cissp-ops-006", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_logging_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "A monitoring tool builds a baseline of each user's normal behavior and then flags a "
                "finance clerk who suddenly downloads gigabytes of data at 3 a.m. from an unusual "
                "location. Which capability is this?",
        "options": [
            {"id": "A", "text": "Signature-based antivirus"},
            {"id": "B", "text": "A static packet filter"},
            {"id": "C", "text": "User and entity behavior analytics (UEBA)"},
            {"id": "D", "text": "A CAPTCHA challenge"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "UEBA establishes behavioral baselines for users and entities and flags anomalous "
                       "activity that deviates from the norm.",
            "distractors": {
                "A": "Signature-based antivirus matches known malware patterns, not behavioral baselines.",
                "B": "A static packet filter checks headers against fixed rules, not user behavior.",
                "D": "A CAPTCHA distinguishes humans from bots, unrelated to behavioral baselining.",
            },
            "exam_pattern": "Baseline normal behavior and flag deviations = UEBA (anomaly/behavior-based detection).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Behavior analytics (UEBA)"],
    },

    # ===== cissp_incident_management ========================================
    {
        "id": "cissp-ops-007", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 2, "type": "mcq",
        "stem": "Following the (ISC)² incident management process, which phase comes FIRST when an "
                "organization becomes aware that something abnormal may be a security incident?",
        "options": [
            {"id": "A", "text": "Detection"},
            {"id": "B", "text": "Recovery"},
            {"id": "C", "text": "Remediation"},
            {"id": "D", "text": "Lessons learned"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Detection is the first phase - recognizing that an event may be a security incident so "
                       "the response can begin.",
            "distractors": {
                "B": "Recovery (restoring systems) occurs after the incident is contained, not first.",
                "C": "Remediation (fixing the root cause) comes after recovery.",
                "D": "Lessons learned is the final phase, not the first.",
            },
            "exam_pattern": "(ISC)² order: Detection → Response → Mitigation → Reporting → Recovery → Remediation → Lessons Learned.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Incident management lifecycle"],
    },
    {
        "id": "cissp-ops-008", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 3, "type": "mcq",
        "stem": "An analyst confirms that a server is actively compromised and the attacker is spreading "
                "to other hosts. After detection and initial response, what is the BEST immediate action "
                "to limit damage?",
        "options": [
            {"id": "A", "text": "Immediately wipe and rebuild every server in the data center"},
            {"id": "B", "text": "Contain the incident (for example, isolate the affected server) to stop the spread"},
            {"id": "C", "text": "Write the final lessons-learned report"},
            {"id": "D", "text": "Ignore it until the next maintenance window"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mitigation/containment - isolating the affected system - limits the damage and stops "
                       "the attacker from spreading before eradication and recovery.",
            "distractors": {
                "A": "Wiping every server is disproportionate and destroys evidence before analysis.",
                "C": "The lessons-learned report is the last phase, not an immediate containment action.",
                "D": "Delaying lets the compromise spread further.",
            },
            "exam_pattern": "After detection/response, mitigation = contain to stop the spread and limit damage first.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Containment/mitigation"],
    },
    {
        "id": "cissp-ops-009", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 2, "type": "mcq",
        "stem": "In the final phase of incident management, the team meets to analyze what happened, how "
                "well the response worked, and what to improve. What is the PRIMARY goal of this phase?",
        "options": [
            {"id": "A", "text": "To assign blame to the individuals involved"},
            {"id": "B", "text": "To immediately restore affected systems to production"},
            {"id": "C", "text": "To capture lessons learned and improve future response and controls"},
            {"id": "D", "text": "To collect volatile memory from the attacker's machine"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The lessons-learned (post-incident review) phase exists to improve processes, "
                       "controls, and future response based on what the incident revealed.",
            "distractors": {
                "A": "The review is for improvement, not assigning blame.",
                "B": "Restoring systems is the recovery phase, which precedes lessons learned.",
                "D": "Collecting volatile memory is part of early evidence gathering, not the post-incident review.",
            },
            "exam_pattern": "Lessons learned improves processes and controls - a no-blame, forward-looking review.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Lessons learned"],
    },
    {
        "id": "cissp-ops-010", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In the (ISC)² incident management process, the phase that addresses "
                "the underlying root cause so the same incident does not recur - for example, patching the "
                "exploited flaw or correcting a misconfiguration - is called ________ (give the phase name).",
        "correct": ["remediation", "remediate"],
        "explanation": {
            "correct": "Remediation addresses the root cause (patching, reconfiguration) so the incident does "
                       "not happen again; it follows recovery and precedes lessons learned.",
            "exam_pattern": "Remediation fixes the root cause to prevent recurrence (recovery restores; remediation prevents).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Remediation"],
    },

    # ===== cissp_dr_recovery ================================================
    {
        "id": "cissp-ops-011", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a disk array that stripes data across at least three drives with "
                "distributed parity, so the array keeps operating if ANY single drive fails. Which RAID "
                "level provides this?",
        "options": [
            {"id": "A", "text": "RAID 0 (striping, no parity)"},
            {"id": "B", "text": "A single disk with no redundancy"},
            {"id": "C", "text": "JBOD (just a bunch of disks)"},
            {"id": "D", "text": "RAID 5 (striping with distributed parity)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "RAID 5 stripes data with distributed parity across three or more drives and can "
                       "tolerate the failure of any single drive.",
            "distractors": {
                "A": "RAID 0 stripes with no parity, so one drive failure loses all data.",
                "B": "A single disk provides no redundancy at all.",
                "C": "JBOD simply concatenates disks with no parity or fault tolerance.",
            },
            "exam_pattern": "Striping with distributed parity surviving one drive failure = RAID 5 (RAID 6 survives two).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - RAID and fault tolerance"],
    },
    {
        "id": "cissp-ops-012", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A company runs a full backup every Sunday and a differential backup each weekday "
                "evening. If a failure occurs Thursday morning, which backups are needed to fully restore "
                "the data?",
        "options": [
            {"id": "A", "text": "Every daily backup from Monday through Wednesday, plus Sunday's full"},
            {"id": "B", "text": "Sunday's full backup plus only Wednesday's differential backup"},
            {"id": "C", "text": "Only Wednesday's differential backup"},
            {"id": "D", "text": "Only Sunday's full backup"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A differential backup captures all changes since the last full backup, so a full "
                       "restore needs only the last full plus the single most recent (Wednesday) differential.",
            "distractors": {
                "A": "Needing every daily backup describes an incremental scheme, not a differential one.",
                "C": "The differential alone omits the baseline full backup.",
                "D": "The full alone omits every change made since Sunday.",
            },
            "exam_pattern": "Full + differential restore = last full + the single most recent differential.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Backup strategies"],
    },
    {
        "id": "cissp-ops-013", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants the MOST thorough disaster-recovery test, in which production is "
                "actually shut down and operations are shifted to the recovery site to prove the plan "
                "truly works. Which test type is this, and what is its main drawback?",
        "options": [
            {"id": "A", "text": "Full-interruption test; it is the most disruptive and highest-risk because real operations stop"},
            {"id": "B", "text": "Checklist (read-through) review; it carries the most operational risk"},
            {"id": "C", "text": "Tabletop (structured walk-through); it fully exercises live failover"},
            {"id": "D", "text": "Parallel test; it requires shutting production down"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A full-interruption test actually halts production and fails over to the recovery "
                       "site - the most thorough test, but also the most disruptive and risky.",
            "distractors": {
                "B": "A checklist review is the least disruptive test, not the most.",
                "C": "A tabletop exercise discusses the plan and does not perform an actual failover.",
                "D": "A parallel test brings the recovery site up alongside production without shutting production down.",
            },
            "exam_pattern": "Full-interruption = most thorough and most disruptive (production stops); parallel runs "
                            "recovery alongside production.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - DR testing types"],
    },

    {
        "id": "cissp-ops-017", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The backup type that captures all data changed since the last FULL "
                "backup - so a restore needs only the last full backup plus the single most recent one of "
                "these - is a ________ backup.",
        "correct": ["differential"],
        "explanation": {
            "correct": "A differential backup copies everything changed since the last full backup; restoring "
                       "requires only the last full plus the most recent differential.",
            "exam_pattern": "Differential = changes since last full (restore = full + latest differential); "
                            "incremental = changes since last backup of any kind.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Backup types"],
    },

    # ===== cissp_change_config_mgmt =========================================
    {
        "id": "cissp-ops-014", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_change_config_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "A systems engineer wants to deploy a configuration change to a production server. "
                "Following sound change management, what should happen BEFORE the change is implemented?",
        "options": [
            {"id": "A", "text": "The change should be made immediately, then documented if there is time"},
            {"id": "B", "text": "The engineer should implement it and let the change advisory board review it next quarter"},
            {"id": "C", "text": "The change should be requested, assessed, tested, and formally approved (e.g., by a change advisory board), with a rollback plan"},
            {"id": "D", "text": "The server should be rebuilt from scratch to avoid paperwork"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Change management requires that a change be requested, assessed for impact, tested, and "
                       "formally approved (often by a change advisory board) with a rollback plan before it "
                       "reaches production.",
            "distractors": {
                "A": "Making changes first undermines the control and risks unreviewed impact.",
                "B": "After-the-fact review defeats the purpose of pre-implementation approval (outside true emergencies).",
                "D": "Rebuilding the server is unnecessary and still skips change control.",
            },
            "exam_pattern": "Change management = request → assess/test → approve (CAB) with rollback BEFORE implementing.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Change management"],
    },
    {
        "id": "cissp-ops-015", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_change_config_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to establish and maintain an approved, documented standard "
                "configuration for its servers so that any unauthorized deviation can be detected. Which "
                "discipline provides this?",
        "options": [
            {"id": "A", "text": "Configuration management (baselining)"},
            {"id": "B", "text": "Incident response"},
            {"id": "C", "text": "Penetration testing"},
            {"id": "D", "text": "Business impact analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Configuration management establishes and maintains approved baselines and tracks "
                       "configuration items, so drift and unauthorized changes can be detected.",
            "distractors": {
                "B": "Incident response handles events after they occur, not configuration baselining.",
                "C": "Penetration testing probes for exploitable weaknesses, not configuration standardization.",
                "D": "A BIA identifies critical functions and impacts, not configuration control.",
            },
            "exam_pattern": "Establishing/maintaining approved baselines to detect drift = configuration management.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Configuration management"],
    },
    {
        "id": "cissp-ops-016", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_change_config_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "A critical production outage requires an urgent fix outside the normal change schedule. "
                "How should a mature change-management process handle this emergency change?",
        "options": [
            {"id": "A", "text": "Prohibit it entirely because it was not pre-approved"},
            {"id": "B", "text": "Allow an expedited emergency change, then document it and submit it for retrospective review and approval"},
            {"id": "C", "text": "Implement it and never record it, to keep the change log clean"},
            {"id": "D", "text": "Wait for the next quarterly change window regardless of impact"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mature processes include an emergency-change path: act quickly to restore service, but "
                       "still document the change and submit it for retrospective review and approval.",
            "distractors": {
                "A": "Forbidding all emergency changes would prolong critical outages.",
                "C": "Failing to record the change destroys the audit trail and configuration accuracy.",
                "D": "Waiting through a critical outage causes unacceptable business impact.",
            },
            "exam_pattern": "Emergency changes use an expedited path but are still documented and reviewed retrospectively.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Emergency change management"],
    },
]
