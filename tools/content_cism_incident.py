"""ISACA CISM pool - Domain 4: Incident Management.

Original, objective-aligned practice items for the five incident subtopics
tracked in the study engine:
  * cism_incident_readiness       - the goal of incident management, a documented
                                    and tested plan, the cross-functional CSIRT,
                                    and the manager's facilitating role.
  * cism_incident_response_plan   - severity classification, the escalation and
                                    communication plan, and immediate priorities.
  * cism_bcp_dr                   - the BIA and recovery objectives (RTO, RPO,
                                    MTD) and keeping RTO within the MTD.
  * cism_containment_eradication  - containment vs eradication vs recovery,
                                    verified restoration, and evidence preservation.
  * cism_post_incident_review     - lessons learned, feeding improvements back into
                                    the plan, and tabletop exercises.

Authoring rules match the other content_*.py pools: the build step shuffles
option order (seeded by id), so keys are not positionally biased, every wrong
option carries a distractor note, and each item names the public ISACA objective
area it draws on.

CISM is a MANAGEMENT exam: keyed answers reflect the information security
manager's view - minimize business impact, coordinate and communicate per a
tested plan, and facilitate rather than perform hands-on technical response.
These are original items built from public CISM objectives; they are never real
or memorised exam questions.
"""

QUESTIONS = [
    # ===== cism_incident_readiness ==========================================
    {
        "id": "cism-inc-001", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 1, "type": "mcq",
        "stem": "What is the PRIMARY goal of incident management?",
        "options": [
            {"id": "A", "text": "To identify and punish the employee responsible"},
            {"id": "B", "text": "To purchase new security tools after each event"},
            {"id": "C", "text": "To minimize the impact of incidents on the business and restore normal operations"},
            {"id": "D", "text": "To avoid ever reporting incidents to senior management"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Incident management exists to limit the damage an incident causes to the business "
                       "and to restore normal operations as quickly as possible.",
            "distractors": {
                "A": "Assigning blame is not the goal; managing impact and recovery is.",
                "B": "Tool acquisition is not the purpose of incident management.",
                "D": "Incidents must be reported and escalated appropriately, not hidden from management.",
            },
            "exam_pattern": "Incident management = minimize business impact and restore operations quickly.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident management objectives"],
    },
    {
        "id": "cism-inc-002", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following MOST improves an organization's readiness to handle security "
                "incidents effectively?",
        "options": [
            {"id": "A", "text": "A larger marketing budget"},
            {"id": "B", "text": "Buying the single most expensive firewall available"},
            {"id": "C", "text": "Hiring more salespeople"},
            {"id": "D", "text": "A documented and regularly tested incident response plan"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Readiness comes from preparation: a documented incident response plan that is "
                       "regularly tested (and a trained team) so people know what to do when an incident occurs.",
            "distractors": {
                "A": "A marketing budget does not affect incident readiness.",
                "B": "A single tool does not equal readiness; preparation and process do.",
                "C": "Sales staffing is unrelated to incident readiness.",
            },
            "exam_pattern": "Readiness comes from a documented, tested plan and a prepared team - preparation is the foundation.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident response planning and testing"],
    },
    {
        "id": "cism-inc-003", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 2, "type": "multi",
        "stem": "When establishing a computer security incident response team (CSIRT), which TWO functions "
                "beyond IT security should be represented so the team can handle an incident's full impact? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Legal / compliance"},
            {"id": "B", "text": "Communications / public relations"},
            {"id": "C", "text": "The office vending-machine supplier"},
            {"id": "D", "text": "An unaffiliated external blogger"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Incidents have legal, regulatory, and reputational dimensions, so the CSIRT needs "
                       "legal/compliance and communications/PR representation in addition to IT security.",
            "distractors": {
                "C": "A vending-machine supplier has no role in incident response.",
                "D": "An unaffiliated blogger is not a trusted internal function and should not be on the team.",
            },
            "exam_pattern": "Effective CSIRT = cross-functional (IT security plus legal, communications, HR, and business), not IT alone.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - CSIRT composition"],
    },
    {
        "id": "cism-inc-004", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_readiness", "difficulty": 3, "type": "mcq",
        "stem": "During incident preparation, what is the information security manager's PRIMARY role?",
        "options": [
            {"id": "A", "text": "Personally performing all malware reverse-engineering"},
            {"id": "B", "text": "Writing custom exploit code to test defenses"},
            {"id": "C", "text": "Ensuring the plan, team, training, and communication processes are in place and supported by management"},
            {"id": "D", "text": "Manually rebuilding every affected server without help"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The manager facilitates and coordinates - making sure the plan, trained team, and "
                       "communication/escalation processes exist and have management support - rather than "
                       "doing the hands-on technical work.",
            "distractors": {
                "A": "Deep technical analysis is performed by specialists, not the manager personally.",
                "B": "Writing exploit code is not a management responsibility.",
                "D": "Hands-on server rebuilds are operational tasks, not the manager's primary role.",
            },
            "exam_pattern": "The manager facilitates and coordinates - plan, people, training, support - rather than doing hands-on technical work.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Role of the information security manager"],
    },

    # ===== cism_incident_response_plan ======================================
    {
        "id": "cism-inc-005", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "Immediately after a suspected incident is confirmed, why is classifying its severity "
                "important?",
        "options": [
            {"id": "A", "text": "It determines the appropriate response, escalation, and allocation of resources"},
            {"id": "B", "text": "It assigns blame to a specific department"},
            {"id": "C", "text": "It removes the need for any containment"},
            {"id": "D", "text": "It is only needed for the final written report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Classifying severity drives the response in real time: how urgently to act, who to "
                       "escalate to, and what resources to commit.",
            "distractors": {
                "B": "Classification guides the response, not blame.",
                "C": "Classification informs containment but does not replace it.",
                "D": "Classification is needed during the incident to drive the response, not just for reporting afterward.",
            },
            "exam_pattern": "Classify/prioritize by impact to drive the right response, escalation, and resources.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident classification and prioritization"],
    },
    {
        "id": "cism-inc-006", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 2, "type": "mcq",
        "stem": "A major incident is underway. According to good incident management practice, who should "
                "be informed based on the incident's severity?",
        "options": [
            {"id": "A", "text": "No one, in order to keep the incident secret"},
            {"id": "B", "text": "Only the help desk"},
            {"id": "C", "text": "The general public immediately, before any assessment"},
            {"id": "D", "text": "Predefined stakeholders per the communication/escalation plan, which can include senior management, legal, and regulators"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Communication follows a predefined escalation plan so the right stakeholders - which "
                       "may include senior management, legal, and regulators - are informed based on severity.",
            "distractors": {
                "A": "Concealment violates escalation requirements and often legal obligations.",
                "B": "The help desk alone is insufficient for a major incident.",
                "C": "Public disclosure before assessment is premature and potentially harmful; follow the plan.",
            },
            "exam_pattern": "Communicate per a predefined escalation plan to the right stakeholders based on severity.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Communication and escalation"],
    },
    {
        "id": "cism-inc-007", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 3, "type": "mcq",
        "stem": "An analyst confirms ransomware is actively spreading across the network. According to the "
                "incident response plan, what is the BEST immediate priority?",
        "options": [
            {"id": "A", "text": "Draft the post-incident review report"},
            {"id": "B", "text": "Update the asset inventory"},
            {"id": "C", "text": "Contain the incident to limit its spread and impact"},
            {"id": "D", "text": "Schedule next year's tabletop exercise"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Once an incident is confirmed and actively spreading, the immediate priority is "
                       "containment to limit the damage and stop it from spreading further.",
            "distractors": {
                "A": "The report comes after the incident is handled, not during active spread.",
                "B": "Inventory updates are not the immediate priority while an incident is spreading.",
                "D": "Exercise scheduling is preparation, irrelevant during an active incident.",
            },
            "exam_pattern": "Once confirmed, the immediate priority is containment to limit damage/spread.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Containment as immediate priority"],
    },
    {
        "id": "cism-inc-008", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_incident_response_plan", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The dedicated group responsible for detecting, analyzing, and "
                "responding to security incidents is abbreviated CSIRT, which stands for Computer Security "
                "Incident Response _____. (one word)",
        "correct": ["team"],
        "explanation": {
            "correct": "CSIRT stands for Computer Security Incident Response Team - a cross-functional team "
                       "with clearly defined roles and responsibilities.",
            "exam_pattern": "CSIRT = Computer Security Incident Response Team (cross-functional, defined roles).",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Incident response team (CSIRT)"],
    },

    # ===== cism_bcp_dr ======================================================
    {
        "id": "cism-inc-009", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a business impact analysis (BIA)?",
        "options": [
            {"id": "A", "text": "To configure the backup software"},
            {"id": "B", "text": "To select a firewall vendor"},
            {"id": "C", "text": "To write the acceptable use policy"},
            {"id": "D", "text": "To identify critical business processes and determine recovery priorities and objectives such as RTO and RPO"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A BIA identifies the organization's critical processes and the impact of their "
                       "disruption, setting recovery priorities and objectives (RTO, RPO, MTD) - the "
                       "foundation of BCP/DR.",
            "distractors": {
                "A": "Configuring backups is an implementation task the BIA informs, not the BIA itself.",
                "B": "Firewall selection is unrelated to a BIA.",
                "C": "The acceptable use policy is unrelated to a BIA.",
            },
            "exam_pattern": "BIA identifies critical processes and sets recovery objectives (RTO/RPO/MTD) - the basis of BCP/DR.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Business impact analysis"],
    },
    {
        "id": "cism-inc-010", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "A recovery plan states that no more than 15 minutes of data may be lost in a disruption. "
                "Which recovery objective does this define?",
        "options": [
            {"id": "A", "text": "Recovery time objective (RTO)"},
            {"id": "B", "text": "Recovery point objective (RPO)"},
            {"id": "C", "text": "Maximum tolerable downtime (MTD)"},
            {"id": "D", "text": "Mean time between failures (MTBF)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The RPO is the maximum acceptable amount of data loss, expressed as a point in time "
                       "(here, 15 minutes of data); it drives backup/replication frequency.",
            "distractors": {
                "A": "RTO is the acceptable time to restore service (downtime), not the amount of data loss.",
                "C": "MTD is the total time a process can be down before unacceptable harm occurs.",
                "D": "MTBF is a reliability measure, not a recovery objective.",
            },
            "exam_pattern": "RPO = acceptable data loss (point in time); RTO = acceptable downtime (time to restore).",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - RPO versus RTO"],
    },
    {
        "id": "cism-inc-011", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "Management specifies that a critical system must be back in operation within four hours "
                "of an outage. Which recovery metric does the four-hour target represent?",
        "options": [
            {"id": "A", "text": "Recovery time objective (RTO)"},
            {"id": "B", "text": "Recovery point objective (RPO)"},
            {"id": "C", "text": "Service delivery objective (SDO)"},
            {"id": "D", "text": "Annual loss expectancy (ALE)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The RTO is the maximum acceptable time to restore a process or system after a "
                       "disruption - here, four hours.",
            "distractors": {
                "B": "RPO measures acceptable data loss, not restoration time.",
                "C": "SDO is the level of service to be met during alternate processing, not the restoration deadline.",
                "D": "ALE is a financial risk/loss measure, not a recovery deadline.",
            },
            "exam_pattern": "RTO = how quickly service must be restored; it must be no greater than the MTD.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Recovery time objective"],
    },
    {
        "id": "cism-inc-012", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "An information security manager finds that a critical process has an RTO of 24 hours but "
                "a maximum tolerable downtime (MTD) of 8 hours. What is the BEST course of action?",
        "options": [
            {"id": "A", "text": "Do nothing, because the two values are independent"},
            {"id": "B", "text": "Arbitrarily increase the MTD to 48 hours"},
            {"id": "C", "text": "Delete the process from the business continuity plan"},
            {"id": "D", "text": "Revise the recovery strategy so the RTO is within the MTD"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The RTO must be less than or equal to the MTD; an RTO of 24 hours against an 8-hour "
                       "MTD is an unacceptable gap, so the recovery strategy must be strengthened to bring "
                       "RTO within the MTD.",
            "distractors": {
                "A": "The values are related - RTO must not exceed MTD - so inaction leaves an unacceptable gap.",
                "B": "Arbitrarily inflating the MTD ignores the real business tolerance it represents.",
                "C": "Removing a critical process from the BCP abandons continuity planning for it.",
            },
            "exam_pattern": "RTO must be <= MTD; if RTO exceeds MTD, strengthen the recovery strategy to close the gap.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - RTO, MTD and recovery strategy"],
    },

    # ===== cism_containment_eradication =====================================
    {
        "id": "cism-inc-013", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "mcq",
        "stem": "During an active malware outbreak, the response team isolates the affected network "
                "segments. Which incident response phase does this action represent?",
        "options": [
            {"id": "A", "text": "Eradication"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Lessons learned"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Isolating affected segments to stop the malware from spreading is containment - "
                       "limiting the scope and impact before removing the cause.",
            "distractors": {
                "A": "Eradication removes the malware/root cause after spread is limited.",
                "C": "Lessons learned occurs after the incident is closed.",
                "D": "Recovery restores systems to normal after eradication.",
            },
            "exam_pattern": "Containment = limit the spread/impact first; then eradicate the cause; then recover.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Containment"],
    },
    {
        "id": "cism-inc-014", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "mcq",
        "stem": "After containing an incident, the team removes the malware, closes the exploited "
                "vulnerability, and eliminates the attacker's footholds. Which phase is this?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Preparation"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Detection"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Eradication removes the root cause - malware, the exploited vulnerability, and any "
                       "attacker access - after the incident has been contained.",
            "distractors": {
                "A": "Containment limits spread but does not remove the cause.",
                "B": "Preparation happens before any incident occurs.",
                "D": "Detection is identifying the incident, not removing its cause.",
            },
            "exam_pattern": "Eradication removes the root cause (malware, vulnerability, attacker access) after containment.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Eradication"],
    },
    {
        "id": "cism-inc-015", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 3, "type": "mcq",
        "stem": "Before returning eradicated systems to production, what should the team do to avoid "
                "re-infection?",
        "options": [
            {"id": "A", "text": "Restore and validate systems from known-good sources and confirm the vulnerability is remediated"},
            {"id": "B", "text": "Reconnect the systems immediately without checks to save time"},
            {"id": "C", "text": "Stop all monitoring once the systems are back online"},
            {"id": "D", "text": "Restore from the most recent backup without verifying that it is clean"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recovery restores systems from known-good sources, confirms the vulnerability is "
                       "fixed, and validates the systems before and after returning them to production, with "
                       "heightened monitoring to catch recurrence.",
            "distractors": {
                "B": "Reconnecting without verification risks immediate re-infection.",
                "C": "Heightened monitoring after recovery is essential to catch recurrence, not something to stop.",
                "D": "An unverified backup may reintroduce the very compromise that was removed.",
            },
            "exam_pattern": "Recovery = restore from known-good, validate remediation, then monitor closely for recurrence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Recovery and validation"],
    },
    {
        "id": "cism-inc-016", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_containment_eradication", "difficulty": 2, "type": "mcq",
        "stem": "While containing a serious incident that may lead to legal action, what should the "
                "information security manager ensure is preserved?",
        "options": [
            {"id": "A", "text": "Nothing - wiping the systems as fast as possible is the only priority"},
            {"id": "B", "text": "Only the CEO's email mailbox"},
            {"id": "C", "text": "Evidence, through proper handling and a documented chain of custody, where feasible"},
            {"id": "D", "text": "The marketing team's event calendar"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When legal or regulatory action is possible, containment must be balanced with "
                       "preserving evidence through proper handling and a documented chain of custody so it "
                       "remains admissible.",
            "distractors": {
                "A": "Prematurely wiping systems can destroy evidence needed for legal action.",
                "B": "Preserving a single mailbox ignores the broader relevant evidence.",
                "D": "The marketing calendar is irrelevant to incident evidence.",
            },
            "exam_pattern": "Balance containment with evidence preservation (chain of custody) when legal/regulatory action is possible.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Evidence preservation and chain of custody"],
    },

    # ===== cism_post_incident_review ========================================
    {
        "id": "cism-inc-017", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a post-incident review (lessons-learned session)?",
        "options": [
            {"id": "A", "text": "To identify root causes and improvements that prevent recurrence and strengthen the response capability"},
            {"id": "B", "text": "To assign blame to individual employees"},
            {"id": "C", "text": "To close the incident ticket as quickly as possible"},
            {"id": "D", "text": "To delete all logs generated during the incident"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A post-incident review performs root-cause analysis and identifies improvements, so "
                       "the organization can prevent recurrence and strengthen its response for next time.",
            "distractors": {
                "B": "Lessons learned focus on improvement, not blaming individuals.",
                "C": "Speed to close is not the purpose; organizational learning is.",
                "D": "Deleting logs destroys records needed for learning and possible legal use.",
            },
            "exam_pattern": "Post-incident review = root-cause analysis and improvements to prevent recurrence.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Post-incident review and lessons learned"],
    },
    {
        "id": "cism-inc-018", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 3, "type": "mcq",
        "stem": "A post-incident review concludes that unclear escalation paths delayed the response. What "
                "should the information security manager do with this finding?",
        "options": [
            {"id": "A", "text": "Ignore it, since the incident is already over"},
            {"id": "B", "text": "Keep it secret from the response team"},
            {"id": "C", "text": "Update the incident response plan and related processes to correct the weakness"},
            {"id": "D", "text": "Remove escalation from the plan entirely"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Lessons learned must feed back into the plan: the manager updates the incident "
                       "response plan and processes so the escalation weakness is corrected for future incidents.",
            "distractors": {
                "A": "Ignoring the finding wastes the review and allows the problem to recur.",
                "B": "Withholding lessons prevents improvement and team learning.",
                "D": "Removing escalation worsens the problem rather than fixing it.",
            },
            "exam_pattern": "Lessons learned must feed back into the plan and controls - continuous improvement closes the loop.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Feeding lessons learned back into the plan"],
    },
    {
        "id": "cism-inc-019", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "mcq",
        "stem": "An organization runs a discussion-based walkthrough of a simulated incident scenario to "
                "validate its response plan without affecting production systems. What is this exercise "
                "called?",
        "options": [
            {"id": "A", "text": "A penetration test"},
            {"id": "B", "text": "A tabletop exercise"},
            {"id": "C", "text": "A vulnerability scan"},
            {"id": "D", "text": "A full data-center failover"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A tabletop exercise is a discussion-based walkthrough of a scenario that validates "
                       "the plan, roles, and decisions without affecting production systems.",
            "distractors": {
                "A": "A penetration test actively probes systems for weaknesses, not a discussion-based walkthrough.",
                "C": "A vulnerability scan is an automated technical assessment, not a scenario discussion.",
                "D": "A full failover actually switches operations and does affect systems, unlike a tabletop.",
            },
            "exam_pattern": "Tabletop = discussion-based plan validation with no production impact; it tests roles, decisions, and gaps.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Tabletop exercises and plan testing"],
    },
    {
        "id": "cism-inc-020", "exam": "cism", "domain": "cism_incident",
        "subtopic": "cism_post_incident_review", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Reviewing an incident after closure to capture what worked, what did "
                "not, and how to improve is commonly called the lessons-_____ process. (one word)",
        "correct": ["learned"],
        "explanation": {
            "correct": "The lessons-learned process reviews the incident after closure and drives "
                       "continuous improvement of the organization's incident response capability.",
            "exam_pattern": "Lessons-learned review drives continuous improvement of incident response.",
        },
        "references": ["ISACA CISM Review Manual: Domain 4 - Lessons-learned process"],
    },
]
