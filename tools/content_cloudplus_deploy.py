"""CompTIA Cloud+ (CV0-004) pool - Domain 2: Deployment.

Original, objective-aligned practice items for the four Deployment subtopics
tracked in CertLab:
  * cloudp_provisioning         - templates, images/golden images, bootstrapping,
                                  orchestrated provisioning.
  * cloudp_storage_deployment   - block/file/object storage, tiers, RAID levels.
  * cloudp_compute_deployment   - virtual machines, containers, serverless,
                                  hypervisors.
  * cloudp_networking_deployment - VPC/VNet and subnets, load balancers (L4/L7),
                                  CDN, site-to-site VPN, security groups.

Cloud+ is vendor-NEUTRAL: a vendor is named only as an example, never as the sole
key. build_content.py shuffles option order (seeded by id), so no key is positionally
biased; every wrong option carries a distractor note, and each item cites the public
CV0-004 objective domain it draws on. Original items only, never real exam content.
"""

QUESTIONS = [
    # ===== cloudp_provisioning ==============================================
    {
        "id": "cloudplus-dep-001", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "An operations team maintains one hardened, fully patched, pre-configured base VM image and clones "
                "every new server from it. What is this base image commonly called, and why is it used?",
        "options": [
            {"id": "A", "text": "A thin clone; it saves storage by sharing blocks"},
            {"id": "B", "text": "A golden image (master image); it ensures every instance starts from a consistent, known-good baseline"},
            {"id": "C", "text": "A snapshot; it is used only to roll a VM back in time"},
            {"id": "D", "text": "A container layer; it is used only by container runtimes"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A golden (master) image is a standardized, hardened, pre-patched template used to provision new "
                       "instances so they all begin from an identical, known-good configuration, improving consistency and speed.",
            "distractors": {
                "A": "A thin clone is a storage-efficiency technique, not the standardized build artifact described.",
                "C": "A snapshot captures a point-in-time state for rollback/backup; a golden image is a reusable deployment baseline.",
                "D": "A container layer is part of a container image; the scenario describes a full VM base image.",
            },
            "exam_pattern": "Standardized, hardened base build cloned for all new instances = golden/master image.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (images/golden images)"],
    },
    {
        "id": "cloudplus-dep-002", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "To make environment builds repeatable and auditable, a team defines all required resources in a "
                "declarative template file and has the orchestration engine create them identically every time. "
                "What is the primary benefit of this template-based provisioning?",
        "options": [
            {"id": "A", "text": "Consistent, repeatable deployments with less manual configuration drift"},
            {"id": "B", "text": "It removes the need for any network connectivity"},
            {"id": "C", "text": "It eliminates all licensing costs"},
            {"id": "D", "text": "It guarantees that no resource ever needs patching"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Template-based (declarative) provisioning produces the same resources every run, reducing manual "
                       "error and configuration drift and making deployments repeatable and auditable.",
            "distractors": {
                "B": "Provisioning still requires network connectivity to reach the cloud control plane.",
                "C": "Templates do not change licensing costs for the resources they create.",
                "D": "Templates automate creation but do not exempt the resulting systems from patching.",
            },
            "exam_pattern": "Declarative templates = repeatable, drift-free, auditable provisioning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (templates/orchestration)"],
    },
    {
        "id": "cloudplus-dep-003", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "After a new instance boots from a base image, a startup script automatically installs the latest "
                "application version and registers the node with the cluster. What is this first-boot configuration "
                "step called?",
        "options": [
            {"id": "A", "text": "Snapshotting"},
            {"id": "B", "text": "Thick provisioning"},
            {"id": "C", "text": "Bootstrapping (instance initialization)"},
            {"id": "D", "text": "Deduplication"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Bootstrapping runs initialization logic (e.g., cloud-init/user-data scripts) at first boot to finish "
                       "configuring an instance — installing software, applying settings, and joining it to a cluster.",
            "distractors": {
                "A": "Snapshotting captures a point-in-time image; it does not configure a booting instance.",
                "B": "Thick provisioning pre-allocates storage; it is unrelated to first-boot configuration.",
                "D": "Deduplication removes redundant data blocks; it has nothing to do with instance startup.",
            },
            "exam_pattern": "First-boot script that finishes configuring an instance = bootstrapping (cloud-init/user-data).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (bootstrapping)"],
    },
    {
        "id": "cloudplus-dep-004", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 3, "type": "multi",
        "stem": "An organization standardizes all deployments on a single golden image. Which TWO are genuine "
                "advantages of this approach? (Choose two.)",
        "options": [
            {"id": "A", "text": "It removes the need to ever update or re-bake the image"},
            {"id": "B", "text": "Faster provisioning because the base is already configured and patched"},
            {"id": "C", "text": "Consistency and easier compliance because every instance starts identical"},
            {"id": "D", "text": "It makes each instance automatically unique and individually tuned"},
        ],
        "correct": ["B", "C"],
        "explanation": {
            "correct": "A golden image speeds provisioning (the base is pre-built and patched) and enforces consistency, "
                       "which simplifies compliance and troubleshooting because every instance starts from the same baseline.",
            "distractors": {
                "A": "Golden images must be periodically re-baked (re-patched); they do not eliminate maintenance.",
                "D": "The point of a golden image is uniformity, not making each instance unique — that would defeat the purpose.",
            },
            "exam_pattern": "Golden image wins = speed + consistency/compliance; it still needs periodic re-baking.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (golden images)"],
    },

    # ===== cloudp_storage_deployment ========================================
    {
        "id": "cloudplus-dep-005", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A database server needs a low-latency volume it can format with its own file system and use as a "
                "raw disk. Which cloud storage type is the best fit?",
        "options": [
            {"id": "A", "text": "Block storage"},
            {"id": "B", "text": "Object storage"},
            {"id": "C", "text": "File storage (shared NFS/SMB)"},
            {"id": "D", "text": "Archive/cold storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Block storage presents raw volumes that the OS formats and mounts like a local disk, offering the "
                       "low latency and random I/O that databases and boot volumes require.",
            "distractors": {
                "B": "Object storage is accessed over HTTP APIs with a flat namespace and higher latency — poor for a database's block-level I/O.",
                "C": "File storage offers a shared file system over NFS/SMB; it is convenient for shared files but not the raw block device a database wants.",
                "D": "Archive/cold storage is optimized for cheap, rarely accessed data with slow retrieval, unsuitable for an active database.",
            },
            "exam_pattern": "Raw low-latency volume for DB/boot = block; shared file system = file; HTTP/flat objects = object.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage types (block/file/object)"],
    },
    {
        "id": "cloudplus-dep-006", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An application stores millions of images and retrieves them by a unique key through an HTTP API, "
                "with virtually unlimited scale and rich metadata per item. Which storage type is designed for this?",
        "options": [
            {"id": "A", "text": "Block storage"},
            {"id": "B", "text": "Local instance (ephemeral) storage"},
            {"id": "C", "text": "File storage"},
            {"id": "D", "text": "Object storage"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Object storage keeps data as objects (data + metadata + unique key) in a flat namespace accessed over "
                       "HTTP(S). It scales massively and suits unstructured data like images, backups, and static assets.",
            "distractors": {
                "A": "Block storage exposes raw volumes to a single instance; it is not an HTTP, infinitely scalable key-addressable store.",
                "B": "Ephemeral instance storage is temporary local disk tied to an instance's life — not a durable, scalable object store.",
                "C": "File storage provides a hierarchical shared file system, not key-addressable objects with per-object metadata at massive scale.",
            },
            "exam_pattern": "Key-addressable, HTTP API, metadata, massive scale, unstructured = object storage.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage types (object storage)"],
    },
    {
        "id": "cloudplus-dep-007", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A storage administrator configures a volume so that data is striped across disks with distributed "
                "parity, letting the array survive the loss of any single disk while keeping most capacity usable. "
                "Which RAID level is this?",
        "options": [
            {"id": "A", "text": "RAID 0"},
            {"id": "B", "text": "RAID 1"},
            {"id": "C", "text": "RAID 5"},
            {"id": "D", "text": "RAID 10"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RAID 5 stripes data with distributed parity across at least three disks, tolerating a single disk "
                       "failure while using only one disk's worth of capacity for parity — a balance of capacity and protection.",
            "distractors": {
                "A": "RAID 0 stripes with no parity or mirroring; it has zero fault tolerance and loses all data if any disk fails.",
                "B": "RAID 1 mirrors disks and uses 50% of capacity for the mirror, not distributed parity across a stripe.",
                "D": "RAID 10 combines mirroring and striping for performance and redundancy but uses 50% of capacity, not single-parity striping.",
            },
            "exam_pattern": "Striping + distributed parity, survives 1 disk, 3+ disks = RAID 5; double parity (4+ disks, survives 2) = RAID 6.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (RAID levels)"],
    },
    {
        "id": "cloudplus-dep-008", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: Moving infrequently accessed data to cheaper, slower classes (such as cool or "
                "archive) while keeping active data on fast storage to control cost is called storage ____ (one word).",
        "correct": ["tiering", "storage tiering"],
        "explanation": {
            "correct": "Storage tiering assigns data to performance/cost classes (hot, cool, archive) based on access "
                       "frequency, reducing cost for cold data while keeping active data fast.",
            "distractors": {},
            "exam_pattern": "Match data to hot/cool/archive classes by access frequency = storage tiering.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (tiers)"],
    },

    # ===== cloudp_compute_deployment ========================================
    {
        "id": "cloudplus-dep-009", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to package an application with its dependencies into a lightweight, portable unit that "
                "shares the host OS kernel and starts in seconds. Which compute technology fits best?",
        "options": [
            {"id": "A", "text": "Containers"},
            {"id": "B", "text": "Full virtual machines with separate guest operating systems"},
            {"id": "C", "text": "Bare-metal servers"},
            {"id": "D", "text": "Dedicated hardware appliances"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Containers package an app with its dependencies and share the host OS kernel, so they are lightweight "
                       "and start quickly compared with VMs that each run a full guest OS.",
            "distractors": {
                "B": "Each VM runs its own guest OS, making it heavier and slower to start than a container.",
                "C": "Bare-metal servers run directly on hardware with no packaging/portability benefit described here.",
                "D": "Dedicated hardware appliances are purpose-built devices, not a portable application packaging model.",
            },
            "exam_pattern": "Share host kernel, lightweight, fast start, dependency packaging = containers.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (containers vs VMs)"],
    },
    {
        "id": "cloudplus-dep-010", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to run event-driven functions without provisioning or managing any servers, "
                "paying only for execution time. Which compute model is this?",
        "options": [
            {"id": "A", "text": "Infrastructure as a Service (VMs)"},
            {"id": "B", "text": "Bare-metal hosting"},
            {"id": "C", "text": "Serverless (Function as a Service)"},
            {"id": "D", "text": "A dedicated host"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Serverless / FaaS runs code in response to events with no server management by the customer and bills "
                       "only for actual execution (compute time/invocations), scaling automatically to zero when idle.",
            "distractors": {
                "A": "IaaS VMs require the customer to provision and manage servers — the opposite of serverless.",
                "B": "Bare-metal hosting gives dedicated physical servers to manage, not an abstracted function runtime.",
                "D": "A dedicated host is isolated physical capacity you manage, not an event-driven, pay-per-execution model.",
            },
            "exam_pattern": "No servers to manage, event-driven, pay-per-execution, scales to zero = serverless/FaaS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (serverless)"],
    },
    {
        "id": "cloudplus-dep-011", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A company must run a specialized OS kernel module that requires full control of the guest operating "
                "system, but still wants provider-managed hardware. Which compute option is most appropriate?",
        "options": [
            {"id": "A", "text": "A serverless function"},
            {"id": "B", "text": "A virtual machine (IaaS instance)"},
            {"id": "C", "text": "A SaaS application"},
            {"id": "D", "text": "A managed container platform with no host OS access"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A virtual machine (IaaS) gives full guest-OS control — including kernel modules and custom "
                       "configuration — while the provider still operates the underlying physical hardware.",
            "distractors": {
                "A": "Serverless functions expose no OS to configure, so a custom kernel module is impossible.",
                "C": "SaaS provides a finished application with no OS access at all.",
                "D": "A managed container platform that hides the host OS would not allow installing a custom kernel module.",
            },
            "exam_pattern": "Need full guest-OS/kernel control on provider hardware = IaaS virtual machine.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (virtual machines)"],
    },
    {
        "id": "cloudplus-dep-012", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: The software layer that creates and runs virtual machines by abstracting and "
                "allocating the physical CPU, memory, and I/O to each guest is called a ____ (one word).",
        "correct": ["hypervisor"],
        "explanation": {
            "correct": "A hypervisor (virtual machine monitor) abstracts physical hardware and allocates it to multiple guest "
                       "VMs. Type 1 runs directly on hardware (bare-metal); Type 2 runs on top of a host OS.",
            "distractors": {},
            "exam_pattern": "Software that creates/runs VMs by partitioning hardware = hypervisor (Type 1 bare-metal, Type 2 hosted).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute virtualization (hypervisors)"],
    },

    # ===== cloudp_networking_deployment =====================================
    {
        "id": "cloudplus-dep-013", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An architect carves a cloud virtual network into separate subnets: a public subnet for "
                "internet-facing load balancers and a private subnet for databases with no direct internet route. "
                "What is the main security benefit of this subnetting?",
        "options": [
            {"id": "A", "text": "Network segmentation that isolates tiers and limits exposure of the database"},
            {"id": "B", "text": "It increases the MTU on all interfaces automatically"},
            {"id": "C", "text": "It removes the need for any security groups or firewalls"},
            {"id": "D", "text": "It guarantees higher bandwidth to the database"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Placing tiers in separate subnets segments the network so the database has no direct inbound internet "
                       "path, shrinking the attack surface and enforcing tier isolation.",
            "distractors": {
                "B": "Subnetting defines address ranges and routing; it does not change MTU.",
                "C": "Segmentation complements, but does not replace, security groups/firewalls — you still need them.",
                "D": "Subnet placement does not by itself guarantee more bandwidth to a resource.",
            },
            "exam_pattern": "Public vs private subnets = segmentation that isolates tiers and limits exposure.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (VPC/subnets/segmentation)"],
    },
    {
        "id": "cloudplus-dep-014", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A global website wants users to download images and videos from a nearby edge location to cut "
                "latency and offload the origin servers. Which service provides this?",
        "options": [
            {"id": "A", "text": "A VPN gateway"},
            {"id": "B", "text": "A NAT gateway"},
            {"id": "C", "text": "A DNS resolver"},
            {"id": "D", "text": "A content delivery network (CDN)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A CDN caches content at geographically distributed edge/points-of-presence so users retrieve it from a "
                       "nearby location, reducing latency and offloading the origin.",
            "distractors": {
                "A": "A VPN gateway provides encrypted connectivity between networks, not edge caching of content.",
                "B": "A NAT gateway lets private hosts reach the internet for outbound traffic; it does not cache or distribute content.",
                "C": "A DNS resolver translates names to addresses; it does not cache and serve the actual content.",
            },
            "exam_pattern": "Cache content at edge POPs near users to cut latency/offload origin = CDN.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (CDN)"],
    },
    {
        "id": "cloudplus-dep-015", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "Incoming web traffic must be spread across several identical application servers, and unhealthy "
                "servers should automatically stop receiving requests. Which component provides this, and at which "
                "layer does an application (L7) load balancer operate?",
        "options": [
            {"id": "A", "text": "A CDN; it operates at Layer 3"},
            {"id": "B", "text": "A load balancer; an L7 load balancer operates at the application layer and can route by URL/host"},
            {"id": "C", "text": "A VPN concentrator; it operates at Layer 2"},
            {"id": "D", "text": "A DNS server; it operates at Layer 4"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A load balancer distributes traffic across healthy backends using health checks. A Layer 7 (application) "
                       "load balancer understands HTTP, so it can route by URL path, host header, or cookies, whereas an L4 load "
                       "balancer routes by IP/port.",
            "distractors": {
                "A": "A CDN caches content at the edge; it is not the component health-checking a backend pool, and L3 is the network layer.",
                "C": "A VPN concentrator terminates VPN tunnels; it does not load-balance application traffic, and this is not a Layer 2 function.",
                "D": "DNS can do basic round-robin but does not health-check per request or route by URL, and name resolution is not Layer 4 load balancing.",
            },
            "exam_pattern": "Distribute with health checks = load balancer; L7 routes by HTTP (URL/host), L4 by IP/port.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (load balancers, L4 vs L7)"],
    },
    {
        "id": "cloudplus-dep-016", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise needs an encrypted, always-on connection between its on-premises data center and its "
                "cloud virtual network over the public internet. Which technology is the standard choice?",
        "options": [
            {"id": "A", "text": "A content delivery network"},
            {"id": "B", "text": "A public object-storage endpoint"},
            {"id": "C", "text": "A site-to-site VPN (IPsec tunnel)"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A site-to-site VPN builds an encrypted IPsec tunnel between the on-premises network and the cloud "
                       "VPC/VNet over the internet, extending private connectivity securely.",
            "distractors": {
                "A": "A CDN distributes cached content to users; it does not connect a data center to a VPC.",
                "B": "A public object-storage endpoint is for storing/retrieving objects, not for site-to-site network connectivity.",
                "D": "A load balancer distributes traffic among servers; it does not create an encrypted inter-site tunnel.",
            },
            "exam_pattern": "Encrypted tunnel between on-prem and cloud over the internet = site-to-site IPsec VPN.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (VPN connectivity)"],
    },
]
