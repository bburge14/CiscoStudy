"""AWS Certified Cloud Practitioner (CLF-C02) pool — Domain 1: Cloud Concepts.

Original, objective-aligned practice items for the four Cloud Concepts
subtopics tracked in CertLab:
  * cloud_benefits   — the advantages of cloud computing (variable cost,
                       economies of scale, elasticity, agility, global reach,
                       stop guessing capacity, high availability).
  * well_architected — the six pillars of the AWS Well-Architected Framework
                       and its core design principles.
  * migration_caf    — the AWS Cloud Adoption Framework perspectives, the 6 R's
                       migration strategies, and the Snow Family transfer concept.
  * cloud_economics  — CapEx vs OpEx, total cost of ownership, pay-as-you-go /
                       consumption pricing, right-sizing, economies of scale.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the answer key authored here as "A" is not
positionally biased, every wrong option carries a distractor note, and each item
names the AWS doc/whitepaper/service area it draws on so facts stay traceable.
Cloud-Practitioner depth only (concepts, purpose, when-to-use) — no numeric
limits/prices, no region/version trivia, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cloud_benefits ===================================================
    {
        "id": "clf-cc-001", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A startup wants to avoid buying and owning servers up front and instead "
                "pay only for the compute capacity it actually consumes. Which cloud benefit is this?",
        "options": [
            {"id": "A", "text": "Trade fixed capital expense for variable expense"},
            {"id": "B", "text": "Benefit from massive economies of scale"},
            {"id": "C", "text": "Go global in minutes"},
            {"id": "D", "text": "Increase speed and agility"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Paying only for capacity you consume instead of purchasing hardware up front "
                       "is the 'trade capital expense for variable expense' advantage: cost scales "
                       "with actual use rather than being locked in before launch.",
            "distractors": {
                "B": "Economies of scale is about lower prices from AWS aggregating many customers' "
                     "usage, not about the capital-to-variable payment shift itself.",
                "C": "Going global in minutes is about deploying to multiple Regions quickly, not "
                     "about how you pay for resources.",
                "D": "Speed and agility is about provisioning resources fast to innovate, not the "
                     "capital-versus-variable cost model.",
            },
            "exam_pattern": "'Pay only for what you use / avoid up-front hardware purchase' = trade "
                            "capital expense for variable expense.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-002", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Because AWS aggregates usage from hundreds of thousands of customers, it can offer "
                "lower pay-as-you-go prices than one company could achieve alone. Which benefit is this?",
        "options": [
            {"id": "A", "text": "Benefit from massive economies of scale"},
            {"id": "B", "text": "Stop guessing capacity"},
            {"id": "C", "text": "Trade capital expense for variable expense"},
            {"id": "D", "text": "Elasticity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Aggregated demand from many customers lets AWS achieve higher economies of "
                       "scale and pass the savings on as lower pay-as-you-go prices.",
            "distractors": {
                "B": "Stopping capacity guesswork is about not having to predict infrastructure "
                     "needs, not about pricing driven by aggregated demand.",
                "C": "The capital-to-variable shift changes how you pay; the lower unit price from "
                     "scale is a separate advantage.",
                "D": "Elasticity is automatically adding and removing resources with demand, not the "
                     "provider's pricing.",
            },
            "exam_pattern": "'Aggregated customer demand leads to lower prices' = economies of scale.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-003", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "An online store's traffic triples during a flash sale, then returns to normal; it "
                "automatically adds compute during the surge and releases it afterward. Which "
                "cloud characteristic is this?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Durability"},
            {"id": "C", "text": "Economies of scale"},
            {"id": "D", "text": "Fault tolerance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elasticity is automatically acquiring resources as demand rises and releasing "
                       "them as it falls, so you pay only for what the workload currently needs.",
            "distractors": {
                "B": "Durability describes how well stored data is protected from loss, not scaling "
                     "compute with demand.",
                "C": "Economies of scale is about lower prices from aggregated demand, not automatic "
                     "scaling to match load.",
                "D": "Fault tolerance is a system's ability to keep operating despite component "
                     "failure, not matching capacity to changing load.",
            },
            "exam_pattern": "'Automatically scale out under load and scale in when idle' = elasticity.",
        },
        "references": ["AWS - Overview of Amazon Web Services whitepaper (cloud computing concepts)"],
    },
    {
        "id": "clf-cc-004", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "multi",
        "stem": "An enterprise is building its cloud business case. Which TWO of the following are "
                "advantages of cloud computing as described by AWS? (Choose two.)",
        "options": [
            {"id": "A", "text": "Go global in minutes"},
            {"id": "B", "text": "Stop guessing capacity"},
            {"id": "C", "text": "Eliminate the customer's share of all security responsibilities"},
            {"id": "D", "text": "Guarantee that applications can never experience downtime"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Going global in minutes (deploying to multiple Regions quickly) and stopping "
                       "capacity guesswork are two of AWS's stated advantages of cloud computing.",
            "distractors": {
                "C": "Security is a shared responsibility; AWS secures the cloud, but the customer "
                     "always keeps responsibilities in the cloud, so the cloud never eliminates them.",
                "D": "No provider guarantees zero downtime; the cloud improves availability and "
                     "resilience but does not promise perfect uptime.",
            },
            "exam_pattern": "Watch for absolutes ('eliminate all', 'never', 'guarantee zero') - they "
                            "are usually wrong cloud-benefit distractors.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-005", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "A team that once waited weeks for hardware procurement can now launch new servers in "
                "minutes and experiment freely. Which cloud benefit does this illustrate?",
        "options": [
            {"id": "A", "text": "Increased speed and agility"},
            {"id": "B", "text": "Benefit from economies of scale"},
            {"id": "C", "text": "Trade capital expense for variable expense"},
            {"id": "D", "text": "High durability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Provisioning resources in minutes lowers the cost of experimenting and lets "
                       "teams innovate and reach market faster - the speed and agility advantage.",
            "distractors": {
                "B": "Economies of scale is about lower prices from aggregated demand, not "
                     "provisioning speed.",
                "C": "The capital-to-variable shift is about how you pay, not how fast you can "
                     "provision resources.",
                "D": "Durability is about protecting stored data from loss, unrelated to how quickly "
                     "you can provision.",
            },
            "exam_pattern": "'Provision in minutes, experiment cheaply, faster time to market' = "
                            "agility / speed.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-006", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to lower latency for customers in Europe and Asia by deploying its "
                "application close to them in several AWS Regions within minutes. Which benefit is this?",
        "options": [
            {"id": "A", "text": "Go global in minutes"},
            {"id": "B", "text": "Elasticity"},
            {"id": "C", "text": "Trade capital expense for variable expense"},
            {"id": "D", "text": "Benefit from economies of scale"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Deploying to multiple AWS Regions quickly to place the application near end "
                       "users, lowering their latency, is the 'go global in minutes' advantage.",
            "distractors": {
                "B": "Elasticity is scaling capacity up and down with demand, not deploying across "
                     "Regions for proximity to users.",
                "C": "The capital-to-variable shift is about the payment model, not global deployment "
                     "speed.",
                "D": "Economies of scale is about pricing from aggregated demand, not multi-Region "
                     "reach.",
            },
            "exam_pattern": "'Deploy near users in multiple Regions to cut latency' = go global in "
                            "minutes.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-007", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 2, "type": "mcq",
        "stem": "Before the cloud, a company often bought too many or too few servers because demand "
                "was hard to predict. How does cloud computing best address this problem?",
        "options": [
            {"id": "A", "text": "It lets the company scale capacity up or down on demand, so it stops guessing capacity"},
            {"id": "B", "text": "It guarantees a fixed block of capacity reserved years in advance"},
            {"id": "C", "text": "It removes the need to monitor usage entirely"},
            {"id": "D", "text": "It requires forecasting peak demand accurately before launch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The cloud lets you scale resources up or down as needed, so you no longer "
                       "over- or under-provision - you 'stop guessing capacity'.",
            "distractors": {
                "B": "Reserving a fixed block of capacity years ahead is the old on-premises model "
                     "the cloud replaces.",
                "C": "You still monitor usage; the cloud removes the guesswork, not the monitoring.",
                "D": "The cloud removes the need to forecast peak demand up front, the opposite of "
                     "this option.",
            },
            "exam_pattern": "'No more over- or under-provisioning; scale with actual demand' = stop "
                            "guessing capacity.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-008", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 1, "type": "mcq",
        "stem": "By moving to AWS, a business no longer racks servers, powers and cools a facility, or "
                "staffs data-center operations, and can focus on customers. Which benefit is this?",
        "options": [
            {"id": "A", "text": "Stop spending money running and maintaining data centers"},
            {"id": "B", "text": "Go global in minutes"},
            {"id": "C", "text": "Elasticity"},
            {"id": "D", "text": "Benefit from economies of scale"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Offloading the heavy lifting of data-center operations - racking, power, "
                       "cooling, and staffing - so the business can focus on its differentiators is "
                       "a core cloud advantage.",
            "distractors": {
                "B": "Going global in minutes is about multi-Region deployment speed, not shedding "
                     "data-center operating costs.",
                "C": "Elasticity is scaling with demand, not eliminating data-center operations.",
                "D": "Economies of scale is about lower prices from aggregated demand, not removing "
                     "facility operations from your plate.",
            },
            "exam_pattern": "'Stop racking/powering/cooling servers; focus on the business' = stop "
                            "spending on data centers (removing undifferentiated heavy lifting).",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (AWS Overview whitepaper)"],
    },
    {
        "id": "clf-cc-009", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_benefits", "difficulty": 3, "type": "mcq",
        "stem": "An architect deploys an application across multiple Availability Zones so it keeps "
                "running if one zone fails. Which cloud benefit is the team primarily pursuing?",
        "options": [
            {"id": "A", "text": "High availability"},
            {"id": "B", "text": "Lower pay-as-you-go pricing"},
            {"id": "C", "text": "Going global in minutes"},
            {"id": "D", "text": "Capital expenditure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spreading a workload across multiple Availability Zones so it survives a "
                       "single-zone failure increases availability and resilience - a key benefit of "
                       "building on the cloud.",
            "distractors": {
                "B": "Multi-AZ deployment targets resilience, not reducing unit prices (that is "
                     "economies of scale).",
                "C": "Going global in minutes refers to multi-Region reach for users and latency; "
                     "multiple AZs within one Region target availability.",
                "D": "Capital expenditure is up-front hardware spend - the opposite of a cloud "
                     "advantage.",
            },
            "exam_pattern": "Multiple AZs = survive a zone failure = high availability; multiple "
                            "Regions = global reach / latency.",
        },
        "references": ["AWS - Global Infrastructure (Regions and Availability Zones)"],
    },

    # ===== well_architected =================================================
    {
        "id": "clf-cc-010", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 1, "type": "mcq",
        "stem": "An organization wants AWS best-practice guidance, organized into six pillars, to "
                "review and improve its cloud architectures over time. Which offering provides this?",
        "options": [
            {"id": "A", "text": "AWS Well-Architected Framework"},
            {"id": "B", "text": "AWS Cloud Adoption Framework"},
            {"id": "C", "text": "AWS Organizations"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Well-Architected Framework provides best practices and questions "
                       "across six pillars to help you build and review secure, reliable, efficient, "
                       "cost-effective, and sustainable workloads.",
            "distractors": {
                "B": "The Cloud Adoption Framework (CAF) guides organizational cloud adoption across "
                     "six perspectives; it is not the architecture-review framework.",
                "C": "AWS Organizations centrally manages multiple AWS accounts; it does not define "
                     "architectural best-practice pillars.",
                "D": "Trusted Advisor is a tool that checks an account against best practices, but "
                     "the six-pillar framework itself is the Well-Architected Framework.",
            },
            "exam_pattern": "Six pillars + architecture best practices/review = Well-Architected "
                            "Framework (CAF is organizational adoption).",
        },
        "references": ["AWS Well-Architected Framework"],
    },
    {
        "id": "clf-cc-011", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 1, "type": "mcq",
        "stem": "A team applies least-privilege permissions, encrypts data at rest and in transit, and "
                "enables traceability of actions. Which Well-Architected pillar do these practices serve?",
        "options": [
            {"id": "A", "text": "Security"},
            {"id": "B", "text": "Reliability"},
            {"id": "C", "text": "Performance Efficiency"},
            {"id": "D", "text": "Cost Optimization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Protecting data, systems, and assets - least privilege, encryption, and "
                       "traceability - is the focus of the Security pillar.",
            "distractors": {
                "B": "Reliability is about a workload performing correctly and recovering from "
                     "failure, not access control or encryption.",
                "C": "Performance Efficiency is about using computing resources efficiently and "
                     "selecting the right resource types.",
                "D": "Cost Optimization is about avoiding unnecessary spend, not protecting data.",
            },
            "exam_pattern": "Least privilege, encryption, traceability, protect data = Security pillar.",
        },
        "references": ["AWS Well-Architected Framework - Security pillar"],
    },
    {
        "id": "clf-cc-012", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "mcq",
        "stem": "A workload must automatically recover from failures, scale horizontally to meet "
                "demand, and have its recovery procedures tested regularly. Which pillar emphasizes this?",
        "options": [
            {"id": "A", "text": "Reliability"},
            {"id": "B", "text": "Operational Excellence"},
            {"id": "C", "text": "Sustainability"},
            {"id": "D", "text": "Security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ensuring a workload performs its intended function correctly and recovers from "
                       "failure - automatic recovery, horizontal scaling, and tested recovery - "
                       "defines the Reliability pillar.",
            "distractors": {
                "B": "Operational Excellence focuses on running and monitoring systems and "
                     "continuously improving processes, not primarily failure recovery.",
                "C": "Sustainability focuses on minimizing environmental impact, not recovery and "
                     "availability.",
                "D": "Security focuses on protecting data and systems, not recovery and scaling for "
                     "availability.",
            },
            "exam_pattern": "Recover from failure, test recovery, scale horizontally = Reliability.",
        },
        "references": ["AWS Well-Architected Framework - Reliability pillar"],
    },
    {
        "id": "clf-cc-013", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "mcq",
        "stem": "An architect selects the most suitable instance types, adopts serverless where "
                "possible, and experiments to use computing resources efficiently. Which pillar is this?",
        "options": [
            {"id": "A", "text": "Performance Efficiency"},
            {"id": "B", "text": "Cost Optimization"},
            {"id": "C", "text": "Reliability"},
            {"id": "D", "text": "Operational Excellence"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Using computing resources efficiently - selecting the right resource "
                       "types/sizes and adopting advanced technologies such as serverless - is the "
                       "Performance Efficiency pillar.",
            "distractors": {
                "B": "Cost Optimization targets eliminating unneeded spend; efficient selection can "
                     "aid cost, but the stated goal here is efficient performance.",
                "C": "Reliability targets correct operation and recovery from failure, not efficient "
                     "use of resources.",
                "D": "Operational Excellence targets running, monitoring, and improving operations, "
                     "not resource efficiency.",
            },
            "exam_pattern": "Select the right/efficient resources, use serverless, experiment = "
                            "Performance Efficiency.",
        },
        "references": ["AWS Well-Architected Framework - Performance Efficiency pillar"],
    },
    {
        "id": "clf-cc-014", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to avoid paying for idle resources, adopt a consumption model, and "
                "attribute spending to the teams that incur it. Which Well-Architected pillar is this?",
        "options": [
            {"id": "A", "text": "Cost Optimization"},
            {"id": "B", "text": "Performance Efficiency"},
            {"id": "C", "text": "Operational Excellence"},
            {"id": "D", "text": "Sustainability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Avoiding unnecessary costs, adopting a consumption model, and attributing "
                       "expenditure are core practices of the Cost Optimization pillar.",
            "distractors": {
                "B": "Performance Efficiency is about using resources efficiently for performance, "
                     "not controlling and attributing spend.",
                "C": "Operational Excellence is about operations and continuous improvement, not cost "
                     "control.",
                "D": "Sustainability is about reducing environmental impact; it can reduce cost but "
                     "is not focused on managing expenditure.",
            },
            "exam_pattern": "Eliminate idle spend, consumption model, cost attribution = Cost "
                            "Optimization.",
        },
        "references": ["AWS Well-Architected Framework - Cost Optimization pillar"],
    },
    {
        "id": "clf-cc-015", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "multi",
        "stem": "A study group lists candidates for the pillars of the AWS Well-Architected Framework. "
                "Which TWO of the following are actual pillars of the framework? (Choose two.)",
        "options": [
            {"id": "A", "text": "Sustainability"},
            {"id": "B", "text": "Operational Excellence"},
            {"id": "C", "text": "Elasticity"},
            {"id": "D", "text": "Scalability"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Sustainability and Operational Excellence are two of the six Well-Architected "
                       "pillars (the others are Security, Reliability, Performance Efficiency, and "
                       "Cost Optimization).",
            "distractors": {
                "C": "Elasticity is a cloud characteristic and design principle, not one of the six "
                     "named pillars.",
                "D": "Scalability is a cloud characteristic, not a pillar of the framework.",
            },
            "exam_pattern": "Six pillars: Operational Excellence, Security, Reliability, Performance "
                            "Efficiency, Cost Optimization, Sustainability - elasticity/scalability "
                            "are concepts, not pillars.",
        },
        "references": ["AWS Well-Architected Framework"],
    },
    {
        "id": "clf-cc-016", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 1, "type": "mcq",
        "stem": "A team performs operations as code, makes frequent small reversible changes, and "
                "continuously improves its processes and procedures. Which pillar describes this?",
        "options": [
            {"id": "A", "text": "Operational Excellence"},
            {"id": "B", "text": "Reliability"},
            {"id": "C", "text": "Security"},
            {"id": "D", "text": "Cost Optimization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Running and monitoring systems while continuously improving processes - "
                       "operations as code, with small frequent reversible changes - is the "
                       "Operational Excellence pillar.",
            "distractors": {
                "B": "Reliability focuses on correct operation and recovery from failure, not "
                     "operations-as-code and process improvement.",
                "C": "Security focuses on protecting data and systems.",
                "D": "Cost Optimization focuses on avoiding unnecessary spend.",
            },
            "exam_pattern": "Operations as code, small reversible changes, continuous improvement = "
                            "Operational Excellence.",
        },
        "references": ["AWS Well-Architected Framework - Operational Excellence pillar"],
    },
    {
        "id": "clf-cc-017", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 2, "type": "mcq",
        "stem": "An architect wants to reduce a workload's environmental impact by maximizing resource "
                "utilization and using efficient managed services. Which pillar is this?",
        "options": [
            {"id": "A", "text": "Sustainability"},
            {"id": "B", "text": "Cost Optimization"},
            {"id": "C", "text": "Performance Efficiency"},
            {"id": "D", "text": "Reliability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Minimizing environmental impact - by maximizing utilization and using "
                       "efficient managed services - is the Sustainability pillar, added to the "
                       "framework in 2021.",
            "distractors": {
                "B": "Cost Optimization targets spend; higher utilization can cut cost, but reducing "
                     "environmental impact is the Sustainability aim.",
                "C": "Performance Efficiency targets efficient performance, not environmental "
                     "footprint.",
                "D": "Reliability targets correct operation and recovery, not sustainability.",
            },
            "exam_pattern": "Minimize environmental impact, maximize utilization = Sustainability "
                            "pillar.",
        },
        "references": ["AWS Well-Architected Framework - Sustainability pillar"],
    },
    {
        "id": "clf-cc-018", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "well_architected", "difficulty": 3, "type": "mcq",
        "stem": "To improve resilience, an architect removes a tight dependency between two components "
                "by placing a message queue between them so one can fail without stopping the other. "
                "Which design principle is applied?",
        "options": [
            {"id": "A", "text": "Decouple your components"},
            {"id": "B", "text": "Over-provision fixed capacity"},
            {"id": "C", "text": "Treat servers as pets, not cattle"},
            {"id": "D", "text": "Scale vertically only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Loosely coupling components - for example by using a queue between them - so "
                       "one component's failure is isolated is a core AWS design principle that "
                       "improves reliability and scalability.",
            "distractors": {
                "B": "Over-provisioning fixed capacity is the on-premises approach the cloud's "
                     "elasticity replaces, not a resilience design principle.",
                "C": "'Pets, not cattle' is the opposite of the best practice; you treat servers as "
                     "disposable (cattle), not unique and irreplaceable (pets).",
                "D": "Scaling vertically only caps growth at one instance's size; AWS best practice "
                     "favors horizontal scaling for resilience.",
            },
            "exam_pattern": "Queue / loose coupling so one failure does not cascade = decouple; "
                            "disposable resources = design for failure.",
        },
        "references": ["AWS Well-Architected Framework (design principles)"],
    },

    # ===== migration_caf ====================================================
    {
        "id": "clf-cc-019", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "To meet a data-center exit deadline, a company moves its applications to AWS as-is, "
                "with no code changes, to migrate quickly. Which migration strategy is this?",
        "options": [
            {"id": "A", "text": "Rehost (\"lift and shift\")"},
            {"id": "B", "text": "Refactor / re-architect"},
            {"id": "C", "text": "Repurchase"},
            {"id": "D", "text": "Retire"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Rehosting ('lift and shift') moves applications to the cloud without changing "
                       "them - the fastest way to migrate, often ahead of later optimization.",
            "distractors": {
                "B": "Refactoring re-architects the application (for example to cloud-native "
                     "microservices), which takes much more time and change.",
                "C": "Repurchasing replaces the app with a different product, typically SaaS, rather "
                     "than moving it unchanged.",
                "D": "Retiring decommissions applications that are no longer needed, not moving them.",
            },
            "exam_pattern": "Move as-is, no changes, fast = rehost (lift and shift).",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-020", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "While migrating, a team keeps its application's core architecture but moves its "
                "self-managed database onto Amazon RDS to cut admin effort. Which strategy is this?",
        "options": [
            {"id": "A", "text": "Replatform (\"lift, tinker, and shift\")"},
            {"id": "B", "text": "Rehost"},
            {"id": "C", "text": "Refactor / re-architect"},
            {"id": "D", "text": "Retain"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Replatforming makes a few cloud optimizations - such as moving to a managed "
                       "database - for clear benefit, without changing the application's core "
                       "architecture.",
            "distractors": {
                "B": "Rehosting moves the app entirely as-is, with no optimizations like switching to "
                     "a managed database.",
                "C": "Refactoring fundamentally re-architects the application, far more change than a "
                     "managed-database swap.",
                "D": "Retain means leaving the application where it is for now, not migrating and "
                     "optimizing it.",
            },
            "exam_pattern": "A few optimizations (for example a managed DB) but the same core "
                            "architecture = replatform.",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-021", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "A company decides to drop its self-hosted CRM and move to a commercial SaaS CRM "
                "subscription instead. Which of the 6 R's migration strategies is this?",
        "options": [
            {"id": "A", "text": "Repurchase (\"drop and shop\")"},
            {"id": "B", "text": "Replatform"},
            {"id": "C", "text": "Rehost"},
            {"id": "D", "text": "Retain"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Repurchasing ('drop and shop') replaces an existing application by moving to a "
                       "different product, commonly a SaaS offering.",
            "distractors": {
                "B": "Replatforming optimizes the same application; it does not switch to a different "
                     "purchased product.",
                "C": "Rehosting moves the existing application to the cloud unchanged, not to a new "
                     "SaaS product.",
                "D": "Retain leaves the application in place; here the company is actively changing "
                     "products.",
            },
            "exam_pattern": "Switch to a different product, usually SaaS = repurchase (drop and shop).",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-022", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 3, "type": "mcq",
        "stem": "To gain scalability, a team redesigns a monolith into microservices using managed and "
                "serverless AWS services rather than moving it unchanged. Which migration strategy is this?",
        "options": [
            {"id": "A", "text": "Refactor / re-architect"},
            {"id": "B", "text": "Rehost"},
            {"id": "C", "text": "Replatform"},
            {"id": "D", "text": "Retire"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Refactoring (re-architecting) reimagines how the application is built - often "
                       "cloud-native microservices or serverless - to gain scalability and agility, "
                       "and is the most involved strategy.",
            "distractors": {
                "B": "Rehosting moves the app as-is; it does not redesign the architecture.",
                "C": "Replatforming makes only minor optimizations, not a full redesign into "
                     "microservices.",
                "D": "Retiring decommissions an application; here the team is rebuilding it, not "
                     "removing it.",
            },
            "exam_pattern": "Redesign to cloud-native (microservices/serverless) for scalability = "
                            "refactor / re-architect (most effort).",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-023", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 1, "type": "mcq",
        "stem": "During migration planning, a company finds several applications that are no longer "
                "used and decides to decommission them. Which of the 6 R's is this?",
        "options": [
            {"id": "A", "text": "Retire"},
            {"id": "B", "text": "Retain"},
            {"id": "C", "text": "Rehost"},
            {"id": "D", "text": "Repurchase"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Retiring means decommissioning applications that are no longer needed, which "
                       "reduces cost and attack surface during a migration.",
            "distractors": {
                "B": "Retain means keeping an application as-is (often on-premises) for now, not "
                     "decommissioning it.",
                "C": "Rehosting moves an application to the cloud; retiring removes it instead.",
                "D": "Repurchasing swaps to a different product; retiring eliminates the application "
                     "entirely.",
            },
            "exam_pattern": "Turn off / decommission unused apps = retire; keep-for-now = retain.",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-024", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "A legacy application cannot move yet due to a vendor dependency, so the company leaves "
                "it on-premises and plans to revisit it later. Which migration strategy is this?",
        "options": [
            {"id": "A", "text": "Retain (\"revisit later\")"},
            {"id": "B", "text": "Retire"},
            {"id": "C", "text": "Rehost"},
            {"id": "D", "text": "Refactor / re-architect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Retaining means keeping an application in its current environment for now - "
                       "for example due to a dependency or timing - and revisiting the decision later.",
            "distractors": {
                "B": "Retiring decommissions an app that is no longer needed; here the app is still "
                     "used and kept.",
                "C": "Rehosting moves the app to the cloud now; retaining deliberately does not move "
                     "it yet.",
                "D": "Refactoring re-architects the app in the cloud; retaining leaves it untouched "
                     "on-premises.",
            },
            "exam_pattern": "Keep as-is for now / not ready to move = retain; remove entirely = retire.",
        },
        "references": ["AWS - Migration strategies (the 6 R's)"],
    },
    {
        "id": "clf-cc-025", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "A company must move a large dataset to AWS from a site with slow, unreliable internet, "
                "where uploading over the network would take months. Which approach fits best?",
        "options": [
            {"id": "A", "text": "Use an AWS Snow Family device to transfer the data physically"},
            {"id": "B", "text": "Enable Amazon S3 Transfer Acceleration over the existing link"},
            {"id": "C", "text": "Email the dataset to AWS Support"},
            {"id": "D", "text": "Create a VPC peering connection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Snow Family provides physical devices to transfer large datasets "
                       "offline when network bandwidth is limited or an online transfer would take "
                       "too long; you load the device and ship it to AWS.",
            "distractors": {
                "B": "S3 Transfer Acceleration still relies on the internet link, which is too slow "
                     "and unreliable in this scenario.",
                "C": "Emailing a large dataset is not a real transfer mechanism and is infeasible.",
                "D": "VPC peering connects two VPCs' networks; it does not move an on-premises dataset "
                     "into AWS.",
            },
            "exam_pattern": "Large dataset + limited bandwidth + offline/physical shipping = AWS Snow "
                            "Family.",
        },
        "references": ["AWS Snow Family"],
    },
    {
        "id": "clf-cc-026", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 1, "type": "mcq",
        "stem": "An organization wants a structured way to plan its cloud journey across business and "
                "technical areas, organized into six perspectives. Which AWS framework provides this?",
        "options": [
            {"id": "A", "text": "AWS Cloud Adoption Framework (AWS CAF)"},
            {"id": "B", "text": "AWS Well-Architected Framework"},
            {"id": "C", "text": "AWS Service Catalog"},
            {"id": "D", "text": "AWS Config"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Cloud Adoption Framework (CAF) offers guidance to plan and accelerate "
                       "cloud adoption, organizing capabilities into six perspectives: Business, "
                       "People, Governance, Platform, Security, and Operations.",
            "distractors": {
                "B": "The Well-Architected Framework guides workload and architecture design across "
                     "six pillars, not organizational adoption perspectives.",
                "C": "AWS Service Catalog manages catalogs of approved IT products; it is not an "
                     "adoption framework.",
                "D": "AWS Config records and evaluates resource configurations; it is not an "
                     "adoption-planning framework.",
            },
            "exam_pattern": "Six perspectives + plan organizational cloud adoption = CAF (six pillars "
                            "+ architecture = Well-Architected).",
        },
        "references": ["AWS Cloud Adoption Framework (AWS CAF)"],
    },
    {
        "id": "clf-cc-027", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "migration_caf", "difficulty": 2, "type": "mcq",
        "stem": "A CAF assessment flags gaps in staff skills, roles, and change management for cloud "
                "adoption. Which AWS CAF perspective most directly addresses these concerns?",
        "options": [
            {"id": "A", "text": "People"},
            {"id": "B", "text": "Platform"},
            {"id": "C", "text": "Operations"},
            {"id": "D", "text": "Business"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The People perspective focuses on culture, organizational structure, roles, "
                       "and skills - bridging technology and business during cloud adoption.",
            "distractors": {
                "B": "The Platform perspective addresses building and modernizing a scalable cloud "
                     "platform and its workloads, not staff skills.",
                "C": "The Operations perspective ensures cloud services are run and managed to meet "
                     "business needs, not workforce development.",
                "D": "The Business perspective ensures cloud investments align with and accelerate "
                     "business outcomes, not specifically skills and roles.",
            },
            "exam_pattern": "Skills, roles, culture, change management = People perspective of the CAF.",
        },
        "references": ["AWS Cloud Adoption Framework (AWS CAF) - perspectives"],
    },

    # ===== cloud_economics ==================================================
    {
        "id": "clf-cc-028", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 1, "type": "mcq",
        "stem": "Moving to AWS lets a company stop making large up-front hardware purchases and instead "
                "pay an ongoing variable bill for what it uses. Which shift does this represent?",
        "options": [
            {"id": "A", "text": "Capital expenditure (CapEx) to operational expenditure (OpEx)"},
            {"id": "B", "text": "Operational expenditure to capital expenditure"},
            {"id": "C", "text": "Fixed pricing to reserved pricing"},
            {"id": "D", "text": "Variable expense to sunk cost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The cloud converts large up-front capital expenditure on hardware into "
                       "ongoing, variable operational expenditure that scales with usage - a shift "
                       "from CapEx to OpEx.",
            "distractors": {
                "B": "This reverses the actual shift; the cloud moves spending away from CapEx, not "
                     "toward it.",
                "C": "Reserved pricing is a commitment-based discount model, not the CapEx-to-OpEx "
                     "concept described.",
                "D": "A sunk cost is money already spent and unrecoverable; pay-as-you-go is the "
                     "opposite of locking in sunk costs.",
            },
            "exam_pattern": "Up-front hardware purchase (CapEx) becomes a pay-as-you-go variable bill "
                            "(OpEx).",
        },
        "references": ["AWS - Cloud economics (CapEx vs OpEx)"],
    },
    {
        "id": "clf-cc-029", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 1, "type": "mcq",
        "stem": "An analytics team runs large jobs only a few hours each week and pays solely for the "
                "compute time those jobs consume. Which pricing principle is this?",
        "options": [
            {"id": "A", "text": "Pay-as-you-go (consumption-based pricing)"},
            {"id": "B", "text": "Flat annual licensing"},
            {"id": "C", "text": "Up-front capital purchase"},
            {"id": "D", "text": "Economies of scale"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Pay-as-you-go means paying only for the resources you consume, for as long as "
                       "you use them, with no large up-front commitment - ideal for intermittent "
                       "workloads.",
            "distractors": {
                "B": "Flat annual licensing charges a fixed fee regardless of usage, unlike "
                     "consumption-based pricing.",
                "C": "An up-front capital purchase pays for capacity in advance, the opposite of "
                     "paying only for what you use.",
                "D": "Economies of scale is about lower unit prices from aggregated demand, not the "
                     "pay-only-for-use model.",
            },
            "exam_pattern": "Pay only for what you use, when you use it = pay-as-you-go / consumption "
                            "pricing.",
        },
        "references": ["AWS - Cloud economics (pay-as-you-go pricing)"],
    },
    {
        "id": "clf-cc-030", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "A review finds many EC2 instances running at under ten percent utilization, so a team "
                "switches them to smaller instance types to cut cost. Which cost practice is this?",
        "options": [
            {"id": "A", "text": "Right-sizing"},
            {"id": "B", "text": "Over-provisioning"},
            {"id": "C", "text": "Vertical sharding"},
            {"id": "D", "text": "Lift and shift"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Right-sizing matches instance types and sizes to actual workload "
                       "requirements, so you pay for the capacity you need rather than for idle, "
                       "oversized resources.",
            "distractors": {
                "B": "Over-provisioning is allocating more capacity than needed - the problem being "
                     "fixed here, not the fix.",
                "C": "Vertical sharding is a data-partitioning technique, unrelated to matching "
                     "instance size to load.",
                "D": "Lift and shift (rehost) is a migration strategy, not a cost-optimization "
                     "resizing practice.",
            },
            "exam_pattern": "Match resource size to actual usage to cut waste = right-sizing.",
        },
        "references": ["AWS Well-Architected Framework - Cost Optimization (right-sizing)"],
    },
    {
        "id": "clf-cc-031", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "Before migrating, a company wants to estimate what a workload will cost to run on AWS "
                "so it can compare against its own data center. Which AWS tool helps model this?",
        "options": [
            {"id": "A", "text": "AWS Pricing Calculator"},
            {"id": "B", "text": "Amazon CloudWatch"},
            {"id": "C", "text": "AWS Cost Explorer"},
            {"id": "D", "text": "AWS Budgets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Pricing Calculator lets you estimate the cost of AWS services up "
                       "front, producing the AWS-side figure you use in a total-cost-of-ownership "
                       "comparison before you migrate.",
            "distractors": {
                "B": "Amazon CloudWatch monitors operational metrics and logs; it does not estimate "
                     "pre-migration costs.",
                "C": "AWS Cost Explorer analyzes your past and current AWS spend, not the cost of a "
                     "workload you have not yet deployed.",
                "D": "AWS Budgets alerts you when actual or forecast spend crosses a threshold; it "
                     "does not model costs before migration.",
            },
            "exam_pattern": "Estimate future AWS cost before deploying = AWS Pricing Calculator; "
                            "analyze existing spend = Cost Explorer.",
        },
        "references": ["AWS Pricing Calculator"],
    },
    {
        "id": "clf-cc-032", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "A finance lead notes that AWS's per-unit prices tend to fall as AWS serves more "
                "customers and gains greater purchasing power. Which economic concept explains this?",
        "options": [
            {"id": "A", "text": "Economies of scale"},
            {"id": "B", "text": "Total cost of ownership"},
            {"id": "C", "text": "Capital expenditure"},
            {"id": "D", "text": "Right-sizing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Economies of scale means higher aggregate usage lets AWS buy and operate at "
                       "lower unit cost and pass the savings on as lower pay-as-you-go prices.",
            "distractors": {
                "B": "Total cost of ownership is the full cost of owning and operating a solution, "
                     "not why unit prices fall with scale.",
                "C": "Capital expenditure is up-front spending on assets, unrelated to volume-driven "
                     "price reductions.",
                "D": "Right-sizing matches resources to workload needs; it does not explain "
                     "provider-wide price drops.",
            },
            "exam_pattern": "Lower unit prices because the provider operates at massive scale = "
                            "economies of scale.",
        },
        "references": ["AWS - Six Advantages of Cloud Computing (economies of scale)"],
    },
    {
        "id": "clf-cc-033", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 3, "type": "mcq",
        "stem": "When comparing on-premises and cloud, a CFO wants a cost figure that includes "
                "hardware, power, cooling, space, and staff. Which measure captures all of these?",
        "options": [
            {"id": "A", "text": "Total cost of ownership (TCO)"},
            {"id": "B", "text": "List price"},
            {"id": "C", "text": "Capital expense only"},
            {"id": "D", "text": "Marginal utility"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Total cost of ownership captures the complete cost of a solution - hardware, "
                       "facilities, power, cooling, and labor - enabling a fair on-premises-versus-"
                       "cloud comparison.",
            "distractors": {
                "B": "List price is only the headline price of a product, excluding operating and "
                     "facility costs.",
                "C": "Capital expense alone omits ongoing operational costs such as power, cooling, "
                     "and staff.",
                "D": "Marginal utility is an economics concept about added satisfaction per unit, "
                     "unrelated to cost comparison.",
            },
            "exam_pattern": "All-in cost (hardware + facilities + power + staff) for comparison = "
                            "total cost of ownership.",
        },
        "references": ["AWS - Cloud economics (Total Cost of Ownership)"],
    },
    {
        "id": "clf-cc-034", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 2, "type": "mcq",
        "stem": "By using AWS managed services, a team spends less staff time on patching, backups, and "
                "hardware upkeep and more on product features. Which cost benefit is this?",
        "options": [
            {"id": "A", "text": "Reducing undifferentiated heavy lifting"},
            {"id": "B", "text": "Increasing capital expenditure"},
            {"id": "C", "text": "Eliminating all operational cost"},
            {"id": "D", "text": "Avoiding economies of scale"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Offloading routine infrastructure tasks - patching, backups, hardware upkeep "
                       "- to AWS managed services removes 'undifferentiated heavy lifting', freeing "
                       "staff to focus on work that differentiates the business.",
            "distractors": {
                "B": "Managed services reduce, not increase, capital expenditure.",
                "C": "Operational cost is reduced and shifted, not entirely eliminated - you still "
                     "pay for the managed services you consume.",
                "D": "This benefit works alongside economies of scale; it does not avoid them.",
            },
            "exam_pattern": "Let AWS handle routine infrastructure chores so staff focus on the "
                            "business = removing undifferentiated heavy lifting.",
        },
        "references": ["AWS - Cloud economics (operational efficiency / managed services)"],
    },
    {
        "id": "clf-cc-035", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 1, "type": "mcq",
        "stem": "A company stops paying for servers that sit idle overnight because it can shut the "
                "resources down and is no longer billed while they are off. Which cost advantage is this?",
        "options": [
            {"id": "A", "text": "Paying only for resources you consume (variable cost)"},
            {"id": "B", "text": "Fixed cost regardless of usage"},
            {"id": "C", "text": "A mandatory multi-year commitment"},
            {"id": "D", "text": "Economies of scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With the cloud's consumption model you can turn resources off when idle and "
                       "stop paying for them, converting the fixed cost of idle capacity into a "
                       "variable cost tied to actual use.",
            "distractors": {
                "B": "Fixed cost regardless of usage describes owned on-premises hardware, not the "
                     "cloud's variable model.",
                "C": "Pay-as-you-go requires no mandatory multi-year commitment to benefit from "
                     "stopping idle resources.",
                "D": "Economies of scope refers to savings from producing varied goods together; it "
                     "is not this pay-for-use advantage.",
            },
            "exam_pattern": "Turn it off and stop paying = variable / consumption cost (versus the "
                            "fixed cost of owned hardware).",
        },
        "references": ["AWS - Cloud economics (variable versus fixed cost)"],
    },
    {
        "id": "clf-cc-036", "exam": "clf", "domain": "cloud_concepts",
        "subtopic": "cloud_economics", "difficulty": 1, "type": "mcq",
        "stem": "A manager is sorting IT spending into categories. Which of the following is an example "
                "of operational expenditure (OpEx) rather than capital expenditure (CapEx)?",
        "options": [
            {"id": "A", "text": "A monthly, usage-based bill for the AWS compute consumed"},
            {"id": "B", "text": "Purchasing physical servers for a new data center"},
            {"id": "C", "text": "Buying networking hardware up front"},
            {"id": "D", "text": "Constructing an on-premises data-center building"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OpEx is ongoing operating spend; a monthly, usage-based AWS bill is OpEx. The "
                       "other choices are one-time up-front asset purchases or builds, which are CapEx.",
            "distractors": {
                "B": "Buying physical servers is an up-front asset purchase - capital expenditure.",
                "C": "Purchasing networking hardware up front is a capital expenditure.",
                "D": "Constructing a data-center building is a large capital expenditure.",
            },
            "exam_pattern": "Recurring usage-based spend = OpEx; one-time asset purchase or build = "
                            "CapEx.",
        },
        "references": ["AWS - Cloud economics (CapEx vs OpEx)"],
    },
]
