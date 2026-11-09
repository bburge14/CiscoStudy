"""ISACA CISM pool - Domain 3: Information Security Program.

Original, objective-aligned practice items for the six program subtopics tracked
in the study engine:
  * cism_program_development - building a program that executes the strategy,
                               risk-driven prioritization, value justification,
                               and integrating security into business/IT processes.
  * cism_security_controls   - functional control types (preventive/detective/
                               corrective/compensating) and categories
                               (administrative/technical/physical).
  * cism_program_frameworks  - control frameworks and catalogs (NIST CSF,
                               ISO/IEC 27002, CIS Controls) and when each applies.
  * cism_awareness_training  - the purpose of awareness, tailoring to the audience,
                               and measuring behavior change.
  * cism_metrics_reporting   - KPIs vs KGIs vs KRIs, audience-appropriate board
                               reporting, and value delivery.
  * cism_third_party_mgmt    - vendor due diligence, contractual security
                               requirements/SLAs/right-to-audit, and ongoing
                               monitoring when accountability stays with the org.

Authoring rules match the other content_*.py pools: the build step shuffles
option order (seeded by id), so keys are not positionally biased, every wrong
option carries a distractor note, and each item names the public ISACA objective
area it draws on.

CISM is a MANAGEMENT exam: keyed answers reflect the information security
manager's view - justify security in business terms, report metrics the audience
can act on, and keep accountability in-house even when work is outsourced. These
are original items built from public CISM objectives; they are never real or
memorised exam questions.
"""

