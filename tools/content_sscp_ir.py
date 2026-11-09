"""(ISC)2 SSCP pool - Domain 4: Incident Response and Recovery.

Original, objective-aligned practice items for the three Incident Response and
Recovery subtopics tracked in CertLab:
  * sscp_incident_handling - the IR lifecycle (preparation, detection &
                             analysis, containment, eradication, recovery,
                             lessons learned) and the role of each phase.
  * sscp_forensics         - order of volatility, chain of custody, forensic
                             imaging and hashing, and write blockers.
  * sscp_bcp_dr            - BIA, RTO/RPO, backup types (full/incremental/
                             differential), and recovery site types.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_incident_handling ===========================================
    {
        "id": "sscp-ir-001", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 2, "type": "mcq",
        "stem": "Which sequence correctly orders the phases of the incident response lifecycle?",
        "options": [
            {"id": "A", "text": "Containment -> Preparation -> Recovery -> Detection"},
            {"id": "B", "text": "Preparation -> Detection & Analysis -> Containment -> Eradication -> Recovery -> Lessons Learned"},
            {"id": "C", "text": "Detection -> Recovery -> Preparation -> Containment"},
            {"id": "D", "text": "Eradication -> Containment -> Detection -> Preparation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The lifecycle runs Preparation, Detection & Analysis, Containment, Eradication, "
                       "Recovery, then Lessons Learned - you prepare first and capture improvements last.",
            "distractors": {
                "A": "You cannot contain before you have prepared and detected; the order is scrambled.",
                "C": "Recovery cannot precede containment and eradication of the threat.",
                "D": "This fully reverses the lifecycle; preparation comes first, not last.",
            },
            "exam_pattern": "Prepare -> Detect/Analyze -> Contain -> Eradicate -> Recover -> Lessons Learned.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Incident response lifecycle"],
    },
    {
        "id": "sscp-ir-002", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 1, "type": "mcq",
        "stem": "During an active malware outbreak, the SOC immediately isolates infected hosts from "
                "the network to stop the spread, before cleaning them. Which IR phase is this?",
        "options": [
            {"id": "A", "text": "Eradication"},
            {"id": "B", "text": "Recovery"},
            {"id": "C", "text": "Containment"},
            {"id": "D", "text": "Lessons learned"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Isolating affected systems to limit the scope and stop propagation is "
                       "containment - done before removing the threat.",
            "distractors": {
                "A": "Eradication is removing the malware and closing the root cause, which follows containment.",
                "B": "Recovery restores systems to normal operation after the threat is gone.",
                "D": "Lessons learned is the post-incident review phase, not the immediate isolation action.",
            },
            "exam_pattern": "Stop the spread / isolate = containment (comes before eradication).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Containment"],
    },
    {
        "id": "sscp-ir-003", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 2, "type": "mcq",
        "stem": "After isolating affected systems, the team removes the malware, deletes attacker "
                "artifacts, and patches the exploited vulnerability so it cannot be reused. Which IR "
                "phase does this describe?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Preparation"},
            {"id": "C", "text": "Detection"},
            {"id": "D", "text": "Eradication"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Eradication removes the threat and its root cause - deleting malware/artifacts "
                       "and closing the vulnerability that allowed the compromise.",
            "distractors": {
                "A": "Containment limited the spread earlier; it does not remove the threat.",
                "B": "Preparation happens before any incident, building plans and tooling.",
                "C": "Detection is identifying that an incident is occurring, not removing the cause.",
            },
            "exam_pattern": "Remove malware + fix root cause = eradication; restore service = recovery.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Eradication"],
    },
    {
        "id": "sscp-ir-004", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 1, "type": "mcq",
        "stem": "Once systems are restored and stable, the team holds a structured meeting to document "
                "what happened, what worked, and how to improve defenses and the plan. Which IR phase "
                "is this?",
        "options": [
            {"id": "A", "text": "Detection"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Lessons learned (post-incident activity)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The lessons-learned (post-incident) phase reviews the incident to capture "
                       "improvements to controls, detection, and the response plan itself.",
            "distractors": {
                "A": "Detection is recognizing the incident, which already happened earlier.",
                "B": "Containment limited damage during the incident, not afterward.",
                "C": "Eradication removed the threat; the review of the whole event comes after recovery.",
            },
            "exam_pattern": "Post-recovery review to improve = lessons learned (feeds back into preparation).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Lessons learned"],
    },
    {
        "id": "sscp-ir-005", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 2, "type": "mcq",
        "stem": "Maintaining an up-to-date incident response plan, a trained response team, contact "
                "lists, and tested tools BEFORE any incident occurs belongs to which IR phase?",
        "options": [
            {"id": "A", "text": "Preparation"},
            {"id": "B", "text": "Recovery"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Detection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Preparation is the readiness phase: building and maintaining the plan, team, "
                       "training, communications, and tooling so the organization can respond "
                       "effectively.",
            "distractors": {
                "B": "Recovery restores normal operations after an incident, not beforehand.",
                "C": "Eradication removes a threat during an active incident.",
                "D": "Detection identifies an incident in progress; readiness work precedes it.",
            },
            "exam_pattern": "All the 'before it happens' readiness work = preparation (the foundation phase).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Preparation"],
    },

    # ===== sscp_forensics ===================================================
    {
        "id": "sscp-ir-006", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 3, "type": "mcq",
        "stem": "A responder must collect digital evidence from a running system. Following the order "
                "of volatility, which data source should be collected FIRST?",
        "options": [
            {"id": "A", "text": "Data on backup tapes in off-site storage"},
            {"id": "B", "text": "Files saved on the system's hard disk"},
            {"id": "C", "text": "The contents of RAM and CPU cache/registers"},
            {"id": "D", "text": "Archived logs on a remote server"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The order of volatility (RFC 3227) collects the most volatile data first: CPU "
                       "registers/cache and system memory (RAM) vanish on power loss, so they are "
                       "captured before disk and archival media.",
            "distractors": {
                "A": "Backup tapes are among the least volatile sources and are collected last.",
                "B": "Disk data persists across reboots and is collected after volatile memory.",
                "D": "Remote archived logs are relatively stable and are gathered after volatile host state.",
            },
            "exam_pattern": "Most volatile first: registers/cache -> RAM -> temp files -> disk -> remote/archival media.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Order of volatility (RFC 3227)"],
    },
    {
        "id": "sscp-ir-007", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 1, "type": "mcq",
        "stem": "Which documentation records every person who collected, handled, transferred, or "
                "stored a piece of evidence, so its integrity can be defended in court?",
        "options": [
            {"id": "A", "text": "Chain of custody"},
            {"id": "B", "text": "Service-level agreement"},
            {"id": "C", "text": "Business impact analysis"},
            {"id": "D", "text": "Acceptable use policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Chain of custody is the chronological record of who handled evidence, when, and "
                       "why - essential to prove it was not altered and to make it admissible.",
            "distractors": {
                "B": "An SLA defines service commitments between parties, not evidence handling.",
                "C": "A BIA assesses the impact of disruptions for continuity planning.",
                "D": "An AUP governs acceptable use of IT resources, unrelated to evidence tracking.",
            },
            "exam_pattern": "Who-touched-the-evidence-when record = chain of custody (preserves admissibility).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Chain of custody"],
    },
    {
        "id": "sscp-ir-008", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 2, "type": "mcq",
        "stem": "Before examining a suspect hard drive, a forensic analyst connects it through a device "
                "that allows the drive to be read but prevents any data from being written back to it. "
                "What is this device?",
        "options": [
            {"id": "A", "text": "A degausser"},
            {"id": "B", "text": "A write blocker"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A KVM switch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A write blocker permits read access while blocking any writes to the original "
                       "media, preserving the evidence in its original state during acquisition.",
            "distractors": {
                "A": "A degausser erases magnetic media - it would destroy the very evidence being examined.",
                "C": "A load balancer distributes network traffic and has no forensic function.",
                "D": "A KVM switch shares a keyboard/monitor across systems; it does not protect media from writes.",
            },
            "exam_pattern": "Read-only acquisition of original media = write blocker (protects integrity).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Forensic acquisition and write blockers"],
    },
    {
        "id": "sscp-ir-009", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 3, "type": "mcq",
        "stem": "A forensic analyst makes a bit-for-bit image of a drive and computes a SHA-256 hash of "
                "both the original and the image. What does matching the two hash values establish?",
        "options": [
            {"id": "A", "text": "That the image has been compressed to save space"},
            {"id": "B", "text": "That the evidence has been encrypted for confidentiality"},
            {"id": "C", "text": "That the image is an exact, unaltered copy of the original (integrity verification)"},
            {"id": "D", "text": "That the imaging process ran faster than normal"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Equal hashes before and after imaging prove the copy is identical to the "
                       "original and that neither has changed - the integrity check that makes analysis "
                       "on the copy defensible.",
            "distractors": {
                "A": "Hashing verifies integrity; it does not compress data.",
                "B": "A hash is a one-way integrity digest, not encryption for confidentiality.",
                "D": "Hash comparison says nothing about imaging speed.",
            },
            "exam_pattern": "Hash original and image; matching values prove an exact, unaltered copy.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Imaging and hashing"],
    },
    {
        "id": "sscp-ir-010", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 2, "type": "fill",
        "stem": "To preserve original evidence, forensic examiners perform their analysis on a "
                "bit-for-bit forensic ____ of the drive rather than on the original media. Provide the "
                "one-word term for this exact copy.",
        "correct": ["image", "copy", "forensic image", "clone"],
        "explanation": {
            "correct": "Analysts work on a forensic image (an exact bit-for-bit copy) so the original "
                       "evidence remains untouched and its integrity provable via hashing.",
            "distractors": {},
            "exam_pattern": "Never work on the original - analyze a hashed forensic image/copy.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Evidence preservation"],
    },

    # ===== sscp_bcp_dr ======================================================
    {
        "id": "sscp-ir-011", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 2, "type": "multi",
        "stem": "A business impact analysis (BIA) identifies critical functions and the consequences "
                "of their disruption. Which TWO key recovery metrics does the BIA help establish to "
                "prioritize restoration? (Choose two.)",
        "options": [
            {"id": "A", "text": "Recovery Time Objective (RTO)"},
            {"id": "B", "text": "Recovery Point Objective (RPO)"},
            {"id": "C", "text": "Annualized Rate of Occurrence (ARO)"},
            {"id": "D", "text": "Mean Time Between Failures (MTBF)"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "The BIA drives the RTO (how quickly a function must be restored) and the RPO "
                       "(how much data loss, measured in time, is tolerable) used to prioritize and "
                       "design recovery.",
            "distractors": {
                "C": "ARO is a quantitative risk metric (incident frequency per year), not a BIA recovery objective.",
                "D": "MTBF is a reliability/hardware metric, not a continuity recovery objective.",
            },
            "exam_pattern": "BIA outputs the recovery objectives: RTO (downtime tolerance) and RPO (data-loss tolerance).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Business impact analysis"],
    },
    {
        "id": "sscp-ir-012", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "Management determines that, in a disaster, the business can tolerate losing at most 15 "
                "minutes' worth of transaction data. Which recovery metric does this 15-minute figure "
                "define?",
        "options": [
            {"id": "A", "text": "Recovery Time Objective (RTO)"},
            {"id": "B", "text": "Recovery Point Objective (RPO)"},
            {"id": "C", "text": "Maximum Tolerable Downtime (MTD)"},
            {"id": "D", "text": "Mean Time to Repair (MTTR)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RPO defines the maximum acceptable amount of data loss measured in time - here, "
                       "15 minutes - which dictates how frequently backups/replication must occur.",
            "distractors": {
                "A": "RTO is how quickly service must be restored (downtime), not how much data loss is acceptable.",
                "C": "MTD is the absolute maximum outage a function can survive, not the data-loss window.",
                "D": "MTTR is the average time to repair a failed component, a maintainability metric.",
            },
            "exam_pattern": "RPO = tolerable DATA loss (time); RTO = tolerable DOWNTIME (time).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - RTO and RPO"],
    },
    {
        "id": "sscp-ir-013", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "The targeted duration within which a critical business process must be restored after "
                "a disruption, in order to avoid unacceptable consequences, is defined by which metric?",
        "options": [
            {"id": "A", "text": "Recovery Point Objective (RPO)"},
            {"id": "B", "text": "Mean Time Between Failures (MTBF)"},
            {"id": "C", "text": "Recovery Time Objective (RTO)"},
            {"id": "D", "text": "Single Loss Expectancy (SLE)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RTO is the target time to restore a process/service after an outage; recovery "
                       "capabilities are designed to meet it.",
            "distractors": {
                "A": "RPO addresses tolerable data loss, not restoration time.",
                "B": "MTBF measures expected time between failures, a reliability metric.",
                "D": "SLE is the expected monetary loss from a single incident, a risk metric.",
            },
            "exam_pattern": "RTO = how fast you must be back up; RPO = how much data you can lose.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Recovery objectives"],
    },
    {
        "id": "sscp-ir-014", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "An organization requires the ability to fail over operations within minutes of a "
                "disaster declaration. Which alternate-site type is required to meet this need?",
        "options": [
            {"id": "A", "text": "Cold site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Reciprocal agreement"},
            {"id": "D", "text": "Hot site"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A hot site is fully equipped and kept current with near-live data, allowing "
                       "near-immediate failover (minutes to a couple of hours) - the only option that "
                       "meets a minutes-level RTO.",
            "distractors": {
                "A": "A cold site provides space and utilities only; standing it up takes days to weeks.",
                "B": "A warm site has some hardware/connectivity but still needs hours to days to become operational.",
                "C": "A reciprocal agreement relies on another organization's capacity and offers no guaranteed rapid failover.",
            },
            "exam_pattern": "Fastest failover (most costly) = hot site; cheapest/slowest = cold site; warm is in between.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Recovery site types"],
    },
    {
        "id": "sscp-ir-015", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "A backup scheme runs a full backup every Sunday, and on each weekday it backs up only "
                "the data changed since the LAST backup of any kind, clearing the archive bit each "
                "time. Which backup type runs on the weekdays?",
        "options": [
            {"id": "A", "text": "Incremental backup"},
            {"id": "B", "text": "Differential backup"},
            {"id": "C", "text": "Full backup"},
            {"id": "D", "text": "Snapshot-only backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An incremental backup captures only what changed since the last backup (full or "
                       "incremental) and clears the archive bit. Backups are fast and small, but "
                       "restoration needs the last full plus every incremental in order.",
            "distractors": {
                "B": "A differential backs up everything changed since the last FULL and does not clear the archive bit, so each one grows larger.",
                "C": "A full backup copies all selected data every time, not just the changes.",
                "D": "'Snapshot-only' does not match the described change-since-last-backup, archive-bit-clearing behavior.",
            },
            "exam_pattern": "Incremental = since last backup, clears archive bit (fast backup, slow restore); differential = since last full (slow backup, fast restore).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Backup strategies"],
    },
]
