"""AWS Certified Cloud Practitioner (CLF-C02) item pool — Domain 3: Cloud
Technology and Services.

Original, objective-aligned practice questions written to the public CLF-C02
exam guide (Domain 3 only); never real or memorized exam items. Content is kept
at Cloud-Practitioner depth: service purpose, when-to-use, and high-level
characteristics — no exact limits, prices, or API parameters. build_content.py
shuffles option order (seeded by id), so the answer key is not positionally
biased here.
"""

QUESTIONS = [
    # ===== global_infrastructure ==========================================
    {
        "id": "clf-tech-001", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 1, "type": "mcq",
        "stem": "A company wants the name for the top-level geographic area where AWS "
                "clusters its data centers worldwide. Which term describes this?",
        "options": [
            {"id": "A", "text": "An AWS Region"},
            {"id": "B", "text": "An Availability Zone"},
            {"id": "C", "text": "An edge location"},
            {"id": "D", "text": "A VPC subnet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Region is a named, physical geographic area (e.g., us-east-1) that "
                       "contains multiple, isolated Availability Zones.",
            "distractors": {
                "B": "An Availability Zone is one or more data centers INSIDE a Region, not the "
                     "top-level geographic area.",
                "C": "Edge locations are CloudFront caching sites for content delivery, not the "
                     "Region container itself.",
                "D": "A subnet is a range of IP addresses within a VPC — a networking construct, "
                     "not a geographic Region.",
            },
            "exam_pattern": "Hierarchy cue: Region > Availability Zone > data center; edge locations "
                            "sit outside this hierarchy for content delivery.",
        },
        "references": ["AWS Global Infrastructure (Regions and Availability Zones)"],
    },
    {
        "id": "clf-tech-002", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 2, "type": "mcq",
        "stem": "An application must stay available even if one data center fails. Across "
                "what should its resources be deployed within a single Region?",
        "options": [
            {"id": "A", "text": "Multiple Availability Zones"},
            {"id": "B", "text": "A single Availability Zone with larger instances"},
            {"id": "C", "text": "A single edge location"},
            {"id": "D", "text": "Multiple AWS accounts in the same data center"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AZs are physically isolated with independent power and networking, so "
                       "spreading resources across multiple AZs keeps the app running if one AZ fails.",
            "distractors": {
                "B": "A bigger instance in ONE AZ still fails entirely if that AZ goes down — no "
                     "high availability.",
                "C": "Edge locations cache content for delivery; they do not run or fail over "
                     "application compute.",
                "D": "Multiple accounts in the SAME data center share one failure domain, so one "
                     "outage still takes everything down.",
            },
            "exam_pattern": "High availability keyword -> 'multiple Availability Zones' within a Region.",
        },
        "references": ["AWS Global Infrastructure (Availability Zones)"],
    },
    {
        "id": "clf-tech-003", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 1, "type": "mcq",
        "stem": "A streaming site wants to cache content at locations physically close to "
                "viewers to cut latency. Which part of AWS infrastructure does this?",
        "options": [
            {"id": "A", "text": "Edge locations (CloudFront points of presence)"},
            {"id": "B", "text": "Availability Zones"},
            {"id": "C", "text": "Regions"},
            {"id": "D", "text": "VPC private subnets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Edge locations are Amazon CloudFront's global points of presence that cache "
                       "content near users to reduce latency.",
            "distractors": {
                "B": "AZs host core compute and storage within a Region; they are not the global "
                     "caching tier for end users.",
                "C": "A Region is the broad geographic area; caching close to users happens at edge "
                     "locations, not Regions.",
                "D": "A private subnet is an internal network segment and has nothing to do with "
                     "caching content near viewers.",
            },
            "exam_pattern": "'Cache near users / low latency content delivery' -> edge locations / CloudFront.",
        },
        "references": ["Amazon CloudFront edge locations"],
    },
    {
        "id": "clf-tech-004", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 3, "type": "mcq",
        "stem": "A European bank is legally required to keep customer data inside one country. "
                "Which factor should MOST drive its AWS Region selection?",
        "options": [
            {"id": "A", "text": "Compliance and data residency requirements"},
            {"id": "B", "text": "The Region with the lowest compute prices"},
            {"id": "C", "text": "The Region physically closest to end users"},
            {"id": "D", "text": "The Region offering the most services"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When law dictates where data may physically reside, compliance and data "
                       "residency govern the Region choice above all other factors.",
            "distractors": {
                "B": "Price is a real Region-selection factor, but it cannot override a legal "
                     "requirement to keep data in-country.",
                "C": "Latency/proximity matters for user experience, yet it does not satisfy a data "
                     "residency mandate on its own.",
                "D": "Service availability is a valid consideration, but it does not address the "
                     "legal obligation to keep data in a specific country.",
            },
            "exam_pattern": "Four Region-choice factors: compliance, latency, price, service availability — "
                            "a legal/data-residency scenario keys to compliance.",
        },
        "references": ["Choosing an AWS Region (compliance and data residency)"],
    },
    {
        "id": "clf-tech-005", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 3, "type": "mcq",
        "stem": "A gaming studio needs very low latency for users in a large metro far from any "
                "Region. Which option places compute closer to them?",
        "options": [
            {"id": "A", "text": "AWS Local Zones"},
            {"id": "B", "text": "A larger EC2 instance type"},
            {"id": "C", "text": "Amazon S3 Standard"},
            {"id": "D", "text": "A second VPC in the same Region"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Local Zones extend a Region to place compute and storage in or near large "
                       "population centers, lowering latency for nearby users.",
            "distractors": {
                "B": "A bigger instance adds capacity but does not move compute physically closer "
                     "to distant users, so latency is unchanged.",
                "C": "S3 Standard is object storage; it does not reduce the network distance for a "
                     "latency-sensitive game.",
                "D": "Adding a VPC in the same Region keeps resources in the same distant location, "
                     "so latency does not improve.",
            },
            "exam_pattern": "'Low latency in a specific metro far from a Region' -> Local Zones "
                            "(Wavelength for 5G/mobile edge).",
        },
        "references": ["AWS Local Zones"],
    },
    {
        "id": "clf-tech-006", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are components of the AWS global infrastructure? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Availability Zones"},
            {"id": "B", "text": "Edge locations"},
            {"id": "C", "text": "Security groups"},
            {"id": "D", "text": "Amazon S3 buckets"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Availability Zones and edge locations are physical building blocks of the AWS "
                       "global infrastructure, alongside Regions.",
            "distractors": {
                "C": "A security group is a virtual firewall configured inside a VPC — a networking "
                     "feature, not a global-infrastructure component.",
                "D": "An S3 bucket is a storage container you create; it is a service resource, not "
                     "part of the physical global infrastructure.",
            },
            "exam_pattern": "Global-infrastructure list = Regions, Availability Zones, edge locations "
                            "(plus Local Zones/Wavelength); service resources are not on it.",
        },
        "references": ["AWS Global Infrastructure"],
    },

    # ===== compute_services ===============================================
    {
        "id": "clf-tech-007", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 1, "type": "mcq",
        "stem": "A team needs full control of the operating system on resizable virtual servers "
                "in the cloud. Which service provides this?",
        "options": [
            {"id": "A", "text": "Amazon EC2"},
            {"id": "B", "text": "AWS Lambda"},
            {"id": "C", "text": "Amazon S3"},
            {"id": "D", "text": "Amazon RDS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon EC2 provides resizable virtual machines where you control the OS, "
                       "patching, and software — infrastructure as a service.",
            "distractors": {
                "B": "Lambda is serverless; you run code without any server or OS to manage, so you "
                     "do not get OS-level control.",
                "C": "S3 is object storage, not a virtual server with an operating system.",
                "D": "RDS is a managed database service; AWS handles the OS, so you do not get full "
                     "OS control.",
            },
            "exam_pattern": "'Full OS control / virtual server you manage' -> EC2 (IaaS).",
        },
        "references": ["Amazon EC2 instance types"],
    },
    {
        "id": "clf-tech-008", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to run short code in response to events without provisioning "
                "or managing any servers. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Lambda"},
            {"id": "B", "text": "Amazon EC2"},
            {"id": "C", "text": "AWS Elastic Beanstalk"},
            {"id": "D", "text": "Amazon EBS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Lambda is serverless, event-driven compute: you upload code, it runs on "
                       "triggers, and you never provision or manage servers.",
            "distractors": {
                "B": "EC2 requires you to provision and manage virtual servers, which is the "
                     "opposite of 'no servers to manage'.",
                "C": "Elastic Beanstalk still runs your app on provisioned infrastructure (e.g., EC2) "
                     "that exists continuously; it is not event-driven serverless functions.",
                "D": "EBS is block storage for EC2, not a compute service that runs code.",
            },
            "exam_pattern": "'Event-driven, no servers to manage, pay per run' -> Lambda (serverless).",
        },
        "references": ["AWS Lambda"],
    },
    {
        "id": "clf-tech-009", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "An online store's traffic spikes during sales and falls overnight. Which feature "
                "automatically adds and removes EC2 capacity to match demand?",
        "options": [
            {"id": "A", "text": "Amazon EC2 Auto Scaling"},
            {"id": "B", "text": "Elastic Load Balancing"},
            {"id": "C", "text": "AWS Lambda"},
            {"id": "D", "text": "Amazon CloudFront"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EC2 Auto Scaling automatically launches or terminates instances based on "
                       "demand, so capacity scales out and in with the load.",
            "distractors": {
                "B": "Elastic Load Balancing distributes incoming traffic across existing instances; "
                     "it does not add or remove instances.",
                "C": "Lambda runs event-driven functions; it does not scale a fleet of EC2 instances "
                     "up and down.",
                "D": "CloudFront is a CDN that caches content at the edge; it does not manage EC2 "
                     "capacity.",
            },
            "exam_pattern": "'Automatically add/remove capacity to match demand' -> Auto Scaling; "
                            "'spread traffic across existing servers' -> ELB.",
        },
        "references": ["Amazon EC2 Auto Scaling"],
    },
    {
        "id": "clf-tech-010", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "A web application runs on several EC2 instances and needs incoming requests "
                "spread evenly across them. Which service does this?",
        "options": [
            {"id": "A", "text": "Elastic Load Balancing"},
            {"id": "B", "text": "Amazon EC2 Auto Scaling"},
            {"id": "C", "text": "AWS CloudFormation"},
            {"id": "D", "text": "Amazon SNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elastic Load Balancing automatically distributes incoming traffic across "
                       "multiple targets, such as EC2 instances across AZs.",
            "distractors": {
                "B": "Auto Scaling changes how many instances exist; it does not distribute requests "
                     "among them.",
                "C": "CloudFormation provisions infrastructure from templates; it does not route "
                     "live traffic.",
                "D": "SNS is a pub/sub notification service, not a traffic load balancer.",
            },
            "exam_pattern": "'Distribute/spread incoming traffic across instances' -> Elastic Load Balancing.",
        },
        "references": ["Elastic Load Balancing"],
    },
    {
        "id": "clf-tech-011", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 3, "type": "mcq",
        "stem": "A team wants to run containers without provisioning or managing the underlying "
                "EC2 instances. Which option should they choose?",
        "options": [
            {"id": "A", "text": "AWS Fargate"},
            {"id": "B", "text": "Self-managed EC2 instances hosting the containers"},
            {"id": "C", "text": "Amazon RDS"},
            {"id": "D", "text": "Amazon EFS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fargate is a serverless compute engine for containers (with ECS or EKS) that "
                       "runs them without you managing any EC2 servers.",
            "distractors": {
                "B": "Running containers on self-managed EC2 means you patch and operate the servers "
                     "yourself — the opposite of what was asked.",
                "C": "RDS is a managed relational database, not a container runtime.",
                "D": "EFS is shared file storage; it stores data for workloads but does not run "
                     "containers.",
            },
            "exam_pattern": "'Run containers, no servers/EC2 to manage' -> Fargate (serverless containers).",
        },
        "references": ["AWS Fargate"],
    },
    {
        "id": "clf-tech-012", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to upload a web app and let AWS handle provisioning, load "
                "balancing, and scaling automatically. Which service fits?",
        "options": [
            {"id": "A", "text": "AWS Elastic Beanstalk"},
            {"id": "B", "text": "Amazon EC2 configured manually"},
            {"id": "C", "text": "Hand-written AWS CloudFormation templates"},
            {"id": "D", "text": "Amazon DynamoDB"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elastic Beanstalk is a platform service: you upload application code and it "
                       "provisions and manages capacity, load balancing, scaling, and health.",
            "distractors": {
                "B": "Manually configuring EC2 puts all provisioning, scaling, and load balancing "
                     "work on you — not automatic.",
                "C": "CloudFormation can build the resources but you must author and maintain the "
                     "templates; it does not manage the app platform for you.",
                "D": "DynamoDB is a NoSQL database, not an application deployment platform.",
            },
            "exam_pattern": "'Just upload my app, AWS runs the platform' -> Elastic Beanstalk (PaaS).",
        },
        "references": ["AWS Elastic Beanstalk"],
    },
    {
        "id": "clf-tech-013", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 3, "type": "mcq",
        "stem": "A company already runs Kubernetes on-premises and wants a managed Kubernetes "
                "service on AWS. Which service should it choose?",
        "options": [
            {"id": "A", "text": "Amazon EKS"},
            {"id": "B", "text": "Amazon ECS"},
            {"id": "C", "text": "AWS Lambda"},
            {"id": "D", "text": "Amazon EC2 Auto Scaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon EKS (Elastic Kubernetes Service) is AWS's managed Kubernetes, letting "
                       "teams keep their existing Kubernetes tooling and workflows.",
            "distractors": {
                "B": "ECS is AWS's own container orchestration service; it is not Kubernetes, so it "
                     "would not reuse their Kubernetes tooling.",
                "C": "Lambda runs functions, not container orchestration clusters, and has nothing "
                     "to do with Kubernetes.",
                "D": "Auto Scaling adjusts EC2 capacity; it does not provide a managed Kubernetes "
                     "control plane.",
            },
            "exam_pattern": "'Managed Kubernetes' -> EKS; 'AWS-native container orchestration' -> ECS.",
        },
        "references": ["Amazon Elastic Kubernetes Service (EKS)"],
    },

    # ===== storage_services ===============================================
    {
        "id": "clf-tech-014", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 1, "type": "mcq",
        "stem": "A company must store millions of files such as images and backups as objects "
                "retrieved by key. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon S3"},
            {"id": "B", "text": "Amazon EBS"},
            {"id": "C", "text": "Amazon EFS"},
            {"id": "D", "text": "Amazon RDS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon S3 is object storage: data is stored as objects in buckets and "
                       "retrieved by key, scaling to virtually unlimited files.",
            "distractors": {
                "B": "EBS provides block volumes attached to a single EC2 instance, not internet-"
                     "scale object storage.",
                "C": "EFS is a shared file system for Linux instances, not a key-based object store.",
                "D": "RDS is a relational database for structured records, not object storage for "
                     "files.",
            },
            "exam_pattern": "'Objects / buckets / unlimited files by key' -> Amazon S3 (object storage).",
        },
        "references": ["Amazon S3"],
    },
    {
        "id": "clf-tech-015", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "A single EC2 instance needs a persistent block storage volume that behaves like "
                "an attached hard drive. Which service provides this?",
        "options": [
            {"id": "A", "text": "Amazon EBS"},
            {"id": "B", "text": "Amazon S3"},
            {"id": "C", "text": "Amazon EFS"},
            {"id": "D", "text": "Amazon S3 Glacier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon EBS provides block storage volumes that attach to an EC2 instance and "
                       "act like a disk, persisting independently of the instance.",
            "distractors": {
                "B": "S3 is object storage accessed over an API, not a block device you attach to an "
                     "instance like a drive.",
                "C": "EFS is a shared file system mounted by many instances, not a single-instance "
                     "block volume.",
                "D": "S3 Glacier is low-cost archival object storage, not attachable block storage.",
            },
            "exam_pattern": "'Block volume / disk attached to one EC2 instance' -> Amazon EBS.",
        },
        "references": ["Amazon Elastic Block Store (EBS)"],
    },
    {
        "id": "clf-tech-016", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "Several Linux EC2 instances must read and write the same file system at the same "
                "time. Which storage service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon EFS"},
            {"id": "B", "text": "Amazon FSx for Windows File Server"},
            {"id": "C", "text": "Amazon EBS"},
            {"id": "D", "text": "Amazon S3 Glacier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon EFS is a shared, elastic file system that many Linux instances can "
                       "mount and access concurrently over NFS.",
            "distractors": {
                "B": "FSx for Windows File Server provides shared storage for Windows/SMB clients, "
                     "not the Linux/NFS sharing described here.",
                "C": "An EBS volume generally attaches to a single instance, so it does not serve "
                     "many instances sharing one file system.",
                "D": "S3 Glacier is archival object storage, not a mountable shared file system.",
            },
            "exam_pattern": "'Shared file system across many Linux instances' -> EFS; Windows/SMB shares -> FSx.",
        },
        "references": ["Amazon Elastic File System (EFS)"],
    },
    {
        "id": "clf-tech-017", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 3, "type": "mcq",
        "stem": "A hospital must retain records for years, rarely accesses them, and wants the "
                "lowest storage cost. Which S3 storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Glacier Deep Archive"},
            {"id": "B", "text": "S3 Standard"},
            {"id": "C", "text": "S3 Standard-Infrequent Access"},
            {"id": "D", "text": "Amazon EBS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Glacier Deep Archive offers the lowest storage cost for long-term archives "
                       "that are rarely accessed and tolerate retrieval times measured in hours.",
            "distractors": {
                "B": "S3 Standard is designed for frequently accessed data and costs much more to "
                     "store than archival classes.",
                "C": "Standard-IA suits infrequent access that still needs millisecond retrieval; it "
                     "costs more to store than Deep Archive.",
                "D": "EBS is block storage for EC2, not an S3 archival class, and is not the "
                     "lowest-cost option for long-term archives.",
            },
            "exam_pattern": "'Rarely accessed, years, lowest cost, hours to retrieve is fine' -> "
                            "Glacier Deep Archive.",
        },
        "references": ["Amazon S3 storage classes (Glacier Deep Archive)"],
    },
    {
        "id": "clf-tech-018", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "Data is accessed only a few times a year but must return within milliseconds when "
                "needed. Which S3 storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Standard-Infrequent Access"},
            {"id": "B", "text": "S3 Glacier Flexible Retrieval"},
            {"id": "C", "text": "S3 Standard"},
            {"id": "D", "text": "S3 Glacier Deep Archive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Standard-IA lowers storage cost for infrequently accessed data while still "
                       "delivering millisecond retrieval when the data is needed.",
            "distractors": {
                "B": "Glacier Flexible Retrieval is for archives and retrieves in minutes to hours, "
                     "not milliseconds.",
                "C": "S3 Standard gives millisecond access but is priced for frequent access, so it "
                     "costs more than needed here.",
                "D": "Glacier Deep Archive is the slowest, cheapest archive tier; retrieval takes "
                     "hours, not milliseconds.",
            },
            "exam_pattern": "'Infrequent access BUT instant/millisecond retrieval' -> Standard-IA; "
                            "slow retrieval acceptable -> a Glacier class.",
        },
        "references": ["Amazon S3 storage classes (Standard-IA)"],
    },
    {
        "id": "clf-tech-019", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "A company wants its on-premises applications to use AWS cloud storage through a "
                "hybrid connection. Which service enables this?",
        "options": [
            {"id": "A", "text": "AWS Storage Gateway"},
            {"id": "B", "text": "Amazon EBS"},
            {"id": "C", "text": "AWS Backup"},
            {"id": "D", "text": "Amazon EFS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Storage Gateway connects on-premises environments to AWS storage, letting "
                       "local applications use cloud storage in a hybrid setup.",
            "distractors": {
                "B": "EBS is block storage attached to EC2 instances in AWS, not a hybrid on-premises "
                     "gateway.",
                "C": "AWS Backup centrally automates backups of AWS resources; it is not a hybrid "
                     "storage bridge for on-premises apps.",
                "D": "EFS is a shared file system for Linux instances in AWS, not a hybrid "
                     "on-premises connector.",
            },
            "exam_pattern": "'Hybrid / on-premises apps using AWS storage' -> Storage Gateway.",
        },
        "references": ["AWS Storage Gateway"],
    },
    {
        "id": "clf-tech-020", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "multi",
        "stem": "Which TWO statements about Amazon S3 are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "It stores data as objects in buckets."},
            {"id": "B", "text": "It offers multiple storage classes for different access patterns."},
            {"id": "C", "text": "It must be mounted as a block device on a single EC2 instance."},
            {"id": "D", "text": "Its data can be accessed from only one Availability Zone."},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "S3 is object storage organized into buckets, and it provides several storage "
                       "classes (Standard, Standard-IA, Glacier tiers, and more) for different needs.",
            "distractors": {
                "C": "Mounting a block device on one instance describes Amazon EBS, not S3.",
                "D": "S3 stores data redundantly across multiple AZs in a Region, so it is not "
                     "limited to a single AZ.",
            },
            "exam_pattern": "S3 true-statement items hinge on 'objects in buckets' + 'storage classes'; "
                            "block-device / single-AZ wording signals EBS, not S3.",
        },
        "references": ["Amazon S3 (object storage and storage classes)"],
    },

    # ===== database_services ==============================================
    {
        "id": "clf-tech-021", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 1, "type": "mcq",
        "stem": "A team wants a managed relational database and does not want to handle patching, "
                "backups, or hardware. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon RDS"},
            {"id": "B", "text": "Amazon DynamoDB"},
            {"id": "C", "text": "Amazon S3"},
            {"id": "D", "text": "Amazon Redshift"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon RDS is a managed relational database service that handles patching, "
                       "backups, and the underlying hardware for engines like MySQL and PostgreSQL.",
            "distractors": {
                "B": "DynamoDB is a NoSQL key-value database, not a relational database.",
                "C": "S3 is object storage, not a relational database.",
                "D": "Redshift is a data warehouse built for analytics, not a general-purpose "
                     "relational (OLTP) database.",
            },
            "exam_pattern": "'Managed relational database, AWS handles ops' -> Amazon RDS.",
        },
        "references": ["Amazon RDS"],
    },
    {
        "id": "clf-tech-022", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 2, "type": "mcq",
        "stem": "An app needs a fully managed NoSQL key-value database with single-digit-"
                "millisecond performance at any scale. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon DynamoDB"},
            {"id": "B", "text": "Amazon RDS"},
            {"id": "C", "text": "Amazon Redshift"},
            {"id": "D", "text": "Amazon Aurora"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DynamoDB is a fully managed, serverless NoSQL key-value database that delivers "
                       "consistent single-digit-millisecond performance at scale.",
            "distractors": {
                "B": "RDS is a relational (SQL) database, not a NoSQL key-value store.",
                "C": "Redshift is an analytics data warehouse, not a low-latency key-value database.",
                "D": "Aurora is a relational database engine; it is not a NoSQL key-value store.",
            },
            "exam_pattern": "'NoSQL / key-value / serverless, single-digit ms at scale' -> DynamoDB.",
        },
        "references": ["Amazon DynamoDB"],
    },
    {
        "id": "clf-tech-023", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 3, "type": "mcq",
        "stem": "A business wants to run complex analytical queries over petabytes of historical "
                "sales data in a data warehouse. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon Redshift"},
            {"id": "B", "text": "Amazon RDS"},
            {"id": "C", "text": "Amazon DynamoDB"},
            {"id": "D", "text": "Amazon ElastiCache"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Redshift is a managed data warehouse optimized for running complex "
                       "analytical queries over very large datasets.",
            "distractors": {
                "B": "RDS targets transactional (OLTP) relational workloads, not petabyte-scale "
                     "analytical warehousing.",
                "C": "DynamoDB is a key-value store for high-throughput lookups, not complex "
                     "analytical queries across a warehouse.",
                "D": "ElastiCache is an in-memory cache for speeding reads, not a data warehouse for "
                     "analytics.",
            },
            "exam_pattern": "'Data warehouse / analytics over huge historical data' -> Amazon Redshift.",
        },
        "references": ["Amazon Redshift"],
    },
    {
        "id": "clf-tech-024", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 2, "type": "mcq",
        "stem": "To cut database load and speed up reads, a team wants an in-memory cache in front "
                "of its database. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon ElastiCache"},
            {"id": "B", "text": "Amazon RDS"},
            {"id": "C", "text": "Amazon Redshift"},
            {"id": "D", "text": "Amazon S3"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon ElastiCache provides managed in-memory caching (Redis or Memcached) to "
                       "serve frequent reads quickly and reduce load on the backing database.",
            "distractors": {
                "B": "RDS is the backing relational database; it is what you cache in front of, not "
                     "the cache itself.",
                "C": "Redshift is a data warehouse for analytics, not an in-memory cache.",
                "D": "S3 is durable object storage, not a low-latency in-memory cache.",
            },
            "exam_pattern": "'In-memory cache / speed up reads' -> ElastiCache (Redis/Memcached).",
        },
        "references": ["Amazon ElastiCache"],
    },
    {
        "id": "clf-tech-025", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a MySQL- and PostgreSQL-compatible relational database built for "
                "the cloud with higher performance than standard engines. Which service?",
        "options": [
            {"id": "A", "text": "Amazon Aurora"},
            {"id": "B", "text": "Amazon DynamoDB"},
            {"id": "C", "text": "Amazon Neptune"},
            {"id": "D", "text": "Amazon Redshift"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Aurora is a cloud-built relational database compatible with MySQL and "
                       "PostgreSQL, offering higher performance than the standard open-source engines.",
            "distractors": {
                "B": "DynamoDB is NoSQL key-value, not a MySQL/PostgreSQL-compatible relational "
                     "database.",
                "C": "Neptune is a graph database, not a MySQL/PostgreSQL-compatible relational "
                     "engine.",
                "D": "Redshift is an analytics data warehouse, not a drop-in MySQL/PostgreSQL "
                     "relational database.",
            },
            "exam_pattern": "'MySQL/PostgreSQL-compatible, cloud-optimized, high performance' -> Aurora.",
        },
        "references": ["Amazon Aurora"],
    },
    {
        "id": "clf-tech-026", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 3, "type": "mcq",
        "stem": "A developer needs a database optimized for highly connected data and relationship "
                "queries, such as a social graph. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon Neptune"},
            {"id": "B", "text": "Amazon RDS"},
            {"id": "C", "text": "Amazon DynamoDB"},
            {"id": "D", "text": "Amazon Redshift"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Neptune is a managed graph database purpose-built for highly connected "
                       "data and relationship (graph) queries like social networks.",
            "distractors": {
                "B": "RDS is a general relational database; modeling deep graph relationships is not "
                     "its strength.",
                "C": "DynamoDB is key-value/document NoSQL, not a graph database for relationship "
                     "traversal.",
                "D": "Redshift is an analytical data warehouse, not a graph database.",
            },
            "exam_pattern": "'Graph / highly connected data / relationships' -> Amazon Neptune.",
        },
        "references": ["Amazon Neptune (graph database)"],
    },

    # ===== networking_services ============================================
    {
        "id": "clf-tech-027", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 1, "type": "mcq",
        "stem": "A company wants a logically isolated section of the AWS cloud where it controls "
                "its own IP ranges, subnets, and routing. Which service?",
        "options": [
            {"id": "A", "text": "Amazon VPC"},
            {"id": "B", "text": "Amazon Route 53"},
            {"id": "C", "text": "AWS Direct Connect"},
            {"id": "D", "text": "Amazon CloudFront"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon VPC provides a logically isolated virtual network where you define IP "
                       "address ranges, subnets, route tables, and gateways.",
            "distractors": {
                "B": "Route 53 is a DNS service for routing domain names, not an isolated virtual "
                     "network.",
                "C": "Direct Connect is a dedicated private link from on-premises to AWS, not the "
                     "virtual network itself.",
                "D": "CloudFront is a content delivery network, not a private virtual network you "
                     "subnet and route.",
            },
            "exam_pattern": "'Isolated virtual network / own IP ranges, subnets, routing' -> Amazon VPC.",
        },
        "references": ["Amazon VPC"],
    },
    {
        "id": "clf-tech-028", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a stateful virtual firewall controlling inbound and "
                "outbound traffic at the individual EC2 instance level. Which should they use?",
        "options": [
            {"id": "A", "text": "A security group"},
            {"id": "B", "text": "A network ACL"},
            {"id": "C", "text": "An internet gateway"},
            {"id": "D", "text": "A route table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A security group is a stateful virtual firewall at the instance level: return "
                       "traffic for an allowed request is automatically permitted.",
            "distractors": {
                "B": "A network ACL is stateless and operates at the subnet level, not statefully at "
                     "the instance level.",
                "C": "An internet gateway connects a VPC to the internet; it does not filter traffic "
                     "like a firewall.",
                "D": "A route table directs where traffic goes; it does not allow or deny traffic as "
                     "a firewall.",
            },
            "exam_pattern": "Security group = stateful + instance level; network ACL = stateless + subnet level.",
        },
        "references": ["Amazon VPC security groups"],
    },
    {
        "id": "clf-tech-029", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 3, "type": "mcq",
        "stem": "A team needs stateless traffic filtering at the subnet boundary, supporting both "
                "explicit allow and deny rules. Which should they use?",
        "options": [
            {"id": "A", "text": "A network ACL"},
            {"id": "B", "text": "A security group"},
            {"id": "C", "text": "Amazon Route 53"},
            {"id": "D", "text": "AWS WAF"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A network ACL is stateless, acts at the subnet level, and supports both allow "
                       "and deny rules evaluated in order.",
            "distractors": {
                "B": "Security groups are stateful, operate at the instance level, and support allow "
                     "rules only (no explicit deny).",
                "C": "Route 53 is a DNS service; it does not filter packet traffic at a subnet "
                     "boundary.",
                "D": "AWS WAF filters web (HTTP/HTTPS) requests at the application layer, not "
                     "stateless subnet-level traffic.",
            },
            "exam_pattern": "'Stateless + subnet + allow AND deny rules' -> network ACL.",
        },
        "references": ["Amazon VPC network ACLs"],
    },
    {
        "id": "clf-tech-030", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 1, "type": "mcq",
        "stem": "A company wants to register a domain name and route users to its resources using "
                "DNS. Which AWS service provides this?",
        "options": [
            {"id": "A", "text": "Amazon Route 53"},
            {"id": "B", "text": "Amazon CloudFront"},
            {"id": "C", "text": "Amazon VPC"},
            {"id": "D", "text": "AWS Direct Connect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Route 53 is a scalable DNS web service that registers domains and "
                       "routes end users to applications by resolving names to resources.",
            "distractors": {
                "B": "CloudFront is a content delivery network; it caches content but is not the DNS "
                     "/ domain registration service.",
                "C": "VPC is a virtual network; it does not provide DNS domain registration and "
                     "routing on the internet.",
                "D": "Direct Connect provides a private physical link to AWS, not DNS resolution.",
            },
            "exam_pattern": "'DNS / domain registration / route users by name' -> Route 53.",
        },
        "references": ["Amazon Route 53"],
    },
    {
        "id": "clf-tech-031", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 2, "type": "mcq",
        "stem": "To deliver web content to global users with low latency by caching at edge "
                "locations, which service should a company use?",
        "options": [
            {"id": "A", "text": "Amazon CloudFront"},
            {"id": "B", "text": "Amazon Route 53"},
            {"id": "C", "text": "Amazon S3 Glacier"},
            {"id": "D", "text": "AWS Direct Connect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon CloudFront is a content delivery network (CDN) that caches content at "
                       "edge locations to serve global users with low latency.",
            "distractors": {
                "B": "Route 53 resolves DNS names; it does not cache and deliver content at the edge.",
                "C": "S3 Glacier is archival storage with slow retrieval, the opposite of a "
                     "low-latency CDN.",
                "D": "Direct Connect is a private on-premises link to AWS, not a global content "
                     "delivery network.",
            },
            "exam_pattern": "'CDN / cache content at edge for global low latency' -> CloudFront.",
        },
        "references": ["Amazon CloudFront (CDN)"],
    },
    {
        "id": "clf-tech-032", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise wants a dedicated, private physical link from its data center to AWS "
                "that avoids the public internet. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Direct Connect"},
            {"id": "B", "text": "AWS Site-to-Site VPN"},
            {"id": "C", "text": "An internet gateway"},
            {"id": "D", "text": "Amazon Route 53"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Direct Connect establishes a dedicated private physical connection from a "
                       "data center to AWS, bypassing the public internet for consistent performance.",
            "distractors": {
                "B": "Site-to-Site VPN is encrypted but runs OVER the public internet, so it is not "
                     "a dedicated private physical link.",
                "C": "An internet gateway connects a VPC to the public internet — the very thing the "
                     "enterprise wants to avoid.",
                "D": "Route 53 is DNS; it does not provide a private network connection to AWS.",
            },
            "exam_pattern": "'Dedicated private physical link, not over internet' -> Direct Connect; "
                            "'encrypted tunnel over internet' -> Site-to-Site VPN.",
        },
        "references": ["AWS Direct Connect vs Site-to-Site VPN"],
    },
    {
        "id": "clf-tech-033", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 2, "type": "mcq",
        "stem": "Instances in a private subnet need outbound internet access for updates, but no "
                "inbound connections from the internet. Which component enables this?",
        "options": [
            {"id": "A", "text": "A NAT gateway"},
            {"id": "B", "text": "An internet gateway attached directly to the instances"},
            {"id": "C", "text": "A security group"},
            {"id": "D", "text": "Amazon CloudFront"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A NAT gateway lets private-subnet instances initiate outbound traffic to the "
                       "internet while blocking unsolicited inbound connections from the internet.",
            "distractors": {
                "B": "An internet gateway provides internet access for public subnets; it does not "
                     "give private instances outbound-only access on its own.",
                "C": "A security group is a firewall that filters traffic; it does not provide the "
                     "address translation or internet path itself.",
                "D": "CloudFront delivers content to users; it is not how instances reach the "
                     "internet for outbound updates.",
            },
            "exam_pattern": "'Private subnet, outbound only, no inbound from internet' -> NAT gateway.",
        },
        "references": ["Amazon VPC NAT gateways"],
    },

    # ===== deployment_access ==============================================
    {
        "id": "clf-tech-034", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 1, "type": "mcq",
        "stem": "A new user wants to manage AWS resources through a point-and-click, web-based "
                "graphical interface. Which access method is this?",
        "options": [
            {"id": "A", "text": "AWS Management Console"},
            {"id": "B", "text": "AWS CLI"},
            {"id": "C", "text": "An AWS SDK"},
            {"id": "D", "text": "AWS CloudFormation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Management Console is the web-based graphical interface for managing "
                       "AWS resources by point and click.",
            "distractors": {
                "B": "The CLI is a command-line, text-based tool, not a graphical interface.",
                "C": "An SDK lets applications call AWS from code, not through a browser GUI.",
                "D": "CloudFormation provisions infrastructure from templates; it is not the "
                     "interactive web console.",
            },
            "exam_pattern": "'Web GUI / point and click' -> Management Console; 'terminal commands' -> "
                            "CLI; 'from application code' -> SDK.",
        },
        "references": ["AWS Management Console"],
    },
    {
        "id": "clf-tech-035", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants to automate AWS tasks from a terminal using scripted text "
                "commands. Which tool should they use?",
        "options": [
            {"id": "A", "text": "AWS CLI"},
            {"id": "B", "text": "AWS Management Console"},
            {"id": "C", "text": "AWS Trusted Advisor"},
            {"id": "D", "text": "Amazon CloudWatch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS CLI (command line interface) lets administrators run and script AWS "
                       "commands from a terminal to automate tasks.",
            "distractors": {
                "B": "The Management Console is a manual web GUI, not a scriptable command-line tool.",
                "C": "Trusted Advisor gives best-practice recommendations; it is not a command-line "
                     "automation tool.",
                "D": "CloudWatch is a monitoring service, not a terminal tool for running AWS "
                     "commands.",
            },
            "exam_pattern": "'Terminal / scripted commands / automate' -> AWS CLI.",
        },
        "references": ["AWS Command Line Interface (CLI)"],
    },
    {
        "id": "clf-tech-036", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to call AWS services directly from inside a Python application's "
                "code. Which option should they use?",
        "options": [
            {"id": "A", "text": "An AWS SDK"},
            {"id": "B", "text": "The AWS Management Console"},
            {"id": "C", "text": "AWS CloudFormation templates"},
            {"id": "D", "text": "AWS Config"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An AWS SDK provides language-specific libraries (e.g., for Python) so "
                       "applications can call AWS service APIs directly from code.",
            "distractors": {
                "B": "The Management Console is a manual web interface, not a code library called "
                     "from an application.",
                "C": "CloudFormation templates provision infrastructure; they are not how application "
                     "code calls services at runtime.",
                "D": "AWS Config records and evaluates resource configurations; it is not a "
                     "programming SDK.",
            },
            "exam_pattern": "'From application code / programming language' -> AWS SDK.",
        },
        "references": ["AWS SDKs"],
    },
    {
        "id": "clf-tech-037", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 3, "type": "mcq",
        "stem": "A team wants to define its entire AWS infrastructure as code in a template and "
                "deploy it repeatably. Which service provides this?",
        "options": [
            {"id": "A", "text": "AWS CloudFormation"},
            {"id": "B", "text": "AWS Elastic Beanstalk"},
            {"id": "C", "text": "The AWS CLI run manually each time"},
            {"id": "D", "text": "Amazon EC2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS CloudFormation is the infrastructure-as-code service: a template defines "
                       "resources that can be provisioned repeatably and consistently.",
            "distractors": {
                "B": "Elastic Beanstalk deploys and manages applications on a platform; it is not a "
                     "general infrastructure-as-code templating service.",
                "C": "Running CLI commands by hand is manual and error-prone, not a declarative "
                     "infrastructure-as-code template.",
                "D": "EC2 is a compute service; it does not define and deploy entire infrastructures "
                     "from a template.",
            },
            "exam_pattern": "'Infrastructure as code / template / repeatable provisioning' -> CloudFormation.",
        },
        "references": ["AWS CloudFormation (Infrastructure as Code)"],
    },
    {
        "id": "clf-tech-038", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 3, "type": "mcq",
        "stem": "A developer just wants to deploy and run a web app while AWS manages the platform "
                "underneath. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Elastic Beanstalk"},
            {"id": "B", "text": "AWS CloudFormation"},
            {"id": "C", "text": "AWS CLI"},
            {"id": "D", "text": "Amazon VPC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elastic Beanstalk focuses on the application: you provide the code and it "
                       "manages the platform, capacity, scaling, and health for you.",
            "distractors": {
                "B": "CloudFormation provisions and manages infrastructure from templates, but it "
                     "does not run and manage the application platform for you.",
                "C": "The CLI is a tool for issuing commands; it is not a managed application "
                     "platform.",
                "D": "VPC is a networking service, not a service that deploys and runs your "
                     "application.",
            },
            "exam_pattern": "'Deploy my app, AWS runs the platform' -> Elastic Beanstalk; "
                            "'provision any infrastructure from a template' -> CloudFormation.",
        },
        "references": ["AWS Elastic Beanstalk vs AWS CloudFormation"],
    },
    {
        "id": "clf-tech-039", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 1, "type": "mcq",
        "stem": "A team interacts with AWS through the Console, the CLI, and SDKs. Underneath, "
                "what do all three ultimately call?",
        "options": [
            {"id": "A", "text": "AWS service APIs"},
            {"id": "B", "text": "Physical servers the customer owns"},
            {"id": "C", "text": "An on-premises Active Directory"},
            {"id": "D", "text": "The AWS Marketplace catalog"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Console, CLI, and SDKs are all front ends that ultimately make calls to "
                       "the underlying AWS service APIs.",
            "distractors": {
                "B": "AWS resources run on AWS-managed infrastructure, not servers the customer owns; "
                     "the common layer is the API.",
                "C": "On-premises Active Directory is an identity directory, not what Console/CLI/SDK "
                     "calls to operate AWS.",
                "D": "The AWS Marketplace is a catalog of software to buy, not the API layer these "
                     "tools call.",
            },
            "exam_pattern": "Console/CLI/SDK are interfaces; they all converge on AWS service APIs.",
        },
        "references": ["AWS APIs (Console, CLI, SDK access)"],
    },

    # ===== other_services =================================================
    {
        "id": "clf-tech-040", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 2, "type": "mcq",
        "stem": "To decouple components, a team wants a managed queue that holds messages until a "
                "consumer processes them. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon SQS"},
            {"id": "B", "text": "Amazon SNS"},
            {"id": "C", "text": "Amazon CloudWatch"},
            {"id": "D", "text": "Amazon Kinesis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon SQS is a managed message queue that stores messages until a consumer "
                       "retrieves and processes them, decoupling producers from consumers.",
            "distractors": {
                "B": "SNS is pub/sub: it pushes messages to subscribers immediately rather than "
                     "holding them in a queue to be pulled.",
                "C": "CloudWatch is a monitoring service, not a message queue for decoupling.",
                "D": "Kinesis handles real-time streaming data, not the simple decoupling queue "
                     "described here.",
            },
            "exam_pattern": "'Queue / hold messages until processed / decouple' -> SQS; "
                            "'publish to many subscribers' -> SNS.",
        },
        "references": ["Amazon SQS"],
    },
    {
        "id": "clf-tech-041", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 2, "type": "mcq",
        "stem": "An application needs to publish one message and push it to many subscribers at "
                "once, such as email and queues. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon SNS"},
            {"id": "B", "text": "Amazon SQS"},
            {"id": "C", "text": "AWS CloudTrail"},
            {"id": "D", "text": "Amazon Athena"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon SNS is a pub/sub service that publishes a message once and pushes it "
                       "to many subscribers (email, SMS, queues, functions) at the same time.",
            "distractors": {
                "B": "SQS is a point-to-point queue that consumers poll; it does not fan out one "
                     "message to many subscriber types at once.",
                "C": "CloudTrail records API activity for auditing; it is not a messaging/pub-sub "
                     "service.",
                "D": "Athena queries data in S3 with SQL; it is not a notification/pub-sub service.",
            },
            "exam_pattern": "'Publish once, fan out to many subscribers' -> SNS (pub/sub).",
        },
        "references": ["Amazon SNS"],
    },
    {
        "id": "clf-tech-042", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 2, "type": "mcq",
        "stem": "An operations team wants to collect performance metrics, set alarms, and view "
                "dashboards for its AWS resources. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon CloudWatch"},
            {"id": "B", "text": "AWS CloudTrail"},
            {"id": "C", "text": "AWS Config"},
            {"id": "D", "text": "Amazon SNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon CloudWatch collects metrics and logs, triggers alarms, and powers "
                       "dashboards to monitor resource and application performance.",
            "distractors": {
                "B": "CloudTrail records who made which API calls for auditing; it is not the "
                     "performance metrics/alarms service.",
                "C": "AWS Config tracks resource configuration and compliance, not performance "
                     "metrics and alarms.",
                "D": "SNS sends notifications; it can deliver an alarm message but does not collect "
                     "metrics or build dashboards.",
            },
            "exam_pattern": "'Metrics / alarms / dashboards / performance monitoring' -> CloudWatch.",
        },
        "references": ["Amazon CloudWatch"],
    },
    {
        "id": "clf-tech-043", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 3, "type": "mcq",
        "stem": "A security auditor needs a record of who made which AWS API calls, and when, "
                "across the account. Which service provides this?",
        "options": [
            {"id": "A", "text": "AWS CloudTrail"},
            {"id": "B", "text": "Amazon CloudWatch"},
            {"id": "C", "text": "Amazon Inspector"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS CloudTrail records account activity and API calls — who did what and "
                       "when — providing the audit trail an auditor needs.",
            "distractors": {
                "B": "CloudWatch focuses on performance metrics and alarms, not an audit log of API "
                     "calls.",
                "C": "Inspector performs automated security vulnerability assessments; it is not the "
                     "account-wide API audit log.",
                "D": "Trusted Advisor gives best-practice recommendations, not a record of every API "
                     "call made.",
            },
            "exam_pattern": "'Who called which API, when / audit trail' -> CloudTrail (vs CloudWatch "
                            "for performance).",
        },
        "references": ["AWS CloudTrail"],
    },
    {
        "id": "clf-tech-044", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 3, "type": "mcq",
        "stem": "An analyst wants to run standard SQL queries directly on data stored in Amazon S3 "
                "without loading it elsewhere. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon Athena"},
            {"id": "B", "text": "Amazon Redshift"},
            {"id": "C", "text": "Amazon RDS"},
            {"id": "D", "text": "AWS Glue"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Athena is a serverless, interactive query service that runs standard "
                       "SQL directly against data in Amazon S3 with no servers to manage.",
            "distractors": {
                "B": "Redshift is a data warehouse; the classic pattern is to load data into it "
                     "rather than query S3 in place as Athena does.",
                "C": "RDS is a relational database you load and manage; it does not query S3 files "
                     "directly with SQL.",
                "D": "Glue is an ETL / data-catalog service for preparing data, not an interactive "
                     "SQL query engine over S3.",
            },
            "exam_pattern": "'Run SQL directly on S3, serverless, no loading' -> Amazon Athena.",
        },
        "references": ["Amazon Athena"],
    },
    {
        "id": "clf-tech-045", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 2, "type": "mcq",
        "stem": "A data science team wants one managed service to build, train, and deploy machine "
                "learning models. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon SageMaker"},
            {"id": "B", "text": "Amazon Rekognition"},
            {"id": "C", "text": "Amazon Comprehend"},
            {"id": "D", "text": "Amazon Polly"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon SageMaker is the managed service for building, training, and deploying "
                       "custom machine learning models end to end.",
            "distractors": {
                "B": "Rekognition is a pre-built AI service for image and video analysis, not a "
                     "platform for building your own models.",
                "C": "Comprehend is a pre-built natural-language-processing service for text "
                     "insights, not a model-building platform.",
                "D": "Polly is a pre-built text-to-speech service, not a service for building and "
                     "training custom ML models.",
            },
            "exam_pattern": "'Build/train/deploy your own ML models' -> SageMaker; named task (vision, "
                            "speech, text) -> a pre-built AI service.",
        },
        "references": ["Amazon SageMaker"],
    },
    {
        "id": "clf-tech-046", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 1, "type": "mcq",
        "stem": "A company wants to automatically detect objects and faces in uploaded images "
                "without building its own model. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon Rekognition"},
            {"id": "B", "text": "Amazon Polly"},
            {"id": "C", "text": "Amazon Translate"},
            {"id": "D", "text": "Amazon Transcribe"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon Rekognition is a pre-built AI service that analyzes images and video "
                       "to detect objects, scenes, and faces without custom model building.",
            "distractors": {
                "B": "Polly converts text into lifelike speech; it does not analyze images.",
                "C": "Translate converts text between languages; it does not perform image analysis.",
                "D": "Transcribe converts speech audio into text; it does not detect objects or faces "
                     "in images.",
            },
            "exam_pattern": "Match AI service to modality: images/video -> Rekognition, text-to-speech "
                            "-> Polly, translation -> Translate, speech-to-text -> Transcribe.",
        },
        "references": ["Amazon Rekognition"],
    },
]
