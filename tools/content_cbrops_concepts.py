"""Cisco CyberOps Associate (CBROPS 200-201) pool - Domain 1: Security Concepts.

Original, objective-aligned practice items for the six Security Concepts
subtopics tracked in CertLab:
  * cbr_cia_defense          - the CIA triad (confidentiality, integrity,
                               availability) and the defense-in-depth strategy.
  * cbr_security_terms       - core SOC vocabulary: least privilege, threat
                               hunting, zero trust, threat intelligence,
                               reverse engineering, run book automation.
  * cbr_access_control_models- DAC, MAC, RBAC, rule-based and time-based access
                               control and how each decides who gets access.
  * cbr_cvss                 - CVSS v3.x base metrics (AV, AC, PR, UI, S, C, I, A)
                               and the qualitative severity bands.
  * cbr_risk_terms           - distinguishing threat, vulnerability, exploit and
                               risk, and basic risk scoring.
  * cbr_soc_analysis_tools   - SIEM, SOAR / orchestration and log management and
                               how a SOC uses each.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a key authored here as "A" is not positionally
biased, every wrong option carries a distractor note, and each item cites the
public Cisco 200-201 exam topic it draws on. Blue-team / analyst depth only -
defensive, monitoring-focused scenarios, no offensive payloads, and never real
or memorized exam items.
"""

