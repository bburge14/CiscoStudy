"""Cisco CyberOps Associate (CBROPS 200-201) pool - Domain 5: Security Policies and Procedures.

Original, objective-aligned practice items for the five Security Policies and
Procedures subtopics tracked in CertLab:
  * cbr_incident_handling_nist - the NIST SP 800-61 incident response life cycle
                                phases and their order.
  * cbr_attack_frameworks      - the Cyber Kill Chain stages and the Diamond
                                Model of intrusion analysis.
  * cbr_chain_of_custody       - chain of custody, order of volatility, data
                                integrity and evidence preservation (NIST SP 800-86).
  * cbr_csirt_metrics          - the CSIRT role and SOC metrics such as time to
                                detect, contain and respond.
  * cbr_runbook_automation     - playbooks/runbooks and run book automation in
                                incident response.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item cites the public Cisco 200-201 exam topic it draws on. Blue-team /
analyst depth only, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cbr_incident_handling_nist =======================================
    {
        "id": "cbrops-pol-001", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "What is the correct order of the four phases of the incident response life cycle as "
                "defined in NIST SP 800-61?",
        "options": [
            {"id": "A", "text": "Preparation; Detection and Analysis; Containment, Eradication and Recovery; Post-Incident Activity"},
            {"id": "B", "text": "Detection and Analysis; Preparation; Recovery; Containment"},
            {"id": "C", "text": "Containment; Preparation; Detection; Lessons Learned"},
            {"id": "D", "text": "Preparation; Containment; Detection and Analysis; Eradication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NIST SP 800-61 defines the life cycle as Preparation; Detection and Analysis; "
                       "Containment, Eradication and Recovery; and Post-Incident Activity (lessons learned), in that order.",
            "distractors": {
                "B": "Preparation comes first, before detection; this ordering is scrambled.",
                "C": "Containment cannot precede Preparation and Detection; the sequence is wrong.",
                "D": "Detection and Analysis must precede Containment; you cannot contain what you have not detected.",
            },
            "exam_pattern": "NIST 800-61: Prepare -> Detect & Analyze -> Contain/Eradicate/Recover -> Post-Incident.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.4 Map elements to the steps of analysis based on NIST SP 800-61"],
    },
    {
        "id": "cbrops-pol-002", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "After confirming an endpoint is infected and spreading, the responder disconnects it "
                "from the network to stop the malware reaching other hosts. Into which NIST SP 800-61 "
                "phase does this action fall?",
        "options": [
            {"id": "A", "text": "Containment, Eradication and Recovery"},
            {"id": "B", "text": "Preparation"},
            {"id": "C", "text": "Detection and Analysis"},
            {"id": "D", "text": "Post-Incident Activity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Isolating an affected system to limit the spread of damage is a containment action, "
                       "part of the Containment, Eradication and Recovery phase.",
            "distractors": {
                "B": "Preparation is the before-the-incident readiness work (tooling, training), not isolating a live host.",
                "C": "Detection and Analysis is identifying and scoping the incident, which has already happened here.",
                "D": "Post-Incident Activity is the later lessons-learned review, not the immediate isolation step.",
            },
            "exam_pattern": "Isolate/limit spread of an active incident = Containment (within Containment/Eradication/Recovery).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.3 Apply the incident handling process (NIST SP 800-61) to an event"],
    },
    {
        "id": "cbrops-pol-003", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "After an incident is fully resolved, the team holds a review to document what happened, "
                "what worked, and how to improve detection and response next time. Which NIST SP 800-61 "
                "phase is this?",
        "options": [
            {"id": "A", "text": "Post-Incident Activity (lessons learned)"},
            {"id": "B", "text": "Detection and Analysis"},
            {"id": "C", "text": "Containment, Eradication and Recovery"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Post-Incident Activity phase captures lessons learned - what happened, how the "
                       "response went, and improvements to feed back into preparation and detection.",
            "distractors": {
                "B": "Detection and Analysis is identifying and validating the incident, which occurs much earlier.",
                "C": "Containment, Eradication and Recovery handles the active response, before the retrospective.",
                "D": "Preparation is the readiness work before an incident; the review afterward feeds into it but is a separate, final phase.",
            },
            "exam_pattern": "Retrospective / lessons learned after resolution = Post-Incident Activity.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.4 Map elements to the steps of analysis based on NIST SP 800-61"],
    },
    {
        "id": "cbrops-pol-004", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The first phase of the NIST SP 800-61 incident response life cycle - "
                "which includes building the CSIRT, acquiring tools, and training staff before any "
                "incident occurs - is called ______.",
        "correct": ["preparation", "the preparation phase", "prepare"],
        "explanation": {
            "correct": "Preparation is the first phase: establishing the team, tooling, policies, and "
                       "training so the organization is ready to respond before an incident ever happens.",
            "exam_pattern": "Readiness before any incident (team, tools, training) = Preparation (phase 1).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.2 Describe the elements in an incident response plan (NIST SP 800-61)"],
    },

    # ===== cbr_attack_frameworks ============================================
    {
        "id": "cbrops-pol-005", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "An adversary emails a weaponized PDF to a targeted employee in hopes they will open it. "
                "Which stage of the Lockheed Martin Cyber Kill Chain does sending that email represent?",
        "options": [
            {"id": "A", "text": "Delivery"},
            {"id": "B", "text": "Reconnaissance"},
            {"id": "C", "text": "Installation"},
            {"id": "D", "text": "Actions on Objectives"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Delivery is the stage where the weaponized payload is transmitted to the target - for "
                       "example, emailing a malicious attachment or link.",
            "distractors": {
                "B": "Reconnaissance is the earlier research/target-selection stage, before any payload is sent.",
                "C": "Installation is when malware installs itself on the victim after successful exploitation.",
                "D": "Actions on Objectives is the final stage where the attacker achieves their goal (e.g., exfiltration).",
            },
            "exam_pattern": "Transmitting the payload to the victim (email/USB/link) = Delivery.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-006", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "The Diamond Model of Intrusion Analysis represents every intrusion event with four core "
                "interconnected features. Which set lists those four features?",
        "options": [
            {"id": "A", "text": "Adversary, Capability, Infrastructure, Victim"},
            {"id": "B", "text": "People, Process, Technology, Governance"},
            {"id": "C", "text": "Confidentiality, Integrity, Availability, Authentication"},
            {"id": "D", "text": "Preparation, Detection, Containment, Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Diamond Model's four core features are Adversary, Capability, Infrastructure, and "
                       "Victim, connected to show how an attacker uses capabilities over infrastructure against a victim.",
            "distractors": {
                "B": "People/Process/Technology/Governance is a general operating-model framing, not the Diamond Model.",
                "C": "Those are CIA-triad and authentication concepts, not Diamond Model vertices.",
                "D": "Those are incident-response phases (NIST 800-61), not the Diamond Model features.",
            },
            "exam_pattern": "Diamond Model vertices = Adversary, Capability, Infrastructure, Victim.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-007", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "After installing itself, malware opens a persistent channel back to an attacker-"
                "controlled server to receive further instructions. Which Cyber Kill Chain stage does "
                "this represent?",
        "options": [
            {"id": "A", "text": "Command and Control (C2)"},
            {"id": "B", "text": "Weaponization"},
            {"id": "C", "text": "Delivery"},
            {"id": "D", "text": "Reconnaissance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Command and Control (C2) is the stage where compromised hosts establish a channel to "
                       "the attacker's infrastructure so the adversary can issue remote instructions.",
            "distractors": {
                "B": "Weaponization is building the payload (coupling an exploit with a backdoor) before delivery.",
                "C": "Delivery is transmitting the payload to the target, which has already occurred here.",
                "D": "Reconnaissance is the initial research stage, long before a C2 channel exists.",
            },
            "exam_pattern": "Channel back to the attacker for remote instructions = Command and Control (C2).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-008", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 1, "type": "mcq",
        "stem": "Which stage of the Cyber Kill Chain involves the adversary researching and selecting "
                "targets - for example, harvesting employee email addresses and identifying exposed "
                "services - before any payload is built?",
        "options": [
            {"id": "A", "text": "Reconnaissance"},
            {"id": "B", "text": "Exploitation"},
            {"id": "C", "text": "Installation"},
            {"id": "D", "text": "Command and Control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reconnaissance is the first Kill Chain stage: the attacker gathers information and "
                       "selects targets before weaponizing or delivering anything.",
            "distractors": {
                "B": "Exploitation is triggering the vulnerability on the target, which comes after delivery.",
                "C": "Installation places malware on the victim after successful exploitation.",
                "D": "Command and Control is establishing remote control, a later stage still.",
            },
            "exam_pattern": "Research and target selection first = Reconnaissance.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },

    # ===== cbr_chain_of_custody =============================================
    {
        "id": "cbrops-pol-009", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The chronological documentation that records every person who "
                "collected, handled, or transferred a piece of evidence - preserving its integrity and "
                "legal admissibility - is called the ______ ______ (three words including 'of').",
        "correct": ["chain of custody", "the chain of custody"],
        "explanation": {
            "correct": "The chain of custody documents the seizure, custody, control, transfer, and handling "
                       "of evidence over time, demonstrating it was not altered and keeping it admissible.",
            "exam_pattern": "Who handled evidence, when, and how, documented end to end = chain of custody.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.3 Describe the role of attribution in an investigation (chain of custody)"],
    },
    {
        "id": "cbrops-pol-010", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 2, "type": "mcq",
        "stem": "Following the order of volatility from NIST SP 800-86 when collecting evidence from a "
                "live system, which data should an analyst capture first?",
        "options": [
            {"id": "A", "text": "Volatile data such as the contents of RAM and active network connections"},
            {"id": "B", "text": "Files archived on offline backup tapes"},
            {"id": "C", "text": "Data written to an optical disc in a drawer"},
            {"id": "D", "text": "Printed documents in a filing cabinet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The order of volatility says to collect the most volatile data first - CPU/registers, "
                       "then RAM and live network state - because it disappears when the system is powered down.",
            "distractors": {
                "B": "Backup tapes are highly non-volatile and are collected much later, not first.",
                "C": "An optical disc is stable, persistent storage; it is low on the volatility order.",
                "D": "Printed documents do not change when the system is powered off and are not volatile data.",
            },
            "exam_pattern": "Collect most volatile first: registers/cache -> RAM/network state -> disk -> backups.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.6 Describe concepts as documented in NIST SP 800-86"],
    },
    {
        "id": "cbrops-pol-011", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 2, "type": "mcq",
        "stem": "To prove that a seized disk image has not been altered between acquisition and analysis, "
                "an analyst computes a cryptographic hash at collection and again later and compares the "
                "two values. What property is this technique verifying?",
        "options": [
            {"id": "A", "text": "Data integrity"},
            {"id": "B", "text": "Data confidentiality"},
            {"id": "C", "text": "Network availability"},
            {"id": "D", "text": "User non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matching hash values before and after demonstrate the evidence is unchanged, which "
                       "verifies its integrity and supports admissibility.",
            "distractors": {
                "B": "Confidentiality is about preventing disclosure; hashing here proves the data was not altered, not that it was kept secret.",
                "C": "Availability concerns access to systems/data, not whether an image was modified.",
                "D": "Non-repudiation ties an action to an identity; the hash comparison here is about integrity of the image.",
            },
            "exam_pattern": "Hash at collection = hash later -> evidence unchanged = data integrity.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.6 Describe concepts as documented in NIST SP 800-86"],
    },
    {
        "id": "cbrops-pol-012", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 3, "type": "mcq",
        "stem": "A responder arrives at a running, compromised workstation that holds active malware in "
                "memory. To preserve the most evidence, what should they generally do before powering the "
                "machine off?",
        "options": [
            {"id": "A", "text": "Capture a memory (RAM) image and other volatile data first"},
            {"id": "B", "text": "Immediately pull the power cord to 'freeze' the disk"},
            {"id": "C", "text": "Reboot the machine to clear the malware"},
            {"id": "D", "text": "Run a full antivirus clean before collecting anything"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Volatile data such as RAM, running processes, and network connections is lost at "
                       "shutdown, so capturing a memory image first preserves evidence (like in-memory malware) that disk forensics would miss.",
            "distractors": {
                "B": "Pulling power destroys all volatile memory evidence before it can be captured.",
                "C": "Rebooting wipes volatile state and may alter the disk, destroying evidence.",
                "D": "Running an AV clean modifies the system and can delete the very artifacts needed as evidence.",
            },
            "exam_pattern": "Live system: collect volatile memory/state before shutdown (order of volatility).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.6 Describe concepts as documented in NIST SP 800-86"],
    },

    # ===== cbr_csirt_metrics ================================================
    {
        "id": "cbrops-pol-013", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A SOC manager wants a metric for the average elapsed time between when an intrusion "
                "actually begins and when the SOC first detects it. Which metric is this?",
        "options": [
            {"id": "A", "text": "Mean time to detect (MTTD)"},
            {"id": "B", "text": "Mean time to contain"},
            {"id": "C", "text": "Mean time between failures (MTBF)"},
            {"id": "D", "text": "Annual loss expectancy (ALE)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mean time to detect (MTTD) measures how long, on average, it takes the SOC to notice "
                       "an incident after it starts; lowering it shrinks the attacker's dwell time.",
            "distractors": {
                "B": "Time to contain measures how long to stop the incident spreading after detection, a later stage.",
                "C": "MTBF is a hardware/reliability metric, not a detection-speed metric.",
                "D": "ALE is a quantitative risk figure (expected yearly loss), not a detection-time metric.",
            },
            "exam_pattern": "Time from compromise to detection = MTTD (mean time to detect).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.11 Describe the relationship of SOC metrics to scope analysis"],
    },
    {
        "id": "cbrops-pol-014", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 2, "type": "mcq",
        "stem": "Which SOC metric specifically tracks how long it takes, after an incident is detected, "
                "to stop it from spreading further to additional systems?",
        "options": [
            {"id": "A", "text": "Time to contain"},
            {"id": "B", "text": "Time to detect"},
            {"id": "C", "text": "Time to onboard a new analyst"},
            {"id": "D", "text": "Certificate validity period"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Time to contain measures the interval from detection to successfully halting the "
                       "incident's spread, limiting its blast radius.",
            "distractors": {
                "B": "Time to detect measures finding the incident, not stopping its spread afterward.",
                "C": "Analyst onboarding time is a staffing metric, not an incident-response timing metric.",
                "D": "A certificate validity period is a PKI attribute, unrelated to incident containment speed.",
            },
            "exam_pattern": "Detection -> stop the spread interval = time to contain.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.11 Describe the relationship of SOC metrics to scope analysis"],
    },
    {
        "id": "cbrops-pol-015", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary function of a Computer Security Incident Response Team (CSIRT) "
                "within an organization?",
        "options": [
            {"id": "A", "text": "To receive, triage, and respond to reported security incidents"},
            {"id": "B", "text": "To design the company's marketing campaigns"},
            {"id": "C", "text": "To issue and sign TLS certificates for the organization"},
            {"id": "D", "text": "To manage employee payroll and benefits"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CSIRT is the designated team that receives incident reports, triages and "
                       "investigates them, and coordinates the response and recovery.",
            "distractors": {
                "B": "Marketing is unrelated to incident response.",
                "C": "Issuing certificates is a PKI/CA function, not the CSIRT's role.",
                "D": "Payroll and benefits are HR functions, not incident response.",
            },
            "exam_pattern": "Team that receives, triages, and responds to incidents = CSIRT.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.5 Map the organization stakeholders against the NIST IR categories"],
    },

    # ===== cbr_runbook_automation ===========================================
    {
        "id": "cbrops-pol-016", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_runbook_automation", "difficulty": 2, "type": "mcq",
        "stem": "In SOC operations, what is a 'playbook' (also called a runbook)?",
        "options": [
            {"id": "A", "text": "A documented, repeatable set of steps for responding to a specific type of incident"},
            {"id": "B", "text": "A hardware appliance that blocks malware inline"},
            {"id": "C", "text": "A legal record of how evidence was handled"},
            {"id": "D", "text": "A database of every user's stored credentials"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A playbook/runbook is a documented, repeatable procedure that tells analysts exactly "
                       "how to handle a given alert or incident type, ensuring consistent and faster response.",
            "distractors": {
                "B": "A hardware appliance that blocks malware is an IPS/firewall, not a documented procedure.",
                "C": "A record of evidence handling is the chain of custody, not a response playbook.",
                "D": "A credential database is an identity store, unrelated to a response procedure.",
            },
            "exam_pattern": "Documented repeatable response steps for an incident type = playbook/runbook.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.3 Apply the incident handling process (NIST SP 800-61) to an event"],
    },
    {
        "id": "cbrops-pol-017", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_runbook_automation", "difficulty": 2, "type": "mcq",
        "stem": "What is the main benefit of run book automation (RBA) for a security operations center?",
        "options": [
            {"id": "A", "text": "It automates repetitive response tasks, reducing response time and human error"},
            {"id": "B", "text": "It guarantees that no incident will ever occur"},
            {"id": "C", "text": "It replaces the need to log any security events"},
            {"id": "D", "text": "It encrypts all of the organization's data at rest"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Run book automation executes routine, well-defined response steps automatically, so "
                       "analysts respond faster and more consistently and are freed for higher-value analysis.",
            "distractors": {
                "B": "Automation speeds response; it cannot guarantee incidents never happen.",
                "C": "Automation relies on logs and telemetry; it does not remove the need to log events.",
                "D": "Encrypting data at rest is a separate data-protection control, not the purpose of RBA.",
            },
            "exam_pattern": "Automate routine response steps -> faster, consistent response, fewer errors = RBA.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms (run book automation)"],
    },
    {
        "id": "cbrops-pol-018", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_runbook_automation", "difficulty": 3, "type": "mcq",
        "stem": "A SOC implements a SOAR playbook for phishing reports that automatically extracts URLs "
                "and attachments, detonates them in a sandbox, enriches any indicators with threat "
                "intelligence, and opens a ticket - escalating to an analyst only if something malicious "
                "is found. What is the main advantage of handling phishing this way?",
        "options": [
            {"id": "A", "text": "It handles routine triage consistently and quickly, so analysts focus on confirmed threats"},
            {"id": "B", "text": "It removes the need for any human analyst involvement at all"},
            {"id": "C", "text": "It makes the organization immune to phishing"},
            {"id": "D", "text": "It permanently stops all email delivery to users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automated playbooks perform repetitive triage and enrichment consistently and fast, "
                       "escalating only true positives, which cuts response time and analyst workload.",
            "distractors": {
                "B": "The playbook still escalates confirmed threats to analysts; it augments, not eliminates, human judgment.",
                "C": "Automation improves response but cannot make an organization immune to phishing.",
                "D": "A triage playbook does not, and should not, halt all email delivery to users.",
            },
            "exam_pattern": "SOAR playbook = consistent, fast automated triage/enrichment; humans handle confirmed threats.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.3 Apply the incident handling process (NIST SP 800-61) to an event"],
    },
]
