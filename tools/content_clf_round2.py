"""AWS Certified Cloud Practitioner (CLF-C02) — ROUND 2 expansion pool.

Deepens the existing verified CLF bank (round-1 = 152 items across
content_clf_concepts.py / _security.py / _technology.py / _billing.py) with
~48 NEW, original, non-duplicate items. Round-1 id prefixes are reused with an
"r2" segment (clf-cc-r2-*, clf-sec-r2-*, clf-tech-r2-*, clf-bill-r2-*) so ids
stay unique, and build_content's ``content_clf_*.py`` glob auto-merges this pool.

Design goals for round 2:
  * Go DEEPER than round-1 with NEW services and angles — cloud service/
    deployment models (IaaS/PaaS/SaaS, hybrid), the AWS Well-Architected Tool
    and its general design principles, more AWS CAF perspectives, the AWS Cloud
    Value Framework, current migration services (Migration Hub), governance
    (AWS Organizations SCPs, AWS Control Tower), IAM depth (MFA, explicit-deny
    evaluation, federation, authn vs authz), additional security services
    (Amazon Detective, Shield Standard vs Advanced, AWS Firewall Manager),
    global infrastructure (AWS Outposts, AWS Wavelength), compute (Amazon
    Lightsail, Amazon ECS, AMIs), storage (S3 Intelligent-Tiering, Amazon FSx,
    S3 durability), databases (RDS Multi-AZ vs Read Replicas), networking
    (AWS Transit Gateway, VPC endpoints), management/deployment (AWS Systems
    Manager, Infrastructure-as-Code), other services (Amazon EventBridge,
    Amazon Q), and billing/support (data-transfer pricing, "prices drop as AWS
    grows", AWS Compute Optimizer, consolidated-billing benefits, Enterprise
    Support Infrastructure Event Management, AWS Service Quotas).

Authoring rules match the round-1 pools: build_content.py shuffles option order
(seeded by id), so the authored answer key is not positionally biased; every
wrong option carries a distractor note; Cloud-Practitioner depth only (concepts,
purpose, when-to-use, who-manages-what) with no exact prices, limits, or
region-count trivia; current service names are used (Amazon Q, IAM Identity
Center, AWS Application Migration Service). Facts were grounded against AWS
documentation (docs.aws.amazon.com / aws.amazon.com) and each item cites the
CLF-C02 domain plus a relevant AWS doc. Never real or memorized exam items.
"""

