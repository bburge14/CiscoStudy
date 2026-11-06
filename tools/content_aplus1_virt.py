"""CompTIA A+ Core 1 (220-1101) — Virtualization & Cloud Computing (4.0) EXPANSION pool.

Deepens the existing `virtualization_cloud` bank in content_aplus1.py (items
aplus1-virt-001..005) with original, objective-aligned questions covering 4.1
cloud-computing concepts (cloud_models) and 4.2 client-side virtualization.

Same authoring rules as the Cisco, Security+ and other CompTIA pools: original
scenario-based content mapped to the public 220-1101 exam objectives, never real
exam items. build_content.py shuffles option order (seeded by id), so the answer
key here is not positionally biased; each wrong option carries its own distractor
note. IDs continue at aplus1-virt-101+ so they never collide with the base pool.
"""

QUESTIONS = [
    # ===== 4.1 Cloud models ==================================================
    {
        "id": "aplus1-virt-101", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A development team wants a ready-made environment — operating system, language "
                "runtime, and a managed database already provided — so it can deploy its own code "
                "without building or maintaining any servers. Which cloud service model fits BEST?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "An on-premises bare-metal server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PaaS supplies a managed platform (OS, runtime, tools, often a database) on which the "
                       "customer deploys its OWN applications, without managing the underlying servers or OS.",
            "distractors": {
                "B": "IaaS gives raw VMs/storage/networking the customer must configure AND patch the OS on — more management than described.",
                "C": "SaaS is a finished application the provider runs end to end; the team here is deploying its own code, not using a ready app.",
                "D": "An on-premises server is not a cloud service model and requires the team to own and maintain all hardware.",
            },
            "exam_pattern": "Deploy your OWN code on a managed stack = PaaS; raw VMs you manage = IaaS; finished app = SaaS.",
        },
    },
    {
        "id": "aplus1-virt-102", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "A company rents virtual machines from an IaaS provider. In this model, which task "
                "remains the CUSTOMER's responsibility?",
        "options": [
            {"id": "A", "text": "Patching and securing the guest operating system and applications on the VMs"},
            {"id": "B", "text": "Maintaining the physical servers and storage hardware"},
            {"id": "C", "text": "Running and updating the hypervisor host"},
            {"id": "D", "text": "Providing datacenter power, cooling, and physical security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With IaaS the provider owns everything up to the hypervisor; the customer is responsible "
                       "for the guest OS, middleware, and applications — including patching and securing them.",
            "distractors": {
                "B": "Physical servers and storage are the provider's responsibility in every cloud model.",
                "C": "The hypervisor/host layer is managed by the provider in IaaS, not the tenant.",
                "D": "Facility power, cooling, and physical security are always handled by the cloud provider.",
            },
            "exam_pattern": "IaaS splits duties: provider = hardware + hypervisor; customer = guest OS + apps + data.",
        },
    },
    {
        "id": "aplus1-virt-103", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A startup's monthly cloud invoice changes each month based on exactly how many "
                "compute-hours and how many gigabytes of storage it actually used. Which cloud "
                "characteristic does this billing reflect?",
        "options": [
            {"id": "A", "text": "Metered (measured) utilization"},
            {"id": "B", "text": "Rapid elasticity"},
            {"id": "C", "text": "High availability"},
            {"id": "D", "text": "File synchronization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Metered (measured) utilization means usage is tracked and billed per unit consumed — "
                       "pay only for the compute and storage you actually use.",
            "distractors": {
                "B": "Rapid elasticity is the ability to scale resources up and down on demand, not the billing of usage.",
                "C": "High availability is about keeping the service running with minimal downtime (redundancy/failover).",
                "D": "File synchronization keeps copies of files consistent across devices; it is unrelated to pay-per-use billing.",
            },
            "exam_pattern": "Pay only for what you use / usage-based billing = metered utilization (a.k.a. measured service).",
        },
    },
    {
        "id": "aplus1-virt-104", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Several independent hospitals jointly fund and share one cloud environment that is "
                "purpose-built to meet healthcare privacy regulations common to all of them. Which "
                "cloud DEPLOYMENT model is this?",
        "options": [
            {"id": "A", "text": "Community cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Private cloud"},
            {"id": "D", "text": "Hybrid cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A community cloud is shared by several organizations that have common requirements "
                       "(here, the same compliance needs) and share the cost of a dedicated environment.",
            "distractors": {
                "B": "A public cloud is open to any customer and owned by a third-party provider, not limited to a group with shared requirements.",
                "C": "A private cloud is dedicated to a SINGLE organization, not shared among several hospitals.",
                "D": "A hybrid cloud combines private and public clouds; nothing here mixes two deployment types.",
            },
            "exam_pattern": "Shared by several orgs with common needs = community; one org only = private; open to all = public.",
        },
    },
    {
        "id": "aplus1-virt-105", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "A bank builds a cloud entirely on hardware in its own datacenter, dedicated solely "
                "to the bank, so it keeps full control for regulatory reasons. Which cloud "
                "DEPLOYMENT model is this?",
        "options": [
            {"id": "A", "text": "Private cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Community cloud"},
            {"id": "D", "text": "Hybrid cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A private cloud is owned by and dedicated to a single organization — often on its own "
                       "hardware — giving maximum control over security and compliance.",
            "distractors": {
                "B": "A public cloud is a shared, provider-owned environment open to many customers — the opposite of dedicated.",
                "C": "A community cloud is shared among several organizations with common requirements, not one bank alone.",
                "D": "A hybrid cloud combines private and public resources; this scenario describes a private cloud only.",
            },
            "exam_pattern": "Dedicated to one organization, full control = private cloud.",
        },
    },
    {
        "id": "aplus1-virt-106", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "An employee edits a document on a work laptop, and the updated file automatically "
                "appears on their phone and tablet through the same cloud service. Which cloud "
                "feature provides this?",
        "options": [
            {"id": "A", "text": "File synchronization"},
            {"id": "B", "text": "Rapid elasticity"},
            {"id": "C", "text": "Resource pooling"},
            {"id": "D", "text": "Metered utilization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File synchronization keeps a file consistent across all of a user's devices by uploading "
                       "changes to the cloud and pushing them back down to every linked device.",
            "distractors": {
                "B": "Rapid elasticity is on-demand scaling of compute resources, not keeping files in sync across devices.",
                "C": "Resource pooling is the provider serving many tenants from shared hardware — a back-end concept, not file sync.",
                "D": "Metered utilization is usage-based billing; it does not describe propagating file changes.",
            },
            "exam_pattern": "Same file auto-updates on all your devices = cloud file synchronization.",
        },
    },
    {
        "id": "aplus1-virt-107", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "An organization runs each employee's Windows desktop as a virtual machine on central "
                "servers in the datacenter; users connect to their desktop remotely from the office "
                "and from home. What is this technology called?",
        "options": [
            {"id": "A", "text": "VDI (Virtual Desktop Infrastructure)"},
            {"id": "B", "text": "SaaS (Software as a Service)"},
            {"id": "C", "text": "A Type 1 bare-metal hypervisor"},
            {"id": "D", "text": "Cloud file synchronization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VDI hosts users' desktop operating systems as VMs on centralized servers; users connect to "
                       "their virtual desktop over the network, so processing and data stay in the datacenter/cloud.",
            "distractors": {
                "B": "SaaS delivers a single finished application, not a full remote desktop environment per user.",
                "C": "A Type 1 hypervisor is the virtualization layer VDI may run on, but the named technology here is VDI itself.",
                "D": "File synchronization keeps files consistent across devices; it does not deliver whole hosted desktops.",
            },
            "exam_pattern": "User desktops hosted centrally and accessed remotely = VDI (often with thin-client endpoints).",
        },
    },
    {
        "id": "aplus1-virt-108", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "A business stops buying and owning its own servers and instead pays a predictable "
                "monthly cloud subscription. In financial terms, this shift moves spending from:",
        "options": [
            {"id": "A", "text": "Capital expenditure (CapEx) to operational expenditure (OpEx)"},
            {"id": "B", "text": "Operational expenditure (OpEx) to capital expenditure (CapEx)"},
            {"id": "C", "text": "Capital expenditure (CapEx) to hardware depreciation"},
            {"id": "D", "text": "It does not change how the costs are classified"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Buying servers is a large up-front CapEx (a capital asset purchase). A recurring cloud "
                       "subscription is an ongoing OpEx, so moving to the cloud shifts CapEx to OpEx.",
            "distractors": {
                "B": "This reverses the relationship — owning hardware is the CapEx side, and the subscription is the OpEx side.",
                "C": "Depreciation applies to owned capital assets; subscribing to the cloud replaces that asset with an operating expense.",
                "D": "The classification clearly changes: an asset purchase becomes a recurring service expense.",
            },
            "exam_pattern": "Own the hardware up front = CapEx; pay a recurring cloud subscription = OpEx.",
        },
    },
    {
        "id": "aplus1-virt-109", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "multi",
        "stem": "Which TWO statements correctly describe the PUBLIC cloud deployment model? (Choose two.)",
        "options": [
            {"id": "A", "text": "It is owned and operated by a third-party provider and reached over the internet"},
            {"id": "B", "text": "Its resources are shared externally among many unrelated customers (multitenant)"},
            {"id": "C", "text": "Its hardware is dedicated to a single organization for its exclusive use"},
            {"id": "D", "text": "Its resources are shared only internally within one company"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A public cloud is run by a third-party provider and accessed over the internet, and its "
                       "pooled resources are shared externally among many unrelated tenants.",
            "distractors": {
                "C": "Dedicating hardware to a single organization describes a PRIVATE cloud, not a public one.",
                "D": "Sharing resources only internally within one company also describes a private cloud, not public.",
            },
            "exam_pattern": "Public = third-party provider, internet-accessed, resources shared EXTERNALLY across many tenants.",
        },
    },

    # ===== 4.2 Client-side virtualization ===================================
    {
        "id": "aplus1-virt-110", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A datacenter team installs VMware ESXi directly onto a server's hardware, with no "
                "underlying Windows or Linux operating system beneath it. Which TYPE of hypervisor "
                "is this?",
        "options": [
            {"id": "A", "text": "Type 1 (bare-metal) hypervisor"},
            {"id": "B", "text": "Type 2 (hosted) hypervisor"},
            {"id": "C", "text": "A cross-architecture emulator"},
            {"id": "D", "text": "A container runtime"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 1 (bare-metal) hypervisor installs directly on the hardware and IS the lowest software "
                       "layer — ESXi, Hyper-V, and Xen are examples. There is no host OS beneath it.",
            "distractors": {
                "B": "A Type 2 (hosted) hypervisor runs as an application on top of an existing host OS (e.g., VirtualBox on Windows).",
                "C": "An emulator translates a different CPU architecture; ESXi runs same-architecture VMs natively on the metal.",
                "D": "A container runtime shares the host kernel to isolate apps, not to run full VMs on bare hardware.",
            },
            "exam_pattern": "Installs straight on hardware, no host OS = Type 1 (bare-metal); runs on a host OS = Type 2.",
        },
    },
    {
        "id": "aplus1-virt-111", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A technician tries to launch a 64-bit guest in a hypervisor and gets an error that "
                "hardware-assisted virtualization is not available. Which setting must be enabled in "
                "the workstation's UEFI/BIOS?",
        "options": [
            {"id": "A", "text": "Intel VT-x / AMD-V (hardware virtualization extensions)"},
            {"id": "B", "text": "Secure Boot"},
            {"id": "C", "text": "TPM 2.0"},
            {"id": "D", "text": "Fast Boot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Client-side virtualization requires the CPU's hardware-assisted virtualization extensions — "
                       "Intel VT-x or AMD-V — which are toggled in UEFI/BIOS and are often disabled by default.",
            "distractors": {
                "B": "Secure Boot validates boot-loader signatures; it does not provide CPU virtualization support (and can even block some hypervisors).",
                "C": "TPM 2.0 is a security module for keys/attestation; it is unrelated to running guest VMs.",
                "D": "Fast Boot shortens POST/startup; it has nothing to do with enabling virtualization.",
            },
            "exam_pattern": "'Virtualization not available' in a hypervisor → enable Intel VT-x / AMD-V in UEFI/BIOS.",
        },
    },
    {
        "id": "aplus1-virt-112", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A security analyst wants to open and observe a suspicious executable without putting "
                "the host or the network at risk. Which use of client-side virtualization fits BEST?",
        "options": [
            {"id": "A", "text": "Run it in an isolated sandbox VM that can be snapshotted and reverted"},
            {"id": "B", "text": "Run it directly on the host and rely on antivirus to catch problems"},
            {"id": "C", "text": "Run it on a thin client connected to the corporate VDI"},
            {"id": "D", "text": "Deploy it to a public PaaS platform to test it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A sandbox is an isolated VM used to detonate/observe risky software; snapshots let the analyst "
                       "revert to a clean state, and isolation keeps anything malicious away from the host and network.",
            "distractors": {
                "B": "Running unknown malware directly on the host risks the very machine you are trying to protect, antivirus or not.",
                "C": "A thin client is just a terminal into shared VDI desktops — detonating malware there endangers the hosted environment.",
                "D": "PaaS is for deploying trusted application code, not for safely isolating and analyzing malware.",
            },
            "exam_pattern": "Safely test risky/unknown software = isolated sandbox VM (snapshot, then revert).",
        },
    },
    {
        "id": "aplus1-virt-113", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 1, "type": "mcq",
        "stem": "A manufacturer must keep using a critical application that only runs on Windows XP, "
                "but all of its physical PCs now run Windows 11. What is the SAFEST way to keep the "
                "app running?",
        "options": [
            {"id": "A", "text": "Run Windows XP inside a virtual machine that hosts the legacy application"},
            {"id": "B", "text": "Dual-boot every Windows 11 PC with a second Windows XP installation"},
            {"id": "C", "text": "Connect to a public SaaS version of Windows XP"},
            {"id": "D", "text": "Reinstall Windows XP on the bare hardware of each PC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Running the unsupported legacy OS inside a VM is a core purpose of client-side virtualization: "
                       "the old app keeps working, isolated from the modern host, without downgrading the physical PCs.",
            "distractors": {
                "B": "Dual-booting means rebooting into an outdated, unpatched OS on every machine and losing access to the modern desktop while in use.",
                "C": "There is no SaaS 'Windows XP'; an operating system is not delivered as a public software-as-a-service app.",
                "D": "Putting XP back on bare hardware exposes unsupported, insecure OSes directly and wastes the modern deployment.",
            },
            "exam_pattern": "Keep legacy software/OS alive on modern hardware = run the old OS in a VM.",
        },
    },
    {
        "id": "aplus1-virt-114", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A developer on a macOS laptop needs to test a website in a Windows-only browser, so "
                "they run a full Windows guest in a VM on the Mac. Which PURPOSE of client-side "
                "virtualization does this illustrate?",
        "options": [
            {"id": "A", "text": "Cross-platform virtualization"},
            {"id": "B", "text": "Sandboxing suspicious files"},
            {"id": "C", "text": "Supporting a legacy operating system"},
            {"id": "D", "text": "Application streaming from the cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cross-platform virtualization runs an operating system different from the host's so you can use "
                       "software for another platform — here, running Windows on a Mac to test a Windows-only browser.",
            "distractors": {
                "B": "Sandboxing isolates risky/unknown software for safety; this is about running another platform's OS, not containing malware.",
                "C": "Legacy support is about keeping an OLD/unsupported OS running; current Windows on a Mac is a cross-platform need.",
                "D": "Application streaming delivers apps from a server/cloud; here a full guest OS runs locally in a VM.",
            },
            "exam_pattern": "Run a different platform's OS on your host (Windows on a Mac) = cross-platform virtualization.",
        },
    },
    {
        "id": "aplus1-virt-115", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 3, "type": "mcq",
        "stem": "A VM must appear on the physical office LAN as its own device — getting an IP address "
                "from the office DHCP router and being directly reachable by other hosts on that LAN. "
                "Which virtual network mode should be configured?",
        "options": [
            {"id": "A", "text": "Bridged networking"},
            {"id": "B", "text": "NAT networking"},
            {"id": "C", "text": "Host-only networking"},
            {"id": "D", "text": "Internal (private) networking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bridged mode connects the VM's virtual NIC straight to the physical network, so the VM gets its "
                       "own IP from the LAN's DHCP and is a first-class, directly reachable host on that LAN.",
            "distractors": {
                "B": "NAT hides the VM behind the host's IP address; the VM can reach out but is not directly reachable as its own LAN device.",
                "C": "Host-only networking creates a private link between the host and VM only, with no access to the physical LAN.",
                "D": "Internal/private networking connects VMs to each other but not to the host or the external LAN.",
            },
            "exam_pattern": "VM needs its own LAN IP, directly reachable = bridged; VM hidden behind host IP = NAT.",
        },
    },
    {
        "id": "aplus1-virt-116", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 3, "type": "mcq",
        "stem": "To run software compiled for a completely different CPU architecture (for example, an "
                "ARM program) on an x86 PC, the virtualization software must translate the guest's "
                "machine instructions. Which tool does this, as opposed to a standard VM?",
        "options": [
            {"id": "A", "text": "An emulator"},
            {"id": "B", "text": "A Type 1 bare-metal hypervisor"},
            {"id": "C", "text": "A standard virtual machine"},
            {"id": "D", "text": "A container"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An emulator imitates a DIFFERENT hardware/CPU architecture by translating its instructions, so "
                       "software built for another platform can run — at a performance cost — on the host.",
            "distractors": {
                "B": "A Type 1 hypervisor partitions the SAME architecture's hardware among VMs; it does not translate a foreign instruction set.",
                "C": "A standard VM runs a guest on the SAME CPU architecture as the host, executing instructions natively, not translating them.",
                "D": "A container shares the host kernel and architecture to isolate apps; it cannot run a foreign CPU architecture.",
            },
            "exam_pattern": "Different CPU architecture → emulator (translates instructions); same architecture → VM (runs natively).",
        },
    },
    {
        "id": "aplus1-virt-117", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "multi",
        "stem": "A technician is hardening a host that runs several guest VMs. Which TWO statements about "
                "VM security requirements are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "Each guest OS must still be patched and protected with anti-malware, just like a physical PC"},
            {"id": "B", "text": "Proper isolation keeps a compromised VM from reaching the host or the other VMs"},
            {"id": "C", "text": "Running an OS inside a VM makes that guest immune to malware"},
            {"id": "D", "text": "Guest VMs never need their own firewall because the host protects them"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A guest OS is a full operating system — it needs the same patching and anti-malware as a physical "
                       "machine — and strong isolation between VMs (and from the host) limits the blast radius if one is compromised.",
            "distractors": {
                "C": "A VM is not immune to malware; the guest OS can be infected exactly like a physical machine.",
                "D": "Each guest still needs its own OS-level security (firewall/anti-malware); the host cannot substitute for protecting the guest.",
            },
            "exam_pattern": "VM security = patch/protect EACH guest + enforce isolation; a VM is not inherently malware-proof.",
        },
    },
    {
        "id": "aplus1-virt-118", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 1, "type": "mcq",
        "stem": "After creating several virtual machines on a workstation, a technician notices the host's "
                "free disk space has dropped sharply. Why do VMs consume so much storage?",
        "options": [
            {"id": "A", "text": "Each VM stores its guest OS and data in a large virtual-disk file on the host"},
            {"id": "B", "text": "VMs store nothing locally; all of their data lives in the cloud"},
            {"id": "C", "text": "The hypervisor compresses every VM down to a few megabytes"},
            {"id": "D", "text": "Only snapshots use disk space, and snapshots are always tiny"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VM keeps its entire guest operating system and data inside a virtual hard-disk file (e.g., .vdi/"
                       ".vmdk) on the host, so each VM consumes real host storage that must be planned for.",
            "distractors": {
                "B": "Client-side VMs store their virtual disks locally on the host; they do not keep all data in the cloud.",
                "C": "Hypervisors do not shrink full guest installs to a few megabytes — a guest OS needs gigabytes of disk.",
                "D": "Snapshots add to disk use, but the main consumer is the VM's full virtual disk holding the OS and data.",
            },
            "exam_pattern": "Each VM needs host RAM, CPU, AND disk — its virtual-disk file holds the whole guest OS.",
        },
    },
]
