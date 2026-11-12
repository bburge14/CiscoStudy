"""CompTIA Cloud+ (CV0-004) pool - Round 2 (deepening bank).

Original, objective-aligned practice items that EXTEND the round-1 Cloud+ pools
(content_cloudplus_arch/deploy/ops/security/devops/ts.py). Every item here is new
and non-duplicative versus round 1: it either covers a concept round 1 did not
touch, or frames a shared concept through a distinct scenario with a different key.

Coverage is distributed by the published CV0-004 domain weighting:
  * cloudp_architecture    (~23%) - ids cloudplus-arch-r2-*
  * cloudp_deployment      (~19%) - ids cloudplus-dep-r2-*
  * cloudp_security        (~19%) - ids cloudplus-sec-r2-*
  * cloudp_operations      (~17%) - ids cloudplus-ops-r2-*
  * cloudp_troubleshooting (~12%) - ids cloudplus-ts-r2-*
  * cloudp_devops          (~10%) - ids cloudplus-dev-r2-*

Cloud+ is vendor-NEUTRAL: concepts apply across providers, and a vendor/tool is
named only as an illustrative example, never as the sole correct answer. The
official CV0-004 migration terms are rehost/replatform/re-architect/refactor/
retain/retire; "repurchase" appears only as a distractor, never as a key.

build_content.py shuffles option order (seeded by id), so no key is positionally
biased; every wrong option carries a distractor note, and each item cites the
public CV0-004 objective domain it draws on. Original items only, never real or
memorized exam content.
"""

