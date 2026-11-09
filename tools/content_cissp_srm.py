"""(ISC)² CISSP pool - Domain 1: Security and Risk Management.

Original, CBK-aligned practice items for the six Security and Risk Management
subtopics tracked in the study engine:
  * cissp_cia_governance     - the CIA triad, due care vs due diligence, and the
                               security roles (data owner/custodian/subject).
  * cissp_compliance_legal   - legal systems, intellectual property (patent,
                               copyright, trademark, trade secret) and privacy
                               (GDPR controller vs processor).
  * cissp_risk_management     - quantitative risk (AV, EF, SLE, ARO, ALE), the
                               four risk-treatment strategies and residual risk.
  * cissp_security_policies   - the policy / standard / baseline / procedure /
                               guideline document hierarchy.
  * cissp_bcp_dr              - BIA, RTO/RPO/MTD/WRT and recovery-site types.
  * cissp_ethics_personnel    - the (ISC)² Code of Ethics canons and order, plus
                               personnel controls (separation of duties, etc.).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and scenario-driven, favor the "BEST /
FIRST" managerial, risk-based mindset CISSP rewards, and never reproduce real or
memorized exam questions.
"""

QUESTIONS = [
    # ===== cissp_cia_governance =============================================
    {
        "id": "cissp-srm-001", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_cia_governance", "difficulty": 2, "type": "mcq",
        "stem": "After identifying that unpatched servers pose a risk, a company implements a "
                "patch-management process and consistently follows it, acting as a reasonable and "
                "prudent organization would. This ongoing practice of taking responsible action to "
                "protect assets BEST describes which concept?",
        "options": [
            {"id": "A", "text": "Due diligence"},
            {"id": "B", "text": "Due care"},
            {"id": "C", "text": "Separation of duties"},
            {"id": "D", "text": "Defense in depth"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Due care is taking the reasonable, prudent actions a careful organization would "
                       "take to protect its assets - here, implementing and consistently following the "
                       "patch process (the 'prudent person' rule).",
            "distractors": {
                "A": "Due diligence is the research and ongoing investigation that identifies the risk and "
                     "informs the action; it is knowing what to do, not the act of doing it.",
                "C": "Separation of duties splits a task among people to deter fraud; it is not about "
                     "reasonable protective action generally.",
                "D": "Defense in depth is layering multiple controls, a design strategy, not the legal "
                     "concept of acting reasonably.",
            },
            "exam_pattern": "Due diligence = research/know what to do; due care = do it (the prudent action).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Security governance and due care/due diligence"],
    },
    {
        "id": "cissp-srm-002", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_cia_governance", "difficulty": 2, "type": "mcq",
        "stem": "A hospital must ensure clinicians can always retrieve patient records, even during "
                "hardware failures, so it deploys redundant servers and reliable backups. Which element "
                "of the CIA triad is the PRIMARY focus of these measures?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Availability ensures authorized users can access information and systems when "
                       "needed; redundancy and backups directly protect against downtime and loss of access.",
            "distractors": {
                "A": "Confidentiality prevents unauthorized disclosure, which redundancy does not address.",
                "B": "Integrity ensures data is accurate and unaltered, a different goal from guaranteeing access.",
                "D": "Non-repudiation prevents a party from denying an action and is not one of the three "
                     "CIA triad elements.",
            },
            "exam_pattern": "Redundancy, backups, and uptime map to availability.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - The CIA triad"],
    },
    {
        "id": "cissp-srm-003", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_cia_governance", "difficulty": 2, "type": "mcq",
        "stem": "In a data-governance program, who is ultimately accountable for assigning a data set's "
                "classification and defining who may access it, even though day-to-day protection is "
                "delegated to the IT operations team?",
        "options": [
            {"id": "A", "text": "Data owner"},
            {"id": "B", "text": "Data custodian"},
            {"id": "C", "text": "Data processor"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The data owner (typically a senior manager) is accountable for classifying the "
                       "data, defining acceptable use and access, and is ultimately responsible for its protection.",
            "distractors": {
                "B": "The data custodian implements and maintains the controls (backups, access settings) "
                     "but does not decide classification.",
                "C": "A data processor processes data on behalf of a controller (a GDPR role), not the "
                     "accountable classifier.",
                "D": "The data subject is the individual the personal data is about, not a governance owner.",
            },
            "exam_pattern": "Owner (senior management) classifies and is accountable; custodian implements protection.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Security roles and responsibilities"],
    },

    # ===== cissp_compliance_legal ===========================================
    {
        "id": "cissp-srm-004", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_compliance_legal", "difficulty": 2, "type": "mcq",
        "stem": "A software company wants to protect the proprietary algorithm inside its product "
                "indefinitely, without disclosing how it works. Which form of intellectual-property "
                "protection is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Patent"},
            {"id": "B", "text": "Copyright"},
            {"id": "C", "text": "Trademark"},
            {"id": "D", "text": "Trade secret"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A trade secret protects confidential business information that provides competitive "
                       "advantage and lasts as long as it is kept secret, with no public disclosure required.",
            "distractors": {
                "A": "A patent requires public disclosure of the invention and protection expires (about 20 years).",
                "B": "Copyright protects the expression of the code but not the underlying idea or algorithm, "
                     "and it carries a fixed term.",
                "C": "A trademark protects brand identifiers such as names and logos, not a secret algorithm.",
            },
            "exam_pattern": "Protect a secret formula/algorithm indefinitely with no disclosure = trade secret.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Intellectual property"],
    },
    {
        "id": "cissp-srm-005", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_compliance_legal", "difficulty": 2, "type": "mcq",
        "stem": "Under the GDPR, a retailer decides why and how customer personal data will be processed "
                "and hires a cloud analytics firm to carry out that processing on its behalf. Which role "
                "does the retailer hold?",
        "options": [
            {"id": "A", "text": "Data processor"},
            {"id": "B", "text": "Data controller"},
            {"id": "C", "text": "Data custodian"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Under the GDPR, the data controller determines the purposes and means of processing "
                       "personal data; the retailer deciding why and how makes it the controller.",
            "distractors": {
                "A": "The processor (the analytics firm) processes data on the controller's behalf and instructions.",
                "C": "Custodian is an operational data-protection role, not a defined GDPR legal role.",
                "D": "The data subject is the individual whose personal data is processed.",
            },
            "exam_pattern": "Controller decides purpose and means; processor acts only on the controller's instructions.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Privacy and GDPR roles"],
    },
    {
        "id": "cissp-srm-006", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_compliance_legal", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The category of intellectual property that protects a brand name, "
                "logo, or slogan used to distinguish an organization's goods or services in the "
                "marketplace is a ________.",
        "correct": ["trademark", "trade mark"],
        "explanation": {
            "correct": "A trademark protects words, symbols, logos, or slogans that identify and distinguish "
                       "the source of goods or services.",
            "exam_pattern": "Brand identifiers (name/logo/slogan) = trademark; inventions = patent; expression "
                            "of a work = copyright; secret business info = trade secret.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Intellectual property"],
    },

    # ===== cissp_risk_management ============================================
    {
        "id": "cissp-srm-007", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "An asset is valued at $200,000. A fire would destroy an estimated 50% of its value, and "
                "such a fire is expected once every 10 years. What is the annualized loss expectancy (ALE)?",
        "options": [
            {"id": "A", "text": "$10,000"},
            {"id": "B", "text": "$100,000"},
            {"id": "C", "text": "$20,000"},
            {"id": "D", "text": "$1,000"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SLE = AV × EF = $200,000 × 0.50 = $100,000. ARO = once per 10 years = 0.1. "
                       "ALE = SLE × ARO = $100,000 × 0.1 = $10,000.",
            "distractors": {
                "B": "$100,000 is the single loss expectancy (SLE), the loss from one event, not annualized.",
                "C": "$20,000 would require an ARO of 0.2 (once every 5 years), not once every 10 years.",
                "D": "$1,000 applies an incorrect ARO of 0.01 (once every 100 years).",
            },
            "exam_pattern": "SLE = AV × EF; ALE = SLE × ARO. Annualize the single loss by the yearly rate.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Quantitative risk analysis"],
    },
    {
        "id": "cissp-srm-008", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After analysis, an organization decides the potential financial loss from a specific "
                "cyber event is too large to absorb, so it purchases a cyber-insurance policy to cover "
                "that loss. Which risk-treatment strategy is this?",
        "options": [
            {"id": "A", "text": "Risk avoidance"},
            {"id": "B", "text": "Risk mitigation"},
            {"id": "C", "text": "Risk transfer"},
            {"id": "D", "text": "Risk acceptance"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Risk transfer (sharing) shifts the financial impact of a risk to a third party, for "
                       "example by buying insurance; the organization still owns the risk but offloads the loss.",
            "distractors": {
                "A": "Avoidance eliminates the risk by not engaging in the risky activity at all.",
                "B": "Mitigation reduces the likelihood or impact with controls, not by insuring the loss.",
                "D": "Acceptance means absorbing the risk with no additional action or insurance.",
            },
            "exam_pattern": "Insurance or outsourcing the financial impact to a third party = risk transfer (sharing).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Risk treatment strategies"],
    },
    {
        "id": "cissp-srm-009", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_risk_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The risk that remains after security controls and safeguards have "
                "been applied, and which senior management must formally accept, is known as ________ risk.",
        "correct": ["residual"],
        "explanation": {
            "correct": "Residual risk is the portion of risk left over after controls reduce the total risk; "
                       "management formally accepts it as the cost of doing business.",
            "exam_pattern": "Residual risk = risk remaining after controls; it is accepted by management, not "
                            "eliminated.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Residual risk"],
    },

    # ===== cissp_security_policies ==========================================
    {
        "id": "cissp-srm-010", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_security_policies", "difficulty": 2, "type": "mcq",
        "stem": "An organization's governance documents include a broad management statement of intent, "
                "mandatory specific rules, and optional recommendations. Which document type is MANDATORY "
                "and specifies, for example, that AES-256 must be used to encrypt data at rest?",
        "options": [
            {"id": "A", "text": "Policy"},
            {"id": "B", "text": "Standard"},
            {"id": "C", "text": "Guideline"},
            {"id": "D", "text": "Procedure"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A standard is a mandatory document that specifies the required technologies, "
                       "configurations, or methods (such as AES-256) to support the broader policy.",
            "distractors": {
                "A": "A policy is the high-level, broad statement of management intent, not the specific "
                     "mandatory control.",
                "C": "A guideline is a recommended, discretionary practice, not mandatory.",
                "D": "A procedure is a step-by-step instruction for performing a task, not a control requirement.",
            },
            "exam_pattern": "Policy = high-level intent; Standard = mandatory specifics; Procedure = steps; "
                            "Guideline = optional advice.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Policy document hierarchy"],
    },
    {
        "id": "cissp-srm-011", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_security_policies", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to define the minimum mandatory level of security configuration that "
                "every corporate workstation must meet. Which type of document establishes this uniform "
                "minimum?",
        "options": [
            {"id": "A", "text": "Guideline"},
            {"id": "B", "text": "Policy"},
            {"id": "C", "text": "Procedure"},
            {"id": "D", "text": "Baseline"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A baseline defines the minimum mandatory level of security (a uniform configuration) "
                       "that all systems of a given type must meet.",
            "distractors": {
                "A": "A guideline is discretionary advice, not a mandatory minimum.",
                "B": "A policy states high-level intent, not a specific configuration minimum.",
                "C": "A procedure lists the steps to accomplish a task, not the required end state.",
            },
            "exam_pattern": "Baseline = mandatory minimum / uniform security configuration level.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Baselines"],
    },
    {
        "id": "cissp-srm-012", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_security_policies", "difficulty": 2, "type": "mcq",
        "stem": "A board directs that information security be formally governed. What should the security "
                "team obtain FIRST, before developing standards, procedures, and baselines?",
        "options": [
            {"id": "A", "text": "A high-level security policy endorsed by senior management"},
            {"id": "B", "text": "A completed penetration test of all systems"},
            {"id": "C", "text": "A fully deployed SIEM platform"},
            {"id": "D", "text": "A detailed incident-response runbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The security policy, endorsed by senior management, establishes authority and "
                       "direction; standards, procedures, and baselines derive from it, so it comes first.",
            "distractors": {
                "B": "A penetration test is an operational assessment that should be justified by, and follow, "
                     "the governing policy.",
                "C": "Deploying a SIEM is a technical control that should be driven by policy and requirements, "
                     "not precede them.",
                "D": "An incident-response runbook is a downstream procedure built under the policy's authority.",
            },
            "exam_pattern": "Management-approved policy comes first; standards, procedures, and baselines flow from it.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Security policy framework"],
    },

    # ===== cissp_bcp_dr =====================================================
    {
        "id": "cissp-srm-013", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "An organization is starting its business continuity program. Which activity should be "
                "performed FIRST to identify critical business functions and the impact of their disruption?",
        "options": [
            {"id": "A", "text": "Selecting and contracting a hot site"},
            {"id": "B", "text": "Writing the disaster-recovery runbook"},
            {"id": "C", "text": "Conducting a business impact analysis (BIA)"},
            {"id": "D", "text": "Purchasing business-interruption insurance"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The business impact analysis (BIA) identifies critical functions and quantifies the "
                       "impact of disruption (MTD, RTO, RPO); its findings drive every later BCP/DRP decision.",
            "distractors": {
                "A": "Choosing a recovery site is premature until the BIA defines which functions are critical "
                     "and their recovery objectives.",
                "B": "Writing recovery procedures should follow, and be shaped by, the BIA's results.",
                "D": "Buying insurance is a risk-transfer decision that should be informed by the BIA's impact figures.",
            },
            "exam_pattern": "BIA first - it identifies critical functions, MTD, and RTO/RPO that drive all later planning.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Business impact analysis"],
    },
    {
        "id": "cissp-srm-014", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "After an outage, management states the business can tolerate losing at most 15 minutes "
                "of transaction data. Which recovery metric does this 15-minute limit define?",
        "options": [
            {"id": "A", "text": "Recovery time objective (RTO)"},
            {"id": "B", "text": "Recovery point objective (RPO)"},
            {"id": "C", "text": "Maximum tolerable downtime (MTD)"},
            {"id": "D", "text": "Work recovery time (WRT)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The recovery point objective (RPO) is the maximum acceptable amount of data loss, "
                       "measured as a point in time (here, 15 minutes of data), which sets backup frequency.",
            "distractors": {
                "A": "RTO is the target time to restore a service after disruption, not the amount of data loss.",
                "C": "MTD is the total time a function can be unavailable before unacceptable harm occurs.",
                "D": "WRT is the time to validate systems and resume normal work after systems are restored.",
            },
            "exam_pattern": "RPO = acceptable data loss (time); RTO = time to restore service; MTD = RTO + WRT.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Recovery metrics (RTO/RPO/MTD/WRT)"],
    },
    {
        "id": "cissp-srm-015", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "An organization needs a recovery facility that is fully equipped with hardware and "
                "near-real-time data replication so operations can resume within minutes to a few hours. "
                "Which recovery-site type fits BEST?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Reciprocal (mutual-aid) agreement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hot site is fully equipped and kept current with data, enabling the fastest "
                       "recovery (minutes to hours), at the highest cost.",
            "distractors": {
                "B": "A warm site has hardware but not live/current data, so recovery takes hours to days.",
                "C": "A cold site is only space with power and HVAC, no hardware, taking days to weeks.",
                "D": "A reciprocal agreement relies on another organization's spare capacity and is informal "
                     "and uncertain.",
            },
            "exam_pattern": "Fully equipped + current data + fastest recovery = hot site (most expensive).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Recovery site strategies"],
    },

    # ===== cissp_ethics_personnel ===========================================
    {
        "id": "cissp-srm-016", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_ethics_personnel", "difficulty": 3, "type": "mcq",
        "stem": "A CISSP faces a situation where honoring a client's confidential request would require "
                "concealing information that endangers public safety. According to the (ISC)² Code of "
                "Ethics, how should this conflict be resolved?",
        "options": [
            {"id": "A", "text": "Favor the client, since duty to the principal always comes first"},
            {"id": "B", "text": "Treat the four canons as equal in weight and decide arbitrarily"},
            {"id": "C", "text": "Resign immediately to avoid making any decision"},
            {"id": "D", "text": "Give precedence to protecting society (Canon I) over service to principals (Canon III)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The canons are applied in order of priority. Canon I (protect society, the common "
                       "good, and the infrastructure) outranks Canon III (provide diligent, competent "
                       "service to principals), so public safety takes precedence.",
            "distractors": {
                "A": "This reverses the priority; service to principals (Canon III) is subordinate to "
                     "protecting society (Canon I).",
                "B": "The canons are ranked, not equal; conflicts are resolved by the order of the canons.",
                "C": "Resigning avoids the ethical duty to act and is not what the order of canons requires.",
            },
            "exam_pattern": "Canon order: I protect society > II act honorably > III service to principals > "
                            "IV advance the profession.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - (ISC)² Code of Ethics canons"],
    },
    {
        "id": "cissp-srm-017", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_ethics_personnel", "difficulty": 2, "type": "mcq",
        "stem": "To ensure no single employee can both initiate and approve a payment, a company splits "
                "these two tasks between two different people. Which principle is being applied?",
        "options": [
            {"id": "A", "text": "Separation of duties"},
            {"id": "B", "text": "Job rotation"},
            {"id": "C", "text": "Least privilege"},
            {"id": "D", "text": "Mandatory vacation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Separation (segregation) of duties divides a sensitive process so no one person can "
                       "complete it alone, deterring fraud because abuse would require collusion.",
            "distractors": {
                "B": "Job rotation moves staff between roles over time to detect fraud and cross-train; it "
                     "does not split a single transaction.",
                "C": "Least privilege grants only the access needed for a role, a different (access-scope) control.",
                "D": "Mandatory vacation forces absence to surface concealed activity; it does not split the task.",
            },
            "exam_pattern": "Splitting a critical task so one person cannot complete it alone = separation of duties.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Personnel security controls"],
    },
    {
        "id": "cissp-srm-018", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_ethics_personnel", "difficulty": 2, "type": "mcq",
        "stem": "A bank requires employees in sensitive financial roles to take at least one continuous "
                "week of vacation each year, during which another employee performs their duties. What is "
                "the PRIMARY security purpose of this policy?",
        "options": [
            {"id": "A", "text": "To reduce employee burnout and improve morale"},
            {"id": "B", "text": "To detect fraud or irregularities an employee must be present to conceal"},
            {"id": "C", "text": "To comply with labor-law vacation requirements"},
            {"id": "D", "text": "To cross-train backup personnel for redundancy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mandatory vacation is a detective control: forcing a continuous absence lets someone "
                       "else perform the duties and can surface ongoing schemes (such as embezzlement) that "
                       "depend on the person being present to hide them.",
            "distractors": {
                "A": "Reduced burnout is a benefit but not the primary security rationale.",
                "C": "Legal compliance may be a factor but is not the security purpose of the control.",
                "D": "Cross-training redundancy is a side benefit, not the detective-control objective.",
            },
            "exam_pattern": "Mandatory vacation is a detective control - fraud needing constant concealment "
                            "surfaces during forced absence.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Personnel security controls"],
    },
]
