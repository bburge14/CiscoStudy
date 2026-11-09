"""CompTIA Cloud+ (CV0-004) pool - Domain 6: Troubleshooting.

Original, objective-aligned practice items for the four Troubleshooting subtopics
tracked in CertLab:
  * cloudp_ts_methodology  - the CompTIA troubleshooting methodology (identify ->
                             theorize -> test -> plan -> implement -> verify ->
                             document) and escalation.
  * cloudp_ts_deployment   - template/syntax errors, service quotas/limits, stale
                             images, region/capacity failures.
  * cloudp_ts_connectivity - DNS, routing, security groups/firewalls, latency, MTU.
  * cloudp_ts_performance  - CPU, memory, storage IOPS/throughput bottlenecks.

Cloud+ is vendor-NEUTRAL: a vendor is named only as an example, never as the sole
key. build_content.py shuffles option order (seeded by id), so no key is positionally
biased; every wrong option carries a distractor note, and each item cites the public
CV0-004 objective domain it draws on. Original items only, never real exam content.
"""

QUESTIONS = [
    # ===== cloudp_ts_methodology ============================================
    {
        "id": "cloudplus-ts-001", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 1, "type": "mcq",
        "stem": "According to the CompTIA troubleshooting methodology, what is the FIRST step when a cloud issue is "
                "reported?",
        "options": [
            {"id": "A", "text": "Identify the problem (gather information; duplicate it if possible)"},
            {"id": "B", "text": "Establish a plan of action"},
            {"id": "C", "text": "Verify full system functionality"},
            {"id": "D", "text": "Document findings and outcomes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The methodology begins with Identify the problem — gather information, question users, identify "
                       "symptoms, and determine whether anything changed — before theorizing a cause.",
            "distractors": {
                "B": "Establishing a plan of action comes after you have tested and confirmed the cause, not first.",
                "C": "Verifying full functionality is near the end, after implementing the solution.",
                "D": "Documenting findings is the final step, not the first.",
            },
            "exam_pattern": "Order: Identify -> theorize cause -> test theory -> plan -> implement -> verify -> document.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology"],
    },
    {
        "id": "cloudplus-ts-002", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "mcq",
        "stem": "A technician has gathered symptoms and formed a theory that a misconfigured security group is blocking "
                "traffic. According to the methodology, what should they do NEXT?",
        "options": [
            {"id": "A", "text": "Document the outcome and close the ticket"},
            {"id": "B", "text": "Implement preventive measures"},
            {"id": "C", "text": "Test the theory to determine the cause"},
            {"id": "D", "text": "Establish a plan of action before any testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "After establishing a theory of probable cause, the next step is to test the theory to confirm or reject "
                       "the cause; if confirmed, you proceed to plan the fix.",
            "distractors": {
                "A": "Documentation is the last step, not immediately after forming a theory.",
                "B": "Preventive measures come during verification after the fix, not right after theorizing.",
                "D": "You establish a plan of action only after the theory is tested and confirmed.",
            },
            "exam_pattern": "Theory -> TEST the theory next; if unconfirmed, form a new theory or escalate.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology"],
    },
    {
        "id": "cloudplus-ts-003", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "mcq",
        "stem": "After successfully fixing a cloud outage and verifying functionality, a methodology-driven "
                "technician's final step is to:",
        "options": [
            {"id": "A", "text": "Establish a new theory of probable cause"},
            {"id": "B", "text": "Document findings, actions, and outcomes"},
            {"id": "C", "text": "Escalate to the vendor"},
            {"id": "D", "text": "Duplicate the problem again"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The last step is to document the findings, actions, and outcomes, creating a record that speeds future "
                       "troubleshooting and knowledge sharing.",
            "distractors": {
                "A": "Forming a theory is an early step, not what you do after the issue is resolved and verified.",
                "C": "Escalation happens when you cannot resolve it yourself, not as the final step after a successful fix.",
                "D": "Duplicating the problem is part of identifying it early on, not the closing step.",
            },
            "exam_pattern": "Always finish by documenting findings, actions, and outcomes.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology"],
    },
    {
        "id": "cloudplus-ts-004", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: When a problem is beyond a technician's authority, access, or expertise to resolve, "
                "the appropriate methodology action is to ____ the issue to a higher tier or the provider (one word).",
        "correct": ["escalate", "escalation"],
        "explanation": {
            "correct": "Escalation moves an issue to a higher support tier, another team, or the cloud provider when it exceeds "
                       "the current responder's access, authority, or expertise, so it still gets resolved.",
            "distractors": {},
            "exam_pattern": "Beyond your access/expertise -> escalate (don't stall).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology (escalation)"],
    },

    # ===== cloudp_ts_deployment =============================================
    {
        "id": "cloudplus-ts-005", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An automated deployment suddenly fails with 'LimitExceeded' when launching the 21st instance, though "
                "the identical template worked before. What is the most likely cause?",
        "options": [
            {"id": "A", "text": "An account service quota/limit has been reached"},
            {"id": "B", "text": "The CPU of each instance is too small"},
            {"id": "C", "text": "The object-storage bucket is in the wrong region"},
            {"id": "D", "text": "TLS 1.2 is disabled"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cloud accounts enforce service quotas/limits (e.g., max instances per region). Hitting one causes "
                       "'LimitExceeded' errors; the fix is to request a quota increase or free up/relocate resources.",
            "distractors": {
                "B": "Instance CPU size does not cause a 'LimitExceeded' error on the 21st launch; it would affect performance, not provisioning count.",
                "C": "A misplaced storage bucket would cause access/region errors, not an instance-count limit error.",
                "D": "Disabled TLS 1.2 would cause connection/security errors, not a provisioning quota error.",
            },
            "exam_pattern": "'LimitExceeded' on the Nth resource = service quota/limit; request an increase.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (quotas/limits)"],
    },
    {
        "id": "cloudplus-ts-006", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An IaC template deployment fails immediately with a parsing error pointing to a specific line before "
                "any resources are created. What should the technician check first?",
        "options": [
            {"id": "A", "text": "The data center's physical power"},
            {"id": "B", "text": "The RAID battery backup"},
            {"id": "C", "text": "The template's syntax/formatting (e.g., malformed JSON/YAML)"},
            {"id": "D", "text": "The user's monitor resolution"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A parsing error before any resource is created indicates a syntax/format problem in the template "
                       "(malformed JSON/YAML, wrong indentation, or an invalid property); validate and lint the template.",
            "distractors": {
                "A": "Physical power issues would not produce a template parsing error at a specific line.",
                "B": "A RAID battery is a storage-hardware concern, unrelated to template parsing.",
                "D": "Monitor resolution has nothing to do with template validation failures.",
            },
            "exam_pattern": "Parse/validation error before resources created = fix template syntax (JSON/YAML).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (templates)"],
    },
    {
        "id": "cloudplus-ts-007", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 2, "type": "mcq",
        "stem": "New instances launch successfully but all come up with an outdated application version and missing "
                "patches. The most likely culprit is:",
        "options": [
            {"id": "A", "text": "The load-balancer algorithm"},
            {"id": "B", "text": "A stale golden image that needs to be rebuilt/re-baked"},
            {"id": "C", "text": "The DNS TTL being too high"},
            {"id": "D", "text": "An expired TLS certificate"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "If every new instance is outdated identically, the base/golden image is stale; re-bake it with current "
                       "patches and the latest application build so new instances start current.",
            "distractors": {
                "A": "A load-balancing algorithm affects traffic distribution, not the software version baked into instances.",
                "C": "A high DNS TTL delays record changes; it does not install outdated software on new instances.",
                "D": "An expired certificate causes TLS errors, not an outdated application build on every new instance.",
            },
            "exam_pattern": "Every new instance identically outdated = stale image; re-bake the golden image.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (images)"],
    },
    {
        "id": "cloudplus-ts-008", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 3, "type": "multi",
        "stem": "A deployment to a new region fails to create resources. Which TWO are plausible deployment-stage causes "
                "to investigate? (Choose two.)",
        "options": [
            {"id": "A", "text": "A requested instance type or service is not available in that region"},
            {"id": "B", "text": "The end user chose a dark-mode theme in the console"},
            {"id": "C", "text": "The company logo image is too large"},
            {"id": "D", "text": "Insufficient quota/limits for the new region's resources"},
        ],
        "correct": ["A", "D"],
        "explanation": {
            "correct": "Region-specific failures commonly stem from a service/instance type not offered in that region, or from "
                       "fresh regional quotas/limits that must be raised before resources can be created.",
            "distractors": {
                "B": "A console theme choice has no effect on resource creation.",
                "C": "A logo image's size is irrelevant to deploying infrastructure resources.",
            },
            "exam_pattern": "New-region deploy fails -> check regional service availability and regional quotas.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (capacity/region/quota)"],
    },

    # ===== cloudp_ts_connectivity ===========================================
    {
        "id": "cloudplus-ts-009", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Users can reach a server by its IP address but not by its hostname. Which subsystem is the most likely "
                "cause?",
        "options": [
            {"id": "A", "text": "RAID array"},
            {"id": "B", "text": "Load-balancer stickiness"},
            {"id": "C", "text": "DNS name resolution"},
            {"id": "D", "text": "Disk IOPS"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reachable by IP but not by name points to DNS: a missing/incorrect record, the wrong resolver, or "
                       "propagation delay is preventing hostname-to-IP resolution.",
            "distractors": {
                "A": "A RAID array is about disk redundancy; it does not resolve hostnames.",
                "B": "Load-balancer stickiness affects session persistence, not name resolution.",
                "D": "Disk IOPS is a storage-performance metric, unrelated to DNS resolution.",
            },
            "exam_pattern": "Works by IP, fails by name = DNS problem.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (DNS)"],
    },
    {
        "id": "cloudplus-ts-010", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Two healthy instances in different subnets cannot communicate; packets are silently dropped. In cloud "
                "networking, what is the most likely first suspect to check?",
        "options": [
            {"id": "A", "text": "Security group / network ACL rules and the route table"},
            {"id": "B", "text": "The instances' CPU governor settings"},
            {"id": "C", "text": "The object-storage lifecycle policy"},
            {"id": "D", "text": "The TLS cipher-suite list"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Silently blocked traffic between subnets is most often a security group/NACL denying the port/protocol "
                       "or a missing/incorrect route in the route table; verify the allow rules and routes first.",
            "distractors": {
                "B": "CPU governor settings affect performance, not whether packets are permitted between subnets.",
                "C": "An object-storage lifecycle policy manages data retention, not inter-subnet connectivity.",
                "D": "TLS cipher suites affect encrypted session negotiation, not basic subnet reachability.",
            },
            "exam_pattern": "No traffic between subnets -> check security groups/NACLs and route tables first.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (firewall/routing)"],
    },
    {
        "id": "cloudplus-ts-011", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 3, "type": "mcq",
        "stem": "A VPN tunnel is up and small pings succeed, but large data transfers hang or fail intermittently across "
                "it. Which issue is the classic cause?",
        "options": [
            {"id": "A", "text": "An expired IAM access key"},
            {"id": "B", "text": "An MTU/fragmentation mismatch (often needing MSS clamping)"},
            {"id": "C", "text": "A stale golden image"},
            {"id": "D", "text": "A missing cost-allocation tag"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Small packets passing while large transfers stall over a tunnel is the hallmark of an MTU/fragmentation "
                       "problem: encapsulation overhead lowers the effective MTU, so oversized packets with 'don't fragment' set are "
                       "dropped. Lowering MTU or clamping MSS resolves it.",
            "distractors": {
                "A": "An expired access key causes authentication failures, not size-dependent packet loss.",
                "C": "A stale image affects software versions on instances, not packet-size behavior on a tunnel.",
                "D": "A missing tag affects cost reporting, not connectivity.",
            },
            "exam_pattern": "Small packets OK, large ones fail over a tunnel = MTU/fragmentation; fix MTU or clamp MSS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (MTU/latency)"],
    },
    {
        "id": "cloudplus-ts-012", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: The time delay for a packet to travel from source to destination, which users "
                "experience as lag and which increases with physical distance between regions, is called ____ (one word).",
        "correct": ["latency"],
        "explanation": {
            "correct": "Latency is the time delay for data to traverse the network path; it grows with distance/hops and, when "
                       "high, degrades interactive and chatty workloads. Placing resources closer to users (or using a CDN) reduces it.",
            "distractors": {},
            "exam_pattern": "Network delay experienced as lag, rising with distance = latency (reduce via proximity/CDN).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (latency)"],
    },

    # ===== cloudp_ts_performance ============================================
    {
        "id": "cloudplus-ts-013", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 2, "type": "mcq",
        "stem": "A database server's storage shows sustained 100% disk utilization with a long I/O queue, while CPU and "
                "memory are moderate. Which resource is the bottleneck?",
        "options": [
            {"id": "A", "text": "Storage I/O (IOPS/throughput)"},
            {"id": "B", "text": "CPU"},
            {"id": "C", "text": "Memory"},
            {"id": "D", "text": "DNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Saturated disk utilization with a growing I/O queue indicates a storage I/O (IOPS/throughput) "
                       "bottleneck; remedies include faster disk tiers, more provisioned IOPS, caching, or spreading I/O.",
            "distractors": {
                "B": "CPU is reported as moderate, so processing is not the constraint here.",
                "C": "Memory is moderate, so paging/exhaustion is not the indicated bottleneck.",
                "D": "DNS is a name-resolution service, not a disk-throughput constraint.",
            },
            "exam_pattern": "Disk at 100% with I/O queue = storage IOPS/throughput bottleneck.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (IOPS/throughput)"],
    },
    {
        "id": "cloudplus-ts-014", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 2, "type": "mcq",
        "stem": "An application server becomes sluggish and the OS begins heavily swapping to disk; available RAM is "
                "near zero while CPU is not maxed. Which resource is constrained?",
        "options": [
            {"id": "A", "text": "Network bandwidth"},
            {"id": "B", "text": "Disk capacity (free space)"},
            {"id": "C", "text": "Memory (RAM)"},
            {"id": "D", "text": "DNS resolution"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Near-zero free RAM with heavy swapping is a memory bottleneck; the system pages to disk, hurting "
                       "performance. Fixes include adding memory (vertical scale), tuning the app, or scaling out.",
            "distractors": {
                "A": "Network-bandwidth saturation would show as network-throughput limits, not swapping.",
                "B": "Low free disk space causes write failures, not the paging/swapping signature of memory pressure.",
                "D": "DNS-resolution issues cause name lookups to fail, not memory swapping.",
            },
            "exam_pattern": "Low free RAM + heavy swapping = memory bottleneck.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (memory)"],
    },
    {
        "id": "cloudplus-ts-015", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 2, "type": "mcq",
        "stem": "During peak load, a compute-heavy service shows sustained 100% CPU utilization and rising request "
                "latency, while memory and disk are fine. Which remediation most directly addresses the bottleneck?",
        "options": [
            {"id": "A", "text": "Increase the DNS TTL"},
            {"id": "B", "text": "Scale the compute (out by adding instances, or up to a larger CPU)"},
            {"id": "C", "text": "Enable object-storage versioning"},
            {"id": "D", "text": "Rotate the TLS certificate"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Sustained 100% CPU with latency growth is a compute bottleneck; adding instances (scale out) behind a "
                       "load balancer or moving to a larger CPU size (scale up) relieves it.",
            "distractors": {
                "A": "DNS TTL affects record caching, not CPU saturation.",
                "C": "Object-storage versioning protects data; it does not reduce CPU load.",
                "D": "Rotating a certificate addresses TLS trust, not CPU exhaustion.",
            },
            "exam_pattern": "Sustained 100% CPU + latency = compute bottleneck -> scale out/up.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (CPU)"],
    },
    {
        "id": "cloudplus-ts-016", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 3, "type": "multi",
        "stem": "A monitoring dashboard is key to diagnosing performance issues. Which TWO metrics most directly "
                "identify a storage-throughput bottleneck? (Choose two.)",
        "options": [
            {"id": "A", "text": "IOPS (I/O operations per second)"},
            {"id": "B", "text": "Disk throughput (MB/s) and I/O queue depth"},
            {"id": "C", "text": "DNS query response code"},
            {"id": "D", "text": "TLS handshake cipher"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "IOPS and disk throughput (with I/O queue depth) directly reveal storage-performance limits; when they "
                       "plateau at the volume's maximum while the queue grows, storage is the bottleneck.",
            "distractors": {
                "C": "A DNS response code reflects name-resolution success, not storage throughput.",
                "D": "A TLS cipher reflects an encryption negotiation, not disk performance.",
            },
            "exam_pattern": "Diagnose storage limits with IOPS, throughput (MB/s), and queue depth.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (storage metrics)"],
    },
]
