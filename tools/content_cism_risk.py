"""ISACA CISM pool - Domain 2: Information Security Risk Management.

Original, objective-aligned practice items for the four risk subtopics tracked
in the study engine:
  * cism_risk_assessment     - the risk management lifecycle, asset identification
                               and valuation, threats vs vulnerabilities, likelihood
                               x impact, and letting risk results drive controls.
  * cism_risk_response       - the four treatment options (accept, mitigate,
                               transfer/share, avoid), risk appetite/tolerance,
                               cost-benefit proportionality, and who accepts risk.
  * cism_risk_monitoring     - key risk indicators (KRIs), the risk register,
                               continuous monitoring, and reassessing when exposure
                               changes.
  * cism_asset_classification - why and how assets are classified, ownership, and
                               how classification drives commensurate controls.

Authoring rules match the other content_*.py pools: the build step shuffles
option order (seeded by id), so keys are not positionally biased, every wrong
option carries a distractor note, and each item names the public ISACA objective
area it draws on.

CISM is a MANAGEMENT exam: keyed answers reflect the information security
manager's view - risk-based decisions, management (not the security team) owning
and accepting risk, and controls proportionate to the value of what they protect.
These are original items built from public CISM objectives; they are never real
or memorised exam questions.
"""

QUESTIONS = [
    # ===== cism_risk_assessment =============================================
    {
        "id": "cism-risk-001", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 1, "type": "multi",
        "stem": "When assessing an information security risk, which TWO factors are combined to determine "
                "the risk's level? (Choose two.)",
        "options": [
            {"id": "A", "text": "The likelihood that the event will occur"},
            {"id": "B", "text": "The impact (consequence) if it occurs"},
            {"id": "C", "text": "The brand name of the affected vendor"},
            {"id": "D", "text": "The number of employees in the IT department"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Risk level is a function of likelihood multiplied by impact - how probable the "
                       "event is and how severe its consequences would be.",
            "distractors": {
                "C": "A vendor's brand is irrelevant to the inherent level of a risk.",
                "D": "IT headcount does not determine a risk's likelihood or impact.",
            },
            "exam_pattern": "Risk level = likelihood x impact (probability and consequence).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk = likelihood x impact"],
    },
    {
        "id": "cism-risk-002", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "An information security manager is beginning a risk assessment. What should be identified "
                "and valued FIRST?",
        "options": [
            {"id": "A", "text": "The firewall rule base"},
            {"id": "B", "text": "The incident response team roster"},
            {"id": "C", "text": "The marketing budget"},
            {"id": "D", "text": "The organization's information assets"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "You cannot assess risk to something you have not identified and valued, so asset "
                       "identification and valuation come first and establish what is worth protecting.",
            "distractors": {
                "A": "A firewall rule base is a control detail examined later, not the starting point.",
                "B": "The incident response roster is unrelated to establishing what is at risk.",
                "C": "The marketing budget is irrelevant to valuing information assets.",
            },
            "exam_pattern": "First identify and value the assets - risk assessment starts from what needs protecting.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Asset identification and valuation"],
    },
    {
        "id": "cism-risk-003", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "An unpatched flaw in a public web application could allow data theft. In risk "
                "terminology, the unpatched flaw itself is BEST described as a:",
        "options": [
            {"id": "A", "text": "Threat"},
            {"id": "B", "text": "Risk response"},
            {"id": "C", "text": "Vulnerability"},
            {"id": "D", "text": "Control"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A vulnerability is a weakness that a threat could exploit; an unpatched flaw is "
                       "exactly such a weakness.",
            "distractors": {
                "A": "A threat is the potential cause or actor (for example, an attacker) that exploits the weakness, not the weakness itself.",
                "B": "A risk response is the chosen treatment of a risk, not the weakness.",
                "D": "A control reduces risk; it is not the weakness being described.",
            },
            "exam_pattern": "Vulnerability = weakness; threat = potential cause that exploits it; risk = likelihood/impact of that exploitation.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Threats and vulnerabilities"],
    },
    {
        "id": "cism-risk-004", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 2, "type": "mcq",
        "stem": "What should PRIMARILY drive the selection and prioritization of security controls?",
        "options": [
            {"id": "A", "text": "The results of the risk assessment"},
            {"id": "B", "text": "The newest products offered by security vendors"},
            {"id": "C", "text": "The personal preference of the CISO"},
            {"id": "D", "text": "The controls a competitor has deployed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Controls should be chosen on a risk basis: the risk assessment results identify "
                       "where exposure is greatest and therefore which controls matter most.",
            "distractors": {
                "B": "Vendor novelty is not a sound basis for control selection.",
                "C": "Personal preference is not a risk-based or defensible basis.",
                "D": "Copying a competitor ignores the organization's own risk profile and context.",
            },
            "exam_pattern": "Controls are risk-driven - selected from assessment results, not from products or peers.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk-based control selection"],
    },
    {
        "id": "cism-risk-005", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_assessment", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: The level of risk that exists before any controls or mitigating "
                "actions are applied is called _____ risk. (one word)",
        "correct": ["inherent"],
        "explanation": {
            "correct": "Inherent risk is the exposure that exists before controls; residual risk is what "
                       "remains after controls have been applied.",
            "exam_pattern": "Inherent risk = before controls; residual risk = after controls.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Inherent and residual risk"],
    },

    # ===== cism_risk_response ===============================================
    {
        "id": "cism-risk-006", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 1, "type": "mcq",
        "stem": "An organization purchases cyber-insurance to offset the financial loss from a potential "
                "breach. Which risk response does this represent?",
        "options": [
            {"id": "A", "text": "Risk transfer (sharing)"},
            {"id": "B", "text": "Risk acceptance"},
            {"id": "C", "text": "Risk avoidance"},
            {"id": "D", "text": "Risk mitigation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Buying insurance shifts (shares) the financial consequence of the risk to a third "
                       "party, which is risk transfer.",
            "distractors": {
                "B": "Acceptance means taking no action and retaining the risk, not shifting the loss.",
                "C": "Avoidance means eliminating the activity that causes the risk.",
                "D": "Mitigation reduces likelihood or impact with controls, not by shifting financial loss to another party.",
            },
            "exam_pattern": "Insurance/outsourcing the loss = transfer (share); accept, avoid, and mitigate are the other three responses.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk response options"],
    },
    {
        "id": "cism-risk-007", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "mcq",
        "stem": "After assessment, management decides a proposed online service carries unacceptable risk "
                "that cannot be cost-effectively reduced, so it cancels the project entirely. This is an "
                "example of risk:",
        "options": [
            {"id": "A", "text": "Mitigation"},
            {"id": "B", "text": "Avoidance"},
            {"id": "C", "text": "Acceptance"},
            {"id": "D", "text": "Transfer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cancelling the activity so the exposure never arises is risk avoidance - eliminating "
                       "the risk by not undertaking the activity.",
            "distractors": {
                "A": "Mitigation would reduce the risk while still offering the service, not cancel it.",
                "C": "Acceptance would proceed with the service and retain the risk.",
                "D": "Transfer would shift the risk to a third party, not eliminate the activity.",
            },
            "exam_pattern": "Eliminating the activity/exposure altogether = risk avoidance.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk avoidance"],
    },
    {
        "id": "cism-risk-008", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "mcq",
        "stem": "After controls are applied, a residual risk remains. Who should FORMALLY accept this "
                "residual risk?",
        "options": [
            {"id": "A", "text": "The information security manager"},
            {"id": "B", "text": "The security operations analyst"},
            {"id": "C", "text": "The external penetration tester"},
            {"id": "D", "text": "The appropriate business or senior management (the risk owner)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Residual risk is a business decision, so it is formally accepted by the appropriate "
                       "level of business/senior management - the risk owner - who bears the consequences.",
            "distractors": {
                "A": "The security manager advises and facilitates but does not own or accept the business risk.",
                "B": "An analyst has no authority to accept organizational risk.",
                "C": "A tester identifies weaknesses; they do not accept risk.",
            },
            "exam_pattern": "Residual risk is accepted by management/the business risk owner - never by the security manager alone.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk acceptance and ownership"],
    },
    {
        "id": "cism-risk-009", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 3, "type": "mcq",
        "stem": "An information security manager is evaluating a control that would cost far more to "
                "implement than the maximum loss the risk could ever cause. What is the BEST recommendation?",
        "options": [
            {"id": "A", "text": "Implement the control anyway to maximize security"},
            {"id": "B", "text": "Recommend a response proportionate to the risk, since the control's cost exceeds the potential loss"},
            {"id": "C", "text": "Ignore the risk entirely and document nothing"},
            {"id": "D", "text": "Transfer the risk by buying the most expensive insurance available"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Controls should be cost-effective: when a control costs more than the loss it "
                       "prevents, the manager recommends a proportionate response rather than overspending.",
            "distractors": {
                "A": "Spending more than the asset or loss is worth is not cost-effective or defensible.",
                "C": "Ignoring and failing to document the risk is not a managed response.",
                "D": "Buying maximal insurance regardless of cost repeats the same disproportion.",
            },
            "exam_pattern": "Control cost must be proportionate to the risk - never spend more protecting an asset than it is worth.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Cost-benefit of controls"],
    },
    {
        "id": "cism-risk-010", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_response", "difficulty": 2, "type": "mcq",
        "stem": "The board states the amount of risk the organization is willing to pursue in order to "
                "meet its objectives. This statement defines the organization's risk:",
        "options": [
            {"id": "A", "text": "Appetite"},
            {"id": "B", "text": "Register"},
            {"id": "C", "text": "Incident"},
            {"id": "D", "text": "Vulnerability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk appetite is the amount and type of risk an organization is willing to take on "
                       "to pursue its objectives; it is set by the board/senior management and guides decisions.",
            "distractors": {
                "B": "A risk register is a list of identified risks, not a statement of willingness to take risk.",
                "C": "An incident is a realized event, not a tolerance statement.",
                "D": "A vulnerability is a weakness, not a statement of acceptable risk.",
            },
            "exam_pattern": "Risk appetite = how much risk the organization will take to meet objectives (set by the board/senior mgmt).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk appetite and tolerance"],
    },

    # ===== cism_risk_monitoring =============================================
    {
        "id": "cism-risk-011", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An information security manager wants a metric that gives an early-warning signal that "
                "risk exposure is rising toward or beyond acceptable levels. Which type of metric is BEST "
                "suited?",
        "options": [
            {"id": "A", "text": "Key goal indicator (KGI)"},
            {"id": "B", "text": "Key performance indicator (KPI)"},
            {"id": "C", "text": "Key risk indicator (KRI)"},
            {"id": "D", "text": "Return on investment (ROI)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A KRI is a threshold-based, forward-looking metric designed to warn when risk "
                       "exposure is increasing, so management can act before the risk is realized.",
            "distractors": {
                "A": "A KGI measures achievement of a goal, not rising risk.",
                "B": "A KPI measures how well a process performs, not risk-exposure thresholds.",
                "D": "ROI measures financial return, not risk exposure.",
            },
            "exam_pattern": "Early warning of rising risk = KRI (predictive, threshold-based).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Key risk indicators"],
    },
    {
        "id": "cism-risk-012", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Why must information security risk be monitored on an ongoing basis rather than assessed "
                "only once?",
        "options": [
            {"id": "A", "text": "Because auditors require a brand-new report every single day"},
            {"id": "B", "text": "Because the threat and business environment change over time, altering risk levels"},
            {"id": "C", "text": "Because controls never work and must be constantly replaced"},
            {"id": "D", "text": "Because risk appetite must be lowered each year"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Risk is dynamic: threats, technology, and the business all change, so continuous "
                       "monitoring keeps the risk picture current and decisions well informed.",
            "distractors": {
                "A": "Audit cadence is not the reason; risk changes independently of audit schedules.",
                "C": "Controls do work; monitoring addresses change, not universal control failure.",
                "D": "Risk appetite is a management decision, not something that must drop every year.",
            },
            "exam_pattern": "Risk is dynamic - continuous monitoring keeps the picture current as threats and the business change.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Continuous risk monitoring"],
    },
    {
        "id": "cism-risk-013", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Which tool does an information security manager use to record identified risks, their "
                "owners, treatment decisions, and current status?",
        "options": [
            {"id": "A", "text": "The network topology diagram"},
            {"id": "B", "text": "The asset depreciation schedule"},
            {"id": "C", "text": "The risk register"},
            {"id": "D", "text": "The incident ticket queue"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The risk register is the central record of identified risks, their owners, chosen "
                       "treatments, and status, and it supports ongoing monitoring and reporting.",
            "distractors": {
                "A": "A network diagram shows topology, not risk tracking.",
                "B": "A depreciation schedule is a finance/asset record, not a risk record.",
                "D": "The ticket queue tracks incidents and requests, not the inventory of risks.",
            },
            "exam_pattern": "Risk register = the central record of risks, owners, treatments, and status.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Risk register"],
    },
    {
        "id": "cism-risk-014", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Monitoring reveals that a newly disclosed vulnerability significantly raises the "
                "likelihood that a previously accepted risk will be exploited. What should the information "
                "security manager do FIRST?",
        "options": [
            {"id": "A", "text": "Immediately shut down all affected systems"},
            {"id": "B", "text": "Reassess the risk and report the changed exposure to the risk owner and management"},
            {"id": "C", "text": "Remove the risk from the risk register"},
            {"id": "D", "text": "Do nothing, because the risk was already accepted"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A material change in exposure invalidates the earlier acceptance, so the manager "
                       "reassesses the risk and escalates the new picture to the risk owner for a decision.",
            "distractors": {
                "A": "Shutting systems down is a drastic step taken only if justified after reassessment.",
                "C": "Deleting the risk hides a now-elevated exposure.",
                "D": "A prior acceptance does not hold once the risk materially changes; it must be revisited.",
            },
            "exam_pattern": "When monitoring shows risk has changed, reassess and escalate to the owner - acceptance is not permanent.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Reassessing changed risk"],
    },
    {
        "id": "cism-risk-015", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_risk_monitoring", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The risk that remains after security controls and other mitigating "
                "measures have been applied is called _____ risk. (one word)",
        "correct": ["residual"],
        "explanation": {
            "correct": "Residual risk is what remains after controls are applied; it should fall within the "
                       "organization's risk appetite/tolerance, and management formally accepts it.",
            "exam_pattern": "Residual risk = after controls; it should be within risk appetite and accepted by management.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Residual risk"],
    },

    # ===== cism_asset_classification ========================================
    {
        "id": "cism-risk-016", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of classifying information assets?",
        "options": [
            {"id": "A", "text": "To make the asset inventory longer and more detailed"},
            {"id": "B", "text": "To determine the appropriate level of protection based on the asset's sensitivity and criticality"},
            {"id": "C", "text": "To assign each asset to a specific employee for tax purposes"},
            {"id": "D", "text": "To decide which assets should be deleted"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Classification matches the level of protection to the asset's sensitivity and "
                       "criticality, so controls are applied where they are most needed - the basis for "
                       "risk-based protection.",
            "distractors": {
                "A": "A longer inventory is not a purpose; classification is about protection level.",
                "C": "Tax assignment is unrelated to security classification.",
                "D": "Classification guides protection, not deletion decisions.",
            },
            "exam_pattern": "Classify to apply protection proportional to sensitivity/criticality.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Asset classification"],
    },
    {
        "id": "cism-risk-017", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "Who should determine the classification level of a particular set of business information?",
        "options": [
            {"id": "A", "text": "The data (information) owner"},
            {"id": "B", "text": "The firewall administrator"},
            {"id": "C", "text": "The physical security guard"},
            {"id": "D", "text": "The newest member of the help desk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The business data/information owner understands the information's value and is "
                       "responsible for classifying it (and authorizing access).",
            "distractors": {
                "B": "The firewall administrator enforces technical controls, not classification.",
                "C": "A guard handles physical access, not data classification.",
                "D": "Help-desk tenure is irrelevant; classification is the owner's responsibility.",
            },
            "exam_pattern": "The business data/information owner classifies the data.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Data ownership and classification"],
    },
    {
        "id": "cism-risk-018", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "An organization has labeled a dataset 'Highly Confidential.' How should this "
                "classification influence the security program?",
        "options": [
            {"id": "A", "text": "It should have no effect on control selection"},
            {"id": "B", "text": "It means the data may now be shared publicly"},
            {"id": "C", "text": "It requires the data to be deleted within 24 hours"},
            {"id": "D", "text": "It should drive stronger, commensurate controls such as encryption and strict access limits"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A higher classification calls for stronger, proportionate controls - the whole "
                       "point of classification is to drive the level of protection applied.",
            "distractors": {
                "A": "Classification exists precisely to influence control selection.",
                "B": "'Highly Confidential' restricts, rather than permits, public sharing.",
                "C": "Classification sets the protection level, not a blanket deletion deadline.",
            },
            "exam_pattern": "Higher classification -> stronger, commensurate controls; classification drives protection decisions.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Classification drives controls"],
    },
    {
        "id": "cism-risk-019", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 3, "type": "mcq",
        "stem": "A business unit labels nearly all of its data as 'Top Secret,' far above its actual "
                "sensitivity. Why is this a concern for the information security manager?",
        "options": [
            {"id": "A", "text": "It has no downside and should be encouraged"},
            {"id": "B", "text": "Over-classification wastes resources on excessive protection and erodes the credibility of the classification scheme"},
            {"id": "C", "text": "It automatically improves the organization's regulatory compliance"},
            {"id": "D", "text": "It reduces the organization's overall risk to zero"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Classification should match actual sensitivity; over-classification spends scarce "
                       "resources on unneeded protection and, when staff see it as excessive, undermines trust "
                       "in the whole scheme.",
            "distractors": {
                "A": "Over-classification does have downsides, so it should not simply be encouraged.",
                "C": "Mislabeling does not improve compliance; accurate classification does.",
                "D": "No scheme reduces risk to zero, and over-classification does not either.",
            },
            "exam_pattern": "Classification should match real sensitivity - over- and under-classification both cause problems (cost, credibility, exposure).",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Appropriate classification"],
    },
    {
        "id": "cism-risk-020", "exam": "cism", "domain": "cism_risk",
        "subtopic": "cism_asset_classification", "difficulty": 2, "type": "mcq",
        "stem": "When an organization adopts a data classification scheme, what must be assigned to each "
                "information asset to ensure accountability for its classification and protection?",
        "options": [
            {"id": "A", "text": "An identified data owner"},
            {"id": "B", "text": "A dedicated new firewall"},
            {"id": "C", "text": "A public IP address"},
            {"id": "D", "text": "A marketing label"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Every asset needs an identified owner; ownership is the foundation of "
                       "accountability for classifying the asset and ensuring it is protected appropriately.",
            "distractors": {
                "B": "A firewall is a control, not an accountability assignment.",
                "C": "An IP address is a network attribute, not accountability for the asset.",
                "D": "A marketing label is unrelated to classification accountability.",
            },
            "exam_pattern": "Assign an owner to every asset - ownership underpins accountability for classification and protection.",
        },
        "references": ["ISACA CISM Review Manual: Domain 2 - Asset ownership"],
    },
]