QUESTIONS = [
    # ===== cism_program_development =========================================
    {
        "id": "cism-prog-001", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "An information security program is being developed. To be effective, with what must the "
                "program be aligned?",
        "options": [
            {"id": "A", "text": "The personal certifications held by the security team"},
            {"id": "B", "text": "The physical office floor plan"},
            {"id": "C", "text": "The vendor's default product settings"},
            {"id": "D", "text": "The information security strategy and the organization's business objectives"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The program is the execution of the security strategy, which itself aligns to "
                       "business objectives; alignment flows from governance down into the program.",
            "distractors": {
                "A": "Staff certifications are useful but do not define program alignment.",
                "B": "The floor plan is irrelevant to program alignment.",
                "C": "Vendor defaults are not an alignment target.",
            },
            "exam_pattern": "The program executes the strategy, which aligns to business objectives - alignment flows from governance.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Program alignment with strategy"],
    },
    {
        "id": "cism-prog-002", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "Before building out specific controls and projects, on what should the information "
                "security program be based so that resources address the greatest exposures?",
        "options": [
            {"id": "A", "text": "The alphabetical order of the business units"},
            {"id": "B", "text": "The cheapest tools currently available"},
            {"id": "C", "text": "A risk assessment of the organization's assets"},
            {"id": "D", "text": "The number of help-desk tickets filed last month"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Program priorities are risk-driven: a risk assessment shows where exposure is "
                       "greatest, so resources go where they reduce the most risk.",
            "distractors": {
                "A": "Alphabetical ordering has nothing to do with exposure.",
                "B": "Choosing by lowest cost is not risk-based prioritization.",
                "D": "Ticket volume does not reflect the greatest risk exposures.",
            },
            "exam_pattern": "Program priorities are risk-driven - focus resources where exposure is greatest.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Risk-based program priorities"],
    },
    {
        "id": "cism-prog-003", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 3, "type": "mcq",
        "stem": "Senior management asks the information security manager to justify the security program's "
                "budget. Which argument is MOST aligned with the CISM perspective?",
        "options": [
            {"id": "A", "text": "'We need the newest technology because our competitors have it'"},
            {"id": "B", "text": "'Spending more always means better security'"},
            {"id": "C", "text": "'The security team prefers these particular tools'"},
            {"id": "D", "text": "'These investments reduce risk to acceptable levels and support the organization's business objectives'"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Security is justified in business terms - reducing risk to acceptable levels and "
                       "supporting business objectives (value delivery) - which is what management responds to.",
            "distractors": {
                "A": "Keeping up with competitors is not a value- or risk-based justification.",
                "B": "More spending does not linearly improve security and ignores cost-benefit.",
                "C": "Team preference is not a business justification.",
            },
            "exam_pattern": "Justify security in business terms - risk reduction and support for objectives (value delivery).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Business case and value delivery"],
    },
    {
        "id": "cism-prog-004", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_development", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following BEST indicates that an information security program is well "
                "integrated with the organization?",
        "options": [
            {"id": "A", "text": "The security team works in isolation from other departments"},
            {"id": "B", "text": "Security is applied only after systems have gone live"},
            {"id": "C", "text": "Only the security team is aware of the security policies"},
            {"id": "D", "text": "Security requirements are considered within business and IT project processes from the start"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An integrated program builds security into business and IT processes from the "
                       "beginning, rather than bolting it on afterward.",
            "distractors": {
                "A": "Isolation is the opposite of integration.",
                "B": "Bolt-on, after-the-fact security indicates poor integration.",
                "C": "Policies known only to the security team show poor integration and awareness.",
            },
            "exam_pattern": "Integrated security is built in from the start across business/IT processes, not bolted on.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Integrating security into processes"],
    },

    # ===== cism_security_controls ===========================================
    {
        "id": "cism-prog-005", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 1, "type": "mcq",
        "stem": "A firewall that blocks unauthorized traffic before it can reach internal systems is BEST "
                "classified as which functional control type?",
        "options": [
            {"id": "A", "text": "Detective"},
            {"id": "B", "text": "Corrective"},
            {"id": "C", "text": "Preventive"},
            {"id": "D", "text": "Compensating"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A preventive control stops an unwanted event before it happens; a firewall blocking "
                       "traffic is a classic preventive control.",
            "distractors": {
                "A": "A detective control identifies events after they occur (for example, an IDS or log review), not before.",
                "B": "A corrective control restores after an event (for example, restoring from backup).",
                "D": "A compensating control is an alternative used when the primary control is not feasible.",
            },
            "exam_pattern": "Preventive = stop before it happens; detective = find it; corrective = fix/restore after.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control types (preventive)"],
    },
    {
        "id": "cism-prog-006", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "An intrusion detection system that alerts analysts to suspicious activity is an example "
                "of which functional control type?",
        "options": [
            {"id": "A", "text": "Preventive"},
            {"id": "B", "text": "Deterrent"},
            {"id": "C", "text": "Detective"},
            {"id": "D", "text": "Corrective"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A detective control identifies and signals events that have occurred; an IDS that "
                       "generates alerts detects rather than blocks.",
            "distractors": {
                "A": "Preventive controls block the activity; an IDS detects it instead.",
                "B": "A deterrent discourages an action (for example, a warning banner); detection happens after the attempt.",
                "D": "Corrective controls restore systems after an incident, not detect it.",
            },
            "exam_pattern": "IDS, log review, and alerts = detective controls (identify events).",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control types (detective)"],
    },
    {
        "id": "cism-prog-007", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are examples of ADMINISTRATIVE (managerial) controls? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Security awareness training"},
            {"id": "B", "text": "A firewall rule set"},
            {"id": "C", "text": "An acceptable use policy"},
            {"id": "D", "text": "A door lock on the server room"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Administrative (managerial) controls are people- and process-oriented - policies, "
                       "procedures, and training such as awareness training and an acceptable use policy.",
            "distractors": {
                "B": "A firewall rule set is a technical (logical) control.",
                "D": "A door lock is a physical control.",
            },
            "exam_pattern": "Administrative = policies/training/procedures; technical = systems; physical = environment.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Control categories (administrative/technical/physical)"],
    },
    {
        "id": "cism-prog-008", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_security_controls", "difficulty": 3, "type": "mcq",
        "stem": "A legacy system cannot support multi-factor authentication. The information security "
                "manager instead isolates it on a restricted network segment with enhanced monitoring. The "
                "added controls are BEST described as:",
        "options": [
            {"id": "A", "text": "Compensating controls"},
            {"id": "B", "text": "Deterrent controls"},
            {"id": "C", "text": "Redundant controls that can safely be removed"},
            {"id": "D", "text": "Preventive controls that fully replicate MFA's assurance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When the preferred control is not feasible, compensating controls provide "
                       "comparable risk reduction by other means - here, isolation plus monitoring stand in for MFA.",
            "distractors": {
                "B": "Deterrents discourage behavior; these controls substitute for a missing control.",
                "C": "They are not disposable; they address a real gap left by the missing control.",
                "D": "They reduce risk but do not claim to fully replicate MFA's assurance; the aim is reasonable compensation.",
            },
            "exam_pattern": "When the preferred control is infeasible, compensating controls reduce risk by alternative means.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Compensating controls"],
    },

    # ===== cism_program_frameworks ==========================================
    {
        "id": "cism-prog-009", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "An organization adopts a framework whose core organizes activities into Identify, "
                "Protect, Detect, Respond, and Recover. Which framework is this?",
        "options": [
            {"id": "A", "text": "The OSI reference model"},
            {"id": "B", "text": "The NIST Cybersecurity Framework (CSF)"},
            {"id": "C", "text": "PCI DSS"},
            {"id": "D", "text": "ITIL"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Identify, Protect, Detect, Respond, and Recover are the core functions of the NIST "
                       "Cybersecurity Framework (CSF 2.0 adds Govern).",
            "distractors": {
                "A": "The OSI model describes networking layers, not security functions.",
                "C": "PCI DSS is a payment-card security standard, not these five functions.",
                "D": "ITIL addresses IT service management, not these cybersecurity functions.",
            },
            "exam_pattern": "Identify, Protect, Detect, Respond, Recover (and Govern in CSF 2.0) = NIST CSF core functions.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - NIST Cybersecurity Framework"],
    },
    {
        "id": "cism-prog-010", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "An information security manager needs a reference catalog of security control best "
                "practices to help implement the organization's ISMS. Which document is the BEST source?",
        "options": [
            {"id": "A", "text": "ISO/IEC 27002"},
            {"id": "B", "text": "The organization's ISO/IEC 27001 certification certificate"},
            {"id": "C", "text": "A structured cabling standard"},
            {"id": "D", "text": "The company travel policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ISO/IEC 27002 provides guidance and best practices for selecting and implementing "
                       "information security controls, supporting an ISO/IEC 27001 ISMS.",
            "distractors": {
                "B": "27001 states the ISMS requirements and is what you certify against; 27002 is the control guidance you implement.",
                "C": "Cabling standards are unrelated to security control selection.",
                "D": "A travel policy is not a security control catalog.",
            },
            "exam_pattern": "27001 = ISMS requirements; 27002 = the control best-practice catalog that supports it.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - ISO/IEC 27002 controls"],
    },
    {
        "id": "cism-prog-011", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_program_frameworks", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A prioritized, prescriptive set of defensive safeguards published by "
                "the Center for Internet Security, often adopted as a practical starting point, are the "
                "_____ Controls. (enter the three-letter acronym)",
        "correct": ["cis"],
        "explanation": {
            "correct": "The CIS Controls are a prioritized, prescriptive set of safeguards; they are more "
                       "actionable and specific than broad frameworks like the NIST CSF or ISO/IEC 27002.",
            "exam_pattern": "CIS Controls = prioritized, prescriptive safeguards; NIST CSF and ISO/IEC 27002 are broader framework/catalog references.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - CIS Controls"],
    },

    # ===== cism_awareness_training ==========================================
    {
        "id": "cism-prog-012", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 1, "type": "mcq",
        "stem": "What is the PRIMARY goal of a security awareness program?",
        "options": [
            {"id": "A", "text": "To replace the need for all technical controls"},
            {"id": "B", "text": "To influence employee behavior so staff recognize and respond appropriately to security risks"},
            {"id": "C", "text": "To train the security team on advanced forensic tools"},
            {"id": "D", "text": "To satisfy a request from the marketing department"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Awareness aims to change behavior and build a security culture so the workforce "
                       "recognizes and responds appropriately to risks such as phishing and social engineering.",
            "distractors": {
                "A": "Awareness complements, rather than replaces, technical controls.",
                "C": "That describes specialized technical training for the security team, not organization-wide awareness.",
                "D": "Awareness targets risk behavior, not a marketing goal.",
            },
            "exam_pattern": "Awareness aims to change behavior and build a security culture across the workforce.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Security awareness objectives"],
    },
    {
        "id": "cism-prog-013", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 2, "type": "mcq",
        "stem": "To maximize effectiveness, how should security awareness content BEST be delivered?",
        "options": [
            {"id": "A", "text": "As a single generic message sent once to everyone"},
            {"id": "B", "text": "Only to the IT department"},
            {"id": "C", "text": "Tailored to the roles and responsibilities of different audiences, on an ongoing basis"},
            {"id": "D", "text": "Only after a breach has already occurred"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Awareness is most effective when it is role-based, ongoing, and tailored to each "
                       "audience so the content is relevant to what people actually do.",
            "distractors": {
                "A": "A one-size-fits-all, one-time message is far less effective.",
                "B": "Awareness must reach the whole workforce, not just IT.",
                "D": "Awareness is ongoing and proactive, not only a reaction to incidents.",
            },
            "exam_pattern": "Effective awareness is role-based, ongoing, and tailored to the audience.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Tailoring awareness to the audience"],
    },
    {
        "id": "cism-prog-014", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_awareness_training", "difficulty": 3, "type": "mcq",
        "stem": "Which metric BEST demonstrates that a security awareness program is effective?",
        "options": [
            {"id": "A", "text": "The number of training slides produced"},
            {"id": "B", "text": "The length of the training video"},
            {"id": "C", "text": "The number of awareness posters printed"},
            {"id": "D", "text": "A measurable reduction in risky behaviors, such as fewer employees falling for simulated phishing"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Effectiveness is shown by outcomes - a measurable change in behavior, such as a "
                       "falling click rate on phishing simulations - not by how much material was produced.",
            "distractors": {
                "A": "Slide counts are output/activity measures, not evidence of behavior change.",
                "B": "Video length measures effort, not effectiveness.",
                "C": "Poster counts are activity, not outcomes.",
            },
            "exam_pattern": "Measure awareness by outcomes/behavior change (for example, phishing-simulation click rates), not activity volume.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Measuring awareness effectiveness"],
    },

    # ===== cism_metrics_reporting ===========================================
    {
        "id": "cism-prog-015", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "mcq",
        "stem": "An information security manager wants a metric showing how well the patch-management "
                "process is performing - for example, the percentage of critical patches applied within "
                "the target window. Which metric type is this?",
        "options": [
            {"id": "A", "text": "Key risk indicator (KRI)"},
            {"id": "B", "text": "Key performance indicator (KPI)"},
            {"id": "C", "text": "Key goal indicator (KGI)"},
            {"id": "D", "text": "A risk appetite statement"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A KPI measures how well a process is performing against a target - here, timely "
                       "application of critical patches.",
            "distractors": {
                "A": "A KRI signals changing risk exposure, not process performance.",
                "C": "A KGI confirms whether a goal was achieved, not how the process is performing.",
                "D": "A risk appetite statement sets acceptable risk; it is not a performance metric.",
            },
            "exam_pattern": "KPI = how well a process performs; KGI = whether the goal was met; KRI = how risk exposure is trending.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - KPIs, KGIs and KRIs"],
    },
    {
        "id": "cism-prog-016", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 3, "type": "mcq",
        "stem": "When reporting security metrics to the board of directors, what should the information "
                "security manager focus on MOST?",
        "options": [
            {"id": "A", "text": "The number of firewall rules changed last month"},
            {"id": "B", "text": "Raw counts of blocked network packets"},
            {"id": "C", "text": "Business-relevant information such as risk posture, trends, and alignment with objectives"},
            {"id": "D", "text": "Verbatim technical log excerpts"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Metrics must suit the audience; the board needs business-relevant information - risk "
                       "posture, trends, and alignment with objectives - to make decisions.",
            "distractors": {
                "A": "Firewall rule-change counts are operational detail with little board value.",
                "B": "Packet counts are too technical and not decision-relevant for the board.",
                "D": "Raw logs are inappropriate for board-level reporting.",
            },
            "exam_pattern": "Tailor metrics to the audience - the board needs business-relevant risk and value information, not technical minutiae.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Reporting to senior management/board"],
    },
    {
        "id": "cism-prog-017", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_metrics_reporting", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In CISM, optimizing security investments so they support business "
                "objectives and manage risk cost-effectively is referred to as value _____. (one word)",
        "correct": ["delivery"],
        "explanation": {
            "correct": "Value delivery means security spending is optimized to support business objectives "
                       "and manage risk cost-effectively - security as a business enabler, not just a cost.",
            "exam_pattern": "Value delivery = optimized, cost-effective security that supports business objectives and manages risk.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Value delivery"],
    },

    # ===== cism_third_party_mgmt ============================================
    {
        "id": "cism-prog-018", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Before onboarding a vendor that will process sensitive customer data, what should the "
                "information security manager ensure is done FIRST?",
        "options": [
            {"id": "A", "text": "Grant the vendor immediate production access to speed integration"},
            {"id": "B", "text": "A due-diligence assessment of the vendor's security posture against the organization's requirements"},
            {"id": "C", "text": "Payment of the full contract value up front"},
            {"id": "D", "text": "A press release announcing the new partnership"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Third-party risk is assessed before engagement: due diligence verifies the vendor "
                       "can meet the organization's security requirements before any data or access is granted.",
            "distractors": {
                "A": "Granting access before assessment introduces unmanaged risk.",
                "C": "Payment is a commercial step, not a security control.",
                "D": "A press release is unrelated to managing third-party risk.",
            },
            "exam_pattern": "Assess third-party risk (due diligence) before engagement; grant access only after requirements are met.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Third-party due diligence"],
    },
    {
        "id": "cism-prog-019", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Which mechanism BEST allows an organization to hold a service provider to agreed security "
                "and service levels and to verify ongoing compliance?",
        "options": [
            {"id": "A", "text": "Verbal assurances from the vendor's sales team"},
            {"id": "B", "text": "The vendor's general brand reputation"},
            {"id": "C", "text": "Contractual security requirements, SLAs, and a right-to-audit clause"},
            {"id": "D", "text": "Checking the vendor's social media presence"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Enforceable contract terms - defined security requirements, SLAs, and a right-to-audit "
                       "clause - let the organization hold the provider accountable and verify compliance.",
            "distractors": {
                "A": "Verbal assurances are unenforceable.",
                "B": "Reputation is not an enforceable control.",
                "D": "Social media presence is not evidence of security compliance.",
            },
            "exam_pattern": "Bind third parties with contractual security requirements, SLAs, and audit rights - then monitor.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Contracts, SLAs and right to audit"],
    },
    {
        "id": "cism-prog-020", "exam": "cism", "domain": "cism_program",
        "subtopic": "cism_third_party_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "After outsourcing a business process to a third party, how should the information "
                "security manager treat the associated risk?",
        "options": [
            {"id": "A", "text": "Consider it fully transferred and stop monitoring it"},
            {"id": "B", "text": "Delete the risk from the risk register"},
            {"id": "C", "text": "Assume the vendor's certifications remove any need for oversight"},
            {"id": "D", "text": "Continue to monitor the provider's performance and security, since accountability for the data remains with the organization"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Outsourcing the function does not outsource accountability; the organization must "
                       "keep monitoring the provider's security and performance throughout the relationship.",
            "distractors": {
                "A": "Outsourcing does not end the organization's accountability or the need to monitor.",
                "B": "Removing it from the register hides an active risk.",
                "C": "Certifications are helpful evidence but do not eliminate ongoing oversight.",
            },
            "exam_pattern": "You can outsource the function, not the accountability - third-party risk needs ongoing monitoring.",
        },
        "references": ["ISACA CISM Review Manual: Domain 3 - Ongoing third-party monitoring"],
    },
]
