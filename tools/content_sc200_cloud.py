"""Microsoft SC-200 pool - Domain 2: Mitigate threats with Microsoft Defender for Cloud.

Original, objective-aligned practice items for the three Defender for Cloud
subtopics tracked for SC-200. Uses current naming: Microsoft Defender for Cloud
(formerly Azure Security Center / Azure Defender), a CNAPP combining cloud
security posture management (CSPM) with workload protection (CWPP).

  * sc200_dfc_posture   - Secure Score, foundational (free) CSPM vs Defender CSPM,
                          Microsoft Cloud Security Benchmark (MCSB), regulatory
                          compliance, recommendations, multicloud (AWS/GCP).
  * sc200_dfc_workloads - Workload protection plans: Defender for Servers,
                          Storage, Databases/SQL, Containers, Key Vault; JIT VM access.
  * sc200_dfc_alerts    - Security alerts vs recommendations, MITRE ATT&CK intent,
                          export to Sentinel, workflow automation, suppression, triage.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Durable capabilities only.
"""

QUESTIONS = [
    # ===== sc200_dfc_posture ===============================================
    {
        "id": "sc200-dfc-001", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 1, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, which single metric aggregates your security "
                "recommendations into a percentage that rises as you remediate them, helping prioritize posture work?",
        "options": [
            {"id": "A", "text": "Secure Score"},
            {"id": "B", "text": "Just-in-time VM access coverage"},
            {"id": "C", "text": "Workload protection coverage"},
            {"id": "D", "text": "Regulatory compliance percentage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secure Score aggregates Defender for Cloud's security recommendations into a "
                       "percentage; remediating recommendations raises it and reduces risk.",
            "distractors": {
                "B": "JIT VM access reduces exposure of management ports; it is one control, not the aggregate posture metric.",
                "C": "Workload protection coverage shows which Defender plans are enabled, not a remediation score.",
                "D": "The regulatory compliance view maps to standards; Secure Score is the overall recommendation-driven posture metric.",
            },
            "exam_pattern": "Aggregate, remediation-driven posture percentage = Secure Score.",
        },
        "references": ["Microsoft Learn (SC-200): Secure Score in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-002", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "Which capability of Microsoft Defender for Cloud is available free on all Azure "
                "subscriptions and provides security recommendations, Secure Score, and asset inventory?",
        "options": [
            {"id": "A", "text": "Defender for Servers Plan 2"},
            {"id": "B", "text": "Foundational (free) Cloud Security Posture Management (CSPM)"},
            {"id": "C", "text": "Defender CSPM (paid)"},
            {"id": "D", "text": "Microsoft Sentinel"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Foundational CSPM is free on Azure subscriptions and includes security "
                       "recommendations, Secure Score, asset inventory, and data export.",
            "distractors": {
                "A": "Defender for Servers is a paid workload-protection plan, not the free posture tier.",
                "C": "Defender CSPM is the paid plan that adds attack path analysis, agentless scanning, and risk prioritization.",
                "D": "Sentinel is a separate SIEM/SOAR service, not Defender for Cloud's free posture tier.",
            },
            "exam_pattern": "Free posture (recommendations/Secure Score/inventory) = Foundational CSPM; advanced posture = Defender CSPM (paid).",
        },
        "references": ["Microsoft Learn (SC-200): Cloud security posture management (CSPM) in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-003", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 3, "type": "mcq",
        "stem": "A security architect wants to see 'attack paths' - chains of exploitable weaknesses an "
                "attacker could use to reach a crown-jewel resource - and query relationships across cloud "
                "assets. Which plan provides attack path analysis and the cloud security explorer?",
        "options": [
            {"id": "A", "text": "Foundational CSPM (free)"},
            {"id": "B", "text": "Defender for Key Vault"},
            {"id": "C", "text": "Defender CSPM (paid)"},
            {"id": "D", "text": "Microsoft Entra ID Protection"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Defender CSPM (paid) adds attack path analysis, the cloud security explorer (graph "
                       "queries over your cloud assets), agentless scanning, and risk prioritization.",
            "distractors": {
                "A": "The free tier provides recommendations and Secure Score but not attack path analysis or the security explorer.",
                "B": "Defender for Key Vault protects Key Vault access; it is not a posture-graph feature.",
                "D": "Entra ID Protection detects identity risk in the cloud directory, not cloud-resource attack paths.",
            },
            "exam_pattern": "Attack paths + cloud security explorer (graph) = Defender CSPM (paid).",
        },
        "references": ["Microsoft Learn (SC-200): Identify risks with attack path analysis and cloud security explorer"],
    },
    {
        "id": "sc200-dfc-004", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "By default, Microsoft Defender for Cloud assesses your environment against a built-in "
                "benchmark shown in the Regulatory compliance dashboard. Which standard is applied by default?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "HIPAA/HITRUST"},
            {"id": "C", "text": "ISO/IEC 27001 only"},
            {"id": "D", "text": "The Microsoft Cloud Security Benchmark (MCSB)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The Microsoft Cloud Security Benchmark (MCSB) is assigned by default; other standards "
                       "can be added to the Regulatory compliance dashboard.",
            "distractors": {
                "A": "PCI DSS can be added to the dashboard, but it is not the default initiative.",
                "B": "HIPAA/HITRUST is an optional standard you can add, not the default.",
                "C": "ISO 27001 is selectable, but the default applied initiative is the MCSB.",
            },
            "exam_pattern": "Default compliance initiative in Defender for Cloud = MCSB; others (PCI DSS, ISO, NIST) are add-ons.",
        },
        "references": ["Microsoft Learn (SC-200): Regulatory compliance and the Microsoft Cloud Security Benchmark"],
    },
    {
        "id": "sc200-dfc-005", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "A recommendation in Defender for Cloud reads 'Management ports of virtual machines should "
                "be protected with just-in-time network access control.' What is the primary purpose of acting on it?",
        "options": [
            {"id": "A", "text": "To increase the volume of ingested logs"},
            {"id": "B", "text": "To enable Microsoft Sentinel"},
            {"id": "C", "text": "To create a custom analytics rule"},
            {"id": "D", "text": "To reduce the attack surface and raise Secure Score"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Recommendations identify misconfigurations; remediating them (e.g., enabling JIT) "
                       "reduces the attack surface and increases Secure Score.",
            "distractors": {
                "A": "Remediation hardens configuration; it is not about increasing log volume.",
                "B": "Sentinel is enabled separately; a VM hardening recommendation does not turn it on.",
                "C": "Analytics rules are a Sentinel construct; this is a Defender for Cloud posture recommendation.",
            },
            "exam_pattern": "Recommendations = hardening actions that raise Secure Score and cut risk.",
        },
        "references": ["Microsoft Learn (SC-200): Remediate security recommendations in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-006", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (acronym): In Microsoft Defender for Cloud, the posture-management "
                "discipline that continuously assesses cloud resources for misconfigurations and drives "
                "Secure Score is abbreviated ______ (four letters).",
        "correct": ["cspm", "cloud security posture management"],
        "explanation": {
            "correct": "CSPM (Cloud Security Posture Management) continuously assesses resources, surfaces "
                       "recommendations, and drives Secure Score; CWPP (workload protection) is the complementary half of the CNAPP.",
            "distractors": {},
            "exam_pattern": "Posture / misconfiguration / recommendations = CSPM; threat protection for workloads = CWPP.",
        },
        "references": ["Microsoft Learn (SC-200): What is cloud security posture management (CSPM)?"],
    },
    {
        "id": "sc200-dfc-007", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 3, "type": "multi",
        "stem": "An enterprise runs workloads in Azure, AWS, and GCP and wants unified posture "
                "management. Which TWO statements about Microsoft Defender for Cloud are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "It can connect AWS and GCP accounts for multicloud posture and recommendations"},
            {"id": "B", "text": "It supports Azure resources only"},
            {"id": "C", "text": "Secure Score and recommendations extend to the connected AWS/GCP resources"},
            {"id": "D", "text": "Connecting AWS/GCP requires first migrating those workloads to Azure"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Defender for Cloud connects AWS and GCP via native cloud connectors, extending "
                       "recommendations and Secure Score across all three clouds as a CNAPP.",
            "distractors": {
                "B": "Defender for Cloud is multicloud; it supports AWS and GCP via connectors, not Azure only.",
                "D": "No migration is needed; a cloud connector brings AWS/GCP resources into scope where they run.",
            },
            "exam_pattern": "Defender for Cloud is multicloud (Azure + AWS + GCP) through connectors; no migration required.",
        },
        "references": ["Microsoft Learn (SC-200): Connect AWS and GCP accounts to Microsoft Defender for Cloud"],
    },

    # ===== sc200_dfc_workloads =============================================
    {
        "id": "sc200-dfc-008", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 1, "type": "mcq",
        "stem": "Beyond free posture management, Defender for Cloud offers paid plans that provide threat "
                "detection and alerts for specific resource types (servers, storage, SQL, etc.). What are these collectively called?",
        "options": [
            {"id": "A", "text": "Analytics rules"},
            {"id": "B", "text": "Workload protection plans (the CWPP capability)"},
            {"id": "C", "text": "Conditional Access policies"},
            {"id": "D", "text": "Automation rules"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The paid Defender plans form the cloud workload protection platform (CWPP) - "
                       "resource-specific threat detection for servers, storage, databases, containers, Key Vault, and more.",
            "distractors": {
                "A": "Analytics rules are a Microsoft Sentinel detection construct, not Defender for Cloud plans.",
                "C": "Conditional Access governs identity sign-in in Entra ID.",
                "D": "Automation rules orchestrate incident handling in Sentinel.",
            },
            "exam_pattern": "Paid, resource-specific threat protection = CWPP (workload protection plans).",
        },
        "references": ["Microsoft Learn (SC-200): Workload protections in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-009", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "Which Defender for Cloud plan protects Windows and Linux machines - integrating Microsoft "
                "Defender for Endpoint, just-in-time VM access, and vulnerability assessment?",
        "options": [
            {"id": "A", "text": "Defender for Storage"},
            {"id": "B", "text": "Defender for Servers"},
            {"id": "C", "text": "Defender for Key Vault"},
            {"id": "D", "text": "Defender for Resource Manager"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defender for Servers protects VMs/machines, integrates Defender for Endpoint, and "
                       "provides JIT VM access and vulnerability assessment (Plan 2 adds the full capability set).",
            "distractors": {
                "A": "Defender for Storage protects storage accounts (malware scanning, sensitive-data detection), not VMs.",
                "C": "Defender for Key Vault detects abnormal Key Vault access, not server protection.",
                "D": "Defender for Resource Manager monitors control-plane (ARM) operations, not guest machines.",
            },
            "exam_pattern": "VM/server threat protection + Defender for Endpoint + JIT = Defender for Servers.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Servers"],
    },
    {
        "id": "sc200-dfc-010", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to detect malware uploaded to Azure Blob Storage and alert on anomalous "
                "access to storage accounts. Which plan should be enabled?",
        "options": [
            {"id": "A", "text": "Defender for Containers"},
            {"id": "B", "text": "Defender for App Service"},
            {"id": "C", "text": "Defender for Storage"},
            {"id": "D", "text": "Defender CSPM"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Defender for Storage adds malware scanning of uploaded blobs, sensitive-data threat "
                       "detection, and alerts on unusual or malicious access (including SAS-token misuse).",
            "distractors": {
                "A": "Defender for Containers protects Kubernetes/container workloads, not blob storage.",
                "B": "Defender for App Service protects web apps running on App Service.",
                "D": "Defender CSPM is posture management; it does not provide storage malware scanning or access-anomaly alerts.",
            },
            "exam_pattern": "Blob malware scanning + storage access anomalies = Defender for Storage.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Storage"],
    },
    {
        "id": "sc200-dfc-011", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "Which Defender for Cloud plan provides Kubernetes environment hardening, container image "
                "vulnerability assessment, and runtime threat detection?",
        "options": [
            {"id": "A", "text": "Defender for Databases"},
            {"id": "B", "text": "Defender for DNS"},
            {"id": "C", "text": "Defender for Servers Plan 1"},
            {"id": "D", "text": "Defender for Containers"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defender for Containers covers cluster hardening, image vulnerability scanning "
                       "(registry and running images), and runtime threat detection for Kubernetes.",
            "distractors": {
                "A": "Defender for Databases protects SQL / open-source databases and Cosmos DB, not containers.",
                "B": "Defender for DNS monitored DNS-layer threats and has since been consolidated; it is not the container runtime plan.",
                "C": "Defender for Servers Plan 1 focuses on machines via Defender for Endpoint, not Kubernetes hardening/runtime.",
            },
            "exam_pattern": "Kubernetes hardening + image scanning + runtime detection = Defender for Containers.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Containers"],
    },
    {
        "id": "sc200-dfc-012", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "An analyst needs alerts for SQL injection attempts and anomalous database access on Azure "
                "SQL Database. Which plan provides this?",
        "options": [
            {"id": "A", "text": "Defender for Key Vault"},
            {"id": "B", "text": "Defender for Databases (Defender for SQL)"},
            {"id": "C", "text": "Foundational CSPM"},
            {"id": "D", "text": "Defender for Resource Manager"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defender for Databases / Defender for SQL detects threats such as SQL injection and "
                       "anomalous database access patterns on Azure SQL and other supported database types.",
            "distractors": {
                "A": "Defender for Key Vault watches secret and key access, not SQL queries.",
                "C": "Foundational CSPM gives posture recommendations, not runtime SQL threat alerts.",
                "D": "Defender for Resource Manager detects suspicious ARM (control-plane) operations.",
            },
            "exam_pattern": "SQL injection / database access anomalies = Defender for Databases (Defender for SQL).",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Databases"],
    },
    {
        "id": "sc200-dfc-013", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "Defender for Cloud raises an alert that an unusual application accessed a large number of "
                "secrets from an Azure Key Vault. Which plan generated this alert?",
        "options": [
            {"id": "A", "text": "Defender for Storage"},
            {"id": "B", "text": "Defender for Containers"},
            {"id": "C", "text": "Defender for Key Vault"},
            {"id": "D", "text": "Defender for App Service"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Defender for Key Vault detects unusual or potentially malicious attempts to access or "
                       "exploit Key Vaults (e.g., anomalous secret access by an unfamiliar identity).",
            "distractors": {
                "A": "Defender for Storage covers storage accounts, not Key Vault.",
                "B": "Defender for Containers covers Kubernetes, not Key Vault access.",
                "D": "Defender for App Service covers web apps, not Key Vault secret access.",
            },
            "exam_pattern": "Abnormal Key Vault secret/key access = Defender for Key Vault.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Key Vault"],
    },
    {
        "id": "sc200-dfc-014", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank (hyphenated term): To minimize exposure of VM management ports "
                "(RDP/SSH) while still allowing on-demand admin access, Defender for Servers provides "
                "______-______-______ VM access, which opens the port only for an approved time window.",
        "correct": ["just-in-time", "just in time", "jit"],
        "explanation": {
            "correct": "Just-in-time (JIT) VM access keeps management ports closed by default and opens them "
                       "only for an approved user, source IP, and time window - shrinking the attack surface.",
            "distractors": {},
            "exam_pattern": "On-demand, time-boxed opening of VM management ports = just-in-time (JIT) VM access.",
        },
        "references": ["Microsoft Learn (SC-200): Just-in-time virtual machine access"],
    },

    # ===== sc200_dfc_alerts ================================================
    {
        "id": "sc200-dfc-015", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 1, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, what is the key difference between a 'recommendation' "
                "and a 'security alert'?",
        "options": [
            {"id": "A", "text": "They are the same thing with different names"},
            {"id": "B", "text": "A recommendation indicates an active attack; an alert is a hardening tip"},
            {"id": "C", "text": "A recommendation is a posture/hardening suggestion; an alert indicates a detected active threat"},
            {"id": "D", "text": "Only alerts affect Secure Score"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Recommendations are proactive hardening actions (and drive Secure Score); security "
                       "alerts are reactive notifications that Defender detected suspicious or malicious activity on a resource.",
            "distractors": {
                "A": "They are distinct: posture guidance versus threat detection.",
                "B": "This reverses the definitions - recommendations are proactive, alerts signal detected activity.",
                "D": "Recommendations (not alerts) drive Secure Score, so this statement is incorrect.",
            },
            "exam_pattern": "Recommendation = fix posture (Secure Score); alert = a threat was detected now.",
        },
        "references": ["Microsoft Learn (SC-200): Security alerts and recommendations in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-016", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "A Defender for Cloud security alert includes an 'Intent' field mapping the activity to "
                "phases like PreAttack, InitialAccess, and Execution. Which framework are these phases based on?",
        "options": [
            {"id": "A", "text": "NIST Cybersecurity Framework (CSF)"},
            {"id": "B", "text": "PCI DSS"},
            {"id": "C", "text": "The Microsoft Cloud Security Benchmark"},
            {"id": "D", "text": "The MITRE ATT&CK framework"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defender for Cloud alerts map intent to MITRE ATT&CK tactics (e.g., InitialAccess, "
                       "Execution), helping analysts place an alert in the attack lifecycle.",
            "distractors": {
                "A": "NIST CSF organizes functions (Identify/Protect/Detect/Respond/Recover), not these kill-chain tactics.",
                "B": "PCI DSS is a payment-card compliance standard, not an attack-tactic taxonomy.",
                "C": "MCSB is Defender for Cloud's posture benchmark, not an alert kill-chain mapping.",
            },
            "exam_pattern": "Alert 'Intent' / tactics = MITRE ATT&CK mapping.",
        },
        "references": ["Microsoft Learn (SC-200): Respond to security alerts (MITRE ATT&CK intent)"],
    },
    {
        "id": "sc200-dfc-017", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants Microsoft Defender for Cloud security alerts to flow into Microsoft Sentinel "
                "for correlation with other data sources. What is the correct approach?",
        "options": [
            {"id": "A", "text": "Enable the Microsoft Defender for Cloud data connector in Microsoft Sentinel"},
            {"id": "B", "text": "Manually copy each alert into a spreadsheet"},
            {"id": "C", "text": "Rebuild each alert as a Sentinel analytics rule"},
            {"id": "D", "text": "Alerts cannot be sent to Sentinel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Defender for Cloud connector streams its security alerts into Sentinel, "
                       "where they can create incidents and be correlated with other sources.",
            "distractors": {
                "B": "Manual copying is not a supported or scalable integration.",
                "C": "You do not recreate alerts as rules; a connector streams them in automatically.",
                "D": "Alerts can be streamed to Sentinel via the connector (and the unified Defender portal).",
            },
            "exam_pattern": "Get Defender for Cloud alerts into Sentinel = enable the Defender for Cloud data connector.",
        },
        "references": ["Microsoft Learn (SC-200): Connect Microsoft Defender for Cloud alerts to Microsoft Sentinel"],
    },
    {
        "id": "sc200-dfc-018", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "When a specific Defender for Cloud alert fires, a team wants to automatically trigger a "
                "remediation workflow (a Logic App) without manual steps. Which feature enables this?",
        "options": [
            {"id": "A", "text": "Workflow automation (a Logic App triggered by alerts/recommendations)"},
            {"id": "B", "text": "Secure Score"},
            {"id": "C", "text": "The Regulatory compliance dashboard"},
            {"id": "D", "text": "Asset inventory"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud's workflow automation triggers a Logic App when matching alerts or "
                       "recommendations occur, enabling automated response or notification.",
            "distractors": {
                "B": "Secure Score measures posture; it does not trigger workflows.",
                "C": "The compliance dashboard reports standard adherence; it is not an automation trigger.",
                "D": "Asset inventory lists resources; it does not run response workflows.",
            },
            "exam_pattern": "Auto-respond to Defender for Cloud alerts = workflow automation + Logic Apps.",
        },
        "references": ["Microsoft Learn (SC-200): Workflow automation in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-019", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 3, "type": "mcq",
        "stem": "Analysts are overwhelmed by a specific benign alert from a known internal vulnerability "
                "scanner. Which feature stops that particular alert pattern from recurring without disabling the whole plan?",
        "options": [
            {"id": "A", "text": "Turning off Defender for Servers"},
            {"id": "B", "text": "An alert suppression rule"},
            {"id": "C", "text": "Lowering the Secure Score target"},
            {"id": "D", "text": "Deleting the scanned resource"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Alert suppression rules let you automatically dismiss a specific, known-benign alert "
                       "pattern while keeping the plan and all other detections active.",
            "distractors": {
                "A": "Disabling the plan removes all protection, not just the noisy alert.",
                "C": "Secure Score targets do not control alert generation.",
                "D": "Deleting the resource is destructive and is not an alert-tuning mechanism.",
            },
            "exam_pattern": "Quiet a specific benign alert = suppression rule, not disabling the plan.",
        },
        "references": ["Microsoft Learn (SC-200): Suppress security alerts in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-020", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "multi",
        "stem": "A high-severity Defender for Cloud alert fires on a production VM. Which TWO are "
                "appropriate analyst actions? (Choose two.)",
        "options": [
            {"id": "A", "text": "Review the alert details, affected resource, and MITRE intent, then investigate"},
            {"id": "B", "text": "Immediately delete the virtual machine"},
            {"id": "C", "text": "Use the alert's remediation steps and linked recommendations to contain and harden"},
            {"id": "D", "text": "Disable Microsoft Defender for Cloud tenant-wide"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Read the alert (resource, intent, evidence) and investigate, then follow the alert's "
                       "remediation guidance and related recommendations to contain and harden the resource.",
            "distractors": {
                "B": "Deleting a production VM destroys evidence and service; it is not a standard triage step.",
                "D": "Disabling Defender for Cloud removes detection entirely - the opposite of responding.",
            },
            "exam_pattern": "Triage = understand the alert/scope, then remediate via the provided steps - not destroy or disable protection.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate and respond to Defender for Cloud alerts"],
    },
]
