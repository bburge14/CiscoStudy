"""Microsoft 365 Fundamentals pool - ROUND 2 (deepening additions).

Round 1 (content_ms900_concepts/apps/security/pricing.py) established 72 items
covering the baseline of every MS-900 subtopic. This round-2 pool adds ~128 more
ORIGINAL, NON-DUPLICATE items that push into services, plans, and angles round 1
did not test, skewing slightly harder toward difficulty-2 "which service/plan/
capability fits this need" scenarios.

Domains and subtopics use the EXACT blueprint keys (studyengine/blueprints.py):
  * ms9_cloud_concepts     -> ms9_cloud_benefits, ms9_m365_vs_office, ms9_cloud_adoption
  * ms9_apps_services      -> ms9_productivity_apps, ms9_teams_collaboration,
                              ms9_endpoint_intune, ms9_analytics_copilot,
                              ms9_deployment_options
  * ms9_security_compliance-> ms9_identity_entra, ms9_threat_protection,
                              ms9_compliance_purview, ms9_zero_trust_privacy
  * ms9_pricing_support    -> ms9_licensing, ms9_billing_cost, ms9_support_sla,
                              ms9_lifecycle

New ids carry an "-r2-" segment (ms900-con-r2-001, ms900-apps-r2-001,
ms900-sec-r2-001, ms900-price-r2-001 ...) guaranteeing uniqueness versus round 1.
Schema is identical to the round-1 files: build_content.py shuffles option order
by id (so the authored key is not positionally biased), every wrong option carries
a distractor note, mcq has one correct answer, multi has two or more, and fill
items omit options and accept lowercase strings. Current Microsoft product names
are used throughout (Microsoft Entra ID, Microsoft Defender XDR / Defender for
Office 365, Microsoft Purview, Microsoft Intune, Microsoft Teams, Microsoft 365
Copilot, Microsoft Viva, Microsoft Priva, Windows 365 / Azure Virtual Desktop).
Fundamentals depth only - no exact prices or numeric caps.
"""

