"""ISACA CISM pool - Round 2 (deepening expansion across all four domains).

Original, objective-aligned practice items that EXTEND the round-1 CISM bank
(content_cism_governance/risk/program/incident.py) without duplicating it. Round
1 established the core of each subtopic; round 2 adds new management scenarios and
second-order concepts:

  * Domain 1 (Governance): COBIT 2019 EDM vs management domains, ISO/IEC 27014,
    baselines/guidelines, policy maintenance, governance outcomes (value
    delivery), the business case, security vs enterprise architecture, CISO
    reporting line/independence, RACI accountability, internal audit assurance,
    multi-jurisdiction requirements, due care, privacy data mapping, breach-law
    readiness and the prudent-person rule.
  * Domain 2 (Risk): quantitative analysis (SLE/EF/ARO/ALE), qualitative vs
    quantitative, assessment timing, threat agents, likelihood factors, the four
    responses (mitigation keyed), risk appetite vs tolerance, escalating
    over-appetite risk, limits of transfer, treatment plans, KRI thresholds and
    quality, risk aggregation, register triggers, risk reporting, data handling,
    CIA-driven classification, aggregation sensitivity and scheme design.
  * Domain 3 (Program): resource optimization, security as enabler, security in
    the SDLC/change management, program-vs-strategy, control types not yet
    covered (corrective/deterrent/least privilege/SoD/defense-in-depth/technical),
    NIST CSF 2.0 Govern, NIST SP 800-53/PCI DSS/ISO 27005, awareness vs training,
    role-based/onboarding delivery, culture, phishing simulations, KGI, metric
    quality, value in financial terms, operational metrics, balanced scorecard,
    SOC 2 assurance, cloud shared responsibility, fourth-party risk, offboarding,
    vendor tiering and incident-notification clauses.
  * Domain 4 (Incident): event vs incident, playbooks, defined authority, IR
    retainers, detection capability, standing up a capability, the IR lifecycle
    order, multi-incident triage, validate-before-declare, breach/law-enforcement/
    media decisions, the ransom decision, WRT/MTD, hot/cold sites, parallel
    testing, BCP vs DRP, offsite backups, short-term containment, containment as a
    business decision, order of volatility, forensic imaging, root-cause before
    eradication, return-to-production criteria, IR metrics (MTTD/MTTR), review
    timing/participants, systemic improvement, functional exercises and plan
    maintenance.

Authoring rules match the other content_*.py pools: the build step shuffles
option order (seeded by id), so a key authored here as "A"/"B"/"C"/"D" is not
positionally biased, every wrong option carries a distractor note, and each item
names the public ISACA objective area it draws on so facts stay traceable. Ids
use the round-1 prefixes (gov/risk/prog/inc) with an "-r2-" segment so they are
unique against round 1.

CISM is a MANAGEMENT exam: keyed answers reflect the information security
manager's view - align security with the business, decide on a risk basis,
facilitate rather than perform hands-on technical work, obtain senior-management
support, and keep accountability in-house. The keyed answer is the BEST "FIRST /
MOST important" management action. These are original items built from public
CISM objectives; they are never real or memorised exam questions.
"""

