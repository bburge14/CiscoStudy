"""ISACA CISA pool - Domain 4: IS Operations and Business Resilience.

Original, objective-aligned practice items for the six Domain 4 subtopics
tracked in the study engine:
  * cisa_it_operations      - change management (incl. emergency changes),
                              capacity management, operator console-log review.
  * cisa_system_interfaces  - interface reconciliation/control totals, interface
                              integrity risk, suspense/error handling of rejects.
  * cisa_data_backup_recovery - grandfather-father-son rotation, full vs.
                              incremental vs. differential backups, restoration
                              testing and offsite storage.
  * cisa_disaster_recovery  - recovery sites (hot/warm/cold/mobile/reciprocal),
                              matching sites to RTO, DR test types.
  * cisa_incident_problem_mgmt - ITIL incident vs. problem management, incident
                              logging and escalation.
  * cisa_database_mgmt       - referential integrity, normalization, controls
                              over privileged DBA access.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's resilience-and-controls mindset. All items are ORIGINAL and aligned to
public exam objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cisa_it_operations ===============================================
    {
        "id": "cisa-ops-001", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor is reviewing change management. For emergency changes applied directly to "
                "production, the MINIMUM acceptable control is that they are:",
        "options": [
            {"id": "A", "text": "Never allowed under any circumstances"},
            {"id": "B", "text": "Documented and reviewed/approved after the fact (retroactively authorized)"},
            {"id": "C", "text": "Applied by the developer without any record"},
            {"id": "D", "text": "Left undocumented to save time during the emergency"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Emergency changes are sometimes unavoidable, but at minimum they must be logged and "
                       "subsequently reviewed and formally approved (retroactive authorization) so the change stays "
                       "controlled and traceable.",
            "distractors": {
                "A": "An absolute ban is impractical; emergencies occur and the process must handle them with controls.",
                "C": "Applying changes with no record removes all traceability and accountability.",
                "D": "Leaving changes undocumented defeats change control entirely.",
            },
            "exam_pattern": "Emergency changes are permitted but must be logged and retroactively reviewed/approved.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Change and release management"],
    },
    {
        "id": "cisa-ops-002", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "Which IT operations process ensures that computing resources are sufficient to meet "
                "current and anticipated future business demand?",
        "options": [
            {"id": "A", "text": "Incident management"},
            {"id": "B", "text": "Change management"},
            {"id": "C", "text": "Capacity management"},
            {"id": "D", "text": "Problem management"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Capacity management monitors and plans resource utilization (CPU, storage, bandwidth) so "
                       "capacity meets current and future demand cost-effectively.",
            "distractors": {
                "A": "Incident management restores service after disruptions; it does not plan capacity.",
                "B": "Change management controls modifications, not resource sufficiency.",
                "D": "Problem management addresses the root cause of incidents, not capacity planning.",
            },
            "exam_pattern": "Match resources to current/future demand = capacity management.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Capacity and performance management"],
    },
    {
        "id": "cisa-ops-003", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_it_operations", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY reason an IS auditor reviews computer operator console logs?",
        "options": [
            {"id": "A", "text": "To improve application screen design"},
            {"id": "B", "text": "To measure network bandwidth usage"},
            {"id": "C", "text": "To calculate software license fees"},
            {"id": "D", "text": "To detect unauthorized or unusual operator actions and interventions"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Operator console logs record operator actions; reviewing them is a detective control to "
                       "identify unauthorized, unusual, or inappropriate interventions.",
            "distractors": {
                "A": "Screen design is a development concern, not what console logs reveal.",
                "B": "Bandwidth is monitored by network tools, not operator console logs.",
                "C": "License fees are not derived from console logs.",
            },
            "exam_pattern": "Console-log review = detect unauthorized/unusual operator activity (a detective control).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — IT operations monitoring"],
    },

    # ===== cisa_system_interfaces ===========================================
    {
        "id": "cisa-ops-004", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 2, "type": "mcq",
        "stem": "Two applications exchange transactions automatically through an interface. Which control "
                "BEST ensures that all transactions sent by the source system are received and processed by "
                "the target system?",
        "options": [
            {"id": "A", "text": "Reconciliation of transaction counts and control totals between the two systems"},
            {"id": "B", "text": "Encrypting the interface traffic"},
            {"id": "C", "text": "Restricting physical access to the server room"},
            {"id": "D", "text": "Requiring strong passwords for end users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reconciling record/transaction counts and control totals between the sending and "
                       "receiving systems directly confirms that data passed completely and accurately across the interface.",
            "distractors": {
                "B": "Encryption protects confidentiality in transit but does not confirm completeness of processing.",
                "C": "Physical access control protects the facility, not interface completeness.",
                "D": "Password strength addresses access control, not interface data integrity.",
            },
            "exam_pattern": "Confirm complete/accurate transfer between systems by reconciling counts and control totals.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — System interface controls"],
    },
    {
        "id": "cisa-ops-005", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 2, "type": "mcq",
        "stem": "When reviewing an automated interface that passes data between two applications, which "
                "risk should MOST concern the IS auditor?",
        "options": [
            {"id": "A", "text": "The interface uses a modern file format"},
            {"id": "B", "text": "The two systems were built by different vendors"},
            {"id": "C", "text": "Data may be transferred incompletely or inaccurately, compromising integrity"},
            {"id": "D", "text": "The interface runs during business hours"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The core risk of a data interface is loss of integrity - incomplete, duplicated, or "
                       "inaccurate transfer - which is why reconciliation and error-handling controls are essential.",
            "distractors": {
                "A": "A modern file format is not inherently a risk.",
                "B": "Different vendors is common and not itself the primary risk when interfaces are controlled.",
                "D": "Running during business hours is a scheduling choice, not the main integrity risk.",
            },
            "exam_pattern": "The primary interface risk is incomplete/inaccurate data transfer (integrity).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — System interface risk"],
    },
    {
        "id": "cisa-ops-006", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_system_interfaces", "difficulty": 3, "type": "mcq",
        "stem": "Transactions that fail an interface's edit/validation checks should be:",
        "options": [
            {"id": "A", "text": "Automatically deleted so they do not clutter the system"},
            {"id": "B", "text": "Written to a suspense/error file and followed up for correction and reprocessing"},
            {"id": "C", "text": "Forced through so that no transaction is ever lost"},
            {"id": "D", "text": "Ignored, because the sending system already validated them"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Rejected transactions should be captured in a suspense/error file and monitored so they "
                       "are investigated, corrected, and reprocessed - ensuring no valid transaction is lost and no "
                       "invalid one is accepted.",
            "distractors": {
                "A": "Deleting rejected transactions loses data and destroys the audit trail.",
                "C": "Forcing invalid transactions through defeats the edit checks and corrupts data.",
                "D": "Assuming the sending system validated them removes an essential independent control.",
            },
            "exam_pattern": "Rejected items go to a suspense file for follow-up/reprocessing - never deleted or forced through.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Interface error handling"],
    },

    # ===== cisa_data_backup_recovery ========================================
    {
        "id": "cisa-ops-007", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The backup media rotation scheme that keeps daily (son), weekly "
                "(father), and monthly (grandfather) backup sets is known as the ______-father-son scheme.",
        "correct": ["grandfather", "grandfather-father-son", "gfs"],
        "explanation": {
            "correct": "The grandfather-father-son (GFS) scheme rotates daily, weekly, and monthly backup "
                       "generations, balancing recovery granularity against media cost and retention.",
            "distractors": {},
            "exam_pattern": "Daily/weekly/monthly generations = grandfather-father-son (GFS) rotation.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Backup schemes"],
    },
    {
        "id": "cisa-ops-008", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Which backup type copies only the data that has changed since the last FULL backup?",
        "options": [
            {"id": "A", "text": "Full backup"},
            {"id": "B", "text": "Incremental backup"},
            {"id": "C", "text": "Differential backup"},
            {"id": "D", "text": "Mirror backup"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A differential backup copies everything changed since the last full backup; restoration "
                       "needs only the last full plus the most recent differential.",
            "distractors": {
                "A": "A full backup copies all data, not only what changed.",
                "B": "An incremental backup copies data changed since the last backup of any type, not since the last full.",
                "D": "A mirror is a complete real-time copy, not a 'since last full' delta.",
            },
            "exam_pattern": "Differential = changes since last FULL; incremental = changes since last ANY backup.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Backup types"],
    },
    {
        "id": "cisa-ops-009", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_data_backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "When reviewing an organization's backup program, which finding should concern the IS "
                "auditor MOST?",
        "options": [
            {"id": "A", "text": "Backups are encrypted"},
            {"id": "B", "text": "Backups are scheduled to run nightly"},
            {"id": "C", "text": "A copy of backups is stored offsite"},
            {"id": "D", "text": "The restoration of backups has never been tested"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Untested backups may be unusable when needed; the ability to actually restore is what "
                       "matters, so never having tested restoration is the most serious concern.",
            "distractors": {
                "A": "Encrypting backups is a good control, not a concern.",
                "B": "Nightly backups are a sound practice.",
                "C": "Offsite storage is a recommended control, not a concern.",
            },
            "exam_pattern": "A backup you cannot restore is worthless - test restoration, don't just take backups.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Backup and restoration testing"],
    },

    # ===== cisa_disaster_recovery ===========================================
    {
        "id": "cisa-ops-010", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A critical system has a recovery time objective (RTO) of two hours. Which type of "
                "recovery site is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Cold site"},
            {"id": "C", "text": "Reciprocal agreement with another company"},
            {"id": "D", "text": "No alternate site"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hot site is fully equipped and kept current, enabling recovery within hours - the only "
                       "option that reliably meets a very short RTO such as two hours.",
            "distractors": {
                "B": "A cold site provides only space and utilities and takes days or weeks to make operational.",
                "C": "A reciprocal agreement offers uncertain capacity and readiness, unsuitable for a tight RTO.",
                "D": "No alternate site cannot meet any recovery objective.",
            },
            "exam_pattern": "Very short RTO demands a hot site (ready to run); longer RTOs can tolerate warm/cold.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Recovery sites and RTO"],
    },
    {
        "id": "cisa-ops-011", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 1, "type": "mcq",
        "stem": "A recovery site that provides environmental infrastructure such as space, power, and "
                "HVAC but contains no installed computing equipment is a:",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Mobile site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A cold site provides only the facility and utilities; hardware, software, and data must "
                       "be brought in and installed, making it the cheapest but slowest option.",
            "distractors": {
                "A": "A hot site is fully equipped and nearly current, ready in hours.",
                "B": "A warm site has some hardware/connectivity in place but not fully current data.",
                "D": "A mobile site is a transportable, pre-configured unit, not merely empty conditioned space.",
            },
            "exam_pattern": "Cold = space/power only (cheapest, slowest); warm = partial; hot = full/ready.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Types of recovery sites"],
    },
    {
        "id": "cisa-ops-012", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 3, "type": "mcq",
        "stem": "What is the MAIN disadvantage of relying on a reciprocal agreement between two "
                "organizations for disaster recovery?",
        "options": [
            {"id": "A", "text": "It is always the most expensive recovery option"},
            {"id": "B", "text": "The partner may lack capacity or a compatible configuration when a disaster occurs, and the arrangement is hard to enforce"},
            {"id": "C", "text": "It provides a fully equipped, dedicated recovery site"},
            {"id": "D", "text": "It eliminates the need to maintain a recovery plan"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Reciprocal (mutual-aid) agreements are inexpensive but risky: the partner's capacity, "
                       "configuration, and availability may be inadequate at the moment of need, and such agreements "
                       "are difficult to enforce.",
            "distractors": {
                "A": "Reciprocal agreements are typically the cheapest option, not the most expensive.",
                "C": "They do not provide a dedicated, fully equipped site - that describes a hot site.",
                "D": "A recovery plan is still required regardless of the agreement.",
            },
            "exam_pattern": "Reciprocal agreement = cheap but unreliable (capacity/compatibility/enforceability doubts).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Reciprocal agreements"],
    },
    {
        "id": "cisa-ops-013", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_disaster_recovery", "difficulty": 3, "type": "multi",
        "stem": "Which TWO disaster recovery test types validate recovery by actually processing real "
                "workloads (not just discussion or review)? (Choose two.)",
        "options": [
            {"id": "A", "text": "Structured walkthrough (paper) test"},
            {"id": "B", "text": "Tabletop discussion exercise"},
            {"id": "C", "text": "Parallel test"},
            {"id": "D", "text": "Full-interruption test"},
        ],
        "correct": ["C", "D"],
        "explanation": {
            "correct": "A parallel test processes real workloads at the alternate site alongside production, and "
                       "a full-interruption test shifts live processing to the alternate site - both exercise actual recovery.",
            "distractors": {
                "A": "A structured walkthrough reviews the plan on paper without processing real transactions.",
                "B": "A tabletop exercise is a discussion-based scenario walkthrough, with no live processing.",
            },
            "exam_pattern": "Parallel and full-interruption tests exercise real recovery; walkthrough/tabletop are discussion-only.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — DR testing methods"],
    },

    # ===== cisa_incident_problem_mgmt =======================================
    {
        "id": "cisa-ops-014", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 1, "type": "mcq",
        "stem": "In IT service management (ITIL) practice, what is the PRIMARY objective of incident "
                "management?",
        "options": [
            {"id": "A", "text": "To restore normal service operation as quickly as possible and minimize business impact"},
            {"id": "B", "text": "To identify and permanently eliminate the root cause of incidents"},
            {"id": "C", "text": "To authorize and schedule changes to the environment"},
            {"id": "D", "text": "To plan long-term capacity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Incident management aims to restore normal service as quickly as possible to limit "
                       "business impact; finding the underlying root cause is the job of problem management.",
            "distractors": {
                "B": "Eliminating root cause is problem management, not incident management.",
                "C": "Authorizing and scheduling changes is change management.",
                "D": "Capacity planning is capacity management.",
            },
            "exam_pattern": "Incident = restore service fast; Problem = fix root cause; Change = control modifications.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Incident vs. problem management"],
    },
    {
        "id": "cisa-ops-015", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The IT service management process whose goal is to identify and remove "
                "the underlying root cause of recurring incidents is called ______ management.",
        "correct": ["problem", "problem management"],
        "explanation": {
            "correct": "Problem management investigates the root cause of incidents and drives permanent fixes so "
                       "the incidents stop recurring, complementing incident management's focus on fast restoration.",
            "distractors": {},
            "exam_pattern": "Root-cause elimination of recurring incidents = problem management.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Problem management"],
    },
    {
        "id": "cisa-ops-016", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_incident_problem_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor reviewing the incident-management process would be MOST concerned if:",
        "options": [
            {"id": "A", "text": "Incidents are assigned a severity level"},
            {"id": "B", "text": "Incidents are not recorded/logged, so there is no tracking or trend analysis"},
            {"id": "C", "text": "Incidents are escalated to senior staff when needed"},
            {"id": "D", "text": "Incident reports are reviewed by management"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "If incidents are not logged, the organization cannot track, prioritize, analyze trends, "
                       "or demonstrate resolution - undermining the entire incident-management and monitoring process.",
            "distractors": {
                "A": "Assigning severity is a good practice, not a concern.",
                "C": "Escalation when needed is appropriate.",
                "D": "Management review of incidents is a sound control.",
            },
            "exam_pattern": "No incident logging = no tracking, no trends, no accountability - the auditor's biggest concern.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Incident recording and escalation"],
    },

    # ===== cisa_database_mgmt ===============================================
    {
        "id": "cisa-ops-017", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "Which database control ensures that a foreign key value in one table always corresponds "
                "to an existing primary key in the related table, preventing orphan records?",
        "options": [
            {"id": "A", "text": "Normalization"},
            {"id": "B", "text": "Data encryption"},
            {"id": "C", "text": "Referential integrity"},
            {"id": "D", "text": "Concurrency control"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Referential integrity enforces that every foreign key matches a valid primary key in the "
                       "referenced table, preventing orphaned records and preserving relational consistency.",
            "distractors": {
                "A": "Normalization organizes tables to reduce redundancy; it does not by itself enforce key relationships at runtime.",
                "B": "Encryption protects confidentiality, not relational consistency.",
                "D": "Concurrency control manages simultaneous access, not key relationships.",
            },
            "exam_pattern": "Foreign key must point to a valid primary key = referential integrity (no orphans).",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Database integrity controls"],
    },
    {
        "id": "cisa-ops-018", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of normalizing a relational database?",
        "options": [
            {"id": "A", "text": "To reduce data redundancy and improve data integrity"},
            {"id": "B", "text": "To encrypt sensitive fields"},
            {"id": "C", "text": "To increase the number of duplicate records for backup"},
            {"id": "D", "text": "To speed up the physical network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Normalization organizes data into related tables to minimize redundancy and the update "
                       "anomalies it causes, improving data integrity.",
            "distractors": {
                "B": "Encryption, not normalization, protects confidentiality.",
                "C": "Normalization reduces duplication; it does not create duplicates.",
                "D": "Network speed is unrelated to logical data normalization.",
            },
            "exam_pattern": "Normalization = reduce redundancy and the anomalies that threaten integrity.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Database normalization"],
    },
    {
        "id": "cisa-ops-019", "exam": "cisa", "domain": "cisa_operations_resilience",
        "subtopic": "cisa_database_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Because a database administrator (DBA) holds powerful, privileged access that can bypass "
                "application controls, which is the BEST control over DBA activity?",
        "options": [
            {"id": "A", "text": "Removing the DBA role entirely"},
            {"id": "B", "text": "Letting the DBA review their own activity logs"},
            {"id": "C", "text": "Giving all developers the same DBA access for balance"},
            {"id": "D", "text": "Logging DBA activities and having them independently reviewed by someone outside the DBA function"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Because a DBA can bypass normal controls, the key compensating control is to log all "
                       "privileged DBA actions and have those logs reviewed independently by someone outside the DBA function.",
            "distractors": {
                "A": "The DBA role is necessary; removing it is impractical.",
                "B": "Self-review of one's own logs is not an independent control.",
                "C": "Granting more people privileged access widens the risk rather than controlling it.",
            },
            "exam_pattern": "Powerful privileged accounts (DBA) need logging + independent review of that log.",
        },
        "references": ["ISACA CISA Review Manual: Domain 4 — Privileged access and the DBA"],
    },
]
