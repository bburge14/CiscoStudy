"""AWS Certified Cloud Practitioner (CLF-C02) EXPANSION pool — Domain 4:
Billing, Pricing, and Support.

Original, objective-aligned practice items covering all four Domain 4 subtopics:
pricing_models, billing_cost_management, support_plans, and technical_resources.
Never real or memorized exam items.

Cloud-Practitioner depth only: items describe relative/conceptual relationships
(e.g. "Spot offers the deepest discount but can be interrupted") and avoid exact
prices, percentages, and SLA minute-counts that drift over time. Every item names
a relevant AWS doc/service in `references`.

Authoring rules match the other pools: build_content.py shuffles option order
(seeded by id), so the answer key here is not positionally biased, and every
wrong option carries a distractor note.
"""

QUESTIONS = [
    # ===== pricing_models ===================================================
    {
        "id": "clf-bill-001", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 1, "type": "mcq",
        "stem": "A startup runs a short-lived EC2 workload with spiky, unpredictable traffic and "
                "wants no commitment or upfront cost. Which purchase option fits best?",
        "options": [
            {"id": "A", "text": "On-Demand Instances"},
            {"id": "B", "text": "Standard Reserved Instances (3-year)"},
            {"id": "C", "text": "Dedicated Hosts"},
            {"id": "D", "text": "Compute Savings Plan (1-year)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On-Demand charges per second/hour with no commitment or upfront payment, "
                       "which suits short-lived, spiky, or unpredictable workloads.",
            "distractors": {
                "B": "Reserved Instances require a 1- or 3-year commitment — the opposite of 'no "
                     "commitment' — and suit steady, predictable usage.",
                "C": "Dedicated Hosts are the most expensive option and target per-socket/core "
                     "licensing and compliance, not short, flexible workloads.",
                "D": "A Savings Plan commits you to a steady hourly spend for 1 or 3 years, which "
                     "a startup with unpredictable traffic does not want.",
            },
            "exam_pattern": "'No commitment / unpredictable / short-term' almost always points to "
                            "On-Demand.",
        },
        "references": ["AWS EC2 Instance Purchasing Options"],
    },
    {
        "id": "clf-bill-002", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "A data team runs fault-tolerant batch jobs that can tolerate interruptions and "
                "wants the deepest possible EC2 discount. Which purchase option fits?",
        "options": [
            {"id": "A", "text": "Spot Instances"},
            {"id": "B", "text": "On-Demand Instances"},
            {"id": "C", "text": "Reserved Instances"},
            {"id": "D", "text": "Dedicated Hosts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spot Instances use spare AWS capacity at the deepest discount off On-Demand, "
                       "but AWS can reclaim them on short notice — ideal for interruption-tolerant, "
                       "flexible work like batch jobs.",
            "distractors": {
                "B": "On-Demand carries no discount, so it is the wrong choice when the goal is the "
                     "deepest savings.",
                "C": "Reserved Instances discount steady, always-on usage via a 1- or 3-year "
                     "commitment; they are not the deepest discount and waste commitment on "
                     "interruptible batch work.",
                "D": "Dedicated Hosts are the most expensive option, aimed at licensing and "
                     "compliance, not savings.",
            },
            "exam_pattern": "'Fault-tolerant / interruptible + biggest discount' = Spot.",
        },
        "references": ["AWS EC2 Instance Purchasing Options"],
    },
    {
        "id": "clf-bill-003", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "A company runs an always-on production database on EC2 for three years and wants "
                "the lowest steady-state cost through commitment. Which option?",
        "options": [
            {"id": "A", "text": "Reserved Instances"},
            {"id": "B", "text": "Spot Instances"},
            {"id": "C", "text": "On-Demand Instances"},
            {"id": "D", "text": "AWS Free Tier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reserved Instances give a significant discount in exchange for a 1- or 3-year "
                       "commitment, which fits predictable, always-on usage like a production "
                       "database.",
            "distractors": {
                "B": "Spot Instances can be interrupted at any time, which is unacceptable for an "
                     "always-on production database.",
                "C": "On-Demand carries no commitment discount, so it costs more for steady, "
                     "long-running workloads.",
                "D": "The Free Tier offers limited introductory usage for learning, not production "
                     "capacity for a three-year database.",
            },
            "exam_pattern": "'Steady / always-on / predictable + willing to commit' = Reserved "
                            "Instances (or a Savings Plan).",
        },
        "references": ["AWS EC2 Instance Purchasing Options"],
    },
    {
        "id": "clf-bill-004", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a discount spanning EC2, Fargate, and Lambda by committing "
                "to a steady hourly spend for one year. Which option?",
        "options": [
            {"id": "A", "text": "Compute Savings Plan"},
            {"id": "B", "text": "Standard Reserved Instances"},
            {"id": "C", "text": "Spot Instances"},
            {"id": "D", "text": "Dedicated Hosts"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Compute Savings Plan commits to a consistent hourly spend and applies the "
                       "discount flexibly across EC2, AWS Fargate, and AWS Lambda, regardless of "
                       "region or instance family.",
            "distractors": {
                "B": "Standard Reserved Instances apply to EC2 only and are tied to specific "
                     "instance attributes — they do not cover Fargate or Lambda.",
                "C": "Spot gives a deep discount but no steady commitment-based savings and can be "
                     "interrupted; it is not a spend commitment.",
                "D": "Dedicated Hosts are a physical-server tenancy model for licensing, not a "
                     "flexible compute discount.",
            },
            "exam_pattern": "'Flexible discount across EC2 + Fargate + Lambda for an hourly $ "
                            "commitment' = Compute Savings Plan.",
        },
        "references": ["AWS Savings Plans"],
    },
    {
        "id": "clf-bill-005", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 1, "type": "mcq",
        "stem": "A learner wants AWS services that stay free beyond the first twelve months, within "
                "monthly limits, to keep practicing. Which AWS Free Tier category?",
        "options": [
            {"id": "A", "text": "Always Free"},
            {"id": "B", "text": "12-Months Free"},
            {"id": "C", "text": "Free Trials"},
            {"id": "D", "text": "Reserved capacity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Always Free category of the AWS Free Tier offers usage that never expires, "
                       "up to defined monthly limits, for as long as you have an account.",
            "distractors": {
                "B": "12-Months Free offers expire 12 months after account sign-up, so they do not "
                     "'stay free beyond twelve months.'",
                "C": "Free Trials are short-term and end after a set period once activated.",
                "D": "'Reserved capacity' is a pricing-commitment idea, not a Free Tier category.",
            },
            "exam_pattern": "Free Tier has three buckets: Always Free (never expires), 12-Months "
                            "Free (from sign-up), and short Free Trials.",
        },
        "references": ["AWS Free Tier"],
    },
    {
        "id": "clf-bill-006", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "A company must honor software licenses tied to physical cores and needs visibility "
                "into the underlying host for compliance. Which EC2 option?",
        "options": [
            {"id": "A", "text": "Dedicated Hosts"},
            {"id": "B", "text": "Spot Instances"},
            {"id": "C", "text": "On-Demand Instances with default (shared) tenancy"},
            {"id": "D", "text": "Reserved Instances"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dedicated Hosts give you a physical server dedicated to your account with "
                       "visibility into sockets and cores, supporting bring-your-own-license (BYOL) "
                       "models and compliance requirements.",
            "distractors": {
                "B": "Spot Instances run on shared spare capacity and give no dedicated-hardware "
                     "visibility or per-core licensing control.",
                "C": "Default shared tenancy places you on multi-tenant hardware with no visibility "
                     "into the physical host.",
                "D": "Reserved Instances are a billing discount, not a tenancy or hardware-visibility "
                     "model.",
            },
            "exam_pattern": "'Per-socket/core licensing (BYOL) or hardware visibility for compliance' "
                            "= Dedicated Hosts.",
        },
        "references": ["AWS EC2 Dedicated Hosts"],
    },
    {
        "id": "clf-bill-007", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 1, "type": "mcq",
        "stem": "A finance lead notices that committing to one- or three-year usage lowers the unit "
                "price versus hourly rates. Which AWS pricing principle is this?",
        "options": [
            {"id": "A", "text": "Pay less when you reserve"},
            {"id": "B", "text": "Pay-as-you-go"},
            {"id": "C", "text": "Pay less by using more"},
            {"id": "D", "text": "You never pay anything upfront"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Pay less when you reserve' means committing to usage (Reserved Instances or "
                       "Savings Plans) lowers the per-unit price compared with On-Demand rates.",
            "distractors": {
                "B": "Pay-as-you-go describes paying only for what you use with no commitment — it "
                     "does not explain the commitment discount.",
                "C": "'Pay less by using more' refers to volume/tiered discounts as usage grows, a "
                     "different mechanism than reserving.",
                "D": "AWS does not promise zero upfront payment; some reservations even offer an "
                     "all-upfront option for a larger discount.",
            },
            "exam_pattern": "Commitment (1/3-year) lowering the rate = 'pay less when you reserve.'",
        },
        "references": ["AWS Cloud Value / How AWS Pricing Works"],
    },
    {
        "id": "clf-bill-008", "exam": "clf", "domain": "billing_support",
        "subtopic": "pricing_models", "difficulty": 2, "type": "mcq",
        "stem": "As a company stores progressively more data in Amazon S3, its per-GB rate drops at "
                "higher usage tiers. Which AWS pricing principle is this?",
        "options": [
            {"id": "A", "text": "Pay less by using more (volume-based discounts)"},
            {"id": "B", "text": "Pay less when you reserve"},
            {"id": "C", "text": "Pay-as-you-go"},
            {"id": "D", "text": "Spot pricing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Pay less by using more' means higher aggregate usage reaches lower-priced "
                       "tiers, as with Amazon S3's tiered per-GB storage pricing.",
            "distractors": {
                "B": "Reserving lowers price through a time commitment, not through greater volume.",
                "C": "Pay-as-you-go describes paying for consumption; it does not by itself drop the "
                     "unit rate as volume grows.",
                "D": "Spot pricing is an EC2 spare-capacity model, unrelated to S3 tiered storage "
                     "rates.",
            },
            "exam_pattern": "'Rate falls as volume/usage rises' = 'pay less by using more.'",
        },
        "references": ["AWS Cloud Value / How AWS Pricing Works"],
    },

    # ===== billing_cost_management ==========================================
    {
        "id": "clf-bill-009", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 1, "type": "mcq",
        "stem": "A manager wants to visualize the last several months of AWS spend by service and "
                "forecast upcoming costs. Which tool fits?",
        "options": [
            {"id": "A", "text": "AWS Cost Explorer"},
            {"id": "B", "text": "AWS Budgets"},
            {"id": "C", "text": "AWS Pricing Calculator"},
            {"id": "D", "text": "AWS Cost and Usage Report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Cost Explorer provides interactive graphs to analyze and visualize past "
                       "spend and usage by dimensions like service, plus built-in forecasting of "
                       "future costs.",
            "distractors": {
                "B": "AWS Budgets is for setting thresholds and sending alerts, not for exploring "
                     "and visualizing historical spend by service.",
                "C": "AWS Pricing Calculator estimates costs before deployment; it does not analyze "
                     "incurred spend.",
                "D": "The Cost and Usage Report delivers raw granular line items to S3; it is not an "
                     "interactive visualization/forecast dashboard.",
            },
            "exam_pattern": "'Visualize/analyze/forecast existing spend' = Cost Explorer.",
        },
        "references": ["AWS Cost Explorer"],
    },
    {
        "id": "clf-bill-010", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A team wants an automatic email alert when monthly AWS spend is forecast to exceed "
                "a set dollar threshold. Which service?",
        "options": [
            {"id": "A", "text": "AWS Budgets"},
            {"id": "B", "text": "AWS Cost Explorer"},
            {"id": "C", "text": "AWS Pricing Calculator"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Budgets lets you set custom cost or usage thresholds and triggers alerts "
                       "when actual or forecasted spend crosses them.",
            "distractors": {
                "B": "Cost Explorer analyzes and forecasts spend for review but does not send "
                     "threshold-based alerts.",
                "C": "Pricing Calculator estimates costs before you deploy; it does not monitor "
                     "actual spend.",
                "D": "Trusted Advisor gives best-practice checks (including cost optimization), not "
                     "custom spend-threshold alerts.",
            },
            "exam_pattern": "'Alert me when spend crosses $X' = AWS Budgets.",
        },
        "references": ["AWS Budgets"],
    },
    {
        "id": "clf-bill-011", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "Before launching a new architecture, an architect wants to estimate the monthly "
                "cost of planned EC2 and S3 usage. Which tool?",
        "options": [
            {"id": "A", "text": "AWS Pricing Calculator"},
            {"id": "B", "text": "AWS Cost Explorer"},
            {"id": "C", "text": "AWS Cost and Usage Report"},
            {"id": "D", "text": "AWS Budgets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Pricing Calculator models and estimates costs for planned workloads "
                       "before anything is deployed, so you can compare configurations up front.",
            "distractors": {
                "B": "Cost Explorer analyzes spend that has already been incurred; it needs existing "
                     "usage to report on.",
                "C": "The Cost and Usage Report details actual past usage, not pre-deployment "
                     "estimates.",
                "D": "Budgets tracks and alerts on actual or forecasted spend of running resources, "
                     "not hypothetical designs.",
            },
            "exam_pattern": "'Estimate before deploying / what-if cost' = Pricing Calculator.",
        },
        "references": ["AWS Pricing Calculator"],
    },
    {
        "id": "clf-bill-012", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise with many AWS accounts wants one monthly bill and combined usage to "
                "reach volume pricing tiers. Which capability?",
        "options": [
            {"id": "A", "text": "Consolidated billing in AWS Organizations"},
            {"id": "B", "text": "AWS Pricing Calculator"},
            {"id": "C", "text": "Cost allocation tags"},
            {"id": "D", "text": "AWS Budgets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Consolidated billing in AWS Organizations combines member accounts under one "
                       "payer with a single bill and aggregates usage so the group can reach volume "
                       "pricing tiers — at no additional charge.",
            "distractors": {
                "B": "Pricing Calculator estimates costs; it does not combine account billing.",
                "C": "Cost allocation tags categorize and break down costs; they do not merge "
                     "accounts onto one bill.",
                "D": "Budgets alerts on thresholds; it does not consolidate billing across accounts.",
            },
            "exam_pattern": "'Many accounts → one bill + aggregated volume discounts' = consolidated "
                            "billing via AWS Organizations.",
        },
        "references": ["AWS Organizations - Consolidated Billing"],
    },
    {
        "id": "clf-bill-013", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "A company must break its AWS bill down by department and project to charge costs "
                "back internally. Which feature enables this?",
        "options": [
            {"id": "A", "text": "Cost allocation tags"},
            {"id": "B", "text": "Consolidated billing"},
            {"id": "C", "text": "AWS Pricing Calculator"},
            {"id": "D", "text": "Savings Plans"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cost allocation tags (key/value labels on resources, activated in the Billing "
                       "console) let you group and report costs by dimensions such as department or "
                       "project for chargeback.",
            "distractors": {
                "B": "Consolidated billing combines accounts into one bill but does not itself split "
                     "spend by department or project.",
                "C": "Pricing Calculator produces pre-deployment estimates, not categorized bill "
                     "breakdowns.",
                "D": "Savings Plans are a discount commitment, unrelated to categorizing costs.",
            },
            "exam_pattern": "'Break down / categorize the bill by team, project, environment' = cost "
                            "allocation tags.",
        },
        "references": ["AWS Cost Allocation Tags"],
    },
    {
        "id": "clf-bill-014", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 3, "type": "mcq",
        "stem": "A FinOps analyst needs the most granular line-item billing data delivered to Amazon "
                "S3 for querying with Amazon Athena. Which resource?",
        "options": [
            {"id": "A", "text": "AWS Cost and Usage Report (CUR)"},
            {"id": "B", "text": "AWS Cost Explorer"},
            {"id": "C", "text": "AWS Budgets"},
            {"id": "D", "text": "AWS Pricing Calculator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Cost and Usage Report is the most comprehensive, granular billing "
                       "dataset; it drops detailed line items into S3 where tools like Athena, "
                       "Redshift, or QuickSight can query them.",
            "distractors": {
                "B": "Cost Explorer offers interactive summaries, not the most granular line-item "
                     "export for external querying.",
                "C": "Budgets focuses on threshold alerts, not detailed data delivery to S3.",
                "D": "Pricing Calculator estimates future costs; it produces no billing data about "
                     "actual usage.",
            },
            "exam_pattern": "'Most granular / line-item data to S3 for Athena' = Cost and Usage "
                            "Report.",
        },
        "references": ["AWS Cost and Usage Report"],
    },
    {
        "id": "clf-bill-015", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants machine-learning-based detection of unusual spending spikes, with "
                "alerts when costs deviate from normal patterns. Which capability fits best?",
        "options": [
            {"id": "A", "text": "AWS Cost Anomaly Detection"},
            {"id": "B", "text": "AWS Pricing Calculator"},
            {"id": "C", "text": "Cost allocation tags"},
            {"id": "D", "text": "AWS Compute Optimizer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Cost Anomaly Detection uses machine learning to learn normal spend "
                       "patterns and alert you when usage or cost deviates unexpectedly.",
            "distractors": {
                "B": "Pricing Calculator estimates costs before deployment; it does not watch live "
                     "spend for anomalies.",
                "C": "Cost allocation tags categorize spend; they do not detect anomalies.",
                "D": "Compute Optimizer recommends right-sizing of resources for efficiency, not "
                     "spend-anomaly alerting.",
            },
            "exam_pattern": "'ML detects unusual/unexpected spend' = Cost Anomaly Detection.",
        },
        "references": ["AWS Cost Anomaly Detection"],
    },
    {
        "id": "clf-bill-016", "exam": "clf", "domain": "billing_support",
        "subtopic": "billing_cost_management", "difficulty": 3, "type": "multi",
        "stem": "A company wants to estimate costs before deploying and be alerted when actual "
                "monthly spend exceeds a threshold. Which two services? (Choose two.)",
        "options": [
            {"id": "A", "text": "AWS Pricing Calculator"},
            {"id": "B", "text": "AWS Budgets"},
            {"id": "C", "text": "AWS Cost and Usage Report"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "AWS Pricing Calculator covers the pre-deployment estimate, and AWS Budgets "
                       "covers the alert when actual spend crosses the chosen threshold — together "
                       "they meet both needs.",
            "distractors": {
                "C": "The Cost and Usage Report delivers granular historical billing data; it "
                     "neither estimates future costs nor sends threshold alerts.",
                "D": "Trusted Advisor runs best-practice checks (including cost optimization) but "
                     "does not estimate pre-deployment costs or send custom spend-threshold alerts.",
            },
            "exam_pattern": "Split the ask: 'estimate first' = Pricing Calculator; 'alert on overspend' "
                            "= Budgets.",
        },
        "references": ["AWS Pricing Calculator", "AWS Budgets"],
    },

    # ===== support_plans ====================================================
    {
        "id": "clf-bill-017", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 1, "type": "mcq",
        "stem": "A new account owner asks which AWS Support plan is included with every account at "
                "no additional cost. Which plan?",
        "options": [
            {"id": "A", "text": "Basic Support"},
            {"id": "B", "text": "Developer Support"},
            {"id": "C", "text": "Business Support"},
            {"id": "D", "text": "Enterprise Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Basic Support is free for all accounts and includes documentation, "
                       "whitepapers, AWS re:Post, 24/7 account and billing customer service, and a "
                       "limited set of Trusted Advisor checks.",
            "distractors": {
                "B": "Developer Support is a paid tier.",
                "C": "Business Support is a paid tier.",
                "D": "Enterprise Support is the highest-cost paid tier.",
            },
            "exam_pattern": "'Included free with every account' = Basic Support.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-018", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A company needs 24/7 phone, chat, and email access to Cloud Support Engineers at "
                "the lowest-cost plan that offers it. Which plan?",
        "options": [
            {"id": "A", "text": "Business Support"},
            {"id": "B", "text": "Developer Support"},
            {"id": "C", "text": "Basic Support"},
            {"id": "D", "text": "Enterprise Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Business Support is the lowest tier that adds 24/7 access to Cloud Support "
                       "Engineers by phone, chat, and email for production issues.",
            "distractors": {
                "B": "Developer Support offers business-hours email access to Cloud Support "
                     "Associates only — not 24/7, and not phone/chat engineer access.",
                "C": "Basic Support has no technical support; its 24/7 contact is for account and "
                     "billing questions only.",
                "D": "Enterprise Support includes 24/7 support but is higher cost, so it is not the "
                     "lowest-cost plan that offers it.",
            },
            "exam_pattern": "'Lowest plan with 24/7 technical support (phone/chat/email)' = Business.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-019", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A large enterprise wants a designated Technical Account Manager who provides "
                "proactive guidance and well-architected reviews. Which support plan includes this?",
        "options": [
            {"id": "A", "text": "Enterprise Support"},
            {"id": "B", "text": "Business Support"},
            {"id": "C", "text": "Developer Support"},
            {"id": "D", "text": "Basic Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Enterprise Support includes a designated Technical Account Manager (TAM) who "
                       "gives proactive, account-specific guidance such as well-architected reviews "
                       "and optimization help.",
            "distractors": {
                "B": "Business Support provides 24/7 technical support but no designated TAM.",
                "C": "Developer Support is business-hours email support only, with no TAM.",
                "D": "Basic Support offers no technical support and no TAM.",
            },
            "exam_pattern": "'Designated TAM / concierge, proactive guidance' = Enterprise Support.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-020", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A developer testing in a non-production environment wants low-cost technical support "
                "by email during business hours. Which entry-level paid plan?",
        "options": [
            {"id": "A", "text": "Developer Support"},
            {"id": "B", "text": "Business Support"},
            {"id": "C", "text": "Enterprise On-Ramp Support"},
            {"id": "D", "text": "Basic Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Developer Support is the lowest-cost paid plan, offering business-hours email "
                       "access to Cloud Support Associates — a fit for experimentation and "
                       "non-production testing.",
            "distractors": {
                "B": "Business Support adds 24/7 engineer access at a higher cost than this use case "
                     "requires.",
                "C": "Enterprise On-Ramp is a much higher tier that adds TAM access and 24/7 support.",
                "D": "Basic Support is free but provides no technical support at all, so it is not a "
                     "paid plan with email tech support.",
            },
            "exam_pattern": "'Cheapest paid plan, business-hours email, test/non-prod' = Developer "
                            "Support.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-021", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 3, "type": "mcq",
        "stem": "A company wants 24/7 support and access to a pool of Technical Account Managers, "
                "below the cost of full Enterprise Support. Which plan?",
        "options": [
            {"id": "A", "text": "Enterprise On-Ramp Support"},
            {"id": "B", "text": "Business Support"},
            {"id": "C", "text": "Developer Support"},
            {"id": "D", "text": "Basic Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Enterprise On-Ramp sits between Business and Enterprise: it adds 24/7 support "
                       "plus access to a pool of Technical Account Managers, at a lower cost than "
                       "full Enterprise Support.",
            "distractors": {
                "B": "Business Support provides 24/7 support but no Technical Account Manager access.",
                "C": "Developer Support is business-hours email only, with no 24/7 or TAM access.",
                "D": "Basic Support has no technical support and no TAM access.",
            },
            "exam_pattern": "'TAM access (pool) + 24/7, but not full Enterprise' = Enterprise "
                            "On-Ramp.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-022", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A customer opens an AWS Support case and asks what determines how quickly AWS "
                "targets its response. Which factor set applies?",
        "options": [
            {"id": "A", "text": "The case severity combined with the support plan tier"},
            {"id": "B", "text": "The AWS Region the resources run in"},
            {"id": "C", "text": "How old the AWS account is"},
            {"id": "D", "text": "The number of IAM users in the account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Targeted response times depend on the severity of the case and the support "
                       "plan tier — higher tiers and more severe (e.g. business-critical) cases get "
                       "faster response targets.",
            "distractors": {
                "B": "The Region where resources run does not set support response times.",
                "C": "Account age has no bearing on support response targets.",
                "D": "The count of IAM users is unrelated to support response times.",
            },
            "exam_pattern": "Response speed scales with case severity and plan tier — not with "
                            "region, account age, or user count.",
        },
        "references": ["AWS Support Plans"],
    },
    {
        "id": "clf-bill-023", "exam": "clf", "domain": "billing_support",
        "subtopic": "support_plans", "difficulty": 2, "type": "mcq",
        "stem": "A team wants the full set of AWS Trusted Advisor checks across all categories "
                "unlocked through their support plan. Which is the minimum plan required?",
        "options": [
            {"id": "A", "text": "Business Support"},
            {"id": "B", "text": "Developer Support"},
            {"id": "C", "text": "Basic Support"},
            {"id": "D", "text": "Any plan — all checks are always free"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The full set of Trusted Advisor checks is unlocked at Business Support and "
                       "above (including Enterprise On-Ramp and Enterprise).",
            "distractors": {
                "B": "Developer Support still gets only the limited, core check set.",
                "C": "Basic Support gets only a limited set of Trusted Advisor checks.",
                "D": "Only a limited set is free on Basic/Developer; the full set is gated behind "
                     "Business+.",
            },
            "exam_pattern": "'Full Trusted Advisor checks' = Business tier or higher (Basic/Developer "
                            "get a limited subset).",
        },
        "references": ["AWS Support Plans", "AWS Trusted Advisor"],
    },

    # ===== technical_resources ==============================================
    {
        "id": "clf-bill-024", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 1, "type": "mcq",
        "stem": "A company wants automated best-practice recommendations spanning cost, security, "
                "fault tolerance, performance, and service limits. Which AWS tool provides these?",
        "options": [
            {"id": "A", "text": "AWS Trusted Advisor"},
            {"id": "B", "text": "AWS Health Dashboard"},
            {"id": "C", "text": "AWS Pricing Calculator"},
            {"id": "D", "text": "AWS CloudTrail"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Trusted Advisor inspects your environment and recommends improvements "
                       "across categories such as cost optimization, security, fault tolerance, "
                       "performance, and service limits.",
            "distractors": {
                "B": "The AWS Health Dashboard reports the status of AWS service events; it does not "
                     "run best-practice checks on your configuration.",
                "C": "Pricing Calculator estimates costs before deployment; it gives no best-practice "
                     "checks.",
                "D": "CloudTrail records API activity for auditing; it is not a recommendations "
                     "engine.",
            },
            "exam_pattern": "'Checks across cost/security/fault-tolerance/performance/limits' = "
                            "Trusted Advisor.",
        },
        "references": ["AWS Trusted Advisor"],
    },
    {
        "id": "clf-bill-025", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 2, "type": "mcq",
        "stem": "An operations team wants personalized alerts about AWS events that affect its own "
                "account's resources, with remediation guidance. Which tool fits?",
        "options": [
            {"id": "A", "text": "AWS Health Dashboard (your account's health)"},
            {"id": "B", "text": "AWS Trusted Advisor"},
            {"id": "C", "text": "The public AWS service health status page"},
            {"id": "D", "text": "Amazon CloudWatch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The account-specific view of the AWS Health Dashboard (formerly the Personal "
                       "Health Dashboard) gives personalized alerts and remediation guidance for AWS "
                       "events that affect your own resources.",
            "distractors": {
                "B": "Trusted Advisor runs best-practice checks; it is not a notification feed for "
                     "AWS-side events.",
                "C": "The public service health status page shows general, non-personalized service "
                     "status, not events scoped to your resources.",
                "D": "CloudWatch monitors metrics, logs, and alarms you configure on your resources, "
                     "not AWS-side operational events.",
            },
            "exam_pattern": "'Personalized / affecting MY resources' = AWS Health Dashboard (account "
                            "health); public status page = everyone's general status.",
        },
        "references": ["AWS Health Dashboard"],
    },
    {
        "id": "clf-bill-026", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 1, "type": "mcq",
        "stem": "A developer wants a free, community-driven AWS question-and-answer service where "
                "AWS experts and other users respond. Which resource?",
        "options": [
            {"id": "A", "text": "AWS re:Post"},
            {"id": "B", "text": "AWS Marketplace"},
            {"id": "C", "text": "AWS Professional Services"},
            {"id": "D", "text": "Business Support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS re:Post is a free, community-driven question-and-answer service (the "
                       "successor to the AWS forums) where AWS experts and the community answer "
                       "technical questions.",
            "distractors": {
                "B": "AWS Marketplace is a catalog for buying third-party software, not a Q&A "
                     "community.",
                "C": "AWS Professional Services is a paid consulting organization, not a free "
                     "community forum.",
                "D": "Business Support is a paid support plan, not a free community Q&A service.",
            },
            "exam_pattern": "'Free community Q&A' = AWS re:Post.",
        },
        "references": ["AWS re:Post"],
    },
    {
        "id": "clf-bill-027", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to find, buy, and deploy third-party software, billed together with "
                "its AWS charges. Which resource fits?",
        "options": [
            {"id": "A", "text": "AWS Marketplace"},
            {"id": "B", "text": "AWS re:Post"},
            {"id": "C", "text": "AWS Knowledge Center"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Marketplace is a curated digital catalog where customers find, buy, and "
                       "deploy third-party software, with charges appearing on their AWS bill.",
            "distractors": {
                "B": "AWS re:Post is a community Q&A service, not a software marketplace.",
                "C": "AWS Knowledge Center is a library of help articles, not a place to purchase "
                     "software.",
                "D": "Trusted Advisor provides best-practice checks, not software procurement.",
            },
            "exam_pattern": "'Buy/deploy third-party software billed through AWS' = AWS Marketplace.",
        },
        "references": ["AWS Marketplace"],
    },
    {
        "id": "clf-bill-028", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 2, "type": "mcq",
        "stem": "A customer needs a vetted third-party consulting firm to help design and migrate "
                "its AWS workloads. Which program helps locate one?",
        "options": [
            {"id": "A", "text": "AWS Partner Network (APN)"},
            {"id": "B", "text": "AWS re:Post"},
            {"id": "C", "text": "AWS Trusted Advisor"},
            {"id": "D", "text": "AWS Health Dashboard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Partner Network is a global community of consulting and technology "
                       "partners; customers use it to find vetted firms that help design, build, and "
                       "migrate AWS workloads.",
            "distractors": {
                "B": "AWS re:Post is a free community Q&A service, not a directory of consulting "
                     "partners.",
                "C": "Trusted Advisor provides best-practice checks, not partner discovery.",
                "D": "The Health Dashboard reports service/account event status, not partners.",
            },
            "exam_pattern": "'Find a vetted partner / consulting firm' = AWS Partner Network.",
        },
        "references": ["AWS Partner Network"],
    },
    {
        "id": "clf-bill-029", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 1, "type": "mcq",
        "stem": "A new user wants free articles that answer the most common AWS questions, without "
                "opening a support case. Which resource?",
        "options": [
            {"id": "A", "text": "AWS Knowledge Center"},
            {"id": "B", "text": "Business Support"},
            {"id": "C", "text": "AWS Professional Services"},
            {"id": "D", "text": "AWS IQ"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS Knowledge Center is a free library of articles and videos answering "
                       "the most frequently asked AWS questions — no support case required.",
            "distractors": {
                "B": "Business Support is a paid support plan, not a free self-service article "
                     "library.",
                "C": "AWS Professional Services is a paid consulting engagement.",
                "D": "AWS IQ connects you with paid, on-demand third-party experts, not free "
                     "self-service articles.",
            },
            "exam_pattern": "'Free self-service articles for common questions' = AWS Knowledge "
                            "Center.",
        },
        "references": ["AWS Knowledge Center"],
    },
    {
        "id": "clf-bill-030", "exam": "clf", "domain": "billing_support",
        "subtopic": "technical_resources", "difficulty": 3, "type": "mcq",
        "stem": "A team wants free AWS-authored whitepapers and best-practice guidance, such as the "
                "Well-Architected Framework, to inform its design. Which resource?",
        "options": [
            {"id": "A", "text": "AWS Whitepapers and documentation"},
            {"id": "B", "text": "AWS Budgets"},
            {"id": "C", "text": "AWS Cost Explorer"},
            {"id": "D", "text": "AWS Marketplace"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Whitepapers and documentation are free, authoritative technical "
                       "resources — including the AWS Well-Architected Framework — that guide "
                       "architecture and best-practice decisions.",
            "distractors": {
                "B": "AWS Budgets sends spend/usage threshold alerts; it is not guidance "
                     "documentation.",
                "C": "Cost Explorer analyzes and visualizes spend, not architectural best practices.",
                "D": "AWS Marketplace sells third-party software; it is not AWS-authored guidance.",
            },
            "exam_pattern": "'Free AWS-authored best-practice guidance / Well-Architected' = "
                            "whitepapers and documentation.",
        },
        "references": ["AWS Whitepapers & Guides"],
    },
]
