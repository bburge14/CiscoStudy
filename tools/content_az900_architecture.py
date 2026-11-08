"""Microsoft Azure Fundamentals (AZ-900) pool - Domain 2: Azure Architecture and Services.

Original, objective-aligned practice items for the four Architecture-and-Services
subtopics tracked in CertLab:
  * az_core_architecture  - regions, region pairs, availability zones, datacenters,
                            geographies; the management hierarchy (management groups >
                            subscriptions > resource groups > resources); Azure
                            Resource Manager (ARM).
  * az_compute_networking - Azure VMs, scale sets & availability sets, containers
                            (ACI, AKS), Azure Functions, App Service; virtual networks
                            & subnets, VPN Gateway vs ExpressRoute, Azure DNS,
                            public/private endpoints; when to pick each compute option.
  * az_storage            - storage accounts; blob/disk/file/queue storage; redundancy
                            (LRS, ZRS, GRS, GZRS); access tiers (hot/cool/cold/archive);
                            migration/transfer (Azure Migrate, Data Box, AzCopy).
  * az_identity           - Microsoft Entra ID (formerly Azure Active Directory);
                            authentication vs authorization; SSO, MFA, Conditional
                            Access; Microsoft Entra External ID (B2B/B2C); Entra ID vs
                            on-premises Active Directory.

Authoring rules match the other content_*.py pools: build_content.py shuffles option
order (seeded by id), so the answer key authored here as "A" is not positionally
biased, every wrong option carries a distractor note, and each item names the Microsoft
Learn area it draws on so facts stay traceable. Fundamentals depth only (concepts,
when-to-use, who-does-what) - no numeric limits/prices, no region/version trivia, and
never real or memorized exam items. Current product naming is used (Microsoft Entra ID,
not "Azure AD"), with the former name noted where it aids recognition.
"""

