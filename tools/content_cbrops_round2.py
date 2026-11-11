"""Cisco CyberOps Associate (CBROPS 200-201) pool - ROUND 2 deepening expansion.

~110 original, objective-aligned practice items that DEEPEN the round-1 banks
(content_cbrops_concepts/monitoring/host/intrusion/policies, 90 items) without
duplicating them. Every item here attacks a different fact, scenario, or angle
than round 1, and is distributed by exam weight (monitoring 25%, concepts/host/
intrusion 20% each, policies 15%).

Ids use the `cbrops-<prefix>-r2-NNN` scheme (con/mon/host/intr/pol) so they never
collide with round-1 ids. Schema is identical to the other content_*.py pools:
build_content.py shuffles the A/B/C/D order (seeded by id), so a key authored
here is not positionally biased; every wrong option carries a distractor note;
fill items list all accepted answers; and each item cites the public Cisco
200-201 exam topic it draws on. Blue-team / SOC-analyst depth only - defensive,
monitoring-focused, no offensive payloads, and never real or memorized exam items.

High-risk facts (CVSS v3.1 metrics and bands, Windows Event IDs 4624/4625/4688/
4672/7045/1102, protocol header fields and numbers, ICMP types, NIST SP 800-61
phases, Kill Chain stages, Diamond Model, VERIS) were web-verified during authoring.
"""

