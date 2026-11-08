"""Microsoft Azure Fundamentals (AZ-900) EXPANSION pool — Domain 3:
Describe Azure management and governance.

Original, objective-aligned practice items covering all three Domain 3
subtopics: az_cost_management, az_governance_compliance, and
az_tools_monitoring. Never real or memorized exam items.

Fundamentals depth only: items describe conceptual roles and relationships
(e.g. "egress is billed, ingress is free", "Policy governs what, RBAC governs
who") and deliberately avoid exact prices, percentages, and service limits that
drift over time. Every item names a relevant Microsoft Learn area in
`references`.

Authoring rules match the other pools: build_content.py shuffles option order
(seeded by id) so the answer key here is not positionally biased, and every
wrong option carries a distractor note. The pool is discovered and merged by
build_content's ``content_<exam>_*.py`` glob once an ``az900`` blueprint and a
base ``content_az900`` module are registered.
"""

QUESTIONS = [
    # ===== az_cost_management ===============================================
    {
        "id": "az900-gov-001", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 1, "type": "mcq",
        "stem": "Before deploying anything, a team wants to estimate the monthly cost of a planned "
                "Azure VM and storage design. Which tool should they use?",
        "options": [
            {"id": "A", "text": "Azure Pricing Calculator"},
            {"id": "B", "text": "Azure TCO Calculator"},
            {"id": "C", "text": "Microsoft Cost Management"},
            {"id": "D", "text": "Azure Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Pricing Calculator lets you configure Azure services, regions, and tiers "
                       "to produce a cost estimate for a solution before you deploy it.",
            "distractors": {
                "B": "The TCO Calculator compares on-premises costs against Azure; it is not for "
                     "estimating a greenfield Azure-only design.",
                "C": "Cost Management analyzes spending on resources you have already deployed, not a "
                     "pre-deployment estimate.",
                "D": "Advisor gives best-practice recommendations on existing resources, not cost "
                     "estimates for planned ones.",
            },
            "exam_pattern": "'Estimate cost before deploying' = Pricing Calculator.",
        },
        "references": ["Azure Pricing Calculator"],
    },
    {
        "id": "az900-gov-002", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a migration business case comparing its current on-premises "
                "datacenter cost against equivalent Azure services. Which tool fits?",
        "options": [
            {"id": "A", "text": "Azure TCO Calculator"},
            {"id": "B", "text": "Azure Pricing Calculator"},
            {"id": "C", "text": "Microsoft Cost Management"},
            {"id": "D", "text": "Azure Service Health"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Total Cost of Ownership (TCO) Calculator models current on-premises costs "
                       "and compares them with the projected cost of running the same workloads in Azure.",
            "distractors": {
                "B": "The Pricing Calculator only estimates Azure service costs; it does not capture "
                     "on-premises costs for comparison.",
                "C": "Cost Management reports on money already spent in Azure, not an on-premises vs "
                     "Azure comparison.",
                "D": "Service Health reports Azure service outages and maintenance, not cost comparisons.",
            },
            "exam_pattern": "'Compare on-premises vs Azure' = TCO Calculator.",
        },
        "references": ["Azure TCO Calculator"],
    },
    {
        "id": "az900-gov-003", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "After months of running Azure workloads, finance wants to analyze actual spending and "
                "see which service costs the most. Which tool should they open?",
        "options": [
            {"id": "A", "text": "Microsoft Cost Management"},
            {"id": "B", "text": "Azure Pricing Calculator"},
            {"id": "C", "text": "Azure TCO Calculator"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Cost Management provides cost analysis of actual billed usage, "
                       "letting you break spend down by service, resource group, or tag.",
            "distractors": {
                "B": "The Pricing Calculator produces pre-deployment estimates, not reports of real "
                     "spending.",
                "C": "The TCO Calculator compares on-premises and Azure costs; it does not analyze "
                     "your live Azure bill.",
                "D": "Azure Policy enforces resource rules; it does not report spending.",
            },
            "exam_pattern": "'Analyze actual/real spend' = Microsoft Cost Management.",
        },
        "references": ["Microsoft Cost Management"],
    },
    {
        "id": "az900-gov-004", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants an automatic email when subscription spending reaches a set "
                "percentage of the monthly limit. What should they configure in Cost Management?",
        "options": [
            {"id": "A", "text": "A budget with an alert threshold"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "An Azure Policy assignment"},
            {"id": "D", "text": "A Service Health alert"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In Microsoft Cost Management you create a budget and set alert thresholds that "
                       "email recipients when spending approaches the defined limit.",
            "distractors": {
                "B": "A resource lock prevents deletion or changes to a resource; it has nothing to "
                     "do with spending notifications.",
                "C": "Azure Policy controls which resources can be deployed, not spending alerts.",
                "D": "Service Health alerts notify you about Azure service issues, not your budget.",
            },
            "exam_pattern": "'Notify at a spending threshold' = Cost Management budget + alert.",
        },
        "references": ["Microsoft Cost Management"],
    },
    {
        "id": "az900-gov-005", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 1, "type": "mcq",
        "stem": "Two identical virtual machines are priced differently on the Pricing Calculator. "
                "Which factor most likely explains the difference?",
        "options": [
            {"id": "A", "text": "The Azure region each VM is deployed to"},
            {"id": "B", "text": "The display name given to each VM"},
            {"id": "C", "text": "The tags applied to each VM"},
            {"id": "D", "text": "The resource group each VM sits in"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Prices for the same resource vary by region because of differing datacenter "
                       "and operating costs, so region is a genuine cost factor.",
            "distractors": {
                "B": "A resource's name is free metadata and never changes its price.",
                "C": "Tags are billing and organization labels; applying them does not change a "
                     "resource's price.",
                "D": "Placing a resource in a different resource group does not change its price; "
                     "resource groups are free containers.",
            },
            "exam_pattern": "Same resource, different price = region is the usual cause.",
        },
        "references": ["Azure cost factors"],
    },
    {
        "id": "az900-gov-006", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A solution moves large amounts of data in and out of an Azure region. Which data "
                "transfer typically appears as a charge on the bill?",
        "options": [
            {"id": "A", "text": "Outbound data leaving the Azure region to the internet"},
            {"id": "B", "text": "Inbound data uploaded into the Azure region"},
            {"id": "C", "text": "Data written to a managed disk in the same region"},
            {"id": "D", "text": "A VM reading from its own attached OS disk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Outbound (egress) data transfer leaving an Azure datacenter or region is "
                       "generally billed, which is why high outbound traffic raises costs.",
            "distractors": {
                "B": "Inbound (ingress) data into an Azure datacenter is generally free.",
                "C": "Writing to a disk in the same region is storage activity, not billed internet "
                     "egress.",
                "D": "A VM reading its own OS disk is not internet data transfer and is not billed as "
                     "egress.",
            },
            "exam_pattern": "Ingress usually free, egress usually billed.",
        },
        "references": ["Azure cost factors"],
    },
    {
        "id": "az900-gov-007", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 1, "type": "mcq",
        "stem": "A company wants its Azure bill broken down by department so each team's spend is "
                "visible. What should they apply to resources?",
        "options": [
            {"id": "A", "text": "Resource tags"},
            {"id": "B", "text": "Resource locks"},
            {"id": "C", "text": "RBAC role assignments"},
            {"id": "D", "text": "Azure Policy definitions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tags are name/value pairs (such as Department:Finance) attached to resources; "
                       "Cost Management can then group and filter spending by tag.",
            "distractors": {
                "B": "Resource locks prevent deletion or changes; they do not categorize costs.",
                "C": "RBAC assignments control who can access resources, not how costs are grouped.",
                "D": "Azure Policy enforces configuration rules; it does not break the bill down by "
                     "team.",
            },
            "exam_pattern": "'Group or track cost by team or project' = tags.",
        },
        "references": ["Azure resource tags"],
    },
    {
        "id": "az900-gov-008", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "To cut costs, an admin stops (deallocates) a development VM every night. For the "
                "hours it is deallocated, what is still billed?",
        "options": [
            {"id": "A", "text": "Its attached managed disk storage"},
            {"id": "B", "text": "Its virtual CPU and memory compute"},
            {"id": "C", "text": "Nothing at all is billed"},
            {"id": "D", "text": "Only its operating system license"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Deallocating a VM stops compute (vCPU/RAM) billing, but the managed disks "
                       "that store the VM stay provisioned and keep incurring storage charges.",
            "distractors": {
                "B": "Compute billing stops while a VM is deallocated, so vCPU and memory is exactly "
                     "what you are no longer paying for.",
                "C": "Storage for the VM's disks persists and is still billed, so leaving a "
                     "deallocated VM in place is not free.",
                "D": "Charges continue for the disks regardless of licensing; an OS license alone "
                     "does not describe the ongoing cost.",
            },
            "exam_pattern": "Deallocated VM = no compute charge, but disks still cost.",
        },
        "references": ["Azure cost factors"],
    },
    {
        "id": "az900-gov-009", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A production database VM runs 24/7 with steady, predictable usage for the next three "
                "years. Which option most reduces its compute cost?",
        "options": [
            {"id": "A", "text": "Purchase an Azure Reservation"},
            {"id": "B", "text": "Switch it to Azure Spot capacity"},
            {"id": "C", "text": "Keep it on pay-as-you-go"},
            {"id": "D", "text": "Apply a ReadOnly resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Reservations give a discount in exchange for a one- or three-year "
                       "commitment, which suits steady, always-on workloads with predictable usage.",
            "distractors": {
                "B": "Azure Spot offers deep discounts but can be evicted at any time, so it is "
                     "unsuitable for an always-on production database.",
                "C": "Pay-as-you-go carries no commitment discount, so it is the more expensive "
                     "option for steady long-term usage.",
                "D": "A resource lock protects against deletion or changes and has no effect on price.",
            },
            "exam_pattern": "'Steady, long-term, predictable' + save money = Reservations.",
        },
        "references": ["Azure Reservations"],
    },
    {
        "id": "az900-gov-010", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "An architect must choose between Premium SSD and Standard HDD managed disks. "
                "Regarding cost, which statement is correct?",
        "options": [
            {"id": "A", "text": "The higher-performance Premium SSD tier costs more than Standard HDD"},
            {"id": "B", "text": "Both disk tiers cost exactly the same"},
            {"id": "C", "text": "Disk tier never affects price, only region does"},
            {"id": "D", "text": "Standard HDD costs more because it is an older technology"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resource type and performance tier are cost factors; higher-performance "
                       "Premium SSD disks are priced above lower-performance Standard HDD disks.",
            "distractors": {
                "B": "Different performance tiers are priced differently, so they are not the same "
                     "cost.",
                "C": "Both tier and region affect price; tier is a real cost factor, not irrelevant.",
                "D": "Standard HDD is the lower-cost tier, not the more expensive one.",
            },
            "exam_pattern": "Higher performance tier/SKU = higher price.",
        },
        "references": ["Azure cost factors"],
    },
    {
        "id": "az900-gov-011", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "A colleague treats the figure from the Pricing Calculator as the exact amount the "
                "company will be invoiced. Why is that assumption wrong?",
        "options": [
            {"id": "A", "text": "It is a planning estimate; the real charge depends on actual usage"},
            {"id": "B", "text": "The Pricing Calculator always overstates cost by design"},
            {"id": "C", "text": "The Pricing Calculator only works after resources are deployed"},
            {"id": "D", "text": "The Pricing Calculator reports last month's invoice totals"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Pricing Calculator produces an estimate from the configuration you enter; "
                       "the actual bill reflects real consumption and is tracked in Cost Management.",
            "distractors": {
                "B": "The calculator is neither deliberately high nor low; it estimates from your "
                     "inputs, which may differ from real usage.",
                "C": "It is a pre-deployment planning tool and does not require any resources to exist.",
                "D": "It does not read invoices; reviewing actual billed amounts is the job of Cost "
                     "Management.",
            },
            "exam_pattern": "Pricing Calculator = estimate; Cost Management = actual spend.",
        },
        "references": ["Azure Pricing Calculator"],
    },
    {
        "id": "az900-gov-012", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 1, "type": "mcq",
        "stem": "Under Azure's pay-as-you-go model, what most directly determines the size of a "
                "workload's monthly compute bill?",
        "options": [
            {"id": "A", "text": "How much the resources are actually used"},
            {"id": "B", "text": "How many tags are applied"},
            {"id": "C", "text": "How many resource groups exist"},
            {"id": "D", "text": "The color theme set in the Azure portal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Pay-as-you-go is consumption-based billing: you are charged for the resources "
                       "you actually use, so usage is the main cost driver.",
            "distractors": {
                "B": "Tags are free labels for organization and reporting; they do not drive the bill.",
                "C": "Resource groups are free logical containers and do not themselves generate "
                     "charges.",
                "D": "Portal appearance settings have no effect on billing.",
            },
            "exam_pattern": "Consumption / pay-as-you-go = you pay for what you use.",
        },
        "references": ["Azure cost factors"],
    },
    {
        "id": "az900-gov-013", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A manager wants to be warned specifically about an unexpected spike in Azure "
                "spending. Which service provides that alert?",
        "options": [
            {"id": "A", "text": "Microsoft Cost Management"},
            {"id": "B", "text": "Azure Service Health"},
            {"id": "C", "text": "Azure Advisor"},
            {"id": "D", "text": "Application Insights"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cost Management provides cost alerts (including anomaly and budget alerts) "
                       "that warn you when spending behaves unexpectedly or crosses a threshold.",
            "distractors": {
                "B": "Service Health alerts cover Azure service outages and maintenance, not your "
                     "spending.",
                "C": "Advisor offers improvement recommendations, including some cost tips, but is "
                     "not the spending-spike alerting tool.",
                "D": "Application Insights monitors application performance, not costs.",
            },
            "exam_pattern": "Spending alerts come from Cost Management, not Service Health.",
        },
        "references": ["Microsoft Cost Management"],
    },

    # ===== az_governance_compliance ========================================
    {
        "id": "az900-gov-014", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "mcq",
        "stem": "An organization must guarantee that resources are only ever created in approved "
                "Azure regions. Which service enforces this rule automatically?",
        "options": [
            {"id": "A", "text": "Azure Policy"},
            {"id": "B", "text": "Azure RBAC"},
            {"id": "C", "text": "A resource lock"},
            {"id": "D", "text": "Service Trust Portal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Policy evaluates resources against rules and can deny deployments that "
                       "violate them, such as creating a resource in a non-approved region.",
            "distractors": {
                "B": "RBAC controls which identities may perform actions; it does not restrict which "
                     "regions a resource may use.",
                "C": "A resource lock prevents deletion or modification of existing resources; it does "
                     "not restrict allowed regions.",
                "D": "The Service Trust Portal hosts Microsoft's compliance reports; it does not "
                     "enforce your deployment rules.",
            },
            "exam_pattern": "'Enforce what can be deployed / allowed config' = Azure Policy.",
        },
        "references": ["Azure Policy"],
    },
    {
        "id": "az900-gov-015", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "An Azure Policy must stop anyone from creating a disallowed VM size at deployment "
                "time. Which policy effect achieves this?",
        "options": [
            {"id": "A", "text": "Deny"},
            {"id": "B", "text": "Audit"},
            {"id": "C", "text": "Append"},
            {"id": "D", "text": "Disabled"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Deny effect blocks a non-compliant resource request, preventing the "
                       "disallowed VM size from being created.",
            "distractors": {
                "B": "The Audit effect only flags non-compliance in reports; it still allows the "
                     "resource to be created.",
                "C": "Append adds fields to a resource; it does not block a disallowed size.",
                "D": "Disabled turns the policy off, so it would enforce nothing.",
            },
            "exam_pattern": "'Block or prevent non-compliant creation' = Deny effect.",
        },
        "references": ["Azure Policy"],
    },
    {
        "id": "az900-gov-016", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "mcq",
        "stem": "A team member should be allowed to manage virtual machines but not networking "
                "resources. Which Azure feature grants this scoped permission?",
        "options": [
            {"id": "A", "text": "An Azure RBAC role assignment"},
            {"id": "B", "text": "Azure Policy"},
            {"id": "C", "text": "A CanNotDelete lock"},
            {"id": "D", "text": "Microsoft Purview"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure role-based access control (RBAC) assigns roles at a scope to control "
                       "who can perform which actions, so you can grant VM management without "
                       "networking rights.",
            "distractors": {
                "B": "Azure Policy governs what resource configurations are allowed, not which users "
                     "may perform actions.",
                "C": "A resource lock prevents deletion or changes for everyone; it does not grant "
                     "per-user permissions.",
                "D": "Microsoft Purview is for data governance, not Azure permission assignment.",
            },
            "exam_pattern": "'Who can do what' = RBAC; 'what is allowed' = Policy.",
        },
        "references": ["Azure RBAC"],
    },
    {
        "id": "az900-gov-017", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "mcq",
        "stem": "An admin wants to protect a critical resource from accidental deletion while still "
                "allowing its settings to be changed. Which lock should they apply?",
        "options": [
            {"id": "A", "text": "CanNotDelete"},
            {"id": "B", "text": "ReadOnly"},
            {"id": "C", "text": "An Azure Policy Deny"},
            {"id": "D", "text": "A Reader role"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CanNotDelete lock lets authorized users read and modify a resource but "
                       "blocks its deletion, protecting against accidental removal.",
            "distractors": {
                "B": "A ReadOnly lock would also block the configuration changes the admin wants to "
                     "keep allowing.",
                "C": "An Azure Policy Deny governs resource properties at creation or update; it is "
                     "not the tool for delete-protecting one specific resource.",
                "D": "A Reader role limits a user to viewing; it does not place deletion protection "
                     "on the resource for everyone.",
            },
            "exam_pattern": "'Prevent deletion but allow edits' = CanNotDelete lock.",
        },
        "references": ["Azure resource locks"],
    },
    {
        "id": "az900-gov-018", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A finished resource must not be modified or deleted by anyone, though it can still "
                "be viewed. Which resource lock enforces this?",
        "options": [
            {"id": "A", "text": "ReadOnly"},
            {"id": "B", "text": "CanNotDelete"},
            {"id": "C", "text": "Azure Policy Audit"},
            {"id": "D", "text": "The Contributor role"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A ReadOnly lock allows users to read a resource but prevents all "
                       "modifications and deletions, even by administrators.",
            "distractors": {
                "B": "A CanNotDelete lock still permits modifications, so it does not fully protect "
                     "the resource from changes.",
                "C": "The Audit policy effect only reports non-compliance; it does not block changes "
                     "or deletions.",
                "D": "The Contributor role grants broad change permissions, the opposite of locking "
                     "the resource.",
            },
            "exam_pattern": "'No changes and no deletion, read-only' = ReadOnly lock.",
        },
        "references": ["Azure resource locks"],
    },
    {
        "id": "az900-gov-019", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A business-critical storage account was deleted by mistake last quarter. Which "
                "control best prevents that specific resource from being deleted again?",
        "options": [
            {"id": "A", "text": "A resource lock set to CanNotDelete"},
            {"id": "B", "text": "An Azure Policy with a Deny effect"},
            {"id": "C", "text": "An RBAC Reader assignment"},
            {"id": "D", "text": "A Cost Management budget alert"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A resource lock directly protects a specific existing resource from deletion "
                       "regardless of a user's RBAC permissions, which fits the accidental-deletion "
                       "scenario.",
            "distractors": {
                "B": "Azure Policy Deny evaluates resource properties on create or update to enforce "
                     "standards; it is not designed to delete-protect one named resource.",
                "C": "A Reader role limits what one identity can do but does not stop other "
                     "privileged users from deleting the resource.",
                "D": "A budget alert concerns spending, not deletion protection.",
            },
            "exam_pattern": "Protect a specific resource from deletion = resource lock, not Policy.",
        },
        "references": ["Azure resource locks"],
    },
    {
        "id": "az900-gov-020", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 1, "type": "mcq",
        "stem": "A company needs to discover, catalog, and classify sensitive data spread across "
                "on-premises, multicloud, and SaaS sources. Which Microsoft solution is designed "
                "for this?",
        "options": [
            {"id": "A", "text": "Microsoft Purview"},
            {"id": "B", "text": "Azure Policy"},
            {"id": "C", "text": "Service Trust Portal"},
            {"id": "D", "text": "Azure Monitor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Purview is a unified data governance solution that discovers, "
                       "catalogs, maps, and classifies data assets across on-premises, multicloud, "
                       "and SaaS estates.",
            "distractors": {
                "B": "Azure Policy enforces configuration rules on Azure resources, not data "
                     "discovery or classification.",
                "C": "The Service Trust Portal hosts Microsoft's compliance documents; it does not "
                     "govern your data.",
                "D": "Azure Monitor collects telemetry from resources; it does not catalog or "
                     "classify data.",
            },
            "exam_pattern": "'Govern or classify data across the estate' = Microsoft Purview.",
        },
        "references": ["Microsoft Purview"],
    },
    {
        "id": "az900-gov-021", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "An auditor asks for Microsoft's independent audit reports and compliance "
                "certifications, such as SOC and ISO, for Azure. Where can these be obtained?",
        "options": [
            {"id": "A", "text": "Service Trust Portal"},
            {"id": "B", "text": "The Azure Policy compliance view"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "Azure Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Service Trust Portal is Microsoft's hub for audit reports, "
                       "certifications, and compliance documentation (such as SOC and ISO) covering "
                       "its cloud services.",
            "distractors": {
                "B": "The Azure Policy compliance view shows whether your own resources meet your "
                     "policies, not Microsoft's third-party audit reports.",
                "C": "Microsoft Purview governs your data; it does not supply Microsoft's compliance "
                     "certifications.",
                "D": "Advisor gives best-practice recommendations, not audit documents.",
            },
            "exam_pattern": "'Download Microsoft's audit/compliance reports' = Service Trust Portal.",
        },
        "references": ["Service Trust Portal"],
    },
    {
        "id": "az900-gov-022", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "An external auditor must view resources in a subscription but change nothing. Which "
                "approach best grants that access to the auditor specifically?",
        "options": [
            {"id": "A", "text": "Assign the auditor the RBAC Reader role"},
            {"id": "B", "text": "Apply a ReadOnly lock to the subscription"},
            {"id": "C", "text": "Give the auditor the Owner role"},
            {"id": "D", "text": "Create an Azure Policy Deny"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Reader RBAC role grants view-only access to a specific identity, which is "
                       "exactly how to let one auditor see resources without making changes.",
            "distractors": {
                "B": "A ReadOnly lock blocks changes for everyone, including administrators; it is "
                     "not a way to grant one person scoped view access.",
                "C": "The Owner role grants full control, far more than view-only.",
                "D": "An Azure Policy Deny restricts resource configurations, not a user's read "
                     "access.",
            },
            "exam_pattern": "Per-user view-only access = RBAC Reader; locks are not per-user.",
        },
        "references": ["Azure RBAC"],
    },
    {
        "id": "az900-gov-023", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 3, "type": "mcq",
        "stem": "A governance team must apply the same tagging policy consistently across twenty "
                "Azure subscriptions at once. Where should the policy be assigned?",
        "options": [
            {"id": "A", "text": "At a management group containing the subscriptions"},
            {"id": "B", "text": "Separately in each resource group"},
            {"id": "C", "text": "On a single resource"},
            {"id": "D", "text": "In the Pricing Calculator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Management groups sit above subscriptions and let you assign a policy once so "
                       "it is inherited by all contained subscriptions, enforcing governance at scale.",
            "distractors": {
                "B": "Assigning to each resource group individually is error-prone and does not scale "
                     "to twenty subscriptions.",
                "C": "Assigning to one resource applies nowhere else; it does not cover many "
                     "subscriptions.",
                "D": "The Pricing Calculator estimates cost; it does not assign policies.",
            },
            "exam_pattern": "'Apply governance across many subscriptions' = management groups.",
        },
        "references": ["Azure management groups"],
    },
    {
        "id": "az900-gov-024", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to identify resources that lack a required tag without blocking anyone "
                "from deploying them. Which Azure Policy effect should they use?",
        "options": [
            {"id": "A", "text": "Audit"},
            {"id": "B", "text": "Deny"},
            {"id": "C", "text": "A resource lock"},
            {"id": "D", "text": "Append"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Audit effect records non-compliant resources in compliance reports while "
                       "still allowing them to be created, which fits a report-only goal.",
            "distractors": {
                "B": "The Deny effect would block deployments, which the team explicitly wants to "
                     "avoid.",
                "C": "A resource lock prevents deletion or changes; it does not report missing tags.",
                "D": "Append adds a value to a resource rather than reporting non-compliance.",
            },
            "exam_pattern": "'Report non-compliance but do not block' = Audit effect.",
        },
        "references": ["Azure Policy"],
    },
    {
        "id": "az900-gov-025", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 3, "type": "mcq",
        "stem": "After assigning several policies, a cloud team wants to see which of their own Azure "
                "resources currently violate those rules. Where do they look?",
        "options": [
            {"id": "A", "text": "The Azure Policy compliance dashboard"},
            {"id": "B", "text": "The Service Trust Portal"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "The Azure TCO Calculator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Policy includes a compliance view that reports which of your resources "
                       "are compliant or non-compliant with the policies you assigned.",
            "distractors": {
                "B": "The Service Trust Portal shows Microsoft's own compliance certifications, not "
                     "the compliance state of your resources.",
                "C": "Microsoft Purview governs data assets; it does not report Azure Policy "
                     "compliance.",
                "D": "The TCO Calculator compares costs; it has no compliance reporting.",
            },
            "exam_pattern": "Your resources' compliance = Azure Policy; Microsoft's audits = Service "
                            "Trust Portal.",
        },
        "references": ["Azure Policy"],
    },
    {
        "id": "az900-gov-026", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_governance_compliance", "difficulty": 2, "type": "multi",
        "stem": "Which TWO statements correctly describe the division of responsibility between Azure "
                "Policy and Azure RBAC? Select two.",
        "options": [
            {"id": "A", "text": "Azure Policy governs what resource configurations are allowed"},
            {"id": "B", "text": "Azure RBAC governs which identities may perform actions"},
            {"id": "C", "text": "Azure Policy decides which users can sign in"},
            {"id": "D", "text": "Azure RBAC defines which VM sizes may be deployed"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Azure Policy enforces rules about allowed resource configurations (the "
                       "'what'), while RBAC controls which users or identities can perform which "
                       "actions (the 'who'); the two work together.",
            "distractors": {
                "C": "User sign-in and identity are handled by Microsoft Entra ID, not Azure Policy.",
                "D": "Allowed VM sizes are enforced by Azure Policy, not by RBAC.",
            },
            "exam_pattern": "Policy = what is allowed; RBAC = who can act.",
        },
        "references": ["Azure Policy", "Azure RBAC"],
    },

    # ===== az_tools_monitoring =============================================
    {
        "id": "az900-gov-027", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "A new administrator prefers a visual, point-and-click web interface to create and "
                "manage Azure resources. Which management option suits them best?",
        "options": [
            {"id": "A", "text": "The Azure portal"},
            {"id": "B", "text": "Azure CLI"},
            {"id": "C", "text": "ARM templates"},
            {"id": "D", "text": "Azure PowerShell"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Azure portal is a web-based graphical console for creating, configuring, "
                       "and managing Azure resources without writing commands.",
            "distractors": {
                "B": "Azure CLI is a text command-line tool, not a point-and-click GUI.",
                "C": "ARM templates are code files for automated deployment, not an interactive "
                     "interface.",
                "D": "Azure PowerShell uses scripted cmdlets rather than a graphical interface.",
            },
            "exam_pattern": "'Visual / point-and-click management' = Azure portal.",
        },
        "references": ["Azure portal"],
    },
    {
        "id": "az900-gov-028", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An engineer needs to run a few Azure commands from a borrowed laptop with nothing "
                "installed, using a browser-based shell that is already authenticated. What fits?",
        "options": [
            {"id": "A", "text": "Azure Cloud Shell"},
            {"id": "B", "text": "A locally installed Azure CLI"},
            {"id": "C", "text": "An ARM template"},
            {"id": "D", "text": "Azure Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Cloud Shell is a browser-based, pre-authenticated shell (Bash or "
                       "PowerShell) available in the portal, so no local installation is required.",
            "distractors": {
                "B": "Installing Azure CLI locally requires setup on the machine, which the "
                     "borrowed-laptop scenario rules out.",
                "C": "An ARM template is a deployment file, not an interactive shell.",
                "D": "Advisor provides recommendations; it is not a command shell.",
            },
            "exam_pattern": "'Browser shell, nothing to install, already signed in' = Cloud Shell.",
        },
        "references": ["Azure Cloud Shell"],
    },
    {
        "id": "az900-gov-029", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A cross-platform team wants to script Azure management using concise commands that "
                "all begin with 'az'. Which tool are they describing?",
        "options": [
            {"id": "A", "text": "Azure CLI"},
            {"id": "B", "text": "Azure PowerShell"},
            {"id": "C", "text": "Bicep"},
            {"id": "D", "text": "The Azure portal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure CLI is a cross-platform command-line tool whose commands start with "
                       "'az', used for scripting and automating Azure management.",
            "distractors": {
                "B": "Azure PowerShell uses verb-noun cmdlets such as Get-AzVM, not 'az' commands.",
                "C": "Bicep is a declarative infrastructure-as-code language, not an interactive "
                     "command tool.",
                "D": "The Azure portal is a graphical interface, not an 'az' command tool.",
            },
            "exam_pattern": "Commands beginning with 'az' = Azure CLI.",
        },
        "references": ["Azure CLI"],
    },
    {
        "id": "az900-gov-030", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A Windows-focused administrator wants to automate Azure tasks using verb-noun "
                "cmdlets like Get-AzVM from the Az module. Which tool is this?",
        "options": [
            {"id": "A", "text": "Azure PowerShell"},
            {"id": "B", "text": "Azure CLI"},
            {"id": "C", "text": "ARM templates"},
            {"id": "D", "text": "Azure Monitor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure PowerShell provides the Az module of cmdlets (such as Get-AzVM) for "
                       "scripting and automating Azure management, popular with PowerShell users.",
            "distractors": {
                "B": "Azure CLI uses 'az' commands, not PowerShell cmdlets.",
                "C": "ARM templates are declarative JSON files, not interactive cmdlets.",
                "D": "Azure Monitor is a monitoring service, not a scripting tool.",
            },
            "exam_pattern": "Az module verb-noun cmdlets = Azure PowerShell.",
        },
        "references": ["Azure PowerShell"],
    },
    {
        "id": "az900-gov-031", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A team must deploy the same multi-resource environment identically in several "
                "subscriptions, repeatedly and without manual steps. Which approach fits best?",
        "options": [
            {"id": "A", "text": "Deploy with an ARM template"},
            {"id": "B", "text": "Build each environment by hand in the portal"},
            {"id": "C", "text": "File a Service Health request"},
            {"id": "D", "text": "Run Azure Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ARM templates are declarative JSON files that define infrastructure as code, "
                       "enabling repeatable, consistent, automated deployments across subscriptions.",
            "distractors": {
                "B": "Building by hand in the portal is manual and error-prone, producing "
                     "inconsistent environments.",
                "C": "Service Health reports Azure service status; it does not deploy resources.",
                "D": "Advisor provides recommendations; it does not deploy environments.",
            },
            "exam_pattern": "'Repeatable, identical, automated deployment' = IaC templates.",
        },
        "references": ["Azure Resource Manager templates"],
    },
    {
        "id": "az900-gov-032", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Engineers find their ARM JSON templates verbose and want a cleaner, purpose-built "
                "language that still compiles down to ARM. What should they adopt?",
        "options": [
            {"id": "A", "text": "Bicep"},
            {"id": "B", "text": "More ARM JSON"},
            {"id": "C", "text": "The Azure portal"},
            {"id": "D", "text": "Imperative Azure CLI scripts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bicep is a domain-specific language with simpler, more readable syntax that "
                       "transpiles to ARM templates, giving the same declarative deployments with "
                       "less verbosity.",
            "distractors": {
                "B": "Writing more ARM JSON keeps the very verbosity the team is trying to escape.",
                "C": "The portal is manual and graphical, not a cleaner IaC authoring language.",
                "D": "Imperative CLI scripts are a different style and do not provide the declarative "
                     "template model the team wants.",
            },
            "exam_pattern": "'Cleaner, readable IaC that compiles to ARM' = Bicep.",
        },
        "references": ["Bicep"],
    },
    {
        "id": "az900-gov-033", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "A team wants personalized recommendations to improve the security, reliability, "
                "performance, and cost of their existing Azure resources. Which service provides "
                "these?",
        "options": [
            {"id": "A", "text": "Azure Advisor"},
            {"id": "B", "text": "Azure Monitor"},
            {"id": "C", "text": "Azure Service Health"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Advisor analyzes your resources and gives personalized best-practice "
                       "recommendations across cost, security, reliability, operational excellence, "
                       "and performance.",
            "distractors": {
                "B": "Azure Monitor collects and analyzes telemetry; it does not itself produce the "
                     "curated best-practice recommendations Advisor does.",
                "C": "Service Health reports Azure service outages and maintenance, not optimization "
                     "recommendations.",
                "D": "Azure Policy enforces configuration rules; it does not recommend improvements.",
            },
            "exam_pattern": "'Personalized best-practice recommendations' = Azure Advisor.",
        },
        "references": ["Azure Advisor"],
    },
    {
        "id": "az900-gov-034", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An operations team wants to collect CPU and memory metrics from their VMs and raise "
                "an alert when a VM is overloaded. Which service do they use?",
        "options": [
            {"id": "A", "text": "Azure Monitor"},
            {"id": "B", "text": "Azure Advisor"},
            {"id": "C", "text": "Service Trust Portal"},
            {"id": "D", "text": "Microsoft Purview"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Monitor collects metrics and logs (telemetry) from resources and can "
                       "trigger alerts, such as when a VM's CPU exceeds a threshold.",
            "distractors": {
                "B": "Advisor gives recommendations; it is not the telemetry-collection and alerting "
                     "engine.",
                "C": "The Service Trust Portal hosts compliance documents, not resource metrics.",
                "D": "Microsoft Purview governs data; it does not monitor VM performance.",
            },
            "exam_pattern": "'Collect metrics/logs and alert on resources' = Azure Monitor.",
        },
        "references": ["Azure Monitor"],
    },
    {
        "id": "az900-gov-035", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An engineer wants to run queries across collected log data from many resources "
                "using a query language in a central workspace. Which Azure Monitor feature is this?",
        "options": [
            {"id": "A", "text": "Log Analytics"},
            {"id": "B", "text": "Application Insights"},
            {"id": "C", "text": "Azure Advisor"},
            {"id": "D", "text": "Azure Service Health"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Log Analytics is the Azure Monitor tool for running queries (using KQL) "
                       "against log data stored in a Log Analytics workspace.",
            "distractors": {
                "B": "Application Insights focuses on monitoring applications, not general "
                     "cross-resource log querying.",
                "C": "Advisor provides recommendations, not a log query experience.",
                "D": "Service Health reports Azure service status, not your log queries.",
            },
            "exam_pattern": "'Query collected logs in a workspace' = Log Analytics.",
        },
        "references": ["Azure Monitor Log Analytics"],
    },
    {
        "id": "az900-gov-036", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to monitor a live web application's response times, request "
                "failures, and availability from the user's perspective. Which tool fits?",
        "options": [
            {"id": "A", "text": "Application Insights"},
            {"id": "B", "text": "Log Analytics"},
            {"id": "C", "text": "Azure Service Health"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Application Insights is the Azure Monitor application performance management "
                       "feature that tracks a live app's requests, failures, dependencies, and "
                       "availability.",
            "distractors": {
                "B": "Log Analytics queries collected logs generally; Application Insights is the "
                     "purpose-built app performance tool for this scenario.",
                "C": "Service Health reports Azure platform status, not your application's "
                     "performance.",
                "D": "Azure Policy enforces resource rules; it does not monitor applications.",
            },
            "exam_pattern": "'Monitor a live app's performance/availability' = Application Insights.",
        },
        "references": ["Azure Monitor Application Insights"],
    },
    {
        "id": "az900-gov-037", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "An operations team needs to know whether an ongoing Azure platform outage or planned "
                "maintenance is affecting the services they use. Which tool shows this?",
        "options": [
            {"id": "A", "text": "Azure Service Health"},
            {"id": "B", "text": "Azure Advisor"},
            {"id": "C", "text": "Application Insights"},
            {"id": "D", "text": "Microsoft Cost Management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Service Health gives a personalized view of Azure service issues, "
                       "planned maintenance, and health advisories affecting the resources and "
                       "regions you use.",
            "distractors": {
                "B": "Advisor provides optimization recommendations, not platform outage status.",
                "C": "Application Insights monitors your application, not Azure platform health.",
                "D": "Cost Management tracks spending, not service outages.",
            },
            "exam_pattern": "'Is an Azure outage/maintenance affecting me?' = Service Health.",
        },
        "references": ["Azure Service Health"],
    },
    {
        "id": "az900-gov-038", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Azure flags that a consistently underused VM should be resized to save money. Which "
                "service surfaces this specific cost-optimization recommendation?",
        "options": [
            {"id": "A", "text": "Azure Advisor"},
            {"id": "B", "text": "Azure Monitor"},
            {"id": "C", "text": "Azure Service Health"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Advisor's cost recommendations identify underutilized resources and "
                       "advise actions such as resizing or shutting down a VM to save money.",
            "distractors": {
                "B": "Azure Monitor can show the underlying utilization metrics, but the actionable "
                     "right-size recommendation is produced by Advisor.",
                "C": "Service Health reports Azure outages and maintenance, not cost recommendations.",
                "D": "A resource lock prevents deletion or changes; it does not recommend resizing.",
            },
            "exam_pattern": "Actionable right-size/cost recommendation = Advisor (Monitor shows raw "
                            "metrics).",
        },
        "references": ["Azure Advisor"],
    },
    {
        "id": "az900-gov-039", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants to be notified only when Microsoft reports an Azure service "
                "outage, not when a VM's own CPU spikes. Which alert should they set up?",
        "options": [
            {"id": "A", "text": "A Service Health alert"},
            {"id": "B", "text": "An Azure Monitor metric alert"},
            {"id": "C", "text": "An Application Insights web test"},
            {"id": "D", "text": "A Cost Management budget alert"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Service Health alerts notify you about Azure platform issues such as outages, "
                       "maintenance, and advisories affecting your services.",
            "distractors": {
                "B": "An Azure Monitor metric alert fires on resource metrics like CPU, which is "
                     "exactly what the administrator wants to exclude.",
                "C": "An Application Insights web test checks application availability, not Azure "
                     "platform outages.",
                "D": "A budget alert concerns spending, not service outages.",
            },
            "exam_pattern": "Notification about Azure platform outages = Service Health alert.",
        },
        "references": ["Azure Service Health"],
    },
    {
        "id": "az900-gov-040", "exam": "az900", "domain": "az_management_governance",
        "subtopic": "az_tools_monitoring", "difficulty": 2, "type": "multi",
        "stem": "Which TWO options let you define Azure infrastructure as code for automated, "
                "repeatable deployments? Select two.",
        "options": [
            {"id": "A", "text": "ARM templates"},
            {"id": "B", "text": "Bicep"},
            {"id": "C", "text": "Azure Advisor"},
            {"id": "D", "text": "Azure Service Health"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "ARM templates (declarative JSON) and Bicep (a cleaner language that compiles "
                       "to ARM) are both infrastructure-as-code options for repeatable, automated "
                       "Azure deployments.",
            "distractors": {
                "C": "Azure Advisor provides best-practice recommendations; it does not define or "
                     "deploy infrastructure.",
                "D": "Azure Service Health reports Azure service status; it is not an "
                     "infrastructure-as-code tool.",
            },
            "exam_pattern": "Azure IaC = ARM templates and Bicep.",
        },
        "references": ["Azure Resource Manager templates", "Bicep"],
    },
]
