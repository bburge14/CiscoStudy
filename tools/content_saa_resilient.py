"""AWS Certified Solutions Architect - Associate (SAA-C03) pool.

Domain 2: Design Resilient Architectures (saa_resilient). Original, scenario-based
practice items for the four resilience subtopics tracked in the engine:

  * saa_decoupling         - loose coupling with Amazon SQS (incl. FIFO), SNS
                             fan-out, EventBridge event routing, and Step Functions
                             orchestration.
  * saa_ha_fault_tolerance - RDS Multi-AZ vs read replicas, EC2 Auto Scaling, ELB
                             types (ALB/NLB/GWLB), and Route 53 failover routing
                             with health checks.
  * saa_backup_dr          - DR strategies (backup & restore, pilot light, warm
                             standby, multi-site active/active), RTO/RPO, S3
                             Cross-Region Replication, and AWS Backup.
  * saa_storage_resilience - S3 eleven-nines durability, EBS snapshots, Amazon EFS,
                             and single-AZ vs multi-AZ storage trade-offs.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer is not positionally biased,
every wrong option carries a distractor note, and each item maps to the SAA-C03
exam-guide task statement. Items test durable "which design BEST meets these
requirements" judgement - not prices, region trivia, or real/memorized exam content.
"""

QUESTIONS = [
    # ===== saa_decoupling ===================================================
    {
        "id": "saa-res-001", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_decoupling",
        "difficulty": 1, "type": "mcq",
        "stem": "A web tier receives bursts of orders that a slower processing tier cannot always keep up with, "
                "causing dropped requests. Which service BEST decouples the tiers and buffers requests so none are "
                "lost during spikes?",
        "options": [
            {"id": "A", "text": "An Amazon SQS queue between the web tier and the processing tier"},
            {"id": "B", "text": "A larger EC2 instance for the processing tier"},
            {"id": "C", "text": "Amazon Route 53 latency-based routing"},
            {"id": "D", "text": "An Application Load Balancer between the two tiers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SQS queue absorbs bursts by durably buffering messages until the consumer can process "
                       "them, decoupling producer and consumer so spikes do not drop work.",
            "distractors": {
                "B": "A bigger consumer still risks drops during spikes and does not decouple the tiers.",
                "C": "Route 53 provides DNS routing, not request buffering.",
                "D": "An ALB distributes synchronous requests but does not persist messages when consumers fall behind.",
            },
            "exam_pattern": "Buffer bursts + decouple producer/consumer = Amazon SQS (asynchronous queue).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design scalable and loosely coupled architectures (SQS)"],
    },
    {
        "id": "saa-res-002", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_decoupling",
        "difficulty": 2, "type": "mcq",
        "stem": "When a new image is uploaded, a company must notify several independent systems at once (a "
                "thumbnail generator, an indexer, and an audit logger), each processing the event on its own. "
                "Which design BEST implements this fan-out?",
        "options": [
            {"id": "A", "text": "Write the event to a single SQS queue that all systems share and compete for"},
            {"id": "B", "text": "Publish the event to an Amazon SNS topic with multiple subscribers (e.g., SQS queues or Lambda), one per system"},
            {"id": "C", "text": "Store the event in S3 and have each system poll the bucket on a timer"},
            {"id": "D", "text": "Send the event to one system that then calls the others synchronously"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An SNS topic delivers each published message to all subscribers, so every system receives its "
                       "own copy - the classic fan-out pattern (often SNS to multiple SQS queues).",
            "distractors": {
                "A": "With one shared queue, consumers compete and each message is processed once, not by all three systems.",
                "C": "Polling S3 on a timer is inefficient and is not event-driven fan-out.",
                "D": "Chaining synchronous calls couples the systems and fails if one is down.",
            },
            "exam_pattern": "One event -> many independent consumers = SNS fan-out (commonly SNS -> multiple SQS queues).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design scalable and loosely coupled architectures (SNS fan-out)"],
    },
    {
        "id": "saa-res-003", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_decoupling",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants to route events from many AWS services and third-party SaaS applications to "
                "different targets based on content-matching rules, using a serverless event bus. Which service is "
                "designed for this?",
        "options": [
            {"id": "A", "text": "Amazon SQS"},
            {"id": "B", "text": "Amazon Kinesis Data Streams"},
            {"id": "C", "text": "Amazon EventBridge"},
            {"id": "D", "text": "AWS Direct Connect"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "EventBridge is a serverless event bus with content-based routing rules and native "
                       "integrations for AWS services and SaaS partner event sources.",
            "distractors": {
                "A": "SQS is a point-to-point queue without content-based routing rules or SaaS event buses.",
                "B": "Kinesis handles high-volume streaming/ordered records, not rule-based routing across SaaS partners.",
                "D": "Direct Connect is a dedicated network link, unrelated to event routing.",
            },
            "exam_pattern": "Rule-based event routing across AWS + SaaS sources = EventBridge event bus.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design scalable and loosely coupled architectures (EventBridge)"],
    },
    {
        "id": "saa-res-004", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_decoupling",
        "difficulty": 3, "type": "mcq",
        "stem": "An order workflow has several steps that must run in sequence with built-in error handling, "
                "retries, and visibility into which step failed. Which service BEST orchestrates this as a managed "
                "state machine?",
        "options": [
            {"id": "A", "text": "AWS Step Functions"},
            {"id": "B", "text": "A single large Lambda function that contains all of the logic"},
            {"id": "C", "text": "Amazon SNS"},
            {"id": "D", "text": "An Amazon SQS FIFO queue"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Step Functions coordinates multi-step workflows as a state machine with built-in retries, "
                       "error handling, branching, and visibility into each step's state.",
            "distractors": {
                "B": "Packing all steps into one function loses per-step retry/visibility and risks timeouts.",
                "C": "SNS is pub/sub notification, not workflow orchestration.",
                "D": "A FIFO queue orders messages but does not orchestrate multi-step workflows with branching/retries.",
            },
            "exam_pattern": "Coordinate a multi-step workflow with retries/state/visibility = Step Functions.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design scalable and loosely coupled architectures (Step Functions)"],
    },
    {
        "id": "saa-res-005", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_decoupling",
        "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: To guarantee that messages are processed in the exact order they are sent and "
                "that duplicates are not introduced, you should use an Amazon SQS ____ queue (four-letter type) "
                "instead of a standard queue.",
        "correct": ["fifo", "fifo queue", "first-in-first-out"],
        "explanation": {
            "correct": "SQS FIFO (first-in-first-out) queues preserve strict ordering and provide exactly-once "
                       "processing, unlike standard queues (best-effort ordering, at-least-once delivery).",
            "distractors": {},
            "exam_pattern": "Strict ordering + no duplicates = SQS FIFO; maximum throughput, best-effort order = standard.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design scalable and loosely coupled architectures (SQS FIFO)"],
    },

    # ===== saa_ha_fault_tolerance ===========================================
    {
        "id": "saa-res-006", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_ha_fault_tolerance",
        "difficulty": 1, "type": "mcq",
        "stem": "A company needs its RDS database to automatically fail over to a standby in another Availability "
                "Zone if the primary fails, with no manual intervention. Which feature provides this?",
        "options": [
            {"id": "A", "text": "An RDS read replica in the same Availability Zone"},
            {"id": "B", "text": "A larger DB instance class"},
            {"id": "C", "text": "Manual daily snapshots"},
            {"id": "D", "text": "An RDS Multi-AZ deployment"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "RDS Multi-AZ maintains a synchronous standby in another AZ and fails over to it automatically "
                       "when the primary becomes unavailable.",
            "distractors": {
                "A": "A read replica is asynchronous and scales reads; by itself it is not an automatic failover target, and same-AZ gives no AZ redundancy.",
                "B": "A bigger instance improves capacity, not AZ-level failover.",
                "C": "Snapshots are backups; they do not provide automatic failover.",
            },
            "exam_pattern": "Automatic cross-AZ DB failover (HA) = RDS Multi-AZ (synchronous standby).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (Multi-AZ)"],
    },
    {
        "id": "saa-res-007", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_ha_fault_tolerance",
        "difficulty": 2, "type": "mcq",
        "stem": "A reporting workload is overwhelming the primary RDS database with read queries, hurting write "
                "performance. Which solution BEST offloads the read traffic?",
        "options": [
            {"id": "A", "text": "Add one or more RDS read replicas and point reporting queries at them"},
            {"id": "B", "text": "Convert the database to a Multi-AZ deployment"},
            {"id": "C", "text": "Take more frequent snapshots"},
            {"id": "D", "text": "Attach a larger EBS volume"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Read replicas provide additional read-only endpoints, so read-heavy reporting can be directed "
                       "to them, relieving the primary.",
            "distractors": {
                "B": "Multi-AZ provides HA/failover; its standby does not serve reads, so it does not offload read traffic.",
                "C": "Snapshots are backups, not a read-serving mechanism.",
                "D": "More storage does not reduce read-query contention.",
            },
            "exam_pattern": "Scale/offload reads = read replicas; HA/failover = Multi-AZ. Know the distinction.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (read replicas)"],
    },
    {
        "id": "saa-res-008", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_ha_fault_tolerance",
        "difficulty": 2, "type": "mcq",
        "stem": "An architect wants a stateless web tier that automatically replaces failed instances and "
                "distributes traffic across multiple Availability Zones. Which combination BEST achieves this?",
        "options": [
            {"id": "A", "text": "A single large EC2 instance with an Elastic IP"},
            {"id": "B", "text": "An EC2 Auto Scaling group spanning multiple AZs behind an Application Load Balancer"},
            {"id": "C", "text": "Several EC2 instances in one AZ with no load balancer"},
            {"id": "D", "text": "One EC2 instance in each AZ, started and stopped manually"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An Auto Scaling group across multiple AZs replaces unhealthy instances automatically, and an "
                       "ALB spreads traffic and routes only to healthy targets.",
            "distractors": {
                "A": "A single instance is a single point of failure regardless of size.",
                "C": "Concentrating in one AZ fails if that AZ has issues, and without an LB there is no traffic distribution.",
                "D": "Manual management provides no automatic replacement or scaling.",
            },
            "exam_pattern": "Self-healing, multi-AZ web tier = Auto Scaling group across AZs + ELB health checks.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (Auto Scaling + ELB)"],
    },
    {
        "id": "saa-res-009", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_ha_fault_tolerance",
        "difficulty": 2, "type": "mcq",
        "stem": "A workload needs a load balancer that handles millions of requests per second at ultra-low latency "
                "for a TCP-based (non-HTTP) protocol and must expose a static IP address. Which load balancer type "
                "BEST fits?",
        "options": [
            {"id": "A", "text": "Application Load Balancer (ALB)"},
            {"id": "B", "text": "Gateway Load Balancer (GWLB)"},
            {"id": "C", "text": "Network Load Balancer (NLB)"},
            {"id": "D", "text": "Classic Load Balancer for HTTP path-based routing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The NLB operates at layer 4 (TCP/UDP), handles very high throughput at ultra-low latency, and "
                       "can expose a static IP per AZ.",
            "distractors": {
                "A": "The ALB is a layer-7 HTTP/HTTPS balancer and does not offer the same raw TCP throughput/static-IP profile.",
                "B": "GWLB is for inserting third-party virtual appliances (firewalls/IDS) at layer 3, not general TCP load balancing.",
                "D": "The Classic Load Balancer is legacy, and path-based routing is a layer-7/ALB feature, not what this TCP scenario needs.",
            },
            "exam_pattern": "Layer-4 TCP/UDP, static IP, extreme performance = NLB; HTTP path/host routing = ALB; appliance insertion = GWLB.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (ELB types)"],
    },
    {
        "id": "saa-res-010", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_ha_fault_tolerance",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants users automatically directed to a standby site in another Region if health checks "
                "show the primary site is down. Which Route 53 routing policy implements this active-passive behavior?",
        "options": [
            {"id": "A", "text": "Weighted routing policy with equal weights"},
            {"id": "B", "text": "Simple routing policy"},
            {"id": "C", "text": "Multivalue answer routing without health checks"},
            {"id": "D", "text": "Failover routing policy with health checks"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Failover routing sends traffic to the primary while it is healthy and automatically shifts to "
                       "the secondary when health checks mark the primary unhealthy - active-passive DR.",
            "distractors": {
                "A": "Weighted routing splits traffic by proportion; it is not automatic primary/standby failover.",
                "B": "Simple routing returns one record set with no health-based failover.",
                "C": "Multivalue returns multiple healthy records but is not designed for active-passive failover.",
            },
            "exam_pattern": "Active-passive automatic failover by health = Route 53 failover routing policy.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (Route 53 failover)"],
    },

    # ===== saa_backup_dr ====================================================
    {
        "id": "saa-res-011", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_backup_dr",
        "difficulty": 2, "type": "mcq",
        "stem": "A mission-critical application must keep serving users with near-zero downtime and near-zero data "
                "loss even if an entire Region fails, and cost is a secondary concern. Which disaster recovery "
                "strategy BEST meets this?",
        "options": [
            {"id": "A", "text": "Multi-site active/active across Regions"},
            {"id": "B", "text": "Backup and restore"},
            {"id": "C", "text": "Pilot light"},
            {"id": "D", "text": "A single-AZ deployment with daily backups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multi-site active/active runs full production in more than one Region simultaneously, giving "
                       "the lowest RTO/RPO (near-zero) at the highest cost.",
            "distractors": {
                "B": "Backup and restore has the longest RTO/RPO because you rebuild and restore after failure.",
                "C": "Pilot light keeps only a minimal core running and must scale up on failover, so RTO is higher than active/active.",
                "D": "A single-AZ deployment is not a cross-Region DR strategy at all.",
            },
            "exam_pattern": "Lowest RTO/RPO = multi-site active/active; cheapest/slowest = backup & restore (pilot light < warm standby < active/active in cost & speed).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (DR strategies)"],
    },
    {
        "id": "saa-res-012", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_backup_dr",
        "difficulty": 3, "type": "mcq",
        "stem": "A company wants a low-cost DR approach where only a minimal core (such as a replicated database) "
                "runs in the recovery Region, and the rest of the environment is provisioned and scaled up only "
                "when a disaster is declared. Which strategy is this?",
        "options": [
            {"id": "A", "text": "Multi-site active/active"},
            {"id": "B", "text": "Pilot light"},
            {"id": "C", "text": "Warm standby"},
            {"id": "D", "text": "Backup and restore"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Pilot light keeps a minimal core (e.g., a replicated database) always running in the recovery "
                       "Region and provisions/scales the rest only when failover is triggered.",
            "distractors": {
                "A": "Active/active runs full production in both Regions at once - far more than a minimal core.",
                "C": "Warm standby keeps a scaled-down but fully functional copy always running, more than a pilot light's core.",
                "D": "Backup and restore keeps nothing running in the recovery Region; it restores from backups.",
            },
            "exam_pattern": "Minimal core always on, scale up on failover = pilot light; scaled-down full stack always on = warm standby.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (pilot light vs warm standby)"],
    },
    {
        "id": "saa-res-013", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_backup_dr",
        "difficulty": 1, "type": "mcq",
        "stem": "A business states it can tolerate losing at most 15 minutes of data in a disaster. Which metric "
                "does the \"15 minutes\" describe?",
        "options": [
            {"id": "A", "text": "Recovery Time Objective (RTO)"},
            {"id": "B", "text": "Mean Time Between Failures (MTBF)"},
            {"id": "C", "text": "Recovery Point Objective (RPO)"},
            {"id": "D", "text": "A Service Level Agreement (SLA) credit"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RPO is the maximum acceptable amount of data loss measured in time - here, 15 minutes - and "
                       "it drives how often you replicate or back up.",
            "distractors": {
                "A": "RTO is how long you can be down (time to recover), not how much data you can lose.",
                "B": "MTBF measures reliability (time between failures), not tolerable data loss.",
                "D": "An SLA credit is a billing remedy, not a data-loss target.",
            },
            "exam_pattern": "Tolerable DATA loss = RPO; tolerable DOWNTIME = RTO.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (RTO/RPO)"],
    },
    {
        "id": "saa-res-014", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_backup_dr",
        "difficulty": 2, "type": "mcq",
        "stem": "A company must keep a continuously updated copy of its S3 objects in a second AWS Region for "
                "disaster recovery and compliance. Which feature BEST meets this requirement?",
        "options": [
            {"id": "A", "text": "S3 Versioning within the same bucket"},
            {"id": "B", "text": "An EBS snapshot copied monthly"},
            {"id": "C", "text": "S3 Transfer Acceleration"},
            {"id": "D", "text": "S3 Cross-Region Replication (CRR)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Cross-Region Replication automatically and continuously copies new/updated objects to a bucket "
                       "in another Region (versioning must be enabled).",
            "distractors": {
                "A": "Versioning keeps object versions in the same bucket/Region; it does not place a copy in another Region.",
                "B": "EBS snapshots apply to block volumes, not S3 objects.",
                "C": "Transfer Acceleration speeds uploads via edge locations; it does not replicate objects across Regions.",
            },
            "exam_pattern": "Continuous cross-Region copy of S3 data = Cross-Region Replication (requires versioning).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (S3 CRR)"],
    },
    {
        "id": "saa-res-015", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_backup_dr",
        "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The AWS service that provides centralized, policy-based backup management across "
                "services such as EBS, RDS, DynamoDB, and EFS is AWS ______.",
        "correct": ["backup", "aws backup"],
        "explanation": {
            "correct": "AWS Backup centralizes and automates backups across many AWS services using backup plans and "
                       "policies, with centralized monitoring and retention.",
            "distractors": {},
            "exam_pattern": "Centralized, policy-driven backups across many services = AWS Backup.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (AWS Backup)"],
    },

    # ===== saa_storage_resilience ===========================================
    {
        "id": "saa-res-016", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_storage_resilience",
        "difficulty": 1, "type": "mcq",
        "stem": "An architect needs object storage that automatically stores data redundantly across multiple "
                "Availability Zones and is designed for 99.999999999% (eleven nines) durability. Which option "
                "provides this out of the box?",
        "options": [
            {"id": "A", "text": "Amazon S3 Standard"},
            {"id": "B", "text": "A single EBS volume"},
            {"id": "C", "text": "EC2 instance store"},
            {"id": "D", "text": "An on-premises NFS share"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Standard stores objects redundantly across multiple AZs and is designed for eleven nines "
                       "of durability with no extra configuration.",
            "distractors": {
                "B": "An EBS volume is replicated only within a single AZ and is tied to one instance; it is not eleven-nines multi-AZ object storage.",
                "C": "Instance store is ephemeral and lost when the instance stops or terminates.",
                "D": "An on-premises share is not AWS-managed and carries no such durability design.",
            },
            "exam_pattern": "Eleven-nines durable, multi-AZ object storage = Amazon S3.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (S3 durability)"],
    },
    {
        "id": "saa-res-017", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_storage_resilience",
        "difficulty": 2, "type": "mcq",
        "stem": "A team must back up an EBS volume so it can be restored later, and also create an identical volume "
                "in a different Availability Zone. Which AWS feature supports both?",
        "options": [
            {"id": "A", "text": "Enabling S3 Versioning on the volume"},
            {"id": "B", "text": "EBS snapshots (stored durably in S3)"},
            {"id": "C", "text": "Instance store volumes"},
            {"id": "D", "text": "Elastic IP addresses"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "EBS snapshots are incremental, Region-scoped point-in-time backups stored in S3; a new volume "
                       "can be created from a snapshot in any AZ in the Region.",
            "distractors": {
                "A": "Versioning is an S3 feature and does not apply to EBS volumes.",
                "C": "Instance store is ephemeral local disk, not a backup mechanism.",
                "D": "Elastic IPs are network addresses, unrelated to volume backup.",
            },
            "exam_pattern": "Back up / clone an EBS volume (and move it across AZs) = EBS snapshots.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (EBS snapshots)"],
    },
    {
        "id": "saa-res-018", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_storage_resilience",
        "difficulty": 2, "type": "mcq",
        "stem": "Several EC2 instances across multiple Availability Zones must concurrently read and write to the "
                "same Linux file system with elastic capacity. Which storage service BEST fits?",
        "options": [
            {"id": "A", "text": "A single EBS volume attached to one instance"},
            {"id": "B", "text": "Amazon S3 Glacier Deep Archive"},
            {"id": "C", "text": "Amazon EFS"},
            {"id": "D", "text": "EC2 instance store"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Amazon EFS is a managed, elastic NFS file system that many instances across AZs can mount and "
                       "access concurrently.",
            "distractors": {
                "A": "A standard EBS volume attaches to one instance in one AZ and is not a shared multi-AZ file system.",
                "B": "Glacier Deep Archive is cold archival storage, not a live shared file system.",
                "D": "Instance store is local ephemeral disk, not shared across instances.",
            },
            "exam_pattern": "Shared POSIX file system across many instances/AZs = Amazon EFS; single-instance block = EBS.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (EFS)"],
    },
    {
        "id": "saa-res-019", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_storage_resilience",
        "difficulty": 3, "type": "mcq",
        "stem": "A company stores easily reproducible, infrequently accessed data and wants to minimize storage "
                "cost, accepting that the data lives in only one Availability Zone. Which S3 storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Standard"},
            {"id": "B", "text": "S3 Standard-Infrequent Access"},
            {"id": "C", "text": "S3 Glacier Deep Archive"},
            {"id": "D", "text": "S3 One Zone-Infrequent Access"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "S3 One Zone-IA stores data in a single AZ at lower cost than multi-AZ IA, which is acceptable "
                       "when the data is infrequently accessed and easily reproducible if that AZ is lost.",
            "distractors": {
                "A": "S3 Standard stores across multiple AZs at higher cost than needed for reproducible data.",
                "B": "Standard-IA is also multi-AZ and costs more than One Zone-IA for this use case.",
                "C": "Deep Archive is for long-term archival with retrieval delays, not readily accessed infrequent data.",
            },
            "exam_pattern": "Infrequent access + reproducible + lowest cost, single-AZ acceptable = S3 One Zone-IA.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (S3 storage classes)"],
    },
    {
        "id": "saa-res-020", "exam": "saa",
        "domain": "saa_resilient", "subtopic": "saa_storage_resilience",
        "difficulty": 3, "type": "multi",
        "stem": "An architect is removing single points of failure from a three-tier web application. Which TWO "
                "actions improve resilience? (Choose two.)",
        "options": [
            {"id": "A", "text": "Deploy the web/app tier across multiple Availability Zones behind a load balancer"},
            {"id": "B", "text": "Enable Multi-AZ for the relational database"},
            {"id": "C", "text": "Run the entire stack on one large EC2 instance to simplify management"},
            {"id": "D", "text": "Store session state only in the memory of individual web servers"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Spreading the compute tier across AZs behind a load balancer and enabling Multi-AZ on the "
                       "database both remove single points of failure.",
            "distractors": {
                "C": "A single instance is a single point of failure regardless of size.",
                "D": "Keeping session state in local memory ties users to one server and loses state on failure; externalize it (e.g., DynamoDB/ElastiCache).",
            },
            "exam_pattern": "Remove SPOFs = multi-AZ compute + load balancing + Multi-AZ data tier + externalized session state.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 2 - Design highly available / fault-tolerant architectures (removing SPOFs)"],
    },
]
