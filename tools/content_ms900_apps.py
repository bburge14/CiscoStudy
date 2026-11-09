"""Microsoft 365 Fundamentals (MS-900) pool - Domain 2: Microsoft 365 Apps and Services.

Original, objective-aligned practice items for the five Apps and Services
subtopics tracked in CertLab (the largest MS-900 domain):
  * ms9_productivity_apps    - the core apps and services: Word/Excel/PowerPoint/
                               Outlook, Exchange Online (email), SharePoint Online
                               (sites/intranet), OneDrive (storage), Microsoft
                               Forms, Microsoft Bookings.
  * ms9_teams_collaboration  - Microsoft Teams (chat, meetings, channels, Teams
                               Phone), real-time co-authoring, and Teams as the
                               successor to the retired Skype for Business.
  * ms9_endpoint_intune      - Microsoft Intune endpoint management (MDM vs MAM),
                               Windows 365 Cloud PC, and Azure Virtual Desktop.
  * ms9_analytics_copilot    - Microsoft 365 Copilot and Copilot in the apps,
                               Microsoft Viva Insights analytics, and Microsoft
                               Graph as the connective data layer.
  * ms9_deployment_options   - Microsoft 365 Apps (Click-to-Run) vs perpetual
                               Office, update channels, and web vs desktop vs mobile.

Current Microsoft product names are used throughout (Microsoft Teams; Microsoft
Intune; Microsoft 365 Copilot; Microsoft Viva). build_content.py shuffles option
order by id, so the authored key is not positionally biased; every wrong option
carries a distractor note. Fundamentals depth only - which service/capability fits
a need - no prices, no numeric limits, and no memorized exam items.
"""