QUESTIONS = [

    # ===============================================================
    # DOMAIN 1: ms9_cloud_concepts
    # ===============================================================

    # ----- ms9_cloud_benefits -----
    {
        "id": "ms900-con-r2-001", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A development team wants to rent virtual machines, storage, and networking from a cloud provider and install and maintain their own operating systems and custom server software on them. Which cloud service model gives them this level of control over the compute resources?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "SaaS (Software as a Service)"},
            {"id": "C", "text": "PaaS (Platform as a Service)"},
            {"id": "D", "text": "On-premises only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Infrastructure as a Service (IaaS) rents the raw building blocks - virtual machines, storage, and networking - while the customer installs and manages the operating system and everything above it. It offers the most customer control of the cloud models.",
            "distractors": {
                "B": "SaaS delivers a finished, provider-managed application (like Microsoft 365); the customer does not manage VMs or operating systems.",
                "C": "PaaS provides a managed platform for building apps, so the customer does not manage the underlying OS - less control than IaaS.",
                "D": "On-premises means the organization owns and runs the hardware itself; nothing is rented from a provider.",
            },
            "exam_pattern": "Rent VMs/storage/network and manage the OS yourself = IaaS (most customer control).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Cloud service models (IaaS)"],
    },
    {
        "id": "ms900-con-r2-002", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Developers want a managed environment where they can build, test, and deploy their own applications without having to patch the operating system or manage the underlying servers. Which cloud service model best fits this?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "A perpetual on-premises license"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Platform as a Service (PaaS) provides a ready, managed platform - operating system, runtime, and services - so developers focus on their application code while the provider handles the servers and OS patching.",
            "distractors": {
                "A": "With IaaS the developer still manages the operating system and patching, which this scenario wants to avoid.",
                "C": "SaaS delivers a finished application to use, not a platform on which to build custom apps.",
                "D": "A perpetual on-premises license runs on hardware the organization must own and maintain itself.",
            },
            "exam_pattern": "Managed platform to build/deploy your own apps, no OS to manage = PaaS.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Cloud service models (PaaS)"],
    },
    {
        "id": "ms900-con-r2-003", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft runs Microsoft 365 across multiple redundant datacenters so that if one component or facility fails, the service keeps running with little or no interruption for customers. Which cloud benefit does this describe?",
        "options": [
            {"id": "A", "text": "Capital expenditure"},
            {"id": "B", "text": "Perpetual licensing"},
            {"id": "C", "text": "High availability and reliability"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "High availability and reliability come from redundancy across datacenters, so the service stays up and data stays accessible even when individual components fail - a core cloud benefit.",
            "distractors": {
                "A": "Capital expenditure is a spending model (large up-front purchases), not a resilience benefit.",
                "B": "Perpetual licensing is a purchasing model, unrelated to uptime and redundancy.",
                "D": "Single sign-on is an identity convenience, not a measure of service resilience.",
            },
            "exam_pattern": "Redundancy that keeps a service running through failures = high availability/reliability.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Benefits of cloud services (reliability/high availability)"],
    },
    {
        "id": "ms900-con-r2-004", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "Because Microsoft buys hardware and power at enormous scale and spreads those costs across millions of customers, it can deliver cloud services more cheaply than a single company running its own small datacenter could. Which cloud benefit is this?",
        "options": [
            {"id": "A", "text": "Zero Trust"},
            {"id": "B", "text": "Co-authoring"},
            {"id": "C", "text": "Data loss prevention"},
            {"id": "D", "text": "Economies of scale"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Economies of scale mean a large provider's massive purchasing and operational scale lowers the per-unit cost, which is passed on as lower prices than a small organization could achieve alone.",
            "distractors": {
                "A": "Zero Trust is a security model, not a cost benefit.",
                "B": "Co-authoring is real-time document collaboration, unrelated to cost.",
                "C": "Data loss prevention protects sensitive data; it is not an economic benefit.",
            },
            "exam_pattern": "Provider's huge scale lowers per-user cost = economies of scale.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Benefits of cloud services (economies of scale)"],
    },
    {
        "id": "ms900-con-r2-005", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "multi",
        "stem": "A CIO is listing genuine benefits of using a cloud service such as Microsoft 365 in a strategy deck. Which TWO of the following are real cloud benefits? (Choose two.)",
        "options": [
            {"id": "A", "text": "Elasticity - resources automatically adjust to match changing demand"},
            {"id": "B", "text": "Global reach - services can be delivered from datacenters close to users worldwide"},
            {"id": "C", "text": "A guarantee that the organization never has any security responsibilities"},
            {"id": "D", "text": "A promise that the service works with no internet connection"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Elasticity (resources scale up and down to meet demand) and global reach (provider datacenters worldwide serve users with lower latency) are genuine cloud benefits.",
            "distractors": {
                "C": "In the cloud, security is shared; the customer still has responsibilities for data, identities, and access.",
                "D": "Cloud services are delivered over the internet, so a connection is required.",
            },
            "exam_pattern": "Elasticity and global reach are real cloud benefits; 'no security duties' and 'no internet needed' are not.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Benefits of cloud services (elasticity, global reach)"],
    },

    # ----- ms9_m365_vs_office -----
    {
        "id": "ms900-con-r2-006", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "A manufacturing firm runs equipment controllers that must keep a fixed, unchanging version of the Office apps for years, cannot receive frequent feature updates, and have no cloud connectivity. They want a one-time perpetual purchase. Which Office offering fits this requirement?",
        "options": [
            {"id": "A", "text": "Office LTSC (Long-Term Servicing Channel)"},
            {"id": "B", "text": "A Microsoft 365 subscription"},
            {"id": "C", "text": "Office for the web"},
            {"id": "D", "text": "Microsoft 365 Apps for business"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Office LTSC is a perpetual (one-time purchase) edition on the Long-Term Servicing Channel, designed for devices that must stay on a fixed feature set for a long time and cannot take the continuous updates of the subscription apps.",
            "distractors": {
                "B": "A Microsoft 365 subscription delivers continuous feature updates and is subscription-based, the opposite of a fixed perpetual release.",
                "C": "Office for the web runs in a browser and needs internet connectivity, which these offline controllers lack.",
                "D": "Microsoft 365 Apps for business is the subscription desktop suite that updates automatically, not a fixed perpetual release.",
            },
            "exam_pattern": "Fixed-version, perpetual, infrequently updated Office for special devices = Office LTSC.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Office LTSC vs Microsoft 365 Apps"],
    },
    {
        "id": "ms900-con-r2-007", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "An executive asks why the company's subscription is branded 'Microsoft 365' rather than 'Office'. Which statement best explains what the Microsoft 365 name is meant to convey?",
        "options": [
            {"id": "A", "text": "It is only the Word, Excel, and PowerPoint desktop apps, renamed"},
            {"id": "B", "text": "It is a complete cloud-powered suite - Office apps plus cloud services, security, and device capabilities - not just the Office apps"},
            {"id": "C", "text": "It is a perpetual, one-time software purchase"},
            {"id": "D", "text": "It is a Windows operating-system edition"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The 'Microsoft 365' brand signals a complete, cloud-connected suite - the Office apps together with cloud services (email, storage, Teams), plus security and device management in higher tiers - going well beyond the standalone Office applications.",
            "distractors": {
                "A": "Microsoft 365 is more than the renamed desktop apps; it bundles cloud services and more.",
                "C": "Microsoft 365 is a subscription, not a one-time perpetual purchase.",
                "D": "Microsoft 365 is a productivity and services suite, not a Windows OS edition (though higher tiers can include Windows licensing).",
            },
            "exam_pattern": "'Microsoft 365' = the broader cloud suite (apps + services + security), not just the Office apps.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): What is Microsoft 365"],
    },
    {
        "id": "ms900-con-r2-008", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 1, "type": "mcq",
        "stem": "Which statement is TRUE of a standalone, perpetual purchase of Office compared with a Microsoft 365 subscription?",
        "options": [
            {"id": "A", "text": "It automatically includes Microsoft Teams and cloud mailboxes"},
            {"id": "B", "text": "It is billed per user every month"},
            {"id": "C", "text": "It is a one-time purchase that does not include cloud services such as Exchange Online or OneDrive"},
            {"id": "D", "text": "It continuously adds brand-new features over its lifetime"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A perpetual Office purchase is bought once and provides only the installed apps; it does not include the cloud services (Exchange Online, OneDrive, Teams) that come with a Microsoft 365 subscription.",
            "distractors": {
                "A": "Those cloud services come with a Microsoft 365 subscription, not with standalone perpetual Office.",
                "B": "A perpetual license is a single up-front purchase, not a monthly per-user charge.",
                "D": "A perpetual edition stays on its shipped feature set; only the subscription continuously gains new features.",
            },
            "exam_pattern": "Perpetual Office = one-time purchase, apps only, no cloud services and no new features.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 versus standalone Office"],
    },
    {
        "id": "ms900-con-r2-009", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "fill",
        "stem": "What is the name of the perpetual (one-time purchase), long-term servicing edition of Office intended for specialized or offline devices that must keep a fixed feature set? Enter the product name (includes a four-letter acronym).",
        "correct": ["office ltsc", "ltsc", "office long-term servicing channel"],
        "explanation": {
            "correct": "Office LTSC (Long-Term Servicing Channel) is the perpetual, fixed-feature edition for devices that cannot take the continuous updates of the Microsoft 365 subscription apps.",
            "distractors": {},
            "exam_pattern": "Perpetual, fixed-version Office for special-purpose devices = Office LTSC.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Office LTSC"],
    },

    # ----- ms9_cloud_adoption -----
    {
        "id": "ms900-con-r2-010", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "mcq",
        "stem": "A government agency evaluating Microsoft 365 must ensure that certain data is stored and processed within its own country to satisfy local regulations. Which cloud adoption consideration does this represent?",
        "options": [
            {"id": "A", "text": "Co-authoring"},
            {"id": "B", "text": "Perpetual licensing"},
            {"id": "C", "text": "Click-to-Run installation"},
            {"id": "D", "text": "Data residency and sovereignty"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Data residency/sovereignty - where data is physically stored and which country's laws apply to it - is a key consideration when adopting cloud services, especially for regulated or public-sector organizations.",
            "distractors": {
                "A": "Co-authoring is a collaboration feature, not a regulatory consideration about where data lives.",
                "B": "Perpetual licensing is a purchasing model, unrelated to data location rules.",
                "C": "Click-to-Run is an app installation technology, not a data-location consideration.",
            },
            "exam_pattern": "Where data is stored / which laws apply = data residency and sovereignty (an adoption consideration).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Cloud adoption considerations (data residency)"],
    },
    {
        "id": "ms900-con-r2-011", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "mcq",
        "stem": "When planning its Microsoft 365 rollout, an organization realizes the biggest risk is not the technology but whether employees will actually learn and embrace the new tools. Which adoption consideration does this highlight?",
        "options": [
            {"id": "A", "text": "User adoption, training, and change management"},
            {"id": "B", "text": "The physical security of Microsoft's datacenters"},
            {"id": "C", "text": "The CapEx cost of new servers"},
            {"id": "D", "text": "The choice of update channel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Successful cloud adoption depends on people, not just technology: user training, communication, and change management help employees embrace the new tools and realize the value.",
            "distractors": {
                "B": "Datacenter physical security is Microsoft's responsibility and is not the human-adoption risk described.",
                "C": "Moving to the cloud reduces server CapEx; the scenario is about people adopting the tools.",
                "D": "Update channels control feature-update cadence, not whether employees embrace the tools.",
            },
            "exam_pattern": "Getting people to actually use the new tools = user adoption/training/change management.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Cloud adoption considerations (change management)"],
    },
    {
        "id": "ms900-con-r2-012", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "multi",
        "stem": "An organization is documenting why it is moving from on-premises systems to Microsoft 365. Which TWO are valid business drivers for adopting the cloud? (Choose two.)",
        "options": [
            {"id": "A", "text": "Enabling secure hybrid and remote work from any location"},
            {"id": "B", "text": "Deploying new services in minutes instead of waiting weeks to procure hardware"},
            {"id": "C", "text": "Removing the organization's obligation to meet any regulations"},
            {"id": "D", "text": "Making the internet connection optional for cloud access"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Enabling secure hybrid/remote work and gaining agility (standing up services quickly without buying hardware) are classic, valid reasons organizations adopt the cloud.",
            "distractors": {
                "C": "Adopting the cloud does not remove compliance obligations; the organization still must meet regulations.",
                "D": "Cloud services are reached over the internet, so a connection remains required.",
            },
            "exam_pattern": "Cloud drivers: enable hybrid/remote work and faster deployment (agility) - not escaping compliance or the internet.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Reasons to adopt cloud services"],
    },
    {
        "id": "ms900-con-r2-013", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "mcq",
        "stem": "After moving to Microsoft 365, an IT leader reminds the team that although Microsoft runs the infrastructure, the organization is still accountable for protecting its own data, user identities, and who is granted access. Which principle is the leader describing?",
        "options": [
            {"id": "A", "text": "The organization has no remaining responsibilities in the cloud"},
            {"id": "B", "text": "Shared responsibility - some duties stay with the customer even in SaaS"},
            {"id": "C", "text": "Perpetual licensing"},
            {"id": "D", "text": "Economies of scale"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Under the shared responsibility model, the provider secures the underlying service, but the customer always remains responsible for its own data, identities/accounts, and access management - even with SaaS like Microsoft 365.",
            "distractors": {
                "A": "Responsibilities are shared, not eliminated; the customer still protects data and identities.",
                "C": "Perpetual licensing is a purchasing model, not a security-responsibility principle.",
                "D": "Economies of scale is a cost benefit, not a division of security duties.",
            },
            "exam_pattern": "Provider secures the service; customer still owns data, identities, and access = shared responsibility.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Shared responsibility in the cloud"],
    },

    # ===============================================================
    # DOMAIN 2: ms9_apps_services
    # ===============================================================

    # ----- ms9_productivity_apps -----
    {
        "id": "ms900-apps-r2-001", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A project team wants a visual board of tasks organized into buckets and columns (like 'To do', 'In progress', 'Done'), assignable to members and usable inside a Microsoft Teams channel. Which Microsoft 365 app is designed for this team task management?",
        "options": [
            {"id": "A", "text": "Microsoft Forms"},
            {"id": "B", "text": "Exchange Online"},
            {"id": "C", "text": "Microsoft Planner"},
            {"id": "D", "text": "Microsoft Whiteboard"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Planner provides shared, board-based (Kanban) task management - buckets, assignments, and progress tracking - and integrates directly into Teams channels.",
            "distractors": {
                "A": "Microsoft Forms creates surveys and quizzes, not task boards.",
                "B": "Exchange Online provides mailboxes, not visual task boards.",
                "D": "Microsoft Whiteboard is a freeform drawing canvas, not a structured task-tracking board.",
            },
            "exam_pattern": "Shared, board-based team task tracking (buckets/assignments) = Microsoft Planner.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Planner"],
    },
    {
        "id": "ms900-apps-r2-002", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "An individual employee wants a simple personal app to jot down their own daily to-dos and flagged Outlook emails, with reminders, separate from any shared team board. Which Microsoft 365 app fits best?",
        "options": [
            {"id": "A", "text": "Microsoft Planner"},
            {"id": "B", "text": "SharePoint Online"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "Microsoft To Do"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft To Do is the personal task-management app for an individual's own lists and reminders, and it surfaces flagged emails from Outlook - distinct from team-shared Planner boards.",
            "distractors": {
                "A": "Microsoft Planner is for shared team task boards, not a personal to-do list.",
                "B": "SharePoint Online hosts team sites and libraries, not a personal task app.",
                "C": "Microsoft Bookings schedules customer appointments, not personal tasks.",
            },
            "exam_pattern": "Personal task list and reminders = Microsoft To Do; shared team task board = Microsoft Planner.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft To Do"],
    },
    {
        "id": "ms900-apps-r2-003", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A facilities team wants to track assets, issues, and inventory in flexible, smart tables with custom columns, views, and rules - more structured than a document but without building a database. Which Microsoft 365 app is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Microsoft Lists"},
            {"id": "B", "text": "OneDrive"},
            {"id": "C", "text": "Microsoft Teams"},
            {"id": "D", "text": "Microsoft Sway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Lists lets teams track information in smart, customizable lists - with columns, views, forms, and rules - to manage things like assets, issues, and inventory without a full database.",
            "distractors": {
                "B": "OneDrive stores personal files; it is not a structured information-tracking app.",
                "C": "Teams is the collaboration hub; Lists can live inside it, but Teams itself is not the tracking tool.",
                "D": "Microsoft Sway creates interactive presentations and newsletters, not tracked data lists.",
            },
            "exam_pattern": "Track info in smart, customizable tables/lists = Microsoft Lists.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Lists"],
    },
    {
        "id": "ms900-apps-r2-004", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "Employees want a digital notebook to capture free-form typed and handwritten notes, images, and clippings, organized into notebooks, sections, and pages, and synced across devices. Which Microsoft 365 app provides this?",
        "options": [
            {"id": "A", "text": "Microsoft Forms"},
            {"id": "B", "text": "OneNote"},
            {"id": "C", "text": "Power BI"},
            {"id": "D", "text": "Exchange Online"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "OneNote is the digital note-taking app, organizing free-form notes (typed, handwritten, images, clippings) into notebooks, sections, and pages that sync across devices.",
            "distractors": {
                "A": "Microsoft Forms is for surveys and quizzes, not note-taking.",
                "C": "Power BI builds analytics dashboards, not notebooks.",
                "D": "Exchange Online handles email and calendars, not notes.",
            },
            "exam_pattern": "Free-form digital notebooks (notebooks/sections/pages) = OneNote.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): OneNote"],
    },
    {
        "id": "ms900-apps-r2-005", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A sales director wants interactive dashboards and reports that connect to multiple data sources and let managers drill into charts to analyze trends. Which Microsoft business-analytics service provides this?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft To Do"},
            {"id": "C", "text": "Microsoft Power BI"},
            {"id": "D", "text": "OneDrive"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Power BI is the business-intelligence service for building interactive reports and dashboards from many data sources, enabling self-service analysis and visual drill-down.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not analytics.",
                "B": "Microsoft To Do manages personal tasks, not data visualization.",
                "D": "OneDrive stores files; it does not build interactive dashboards.",
            },
            "exam_pattern": "Interactive dashboards and business analytics = Microsoft Power BI (Power Platform).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Power BI"],
    },
    {
        "id": "ms900-apps-r2-006", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to automate a repetitive process: when a file is added to a SharePoint library, automatically send an approval request and then post a message in Teams. Which Power Platform service creates these automated workflows?",
        "options": [
            {"id": "A", "text": "Power BI"},
            {"id": "B", "text": "Microsoft Forms"},
            {"id": "C", "text": "Microsoft Viva"},
            {"id": "D", "text": "Power Automate"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Power Automate (formerly Microsoft Flow) builds automated workflows that connect apps and services - triggering actions like approvals and notifications when events occur.",
            "distractors": {
                "A": "Power BI visualizes data; it does not run automated action workflows.",
                "B": "Microsoft Forms collects responses but does not orchestrate multi-step automated workflows.",
                "C": "Microsoft Viva is the employee experience platform, not a workflow-automation service.",
            },
            "exam_pattern": "Automate repetitive, event-driven workflows across apps = Power Automate.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Power Automate"],
    },
    {
        "id": "ms900-apps-r2-007", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A department wants to build a simple custom business app - an inspection form with a data back end - without hiring professional developers or writing much code. Which Power Platform service is designed for this low-code app building?",
        "options": [
            {"id": "A", "text": "Power Apps"},
            {"id": "B", "text": "Power BI"},
            {"id": "C", "text": "SharePoint Online"},
            {"id": "D", "text": "Microsoft Stream"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Power Apps is the low-code platform for quickly building custom business applications (forms and apps with data back ends) with little or no traditional coding.",
            "distractors": {
                "B": "Power BI is for analytics and dashboards, not building interactive data-entry apps.",
                "C": "SharePoint hosts sites and lists; it is not the low-code app-building platform itself.",
                "D": "Microsoft Stream is a video service, unrelated to building apps.",
            },
            "exam_pattern": "Low-code custom business apps = Power Apps (Power Platform).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Power Apps"],
    },
    {
        "id": "ms900-apps-r2-008", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "Colleagues want flexible, co-created workspaces with portable content blocks - a table or task list - that stay in sync wherever they are pasted, whether in Teams chat, an email, or a document. Which Microsoft 365 app provides these components and workspaces?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft Loop"},
            {"id": "C", "text": "OneDrive"},
            {"id": "D", "text": "Microsoft Intune"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Loop provides flexible workspaces and 'Loop components' - portable, live content blocks that stay synchronized everywhere they are shared across Microsoft 365 apps.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not shared live components.",
                "C": "OneDrive stores files; it does not provide synchronized portable content blocks.",
                "D": "Microsoft Intune manages devices, unrelated to collaborative content components.",
            },
            "exam_pattern": "Portable, always-in-sync content components and co-creation workspaces = Microsoft Loop.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Loop"],
    },
    {
        "id": "ms900-apps-r2-009", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "During remote brainstorming sessions, a team wants a shared freeform digital canvas where everyone can sketch ideas, add sticky notes, and draw together in real time, including inside a Teams meeting. Which Microsoft 365 app is this?",
        "options": [
            {"id": "A", "text": "Microsoft Lists"},
            {"id": "B", "text": "Exchange Online"},
            {"id": "C", "text": "Microsoft Whiteboard"},
            {"id": "D", "text": "Power Automate"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Whiteboard is the shared, freeform digital canvas for real-time visual collaboration - drawing, sticky notes, and sketching - and it integrates into Teams meetings.",
            "distractors": {
                "A": "Microsoft Lists tracks structured information, not freeform drawing.",
                "B": "Exchange Online is email and calendaring, not a drawing canvas.",
                "D": "Power Automate builds workflows, unrelated to visual brainstorming.",
            },
            "exam_pattern": "Shared freeform brainstorming canvas = Microsoft Whiteboard.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Whiteboard"],
    },
    {
        "id": "ms900-apps-r2-010", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A communications team wants to upload, store, and share internal training and town-hall videos for employees to stream on demand, with the videos held in the organization's Microsoft 365 storage. Which service is designed for this video experience?",
        "options": [
            {"id": "A", "text": "Microsoft Forms"},
            {"id": "B", "text": "Microsoft Planner"},
            {"id": "C", "text": "Microsoft Entra ID"},
            {"id": "D", "text": "Microsoft Stream"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Stream is the enterprise video service for uploading, managing, and streaming videos on demand; videos are stored in the organization's SharePoint/OneDrive within Microsoft 365.",
            "distractors": {
                "A": "Microsoft Forms collects survey responses, not videos.",
                "B": "Microsoft Planner tracks tasks, not video content.",
                "C": "Microsoft Entra ID handles identity, unrelated to video hosting.",
            },
            "exam_pattern": "Upload/share/stream internal videos = Microsoft Stream.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Stream"],
    },
    {
        "id": "ms900-apps-r2-011", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A user keeps personal draft files in their own cloud storage, but the finished project files should live in a location the whole project team owns and co-manages. Which pairing correctly matches each need?",
        "options": [
            {"id": "A", "text": "Personal drafts in OneDrive; shared team files in a SharePoint team site"},
            {"id": "B", "text": "Personal drafts in a SharePoint team site; shared files in OneDrive"},
            {"id": "C", "text": "Both in Microsoft Forms"},
            {"id": "D", "text": "Both in Exchange Online mailboxes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OneDrive is for an individual's personal work files, while a SharePoint team site is owned by the group for shared, co-managed content - so personal drafts go in OneDrive and team deliverables in SharePoint.",
            "distractors": {
                "B": "This reverses the roles: SharePoint is the shared team location and OneDrive is personal, not the other way around.",
                "C": "Microsoft Forms collects survey/quiz responses; it is not file storage.",
                "D": "Exchange Online stores mail, not project files and libraries.",
            },
            "exam_pattern": "Personal files = OneDrive; shared, team-owned files = SharePoint team site.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): OneDrive vs SharePoint"],
    },
    {
        "id": "ms900-apps-r2-012", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 3, "type": "mcq",
        "stem": "Corporate communications wants a polished SharePoint site to broadcast company news and policies to a broad, mostly read-only audience across the organization. Which type of SharePoint site is intended for this one-to-many publishing?",
        "options": [
            {"id": "A", "text": "A team site"},
            {"id": "B", "text": "A communication site"},
            {"id": "C", "text": "A OneDrive personal site"},
            {"id": "D", "text": "A Microsoft Bookings page"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A SharePoint communication site is built for broadcasting information (news, reports, policies) to a wide audience that mostly consumes content, versus a team site where a group actively collaborates.",
            "distractors": {
                "A": "A team site is for a specific group to collaborate and co-author, not broad one-to-many publishing.",
                "C": "A OneDrive personal site is for an individual's files, not organization-wide communication.",
                "D": "A Microsoft Bookings page is for scheduling appointments, not publishing news.",
            },
            "exam_pattern": "Broadcast news to a broad, read-mostly audience = SharePoint communication site; group collaboration = team site.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): SharePoint communication vs team sites"],
    },
    {
        "id": "ms900-apps-r2-013", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "An operations analyst needs to create professional flowcharts, network diagrams, and organizational charts using standard shapes and connectors. Which Microsoft 365 app is designed for diagramming?",
        "options": [
            {"id": "A", "text": "Microsoft Sway"},
            {"id": "B", "text": "Microsoft To Do"},
            {"id": "C", "text": "Microsoft Visio"},
            {"id": "D", "text": "OneNote"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Visio is the diagramming app for flowcharts, network and org charts, and process maps, using a library of standard shapes and connectors.",
            "distractors": {
                "A": "Microsoft Sway creates interactive presentations and newsletters, not technical diagrams.",
                "B": "Microsoft To Do manages personal tasks, not diagrams.",
                "D": "OneNote captures notes; it is not a structured diagramming tool.",
            },
            "exam_pattern": "Flowcharts, network and org diagrams = Microsoft Visio.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Visio"],
    },
    {
        "id": "ms900-apps-r2-014", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "fill",
        "stem": "Which Power Platform service lets users build automated workflows that trigger actions across apps and services (for example, when a form is submitted, save the file and notify a channel)? It was formerly named Microsoft Flow. Enter the current product name (two words).",
        "correct": ["power automate", "microsoft power automate"],
        "explanation": {
            "correct": "Power Automate (formerly Microsoft Flow) automates workflows across apps and services, running actions in response to triggers.",
            "distractors": {},
            "exam_pattern": "Automated cross-app workflows = Power Automate (formerly Microsoft Flow).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Power Automate"],
    },

    # ----- ms9_teams_collaboration -----
    {
        "id": "ms900-apps-r2-015", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "Within a large team in Microsoft Teams, a few members handling a sensitive budget want a space whose conversations and files are visible ONLY to them, not to everyone in the team. Which Teams feature provides this restricted space?",
        "options": [
            {"id": "A", "text": "A standard channel"},
            {"id": "B", "text": "A sensitivity label"},
            {"id": "C", "text": "A calling plan"},
            {"id": "D", "text": "A private channel"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A private channel is visible and accessible only to the specific team members added to it, giving a focused, restricted space within a broader team.",
            "distractors": {
                "A": "A standard channel is open to all members of the team, so it is not restricted to a subset.",
                "B": "A sensitivity label classifies and protects content; it is not a Teams channel type.",
                "C": "A calling plan enables PSTN calling, unrelated to channel visibility.",
            },
            "exam_pattern": "A space inside a team limited to a subset of members = private channel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams private channels"],
    },
    {
        "id": "ms900-apps-r2-016", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 3, "type": "mcq",
        "stem": "Two companies want to collaborate in a single Teams channel, where people from each organization work together in place using their own Teams accounts - without being added as guests and without switching tenants. Which Teams capability enables this?",
        "options": [
            {"id": "A", "text": "A shared channel (Teams Connect)"},
            {"id": "B", "text": "A private channel"},
            {"id": "C", "text": "Teams Phone"},
            {"id": "D", "text": "Microsoft Whiteboard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shared channels (Teams Connect) let people from different teams or organizations collaborate in one channel using their own identities, without switching tenants or being added as guests to the host team.",
            "distractors": {
                "B": "A private channel restricts access to a subset of the same team's members; it is not for cross-organization sharing in place.",
                "C": "Teams Phone provides PSTN calling, not cross-tenant channel collaboration.",
                "D": "Microsoft Whiteboard is a drawing canvas, not a channel-sharing capability.",
            },
            "exam_pattern": "Collaborate across organizations in one channel using your own identity = shared channel (Teams Connect).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams shared channels (Teams Connect)"],
    },
    {
        "id": "ms900-apps-r2-017", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "A project team wants to add an external consultant, using their own email address, as a member of a specific team so they can access that team's channels, chats, and files. Which capability allows inviting the external person into the team?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Guest access"},
            {"id": "C", "text": "Click-to-Run"},
            {"id": "D", "text": "A retention policy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Guest access lets an organization invite people from outside (using their own email identity) to join a specific team as guests, giving them access to that team's channels, chats, and files.",
            "distractors": {
                "A": "Conditional Access enforces sign-in policies; it does not add external members to a team.",
                "C": "Click-to-Run installs Office apps, unrelated to inviting external collaborators.",
                "D": "A retention policy governs content lifecycle, not external access.",
            },
            "exam_pattern": "Invite an external person INTO a team as a member = guest access.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams guest access"],
    },
    {
        "id": "ms900-apps-r2-018", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 3, "type": "mcq",
        "stem": "An employee wants to chat with and call people at a partner company who use Microsoft Teams in their own tenant, finding them by their email domain, without inviting them into any of their own teams. Which capability is designed for this organization-to-organization communication?",
        "options": [
            {"id": "A", "text": "Guest access"},
            {"id": "B", "text": "A SharePoint team site"},
            {"id": "C", "text": "External access (federation)"},
            {"id": "D", "text": "Mobile application management"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "External access (federation) lets users find, chat, and call people in other Teams organizations by their domain/email, using each side's own identity - without adding anyone as a guest to a team.",
            "distractors": {
                "A": "Guest access brings an external user INTO your team as a member; it is not domain-to-domain chat/call between organizations.",
                "B": "A SharePoint team site stores shared content; it is not a communication channel to another organization.",
                "D": "Mobile application management protects app data on devices, unrelated to external communication.",
            },
            "exam_pattern": "Chat/call another org's Teams users by domain, no team membership = external access (federation); add someone to your team = guest access.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams external access vs guest access"],
    },
    {
        "id": "ms900-apps-r2-019", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "During a large Teams meeting, the facilitator wants to split the attendees into several smaller groups for separate discussions, then bring everyone back to the main meeting afterward. Which Teams meeting feature does this?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Update channels"},
            {"id": "D", "text": "Breakout rooms"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Breakout rooms let a meeting organizer divide participants into smaller rooms for focused group discussion and then return them to the main meeting.",
            "distractors": {
                "A": "Safe Links is an email/URL protection feature, not a meeting breakout feature.",
                "B": "Sensitivity labels classify content; they do not split meeting participants.",
                "C": "Update channels control Microsoft 365 Apps feature cadence, unrelated to meetings.",
            },
            "exam_pattern": "Split a meeting into smaller discussion groups = breakout rooms.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams meetings (breakout rooms)"],
    },
    {
        "id": "ms900-apps-r2-020", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 1, "type": "mcq",
        "stem": "After recording a Teams meeting, participants want to rewatch it later, and the recording should be saved in the organization's Microsoft 365 cloud storage rather than on someone's local disk. Where are Teams meeting recordings stored by default?",
        "options": [
            {"id": "A", "text": "In OneDrive and SharePoint"},
            {"id": "B", "text": "In Microsoft Forms"},
            {"id": "C", "text": "On the organizer's local hard drive only"},
            {"id": "D", "text": "In Microsoft Entra ID"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Teams meeting recordings are saved to Microsoft 365 cloud storage - OneDrive or the channel's SharePoint site - so they can be shared and watched later with existing permissions applied.",
            "distractors": {
                "B": "Microsoft Forms collects survey responses; it does not store video recordings.",
                "C": "Recordings go to the cloud (OneDrive/SharePoint), not solely to a local disk.",
                "D": "Microsoft Entra ID is the identity service, not a storage location for recordings.",
            },
            "exam_pattern": "Teams meeting recordings are stored in OneDrive/SharePoint.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams meeting recordings"],
    },
    {
        "id": "ms900-apps-r2-021", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "A marketing lead wants to host a structured online event for hundreds of external registrants, with a registration page, a managed attendee experience, and attendance reporting. Which Teams capability best fits a large, one-to-many event like this?",
        "options": [
            {"id": "A", "text": "A one-to-one chat"},
            {"id": "B", "text": "A Teams webinar"},
            {"id": "C", "text": "A private channel"},
            {"id": "D", "text": "A OneDrive share link"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A Teams webinar is a structured event format with registration, a presenter/attendee separation, and post-event reporting - suited to large, one-to-many sessions for internal or external audiences.",
            "distractors": {
                "A": "A one-to-one chat is for individual conversations, not a large managed event.",
                "C": "A private channel is a restricted collaboration space, not a broadcast event with registration.",
                "D": "A OneDrive share link shares a file; it does not host a live event.",
            },
            "exam_pattern": "Large, registration-based, one-to-many online event = Teams webinar.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams webinars and events"],
    },
    {
        "id": "ms900-apps-r2-022", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "When a team posts and edits documents inside a standard Teams channel, those files are actually kept in another Microsoft 365 service behind the scenes. Which service stores a standard channel's files?",
        "options": [
            {"id": "A", "text": "Exchange Online"},
            {"id": "B", "text": "Microsoft Bookings"},
            {"id": "C", "text": "SharePoint Online"},
            {"id": "D", "text": "Microsoft Intune"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Each team has an associated SharePoint team site, and files shared in a standard channel are stored in that SharePoint document library - which is why Teams and SharePoint are tightly integrated.",
            "distractors": {
                "A": "Exchange Online stores mailboxes and calendars, not channel files.",
                "B": "Microsoft Bookings schedules appointments, unrelated to file storage.",
                "D": "Microsoft Intune manages devices; it does not store channel files.",
            },
            "exam_pattern": "Files in a Teams standard channel are stored in the team's SharePoint site.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams and SharePoint integration"],
    },
    {
        "id": "ms900-apps-r2-023", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to pin a Power BI dashboard and a Planner board directly into a Teams channel so members can open them without leaving Teams. Which Teams capability lets you add these services into a channel?",
        "options": [
            {"id": "A", "text": "A calling plan"},
            {"id": "B", "text": "Multifactor authentication"},
            {"id": "C", "text": "Retention labels"},
            {"id": "D", "text": "Apps and tabs"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Teams can be extended with apps and tabs, letting you pin services such as Power BI, Planner, SharePoint pages, and third-party tools directly into a channel for in-place access.",
            "distractors": {
                "A": "A calling plan enables PSTN calling, not app integration.",
                "B": "Multifactor authentication secures sign-ins, unrelated to adding apps to channels.",
                "C": "Retention labels govern content lifecycle, not channel extensibility.",
            },
            "exam_pattern": "Pin other services into a Teams channel = apps and tabs (Teams extensibility).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams apps and tabs"],
    },
    {
        "id": "ms900-apps-r2-024", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "An organization is equipping its physical conference rooms with certified devices and consoles that provide one-touch join, in-room cameras, and audio for hybrid Teams meetings. Which Microsoft offering is this?",
        "options": [
            {"id": "A", "text": "Microsoft Teams Rooms"},
            {"id": "B", "text": "Windows 365"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Microsoft Priva"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Teams Rooms is the solution of certified room hardware and software for conference spaces, offering one-touch meeting join and integrated room audio/video for hybrid meetings.",
            "distractors": {
                "B": "Windows 365 provides Cloud PCs, not conference-room meeting systems.",
                "C": "Microsoft Forms is for surveys and quizzes.",
                "D": "Microsoft Priva is a privacy-management solution, unrelated to meeting-room hardware.",
            },
            "exam_pattern": "Certified conference-room meeting hardware/software for Teams = Microsoft Teams Rooms.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Teams Rooms"],
    },
    {
        "id": "ms900-apps-r2-025", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "To make meetings more accessible, an attendee who is hard of hearing wants real-time on-screen text of what speakers are saying during a Teams meeting. Which meeting feature provides this?",
        "options": [
            {"id": "A", "text": "Data loss prevention"},
            {"id": "B", "text": "Live captions"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Co-authoring"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Live captions display real-time text of spoken content during a Teams meeting, improving accessibility for attendees who are deaf or hard of hearing, or in noisy environments.",
            "distractors": {
                "A": "Data loss prevention protects sensitive data; it does not caption speech.",
                "C": "Conditional Access controls sign-ins, unrelated to meeting captions.",
                "D": "Co-authoring is simultaneous document editing, not live meeting captions.",
            },
            "exam_pattern": "Real-time on-screen meeting text for accessibility = live captions.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams accessibility (live captions)"],
    },
    {
        "id": "ms900-apps-r2-026", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "fill",
        "stem": "In Microsoft Teams, what is the channel type called that lets you collaborate in place with specific people outside your team or organization, using their own identity, without adding them as guests or switching tenants? Enter the one-word channel type.",
        "correct": ["shared", "shared channel"],
        "explanation": {
            "correct": "A shared channel (Teams Connect) enables in-place collaboration with people outside the team or organization using their own identities, without guest accounts or tenant switching.",
            "distractors": {},
            "exam_pattern": "In-place cross-org collaboration channel = shared channel (Teams Connect).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams shared channels"],
    },

    # ----- ms9_endpoint_intune -----
    {
        "id": "ms900-apps-r2-027", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "An admin wants Microsoft Intune to check that each enrolled device meets requirements - disk encryption on, a minimum OS version, and a screen-lock PIN - and to flag devices that fall short. Which Intune feature defines and evaluates these requirements?",
        "options": [
            {"id": "A", "text": "A retention label"},
            {"id": "B", "text": "A calling plan"},
            {"id": "C", "text": "A compliance policy"},
            {"id": "D", "text": "A sensitivity label"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An Intune compliance policy defines the rules a device must meet (such as encryption, minimum OS, and a required PIN) and marks each device compliant or noncompliant.",
            "distractors": {
                "A": "A retention label governs how long content is kept, not device health requirements.",
                "B": "A calling plan enables PSTN calling, unrelated to device compliance.",
                "D": "A sensitivity label classifies and protects content, not device settings.",
            },
            "exam_pattern": "Define device requirements and flag devices that fail = Intune compliance policy.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune compliance policies"],
    },
    {
        "id": "ms900-apps-r2-028", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 3, "type": "mcq",
        "stem": "Security wants to allow access to Microsoft 365 only from devices that Intune reports as compliant, and block the rest. Which combination of services works together to enforce this 'compliant device required' rule at sign-in?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings with Microsoft Forms"},
            {"id": "B", "text": "OneDrive with Microsoft Stream"},
            {"id": "C", "text": "Microsoft Whiteboard with Microsoft To Do"},
            {"id": "D", "text": "Microsoft Intune compliance policies with Microsoft Entra Conditional Access"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Intune evaluates device compliance, and Microsoft Entra Conditional Access uses that compliance signal in its sign-in policy - granting access to compliant devices and blocking noncompliant ones.",
            "distractors": {
                "A": "Bookings and Forms handle scheduling and surveys; neither enforces device-based access.",
                "B": "OneDrive and Stream are storage and video services, not access-control enforcement.",
                "C": "Whiteboard and To Do are collaboration and task apps, not access policy tools.",
            },
            "exam_pattern": "Require a compliant device at sign-in = Intune compliance + Entra Conditional Access together.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune and Conditional Access"],
    },
    {
        "id": "ms900-apps-r2-029", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "An IT team wants to push standardized settings - Wi-Fi profiles, a VPN configuration, and email setup - automatically to all enrolled company devices so users do not configure them by hand. Which Intune feature delivers these settings?",
        "options": [
            {"id": "A", "text": "Configuration profiles"},
            {"id": "B", "text": "eDiscovery"},
            {"id": "C", "text": "Safe Attachments"},
            {"id": "D", "text": "Co-authoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Intune configuration profiles push device settings - Wi-Fi, VPN, email, restrictions, and more - to enrolled devices so they are configured consistently without manual setup.",
            "distractors": {
                "B": "eDiscovery finds and holds content for legal cases, unrelated to device settings.",
                "C": "Safe Attachments scans email attachments, not device configuration.",
                "D": "Co-authoring is simultaneous document editing, not a settings-deployment feature.",
            },
            "exam_pattern": "Push standardized device settings (Wi-Fi/VPN/email) = Intune configuration profiles.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune configuration profiles"],
    },
    {
        "id": "ms900-apps-r2-030", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "A company ships brand-new Windows laptops straight to remote employees. When a user powers one on and signs in, it should automatically configure itself and enroll in management with no IT staff touching it first. Which Microsoft technology provides this zero-touch provisioning?",
        "options": [
            {"id": "A", "text": "Office for the web"},
            {"id": "B", "text": "Windows Autopilot"},
            {"id": "C", "text": "Microsoft Secure Score"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Windows Autopilot pre-configures and sets up new Windows devices automatically on first sign-in, enrolling them into management - a zero-touch experience that needs no manual imaging by IT.",
            "distractors": {
                "A": "Office for the web provides browser apps; it does not provision and enroll devices.",
                "C": "Microsoft Secure Score measures security posture, not device provisioning.",
                "D": "Microsoft Bookings schedules appointments, unrelated to device setup.",
            },
            "exam_pattern": "Zero-touch, out-of-box setup and enrollment of new Windows devices = Windows Autopilot.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Windows Autopilot"],
    },
    {
        "id": "ms900-apps-r2-031", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "On managed devices, employees need a self-service app where they can enroll their device, install company-approved apps, and reset their own settings without calling the help desk. Which Intune component provides this user-facing experience?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal"},
            {"id": "B", "text": "The Microsoft 365 roadmap"},
            {"id": "C", "text": "The Company Portal"},
            {"id": "D", "text": "The Message center"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Intune Company Portal is the self-service app/website where users enroll devices, install assigned apps, and perform self-service actions on their managed devices.",
            "distractors": {
                "A": "The Service Trust Portal hosts Microsoft's compliance/audit documents, not device self-service.",
                "B": "The Microsoft 365 roadmap lists upcoming features, not an app-install portal.",
                "D": "The Message center posts tenant change notices, not user device self-service.",
            },
            "exam_pattern": "User self-service to enroll and install approved apps = Intune Company Portal.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune Company Portal"],
    },
    {
        "id": "ms900-apps-r2-032", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "An admin needs to deploy a line-of-business application to all enrolled devices and keep it updated, without visiting each device. Which capability of Microsoft Intune does this?",
        "options": [
            {"id": "A", "text": "Sensitivity labeling"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Retention policies"},
            {"id": "D", "text": "Application deployment to managed devices"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Intune can deploy and assign apps to enrolled users and devices and keep them updated centrally, so software is distributed without touching each device individually.",
            "distractors": {
                "A": "Sensitivity labeling classifies and protects content, not app distribution.",
                "B": "Single sign-on streamlines authentication, not software deployment.",
                "C": "Retention policies govern content lifecycle, unrelated to deploying apps.",
            },
            "exam_pattern": "Centrally push and update apps to managed devices = Intune app deployment.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune app management"],
    },
    {
        "id": "ms900-apps-r2-033", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "An organization has a mix of Windows PCs, Macs, iPhones, and Android devices. It wants ONE cloud console to manage security and settings across all of them. Which description of Microsoft Intune is accurate?",
        "options": [
            {"id": "A", "text": "It is a unified endpoint-management service covering Windows, macOS, iOS/iPadOS, and Android"},
            {"id": "B", "text": "It manages only Windows devices"},
            {"id": "C", "text": "It manages only Apple devices"},
            {"id": "D", "text": "It is an email service for mobile devices"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Intune is a cross-platform (unified) endpoint-management service that manages Windows, macOS, iOS/iPadOS, and Android devices from a single cloud console.",
            "distractors": {
                "B": "Intune is not Windows-only; it manages multiple platforms.",
                "C": "Intune is not limited to Apple devices; it covers Windows and Android too.",
                "D": "Intune manages devices and apps; it is not an email service.",
            },
            "exam_pattern": "One cloud console across Windows/macOS/iOS/Android = Microsoft Intune (unified endpoint management).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Intune (cross-platform management)"],
    },
    {
        "id": "ms900-apps-r2-034", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 1, "type": "mcq",
        "stem": "An older internal document refers to the device-management product as 'Microsoft Endpoint Manager.' What is the current product/family name for Microsoft's cloud endpoint management?",
        "options": [
            {"id": "A", "text": "Microsoft Purview"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Microsoft Entra ID"},
            {"id": "D", "text": "Microsoft Viva"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The product is now known as Microsoft Intune; 'Microsoft Endpoint Manager' was an earlier name for the endpoint-management family.",
            "distractors": {
                "A": "Microsoft Purview is the compliance and data-governance suite, not endpoint management.",
                "C": "Microsoft Entra ID is the identity service, not device management.",
                "D": "Microsoft Viva is the employee experience platform, unrelated to endpoint management.",
            },
            "exam_pattern": "'Microsoft Endpoint Manager' is now called Microsoft Intune.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Intune naming"],
    },
    {
        "id": "ms900-apps-r2-035", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 3, "type": "mcq",
        "stem": "An admin wants to apply Microsoft's recommended, pre-configured group of security settings to managed Windows devices as a known-good starting point, rather than configuring each setting individually. Which Intune feature provides these recommended settings bundles?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Teams channels"},
            {"id": "C", "text": "Security baselines"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Intune security baselines are pre-configured groups of Microsoft-recommended security settings that admins can apply to devices as a vetted starting point and then adjust.",
            "distractors": {
                "A": "Safe Links protects against malicious URLs in email, not device security configuration.",
                "B": "Teams channels organize conversations, unrelated to device security settings.",
                "D": "Microsoft Bookings schedules appointments.",
            },
            "exam_pattern": "Microsoft-recommended, pre-configured device security settings = Intune security baselines.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Intune security baselines"],
    },
    {
        "id": "ms900-apps-r2-036", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 3, "type": "mcq",
        "stem": "A company already manages its Windows PCs with on-premises Configuration Manager but wants to add cloud capabilities by attaching Microsoft Intune, managing the same devices with both tools at once. What is this approach called?",
        "options": [
            {"id": "A", "text": "Co-authoring"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Click-to-Run"},
            {"id": "D", "text": "Co-management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Co-management lets Windows devices be managed concurrently by on-premises Configuration Manager and cloud-based Microsoft Intune, so an organization can add cloud capabilities gradually.",
            "distractors": {
                "A": "Co-authoring is real-time document editing, not device management.",
                "B": "Conditional Access enforces sign-in policy; it is not a dual device-management model.",
                "C": "Click-to-Run installs Office apps, unrelated to managing devices with two tools.",
            },
            "exam_pattern": "Manage Windows with Configuration Manager AND Intune together = co-management.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Co-management (Configuration Manager + Intune)"],
    },
    {
        "id": "ms900-apps-r2-037", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "fill",
        "stem": "Name the Microsoft technology that automatically sets up and enrolls brand-new Windows devices the first time a user signs in, giving a zero-touch, out-of-box deployment (one word after 'Windows'). Enter the single word.",
        "correct": ["autopilot", "windows autopilot"],
        "explanation": {
            "correct": "Windows Autopilot provides zero-touch provisioning, configuring and enrolling new Windows devices automatically on first sign-in.",
            "distractors": {},
            "exam_pattern": "Zero-touch new-device setup and enrollment = Windows Autopilot.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Windows Autopilot"],
    },

    # ----- ms9_analytics_copilot -----
    {
        "id": "ms900-apps-r2-038", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a curated 'home base' inside Microsoft Teams where employees see company news, a resource dashboard, and quick links - acting as a gateway to the digital workplace. Which Microsoft Viva module provides this employee-experience entry point?",
        "options": [
            {"id": "A", "text": "Viva Connections"},
            {"id": "B", "text": "Viva Learning"},
            {"id": "C", "text": "Microsoft Intune"},
            {"id": "D", "text": "Power Automate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Viva Connections provides a personalized gateway to the digital workplace inside Teams - company news, a dashboard of resources, and a feed - as the employee's home base.",
            "distractors": {
                "B": "Viva Learning centralizes training content and courses inside Teams, not a news/resource home base.",
                "C": "Microsoft Intune manages devices, not an employee experience portal.",
                "D": "Power Automate builds workflows, unrelated to an employee home base.",
            },
            "exam_pattern": "Employee home base/gateway in Teams (news, dashboard, resources) = Viva Connections.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Viva Connections"],
    },
    {
        "id": "ms900-apps-r2-039", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "An L&D team wants employees to discover, share, and complete training courses from various content providers in one place inside Microsoft Teams. Which Microsoft Viva module centralizes learning content?",
        "options": [
            {"id": "A", "text": "Viva Connections"},
            {"id": "B", "text": "Viva Learning"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Microsoft Stream"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Viva Learning brings learning content from multiple providers into Microsoft Teams, so employees can discover, share, and track training in the flow of work.",
            "distractors": {
                "A": "Viva Connections is the employee home base/gateway, not a learning hub.",
                "C": "Microsoft Forms creates surveys and quizzes, not a course catalog.",
                "D": "Microsoft Stream hosts videos but is not the aggregated learning module.",
            },
            "exam_pattern": "Aggregated training/learning content in Teams = Viva Learning.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Viva Learning"],
    },
    {
        "id": "ms900-apps-r2-040", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants internal communities and a social, conversational space for employees to connect across departments and with leadership - the successor to Yammer. Which Microsoft Viva module is this?",
        "options": [
            {"id": "A", "text": "Viva Insights"},
            {"id": "B", "text": "Microsoft Bookings"},
            {"id": "C", "text": "Viva Engage"},
            {"id": "D", "text": "Microsoft Lists"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Viva Engage is the communities and conversations module (the successor to Yammer), connecting employees socially across the organization and with leadership.",
            "distractors": {
                "A": "Viva Insights provides productivity and wellbeing analytics, not social communities.",
                "B": "Microsoft Bookings schedules appointments.",
                "D": "Microsoft Lists tracks structured information, not community conversations.",
            },
            "exam_pattern": "Internal communities/social conversations (formerly Yammer) = Viva Engage.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Viva Engage"],
    },
    {
        "id": "ms900-apps-r2-041", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to give employees, managers, and leaders personalized, privacy-protected insights into work patterns - focus time, meeting load, and collaboration habits - to improve productivity and wellbeing. Which Microsoft Viva module provides this?",
        "options": [
            {"id": "A", "text": "Viva Insights"},
            {"id": "B", "text": "Microsoft Whiteboard"},
            {"id": "C", "text": "OneDrive"},
            {"id": "D", "text": "Microsoft Forms"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Viva Insights delivers personalized, privacy-protected productivity and wellbeing insights (focus/quiet time, meeting and collaboration habits) for individuals, with aggregated, de-identified analytics for managers and leaders.",
            "distractors": {
                "B": "Microsoft Whiteboard is a collaborative brainstorming canvas, not analytics.",
                "C": "OneDrive stores personal files; it does not analyze work patterns.",
                "D": "Microsoft Forms creates surveys and quizzes, not productivity insights.",
            },
            "exam_pattern": "Productivity & wellbeing analytics = Viva Insights; Viva Learning = training; Viva Connections = intranet gateway; Viva Engage = communities.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Viva Insights"],
    },
    {
        "id": "ms900-apps-r2-042", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "An analyst wants to ask, in plain language, for trends and insights in a spreadsheet - 'highlight key trends and suggest a formula for projected growth' - directly within the app. Which capability provides this AI help inside Excel?",
        "options": [
            {"id": "A", "text": "Microsoft 365 Copilot in Excel"},
            {"id": "B", "text": "Power Automate"},
            {"id": "C", "text": "A retention label"},
            {"id": "D", "text": "Safe Links"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 Copilot in Excel uses natural-language prompts to analyze data, surface trends, and suggest formulas and visualizations within the spreadsheet.",
            "distractors": {
                "B": "Power Automate builds workflows between apps; it is not the in-Excel AI assistant.",
                "C": "A retention label governs content lifecycle, not data analysis.",
                "D": "Safe Links protects against malicious URLs, unrelated to spreadsheet analysis.",
            },
            "exam_pattern": "Natural-language data analysis/formula help inside Excel = Microsoft 365 Copilot in Excel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Copilot in the apps"],
    },
    {
        "id": "ms900-apps-r2-043", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "A manager wants to turn an existing Word document into a draft slide deck automatically, then refine the layout with prompts, without building each slide by hand. Which capability does this inside PowerPoint?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft 365 Copilot in PowerPoint"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Office for the web"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 Copilot in PowerPoint can generate a draft presentation from a prompt or an existing document and help restructure and design slides through natural-language requests.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not slide creation.",
                "C": "Conditional Access controls sign-ins, unrelated to building decks.",
                "D": "Office for the web is the browser version of the apps, not the AI deck-creation capability itself.",
            },
            "exam_pattern": "Generate/refine slide decks with AI inside PowerPoint = Microsoft 365 Copilot in PowerPoint.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Copilot in the apps"],
    },
    {
        "id": "ms900-apps-r2-044", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "An employee asks Microsoft 365 Copilot to summarize a long Outlook email thread and draft a reply. Which capability is being used?",
        "options": [
            {"id": "A", "text": "Microsoft Intune"},
            {"id": "B", "text": "Microsoft Priva"},
            {"id": "C", "text": "Microsoft 365 Copilot in Outlook"},
            {"id": "D", "text": "A sensitivity label"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft 365 Copilot in Outlook can summarize lengthy email threads, draft and refine replies, and suggest follow-ups within the mail experience.",
            "distractors": {
                "A": "Microsoft Intune manages devices, not email drafting.",
                "B": "Microsoft Priva manages privacy risk, not email summaries.",
                "D": "A sensitivity label classifies and protects content, not composing replies.",
            },
            "exam_pattern": "Summarize threads / draft email replies with AI = Microsoft 365 Copilot in Outlook.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Copilot in the apps"],
    },
    {
        "id": "ms900-apps-r2-045", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 3, "type": "mcq",
        "stem": "A compliance officer asks how Microsoft 365 Copilot handles the organization's data. Which statement best reflects Copilot's enterprise data protection approach?",
        "options": [
            {"id": "A", "text": "It ignores user permissions and lets anyone see any file"},
            {"id": "B", "text": "It publishes the organization's documents publicly to improve answers"},
            {"id": "C", "text": "It requires turning off all security controls to function"},
            {"id": "D", "text": "It honors each user's existing permissions and does not use the organization's tenant data to train the foundation models"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft 365 Copilot is grounded in organizational data through Microsoft Graph while honoring each user's existing permissions, and the organization's tenant data is not used to train the underlying foundation models - part of its enterprise data protection commitments.",
            "distractors": {
                "A": "Copilot respects existing permissions; it does not expose files a user cannot already access.",
                "B": "Copilot does not publish tenant documents publicly.",
                "C": "Copilot works within existing security and compliance controls, not by disabling them.",
            },
            "exam_pattern": "Copilot respects user permissions and does not train foundation models on your tenant data.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Copilot data protection"],
    },
    {
        "id": "ms900-apps-r2-046", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 3, "type": "mcq",
        "stem": "A business team wants to build its own custom AI assistant - for example, an internal HR agent that answers policy questions - using a low-code tool (formerly called Power Virtual Agents). Which Microsoft product is designed for building custom copilots and agents?",
        "options": [
            {"id": "A", "text": "Microsoft Copilot Studio"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "Azure Virtual Desktop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Copilot Studio (formerly Power Virtual Agents) is the low-code tool for building and customizing copilots/agents, such as an internal HR or support assistant.",
            "distractors": {
                "B": "Microsoft Secure Score measures security posture, not AI-agent building.",
                "C": "Microsoft Bookings schedules appointments.",
                "D": "Azure Virtual Desktop provides virtual desktops, unrelated to building copilots.",
            },
            "exam_pattern": "Build custom copilots/agents (formerly Power Virtual Agents) = Microsoft Copilot Studio.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Copilot Studio"],
    },
    {
        "id": "ms900-apps-r2-047", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants content from a third-party system (such as an external knowledge base) to appear in Microsoft Search results and be usable by Microsoft 365 Copilot, by indexing it into Microsoft Graph. Which capability brings that external data in?",
        "options": [
            {"id": "A", "text": "Click-to-Run"},
            {"id": "B", "text": "Microsoft Graph connectors"},
            {"id": "C", "text": "Retention policies"},
            {"id": "D", "text": "Teams Phone"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Graph connectors index external/third-party content into Microsoft Graph, so it surfaces in Microsoft Search and can be used to ground Microsoft 365 Copilot.",
            "distractors": {
                "A": "Click-to-Run installs Office apps, unrelated to indexing external data.",
                "C": "Retention policies govern content lifecycle, not data ingestion for search.",
                "D": "Teams Phone provides PSTN calling, unrelated to Graph data.",
            },
            "exam_pattern": "Index external/third-party data into Microsoft Graph for Search and Copilot = Microsoft Graph connectors.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Graph connectors"],
    },
    {
        "id": "ms900-apps-r2-048", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 1, "type": "fill",
        "stem": "What is the name of Microsoft's employee experience platform, integrated into Microsoft Teams, whose modules include Connections, Learning, Engage, and Insights? Enter the one-word brand name (after 'Microsoft').",
        "correct": ["viva", "microsoft viva"],
        "explanation": {
            "correct": "Microsoft Viva is the employee experience platform in Teams; its modules include Viva Connections, Viva Learning, Viva Engage, and Viva Insights.",
            "distractors": {},
            "exam_pattern": "Employee experience platform in Teams (Connections/Learning/Engage/Insights) = Microsoft Viva.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Viva"],
    },

    # ----- ms9_deployment_options -----
    {
        "id": "ms900-apps-r2-049", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "A small group of IT and pilot users wants to receive new Microsoft 365 Apps features as soon as they are released, to evaluate them before the rest of the company. Which update channel delivers new features most frequently?",
        "options": [
            {"id": "A", "text": "Semi-Annual Enterprise Channel"},
            {"id": "B", "text": "Office LTSC"},
            {"id": "C", "text": "Current Channel"},
            {"id": "D", "text": "Office for the web"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Current Channel delivers new Microsoft 365 Apps features as soon as they are ready (the most frequent cadence), making it well suited to pilot and early-adopter users.",
            "distractors": {
                "A": "Semi-Annual Enterprise Channel delivers features only twice a year, the opposite of 'as soon as released'.",
                "B": "Office LTSC is a perpetual, fixed-feature edition, not a subscription update channel.",
                "D": "Office for the web is the browser version; it is not an install/update channel for the desktop apps.",
            },
            "exam_pattern": "New features as soon as available (fastest) = Current Channel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps update channels (Current)"],
    },
    {
        "id": "ms900-apps-r2-050", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 3, "type": "mcq",
        "stem": "An IT department wants Microsoft 365 Apps feature and security updates to arrive on a single, predictable schedule once a month so they can test and deploy them together. Which update channel fits this predictable monthly cadence?",
        "options": [
            {"id": "A", "text": "Current Channel"},
            {"id": "B", "text": "Beta Channel"},
            {"id": "C", "text": "Office for the web"},
            {"id": "D", "text": "Monthly Enterprise Channel"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Monthly Enterprise Channel delivers feature and security updates once a month on a predictable schedule, balancing newer features with the manageability enterprises want.",
            "distractors": {
                "A": "Current Channel ships updates as soon as they are ready - more frequent and less predictable than a single monthly rollup.",
                "B": "Beta Channel is an unsupported preview channel for early testing, not a predictable production cadence.",
                "C": "Office for the web is the browser version, not an update channel for installed apps.",
            },
            "exam_pattern": "Predictable once-a-month feature/security rollup = Monthly Enterprise Channel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps update channels (Monthly Enterprise)"],
    },
    {
        "id": "ms900-apps-r2-051", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 3, "type": "mcq",
        "stem": "A regulated organization runs specialized line-of-business add-ins and must perform extensive testing before any Office feature change, so it wants new features as infrequently as possible - only a couple of times per year. Which update channel best fits?",
        "options": [
            {"id": "A", "text": "Semi-Annual Enterprise Channel"},
            {"id": "B", "text": "Current Channel"},
            {"id": "C", "text": "Monthly Enterprise Channel"},
            {"id": "D", "text": "Insider/Beta Channel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Semi-Annual Enterprise Channel provides new features only twice a year, giving organizations the longest window to test add-ins and validate changes - ideal for regulated or highly managed environments.",
            "distractors": {
                "B": "Current Channel pushes features as soon as ready, far more often than this scenario allows.",
                "C": "Monthly Enterprise Channel delivers features monthly - still more frequent than twice a year.",
                "D": "Insider/Beta Channel is an unsupported preview with the most frequent changes, the opposite of what is wanted.",
            },
            "exam_pattern": "Fewest, most-tested feature updates (twice a year) = Semi-Annual Enterprise Channel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps update channels (Semi-Annual Enterprise)"],
    },
    {
        "id": "ms900-apps-r2-052", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 3, "type": "mcq",
        "stem": "An admin needs to download and deploy Microsoft 365 Apps to many PCs with a customized configuration - choosing the channel, language, and which apps to include - using a configuration file rather than each user installing manually. Which tool is built for this?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "The Office Deployment Tool (ODT)"},
            {"id": "C", "text": "Microsoft Secure Score"},
            {"id": "D", "text": "The Service Trust Portal"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Office Deployment Tool (ODT) uses a configuration file to download and deploy Microsoft 365 Apps at scale with chosen channel, languages, and apps - for controlled, IT-managed installations.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, unrelated to software deployment.",
                "C": "Microsoft Secure Score measures security posture, not app deployment.",
                "D": "The Service Trust Portal hosts compliance documents, not deployment tooling.",
            },
            "exam_pattern": "Customized, scripted, at-scale Microsoft 365 Apps deployment = Office Deployment Tool (ODT).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Office Deployment Tool"],
    },
    {
        "id": "ms900-apps-r2-053", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "A frequent traveler needs the fullest Office feature set and the ability to work on large files offline on a laptop. Which form of the Office apps best meets this need?",
        "options": [
            {"id": "A", "text": "Office for the web only"},
            {"id": "B", "text": "A read-only PDF export"},
            {"id": "C", "text": "The installed desktop apps (Microsoft 365 Apps)"},
            {"id": "D", "text": "A SharePoint communication site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The installed desktop apps provide the richest, most complete feature set and full offline editing - best for power users and large files - whereas the web apps need a connection and offer a lighter feature set.",
            "distractors": {
                "A": "Office for the web requires internet connectivity and offers fewer advanced features than the desktop apps.",
                "B": "A read-only PDF export cannot be edited and is not an Office app form.",
                "D": "A SharePoint communication site publishes content; it is not an Office editing experience.",
            },
            "exam_pattern": "Fullest features and robust offline editing = installed desktop apps; lightweight/no install = Office for the web.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Office desktop vs web vs mobile"],
    },
    {
        "id": "ms900-apps-r2-054", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 3, "type": "mcq",
        "stem": "A virtual desktop (VDI) environment has many users signing in to the same shared computers, and the Microsoft 365 Apps must activate per user rather than being tied to one device. Which Microsoft 365 Apps feature enables this scenario?",
        "options": [
            {"id": "A", "text": "Click-to-Run"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Update channels"},
            {"id": "D", "text": "Shared computer activation"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Shared computer activation lets Microsoft 365 Apps be used on shared devices (such as VDI or multi-user workstations), activating per signed-in licensed user instead of consuming a per-device installation.",
            "distractors": {
                "A": "Click-to-Run is the install/update technology, not the shared-device activation feature.",
                "B": "Conditional Access controls sign-ins, not Office activation on shared devices.",
                "C": "Update channels control feature cadence, not multi-user activation.",
            },
            "exam_pattern": "Run Microsoft 365 Apps on shared/VDI computers, activating per user = shared computer activation.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Shared computer activation"],
    },
    {
        "id": "ms900-apps-r2-055", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "In a small business without a dedicated deployment process, a licensed user wants to install the Office desktop apps themselves on their own PC. What is the simplest supported way for them to do this?",
        "options": [
            {"id": "A", "text": "Self-install from the Microsoft 365 portal (office.com)"},
            {"id": "B", "text": "Buy new server hardware"},
            {"id": "C", "text": "Submit a legal eDiscovery request"},
            {"id": "D", "text": "Enable a retention policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A licensed user can sign in to the Microsoft 365 portal (office.com) and install the desktop apps themselves via self-service install - the simplest option when there is no managed deployment.",
            "distractors": {
                "B": "No server hardware is needed to install the subscription desktop apps.",
                "C": "An eDiscovery request is a legal/compliance action, unrelated to installing Office.",
                "D": "A retention policy governs content lifecycle, not app installation.",
            },
            "exam_pattern": "Licensed user installs Office themselves = self-service install from the Microsoft 365 portal.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Install Microsoft 365 Apps (self-service)"],
    },
    {
        "id": "ms900-apps-r2-056", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "On a smartphone, an employee needs to quickly review and make light edits to Word and Excel files while away from their computer. Which form of the Office apps is optimized for phones and tablets?",
        "options": [
            {"id": "A", "text": "Office LTSC"},
            {"id": "B", "text": "The Office mobile apps"},
            {"id": "C", "text": "The Office Deployment Tool"},
            {"id": "D", "text": "Shared computer activation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Office mobile apps (for iOS and Android) are optimized for phones and tablets, giving touch-friendly review and light editing on the go.",
            "distractors": {
                "A": "Office LTSC is a perpetual desktop edition, not the mobile experience.",
                "C": "The Office Deployment Tool is an IT deployment utility, not a mobile app form.",
                "D": "Shared computer activation is a licensing feature for shared PCs, not a mobile app.",
            },
            "exam_pattern": "Touch-optimized Office on phones/tablets = the Office mobile apps.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Office mobile apps"],
    },
    {
        "id": "ms900-apps-r2-057", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "Which name refers to the subscription version of the installed Office desktop applications that is included with Microsoft 365 enterprise plans (such as E3 and E5) and kept automatically updated?",
        "options": [
            {"id": "A", "text": "Office LTSC"},
            {"id": "B", "text": "Office for the web"},
            {"id": "C", "text": "Microsoft 365 Apps for enterprise"},
            {"id": "D", "text": "Microsoft Entra ID"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft 365 Apps for enterprise is the subscription desktop Office suite included with enterprise plans like E3 and E5, installed locally and automatically updated.",
            "distractors": {
                "A": "Office LTSC is the perpetual, fixed-feature edition, not the subscription enterprise apps.",
                "B": "Office for the web is the browser version, not the installed desktop suite.",
                "D": "Microsoft Entra ID is the identity service, not an Office apps edition.",
            },
            "exam_pattern": "Subscription desktop Office in enterprise plans = Microsoft 365 Apps for enterprise.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps for enterprise"],
    },
    {
        "id": "ms900-apps-r2-058", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "fill",
        "stem": "Which Microsoft 365 Apps update channel delivers new features as soon as they are ready - the most frequent cadence, often used by pilot users? Enter the channel name (two words).",
        "correct": ["current channel", "current"],
        "explanation": {
            "correct": "Current Channel provides the newest Microsoft 365 Apps features as soon as they are released, the most frequent update cadence.",
            "distractors": {},
            "exam_pattern": "Newest features as soon as available = Current Channel.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps update channels"],
    },

    # ===============================================================
    # DOMAIN 3: ms9_security_compliance
    # ===============================================================

    # ----- ms9_identity_entra -----
    {
        "id": "ms900-sec-r2-001", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "To cut help-desk calls, an organization wants employees to securely reset or unlock their own accounts after verifying their identity, without contacting IT. Which Microsoft Entra capability provides this?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Data loss prevention"},
            {"id": "C", "text": "Co-authoring"},
            {"id": "D", "text": "Self-service password reset (SSPR)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Self-service password reset (SSPR) lets users reset or unlock their own accounts after completing identity verification, reducing help-desk workload.",
            "distractors": {
                "A": "Conditional Access evaluates sign-in policies; it does not let users reset their own passwords.",
                "B": "Data loss prevention protects sensitive data, unrelated to password reset.",
                "C": "Co-authoring is real-time document editing, not an identity feature.",
            },
            "exam_pattern": "Users reset their own passwords after verification = self-service password reset (SSPR).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Self-service password reset"],
    },
    {
        "id": "ms900-sec-r2-002", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to remove passwords from the sign-in process entirely, letting users authenticate with methods like Windows Hello, a FIDO2 security key, or an authenticator app. What is this approach called?",
        "options": [
            {"id": "A", "text": "Passwordless authentication"},
            {"id": "B", "text": "Single sign-on"},
            {"id": "C", "text": "Perpetual licensing"},
            {"id": "D", "text": "Shared computer activation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Passwordless authentication replaces passwords with stronger methods such as Windows Hello for Business, FIDO2 security keys, or the Microsoft Authenticator app - improving security and user experience.",
            "distractors": {
                "B": "Single sign-on reduces repeated sign-ins but still typically relies on a credential like a password.",
                "C": "Perpetual licensing is a purchasing model, unrelated to authentication.",
                "D": "Shared computer activation is an Office licensing feature, not a sign-in method.",
            },
            "exam_pattern": "Sign in without a password (Windows Hello/FIDO2/Authenticator) = passwordless authentication.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Passwordless authentication"],
    },
    {
        "id": "ms900-sec-r2-003", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 1, "type": "mcq",
        "stem": "Which Microsoft app can users install on their phones to approve sign-in requests, provide one-time passcodes for MFA, and enable phone sign-in without a password?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft Authenticator"},
            {"id": "C", "text": "Microsoft Stream"},
            {"id": "D", "text": "Microsoft To Do"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Microsoft Authenticator app approves sign-in requests, generates one-time passcodes, and supports passwordless phone sign-in, serving as a verification factor for MFA.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not sign-in approvals.",
                "C": "Microsoft Stream is a video service, unrelated to authentication.",
                "D": "Microsoft To Do manages personal tasks, not MFA.",
            },
            "exam_pattern": "App for approvals, one-time codes, and passwordless phone sign-in = Microsoft Authenticator.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Authenticator"],
    },
    {
        "id": "ms900-sec-r2-004", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 3, "type": "mcq",
        "stem": "A security team wants Microsoft Entra to automatically detect risky sign-ins - such as logins from anonymous IP addresses or atypical locations - and flag potentially compromised accounts so policy can respond. Which capability provides this risk detection?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Retention labels"},
            {"id": "C", "text": "Microsoft Entra ID Protection"},
            {"id": "D", "text": "Office for the web"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Entra ID Protection uses signals and machine learning to detect risky sign-ins and risky users (such as leaked credentials or anonymous-IP logins), feeding risk-based Conditional Access responses.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not risk detection.",
                "B": "Retention labels govern content lifecycle, unrelated to sign-in risk.",
                "D": "Office for the web is the browser apps, not an identity-risk service.",
            },
            "exam_pattern": "Detect risky sign-ins/compromised accounts in Entra = Microsoft Entra ID Protection.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Entra ID Protection"],
    },
    {
        "id": "ms900-sec-r2-005", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 3, "type": "mcq",
        "stem": "To limit standing administrative access, an organization wants admins to hold no permanent privileged role, instead requesting time-limited, just-in-time activation (with approval) only when they need it. Which Microsoft Entra capability provides this?",
        "options": [
            {"id": "A", "text": "Single sign-on"},
            {"id": "B", "text": "Safe Attachments"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Privileged Identity Management (PIM)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Privileged Identity Management (PIM) provides just-in-time, time-bound activation of privileged roles - often with approval and auditing - so admins do not hold standing elevated access.",
            "distractors": {
                "A": "Single sign-on streamlines authentication; it does not manage just-in-time privileged access.",
                "B": "Safe Attachments scans email attachments, unrelated to admin role activation.",
                "C": "Microsoft Forms creates surveys and quizzes.",
            },
            "exam_pattern": "Just-in-time, time-limited privileged role access = Privileged Identity Management (PIM).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Privileged Identity Management"],
    },
    {
        "id": "ms900-sec-r2-006", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to let partners and vendors from other organizations access certain apps and resources using their OWN existing credentials, rather than creating and managing separate passwords for them. Which Microsoft Entra capability enables this external collaboration?",
        "options": [
            {"id": "A", "text": "Microsoft Entra B2B collaboration (external/guest identities)"},
            {"id": "B", "text": "Shared computer activation"},
            {"id": "C", "text": "Microsoft Secure Score"},
            {"id": "D", "text": "Click-to-Run"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra B2B collaboration lets external users (guests) access resources using their own identities/credentials, so the host organization does not manage separate accounts for them.",
            "distractors": {
                "B": "Shared computer activation is an Office licensing feature, not external identity.",
                "C": "Microsoft Secure Score measures security posture, not external collaboration.",
                "D": "Click-to-Run installs Office apps, unrelated to guest access.",
            },
            "exam_pattern": "External partners using their own credentials to access resources = Entra B2B (guest) collaboration.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Entra External ID / B2B"],
    },
    {
        "id": "ms900-sec-r2-007", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "A very small organization has no time to design custom access policies but wants Microsoft's preconfigured baseline protections - like requiring multifactor authentication registration and blocking legacy authentication - turned on with a single toggle. Which Microsoft Entra feature provides this baseline?",
        "options": [
            {"id": "A", "text": "eDiscovery"},
            {"id": "B", "text": "Security defaults"},
            {"id": "C", "text": "Teams channels"},
            {"id": "D", "text": "Sensitivity labels"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Security defaults provide a free, preconfigured set of baseline identity protections (including MFA registration and blocking legacy authentication) suitable for organizations that are not using custom Conditional Access policies.",
            "distractors": {
                "A": "eDiscovery finds and holds content for legal cases, unrelated to identity baselines.",
                "C": "Teams channels organize conversations, not security baselines.",
                "D": "Sensitivity labels classify content, not sign-in protections.",
            },
            "exam_pattern": "One-click preconfigured baseline identity protections = security defaults.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Security defaults"],
    },
    {
        "id": "ms900-sec-r2-008", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 3, "type": "mcq",
        "stem": "An organization keeps its on-premises Active Directory but wants those same user accounts and passwords usable to sign in to Microsoft 365 in the cloud. Which tool synchronizes on-premises identities to Microsoft Entra ID to enable this hybrid identity?",
        "options": [
            {"id": "A", "text": "Microsoft Priva"},
            {"id": "B", "text": "Microsoft Bookings"},
            {"id": "C", "text": "Microsoft Entra Connect"},
            {"id": "D", "text": "Microsoft Whiteboard"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Entra Connect synchronizes on-premises Active Directory accounts (and, optionally, password hashes) to Microsoft Entra ID, enabling hybrid identity and a common sign-in for cloud and on-premises.",
            "distractors": {
                "A": "Microsoft Priva manages privacy risk, not identity synchronization.",
                "B": "Microsoft Bookings schedules appointments.",
                "D": "Microsoft Whiteboard is a collaboration canvas, unrelated to directory sync.",
            },
            "exam_pattern": "Sync on-premises AD to the cloud for hybrid identity = Microsoft Entra Connect.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Hybrid identity (Microsoft Entra Connect)"],
    },
    {
        "id": "ms900-sec-r2-009", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "A trainer explains two identity terms: one is the process of PROVING who a user is, and the other is the process of determining WHAT that verified user is allowed to access. Which pairing is correct?",
        "options": [
            {"id": "A", "text": "Authorization proves identity; authentication determines access"},
            {"id": "B", "text": "Both terms mean exactly the same thing"},
            {"id": "C", "text": "Authentication and authorization both only apply to devices, not users"},
            {"id": "D", "text": "Authentication proves identity; authorization determines access"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Authentication (AuthN) verifies who a user is, while authorization (AuthZ) determines what that verified user is permitted to do or access - two distinct steps.",
            "distractors": {
                "A": "This reverses the definitions; authentication verifies identity and authorization grants access.",
                "B": "They are related but different: one proves identity, the other grants permissions.",
                "C": "Both apply to users (and other principals), not only devices.",
            },
            "exam_pattern": "AuthN = prove who you are; AuthZ = what you're allowed to access.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Authentication vs authorization"],
    },
    {
        "id": "ms900-sec-r2-010", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "fill",
        "stem": "Which Microsoft Entra capability lets users securely reset or unlock their own accounts without calling the help desk? Enter the common four-letter acronym.",
        "correct": ["sspr", "self-service password reset", "self service password reset"],
        "explanation": {
            "correct": "Self-service password reset (SSPR) lets users reset or unlock their own accounts after verifying their identity, reducing help-desk calls.",
            "distractors": {},
            "exam_pattern": "Users reset their own passwords = SSPR.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Self-service password reset"],
    },

    # ----- ms9_threat_protection -----
    {
        "id": "ms900-sec-r2-011", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to detect, investigate, and respond to threats on laptops and servers themselves - with endpoint detection and response (EDR) and automated remediation on the devices. Which Microsoft Defender product protects endpoints?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Endpoint"},
            {"id": "B", "text": "Microsoft Defender for Office 365"},
            {"id": "C", "text": "Microsoft Priva"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Endpoint provides endpoint detection and response (EDR), threat and vulnerability insights, and automated remediation on devices such as laptops and servers.",
            "distractors": {
                "B": "Microsoft Defender for Office 365 protects email and collaboration, not the devices themselves.",
                "C": "Microsoft Priva manages privacy risk, not endpoint threats.",
                "D": "Microsoft Bookings schedules appointments, unrelated to security.",
            },
            "exam_pattern": "EDR and threat response on devices = Microsoft Defender for Endpoint.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Defender for Endpoint"],
    },
    {
        "id": "ms900-sec-r2-012", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants to detect identity-based attacks against its on-premises Active Directory - such as compromised accounts and lateral movement - by analyzing domain controller signals. Which Microsoft Defender product is designed for this?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Endpoint"},
            {"id": "B", "text": "Microsoft Defender for Identity"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Microsoft Stream"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Defender for Identity uses signals from on-premises Active Directory (domain controllers) to detect identity-based threats like compromised accounts and lateral movement.",
            "distractors": {
                "A": "Microsoft Defender for Endpoint protects devices/endpoints, not Active Directory identity signals specifically.",
                "C": "Microsoft Forms creates surveys and quizzes.",
                "D": "Microsoft Stream is a video service, unrelated to identity threat detection.",
            },
            "exam_pattern": "Detect identity attacks from on-prem AD signals = Microsoft Defender for Identity.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Defender for Identity"],
    },
    {
        "id": "ms900-sec-r2-013", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 3, "type": "mcq",
        "stem": "IT suspects employees are using unsanctioned cloud (SaaS) apps - 'shadow IT' - and wants to discover which cloud apps are in use and govern access to them. Which Microsoft Defender product acts as a cloud access security broker (CASB) for this?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Office 365"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Microsoft Defender for Cloud Apps"},
            {"id": "D", "text": "Microsoft Entra Connect"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Defender for Cloud Apps is a cloud access security broker (CASB) that discovers cloud app usage (including shadow IT), assesses risk, and helps govern access to SaaS apps.",
            "distractors": {
                "A": "Microsoft Defender for Office 365 protects email and collaboration, not SaaS app discovery.",
                "B": "Microsoft Intune manages devices, not cloud-app discovery and governance.",
                "D": "Microsoft Entra Connect synchronizes identities; it is not a CASB.",
            },
            "exam_pattern": "Discover/govern SaaS apps and shadow IT (CASB) = Microsoft Defender for Cloud Apps.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Defender for Cloud Apps"],
    },
    {
        "id": "ms900-sec-r2-014", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "A company is worried that attackers send emails whose links look safe at delivery but become malicious later. It wants URLs re-checked at the exact moment a user clicks them. Which Microsoft Defender for Office 365 feature provides this time-of-click protection?",
        "options": [
            {"id": "A", "text": "Safe Attachments"},
            {"id": "B", "text": "Retention policies"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "Safe Links"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Safe Links checks URLs at the time a user clicks them (not just at delivery), protecting against links that are weaponized after the message arrives.",
            "distractors": {
                "A": "Safe Attachments detonates attachments in a sandbox; it protects files, not click-time URLs.",
                "B": "Retention policies govern content lifecycle, not link protection.",
                "C": "Sensitivity labels classify and protect content, not URLs at click time.",
            },
            "exam_pattern": "Re-check URLs at the moment of click = Safe Links; sandbox attachments = Safe Attachments.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Defender for Office 365 Safe Links"],
    },
    {
        "id": "ms900-sec-r2-015", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "To defend against business email compromise, an organization wants protection that detects when a message tries to impersonate an executive or a trusted domain. Which type of Microsoft Defender for Office 365 policy addresses impersonation and spoofing?",
        "options": [
            {"id": "A", "text": "Anti-phishing policies"},
            {"id": "B", "text": "Update channels"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "A calling plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anti-phishing policies in Defender for Office 365 detect impersonation of users and domains and spoofing attempts, helping defend against business email compromise.",
            "distractors": {
                "B": "Update channels control Microsoft 365 Apps feature cadence, not phishing defense.",
                "C": "Conditional Access controls sign-in access, not email impersonation detection.",
                "D": "A calling plan enables PSTN calling, unrelated to phishing.",
            },
            "exam_pattern": "Detect impersonation/spoofing in email = anti-phishing policies (Defender for Office 365).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Defender for Office 365 anti-phishing"],
    },
    {
        "id": "ms900-sec-r2-016", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to send employees realistic but harmless simulated phishing emails to measure who falls for them and automatically assign targeted training. Which Microsoft Defender for Office 365 capability does this?",
        "options": [
            {"id": "A", "text": "Data loss prevention"},
            {"id": "B", "text": "Attack simulation training"},
            {"id": "C", "text": "eDiscovery"},
            {"id": "D", "text": "Co-authoring"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Attack simulation training runs benign, realistic phishing simulations, measures user susceptibility, and assigns targeted training to improve security awareness.",
            "distractors": {
                "A": "Data loss prevention stops oversharing of sensitive data; it does not run phishing simulations.",
                "C": "eDiscovery finds and holds content for legal cases, unrelated to user training.",
                "D": "Co-authoring is simultaneous document editing, not security training.",
            },
            "exam_pattern": "Simulated phishing + assigned training = attack simulation training.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Attack simulation training"],
    },
    {
        "id": "ms900-sec-r2-017", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "An analyst wants one unified portal to view and manage correlated incidents, alerts, and hunting across Defender for Endpoint, Office 365, Identity, and Cloud Apps. Which portal brings Microsoft Defender XDR together?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal"},
            {"id": "B", "text": "The Microsoft 365 roadmap"},
            {"id": "C", "text": "The Microsoft Defender portal"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Microsoft Defender portal is the unified console for Microsoft Defender XDR, where correlated incidents, alerts, and advanced hunting across the Defender workloads are managed.",
            "distractors": {
                "A": "The Service Trust Portal hosts compliance/audit documents, not security incidents.",
                "B": "The Microsoft 365 roadmap lists upcoming features, not security operations.",
                "D": "Microsoft Bookings schedules appointments.",
            },
            "exam_pattern": "Unified console for Defender XDR incidents/hunting = the Microsoft Defender portal.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Defender portal"],
    },
    {
        "id": "ms900-sec-r2-018", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 3, "type": "mcq",
        "stem": "Before attackers can exploit them, a security team wants to continuously discover, assess, and prioritize software vulnerabilities and misconfigurations on their managed devices. Which Microsoft Defender capability focuses on this?",
        "options": [
            {"id": "A", "text": "Safe Attachments"},
            {"id": "B", "text": "Retention labels"},
            {"id": "C", "text": "Single sign-on"},
            {"id": "D", "text": "Microsoft Defender Vulnerability Management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Defender Vulnerability Management continuously discovers, assesses, and prioritizes device vulnerabilities and misconfigurations so teams can remediate the highest-risk issues first.",
            "distractors": {
                "A": "Safe Attachments sandboxes email attachments; it does not assess device vulnerabilities.",
                "B": "Retention labels govern content lifecycle, unrelated to vulnerabilities.",
                "C": "Single sign-on streamlines authentication, not vulnerability assessment.",
            },
            "exam_pattern": "Continuously find/prioritize device vulnerabilities = Microsoft Defender Vulnerability Management.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Defender Vulnerability Management"],
    },
    {
        "id": "ms900-sec-r2-019", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "fill",
        "stem": "In Microsoft Defender for Office 365, name the feature that verifies the safety of a URL at the moment a user clicks it (rather than only when the email is delivered). Enter the feature name (two words).",
        "correct": ["safe links", "safe link"],
        "explanation": {
            "correct": "Safe Links checks URLs at time-of-click, protecting users from links that become malicious after a message is delivered.",
            "distractors": {},
            "exam_pattern": "Time-of-click URL protection = Safe Links.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Defender for Office 365 Safe Links"],
    },

    # ----- ms9_compliance_purview -----
    {
        "id": "ms900-sec-r2-020", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "A compliance lead wants a dashboard that scores the organization's compliance posture, maps controls to regulations like GDPR, and lists prioritized improvement actions to raise the score. Which Microsoft Purview solution provides this?",
        "options": [
            {"id": "A", "text": "Compliance Manager"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "Microsoft Intune"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Purview Compliance Manager assesses compliance posture, provides a compliance score, maps controls to regulations via assessment templates, and recommends prioritized improvement actions.",
            "distractors": {
                "B": "Microsoft Secure Score measures SECURITY posture, not regulatory compliance posture.",
                "C": "Microsoft Intune manages devices, not compliance scoring.",
                "D": "Microsoft Bookings schedules appointments.",
            },
            "exam_pattern": "Compliance score + improvement actions + regulatory templates = Compliance Manager (security posture = Secure Score).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Purview Compliance Manager"],
    },
    {
        "id": "ms900-sec-r2-021", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 3, "type": "mcq",
        "stem": "A company is concerned that a departing employee might take confidential files, and more broadly wants to detect and investigate risky internal activities such as data theft or leaks. Which Microsoft Purview solution is designed for this?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Insider Risk Management"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Microsoft Stream"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Purview Insider Risk Management helps detect, investigate, and act on risky internal activities - like data theft by a departing employee or inadvertent leaks - using configurable policies and signals.",
            "distractors": {
                "A": "Safe Links protects against malicious URLs in email, not insider activity.",
                "C": "Conditional Access controls sign-in access, not internal data-risk detection.",
                "D": "Microsoft Stream is a video service, unrelated to insider risk.",
            },
            "exam_pattern": "Detect/investigate risky insider activity (data theft, leaks) = Insider Risk Management.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Insider Risk Management"],
    },
    {
        "id": "ms900-sec-r2-022", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 3, "type": "mcq",
        "stem": "A regulated firm must monitor employee messages in Teams and email for policy violations such as harassment or sharing of inappropriate content, with reviewers and remediation workflows. Which Microsoft Purview solution addresses this?",
        "options": [
            {"id": "A", "text": "Data loss prevention"},
            {"id": "B", "text": "Multifactor authentication"},
            {"id": "C", "text": "Communication Compliance"},
            {"id": "D", "text": "Windows Autopilot"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Purview Communication Compliance detects and helps remediate policy violations in messages (Teams, email, Viva Engage) - such as harassment or inappropriate/regulated content - with reviewer workflows.",
            "distractors": {
                "A": "Data loss prevention focuses on sensitive-data oversharing, not monitoring message content for conduct violations.",
                "B": "Multifactor authentication verifies sign-ins, unrelated to message monitoring.",
                "D": "Windows Autopilot provisions devices, not communication monitoring.",
            },
            "exam_pattern": "Monitor messages for conduct/policy violations = Communication Compliance; prevent sensitive-data leaks = DLP.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Communication Compliance"],
    },
    {
        "id": "ms900-sec-r2-023", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "To meet formal recordkeeping obligations, an organization needs to declare certain documents as immutable 'records,' manage their retention and disposition, and maintain a file plan. Which Microsoft Purview capability provides this?",
        "options": [
            {"id": "A", "text": "Co-authoring"},
            {"id": "B", "text": "Teams Phone"},
            {"id": "C", "text": "Microsoft Secure Score"},
            {"id": "D", "text": "Records Management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Purview Records Management lets organizations declare content as records, apply retention and disposition, and maintain a file plan to satisfy recordkeeping requirements.",
            "distractors": {
                "A": "Co-authoring is simultaneous document editing, not records declaration.",
                "B": "Teams Phone provides PSTN calling, unrelated to records.",
                "C": "Microsoft Secure Score measures security posture, not recordkeeping.",
            },
            "exam_pattern": "Declare records, manage disposition and file plans = Records Management.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Records Management"],
    },
    {
        "id": "ms900-sec-r2-024", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "During an investigation, a compliance officer needs to review a log of who did what across Microsoft 365 - which admin changed a setting, who accessed or deleted a file - over a period of time. Which Microsoft Purview capability records this activity?",
        "options": [
            {"id": "A", "text": "Audit (audit log)"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Office for the web"},
            {"id": "D", "text": "Microsoft Whiteboard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Purview Audit records user and admin activities across Microsoft 365 into a searchable audit log, supporting investigations and compliance reviews.",
            "distractors": {
                "B": "Sensitivity labels classify and protect content; they do not log activity.",
                "C": "Office for the web is the browser apps, not an audit capability.",
                "D": "Microsoft Whiteboard is a collaboration canvas, unrelated to activity logging.",
            },
            "exam_pattern": "Searchable log of user/admin activity across Microsoft 365 = Audit (audit log).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Purview Audit"],
    },
    {
        "id": "ms900-sec-r2-025", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "An investigator needs to search across mailboxes, SharePoint sites, OneDrive, and Teams to find all content containing a specific keyword, without necessarily running a full legal case workflow. Which Microsoft Purview capability performs this cross-service search?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Content Search"},
            {"id": "C", "text": "Retention labels"},
            {"id": "D", "text": "Microsoft Intune"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Content Search lets investigators search across Exchange mailboxes, SharePoint, OneDrive, and Teams for content matching criteria, and export results - a lighter-weight tool than a full eDiscovery case.",
            "distractors": {
                "A": "Conditional Access controls sign-in access, not content search.",
                "C": "Retention labels govern content lifecycle, not searching for content.",
                "D": "Microsoft Intune manages devices, unrelated to content search.",
            },
            "exam_pattern": "Search content across Microsoft 365 services = Content Search.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Content Search"],
    },
    {
        "id": "ms900-sec-r2-026", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 3, "type": "mcq",
        "stem": "At an investment bank, regulations require that the team advising a client cannot communicate with the team trading that client's stock, to avoid conflicts of interest. Which Microsoft Purview capability enforces such restrictions between groups?",
        "options": [
            {"id": "A", "text": "Safe Attachments"},
            {"id": "B", "text": "Self-service password reset"},
            {"id": "C", "text": "Information Barriers"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Information Barriers restrict or block communication and collaboration between specific groups of users (ethical walls), helping meet conflict-of-interest and regulatory requirements.",
            "distractors": {
                "A": "Safe Attachments scans email attachments, not inter-group communication.",
                "B": "Self-service password reset is an identity convenience, unrelated to communication restrictions.",
                "D": "Microsoft Bookings schedules appointments.",
            },
            "exam_pattern": "Block communication between conflicting groups (ethical walls) = Information Barriers.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Information Barriers"],
    },
    {
        "id": "ms900-sec-r2-027", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "An employee must email sensitive information to an external recipient and wants the message encrypted so only the intended recipient can read it, even outside the organization. Which Microsoft Purview capability provides this email protection?",
        "options": [
            {"id": "A", "text": "Microsoft Secure Score"},
            {"id": "B", "text": "Click-to-Run"},
            {"id": "C", "text": "Microsoft Lists"},
            {"id": "D", "text": "Microsoft Purview Message Encryption"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Purview Message Encryption lets users send encrypted, access-controlled email to recipients inside or outside the organization, so only intended recipients can read it.",
            "distractors": {
                "A": "Microsoft Secure Score measures security posture, not email encryption.",
                "B": "Click-to-Run installs Office apps, unrelated to message encryption.",
                "C": "Microsoft Lists tracks information, not encrypted email.",
            },
            "exam_pattern": "Encrypt/restrict email to internal or external recipients = Microsoft Purview Message Encryption.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Purview Message Encryption"],
    },
    {
        "id": "ms900-sec-r2-028", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "To make data loss prevention and labeling work, Microsoft Purview must first recognize when content contains patterns like credit-card numbers, passport numbers, or national IDs. What are these built-in pattern definitions called?",
        "options": [
            {"id": "A", "text": "Sensitive information types"},
            {"id": "B", "text": "Update channels"},
            {"id": "C", "text": "Teams channels"},
            {"id": "D", "text": "Calling plans"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitive information types are the built-in (and custom) pattern definitions Microsoft Purview uses to detect data such as credit-card, passport, or national ID numbers, powering DLP and auto-labeling.",
            "distractors": {
                "B": "Update channels control Microsoft 365 Apps feature cadence, not data detection.",
                "C": "Teams channels organize conversations, not data patterns.",
                "D": "Calling plans enable PSTN calling, unrelated to sensitive-data detection.",
            },
            "exam_pattern": "Built-in patterns that detect sensitive data (SSNs, card numbers) = sensitive information types.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Sensitive information types"],
    },
    {
        "id": "ms900-sec-r2-029", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "fill",
        "stem": "Which Microsoft Purview solution gives an organization a compliance score and a prioritized list of recommended improvement actions, with assessment templates mapped to regulations? Enter the two-word solution name.",
        "correct": ["compliance manager", "purview compliance manager", "microsoft purview compliance manager"],
        "explanation": {
            "correct": "Microsoft Purview Compliance Manager measures compliance posture (a compliance score) and provides prioritized improvement actions using regulation-mapped assessment templates.",
            "distractors": {},
            "exam_pattern": "Compliance score + improvement actions = Compliance Manager.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Compliance Manager"],
    },

    # ----- ms9_zero_trust_privacy -----
    {
        "id": "ms900-sec-r2-030", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 3, "type": "mcq",
        "stem": "Under Zero Trust, every access request is authenticated and authorized using all available signals - the user's identity, device health, location, and risk - on each attempt, rather than trusting a request just because it comes from the corporate network. Which Zero Trust guiding principle does this describe?",
        "options": [
            {"id": "A", "text": "Trust everything inside the perimeter"},
            {"id": "B", "text": "Verify explicitly"},
            {"id": "C", "text": "Disable all authentication"},
            {"id": "D", "text": "Perpetual licensing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "'Verify explicitly' means always authenticate and authorize based on all available data points (identity, device, location, risk) for every request - never assuming trust by network location.",
            "distractors": {
                "A": "Trusting everything inside the perimeter is the old castle-and-moat model that Zero Trust rejects.",
                "C": "Zero Trust strengthens verification; it never disables authentication.",
                "D": "Perpetual licensing is a purchasing model, not a Zero Trust principle.",
            },
            "exam_pattern": "Authenticate/authorize on all signals every time = 'verify explicitly' (a Zero Trust principle).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Zero Trust principles (verify explicitly)"],
    },
    {
        "id": "ms900-sec-r2-031", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 3, "type": "mcq",
        "stem": "A security architect designs the network and access so that, if attackers do get in, the damage is contained - using segmentation, end-to-end encryption, and analytics to limit the blast radius. Which Zero Trust principle is being applied?",
        "options": [
            {"id": "A", "text": "Trust by default"},
            {"id": "B", "text": "Economies of scale"},
            {"id": "C", "text": "Assume breach"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "'Assume breach' means operating as if an attacker is already present - segmenting access, encrypting end to end, and using analytics to detect threats and minimize the blast radius.",
            "distractors": {
                "A": "Trusting by default is the opposite of Zero Trust.",
                "B": "Economies of scale is a cloud cost benefit, not a security principle.",
                "D": "Single sign-on is an authentication convenience, not the 'assume breach' principle.",
            },
            "exam_pattern": "Segment and limit blast radius as if already breached = 'assume breach' (a Zero Trust principle).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Zero Trust principles (assume breach)"],
    },
    {
        "id": "ms900-sec-r2-032", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A security strategy applies multiple independent layers of protection - physical, identity, network, application, and data - so that if one layer is bypassed, others still protect the asset. What is this layered approach called?",
        "options": [
            {"id": "A", "text": "A single sign-on"},
            {"id": "B", "text": "A service level agreement"},
            {"id": "C", "text": "Co-authoring"},
            {"id": "D", "text": "Defense in depth"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defense in depth uses multiple layers of security controls so that if one layer fails or is bypassed, subsequent layers continue to protect the asset.",
            "distractors": {
                "A": "Single sign-on is an authentication convenience, not a layered-defense strategy.",
                "B": "A service level agreement is an availability commitment, not a security layering concept.",
                "C": "Co-authoring is real-time document editing, unrelated to layered security.",
            },
            "exam_pattern": "Multiple independent protective layers = defense in depth.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Defense in depth"],
    },
    {
        "id": "ms900-sec-r2-033", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 3, "type": "mcq",
        "stem": "A customer wants a public website that explains, in plain terms, how Microsoft approaches privacy, security, and compliance across its products - distinct from the portal that hosts the actual downloadable audit reports and certifications. Which resource is this public explainer?",
        "options": [
            {"id": "A", "text": "The Microsoft Trust Center"},
            {"id": "B", "text": "The Service Trust Portal"},
            {"id": "C", "text": "The Message center"},
            {"id": "D", "text": "The Microsoft 365 admin center"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Trust Center is the public site explaining Microsoft's approach to privacy, security, and compliance; the Service Trust Portal is where the actual audit reports and certifications are obtained.",
            "distractors": {
                "B": "The Service Trust Portal hosts the downloadable audit reports/certifications - it is not the plain-language public explainer.",
                "C": "The Message center posts tenant change notices, not trust information.",
                "D": "The Microsoft 365 admin center manages users and billing, not public trust content.",
            },
            "exam_pattern": "Public explainer of privacy/security/compliance = Trust Center; audit reports/certs = Service Trust Portal.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Trust Center vs Service Trust Portal"],
    },
    {
        "id": "ms900-sec-r2-034", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Under privacy regulations, individuals can ask an organization for a copy of the personal data it holds about them. A company wants to discover, review, and fulfill these requests efficiently. Which Microsoft Priva capability is designed for this?",
        "options": [
            {"id": "A", "text": "Safe Attachments"},
            {"id": "B", "text": "Subject Rights Requests"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Microsoft Whiteboard"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Priva Subject Rights Requests helps organizations discover, review, and fulfill individuals' data (subject) requests - such as requests for a copy of their personal data - more efficiently.",
            "distractors": {
                "A": "Safe Attachments scans email attachments, unrelated to privacy requests.",
                "C": "Conditional Access controls sign-ins, not data subject requests.",
                "D": "Microsoft Whiteboard is a collaboration canvas.",
            },
            "exam_pattern": "Manage/fulfill individuals' data (subject) requests = Priva Subject Rights Requests.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Priva Subject Rights Requests"],
    },
    {
        "id": "ms900-sec-r2-035", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A prospective customer asks what Microsoft does with their organization's data in Microsoft 365. Which statement reflects Microsoft's stated privacy commitments?",
        "options": [
            {"id": "A", "text": "Microsoft sells customer content to advertisers"},
            {"id": "B", "text": "Customer data automatically becomes public"},
            {"id": "C", "text": "The customer owns and controls their data, and Microsoft does not use it to build advertising profiles"},
            {"id": "D", "text": "Customers lose all rights to their data once uploaded"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft's privacy commitments state that customers own and control their data, and that Microsoft does not use customer content to build advertising profiles or mine it for advertising.",
            "distractors": {
                "A": "Microsoft does not sell customer content to advertisers; this contradicts its commitments.",
                "B": "Customer data does not become public; it remains the customer's, with strong protections.",
                "D": "Customers retain ownership and rights to their data; they do not lose them on upload.",
            },
            "exam_pattern": "You own and control your data; Microsoft does not use it for advertising.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft privacy principles"],
    },
    {
        "id": "ms900-sec-r2-036", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "fill",
        "stem": "Which Zero Trust guiding principle means granting users only the minimum access they need - using just-enough and just-in-time access and risk-based policies? Enter the two-word phrase (the '___ privilege' principle).",
        "correct": ["least privilege", "use least privilege access", "least privilege access"],
        "explanation": {
            "correct": "The 'use least privilege access' principle limits users to the minimum access required, using just-enough/just-in-time access and adaptive, risk-based policies.",
            "distractors": {},
            "exam_pattern": "Grant only the minimum access needed = least privilege (a Zero Trust principle).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Zero Trust principles (least privilege)"],
    },

    # ===============================================================
    # DOMAIN 4: ms9_pricing_support
    # ===============================================================

    # ----- ms9_licensing -----
    {
        "id": "ms900-price-r2-001", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 3, "type": "mcq",
        "stem": "A 200-person company wants the desktop Office apps and cloud services, PLUS built-in advanced security (Defender), device management with Intune, and Microsoft Entra ID P1 - in a single plan aimed at small and medium-sized businesses. Which Microsoft 365 plan fits best?",
        "options": [
            {"id": "A", "text": "Microsoft 365 Business Basic"},
            {"id": "B", "text": "Microsoft 365 Business Standard"},
            {"id": "C", "text": "Office LTSC"},
            {"id": "D", "text": "Microsoft 365 Business Premium"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft 365 Business Premium is the SMB plan that adds advanced security (Microsoft Defender), device management (Intune), and Microsoft Entra ID P1 on top of the desktop apps and cloud services found in Business Standard.",
            "distractors": {
                "A": "Business Basic lacks the installed desktop apps and the advanced security/device management described.",
                "B": "Business Standard includes the desktop apps and cloud services but not the advanced security, Intune, and Entra ID P1.",
                "C": "Office LTSC is a perpetual apps-only edition with no cloud services or security tooling.",
            },
            "exam_pattern": "SMB needing desktop apps PLUS advanced security/Intune/Entra P1 = Microsoft 365 Business Premium.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Business Premium"],
    },
    {
        "id": "ms900-price-r2-002", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A large enterprise wants the installed desktop apps, cloud services, and core security and compliance features for all staff, but does NOT need E5's most advanced Defender, advanced compliance, Power BI Pro, or Teams Phone. Which enterprise plan is the appropriate mid-tier choice?",
        "options": [
            {"id": "A", "text": "Microsoft 365 E3"},
            {"id": "B", "text": "Microsoft 365 E5"},
            {"id": "C", "text": "Microsoft 365 Business Basic"},
            {"id": "D", "text": "Microsoft 365 F1"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 E3 is the mid-tier enterprise plan: desktop apps, cloud services, and core security/compliance - without E5's most advanced security, compliance, analytics, and Teams Phone additions.",
            "distractors": {
                "B": "E5 is the premium tier with the advanced capabilities this scenario explicitly does not need.",
                "C": "Business Basic is a small/medium-business web-and-mobile plan, not an enterprise plan for all staff with desktop apps.",
                "D": "F1 is an entry frontline-worker plan, not a full enterprise plan with the desktop apps.",
            },
            "exam_pattern": "Enterprise desktop apps + core security, without E5 extras = Microsoft 365 E3.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Enterprise plans (E3)"],
    },
    {
        "id": "ms900-price-r2-003", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A school district needs licensing designed for academic institutions, with plans for students and faculty (including a free entry tier). Which Microsoft 365 plan family is intended for schools and universities?",
        "options": [
            {"id": "A", "text": "Microsoft 365 Business plans"},
            {"id": "B", "text": "Microsoft 365 Education (A1, A3, A5)"},
            {"id": "C", "text": "Microsoft 365 F3"},
            {"id": "D", "text": "Office LTSC"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 Education (A1, A3, A5) is the plan family for academic institutions, with tiers for students and faculty, including a free A1 entry option.",
            "distractors": {
                "A": "Business plans target small and medium-sized businesses, not academic institutions with student/faculty licensing.",
                "C": "F3 is an enterprise frontline-worker plan, not an education-specific family.",
                "D": "Office LTSC is a perpetual apps-only edition, not an education plan family.",
            },
            "exam_pattern": "School/university licensing (A1/A3/A5) = Microsoft 365 Education.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Education plans"],
    },
    {
        "id": "ms900-price-r2-004", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 3, "type": "mcq",
        "stem": "An architect compares 'Office 365 E3' with 'Microsoft 365 E3'. Beyond the Office 365 productivity and cloud services, what does the Microsoft 365 E3 plan additionally bundle?",
        "options": [
            {"id": "A", "text": "Nothing; the two plan names are identical"},
            {"id": "B", "text": "Only a larger mailbox"},
            {"id": "C", "text": "Windows Enterprise licensing plus Enterprise Mobility + Security (Intune and Microsoft Entra)"},
            {"id": "D", "text": "A perpetual Office license"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft 365 E3 bundles Office 365 (the productivity and cloud services) together with Windows Enterprise and Enterprise Mobility + Security (Intune and Microsoft Entra), so it is a broader suite than Office 365 E3 alone.",
            "distractors": {
                "A": "They are not identical: Microsoft 365 adds Windows and security/management that Office 365 does not.",
                "B": "The difference is far more than mailbox size; it includes Windows and EMS components.",
                "D": "Microsoft 365 E3 is a subscription suite, not a perpetual Office license.",
            },
            "exam_pattern": "Microsoft 365 = Office 365 + Windows Enterprise + Enterprise Mobility + Security; Office 365 = apps/services only.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 vs Office 365 plans"],
    },
    {
        "id": "ms900-price-r2-005", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A company on Microsoft 365 E3 wants to add cloud-based phone system calling to the public telephone network for some users, which E3 does not include. Which add-on provides this enterprise calling capability?",
        "options": [
            {"id": "A", "text": "The Microsoft 365 Copilot add-on"},
            {"id": "B", "text": "Office LTSC"},
            {"id": "C", "text": "Windows 365"},
            {"id": "D", "text": "The Teams Phone add-on"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Teams Phone add-on adds cloud PBX/telephony to users (enabling PSTN calling with a calling plan), and can be licensed on top of plans like E3 that do not already include it.",
            "distractors": {
                "A": "The Microsoft 365 Copilot add-on adds AI assistance, not telephony.",
                "B": "Office LTSC is a perpetual Office edition, not a calling add-on.",
                "C": "Windows 365 provides Cloud PCs, not phone-system calling.",
            },
            "exam_pattern": "Add enterprise PSTN calling to a plan = Teams Phone add-on.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Teams Phone add-on"],
    },
    {
        "id": "ms900-price-r2-006", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "An admin is told that every employee who will use Microsoft 365 services must be individually licensed. Which statement best describes how Microsoft 365 is licensed?",
        "options": [
            {"id": "A", "text": "It uses per-user subscription licenses - each user needs their own license"},
            {"id": "B", "text": "One license covers the entire company regardless of headcount"},
            {"id": "C", "text": "Licensing is per physical device only, never per user"},
            {"id": "D", "text": "No license is required to use the services"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 uses per-user subscription licenses: each person who uses the services is assigned their own user license, which grants them the plan's apps and services.",
            "distractors": {
                "B": "A single company-wide license does not cover all users; licensing is per user.",
                "C": "Microsoft 365 is licensed per user, not strictly per device.",
                "D": "A license is required; without one, a user cannot access the services.",
            },
            "exam_pattern": "Microsoft 365 = per-user subscription licensing (one license per user).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 user subscription licenses"],
    },
    {
        "id": "ms900-price-r2-007", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 3, "type": "mcq",
        "stem": "A warehouse wants the lowest-cost frontline plan for staff who only need basic collaboration (Teams and SharePoint) on shared devices and do NOT need the web or desktop Office apps. Which plan is the entry frontline option, below F3?",
        "options": [
            {"id": "A", "text": "Microsoft 365 E5"},
            {"id": "B", "text": "Microsoft 365 F1"},
            {"id": "C", "text": "Microsoft 365 Business Premium"},
            {"id": "D", "text": "Microsoft 365 Apps for enterprise"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 F1 is the entry frontline plan focused on basic collaboration (such as Teams and SharePoint) for deskless staff; it includes read-only Office for the web and mobile apps, while F3 adds full web/mobile editing (the desktop Office apps are in neither frontline plan).",
            "distractors": {
                "A": "E5 is the premium enterprise plan - far more than entry frontline staff need, and much costlier.",
                "C": "Business Premium is an SMB plan with desktop apps and advanced security, not an entry frontline plan.",
                "D": "Microsoft 365 Apps for enterprise is just the Office apps suite, not a frontline user plan.",
            },
            "exam_pattern": "Lowest-cost frontline, basic collaboration = Microsoft 365 F1 (read-only web/mobile Office; F3 adds full editing; no desktop apps in either).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 frontline plans (F1 vs F3)"],
    },
    {
        "id": "ms900-price-r2-008", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "fill",
        "stem": "Which Microsoft 365 plan for small and medium-sized businesses includes the desktop apps and cloud services PLUS advanced security (Defender), device management (Intune), and Microsoft Entra ID P1? Enter the plan name after 'Microsoft 365' (two words).",
        "correct": ["business premium", "microsoft 365 business premium"],
        "explanation": {
            "correct": "Microsoft 365 Business Premium is the SMB plan bundling the desktop apps and cloud services with advanced security, Intune device management, and Microsoft Entra ID P1.",
            "distractors": {},
            "exam_pattern": "SMB plan with advanced security + Intune + Entra P1 = Microsoft 365 Business Premium.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Business Premium"],
    },

    # ----- ms9_billing_cost -----
    {
        "id": "ms900-price-r2-009", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 3, "type": "mcq",
        "stem": "A large organization wants licenses assigned automatically to users based on their group membership - when someone joins the 'Sales' group they receive the right license, and lose it when they leave the group. Which approach provides this automated assignment?",
        "options": [
            {"id": "A", "text": "Manually assigning each user one at a time forever"},
            {"id": "B", "text": "Shared computer activation"},
            {"id": "C", "text": "Group-based licensing"},
            {"id": "D", "text": "A retention policy"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Group-based licensing assigns licenses to a group so members automatically receive the licenses when they join and have them removed when they leave - reducing manual administration at scale.",
            "distractors": {
                "A": "Manual per-user assignment is exactly what group-based licensing automates away.",
                "B": "Shared computer activation is an Office activation feature for shared PCs, not license assignment.",
                "D": "A retention policy governs content lifecycle, not license assignment.",
            },
            "exam_pattern": "Assign licenses automatically via group membership = group-based licensing.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Group-based licensing"],
    },
    {
        "id": "ms900-price-r2-010", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a staff member who can assign and remove user licenses, but who should NOT be able to make purchases or manage invoices. Which role fits this need under least privilege?",
        "options": [
            {"id": "A", "text": "Billing Administrator"},
            {"id": "B", "text": "Global Administrator"},
            {"id": "C", "text": "Guest user"},
            {"id": "D", "text": "License Administrator"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The License Administrator role can assign and remove licenses and manage license-related settings, without the purchasing and invoice-management powers of a Billing Administrator.",
            "distractors": {
                "A": "A Billing Administrator manages purchases and invoices - which this person should not do.",
                "B": "Global Administrator has full control over everything, far beyond assigning licenses.",
                "C": "A guest user is an external collaborator with limited access, not a license manager.",
            },
            "exam_pattern": "Assign/remove licenses but not purchase = License Administrator; manage purchases/invoices = Billing Administrator.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 admin roles (License Administrator)"],
    },
    {
        "id": "ms900-price-r2-011", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "A finance team suspects the company is paying for more Microsoft 365 licenses than employees actually use. In the Microsoft 365 admin center, what is the most direct way to reduce this waste?",
        "options": [
            {"id": "A", "text": "Identify unassigned/unused licenses and stop paying for seats no one uses"},
            {"id": "B", "text": "Buy additional licenses for everyone"},
            {"id": "C", "text": "Enable a sensitivity label on all files"},
            {"id": "D", "text": "Turn off multifactor authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reviewing license usage to find unassigned or unused licenses lets an organization reduce or reclaim those seats, controlling cost - a core billing/cost-management activity in the admin center.",
            "distractors": {
                "B": "Buying more licenses increases cost; it does not reduce waste.",
                "C": "A sensitivity label protects content; it does not reduce licensing spend.",
                "D": "Disabling MFA weakens security and has nothing to do with license costs.",
            },
            "exam_pattern": "Cut licensing waste = find and reclaim unused/unassigned licenses.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Managing Microsoft 365 licenses and cost"],
    },
    {
        "id": "ms900-price-r2-012", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "When an employee leaves the company, an admin wants to make that person's Microsoft 365 license available for a new hire instead of purchasing an extra one. What should the admin do?",
        "options": [
            {"id": "A", "text": "Buy a brand-new license and leave the old one assigned"},
            {"id": "B", "text": "Unassign the license from the departing user and assign it to the new hire"},
            {"id": "C", "text": "Delete the entire tenant"},
            {"id": "D", "text": "Switch the organization to Office LTSC"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Licenses can be unassigned from a departing user and reassigned to someone else, so the organization reuses the seat rather than buying an additional license.",
            "distractors": {
                "A": "Buying a new license while leaving the old one assigned wastes money on an unused seat.",
                "C": "Deleting the tenant would remove the entire organization's Microsoft 365 environment - drastically wrong.",
                "D": "Office LTSC is a separate perpetual product and does not address reusing a subscription seat.",
            },
            "exam_pattern": "Reuse a seat when someone leaves = unassign and reassign the license.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Assign and reassign licenses"],
    },
    {
        "id": "ms900-price-r2-013", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "fill",
        "stem": "What is the term for assigning Microsoft 365 licenses to a group so that members automatically receive (and lose) the licenses based on their membership? Enter the three-word term (hyphen optional).",
        "correct": ["group-based licensing", "group based licensing"],
        "explanation": {
            "correct": "Group-based licensing assigns licenses to a group; members automatically gain or lose the licenses as their membership changes, reducing manual effort.",
            "distractors": {},
            "exam_pattern": "Automatic license assignment via group membership = group-based licensing.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Group-based licensing"],
    },

    # ----- ms9_support_sla -----
    {
        "id": "ms900-price-r2-014", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 2, "type": "mcq",
        "stem": "A company that just purchased Microsoft 365 for thousands of users wants Microsoft-provided guidance and remote assistance to help onboard, migrate data, and drive user adoption, at no extra charge for eligible subscriptions. Which Microsoft service provides this onboarding help?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "FastTrack for Microsoft 365"},
            {"id": "D", "text": "The Message center"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "FastTrack provides Microsoft-led onboarding, migration, and adoption guidance for eligible Microsoft 365 subscriptions, helping customers deploy and drive usage at no additional cost.",
            "distractors": {
                "A": "The Service Trust Portal hosts compliance/audit documents, not onboarding assistance.",
                "B": "Microsoft Secure Score measures security posture, not deployment help.",
                "D": "The Message center posts tenant change notices, not onboarding services.",
            },
            "exam_pattern": "Microsoft-led onboarding/migration/adoption help = FastTrack.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): FastTrack"],
    },
    {
        "id": "ms900-price-r2-015", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 2, "type": "mcq",
        "stem": "A total email outage is blocking all business for a large organization. When opening a support request, how does the chosen severity affect Microsoft's response for such a critical, business-stopping issue?",
        "options": [
            {"id": "A", "text": "Severity has no effect on how support responds"},
            {"id": "B", "text": "A higher severity makes Microsoft respond more slowly"},
            {"id": "C", "text": "Severity determines which Office apps are installed"},
            {"id": "D", "text": "A higher severity signals greater business impact and receives faster, around-the-clock handling"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Severity reflects business impact: critical, business-stopping issues are raised at the highest severity and receive the fastest, often 24x7 response, while lower-severity issues are handled during business hours.",
            "distractors": {
                "A": "Severity directly influences prioritization and response expectations.",
                "B": "Higher severity speeds up response, not slows it.",
                "C": "Severity relates to support prioritization, not app installation.",
            },
            "exam_pattern": "Higher severity = greater impact = faster, round-the-clock support response.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Support request severity"],
    },
    {
        "id": "ms900-price-r2-016", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 1, "type": "mcq",
        "stem": "Before opening a paid support case for a minor, non-urgent how-to question, an admin wants free self-help resources. Which of the following is an appropriate self-help option?",
        "options": [
            {"id": "A", "text": "Microsoft Learn documentation and the Microsoft Tech Community"},
            {"id": "B", "text": "Deleting the user's mailbox"},
            {"id": "C", "text": "Turning off the tenant"},
            {"id": "D", "text": "Filing a legal eDiscovery case"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Learn documentation and the Microsoft Tech Community are free self-help resources well suited to non-urgent how-to questions, before opening a support request.",
            "distractors": {
                "B": "Deleting a mailbox is a destructive action, not a self-help resource.",
                "C": "Turning off the tenant would disable the whole organization - clearly inappropriate.",
                "D": "An eDiscovery case is a legal/compliance tool, not a help resource for how-to questions.",
            },
            "exam_pattern": "Free self-help for non-urgent questions = Microsoft Learn docs and Tech Community.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Support and self-help resources"],
    },
    {
        "id": "ms900-price-r2-017", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 2, "type": "fill",
        "stem": "If Microsoft fails to meet the uptime percentage promised in its Service Level Agreement, eligible customers may be able to claim a ___ ___ as the remedy (financial compensation applied to the account). Enter the two-word term.",
        "correct": ["service credit", "service credits"],
        "explanation": {
            "correct": "When Microsoft misses the SLA's committed uptime, eligible customers may claim service credits - compensation applied to the account - as the financially backed remedy.",
            "distractors": {},
            "exam_pattern": "SLA remedy for missed uptime = service credits.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Service Level Agreement and service credits"],
    },

    # ----- ms9_lifecycle -----
    {
        "id": "ms900-price-r2-018", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Most of an organization's users should receive new Microsoft 365 features on the normal, broadly-available schedule - not early - so changes arrive after general rollout. Which release option is this default track?",
        "options": [
            {"id": "A", "text": "Targeted release"},
            {"id": "B", "text": "Standard release"},
            {"id": "C", "text": "Beta Channel"},
            {"id": "D", "text": "Office LTSC"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Standard release is the default option in which users receive new features on the normal, general-availability schedule, after broad rollout - as opposed to Targeted release, which delivers them early.",
            "distractors": {
                "A": "Targeted release delivers features early to selected users or the whole org for evaluation - not the default track.",
                "C": "Beta Channel is an unsupported preview channel for Microsoft 365 Apps, not the standard tenant release option.",
                "D": "Office LTSC is a perpetual Office edition, not a feature-release track.",
            },
            "exam_pattern": "Default, general-schedule feature rollout = Standard release; early access = Targeted release.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Release options (Standard release)"],
    },
    {
        "id": "ms900-price-r2-019", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 3, "type": "mcq",
        "stem": "An admin wants to enable Targeted release so new features can be evaluated early. Which statement correctly describes the scope options for Targeted release?",
        "options": [
            {"id": "A", "text": "It can only ever apply to a single user, never a group"},
            {"id": "B", "text": "It applies automatically to every Microsoft 365 tenant worldwide at once"},
            {"id": "C", "text": "It can be enabled for the entire organization or only for selected individual users"},
            {"id": "D", "text": "It can only be enabled for external guest users"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Targeted release can be configured for the entire organization or for a selected set of individual users, letting admins pilot new features before the Standard release reaches everyone.",
            "distractors": {
                "A": "Targeted release is not limited to one user; it can cover selected users or the whole org.",
                "B": "It is opt-in per tenant and per scope, not an automatic worldwide rollout.",
                "D": "It applies to the organization's own users, not specifically external guests.",
            },
            "exam_pattern": "Targeted release scope = entire organization OR selected users (admin opt-in for early features).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Release options (Targeted release scope)"],
    },
    {
        "id": "ms900-price-r2-020", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An IT planner needs to know the supported servicing timelines for Microsoft products and when a given product or version reaches end of support, so they can plan upgrades. Which Microsoft resource defines these support timelines?",
        "options": [
            {"id": "A", "text": "A sensitivity label"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "A calling plan"},
            {"id": "D", "text": "The Microsoft Lifecycle Policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Microsoft Lifecycle Policy provides consistent, predictable support timelines and end-of-support dates for Microsoft products, helping organizations plan updates and migrations.",
            "distractors": {
                "A": "A sensitivity label classifies and protects content, not product support timelines.",
                "B": "Microsoft Secure Score measures security posture, not lifecycle dates.",
                "C": "A calling plan enables PSTN calling, unrelated to support timelines.",
            },
            "exam_pattern": "Support timelines and end-of-support dates for products = Microsoft Lifecycle Policy.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft Lifecycle Policy"],
    },
    {
        "id": "ms900-price-r2-021", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 1, "type": "fill",
        "stem": "What is the name of the DEFAULT Microsoft 365 release option, in which users receive new features on the normal general-availability schedule rather than early? Enter the two-word term (the opposite of Targeted release).",
        "correct": ["standard release", "standard"],
        "explanation": {
            "correct": "Standard release is the default track, delivering new features on the normal general-availability schedule; Targeted release provides early access for evaluation.",
            "distractors": {},
            "exam_pattern": "Default general-schedule rollout = Standard release (early = Targeted release).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Release options"],
    },
]