QUESTIONS = [
    # ===== cbr_cia_defense ==================================================
    {
        "id": "cbrops-con-001", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 1, "type": "mcq",
        "stem": "A control is designed to ensure that stored records cannot be altered by "
                "unauthorized users so their accuracy can be trusted. Which element of the CIA "
                "triad does this control protect?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Integrity ensures data is not modified by unauthorized parties and stays "
                       "accurate and trustworthy; hashing and access controls help enforce it.",
            "distractors": {
                "A": "Confidentiality protects against unauthorized disclosure, not unauthorized modification.",
                "C": "Availability ensures timely, reliable access to data, not that it stays unaltered.",
                "D": "Non-repudiation assures an action cannot be denied; it is not one of the three CIA elements.",
            },
            "exam_pattern": "Unauthorized modification / accuracy / trustworthiness = Integrity.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.1 Describe the CIA triad"],
    },
    {
        "id": "cbrops-con-002", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 2, "type": "mcq",
        "stem": "A volumetric DDoS attack floods a public web server until legitimate users can no "
                "longer reach the site, though no data is read or changed. Which pillar of the CIA "
                "triad is most directly impacted?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Authentication"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Availability is the assurance that systems and data are accessible when needed; "
                       "a DoS/DDoS that exhausts resources and blocks access attacks availability.",
            "distractors": {
                "A": "Confidentiality concerns disclosure of data, but nothing was read or exposed here.",
                "B": "Integrity concerns unauthorized change of data, but nothing was altered.",
                "D": "Authentication verifies identity and is not one of the three CIA pillars.",
            },
            "exam_pattern": "DoS/DDoS, resource exhaustion, 'cannot reach the service' = Availability.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.1 Describe the CIA triad"],
    },
    {
        "id": "cbrops-con-003", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cia_defense", "difficulty": 2, "type": "mcq",
        "stem": "A security architecture layers a perimeter firewall, a network IPS, endpoint "
                "antimalware, and encryption of data at rest so that no single control failure "
                "exposes the protected asset. Which strategy does this describe?",
        "options": [
            {"id": "A", "text": "Defense in depth"},
            {"id": "B", "text": "Principle of least privilege"},
            {"id": "C", "text": "Zero trust"},
            {"id": "D", "text": "Separation of duties"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defense in depth layers multiple, independent controls so that if one fails the "
                       "others still protect the asset.",
            "distractors": {
                "B": "Least privilege limits each identity to the minimum access needed; it is one control, not the layered strategy.",
                "C": "Zero trust removes implicit trust and verifies every request; related, but not the 'multiple layers' definition.",
                "D": "Separation of duties splits a task among people to prevent fraud, not a stack of technical defenses.",
            },
            "exam_pattern": "Multiple independent layers so one failure is not fatal = defense in depth.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.5 Describe the principles of the defense-in-depth strategy"],
    },

    # ===== cbr_security_terms ===============================================
    {
        "id": "cbrops-con-004", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 1, "type": "mcq",
        "stem": "A new SOC analyst is granted only the specific log-review and ticketing permissions "
                "the job requires, and nothing more. Which security principle is being applied?",
        "options": [
            {"id": "A", "text": "Defense in depth"},
            {"id": "B", "text": "Separation of duties"},
            {"id": "C", "text": "Principle of least privilege"},
            {"id": "D", "text": "Due diligence"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The principle of least privilege grants each user, process, or system only the "
                       "minimum access needed to perform its function, limiting damage if the account is misused.",
            "distractors": {
                "A": "Defense in depth is about layering controls, not minimizing an account's access.",
                "B": "Separation of duties divides a sensitive task among multiple people.",
                "D": "Due diligence is the ongoing effort to maintain security, not a minimal-access rule.",
            },
            "exam_pattern": "Minimum access needed to do the job = least privilege.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },
    {
        "id": "cbrops-con-005", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 2, "type": "mcq",
        "stem": "Rather than waiting for alerts to fire, an analyst forms a hypothesis and proactively "
                "searches historical telemetry for signs of an adversary that evaded existing "
                "detections. What is this activity called?",
        "options": [
            {"id": "A", "text": "Threat hunting"},
            {"id": "B", "text": "Penetration testing"},
            {"id": "C", "text": "Reverse engineering"},
            {"id": "D", "text": "Incident eradication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat hunting is the proactive, hypothesis-driven search through telemetry for "
                       "threats that automated detections missed, rather than reacting to alerts.",
            "distractors": {
                "B": "Penetration testing is authorized offensive testing to find exploitable weaknesses, not a search for intruders in logs.",
                "C": "Reverse engineering deconstructs malware or software to understand how it works.",
                "D": "Eradication removes a confirmed threat after detection; it is a later incident-response step.",
            },
            "exam_pattern": "Proactive, hypothesis-driven search for undetected threats = threat hunting.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },
    {
        "id": "cbrops-con-006", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_security_terms", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The security model that eliminates implicit trust based on network "
                "location and instead continuously verifies every user, device, and request is known "
                "as the ______ model. (two words)",
        "correct": ["zero trust", "zero-trust", "zerotrust", "zero trust model"],
        "explanation": {
            "correct": "Zero trust assumes no implicit trust inside or outside the perimeter and requires "
                       "continuous authentication and authorization - 'never trust, always verify' - for every access request.",
            "exam_pattern": "'Never trust, always verify' / no implicit trust by location = zero trust.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.3 Describe security terms"],
    },

    # ===== cbr_access_control_models ========================================
    {
        "id": "cbrops-con-007", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "On a file server, the owner of each file decides which other users may read or modify "
                "it and sets those permissions directly. Which access control model is in use?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Mandatory access control (MAC)"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "Rule-based access control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In DAC the resource owner has discretion to decide who may access the object and "
                       "grants permissions at will - exactly the file-owner behavior described.",
            "distractors": {
                "B": "Under MAC the system enforces access using labels and clearances; owners cannot choose.",
                "C": "RBAC ties access to job roles, not to the owner's discretion.",
                "D": "Rule-based control applies administrator-defined global rules (e.g., ACL conditions), not owner choice.",
            },
            "exam_pattern": "Resource owner decides who gets access = DAC.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },
    {
        "id": "cbrops-con-008", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "In a classified system, access is enforced by the operating system using security "
                "labels (such as Secret and Top Secret) matched against user clearances, and "
                "individual users cannot override these decisions. Which model is this?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Role-based access control (RBAC)"},
            {"id": "C", "text": "Mandatory access control (MAC)"},
            {"id": "D", "text": "Attribute-based access control (ABAC)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MAC enforces access centrally through security labels and clearances set by the "
                       "system (not the user), which is why it is common in military and classified environments.",
            "distractors": {
                "A": "DAC lets owners set permissions at their discretion - the opposite of system-enforced labels.",
                "B": "RBAC groups permissions by job role, not by classification labels and clearances.",
                "D": "ABAC decides by attributes and policy; the defining label-and-clearance enforcement described is MAC.",
            },
            "exam_pattern": "Security labels + clearances, system-enforced, military/classified = MAC.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },
    {
        "id": "cbrops-con-009", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_access_control_models", "difficulty": 1, "type": "mcq",
        "stem": "A company grants permissions by job function: every account in the 'SOC Analyst' role "
                "automatically receives the same rights, and moving a user to a different role changes "
                "their access. Which access control model is this?",
        "options": [
            {"id": "A", "text": "Role-based access control (RBAC)"},
            {"id": "B", "text": "Discretionary access control (DAC)"},
            {"id": "C", "text": "Mandatory access control (MAC)"},
            {"id": "D", "text": "Time-based access control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC assigns permissions to roles rather than to individuals; users inherit rights "
                       "by their role, which simplifies administration as people change jobs.",
            "distractors": {
                "B": "DAC leaves access to the owner's discretion, not tied to a defined role.",
                "C": "MAC uses labels and clearances enforced by the system, not job roles.",
                "D": "Time-based control grants access only during permitted time windows, which is not what is described.",
            },
            "exam_pattern": "Permissions attached to a job role/function = RBAC.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.6 Compare access control models"],
    },

    # ===== cbr_cvss =========================================================
    {
        "id": "cbrops-con-010", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "In CVSS v3.1, which base metric expresses the context from which exploitation is "
                "possible, using the values Network, Adjacent, Local, and Physical?",
        "options": [
            {"id": "A", "text": "Attack Complexity (AC)"},
            {"id": "B", "text": "Attack Vector (AV)"},
            {"id": "C", "text": "Privileges Required (PR)"},
            {"id": "D", "text": "Scope (S)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Attack Vector (AV) reflects how 'remote' an attacker can be; its values are "
                       "Network, Adjacent, Local, and Physical.",
            "distractors": {
                "A": "Attack Complexity describes conditions beyond the attacker's control (Low/High), not where the attack originates.",
                "C": "Privileges Required is the privilege level the attacker must already hold (None/Low/High).",
                "D": "Scope indicates whether impact crosses a security authority boundary (Unchanged/Changed).",
            },
            "exam_pattern": "Network/Adjacent/Local/Physical = Attack Vector (AV).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-011", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 3, "type": "mcq",
        "stem": "A CVSS v3.1 assessment notes that exploiting a hypervisor flaw lets the attacker "
                "affect guest VMs that sit beyond the vulnerable component's own security authority. "
                "Which base metric captures this condition?",
        "options": [
            {"id": "A", "text": "Confidentiality (C)"},
            {"id": "B", "text": "Attack Vector (AV)"},
            {"id": "C", "text": "User Interaction (UI)"},
            {"id": "D", "text": "Scope (S)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Scope (Unchanged vs Changed) captures whether a successful exploit can impact "
                       "resources beyond the security authority of the vulnerable component - here, other VMs.",
            "distractors": {
                "A": "Confidentiality measures the impact to data confidentiality, not whether impact crosses a boundary.",
                "B": "Attack Vector describes where the attack originates, not the spread of impact.",
                "C": "User Interaction states whether a human must participate (None/Required).",
            },
            "exam_pattern": "Impact crosses a security authority boundary (Unchanged vs Changed) = Scope.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },
    {
        "id": "cbrops-con-012", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_cvss", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability is published with a CVSS v3.1 base score of 9.8. Into which qualitative "
                "severity rating does that score fall?",
        "options": [
            {"id": "A", "text": "Critical"},
            {"id": "B", "text": "High"},
            {"id": "C", "text": "Medium"},
            {"id": "D", "text": "Low"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On the CVSS v3.1 qualitative scale, 9.0-10.0 is Critical, so a 9.8 base score is Critical.",
            "distractors": {
                "B": "High covers 7.0-8.9, which is below a 9.8 score.",
                "C": "Medium covers 4.0-6.9.",
                "D": "Low covers 0.1-3.9.",
            },
            "exam_pattern": "CVSS v3 bands: 0.1-3.9 Low, 4.0-6.9 Medium, 7.0-8.9 High, 9.0-10.0 Critical.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.7 Describe terms as defined in CVSS"],
    },

    # ===== cbr_risk_terms ===================================================
    {
        "id": "cbrops-con-013", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 1, "type": "mcq",
        "stem": "In risk terminology, how is a 'vulnerability' best defined?",
        "options": [
            {"id": "A", "text": "A weakness in a system or process that could be exploited"},
            {"id": "B", "text": "A person or event with the potential to cause harm"},
            {"id": "C", "text": "The tool or code used to take advantage of a weakness"},
            {"id": "D", "text": "The probability and impact of a loss event"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A vulnerability is a weakness or flaw (in software, configuration, or process) that "
                       "a threat could exploit.",
            "distractors": {
                "B": "A person or event with potential to cause harm is a threat, not a vulnerability.",
                "C": "The tool or code that leverages a weakness is an exploit.",
                "D": "The probability and impact of a loss is risk.",
            },
            "exam_pattern": "Weakness that could be exploited = vulnerability; who/what causes harm = threat.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },
    {
        "id": "cbrops-con-014", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 3, "type": "mcq",
        "stem": "An unpatched internet-facing server (a known weakness) is being actively targeted by a "
                "worm circulating in the wild. The potential for loss that results from the worm acting "
                "on the weakness is best described as the organization's ______.",
        "options": [
            {"id": "A", "text": "Threat"},
            {"id": "B", "text": "Risk"},
            {"id": "C", "text": "Vulnerability"},
            {"id": "D", "text": "Exploit"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Risk is the potential for loss when a threat acts on a vulnerability; it combines the "
                       "likelihood of that happening with the impact if it does.",
            "distractors": {
                "A": "The worm itself is the threat - the agent with potential to cause harm.",
                "C": "The unpatched server is the vulnerability - the weakness.",
                "D": "The specific code the worm uses to compromise the server is the exploit.",
            },
            "exam_pattern": "Risk = likelihood a threat exploits a vulnerability x impact; it is the potential for loss.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },
    {
        "id": "cbrops-con-015", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_risk_terms", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A piece of software, a chunk of data, or a sequence of commands that "
                "takes advantage of a specific vulnerability to cause unintended behavior on a system is "
                "called a(n) ______.",
        "correct": ["exploit"],
        "explanation": {
            "correct": "An exploit is the actual tool, code, or technique that leverages a vulnerability. "
                       "The vulnerability is the weakness itself; the threat is the actor or event that may use the exploit.",
            "exam_pattern": "Code/technique that leverages a vulnerability = exploit (distinct from the weakness).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.4 Compare security concepts"],
    },

    # ===== cbr_soc_analysis_tools ===========================================
    {
        "id": "cbrops-con-016", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 1, "type": "mcq",
        "stem": "A SOC deploys a platform that ingests logs from firewalls, servers, and endpoints, "
                "normalizes them, and correlates events across sources to generate prioritized alerts "
                "for analysts. Which technology is this?",
        "options": [
            {"id": "A", "text": "SIEM"},
            {"id": "B", "text": "SOAR"},
            {"id": "C", "text": "IPS"},
            {"id": "D", "text": "Certificate authority (CA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM (security information and event management) centrally collects, normalizes, "
                       "and correlates log data from many sources and raises alerts for investigation.",
            "distractors": {
                "B": "SOAR focuses on orchestrating and automating response actions, not primarily on log aggregation and correlation.",
                "C": "An IPS inspects and blocks malicious traffic inline; it is a log source, not the aggregation platform.",
                "D": "A certificate authority issues digital certificates and has nothing to do with log correlation.",
            },
            "exam_pattern": "Central collection + normalization + correlation of logs into alerts = SIEM.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },
    {
        "id": "cbrops-con-017", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 2, "type": "mcq",
        "stem": "To cut response time, a SOC wants a platform that runs automated playbooks to enrich "
                "alerts and push containment actions across its firewall, EDR, and ticketing systems "
                "from one place. Which technology best fits?",
        "options": [
            {"id": "A", "text": "SOAR"},
            {"id": "B", "text": "SIEM"},
            {"id": "C", "text": "NetFlow collector"},
            {"id": "D", "text": "Data loss prevention (DLP)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SOAR (security orchestration, automation, and response) runs playbooks that automate "
                       "enrichment and response across integrated tools, reducing manual effort and response time.",
            "distractors": {
                "B": "A SIEM aggregates and correlates logs and raises alerts but does not natively orchestrate multi-tool automated response.",
                "C": "A NetFlow collector gathers flow records for traffic analysis, not response automation.",
                "D": "DLP focuses on preventing data exfiltration, not orchestrating incident response.",
            },
            "exam_pattern": "Automation + orchestration + playbooks across tools = SOAR.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },
    {
        "id": "cbrops-con-018", "exam": "cbrops", "domain": "cbr_security_concepts",
        "subtopic": "cbr_soc_analysis_tools", "difficulty": 3, "type": "multi",
        "stem": "Which TWO capabilities most distinguish a SOAR platform from a traditional SIEM? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Orchestrating actions across multiple separate security tools"},
            {"id": "B", "text": "Executing automated response playbooks"},
            {"id": "C", "text": "Storing and correlating raw log events"},
            {"id": "D", "text": "Signing and issuing X.509 certificates"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "SOAR adds orchestration across tools and automated playbook-driven response on top of "
                       "detection; those are its defining capabilities versus a SIEM.",
            "distractors": {
                "C": "Storing and correlating logs is the SIEM's core role, not what sets SOAR apart.",
                "D": "Certificate issuance is a PKI/CA function, unrelated to SOAR.",
            },
            "exam_pattern": "SOAR = orchestration + automated playbooks layered on detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.2 Compare security deployments"],
    },
]
