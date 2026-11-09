"""(ISC)² Certified in Cybersecurity (CC) pool - Domain 2: BC, DR & Incident Response.

Original, objective-aligned practice items for the three subtopics CertLab tracks:
  * cc_incident_response  - events vs. incidents, the incident-response lifecycle
                            (preparation, detection, containment, eradication,
                            recovery, post-incident), and the CSIRT.
  * cc_business_continuity - keeping essential functions running through a
                            disruption; the business impact analysis (BIA) and the
                            business continuity plan (BCP).
  * cc_disaster_recovery   - restoring IT after a disaster; recovery sites (hot,
                            warm, cold), RTO vs. RPO, and backup types.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased, every
wrong option carries a distractor note, and each item names the (ISC)² CC exam-outline
area it draws on. Entry-level depth only - core, well-established facts.
"""

QUESTIONS = [
    # ===== cc_incident_response =============================================
    {
        "id": "isc2cc-bcdr-001", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 1, "type": "mcq",
        "stem": "A monitoring tool logs an unremarkable user login - an observable occurrence with no "
                "harm. In incident-response terms, what is this best called?",
        "options": [
            {"id": "A", "text": "A disaster"},
            {"id": "B", "text": "An incident"},
            {"id": "C", "text": "A breach"},
            {"id": "D", "text": "An event"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An event is any observable occurrence in a system or network; most events are "
                       "routine and harmless, like a normal login.",
            "distractors": {
                "A": "A disaster is a large-scale disruptive event that invokes DR/BC plans, far beyond a single login.",
                "B": "An incident is an event that actually or potentially harms the CIA of information; a normal login is not harmful.",
                "C": "A breach specifically involves confirmed unauthorized access to or disclosure of data.",
            },
            "exam_pattern": "Any observable occurrence = event; one that harms/threatens CIA = incident.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident terminology (event vs. incident)"],
    },
    {
        "id": "isc2cc-bcdr-002", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "After confirming malware is spreading on a server, the response team's immediate goal "
                "is to stop it from reaching other systems. Which incident-response phase is this?",
        "options": [
            {"id": "A", "text": "Detection and analysis"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Recovery"},
            {"id": "D", "text": "Post-incident activity"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Containment limits the scope and spread of an incident - for example, isolating the "
                       "infected server - so the damage does not expand.",
            "distractors": {
                "A": "Detection and analysis is where the incident is identified and confirmed, which already happened here.",
                "C": "Recovery restores systems to normal operation, which comes after the threat is contained and removed.",
                "D": "Post-incident activity captures lessons learned after the incident is resolved.",
            },
            "exam_pattern": "Stop the spread / isolate affected systems = containment.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident response (containment)"],
    },
    {
        "id": "isc2cc-bcdr-003", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "Once an infected host is isolated, the team deletes the malware and closes the "
                "vulnerability that let it in. Which incident-response phase does this describe?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Preparation"},
            {"id": "D", "text": "Detection"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Eradication removes the cause of the incident - deleting the malware and fixing the "
                       "exploited weakness - so it cannot recur from the same source.",
            "distractors": {
                "A": "Containment only isolates/limits the incident; it does not remove the malware or fix the flaw.",
                "C": "Preparation happens before incidents, building plans, tools, and training.",
                "D": "Detection is identifying that an incident is occurring, not removing the threat.",
            },
            "exam_pattern": "Remove the malware / eliminate the root cause = eradication (before recovery).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident response (eradication)"],
    },
    {
        "id": "isc2cc-bcdr-004", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 1, "type": "mcq",
        "stem": "A company forms a dedicated group of trained staff responsible for detecting, "
                "responding to, and recovering from security incidents. This group is commonly called a:",
        "options": [
            {"id": "A", "text": "CSIRT (Computer Security Incident Response Team)"},
            {"id": "B", "text": "Change Advisory Board (CAB)"},
            {"id": "C", "text": "Help desk"},
            {"id": "D", "text": "Steering committee"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CSIRT (also called CIRT or IRT) is the team specifically chartered to handle "
                       "security incidents across their lifecycle.",
            "distractors": {
                "B": "A Change Advisory Board reviews and approves changes, not security incidents.",
                "C": "A help desk handles general user support, not coordinated incident response.",
                "D": "A steering committee sets strategy and priorities; it does not run incident response.",
            },
            "exam_pattern": "Dedicated incident-handling team = CSIRT/CIRT/IRT.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident response team (CSIRT)"],
    },
    {
        "id": "isc2cc-bcdr-005", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "Days after an incident is resolved, the team meets to review what happened and update "
                "procedures to prevent a repeat. Which incident-response phase is this?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Post-incident activity (lessons learned)"},
            {"id": "D", "text": "Detection and analysis"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Post-incident activity - the lessons-learned review - analyzes how the incident was "
                       "handled and feeds improvements back into preparation.",
            "distractors": {
                "A": "Containment happens during the active incident to limit spread, not afterward.",
                "B": "Eradication removes the threat during response, before the review.",
                "D": "Detection and analysis is the early phase of recognizing the incident.",
            },
            "exam_pattern": "Review/lessons learned to improve for next time = post-incident activity.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident response (post-incident activity)"],
    },
    {
        "id": "isc2cc-bcdr-006", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response", "difficulty": 2, "type": "fill",
        "stem": "In the incident-response lifecycle, the phase done BEFORE any incident - creating the "
                "IR plan, assembling tools, and training the team - is called ___. (one word)",
        "correct": ["preparation", "prepare"],
        "explanation": {
            "correct": "Preparation is the first phase: building the capability (plans, tools, training) "
                       "so the organization can respond effectively when an incident occurs.",
            "exam_pattern": "Readiness work done before incidents (plans/tools/training) = preparation.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Incident response (preparation)"],
    },

    # ===== cc_business_continuity ===========================================
    {
        "id": "isc2cc-bcdr-007", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary purpose of business continuity (BC) planning?",
        "options": [
            {"id": "A", "text": "To keep essential business functions operating during and after a disruption"},
            {"id": "B", "text": "To delete malware from infected endpoints"},
            {"id": "C", "text": "To encrypt data while it travels across the internet"},
            {"id": "D", "text": "To test employees with simulated phishing emails"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Business continuity focuses on maintaining the organization's critical/essential "
                       "functions through a disruption so the business can keep operating.",
            "distractors": {
                "B": "Removing malware is part of incident response, not business continuity.",
                "C": "Encrypting data in transit is a confidentiality control, not continuity planning.",
                "D": "Phishing simulations are security-awareness activities, not business continuity.",
            },
            "exam_pattern": "Keep the business running through disruption = business continuity.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Business continuity (purpose)"],
    },
    {
        "id": "isc2cc-bcdr-008", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 2, "type": "mcq",
        "stem": "Before writing its continuity plan, an organization studies which functions are most "
                "critical and the impact if each were lost. What is this analysis called?",
        "options": [
            {"id": "A", "text": "Vulnerability scan"},
            {"id": "B", "text": "Penetration test"},
            {"id": "C", "text": "Root-cause analysis"},
            {"id": "D", "text": "Business impact analysis (BIA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A business impact analysis (BIA) identifies critical business functions and the "
                       "consequences of their disruption, driving recovery priorities and objectives.",
            "distractors": {
                "A": "A vulnerability scan finds technical flaws, not the business impact of losing functions.",
                "B": "A penetration test probes for exploitable weaknesses; it does not rank business functions by impact.",
                "C": "Root-cause analysis finds why an incident happened, not which functions are most critical.",
            },
            "exam_pattern": "Identify critical functions + impact of their loss = BIA.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Business continuity (BIA)"],
    },
    {
        "id": "isc2cc-bcdr-009", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 3, "type": "mcq",
        "stem": "During a flood, leadership's first priority is keeping the order-processing function "
                "running from an alternate location - not yet rebuilding the damaged data center. "
                "Which discipline is being exercised?",
        "options": [
            {"id": "A", "text": "Disaster recovery"},
            {"id": "B", "text": "Business continuity"},
            {"id": "C", "text": "Digital forensics"},
            {"id": "D", "text": "Penetration testing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Keeping essential functions operating through the disruption is the heart of "
                       "business continuity; disaster recovery is the related effort to restore the IT systems.",
            "distractors": {
                "A": "Disaster recovery focuses on restoring/rebuilding IT systems after the disaster, not keeping functions running now.",
                "C": "Digital forensics investigates and preserves evidence; it does not keep operations running.",
                "D": "Penetration testing assesses security weaknesses; it is unrelated to continuity during a flood.",
            },
            "exam_pattern": "Keep operating during the event = BC; restore the systems afterward = DR.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - BC vs. DR"],
    },
    {
        "id": "isc2cc-bcdr-010", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 1, "type": "fill",
        "stem": "The document that lays out how an organization will keep its essential functions "
                "operating during and after a disruption is the business ___ plan. (one word)",
        "correct": ["continuity"],
        "explanation": {
            "correct": "The business continuity plan (BCP) documents the strategy and steps to sustain "
                       "essential operations through a disruption.",
            "exam_pattern": "Plan to keep operating through disruption = business continuity plan (BCP).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Business continuity (BCP)"],
    },
    {
        "id": "isc2cc-bcdr-011", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 2, "type": "mcq",
        "stem": "A consultant stresses that a business continuity program is far more likely to succeed "
                "if one group visibly backs it and funds it. Who is that group?",
        "options": [
            {"id": "A", "text": "Senior (executive) management"},
            {"id": "B", "text": "The external auditors"},
            {"id": "C", "text": "The marketing department"},
            {"id": "D", "text": "End users in general"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Senior management's sponsorship, funding, and visible support are essential for a "
                       "continuity program to be resourced and taken seriously across the organization.",
            "distractors": {
                "B": "Auditors assess the program's effectiveness; they do not sponsor or fund it.",
                "C": "Marketing is a business unit the plan protects, not the sponsor of the program.",
                "D": "General end users follow the plan but cannot authorize budget or enforce it enterprise-wide.",
            },
            "exam_pattern": "Program success depends on senior/executive management support and funding.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Business continuity (management support)"],
    },
    {
        "id": "isc2cc-bcdr-012", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity", "difficulty": 2, "type": "mcq",
        "stem": "A manufacturer keeps a fully staffed backup call center so customer support never "
                "stops, even if the primary site goes down. This is an example of:",
        "options": [
            {"id": "A", "text": "Maintaining continuity of an essential business function"},
            {"id": "B", "text": "Performing a forensic investigation"},
            {"id": "C", "text": "Conducting a risk transference via insurance"},
            {"id": "D", "text": "Hardening a server's configuration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An alternate, ready-to-run call center keeps the essential customer-support "
                       "function operating during a disruption - the goal of business continuity.",
            "distractors": {
                "B": "A forensic investigation gathers evidence after an incident; it does not keep support running.",
                "C": "Risk transference shifts financial loss to an insurer; a staffed backup site is not insurance.",
                "D": "Server hardening reduces attack surface; it is not about keeping a business function available.",
            },
            "exam_pattern": "An alternate site/staff that keeps a function running = business continuity.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Business continuity (continuity of operations)"],
    },

    # ===== cc_disaster_recovery =============================================
    {
        "id": "isc2cc-bcdr-013", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 1, "type": "mcq",
        "stem": "What does disaster recovery (DR) primarily focus on?",
        "options": [
            {"id": "A", "text": "Writing the organization's acceptable-use policy"},
            {"id": "B", "text": "Preventing phishing emails from reaching users"},
            {"id": "C", "text": "Classifying data as public or confidential"},
            {"id": "D", "text": "Restoring IT systems, data, and operations after a disruptive event"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Disaster recovery is the set of processes and tools used to restore IT systems, "
                       "data, and operations after a disaster so normal service can resume.",
            "distractors": {
                "A": "Writing an acceptable-use policy is a governance task, not disaster recovery.",
                "B": "Blocking phishing is an operational email-security control, not disaster recovery.",
                "C": "Data classification is a data-security activity, unrelated to restoring systems after a disaster.",
            },
            "exam_pattern": "Restore IT systems/data/operations after a disaster = disaster recovery.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (purpose)"],
    },
    {
        "id": "isc2cc-bcdr-014", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "An organization needs an alternate facility that is fully equipped with hardware, "
                "current data, and connectivity so it can take over almost immediately. This is a:",
        "options": [
            {"id": "A", "text": "Cold site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Hot site"},
            {"id": "D", "text": "Reciprocal site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A hot site is a fully operational alternate location with hardware, up-to-date "
                       "data, and connectivity, giving the fastest recovery (at the highest cost).",
            "distractors": {
                "A": "A cold site has only space, power, and cooling - no ready hardware or data - so it is slowest to activate.",
                "B": "A warm site is partially equipped (some hardware, but data must be loaded), slower than a hot site.",
                "D": "A reciprocal agreement shares another organization's facility; it is not a fully ready hot site.",
            },
            "exam_pattern": "Fully equipped, ready now, costliest = hot site; empty shell, cheapest, slowest = cold site.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (recovery sites)"],
    },
    {
        "id": "isc2cc-bcdr-015", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A small company wants the cheapest alternate site and accepts that bringing it online "
                "will be slow because it has only space, power, and cooling - no installed equipment. "
                "Which site type fits?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Mirror site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A cold site provides only the physical space and utilities; equipment and data must "
                       "be brought in and set up, making it the cheapest but slowest option.",
            "distractors": {
                "A": "A hot site is fully equipped and ready immediately - the opposite of cheap and slow.",
                "B": "A warm site has some equipment already in place, so it is faster and costlier than a cold site.",
                "D": "A mirror site is a real-time duplicate of production, the fastest and most expensive, not the cheapest.",
            },
            "exam_pattern": "Only space/power/cooling, cheapest, slowest to activate = cold site.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (recovery sites)"],
    },
    {
        "id": "isc2cc-bcdr-016", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A recovery plan states that after an outage the email system must be back up within "
                "4 hours. Which metric does the '4 hours to restore' describe?",
        "options": [
            {"id": "A", "text": "Annualized Loss Expectancy (ALE)"},
            {"id": "B", "text": "Recovery Point Objective (RPO)"},
            {"id": "C", "text": "Mean Time Between Failures (MTBF)"},
            {"id": "D", "text": "Recovery Time Objective (RTO)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Recovery Time Objective (RTO) is the target time within which a system or "
                       "process must be restored after a disruption - here, 4 hours.",
            "distractors": {
                "A": "ALE is a yearly expected-loss figure from risk analysis, not a recovery-time target.",
                "B": "RPO measures how much data loss is acceptable (how far back to recover), not how long restoration takes.",
                "C": "MTBF estimates average time between hardware failures, a reliability metric, not a recovery target.",
            },
            "exam_pattern": "'How fast must we be back up' = RTO (time); 'how much data can we lose' = RPO (data).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (RTO vs. RPO)"],
    },
    {
        "id": "isc2cc-bcdr-017", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A database team says it can tolerate losing at most 15 minutes of transactions if a "
                "crash occurs. Which recovery metric does the '15 minutes of data' describe?",
        "options": [
            {"id": "A", "text": "Recovery Time Objective (RTO)"},
            {"id": "B", "text": "Recovery Point Objective (RPO)"},
            {"id": "C", "text": "Maximum Tolerable Downtime (MTD)"},
            {"id": "D", "text": "Service-Level Agreement (SLA)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Recovery Point Objective (RPO) is the maximum acceptable amount of data loss, "
                       "expressed as a point in time - here, up to 15 minutes of transactions.",
            "distractors": {
                "A": "RTO is the time allowed to restore service, not the amount of data loss tolerated.",
                "C": "MTD is the total time a function can be down before unacceptable harm, not the data-loss limit.",
                "D": "An SLA is a service commitment between parties, not a specific data-loss metric.",
            },
            "exam_pattern": "Acceptable data loss (point to recover to) = RPO; often set by backup frequency.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (RTO vs. RPO)"],
    },
    {
        "id": "isc2cc-bcdr-018", "exam": "isc2cc", "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A backup job copies only the files changed since the last FULL backup. Each night's "
                "backup grows larger, but a restore needs just the full backup plus the latest job. "
                "Which backup type is this?",
        "options": [
            {"id": "A", "text": "Incremental backup"},
            {"id": "B", "text": "Differential backup"},
            {"id": "C", "text": "Full backup"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A differential backup captures everything changed since the last full backup, so it "
                       "grows over time, and a restore requires only the full plus the most recent differential.",
            "distractors": {
                "A": "An incremental backup copies changes since the last backup of any kind, so a restore needs the full plus every incremental in order.",
                "C": "A full backup copies all selected data every time; it does not copy 'only changes since the last full.'",
                "D": "A snapshot is a point-in-time image of a system/volume, not the described change-based file backup.",
            },
            "exam_pattern": "Changes since last FULL = differential (restore: full + last diff); changes since last ANY backup = incremental.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (backup types)"],
    },
]
