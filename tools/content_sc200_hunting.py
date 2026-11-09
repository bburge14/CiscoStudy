"""Microsoft SC-200 pool - Domain 4: Threat Hunting and Intelligence (KQL).

Original, objective-aligned practice items for the four hunting/intelligence
subtopics tracked for SC-200. Covers Kusto Query Language (KQL), Microsoft
Defender XDR advanced hunting, custom detection rules, and threat intelligence
in Microsoft Sentinel and Microsoft Defender for Endpoint.

  * sc200_kql                - KQL operators and semantics: where, project,
                               extend, summarize, bin, join (default innerunique),
                               union, make-series, has vs contains.
  * sc200_advanced_hunting   - Advanced hunting schema/tables (DeviceProcessEvents,
                               EmailEvents, UrlClickEvents, SigninLogs, AlertEvidence)
                               and the 30-day data window.
  * sc200_custom_detections  - Turning advanced-hunting queries into scheduled
                               custom detection rules (required columns, frequency,
                               response actions).
  * sc200_threat_intel       - Indicators of compromise, TAXII and Upload
                               Indicators API connectors, TI-matching analytics
                               rules, Defender for Endpoint custom indicators.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. KQL operator semantics are
stated precisely. Durable capabilities only.
"""

QUESTIONS = [
    # ===== sc200_kql =======================================================
    {
        "id": "sc200-hunt-001", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 1, "type": "mcq",
        "stem": "In KQL, which operator filters a table to only the rows that match a condition "
                "(for example, EventID == 4625)?",
        "options": [
            {"id": "A", "text": "where"},
            {"id": "B", "text": "project"},
            {"id": "C", "text": "summarize"},
            {"id": "D", "text": "render"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "where filters a table to the rows that satisfy the predicate.",
            "distractors": {
                "B": "project selects or renames columns; it does not filter rows.",
                "C": "summarize aggregates rows into groups; it is not a row filter.",
                "D": "render chooses a chart type for the results.",
            },
            "exam_pattern": "Filter rows = where; choose columns = project; aggregate = summarize.",
        },
        "references": ["Microsoft Learn (SC-200): KQL fundamentals - the where operator"],
    },
    {
        "id": "sc200-hunt-002", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "A hunter needs to add a new calculated column (e.g., a session duration) while keeping "
                "all existing columns in the result. Which KQL operator should be used?",
        "options": [
            {"id": "A", "text": "project"},
            {"id": "B", "text": "extend"},
            {"id": "C", "text": "project-away"},
            {"id": "D", "text": "distinct"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "extend adds a new calculated column while preserving the existing columns; project "
                       "would drop any columns you do not list.",
            "distractors": {
                "A": "project returns only the columns you list (dropping the rest); it is not for adding while keeping all.",
                "C": "project-away removes columns rather than adding one.",
                "D": "distinct returns unique combinations of the specified columns.",
            },
            "exam_pattern": "Add a computed column (keep the others) = extend; select/limit columns = project.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - extend and project operators"],
    },
    {
        "id": "sc200-hunt-003", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "Which KQL expression returns the number of events per host (device)?",
        "options": [
            {"id": "A", "text": "project count() by DeviceName"},
            {"id": "B", "text": "sort by DeviceName"},
            {"id": "C", "text": "summarize count() by DeviceName"},
            {"id": "D", "text": "where count() > DeviceName"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "summarize count() by DeviceName groups rows by host and returns the per-host event count.",
            "distractors": {
                "A": "project selects/renames columns; it cannot perform a grouped aggregation with 'by'.",
                "B": "sort by orders rows; it does not count per host.",
                "D": "where filters rows; count() is an aggregation, not used like this in a predicate.",
            },
            "exam_pattern": "Aggregate per group = summarize <aggregation> by <column>.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the summarize operator"],
    },
    {
        "id": "sc200-hunt-004", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "To chart event volume in hourly buckets over time, which KQL function groups timestamps "
                "into fixed intervals within a summarize?",
        "options": [
            {"id": "A", "text": "ago()"},
            {"id": "B", "text": "bin()"},
            {"id": "C", "text": "parse()"},
            {"id": "D", "text": "toupper()"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "bin(Timestamp, 1h) rounds timestamps down into fixed buckets so summarize can "
                       "aggregate per interval (e.g., per hour) for trend charts.",
            "distractors": {
                "A": "ago() produces a time in the past relative to now (for filtering), not bucketing.",
                "C": "parse() extracts fields from a string.",
                "D": "toupper() changes string case.",
            },
            "exam_pattern": "Time-bucketing for trends = bin(Timestamp, <interval>) inside summarize.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the bin function for time series"],
    },
    {
        "id": "sc200-hunt-005", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 3, "type": "mcq",
        "stem": "An analyst joins two tables in KQL without specifying a kind (e.g., T1 | join (T2) on "
                "Key). Which join flavor is applied by default, and what is its key behavior?",
        "options": [
            {"id": "A", "text": "inner - returns all matching row combinations"},
            {"id": "B", "text": "innerunique - deduplicates the left side first, keeping one row per key"},
            {"id": "C", "text": "leftouter - keeps all left rows"},
            {"id": "D", "text": "fullouter - keeps all rows from both tables"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "KQL's default join flavor is innerunique, which removes duplicate keys from the left "
                       "(first) table before joining - so some left rows can be dropped; use kind=inner when you need every match.",
            "distractors": {
                "A": "inner returns all matches, but it must be specified explicitly; it is not the default.",
                "C": "leftouter keeps unmatched left rows but must be requested explicitly.",
                "D": "fullouter keeps unmatched rows from both sides and must be specified.",
            },
            "exam_pattern": "Unspecified KQL join = innerunique (dedups the left side); use kind=inner for all matches.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the join operator and its default flavor"],
    },
    {
        "id": "sc200-hunt-006", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "For best performance when matching a whole term (like the word 'powershell') in a large "
                "text column, which KQL string operator is preferred over contains?",
        "options": [
            {"id": "A", "text": "startswith"},
            {"id": "B", "text": "matches regex"},
            {"id": "C", "text": "contains_cs"},
            {"id": "D", "text": "has"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "has matches whole terms using the index and is faster than contains (a substring "
                       "scan) for large datasets.",
            "distractors": {
                "A": "startswith only matches at the beginning of the string.",
                "B": "matches regex is powerful but generally slower, not the term-optimized choice.",
                "C": "contains_cs is a case-sensitive substring match - still a substring scan, not term-indexed.",
            },
            "exam_pattern": "Whole-term, indexed, fast = has; substring match = contains (slower).",
        },
        "references": ["Microsoft Learn (SC-200): KQL string operators - has vs contains"],
    },
    {
        "id": "sc200-hunt-007", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "multi",
        "stem": "Which TWO KQL operators produce aggregated results (reducing many rows into summary "
                "values)? (Choose two.)",
        "options": [
            {"id": "A", "text": "summarize"},
            {"id": "B", "text": "make-series"},
            {"id": "C", "text": "where"},
            {"id": "D", "text": "project"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "summarize aggregates rows into groups (e.g., count() by host), and make-series builds "
                       "aggregated series along an axis (usually time), filling gaps - both reduce rows into summaries.",
            "distractors": {
                "C": "where filters rows but returns the same granularity - it does not aggregate.",
                "D": "project selects or renames columns; it does not aggregate rows.",
            },
            "exam_pattern": "Aggregation = summarize / make-series; row filter = where; column select = project.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - summarize and make-series"],
    },
    {
        "id": "sc200-hunt-008", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (one KQL operator): To stack the rows of two or more tables that share "
                "the same schema into a single result set, use the ______ operator.",
        "correct": ["union"],
        "explanation": {
            "correct": "union combines (stacks) the rows of two or more tables; join instead correlates rows "
                       "by matching key columns.",
            "distractors": {},
            "exam_pattern": "Stack rows from multiple tables = union; correlate by key = join.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the union operator"],
    },

    # ===== sc200_advanced_hunting ==========================================
    {
        "id": "sc200-hunt-009", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 1, "type": "mcq",
        "stem": "In Microsoft Defender XDR advanced hunting, process-creation events from onboarded "
                "devices are found in which table?",
        "options": [
            {"id": "A", "text": "SigninLogs"},
            {"id": "B", "text": "CommonSecurityLog"},
            {"id": "C", "text": "DeviceProcessEvents"},
            {"id": "D", "text": "AzureActivity"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DeviceProcessEvents contains process-creation telemetry from onboarded devices in "
                       "Defender XDR advanced hunting.",
            "distractors": {
                "A": "SigninLogs (Entra sign-ins) lives in Sentinel/Log Analytics, not the Defender device schema.",
                "B": "CommonSecurityLog holds CEF data in Sentinel, not Defender device events.",
                "D": "AzureActivity records Azure control-plane operations in Sentinel.",
            },
            "exam_pattern": "Defender XDR device telemetry = Device* tables (DeviceProcessEvents, DeviceNetworkEvents, etc.).",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting schema - DeviceProcessEvents"],
    },
    {
        "id": "sc200-hunt-010", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A hunter in Microsoft Defender XDR wants to find which users received a phishing email "
                "and whether they clicked the URL. Which pair of advanced-hunting tables is most relevant?",
        "options": [
            {"id": "A", "text": "DeviceRegistryEvents and DeviceImageLoadEvents"},
            {"id": "B", "text": "AuditLogs and AzureActivity"},
            {"id": "C", "text": "EmailEvents and UrlClickEvents"},
            {"id": "D", "text": "SecurityEvent and Syslog"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "EmailEvents shows message delivery (sender, recipient, verdict), and UrlClickEvents "
                       "records Safe Links click events - together they trace phishing receipt and clicks.",
            "distractors": {
                "A": "These are endpoint registry and image-load tables, unrelated to email delivery or URL clicks.",
                "B": "AuditLogs/AzureActivity cover directory and Azure control-plane actions, not email.",
                "D": "SecurityEvent/Syslog are Sentinel log tables, not Defender email telemetry.",
            },
            "exam_pattern": "Email delivery = EmailEvents; Safe Links clicks = UrlClickEvents.",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting - email tables (EmailEvents, UrlClickEvents)"],
    },
    {
        "id": "sc200-hunt-011", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Sentinel (Log Analytics), which table contains Microsoft Entra ID "
                "interactive sign-in events for hunting failed-logon patterns?",
        "options": [
            {"id": "A", "text": "SigninLogs"},
            {"id": "B", "text": "DeviceLogonEvents"},
            {"id": "C", "text": "SecurityAlert"},
            {"id": "D", "text": "Heartbeat"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SigninLogs holds Microsoft Entra ID interactive sign-in events in Log "
                       "Analytics/Sentinel - ideal for failed-logon and sign-in anomaly hunting.",
            "distractors": {
                "B": "DeviceLogonEvents is a Defender XDR endpoint logon table, not the Entra sign-in log in Sentinel.",
                "C": "SecurityAlert stores alerts from connected products, not raw sign-ins.",
                "D": "Heartbeat tracks agent connectivity, not sign-ins.",
            },
            "exam_pattern": "Entra sign-ins in Sentinel = SigninLogs; endpoint logons in Defender = DeviceLogonEvents.",
        },
        "references": ["Microsoft Learn (SC-200): Hunt with the SigninLogs table in Microsoft Sentinel"],
    },
    {
        "id": "sc200-hunt-012", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 3, "type": "mcq",
        "stem": "To correlate Microsoft Defender XDR alerts with the specific files, IPs, and accounts "
                "involved, which advanced-hunting table provides the per-alert evidence entities?",
        "options": [
            {"id": "A", "text": "AlertInfo"},
            {"id": "B", "text": "AlertEvidence"},
            {"id": "C", "text": "DeviceInfo"},
            {"id": "D", "text": "IdentityInfo"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AlertEvidence contains the entities (files, IPs, URLs, users, devices) tied to each "
                       "alert; join it with AlertInfo to enrich alerts with their evidence.",
            "distractors": {
                "A": "AlertInfo lists the alerts themselves (title, severity, category) but not the evidence entities.",
                "C": "DeviceInfo describes devices, not alert evidence.",
                "D": "IdentityInfo describes user accounts, not alert evidence.",
            },
            "exam_pattern": "Alert list = AlertInfo; its evidence entities = AlertEvidence (join them).",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting - AlertInfo and AlertEvidence tables"],
    },
    {
        "id": "sc200-hunt-013", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (number): Advanced hunting in Microsoft Defender XDR lets you query raw "
                "event data from the most recent ______ days.",
        "correct": ["30", "thirty"],
        "explanation": {
            "correct": "Defender XDR advanced hunting exposes the last 30 days of raw telemetry across its "
                       "schema tables.",
            "distractors": {},
            "exam_pattern": "Defender XDR advanced hunting lookback window = 30 days.",
        },
        "references": ["Microsoft Learn (SC-200): Overview of advanced hunting in Microsoft Defender XDR"],
    },

    # ===== sc200_custom_detections =========================================
    {
        "id": "sc200-hunt-014", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 2, "type": "mcq",
        "stem": "A hunter has an advanced-hunting KQL query that reliably finds a malicious pattern. To "
                "have Microsoft Defender XDR run it automatically on a schedule and raise alerts (and take actions), what should they create?",
        "options": [
            {"id": "A", "text": "A custom detection rule"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A workbook"},
            {"id": "D", "text": "A playbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A custom detection rule turns a saved advanced-hunting query into a scheduled "
                       "detection that creates alerts/incidents and can trigger response actions in Defender XDR.",
            "distractors": {
                "B": "Watchlists are reference data in Sentinel, not a scheduled Defender detection.",
                "C": "Workbooks visualize data; they do not generate alerts.",
                "D": "Playbooks automate response in Sentinel; they do not run a detection query on a schedule in Defender XDR.",
            },
            "exam_pattern": "Operationalize an advanced-hunting query into recurring alerts = custom detection rule.",
        },
        "references": ["Microsoft Learn (SC-200): Create custom detection rules in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-hunt-015", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 2, "type": "mcq",
        "stem": "When creating a Microsoft Defender XDR custom detection rule, the query must return "
                "certain columns so alerts can be generated and records identified. Which columns are required?",
        "options": [
            {"id": "A", "text": "Only DeviceName"},
            {"id": "B", "text": "SecureScore and Recommendation"},
            {"id": "C", "text": "TenantId and SubscriptionId"},
            {"id": "D", "text": "Timestamp and ReportId (plus an impacted entity such as DeviceId or AccountObjectId)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A custom detection query must return Timestamp and ReportId (and typically an "
                       "impacted entity like DeviceId or AccountObjectId) so Defender XDR can raise and track alerts.",
            "distractors": {
                "A": "DeviceName alone is insufficient; the rule needs Timestamp and ReportId to identify records.",
                "B": "Those are Defender for Cloud posture fields, not custom-detection requirements.",
                "C": "Those identify Azure scope, not detection-record columns.",
            },
            "exam_pattern": "Custom detection query must return Timestamp + ReportId (plus entity columns to act on).",
        },
        "references": ["Microsoft Learn (SC-200): Required columns for custom detection rules"],
    },
    {
        "id": "sc200-hunt-016", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 3, "type": "mcq",
        "stem": "Which run frequency for a Microsoft Defender XDR custom detection evaluates events "
                "continuously, as close to real time as possible?",
        "options": [
            {"id": "A", "text": "Every 24 hours"},
            {"id": "B", "text": "Every 3 hours"},
            {"id": "C", "text": "Continuous (NRT)"},
            {"id": "D", "text": "Every hour"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Continuous (NRT) evaluates events as they arrive for near-real-time detection; the "
                       "periodic options (every 1, 3, 12, or 24 hours) run on a schedule.",
            "distractors": {
                "A": "Every 24 hours runs once daily - the slowest option, not real time.",
                "B": "Every 3 hours is a periodic batch interval, not continuous.",
                "D": "Every hour is a periodic batch interval, not continuous.",
            },
            "exam_pattern": "Real-time custom detection = Continuous (NRT); the others are batch intervals.",
        },
        "references": ["Microsoft Learn (SC-200): Custom detection rule frequency and Continuous (NRT)"],
    },
    {
        "id": "sc200-hunt-017", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 2, "type": "mcq",
        "stem": "A custom detection rule in Defender XDR matches a malicious process on a device. Which of "
                "the following can the rule be configured to do automatically?",
        "options": [
            {"id": "A", "text": "Modify the Secure Score weighting"},
            {"id": "B", "text": "Take response actions on the impacted device, file, or user (e.g., isolate device, quarantine file)"},
            {"id": "C", "text": "Create a Sentinel watchlist"},
            {"id": "D", "text": "Edit Entra Conditional Access policies directly"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Custom detection rules can automatically apply response actions to the entities they "
                       "return - isolating devices, collecting investigation packages, quarantining files, disabling users, and so on.",
            "distractors": {
                "A": "Custom detections do not alter Secure Score weightings.",
                "C": "Watchlists are a Sentinel feature, not a custom-detection action.",
                "D": "Custom detections do not directly edit Conditional Access policies.",
            },
            "exam_pattern": "Custom detections can both alert and auto-respond on the impacted entities.",
        },
        "references": ["Microsoft Learn (SC-200): Response actions in custom detection rules"],
    },

    # ===== sc200_threat_intel ==============================================
    {
        "id": "sc200-hunt-018", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 1, "type": "mcq",
        "stem": "In threat intelligence, a known-malicious file hash, IP address, domain, or URL used to "
                "detect threats is called an indicator of ______. Which word completes this?",
        "options": [
            {"id": "A", "text": "compromise (IoC)"},
            {"id": "B", "text": "compliance"},
            {"id": "C", "text": "coverage"},
            {"id": "D", "text": "consent"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "These artifacts are indicators of compromise (IoCs) - observable evidence (hashes, "
                       "IPs, domains, URLs) that signals malicious activity.",
            "distractors": {
                "B": "Compliance relates to standards adherence, not threat artifacts.",
                "C": "Coverage describes protection breadth, not an artifact.",
                "D": "Consent relates to app permissions (OAuth), not threat indicators.",
            },
            "exam_pattern": "Hash/IP/domain/URL threat artifact = indicator of compromise (IoC).",
        },
        "references": ["Microsoft Learn (SC-200): Threat intelligence and indicators of compromise"],
    },
    {
        "id": "sc200-hunt-019", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "An organization subscribes to a threat-intel feed served over STIX/TAXII and wants those "
                "indicators in Microsoft Sentinel. Which data connector should they use?",
        "options": [
            {"id": "A", "text": "Syslog"},
            {"id": "B", "text": "Azure Activity"},
            {"id": "C", "text": "Threat Intelligence - TAXII"},
            {"id": "D", "text": "Microsoft Defender XDR"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Threat Intelligence - TAXII connector pulls STIX indicators from TAXII 2.x "
                       "servers into Sentinel's ThreatIntelligenceIndicator table.",
            "distractors": {
                "A": "Syslog ingests appliance/Linux logs, not TAXII indicator feeds.",
                "B": "Azure Activity logs control-plane operations, not threat indicators.",
                "D": "The Defender XDR connector brings XDR incidents/events, not external TAXII feeds.",
            },
            "exam_pattern": "Consume a STIX/TAXII feed in Sentinel = Threat Intelligence - TAXII connector.",
        },
        "references": ["Microsoft Learn (SC-200): Connect threat intelligence feeds with the TAXII connector"],
    },
    {
        "id": "sc200-hunt-020", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A security team maintains indicators in their own Threat Intelligence Platform (TIP) and "
                "wants to push them into Microsoft Sentinel programmatically. Which approach is intended for this?",
        "options": [
            {"id": "A", "text": "A watchlist CSV import"},
            {"id": "B", "text": "The Office 365 connector"},
            {"id": "C", "text": "Live response"},
            {"id": "D", "text": "The Threat Intelligence Upload Indicators API connector"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Threat Intelligence Upload Indicators API lets a TIP (or custom app) push STIX "
                       "indicators into Sentinel via API, landing them in the ThreatIntelligenceIndicator table.",
            "distractors": {
                "A": "A watchlist could store some data but is not the mechanism to push STIX indicators into the TI table.",
                "B": "The Office 365 connector ingests O365 audit data, not TIP indicators.",
                "C": "Live response is a Defender for Endpoint remote shell, unrelated to TI ingestion.",
            },
            "exam_pattern": "Push indicators from a TIP into Sentinel = Upload Indicators API; pull a feed = TAXII.",
        },
        "references": ["Microsoft Learn (SC-200): Connect a TIP using the Upload Indicators API"],
    },
    {
        "id": "sc200-hunt-021", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 2, "type": "multi",
        "stem": "Which TWO are valid indicator-of-compromise (IoC) types you can manage as threat "
                "indicators (for example, as Microsoft Defender for Endpoint custom indicators)? (Choose two.)",
        "options": [
            {"id": "A", "text": "A file hash (e.g., SHA-256)"},
            {"id": "B", "text": "An IP address or URL/domain"},
            {"id": "C", "text": "A Secure Score percentage"},
            {"id": "D", "text": "A KQL operator"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "IoCs include file hashes, IP addresses, URLs/domains, and certificates - Defender for "
                       "Endpoint custom indicators support these types with allow/block/alert actions.",
            "distractors": {
                "C": "Secure Score is a posture metric, not a threat indicator.",
                "D": "A KQL operator is query syntax, not an IoC.",
            },
            "exam_pattern": "IoC types = file hashes, IPs, URLs/domains, and certificates.",
        },
        "references": ["Microsoft Learn (SC-200): Manage indicators of compromise in Microsoft Defender"],
    },
    {
        "id": "sc200-hunt-022", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 3, "type": "mcq",
        "stem": "A SOC confirms a specific file hash is malicious and wants onboarded endpoints to block "
                "it immediately, tenant-wide. In Microsoft Defender for Endpoint, what should they create?",
        "options": [
            {"id": "A", "text": "An attack surface reduction (ASR) rule"},
            {"id": "B", "text": "A Safe Attachments policy"},
            {"id": "C", "text": "A Sentinel watchlist entry"},
            {"id": "D", "text": "A custom indicator (IoC) with the action set to Block"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defender for Endpoint custom indicators let you set allow/block/alert on specific "
                       "IoCs (file hashes, IPs, URLs/domains, certificates); a Block indicator on the hash stops it across onboarded devices.",
            "distractors": {
                "A": "ASR rules govern behaviors, not a specific file-hash block.",
                "B": "Safe Attachments scans email attachments; it is not an endpoint hash-block across devices.",
                "C": "A watchlist is Sentinel reference data; it does not block execution on endpoints.",
            },
            "exam_pattern": "Block a known-bad hash/IP/URL on endpoints = Defender for Endpoint custom indicator (IoC).",
        },
        "references": ["Microsoft Learn (SC-200): Create indicators for files, IPs, and URLs in Defender for Endpoint"],
    },
]
