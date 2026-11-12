"""Microsoft Azure Fundamentals (AZ-900) ROUND-2 EXPANSION pool.

This module deepens the verified AZ-900 bank. Round 1 (content_az900_concepts.py,
content_az900_architecture.py, content_az900_governance.py) contributed 121 items
using the id prefixes ``az900-cc-``, ``az900-arch-`` and ``az900-gov-``. This
round adds ~80 NEW, non-duplicate items, reusing each domain's round-1 prefix with
an extra ``r2`` segment (``az900-cc-r2-``, ``az900-arch-r2-``, ``az900-gov-r2-``)
so every id is unique against round 1.

Coverage is distributed by exam weight:
  * az_architecture_services  (38%) - 30 items
  * az_management_governance  (34%) - 27 items
  * az_cloud_concepts         (28%) - 23 items

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer key is not positionally
biased; in addition, correct answers here are deliberately spread across A/B/C/D.
Every wrong option carries a distractor note, and each item names the Microsoft
Learn (AZ-900) area it draws on so facts stay traceable. Current product naming is
used throughout (Microsoft Entra ID, Microsoft Defender for Cloud, Azure Arc,
Microsoft Purview); never "Azure AD". Fundamentals depth only (concepts,
when-to-use, who-manages-what) - no exact prices, service limits, or region/version
trivia that drift over time, and never real or memorized exam items.
"""

