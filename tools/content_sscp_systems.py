"""(ISC)2 SSCP pool - Domain 7: Systems and Application Security.

Original, objective-aligned practice items for the four Systems and Application
Security subtopics tracked in CertLab:
  * sscp_malware_endpoint       - malware types (virus/worm/trojan/ransomware)
                                  and endpoint protection (EDR, application
                                  allowlisting, HIDS).
  * sscp_cloud_security         - the shared responsibility model, SaaS/PaaS/
                                  IaaS, and CASB.
  * sscp_virtualization_security- Type 1 vs Type 2 hypervisors, VM escape, and
                                  VM sprawl.
  * sscp_mobile_iot_security    - MDM/MAM, containerization, and IoT hardening.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_malware_endpoint ============================================
    {
        "id": "sscp-sys-001", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "Which type of malware is self-replicating and spreads across networks on its own, "
                "without needing to attach to a host file or rely on a user running it?",
        "options": [
            {"id": "A", "text": "Virus"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Trojan"},
            {"id": "D", "text": "Logic bomb"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A worm self-propagates across networks by exploiting vulnerabilities or weak "
                       "configurations, requiring no host file and no user action to spread.",
            "distractors": {
                "A": "A virus attaches to a host file/program and typically needs a user to execute that host to spread.",
                "C": "A trojan disguises itself as legitimate software and relies on the user to run it; it does not self-propagate.",
                "D": "A logic bomb is dormant code that triggers on a condition; it does not self-replicate across a network.",
            },
            "exam_pattern": "Self-propagating, no host file, no user action = worm.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Malware types"],
    },
    {
        "id": "sscp-sys-002", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 1, "type": "mcq",
        "stem": "Malware encrypts a victim's files and then demands a payment in exchange for the "
                "decryption key. Which category of malware is this?",
        "options": [
            {"id": "A", "text": "Spyware"},
            {"id": "B", "text": "Adware"},
            {"id": "C", "text": "Ransomware"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Ransomware encrypts data (or locks systems) and extorts payment for recovery; "
                       "robust, tested, offline backups are the key defense.",
            "distractors": {
                "A": "Spyware covertly gathers information about a user; it does not extort via encryption.",
                "B": "Adware displays unwanted advertisements and is generally not extortive.",
                "D": "A rootkit hides an attacker's presence and maintains stealthy privileged access; encryption-for-ransom is not its defining behavior.",
            },
            "exam_pattern": "Encrypt-and-extort = ransomware; defense = tested offline/immutable backups.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Ransomware"],
    },
    {
        "id": "sscp-sys-003", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "Which endpoint technology continuously records endpoint activity, detects suspicious "
                "behavior, and supports investigation and automated response, going beyond "
                "signature-based antivirus?",
        "options": [
            {"id": "A", "text": "Endpoint Detection and Response (EDR)"},
            {"id": "B", "text": "A signature-only antivirus scanner"},
            {"id": "C", "text": "A screen-saver lock"},
            {"id": "D", "text": "An uninterruptible power supply (UPS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR records endpoint telemetry, detects behavioral indicators of compromise, "
                       "and enables investigation and response (isolate, roll back, hunt) beyond static "
                       "signatures.",
            "distractors": {
                "B": "Signature-only AV detects known malware patterns but lacks EDR's behavioral detection, telemetry, and response.",
                "C": "A screen-saver lock is a basic session control, not a malware detection/response tool.",
                "D": "A UPS provides backup power; it has no role in detecting or responding to malware.",
            },
            "exam_pattern": "Behavioral detection + telemetry + response on endpoints = EDR.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Endpoint protection (EDR)"],
    },
    {
        "id": "sscp-sys-004", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 2, "type": "fill",
        "stem": "A strong endpoint-hardening technique permits ONLY explicitly approved applications to "
                "execute and blocks everything else by default. This technique is called application "
                "____ (the term that has largely replaced 'whitelisting'). Provide the missing word.",
        "correct": ["allowlisting", "allow-listing", "allow listing", "whitelisting", "white-listing"],
        "explanation": {
            "correct": "Application allowlisting (formerly whitelisting) enforces a default-deny posture: "
                       "only approved software runs, which strongly limits malware and unauthorized "
                       "programs.",
            "distractors": {},
            "exam_pattern": "Default-deny, only approved apps run = application allowlisting (whitelisting).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Application allowlisting"],
    },

    # ===== sscp_cloud_security ==============================================
    {
        "id": "sscp-sys-005", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 2, "type": "mcq",
        "stem": "In an Infrastructure as a Service (IaaS) deployment, who is responsible for patching "
                "the guest operating system and the applications running on the provisioned virtual "
                "machines?",
        "options": [
            {"id": "A", "text": "The cloud provider"},
            {"id": "B", "text": "The customer (tenant)"},
            {"id": "C", "text": "The internet service provider"},
            {"id": "D", "text": "No one; it is fully automatic"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Under IaaS, the provider secures the physical infrastructure and hypervisor, but "
                       "the customer manages and patches the guest OS, middleware, applications, and "
                       "data.",
            "distractors": {
                "A": "The provider's responsibility in IaaS stops below the guest OS; it does not patch the tenant's operating systems or apps.",
                "C": "The ISP merely provides connectivity and has no role in patching cloud workloads.",
                "D": "Patching is not automatic; the tenant owns guest-OS and application maintenance in IaaS.",
            },
            "exam_pattern": "IaaS: provider owns the infrastructure/hypervisor; customer owns guest OS, apps, and data.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud shared responsibility (IaaS)"],
    },
    {
        "id": "sscp-sys-006", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 3, "type": "mcq",
        "stem": "Under the cloud shared responsibility model, which responsibility ALWAYS remains with "
                "the customer, even when using a fully managed SaaS application?",
        "options": [
            {"id": "A", "text": "Physical security of the provider's data centers"},
            {"id": "B", "text": "Patching the underlying hypervisor"},
            {"id": "C", "text": "Their own data and the management of user access/identities"},
            {"id": "D", "text": "Maintaining the provider's network hardware"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "No matter the service model, the customer always retains responsibility for "
                       "their own data (classification, handling) and for managing user access and "
                       "identities within the service.",
            "distractors": {
                "A": "Physical data-center security is always the provider's responsibility.",
                "B": "The hypervisor is managed by the provider in all commercial cloud service models.",
                "D": "The provider owns and maintains the underlying network hardware.",
            },
            "exam_pattern": "Always the customer's, even in SaaS: data and identity/access management.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud shared responsibility (SaaS)"],
    },
    {
        "id": "sscp-sys-007", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise wants a control point that sits between its users and its cloud services "
                "to enforce security policy, give visibility into cloud usage, and detect unsanctioned "
                "'shadow IT' applications. Which solution provides this?",
        "options": [
            {"id": "A", "text": "Cloud Access Security Broker (CASB)"},
            {"id": "B", "text": "Certificate Revocation List (CRL)"},
            {"id": "C", "text": "Network Address Translation (NAT) gateway"},
            {"id": "D", "text": "KVM switch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CASB sits between users and cloud providers to enforce policy, provide "
                       "visibility into cloud usage, discover shadow IT, and apply controls such as DLP "
                       "and access governance.",
            "distractors": {
                "B": "A CRL lists revoked certificates in a PKI; it does not broker cloud access policy.",
                "C": "NAT translates IP addresses for connectivity; it does not enforce cloud-app policy or discover shadow IT.",
                "D": "A KVM switch shares input/display across machines and is unrelated to cloud governance.",
            },
            "exam_pattern": "Policy/visibility/shadow-IT control point between users and cloud = CASB.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - CASB"],
    },
    {
        "id": "sscp-sys-008", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 1, "type": "mcq",
        "stem": "A development team wants a managed environment that provides the operating system, "
                "runtime, and middleware so they only have to deploy their application code. Which "
                "cloud service model is this?",
        "options": [
            {"id": "A", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "B", "text": "Software as a Service (SaaS)"},
            {"id": "C", "text": "On-premises hosting"},
            {"id": "D", "text": "Platform as a Service (PaaS)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "PaaS provides a managed platform (OS, runtime, middleware) so developers focus "
                       "on code and data while the provider handles the underlying stack.",
            "distractors": {
                "A": "IaaS provides raw infrastructure (VMs/networking), leaving the OS and runtime for the customer to manage.",
                "B": "SaaS delivers finished applications to end users, not a platform to deploy custom code.",
                "C": "On-premises hosting means the organization manages the entire stack itself.",
            },
            "exam_pattern": "Provider manages OS/runtime, you deploy code = PaaS; raw VMs = IaaS; finished app = SaaS.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud service models"],
    },

    # ===== sscp_virtualization_security =====================================
    {
        "id": "sscp-sys-009", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 2, "type": "fill",
        "stem": "A hypervisor that runs directly on the host's bare-metal hardware with no underlying "
                "host operating system is known as a Type ____ hypervisor. Provide the number.",
        "correct": ["1", "one", "type 1", "type one"],
        "explanation": {
            "correct": "A Type 1 (bare-metal / native) hypervisor runs directly on the hardware, "
                       "offering better performance and a smaller attack surface; it is typical in "
                       "enterprise and cloud environments.",
            "distractors": {},
            "exam_pattern": "Type 1 = bare-metal (runs on hardware); Type 2 = hosted (runs on a host OS).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Hypervisor types"],
    },
    {
        "id": "sscp-sys-010", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "A developer runs virtual machines using desktop virtualization software that itself "
                "runs as an application ON TOP of an existing host operating system. Which hypervisor "
                "type is this?",
        "options": [
            {"id": "A", "text": "Type 1 (bare-metal)"},
            {"id": "B", "text": "Type 2 (hosted)"},
            {"id": "C", "text": "A microkernel"},
            {"id": "D", "text": "A unikernel"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A Type 2 (hosted) hypervisor runs as an application on top of a conventional host "
                       "OS - common for desktops, labs, and testing.",
            "distractors": {
                "A": "A Type 1 hypervisor runs directly on hardware with no host OS beneath it.",
                "C": "A microkernel is an OS kernel design, not a hypervisor hosting model.",
                "D": "A unikernel is a specialized single-purpose machine image, not the hosted-hypervisor model described.",
            },
            "exam_pattern": "Runs on top of a host OS = Type 2 (hosted); runs on hardware = Type 1 (bare-metal).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Hypervisor types"],
    },
    {
        "id": "sscp-sys-011", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "Which virtualization-specific threat occurs when malicious code running inside a guest "
                "VM breaks out of its isolation to access the hypervisor or other virtual machines on "
                "the same host?",
        "options": [
            {"id": "A", "text": "VM sprawl"},
            {"id": "B", "text": "Snapshotting"},
            {"id": "C", "text": "Thin provisioning"},
            {"id": "D", "text": "VM escape"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "VM escape is when code breaks out of the guest's isolation to reach the "
                       "hypervisor or sibling VMs - a critical risk because it defeats the primary "
                       "security boundary of virtualization.",
            "distractors": {
                "A": "VM sprawl is the uncontrolled proliferation of unmanaged VMs, an operational/governance risk, not an isolation breakout.",
                "B": "Snapshotting captures VM state at a point in time; it is a feature, not an escape attack.",
                "C": "Thin provisioning allocates storage on demand; it is a storage efficiency technique, not an attack.",
            },
            "exam_pattern": "Breaking out of the guest to the hypervisor/other VMs = VM escape (breaks the isolation boundary).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - VM escape"],
    },
    {
        "id": "sscp-sys-012", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "An organization discovers it has accumulated many virtual machines that were created "
                "ad hoc and are now untracked, unpatched, and unmanaged. What is this governance "
                "problem called?",
        "options": [
            {"id": "A", "text": "VM escape"},
            {"id": "B", "text": "Live migration"},
            {"id": "C", "text": "Clustering"},
            {"id": "D", "text": "VM sprawl"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "VM sprawl is the uncontrolled growth of virtual machines that outpaces "
                       "management, leaving unpatched, unmonitored systems that expand the attack "
                       "surface.",
            "distractors": {
                "A": "VM escape is a technical isolation-breakout attack, not an inventory/governance issue.",
                "B": "Live migration moves a running VM between hosts; it is a feature, not the sprawl problem.",
                "C": "Clustering groups hosts for availability/scale; it is not uncontrolled VM proliferation.",
            },
            "exam_pattern": "Too many unmanaged/unpatched VMs created ad hoc = VM sprawl.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - VM sprawl"],
    },

    # ===== sscp_mobile_iot_security =========================================
    {
        "id": "sscp-sys-013", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 1, "type": "mcq",
        "stem": "Which solution lets an organization centrally enforce encryption, passcode policy, "
                "configuration, and remote wipe across the fleet of employee smartphones and tablets?",
        "options": [
            {"id": "A", "text": "Mobile Device Management (MDM)"},
            {"id": "B", "text": "Dynamic Host Configuration Protocol (DHCP)"},
            {"id": "C", "text": "Network Time Protocol (NTP)"},
            {"id": "D", "text": "A Certificate Revocation List (CRL)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MDM centrally manages mobile devices - enforcing encryption, passcodes, and "
                       "configuration profiles, and enabling remote lock/wipe of lost or stolen "
                       "devices.",
            "distractors": {
                "B": "DHCP assigns IP addresses; it does not manage device security policy.",
                "C": "NTP synchronizes clocks; it has no device-management function.",
                "D": "A CRL lists revoked certificates in a PKI; it is unrelated to managing mobile devices.",
            },
            "exam_pattern": "Central mobile policy + remote wipe = MDM (MAM manages the apps/data specifically).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Mobile device management"],
    },
    {
        "id": "sscp-sys-014", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 2, "type": "mcq",
        "stem": "On a BYOD smartphone, which approach keeps corporate apps and data in a separate, "
                "encrypted, centrally managed space that is isolated from the user's personal apps and "
                "data?",
        "options": [
            {"id": "A", "text": "Jailbreaking the device"},
            {"id": "B", "text": "Rooting the device"},
            {"id": "C", "text": "Containerization"},
            {"id": "D", "text": "Bluetooth pairing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Containerization creates an isolated, encrypted, managed workspace for corporate "
                       "apps/data on a personal device, so the organization can control and wipe work "
                       "data without touching personal content.",
            "distractors": {
                "A": "Jailbreaking removes vendor restrictions on iOS and weakens security - the opposite of a protective control.",
                "B": "Rooting grants privileged control on Android and similarly undermines the device's security model.",
                "D": "Bluetooth pairing connects peripherals; it does not isolate corporate data from personal data.",
            },
            "exam_pattern": "Separate, encrypted, managed work space on a BYOD device = containerization.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Mobile containerization (BYOD)"],
    },
    {
        "id": "sscp-sys-015", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 2, "type": "multi",
        "stem": "A facilities team is deploying many IoT sensors on the corporate network. Which TWO "
                "practices most directly reduce the security risk these devices introduce? (Choose "
                "two.)",
        "options": [
            {"id": "A", "text": "Change the default/vendor-supplied credentials on each device"},
            {"id": "B", "text": "Place the IoT devices on a segmented (isolated) network or VLAN"},
            {"id": "C", "text": "Expose each device's administrative interface directly to the internet for convenience"},
            {"id": "D", "text": "Disable all firmware updates to maximize uptime"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Changing default credentials closes a very common IoT attack path, and placing "
                       "IoT devices on a segmented network limits the damage if one is compromised - "
                       "two foundational IoT hardening steps.",
            "distractors": {
                "C": "Exposing admin interfaces to the internet dramatically increases risk and is a frequent cause of IoT compromise.",
                "D": "Disabling firmware updates leaves known vulnerabilities unpatched, increasing risk rather than reducing it.",
            },
            "exam_pattern": "IoT hardening basics: change default credentials + segment the devices; never expose admin interfaces or skip patching.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - IoT security"],
    },
]
