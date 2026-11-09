"""CompTIA Cloud+ (CV0-004) pool - Domain 1: Cloud Architecture.

Original, objective-aligned practice items for the four Cloud Architecture
subtopics tracked in CertLab:
  * cloudp_requirements          - functional vs non-functional requirements,
                                   SLAs/SLOs, data sovereignty/residency drivers.
  * cloudp_design_solutions      - service models (IaaS/PaaS/SaaS/XaaS), deployment
                                   models (public/private/hybrid/community/multi),
                                   high-availability and redundant design.
  * cloudp_capacity_scaling      - vertical vs horizontal scaling, elasticity and
                                   auto-scaling, capacity planning.
  * cloudp_integration_migration - rehost/replatform/refactor, phased vs big-bang.

Cloud+ is vendor-NEUTRAL: concepts apply across providers, and a vendor is named
only as an illustrative example, never as the sole correct answer. build_content.py
shuffles option order (seeded by id), so no key is positionally biased; every wrong
option carries a distractor note, and each item cites the public CV0-004 objective
domain it draws on. These are original items, never real or memorized exam content.
"""

QUESTIONS = [
    # ===== cloudp_requirements ==============================================
    {
        "id": "cloudplus-arch-001", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "During discovery for a new platform, an architect records that the system must sustain "
                "10,000 concurrent users, respond in under 500 ms, and stay available 99.95% of the time. "
                "How are these statements best classified?",
        "options": [
            {"id": "A", "text": "Functional requirements, because they describe features users interact with"},
            {"id": "B", "text": "Non-functional requirements, because they define quality attributes such as performance and availability"},
            {"id": "C", "text": "A business case, because it justifies the project budget"},
            {"id": "D", "text": "Acceptance test scripts, because they run after go-live"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Performance, capacity, and availability targets are non-functional (quality-of-service) "
                       "requirements: they constrain how well the system must behave rather than naming a specific feature.",
            "distractors": {
                "A": "Functional requirements describe specific behaviors or features (e.g., 'a user can reset a password'), not latency or uptime targets.",
                "C": "A business case justifies the investment; it is not a measurable system constraint.",
                "D": "Acceptance scripts are test procedures derived from requirements, not the requirements themselves.",
            },
            "exam_pattern": "Latency, throughput, uptime, scalability = non-functional (quality) requirements; specific features = functional.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements analysis (functional vs non-functional)"],
    },
    {
        "id": "cloudplus-arch-002", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A customer and provider sign a contract guaranteeing 99.9% monthly uptime and specifying "
                "service credits if the target is missed. Which document defines this commitment?",
        "options": [
            {"id": "A", "text": "An SOP (standard operating procedure)"},
            {"id": "B", "text": "An SLO (service-level objective)"},
            {"id": "C", "text": "An SLA (service-level agreement)"},
            {"id": "D", "text": "An RFC (request for change)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An SLA is the contract between provider and customer that states the measurable commitment "
                       "(e.g., 99.9% uptime) and the remedies, such as service credits, when it is not met.",
            "distractors": {
                "A": "An SOP documents how to perform a routine task; it is not a service commitment.",
                "B": "An SLO is the internal target that supports an SLA, but it is not the customer-facing contract or its penalties.",
                "D": "An RFC proposes a change to a system; it does not define an uptime guarantee.",
            },
            "exam_pattern": "SLA = the contract and its penalties; SLO = the target that rolls up into it.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (SLAs/SLOs)"],
    },
    {
        "id": "cloudplus-arch-003", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A regulation requires that a European bank's customer records are stored and processed only "
                "within the EU. Which requirement most directly drives the cloud design to use EU regions?",
        "options": [
            {"id": "A", "text": "Data sovereignty / residency"},
            {"id": "B", "text": "Horizontal scalability"},
            {"id": "C", "text": "Loose coupling"},
            {"id": "D", "text": "Thin provisioning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data sovereignty (residency) requires data to remain within a defined legal or geographic "
                       "boundary, so the architect must select regions and services that keep data in the EU.",
            "distractors": {
                "B": "Horizontal scalability concerns adding instances for load, not where data legally resides.",
                "C": "Loose coupling is a design pattern for component independence, unrelated to data location.",
                "D": "Thin provisioning is a storage-allocation technique, not a geographic constraint.",
            },
            "exam_pattern": "'Data must stay in region/country' = data sovereignty / residency requirement.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (data sovereignty/residency)"],
    },
    {
        "id": "cloudplus-arch-004", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 3, "type": "multi",
        "stem": "An architect is separating non-functional requirements from functional ones in a workshop. "
                "Which TWO of the following are non-functional requirements? (Choose two.)",
        "options": [
            {"id": "A", "text": "The platform must recover from a zone failure within 5 minutes"},
            {"id": "B", "text": "A user can upload a profile photo"},
            {"id": "C", "text": "An administrator can export a report to CSV"},
            {"id": "D", "text": "All data in transit must be encrypted with TLS 1.2 or higher"},
        ],
        "correct": ["A", "D"],
        "explanation": {
            "correct": "Recovery-time and encryption-strength targets are quality/constraint (non-functional) "
                       "requirements that govern how the system must perform and be secured, independent of any one feature.",
            "distractors": {
                "B": "Uploading a profile photo is a specific feature a user performs — a functional requirement.",
                "C": "Exporting a report is a discrete feature/behavior — a functional requirement.",
            },
            "exam_pattern": "Non-functional = the '-ilities' and constraints (recovery, security, performance); functional = specific user actions.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements analysis"],
    },

    # ===== cloudp_design_solutions ==========================================
    {
        "id": "cloudplus-arch-005", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "mcq",
        "stem": "To keep a web tier available even if an entire data-center building fails, an architect spreads "
                "identical instances across multiple availability zones behind a load balancer. Which design "
                "principle is this?",
        "options": [
            {"id": "A", "text": "Vertical scaling"},
            {"id": "B", "text": "Eliminating single points of failure (high-availability redundancy)"},
            {"id": "C", "text": "Vendor lock-in"},
            {"id": "D", "text": "Thick provisioning"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Distributing redundant instances across independent availability zones removes any single point "
                       "of failure, so the loss of one zone does not take the service down — the core of high-availability design.",
            "distractors": {
                "A": "Vertical scaling resizes one instance; it does nothing to survive the loss of an entire zone.",
                "C": "Vendor lock-in is a risk to avoid, not a resilience design principle.",
                "D": "Thick provisioning is a storage allocation method, unrelated to availability zones.",
            },
            "exam_pattern": "Spread redundant components across fault domains/AZs = remove single points of failure (HA).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — High-availability and resilient design"],
    },
    {
        "id": "cloudplus-arch-006", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "mcq",
        "stem": "Several regional hospitals that share the same regulatory and privacy requirements jointly fund "
                "and use one cloud environment restricted to their group. Which deployment model is this?",
        "options": [
            {"id": "A", "text": "Public cloud"},
            {"id": "B", "text": "Private cloud"},
            {"id": "C", "text": "Multi-cloud"},
            {"id": "D", "text": "Community cloud"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A community cloud is shared by several organizations with common concerns (compliance, mission, "
                       "or security needs) and is not open to the general public.",
            "distractors": {
                "A": "A public cloud is open to any customer over the internet, not limited to a specific group of organizations.",
                "B": "A private cloud serves a single organization exclusively, not a consortium of several.",
                "C": "Multi-cloud means one organization using more than one public provider, not several organizations sharing one environment.",
            },
            "exam_pattern": "Several orgs with shared requirements sharing one environment = community cloud.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Cloud deployment models"],
    },
    {
        "id": "cloudplus-arch-007", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 1, "type": "mcq",
        "stem": "A development team wants to deploy application code onto a managed runtime and database without "
                "provisioning or patching the underlying operating systems. Which service model best fits?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "On-premises colocation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PaaS provides a managed platform (runtime, OS, scaling, patching) so developers deploy code and "
                       "data while the provider operates everything underneath.",
            "distractors": {
                "B": "IaaS still requires the team to manage and patch the guest operating systems.",
                "C": "SaaS delivers finished applications to end users, not a platform to deploy custom code on.",
                "D": "Colocation means hosting your own hardware in a rented facility — the opposite of a managed platform.",
            },
            "exam_pattern": "Deploy your code, provider manages the OS/runtime = PaaS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Cloud service models (IaaS/PaaS/SaaS/XaaS)"],
    },
    {
        "id": "cloudplus-arch-008", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: A resilient design duplicates critical components — power, network paths, and "
                "servers — so the failure of any one does not stop the service. This duplication of components "
                "is called ____ (one word).",
        "correct": ["redundancy", "redundant"],
        "explanation": {
            "correct": "Redundancy is the duplication of critical components (often expressed as N+1 or 2N) so a single "
                       "failure does not cause an outage; it is the foundation of high-availability design.",
            "distractors": {},
            "exam_pattern": "Duplicate components so one failure doesn't cause downtime = redundancy (N+1, 2N).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Redundancy and high availability"],
    },

    # ===== cloudp_capacity_scaling ==========================================
    {
        "id": "cloudplus-arch-009", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 1, "type": "mcq",
        "stem": "As demand grows, an operations team keeps the instance size fixed but adds more identical "
                "application servers behind a load balancer. Which scaling approach is this?",
        "options": [
            {"id": "A", "text": "Vertical scaling (scaling up)"},
            {"id": "B", "text": "Scaling in"},
            {"id": "C", "text": "Horizontal scaling (scaling out)"},
            {"id": "D", "text": "Geo-replication"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Horizontal scaling (scaling out) adds more instances to share the load; combined with a load "
                       "balancer it increases capacity without resizing any single server.",
            "distractors": {
                "A": "Vertical scaling increases the resources of a single instance, which the team specifically avoided.",
                "B": "Scaling in removes instances to shed capacity — the opposite of what is happening as demand grows.",
                "D": "Geo-replication copies data across regions for resilience; it is not a method of adding compute capacity for load.",
            },
            "exam_pattern": "Add/remove instances = horizontal (out/in); resize one instance = vertical (up/down).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Scalability (horizontal vs vertical)"],
    },
    {
        "id": "cloudplus-arch-010", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "mcq",
        "stem": "A legacy database cannot be split across multiple nodes, but it needs more processing power. The "
                "team increases the CPU and memory of the single database server. Which scaling approach is this, "
                "and what is its main limitation?",
        "options": [
            {"id": "A", "text": "Horizontal scaling; limited by load-balancer throughput"},
            {"id": "B", "text": "Vertical scaling; limited by the maximum size of a single machine"},
            {"id": "C", "text": "Elastic scaling; limited by the number of availability zones"},
            {"id": "D", "text": "Geographic scaling; limited by DNS propagation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Increasing CPU/memory of one instance is vertical scaling (scaling up). Its ceiling is the largest "
                       "instance available, and resizing often requires downtime, which is why it suits workloads that cannot scale out.",
            "distractors": {
                "A": "Horizontal scaling adds instances; the scenario resizes a single server instead.",
                "C": "'Elastic scaling' describes automation of scaling, not enlarging one server, and AZ count is not its limit.",
                "D": "'Geographic scaling' is not the technique here, and DNS propagation is unrelated to resizing a server.",
            },
            "exam_pattern": "Vertical = bigger single box, capped by max machine size and usually needs a reboot.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Scalability (vertical scaling limits)"],
    },
    {
        "id": "cloudplus-arch-011", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "mcq",
        "stem": "An auto-scaling group adds instances when average CPU exceeds 70% for five minutes and removes "
                "them when CPU falls below 30%. This automatic matching of capacity to real-time demand is best "
                "described as:",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Fault tolerance"},
            {"id": "C", "text": "Vendor lock-in"},
            {"id": "D", "text": "Over-provisioning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elasticity is the automatic expansion and contraction of resources to match current demand; "
                       "metric-driven auto-scaling policies are how it is implemented.",
            "distractors": {
                "B": "Fault tolerance keeps a system running through component failures; it is not about matching capacity to load.",
                "C": "Vendor lock-in is a dependency risk, not a scaling behavior.",
                "D": "Over-provisioning means permanently allocating excess capacity — the opposite of elastically scaling to demand.",
            },
            "exam_pattern": "Automatic scale-out/scale-in to track demand = elasticity (via auto-scaling policies).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Elasticity and auto-scaling"],
    },
    {
        "id": "cloudplus-arch-012", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: The ongoing practice of forecasting future compute, storage, and network needs "
                "from growth trends so the environment is neither over- nor under-provisioned is called ____ ____ "
                "(two words).",
        "correct": ["capacity planning", "capacity-planning"],
        "explanation": {
            "correct": "Capacity planning forecasts future resource demand (from trends, baselines, and business "
                       "projections) so resources are provisioned ahead of need without wasteful over-provisioning.",
            "distractors": {},
            "exam_pattern": "Forecast future resource needs from trends/baselines = capacity planning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Capacity planning"],
    },

    # ===== cloudp_integration_migration =====================================
    {
        "id": "cloudplus-arch-013", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 1, "type": "mcq",
        "stem": "An organization moves its existing virtual machines to a provider's IaaS with no changes to the "
                "applications or operating systems, aiming to migrate quickly. Which migration strategy is this?",
        "options": [
            {"id": "A", "text": "Refactor (re-architect)"},
            {"id": "B", "text": "Replatform"},
            {"id": "C", "text": "Rehost (lift-and-shift)"},
            {"id": "D", "text": "Retire"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Rehosting, or lift-and-shift, moves workloads to the cloud essentially unchanged. It is the "
                       "fastest strategy and a common first step, though it may not exploit cloud-native efficiencies.",
            "distractors": {
                "A": "Refactoring rewrites the application for cloud-native services — far more than a no-change move.",
                "B": "Replatforming makes targeted optimizations (e.g., swapping in a managed database); the scenario changes nothing.",
                "D": "Retiring decommissions a workload rather than migrating it.",
            },
            "exam_pattern": "Move as-is, no code changes, fastest = rehost / lift-and-shift.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration strategies (rehost/replatform/refactor)"],
    },
    {
        "id": "cloudplus-arch-014", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "To take full advantage of cloud-native scaling, a team rewrites a monolithic application into "
                "containerized microservices that use managed queues and databases. Which migration strategy is this?",
        "options": [
            {"id": "A", "text": "Rehost (lift-and-shift)"},
            {"id": "B", "text": "Retain (revisit later)"},
            {"id": "C", "text": "Repurchase (move to SaaS)"},
            {"id": "D", "text": "Refactor (re-architect)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Refactoring (re-architecting) significantly changes the application's design to use cloud-native "
                       "patterns such as microservices and managed services. It is the most effort but yields the greatest cloud benefits.",
            "distractors": {
                "A": "Lift-and-shift moves the app unchanged; the scenario rewrites it substantially.",
                "B": "Retain leaves a workload where it is; nothing is rewritten.",
                "C": "Repurchase swaps the app for a SaaS product rather than re-architecting your own code.",
            },
            "exam_pattern": "Rewrite into cloud-native (microservices/managed services) = refactor / re-architect.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration strategies (refactor)"],
    },
    {
        "id": "cloudplus-arch-015", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "A risk-averse enterprise migrates workloads to the cloud in small, sequential waves, validating "
                "each wave before moving the next, instead of cutting everything over on one weekend. Which approach "
                "is this, and what is its chief advantage?",
        "options": [
            {"id": "A", "text": "Big-bang migration; it minimizes total project duration"},
            {"id": "B", "text": "Phased migration; it limits blast radius and allows rollback per wave"},
            {"id": "C", "text": "Big-bang migration; it reduces the need for coexistence/integration"},
            {"id": "D", "text": "Phased migration; it guarantees zero data-transfer costs"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A phased (staged) migration moves workloads in increments, so problems affect only the current "
                       "wave and can be rolled back, reducing risk — at the cost of a longer period of running hybrid/coexisting systems.",
            "distractors": {
                "A": "Big-bang does shorten the timeline but moves everything at once, raising risk; the scenario describes waves.",
                "C": "Big-bang avoids prolonged coexistence, but the scenario is clearly phased, not big-bang.",
                "D": "Phased migration reduces risk but does not eliminate data-transfer costs; that claim is incorrect.",
            },
            "exam_pattern": "Waves with validation/rollback = phased (lower risk, longer coexistence); one cutover = big-bang (faster, riskier).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration approaches (phased vs big-bang)"],
    },
    {
        "id": "cloudplus-arch-016", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "During a migration, a team replaces its self-managed SQL database with the provider's managed "
                "database service but leaves the application code largely unchanged. Which migration strategy best "
                "describes this?",
        "options": [
            {"id": "A", "text": "Replatform (lift-tinker-and-shift)"},
            {"id": "B", "text": "Rehost (lift-and-shift)"},
            {"id": "C", "text": "Refactor (re-architect)"},
            {"id": "D", "text": "Retire"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Replatforming makes a few targeted optimizations during the move — such as swapping a self-managed "
                       "database for a managed service — without rewriting the application. It sits between rehosting and refactoring.",
            "distractors": {
                "B": "Pure rehosting changes nothing; here the database layer is deliberately swapped for a managed service.",
                "C": "Refactoring would substantially rewrite the application, which the team avoided.",
                "D": "Retiring decommissions a workload; this one is being migrated and improved.",
            },
            "exam_pattern": "Small optimizations during move (e.g., managed DB) with no app rewrite = replatform.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration strategies (replatform)"],
    },
]
