"""(ISC)² Certified in Cybersecurity (CC) pool - Domain 1: Security Principles.

Original, objective-aligned practice items for the five Security Principles
subtopics tracked in CertLab:
  * cc_cia_triad          - confidentiality, integrity, and availability; what
                            each protects and how a scenario maps to one of them.
  * cc_risk_management     - assets, threats, vulnerabilities, likelihood/impact,
                            and the four risk-treatment options (accept, avoid,
                            mitigate, transfer).
  * cc_security_controls   - control functions (preventive, detective, corrective)
                            and control categories (technical, administrative,
                            physical).
  * cc_isc2_ethics         - the (ISC)² Code of Ethics: four canons and how they
                            are applied.
  * cc_governance_policies - the policy hierarchy (policies, standards, procedures,
                            guidelines) and laws/regulations.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the answer key authored here as "A" is not
positionally biased, every wrong option carries a distractor note, and each item
names the (ISC)² CC exam-outline area it draws on. Entry-level depth only - core,
well-established facts, no obscure edge cases, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cc_cia_triad =====================================================
    {
        "id": "isc2cc-prin-001", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad", "difficulty": 1, "type": "mcq",
        "stem": "A security team's main goal for a file of customer records is to make sure only "
                "authorized people can view it. Which element of the CIA triad is this?",
        "options": [
            {"id": "A", "text": "Non-repudiation"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Confidentiality"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Confidentiality is the assurance that information is not disclosed to "
                       "unauthorized people, processes, or devices - exactly the goal of limiting who can view the records.",
            "distractors": {
                "A": "Non-repudiation proves who performed an action; it is not one of the three CIA elements.",
                "B": "Integrity is about preventing unauthorized or improper changes, not about who can view data.",
                "C": "Availability is about keeping data and systems reachable when needed, not restricting viewing.",
            },
            "exam_pattern": "Keep data secret / limit who can read it = confidentiality.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - CIA triad (confidentiality)"],
    },
    {
        "id": "isc2cc-prin-002", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad", "difficulty": 2, "type": "mcq",
        "stem": "An attacker alters the dollar amounts in an accounting database without permission. "
                "Which element of the CIA triad has been violated?",
        "options": [
            {"id": "A", "text": "Availability"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Confidentiality"},
            {"id": "D", "text": "Authentication"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Integrity is the assurance that data is accurate and has not been changed in an "
                       "unauthorized way; altering the stored amounts is an integrity violation.",
            "distractors": {
                "A": "Availability concerns whether data is accessible; here the data is reachable but wrong.",
                "C": "Confidentiality is about disclosure; the problem is unauthorized change, not viewing.",
                "D": "Authentication verifies identity; it is a mechanism, not one of the three CIA elements.",
            },
            "exam_pattern": "Unauthorized or improper modification of data = integrity loss.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - CIA triad (integrity)"],
    },
    {
        "id": "isc2cc-prin-003", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad", "difficulty": 2, "type": "mcq",
        "stem": "A flood of bogus traffic knocks a company's public website offline so customers "
                "cannot reach it. Which element of the CIA triad is most directly affected?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Accountability"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Availability is the assurance that systems and data are accessible to authorized "
                       "users when needed; a denial-of-service outage directly attacks availability.",
            "distractors": {
                "A": "Confidentiality is about disclosure; the data was not necessarily exposed.",
                "B": "Integrity is about accuracy; the data was not altered, just unreachable.",
                "D": "Accountability traces actions to a user; it is not one of the three CIA elements.",
            },
            "exam_pattern": "System/service made unreachable (e.g., DoS) = availability.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - CIA triad (availability)"],
    },
    {
        "id": "isc2cc-prin-004", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad", "difficulty": 1, "type": "fill",
        "stem": "Scrambling data with a cipher so that only authorized parties who hold the key can "
                "read it protects which single element of the CIA triad? (one word)",
        "correct": ["confidentiality", "confidential"],
        "explanation": {
            "correct": "Encryption makes data unreadable to anyone without the key, which protects "
                       "confidentiality - preventing unauthorized disclosure.",
            "exam_pattern": "Encryption's primary CIA goal is confidentiality (secrecy).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - CIA triad (confidentiality)"],
    },

    # ===== cc_risk_management ===============================================
    {
        "id": "isc2cc-prin-005", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_risk_management", "difficulty": 1, "type": "mcq",
        "stem": "A scanner reports that a server is missing a critical patch, leaving a weakness an "
                "attacker could exploit. In risk terms, the missing patch is best described as a:",
        "options": [
            {"id": "A", "text": "Vulnerability"},
            {"id": "B", "text": "Threat"},
            {"id": "C", "text": "Risk"},
            {"id": "D", "text": "Safeguard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A vulnerability is a weakness or gap in a system or control that a threat could "
                       "exploit; an unpatched flaw is a classic vulnerability.",
            "distractors": {
                "B": "A threat is the potential cause of harm (such as the attacker), not the weakness itself.",
                "C": "Risk is the combination of likelihood and impact if a threat exploits the weakness.",
                "D": "A safeguard (control) reduces risk; a missing patch is the opposite of a safeguard.",
            },
            "exam_pattern": "Weakness/gap that can be exploited = vulnerability.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Risk terms (vulnerability)"],
    },
    {
        "id": "isc2cc-prin-006", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "In a risk discussion, a manager asks for the term meaning 'any circumstance or event "
                "with the potential to cause harm,' such as a hacker, malware, or a flood. This is a:",
        "options": [
            {"id": "A", "text": "Vulnerability"},
            {"id": "B", "text": "Threat"},
            {"id": "C", "text": "Control"},
            {"id": "D", "text": "Residual risk"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A threat is any circumstance or event (natural or human) with the potential to "
                       "cause harm by exploiting a vulnerability.",
            "distractors": {
                "A": "A vulnerability is the weakness the threat targets, not the source of harm.",
                "C": "A control is a measure that reduces risk, not a source of potential harm.",
                "D": "Residual risk is the risk left over after controls are applied, not the harm source.",
            },
            "exam_pattern": "The potential source of harm (hacker, malware, flood) = threat; the weakness it targets = vulnerability.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Risk terms (threat)"],
    },
    {
        "id": "isc2cc-prin-007", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "To offset the financial impact of a possible ransomware attack, a company buys a "
                "cyber-insurance policy. Which risk-treatment option is this?",
        "options": [
            {"id": "A", "text": "Risk acceptance"},
            {"id": "B", "text": "Risk avoidance"},
            {"id": "C", "text": "Risk transference"},
            {"id": "D", "text": "Risk mitigation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Risk transference shifts the impact of a risk to a third party; buying insurance "
                       "transfers the financial loss to the insurer.",
            "distractors": {
                "A": "Acceptance means taking no action and absorbing the risk, not paying a third party to carry it.",
                "B": "Avoidance means stopping the risky activity entirely, which insurance does not do.",
                "D": "Mitigation reduces likelihood or impact with controls; insurance does not reduce the chance of attack.",
            },
            "exam_pattern": "Insurance or outsourcing the loss to another party = risk transference.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Risk treatment (transference)"],
    },
    {
        "id": "isc2cc-prin-008", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_risk_management", "difficulty": 2, "type": "fill",
        "stem": "A company decides the security risk of launching a new online feature is too high, so "
                "it cancels the feature entirely. Which risk-treatment option is this? Answer with one word.",
        "correct": ["avoidance", "avoid", "avoiding"],
        "explanation": {
            "correct": "Risk avoidance eliminates the risk by not engaging in the activity that creates "
                       "it; cancelling the feature removes the exposure altogether.",
            "exam_pattern": "Stop/cancel the activity so the risk cannot occur = risk avoidance.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Risk treatment (avoidance)"],
    },

    # ===== cc_security_controls =============================================
    {
        "id": "isc2cc-prin-009", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_security_controls", "difficulty": 1, "type": "mcq",
        "stem": "A firewall rule is configured to block malicious traffic before it can ever reach an "
                "internal server. By its function, this is best classified as which type of control?",
        "options": [
            {"id": "A", "text": "Detective control"},
            {"id": "B", "text": "Corrective control"},
            {"id": "C", "text": "Preventive control"},
            {"id": "D", "text": "Recovery control"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A preventive control stops an unwanted event before it happens; blocking traffic "
                       "at the firewall prevents the attack from reaching the server.",
            "distractors": {
                "A": "A detective control identifies an event after it occurs (e.g., an alert), not before.",
                "B": "A corrective control fixes or restores things after an incident, not beforehand.",
                "D": "A recovery control restores operations after damage; it does not block the event up front.",
            },
            "exam_pattern": "Stops the bad thing before it happens = preventive.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Security controls (preventive)"],
    },
    {
        "id": "isc2cc-prin-010", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "An intrusion detection system does not stop attacks but raises an alert whenever it "
                "spots suspicious activity so staff can investigate. By function, this is a:",
        "options": [
            {"id": "A", "text": "Detective control"},
            {"id": "B", "text": "Preventive control"},
            {"id": "C", "text": "Deterrent control"},
            {"id": "D", "text": "Directive control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A detective control discovers and signals that an event has occurred; an IDS that "
                       "alerts on suspicious activity is a textbook detective control.",
            "distractors": {
                "B": "A preventive control would block the activity, but an IDS only observes and alerts.",
                "C": "A deterrent control discourages an attacker (e.g., a warning sign); an IDS does not warn off attackers.",
                "D": "A directive control instructs behavior (e.g., a policy), not automated detection.",
            },
            "exam_pattern": "Finds and alerts on events after they happen = detective.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Security controls (detective)"],
    },
    {
        "id": "isc2cc-prin-011", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "An organization writes an acceptable-use policy and mandatory security-awareness "
                "training for employees. By category, these are examples of which kind of control?",
        "options": [
            {"id": "A", "text": "Physical controls"},
            {"id": "B", "text": "Technical (logical) controls"},
            {"id": "C", "text": "Compensating controls"},
            {"id": "D", "text": "Administrative (managerial) controls"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Administrative controls are policies, procedures, and training - management-driven "
                       "measures that govern how people behave and how the program is run.",
            "distractors": {
                "A": "Physical controls are tangible barriers like locks, fences, and guards, not policies.",
                "B": "Technical controls are implemented in hardware/software (firewalls, encryption), not written rules.",
                "C": "'Compensating' describes a control's role as a substitute, not the people/policy category.",
            },
            "exam_pattern": "Policies, procedures, training = administrative (managerial) controls.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Security controls (administrative)"],
    },
    {
        "id": "isc2cc-prin-012", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_security_controls", "difficulty": 3, "type": "multi",
        "stem": "A facilities manager lists safeguards for the building. Which TWO are PHYSICAL "
                "security controls? (Choose two.)",
        "options": [
            {"id": "A", "text": "Bollards in front of the entrance"},
            {"id": "B", "text": "A security guard at the lobby desk"},
            {"id": "C", "text": "A host-based firewall on each laptop"},
            {"id": "D", "text": "A written password policy"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Bollards and security guards are tangible, physical controls that protect people, "
                       "equipment, and facilities.",
            "distractors": {
                "C": "A host-based firewall is a technical (logical) control implemented in software.",
                "D": "A password policy is an administrative control - a management rule, not a physical barrier.",
            },
            "exam_pattern": "Tangible barriers and guards = physical; software settings = technical; rules/policies = administrative.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Security controls (physical)"],
    },

    # ===== cc_isc2_ethics ===================================================
    {
        "id": "isc2cc-prin-013", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics", "difficulty": 1, "type": "mcq",
        "stem": "A new member is studying the (ISC)² Code of Ethics. How many canons does the Code "
                "of Ethics contain?",
        "options": [
            {"id": "A", "text": "Two"},
            {"id": "B", "text": "Four"},
            {"id": "C", "text": "Seven"},
            {"id": "D", "text": "Ten"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The (ISC)² Code of Ethics has a preamble plus four canons that every member "
                       "agrees to uphold.",
            "distractors": {
                "A": "Two is too few; the Code has four canons.",
                "C": "Seven does not match the Code of Ethics; there are four canons.",
                "D": "Ten is incorrect; the Code of Ethics defines four canons.",
            },
            "exam_pattern": "(ISC)² Code of Ethics = preamble + four canons.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (canons)"],
    },
    {
        "id": "isc2cc-prin-014", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics", "difficulty": 2, "type": "mcq",
        "stem": "A security professional discovers a flaw in a water-treatment control system that "
                "could endanger the public. Which (ISC)² canon most directly guides them to act?",
        "options": [
            {"id": "A", "text": "Protect society, the common good, necessary public trust and confidence, and the infrastructure"},
            {"id": "B", "text": "Act honorably, honestly, justly, responsibly, and legally"},
            {"id": "C", "text": "Provide diligent and competent service to principals"},
            {"id": "D", "text": "Advance and protect the profession"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The first canon - protect society, the common good, and the infrastructure - "
                       "directly addresses safeguarding public safety and critical infrastructure.",
            "distractors": {
                "B": "Acting honestly is about personal conduct and legality, not specifically protecting the public.",
                "C": "Serving principals concerns duty to employers/clients, not the broader public interest.",
                "D": "Advancing the profession is about the field's reputation, not protecting public safety.",
            },
            "exam_pattern": "Public safety / infrastructure / common good = Canon I (protect society).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (Canon I)"],
    },
    {
        "id": "isc2cc-prin-015", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics", "difficulty": 2, "type": "mcq",
        "stem": "An (ISC)² member is expected to perform competent, high-quality, and diligent work for "
                "the employers and clients they serve. Which canon addresses this duty?",
        "options": [
            {"id": "A", "text": "Protect society, the common good, and the infrastructure"},
            {"id": "B", "text": "Act honorably, honestly, justly, responsibly, and legally"},
            {"id": "C", "text": "Provide diligent and competent service to principals"},
            {"id": "D", "text": "Advance and protect the profession"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The third canon requires diligent and competent service to principals - the "
                       "employers and clients a professional works for.",
            "distractors": {
                "A": "Protecting society addresses the broad public, not specifically the member's employer or client.",
                "B": "Acting honestly governs personal conduct, not the quality of service to principals.",
                "D": "Advancing the profession concerns the field at large, not duty to one's employer or client.",
            },
            "exam_pattern": "Duty/quality of work to employers and clients (principals) = Canon III.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (Canon III)"],
    },

    # ===== cc_governance_policies ===========================================
    {
        "id": "isc2cc-prin-016", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies", "difficulty": 1, "type": "mcq",
        "stem": "Senior management publishes a short, high-level document stating the organization's "
                "overall intent and expectations for protecting information. This document is a:",
        "options": [
            {"id": "A", "text": "Baseline"},
            {"id": "B", "text": "Procedure"},
            {"id": "C", "text": "Guideline"},
            {"id": "D", "text": "Policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A policy is a high-level statement of management's intent and direction; it is "
                       "mandatory but broad, setting the tone for more detailed documents.",
            "distractors": {
                "A": "A baseline defines a minimum security configuration level, not overall management intent.",
                "B": "A procedure is a detailed, step-by-step set of instructions, not a high-level statement.",
                "C": "A guideline offers recommended, non-mandatory advice, whereas a policy states required intent.",
            },
            "exam_pattern": "High-level statement of management intent = policy (top of the governance hierarchy).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Governance (policy)"],
    },
    {
        "id": "isc2cc-prin-017", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies", "difficulty": 2, "type": "mcq",
        "stem": "A help-desk analyst follows a document that lists the exact, ordered steps for resetting "
                "a locked user account. Which type of governance document is this?",
        "options": [
            {"id": "A", "text": "Policy"},
            {"id": "B", "text": "Guideline"},
            {"id": "C", "text": "Procedure"},
            {"id": "D", "text": "Regulation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A procedure provides detailed, step-by-step instructions for carrying out a "
                       "specific task, such as resetting an account.",
            "distractors": {
                "A": "A policy states high-level intent; it does not spell out individual task steps.",
                "B": "A guideline is a recommendation, not a required ordered set of steps.",
                "D": "A regulation is an externally imposed legal requirement, not an internal how-to document.",
            },
            "exam_pattern": "Detailed step-by-step 'how to' = procedure.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Governance (procedure)"],
    },
    {
        "id": "isc2cc-prin-018", "exam": "isc2cc", "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies", "difficulty": 2, "type": "fill",
        "stem": "A mandatory document specifies that all company laptops must use AES-256 full-disk "
                "encryption. In the governance hierarchy, this specific, required rule is called a ___. "
                "(one word)",
        "correct": ["standard", "standards"],
        "explanation": {
            "correct": "A standard is a mandatory rule that specifies the uniform use of a specific "
                       "technology or configuration, supporting the broader policy.",
            "exam_pattern": "Mandatory, specific requirement (exact tech/config) = standard; recommended = guideline.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 1 - Governance (standard)"],
    },
]
