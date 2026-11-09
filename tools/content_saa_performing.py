"""AWS Certified Solutions Architect - Associate (SAA-C03) pool.

Domain 3: Design High-Performing Architectures (saa_performing). Original,
scenario-based practice items for the four performance subtopics tracked in the
engine:

  * saa_compute_perf  - EC2 Auto Scaling policies, AWS Lambda, Fargate/ECS
                        serverless containers, and EC2 placement groups.
  * saa_storage_perf  - EBS volume types (gp3/io2/st1/sc1), EC2 instance store,
                        and S3 Transfer Acceleration for fast long-distance uploads.
  * saa_database_perf - DynamoDB Accelerator (DAX), ElastiCache (Redis vs
                        Memcached), Amazon Aurora, and read replicas for read scaling.
  * saa_network_perf  - Amazon CloudFront, AWS Global Accelerator, enhanced
                        networking (ENA), and AWS Direct Connect.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer is not positionally biased,
every wrong option carries a distractor note, and each item maps to the SAA-C03
exam-guide task statement. Items test durable "which design BEST meets these
requirements" judgement - not prices, region trivia, or real/memorized exam content.
"""

QUESTIONS = [
    # ===== saa_compute_perf =================================================
    {
        "id": "saa-perf-001", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_compute_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A web application's CPU utilization varies throughout the day, and the team wants EC2 capacity to "
                "adjust automatically to keep average CPU near 50%. Which EC2 Auto Scaling approach BEST meets this?",
        "options": [
            {"id": "A", "text": "A target tracking scaling policy on average CPU utilization"},
            {"id": "B", "text": "Manually launching instances each morning"},
            {"id": "C", "text": "A fixed desired capacity with no scaling"},
            {"id": "D", "text": "Resizing the instance type by hand each day"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Target tracking adjusts capacity automatically to hold a chosen metric (e.g., average CPU) at "
                       "a target value, adding or removing instances as load changes.",
            "distractors": {
                "B": "Manual launches cannot react to real-time demand changes.",
                "C": "A fixed capacity cannot adapt to variable load.",
                "D": "Resizing the instance type requires stop/replace and does not continuously track a metric.",
            },
            "exam_pattern": "Hold a metric at a target automatically = target tracking scaling policy (dynamic scaling).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Design high-performing and elastic compute solutions (Auto Scaling)"],
    },
    {
        "id": "saa-perf-002", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_compute_perf",
        "difficulty": 1, "type": "mcq",
        "stem": "A company wants to run short, event-driven image-processing code that scales automatically from "
                "zero to thousands of concurrent executions with no servers to manage, paying only for compute used. "
                "Which service fits BEST?",
        "options": [
            {"id": "A", "text": "A fleet of always-on EC2 instances"},
            {"id": "B", "text": "AWS Lambda"},
            {"id": "C", "text": "Amazon RDS"},
            {"id": "D", "text": "AWS Direct Connect"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Lambda runs event-driven code, scales concurrency automatically, requires no server "
                       "management, and bills only for execution time.",
            "distractors": {
                "A": "Always-on EC2 means managing servers and paying while idle.",
                "C": "RDS is a managed database, not a runtime for arbitrary application code.",
                "D": "Direct Connect is a networking service, not compute.",
            },
            "exam_pattern": "Event-driven, auto-scaling, no servers, pay-per-use = AWS Lambda.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Design high-performing and elastic compute solutions (Lambda)"],
    },
    {
        "id": "saa-perf-003", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_compute_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A team runs containerized microservices on Amazon ECS and wants to stop managing and patching the "
                "underlying EC2 host instances while still running containers. Which launch option BEST meets this?",
        "options": [
            {"id": "A", "text": "The ECS EC2 launch type with self-managed instances"},
            {"id": "B", "text": "Running containers directly on Lambda layers"},
            {"id": "C", "text": "AWS Fargate (serverless containers)"},
            {"id": "D", "text": "Migrating the containers to Amazon S3"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Fargate runs containers without any EC2 hosts to provision, patch, or scale - AWS manages the "
                       "underlying compute.",
            "distractors": {
                "A": "The EC2 launch type still requires you to manage and patch the host instances.",
                "B": "Lambda layers package dependencies; they are not a container host.",
                "D": "S3 is object storage and cannot run containers.",
            },
            "exam_pattern": "Run containers without managing servers = AWS Fargate (serverless for ECS/EKS).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Design high-performing and elastic compute solutions (Fargate)"],
    },
    {
        "id": "saa-perf-004", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_compute_perf",
        "difficulty": 3, "type": "mcq",
        "stem": "A tightly coupled high-performance computing job needs the lowest possible network latency and "
                "highest throughput between EC2 instances. Which placement strategy BEST supports this?",
        "options": [
            {"id": "A", "text": "A spread placement group"},
            {"id": "B", "text": "Distributing instances across multiple Regions"},
            {"id": "C", "text": "A partition placement group across many racks"},
            {"id": "D", "text": "A cluster placement group"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A cluster placement group packs instances close together in one AZ for the lowest latency and "
                       "highest network throughput between nodes - ideal for HPC.",
            "distractors": {
                "A": "A spread placement group separates instances onto distinct hardware to reduce correlated failure, which increases latency.",
                "B": "Spreading across Regions maximizes latency, the opposite of the goal.",
                "C": "Partition groups isolate racks for large distributed systems (e.g., Hadoop), not minimal inter-node latency.",
            },
            "exam_pattern": "Lowest latency between instances (HPC) = cluster placement group; max fault isolation = spread; big distributed = partition.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Design high-performing and elastic compute solutions (placement groups)"],
    },
    {
        "id": "saa-perf-005", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_compute_perf",
        "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Adding more EC2 instances to handle increased load, rather than increasing the "
                "size of a single instance, is called scaling ___ (one word, the opposite of \"up\").",
        "correct": ["out", "horizontally", "horizontal"],
        "explanation": {
            "correct": "Scaling out (horizontal scaling) adds more instances to share load, which also improves "
                       "fault tolerance; scaling up (vertical) uses a bigger instance.",
            "distractors": {},
            "exam_pattern": "Add instances = scale out (horizontal); bigger instance = scale up (vertical).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Design high-performing and elastic compute solutions (horizontal scaling)"],
    },

    # ===== saa_storage_perf =================================================
    {
        "id": "saa-perf-006", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_storage_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A latency-sensitive production database on EC2 needs very high, consistent IOPS with the highest "
                "durability for its block storage. Which EBS volume type BEST fits?",
        "options": [
            {"id": "A", "text": "Provisioned IOPS SSD (io2 / io2 Block Express)"},
            {"id": "B", "text": "Throughput Optimized HDD (st1)"},
            {"id": "C", "text": "Cold HDD (sc1)"},
            {"id": "D", "text": "A general-purpose SSD left at its default baseline"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "io2 / io2 Block Express is designed for high, consistent provisioned IOPS with low latency and "
                       "the highest EBS durability - a fit for critical, latency-sensitive databases.",
            "distractors": {
                "B": "st1 is HDD optimized for large sequential throughput, not high random IOPS or low latency.",
                "C": "sc1 is the lowest-cost cold HDD for infrequent access, unsuitable for a busy database.",
                "D": "gp3 is SSD, but the scenario calls for the highest, most consistent provisioned IOPS and durability, which io2 targets.",
            },
            "exam_pattern": "Highest/consistent IOPS + critical DB = io2/io2 Block Express; general purpose = gp3; big sequential = st1; cold/cheap = sc1.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable storage solutions (EBS io2)"],
    },
    {
        "id": "saa-perf-007", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_storage_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A big-data workload streams large, sequential reads and writes (log processing and data "
                "warehousing) and wants the most cost-effective volume optimized for throughput rather than IOPS. "
                "Which EBS volume type fits BEST?",
        "options": [
            {"id": "A", "text": "Provisioned IOPS SSD (io2)"},
            {"id": "B", "text": "Throughput Optimized HDD (st1)"},
            {"id": "C", "text": "General Purpose SSD (gp3)"},
            {"id": "D", "text": "Instance store for permanent data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "st1 (Throughput Optimized HDD) is designed for large, sequential throughput workloads such as "
                       "big data and log processing at a lower cost than SSD.",
            "distractors": {
                "A": "io2 targets high random IOPS and is far costlier than needed for sequential throughput.",
                "C": "gp3 is general-purpose SSD; st1 is more cost-effective for large sequential throughput.",
                "D": "Instance store is ephemeral and unsuitable for data that must persist.",
            },
            "exam_pattern": "Large sequential throughput, cost-sensitive = st1 (HDD); random IOPS/low latency = SSD (gp3/io2).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable storage solutions (EBS st1)"],
    },
    {
        "id": "saa-perf-008", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_storage_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "An application needs the highest possible I/O performance for temporary scratch data (a local "
                "cache/buffer) that can be lost when the instance stops. Which storage option offers the best "
                "performance for this ephemeral need?",
        "options": [
            {"id": "A", "text": "S3 Standard"},
            {"id": "B", "text": "A Cold HDD (sc1) EBS volume"},
            {"id": "C", "text": "EC2 instance store (local NVMe)"},
            {"id": "D", "text": "Amazon S3 Glacier Flexible Retrieval"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Instance store is physically attached local NVMe/SSD offering the highest I/O performance for "
                       "temporary data, accepting that it is lost when the instance stops or terminates.",
            "distractors": {
                "A": "S3 is durable object storage accessed over the network, not the lowest-latency local scratch disk.",
                "B": "sc1 is a low-cost cold HDD, the opposite of high performance.",
                "D": "Glacier is archival storage with retrieval delays.",
            },
            "exam_pattern": "Highest-performance ephemeral/scratch that can be lost = instance store (local NVMe); persistent block = EBS.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable storage solutions (instance store)"],
    },
    {
        "id": "saa-perf-009", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_storage_perf",
        "difficulty": 3, "type": "mcq",
        "stem": "A team on gp2 volumes finds that to get more IOPS they must over-provision volume size. They want "
                "to raise IOPS and throughput independently of capacity. Which EBS volume type enables this?",
        "options": [
            {"id": "A", "text": "General Purpose SSD gp2"},
            {"id": "B", "text": "Cold HDD sc1"},
            {"id": "C", "text": "Throughput Optimized HDD st1"},
            {"id": "D", "text": "General Purpose SSD gp3"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "gp3 provides a fixed baseline of performance and lets you provision IOPS and throughput "
                       "independently of volume size, avoiding gp2's size-to-IOPS coupling.",
            "distractors": {
                "A": "With gp2, IOPS scale with volume size, which is exactly the limitation described.",
                "B": "sc1 is a cold HDD for infrequent access, not independently provisioned SSD IOPS.",
                "C": "st1 is a throughput HDD, not an SSD with independently provisioned IOPS.",
            },
            "exam_pattern": "gp3 decouples IOPS/throughput from size; gp2 ties IOPS to size.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable storage solutions (EBS gp3)"],
    },
    {
        "id": "saa-perf-010", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_storage_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "Users around the world upload large files to an S3 bucket in a single Region and experience slow "
                "transfers over long distances. Which feature speeds these uploads by routing through the nearest "
                "edge location?",
        "options": [
            {"id": "A", "text": "S3 Transfer Acceleration"},
            {"id": "B", "text": "S3 Versioning"},
            {"id": "C", "text": "S3 Object Lock"},
            {"id": "D", "text": "Reducing the bucket's durability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Transfer Acceleration routes uploads through the nearest CloudFront edge location and over "
                       "the AWS backbone, speeding long-distance transfers to the bucket.",
            "distractors": {
                "B": "Versioning retains object versions; it does not accelerate transfers.",
                "C": "Object Lock enforces WORM retention, unrelated to speed.",
                "D": "Durability is not adjustable and would not affect upload speed.",
            },
            "exam_pattern": "Faster long-distance uploads to S3 via the edge network = S3 Transfer Acceleration.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable storage solutions (Transfer Acceleration)"],
    },

    # ===== saa_database_perf ================================================
    {
        "id": "saa-perf-011", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_database_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A read-heavy application on Amazon DynamoDB needs microsecond read latency for repeated reads "
                "without changing its DynamoDB API calls. Which solution BEST provides this?",
        "options": [
            {"id": "A", "text": "An Amazon RDS read replica"},
            {"id": "B", "text": "Amazon DynamoDB Accelerator (DAX)"},
            {"id": "C", "text": "Amazon Redshift"},
            {"id": "D", "text": "Increasing the DynamoDB item size"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DAX is an in-memory cache purpose-built for DynamoDB that delivers microsecond read latency "
                       "and is API-compatible, so the application code needs no changes.",
            "distractors": {
                "A": "Read replicas apply to RDS/Aurora relational databases, not DynamoDB.",
                "C": "Redshift is a data warehouse for analytics, not a low-latency cache for DynamoDB.",
                "D": "Larger items do not reduce read latency and increase cost.",
            },
            "exam_pattern": "Microsecond caching for read-heavy DynamoDB = DAX (in-memory, DynamoDB-API compatible).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing database solutions (DynamoDB DAX)"],
    },
    {
        "id": "saa-perf-012", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_database_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A relational database is strained by repeated identical read queries for popular items. The team "
                "wants to cache results in memory to reduce database load and latency. Which service BEST fits?",
        "options": [
            {"id": "A", "text": "Amazon Athena"},
            {"id": "B", "text": "AWS Glue"},
            {"id": "C", "text": "Amazon ElastiCache"},
            {"id": "D", "text": "Amazon QuickSight"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "ElastiCache provides an in-memory cache (Redis or Memcached) in front of the database to serve "
                       "hot reads with low latency and offload the backend.",
            "distractors": {
                "A": "Athena queries data in S3 with SQL; it is not an in-memory cache fronting a database.",
                "B": "Glue is a managed ETL service, not a cache.",
                "D": "QuickSight is BI visualization, not a cache.",
            },
            "exam_pattern": "In-memory cache to offload a database and cut latency = Amazon ElastiCache.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing database solutions (ElastiCache)"],
    },
    {
        "id": "saa-perf-013", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_database_perf",
        "difficulty": 3, "type": "mcq",
        "stem": "An application needs an in-memory data store that supports replication, high availability with "
                "failover, persistence, and advanced data structures (sorted sets, pub/sub). Which ElastiCache "
                "engine BEST fits?",
        "options": [
            {"id": "A", "text": "ElastiCache for Memcached"},
            {"id": "B", "text": "Amazon RDS for MySQL"},
            {"id": "C", "text": "Amazon Neptune"},
            {"id": "D", "text": "ElastiCache for Redis"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Redis supports replication, Multi-AZ failover, persistence, and rich data structures "
                       "(sorted sets, pub/sub), which Memcached does not.",
            "distractors": {
                "A": "Memcached is a simple, multi-threaded cache without persistence, replication, or advanced data structures.",
                "B": "RDS MySQL is a disk-based relational database, not an in-memory store.",
                "C": "Neptune is a graph database, not an in-memory cache.",
            },
            "exam_pattern": "Need replication/HA/persistence/advanced structures = Redis; simple multi-threaded cache = Memcached.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing database solutions (Redis vs Memcached)"],
    },
    {
        "id": "saa-perf-014", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_database_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants a MySQL-compatible managed relational database with much higher performance than "
                "standard RDS MySQL, storage that scales automatically, and up to 15 low-latency read replicas. "
                "Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon Aurora"},
            {"id": "B", "text": "Amazon DynamoDB"},
            {"id": "C", "text": "Amazon Redshift"},
            {"id": "D", "text": "Self-managed MySQL on EC2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Aurora is a MySQL/PostgreSQL-compatible managed database with high performance, auto-scaling "
                       "shared storage, and up to 15 low-latency read replicas.",
            "distractors": {
                "B": "DynamoDB is a NoSQL key-value store, not MySQL-compatible relational.",
                "C": "Redshift is an analytics data warehouse, not an OLTP MySQL-compatible database.",
                "D": "Self-managed MySQL on EC2 shifts all administration to you and lacks Aurora's managed scaling and replica design.",
            },
            "exam_pattern": "High-performance, MySQL/PostgreSQL-compatible managed relational with auto-scaling storage + many replicas = Aurora.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing database solutions (Aurora)"],
    },
    {
        "id": "saa-perf-015", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_database_perf",
        "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: To scale read throughput of an Amazon RDS or Aurora database, you add one or "
                "more read ________ (one word), which serve read-only queries separately from the primary.",
        "correct": ["replicas", "replica", "read replicas", "read replica"],
        "explanation": {
            "correct": "Read replicas serve read-only traffic (asynchronously replicated), letting you scale reads "
                       "horizontally and relieve the primary instance.",
            "distractors": {},
            "exam_pattern": "Scale reads = read replicas (read-only); HA/failover = Multi-AZ.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing database solutions (read replicas)"],
    },

    # ===== saa_network_perf =================================================
    {
        "id": "saa-perf-016", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_network_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "A media company serves images and video to a global audience from an S3 origin and wants to reduce "
                "latency by caching content at locations close to users. Which service BEST provides this?",
        "options": [
            {"id": "A", "text": "Amazon Route 53 alone"},
            {"id": "B", "text": "Amazon CloudFront"},
            {"id": "C", "text": "AWS Direct Connect"},
            {"id": "D", "text": "A larger S3 bucket"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "CloudFront is a content delivery network that caches content at edge locations near users, "
                       "cutting latency and offloading the origin.",
            "distractors": {
                "A": "Route 53 resolves DNS; it does not cache content at the edge.",
                "C": "Direct Connect is a private link from on-premises to AWS, not a global content cache.",
                "D": "S3 buckets have no fixed size, and adding capacity does not reduce global latency.",
            },
            "exam_pattern": "Cache/deliver content near users globally = CloudFront (CDN, edge caching).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable network architectures (CloudFront)"],
    },
    {
        "id": "saa-perf-017", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_network_perf",
        "difficulty": 3, "type": "mcq",
        "stem": "A global, latency-sensitive application uses a non-HTTP TCP/UDP protocol and needs two static "
                "anycast IP addresses plus fast regional failover, routing user traffic over the AWS global network. "
                "Which service BEST meets this?",
        "options": [
            {"id": "A", "text": "Amazon CloudFront"},
            {"id": "B", "text": "An internet-facing Application Load Balancer only"},
            {"id": "C", "text": "AWS Global Accelerator"},
            {"id": "D", "text": "Amazon Route 53 weighted routing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Global Accelerator provides two static anycast IPs, routes traffic over the AWS backbone to the "
                       "optimal healthy endpoint, and supports TCP/UDP with fast failover - ideal for non-HTTP apps.",
            "distractors": {
                "A": "CloudFront is optimized for cacheable HTTP(S) content, not arbitrary TCP/UDP with static anycast IPs.",
                "B": "An ALB is regional and layer-7 HTTP; it does not provide global anycast IPs or cross-Region routing.",
                "D": "Route 53 weighted routing uses DNS and is subject to caching/TTLs, so failover is slower than Global Accelerator's.",
            },
            "exam_pattern": "Global TCP/UDP, static anycast IPs, fast failover over AWS backbone = Global Accelerator; cacheable HTTP = CloudFront.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable network architectures (Global Accelerator)"],
    },
    {
        "id": "saa-perf-018", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_network_perf",
        "difficulty": 2, "type": "mcq",
        "stem": "An application requires very high network throughput and packets-per-second with consistently low "
                "latency between EC2 instances. Which capability should the architect use?",
        "options": [
            {"id": "A", "text": "A larger EBS volume"},
            {"id": "B", "text": "S3 Transfer Acceleration"},
            {"id": "C", "text": "A NAT gateway in front of the instances"},
            {"id": "D", "text": "Enhanced networking with the Elastic Network Adapter (ENA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Enhanced networking (ENA, and EFA for HPC) gives higher packets-per-second, higher throughput, "
                       "and lower, more consistent latency between instances.",
            "distractors": {
                "A": "EBS size affects storage, not network performance.",
                "B": "Transfer Acceleration speeds S3 uploads over the internet, not inter-instance networking.",
                "C": "A NAT gateway provides outbound internet for private subnets; it does not boost inter-instance throughput and adds a hop.",
            },
            "exam_pattern": "High pps/throughput, low latency on EC2 = enhanced networking (ENA; EFA for tightly coupled HPC).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable network architectures (enhanced networking)"],
    },
    {
        "id": "saa-perf-019", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_network_perf",
        "difficulty": 1, "type": "mcq",
        "stem": "A company needs a dedicated, consistent, high-bandwidth private network connection between its "
                "on-premises data center and AWS, avoiding the variability of the public internet. Which service "
                "BEST meets this?",
        "options": [
            {"id": "A", "text": "AWS Direct Connect"},
            {"id": "B", "text": "A Site-to-Site VPN over the public internet"},
            {"id": "C", "text": "Amazon CloudFront"},
            {"id": "D", "text": "An interface VPC endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Direct Connect is a dedicated private connection between on-premises and AWS, offering more "
                       "consistent bandwidth and latency than the public internet.",
            "distractors": {
                "B": "A VPN traverses the public internet with more variable latency/throughput than a dedicated link.",
                "C": "CloudFront is a CDN, not a private on-premises connection.",
                "D": "A VPC endpoint provides private access to AWS services from within a VPC, not a link from on-premises.",
            },
            "exam_pattern": "Dedicated, consistent, private on-prem<->AWS bandwidth = Direct Connect; encrypted-over-internet/quick = Site-to-Site VPN.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable network architectures (Direct Connect)"],
    },
    {
        "id": "saa-perf-020", "exam": "saa",
        "domain": "saa_performing", "subtopic": "saa_network_perf",
        "difficulty": 3, "type": "multi",
        "stem": "A globally used, read-heavy application must reduce latency for users far from the single Region "
                "where it runs. Which TWO approaches BEST improve read performance for distant users? (Choose two.)",
        "options": [
            {"id": "A", "text": "Serve static content through Amazon CloudFront edge locations"},
            {"id": "B", "text": "Add cross-Region read replicas (or a global database) closer to users"},
            {"id": "C", "text": "Downgrade the database to a smaller instance to save money"},
            {"id": "D", "text": "Remove all caching so requests always read from the origin"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Caching at CloudFront edge locations and placing read replicas/global database copies closer "
                       "to users both cut read latency for distant users.",
            "distractors": {
                "C": "A smaller database reduces performance and worsens latency under load.",
                "D": "Removing caching increases origin load and latency - the opposite of the goal.",
            },
            "exam_pattern": "Reduce global read latency = edge caching (CloudFront) + read replicas/global tables near users.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 3 - Determine high-performing / scalable network architectures (global read performance)"],
    },
]
