"""ISACA CISA pool - Domain 1: Information Systems Auditing Process.

Original, objective-aligned practice items for the five Domain 1 subtopics
tracked in the study engine:
  * cisa_audit_standards   - ISACA IS Audit and Assurance Standards vs.
                             Guidelines, the audit charter, independence and
                             objectivity of the IS auditor.
  * cisa_risk_based_audit  - risk-based audit planning, audit risk components
                             (inherent/control/detection), materiality.
  * cisa_audit_execution   - control types (preventive/detective/corrective),
                             control self-assessment, CAATs.
  * cisa_evidence_sampling - audit evidence and its reliability, statistical vs.
                             non-statistical sampling, attribute vs. variable
                             sampling, sampling risk.
  * cisa_audit_reporting   - communicating findings to the auditee and to those
                             charged with governance, follow-up, management's
                             responsibility for risk acceptance.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's mindset (objectivity, evidence, risk-based focus, reporting to
governance). All items are ORIGINAL and aligned to public exam objectives -
never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cisa_audit_standards =============================================
    {
        "id": "cisa-aud-001", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 2, "type": "mcq",
        "stem": "An organization is establishing a new IS audit function. What is the PRIMARY "
                "purpose of the audit charter?",
        "options": [
            {"id": "A", "text": "To document the detailed audit procedures the team follows on each engagement"},
            {"id": "B", "text": "To list the specific IT systems that will be audited during the year"},
            {"id": "C", "text": "To define the IS audit function's authority, responsibility, and accountability, "
                               "approved by the board or audit committee"},
            {"id": "D", "text": "To record the findings and recommendations from completed audits"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The audit charter is a high-level document, approved at the highest level (board or "
                       "audit committee), that formally establishes the audit function's purpose, authority, "
                       "responsibility, and accountability.",
            "distractors": {
                "A": "Detailed procedures belong in the audit program/methodology, not the charter.",
                "B": "The systems to audit come from the risk-based annual audit plan, not the charter.",
                "D": "Findings and recommendations are documented in audit reports, not the charter.",
            },
            "exam_pattern": "Charter = the mandate/authority approved at the top; it is not the plan, program, or report.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit charter and the IS audit function"],
    },
    {
        "id": "cisa-aud-002", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor is assigned to audit an application that the same auditor helped design "
                "and implement last year. What should the auditor do?",
        "options": [
            {"id": "A", "text": "Proceed, because prior involvement gives the auditor useful system knowledge"},
            {"id": "B", "text": "Inform audit management of the impairment to independence so the work can be reassigned"},
            {"id": "C", "text": "Perform the audit but omit the modules the auditor personally built"},
            {"id": "D", "text": "Proceed only after obtaining written approval from the application's users"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Having designed and implemented the system creates a self-review threat that impairs "
                       "independence and objectivity; the auditor must disclose it to audit management so the "
                       "work is reassigned to an objective auditor.",
            "distractors": {
                "A": "Useful knowledge does not cure the self-review threat; independence is still impaired.",
                "C": "Omitting modules does not restore objectivity over a system the auditor built.",
                "D": "User approval cannot restore the auditor's independence; only reassignment does.",
            },
            "exam_pattern": "Auditing your own prior work is a self-review threat - disclose and reassign, don't rationalize.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Independence and objectivity"],
    },
    {
        "id": "cisa-aud-003", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 1, "type": "mcq",
        "stem": "How do ISACA's IS Audit and Assurance Standards differ from the related Guidelines?",
        "options": [
            {"id": "A", "text": "Standards are optional; Guidelines are mandatory"},
            {"id": "B", "text": "Both Standards and Guidelines are optional recommendations"},
            {"id": "C", "text": "Both Standards and Guidelines are mandatory requirements"},
            {"id": "D", "text": "Standards are mandatory; Guidelines provide guidance on how to apply the Standards"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "ISACA IS Audit and Assurance Standards are mandatory for CISAs, while Guidelines provide "
                       "non-mandatory guidance on how to meet the Standards.",
            "distractors": {
                "A": "Reversed - the Standards are the mandatory element, not the Guidelines.",
                "B": "Standards are mandatory, not optional.",
                "C": "Guidelines are guidance, not mandatory requirements.",
            },
            "exam_pattern": "Standards = mandatory 'what'; Guidelines = non-mandatory 'how.'",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — ISACA IS Audit and Assurance Standards and Guidelines"],
    },
    {
        "id": "cisa-aud-004", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 3, "type": "multi",
        "stem": "Which TWO situations would MOST likely impair an IS auditor's independence? (Choose two.)",
        "options": [
            {"id": "A", "text": "The auditor developed the key control scripts for the system now under audit"},
            {"id": "B", "text": "The auditor has no prior relationship with the audited department"},
            {"id": "C", "text": "A close family member of the auditor manages the department being audited"},
            {"id": "D", "text": "The auditor uses generalized audit software provided by a third party"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Auditing a system one personally developed (self-review threat) and auditing a unit run "
                       "by a close family member (personal/relationship threat) both impair independence and objectivity.",
            "distractors": {
                "B": "Having no prior relationship supports independence rather than impairing it.",
                "D": "Using third-party audit software is a normal tool and does not impair independence.",
            },
            "exam_pattern": "Self-review and personal relationships impair independence; neutral tools and no prior ties do not.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Independence and objectivity"],
    },

    # ===== cisa_risk_based_audit ============================================
    {
        "id": "cisa-aud-005", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY advantage of a risk-based approach to audit planning?",
        "options": [
            {"id": "A", "text": "It guarantees that every system is audited with equal depth each year"},
            {"id": "B", "text": "It directs limited audit resources toward the areas of greatest risk"},
            {"id": "C", "text": "It removes the need for the auditor to document a conclusion"},
            {"id": "D", "text": "It eliminates detection risk from the engagement"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A risk-based approach focuses finite audit resources on the areas where risk to the "
                       "organization is highest, improving the efficiency and relevance of the audit.",
            "distractors": {
                "A": "A risk-based plan deliberately covers low-risk areas less often, not everything equally.",
                "C": "The auditor must still document a supported conclusion regardless of approach.",
                "D": "Detection risk can be reduced but never fully eliminated.",
            },
            "exam_pattern": "Risk-based = aim scarce audit effort at the highest-risk areas.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Risk-based audit planning"],
    },
    {
        "id": "cisa-aud-006", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 3, "type": "mcq",
        "stem": "When determining materiality for an IS audit of a non-financial system, what should the "
                "IS auditor consider MOST?",
        "options": [
            {"id": "A", "text": "Only the monetary value of the hardware involved"},
            {"id": "B", "text": "The number of programs written for the application"},
            {"id": "C", "text": "The criticality and sensitivity of the information assets and the impact of control failures"},
            {"id": "D", "text": "The personal preference of the lead auditor"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "In IS audit, materiality extends beyond monetary value to the criticality and sensitivity "
                       "of the information assets and the potential impact of control weaknesses on the organization.",
            "distractors": {
                "A": "Hardware value alone ignores the sensitivity and criticality of the data and processes.",
                "B": "The count of programs does not indicate how material a weakness is.",
                "D": "Materiality is an objective judgment about impact, not personal preference.",
            },
            "exam_pattern": "IS-audit materiality = criticality/sensitivity and impact of control failure, not just dollars.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Materiality"],
    },
    {
        "id": "cisa-aud-007", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: The risk that an IS auditor's substantive testing fails to detect a "
                "material error that actually exists is called ______ risk.",
        "correct": ["detection", "detection risk"],
        "explanation": {
            "correct": "Detection risk is the risk that the auditor's own procedures will not catch a material "
                       "error; the auditor manages it by adjusting the nature, timing, and extent of testing.",
            "distractors": {},
            "exam_pattern": "Audit risk = inherent x control x detection; detection risk is the part the auditor directly controls.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit risk and materiality"],
    },
    {
        "id": "cisa-aud-008", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 2, "type": "mcq",
        "stem": "When beginning a risk-based audit of a new business application, what should the IS "
                "auditor do FIRST?",
        "options": [
            {"id": "A", "text": "Draft the structure of the final audit report"},
            {"id": "B", "text": "Select the sampling method for fieldwork"},
            {"id": "C", "text": "Recommend specific control improvements to management"},
            {"id": "D", "text": "Obtain an understanding of the business process and its environment to identify risks"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The auditor must first understand the business process, its objectives, and environment "
                       "so that the relevant risks - which drive the rest of the audit - can be identified and assessed.",
            "distractors": {
                "A": "The report is drafted near the end, after fieldwork is complete.",
                "B": "Sampling is chosen during fieldwork planning, after the risks are understood.",
                "C": "Recommendations come after testing reveals weaknesses, not first.",
            },
            "exam_pattern": "FIRST in any audit = understand the process/environment and assess risk before testing or reporting.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Risk-based audit planning"],
    },

    # ===== cisa_audit_execution =============================================
    {
        "id": "cisa-aud-009", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 2, "type": "mcq",
        "stem": "In a control self-assessment (CSA) program, which statement BEST describes the IS "
                "auditor's role?",
        "options": [
            {"id": "A", "text": "The auditor performs all control testing on behalf of the business"},
            {"id": "B", "text": "The auditor assumes ownership of the business unit's controls"},
            {"id": "C", "text": "The auditor acts as a facilitator while business process owners assess their own controls"},
            {"id": "D", "text": "The auditor replaces management's responsibility for the control environment"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "In CSA, the business process owners evaluate their own controls while the IS auditor "
                       "typically facilitates the process - which also preserves the auditor's independence.",
            "distractors": {
                "A": "In CSA the business, not the auditor, performs the self-assessment of its controls.",
                "B": "Control ownership stays with management, never the auditor.",
                "D": "Management remains responsible for controls; CSA does not shift that to the auditor.",
            },
            "exam_pattern": "CSA = owners assess their own controls; the auditor facilitates, it does not own them.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Control self-assessment (CSA)"],
    },
    {
        "id": "cisa-aud-010", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor wants to test every transaction in a large payment file rather than a "
                "sample. What is the PRIMARY benefit of using computer-assisted audit techniques (CAATs)?",
        "options": [
            {"id": "A", "text": "They remove the need to understand the application's controls"},
            {"id": "B", "text": "They allow the auditor to analyze entire populations of data efficiently"},
            {"id": "C", "text": "They transfer responsibility for the conclusion to the software vendor"},
            {"id": "D", "text": "They guarantee that no errors exist in the data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "CAATs such as generalized audit software let the auditor independently examine large "
                       "volumes or entire populations of data efficiently, improving coverage and the reliability of evidence.",
            "distractors": {
                "A": "The auditor still needs to understand the controls to interpret the results.",
                "C": "The auditor retains responsibility for the audit conclusion.",
                "D": "Testing can detect errors but cannot guarantee their absence.",
            },
            "exam_pattern": "CAATs' value = efficient, independent analysis of full populations / large data sets.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Computer-assisted audit techniques (CAATs)"],
    },
    {
        "id": "cisa-aud-011", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 1, "type": "mcq",
        "stem": "An organization reconciles system audit logs each week to spot unauthorized changes "
                "after they occur. This is an example of which type of control?",
        "options": [
            {"id": "A", "text": "Preventive control"},
            {"id": "B", "text": "Corrective control"},
            {"id": "C", "text": "Detective control"},
            {"id": "D", "text": "Deterrent control"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reviewing logs to identify events that have already happened is a detective control - it "
                       "discovers problems rather than stopping or fixing them.",
            "distractors": {
                "A": "A preventive control would stop the change before it occurs, e.g., an access restriction.",
                "B": "A corrective control restores or remediates after an event, e.g., restoring from backup.",
                "D": "A deterrent discourages the act (e.g., a warning banner) but does not detect it.",
            },
            "exam_pattern": "Prevent = stop before; Detect = find after; Correct = fix after.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Types of controls"],
    },

    # ===== cisa_evidence_sampling ===========================================
    {
        "id": "cisa-aud-012", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following would provide the MOST reliable audit evidence?",
        "options": [
            {"id": "A", "text": "A photocopy of a report supplied by the auditee"},
            {"id": "B", "text": "An oral explanation given by the system administrator"},
            {"id": "C", "text": "A screenshot emailed by the process owner"},
            {"id": "D", "text": "A confirmation obtained directly by the auditor from an independent external party"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Evidence is most reliable when it is obtained directly by the auditor and originates from "
                       "an independent, external source; both factors strengthen reliability.",
            "distractors": {
                "A": "A copy provided by the auditee is internal and not obtained directly by the auditor.",
                "B": "Oral evidence is among the least reliable and needs corroboration.",
                "C": "A screenshot supplied by the auditee is internal and easily altered.",
            },
            "exam_pattern": "Reliability rises with auditor-obtained + independent/external + written/original evidence.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit evidence and its reliability"],
    },
    {
        "id": "cisa-aud-013", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor wants to estimate how often a required purchase-order approval control was "
                "actually performed. Which sampling method is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Variable (substantive) sampling"},
            {"id": "B", "text": "Attribute sampling"},
            {"id": "C", "text": "Stratified mean-per-unit sampling"},
            {"id": "D", "text": "Monetary unit sampling"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Attribute sampling measures the rate of occurrence (deviation rate) of a control "
                       "attribute - whether the approval was present or not - making it the right choice for "
                       "compliance testing of a control.",
            "distractors": {
                "A": "Variable sampling estimates monetary amounts or quantities, not how often a control operated.",
                "C": "Stratified mean-per-unit is a variable technique for estimating values.",
                "D": "Monetary unit sampling targets dollar misstatement, not control-operation frequency.",
            },
            "exam_pattern": "Compliance test of a control's presence/absence = attribute sampling; estimate amounts = variable.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit sampling (attribute vs. variable)"],
    },
    {
        "id": "cisa-aud-014", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The risk that the auditor's conclusion drawn from a sample differs "
                "from the conclusion that testing the entire population would produce is called ______ risk.",
        "correct": ["sampling", "sampling risk"],
        "explanation": {
            "correct": "Sampling risk arises because a sample may not perfectly represent the population; "
                       "statistical sampling lets the auditor quantify and control it.",
            "distractors": {},
            "exam_pattern": "Sampling risk = the sample might not represent the whole population.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit sampling and sampling risk"],
    },
    {
        "id": "cisa-aud-015", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 2, "type": "mcq",
        "stem": "What is the MAIN advantage of statistical sampling over non-statistical (judgmental) "
                "sampling?",
        "options": [
            {"id": "A", "text": "It lets the auditor objectively quantify sampling risk and the confidence level"},
            {"id": "B", "text": "It always requires a smaller sample than judgmental sampling"},
            {"id": "C", "text": "It removes the need for the auditor to use professional judgment at all"},
            {"id": "D", "text": "It guarantees the sample is free from error"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Statistical sampling uses probability theory, so the auditor can objectively measure "
                       "sampling risk and express the result with a defined confidence level.",
            "distractors": {
                "B": "Statistical sampling does not inherently produce smaller samples; size depends on the parameters.",
                "C": "Judgment is still needed to design the test and evaluate the results.",
                "D": "No sampling method can guarantee an error-free sample.",
            },
            "exam_pattern": "Statistical sampling's edge = objective, quantified sampling risk and confidence.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Statistical vs. non-statistical sampling"],
    },

    # ===== cisa_audit_reporting =============================================
    {
        "id": "cisa-aud-016", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 2, "type": "mcq",
        "stem": "Before finalizing and issuing the audit report, what should the IS auditor do with the "
                "findings?",
        "options": [
            {"id": "A", "text": "Submit them directly to external regulators"},
            {"id": "B", "text": "Implement the corrective actions personally"},
            {"id": "C", "text": "Discuss them with the auditee to confirm factual accuracy and obtain management's response"},
            {"id": "D", "text": "Remove any finding that management disagrees with"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The auditor should review findings with the auditee (e.g., at a closing meeting) to "
                       "validate the facts, correct any misunderstanding, and capture management's response before "
                       "the report is finalized.",
            "distractors": {
                "A": "Reporting to regulators is management's decision and not the normal pre-issuance step.",
                "B": "Implementing corrective actions would impair independence; remediation is management's job.",
                "D": "Findings are not deleted because of disagreement; management's view is documented instead.",
            },
            "exam_pattern": "Validate findings with the auditee first - don't fix, hide, or escalate them yourself.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Communicating audit results"],
    },
    {
        "id": "cisa-aud-017", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 1, "type": "mcq",
        "stem": "What is the PRIMARY purpose of audit follow-up activities?",
        "options": [
            {"id": "A", "text": "To design the controls the auditee should implement"},
            {"id": "B", "text": "To determine whether management has implemented the agreed corrective actions"},
            {"id": "C", "text": "To re-perform the entire original audit from the start"},
            {"id": "D", "text": "To assign blame for the original findings"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Follow-up verifies whether management took the agreed corrective action within the "
                       "committed timeframe and whether that action adequately addresses the reported risk.",
            "distractors": {
                "A": "Designing controls is management's responsibility, not the purpose of follow-up.",
                "C": "Follow-up targets the agreed actions, not a full re-audit.",
                "D": "Audit aims to improve controls, not to assign blame.",
            },
            "exam_pattern": "Follow-up = did management act on the agreed remediation, and did it work?",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Follow-up activities"],
    },
    {
        "id": "cisa-aud-018", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 2, "type": "mcq",
        "stem": "After an IS audit reports a significant control weakness, who is responsible for deciding "
                "whether to remediate it or formally accept the risk?",
        "options": [
            {"id": "A", "text": "The IS auditor who identified the weakness"},
            {"id": "B", "text": "The external regulator"},
            {"id": "C", "text": "The audit committee's administrative secretary"},
            {"id": "D", "text": "Management, as the business and risk owner"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Management owns the risk and therefore decides whether to remediate or formally accept "
                       "it; the auditor reports and recommends but does not make or own that decision.",
            "distractors": {
                "A": "The auditor recommends but cannot accept risk on the organization's behalf - that would impair independence.",
                "B": "Regulators may impose requirements but do not make this internal risk-acceptance decision.",
                "C": "Administrative audit-committee staff do not own the business risk.",
            },
            "exam_pattern": "Auditor recommends; management decides and owns the risk acceptance.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Reporting and management's responsibility"],
    },
]
