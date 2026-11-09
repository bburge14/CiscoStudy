"""CompTIA Cloud+ (CV0-004) pool - Domain 3: Operations.

Original, objective-aligned practice items for the four Operations subtopics
tracked in CertLab:
  * cloudp_logging_monitoring    - metrics and threshold alerting, SIEM, APM,
                                   centralized log aggregation.
  * cloudp_maintenance_automation - patch management, maintenance windows,
                                   orchestration, automation use cases.
  * cloudp_backup_restore        - full/incremental/differential, snapshots,
                                   RTO/RPO, the 3-2-1 rule.
  * cloudp_optimization          - rightsizing, reserved capacity, cost-allocation
                                   tagging, auto-scaling for cost.

Cloud+ is vendor-NEUTRAL: a vendor is named only as an example, never as the sole
key. build_content.py shuffles option order (seeded by id), so no key is positionally
biased; every wrong option carries a distractor note, and each item cites the public
CV0-004 objective domain it draws on. Original items only, never real exam content.
"""

QUESTIONS = [
    # ===== cloudp_logging_monitoring ========================================
    {
        "id": "cloudplus-ops-001", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An operations team wants to be automatically notified when a service's error rate crosses a defined "
                "threshold so they can react before users complain. What must they configure on their monitoring metrics?",
        "options": [
            {"id": "A", "text": "A snapshot schedule"},
            {"id": "B", "text": "An alert (threshold-based alarm) on the metric"},
            {"id": "C", "text": "A new subnet"},
            {"id": "D", "text": "A golden image"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Alerting evaluates metrics against thresholds (static or dynamic) and notifies responders or triggers "
                       "automation when breached, enabling proactive response.",
            "distractors": {
                "A": "A snapshot schedule captures data backups; it does not notify on metric thresholds.",
                "C": "A subnet is a network segment; it has nothing to do with metric alerting.",
                "D": "A golden image is a deployment baseline, unrelated to monitoring notifications.",
            },
            "exam_pattern": "Notify when a metric crosses a threshold = configure an alert/alarm.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring and alerting"],
    },
    {
        "id": "cloudplus-ops-002", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants one platform that collects logs from servers, firewalls, and applications, "
                "then correlates events to detect and alert on suspicious activity. Which type of system is this?",
        "options": [
            {"id": "A", "text": "SIEM (Security Information and Event Management)"},
            {"id": "B", "text": "CDN (Content Delivery Network)"},
            {"id": "C", "text": "CMDB (Configuration Management Database)"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM aggregates and normalizes logs/events from many sources and correlates them to detect threats, "
                       "raise alerts, and support investigations and compliance.",
            "distractors": {
                "B": "A CDN caches and delivers content; it does not correlate security events.",
                "C": "A CMDB inventories configuration items and relationships; it is not an event-correlation/alerting engine.",
                "D": "A load balancer distributes traffic; it has no security-event correlation role.",
            },
            "exam_pattern": "Aggregate + correlate logs to detect/alert on threats = SIEM.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Logging/monitoring (SIEM)"],
    },
    {
        "id": "cloudplus-ops-003", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Developers need visibility into application response times, transaction traces, and where latency is "
                "introduced across microservices. Which class of tool best provides this?",
        "options": [
            {"id": "A", "text": "A DNS analyzer"},
            {"id": "B", "text": "A RAID controller"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "APM (Application Performance Monitoring)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "APM tools instrument applications to measure response times, throughput, and errors and to trace "
                       "requests across services, pinpointing where latency or failures occur.",
            "distractors": {
                "A": "A DNS analyzer inspects name resolution, not application transaction performance.",
                "B": "A RAID controller manages disk arrays; it is unrelated to application tracing.",
                "C": "A SIEM focuses on security-event correlation, not detailed application performance traces.",
            },
            "exam_pattern": "Transaction traces, response times across services = APM.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring (APM)"],
    },
    {
        "id": "cloudplus-ops-004", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Across dozens of ephemeral instances that come and go, troubleshooting is hard because logs "
                "disappear with the instances. What practice solves this?",
        "options": [
            {"id": "A", "text": "Storing logs only on each local instance disk"},
            {"id": "B", "text": "Disabling logging to save space"},
            {"id": "C", "text": "Centralized log aggregation to a durable, external log store"},
            {"id": "D", "text": "Taking a VM snapshot once per month"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Shipping logs to a centralized, durable aggregation platform preserves them independently of the "
                       "short-lived instances, enabling search, correlation, and retention.",
            "distractors": {
                "A": "Local-only logs vanish when ephemeral instances are terminated — exactly the problem.",
                "B": "Disabling logging removes the evidence needed to troubleshoot and audit.",
                "D": "A monthly VM snapshot does not continuously capture per-request logs from transient instances.",
            },
            "exam_pattern": "Ephemeral instances -> ship logs to centralized durable aggregation.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Logging (centralized aggregation)"],
    },

    # ===== cloudp_maintenance_automation ====================================
    {
        "id": "cloudplus-ops-005", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "To apply operating-system security updates across hundreds of servers consistently and on a schedule, "
                "with minimal manual effort, an operations team should use:",
        "options": [
            {"id": "A", "text": "An automated patch-management system"},
            {"id": "B", "text": "Manual updates one server at a time"},
            {"id": "C", "text": "A content delivery network"},
            {"id": "D", "text": "A load-balancer health check"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automated patch management deploys, tracks, and reports updates across many systems on a schedule, "
                       "ensuring consistency and reducing the risk and labor of manual patching.",
            "distractors": {
                "B": "Manual, per-server patching does not scale to hundreds of systems and invites inconsistency and missed hosts.",
                "C": "A CDN distributes content; it does not patch operating systems.",
                "D": "A load-balancer health check routes traffic away from unhealthy nodes; it does not install patches.",
            },
            "exam_pattern": "Consistent, scheduled updates at scale = automated patch management.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance (patch automation)"],
    },
    {
        "id": "cloudplus-ops-006", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "A team schedules disruptive maintenance (reboots, upgrades) for a fixed, communicated period of low "
                "usage to limit user impact. What is this period called?",
        "options": [
            {"id": "A", "text": "A blast radius"},
            {"id": "B", "text": "A maintenance window"},
            {"id": "C", "text": "A recovery point"},
            {"id": "D", "text": "A sprint"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A maintenance window is a pre-approved, communicated time period for performing disruptive changes "
                       "when impact to users is lowest.",
            "distractors": {
                "A": "Blast radius describes how far a failure or change could spread, not a scheduled time period.",
                "C": "A recovery point relates to how much data loss is acceptable (RPO), not a maintenance schedule.",
                "D": "A sprint is an agile development iteration, not a change/maintenance window.",
            },
            "exam_pattern": "Pre-approved low-impact time slot for disruptive changes = maintenance window.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance windows"],
    },
    {
        "id": "cloudplus-ops-007", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "Rather than manually creating and configuring resources, a team uses a tool to coordinate multi-step "
                "workflows that provision, configure, and connect many resources automatically. This coordination of "
                "automated tasks is best called:",
        "options": [
            {"id": "A", "text": "Tokenization"},
            {"id": "B", "text": "Deduplication"},
            {"id": "C", "text": "Orchestration"},
            {"id": "D", "text": "Striping"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Orchestration coordinates multiple automated tasks into an ordered end-to-end workflow (provision, "
                       "configure, integrate), going beyond single-task automation.",
            "distractors": {
                "A": "Tokenization replaces sensitive data with tokens; it is a data-security technique, not workflow coordination.",
                "B": "Deduplication eliminates redundant data copies; it is unrelated to workflow coordination.",
                "D": "Striping spreads data across disks for performance; it is a storage concept.",
            },
            "exam_pattern": "Coordinate many automated tasks into one workflow = orchestration.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Automation and orchestration"],
    },
    {
        "id": "cloudplus-ops-008", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 3, "type": "multi",
        "stem": "An organization wants to reduce manual effort and human error in routine operations. Which TWO are "
                "appropriate automation use cases? (Choose two.)",
        "options": [
            {"id": "A", "text": "Automatically scaling instances based on demand metrics"},
            {"id": "B", "text": "Hand-editing production server configs during peak hours"},
            {"id": "C", "text": "Scheduled, automated patching and configuration enforcement"},
            {"id": "D", "text": "Emailing engineers to remind them to log in and patch manually"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Auto-scaling on metrics and scheduled automated patching/configuration enforcement are classic "
                       "automation use cases that cut manual toil and drift while improving consistency.",
            "distractors": {
                "B": "Hand-editing production configs during peak hours is manual, risky, and the opposite of automation.",
                "D": "Relying on email reminders for manual patching is still a manual, error-prone process.",
            },
            "exam_pattern": "Automate repetitive, error-prone ops (scaling, patching, config enforcement).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance automation"],
    },

    # ===== cloudp_backup_restore ============================================
    {
        "id": "cloudplus-ops-009", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "A backup job copies only the data that changed since the most recent backup of any type, resetting the "
                "archive marker each time. Backups are fast, but a restore may require the last full backup plus every "
                "one of these jobs in order. Which backup type is this?",
        "options": [
            {"id": "A", "text": "Full backup"},
            {"id": "B", "text": "Incremental backup"},
            {"id": "C", "text": "Differential backup"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Incremental backups copy only changes since the last backup (full or incremental), so they are small "
                       "and fast, but restoring requires the last full plus every subsequent incremental in sequence.",
            "distractors": {
                "A": "A full backup copies everything every time; it is large and slow, not 'changes since the last backup.'",
                "C": "A differential copies changes since the last full backup and does not reset the archive marker, so differentials grow and a restore needs only full + last differential.",
                "D": "A snapshot captures a point-in-time image of a volume/VM; it is not the archive-bit-based incremental scheme described.",
            },
            "exam_pattern": "Incremental = since last backup, small, restore needs full + ALL increments; differential = since last full, restore needs full + LAST diff.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup types (incremental)"],
    },
    {
        "id": "cloudplus-ops-010", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "After an outage, management asks: 'How much data, measured in time, can we afford to lose?' Which "
                "metric answers this question?",
        "options": [
            {"id": "A", "text": "RTO (Recovery Time Objective)"},
            {"id": "B", "text": "MTBF (Mean Time Between Failures)"},
            {"id": "C", "text": "SLA (Service-Level Agreement)"},
            {"id": "D", "text": "RPO (Recovery Point Objective)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "RPO defines the maximum acceptable amount of data loss expressed as time (e.g., 15 minutes), which "
                       "dictates how frequently backups/replication must occur.",
            "distractors": {
                "A": "RTO is the maximum acceptable time to restore service (downtime), not the amount of data loss.",
                "B": "MTBF estimates average time between failures of a component; it is a reliability metric, not data-loss tolerance.",
                "C": "An SLA is a service-commitment contract; it is not specifically the data-loss metric.",
            },
            "exam_pattern": "RPO = how much data (time) you can lose -> backup frequency; RTO = how long to recover.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup/DR (RPO vs RTO)"],
    },
    {
        "id": "cloudplus-ops-011", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "A company follows the 3-2-1 backup rule. Which statement correctly describes it?",
        "options": [
            {"id": "A", "text": "Keep 3 copies of data, on 2 different media types, with 1 copy off-site"},
            {"id": "B", "text": "Keep 3 backups per day, for 2 weeks, deleting after 1 month"},
            {"id": "C", "text": "Use 3 providers, 2 regions, and 1 encryption key"},
            {"id": "D", "text": "Run 3 full, 2 differential, and 1 incremental backup each cycle"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 3-2-1 rule: maintain at least three copies of data, store them on two different media/storage types, "
                       "and keep one copy off-site (ideally offline/immutable) to survive site-wide loss.",
            "distractors": {
                "B": "This invents a retention schedule unrelated to the 3-2-1 rule's copies/media/off-site structure.",
                "C": "Providers/regions/keys are not what 3-2-1 specifies; it is about copies, media diversity, and off-site.",
                "D": "Mixing backup-type counts is not the definition of 3-2-1.",
            },
            "exam_pattern": "3-2-1 = 3 copies, 2 media types, 1 off-site.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup strategy (3-2-1 rule)"],
    },
    {
        "id": "cloudplus-ops-012", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: A point-in-time copy of a volume or virtual machine's state, often used for quick "
                "rollback and captured near-instantly by recording block changes, is called a ____ (one word).",
        "correct": ["snapshot"],
        "explanation": {
            "correct": "A snapshot records the state of a volume/VM at a moment in time, enabling fast rollback. Many "
                       "implementations are copy-on-write, so snapshots are quick and space-efficient but depend on the source volume.",
            "distractors": {},
            "exam_pattern": "Point-in-time, fast-rollback copy of a volume/VM = snapshot (often copy-on-write).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup (snapshots)"],
    },

    # ===== cloudp_optimization ==============================================
    {
        "id": "cloudplus-ops-013", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A monthly review finds many instances running at 5-10% CPU with large amounts of idle memory. Which "
                "optimization directly addresses this waste?",
        "options": [
            {"id": "A", "text": "Scaling out by adding more identical instances"},
            {"id": "B", "text": "Rightsizing the instances to smaller types that match actual usage"},
            {"id": "C", "text": "Enabling a CDN for the database"},
            {"id": "D", "text": "Increasing the backup frequency"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Rightsizing matches instance size to measured utilization; moving chronically underused instances to "
                       "smaller types cuts cost without harming performance.",
            "distractors": {
                "A": "Adding more instances increases cost and capacity — the wrong move for resources already underutilized.",
                "C": "A CDN caches web content; it does not fix oversized, underused compute instances.",
                "D": "More frequent backups improve RPO but do nothing about wasted compute capacity.",
            },
            "exam_pattern": "Underused instances -> rightsize to smaller types to cut cost.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (rightsizing)"],
    },
    {
        "id": "cloudplus-ops-014", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A workload runs 24/7 and is highly predictable for the next three years. To lower cost versus "
                "on-demand pricing, which purchasing option is most appropriate?",
        "options": [
            {"id": "A", "text": "Spot/preemptible instances for the production database"},
            {"id": "B", "text": "On-demand only"},
            {"id": "C", "text": "Reserved capacity (committed-use) for a 1- or 3-year term"},
            {"id": "D", "text": "Scaling the instance up every night"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reserved/committed-use pricing offers a significant discount over on-demand in exchange for a 1- or "
                       "3-year commitment — ideal for steady, predictable, always-on workloads.",
            "distractors": {
                "A": "Spot/preemptible capacity can be reclaimed at short notice, which is risky for an always-on production database.",
                "B": "On-demand is the most expensive option for steady workloads; a commitment would save money here.",
                "D": "Scaling up nightly does not reduce cost for a constant workload and adds operational complexity.",
            },
            "exam_pattern": "Steady, predictable, long-term workload -> reserved/committed-use; bursty/fault-tolerant -> spot.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (reserved capacity)"],
    },
    {
        "id": "cloudplus-ops-015", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A finance team wants to attribute cloud spend to specific projects and departments for "
                "showback/chargeback. Which practice most directly enables this?",
        "options": [
            {"id": "A", "text": "Tagging resources with consistent cost-allocation labels"},
            {"id": "B", "text": "Disabling monitoring to reduce overhead"},
            {"id": "C", "text": "Deleting all snapshots weekly"},
            {"id": "D", "text": "Using a single shared account with no metadata"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Consistent resource tagging (cost-allocation tags) attributes spend to projects, teams, or "
                       "environments, enabling accurate showback/chargeback and targeted optimization.",
            "distractors": {
                "B": "Disabling monitoring removes the visibility needed to manage and optimize cost.",
                "C": "Deleting snapshots may trim some storage cost but does not attribute spend to departments.",
                "D": "A single untagged shared account makes cost attribution nearly impossible — the opposite of the goal.",
            },
            "exam_pattern": "Attribute spend to teams/projects = consistent cost-allocation tagging.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (tagging/chargeback)"],
    },
    {
        "id": "cloudplus-ops-016", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: Configuring the platform to automatically add instances during demand spikes and "
                "remove them when idle — so you pay only for needed capacity — is known as ____ (one word or hyphenated).",
        "correct": ["autoscaling", "auto-scaling", "auto scaling"],
        "explanation": {
            "correct": "Auto-scaling adds and removes capacity automatically against demand metrics or schedules, improving "
                       "both performance (enough capacity under load) and cost (no idle over-provisioning).",
            "distractors": {},
            "exam_pattern": "Automatically add/remove capacity to match demand = auto-scaling (cost + performance).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (auto-scaling for cost)"],
    },
]
