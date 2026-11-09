"""Microsoft 365 Fundamentals (MS-900) pool - Domain 4: Pricing, Licensing, and Support.

Original, objective-aligned practice items for the four subtopics tracked in CertLab:
  * ms9_licensing     - Microsoft 365 Business plans (Basic / Standard / Premium)
                        vs Enterprise plans (E3 / E5 / F3 frontline); user
                        subscription licenses; add-ons (e.g. Microsoft 365 Copilot).
  * ms9_billing_cost  - the Microsoft 365 admin center for subscriptions and
                        billing, the Billing Administrator role, license assignment,
                        and monthly vs annual commitment.
  * ms9_support_sla   - service-level agreements (SLAs), service health, and
                        support requests with severity levels.
  * ms9_lifecycle     - the Message center, the Microsoft 365 roadmap, and release
                        options (Targeted release vs Standard release).

Current Microsoft product names are used throughout. Per MS-900 guidance and because
prices/limits change, items test WHICH plan or tool fits a need and the capability
each provides - not specific prices or numeric caps. build_content.py shuffles option
order by id, so the authored key is not positionally biased; every wrong option
carries a distractor note. No memorized exam items.
"""

QUESTIONS = [
    # ===== ms9_licensing ====================================================
    {
        "id": "ms900-price-001", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A growing company of about 120 employees wants the full installed desktop Office apps plus cloud "
                "services (email, Teams, OneDrive), on a per-user plan aimed at small and medium-sized businesses. "
                "Which Microsoft 365 plan best fits?",
        "options": [
            {"id": "A", "text": "Microsoft 365 F3"},
            {"id": "B", "text": "Office LTSC (perpetual)"},
            {"id": "C", "text": "Microsoft 365 Business Standard"},
            {"id": "D", "text": "Windows 365"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft 365 Business plans are designed for small and medium-sized businesses; Business "
                       "Standard includes the installed desktop apps plus cloud services such as Exchange Online, "
                       "Teams, and OneDrive.",
            "distractors": {
                "A": "F3 is an enterprise frontline-worker plan (typically web/mobile apps), not the SMB desktop-apps plan described.",
                "B": "Office LTSC is a perpetual, apps-only edition with no cloud services.",
                "D": "Windows 365 provides Cloud PCs; it is not a Microsoft 365 Office licensing plan.",
            },
            "exam_pattern": "Small/medium business + desktop apps + cloud services = Microsoft 365 Business Standard.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Business plans"],
    },
    {
        "id": "ms900-price-002", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A retailer employs many shift-based frontline workers who often share devices, do not sit at a "
                "desk, and mainly need web and mobile apps, email, and Teams at the lowest cost. Which Microsoft "
                "365 license is designed for them?",
        "options": [
            {"id": "A", "text": "Microsoft 365 F3"},
            {"id": "B", "text": "Microsoft 365 E5"},
            {"id": "C", "text": "Office LTSC"},
            {"id": "D", "text": "Microsoft Entra ID P2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 F3 is the enterprise plan tailored to frontline workers - lower-cost and "
                       "oriented to web and mobile apps plus core services - fitting shift-based, deskless staff.",
            "distractors": {
                "B": "E5 is the premium enterprise plan with advanced security, compliance, and analytics - far more than frontline staff need.",
                "C": "Office LTSC is a perpetual apps-only edition, not a frontline-worker plan.",
                "D": "Entra ID P2 is an identity add-on, not a Microsoft 365 user plan.",
            },
            "exam_pattern": "Deskless, shift-based, low-cost web/mobile = Microsoft 365 F3 (frontline).",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 frontline (F3)"],
    },
    {
        "id": "ms900-price-003", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 3, "type": "mcq",
        "stem": "A large enterprise wants the most comprehensive Microsoft 365 plan, adding advanced security "
                "(Microsoft Defender), advanced compliance, analytics (Power BI Pro), and Teams Phone beyond what "
                "the mid-tier enterprise plan offers. Which plan is this?",
        "options": [
            {"id": "A", "text": "Microsoft 365 E3"},
            {"id": "B", "text": "Microsoft 365 Business Basic"},
            {"id": "C", "text": "Office for the web"},
            {"id": "D", "text": "Microsoft 365 E5"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft 365 E5 is the top enterprise plan, adding advanced Defender security, advanced "
                       "compliance, analytics (Power BI Pro), and Teams Phone capabilities over the mid-tier E3.",
            "distractors": {
                "A": "E3 is the mid-tier enterprise plan, without E5's advanced security/compliance/analytics additions.",
                "B": "Business Basic is a small/medium-business web-and-mobile plan, not the top enterprise plan.",
                "C": "Office for the web is the browser apps, not an enterprise suite plan.",
            },
            "exam_pattern": "Top enterprise plan with advanced security/compliance/analytics = Microsoft 365 E5.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Enterprise E3 vs E5"],
    },
    {
        "id": "ms900-price-004", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A startup wants cloud email, Teams, OneDrive, and the web and mobile versions of the Office apps, "
                "but does NOT need the installed desktop applications, at the lowest Business price. Which plan fits?",
        "options": [
            {"id": "A", "text": "Microsoft 365 Business Standard"},
            {"id": "B", "text": "Microsoft 365 Business Basic"},
            {"id": "C", "text": "Microsoft 365 E5"},
            {"id": "D", "text": "Office LTSC"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 Business Basic includes cloud services (Exchange Online, Teams, OneDrive, "
                       "SharePoint) and the web and mobile Office apps, but not the installed desktop applications - "
                       "the lowest-cost Business tier.",
            "distractors": {
                "A": "Business Standard adds the installed desktop apps, which this scenario says are not needed.",
                "C": "E5 is the premium enterprise plan, far beyond this need.",
                "D": "Office LTSC is a perpetual desktop-only edition with no cloud services.",
            },
            "exam_pattern": "Cloud services + web/mobile apps, no desktop install = Microsoft 365 Business Basic.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Business Basic"],
    },
    {
        "id": "ms900-price-005", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to roll out Microsoft 365 Copilot to some users. What must each of those users "
                "already have before the Copilot add-on license can be assigned to them?",
        "options": [
            {"id": "A", "text": "An eligible base Microsoft 365 subscription license"},
            {"id": "B", "text": "Nothing; Copilot replaces the base license"},
            {"id": "C", "text": "A perpetual Office 2021 license"},
            {"id": "D", "text": "A Windows 365 Cloud PC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 Copilot is an add-on license: each user must already have an eligible base "
                       "Microsoft 365 (or Office 365) subscription, and Copilot is licensed on top of it.",
            "distractors": {
                "B": "An add-on supplements, rather than replaces, the base subscription.",
                "C": "A perpetual Office 2021 license is not an eligible base Microsoft 365 subscription for the Copilot add-on.",
                "D": "A Cloud PC is unrelated to the licensing prerequisite for Copilot.",
            },
            "exam_pattern": "Add-ons (like Microsoft 365 Copilot) require an eligible base subscription underneath.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 add-ons and Copilot licensing"],
    },
    {
        "id": "ms900-price-006", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_licensing", "difficulty": 1, "type": "fill",
        "stem": "A license such as Microsoft 365 Copilot that is purchased on top of an existing eligible "
                "subscription - rather than as a standalone plan - is known as an ___. Enter the term (one word; "
                "a hyphen is optional).",
        "correct": ["add-on", "addon", "add on"],
        "explanation": {
            "correct": "Licenses purchased on top of an eligible base plan (such as Microsoft 365 Copilot) are "
                       "called add-ons.",
            "distractors": {},
            "exam_pattern": "Licensed on top of a base plan = an add-on.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 add-ons"],
    },

    # ===== ms9_billing_cost =================================================
    {
        "id": "ms900-price-007", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 1, "type": "mcq",
        "stem": "An administrator needs one place to buy and assign licenses, add users, manage subscriptions, "
                "and view invoices for Microsoft 365. Which portal is used for these administration and billing tasks?",
        "options": [
            {"id": "A", "text": "Microsoft Teams"},
            {"id": "B", "text": "OneDrive"},
            {"id": "C", "text": "The Microsoft 365 admin center"},
            {"id": "D", "text": "The Service Trust Portal"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Microsoft 365 admin center is the central portal for managing users, subscriptions, "
                       "license assignment, and billing (including invoices) for the organization.",
            "distractors": {
                "A": "Teams is for collaboration, not subscription and billing administration.",
                "B": "OneDrive is file storage.",
                "D": "The Service Trust Portal hosts compliance reports, not billing.",
            },
            "exam_pattern": "Manage users, licenses, subscriptions, and billing = Microsoft 365 admin center.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 admin center"],
    },
    {
        "id": "ms900-price-008", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to let a finance staff member manage purchases, subscriptions, and invoices "
                "in Microsoft 365 without granting broad administrative control over users or security. Which role "
                "best follows the principle of least privilege?",
        "options": [
            {"id": "A", "text": "Billing Administrator"},
            {"id": "B", "text": "Global Administrator"},
            {"id": "C", "text": "Guest user"},
            {"id": "D", "text": "Teams owner"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Billing Administrator role can manage purchases, subscriptions, and invoices without "
                       "the broad powers of a Global Administrator, aligning with least privilege.",
            "distractors": {
                "B": "Global Administrator has full control over everything - far more access than this task requires.",
                "C": "A guest user is an external collaborator with limited access, not a billing manager.",
                "D": "A Teams owner manages a specific team, not organization-wide billing.",
            },
            "exam_pattern": "Manage billing only (least privilege) = Billing Administrator role.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 admin roles (Billing Administrator)"],
    },
    {
        "id": "ms900-price-009", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "A new employee's account exists in Microsoft Entra ID, but they cannot access Exchange Online "
                "email or Teams. What must an administrator typically do to grant access to these services?",
        "options": [
            {"id": "A", "text": "Buy new on-premises server hardware"},
            {"id": "B", "text": "Assign the user a license for a Microsoft 365 plan"},
            {"id": "C", "text": "Enroll the company in the Service Trust Portal"},
            {"id": "D", "text": "Install Office LTSC on a server"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Access to Microsoft 365 services is granted by assigning the user a license (a user "
                       "subscription license) for a plan that includes those services; without a license, the "
                       "services are unavailable.",
            "distractors": {
                "A": "No server hardware is needed for a SaaS service.",
                "C": "The Service Trust Portal provides compliance documents, not user access.",
                "D": "Installing a perpetual Office edition does not grant access to Exchange Online or Teams.",
            },
            "exam_pattern": "A user needs an assigned license to use Microsoft 365 services.",
        },
        "references": ["Microsoft Learn (MS-900): Assigning Microsoft 365 licenses"],
    },
    {
        "id": "ms900-price-010", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_billing_cost", "difficulty": 2, "type": "mcq",
        "stem": "When choosing how to pay for a Microsoft 365 subscription, an organization compares a "
                "month-to-month commitment with an annual commitment. Which statement is generally true about "
                "this choice?",
        "options": [
            {"id": "A", "text": "An annual commitment typically offers a lower per-user rate than paying month-to-month"},
            {"id": "B", "text": "Monthly billing is always free"},
            {"id": "C", "text": "An annual commitment can never be paid in monthly installments"},
            {"id": "D", "text": "The billing frequency changes which apps are included in the plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 generally offers a lower per-user price for an annual commitment than for a "
                       "flexible month-to-month plan, which trades a higher rate for more flexibility.",
            "distractors": {
                "B": "Monthly billing is not free; it is simply billed more frequently.",
                "C": "Many annual-term commitments can still be paid in monthly installments.",
                "D": "Billing frequency affects price and flexibility, not which apps the plan includes.",
            },
            "exam_pattern": "Annual commitment usually costs less per user than month-to-month flexibility.",
        },
        "references": ["Microsoft Learn (MS-900): Billing and subscription options"],
    },

    # ===== ms9_support_sla ==================================================
    {
        "id": "ms900-price-011", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft publishes a financially backed commitment that its online services will be available a "
                "certain percentage of the time, offering service credits if it falls short. What is this "
                "commitment called?",
        "options": [
            {"id": "A", "text": "A sensitivity label"},
            {"id": "B", "text": "A retention policy"},
            {"id": "C", "text": "A calling plan"},
            {"id": "D", "text": "A Service Level Agreement (SLA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A Service Level Agreement (SLA) is Microsoft's financially backed commitment to a level of "
                       "service availability (uptime); if Microsoft misses it, customers may be eligible for service credits.",
            "distractors": {
                "A": "A sensitivity label classifies and protects content, not an uptime commitment.",
                "B": "A retention policy governs content lifecycle.",
                "C": "A calling plan enables PSTN calling. None of these are availability guarantees.",
            },
            "exam_pattern": "Financially backed uptime/availability guarantee = Service Level Agreement (SLA).",
        },
        "references": ["Microsoft Learn (MS-900): Service Level Agreement"],
    },
    {
        "id": "ms900-price-012", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 1, "type": "mcq",
        "stem": "Users report that Outlook is slow, and an admin wants to confirm whether Microsoft is "
                "experiencing a service incident affecting the organization's tenant. Where should the admin look?",
        "options": [
            {"id": "A", "text": "The service health page in the Microsoft 365 admin center"},
            {"id": "B", "text": "Microsoft Forms"},
            {"id": "C", "text": "The OneDrive recycle bin"},
            {"id": "D", "text": "The Microsoft 365 roadmap"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The service health page (in the Microsoft 365 admin center) shows the current health of "
                       "Microsoft 365 services, including active incidents and advisories affecting the tenant.",
            "distractors": {
                "B": "Microsoft Forms is for surveys and quizzes.",
                "C": "The OneDrive recycle bin restores deleted files.",
                "D": "The roadmap lists upcoming features, not live service incidents.",
            },
            "exam_pattern": "Check live Microsoft 365 service incidents = service health in the admin center.",
        },
        "references": ["Microsoft Learn (MS-900): Service health and continuity"],
    },
    {
        "id": "ms900-price-013", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_support_sla", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs to open a support request with Microsoft for a Microsoft 365 problem. "
                "Where is this done, and what helps Microsoft prioritize the response?",
        "options": [
            {"id": "A", "text": "By editing a retention label"},
            {"id": "B", "text": "In the Microsoft 365 admin center, assigning a severity to the request"},
            {"id": "C", "text": "Through the certifications in the Service Trust Portal"},
            {"id": "D", "text": "By applying a sensitivity label to the mailbox"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Admins open support requests from the Microsoft 365 admin center (Help & support); the "
                       "request's severity level helps Microsoft prioritize how urgently to respond.",
            "distractors": {
                "A": "Retention labels manage content lifecycle, not support tickets.",
                "C": "The Service Trust Portal provides compliance documents, not support requests.",
                "D": "Sensitivity labels classify content, unrelated to opening support cases.",
            },
            "exam_pattern": "Open support requests in the Microsoft 365 admin center; a severity level sets priority.",
        },
        "references": ["Microsoft Learn (MS-900): Support options and severity"],
    },

    # ===== ms9_lifecycle ====================================================
    {
        "id": "ms900-price-014", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An IT admin wants advance notices about upcoming changes, new features, and planned updates that "
                "will affect their specific Microsoft 365 tenant, so they can prepare users. Where are these "
                "tenant-specific notifications posted?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal"},
            {"id": "B", "text": "Microsoft Bookings"},
            {"id": "C", "text": "The Message center"},
            {"id": "D", "text": "A sensitivity label"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Message center (in the Microsoft 365 admin center) posts notifications about upcoming "
                       "changes, new and updated features, and planned maintenance affecting the organization's tenant.",
            "distractors": {
                "A": "The Service Trust Portal hosts compliance and audit documents, not change notifications.",
                "B": "Microsoft Bookings schedules appointments.",
                "D": "A sensitivity label classifies content. None of these deliver tenant change notices.",
            },
            "exam_pattern": "Tenant-specific notices about upcoming changes/features = Message center.",
        },
        "references": ["Microsoft Learn (MS-900): Message center"],
    },
    {
        "id": "ms900-price-015", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a public view of Microsoft 365 features that are in development, rolling out, or "
                "recently launched across the service - not specific to their own tenant. Which resource provides this?",
        "options": [
            {"id": "A", "text": "The Microsoft 365 roadmap"},
            {"id": "B", "text": "The Message center"},
            {"id": "C", "text": "Microsoft Secure Score"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft 365 roadmap is a public resource listing features that are in development, "
                       "rolling out, or launched; the Message center, by contrast, is tenant-specific.",
            "distractors": {
                "B": "The Message center shows changes for your own tenant, not the public roadmap.",
                "C": "Secure Score measures security posture.",
                "D": "Conditional Access controls sign-ins. Neither lists upcoming features publicly.",
            },
            "exam_pattern": "Public, forward-looking feature list = Microsoft 365 roadmap; tenant-specific = Message center.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 roadmap"],
    },
    {
        "id": "ms900-price-016", "exam": "ms900", "domain": "ms9_pricing_support",
        "subtopic": "ms9_lifecycle", "difficulty": 2, "type": "fill",
        "stem": "To let a group of pilot users receive new Microsoft 365 features earlier than the rest of the "
                "organization (for evaluation), an admin enables ___ release. Fill in the missing word (one word; "
                "formerly called 'First Release').",
        "correct": ["targeted", "target"],
        "explanation": {
            "correct": "Targeted release (formerly First Release) lets selected users - or the whole organization "
                       "- get new features early, before the Standard release rollout.",
            "distractors": {},
            "exam_pattern": "Early feature access for pilot users = Targeted release; default broad rollout = Standard release.",
        },
        "references": ["Microsoft Learn (MS-900): Release options (Targeted vs Standard release)"],
    },
]