QUESTIONS = [
    # ===== az_core_architecture =============================================
    {
        "id": "az900-arch-001", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 1, "type": "mcq",
        "stem": "Your team must keep a production app running even if one datacenter inside an Azure "
                "region fails, without leaving that region. Which feature should you use?",
        "options": [
            {"id": "A", "text": "Availability zones"},
            {"id": "B", "text": "Region pairs"},
            {"id": "C", "text": "Resource groups"},
            {"id": "D", "text": "Management groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Availability zones are physically separate datacenters within a single region, "
                       "each with independent power, cooling, and networking, so losing one datacenter "
                       "does not take the app down.",
            "distractors": {
                "B": "Region pairs span two different regions, not datacenters inside one region.",
                "C": "Resource groups are logical containers for management and give no physical fault isolation.",
                "D": "Management groups organize subscriptions for governance, not datacenter resilience.",
            },
            "exam_pattern": "Survive a single-datacenter failure within one region = availability zones.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions, availability zones, and region pairs"],
    },
    {
        "id": "az900-arch-002", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 1, "type": "mcq",
        "stem": "A new teammate asks you to define an Azure region in fundamentals terms. Which "
                "description is correct?",
        "options": [
            {"id": "A", "text": "A geographical area containing one or more networked datacenters"},
            {"id": "B", "text": "A single server rack inside a datacenter"},
            {"id": "C", "text": "A monthly invoice for Azure usage"},
            {"id": "D", "text": "A JSON template file that deploys resources"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An Azure region is a geographical area that contains one or more datacenters "
                       "networked together with low-latency links.",
            "distractors": {
                "B": "A rack is hardware inside a datacenter, far smaller than a region.",
                "C": "That describes billing or an invoice, which is a subscription concept, not a region.",
                "D": "That describes an ARM template, not a region.",
            },
            "exam_pattern": "Region = geographic area of one or more networked datacenters.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions, availability zones, and region pairs"],
    },
    {
        "id": "az900-arch-003", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Your team wants two Azure regions in the same geography where planned platform updates "
                "roll out to only one region at a time. Which concept describes this?",
        "options": [
            {"id": "A", "text": "Region pairs"},
            {"id": "B", "text": "Availability zones"},
            {"id": "C", "text": "Availability sets"},
            {"id": "D", "text": "Subnets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Region pairs are two regions in the same geography; Azure staggers planned "
                       "maintenance so updates reach only one region of the pair at a time, and the pair "
                       "is also the target for geo-redundant replication.",
            "distractors": {
                "B": "Availability zones are separate datacenters within a single region, not a two-region relationship.",
                "C": "Availability sets protect VMs within one datacenter, not across regions.",
                "D": "Subnets segment a virtual network and are unrelated to regional update behavior.",
            },
            "exam_pattern": "Two regions, same geography, staggered updates = region pairs.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions, availability zones, and region pairs"],
    },
    {
        "id": "az900-arch-004", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Which list shows the Azure resource management hierarchy ordered from the broadest "
                "scope to the narrowest?",
        "options": [
            {"id": "A", "text": "Management groups, subscriptions, resource groups, resources"},
            {"id": "B", "text": "Subscriptions, management groups, resources, resource groups"},
            {"id": "C", "text": "Resource groups, resources, subscriptions, management groups"},
            {"id": "D", "text": "Resources, resource groups, management groups, subscriptions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "From broad to narrow, Azure organizes management groups, then subscriptions, then "
                       "resource groups, then individual resources.",
            "distractors": {
                "B": "Management groups sit above subscriptions, not below them.",
                "C": "This inverts the hierarchy, placing resource groups above subscriptions.",
                "D": "This is fully reversed; resources are the narrowest scope, not the broadest.",
            },
            "exam_pattern": "Broad to narrow: management group > subscription > resource group > resource.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-005", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Your company has 20 subscriptions and wants to apply one governance policy to all of "
                "them at once. Which scope should you assign the policy to?",
        "options": [
            {"id": "A", "text": "A management group that contains the subscriptions"},
            {"id": "B", "text": "Each resource group separately"},
            {"id": "C", "text": "A single resource"},
            {"id": "D", "text": "An availability zone"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Management groups sit above subscriptions; a policy assigned to a management group "
                       "is inherited by every subscription beneath it, covering all 20 at once.",
            "distractors": {
                "B": "Assigning per resource group is repetitive and would not uniformly cover whole subscriptions.",
                "C": "A single resource is the narrowest scope and cannot govern 20 subscriptions.",
                "D": "Availability zones are a resiliency feature, not a governance scope.",
            },
            "exam_pattern": "Govern many subscriptions together = management group.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-006", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 1, "type": "mcq",
        "stem": "A colleague asks what an Azure resource group is. Which statement describes it best?",
        "options": [
            {"id": "A", "text": "A logical container that holds related Azure resources for management"},
            {"id": "B", "text": "A physical datacenter building"},
            {"id": "C", "text": "A dedicated private network link into Azure"},
            {"id": "D", "text": "A worldwide billing account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A resource group is a logical container that holds related resources so they can be "
                       "managed together, such as deployed, updated, or deleted as a unit.",
            "distractors": {
                "B": "A datacenter is a physical facility, not a logical container.",
                "C": "That describes ExpressRoute, a connectivity service, not a resource group.",
                "D": "That describes billing through a subscription or account, not a resource group.",
            },
            "exam_pattern": "Resource group = logical container for related resources.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-007", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "A developer deletes a resource group that holds a VM, its disk, and a storage account. "
                "What happens to those resources?",
        "options": [
            {"id": "A", "text": "All resources in the group are deleted"},
            {"id": "B", "text": "Only the group name is removed; the resources remain"},
            {"id": "C", "text": "The resources move to a default group automatically"},
            {"id": "D", "text": "Only the VM is deleted; the disk and storage remain"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resources share the lifecycle of their resource group, so deleting the group deletes "
                       "every resource contained in it.",
            "distractors": {
                "B": "Deleting a group is not just a rename; its contents are removed as well.",
                "C": "Resources are not auto-migrated on deletion; they are removed with the group.",
                "D": "Deletion is not selective; all contained resources go, not only the VM.",
            },
            "exam_pattern": "Delete the resource group and you delete everything inside it.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-008", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "You need to know how many resource groups a single resource, such as one virtual "
                "machine, can belong to at the same time. What is correct?",
        "options": [
            {"id": "A", "text": "Exactly one"},
            {"id": "B", "text": "Up to two"},
            {"id": "C", "text": "Any number, with no limit"},
            {"id": "D", "text": "Zero; resources exist outside groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Each Azure resource belongs to exactly one resource group at a time, though it can be "
                       "moved to a different group later.",
            "distractors": {
                "B": "A resource cannot belong to two resource groups simultaneously.",
                "C": "Membership is not unlimited; it is exactly one group at a time.",
                "D": "Every resource must reside in a resource group, so zero is incorrect.",
            },
            "exam_pattern": "One resource lives in exactly one resource group at a time.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-009", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Every request to create, update, or delete Azure resources from the portal, CLI, "
                "PowerShell, or templates is processed by which service?",
        "options": [
            {"id": "A", "text": "Azure Resource Manager"},
            {"id": "B", "text": "Microsoft Entra ID"},
            {"id": "C", "text": "Azure Monitor"},
            {"id": "D", "text": "Azure Blob Storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Resource Manager (ARM) is the unified deployment and management layer that "
                       "handles all resource create, update, and delete requests, no matter which tool issues them.",
            "distractors": {
                "B": "Microsoft Entra ID handles identity and access, not resource deployment.",
                "C": "Azure Monitor collects telemetry and metrics; it does not process resource requests.",
                "D": "Blob Storage stores data objects and is not the management layer.",
            },
            "exam_pattern": "All resource management requests flow through Azure Resource Manager.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure Resource Manager (ARM)"],
    },
    {
        "id": "az900-arch-010", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Your finance team wants completely separate invoices for the development and production "
                "workloads. Which Azure boundary most directly separates billing?",
        "options": [
            {"id": "A", "text": "Separate subscriptions"},
            {"id": "B", "text": "Separate resource groups in one subscription"},
            {"id": "C", "text": "Resource tags only"},
            {"id": "D", "text": "Availability zones"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A subscription is a billing and access boundary, so placing dev and prod in separate "
                       "subscriptions produces separate invoices.",
            "distractors": {
                "B": "Resource groups organize resources but do not generate separate invoices by themselves.",
                "C": "Tags help categorize and report costs but do not split billing into separate invoices.",
                "D": "Availability zones are a resiliency feature, unrelated to billing separation.",
            },
            "exam_pattern": "Separate invoices = separate subscriptions.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure resource groups, subscriptions, and management groups"],
    },
    {
        "id": "az900-arch-011", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_core_architecture", "difficulty": 3, "type": "mcq",
        "stem": "A regulator requires that your customer data stay within a specific country's "
                "boundaries. Which Azure concept is defined to preserve data residency and compliance?",
        "options": [
            {"id": "A", "text": "An Azure geography"},
            {"id": "B", "text": "An availability zone"},
            {"id": "C", "text": "A resource group"},
            {"id": "D", "text": "A subnet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A geography is a discrete market, often aligned to country or compliance boundaries, "
                       "that ensures data residency; region pairs always stay within the same geography.",
            "distractors": {
                "B": "An availability zone is a datacenter grouping inside one region, not a data-residency boundary.",
                "C": "A resource group is a logical management container, not a compliance or residency boundary.",
                "D": "A subnet segments a virtual network and has nothing to do with data residency.",
            },
            "exam_pattern": "Data-residency and compliance boundary = geography.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure regions, region pairs, and sovereign regions"],
    },

    # ===== az_compute_networking ============================================
    {
        "id": "az900-arch-012", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "A developer must run a small piece of code only when a queue message arrives, and pay "
                "only while it runs. Which service fits best?",
        "options": [
            {"id": "A", "text": "Azure Functions"},
            {"id": "B", "text": "Azure Virtual Machines"},
            {"id": "C", "text": "Azure App Service"},
            {"id": "D", "text": "Azure Kubernetes Service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Functions is serverless and event-driven: code runs in response to a trigger "
                       "such as a queue message, you pay only for the execution, and it scales automatically.",
            "distractors": {
                "B": "A VM runs continuously and must be managed and paid for even when idle.",
                "C": "App Service hosts always-running web apps, not pay-per-execution event code.",
                "D": "AKS orchestrates containers and adds management overhead unnecessary for a tiny function.",
            },
            "exam_pattern": "Event-triggered, pay-per-run code = Azure Functions (serverless).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-013", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Your company needs a private, dedicated connection to Azure that does not travel over "
                "the public internet, with predictable low latency. Which service meets this?",
        "options": [
            {"id": "A", "text": "ExpressRoute"},
            {"id": "B", "text": "VPN Gateway"},
            {"id": "C", "text": "Azure DNS"},
            {"id": "D", "text": "A public endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ExpressRoute provides a private, dedicated connection to Azure through a connectivity "
                       "provider, bypassing the public internet for more consistent latency and bandwidth.",
            "distractors": {
                "B": "A VPN Gateway is encrypted but still carries traffic across the public internet.",
                "C": "Azure DNS resolves domain names and is not a connectivity circuit.",
                "D": "A public endpoint is reached over the internet, the opposite of a private dedicated link.",
            },
            "exam_pattern": "Private, dedicated, off-the-internet link = ExpressRoute.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure networking (virtual networks, VPN Gateway, ExpressRoute, DNS)"],
    },
    {
        "id": "az900-arch-014", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "A small branch office needs an encrypted site-to-site tunnel to Azure over its existing "
                "internet connection, with no dedicated circuit. Which service fits?",
        "options": [
            {"id": "A", "text": "VPN Gateway"},
            {"id": "B", "text": "ExpressRoute"},
            {"id": "C", "text": "Azure Functions"},
            {"id": "D", "text": "An availability set"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VPN Gateway creates encrypted IPsec/IKE tunnels to Azure over the public internet, "
                       "so a branch can connect without provisioning a dedicated circuit.",
            "distractors": {
                "B": "ExpressRoute requires a provider-provisioned private circuit, which the scenario rules out.",
                "C": "Azure Functions runs code and is unrelated to network connectivity.",
                "D": "An availability set spreads VMs for resiliency and does not connect networks.",
            },
            "exam_pattern": "Encrypted tunnel over the public internet = VPN Gateway.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure networking (virtual networks, VPN Gateway, ExpressRoute, DNS)"],
    },
    {
        "id": "az900-arch-015", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "You want to protect several VMs from a hardware fault or planned maintenance within a "
                "single datacenter. Which feature spreads them across fault and update domains?",
        "options": [
            {"id": "A", "text": "An availability set"},
            {"id": "B", "text": "An availability zone"},
            {"id": "C", "text": "A virtual machine scale set"},
            {"id": "D", "text": "A resource group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An availability set distributes VMs across fault domains and update domains inside one "
                       "datacenter, protecting them from localized hardware failures and planned maintenance.",
            "distractors": {
                "B": "Availability zones protect across separate datacenters in a region, not within one datacenter's domains.",
                "C": "A scale set manages identical VMs for scaling; it is not the fault/update-domain resiliency construct.",
                "D": "A resource group is a logical container and provides no physical fault isolation.",
            },
            "exam_pattern": "Fault and update domains within one datacenter = availability set.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-016", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "Your web tier must automatically add or remove identical, load-balanced VMs as traffic "
                "rises and falls. Which capability provides this?",
        "options": [
            {"id": "A", "text": "Virtual machine scale sets"},
            {"id": "B", "text": "Availability sets"},
            {"id": "C", "text": "Azure Container Instances"},
            {"id": "D", "text": "ExpressRoute"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Virtual machine scale sets create and manage a group of identical, load-balanced VMs "
                       "and automatically scale their number based on demand or a schedule.",
            "distractors": {
                "B": "Availability sets improve resiliency but do not autoscale the number of VMs.",
                "C": "Azure Container Instances runs containers, not a managed fleet of VMs.",
                "D": "ExpressRoute is a connectivity service, unrelated to autoscaling VMs.",
            },
            "exam_pattern": "Autoscaling a fleet of identical VMs = scale sets.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-017", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "Your team is deploying dozens of microservice containers that need orchestration, "
                "scaling, and self-healing. Which service is designed for this?",
        "options": [
            {"id": "A", "text": "Azure Kubernetes Service"},
            {"id": "B", "text": "Azure Container Instances"},
            {"id": "C", "text": "Azure Functions"},
            {"id": "D", "text": "Azure DNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Kubernetes Service (AKS) is managed Kubernetes for orchestrating many containers "
                       "at scale, including scheduling, scaling, and self-healing.",
            "distractors": {
                "B": "Azure Container Instances runs single or simple containers without an orchestrator.",
                "C": "Azure Functions runs event-driven code, not container orchestration.",
                "D": "Azure DNS resolves names and is unrelated to running containers.",
            },
            "exam_pattern": "Orchestrate many containers at scale = AKS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-018", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants the fastest, simplest way to run a single container in Azure without "
                "managing servers or an orchestrator. Which service should they choose?",
        "options": [
            {"id": "A", "text": "Azure Container Instances"},
            {"id": "B", "text": "Azure Kubernetes Service"},
            {"id": "C", "text": "Azure Virtual Machines"},
            {"id": "D", "text": "Azure ExpressRoute"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Container Instances (ACI) is the quickest, simplest way to run a container "
                       "serverlessly, with no VM or orchestrator to manage.",
            "distractors": {
                "B": "AKS adds orchestration and cluster management overhead not needed for a single container.",
                "C": "A VM requires you to manage the operating system and container runtime yourself.",
                "D": "ExpressRoute is a networking service and cannot run containers.",
            },
            "exam_pattern": "One container, no orchestration, fastest start = ACI.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-019", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "Your team wants to host a scalable web app and REST API without managing the underlying "
                "operating system or servers. Which service fits best?",
        "options": [
            {"id": "A", "text": "Azure App Service"},
            {"id": "B", "text": "Azure Virtual Machines"},
            {"id": "C", "text": "An availability zone"},
            {"id": "D", "text": "Azure Data Box"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure App Service is a platform-as-a-service offering that hosts web apps and APIs with "
                       "built-in scaling and no operating system for you to manage.",
            "distractors": {
                "B": "A VM is infrastructure-as-a-service, so you must manage and patch the OS yourself.",
                "C": "An availability zone is a resiliency construct, not an app-hosting service.",
                "D": "Azure Data Box is a data-transfer appliance, not a web host.",
            },
            "exam_pattern": "Managed web/API hosting with no OS to manage = App Service (PaaS).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },
    {
        "id": "az900-arch-020", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "You must divide a virtual network's private address space into smaller ranges for "
                "different tiers of an application. What do you create?",
        "options": [
            {"id": "A", "text": "Subnets"},
            {"id": "B", "text": "Resource groups"},
            {"id": "C", "text": "Management groups"},
            {"id": "D", "text": "Storage accounts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Subnets segment a virtual network's address space into smaller ranges so you can "
                       "separate and control the tiers of an application.",
            "distractors": {
                "B": "Resource groups are management containers, not network segments.",
                "C": "Management groups organize subscriptions, not IP address ranges.",
                "D": "Storage accounts hold data and are unrelated to network segmentation.",
            },
            "exam_pattern": "Segment a virtual network's address space = subnets.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure networking (virtual networks, VPN Gateway, ExpressRoute, DNS)"],
    },
    {
        "id": "az900-arch-021", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 2, "type": "mcq",
        "stem": "You want to reach an Azure storage account from your virtual network using a private IP "
                "address so traffic never crosses the public internet. What should you configure?",
        "options": [
            {"id": "A", "text": "A private endpoint"},
            {"id": "B", "text": "A public endpoint"},
            {"id": "C", "text": "An Azure DNS zone by itself"},
            {"id": "D", "text": "A VPN Gateway to the storage account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A private endpoint uses Azure Private Link to give the service a private IP inside your "
                       "virtual network, keeping traffic off the public internet.",
            "distractors": {
                "B": "A public endpoint is internet-facing, the opposite of what is required.",
                "C": "A DNS zone resolves names but does not by itself move traffic onto a private path.",
                "D": "A VPN Gateway connects whole networks; it does not attach a private IP to an individual PaaS service.",
            },
            "exam_pattern": "Private IP to a PaaS service, off the internet = private endpoint (Private Link).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure networking (virtual networks, VPN Gateway, ExpressRoute, DNS)"],
    },
    {
        "id": "az900-arch-022", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 1, "type": "mcq",
        "stem": "Your team wants to host your domain's DNS records in Azure and resolve names using "
                "Microsoft's global name servers. Which service provides this?",
        "options": [
            {"id": "A", "text": "Azure DNS"},
            {"id": "B", "text": "VPN Gateway"},
            {"id": "C", "text": "Azure Functions"},
            {"id": "D", "text": "An availability set"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure DNS hosts your DNS domains and records and resolves names using Microsoft's "
                       "global DNS infrastructure.",
            "distractors": {
                "B": "A VPN Gateway provides encrypted connectivity, not DNS hosting.",
                "C": "Azure Functions runs code and does not host DNS zones.",
                "D": "An availability set is a VM resiliency feature, unrelated to DNS.",
            },
            "exam_pattern": "Host DNS records in Azure = Azure DNS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure networking (virtual networks, VPN Gateway, ExpressRoute, DNS)"],
    },
    {
        "id": "az900-arch-023", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_compute_networking", "difficulty": 3, "type": "multi",
        "stem": "Your architect wants compute options where Azure manages the operating system for you. "
                "Which TWO of the following are platform-as-a-service (PaaS) options? (Choose two.)",
        "options": [
            {"id": "A", "text": "Azure App Service"},
            {"id": "B", "text": "Azure Functions"},
            {"id": "C", "text": "Azure Virtual Machines"},
            {"id": "D", "text": "Virtual machine scale sets"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Azure App Service and Azure Functions are platform/serverless (PaaS) services: Azure "
                       "manages the underlying operating system and infrastructure, and you supply only your "
                       "app or code.",
            "distractors": {
                "C": "Azure Virtual Machines is infrastructure-as-a-service; you manage the guest operating system.",
                "D": "Virtual machine scale sets are groups of VMs, so you still manage their operating system (IaaS).",
            },
            "exam_pattern": "App Service and Functions = PaaS (no OS to manage); VMs and scale sets = IaaS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure compute services (VMs, containers, Azure Functions, App Service)"],
    },

    # ===== az_storage =======================================================
    {
        "id": "az900-arch-024", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 1, "type": "mcq",
        "stem": "Your application must store millions of images and video files as objects with massive "
                "scalability. Which Azure Storage service is designed for this?",
        "options": [
            {"id": "A", "text": "Blob storage"},
            {"id": "B", "text": "Queue storage"},
            {"id": "C", "text": "Disk storage"},
            {"id": "D", "text": "Table storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Blob storage is Azure's object store for unstructured data such as images, video, "
                       "documents, and backups, and it scales massively.",
            "distractors": {
                "B": "Queue storage holds messages for component communication, not large media objects.",
                "C": "Disk storage provides block volumes attached to VMs, not an object store.",
                "D": "Table storage is a NoSQL key-value store, not an object store for media files.",
            },
            "exam_pattern": "Unstructured objects (images, video, backups) = Blob storage.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-025", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 1, "type": "mcq",
        "stem": "You need a fully managed file share that multiple VMs and on-premises machines can mount "
                "over SMB. Which storage option fits?",
        "options": [
            {"id": "A", "text": "Azure Files"},
            {"id": "B", "text": "Blob storage"},
            {"id": "C", "text": "Queue storage"},
            {"id": "D", "text": "Managed disks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Files provides fully managed file shares accessible over SMB (and NFS) that cloud "
                       "and on-premises machines can mount concurrently.",
            "distractors": {
                "B": "Blob storage serves objects through HTTP APIs, not a mountable SMB file share.",
                "C": "Queue storage holds messages, not files.",
                "D": "A managed disk attaches to a single VM and is not a shared file share.",
            },
            "exam_pattern": "Managed SMB file share mountable by many clients = Azure Files.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-026", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 1, "type": "mcq",
        "stem": "An Azure VM needs a block-level storage volume that behaves like a physical hard drive "
                "attached to it. Which storage type is this?",
        "options": [
            {"id": "A", "text": "A managed disk"},
            {"id": "B", "text": "A blob container"},
            {"id": "C", "text": "An Azure Files share"},
            {"id": "D", "text": "Queue storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Managed disks are block-level storage volumes attached to Azure VMs, functioning like a "
                       "hard drive for the VM.",
            "distractors": {
                "B": "A blob container stores objects, not a block volume for a VM's operating system or data disk.",
                "C": "An Azure Files share is a network file share, not a VM block disk.",
                "D": "Queue storage holds messages and is not block storage.",
            },
            "exam_pattern": "Block volume attached to a VM = managed disk.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-027", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "Two parts of your application must exchange large numbers of messages asynchronously so "
                "they can scale independently. Which storage service suits this?",
        "options": [
            {"id": "A", "text": "Queue storage"},
            {"id": "B", "text": "Disk storage"},
            {"id": "C", "text": "Blob storage"},
            {"id": "D", "text": "Azure Files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Queue storage stores large numbers of messages, letting application components "
                       "communicate asynchronously and scale independently.",
            "distractors": {
                "B": "Disk storage provides VM volumes, not a messaging queue.",
                "C": "Blob storage holds objects, not a message queue for decoupling components.",
                "D": "Azure Files provides file shares, not asynchronous messaging.",
            },
            "exam_pattern": "Async messages between components = Queue storage.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-028", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "Which redundancy option keeps three copies of your data within a single datacenter in "
                "the primary region at the lowest cost?",
        "options": [
            {"id": "A", "text": "Locally redundant storage (LRS)"},
            {"id": "B", "text": "Zone-redundant storage (ZRS)"},
            {"id": "C", "text": "Geo-redundant storage (GRS)"},
            {"id": "D", "text": "Geo-zone-redundant storage (GZRS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LRS replicates data three times within a single datacenter in the primary region; it is "
                       "the lowest-cost option but does not survive a datacenter outage.",
            "distractors": {
                "B": "ZRS copies data across availability zones, not within a single datacenter.",
                "C": "GRS also replicates to a second region, so it is not confined to one datacenter.",
                "D": "GZRS combines zone and geo redundancy and is not confined to a single datacenter.",
            },
            "exam_pattern": "Three copies in one datacenter, cheapest = LRS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-029", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "You must keep storage available even if an entire datacenter in the region fails, while "
                "keeping all copies within that one region. Which option fits?",
        "options": [
            {"id": "A", "text": "Zone-redundant storage (ZRS)"},
            {"id": "B", "text": "Locally redundant storage (LRS)"},
            {"id": "C", "text": "Geo-redundant storage (GRS)"},
            {"id": "D", "text": "Read-access geo-redundant storage (RA-GRS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ZRS replicates data synchronously across three availability zones within the primary "
                       "region, so it survives a single datacenter (zone) failure while staying in-region.",
            "distractors": {
                "B": "LRS keeps all copies in one datacenter, so a datacenter failure could lose access.",
                "C": "GRS copies data to a second region, which goes beyond the in-region requirement.",
                "D": "RA-GRS also replicates to a second region, so copies leave the single region.",
            },
            "exam_pattern": "Survive a datacenter loss while staying in one region = ZRS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-030", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "Your compliance policy requires storage data to survive a complete regional outage by "
                "replicating to Azure's paired region. Which redundancy option provides this?",
        "options": [
            {"id": "A", "text": "Geo-redundant storage (GRS)"},
            {"id": "B", "text": "Locally redundant storage (LRS)"},
            {"id": "C", "text": "Zone-redundant storage (ZRS)"},
            {"id": "D", "text": "The hot access tier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GRS replicates data to the paired secondary region in addition to the primary, so it "
                       "survives a complete regional outage.",
            "distractors": {
                "B": "LRS stays in one datacenter and cannot survive a regional outage.",
                "C": "ZRS stays within the primary region, so a full regional outage could still affect it.",
                "D": "The hot tier is an access-frequency setting, not a redundancy option at all.",
            },
            "exam_pattern": "Survive a whole-region outage via the paired region = GRS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-031", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 3, "type": "mcq",
        "stem": "You want the highest durability: zone redundancy within the primary region plus "
                "replication to the paired region. Which option combines both?",
        "options": [
            {"id": "A", "text": "Geo-zone-redundant storage (GZRS)"},
            {"id": "B", "text": "Zone-redundant storage (ZRS)"},
            {"id": "C", "text": "Geo-redundant storage (GRS)"},
            {"id": "D", "text": "Locally redundant storage (LRS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GZRS writes data across availability zones in the primary region (like ZRS) and also "
                       "replicates to the paired secondary region, combining zone and geo protection.",
            "distractors": {
                "B": "ZRS protects across zones but does not replicate to a second region.",
                "C": "GRS replicates to a second region but keeps the primary copy as LRS, not zone-redundant.",
                "D": "LRS is single-datacenter, offering neither zone nor geo redundancy.",
            },
            "exam_pattern": "Zone redundancy plus geo replication = GZRS.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage services and redundancy"],
    },
    {
        "id": "az900-arch-032", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "You must retain compliance backups that are almost never read, at the lowest storage "
                "cost, and can tolerate hours of retrieval latency. Which blob access tier fits?",
        "options": [
            {"id": "A", "text": "Archive"},
            {"id": "B", "text": "Hot"},
            {"id": "C", "text": "Cool"},
            {"id": "D", "text": "Cold"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The archive tier offers the lowest storage cost for rarely accessed data, but it is "
                       "offline, so data must be rehydrated (which can take hours) before it can be read.",
            "distractors": {
                "B": "The hot tier is optimized for frequent access with the highest storage cost.",
                "C": "The cool tier is for infrequently accessed data that still stays online and readily available.",
                "D": "The cold tier stores rarely accessed data online, without archive's lowest cost or hours-long rehydration.",
            },
            "exam_pattern": "Rarely read, cheapest storage, retrieval delay acceptable = archive tier.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage access tiers"],
    },
    {
        "id": "az900-arch-033", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 1, "type": "mcq",
        "stem": "A dataset is read many times every day and must return immediately. Which blob access "
                "tier minimizes access (read) costs for this pattern?",
        "options": [
            {"id": "A", "text": "Hot"},
            {"id": "B", "text": "Cool"},
            {"id": "C", "text": "Archive"},
            {"id": "D", "text": "Cold"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The hot tier has the highest storage cost but the lowest access cost and immediate "
                       "availability, making it ideal for frequently read data.",
            "distractors": {
                "B": "The cool tier lowers storage cost but raises access cost, so frequent reads become expensive.",
                "C": "The archive tier is offline and requires rehydration, so it cannot return data immediately.",
                "D": "The cold tier targets rarely accessed data and has higher access costs than hot.",
            },
            "exam_pattern": "Frequent reads with instant access = hot tier.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure storage access tiers"],
    },
    {
        "id": "az900-arch-034", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "You must move 80 TB into Azure, but your internet link is too slow to transfer it in "
                "reasonable time. Which option fits?",
        "options": [
            {"id": "A", "text": "Azure Data Box"},
            {"id": "B", "text": "AzCopy over the internet"},
            {"id": "C", "text": "Azure DNS"},
            {"id": "D", "text": "A private endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Data Box is a physical appliance Microsoft ships to you so you can load data "
                       "locally and return it, ideal for large offline transfers when the network is impractical.",
            "distractors": {
                "B": "AzCopy transfers over the network, which the scenario says is too slow for this volume.",
                "C": "Azure DNS resolves names and has nothing to do with bulk data transfer.",
                "D": "A private endpoint controls a network access path, not bulk offline migration.",
            },
            "exam_pattern": "Huge offline transfer when the network is too slow = Data Box.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure data migration options (Azure Migrate, Azure Data Box, AzCopy)"],
    },
    {
        "id": "az900-arch-035", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a command-line tool to copy blobs and files to and from Azure "
                "Storage over the network with scriptable commands. Which tool fits?",
        "options": [
            {"id": "A", "text": "AzCopy"},
            {"id": "B", "text": "Azure Data Box"},
            {"id": "C", "text": "Azure Migrate"},
            {"id": "D", "text": "Azure Monitor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AzCopy is a command-line utility for copying data to and from Blob and Azure Files "
                       "storage over the network, well suited to scripted transfers.",
            "distractors": {
                "B": "Azure Data Box is a physical appliance for offline transfer, not a command-line tool.",
                "C": "Azure Migrate discovers and migrates servers and workloads, not simple scripted file copies.",
                "D": "Azure Monitor collects telemetry and does not copy storage data.",
            },
            "exam_pattern": "Scriptable command-line copy to/from storage = AzCopy.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure data migration options (Azure Migrate, Azure Data Box, AzCopy)"],
    },
    {
        "id": "az900-arch-036", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_storage", "difficulty": 2, "type": "mcq",
        "stem": "Before moving to Azure, your team wants to discover on-premises servers, assess their "
                "readiness, and then migrate them. Which service is the central hub for this?",
        "options": [
            {"id": "A", "text": "Azure Migrate"},
            {"id": "B", "text": "AzCopy"},
            {"id": "C", "text": "Azure DNS"},
            {"id": "D", "text": "Azure Files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Migrate is a central hub to discover, assess, and migrate on-premises servers, "
                       "databases, and other workloads to Azure.",
            "distractors": {
                "B": "AzCopy only copies storage data; it does not assess or migrate servers.",
                "C": "Azure DNS resolves names and is unrelated to migration assessment.",
                "D": "Azure Files provides file shares, not a migration assessment and move service.",
            },
            "exam_pattern": "Discover, assess, and migrate servers to Azure = Azure Migrate.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Azure data migration options (Azure Migrate, Azure Data Box, AzCopy)"],
    },

    # ===== az_identity ======================================================
    {
        "id": "az900-arch-037", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 1, "type": "mcq",
        "stem": "Which Azure service provides cloud-based identity and access management for users "
                "signing in to applications, and was formerly called Azure Active Directory?",
        "options": [
            {"id": "A", "text": "Microsoft Entra ID"},
            {"id": "B", "text": "Azure Blob Storage"},
            {"id": "C", "text": "Azure Virtual Network"},
            {"id": "D", "text": "Azure Resource Manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra ID (formerly Azure Active Directory) is Azure's cloud identity and "
                       "access management service for users, groups, and application sign-in.",
            "distractors": {
                "B": "Blob Storage stores data objects and does not manage identities.",
                "C": "A virtual network provides networking, not identity services.",
                "D": "Azure Resource Manager deploys and manages resources; it is not an identity service.",
            },
            "exam_pattern": "Cloud identity and access management = Microsoft Entra ID (formerly Azure AD).",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra ID"],
    },
    {
        "id": "az900-arch-038", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 1, "type": "mcq",
        "stem": "When a user signs in and the system verifies their identity by checking their "
                "credentials, which process is taking place?",
        "options": [
            {"id": "A", "text": "Authentication"},
            {"id": "B", "text": "Authorization"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "Encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authentication is the process of verifying who a user is, typically by checking "
                       "credentials such as a password.",
            "distractors": {
                "B": "Authorization determines what an already-identified user may do, which is a later step.",
                "C": "Load balancing distributes network traffic and is unrelated to verifying identity.",
                "D": "Encryption protects data confidentiality; it is not identity verification.",
            },
            "exam_pattern": "Proving who you are = authentication.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication and authorization"],
    },
    {
        "id": "az900-arch-039", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "After a user has signed in, Azure checks whether they are permitted to delete a "
                "particular resource. Which process does this permission check represent?",
        "options": [
            {"id": "A", "text": "Authorization"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Single sign-on"},
            {"id": "D", "text": "Multi-factor authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authorization determines what an authenticated user is allowed to do, such as whether "
                       "they may delete a resource.",
            "distractors": {
                "B": "Authentication verifies identity and happens before the permission check.",
                "C": "Single sign-on reduces repeated sign-ins; it does not decide permissions.",
                "D": "Multi-factor authentication strengthens sign-in, not what actions are permitted.",
            },
            "exam_pattern": "Deciding what you are allowed to do = authorization.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication and authorization"],
    },
    {
        "id": "az900-arch-040", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 1, "type": "mcq",
        "stem": "Your employees want to sign in once and then open many different applications without "
                "re-entering their password each time. Which capability provides this?",
        "options": [
            {"id": "A", "text": "Single sign-on"},
            {"id": "B", "text": "Multi-factor authentication"},
            {"id": "C", "text": "Locally redundant storage"},
            {"id": "D", "text": "ExpressRoute"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Single sign-on (SSO) lets a user authenticate once and then access multiple "
                       "applications without signing in again for each one.",
            "distractors": {
                "B": "Multi-factor authentication adds verification steps, increasing prompts rather than reducing them.",
                "C": "Locally redundant storage is a data-redundancy option, unrelated to sign-in.",
                "D": "ExpressRoute is a connectivity service and has nothing to do with sign-in.",
            },
            "exam_pattern": "Sign in once, reach many apps = single sign-on.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication and authorization"],
    },
    {
        "id": "az900-arch-041", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 1, "type": "mcq",
        "stem": "To harden sign-ins, you require users to provide both a password and a one-time code "
                "from their phone. What is this practice called?",
        "options": [
            {"id": "A", "text": "Multi-factor authentication"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multi-factor authentication (MFA) requires two or more independent verification factors, "
                       "such as a password plus a phone code, strengthening sign-in security.",
            "distractors": {
                "B": "Single sign-on reduces repeated sign-ins; it does not add verification factors.",
                "C": "Authorization governs permissions after sign-in, not the number of sign-in factors.",
                "D": "Conditional Access is a policy engine that can require MFA, but the act of providing two factors is MFA itself.",
            },
            "exam_pattern": "Two or more verification factors = multi-factor authentication.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe authentication and authorization"],
    },
    {
        "id": "az900-arch-042", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "You want to block sign-ins from outside your country and require extra verification when "
                "access comes from an unmanaged device. Which Entra ID feature enforces such if-then rules?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Azure DNS"},
            {"id": "D", "text": "Availability zones"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access applies if-then policies that use signals such as location, device "
                       "state, and risk to allow, block, or add requirements like MFA.",
            "distractors": {
                "B": "Single sign-on streamlines sign-in but does not evaluate access conditions.",
                "C": "Azure DNS resolves names and does not enforce access policy.",
                "D": "Availability zones are a resiliency feature, unrelated to access policies.",
            },
            "exam_pattern": "Signal-based if-then access rules = Conditional Access.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Conditional Access"],
    },
    {
        "id": "az900-arch-043", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "Your company must let partner-organization users access a shared app using their own "
                "existing credentials as guests. Which capability supports this?",
        "options": [
            {"id": "A", "text": "Microsoft Entra External ID business-to-business (B2B) collaboration"},
            {"id": "B", "text": "Business-to-consumer (B2C) identities"},
            {"id": "C", "text": "Locally redundant storage"},
            {"id": "D", "text": "A VPN Gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "B2B collaboration, part of Microsoft Entra External ID, invites external partners as "
                       "guest users who sign in with their own organization's credentials.",
            "distractors": {
                "B": "B2C is for consumer/customer identities on customer-facing apps, not partner guest access.",
                "C": "Locally redundant storage is a data-redundancy option, not an identity feature.",
                "D": "A VPN Gateway provides network connectivity, not external guest identity.",
            },
            "exam_pattern": "Partner guests using their own credentials = Entra External ID B2B.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra External ID"],
    },
    {
        "id": "az900-arch-044", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "You are building a public shopping app where millions of customers create their own "
                "accounts or sign in with social logins. Which identity solution is designed for this?",
        "options": [
            {"id": "A", "text": "Microsoft Entra External ID for customers (business-to-consumer, B2C)"},
            {"id": "B", "text": "Business-to-business (B2B) collaboration"},
            {"id": "C", "text": "On-premises Active Directory Domain Services"},
            {"id": "D", "text": "Azure Files"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Customer identity (B2C, part of Microsoft Entra External ID) handles consumer sign-up "
                       "and sign-in, including social identity providers, for customer-facing apps at scale.",
            "distractors": {
                "B": "B2B collaboration is for partner organizations, not millions of consumer customers.",
                "C": "On-premises Active Directory Domain Services manages internal corporate identities, not public customer accounts.",
                "D": "Azure Files is a storage service and does not manage customer identities.",
            },
            "exam_pattern": "Consumer-facing sign-up/sign-in with social logins = Entra External ID B2C.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra External ID"],
    },
    {
        "id": "az900-arch-045", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 3, "type": "mcq",
        "stem": "A colleague assumes Microsoft Entra ID is simply on-premises Active Directory running in "
                "the cloud. Which statement correctly distinguishes them?",
        "options": [
            {"id": "A", "text": "Entra ID is a cloud identity service using internet protocols such as HTTP/HTTPS; it is not a lifted-and-shifted on-premises AD domain controller"},
            {"id": "B", "text": "Entra ID and on-premises AD are identical in features and structure"},
            {"id": "C", "text": "Entra ID uses organizational units and Group Policy exactly like on-premises AD"},
            {"id": "D", "text": "On-premises AD is a cloud-only service that has no domain controllers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Entra ID is cloud-based and uses internet protocols (HTTP/HTTPS) for web and cloud app "
                       "identity; it is not the same as on-premises AD Domain Services, which uses protocols "
                       "like LDAP and Kerberos with domain controllers.",
            "distractors": {
                "B": "They differ in structure and capabilities; they are not identical.",
                "C": "Organizational units and Group Policy are on-premises AD DS features, not how Entra ID works.",
                "D": "On-premises Active Directory runs on domain controllers you operate; it is not cloud-only.",
            },
            "exam_pattern": "Entra ID is cloud identity, not a cloud-hosted on-premises domain controller.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra ID"],
    },
    {
        "id": "az900-arch-046", "exam": "az900", "domain": "az_architecture_services",
        "subtopic": "az_identity", "difficulty": 2, "type": "mcq",
        "stem": "A teammate suggests using Microsoft Entra ID to store the company's large video files. "
                "Why is that the wrong tool?",
        "options": [
            {"id": "A", "text": "Entra ID is an identity and access service, not a data store; large files belong in Blob storage"},
            {"id": "B", "text": "Entra ID can store files, but only those under 1 GB"},
            {"id": "C", "text": "Entra ID stores files only in the archive access tier"},
            {"id": "D", "text": "Entra ID stores files but cannot authenticate users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra ID manages identities and access, not data storage; large media files "
                       "belong in Blob storage, which is built for unstructured objects.",
            "distractors": {
                "B": "Entra ID is not a file store at all, so a size limit for stored files does not apply.",
                "C": "Access tiers are a Blob storage concept, not an Entra ID capability.",
                "D": "Authenticating users is exactly what Entra ID does; the false claim is that it stores files.",
            },
            "exam_pattern": "Entra ID = identity, not a storage or networking service.",
        },
        "references": ["Microsoft Learn (AZ-900): Describe Microsoft Entra ID"],
    },
]
