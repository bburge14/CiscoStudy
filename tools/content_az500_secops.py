"""Microsoft AZ-500 (Azure Security Engineer) pool - Domain 4: Manage Security Operations.

Original, objective-aligned practice items for the four subtopics tracked in CertLab:
  * az500_defender_for_cloud  - Secure Score, foundational CSPM vs Defender CSPM,
                                workload protection plans mapped to resources, and
                                the regulatory compliance dashboard.
  * az500_sentinel_ops        - Microsoft Sentinel on Log Analytics, data
                                connectors, analytics rules, incidents, and SOAR
                                (playbooks and automation rules).
  * az500_monitoring_logging  - Azure Monitor diagnostic settings, the activity
                                log, Log Analytics and KQL, and alert rules with
                                action groups.
  * az500_governance_policy   - Azure Policy effects and initiatives, management
                                groups, resource locks, and the modern successors
                                to Azure Blueprints.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), and the authored answer key is spread across A/B/C/D
rather than defaulting to "A"; every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Current product names are
used throughout: Microsoft Defender for Cloud (formerly Azure Security Center /
Azure Defender) and Microsoft Sentinel (formerly Azure Sentinel). Items are
original and aligned to the public AZ-500 objectives - never real or memorized
exam items.
"""

QUESTIONS = [
    # ===== az500_defender_for_cloud =========================================
    {
        "id": "az500-ops-001", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 1, "type": "mcq",
        "stem": "Leadership wants a single percentage that reflects the current security posture of your "
                "Azure subscriptions and rises as your team remediates recommendations. Which Microsoft "
                "Defender for Cloud feature provides this?",
        "options": [
            {"id": "A", "text": "Just-in-time VM access"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Secure Score"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Secure Score aggregates your remediation of security recommendations into a single percentage "
                       "that measures and tracks posture over time.",
            "distractors": {
                "A": "JIT reduces management-port exposure; it is not a posture score.",
                "B": "Workbooks visualize data but are not the built-in posture percentage.",
                "D": "A resource lock prevents deletion/modification; it does not measure posture.",
            },
            "exam_pattern": "Single posture percentage that rises as you remediate recommendations = Defender for Cloud Secure Score.",
        },
        "references": ["Microsoft Learn (AZ-500): Secure Score in Microsoft Defender for Cloud"],
    },
    {
        "id": "az500-ops-002", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "You already get asset inventory, Secure Score, security recommendations, and Microsoft "
                "Cloud Security Benchmark assessments at no cost. Now you need attack path analysis and the "
                "cloud security explorer to reason about risk across resources. What must you enable?",
        "options": [
            {"id": "A", "text": "Nothing; attack path analysis is included in the free tier"},
            {"id": "B", "text": "The Defender CSPM plan"},
            {"id": "C", "text": "Microsoft Sentinel"},
            {"id": "D", "text": "A Log Analytics workspace"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Attack path analysis and the cloud security explorer are capabilities of the paid Defender CSPM "
                       "plan; the free foundational CSPM tier does not include them.",
            "distractors": {
                "A": "These are paid Defender CSPM capabilities, not part of free foundational CSPM.",
                "C": "Sentinel is a SIEM/SOAR; it does not provide Defender for Cloud attack path analysis.",
                "D": "A Log Analytics workspace stores logs; it does not by itself enable Defender CSPM features.",
            },
            "exam_pattern": "Free foundational CSPM = inventory, Secure Score, recommendations, MCSB; paid Defender CSPM "
                            "adds attack path analysis, cloud security explorer, and agentless scanning.",
        },
        "references": ["Microsoft Learn (AZ-500): Cloud security posture management - foundational vs Defender CSPM"],
    },
    {
        "id": "az500-ops-003", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "You must enable threat protection specifically for your Azure Storage accounts, including "
                "detection of malware uploads and unusual access patterns. Which plan do you turn on?",
        "options": [
            {"id": "A", "text": "Defender for Servers"},
            {"id": "B", "text": "Defender for Key Vault"},
            {"id": "C", "text": "Defender for Resource Manager"},
            {"id": "D", "text": "Defender for Storage"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Defender for Storage provides threat detection for storage accounts, including malware "
                       "scanning of uploads and alerts on unusual access patterns.",
            "distractors": {
                "A": "Defender for Servers protects VMs/servers, not storage accounts.",
                "B": "Defender for Key Vault detects anomalous vault access, not storage account threats.",
                "C": "Defender for Resource Manager monitors the ARM control/management layer, not storage data threats.",
            },
            "exam_pattern": "Match the plan to the resource - Defender for Storage protects storage accounts; each "
                            "Defender plan is scoped to its resource type.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Defender for Storage"],
    },
    {
        "id": "az500-ops-004", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "An auditor asks you to show how your Azure environment maps to PCI DSS and ISO 27001 "
                "controls and where it falls short. Which Microsoft Defender for Cloud capability presents this?",
        "options": [
            {"id": "A", "text": "The regulatory compliance dashboard"},
            {"id": "B", "text": "Secure Score history only"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Network security groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The regulatory compliance dashboard maps your posture to compliance standards such as PCI DSS "
                       "and ISO 27001 (the Microsoft Cloud Security Benchmark is applied by default; you add other standards).",
            "distractors": {
                "B": "Secure Score reflects general posture, not control-by-control mapping to a specific standard.",
                "C": "Bastion provides secure VM access; it has no compliance mapping.",
                "D": "NSGs filter traffic; they do not report regulatory compliance.",
            },
            "exam_pattern": "Map posture to standards (PCI DSS, ISO 27001, etc.) = the Defender for Cloud regulatory "
                            "compliance dashboard; MCSB is the default applied standard.",
        },
        "references": ["Microsoft Learn (AZ-500): Regulatory compliance in Microsoft Defender for Cloud"],
    },
    {
        "id": "az500-ops-005", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Microsoft Defender for Cloud expresses your overall security posture as "
                "a ________ Score, a percentage that increases as you remediate its security recommendations.",
        "correct": ["secure"],
        "explanation": {
            "correct": "Secure Score aggregates how many recommendations you have remediated into a single percentage, "
                       "giving a measurable, improvable view of posture.",
            "exam_pattern": "Defender for Cloud posture metric = Secure Score (remediate recommendations to raise it).",
        },
        "references": ["Microsoft Learn (AZ-500): Secure Score in Microsoft Defender for Cloud"],
    },

    # ===== az500_sentinel_ops ===============================================
    {
        "id": "az500-ops-006", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "You are deploying Microsoft Sentinel and need to bring in sign-in and audit logs from "
                "Microsoft Entra ID plus events from Azure activity logs. On what is Sentinel built, and how "
                "do you ingest these sources?",
        "options": [
            {"id": "A", "text": "On a storage account, ingested via SAS tokens"},
            {"id": "B", "text": "On a Log Analytics workspace, ingested via data connectors"},
            {"id": "C", "text": "On an NSG, ingested via flow logs only"},
            {"id": "D", "text": "On Key Vault, ingested via access policies"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Sentinel runs on top of a Log Analytics workspace and uses data connectors to ingest "
                       "sources such as Entra ID logs and Azure activity logs.",
            "distractors": {
                "A": "Sentinel is not built on a storage account, and SAS tokens are not how it ingests sources.",
                "C": "Sentinel is not built on an NSG; data connectors (not NSG flow logs alone) bring in the sources.",
                "D": "Key Vault stores secrets; it is not the Sentinel platform or its ingestion method.",
            },
            "exam_pattern": "Microsoft Sentinel is built on a Log Analytics workspace and ingests sources through data connectors.",
        },
        "references": ["Microsoft Learn (AZ-500): Connect data sources to Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-007", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Sentinel, which component continuously evaluates ingested data against "
                "detection logic and generates alerts that are grouped into incidents for investigation?",
        "options": [
            {"id": "A", "text": "Analytics rules"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Workbooks"},
            {"id": "D", "text": "Data connectors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Analytics rules (for example, scheduled or near-real-time) run detection logic over the data "
                       "and generate alerts, which Sentinel groups into incidents.",
            "distractors": {
                "B": "Playbooks are automated response workflows (Logic Apps), not the detection logic that raises alerts.",
                "C": "Workbooks are interactive dashboards for visualization, not detections.",
                "D": "Data connectors bring data in; they do not evaluate detection logic.",
            },
            "exam_pattern": "Sentinel detections = analytics rules (create alerts/incidents); playbooks respond; workbooks visualize.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Sentinel analytics rules"],
    },
    {
        "id": "az500-ops-008", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 3, "type": "mcq",
        "stem": "When a specific Sentinel incident type is created, you want to automatically disable the "
                "affected user and post to a Teams channel, with no analyst action. Which combination "
                "implements this SOAR response?",
        "options": [
            {"id": "A", "text": "A workbook triggered by a KQL query"},
            {"id": "B", "text": "A diagnostic setting routed to a storage account"},
            {"id": "C", "text": "An automation rule that triggers a playbook (an Azure Logic Apps workflow)"},
            {"id": "D", "text": "A network security group rule"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Automation rules react to incident creation and can trigger playbooks (Logic Apps workflows) "
                       "that take actions such as disabling a user and posting to Teams - Sentinel's SOAR capability.",
            "distractors": {
                "A": "Workbooks visualize data; they do not execute response actions.",
                "B": "Diagnostic settings route logs; they do not perform automated incident response.",
                "D": "An NSG rule filters network traffic; it cannot disable a user or post to Teams.",
            },
            "exam_pattern": "Sentinel SOAR = automation rules trigger playbooks (Logic Apps) to respond to incidents automatically.",
        },
        "references": ["Microsoft Learn (AZ-500): Automate threat response with playbooks and automation rules"],
    },
    {
        "id": "az500-ops-009", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "An analyst needs a single view in Microsoft Sentinel that aggregates related alerts and "
                "entities for a security case, tracks status and severity, and supports assignment and "
                "investigation. Which object is this?",
        "options": [
            {"id": "A", "text": "A data connector"},
            {"id": "B", "text": "A workbook"},
            {"id": "C", "text": "A hunting query"},
            {"id": "D", "text": "An incident"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An incident groups related alerts and entities into a trackable case with status, severity, and "
                       "ownership, and is the unit analysts investigate.",
            "distractors": {
                "A": "A data connector ingests sources; it is not a case-management object.",
                "B": "A workbook is a dashboard, not a tracked case with status/severity/owner.",
                "C": "A hunting query proactively searches data; it is not the case object that groups alerts.",
            },
            "exam_pattern": "Sentinel case object grouping alerts/entities with status, severity, and ownership = an incident.",
        },
        "references": ["Microsoft Learn (AZ-500): Investigate incidents in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-010", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "multi",
        "stem": "Which TWO Microsoft Sentinel components work together to orchestrate and automate incident "
                "response (SOAR)? (Choose two.)",
        "options": [
            {"id": "A", "text": "Playbooks (Azure Logic Apps workflows)"},
            {"id": "B", "text": "Data connectors"},
            {"id": "C", "text": "Automation rules"},
            {"id": "D", "text": "Transparent Data Encryption"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Automation rules define when and under what conditions to respond, and playbooks (Logic Apps) "
                       "carry out the response actions - together they provide Sentinel's SOAR.",
            "distractors": {
                "B": "Data connectors ingest data into Sentinel; they are not response-orchestration components.",
                "D": "TDE encrypts databases at rest and is unrelated to Sentinel SOAR.",
            },
            "exam_pattern": "Sentinel SOAR = automation rules (when/conditions) + playbooks (Logic Apps actions).",
        },
        "references": ["Microsoft Learn (AZ-500): Security orchestration, automation, and response (SOAR) in Microsoft Sentinel"],
    },

    # ===== az500_monitoring_logging =========================================
    {
        "id": "az500-ops-011", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "You must send a Key Vault's resource (data-plane) logs to a Log Analytics workspace for "
                "90-day analysis and alerting. Which configuration routes these platform logs there?",
        "options": [
            {"id": "A", "text": "An NSG flow log"},
            {"id": "B", "text": "A diagnostic setting on the Key Vault"},
            {"id": "C", "text": "A stored access policy"},
            {"id": "D", "text": "A user-defined route"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A diagnostic setting on the resource routes its platform/resource logs and metrics to a Log "
                       "Analytics workspace (and/or storage account or event hub) for retention and analysis.",
            "distractors": {
                "A": "NSG flow logs capture network traffic, not Key Vault resource logs.",
                "C": "A stored access policy manages storage SAS constraints, not log routing.",
                "D": "A UDR controls routing of network traffic, not log export.",
            },
            "exam_pattern": "Route a resource's platform/resource logs to Log Analytics/Storage/Event Hub = diagnostic "
                            "settings on that resource.",
        },
        "references": ["Microsoft Learn (AZ-500): Diagnostic settings in Azure Monitor"],
    },
    {
        "id": "az500-ops-012", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "You need to see who deleted a virtual machine and when, at the subscription management "
                "(control-plane) level. Which log records these subscription-level operations?",
        "options": [
            {"id": "A", "text": "The Azure activity log"},
            {"id": "B", "text": "The NSG flow log"},
            {"id": "C", "text": "Microsoft Entra ID sign-in logs"},
            {"id": "D", "text": "The guest OS event log"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Azure activity log records subscription-level control-plane operations - who performed a "
                       "create/update/delete on a resource, and when.",
            "distractors": {
                "B": "NSG flow logs record network traffic flows, not resource management operations.",
                "C": "Entra sign-in logs record authentication events, not who deleted an Azure resource.",
                "D": "Guest OS event logs are inside the VM and cannot record the VM's own deletion at the control plane.",
            },
            "exam_pattern": "Subscription-level control-plane operations (who/what/when for create/update/delete) = the "
                            "Azure activity log.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Monitor activity log"],
    },
    {
        "id": "az500-ops-013", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "Having centralized logs from many resources into one Log Analytics workspace, which "
                "language do you use to write queries, detections, and alerts over that data?",
        "options": [
            {"id": "A", "text": "T-SQL"},
            {"id": "B", "text": "PowerShell DSC"},
            {"id": "C", "text": "Kusto Query Language (KQL)"},
            {"id": "D", "text": "Bicep"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Kusto Query Language (KQL) is the query language for Azure Monitor Logs / Log Analytics (and "
                       "Microsoft Sentinel), used for queries, detections, and log-based alerts.",
            "distractors": {
                "A": "T-SQL queries relational databases, not Log Analytics / Azure Monitor Logs.",
                "B": "PowerShell DSC is a configuration-management technology, not a log query language.",
                "D": "Bicep is an infrastructure-as-code language for deployments, not log querying.",
            },
            "exam_pattern": "Query Azure Monitor Logs / Log Analytics (and Sentinel) with Kusto Query Language (KQL).",
        },
        "references": ["Microsoft Learn (AZ-500): Log queries with Kusto Query Language (KQL)"],
    },
    {
        "id": "az500-ops-014", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "You want to be notified and trigger an action automatically whenever a particular high-risk "
                "operation is recorded in the activity log. Which Azure Monitor capability do you configure?",
        "options": [
            {"id": "A", "text": "A workbook"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "A diagnostic setting alone"},
            {"id": "D", "text": "An alert rule with an action group"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An Azure Monitor alert rule evaluates a condition (here on the activity log) and, when it fires, "
                       "an action group sends notifications and triggers automated actions.",
            "distractors": {
                "A": "Workbooks visualize data; they do not notify or trigger actions.",
                "B": "A resource lock prevents changes; it does not alert on activity.",
                "C": "A diagnostic setting routes logs but does not itself notify or act; you still need an alert rule.",
            },
            "exam_pattern": "Notify/act on a condition in metrics or logs = an Azure Monitor alert rule firing an action group.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Monitor alerts and action groups"],
    },
    {
        "id": "az500-ops-015", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Logs collected in an Azure Monitor Log Analytics workspace (and in "
                "Microsoft Sentinel) are queried with the ________ Query Language, abbreviated KQL.",
        "correct": ["kusto"],
        "explanation": {
            "correct": "Kusto Query Language (KQL) is the read-only query language for Azure Monitor Logs, Log "
                       "Analytics, and Microsoft Sentinel.",
            "exam_pattern": "KQL = Kusto Query Language, used across Log Analytics and Sentinel.",
        },
        "references": ["Microsoft Learn (AZ-500): Kusto Query Language (KQL) overview"],
    },

    # ===== az500_governance_policy ==========================================
    {
        "id": "az500-ops-016", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "To stop anyone from creating storage accounts that allow public blob access, you want "
                "noncompliant resource creations blocked at deployment time. Which Azure Policy effect "
                "achieves this?",
        "options": [
            {"id": "A", "text": "Audit"},
            {"id": "B", "text": "Deny"},
            {"id": "C", "text": "Append"},
            {"id": "D", "text": "DeployIfNotExists"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Deny effect blocks creation or update of resources that do not satisfy the policy, stopping "
                       "the noncompliant deployment before it happens.",
            "distractors": {
                "A": "Audit only flags noncompliant resources; it does not block their creation.",
                "C": "Append adds fields to a resource; it does not block a noncompliant deployment.",
                "D": "DeployIfNotExists deploys a related resource after creation; it does not block the initial deployment.",
            },
            "exam_pattern": "Block noncompliant deployments = the Deny effect; Audit only records; DeployIfNotExists/"
                            "Modify remediate.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy effects (Deny, Audit, DeployIfNotExists, Modify)"],
    },
    {
        "id": "az500-ops-017", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "You want to assign a whole group of related Azure Policy definitions (for example, all "
                "controls for a compliance standard) as a single unit with one assignment. What do you create?",
        "options": [
            {"id": "A", "text": "A management group"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "A policy initiative (policy set definition)"},
            {"id": "D", "text": "An action group"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A policy initiative (policy set definition) bundles many policy definitions so they can be "
                       "assigned and managed together as one unit.",
            "distractors": {
                "A": "A management group organizes subscriptions; it is not a bundle of policy definitions.",
                "B": "A resource lock prevents deletion/modification; it does not bundle policies.",
                "D": "An action group defines alert notifications/actions, not a set of policies.",
            },
            "exam_pattern": "Bundle many policy definitions into one assignable unit = an initiative (policy set definition).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy initiatives (policy set definitions)"],
    },
    {
        "id": "az500-ops-018", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "Your organization has dozens of subscriptions and wants to apply a baseline set of RBAC "
                "assignments and policy initiatives once, inherited by all current and future subscriptions. "
                "Which Azure governance construct enables this?",
        "options": [
            {"id": "A", "text": "Management groups"},
            {"id": "B", "text": "Resource groups"},
            {"id": "C", "text": "Availability zones"},
            {"id": "D", "text": "Network security groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Management groups sit above subscriptions in the hierarchy, so policy and RBAC assigned at a "
                       "management group are inherited by all subscriptions beneath it, now and in the future.",
            "distractors": {
                "B": "A resource group contains resources within one subscription; it cannot span or govern many subscriptions.",
                "C": "Availability zones provide datacenter-level resiliency, not governance inheritance.",
                "D": "NSGs filter network traffic; they are unrelated to subscription governance.",
            },
            "exam_pattern": "Apply policy/RBAC across many subscriptions with inheritance = management groups (above "
                            "subscriptions in the hierarchy).",
        },
        "references": ["Microsoft Learn (AZ-500): Organize resources with management groups"],
    },
    {
        "id": "az500-ops-019", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "To protect a production virtual network from accidental deletion while still allowing "
                "configuration changes, which control should you apply?",
        "options": [
            {"id": "A", "text": "An Azure Policy Audit effect"},
            {"id": "B", "text": "A ReadOnly resource lock"},
            {"id": "C", "text": "A network security group"},
            {"id": "D", "text": "A CanNotDelete resource lock"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A CanNotDelete lock prevents deletion of the resource while still permitting read and "
                       "configuration changes, exactly matching the requirement.",
            "distractors": {
                "A": "An Audit policy only reports noncompliance; it does not prevent deletion.",
                "B": "A ReadOnly lock would also block the allowed configuration changes, which is too restrictive here.",
                "C": "An NSG filters traffic; it does not prevent resource deletion.",
            },
            "exam_pattern": "Prevent deletion but allow changes = CanNotDelete lock; block all changes = ReadOnly lock.",
        },
        "references": ["Microsoft Learn (AZ-500): Lock resources to prevent changes (CanNotDelete, ReadOnly)"],
    },
    {
        "id": "az500-ops-020", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 3, "type": "mcq",
        "stem": "Your team previously planned to package policies, role assignments, and ARM templates as a "
                "repeatable environment using Azure Blueprints, which is now on a retirement path. Which "
                "current Azure capabilities are recommended to achieve the same governed, repeatable deployments?",
        "options": [
            {"id": "A", "text": "Network security groups and application security groups"},
            {"id": "B", "text": "Azure Policy (and initiatives) together with template specs and deployment stacks"},
            {"id": "C", "text": "Azure Bastion and just-in-time VM access"},
            {"id": "D", "text": "Dynamic Data Masking and Always Encrypted"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "With Azure Blueprints retiring, Microsoft recommends Azure Policy and initiatives for guardrails, "
                       "plus template specs (to store/version templates) and deployment stacks (to deploy and lifecycle-manage "
                       "resources) for repeatable, governed environments.",
            "distractors": {
                "A": "NSGs/ASGs are network traffic controls, not a governance/deployment packaging solution.",
                "C": "Bastion and JIT are access controls, not repeatable environment governance.",
                "D": "These are database data-protection features, unrelated to deploying governed environments.",
            },
            "exam_pattern": "Blueprints is retiring - use Azure Policy/initiatives for guardrails plus template specs and "
                            "deployment stacks for repeatable, governed deployments.",
        },
        "references": ["Microsoft Learn (AZ-500): Govern with Azure Policy; Azure Blueprints retirement guidance"],
    },
]
