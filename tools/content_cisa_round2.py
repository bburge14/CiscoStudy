"""ISACA CISA pool - Round 2 expansion (all five domains).

Original, objective-aligned practice items that DEEPEN the round-1 CISA bank
(content_cisa_audit/governance/acquisition/operations/protection.py, 92 items)
without duplicating any of them. Round-2 ids carry an `-r2-` segment so they are
unique across the merged pool; the build glob (tools/build_content.py) auto-
discovers this file and concatenates it with the base pool.

Distribution mirrors the blueprint weights (operations_resilience 26%,
protection_assets 26%, audit_process 18%, governance 18%, acquisition_dev 12%):
  * cisa_audit_process          - 20 items
  * cisa_governance             - 19 items
  * cisa_acquisition_dev        - 13 items
  * cisa_operations_resilience  - 28 items
  * cisa_protection_assets      - 28 items  (108 total)

Round-2 goes deeper than round-1 on: organizational independence / reporting
line, proficiency & use of experts, reasonable assurance, scope limitation;
inherent/control risk, the audit-risk model, risk-based planning; compliance vs.
substantive testing, continuous-audit CAATs (embedded audit modules/SCARF, ITF,
parallel simulation), control types; variable/discovery/stop-or-go sampling,
re-performance; fraud reporting, finding structure, follow-up escalation;
COBIT governance-vs-management, IT balanced scorecard, enterprise architecture,
maturity models, standards hierarchy, SoD/mandatory-vacation, ALE/KRI/qualitative
risk, MTD/RTO, BCP-vs-DRP; PERT/Gantt/critical-path/earned value, prototyping/
agile/escrow/white-box testing, phased/pilot conversion & data cleansing, PIR;
change/patch/job-scheduling/CMDB/EUC, EDI & input controls (check digit, hash
totals, range checks), backup mechanics (archive bit, incremental restore, RAID
vs. backup, remote journaling), recovery sites (warm/mobile), DR test order,
incident priority/known error/service desk/escalation, database ACID/concurrency/
views/recovery/data dictionary; access models (MAC/RBAC), biometrics (FAR/FRR/
CER), deprovisioning, SSO; DMZ/proxy/segmentation/WEP/honeypot, retention &
sanitization/labeling/DLP, asymmetric confidentiality/hashing/OCSP-CRL/key mgmt/
signature services, log time-sync/IDS methods/scan-vs-pentest/audit trails, HVAC
humidity/pre-action suppression/generator/Halon/physical access logging.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's mindset (objectivity, evidence-based, risk-based focus, BEST FIRST/
PRIMARY action, reporting to governance). All items are ORIGINAL and aligned to
public exam objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ======================================================================
    # DOMAIN 1 - Information Systems Auditing Process
    # ======================================================================
    # ----- cisa_audit_standards -----
    {
        "id": "cisa-aud-r2-001", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 2, "type": "mcq",
        "stem": "To preserve the independence of the IS audit function, the function should report FUNCTIONALLY to:",
        "options": [
            {"id": "A", "text": "The audit committee of the board of directors"},
            {"id": "B", "text": "The chief information officer (CIO) whose area it audits"},
            {"id": "C", "text": "The IT operations manager"},
            {"id": "D", "text": "The head of software development"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reporting functionally to the audit committee (board) keeps the audit function organizationally independent of the IT management whose activities it examines.",
            "distractors": {
                "B": "The CIO owns the IT area under audit; reporting to the CIO impairs independence.",
                "C": "IT operations is a subject of the audit, not an independent oversight body.",
                "D": "Software development is audited by the function and cannot be its reporting line.",
            },
            "exam_pattern": "Audit reports functionally to the audit committee/board - never to the IT management it audits.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Organizational independence and reporting lines"],
    },
    {
        "id": "cisa-aud-r2-002", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor is assigned to audit a highly specialized system that is outside the auditor's technical expertise. What is the BEST course of action?",
        "options": [
            {"id": "A", "text": "Decline to form any conclusion about the system"},
            {"id": "B", "text": "Engage or consult a qualified subject-matter expert while retaining responsibility for the audit conclusion"},
            {"id": "C", "text": "Proceed and rely only on management's verbal assurances"},
            {"id": "D", "text": "Omit the specialized system and report on the rest"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The proficiency standard lets the auditor use a competent expert's work for areas beyond their skill, but the IS auditor still owns and supervises the conclusion.",
            "distractors": {
                "A": "Declining abandons the objective; the standards provide for using experts instead.",
                "C": "Verbal assurances are weak evidence and do not address the competence gap.",
                "D": "Scoping out the key system undermines the purpose of the audit.",
            },
            "exam_pattern": "Lack a skill? Use a competent expert - but the auditor still owns the conclusion (proficiency/due care).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Proficiency and use of the work of experts"],
    },
    {
        "id": "cisa-aud-r2-003", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 2, "type": "mcq",
        "stem": "An IS audit concludes that controls are adequate. Which statement BEST reflects the level of assurance the auditor can provide?",
        "options": [
            {"id": "A", "text": "Absolute assurance that no control weakness or error exists"},
            {"id": "B", "text": "A guarantee that fraud is impossible"},
            {"id": "C", "text": "Reasonable assurance, because inherent limitations and sampling mean some issues may go undetected"},
            {"id": "D", "text": "No assurance at all"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Because of sampling and the inherent limitations of any audit, the IS auditor provides reasonable - not absolute - assurance.",
            "distractors": {
                "A": "Audits cannot provide absolute assurance that every issue has been found.",
                "B": "No audit can guarantee that fraud is impossible.",
                "D": "The audit does provide assurance; it is reasonable rather than none.",
            },
            "exam_pattern": "Audits give REASONABLE assurance, not absolute (sampling + inherent limitations).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Reasonable assurance and inherent limitations"],
    },
    {
        "id": "cisa-aud-r2-004", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_standards", "difficulty": 3, "type": "mcq",
        "stem": "Midway through an engagement, management restricts the IS auditor from accessing records needed to complete testing. What should the auditor do?",
        "options": [
            {"id": "A", "text": "Document the scope limitation and communicate it to those charged with governance, assessing its effect on the conclusion"},
            {"id": "B", "text": "Quietly drop the affected tests and issue an unqualified report"},
            {"id": "C", "text": "Accept management's decision without comment"},
            {"id": "D", "text": "Continue and estimate the missing results"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A scope limitation must be documented and reported to those charged with governance, and its effect on the audit opinion must be considered.",
            "distractors": {
                "B": "Silently dropping tests and issuing a clean report misrepresents the audit.",
                "C": "Accepting a limitation without comment fails the auditor's reporting duty.",
                "D": "Fabricating or estimating missing results is an ethics violation, not evidence.",
            },
            "exam_pattern": "Scope limitation -> document it, report to governance, and weigh its effect on the opinion.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Scope limitations and reporting"],
    },
    # ----- cisa_risk_based_audit -----
    {
        "id": "cisa-aud-r2-005", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The susceptibility of a process or account to a material error, assuming NO related internal controls are in place, is called ______ risk.",
        "correct": ["inherent", "inherent risk"],
        "explanation": {
            "correct": "Inherent risk is the risk present before controls are considered; the audit risk model then factors in control risk and detection risk.",
            "distractors": {},
            "exam_pattern": "Inherent = risk before controls; control = controls fail; detection = auditor misses it.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit risk components (inherent risk)"],
    },
    {
        "id": "cisa-aud-r2-006", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor assesses both inherent risk and control risk for a process as high. To keep overall audit risk at an acceptable level, the auditor should:",
        "options": [
            {"id": "A", "text": "Reduce the amount of substantive testing"},
            {"id": "B", "text": "Ignore detection risk because it cannot be controlled"},
            {"id": "C", "text": "Increase the extent of substantive testing to lower detection risk"},
            {"id": "D", "text": "Issue the report without any testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When inherent and control risk are high, the auditor lowers detection risk - the component they control - by performing more or more rigorous substantive testing.",
            "distractors": {
                "A": "Reducing testing raises detection risk and therefore overall audit risk.",
                "B": "Detection risk is exactly the component the auditor can manage through testing.",
                "D": "No testing provides no basis for a supported conclusion.",
            },
            "exam_pattern": "High inherent + control risk -> lower detection risk by doing MORE substantive testing.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit risk model (inherent x control x detection)"],
    },
    {
        "id": "cisa-aud-r2-007", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 2, "type": "mcq",
        "stem": "Which component of the audit risk model is reduced when an organization designs and operates strong, effective internal controls?",
        "options": [
            {"id": "A", "text": "Control risk"},
            {"id": "B", "text": "Inherent risk"},
            {"id": "C", "text": "Detection risk"},
            {"id": "D", "text": "Business risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Effective internal controls reduce control risk - the risk that a material error is not prevented or detected by the organization's own controls.",
            "distractors": {
                "B": "Inherent risk exists regardless of controls and is not reduced by them.",
                "C": "Detection risk relates to the auditor's own procedures, not the client's controls.",
                "D": "Business risk is broader and is not a component of the audit risk model.",
            },
            "exam_pattern": "Strong internal controls lower CONTROL risk (not inherent, detection, or business risk).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Control risk"],
    },
    {
        "id": "cisa-aud-r2-008", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_risk_based_audit", "difficulty": 2, "type": "mcq",
        "stem": "What should be the PRIMARY basis for deciding which areas to include in the annual IS audit plan?",
        "options": [
            {"id": "A", "text": "The areas that are easiest and quickest to audit"},
            {"id": "B", "text": "The personal interests of the audit team"},
            {"id": "C", "text": "Alphabetical order of the systems"},
            {"id": "D", "text": "A risk assessment of the organization's auditable universe"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A risk-based plan allocates audit coverage according to a risk assessment of the auditable universe, directing effort where risk is greatest.",
            "distractors": {
                "A": "Auditing by convenience leaves the highest-risk areas potentially uncovered.",
                "B": "Personal interest is neither objective nor risk-driven.",
                "C": "Arbitrary ordering ignores risk entirely.",
            },
            "exam_pattern": "The annual audit plan is built from a risk assessment of the audit universe.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Risk-based annual audit planning"],
    },
    # ----- cisa_audit_execution -----
    {
        "id": "cisa-aud-r2-009", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor wants to determine whether a required access-approval control is actually operating. Which type of test is this?",
        "options": [
            {"id": "A", "text": "Compliance test"},
            {"id": "B", "text": "Substantive test"},
            {"id": "C", "text": "Penetration test"},
            {"id": "D", "text": "Stress test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A compliance test determines whether a control is being applied as designed (operating effectiveness).",
            "distractors": {
                "B": "A substantive test verifies the integrity/accuracy of data or balances, not whether a control operates.",
                "C": "Penetration testing probes exploitable security weaknesses, not control operation.",
                "D": "Stress testing checks performance under load.",
            },
            "exam_pattern": "Does the CONTROL operate? = compliance test. Is the DATA accurate? = substantive test.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Compliance vs. substantive testing"],
    },
    {
        "id": "cisa-aud-r2-010", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 3, "type": "mcq",
        "stem": "For a high-volume online transaction system that cannot be interrupted, which technique lets the IS auditor capture and flag selected transactions continuously as they are processed?",
        "options": [
            {"id": "A", "text": "An embedded audit module (e.g., SCARF) built into the application"},
            {"id": "B", "text": "A one-time year-end manual sample"},
            {"id": "C", "text": "Reviewing printed reports once a year"},
            {"id": "D", "text": "Shutting the system down to review it offline"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An embedded audit module - such as a systems control audit review file (SCARF) - is built into the production application to capture and flag transactions continuously, ideal when processing cannot be stopped.",
            "distractors": {
                "B": "A single year-end sample is not continuous and misses interim activity.",
                "C": "Annual report review is neither continuous nor transaction-level.",
                "D": "Disabling an online production system is not acceptable.",
            },
            "exam_pattern": "Continuous, in-line transaction capture on a non-stop system = embedded audit module (SCARF).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Continuous auditing and embedded audit modules"],
    },
    {
        "id": "cisa-aud-r2-011", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor uses an integrated test facility (ITF), processing test transactions for a fictitious entity within the LIVE production system. What is the auditor's KEY precaution?",
        "options": [
            {"id": "A", "text": "Allow the test transactions to post permanently to prove the system works"},
            {"id": "B", "text": "Ensure the test transactions are isolated and reversed so they do not corrupt live data or financial totals"},
            {"id": "C", "text": "Give every user access to the fictitious entity"},
            {"id": "D", "text": "Run the ITF only after the system is decommissioned"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Because ITF runs test data through the live system, the test transactions must be segregated and backed out so real data and totals are not contaminated.",
            "distractors": {
                "A": "Leaving test entries posted corrupts real balances.",
                "C": "Broad access to the test entity is unnecessary and risky.",
                "D": "Running ITF on a decommissioned system defeats its purpose of testing live processing.",
            },
            "exam_pattern": "ITF runs test data through the LIVE system -> isolate and reverse the test transactions.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Integrated test facility (ITF)"],
    },
    {
        "id": "cisa-aud-r2-012", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor reprocesses real production data using the auditor's own independently written program and compares the output to the live system's results. This CAAT is known as:",
        "options": [
            {"id": "A", "text": "The test data method"},
            {"id": "B", "text": "Parallel simulation"},
            {"id": "C", "text": "Control self-assessment"},
            {"id": "D", "text": "A structured walkthrough"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Parallel simulation uses the auditor's own program on actual production data, comparing its output with the live system to detect processing errors.",
            "distractors": {
                "A": "The test data method runs the auditor's (often fictitious) data through the client's program - the reverse of this.",
                "C": "CSA is a facilitated self-review by process owners, not reprocessing of data.",
                "D": "A structured walkthrough is a review/discussion, not reprocessing.",
            },
            "exam_pattern": "Auditor's OWN program + REAL data, compared to production = parallel simulation.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — CAATs (parallel simulation)"],
    },
    {
        "id": "cisa-aud-r2-013", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_execution", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are PREVENTIVE controls? (Choose two.)",
        "options": [
            {"id": "A", "text": "An input edit/validation check that rejects invalid data before it is processed"},
            {"id": "B", "text": "Segregation of duties between authorizing and recording transactions"},
            {"id": "C", "text": "Reviewing audit logs weekly to spot unauthorized changes"},
            {"id": "D", "text": "Restoring data from backup after corruption is discovered"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "An edit check that blocks bad data before processing and segregation of duties both stop an undesirable event before it occurs - preventive controls.",
            "distractors": {
                "C": "Reviewing logs after the fact discovers events that already happened - a detective control.",
                "D": "Restoring from backup after corruption remediates an event - a corrective control.",
            },
            "exam_pattern": "Preventive = stop before (edit checks, SoD); detective = find after (log review); corrective = fix after (restore).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Types of controls (preventive/detective/corrective)"],
    },
    # ----- cisa_evidence_sampling -----
    {
        "id": "cisa-aud-r2-014", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor wants to estimate the total dollar value of misstatement in an accounts-payable file. Which sampling approach is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Variable sampling"},
            {"id": "B", "text": "Attribute sampling"},
            {"id": "C", "text": "Discovery sampling"},
            {"id": "D", "text": "Stop-or-go sampling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Variable sampling estimates a numeric amount (such as a monetary value or misstatement), which is what this objective requires.",
            "distractors": {
                "B": "Attribute sampling estimates a rate of occurrence (how often), not a dollar amount.",
                "C": "Discovery sampling aims to find at least one critical/fraudulent item, not estimate a total value.",
                "D": "Stop-or-go sampling is used to minimize sample size when few errors are expected.",
            },
            "exam_pattern": "Estimate an AMOUNT/value = variable sampling; estimate a RATE of occurrence = attribute sampling.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Variable vs. attribute sampling"],
    },
    {
        "id": "cisa-aud-r2-015", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor suspects fraud and wants a sampling method whose goal is to detect at least one instance of an irregularity when the expected occurrence rate is very low. Which method fits BEST?",
        "options": [
            {"id": "A", "text": "Discovery sampling"},
            {"id": "B", "text": "Variable (mean-per-unit) sampling"},
            {"id": "C", "text": "Monetary unit sampling for valuation"},
            {"id": "D", "text": "Judgmental sampling of the largest items only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Discovery sampling is designed to surface at least one instance of a critical deviation or fraud when the expected occurrence rate is very low.",
            "distractors": {
                "B": "Variable sampling estimates monetary values, not the existence of a rare irregularity.",
                "C": "Monetary unit sampling targets overstatement in value, not fraud discovery.",
                "D": "Testing only the largest items can miss small fraudulent transactions.",
            },
            "exam_pattern": "Find at least one rare/fraudulent instance (low expected rate) = discovery sampling.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Discovery sampling"],
    },
    {
        "id": "cisa-aud-r2-016", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 3, "type": "mcq",
        "stem": "Which sampling approach is designed to avoid excessive sampling by allowing the auditor to stop as early as possible when few or no errors are expected?",
        "options": [
            {"id": "A", "text": "Stop-or-go sampling"},
            {"id": "B", "text": "Variable sampling"},
            {"id": "C", "text": "Stratified sampling"},
            {"id": "D", "text": "Cluster sampling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Stop-or-go sampling lets the test end at the earliest justified point, preventing an unnecessarily large sample when the expected error rate is low.",
            "distractors": {
                "B": "Variable sampling estimates values and does not inherently minimize sample size.",
                "C": "Stratification groups the population by a characteristic; it does not stop testing early.",
                "D": "Cluster sampling draws groups of items; it is not about early stopping.",
            },
            "exam_pattern": "Minimize sample size / stop early when few errors are expected = stop-or-go sampling.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Stop-or-go sampling"],
    },
    {
        "id": "cisa-aud-r2-017", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_evidence_sampling", "difficulty": 2, "type": "mcq",
        "stem": "Which procedure gives the IS auditor the STRONGEST evidence that an automated control is operating as intended?",
        "options": [
            {"id": "A", "text": "Re-performing the control and observing the result directly"},
            {"id": "B", "text": "Asking the control owner whether the control works"},
            {"id": "C", "text": "Reading the documented control procedure"},
            {"id": "D", "text": "Accepting a management self-assessment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Re-performing the control and directly observing the outcome gives the auditor the most reliable, firsthand evidence that it operates.",
            "distractors": {
                "B": "Inquiry alone is the weakest evidence and needs corroboration.",
                "C": "A documented procedure evidences design, not that the control actually operates.",
                "D": "A self-assessment is management's assertion, not independent evidence.",
            },
            "exam_pattern": "Re-performance > observation > inquiry; proving a control OPERATES is strongest by re-performing it.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Audit evidence-gathering techniques"],
    },
    # ----- cisa_audit_reporting -----
    {
        "id": "cisa-aud-r2-018", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 3, "type": "mcq",
        "stem": "While performing fieldwork, an IS auditor uncovers evidence suggesting a possible fraud by a department supervisor. What should the auditor do FIRST?",
        "options": [
            {"id": "A", "text": "Report the matter to the appropriate level of management or the audit committee, per the organization's protocol"},
            {"id": "B", "text": "Confront the supervisor and demand an explanation"},
            {"id": "C", "text": "Begin a covert investigation and interrogate staff"},
            {"id": "D", "text": "Ignore it unless it is material to the current audit scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Suspected fraud should be escalated to the appropriate level of management (above those involved) or the audit committee, following the organization's protocol; the auditor does not investigate or confront alone.",
            "distractors": {
                "B": "Confronting the suspect can compromise evidence and the inquiry.",
                "C": "The IS auditor is not the investigator and should not run interrogations alone.",
                "D": "Suspected fraud must be escalated regardless of the original audit scope.",
            },
            "exam_pattern": "Suspected fraud -> report to appropriate management/audit committee; don't investigate or confront alone.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Irregularities, illegal acts, and reporting"],
    },
    {
        "id": "cisa-aud-r2-019", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A well-developed audit finding documents the condition, the criteria, the cause, and the effect. What does the 'criteria' element represent?",
        "options": [
            {"id": "A", "text": "The current state or problem the auditor observed"},
            {"id": "B", "text": "The standard, policy, or requirement that the condition is measured against"},
            {"id": "C", "text": "The underlying reason the problem occurred"},
            {"id": "D", "text": "The business impact or risk of the problem"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Criteria is the standard or requirement (what should be) against which the observed condition is compared.",
            "distractors": {
                "A": "That is the 'condition' (what is).",
                "C": "That is the 'cause' (why it happened).",
                "D": "That is the 'effect' (the impact or risk).",
            },
            "exam_pattern": "Finding = Condition (what is) vs Criteria (what should be) + Cause (why) + Effect (impact).",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Structure of audit findings"],
    },
    {
        "id": "cisa-aud-r2-020", "exam": "cisa", "domain": "cisa_audit_process",
        "subtopic": "cisa_audit_reporting", "difficulty": 3, "type": "mcq",
        "stem": "During follow-up, an IS auditor finds that a previously reported HIGH-risk weakness has not been remediated, and management has chosen to accept the risk. What is the auditor's BEST action?",
        "options": [
            {"id": "A", "text": "Report that the risk remains and has been formally accepted by management, escalating to senior management/the audit committee if it exceeds risk appetite"},
            {"id": "B", "text": "Remove the finding because management accepted the risk"},
            {"id": "C", "text": "Implement the fix personally to close the gap"},
            {"id": "D", "text": "Re-audit the entire original engagement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An unremediated, accepted risk is still reported; if the residual risk exceeds the organization's risk appetite, the auditor escalates to senior management or the audit committee.",
            "distractors": {
                "B": "An accepted risk is documented, not deleted from the report.",
                "C": "Remediating personally impairs independence; the fix is management's responsibility.",
                "D": "A full re-audit is disproportionate; follow-up targets the specific agreed action.",
            },
            "exam_pattern": "Unremediated high risk accepted by management -> document and escalate to governance; don't delete or fix it yourself.",
        },
        "references": ["ISACA CISA Review Manual: Domain 1 — Follow-up and residual risk acceptance"],
    },
    # ======================================================================
    # DOMAIN 2 - Governance and Management of IT
    # ======================================================================
    # ----- cisa_it_governance -----
    {
        "id": "cisa-gov-r2-001", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 3, "type": "mcq",
        "stem": "In COBIT, which activity BEST characterizes GOVERNANCE as distinct from management?",
        "options": [
            {"id": "A", "text": "Evaluating, directing, and monitoring to set direction and oversee that objectives are met"},
            {"id": "B", "text": "Planning, building, running, and monitoring day-to-day activities"},
            {"id": "C", "text": "Writing the application source code for each project"},
            {"id": "D", "text": "Staffing and operating the service desk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance (the board's role) evaluates, directs, and monitors (EDM) - setting direction and overseeing outcomes - while management plans, builds, runs, and monitors execution.",
            "distractors": {
                "B": "Plan/Build/Run/Monitor is management's role, not governance.",
                "C": "Writing code is a development activity, not governance.",
                "D": "Operating the service desk is an operational task.",
            },
            "exam_pattern": "Governance = Evaluate/Direct/Monitor (board sets direction); management = Plan/Build/Run/Monitor (executes).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Governance vs. management of enterprise IT (COBIT)"],
    },
    {
        "id": "cisa-gov-r2-002", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 2, "type": "mcq",
        "stem": "Which tool helps management measure IT performance and its alignment with business objectives across multiple perspectives rather than financial measures alone?",
        "options": [
            {"id": "A", "text": "A single server-uptime percentage"},
            {"id": "B", "text": "The IT balanced scorecard"},
            {"id": "C", "text": "The general ledger"},
            {"id": "D", "text": "A firewall rule base"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An IT balanced scorecard measures IT across several perspectives (e.g., business contribution, user, operational excellence, future orientation), linking IT performance to business goals.",
            "distractors": {
                "A": "Uptime alone is a single operational metric, not a multi-perspective measure of alignment.",
                "C": "The general ledger is a financial accounting record.",
                "D": "A firewall rule base is a technical configuration, not a performance measure.",
            },
            "exam_pattern": "Multi-perspective measurement of IT performance/alignment = IT balanced scorecard.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT balanced scorecard"],
    },
    {
        "id": "cisa-gov-r2-003", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of an enterprise architecture (EA)?",
        "options": [
            {"id": "A", "text": "To provide a blueprint that aligns IT structure, data, and technology standards with business strategy"},
            {"id": "B", "text": "To schedule nightly data backups"},
            {"id": "C", "text": "To encrypt the production databases"},
            {"id": "D", "text": "To staff the help desk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An enterprise architecture is the blueprint that keeps the organization's IT structure, data, and technology standards aligned with and supporting business strategy.",
            "distractors": {
                "B": "Backup scheduling is an operations task, not the purpose of EA.",
                "C": "Encryption is a control, not an architecture blueprint.",
                "D": "Help-desk staffing is an operational function.",
            },
            "exam_pattern": "EA = the blueprint that keeps IT standards/structure aligned with business strategy.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Enterprise architecture"],
    },
    {
        "id": "cisa-gov-r2-004", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_governance", "difficulty": 2, "type": "mcq",
        "stem": "An organization rates each IT process on a scale from 'initial/ad hoc' to 'optimized'. This is an example of using a:",
        "options": [
            {"id": "A", "text": "Penetration test"},
            {"id": "B", "text": "Capability maturity model"},
            {"id": "C", "text": "Data flow diagram"},
            {"id": "D", "text": "Backup rotation scheme"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A capability maturity model rates process maturity on a graded scale (e.g., initial, repeatable, defined, managed, optimized), helping identify improvement priorities.",
            "distractors": {
                "A": "A penetration test probes security weaknesses, not process maturity.",
                "C": "A data flow diagram models how data moves through a system.",
                "D": "A backup rotation scheme is an operations control.",
            },
            "exam_pattern": "Rating process maturity (initial -> optimized) = capability maturity model.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Process maturity models"],
    },
    # ----- cisa_it_strategy_policies -----
    {
        "id": "cisa-gov-r2-005", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "Which type of governance document specifies a MANDATORY, uniform rule - such as requiring a specific minimum encryption algorithm on all laptops?",
        "options": [
            {"id": "A", "text": "Guideline"},
            {"id": "B", "text": "Policy"},
            {"id": "C", "text": "Standard"},
            {"id": "D", "text": "Procedure"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A standard is a mandatory, specific, uniform rule (e.g., a required technology or configuration) that implements a policy.",
            "distractors": {
                "A": "A guideline is a recommended, non-mandatory practice.",
                "B": "A policy states high-level management intent, not a specific mandatory rule.",
                "D": "A procedure is the step-by-step how-to, not the mandatory rule itself.",
            },
            "exam_pattern": "Mandatory, specific, uniform rule/technology = standard (policy=intent, procedure=steps, guideline=optional).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Standards vs. policies, procedures, guidelines"],
    },
    {
        "id": "cisa-gov-r2-006", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "The IT strategic plan should be derived PRIMARILY from:",
        "options": [
            {"id": "A", "text": "The organization's business/corporate strategy"},
            {"id": "B", "text": "The newest available technology trends"},
            {"id": "C", "text": "The preferences of the IT staff"},
            {"id": "D", "text": "The external auditor's recommendations"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IT strategy must flow from and align with the business/corporate strategy so IT investments support enterprise objectives.",
            "distractors": {
                "B": "Chasing the newest technology is not the same as aligning with business goals.",
                "C": "Staff preference is not a strategic basis.",
                "D": "The auditor advises on controls but does not set IT strategy.",
            },
            "exam_pattern": "IT strategy must flow from (align with) the business strategy.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT strategy alignment"],
    },
    {
        "id": "cisa-gov-r2-007", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "To ensure IT investments reflect business priorities, an IT steering committee should include:",
        "options": [
            {"id": "A", "text": "Only IT staff"},
            {"id": "B", "text": "Only external vendors"},
            {"id": "C", "text": "Representatives from business/user units as well as senior IT management"},
            {"id": "D", "text": "Only junior developers"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A steering committee should be cross-functional - business/user representatives plus senior IT management - so IT delivery reflects business needs and priorities.",
            "distractors": {
                "A": "An IT-only committee loses the business voice that prioritization requires.",
                "B": "Vendors have commercial conflicts and should not set internal priorities.",
                "D": "Junior developers lack the authority to set investment priorities.",
            },
            "exam_pattern": "Steering committee = cross-functional (business + senior IT) so IT serves business needs.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — IT steering committee composition"],
    },
    {
        "id": "cisa-gov-r2-008", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_it_strategy_policies", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor notes the information security policy has not been reviewed or updated in five years. What is the GREATEST concern?",
        "options": [
            {"id": "A", "text": "The document uses an outdated font"},
            {"id": "B", "text": "The policy is too short"},
            {"id": "C", "text": "Employees have already read it"},
            {"id": "D", "text": "It may no longer address current threats, technologies, and regulatory requirements"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Policies must be reviewed periodically; a stale policy may fail to cover current threats, technology, and regulations, leaving gaps.",
            "distractors": {
                "A": "Font choice is irrelevant to the control.",
                "B": "Length is not the issue; relevance is.",
                "C": "Employees reading the policy is a good thing, not a concern.",
            },
            "exam_pattern": "Policies must be reviewed periodically - a stale policy may not cover current risks/regulations.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Policy lifecycle and review"],
    },
    # ----- cisa_org_structure -----
    {
        "id": "cisa-gov-r2-009", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 3, "type": "mcq",
        "stem": "Which combination of duties performed by ONE person represents the GREATEST segregation-of-duties concern?",
        "options": [
            {"id": "A", "text": "Answering the help desk and writing user documentation"},
            {"id": "B", "text": "Authorizing payments and reconciling the bank account that records them"},
            {"id": "C", "text": "Running two different management reports"},
            {"id": "D", "text": "Attending two project meetings"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "One person who both authorizes/executes payments and reconciles the account can commit and then conceal a fraud - the classic incompatible-duties conflict.",
            "distractors": {
                "A": "Help desk and documentation are compatible, low-risk duties.",
                "C": "Running reports is not a conflicting combination of duties.",
                "D": "Attending meetings is not a duties conflict.",
            },
            "exam_pattern": "One person who both authorizes/executes AND reconciles/records can commit and hide fraud - incompatible.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Segregation of incompatible duties"],
    },
    {
        "id": "cisa-gov-r2-010", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 2, "type": "mcq",
        "stem": "A data custodian (such as IT operations) is PRIMARILY responsible for:",
        "options": [
            {"id": "A", "text": "Assigning the data's classification level"},
            {"id": "B", "text": "Setting the organization's risk appetite"},
            {"id": "C", "text": "Implementing and maintaining protection controls (backups, access enforcement) as directed by the data owner"},
            {"id": "D", "text": "Approving the IT budget"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The custodian safeguards the data day to day - implementing and maintaining the controls (backup, access enforcement) that the owner specifies.",
            "distractors": {
                "A": "Classifying data is the data owner's responsibility.",
                "B": "Risk appetite is set by senior management.",
                "D": "Budget approval is a management decision, not a custodian task.",
            },
            "exam_pattern": "Owner classifies/authorizes; custodian safeguards and maintains controls as directed.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Data owner vs. custodian"],
    },
    {
        "id": "cisa-gov-r2-011", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 3, "type": "mcq",
        "stem": "To avoid a conflict of interest, the information security function should ideally be organizationally independent of:",
        "options": [
            {"id": "A", "text": "The legal department"},
            {"id": "B", "text": "The marketing team"},
            {"id": "C", "text": "External customers"},
            {"id": "D", "text": "IT operations and development, whose activities it must oversee"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Security should not report into the IT operations/development functions it is meant to oversee, or it would be judging its own masters - a self-oversight conflict.",
            "distractors": {
                "A": "Legal does not create the self-oversight conflict that reporting into IT ops/dev does.",
                "B": "Marketing is unrelated to the security-oversight conflict.",
                "C": "Customers are external and not part of the reporting line.",
            },
            "exam_pattern": "Security shouldn't report to the IT functions it polices (self-oversight conflict of interest).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Organizational placement of the security function"],
    },
    {
        "id": "cisa-gov-r2-012", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_org_structure", "difficulty": 3, "type": "mcq",
        "stem": "A policy requiring employees in sensitive positions to take at least one continuous week of vacation each year functions PRIMARILY as a control to:",
        "options": [
            {"id": "A", "text": "Improve employee morale only"},
            {"id": "B", "text": "Detect fraud or irregularities that require the employee's ongoing presence to conceal"},
            {"id": "C", "text": "Reduce payroll costs"},
            {"id": "D", "text": "Speed up transaction processing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mandatory vacation (like job rotation) forces an absence during which another person operates the role, surfacing fraud that needs the perpetrator present to stay hidden.",
            "distractors": {
                "A": "Morale may improve, but that is not the control's purpose.",
                "C": "Mandatory vacation does not reduce payroll costs.",
                "D": "It does not speed up processing.",
            },
            "exam_pattern": "Mandatory vacation / job rotation surfaces fraud that needs the perpetrator present to hide it.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Mandatory vacation and job rotation"],
    },
    # ----- cisa_risk_management -----
    {
        "id": "cisa-gov-r2-013", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 1, "type": "mcq",
        "stem": "An organization decides NOT to launch a new online service because the associated security risk is judged too high. Which risk response is this?",
        "options": [
            {"id": "A", "text": "Risk acceptance"},
            {"id": "B", "text": "Risk transfer"},
            {"id": "C", "text": "Risk mitigation"},
            {"id": "D", "text": "Risk avoidance"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Choosing not to undertake the risky activity at all is risk avoidance.",
            "distractors": {
                "A": "Acceptance means proceeding and retaining the risk.",
                "B": "Transfer shifts the impact to a third party (e.g., insurance).",
                "C": "Mitigation reduces the risk with controls but still proceeds.",
            },
            "exam_pattern": "Decline the risky activity entirely = avoidance (accept=retain, transfer=shift, mitigate=reduce).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Risk response options"],
    },
    {
        "id": "cisa-gov-r2-014", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "In quantitative risk analysis, which value represents the expected annual monetary loss from a specific risk, calculated as single loss expectancy multiplied by the annualized rate of occurrence?",
        "options": [
            {"id": "A", "text": "Annual loss expectancy (ALE)"},
            {"id": "B", "text": "Exposure factor"},
            {"id": "C", "text": "Residual risk"},
            {"id": "D", "text": "Risk appetite"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ALE = SLE x ARO, the expected yearly monetary loss used to compare risks and justify control spending.",
            "distractors": {
                "B": "The exposure factor is the percentage of asset value lost per event, not the annual loss.",
                "C": "Residual risk is what remains after controls, not a loss figure.",
                "D": "Risk appetite is the level of risk tolerated, not a calculated loss.",
            },
            "exam_pattern": "ALE = SLE x ARO (expected yearly loss); SLE = asset value x exposure factor.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Quantitative risk analysis (ALE/SLE/ARO)"],
    },
    {
        "id": "cisa-gov-r2-015", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "Which metric is designed to give management an EARLY WARNING that risk exposure is rising toward an unacceptable level?",
        "options": [
            {"id": "A", "text": "A throughput key performance indicator (KPI)"},
            {"id": "B", "text": "A key risk indicator (KRI)"},
            {"id": "C", "text": "A profit margin"},
            {"id": "D", "text": "A help-desk satisfaction score"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A key risk indicator is a forward-looking metric that signals increasing risk exposure before it becomes a loss.",
            "distractors": {
                "A": "A throughput KPI measures performance, not risk.",
                "C": "Profit margin is a financial outcome, not a risk early-warning.",
                "D": "A satisfaction score measures service quality, not risk.",
            },
            "exam_pattern": "Early-warning signal of increasing risk = key risk indicator (KRI).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Key risk indicators"],
    },
    {
        "id": "cisa-gov-r2-016", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "When reliable monetary loss data is not available, which risk-analysis approach is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Quantitative analysis requiring precise dollar figures"},
            {"id": "B", "text": "No analysis at all"},
            {"id": "C", "text": "Qualitative analysis using ratings such as high/medium/low"},
            {"id": "D", "text": "Waiting until a loss actually occurs"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When hard monetary data is lacking, qualitative analysis uses relative ratings (high/medium/low likelihood and impact) to prioritize risks.",
            "distractors": {
                "A": "Quantitative analysis needs the monetary data that is unavailable here.",
                "B": "Skipping analysis leaves risk unmanaged.",
                "D": "Waiting for a loss is reactive, not analysis.",
            },
            "exam_pattern": "No hard dollar data -> qualitative (relative) rating; precise dollar impact -> quantitative.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Qualitative vs. quantitative risk analysis"],
    },
    # ----- cisa_bcp -----
    {
        "id": "cisa-gov-r2-017", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 3, "type": "mcq",
        "stem": "How does the recovery time objective (RTO) relate to the maximum tolerable downtime (MTD) for a business process?",
        "options": [
            {"id": "A", "text": "The RTO must be less than or equal to the MTD"},
            {"id": "B", "text": "The RTO must always exceed the MTD"},
            {"id": "C", "text": "They are unrelated measures"},
            {"id": "D", "text": "The MTD must always be zero"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recovery must complete within the maximum downtime the business can tolerate, so the RTO must be set at or below the MTD.",
            "distractors": {
                "B": "An RTO exceeding the MTD means recovery is too slow to be tolerable.",
                "C": "They are directly related - RTO is bounded by MTD.",
                "D": "MTD is rarely zero; it reflects how long the process can be down.",
            },
            "exam_pattern": "RTO (planned recovery time) must fit within MTD (max downtime the business can bear).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — MTD, RTO, and recovery objectives"],
    },
    {
        "id": "cisa-gov-r2-018", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 2, "type": "mcq",
        "stem": "Which statement BEST distinguishes a business continuity plan (BCP) from a disaster recovery plan (DRP)?",
        "options": [
            {"id": "A", "text": "They are identical documents"},
            {"id": "B", "text": "The DRP is broader than the BCP"},
            {"id": "C", "text": "The BCP covers only IT systems"},
            {"id": "D", "text": "The BCP addresses keeping the whole business (people, processes, facilities) operating, while the DRP focuses on recovering IT systems and infrastructure"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The BCP is the broad plan to keep the business functioning; the DRP is the IT-focused subset that restores systems and infrastructure.",
            "distractors": {
                "A": "They are related but not identical.",
                "B": "The BCP is the broader of the two, not the DRP.",
                "C": "The BCP spans people, processes, and facilities, not IT alone.",
            },
            "exam_pattern": "BCP = keep the business running (broad); DRP = restore IT (a subset of BCP).",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — Business continuity vs. disaster recovery"],
    },
    {
        "id": "cisa-gov-r2-019", "exam": "cisa", "domain": "cisa_governance",
        "subtopic": "cisa_bcp", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor reviewing business continuity would be MOST concerned to find that the BCP:",
        "options": [
            {"id": "A", "text": "Is stored in a shared document library"},
            {"id": "B", "text": "References the current organization chart"},
            {"id": "C", "text": "Has never been tested or updated since it was first written"},
            {"id": "D", "text": "Includes staff contact lists"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An untested, outdated BCP may fail when invoked; continuity plans must be tested and maintained to stay effective.",
            "distractors": {
                "A": "A shared library is reasonable storage (ideally with an accessible offsite copy).",
                "B": "A current org chart is a sign the plan is maintained - good, not a concern.",
                "D": "Contact lists are expected, useful plan content.",
            },
            "exam_pattern": "An untested, outdated BCP may fail when needed - test and maintain it.",
        },
        "references": ["ISACA CISA Review Manual: Domain 2 — BCP testing and maintenance"],
    },
    # ======================================================================
    # DOMAIN 3 - IS Acquisition, Development and Implementation
    # ======================================================================
    # ----- cisa_project_management -----
    {
        "id": "cisa-acq-r2-001", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 3, "type": "mcq",
        "stem": "Using PERT with an optimistic estimate (O), most likely estimate (M), and pessimistic estimate (P), the expected activity duration is calculated as:",
        "options": [
            {"id": "A", "text": "(O + 4M + P) / 6"},
            {"id": "B", "text": "(O + M + P) / 3"},
            {"id": "C", "text": "(O + P) / 2"},
            {"id": "D", "text": "The largest of O, M, and P"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PERT weights the most likely estimate four times: expected time = (O + 4M + P) / 6.",
            "distractors": {
                "B": "A simple average ignores the extra weight on the most likely estimate.",
                "C": "The midpoint of O and P ignores M entirely.",
                "D": "Taking the maximum is overly pessimistic and not the PERT formula.",
            },
            "exam_pattern": "PERT expected time = (O + 4M + P) / 6 (the most likely estimate is weighted x4).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — PERT estimation"],
    },
    {
        "id": "cisa-acq-r2-002", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 2, "type": "mcq",
        "stem": "Which project tool shows tasks as horizontal bars along a timeline and is used mainly to track progress against the schedule?",
        "options": [
            {"id": "A", "text": "A Gantt chart"},
            {"id": "B", "text": "A data flow diagram"},
            {"id": "C", "text": "An entity-relationship diagram"},
            {"id": "D", "text": "A decision table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Gantt chart plots tasks as bars on a timeline, making it easy to track schedule and progress (though it does not highlight the critical path the way a network diagram does).",
            "distractors": {
                "B": "A data flow diagram models how data moves through a system.",
                "C": "An entity-relationship diagram models data relationships.",
                "D": "A decision table maps conditions to actions.",
            },
            "exam_pattern": "Bars on a timeline for scheduling/progress = Gantt chart.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Project scheduling tools (Gantt)"],
    },
    {
        "id": "cisa-acq-r2-003", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 3, "type": "mcq",
        "stem": "A task that lies ON the critical path is delayed by three days. Assuming no corrective action, what is the effect?",
        "options": [
            {"id": "A", "text": "There is no effect because the task has slack"},
            {"id": "B", "text": "The entire project's completion is delayed by three days"},
            {"id": "C", "text": "The project finishes earlier"},
            {"id": "D", "text": "Only non-critical tasks are affected"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Critical-path tasks have zero float, so any delay to them pushes out the whole project's completion by the same amount.",
            "distractors": {
                "A": "Critical-path tasks have zero slack/float by definition.",
                "C": "A delay cannot make the project finish earlier.",
                "D": "A critical-path delay affects the overall project end date, not just non-critical tasks.",
            },
            "exam_pattern": "Critical-path tasks have zero float - any delay to them delays the whole project.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Critical path and float"],
    },
    {
        "id": "cisa-acq-r2-004", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 3, "type": "mcq",
        "stem": "Which technique measures whether a project is on schedule and within budget by comparing the planned value, earned value, and actual cost of work?",
        "options": [
            {"id": "A", "text": "Earned value management"},
            {"id": "B", "text": "Function point analysis"},
            {"id": "C", "text": "A feasibility study"},
            {"id": "D", "text": "A structured walkthrough"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Earned value management integrates scope, schedule, and cost by comparing planned value, earned value, and actual cost to show schedule and cost performance.",
            "distractors": {
                "B": "Function point analysis sizes software; it does not track schedule/cost performance.",
                "C": "A feasibility study assesses viability up front, not ongoing performance.",
                "D": "A structured walkthrough is a review technique, not a performance measure.",
            },
            "exam_pattern": "Integrated schedule+cost performance (planned vs earned vs actual) = earned value management.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Earned value management"],
    },
    # ----- cisa_sdlc -----
    {
        "id": "cisa-acq-r2-005", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "When user requirements are unclear or evolving, which development approach builds successive working models for users to react to and refine?",
        "options": [
            {"id": "A", "text": "The traditional waterfall model"},
            {"id": "B", "text": "Prototyping"},
            {"id": "C", "text": "Big-bang integration"},
            {"id": "D", "text": "Direct cutover"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Prototyping iteratively builds working models that users evaluate, clarifying unclear or evolving requirements before full build.",
            "distractors": {
                "A": "Waterfall fixes requirements up front and suits well-understood needs.",
                "C": "Big-bang integration is a testing/integration approach, not a requirements technique.",
                "D": "Direct cutover is a system conversion strategy.",
            },
            "exam_pattern": "Unclear/evolving requirements -> iterative prototyping to refine with users.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — SDLC approaches (prototyping)"],
    },
    {
        "id": "cisa-acq-r2-006", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 3, "type": "mcq",
        "stem": "When auditing a project using agile/rapid development, what is the IS auditor's PRIMARY concern?",
        "options": [
            {"id": "A", "text": "That the team holds daily stand-up meetings"},
            {"id": "B", "text": "That software is delivered in increments"},
            {"id": "C", "text": "That speed and reduced formality may weaken documentation, controls, and audit trails"},
            {"id": "D", "text": "That users are involved frequently"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Agile/RAD's speed and lighter ceremony can erode documentation, controls, and traceability; the auditor verifies that adequate controls and audit trails still exist.",
            "distractors": {
                "A": "Daily stand-ups are a normal, beneficial agile practice.",
                "B": "Incremental delivery is a feature of agile, not a concern.",
                "D": "Frequent user involvement is a strength of agile.",
            },
            "exam_pattern": "Agile/RAD's risk to the auditor = lighter documentation/controls - confirm controls and traceability remain.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Agile/RAD and control considerations"],
    },
    {
        "id": "cisa-acq-r2-007", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "An organization licenses critical software from a small vendor and worries the vendor could go out of business. Which arrangement BEST protects its ability to maintain the software?",
        "options": [
            {"id": "A", "text": "A longer payment term"},
            {"id": "B", "text": "A bigger marketing budget"},
            {"id": "C", "text": "A faster internet connection"},
            {"id": "D", "text": "A source code escrow agreement with a trusted third party"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A source code escrow holds the source with a neutral third party, released to the licensee on defined triggers (e.g., vendor bankruptcy) so the software can be maintained.",
            "distractors": {
                "A": "Payment terms do not secure access to the source code.",
                "B": "Marketing budget is irrelevant to this risk.",
                "C": "Bandwidth has nothing to do with vendor failure.",
            },
            "exam_pattern": "Vendor-failure protection for licensed software = source code escrow (released on defined triggers).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Software acquisition and source code escrow"],
    },
    {
        "id": "cisa-acq-r2-008", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "Which type of testing examines the internal logic and code paths of a program, requiring knowledge of its internal structure?",
        "options": [
            {"id": "A", "text": "Black-box testing"},
            {"id": "B", "text": "White-box testing"},
            {"id": "C", "text": "User acceptance testing"},
            {"id": "D", "text": "Parallel testing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "White-box testing inspects internal logic and code paths, so it requires knowledge of the program's internal structure.",
            "distractors": {
                "A": "Black-box testing checks functionality without knowledge of internal code.",
                "C": "User acceptance testing validates business requirements from the user's perspective.",
                "D": "Parallel testing is a system conversion method, not a code-logic test.",
            },
            "exam_pattern": "Internal logic/code = white-box; external behavior without internals = black-box.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Testing methods (white-box vs. black-box)"],
    },
    # ----- cisa_system_migration -----
    {
        "id": "cisa-acq-r2-009", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "Which conversion strategy introduces the new system gradually, module by module or location by location, over time?",
        "options": [
            {"id": "A", "text": "Phased changeover"},
            {"id": "B", "text": "Direct (big-bang) changeover"},
            {"id": "C", "text": "Parallel changeover"},
            {"id": "D", "text": "No changeover"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A phased changeover rolls the new system out incrementally (by module or site), lowering risk per step but taking longer and requiring old/new interfaces during transition.",
            "distractors": {
                "B": "Direct/big-bang switches everything at once.",
                "C": "Parallel runs the old and new systems together for comparison.",
                "D": "'No changeover' is not a strategy.",
            },
            "exam_pattern": "Gradual, incremental rollout = phased changeover (lower risk than big-bang, but longer).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Changeover strategies (phased)"],
    },
    {
        "id": "cisa-acq-r2-010", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "An organization deploys a new system to one branch office first to validate it before rolling it out company-wide. This conversion approach is:",
        "options": [
            {"id": "A", "text": "Parallel changeover"},
            {"id": "B", "text": "Pilot changeover"},
            {"id": "C", "text": "Direct changeover across all sites at once"},
            {"id": "D", "text": "Big-bang conversion"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A pilot changeover proves the system at one site/group first, containing risk before an organization-wide rollout.",
            "distractors": {
                "A": "Parallel runs the old and new systems together, not a single trial site.",
                "C": "Direct changeover deploys everywhere at once with no trial site.",
                "D": "Big-bang conversion switches the whole organization simultaneously.",
            },
            "exam_pattern": "Try it at one site/group first, then expand = pilot conversion.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Changeover strategies (pilot)"],
    },
    {
        "id": "cisa-acq-r2-011", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "Before migrating data from a legacy system, the project cleans up duplicate, incomplete, and inconsistent records. What is the PRIMARY purpose of this data-cleansing step?",
        "options": [
            {"id": "A", "text": "To prevent carrying poor-quality 'garbage' data into the new system"},
            {"id": "B", "text": "To encrypt the data in transit"},
            {"id": "C", "text": "To speed up the office network"},
            {"id": "D", "text": "To train the end users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cleansing corrects duplicates and errors in legacy data so poor-quality data is not migrated into the new system (garbage in, garbage out).",
            "distractors": {
                "B": "Encryption is a confidentiality control, not the goal of cleansing.",
                "C": "Network speed is unrelated to data cleansing.",
                "D": "User training is a separate implementation activity.",
            },
            "exam_pattern": "Clean legacy data before migration so errors/duplicates aren't carried forward.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Data migration and cleansing"],
    },
    # ----- cisa_post_implementation -----
    {
        "id": "cisa-acq-r2-012", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 2, "type": "mcq",
        "stem": "A post-implementation review should compare the system's actual results PRIMARILY against:",
        "options": [
            {"id": "A", "text": "The costs, benefits, and objectives projected in the original business case"},
            {"id": "B", "text": "The preferences of the development team"},
            {"id": "C", "text": "The newest industry technology trends"},
            {"id": "D", "text": "The vendor's marketing claims"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A PIR measures the live system's actual costs, benefits, and performance against the original business case that justified the project.",
            "distractors": {
                "B": "Team preference is not the approved baseline.",
                "C": "Industry trends are not the project's success criteria.",
                "D": "Marketing claims are not an objective benchmark.",
            },
            "exam_pattern": "PIR measures actual outcomes against the original business case (planned costs/benefits/objectives).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Post-implementation review and benefits"],
    },
    {
        "id": "cisa-acq-r2-013", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 3, "type": "mcq",
        "stem": "When an IS auditor participates in a post-implementation review, the auditor is PRIMARILY concerned with whether:",
        "options": [
            {"id": "A", "text": "The launch event was well attended"},
            {"id": "B", "text": "Adequate controls were built into the delivered system and the system met its objectives"},
            {"id": "C", "text": "The developers enjoyed the project"},
            {"id": "D", "text": "The system uses the latest framework"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The IS auditor's PIR focus is whether adequate controls are present and operating and whether the system achieved its intended objectives and benefits.",
            "distractors": {
                "A": "Event attendance is irrelevant to control adequacy.",
                "C": "Team satisfaction does not evidence controls or benefits.",
                "D": "Using the latest framework is not the audit concern.",
            },
            "exam_pattern": "In a PIR, the auditor focuses on control adequacy and whether objectives/benefits were achieved.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Auditor's role in post-implementation review"],
    },
    # ======================================================================
    # DOMAIN 4 - IS Operations and Business Resilience
    # ======================================================================
    # ----- cisa_it_operations -----
    {
        "id": "cisa-ops-r2-001", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "Which control BEST ensures that only authorized, tested program changes are moved into production?",
        "options": [
            {"id": "A", "text": "Changes are approved through change management and migrated by someone other than the developer who wrote them"},
            {"id": "B", "text": "Developers move their own changes whenever convenient"},
            {"id": "C", "text": "Changes are applied directly to production and documented only if problems arise"},
            {"id": "D", "text": "No approval is required for small changes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authorized and tested changes migrated by someone other than the developer enforces both change control and segregation of duties between development and production.",
            "distractors": {
                "B": "Developers promoting their own code breaks segregation of duties.",
                "C": "Applying changes directly and documenting only on failure is uncontrolled.",
                "D": "'No approval for small changes' is a loophole that undermines change control.",
            },
            "exam_pattern": "Authorized + tested + segregated migration (developer doesn't promote own code) = sound change control.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Change and release management controls"],
    },
    {
        "id": "cisa-ops-r2-002", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "What is the GREATEST risk of applying vendor security patches directly to production systems without testing them first?",
        "options": [
            {"id": "A", "text": "The systems will become more secure"},
            {"id": "B", "text": "A patch could introduce incompatibilities that disrupt or crash production services"},
            {"id": "C", "text": "The vendor will revoke support"},
            {"id": "D", "text": "The patch will install faster"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An untested patch may be incompatible and destabilize or crash production; patches should be tested in a non-production environment first.",
            "distractors": {
                "A": "Added security is the goal, not a risk.",
                "C": "Vendors do not revoke support simply for applying patches.",
                "D": "Install speed is not a meaningful risk.",
            },
            "exam_pattern": "Patch untested in production -> risk of outages/instability; test patches before deployment.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Patch management"],
    },
    {
        "id": "cisa-ops-r2-003", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor wants assurance that scheduled batch jobs complete successfully and that failures are handled. The BEST evidence is:",
        "options": [
            {"id": "A", "text": "A verbal assurance from an operator"},
            {"id": "B", "text": "The brand of the job-scheduling software"},
            {"id": "C", "text": "Review of the job schedule and exception/error logs showing failures are detected and reruns are performed"},
            {"id": "D", "text": "The color of the operations console screen"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reviewing the job schedule and exception logs provides objective evidence that failed jobs are detected, escalated, and rerun.",
            "distractors": {
                "A": "A verbal assurance is weak, uncorroborated evidence.",
                "B": "The software brand says nothing about whether jobs complete.",
                "D": "Screen color is irrelevant.",
            },
            "exam_pattern": "Batch assurance = review the schedule and exception logs for detection and rerun of failed jobs.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Job scheduling and batch monitoring"],
    },
    {
        "id": "cisa-ops-r2-004", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a configuration management database (CMDB)?",
        "options": [
            {"id": "A", "text": "To maintain accurate records of IT assets (configuration items) and their relationships to support change and incident management"},
            {"id": "B", "text": "To store user passwords"},
            {"id": "C", "text": "To back up application data"},
            {"id": "D", "text": "To filter inbound network traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CMDB is the authoritative inventory of configuration items and their relationships, supporting change, incident, and problem management.",
            "distractors": {
                "B": "Passwords belong in an identity/credential store, not the CMDB.",
                "C": "Data backup is a separate function.",
                "D": "Traffic filtering is a firewall role.",
            },
            "exam_pattern": "CMDB = authoritative inventory of configuration items and their relationships.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Configuration management"],
    },
    {
        "id": "cisa-ops-r2-005", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor finds that a critical financial report is produced by a complex end-user spreadsheet maintained by one analyst. What is the GREATEST concern?",
        "options": [
            {"id": "A", "text": "The spreadsheet uses color formatting"},
            {"id": "B", "text": "The analyst sometimes works from home"},
            {"id": "C", "text": "The spreadsheet lacks the change control, testing, and validation applied to formal applications, risking undetected errors"},
            {"id": "D", "text": "The file has a long name"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "User-developed spreadsheets driving key decisions typically lack formal change control, testing, and validation, so errors can go undetected - a data-integrity risk.",
            "distractors": {
                "A": "Formatting is not a control weakness.",
                "B": "Remote work is not the core concern.",
                "D": "The file name is irrelevant.",
            },
            "exam_pattern": "End-user spreadsheets driving key decisions lack formal controls (change/test/validation) - a data-integrity risk.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — End-user computing controls"],
    },
    # ----- cisa_system_interfaces -----
    {
        "id": "cisa-ops-r2-006", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 3, "type": "mcq",
        "stem": "In an electronic data interchange (EDI) environment, which control BEST provides assurance that inbound trading-partner transactions are complete and were not lost?",
        "options": [
            {"id": "A", "text": "Using a colorful user interface"},
            {"id": "B", "text": "Transmitting functional acknowledgments and reconciling control totals for each batch received"},
            {"id": "C", "text": "Storing messages in a larger database"},
            {"id": "D", "text": "Printing each message"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Functional acknowledgments confirm receipt, and reconciling control totals confirms that every transaction in a batch was received and processed - completeness.",
            "distractors": {
                "A": "UI appearance does not assure completeness.",
                "C": "Database size is irrelevant to transaction completeness.",
                "D": "Printing messages does not reconcile what was sent versus received.",
            },
            "exam_pattern": "EDI completeness = functional acknowledgments + control-total reconciliation at receipt.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — EDI controls"],
    },
    {
        "id": "cisa-ops-r2-007", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The input control that detects transposition and transcription errors in a key field (such as an account number) by appending a calculated extra digit is called a check ______.",
        "correct": ["digit", "check digit"],
        "explanation": {
            "correct": "A check digit is a digit computed from the other digits of a key field; if the field is mis-keyed or transposed, the recomputed check digit will not match, flagging the error.",
            "distractors": {},
            "exam_pattern": "Catch mis-keyed/transposed digits in an identifier = check digit.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Input/edit controls (check digit)"],
    },
    {
        "id": "cisa-ops-r2-008", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 3, "type": "mcq",
        "stem": "A batch process sums the account-number field of all records (a total with no intrinsic meaning) and compares it before and after transfer. This control is a:",
        "options": [
            {"id": "A", "text": "Hash total"},
            {"id": "B", "text": "Check digit"},
            {"id": "C", "text": "Parity bit"},
            {"id": "D", "text": "Digital signature"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hash total is a meaningless control sum of a field (e.g., account numbers) used only to verify that the batch is complete and unchanged between sender and receiver.",
            "distractors": {
                "B": "A check digit validates a single field's keystrokes, not batch completeness.",
                "C": "A parity bit detects single-bit transmission errors, not batch totals.",
                "D": "A digital signature provides authentication/non-repudiation, not batch completeness.",
            },
            "exam_pattern": "A meaningless control sum over a field to prove batch completeness = hash total.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Batch/processing controls (hash totals)"],
    },
    {
        "id": "cisa-ops-r2-009", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 2, "type": "mcq",
        "stem": "An application rejects any entry for 'hours worked in a week' that is greater than 168. Which type of input validation is this?",
        "options": [
            {"id": "A", "text": "A check digit"},
            {"id": "B", "text": "A hash total"},
            {"id": "C", "text": "A range (limit) check"},
            {"id": "D", "text": "A referential integrity check"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A range (limit) check verifies that a value falls within predefined bounds - here, that weekly hours cannot exceed 168.",
            "distractors": {
                "A": "A check digit validates an identifier's keystrokes, not a value's reasonableness.",
                "B": "A hash total verifies batch completeness, not a single value's range.",
                "D": "Referential integrity enforces key relationships in a database.",
            },
            "exam_pattern": "Value must fall within predefined bounds = range/limit check.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Input validation (range/limit checks)"],
    },
    # ----- cisa_data_backup_recovery -----
    {
        "id": "cisa-ops-r2-010", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "An organization performs a weekly full backup and daily incremental backups. To fully restore after a Thursday failure, what must be applied?",
        "options": [
            {"id": "A", "text": "The last full backup plus every incremental taken since, applied in order"},
            {"id": "B", "text": "Only the last full backup"},
            {"id": "C", "text": "Only the most recent incremental"},
            {"id": "D", "text": "The last full plus the single most recent incremental"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Incremental backups each capture changes since the previous backup, so a full restore needs the last full plus all subsequent incrementals applied in sequence.",
            "distractors": {
                "B": "The full alone misses all the daily changes since.",
                "C": "A single incremental misses the earlier days' changes.",
                "D": "'Full + one incremental' describes a differential scheme, not incremental.",
            },
            "exam_pattern": "Incremental restore = last FULL + ALL incrementals in order (fast backup, slower/complex restore).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Backup types and restoration"],
    },
    {
        "id": "cisa-ops-r2-011", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "Which statement about the archive bit is correct?",
        "options": [
            {"id": "A", "text": "An incremental backup clears (resets) the archive bit, whereas a differential backup leaves it set"},
            {"id": "B", "text": "Both incremental and differential backups clear it"},
            {"id": "C", "text": "Neither incremental nor differential backups touch it"},
            {"id": "D", "text": "Only a differential backup clears it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Incremental backups clear the archive bit (so the next incremental only grabs new changes), while differentials leave it set - which is why differentials keep growing until the next full backup.",
            "distractors": {
                "B": "A differential does not clear the archive bit.",
                "C": "Both types read the archive bit, and incremental resets it.",
                "D": "It is the incremental, not the differential, that clears the bit.",
            },
            "exam_pattern": "Incremental CLEARS the archive bit; differential does NOT - so differentials accumulate changes since the last full.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Backup mechanics (archive bit)"],
    },
    {
        "id": "cisa-ops-r2-012", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "An administrator argues that RAID 5 on the server makes backups unnecessary. Why should the IS auditor disagree?",
        "options": [
            {"id": "A", "text": "RAID protects against disk hardware failure but not against data corruption, accidental deletion, ransomware, or site disaster"},
            {"id": "B", "text": "RAID encrypts all stored data"},
            {"id": "C", "text": "RAID automatically stores copies offsite"},
            {"id": "D", "text": "RAID eliminates the need for a UPS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RAID provides disk fault tolerance/availability, but it faithfully replicates corruption, deletions, and ransomware, and offers no protection against site disaster - so it is not a substitute for backups.",
            "distractors": {
                "B": "RAID does not encrypt data.",
                "C": "RAID does not provide offsite copies.",
                "D": "RAID is unrelated to power protection.",
            },
            "exam_pattern": "RAID = disk fault tolerance/availability, NOT a backup (no protection from deletion/corruption/disaster).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — RAID vs. backup"],
    },
    {
        "id": "cisa-ops-r2-013", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "Which technique transmits database transaction logs to an offsite location in near real time to minimize data loss (a very small RPO)?",
        "options": [
            {"id": "A", "text": "Remote journaling"},
            {"id": "B", "text": "Monthly tape rotation to a local cabinet"},
            {"id": "C", "text": "An annual full backup only"},
            {"id": "D", "text": "Printing reports nightly"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Remote journaling streams transaction LOGS offsite in near real time, so very little data is lost if the primary site fails - a small RPO. (It differs from electronic vaulting, which transfers bulk backup data in periodic batches, and from database shadowing, which keeps a real-time duplicate.)",
            "distractors": {
                "B": "Monthly local tapes leave a large data-loss window and sit at the primary location.",
                "C": "An annual backup leaves an enormous RPO.",
                "D": "Printing reports is not a data-recovery mechanism.",
            },
            "exam_pattern": "Near-real-time offsite transaction logs = remote journaling -> small RPO (electronic vaulting = periodic batch transfer; database shadowing = real-time duplicate).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Electronic vaulting and remote journaling"],
    },
    {
        "id": "cisa-ops-r2-014", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Why should backup copies be stored at an offsite location that is geographically separated from the primary site?",
        "options": [
            {"id": "A", "text": "So that a single local disaster (fire, flood) cannot destroy both the primary data and its backups"},
            {"id": "B", "text": "So that the tapes accumulate more mileage"},
            {"id": "C", "text": "To reduce the organization's electricity costs"},
            {"id": "D", "text": "To make restores intentionally slower"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Geographic separation ensures one local disaster cannot wipe out both production data and its backups at the same time.",
            "distractors": {
                "B": "Tape mileage is not a reason for offsite storage.",
                "C": "Offsite storage is about disaster resilience, not electricity cost.",
                "D": "Slower restores are a drawback, not the purpose.",
            },
            "exam_pattern": "Separate offsite storage so one disaster can't take out both production and backups.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Offsite backup storage"],
    },
    # ----- cisa_disaster_recovery -----
    {
        "id": "cisa-ops-r2-015", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A recovery site that has hardware and network connectivity in place but requires recent data and final configuration to be loaded before operations resume is a:",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Reciprocal site"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A warm site has hardware and connectivity ready but needs current data and final setup, giving a moderate recovery time at moderate cost - between hot and cold.",
            "distractors": {
                "A": "A hot site is fully equipped and current, ready within hours with no major load step.",
                "C": "A cold site provides only space, power, and HVAC - no installed hardware.",
                "D": "A reciprocal site is a mutual-aid arrangement with another organization, not a staged facility.",
            },
            "exam_pattern": "Partial equipment, needs data/config load, moderate time/cost = warm site.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Recovery site types (warm)"],
    },
    {
        "id": "cisa-ops-r2-016", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Which alternate-processing option is a transportable, pre-configured unit (e.g., a trailer) that can be moved to a location and connected to restore operations?",
        "options": [
            {"id": "A", "text": "A cold site"},
            {"id": "B", "text": "A reciprocal agreement"},
            {"id": "C", "text": "A mobile site"},
            {"id": "D", "text": "A hot site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A mobile site is a transportable, pre-equipped unit brought to a location and connected to resume operations - useful when a fixed alternate facility is impractical.",
            "distractors": {
                "A": "A cold site is a fixed, empty conditioned facility.",
                "B": "A reciprocal agreement uses a partner's existing data center.",
                "D": "A hot site is a fixed, fully equipped facility.",
            },
            "exam_pattern": "Transportable, pre-equipped unit brought to a site = mobile site.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Recovery site types (mobile)"],
    },
    {
        "id": "cisa-ops-r2-017", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Which disaster recovery test is the LEAST disruptive and typically performed FIRST to validate the plan on paper?",
        "options": [
            {"id": "A", "text": "A checklist / structured walkthrough review"},
            {"id": "B", "text": "A full-interruption test"},
            {"id": "C", "text": "A parallel test"},
            {"id": "D", "text": "An unannounced shutdown of the production data center"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A checklist/structured walkthrough reviews the plan on paper with no live processing, making it the least disruptive and a natural first step before more realistic tests.",
            "distractors": {
                "B": "A full-interruption test shifts live processing to the alternate site - the most disruptive.",
                "C": "A parallel test processes real workloads at the alternate site - more disruptive than a walkthrough.",
                "D": "An unannounced production shutdown is the most disruptive and risky option.",
            },
            "exam_pattern": "Start DR testing with a low-risk checklist/walkthrough; progress toward parallel then full-interruption.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — DR test types and progression"],
    },
    {
        "id": "cisa-ops-r2-018", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "During disaster recovery, in what order should systems and processes be restored?",
        "options": [
            {"id": "A", "text": "In alphabetical order of system name"},
            {"id": "B", "text": "In order of business criticality, with the most time-sensitive processes (per the BIA) restored first"},
            {"id": "C", "text": "Starting with the least important systems"},
            {"id": "D", "text": "In the order the systems were originally purchased"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Recovery is prioritized by business criticality from the BIA, restoring the most time-sensitive processes first to limit business impact.",
            "distractors": {
                "A": "Alphabetical order ignores business priority.",
                "C": "Restoring least-important systems first wastes the critical recovery window.",
                "D": "Purchase order has no bearing on business criticality.",
            },
            "exam_pattern": "Recover the most business-critical/time-sensitive systems first, driven by the BIA.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Recovery prioritization"],
    },
    {
        "id": "cisa-ops-r2-019", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor finds that the only copies of the disaster recovery plan are stored in the primary data center. Why is this a concern?",
        "options": [
            {"id": "A", "text": "A disaster that destroys the data center would also destroy the plan needed to recover"},
            {"id": "B", "text": "The plan would be read too often"},
            {"id": "C", "text": "The plan would take up too much shelf space"},
            {"id": "D", "text": "Staff would become too familiar with the plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "If the DRP exists only at the primary site, the same disaster that takes out the site destroys the plan; current copies must be kept offsite and accessible to recovery teams.",
            "distractors": {
                "B": "Frequent reading of the plan is beneficial, not a risk.",
                "C": "Shelf space is irrelevant.",
                "D": "Familiarity with the plan is desirable.",
            },
            "exam_pattern": "Keep accessible DRP copies offsite - a plan trapped in the destroyed site is useless.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — DRP availability and storage"],
    },
    # ----- cisa_incident_problem_mgmt -----
    {
        "id": "cisa-ops-r2-020", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "In IT service management, how is the PRIORITY of an incident normally determined?",
        "options": [
            {"id": "A", "text": "By combining its impact and its urgency"},
            {"id": "B", "text": "By the alphabetical name of the affected system"},
            {"id": "C", "text": "By how long the assigned technician has worked there"},
            {"id": "D", "text": "Solely by who reported it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Incident priority is derived by combining impact (how much/how many are affected) with urgency (how quickly resolution is needed).",
            "distractors": {
                "B": "The system's name does not determine priority.",
                "C": "Technician tenure is irrelevant to incident priority.",
                "D": "The reporter's identity alone does not set priority.",
            },
            "exam_pattern": "Incident priority = impact (how much/many) x urgency (how fast it's needed).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Incident prioritization"],
    },
    {
        "id": "cisa-ops-r2-021", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "In problem management, a problem whose root cause has been identified and for which a workaround exists is recorded as a:",
        "options": [
            {"id": "A", "text": "Known error"},
            {"id": "B", "text": "Service request"},
            {"id": "C", "text": "Change request"},
            {"id": "D", "text": "Major incident"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Once root cause and a workaround are documented, a problem is logged as a known error, speeding resolution of future related incidents.",
            "distractors": {
                "B": "A service request is a routine user request (e.g., access or equipment).",
                "C": "A change request proposes a modification to the environment.",
                "D": "A major incident is a high-impact incident, not a documented root cause plus workaround.",
            },
            "exam_pattern": "Root cause found + workaround documented = known error.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Problem management (known error)"],
    },
    {
        "id": "cisa-ops-r2-022", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 1, "type": "mcq",
        "stem": "In ITIL-based operations, the service desk functions PRIMARILY as:",
        "options": [
            {"id": "A", "text": "The team that writes application code"},
            {"id": "B", "text": "The single point of contact (SPOC) between users and IT for incidents and service requests"},
            {"id": "C", "text": "The group that approves the IT budget"},
            {"id": "D", "text": "The external audit function"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The service desk is the single point of contact for users - logging, routing, and tracking incidents and service requests.",
            "distractors": {
                "A": "Coding is a development activity, not the service desk's role.",
                "C": "Budget approval is a management responsibility.",
                "D": "External audit is independent of the service desk.",
            },
            "exam_pattern": "Service desk = single point of contact for users (logs/routes incidents and requests).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Service desk function"],
    },
    {
        "id": "cisa-ops-r2-023", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "An incident requires a decision to authorize significant emergency spending to resolve it. Which type of escalation is appropriate?",
        "options": [
            {"id": "A", "text": "Hierarchical escalation up the management chain"},
            {"id": "B", "text": "Functional escalation to a technical specialist team"},
            {"id": "C", "text": "Closing the incident immediately"},
            {"id": "D", "text": "Logging it as a known error"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Decisions needing authority (like approving emergency spend) require hierarchical escalation up the management chain.",
            "distractors": {
                "B": "Functional escalation obtains technical expertise, not spending authority.",
                "C": "Closing the incident leaves it unresolved.",
                "D": "A known error is a problem-management record, not an escalation for authority.",
            },
            "exam_pattern": "Need authority/management decision = hierarchical escalation; need expertise = functional escalation.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Incident escalation"],
    },
    # ----- cisa_database_mgmt -----
    {
        "id": "cisa-ops-r2-024", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "Which property of a database transaction guarantees that it either completes entirely or has no effect at all (no partial updates)?",
        "options": [
            {"id": "A", "text": "Atomicity"},
            {"id": "B", "text": "Consistency"},
            {"id": "C", "text": "Isolation"},
            {"id": "D", "text": "Durability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Atomicity is the all-or-nothing property: a transaction either fully commits or is completely rolled back, leaving no partial updates.",
            "distractors": {
                "B": "Consistency keeps the database in a valid state that satisfies all constraints.",
                "C": "Isolation keeps concurrent transactions from interfering with each other.",
                "D": "Durability ensures committed results survive a subsequent failure.",
            },
            "exam_pattern": "All-or-nothing transaction = Atomicity (the 'A' in ACID).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Transaction integrity (ACID)"],
    },
    {
        "id": "cisa-ops-r2-025", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "Which database control prevents two concurrent transactions from overwriting each other's updates (the 'lost update' problem)?",
        "options": [
            {"id": "A", "text": "Locking / concurrency control"},
            {"id": "B", "text": "Data encryption"},
            {"id": "C", "text": "A check digit"},
            {"id": "D", "text": "Normalization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Locking/concurrency control serializes conflicting access so simultaneous transactions cannot overwrite one another (a deadlock is two transactions each waiting on the other's lock).",
            "distractors": {
                "B": "Encryption protects confidentiality, not concurrent-update integrity.",
                "C": "A check digit validates input keystrokes, not concurrency.",
                "D": "Normalization reduces redundancy in the schema design, not runtime concurrency.",
            },
            "exam_pattern": "Serialize concurrent updates to prevent lost updates = locking/concurrency control.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Database concurrency control"],
    },
    {
        "id": "cisa-ops-r2-026", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "A database administrator gives a group of users a view that exposes only certain columns and rows of a table. This BEST supports which objective?",
        "options": [
            {"id": "A", "text": "Enforcing least-privilege logical access to data"},
            {"id": "B", "text": "Encrypting the database at rest"},
            {"id": "C", "text": "Backing up the database"},
            {"id": "D", "text": "Improving physical disk speed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A view restricts users to only the rows/columns they need, implementing least-privilege access at the data level.",
            "distractors": {
                "B": "A view is not encryption.",
                "C": "A view is not a backup mechanism.",
                "D": "A view does not affect disk performance.",
            },
            "exam_pattern": "Restrict users to specific columns/rows with a database view = least-privilege data access.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Database access controls (views)"],
    },
    {
        "id": "cisa-ops-r2-027", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "After a database server crash, which mechanism allows the DBMS to restore the database to a consistent state by undoing incomplete transactions and reapplying committed ones?",
        "options": [
            {"id": "A", "text": "Transaction logs/journals with rollback and roll-forward"},
            {"id": "B", "text": "The data dictionary"},
            {"id": "C", "text": "Referential integrity constraints"},
            {"id": "D", "text": "A hash total"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The DBMS uses transaction logs/journals (with checkpoints) to roll back uncommitted transactions and roll forward committed ones, restoring a consistent state after a crash.",
            "distractors": {
                "B": "The data dictionary defines metadata, not recovery state.",
                "C": "Referential integrity enforces key relationships, not crash recovery.",
                "D": "A hash total is a batch-completeness control.",
            },
            "exam_pattern": "Crash recovery to a consistent state = transaction logs + rollback (undo) / roll-forward (reapply).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Database recovery (logging, checkpoints)"],
    },
    {
        "id": "cisa-ops-r2-028", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The repository that defines each data element, its format, attributes, and relationships (the database's metadata) is the data ______.",
        "correct": ["dictionary", "data dictionary"],
        "explanation": {
            "correct": "The data dictionary holds metadata - the definitions, formats, attributes, and relationships of the data elements - supporting consistency and controlled change.",
            "distractors": {},
            "exam_pattern": "Metadata repository defining data elements/attributes/relationships = data dictionary.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Data dictionary"],
    },
    # ======================================================================
    # DOMAIN 5 - Protection of Information Assets
    # ======================================================================
    # ----- cisa_access_controls -----
    {
        "id": "cisa-prot-r2-001", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 3, "type": "mcq",
        "stem": "Which access control model enforces access decisions using system-assigned security labels and clearances that users cannot change, making it suitable for high-security environments?",
        "options": [
            {"id": "A", "text": "Mandatory access control (MAC)"},
            {"id": "B", "text": "Discretionary access control (DAC)"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "No access control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MAC uses system-enforced labels and clearances that users cannot override, the most restrictive model, favored in military/high-security settings.",
            "distractors": {
                "B": "DAC lets the data owner grant access at their discretion - less restrictive.",
                "C": "RBAC assigns access by job role, not by security labels/clearances.",
                "D": "'No access control' is not a model.",
            },
            "exam_pattern": "Labels/clearances, system-enforced, most restrictive = MAC; owner-granted = DAC; role-based = RBAC.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Access control models (MAC)"],
    },
    {
        "id": "cisa-prot-r2-002", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 2, "type": "mcq",
        "stem": "A large organization with frequent staff moves wants to simplify access administration and enforce least privilege consistently. Which access control model is MOST suitable?",
        "options": [
            {"id": "A", "text": "Assigning permissions individually to each user"},
            {"id": "B", "text": "Role-based access control (RBAC)"},
            {"id": "C", "text": "Discretionary access managed ad hoc by each user"},
            {"id": "D", "text": "Granting everyone administrator rights"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RBAC assigns permissions to roles and users to roles, so access changes with the job - scaling cleanly and enforcing least privilege despite frequent moves.",
            "distractors": {
                "A": "Per-user permissions do not scale and drift out of alignment over time.",
                "C": "Ad hoc discretionary access is inconsistent and hard to govern.",
                "D": "Universal administrator rights violate least privilege entirely.",
            },
            "exam_pattern": "Scale + consistency + least privilege across many users = RBAC (permissions by role).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Role-based access control"],
    },
    {
        "id": "cisa-prot-r2-003", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 3, "type": "mcq",
        "stem": "When comparing biometric systems, which single metric BEST indicates overall accuracy, measured where the false acceptance rate equals the false rejection rate?",
        "options": [
            {"id": "A", "text": "The crossover error rate (CER/EER), where lower is better"},
            {"id": "B", "text": "The false acceptance rate alone"},
            {"id": "C", "text": "The false rejection rate alone"},
            {"id": "D", "text": "The average enrollment time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The crossover error rate (equal error rate) is the point where FAR equals FRR; a lower CER indicates a more accurate biometric system and allows fair comparison.",
            "distractors": {
                "B": "FAR alone (Type II error - accepting an impostor) describes only one error type at one threshold.",
                "C": "FRR alone (Type I error - rejecting a legitimate user) also describes only one error type.",
                "D": "Enrollment time is a usability factor, not accuracy.",
            },
            "exam_pattern": "Compare biometrics by the CER/EER (FAR=FRR) - lower CER = more accurate. (FRR=Type I, FAR=Type II.)",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Biometric accuracy (FAR/FRR/CER)"],
    },
    {
        "id": "cisa-prot-r2-004", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 2, "type": "mcq",
        "stem": "Which control is MOST important to prevent access misuse when an employee is involuntarily terminated?",
        "options": [
            {"id": "A", "text": "Promptly disabling the employee's access, coordinated with the termination"},
            {"id": "B", "text": "Scheduling a quarterly access review"},
            {"id": "C", "text": "Sending a company-wide announcement email"},
            {"id": "D", "text": "Archiving the employee's old emails"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Access should be revoked immediately, ideally at or before the moment of an involuntary termination, to prevent retaliatory misuse.",
            "distractors": {
                "B": "A quarterly review is far too slow to address an immediate termination.",
                "C": "An email announcement does not remove the person's access.",
                "D": "Archiving emails does not disable the account.",
            },
            "exam_pattern": "On termination (especially involuntary), revoke/disable access immediately - don't wait for the periodic review.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Access deprovisioning / termination"],
    },
    {
        "id": "cisa-prot-r2-005", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY security risk introduced by single sign-on (SSO)?",
        "options": [
            {"id": "A", "text": "A compromised set of SSO credentials can grant an attacker access to all connected systems"},
            {"id": "B", "text": "Users must remember many more passwords"},
            {"id": "C", "text": "Each application requires a separate login"},
            {"id": "D", "text": "Authentication becomes much slower"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSO concentrates risk: one compromised credential can unlock every connected system, so it should be protected with strong (multi-factor) authentication.",
            "distractors": {
                "B": "SSO reduces the number of passwords users must remember.",
                "C": "SSO removes the need for separate logins - that is its purpose.",
                "D": "SSO generally speeds access rather than slowing it.",
            },
            "exam_pattern": "SSO convenience concentrates risk - one compromised credential unlocks everything (protect it with MFA).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Single sign-on"],
    },
    # ----- cisa_network_security -----
    {
        "id": "cisa-prot-r2-006", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "mcq",
        "stem": "Where should an organization place its public-facing web and email servers to keep them separated from the internal corporate network?",
        "options": [
            {"id": "A", "text": "In a DMZ (screened subnet) between external and internal firewalls"},
            {"id": "B", "text": "Directly on the internal LAN"},
            {"id": "C", "text": "On each employee's workstation"},
            {"id": "D", "text": "Outside any firewall on the public internet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A DMZ/screened subnet isolates internet-facing servers between two firewalls, so a compromise of a public server does not directly expose the internal network.",
            "distractors": {
                "B": "Placing public servers on the internal LAN exposes internal systems if they are breached.",
                "C": "Workstations are inappropriate hosts for public services.",
                "D": "No-firewall exposure leaves the servers and network unprotected.",
            },
            "exam_pattern": "Internet-facing servers belong in a DMZ/screened subnet, isolated from the internal network.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Network segmentation (DMZ)"],
    },
    {
        "id": "cisa-prot-r2-007", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 3, "type": "mcq",
        "stem": "Which type of firewall inspects traffic at the application layer, can hide internal addresses, and makes connections on behalf of clients?",
        "options": [
            {"id": "A", "text": "An application-level gateway (proxy) firewall"},
            {"id": "B", "text": "A static packet-filtering firewall"},
            {"id": "C", "text": "A network hub"},
            {"id": "D", "text": "A media converter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An application-level gateway (proxy) inspects traffic at the application layer, proxies connections for clients, and hides internal addresses - deeper control than packet filtering.",
            "distractors": {
                "B": "A static packet filter only checks header fields at lower layers.",
                "C": "A hub is a passive repeater with no filtering.",
                "D": "A media converter changes the physical medium and performs no filtering.",
            },
            "exam_pattern": "Deep application-layer inspection + proxies connections + hides internal hosts = application-level gateway (proxy).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Firewall types (application gateway)"],
    },
    {
        "id": "cisa-prot-r2-008", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "mcq",
        "stem": "Which network design BEST limits an attacker's ability to move laterally and reach all internal systems after compromising one host?",
        "options": [
            {"id": "A", "text": "Segmenting the network into zones/VLANs with filtering between them"},
            {"id": "B", "text": "Using a single flat network for simplicity"},
            {"id": "C", "text": "Disabling all logging"},
            {"id": "D", "text": "Giving every device a public IP address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Segmenting the network into zones/VLANs with filtering between them contains a breach and restricts lateral movement from a compromised host.",
            "distractors": {
                "B": "A flat network lets an intruder reach everything once inside.",
                "C": "Disabling logging hides attacker activity and aids, not limits, the attacker.",
                "D": "Public IPs on every device widen the attack surface.",
            },
            "exam_pattern": "Segment the network (zones/VLANs) to contain breaches and limit lateral movement.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Network segmentation"],
    },
    {
        "id": "cisa-prot-r2-009", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor finds a wireless LAN still secured with WEP. What is the PRIMARY concern?",
        "options": [
            {"id": "A", "text": "WEP is cryptographically weak and easily broken; it should be replaced with WPA2/WPA3"},
            {"id": "B", "text": "WEP transmits data too slowly"},
            {"id": "C", "text": "WEP uses too much electrical power"},
            {"id": "D", "text": "WEP is incompatible with modern laptops"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "WEP's encryption is fundamentally broken and can be cracked quickly, so wireless should use WPA2/WPA3 (AES) instead.",
            "distractors": {
                "B": "The concern is weak security, not speed.",
                "C": "Power consumption is not the issue.",
                "D": "Compatibility is not the primary concern - weak encryption is.",
            },
            "exam_pattern": "WEP is broken - require WPA2/WPA3 (AES) for wireless.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Wireless security"],
    },
    {
        "id": "cisa-prot-r2-010", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A decoy system deliberately exposed to attract attackers so their activity can be detected and studied is called a ______.",
        "correct": ["honeypot", "honey pot"],
        "explanation": {
            "correct": "A honeypot is a decoy with no production purpose; any interaction with it is suspicious, so it helps detect, divert, and study attackers.",
            "distractors": {},
            "exam_pattern": "Decoy to lure/detect/study attackers = honeypot.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Deception technologies (honeypot)"],
    },
    # ----- cisa_data_classification -----
    {
        "id": "cisa-prot-r2-011", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "What should PRIMARILY determine how long an organization retains a category of records?",
        "options": [
            {"id": "A", "text": "Legal, regulatory, and business requirements"},
            {"id": "B", "text": "The amount of free disk space available"},
            {"id": "C", "text": "The preference of the newest employee"},
            {"id": "D", "text": "How interesting the data is"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Retention periods are driven by legal, regulatory, and business requirements; keeping data longer than required raises cost and risk, while deleting too early can breach obligations.",
            "distractors": {
                "B": "Free disk space is not a valid basis for retention decisions.",
                "C": "Individual preference is not a governance driver.",
                "D": "How 'interesting' data is has no bearing on required retention.",
            },
            "exam_pattern": "Retention periods come from legal/regulatory/business requirements - not convenience.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Data retention"],
    },
    {
        "id": "cisa-prot-r2-012", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 3, "type": "mcq",
        "stem": "Which method BEST ensures that highly sensitive data on decommissioned hard drives cannot be recovered?",
        "options": [
            {"id": "A", "text": "Physical destruction, degaussing, or cryptographic erasure of the media"},
            {"id": "B", "text": "Deleting the files and emptying the recycle bin"},
            {"id": "C", "text": "Performing a quick format of the drive"},
            {"id": "D", "text": "Renaming the files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Physical destruction, degaussing, or cryptographic erase defeats data remanence so sensitive data cannot be reconstructed from retired media.",
            "distractors": {
                "B": "Deleting files and emptying the recycle bin leaves the data recoverable.",
                "C": "A quick format does not overwrite the underlying data.",
                "D": "Renaming files changes nothing about recoverability.",
            },
            "exam_pattern": "Defeat data remanence with degaussing, crypto-erase, or physical destruction - not simple delete/format.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Media sanitization and data remanence"],
    },
    {
        "id": "cisa-prot-r2-013", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "After data has been classified, what is the NEXT step to ensure it is protected consistently throughout its life cycle?",
        "options": [
            {"id": "A", "text": "Label the data and apply handling procedures (storage, transmission, disposal) appropriate to its classification"},
            {"id": "B", "text": "Publish all of it to the intranet"},
            {"id": "C", "text": "Delete the classification so it is simpler"},
            {"id": "D", "text": "Encrypt only the public data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Classification is only useful if data is then labeled and handled - stored, transmitted, and disposed of - according to procedures matching its sensitivity level.",
            "distractors": {
                "B": "Publishing broadly ignores the classification.",
                "C": "Discarding the classification defeats the scheme.",
                "D": "Encrypting only public data misdirects protection away from sensitive data.",
            },
            "exam_pattern": "Classification is only useful if data is then labeled and handled per its level.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Data labeling and handling"],
    },
    {
        "id": "cisa-prot-r2-014", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "Which technology inspects content to detect and block unauthorized transmission of sensitive data via email, web uploads, or removable media?",
        "options": [
            {"id": "A", "text": "Data loss prevention (DLP)"},
            {"id": "B", "text": "A load balancer"},
            {"id": "C", "text": "An uninterruptible power supply (UPS)"},
            {"id": "D", "text": "A hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data loss prevention inspects content against classification/policy and blocks or alerts on unauthorized exfiltration through channels such as email, web, and USB.",
            "distractors": {
                "B": "A load balancer distributes traffic across servers.",
                "C": "A UPS supplies backup power.",
                "D": "A hypervisor runs virtual machines.",
            },
            "exam_pattern": "Detect/block sensitive-data exfiltration by content = data loss prevention (DLP).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Data loss prevention"],
    },
    # ----- cisa_encryption_pki -----
    {
        "id": "cisa-prot-r2-015", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 3, "type": "mcq",
        "stem": "To send a confidential message so that ONLY the intended recipient can read it, the sender should encrypt it with:",
        "options": [
            {"id": "A", "text": "The recipient's public key"},
            {"id": "B", "text": "The sender's private key"},
            {"id": "C", "text": "The sender's public key"},
            {"id": "D", "text": "A one-way hash function"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encrypting with the recipient's public key means only the recipient's matching private key can decrypt it, providing confidentiality to that recipient.",
            "distractors": {
                "B": "Encrypting with the sender's private key creates a signature anyone can read with the public key - not confidentiality.",
                "C": "The sender's public key cannot be decrypted by the recipient alone.",
                "D": "A hash is one-way and cannot be decrypted, so it provides no confidentiality.",
            },
            "exam_pattern": "Confidentiality to a recipient = encrypt with the RECIPIENT's PUBLIC key (only their private key decrypts).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Asymmetric encryption for confidentiality"],
    },
    {
        "id": "cisa-prot-r2-016", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 2, "type": "mcq",
        "stem": "Which technique BEST allows a recipient to verify that a downloaded file has not been altered in transit?",
        "options": [
            {"id": "A", "text": "Comparing a cryptographic hash (message digest) of the file against the published value"},
            {"id": "B", "text": "Checking the file's size only"},
            {"id": "C", "text": "Opening the file to see if it looks right"},
            {"id": "D", "text": "Renaming the file"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cryptographic hash is a one-way digest; if the recomputed hash matches the published value, the file is unchanged - this verifies integrity.",
            "distractors": {
                "B": "File size is a weak indicator that an attacker can easily preserve.",
                "C": "A visual check does not detect subtle tampering.",
                "D": "Renaming proves nothing about integrity.",
            },
            "exam_pattern": "Detect tampering by comparing cryptographic hashes (integrity) - a hash is one-way, no key.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Hashing and integrity"],
    },
    {
        "id": "cisa-prot-r2-017", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 3, "type": "mcq",
        "stem": "Which mechanism provides REAL-TIME checking of whether a digital certificate has been revoked?",
        "options": [
            {"id": "A", "text": "The Online Certificate Status Protocol (OCSP)"},
            {"id": "B", "text": "A certificate revocation list (CRL) published periodically"},
            {"id": "C", "text": "The certificate's expiry date"},
            {"id": "D", "text": "The length of the public key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OCSP queries the certificate's status in real time, returning good/revoked/unknown, unlike a periodically published list.",
            "distractors": {
                "B": "A CRL is published on a schedule, so it can be stale between updates.",
                "C": "The expiry date reflects validity period, not revocation.",
                "D": "Key length is unrelated to revocation status.",
            },
            "exam_pattern": "Real-time revocation check = OCSP; periodically published list = CRL.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Certificate revocation (OCSP/CRL)"],
    },
    {
        "id": "cisa-prot-r2-018", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY challenge of using symmetric encryption among many parties?",
        "options": [
            {"id": "A", "text": "Securely distributing and managing the shared secret keys, whose number grows rapidly with participants"},
            {"id": "B", "text": "It is far too slow to use in practice"},
            {"id": "C", "text": "It cannot encrypt large files"},
            {"id": "D", "text": "It requires a certificate authority for every message"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Symmetric encryption is fast, but its weakness is secure key distribution/management - the number of keys grows roughly as n(n-1)/2 as participants increase.",
            "distractors": {
                "B": "Symmetric algorithms are fast, not too slow.",
                "C": "Symmetric encryption handles large data well.",
                "D": "It does not need a CA for every message.",
            },
            "exam_pattern": "Symmetric is fast but its weakness is secure key distribution/management (key count = n(n-1)/2).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Symmetric key management"],
    },
    {
        "id": "cisa-prot-r2-019", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 2, "type": "multi",
        "stem": "Which TWO security services does a digital signature provide? (Choose two.)",
        "options": [
            {"id": "A", "text": "Integrity (detecting if the message was altered)"},
            {"id": "B", "text": "Non-repudiation (the signer cannot deny signing)"},
            {"id": "C", "text": "Confidentiality (hiding the message contents from eavesdroppers)"},
            {"id": "D", "text": "High availability of the mail server"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A digital signature (the message digest encrypted with the sender's private key) provides integrity and non-repudiation (along with sender authentication).",
            "distractors": {
                "C": "A signature does not hide the message; confidentiality requires separately encrypting with the recipient's public key.",
                "D": "Availability is unrelated to digital signatures.",
            },
            "exam_pattern": "Digital signature = integrity + authentication + non-repudiation, NOT confidentiality.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Digital signature services"],
    },
    # ----- cisa_security_monitoring -----
    {
        "id": "cisa-prot-r2-020", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Why is synchronized time (e.g., via NTP) across servers and network devices IMPORTANT for security monitoring and investigations?",
        "options": [
            {"id": "A", "text": "It lets log events from different systems be accurately correlated and sequenced during analysis and forensics"},
            {"id": "B", "text": "It reduces the organization's electricity use"},
            {"id": "C", "text": "It speeds up nightly backups"},
            {"id": "D", "text": "It encrypts the log files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Without synchronized clocks, events from different systems cannot be reliably correlated or placed in sequence, which undermines SIEM correlation and forensic reconstruction.",
            "distractors": {
                "B": "Time sync does not affect power use.",
                "C": "It does not speed up backups.",
                "D": "NTP does not encrypt logs.",
            },
            "exam_pattern": "Without synchronized clocks you can't reliably correlate/sequence logs across systems (SIEM/forensics depend on it).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Log correlation and time synchronization"],
    },
    {
        "id": "cisa-prot-r2-021", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Which intrusion detection method is MOST likely to detect a previously unknown (zero-day) attack?",
        "options": [
            {"id": "A", "text": "Anomaly/behavior-based detection that flags deviations from a baseline"},
            {"id": "B", "text": "Signature-based detection matching known attack patterns"},
            {"id": "C", "text": "A static list of blocked IP addresses"},
            {"id": "D", "text": "A password-complexity policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anomaly/behavior-based detection compares activity to a learned baseline, so it can flag novel attacks that have no existing signature (at the cost of more false positives).",
            "distractors": {
                "B": "Signature-based detection only catches attacks whose patterns are already known.",
                "C": "A static IP blocklist cannot detect a new attack from an unknown source.",
                "D": "A password policy is a preventive control, not a detection method.",
            },
            "exam_pattern": "Known patterns = signature-based; unknown/zero-day via baseline deviation = anomaly/behavior-based.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — IDS detection methods"],
    },
    {
        "id": "cisa-prot-r2-022", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Which activity BEST demonstrates whether an identified vulnerability can actually be exploited to compromise a system?",
        "options": [
            {"id": "A", "text": "An authorized penetration test that attempts to exploit the weakness"},
            {"id": "B", "text": "An automated vulnerability scan that lists potential weaknesses"},
            {"id": "C", "text": "A review of the security policy document"},
            {"id": "D", "text": "A user satisfaction survey"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A penetration test attempts actual exploitation (with authorization), demonstrating whether a weakness is truly exploitable and its real impact.",
            "distractors": {
                "B": "A vulnerability scan identifies potential weaknesses but does not confirm exploitability.",
                "C": "A policy review assesses documentation, not technical exploitability.",
                "D": "A survey measures perception, not exploitability.",
            },
            "exam_pattern": "Scan = find potential weaknesses (broad); pen test = prove exploitability (depth), with authorization.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Vulnerability scanning vs. penetration testing"],
    },
    {
        "id": "cisa-prot-r2-023", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of maintaining an audit trail of user and system activity?",
        "options": [
            {"id": "A", "text": "To establish individual accountability and enable reconstruction of events"},
            {"id": "B", "text": "To speed up application response time"},
            {"id": "C", "text": "To reduce storage costs"},
            {"id": "D", "text": "To replace the need for access controls"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An audit trail records who did what and when, establishing accountability and letting investigators reconstruct the sequence of events.",
            "distractors": {
                "B": "Audit logging does not improve application performance.",
                "C": "Audit trails consume storage rather than reduce it.",
                "D": "Audit trails complement, not replace, access controls.",
            },
            "exam_pattern": "Audit trail = accountability (who did what, when) + ability to reconstruct events.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Audit trails and accountability"],
    },
    # ----- cisa_physical_environmental -----
    {
        "id": "cisa-prot-r2-024", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "Why must a data center's HVAC system control HUMIDITY within a defined range?",
        "options": [
            {"id": "A", "text": "Low humidity increases static electricity (ESD) that can damage components, while high humidity causes condensation and corrosion"},
            {"id": "B", "text": "Humidity changes the strength of the data's encryption"},
            {"id": "C", "text": "Humidity determines software licensing costs"},
            {"id": "D", "text": "Humidity sets the server's IP addressing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Humidity that is too low invites static discharge (ESD) that harms electronics, while humidity that is too high promotes condensation and corrosion - both must be avoided.",
            "distractors": {
                "B": "Humidity has no effect on encryption strength.",
                "C": "Humidity is unrelated to licensing.",
                "D": "Humidity is unrelated to IP addressing.",
            },
            "exam_pattern": "Keep humidity in range - too low = static/ESD, too high = condensation/corrosion.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Environmental controls (HVAC/humidity)"],
    },
    {
        "id": "cisa-prot-r2-025", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 3, "type": "mcq",
        "stem": "Which water-based fire-suppression system keeps the pipes DRY until a fire is detected, reducing the risk of accidental water damage to equipment, and is therefore often preferred in data centers?",
        "options": [
            {"id": "A", "text": "A pre-action sprinkler system"},
            {"id": "B", "text": "A wet-pipe sprinkler system that always holds water in the pipes"},
            {"id": "C", "text": "An open bucket of water at each rack"},
            {"id": "D", "text": "A deluge system that floods all heads immediately"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A pre-action system holds water back until a detector triggers (and a sprinkler head opens), minimizing the chance of accidental water release over electronics.",
            "distractors": {
                "B": "A wet-pipe system keeps water in the pipes, risking leaks over equipment.",
                "C": "A bucket of water is not a suppression system and harms electronics.",
                "D": "A deluge system discharges from all heads at once - inappropriate over electronics.",
            },
            "exam_pattern": "Pipes stay dry until detection (then charge, then discharge) = pre-action; preferred where water + electronics coexist.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Fire suppression (pre-action systems)"],
    },
    {
        "id": "cisa-prot-r2-026", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "A UPS keeps systems running for a few minutes during an outage. What is required to sustain operations through a PROLONGED power outage?",
        "options": [
            {"id": "A", "text": "A backup generator"},
            {"id": "B", "text": "Additional UPS batteries for a few more minutes"},
            {"id": "C", "text": "A surge protector"},
            {"id": "D", "text": "A thicker power cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A UPS only bridges short gaps; a backup generator supplies power for the duration of a prolonged outage once it starts and takes over from the UPS.",
            "distractors": {
                "B": "More UPS batteries still only extend short-term runtime.",
                "C": "A surge protector conditions power spikes; it provides no power during an outage.",
                "D": "Cable thickness does not supply power during an outage.",
            },
            "exam_pattern": "UPS bridges short outages/allows transfer; a generator sustains power through prolonged outages.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Power continuity (UPS vs. generator)"],
    },
    {
        "id": "cisa-prot-r2-027", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "Halon fire-suppression agents were phased out and replaced by clean agents such as FM-200 or inert gases PRIMARILY because Halon:",
        "options": [
            {"id": "A", "text": "Depletes the ozone layer and was restricted under international agreement"},
            {"id": "B", "text": "Is too expensive to manufacture"},
            {"id": "C", "text": "Is itself flammable"},
            {"id": "D", "text": "Corrodes network cabling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Halon production was banned because it is ozone-depleting (Montreal Protocol); clean agents like FM-200, Novec 1230, and inert gases are the environmentally acceptable replacements.",
            "distractors": {
                "B": "The driver was environmental impact, not manufacturing cost.",
                "C": "Halon is a fire suppressant, not flammable.",
                "D": "Cabling corrosion was not the reason for phasing out Halon.",
            },
            "exam_pattern": "Halon was banned for ozone depletion -> replaced by clean agents (FM-200, Novec 1230, inert gas).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Fire suppression agents (Halon replacement)"],
    },
    {
        "id": "cisa-prot-r2-028", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "Which physical security control provides a DETECTIVE record of who entered the data center and when?",
        "options": [
            {"id": "A", "text": "Badge-reader access logs and CCTV recordings"},
            {"id": "B", "text": "A locked door"},
            {"id": "C", "text": "A perimeter security fence"},
            {"id": "D", "text": "A warning sign"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Badge-reader logs and CCTV recordings capture who entered and when, providing an after-the-fact detective record for review and investigation.",
            "distractors": {
                "B": "A locked door is a preventive control; it keeps people out but keeps no record.",
                "C": "A fence is a preventive/physical barrier, not a record of entries.",
                "D": "A warning sign is a deterrent and records nothing.",
            },
            "exam_pattern": "Record of who/when entered = access logs/CCTV (detective); locks/fences prevent, signs deter.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Physical access monitoring"],
    },
]