QUESTIONS = [
    # ========================================================================
    # DOMAIN 1: cbr_security_concepts (22)
    # ========================================================================

    # ===== cbr_cia_defense ==================================================
    {
        "id": "cbrops-con-r2-001", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 1, "type": "mcq",
        "stem": "An attacker copies a database of customer records and posts it on a public forum. No "
                "records were altered and the systems stayed online the whole time. Which pillar of the "
                "CIA triad was violated?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Accounting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Confidentiality is the assurance that data is not disclosed to unauthorized parties; "
                       "copying and publishing private records is a confidentiality (disclosure) breach.",
            "distractors": {
                "B": "Integrity concerns unauthorized modification; the records were read, not changed.",
                "C": "Availability concerns access to systems/data; the systems stayed online throughout.",
                "D": "Accounting is the AAA function of recording actions; it is not a CIA pillar.",
            },
            "exam_pattern": "Data read/stolen/disclosed, nothing changed = Confidentiality.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.1 Describe the CIA triad"],
    },
    {
        "id": "cbrops-con-r2-002", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 2, "type": "mcq",
        "stem": "A security program uses security-awareness training and an acceptable-use policy to "
                "shape user behavior. Which CATEGORY of security control do training and policies belong "
                "to?",
        "options": [
            {"id": "A", "text": "Administrative (managerial) controls"},
            {"id": "B", "text": "Technical (logical) controls"},
            {"id": "C", "text": "Physical controls"},
            {"id": "D", "text": "Cryptographic controls"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Administrative (managerial) controls are policies, procedures, standards, and training "
                       "that govern how people behave; defense in depth layers them with technical and physical controls.",
            "distractors": {
                "B": "Technical/logical controls are enforced by systems (firewalls, encryption, access lists), not written policy.",
                "C": "Physical controls are locks, guards, fences, and cameras that protect facilities and hardware.",
                "D": "'Cryptographic' is a type of technical control, not one of the three primary control categories.",
            },
            "exam_pattern": "Policies, procedures, training = administrative; systems = technical; locks/guards = physical.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.5 Describe the principles of the defense-in-depth strategy"],
    },
    {
        "id": "cbrops-con-r2-003", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 2, "type": "mcq",
        "stem": "To protect the AVAILABILITY of a critical application against hardware failure, which "
                "approach most directly addresses the risk?",
        "options": [
            {"id": "A", "text": "Redundant servers with automatic failover clustering"},
            {"id": "B", "text": "Encrypting the application's data at rest"},
            {"id": "C", "text": "Hashing the application's configuration files"},
            {"id": "D", "text": "Requiring multi-factor authentication to log in"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Redundancy and failover keep a service reachable when a component fails, directly "
                       "supporting availability; backups and load balancing serve the same pillar.",
            "distractors": {
                "B": "Encryption at rest protects confidentiality, not availability during a hardware failure.",
                "C": "Hashing verifies integrity (unchanged files); it does not keep a failed server running.",
                "D": "MFA strengthens authentication/confidentiality of access, not availability.",
            },
            "exam_pattern": "Redundancy / failover / backups / load balancing = availability controls.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.1 Describe the CIA triad"],
    },
    {
        "id": "cbrops-con-r2-004", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The security property that assures a user cannot later deny having "
                "performed an action - supported by digital signatures and detailed logging - is called "
                "______ (one hyphenated term).",
        "correct": ["non-repudiation", "nonrepudiation", "non repudiation"],
        "explanation": {
            "correct": "Non-repudiation binds an action to an identity so the actor cannot credibly deny it; "
                       "digital signatures and tamper-evident logs provide it, extending the core CIA goals.",
            "exam_pattern": "Cannot deny an action was performed (signatures, logging) = non-repudiation.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.1 Describe the CIA triad"],
    },

    # ===== cbr_security_terms ===============================================
    {
        "id": "cbrops-con-r2-005", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 2, "type": "mcq",
        "stem": "A SOC subscribes to a feed of known-malicious IP addresses, domains, and file hashes "
                "enriched with context about active adversary campaigns, and uses it to inform its "
                "detections. What is this feed an example of?",
        "options": [
            {"id": "A", "text": "Threat intelligence"},
            {"id": "B", "text": "Threat hunting"},
            {"id": "C", "text": "Penetration testing"},
            {"id": "D", "text": "A certificate revocation list"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat intelligence is curated, context-rich information about threats and adversaries "
                       "(indicators, TTPs, campaigns) that drives detection, prioritization, and response.",
            "distractors": {
                "B": "Threat hunting is the proactive, hypothesis-driven search through telemetry; intelligence is an input to it, not the activity itself.",
                "C": "Penetration testing is authorized offensive testing, not a feed of indicators.",
                "D": "A CRL lists revoked certificates; it is unrelated to adversary indicator feeds.",
            },
            "exam_pattern": "Curated indicators + adversary context used to inform detection = threat intelligence.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },
    {
        "id": "cbrops-con-r2-006", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 2, "type": "mcq",
        "stem": "How is an advanced persistent threat (APT) best characterized as a type of threat actor?",
        "options": [
            {"id": "A", "text": "A well-resourced, stealthy adversary that maintains long-term, undetected access to meet strategic goals"},
            {"id": "B", "text": "An inexperienced attacker running prebuilt tools without understanding them"},
            {"id": "C", "text": "An automated vulnerability scanner with no human operator"},
            {"id": "D", "text": "A one-time opportunistic smash-and-grab with no persistence"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An APT is a sophisticated, often state-sponsored or organized actor with significant "
                       "resources that establishes persistent, low-and-slow access for espionage or sabotage over long periods.",
            "distractors": {
                "B": "That describes a 'script kiddie', the opposite of an APT's sophistication.",
                "C": "A scanner is a tool, not a threat actor; an APT is a human-directed adversary.",
                "D": "APTs are defined by long-term persistence, not opportunistic one-off intrusions.",
            },
            "exam_pattern": "Well-resourced, stealthy, persistent, strategic adversary = APT.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },
    {
        "id": "cbrops-con-r2-007", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Deconstructing a malware sample to understand its design and behavior "
                "- for example by disassembling or decompiling the binary - is known as ______ "
                "______ (two words).",
        "correct": ["reverse engineering", "reverse-engineering"],
        "explanation": {
            "correct": "Reverse engineering analyzes compiled code (via disassembly/decompilation) to reveal "
                       "how malware works, what it targets, and what indicators it leaves, informing detection and response.",
            "exam_pattern": "Take software/malware apart to learn how it works = reverse engineering.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },

    # ===== cbr_access_control_models ========================================
    {
        "id": "cbrops-con-r2-008", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "In the AAA framework, which component records WHAT an authenticated user did - commands "
                "entered, resources accessed, and session duration - for auditing and billing?",
        "options": [
            {"id": "A", "text": "Accounting"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "Attestation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Accounting is the AAA function that tracks and logs user activity and resource "
                       "consumption, producing the audit trail analysts rely on.",
            "distractors": {
                "B": "Authentication verifies who the user is (identity proofing), before any activity is logged.",
                "C": "Authorization decides what an authenticated user is permitted to do.",
                "D": "Attestation is evidence that a system is in a known-good state; it is not part of AAA.",
            },
            "exam_pattern": "AAA: Authentication = who you are, Authorization = what you may do, Accounting = what you did.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },
    {
        "id": "cbrops-con-r2-009", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "A firewall enforces an administrator-defined global rule that denies a particular "
                "protocol for everyone, applied uniformly regardless of the user's identity or the "
                "resource owner. Which access control model is this?",
        "options": [
            {"id": "A", "text": "Rule-based access control"},
            {"id": "B", "text": "Discretionary access control (DAC)"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "Mandatory access control (MAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Rule-based access control applies administrator-defined rules uniformly to all subjects "
                       "(classic example: a firewall/ACL), independent of individual identity or ownership.",
            "distractors": {
                "B": "DAC lets the resource owner decide access at their discretion - not a global rule for all.",
                "C": "RBAC grants access by the user's job role, not a single rule applied to everyone.",
                "D": "MAC enforces access by security labels and clearances, not administrator firewall-style rules.",
            },
            "exam_pattern": "Admin-defined rules applied to everyone regardless of identity = rule-based access control.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },
    {
        "id": "cbrops-con-r2-010", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "Contractors may authenticate and access systems only between 09:00 and 17:00 on "
                "weekdays; outside that window their access is automatically denied. Which access control "
                "model is in use?",
        "options": [
            {"id": "A", "text": "Time-based access control"},
            {"id": "B", "text": "Role-based access control (RBAC)"},
            {"id": "C", "text": "Discretionary access control (DAC)"},
            {"id": "D", "text": "Mandatory access control (MAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Time-based access control permits or denies access according to time windows, so the "
                       "same identity is allowed only during approved hours.",
            "distractors": {
                "B": "RBAC decides access by job role, not by time of day.",
                "C": "DAC leaves access to the owner's discretion, not a schedule.",
                "D": "MAC uses labels and clearances; it does not key access to the clock.",
            },
            "exam_pattern": "Access allowed only during defined hours/windows = time-based access control.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },
    {
        "id": "cbrops-con-r2-011", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "A login requires a password (something you know) AND a fingerprint (something you are). "
                "Using two DIFFERENT factor categories like this is known as:",
        "options": [
            {"id": "A", "text": "Multi-factor authentication (MFA)"},
            {"id": "B", "text": "Single sign-on (SSO)"},
            {"id": "C", "text": "Two passwords (same-factor) authentication"},
            {"id": "D", "text": "Federated identity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MFA combines factors from two or more distinct categories - knowledge (know), "
                       "possession (have), and inherence (are) - so a stolen password alone is not enough to log in.",
            "distractors": {
                "B": "SSO lets one authentication grant access to many systems; it is not about combining factor types.",
                "C": "Two passwords are both the 'something you know' factor, so that is single-factor, not MFA.",
                "D": "Federated identity shares authentication across organizations/domains; it is not the definition of MFA.",
            },
            "exam_pattern": "Two or more DIFFERENT factor categories (know/have/are) = MFA.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },

    # ===== cbr_cvss =========================================================
    {
        "id": "cbrops-con-r2-012", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "In CVSS v3.1, which base metric describes conditions beyond the attacker's control that "
                "must exist for exploitation, and takes the values Low and High?",
        "options": [
            {"id": "A", "text": "Attack Complexity (AC)"},
            {"id": "B", "text": "Privileges Required (PR)"},
            {"id": "C", "text": "User Interaction (UI)"},
            {"id": "D", "text": "Attack Vector (AV)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Attack Complexity (Low/High) reflects conditions outside the attacker's control (such "
                       "as a required race condition or specific configuration); High AC means exploitation is harder.",
            "distractors": {
                "B": "Privileges Required is the privilege level the attacker must already hold (None/Low/High).",
                "C": "User Interaction states whether a human victim must act (None/Required).",
                "D": "Attack Vector is where the attack originates (Network/Adjacent/Local/Physical).",
            },
            "exam_pattern": "Conditions beyond attacker control, values Low/High = Attack Complexity.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-r2-013", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "A CVSS v3.1 assessment notes that the attacker must already possess valid low-level "
                "account access on the target before the flaw can be exploited. Which base metric captures "
                "this, using the values None, Low, and High?",
        "options": [
            {"id": "A", "text": "Privileges Required (PR)"},
            {"id": "B", "text": "Attack Complexity (AC)"},
            {"id": "C", "text": "User Interaction (UI)"},
            {"id": "D", "text": "Scope (S)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Privileges Required (None/Low/High) captures the level of access an attacker must "
                       "already hold before exploiting the vulnerability; needing an account sets PR to Low.",
            "distractors": {
                "B": "Attack Complexity describes external conditions (Low/High), not the attacker's starting privilege.",
                "C": "User Interaction is whether a separate victim must participate (None/Required).",
                "D": "Scope is whether impact crosses a security authority boundary (Unchanged/Changed).",
            },
            "exam_pattern": "Privilege the attacker must already have (None/Low/High) = Privileges Required.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-r2-014", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability can only be exploited if a victim opens a malicious document. Which CVSS "
                "v3.1 base metric reflects this requirement, with the values None and Required?",
        "options": [
            {"id": "A", "text": "User Interaction (UI)"},
            {"id": "B", "text": "Privileges Required (PR)"},
            {"id": "C", "text": "Attack Vector (AV)"},
            {"id": "D", "text": "Availability (A)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "User Interaction (None/Required) indicates whether a human other than the attacker "
                       "must take an action (such as opening a file) for exploitation to succeed.",
            "distractors": {
                "B": "Privileges Required is the attacker's own starting privilege level, not a victim's action.",
                "C": "Attack Vector is the context/distance of the attack (Network/Adjacent/Local/Physical).",
                "D": "Availability is an impact metric (effect on uptime), not whether a user must interact.",
            },
            "exam_pattern": "A victim must act (open/click) for exploit, values None/Required = User Interaction.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-r2-015", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability is published with a CVSS v3.1 base score of 5.4. Into which qualitative "
                "severity rating does that score fall?",
        "options": [
            {"id": "A", "text": "Medium"},
            {"id": "B", "text": "Low"},
            {"id": "C", "text": "High"},
            {"id": "D", "text": "Critical"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On the CVSS v3.1 scale, 4.0-6.9 is Medium, so a 5.4 base score is Medium severity.",
            "distractors": {
                "B": "Low is 0.1-3.9, below 5.4.",
                "C": "High is 7.0-8.9, above 5.4.",
                "D": "Critical is 9.0-10.0, far above 5.4.",
            },
            "exam_pattern": "CVSS v3.1 bands: 0.0 None, 0.1-3.9 Low, 4.0-6.9 Medium, 7.0-8.9 High, 9.0-10.0 Critical.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-r2-016", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 3, "type": "mcq",
        "stem": "Beyond the Base metric group, CVSS v3.1 defines optional groups. Which group adjusts a "
                "score for characteristics that change over TIME, such as whether reliable exploit code or "
                "an official patch now exists?",
        "options": [
            {"id": "A", "text": "Temporal metric group"},
            {"id": "B", "text": "Environmental metric group"},
            {"id": "C", "text": "Base metric group"},
            {"id": "D", "text": "Impact metric group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Temporal group (Exploit Code Maturity, Remediation Level, Report Confidence) "
                       "refines the Base score for factors that evolve over time, like exploit availability and patch status.",
            "distractors": {
                "B": "The Environmental group tailors the score to a specific organization's context (asset criticality, modified base metrics), not the passage of time.",
                "C": "The Base group captures intrinsic, constant characteristics of the vulnerability itself.",
                "D": "There is no separate 'Impact' group; Confidentiality/Integrity/Availability impacts live inside the Base group.",
            },
            "exam_pattern": "Changes over time (exploit maturity, remediation level, report confidence) = Temporal group.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },

    # ===== cbr_risk_terms ===================================================
    {
        "id": "cbrops-con-r2-017", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 1, "type": "mcq",
        "stem": "Which term best describes any circumstance, agent, or event with the POTENTIAL to "
                "adversely affect an asset - for example a hurricane, a malicious insider, or a new strain "
                "of malware?",
        "options": [
            {"id": "A", "text": "Threat"},
            {"id": "B", "text": "Vulnerability"},
            {"id": "C", "text": "Risk"},
            {"id": "D", "text": "Exploit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A threat is any potential danger - an actor or event - that could exploit a weakness "
                       "and cause harm to an asset.",
            "distractors": {
                "B": "A vulnerability is the weakness that a threat could act upon, not the danger itself.",
                "C": "Risk is the potential for loss when a threat exploits a vulnerability (likelihood x impact).",
                "D": "An exploit is the specific tool or technique used to leverage a vulnerability.",
            },
            "exam_pattern": "Potential danger / agent or event that could cause harm = threat.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },
    {
        "id": "cbrops-con-r2-018", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 2, "type": "mcq",
        "stem": "An organization patches a vulnerable internet-facing server to lower the likelihood it "
                "is exploited. Which risk-response strategy does patching represent?",
        "options": [
            {"id": "A", "text": "Risk reduction (mitigation)"},
            {"id": "B", "text": "Risk acceptance"},
            {"id": "C", "text": "Risk transfer"},
            {"id": "D", "text": "Risk avoidance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Applying a control (patching) to lower the likelihood or impact of a risk is risk "
                       "reduction, also called mitigation.",
            "distractors": {
                "B": "Risk acceptance means knowingly taking no action and tolerating the risk - the opposite of patching.",
                "C": "Risk transfer shifts the impact to a third party (e.g., insurance), not by patching the flaw.",
                "D": "Risk avoidance eliminates the activity/asset entirely (e.g., decommissioning the server), not patching to keep using it.",
            },
            "exam_pattern": "Apply a control to lower likelihood/impact = risk reduction (mitigation).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },
    {
        "id": "cbrops-con-r2-019", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 2, "type": "mcq",
        "stem": "When scoring risk, an analyst commonly combines which TWO factors to estimate the level "
                "of a given risk?",
        "options": [
            {"id": "A", "text": "Likelihood (probability) and impact (consequence)"},
            {"id": "B", "text": "Threat and exploit code maturity"},
            {"id": "C", "text": "CVE identifier and vendor name"},
            {"id": "D", "text": "Confidentiality and integrity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk is typically expressed as a function of likelihood (how probable the event is) and "
                       "impact (how severe the loss would be); both drive prioritization.",
            "distractors": {
                "B": "Exploit code maturity is a CVSS temporal input, not the two core risk-scoring factors.",
                "C": "A CVE id and vendor name identify a vulnerability but do not by themselves quantify risk.",
                "D": "Confidentiality and integrity are CIA pillars (impact dimensions), not the two-factor risk formula.",
            },
            "exam_pattern": "Risk level = likelihood x impact.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },

    # ===== cbr_soc_analysis_tools ===========================================
    {
        "id": "cbrops-con-r2-020", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 2, "type": "mcq",
        "stem": "A platform collects, aggregates, and retains raw log data from many sources for storage "
                "and search, but does NOT correlate events across sources or raise prioritized alerts. "
                "What is it?",
        "options": [
            {"id": "A", "text": "A log management system"},
            {"id": "B", "text": "A SIEM"},
            {"id": "C", "text": "A SOAR platform"},
            {"id": "D", "text": "An intrusion prevention system (IPS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Log management centralizes collection, storage, and retrieval of logs; it is the "
                       "foundation a SIEM builds on but lacks the SIEM's cross-source correlation and alerting.",
            "distractors": {
                "B": "A SIEM adds normalization, correlation, and alerting on top of log storage - more than described here.",
                "C": "SOAR orchestrates and automates response across tools; it is not a plain log store.",
                "D": "An IPS inspects and blocks traffic inline; it is a log source, not a log-management platform.",
            },
            "exam_pattern": "Collect/store/search logs only, no correlation/alerting = log management (SIEM adds correlation).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },
    {
        "id": "cbrops-con-r2-021", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 2, "type": "mcq",
        "stem": "A protection approach installs software on each endpoint to provide deep, continuous "
                "local visibility and on-host enforcement. Compared with an agentless approach, this is "
                "best described as:",
        "options": [
            {"id": "A", "text": "Agent-based protection"},
            {"id": "B", "text": "Agentless protection"},
            {"id": "C", "text": "Perimeter-only protection"},
            {"id": "D", "text": "Network tap monitoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Agent-based protection runs software on the host, giving rich local telemetry and the "
                       "ability to enforce policy on the endpoint itself, at the cost of deploying and maintaining agents.",
            "distractors": {
                "B": "Agentless protection monitors from the network or an API without installing software on each host - the opposite of what is described.",
                "C": "Perimeter-only protection watches the boundary, not individual endpoints.",
                "D": "A network tap passively copies traffic; it is not host-resident software.",
            },
            "exam_pattern": "Software installed on each host for local visibility/enforcement = agent-based.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },
    {
        "id": "cbrops-con-r2-022", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 2, "type": "mcq",
        "stem": "Which technology continuously monitors endpoints - recording process trees, file and "
                "registry changes, and network connections - and lets responders investigate and "
                "remediate threats on hosts, going beyond signature-only antivirus?",
        "options": [
            {"id": "A", "text": "Endpoint detection and response (EDR)"},
            {"id": "B", "text": "A SIEM correlation engine"},
            {"id": "C", "text": "A network firewall"},
            {"id": "D", "text": "Network access control (NAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR provides deep, continuous endpoint telemetry plus detection, investigation, and "
                       "response capabilities, catching behavior that signature antivirus misses.",
            "distractors": {
                "B": "A SIEM correlates logs centrally across the environment; it is not the on-host detection/response agent.",
                "C": "A network firewall filters traffic at the boundary, not endpoint process/registry activity.",
                "D": "NAC controls which devices may join the network; it does not record host process behavior.",
            },
            "exam_pattern": "Deep host telemetry + investigate/remediate on endpoints = EDR.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },

    # ========================================================================
    # DOMAIN 2: cbr_security_monitoring (28)
    # ========================================================================

    # ===== cbr_data_types ===================================================
    {
        "id": "cbrops-mon-r2-001", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "Logs that record application-level request/response pairs - such as an HTTP GET for "
                "/login returning 200, or a DNS query and the answer it received - are which category of "
                "monitored data?",
        "options": [
            {"id": "A", "text": "Transaction data"},
            {"id": "B", "text": "Session data"},
            {"id": "C", "text": "Statistical data"},
            {"id": "D", "text": "Full packet capture"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Transaction data captures discrete application-layer exchanges (requests and their "
                       "responses), such as HTTP transactions or DNS query/answer pairs.",
            "distractors": {
                "B": "Session data summarizes a whole conversation (5-tuple, counts, timing), not individual request/response pairs.",
                "C": "Statistical data is aggregated trend/baseline information, not individual transactions.",
                "D": "Full packet capture stores entire raw packets including payload, far more than a transaction record.",
            },
            "exam_pattern": "Application-level request/response records (HTTP GET, DNS query/answer) = transaction data.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-r2-002", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "A monitoring dashboard shows average bytes per hour, peak throughput, and the top-talker "
                "hosts, all computed over a week of traffic. This aggregated, derived information is which "
                "data type?",
        "options": [
            {"id": "A", "text": "Statistical data"},
            {"id": "B", "text": "Alert data"},
            {"id": "C", "text": "Transaction data"},
            {"id": "D", "text": "Full packet capture"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Statistical data is aggregated/derived information (averages, counts, baselines) that "
                       "describes traffic behavior over time and underpins anomaly detection.",
            "distractors": {
                "B": "Alert data is produced when a rule or signature matches, not computed aggregates.",
                "C": "Transaction data records individual application exchanges, not weekly aggregates.",
                "D": "Full packet capture is raw per-packet content, the opposite of summarized statistics.",
            },
            "exam_pattern": "Aggregated averages/counts/baselines over time = statistical data.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-r2-003", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "An analyst examines a file's creation timestamp, author, and size, and an email's header "
                "fields, to understand context without reading the content itself. This 'data about data' "
                "is called:",
        "options": [
            {"id": "A", "text": "Metadata"},
            {"id": "B", "text": "Payload"},
            {"id": "C", "text": "Alert data"},
            {"id": "D", "text": "Full packet capture"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Metadata is descriptive data about other data (timestamps, authorship, sizes, headers); "
                       "it is a recognized monitoring data type that often reveals a lot without the content.",
            "distractors": {
                "B": "The payload is the actual content, not the descriptive data about it.",
                "C": "Alert data is a sensor's notification of a match, not descriptive attributes of a file/email.",
                "D": "Full packet capture is the raw traffic itself, not metadata describing it.",
            },
            "exam_pattern": "Data that describes other data (timestamps, headers, size) = metadata.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-r2-004", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "What is the primary DRAWBACK of relying on full packet capture for continuous, "
                "long-term network monitoring?",
        "options": [
            {"id": "A", "text": "It consumes very large amounts of storage, limiting how long it can be retained"},
            {"id": "B", "text": "It cannot record application payloads"},
            {"id": "C", "text": "It is unable to see packet headers"},
            {"id": "D", "text": "It only works on encrypted traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Full packet capture stores every byte of traffic, so its storage cost is high and "
                       "retention is short; teams often keep compact session/transaction data for the long haul.",
            "distractors": {
                "B": "Recording full payloads is exactly what full capture does best.",
                "C": "Full capture includes all headers; it sees them fully.",
                "D": "Full capture works on any traffic; encryption hides the payload content but capture still records the bytes.",
            },
            "exam_pattern": "Full capture's cost = huge storage / short retention (session data scales for long retention).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-r2-005", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 3, "type": "multi",
        "stem": "Which TWO of the following are examples of SESSION data rather than full packet capture? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "A NetFlow record for a conversation"},
            {"id": "B", "text": "A 5-tuple with byte and packet counts and start/stop times"},
            {"id": "C", "text": "The reconstructed bytes of a transferred file"},
            {"id": "D", "text": "The raw hexadecimal payload of each packet"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Session data summarizes a conversation as metadata - a NetFlow record and a 5-tuple "
                       "with counts and timestamps are classic examples; neither holds payload.",
            "distractors": {
                "C": "Reconstructing a transferred file requires payload, which comes from full packet capture, not session data.",
                "D": "Raw packet payload is captured content, the defining feature of full packet capture.",
            },
            "exam_pattern": "Flow summaries/5-tuple+counts = session data; payload/reconstructed content = full capture.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },

    # ===== cbr_attack_surface_vectors =======================================
    {
        "id": "cbrops-mon-r2-006", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "An attacker secretly positions themselves between a client and a server, relaying (and "
                "potentially altering) the traffic while both sides believe they are communicating "
                "directly. Which network attack is this?",
        "options": [
            {"id": "A", "text": "Man-in-the-middle (on-path) attack"},
            {"id": "B", "text": "Distributed denial of service"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Phishing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A man-in-the-middle (on-path) attacker intercepts and relays traffic between two "
                       "parties, able to eavesdrop or tamper while both believe the channel is direct.",
            "distractors": {
                "B": "A DDoS floods a target to deny availability; it does not sit between two parties relaying traffic.",
                "C": "SQL injection targets a database through application input, not by intercepting a channel.",
                "D": "Phishing tricks a user into acting; it is a social-engineering delivery method, not traffic interception.",
            },
            "exam_pattern": "Attacker secretly relays/alters traffic between two parties = man-in-the-middle / on-path.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.5 Describe network attacks"],
    },
    {
        "id": "cbrops-mon-r2-007", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "A service is overwhelmed by traffic sent simultaneously from thousands of compromised "
                "hosts in a botnet. How does this differ from a basic denial-of-service (DoS) attack?",
        "options": [
            {"id": "A", "text": "The flood is distributed across many sources (DDoS), making it harder to block by source"},
            {"id": "B", "text": "It targets integrity instead of availability"},
            {"id": "C", "text": "It requires physical access to the server"},
            {"id": "D", "text": "It is not actually a denial-of-service attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A DDoS uses many distributed sources (often a botnet) at once, so defenders cannot "
                       "simply block one IP; a plain DoS comes from a single source.",
            "distractors": {
                "B": "Both DoS and DDoS attack availability, not integrity.",
                "C": "These are remote network floods; they do not need physical access.",
                "D": "A DDoS is a denial-of-service attack - just distributed across many sources.",
            },
            "exam_pattern": "Many distributed sources flooding at once = DDoS (vs single-source DoS).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.5 Describe network attacks"],
    },
    {
        "id": "cbrops-mon-r2-008", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "An attacker phones the service desk pretending to be a senior executive and pressures "
                "the agent into resetting an account password immediately. Which attack category is this?",
        "options": [
            {"id": "A", "text": "Social engineering"},
            {"id": "B", "text": "Buffer overflow"},
            {"id": "C", "text": "Distributed denial of service"},
            {"id": "D", "text": "SQL injection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Social engineering manipulates people (here via impersonation and urgency/authority) "
                       "into taking actions that undermine security, such as resetting a password for an attacker.",
            "distractors": {
                "B": "A buffer overflow abuses a program's memory handling, not a human agent.",
                "C": "A DDoS floods a service; it does not involve manipulating a help-desk employee.",
                "D": "SQL injection attacks a database through input fields, not a phone call to staff.",
            },
            "exam_pattern": "Manipulating a person (impersonation, urgency, authority) into acting = social engineering.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.7 Describe social engineering attacks"],
    },
    {
        "id": "cbrops-mon-r2-009", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 1, "type": "mcq",
        "stem": "Malware encrypts a victim's files and then demands a payment in exchange for the "
                "decryption key. Which class of malware is this, and which CIA pillar does it most "
                "directly attack?",
        "options": [
            {"id": "A", "text": "Ransomware; availability"},
            {"id": "B", "text": "Spyware; confidentiality"},
            {"id": "C", "text": "Rootkit; integrity"},
            {"id": "D", "text": "Adware; availability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ransomware encrypts data to deny the owner access and extorts payment for recovery; by "
                       "locking users out of their own files it chiefly attacks availability.",
            "distractors": {
                "B": "Spyware covertly collects information (confidentiality) but does not lock files for ransom.",
                "C": "A rootkit hides an attacker's presence; it is not defined by encrypting files for payment.",
                "D": "Adware displays unwanted ads; it does not encrypt files or demand ransom.",
            },
            "exam_pattern": "Encrypts files + demands payment = ransomware, an availability attack.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.8 Describe endpoint-based attacks"],
    },
    {
        "id": "cbrops-mon-r2-010", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 3, "type": "mcq",
        "stem": "A program writes attacker-supplied input past the end of a fixed-size memory buffer, "
                "overwriting adjacent memory and altering the program's execution flow. Which endpoint-"
                "based attack is this?",
        "options": [
            {"id": "A", "text": "Buffer overflow"},
            {"id": "B", "text": "Cross-site scripting"},
            {"id": "C", "text": "Phishing"},
            {"id": "D", "text": "ARP spoofing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A buffer overflow occurs when more data is written to a buffer than it can hold, "
                       "corrupting adjacent memory and potentially redirecting execution - a classic endpoint/software attack.",
            "distractors": {
                "B": "Cross-site scripting injects script into web pages viewed by other users; it is a web-app attack, not a memory overflow.",
                "C": "Phishing is social engineering via deceptive messages, not memory corruption.",
                "D": "ARP spoofing manipulates Layer 2 address mappings on a LAN, unrelated to buffer memory.",
            },
            "exam_pattern": "Input written past a buffer's bounds, overwrites memory, alters execution = buffer overflow.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.8 Describe endpoint-based attacks"],
    },
    {
        "id": "cbrops-mon-r2-011", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "On a local network an attacker sends forged ARP replies that map their own MAC address "
                "to the default gateway's IP, so other hosts send their traffic to the attacker. This "
                "technique, which enables a man-in-the-middle position, is called:",
        "options": [
            {"id": "A", "text": "ARP spoofing (ARP poisoning)"},
            {"id": "B", "text": "DNS tunneling"},
            {"id": "C", "text": "SYN flooding"},
            {"id": "D", "text": "Port scanning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ARP spoofing/poisoning sends falsified ARP replies so victims associate the attacker's "
                       "MAC with another host's IP (often the gateway), redirecting traffic through the attacker.",
            "distractors": {
                "B": "DNS tunneling hides data inside DNS queries; it does not forge Layer 2 ARP mappings.",
                "C": "A SYN flood exhausts a server's connection table; it does not redirect LAN traffic via ARP.",
                "D": "Port scanning probes which services are open; it does not poison ARP caches.",
            },
            "exam_pattern": "Forged ARP replies mapping attacker MAC to a victim/gateway IP = ARP spoofing/poisoning.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.5 Describe network attacks"],
    },

    # ===== cbr_network_telemetry ============================================
    {
        "id": "cbrops-mon-r2-012", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 2, "type": "mcq",
        "stem": "Which command-line tool captures packets traversing a network interface and can write "
                "the raw traffic to a .pcap file for later analysis in a tool such as Wireshark?",
        "options": [
            {"id": "A", "text": "tcpdump"},
            {"id": "B", "text": "netstat"},
            {"id": "C", "text": "nslookup"},
            {"id": "D", "text": "traceroute"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "tcpdump is a packet-capture tool that reads traffic off an interface and can save it to "
                       "a .pcap file for offline analysis.",
            "distractors": {
                "B": "netstat lists active connections and listening ports on a host; it does not capture packets.",
                "C": "nslookup queries DNS to resolve names; it is not a packet capture tool.",
                "D": "traceroute maps the path to a destination; it does not capture and save full traffic.",
            },
            "exam_pattern": "CLI packet capture to .pcap = tcpdump.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-r2-013", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 2, "type": "mcq",
        "stem": "A security appliance blocks users from reaching known-malicious and policy-prohibited "
                "websites based on URL category and reputation. Which technology is this?",
        "options": [
            {"id": "A", "text": "Web content filtering (secure web gateway)"},
            {"id": "B", "text": "A NetFlow collector"},
            {"id": "C", "text": "Email content filtering"},
            {"id": "D", "text": "A traditional stateful firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Web content filtering / a secure web gateway inspects and controls web access by URL, "
                       "category, and reputation, blocking malicious or disallowed sites.",
            "distractors": {
                "B": "A NetFlow collector gathers flow metadata; it does not enforce web-access policy.",
                "C": "Email content filtering inspects email, not web browsing.",
                "D": "A traditional stateful firewall filters by the 5-tuple and connection state, not URL category/reputation.",
            },
            "exam_pattern": "Block websites by URL category/reputation = web content filtering (secure web gateway).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-r2-014", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 2, "type": "mcq",
        "stem": "A gateway scans inbound messages and strips malicious attachments and quarantines "
                "phishing and spam before they reach users' inboxes. Which technology is this?",
        "options": [
            {"id": "A", "text": "Email content filtering (secure email gateway)"},
            {"id": "B", "text": "Web content filtering"},
            {"id": "C", "text": "A network tap"},
            {"id": "D", "text": "An intrusion prevention system on the LAN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Email content filtering / a secure email gateway inspects inbound (and outbound) mail "
                       "to block malware, phishing, and spam before delivery.",
            "distractors": {
                "B": "Web content filtering governs web browsing, not email.",
                "C": "A tap passively copies traffic for monitoring; it does not filter email.",
                "D": "A LAN IPS inspects network traffic broadly; the described mail-specific scanning is email content filtering.",
            },
            "exam_pattern": "Scan/strip/quarantine malicious email before delivery = email content filtering.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-r2-015", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 3, "type": "mcq",
        "stem": "What primarily distinguishes a next-generation firewall (NGFW) from a traditional "
                "stateful firewall?",
        "options": [
            {"id": "A", "text": "It adds application awareness, integrated IPS, and deep inspection beyond port/protocol"},
            {"id": "B", "text": "It filters strictly by the 5-tuple and keeps no connection state"},
            {"id": "C", "text": "It cannot track connection state at all"},
            {"id": "D", "text": "It operates only at Layer 2 using MAC addresses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An NGFW builds on stateful filtering by adding application identification/control, "
                       "integrated intrusion prevention, and deeper payload inspection, so it decides on more than ports.",
            "distractors": {
                "B": "Filtering only by the 5-tuple with no state describes a stateless packet filter, not an NGFW.",
                "C": "An NGFW still tracks connection state; it adds capabilities on top of that.",
                "D": "An NGFW inspects up through the application layer, not just Layer 2.",
            },
            "exam_pattern": "NGFW = stateful firewall + app awareness + integrated IPS + deep inspection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-r2-016", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 3, "type": "mcq",
        "stem": "A single NetFlow record shows an internal host uploaded 40 GB to an unfamiliar external "
                "IP overnight. Even though NetFlow holds no payload, why is this record enough to flag "
                "possible data exfiltration?",
        "options": [
            {"id": "A", "text": "The byte counts and endpoints reveal an abnormally large outbound transfer to an unknown destination"},
            {"id": "B", "text": "NetFlow decrypts the payload to confirm the stolen data"},
            {"id": "C", "text": "NetFlow lists the exact file names that were taken"},
            {"id": "D", "text": "NetFlow automatically blocks the transfer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Flow metadata (who, when, how much, to where) is enough to spot an anomalous bulk "
                       "outbound transfer to an unknown host - a strong exfiltration indicator worth investigating.",
            "distractors": {
                "B": "NetFlow never decrypts or stores payload; it records metadata only.",
                "C": "NetFlow has no file names or content; it has the 5-tuple, counts, and timing.",
                "D": "NetFlow is a monitoring/telemetry source; it observes flows, it does not block them.",
            },
            "exam_pattern": "Large byte counts to an unknown external host in flow data = possible exfiltration (no payload needed).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },

    # ===== cbr_detection_methods ============================================
    {
        "id": "cbrops-mon-r2-017", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 2, "type": "mcq",
        "stem": "What is the main ADVANTAGE of signature-based detection for threats that are already "
                "known?",
        "options": [
            {"id": "A", "text": "It identifies known attacks precisely with a low false-positive rate"},
            {"id": "B", "text": "It reliably detects brand-new zero-day attacks"},
            {"id": "C", "text": "It never needs its signature database updated"},
            {"id": "D", "text": "It learns each user's behavioral baseline automatically"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Because it matches well-defined known patterns, signature detection is precise for known "
                       "threats and tends to generate few false positives.",
            "distractors": {
                "B": "Zero-days have no signature yet, so signature detection generally misses them - that is its key weakness.",
                "C": "Signatures must be updated constantly to cover new known threats.",
                "D": "Learning a per-user baseline is behavioral/anomaly detection, not signature matching.",
            },
            "exam_pattern": "Signature detection's strength = precise, low-false-positive detection of KNOWN threats.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },
    {
        "id": "cbrops-mon-r2-018", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 2, "type": "mcq",
        "stem": "Why do behavioral / anomaly-based detection systems tend to produce MORE false positives "
                "than signature-based systems?",
        "options": [
            {"id": "A", "text": "Legitimate but unusual activity can deviate from the learned baseline and be flagged"},
            {"id": "B", "text": "They can only inspect encrypted traffic"},
            {"id": "C", "text": "They rely solely on exact known-bad patterns"},
            {"id": "D", "text": "They never raise any alerts at all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anomaly detection flags deviations from 'normal', so benign-but-unusual behavior (a new "
                       "app, a late-night project) can trip alerts, raising the false-positive rate.",
            "distractors": {
                "B": "Anomaly detection works on many data types, not only encrypted traffic.",
                "C": "Relying on exact known-bad patterns describes signature detection, not anomaly detection.",
                "D": "Anomaly systems do raise alerts - the issue is that some are false positives.",
            },
            "exam_pattern": "Anomaly detection flags deviations, so benign-unusual activity inflates false positives.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },
    {
        "id": "cbrops-mon-r2-019", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Behavioral and anomaly-based detection first establish a ______ of "
                "normal activity, then alert on significant deviations from it. (one word)",
        "correct": ["baseline", "a baseline"],
        "explanation": {
            "correct": "A baseline is the learned profile of normal behavior; anomaly/behavioral detection "
                       "compares live activity to it and flags meaningful deviations, catching novel threats.",
            "exam_pattern": "Learn normal, flag deviations -> the learned 'normal' profile is the baseline.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },
    {
        "id": "cbrops-mon-r2-020", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 2, "type": "mcq",
        "stem": "An antimalware engine flags a never-before-seen file as suspicious because it exhibits "
                "traits common to malware (packing, self-modifying code, suspicious API calls) rather than "
                "matching an exact signature. Which detection approach is this?",
        "options": [
            {"id": "A", "text": "Heuristic (behavioral) detection"},
            {"id": "B", "text": "Exact signature matching"},
            {"id": "C", "text": "Hash blocklisting"},
            {"id": "D", "text": "Application allowlisting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Heuristic detection scores files/behavior by malware-like characteristics, allowing it "
                       "to flag new or modified samples that no exact signature yet covers.",
            "distractors": {
                "B": "Exact signature matching needs a known pattern and would miss a brand-new file.",
                "C": "Hash blocklisting only catches files whose exact hash is already known-bad.",
                "D": "Allowlisting permits only approved programs; it is a policy control, not trait-based detection.",
            },
            "exam_pattern": "Flag unknown files by malware-like traits (not exact match) = heuristic detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },

    # ===== cbr_evasion_obfuscation ==========================================
    {
        "id": "cbrops-mon-r2-021", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 2, "type": "mcq",
        "stem": "An attacker routes command-and-control traffic through the Tor network. How does this "
                "primarily hinder an investigation?",
        "options": [
            {"id": "A", "text": "It anonymizes and obscures the true source and destination by relaying through many nodes"},
            {"id": "B", "text": "It decrypts all of the victim's traffic for the defender"},
            {"id": "C", "text": "It speeds up detection by labeling malicious flows"},
            {"id": "D", "text": "It removes the IP headers so packets cannot be routed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tor relays traffic through multiple volunteer nodes with layered encryption, concealing "
                       "the real endpoints and making attribution and blocking much harder.",
            "distractors": {
                "B": "Tor adds encryption and anonymity; it does not reveal plaintext to defenders.",
                "C": "Tor hides activity; it does not help defenders label malicious flows.",
                "D": "Packets still need IP headers to route; Tor hides endpoints by relaying, not by deleting headers.",
            },
            "exam_pattern": "Anonymizing relay network hiding true source/destination = Tor / anonymizing proxy.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.3 Describe the impact of these technologies on data visibility"],
    },
    {
        "id": "cbrops-mon-r2-022", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 2, "type": "mcq",
        "stem": "Many internal hosts share one public IP address through Port Address Translation (PAT). "
                "Why can this complicate attributing malicious outbound traffic seen at the perimeter to a "
                "specific internal host?",
        "options": [
            {"id": "A", "text": "The source address is translated, so external logs show the shared public IP, not the internal host"},
            {"id": "B", "text": "PAT encrypts the packet payloads so they cannot be read"},
            {"id": "C", "text": "PAT discards all connection logs automatically"},
            {"id": "D", "text": "PAT randomly changes the destination to hide the target"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PAT maps many private source addresses to one public address, so traffic observed "
                       "outside shows the shared IP; analysts need the internal NAT translation records to pinpoint the host.",
            "distractors": {
                "B": "PAT rewrites addresses/ports; it does not encrypt payloads.",
                "C": "PAT devices can and should log translations; the complication is the shared external IP, not lost logs.",
                "D": "PAT translates the source side for internal hosts; it does not randomize the destination.",
            },
            "exam_pattern": "PAT hides internal hosts behind one public IP -> attribution needs the translation records.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.3 Describe the impact of these technologies on data visibility"],
    },
    {
        "id": "cbrops-mon-r2-023", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 3, "type": "mcq",
        "stem": "Malware hides a command string by Base64-encoding it so that a simple keyword search of "
                "the traffic will not match the plaintext command. This technique is best described as:",
        "options": [
            {"id": "A", "text": "Encoding / obfuscation"},
            {"id": "B", "text": "Encryption"},
            {"id": "C", "text": "Fragmentation"},
            {"id": "D", "text": "Tunneling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Base64 is an encoding scheme that transforms data into another representation to evade "
                       "simple string matching; it is reversible by anyone and uses no secret key, so it is obfuscation, not encryption.",
            "distractors": {
                "B": "Encryption requires a key and provides confidentiality; Base64 needs no key and anyone can decode it.",
                "C": "Fragmentation splits a payload across packets; it does not re-encode the content.",
                "D": "Tunneling wraps traffic inside another protocol; it is not the same as re-encoding a string.",
            },
            "exam_pattern": "Base64 / reversible re-representation with no key = encoding/obfuscation (NOT encryption).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.9 Describe evasion and obfuscation techniques"],
    },
    {
        "id": "cbrops-mon-r2-024", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 3, "type": "mcq",
        "stem": "An attacker floods a network IDS with huge volumes of crafted traffic, hoping the sensor "
                "drops packets or stops inspecting while the real attack slips through. Which evasion "
                "technique is this?",
        "options": [
            {"id": "A", "text": "Resource exhaustion of the sensor"},
            {"id": "B", "text": "TLS encryption of the payload"},
            {"id": "C", "text": "Certificate pinning"},
            {"id": "D", "text": "Load balancing for performance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Overwhelming a sensor's CPU, memory, or inspection capacity (resource exhaustion) can "
                       "cause it to drop or skip packets, letting malicious traffic pass uninspected.",
            "distractors": {
                "B": "Encryption hides payload content but does not work by overloading the sensor.",
                "C": "Certificate pinning is an app-side trust control, not an IDS-evasion flooding technique.",
                "D": "Load balancing distributes traffic for performance/availability; it is not an evasion attack on a sensor.",
            },
            "exam_pattern": "Overload the sensor so it drops/skips inspection = resource exhaustion evasion.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.9 Describe evasion and obfuscation techniques"],
    },

    # ===== cbr_certificates_crypto ==========================================
    {
        "id": "cbrops-mon-r2-025", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "mcq",
        "stem": "In asymmetric cryptography, to send data that only the intended recipient can read, the "
                "sender encrypts with the recipient's ______ key, and the recipient decrypts with their "
                "______ key.",
        "options": [
            {"id": "A", "text": "public; private"},
            {"id": "B", "text": "private; public"},
            {"id": "C", "text": "symmetric; symmetric"},
            {"id": "D", "text": "private; private"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "For confidentiality with asymmetric keys, encrypt with the recipient's PUBLIC key; only "
                       "the matching PRIVATE key (held solely by the recipient) can decrypt it.",
            "distractors": {
                "B": "Encrypting with a private key and decrypting with the public key is how signing/verification works, not confidential delivery.",
                "C": "A single shared symmetric key is symmetric cryptography, not the asymmetric scenario described.",
                "D": "The private key is never shared, so a sender cannot encrypt with the recipient's private key.",
            },
            "exam_pattern": "Confidentiality: encrypt with recipient's PUBLIC key, decrypt with recipient's PRIVATE key.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.10 Describe the impact of certificates on security"],
    },
    {
        "id": "cbrops-mon-r2-026", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "mcq",
        "stem": "A sender creates a digital signature by encrypting a message's hash with their own "
                "private key; recipients verify it using the sender's public key. What does a valid "
                "digital signature primarily provide?",
        "options": [
            {"id": "A", "text": "Authentication of origin, integrity, and non-repudiation"},
            {"id": "B", "text": "Confidentiality of the message body"},
            {"id": "C", "text": "Higher availability of the service"},
            {"id": "D", "text": "Faster data transfer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Signing with the private key lets anyone verify with the public key that the message "
                       "came from that signer (authentication/non-repudiation) and was not altered (integrity).",
            "distractors": {
                "B": "A signature does not hide the message content; encryption of the body would provide confidentiality.",
                "C": "Signatures are about authenticity/integrity, not keeping a service online.",
                "D": "Signing adds verification work; it does not speed up transfer.",
            },
            "exam_pattern": "Sign with private key, verify with public key = authentication + integrity + non-repudiation.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.10 Describe the impact of certificates on security"],
    },
    {
        "id": "cbrops-mon-r2-027", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "mcq",
        "stem": "A browser trusts a web server's certificate because it was signed by an intermediate CA "
                "whose own certificate chains up to a trusted ______ CA already in the browser's trust "
                "store.",
        "options": [
            {"id": "A", "text": "root"},
            {"id": "B", "text": "subordinate leaf"},
            {"id": "C", "text": "self-signed server"},
            {"id": "D", "text": "revoked"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The chain of trust ends at a root CA preinstalled in the trust store; if every link "
                       "(server -> intermediate -> root) validates, the server certificate is trusted.",
            "distractors": {
                "B": "The leaf is the server's own end-entity certificate, the bottom of the chain, not the trusted anchor.",
                "C": "A self-signed server certificate has no external anchor, so browsers do not trust it by default.",
                "D": "A revoked CA certificate would break trust, not establish it.",
            },
            "exam_pattern": "Trust anchor at the top of the certificate chain = root CA (in the trust store).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.11 Identify the certificate components in a given scenario"],
    },
    {
        "id": "cbrops-mon-r2-028", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "multi",
        "stem": "Before trusting a certificate, a client should check whether the issuing CA revoked it "
                "early (for example, after a key compromise). Which TWO mechanisms provide certificate "
                "revocation status? (Choose two.)",
        "options": [
            {"id": "A", "text": "Certificate Revocation List (CRL)"},
            {"id": "B", "text": "Online Certificate Status Protocol (OCSP)"},
            {"id": "C", "text": "Certificate Signing Request (CSR)"},
            {"id": "D", "text": "Maximum Transmission Unit (MTU)"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A CRL is the CA's published list of revoked certificates, and OCSP lets a client query "
                       "a responder for a specific certificate's status in real time; both report revocation.",
            "distractors": {
                "C": "A CSR is the request used to obtain a certificate, not a way to check revocation.",
                "D": "MTU is the largest packet size on a link - a networking parameter unrelated to certificates.",
            },
            "exam_pattern": "Check if a certificate is revoked = CRL (list) or OCSP (live query).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.11 Identify the certificate components in a given scenario"],
    },

    # ========================================================================
    # DOMAIN 3: cbr_host_analysis (22)
    # ========================================================================

    # ===== cbr_endpoint_technologies ========================================
    {
        "id": "cbrops-host-r2-001", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "Software on a host not only detects malicious activity but actively BLOCKS it in real "
                "time - for example terminating a process or dropping a connection as it happens. Which "
                "endpoint technology is this?",
        "options": [
            {"id": "A", "text": "Host-based intrusion prevention system (HIPS)"},
            {"id": "B", "text": "Host-based intrusion detection system (HIDS)"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "A certificate authority"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A HIPS sits inline on the host and can block/prevent malicious activity in real time, "
                       "whereas a HIDS only detects and alerts after the fact.",
            "distractors": {
                "B": "A HIDS detects and alerts but does not actively block the activity - that is the key difference.",
                "C": "A SIEM aggregates and correlates logs centrally; it does not enforce blocking on the host.",
                "D": "A certificate authority issues certificates and performs no host intrusion prevention.",
            },
            "exam_pattern": "Host software that blocks/prevents in real time = HIPS (HIDS only detects).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-r2-002", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 1, "type": "mcq",
        "stem": "By what primary method does traditional (legacy) antivirus identify malware on an "
                "endpoint?",
        "options": [
            {"id": "A", "text": "Matching files against a database of known malware signatures"},
            {"id": "B", "text": "Learning each user's login baseline and flagging deviations"},
            {"id": "C", "text": "Blocking inbound and outbound network ports"},
            {"id": "D", "text": "Issuing and validating digital certificates"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Traditional antivirus relies on signatures - patterns/hashes of known malware - so it "
                       "catches known samples but can miss new, unknown ones.",
            "distractors": {
                "B": "Learning a behavioral baseline describes anomaly/EDR techniques, not legacy signature AV.",
                "C": "Blocking ports is a firewall function, not how signature AV identifies malware.",
                "D": "Certificate handling is a PKI function, unrelated to antivirus detection.",
            },
            "exam_pattern": "Legacy AV = signature matching against known malware (misses the unknown).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-r2-003", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A control allows ALL applications to run EXCEPT those named on a defined list of "
                "prohibited programs. What is this default-allow approach called?",
        "options": [
            {"id": "A", "text": "Application blocklisting (blacklisting)"},
            {"id": "B", "text": "Application allowlisting (whitelisting)"},
            {"id": "C", "text": "Sandboxing"},
            {"id": "D", "text": "File integrity monitoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Blocklisting permits everything by default and denies only listed-bad programs; it is "
                       "easier to run but can miss unknown malware not yet on the list.",
            "distractors": {
                "B": "Allowlisting is the opposite, default-DENY model: only approved programs run.",
                "C": "Sandboxing isolates code to observe/contain it; it is not a run/deny list policy.",
                "D": "File integrity monitoring watches for changes to protected files, not which apps may execute.",
            },
            "exam_pattern": "Default-allow, deny only listed-bad apps = blocklisting (allowlisting is default-deny).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-r2-004", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "Modern browsers, Java, and Adobe Reader run untrusted content in a restricted, isolated "
                "process so that exploited code cannot easily reach the rest of the system. This built-in "
                "protection is an example of:",
        "options": [
            {"id": "A", "text": "Application (systems-based) sandboxing"},
            {"id": "B", "text": "Application allowlisting"},
            {"id": "C", "text": "A host-based firewall"},
            {"id": "D", "text": "Full-disk encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Systems-based sandboxing confines a program's content to an isolated, low-privilege "
                       "process, containing exploits so they cannot easily affect the wider system.",
            "distractors": {
                "B": "Allowlisting decides which programs may run; it does not isolate a running program's content.",
                "C": "A host firewall filters network connections, not in-process execution isolation.",
                "D": "Full-disk encryption protects data at rest; it does not sandbox a running application.",
            },
            "exam_pattern": "Run untrusted content in an isolated, restricted process = application sandboxing.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },
    {
        "id": "cbrops-host-r2-005", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_endpoint_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A host agent computes hashes of critical system files and periodically re-checks them, "
                "alerting if a protected file changes unexpectedly. This capability is called:",
        "options": [
            {"id": "A", "text": "File integrity monitoring (FIM)"},
            {"id": "B", "text": "Application allowlisting"},
            {"id": "C", "text": "Signature-based antivirus"},
            {"id": "D", "text": "Sandboxing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File integrity monitoring baselines file hashes and alerts on unexpected changes, "
                       "surfacing tampering with system binaries or configuration files.",
            "distractors": {
                "B": "Allowlisting governs which programs may execute, not whether protected files were altered.",
                "C": "Signature AV looks for known malware patterns, not integrity changes to legitimate files.",
                "D": "Sandboxing isolates running code; it does not continuously verify file hashes.",
            },
            "exam_pattern": "Hash critical files and alert on change = file integrity monitoring (FIM).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.1 Describe the functionality of endpoint technologies"],
    },

    # ===== cbr_os_components =================================================
    {
        "id": "cbrops-host-r2-006", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 1, "type": "mcq",
        "stem": "On a Windows host, which built-in tool lets an analyst quickly view running processes, "
                "CPU and memory usage, services, and startup programs during triage?",
        "options": [
            {"id": "A", "text": "Task Manager"},
            {"id": "B", "text": "ps"},
            {"id": "C", "text": "crontab"},
            {"id": "D", "text": "/etc/passwd"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Task Manager (and the tasklist command) shows running processes and resource usage on "
                       "Windows, a fast way to spot an unexpected or resource-hungry process.",
            "distractors": {
                "B": "ps lists processes on Linux/UNIX, not Windows.",
                "C": "crontab schedules jobs on Linux; it is not a Windows process viewer.",
                "D": "/etc/passwd is a Linux account file, not a Windows process tool.",
            },
            "exam_pattern": "Windows process/resource triage = Task Manager / tasklist (ps is Linux).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-r2-007", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "mcq",
        "stem": "On a Linux system, which account has UID 0 and holds unrestricted administrative "
                "privileges over the entire system?",
        "options": [
            {"id": "A", "text": "root"},
            {"id": "B", "text": "Administrator"},
            {"id": "C", "text": "guest"},
            {"id": "D", "text": "nobody"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On Linux the superuser 'root' has UID 0 and full control of the system; attackers "
                       "escalating to UID 0 effectively own the host.",
            "distractors": {
                "B": "Administrator is the built-in privileged account on Windows, not Linux.",
                "C": "guest is a low-privilege account, not the superuser.",
                "D": "nobody is an intentionally unprivileged account used to run services with minimal rights.",
            },
            "exam_pattern": "Linux superuser = root (UID 0); Windows equivalent = Administrator.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-r2-008", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 3, "type": "multi",
        "stem": "An analyst hunting Windows persistence reviews mechanisms that launch programs "
                "automatically. Which TWO are common Windows autostart locations that malware abuses? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "A Windows service configured to start automatically"},
            {"id": "B", "text": "A Scheduled Task with a logon or boot trigger"},
            {"id": "C", "text": "An entry in the Linux /etc/rc.local file"},
            {"id": "D", "text": "The switch's MAC address table"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Auto-start Windows services and Scheduled Tasks are classic persistence mechanisms, "
                       "re-launching malware at boot or logon; both are standard hunt targets.",
            "distractors": {
                "C": "/etc/rc.local is a Linux startup file, not a Windows autostart location.",
                "D": "A MAC address table lives on a switch for Layer 2 forwarding; it is not a host autostart mechanism.",
            },
            "exam_pattern": "Windows persistence autostarts include services, Scheduled Tasks, and Run keys.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-r2-009", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "mcq",
        "stem": "On a Linux host, which facility schedules commands to run automatically at specified "
                "times and is a common persistence mechanism an analyst should review?",
        "options": [
            {"id": "A", "text": "cron (crontab)"},
            {"id": "B", "text": "The Windows Registry"},
            {"id": "C", "text": "Windows Event Viewer"},
            {"id": "D", "text": "PowerShell ISE"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "cron runs scheduled jobs from crontab entries on Linux; attackers add cron jobs for "
                       "persistence, so analysts examine user and system crontabs.",
            "distractors": {
                "B": "The Windows Registry is a Windows configuration store, not a Linux scheduler.",
                "C": "Event Viewer is the Windows log interface, not a Linux scheduling facility.",
                "D": "PowerShell ISE is a Windows scripting environment, not the Linux job scheduler.",
            },
            "exam_pattern": "Linux scheduled jobs / persistence = cron (crontab); Windows uses Task Scheduler.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },
    {
        "id": "cbrops-host-r2-010", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_os_components", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: On Linux, the file that traditionally stores local user account "
                "information - username, UID, GID, home directory, and login shell - is /etc/______.",
        "correct": ["passwd", "/etc/passwd"],
        "explanation": {
            "correct": "/etc/passwd lists local accounts and their attributes; the password hashes themselves "
                       "live in the more restricted /etc/shadow, so analysts review both during host analysis.",
            "exam_pattern": "Linux local account info = /etc/passwd (hashes in /etc/shadow).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.2 Identify components of an operating system (Windows and Linux)"],
    },

    # ===== cbr_logs_artifacts ===============================================
    {
        "id": "cbrops-host-r2-011", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "Which Windows Security event ID records a SUCCESSFUL account logon and includes a Logon "
                "Type field (for example, 2 = interactive, 3 = network, 10 = RemoteInteractive/RDP)?",
        "options": [
            {"id": "A", "text": "4624"},
            {"id": "B", "text": "4625"},
            {"id": "C", "text": "4688"},
            {"id": "D", "text": "1102"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 4624 'An account was successfully logged on' includes the Logon Type, letting "
                       "analysts distinguish interactive, network, and RDP logons.",
            "distractors": {
                "B": "4625 is a FAILED logon, not a success.",
                "C": "4688 records new process creation, not a logon.",
                "D": "1102 records that the Security audit log was cleared.",
            },
            "exam_pattern": "Successful logon + Logon Type = 4624 (4625 = failed).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-r2-012", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "An analyst hunting for malicious command execution wants the Windows Security event that "
                "logs each NEW PROCESS creation (with the process name and, if command-line auditing is "
                "enabled, the full command line). Which event ID?",
        "options": [
            {"id": "A", "text": "4688"},
            {"id": "B", "text": "4624"},
            {"id": "C", "text": "7045"},
            {"id": "D", "text": "4672"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 4688 'A new process has been created' is the core process-execution record; "
                       "with command-line process auditing enabled it also captures the command line.",
            "distractors": {
                "B": "4624 is a successful logon, not process creation.",
                "C": "7045 marks a new service installed, not every process launch.",
                "D": "4672 records that special/administrative privileges were assigned to a logon.",
            },
            "exam_pattern": "New process creation (and command line if audited) = Event ID 4688.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-r2-013", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 3, "type": "mcq",
        "stem": "Immediately after a logon, Windows logs Security event ID 4672 for the account. What "
                "does this most likely indicate to an analyst?",
        "options": [
            {"id": "A", "text": "The logon was granted sensitive/administrator-level privileges (an elevated session)"},
            {"id": "B", "text": "The logon attempt failed"},
            {"id": "C", "text": "The Security log was cleared"},
            {"id": "D", "text": "A new Windows service was installed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 4672 'Special privileges assigned to new logon' fires when an account receives "
                       "powerful rights at logon, flagging administrator-equivalent sessions worth scrutiny.",
            "distractors": {
                "B": "A failed logon is 4625, not 4672.",
                "C": "Clearing the Security log is event 1102.",
                "D": "A new service install is 7045 (System log) or 4697 (Security log).",
            },
            "exam_pattern": "Special/admin privileges assigned at logon = Event ID 4672 (elevated session).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-r2-014", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 3, "type": "mcq",
        "stem": "A host shows Windows event ID 7045 ('A service was installed in the system') for an "
                "oddly named service whose binary points to a file in a user's temp folder. Why is this "
                "notable to an analyst?",
        "options": [
            {"id": "A", "text": "Attackers often install malicious services for persistence, so an unexpected 7045 is a red flag"},
            {"id": "B", "text": "It simply records a normal failed logon"},
            {"id": "C", "text": "It means the host firewall blocked traffic"},
            {"id": "D", "text": "It is a routine DNS resolution event"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A newly installed service that auto-starts is a common persistence technique; a service "
                       "with a strange name running from a temp path strongly suggests malware.",
            "distractors": {
                "B": "A failed logon is event 4625, not a service installation.",
                "C": "7045 is about service installation, not firewall blocking.",
                "D": "DNS resolution is not recorded by the Windows service-install event 7045.",
            },
            "exam_pattern": "Unexpected 7045 service install (odd name/temp path) = possible persistence.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },
    {
        "id": "cbrops-host-r2-015", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_logs_artifacts", "difficulty": 3, "type": "mcq",
        "stem": "During triage an analyst finds Windows Security event ID 1102 generated just before log "
                "activity goes dark. What does this most likely indicate?",
        "options": [
            {"id": "A", "text": "The Security audit log was cleared - a common anti-forensic action"},
            {"id": "B", "text": "A successful backup completed normally"},
            {"id": "C", "text": "A user successfully logged on"},
            {"id": "D", "text": "A new process was created"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event ID 1102 'The audit log was cleared' often signals an attacker destroying evidence; "
                       "a 1102 followed by a gap in logging is a strong anti-forensics indicator.",
            "distractors": {
                "B": "A backup does not generate a log-cleared event.",
                "C": "A successful logon is event 4624, not 1102.",
                "D": "New process creation is event 4688, not a log-cleared event.",
            },
            "exam_pattern": "Security log cleared (then logging goes dark) = Event ID 1102, anti-forensics.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.6 Interpret OS, application, or command line logs to identify an event"],
    },

    # ===== cbr_malware_analysis =============================================
    {
        "id": "cbrops-host-r2-016", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An analyst inspects a malware file's printable strings, PE headers, and imported "
                "functions and computes its hash - all WITHOUT executing it. Which type of malware "
                "analysis is this?",
        "options": [
            {"id": "A", "text": "Static analysis"},
            {"id": "B", "text": "Dynamic (behavioral) analysis"},
            {"id": "C", "text": "Sandbox detonation"},
            {"id": "D", "text": "Penetration testing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Static analysis examines the sample without running it - strings, headers, imports, and "
                       "hashes - to derive indicators and intent safely.",
            "distractors": {
                "B": "Dynamic analysis runs the sample and watches its behavior; the scenario explicitly avoids execution.",
                "C": "Sandbox detonation is a form of dynamic analysis (it executes the file).",
                "D": "Penetration testing is authorized offensive assessment, not file analysis.",
            },
            "exam_pattern": "Examine the file WITHOUT running it (strings/headers/imports/hash) = static analysis.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },
    {
        "id": "cbrops-host-r2-017", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A sandbox report's 'dropped files' section lists additional executables the sample wrote "
                "to disk while running. Why does this matter to an analyst?",
        "options": [
            {"id": "A", "text": "The dropped files may be further malware payloads, and their hashes become new IOCs to hunt"},
            {"id": "B", "text": "Dropped files are always benign operating-system files"},
            {"id": "C", "text": "They reveal the password of the logged-in user"},
            {"id": "D", "text": "They decrypt the host's network traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Malware often drops secondary payloads; cataloging and hashing them yields new "
                       "indicators to detect and remove the full infection across the environment.",
            "distractors": {
                "B": "Dropped files are frequently malicious components, not guaranteed-benign OS files.",
                "C": "Dropped files are artifacts of the malware, not a store of user passwords.",
                "D": "Writing files to disk does not decrypt network traffic.",
            },
            "exam_pattern": "Dropped files = possible secondary payloads; hash them as new IOCs.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },
    {
        "id": "cbrops-host-r2-018", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A malware analysis report lists the domains and IP addresses the sample contacted during "
                "execution. What is the main analytical value of these network indicators?",
        "options": [
            {"id": "A", "text": "They are IOCs that can be blocked at DNS/firewall and searched across logs to find other infected hosts"},
            {"id": "B", "text": "They contain the malware's full source code"},
            {"id": "C", "text": "They prove the real-world identity of the author"},
            {"id": "D", "text": "They are the file's cryptographic hash"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Contacted domains/IPs (often C2) are network IOCs: block them to cut off the malware and "
                       "pivot through logs to discover every host that reached the same infrastructure.",
            "distractors": {
                "B": "Network destinations are not the program's source code.",
                "C": "Infrastructure indicators rarely prove authorship; attribution needs much more corroboration.",
                "D": "A hash fingerprints the file; it is a separate artifact from contacted domains/IPs.",
            },
            "exam_pattern": "Contacted domains/IPs = network IOCs to block and hunt across the fleet.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },
    {
        "id": "cbrops-host-r2-019", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_malware_analysis", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A tool that runs a suspicious sample in an instrumented, isolated "
                "virtual environment to observe its behavior is sometimes called a ______ chamber (and is "
                "more generally known as a sandbox). (one word)",
        "correct": ["detonation"],
        "explanation": {
            "correct": "A detonation chamber (sandbox) executes untrusted samples in isolation and records "
                       "their file, registry, and network behavior for dynamic analysis.",
            "exam_pattern": "Isolated environment to run and observe malware = detonation chamber / sandbox.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.7 Interpret the output report of a malware analysis tool"],
    },

    # ===== cbr_evidence_attribution =========================================
    {
        "id": "cbrops-host-r2-020", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "mcq",
        "stem": "Logs show a user's account was active at the time of an intrusion, which IMPLIES but does "
                "not directly prove that the user carried out the attack. What type of evidence is this?",
        "options": [
            {"id": "A", "text": "Indirect (circumstantial) evidence"},
            {"id": "B", "text": "Best evidence"},
            {"id": "C", "text": "Corroborative evidence"},
            {"id": "D", "text": "A signed confession"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Indirect (circumstantial) evidence suggests a fact by inference rather than proving it "
                       "directly; account activity implies involvement but does not conclusively establish it.",
            "distractors": {
                "B": "Best evidence is the original, most authoritative source (e.g., the original drive/image).",
                "C": "Corroborative evidence supports other evidence; here the log stands as an inference on its own.",
                "D": "A confession is direct evidence, not circumstantial inference.",
            },
            "exam_pattern": "Implies a fact by inference, does not directly prove it = indirect/circumstantial evidence.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.4 Identify type of evidence used based on provided logs"],
    },
    {
        "id": "cbrops-host-r2-021", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "mcq",
        "stem": "What distinguishes an indicator of attack (IOA) from an indicator of compromise (IOC)?",
        "options": [
            {"id": "A", "text": "An IOA focuses on the attacker's behavior/intent in progress; an IOC is forensic evidence that a compromise already occurred"},
            {"id": "B", "text": "They are identical terms with no difference"},
            {"id": "C", "text": "An IOA is always a file hash and an IOC is always a behavior"},
            {"id": "D", "text": "An IOC predicts attacks before any activity happens"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IOA describes adversary behavior/intent as an attack unfolds (useful for early "
                       "detection), while an IOC is an artifact (hash, domain, IP) showing a compromise has already taken place.",
            "distractors": {
                "B": "They are related but distinct: behavior/intent (IOA) vs after-the-fact artifact (IOC).",
                "C": "This swaps the definitions; IOAs are behavior-focused and IOCs include hashes/domains/IPs.",
                "D": "IOCs are evidence of a compromise that already happened, not pre-attack predictions.",
            },
            "exam_pattern": "IOA = behavior/intent in progress; IOC = forensic artifact of a past/ongoing compromise.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.3 Describe the role of attribution in an investigation"],
    },
    {
        "id": "cbrops-host-r2-022", "exam": "cbrops", "domain": "cbr_host_analysis",
        "subtopic": "cbr_evidence_attribution", "difficulty": 2, "type": "mcq",
        "stem": "To determine whether a disk image is untampered, an analyst compares its hash now with "
                "the hash taken at acquisition. If the two hash values DIFFER, what should be concluded?",
        "options": [
            {"id": "A", "text": "The image was altered/tampered, so its integrity and admissibility are in question"},
            {"id": "B", "text": "The image is confirmed authentic and unchanged"},
            {"id": "C", "text": "The disk must be encrypted"},
            {"id": "D", "text": "The evidence is strengthened by the mismatch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A matching hash proves the image is unchanged; a mismatch means at least one bit "
                       "changed, so the image is tampered and can no longer be trusted as pristine evidence.",
            "distractors": {
                "B": "Identical hashes - not differing ones - would confirm the image is unchanged.",
                "C": "A hash mismatch indicates alteration, not that the disk is encrypted.",
                "D": "A mismatch undermines evidentiary value; it does not strengthen it.",
            },
            "exam_pattern": "Acquisition hash != current hash -> image tampered (integrity/admissibility lost).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.5 Compare tampered and untampered disk image"],
    },

    # ========================================================================
    # DOMAIN 4: cbr_network_intrusion (22)
    # ========================================================================

    # ===== cbr_packet_session_analysis ======================================
    {
        "id": "cbrops-intr-r2-001", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_packet_session_analysis", "difficulty": 3, "type": "mcq",
        "stem": "In Wireshark, which entry is a valid DISPLAY filter that shows only traffic to or from "
                "host 10.0.0.5 on the HTTPS port?",
        "options": [
            {"id": "A", "text": "ip.addr == 10.0.0.5 && tcp.port == 443"},
            {"id": "B", "text": "host 10.0.0.5 and tcp port 443"},
            {"id": "C", "text": "ip.addr = 10.0.0.5 and port = 443"},
            {"id": "D", "text": "src 10.0.0.5 only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Wireshark display filters use field names with '==' and logical '&&', so "
                       "'ip.addr == 10.0.0.5 && tcp.port == 443' correctly restricts the view.",
            "distractors": {
                "B": "'host ... and tcp port ...' is BPF capture-filter (tcpdump) syntax, not a Wireshark display filter.",
                "C": "Display filters require '==' for equality; a single '=' is invalid syntax.",
                "D": "'src 10.0.0.5 only' is not valid Wireshark display-filter syntax.",
            },
            "exam_pattern": "Display filter = field + '==' + '&&' (e.g., ip.addr == x && tcp.port == 443); capture filter uses 'host/port'.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.6 Extract files from a TCP stream when given a PCAP file and Wireshark"],
    },
    {
        "id": "cbrops-intr-r2-002", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_packet_session_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A network TAP (or SPAN port) sends a copy of traffic to a monitoring tool without "
                "sitting in the forwarding path. Compared with inline traffic interrogation, what "
                "characterizes this out-of-band approach?",
        "options": [
            {"id": "A", "text": "It passively monitors a copy of the traffic and cannot itself block packets"},
            {"id": "B", "text": "It actively drops malicious packets in real time"},
            {"id": "C", "text": "It adds a single point of failure directly in the data path"},
            {"id": "D", "text": "It automatically decrypts all TLS sessions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A TAP/SPAN feed is out-of-band: it observes a copy, so it can detect and alert but "
                       "cannot block, and it does not add latency or a failure point to the live path.",
            "distractors": {
                "B": "Blocking in real time requires an INLINE device (like an IPS), not an out-of-band tap.",
                "C": "Because a tap is off-path, it does not become a single point of failure for forwarded traffic.",
                "D": "A tap copies traffic as-is; it does not decrypt TLS.",
            },
            "exam_pattern": "Tap/SPAN = passive copy, detect-only (no blocking); inline = can block but sits in the path.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.4 Compare inline traffic interrogation and taps or traffic monitoring"],
    },
    {
        "id": "cbrops-intr-r2-003", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_packet_session_analysis", "difficulty": 3, "type": "mcq",
        "stem": "An analyst keeps both NetFlow (transactional data) for breadth and targeted full packet "
                "captures for depth. Why use both rather than one?",
        "options": [
            {"id": "A", "text": "NetFlow gives broad, long-term visibility of all flows; full capture gives payload detail for specific suspect flows"},
            {"id": "B", "text": "NetFlow stores full payloads, so the captures are redundant"},
            {"id": "C", "text": "Full packet capture scales better than NetFlow for long-term retention"},
            {"id": "D", "text": "They provide identical data, so using both is purely for backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Transactional NetFlow data is compact and retainable for broad, long-term flow visibility; "
                       "full capture supplies payload depth for a few flows of interest - the two are complementary.",
            "distractors": {
                "B": "NetFlow holds no payload, so captures are not redundant.",
                "C": "Full capture is storage-heavy and scales worse than NetFlow for long retention.",
                "D": "They differ: NetFlow is metadata breadth, capture is payload depth.",
            },
            "exam_pattern": "NetFlow = broad/long-term metadata; full capture = deep payload for suspect flows (use both).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.5 Compare the characteristics of data obtained from taps or traffic monitoring and transactional data (NetFlow)"],
    },
    {
        "id": "cbrops-intr-r2-004", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_packet_session_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A PCAP shows a TCP conversation to destination port 23. Even before reading any payload, "
                "what service and risk does port 23 suggest to the analyst?",
        "options": [
            {"id": "A", "text": "Telnet - a cleartext remote-access protocol whose credentials are visible on the wire"},
            {"id": "B", "text": "HTTPS - encrypted web traffic"},
            {"id": "C", "text": "SSH - encrypted remote shell"},
            {"id": "D", "text": "DNS - name resolution"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TCP port 23 is Telnet, which transmits data (including credentials) in cleartext; seeing "
                       "it is both a service identification and a security concern worth investigating.",
            "distractors": {
                "B": "HTTPS uses TCP 443, not 23.",
                "C": "SSH uses TCP 22, not 23, and is encrypted (the opposite of Telnet).",
                "D": "DNS uses port 53, not 23.",
            },
            "exam_pattern": "Port 23 = Telnet (cleartext); 22 = SSH, 443 = HTTPS, 53 = DNS.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.7 Identify key elements in an intrusion from a given PCAP file"],
    },

    # ===== cbr_protocol_headers =============================================
    {
        "id": "cbrops-intr-r2-005", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 2, "type": "mcq",
        "stem": "Which sequence of TCP flags establishes a connection in the normal three-way handshake?",
        "options": [
            {"id": "A", "text": "SYN, then SYN-ACK, then ACK"},
            {"id": "B", "text": "SYN, then ACK, then FIN"},
            {"id": "C", "text": "ACK, then RST, then SYN"},
            {"id": "D", "text": "FIN, then FIN-ACK, then ACK"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The TCP three-way handshake is SYN (client) -> SYN-ACK (server) -> ACK (client), after "
                       "which the connection is established.",
            "distractors": {
                "B": "This mixes in FIN, which tears a connection down rather than establishing it.",
                "C": "RST abruptly resets a connection; it is not part of normal establishment.",
                "D": "FIN/FIN-ACK/ACK is the graceful connection teardown, not the setup handshake.",
            },
            "exam_pattern": "TCP setup = SYN -> SYN-ACK -> ACK; graceful close uses FIN.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },
    {
        "id": "cbrops-intr-r2-006", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 2, "type": "mcq",
        "stem": "An analyst sees many TCP segments with only the RST flag set sent in response to "
                "connection attempts. What does a RST most commonly indicate?",
        "options": [
            {"id": "A", "text": "An abrupt connection reset/refusal (for example, a closed port or forced teardown)"},
            {"id": "B", "text": "A successfully completed three-way handshake"},
            {"id": "C", "text": "A graceful, orderly connection close"},
            {"id": "D", "text": "An ICMP echo reply"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RST (reset) abruptly tears down or refuses a connection; a RST to a SYN often means the "
                       "destination port is closed, and many RSTs can accompany scanning.",
            "distractors": {
                "B": "A completed handshake ends with ACK after SYN/SYN-ACK, not a RST.",
                "C": "A graceful close uses FIN exchanges; RST is the abrupt, non-graceful alternative.",
                "D": "An echo reply is ICMP Type 0, unrelated to the TCP RST flag.",
            },
            "exam_pattern": "TCP RST = abrupt reset/refusal (closed port, forced teardown); FIN = graceful close.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },
    {
        "id": "cbrops-intr-r2-007", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about UDP is correct and relevant to intrusion analysis?",
        "options": [
            {"id": "A", "text": "UDP is connectionless with no handshake, sequence, or ACK fields - just ports, length, and checksum"},
            {"id": "B", "text": "UDP uses a three-way handshake like TCP"},
            {"id": "C", "text": "UDP guarantees ordered, reliable delivery"},
            {"id": "D", "text": "UDP carries SYN and ACK flags in its header"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "UDP is a minimal connectionless transport - its header has only source/destination "
                       "ports, length, and checksum - so there is no session state to reassemble and no handshake.",
            "distractors": {
                "B": "The three-way handshake (SYN/SYN-ACK/ACK) is a TCP feature; UDP has none.",
                "C": "UDP does not guarantee ordering or reliability; applications must handle that if needed.",
                "D": "SYN/ACK flags belong to TCP; UDP has no flags field.",
            },
            "exam_pattern": "UDP = connectionless, no handshake/flags/sequence; header is ports+length+checksum.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },
    {
        "id": "cbrops-intr-r2-008", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 3, "type": "mcq",
        "stem": "Which IPv4 header fields work together to allow a receiver to reassemble fragmented "
                "packets (and are abused in fragmentation-based IDS evasion)?",
        "options": [
            {"id": "A", "text": "Identification, Flags (More Fragments), and Fragment Offset"},
            {"id": "B", "text": "Time To Live and Protocol"},
            {"id": "C", "text": "Source Port and Destination Port"},
            {"id": "D", "text": "Window Size and Checksum"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fragments of one datagram share an Identification value; the More Fragments flag and the "
                       "Fragment Offset tell the receiver how to order and when to stop reassembling.",
            "distractors": {
                "B": "TTL limits hop count and Protocol names the upper layer; neither drives reassembly.",
                "C": "Ports are in the TCP/UDP header, not the IPv4 header, and are not reassembly fields.",
                "D": "Window Size and Checksum are TCP fields; they are unrelated to IP fragment reassembly.",
            },
            "exam_pattern": "IP reassembly = Identification + Flags (MF) + Fragment Offset.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },
    {
        "id": "cbrops-intr-r2-009", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 2, "type": "mcq",
        "stem": "In the IPv4 header, the Protocol field carries the value 6. Which encapsulated transport "
                "protocol does that indicate?",
        "options": [
            {"id": "A", "text": "TCP"},
            {"id": "B", "text": "UDP"},
            {"id": "C", "text": "ICMP"},
            {"id": "D", "text": "IGMP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IANA protocol number 6 is TCP; the IPv4 Protocol field tells the receiver which Layer 4 "
                       "protocol is inside so it can parse the next header correctly.",
            "distractors": {
                "B": "UDP is protocol number 17, not 6.",
                "C": "ICMP is protocol number 1.",
                "D": "IGMP is protocol number 2.",
            },
            "exam_pattern": "IP Protocol field: 1 = ICMP, 6 = TCP, 17 = UDP.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },
    {
        "id": "cbrops-intr-r2-010", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_protocol_headers", "difficulty": 2, "type": "mcq",
        "stem": "traceroute works by sending packets with increasing TTL values. Which ICMP message does "
                "each intermediate router return when a packet's TTL reaches zero?",
        "options": [
            {"id": "A", "text": "ICMP Time Exceeded (Type 11)"},
            {"id": "B", "text": "ICMP Echo Reply (Type 0)"},
            {"id": "C", "text": "ICMP Destination Unreachable (Type 3)"},
            {"id": "D", "text": "ICMP Redirect (Type 5)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When TTL decrements to zero, the router drops the packet and returns ICMP Time Exceeded "
                       "(Type 11); traceroute uses the source addresses of these replies to map each hop.",
            "distractors": {
                "B": "Echo Reply (Type 0) answers a ping Echo Request, not a TTL-expiry event.",
                "C": "Destination Unreachable (Type 3) signals the target/port cannot be reached, often at the final hop, not each intermediate hop.",
                "D": "Redirect (Type 5) tells a host of a better next-hop route; it is unrelated to TTL expiry.",
            },
            "exam_pattern": "TTL hits 0 at a router -> ICMP Time Exceeded (Type 11); the basis of traceroute.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.8 Interpret the fields in protocol headers as related to intrusion analysis"],
    },

    # ===== cbr_ids_ips_events ===============================================
    {
        "id": "cbrops-intr-r2-011", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_ids_ips_events", "difficulty": 2, "type": "mcq",
        "stem": "An IDS correctly stays silent while only normal, benign traffic flows - no alert is "
                "raised and no attack is occurring. How is this outcome classified?",
        "options": [
            {"id": "A", "text": "True negative"},
            {"id": "B", "text": "False negative"},
            {"id": "C", "text": "True positive"},
            {"id": "D", "text": "False positive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A true negative is the correct absence of an alert when there is genuinely no malicious "
                       "activity - the sensor rightly stayed quiet.",
            "distractors": {
                "B": "A false negative is a MISSED attack (no alert when there should be one).",
                "C": "A true positive is a correct alert on real malicious activity; here nothing alerted.",
                "D": "A false positive is an alert on benign activity; here no alert fired.",
            },
            "exam_pattern": "No alert + no attack = true negative (correct silence).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.2 Compare impact and no impact for these items"],
    },
    {
        "id": "cbrops-intr-r2-012", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_ids_ips_events", "difficulty": 2, "type": "mcq",
        "stem": "A signature fires, and investigation shows the triggering activity was unusual but "
                "authorized and harmless - an administrator's approved vulnerability scan. In CBROPS "
                "impact terminology, how is this triggering activity best labeled?",
        "options": [
            {"id": "A", "text": "Benign"},
            {"id": "B", "text": "True positive (malicious)"},
            {"id": "C", "text": "False negative"},
            {"id": "D", "text": "A confirmed breach"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Benign describes activity that trips a rule but is determined to be non-malicious, "
                       "authorized traffic; the alert is effectively a false positive for 'attack'.",
            "distractors": {
                "B": "A true positive is genuinely malicious activity; an authorized scan is not malicious.",
                "C": "A false negative is a missed attack; here the sensor did alert and the activity was benign.",
                "D": "Nothing was breached; the scan was authorized and harmless.",
            },
            "exam_pattern": "Rule fires on authorized, harmless activity = benign (non-malicious).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.2 Compare impact and no impact for these items"],
    },
    {
        "id": "cbrops-intr-r2-013", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_ids_ips_events", "difficulty": 2, "type": "mcq",
        "stem": "A log entry reads: 'DENY tcp 203.0.113.5:443 -> 10.1.1.9:51000, rule 42'. Which source "
                "technology most likely produced this entry?",
        "options": [
            {"id": "A", "text": "A firewall (permit/deny by rule and 5-tuple)"},
            {"id": "B", "text": "A host antivirus scanner"},
            {"id": "C", "text": "A web proxy URL log"},
            {"id": "D", "text": "An NTP time server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A permit/deny decision referencing a rule number and the 5-tuple (addresses/ports/"
                       "protocol) is characteristic of a firewall log.",
            "distractors": {
                "B": "Antivirus logs reference files, signatures, and hashes, not allow/deny rules on flows.",
                "C": "A proxy log centers on URLs, methods, and HTTP status codes, not a numbered deny rule.",
                "D": "An NTP server syncs time; it does not permit/deny traffic.",
            },
            "exam_pattern": "PERMIT/DENY + rule number + 5-tuple = firewall log.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.1 Map the provided events to source technologies"],
    },
    {
        "id": "cbrops-intr-r2-014", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_ids_ips_events", "difficulty": 2, "type": "mcq",
        "stem": "A log line shows a username, the full URL requested, the HTTP method, the response code, "
                "and bytes served for a user's web browsing. Which technology most likely generated it?",
        "options": [
            {"id": "A", "text": "A web proxy (proxy logs)"},
            {"id": "B", "text": "An intrusion prevention system payload signature"},
            {"id": "C", "text": "A NetFlow collector"},
            {"id": "D", "text": "A host-based antivirus engine"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "URL, HTTP method, status code, bytes, and the associated user are hallmarks of web "
                       "proxy logs, which record and often control users' web requests.",
            "distractors": {
                "B": "An IPS logs signature matches on packet content, not per-request URL/method/status detail with a username.",
                "C": "NetFlow records flow metadata (5-tuple, counts), not URLs or HTTP methods.",
                "D": "Antivirus logs reference files and detections, not web request URLs and status codes.",
            },
            "exam_pattern": "URL + method + status code + user = web proxy log.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.1 Map the provided events to source technologies"],
    },
    {
        "id": "cbrops-intr-r2-015", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_ids_ips_events", "difficulty": 3, "type": "mcq",
        "stem": "An IPS logs that it DROPPED an inbound exploit attempt before it reached the target "
                "server. For impact analysis, how should an analyst classify the outcome of this event?",
        "options": [
            {"id": "A", "text": "No impact - the malicious attempt was correctly detected and blocked"},
            {"id": "B", "text": "High impact - data was exfiltrated from the server"},
            {"id": "C", "text": "A false negative - the attack was missed"},
            {"id": "D", "text": "Benign - the traffic was normal and authorized"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The IPS detected a real attack (true positive) and prevented it inline, so the outcome "
                       "is no impact - the exploit never reached the target.",
            "distractors": {
                "B": "Nothing was exfiltrated; the attempt was blocked before reaching the server.",
                "C": "It is not a false negative; the IPS did detect and act on the attack.",
                "D": "The traffic was a genuine exploit attempt, not benign authorized activity.",
            },
            "exam_pattern": "Real attack detected AND blocked inline = true positive, no impact.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.2 Compare impact and no impact for these items"],
    },

    # ===== cbr_firewall_filtering ===========================================
    {
        "id": "cbrops-intr-r2-016", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_firewall_filtering", "difficulty": 2, "type": "mcq",
        "stem": "A firewall terminates the client's connection and then makes the request to the server "
                "on the client's behalf, fully inspecting application-layer content in between. What type "
                "of firewall is this?",
        "options": [
            {"id": "A", "text": "A proxy (application-layer gateway) firewall"},
            {"id": "B", "text": "A stateless packet filter"},
            {"id": "C", "text": "A simple NAT router"},
            {"id": "D", "text": "A Layer 2 switch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A proxy/application-layer gateway sits between client and server as an intermediary, "
                       "terminating and re-originating connections so it can deeply inspect and control application content.",
            "distractors": {
                "B": "A stateless packet filter only checks headers per packet; it does not proxy connections or inspect application content.",
                "C": "A NAT router rewrites addresses; it does not act as an application-layer intermediary.",
                "D": "A Layer 2 switch forwards frames by MAC; it performs no application-layer proxying.",
            },
            "exam_pattern": "Terminates and re-originates the connection to inspect app content = proxy/application gateway firewall.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.3 Compare deep packet inspection with packet filtering and stateful firewall operation"],
    },
    {
        "id": "cbrops-intr-r2-017", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_firewall_filtering", "difficulty": 3, "type": "mcq",
        "stem": "Why can a STATELESS packet filter be tricked into permitting malicious inbound traffic "
                "that a stateful firewall would block?",
        "options": [
            {"id": "A", "text": "It evaluates each packet in isolation with no connection state, so a crafted packet can match a permissive rule"},
            {"id": "B", "text": "It inspects full payloads and is overwhelmed by volume"},
            {"id": "C", "text": "It always blocks packets belonging to established connections"},
            {"id": "D", "text": "It decrypts TLS incorrectly and lets everything through"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A stateless filter has no memory of connections, so a packet crafted to look like "
                       "allowed return traffic (e.g., a lone ACK) can slip through a permissive rule; a stateful firewall would see it matches no real session.",
            "distractors": {
                "B": "Stateless filters check only headers, not full payloads, so payload volume is not the issue.",
                "C": "It does not track established connections at all - that lack of state is the weakness.",
                "D": "Stateless filtering does not involve TLS decryption.",
            },
            "exam_pattern": "No connection state -> crafted 'reply' packets bypass stateless rules (stateful would reject).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.3 Compare deep packet inspection with packet filtering and stateful firewall operation"],
    },
    {
        "id": "cbrops-intr-r2-018", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_firewall_filtering", "difficulty": 2, "type": "mcq",
        "stem": "Which task specifically REQUIRES deep packet inspection rather than simple 5-tuple packet "
                "filtering?",
        "options": [
            {"id": "A", "text": "Detecting a known exploit signature or a sensitive-data pattern inside the packet payload"},
            {"id": "B", "text": "Allowing or denying traffic by destination port number"},
            {"id": "C", "text": "Blocking a specific source IP address"},
            {"id": "D", "text": "Counting bytes transferred per flow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matching content inside the payload (an exploit signature, a credit-card pattern) "
                       "requires DPI to look beyond headers; header-only filtering cannot see payload content.",
            "distractors": {
                "B": "Allowing/denying by port uses header fields - basic packet filtering handles it.",
                "C": "Blocking by source IP is a header check, no DPI needed.",
                "D": "Counting bytes per flow is flow accounting (e.g., NetFlow), not payload inspection.",
            },
            "exam_pattern": "Need to inspect PAYLOAD content (signatures/sensitive data) = requires DPI.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.3 Compare deep packet inspection with packet filtering and stateful firewall operation"],
    },
    {
        "id": "cbrops-intr-r2-019", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_firewall_filtering", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A well-configured firewall follows a default-______ posture (an "
                "implicit deny), permitting only traffic that is explicitly allowed and blocking "
                "everything else. (one word)",
        "correct": ["deny", "default deny", "default-deny"],
        "explanation": {
            "correct": "Default-deny (implicit deny) blocks all traffic unless a rule explicitly permits it, "
                       "minimizing exposure by allowing only known-good flows.",
            "exam_pattern": "Permit only what is explicitly allowed, block the rest = default-deny / implicit deny.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.3 Compare deep packet inspection with packet filtering and stateful firewall operation"],
    },

    # ===== cbr_intrusion_artifacts ==========================================
    {
        "id": "cbrops-intr-r2-020", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_intrusion_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "An endpoint alert's artifacts include a process named svch0st.exe (with a zero) spawned "
                "from an unusual path, plus a new registry Run-key value it created. Why are these "
                "artifacts valuable?",
        "options": [
            {"id": "A", "text": "They identify the malicious process and its persistence mechanism, usable as host IOCs to detect and remediate across the fleet"},
            {"id": "B", "text": "They reveal the attacker's account password"},
            {"id": "C", "text": "They decrypt the host's network traffic"},
            {"id": "D", "text": "They are irrelevant without the packet payload"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A masquerading process name (svch0st vs svchost) from an odd path and a new Run-key both "
                       "pinpoint the malware and how it persists - strong host IOCs to hunt and clean up everywhere.",
            "distractors": {
                "B": "Process and registry artifacts do not contain user passwords.",
                "C": "These host artifacts do not decrypt network traffic.",
                "D": "Host process/registry artifacts are valuable on their own; they do not require packet payload.",
            },
            "exam_pattern": "Masquerading process name + new Run key = malware identity + persistence IOCs.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.9 Interpret common artifact elements from an event to identify an alert"],
    },
    {
        "id": "cbrops-intr-r2-021", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_intrusion_artifacts", "difficulty": 2, "type": "mcq",
        "stem": "In an alert for an inbound web attack, the SOURCE IP is an external address and the "
                "DESTINATION IP is an internal web server. Which address identifies the likely attacker, "
                "and which the target?",
        "options": [
            {"id": "A", "text": "Source = attacker; Destination = target/victim"},
            {"id": "B", "text": "Source = victim; Destination = attacker"},
            {"id": "C", "text": "Both addresses are the attacker"},
            {"id": "D", "text": "Neither can be determined from addresses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "For inbound traffic, the source address is where the attack originates (the attacker) and "
                       "the destination is the internal asset under attack (the target).",
            "distractors": {
                "B": "This reverses the roles; the external source initiated the inbound attack.",
                "C": "The internal destination is the victim, not another attacker.",
                "D": "Direction and addresses do indicate the likely attacker and target for an inbound event.",
            },
            "exam_pattern": "Inbound attack: source IP = attacker, destination IP = target/victim.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.9 Interpret common artifact elements from an event to identify an alert"],
    },
    {
        "id": "cbrops-intr-r2-022", "exam": "cbrops", "domain": "cbr_network_intrusion",
        "subtopic": "cbr_intrusion_artifacts", "difficulty": 3, "type": "mcq",
        "stem": "A web server alert shows the request URI '/admin/../../etc/passwd'. What does this URI "
                "artifact most likely indicate?",
        "options": [
            {"id": "A", "text": "A directory/path traversal attempt to read files outside the web root"},
            {"id": "B", "text": "A normal administrator login"},
            {"id": "C", "text": "A routine DNS lookup"},
            {"id": "D", "text": "An encrypted file transfer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The '../' sequences try to climb out of the web root toward a sensitive system file "
                       "(/etc/passwd); this URI pattern is a classic path/directory traversal attempt.",
            "distractors": {
                "B": "A normal login would not contain '../' traversal sequences aimed at /etc/passwd.",
                "C": "This is an HTTP request URI, not a DNS lookup.",
                "D": "The readable traversal URI is not an encrypted transfer.",
            },
            "exam_pattern": "'../' climbing toward system files in a URI = path/directory traversal attempt.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 4.9 Interpret common artifact elements from an event to identify an alert"],
    },

    # ========================================================================
    # DOMAIN 5: cbr_policies_procedures (16)
    # ========================================================================

    # ===== cbr_incident_handling_nist =======================================
    {
        "id": "cbrops-pol-r2-001", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "A SOC analyst validates incoming alerts, confirms that a genuine incident has occurred, "
                "and determines which systems are affected. Into which NIST SP 800-61 phase do these "
                "actions fall?",
        "options": [
            {"id": "A", "text": "Detection and Analysis"},
            {"id": "B", "text": "Preparation"},
            {"id": "C", "text": "Containment, Eradication and Recovery"},
            {"id": "D", "text": "Post-Incident Activity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Validating alerts, confirming an incident, and scoping impact are the core tasks of the "
                       "Detection and Analysis phase.",
            "distractors": {
                "B": "Preparation is the readiness work (tools, training, plans) done before any incident.",
                "C": "Containment/Eradication/Recovery is the active response that follows confirmation and scoping.",
                "D": "Post-Incident Activity is the retrospective after the incident is resolved.",
            },
            "exam_pattern": "Validate alerts + confirm incident + scope impact = Detection and Analysis.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.4 Map elements to the steps of analysis based on NIST SP 800-61"],
    },
    {
        "id": "cbrops-pol-r2-002", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "After isolating infected hosts, the team removes the malware, disables the breached "
                "accounts, and closes the exploited vulnerability so the threat cannot return. Within "
                "NIST's combined phase, this specific step is:",
        "options": [
            {"id": "A", "text": "Eradication"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Recovery"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Eradication removes the threat and its root cause - deleting malware, disabling "
                       "compromised accounts, and remediating the exploited weakness.",
            "distractors": {
                "B": "Containment limits the spread (e.g., isolating hosts) but does not remove the threat itself.",
                "C": "Recovery restores clean systems to production after eradication.",
                "D": "Preparation is pre-incident readiness, not removal of an active threat.",
            },
            "exam_pattern": "Remove malware + close the root cause = Eradication (contain = isolate, recover = restore).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.4 Map elements to the steps of analysis based on NIST SP 800-61"],
    },
    {
        "id": "cbrops-pol-r2-003", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "The team restores cleaned systems from known-good backups, validates them, and returns "
                "them to production while watching closely for any recurrence. Which NIST SP 800-61 step "
                "is this?",
        "options": [
            {"id": "A", "text": "Recovery"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Detection and Analysis"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recovery brings systems safely back into operation - restoring from clean backups, "
                       "validating, and monitoring to confirm the threat does not reappear.",
            "distractors": {
                "B": "Eradication removes the threat; recovery is the subsequent restoration to service.",
                "C": "Detection and Analysis identifies and scopes the incident, earlier in the lifecycle.",
                "D": "Preparation is the readiness work before an incident occurs.",
            },
            "exam_pattern": "Restore from clean backups + validate + return to production = Recovery.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.4 Map elements to the steps of analysis based on NIST SP 800-61"],
    },
    {
        "id": "cbrops-pol-r2-004", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_incident_handling_nist", "difficulty": 2, "type": "mcq",
        "stem": "Per NIST SP 800-61, why should stakeholders such as Legal, HR, and Public Relations be "
                "identified in the incident response plan BEFORE an incident occurs?",
        "options": [
            {"id": "A", "text": "So the right parties can be engaged quickly for legal, personnel, and communication decisions during a response"},
            {"id": "B", "text": "Because they personally perform the technical malware removal"},
            {"id": "C", "text": "Because they are never involved in incident response"},
            {"id": "D", "text": "To replace the CSIRT during active incidents"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IR plan pre-defines stakeholders and their roles so legal exposure, employee matters, "
                       "and external messaging are handled quickly by the right people when an incident hits.",
            "distractors": {
                "B": "Legal/HR/PR provide their specialized functions; they do not perform hands-on malware removal.",
                "C": "They are important stakeholders in response, not uninvolved.",
                "D": "They support, not replace, the CSIRT that coordinates the technical response.",
            },
            "exam_pattern": "Pre-identify Legal/HR/PR stakeholders so decisions happen fast during response.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.5 Map the organization stakeholders against the NIST IR categories"],
    },

    # ===== cbr_attack_frameworks ============================================
    {
        "id": "cbrops-pol-r2-005", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "An adversary couples an exploit with a backdoor to build a deliverable malicious payload "
                "- for example embedding it in a PDF - BEFORE sending it to any victim. Which Cyber Kill "
                "Chain stage is this?",
        "options": [
            {"id": "A", "text": "Weaponization"},
            {"id": "B", "text": "Delivery"},
            {"id": "C", "text": "Exploitation"},
            {"id": "D", "text": "Installation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Weaponization is building the deliverable payload (coupling an exploit with a backdoor), "
                       "which happens after reconnaissance and before delivery.",
            "distractors": {
                "B": "Delivery is transmitting the finished payload to the target, a later stage.",
                "C": "Exploitation is triggering the vulnerability on the victim after delivery.",
                "D": "Installation is the malware establishing itself on the host after exploitation.",
            },
            "exam_pattern": "Build the payload (exploit + backdoor) before sending = Weaponization.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-r2-006", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "A victim opens a malicious attachment and the embedded code triggers a vulnerability to "
                "run on the host. Which Cyber Kill Chain stage is the triggering of that vulnerability?",
        "options": [
            {"id": "A", "text": "Exploitation"},
            {"id": "B", "text": "Installation"},
            {"id": "C", "text": "Delivery"},
            {"id": "D", "text": "Actions on Objectives"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Exploitation is the moment the delivered payload triggers a vulnerability to execute "
                       "code on the target.",
            "distractors": {
                "B": "Installation is the malware persisting on the host, which follows successful exploitation.",
                "C": "Delivery got the payload to the victim; exploitation is the subsequent triggering.",
                "D": "Actions on Objectives is the final goal (e.g., exfiltration), after control is established.",
            },
            "exam_pattern": "Delivered code triggers the vulnerability to execute = Exploitation (then Installation).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-r2-007", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "In the Diamond Model of Intrusion Analysis, the malware, exploits, and tools an adversary "
                "uses map to which core feature?",
        "options": [
            {"id": "A", "text": "Capability"},
            {"id": "B", "text": "Infrastructure"},
            {"id": "C", "text": "Adversary"},
            {"id": "D", "text": "Victim"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Capability is the Diamond Model vertex for the adversary's tools and techniques - "
                       "malware, exploits, and other capabilities used in the intrusion.",
            "distractors": {
                "B": "Infrastructure is the delivery/control systems (domains, IPs, C2 servers) the adversary uses.",
                "C": "Adversary is the actor behind the intrusion, not the tools themselves.",
                "D": "Victim is the targeted organization, asset, or person.",
            },
            "exam_pattern": "Diamond Model: tools/malware/exploits = Capability; domains/IPs/C2 = Infrastructure.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },
    {
        "id": "cbrops-pol-r2-008", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_attack_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "The VERIS framework (used in the Verizon DBIR) structures each incident around four "
                "elements, the '4 A's'. Which set correctly lists them?",
        "options": [
            {"id": "A", "text": "Actor, Action, Asset, Attribute"},
            {"id": "B", "text": "Adversary, Capability, Infrastructure, Victim"},
            {"id": "C", "text": "Preparation, Detection, Containment, Recovery"},
            {"id": "D", "text": "Confidentiality, Integrity, Availability, Accountability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VERIS (Vocabulary for Event Recording and Incident Sharing) records each incident as "
                       "Actor (who), Action (how), Asset (what was affected), and Attribute (how it was affected) - the 4 A's.",
            "distractors": {
                "B": "Adversary/Capability/Infrastructure/Victim are the Diamond Model vertices, not VERIS.",
                "C": "Those are NIST SP 800-61 incident-response phases, not the VERIS elements.",
                "D": "Those mix CIA-triad pillars with accountability; they are not the VERIS 4 A's.",
            },
            "exam_pattern": "VERIS 4 A's = Actor, Action, Asset, Attribute (Diamond = Adversary/Capability/Infrastructure/Victim).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.10 Classify intrusion events into categories (Cyber Kill Chain, Diamond Model)"],
    },

    # ===== cbr_chain_of_custody =============================================
    {
        "id": "cbrops-pol-r2-009", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 3, "type": "mcq",
        "stem": "Following the NIST SP 800-86 order of volatility, which of these data sources should be "
                "collected LAST because it is the LEAST volatile?",
        "options": [
            {"id": "A", "text": "Data on archival/backup media"},
            {"id": "B", "text": "CPU registers and cache"},
            {"id": "C", "text": "The contents of RAM"},
            {"id": "D", "text": "The ARP cache and active network connections"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Archival/backup media is the most stable, least volatile source, so it is collected last; "
                       "the most volatile data (registers/cache, then RAM and network state) must be captured first.",
            "distractors": {
                "B": "CPU registers and cache are the MOST volatile - collected first, not last.",
                "C": "RAM is volatile and lost at power-off, so it is collected early.",
                "D": "The ARP cache and live connections are volatile network state, captured early.",
            },
            "exam_pattern": "Order of volatility: registers/cache -> RAM -> network state -> disk -> archival media (last).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.6 Describe concepts as documented in NIST SP 800-86"],
    },
    {
        "id": "cbrops-pol-r2-010", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 2, "type": "mcq",
        "stem": "When acquiring a forensic image from a suspect drive, an analyst connects it through a "
                "hardware write blocker. What is the primary reason?",
        "options": [
            {"id": "A", "text": "To prevent any modification of the source evidence during imaging, preserving its integrity"},
            {"id": "B", "text": "To speed up the copy by caching writes"},
            {"id": "C", "text": "To decrypt the drive automatically"},
            {"id": "D", "text": "To compress the image to save space"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A write blocker permits reads but blocks writes to the source, ensuring the original "
                       "evidence is not altered during acquisition - critical for integrity and admissibility.",
            "distractors": {
                "B": "A write blocker protects evidence; it is not a performance/caching device.",
                "C": "Write blockers do not decrypt drives.",
                "D": "Compression is a function of imaging software, not a write blocker's purpose.",
            },
            "exam_pattern": "Write blocker = read-only access to the source so evidence stays unaltered.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.6 Describe concepts as documented in NIST SP 800-86"],
    },
    {
        "id": "cbrops-pol-r2-011", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_chain_of_custody", "difficulty": 2, "type": "mcq",
        "stem": "Which information must a chain-of-custody record capture each time a piece of evidence "
                "changes hands?",
        "options": [
            {"id": "A", "text": "Who had the evidence, when, what was done with it, and each transfer - with signatures"},
            {"id": "B", "text": "The suspect's personal motive for the crime"},
            {"id": "C", "text": "The current market value of the affected asset"},
            {"id": "D", "text": "The geolocation of the attacker's home"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A chain-of-custody log documents custody and handling over time - who, when, what, and "
                       "each transfer, with signatures - so the evidence's integrity can be demonstrated in court.",
            "distractors": {
                "B": "Motive is an investigative conclusion, not a custody-log field.",
                "C": "Asset value is not part of tracking evidence handling.",
                "D": "Attacker geolocation is investigative data, not a chain-of-custody entry.",
            },
            "exam_pattern": "Chain of custody records who/when/what/transfer (with signatures) for each handoff.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 3.3 Describe the role of attribution in an investigation"],
    },

    # ===== cbr_csirt_metrics ================================================
    {
        "id": "cbrops-pol-r2-012", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A SOC measures the average time from when an incident is DETECTED to when the team "
                "begins effective response actions. Which metric is this?",
        "options": [
            {"id": "A", "text": "Mean time to respond (time to respond)"},
            {"id": "B", "text": "Mean time to detect (MTTD)"},
            {"id": "C", "text": "Time to contain"},
            {"id": "D", "text": "Mean time between failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Time to respond measures how quickly responders begin acting once an incident is "
                       "detected; shorter is better for limiting damage.",
            "distractors": {
                "B": "MTTD measures time from incident start to detection, before response begins.",
                "C": "Time to contain measures how long to stop the incident spreading, a related but distinct interval.",
                "D": "MTBF is a hardware reliability metric, not an incident-response timing metric.",
            },
            "exam_pattern": "Detection -> start of response interval = time to respond.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.11 Describe the relationship of SOC metrics to scope analysis"],
    },
    {
        "id": "cbrops-pol-r2-013", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 2, "type": "mcq",
        "stem": "The total length of time an attacker remains undetected in an environment, from the "
                "initial compromise until detection, is commonly called:",
        "options": [
            {"id": "A", "text": "Dwell time"},
            {"id": "B", "text": "Uptime"},
            {"id": "C", "text": "Time to live (TTL)"},
            {"id": "D", "text": "Mean time between failures"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dwell time is how long an adversary goes undetected inside the environment; reducing "
                       "MTTD directly shrinks dwell time and the damage an attacker can do.",
            "distractors": {
                "B": "Uptime measures how long a system stays operational, unrelated to attacker presence.",
                "C": "TTL is a packet's hop/lifetime counter in IP, not a measure of attacker dwell.",
                "D": "MTBF is a reliability metric for hardware, not intrusion dwell time.",
            },
            "exam_pattern": "Time an attacker stays undetected (compromise -> detection) = dwell time.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.11 Describe the relationship of SOC metrics to scope analysis"],
    },
    {
        "id": "cbrops-pol-r2-014", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_csirt_metrics", "difficulty": 3, "type": "mcq",
        "stem": "Why does lowering mean time to detect (MTTD) and time to contain reduce the overall "
                "impact of an incident?",
        "options": [
            {"id": "A", "text": "Less attacker dwell time means fewer systems compromised and less data lost before the threat is stopped"},
            {"id": "B", "text": "It eliminates all vulnerabilities in the environment"},
            {"id": "C", "text": "It guarantees that no future incidents can occur"},
            {"id": "D", "text": "It increases the organization's attack surface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The faster a threat is detected and contained, the less time it has to spread and "
                       "exfiltrate, so the blast radius and total loss shrink.",
            "distractors": {
                "B": "Faster detection/containment limits impact; it does not remove underlying vulnerabilities.",
                "C": "No metric can guarantee that incidents never happen.",
                "D": "Improving response does not expand the attack surface; it reduces impact.",
            },
            "exam_pattern": "Lower MTTD/containment time -> less dwell time -> smaller blast radius and loss.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.11 Describe the relationship of SOC metrics to scope analysis"],
    },

    # ===== cbr_runbook_automation ===========================================
    {
        "id": "cbrops-pol-r2-015", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_runbook_automation", "difficulty": 2, "type": "mcq",
        "stem": "A playbook specifies that a Tier-1 analyst escalates an alert to Tier-2 when defined "
                "criteria are met. What is the main benefit of documenting such escalation steps in the "
                "playbook?",
        "options": [
            {"id": "A", "text": "Consistent, timely handoffs so incidents reach the right expertise without delay or omission"},
            {"id": "B", "text": "It removes the need for any Tier-2 analysts"},
            {"id": "C", "text": "It automatically blocks the attack at the firewall"},
            {"id": "D", "text": "It encrypts the alert so no one can read it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Documented escalation criteria make handoffs consistent and timely, so incidents are "
                       "routed to the right expertise and nothing is dropped between tiers.",
            "distractors": {
                "B": "Escalation routes work to Tier-2; it does not eliminate the need for them.",
                "C": "A playbook step for escalation does not itself block traffic at the firewall.",
                "D": "Escalation is about routing and handoff, not encrypting alerts.",
            },
            "exam_pattern": "Playbook escalation criteria = consistent, timely handoffs to the right responders.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.3 Apply the incident handling process (NIST SP 800-61) to an event"],
    },
    {
        "id": "cbrops-pol-r2-016", "exam": "cbrops", "domain": "cbr_policies_procedures",
        "subtopic": "cbr_runbook_automation", "difficulty": 2, "type": "mcq",
        "stem": "Which type of SOC task is the BEST candidate for run book automation (RBA)?",
        "options": [
            {"id": "A", "text": "High-volume, well-defined, repetitive tasks with clear decision logic, such as enriching an alert with reputation data"},
            {"id": "B", "text": "Novel incidents that require human judgment, creativity, and investigation"},
            {"id": "C", "text": "Sensitive legal decisions about disclosure obligations"},
            {"id": "D", "text": "Executive crisis communications to the public"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation pays off on repetitive, high-volume tasks with clear, deterministic steps "
                       "(like IOC enrichment), freeing analysts for work that needs judgment.",
            "distractors": {
                "B": "Novel incidents need human analysis and creativity - poor fits for rote automation.",
                "C": "Sensitive legal decisions require human judgment and accountability, not automation.",
                "D": "Executive crisis communication is a human leadership task, not an automated playbook step.",
            },
            "exam_pattern": "Automate high-volume, well-defined, repetitive tasks; leave judgment calls to humans.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 5.3 Apply the incident handling process (NIST SP 800-61) to an event"],
    },
]