QUESTIONS = [
    # ====================================================================
    # DOMAIN 1 - INFORMATION SECURITY GOVERNANCE (20)
    # ====================================================================

    # ----- cism_governance_framework -----------------------------------
    {
        "id": "cism-gov-r2-001", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 3, "type": "mcq",
        "stem": "In COBIT 2019, the objectives are grouped into one governance domain and four "
                "management domains. Which domain represents GOVERNANCE (the board's evaluate, direct "
                "and monitor responsibilities)?",
        "options": [
            {"id": "A", "text": "APO (Align, Plan and Organize)"},
            {"id": "B", "text": "EDM (Evaluate, Direct and Monitor)"},
            {"id": "C", "text": "DSS (Deliver, Service and Support)"},
            {"id": "D", "text": "MEA (Monitor, Evaluate and Assess)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "EDM (Evaluate, Direct and Monitor) is COBIT 2019's governance domain - the board "
                       "evaluates options, sets direction, and monitors outcomes; the other four domains are "
                       "management.",
            "distractors": {
                "A": "APO is a management domain (strategy and supporting activities), not governance.",
                "C": "DSS is a management domain covering operational delivery and support.",
                "D": "MEA is a management domain for performance monitoring and conformance assessment.",
            },
            "exam_pattern": "COBIT 2019: EDM = governance (board); APO/BAI/DSS/MEA = management.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - COBIT 2019 governance and management objectives"],
    },
    {
        "id": "cism-gov-r2-002", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "mcq",
        "stem": "Which security documentation artifact defines the MINIMUM mandatory configuration that "
                "every system of a given type must meet (for example, a hardened server build)?",
        "options": [
            {"id": "A", "text": "Guideline"},
            {"id": "B", "text": "Policy"},
            {"id": "C", "text": "Baseline"},
            {"id": "D", "text": "Mission statement"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A baseline specifies the minimum mandatory level/configuration of security that a "
                       "class of systems must meet, making 'adequate protection' concrete and enforceable.",
            "distractors": {
                "A": "A guideline is a recommended, discretionary practice - not a mandatory minimum.",
                "B": "A policy is a high-level statement of intent, not a specific configuration minimum.",
                "D": "A mission statement expresses organizational purpose, not a security configuration.",
            },
            "exam_pattern": "Baseline = mandatory minimum configuration for a class of systems; policy = intent; guideline = optional advice.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Security baselines in the documentation hierarchy"],
    },
    {
        "id": "cism-gov-r2-003", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 3, "type": "mcq",
        "stem": "A board wants guidance specifically on the GOVERNANCE of information security - how to "
                "direct and oversee the ISMS. Which ISO/IEC standard is the BEST fit?",
        "options": [
            {"id": "A", "text": "ISO/IEC 27014"},
            {"id": "B", "text": "ISO/IEC 27002"},
            {"id": "C", "text": "ISO/IEC 27005"},
            {"id": "D", "text": "ISO/IEC 27701"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ISO/IEC 27014 provides guidance on the governance of information security, helping "
                       "the governing body direct and monitor security activities.",
            "distractors": {
                "B": "ISO/IEC 27002 is a catalog of security control best practices, not governance guidance.",
                "C": "ISO/IEC 27005 covers information security risk management, not governance.",
                "D": "ISO/IEC 27701 extends the ISMS for privacy information management, not governance.",
            },
            "exam_pattern": "27014 = governance of information security; 27002 = controls; 27005 = risk; 27701 = privacy.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - ISO/IEC 27014 governance of information security"],
    },
    {
        "id": "cism-gov-r2-004", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "mcq",
        "stem": "What BEST ensures that the organization's information security policies remain effective "
                "and relevant over time?",
        "options": [
            {"id": "A", "text": "Publishing them once and leaving them unchanged for stability"},
            {"id": "B", "text": "Reviewing and updating them periodically and whenever a significant change occurs"},
            {"id": "C", "text": "Letting each employee interpret them however they prefer"},
            {"id": "D", "text": "Replacing all policies with technical controls"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Policies must be living documents: scheduled periodic review plus review on "
                       "significant change (new regulation, technology, or risk) keeps them aligned and enforceable.",
            "distractors": {
                "A": "Static policies become outdated as the business, threats, and regulations change.",
                "C": "Individual interpretation defeats the purpose of a consistent, authoritative policy.",
                "D": "Technical controls implement policy; they do not replace the management direction policy provides.",
            },
            "exam_pattern": "Keep policies current via periodic review and review on significant change.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Policy lifecycle and maintenance"],
    },
    {
        "id": "cism-gov-r2-005", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_governance_framework", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In the security documentation hierarchy, recommended but NON-mandatory "
                "best-practice statements that help people apply standards are called _____. (one word)",
        "correct": ["guidelines", "guideline"],
        "explanation": {
            "correct": "Guidelines are discretionary, recommended practices; unlike standards and baselines, "
                       "they are not mandatory, but they help staff apply policy and standards in practice.",
            "exam_pattern": "Policy (intent) -> Standard/Baseline (mandatory) -> Procedure (steps) -> Guideline (optional advice).",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Guidelines in the documentation hierarchy"],
    },

    # ----- cism_strategy_alignment -------------------------------------
    {
        "id": "cism-gov-r2-006", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 3, "type": "mcq",
        "stem": "Which of the following is a recognized desired OUTCOME of effective information security "
                "governance?",
        "options": [
            {"id": "A", "text": "Eliminating all information security risk"},
            {"id": "B", "text": "Maximizing annual security spending"},
            {"id": "C", "text": "Value delivery - optimizing security investments to support business objectives"},
            {"id": "D", "text": "Achieving zero security incidents permanently"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Value delivery (optimizing security investment so it supports business objectives and "
                       "manages risk cost-effectively) is one of governance's desired outcomes, alongside "
                       "strategic alignment, risk management, resource optimization, performance measurement "
                       "and assurance integration.",
            "distractors": {
                "A": "Risk is managed to an acceptable level, never fully eliminated.",
                "B": "Maximizing spend is not an outcome; cost-effective value delivery is.",
                "D": "Zero incidents is unrealistic and is not a governance outcome.",
            },
            "exam_pattern": "Governance outcomes include strategic alignment, risk management, value delivery, resource optimization, performance measurement and assurance integration.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Desired outcomes of information security governance"],
    },
    {
        "id": "cism-gov-r2-007", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 3, "type": "mcq",
        "stem": "The information security manager needs funding and senior-management commitment for a "
                "strategic security initiative. What is the BEST tool to obtain it?",
        "options": [
            {"id": "A", "text": "A business case expressing the initiative's risk reduction and value in business terms"},
            {"id": "B", "text": "A detailed technical specification of the proposed appliances"},
            {"id": "C", "text": "A list of the security team's preferred vendors"},
            {"id": "D", "text": "A warning that the auditors will be upset otherwise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Senior management responds to business justification: a business case that frames the "
                       "initiative in terms of risk reduction, cost-benefit, and support for objectives is the "
                       "manager's best instrument for buy-in and funding.",
            "distractors": {
                "B": "Technical specifications do not justify value to executives.",
                "C": "Vendor preference is not a business justification.",
                "D": "Fear of audit is a weak, negative argument compared with a value-based business case.",
            },
            "exam_pattern": "Win senior-management support with a business case stated in business terms (risk, value, cost-benefit).",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Obtaining management commitment / business case"],
    },
    {
        "id": "cism-gov-r2-008", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 2, "type": "mcq",
        "stem": "After defining the current and desired states of security, the information security "
                "manager builds a roadmap. What does the roadmap PRIMARILY provide?",
        "options": [
            {"id": "A", "text": "A guarantee that no incidents will occur"},
            {"id": "B", "text": "A sequenced, prioritized set of initiatives to move from the current state to the desired state within the organization's constraints"},
            {"id": "C", "text": "A catalog of every security product on the market"},
            {"id": "D", "text": "The organization's risk appetite statement"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The roadmap translates the strategy into a prioritized, time-sequenced plan of "
                       "initiatives that closes the gap between current and desired state, respecting budget, "
                       "resource and other constraints.",
            "distractors": {
                "A": "No plan guarantees zero incidents.",
                "C": "A roadmap is organization-specific initiatives, not a product catalog.",
                "D": "Risk appetite is set by management; it is an input to, not the output of, the roadmap.",
            },
            "exam_pattern": "Roadmap = prioritized, sequenced initiatives to close the current-to-desired gap within constraints.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Strategy roadmap development"],
    },
    {
        "id": "cism-gov-r2-009", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 3, "type": "mcq",
        "stem": "Which of the following BEST helps ensure the information security strategy is implemented "
                "consistently and integrates with the organization's overall technology direction?",
        "options": [
            {"id": "A", "text": "Allowing each team to independently choose its own controls"},
            {"id": "B", "text": "A security architecture aligned with the enterprise architecture"},
            {"id": "C", "text": "Buying point security products as individual needs arise"},
            {"id": "D", "text": "Deferring all security decisions until after systems are built"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A security architecture that is derived from and aligned with the enterprise "
                       "architecture gives a coherent structure so controls are consistent, integrated, and "
                       "support the technology direction rather than being ad hoc.",
            "distractors": {
                "A": "Independent choices produce inconsistent, siloed controls.",
                "C": "Point purchases without an architecture create gaps and overlaps.",
                "D": "Bolting security on after build is costly and weakens integration.",
            },
            "exam_pattern": "Security architecture (aligned to enterprise architecture) drives consistent, integrated implementation of the strategy.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Security architecture and enterprise alignment"],
    },
    {
        "id": "cism-gov-r2-010", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_strategy_alignment", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Senior management's visible commitment and involvement, which sets the "
                "organization's attitude toward security, is commonly called 'tone at the _____.' (one word)",
        "correct": ["top"],
        "explanation": {
            "correct": "'Tone at the top' describes how visible leadership support and behavior set the "
                       "organizational culture and attitude toward security; it is a key governance success factor.",
            "exam_pattern": "Tone at the top = visible senior-management commitment that shapes security culture.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Tone at the top and management commitment"],
    },

    # ----- cism_roles_responsibilities ---------------------------------
    {
        "id": "cism-gov-r2-011", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 3, "type": "mcq",
        "stem": "To preserve independence and avoid a conflict of interest, to whom is it generally BEST "
                "for the information security manager (CISO) to report?",
        "options": [
            {"id": "A", "text": "The IT operations manager"},
            {"id": "B", "text": "The network administrator"},
            {"id": "C", "text": "Senior management or the board (e.g., via a risk or executive committee)"},
            {"id": "D", "text": "The internal audit function"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reporting to senior management or the board keeps security independent of the IT "
                       "functions it must oversee and gives it the authority and visibility it needs.",
            "distractors": {
                "A": "Reporting into IT operations subordinates security to operational goals and creates a conflict of interest.",
                "B": "A network administrator is far too low and also an operational conflict.",
                "D": "Internal audit must remain independent to audit security objectively; the CISO should not report into it.",
            },
            "exam_pattern": "The CISO should report high enough (senior management/board) to stay independent of the operations it governs.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - CISO reporting line and independence"],
    },
    {
        "id": "cism-gov-r2-012", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 3, "type": "mcq",
        "stem": "In a RACI chart for the security program, why should each activity have exactly ONE party "
                "designated as 'Accountable'?",
        "options": [
            {"id": "A", "text": "Because accountability must be unambiguous - one party answers for the outcome and it cannot be effectively shared"},
            {"id": "B", "text": "Because only one person is ever allowed to work on the task"},
            {"id": "C", "text": "Because the 'Responsible' role is unnecessary"},
            {"id": "D", "text": "Because accountability can always be fully delegated to a vendor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Accountability must rest with a single, clearly identified party so there is no "
                       "confusion over who answers for the result; multiple parties may be Responsible (do the "
                       "work), but accountability is singular.",
            "distractors": {
                "B": "Many people can be Responsible and perform the work; 'Accountable' is about answerability, not sole labor.",
                "C": "The Responsible role (those doing the work) is still required.",
                "D": "Operational work can be outsourced, but accountability cannot be delegated away.",
            },
            "exam_pattern": "RACI: one Accountable per activity (answerability is singular); Responsible can be many; accountability isn't outsourced.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - RACI and accountability"],
    },
    {
        "id": "cism-gov-r2-013", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 3, "type": "multi",
        "stem": "Which TWO of the following are GOVERNANCE responsibilities of the board and senior "
                "management rather than the information security manager? (Choose two.)",
        "options": [
            {"id": "A", "text": "Approving the organization's risk appetite"},
            {"id": "B", "text": "Providing visible support and adequate resources for the security program"},
            {"id": "C", "text": "Configuring and maintaining firewall rule sets"},
            {"id": "D", "text": "Performing hands-on forensic analysis during an incident"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Setting/approving risk appetite and providing visible support and resources are "
                       "board/senior-management governance duties; the manager and specialists execute within "
                       "that direction.",
            "distractors": {
                "C": "Firewall configuration is an operational task performed by technical staff, not a governance duty.",
                "D": "Hands-on forensics is performed by specialists, not the board or senior management.",
            },
            "exam_pattern": "Board/senior mgmt: set risk appetite, give support/resources, oversee; they do not perform operational/technical tasks.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Governance vs operational responsibilities"],
    },
    {
        "id": "cism-gov-r2-014", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "mcq",
        "stem": "Who is PRIMARILY responsible for ensuring that employees within a business unit follow "
                "information security policies in their day-to-day work?",
        "options": [
            {"id": "A", "text": "That business unit's line management (its managers)"},
            {"id": "B", "text": "The external auditors"},
            {"id": "C", "text": "The information security manager personally"},
            {"id": "D", "text": "The data custodians in IT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Line managers are responsible for enforcing policy and secure behavior within their "
                       "own units; security is embedded in the business, not policed solely by the security team.",
            "distractors": {
                "B": "Auditors independently assess compliance; they do not enforce it operationally.",
                "C": "The security manager sets direction and facilitates but cannot personally enforce behavior in every unit.",
                "D": "Custodians maintain technical controls; they do not supervise staff behavior.",
            },
            "exam_pattern": "Line/business management enforces policy within its own area; security facilitates, audit assures.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Line management responsibility for compliance"],
    },
    {
        "id": "cism-gov-r2-015", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_roles_responsibilities", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: An independent function that provides the board with assurance on "
                "whether security controls are operating effectively, without owning or running them, is "
                "internal _____. (one word)",
        "correct": ["audit"],
        "explanation": {
            "correct": "Internal audit provides independent assurance over control effectiveness; keeping it "
                       "independent of the functions it audits is essential to objective oversight.",
            "exam_pattern": "Internal audit = independent assurance; it must not own or run the controls it evaluates.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Internal audit and independent assurance"],
    },

    # ----- cism_legal_regulatory ---------------------------------------
    {
        "id": "cism-gov-r2-016", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 3, "type": "mcq",
        "stem": "An organization is expanding into several countries, each with its own data-protection "
                "laws. What should the information security manager do FIRST?",
        "options": [
            {"id": "A", "text": "Identify all applicable legal and regulatory requirements across the jurisdictions involved"},
            {"id": "B", "text": "Immediately adopt the controls used by the largest competitor"},
            {"id": "C", "text": "Apply only the home country's laws everywhere"},
            {"id": "D", "text": "Halt the expansion to avoid any compliance work"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The manager must first determine which laws and regulations apply in each "
                       "jurisdiction; you cannot design compliant controls before you know the obligations.",
            "distractors": {
                "B": "Copying a competitor ignores the organization's own obligations and context.",
                "C": "Other jurisdictions' laws still apply to activities there.",
                "D": "Halting expansion is a disproportionate overreaction, not a risk-based first step.",
            },
            "exam_pattern": "Multi-jurisdiction: FIRST identify all applicable requirements, then harmonize and design controls.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Identifying applicable legal/regulatory requirements"],
    },
    {
        "id": "cism-gov-r2-017", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 2, "type": "mcq",
        "stem": "Having investigated its risks (due diligence), an organization then takes reasonable, "
                "ongoing measures a prudent organization would take to protect its assets. This ongoing "
                "action is BEST described as:",
        "options": [
            {"id": "A", "text": "Due care"},
            {"id": "B", "text": "Due diligence"},
            {"id": "C", "text": "Risk acceptance"},
            {"id": "D", "text": "Risk avoidance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Due care is the ongoing, prudent action taken to protect assets - the 'doing' that "
                       "follows the investigation (due diligence).",
            "distractors": {
                "B": "Due diligence is the prior investigation/evaluation, not the ongoing protective action.",
                "C": "Risk acceptance is a specific treatment decision, not the general duty of prudent care.",
                "D": "Risk avoidance eliminates an activity; it is not the general duty of care.",
            },
            "exam_pattern": "Due diligence = investigate beforehand; due care = act prudently and continuously afterward.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Due care versus due diligence"],
    },
    {
        "id": "cism-gov-r2-018", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 3, "type": "mcq",
        "stem": "A new privacy law gives individuals the right to request erasure of their personal data. "
                "What should the information security manager do FIRST to prepare the organization to comply?",
        "options": [
            {"id": "A", "text": "Identify and map where personal data is collected, stored, and processed"},
            {"id": "B", "text": "Delete the entire customer database immediately"},
            {"id": "C", "text": "Purchase encryption software for all servers"},
            {"id": "D", "text": "Announce publicly that the organization cannot comply"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "You cannot honor an erasure (or any data-subject) request without first knowing where "
                       "the personal data resides; data discovery/mapping is the necessary first step.",
            "distractors": {
                "B": "Deleting all data destroys information the business legitimately needs - an overreaction.",
                "C": "Buying encryption is technology-first and does not address knowing where data lives or enabling erasure.",
                "D": "Declaring non-compliance before assessing the situation is premature and harmful.",
            },
            "exam_pattern": "New privacy obligation -> FIRST inventory/map personal data, then build the process to meet the requirement.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Privacy requirements and data mapping"],
    },
    {
        "id": "cism-gov-r2-019", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 2, "type": "mcq",
        "stem": "A jurisdiction requires organizations to notify regulators of qualifying data breaches "
                "within a set time. What should the information security manager ensure is in place to meet "
                "this obligation?",
        "options": [
            {"id": "A", "text": "A defined breach-notification process aligned with the legal timelines and integrated into the incident response plan"},
            {"id": "B", "text": "A policy never to report breaches to anyone"},
            {"id": "C", "text": "A plan to notify only if the media discovers the breach"},
            {"id": "D", "text": "Full reliance on the cloud provider to handle all legal obligations"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Meeting a legal notification deadline requires a pre-defined process (who decides, who "
                       "is notified, within what timeframe) built into the incident response plan so the "
                       "organization can act within the mandated window.",
            "distractors": {
                "B": "Never reporting violates the law.",
                "C": "Waiting for media exposure is evasive and still breaches the legal deadline.",
                "D": "Legal accountability cannot be outsourced to a provider.",
            },
            "exam_pattern": "Know the obligation in advance and bake breach-notification timelines into the IR plan.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Breach-notification obligations"],
    },
    {
        "id": "cism-gov-r2-020", "exam": "cism", "domain": "cism_governance",
        "subtopic": "cism_legal_regulatory", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: The legal principle that senior managers can be held liable if they "
                "fail to exercise the care a reasonable individual would exercise in protecting the "
                "organization is known as the 'prudent _____ rule.' (one word)",
        "correct": ["person", "man"],
        "explanation": {
            "correct": "Under the prudent-person rule, officers must act with the diligence and care a "
                       "reasonable (prudent) person would in the same situation; failing to do so can create "
                       "personal liability - a key driver of due care.",
            "exam_pattern": "Prudent-person rule = act as a reasonable person would; underpins due care and management liability.",
        },
        "references": ["ISACA CISM Review Manual: Domain 1 - Prudent-person rule and liability"],
    },

    # ====================================================================
    # DOMAIN 2 - INFORMATION SECURITY RISK MANAGEMENT (24)
    # ====================================================================

    # ----- cism_risk_assessment ----------------------------------------
    {
        "id": "cism-risk-r2-001", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 3, "type": "mcq",
        "stem": "A data-center asset is valued at $200,000. A flood would destroy an estimated 25% of its "
                "value, and floods are expected about once every 10 years. What is the annualized loss "
                "expectancy (ALE)?",
        "options": [
            {"id": "A", "text": "$5,000"},
            {"id": "B", "text": "$50,000"},
            {"id": "C", "text": "$20,000"},
            {"id": "D", "text": "$500"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SLE = asset value x exposure factor = $200,000 x 0.25 = $50,000. ALE = SLE x ARO = "
                       "$50,000 x 0.1 (once per 10 years) = $5,000.",
            "distractors": {
                "B": "$50,000 is the single loss expectancy (SLE); it omits the annualized rate of occurrence.",
                "C": "$20,000 multiplies asset value by ARO but wrongly omits the exposure factor.",
                "D": "$500 reflects a misplaced decimal in the ARO.",
            },
            "exam_pattern": "SLE = AV x EF; ALE = SLE x ARO. Watch for answers that drop the EF or the ARO.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Quantitative risk analysis (SLE, ARO, ALE)"],
    },
    {
        "id": "cism-risk-r2-002", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "A risk analysis rates each risk's likelihood and impact as 'High,' 'Medium,' or 'Low' "
                "instead of calculating monetary values. This approach is BEST described as:",
        "options": [
            {"id": "A", "text": "Qualitative risk analysis"},
            {"id": "B", "text": "Quantitative risk analysis"},
            {"id": "C", "text": "A business impact analysis"},
            {"id": "D", "text": "A penetration test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Qualitative analysis uses descriptive/relative ratings (High/Medium/Low) rather than "
                       "numeric monetary values; it is faster but less precise than quantitative analysis.",
            "distractors": {
                "B": "Quantitative analysis assigns numeric/monetary values (e.g., SLE, ALE).",
                "C": "A BIA assesses the impact of disruptions on business processes for continuity planning.",
                "D": "A penetration test is a hands-on technical assessment, not a risk-rating method.",
            },
            "exam_pattern": "Qualitative = High/Medium/Low ratings; quantitative = numeric/monetary (SLE, ALE).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Qualitative versus quantitative analysis"],
    },
    {
        "id": "cism-risk-r2-003", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "When is it BEST to perform a risk assessment for a major new system?",
        "options": [
            {"id": "A", "text": "Before deployment (during design/selection) and again after significant changes"},
            {"id": "B", "text": "Only after a breach has occurred"},
            {"id": "C", "text": "Only at the very end of the system's life"},
            {"id": "D", "text": "Never, provided the vendor is reputable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Assessing risk before deployment lets the organization design in appropriate controls, "
                       "and reassessing after significant change keeps the picture current - risk management is "
                       "proactive and continuous.",
            "distractors": {
                "B": "Waiting for a breach is reactive and too late to prevent avoidable harm.",
                "C": "Assessing only at end-of-life provides no protection during operation.",
                "D": "Vendor reputation is not a substitute for assessing the organization's own risk.",
            },
            "exam_pattern": "Assess risk before deployment and after significant change - proactive, not reactive.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Timing of risk assessments"],
    },
    {
        "id": "cism-risk-r2-004", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "A disgruntled administrator who could abuse privileged access is BEST described, in risk "
                "terminology, as a:",
        "options": [
            {"id": "A", "text": "Threat (threat source/agent)"},
            {"id": "B", "text": "Vulnerability"},
            {"id": "C", "text": "Control"},
            {"id": "D", "text": "Residual risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A threat (source/agent) is the potential cause of an unwanted event; a disgruntled "
                       "insider with the means and motive to misuse access is a threat agent.",
            "distractors": {
                "B": "A vulnerability is a weakness that a threat exploits (e.g., excessive privileges), not the actor.",
                "C": "A control reduces risk; it is not the threat.",
                "D": "Residual risk is the exposure remaining after controls, not the actor.",
            },
            "exam_pattern": "Threat (agent) = potential cause; vulnerability = weakness it exploits; risk = likelihood/impact of exploitation.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Threat sources and agents"],
    },
    {
        "id": "cism-risk-r2-005", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 3, "type": "mcq",
        "stem": "When estimating the LIKELIHOOD that a vulnerability will be exploited, which factor is "
                "MOST relevant?",
        "options": [
            {"id": "A", "text": "The capability and motivation of threat actors combined with how easily the vulnerability can be exploited"},
            {"id": "B", "text": "The book value of the affected asset"},
            {"id": "C", "text": "The total size of the security budget"},
            {"id": "D", "text": "The number of employees in the organization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Likelihood depends on the threat (capability and motivation) and the ease of "
                       "exploiting the weakness (including whether an exploit exists and the exposure).",
            "distractors": {
                "B": "Asset value affects the impact side of risk, not the likelihood of exploitation.",
                "C": "Budget size influences control capacity, not the inherent likelihood of an exploit.",
                "D": "Headcount does not determine how likely a given vulnerability is to be exploited.",
            },
            "exam_pattern": "Likelihood = threat capability/motivation x ease of exploitation; asset value drives impact, not likelihood.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Estimating likelihood"],
    },
    {
        "id": "cism-risk-r2-006", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: Single loss expectancy (SLE) equals the asset value multiplied by the "
                "_____ factor, which represents the proportion of the asset lost in a single event. (one word)",
        "correct": ["exposure"],
        "explanation": {
            "correct": "SLE = asset value x exposure factor (EF). The EF is the percentage of asset value "
                       "lost in a single occurrence of the threat.",
            "exam_pattern": "SLE = AV x EF; ALE = SLE x ARO. EF is the fraction of value lost per event.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Exposure factor and SLE"],
    },

    # ----- cism_risk_response ------------------------------------------
    {
        "id": "cism-risk-r2-007", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the likelihood and impact of account compromise, the organization implements "
                "multi-factor authentication and network segmentation. Which risk response does this "
                "represent?",
        "options": [
            {"id": "A", "text": "Mitigation (risk reduction)"},
            {"id": "B", "text": "Transfer (sharing)"},
            {"id": "C", "text": "Avoidance"},
            {"id": "D", "text": "Acceptance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Applying controls to lower a risk's likelihood or impact is mitigation (risk "
                       "reduction) - the most common response.",
            "distractors": {
                "B": "Transfer shifts the loss to a third party (e.g., insurance), not reduce it with controls.",
                "C": "Avoidance eliminates the activity that creates the risk.",
                "D": "Acceptance takes no action and retains the risk.",
            },
            "exam_pattern": "Controls that lower likelihood/impact = mitigation; the four responses are mitigate, transfer, avoid, accept.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk mitigation"],
    },
    {
        "id": "cism-risk-r2-008", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 3, "type": "mcq",
        "stem": "Which statement BEST describes the difference between risk appetite and risk tolerance?",
        "options": [
            {"id": "A", "text": "Risk appetite is the broad amount of risk the organization is willing to take to meet its objectives; risk tolerance is the acceptable deviation around that level, usually expressed as specific, measurable thresholds"},
            {"id": "B", "text": "They are identical terms with no practical difference"},
            {"id": "C", "text": "Risk appetite is always zero, while tolerance is unlimited"},
            {"id": "D", "text": "Risk tolerance is set only by the security team without management input"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Appetite is the strategic, broad level of risk the organization will pursue; tolerance "
                       "is the tactical, acceptable deviation around that level, typically stated as measurable "
                       "thresholds that KRIs monitor.",
            "distractors": {
                "B": "They are related but distinct - one is broad/strategic, the other specific/tactical.",
                "C": "Appetite is rarely zero, and tolerance is not unlimited; both are bounded by objectives.",
                "D": "Both appetite and tolerance are management/board decisions, not set by the security team alone.",
            },
            "exam_pattern": "Appetite = broad strategic level of acceptable risk; tolerance = acceptable, measurable deviation around it.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk appetite versus risk tolerance"],
    },
    {
        "id": "cism-risk-r2-009", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 3, "type": "multi",
        "stem": "A risk is found to EXCEED the organization's risk appetite. Which TWO actions are MOST "
                "appropriate for the information security manager? (Choose two.)",
        "options": [
            {"id": "A", "text": "Present risk treatment options to the risk owner/management for a decision"},
            {"id": "B", "text": "Record the risk and its status in the risk register"},
            {"id": "C", "text": "Unilaterally accept the risk on the organization's behalf"},
            {"id": "D", "text": "Remove the risk from tracking to avoid alarming management"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "When a risk exceeds appetite, the manager escalates with treatment options for the "
                       "risk owner to decide and documents the risk and its status in the register - "
                       "facilitating a management decision, not making it alone.",
            "distractors": {
                "C": "The manager does not own or accept business risk; acceptance is management's decision.",
                "D": "Hiding the risk removes visibility management needs to decide.",
            },
            "exam_pattern": "Over-appetite risk -> manager escalates options to the risk owner and documents it; management decides.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Escalating risks beyond appetite"],
    },
    {
        "id": "cism-risk-r2-010", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 3, "type": "mcq",
        "stem": "An organization transfers risk by buying cyber-insurance and outsourcing security "
                "monitoring. Which statement is TRUE about what has actually been transferred?",
        "options": [
            {"id": "A", "text": "The financial or operational burden may shift, but accountability for the risk and the data remains with the organization"},
            {"id": "B", "text": "All accountability moves permanently to the insurer and the provider"},
            {"id": "C", "text": "The risk can now be deleted from the risk register"},
            {"id": "D", "text": "No further monitoring of the arrangement is required"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Transfer shifts some financial or operational burden to a third party, but the "
                       "organization remains accountable for the risk and its data; transfer is not a way to "
                       "offload accountability.",
            "distractors": {
                "B": "Accountability cannot be transferred away by contract or insurance.",
                "C": "The risk remains and must still be tracked.",
                "D": "Outsourced/insured arrangements require ongoing monitoring of the third party.",
            },
            "exam_pattern": "You can transfer financial/operational burden, not accountability; keep monitoring the arrangement.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Limits of risk transfer"],
    },
    {
        "id": "cism-risk-r2-011", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "mcq",
        "stem": "Management has decided to mitigate a high risk by implementing new controls. What should "
                "the information security manager prepare to guide and track that mitigation?",
        "options": [
            {"id": "A", "text": "A risk treatment (action) plan with assigned owners, actions, and target dates"},
            {"id": "B", "text": "A press release announcing the risk"},
            {"id": "C", "text": "A new company-wide holiday schedule"},
            {"id": "D", "text": "A decision to accept the risk instead"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A risk treatment/action plan documents the chosen controls, responsible owners, "
                       "actions, and timelines so implementation can be driven and tracked to completion.",
            "distractors": {
                "B": "A press release is unrelated to implementing controls.",
                "C": "A holiday schedule has nothing to do with risk treatment.",
                "D": "Accepting the risk contradicts management's decision to mitigate.",
            },
            "exam_pattern": "Chosen mitigation is implemented and tracked via a risk treatment/action plan (owners, actions, dates).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk treatment plans"],
    },
    {
        "id": "cism-risk-r2-012", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Knowingly taking no further action and retaining a risk whose exposure "
                "is within the organization's risk appetite is risk _____. (one word)",
        "correct": ["acceptance", "accept"],
        "explanation": {
            "correct": "Risk acceptance is the informed decision to retain a risk (take no further "
                       "mitigation), appropriate when the residual exposure is within appetite and formally "
                       "approved by the risk owner.",
            "exam_pattern": "Acceptance = informed retention of a risk within appetite, formally approved by management.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk acceptance"],
    },

    # ----- cism_risk_monitoring ----------------------------------------
    {
        "id": "cism-risk-r2-013", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "A key risk indicator (KRI) crosses its predefined threshold, signaling rising exposure. "
                "What should the information security manager do FIRST?",
        "options": [
            {"id": "A", "text": "Investigate the cause and report the changed exposure to the risk owner for a decision"},
            {"id": "B", "text": "Delete the KRI so it stops generating alerts"},
            {"id": "C", "text": "Wait until the next annual review to look into it"},
            {"id": "D", "text": "Immediately shut down all business systems"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A breached KRI threshold is an early warning: the manager analyzes the cause and "
                       "reports the changed exposure to the risk owner so an informed treatment decision can be "
                       "made.",
            "distractors": {
                "B": "Deleting the KRI suppresses the warning it was designed to provide.",
                "C": "Waiting defeats the purpose of an early-warning indicator.",
                "D": "Shutting everything down is disproportionate before the cause is understood.",
            },
            "exam_pattern": "KRI threshold breached -> investigate and escalate to the risk owner; it is an early warning, not an automatic shutdown.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Acting on KRI thresholds"],
    },
    {
        "id": "cism-risk-r2-014", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "What MOST determines whether a metric is an effective key risk indicator (KRI)?",
        "options": [
            {"id": "A", "text": "It is a relevant, measurable leading indicator that reliably signals changes in risk exposure against a threshold"},
            {"id": "B", "text": "It is simply the easiest number for the team to collect"},
            {"id": "C", "text": "It always trends upward over time"},
            {"id": "D", "text": "It is expressed only in deep technical jargon"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A good KRI is relevant to a specific risk, measurable, and predictive (leading) - it "
                       "warns of changing exposure against a defined threshold so management can act early.",
            "distractors": {
                "B": "Ease of collection does not make a metric a meaningful predictor of risk.",
                "C": "A KRI need not always rise; it must reflect actual changes in exposure.",
                "D": "Jargon-heavy metrics are less useful; KRIs should be understandable to decision-makers.",
            },
            "exam_pattern": "Effective KRI = relevant, measurable, leading/predictive, tied to a threshold.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Designing effective KRIs"],
    },
    {
        "id": "cism-risk-r2-015", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Why should the information security manager consider risk AGGREGATION when reviewing the "
                "risk register?",
        "options": [
            {"id": "A", "text": "Several individually minor but related risks can combine into an aggregate risk that exceeds the organization's appetite"},
            {"id": "B", "text": "Aggregation always reduces the total level of risk"},
            {"id": "C", "text": "It allows unrelated risks to be deleted in bulk"},
            {"id": "D", "text": "It removes the need to assign risk owners"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risks that look minor in isolation can, when combined or correlated, produce a much "
                       "larger aggregate exposure that breaches appetite; aggregation ensures these are seen "
                       "and managed.",
            "distractors": {
                "B": "Aggregation typically reveals a larger combined exposure, not a smaller one.",
                "C": "Aggregation is about combined exposure, not bulk deletion.",
                "D": "Risk owners are still required regardless of aggregation.",
            },
            "exam_pattern": "Aggregate related 'small' risks - combined they can exceed appetite even when each alone does not.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk aggregation"],
    },
    {
        "id": "cism-risk-r2-016", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Which event should MOST prompt the information security manager to update the "
                "organization's risk register?",
        "options": [
            {"id": "A", "text": "A significant business or environmental change, such as a merger, a new product line, or a major breach affecting the industry"},
            {"id": "B", "text": "A change to the office lunch menu"},
            {"id": "C", "text": "The hiring of a new receptionist"},
            {"id": "D", "text": "A routine, scheduled password reset"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Material changes to the business or threat environment can create, remove, or alter "
                       "risks, so they should trigger an update to the register in addition to periodic review.",
            "distractors": {
                "B": "A lunch-menu change has no effect on the risk profile.",
                "C": "A routine non-sensitive hire does not materially change enterprise risk.",
                "D": "A routine password reset is business as usual, not a risk-changing event.",
            },
            "exam_pattern": "Update the register on significant business/environmental change, not just on a fixed calendar.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Triggers for risk reassessment"],
    },
    {
        "id": "cism-risk-r2-017", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "What is the BEST way to keep senior management informed of the organization's information "
                "security risk status over time?",
        "options": [
            {"id": "A", "text": "Provide regular, consistent risk reporting (e.g., a risk dashboard or updated register) highlighting trends and items outside appetite"},
            {"id": "B", "text": "Forward raw vulnerability-scan output files whenever they are produced"},
            {"id": "C", "text": "Report on risk only after a serious incident has occurred"},
            {"id": "D", "text": "Avoid reporting risk to prevent alarming the board"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Consistent, business-oriented risk reporting - trends, status against appetite, key "
                       "items - gives management the ongoing visibility it needs to make informed decisions.",
            "distractors": {
                "B": "Raw scan files are too technical and not decision-useful for management.",
                "C": "Reporting only after incidents is reactive and leaves management blind in between.",
                "D": "Withholding risk information prevents informed governance.",
            },
            "exam_pattern": "Give management regular, trend-based risk reporting tied to appetite - not raw data or silence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk reporting to management"],
    },
    {
        "id": "cism-risk-r2-018", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The ongoing process of tracking identified risks, control effectiveness "
                "and the threat environment so that risk decisions stay current is risk _____. (one word)",
        "correct": ["monitoring", "monitor"],
        "explanation": {
            "correct": "Risk monitoring is the continuous tracking of risks, control performance, and the "
                       "environment, enabling timely reassessment and reporting as conditions change.",
            "exam_pattern": "Risk monitoring = continuous tracking that keeps the risk picture and decisions current.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk monitoring"],
    },

    # ----- cism_asset_classification -----------------------------------
    {
        "id": "cism-risk-r2-019", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "After information has been classified, what MOST ensures it is protected consistently "
                "throughout its lifecycle?",
        "options": [
            {"id": "A", "text": "Defined handling, labeling, and storage requirements for each classification level"},
            {"id": "B", "text": "A single firewall at the network perimeter"},
            {"id": "C", "text": "Letting each employee decide how to handle the data"},
            {"id": "D", "text": "Automatically deleting all classified data after one week"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Classification only drives protection if each level has defined handling, labeling, "
                       "and storage rules; these make consistent, commensurate protection actionable across the "
                       "data lifecycle.",
            "distractors": {
                "B": "A perimeter firewall is one control and does not govern handling across the lifecycle.",
                "C": "Letting everyone improvise produces inconsistent, non-compliant handling.",
                "D": "Blanket deletion is not a handling scheme and destroys needed data.",
            },
            "exam_pattern": "Classification must be paired with handling/labeling standards per level to drive consistent protection.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Data handling and labeling"],
    },
    {
        "id": "cism-risk-r2-020", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 3, "type": "mcq",
        "stem": "A hospital's PRIMARY concern for its patient medication records is that they not be altered "
                "without authorization. When classifying this data, which security attribute is the primary "
                "driver?",
        "options": [
            {"id": "A", "text": "Integrity"},
            {"id": "B", "text": "Confidentiality"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Scalability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The stated concern is unauthorized alteration, which is an integrity issue; "
                       "classification should ensure controls that protect accuracy and prevent unauthorized "
                       "change.",
            "distractors": {
                "B": "Confidentiality concerns unauthorized disclosure, not alteration.",
                "C": "Availability concerns access/uptime, not unauthorized change.",
                "D": "Scalability is a performance attribute, not a security property.",
            },
            "exam_pattern": "Map the stated concern to CIA: alteration = integrity; disclosure = confidentiality; uptime/access = availability.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Classification and the CIA triad"],
    },
    {
        "id": "cism-risk-r2-021", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 3, "type": "mcq",
        "stem": "Individually, several data fields are low sensitivity, but combined they can identify "
                "individuals and reveal their health status. How should this affect classification?",
        "options": [
            {"id": "A", "text": "The combined dataset may warrant a higher classification than its individual fields, because of aggregation"},
            {"id": "B", "text": "Classification should always follow only the single least-sensitive field"},
            {"id": "C", "text": "Aggregation never changes the sensitivity of data"},
            {"id": "D", "text": "The data should be made public to simplify handling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Aggregation can raise sensitivity: combining individually innocuous fields may enable "
                       "identification or reveal sensitive attributes, so the combined dataset can justify a "
                       "higher classification.",
            "distractors": {
                "B": "Classifying by the least-sensitive field understates the real sensitivity of the aggregate.",
                "C": "Aggregation can materially increase sensitivity through inference.",
                "D": "Making sensitive aggregated data public is reckless.",
            },
            "exam_pattern": "Aggregation can raise classification - combined low-sensitivity data may become sensitive.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Aggregation and classification"],
    },
    {
        "id": "cism-risk-r2-022", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "What should trigger a review of an information asset's classification level?",
        "options": [
            {"id": "A", "text": "A change in the asset's value, sensitivity, or regulatory status, in addition to periodic review"},
            {"id": "B", "text": "Only the eventual retirement of the asset"},
            {"id": "C", "text": "Nothing - a classification is permanent once assigned"},
            {"id": "D", "text": "A change in the company's stock ticker symbol"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity changes over time (e.g., data becomes public, or new regulation applies), "
                       "so classification should be reviewed periodically and whenever the asset's value, "
                       "sensitivity, or regulatory status changes.",
            "distractors": {
                "B": "Retirement is one trigger but far too narrow on its own.",
                "C": "Classification is not permanent; it must be revisited as sensitivity changes.",
                "D": "A ticker-symbol change does not affect data sensitivity.",
            },
            "exam_pattern": "Reclassify on change in value/sensitivity/regulation and on periodic review - classification is not static.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Reviewing classification over time"],
    },
    {
        "id": "cism-risk-r2-023", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 3, "type": "mcq",
        "stem": "When designing a data classification scheme, what is a key BEST practice regarding the "
                "NUMBER of classification levels?",
        "options": [
            {"id": "A", "text": "Use the fewest levels necessary so the scheme is simple enough to be applied consistently"},
            {"id": "B", "text": "Create as many levels as possible for maximum granularity"},
            {"id": "C", "text": "Use exactly one level for all data in the organization"},
            {"id": "D", "text": "Let each department invent its own incompatible set of levels"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A workable scheme uses the fewest levels needed to distinguish protection "
                       "requirements; too many levels become confusing and are applied inconsistently, "
                       "undermining the whole scheme.",
            "distractors": {
                "B": "Excessive granularity is impractical and leads to inconsistent classification.",
                "C": "A single level cannot distinguish differing protection needs.",
                "D": "Incompatible per-department schemes destroy consistency and interoperability.",
            },
            "exam_pattern": "Keep the classification scheme simple (few, clear levels) so it is applied consistently.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Designing a classification scheme"],
    },
    {
        "id": "cism-risk-r2-024", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Assigning a sensitivity level such as 'Confidential' or 'Public' to "
                "information so that commensurate controls can be applied is called data _____. (one word)",
        "correct": ["classification"],
        "explanation": {
            "correct": "Data classification assigns a sensitivity level to information so that protection can "
                       "be applied in proportion to its value and sensitivity.",
            "exam_pattern": "Classification = assigning sensitivity levels so controls match the data's value/sensitivity.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Data classification"],
    },

    # ====================================================================
    # DOMAIN 3 - INFORMATION SECURITY PROGRAM (40)
    # ====================================================================

    # ----- cism_program_development ------------------------------------
    {
        "id": "cism-prog-r2-001", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 3, "type": "mcq",
        "stem": "Two proposed initiatives would reduce similar amounts of risk, but one costs far less "
                "than the other. From a CISM perspective, which should the information security manager "
                "prioritize, and why?",
        "options": [
            {"id": "A", "text": "The lower-cost initiative, because it delivers greater value and optimizes limited resources"},
            {"id": "B", "text": "The higher-cost initiative, because higher spending always means better security"},
            {"id": "C", "text": "Whichever initiative the newest vendor is promoting"},
            {"id": "D", "text": "Neither, because cost should never influence a security decision"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With comparable risk reduction, the lower-cost option provides greater value and makes "
                       "better use of scarce resources - resource optimization and value delivery are core "
                       "program objectives.",
            "distractors": {
                "B": "Spending more does not linearly improve security and ignores cost-benefit.",
                "C": "Vendor promotion is not a basis for prioritization.",
                "D": "Cost-effectiveness is central to program decisions; cost must be considered.",
            },
            "exam_pattern": "Equal risk reduction -> choose the more cost-effective option (value delivery, resource optimization).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Resource optimization and value"],
    },
    {
        "id": "cism-prog-r2-002", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "A business unit complains that security 'slows them down.' What is the BEST way for the "
                "information security manager to position the security program?",
        "options": [
            {"id": "A", "text": "As a business enabler that manages risk so the business can pursue its objectives safely, engaging with the unit early"},
            {"id": "B", "text": "As a gatekeeper whose main job is to say 'no' to new initiatives"},
            {"id": "C", "text": "As a purely technical function with no need for business involvement"},
            {"id": "D", "text": "As an obstacle the business simply has to tolerate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security should be framed and run as a business enabler: by managing risk and engaging "
                       "early, it helps the business move faster and more safely, which also builds support for "
                       "the program.",
            "distractors": {
                "B": "A 'department of no' creates friction and gets bypassed.",
                "C": "Security divorced from the business cannot align with objectives.",
                "D": "Positioning security as an obstacle undermines its own effectiveness.",
            },
            "exam_pattern": "Position security as a business enabler (manage risk, engage early), not a blocker.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security as a business enabler"],
    },
    {
        "id": "cism-prog-r2-003", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "At what point is it MOST cost-effective to incorporate security requirements into a new "
                "application?",
        "options": [
            {"id": "A", "text": "Early, during the requirements and design phases of the development lifecycle"},
            {"id": "B", "text": "After the application is already in production"},
            {"id": "C", "text": "Only once a vulnerability has been exploited"},
            {"id": "D", "text": "Never, since developers will handle it informally"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Building security in from requirements/design is far cheaper and more effective than "
                       "retrofitting it; defects found late cost much more to fix (security by design).",
            "distractors": {
                "B": "Adding security after go-live means costly rework and residual exposure.",
                "C": "Waiting for exploitation is reactive and damaging.",
                "D": "Leaving it to informal handling produces inconsistent, weak controls.",
            },
            "exam_pattern": "Build security in early (requirements/design) - the SDLC is where it is cheapest and most effective.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security in the SDLC"],
    },
    {
        "id": "cism-prog-r2-004", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "The information security strategy sets direction. What does the information security "
                "PROGRAM primarily provide?",
        "options": [
            {"id": "A", "text": "The execution - the projects, controls, resources, and processes that implement the strategy"},
            {"id": "B", "text": "The organization's risk appetite"},
            {"id": "C", "text": "The board's governance charter"},
            {"id": "D", "text": "The external auditor's independent opinion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The program is the execution vehicle: it delivers the initiatives, controls, people, "
                       "and processes that turn the strategy's direction into operational reality.",
            "distractors": {
                "B": "Risk appetite is set by the board/senior management, not produced by the program.",
                "C": "A governance charter is a governance artifact, not the program.",
                "D": "The auditor's opinion is independent assurance, separate from the program.",
            },
            "exam_pattern": "Strategy = direction; program = execution (projects, controls, resources, processes).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Program as execution of the strategy"],
    },
    {
        "id": "cism-prog-r2-005", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "Before rolling out specific technical controls under a new security program, what should "
                "the information security manager ensure is approved to give those controls their authority?",
        "options": [
            {"id": "A", "text": "Information security policies (and supporting standards) approved by management"},
            {"id": "B", "text": "A new corporate brand logo"},
            {"id": "C", "text": "The procurement team's travel budget"},
            {"id": "D", "text": "A list of competitor tools"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Controls derive their mandate from management-approved policies and standards; "
                       "establishing that authority first makes the controls enforceable and defensible.",
            "distractors": {
                "B": "A logo has nothing to do with control authority.",
                "C": "A travel budget is unrelated to the program's mandate.",
                "D": "A competitor tool list does not authorize the organization's controls.",
            },
            "exam_pattern": "Controls get their authority from approved policies/standards - establish those first.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Policies as the foundation for controls"],
    },
    {
        "id": "cism-prog-r2-006", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "To prevent security from being unintentionally weakened when systems are modified, security "
                "review should be embedded in which process?",
        "options": [
            {"id": "A", "text": "Change management"},
            {"id": "B", "text": "Payroll processing"},
            {"id": "C", "text": "The annual holiday calendar"},
            {"id": "D", "text": "Office space planning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Embedding security review in the change-management process ensures modifications are "
                       "assessed for security impact and approved before implementation, preventing drift and "
                       "unmanaged risk.",
            "distractors": {
                "B": "Payroll is unrelated to securing system changes.",
                "C": "A holiday calendar has no bearing on change security.",
                "D": "Office space planning does not govern system modifications.",
            },
            "exam_pattern": "Integrate security into change management so modifications are risk-assessed and approved.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security in change management"],
    },
    {
        "id": "cism-prog-r2-007", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Designing systems and processes so that security is built in from the "
                "outset rather than added later is known as security by _____. (one word)",
        "correct": ["design"],
        "explanation": {
            "correct": "Security by design embeds security into architecture and development from the start, "
                       "which is more effective and cheaper than retrofitting controls later.",
            "exam_pattern": "Security by design = build security in from the start (cheaper, stronger than bolt-on).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security by design"],
    },

    # ----- cism_security_controls --------------------------------------
    {
        "id": "cism-prog-r2-008", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "Restoring affected systems from clean backups after a ransomware attack is an example of "
                "which functional control type?",
        "options": [
            {"id": "A", "text": "Corrective"},
            {"id": "B", "text": "Preventive"},
            {"id": "C", "text": "Deterrent"},
            {"id": "D", "text": "Detective"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A corrective control restores systems/operations after an incident - recovering from "
                       "backup is a classic corrective (recovery) action.",
            "distractors": {
                "B": "Preventive controls stop an event before it happens.",
                "C": "Deterrent controls discourage an action (e.g., a warning banner).",
                "D": "Detective controls identify that an event occurred (e.g., alerts), not restore service.",
            },
            "exam_pattern": "Restore/repair after an event = corrective; prevent = before; detect = find; deter = discourage.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control types (corrective)"],
    },
    {
        "id": "cism-prog-r2-009", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A login banner warning that systems are monitored and that unauthorized use will be "
                "prosecuted is BEST classified as which control type?",
        "options": [
            {"id": "A", "text": "Deterrent"},
            {"id": "B", "text": "Corrective"},
            {"id": "C", "text": "Recovery"},
            {"id": "D", "text": "Compensating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A deterrent control discourages a would-be actor from attempting an action; a warning "
                       "banner is intended to dissuade misuse.",
            "distractors": {
                "B": "Corrective controls fix or restore after an event.",
                "C": "Recovery controls restore operations after disruption.",
                "D": "A compensating control substitutes for an infeasible primary control.",
            },
            "exam_pattern": "Warning banner/signage = deterrent (discourages the act before it happens).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control types (deterrent)"],
    },
    {
        "id": "cism-prog-r2-010", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "Granting each user only the access rights required to perform their job duties implements "
                "which principle?",
        "options": [
            {"id": "A", "text": "Least privilege"},
            {"id": "B", "text": "Defense in depth"},
            {"id": "C", "text": "Security through obscurity"},
            {"id": "D", "text": "Implicit allow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Least privilege limits each user's access to only what is needed for their role, "
                       "reducing the attack surface and the impact of compromise or misuse.",
            "distractors": {
                "B": "Defense in depth is about layering multiple controls, not limiting individual access.",
                "C": "Security through obscurity relies on secrecy of design, not on restricting access.",
                "D": "Implicit allow is the opposite of good practice; default-deny is preferred.",
            },
            "exam_pattern": "Minimum access needed for the job = least privilege.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Least privilege"],
    },
    {
        "id": "cism-prog-r2-011", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A process is designed so that no single individual can both initiate and approve the same "
                "financial transaction. Which control principle does this implement?",
        "options": [
            {"id": "A", "text": "Separation (segregation) of duties"},
            {"id": "B", "text": "Least privilege"},
            {"id": "C", "text": "Job rotation"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Separation of duties divides a sensitive task among people so that no one person can "
                       "complete it alone, reducing fraud and error.",
            "distractors": {
                "B": "Least privilege limits access scope but does not by itself split a transaction across people.",
                "C": "Job rotation moves staff between roles to detect/deter fraud; it is a different control.",
                "D": "Single sign-on is an authentication convenience, not a duty-splitting control.",
            },
            "exam_pattern": "No single person completes a sensitive transaction = separation/segregation of duties.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Separation of duties"],
    },
    {
        "id": "cism-prog-r2-012", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "Deploying multiple, overlapping layers of controls so that the failure of any one layer "
                "does not immediately expose the asset is BEST described as:",
        "options": [
            {"id": "A", "text": "Defense in depth (layered security)"},
            {"id": "B", "text": "A single point of failure"},
            {"id": "C", "text": "Risk acceptance"},
            {"id": "D", "text": "Security through obscurity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defense in depth layers independent controls so that if one fails, others still "
                       "protect the asset - redundancy that improves resilience.",
            "distractors": {
                "B": "A single point of failure is the opposite - one failure causes full exposure.",
                "C": "Risk acceptance is a treatment decision, not a layering strategy.",
                "D": "Security through obscurity relies on secrecy, not layered controls.",
            },
            "exam_pattern": "Overlapping, independent layers = defense in depth.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Defense in depth"],
    },
    {
        "id": "cism-prog-r2-013", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are technical (logical) controls? (Choose two.)",
        "options": [
            {"id": "A", "text": "Encryption of data at rest"},
            {"id": "B", "text": "Multi-factor authentication"},
            {"id": "C", "text": "A security awareness poster in the break room"},
            {"id": "D", "text": "A visitor sign-in sheet at reception"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Encryption and multi-factor authentication are technical (logical) controls "
                       "implemented in systems/software.",
            "distractors": {
                "C": "An awareness poster is an administrative/awareness control.",
                "D": "A visitor sign-in sheet is a physical/administrative control at the premises.",
            },
            "exam_pattern": "Technical = implemented in systems (encryption, MFA, ACLs); administrative = policy/training; physical = premises.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Technical control category"],
    },
    {
        "id": "cism-prog-r2-014", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Controls are grouped into three categories by their nature: technical, "
                "physical, and _____ (managerial). (one word)",
        "correct": ["administrative", "managerial"],
        "explanation": {
            "correct": "The three control categories are technical (logical), physical, and administrative "
                       "(managerial) - the people/process controls such as policies, procedures, and training.",
            "exam_pattern": "Control categories: technical, physical, administrative (managerial).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control categories"],
    },

    # ----- cism_program_frameworks -------------------------------------
    {
        "id": "cism-prog-r2-015", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "NIST Cybersecurity Framework 2.0 introduced a new core function covering organizational "
                "context, risk-management strategy, roles, policy, and oversight. Which function is it?",
        "options": [
            {"id": "A", "text": "Govern"},
            {"id": "B", "text": "Protect"},
            {"id": "C", "text": "Recover"},
            {"id": "D", "text": "Respond"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CSF 2.0 added Govern as a sixth core function, emphasizing governance, risk strategy, "
                       "roles/responsibilities, and policy that cut across the other five functions.",
            "distractors": {
                "B": "Protect (safeguards) was already a core function in CSF 1.1.",
                "C": "Recover (restoration) was already present in CSF 1.1.",
                "D": "Respond (acting on detected incidents) was already present in CSF 1.1.",
            },
            "exam_pattern": "CSF 2.0 functions: Govern (new), Identify, Protect, Detect, Respond, Recover.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - NIST CSF 2.0 Govern function"],
    },
    {
        "id": "cism-prog-r2-016", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "Which publication provides a comprehensive catalog of security and privacy controls widely "
                "used by U.S. federal agencies and their contractors?",
        "options": [
            {"id": "A", "text": "NIST SP 800-53"},
            {"id": "B", "text": "ISO/IEC 27014"},
            {"id": "C", "text": "PCI DSS"},
            {"id": "D", "text": "ITIL"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NIST SP 800-53 is a detailed catalog of security and privacy controls, extensively "
                       "used across U.S. federal systems and beyond.",
            "distractors": {
                "B": "ISO/IEC 27014 addresses the governance of information security, not a control catalog.",
                "C": "PCI DSS is a payment-card data security standard, not a general control catalog.",
                "D": "ITIL is an IT service-management framework, not a security control catalog.",
            },
            "exam_pattern": "Comprehensive control catalog (US federal) = NIST SP 800-53.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - NIST SP 800-53 control catalog"],
    },
    {
        "id": "cism-prog-r2-017", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "An organization stores and processes credit-card data. Which standard applies MOST "
                "directly to that activity?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "NIST Cybersecurity Framework"},
            {"id": "C", "text": "ISO 22301"},
            {"id": "D", "text": "COBIT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Payment Card Industry Data Security Standard (PCI DSS) directly governs the "
                       "handling of cardholder data.",
            "distractors": {
                "B": "The NIST CSF is a voluntary cybersecurity framework, not the card-data mandate.",
                "C": "ISO 22301 is a business-continuity management standard.",
                "D": "COBIT is an enterprise IT governance framework, not a card-data standard.",
            },
            "exam_pattern": "Cardholder data = PCI DSS applies most directly.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - PCI DSS applicability"],
    },
    {
        "id": "cism-prog-r2-018", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY benefit of adopting an established security control framework rather "
                "than building controls ad hoc?",
        "options": [
            {"id": "A", "text": "It provides a structured, comprehensive, recognized baseline that reduces gaps and supports consistency and benchmarking"},
            {"id": "B", "text": "It guarantees the organization can never be breached"},
            {"id": "C", "text": "It removes the need to perform a risk assessment"},
            {"id": "D", "text": "It eliminates the need for management involvement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A recognized framework gives a complete, structured starting point so controls are "
                       "comprehensive and consistent, gaps are reduced, and the program can be benchmarked and "
                       "assured.",
            "distractors": {
                "B": "No framework guarantees breach immunity.",
                "C": "Frameworks are applied on a risk basis; they do not replace risk assessment.",
                "D": "Management involvement remains essential to governance and resourcing.",
            },
            "exam_pattern": "Frameworks give a structured, comprehensive, benchmarkable baseline - not a breach guarantee.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Value of control frameworks"],
    },
    {
        "id": "cism-prog-r2-019", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "When selecting a security framework or control set, what should MOST influence the choice?",
        "options": [
            {"id": "A", "text": "The organization's business objectives, regulatory requirements, and risk profile"},
            {"id": "B", "text": "Whichever framework has the longest name"},
            {"id": "C", "text": "The personal preference of a single engineer"},
            {"id": "D", "text": "Whatever framework is cheapest to download"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The right framework is the one that fits the organization's context - its objectives, "
                       "the regulations it must meet, and its risk profile - not a generic or arbitrary choice.",
            "distractors": {
                "B": "A name's length is irrelevant.",
                "C": "One engineer's preference is not a sound organizational basis.",
                "D": "Download cost is trivial compared with fit-for-purpose.",
            },
            "exam_pattern": "Choose a framework for fit: business objectives, regulatory needs, and risk profile.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Selecting an appropriate framework"],
    },
    {
        "id": "cism-prog-r2-020", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: The ISO/IEC standard that provides guidance specifically on information "
                "security risk management, supporting an ISMS, is ISO/IEC _____. (enter the number)",
        "correct": ["27005"],
        "explanation": {
            "correct": "ISO/IEC 27005 gives guidance on information security risk management, complementing "
                       "the ISMS requirements of ISO/IEC 27001 and the controls of ISO/IEC 27002.",
            "exam_pattern": "27001 = ISMS requirements; 27002 = controls; 27005 = risk management; 27014 = governance.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - ISO/IEC 27005 risk management"],
    },

    # ----- cism_awareness_training -------------------------------------
    {
        "id": "cism-prog-r2-021", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 3, "type": "mcq",
        "stem": "Which statement BEST distinguishes security 'awareness' from security 'training'?",
        "options": [
            {"id": "A", "text": "Awareness changes attitudes and keeps security top-of-mind across the workforce, while training teaches specific skills needed to perform tasks securely"},
            {"id": "B", "text": "They are the same thing with different names"},
            {"id": "C", "text": "Awareness is only for IT and training is only for executives"},
            {"id": "D", "text": "Training is a one-time poster and awareness is a professional certification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Awareness focuses general attention and attitudes so people recognize risks; training "
                       "builds specific job skills (e.g., secure coding). They are complementary, not identical.",
            "distractors": {
                "B": "They differ in purpose and depth - broad attitude change versus specific skills.",
                "C": "Both apply across the workforce, not to narrow audiences.",
                "D": "This mischaracterizes both; a poster is an awareness tactic, not training.",
            },
            "exam_pattern": "Awareness = attention/attitude (broad); training = specific skills to perform tasks securely.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Awareness versus training"],
    },
    {
        "id": "cism-prog-r2-022", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 2, "type": "mcq",
        "stem": "Developers need secure-coding training while finance staff need to recognize payment "
                "fraud. This difference illustrates the need for security education that is:",
        "options": [
            {"id": "A", "text": "Role-based (tailored to job responsibilities)"},
            {"id": "B", "text": "Identical for every employee"},
            {"id": "C", "text": "Delivered only once at hire"},
            {"id": "D", "text": "Limited to the security team"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Different roles face different risks, so role-based education targets the content each "
                       "group actually needs, making it relevant and effective.",
            "distractors": {
                "B": "One-size-fits-all content ignores role-specific risks.",
                "C": "One-time-at-hire training is not sufficient or ongoing.",
                "D": "Education must reach the whole workforce, not just the security team.",
            },
            "exam_pattern": "Different roles, different risks -> role-based training.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Role-based security education"],
    },
    {
        "id": "cism-prog-r2-023", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 2, "type": "mcq",
        "stem": "When should security awareness education BEST be delivered to employees?",
        "options": [
            {"id": "A", "text": "At onboarding and then reinforced periodically and whenever significant changes occur"},
            {"id": "B", "text": "Only after an employee has caused an incident"},
            {"id": "C", "text": "Only during the annual financial audit"},
            {"id": "D", "text": "Never, to avoid distracting staff"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Awareness should start at onboarding and be reinforced on an ongoing basis (and on "
                       "relevant change) so it stays current and shapes a lasting security culture.",
            "distractors": {
                "B": "Training only after an incident is reactive and too late.",
                "C": "Tying awareness to the audit cycle is arbitrary and insufficient.",
                "D": "Skipping awareness leaves the workforce vulnerable.",
            },
            "exam_pattern": "Awareness is continuous: at onboarding and reinforced periodically and on change.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Timing and frequency of awareness"],
    },
    {
        "id": "cism-prog-r2-024", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 3, "type": "mcq",
        "stem": "Which of the following BEST indicates that an organization has a strong security culture?",
        "options": [
            {"id": "A", "text": "Employees proactively report suspicious activity and follow policy without needing to be compelled"},
            {"id": "B", "text": "Employees never mention or think about security at all"},
            {"id": "C", "text": "Only the security team is aware of the policies"},
            {"id": "D", "text": "Staff routinely share passwords to work faster"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A strong culture shows in behavior: people proactively report concerns and follow "
                       "policy because they value security, not merely because they are forced to.",
            "distractors": {
                "B": "Silence/apathy signals a weak culture, not a strong one.",
                "C": "Policies known only to the security team indicate poor awareness.",
                "D": "Password sharing is insecure behavior, the opposite of a strong culture.",
            },
            "exam_pattern": "Strong culture = proactive reporting and voluntary policy adherence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security culture indicators"],
    },
    {
        "id": "cism-prog-r2-025", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of running simulated phishing campaigns against employees?",
        "options": [
            {"id": "A", "text": "To measure susceptibility and improve behavior through targeted follow-up training"},
            {"id": "B", "text": "To identify and punish individual employees"},
            {"id": "C", "text": "To replace all email-filtering technology"},
            {"id": "D", "text": "To satisfy a request from the marketing department"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Phishing simulations are a measurement-and-improvement tool: they gauge resilience and "
                       "direct targeted training, strengthening behavior over time.",
            "distractors": {
                "B": "Using simulations punitively undermines trust and reporting.",
                "C": "Simulations do not replace technical email controls.",
                "D": "They serve security objectives, not marketing.",
            },
            "exam_pattern": "Phishing simulations measure and improve behavior (training), not punish staff or replace controls.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Phishing simulations"],
    },
    {
        "id": "cism-prog-r2-026", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Security _____ programs aim to change employee behavior and build a "
                "security-conscious culture across the entire workforce. (one word)",
        "correct": ["awareness"],
        "explanation": {
            "correct": "Security awareness programs seek to change behavior and build a security-conscious "
                       "culture, complementing (not replacing) technical controls.",
            "exam_pattern": "Awareness programs target behavior change and culture across the workforce.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security awareness programs"],
    },

    # ----- cism_metrics_reporting --------------------------------------
    {
        "id": "cism-prog-r2-027", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A metric confirms that 100% of critical systems were recovered within their recovery time "
                "objectives during the last disaster-recovery test - measuring achievement of a desired "
                "goal. This is BEST described as a:",
        "options": [
            {"id": "A", "text": "Key goal indicator (KGI)"},
            {"id": "B", "text": "Key risk indicator (KRI)"},
            {"id": "C", "text": "Key performance indicator (KPI)"},
            {"id": "D", "text": "Service level agreement (SLA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A KGI measures whether a goal/outcome was achieved (here, meeting recovery objectives) "
                       "- it confirms the end result.",
            "distractors": {
                "B": "A KRI signals rising risk exposure, not achievement of a goal.",
                "C": "A KPI measures how well a process is performing, not whether the goal was met.",
                "D": "An SLA is a contractual service commitment, not a metric type.",
            },
            "exam_pattern": "KGI = goal achieved; KPI = process performance; KRI = risk trend.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Key goal indicators"],
    },
    {
        "id": "cism-prog-r2-028", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "mcq",
        "stem": "What MOST makes a security metric valuable to management?",
        "options": [
            {"id": "A", "text": "It is relevant, measurable, and supports a decision or action"},
            {"id": "B", "text": "It produces the largest possible number"},
            {"id": "C", "text": "It is highly technical and hard to interpret"},
            {"id": "D", "text": "Its definition changes every reporting period"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A useful metric is relevant to objectives, measurable, and actionable - it informs a "
                       "decision; otherwise it is noise.",
            "distractors": {
                "B": "A big number is not inherently meaningful.",
                "C": "Hard-to-interpret metrics do not support decisions.",
                "D": "Shifting definitions destroy comparability and trust.",
            },
            "exam_pattern": "Good metrics are relevant, measurable, and actionable (decision-supporting).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Characteristics of good metrics"],
    },
    {
        "id": "cism-prog-r2-029", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 3, "type": "mcq",
        "stem": "Executives ask the information security manager to justify a proposed control's value. "
                "Which is the BEST way to express it?",
        "options": [
            {"id": "A", "text": "The reduction in expected loss (risk) relative to the control's cost"},
            {"id": "B", "text": "The number of lines in the firewall configuration"},
            {"id": "C", "text": "The brand of the appliance purchased"},
            {"id": "D", "text": "The number of hours the team spent installing it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Value to executives is best expressed in business/financial terms: how much the "
                       "control reduces expected loss (risk) for its cost - a cost-benefit view they can act on.",
            "distractors": {
                "B": "Configuration size is a technical detail, not business value.",
                "C": "The appliance brand says nothing about value delivered.",
                "D": "Install hours measure effort, not value or risk reduction.",
            },
            "exam_pattern": "Express value to executives as risk/expected-loss reduction versus cost (cost-benefit).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Communicating security value"],
    },
    {
        "id": "cism-prog-r2-030", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "mcq",
        "stem": "Which type of metric is MOST useful to the security operations team for managing "
                "day-to-day performance?",
        "options": [
            {"id": "A", "text": "Operational metrics such as mean time to detect, mean time to respond, and patch timeliness"},
            {"id": "B", "text": "The board's three-year risk-appetite statement"},
            {"id": "C", "text": "The company's quarterly stock price"},
            {"id": "D", "text": "The CEO's travel schedule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Operations teams need granular operational metrics (detection/response times, patch "
                       "timeliness) to manage and improve day-to-day performance.",
            "distractors": {
                "B": "A multi-year appetite statement is strategic, not operational.",
                "C": "Stock price is unrelated to security operations performance.",
                "D": "The CEO's schedule is irrelevant to operations metrics.",
            },
            "exam_pattern": "Match the metric to the audience: operations needs operational metrics; the board needs strategic ones.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Audience-appropriate metrics"],
    },
    {
        "id": "cism-prog-r2-031", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "mcq",
        "stem": "To make a security metric meaningful for tracking progress, what is MOST important to "
                "establish alongside it?",
        "options": [
            {"id": "A", "text": "A baseline and target/threshold so trends and deviations can be interpreted"},
            {"id": "B", "text": "A longer report cover page"},
            {"id": "C", "text": "A new color scheme for the dashboard"},
            {"id": "D", "text": "A rule that the metric may never be changed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A metric is only interpretable against a baseline and target/threshold; these let you "
                       "see trends, judge performance, and know when to act.",
            "distractors": {
                "B": "A cover page adds no analytical value.",
                "C": "Colors are cosmetic, not analytical.",
                "D": "Metrics may need refinement; freezing definitions forever is not a requirement for meaning.",
            },
            "exam_pattern": "Give metrics a baseline and target so trends/deviations are meaningful.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Baselines and targets for metrics"],
    },
    {
        "id": "cism-prog-r2-032", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A manager wants to report security performance across several perspectives - financial, "
                "customer/stakeholder, internal process, and learning/growth - linked to business goals. "
                "Which tool is BEST suited?",
        "options": [
            {"id": "A", "text": "A balanced scorecard"},
            {"id": "B", "text": "A single packet-capture file"},
            {"id": "C", "text": "A raw server log"},
            {"id": "D", "text": "An organization chart"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A balanced scorecard reports performance across multiple linked perspectives tied to "
                       "strategy, which suits communicating security's contribution to business goals.",
            "distractors": {
                "B": "A packet capture is a low-level technical artifact, not a strategic reporting tool.",
                "C": "A raw log is operational detail, not a multi-perspective scorecard.",
                "D": "An org chart shows structure, not performance.",
            },
            "exam_pattern": "Multiple linked perspectives tied to strategy = balanced scorecard.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Balanced scorecard for security"],
    },
    {
        "id": "cism-prog-r2-033", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A metric that measures how well a process is performing against its "
                "target, such as the mean time to detect incidents, is a key _____ indicator. (one word)",
        "correct": ["performance"],
        "explanation": {
            "correct": "A key performance indicator (KPI) measures how well a process performs against a "
                       "target, such as detection or patching timeliness.",
            "exam_pattern": "KPI = process performance vs target; KGI = goal met; KRI = risk trend.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Key performance indicators"],
    },

    # ----- cism_third_party_mgmt ---------------------------------------
    {
        "id": "cism-prog-r2-034", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "A cloud provider will not permit customer on-site audits. What is the BEST alternative way "
                "for the information security manager to gain assurance over the provider's controls?",
        "options": [
            {"id": "A", "text": "Obtain and review an independent third-party audit report, such as a SOC 2 Type II"},
            {"id": "B", "text": "Trust the provider's marketing brochure"},
            {"id": "C", "text": "Assume the controls are adequate because the provider is large"},
            {"id": "D", "text": "Skip assurance entirely to save time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When direct audits are not possible, an independent assurance report (e.g., SOC 2 Type "
                       "II) provides credible, third-party evidence of the provider's control design and "
                       "operating effectiveness.",
            "distractors": {
                "B": "Marketing material is not independent assurance.",
                "C": "Size is not evidence of effective controls.",
                "D": "Skipping assurance leaves third-party risk unmanaged.",
            },
            "exam_pattern": "No on-site audit? Rely on independent assurance reports (SOC 2 Type II) for evidence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Third-party assurance reports"],
    },
    {
        "id": "cism-prog-r2-035", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Under the cloud shared-responsibility model for infrastructure as a service (IaaS), who is "
                "responsible for securing the customer's data and its access configuration?",
        "options": [
            {"id": "A", "text": "The customer organization"},
            {"id": "B", "text": "The cloud provider alone"},
            {"id": "C", "text": "No one is responsible"},
            {"id": "D", "text": "The end users' internet service provider"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In IaaS, the provider secures the underlying infrastructure, but the customer remains "
                       "responsible for its own data, identity/access configuration, and workloads.",
            "distractors": {
                "B": "The provider secures the infrastructure, not the customer's data and configuration.",
                "C": "Responsibility is shared and clearly allocated, not absent.",
                "D": "An ISP has no role in securing the customer's cloud data.",
            },
            "exam_pattern": "Shared responsibility: provider secures the infrastructure; customer secures its data, access, and config.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Cloud shared responsibility"],
    },
    {
        "id": "cism-prog-r2-036", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "A critical vendor subcontracts part of its data processing to other companies. Which risk "
                "should the information security manager MOST consider?",
        "options": [
            {"id": "A", "text": "Fourth-party (subcontractor/supply-chain) risk, requiring flow-down security requirements and visibility"},
            {"id": "B", "text": "No additional risk, since it is entirely the vendor's problem"},
            {"id": "C", "text": "Only the risk that the vendor might raise its prices"},
            {"id": "D", "text": "The risk that the vendor's logo might change"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Subcontractors (fourth parties) can introduce risk the organization is still "
                       "accountable for; contracts should flow down security requirements and provide visibility "
                       "into the chain.",
            "distractors": {
                "B": "Accountability extends down the supply chain; it is not solely the vendor's problem.",
                "C": "Pricing is a commercial concern, not the security risk at issue.",
                "D": "A logo change is trivial and irrelevant to data risk.",
            },
            "exam_pattern": "Subcontracting creates fourth-party/supply-chain risk - flow down requirements and keep visibility.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Fourth-party and supply-chain risk"],
    },
    {
        "id": "cism-prog-r2-037", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "When a contract with a third-party service provider ends, what is the MOST important "
                "security action?",
        "options": [
            {"id": "A", "text": "Ensure return or secure destruction of the organization's data and revoke all of the provider's access"},
            {"id": "B", "text": "Immediately publish a public thank-you note"},
            {"id": "C", "text": "Leave the provider's accounts active in case they are needed later"},
            {"id": "D", "text": "Delete the organization's own production systems"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secure offboarding requires recovering or destroying the organization's data and "
                       "revoking the provider's access so no residual exposure remains after the relationship ends.",
            "distractors": {
                "B": "A thank-you note does nothing to manage the security exposure.",
                "C": "Leaving accounts active is an open door - exactly the risk to close.",
                "D": "Deleting your own systems is self-harm and unrelated to offboarding the vendor.",
            },
            "exam_pattern": "Vendor offboarding = recover/destroy data and revoke all access.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Third-party offboarding"],
    },
    {
        "id": "cism-prog-r2-038", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "With hundreds of third-party relationships, how should the information security manager "
                "BEST focus third-party risk-management effort?",
        "options": [
            {"id": "A", "text": "Tier and prioritize vendors based on the sensitivity of data and level of access they have (risk-based)"},
            {"id": "B", "text": "Treat every vendor identically regardless of risk"},
            {"id": "C", "text": "Review only the vendor with the smallest contract"},
            {"id": "D", "text": "Ignore vendors that have been used for a long time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk-based tiering concentrates due diligence and monitoring on the vendors that "
                       "handle the most sensitive data or have the most access, using limited resources where "
                       "exposure is greatest.",
            "distractors": {
                "B": "Identical treatment wastes effort on low-risk vendors and under-serves high-risk ones.",
                "C": "Contract size is not a proxy for risk.",
                "D": "Long-standing vendors are not automatically low risk.",
            },
            "exam_pattern": "Tier/prioritize vendors by data sensitivity and access (risk-based focus).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Risk-based vendor tiering"],
    },
    {
        "id": "cism-prog-r2-039", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Which contractual clause MOST helps the organization meet its OWN breach-notification "
                "obligations if a vendor is compromised?",
        "options": [
            {"id": "A", "text": "A requirement that the vendor notify the organization of security incidents within a defined timeframe"},
            {"id": "B", "text": "A clause fixing the vendor's logo colors"},
            {"id": "C", "text": "A clause waiving all vendor responsibility for incidents"},
            {"id": "D", "text": "A clause prohibiting the vendor from ever discussing security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A defined incident-notification clause ensures the organization learns of a vendor "
                       "breach quickly enough to meet its own regulatory notification deadlines.",
            "distractors": {
                "B": "Logo colors are irrelevant to incident notification.",
                "C": "Waiving vendor responsibility removes the very obligation needed.",
                "D": "Prohibiting security discussion is counterproductive and dangerous.",
            },
            "exam_pattern": "Require timely vendor incident notification so you can meet your own breach-notification obligations.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Vendor incident-notification clauses"],
    },
    {
        "id": "cism-prog-r2-040", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Risk introduced to an organization through its vendors, suppliers, and "
                "service providers is collectively called third-_____ risk. (one word)",
        "correct": ["party"],
        "explanation": {
            "correct": "Third-party risk is the risk arising from vendors, suppliers, and service providers; "
                       "the organization stays accountable and must assess and monitor it.",
            "exam_pattern": "Third-party risk = risk from vendors/suppliers/providers; accountability stays in-house.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Third-party risk"],
    },

    # ====================================================================
    # DOMAIN 4 - INCIDENT MANAGEMENT (36)
    # ====================================================================

    # ----- cism_incident_readiness -------------------------------------
    {
        "id": "cism-inc-r2-001", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 3, "type": "mcq",
        "stem": "Which statement BEST distinguishes a security 'event' from a security 'incident'?",
        "options": [
            {"id": "A", "text": "An event is any observable occurrence in a system; an incident is an event (or series) that actually or imminently jeopardizes security or violates policy"},
            {"id": "B", "text": "They are identical terms"},
            {"id": "C", "text": "An incident is always less serious than an event"},
            {"id": "D", "text": "An event can only occur on weekends"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An event is any observable occurrence; it becomes an incident when it adversely "
                       "affects (or is about to affect) confidentiality, integrity, or availability, or "
                       "violates policy. Not every event is an incident.",
            "distractors": {
                "B": "They are related but distinct - the incident is the adverse subset of events.",
                "C": "An incident is the more serious, adverse case, not the lesser one.",
                "D": "Timing (weekends) has nothing to do with the definition.",
            },
            "exam_pattern": "Event = any observable occurrence; incident = an adverse event that harms or threatens security/policy.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Events versus incidents"],
    },
    {
        "id": "cism-inc-r2-002", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "mcq",
        "stem": "To ensure common incident types (such as phishing or malware) are handled consistently and "
                "quickly, what should the information security manager develop in advance?",
        "options": [
            {"id": "A", "text": "Incident response playbooks (predefined procedures) for those scenarios"},
            {"id": "B", "text": "A larger advertising budget"},
            {"id": "C", "text": "A company picnic schedule"},
            {"id": "D", "text": "A list of the CEO's favorite restaurants"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Playbooks (runbooks) give responders predefined, repeatable steps for specific "
                       "incident types, improving speed and consistency when time matters.",
            "distractors": {
                "B": "An advertising budget does nothing for incident handling.",
                "C": "A picnic schedule is irrelevant to response.",
                "D": "Restaurant preferences have no bearing on readiness.",
            },
            "exam_pattern": "Prepare playbooks/runbooks for common incident types for fast, consistent response.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident response playbooks"],
    },
    {
        "id": "cism-inc-r2-003", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "mcq",
        "stem": "Which factor MOST enables a fast, coordinated response when an incident occurs?",
        "options": [
            {"id": "A", "text": "Clearly defined roles, responsibilities, and the authority to declare and escalate an incident"},
            {"id": "B", "text": "A single technician who keeps all knowledge in their head"},
            {"id": "C", "text": "Waiting for the annual audit to assign duties"},
            {"id": "D", "text": "Letting whoever is available improvise each time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Predefined roles, responsibilities, and clear authority (including who may declare and "
                       "escalate) let the team act immediately and in a coordinated way under pressure.",
            "distractors": {
                "B": "Concentrating knowledge in one person creates a single point of failure.",
                "C": "Assigning duties only at audit time is far too slow for incidents.",
                "D": "Improvising each time yields inconsistent, delayed responses.",
            },
            "exam_pattern": "Defined roles and clear authority to declare/escalate drive fast, coordinated response.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Roles, responsibilities and authority"],
    },
    {
        "id": "cism-inc-r2-004", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 3, "type": "mcq",
        "stem": "To ensure specialized forensic and response expertise is available during a major "
                "incident, what should the information security manager arrange BEFORE an incident occurs?",
        "options": [
            {"id": "A", "text": "A pre-arranged incident response/forensics retainer and defined external contacts"},
            {"id": "B", "text": "Nothing - such help can always be found instantly mid-incident"},
            {"id": "C", "text": "A new marketing campaign"},
            {"id": "D", "text": "A standing ban on calling any outside experts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A retainer and predefined external contacts (forensics, legal, law enforcement) ensure "
                       "expert help can be engaged immediately rather than scrambled for during a crisis.",
            "distractors": {
                "B": "Finding and contracting experts mid-incident wastes critical time.",
                "C": "A marketing campaign is unrelated to response readiness.",
                "D": "Banning outside experts removes a valuable response option.",
            },
            "exam_pattern": "Arrange IR/forensics retainers and external contacts in advance - readiness is preparation.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - External support and retainers"],
    },
    {
        "id": "cism-inc-r2-005", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "mcq",
        "stem": "Which capability MOST improves an organization's ability to DETECT incidents early?",
        "options": [
            {"id": "A", "text": "Centralized logging and monitoring with tuned alerting (e.g., a SIEM)"},
            {"id": "B", "text": "Disabling logging to save storage space"},
            {"id": "C", "text": "Reducing the security team to cut costs"},
            {"id": "D", "text": "Turning off all alerts to avoid noise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Centralized logging/monitoring with well-tuned alerts gives timely visibility into "
                       "suspicious activity, which is foundational to early detection.",
            "distractors": {
                "B": "Disabling logging removes the very data needed to detect incidents.",
                "C": "Cutting the team reduces capacity to detect and respond.",
                "D": "Turning off alerts blinds the team to real events.",
            },
            "exam_pattern": "Early detection depends on monitoring/logging with tuned alerting - not on turning visibility off.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Detection capability"],
    },
    {
        "id": "cism-inc-r2-006", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 3, "type": "mcq",
        "stem": "A company has no incident response capability at all. What is the information security "
                "manager's BEST FIRST step to establish one?",
        "options": [
            {"id": "A", "text": "Obtain senior-management support and an approved incident response policy/mandate, then build the plan and team"},
            {"id": "B", "text": "Immediately buy the most expensive forensic tool on the market"},
            {"id": "C", "text": "Plan to personally handle every future incident alone"},
            {"id": "D", "text": "Wait until the first incident to decide what to do"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Like any program element, an IR capability starts with management support and an "
                       "approved policy/mandate, which provide authority and resources; the plan, team, and "
                       "tooling follow.",
            "distractors": {
                "B": "Buying tools first is technology-led and premature without a mandate or plan.",
                "C": "One person handling everything is unsustainable and a single point of failure.",
                "D": "Waiting for an incident is reactive and leaves the organization exposed.",
            },
            "exam_pattern": "Stand up a capability by first securing management support/mandate and policy, then plan/team/tools.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Establishing an IR capability"],
    },
    {
        "id": "cism-inc-r2-007", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A documented, step-by-step set of procedures for responding to a "
                "specific incident type (also called a runbook) is commonly known as a _____. (one word)",
        "correct": ["playbook", "runbook"],
        "explanation": {
            "correct": "A playbook (runbook) is a predefined, step-by-step procedure for a specific incident "
                       "type, enabling fast and consistent response.",
            "exam_pattern": "Playbook/runbook = predefined step-by-step response procedure for a specific scenario.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Playbooks and runbooks"],
    },

    # ----- cism_incident_response_plan ---------------------------------
    {
        "id": "cism-inc-r2-008", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "Which sequence BEST represents the incident response lifecycle?",
        "options": [
            {"id": "A", "text": "Preparation -> Detection and analysis -> Containment, eradication and recovery -> Post-incident activity"},
            {"id": "B", "text": "Recovery -> Preparation -> Detection -> Containment"},
            {"id": "C", "text": "Containment -> Preparation -> Lessons learned -> Detection"},
            {"id": "D", "text": "Detection -> Eradication -> Preparation -> Containment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The widely used lifecycle runs Preparation, Detection and analysis, Containment/"
                       "eradication/recovery, then Post-incident activity (lessons learned).",
            "distractors": {
                "B": "You cannot recover before preparing or detecting.",
                "C": "Containment cannot precede preparation and detection.",
                "D": "Preparation precedes detection; eradication cannot come before containment.",
            },
            "exam_pattern": "IR lifecycle: Prepare -> Detect/Analyze -> Contain/Eradicate/Recover -> Post-incident.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident response lifecycle"],
    },
    {
        "id": "cism-inc-r2-009", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "Several incidents are reported at the same time and resources are limited. How should the "
                "information security manager prioritize the response?",
        "options": [
            {"id": "A", "text": "By business impact and criticality, addressing the highest-impact incidents first per the classification scheme"},
            {"id": "B", "text": "By whichever was reported first alphabetically"},
            {"id": "C", "text": "By whichever is simply easiest to fix"},
            {"id": "D", "text": "Randomly, to be fair to all incidents"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With limited resources, prioritize by business impact and criticality so the most "
                       "damaging incidents get attention first - consistent with the severity/classification "
                       "scheme.",
            "distractors": {
                "B": "Alphabetical order has no relationship to impact.",
                "C": "Easiest-first can leave the most damaging incident unaddressed.",
                "D": "Random assignment ignores business impact.",
            },
            "exam_pattern": "Triage concurrent incidents by business impact/criticality, not convenience.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Triage and prioritization"],
    },
    {
        "id": "cism-inc-r2-010", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 3, "type": "mcq",
        "stem": "A monitoring alert suggests a possible intrusion. What should the response team do FIRST?",
        "options": [
            {"id": "A", "text": "Validate and analyze the alert to confirm whether a real incident has occurred before declaring and escalating"},
            {"id": "B", "text": "Immediately notify the news media"},
            {"id": "C", "text": "Rebuild every server in the company"},
            {"id": "D", "text": "Ignore it, since alerts are usually false"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Alerts must be validated/triaged first to confirm a true incident and understand its "
                       "nature; declaration, escalation, and action follow from that analysis.",
            "distractors": {
                "B": "Notifying media before confirming anything is premature and harmful.",
                "C": "Mass rebuilds are a disproportionate reaction before analysis.",
                "D": "Dismissing alerts risks missing a genuine intrusion.",
            },
            "exam_pattern": "Detection -> validate/analyze FIRST to confirm a real incident, then declare/escalate/act.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Detection and analysis"],
    },
    {
        "id": "cism-inc-r2-011", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 3, "type": "mcq",
        "stem": "After confirming a breach of regulated personal data, what should the information security "
                "manager ensure regarding notification?",
        "options": [
            {"id": "A", "text": "Notify affected parties and regulators as required by law and the communication plan, involving legal and meeting mandated timeframes"},
            {"id": "B", "text": "Keep the breach permanently secret"},
            {"id": "C", "text": "Notify only if a customer happens to ask"},
            {"id": "D", "text": "Delegate the legal notification decision to the IT help desk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Confirmed breaches of regulated data trigger legal notification duties; the manager "
                       "ensures notifications go to the right parties within required timeframes, with legal "
                       "counsel involved, per the communication plan.",
            "distractors": {
                "B": "Concealing a reportable breach is unlawful.",
                "C": "Notification is driven by legal duty, not by whether a customer asks.",
                "D": "Such legal decisions belong with management/legal, not the help desk.",
            },
            "exam_pattern": "Confirmed regulated-data breach -> notify per law and plan, with legal, within deadlines.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Breach notification during response"],
    },
    {
        "id": "cism-inc-r2-012", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "Who should decide whether to involve law enforcement during a security incident?",
        "options": [
            {"id": "A", "text": "Senior management in consultation with legal counsel, per the incident response plan"},
            {"id": "B", "text": "The first analyst who notices the incident, acting unilaterally"},
            {"id": "C", "text": "The vendor help desk"},
            {"id": "D", "text": "Whoever happens to be nearest the server room"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Involving law enforcement has legal and business implications, so the decision rests "
                       "with senior management and legal counsel following the predefined plan.",
            "distractors": {
                "B": "An analyst lacks the authority and context for this decision.",
                "C": "A vendor help desk has no standing to make this call.",
                "D": "Proximity to the server room confers no decision authority.",
            },
            "exam_pattern": "Law-enforcement involvement = management + legal decision, per the plan.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Law-enforcement involvement"],
    },
    {
        "id": "cism-inc-r2-013", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "During a major incident, who should communicate with the media and the public?",
        "options": [
            {"id": "A", "text": "A designated spokesperson (e.g., communications/PR) delivering approved messaging per the plan"},
            {"id": "B", "text": "Any technical staff member who happens to be available"},
            {"id": "C", "text": "Nobody - all inquiries should be ignored indefinitely"},
            {"id": "D", "text": "The attacker's negotiator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "External communications should flow through a single designated spokesperson using "
                       "approved, consistent messaging to protect accuracy and reputation and meet obligations.",
            "distractors": {
                "B": "Ad hoc technical statements risk inaccurate or damaging disclosures.",
                "C": "Ignoring all inquiries can worsen reputational harm and may breach obligations.",
                "D": "The attacker's negotiator is not an appropriate public voice for the organization.",
            },
            "exam_pattern": "Route external/media communications through one approved spokesperson per the plan.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident communications and spokesperson"],
    },
    {
        "id": "cism-inc-r2-014", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 3, "type": "mcq",
        "stem": "Whether to pay a ransomware demand is BEST decided by:",
        "options": [
            {"id": "A", "text": "Senior management, with input from legal counsel and law enforcement, as a business and legal decision"},
            {"id": "B", "text": "The incident response technician, alone and immediately"},
            {"id": "C", "text": "The help desk"},
            {"id": "D", "text": "The backup-software vendor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Paying a ransom carries business, legal, ethical, and sometimes sanctions "
                       "implications; it is a senior-management decision made with legal and law-enforcement "
                       "input, not a technical call.",
            "distractors": {
                "B": "A technician lacks the authority and context for such a consequential decision.",
                "C": "The help desk has no standing to decide this.",
                "D": "A software vendor has a conflict of interest and no authority here.",
            },
            "exam_pattern": "Ransom-payment decisions are management/legal business decisions, not technical ones.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Ransomware response decisions"],
    },
    {
        "id": "cism-inc-r2-015", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In the incident response plan, the predefined sequence of people and "
                "roles to be informed as an incident's severity increases is the _____ path. (one word)",
        "correct": ["escalation"],
        "explanation": {
            "correct": "The escalation path defines who is notified, and in what order, as severity rises - "
                       "ensuring the right stakeholders (management, legal, executives) are engaged in time.",
            "exam_pattern": "Escalation path = predefined who-to-notify-as-severity-rises sequence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Escalation path"],
    },

    # ----- cism_bcp_dr -------------------------------------------------
    {
        "id": "cism-inc-r2-016", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "After systems are technically restored within the RTO, additional time is needed to "
                "validate data integrity and resume normal business operations. This additional time is "
                "called the:",
        "options": [
            {"id": "A", "text": "Work recovery time (WRT)"},
            {"id": "B", "text": "Recovery point objective (RPO)"},
            {"id": "C", "text": "Mean time between failures (MTBF)"},
            {"id": "D", "text": "Annualized rate of occurrence (ARO)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Work recovery time (WRT) is the time after technical recovery (RTO) needed to verify "
                       "data and restore normal business operations. The maximum tolerable downtime equals RTO "
                       "plus WRT.",
            "distractors": {
                "B": "RPO is the acceptable amount of data loss, not post-recovery work time.",
                "C": "MTBF is a reliability measure, not a recovery interval.",
                "D": "ARO is a frequency measure used in quantitative risk analysis.",
            },
            "exam_pattern": "MTD = RTO + WRT; WRT is the post-restore work needed to resume normal operations.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - RTO, WRT and MTD"],
    },
    {
        "id": "cism-inc-r2-017", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "An alternate processing site that is fully equipped with hardware and current data and can "
                "assume operations within minutes to a few hours is a:",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Cold site"},
            {"id": "C", "text": "Reciprocal agreement"},
            {"id": "D", "text": "Warm site"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hot site is fully equipped and kept current, enabling the fastest failover - "
                       "appropriate when the RTO is very short.",
            "distractors": {
                "B": "A cold site provides only space/utilities; recovery takes much longer.",
                "C": "A reciprocal agreement is a mutual-aid arrangement with another organization, not a ready site.",
                "D": "A warm site is partially equipped and recovers more slowly than a hot site.",
            },
            "exam_pattern": "Fastest recovery = hot site (fully equipped, current data); slowest = cold site.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Alternate site types"],
    },
    {
        "id": "cism-inc-r2-018", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "An organization selects a cold site to minimize cost. What is the MAIN tradeoff of this "
                "choice?",
        "options": [
            {"id": "A", "text": "The longest recovery time, since equipment, software, and data must be installed before operations can resume"},
            {"id": "B", "text": "It is actually the fastest possible recovery option"},
            {"id": "C", "text": "It requires no planning at all"},
            {"id": "D", "text": "It eliminates the need for data backups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cold site is cheapest but provides only space and utilities, so hardware, software, "
                       "and data must be brought in and configured - giving the longest recovery time and "
                       "making it unsuitable for short RTOs.",
            "distractors": {
                "B": "A cold site is the slowest option, not the fastest.",
                "C": "It still requires careful recovery planning and logistics.",
                "D": "Backups are still essential; the cold site needs data restored to it.",
            },
            "exam_pattern": "Cold site = lowest cost but longest recovery; match site type to the RTO.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Cold site tradeoffs"],
    },
    {
        "id": "cism-inc-r2-019", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "The organization wants to validate that recovery systems work at the alternate site "
                "WITHOUT taking production systems offline. Which type of test is BEST?",
        "options": [
            {"id": "A", "text": "A parallel test"},
            {"id": "B", "text": "A full-interruption test"},
            {"id": "C", "text": "A checklist review"},
            {"id": "D", "text": "A structured walkthrough"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A parallel test runs recovery systems alongside production, validating actual recovery "
                       "capability without disrupting live operations.",
            "distractors": {
                "B": "A full-interruption test shuts down production, which the question rules out.",
                "C": "A checklist review only verifies documentation, not actual recovery.",
                "D": "A structured walkthrough is discussion-based and does not validate real recovery.",
            },
            "exam_pattern": "Validate real recovery without disrupting production = parallel test; full-interruption takes production down.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - DR test types"],
    },
    {
        "id": "cism-inc-r2-020", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "Which statement BEST distinguishes a business continuity plan (BCP) from a disaster "
                "recovery plan (DRP)?",
        "options": [
            {"id": "A", "text": "The BCP keeps critical business functions operating during a disruption (business-wide), while the DRP focuses on restoring IT systems and infrastructure"},
            {"id": "B", "text": "They are identical documents"},
            {"id": "C", "text": "The DRP is broader in scope than the BCP"},
            {"id": "D", "text": "The BCP applies only to the IT department"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The BCP is the broad, business-wide plan to keep critical functions running; the DRP "
                       "is the IT-focused subset that restores systems and infrastructure to support it.",
            "distractors": {
                "B": "They have different scopes and purposes.",
                "C": "The BCP is broader; the DRP is the narrower, IT-focused plan.",
                "D": "The BCP spans the whole organization, not just IT.",
            },
            "exam_pattern": "BCP = keep the business running (broad); DRP = restore IT systems (subset).",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - BCP versus DRP"],
    },
    {
        "id": "cism-inc-r2-021", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "To ensure data can be recovered after a site-wide disaster or a ransomware attack that "
                "reaches connected storage, what is the BEST backup practice?",
        "options": [
            {"id": "A", "text": "Maintain tested, offsite (and ideally immutable) backups, following a strategy such as 3-2-1"},
            {"id": "B", "text": "Keep the only backup on the same server as the production data"},
            {"id": "C", "text": "Never test restores, to avoid wear on the media"},
            {"id": "D", "text": "Rely on users to email themselves copies of important files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Offsite, tested, and ideally immutable backups (e.g., 3-2-1: three copies, two media, "
                       "one offsite) survive site disasters and ransomware that reaches connected storage, and "
                       "tested restores prove they work.",
            "distractors": {
                "B": "A backup on the production server is lost with it - a single point of failure.",
                "C": "Untested backups often fail exactly when needed.",
                "D": "User-emailed copies are unmanaged, incomplete, and insecure.",
            },
            "exam_pattern": "Resilient backups are offsite, tested, and ideally immutable (3-2-1).",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Backup strategy and resilience"],
    },
    {
        "id": "cism-inc-r2-022", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The maximum total length of time a critical process can be unavailable "
                "before the organization suffers unacceptable harm is the maximum tolerable _____. (one word)",
        "correct": ["downtime"],
        "explanation": {
            "correct": "Maximum tolerable downtime (MTD) is the outer limit of acceptable unavailability; the "
                       "recovery time objective must fall within it (RTO + WRT <= MTD).",
            "exam_pattern": "MTD = outer limit of tolerable outage; RTO (plus WRT) must stay within the MTD.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Maximum tolerable downtime"],
    },

    # ----- cism_containment_eradication --------------------------------
    {
        "id": "cism-inc-r2-023", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 3, "type": "mcq",
        "stem": "During an active intrusion, the team quickly isolates the affected host to stop the "
                "attacker's spread while preserving it for analysis, planning a more complete fix "
                "afterward. This is BEST described as:",
        "options": [
            {"id": "A", "text": "Short-term containment"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Post-incident review"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Short-term containment takes immediate action (such as isolating a host) to limit "
                       "spread and damage while preserving evidence, before a longer-term fix and eradication.",
            "distractors": {
                "B": "Eradication removes the root cause (malware, footholds), which comes after containment.",
                "C": "Post-incident review happens after the incident is closed.",
                "D": "Recovery restores systems to normal operation after eradication.",
            },
            "exam_pattern": "Immediate isolation to limit spread while preserving evidence = short-term containment.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Short-term versus long-term containment"],
    },
    {
        "id": "cism-inc-r2-024", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 3, "type": "mcq",
        "stem": "Containing an incident may require taking a critical revenue-generating system offline. "
                "Who should make that decision, and on what basis?",
        "options": [
            {"id": "A", "text": "Management/the business owner, based on business impact weighed against the risk of continuing to operate, with the security manager advising"},
            {"id": "B", "text": "The newest analyst, based on personal preference"},
            {"id": "C", "text": "Whoever can act fastest, with no consultation"},
            {"id": "D", "text": "No one - a revenue system must never be taken offline under any circumstances"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Taking a critical system offline is a business decision: management/the business owner "
                       "weighs the operational impact against the risk of continuing, with the security manager "
                       "advising on the risk.",
            "distractors": {
                "B": "An analyst's preference is not an appropriate basis for a business-impacting decision.",
                "C": "Acting without consulting the business can cause avoidable harm.",
                "D": "An absolute rule ignores the risk of allowing an active compromise to continue.",
            },
            "exam_pattern": "Containment actions with business impact are management decisions; the manager advises on risk.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Containment as a business decision"],
    },
    {
        "id": "cism-inc-r2-025", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 3, "type": "mcq",
        "stem": "When collecting digital evidence during an incident, in what order should data generally "
                "be acquired to preserve it?",
        "options": [
            {"id": "A", "text": "Most volatile first (e.g., memory and running state) before less volatile data (e.g., disk and backups)"},
            {"id": "B", "text": "Least volatile first, leaving memory for last"},
            {"id": "C", "text": "In alphabetical order of file names"},
            {"id": "D", "text": "Only whatever is easiest to copy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The order of volatility dictates capturing the most volatile data first (memory, "
                       "running processes, network state) before it is lost, then less volatile media such as "
                       "disk and backups.",
            "distractors": {
                "B": "Capturing least volatile first risks losing volatile data like memory.",
                "C": "Alphabetical order is irrelevant to evidence preservation.",
                "D": "Convenience is not a sound basis for forensic collection order.",
            },
            "exam_pattern": "Follow the order of volatility: collect most volatile (memory) first, least volatile (disk/backups) last.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Order of volatility"],
    },
    {
        "id": "cism-inc-r2-026", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "mcq",
        "stem": "Before analyzing a compromised hard drive, what should the investigator do to protect the "
                "integrity and admissibility of the evidence?",
        "options": [
            {"id": "A", "text": "Create a forensic (bit-for-bit) image, verify it with a hash, and work only on the copy"},
            {"id": "B", "text": "Analyze the original drive directly to save time"},
            {"id": "C", "text": "Reformat the drive and start fresh"},
            {"id": "D", "text": "Let several people edit the original in parallel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Working from a hashed, bit-for-bit forensic image preserves the original unchanged and "
                       "lets the investigator prove the evidence was not altered - essential for admissibility.",
            "distractors": {
                "B": "Analyzing the original risks altering it and undermining its evidentiary value.",
                "C": "Reformatting destroys the evidence entirely.",
                "D": "Multiple people editing the original destroys integrity and chain of custody.",
            },
            "exam_pattern": "Preserve evidence: image bit-for-bit, hash it, and analyze the copy - never the original.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Forensic imaging and evidence integrity"],
    },
    {
        "id": "cism-inc-r2-027", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "mcq",
        "stem": "Why is identifying the root cause essential before an incident can be considered fully "
                "ERADICATED?",
        "options": [
            {"id": "A", "text": "To ensure the underlying vulnerability and any attacker footholds are completely removed so the incident cannot simply recur"},
            {"id": "B", "text": "To determine which employee to fire"},
            {"id": "C", "text": "To close the ticket faster regardless of the cause"},
            {"id": "D", "text": "To justify buying more products"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Without addressing the root cause (the exploited weakness and any persistence), the "
                       "attacker can return and the incident recurs; eradication must remove the cause, not just "
                       "visible symptoms.",
            "distractors": {
                "B": "Eradication is about removing the technical cause, not assigning blame.",
                "C": "Closing the ticket prematurely leaves the organization exposed.",
                "D": "Root-cause analysis is about remediation, not justifying purchases.",
            },
            "exam_pattern": "Eradicate the root cause (vulnerability + footholds) so the incident cannot recur.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Root cause and eradication"],
    },
    {
        "id": "cism-inc-r2-028", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 3, "type": "mcq",
        "stem": "Which criterion BEST determines when a recovered system can be returned to production after "
                "an incident?",
        "options": [
            {"id": "A", "text": "It has been verified free of compromise, the exploited weakness is remediated, and it meets normal operating baselines, with business-owner sign-off"},
            {"id": "B", "text": "Enough time has simply passed since the incident"},
            {"id": "C", "text": "The team is tired and wants to finish"},
            {"id": "D", "text": "The system is able to power on"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A system should return to production only once it is validated clean, the weakness is "
                       "fixed, it performs to baseline, and the business owner accepts it - verification, not "
                       "time or convenience, is the criterion.",
            "distractors": {
                "B": "Elapsed time proves nothing about whether the system is clean.",
                "C": "Team fatigue is not a security criterion.",
                "D": "Powering on does not mean the system is free of compromise.",
            },
            "exam_pattern": "Return to production only after verified-clean + remediated + baseline + owner sign-off.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Return-to-production criteria"],
    },
    {
        "id": "cism-inc-r2-029", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The documented record proving who handled a piece of evidence, when, "
                "and how it was protected from tampering is the chain of _____. (one word)",
        "correct": ["custody"],
        "explanation": {
            "correct": "The chain of custody documents everyone who handled evidence and how it was "
                       "safeguarded, so its integrity can be demonstrated and it remains admissible.",
            "exam_pattern": "Chain of custody = documented handling record that keeps evidence admissible.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Chain of custody"],
    },

    # ----- cism_post_incident_review -----------------------------------
    {
        "id": "cism-inc-r2-030", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 3, "type": "multi",
        "stem": "Which TWO metrics BEST help evaluate and improve incident response effectiveness over "
                "time? (Choose two.)",
        "options": [
            {"id": "A", "text": "Mean time to detect (MTTD)"},
            {"id": "B", "text": "Mean time to respond/recover (MTTR)"},
            {"id": "C", "text": "The number of motivational posters displayed in the office"},
            {"id": "D", "text": "The size of the marketing team"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "MTTD and MTTR measure how quickly incidents are detected and handled; tracking them "
                       "over time shows whether the response capability is improving.",
            "distractors": {
                "C": "Poster counts have no relationship to response effectiveness.",
                "D": "Marketing headcount is unrelated to incident response.",
            },
            "exam_pattern": "Measure IR effectiveness with MTTD and MTTR (and dwell time), not activity trivia.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident response metrics"],
    },
    {
        "id": "cism-inc-r2-031", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "mcq",
        "stem": "When should a post-incident review BEST be conducted?",
        "options": [
            {"id": "A", "text": "Promptly after the incident is resolved and closed, while details are still fresh"},
            {"id": "B", "text": "Several years after the incident"},
            {"id": "C", "text": "Never, to avoid dwelling on problems"},
            {"id": "D", "text": "Only if the exact same incident happens a second time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A review conducted soon after closure captures accurate details and timely lessons "
                       "while participants still remember events clearly.",
            "distractors": {
                "B": "Waiting years lets crucial details and context fade.",
                "C": "Skipping the review wastes the chance to improve.",
                "D": "Waiting for a recurrence forgoes the lesson the first incident offered.",
            },
            "exam_pattern": "Do the post-incident review promptly after closure, while details are fresh.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Timing of the post-incident review"],
    },
    {
        "id": "cism-inc-r2-032", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "mcq",
        "stem": "To get the most value from a post-incident (lessons-learned) review, who should "
                "participate?",
        "options": [
            {"id": "A", "text": "All stakeholders involved in the response - security, IT, affected business units, legal, and communications"},
            {"id": "B", "text": "Only the information security manager"},
            {"id": "C", "text": "Only people from outside the organization"},
            {"id": "D", "text": "No one - the review should be skipped"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cross-functional review that includes everyone involved surfaces the full picture - "
                       "technical, business, legal, and communication perspectives - and produces better, "
                       "actionable improvements.",
            "distractors": {
                "B": "A single viewpoint misses most of the lessons.",
                "C": "Outsiders alone lack the internal context needed.",
                "D": "Skipping the review forfeits improvement.",
            },
            "exam_pattern": "Make the lessons-learned review cross-functional - include all who were involved.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Participants in lessons learned"],
    },
    {
        "id": "cism-inc-r2-033", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 3, "type": "mcq",
        "stem": "A post-incident review finds the root cause was an unpatched, known vulnerability. Beyond "
                "patching that one system, what is the BEST systemic action?",
        "options": [
            {"id": "A", "text": "Strengthen the vulnerability and patch-management process and update the risk register to prevent the whole class of issue"},
            {"id": "B", "text": "Patch only the single affected server and consider the matter closed"},
            {"id": "C", "text": "Remove patch management from the program's scope"},
            {"id": "D", "text": "Blame the individual server owner and move on"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Lessons learned should drive systemic improvement: fixing the patch-management process "
                       "(and updating the risk register) prevents the entire class of similar incidents, not "
                       "just this instance.",
            "distractors": {
                "B": "Patching one server leaves the systemic weakness - and other vulnerable systems - in place.",
                "C": "Removing patch management worsens the exposure.",
                "D": "Blame does not fix the process that allowed the gap.",
            },
            "exam_pattern": "Feed lessons into systemic process/control and risk-register improvements, not just a one-off fix.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Systemic improvement from lessons learned"],
    },
    {
        "id": "cism-inc-r2-034", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 3, "type": "mcq",
        "stem": "Which exercise BEST validates that the team can actually recover systems and execute the "
                "plan, beyond merely discussing it?",
        "options": [
            {"id": "A", "text": "A functional/simulation or full-scale operational exercise"},
            {"id": "B", "text": "A tabletop (discussion-based) exercise alone"},
            {"id": "C", "text": "Reading the plan silently"},
            {"id": "D", "text": "Deleting the plan and starting over"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Functional/simulation and full-scale exercises actually execute recovery steps, "
                       "proving the team and systems can perform - something a discussion cannot demonstrate.",
            "distractors": {
                "B": "A tabletop validates understanding and decisions, not actual recovery execution.",
                "C": "Reading the plan validates nothing operationally.",
                "D": "Deleting the plan destroys readiness rather than testing it.",
            },
            "exam_pattern": "To prove real recovery, run functional/full-scale exercises; tabletops test discussion only.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Exercise types and plan validation"],
    },
    {
        "id": "cism-inc-r2-035", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "mcq",
        "stem": "How often should incident response and business continuity plans be reviewed and updated?",
        "options": [
            {"id": "A", "text": "Periodically (e.g., at least annually) and after significant changes, tests, or actual incidents"},
            {"id": "B", "text": "Once, when first written, and then never again"},
            {"id": "C", "text": "Only when an auditor explicitly demands it"},
            {"id": "D", "text": "Only after the organization goes out of business"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Plans must be living documents: review them on a regular cadence and whenever the "
                       "organization, systems, or threats change significantly, and after tests and incidents "
                       "reveal gaps.",
            "distractors": {
                "B": "A write-once plan quickly becomes outdated and ineffective.",
                "C": "Waiting for the auditor is reactive and leaves stale plans in place.",
                "D": "Updating after the organization closes is meaningless.",
            },
            "exam_pattern": "Keep IR/BC plans current via periodic review plus review after change, tests, and incidents.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Plan maintenance and review"],
    },
    {
        "id": "cism-inc-r2-036", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Analysis performed after an incident to identify the underlying reason "
                "it occurred, so the problem can be prevented in future, is called _____ cause analysis. "
                "(one word)",
        "correct": ["root"],
        "explanation": {
            "correct": "Root cause analysis determines why an incident happened (the underlying cause, not "
                       "just symptoms) so corrective actions can prevent recurrence.",
            "exam_pattern": "Root cause analysis finds the underlying cause to prevent recurrence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Root cause analysis"],
    },
]