QUESTIONS = [
    # =====================================================================
    # DOMAIN 1 - Cloud Concepts (az_cloud_concepts)
    # =====================================================================

    # ----- az_cloud_models --------------------------------------------------
    {
        "id": "az900-cc-r2-001", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "A colleague asks for a plain-language definition of cloud computing. Which "
                "statement is most accurate?",
        "options": [
            {"id": "A", "text": "A way to run software only on a single on-premises server"},
            {"id": "B", "text": "The delivery of computing services such as servers, storage, databases, "
                               "networking, and software over the internet"},
            {"id": "C", "text": "A physical datacenter that a company builds and owns"},
            {"id": "D", "text": "A programming language used to automate deployments"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cloud computing is the delivery of computing services (compute, storage, "
                       "databases, networking, software, and more) over the internet, typically billed "
                       "as you use them.",
            "distractors": {
                "A": "Running software on your own single server is local/on-premises computing, not cloud.",
                "C": "A company-owned physical datacenter is on-premises infrastructure, not the cloud.",
                "D": "That describes infrastructure-as-code tooling, not the definition of cloud computing.",
            },
            "exam_pattern": "Cloud computing = computing services delivered over the internet.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud computing"],
    },
    {
        "id": "az900-cc-r2-002", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "An organization runs some workloads on Microsoft Azure and others on a second public "
                "cloud provider at the same time. What is this arrangement called?",
        "options": [
            {"id": "A", "text": "Hybrid cloud"},
            {"id": "B", "text": "Private cloud"},
            {"id": "C", "text": "Multicloud"},
            {"id": "D", "text": "On-premises only"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Multicloud means using two or more public cloud providers at the same time.",
            "distractors": {
                "A": "Hybrid cloud combines a private/on-premises environment with a public cloud, not two public providers.",
                "B": "A private cloud is used exclusively by a single organization; it is not two public clouds.",
                "D": "On-premises means running in your own datacenter, with no public cloud at all.",
            },
            "exam_pattern": "Two or more public cloud providers together = multicloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud deployment models"],
    },
    {
        "id": "az900-cc-r2-003", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following is an example of operational expenditure (OpEx) rather than "
                "capital expenditure (CapEx)?",
        "options": [
            {"id": "A", "text": "Buying physical servers for a datacenter up front"},
            {"id": "B", "text": "Purchasing networking hardware to own"},
            {"id": "C", "text": "Constructing a new datacenter building"},
            {"id": "D", "text": "Paying a monthly, usage-based fee for Azure services"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A recurring, usage-based charge such as a monthly pay-as-you-go cloud fee is "
                       "operational expenditure (OpEx).",
            "distractors": {
                "A": "Buying servers up front is a one-time purchase of an owned asset - capital expenditure.",
                "B": "Purchasing hardware you own and depreciate is capital expenditure.",
                "C": "Building a datacenter is a large up-front capital expenditure.",
            },
            "exam_pattern": "Ongoing pay-for-use charges = OpEx; up-front owned assets = CapEx.",
        },
        "references": ["Microsoft Learn (AZ-900): Compare cloud pricing (CapEx vs OpEx)"],
    },
    {
        "id": "az900-cc-r2-004", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A startup with limited cash wants to avoid a large up-front hardware purchase and "
                "instead pay for computing as it grows. Which model best meets this need?",
        "options": [
            {"id": "A", "text": "A capital-expenditure (CapEx) model"},
            {"id": "B", "text": "The cloud's operational-expenditure (OpEx), pay-as-you-go model"},
            {"id": "C", "text": "Building a private on-premises datacenter"},
            {"id": "D", "text": "A one-time perpetual hardware purchase"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The cloud's consumption-based OpEx model lets the startup avoid up-front capital "
                       "and pay only for what it uses as it scales.",
            "distractors": {
                "A": "A CapEx model requires exactly the large up-front investment the startup wants to avoid.",
                "C": "Building an on-premises datacenter is a major capital expense.",
                "D": "A one-time perpetual hardware purchase is an up-front CapEx outlay.",
            },
            "exam_pattern": "Avoid up-front cost, pay as you grow = cloud OpEx / pay-as-you-go.",
        },
        "references": ["Microsoft Learn (AZ-900): Compare cloud pricing (CapEx vs OpEx)"],
    },
    {
        "id": "az900-cc-r2-005", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "A manager claims a private cloud must always be located in the company's own "
                "on-premises datacenter. Which statement correctly clarifies this?",
        "options": [
            {"id": "A", "text": "Correct - a private cloud can only ever run on-premises"},
            {"id": "B", "text": "A private cloud is always multi-tenant and shared with other companies"},
            {"id": "C", "text": "A private cloud is defined by exclusive use by a single organization; it can be "
                               "hosted on-premises or by a third-party provider"},
            {"id": "D", "text": "A private cloud is just another name for the public cloud"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "What defines a private cloud is exclusive, single-organization use of the "
                       "resources; it can be hosted in the company's own datacenter or by a third party.",
            "distractors": {
                "A": "Location is not the defining trait; a private cloud can be hosted by a third party.",
                "B": "A private cloud is single-tenant (exclusive), not multi-tenant/shared.",
                "D": "The public cloud is shared and multi-tenant - the opposite of a private cloud.",
            },
            "exam_pattern": "Private cloud = exclusive single-org use, regardless of where it is hosted.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud deployment models"],
    },
    {
        "id": "az900-cc-r2-006", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Under the consumption-based model, what financial advantage does a team get when "
                "demand for an application drops?",
        "options": [
            {"id": "A", "text": "It can scale resources down and stop paying for capacity it no longer uses"},
            {"id": "B", "text": "It is locked into paying the original peak amount for a full year"},
            {"id": "C", "text": "It must pay a penalty for reducing capacity"},
            {"id": "D", "text": "Its costs are fixed and unaffected by usage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Because you pay only for what you use, scaling down when demand falls reduces "
                       "what you pay - you stop paying for capacity you release.",
            "distractors": {
                "B": "Consumption billing is not a fixed annual peak charge; spend follows usage.",
                "C": "There is no penalty for scaling down in the consumption model.",
                "D": "Costs are not fixed; they rise and fall with actual usage.",
            },
            "exam_pattern": "Consumption model = scale down and pay less when demand drops.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the consumption-based model"],
    },
    {
        "id": "az900-cc-r2-007", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "In the shared responsibility model, some duties are always the provider's, some always "
                "the customer's, and some shift depending on the service type. Which responsibility is "
                "in the 'depends on the service type' group?",
        "options": [
            {"id": "A", "text": "Physical security of the datacenter"},
            {"id": "B", "text": "The organization's information and data"},
            {"id": "C", "text": "The physical host servers"},
            {"id": "D", "text": "The operating system"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Responsibility for the operating system (along with applications, network controls, "
                       "and identity/directory infrastructure) shifts between customer and provider "
                       "depending on whether the service is IaaS, PaaS, or SaaS.",
            "distractors": {
                "A": "Physical datacenter security is always the provider's responsibility.",
                "B": "Information and data are always the customer's responsibility.",
                "C": "The physical host servers are always the provider's responsibility.",
            },
            "exam_pattern": "Always-provider (physical) + always-customer (data/identities) + varies (OS/apps/network).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the shared responsibility model"],
    },
    {
        "id": "az900-cc-r2-008", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "What distinguishes a hybrid cloud from a multicloud deployment?",
        "options": [
            {"id": "A", "text": "Hybrid uses two or more public cloud providers; multicloud uses only one"},
            {"id": "B", "text": "Hybrid combines a private/on-premises environment with a public cloud, while "
                               "multicloud uses two or more public cloud providers"},
            {"id": "C", "text": "They are two names for exactly the same thing"},
            {"id": "D", "text": "Hybrid means on-premises only, with no public cloud involved"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Hybrid combines a private/on-premises environment with a public cloud; multicloud "
                       "means using two or more public cloud providers.",
            "distractors": {
                "A": "This reverses the definitions - that description of 'hybrid' is actually multicloud.",
                "C": "They are distinct concepts, not synonyms.",
                "D": "Hybrid, by definition, includes a public cloud alongside the private/on-premises part.",
            },
            "exam_pattern": "Hybrid = private/on-prem + public; multicloud = multiple public clouds.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud deployment models"],
    },

    # ----- az_cloud_benefits ------------------------------------------------
    {
        "id": "az900-cc-r2-009", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A business wants to provision new computing resources in minutes to seize a market "
                "opportunity, instead of waiting weeks to procure hardware. Which cloud benefit does "
                "this describe?",
        "options": [
            {"id": "A", "text": "Agility"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Capital expenditure"},
            {"id": "D", "text": "Data residency"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Agility is the ability to rapidly provision and deploy resources, cutting the time "
                       "from idea to running service.",
            "distractors": {
                "B": "Governance is about enforcing standards and compliance, not speed of provisioning.",
                "C": "Capital expenditure is a spending type, not a benefit of fast provisioning.",
                "D": "Data residency concerns where data is stored, not how quickly resources are deployed.",
            },
            "exam_pattern": "Rapidly provision/deploy to move fast = agility.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of using cloud services"],
    },
    {
        "id": "az900-cc-r2-010", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "To prepare for a major regional outage, a company replicates its systems and data to a "
                "second Azure region so it can recover and resume operations. Which capability is this?",
        "options": [
            {"id": "A", "text": "Vertical scaling"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Disaster recovery"},
            {"id": "D", "text": "Economies of scale"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Disaster recovery is the ability to recover from a significant event, such as a "
                       "regional outage, often by replicating to another region.",
            "distractors": {
                "A": "Vertical scaling resizes a single resource; it does not provide regional recovery.",
                "B": "Single sign-on is an identity convenience, unrelated to recovering from outages.",
                "D": "Economies of scale is about lower unit cost from scale, not recovery.",
            },
            "exam_pattern": "Recover and resume after a major/regional failure = disaster recovery.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of reliability and predictability"],
    },
    {
        "id": "az900-cc-r2-011", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A system is designed so that if one component fails, it keeps operating without "
                "interruption. Which characteristic does this describe?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Fault tolerance"},
            {"id": "C", "text": "Agility"},
            {"id": "D", "text": "Consumption-based pricing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Fault tolerance is the ability to keep running despite the failure of a component, "
                       "typically through redundancy.",
            "distractors": {
                "A": "Elasticity is automatically matching capacity to demand, not surviving a failure.",
                "C": "Agility is how quickly you can provision resources, not resilience to failure.",
                "D": "Consumption-based pricing is a cost model, not a resilience property.",
            },
            "exam_pattern": "Keep operating despite a component failure = fault tolerance.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-r2-012", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 3, "type": "mcq",
        "stem": "A team plans ahead to add capacity so an application can handle a known, steady "
                "increase in users over the next year. Which term best fits adding capacity to handle "
                "growth, as opposed to automatic, real-time, demand-driven adjustment?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Fault tolerance"},
            {"id": "C", "text": "Disaster recovery"},
            {"id": "D", "text": "Scalability"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Scalability is the ability to increase (or decrease) resources to meet demand, such "
                       "as planning added capacity for expected growth.",
            "distractors": {
                "A": "Elasticity emphasizes automatically adjusting capacity in real time as demand changes.",
                "B": "Fault tolerance is about surviving component failures, not adding capacity for growth.",
                "C": "Disaster recovery is about recovering after a major outage, not scaling for growth.",
            },
            "exam_pattern": "Add capacity for growth = scalability; automatic real-time adjustment = elasticity.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-r2-013", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "Because a cloud provider buys computing hardware in enormous volumes, it can offer "
                "services at a lower per-unit price than a single company could achieve alone. Which "
                "cloud advantage is this?",
        "options": [
            {"id": "A", "text": "Economies of scale"},
            {"id": "B", "text": "Fault tolerance"},
            {"id": "C", "text": "Governance"},
            {"id": "D", "text": "Elasticity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Economies of scale lets a provider buy at huge volume and pass lower per-unit "
                       "costs to customers - something a single organization cannot match.",
            "distractors": {
                "B": "Fault tolerance is about surviving failures, not lower unit cost.",
                "C": "Governance is about enforcing standards and compliance, not pricing from volume.",
                "D": "Elasticity is automatic scaling with demand, not bulk-purchasing savings.",
            },
            "exam_pattern": "Lower unit cost from buying at huge volume = economies of scale.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of using cloud services"],
    },
    {
        "id": "az900-cc-r2-014", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "An architect deploys duplicate copies of each critical component so that no single "
                "failure can take the application offline. What is this design practice called?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Redundancy"},
            {"id": "C", "text": "Vertical scaling"},
            {"id": "D", "text": "Consumption-based pricing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Redundancy means duplicating components so there is no single point of failure; it "
                       "underpins high availability and fault tolerance.",
            "distractors": {
                "A": "Elasticity is automatic scaling with demand, not duplicating components.",
                "C": "Vertical scaling resizes a single resource; it does not add duplicate copies.",
                "D": "Consumption-based pricing is a cost model, not a resilience design.",
            },
            "exam_pattern": "Duplicate components, no single point of failure = redundancy.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of high availability and scalability"],
    },
    {
        "id": "az900-cc-r2-015", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Beyond letting the provider patch managed services, which of the following is a genuine "
                "security benefit of using a major cloud platform?",
        "options": [
            {"id": "A", "text": "It removes the customer's responsibility for their own data and identities"},
            {"id": "B", "text": "It guarantees that no security incident can ever occur"},
            {"id": "C", "text": "It provides built-in, centrally managed security features such as threat "
                               "detection and DDoS protection"},
            {"id": "D", "text": "It eliminates the need for any access controls"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Cloud platforms offer built-in, centrally managed security capabilities (for "
                       "example, threat detection and DDoS protection) that strengthen a workload's posture.",
            "distractors": {
                "A": "Data and identities always remain the customer's responsibility under shared responsibility.",
                "B": "No provider can guarantee that no incident will ever occur.",
                "D": "Access controls are still required; security is shared, not eliminated.",
            },
            "exam_pattern": "Built-in, centralized protections (threat detection, DDoS) = cloud security benefit.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of security and governance"],
    },
    {
        "id": "az900-cc-r2-016", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_cloud_benefits", "difficulty": 3, "type": "mcq",
        "stem": "Which statement correctly contrasts high availability with disaster recovery?",
        "options": [
            {"id": "A", "text": "High availability minimizes downtime during normal operations, while disaster "
                               "recovery restores service after a major, often regional, failure"},
            {"id": "B", "text": "High availability and disaster recovery are identical concepts"},
            {"id": "C", "text": "Disaster recovery keeps an app online during routine component failures, while "
                               "high availability is only for region-wide disasters"},
            {"id": "D", "text": "High availability is a billing model and disaster recovery is a networking service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "High availability keeps a system running with minimal downtime in normal operation; "
                       "disaster recovery is about recovering service after a major, often regional, event.",
            "distractors": {
                "B": "They are related but distinct goals, not the same thing.",
                "C": "This reverses the two concepts.",
                "D": "Neither is a billing model or a networking service.",
            },
            "exam_pattern": "HA = minimize everyday downtime; DR = recover after a major disaster.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the benefits of reliability and predictability"],
    },

    # ----- az_service_types -------------------------------------------------
    {
        "id": "az900-cc-r2-017", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "Which Azure offering is a classic example of Infrastructure as a Service (IaaS)?",
        "options": [
            {"id": "A", "text": "Microsoft 365"},
            {"id": "B", "text": "Azure Virtual Machines"},
            {"id": "C", "text": "Azure SQL Database (a fully managed database)"},
            {"id": "D", "text": "A ready-to-use, vendor-managed CRM application"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Virtual Machines is IaaS: you get virtualized infrastructure and manage the "
                       "operating system and software, while the provider runs the hardware.",
            "distractors": {
                "A": "Microsoft 365 is finished software delivered as SaaS.",
                "C": "A fully managed database is PaaS - the provider manages the OS and platform.",
                "D": "A ready-to-use managed application is SaaS.",
            },
            "exam_pattern": "VMs / virtual infrastructure you manage the OS on = IaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },
    {
        "id": "az900-cc-r2-018", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "Which option is an example of Platform as a Service (PaaS), where the provider manages "
                "the operating system and you build on top of it?",
        "options": [
            {"id": "A", "text": "An Azure virtual machine that you patch yourself"},
            {"id": "B", "text": "Microsoft 365"},
            {"id": "C", "text": "Azure App Service"},
            {"id": "D", "text": "A laptop running a locally installed application"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Azure App Service is PaaS: the provider manages the operating system and platform, "
                       "and you deploy your application on top.",
            "distractors": {
                "A": "A VM you patch yourself is IaaS, not PaaS.",
                "B": "Microsoft 365 is finished software, which is SaaS.",
                "D": "A locally installed application is on-premises/local computing, not a cloud service type.",
            },
            "exam_pattern": "Provider manages the OS/platform, you deploy your app = PaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - PaaS"],
    },
    {
        "id": "az900-cc-r2-019", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 1, "type": "mcq",
        "stem": "Which option is an example of Software as a Service (SaaS)?",
        "options": [
            {"id": "A", "text": "Azure Virtual Machines"},
            {"id": "B", "text": "A virtual network you configure yourself"},
            {"id": "C", "text": "An Azure Kubernetes Service cluster you manage"},
            {"id": "D", "text": "Microsoft 365"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft 365 is SaaS: complete, provider-managed software that users simply sign "
                       "in to and use.",
            "distractors": {
                "A": "Azure Virtual Machines is IaaS, where you manage the operating system.",
                "B": "Configuring your own virtual network is infrastructure management, not finished software.",
                "C": "Managing a Kubernetes cluster is a platform/infrastructure task, not consuming finished software.",
            },
            "exam_pattern": "Finished, provider-managed application you just use = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - SaaS"],
    },
    {
        "id": "az900-cc-r2-020", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "Across IaaS, PaaS, and SaaS, in which service type does the customer have the MOST "
                "management responsibility?",
        "options": [
            {"id": "A", "text": "IaaS"},
            {"id": "B", "text": "PaaS"},
            {"id": "C", "text": "SaaS"},
            {"id": "D", "text": "Responsibility is identical in all three"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In IaaS the customer manages the most - the operating system, runtime, "
                       "applications, and data - while the provider runs only the physical infrastructure.",
            "distractors": {
                "B": "In PaaS the provider manages the OS and platform, so the customer manages less than in IaaS.",
                "C": "SaaS is where the customer manages the least.",
                "D": "Responsibility clearly differs across the three service types.",
            },
            "exam_pattern": "Most customer responsibility = IaaS; least = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types"],
    },
    {
        "id": "az900-cc-r2-021", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 1, "type": "mcq",
        "stem": "A company wants the service type where the provider manages the most and the customer "
                "manages the least. Which should it choose?",
        "options": [
            {"id": "A", "text": "IaaS"},
            {"id": "B", "text": "PaaS"},
            {"id": "C", "text": "SaaS"},
            {"id": "D", "text": "On-premises hosting"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "SaaS places the most responsibility on the provider; the customer mainly manages "
                       "its data, accounts, and access.",
            "distractors": {
                "A": "IaaS puts the most responsibility on the customer, not the least.",
                "B": "PaaS is in the middle - the customer still manages the application.",
                "D": "On-premises means the customer manages everything, including the hardware.",
            },
            "exam_pattern": "Provider manages the most, customer the least = SaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - SaaS"],
    },
    {
        "id": "az900-cc-r2-022", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 2, "type": "mcq",
        "stem": "When using a PaaS offering, which responsibilities does the customer still retain?",
        "options": [
            {"id": "A", "text": "Patching the underlying operating system"},
            {"id": "B", "text": "The application and data it builds, plus its user accounts and identities"},
            {"id": "C", "text": "Maintaining the physical servers"},
            {"id": "D", "text": "Securing the physical datacenter"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In PaaS the provider manages the OS and platform, but the customer still owns the "
                       "application and data it builds, and always its accounts/identities.",
            "distractors": {
                "A": "Patching the operating system is the provider's job in PaaS.",
                "C": "Physical servers are always maintained by the provider.",
                "D": "Physical datacenter security is always the provider's responsibility.",
            },
            "exam_pattern": "PaaS: customer keeps app, data, and identities; provider handles OS and below.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - PaaS"],
    },
    {
        "id": "az900-cc-r2-023", "exam": "az900", "domain": "az_cloud_concepts",
        "subtopic": "az_service_types", "difficulty": 3, "type": "mcq",
        "stem": "A workload is moved from a PaaS platform to running on IaaS virtual machines instead. "
                "Which responsibility now returns to the customer?",
        "options": [
            {"id": "A", "text": "Physical datacenter security"},
            {"id": "B", "text": "Ownership of the physical host hardware"},
            {"id": "C", "text": "Classifying and protecting the company's own data"},
            {"id": "D", "text": "Patching and managing the operating system"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Moving from PaaS to IaaS returns operating-system management (including patching) "
                       "to the customer, because IaaS gives OS-level control.",
            "distractors": {
                "A": "Physical datacenter security remains the provider's in every service type.",
                "B": "The physical host hardware is always the provider's, never the customer's.",
                "C": "Data was always the customer's responsibility, so it does not 'return'.",
            },
            "exam_pattern": "PaaS -> IaaS: the operating system becomes the customer's responsibility again.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cloud service types - IaaS"],
    },

    # =====================================================================
    # DOMAIN 2 - Azure Architecture and Services (az_architecture_services)
    # =====================================================================

    # ----- az_core_architecture ---------------------------------------------
    {
        "id": "az900-arch-r2-001", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "In fundamentals terms, what is an Azure availability zone?",
        "options": [
            {"id": "A", "text": "A geographic area aligned to a country for data residency"},
            {"id": "B", "text": "A logical container that holds related resources"},
            {"id": "C", "text": "One or more physically separate datacenters within a region, each with "
                               "independent power, cooling, and networking"},
            {"id": "D", "text": "A pair of regions used for geo-redundant replication"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An availability zone is one or more physically separate datacenters within a "
                       "single region, each with independent power, cooling, and networking.",
            "distractors": {
                "A": "A geographic area for data residency is an Azure geography, not a zone.",
                "B": "A logical container for related resources is a resource group.",
                "D": "A pair of regions for geo-redundancy is a region pair, not an availability zone.",
            },
            "exam_pattern": "Physically separate datacenters within one region = availability zone.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions, availability zones, and region pairs"],
    },
    {
        "id": "az900-arch-r2-002", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 1, "type": "mcq",
        "stem": "Which statement best describes an Azure subscription?",
        "options": [
            {"id": "A", "text": "A logical unit of Azure services linked to an account that acts as a billing "
                               "and access-management boundary"},
            {"id": "B", "text": "A physically separate datacenter within a region"},
            {"id": "C", "text": "A command-line tool for managing Azure"},
            {"id": "D", "text": "An encrypted tunnel from on-premises to Azure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A subscription is a logical container of Azure services tied to an account; it acts "
                       "as a boundary for billing and for access management.",
            "distractors": {
                "B": "A physically separate datacenter within a region is an availability zone.",
                "C": "A command-line management tool is the Azure CLI, not a subscription.",
                "D": "An encrypted tunnel from on-premises to Azure is a VPN connection.",
            },
            "exam_pattern": "Subscription = logical unit + billing/access boundary.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure subscriptions"],
    },
    {
        "id": "az900-arch-r2-003", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Besides separating invoices, why might an organization create multiple Azure "
                "subscriptions?",
        "options": [
            {"id": "A", "text": "Because a single resource can belong to several subscriptions at once"},
            {"id": "B", "text": "To separate environments (such as development and production) and to work "
                               "within per-subscription limits"},
            {"id": "C", "text": "Because a subscription is required before you can define a subnet"},
            {"id": "D", "text": "To avoid ever needing resource groups"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Multiple subscriptions help separate environments and workloads, apply different "
                       "access/management boundaries, and stay within per-subscription limits.",
            "distractors": {
                "A": "A resource belongs to exactly one subscription, not several at once.",
                "C": "Subnets are defined inside a virtual network; they are not a reason for extra subscriptions.",
                "D": "Resource groups are still used within every subscription.",
            },
            "exam_pattern": "Multiple subscriptions = separate environments, access boundaries, and limits.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure subscriptions"],
    },
    {
        "id": "az900-arch-r2-004", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "A policy and several role assignments are applied to an Azure management group. What "
                "happens to the subscriptions contained in that management group?",
        "options": [
            {"id": "A", "text": "They ignore the settings unless each setting is re-applied individually"},
            {"id": "B", "text": "Only brand-new resources are affected; existing subscriptions are exempt"},
            {"id": "C", "text": "The settings apply only to the management group object itself"},
            {"id": "D", "text": "They inherit the applied conditions, which cascade down to their resources"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Conditions applied at a management group (such as policy and RBAC) are inherited by "
                       "the subscriptions beneath it and cascade down to their resources.",
            "distractors": {
                "A": "Inheritance is automatic; you do not re-apply the settings to each subscription.",
                "B": "Inheritance applies to the subscriptions regardless of when they were created.",
                "C": "The point of a management group is to govern the subscriptions inside it, not just itself.",
            },
            "exam_pattern": "Management group settings are inherited by child subscriptions and resources.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe management groups"],
    },
    {
        "id": "az900-arch-r2-005", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 1, "type": "mcq",
        "stem": "In Azure, which of the following is the best definition of a 'resource'?",
        "options": [
            {"id": "A", "text": "A manageable item available through Azure, such as a virtual machine, "
                               "storage account, or virtual network"},
            {"id": "B", "text": "A geographic area that contains datacenters"},
            {"id": "C", "text": "The billing boundary for an entire organization"},
            {"id": "D", "text": "A query language used to search log data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A resource is a manageable item available through Azure - for example a VM, "
                       "storage account, virtual network, or web app.",
            "distractors": {
                "B": "A geographic area containing datacenters is a region (or geography).",
                "C": "An organization-wide billing boundary is a subscription (or account).",
                "D": "A query language for logs is KQL, used in Log Analytics.",
            },
            "exam_pattern": "Resource = a manageable Azure item (VM, storage account, VNet, ...).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups and resources"],
    },
    {
        "id": "az900-arch-r2-006", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Beyond processing deployment requests, which capabilities does Azure Resource Manager "
                "(ARM) make possible across your resources?",
        "options": [
            {"id": "A", "text": "Only manual creation of one resource at a time through the portal"},
            {"id": "B", "text": "Organizing resources into resource groups, applying tags, assigning RBAC, "
                               "setting resource locks, and deploying from templates"},
            {"id": "C", "text": "Hosting your public DNS domain records"},
            {"id": "D", "text": "Providing a global content delivery network"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ARM is the consistent management layer that enables grouping, tagging, RBAC, "
                       "resource locks, and repeatable template-based deployment across all tools.",
            "distractors": {
                "A": "ARM enables consistent, automatable management - not just one-at-a-time manual work.",
                "C": "Hosting DNS records is the job of Azure DNS, not ARM.",
                "D": "A global content delivery network is Azure CDN, not ARM.",
            },
            "exam_pattern": "ARM = one management layer for grouping, tags, RBAC, locks, and templates.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Resource Manager and resource groups"],
    },
    {
        "id": "az900-arch-r2-007", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "When choosing which Azure region to deploy a workload in, which set of factors is most "
                "relevant?",
        "options": [
            {"id": "A", "text": "The resource's name and the tags applied to it"},
            {"id": "B", "text": "The number of resource groups already in the subscription"},
            {"id": "C", "text": "Proximity to users (latency), service availability in the region, price, and "
                               "compliance/data-residency requirements"},
            {"id": "D", "text": "The color theme selected in the Azure portal"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Region choice is driven by proximity to users (latency), which services/features "
                       "are available there, pricing, and compliance/data-residency needs.",
            "distractors": {
                "A": "A resource's name and tags do not determine which region is appropriate.",
                "B": "The count of resource groups is irrelevant to region selection.",
                "D": "Portal appearance has no bearing on where to deploy.",
            },
            "exam_pattern": "Region selection = latency/proximity, availability, price, compliance/residency.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions"],
    },
    {
        "id": "az900-arch-r2-008", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Several Azure services can replicate data to a region's paired region. What is the main "
                "benefit of this region pairing?",
        "options": [
            {"id": "A", "text": "It lets a single resource belong to two resource groups"},
            {"id": "B", "text": "It reduces the price of the resources"},
            {"id": "C", "text": "It allows a resource to skip authentication"},
            {"id": "D", "text": "It provides geo-redundancy so data and workloads can be recovered if the "
                               "primary region has a major outage"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Region pairs provide geo-redundancy: many services replicate to the paired region "
                       "so data and workloads can be recovered after a major regional outage.",
            "distractors": {
                "A": "Region pairing has nothing to do with resource-group membership.",
                "B": "Pairing is a resiliency feature, not a pricing discount.",
                "C": "Pairing does not affect authentication.",
            },
            "exam_pattern": "Region pairs = geo-redundancy and regional disaster recovery.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions and region pairs"],
    },

    # ----- az_compute_networking --------------------------------------------
    {
        "id": "az900-arch-r2-009", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "A company wants employees to access a full Windows desktop and their applications "
                "remotely from any device, hosted and managed in Azure. Which service provides this "
                "desktop and app virtualization?",
        "options": [
            {"id": "A", "text": "Azure Virtual Desktop"},
            {"id": "B", "text": "Azure Functions"},
            {"id": "C", "text": "Azure Blob Storage"},
            {"id": "D", "text": "Azure DNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Virtual Desktop is a desktop and application virtualization service that "
                       "runs Windows desktops and apps in Azure for remote access from any device.",
            "distractors": {
                "B": "Azure Functions runs event-driven code, not virtual desktops.",
                "C": "Azure Blob Storage stores objects; it does not deliver desktops.",
                "D": "Azure DNS resolves names and is unrelated to desktop virtualization.",
            },
            "exam_pattern": "Cloud-hosted Windows desktops/apps accessed remotely = Azure Virtual Desktop.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Virtual Desktop"],
    },
    {
        "id": "az900-arch-r2-010", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Two Azure virtual networks must communicate privately with each other over Microsoft's "
                "backbone network, without traffic crossing the public internet. Which feature connects "
                "them?",
        "options": [
            {"id": "A", "text": "A public endpoint"},
            {"id": "B", "text": "Azure Load Balancer"},
            {"id": "C", "text": "Virtual network peering"},
            {"id": "D", "text": "An availability set"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Virtual network peering links two VNets so their resources communicate privately "
                       "over the Microsoft backbone, not the public internet.",
            "distractors": {
                "A": "A public endpoint is internet-facing, the opposite of private peering.",
                "B": "A load balancer distributes traffic to backend VMs; it does not join two VNets.",
                "D": "An availability set spreads VMs for resiliency; it does not connect networks.",
            },
            "exam_pattern": "Privately connect two VNets over Microsoft's backbone = VNet peering.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure virtual networking"],
    },
    {
        "id": "az900-arch-r2-011", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Incoming traffic to an application must be evenly distributed across a pool of identical "
                "backend virtual machines. Which Azure networking service does this?",
        "options": [
            {"id": "A", "text": "Azure DNS"},
            {"id": "B", "text": "Azure Load Balancer"},
            {"id": "C", "text": "VPN Gateway"},
            {"id": "D", "text": "A private endpoint"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Load Balancer distributes incoming traffic across a pool of backend VMs to "
                       "spread load and improve availability.",
            "distractors": {
                "A": "Azure DNS resolves domain names; it does not distribute traffic across VMs.",
                "C": "A VPN Gateway provides encrypted connectivity, not load distribution.",
                "D": "A private endpoint gives a PaaS service a private IP; it does not balance traffic.",
            },
            "exam_pattern": "Distribute inbound traffic across backend VMs = Azure Load Balancer.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure virtual networking"],
    },
    {
        "id": "az900-arch-r2-012", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "Which statement best describes an Azure virtual network (VNet)?",
        "options": [
            {"id": "A", "text": "A physical cable that connects on-premises hardware to Azure"},
            {"id": "B", "text": "A fully managed relational database"},
            {"id": "C", "text": "A command-line tool for deployments"},
            {"id": "D", "text": "A logically isolated private network in Azure that lets resources securely "
                               "communicate with each other, the internet, and on-premises networks"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A VNet is a logically isolated, software-defined private network in Azure in which "
                       "resources can securely communicate with each other, the internet, and on-premises.",
            "distractors": {
                "A": "A VNet is logical/software-defined, not a physical cable.",
                "B": "A fully managed relational database is Azure SQL Database.",
                "C": "A command-line deployment tool is the Azure CLI, not a VNet.",
            },
            "exam_pattern": "Logically isolated private network for secure communication = VNet.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure virtual networking"],
    },
    {
        "id": "az900-arch-r2-013", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Compared with virtual machines, what is a key characteristic of containers?",
        "options": [
            {"id": "A", "text": "They are lightweight, share the host operating system's kernel, start quickly, "
                               "and package an app with its dependencies for portability"},
            {"id": "B", "text": "Each container must include its own full, separate guest operating system"},
            {"id": "C", "text": "Containers can only run on physical hardware, never in the cloud"},
            {"id": "D", "text": "Containers remove the need to write or deploy any application code"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Containers are lightweight, share the host OS kernel, start fast, and bundle an app "
                       "with its dependencies, making them portable across environments.",
            "distractors": {
                "B": "Including a full separate guest OS per instance describes virtual machines, not containers.",
                "C": "Containers run well in the cloud, for example via Azure Container Instances or AKS.",
                "D": "You still build and deploy the application code that runs inside the container.",
            },
            "exam_pattern": "Lightweight, share host OS kernel, portable = containers (vs full-OS VMs).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (containers)"],
    },
    {
        "id": "az900-arch-r2-014", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Which statement best describes serverless computing, such as Azure Functions?",
        "options": [
            {"id": "A", "text": "You must provision and patch the virtual machines that run the code"},
            {"id": "B", "text": "You do not manage the underlying servers; the platform scales automatically "
                               "and you pay only while your code runs"},
            {"id": "C", "text": "It requires a three-year capacity commitment to use"},
            {"id": "D", "text": "It can only run on-premises"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Serverless means you do not manage servers; the platform scales automatically and "
                       "you pay only for actual execution.",
            "distractors": {
                "A": "Serverless removes server provisioning and patching from your responsibilities.",
                "C": "Serverless has no long-term capacity commitment; it is consumption-based.",
                "D": "Serverless services run in the cloud, not on-premises only.",
            },
            "exam_pattern": "No servers to manage, auto-scaling, pay-per-execution = serverless.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (Azure Functions, serverless)"],
    },
    {
        "id": "az900-arch-r2-015", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "A single remote employee's laptop needs a secure, encrypted connection into an Azure "
                "virtual network from home. Which connectivity option fits this single-device scenario?",
        "options": [
            {"id": "A", "text": "ExpressRoute"},
            {"id": "B", "text": "A site-to-site VPN connecting a whole network"},
            {"id": "C", "text": "A point-to-site VPN"},
            {"id": "D", "text": "Virtual network peering"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A point-to-site VPN connects an individual client device securely into an Azure "
                       "virtual network, which fits a single remote laptop.",
            "distractors": {
                "A": "ExpressRoute provisions a dedicated private circuit, overkill for one device.",
                "B": "A site-to-site VPN connects an entire on-premises network, not a single device.",
                "D": "VNet peering connects two virtual networks, not a laptop to a VNet.",
            },
            "exam_pattern": "Single device into a VNet = point-to-site VPN; whole site = site-to-site.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure virtual networking (VPN Gateway)"],
    },
    {
        "id": "az900-arch-r2-016", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 3, "type": "mcq",
        "stem": "Which statement correctly contrasts Azure ExpressRoute with a VPN Gateway connection?",
        "options": [
            {"id": "A", "text": "ExpressRoute uses a private, dedicated connection that does not travel over "
                               "the public internet, while a VPN Gateway sends encrypted traffic across the "
                               "public internet"},
            {"id": "B", "text": "ExpressRoute sends encrypted traffic over the public internet, while a VPN "
                               "Gateway uses a private dedicated circuit"},
            {"id": "C", "text": "Both always travel over the public internet with no meaningful difference"},
            {"id": "D", "text": "Neither can connect on-premises networks to Azure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ExpressRoute is a private, dedicated connection that bypasses the public internet; "
                       "a VPN Gateway sends encrypted traffic across the public internet.",
            "distractors": {
                "B": "This reverses the two services.",
                "C": "They differ: ExpressRoute specifically avoids the public internet.",
                "D": "Both can connect on-premises networks to Azure; they just do it differently.",
            },
            "exam_pattern": "ExpressRoute = private dedicated (off-internet); VPN Gateway = encrypted over internet.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure virtual networking (ExpressRoute and VPN Gateway)"],
    },

    # ----- az_storage -------------------------------------------------------
    {
        "id": "az900-arch-r2-017", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "An application needs to store large amounts of structured, non-relational (NoSQL) data "
                "as key/attribute pairs with a schemaless design, at low cost. Which Azure Storage "
                "service fits?",
        "options": [
            {"id": "A", "text": "Blob storage"},
            {"id": "B", "text": "Table storage"},
            {"id": "C", "text": "Queue storage"},
            {"id": "D", "text": "Managed disks"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Table storage is a NoSQL key/attribute store for structured, non-relational "
                       "data with a schemaless design, at low cost.",
            "distractors": {
                "A": "Blob storage is an object store for unstructured data such as images and video.",
                "C": "Queue storage holds messages for asynchronous communication, not a data table.",
                "D": "Managed disks are block volumes attached to VMs, not a NoSQL table store.",
            },
            "exam_pattern": "Structured NoSQL key/attribute (schemaless) data = Table storage.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services"],
    },
    {
        "id": "az900-arch-r2-018", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 3, "type": "mcq",
        "stem": "Data is rarely accessed, but when it is needed it must be retrieved immediately (not "
                "after hours of rehydration), and it should cost less to store than the cool tier. Which "
                "blob access tier fits?",
        "options": [
            {"id": "A", "text": "Hot"},
            {"id": "B", "text": "Archive"},
            {"id": "C", "text": "Cold"},
            {"id": "D", "text": "Premium"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The cold tier is an online tier for rarely accessed data that still needs immediate "
                       "retrieval; its storage cost is lower than cool (with higher access costs).",
            "distractors": {
                "A": "The hot tier is for frequently accessed data and has the highest storage cost.",
                "B": "The archive tier is offline and requires rehydration (potentially hours), so it cannot return data immediately.",
                "D": "'Premium' is a storage-account performance tier, not one of the hot/cool/cold/archive access tiers.",
            },
            "exam_pattern": "Rarely accessed but instantly retrievable, cheaper than cool = cold tier.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage access tiers"],
    },
    {
        "id": "az900-arch-r2-019", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "Monthly backups are accessed only occasionally but must stay immediately available when "
                "needed, and are expected to be kept for at least 30 days. Which blob access tier is the "
                "best fit?",
        "options": [
            {"id": "A", "text": "Cool"},
            {"id": "B", "text": "Hot"},
            {"id": "C", "text": "Archive"},
            {"id": "D", "text": "Blobs cannot be tiered at all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The cool tier is an online tier optimized for infrequently accessed data that still "
                       "needs immediate availability, with a recommended minimum retention around 30 days.",
            "distractors": {
                "B": "The hot tier targets frequently accessed data and carries the highest storage cost.",
                "C": "The archive tier is offline and must be rehydrated before reading, so it is not immediately available.",
                "D": "Blobs can be placed in hot, cool, cold, or archive tiers.",
            },
            "exam_pattern": "Infrequent access but still immediately available = cool tier.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage access tiers"],
    },
    {
        "id": "az900-arch-r2-020", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 3, "type": "mcq",
        "stem": "An application must be able to READ data from the secondary (paired) region, not just "
                "have it replicated there. Which redundancy option provides read access to the secondary "
                "region?",
        "options": [
            {"id": "A", "text": "Locally redundant storage (LRS)"},
            {"id": "B", "text": "Zone-redundant storage (ZRS)"},
            {"id": "C", "text": "Geo-redundant storage (GRS) without read access"},
            {"id": "D", "text": "Read-access geo-redundant storage (RA-GRS)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "RA-GRS replicates to the paired secondary region and also grants read access to the "
                       "secondary, so applications can read from it.",
            "distractors": {
                "A": "LRS keeps all copies in a single datacenter, with no secondary region at all.",
                "B": "ZRS replicates across zones within one region; it has no secondary region.",
                "C": "Standard GRS replicates to the secondary region, but the secondary is not readable unless read access (RA) is enabled.",
            },
            "exam_pattern": "Read from the secondary region = RA-GRS (read-access geo-redundant).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage redundancy"],
    },
    {
        "id": "az900-arch-r2-021", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 1, "type": "mcq",
        "stem": "What is an Azure storage account?",
        "options": [
            {"id": "A", "text": "A geographic grouping of datacenters"},
            {"id": "B", "text": "A container that groups Azure Storage services (blob, file, queue, table) "
                               "under a single namespace and provides a unique endpoint for your data"},
            {"id": "C", "text": "An RBAC role that grants users read access"},
            {"id": "D", "text": "A fully managed relational database"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A storage account groups the Azure Storage data services under one namespace and "
                       "gives your data a unique, addressable endpoint.",
            "distractors": {
                "A": "A geographic grouping of datacenters is an Azure geography, not a storage account.",
                "C": "An RBAC role grants permissions; it is not a storage account.",
                "D": "A fully managed relational database is Azure SQL Database, not a storage account.",
            },
            "exam_pattern": "Storage account = namespace/endpoint grouping blob, file, queue, and table services.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage accounts"],
    },
    {
        "id": "az900-arch-r2-022", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "A team wants a fully managed relational SQL database in Azure where Microsoft handles "
                "patching, backups, and the underlying operating system. Which service fits?",
        "options": [
            {"id": "A", "text": "Azure Cosmos DB"},
            {"id": "B", "text": "SQL Server installed on an Azure virtual machine"},
            {"id": "C", "text": "Azure SQL Database"},
            {"id": "D", "text": "Azure Blob Storage"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Azure SQL Database is a fully managed (PaaS) relational database where Microsoft "
                       "handles patching, backups, and the operating system.",
            "distractors": {
                "A": "Azure Cosmos DB is a NoSQL/multi-model database, not a managed relational SQL database.",
                "B": "SQL Server on an Azure VM is IaaS - you manage and patch the OS and SQL Server yourself.",
                "D": "Azure Blob Storage is object storage, not a relational database.",
            },
            "exam_pattern": "Fully managed relational SQL database (PaaS) = Azure SQL Database.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure database services"],
    },
    {
        "id": "az900-arch-r2-023", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "An application needs a globally distributed, low-latency NoSQL database that can "
                "replicate data across multiple regions and scale elastically. Which Azure service is "
                "designed for this?",
        "options": [
            {"id": "A", "text": "Azure Cosmos DB"},
            {"id": "B", "text": "Azure SQL Database"},
            {"id": "C", "text": "Azure Files"},
            {"id": "D", "text": "Azure Queue storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Cosmos DB is a globally distributed, multi-model NoSQL database offering "
                       "low-latency access, multi-region replication, and elastic scale.",
            "distractors": {
                "B": "Azure SQL Database is a managed relational database, not a globally distributed NoSQL store.",
                "C": "Azure Files provides managed file shares, not a distributed database.",
                "D": "Azure Queue storage holds messages for decoupling components, not database data.",
            },
            "exam_pattern": "Globally distributed, low-latency NoSQL, multi-region = Azure Cosmos DB.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure database services (Azure Cosmos DB)"],
    },
    {
        "id": "az900-arch-r2-024", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "A company must run a specific version of SQL Server with full control of the operating "
                "system and database configuration, accepting responsibility for patching both. Which "
                "option matches this (an IaaS approach)?",
        "options": [
            {"id": "A", "text": "Azure SQL Database (a PaaS service)"},
            {"id": "B", "text": "Azure Cosmos DB"},
            {"id": "C", "text": "Azure Table storage"},
            {"id": "D", "text": "SQL Server installed on an Azure virtual machine"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Running SQL Server on an Azure virtual machine is IaaS, giving full OS and database "
                       "control while making the customer responsible for patching both.",
            "distractors": {
                "A": "Azure SQL Database is PaaS and abstracts the OS away, removing that level of control.",
                "B": "Azure Cosmos DB is a managed NoSQL service, not self-managed SQL Server.",
                "C": "Azure Table storage is NoSQL key/attribute storage, not SQL Server at all.",
            },
            "exam_pattern": "Full OS + SQL control, you patch it = SQL Server on an Azure VM (IaaS).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure database services"],
    },

    # ----- az_identity ------------------------------------------------------
    {
        "id": "az900-arch-r2-025", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "Multi-factor authentication requires factors from at least two different categories. "
                "Which set correctly lists those categories?",
        "options": [
            {"id": "A", "text": "Something you buy, something you rent, something you build"},
            {"id": "B", "text": "A username, a device name, and an IP address"},
            {"id": "C", "text": "Something you know, something you have, and something you are"},
            {"id": "D", "text": "A password, a second password, and a third password"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MFA combines factors from different categories: something you know (password), "
                       "something you have (phone/token), and something you are (biometric).",
            "distractors": {
                "A": "These are not recognized authentication factor categories.",
                "B": "A username, device name, and IP address are identifiers, not independent factor categories.",
                "D": "Several passwords are all the same factor ('something you know'), so they are not multi-factor.",
            },
            "exam_pattern": "MFA categories = know, have, are (at least two different ones).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication methods (multi-factor authentication)"],
    },
    {
        "id": "az900-arch-r2-026", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "To improve security, an organization wants users to sign in without a password, using "
                "methods such as Windows Hello, a FIDO2 security key, or the Microsoft Authenticator app. "
                "What is this approach called?",
        "options": [
            {"id": "A", "text": "Passwordless authentication"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Passwordless authentication replaces the password with methods like Windows Hello, "
                       "FIDO2 security keys, or the Microsoft Authenticator app.",
            "distractors": {
                "B": "Single sign-on reduces repeated sign-ins but still typically relies on a credential such as a password.",
                "C": "Authorization decides what an identity may do; it is not a sign-in method.",
                "D": "A resource lock protects a resource from change or deletion; it is unrelated to sign-in.",
            },
            "exam_pattern": "Sign in with Windows Hello / FIDO2 / Authenticator, no password = passwordless.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication methods (passwordless)"],
    },
    {
        "id": "az900-arch-r2-027", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "A company wants its users to use one identity for both on-premises systems and cloud "
                "apps by synchronizing on-premises Active Directory accounts to Microsoft Entra ID. Which "
                "approach enables this hybrid identity?",
        "options": [
            {"id": "A", "text": "Deleting on-premises Active Directory entirely before any cloud use"},
            {"id": "B", "text": "Synchronizing identities with Microsoft Entra Connect"},
            {"id": "C", "text": "Storing user profile files in Blob storage"},
            {"id": "D", "text": "Applying a CanNotDelete lock to each user account"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Entra Connect (formerly Azure AD Connect) synchronizes on-premises "
                       "Active Directory accounts to Microsoft Entra ID, giving users one hybrid identity.",
            "distractors": {
                "A": "Hybrid identity keeps on-premises AD and synchronizes it; it does not require deleting AD.",
                "C": "Blob storage holds data objects; it does not synchronize identities.",
                "D": "Resource locks protect Azure resources, not identity synchronization.",
            },
            "exam_pattern": "Sync on-prem AD to Entra ID for one identity = Microsoft Entra Connect (hybrid identity).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra ID and hybrid identity"],
    },
    {
        "id": "az900-arch-r2-028", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 3, "type": "mcq",
        "stem": "Which statement correctly distinguishes Microsoft Entra ID roles from Azure role-based "
                "access control (RBAC) roles?",
        "options": [
            {"id": "A", "text": "They are the same thing with two different names"},
            {"id": "B", "text": "Entra ID roles control access to storage blobs, while Azure RBAC controls "
                               "user passwords"},
            {"id": "C", "text": "Azure RBAC manages identity settings such as creating users, while Entra "
                               "roles manage virtual machines"},
            {"id": "D", "text": "Entra ID roles manage identity and directory tasks (such as managing users "
                               "in Entra ID), while Azure RBAC controls access to Azure resources (such as "
                               "VMs and storage)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Entra ID roles govern identity/directory administration (for example, managing "
                       "users in Entra ID); Azure RBAC governs access to Azure resources such as VMs and storage.",
            "distractors": {
                "A": "They are two distinct role systems with different scopes.",
                "B": "This mis-assigns the responsibilities of each.",
                "C": "This reverses the two role systems.",
            },
            "exam_pattern": "Entra roles = manage identity/directory; Azure RBAC = manage Azure resources.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure identity, access, and security"],
    },
    {
        "id": "az900-arch-r2-029", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants to prompt for multi-factor authentication only when a sign-in "
                "looks risky (for example, from an unfamiliar location), rather than on every single "
                "sign-in. Which Microsoft Entra capability makes this possible?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "A resource lock"},
            {"id": "D", "text": "Locally redundant storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access evaluates signals such as location, device, and risk and then "
                       "applies controls - for example, requiring MFA only when a sign-in appears risky.",
            "distractors": {
                "B": "Single sign-on reduces repeated sign-ins; it does not evaluate risk signals.",
                "C": "A resource lock protects a resource; it has nothing to do with sign-in conditions.",
                "D": "Locally redundant storage is a data-redundancy option, unrelated to access policy.",
            },
            "exam_pattern": "Signal- and risk-based if-then access decisions = Conditional Access.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Conditional Access"],
    },
    {
        "id": "az900-arch-r2-030", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "To reduce help-desk calls, a company wants users to securely reset their own passwords "
                "after verifying their identity. Which Microsoft Entra feature provides this?",
        "options": [
            {"id": "A", "text": "Multi-factor authentication by itself"},
            {"id": "B", "text": "Self-service password reset (SSPR)"},
            {"id": "C", "text": "ExpressRoute"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Self-service password reset (SSPR) lets users reset their own passwords after "
                       "verifying their identity, reducing help-desk workload.",
            "distractors": {
                "A": "MFA adds verification but does not by itself let users reset their passwords.",
                "C": "ExpressRoute is a private connectivity service, unrelated to password reset.",
                "D": "Azure Policy governs resource configurations, not user password resets.",
            },
            "exam_pattern": "Users reset their own passwords securely = self-service password reset (SSPR).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra ID (self-service password reset)"],
    },

    # =====================================================================
    # DOMAIN 3 - Azure Management and Governance (az_management_governance)
    # =====================================================================

    # ----- az_cost_management -----------------------------------------------
    {
        "id": "az900-gov-r2-001", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A company already owns Windows Server and SQL Server licenses with Software Assurance. "
                "Which Azure option lets it use those existing licenses to reduce the cost of running "
                "those workloads in Azure?",
        "options": [
            {"id": "A", "text": "Azure Hybrid Benefit"},
            {"id": "B", "text": "Azure Spot Virtual Machines"},
            {"id": "C", "text": "An Azure Reservation"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Hybrid Benefit lets you apply existing on-premises Windows Server and SQL "
                       "Server licenses (with Software Assurance) to cut the cost of those workloads in Azure.",
            "distractors": {
                "B": "Spot VMs discount spare capacity; they do not reuse your existing licenses.",
                "C": "Reservations discount through a usage commitment, not by applying your licenses.",
                "D": "A resource lock protects a resource from change or deletion; it does not affect cost.",
            },
            "exam_pattern": "Reuse existing Windows/SQL Server licenses in Azure = Azure Hybrid Benefit.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (Azure Hybrid Benefit)"],
    },
    {
        "id": "az900-gov-r2-002", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A batch-processing job can tolerate being interrupted and restarted later. Which option "
                "offers deeply discounted compute using Azure's spare capacity, which can be reclaimed "
                "(evicted) when Azure needs it back?",
        "options": [
            {"id": "A", "text": "An Azure Reservation"},
            {"id": "B", "text": "Azure Hybrid Benefit"},
            {"id": "C", "text": "Azure Spot Virtual Machines"},
            {"id": "D", "text": "Pay-as-you-go with no changes"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Azure Spot Virtual Machines use spare capacity at a deep discount but can be "
                       "evicted when Azure needs the capacity, which suits interruptible jobs.",
            "distractors": {
                "A": "Reservations suit steady, always-on workloads with a one- or three-year commitment, not evictable spare capacity.",
                "B": "Azure Hybrid Benefit reuses existing licenses; it is not spare-capacity pricing.",
                "D": "Plain pay-as-you-go offers no spare-capacity discount.",
            },
            "exam_pattern": "Interruptible workload on cheap, evictable spare capacity = Spot VMs.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (Spot pricing)"],
    },
    {
        "id": "az900-gov-r2-003", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "A company's compute usage shifts between different VM types and regions, but it can "
                "commit to a steady hourly amount of spend for one to three years in exchange for a "
                "discount. Which option best fits this flexible commitment?",
        "options": [
            {"id": "A", "text": "An Azure Reservation for one specific VM size and region"},
            {"id": "B", "text": "An Azure savings plan for compute"},
            {"id": "C", "text": "Azure Spot Virtual Machines"},
            {"id": "D", "text": "Azure Hybrid Benefit"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An Azure savings plan for compute gives a discount in exchange for committing to a "
                       "steady hourly spend, with the benefit applying flexibly across eligible compute "
                       "services and regions.",
            "distractors": {
                "A": "A reservation commits to a specific resource type/region, so it is less flexible across changing VM types.",
                "C": "Spot VMs are interruptible spare capacity with no committed discount.",
                "D": "Azure Hybrid Benefit reuses licenses; it is not a spend commitment.",
            },
            "exam_pattern": "Flexible hourly-spend commitment across compute = Azure savings plan.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (savings plans and reservations)"],
    },
    {
        "id": "az900-gov-r2-004", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs to view and download the organization's Azure invoices and "
                "manage its payment method. Which area should they use?",
        "options": [
            {"id": "A", "text": "The Azure Pricing Calculator"},
            {"id": "B", "text": "Azure Advisor"},
            {"id": "C", "text": "Azure Policy"},
            {"id": "D", "text": "Cost Management + Billing (the billing experience)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The billing experience in Cost Management + Billing is where you view and download "
                       "invoices and manage payment methods.",
            "distractors": {
                "A": "The Pricing Calculator estimates costs before deployment; it does not show invoices.",
                "B": "Azure Advisor gives recommendations, not billing documents.",
                "C": "Azure Policy enforces resource rules; it does not handle invoices or payment.",
            },
            "exam_pattern": "View/download invoices and manage payment = Cost Management + Billing.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (Microsoft Cost Management + Billing)"],
    },
    {
        "id": "az900-gov-r2-005", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "A team applies tags to a resource group and assumes the resources inside automatically "
                "inherit them. Which statement is correct?",
        "options": [
            {"id": "A", "text": "Resources do not automatically inherit their resource group's tags; tags "
                               "must be applied to resources directly (for example, enforced with Azure Policy)"},
            {"id": "B", "text": "Resources always inherit every tag from their resource group automatically"},
            {"id": "C", "text": "Tags cannot be applied to individual resources at all"},
            {"id": "D", "text": "Tagging a resource group deletes the tags already on its resources"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tags are not inherited by default: a resource does not automatically take its "
                       "resource group's tags, so tags must be applied to resources (Azure Policy can enforce this).",
            "distractors": {
                "B": "Tag inheritance is not automatic by default.",
                "C": "Tags can be applied directly to individual resources.",
                "D": "Tagging a resource group does not delete tags on its resources.",
            },
            "exam_pattern": "Tags are NOT inherited by default; apply/enforce them on resources.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (tags)"],
    },
    {
        "id": "az900-gov-r2-006", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "If spending exceeds an Azure Cost Management budget, what happens by default?",
        "options": [
            {"id": "A", "text": "Azure immediately deletes the over-budget resources"},
            {"id": "B", "text": "Azure automatically shuts down all of the subscription's resources"},
            {"id": "C", "text": "The budget triggers alerts/notifications; it does not automatically stop or "
                               "delete resources by default"},
            {"id": "D", "text": "The budget permanently blocks all future deployments"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A budget is a tracking-and-alerting tool: exceeding it sends notifications, but it "
                       "does not stop or delete resources by itself (alerts can trigger automation you set up).",
            "distractors": {
                "A": "Budgets do not delete resources.",
                "B": "Budgets do not automatically shut resources down on their own.",
                "D": "Budgets do not permanently block deployments.",
            },
            "exam_pattern": "Budgets alert on spend; they do not auto-stop resources by default.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (budgets)"],
    },
    {
        "id": "az900-gov-r2-007", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "The same virtual machine, unchanged in size or configuration, cost more last month than "
                "the month before. What most likely explains the higher charge?",
        "options": [
            {"id": "A", "text": "The VM was given a new name"},
            {"id": "B", "text": "It ran (was used) for more hours, and Azure bills metered consumption based "
                               "on usage"},
            {"id": "C", "text": "More tags were added to it"},
            {"id": "D", "text": "It was moved to a different resource group"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure uses metered, consumption-based billing, so running the VM for more hours "
                       "increases its cost even if nothing about its configuration changed.",
            "distractors": {
                "A": "A resource's name is free metadata and does not affect price.",
                "C": "Tags are free labels for organization and reporting; they do not change cost.",
                "D": "Resource groups are free containers; moving between them does not change price.",
            },
            "exam_pattern": "Metered consumption: more usage (hours) = higher bill.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (consumption-based costs)"],
    },
    {
        "id": "az900-gov-r2-008", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A development virtual machine is only needed during business hours. Which action most "
                "directly reduces its compute cost?",
        "options": [
            {"id": "A", "text": "Schedule it to automatically shut down (deallocate) outside business hours"},
            {"id": "B", "text": "Add more tags to the VM"},
            {"id": "C", "text": "Apply a ReadOnly lock to the VM"},
            {"id": "D", "text": "Move it to a different resource group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Deallocating (shutting down) the VM outside business hours stops its compute "
                       "billing for those hours, directly reducing cost.",
            "distractors": {
                "B": "Tags are free labels and do not reduce cost.",
                "C": "A ReadOnly lock prevents changes but keeps the VM running and billed.",
                "D": "Moving between resource groups does not change price.",
            },
            "exam_pattern": "Deallocate idle dev VMs off-hours to cut compute cost.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe cost management (optimizing cost)"],
    },
    {
        "id": "az900-gov-r2-009", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "multi",
        "stem": "Which TWO factors genuinely affect how much an Azure resource costs? (Choose two.)",
        "options": [
            {"id": "A", "text": "The Azure region where it is deployed"},
            {"id": "B", "text": "The resource's display name"},
            {"id": "C", "text": "Outbound data transfer (egress) that it generates"},
            {"id": "D", "text": "The number of tags applied to it"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Region (datacenter costs vary by location) and outbound data transfer (egress is "
                       "generally billed) are genuine cost factors.",
            "distractors": {
                "B": "A resource's display name is free metadata and does not affect price.",
                "D": "Tags are free labels for organization and reporting; their count does not change cost.",
            },
            "exam_pattern": "Real cost factors include region and egress; names and tags do not cost money.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the factors that affect cost"],
    },

    # ----- az_governance_compliance -----------------------------------------
    {
        "id": "az900-gov-r2-010", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 3, "type": "mcq",
        "stem": "Azure Blueprints packaged governance artifacts (ARM templates, policy assignments, and "
                "role assignments) into repeatable environment definitions, but Microsoft is retiring it. "
                "Which does Microsoft now recommend as the replacement approach?",
        "options": [
            {"id": "A", "text": "Keep using Azure Blueprints indefinitely; nothing is changing"},
            {"id": "B", "text": "Microsoft Purview"},
            {"id": "C", "text": "The Azure Pricing Calculator"},
            {"id": "D", "text": "Template Specs (for the definitions) together with deployment stacks"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Azure Blueprints is being retired; Microsoft recommends migrating blueprint "
                       "definitions to Template Specs and blueprint assignments to deployment stacks.",
            "distractors": {
                "A": "Blueprints is on a retirement path, so continuing to rely on it is not the recommended approach.",
                "B": "Microsoft Purview is a data governance solution, not a replacement for Blueprints.",
                "C": "The Pricing Calculator estimates cost; it has nothing to do with packaging governance artifacts.",
            },
            "exam_pattern": "Blueprints is retiring -> use Template Specs + deployment stacks.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure governance features"],
    },
    {
        "id": "az900-gov-r2-011", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A user needs to create and manage Azure resources but must NOT be able to grant other "
                "people access to those resources. Which built-in RBAC role fits best?",
        "options": [
            {"id": "A", "text": "Owner"},
            {"id": "B", "text": "Contributor"},
            {"id": "C", "text": "Reader"},
            {"id": "D", "text": "User Access Administrator"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Contributor can create and manage resources but cannot grant access to others "
                       "(it cannot manage role assignments).",
            "distractors": {
                "A": "Owner can manage resources AND grant others access, which exceeds the requirement.",
                "C": "Reader is view-only and cannot create or manage resources.",
                "D": "User Access Administrator manages access but is not meant to manage the resources themselves.",
            },
            "exam_pattern": "Manage resources but not grant access = Contributor; full control = Owner.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe role-based access control (RBAC)"],
    },
    {
        "id": "az900-gov-r2-012", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "An RBAC role is assigned at the subscription scope. How does it apply to the resource "
                "groups and resources within that subscription?",
        "options": [
            {"id": "A", "text": "It is inherited by the resource groups and resources beneath the subscription"},
            {"id": "B", "text": "It applies only to the subscription object and nothing inside it"},
            {"id": "C", "text": "It must be re-created separately on every single resource"},
            {"id": "D", "text": "It is ignored unless it is also assigned at a management group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC assignments are inherited down the hierarchy, so a role assigned at the "
                       "subscription applies to the resource groups and resources within it.",
            "distractors": {
                "B": "The assignment cascades to the contents, not just the subscription object.",
                "C": "Inheritance means you do not re-create the assignment on every resource.",
                "D": "The assignment works on its own; it does not require a management-group assignment.",
            },
            "exam_pattern": "RBAC assigned at a higher scope is inherited by child scopes.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe role-based access control (RBAC)"],
    },
    {
        "id": "az900-gov-r2-013", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A governance team wants to group many related Azure Policy definitions together and "
                "assign them as a single compliance package. What is this grouping called?",
        "options": [
            {"id": "A", "text": "A resource lock"},
            {"id": "B", "text": "A management group"},
            {"id": "C", "text": "A policy initiative (policy set)"},
            {"id": "D", "text": "An availability set"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A policy initiative (also called a policy set) groups multiple policy definitions "
                       "so they can be assigned and tracked together as one compliance package.",
            "distractors": {
                "A": "A resource lock protects a resource from change or deletion; it is not a group of policies.",
                "B": "A management group organizes subscriptions, not policy definitions.",
                "D": "An availability set is a VM resiliency feature, unrelated to policy grouping.",
            },
            "exam_pattern": "Group many policy definitions for one assignment = initiative (policy set).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Policy"],
    },
    {
        "id": "az900-gov-r2-014", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A CanNotDelete lock is applied at the resource group scope. Which resources does it "
                "protect?",
        "options": [
            {"id": "A", "text": "Only the resource group object, not the resources inside it"},
            {"id": "B", "text": "The resource group and all resources within it, because locks are inherited "
                               "by child resources"},
            {"id": "C", "text": "Only resources created after the lock was applied"},
            {"id": "D", "text": "Only virtual machines, never any other resource type"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Locks applied at a parent scope are inherited, so a CanNotDelete lock on a resource "
                       "group protects the group and every resource within it.",
            "distractors": {
                "A": "The lock protects the contained resources, not just the group object.",
                "C": "Inherited locks apply to existing resources too, not only new ones.",
                "D": "Locks apply to all resource types, not just virtual machines.",
            },
            "exam_pattern": "A lock at a parent scope is inherited by all child resources.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe resource locks"],
    },
    {
        "id": "az900-gov-r2-015", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 3, "type": "mcq",
        "stem": "A user has the Owner role on a resource, but the resource has a CanNotDelete lock. What "
                "happens when the Owner tries to delete it?",
        "options": [
            {"id": "A", "text": "The Owner role overrides the lock and the resource is deleted"},
            {"id": "B", "text": "The resource is deleted but then automatically recreated"},
            {"id": "C", "text": "Locks do not apply to Owners at all"},
            {"id": "D", "text": "The deletion is blocked until the lock is removed, regardless of the user's role"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Resource locks apply on top of RBAC, so even an Owner cannot delete a resource with "
                       "a CanNotDelete lock until the lock is removed.",
            "distractors": {
                "A": "An Owner's permissions do not override a resource lock.",
                "B": "The resource is simply not deleted; nothing is recreated.",
                "C": "Locks apply regardless of role, including to Owners.",
            },
            "exam_pattern": "A resource lock blocks deletion even for an Owner until it is removed.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe resource locks"],
    },
    {
        "id": "az900-gov-r2-016", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "mcq",
        "stem": "A security policy says each user should be granted only the permissions required to do "
                "their job, and no more. Which principle does this describe, and which Azure feature "
                "helps enforce it?",
        "options": [
            {"id": "A", "text": "The principle of least privilege, enforced through Azure RBAC role assignments"},
            {"id": "B", "text": "The principle of maximum access, enforced by giving everyone the Owner role"},
            {"id": "C", "text": "Data residency, enforced through Azure geographies"},
            {"id": "D", "text": "Elasticity, enforced through autoscaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Granting only the permissions needed is the principle of least privilege; Azure "
                       "RBAC helps enforce it by assigning scoped roles.",
            "distractors": {
                "B": "Giving everyone Owner is the opposite of least privilege.",
                "C": "Data residency concerns where data is stored, not permission levels.",
                "D": "Elasticity is a scaling concept, unrelated to permissions.",
            },
            "exam_pattern": "Minimum permissions needed = least privilege, enforced via RBAC.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe role-based access control (RBAC)"],
    },
    {
        "id": "az900-gov-r2-017", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants Azure Policy to automatically add a missing required tag to "
                "resources as they are created, rather than merely reporting or blocking them. Which kind "
                "of policy effect does this?",
        "options": [
            {"id": "A", "text": "The Deny effect"},
            {"id": "B", "text": "The Audit effect"},
            {"id": "C", "text": "An effect that adds or sets the value, such as Append or Modify"},
            {"id": "D", "text": "The Disabled effect"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Effects such as Append or Modify add or set values (for example, adding a missing "
                       "required tag) during resource creation or update.",
            "distractors": {
                "A": "The Deny effect blocks non-compliant deployments rather than fixing them.",
                "B": "The Audit effect only records non-compliance in reports.",
                "D": "The Disabled effect turns the policy off, so it does nothing.",
            },
            "exam_pattern": "Auto-add/set a value (e.g., a tag) = Append/Modify; block = Deny; report = Audit.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Policy (effects)"],
    },
    {
        "id": "az900-gov-r2-018", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "multi",
        "stem": "Which TWO Azure features are used for governance and compliance? (Choose two.)",
        "options": [
            {"id": "A", "text": "Azure Policy"},
            {"id": "B", "text": "Resource locks"},
            {"id": "C", "text": "The Azure Pricing Calculator"},
            {"id": "D", "text": "Application Insights"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Azure Policy enforces organizational standards, and resource locks protect "
                       "resources from change or deletion; both are governance features.",
            "distractors": {
                "C": "The Pricing Calculator estimates cost before deployment; it is not a governance control.",
                "D": "Application Insights monitors application performance; it is not a governance control.",
            },
            "exam_pattern": "Governance toolset includes Azure Policy and resource locks.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure governance features"],
    },

    # ----- az_tools_monitoring ----------------------------------------------
    {
        "id": "az900-gov-r2-019", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to continuously assess and strengthen the security posture of its Azure "
                "(and hybrid/multicloud) resources and protect workloads against threats. Which service "
                "is designed for this?",
        "options": [
            {"id": "A", "text": "Azure Advisor"},
            {"id": "B", "text": "Microsoft Defender for Cloud"},
            {"id": "C", "text": "Azure Monitor"},
            {"id": "D", "text": "The Azure Pricing Calculator"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Defender for Cloud provides cloud security posture management and "
                       "workload protection across Azure, hybrid, and multicloud environments.",
            "distractors": {
                "A": "Azure Advisor gives broad best-practice recommendations, not a dedicated security-posture and workload-protection platform.",
                "C": "Azure Monitor collects telemetry and alerts; it is not a security-posture solution.",
                "D": "The Pricing Calculator estimates cost; it has no security role.",
            },
            "exam_pattern": "Assess security posture and protect workloads = Microsoft Defender for Cloud.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Defender for Cloud"],
    },
    {
        "id": "az900-gov-r2-020", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Within Microsoft Defender for Cloud, which feature gives you a single measurement of "
                "your current security posture, along with recommendations to improve it?",
        "options": [
            {"id": "A", "text": "Secure Score"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "A policy initiative"},
            {"id": "D", "text": "The TCO Calculator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secure Score in Microsoft Defender for Cloud measures your security posture as a "
                       "single score and provides recommendations to improve it.",
            "distractors": {
                "B": "A resource lock protects a resource from change or deletion; it is not a posture score.",
                "C": "A policy initiative groups policy definitions; it is not a security score.",
                "D": "The TCO Calculator compares on-premises and Azure costs, not security posture.",
            },
            "exam_pattern": "Single security-posture measurement with guidance = Secure Score.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Defender for Cloud (Secure Score)"],
    },
    {
        "id": "az900-gov-r2-021", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to manage and govern servers and Kubernetes clusters that run "
                "on-premises and in other clouds, using familiar Azure tools such as Azure Policy and "
                "RBAC. Which service extends Azure management to those resources?",
        "options": [
            {"id": "A", "text": "Azure Virtual Desktop"},
            {"id": "B", "text": "Azure Load Balancer"},
            {"id": "C", "text": "Azure Arc"},
            {"id": "D", "text": "Azure Blob Storage"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Azure Arc extends Azure management and governance (such as Azure Policy and RBAC) "
                       "to servers, Kubernetes clusters, and services running outside Azure.",
            "distractors": {
                "A": "Azure Virtual Desktop delivers cloud-hosted desktops, not multicloud management.",
                "B": "Azure Load Balancer distributes network traffic; it does not govern external resources.",
                "D": "Azure Blob Storage stores objects; it does not manage servers or clusters.",
            },
            "exam_pattern": "Manage on-premises/multicloud resources with Azure tools = Azure Arc.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Arc"],
    },
    {
        "id": "az900-gov-r2-022", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An Azure feature is labeled 'preview'. Compared with a generally available (GA) feature, "
                "what should a team expect?",
        "options": [
            {"id": "A", "text": "Preview features always include the full production SLA and support"},
            {"id": "B", "text": "Preview and GA are identical in every way"},
            {"id": "C", "text": "GA features are the early, experimental, unsupported ones"},
            {"id": "D", "text": "Preview features are for early evaluation and may have limited support and no "
                               "production SLA, while GA features are fully released and production-ready"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Preview features are for early evaluation and typically carry limited support and "
                       "no production SLA; GA (general availability) features are fully released and production-ready.",
            "distractors": {
                "A": "Preview features typically do not come with a production SLA.",
                "B": "Preview and GA differ in support, stability, and SLA.",
                "C": "This reverses the lifecycle - GA is the fully released stage, not the experimental one.",
            },
            "exam_pattern": "Preview = early eval, no production SLA; GA = production-ready.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the service lifecycle (preview and general availability)"],
    },
    {
        "id": "az900-gov-r2-023", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "What is an Azure service-level agreement (SLA)?",
        "options": [
            {"id": "A", "text": "A tool that estimates the cost of a workload before deployment"},
            {"id": "B", "text": "A formal agreement from Microsoft stating the expected performance and "
                               "availability (such as an uptime target) for a service"},
            {"id": "C", "text": "A role that grants a user read-only access"},
            {"id": "D", "text": "A physical appliance used to transfer large amounts of data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An SLA is Microsoft's formal commitment describing the expected performance and "
                       "availability (for example, an uptime target) of a service.",
            "distractors": {
                "A": "Estimating cost before deployment is the Pricing Calculator, not an SLA.",
                "C": "A read-only role is the RBAC Reader role, not an SLA.",
                "D": "A physical data-transfer appliance is Azure Data Box, not an SLA.",
            },
            "exam_pattern": "SLA = formal commitment on a service's availability/performance.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe service-level agreements (SLAs)"],
    },
    {
        "id": "az900-gov-r2-024", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants to check whether one specific virtual machine instance is healthy "
                "and, if not, whether the cause is a problem on the Azure platform. Which tool focuses on "
                "the health of that individual resource?",
        "options": [
            {"id": "A", "text": "Azure Resource Health"},
            {"id": "B", "text": "The Azure Pricing Calculator"},
            {"id": "C", "text": "Microsoft Cost Management"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Resource Health reports the health of a specific resource instance and whether "
                       "any issue is caused by the Azure platform. (Azure Service Health, by contrast, covers "
                       "broad platform-wide events.)",
            "distractors": {
                "B": "The Pricing Calculator estimates cost; it does not report resource health.",
                "C": "Cost Management tracks spending, not resource health.",
                "D": "Azure Policy enforces configuration rules; it does not report health.",
            },
            "exam_pattern": "Health of one specific resource = Resource Health; platform-wide = Service Health.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Service Health and Resource Health"],
    },
    {
        "id": "az900-gov-r2-025", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "An on-call engineer wants to check resource status and run basic management tasks from a "
                "smartphone while away from a computer. Which option is intended for this?",
        "options": [
            {"id": "A", "text": "ARM templates"},
            {"id": "B", "text": "Bicep"},
            {"id": "C", "text": "The Azure mobile app"},
            {"id": "D", "text": "Azure Data Box"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Azure mobile app lets you monitor resource status and perform basic management "
                       "tasks from a phone.",
            "distractors": {
                "A": "ARM templates are infrastructure-as-code files, not a mobile management app.",
                "B": "Bicep is an infrastructure-as-code language, not a mobile app.",
                "D": "Azure Data Box is a physical data-transfer appliance, not a management app.",
            },
            "exam_pattern": "Monitor and manage from a phone = the Azure mobile app.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe the tools for managing and deploying Azure resources"],
    },
    {
        "id": "az900-gov-r2-026", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "In Azure Monitor, which statement correctly distinguishes metrics from logs?",
        "options": [
            {"id": "A", "text": "Metrics and logs are the same data with two different names"},
            {"id": "B", "text": "Metrics are text records you query with KQL, while logs are numeric only"},
            {"id": "C", "text": "Logs can never be queried"},
            {"id": "D", "text": "Metrics are numeric values collected over time (time-series), while logs are "
                               "records of events/data you query, for example with Log Analytics using KQL"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Metrics are numeric, time-series values; logs are records of events and data that "
                       "you query (for example, in Log Analytics using KQL).",
            "distractors": {
                "A": "Metrics and logs are different data types with different uses.",
                "B": "This reverses the definitions - metrics are numeric, logs are the queryable records.",
                "C": "Logs are specifically meant to be queried.",
            },
            "exam_pattern": "Metrics = numeric time-series; logs = queryable event/data records (KQL).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Monitor (metrics and logs)"],
    },
    {
        "id": "az900-gov-r2-027", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "multi",
        "stem": "Which TWO services help you observe the health and performance of your Azure "
                "environment? (Choose two.)",
        "options": [
            {"id": "A", "text": "Azure Pricing Calculator"},
            {"id": "B", "text": "Azure Monitor"},
            {"id": "C", "text": "Azure Service Health"},
            {"id": "D", "text": "Azure Blueprints"},
        ],
        "correct": ["B", "C"],
        "explanation": {
            "correct": "Azure Monitor collects and analyzes resource telemetry, and Azure Service Health "
                       "reports Azure platform status affecting you; both help you observe your environment.",
            "distractors": {
                "A": "The Pricing Calculator estimates cost before deployment; it does not monitor health.",
                "D": "Azure Blueprints packaged governance artifacts (and is being retired); it is not a monitoring tool.",
            },
            "exam_pattern": "Observe health/performance = Azure Monitor + Azure Service Health.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe monitoring tools (Azure Monitor and Azure Service Health)"],
    },
]
