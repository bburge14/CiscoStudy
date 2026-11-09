"""ISACA CISM pool - Domain 1: Information Security Governance.

Original, objective-aligned practice items for the four governance subtopics
tracked in the study engine:
  * cism_governance_framework   - what governance is (vs management), the
                                  policy/standard/procedure/guideline hierarchy,
                                  and governance frameworks (COBIT, ISO/IEC
                                  27001/27002/27014).
  * cism_strategy_alignment     - aligning the security strategy with business
                                  objectives, the steering committee, desired vs
                                  current state / gap, and critical success factors.
  * cism_roles_responsibilities - board/senior management accountability, the
                                  CISO's role, data owner vs custodian, and policy
                                  approval authority.
  * cism_legal_regulatory       - responding to new regulation, due diligence,
                                  harmonising overlapping requirements, and the
                                  limits of outsourcing accountability.

Authoring rules match the other content_*.py pools: the build step shuffles
option order (seeded by id), so a key authored here as "A"/"B"/"C"/"D" is not
positionally biased, every wrong option carries a distractor note, and each item
names the public ISACA objective area it draws on so facts stay traceable.

CISM is a MANAGEMENT exam: keyed answers reflect the information security
manager's view - align security with the business, decide on a risk basis, put
governance before technology, and have the manager facilitate, advise, and
communicate rather than perform hands-on technical work. These are original
items built from public CISM objectives; they are never real or memorised exam
questions.
"""

