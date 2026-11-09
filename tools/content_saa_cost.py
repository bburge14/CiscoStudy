"""AWS Certified Solutions Architect - Associate (SAA-C03) pool.

Domain 4: Design Cost-Optimized Architectures (saa_cost). Original, scenario-based
practice items for the four cost subtopics tracked in the engine:

  * saa_cost_compute    - EC2 purchasing options (On-Demand, Reserved, Spot,
                          Savings Plans) and right-sizing to cut compute spend.
  * saa_cost_storage    - S3 Intelligent-Tiering, lifecycle policies, Glacier
                          tiers, Standard-IA, and gp2 -> gp3 cost optimization.
  * saa_cost_management  - AWS Budgets, Cost Explorer, cost allocation tags, and
                          Trusted Advisor cost-optimization checks.
  * saa_cost_network    - gateway VPC endpoints to avoid NAT charges, CloudFront
                          to cut data-transfer-out cost, and cross-AZ / cross-Region
                          data-transfer awareness.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer is not positionally biased,
every wrong option carries a distractor note, and each item maps to the SAA-C03
exam-guide task statement. Items test durable pricing-model and design trade-offs -
not exact prices, region trivia, or real/memorized exam content.
"""

QUESTIONS = [
    # ===== saa_cost_compute =================================================
    {
        "id": "saa-cost-001", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_compute",
        "difficulty": 2, "type": "mcq",
        "stem": "A company runs a fault-tolerant batch image-processing job that can be interrupted and resumed. "
                "It wants the lowest possible EC2 compute cost. Which purchasing option fits BEST?",
        "options": [
            {"id": "A", "text": "Spot Instances"},
            {"id": "B", "text": "On-Demand Instances"},
            {"id": "C", "text": "Standard Reserved Instances (3-year)"},
            {"id": "D", "text": "Dedicated Hosts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spot Instances offer the deepest discount (up to about 90% off On-Demand) for interruptible, "
                       "fault-tolerant workloads that can tolerate capacity reclamation.",
            "distractors": {
                "B": "On-Demand has no discount and is costlier for interruption-tolerant work.",
                "C": "Reserved Instances commit to steady-state usage for 1-3 years; they suit always-on baseline load, not sporadic batch.",
                "D": "Dedicated Hosts are the most expensive option, aimed at licensing/compliance needs.",
            },
            "exam_pattern": "Interruptible + fault-tolerant + cheapest = Spot; steady baseline = Reserved/Savings Plans; short-term unpredictable = On-Demand.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized compute solutions (Spot)"],
    },
    {
        "id": "saa-cost-002", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_compute",
        "difficulty": 2, "type": "mcq",
        "stem": "A production database runs 24/7 at a predictable, steady level for at least the next three years. "
                "Which EC2 pricing approach BEST reduces its cost?",
        "options": [
            {"id": "A", "text": "Spot Instances"},
            {"id": "B", "text": "A Reserved Instance or Savings Plan commitment"},
            {"id": "C", "text": "On-Demand Instances"},
            {"id": "D", "text": "Scaling the instance to zero each night"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A 1- or 3-year Reserved Instance or Savings Plan gives a significant discount in exchange for a "
                       "usage commitment, which suits steady, predictable, long-running workloads.",
            "distractors": {
                "A": "Spot can be interrupted, which is unacceptable for an always-on production database.",
                "C": "On-Demand is the most expensive choice for steady, predictable usage.",
                "D": "A 24/7 database cannot be scaled to zero nightly.",
            },
            "exam_pattern": "Steady, predictable, long-term usage = Reserved Instances / Savings Plans (commitment discount).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized compute solutions (Reserved/Savings Plans)"],
    },
    {
        "id": "saa-cost-003", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_compute",
        "difficulty": 3, "type": "mcq",
        "stem": "A company wants a commitment-based discount that applies flexibly across EC2 instance families and "
                "Regions, and also covers AWS Fargate and Lambda usage, without locking to one instance type. Which "
                "option BEST fits?",
        "options": [
            {"id": "A", "text": "Standard Reserved Instances for one instance type"},
            {"id": "B", "text": "Spot Instances"},
            {"id": "C", "text": "Compute Savings Plans"},
            {"id": "D", "text": "On-Demand Capacity Reservations"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Compute Savings Plans give a discount for an hourly spend commitment that applies flexibly "
                       "across EC2 (any family/Region), Fargate, and Lambda.",
            "distractors": {
                "A": "Standard RIs lock to attributes like instance family/Region and do not cover Fargate/Lambda.",
                "B": "Spot offers discounts but no committed coverage across services and can be interrupted.",
                "D": "Capacity Reservations ensure capacity but do not provide a committed-use discount across Fargate/Lambda.",
            },
            "exam_pattern": "Flexible commitment across EC2/Fargate/Lambda = Compute Savings Plans; max discount, least flexible = Standard RIs.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized compute solutions (Savings Plans)"],
    },
    {
        "id": "saa-cost-004", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_compute",
        "difficulty": 2, "type": "mcq",
        "stem": "An analysis shows EC2 instances are consistently utilized at only 10-15%. Which action MOST "
                "directly reduces cost while maintaining performance?",
        "options": [
            {"id": "A", "text": "Buy 3-year Reserved Instances for the current oversized instances"},
            {"id": "B", "text": "Add more instances of the same size"},
            {"id": "C", "text": "Move the instances to Dedicated Hosts"},
            {"id": "D", "text": "Right-size to smaller instance types and use Auto Scaling for peaks"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Right-sizing to smaller instances matched to real utilization cuts waste, and Auto Scaling "
                       "handles occasional peaks without permanent over-provisioning.",
            "distractors": {
                "A": "Committing to Reserved pricing on oversized instances locks in the waste.",
                "B": "Adding capacity increases cost without addressing low utilization.",
                "C": "Dedicated Hosts raise cost and do not fix over-provisioning.",
            },
            "exam_pattern": "Low utilization = right-size (smaller types) + Auto Scaling; don't reserve waste.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized compute solutions (right-sizing)"],
    },
    {
        "id": "saa-cost-005", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_compute",
        "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: EC2 ____ Instances offer the largest discount (up to about 90% off On-Demand) in "
                "exchange for the possibility that AWS reclaims the capacity with little notice, making them ideal "
                "for interruptible workloads. (one word)",
        "correct": ["spot"],
        "explanation": {
            "correct": "Spot Instances use spare EC2 capacity at a steep discount and can be reclaimed on short "
                       "notice, so they fit fault-tolerant, interruptible workloads.",
            "distractors": {},
            "exam_pattern": "Deepest discount + interruptible = Spot Instances.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized compute solutions (Spot pricing model)"],
    },

    # ===== saa_cost_storage =================================================
    {
        "id": "saa-cost-006", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_storage",
        "difficulty": 2, "type": "mcq",
        "stem": "A company stores objects whose access patterns are unknown and change over time, and wants to "
                "minimize storage cost automatically without performance impact or retrieval fees for moving between "
                "frequent and infrequent tiers. Which S3 storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Intelligent-Tiering"},
            {"id": "B", "text": "S3 Standard"},
            {"id": "C", "text": "S3 Glacier Deep Archive"},
            {"id": "D", "text": "S3 One Zone-Infrequent Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Intelligent-Tiering automatically moves objects between frequent and infrequent access "
                       "tiers based on usage, optimizing cost with no retrieval fees for those movements.",
            "distractors": {
                "B": "S3 Standard does not automatically optimize cost for infrequently accessed objects.",
                "C": "Deep Archive is for long-term archival with retrieval latency, unsuitable for unpredictable active access.",
                "D": "One Zone-IA assumes known infrequent access and sacrifices AZ redundancy; it does not auto-tier.",
            },
            "exam_pattern": "Unknown/changing access patterns, auto cost-optimize = S3 Intelligent-Tiering.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized storage solutions (Intelligent-Tiering)"],
    },
    {
        "id": "saa-cost-007", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_storage",
        "difficulty": 2, "type": "mcq",
        "stem": "Logs in S3 are accessed often for 30 days, rarely after that, and must be archived cheaply for 7 "
                "years. Which S3 capability BEST automates moving and expiring this data to cut cost?",
        "options": [
            {"id": "A", "text": "Manually copying objects between buckets each month"},
            {"id": "B", "text": "S3 Lifecycle policies that transition objects to Glacier tiers and later expire them"},
            {"id": "C", "text": "Enabling S3 Transfer Acceleration"},
            {"id": "D", "text": "Turning off versioning"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "S3 Lifecycle rules automatically transition objects to cheaper classes (e.g., Glacier tiers) "
                       "as they age and can expire them after a retention period.",
            "distractors": {
                "A": "Manual copying is error-prone and does not scale.",
                "C": "Transfer Acceleration speeds uploads; it does not tier or expire data.",
                "D": "Disabling versioning does not archive or transition data by age.",
            },
            "exam_pattern": "Age-based transition/expiration to cheaper tiers = S3 Lifecycle policies.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized storage solutions (lifecycle policies)"],
    },
    {
        "id": "saa-cost-008", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_storage",
        "difficulty": 2, "type": "mcq",
        "stem": "Compliance data must be retained for 10 years, is almost never accessed, and a retrieval time of "
                "up to 12 hours is acceptable. Which storage class offers the LOWEST cost?",
        "options": [
            {"id": "A", "text": "S3 Standard-Infrequent Access"},
            {"id": "B", "text": "S3 Intelligent-Tiering"},
            {"id": "C", "text": "S3 Glacier Deep Archive"},
            {"id": "D", "text": "S3 Glacier Instant Retrieval"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Glacier Deep Archive is the lowest-cost S3 storage class, designed for long-term archives that "
                       "are rarely accessed and can tolerate retrieval times measured in hours.",
            "distractors": {
                "A": "Standard-IA costs far more than archival tiers for data almost never read.",
                "B": "Intelligent-Tiering suits changing access patterns, not decade-long cold data at lowest cost.",
                "D": "Glacier Instant Retrieval costs more than Deep Archive because it offers millisecond access, which is not needed here.",
            },
            "exam_pattern": "Cheapest archive, retrieval in hours acceptable = Glacier Deep Archive; instant archive reads = Glacier Instant Retrieval.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized storage solutions (Glacier tiers)"],
    },
    {
        "id": "saa-cost-009", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_storage",
        "difficulty": 2, "type": "mcq",
        "stem": "A team wants to reduce EBS cost on general-purpose SSD volumes while keeping or improving baseline "
                "performance. Which change is a straightforward cost optimization?",
        "options": [
            {"id": "A", "text": "Convert all volumes to Provisioned IOPS io2"},
            {"id": "B", "text": "Move the volumes to instance store"},
            {"id": "C", "text": "Increase volume size just to gain IOPS"},
            {"id": "D", "text": "Migrate gp2 volumes to gp3"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "gp3 generally costs less per GB than gp2 while providing a solid baseline and letting you "
                       "provision IOPS/throughput independently of size - a common straightforward saving.",
            "distractors": {
                "A": "io2 is premium-priced for high IOPS/durability, raising cost.",
                "B": "Instance store is ephemeral and cannot replace persistent EBS.",
                "C": "Oversizing to gain IOPS (the gp2 model) wastes capacity; gp3 avoids it.",
            },
            "exam_pattern": "Lower general-purpose EBS cost with equal/better baseline = migrate gp2 -> gp3.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized storage solutions (EBS gp3)"],
    },
    {
        "id": "saa-cost-010", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_storage",
        "difficulty": 2, "type": "mcq",
        "stem": "A company keeps data that is accessed about once a month but must be retrieved within "
                "milliseconds when needed, and wants lower storage cost than S3 Standard. Which storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Standard-Infrequent Access (Standard-IA)"},
            {"id": "B", "text": "S3 Standard"},
            {"id": "C", "text": "S3 Glacier Deep Archive"},
            {"id": "D", "text": "An archive-only tier with multi-hour retrieval"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Standard-IA offers millisecond access at a lower per-GB storage price than Standard, suited to "
                       "data accessed infrequently but needed immediately when requested.",
            "distractors": {
                "B": "Standard costs more for data accessed only a few times a year.",
                "C": "Deep Archive has multi-hour retrieval, which fails the millisecond requirement.",
                "D": "Forcing an archive-only tier adds retrieval latency; IA is the direct fit for infrequent but instant access.",
            },
            "exam_pattern": "Infrequent access + instant (ms) retrieval + lower cost = S3 Standard-IA (One Zone-IA if single-AZ acceptable).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized storage solutions (Standard-IA)"],
    },

    # ===== saa_cost_management ==============================================
    {
        "id": "saa-cost-011", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_management",
        "difficulty": 1, "type": "mcq",
        "stem": "A finance team wants to be alerted automatically when monthly AWS spending is forecast to exceed a "
                "set threshold. Which service BEST provides this?",
        "options": [
            {"id": "A", "text": "AWS CloudTrail"},
            {"id": "B", "text": "AWS Budgets"},
            {"id": "C", "text": "AWS Config"},
            {"id": "D", "text": "Amazon Inspector"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Budgets lets you define cost/usage thresholds (including forecasted spend) and sends alerts "
                       "when actual or projected spending crosses them.",
            "distractors": {
                "A": "CloudTrail logs API activity, not budget thresholds.",
                "C": "Config tracks resource configuration compliance, not spend.",
                "D": "Inspector scans for software vulnerabilities.",
            },
            "exam_pattern": "Set spend/usage thresholds + alerts = AWS Budgets.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized architectures (AWS Budgets)"],
    },
    {
        "id": "saa-cost-012", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_management",
        "difficulty": 2, "type": "mcq",
        "stem": "An architect needs to visualize and analyze historical cost and usage trends over the past year to "
                "find the biggest cost drivers. Which tool is designed for this?",
        "options": [
            {"id": "A", "text": "AWS Budgets alerts only"},
            {"id": "B", "text": "Amazon CloudWatch dashboards for application metrics"},
            {"id": "C", "text": "AWS Cost Explorer"},
            {"id": "D", "text": "AWS Trusted Advisor security checks"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Cost Explorer visualizes and analyzes historical cost and usage with filtering and grouping, "
                       "making it easy to spot the biggest cost drivers and trends.",
            "distractors": {
                "A": "Budgets is for threshold alerts, not rich historical trend analysis.",
                "B": "CloudWatch dashboards show operational/application metrics, not detailed cost breakdowns.",
                "D": "Trusted Advisor gives best-practice checks, not deep cost-trend visualization.",
            },
            "exam_pattern": "Visualize/analyze historical cost & usage trends = Cost Explorer; threshold alerts = Budgets.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized architectures (Cost Explorer)"],
    },
    {
        "id": "saa-cost-013", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_management",
        "difficulty": 2, "type": "mcq",
        "stem": "A company needs to break down its AWS bill by department and project to charge back costs. Which "
                "feature BEST enables this attribution?",
        "options": [
            {"id": "A", "text": "Security groups"},
            {"id": "B", "text": "IAM roles"},
            {"id": "C", "text": "Placement groups"},
            {"id": "D", "text": "Cost allocation tags"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Activated cost allocation tags attach metadata (e.g., department, project) to resources so "
                       "costs can be grouped and attributed in Cost Explorer and cost/usage reports.",
            "distractors": {
                "A": "Security groups filter network traffic, not attribute cost.",
                "B": "IAM roles grant permissions, not cost breakdowns.",
                "C": "Placement groups affect instance placement, not billing categorization.",
            },
            "exam_pattern": "Attribute / charge back costs by team/project = cost allocation tags.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized architectures (cost allocation tags)"],
    },
    {
        "id": "saa-cost-014", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_management",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants automated recommendations that flag idle or underutilized resources (such as idle "
                "load balancers or low-utilization EC2 instances) to save money. Which service provides these "
                "best-practice checks?",
        "options": [
            {"id": "A", "text": "AWS Trusted Advisor"},
            {"id": "B", "text": "AWS CloudFormation"},
            {"id": "C", "text": "Amazon Macie"},
            {"id": "D", "text": "AWS Step Functions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Trusted Advisor runs best-practice checks, including cost optimization, that flag idle or "
                       "underutilized resources and other savings opportunities.",
            "distractors": {
                "B": "CloudFormation provisions infrastructure as code; it does not flag idle resources for savings.",
                "C": "Macie classifies sensitive data.",
                "D": "Step Functions orchestrates workflows.",
            },
            "exam_pattern": "Best-practice checks incl. cost optimization (idle/underused resources) = Trusted Advisor.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized architectures (Trusted Advisor)"],
    },
    {
        "id": "saa-cost-015", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_management",
        "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: To receive an automated alert when your actual or forecasted AWS costs cross a "
                "threshold you define, you create an AWS ______ (the cost-and-usage threshold service).",
        "correct": ["budget", "budgets", "aws budget", "aws budgets"],
        "explanation": {
            "correct": "AWS Budgets lets you set custom cost or usage thresholds and notifies you when actual or "
                       "forecasted values exceed them.",
            "distractors": {},
            "exam_pattern": "Threshold-based cost/usage alerts = AWS Budgets (Cost Explorer = analysis/visualization).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized architectures (AWS Budgets)"],
    },

    # ===== saa_cost_network =================================================
    {
        "id": "saa-cost-016", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_network",
        "difficulty": 3, "type": "mcq",
        "stem": "Instances in private subnets download large volumes of data from Amazon S3 through a NAT gateway, "
                "and the NAT data-processing charges are high. Which change BEST reduces this cost?",
        "options": [
            {"id": "A", "text": "Add a second NAT gateway"},
            {"id": "B", "text": "Create an S3 gateway VPC endpoint so S3 traffic bypasses the NAT gateway"},
            {"id": "C", "text": "Give each instance a public IP address"},
            {"id": "D", "text": "Enable S3 Transfer Acceleration"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A gateway VPC endpoint for S3 routes S3 traffic privately and is free, so it removes the NAT "
                       "gateway data-processing charges for that traffic.",
            "distractors": {
                "A": "A second NAT gateway adds cost rather than removing the NAT data-processing charges.",
                "C": "Public IPs route over the internet (still incurring transfer costs) and reduce security.",
                "D": "Transfer Acceleration adds a fee for faster uploads; it does not remove NAT costs for S3 access.",
            },
            "exam_pattern": "Private S3/DynamoDB access without NAT costs = gateway VPC endpoint (free); avoids NAT data-processing charges.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized network architectures (gateway endpoints vs NAT)"],
    },
    {
        "id": "saa-cost-017", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_network",
        "difficulty": 2, "type": "mcq",
        "stem": "A popular website serves the same large static assets to many users directly from S3, and "
                "data-transfer-out costs are rising. Which service BEST lowers these costs while improving "
                "performance?",
        "options": [
            {"id": "A", "text": "Enabling S3 Versioning"},
            {"id": "B", "text": "Moving the assets to S3 Glacier"},
            {"id": "C", "text": "Amazon CloudFront in front of the S3 origin"},
            {"id": "D", "text": "Adding more S3 buckets in the same Region"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "CloudFront caches assets at edge locations, so repeated requests are served from the cache "
                       "rather than refetched from the origin, reducing origin data-transfer costs and improving latency.",
            "distractors": {
                "A": "Versioning does not reduce transfer costs.",
                "B": "Glacier is archival and cannot directly serve live website assets with low latency.",
                "D": "More buckets in the same Region do not reduce data-transfer-out costs.",
            },
            "exam_pattern": "Cache popular content at the edge to cut origin data-transfer cost + latency = CloudFront.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized network architectures (CloudFront data transfer)"],
    },
    {
        "id": "saa-cost-018", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_network",
        "difficulty": 3, "type": "mcq",
        "stem": "An architect notices significant data-transfer charges from chatty traffic between two tiers "
                "deployed in different Availability Zones. Which approach can reduce these specific charges?",
        "options": [
            {"id": "A", "text": "Route the traffic through a NAT gateway"},
            {"id": "B", "text": "Send the traffic over the public internet using Elastic IPs"},
            {"id": "C", "text": "Enable detailed CloudWatch monitoring"},
            {"id": "D", "text": "Keep high-volume communicating components in the same Availability Zone, using private IPs, where resilience requirements allow"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Data transfer between AZs in the same Region is billable; co-locating chatty components in a "
                       "single AZ and using private IPs avoids the cross-AZ charge (balanced against HA needs).",
            "distractors": {
                "A": "A NAT gateway is for outbound internet access and adds processing charges, not reduce inter-AZ transfer.",
                "B": "Using public endpoints/Elastic IPs can incur more data-transfer cost and reduce security.",
                "C": "Monitoring shows the cost but does not reduce the cross-AZ transfer itself.",
            },
            "exam_pattern": "Cross-AZ data transfer is billable; co-locate chatty components in one AZ with private IPs (within HA limits) to cut it.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized network architectures (cross-AZ data transfer)"],
    },
    {
        "id": "saa-cost-019", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_network",
        "difficulty": 1, "type": "mcq",
        "stem": "A data-processing fleet of EC2 instances repeatedly reads large datasets from S3. To avoid "
                "unnecessary data-transfer charges, where should the S3 bucket be located relative to the instances?",
        "options": [
            {"id": "A", "text": "In the same AWS Region as the EC2 instances"},
            {"id": "B", "text": "In a different Region to spread load"},
            {"id": "C", "text": "Accessed only via the public internet"},
            {"id": "D", "text": "In S3 Glacier Deep Archive to lower transfer cost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data transfer between S3 and EC2 in the same Region does not incur transfer charges, so "
                       "co-locating the bucket and instances in one Region avoids unnecessary cost (and latency).",
            "distractors": {
                "B": "Cross-Region transfer between S3 and EC2 incurs charges and adds latency.",
                "C": "Forcing public-internet access can add transfer cost and reduce security versus in-Region private access.",
                "D": "Glacier is archival with retrieval fees/latency; it does not address transfer-cost placement and cannot serve as a live dataset readily.",
            },
            "exam_pattern": "S3<->EC2 data transfer in the SAME Region is free; cross-Region is billable - co-locate to cut cost.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized network architectures (same-Region data transfer)"],
    },
    {
        "id": "saa-cost-020", "exam": "saa",
        "domain": "saa_cost", "subtopic": "saa_cost_network",
        "difficulty": 3, "type": "multi",
        "stem": "A team wants to reduce networking costs for private-subnet workloads that access AWS services. "
                "Which TWO actions reduce cost? (Choose two.)",
        "options": [
            {"id": "A", "text": "Use gateway VPC endpoints for S3 and DynamoDB to avoid NAT gateway data-processing charges"},
            {"id": "B", "text": "Co-locate heavily communicating components in the same Availability Zone (within HA limits) to reduce cross-AZ transfer charges"},
            {"id": "C", "text": "Replace all private subnets with public subnets and public IP addresses"},
            {"id": "D", "text": "Add redundant NAT gateways in every AZ regardless of need"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Gateway endpoints for S3/DynamoDB are free and remove NAT data-processing charges, and "
                       "co-locating chatty components in one AZ reduces billable cross-AZ transfer.",
            "distractors": {
                "C": "Exposing workloads publicly reduces security and does not reliably cut transfer cost.",
                "D": "Adding NAT gateways everywhere increases hourly and data-processing charges.",
            },
            "exam_pattern": "Cut network cost = gateway endpoints (free S3/DynamoDB) + keep traffic in-AZ/in-Region + minimize NAT reliance.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 4 - Design cost-optimized network architectures (endpoints, NAT, data transfer)"],
    },
]
