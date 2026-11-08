"""AWS Certified Cloud Practitioner (CLF-C02) — Domain 2: Security and Compliance.

Original, objective-aligned practice items (never real or memorized exam items),
written at Cloud-Practitioner depth: purpose, when-to-use, and who is responsible.
Facts are limited to well-established, current CLF-C02 content; exact limits and
prices are deliberately avoided. build_content.py shuffles option order (seeded by
question id), so the answer key below is not positionally biased.

Subtopics covered (all four):
  - shared_responsibility : AWS Shared Responsibility Model
  - compliance_governance : Artifact, Audit Manager, Config/CloudTrail, data residency
  - iam                   : users, groups, roles, policies, root user, MFA, SSO
  - security_services     : KMS, Shield, WAF, GuardDuty, Inspector, Macie, Secrets
                            Manager, Security Hub, ACM, encryption in transit/at rest
"""

QUESTIONS = [
    # ===== Shared Responsibility Model ======================================
    {
        "id": "clf-sec-001", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 1, "type": "mcq",
        "stem": "Under the AWS Shared Responsibility Model, which party is responsible for the "
                "physical security of AWS data centers?",
        "options": [
            {"id": "A", "text": "The customer"},
            {"id": "B", "text": "AWS"},
            {"id": "C", "text": "A third-party compliance auditor"},
            {"id": "D", "text": "The customer and AWS equally"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS is responsible for 'security OF the cloud,' which includes the physical "
                       "security of its data centers and global infrastructure.",
            "distractors": {
                "A": "The customer manages 'security IN the cloud' (data and configuration), not the physical facilities.",
                "C": "Auditors verify AWS's controls but are not responsible for operating physical security.",
                "D": "Physical data-center security is solely AWS's responsibility, not a shared duty.",
            },
            "exam_pattern": "Physical, hardware, and facility wording points to AWS ('security OF the cloud').",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-002", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "mcq",
        "stem": "A company runs applications on Amazon EC2 instances. Under the Shared Responsibility "
                "Model, who must patch the guest operating system?",
        "options": [
            {"id": "A", "text": "AWS"},
            {"id": "B", "text": "The EC2 service patches it automatically"},
            {"id": "C", "text": "The customer"},
            {"id": "D", "text": "AWS Support engineers"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "For EC2 (an IaaS offering), the customer manages the guest OS, including applying patches and updates.",
            "distractors": {
                "A": "AWS patches the host infrastructure and hypervisor, but not the customer's guest OS on EC2.",
                "B": "EC2 does not automatically patch the guest OS; that is left to the customer.",
                "D": "AWS Support can advise but does not patch customer instances.",
            },
            "exam_pattern": "EC2 (IaaS) plus guest OS or patching = customer responsibility.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-003", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 1, "type": "mcq",
        "stem": "In the Shared Responsibility Model, which item is always the customer's responsibility, "
                "regardless of which AWS service is used?",
        "options": [
            {"id": "A", "text": "Securing the physical server hardware"},
            {"id": "B", "text": "Maintaining the hypervisor"},
            {"id": "C", "text": "Decommissioning failed storage devices"},
            {"id": "D", "text": "Managing their own data and its classification"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Customer data and its classification are always the customer's responsibility ('security IN the cloud').",
            "distractors": {
                "A": "Physical hardware security is AWS's responsibility (security OF the cloud).",
                "B": "The hypervisor and virtualization layer are maintained by AWS.",
                "C": "Secure disposal of storage media is handled by AWS.",
            },
            "exam_pattern": "'Customer data' is owned by the customer in every service model.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-004", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "mcq",
        "stem": "A customer moves from self-managing a database on EC2 to the managed Amazon RDS service. "
                "Which task does AWS now take over?",
        "options": [
            {"id": "A", "text": "Patching the underlying database engine and operating system"},
            {"id": "B", "text": "Creating database users and granting data access"},
            {"id": "C", "text": "Choosing which data to store in the database"},
            {"id": "D", "text": "Configuring the security group rules"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With managed Amazon RDS, AWS handles the underlying operating system and database engine patching.",
            "distractors": {
                "B": "Database users and data-level access remain the customer's responsibility.",
                "C": "The customer always controls their own data.",
                "D": "Security group (firewall) configuration stays with the customer.",
            },
            "exam_pattern": "A managed service shifts OS/engine patching to AWS; data and access stay with the customer.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-005", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are customer responsibilities under the AWS Shared "
                "Responsibility Model? (Choose two.)",
        "options": [
            {"id": "A", "text": "Configuring security group (firewall) rules"},
            {"id": "B", "text": "Managing physical access to AWS data centers"},
            {"id": "C", "text": "Patching the guest operating system on EC2 instances"},
            {"id": "D", "text": "Maintaining the hardware that runs AWS services"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Configuring security groups and patching the EC2 guest OS are both 'security IN the cloud' "
                       "tasks owned by the customer.",
            "distractors": {
                "B": "Physical access to data centers is AWS's responsibility (security OF the cloud).",
                "D": "Maintaining the underlying hardware is AWS's responsibility.",
            },
            "exam_pattern": "On 'choose two' responsibility items, pick what you configure or run inside your own account.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-006", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "mcq",
        "stem": "A developer runs code on AWS Lambda. Under the Shared Responsibility Model, what "
                "remains the customer's responsibility?",
        "options": [
            {"id": "A", "text": "Patching the operating system that runs the function"},
            {"id": "B", "text": "The function code and the IAM permissions it uses"},
            {"id": "C", "text": "Managing the underlying compute fleet"},
            {"id": "D", "text": "Scaling the execution environment"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "With Lambda, AWS manages the operating system and compute; the customer is responsible for "
                       "their function code and the IAM permissions it uses.",
            "distractors": {
                "A": "For Lambda, AWS manages and patches the underlying operating system.",
                "C": "AWS manages the underlying compute fleet for Lambda.",
                "D": "AWS automatically scales the Lambda execution environment.",
            },
            "exam_pattern": "Serverless (Lambda): the customer owns the code and access; AWS owns the rest.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-007", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 1, "type": "mcq",
        "stem": "Which of the following is handled by AWS, not the customer, under the Shared "
                "Responsibility Model?",
        "options": [
            {"id": "A", "text": "Encrypting the customer's application data"},
            {"id": "B", "text": "Managing IAM user permissions"},
            {"id": "C", "text": "Securely disposing of decommissioned storage hardware"},
            {"id": "D", "text": "Configuring the guest OS firewall"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Secure disposal and decommissioning of storage hardware is AWS's responsibility.",
            "distractors": {
                "A": "Choosing and applying encryption to customer data is a customer responsibility.",
                "B": "IAM user and permission management belongs to the customer.",
                "D": "Guest OS firewall configuration is the customer's job.",
            },
            "exam_pattern": "Hardware lifecycle and media disposal belong to AWS.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-008", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 2, "type": "mcq",
        "stem": "Under the Shared Responsibility Model, who is responsible for choosing and configuring "
                "how customer data is encrypted, both in transit and at rest?",
        "options": [
            {"id": "A", "text": "AWS, because encryption is part of the managed infrastructure"},
            {"id": "B", "text": "No one; data in AWS cannot be customer-encrypted"},
            {"id": "C", "text": "An external compliance auditor"},
            {"id": "D", "text": "The customer, who controls encryption of their data"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The customer decides on and configures how their data is encrypted, in transit and at rest, "
                       "even when using managed services.",
            "distractors": {
                "A": "AWS secures the infrastructure, but the customer configures data encryption choices.",
                "B": "AWS services support both in-transit and at-rest encryption.",
                "C": "Auditors verify controls; they do not configure a customer's encryption.",
            },
            "exam_pattern": "Encryption choices for your data are a customer responsibility.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-009", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 3, "type": "mcq",
        "stem": "An auditor asks a company to prove that OS patches are current on its EC2 fleet. Under the "
                "Shared Responsibility Model, who must maintain those patches?",
        "options": [
            {"id": "A", "text": "AWS, as part of security of the cloud"},
            {"id": "B", "text": "The customer, as part of security in the cloud"},
            {"id": "C", "text": "Amazon Inspector, which applies the patches automatically"},
            {"id": "D", "text": "The AWS data-center operations team"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Guest OS patching on EC2 is the customer's responsibility ('security IN the cloud').",
            "distractors": {
                "A": "AWS patches the underlying host, not the customer's guest OS on EC2.",
                "C": "Amazon Inspector assesses instances for vulnerabilities but does not apply patches.",
                "D": "AWS staff do not patch customer-managed guest operating systems.",
            },
            "exam_pattern": "If it runs inside your EC2 instance, you are responsible for patching it.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },
    {
        "id": "clf-sec-010", "exam": "clf", "domain": "security_compliance",
        "subtopic": "shared_responsibility", "difficulty": 1, "type": "mcq",
        "stem": "In the AWS Shared Responsibility Model, the phrase 'security of the cloud' describes "
                "whose responsibilities?",
        "options": [
            {"id": "A", "text": "AWS's"},
            {"id": "B", "text": "The customer's"},
            {"id": "C", "text": "A managed service provider's"},
            {"id": "D", "text": "The end user's"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Security OF the cloud' describes AWS's responsibility for the infrastructure that runs all AWS services.",
            "distractors": {
                "B": "The customer handles 'security IN the cloud' (data, IAM, configuration).",
                "C": "'Managed service provider' is not a party defined in the model.",
                "D": "End users are not a party defined in the model.",
            },
            "exam_pattern": "'OF the cloud' = AWS; 'IN the cloud' = customer.",
        },
        "references": ["AWS Shared Responsibility Model"],
    },

    # ===== Compliance and Governance ========================================
    {
        "id": "clf-sec-011", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 1, "type": "mcq",
        "stem": "Which AWS service provides on-demand access to AWS compliance reports such as SOC and "
                "PCI DSS documents?",
        "options": [
            {"id": "A", "text": "AWS Config"},
            {"id": "B", "text": "AWS Artifact"},
            {"id": "C", "text": "AWS CloudTrail"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Artifact is the self-service portal for on-demand AWS compliance reports and agreements.",
            "distractors": {
                "A": "AWS Config tracks resource configurations, not compliance report downloads.",
                "C": "AWS CloudTrail records API activity, not downloadable compliance reports.",
                "D": "AWS Trusted Advisor gives best-practice recommendations, not compliance reports.",
            },
            "exam_pattern": "Need an AWS compliance report or certification document = AWS Artifact.",
        },
        "references": ["AWS Artifact"],
    },
    {
        "id": "clf-sec-012", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "A healthcare provider must review and accept a Business Associate Addendum (BAA) with AWS "
                "for HIPAA workloads. Where is this agreement available?",
        "options": [
            {"id": "A", "text": "AWS Artifact"},
            {"id": "B", "text": "AWS Secrets Manager"},
            {"id": "C", "text": "Amazon Macie"},
            {"id": "D", "text": "AWS Audit Manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Artifact provides AWS agreements, such as the BAA, which customers can review and accept online.",
            "distractors": {
                "B": "AWS Secrets Manager stores and rotates secrets, not legal agreements.",
                "C": "Amazon Macie discovers sensitive data in S3; it does not host agreements.",
                "D": "AWS Audit Manager automates evidence collection but does not host the BAA.",
            },
            "exam_pattern": "AWS online agreements (BAA/NDA) are reviewed and accepted in AWS Artifact.",
        },
        "references": ["AWS Artifact"],
    },
    {
        "id": "clf-sec-013", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "A security team needs a record of who made each API call in their AWS account, for "
                "auditing. Which service should they use?",
        "options": [
            {"id": "A", "text": "Amazon CloudWatch"},
            {"id": "B", "text": "AWS Config"},
            {"id": "C", "text": "AWS CloudTrail"},
            {"id": "D", "text": "AWS Artifact"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "AWS CloudTrail records API calls and account activity for governance, compliance, and auditing.",
            "distractors": {
                "A": "Amazon CloudWatch monitors metrics and logs for performance, not an API audit trail.",
                "B": "AWS Config tracks resource configuration state, not who called each API.",
                "D": "AWS Artifact provides compliance documents, not account activity logs.",
            },
            "exam_pattern": "'Who did what, and when' via API history = AWS CloudTrail.",
        },
        "references": ["AWS CloudTrail"],
    },
    {
        "id": "clf-sec-014", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "A governance team wants to continuously evaluate whether resource configurations meet "
                "internal rules and track configuration changes over time. Which service fits best?",
        "options": [
            {"id": "A", "text": "AWS Config"},
            {"id": "B", "text": "AWS CloudTrail"},
            {"id": "C", "text": "Amazon Inspector"},
            {"id": "D", "text": "AWS Shield"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS Config records resource configurations, tracks changes over time, and evaluates them against desired rules.",
            "distractors": {
                "B": "AWS CloudTrail logs API calls, not the configuration state of resources.",
                "C": "Amazon Inspector assesses software vulnerabilities, not configuration compliance.",
                "D": "AWS Shield protects against DDoS attacks.",
            },
            "exam_pattern": "Resource configuration compliance and history = AWS Config.",
        },
        "references": ["AWS Config"],
    },
    {
        "id": "clf-sec-015", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 3, "type": "mcq",
        "stem": "An investigator must determine which IAM user deleted a specific resource and exactly "
                "when it happened. Which service provides this?",
        "options": [
            {"id": "A", "text": "AWS Config"},
            {"id": "B", "text": "AWS CloudTrail"},
            {"id": "C", "text": "AWS Artifact"},
            {"id": "D", "text": "AWS Audit Manager"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS CloudTrail logs the identity, action, and timestamp of API calls, so it shows who deleted "
                       "the resource and when.",
            "distractors": {
                "A": "AWS Config shows configuration state and changes but not the user identity behind each API call.",
                "C": "AWS Artifact provides compliance reports, not account activity.",
                "D": "AWS Audit Manager automates evidence collection, not per-action user attribution.",
            },
            "exam_pattern": "User identity plus time of an action = CloudTrail; resource state over time = Config.",
        },
        "references": ["AWS CloudTrail"],
    },
    {
        "id": "clf-sec-016", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "Which AWS service continuously assesses risk and automates the collection of evidence to "
                "help prepare for audits against frameworks and regulations?",
        "options": [
            {"id": "A", "text": "AWS Artifact"},
            {"id": "B", "text": "AWS CloudTrail"},
            {"id": "C", "text": "Amazon GuardDuty"},
            {"id": "D", "text": "AWS Audit Manager"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "AWS Audit Manager continuously audits AWS usage and automates evidence collection to simplify compliance assessments.",
            "distractors": {
                "A": "AWS Artifact only provides pre-built reports and agreements, not automated evidence collection.",
                "B": "AWS CloudTrail logs API activity but does not map evidence to compliance frameworks.",
                "C": "Amazon GuardDuty is a threat-detection service.",
            },
            "exam_pattern": "'Automate audit evidence collection' = AWS Audit Manager.",
        },
        "references": ["AWS Audit Manager"],
    },
    {
        "id": "clf-sec-017", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "A company must ensure its customer data is stored only within a specific country to meet "
                "data-residency rules. Which AWS capability lets it control this?",
        "options": [
            {"id": "A", "text": "Enabling AWS Shield Advanced"},
            {"id": "B", "text": "Choosing a larger EC2 instance type"},
            {"id": "C", "text": "Selecting the AWS Region where resources are deployed"},
            {"id": "D", "text": "Turning on Amazon Macie"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Customers choose the Region, and AWS does not move their data out of it without consent, which "
                       "supports data residency and sovereignty requirements.",
            "distractors": {
                "A": "AWS Shield Advanced provides DDoS protection, not control over data location.",
                "B": "Instance size has no effect on where data is stored.",
                "D": "Amazon Macie discovers sensitive data but does not control its geographic location.",
            },
            "exam_pattern": "Data residency and sovereignty = the customer's choice of Region.",
        },
        "references": ["AWS Global Infrastructure / Regions"],
    },
    {
        "id": "clf-sec-018", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 1, "type": "mcq",
        "stem": "AWS maintains compliance with programs such as PCI DSS, ISO 27001, and SOC. How can a "
                "customer obtain proof of these certifications?",
        "options": [
            {"id": "A", "text": "Open a support case with AWS Shield"},
            {"id": "B", "text": "Query the account with Amazon Athena"},
            {"id": "C", "text": "Download the audit reports from AWS Artifact"},
            {"id": "D", "text": "Enable AWS WAF on the account"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "AWS Artifact provides the certification and attestation reports that demonstrate AWS's compliance.",
            "distractors": {
                "A": "AWS Shield is a DDoS protection service, unrelated to compliance reports.",
                "B": "Amazon Athena queries data in S3; it does not supply AWS's compliance reports.",
                "D": "AWS WAF filters web traffic and does not provide certifications.",
            },
            "exam_pattern": "Proof of AWS's certifications = reports in AWS Artifact.",
        },
        "references": ["AWS Artifact"],
    },
    {
        "id": "clf-sec-019", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 2, "type": "mcq",
        "stem": "Which statement best describes how compliance works under the AWS Shared Responsibility Model?",
        "options": [
            {"id": "A", "text": "AWS is fully responsible for the customer's compliance"},
            {"id": "B", "text": "The customer is responsible for the data center's compliance"},
            {"id": "C", "text": "AWS certifies the infrastructure, while the customer is responsible for compliance of what they build in the cloud"},
            {"id": "D", "text": "Compliance is owned entirely by third-party auditors"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Compliance is shared: AWS certifies the underlying infrastructure, and customers are responsible "
                       "for their own workloads and data meeting requirements.",
            "distractors": {
                "A": "Customers remain responsible for their own workloads meeting requirements; AWS does not own it fully.",
                "B": "The customer does not run or certify AWS's physical data centers.",
                "D": "Auditors verify compliance, but responsibility is shared between AWS and the customer.",
            },
            "exam_pattern": "Compliance is shared, just like security.",
        },
        "references": ["AWS Compliance Programs"],
    },
    {
        "id": "clf-sec-020", "exam": "clf", "domain": "security_compliance",
        "subtopic": "compliance_governance", "difficulty": 3, "type": "mcq",
        "stem": "A company must show auditors a timeline of how one security group's rules changed over the "
                "past month. Which service provides this configuration history?",
        "options": [
            {"id": "A", "text": "AWS CloudTrail"},
            {"id": "B", "text": "AWS Config"},
            {"id": "C", "text": "AWS Artifact"},
            {"id": "D", "text": "AWS Trusted Advisor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Config records configuration snapshots and a timeline of changes for resources such as security groups.",
            "distractors": {
                "A": "AWS CloudTrail shows the API calls that made changes, but not a configuration-state timeline per resource.",
                "C": "AWS Artifact supplies compliance documents, not resource change history.",
                "D": "AWS Trusted Advisor gives recommendations, not a configuration timeline.",
            },
            "exam_pattern": "Configuration change history or timeline for a resource = AWS Config.",
        },
        "references": ["AWS Config"],
    },

    # ===== Identity and Access Management (IAM) =============================
    {
        "id": "clf-sec-021", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "multi",
        "stem": "Which TWO actions are AWS-recommended best practices for protecting the account root "
                "user? (Choose two.)",
        "options": [
            {"id": "A", "text": "Enable multi-factor authentication (MFA) on the root user"},
            {"id": "B", "text": "Use the root user for all daily administrative work"},
            {"id": "C", "text": "Avoid using root access keys and remove them if they exist"},
            {"id": "D", "text": "Store the root password in the application source code"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Enabling MFA on root and avoiding/removing root access keys are both recommended protections "
                       "for this highly privileged identity.",
            "distractors": {
                "B": "The root user should not be used for routine tasks; create IAM identities instead.",
                "D": "Storing the root password in source code exposes it and is never recommended.",
            },
            "exam_pattern": "Root best-practice 'choose two' items usually pair MFA with removing root access keys.",
        },
        "references": ["AWS IAM Best Practices"],
    },
    {
        "id": "clf-sec-022", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "An application on an EC2 instance needs to read objects from an Amazon S3 bucket. What is "
                "the most secure way to grant this access?",
        "options": [
            {"id": "A", "text": "Attach an IAM role to the EC2 instance"},
            {"id": "B", "text": "Embed the root user's access keys in the application"},
            {"id": "C", "text": "Hard-code an IAM user's access keys in the application"},
            {"id": "D", "text": "Make the S3 bucket publicly readable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IAM role attached to the instance supplies temporary credentials automatically, with no long-term keys to manage.",
            "distractors": {
                "B": "Root access keys should never be used in applications.",
                "C": "Hard-coding long-term access keys is insecure and hard to rotate.",
                "D": "Making the bucket public exposes the data to everyone on the internet.",
            },
            "exam_pattern": "An app on EC2 needing AWS access = attach an IAM role, not stored keys.",
        },
        "references": ["AWS IAM Roles"],
    },
    {
        "id": "clf-sec-023", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary purpose of an IAM group?",
        "options": [
            {"id": "A", "text": "To store and manage encryption keys"},
            {"id": "B", "text": "To attach permissions to a collection of IAM users at once"},
            {"id": "C", "text": "To provide DDoS protection for applications"},
            {"id": "D", "text": "To record API calls for auditing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An IAM group lets you attach policies to many users at once, which simplifies permission management.",
            "distractors": {
                "A": "Managing encryption keys is the job of AWS KMS.",
                "C": "DDoS protection is provided by AWS Shield.",
                "D": "Recording API calls is done by AWS CloudTrail.",
            },
            "exam_pattern": "IAM group = manage permissions for many users together.",
        },
        "references": ["AWS IAM (Users, Groups, and Roles)"],
    },
    {
        "id": "clf-sec-024", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "A security policy states that each user should receive only the permissions required to "
                "perform their job. Which security principle does this describe?",
        "options": [
            {"id": "A", "text": "Defense in depth"},
            {"id": "B", "text": "Shared responsibility"},
            {"id": "C", "text": "Elasticity"},
            {"id": "D", "text": "Least privilege"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Granting only the permissions needed to do a job is the principle of least privilege.",
            "distractors": {
                "A": "Defense in depth refers to layering multiple security controls, not scoping permissions.",
                "B": "Shared responsibility splits duties between AWS and the customer.",
                "C": "Elasticity is a scaling concept, not a security principle.",
            },
            "exam_pattern": "'Only the permissions needed' = principle of least privilege.",
        },
        "references": ["AWS IAM Best Practices"],
    },
    {
        "id": "clf-sec-025", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly contrasts IAM access keys with a console password?",
        "options": [
            {"id": "A", "text": "Access keys can be created only for the root user"},
            {"id": "B", "text": "Passwords are used by the CLI and access keys by the console"},
            {"id": "C", "text": "Access keys are for programmatic access (CLI, SDK, API); a password signs a user in to the console"},
            {"id": "D", "text": "Both are used only for physical data-center entry"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Access keys authenticate programmatic requests (CLI, SDK, API), while a password signs a user in to the console.",
            "distractors": {
                "A": "IAM users, not only the root user, can have access keys.",
                "B": "This reverses their roles: the CLI uses access keys, and the console uses a password.",
                "D": "Neither credential is used for physical facility access.",
            },
            "exam_pattern": "Programmatic access = access keys; human console sign-in = password.",
        },
        "references": ["AWS IAM (Access Keys)"],
    },
    {
        "id": "clf-sec-026", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 1, "type": "mcq",
        "stem": "In AWS IAM, what does a policy define?",
        "options": [
            {"id": "A", "text": "The permissions that allow or deny specific actions on specific resources"},
            {"id": "B", "text": "The physical location of a data center"},
            {"id": "C", "text": "The hourly price of an EC2 instance"},
            {"id": "D", "text": "The encryption algorithm used by AWS KMS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IAM policy is a JSON document that defines permissions, specifying allowed or denied actions on resources.",
            "distractors": {
                "B": "Data-center location is unrelated to an IAM policy.",
                "C": "Pricing is not defined by IAM policies.",
                "D": "Encryption algorithms are not set by IAM policies.",
            },
            "exam_pattern": "IAM policy = a JSON document of allowed/denied actions on resources.",
        },
        "references": ["AWS IAM Policies"],
    },
    {
        "id": "clf-sec-027", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants employees to sign in once and gain access to multiple AWS accounts "
                "and business applications. Which service supports this?",
        "options": [
            {"id": "A", "text": "AWS Key Management Service"},
            {"id": "B", "text": "AWS IAM Identity Center (successor to AWS SSO)"},
            {"id": "C", "text": "Amazon GuardDuty"},
            {"id": "D", "text": "AWS Artifact"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS IAM Identity Center provides single sign-on access to multiple AWS accounts and applications.",
            "distractors": {
                "A": "AWS KMS manages encryption keys, not single sign-on.",
                "C": "Amazon GuardDuty is a threat-detection service.",
                "D": "AWS Artifact provides compliance documents.",
            },
            "exam_pattern": "Single sign-on across multiple accounts/apps = IAM Identity Center.",
        },
        "references": ["AWS IAM Identity Center"],
    },
    {
        "id": "clf-sec-028", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 2, "type": "mcq",
        "stem": "Why is the AWS account root user considered especially sensitive and in need of protection?",
        "options": [
            {"id": "A", "text": "It can only view billing information"},
            {"id": "B", "text": "It has no permissions until policies are attached"},
            {"id": "C", "text": "It is automatically disabled after account sign-up"},
            {"id": "D", "text": "It has complete, unrestricted access to every service and resource in the account"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The root user has full, unrestricted access to everything in the account, so it must be tightly protected.",
            "distractors": {
                "A": "The root user can do far more than view billing.",
                "B": "The root user starts with full access, not none.",
                "C": "The root user is not automatically disabled.",
            },
            "exam_pattern": "Root = unlimited account power, so lock it down.",
        },
        "references": ["AWS IAM (Root User)"],
    },
    {
        "id": "clf-sec-029", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 1, "type": "mcq",
        "stem": "Which IAM identity is designed to be assumed by a trusted entity, such as an AWS service, "
                "and supplies temporary credentials?",
        "options": [
            {"id": "A", "text": "An IAM role"},
            {"id": "B", "text": "An IAM group"},
            {"id": "C", "text": "The root user"},
            {"id": "D", "text": "A long-term access key stored in code"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IAM role is assumed by trusted entities (services, users, applications) and grants temporary credentials.",
            "distractors": {
                "B": "An IAM group organizes users and their permissions; it is not assumed and issues no credentials.",
                "C": "The root user is a permanent, highly privileged identity, not a temporary role.",
                "D": "A stored access key is a long-term credential, not a role that grants temporary access.",
            },
            "exam_pattern": "Temporary credentials for a trusted entity = IAM role.",
        },
        "references": ["AWS IAM Roles"],
    },
    {
        "id": "clf-sec-030", "exam": "clf", "domain": "security_compliance",
        "subtopic": "iam", "difficulty": 3, "type": "mcq",
        "stem": "A startup discovers it is using the root user's access keys inside a deployment script. "
                "Following AWS best practices, what should it do?",
        "options": [
            {"id": "A", "text": "Share the root keys with more developers for convenience"},
            {"id": "B", "text": "Commit the root keys to a public repository"},
            {"id": "C", "text": "Remove the root access keys and switch to an IAM role or IAM user with least privilege"},
            {"id": "D", "text": "Keep the root keys but turn off MFA"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Best practice is to avoid root access keys entirely: remove them and use an IAM role or IAM user "
                       "scoped with least privilege.",
            "distractors": {
                "A": "Sharing root keys widens the blast radius of a compromise.",
                "B": "Publishing keys publicly is a severe security breach.",
                "D": "Disabling MFA weakens security instead of improving it.",
            },
            "exam_pattern": "Root access keys in use = remove them and switch to an IAM role or user.",
        },
        "references": ["AWS IAM Best Practices"],
    },

    # ===== Security Services =================================================
    {
        "id": "clf-sec-031", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 1, "type": "mcq",
        "stem": "Which AWS service is used to create and manage the cryptographic keys that encrypt data "
                "across AWS services?",
        "options": [
            {"id": "A", "text": "AWS Shield"},
            {"id": "B", "text": "Amazon GuardDuty"},
            {"id": "C", "text": "AWS WAF"},
            {"id": "D", "text": "AWS Key Management Service (KMS)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "AWS KMS creates and manages cryptographic keys and controls their use for encryption across AWS services.",
            "distractors": {
                "A": "AWS Shield provides DDoS protection.",
                "B": "Amazon GuardDuty is a threat-detection service.",
                "C": "AWS WAF filters malicious web traffic.",
            },
            "exam_pattern": "Create and manage encryption keys = AWS KMS.",
        },
        "references": ["AWS Key Management Service (KMS)"],
    },
    {
        "id": "clf-sec-032", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "A public-facing web application is being overwhelmed by a distributed denial-of-service "
                "(DDoS) attack. Which AWS service is designed to help defend against this?",
        "options": [
            {"id": "A", "text": "Amazon Macie"},
            {"id": "B", "text": "AWS Secrets Manager"},
            {"id": "C", "text": "AWS Shield"},
            {"id": "D", "text": "Amazon Inspector"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "AWS Shield is a managed service specifically for protecting against DDoS attacks.",
            "distractors": {
                "A": "Amazon Macie discovers sensitive data in S3.",
                "B": "AWS Secrets Manager stores and rotates secrets.",
                "D": "Amazon Inspector assesses workloads for software vulnerabilities.",
            },
            "exam_pattern": "DDoS protection = AWS Shield.",
        },
        "references": ["AWS Shield"],
    },
    {
        "id": "clf-sec-033", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "A team wants to block common web exploits such as SQL injection and cross-site scripting "
                "before they reach an application. Which service should they use?",
        "options": [
            {"id": "A", "text": "AWS KMS"},
            {"id": "B", "text": "AWS WAF"},
            {"id": "C", "text": "Amazon GuardDuty"},
            {"id": "D", "text": "AWS Config"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS WAF (Web Application Firewall) filters HTTP(S) requests and blocks common web exploits like SQL injection and XSS.",
            "distractors": {
                "A": "AWS KMS manages encryption keys, not web traffic filtering.",
                "C": "Amazon GuardDuty detects threats from logs but is not a web-request filter.",
                "D": "AWS Config tracks resource configuration.",
            },
            "exam_pattern": "Filter malicious web requests (SQLi/XSS) at layer 7 = AWS WAF.",
        },
        "references": ["AWS WAF"],
    },
    {
        "id": "clf-sec-034", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 3, "type": "mcq",
        "stem": "A company wants a service that continuously analyzes account activity and network logs to "
                "detect unusual behavior, such as potentially compromised credentials. Which service fits?",
        "options": [
            {"id": "A", "text": "Amazon Inspector"},
            {"id": "B", "text": "Amazon GuardDuty"},
            {"id": "C", "text": "AWS WAF"},
            {"id": "D", "text": "AWS Artifact"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Amazon GuardDuty is a threat-detection service that analyzes logs (such as CloudTrail, VPC Flow "
                       "Logs, and DNS logs) to identify malicious or unusual activity.",
            "distractors": {
                "A": "Amazon Inspector scans for software vulnerabilities, not behavioral threats in logs.",
                "C": "AWS WAF filters inbound web requests; it does not analyze account activity.",
                "D": "AWS Artifact provides compliance documents.",
            },
            "exam_pattern": "Threat detection from logs and behavior = Amazon GuardDuty.",
        },
        "references": ["Amazon GuardDuty"],
    },
    {
        "id": "clf-sec-035", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 3, "type": "mcq",
        "stem": "A security team needs to automatically scan EC2 instances and container images for software "
                "vulnerabilities and unintended network exposure. Which service should they choose?",
        "options": [
            {"id": "A", "text": "Amazon Macie"},
            {"id": "B", "text": "AWS Shield"},
            {"id": "C", "text": "Amazon Inspector"},
            {"id": "D", "text": "Amazon GuardDuty"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Amazon Inspector performs automated vulnerability assessments of workloads such as EC2 instances, "
                       "container images, and Lambda functions.",
            "distractors": {
                "A": "Amazon Macie discovers sensitive data in S3, not software vulnerabilities.",
                "B": "AWS Shield provides DDoS protection.",
                "D": "Amazon GuardDuty detects threats from logs; it does not scan for software CVEs.",
            },
            "exam_pattern": "Automated vulnerability/CVE scanning of workloads = Amazon Inspector.",
        },
        "references": ["Amazon Inspector"],
    },
    {
        "id": "clf-sec-036", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 3, "type": "mcq",
        "stem": "A company wants to automatically discover and help protect sensitive data, such as "
                "personally identifiable information (PII), stored in Amazon S3. Which service is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Amazon Inspector"},
            {"id": "B", "text": "AWS WAF"},
            {"id": "C", "text": "AWS KMS"},
            {"id": "D", "text": "Amazon Macie"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Amazon Macie uses machine learning to discover, classify, and help protect sensitive data like PII in Amazon S3.",
            "distractors": {
                "A": "Amazon Inspector assesses vulnerabilities, not the content of stored data.",
                "B": "AWS WAF filters web traffic.",
                "C": "AWS KMS manages encryption keys but does not discover sensitive data.",
            },
            "exam_pattern": "Find and classify sensitive data/PII in S3 = Amazon Macie.",
        },
        "references": ["Amazon Macie"],
    },
    {
        "id": "clf-sec-037", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "An application needs to store database credentials securely and rotate them automatically. "
                "Which AWS service is designed for this?",
        "options": [
            {"id": "A", "text": "Amazon GuardDuty"},
            {"id": "B", "text": "AWS Shield"},
            {"id": "C", "text": "AWS Secrets Manager"},
            {"id": "D", "text": "AWS Config"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "AWS Secrets Manager securely stores secrets like database credentials and supports automatic rotation.",
            "distractors": {
                "A": "Amazon GuardDuty is a threat-detection service.",
                "B": "AWS Shield provides DDoS protection.",
                "D": "AWS Config tracks resource configurations.",
            },
            "exam_pattern": "Store and automatically rotate secrets/credentials = AWS Secrets Manager.",
        },
        "references": ["AWS Secrets Manager"],
    },
    {
        "id": "clf-sec-038", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants one place to aggregate and prioritize findings from services like "
                "GuardDuty, Inspector, and Macie. Which service provides this?",
        "options": [
            {"id": "A", "text": "AWS Artifact"},
            {"id": "B", "text": "AWS Security Hub"},
            {"id": "C", "text": "AWS KMS"},
            {"id": "D", "text": "Amazon CloudFront"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AWS Security Hub gives a centralized view that aggregates and prioritizes security findings from "
                       "multiple AWS services and partner tools.",
            "distractors": {
                "A": "AWS Artifact provides compliance documents, not aggregated security findings.",
                "C": "AWS KMS manages encryption keys.",
                "D": "Amazon CloudFront is a content delivery network.",
            },
            "exam_pattern": "A central dashboard aggregating security findings = AWS Security Hub.",
        },
        "references": ["AWS Security Hub"],
    },
    {
        "id": "clf-sec-039", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 1, "type": "mcq",
        "stem": "Protecting data with TLS/SSL as it travels between a client and an AWS service is an example of what?",
        "options": [
            {"id": "A", "text": "Encryption at rest"},
            {"id": "B", "text": "Encryption in transit"},
            {"id": "C", "text": "Data classification"},
            {"id": "D", "text": "Multi-factor authentication"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Encrypting data as it moves over the network using TLS/SSL is encryption in transit.",
            "distractors": {
                "A": "Encryption at rest protects data while it is stored, not while it moves.",
                "C": "Data classification labels data by sensitivity; it is not encryption.",
                "D": "Multi-factor authentication is an identity control, not encryption.",
            },
            "exam_pattern": "Data moving over the network protected by TLS = encryption in transit.",
        },
        "references": ["AWS Encryption (In Transit and At Rest)"],
    },
    {
        "id": "clf-sec-040", "exam": "clf", "domain": "security_compliance",
        "subtopic": "security_services", "difficulty": 2, "type": "mcq",
        "stem": "A company needs to provision and manage the SSL/TLS certificates that enable HTTPS on its "
                "load balancer. Which service helps with this?",
        "options": [
            {"id": "A", "text": "Amazon GuardDuty"},
            {"id": "B", "text": "AWS Secrets Manager"},
            {"id": "C", "text": "Amazon Macie"},
            {"id": "D", "text": "AWS Certificate Manager (ACM)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "AWS Certificate Manager (ACM) provisions, manages, and deploys SSL/TLS certificates for use with "
                       "AWS services such as load balancers.",
            "distractors": {
                "A": "Amazon GuardDuty is a threat-detection service.",
                "B": "AWS Secrets Manager stores application secrets, not public TLS certificates for load balancers.",
                "C": "Amazon Macie discovers sensitive data in S3.",
            },
            "exam_pattern": "Provision and manage SSL/TLS certificates = AWS Certificate Manager (ACM).",
        },
        "references": ["AWS Certificate Manager (ACM)"],
    },
]
