"""CompTIA Cloud+ (CV0-004) pool - Domain 5: DevOps Fundamentals.

Original, objective-aligned practice items for the three DevOps subtopics
tracked in CertLab:
  * cloudp_cicd                 - continuous integration/delivery/deployment,
                                  version control, blue-green and canary releases,
                                  GitOps.
  * cloudp_iac                  - Infrastructure as Code, declarative vs imperative,
                                  idempotency, configuration management, drift.
  * cloudp_automation_scripting - REST APIs, JSON/YAML, event-driven webhooks,
                                  scripting benefits and automation candidates.

Cloud+ is vendor-NEUTRAL: tools (Git, Terraform, Ansible, etc.) are named only as
illustrative examples of a concept, never as the sole key. build_content.py shuffles
option order (seeded by id), so no key is positionally biased; every wrong option
carries a distractor note, and each item cites the public CV0-004 objective domain it
draws on. Original items only, never real exam content.
"""

QUESTIONS = [
    # ===== cloudp_cicd ======================================================
    {
        "id": "cloudplus-dev-001", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 1, "type": "mcq",
        "stem": "Developers merge code to a shared repository several times a day, and each merge automatically "
                "triggers a build and automated test run to catch integration problems early. Which practice is this?",
        "options": [
            {"id": "A", "text": "Continuous integration (CI)"},
            {"id": "B", "text": "Continuous deployment to production"},
            {"id": "C", "text": "Manual quarterly releases"},
            {"id": "D", "text": "Infrastructure as code"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Continuous integration has developers merge frequently, with each change automatically built and "
                       "tested so integration defects are caught quickly.",
            "distractors": {
                "B": "Continuous deployment automatically releases to production; the scenario describes build/test on merge, which is CI.",
                "C": "Quarterly manual releases are the opposite of the frequent, automated integration described.",
                "D": "Infrastructure as code manages infrastructure via definition files; it is not the merge/build/test loop.",
            },
            "exam_pattern": "Frequent merges + automated build/test on each = continuous integration.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (continuous integration)"],
    },
    {
        "id": "cloudplus-dev-002", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "After automated tests pass, a pipeline automatically releases every successful build straight to "
                "production with no human approval step. Which practice is this?",
        "options": [
            {"id": "A", "text": "Continuous integration"},
            {"id": "B", "text": "Continuous delivery"},
            {"id": "C", "text": "Manual change-advisory-board approval"},
            {"id": "D", "text": "Continuous deployment"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Continuous deployment automatically pushes every build that passes the pipeline all the way to "
                       "production without manual gating. (Continuous delivery stops just short, keeping a manual release decision.)",
            "distractors": {
                "A": "Continuous integration covers building and testing merges, not releasing to production.",
                "B": "Continuous delivery automates up to a release-ready artifact but keeps a human approval before production — the scenario has none.",
                "C": "A manual CAB approval is exactly the human gate that continuous deployment removes.",
            },
            "exam_pattern": "Auto-release every passing build to prod, no human gate = continuous deployment; a manual gate = continuous delivery.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (deployment vs delivery)"],
    },
    {
        "id": "cloudplus-dev-003", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "To release a new version with near-zero downtime and fast rollback, a team runs the new version "
                "('green') alongside the current one ('blue') and switches all traffic to green once it is verified, "
                "keeping blue ready to revert. Which deployment strategy is this?",
        "options": [
            {"id": "A", "text": "Canary deployment"},
            {"id": "B", "text": "Blue-green deployment"},
            {"id": "C", "text": "Rolling restart only"},
            {"id": "D", "text": "Big-bang in place"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Blue-green keeps two production environments; traffic cuts over to the new (green) once verified, and "
                       "rollback is immediate by switching back to blue, minimizing downtime and risk.",
            "distractors": {
                "A": "A canary releases to a small subset first and gradually increases, rather than switching all traffic between two full environments.",
                "C": "A rolling restart updates instances in place in batches; it is not the two-environment cutover described.",
                "D": "A big-bang in-place upgrade replaces everything at once with no easy rollback — the opposite of this strategy.",
            },
            "exam_pattern": "Two full environments, cut traffic over, instant rollback = blue-green; small gradual subset = canary.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (deployment strategies)"],
    },
    {
        "id": "cloudplus-dev-004", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 2, "type": "mcq",
        "stem": "A team releases a change to only 5% of users first, watches error and performance metrics, and "
                "expands to 100% only if the metrics stay healthy. Which deployment strategy is this?",
        "options": [
            {"id": "A", "text": "Blue-green deployment"},
            {"id": "B", "text": "Big-bang deployment"},
            {"id": "C", "text": "Canary deployment"},
            {"id": "D", "text": "Rollback"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A canary deployment exposes the change to a small percentage of users/traffic first and gradually ramps "
                       "up as metrics confirm health, limiting the blast radius of a bad release.",
            "distractors": {
                "A": "Blue-green switches all traffic between two full environments at once, not a gradual percentage ramp.",
                "B": "Big-bang releases to everyone simultaneously, the opposite of a small initial subset.",
                "D": "Rollback is reverting a release, not a progressive rollout strategy.",
            },
            "exam_pattern": "Small % first, ramp up on good metrics = canary.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — CI/CD (canary)"],
    },
    {
        "id": "cloudplus-dev-005", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 1, "type": "fill",
        "stem": "Fill in the term: The category of tools (such as Git) that records the full history of code changes "
                "and enables branching and merging — the foundation that CI/CD pipelines build on — is called ____ "
                "____ (two words).",
        "correct": ["version control", "source control", "version control system"],
        "explanation": {
            "correct": "Version control (source control) systems track the complete history of changes to code and support "
                       "branching/merging; pipelines trigger from them, making them the backbone of CI/CD.",
            "distractors": {},
            "exam_pattern": "Tool category tracking code history/branching = version control (e.g., Git).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — DevOps (version control)"],
    },
    {
        "id": "cloudplus-dev-006", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_cicd", "difficulty": 3, "type": "mcq",
        "stem": "A team keeps the desired state of both application and infrastructure in a Git repository; an automated "
                "agent continuously reconciles the live environment to match whatever is committed, and all changes are "
                "made through pull requests. What is this practice called?",
        "options": [
            {"id": "A", "text": "ClickOps (manual console changes)"},
            {"id": "B", "text": "GitOps"},
            {"id": "C", "text": "Shadow IT"},
            {"id": "D", "text": "Snowflake server administration"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "GitOps uses Git as the single source of truth for declarative infrastructure and apps; an automated "
                       "reconciler continuously drives the live state to match the repo, with changes delivered via pull requests "
                       "for review and auditability.",
            "distractors": {
                "A": "ClickOps is manual change-making in a console — the opposite of Git-driven reconciliation.",
                "C": "Shadow IT is unsanctioned technology use, unrelated to this operating model.",
                "D": "Snowflake servers are hand-tuned, non-reproducible systems GitOps specifically avoids.",
            },
            "exam_pattern": "Git as source of truth + automatic reconciliation + PR-driven changes = GitOps.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — DevOps (GitOps)"],
    },

    # ===== cloudp_iac =======================================================
    {
        "id": "cloudplus-dev-007", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 1, "type": "mcq",
        "stem": "Instead of clicking through a console, a team defines all its cloud resources in version-controlled "
                "configuration files that a tool uses to create and update the environment. What is this practice called?",
        "options": [
            {"id": "A", "text": "Infrastructure as Code (IaC)"},
            {"id": "B", "text": "Shadow IT"},
            {"id": "C", "text": "Manual provisioning"},
            {"id": "D", "text": "Penetration testing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Infrastructure as Code defines and manages infrastructure through machine-readable, version-controlled "
                       "files, making provisioning repeatable, reviewable, and automatable.",
            "distractors": {
                "B": "Shadow IT is unsanctioned tech use, not managed, version-controlled provisioning.",
                "C": "Manual provisioning via a console is exactly what IaC replaces.",
                "D": "Penetration testing assesses security; it is not a provisioning method.",
            },
            "exam_pattern": "Define infrastructure in version-controlled files = Infrastructure as Code.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (concept)"],
    },
    {
        "id": "cloudplus-dev-008", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 3, "type": "mcq",
        "stem": "A team describes the desired end state of their infrastructure (e.g., 'three web servers behind a load "
                "balancer') and lets the tool figure out the steps to reach it, rather than scripting each command. "
                "Which IaC approach is this?",
        "options": [
            {"id": "A", "text": "Imperative (procedural)"},
            {"id": "B", "text": "Declarative"},
            {"id": "C", "text": "Interpreted"},
            {"id": "D", "text": "Manual"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A declarative approach specifies the desired end state and lets the tool determine how to achieve it "
                       "(e.g., Terraform, CloudFormation). An imperative approach specifies the explicit sequence of steps.",
            "distractors": {
                "A": "Imperative/procedural defines the step-by-step commands to run, not just the desired end state.",
                "C": "'Interpreted' refers to how code is executed, not to the declarative-vs-imperative distinction.",
                "D": "Manual provisioning is not an IaC approach at all.",
            },
            "exam_pattern": "Describe the end state, tool figures out steps = declarative; script each step = imperative.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (declarative vs imperative)"],
    },
    {
        "id": "cloudplus-dev-009", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 3, "type": "mcq",
        "stem": "An IaC team values that running the same configuration repeatedly always converges to the same end "
                "state, so re-applying it causes no unintended changes. Which property are they relying on?",
        "options": [
            {"id": "A", "text": "Statefulness"},
            {"id": "B", "text": "Polymorphism"},
            {"id": "C", "text": "Idempotency"},
            {"id": "D", "text": "Concurrency"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Idempotency means applying the same declarative configuration repeatedly yields the same result; "
                       "already-correct resources are left unchanged, so re-runs are safe.",
            "distractors": {
                "A": "Statefulness describes retaining data between operations, not the safe-to-reapply property.",
                "B": "Polymorphism is an object-oriented programming concept, unrelated to IaC convergence.",
                "D": "Concurrency is about simultaneous execution, not repeatable convergence to one state.",
            },
            "exam_pattern": "Re-applying the same config changes nothing already correct = idempotency.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (idempotency)"],
    },
    {
        "id": "cloudplus-dev-010", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 2, "type": "mcq",
        "stem": "Tools such as Ansible, Puppet, and Chef are primarily used to:",
        "options": [
            {"id": "A", "text": "Automate the configuration and desired state of servers and applications (configuration management)"},
            {"id": "B", "text": "Provide Layer 7 load balancing"},
            {"id": "C", "text": "Encrypt data at rest in object storage"},
            {"id": "D", "text": "Serve as the organization's SIEM"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Configuration management tools (Ansible, Puppet, Chef) automate installing software and enforcing a "
                       "consistent, declared configuration across many systems, reducing drift.",
            "distractors": {
                "B": "Load balancing is handled by load balancers, not configuration management tools.",
                "C": "Encryption at rest is a storage/KMS function, not what these tools exist to do.",
                "D": "A SIEM correlates security events; configuration management tools do not fill that role.",
            },
            "exam_pattern": "Ansible/Puppet/Chef = configuration management (enforce consistent server/app state).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC/configuration management"],
    },
    {
        "id": "cloudplus-dev-011", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_iac", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: When servers gradually diverge from their defined baseline because of ad-hoc manual "
                "changes over time, the resulting inconsistency is called configuration ____ (one word).",
        "correct": ["drift", "configuration drift"],
        "explanation": {
            "correct": "Configuration drift is the gradual divergence of systems from their intended baseline due to "
                       "undocumented manual changes; IaC and configuration management detect and correct it by reasserting the declared state.",
            "distractors": {},
            "exam_pattern": "Systems drifting from baseline via manual changes = configuration drift (fixed by IaC/config mgmt).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — IaC (configuration drift)"],
    },

    # ===== cloudp_automation_scripting ======================================
    {
        "id": "cloudplus-dev-012", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "A cloud engineer wants to programmatically create and manage resources by sending structured requests "
                "(often JSON over HTTPS) to the provider. Which interface is designed for this?",
        "options": [
            {"id": "A", "text": "The physical console port"},
            {"id": "B", "text": "A RAID controller"},
            {"id": "C", "text": "RDP to each server"},
            {"id": "D", "text": "A REST API"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Cloud providers expose REST APIs that accept structured requests (commonly JSON over HTTPS) so resources "
                       "can be created and managed programmatically, which underpins SDKs, CLIs, and automation.",
            "distractors": {
                "A": "A physical console port is for local hardware access, not programmatic cloud control.",
                "B": "A RAID controller manages disks; it is not a cloud management interface.",
                "C": "RDP gives interactive desktop access to a single server, not programmatic resource management.",
            },
            "exam_pattern": "Programmatic resource management via structured JSON/HTTPS calls = REST API.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (APIs)"],
    },
    {
        "id": "cloudplus-dev-013", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "Which data format is commonly used for both configuration files and API payloads in cloud automation "
                "because it is human-readable and maps cleanly to key-value structures?",
        "options": [
            {"id": "A", "text": "JSON (or YAML)"},
            {"id": "B", "text": "A compiled binary blob"},
            {"id": "C", "text": "A RAID stripe set"},
            {"id": "D", "text": "An ISO disk image"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "JSON and YAML are the dominant human-readable, structured formats for cloud configuration and API "
                       "payloads, representing nested key-value data that tools and humans can both parse.",
            "distractors": {
                "B": "A compiled binary blob is not human-readable and is not the standard for config/API payloads.",
                "C": "A RAID stripe set is a storage construct, not a data-serialization format.",
                "D": "An ISO image is a disk-image format, not a configuration/data-exchange format.",
            },
            "exam_pattern": "Human-readable structured config/API data = JSON/YAML.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation/scripting (data formats)"],
    },
    {
        "id": "cloudplus-dev-014", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 2, "type": "mcq",
        "stem": "A pipeline should start automatically the moment code is pushed to the repository. Which mechanism lets "
                "the repository notify the pipeline of the event in real time?",
        "options": [
            {"id": "A", "text": "A nightly cron job that polls for changes"},
            {"id": "B", "text": "A webhook (event-driven HTTP callback)"},
            {"id": "C", "text": "A manual email to the build team"},
            {"id": "D", "text": "A RAID rebuild"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A webhook is an event-driven HTTP callback: the repository POSTs to the pipeline's URL the instant a "
                       "push occurs, triggering the build immediately without polling.",
            "distractors": {
                "A": "A nightly polling cron job reacts on a schedule, not in real time at the moment of the push.",
                "C": "A manual email is not an automated, real-time trigger.",
                "D": "A RAID rebuild is a storage recovery operation, unrelated to pipeline triggering.",
            },
            "exam_pattern": "Real-time event notification to trigger automation = webhook (vs scheduled polling).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (event-driven triggers/webhooks)"],
    },
    {
        "id": "cloudplus-dev-015", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 1, "type": "mcq",
        "stem": "An administrator writes a short shell/PowerShell script to automate a repetitive task such as rotating "
                "logs nightly. The chief benefit of scripting routine tasks is:",
        "options": [
            {"id": "A", "text": "It guarantees the task never needs testing"},
            {"id": "B", "text": "It makes the task slower but more secure"},
            {"id": "C", "text": "Consistency and reduced human error for repetitive work"},
            {"id": "D", "text": "It removes the need for any access controls"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Scripting repetitive tasks yields consistent, repeatable execution and reduces human error and toil "
                       "compared with performing the steps manually each time.",
            "distractors": {
                "A": "Scripts still require testing; automation does not remove that need.",
                "B": "Automation generally speeds tasks up; 'slower but more secure' is not its benefit.",
                "D": "Scripts must still run under proper access controls; automation does not eliminate them.",
            },
            "exam_pattern": "Automate repetitive work for consistency and fewer human errors.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation/scripting (benefits)"],
    },
    {
        "id": "cloudplus-dev-016", "exam": "cloudplus", "domain": "cloudp_devops",
        "subtopic": "cloudp_automation_scripting", "difficulty": 3, "type": "multi",
        "stem": "A team is deciding what to automate first. Which TWO tasks are the best candidates for "
                "scripting/automation? (Choose two.)",
        "options": [
            {"id": "A", "text": "Provisioning identical test environments on demand"},
            {"id": "B", "text": "Making a one-time, never-repeated judgment call about vendor selection"},
            {"id": "C", "text": "Nightly database backups and log rotation"},
            {"id": "D", "text": "A unique architectural design decision requiring human trade-off analysis"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Repetitive, well-defined, frequently performed tasks — spinning up standard environments and nightly "
                       "backups/log rotation — are ideal automation targets, delivering consistency and time savings.",
            "distractors": {
                "B": "A one-time, non-repeating judgment call gains little from automation and needs human reasoning.",
                "D": "A unique design decision requiring human trade-off analysis is not a repeatable task to script.",
            },
            "exam_pattern": "Automate repetitive, well-defined, frequent tasks; leave one-off judgment to humans.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 5 — Automation (what to automate)"],
    },
]
