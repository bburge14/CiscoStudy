"""Microsoft SC-200 pool - Domain 3: Mitigate threats with Microsoft Sentinel.

Original, objective-aligned practice items for the five Microsoft Sentinel
subtopics tracked for SC-200. Uses current naming: Microsoft Sentinel (formerly
Azure Sentinel), a cloud-native SIEM + SOAR built on a Log Analytics workspace,
now also hosted in the Microsoft Defender portal. Entra ID = formerly Azure AD.

  * sc200_sentinel_setup      - Log Analytics workspace, workspace/region design,
                                data residency, built-in RBAC roles.
  * sc200_sentinel_connectors - Content hub solutions, CEF/Syslog via AMA,
                                Defender XDR connector, service-to-service connectors.
  * sc200_sentinel_analytics  - Rule types: scheduled, NRT, Fusion, anomaly,
                                Microsoft security; entity mapping.
  * sc200_sentinel_soar       - Playbooks (Logic Apps), automation rules, triggers.
  * sc200_sentinel_incidents  - Investigation graph, UEBA, watchlists, notebooks,
                                bookmarks.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Durable capabilities only.
"""

QUESTIONS = [
    # ===== sc200_sentinel_setup ============================================
    {
        "id": "sc200-sent-001", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 1, "type": "mcq",
        "stem": "Microsoft Sentinel stores and queries its ingested data in which underlying Azure resource?",
        "options": [
            {"id": "A", "text": "An Azure Storage account"},
            {"id": "B", "text": "A Log Analytics workspace"},
            {"id": "C", "text": "An Azure SQL database"},
            {"id": "D", "text": "A Cosmos DB container"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Sentinel is enabled on top of a Log Analytics workspace, which stores the "
                       "ingested data and is queried with KQL.",
            "distractors": {
                "A": "Storage accounts hold blobs and files; Sentinel's searchable data lives in Log Analytics.",
                "C": "Azure SQL is a relational database service; Sentinel's log store is Log Analytics.",
                "D": "Cosmos DB is a NoSQL service; Sentinel uses a Log Analytics workspace.",
            },
            "exam_pattern": "Sentinel = SIEM/SOAR layered on a Log Analytics workspace (queried with KQL).",
        },
        "references": ["Microsoft Learn (SC-200): Create and configure a Microsoft Sentinel workspace"],
    },
    {
        "id": "sc200-sent-002", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "A multinational must keep European log data in an EU region for data residency while "
                "running a unified SOC. Which is a sound Microsoft Sentinel workspace design consideration?",
        "options": [
            {"id": "A", "text": "The workspace region determines where ingested data is stored, so plan workspaces/regions around residency requirements"},
            {"id": "B", "text": "Sentinel ignores region, so data can be placed anywhere without planning"},
            {"id": "C", "text": "Data residency is handled automatically by Conditional Access"},
            {"id": "D", "text": "You must deploy one workspace per user"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A workspace's region dictates where its data is stored, so residency, cost, and "
                       "access boundaries drive whether you use one or multiple workspaces.",
            "distractors": {
                "B": "Region matters: the workspace region sets where data resides, which is central to residency planning.",
                "C": "Conditional Access governs sign-in, not where logs are physically stored.",
                "D": "Workspaces are not per user; design is driven by residency, cost, and RBAC boundaries.",
            },
            "exam_pattern": "Data residency -> choose workspace region(s); design around residency/cost/RBAC, not per-user.",
        },
        "references": ["Microsoft Learn (SC-200): Design your Microsoft Sentinel workspace architecture"],
    },
    {
        "id": "sc200-sent-003", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "An analyst must triage and manage Microsoft Sentinel incidents but should NOT be able to "
                "edit analytics rules or connectors. Which built-in role best fits (least privilege)?",
        "options": [
            {"id": "A", "text": "Microsoft Sentinel Reader"},
            {"id": "B", "text": "Microsoft Sentinel Responder"},
            {"id": "C", "text": "Microsoft Sentinel Contributor"},
            {"id": "D", "text": "Owner"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Sentinel Responder adds incident management (triage, assign, change status) "
                       "on top of Reader, without rule or connector authoring - matching least privilege here.",
            "distractors": {
                "A": "Reader can view but not manage or triage incidents (change status, assign, etc.).",
                "C": "Contributor can create and edit analytics rules and more - broader than needed.",
                "D": "Owner is far more than least privilege for incident triage.",
            },
            "exam_pattern": "Triage incidents only = Responder; author rules = Contributor; view only = Reader.",
        },
        "references": ["Microsoft Learn (SC-200): Roles and permissions in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-004", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (four-letter acronym): Microsoft Sentinel is a cloud-native ______ "
                "(security information and event management) solution that also provides SOAR capabilities.",
        "correct": ["siem"],
        "explanation": {
            "correct": "Sentinel is a cloud-native SIEM (Security Information and Event Management) with "
                       "built-in SOAR (Security Orchestration, Automation, and Response).",
            "distractors": {},
            "exam_pattern": "Sentinel = SIEM + SOAR, cloud-native, on a Log Analytics workspace.",
        },
        "references": ["Microsoft Learn (SC-200): What is Microsoft Sentinel?"],
    },

    # ===== sc200_sentinel_connectors =======================================
    {
        "id": "sc200-sent-005", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 1, "type": "mcq",
        "stem": "Where in Microsoft Sentinel do you install packaged solutions that bundle a data "
                "connector with related analytics rules, workbooks, hunting queries, and playbooks?",
        "options": [
            {"id": "A", "text": "The Content hub"},
            {"id": "B", "text": "The investigation graph"},
            {"id": "C", "text": "The Secure Score page"},
            {"id": "D", "text": "Live response"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Content hub is Sentinel's centralized marketplace for solutions - packaged "
                       "connectors plus analytics rules, workbooks, hunting queries, and playbooks.",
            "distractors": {
                "B": "The investigation graph visualizes an incident's entities; it does not install solutions.",
                "C": "Secure Score is a Defender for Cloud posture metric, not a Sentinel content store.",
                "D": "Live response is a Defender for Endpoint remote shell, unrelated to Sentinel content.",
            },
            "exam_pattern": "Install packaged Sentinel content/solutions = Content hub.",
        },
        "references": ["Microsoft Learn (SC-200): Discover and manage content in the Microsoft Sentinel Content hub"],
    },
    {
        "id": "sc200-sent-006", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "An on-premises firewall forwards logs in Common Event Format (CEF). To ingest these into "
                "Microsoft Sentinel, which component collects and forwards them?",
        "options": [
            {"id": "A", "text": "A Logic App playbook"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "Microsoft Entra Connect"},
            {"id": "D", "text": "The Azure Monitor Agent (AMA) on a Linux log-forwarder"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "CEF/Syslog data is collected by the Azure Monitor Agent (AMA) running on a Linux "
                       "forwarder, which sends it into the Sentinel workspace (landing in the CommonSecurityLog table).",
            "distractors": {
                "A": "Playbooks automate responses; they are not the CEF/Syslog ingestion pipeline.",
                "B": "Watchlists are reference data you import, not a log collector.",
                "C": "Entra Connect syncs identities to Entra ID; it does not forward firewall CEF logs.",
            },
            "exam_pattern": "On-prem CEF/Syslog -> Azure Monitor Agent on a Linux forwarder -> Sentinel.",
        },
        "references": ["Microsoft Learn (SC-200): Ingest Syslog and CEF logs with the Azure Monitor Agent"],
    },
    {
        "id": "sc200-sent-007", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "A team wants Microsoft Defender XDR incidents and the underlying advanced-hunting events "
                "available in Microsoft Sentinel. Which data connector should they enable?",
        "options": [
            {"id": "A", "text": "The Syslog connector"},
            {"id": "B", "text": "The Amazon Web Services connector"},
            {"id": "C", "text": "The DNS connector"},
            {"id": "D", "text": "The Microsoft Defender XDR connector"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Microsoft Defender XDR connector streams XDR incidents and (optionally) the "
                       "underlying advanced-hunting tables into Sentinel for unified analysis.",
            "distractors": {
                "A": "Syslog ingests Linux/appliance logs, not Defender XDR incidents.",
                "B": "The AWS connector brings in AWS logs (e.g., CloudTrail), not Defender XDR.",
                "C": "The DNS connector collects DNS analytics, not Defender XDR data.",
            },
            "exam_pattern": "Bring Defender XDR incidents/events into Sentinel = the Defender XDR connector.",
        },
        "references": ["Microsoft Learn (SC-200): Connect Microsoft Defender XDR data to Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-008", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 3, "type": "mcq",
        "stem": "Which statement best describes how many first-party Microsoft cloud services (e.g., "
                "Microsoft Entra ID, Office 365) connect to Microsoft Sentinel?",
        "options": [
            {"id": "A", "text": "Only through manual CSV upload"},
            {"id": "B", "text": "As native service-to-service connectors that stream logs directly (e.g., SigninLogs, OfficeActivity)"},
            {"id": "C", "text": "Only via on-premises Syslog forwarders"},
            {"id": "D", "text": "They cannot be connected to Sentinel"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "First-party Microsoft sources connect as native service-to-service connectors, "
                       "streaming tables like SigninLogs (Entra sign-ins) and OfficeActivity directly into the workspace.",
            "distractors": {
                "A": "CSV upload is for watchlists, not streaming service logs.",
                "C": "First-party cloud services connect natively, not through on-prem Syslog forwarders.",
                "D": "They can and do connect - natively, as service-to-service connectors.",
            },
            "exam_pattern": "Microsoft cloud sources = native service-to-service connectors (no agent/forwarder needed).",
        },
        "references": ["Microsoft Learn (SC-200): Connect data sources to Microsoft Sentinel"],
    },

    # ===== sc200_sentinel_analytics ========================================
    {
        "id": "sc200-sent-009", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 1, "type": "mcq",
        "stem": "Which Microsoft Sentinel analytics rule type runs a KQL query on a schedule over a "
                "defined lookback period and is the most common, customizable detection type?",
        "options": [
            {"id": "A", "text": "Scheduled"},
            {"id": "B", "text": "Fusion"},
            {"id": "C", "text": "Microsoft security"},
            {"id": "D", "text": "Anomaly"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scheduled analytics rules run a custom KQL query at a set interval over a lookback "
                       "window - the most common and flexible detection type.",
            "distractors": {
                "B": "Fusion is a built-in multistage correlation rule, not a custom scheduled query.",
                "C": "Microsoft security rules create incidents from other Microsoft products' alerts; they do not run your KQL on a schedule.",
                "D": "Anomaly rules use built-in ML templates, not arbitrary scheduled KQL.",
            },
            "exam_pattern": "Custom KQL on an interval = scheduled analytics rule.",
        },
        "references": ["Microsoft Learn (SC-200): Create scheduled analytics rules in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-010", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "A detection must fire as close to real time as possible, running about once a minute "
                "against a single table. Which rule type fits, with the trade-off of limited query complexity (no cross-table joins)?",
        "options": [
            {"id": "A", "text": "Scheduled (every 5 minutes)"},
            {"id": "B", "text": "Near-real-time (NRT)"},
            {"id": "C", "text": "Fusion"},
            {"id": "D", "text": "Microsoft security"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "NRT rules run roughly every minute for near-real-time detection but are limited "
                       "(typically a single table, no cross-table joins) in order to achieve that speed.",
            "distractors": {
                "A": "A 5-minute scheduled rule is slower and is not the purpose-built low-latency option.",
                "C": "Fusion correlates multistage attacks via ML; it is not a per-minute single-table rule you author.",
                "D": "Microsoft security rules create incidents from imported alerts; they do not run a per-minute KQL query.",
            },
            "exam_pattern": "Lowest latency, single-table, ~1-minute cadence = NRT rule (with query limits).",
        },
        "references": ["Microsoft Learn (SC-200): Detect threats quickly with near-real-time (NRT) analytics rules"],
    },
    {
        "id": "sc200-sent-011", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Sentinel capability uses machine learning to correlate low-fidelity "
                "alerts and anomalies across the kill chain into high-fidelity multistage-attack incidents, and is enabled by default?",
        "options": [
            {"id": "A", "text": "Watchlists"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Fusion"},
            {"id": "D", "text": "Scheduled rules"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Fusion (multistage attack detection) uses ML to correlate alerts and anomalies across "
                       "the kill chain into high-fidelity incidents and is enabled by default.",
            "distractors": {
                "A": "Watchlists are reference datasets for enrichment, not a correlation engine.",
                "B": "Workbooks visualize data; they do not correlate alerts into incidents.",
                "D": "Scheduled rules detect individual patterns; Fusion correlates across many signals.",
            },
            "exam_pattern": "ML multistage correlation, on by default = Fusion.",
        },
        "references": ["Microsoft Learn (SC-200): Multistage attack detection (Fusion) in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-012", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants Microsoft Sentinel to automatically create incidents from Microsoft "
                "Defender for Cloud alerts without writing any KQL. Which analytics rule type does this?",
        "options": [
            {"id": "A", "text": "Anomaly"},
            {"id": "B", "text": "Microsoft security"},
            {"id": "C", "text": "Near-real-time (NRT)"},
            {"id": "D", "text": "Scheduled"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft security analytics rules automatically create Sentinel incidents from "
                       "alerts generated by Microsoft security products (e.g., Defender for Cloud, Defender XDR) - no KQL required.",
            "distractors": {
                "A": "Anomaly rules surface behavioral outliers via ML templates, not alert-to-incident creation from Microsoft products.",
                "C": "NRT runs custom KQL near real time; it is not the alert-import rule.",
                "D": "Scheduled rules require you to author KQL; the goal here is no KQL.",
            },
            "exam_pattern": "Turn Microsoft product alerts into Sentinel incidents with no KQL = Microsoft security rule.",
        },
        "references": ["Microsoft Learn (SC-200): Create incidents from Microsoft security alerts"],
    },
    {
        "id": "sc200-sent-013", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 3, "type": "multi",
        "stem": "Which TWO Microsoft Sentinel analytics rule types are built-in and powered by Microsoft's "
                "machine learning, so you enable them rather than authoring the detection query? (Choose two.)",
        "options": [
            {"id": "A", "text": "Fusion"},
            {"id": "B", "text": "Anomaly"},
            {"id": "C", "text": "Scheduled"},
            {"id": "D", "text": "Near-real-time (NRT)"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Fusion (multistage attack correlation) and Anomaly rules are built-in, ML-driven "
                       "templates you enable; scheduled and NRT rules require you to write the query.",
            "distractors": {
                "C": "Scheduled rules require you to author the KQL detection logic.",
                "D": "NRT rules also require you to author a (single-table) KQL query.",
            },
            "exam_pattern": "ML/built-in = Fusion & Anomaly; author-your-own KQL = scheduled & NRT.",
        },
        "references": ["Microsoft Learn (SC-200): Analytics rule types in Microsoft Sentinel"],
    },

    # ===== sc200_sentinel_soar =============================================
    {
        "id": "sc200-sent-014", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 1, "type": "mcq",
        "stem": "In Microsoft Sentinel, an automated response workflow (e.g., post to Teams, create a "
                "ticket, isolate a device) is built as a playbook. What underlying Azure service powers a playbook?",
        "options": [
            {"id": "A", "text": "Azure Logic Apps"},
            {"id": "B", "text": "Azure Functions only"},
            {"id": "C", "text": "Azure DevOps Pipelines"},
            {"id": "D", "text": "Azure Policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel playbooks are Azure Logic Apps workflows triggered by alerts, incidents, or "
                       "entities to automate response actions.",
            "distractors": {
                "B": "Functions can be called within a workflow, but a playbook itself is a Logic Apps workflow.",
                "C": "DevOps Pipelines are for CI/CD, not Sentinel response automation.",
                "D": "Azure Policy enforces resource governance, not incident-response workflows.",
            },
            "exam_pattern": "Playbook = Azure Logic App (the SOAR automation engine).",
        },
        "references": ["Microsoft Learn (SC-200): Create playbooks with Azure Logic Apps in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-015", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants every incident created by a specific analytics rule to be automatically "
                "assigned to an owner and tagged, and sometimes to run a playbook - managed centrally without "
                "rebuilding a workflow each time. Which feature provides this orchestration?",
        "options": [
            {"id": "A", "text": "Watchlists"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Hunting queries"},
            {"id": "D", "text": "Automation rules"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Automation rules centrally orchestrate incident handling - set severity/status/owner, "
                       "add tags, and call playbooks - based on conditions and order, without a custom workflow each time.",
            "distractors": {
                "A": "Watchlists store reference data; they do not orchestrate incident handling.",
                "B": "Workbooks visualize data; they do not assign owners or run playbooks.",
                "C": "Hunting queries proactively search data; they do not automate incident response.",
            },
            "exam_pattern": "Centralized, condition-based incident orchestration (assign/tag/run playbook) = automation rules; the workflow itself = playbook.",
        },
        "references": ["Microsoft Learn (SC-200): Automate incident handling with automation rules"],
    },
    {
        "id": "sc200-sent-016", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 2, "type": "mcq",
        "stem": "A playbook must automatically isolate a device the moment a high-severity incident is "
                "created in Sentinel. Which trigger should the Logic App playbook use so an automation rule can run it on new incidents?",
        "options": [
            {"id": "A", "text": "A recurrence (timer) trigger"},
            {"id": "B", "text": "An HTTP request trigger only"},
            {"id": "C", "text": "A blob-created trigger"},
            {"id": "D", "text": "The Microsoft Sentinel incident trigger"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Use the Microsoft Sentinel incident trigger so an automation rule can invoke the "
                       "playbook automatically when incidents are created or updated.",
            "distractors": {
                "A": "A recurrence trigger runs on a timer, not when an incident is created.",
                "B": "A manual HTTP trigger is not what an automation rule uses to run a playbook on incident creation.",
                "C": "A blob-created trigger fires on storage events, unrelated to Sentinel incidents.",
            },
            "exam_pattern": "Run a playbook on new incidents via an automation rule = Sentinel incident trigger (alert trigger for alert-based playbooks).",
        },
        "references": ["Microsoft Learn (SC-200): Use triggers and actions in Microsoft Sentinel playbooks"],
    },
    {
        "id": "sc200-sent-017", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank (four-letter acronym): Playbooks and automation rules give Microsoft "
                "Sentinel its ______ capability - Security Orchestration, Automation, and Response.",
        "correct": ["soar"],
        "explanation": {
            "correct": "SOAR (Security Orchestration, Automation, and Response) in Sentinel is delivered "
                       "through automation rules (orchestration) and playbooks (Logic Apps workflows).",
            "distractors": {},
            "exam_pattern": "Automation rules + playbooks = SOAR.",
        },
        "references": ["Microsoft Learn (SC-200): Security orchestration, automation, and response (SOAR) in Microsoft Sentinel"],
    },

    # ===== sc200_sentinel_incidents ========================================
    {
        "id": "sc200-sent-018", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "While investigating a Sentinel incident, an analyst wants a visual map of the related "
                "entities (users, hosts, IPs) and how they connect, to expand the blast radius interactively. Which feature provides this?",
        "options": [
            {"id": "A", "text": "The Content hub"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "The investigation graph"},
            {"id": "D", "text": "Secure Score"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The investigation graph visually maps an incident's entities and their "
                       "relationships, letting analysts expand connections to understand scope (requires entity mapping on rules).",
            "distractors": {
                "A": "The Content hub installs solutions; it is not an investigation visualization.",
                "B": "Watchlists provide reference data, not an interactive entity map.",
                "D": "Secure Score is a Defender for Cloud posture metric, unrelated to incident investigation.",
            },
            "exam_pattern": "Visual, interactive entity exploration of an incident = investigation graph.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate incidents with the Microsoft Sentinel investigation graph"],
    },
    {
        "id": "sc200-sent-019", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants Microsoft Sentinel to baseline normal user and host behavior and surface "
                "deviations (and an investigation priority) to help find compromised accounts. Which capability should they enable?",
        "options": [
            {"id": "A", "text": "User and Entity Behavior Analytics (UEBA)"},
            {"id": "B", "text": "Watchlists"},
            {"id": "C", "text": "The Content hub"},
            {"id": "D", "text": "Playbooks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "UEBA baselines entity behavior and flags anomalies (enriching entities and providing "
                       "an investigation priority), helping detect compromised accounts or insider activity.",
            "distractors": {
                "B": "Watchlists are static reference data, not behavioral baselining.",
                "C": "The Content hub installs solutions; it does not model behavior.",
                "D": "Playbooks automate responses; they do not baseline behavior.",
            },
            "exam_pattern": "Behavioral baselining/anomalies for users and entities = UEBA.",
        },
        "references": ["Microsoft Learn (SC-200): User and entity behavior analytics (UEBA) in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-020", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "An analyst wants to correlate incoming logs against a static list of high-value 'VIP' "
                "user accounts imported from a CSV, to enrich detections. Which Sentinel feature fits?",
        "options": [
            {"id": "A", "text": "An automation rule"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A workbook"},
            {"id": "D", "text": "The investigation graph"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Watchlists import reference data (e.g., a CSV of VIPs, assets, or allowed IPs) that "
                       "analytics rules and hunting queries can join against for enrichment.",
            "distractors": {
                "A": "Automation rules orchestrate incident handling; they are not an imported reference dataset.",
                "C": "Workbooks visualize data; they do not serve as a joinable reference list.",
                "D": "The investigation graph maps entities for one incident; it is not a reusable imported list.",
            },
            "exam_pattern": "Imported reference/lookup data for correlation = watchlist.",
        },
        "references": ["Microsoft Learn (SC-200): Use watchlists in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-021", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 3, "type": "multi",
        "stem": "When investigating a Microsoft Sentinel incident, which TWO features help an analyst "
                "explore and document the investigation? (Choose two.)",
        "options": [
            {"id": "A", "text": "The investigation graph (visualize related entities)"},
            {"id": "B", "text": "Bookmarks (save notable hunting findings as evidence)"},
            {"id": "C", "text": "Deleting the Log Analytics workspace"},
            {"id": "D", "text": "Disabling all analytics rules"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "The investigation graph maps related entities, and bookmarks let analysts preserve "
                       "notable query results as evidence tied to incidents.",
            "distractors": {
                "C": "Deleting the workspace destroys all data - the opposite of investigating.",
                "D": "Disabling rules stops detection and does not aid the current investigation.",
            },
            "exam_pattern": "Investigate/document in Sentinel = investigation graph + bookmarks (and comments).",
        },
        "references": ["Microsoft Learn (SC-200): Use bookmarks and the investigation graph in Microsoft Sentinel"],
    },
]
