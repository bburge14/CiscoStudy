"""Microsoft AZ-500 (Azure Security Engineer) pool - Domain 2: Secure Networking.

Original, objective-aligned practice items for the three Secure Networking
subtopics tracked in CertLab:
  * az500_network_security      - network security groups (NSGs) and rule
                                  evaluation, application security groups (ASGs),
                                  Azure Firewall and Firewall Policy rule types,
                                  and hub-and-spoke segmentation with UDRs.
  * az500_private_connectivity  - service endpoints vs private endpoints
                                  (Azure Private Link), private-endpoint DNS,
                                  disabling public network access, and
                                  Azure Bastion.
  * az500_edge_protection       - Web Application Firewall (Application Gateway
                                  vs Front Door), Azure Firewall Premium
                                  (TLS inspection/IDPS), Azure DDoS Protection,
                                  and just-in-time VM access.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), and the authored answer key is spread across A/B/C/D
rather than defaulting to "A"; every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Current product names are
used throughout (Microsoft Defender for Cloud). Items are original and aligned to
the public AZ-500 objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== az500_network_security ===========================================
    {
        "id": "az500-net-001", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 1, "type": "mcq",
        "stem": "You must allow inbound HTTPS (TCP 443) to a subnet of web servers while blocking all "
                "other inbound traffic from the internet. Which Azure control filters this by source, "
                "destination, port, and protocol at the subnet level, at no additional cost?",
        "options": [
            {"id": "A", "text": "Azure Firewall"},
            {"id": "B", "text": "Azure Front Door"},
            {"id": "C", "text": "A network security group (NSG)"},
            {"id": "D", "text": "A user-defined route (UDR)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A network security group filters traffic with 5-tuple allow/deny rules (source, source "
                       "port, destination, destination port, protocol) and can be associated to a subnet at no extra charge.",
            "distractors": {
                "A": "Azure Firewall is a chargeable managed firewall for centralized filtering; a simple per-subnet "
                     "allow/deny is met by an NSG at no cost.",
                "B": "Front Door is a global HTTP(S) entry/CDN service, not a subnet-level packet filter.",
                "D": "A user-defined route controls next-hop routing, not traffic allow/deny.",
            },
            "exam_pattern": "Basic L3-L4 allow/deny by 5-tuple on a subnet or NIC = NSG (free).",
        },
        "references": ["Microsoft Learn (AZ-500): Network security groups"],
    },
    {
        "id": "az500-net-002", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "An NSG has an allow rule for TCP 3389 at priority 200 and a deny rule for TCP 3389 at "
                "priority 300. What happens to inbound RDP traffic?",
        "options": [
            {"id": "A", "text": "It is allowed, because the lower priority number (200) is processed first and matches"},
            {"id": "B", "text": "It is denied, because deny rules always win regardless of priority"},
            {"id": "C", "text": "Both rules are ignored because they conflict"},
            {"id": "D", "text": "It is allowed only if Azure Firewall also permits it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NSG rules are processed in priority order from lowest number to highest, and the first rule "
                       "that matches is applied. The allow at 200 matches before the deny at 300, so RDP is allowed.",
            "distractors": {
                "B": "NSG evaluation is by priority order, not deny-always; the first matching rule (lowest number) wins.",
                "C": "Conflicting rules are resolved by priority, not discarded.",
                "D": "NSG evaluation is independent of whether an Azure Firewall exists.",
            },
            "exam_pattern": "NSG rules process by priority (100-4096); lowest number first, first match wins.",
        },
        "references": ["Microsoft Learn (AZ-500): How network security group rules are evaluated"],
    },
    {
        "id": "az500-net-003", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "You want NSG rules that reference logical workload groups (for example, 'web' and 'db' "
                "servers) instead of hard-coded IP addresses, so the rules stay correct as VMs scale in and "
                "out. Which feature enables this?",
        "options": [
            {"id": "A", "text": "Service tags"},
            {"id": "B", "text": "User-defined routes"},
            {"id": "C", "text": "Private endpoints"},
            {"id": "D", "text": "Application security groups (ASGs)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Application security groups let you group VM NICs by workload and reference the group as the "
                       "source or destination in NSG rules, so membership (not static IPs) drives the rule.",
            "distractors": {
                "A": "Service tags represent Azure service IP ranges (for example, Storage), not your own workload-grouped VMs.",
                "B": "User-defined routes control next-hop routing, not NSG rule membership.",
                "C": "Private endpoints give a service a private IP; they do not group your VMs for NSG rules.",
            },
            "exam_pattern": "Group your own VMs by workload for NSG rules = application security groups; service tags = "
                            "Azure service ranges.",
        },
        "references": ["Microsoft Learn (AZ-500): Application security groups"],
    },
    {
        "id": "az500-net-004", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "An NSG is associated with both a subnet and the NIC of a VM in that subnet. For inbound "
                "traffic to the VM, how are the rules applied?",
        "options": [
            {"id": "A", "text": "Only the NIC NSG is evaluated"},
            {"id": "B", "text": "The subnet NSG is evaluated first, then the NIC NSG; traffic must be allowed by both"},
            {"id": "C", "text": "Only the subnet NSG is evaluated"},
            {"id": "D", "text": "The two NSGs are merged into one combined rule set"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "For inbound traffic Azure evaluates the subnet NSG first, then the NIC NSG (the reverse for "
                       "outbound); the traffic must be allowed by both to reach the VM.",
            "distractors": {
                "A": "Both NSGs apply to inbound traffic, not the NIC alone.",
                "C": "Both NSGs apply; the subnet NSG does not override the NIC NSG.",
                "D": "They are evaluated in sequence, not merged; each must allow the traffic.",
            },
            "exam_pattern": "Inbound: subnet NSG then NIC NSG (outbound is reversed); traffic must pass both.",
        },
        "references": ["Microsoft Learn (AZ-500): NSG association to subnets and network interfaces"],
    },
    {
        "id": "az500-net-005", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "Across many spoke VNets you must centrally control outbound traffic and permit connections "
                "only to a set of fully qualified domain names (FQDNs), with built-in threat-intelligence "
                "filtering. Which service is designed for this?",
        "options": [
            {"id": "A", "text": "Network security groups on each subnet"},
            {"id": "B", "text": "Application security groups"},
            {"id": "C", "text": "Azure Firewall with application rules"},
            {"id": "D", "text": "A load balancer health probe"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Azure Firewall is a managed, stateful, cloud-native firewall that supports FQDN-based "
                       "application rules and threat-intelligence-based filtering, and can be centralized for many VNets.",
            "distractors": {
                "A": "NSGs filter by IP/port 5-tuple and cannot allow by FQDN or provide centralized threat intelligence.",
                "B": "ASGs only group VMs for NSG rules; they do not filter outbound FQDN traffic.",
                "D": "A load balancer distributes traffic; it is not a filtering firewall.",
            },
            "exam_pattern": "Centralized, stateful, FQDN/threat-intel filtering across VNets = Azure Firewall; NSG = "
                            "basic per-subnet 5-tuple.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall features and rules"],
    },
    {
        "id": "az500-net-006", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 3, "type": "mcq",
        "stem": "In an Azure Firewall Policy you must allow VMs to reach https://updates.contoso.com by "
                "name, and also allow a specific TCP port to a partner IP range. Which rule types do you use, "
                "respectively?",
        "options": [
            {"id": "A", "text": "An application rule for the FQDN and a network rule for the IP/port"},
            {"id": "B", "text": "A network rule for the FQDN and an application rule for the IP/port"},
            {"id": "C", "text": "A DNAT rule for both"},
            {"id": "D", "text": "An NSG rule for both"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Firewall application rules filter by FQDN/HTTP(S)/web category, while network rules filter "
                       "by IP address, port, and protocol - so FQDN goes in an application rule and IP/port in a network rule.",
            "distractors": {
                "B": "This reverses them; FQDN/HTTP(S) filtering is an application rule and IP/port filtering is a network rule.",
                "C": "DNAT rules translate inbound traffic to internal resources; they are not for outbound allow-by-name or IP/port.",
                "D": "NSGs cannot filter by FQDN and are not Azure Firewall Policy rules.",
            },
            "exam_pattern": "Azure Firewall: application rules = FQDN/HTTP(S)/web categories; network rules = IP/port/"
                            "protocol; DNAT = inbound translation.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall rule types - application, network, NAT"],
    },
    {
        "id": "az500-net-007", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: An ________ security group (ASG) lets you group virtual machines by "
                "workload and use that group as the source or destination in network security group rules, "
                "instead of listing individual IP addresses.",
        "correct": ["application"],
        "explanation": {
            "correct": "An application security group (ASG) is a logical grouping of VM network interfaces by workload; "
                       "NSG rules reference the ASG as source or destination, so rules track membership as VMs scale.",
            "exam_pattern": "ASG = application security group; it groups your VMs for use inside NSG rules.",
        },
        "references": ["Microsoft Learn (AZ-500): Application security groups"],
    },

    # ===== az500_private_connectivity =======================================
    {
        "id": "az500-net-008", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "You must let VMs in a VNet reach an Azure Storage account over a private IP address drawn "
                "from your own address space, with the account reachable only through that private path. "
                "Which feature provides this?",
        "options": [
            {"id": "A", "text": "A service endpoint for Microsoft.Storage on the subnet"},
            {"id": "B", "text": "A private endpoint (Azure Private Link) for the storage account"},
            {"id": "C", "text": "A public IP on the storage account protected by an NSG"},
            {"id": "D", "text": "A user-defined route to the internet"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A private endpoint projects the storage account into your VNet as a network interface with a "
                       "private IP from your address space (via Azure Private Link), and public access can then be disabled.",
            "distractors": {
                "A": "A service endpoint keeps traffic on the Azure backbone, but the storage account still exposes a "
                     "public endpoint and gets no private IP in your VNet.",
                "C": "A public IP with an NSG does not create a private path; the service remains internet-facing.",
                "D": "A UDR changes routing; it does not give the service a private IP in your VNet.",
            },
            "exam_pattern": "Private IP in your VNet mapped to a specific PaaS resource = private endpoint (Private Link); "
                            "service endpoint = backbone path, still a public endpoint.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Private Link / private endpoints vs service endpoints"],
    },
    {
        "id": "az500-net-009", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "After enabling a virtual network service endpoint for Azure Storage on a subnet and "
                "restricting the storage firewall to that subnet, how does traffic to the storage account behave?",
        "options": [
            {"id": "A", "text": "The storage account receives a private IP address inside your VNet"},
            {"id": "B", "text": "Traffic traverses the public internet to reach storage"},
            {"id": "C", "text": "Traffic stays on the Azure backbone sourced from the subnet's private IPs, which the "
                               "storage firewall now allows"},
            {"id": "D", "text": "All access becomes impossible, even from the service-endpoint subnet"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A service endpoint keeps the subnet's traffic on Microsoft's backbone and lets the storage "
                       "firewall recognize and allow that subnet; the service keeps its public endpoint but is restricted to the subnet.",
            "distractors": {
                "A": "Service endpoints do not assign the service a private IP; that is a private endpoint.",
                "B": "The point of a service endpoint is to keep traffic on Microsoft's backbone, not the public internet.",
                "D": "The service-endpoint subnet is exactly what the storage firewall is configured to allow.",
            },
            "exam_pattern": "Service endpoint = optimized backbone path + subnet identity for the service firewall; the "
                            "service keeps its public endpoint.",
        },
        "references": ["Microsoft Learn (AZ-500): Virtual network service endpoints"],
    },
    {
        "id": "az500-net-010", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 1, "type": "mcq",
        "stem": "You need to let admins RDP and SSH to VMs without exposing a public IP on the VMs or "
                "opening 3389/22 to the internet, connecting instead through the Azure portal over TLS. Which "
                "service provides this?",
        "options": [
            {"id": "A", "text": "Azure Bastion"},
            {"id": "B", "text": "Azure Front Door"},
            {"id": "C", "text": "A point-to-site VPN terminated on each VM"},
            {"id": "D", "text": "A public load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Bastion is a managed PaaS jump host that brokers RDP/SSH over TLS from the portal, so VMs "
                       "need no public IP and management ports need not be exposed to the internet.",
            "distractors": {
                "B": "Front Door is a global HTTP(S) entry service, not an RDP/SSH broker.",
                "C": "A point-to-site VPN connects clients to the VNet but does not provide Bastion's browser-based, "
                     "public-IP-free RDP/SSH.",
                "D": "A public load balancer exposes endpoints; it does not provide secure management access.",
            },
            "exam_pattern": "Browser/portal RDP/SSH over TLS with no public IP on the VM = Azure Bastion.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Bastion"],
    },
    {
        "id": "az500-net-011", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 3, "type": "mcq",
        "stem": "After creating a private endpoint for an Azure SQL database, clients in the VNet still "
                "resolve the database's name to its public IP and bypass the private path. What is the "
                "correct fix?",
        "options": [
            {"id": "A", "text": "Add a public IP to the private endpoint"},
            {"id": "B", "text": "Delete the private endpoint and use a service endpoint instead"},
            {"id": "C", "text": "Open port 1433 to the internet on the SQL firewall"},
            {"id": "D", "text": "Configure DNS - an Azure Private DNS zone linked to the VNet - so the FQDN "
                               "resolves to the private endpoint's private IP"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Private endpoints require DNS integration: linking a private DNS zone (for example, "
                       "privatelink.database.windows.net) to the VNet makes the database FQDN resolve to the private IP.",
            "distractors": {
                "A": "Private endpoints use a private IP; adding a public IP contradicts the design and does not fix resolution.",
                "B": "Service endpoints do not provide a private IP and would not solve private name resolution.",
                "C": "Opening the public port is the opposite of restricting traffic to the private path.",
            },
            "exam_pattern": "Private endpoints need DNS integration (private DNS zone) so the FQDN resolves to the "
                            "private IP, or clients keep hitting the public endpoint.",
        },
        "references": ["Microsoft Learn (AZ-500): Private endpoint DNS configuration"],
    },
    {
        "id": "az500-net-012", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Compliance requires that a storage account be reachable only from within the corporate "
                "network over Private Link, with no public access at all. Which combination meets this?",
        "options": [
            {"id": "A", "text": "Leave public network access enabled and rely on SAS tokens"},
            {"id": "B", "text": "Create a private endpoint for the storage account and set Public network access to Disabled"},
            {"id": "C", "text": "Add a service endpoint and keep public access enabled"},
            {"id": "D", "text": "Rotate the account keys weekly"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A private endpoint provides the private path, and setting Public network access to Disabled on "
                       "the account removes the internet-facing endpoint, so access is private-only.",
            "distractors": {
                "A": "SAS tokens limit what a caller can do but do not remove the public network surface.",
                "C": "A service endpoint still leaves the storage account's public endpoint reachable.",
                "D": "Key rotation is good hygiene but does not restrict network exposure.",
            },
            "exam_pattern": "'Private only' = private endpoint + set Public network access to Disabled on the resource.",
        },
        "references": ["Microsoft Learn (AZ-500): Restrict storage to private endpoints / disable public network access"],
    },
    {
        "id": "az500-net-013", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "In a hub-and-spoke topology you must force all outbound internet traffic from the spoke "
                "VNets through the Azure Firewall in the hub for inspection. Which configuration accomplishes this?",
        "options": [
            {"id": "A", "text": "An NSG rule on each spoke that allows internet traffic"},
            {"id": "B", "text": "A service endpoint on each spoke subnet"},
            {"id": "C", "text": "A user-defined route on spoke subnets with 0.0.0.0/0 next hop set to the hub "
                               "firewall's private IP"},
            {"id": "D", "text": "A private endpoint in each spoke"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A user-defined route with a default route (0.0.0.0/0) whose next hop is the firewall's private "
                       "IP forces spoke egress through the hub firewall for inspection.",
            "distractors": {
                "A": "NSGs allow or deny traffic but do not redirect its next hop through the firewall.",
                "B": "Service endpoints optimize paths to Azure PaaS; they do not force internet egress through a firewall.",
                "D": "Private endpoints provide private access to a PaaS resource, not egress inspection.",
            },
            "exam_pattern": "Force egress through a firewall = UDR with default route (0.0.0.0/0) next hop = firewall private IP.",
        },
        "references": ["Microsoft Learn (AZ-500): Route traffic through Azure Firewall with UDRs (hub-and-spoke)"],
    },

    # ===== az500_edge_protection ============================================
    {
        "id": "az500-net-014", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "A web application hosted in a single Azure region needs protection against SQL injection "
                "and cross-site scripting at the HTTP layer, delivered by a regional reverse proxy. Which "
                "service provides a WAF for this?",
        "options": [
            {"id": "A", "text": "Web Application Firewall on Azure Application Gateway"},
            {"id": "B", "text": "A network security group"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Azure DDoS infrastructure protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A WAF on Azure Application Gateway inspects HTTP(S) requests with the OWASP Core Rule Set at a "
                       "regional reverse proxy, blocking SQL injection and XSS.",
            "distractors": {
                "B": "NSGs operate at L3-L4 on IP/port; they do not inspect HTTP for SQLi/XSS.",
                "C": "Bastion provides secure RDP/SSH management access, not web application protection.",
                "D": "DDoS protection mitigates volumetric network attacks, not application-layer injection.",
            },
            "exam_pattern": "L7 web protection (OWASP SQLi/XSS) regionally = WAF on Application Gateway; globally = WAF on Front Door.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Web Application Firewall on Application Gateway"],
    },
    {
        "id": "az500-net-015", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which statement best describes how the Azure Web Application Firewall detects common "
                "attacks out of the box?",
        "options": [
            {"id": "A", "text": "It encrypts the web app's database at rest"},
            {"id": "B", "text": "It applies managed rule sets based on the OWASP Core Rule Set to inspect HTTP "
                               "requests for patterns such as SQL injection and XSS"},
            {"id": "C", "text": "It requires MFA for every web request"},
            {"id": "D", "text": "It blocks traffic purely by source-IP geography and nothing else"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure WAF ships managed rule sets based on the OWASP Core Rule Set that inspect request content "
                       "for known attack patterns; you can add custom rules (rate limiting, geo-match, bot protection) on top.",
            "distractors": {
                "A": "Database encryption at rest (for example, TDE) is unrelated to WAF request inspection.",
                "C": "WAF inspects request content; it does not perform user MFA.",
                "D": "Geo-filtering is an optional custom rule, not the primary managed-rule detection mechanism.",
            },
            "exam_pattern": "WAF = managed OWASP Core Rule Set inspection, plus custom rules such as rate limiting, "
                            "geo-match, and bot protection.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure WAF managed rule sets (OWASP CRS)"],
    },
    {
        "id": "az500-net-016", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 3, "type": "mcq",
        "stem": "You need deep inspection of encrypted outbound traffic, including TLS inspection and a "
                "signature-based intrusion detection and prevention system (IDPS). Which option provides these?",
        "options": [
            {"id": "A", "text": "Azure Firewall Standard"},
            {"id": "B", "text": "A network security group with service tags"},
            {"id": "C", "text": "Azure Front Door Standard"},
            {"id": "D", "text": "Azure Firewall Premium"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Azure Firewall Premium adds TLS inspection, an IDPS signature engine, URL filtering, and web "
                       "categories beyond what the Standard tier offers.",
            "distractors": {
                "A": "Azure Firewall Standard provides FQDN and network filtering but not TLS inspection or IDPS.",
                "B": "NSGs cannot perform TLS inspection or signature-based intrusion prevention.",
                "C": "Front Door is an application-delivery/WAF service, not a TLS-inspecting network IDPS.",
            },
            "exam_pattern": "TLS inspection + IDPS + URL filtering + web categories = Azure Firewall Premium (Standard lacks these).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall Premium features (TLS inspection, IDPS)"],
    },
    {
        "id": "az500-net-017", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "An internet-facing application needs DDoS mitigation tuned to its normal traffic, with "
                "attack telemetry, alerting, and access to a rapid-response team beyond the always-on "
                "platform defense. Which option should you enable?",
        "options": [
            {"id": "A", "text": "Azure DDoS Network Protection on the virtual network"},
            {"id": "B", "text": "A network security group deny-all rule"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Transparent Data Encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure DDoS Network Protection adds adaptive tuning, attack metrics and telemetry, alerting, an "
                       "SLA, and rapid-response support on top of the free, always-on infrastructure protection.",
            "distractors": {
                "B": "An NSG cannot absorb or adaptively mitigate a volumetric DDoS attack, nor provide telemetry/alerting.",
                "C": "Bastion provides secure management access, not DDoS mitigation.",
                "D": "TDE encrypts database data at rest and is unrelated to DDoS.",
            },
            "exam_pattern": "Tuned, telemetry-rich, SLA-backed DDoS mitigation = DDoS Network Protection (or IP "
                            "Protection per-IP); basic infrastructure protection is always on, free, and untuned.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure DDoS Protection tiers"],
    },
    {
        "id": "az500-net-018", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "To shrink exposure of VM management ports you want RDP/SSH blocked by default and opened "
                "only on request, to a specific source, for a limited time, with the change audited. Which "
                "Microsoft Defender for Cloud feature provides this?",
        "options": [
            {"id": "A", "text": "Adaptive application controls"},
            {"id": "B", "text": "Azure Bastion"},
            {"id": "C", "text": "Just-in-time (JIT) VM access"},
            {"id": "D", "text": "Secure Score"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Just-in-time VM access in Defender for Cloud keeps management ports closed in the NSG/firewall "
                       "and opens them on approved request, to a specified source, for a limited window, with the action logged.",
            "distractors": {
                "A": "Adaptive application controls allowlist which applications may run; they do not open/close management ports.",
                "B": "Bastion brokers RDP/SSH but does not itself time-box NSG port openings the way JIT does; the two are complementary.",
                "D": "Secure Score measures posture; it does not gate port access.",
            },
            "exam_pattern": "On-demand, time-boxed, audited opening of management ports via NSG/firewall = Defender for "
                            "Cloud JIT VM access.",
        },
        "references": ["Microsoft Learn (AZ-500): Just-in-time virtual machine access in Defender for Cloud"],
    },
    {
        "id": "az500-net-019", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "A globally distributed web app needs a single entry point that provides global HTTP(S) "
                "load balancing, TLS offload, and an integrated WAF at the network edge. Which service fits?",
        "options": [
            {"id": "A", "text": "Azure Application Gateway (regional)"},
            {"id": "B", "text": "Azure Front Door with Web Application Firewall"},
            {"id": "C", "text": "Azure Firewall Standard"},
            {"id": "D", "text": "A regional internal load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Front Door is a global, edge-based HTTP(S) load balancer and CDN with an integrated WAF, "
                       "giving a single global entry point with TLS offload and L7 protection.",
            "distractors": {
                "A": "Application Gateway is a regional L7 load balancer/WAF, not a global edge service.",
                "C": "Azure Firewall is a network firewall, not a global HTTP(S) delivery and WAF service.",
                "D": "An internal load balancer is private and regional, not a global edge entry point.",
            },
            "exam_pattern": "Global edge L7 + WAF = Azure Front Door; regional L7 + WAF = Application Gateway.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Front Door and Web Application Firewall"],
    },
    {
        "id": "az500-net-020", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: A Web Application ________ (WAF) protects web applications at the HTTP "
                "layer from common exploits such as SQL injection and cross-site scripting, and can run on "
                "Azure Application Gateway or Azure Front Door.",
        "correct": ["firewall"],
        "explanation": {
            "correct": "A Web Application Firewall (WAF) inspects HTTP(S) requests against managed rule sets (OWASP CRS) "
                       "and custom rules to block web exploits; it runs on Application Gateway (regional) or Front Door (global).",
            "exam_pattern": "WAF = Web Application Firewall; L7 protection on App Gateway (regional) or Front Door (global).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Web Application Firewall overview"],
    },
]