QUESTIONS = [
    # ======================================================================
    # Domain 1 — Cloud Concepts (cloud_benefits, well_architected,
    # migration_caf, cloud_economics)
    # ======================================================================

    # ----- cloud_benefits (service & deployment models) -------------------
    {
        "id": "clf-cc-r2-001", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A company uses a ready-to-run email and calendar application over the internet. "
                "The vendor runs and maintains the entire stack, and the company just signs in and "
                "uses the features. Which cloud service model is this?",
        "options": [
            {"id": "A", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "B", "text": "Platform as a Service (PaaS)"},
            {"id": "C", "text": "Software as a Service (SaaS)"},
            {"id": "D", "text": "On-premises hosting"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Software as a Service delivers a complete, ready-to-use application over the "
                       "internet; the provider manages everything and the customer simply consumes "
                       "the software.",
            "distractors": {
                "A": "IaaS provides raw building blocks (virtual servers, storage, networking) that "
                     "the customer configures and manages — not a finished application.",
                "B": "PaaS provides a managed platform on which developers deploy their own code; "
                     "here no custom application is being built or deployed.",
                "D": "On-premises hosting means the company owns and runs the hardware and software "
                     "itself, the opposite of consuming a vendor-run application.",
            },
            "exam_pattern": "'Ready-to-use app, provider runs everything, just sign in' = SaaS; "
                            "'deploy my code on a managed platform' = PaaS; 'raw VMs/storage I "
                            "manage' = IaaS.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS - Types of Cloud Computing (IaaS, PaaS, SaaS)"],
    },
    {
        "id": "clf-cc-r2-002", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A bank keeps a legacy core system in its own data center while running new "
                "customer-facing applications on AWS, with the two environments connected. Which "
                "cloud deployment model is this?",
        "options": [
            {"id": "A", "text": "Cloud (all-in) deployment"},
            {"id": "B", "text": "Hybrid deployment"},
            {"id": "C", "text": "On-premises (private) deployment"},
            {"id": "D", "text": "Multi-Region deployment"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A hybrid deployment connects on-premises (or private) infrastructure with "
                       "cloud resources, letting a workload span both — common when a legacy system "
                       "stays on-premises while new parts run on AWS.",
            "distractors": {
                "A": "An all-in cloud deployment runs entirely on AWS with nothing left on-premises, "
                     "which is not the case here.",
                "C": "A purely on-premises/private deployment keeps everything in the company's own "
                     "data center and uses no public cloud.",
                "D": "Multi-Region describes spreading a workload across AWS Regions; it does not "
                     "describe mixing on-premises and cloud.",
            },
            "exam_pattern": "Deployment models: cloud (all-in), on-premises/private, and hybrid "
                            "(on-premises + cloud connected together).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS - Cloud Computing Deployment Models"],
    },
    {
        "id": "clf-cc-r2-003", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A cloud model provides fundamental building blocks — virtual compute, storage, and "
                "networking — that the customer configures and controls, including the operating "
                "system. Which service model is described?",
        "options": [
            {"id": "A", "text": "Software as a Service (SaaS)"},
            {"id": "B", "text": "Platform as a Service (PaaS)"},
            {"id": "C", "text": "Function as a Service only"},
            {"id": "D", "text": "Infrastructure as a Service (IaaS)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Infrastructure as a Service offers the basic building blocks of compute, "
                       "storage, and networking, giving the customer the most control and flexibility "
                       "— including over the operating system.",
            "distractors": {
                "A": "SaaS delivers a finished application; the customer does not configure the "
                     "operating system or infrastructure.",
                "B": "PaaS abstracts away the operating system and servers so developers focus on "
                     "code, so the customer does not control the OS.",
                "C": "'Function as a Service' (serverless functions) is a narrow category and removes "
                     "server/OS control rather than providing it.",
            },
            "exam_pattern": "'Basic building blocks, I control the OS, most flexibility' = IaaS "
                            "(highest control); SaaS = least control, fully managed app.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS - Types of Cloud Computing (IaaS)"],
    },

    # ----- well_architected (tool, design principles, pillar count) -------
    {
        "id": "clf-cc-r2-004", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "mcq",
        "stem": "A team wants a free, self-service tool in the AWS Management Console to review a "
                "workload against the six pillars and get a report of risks and improvement actions. "
                "Which should they use?",
        "options": [
            {"id": "A", "text": "AWS Well-Architected Tool"},
            {"id": "B", "text": "AWS Trusted Advisor"},
            {"id": "C", "text": "AWS Config"},
            {"id": "D", "text": "Amazon Inspector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Well-Architected Tool is a free console service that guides you "
                       "through the framework's questions, measures a workload against the pillars, "
                       "and produces a plan of improvement items.",
            "distractors": {
                "B": "Trusted Advisor runs automated best-practice checks across categories, but it "
                     "is not the structured Well-Architected pillar review of a workload.",
                "C": "AWS Config records and evaluates resource configurations against rules; it does "
                     "not perform a Well-Architected pillar review.",
                "D": "Amazon Inspector scans workloads for software vulnerabilities, not for "
                     "Well-Architected design alignment.",
            },
            "exam_pattern": "'Review a workload against the framework's pillars in the console' = AWS "
                            "Well-Architected Tool (the Framework is the guidance; the Tool runs the "
                            "review).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Well-Architected Tool"],
    },
    {
        "id": "clf-cc-r2-005", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are general design principles of the AWS Well-Architected "
                "Framework? (Choose two.)",
        "options": [
            {"id": "A", "text": "Stop guessing your capacity needs"},
            {"id": "B", "text": "Treat every server as a unique, long-lived 'pet'"},
            {"id": "C", "text": "Make frequent, small, reversible changes"},
            {"id": "D", "text": "Always scale a single server vertically before anything else"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "'Stop guessing capacity' and 'make frequent, small, reversible changes' are "
                       "both general design principles of the Well-Architected Framework, enabled by "
                       "the cloud's elasticity and automation.",
            "distractors": {
                "B": "Best practice treats servers as disposable and replaceable ('cattle'), not as "
                     "unique long-lived 'pets'.",
                "D": "The framework favors horizontal scaling (many smaller resources) over always "
                     "scaling one server vertically, which creates a single point of failure.",
            },
            "exam_pattern": "General design principles include: stop guessing capacity, test at "
                            "production scale, automate experimentation, allow evolutionary "
                            "architectures, drive decisions with data, and improve through game days.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Well-Architected Framework - General Design Principles"],
    },
    {
        "id": "clf-cc-r2-006", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 1, "type": "fill",
        "stem": "The AWS Well-Architected Framework organizes its best practices into a fixed number "
                "of pillars (Operational Excellence, Security, Reliability, Performance Efficiency, "
                "Cost Optimization, and Sustainability). How many pillars are there? Enter the number "
                "(digit or word).",
        "correct": ["6", "six"],
        "explanation": {
            "correct": "The AWS Well-Architected Framework has six pillars: Operational Excellence, "
                       "Security, Reliability, Performance Efficiency, Cost Optimization, and "
                       "Sustainability.",
            "distractors": {},
            "exam_pattern": "Six pillars (Sustainability was added in 2021) — do not confuse with the "
                            "six AWS Cloud Adoption Framework perspectives.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Well-Architected Framework (the six pillars)"],
    },

    # ----- migration_caf (CAF perspectives, Migration Hub) ----------------
    {
        "id": "clf-cc-r2-007", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "During a Cloud Adoption Framework assessment, leadership needs help managing and "
                "measuring cloud investments, controlling risk, and keeping a portfolio view of "
                "value. Which AWS CAF perspective most directly covers this?",
        "options": [
            {"id": "A", "text": "Platform"},
            {"id": "B", "text": "People"},
            {"id": "C", "text": "Governance"},
            {"id": "D", "text": "Operations"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Governance perspective helps orchestrate and manage cloud initiatives — "
                       "maximizing organizational value while managing risk through portfolio, "
                       "program, and performance management.",
            "distractors": {
                "A": "The Platform perspective focuses on building and modernizing a scalable, "
                     "hybrid cloud platform and its workloads, not governing investments and risk.",
                "B": "The People perspective addresses culture, skills, roles, and change management "
                     "for the workforce, not investment and risk governance.",
                "D": "The Operations perspective ensures cloud services are run and operated to meet "
                     "business needs, not the governing of investments and portfolio value.",
            },
            "exam_pattern": "Manage/measure investments, portfolio, and risk = Governance "
                            "perspective; skills/roles = People; run workloads = Operations.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Cloud Adoption Framework - Governance perspective"],
    },
    {
        "id": "clf-cc-r2-008", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "multi",
        "stem": "A study group must separate the AWS Cloud Adoption Framework (CAF) perspectives from "
                "the Well-Architected pillars. Which TWO of the following are CAF perspectives? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Governance"},
            {"id": "B", "text": "Operations"},
            {"id": "C", "text": "Reliability"},
            {"id": "D", "text": "Sustainability"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Governance and Operations are two of the six CAF perspectives (the others are "
                       "Business, People, Platform, and Security).",
            "distractors": {
                "C": "Reliability is a Well-Architected Framework pillar, not a CAF perspective.",
                "D": "Sustainability is a Well-Architected Framework pillar, not a CAF perspective.",
            },
            "exam_pattern": "CAF perspectives (organizational adoption): Business, People, "
                            "Governance, Platform, Security, Operations. WA pillars are a different "
                            "list — Reliability/Sustainability belong to the pillars.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Cloud Adoption Framework (the six perspectives)"],
    },
    {
        "id": "clf-cc-r2-009", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "A company is migrating dozens of applications using several AWS and partner tools and "
                "wants one place to discover its servers and track migration progress across them. "
                "Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Cost Explorer"},
            {"id": "B", "text": "AWS Migration Hub"},
            {"id": "C", "text": "AWS Config"},
            {"id": "D", "text": "Amazon CloudWatch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Migration Hub provides a single location to discover resources and track "
                       "the progress of application migrations across multiple AWS and partner "
                       "migration tools.",
            "distractors": {
                "A": "Cost Explorer analyzes and visualizes AWS spending; it does not track migration "
                     "progress.",
                "C": "AWS Config records and evaluates resource configurations; it is not a migration "
                     "tracking hub.",
                "D": "Amazon CloudWatch monitors metrics, logs, and alarms for running resources, not "
                     "the status of application migrations.",
            },
            "exam_pattern": "'Single pane to discover and track migration progress across tools' = "
                            "AWS Migration Hub.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Migration Hub"],
    },

    # ----- cloud_economics (consumption value, Cloud Value Framework) -----
    {
        "id": "clf-cc-r2-010", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "A retailer's demand peaks sharply each December and is low the rest of the year. "
                "Instead of owning servers sized for the December peak all year, it runs on AWS and "
                "pays for the capacity each month actually uses. Which cloud economic advantage is "
                "this?",
        "options": [
            {"id": "A", "text": "Benefiting from AWS's economies of scale"},
            {"id": "B", "text": "Meeting data-residency requirements"},
            {"id": "C", "text": "Higher data durability"},
            {"id": "D", "text": "A variable, consumption-based cost that avoids paying for peak "
                                 "capacity year-round"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The cloud's variable, consumption-based model lets the retailer scale with "
                       "demand and pay only for what it uses each period, instead of buying and "
                       "owning fixed peak capacity that sits idle most of the year.",
            "distractors": {
                "A": "Economies of scale is about AWS's lower unit prices from aggregated demand, not "
                     "about matching a single customer's spend to its own seasonal usage.",
                "B": "Data residency is about where data is stored to meet legal requirements, "
                     "unrelated to paying for seasonal capacity.",
                "C": "Data durability describes how safely data is stored against loss, not the cost "
                     "advantage of matching spend to seasonal demand.",
            },
            "exam_pattern": "'Pay for actual (seasonal/variable) usage instead of owning peak "
                            "capacity' = variable/consumption-based cost (elasticity economics).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS - Cloud economics (variable vs fixed cost)"],
    },
    {
        "id": "clf-cc-r2-011", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "AWS describes cloud value beyond raw infrastructure savings, including dimensions "
                "such as staff productivity, operational resilience, and business agility. A company "
                "reassigns administrators from patching and backups to building new product features. "
                "Which cloud value dimension does this represent?",
        "options": [
            {"id": "A", "text": "Staff productivity"},
            {"id": "B", "text": "Data residency"},
            {"id": "C", "text": "Reduced data durability"},
            {"id": "D", "text": "Economies of scale"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Freeing staff from undifferentiated operational tasks (patching, backups) so "
                       "they can focus on higher-value work is the staff-productivity dimension of "
                       "the AWS Cloud Value Framework.",
            "distractors": {
                "B": "Data residency concerns where data physically resides to meet legal rules, not "
                     "how staff time is redeployed.",
                "C": "Durability is about protecting stored data from loss; reducing it would be a "
                     "drawback, not a value dimension.",
                "D": "Economies of scale is AWS's provider-side pricing advantage, not the "
                     "redeployment of a customer's staff to value-adding work.",
            },
            "exam_pattern": "Cloud Value Framework dimensions: cost savings, staff productivity, "
                            "operational resilience, business agility — 'staff do value work instead "
                            "of ops chores' = staff productivity.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS Cloud Value Framework"],
    },
    {
        "id": "clf-cc-r2-012", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 1, "type": "fill",
        "stem": "Because AWS aggregates usage across hundreds of thousands of customers, it operates "
                "at lower per-unit cost and passes the savings on as lower prices. This cost "
                "advantage is called economies of ______. Enter the missing word.",
        "correct": ["scale"],
        "explanation": {
            "correct": "Economies of scale: higher aggregate usage lets AWS achieve lower unit costs "
                       "and offer lower pay-as-you-go prices than a single organization could reach "
                       "on its own.",
            "distractors": {},
            "exam_pattern": "'Lower unit prices because the provider operates at massive scale' = "
                            "economies of scale.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 1: Cloud Concepts)",
                       "AWS - Six Advantages of Cloud Computing (economies of scale)"],
    },

    # ======================================================================
    # Domain 2 — Security and Compliance (shared_responsibility,
    # compliance_governance, iam, security_services)
    # ======================================================================

    # ----- shared_responsibility ------------------------------------------
    {
        "id": "clf-sec-r2-001", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "mcq",
        "stem": "A company stores files in Amazon S3. Under the Shared Responsibility Model, which of "
                "the following is the CUSTOMER'S responsibility?",
        "options": [
            {"id": "A", "text": "Maintaining the physical storage media in the data center"},
            {"id": "B", "text": "Ensuring the durability of the underlying storage infrastructure"},
            {"id": "C", "text": "Configuring bucket permissions and access controls so data is not "
                                 "unintentionally exposed"},
            {"id": "D", "text": "Securely decommissioning failed disks"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "AWS secures the S3 infrastructure, but the customer configures bucket "
                       "policies, access controls, and settings (such as Block Public Access) to "
                       "control who can reach the data — 'security IN the cloud.'",
            "distractors": {
                "A": "Maintaining physical storage media is AWS's responsibility (security OF the "
                     "cloud).",
                "B": "The durability of the underlying S3 infrastructure is provided and managed by "
                     "AWS.",
                "D": "Secure disposal of failed hardware is handled by AWS.",
            },
            "exam_pattern": "For managed storage like S3, the customer owns data and access "
                            "configuration; AWS owns the physical infrastructure and durability.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-r2-002", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 3, "type": "mcq",
        "stem": "How does the division of responsibility change as a customer moves from Amazon EC2 "
                "(IaaS) to more fully managed services such as Amazon S3 or Amazon DynamoDB?",
        "options": [
            {"id": "A", "text": "Responsibility is identical for every AWS service"},
            {"id": "B", "text": "The customer must patch the operating system even for fully managed "
                                 "services"},
            {"id": "C", "text": "AWS becomes responsible for the customer's data classification"},
            {"id": "D", "text": "AWS takes on more of the operational responsibility, and the "
                                 "customer focuses mainly on data and access management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The more managed/abstracted the service, the more AWS handles (OS, patching, "
                       "underlying infrastructure); the customer's responsibilities shrink toward "
                       "managing their data and controlling access.",
            "distractors": {
                "A": "Responsibility is not identical — it shifts by service type (IaaS vs. managed "
                     "vs. serverless).",
                "B": "For fully managed services AWS patches the operating system; the customer does "
                     "not.",
                "C": "Data classification and ownership always remain the customer's responsibility, "
                     "regardless of service.",
            },
            "exam_pattern": "More managed service = more AWS responsibility; the customer always "
                            "keeps data and access (identity) responsibilities.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-r2-003", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are AWS responsibilities ('security OF the cloud') under "
                "the Shared Responsibility Model? (Choose two.)",
        "options": [
            {"id": "A", "text": "Maintaining the hypervisor and virtualization layer"},
            {"id": "B", "text": "Physical and environmental controls (power, cooling) of the data "
                                 "centers"},
            {"id": "C", "text": "Configuring IAM users, groups, and policies"},
            {"id": "D", "text": "Classifying and encrypting the customer's own data"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "AWS operates and secures the global infrastructure — including the "
                       "virtualization/hypervisor layer and data-center physical and environmental "
                       "controls — as 'security OF the cloud.'",
            "distractors": {
                "C": "Configuring IAM identities and policies is the customer's responsibility "
                     "('security IN the cloud').",
                "D": "Classifying and encrypting one's own data is always a customer responsibility.",
            },
            "exam_pattern": "AWS owns the infrastructure layers (hardware, facilities, hypervisor); "
                            "the customer owns identity, configuration, and data.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Shared Responsibility Model"],
    },

    # ----- compliance_governance (Organizations/SCP, Control Tower, data ownership) -----
    {
        "id": "clf-sec-r2-004", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "A company with many AWS accounts under AWS Organizations wants to centrally set "
                "guardrails that prevent member accounts from using disallowed services, no matter "
                "what their IAM policies say. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Individual IAM policies in each account only"},
            {"id": "B", "text": "Service control policies (SCPs) in AWS Organizations"},
            {"id": "C", "text": "AWS Security Hub"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Service control policies in AWS Organizations set the maximum available "
                       "permissions (guardrails) for member accounts; even an account's own IAM "
                       "allow cannot exceed what an SCP permits.",
            "distractors": {
                "A": "IAM policies grant permissions within one account but cannot centrally cap what "
                     "all member accounts are allowed to do.",
                "C": "AWS Security Hub aggregates and prioritizes security findings; it does not "
                     "enforce account-wide permission guardrails.",
                "D": "Trusted Advisor gives best-practice recommendations; it does not restrict which "
                     "services accounts may use.",
            },
            "exam_pattern": "'Central guardrails capping what member accounts can do across an "
                            "organization' = SCPs in AWS Organizations.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Organizations - Service Control Policies (SCPs)"],
    },
    {
        "id": "clf-sec-r2-005", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 3, "type": "mcq",
        "stem": "A company wants an automated way to set up and govern a secure, compliant "
                "multi-account environment (a 'landing zone') with pre-packaged guardrails and "
                "standardized account provisioning. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Control Tower"},
            {"id": "B", "text": "AWS Config alone"},
            {"id": "C", "text": "AWS CloudFormation alone"},
            {"id": "D", "text": "Amazon Inspector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Control Tower automates setup of a well-architected, multi-account "
                       "landing zone on top of AWS Organizations, applying preventive and detective "
                       "guardrails and standardizing account provisioning.",
            "distractors": {
                "B": "AWS Config evaluates resource configurations and can act as a detective "
                     "control, but it does not set up and govern a full multi-account landing zone by "
                     "itself.",
                "C": "CloudFormation provisions infrastructure from templates but does not provide "
                     "the managed landing zone, guardrails, and account factory that Control Tower "
                     "does.",
                "D": "Amazon Inspector performs vulnerability assessments, unrelated to landing-zone "
                     "governance.",
            },
            "exam_pattern": "'Set up and govern a secure multi-account landing zone with guardrails' "
                            "= AWS Control Tower (built on AWS Organizations).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Control Tower"],
    },
    {
        "id": "clf-sec-r2-006", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 1, "type": "mcq",
        "stem": "A customer asks who owns and controls the content (data) they store in AWS. Which "
                "statement is correct?",
        "options": [
            {"id": "A", "text": "AWS owns the data once it is uploaded to the cloud"},
            {"id": "B", "text": "Ownership is automatically shared equally between AWS and the "
                                 "customer"},
            {"id": "C", "text": "The customer retains ownership and control of their content and "
                                 "chooses which Region and services store it"},
            {"id": "D", "text": "A third-party auditor owns the data for compliance purposes"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Customers retain ownership and control of their content: they choose the "
                       "Region and services used, who can access it, and how it is secured and "
                       "encrypted.",
            "distractors": {
                "A": "AWS does not take ownership of customer content; the customer keeps it.",
                "B": "Ownership is not shared with AWS; the customer owns their data.",
                "D": "Auditors verify controls; they do not own the customer's data.",
            },
            "exam_pattern": "Customers always own and control their own data in AWS — this underpins "
                            "data residency and privacy choices.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Data Privacy / Shared Responsibility Model"],
    },

    # ----- iam (MFA, explicit deny, federation, authn vs authz) -----------
    {
        "id": "clf-sec-r2-007", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "What security benefit does enabling multi-factor authentication (MFA) on an AWS "
                "sign-in provide?",
        "options": [
            {"id": "A", "text": "It encrypts all of the account's data at rest automatically"},
            {"id": "B", "text": "It removes the need for any password"},
            {"id": "C", "text": "It provides automatic DDoS protection"},
            {"id": "D", "text": "It requires a second authentication factor in addition to the "
                                 "password, so a stolen password alone is not enough to sign in"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "MFA adds a second factor (for example, a one-time code from a device) on top "
                       "of the password, so an attacker who steals only the password still cannot "
                       "sign in.",
            "distractors": {
                "A": "MFA controls sign-in; it does not encrypt stored data — that is handled by "
                     "services such as AWS KMS.",
                "B": "MFA supplements the password with a second factor; it does not eliminate the "
                     "password.",
                "C": "DDoS protection is provided by AWS Shield, not by MFA.",
            },
            "exam_pattern": "MFA = 'something you know (password) + something you have (device code)'; "
                            "protects even if the password leaks.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS IAM - Multi-Factor Authentication (MFA)"],
    },
    {
        "id": "clf-sec-r2-008", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 3, "type": "mcq",
        "stem": "A user belongs to a group whose policy allows Amazon S3 access, but another policy "
                "attached to the user contains an explicit Deny for a specific bucket. What is the "
                "result for that bucket?",
        "options": [
            {"id": "A", "text": "The most recently attached policy always wins"},
            {"id": "B", "text": "Access is denied, because an explicit deny overrides any allow"},
            {"id": "C", "text": "Access is allowed, because an allow overrides a deny"},
            {"id": "D", "text": "Only the account root user can override the deny for that user"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In IAM policy evaluation, an explicit Deny always overrides any Allow, so the "
                       "user is denied access to that specific bucket regardless of the group's "
                       "allow.",
            "distractors": {
                "A": "Policy evaluation is not based on which policy was attached most recently; an "
                     "explicit deny wins regardless of order.",
                "C": "An allow does not override an explicit deny — the deny takes precedence.",
                "D": "The outcome is determined by policy evaluation logic; the root user is not "
                     "required to 'override' it, and this is not how evaluation works.",
            },
            "exam_pattern": "IAM evaluation rule: default deny, an Allow grants access, and an "
                            "explicit Deny overrides everything.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS IAM - Policy Evaluation Logic (explicit deny)"],
    },
    {
        "id": "clf-sec-r2-009", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "A company wants employees who already have corporate identities in its existing "
                "identity provider to access AWS using temporary credentials, without creating a "
                "separate IAM user for each person. Which approach supports this?",
        "options": [
            {"id": "A", "text": "Identity federation, where external identities assume an IAM role "
                                 "for temporary credentials"},
            {"id": "B", "text": "Creating one IAM user per employee and sharing passwords"},
            {"id": "C", "text": "Sharing the account root user credentials with the team"},
            {"id": "D", "text": "Embedding long-term access keys in each employee's laptop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Identity federation lets users authenticate with an existing identity "
                       "provider and assume an IAM role to receive temporary AWS credentials, so no "
                       "per-user IAM identity is required (often via AWS IAM Identity Center).",
            "distractors": {
                "B": "Creating an IAM user per employee defeats the goal of reusing existing "
                     "identities, and sharing passwords is insecure.",
                "C": "Sharing root credentials is a severe security risk and is never recommended.",
                "D": "Embedding long-term access keys is insecure and hard to rotate; federation "
                     "provides short-lived credentials instead.",
            },
            "exam_pattern": "'Reuse existing corporate identities for AWS with temporary "
                            "credentials' = identity federation using IAM roles (IAM Identity "
                            "Center).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS IAM - Identity Federation and Roles"],
    },
    {
        "id": "clf-sec-r2-010", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 1, "type": "mcq",
        "stem": "In AWS Identity and Access Management, what is the difference between authentication "
                "and authorization?",
        "options": [
            {"id": "A", "text": "They are the same thing with two names"},
            {"id": "B", "text": "Authentication decides what actions you may perform; authorization "
                                 "proves who you are"},
            {"id": "C", "text": "Authentication verifies who you are (identity); authorization "
                                 "determines what you are allowed to do (permissions)"},
            {"id": "D", "text": "Both only apply to the account root user"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Authentication confirms identity (who you are, e.g., via password/MFA or "
                       "access keys); authorization then determines which actions and resources that "
                       "identity is permitted to use, via IAM policies.",
            "distractors": {
                "A": "They are distinct steps: proving identity versus granting permissions.",
                "B": "This reverses the definitions — authentication proves identity, authorization "
                     "grants permissions.",
                "D": "Both concepts apply to all IAM identities (users, roles), not just the root "
                     "user.",
            },
            "exam_pattern": "Authentication = who you are; authorization = what you can do.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS IAM - Authentication and Authorization"],
    },

    # ----- security_services (Detective, Shield tiers, Firewall Manager, KMS) -----
    {
        "id": "clf-sec-r2-011", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 3, "type": "mcq",
        "stem": "After a threat-detection service raises a finding, a security team wants to analyze "
                "logs and visualize relationships to investigate the root cause of the suspicious "
                "activity. Which service is purpose-built for this investigation step?",
        "options": [
            {"id": "A", "text": "Amazon Inspector"},
            {"id": "B", "text": "Amazon Detective"},
            {"id": "C", "text": "Amazon Macie"},
            {"id": "D", "text": "AWS WAF"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Amazon Detective automatically collects and correlates log data (such as "
                       "CloudTrail, VPC Flow Logs, and GuardDuty findings) and builds visualizations "
                       "to help analyze and determine the root cause of security findings.",
            "distractors": {
                "A": "Amazon Inspector performs automated vulnerability assessments of workloads, not "
                     "root-cause investigation of findings.",
                "C": "Amazon Macie discovers and classifies sensitive data in Amazon S3, not security "
                     "investigations.",
                "D": "AWS WAF filters malicious web requests; it is not an investigation tool.",
            },
            "exam_pattern": "GuardDuty = detect; Amazon Detective = investigate/root-cause analysis "
                            "of findings.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "Amazon Detective"],
    },
    {
        "id": "clf-sec-r2-012", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly describes AWS Shield Standard versus AWS Shield Advanced?",
        "options": [
            {"id": "A", "text": "Shield Standard is automatically included for all AWS customers at "
                                 "no additional cost for common network and transport layer DDoS "
                                 "protection; Shield Advanced is a paid tier with enhanced protection"},
            {"id": "B", "text": "Both tiers are paid add-ons that must be purchased before any DDoS "
                                 "protection applies"},
            {"id": "C", "text": "Shield Standard filters SQL injection and cross-site scripting at "
                                 "the application layer"},
            {"id": "D", "text": "Shield Advanced is the free default and Shield Standard is the paid "
                                 "upgrade"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Shield Standard is automatic and free for all customers, defending "
                       "against common network/transport-layer DDoS attacks; Shield Advanced is a "
                       "paid tier adding enhanced detection, DDoS response team access, and cost "
                       "protection.",
            "distractors": {
                "B": "Shield Standard is free and always on; DDoS protection is not entirely "
                     "pay-to-enable.",
                "C": "Filtering SQL injection and cross-site scripting is the job of AWS WAF, not "
                     "Shield Standard.",
                "D": "This reverses the tiers — Standard is the free default, Advanced is the paid "
                     "upgrade.",
            },
            "exam_pattern": "Shield Standard = free, automatic, common DDoS; Shield Advanced = paid, "
                            "enhanced, response team + cost protection.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Shield (Standard and Advanced)"],
    },
    {
        "id": "clf-sec-r2-013", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 3, "type": "mcq",
        "stem": "A security team wants to configure and centrally enforce firewall rules — such as "
                "AWS WAF rules and AWS Shield Advanced protections — once and have them applied "
                "consistently across many accounts in AWS Organizations, including new resources. "
                "Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS WAF used individually in each account"},
            {"id": "B", "text": "AWS Network Firewall used in a single VPC"},
            {"id": "C", "text": "AWS Security Hub"},
            {"id": "D", "text": "AWS Firewall Manager"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "AWS Firewall Manager centrally configures and manages firewall rules (AWS "
                       "WAF, AWS Shield Advanced, security groups, AWS Network Firewall, Route 53 "
                       "Resolver DNS Firewall) across accounts and resources in an organization, "
                       "including newly created ones.",
            "distractors": {
                "A": "Configuring AWS WAF separately in each account does not provide central, "
                     "organization-wide enforcement across accounts.",
                "B": "AWS Network Firewall protects traffic in a VPC; it is not the cross-account "
                     "central policy manager.",
                "C": "AWS Security Hub aggregates and prioritizes findings; it does not centrally "
                     "deploy and enforce firewall rules.",
            },
            "exam_pattern": "'Centrally manage WAF/Shield/firewall rules across many accounts in an "
                            "organization' = AWS Firewall Manager.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Firewall Manager"],
    },
    {
        "id": "clf-sec-r2-014", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "multi",
        "stem": "A company encrypts data at rest in Amazon S3 using AWS Key Management Service (AWS "
                "KMS). Which TWO statements are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "AWS KMS integrates with many AWS services to encrypt data at rest"},
            {"id": "B", "text": "Amazon Macie stores and manages the account's encryption keys"},
            {"id": "C", "text": "AWS KMS key usage can be logged in AWS CloudTrail for auditing"},
            {"id": "D", "text": "Objects in Amazon S3 cannot be encrypted at rest"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "AWS KMS is integrated with many AWS services to encrypt data at rest, and "
                       "KMS key usage (such as encrypt/decrypt calls) can be recorded in AWS "
                       "CloudTrail for auditing.",
            "distractors": {
                "B": "Amazon Macie discovers and classifies sensitive data; it does not store or "
                     "manage encryption keys (that is AWS KMS).",
                "D": "Amazon S3 fully supports encryption of objects at rest, including with AWS "
                     "KMS-managed keys.",
            },
            "exam_pattern": "KMS = manage keys + encrypt-at-rest integration; key usage is auditable "
                            "via CloudTrail.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 2: Security and Compliance)",
                       "AWS Key Management Service (KMS)"],
    },

    # ======================================================================
    # Domain 3 — Cloud Technology and Services (global_infrastructure,
    # compute_services, storage_services, database_services,
    # networking_services, deployment_access, other_services)
    # ======================================================================

    # ----- global_infrastructure (Outposts, Wavelength) ------------------
    {
        "id": "clf-tech-r2-001", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 2, "type": "mcq",
        "stem": "A manufacturer must keep certain workloads physically inside its own factory for "
                "data residency and low-latency control, but wants to use AWS services and APIs with "
                "AWS-managed hardware on-site. Which option fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Local Zones"},
            {"id": "B", "text": "AWS Outposts"},
            {"id": "C", "text": "AWS Direct Connect"},
            {"id": "D", "text": "Amazon CloudFront"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Outposts brings AWS-managed infrastructure, services, and APIs to the "
                       "customer's own data center or facility, supporting on-premises data residency "
                       "and low-latency local processing while staying consistent with AWS.",
            "distractors": {
                "A": "Local Zones place AWS infrastructure in large metro areas (operated by AWS), "
                     "not inside the customer's own facility.",
                "C": "Direct Connect is a private network link to an AWS Region; it does not place "
                     "compute on-premises.",
                "D": "CloudFront caches content at edge locations for delivery; it does not run "
                     "workloads inside a customer facility.",
            },
            "exam_pattern": "'AWS hardware/services inside MY own data center/facility' = AWS "
                            "Outposts; 'AWS compute in a nearby metro' = Local Zones.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "AWS Outposts"],
    },
    {
        "id": "clf-tech-r2-002", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "global_infrastructure", "difficulty": 3, "type": "mcq",
        "stem": "A developer building an app for 5G mobile users needs ultra-low latency by placing "
                "compute and storage inside telecommunications providers' 5G networks, at the mobile "
                "edge. Which AWS offering is designed for this?",
        "options": [
            {"id": "A", "text": "AWS Wavelength"},
            {"id": "B", "text": "AWS Local Zones"},
            {"id": "C", "text": "Amazon Route 53"},
            {"id": "D", "text": "AWS Global Accelerator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Wavelength embeds AWS compute and storage within communications "
                       "providers' 5G networks, so traffic from mobile devices reaches the "
                       "application without leaving the carrier network — minimizing latency for 5G "
                       "users.",
            "distractors": {
                "B": "Local Zones reduce latency for users in a metropolitan area but are not "
                     "embedded in carriers' 5G networks for mobile-edge use.",
                "C": "Route 53 is a DNS service; it does not place compute at the 5G mobile edge.",
                "D": "Global Accelerator improves availability and routing over the AWS network, but "
                     "it does not run compute inside carrier 5G networks.",
            },
            "exam_pattern": "'Ultra-low latency for 5G/mobile users, compute inside the carrier "
                            "network' = AWS Wavelength.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "AWS Wavelength"],
    },

    # ----- compute_services (Lightsail, ECS, AMI) -------------------------
    {
        "id": "clf-tech-r2-003", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 1, "type": "mcq",
        "stem": "A small business wants the easiest way to launch a simple WordPress website with a "
                "preconfigured bundle and low, predictable monthly pricing, without configuring "
                "individual AWS resources. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon EC2 configured manually"},
            {"id": "B", "text": "AWS Fargate"},
            {"id": "C", "text": "Amazon Lightsail"},
            {"id": "D", "text": "AWS Elastic Beanstalk"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Amazon Lightsail is an easy-to-use virtual private server offering "
                       "preconfigured blueprints (such as WordPress) and bundled, predictable monthly "
                       "pricing — ideal for simple websites and applications.",
            "distractors": {
                "A": "Manually configured EC2 requires choosing and wiring up many resources, which "
                     "is more complex than the simple bundle requested.",
                "B": "Fargate runs containers serverlessly; it is not a simple preconfigured website "
                     "bundle with fixed monthly pricing.",
                "D": "Elastic Beanstalk deploys and manages applications but is aimed at developers "
                     "deploying their own code, not the simplest preconfigured website bundle.",
            },
            "exam_pattern": "'Simplest VPS, preconfigured blueprint (WordPress), predictable monthly "
                            "price' = Amazon Lightsail.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon Lightsail"],
    },
    {
        "id": "clf-tech-r2-004", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "A team wants a fully managed AWS-native container orchestration service to run and "
                "scale Docker containers, and does not require Kubernetes. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon EKS"},
            {"id": "B", "text": "Amazon ECS"},
            {"id": "C", "text": "AWS Lambda"},
            {"id": "D", "text": "Amazon EC2 Auto Scaling"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Amazon ECS (Elastic Container Service) is AWS's own fully managed container "
                       "orchestration service for running and scaling containers without requiring "
                       "Kubernetes.",
            "distractors": {
                "A": "Amazon EKS is the managed Kubernetes service — appropriate when you specifically "
                     "want Kubernetes, which this team does not.",
                "C": "AWS Lambda runs event-driven functions, not long-running orchestrated "
                     "containers.",
                "D": "EC2 Auto Scaling adjusts the number of EC2 instances; it is not a container "
                     "orchestrator.",
            },
            "exam_pattern": "'AWS-native container orchestration, no Kubernetes needed' = Amazon ECS; "
                            "'managed Kubernetes' = Amazon EKS.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon Elastic Container Service (ECS)"],
    },
    {
        "id": "clf-tech-r2-005", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "compute_services", "difficulty": 2, "type": "mcq",
        "stem": "When launching Amazon EC2 instances, what does an Amazon Machine Image (AMI) "
                "provide?",
        "options": [
            {"id": "A", "text": "A billing discount for long-term commitments"},
            {"id": "B", "text": "A load balancer for distributing traffic"},
            {"id": "C", "text": "A virtual network with subnets and routing"},
            {"id": "D", "text": "A template containing the operating system and configuration used "
                                 "to launch instances"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An AMI is a template that includes the operating system, and optionally "
                       "software and configuration, used to launch EC2 instances — enabling "
                       "consistent, repeatable instance creation.",
            "distractors": {
                "A": "Billing discounts come from Reserved Instances or Savings Plans, not from an "
                     "AMI.",
                "B": "Distributing traffic is the job of Elastic Load Balancing, not an AMI.",
                "C": "A virtual network with subnets and routing is an Amazon VPC, not an AMI.",
            },
            "exam_pattern": "AMI = the OS/software template an EC2 instance is launched from.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon EC2 - Amazon Machine Images (AMI)"],
    },

    # ----- storage_services (Intelligent-Tiering, FSx, S3 durability) -----
    {
        "id": "clf-tech-r2-006", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "A company stores data in Amazon S3 whose access patterns are unknown and change over "
                "time. It wants storage costs optimized automatically as objects move between frequent "
                "and infrequent access, without retrieval fees or operational effort. Which S3 "
                "storage class fits BEST?",
        "options": [
            {"id": "A", "text": "S3 Intelligent-Tiering"},
            {"id": "B", "text": "S3 Standard-Infrequent Access"},
            {"id": "C", "text": "S3 Glacier Deep Archive"},
            {"id": "D", "text": "Amazon EBS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "S3 Intelligent-Tiering automatically moves objects between access tiers based "
                       "on changing usage, optimizing cost with no retrieval fees — ideal when access "
                       "patterns are unknown or unpredictable.",
            "distractors": {
                "B": "Standard-IA suits data with known, predictable infrequent access, and it "
                     "charges retrieval fees; it does not auto-tier.",
                "C": "Glacier Deep Archive is the lowest-cost archive for rarely accessed data with "
                     "slow (hours) retrieval, not unpredictable access needing millisecond reads.",
                "D": "Amazon EBS is block storage for EC2, not an S3 storage class.",
            },
            "exam_pattern": "'Unknown/changing access patterns + automatic cost optimization, no "
                            "retrieval fees' = S3 Intelligent-Tiering.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon S3 Intelligent-Tiering storage class"],
    },
    {
        "id": "clf-tech-r2-007", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 2, "type": "mcq",
        "stem": "A company's Windows-based applications need fully managed shared file storage that "
                "supports the SMB protocol and native Windows features. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon EFS"},
            {"id": "B", "text": "Amazon S3"},
            {"id": "C", "text": "Amazon FSx for Windows File Server"},
            {"id": "D", "text": "Amazon EBS"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Amazon FSx for Windows File Server provides fully managed shared file storage "
                       "built on Windows Server, supporting the SMB protocol and native Windows file "
                       "system features.",
            "distractors": {
                "A": "Amazon EFS is a shared file system for Linux instances using NFS, not Windows "
                     "SMB shares.",
                "B": "Amazon S3 is object storage accessed via an API, not an SMB file share.",
                "D": "Amazon EBS is single-instance block storage, not a shared SMB file system.",
            },
            "exam_pattern": "'Windows / SMB shared file system' = Amazon FSx for Windows File Server; "
                            "'Linux / NFS shared file system' = Amazon EFS.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon FSx for Windows File Server"],
    },
    {
        "id": "clf-tech-r2-008", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "storage_services", "difficulty": 1, "type": "mcq",
        "stem": "Which statement about the durability of data stored in Amazon S3 Standard is "
                "correct?",
        "options": [
            {"id": "A", "text": "S3 stores each object in only one Availability Zone"},
            {"id": "B", "text": "S3 automatically stores data redundantly across multiple "
                                 "Availability Zones within a Region for high durability"},
            {"id": "C", "text": "Customers must manually copy objects between AZs to avoid data loss"},
            {"id": "D", "text": "Durability requires moving data to S3 Glacier first"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "S3 Standard automatically and redundantly stores objects across multiple "
                       "Availability Zones in a Region, giving very high durability without customer "
                       "effort.",
            "distractors": {
                "A": "S3 Standard spans multiple AZs; single-AZ storage is a specific class (S3 One "
                     "Zone-IA), not the default behavior.",
                "C": "S3 handles redundancy automatically; customers do not manually copy objects "
                     "between AZs for durability.",
                "D": "High durability is inherent to S3; it does not require first moving data to "
                     "Glacier.",
            },
            "exam_pattern": "S3 durability comes from automatic redundant storage across multiple AZs "
                            "in a Region.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon S3 (data durability and availability)"],
    },

    # ----- database_services (RDS Multi-AZ vs Read Replicas) --------------
    {
        "id": "clf-tech-r2-009", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 2, "type": "mcq",
        "stem": "A company runs a production database on Amazon RDS and needs automatic failover to a "
                "standby copy in another Availability Zone if the primary fails, to maximize "
                "availability. Which RDS feature should it enable?",
        "options": [
            {"id": "A", "text": "A Multi-AZ deployment"},
            {"id": "B", "text": "A read replica"},
            {"id": "C", "text": "A single-AZ deployment with a larger instance"},
            {"id": "D", "text": "Amazon DynamoDB global tables"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An RDS Multi-AZ deployment maintains a synchronous standby in a different "
                       "Availability Zone and fails over to it automatically if the primary becomes "
                       "unavailable — this targets high availability.",
            "distractors": {
                "B": "Read replicas are for scaling read traffic (asynchronous copies); they are not "
                     "the primary mechanism for automatic failover.",
                "C": "A larger single-AZ instance still fails entirely if that AZ goes down — no "
                     "automatic failover.",
                "D": "DynamoDB global tables apply to DynamoDB, not to an Amazon RDS high-availability "
                     "deployment.",
            },
            "exam_pattern": "'Automatic failover to a standby in another AZ / high availability' = RDS "
                            "Multi-AZ; 'scale reads' = read replicas.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon RDS Multi-AZ deployments"],
    },
    {
        "id": "clf-tech-r2-010", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "database_services", "difficulty": 2, "type": "mcq",
        "stem": "An application's database is overwhelmed by heavy read traffic from reporting "
                "queries. The team wants to offload reads to additional copies of the database to "
                "improve read performance. Which Amazon RDS feature fits BEST?",
        "options": [
            {"id": "A", "text": "A Multi-AZ standby instance"},
            {"id": "B", "text": "Amazon ElastiCache only"},
            {"id": "C", "text": "Vertically scaling to the largest instance and nothing else"},
            {"id": "D", "text": "Read replicas"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "RDS read replicas are additional read-only copies that serve read traffic, "
                       "offloading the primary and improving read scalability for read-heavy "
                       "workloads.",
            "distractors": {
                "A": "A Multi-AZ standby is for failover/high availability; the standby does not "
                     "serve application read traffic.",
                "B": "ElastiCache can cache reads, but the question asks specifically for the RDS "
                     "feature that adds read-serving database copies — read replicas.",
                "C": "Vertical scaling raises the ceiling of one instance but does not distribute "
                     "read load across multiple copies.",
            },
            "exam_pattern": "'Offload/scale reads with extra copies' = RDS read replicas; "
                            "'failover/HA' = Multi-AZ.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon RDS Read Replicas"],
    },

    # ----- networking_services (Transit Gateway, VPC endpoints) -----------
    {
        "id": "clf-tech-r2-011", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise has dozens of VPCs plus on-premises networks and wants a single "
                "central hub to connect them all, instead of building many individual VPC-to-VPC "
                "peering connections. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Transit Gateway"},
            {"id": "B", "text": "VPC peering between every pair of VPCs"},
            {"id": "C", "text": "An internet gateway"},
            {"id": "D", "text": "Amazon Route 53"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Transit Gateway acts as a central hub that connects many VPCs and "
                       "on-premises networks through a single gateway, simplifying large-scale "
                       "connectivity compared with meshes of peering connections.",
            "distractors": {
                "B": "VPC peering is one-to-one and non-transitive, so connecting dozens of VPCs "
                     "requires many connections and does not scale cleanly.",
                "C": "An internet gateway connects a VPC to the public internet; it does not "
                     "interconnect many private networks.",
                "D": "Route 53 is a DNS service; it does not provide network interconnectivity "
                     "between VPCs and on-premises.",
            },
            "exam_pattern": "'Central hub connecting many VPCs and on-premises at scale' = AWS Transit "
                            "Gateway; 'simple one-to-one VPC link' = VPC peering.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "AWS Transit Gateway"],
    },
    {
        "id": "clf-tech-r2-012", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "networking_services", "difficulty": 2, "type": "mcq",
        "stem": "A security-conscious team wants resources in a VPC to reach an AWS service such as "
                "Amazon S3 using the private AWS network, without the traffic traversing the public "
                "internet. Which capability enables this?",
        "options": [
            {"id": "A", "text": "An internet gateway"},
            {"id": "B", "text": "A NAT gateway"},
            {"id": "C", "text": "A VPC endpoint"},
            {"id": "D", "text": "An Elastic IP address"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A VPC endpoint lets resources in a VPC connect privately to supported AWS "
                       "services over the AWS network, so the traffic does not go over the public "
                       "internet.",
            "distractors": {
                "A": "An internet gateway provides a path to the public internet — the opposite of "
                     "keeping traffic private.",
                "B": "A NAT gateway lets private instances reach the internet for outbound traffic; "
                     "it still uses the public internet path.",
                "D": "An Elastic IP is a static public IPv4 address; it does not create a private "
                     "path to AWS services.",
            },
            "exam_pattern": "'Reach an AWS service privately, no public internet' = VPC endpoint "
                            "(AWS PrivateLink).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon VPC endpoints / AWS PrivateLink"],
    },

    # ----- deployment_access (Systems Manager, Infrastructure as Code) ----
    {
        "id": "clf-tech-r2-013", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 2, "type": "mcq",
        "stem": "An operations team wants a single service to manage a fleet of EC2 and on-premises "
                "servers — applying OS patches, running commands at scale, and storing configuration "
                "parameters centrally. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "AWS CloudFormation"},
            {"id": "B", "text": "AWS Systems Manager"},
            {"id": "C", "text": "AWS Config"},
            {"id": "D", "text": "Amazon CloudWatch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Systems Manager provides operational management of fleets — Patch Manager "
                       "for patching, Run Command for executing commands at scale, and Parameter "
                       "Store for configuration data — across EC2 and on-premises servers.",
            "distractors": {
                "A": "CloudFormation provisions infrastructure from templates; it is not the "
                     "operational fleet-management and patching tool.",
                "C": "AWS Config records and evaluates resource configurations for compliance, not "
                     "fleet patching and command execution.",
                "D": "Amazon CloudWatch monitors metrics, logs, and alarms; it does not patch servers "
                     "or run operational commands.",
            },
            "exam_pattern": "'Patch, run commands at scale, store parameters across a server fleet' = "
                            "AWS Systems Manager.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "AWS Systems Manager"],
    },
    {
        "id": "clf-tech-r2-014", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "deployment_access", "difficulty": 1, "type": "fill",
        "stem": "The practice of defining and provisioning cloud resources from machine-readable "
                "template or definition files — so environments are repeatable and version-controlled "
                "instead of built by manual console clicks — is called Infrastructure as ______. "
                "Enter the missing word.",
        "correct": ["code", "Code", "IaC", "infrastructure as code"],
        "explanation": {
            "correct": "Infrastructure as Code (IaC) provisions infrastructure from template/"
                       "definition files (for example with AWS CloudFormation), making deployments "
                       "consistent, repeatable, and version-controlled.",
            "distractors": {},
            "exam_pattern": "'Define/provision infrastructure from templates, repeatable, no manual "
                            "clicks' = Infrastructure as Code (CloudFormation is the AWS IaC "
                            "service).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "AWS CloudFormation (Infrastructure as Code)"],
    },

    # ----- other_services (EventBridge, Amazon Q) -------------------------
    {
        "id": "clf-tech-r2-015", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 2, "type": "mcq",
        "stem": "A team wants a serverless event bus that receives events from AWS services, custom "
                "applications, and SaaS providers, and routes them to targets using rules, to build "
                "event-driven architectures. Which service fits BEST?",
        "options": [
            {"id": "A", "text": "Amazon EventBridge"},
            {"id": "B", "text": "Amazon SQS"},
            {"id": "C", "text": "Amazon Athena"},
            {"id": "D", "text": "AWS CloudTrail"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Amazon EventBridge is a serverless event bus that ingests events from AWS "
                       "services, custom apps, and SaaS partners and routes them to targets based on "
                       "rules, enabling event-driven architectures.",
            "distractors": {
                "B": "Amazon SQS is a point-to-point message queue that consumers poll; it is not a "
                     "rules-based event bus that routes from many event sources.",
                "C": "Amazon Athena runs SQL queries on data in S3; it is not an event router.",
                "D": "AWS CloudTrail records API activity for auditing; it is not an event bus for "
                     "application integration.",
            },
            "exam_pattern": "'Serverless event bus routing events from many sources via rules' = "
                            "Amazon EventBridge.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon EventBridge"],
    },
    {
        "id": "clf-tech-r2-016", "exam": "clf", "domain": "cloud_technology",
        "subtopic": "other_services", "difficulty": 1, "type": "mcq",
        "stem": "A company wants a generative AI-powered assistant from AWS — one version to help "
                "developers build and operate on AWS, and another to let employees ask questions of "
                "their enterprise data. Which service provides these assistants?",
        "options": [
            {"id": "A", "text": "Amazon SageMaker"},
            {"id": "B", "text": "Amazon Rekognition"},
            {"id": "C", "text": "Amazon Comprehend"},
            {"id": "D", "text": "Amazon Q"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Amazon Q is AWS's generative AI-powered assistant: Amazon Q Developer helps "
                       "build, troubleshoot, and operate on AWS, while Amazon Q Business answers "
                       "questions grounded in an organization's own enterprise data.",
            "distractors": {
                "A": "Amazon SageMaker is for building, training, and deploying your own machine "
                     "learning models, not a ready-to-use generative AI assistant.",
                "B": "Amazon Rekognition is a pre-built image and video analysis service.",
                "C": "Amazon Comprehend is a pre-built natural-language-processing service for "
                     "extracting insights from text.",
            },
            "exam_pattern": "'AWS generative AI assistant (for builders and for enterprise data Q&A)' "
                            "= Amazon Q (Q Developer / Q Business).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 3: Cloud Technology and Services)",
                       "Amazon Q (Amazon Q Developer and Amazon Q Business)"],
    },

    # ======================================================================
    # Domain 4 — Billing, Pricing, and Support (pricing_models,
    # billing_cost_management, support_plans, technical_resources)
    # ======================================================================

    # ----- pricing_models -------------------------------------------------
    {
        "id": "clf-bill-r2-001", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "A company is estimating AWS costs and asks how data transfer is generally priced. "
                "Which statement best reflects AWS's typical data-transfer pricing?",
        "options": [
            {"id": "A", "text": "All data transfer, in and out, is always free"},
            {"id": "B", "text": "Inbound data transfer into AWS is generally free, while outbound "
                                 "data transfer to the internet is generally charged"},
            {"id": "C", "text": "Inbound data transfer into AWS is the most expensive charge"},
            {"id": "D", "text": "Data transfer is billed only when using the AWS Management Console"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "As a general rule, inbound data transfer into AWS is free, while data "
                       "transferred out to the internet is metered and charged (beyond any free-tier "
                       "allowance).",
            "distractors": {
                "A": "Outbound internet data transfer is generally charged, so not all transfer is "
                     "free.",
                "C": "Inbound transfer into AWS is typically free, not the most expensive charge.",
                "D": "Data-transfer charges are based on bytes moved, not on which interface "
                     "(console, CLI, SDK) you use.",
            },
            "exam_pattern": "'Data IN is generally free; data OUT to the internet is generally "
                            "charged' — a common CLF cost concept.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS - How AWS Pricing Works (data transfer)"],
    },
    {
        "id": "clf-bill-r2-002", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "Over the years AWS has repeatedly lowered the prices of many services as it grows, "
                "gains efficiency, and benefits from greater scale. Which AWS pricing principle does "
                "this reflect?",
        "options": [
            {"id": "A", "text": "Pay-as-you-go"},
            {"id": "B", "text": "Pay less when you reserve"},
            {"id": "C", "text": "AWS reduces prices over time as it grows (benefit from AWS's "
                                 "economies of scale)"},
            {"id": "D", "text": "Pay more for predictable workloads"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A core AWS pricing principle is that as AWS grows, its economies of scale and "
                       "efficiencies let it lower prices over time, passing savings to customers.",
            "distractors": {
                "A": "Pay-as-you-go means paying only for what you use; it does not describe AWS "
                     "lowering prices as it scales.",
                "B": "'Pay less when you reserve' is the commitment-discount principle, not "
                     "provider-wide price reductions over time.",
                "D": "AWS does not charge more for predictable workloads; predictability typically "
                     "enables discounts, not surcharges.",
            },
            "exam_pattern": "Pricing fundamentals: pay-as-you-go, pay less when you reserve, pay less "
                            "by using more, and AWS keeps reducing prices as it grows.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS - How AWS Pricing Works (pricing principles)"],
    },

    # ----- billing_cost_management ---------------------------------------
    {
        "id": "clf-bill-r2-003", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants machine-learning-based recommendations that identify optimal AWS "
                "resources (for example, right-sizing EC2 instances, Auto Scaling groups, EBS "
                "volumes, and Lambda functions) to reduce cost and improve performance. Which service "
                "fits BEST?",
        "options": [
            {"id": "A", "text": "AWS Compute Optimizer"},
            {"id": "B", "text": "AWS Pricing Calculator"},
            {"id": "C", "text": "AWS Budgets"},
            {"id": "D", "text": "AWS Cost and Usage Report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Compute Optimizer uses machine learning to analyze utilization and "
                       "recommend optimal resource configurations (right-sizing) for EC2, Auto "
                       "Scaling groups, EBS volumes, and Lambda functions.",
            "distractors": {
                "B": "The Pricing Calculator estimates costs before deployment; it does not analyze "
                     "running resources and recommend right-sizing.",
                "C": "AWS Budgets sends threshold alerts on cost/usage; it does not generate "
                     "ML-based right-sizing recommendations.",
                "D": "The Cost and Usage Report delivers granular billing data to S3; it is not a "
                     "right-sizing recommendation engine.",
            },
            "exam_pattern": "'ML recommendations for optimal/right-sized resources' = AWS Compute "
                            "Optimizer.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS Compute Optimizer"],
    },
    {
        "id": "clf-bill-r2-004", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "multi",
        "stem": "Which TWO are benefits of using consolidated billing with AWS Organizations? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "A single, combined bill across all accounts in the organization"},
            {"id": "B", "text": "Aggregated usage can reach volume pricing tiers, and Reserved "
                                 "Instance / Savings Plans discounts can be shared across accounts"},
            {"id": "C", "text": "AWS waives all usage charges for member accounts"},
            {"id": "D", "text": "It automatically encrypts all data stored in member accounts"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Consolidated billing provides one combined bill for all accounts and lets "
                       "their combined usage reach volume pricing tiers, with Reserved Instance and "
                       "Savings Plans discounts shared across accounts — at no additional charge.",
            "distractors": {
                "C": "Consolidated billing combines charges; it does not waive member accounts' usage "
                     "charges.",
                "D": "Consolidated billing is about billing, not data encryption of member accounts.",
            },
            "exam_pattern": "Consolidated billing = one bill + aggregated volume discounts + shared "
                            "RI/Savings Plans benefits, at no extra cost.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS Organizations - Consolidated Billing"],
    },

    # ----- support_plans --------------------------------------------------
    {
        "id": "clf-bill-r2-005", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A company planning a major, time-bound product launch wants AWS to provide "
                "architecture and scaling guidance and dedicated real-time support during the event "
                "so its workload can handle the surge. Which AWS Support offering provides this?",
        "options": [
            {"id": "A", "text": "Basic Support"},
            {"id": "B", "text": "AWS re:Post community Q&A"},
            {"id": "C", "text": "Infrastructure Event Management (available with Enterprise Support "
                                 "and Enterprise On-Ramp)"},
            {"id": "D", "text": "AWS Pricing Calculator"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Infrastructure Event Management (IEM) is an offering of Enterprise Support "
                       "(and Enterprise On-Ramp) that provides architectural and scaling guidance and "
                       "dedicated real-time support to help a workload handle a planned, high-demand "
                       "event such as a launch.",
            "distractors": {
                "A": "Basic Support offers no technical support beyond account/billing help, so it "
                     "cannot provide event scaling guidance.",
                "B": "AWS re:Post is a free community Q&A service, not dedicated real-time launch "
                     "support.",
                "D": "The Pricing Calculator estimates costs; it does not provide event support.",
            },
            "exam_pattern": "'Dedicated guidance + real-time support for a planned high-traffic "
                            "event' = Infrastructure Event Management (Enterprise / Enterprise "
                            "On-Ramp).",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS Support plans (Infrastructure Event Management)"],
    },

    # ----- technical_resources -------------------------------------------
    {
        "id": "clf-bill-r2-006", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a central place to view the service quotas (limits) that "
                "apply to the account and to request increases to those quotas. Which service "
                "provides this?",
        "options": [
            {"id": "A", "text": "AWS Budgets"},
            {"id": "B", "text": "AWS Config"},
            {"id": "C", "text": "Amazon CloudWatch"},
            {"id": "D", "text": "AWS Service Quotas"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "AWS Service Quotas is a central console to view the quotas (limits) that apply "
                       "to AWS services in an account and to request quota increases from one place.",
            "distractors": {
                "A": "AWS Budgets tracks and alerts on cost and usage thresholds; it does not manage "
                     "service quotas.",
                "B": "AWS Config evaluates resource configurations for compliance, not service "
                     "quotas.",
                "C": "Amazon CloudWatch monitors metrics and alarms; while it can alarm on some "
                     "usage, it is not the central place to view and request quota increases.",
            },
            "exam_pattern": "'View and request increases to service limits/quotas in one place' = AWS "
                            "Service Quotas.",
        },
        "references": ["AWS CLF-C02 Exam Guide (Domain 4: Billing, Pricing, and Support)",
                       "AWS Service Quotas"],
    },
]
