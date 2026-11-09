"""Microsoft Azure Fundamentals (AZ-900) pool - Domain 1: Cloud Concepts.

Original, objective-aligned practice items for the three Cloud Concepts
subtopics tracked in CertLab:
  * az_cloud_models    - the shared responsibility model; public, private, and
                         hybrid cloud; the consumption-based / pay-as-you-go
                         model; CapEx vs OpEx.
  * az_cloud_benefits  - high availability & scalability (vertical vs horizontal,
                         elasticity); reliability & predictability; security &
                         governance; manageability of and in the cloud.
  * az_service_types   - IaaS vs PaaS vs SaaS: what each provides, who manages
                         what, and when to choose each.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the answer key authored here as "A" is not
positionally biased, every wrong option carries a distractor note, and each item
names the Microsoft Learn area it draws on so facts stay traceable. Fundamentals
depth only (concepts, when-to-use, who-manages-what) - no numeric limits/prices,
no region/version trivia, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== az_cloud_models ==================================================
    {
        "id": "az900-cc-001", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "No matter which Azure service a company adopts, one set of duties never transfers "
                "to Microsoft. Which responsibility does the customer always retain?",
        "options": [
            {"id": "A", "text": "Its information and data"},
            {"id": "B", "text": "The physical host servers"},
            {"id": "C", "text": "The physical datacenter network"},
            {"id": "D", "text": "The physical security of the facility"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Under the shared responsibility model, information and data (along with devices "
                       "and accounts/identities) always remain the customer's responsibility, whether "
                       "the service is IaaS, PaaS, or SaaS.",
            "distractors": {
                "B": "Physical hosts are always the provider's responsibility in every service type.",
                "C": "The physical network is always owned and secured by the provider.",
                "D": "Physical datacenter security is always Microsoft's responsibility, never the customer's.",
            },
            "exam_pattern": "Always-customer = data, devices, accounts/identities; always-provider = "
                            "physical hosts, network, datacenter.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
    {
        "id": "az900-cc-002", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A customer running Azure virtual machines asks who secures the physical servers and "
                "the datacenter they sit in. Who holds that responsibility?",
        "options": [
            {"id": "A", "text": "Microsoft, in every cloud service type"},
            {"id": "B", "text": "The customer, because they deployed the VMs"},
            {"id": "C", "text": "It is split evenly between the two parties"},
            {"id": "D", "text": "Whichever party is named in an Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The physical hosts, physical network, and datacenter are always the provider's "
                       "responsibility, regardless of whether the service is IaaS, PaaS, or SaaS.",
            "distractors": {
                "B": "The physical layer is never the customer's duty, even in IaaS where they manage the OS.",
                "C": "The physical datacenter is not a shared or split responsibility; it is entirely the provider's.",
                "D": "Azure Policy governs how resources are configured, not who owns the physical datacenter.",
            },
            "exam_pattern": "Physical hosts, physical network, and the datacenter are always the provider's.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
    {
        "id": "az900-cc-003", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "As an organization moves the same workload from IaaS toward SaaS, how does the "
                "division of responsibilities change?",
        "options": [
            {"id": "A", "text": "The customer manages less and the provider manages more"},
            {"id": "B", "text": "The customer manages more and the provider manages less"},
            {"id": "C", "text": "Responsibilities stay identical across all service types"},
            {"id": "D", "text": "The customer becomes responsible for the physical datacenter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Moving from IaaS to PaaS to SaaS, the provider takes on more (such as the OS and "
                       "applications) and the customer retains less, ending at data, devices, and identities.",
            "distractors": {
                "B": "This is reversed; responsibility shifts toward the provider as you move toward SaaS.",
                "C": "The responsibility split is exactly what changes across service types.",
                "D": "The physical datacenter is never the customer's responsibility in any service type.",
            },
            "exam_pattern": "More managed service (toward SaaS) means less customer responsibility.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
    {
        "id": "az900-cc-004", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "A provider owns the hardware and offers services over the internet to many "
                "organizations that share it. Which cloud model is this?",
        "options": [
            {"id": "A", "text": "Public cloud"},
            {"id": "B", "text": "Private cloud"},
            {"id": "C", "text": "Hybrid cloud"},
            {"id": "D", "text": "On-premises datacenter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A public cloud is owned by a third-party provider, shared across many customers "
                       "(multi-tenant), and delivered over the internet with no up-front hardware cost.",
            "distractors": {
                "B": "A private cloud's resources are used exclusively by a single organization, not shared.",
                "C": "A hybrid cloud combines public and private environments; this describes only the public part.",
                "D": "An on-premises datacenter is owned and operated by the organization itself, not a provider.",
            },
            "exam_pattern": "Shared, provider-owned, internet-delivered, multi-tenant = public cloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing - public, private, and hybrid cloud models"],
    },
    {
        "id": "az900-cc-005", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A bank wants cloud-style resources used exclusively by itself, with the greatest "
                "control over the environment. Which deployment model fits best?",
        "options": [
            {"id": "A", "text": "Private cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Hybrid cloud"},
            {"id": "D", "text": "Multi-tenant SaaS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A private cloud dedicates resources to a single organization (hosted on-site or by "
                       "a third party), giving the most control over the environment.",
            "distractors": {
                "B": "A public cloud is shared and multi-tenant, offering less control over the stack.",
                "C": "A hybrid cloud mixes private and public; the scenario asks only for exclusive use.",
                "D": "Multi-tenant SaaS shares infrastructure among customers, the opposite of exclusive use.",
            },
            "exam_pattern": "Used by a single organization with maximum control = private cloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing - public, private, and hybrid cloud models"],
    },
    {
        "id": "az900-cc-006", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A retailer keeps sensitive records in its own datacenter but shifts extra holiday "
                "traffic to Azure when demand spikes. Which model is this?",
        "options": [
            {"id": "A", "text": "Hybrid cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Private cloud"},
            {"id": "D", "text": "Multicloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hybrid cloud combines a private (on-premises) environment with the public cloud, "
                       "letting workloads move between them, such as bursting to Azure for peak demand.",
            "distractors": {
                "B": "A public-cloud-only approach would not keep the records in the company's own datacenter.",
                "C": "A private cloud alone cannot burst into Azure's public capacity for the spike.",
                "D": "Multicloud means using more than one public provider; here on-premises is combined with one cloud.",
            },
            "exam_pattern": "On-premises plus public cloud working together = hybrid.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing - public, private, and hybrid cloud models"],
    },
    {
        "id": "az900-cc-007", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "A team provisions Azure resources and is billed only for the compute and storage it "
                "actually uses, with no up-front purchase. What is this called?",
        "options": [
            {"id": "A", "text": "The consumption-based (pay-as-you-go) model"},
            {"id": "B", "text": "A capital expenditure model"},
            {"id": "C", "text": "A fixed annual licensing model"},
            {"id": "D", "text": "A perpetual on-premises license"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The consumption-based model means you pay only for the resources you use, with no "
                       "up-front cost, and your spend scales up or down with usage.",
            "distractors": {
                "B": "Capital expenditure is up-front spending on owned infrastructure, not usage-based billing.",
                "C": "A fixed annual license charges a set fee regardless of how much you use.",
                "D": "A perpetual license is a one-time purchase to own software, not pay-per-use.",
            },
            "exam_pattern": "Pay only for what you use, no up-front cost = consumption-based model.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the consumption-based model"],
    },
    {
        "id": "az900-cc-008", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Moving from buying its own servers to paying monthly for Azure services changes how a "
                "company accounts for IT spend. Which shift occurs?",
        "options": [
            {"id": "A", "text": "From capital expenditure (CapEx) to operational expenditure (OpEx)"},
            {"id": "B", "text": "From operational expenditure (OpEx) to capital expenditure (CapEx)"},
            {"id": "C", "text": "From a variable cost to a one-time fixed cost"},
            {"id": "D", "text": "From a subscription model to an up-front purchase"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Buying servers is CapEx (up-front investment in owned assets); paying for cloud "
                       "services as you use them is OpEx, so the cloud shifts spending from CapEx to OpEx.",
            "distractors": {
                "B": "This reverses the direction; cloud moves spend toward OpEx, not CapEx.",
                "C": "Cloud billing is an ongoing variable cost, not a one-time fixed cost.",
                "D": "Pay-as-you-go cloud is the opposite of an up-front purchase.",
            },
            "exam_pattern": "Cloud pay-as-you-go turns big up-front CapEx into ongoing OpEx.",
        },
        "references": ["Microsoft Learn (AZ-900): Compare cloud pricing (CapEx vs OpEx)"],
    },
    {
        "id": "az900-cc-009", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A finance manager records a large one-time purchase of on-premises servers and "
                "datacenter equipment. How is this expense best classified?",
        "options": [
            {"id": "A", "text": "Capital expenditure (CapEx)"},
            {"id": "B", "text": "Operational expenditure (OpEx)"},
            {"id": "C", "text": "Consumption-based spending"},
            {"id": "D", "text": "A pay-as-you-go cost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A one-time, up-front purchase of physical infrastructure that is owned and "
                       "depreciated over time is a capital expenditure (CapEx).",
            "distractors": {
                "B": "OpEx is ongoing pay-for-use spending, not an up-front hardware purchase.",
                "C": "Consumption-based spending is billed by actual usage, unlike a fixed hardware buy.",
                "D": "Pay-as-you-go describes cloud billing tied to usage, not owning hardware up front.",
            },
            "exam_pattern": "Up-front, owned, depreciated hardware = CapEx; ongoing usage billing = OpEx.",
        },
        "references": ["Microsoft Learn (AZ-900): Compare cloud pricing (CapEx vs OpEx)"],
    },
    {
        "id": "az900-cc-010", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "An insurer must keep one legacy app on-premises for compliance while gradually moving "
                "other systems to Azure. Which model supports this?",
        "options": [
            {"id": "A", "text": "Hybrid cloud"},
            {"id": "B", "text": "Public cloud only"},
            {"id": "C", "text": "Private cloud only"},
            {"id": "D", "text": "The consumption-based model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Hybrid lets the insurer keep some workloads on-premises (for compliance) while "
                       "using the public cloud for others, which also eases a gradual migration.",
            "distractors": {
                "B": "A public-cloud-only model cannot keep the legacy app running on-premises.",
                "C": "A private-cloud-only model would not use Azure's public cloud for the other systems.",
                "D": "The consumption-based model is a pricing approach, not a deployment model.",
            },
            "exam_pattern": "Keep some on-prem, use cloud for the rest, migrate over time = hybrid.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing - public, private, and hybrid cloud models"],
    },
    {
        "id": "az900-cc-011", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 3, "type": "multi",
        "stem": "A customer reviews the shared responsibility model across IaaS, PaaS, and SaaS. Which "
                "TWO responsibilities always remain the customer's? (Choose two.)",
        "options": [
            {"id": "A", "text": "The organization's information and data"},
            {"id": "B", "text": "User accounts and identities"},
            {"id": "C", "text": "The physical host servers in the datacenter"},
            {"id": "D", "text": "The physical datacenter network"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Information/data and accounts/identities (along with devices) stay the customer's "
                       "responsibility in IaaS, PaaS, and SaaS alike.",
            "distractors": {
                "C": "Physical host servers are always the provider's responsibility, never the customer's.",
                "D": "The physical datacenter network is always the provider's responsibility.",
            },
            "exam_pattern": "Always-customer trio: data, devices, accounts/identities.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
    {
        "id": "az900-cc-012", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Compared with running its own private cloud, what key advantage does an organization "
                "gain by using the public cloud?",
        "options": [
            {"id": "A", "text": "No capital expense for hardware, since the provider owns and maintains it"},
            {"id": "B", "text": "Exclusive, single-tenant use of all physical servers"},
            {"id": "C", "text": "Full physical control of the datacenter"},
            {"id": "D", "text": "Elimination of all of its security responsibilities"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The public cloud removes up-front hardware CapEx because the provider owns and "
                       "operates the infrastructure, and you pay as you go.",
            "distractors": {
                "B": "Exclusive, single-tenant hardware describes a private cloud, not the public cloud.",
                "C": "Full physical control of the datacenter is a private-cloud or on-premises trait.",
                "D": "Security is always shared; the customer keeps responsibilities such as data and identities.",
            },
            "exam_pattern": "Public cloud = no hardware CapEx, provider-owned; beware 'eliminate all security' absolutes.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing - public, private, and hybrid cloud models"],
    },

    # ===== az_cloud_benefits ================================================
    {
        "id": "az900-cc-013", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A company wants its customer-facing app to stay up with as little downtime as "
                "possible. Which cloud benefit most directly addresses this goal?",
        "options": [
            {"id": "A", "text": "High availability"},
            {"id": "B", "text": "Economies of scale"},
            {"id": "C", "text": "Governance"},
            {"id": "D", "text": "Capital expenditure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "High availability keeps applications running with minimal downtime, typically "
                       "backed by service-level agreements and redundant infrastructure.",
            "distractors": {
                "B": "Economies of scale is about lower unit cost from aggregated demand, not uptime.",
                "C": "Governance is about meeting standards and compliance, not keeping an app online.",
                "D": "Capital expenditure is a spending type, not an availability benefit.",
            },
            "exam_pattern": "Minimize downtime / keep apps running = high availability.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-014", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "To handle a heavier database, an admin raises an existing Azure VM's CPU and memory "
                "instead of adding more VMs. What is this?",
        "options": [
            {"id": "A", "text": "Vertical scaling (scaling up)"},
            {"id": "B", "text": "Horizontal scaling (scaling out)"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "Geo-replication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Vertical scaling (scaling up or down) changes the power - CPU, memory - of an "
                       "existing resource rather than adding more instances.",
            "distractors": {
                "B": "Horizontal scaling adds or removes separate instances, which the admin did not do.",
                "C": "Load balancing distributes traffic across instances; it does not resize a VM.",
                "D": "Geo-replication copies data across regions; it is not a form of scaling a VM's size.",
            },
            "exam_pattern": "Bigger/stronger single resource = vertical (up); more instances = horizontal (out).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-015", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "As web traffic grows, a team adds more identical VM instances behind a load balancer "
                "instead of resizing one server. Which scaling is this?",
        "options": [
            {"id": "A", "text": "Horizontal scaling (scaling out)"},
            {"id": "B", "text": "Vertical scaling (scaling up)"},
            {"id": "C", "text": "Capital scaling"},
            {"id": "D", "text": "Manual failover"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Horizontal scaling (scaling out or in) adds or removes instances to meet demand, "
                       "exactly what adding more VMs behind a load balancer does.",
            "distractors": {
                "B": "Vertical scaling resizes a single resource, which the team specifically avoided.",
                "C": "'Capital scaling' is not a real scaling type.",
                "D": "Failover switches to a standby after a fault; it does not add capacity for growth.",
            },
            "exam_pattern": "Add or remove instances = horizontal (out/in).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-016", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A workload automatically gains resources during busy hours and releases them when "
                "demand drops, with no manual action. Which capability is this?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "High availability"},
            {"id": "C", "text": "Fault tolerance"},
            {"id": "D", "text": "Capital expenditure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elasticity is the ability to automatically add resources as demand rises and "
                       "remove them as it falls, so capacity matches load.",
            "distractors": {
                "B": "High availability is about uptime, not automatically right-sizing capacity.",
                "C": "Fault tolerance is surviving component failure, not matching capacity to demand.",
                "D": "Capital expenditure is a spending type, not a scaling behavior.",
            },
            "exam_pattern": "Automatic scale-out under load and scale-in when idle = elasticity.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-017", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A design goal is for the system to recover from failures and keep functioning, partly "
                "by deploying across multiple regions. Which benefit is this?",
        "options": [
            {"id": "A", "text": "Reliability"},
            {"id": "B", "text": "Manageability"},
            {"id": "C", "text": "Consumption-based pricing"},
            {"id": "D", "text": "Vertical scaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reliability is a system's ability to recover from failures and continue to "
                       "function; the cloud's distributed, multi-region design supports it.",
            "distractors": {
                "B": "Manageability is about operating and managing resources, not recovering from failure.",
                "C": "Consumption-based pricing is a cost model, not a resilience property.",
                "D": "Vertical scaling resizes a resource; it is not itself a recover-from-failure goal.",
            },
            "exam_pattern": "Recover from failure and keep running = reliability (a Well-Architected pillar).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of reliability and predictability"],
    },
    {
        "id": "az900-cc-018", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "An architect uses autoscaling and load balancing so the application's performance can "
                "be forecast as demand changes. Which cloud benefit does this support?",
        "options": [
            {"id": "A", "text": "Predictability (performance predictability)"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Capital expenditure"},
            {"id": "D", "text": "Multi-tenancy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Performance predictability means forecasting the resources needed for a good "
                       "experience; autoscaling, load balancing, and high availability support it.",
            "distractors": {
                "B": "Governance concerns compliance and standards, not forecasting performance.",
                "C": "Capital expenditure is a spending model, not a performance benefit.",
                "D": "Multi-tenancy describes shared infrastructure, not performance forecasting.",
            },
            "exam_pattern": "Forecast performance via autoscale/load balancing/HA = performance predictability.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of reliability and predictability"],
    },
    {
        "id": "az900-cc-019", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A finance team wants to forecast and track Azure spending using the pricing calculator "
                "and cost-management tools. Which cloud benefit is this?",
        "options": [
            {"id": "A", "text": "Predictability (cost predictability)"},
            {"id": "B", "text": "High availability"},
            {"id": "C", "text": "Horizontal scaling"},
            {"id": "D", "text": "Private-cloud isolation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cost predictability means forecasting and tracking spend; tools such as the "
                       "Pricing Calculator, TCO Calculator, and Microsoft Cost Management support it.",
            "distractors": {
                "B": "High availability is about uptime, not forecasting cost.",
                "C": "Horizontal scaling is about capacity, not predicting spend.",
                "D": "Private-cloud isolation is a deployment trait, not a cost-forecasting benefit.",
            },
            "exam_pattern": "Forecast/track spend with calculators and cost management = cost predictability.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of reliability and predictability"],
    },
    {
        "id": "az900-cc-020", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "By choosing managed Azure services, a team lets the provider handle operating-system "
                "patching while it still sets access controls. Which benefit is this?",
        "options": [
            {"id": "A", "text": "The security benefits of the cloud"},
            {"id": "B", "text": "Economies of scale"},
            {"id": "C", "text": "Vertical scaling"},
            {"id": "D", "text": "Consumption-based billing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The cloud lets you choose your level of responsibility: with managed (PaaS/SaaS) "
                       "services the provider patches the OS, strengthening security while you manage access.",
            "distractors": {
                "B": "Economies of scale is about lower price from aggregated demand, not security.",
                "C": "Vertical scaling is about capacity, not who patches the operating system.",
                "D": "Consumption-based billing is a cost model, not a security benefit.",
            },
            "exam_pattern": "Provider handles patching in managed services = a cloud security benefit.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of security and governance"],
    },
    {
        "id": "az900-cc-021", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A company must ensure every deployed resource follows corporate standards, using "
                "policies and templates that flag anything non-compliant. Which cloud benefit is this?",
        "options": [
            {"id": "A", "text": "Governance"},
            {"id": "B", "text": "Elasticity"},
            {"id": "C", "text": "High availability"},
            {"id": "D", "text": "Capital expenditure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance uses tools such as Azure Policy, resource locks, and templates to "
                       "enforce corporate and regulatory standards and flag non-compliant resources.",
            "distractors": {
                "B": "Elasticity is automatic scaling with demand, not enforcing standards.",
                "C": "High availability is about uptime, not compliance with corporate standards.",
                "D": "Capital expenditure is a spending type, unrelated to enforcing standards.",
            },
            "exam_pattern": "Enforce standards/compliance via policy and templates = governance.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of security and governance"],
    },
    {
        "id": "az900-cc-022", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 3, "type": "mcq",
        "stem": "An operations team sets resources to scale automatically, deploys from reusable "
                "templates, and gets health alerts. Which kind of management is this?",
        "options": [
            {"id": "A", "text": "Management of the cloud"},
            {"id": "B", "text": "Management in the cloud"},
            {"id": "C", "text": "On-premises management"},
            {"id": "D", "text": "Identity governance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Management OF the cloud is how you manage cloud resources: autoscaling, deploying "
                       "from templates (such as ARM or Bicep), and monitoring with alerts.",
            "distractors": {
                "B": "Management IN the cloud is about the tools used to interact with Azure, not these tasks.",
                "C": "On-premises management is not cloud management at all.",
                "D": "Identity governance is a narrower security/access topic, not this set of operational tasks.",
            },
            "exam_pattern": "Autoscale, templates, monitoring/alerts = management OF the cloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of manageability in the cloud"],
    },
    {
        "id": "az900-cc-023", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "An administrator interacts with Azure through the web portal, the CLI, PowerShell, and "
                "REST APIs. Which type of manageability does this describe?",
        "options": [
            {"id": "A", "text": "Management in the cloud"},
            {"id": "B", "text": "Management of the cloud"},
            {"id": "C", "text": "Capital expenditure management"},
            {"id": "D", "text": "Horizontal scaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Management IN the cloud is how you interact with your environment: the Azure "
                       "portal, CLI, PowerShell, and APIs.",
            "distractors": {
                "B": "Management OF the cloud is automating, scaling, and monitoring the resources themselves.",
                "C": "'Capital expenditure management' is a spending concept, not a way to interact with Azure.",
                "D": "Horizontal scaling is a scaling method, not a management interface.",
            },
            "exam_pattern": "Portal, CLI, PowerShell, APIs = management IN the cloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of manageability in the cloud"],
    },
    {
        "id": "az900-cc-024", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 3, "type": "multi",
        "stem": "An app's load swings sharply through the day and the team wants Azure to match "
                "capacity to demand. Which TWO scaling approaches apply? (Choose two.)",
        "options": [
            {"id": "A", "text": "Add or remove VM instances (horizontal scaling)"},
            {"id": "B", "text": "Increase or decrease a VM's size (vertical scaling)"},
            {"id": "C", "text": "Delete the application's resource group"},
            {"id": "D", "text": "Switch the billing from OpEx to CapEx"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Capacity can be matched to demand by scaling horizontally (adding/removing "
                       "instances) or vertically (resizing a resource); both are valid scaling approaches.",
            "distractors": {
                "C": "Deleting the resource group removes the app entirely; it does not scale capacity.",
                "D": "Changing how spend is accounted for does not adjust capacity to load.",
            },
            "exam_pattern": "Two ways to scale: horizontal (instances) and vertical (resource size).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },

    # ===== az_service_types =================================================
    {
        "id": "az900-cc-025", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 1, "type": "mcq",
        "stem": "A team wants cloud servers where it controls the operating system and installed "
                "software while the provider runs the physical hardware. Which service type?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "On-premises"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IaaS provides virtualized infrastructure such as VMs and networking; the provider "
                       "maintains the physical hardware while the customer manages the OS and everything above it.",
            "distractors": {
                "B": "PaaS hands operating-system management to the provider, reducing that control.",
                "C": "SaaS delivers finished software with no operating-system control for the customer.",
                "D": "On-premises means the organization owns and runs the physical hardware too.",
            },
            "exam_pattern": "You manage the OS and up, provider runs the hardware = IaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },
    {
        "id": "az900-cc-026", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 1, "type": "mcq",
        "stem": "Staff sign in and use a ready-made email and productivity application over the "
                "internet, managing none of the servers underneath. Which service type is this?",
        "options": [
            {"id": "A", "text": "SaaS (Software as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "D", "text": "Private cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SaaS delivers complete, provider-managed software to end users (usually by "
                       "subscription over the internet); the customer just uses it and manages their data and accounts.",
            "distractors": {
                "B": "PaaS targets developers building applications, not consuming finished software.",
                "C": "IaaS gives you VMs and infrastructure to manage, not ready-made software.",
                "D": "Private cloud is a deployment model, not a service type like SaaS.",
            },
            "exam_pattern": "Ready-to-use software, provider manages everything = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - SaaS"],
    },
    {
        "id": "az900-cc-027", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 1, "type": "mcq",
        "stem": "Developers want a managed platform to build and deploy an app without maintaining the "
                "operating system or servers underneath. Which service type fits?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "On-premises hosting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PaaS provides a managed environment for developing, testing, and deploying apps; "
                       "the provider handles the OS and infrastructure while developers focus on code and data.",
            "distractors": {
                "B": "IaaS would still require the team to manage the operating system.",
                "C": "SaaS is finished software, not a platform on which to build your own app.",
                "D": "On-premises hosting means managing the servers and OS yourself.",
            },
            "exam_pattern": "Managed platform to build/deploy apps, no OS upkeep = PaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - PaaS"],
    },
    {
        "id": "az900-cc-028", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to move existing servers to Azure with minimal changes while keeping "
                "full control of each operating system. Which service type suits this?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "A hybrid deployment model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IaaS suits lift-and-shift migrations because it gives maximum control over the "
                       "operating system and configuration of each server.",
            "distractors": {
                "B": "PaaS abstracts the OS away, reducing the control the company wants to keep.",
                "C": "SaaS offers no operating-system access at all.",
                "D": "Hybrid is a deployment model describing where resources live, not the service type here.",
            },
            "exam_pattern": "Lift-and-shift with full OS control = IaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },
    {
        "id": "az900-cc-029", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "A dev team wants to ship a web app quickly and let Azure handle OS patching, runtime, "
                "and platform scaling. Which service type should it use?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "Colocation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PaaS lets developers focus on the application while the provider manages the OS, "
                       "runtime, patching, and platform scaling.",
            "distractors": {
                "B": "IaaS would put OS patching and platform maintenance back on the team.",
                "C": "SaaS is finished software, not a place to deploy your own application.",
                "D": "Colocation is renting datacenter space for your own hardware, not a managed platform.",
            },
            "exam_pattern": "Deploy your app, provider manages the platform/OS = PaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - PaaS"],
    },
    {
        "id": "az900-cc-030", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "A small business wants finished accounting and email software with no servers to "
                "manage, paid by subscription per user. Which service type should it choose?",
        "options": [
            {"id": "A", "text": "SaaS (Software as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "D", "text": "Hybrid cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SaaS delivers complete, subscription-based software (such as email and finance "
                       "apps) with the provider managing everything underneath.",
            "distractors": {
                "B": "PaaS is for building and deploying apps, not consuming finished ones.",
                "C": "IaaS would require the business to manage VMs and operating systems.",
                "D": "Hybrid cloud is a deployment model, not a ready-to-use application.",
            },
            "exam_pattern": "Finished, subscription software, nothing to manage = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - SaaS"],
    },
    {
        "id": "az900-cc-031", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "When an organization deploys an application to an Azure PaaS offering, who is "
                "responsible for patching and maintaining the operating system?",
        "options": [
            {"id": "A", "text": "The cloud provider (Microsoft)"},
            {"id": "B", "text": "The customer's application team"},
            {"id": "C", "text": "The customer's end users"},
            {"id": "D", "text": "No one, because PaaS has no operating system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In PaaS the provider manages the operating system (including patching) and the "
                       "underlying platform; the customer manages the app and its data.",
            "distractors": {
                "B": "The customer patching the OS describes the IaaS split, not PaaS.",
                "C": "End users only consume the application; they do not patch the OS.",
                "D": "There is an operating system in PaaS; the provider simply manages it for you.",
            },
            "exam_pattern": "PaaS/SaaS: provider patches the OS; IaaS: customer does.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - PaaS"],
    },
    {
        "id": "az900-cc-032", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "A customer runs Azure virtual machines under IaaS. Who is responsible for installing "
                "operating-system updates and configuring the OS?",
        "options": [
            {"id": "A", "text": "The customer"},
            {"id": "B", "text": "Microsoft, as part of IaaS"},
            {"id": "C", "text": "The hardware vendor"},
            {"id": "D", "text": "It is fully automated, with no owner"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In IaaS the provider maintains the physical hardware, but the customer manages "
                       "the operating system, including its updates, configuration, and the software above it.",
            "distractors": {
                "B": "Provider-managed operating systems begin at PaaS, not IaaS.",
                "C": "Hardware vendors do not patch a customer's guest operating system.",
                "D": "Operating-system updates do not apply themselves; someone must own the task.",
            },
            "exam_pattern": "IaaS = customer manages the OS and up; provider only runs the hardware.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },
    {
        "id": "az900-cc-033", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 3, "type": "mcq",
        "stem": "A legacy application needs specific OS-level drivers and full control of the server "
                "configuration in Azure. Which service type best meets this need?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "The consumption-based model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IaaS gives the OS-level control and custom server configuration that a legacy "
                       "app's specific drivers require.",
            "distractors": {
                "B": "PaaS hides the operating system, which blocks driver-level control.",
                "C": "SaaS offers no configuration or OS access.",
                "D": "The consumption-based model is a pricing approach, not a service type.",
            },
            "exam_pattern": "Need OS-level control / custom configuration = IaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },
    {
        "id": "az900-cc-034", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 3, "type": "mcq",
        "stem": "A company wants a ready-to-use customer-relationship application staff can adopt right "
                "away, with the vendor handling all maintenance. Which service type fits?",
        "options": [
            {"id": "A", "text": "SaaS (Software as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "PaaS (Platform as a Service)"},
            {"id": "D", "text": "Private cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A ready-to-use, vendor-maintained application is SaaS: the provider runs and "
                       "maintains everything, and the customer simply uses it.",
            "distractors": {
                "B": "IaaS would require the company to build and manage the whole application stack.",
                "C": "PaaS still requires the company to build the application itself.",
                "D": "Private cloud is a deployment model, not a finished application.",
            },
            "exam_pattern": "Ready-made app, vendor maintains all = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - SaaS"],
    },
    {
        "id": "az900-cc-035", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 3, "type": "multi",
        "stem": "An architect compares running a workload as IaaS versus consuming it as SaaS. Which "
                "TWO responsibilities move from the customer to the provider? (Choose two.)",
        "options": [
            {"id": "A", "text": "Patching and maintaining the operating system"},
            {"id": "B", "text": "Installing and configuring the applications"},
            {"id": "C", "text": "Classifying and protecting its own data"},
            {"id": "D", "text": "Managing its user accounts and identities"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "The operating system and applications are the customer's job in IaaS but are "
                       "managed by the provider in SaaS, so these shift to the provider as you move toward SaaS.",
            "distractors": {
                "C": "Data is always the customer's responsibility, in IaaS and SaaS alike.",
                "D": "Accounts and identities are always the customer's responsibility in every service type.",
            },
            "exam_pattern": "OS and apps shift to the provider toward SaaS; data and identities never do.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
]
