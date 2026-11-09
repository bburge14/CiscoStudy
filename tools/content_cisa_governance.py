"""ISACA CISA pool - Domain 2: Governance and Management of IT.

Original, objective-aligned practice items for the five Domain 2 subtopics
tracked in the study engine:
  * cisa_it_governance      - IT governance frameworks (COBIT), the objective
                              of IT governance, board/executive accountability,
                              governance focus areas.
  * cisa_it_strategy_policies - IT strategy committee vs. IT steering committee,
                              the policy/standard/procedure/guideline hierarchy.
  * cisa_org_structure      - segregation of duties, compensating controls,
                              data owner vs. custodian responsibilities.
  * cisa_risk_management     - risk response options (accept/mitigate/transfer/
                              avoid), residual risk, risk-assessment steps, risk
                              appetite ownership.
  * cisa_bcp                 - business impact analysis, RTO/RPO, outsourcing and
                              SLA governance.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's governance-assurance mindset. All items are ORIGINAL and aligned to
public exam objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cisa_it_governance ===============================================
    {
        "id": "cisa-gov-001", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 1, "type": "mcq",
        "stem": "An IS auditor needs a widely accepted framework for assessing the governance and "
                "management of enterprise IT. Which framework is MOST appropriate?",
        "options": [
            {"id": "A", "text": "ITIL"},
            {"id": "B", "text": "COBIT"},
            {"id": "C", "text": "TOGAF"},
            {"id": "D", "text": "PRINCE2"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "COBIT is ISACA's framework for the governance and management of enterprise IT and is "
                       "the standard reference for evaluating IT governance.",
            "distractors": {
                "A": "ITIL is a framework for IT service management, not overall IT governance.",
                "C": "TOGAF is an enterprise architecture framework.",
                "D": "PRINCE2 is a project management methodology.",
            },
            "exam_pattern": "Governance of enterprise IT = COBIT; service mgmt = ITIL; architecture = TOGAF; projects = PRINCE2/PMBOK.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT governance frameworks (COBIT)"],
    },
    {
        "id": "cisa-gov-002", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY objective of IT governance?",
        "options": [
            {"id": "A", "text": "To ensure IT investments and activities are aligned with, and deliver value to, business objectives"},
            {"id": "B", "text": "To maximize the number of IT projects completed each year"},
            {"id": "C", "text": "To ensure the IT department operates independently of the business"},
            {"id": "D", "text": "To eliminate all IT-related risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IT governance exists to align IT with the organization's strategy and objectives so that "
                       "IT delivers value and manages risk in support of the business.",
            "distractors": {
                "B": "The volume of projects is not the goal; alignment and value delivery are.",
                "C": "IT should be integrated with the business, not isolated from it.",
                "D": "Risk is managed to an acceptable level, never fully eliminated.",
            },
            "exam_pattern": "IT governance = align IT with business strategy and deliver value (not volume, isolation, or zero risk).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Purpose of IT governance"],
    },
    {
        "id": "cisa-gov-003", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 2, "type": "mcq",
        "stem": "Who holds ultimate responsibility for IT governance in an organization?",
        "options": [
            {"id": "A", "text": "The IT help desk manager"},
            {"id": "B", "text": "The external IS auditor"},
            {"id": "C", "text": "The board of directors and senior management"},
            {"id": "D", "text": "Individual system administrators"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "IT governance is the responsibility of the board of directors and senior/executive "
                       "management, as an integral part of enterprise governance.",
            "distractors": {
                "A": "The help desk manager handles operations, not governance accountability.",
                "B": "The external auditor provides assurance but is not accountable for governance.",
                "D": "Administrators operate systems; they do not own governance.",
            },
            "exam_pattern": "Governance accountability sits with the board and executive management - the top, not operations or audit.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Governance roles and responsibilities"],
    },
    {
        "id": "cisa-gov-004", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 3, "type": "multi",
        "stem": "Which TWO are recognized focus areas (outcomes) of effective IT governance? (Choose two.)",
        "options": [
            {"id": "A", "text": "Strategic alignment of IT with business goals"},
            {"id": "B", "text": "Writing the application source code for each project"},
            {"id": "C", "text": "Staffing the overnight computer-operations shift"},
            {"id": "D", "text": "Value delivery and benefits realization from IT"},
        ],
        "correct": ["A", "D"],
        "explanation": {
            "correct": "Strategic alignment and value delivery are two of the core IT governance focus areas, "
                       "alongside risk management, resource management, and performance measurement.",
            "distractors": {
                "B": "Writing source code is a development activity, not a governance focus area.",
                "C": "Staffing an operations shift is an operational task, not a governance outcome.",
            },
            "exam_pattern": "IT governance focus areas = strategic alignment, value delivery, risk mgmt, resource mgmt, performance measurement.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT governance focus areas"],
    },

    # ===== cisa_it_strategy_policies ========================================
    {
        "id": "cisa-gov-005", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "Which body is responsible for prioritizing IT projects, allocating resources, and "
                "monitoring project progress at the executive/management level?",
        "options": [
            {"id": "A", "text": "The IT strategy committee"},
            {"id": "B", "text": "The external audit firm"},
            {"id": "C", "text": "The IT steering committee"},
            {"id": "D", "text": "The service desk"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The IT steering committee operates at the executive/management level and is responsible "
                       "for prioritizing projects, allocating resources, and overseeing delivery.",
            "distractors": {
                "A": "The IT strategy committee operates at board level, advising on strategic direction, not day-to-day project prioritization.",
                "B": "The external audit firm provides assurance, not project oversight.",
                "D": "The service desk handles user support, not project prioritization.",
            },
            "exam_pattern": "Steering committee = executive-level project prioritization/oversight; strategy committee = board-level direction.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT strategy and steering committees"],
    },
    {
        "id": "cisa-gov-006", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "At what organizational level does an IT strategy committee typically operate?",
        "options": [
            {"id": "A", "text": "At the operational / service-desk level"},
            {"id": "B", "text": "At the board level, advising on IT strategic direction"},
            {"id": "C", "text": "At the vendor's level, outside the organization"},
            {"id": "D", "text": "At the individual project-team level"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An IT strategy committee operates at the board level, advising the board on IT strategic "
                       "direction and its alignment with enterprise strategy.",
            "distractors": {
                "A": "Operational support is handled below the strategy committee's level.",
                "C": "The committee is part of the organization's own governance, not the vendor's.",
                "D": "Project teams execute work; they do not set board-level strategy.",
            },
            "exam_pattern": "Strategy committee = board level (direction); steering committee = executive level (execution).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT strategy committee"],
    },
    {
        "id": "cisa-gov-007", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "In the hierarchy of security documents, which one expresses high-level management intent "
                "and serves as the foundation for standards and procedures?",
        "options": [
            {"id": "A", "text": "Policy"},
            {"id": "B", "text": "Procedure"},
            {"id": "C", "text": "Guideline"},
            {"id": "D", "text": "Work instruction"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A policy is the high-level statement of management intent and direction, approved by "
                       "senior management; standards, procedures, and guidelines are derived from it.",
            "distractors": {
                "B": "A procedure gives detailed step-by-step instructions that implement a policy.",
                "C": "A guideline is a recommended, non-mandatory practice.",
                "D": "A work instruction is an even more granular task-level detail, not high-level intent.",
            },
            "exam_pattern": "Policy (intent) -> Standard (mandatory rule) -> Procedure (steps) -> Guideline (recommended).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Policies, standards, and procedures"],
    },

    # ===== cisa_org_structure ===============================================
    {
        "id": "cisa-gov-008", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 2, "type": "mcq",
        "stem": "During an audit, the IS auditor finds that an application developer also has update "
                "access to the production environment. This is MOST likely a violation of:",
        "options": [
            {"id": "A", "text": "Data classification requirements"},
            {"id": "B", "text": "The principle of least privilege only"},
            {"id": "C", "text": "Capacity management"},
            {"id": "D", "text": "Segregation of duties"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A developer with update access to production can introduce and promote unauthorized or "
                       "untested code, which breaks the segregation of duties between development and production.",
            "distractors": {
                "A": "Data classification concerns labeling sensitivity, not this access conflict.",
                "B": "Least privilege is related, but the specific control broken here is segregation of development and production duties.",
                "C": "Capacity management concerns resource sufficiency, not conflicting access.",
            },
            "exam_pattern": "Developer + production update access = classic segregation-of-duties violation.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Segregation of duties"],
    },
    {
        "id": "cisa-gov-009", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 3, "type": "mcq",
        "stem": "In a small IT department, full segregation of duties is not practical. Which is the BEST "
                "compensating control?",
        "options": [
            {"id": "A", "text": "Hiring additional internal auditors"},
            {"id": "B", "text": "Increased management supervision and independent review of activity logs"},
            {"id": "C", "text": "Removing all logging to simplify operations"},
            {"id": "D", "text": "Giving every employee administrator rights for flexibility"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "When duties cannot be fully segregated, stronger management supervision together with "
                       "independent review of detailed activity logs is the recognized compensating control.",
            "distractors": {
                "A": "Adding auditors does not compensate for day-to-day control gaps in operations.",
                "C": "Removing logging destroys the evidence needed to detect problems.",
                "D": "Broad admin rights worsen the control weakness rather than compensate for it.",
            },
            "exam_pattern": "When SoD is impractical, compensate with supervision + independent log review.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Compensating controls"],
    },
    {
        "id": "cisa-gov-010", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 2, "type": "mcq",
        "stem": "Who is PRIMARILY responsible for classifying data and authorizing which users may access it?",
        "options": [
            {"id": "A", "text": "The database administrator"},
            {"id": "B", "text": "The network engineer"},
            {"id": "C", "text": "The data owner"},
            {"id": "D", "text": "The end user"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The data owner (usually a senior business manager) is accountable for classifying the "
                       "data and authorizing access; the custodian (e.g., IT) implements and maintains the controls.",
            "distractors": {
                "A": "The DBA is a custodian who maintains the data per the owner's direction, not the classifier.",
                "B": "The network engineer supports infrastructure, not data classification.",
                "D": "End users consume data within the access the owner authorizes.",
            },
            "exam_pattern": "Owner classifies and authorizes access; custodian safeguards/maintains; user operates within granted rights.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Data owner and custodian roles"],
    },

    # ===== cisa_risk_management =============================================
    {
        "id": "cisa-gov-011", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 1, "type": "mcq",
        "stem": "An organization purchases cyber insurance to cover potential losses from a data breach. "
                "Which risk response does this represent?",
        "options": [
            {"id": "A", "text": "Risk transfer (sharing)"},
            {"id": "B", "text": "Risk avoidance"},
            {"id": "C", "text": "Risk acceptance"},
            {"id": "D", "text": "Risk elimination"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Buying insurance shifts the financial impact of the risk to a third party, which is risk "
                       "transfer (sharing).",
            "distractors": {
                "B": "Avoidance means not undertaking the risky activity at all.",
                "C": "Acceptance means retaining the risk without a countermeasure.",
                "D": "Risk cannot be fully eliminated; some residual risk always remains.",
            },
            "exam_pattern": "Insurance = transfer/share; stop the activity = avoid; do nothing = accept; reduce = mitigate.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Risk response options"],
    },
    {
        "id": "cisa-gov-012", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The risk that remains after management has implemented controls and "
                "countermeasures is called ______ risk.",
        "correct": ["residual", "residual risk"],
        "explanation": {
            "correct": "Residual risk is what is left after controls are applied; management must decide whether "
                       "that residual risk is within the organization's risk appetite.",
            "distractors": {},
            "exam_pattern": "Inherent risk reduced by the effect of controls = residual risk.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Residual risk"],
    },
    {
        "id": "cisa-gov-013", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "When performing a risk assessment, which activity should be performed FIRST?",
        "options": [
            {"id": "A", "text": "Select and implement controls"},
            {"id": "B", "text": "Calculate the annual loss expectancy"},
            {"id": "C", "text": "Purchase insurance for the largest risks"},
            {"id": "D", "text": "Identify and determine the value of the information assets"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "You cannot assess risk to assets you have not identified; identifying and valuing the "
                       "information assets is the first step, before threats, likelihood, impact, and controls are considered.",
            "distractors": {
                "A": "Controls are selected later, after risks are identified and assessed.",
                "B": "Loss expectancy is computed after assets, threats, and impact are understood.",
                "C": "Insurance is a response chosen after the assessment, not first.",
            },
            "exam_pattern": "Risk assessment starts by identifying/valuing assets - you can't protect what you haven't identified.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Risk management process"],
    },
    {
        "id": "cisa-gov-014", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "Who should determine the level of risk that is acceptable for the organization (its risk "
                "appetite)?",
        "options": [
            {"id": "A", "text": "The IS auditor"},
            {"id": "B", "text": "Senior management and the business owners"},
            {"id": "C", "text": "The firewall administrator"},
            {"id": "D", "text": "The software vendor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Setting risk appetite and accepting risk is a business decision owned by senior "
                       "management and the business owners, not by IT staff or the auditor.",
            "distractors": {
                "A": "The auditor evaluates and reports on risk but does not set the organization's risk appetite.",
                "C": "The firewall administrator implements technical controls, not risk appetite.",
                "D": "The vendor supplies products; it does not set the customer's risk tolerance.",
            },
            "exam_pattern": "Risk appetite and risk acceptance are senior-management business decisions.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Risk appetite and ownership"],
    },

    # ===== cisa_bcp =========================================================
    {
        "id": "cisa-gov-015", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a business impact analysis (BIA)?",
        "options": [
            {"id": "A", "text": "To select the vendor for the recovery site"},
            {"id": "B", "text": "To test the disaster recovery plan"},
            {"id": "C", "text": "To identify critical processes and the impact of their disruption, and to set recovery priorities and objectives"},
            {"id": "D", "text": "To encrypt the backup media"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A BIA identifies critical business processes, assesses the impact of their disruption "
                       "over time, and establishes recovery priorities and objectives (such as RTO and RPO) that "
                       "drive the continuity and recovery strategy.",
            "distractors": {
                "A": "Site selection is a later strategy decision informed by the BIA, not its purpose.",
                "B": "Testing the plan comes after the plan is built from the BIA.",
                "D": "Encrypting media is an operational control, not the purpose of a BIA.",
            },
            "exam_pattern": "BIA = identify critical processes + impact of disruption -> recovery priorities, RTO/RPO.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Business impact analysis (BIA)"],
    },
    {
        "id": "cisa-gov-016", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The maximum acceptable length of time to restore a business process "
                "after a disruption is known as the recovery ______ objective.",
        "correct": ["time", "recovery time objective", "rto"],
        "explanation": {
            "correct": "The recovery time objective (RTO) is the target maximum time to restore a process or "
                       "system after a disruption; it drives the choice of recovery strategy and site.",
            "distractors": {},
            "exam_pattern": "RTO = how fast you must be back (time); RPO = how much data you can afford to lose (data).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — RTO and RPO"],
    },
    {
        "id": "cisa-gov-017", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 3, "type": "mcq",
        "stem": "A critical transaction system is assigned a recovery point objective (RPO) of nearly "
                "zero. What does this imply?",
        "options": [
            {"id": "A", "text": "The organization can tolerate almost no data loss, so near-continuous replication/mirroring is required"},
            {"id": "B", "text": "The system can be restored slowly over several days"},
            {"id": "C", "text": "Backups are no longer necessary"},
            {"id": "D", "text": "The system is not important to the business"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An RPO near zero means almost no data loss is acceptable, which requires near-real-time "
                       "data protection such as synchronous replication or mirroring.",
            "distractors": {
                "B": "A slow restore window describes a long recovery time objective (RTO), not an RPO near zero.",
                "C": "A near-zero RPO demands more frequent data protection, not less.",
                "D": "A near-zero RPO signals the system is highly critical, not unimportant.",
            },
            "exam_pattern": "Lower RPO = less tolerable data loss = more frequent/continuous replication.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — RTO and RPO"],
    },
    {
        "id": "cisa-gov-018", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 2, "type": "mcq",
        "stem": "An organization outsources its payroll processing to a third-party service provider. Who "
                "retains ultimate accountability for the risks associated with the outsourced process?",
        "options": [
            {"id": "A", "text": "The service provider alone"},
            {"id": "B", "text": "The regulator"},
            {"id": "C", "text": "No one, because the risk has been fully transferred"},
            {"id": "D", "text": "The organization that outsourced the process"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Outsourcing can transfer the activity, but accountability for the risk, data, and "
                       "compliance remains with the organization that owns the process - which is why strong SLA "
                       "and oversight controls are needed.",
            "distractors": {
                "A": "The provider is responsible for delivering the service, but the outsourcing organization stays accountable for the risk.",
                "B": "Regulators set requirements but do not assume the organization's accountability.",
                "C": "Accountability cannot be fully outsourced, even when the work is.",
            },
            "exam_pattern": "You can outsource the function, but not the accountability - govern it with SLAs and monitoring.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Outsourcing and SLA governance"],
    },
]