QUESTIONS = [
    # ===== ms9_productivity_apps ============================================
    {
        "id": "ms900-apps-001", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "A company wants cloud-hosted business email, calendars, and contacts for all employees, "
                "managed as part of Microsoft 365 with no on-premises mail server. Which service provides this?",
        "options": [
            {"id": "A", "text": "SharePoint Online"},
            {"id": "B", "text": "Exchange Online"},
            {"id": "C", "text": "OneDrive"},
            {"id": "D", "text": "Microsoft Forms"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Exchange Online is the cloud-hosted email, calendar, and contacts (mailbox) service in "
                       "Microsoft 365, removing the need for an on-premises Exchange server.",
            "distractors": {
                "A": "SharePoint Online hosts sites and document libraries, not mailboxes.",
                "C": "OneDrive provides personal file storage, not email/calendar.",
                "D": "Microsoft Forms creates surveys and quizzes, not email.",
            },
            "exam_pattern": "Cloud email/calendar/contacts in Microsoft 365 = Exchange Online.",
        },
        "references": ["Microsoft Learn (MS-900): Exchange Online"],
    },
    {
        "id": "ms900-apps-002", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "A department needs a shared intranet site with team pages, news, and document libraries where "
                "many colleagues store and co-manage files together. Which Microsoft 365 service is designed for this?",
        "options": [
            {"id": "A", "text": "SharePoint Online"},
            {"id": "B", "text": "Outlook"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "Exchange Online"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SharePoint Online provides team sites, intranet portals, news, and shared document "
                       "libraries for group collaboration and content management.",
            "distractors": {
                "B": "Outlook is an email and calendar client, not an intranet/site platform.",
                "C": "Microsoft Bookings schedules appointments, not intranet sites.",
                "D": "Exchange Online provides mailboxes, not collaborative sites and libraries.",
            },
            "exam_pattern": "Intranet, team sites, and shared document libraries = SharePoint Online.",
        },
        "references": ["Microsoft Learn (MS-900): SharePoint Online"],
    },
    {
        "id": "ms900-apps-003", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "Each employee needs personal cloud storage to save work files, sync them across their laptop "
                "and phone, and share individual documents with specific people. Which service fits best?",
        "options": [
            {"id": "A", "text": "A SharePoint communication site"},
            {"id": "B", "text": "Microsoft OneDrive"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Exchange Online"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "OneDrive (for work or school) gives each user personal cloud file storage that syncs "
                       "across devices and allows sharing specific files, tied to their Microsoft 365 account.",
            "distractors": {
                "A": "A SharePoint communication site is for broad team/organization content, not an individual's personal storage.",
                "C": "Microsoft Forms collects survey and quiz responses, not files.",
                "D": "Exchange Online handles email, not personal file storage and sync.",
            },
            "exam_pattern": "Personal, per-user cloud file storage and sync = OneDrive; shared team libraries = SharePoint.",
        },
        "references": ["Microsoft Learn (MS-900): OneDrive"],
    },
    {
        "id": "ms900-apps-004", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "mcq",
        "stem": "An HR team wants to send employees a quick online survey and an auto-graded training quiz, then "
                "view response charts. Which Microsoft 365 app is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft Forms"},
            {"id": "C", "text": "SharePoint Online"},
            {"id": "D", "text": "OneDrive"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Forms lets users create surveys, quizzes, and polls, collect responses, and "
                       "view real-time results and charts, with automatic grading for quizzes.",
            "distractors": {
                "A": "Microsoft Bookings manages appointment scheduling, not surveys or quizzes.",
                "C": "SharePoint hosts sites and content; it is not a dedicated survey/quiz app with auto-grading.",
                "D": "OneDrive stores files; it does not create surveys or quizzes.",
            },
            "exam_pattern": "Surveys, quizzes, and polls = Microsoft Forms.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Forms"],
    },
    {
        "id": "ms900-apps-005", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 2, "type": "mcq",
        "stem": "A clinic wants customers to self-schedule appointments online, choosing a staff member and time "
                "slot, with automatic confirmations and calendar updates. Which Microsoft 365 service provides this?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Microsoft Forms"},
            {"id": "C", "text": "Microsoft Teams"},
            {"id": "D", "text": "OneDrive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Bookings provides online appointment scheduling - a customer-facing booking "
                       "page, staff calendars, and automatic confirmations and reminders.",
            "distractors": {
                "B": "Microsoft Forms collects survey and quiz responses, not appointment bookings.",
                "C": "Teams is for chat, meetings, and calling, not a customer self-scheduling booking page.",
                "D": "OneDrive is personal file storage, unrelated to scheduling.",
            },
            "exam_pattern": "Customer self-service appointment scheduling = Microsoft Bookings.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Bookings"],
    },
    {
        "id": "ms900-apps-006", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_productivity_apps", "difficulty": 1, "type": "fill",
        "stem": "Which Microsoft 365 service hosts users' mailboxes - email, calendar, and contacts - in the "
                "cloud, replacing an on-premises mail server? Enter the service name.",
        "correct": ["exchange online", "exchange"],
        "explanation": {
            "correct": "Exchange Online is the cloud mailbox service (email, calendar, contacts) in Microsoft 365.",
            "distractors": {},
            "exam_pattern": "Cloud mailboxes in Microsoft 365 = Exchange Online.",
        },
        "references": ["Microsoft Learn (MS-900): Exchange Online"],
    },

    # ===== ms9_teams_collaboration ==========================================
    {
        "id": "ms900-apps-007", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 1, "type": "mcq",
        "stem": "Employees want a single app that combines persistent chat, online meetings with video, calling, "
                "and shared workspaces organized by project. Which Microsoft 365 service is this hub for teamwork?",
        "options": [
            {"id": "A", "text": "Outlook"},
            {"id": "B", "text": "SharePoint Online"},
            {"id": "C", "text": "Microsoft Teams"},
            {"id": "D", "text": "OneDrive"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Teams is the hub for teamwork in Microsoft 365, bringing together chat, "
                       "meetings, calling, and collaboration in teams and channels within one app.",
            "distractors": {
                "A": "Outlook handles email and calendar but is not the chat/meetings/channels hub.",
                "B": "SharePoint provides sites and libraries that Teams builds on, but is not the chat and meeting app.",
                "D": "OneDrive is personal file storage, not a teamwork hub.",
            },
            "exam_pattern": "Chat + meetings + calling + channels in one app = Microsoft Teams.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Teams"],
    },
    {
        "id": "ms900-apps-008", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "Several colleagues open the same Word document stored in the cloud and edit it at the same time, "
                "each seeing the others' changes live. What is this capability called?",
        "options": [
            {"id": "A", "text": "Co-authoring"},
            {"id": "B", "text": "Mail merge"},
            {"id": "C", "text": "Device enrollment"},
            {"id": "D", "text": "Data loss prevention"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Co-authoring lets multiple people edit the same document simultaneously in real time, "
                       "with changes visible to all; it works when files are stored in OneDrive or SharePoint.",
            "distractors": {
                "B": "Mail merge generates personalized documents from a data source, not simultaneous editing.",
                "C": "Device enrollment registers devices for management (Intune), unrelated to document editing.",
                "D": "Data loss prevention blocks oversharing of sensitive data; it is not a collaboration feature.",
            },
            "exam_pattern": "Multiple people editing one cloud document at once in real time = co-authoring.",
        },
        "references": ["Microsoft Learn (MS-900): Collaboration and co-authoring"],
    },
    {
        "id": "ms900-apps-009", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "An organization's older documentation still references 'Skype for Business' for internal "
                "meetings and instant messaging. Which current Microsoft 365 service is its replacement for "
                "meetings, chat, and calling?",
        "options": [
            {"id": "A", "text": "Microsoft Viva"},
            {"id": "B", "text": "Exchange Online"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "Microsoft Teams"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Skype for Business has been retired; Microsoft Teams is its successor for chat, meetings, "
                       "and calling in Microsoft 365.",
            "distractors": {
                "A": "Microsoft Viva is an employee experience platform, not a meetings/chat replacement.",
                "B": "Exchange Online is email and calendaring, not meetings and instant messaging.",
                "C": "Microsoft Bookings is appointment scheduling, unrelated to instant messaging and meetings.",
            },
            "exam_pattern": "Skype for Business is retired; Microsoft Teams replaced it.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Teams (Skype for Business retirement)"],
    },
    {
        "id": "ms900-apps-010", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "A company wants users to make and receive regular phone calls to external phone numbers "
                "directly inside Microsoft Teams. Which capability enables this?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Teams Phone (with a calling plan)"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "OneDrive sync"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Teams Phone adds cloud-based telephony to Teams, so users can place and receive calls to "
                       "the public telephone network (PSTN) when paired with a calling plan or equivalent connectivity.",
            "distractors": {
                "A": "Safe Links is an email/URL protection feature in Defender for Office 365, not telephony.",
                "C": "Sensitivity labels classify and protect content, unrelated to phone calling.",
                "D": "OneDrive sync keeps files current across devices, not phone calling.",
            },
            "exam_pattern": "PSTN calling inside Teams = Teams Phone.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Teams Phone"],
    },
    {
        "id": "ms900-apps-011", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_teams_collaboration", "difficulty": 2, "type": "mcq",
        "stem": "Within a team in Microsoft Teams, members want separate, persistent spaces to organize "
                "conversations, files, and apps by topic - for example 'Marketing', 'Budget', and 'Events'. "
                "What are these spaces called?",
        "options": [
            {"id": "A", "text": "Channels"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Tenants"},
            {"id": "D", "text": "Licenses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Channels are dedicated sections within a team that keep conversations, files, and apps "
                       "organized by topic, project, or department.",
            "distractors": {
                "B": "Sensitivity labels classify and protect content; they are not Teams conversation spaces.",
                "C": "A tenant is the organization's entire Microsoft 365 instance, not a topic space inside a team.",
                "D": "A license grants a user access to services; it is not a workspace within a team.",
            },
            "exam_pattern": "Topic-based, persistent sections inside a team = channels.",
        },
        "references": ["Microsoft Learn (MS-900): Teams channels"],
    },

    # ===== ms9_endpoint_intune ==============================================
    {
        "id": "ms900-apps-012", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 1, "type": "mcq",
        "stem": "An IT admin needs a cloud service to enroll, configure, and secure laptops and phones, deploy "
                "apps, and enforce compliance policies across the organization. Which Microsoft service provides "
                "this endpoint management?",
        "options": [
            {"id": "A", "text": "Microsoft Bookings"},
            {"id": "B", "text": "Exchange Online"},
            {"id": "C", "text": "Microsoft Intune"},
            {"id": "D", "text": "Microsoft Forms"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Intune is the cloud-based endpoint management service for mobile device "
                       "management (MDM) and mobile application management (MAM), used to enroll, configure, "
                       "secure, and monitor devices and apps.",
            "distractors": {
                "A": "Microsoft Bookings schedules appointments, not devices.",
                "B": "Exchange Online provides mailboxes, not device management.",
                "D": "Microsoft Forms creates surveys and quizzes, unrelated to endpoint management.",
            },
            "exam_pattern": "Cloud device and app management (MDM/MAM) = Microsoft Intune.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Intune"],
    },
    {
        "id": "ms900-apps-013", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "On corporate-owned phones, IT wants to manage the entire enrolled device - its settings, "
                "compliance state, and the ability to wipe the whole device remotely. Which management approach is this?",
        "options": [
            {"id": "A", "text": "Mobile application management (MAM)"},
            {"id": "B", "text": "Mobile device management (MDM)"},
            {"id": "C", "text": "Click-to-Run"},
            {"id": "D", "text": "Co-authoring"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mobile device management (MDM) enrolls and manages the entire device, enforcing settings "
                       "and compliance and allowing a full device wipe - appropriate for corporate-owned devices.",
            "distractors": {
                "A": "MAM manages only specific apps and their data (well suited to BYOD), not the whole device.",
                "C": "Click-to-Run is an Office installation technology, not a device-management approach.",
                "D": "Co-authoring is real-time document collaboration, unrelated to device management.",
            },
            "exam_pattern": "Manage the whole enrolled device = MDM; manage just the app and its data = MAM.",
        },
        "references": ["Microsoft Learn (MS-900): Intune MDM vs MAM"],
    },
    {
        "id": "ms900-apps-014", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "Employees use personal phones for work (BYOD). IT wants to protect and, if needed, remove only "
                "the company data in work apps, without touching the user's personal photos and apps. Which "
                "approach fits best?",
        "options": [
            {"id": "A", "text": "Mobile application management (MAM) with app protection policies"},
            {"id": "B", "text": "A full device wipe via MDM enrollment"},
            {"id": "C", "text": "Disabling the user's Microsoft 365 license"},
            {"id": "D", "text": "Installing Office LTSC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mobile application management (MAM) with app protection policies secures corporate data "
                       "inside managed apps and supports a selective wipe of only company data, making it ideal "
                       "for personal (BYOD) devices.",
            "distractors": {
                "B": "A full device wipe would also erase the user's personal data, which BYOD aims to avoid.",
                "C": "Removing a license blocks service access but does not selectively protect or wipe app data on the device.",
                "D": "Office LTSC is a perpetual Office edition, unrelated to protecting mobile app data.",
            },
            "exam_pattern": "Protect and selectively wipe only company data on personal devices = MAM app protection policies.",
        },
        "references": ["Microsoft Learn (MS-900): Intune app protection (MAM)"],
    },
    {
        "id": "ms900-apps-015", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to give each user a personal, persistent Windows desktop in the cloud that they "
                "can stream to any device, with simple, fixed per-user monthly pricing. Which service provides this?",
        "options": [
            {"id": "A", "text": "Microsoft Intune"},
            {"id": "B", "text": "SharePoint Online"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Windows 365 (Cloud PC)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Windows 365 delivers a Cloud PC - a personal, persistent Windows desktop hosted in the "
                       "cloud and streamed to any device - with simple, fixed per-user pricing.",
            "distractors": {
                "A": "Intune manages devices but does not itself provide a hosted Windows desktop.",
                "B": "SharePoint Online hosts sites and files, not virtual desktops.",
                "C": "Microsoft Forms is for surveys and quizzes, unrelated to desktops.",
            },
            "exam_pattern": "Personal, persistent, fixed-price cloud Windows desktop = Windows 365 Cloud PC.",
        },
        "references": ["Microsoft Learn (MS-900): Windows 365"],
    },
    {
        "id": "ms900-apps-016", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_endpoint_intune", "difficulty": 3, "type": "mcq",
        "stem": "An organization needs flexible, highly configurable desktop and app virtualization in Azure, "
                "including multi-session Windows and consumption-based scaling that IT manages in detail. Which "
                "service is designed for this?",
        "options": [
            {"id": "A", "text": "The fixed Windows 365 Cloud PC"},
            {"id": "B", "text": "Azure Virtual Desktop"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "OneDrive"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Virtual Desktop (AVD) provides flexible, deeply configurable desktop and app "
                       "virtualization in Azure, including multi-session Windows and consumption-based scaling that IT manages.",
            "distractors": {
                "A": "Windows 365 offers a simpler, fixed-price personal Cloud PC rather than the configurable, multi-session, consumption-based model described.",
                "C": "Microsoft Bookings is appointment scheduling, not virtualization.",
                "D": "OneDrive is file storage, not desktop virtualization.",
            },
            "exam_pattern": "Flexible, multi-session, consumption-based Azure VDI = Azure Virtual Desktop; simple fixed-price personal Cloud PC = Windows 365.",
        },
        "references": ["Microsoft Learn (MS-900): Azure Virtual Desktop vs Windows 365"],
    },

    # ===== ms9_analytics_copilot ============================================
    {
        "id": "ms900-apps-017", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 1, "type": "mcq",
        "stem": "A company wants an AI assistant built into Word, Excel, PowerPoint, Outlook, and Teams that can "
                "draft content, summarize meetings, and analyze data using the organization's own Microsoft 365 "
                "content. Which offering is this?",
        "options": [
            {"id": "A", "text": "Microsoft 365 Copilot"},
            {"id": "B", "text": "Microsoft Bookings"},
            {"id": "C", "text": "Microsoft Forms"},
            {"id": "D", "text": "Windows 365"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft 365 Copilot is the generative-AI assistant integrated across the Microsoft 365 "
                       "apps; it uses the organization's data (via Microsoft Graph) to draft, summarize, and "
                       "analyze, with enterprise data protection.",
            "distractors": {
                "B": "Microsoft Bookings handles appointment scheduling, not AI assistance.",
                "C": "Microsoft Forms creates surveys and quizzes.",
                "D": "Windows 365 provides Cloud PCs, not an in-app AI assistant.",
            },
            "exam_pattern": "Generative-AI assistant across the Microsoft 365 apps, grounded in your org data = Microsoft 365 Copilot.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Copilot"],
    },
    {
        "id": "ms900-apps-018", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft 365 Copilot and Viva Insights draw on a common layer that connects an organization's "
                "Microsoft 365 data - emails, chats, documents, calendar - through a single programmable gateway "
                "that respects each user's existing permissions. What is this layer called?",
        "options": [
            {"id": "A", "text": "Click-to-Run"},
            {"id": "B", "text": "The Microsoft 365 roadmap"},
            {"id": "C", "text": "Microsoft Graph"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Graph is the unified API and data layer that connects Microsoft 365 data and "
                       "signals; Copilot and insights experiences are grounded in it, honoring each user's existing permissions.",
            "distractors": {
                "A": "Click-to-Run is an Office install technology, not a data layer.",
                "B": "The Microsoft 365 roadmap lists upcoming features, not a data gateway.",
                "D": "Conditional Access is an identity access-control feature, not a data API.",
            },
            "exam_pattern": "The unified Microsoft 365 data/API layer that Copilot is grounded in = Microsoft Graph.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Graph"],
    },
    {
        "id": "ms900-apps-019", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "Employees and managers want data-driven insights into productivity and wellbeing - focus time, "
                "meeting habits, and after-hours work - to help build better work patterns. Which Microsoft "
                "service provides these analytics?",
        "options": [
            {"id": "A", "text": "Microsoft Viva Insights"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Exchange Online"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Viva Insights delivers personal, manager, and organizational productivity and "
                       "wellbeing analytics (with privacy protections) to help improve work patterns.",
            "distractors": {
                "B": "Intune manages devices, not productivity analytics.",
                "C": "Exchange Online provides mailboxes, not insights dashboards.",
                "D": "Microsoft Bookings schedules appointments, unrelated to analytics.",
            },
            "exam_pattern": "Productivity and wellbeing analytics = Microsoft Viva Insights (part of Microsoft Viva).",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Viva Insights"],
    },
    {
        "id": "ms900-apps-020", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_analytics_copilot", "difficulty": 2, "type": "mcq",
        "stem": "After a Teams meeting, a user wants an AI-generated recap with key points, decisions, and action "
                "items drawn from the meeting. Which capability provides this?",
        "options": [
            {"id": "A", "text": "A sensitivity label"},
            {"id": "B", "text": "Microsoft 365 Copilot in Teams"},
            {"id": "C", "text": "A retention policy"},
            {"id": "D", "text": "Click-to-Run"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft 365 Copilot in Teams can generate meeting recaps - summarizing the discussion, "
                       "decisions, and action items - as part of Copilot's in-app AI experiences.",
            "distractors": {
                "A": "A sensitivity label classifies and protects content; it does not summarize meetings.",
                "C": "A retention policy governs how long content is kept, not meeting recaps.",
                "D": "Click-to-Run installs Office apps; it does not produce AI summaries.",
            },
            "exam_pattern": "In-app AI experiences such as a Teams meeting recap come from Microsoft 365 Copilot.",
        },
        "references": ["Microsoft Learn (MS-900): Copilot in Microsoft 365 apps"],
    },

    # ===== ms9_deployment_options ===========================================
    {
        "id": "ms900-apps-021", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft 365 Apps install on PCs using a streaming technology that downloads the apps quickly "
                "and keeps them updated automatically, rather than the older Windows Installer (MSI) method. What "
                "is this technology called?",
        "options": [
            {"id": "A", "text": "Click-to-Run"},
            {"id": "B", "text": "Azure Virtual Desktop"},
            {"id": "C", "text": "Mobile application management"},
            {"id": "D", "text": "Office for the web"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Click-to-Run is the streaming install-and-update technology for Microsoft 365 Apps; it "
                       "provisions apps quickly and keeps them automatically updated.",
            "distractors": {
                "B": "Azure Virtual Desktop is desktop virtualization, not an install technology.",
                "C": "MAM protects mobile app data; it is not an Office install method.",
                "D": "Office for the web is the browser version; it is not an install technology for the desktop apps.",
            },
            "exam_pattern": "The Microsoft 365 Apps install and update technology = Click-to-Run.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Apps deployment (Click-to-Run)"],
    },
    {
        "id": "ms900-apps-022", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise wants to control how often users receive new Microsoft 365 Apps features - some "
                "pilot users getting them sooner and most users on a more predictable, less frequent cadence. "
                "Which deployment setting governs this?",
        "options": [
            {"id": "A", "text": "Sensitivity labels"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Calling plans"},
            {"id": "D", "text": "Update channels"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Update channels (for example, Current Channel, Monthly Enterprise Channel, and Semi-Annual "
                       "Enterprise Channel) control how frequently devices receive new feature updates for Microsoft 365 Apps.",
            "distractors": {
                "A": "Sensitivity labels classify and protect content, not update cadence.",
                "B": "Conditional Access controls sign-in access, not feature-update frequency.",
                "C": "Calling plans enable PSTN calling, unrelated to app updates.",
            },
            "exam_pattern": "How often users get new Microsoft 365 Apps features = update channels.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft 365 Apps update channels"],
    },
    {
        "id": "ms900-apps-023", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 1, "type": "mcq",
        "stem": "A contractor on a locked-down device that cannot install software still needs to view and lightly "
                "edit Word and Excel files in a browser. Which option meets this need without any installation?",
        "options": [
            {"id": "A", "text": "Office for the web"},
            {"id": "B", "text": "A full Click-to-Run installation"},
            {"id": "C", "text": "Windows 365 enrollment"},
            {"id": "D", "text": "Microsoft Intune"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Office for the web provides browser-based versions of Word, Excel, PowerPoint, and more, "
                       "so users can view and edit documents without installing anything locally.",
            "distractors": {
                "B": "A Click-to-Run installation is exactly what the scenario rules out.",
                "C": "Windows 365 provides a full Cloud PC, a heavier solution than simply editing in a browser.",
                "D": "Intune manages devices; it is not a way to edit documents in a browser.",
            },
            "exam_pattern": "Edit documents in a browser with no install = Office for the web.",
        },
        "references": ["Microsoft Learn (MS-900): Office for the web"],
    },
    {
        "id": "ms900-apps-024", "exam": "ms900", "domain": "ms9_apps_services",
        "subtopic": "ms9_deployment_options", "difficulty": 1, "type": "fill",
        "stem": "Name the streaming technology used to install and automatically update Microsoft 365 Apps on "
                "Windows PCs (the hyphenated three-word name; spacing is ignored).",
        "correct": ["click-to-run", "click to run", "clicktorun"],
        "explanation": {
            "correct": "Click-to-Run is the streaming technology that installs and keeps Microsoft 365 Apps updated.",
            "distractors": {},
            "exam_pattern": "The Microsoft 365 Apps install/update technology = Click-to-Run.",
        },
        "references": ["Microsoft Learn (MS-900): Click-to-Run"],
    },
]