QUESTIONS = [
    # ===================================================================
    # Domain 1: Cloud Architecture  (cloudp_architecture)
    # ===================================================================

    # ----- cloudp_requirements -----------------------------------------
    {
        "id": "cloudplus-arch-r2-001", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "During project intake, a sponsor states the platform must return its investment within 18 months "
                "and must not exceed a $200,000 annual operating budget. How are these statements best classified?",
        "options": [
            {"id": "A", "text": "Functional requirements"},
            {"id": "B", "text": "Business requirements"},
            {"id": "C", "text": "Non-functional (quality) requirements"},
            {"id": "D", "text": "Acceptance criteria"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ROI targets and budget ceilings are business requirements: they express the organizational and "
                       "financial goals the solution must satisfy, independent of any technical feature or quality attribute.",
            "distractors": {
                "A": "Functional requirements describe specific system behaviors (e.g., 'a user can reset a password'), not financial goals.",
                "C": "Non-functional requirements constrain quality attributes such as performance or availability, not budget or ROI.",
                "D": "Acceptance criteria are the testable conditions for sign-off, derived from requirements — not the business goals themselves.",
            },
            "exam_pattern": "ROI, budget, time-to-market, regulatory drivers = business requirements.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements analysis (business requirements)"],
    },
    {
        "id": "cloudplus-arch-r2-002", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A requirement states that the solution must be able to move to a different cloud provider later with "
                "minimal rework. Which non-functional requirement is being specified?",
        "options": [
            {"id": "A", "text": "Interoperability"},
            {"id": "B", "text": "Scalability"},
            {"id": "C", "text": "Portability"},
            {"id": "D", "text": "Elasticity"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Portability is the ability to move a workload between environments or providers with little change; "
                       "designing for it (open standards, containers, avoiding proprietary lock-in) satisfies this requirement.",
            "distractors": {
                "A": "Interoperability is the ability of systems to exchange and use data with each other, not to relocate between providers.",
                "B": "Scalability is the ability to grow to handle more load, not to move providers.",
                "D": "Elasticity is the automatic matching of resources to demand, unrelated to cross-provider relocation.",
            },
            "exam_pattern": "Move between providers/environments with minimal rework = portability (counters vendor lock-in).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (portability)"],
    },
    {
        "id": "cloudplus-arch-r2-003", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A requirement states that the new cloud ordering system must exchange data with the company's "
                "existing on-premises ERP using standard APIs and data formats. Which quality attribute is this?",
        "options": [
            {"id": "A", "text": "Portability"},
            {"id": "B", "text": "Interoperability"},
            {"id": "C", "text": "Redundancy"},
            {"id": "D", "text": "Latency"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Interoperability is the capability of different systems to communicate and use each other's data via "
                       "agreed interfaces/standards; integrating the cloud app with the on-prem ERP depends on it.",
            "distractors": {
                "A": "Portability concerns relocating a workload, not two systems exchanging data while each stays in place.",
                "C": "Redundancy is duplication for availability, not system-to-system data exchange.",
                "D": "Latency is network delay, a performance metric, not the ability to integrate systems.",
            },
            "exam_pattern": "Different systems must exchange/use each other's data via standards = interoperability.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (interoperability)"],
    },
    {
        "id": "cloudplus-arch-r2-004", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A retailer specifies that, without redesign, the platform must absorb a 4x jump in traffic during "
                "seasonal sales and then return to normal. Which non-functional requirement does this describe?",
        "options": [
            {"id": "A", "text": "Availability requirement"},
            {"id": "B", "text": "Scalability requirement"},
            {"id": "C", "text": "Portability requirement"},
            {"id": "D", "text": "Recoverability requirement"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The ability to grow (and later shrink) to handle a large, known increase in load without re-architecting "
                       "is a scalability requirement; it drives choices such as stateless tiers and auto-scaling.",
            "distractors": {
                "A": "An availability requirement specifies uptime (e.g., 99.95%), not the ability to absorb a traffic surge.",
                "C": "A portability requirement is about moving between providers, not handling load growth.",
                "D": "A recoverability requirement concerns restoring after failure (RTO/RPO), not scaling for demand.",
            },
            "exam_pattern": "Handle a large increase in load without redesign = scalability requirement.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (scalability)"],
    },
    {
        "id": "cloudplus-arch-r2-005", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: A documented set of normal, expected performance and utilization measurements, "
                "captured so future readings can be compared against 'normal' to spot anomalies and plan capacity, "
                "is called a ____ (one word).",
        "correct": ["baseline"],
        "explanation": {
            "correct": "A baseline records normal operating metrics (CPU, memory, latency, throughput) so deviations stand out "
                       "and capacity trends can be forecast; it is the reference point for monitoring and capacity planning.",
            "distractors": {},
            "exam_pattern": "Reference set of 'normal' metrics for comparison/forecasting = baseline.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (baselines)"],
    },
    {
        "id": "cloudplus-arch-r2-006", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_requirements", "difficulty": 2, "type": "mcq",
        "stem": "A company already owns perpetual licenses for a commercial database and wants to apply them to "
                "instances it runs in a provider's cloud rather than paying the provider's bundled license fee. Which "
                "licensing model enables this?",
        "options": [
            {"id": "A", "text": "Bring Your Own License (BYOL)"},
            {"id": "B", "text": "Pay-as-you-go (license included)"},
            {"id": "C", "text": "Open-source (no license required)"},
            {"id": "D", "text": "Per-socket perpetual on-premises only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BYOL lets an organization apply licenses it already owns to cloud workloads, often reducing cost when "
                       "existing entitlements can be reused instead of renting provider-bundled licenses.",
            "distractors": {
                "B": "Pay-as-you-go bundles the license into the hourly price; the company is instead reusing licenses it owns.",
                "C": "The database is commercial/licensed, so 'no license required' does not apply.",
                "D": "Perpetual on-prem-only licensing would not permit cloud use; BYOL mobility rights are what allow it.",
            },
            "exam_pattern": "Reuse licenses you already own in the cloud = BYOL.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Requirements (licensing models/BYOL)"],
    },

    # ----- cloudp_design_solutions -------------------------------------
    {
        "id": "cloudplus-arch-r2-007", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 1, "type": "mcq",
        "stem": "A team wants to rent virtual machines, virtual networks, and block storage, and is willing to install "
                "and patch the guest operating systems and everything above them. Which service model is this?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "FaaS (Function as a Service)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "IaaS provides fundamental compute, network, and storage building blocks; the customer manages the guest "
                       "OS, middleware, runtime, and applications while the provider runs the physical infrastructure.",
            "distractors": {
                "A": "PaaS hides the OS/runtime so developers only deploy code and data — the team here wants OS control.",
                "C": "SaaS delivers a finished application to end users, with no VMs or OS to manage.",
                "D": "FaaS runs event-driven functions with no servers or OS to manage, the opposite of renting and patching VMs.",
            },
            "exam_pattern": "Rent raw compute/network/storage and manage the OS yourself = IaaS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Cloud service models (IaaS)"],
    },
    {
        "id": "cloudplus-arch-r2-008", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 1, "type": "mcq",
        "stem": "A small business wants to use a fully managed email and CRM product through a web browser, with the "
                "provider responsible for all infrastructure, updates, and the application itself. Which service model "
                "is this?",
        "options": [
            {"id": "A", "text": "SaaS (Software as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "D", "text": "DBaaS (Database as a Service)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SaaS delivers complete, ready-to-use applications over the network; the provider manages everything "
                       "from the hardware up to the application, and the customer only configures and uses it.",
            "distractors": {
                "B": "PaaS supplies a platform to build and run custom code, not a finished email/CRM application.",
                "C": "IaaS supplies infrastructure the customer must build applications on; it is not a turnkey app.",
                "D": "DBaaS is a managed database service; it is not a complete email/CRM application for end users.",
            },
            "exam_pattern": "Ready-to-use application, provider manages everything = SaaS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Cloud service models (SaaS)"],
    },
    {
        "id": "cloudplus-arch-r2-009", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "mcq",
        "stem": "A company keeps sensitive records in its own on-premises private cloud but runs its public-facing web "
                "tier in a public cloud, with orchestration moving data and workloads between the two as one system. "
                "Which deployment model is this?",
        "options": [
            {"id": "A", "text": "Community cloud"},
            {"id": "B", "text": "Hybrid cloud"},
            {"id": "C", "text": "Multi-cloud"},
            {"id": "D", "text": "Public cloud"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A hybrid cloud combines private (or on-premises) and public cloud environments, integrated so data and "
                       "applications can move between them — exactly the on-prem-plus-public arrangement described.",
            "distractors": {
                "A": "A community cloud is shared by several organizations with common requirements, not one org blending private and public.",
                "C": "Multi-cloud means using two or more public providers; the scenario pairs a private environment with one public cloud.",
                "D": "Public cloud alone would not include the organization's on-premises private environment.",
            },
            "exam_pattern": "Private/on-prem + public, integrated as one = hybrid cloud; several public providers = multi-cloud.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Cloud deployment models (hybrid)"],
    },
    {
        "id": "cloudplus-arch-r2-010", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "mcq",
        "stem": "A private cloud normally handles the workload, but during rare demand spikes it automatically overflows "
                "the excess load to a public cloud and scales back once the spike passes. What is this pattern called?",
        "options": [
            {"id": "A", "text": "Cloud bursting"},
            {"id": "B", "text": "Geo-replication"},
            {"id": "C", "text": "Blue-green deployment"},
            {"id": "D", "text": "Vertical scaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cloud bursting lets a private environment offload peak demand to a public cloud only when needed, so the "
                       "organization pays for extra public capacity just during spikes — a common hybrid-cloud use case.",
            "distractors": {
                "B": "Geo-replication copies data across regions for resilience; it is not overflow of compute load to a public cloud.",
                "C": "Blue-green is a release strategy using two environments, not a demand-overflow pattern.",
                "D": "Vertical scaling enlarges a single instance; cloud bursting spills workload to another cloud instead.",
            },
            "exam_pattern": "Private cloud overflows peak load to public cloud on demand = cloud bursting.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Design (cloud bursting)"],
    },
    {
        "id": "cloudplus-arch-r2-011", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 3, "type": "mcq",
        "stem": "An avionics-grade service is engineered with fully redundant, synchronized components so that if one "
                "fails, processing continues with NO interruption or lost transactions at all. Which property BEST "
                "describes this, as distinct from merely minimizing downtime?",
        "options": [
            {"id": "A", "text": "High availability"},
            {"id": "B", "text": "Fault tolerance"},
            {"id": "C", "text": "Disaster recovery"},
            {"id": "D", "text": "Load balancing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Fault tolerance uses redundant, often synchronized components so a failure causes zero interruption. "
                       "High availability aims to minimize downtime (brief failover is acceptable), whereas fault tolerance targets no downtime.",
            "distractors": {
                "A": "High availability minimizes downtime but typically permits a short failover gap; the scenario demands no interruption.",
                "C": "Disaster recovery restores service after a major outage; it is about recovery, not uninterrupted operation.",
                "D": "Load balancing distributes traffic; alone it does not guarantee zero-interruption continuity on component failure.",
            },
            "exam_pattern": "No interruption at all on failure = fault tolerance; minimal (not zero) downtime = high availability.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Resilient design (fault tolerance vs HA)"],
    },
    {
        "id": "cloudplus-arch-r2-012", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 3, "type": "mcq",
        "stem": "For disaster recovery, a company maintains a fully equipped secondary site with hardware running and "
                "data replicated continuously, so it can take over within minutes of a primary failure. Which type of "
                "recovery site is this?",
        "options": [
            {"id": "A", "text": "Cold site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Hot site"},
            {"id": "D", "text": "Pilot light"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A hot site is fully provisioned and kept in near-real-time sync with production, giving the lowest RTO/RPO "
                       "(takeover in minutes) at the highest cost.",
            "distractors": {
                "A": "A cold site provides only space/power/connectivity; hardware and data must be brought in, so recovery takes days.",
                "B": "A warm site has some hardware and periodically updated data, giving recovery in hours — not minutes.",
                "D": "'Pilot light' keeps only a minimal core running to be scaled up later; it is not a fully running, continuously synced site.",
            },
            "exam_pattern": "Fully running, continuously synced, minutes to recover = hot site; space-only, days = cold; in between = warm.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — DR design (recovery site types)"],
    },
    {
        "id": "cloudplus-arch-r2-013", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 2, "type": "mcq",
        "stem": "Under the cloud shared responsibility model for an IaaS virtual machine, who is responsible for patching "
                "the guest operating system and securing the applications and data on it?",
        "options": [
            {"id": "A", "text": "The cloud provider"},
            {"id": "B", "text": "The customer"},
            {"id": "C", "text": "No one; IaaS VMs patch themselves"},
            {"id": "D", "text": "It depends entirely on the region"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In IaaS the provider secures the underlying cloud (physical facilities, hardware, hypervisor), while the "
                       "customer is responsible for the guest OS, patches, applications, configuration, and data — security 'in' the cloud.",
            "distractors": {
                "A": "The provider secures the infrastructure OF the cloud, not the customer's guest OS and apps in an IaaS VM.",
                "C": "IaaS VMs do not self-patch; the customer must apply OS and application updates.",
                "D": "Responsibility boundaries follow the service model (IaaS), not the region.",
            },
            "exam_pattern": "IaaS: provider secures the cloud; customer secures the guest OS, apps, and data in the cloud.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Shared responsibility model"],
    },
    {
        "id": "cloudplus-arch-r2-014", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_design_solutions", "difficulty": 3, "type": "mcq",
        "stem": "Two data centers both run the application simultaneously and share live traffic, and either one can "
                "carry the full load if the other fails. Which high-availability configuration is this?",
        "options": [
            {"id": "A", "text": "Active-passive (standby)"},
            {"id": "B", "text": "Active-active"},
            {"id": "C", "text": "Cold standby"},
            {"id": "D", "text": "Pilot light"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In active-active, all nodes/sites serve traffic concurrently and share load; losing one leaves the others "
                       "to absorb its share. It improves both capacity and resilience but requires data synchronization.",
            "distractors": {
                "A": "Active-passive keeps the secondary idle until failover; the scenario has both sites actively serving.",
                "C": "A cold standby is powered off until needed — not simultaneously serving live traffic.",
                "D": "Pilot light keeps only a minimal core warm to scale up later, not a second site taking live load now.",
            },
            "exam_pattern": "Both nodes serve live traffic and share load = active-active; standby idle until failover = active-passive.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — HA design (active-active vs active-passive)"],
    },

    # ----- cloudp_capacity_scaling -------------------------------------
    {
        "id": "cloudplus-arch-r2-015", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "mcq",
        "stem": "As evening demand falls, an auto-scaling group terminates several of its identical web instances to "
                "cut cost while keeping the remaining instances the same size. Which action is this?",
        "options": [
            {"id": "A", "text": "Scaling up"},
            {"id": "B", "text": "Scaling out"},
            {"id": "C", "text": "Scaling in"},
            {"id": "D", "text": "Scaling down"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Removing instances from a horizontally scaled pool is scaling in — the reverse of scaling out. Instance "
                       "size is unchanged; only the instance count drops.",
            "distractors": {
                "A": "Scaling up increases the size (CPU/RAM) of a single instance — a vertical action, not removing instances.",
                "B": "Scaling out adds instances; the scenario removes them.",
                "D": "Scaling down reduces the size of an instance (vertical), not the number of instances.",
            },
            "exam_pattern": "Remove instances = scale in; add instances = scale out; resize one instance = scale up/down.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Scalability (scaling in vs out/up/down)"],
    },
    {
        "id": "cloudplus-arch-r2-016", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "mcq",
        "stem": "A payroll system is idle most of the month but is hammered every weekday from 08:00-10:00. The team "
                "configures the platform to add capacity at 07:45 and remove it at 10:30 on weekdays. Which auto-scaling "
                "method is this?",
        "options": [
            {"id": "A", "text": "Dynamic (target-tracking) scaling"},
            {"id": "B", "text": "Scheduled scaling"},
            {"id": "C", "text": "Manual scaling"},
            {"id": "D", "text": "Vertical scaling"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Scheduled scaling changes capacity at known times based on a predictable pattern, provisioning ahead of a "
                       "recurring peak rather than waiting for a metric threshold to be crossed.",
            "distractors": {
                "A": "Dynamic/target-tracking scaling reacts to live metrics (e.g., CPU); here capacity changes on a fixed clock, not on metrics.",
                "C": "Manual scaling requires a person to act each time; this is automated on a schedule.",
                "D": "Vertical scaling resizes a single instance; the scenario adds/removes capacity on a schedule.",
            },
            "exam_pattern": "Known, time-based pattern -> scheduled scaling; react to live metrics -> dynamic scaling.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Auto-scaling (scheduled vs dynamic)"],
    },
    {
        "id": "cloudplus-arch-r2-017", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 3, "type": "mcq",
        "stem": "An architect notes that their system is designed so capacity CAN be increased to meet long-term growth "
                "by adding resources, even though that growth is planned and provisioned manually rather than "
                "automatically. Which property does this describe?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Scalability"},
            {"id": "C", "text": "Redundancy"},
            {"id": "D", "text": "Fault tolerance"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Scalability is the capability of a system to grow to handle increased load by adding resources, whether "
                       "that growth is manual or automated. Elasticity is the narrower, automatic, real-time, bidirectional form of it.",
            "distractors": {
                "A": "Elasticity specifically means AUTOMATIC, rapid expansion and contraction with demand; the scenario is deliberate, planned growth.",
                "C": "Redundancy is duplicating components for availability, not the ability to grow capacity.",
                "D": "Fault tolerance keeps running through failures; it is not about increasing capacity for load.",
            },
            "exam_pattern": "Ability to grow (manual or auto) = scalability; automatic real-time growth/shrink = elasticity.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Scalability vs elasticity"],
    },
    {
        "id": "cloudplus-arch-r2-018", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 2, "type": "mcq",
        "stem": "A capacity review finds that engineers permanently allocate four times the resources any workload has "
                "ever used, 'just to be safe,' leaving most capacity idle and inflating the bill. Which problem is this?",
        "options": [
            {"id": "A", "text": "Under-provisioning"},
            {"id": "B", "text": "Over-provisioning"},
            {"id": "C", "text": "Right-sizing"},
            {"id": "D", "text": "Cloud bursting"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Over-provisioning allocates far more capacity than needed, wasting money on idle resources. Capacity "
                       "planning and right-sizing correct it by matching allocation to actual demand plus a sensible margin.",
            "distractors": {
                "A": "Under-provisioning allocates too little capacity, causing performance problems — the opposite of the waste described.",
                "C": "Right-sizing is the fix (matching resources to real usage), not the problem.",
                "D": "Cloud bursting offloads peaks to another cloud; it is not the chronic over-allocation described.",
            },
            "exam_pattern": "Allocating far more than needed, idle waste = over-provisioning; too little = under-provisioning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Capacity planning (over/under-provisioning)"],
    },
    {
        "id": "cloudplus-arch-r2-019", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_capacity_scaling", "difficulty": 3, "type": "mcq",
        "stem": "A single relational database can no longer hold or serve its data from one node. The team splits the "
                "data horizontally across several database nodes by a key (e.g., customer ID ranges), so each node holds "
                "a subset. Which technique is this?",
        "options": [
            {"id": "A", "text": "Vertical scaling"},
            {"id": "B", "text": "Replication (mirroring)"},
            {"id": "C", "text": "Sharding (horizontal partitioning)"},
            {"id": "D", "text": "RAID striping"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Sharding horizontally partitions a dataset across multiple nodes, each holding a portion keyed by some "
                       "attribute, distributing both storage and load so the database can scale out beyond one node.",
            "distractors": {
                "A": "Vertical scaling makes one node bigger; it does not split data across nodes.",
                "B": "Replication copies the whole dataset to other nodes (for read scaling/HA); it does not partition the data into subsets.",
                "D": "RAID striping spreads blocks across disks within one system for performance, not a dataset across database nodes.",
            },
            "exam_pattern": "Split a dataset across nodes by key = sharding; copy the whole dataset = replication.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Scaling data tiers (sharding/partitioning)"],
    },

    # ----- cloudp_integration_migration --------------------------------
    {
        "id": "cloudplus-arch-r2-020", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "A migration assessment discovers an internal reporting application that no users have opened in two "
                "years and that duplicates a newer tool. The team decommissions it instead of moving it. Which of the "
                "official migration strategies is this?",
        "options": [
            {"id": "A", "text": "Retain"},
            {"id": "B", "text": "Rehost"},
            {"id": "C", "text": "Retire"},
            {"id": "D", "text": "Repurchase"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Retiring decommissions a workload that is no longer needed, eliminating its cost and maintenance instead "
                       "of migrating it — a legitimate and common outcome of a migration assessment.",
            "distractors": {
                "A": "Retain means keeping a workload where it is to revisit later; the scenario shuts the app down entirely.",
                "B": "Rehosting lifts-and-shifts a workload to the cloud; this app is being removed, not moved.",
                "D": "Repurchasing means switching to a different (often SaaS) product; here the redundant app is simply decommissioned.",
            },
            "exam_pattern": "Unused/redundant workload decommissioned = retire.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration strategies (retire)"],
    },
    {
        "id": "cloudplus-arch-r2-021", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "An application depends on ultra-low-latency links to factory equipment and faces a compliance review "
                "next year, so the team decides to leave it on-premises for now and reassess after the review. Which "
                "migration strategy is this?",
        "options": [
            {"id": "A", "text": "Retire"},
            {"id": "B", "text": "Retain (revisit later)"},
            {"id": "C", "text": "Refactor"},
            {"id": "D", "text": "Replatform"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Retain (sometimes 'revisit') means consciously keeping a workload in its current location for now — because "
                       "of latency, compliance, cost, or readiness — and reassessing later, rather than migrating it in this wave.",
            "distractors": {
                "A": "Retire decommissions a workload; this one is still needed and kept running on-premises.",
                "C": "Refactor rewrites an application for cloud-native services; nothing is being rewritten here.",
                "D": "Replatform makes targeted changes during a move to the cloud; this app is not being moved at all yet.",
            },
            "exam_pattern": "Deliberately keep a workload in place for now, revisit later = retain.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration strategies (retain)"],
    },
    {
        "id": "cloudplus-arch-r2-022", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "A company must move 500 TB of archival data to the cloud, but its internet link would take months to "
                "transfer that volume. Which migration approach is most practical?",
        "options": [
            {"id": "A", "text": "Stream it live over an IPsec VPN during business hours"},
            {"id": "B", "text": "Ship the data on a provider's physical transfer appliance (offline seeding)"},
            {"id": "C", "text": "Serve it through a content delivery network"},
            {"id": "D", "text": "Transfer it using DNS TXT records"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "For very large datasets over limited bandwidth, an offline/physical data-transfer appliance (seeding) is "
                       "far faster than network transfer: data is copied to a device and shipped, then ingested at the provider.",
            "distractors": {
                "A": "Streaming 500 TB over a constrained link would take an impractically long time — the exact problem stated.",
                "C": "A CDN caches and distributes content to users; it is not a bulk data-migration mechanism.",
                "D": "DNS TXT records carry tiny text values; they cannot transport hundreds of terabytes.",
            },
            "exam_pattern": "Huge dataset + limited bandwidth -> offline/physical transfer appliance (seeding).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Migration (offline/bulk data transfer)"],
    },
    {
        "id": "cloudplus-arch-r2-023", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 2, "type": "mcq",
        "stem": "After migrating a new order system to the cloud, it must exchange transactions with a legacy "
                "on-premises mainframe that uses different message formats. Which component is designed to translate and "
                "route messages between the two systems?",
        "options": [
            {"id": "A", "text": "A content delivery network"},
            {"id": "B", "text": "An integration middleware layer (e.g., an enterprise service bus / API gateway)"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A hypervisor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Integration middleware (such as an enterprise service bus or API gateway/adapter) mediates between systems, "
                       "transforming message formats and routing transactions so a modern cloud app and a legacy system can interoperate.",
            "distractors": {
                "A": "A CDN caches content for users; it does not translate transaction formats between back-end systems.",
                "C": "A load balancer distributes requests across servers; it does not transform or route differing message formats.",
                "D": "A hypervisor runs virtual machines; it has no role in application-level message integration.",
            },
            "exam_pattern": "Translate/route messages between disparate systems = integration middleware (ESB/API gateway).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Integration (middleware/APIs)"],
    },
    {
        "id": "cloudplus-arch-r2-024", "exam": "cloudplus", "domain": "cloudp_architecture",
        "subtopic": "cloudp_integration_migration", "difficulty": 3, "type": "mcq",
        "stem": "Leadership is concerned about becoming unable to leave a single provider later. Which design choice "
                "most directly reduces the risk of vendor lock-in?",
        "options": [
            {"id": "A", "text": "Build exclusively on one provider's proprietary managed services"},
            {"id": "B", "text": "Favor open standards and portable formats (e.g., containers, open APIs)"},
            {"id": "C", "text": "Sign a longer-term contract with the provider"},
            {"id": "D", "text": "Disable multi-region deployment"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Using open standards and portable technologies (containers, open APIs, portable data formats) keeps "
                       "workloads movable between providers, which directly mitigates vendor lock-in.",
            "distractors": {
                "A": "Depending solely on one provider's proprietary services deepens lock-in — the opposite of the goal.",
                "C": "A longer contract is a commercial commitment that can increase dependence, not reduce technical lock-in.",
                "D": "Disabling multi-region reduces resilience and has nothing to do with provider portability.",
            },
            "exam_pattern": "Reduce lock-in with open standards/portable formats (containers, open APIs).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 1 — Integration/migration (vendor lock-in/portability)"],
    },

    # ===================================================================
    # Domain 2: Deployment  (cloudp_deployment)
    # ===================================================================

    # ----- cloudp_provisioning -----------------------------------------
    {
        "id": "cloudplus-dep-r2-001", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "A 2 TB volume is presented to a VM, but the storage array only consumes physical capacity as data is "
                "actually written, allowing the array's logical allocations to exceed its raw capacity. Which allocation "
                "method is this?",
        "options": [
            {"id": "A", "text": "Thin provisioning"},
            {"id": "B", "text": "Thick provisioning"},
            {"id": "C", "text": "Deduplication"},
            {"id": "D", "text": "Snapshotting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Thin provisioning allocates physical storage on demand as data is written, so the sum of logical volumes "
                       "can exceed physical capacity (oversubscription). It improves utilization but must be monitored to avoid running out of real space.",
            "distractors": {
                "B": "Thick provisioning reserves the full declared capacity up front, so logical allocation cannot exceed physical capacity.",
                "C": "Deduplication removes duplicate blocks to save space; it is not an allocation-on-write scheme.",
                "D": "A snapshot captures point-in-time state; it is not a capacity-allocation method.",
            },
            "exam_pattern": "Allocate physical space only as written, allows oversubscription = thin provisioning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage provisioning (thin vs thick)"],
    },
    {
        "id": "cloudplus-dep-r2-002", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "A latency-sensitive database must never risk a write failing because the underlying array ran out of "
                "unallocated space. The administrator pre-reserves the volume's entire capacity when it is created. Which "
                "method is this, and why is it chosen here?",
        "options": [
            {"id": "A", "text": "Thin provisioning; it saves the most physical space"},
            {"id": "B", "text": "Thick provisioning; it guarantees the full capacity is reserved up front, avoiding oversubscription surprises"},
            {"id": "C", "text": "Deduplication; it prevents fragmentation"},
            {"id": "D", "text": "Tiering; it moves cold data to cheaper storage"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Thick provisioning pre-allocates the entire declared capacity at creation, so the space is guaranteed and "
                       "the volume cannot be starved by oversubscription — valuable for predictable, latency-sensitive workloads.",
            "distractors": {
                "A": "Thin provisioning saves space but risks running out of real capacity under oversubscription — the opposite of the requirement.",
                "C": "Deduplication reduces duplicate data; it does not reserve capacity to guarantee writes.",
                "D": "Tiering relocates data by access frequency; it does not pre-reserve a volume's full capacity.",
            },
            "exam_pattern": "Pre-reserve full capacity up front to guarantee space = thick provisioning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage provisioning (thick provisioning)"],
    },
    {
        "id": "cloudplus-dep-r2-003", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "To let developers deploy only pre-approved, standardized resource configurations themselves — without "
                "raising a ticket — a cloud team publishes a curated set of templates they can launch on demand. What is "
                "this capability called?",
        "options": [
            {"id": "A", "text": "A self-service catalog (service catalog)"},
            {"id": "B", "text": "A configuration management database (CMDB)"},
            {"id": "C", "text": "A load-balancer pool"},
            {"id": "D", "text": "A SIEM"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A self-service catalog exposes pre-approved, standardized offerings that users can provision on demand, "
                       "balancing agility with governance because only vetted configurations are available.",
            "distractors": {
                "B": "A CMDB records configuration items and relationships; it is not a user-facing menu for provisioning resources.",
                "C": "A load-balancer pool is a group of backend targets, not a provisioning catalog.",
                "D": "A SIEM correlates security events; it does not provide self-service provisioning.",
            },
            "exam_pattern": "Curated, pre-approved offerings users provision themselves = self-service/service catalog.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (self-service catalog)"],
    },
    {
        "id": "cloudplus-dep-r2-004", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 2, "type": "mcq",
        "stem": "An auto-scaling group needs to launch new instances that are always identical — same base image, "
                "instance size, subnet, security group, and first-boot script. Which artifact captures this full launch "
                "specification for reuse?",
        "options": [
            {"id": "A", "text": "A launch/instance template"},
            {"id": "B", "text": "A snapshot"},
            {"id": "C", "text": "A security group only"},
            {"id": "D", "text": "A RAID set"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A launch (instance) template bundles the complete specification for launching an instance — image, size, "
                       "network, security group, and bootstrap data — so auto-scaling and deployments produce identical instances every time.",
            "distractors": {
                "B": "A snapshot is a point-in-time copy of a volume; it is not a full launch specification (size, network, etc.).",
                "C": "A security group is only the firewall rules — one part of the spec, not the whole launch configuration.",
                "D": "A RAID set is a disk-redundancy arrangement, unrelated to instance launch specifications.",
            },
            "exam_pattern": "Full reusable launch spec (image + size + network + bootstrap) = launch/instance template.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Provisioning (templates/launch configurations)"],
    },
    {
        "id": "cloudplus-dep-r2-005", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_provisioning", "difficulty": 3, "type": "fill",
        "stem": "Fill in the term: Allocating more virtual resources (such as vCPUs or memory) to guests than the host "
                "physically has, on the assumption that not all guests peak at once, is called ____ (one word, also "
                "known as oversubscription).",
        "correct": ["overcommitment", "overcommit", "oversubscription"],
        "explanation": {
            "correct": "Overcommitment (oversubscription) assigns more virtual resources than the host physically owns, improving "
                       "density and utilization; it works when guests do not all demand peak resources simultaneously, but excessive "
                       "overcommit causes contention (e.g., CPU ready time, memory ballooning/swapping).",
            "distractors": {},
            "exam_pattern": "Assign more virtual resource than physically exists = overcommitment/oversubscription (watch for contention).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute provisioning (resource overcommitment)"],
    },

    # ----- cloudp_storage_deployment -----------------------------------
    {
        "id": "cloudplus-dep-r2-006", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A dozen application servers must all mount the same directory of shared documents at once and read and "
                "write files using standard file-system semantics over NFS or SMB. Which storage type fits best?",
        "options": [
            {"id": "A", "text": "Block storage"},
            {"id": "B", "text": "Object storage"},
            {"id": "C", "text": "File storage (shared file system)"},
            {"id": "D", "text": "Ephemeral instance storage"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "File storage presents a shared, hierarchical file system over NFS/SMB that many clients can mount "
                       "simultaneously — ideal for shared document directories and home folders.",
            "distractors": {
                "A": "Block storage is typically attached to a single instance as a raw volume; it is not a natively shared multi-client file system.",
                "B": "Object storage uses an HTTP API and flat namespace, not POSIX file-system semantics with concurrent mounts.",
                "D": "Ephemeral instance storage is temporary local disk tied to one instance, not a shared network file system.",
            },
            "exam_pattern": "Many clients mount the same file system over NFS/SMB = file storage.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage types (file storage)"],
    },
    {
        "id": "cloudplus-dep-r2-007", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs the maximum fault tolerance from exactly two disks, accepting that only half the "
                "raw capacity is usable, so that either disk can fail without data loss. Which RAID level is this?",
        "options": [
            {"id": "A", "text": "RAID 0"},
            {"id": "B", "text": "RAID 1"},
            {"id": "C", "text": "RAID 5"},
            {"id": "D", "text": "RAID 6"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RAID 1 mirrors identical data onto two disks, so either disk can fail with no data loss; usable capacity is "
                       "50% of the raw total. It is the simplest redundancy and needs only two disks.",
            "distractors": {
                "A": "RAID 0 stripes with no redundancy; losing either disk loses all data.",
                "C": "RAID 5 needs at least three disks and uses distributed parity, not mirroring across two.",
                "D": "RAID 6 needs at least four disks (double parity); it is not a two-disk mirror.",
            },
            "exam_pattern": "Two disks, mirror, 50% usable, survives one failure = RAID 1.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (RAID 1)"],
    },
    {
        "id": "cloudplus-dep-r2-008", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A video-rendering scratch volume values maximum speed and total capacity and holds only disposable "
                "temporary data, so redundancy is not required. Disks are striped with no parity or mirroring. Which "
                "RAID level is this, and what is its key risk?",
        "options": [
            {"id": "A", "text": "RAID 0; any single disk failure loses the entire array"},
            {"id": "B", "text": "RAID 1; it halves usable capacity"},
            {"id": "C", "text": "RAID 5; it must rebuild parity"},
            {"id": "D", "text": "RAID 10; it needs at least four disks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RAID 0 stripes data across disks for maximum performance and 100% usable capacity but provides no "
                       "redundancy, so the failure of any single disk destroys the whole array — acceptable only for disposable data.",
            "distractors": {
                "B": "RAID 1 mirrors (50% usable) and is redundant; the scenario explicitly has no mirroring or parity.",
                "C": "RAID 5 adds distributed parity for fault tolerance; the scenario has no parity.",
                "D": "RAID 10 combines mirroring and striping for redundancy; the scenario is pure striping with none.",
            },
            "exam_pattern": "Striping only, no redundancy, fastest, any disk loss = total loss = RAID 0.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (RAID 0)"],
    },
    {
        "id": "cloudplus-dep-r2-009", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 3, "type": "mcq",
        "stem": "A storage team wants an array that can survive TWO disks failing at the same time while still using "
                "distributed parity (not full mirroring). Which RAID level meets this with a minimum of four disks?",
        "options": [
            {"id": "A", "text": "RAID 5"},
            {"id": "B", "text": "RAID 6"},
            {"id": "C", "text": "RAID 10"},
            {"id": "D", "text": "RAID 0"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RAID 6 uses double distributed parity and tolerates the loss of any two disks simultaneously, needing at "
                       "least four disks. It is favored for large arrays where a second disk may fail during a lengthy rebuild.",
            "distractors": {
                "A": "RAID 5 has single parity and survives only one disk failure, not two at once.",
                "C": "RAID 10 can survive two failures only if they are not both in the same mirrored pair, and it uses mirroring, not distributed parity.",
                "D": "RAID 0 has no redundancy and cannot survive any disk failure.",
            },
            "exam_pattern": "Survive two simultaneous failures with distributed parity, 4+ disks = RAID 6.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (RAID 6)"],
    },
    {
        "id": "cloudplus-dep-r2-010", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 3, "type": "mcq",
        "stem": "A transactional database needs both high write performance and redundancy, and the team is willing to "
                "give up 50% of raw capacity. They choose a nested level that mirrors pairs of disks and then stripes "
                "across those mirrors. Which RAID level is this?",
        "options": [
            {"id": "A", "text": "RAID 5"},
            {"id": "B", "text": "RAID 6"},
            {"id": "C", "text": "RAID 10 (1+0)"},
            {"id": "D", "text": "RAID 0"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RAID 10 (1+0) stripes across mirrored pairs, combining the performance of striping with the redundancy of "
                       "mirroring. Usable capacity is 50%, and it rebuilds quickly, making it a common choice for write-heavy databases.",
            "distractors": {
                "A": "RAID 5 uses single distributed parity, not mirrored-then-striped pairs, and write performance suffers from parity calculation.",
                "B": "RAID 6 uses double parity with even higher write overhead, not mirroring and striping.",
                "D": "RAID 0 stripes with no mirroring and provides no redundancy.",
            },
            "exam_pattern": "Mirror pairs then stripe, 50% usable, fast + redundant = RAID 10.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (RAID 10/nested RAID)"],
    },
    {
        "id": "cloudplus-dep-r2-011", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_storage_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A cache tier wants the fastest possible local disk and does not care if the data is lost when the "
                "instance is stopped or terminated. Which storage option is most appropriate?",
        "options": [
            {"id": "A", "text": "Ephemeral (instance/local) storage"},
            {"id": "B", "text": "A persistent network block volume"},
            {"id": "C", "text": "Object storage"},
            {"id": "D", "text": "An archive/cold tier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ephemeral (instance/local) storage is physically attached to the host, offering very low latency, but its "
                       "data does not survive instance stop/termination — a good fit for caches, scratch, and other disposable data.",
            "distractors": {
                "B": "A persistent network block volume survives instance termination (durability the cache does not need) and adds network latency.",
                "C": "Object storage is durable and API-accessed with higher latency — the opposite of a fast local disk.",
                "D": "An archive tier is optimized for cheap, slow, long-term retention, not a high-speed cache.",
            },
            "exam_pattern": "Fastest local disk, data loss on stop is acceptable = ephemeral/instance storage.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Storage (ephemeral vs persistent)"],
    },

    # ----- cloudp_compute_deployment -----------------------------------
    {
        "id": "cloudplus-dep-r2-012", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A team runs hundreds of containers across many hosts and needs automated scheduling, scaling, "
                "self-healing (restarting failed containers), and rolling updates. Which category of tool provides this?",
        "options": [
            {"id": "A", "text": "A container orchestration platform"},
            {"id": "B", "text": "A single container runtime on one host"},
            {"id": "C", "text": "A Type 2 hypervisor"},
            {"id": "D", "text": "A Layer 4 load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A container orchestration platform (e.g., Kubernetes as one example) schedules containers across a cluster "
                       "and automates scaling, self-healing, service discovery, and rolling updates — far beyond running a single runtime.",
            "distractors": {
                "B": "A single container runtime starts/stops containers on one host but does not schedule, scale, or self-heal across a cluster.",
                "C": "A Type 2 hypervisor runs VMs on a host OS; it does not orchestrate containers.",
                "D": "A load balancer distributes traffic; it does not schedule or self-heal containers.",
            },
            "exam_pattern": "Cluster-wide scheduling, scaling, self-healing of containers = container orchestration (e.g., Kubernetes).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (container orchestration)"],
    },
    {
        "id": "cloudplus-dep-r2-013", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 3, "type": "mcq",
        "stem": "To maximize VM density and performance in a production data center, an operator installs a hypervisor "
                "that runs directly on the bare-metal hardware with no underlying host operating system. Which hypervisor "
                "type is this?",
        "options": [
            {"id": "A", "text": "Type 1 (bare-metal) hypervisor"},
            {"id": "B", "text": "Type 2 (hosted) hypervisor"},
            {"id": "C", "text": "A container engine"},
            {"id": "D", "text": "An application emulator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 1 (bare-metal) hypervisor runs directly on the hardware, giving better performance, density, and "
                       "isolation for production; Type 2 runs atop a host OS and is typical for desktops/labs.",
            "distractors": {
                "B": "A Type 2 (hosted) hypervisor runs on top of a host operating system, adding overhead — not the bare-metal install described.",
                "C": "A container engine shares the host OS kernel and runs containers, not full VMs on bare metal.",
                "D": "An emulator imitates different hardware/architecture; it is not a bare-metal VM hypervisor.",
            },
            "exam_pattern": "Hypervisor on bare metal, no host OS = Type 1; hypervisor on a host OS = Type 2.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute virtualization (hypervisor types)"],
    },
    {
        "id": "cloudplus-dep-r2-014", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 3, "type": "mcq",
        "stem": "Two redundant database VMs must never land on the same physical host, so that a single hardware failure "
                "cannot take both down. Which placement control enforces this?",
        "options": [
            {"id": "A", "text": "An affinity rule"},
            {"id": "B", "text": "An anti-affinity rule"},
            {"id": "C", "text": "A load-balancing algorithm"},
            {"id": "D", "text": "A snapshot schedule"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An anti-affinity rule keeps specified VMs on separate physical hosts, so a single host failure cannot take "
                       "out both members of a redundant pair — essential for high availability.",
            "distractors": {
                "A": "An affinity rule does the opposite: it keeps VMs together on the same host (e.g., for low inter-VM latency).",
                "C": "A load-balancing algorithm distributes network traffic; it does not control VM-to-host placement.",
                "D": "A snapshot schedule governs backups, not placement of VMs across hosts.",
            },
            "exam_pattern": "Keep redundant VMs on different hosts = anti-affinity; keep them together = affinity.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (affinity/anti-affinity placement)"],
    },
    {
        "id": "cloudplus-dep-r2-015", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_compute_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A machine-learning team needs to train deep neural networks that depend on massively parallel matrix "
                "computation. Which instance family best matches this workload?",
        "options": [
            {"id": "A", "text": "GPU-accelerated (accelerated computing) instances"},
            {"id": "B", "text": "General-purpose instances"},
            {"id": "C", "text": "Burstable (shared-core) instances"},
            {"id": "D", "text": "Memory-optimized instances"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GPU/accelerated-computing instances provide the massively parallel processing that neural-network training "
                       "needs, dramatically outperforming CPUs for matrix-heavy workloads.",
            "distractors": {
                "B": "General-purpose instances balance CPU/memory for typical workloads but lack the parallel acceleration ML training needs.",
                "C": "Burstable instances share CPU and are meant for low, spiky baselines — unsuitable for sustained heavy training.",
                "D": "Memory-optimized instances suit large in-memory datasets (e.g., caches, big databases), not parallel matrix compute.",
            },
            "exam_pattern": "Match the workload to the instance family; parallel ML/graphics compute = GPU/accelerated instances.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Compute (instance types/sizing)"],
    },

    # ----- cloudp_networking_deployment --------------------------------
    {
        "id": "cloudplus-dep-r2-016", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 3, "type": "mcq",
        "stem": "In cloud networking, which control is STATELESS, is evaluated at the subnet boundary, and does NOT "
                "automatically allow return traffic (so you must permit both inbound and outbound directions explicitly)?",
        "options": [
            {"id": "A", "text": "A security group"},
            {"id": "B", "text": "A network ACL (subnet ACL)"},
            {"id": "C", "text": "A Web Application Firewall"},
            {"id": "D", "text": "A route table"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A network ACL filters traffic at the subnet boundary and is stateless: it does not track connections, so "
                       "return traffic must be explicitly allowed in both directions. Security groups, by contrast, are stateful.",
            "distractors": {
                "A": "A security group is stateful and instance-level: return traffic for an allowed connection is automatically permitted.",
                "C": "A WAF inspects Layer 7 HTTP content for app attacks; it is not the stateless subnet-level packet filter described.",
                "D": "A route table directs where traffic goes; it does not permit or deny traffic statefully or statelessly.",
            },
            "exam_pattern": "Stateless, subnet-level, return traffic not auto-allowed = network ACL; stateful, instance-level = security group.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (NACL vs security group; stateful vs stateless)"],
    },
    {
        "id": "cloudplus-dep-r2-017", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "Ignoring the handful of addresses the cloud reserves in each subnet, which IPv4 CIDR block provides the "
                "LARGEST number of usable host addresses?",
        "options": [
            {"id": "A", "text": "10.0.0.0/24"},
            {"id": "B", "text": "10.0.0.0/26"},
            {"id": "C", "text": "10.0.0.0/28"},
            {"id": "D", "text": "10.0.0.0/30"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The smaller the prefix length, the more host bits remain. A /24 leaves 8 host bits (256 addresses), far "
                       "more than /26 (64), /28 (16), or /30 (4). Lower prefix = larger subnet.",
            "distractors": {
                "B": "A /26 leaves only 6 host bits (64 addresses) — smaller than a /24.",
                "C": "A /28 leaves 4 host bits (16 addresses) — much smaller than a /24.",
                "D": "A /30 leaves 2 host bits (4 addresses), typically used for point-to-point links — the smallest here.",
            },
            "exam_pattern": "Smaller prefix (/24) = more host bits = more addresses; larger prefix (/30) = fewer.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (CIDR/subnet sizing)"],
    },
    {
        "id": "cloudplus-dep-r2-018", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "Instances in a private subnet must download OS updates from the internet, but nothing on the internet "
                "should be able to initiate a connection to them. Which component provides this outbound-only internet "
                "access?",
        "options": [
            {"id": "A", "text": "An internet gateway"},
            {"id": "B", "text": "A NAT gateway"},
            {"id": "C", "text": "A site-to-site VPN gateway"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A NAT gateway lets private-subnet instances initiate outbound connections to the internet (e.g., for "
                       "updates) while preventing unsolicited inbound connections, preserving the subnet's privacy.",
            "distractors": {
                "A": "An internet gateway allows bidirectional internet access, including inbound — which the requirement forbids.",
                "C": "A site-to-site VPN connects to another private network (e.g., on-prem), not general outbound internet access.",
                "D": "A load balancer distributes inbound traffic to servers; it does not provide outbound internet access for private instances.",
            },
            "exam_pattern": "Outbound-only internet for private subnet = NAT gateway; bidirectional = internet gateway.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (NAT gateway)"],
    },
    {
        "id": "cloudplus-dep-r2-019", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "Two separate cloud virtual networks owned by the same company must let their resources communicate "
                "using private IP addresses, without traffic ever traversing the public internet. Which mechanism "
                "provides this directly?",
        "options": [
            {"id": "A", "text": "Virtual network (VPC) peering"},
            {"id": "B", "text": "A content delivery network"},
            {"id": "C", "text": "A NAT gateway"},
            {"id": "D", "text": "A public object-storage endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Network/VPC peering privately connects two virtual networks so their resources communicate over private IPs "
                       "on the provider's backbone, never crossing the public internet.",
            "distractors": {
                "B": "A CDN caches content at the edge for end users; it does not privately interconnect two virtual networks.",
                "C": "A NAT gateway provides outbound internet access for private hosts; it does not peer two virtual networks.",
                "D": "A public object-storage endpoint is for storing/retrieving objects, not for interconnecting networks.",
            },
            "exam_pattern": "Privately connect two cloud VNets over private IPs = VPC/network peering.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (VPC/VNet peering)"],
    },
    {
        "id": "cloudplus-dep-r2-020", "exam": "cloudplus", "domain": "cloudp_deployment",
        "subtopic": "cloudp_networking_deployment", "difficulty": 2, "type": "mcq",
        "stem": "Backend servers hold long-lived sessions of very uneven duration, so simple round-robin leaves some "
                "servers overloaded. The team wants each new connection sent to whichever server currently has the "
                "fewest active connections. Which load-balancing algorithm is this?",
        "options": [
            {"id": "A", "text": "Round robin"},
            {"id": "B", "text": "Least connections"},
            {"id": "C", "text": "Source IP hash"},
            {"id": "D", "text": "Geolocation (geographic) routing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Least-connections sends each new request to the backend with the fewest active connections, which balances "
                       "load better than round robin when session durations vary widely.",
            "distractors": {
                "A": "Round robin cycles through servers in order regardless of current load — the very problem described.",
                "C": "Source IP hash pins a client to a server for persistence; it does not balance by current connection count.",
                "D": "Geolocation routing chooses a server by the client's region, not by how busy each server is.",
            },
            "exam_pattern": "Send to the least-busy backend = least connections; fixed rotation = round robin; sticky by client = IP hash.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 2 — Networking (load-balancing algorithms)"],
    },

    # ===================================================================
    # Domain 4: Security  (cloudp_security)
    # ===================================================================

    # ----- cloudp_identity_access --------------------------------------
    {
        "id": "cloudplus-sec-r2-001", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 3, "type": "mcq",
        "stem": "An access policy grants entry only when multiple attributes are satisfied together — the user's "
                "department is 'Finance', the resource is tagged 'confidential', the request comes from a corporate "
                "network, and the time is within business hours. Which access-control model evaluates policies like this?",
        "options": [
            {"id": "A", "text": "Role-based access control (RBAC)"},
            {"id": "B", "text": "Mandatory access control (MAC)"},
            {"id": "C", "text": "Attribute-based access control (ABAC)"},
            {"id": "D", "text": "Discretionary access control (DAC)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "ABAC makes decisions by evaluating attributes of the subject, resource, action, and environment "
                       "(department, tags, network, time) against policies, enabling fine-grained, context-aware access.",
            "distractors": {
                "A": "RBAC grants access based solely on assigned roles, not a combination of contextual attributes like time and location.",
                "B": "MAC enforces access through system-wide classification labels and clearances, not flexible attribute policies.",
                "D": "DAC lets resource owners grant access at their discretion; it is not attribute/condition-driven policy evaluation.",
            },
            "exam_pattern": "Access by multiple attributes/conditions (user, resource, environment) = ABAC; by role = RBAC.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (ABAC)"],
    },
    {
        "id": "cloudplus-sec-r2-002", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following sign-in combinations genuinely qualifies as multi-factor authentication?",
        "options": [
            {"id": "A", "text": "A password plus a one-time code from a hardware token"},
            {"id": "B", "text": "A password plus a PIN"},
            {"id": "C", "text": "A password plus a security question"},
            {"id": "D", "text": "Two different passwords"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "True MFA combines factors from DIFFERENT categories. A password (something you know) plus a hardware-token "
                       "code (something you have) uses two distinct categories, so a stolen password alone is not enough.",
            "distractors": {
                "B": "A password and a PIN are both 'something you know' — the same factor category, so this is single-factor.",
                "C": "A password and a security question are both knowledge factors, not two different categories.",
                "D": "Two passwords are both knowledge factors; using more of the same category is still single-factor.",
            },
            "exam_pattern": "MFA = factors from DIFFERENT categories (know/have/are); two of the same category is not MFA.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (MFA factor categories)"],
    },
    {
        "id": "cloudplus-sec-r2-003", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 3, "type": "mcq",
        "stem": "To tightly govern administrator accounts, a company stores privileged credentials in a vault, grants "
                "elevated access only on checkout for a limited time, and records the entire admin session. Which class "
                "of solution is this?",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO)"},
            {"id": "B", "text": "A SIEM"},
            {"id": "C", "text": "Multi-factor authentication (MFA)"},
            {"id": "D", "text": "Privileged access management (PAM)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "PAM secures, vaults, and monitors privileged accounts, issuing elevated access just-in-time with session "
                       "recording and automatic credential rotation, limiting standing admin rights and abuse.",
            "distractors": {
                "A": "SSO lets one authentication cover many apps; it does not vault and time-limit privileged credentials.",
                "B": "A SIEM correlates and alerts on security events; it does not broker just-in-time privileged access.",
                "C": "MFA adds authentication factors but does not provide credential vaulting, checkout, or session recording for admins.",
            },
            "exam_pattern": "Vault + just-in-time elevation + session recording for admin accounts = PAM.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (privileged access management)"],
    },
    {
        "id": "cloudplus-sec-r2-004", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 3, "type": "mcq",
        "stem": "A control requires that the person who REQUESTS a production change cannot be the same person who "
                "APPROVES and deploys it, so no single individual controls the whole process. Which principle is this?",
        "options": [
            {"id": "A", "text": "Least privilege"},
            {"id": "B", "text": "Job rotation"},
            {"id": "C", "text": "Separation of duties"},
            {"id": "D", "text": "Mandatory vacation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Separation (segregation) of duties divides a sensitive process among multiple people so no one person can "
                       "complete it alone, reducing fraud and error — here, splitting request from approval/deployment.",
            "distractors": {
                "A": "Least privilege limits how much access each identity has; it does not require splitting a process across people.",
                "B": "Job rotation moves staff between roles to detect issues and cross-train; it is not splitting a single transaction.",
                "D": "Mandatory vacation forces time off to surface hidden misconduct; it is not request-vs-approval separation.",
            },
            "exam_pattern": "No single person completes a sensitive process (request vs approve) = separation of duties.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (separation of duties)"],
    },
    {
        "id": "cloudplus-sec-r2-005", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 3, "type": "mcq",
        "stem": "An identity is granted an action by one attached policy, while a separate policy contains an explicit "
                "Deny for that same action. In the standard cloud IAM evaluation logic, what is the result?",
        "options": [
            {"id": "A", "text": "The Allow takes effect because allows outrank denies"},
            {"id": "B", "text": "The explicit Deny overrides the Allow, so access is denied"},
            {"id": "C", "text": "The most recently attached policy wins"},
            {"id": "D", "text": "The longer/more detailed policy wins"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In typical IAM evaluation, an explicit Deny always overrides any Allow. Access is permitted only when at "
                       "least one Allow applies AND no explicit Deny matches, so the Deny here wins and access is blocked.",
            "distractors": {
                "A": "Allows do not outrank denies; an explicit Deny takes precedence over any Allow.",
                "C": "Policy evaluation is not based on attachment order or recency; an explicit Deny is decisive regardless of order.",
                "D": "Length or detail of a policy does not decide the outcome; the explicit Deny controls.",
            },
            "exam_pattern": "Explicit Deny overrides Allow; need an Allow AND no Deny for access.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (IAM policy evaluation)"],
    },

    # ----- cloudp_data_security ----------------------------------------
    {
        "id": "cloudplus-sec-r2-006", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 3, "type": "mcq",
        "stem": "A workload must keep data encrypted even while it is actively being processed in memory, so that even a "
                "privileged administrator on the host cannot read the plaintext. Which protection state does this "
                "describe?",
        "options": [
            {"id": "A", "text": "Encryption in use (confidential computing)"},
            {"id": "B", "text": "Encryption at rest"},
            {"id": "C", "text": "Encryption in transit"},
            {"id": "D", "text": "Tokenization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encryption in use protects data during processing, typically via a hardware-based trusted execution "
                       "environment (confidential computing), so plaintext is never exposed in memory even to host administrators.",
            "distractors": {
                "B": "Encryption at rest protects stored data on disk, not data being actively processed in memory.",
                "C": "Encryption in transit protects data moving across the network, not data in memory during computation.",
                "D": "Tokenization substitutes sensitive values with surrogates; it does not keep data encrypted while in use in memory.",
            },
            "exam_pattern": "Keep data encrypted while processed in memory (TEE) = encryption in use / confidential computing.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (encryption in use)"],
    },
    {
        "id": "cloudplus-sec-r2-007", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "To encrypt large volumes of data quickly, a system uses a single shared secret key for both encryption "
                "and decryption. Which type of cryptography is this?",
        "options": [
            {"id": "A", "text": "Asymmetric (public-key) encryption"},
            {"id": "B", "text": "Hashing"},
            {"id": "C", "text": "Symmetric encryption"},
            {"id": "D", "text": "Tokenization"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Symmetric encryption uses one shared secret key to both encrypt and decrypt. It is fast and well suited to "
                       "bulk data; its challenge is securely distributing the shared key.",
            "distractors": {
                "A": "Asymmetric encryption uses a public/private key pair (different keys) and is slower — often used to exchange symmetric keys.",
                "B": "Hashing is a one-way function that cannot be reversed to recover the data; it is not encryption.",
                "D": "Tokenization replaces data with surrogate tokens via a vault; it is not key-based encryption.",
            },
            "exam_pattern": "One shared key for encrypt and decrypt, fast for bulk = symmetric; key pair = asymmetric.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (symmetric vs asymmetric)"],
    },
    {
        "id": "cloudplus-sec-r2-008", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A service must store user passwords so it can verify them at login but must never be able to recover the "
                "original password, even if its database is stolen. Which technique is appropriate?",
        "options": [
            {"id": "A", "text": "Symmetric encryption of the password"},
            {"id": "B", "text": "Hashing (ideally salted) the password"},
            {"id": "C", "text": "Base64 encoding the password"},
            {"id": "D", "text": "Tokenizing the password"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Passwords should be hashed with a strong, salted one-way function: the system compares hashes at login, "
                       "and because hashing is irreversible, the original password cannot be recovered from the stored value.",
            "distractors": {
                "A": "Symmetric encryption is reversible — anyone with the key can recover the plaintext password, which this requirement forbids.",
                "C": "Base64 is encoding, not security; it is trivially reversible and provides no protection.",
                "D": "Tokenization maps values via a vault and is reversible through that vault; hashing is the standard for password verification.",
            },
            "exam_pattern": "Store passwords so they can be verified but never recovered = salted hashing (one-way).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (hashing vs encryption)"],
    },
    {
        "id": "cloudplus-sec-r2-009", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 3, "type": "mcq",
        "stem": "A regulated organization must generate and store its encryption keys inside dedicated, tamper-resistant "
                "hardware validated to FIPS 140, so key material never exists in plaintext outside the device. Which "
                "technology meets this requirement?",
        "options": [
            {"id": "A", "text": "A hardware security module (HSM)"},
            {"id": "B", "text": "A software-only key store with default settings"},
            {"id": "C", "text": "A TLS certificate"},
            {"id": "D", "text": "A web application firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An HSM is dedicated, tamper-resistant hardware (often FIPS 140-validated) that generates, stores, and uses "
                       "keys so the key material never leaves the device in plaintext — the highest assurance for key protection.",
            "distractors": {
                "B": "A general software key store does not provide the tamper-resistant hardware boundary and FIPS-validated assurance required.",
                "C": "A TLS certificate secures a connection; it is not a device for protecting key material at rest.",
                "D": "A WAF filters web attacks; it has no role in hardware key protection.",
            },
            "exam_pattern": "Tamper-resistant, FIPS-validated hardware holding keys = HSM (backs KMS for highest assurance).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (HSM/key management)"],
    },
    {
        "id": "cloudplus-sec-r2-010", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to automatically detect and block attempts to email or upload files containing patterns "
                "like credit-card numbers or national IDs outside the organization. Which control is purpose-built for "
                "this?",
        "options": [
            {"id": "A", "text": "A Web Application Firewall"},
            {"id": "B", "text": "An intrusion detection system"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "Data Loss Prevention (DLP)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "DLP inspects content in email, uploads, and endpoints for sensitive patterns and enforces policy (block, "
                       "quarantine, alert) to prevent unauthorized exfiltration of regulated data.",
            "distractors": {
                "A": "A WAF blocks web-application attacks against your apps; it does not inspect outbound content for sensitive data leaks.",
                "B": "An IDS detects intrusions and alerts; it is not designed to classify and block sensitive-data exfiltration by policy.",
                "C": "A SIEM aggregates and correlates logs for detection; it does not itself enforce data-handling policy on content.",
            },
            "exam_pattern": "Detect/block sensitive data leaving the org by content = Data Loss Prevention (DLP).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (DLP)"],
    },

    # ----- cloudp_network_security -------------------------------------
    {
        "id": "cloudplus-sec-r2-011", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "A public-facing service is knocked offline by a massive flood of traffic from thousands of sources "
                "saturating its bandwidth. Which protection is specifically designed to absorb and filter this kind of "
                "volumetric attack?",
        "options": [
            {"id": "A", "text": "A Web Application Firewall alone"},
            {"id": "B", "text": "A DDoS protection/scrubbing service"},
            {"id": "C", "text": "A host-based antivirus agent"},
            {"id": "D", "text": "A NAT gateway"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A DDoS protection/scrubbing service absorbs and filters volumetric distributed floods at scale (often at the "
                       "network edge) so legitimate traffic still reaches the service.",
            "distractors": {
                "A": "A WAF inspects application-layer (Layer 7) requests and is not designed to absorb a massive volumetric bandwidth flood on its own.",
                "C": "Host antivirus scans files/processes on a host; it cannot mitigate a network-wide traffic flood.",
                "D": "A NAT gateway provides outbound address translation; it offers no DDoS mitigation.",
            },
            "exam_pattern": "Volumetric flood from many sources = DDoS mitigation/scrubbing; app-layer exploit = WAF.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (DDoS protection)"],
    },
    {
        "id": "cloudplus-sec-r2-012", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants a sensor placed inline that not only detects malicious traffic signatures but "
                "actively drops the offending packets before they reach the target. Which device is this?",
        "options": [
            {"id": "A", "text": "An intrusion detection system (IDS)"},
            {"id": "B", "text": "A honeypot"},
            {"id": "C", "text": "An intrusion prevention system (IPS)"},
            {"id": "D", "text": "A SIEM"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An IPS sits inline and can block or drop malicious traffic in real time, actively preventing the attack, "
                       "whereas an IDS only detects and alerts (passive, out of band).",
            "distractors": {
                "A": "An IDS detects and alerts but does not sit inline to drop traffic; it is passive.",
                "B": "A honeypot is a decoy to lure and study attackers; it does not block production traffic.",
                "D": "A SIEM aggregates and correlates logs for analysis; it does not inline-block packets.",
            },
            "exam_pattern": "Inline, actively blocks = IPS; passive, detect/alert only = IDS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (IDS vs IPS)"],
    },
    {
        "id": "cloudplus-sec-r2-013", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "Administrators must manage instances in a private subnet over SSH/RDP, but those instances must not be "
                "directly reachable from the internet. Which design provides a single hardened entry point for this "
                "administrative access?",
        "options": [
            {"id": "A", "text": "A bastion host (jump box)"},
            {"id": "B", "text": "A NAT gateway"},
            {"id": "C", "text": "A CDN edge node"},
            {"id": "D", "text": "A reverse proxy for web traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A bastion host (jump box) is a single hardened, monitored system exposed for administrative access; admins "
                       "connect to it and then reach private instances, so those instances never accept direct internet SSH/RDP.",
            "distractors": {
                "B": "A NAT gateway provides outbound internet for private hosts; it is not an inbound administrative entry point.",
                "C": "A CDN edge node caches content for users; it is not an admin access gateway.",
                "D": "A reverse proxy fronts web applications; it is not the hardened SSH/RDP jump host described.",
            },
            "exam_pattern": "Single hardened SSH/RDP entry point to private instances = bastion host / jump box.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (bastion/jump host)"],
    },
    {
        "id": "cloudplus-sec-r2-014", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 3, "type": "mcq",
        "stem": "Replacing a legacy VPN, a company grants each user access to only the specific applications they are "
                "authorized for, verifying identity and device posture per session and never exposing the full internal "
                "network. Which approach is this?",
        "options": [
            {"id": "A", "text": "A site-to-site IPsec VPN"},
            {"id": "B", "text": "Port forwarding on the edge firewall"},
            {"id": "C", "text": "A DMZ with a single shared gateway"},
            {"id": "D", "text": "Zero Trust Network Access (ZTNA)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "ZTNA brokers per-application access based on verified identity and device posture, granting least-privilege "
                       "connectivity to specific apps rather than placing the user on the whole network as a traditional VPN does.",
            "distractors": {
                "A": "A traditional VPN typically grants broad network access once connected — the exposure ZTNA is designed to remove.",
                "B": "Port forwarding exposes specific ports through the firewall; it does not verify identity/posture per application session.",
                "C": "A DMZ segments public-facing servers; it does not provide per-user, per-app, posture-aware access.",
            },
            "exam_pattern": "Per-app, identity/posture-verified access without exposing the whole network = ZTNA.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (zero trust/ZTNA)"],
    },
    {
        "id": "cloudplus-sec-r2-015", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 3, "type": "mcq",
        "stem": "To limit the damage if a server is compromised, a team restricts the OUTBOUND destinations that "
                "workloads may reach, allowing only a small set of approved endpoints and blocking everything else. What "
                "is this practice called, and what threat does it most directly counter?",
        "options": [
            {"id": "A", "text": "Ingress filtering; it blocks inbound port scans"},
            {"id": "B", "text": "Egress filtering; it limits data exfiltration and command-and-control callbacks"},
            {"id": "C", "text": "Port forwarding; it publishes internal services"},
            {"id": "D", "text": "NAT; it conserves public IP addresses"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Egress filtering controls outbound traffic to approved destinations only, so a compromised host cannot "
                       "freely exfiltrate data or reach attacker command-and-control servers.",
            "distractors": {
                "A": "Ingress filtering governs inbound traffic; the scenario restricts outbound destinations.",
                "C": "Port forwarding exposes internal services inbound; it is unrelated to restricting outbound destinations.",
                "D": "NAT translates addresses to conserve IPs; it is not an outbound allow-list security control.",
            },
            "exam_pattern": "Restrict outbound to approved destinations = egress filtering (limits exfiltration/C2).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (egress filtering)"],
    },

    # ----- cloudp_compliance_hardening ---------------------------------
    {
        "id": "cloudplus-sec-r2-016", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A cloud application processes the personal data of individuals residing in the European Union. Which "
                "regulation most directly governs how that personal data must be protected, including consent and the "
                "right to erasure?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "HIPAA"},
            {"id": "C", "text": "GDPR (General Data Protection Regulation)"},
            {"id": "D", "text": "SOX (Sarbanes-Oxley)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "GDPR governs the processing of personal data of EU residents, defining rights (consent, access, erasure) and "
                       "obligations on controllers/processors, with significant penalties for non-compliance.",
            "distractors": {
                "A": "PCI DSS governs cardholder (payment-card) data, not general personal-data privacy rights.",
                "B": "HIPAA governs protected health information in the US healthcare context, not EU personal data broadly.",
                "D": "SOX governs financial reporting and controls for public companies, not personal-data privacy.",
            },
            "exam_pattern": "EU personal-data privacy (consent, erasure) = GDPR; map each regulation to the data it protects.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance (regulations/GDPR)"],
    },
    {
        "id": "cloudplus-sec-r2-017", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A US healthcare provider moves patient medical records to the cloud. Which regulation most directly "
                "dictates how this protected health information (PHI) must be safeguarded?",
        "options": [
            {"id": "A", "text": "HIPAA"},
            {"id": "B", "text": "GDPR"},
            {"id": "C", "text": "PCI DSS"},
            {"id": "D", "text": "FERPA"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "HIPAA sets US requirements for safeguarding protected health information (PHI), including security, privacy, "
                       "and breach-notification rules that extend to cloud providers acting as business associates.",
            "distractors": {
                "B": "GDPR protects EU residents' personal data broadly; the scenario is US healthcare PHI governed by HIPAA.",
                "C": "PCI DSS covers payment-card data, not medical records.",
                "D": "FERPA protects student education records, not healthcare PHI.",
            },
            "exam_pattern": "US protected health information (PHI) = HIPAA.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance (regulations/HIPAA)"],
    },
    {
        "id": "cloudplus-sec-r2-018", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Before a container image is promoted to production, a pipeline step inspects its layers and packages for "
                "known CVEs and insecure configurations, failing the build if critical vulnerabilities are found. What is "
                "this practice called?",
        "options": [
            {"id": "A", "text": "Penetration testing"},
            {"id": "B", "text": "Container image (vulnerability) scanning"},
            {"id": "C", "text": "Load testing"},
            {"id": "D", "text": "Chaos engineering"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Image scanning analyzes a container image's OS packages, libraries, and settings against vulnerability "
                       "databases (CVEs) and policies, blocking images with critical findings before they reach production.",
            "distractors": {
                "A": "Penetration testing is a broader simulated attack against a running system, not automated per-image CVE inspection in the pipeline.",
                "C": "Load testing measures performance under load, not image vulnerabilities.",
                "D": "Chaos engineering deliberately injects failures to test resilience; it does not scan images for CVEs.",
            },
            "exam_pattern": "Scan images for CVEs/misconfig before deploy = container image/vulnerability scanning.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Hardening (container/image scanning)"],
    },
    {
        "id": "cloudplus-sec-r2-019", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 3, "type": "mcq",
        "stem": "A SaaS provider must give enterprise customers an independent auditor's report attesting that its "
                "controls for security, availability, and confidentiality are suitably designed and operating. Which "
                "report/framework fits this need?",
        "options": [
            {"id": "A", "text": "A CIS Benchmark score"},
            {"id": "B", "text": "A RAID configuration report"},
            {"id": "C", "text": "An RFC 1918 statement"},
            {"id": "D", "text": "A SOC 2 report"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A SOC 2 report is an independent attestation of a service organization's controls against the Trust Services "
                       "Criteria (security, availability, processing integrity, confidentiality, privacy), commonly requested of SaaS vendors.",
            "distractors": {
                "A": "A CIS Benchmark is a hardening guide/score for configurations, not an independent audit attestation of organizational controls.",
                "B": "A RAID report concerns disk redundancy, not control attestation.",
                "C": "RFC 1918 defines private IP ranges; it is not an audit report.",
            },
            "exam_pattern": "Independent attestation of a service org's controls = SOC 2 (Trust Services Criteria).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance (audits/attestations, SOC 2)"],
    },
    {
        "id": "cloudplus-sec-r2-020", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A regulation requires that financial transaction logs be kept, unaltered and retrievable, for seven "
                "years and then disposed of. Which governance artifact defines how long data is kept and when it is "
                "destroyed?",
        "options": [
            {"id": "A", "text": "A recovery point objective (RPO)"},
            {"id": "B", "text": "An encryption-at-rest policy"},
            {"id": "C", "text": "A data retention policy"},
            {"id": "D", "text": "A tokenization scheme"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A data retention policy specifies how long each class of data must be kept and when it must be securely "
                       "disposed of, aligning storage and deletion with legal and regulatory requirements.",
            "distractors": {
                "A": "RPO defines acceptable data loss (time) for recovery; it does not govern long-term retention and disposal.",
                "B": "An encryption-at-rest policy protects stored data's confidentiality; it does not set retention periods.",
                "D": "Tokenization substitutes sensitive values; it is not a retention/disposal schedule.",
            },
            "exam_pattern": "How long to keep data and when to destroy it = data retention policy.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance (data retention/governance)"],
    },

    # ===================================================================
    # Domain 3: Operations  (cloudp_operations)
    # ===================================================================

    # ----- cloudp_logging_monitoring -----------------------------------
    {
        "id": "cloudplus-ops-r2-001", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A monitoring platform samples CPU utilization as a timestamped numeric value every 60 seconds and plots "
                "it over time. Which type of telemetry is this specifically?",
        "options": [
            {"id": "A", "text": "A log entry"},
            {"id": "B", "text": "A metric"},
            {"id": "C", "text": "A trace"},
            {"id": "D", "text": "An alert"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A metric is a numeric measurement captured at intervals over time (e.g., CPU %, request rate). Metrics are "
                       "ideal for dashboards, thresholds, and trend analysis.",
            "distractors": {
                "A": "A log is a discrete, timestamped event record (often text), not a sampled numeric time series.",
                "C": "A trace follows a single request across services/components; it is not a periodic numeric sample.",
                "D": "An alert is a notification fired when a condition is met; it is not the underlying measurement itself.",
            },
            "exam_pattern": "Numeric sample over time = metric; event record = log; request path across services = trace.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring (metrics vs logs vs traces)"],
    },
    {
        "id": "cloudplus-ops-r2-002", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "To catch outages before customers do, a team runs scripted, simulated transactions (login, search, "
                "checkout) against the production site every minute from external locations and alerts on failures. Which "
                "monitoring approach is this?",
        "options": [
            {"id": "A", "text": "Real user monitoring (RUM)"},
            {"id": "B", "text": "Application performance monitoring agents only"},
            {"id": "C", "text": "Synthetic monitoring"},
            {"id": "D", "text": "Centralized log aggregation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Synthetic monitoring proactively runs scripted transactions from outside the system on a schedule, detecting "
                       "availability and performance problems even when no real user is currently active.",
            "distractors": {
                "A": "Real user monitoring passively measures actual user sessions; it cannot detect a problem before any user hits it.",
                "B": "APM agents instrument the running app internally; they do not simulate external user journeys on a schedule.",
                "D": "Log aggregation centralizes logs for search; it does not actively probe the service with simulated transactions.",
            },
            "exam_pattern": "Scripted external probes on a schedule to catch issues proactively = synthetic monitoring.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring (synthetic monitoring)"],
    },
    {
        "id": "cloudplus-ops-r2-003", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Instead of a fixed threshold, a monitoring system learns each metric's normal pattern over time and "
                "alerts when current behavior deviates significantly from that learned baseline. Which capability is this?",
        "options": [
            {"id": "A", "text": "A static threshold alarm"},
            {"id": "B", "text": "Anomaly detection (dynamic baselining)"},
            {"id": "C", "text": "A snapshot schedule"},
            {"id": "D", "text": "Log rotation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Anomaly detection builds a dynamic baseline of normal behavior and flags significant deviations, catching "
                       "problems that a single fixed threshold would miss (e.g., seasonal or time-of-day variation).",
            "distractors": {
                "A": "A static threshold fires at one fixed value and cannot adapt to normal variation — the limitation anomaly detection addresses.",
                "C": "A snapshot schedule governs backups; it is not a metric-analysis technique.",
                "D": "Log rotation manages log file size/retention; it does not detect behavioral anomalies.",
            },
            "exam_pattern": "Alert on deviation from a learned baseline (not a fixed value) = anomaly detection/dynamic baselining.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring (anomaly detection/baselines)"],
    },
    {
        "id": "cloudplus-ops-r2-004", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "While triaging an incident, an engineer filters the centralized logs to show only ERROR and CRITICAL "
                "entries, hiding INFO and DEBUG. The categories ERROR, WARN, INFO, and DEBUG are examples of what?",
        "options": [
            {"id": "A", "text": "Metric units"},
            {"id": "B", "text": "Distributed trace spans"},
            {"id": "C", "text": "Log severity levels"},
            {"id": "D", "text": "Synthetic checks"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Log severity (log) levels rank messages by importance (e.g., DEBUG < INFO < WARN < ERROR < CRITICAL), letting "
                       "operators filter noise and focus on significant events, and control how much is retained.",
            "distractors": {
                "A": "Metric units (e.g., percent, bytes) describe measurements, not log importance categories.",
                "B": "Trace spans represent segments of a request's path; they are not message-importance categories.",
                "D": "Synthetic checks are scripted probes, not categories applied to log messages.",
            },
            "exam_pattern": "DEBUG/INFO/WARN/ERROR/CRITICAL = log severity levels used to filter and prioritize.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Logging (log levels/severity)"],
    },
    {
        "id": "cloudplus-ops-r2-005", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "To collect detailed in-guest metrics such as per-process memory, disk latency, and application counters, "
                "an operations team installs a lightweight collector inside each virtual machine. What is this monitoring "
                "model called?",
        "options": [
            {"id": "A", "text": "Agent-based monitoring"},
            {"id": "B", "text": "Agentless monitoring"},
            {"id": "C", "text": "Synthetic monitoring"},
            {"id": "D", "text": "Edge caching"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Agent-based monitoring installs software inside each host to gather deep, in-guest telemetry (process-level "
                       "metrics, custom counters) that external/agentless polling cannot see, at the cost of deploying and maintaining agents.",
            "distractors": {
                "B": "Agentless monitoring collects data from outside the guest (APIs, SNMP, hypervisor) and typically cannot see per-process in-guest detail.",
                "C": "Synthetic monitoring runs external scripted transactions; it is not an in-guest collector.",
                "D": "Edge caching distributes content; it is unrelated to monitoring collection models.",
            },
            "exam_pattern": "Collector installed in the host for deep in-guest metrics = agent-based; external collection = agentless.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Monitoring (agent-based vs agentless)"],
    },

    # ----- cloudp_maintenance_automation -------------------------------
    {
        "id": "cloudplus-ops-r2-006", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "To patch a cluster with no user-visible downtime, an operator updates a few instances at a time, waiting "
                "for each batch to pass health checks and rejoin before moving on. Which maintenance approach is this?",
        "options": [
            {"id": "A", "text": "A big-bang update of all instances at once"},
            {"id": "B", "text": "A rolling (batched) update"},
            {"id": "C", "text": "Disabling patching entirely"},
            {"id": "D", "text": "A full-outage maintenance window"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A rolling update patches instances in small batches while the rest keep serving traffic, preserving "
                       "availability; each batch is verified healthy before the next proceeds.",
            "distractors": {
                "A": "A big-bang update changes everything at once, risking a full outage and offering no gradual verification.",
                "C": "Disabling patching leaves systems vulnerable and does not accomplish the maintenance.",
                "D": "A full-outage window takes the whole service down — the opposite of the no-downtime goal.",
            },
            "exam_pattern": "Patch in small batches with health checks, service stays up = rolling update.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance (rolling updates)"],
    },
    {
        "id": "cloudplus-ops-r2-007", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "A team documents an exact, step-by-step procedure for responding to a specific recurring operational "
                "event (e.g., 'disk nearly full on a log server'), which they increasingly automate. What is this "
                "document commonly called?",
        "options": [
            {"id": "A", "text": "A service-level agreement"},
            {"id": "B", "text": "A runbook (or playbook)"},
            {"id": "C", "text": "A performance baseline"},
            {"id": "D", "text": "A change request number"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A runbook (playbook) captures the precise steps to handle a defined operational or incident scenario, "
                       "improving consistency and speed and serving as the basis for automation/orchestration.",
            "distractors": {
                "A": "An SLA is a service commitment contract, not a procedural response document.",
                "C": "A baseline is a reference set of normal metrics, not a step-by-step procedure.",
                "D": "A change request number identifies a tracked change; it is not the response procedure itself.",
            },
            "exam_pattern": "Documented step-by-step response to a defined event = runbook/playbook (automation candidate).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance/automation (runbooks)"],
    },
    {
        "id": "cloudplus-ops-r2-008", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "To avoid a repeat of a patch that once broke production, what is the BEST practice before applying "
                "updates to production systems?",
        "options": [
            {"id": "A", "text": "Apply patches directly to production during business hours"},
            {"id": "B", "text": "Test patches in a staging/non-production environment that mirrors production first"},
            {"id": "C", "text": "Skip testing to patch faster"},
            {"id": "D", "text": "Patch only once per year to minimize risk"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Patches should be validated in a staging/test environment that resembles production before rollout, catching "
                       "breakage safely; combined with a rollback plan and maintenance window, this minimizes production risk.",
            "distractors": {
                "A": "Patching straight to production during business hours maximizes the blast radius if the patch fails.",
                "C": "Skipping testing is exactly what caused the earlier outage; it increases, not reduces, risk.",
                "D": "Patching only yearly leaves systems exposed to known vulnerabilities far too long.",
            },
            "exam_pattern": "Validate patches in staging that mirrors prod before production rollout.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Maintenance (patch testing/staging)"],
    },
    {
        "id": "cloudplus-ops-r2-009", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_maintenance_automation", "difficulty": 2, "type": "mcq",
        "stem": "An organization requires that every modification to production go through a formal process of request, "
                "risk assessment, approval, and scheduling before implementation. Which practice is this?",
        "options": [
            {"id": "A", "text": "Incident response"},
            {"id": "B", "text": "Vulnerability management"},
            {"id": "C", "text": "Change management"},
            {"id": "D", "text": "Capacity planning"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Change management governs how changes are requested, assessed for risk, approved, scheduled, implemented, and "
                       "reviewed, reducing the chance that a change causes an unplanned outage.",
            "distractors": {
                "A": "Incident response handles active disruptions after they occur, not the authorization of planned changes.",
                "B": "Vulnerability management finds and remediates weaknesses; it is not the change-approval workflow.",
                "D": "Capacity planning forecasts resource needs; it is not the process for approving production changes.",
            },
            "exam_pattern": "Formal request/assess/approve/schedule of changes = change management.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Operations (change management)"],
    },

    # ----- cloudp_backup_restore ---------------------------------------
    {
        "id": "cloudplus-ops-r2-010", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 3, "type": "mcq",
        "stem": "A backup job copies all data that has changed since the last FULL backup. It does not reset the archive "
                "marker, so each successive job grows, but a restore needs only the last full plus the single most recent "
                "job. Which backup type is this?",
        "options": [
            {"id": "A", "text": "Incremental backup"},
            {"id": "B", "text": "Differential backup"},
            {"id": "C", "text": "Full backup"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A differential backup copies everything changed since the last full backup and does not clear the archive "
                       "marker, so it grows over time; restoring requires only the last full plus the latest differential (two sets).",
            "distractors": {
                "A": "An incremental copies changes since the last backup of ANY type and resets the marker, so a restore needs the full plus EVERY incremental in order.",
                "C": "A full backup copies all data every time; it is not 'changes since the last full.'",
                "D": "A snapshot is a point-in-time volume/VM image, not the archive-marker differential scheme described.",
            },
            "exam_pattern": "Differential = since last FULL, restore needs full + LAST diff; incremental = since last backup, restore needs full + ALL increments.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup types (differential)"],
    },
    {
        "id": "cloudplus-ops-r2-011", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "Which backup type copies ALL selected data every time it runs — using the most storage and time per job "
                "but providing the simplest, fastest single-step restore?",
        "options": [
            {"id": "A", "text": "Full backup"},
            {"id": "B", "text": "Incremental backup"},
            {"id": "C", "text": "Differential backup"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A full backup copies all data on every run. It consumes the most time and space per job, but restoration is "
                       "simplest and fastest because everything is in one set — no chaining of other backups is needed.",
            "distractors": {
                "B": "An incremental copies only changes since the last backup; restore requires the full plus every incremental in order.",
                "C": "A differential copies changes since the last full; restore needs the full plus the last differential, not a single complete set.",
                "D": "A snapshot captures point-in-time state and often depends on the source volume; it is not a standalone full copy of all selected data.",
            },
            "exam_pattern": "Copies everything each run, simplest restore, most space = full backup.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup types (full)"],
    },
    {
        "id": "cloudplus-ops-r2-012", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "After an outage, leadership asks: 'What is the maximum time we can take to restore the service back to "
                "operation?' Which metric answers this?",
        "options": [
            {"id": "A", "text": "RPO (Recovery Point Objective)"},
            {"id": "B", "text": "RTO (Recovery Time Objective)"},
            {"id": "C", "text": "MTBF (Mean Time Between Failures)"},
            {"id": "D", "text": "SLA (Service-Level Agreement)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RTO is the maximum acceptable time to restore service after a disruption; it drives recovery design such as "
                       "warm/hot standby and automation. (RPO, by contrast, measures acceptable data loss in time.)",
            "distractors": {
                "A": "RPO defines how much DATA (as time) you can afford to lose, not how long recovery may take.",
                "C": "MTBF estimates average time between failures — a reliability metric, not a recovery-time target.",
                "D": "An SLA is a service commitment contract; it may reference RTO but is not itself the recovery-time metric.",
            },
            "exam_pattern": "RTO = how long to recover (downtime); RPO = how much data (time) can be lost.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup/DR (RTO vs RPO)"],
    },
    {
        "id": "cloudplus-ops-r2-013", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 2, "type": "mcq",
        "stem": "An auditor notes that although backups run nightly, the company has never confirmed it can actually "
                "recover from them. Which practice closes this gap?",
        "options": [
            {"id": "A", "text": "Taking backups more frequently"},
            {"id": "B", "text": "Performing periodic test restores (recovery testing)"},
            {"id": "C", "text": "Increasing backup retention"},
            {"id": "D", "text": "Encrypting the backups"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Regular test restores verify that backups are complete, uncorrupted, and recoverable within the RTO. An "
                       "untested backup provides no assurance it will work when needed.",
            "distractors": {
                "A": "More frequent backups improve RPO but still do not prove the backups can be restored.",
                "C": "Longer retention keeps backups available longer but does not validate recoverability.",
                "D": "Encryption protects confidentiality but does not confirm the data can be restored.",
            },
            "exam_pattern": "Untested backup = unproven; validate with periodic test restores.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup/restore (recovery testing)"],
    },
    {
        "id": "cloudplus-ops-r2-014", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_backup_restore", "difficulty": 3, "type": "mcq",
        "stem": "To ensure ransomware cannot alter or delete the backups it would need to recover, a company stores "
                "backups that cannot be modified or erased until a set retention period expires. Which backup property is "
                "this?",
        "options": [
            {"id": "A", "text": "Immutable (WORM) backups"},
            {"id": "B", "text": "Incremental backups"},
            {"id": "C", "text": "A single off-site copy"},
            {"id": "D", "text": "More frequent snapshots"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Immutable (write-once-read-many) backups cannot be changed or deleted until their retention expires, so "
                       "ransomware or a malicious insider cannot tamper with the recovery data — a key modern resilience control.",
            "distractors": {
                "B": "Incremental is a backup scheduling type; it does not make backups tamper-proof.",
                "C": "An off-site copy aids disaster recovery but, if writable, can still be encrypted or deleted by ransomware.",
                "D": "More frequent snapshots improve RPO but are not inherently immutable against tampering.",
            },
            "exam_pattern": "Backups that cannot be altered/deleted until retention expires = immutable/WORM (anti-ransomware).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Backup (immutability/WORM)"],
    },

    # ----- cloudp_optimization -----------------------------------------
    {
        "id": "cloudplus-ops-r2-015", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A nightly batch-processing job is fault-tolerant and can restart if interrupted. To run it at the lowest "
                "possible cost, which purchasing option is most appropriate?",
        "options": [
            {"id": "A", "text": "Reserved (committed-use) instances"},
            {"id": "B", "text": "On-demand instances"},
            {"id": "C", "text": "Spot / preemptible instances"},
            {"id": "D", "text": "Dedicated hosts"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Spot/preemptible instances use spare capacity at steep discounts but can be reclaimed on short notice. They "
                       "suit interruptible, fault-tolerant, restartable work such as batch jobs where occasional eviction is acceptable.",
            "distractors": {
                "A": "Reserved instances save money for steady, always-on workloads via a long commitment — not needed for a nightly interruptible job.",
                "B": "On-demand is flexible but the most expensive per hour; spot is cheaper for interruption-tolerant work.",
                "D": "Dedicated hosts provide isolated physical capacity at premium cost, the opposite of lowest-cost.",
            },
            "exam_pattern": "Interruptible, fault-tolerant, restartable work -> spot/preemptible (cheapest); steady always-on -> reserved.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (spot/preemptible)"],
    },
    {
        "id": "cloudplus-ops-r2-016", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 3, "type": "mcq",
        "stem": "A cost review reveals a surprisingly large bill line item for data transfer. Analytics jobs repeatedly "
                "pull terabytes from object storage in one region to compute nodes in another region and out to the "
                "internet. Which optimization most directly reduces this cost?",
        "options": [
            {"id": "A", "text": "Enlarge the compute instances"},
            {"id": "B", "text": "Minimize cross-region/internet data egress (co-locate compute with data; cache)"},
            {"id": "C", "text": "Take more frequent snapshots"},
            {"id": "D", "text": "Disable monitoring to cut overhead"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Data egress — especially cross-region and internet-bound transfer — is a common hidden cost. Keeping compute "
                       "in the same region as its data and caching/reducing outbound transfer directly lowers egress charges.",
            "distractors": {
                "A": "Larger instances raise compute cost and do nothing about data-transfer charges.",
                "C": "More snapshots add storage cost; they do not reduce data-transfer (egress) charges.",
                "D": "Disabling monitoring removes visibility and does not address egress cost — a false economy.",
            },
            "exam_pattern": "Cross-region/internet transfer is costly -> co-locate compute with data, cache, minimize egress.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (data transfer/egress cost)"],
    },
    {
        "id": "cloudplus-ops-r2-017", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A cost audit finds the account is paying for unattached block volumes, idle reserved IP addresses, "
                "load balancers with no targets, and snapshots of long-deleted instances. Which optimization addresses "
                "this waste?",
        "options": [
            {"id": "A", "text": "Reclaiming orphaned/idle resources (decommissioning unused assets)"},
            {"id": "B", "text": "Scaling out by adding instances"},
            {"id": "C", "text": "Purchasing more reserved capacity"},
            {"id": "D", "text": "Increasing backup frequency"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Orphaned resources — unattached volumes, unused IPs, empty load balancers, stale snapshots — accrue charges "
                       "for no benefit. Identifying and decommissioning them is a direct, low-risk cost saving.",
            "distractors": {
                "B": "Adding instances increases cost; the problem is unused resources, not insufficient capacity.",
                "C": "Buying more reserved capacity spends more money and does not remove the existing waste.",
                "D": "More frequent backups add cost; they do not clean up orphaned assets.",
            },
            "exam_pattern": "Pay for unused assets -> find and decommission orphaned/idle resources.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (orphaned/idle resource cleanup)"],
    },
    {
        "id": "cloudplus-ops-r2-018", "exam": "cloudplus", "domain": "cloudp_operations",
        "subtopic": "cloudp_optimization", "difficulty": 2, "type": "mcq",
        "stem": "A team wants object data to move automatically to a cheaper storage class after 30 days and be deleted "
                "after 365 days, with no manual intervention. Which feature accomplishes this?",
        "options": [
            {"id": "A", "text": "A storage lifecycle policy"},
            {"id": "B", "text": "A one-time manual cleanup each quarter"},
            {"id": "C", "text": "A snapshot schedule"},
            {"id": "D", "text": "Cross-region geo-replication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A storage lifecycle policy automates transitions between storage classes and expiration/deletion based on age "
                       "or rules, cutting cost without manual effort.",
            "distractors": {
                "B": "Manual quarterly cleanup is error-prone and not automatic, failing the 'no manual intervention' requirement.",
                "C": "A snapshot schedule creates backups on a timer; it does not tier or expire object data by age.",
                "D": "Geo-replication copies data to another region for resilience; it increases, not reduces, storage footprint and cost.",
            },
            "exam_pattern": "Auto-tier and expire objects by age/rules = storage lifecycle policy.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 3 — Optimization (storage lifecycle policies)"],
    },

    # ===================================================================
    # Domain 5: DevOps Fundamentals  (cloudp_devops)
    # ===================================================================

    # ----- cloudp_cicd -------------------------------------------------
    {
        "id": "cloudplus-dev-r2-001", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "A pipeline automatically builds, tests, and packages every change into a release-ready artifact and "
                "stages it, but a human must click 'approve' before it is promoted to production. Which practice is this?",
        "options": [
            {"id": "A", "text": "Continuous deployment"},
            {"id": "B", "text": "Continuous delivery"},
            {"id": "C", "text": "Continuous integration"},
            {"id": "D", "text": "Continuous monitoring"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Continuous delivery automates everything up to a release-ready artifact but keeps a manual approval gate "
                       "before production. Continuous deployment removes that gate and releases automatically.",
            "distractors": {
                "A": "Continuous deployment pushes every passing build to production with NO human gate — the scenario has an approval step.",
                "C": "Continuous integration covers building and testing merged code; it does not describe the release-to-production decision.",
                "D": "Continuous monitoring is observing systems in production; it is not a release automation practice.",
            },
            "exam_pattern": "Automated to release-ready, manual approval before prod = continuous delivery; no gate = continuous deployment.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (continuous delivery vs deployment)"],
    },
    {
        "id": "cloudplus-dev-r2-002", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "A team upgrades a service by gradually replacing the instances running the old version with instances "
                "running the new version, a few at a time, within the SAME environment until all are updated. Which "
                "deployment strategy is this?",
        "options": [
            {"id": "A", "text": "Blue-green deployment"},
            {"id": "B", "text": "Canary deployment"},
            {"id": "C", "text": "Rolling deployment"},
            {"id": "D", "text": "Big-bang deployment"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A rolling deployment incrementally replaces old instances with new ones in batches within one environment, "
                       "avoiding a full second environment while keeping the service available throughout.",
            "distractors": {
                "A": "Blue-green stands up a second full environment and cuts traffic over all at once, not a gradual in-place replacement.",
                "B": "A canary routes a small percentage of users to the new version first to evaluate it, rather than replacing instances batch by batch for everyone.",
                "D": "Big-bang replaces everything at once, with no gradual batching.",
            },
            "exam_pattern": "Replace instances in batches in one environment = rolling; two environments cut over = blue-green; small % first = canary.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (rolling deployment)"],
    },
    {
        "id": "cloudplus-dev-r2-003", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "After a pipeline builds versioned packages and container images, it needs a central, versioned store to "
                "hold these build outputs so later stages can pull and promote the exact same binaries. Which component "
                "provides this?",
        "options": [
            {"id": "A", "text": "A source/version control repository"},
            {"id": "B", "text": "A SIEM"},
            {"id": "C", "text": "A configuration management database (CMDB)"},
            {"id": "D", "text": "An artifact repository"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An artifact repository stores and versions BUILD OUTPUTS (packages, libraries, container images) so pipelines "
                       "can promote the identical, tested binary through environments rather than rebuilding it.",
            "distractors": {
                "A": "Source/version control stores the SOURCE CODE and its history, not the compiled/built artifacts.",
                "B": "A SIEM correlates security events; it does not store build artifacts.",
                "C": "A CMDB tracks configuration items and relationships; it is not a binary artifact store.",
            },
            "exam_pattern": "Store/version built binaries and images = artifact repository; store source code = version control.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (artifact repository)"],
    },
    {
        "id": "cloudplus-dev-r2-004", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 3, "type": "mcq",
        "stem": "New code for a feature is already deployed to production but kept switched OFF; the team can then enable "
                "it for specific users without another deployment, and disable it instantly if problems appear. Which "
                "technique decouples release from deployment like this?",
        "options": [
            {"id": "A", "text": "A canary release"},
            {"id": "B", "text": "A feature flag (feature toggle)"},
            {"id": "C", "text": "A blue-green deployment"},
            {"id": "D", "text": "A rollback"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A feature flag (toggle) lets already-deployed code be turned on or off at runtime for chosen users, separating "
                       "the act of deploying from the act of releasing and enabling instant disable without redeploying.",
            "distractors": {
                "A": "A canary shifts a small share of traffic to a new deployed version; it does not toggle a dormant feature already shipped to everyone.",
                "C": "Blue-green swaps whole environments; it is not a runtime on/off switch for individual features.",
                "D": "A rollback reverts to a previous deployment; a feature flag disables a feature without redeploying at all.",
            },
            "exam_pattern": "Ship code off, toggle on/off at runtime per user = feature flag (decouples deploy from release).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (feature flags)"],
    },

    # ----- cloudp_iac --------------------------------------------------
    {
        "id": "cloudplus-dev-r2-005", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 3, "type": "mcq",
        "stem": "An automation script spells out the exact ordered commands to run — create the network, THEN create the "
                "subnet, THEN launch the instance — explicitly controlling each step and its sequence. Which IaC style is "
                "this?",
        "options": [
            {"id": "A", "text": "Declarative"},
            {"id": "B", "text": "Idempotent"},
            {"id": "C", "text": "Imperative (procedural)"},
            {"id": "D", "text": "Immutable"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An imperative (procedural) approach specifies the explicit sequence of commands/steps to reach the result. "
                       "A declarative approach instead states the desired end state and lets the tool work out the steps.",
            "distractors": {
                "A": "Declarative code states the end state (what), not the ordered commands (how) the scenario lays out.",
                "B": "Idempotency is a property (re-running yields the same state), not the step-by-step style described.",
                "D": "Immutable refers to replacing rather than modifying infrastructure, not to specifying ordered commands.",
            },
            "exam_pattern": "Explicit ordered commands (how) = imperative; desired end state (what) = declarative.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (imperative vs declarative)"],
    },
    {
        "id": "cloudplus-dev-r2-006", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 3, "type": "mcq",
        "stem": "A team's policy is that servers are NEVER patched or modified after deployment. To change anything, they "
                "build a brand-new image, deploy fresh instances from it, and destroy the old ones. Which model is this?",
        "options": [
            {"id": "A", "text": "Mutable infrastructure"},
            {"id": "B", "text": "Immutable infrastructure"},
            {"id": "C", "text": "Configuration drift"},
            {"id": "D", "text": "Vertical scaling"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Immutable infrastructure replaces instances with newly built images instead of changing running servers. This "
                       "eliminates configuration drift and makes deployments predictable and easy to roll back by redeploying a prior image.",
            "distractors": {
                "A": "Mutable infrastructure updates servers in place over time — exactly what this policy forbids.",
                "C": "Configuration drift is the problem (servers diverging from baseline) that immutability prevents, not the model itself.",
                "D": "Vertical scaling resizes an instance; it is unrelated to the replace-don't-modify model.",
            },
            "exam_pattern": "Never modify in place; rebuild and replace from images = immutable infrastructure (prevents drift).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (mutable vs immutable infrastructure)"],
    },
    {
        "id": "cloudplus-dev-r2-007", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 3, "type": "mcq",
        "stem": "A declarative IaC tool keeps a file recording the resources it currently manages and their last-known "
                "attributes, which it compares against the configuration to decide what to create, change, or destroy on "
                "the next run. What is this file called?",
        "options": [
            {"id": "A", "text": "A golden image"},
            {"id": "B", "text": "A configuration management database (CMDB)"},
            {"id": "C", "text": "A state file (state management)"},
            {"id": "D", "text": "A snapshot"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The state file records what the IaC tool manages and the resources' last-known state, so the tool can compute "
                       "the difference between desired configuration and reality (including detecting drift) and apply only needed changes.",
            "distractors": {
                "A": "A golden image is a standardized base image for instances, not a record of managed-resource state.",
                "B": "A CMDB is a broader IT asset/relationship database, not the IaC tool's own working state record.",
                "D": "A snapshot is a point-in-time copy of a volume/VM, not an IaC resource-state tracking file.",
            },
            "exam_pattern": "IaC's record of managed resources used to plan changes/detect drift = state file.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (state management)"],
    },

    # ----- cloudp_automation_scripting ---------------------------------
    {
        "id": "cloudplus-dev-r2-008", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "An automation script needs an API key and a database password to run. What is the SECURE way to supply "
                "these credentials?",
        "options": [
            {"id": "A", "text": "Retrieve them at runtime from a secrets manager/vault rather than storing them in code"},
            {"id": "B", "text": "Hardcode them directly in the script"},
            {"id": "C", "text": "Commit them into the Git repository for convenience"},
            {"id": "D", "text": "Email the credentials to everyone on the team"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secrets should be stored in a dedicated secrets manager/vault and fetched at runtime (often injected via "
                       "short-lived tokens), so credentials never live in source code, logs, or images and can be rotated centrally.",
            "distractors": {
                "B": "Hardcoding credentials exposes them to anyone who reads the script or its history and makes rotation painful.",
                "C": "Committing secrets to version control leaks them to everyone with repo access and persists them in history.",
                "D": "Emailing credentials scatters secrets insecurely and cannot be controlled or rotated.",
            },
            "exam_pattern": "Never hardcode/commit secrets; pull them from a secrets manager/vault at runtime.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (secrets management)"],
    },
    {
        "id": "cloudplus-dev-r2-009", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "A script calls a cloud provider's REST API that requires proof of identity on every request. Which is "
                "the standard way for the script to authenticate its API calls?",
        "options": [
            {"id": "A", "text": "No authentication is needed for REST APIs"},
            {"id": "B", "text": "Present a token/key (e.g., a bearer token in the Authorization header)"},
            {"id": "C", "text": "Place the root password in the URL query string"},
            {"id": "D", "text": "Send an ICMP ping before each call"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cloud REST APIs authenticate callers with a credential such as an API key or OAuth/bearer token, commonly "
                       "presented in the Authorization header (or a signed request), proving the caller's identity on each request.",
            "distractors": {
                "A": "Management REST APIs require authentication; unauthenticated access would be a serious security flaw.",
                "C": "Putting a root password in a URL exposes it in logs and history and is never the standard, secure method.",
                "D": "An ICMP ping tests reachability; it does not authenticate API requests.",
            },
            "exam_pattern": "Authenticate REST API calls with a token/key (e.g., bearer token in Authorization header).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (API authentication)"],
    },
    {
        "id": "cloudplus-dev-r2-010", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to call cloud provider operations directly from within a Python application, using "
                "native language objects and methods instead of shelling out or crafting raw HTTP requests. Which tool is "
                "designed for this?",
        "options": [
            {"id": "A", "text": "The provider's web console"},
            {"id": "B", "text": "RDP to a management server"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A software development kit (SDK)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An SDK is a language-specific library that wraps the provider's REST API in native objects/methods, letting "
                       "developers integrate cloud operations directly into application code (handling auth, retries, and serialization).",
            "distractors": {
                "A": "The web console is a manual, point-and-click GUI, not a way to call operations from within code.",
                "B": "RDP provides interactive desktop access to a server; it is not a programming interface for cloud operations.",
                "C": "A load balancer distributes traffic; it is not a developer tool for invoking cloud APIs from code.",
            },
            "exam_pattern": "Call cloud APIs from application code in a given language = SDK; interactive shell = CLI; GUI = console.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (SDK vs CLI vs API/console)"],
    },

    # ===================================================================
    # Domain 6: Troubleshooting  (cloudp_troubleshooting)
    # ===================================================================

    # ----- cloudp_ts_methodology ---------------------------------------
    {
        "id": "cloudplus-ts-r2-001", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "mcq",
        "stem": "A technician has tested and CONFIRMED that a misconfigured route table is the cause of an outage. "
                "According to the CompTIA troubleshooting methodology, what is the NEXT step?",
        "options": [
            {"id": "A", "text": "Re-test the theory a second time"},
            {"id": "B", "text": "Establish a plan of action to resolve the problem (and identify potential effects)"},
            {"id": "C", "text": "Document findings and close the ticket"},
            {"id": "D", "text": "Verify full system functionality"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Once the theory is confirmed, the methodology moves to establishing a plan of action to resolve the problem "
                       "and identify potential effects — before implementing the solution.",
            "distractors": {
                "A": "The theory is already confirmed; re-testing it is unnecessary and not the defined next step.",
                "C": "Documentation is the final step, after the fix is implemented and functionality verified.",
                "D": "Verifying full functionality comes after the solution is implemented, not immediately after confirming the cause.",
            },
            "exam_pattern": "Confirmed cause -> establish a plan of action -> implement -> verify -> document.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology (plan of action)"],
    },
    {
        "id": "cloudplus-ts-r2-002", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "mcq",
        "stem": "A technician tests a theory of probable cause, but the test does NOT confirm it. According to the "
                "methodology, what should they do?",
        "options": [
            {"id": "A", "text": "Implement the planned fix anyway"},
            {"id": "B", "text": "Document the outcome and close the ticket"},
            {"id": "C", "text": "Reboot all systems and hope it resolves"},
            {"id": "D", "text": "Establish a new theory (or escalate if needed)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "If testing does not confirm the theory, you establish a new theory of probable cause — or escalate when the "
                       "problem is beyond your access or expertise — rather than proceeding to a fix based on an unconfirmed cause.",
            "distractors": {
                "A": "Implementing a fix for an unconfirmed cause risks wasted effort and new problems; the cause must be confirmed first.",
                "B": "The problem is unresolved, so documenting and closing is premature.",
                "C": "Rebooting everything blindly is not a methodical step and may cause further disruption.",
            },
            "exam_pattern": "Theory not confirmed -> form a new theory or escalate; never fix on an unconfirmed cause.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology (unconfirmed theory)"],
    },
    {
        "id": "cloudplus-ts-r2-003", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_methodology", "difficulty": 2, "type": "mcq",
        "stem": "While testing fixes, a disciplined technician changes only ONE setting at a time and re-tests before "
                "changing anything else. Why is this the preferred practice?",
        "options": [
            {"id": "A", "text": "To make changes faster by batching many at once"},
            {"id": "B", "text": "To avoid having to verify functionality later"},
            {"id": "C", "text": "So the effect of each change is isolated and the actual fix can be identified"},
            {"id": "D", "text": "To avoid documenting the change"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Changing one variable at a time isolates cause and effect, so you know exactly which change resolved (or "
                       "worsened) the issue and can cleanly roll back anything that did not help.",
            "distractors": {
                "A": "Batching many changes is the opposite of the practice and obscures which change had an effect.",
                "B": "Verifying functionality is still required; isolating changes does not remove that step.",
                "D": "Good troubleshooting still documents changes; isolation is about attribution, not skipping documentation.",
            },
            "exam_pattern": "Change one thing at a time to isolate cause/effect and identify the real fix.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Troubleshooting methodology (isolating variables)"],
    },

    # ----- cloudp_ts_deployment ----------------------------------------
    {
        "id": "cloudplus-ts-r2-004", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A deployment template is syntactically valid and worked for a colleague, but when a new engineer runs "
                "it, creating resources fails with 'AccessDenied / not authorized.' What is the most likely cause?",
        "options": [
            {"id": "A", "text": "The instance CPU size is too small"},
            {"id": "B", "text": "The identity/role running the deployment lacks the required IAM permissions"},
            {"id": "C", "text": "The DNS TTL is set too high"},
            {"id": "D", "text": "An MTU mismatch on the network"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An authorization error on resource creation points to insufficient IAM permissions for the identity/role "
                       "running the deployment; grant the needed permissions (least privilege) to that principal.",
            "distractors": {
                "A": "Instance CPU size affects performance, not an authorization failure to create resources.",
                "C": "DNS TTL governs record caching; it does not cause 'AccessDenied' during provisioning.",
                "D": "An MTU mismatch causes packet-size network issues, not an authorization error.",
            },
            "exam_pattern": "'AccessDenied/not authorized' creating resources = missing IAM permissions on the deploying identity.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (permissions/IAM)"],
    },
    {
        "id": "cloudplus-ts-r2-005", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 3, "type": "mcq",
        "stem": "An IaC deployment fails partway: a load balancer resource errors out because it references a target "
                "group / subnet that does not exist yet at the moment it is created. What is the most likely cause?",
        "options": [
            {"id": "A", "text": "An expired TLS certificate"},
            {"id": "B", "text": "Over-provisioning of compute"},
            {"id": "C", "text": "An unmet resource dependency / incorrect creation ordering"},
            {"id": "D", "text": "A noisy neighbor on the host"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When one resource references another that has not been created yet, it is a dependency/ordering problem. The "
                       "template must declare dependencies so the engine builds prerequisites first (or the reference must be corrected).",
            "distractors": {
                "A": "An expired certificate causes TLS trust errors, not a 'referenced resource does not exist yet' failure.",
                "B": "Over-provisioning wastes capacity; it does not cause an ordering/dependency error.",
                "D": "A noisy neighbor degrades performance; it does not cause a missing-dependency provisioning failure.",
            },
            "exam_pattern": "Resource references something not yet created = unmet dependency/ordering; declare dependencies.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (dependencies/ordering)"],
    },
    {
        "id": "cloudplus-ts-r2-006", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_deployment", "difficulty": 3, "type": "mcq",
        "stem": "A launch of a specific large instance type intermittently fails with 'insufficient capacity' in one "
                "availability zone, even though the account is well under its service quota. What is the best "
                "explanation and remedy?",
        "options": [
            {"id": "A", "text": "The account quota is exceeded; request a quota increase"},
            {"id": "B", "text": "The template has a syntax error; validate the JSON/YAML"},
            {"id": "C", "text": "DNS resolution is failing; check the resolver"},
            {"id": "D", "text": "The provider temporarily lacks that instance type's capacity in that zone; try another zone or instance type"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "'Insufficient capacity' while under quota means the provider itself is temporarily out of that instance type "
                       "in that zone. Retrying in another availability zone, choosing a different instance type, or retrying later resolves it.",
            "distractors": {
                "A": "A quota problem reports a limit/quota error (e.g., 'LimitExceeded'); here the account is under quota, so quota is not the cause.",
                "B": "A syntax error fails before any resource is attempted, not intermittently on one instance type in one zone.",
                "C": "DNS resolution issues do not produce a provider capacity error during instance launch.",
            },
            "exam_pattern": "'Insufficient capacity' but under quota = provider capacity shortage in that AZ; try another AZ/type.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Deployment issues (capacity vs quota)"],
    },

    # ----- cloudp_ts_connectivity --------------------------------------
    {
        "id": "cloudplus-ts-r2-007", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 3, "type": "mcq",
        "stem": "An attempt to peer two virtual networks (or to connect an on-prem network to a cloud VNet) fails or "
                "routes incorrectly because both use the same 10.0.0.0/16 address range. What is the root cause?",
        "options": [
            {"id": "A", "text": "A DNS misconfiguration"},
            {"id": "B", "text": "Overlapping / conflicting CIDR ranges between the networks"},
            {"id": "C", "text": "An MTU mismatch"},
            {"id": "D", "text": "An expired access key"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Peering or routing between networks requires non-overlapping address space. Identical/overlapping CIDR ranges "
                       "make destinations ambiguous, so peering is rejected or traffic misroutes; re-IP one side or use distinct ranges.",
            "distractors": {
                "A": "DNS maps names to addresses; it does not cause an address-range conflict between peered networks.",
                "C": "An MTU mismatch affects packet sizing on an established path, not the ability to peer overlapping ranges.",
                "D": "An expired access key causes authentication failures, not an IP-range routing conflict.",
            },
            "exam_pattern": "Peering/routing fails with identical ranges = overlapping CIDR; networks must use distinct address space.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (overlapping CIDR/routing)"],
    },
    {
        "id": "cloudplus-ts-r2-008", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Instances in a subnet can reach each other but none can reach the internet. The security groups allow "
                "outbound traffic, and DNS works. Which configuration should you check next?",
        "options": [
            {"id": "A", "text": "A DNS resolver failure"},
            {"id": "B", "text": "Host memory pressure"},
            {"id": "C", "text": "A missing default route (0.0.0.0/0) to the internet gateway in the route table"},
            {"id": "D", "text": "A failed RAID array"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Local subnet traffic works but internet access fails points to routing: the subnet's route table likely lacks "
                       "a default route (0.0.0.0/0) pointing to an internet gateway, so outbound internet traffic has no path.",
            "distractors": {
                "A": "DNS is stated to be working, so name resolution is not the issue here.",
                "B": "Memory pressure degrades performance on a host; it does not block a whole subnet's internet routing.",
                "D": "A RAID failure is a storage problem, unrelated to subnet internet routing.",
            },
            "exam_pattern": "Local works, internet fails, SG/DNS fine -> check for a missing default route to the internet gateway.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (routing/default route)"],
    },
    {
        "id": "cloudplus-ts-r2-009", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "After an administrator updates a DNS record to point a hostname at a new server's IP, some users reach "
                "the new server immediately while others keep hitting the old IP for hours. What is the most likely "
                "cause?",
        "options": [
            {"id": "A", "text": "An MTU mismatch on the path"},
            {"id": "B", "text": "DNS caching: resolvers/clients hold the old record until its TTL expires"},
            {"id": "C", "text": "A security group blocking the new server"},
            {"id": "D", "text": "The account exceeded a service quota"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DNS responses are cached for the record's TTL. Until each resolver/client's cached entry expires, it keeps "
                       "using the old IP, so the change appears to roll out gradually. A lower TTL set beforehand speeds future cutovers.",
            "distractors": {
                "A": "An MTU mismatch affects large packet transfers, not which IP a hostname resolves to.",
                "C": "A security group block would stop connectivity entirely for affected clients, not serve the OLD IP to some users.",
                "D": "A service quota limits resource counts; it does not cause stale name resolution.",
            },
            "exam_pattern": "Some users hit old IP after a DNS change = cached records until TTL expires; pre-lower TTL before cutover.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Connectivity (DNS TTL/propagation)"],
    },

    # ----- cloudp_ts_performance ---------------------------------------
    {
        "id": "cloudplus-ts-r2-010", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 3, "type": "mcq",
        "stem": "A volume delivers excellent I/O for the first few minutes of a heavy job, then its throughput suddenly "
                "drops to a much lower, steady level for the rest of the run. CPU and memory are fine. What is the most "
                "likely cause?",
        "options": [
            {"id": "A", "text": "CPU saturation"},
            {"id": "B", "text": "Memory swapping"},
            {"id": "C", "text": "Storage I/O throttling after the volume's burst credits/allowance are exhausted"},
            {"id": "D", "text": "DNS resolution latency"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Many cloud volumes allow bursting above a baseline using credits; when the credits are depleted, performance "
                       "drops to the sustained baseline IOPS/throughput — matching the 'fast then steady-slow' pattern. Provision higher baseline IOPS or a faster tier.",
            "distractors": {
                "A": "CPU is reported fine, so processing is not the constraint.",
                "B": "Memory is fine and there is no swapping signature; this is a storage throughput pattern.",
                "D": "DNS latency affects name lookups, not sustained disk throughput that steps down after a burst.",
            },
            "exam_pattern": "Fast then steps down to a steady floor = burst credits exhausted -> baseline IOPS throttling.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (IOPS throttling/burst credits)"],
    },
    {
        "id": "cloudplus-ts-r2-011", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 3, "type": "mcq",
        "stem": "A VM on shared, multi-tenant hardware shows unpredictable performance dips that correlate with nothing "
                "in its own metrics (CPU, memory, disk, and network all look normal inside the guest). Which cause should "
                "be suspected?",
        "options": [
            {"id": "A", "text": "A memory leak in the application"},
            {"id": "B", "text": "A noisy neighbor: another tenant on the same physical host contending for shared resources"},
            {"id": "C", "text": "A DNS misconfiguration"},
            {"id": "D", "text": "An expired TLS certificate"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A noisy neighbor is another tenant on the same physical host consuming shared CPU, cache, disk, or network "
                       "bandwidth, degrading your VM even though its own guest metrics look normal. Dedicated hosts or moving the instance mitigates it.",
            "distractors": {
                "A": "A memory leak would show rising memory use inside the guest — but the guest's own metrics are normal here.",
                "C": "A DNS misconfiguration causes name-resolution failures, not intermittent host-contention dips.",
                "D": "An expired certificate causes TLS errors, not random performance contention.",
            },
            "exam_pattern": "Random dips on shared hardware with normal guest metrics = noisy neighbor (resource contention).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (noisy neighbor/multitenancy)"],
    },
    {
        "id": "cloudplus-ts-r2-012", "exam": "cloudplus", "domain": "cloudp_troubleshooting",
        "subtopic": "cloudp_ts_performance", "difficulty": 3, "type": "mcq",
        "stem": "Under heavy load, a web application starts returning errors like 'too many connections' and requests "
                "queue up, yet the database server's CPU, memory, and disk are all only moderately used. What is the most "
                "likely bottleneck?",
        "options": [
            {"id": "A", "text": "The database connection pool / maximum-connections limit is exhausted"},
            {"id": "B", "text": "Disk IOPS saturation"},
            {"id": "C", "text": "DNS resolution failure"},
            {"id": "D", "text": "An MTU mismatch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Too many connections' with healthy CPU/memory/disk indicates the connection pool or the database's "
                       "max-connections limit is exhausted — a configuration/concurrency bottleneck. Tune pool size/limits or add pooling, not more hardware.",
            "distractors": {
                "B": "Disk IOPS saturation would show high disk utilization and queue depth; here disk is only moderate.",
                "C": "A DNS failure prevents connecting at all by name; it does not produce a 'too many connections' limit error.",
                "D": "An MTU mismatch causes size-dependent packet loss, not a connection-count limit error.",
            },
            "exam_pattern": "'Too many connections' with hardware fine = connection pool / max-connections limit exhausted.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 6 — Performance (connection limits/pool exhaustion)"],
    },
]
