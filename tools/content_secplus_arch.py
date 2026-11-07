"""Security+ SY0-701 EXPANSION pool — Domain 3.0 Security Architecture.

Original, objective-aligned items that deepen the base `security_architecture`
set in content_secplus.py (which covers tokenization, data states, RPO, RAID 5,
IaaS shared responsibility, and screened-subnet segmentation). These add new
angles across all five subtopics — architecture_models,
cloud_virtualization_security, secure_design, data_protection, and
resilience_recovery — never real exam items.

Authoring rules match the base pool: build_content.py shuffles option order
(seeded by id), so the answer key here is not positionally biased, and every
wrong option carries a distractor note.
"""

QUESTIONS = [
    # ===== architecture_models ==============================================
    {
        "id": "secplus-arch-101", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 2, "type": "mcq",
        "stem": "A development team uploads small blocks of code that run only when an event "
                "fires (an HTTP request, a file upload). There are no servers or operating "
                "systems for the team to provision or patch, and they are billed only for the "
                "milliseconds each function executes. Which model is this?",
        "options": [
            {"id": "A", "text": "Serverless (Function as a Service)"},
            {"id": "B", "text": "Platform as a Service (PaaS)"},
            {"id": "C", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "D", "text": "Containerization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Serverless / FaaS runs event-triggered functions on infrastructure the "
                       "provider fully manages and auto-scales (even to zero); the customer owns "
                       "only the function code and pays per execution.",
            "distractors": {
                "B": "PaaS supplies a managed runtime/platform, but the customer still deploys and "
                     "runs a continuously-running application and manages its scaling.",
                "C": "IaaS gives VMs where the customer still provisions and patches the guest OS.",
                "D": "Containerization packages an app with its dependencies, but you still deploy "
                     "and orchestrate the running containers — it is not event-driven pay-per-run.",
            },
            "exam_pattern": "Serverless = event-driven, no server/OS management, scales to zero, "
                            "pay-per-execution. PaaS still runs a persistent app you manage.",
        },
    },
    {
        "id": "secplus-arch-102", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 2, "type": "mcq",
        "stem": "An application is decomposed into many small, independently deployable services "
                "that talk to each other over APIs, so one service can be patched or scaled "
                "without redeploying the entire application. Which architecture is this?",
        "options": [
            {"id": "A", "text": "Microservices"},
            {"id": "B", "text": "Monolithic application"},
            {"id": "C", "text": "Software-defined networking (SDN)"},
            {"id": "D", "text": "Thick (fat) client"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microservices split functionality into loosely-coupled services with their "
                       "own lifecycles, giving independent deployment/scaling and fault isolation — "
                       "but a larger API attack surface to secure.",
            "distractors": {
                "B": "A monolith is one large codebase that must be redeployed as a whole; it is the "
                     "opposite of independently deployable services.",
                "C": "SDN decouples the network control plane from the data plane — it is a network "
                     "design, not an application decomposition pattern.",
                "D": "A thick client does heavy processing locally; it describes where code runs, "
                     "not how an app is broken into services.",
            },
            "exam_pattern": "Microservices = small API-connected services, independent deploy/scale, "
                            "more endpoints to secure. Monolith = single unit redeployed together.",
        },
    },
    {
        "id": "secplus-arch-103", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 2, "type": "mcq",
        "stem": "A cloud team defines all networks, VM instances, and firewall rules in "
                "version-controlled text templates and applies them through an automated "
                "pipeline, rather than clicking through the provider console. This yields "
                "consistent, repeatable, auditable deployments. Which practice is this?",
        "options": [
            {"id": "A", "text": "Infrastructure as code (IaC)"},
            {"id": "B", "text": "Software-defined networking (SDN)"},
            {"id": "C", "text": "Containerization"},
            {"id": "D", "text": "Continuous monitoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IaC provisions and configures infrastructure from declarative, "
                       "version-controlled code, so environments are repeatable and drift/changes "
                       "are reviewable — misconfigurations can be caught before deployment.",
            "distractors": {
                "B": "SDN programmatically controls network forwarding via a controller; it governs "
                     "traffic flow, not the templated provisioning of whole environments.",
                "C": "Containerization packages applications; it is not the practice of defining "
                     "infrastructure in code.",
                "D": "Continuous monitoring watches a running environment for issues; it does not "
                     "describe building that environment from templates.",
            },
            "exam_pattern": "IaC = infrastructure defined in version-controlled templates "
                            "(repeatable, auditable, reduces configuration drift).",
        },
    },
    {
        "id": "secplus-arch-104", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 3, "type": "mcq",
        "stem": "Compared with full machine virtualization, which statement correctly describes "
                "containerization?",
        "options": [
            {"id": "A", "text": "Containers share the host operating system's kernel, so they are "
                                "more lightweight than virtual machines"},
            {"id": "B", "text": "Each container bundles its own complete, separate guest operating "
                                "system"},
            {"id": "C", "text": "Containers require a Type 1 (bare-metal) hypervisor to run"},
            {"id": "D", "text": "Containers provide stronger workload isolation than virtual "
                                "machines"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Containers are OS-level virtualization: they share the host kernel and "
                       "package only the app and its dependencies, so they start fast and use fewer "
                       "resources than full VMs.",
            "distractors": {
                "B": "Bundling a full guest OS per instance describes virtual machines, not "
                     "containers — that is exactly the overhead containers avoid.",
                "C": "Containers run on a container engine atop the host OS, not on a Type 1 "
                     "hypervisor.",
                "D": "Because they share the host kernel, containers generally provide WEAKER "
                     "isolation than VMs, which each have a separate guest OS on the hypervisor.",
            },
            "exam_pattern": "Containers share the host kernel (lightweight, weaker isolation); VMs "
                            "each run a full guest OS on a hypervisor (heavier, stronger isolation).",
        },
    },
    {
        "id": "secplus-arch-105", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 3, "type": "mcq",
        "stem": "A utility runs ICS/SCADA equipment that controls pumps and breakers. Which "
                "characteristic MOST explains why these systems are hard to secure with "
                "conventional patch management?",
        "options": [
            {"id": "A", "text": "They often run legacy, proprietary software and must stay "
                                "available, so patching is infrequent and downtime for updates is "
                                "rarely acceptable"},
            {"id": "B", "text": "They have abundant compute, making host-based security agents "
                                "trivial to deploy on every node"},
            {"id": "C", "text": "Because they are always fully air-gapped, they need no security "
                                "controls at all"},
            {"id": "D", "text": "They automatically pull and install vendor updates over the "
                                "Internet, like modern smartphones"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ICS/SCADA and many embedded/RTOS systems prioritize availability and run "
                       "aging, vendor-specific software with long certification cycles, so patching "
                       "is slow and taking them offline to update is often unacceptable.",
            "distractors": {
                "B": "These devices are usually resource-constrained; installing full endpoint "
                     "agents is often impossible, not trivial.",
                "C": "Air gaps are frequently incomplete and can be bridged (e.g., removable media); "
                     "compensating controls like segmentation are still required.",
                "D": "Industrial controllers do not auto-update over the Internet; updates are "
                     "manual, tested, and tightly scheduled.",
            },
            "exam_pattern": "OT/ICS/SCADA and embedded systems: availability-first, legacy software, "
                            "constrained resources -> protect with segmentation, not frequent patching.",
        },
    },
    # ===== cloud_virtualization_security ====================================
    {
        "id": "secplus-arch-106", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "An attacker exploits a hypervisor flaw from inside a guest VM to run code on the "
                "underlying host and reach other tenants' virtual machines. What is this attack "
                "called?",
        "options": [
            {"id": "A", "text": "VM escape"},
            {"id": "B", "text": "VM sprawl"},
            {"id": "C", "text": "Resource reuse"},
            {"id": "D", "text": "Privilege escalation within the guest"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VM escape breaks the isolation boundary between a guest and the hypervisor/"
                       "host, letting the attacker affect the host and other VMs — the most serious "
                       "virtualization threat.",
            "distractors": {
                "B": "VM sprawl is the uncontrolled growth of unmanaged VMs, not a boundary breakout.",
                "C": "Resource reuse is leftover data exposed when memory/storage is reassigned, "
                     "not escaping to the host.",
                "D": "Privilege escalation gains higher rights WITHIN a single system; VM escape "
                     "specifically crosses the guest-to-host/hypervisor boundary.",
            },
            "exam_pattern": "VM escape = guest breaks out to the hypervisor/host (isolation failure). "
                            "Patch the hypervisor and limit host exposure to mitigate.",
        },
    },
    {
        "id": "secplus-arch-107", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "Over several years a company has spun up hundreds of VMs; many are now idle, "
                "unpatched, and absent from the asset inventory, quietly expanding the attack "
                "surface. Which virtualization problem is this?",
        "options": [
            {"id": "A", "text": "VM sprawl"},
            {"id": "B", "text": "VM escape"},
            {"id": "C", "text": "Resource reuse"},
            {"id": "D", "text": "Shadow IT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VM sprawl is the uncontrolled proliferation of virtual machines that are "
                       "never decommissioned or tracked, leaving unpatched, unmonitored systems — a "
                       "management and attack-surface problem solved with lifecycle governance.",
            "distractors": {
                "B": "VM escape is an attacker breaking out of a guest to the host — a different, "
                     "active attack.",
                "C": "Resource reuse concerns leftover data on reassigned memory/storage, not the "
                     "number of VMs.",
                "D": "Shadow IT is unsanctioned technology deployed without approval; sprawl can "
                     "consist of fully sanctioned VMs that simply were never retired.",
            },
            "exam_pattern": "VM sprawl = too many untracked/unretired VMs. Control with inventory, "
                            "lifecycle policies, and decommissioning.",
        },
    },
    {
        "id": "secplus-arch-108", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "Which hypervisor type installs directly on the bare-metal hardware with no "
                "underlying host operating system and is typical for enterprise data-center "
                "virtualization?",
        "options": [
            {"id": "A", "text": "Type 1 (bare-metal) hypervisor"},
            {"id": "B", "text": "Type 2 (hosted) hypervisor"},
            {"id": "C", "text": "A container engine"},
            {"id": "D", "text": "Type 3 hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 1 hypervisor runs directly on hardware (e.g., ESXi, Hyper-V, Xen). "
                       "With no host OS beneath it, it has a smaller attack surface and better "
                       "performance — the data-center standard.",
            "distractors": {
                "B": "A Type 2 hypervisor runs as an application ON TOP of a host OS (e.g., "
                     "VirtualBox, VMware Workstation) — common on desktops, not bare metal.",
                "C": "A container engine provides OS-level virtualization on a host OS; it is not a "
                     "hypervisor at all.",
                "D": "There is no 'Type 3' hypervisor — hypervisors are classed only as Type 1 or "
                     "Type 2.",
            },
            "exam_pattern": "Type 1 = bare-metal (data center). Type 2 = hosted on a host OS "
                            "(desktop/lab). No Type 3 exists.",
        },
    },
    {
        "id": "secplus-arch-109", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "In a multi-tenant cloud, a newly provisioned instance is assigned memory and "
                "storage blocks that a previous tenant used. Because the provider did not "
                "sanitize them, the new tenant can read residual data. Which cloud risk is this?",
        "options": [
            {"id": "A", "text": "Resource reuse"},
            {"id": "B", "text": "VM escape"},
            {"id": "C", "text": "VM sprawl"},
            {"id": "D", "text": "Data sovereignty"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resource reuse (data remnants) occurs when reassigned memory or storage "
                       "still holds a prior tenant's data; providers must zero/sanitize resources "
                       "before reallocating them.",
            "distractors": {
                "B": "VM escape is actively breaking out of a guest to the host — not passively "
                     "reading leftover data on reassigned resources.",
                "C": "VM sprawl is about too many unmanaged VMs, not residual data on reused blocks.",
                "D": "Data sovereignty concerns which country's laws govern stored data, unrelated "
                     "to resource sanitization.",
            },
            "exam_pattern": "Resource reuse = leftover data on reassigned memory/storage in shared "
                            "infrastructure; mitigated by sanitizing resources on release.",
        },
    },
    {
        "id": "secplus-arch-110", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "A company builds a web application on a provider's PaaS offering. Under the "
                "shared responsibility model, which task remains the CUSTOMER's responsibility?",
        "options": [
            {"id": "A", "text": "Securing the application code and the data they deploy to the "
                                "platform"},
            {"id": "B", "text": "Patching the underlying operating system and runtime"},
            {"id": "C", "text": "Maintaining the physical servers and data-center facilities"},
            {"id": "D", "text": "Managing and patching the hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In PaaS the provider manages hardware, OS, and runtime; the customer is "
                       "responsible for the application code they write, its configuration, and the "
                       "data and access they put on the platform.",
            "distractors": {
                "B": "In PaaS the provider — not the customer — patches the OS and managed runtime.",
                "C": "The provider owns the physical infrastructure and facilities in every cloud "
                     "service model.",
                "D": "The hypervisor is the provider's responsibility; customers never manage it in "
                     "PaaS.",
            },
            "exam_pattern": "Shared responsibility: the more managed the service (SaaS>PaaS>IaaS), "
                            "the less the customer owns — but the customer ALWAYS owns their data "
                            "and access.",
        },
    },
    # ===== secure_design ====================================================
    {
        "id": "secplus-arch-111", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "To administer servers in a protected zone, staff must first connect to one "
                "hardened, heavily-logged host and launch all management sessions from there; "
                "direct connections to the servers are blocked. What is this intermediary host "
                "called?",
        "options": [
            {"id": "A", "text": "Jump server (jump box)"},
            {"id": "B", "text": "Reverse proxy"},
            {"id": "C", "text": "Load balancer"},
            {"id": "D", "text": "Honeypot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A jump server is a single hardened, monitored pivot point for administrative "
                       "access into a secured segment, shrinking and auditing the paths into "
                       "sensitive systems.",
            "distractors": {
                "B": "A reverse proxy fronts servers for client/application traffic; it is not the "
                     "controlled admin-access pivot.",
                "C": "A load balancer distributes client requests across servers for availability/"
                     "performance, not administrative access control.",
                "D": "A honeypot is a decoy to attract and study attackers, not a management "
                     "gateway for admins.",
            },
            "exam_pattern": "Jump server / bastion host = single hardened, logged hop for admin "
                            "access into a protected zone.",
        },
    },
    {
        "id": "secplus-arch-112", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "A device sits in front of several internal web servers. It receives all inbound "
                "requests from the Internet, terminates TLS, and forwards each request to the "
                "right back-end server while hiding the servers from clients. Which appliance is "
                "this?",
        "options": [
            {"id": "A", "text": "Reverse proxy"},
            {"id": "B", "text": "Forward proxy"},
            {"id": "C", "text": "Jump server"},
            {"id": "D", "text": "VPN concentrator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A reverse proxy represents the servers to inbound clients — handling TLS "
                       "offload, request routing, caching, and concealment of the back-end — the "
                       "mirror image of a forward proxy.",
            "distractors": {
                "B": "A forward proxy sits in front of internal CLIENTS to control/filter their "
                     "OUTBOUND traffic, not inbound requests to servers.",
                "C": "A jump server is an administrative pivot host, not an inline front end for "
                     "client web traffic.",
                "D": "A VPN concentrator terminates remote-access VPN tunnels; it does not proxy "
                     "web requests to back-end servers.",
            },
            "exam_pattern": "Reverse proxy = protects/represents SERVERS to inbound clients. Forward "
                            "proxy = controls internal CLIENTS' outbound access.",
        },
    },
    {
        "id": "secplus-arch-113", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "A network security appliance is configured so that if the device itself fails, "
                "all traffic through it is BLOCKED — preserving security even though it costs "
                "availability. Which failure mode is this?",
        "options": [
            {"id": "A", "text": "Fail-closed (fail-secure)"},
            {"id": "B", "text": "Fail-open"},
            {"id": "C", "text": "Active-passive high availability"},
            {"id": "D", "text": "Implicit deny"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fail-closed (fail-secure) stops traffic when the control fails, prioritizing "
                       "confidentiality/integrity over availability — appropriate where uninspected "
                       "traffic is unacceptable.",
            "distractors": {
                "B": "Fail-open does the opposite — it lets traffic pass when the device fails, "
                     "favoring availability over security.",
                "C": "Active-passive HA is a redundancy design (a standby takes over); it is not a "
                     "single device's failure behavior toward traffic.",
                "D": "Implicit deny is a rule-base default (block anything not explicitly allowed), "
                     "not what happens when the device itself fails.",
            },
            "exam_pattern": "Fail-closed = block on failure (security first). Fail-open = pass on "
                            "failure (availability first).",
        },
    },
    {
        "id": "secplus-arch-114", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "A team wants a sensor that can actively drop malicious packets in real time, so "
                "it must sit directly in the traffic path. Which device fits this requirement, "
                "as opposed to one that only passively watches a copy of the traffic and alerts?",
        "options": [
            {"id": "A", "text": "An IPS deployed inline"},
            {"id": "B", "text": "An IDS on a SPAN/mirror port"},
            {"id": "C", "text": "A passive network tap"},
            {"id": "D", "text": "A SIEM collector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An intrusion PREVENTION system must be inline so it can block/drop traffic "
                       "in real time. Being in the path means a failure or overload can affect "
                       "availability, which drives its failure-mode design.",
            "distractors": {
                "B": "An IDS watches a copy of traffic (via SPAN/mirror) out-of-band — it can only "
                     "detect and alert, not block.",
                "C": "A tap passively copies traffic for monitoring tools; it has no ability to act "
                     "on packets.",
                "D": "A SIEM aggregates and correlates logs after the fact; it is not an inline "
                     "packet-blocking sensor.",
            },
            "exam_pattern": "IPS = inline, can block (active). IDS = out-of-band on a tap/SPAN, "
                            "detect-only (passive).",
        },
    },
    {
        "id": "secplus-arch-115", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "Before any device plugged into a switch port is allowed onto the LAN, it must "
                "authenticate (via EAP) to a RADIUS server; until it does, the port grants no "
                "network access. Which standard provides this port-based access control?",
        "options": [
            {"id": "A", "text": "IEEE 802.1X"},
            {"id": "B", "text": "IEEE 802.11"},
            {"id": "C", "text": "Static MAC address filtering"},
            {"id": "D", "text": "IEEE 802.3"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.1X is port-based network access control: the supplicant (device) "
                       "authenticates via EAP through the authenticator (switch/AP) to an "
                       "authentication server (RADIUS) before the port opens.",
            "distractors": {
                "B": "802.11 is the wireless LAN standard, not the port-based authentication "
                     "framework (though 802.1X can be used over it).",
                "C": "MAC filtering only checks a hardware address, which is trivially spoofed; it "
                     "is not strong authentication.",
                "D": "802.3 defines wired Ethernet at the physical/data-link layer, not "
                     "authentication.",
            },
            "exam_pattern": "802.1X = supplicant + authenticator + authentication server (RADIUS) "
                            "with EAP; port-based NAC for wired and wireless.",
        },
    },
    # ===== data_protection ==================================================
    {
        "id": "secplus-arch-116", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "mcq",
        "stem": "A support application shows account numbers on screen as 'XXXX-XXXX-XXXX-4417', "
                "revealing only the last four digits to agents who do not need the full value. "
                "The stored record is unchanged. Which technique is this?",
        "options": [
            {"id": "A", "text": "Data masking"},
            {"id": "B", "text": "Tokenization"},
            {"id": "C", "text": "Encryption"},
            {"id": "D", "text": "Hashing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data masking hides portions of a value (often with placeholder characters) "
                       "so unauthorized viewers cannot see the full data, while authorized processes "
                       "can still use the underlying record.",
            "distractors": {
                "B": "Tokenization replaces the value with an unrelated surrogate stored in a vault; "
                     "here the real value is merely obscured on display, not swapped out.",
                "C": "Encryption transforms the whole value into ciphertext recoverable with a key — "
                     "not a partial, human-readable redaction.",
                "D": "Hashing is a one-way digest for integrity; it cannot produce a readable "
                     "'last four' view of the original.",
            },
            "exam_pattern": "Masking = hide/redact part of a value for display. Tokenization = swap "
                            "to a vaulted surrogate. Encryption = reversible with a key.",
        },
    },
    {
        "id": "secplus-arch-117", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "multi",
        "stem": "A security architect must protect data IN TRANSIT across the network. Which TWO "
                "technologies are designed for that state specifically? (Select TWO.)",
        "options": [
            {"id": "A", "text": "TLS"},
            {"id": "B", "text": "IPsec"},
            {"id": "C", "text": "Full-disk encryption (BitLocker)"},
            {"id": "D", "text": "Transparent database encryption (TDE)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "TLS secures data moving at the session/application layer, and IPsec secures "
                       "it at the network layer (VPNs); both protect data while it traverses a "
                       "network — the in-transit state.",
            "distractors": {
                "C": "Full-disk encryption protects data AT REST on a drive; it does nothing once "
                     "data leaves the host on the wire.",
                "D": "TDE encrypts database files AT REST on storage; it does not protect the data "
                     "as it moves across the network.",
            },
            "exam_pattern": "In transit -> TLS / IPsec. At rest -> full-disk / file / database "
                            "(TDE) encryption. Match the control to the data state.",
        },
    },
    {
        "id": "secplus-arch-118", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 1, "type": "mcq",
        "stem": "An organization assigns every document a sensitivity level — public, sensitive, "
                "confidential, or restricted — so that the right handling and controls are "
                "applied to each. What is this process called?",
        "options": [
            {"id": "A", "text": "Data classification"},
            {"id": "B", "text": "Data sovereignty"},
            {"id": "C", "text": "Data masking"},
            {"id": "D", "text": "Data loss prevention"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data classification assigns sensitivity levels to information so protection, "
                       "access, retention, and disposal rules can be matched to each level.",
            "distractors": {
                "B": "Data sovereignty is about which nation's laws govern data based on where it is "
                     "stored, not labeling by sensitivity.",
                "C": "Data masking obscures values for display; it is a protection technique, not "
                     "the labeling scheme that drives which controls apply.",
                "D": "DLP is the technology that enforces policy on sensitive data; classification "
                     "is what tells DLP which data is sensitive.",
            },
            "exam_pattern": "Classification = assign sensitivity labels first; those labels then "
                            "drive handling, access, and DLP policy.",
        },
    },
    {
        "id": "secplus-arch-119", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "mcq",
        "stem": "A multinational must keep certain citizens' personal data stored and processed "
                "within the country of origin, because that data is subject to the laws of the "
                "nation where it physically resides. Which concept drives this requirement?",
        "options": [
            {"id": "A", "text": "Data sovereignty"},
            {"id": "B", "text": "Data classification"},
            {"id": "C", "text": "Geographic dispersion"},
            {"id": "D", "text": "Data masking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data sovereignty means data is governed by the laws of the country where it "
                       "is located, so regulations may force storage/processing to stay within "
                       "specific borders (tied to geolocation).",
            "distractors": {
                "B": "Classification assigns sensitivity levels; it does not dictate the geographic "
                     "/legal jurisdiction of storage.",
                "C": "Geographic dispersion spreads copies across locations for resilience — a "
                     "recovery concern, not a legal-jurisdiction requirement.",
                "D": "Masking obscures values for viewing; it has nothing to do with which laws "
                     "apply to the data.",
            },
            "exam_pattern": "Data sovereignty/geolocation = whose laws govern the data based on "
                            "where it is stored; can mandate in-country residency.",
        },
    },
    {
        "id": "secplus-arch-120", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "mcq",
        "stem": "Employees keep emailing spreadsheets that contain Social Security numbers to "
                "external addresses. Security wants a system that inspects outbound content and "
                "automatically blocks or quarantines messages carrying such regulated data. "
                "Which solution fits?",
        "options": [
            {"id": "A", "text": "Data loss prevention (DLP)"},
            {"id": "B", "text": "Full-disk encryption"},
            {"id": "C", "text": "An intrusion detection system (IDS)"},
            {"id": "D", "text": "A stateful firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DLP inspects data in use, in transit, and at rest against content rules "
                       "(e.g., SSN patterns) and can block, quarantine, or alert — purpose-built to "
                       "stop sensitive data from leaving.",
            "distractors": {
                "B": "Full-disk encryption protects data at rest on a lost/stolen drive; it cannot "
                     "inspect or stop outbound email content.",
                "C": "An IDS detects and alerts on suspicious network activity; it is not designed "
                     "to recognize and block regulated data in messages.",
                "D": "A stateful firewall filters by ports/addresses/connection state, not by the "
                     "sensitive content inside allowed traffic.",
            },
            "exam_pattern": "DLP = content-aware control that blocks sensitive data exfiltration "
                            "across endpoints, network, and storage.",
        },
    },
    # ===== resilience_recovery ==============================================
    {
        "id": "secplus-arch-121", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A firm needs an alternate site that is fully equipped with hardware AND has data "
                "replicated in near-real-time, so it can take over production within minutes of a "
                "disaster — accepting the highest cost. Which recovery site is this?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Mobile site"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hot site is fully provisioned with equipment and current, replicated data, "
                       "enabling near-immediate failover — the fastest recovery and the most "
                       "expensive to maintain.",
            "distractors": {
                "B": "A warm site has hardware and connectivity but not current data, so it takes "
                     "hours (restore/sync) to bring online.",
                "C": "A cold site provides only space, power, and cooling — no equipment or data — "
                     "and takes the longest to activate, at the lowest cost.",
                "D": "A mobile site is a transportable facility; readiness varies and it is not "
                     "defined by near-real-time data replication.",
            },
            "exam_pattern": "Hot = ready now, priciest. Warm = equipped, data lag, hours. Cold = "
                            "empty shell, cheapest, slowest.",
        },
    },
    {
        "id": "secplus-arch-122", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 3, "type": "mcq",
        "stem": "Several servers are grouped so that if one node fails, another node in the group "
                "automatically assumes its workload, and the group presents to clients as one "
                "highly available system. Which technique BEST describes this (as distinct from "
                "merely spreading incoming requests across independent servers)?",
        "options": [
            {"id": "A", "text": "Clustering"},
            {"id": "B", "text": "Load balancing"},
            {"id": "C", "text": "Geographic dispersion"},
            {"id": "D", "text": "RAID"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Clustering joins nodes into a coordinated group with failover, so a surviving "
                       "node takes over a failed node's role and the cluster appears as a single "
                       "resilient service.",
            "distractors": {
                "B": "Load balancing distributes requests across servers for performance/scale; the "
                     "servers are independent and it does not by itself provide node-takeover "
                     "failover semantics.",
                "C": "Geographic dispersion places resources in different locations to survive a "
                     "site-wide event — a siting strategy, not node failover grouping.",
                "D": "RAID provides disk-level redundancy within one system, not server-to-server "
                     "workload takeover.",
            },
            "exam_pattern": "Clustering = nodes fail over to each other (one logical HA system). "
                            "Load balancing = distribute load across independent servers.",
        },
    },
    {
        "id": "secplus-arch-123", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 1, "type": "multi",
        "stem": "To keep a data center running through a utility power failure, which TWO controls "
                "work together — one bridging the immediate gap and one sustaining extended "
                "outages? (Select TWO.)",
        "options": [
            {"id": "A", "text": "Uninterruptible power supply (UPS)"},
            {"id": "B", "text": "Backup generator"},
            {"id": "C", "text": "Power distribution unit (PDU)"},
            {"id": "D", "text": "RAID array"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A UPS provides instant battery power to ride through the brief gap and allow "
                       "graceful transition, while a generator supplies longer-term power for "
                       "extended outages; together they cover both time horizons.",
            "distractors": {
                "C": "A PDU just distributes power to equipment within the rack — it adds no backup "
                     "source when utility power is lost.",
                "D": "RAID provides disk redundancy for data availability; it does nothing for power "
                     "continuity.",
            },
            "exam_pattern": "Power resilience = UPS (instant, short-term bridge) + generator "
                            "(sustained, long-term). The UPS buys time until the generator takes over.",
        },
    },
    {
        "id": "secplus-arch-124", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Before applying a risky patch, a virtualization admin captures a point-in-time "
                "image of a VM's disk and memory state so the machine can be instantly reverted "
                "if the patch breaks it. Which backup/recovery method is this?",
        "options": [
            {"id": "A", "text": "Snapshot"},
            {"id": "B", "text": "Full backup"},
            {"id": "C", "text": "Replication"},
            {"id": "D", "text": "Journaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A snapshot records a VM's state at a moment in time, allowing a fast revert "
                       "to that exact point — ideal for short-term rollback around changes like "
                       "patching (not a substitute for real backups).",
            "distractors": {
                "B": "A full backup copies all data to separate media; it is slower to take and "
                     "restore and is not the instant in-place revert described.",
                "C": "Replication continuously copies data to another system/site for availability "
                     "or DR, not a revertible point-in-time image of one VM.",
                "D": "Journaling logs changes so transactions can be replayed/rolled back; it is a "
                     "change-log mechanism, not a VM state image.",
            },
            "exam_pattern": "Snapshot = instant point-in-time state to revert to (short-term). "
                            "Backup = durable copy. Replication = ongoing copy elsewhere.",
        },
    },
]
