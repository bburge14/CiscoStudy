"""Microsoft 365 Fundamentals pool - Domain 1: Cloud Concepts.

Original, objective-aligned practice items for the three Cloud Concepts
subtopics tracked in CertLab:
  * ms9_cloud_benefits   - cloud service models (IaaS/PaaS/SaaS) with Microsoft
                           365 as SaaS; public/private/hybrid cloud; scalability
                           and other benefits; CapEx vs OpEx.
  * ms9_m365_vs_office   - what a Microsoft 365 subscription adds over a
                           standalone, perpetual Office purchase (cloud services,
                           continuous updates, multi-device, co-authoring); the
                           "Microsoft 365 Apps" subscription client.
  * ms9_cloud_adoption   - why organizations adopt the cloud (anywhere-access,
                           hybrid work, less owned hardware, business continuity)
                           and the considerations involved (connectivity, etc.).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased,
every wrong option carries a distractor note, and each item names the Microsoft
Learn area it draws on. Current Microsoft product names are used throughout
(Microsoft 365 for the suite; Microsoft Entra ID; Microsoft Teams). Fundamentals
depth only - no prices or numeric limits (they change), no memorized exam items.
"""

QUESTIONS = [
    # ===== ms9_cloud_benefits ===============================================
    {
        "id": "ms900-con-001", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "An organization subscribes to Microsoft 365, and Microsoft fully manages the underlying "
                "servers, infrastructure, and software updates while staff simply sign in and use the apps. "
                "Which cloud service model does Microsoft 365 represent?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "SaaS (Software as a Service)"},
            {"id": "C", "text": "PaaS (Platform as a Service)"},
            {"id": "D", "text": "On-premises software"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 is Software as a Service (SaaS): a complete, provider-managed cloud "
                       "solution delivered by subscription. Microsoft maintains the infrastructure, platform, "
                       "and application, and the customer just uses it.",
            "distractors": {
                "A": "IaaS provides raw infrastructure (VMs, storage, networking) the customer must manage, not finished software.",
                "C": "PaaS gives developers a managed platform to build apps, not a ready-to-use application suite.",
                "D": "On-premises software runs on the organization's own servers, the opposite of a managed cloud subscription.",
            },
            "exam_pattern": "Ready-to-use, provider-managed, subscription software = SaaS; Microsoft 365 is the classic SaaS example.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe cloud concepts - cloud services (SaaS)"],
    },
    {
        "id": "ms900-con-002", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A company retires its on-premises Exchange servers, which it bought outright and refreshed "
                "every few years, and moves to Exchange Online in Microsoft 365, paid per user each month. "
                "How does this change its IT spending model?",
        "options": [
            {"id": "A", "text": "From operational expenditure (OpEx) to capital expenditure (CapEx)"},
            {"id": "B", "text": "From capital expenditure (CapEx) to operational expenditure (OpEx)"},
            {"id": "C", "text": "It removes all IT costs entirely"},
            {"id": "D", "text": "From a subscription to a one-time perpetual purchase"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Buying servers is a capital expenditure (CapEx) - a large up-front purchase of owned "
                       "assets. A monthly per-user cloud subscription is an operating expenditure (OpEx) - an "
                       "ongoing, pay-as-you-go cost. Moving to Microsoft 365 shifts spend from CapEx to OpEx.",
            "distractors": {
                "A": "This reverses the direction; cloud subscriptions move spend toward OpEx, not CapEx.",
                "C": "Cloud services still cost money; it is a different spending model, not free.",
                "D": "A per-user monthly subscription is the opposite of a one-time perpetual purchase.",
            },
            "exam_pattern": "Buy-and-own hardware = CapEx; pay-as-you-go cloud subscription = OpEx.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe the benefits of cloud services (CapEx vs OpEx)"],
    },
    {
        "id": "ms900-con-003", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A business grows from 50 to 500 employees and later cuts seasonal staff. With Microsoft 365 "
                "it can add or remove user licenses on demand, without buying or decommissioning any hardware. "
                "Which cloud benefit does this illustrate?",
        "options": [
            {"id": "A", "text": "Scalability"},
            {"id": "B", "text": "Physical datacenter security"},
            {"id": "C", "text": "Perpetual licensing"},
            {"id": "D", "text": "Real-time co-authoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scalability (and elasticity) is the ability to increase or decrease resources - here, "
                       "user licenses - to match demand, without the delay and cost of provisioning your own hardware.",
            "distractors": {
                "B": "Physical datacenter security is about protecting facilities, not adjusting capacity to demand.",
                "C": "Perpetual licensing is a one-time purchase model, unrelated to scaling capacity up and down.",
                "D": "Co-authoring is real-time document collaboration, not a capacity/scaling benefit.",
            },
            "exam_pattern": "Grow or shrink capacity on demand = scalability/elasticity.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe the benefits of cloud services (scalability)"],
    },
    {
        "id": "ms900-con-004", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "After adopting Microsoft 365 as a SaaS solution, the IT team asks who applies security patches "
                "and feature updates to the Microsoft 365 applications and services. Who is responsible?",
        "options": [
            {"id": "A", "text": "The organization's end users"},
            {"id": "B", "text": "A third-party reseller"},
            {"id": "C", "text": "The organization's own IT team"},
            {"id": "D", "text": "Microsoft, the cloud provider"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "In SaaS the provider manages the application and everything beneath it, including patching "
                       "and updating. With Microsoft 365, Microsoft keeps the apps and services current automatically.",
            "distractors": {
                "A": "End users consume the apps; they do not patch cloud services.",
                "B": "A reseller may sell licenses but does not maintain or patch the service.",
                "C": "In SaaS the provider, not the customer's IT team, maintains the software (unlike on-premises).",
            },
            "exam_pattern": "In SaaS the provider patches/updates the software; Microsoft keeps Microsoft 365 always up to date.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe the benefits of cloud services (SaaS responsibilities)"],
    },
    {
        "id": "ms900-con-005", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft 365 delivers its services to many different customer organizations from "
                "Microsoft-owned datacenters over the internet, with each tenant's data logically isolated. "
                "Which cloud deployment model is this?",
        "options": [
            {"id": "A", "text": "A private cloud"},
            {"id": "B", "text": "The public cloud"},
            {"id": "C", "text": "An on-premises datacenter"},
            {"id": "D", "text": "A standalone desktop installation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The public cloud is owned and operated by a third-party provider and shared (multi-tenant) "
                       "across many organizations over the internet - exactly how Microsoft 365 is delivered.",
            "distractors": {
                "A": "A private cloud is dedicated to a single organization, not shared across many tenants.",
                "C": "An on-premises datacenter is owned and operated by the organization itself.",
                "D": "A standalone desktop installation is local software, not a cloud deployment model.",
            },
            "exam_pattern": "Provider-owned, internet-delivered, multi-tenant service = public cloud (Microsoft 365).",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe cloud concepts (public, private, hybrid)"],
    },
    {
        "id": "ms900-con-006", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_benefits", "difficulty": 1, "type": "fill",
        "stem": "Microsoft 365 is delivered as a complete, ready-to-use cloud solution in which the provider "
                "manages the infrastructure, platform, and application, and the customer subscribes and uses it. "
                "Which cloud service model is this? Enter the three-letter acronym.",
        "correct": ["saas", "software as a service"],
        "explanation": {
            "correct": "Microsoft 365 is Software as a Service (SaaS) - the provider manages everything and the "
                       "customer subscribes to and uses the software.",
            "distractors": {},
            "exam_pattern": "Fully managed, subscription-based application delivered over the internet = SaaS.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe cloud concepts (SaaS)"],
    },

    # ===== ms9_m365_vs_office ===============================================
    {
        "id": "ms900-con-007", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "A company currently uses a one-time-purchase edition of Office installed only on individual "
                "PCs. Leadership now wants always-current apps PLUS cloud email, personal cloud storage, and "
                "Microsoft Teams. Which offering adds these capabilities over standalone Office?",
        "options": [
            {"id": "A", "text": "A second copy of the standalone Office edition"},
            {"id": "B", "text": "Office for the web only"},
            {"id": "C", "text": "A Microsoft 365 subscription"},
            {"id": "D", "text": "A Windows operating-system upgrade"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A Microsoft 365 subscription bundles the Office apps with cloud services - Exchange Online "
                       "email, OneDrive storage, SharePoint, and Microsoft Teams - and keeps the apps continuously "
                       "updated, which standalone (perpetual) Office does not provide.",
            "distractors": {
                "A": "Another standalone copy still lacks cloud services and ongoing feature updates.",
                "B": "Office for the web gives browser apps but not the full bundle of mailboxes, storage, and Teams described.",
                "D": "A Windows upgrade updates the operating system, not the Office apps or cloud services.",
            },
            "exam_pattern": "Standalone Office = installed apps only; Microsoft 365 adds cloud services, multi-device, and continuous updates.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Differences between Microsoft 365 and Office"],
    },
    {
        "id": "ms900-con-008", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 1, "type": "mcq",
        "stem": "An administrator compares a perpetual-license edition of Office (bought once) with a Microsoft "
                "365 subscription. Which one continuously receives new features, not just security and quality fixes?",
        "options": [
            {"id": "A", "text": "The Microsoft 365 subscription"},
            {"id": "B", "text": "The perpetual Office license"},
            {"id": "C", "text": "Neither receives any updates"},
            {"id": "D", "text": "Both stop at the originally shipped features"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Microsoft 365 subscription delivers ongoing feature updates and improvements in addition "
                       "to security fixes. A perpetual Office license receives only security/quality fixes for its "
                       "support lifetime and stays on the feature set it shipped with.",
            "distractors": {
                "B": "A perpetual license is frozen at its original features; it does not gain new ones.",
                "C": "The subscription clearly keeps receiving new features, so 'neither' is wrong.",
                "D": "Only the perpetual license is limited to its original features; the subscription keeps evolving.",
            },
            "exam_pattern": "Subscription (Microsoft 365) = always up to date with new features; perpetual Office = security/quality fixes only.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Differences between Microsoft 365 and Office"],
    },
    {
        "id": "ms900-con-009", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "Within a Microsoft 365 subscription, what is the name for the subscription version of the Office "
                "desktop client applications (Word, Excel, PowerPoint, Outlook) that installs on PCs and Macs and "
                "stays automatically updated?",
        "options": [
            {"id": "A", "text": "Office LTSC"},
            {"id": "B", "text": "Office for the web"},
            {"id": "C", "text": "Office Mobile only"},
            {"id": "D", "text": "Microsoft 365 Apps"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "'Microsoft 365 Apps' is the subscription-delivered suite of Office desktop client "
                       "applications included with most Microsoft 365 plans; it installs locally and updates automatically.",
            "distractors": {
                "A": "Office LTSC is a separate perpetual, long-term-servicing edition, not the subscription apps.",
                "B": "Office for the web is the browser-based version, not the installed desktop suite.",
                "C": "Office Mobile refers only to phone/tablet apps, not the full installed desktop suite.",
            },
            "exam_pattern": "The subscription desktop Office suite in Microsoft 365 is called 'Microsoft 365 Apps'.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Microsoft 365 Apps"],
    },
    {
        "id": "ms900-con-010", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "Staff need to install the Office apps on several of their own devices and edit the same documents "
                "together in real time, with files saved to the cloud. Which option best meets this need?",
        "options": [
            {"id": "A", "text": "A perpetual Office license tied to a single PC"},
            {"id": "B", "text": "A Microsoft 365 subscription"},
            {"id": "C", "text": "A Windows Server license"},
            {"id": "D", "text": "An on-premises file server only"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A Microsoft 365 subscription allows installing the apps on multiple devices per user and, "
                       "by storing files in OneDrive/SharePoint, enables real-time co-authoring - capabilities a "
                       "single-PC perpetual license does not offer.",
            "distractors": {
                "A": "A perpetual license is typically tied to one device and lacks cloud co-authoring.",
                "C": "A Windows Server license is for a server operating system, not Office productivity apps.",
                "D": "An on-premises file server stores files but does not provide the apps or cloud co-authoring.",
            },
            "exam_pattern": "Multi-device install + real-time cloud co-authoring = Microsoft 365 subscription.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Differences between Microsoft 365 and Office"],
    },
    {
        "id": "ms900-con-011", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_m365_vs_office", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following is included with a Microsoft 365 subscription but NOT with a standalone, "
                "perpetual purchase of Office?",
        "options": [
            {"id": "A", "text": "The ability to type in Word while offline"},
            {"id": "B", "text": "Cloud services such as Exchange Online and OneDrive"},
            {"id": "C", "text": "A local installation of Excel"},
            {"id": "D", "text": "Saving a file to the local hard drive"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cloud services - Exchange Online mailboxes, OneDrive storage, SharePoint, and Teams - come "
                       "with Microsoft 365 but not with standalone perpetual Office, which provides only the locally "
                       "installed apps.",
            "distractors": {
                "A": "Typing offline in Word works in both the subscription and the perpetual edition.",
                "C": "Both offerings provide a local installation of Excel.",
                "D": "Saving to the local disk is possible in both offerings.",
            },
            "exam_pattern": "The cloud services (email, storage, Teams) are the key add Microsoft 365 brings over standalone Office.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Differences between Microsoft 365 and Office"],
    },

    # ===== ms9_cloud_adoption ===============================================
    {
        "id": "ms900-con-012", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 1, "type": "mcq",
        "stem": "A company shifts to hybrid work and wants employees to reach their email, files, and meetings "
                "securely from home, the office, or on the road. Which characteristic of adopting Microsoft 365 "
                "most directly supports this?",
        "options": [
            {"id": "A", "text": "Access to services from anywhere with an internet connection"},
            {"id": "B", "text": "A requirement to be on the office LAN"},
            {"id": "C", "text": "Elimination of the need for user accounts"},
            {"id": "D", "text": "Removal of all security controls"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A core driver for adopting a cloud service like Microsoft 365 is anywhere-access: because "
                       "the services are internet-delivered, users can work securely from any location and device, "
                       "enabling hybrid and remote work.",
            "distractors": {
                "B": "Requiring the office LAN is an on-premises limitation that cloud adoption removes.",
                "C": "Cloud services still require identities/user accounts to sign in securely.",
                "D": "Adopting the cloud does not remove security controls; it provides them.",
            },
            "exam_pattern": "Cloud adoption enables secure anywhere-access, a key enabler of hybrid/remote work.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Reasons to adopt cloud services"],
    },
    {
        "id": "ms900-con-013", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "mcq",
        "stem": "While planning a move to Microsoft 365, IT identifies a practical consideration: because the "
                "services are delivered over the internet, what does day-to-day access most depend on?",
        "options": [
            {"id": "A", "text": "Owning more on-premises servers"},
            {"id": "B", "text": "Buying perpetual software licenses"},
            {"id": "C", "text": "Printing all documents locally"},
            {"id": "D", "text": "Reliable internet connectivity and bandwidth"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Cloud services are reached over the internet, so dependable connectivity and adequate "
                       "bandwidth are important adoption considerations; if the internet is down, access to the "
                       "cloud services is affected.",
            "distractors": {
                "A": "Moving to the cloud reduces, not increases, the need to own servers.",
                "B": "The licensing model does not determine day-to-day connectivity.",
                "C": "Local printing is unrelated to reaching cloud services over the internet.",
            },
            "exam_pattern": "Cloud is internet-delivered, so reliable connectivity/bandwidth is a key adoption consideration.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Cloud adoption considerations"],
    },
    {
        "id": "ms900-con-014", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "multi",
        "stem": "An organization is building the business case to adopt Microsoft 365. Which TWO are commonly "
                "cited benefits of moving to this cloud service? (Choose two.)",
        "options": [
            {"id": "A", "text": "Reduced need to buy and maintain on-premises servers"},
            {"id": "B", "text": "A guarantee that no internet connection is ever required"},
            {"id": "C", "text": "Built-in business continuity, so data stays available if an office is unavailable"},
            {"id": "D", "text": "Automatic exemption from all compliance regulations"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Adopting Microsoft 365 reduces on-premises hardware and maintenance (a cost and agility "
                       "benefit) and improves business continuity, because data lives in resilient cloud datacenters "
                       "and remains reachable even if a local office is down.",
            "distractors": {
                "B": "Cloud services require internet access, so this is false.",
                "D": "Moving to the cloud does not exempt an organization from regulations; it must still meet its compliance obligations.",
            },
            "exam_pattern": "Cloud adoption wins: less owned hardware/maintenance and stronger business continuity - not freedom from internet or compliance.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Reasons to adopt cloud services"],
    },
    {
        "id": "ms900-con-015", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "mcq",
        "stem": "A small firm with a lean IT staff wants to stop racking servers, patching the email server, and "
                "planning hardware refreshes. How does adopting Microsoft 365 help with this goal?",
        "options": [
            {"id": "A", "text": "It requires hiring more datacenter staff"},
            {"id": "B", "text": "Microsoft manages the underlying infrastructure and keeps the services updated"},
            {"id": "C", "text": "It forces a company-wide hardware refresh every year"},
            {"id": "D", "text": "It shifts all patching responsibility to end users"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "With Microsoft 365 (SaaS), Microsoft runs and maintains the datacenters, servers, and "
                       "service updates, so a small IT team can focus on users and business needs instead of "
                       "infrastructure upkeep.",
            "distractors": {
                "A": "The cloud reduces datacenter staffing needs rather than increasing them.",
                "C": "There is no owned server hardware to refresh on a schedule in a SaaS model.",
                "D": "Patching the cloud services is Microsoft's responsibility, not the end users'.",
            },
            "exam_pattern": "Cloud adoption offloads infrastructure and maintenance to the provider - a key draw for small IT teams.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Reasons to adopt cloud services"],
    },
    {
        "id": "ms900-con-016", "exam": "ms900", "domain": "ms9_cloud_concepts",
        "subtopic": "ms9_cloud_adoption", "difficulty": 2, "type": "fill",
        "stem": "Paying for Microsoft 365 as an ongoing, per-user monthly or annual subscription - instead of a "
                "large up-front hardware purchase - is an example of which type of expenditure? Enter the common "
                "four-letter abbreviation (ends in 'Ex').",
        "correct": ["opex", "operating expenditure", "operational expenditure", "operating expense"],
        "explanation": {
            "correct": "An ongoing, subscription/usage-based cost is an operating expenditure (OpEx), in contrast "
                       "to a capital expenditure (CapEx), which is a large up-front purchase of owned assets.",
            "distractors": {},
            "exam_pattern": "Subscription / pay-as-you-go = OpEx; up-front owned hardware = CapEx.",
        },
        "references": ["Microsoft Learn (M365 Fundamentals): Describe the benefits of cloud services (OpEx)"],
    },
]
