"""Microsoft SC-900 pool - Domain 3: Capabilities of Microsoft Security Solutions.

Original, objective-aligned practice items for the five security-solutions
subtopics tracked in CertLab:
  * sc9_azure_security      - core Azure infrastructure security: network
                              security groups, Azure Firewall, Azure DDoS
                              Protection, Web Application Firewall, Azure
                              Bastion, and Azure Key Vault.
  * sc9_defender_for_cloud  - Microsoft Defender for Cloud: cloud security
                              posture management, secure score, workload
                              protections, and the regulatory compliance
                              dashboard.
  * sc9_sentinel            - Microsoft Sentinel: cloud-native SIEM + SOAR,
                              data connectors, analytics, workbooks, playbooks.
  * sc9_defender_xdr        - Microsoft Defender XDR (formerly Microsoft 365
                              Defender): Defender for Endpoint, Office 365,
                              Identity, and Cloud Apps, via the Defender portal.
  * sc9_security_baselines  - security baselines and the Microsoft cloud
                              security benchmark.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the key authored as "A" is not positionally
biased, every wrong option carries a distractor note, and each item cites the
Microsoft Learn (SC-900) area. Current product names are used throughout
(Microsoft Defender XDR, Microsoft Defender for Cloud, Microsoft Sentinel).
Fundamentals depth only - which solution fits a need; no numeric limits or
preview trivia, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== sc9_azure_security ===============================================
    {
        "id": "sc900-sec-001", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs to allow or deny network traffic to and from Azure virtual machines in "
                "a subnet based on source/destination IP address, port, and protocol. Which Azure feature "
                "provides this basic traffic filtering?",
        "options": [
            {"id": "A", "text": "A network security group (NSG)"},
            {"id": "B", "text": "Azure Bastion"},
            {"id": "C", "text": "Azure Key Vault"},
            {"id": "D", "text": "Microsoft Sentinel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A network security group filters inbound and outbound traffic to Azure resources using "
                       "allow/deny rules based on IP, port, and protocol.",
            "distractors": {
                "B": "Azure Bastion provides secure RDP/SSH access to VMs, not subnet traffic filtering rules.",
                "C": "Azure Key Vault stores secrets, keys, and certificates; it does not filter network traffic.",
                "D": "Microsoft Sentinel is a SIEM/SOAR platform for analytics and response, not a packet filter.",
            },
            "exam_pattern": "Basic allow/deny by IP/port/protocol on subnets or NICs = network security group.",
        },
        "references": ["Microsoft Learn (SC-900): Describe network security groups"],
    },
    {
        "id": "sc900-sec-002", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a managed, stateful, cloud-based firewall service to centrally protect "
                "resources across many Azure virtual networks, including threat-intelligence-based filtering. "
                "Which service best fits?",
        "options": [
            {"id": "A", "text": "Azure Firewall"},
            {"id": "B", "text": "A network security group (NSG)"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Azure Key Vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Firewall is a managed, stateful, cloud-based network security service that "
                       "centrally protects virtual networks and supports threat-intelligence-based filtering.",
            "distractors": {
                "B": "An NSG provides basic per-subnet/NIC allow-deny rules, not a centralized managed firewall with threat intelligence.",
                "C": "Azure Bastion provides secure VM remote access, not centralized network firewalling.",
                "D": "Azure Key Vault secures secrets and keys, not network traffic across virtual networks.",
            },
            "exam_pattern": "Managed, centralized, stateful firewall with threat intel = Azure Firewall (vs basic NSG rules).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Firewall"],
    },
    {
        "id": "sc900-sec-003", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Which Azure service helps protect applications from attacks that attempt to overwhelm "
                "resources by flooding them with traffic, so the application stays available?",
        "options": [
            {"id": "A", "text": "Azure DDoS Protection"},
            {"id": "B", "text": "Azure Key Vault"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure DDoS Protection defends applications against distributed denial-of-service attacks "
                       "that flood resources to exhaust them and cause outages.",
            "distractors": {
                "B": "Azure Key Vault secures secrets and keys; it does not mitigate flooding attacks.",
                "C": "Azure Bastion provides secure remote access to VMs, not DDoS mitigation.",
                "D": "Conditional Access governs identity sign-in decisions, not network flooding attacks.",
            },
            "exam_pattern": "Protect against traffic-flooding attacks that exhaust resources = Azure DDoS Protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure DDoS Protection"],
    },
    {
        "id": "sc900-sec-004", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to protect its public web applications from common web exploits such as SQL "
                "injection and cross-site scripting at the HTTP layer. Which capability should it use?",
        "options": [
            {"id": "A", "text": "A Web Application Firewall (WAF)"},
            {"id": "B", "text": "A network security group (NSG)"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Azure DDoS Protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Web Application Firewall protects web apps from common HTTP-layer exploits such as SQL "
                       "injection and cross-site scripting.",
            "distractors": {
                "B": "An NSG filters by IP/port/protocol at the network layer; it does not inspect web-application exploits.",
                "C": "Azure Bastion provides secure VM remote access, not web-application protection.",
                "D": "DDoS Protection mitigates traffic floods, not application-layer injection or scripting attacks.",
            },
            "exam_pattern": "Protect web apps from SQL injection / XSS at HTTP layer = Web Application Firewall.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Web Application Firewall"],
    },
    {
        "id": "sc900-sec-005", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants secure RDP and SSH connectivity to Azure virtual machines directly "
                "through the Azure portal over TLS, without exposing the VMs' public IP addresses or opening "
                "RDP/SSH ports to the internet. Which service provides this?",
        "options": [
            {"id": "A", "text": "Azure Bastion"},
            {"id": "B", "text": "Azure Firewall"},
            {"id": "C", "text": "Azure Key Vault"},
            {"id": "D", "text": "Microsoft Sentinel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Bastion provides secure RDP/SSH access to VMs through the portal over TLS without "
                       "exposing public IPs or opening those ports to the internet.",
            "distractors": {
                "B": "Azure Firewall filters network traffic centrally; it is not the browser-based secure VM access service.",
                "C": "Azure Key Vault stores secrets and keys; it does not provide VM remote access.",
                "D": "Microsoft Sentinel is for security analytics and response, not RDP/SSH connectivity.",
            },
            "exam_pattern": "Secure RDP/SSH via portal, no public IP exposure = Azure Bastion.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Bastion"],
    },
    {
        "id": "sc900-sec-006", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Where should an organization centrally and securely store and manage the secrets, encryption "
                "keys, and certificates used by its Azure applications?",
        "options": [
            {"id": "A", "text": "Azure Key Vault"},
            {"id": "B", "text": "A network security group (NSG)"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Microsoft Entra ID Protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Key Vault centrally and securely stores and manages secrets, keys, and "
                       "certificates, and controls access to them.",
            "distractors": {
                "B": "An NSG filters network traffic; it does not store secrets or keys.",
                "C": "Azure Bastion provides secure VM access, not secret or key storage.",
                "D": "Microsoft Entra ID Protection detects identity risk; it is not a secrets store.",
            },
            "exam_pattern": "Central, secure store for secrets/keys/certificates = Azure Key Vault.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Key Vault"],
    },
    {
        "id": "sc900-sec-007", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 1, "type": "fill",
        "stem": "Azure DDoS Protection defends resources against DDoS attacks. In that acronym, DDoS stands for "
                "distributed denial of ___. Enter the missing one-word term.",
        "correct": ["service"],
        "explanation": {
            "correct": "DDoS stands for distributed denial of service - an attack that floods a target from many "
                       "sources to make it unavailable to legitimate users.",
            "distractors": {},
            "exam_pattern": "DDoS = distributed denial of service (availability attack via flooding).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure DDoS Protection"],
    },

    # ===== sc9_defender_for_cloud ===========================================
    {
        "id": "sc900-sec-008", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft solution provides cloud security posture management (CSPM) and cloud workload "
                "protection, continuously assessing the security of resources across Azure, on-premises, and "
                "other clouds?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Cloud"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "Azure Bastion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Cloud delivers CSPM and cloud workload protection, assessing and "
                       "strengthening the posture of resources across Azure, hybrid, and multicloud environments.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR for collecting and responding to security data, not a posture-management tool.",
                "C": "Microsoft Purview is the compliance and data governance suite, not cloud security posture management.",
                "D": "Azure Bastion provides secure VM access; it does not assess security posture.",
            },
            "exam_pattern": "CSPM + workload protection across Azure/hybrid/multicloud = Microsoft Defender for Cloud.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud"],
    },
    {
        "id": "sc900-sec-009", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Defender for Cloud expresses an organization's security posture as a single "
                "measurement that rises as recommended security controls are remediated. What is this "
                "measurement called?",
        "options": [
            {"id": "A", "text": "Secure score"},
            {"id": "B", "text": "Compliance score"},
            {"id": "C", "text": "Sign-in risk level"},
            {"id": "D", "text": "Service level agreement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud's secure score measures your current security posture; it increases as "
                       "you implement the recommended security controls.",
            "distractors": {
                "B": "Compliance score is the measure in Microsoft Purview Compliance Manager, not Defender for Cloud.",
                "C": "Sign-in risk level is a Microsoft Entra ID Protection signal, not a posture score.",
                "D": "A service level agreement is a uptime commitment, not a security-posture measurement.",
            },
            "exam_pattern": "Defender for Cloud posture measurement that rises with remediation = secure score.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (secure score)"],
    },
    {
        "id": "sc900-sec-010", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, where can an organization see how its environment aligns with "
                "standards such as ISO 27001 or the Microsoft cloud security benchmark?",
        "options": [
            {"id": "A", "text": "The regulatory compliance dashboard"},
            {"id": "B", "text": "A Microsoft Sentinel workbook"},
            {"id": "C", "text": "The Microsoft Entra admin center"},
            {"id": "D", "text": "The Microsoft 365 message center"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The regulatory compliance dashboard in Defender for Cloud shows how your environment "
                       "measures against regulatory standards and benchmarks you apply.",
            "distractors": {
                "B": "Sentinel workbooks visualize ingested security data; they are not Defender for Cloud's compliance view.",
                "C": "The Entra admin center manages identities, not Azure resource regulatory compliance posture.",
                "D": "The Microsoft 365 message center posts service announcements, not compliance alignment.",
            },
            "exam_pattern": "See alignment to standards/benchmarks in Defender for Cloud = regulatory compliance dashboard.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (regulatory compliance)"],
    },
    {
        "id": "sc900-sec-011", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Defender for Cloud offers enhanced, resource-specific protections (Defender plans) "
                "for workloads such as servers, storage, SQL databases, and containers. These protections are "
                "collectively known as which capability?",
        "options": [
            {"id": "A", "text": "Cloud workload protection"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Data loss prevention"},
            {"id": "D", "text": "Entitlement management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cloud workload protection (via Defender plans) provides advanced threat protection for "
                       "specific resource types like servers, storage, databases, and containers.",
            "distractors": {
                "B": "Conditional Access is an identity sign-in control, not workload threat protection.",
                "C": "Data loss prevention is a Microsoft Purview capability for protecting sensitive data, not workload protection.",
                "D": "Entitlement management governs access packages in Entra, not cloud workload protection.",
            },
            "exam_pattern": "Defender plans protecting servers/storage/SQL/containers = cloud workload protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (workload protections)"],
    },

    # ===== sc9_sentinel =====================================================
    {
        "id": "sc900-sec-012", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 1, "type": "mcq",
        "stem": "Which Microsoft solution is a cloud-native SIEM and SOAR platform that collects security data "
                "at scale and helps detect, investigate, and respond to threats across the enterprise?",
        "options": [
            {"id": "A", "text": "Microsoft Sentinel"},
            {"id": "B", "text": "Microsoft Defender for Cloud"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "Azure Firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Sentinel is a cloud-native SIEM and SOAR solution that ingests security data "
                       "broadly and supports detection, investigation, and automated response.",
            "distractors": {
                "B": "Defender for Cloud focuses on cloud security posture and workload protection, not enterprise-wide SIEM/SOAR.",
                "C": "Microsoft Purview is the compliance and data governance suite, not a SIEM.",
                "D": "Azure Firewall filters network traffic; it is not a SIEM/SOAR platform.",
            },
            "exam_pattern": "Cloud-native SIEM + SOAR for enterprise threat detection and response = Microsoft Sentinel.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel"],
    },
    {
        "id": "sc900-sec-013", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "To bring security logs and alerts from Microsoft and third-party sources (such as firewalls, "
                "Microsoft Entra ID, and Office 365) into Microsoft Sentinel, an analyst configures which "
                "component?",
        "options": [
            {"id": "A", "text": "Data connectors"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Workbooks"},
            {"id": "D", "text": "Access packages"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data connectors ingest logs and alerts from Microsoft and third-party sources into "
                       "Microsoft Sentinel so the data can be analyzed.",
            "distractors": {
                "B": "Playbooks automate response actions; they do not ingest source data.",
                "C": "Workbooks visualize data already ingested; they are not the ingestion mechanism.",
                "D": "Access packages are an Entra entitlement-management concept, unrelated to Sentinel ingestion.",
            },
            "exam_pattern": "Ingest data from sources into Sentinel = data connectors.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (data connectors)"],
    },
    {
        "id": "sc900-sec-014", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "A security operations team wants to automatically run a predefined set of remediation actions "
                "in response to a specific Microsoft Sentinel alert. Which Sentinel feature, built on Azure "
                "Logic Apps, provides this automation (the SOAR capability)?",
        "options": [
            {"id": "A", "text": "Playbooks"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Sensitivity labels"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Playbooks are automated response workflows built on Azure Logic Apps; they deliver "
                       "Sentinel's SOAR (security orchestration, automation, and response) capability.",
            "distractors": {
                "B": "Workbooks are for visualization and dashboards, not automated response.",
                "C": "Data connectors ingest data; they do not run response actions.",
                "D": "Sensitivity labels are a Microsoft Purview data-protection feature, not a Sentinel automation.",
            },
            "exam_pattern": "Automated response workflow on Logic Apps (SOAR) in Sentinel = playbook.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (playbooks)"],
    },
    {
        "id": "sc900-sec-015", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Sentinel feature provides interactive dashboards used to visualize and monitor "
                "the data that has been ingested?",
        "options": [
            {"id": "A", "text": "Workbooks"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Access reviews"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Workbooks provide interactive dashboards and visualizations of the data ingested into "
                       "Microsoft Sentinel.",
            "distractors": {
                "B": "Playbooks automate responses; they are not visualization dashboards.",
                "C": "Data connectors bring data in; they do not visualize it.",
                "D": "Access reviews are an Entra ID Governance feature, not a Sentinel visualization tool.",
            },
            "exam_pattern": "Interactive dashboards/visualization in Sentinel = workbooks (contrast with playbooks for automation).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (workbooks)"],
    },
    {
        "id": "sc900-sec-016", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 1, "type": "fill",
        "stem": "Microsoft Sentinel is described as a cloud-native SIEM and SOAR solution. In SIEM, the letters "
                "stand for security information and event ___. Enter the missing one-word term.",
        "correct": ["management"],
        "explanation": {
            "correct": "SIEM stands for security information and event management - collecting and analyzing "
                       "security data to detect and investigate threats.",
            "distractors": {},
            "exam_pattern": "SIEM = security information and event management; SOAR = security orchestration, automation, and response.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel"],
    },

    # ===== sc9_defender_xdr =================================================
    {
        "id": "sc900-sec-017", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft solution is an extended detection and response (XDR) suite that unifies "
                "protection across endpoints, email, identities, and cloud apps, correlating their signals into "
                "incidents (formerly called Microsoft 365 Defender)?",
        "options": [
            {"id": "A", "text": "Microsoft Defender XDR"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "Microsoft Defender for Cloud"},
            {"id": "D", "text": "Microsoft Purview"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender XDR (formerly Microsoft 365 Defender) correlates signals across "
                       "endpoints, email, identities, and cloud apps into unified incidents.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR that can ingest many sources; the XDR suite itself is Defender XDR.",
                "C": "Defender for Cloud protects cloud infrastructure posture and workloads, not the M365 XDR workloads.",
                "D": "Microsoft Purview is the compliance suite, not an XDR solution.",
            },
            "exam_pattern": "XDR across endpoints/email/identities/cloud apps, formerly M365 Defender = Microsoft Defender XDR.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR"],
    },
    {
        "id": "sc900-sec-018", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Defender XDR service provides endpoint detection and response (EDR), "
                "vulnerability management, and threat protection for devices such as laptops and servers?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Endpoint"},
            {"id": "B", "text": "Microsoft Defender for Office 365"},
            {"id": "C", "text": "Microsoft Defender for Identity"},
            {"id": "D", "text": "Microsoft Defender for Cloud Apps"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Endpoint protects devices (endpoints) with EDR, vulnerability "
                       "management, and threat protection.",
            "distractors": {
                "B": "Defender for Office 365 protects email and collaboration content, not device endpoints.",
                "C": "Defender for Identity monitors on-premises Active Directory signals, not device endpoints.",
                "D": "Defender for Cloud Apps is a CASB for SaaS app visibility, not an endpoint EDR tool.",
            },
            "exam_pattern": "EDR and protection for devices/endpoints = Microsoft Defender for Endpoint.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc900-sec-019", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "A company wants protection against malicious attachments, phishing, and unsafe links delivered "
                "through email and collaboration tools like Microsoft Teams and SharePoint. Which Microsoft "
                "Defender XDR service fits?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Office 365"},
            {"id": "B", "text": "Microsoft Defender for Endpoint"},
            {"id": "C", "text": "Microsoft Defender for Identity"},
            {"id": "D", "text": "Microsoft Sentinel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Office 365 protects against email- and collaboration-borne threats "
                       "such as malicious attachments, phishing, and unsafe links.",
            "distractors": {
                "B": "Defender for Endpoint protects devices, not email and collaboration content.",
                "C": "Defender for Identity focuses on on-premises identity threats, not email protection.",
                "D": "Microsoft Sentinel is a SIEM/SOAR platform, not the email-protection service.",
            },
            "exam_pattern": "Protect email/Teams/SharePoint from phishing and malicious links/attachments = Defender for Office 365.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Office 365"],
    },
    {
        "id": "sc900-sec-020", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Defender XDR service uses signals from on-premises Active Directory Domain "
                "Services to detect identity-based threats such as compromised accounts and lateral movement?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Identity"},
            {"id": "B", "text": "Microsoft Entra ID Protection"},
            {"id": "C", "text": "Microsoft Defender for Endpoint"},
            {"id": "D", "text": "Microsoft Defender for Cloud Apps"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Identity uses on-premises Active Directory signals to detect "
                       "identity threats like compromised accounts, lateral movement, and reconnaissance.",
            "distractors": {
                "B": "Entra ID Protection detects risk for cloud identities in Microsoft Entra ID, not on-premises AD DS signals.",
                "C": "Defender for Endpoint protects devices; it is not focused on AD identity threat detection.",
                "D": "Defender for Cloud Apps is a CASB for SaaS visibility, not an on-premises AD monitor.",
            },
            "exam_pattern": "Detect identity threats from on-prem Active Directory = Microsoft Defender for Identity (vs Entra ID Protection for cloud identities).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Identity"],
    },
    {
        "id": "sc900-sec-021", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Defender XDR service is a cloud access security broker (CASB) that gives "
                "visibility into and control over the cloud/SaaS apps used across an organization, including "
                "discovering shadow IT?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Cloud Apps"},
            {"id": "B", "text": "Microsoft Defender for Cloud"},
            {"id": "C", "text": "Microsoft Defender for Endpoint"},
            {"id": "D", "text": "Azure Firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Cloud Apps is a CASB that provides visibility into and control "
                       "over SaaS/cloud app usage, including discovering unsanctioned shadow IT.",
            "distractors": {
                "B": "Microsoft Defender for Cloud protects cloud infrastructure posture and workloads; it is not the CASB for SaaS apps.",
                "C": "Defender for Endpoint protects devices, not cloud app usage visibility.",
                "D": "Azure Firewall filters network traffic; it is not a CASB.",
            },
            "exam_pattern": "CASB for SaaS app visibility/control and shadow IT = Microsoft Defender for Cloud Apps (not Defender for Cloud).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud Apps"],
    },

    # ===== sc9_security_baselines ===========================================
    {
        "id": "sc900-sec-022", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 2, "type": "mcq",
        "stem": "What is the purpose of a security baseline?",
        "options": [
            {"id": "A", "text": "To provide a standardized set of recommended security configuration settings that resources should meet"},
            {"id": "B", "text": "To encrypt all data stored at rest automatically"},
            {"id": "C", "text": "To block all inbound traffic from the internet by default"},
            {"id": "D", "text": "To automatically respond to and remediate every security alert"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A security baseline is a standardized group of recommended configuration settings that "
                       "resources should conform to, helping maintain a consistent, hardened posture.",
            "distractors": {
                "B": "Automatic encryption at rest is a data-protection feature, not the definition of a baseline.",
                "C": "Blocking all inbound traffic is a firewall rule, not what a security baseline is.",
                "D": "Automated alert remediation describes SOAR/playbooks, not a configuration baseline.",
            },
            "exam_pattern": "Standardized recommended configuration settings to conform to = a security baseline.",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines"],
    },
    {
        "id": "sc900-sec-023", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft-provided set of best-practice security recommendations and controls can be "
                "used as a baseline to secure Azure workloads and is assessed within Microsoft Defender for "
                "Cloud?",
        "options": [
            {"id": "A", "text": "The Microsoft cloud security benchmark (MCSB)"},
            {"id": "B", "text": "The CIA triad"},
            {"id": "C", "text": "A Conditional Access policy"},
            {"id": "D", "text": "A Microsoft Sentinel playbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft cloud security benchmark is a set of best-practice controls used as a "
                       "baseline for securing Azure workloads and is assessed in Defender for Cloud.",
            "distractors": {
                "B": "The CIA triad is a set of security goals (confidentiality, integrity, availability), not a configuration benchmark.",
                "C": "A Conditional Access policy governs identity sign-in; it is not a security baseline/benchmark.",
                "D": "A Sentinel playbook automates response actions; it is not a baseline of controls.",
            },
            "exam_pattern": "Microsoft baseline of best-practice controls for Azure, assessed in Defender for Cloud = Microsoft cloud security benchmark.",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines for Azure"],
    },
    {
        "id": "sc900-sec-024", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 2, "type": "multi",
        "stem": "Applying security baselines across many Azure resources helps an organization in which TWO "
                "ways? (Choose two.)",
        "options": [
            {"id": "A", "text": "It applies consistent, recommended hardening settings across resources"},
            {"id": "B", "text": "It highlights resources that deviate from the recommended configuration"},
            {"id": "C", "text": "It guarantees that all services become free of charge"},
            {"id": "D", "text": "It removes the need for identity and access management"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Baselines bring consistent, recommended hardening to resources and make deviations from "
                       "the recommended configuration visible so they can be corrected.",
            "distractors": {
                "C": "Baselines are about security configuration, not pricing; they do not make services free.",
                "D": "Baselines complement identity and access management; they do not remove the need for it.",
            },
            "exam_pattern": "Baselines = consistent hardening + visibility into configuration drift.",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines"],
    },
]