QUESTIONS = [
    # ===== cism_governance_framework ========================================
    {
        "id": "cism-gov-001", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 1, "type": "mcq",
        "stem": "Senior leadership asks the information security manager to state, in one sentence, the "
                "PRIMARY objective of information security governance. Which response is best?",
        "options": [
            {"id": "A", "text": "To deploy the strongest available technical controls across the enterprise"},
            {"id": "B", "text": "To let the security team operate independently of the business units"},
            {"id": "C", "text": "To align the information security program with the organization's business objectives and strategy"},
            {"id": "D", "text": "To eliminate all information security risk to the organization"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Governance exists to direct and align information security with business goals so "
                       "that security delivers value and manages risk to an acceptable level; strategic "
                       "alignment is its primary objective.",
            "distractors": {
                "A": "Technology is a means, not the objective; governance is business- and strategy-driven, not technology-first.",
                "B": "Security must be integrated with the business, not isolated from it.",
                "D": "Risk can be managed to an acceptable level but never fully eliminated; 'eliminate all risk' is a classic trap.",
            },
            "exam_pattern": "Governance = align security with business objectives; 'eliminate all risk' and 'technology-first' are wrong-answer signatures.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Information Security Governance (objectives)"],
    },
    {
        "id": "cism-gov-002", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "mcq",
        "stem": "A board member asks how information security 'governance' differs from information "
                "security 'management.' Which distinction is MOST accurate?",
        "options": [
            {"id": "A", "text": "Governance sets strategic direction and oversees outcomes, while management executes and runs day-to-day activities"},
            {"id": "B", "text": "Governance writes the operating procedures, while management approves the overall budget"},
            {"id": "C", "text": "Governance is performed by the security operations team, while management is performed by the auditors"},
            {"id": "D", "text": "They are interchangeable terms for the same function"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance (a board/senior-management responsibility) evaluates, directs, and "
                       "monitors; management plans, builds, and runs the program to carry out that direction.",
            "distractors": {
                "B": "This is reversed and mischaracterised: procedures are an execution (management) artifact, while budget approval is a governance/senior-management act.",
                "C": "Governance is a board/senior-management responsibility, not a security-operations task; auditors provide independent assurance, not management.",
                "D": "They are distinct layers - direction and oversight versus execution - not synonyms.",
            },
            "exam_pattern": "Governance = evaluate/direct/monitor (board, senior mgmt); management = plan/build/run (CISO and team).",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Governance versus management"],
    },
    {
        "id": "cism-gov-003", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "mcq",
        "stem": "The information security manager is organizing the program's documentation. Which "
                "document type specifies mandatory, measurable requirements (such as approved encryption "
                "algorithms) that support a policy?",
        "options": [
            {"id": "A", "text": "Guideline"},
            {"id": "B", "text": "Procedure"},
            {"id": "C", "text": "Policy"},
            {"id": "D", "text": "Standard"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A standard is a mandatory, specific requirement that supports a policy (for example, "
                       "a minimum key length or an approved algorithm list) and makes the policy enforceable.",
            "distractors": {
                "A": "Guidelines are recommended, discretionary practices, not mandatory requirements.",
                "B": "Procedures are step-by-step instructions for performing a task, not the requirement itself.",
                "C": "A policy is a high-level statement of management intent and direction, not the specific mandatory requirement.",
            },
            "exam_pattern": "Hierarchy: Policy (intent) -> Standard (mandatory specifics) -> Procedure (steps) -> Guideline (optional advice).",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Policies, standards, procedures and guidelines"],
    },
    {
        "id": "cism-gov-004", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a framework that governs and manages enterprise IT and links IT "
                "goals to business goals for the board's oversight. Which framework is the BEST fit?",
        "options": [
            {"id": "A", "text": "ISO/IEC 27002"},
            {"id": "B", "text": "NIST SP 800-53"},
            {"id": "C", "text": "COBIT"},
            {"id": "D", "text": "PCI DSS"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "COBIT is a framework for the governance and management of enterprise IT; it maps "
                       "enterprise and IT goals and gives the board a structure for oversight.",
            "distractors": {
                "A": "ISO/IEC 27002 is a catalog of information security controls, not an enterprise IT governance framework.",
                "B": "NIST SP 800-53 is a security and privacy control catalog (primarily for US federal systems), not a governance framework.",
                "D": "PCI DSS is a payment-card data security standard, not an enterprise governance framework.",
            },
            "exam_pattern": "Governance of enterprise IT and business-IT goal alignment for the board = COBIT.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Governance frameworks (COBIT)"],
    },
    {
        "id": "cism-gov-005", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The international standard that specifies the certifiable requirements "
                "for establishing and operating an Information Security Management System (ISMS) is "
                "ISO/IEC _____. (enter the number)",
        "correct": ["27001"],
        "explanation": {
            "correct": "ISO/IEC 27001 defines the requirements for an ISMS and is the standard an "
                       "organization is certified against; ISO/IEC 27002 provides the supporting control guidance.",
            "exam_pattern": "27001 = ISMS requirements (certifiable); 27002 = control best-practice guidance; 27014 = governance of information security.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - ISO/IEC 27001 and the ISMS"],
    },

    # ===== cism_strategy_alignment ==========================================
    {
        "id": "cism-gov-006", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 2, "type": "mcq",
        "stem": "To ensure the information security strategy truly supports the organization, on what "
                "should the information security manager BASE the strategy?",
        "options": [
            {"id": "A", "text": "The latest industry threat-intelligence reports"},
            {"id": "B", "text": "The organization's business strategy and objectives"},
            {"id": "C", "text": "The capabilities of the security tools already owned"},
            {"id": "D", "text": "The preferences of the security operations staff"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The security strategy must be derived from and support the business strategy and "
                       "objectives; alignment with the business is what makes the strategy appropriate.",
            "distractors": {
                "A": "Threat intelligence informs risk decisions but is not the foundation of strategic alignment.",
                "C": "Basing the strategy on existing tools is technology-driven and backwards - needs should drive tools, not the reverse.",
                "D": "Staff preferences do not define business alignment or priorities.",
            },
            "exam_pattern": "Security strategy derives from business strategy/objectives - business-driven, not tool- or threat-driven.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Strategic alignment"],
    },
    {
        "id": "cism-gov-007", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 2, "type": "mcq",
        "stem": "An information security steering committee made up of senior business and IT leaders has "
                "been formed. What is its PRIMARY purpose?",
        "options": [
            {"id": "A", "text": "To perform technical configuration reviews of security controls"},
            {"id": "B", "text": "To investigate and respond to security incidents"},
            {"id": "C", "text": "To ensure security initiatives are aligned with and prioritized against business objectives"},
            {"id": "D", "text": "To deliver security awareness training to all staff"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The steering committee provides cross-functional direction - ensuring security "
                       "initiatives align with business objectives and are prioritized appropriately.",
            "distractors": {
                "A": "Technical configuration reviews are an operational task, not a steering-committee function.",
                "B": "Incident investigation is handled by the incident response team, not the steering committee.",
                "D": "Delivering training is a program activity, not the committee's governing role.",
            },
            "exam_pattern": "Steering committee = cross-functional alignment, prioritization, and direction of security with the business.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Security steering committee"],
    },
    {
        "id": "cism-gov-008", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 3, "type": "mcq",
        "stem": "A newly hired information security manager is asked to develop the organization's first "
                "information security strategy. What should the manager do FIRST?",
        "options": [
            {"id": "A", "text": "Understand the organization's business objectives and current risk posture"},
            {"id": "B", "text": "Purchase and deploy a security information and event management (SIEM) platform"},
            {"id": "C", "text": "Write and publish the acceptable use policy"},
            {"id": "D", "text": "Benchmark the proposed security budget against competitors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A strategy must be grounded in the business objectives (the desired state) and the "
                       "current state of risk; understanding both comes first and everything else follows.",
            "distractors": {
                "B": "Deploying tooling before understanding needs is technology-first and premature.",
                "C": "Policies are written after the strategy's direction is understood, not before.",
                "D": "Budget benchmarking is an input used later in planning, not the first step.",
            },
            "exam_pattern": "Start a strategy by understanding business objectives (desired state) and current state; define direction before tools or policies.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Developing an information security strategy"],
    },
    {
        "id": "cism-gov-009", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 3, "type": "mcq",
        "stem": "The information security manager has documented the organization's desired state of "
                "security and its current state. What does the difference between the two BEST represent?",
        "options": [
            {"id": "A", "text": "The residual risk the board must formally accept"},
            {"id": "B", "text": "The gap that the security strategy's roadmap is designed to close"},
            {"id": "C", "text": "The list of controls that have already failed an audit"},
            {"id": "D", "text": "The organization's risk appetite"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Desired state minus current state is the gap; the strategy produces a roadmap of "
                       "initiatives to close that gap over time.",
            "distractors": {
                "A": "Residual risk is what remains after controls are applied, not the current-versus-desired gap.",
                "C": "The gap is not an audit-failure list; it reflects where the program needs to go.",
                "D": "Risk appetite is how much risk is acceptable, not a measure of the state gap.",
            },
            "exam_pattern": "Desired state - current state = the gap; the strategy/roadmap is what closes it.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Current state, desired state and gap analysis"],
    },
    {
        "id": "cism-gov-010", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 2, "type": "multi",
        "stem": "Which TWO factors are MOST critical to the success of an organization's information "
                "security governance program? (Choose two.)",
        "options": [
            {"id": "A", "text": "Visible commitment and support from senior management"},
            {"id": "B", "text": "Alignment of the security program with business objectives"},
            {"id": "C", "text": "Deploying the newest available security technology"},
            {"id": "D", "text": "Maintaining the largest possible security headcount"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Governance succeeds when senior management visibly supports it and when the program "
                       "is aligned with business objectives; these are the top critical success factors.",
            "distractors": {
                "C": "Technology is an enabler, not a governance critical success factor.",
                "D": "A large headcount does not by itself make governance effective; direction and alignment do.",
            },
            "exam_pattern": "Top governance success factors = senior-management support and business alignment; technology/headcount are distractors.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Critical success factors"],
    },

    # ===== cism_roles_responsibilities ======================================
    {
        "id": "cism-gov-011", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "mcq",
        "stem": "After a breach, regulators ask who is ultimately accountable for the organization's "
                "information security. Who is it?",
        "options": [
            {"id": "A", "text": "The information security manager (CISO)"},
            {"id": "B", "text": "The data custodians in the IT department"},
            {"id": "C", "text": "The board of directors and senior management"},
            {"id": "D", "text": "The third-party managed security service provider"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Day-to-day responsibility is delegated, but ultimate accountability for information "
                       "security rests with the board of directors and senior management and cannot be delegated away.",
            "distractors": {
                "A": "The CISO is responsible for running the program but is not where ultimate accountability stops.",
                "B": "Custodians maintain controls operationally; they are not ultimately accountable.",
                "D": "Outsourcing operations transfers tasks, not the organization's accountability.",
            },
            "exam_pattern": "Responsibility can be delegated; ultimate accountability stays with the board/senior management.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Roles and responsibilities (accountability)"],
    },
    {
        "id": "cism-gov-012", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "mcq",
        "stem": "Who is responsible for determining the classification level of a set of business "
                "information and for deciding who may access it?",
        "options": [
            {"id": "A", "text": "The data (information) owner"},
            {"id": "B", "text": "The data custodian"},
            {"id": "C", "text": "The information security manager"},
            {"id": "D", "text": "The end users of the data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The data/information owner - typically a business leader - classifies the data and "
                       "authorizes access, because the owner understands its value to the business.",
            "distractors": {
                "B": "The custodian implements and maintains protection per the owner's direction but does not set classification.",
                "C": "The security manager facilitates and advises on the scheme but does not own the business data.",
                "D": "Users consume data under the access rules; they do not set its classification.",
            },
            "exam_pattern": "Data/information owner classifies and authorizes access; the custodian protects it as directed.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Data owner responsibilities"],
    },
    {
        "id": "cism-gov-013", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "mcq",
        "stem": "An IT storage administrator implements and maintains the encryption, backups, and access "
                "controls that a business unit's data owner has specified. Which role is the administrator "
                "fulfilling?",
        "options": [
            {"id": "A", "text": "Data owner"},
            {"id": "B", "text": "Data custodian"},
            {"id": "C", "text": "Risk owner"},
            {"id": "D", "text": "Security steering committee member"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A data custodian implements and maintains the protective controls as directed by "
                       "the owner; this is typically an IT operations role.",
            "distractors": {
                "A": "The owner sets classification and requirements; the administrator is carrying them out, not setting them.",
                "C": "A risk owner is accountable for a specific risk's treatment, not for maintaining controls.",
                "D": "Steering committee members provide governance direction, not hands-on control maintenance.",
            },
            "exam_pattern": "Custodian = implements/maintains controls per the owner's direction (usually IT).",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Data custodian responsibilities"],
    },
    {
        "id": "cism-gov-014", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "mcq",
        "stem": "Within a well-governed organization, what is the PRIMARY responsibility of the "
                "information security manager (CISO)?",
        "options": [
            {"id": "A", "text": "Approving the organization's risk appetite"},
            {"id": "B", "text": "Personally performing all forensic investigations"},
            {"id": "C", "text": "Owning and classifying all business data"},
            {"id": "D", "text": "Developing and managing the information security program and reporting on it to senior management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The information security manager builds, runs, and reports on the program, "
                       "translating governance direction into an effective security capability.",
            "distractors": {
                "A": "Risk appetite is set by the board/senior management, not the CISO.",
                "B": "The manager coordinates and facilitates; hands-on forensics is performed by specialists.",
                "C": "Data ownership and classification rest with the business data owners.",
            },
            "exam_pattern": "The manager builds/runs/reports on the program and facilitates - rather than owning business decisions or doing hands-on work.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Information security manager role"],
    },
    {
        "id": "cism-gov-015", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 1, "type": "mcq",
        "stem": "An information security policy has been drafted. Whose approval gives it the authority to "
                "be enforced across the organization?",
        "options": [
            {"id": "A", "text": "The security operations team"},
            {"id": "B", "text": "The external auditors"},
            {"id": "C", "text": "The help desk"},
            {"id": "D", "text": "Senior management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An information security policy derives its authority from senior management (and "
                       "board) approval, which signals the organization's commitment and makes it enforceable.",
            "distractors": {
                "A": "The operations team implements policy but cannot grant it organizational authority.",
                "B": "Auditors assess compliance with policy; they do not approve or own it.",
                "C": "The help desk has no policy-approval authority.",
            },
            "exam_pattern": "Policy authority comes from senior-management (and board) approval - a sign of tone at the top.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Policy approval and management commitment"],
    },

    # ===== cism_legal_regulatory ============================================
    {
        "id": "cism-gov-016", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 2, "type": "mcq",
        "stem": "A new data-protection regulation will soon apply to the organization. What should the "
                "information security manager do FIRST?",
        "options": [
            {"id": "A", "text": "Immediately purchase a compliance-management tool"},
            {"id": "B", "text": "Perform a gap analysis comparing current controls against the new requirements"},
            {"id": "C", "text": "Notify all customers that the organization is non-compliant"},
            {"id": "D", "text": "Halt all processing of personal data until further notice"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The manager should first understand the impact by performing a gap analysis of "
                       "current controls against the new requirements, then plan risk-based remediation.",
            "distractors": {
                "A": "Buying a tool before understanding the gap is premature and technology-first.",
                "C": "Declaring non-compliance to customers before assessing the situation is unwarranted and harmful.",
                "D": "Halting all processing is a disproportionate overreaction, not a risk-based first step.",
            },
            "exam_pattern": "New law/regulation -> first assess impact via gap/impact analysis, then plan remediation.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Legal and regulatory requirements"],
    },
    {
        "id": "cism-gov-017", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 2, "type": "mcq",
        "stem": "From a management perspective, what is the BEST reason for the organization to comply "
                "with applicable laws and regulations?",
        "options": [
            {"id": "A", "text": "To achieve the strongest possible technical security"},
            {"id": "B", "text": "To avoid having to perform risk assessments"},
            {"id": "C", "text": "To demonstrate due diligence and reduce legal and financial liability"},
            {"id": "D", "text": "To guarantee that a breach can never occur"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Compliance is a business and legal driver: it demonstrates due diligence/due care "
                       "and reduces the organization's legal and financial liability.",
            "distractors": {
                "A": "Compliance is a legal/risk obligation, not a measure of technical strength.",
                "B": "Compliance does not remove the need for risk assessment; the two are complementary.",
                "D": "Compliance reduces but never guarantees against breaches.",
            },
            "exam_pattern": "Compliance = demonstrating due diligence/due care and limiting liability - a business/legal driver.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Due diligence and legal drivers"],
    },
    {
        "id": "cism-gov-018", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 3, "type": "mcq",
        "stem": "The organization must satisfy several overlapping regulations and standards that share "
                "many similar control requirements. What is the MOST efficient approach for the "
                "information security manager?",
        "options": [
            {"id": "A", "text": "Map the requirements to a single common (unified) control framework"},
            {"id": "B", "text": "Maintain a separate, independent control set for each regulation"},
            {"id": "C", "text": "Comply only with the strictest regulation and ignore the others"},
            {"id": "D", "text": "Delegate each regulation to a different business unit without coordination"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mapping overlapping obligations to one common control framework (control "
                       "rationalization) lets a single control satisfy many requirements, reducing duplication.",
            "distractors": {
                "B": "Duplicate, siloed control sets are inefficient and hard to maintain.",
                "C": "Ignoring the other regulations creates compliance gaps and legal exposure.",
                "D": "Uncoordinated delegation leads to inconsistency and gaps.",
            },
            "exam_pattern": "Harmonise overlapping obligations by mapping to one common control framework.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Managing multiple compliance requirements"],
    },
    {
        "id": "cism-gov-019", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 3, "type": "mcq",
        "stem": "The organization outsources processing of regulated customer data to a cloud provider. "
                "Who remains accountable to regulators for protecting that data?",
        "options": [
            {"id": "A", "text": "The cloud provider alone"},
            {"id": "B", "text": "The organization that collected the data"},
            {"id": "C", "text": "The regulator"},
            {"id": "D", "text": "No one, once a contract is signed"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The organization that collected the data (the data controller) remains accountable "
                       "to regulators even when processing is outsourced; accountability cannot be contracted away.",
            "distractors": {
                "A": "The provider has contractual obligations, but legal accountability to regulators stays with the controller.",
                "C": "The regulator enforces the law; it is not accountable for protecting the data.",
                "D": "A contract allocates duties but does not erase the organization's accountability.",
            },
            "exam_pattern": "You can outsource the processing, but not the accountability - the data controller stays responsible.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Outsourcing and accountability"],
    },
    {
        "id": "cism-gov-020", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Before engaging a vendor to handle regulated data, an organization "
                "investigates the vendor's security practices and compliance posture. This investigative "
                "process is known as due _____. (one word)",
        "correct": ["diligence"],
        "explanation": {
            "correct": "Due diligence is the investigation and evaluation performed before a decision or "
                       "engagement; due care is then the ongoing prudent action taken to protect assets.",
            "exam_pattern": "Due diligence = investigate/evaluate beforehand; due care = act prudently afterward.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Due diligence and due care"],
    },
]
