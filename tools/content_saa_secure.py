"""AWS Certified Solutions Architect - Associate (SAA-C03) pool.

Domain 1: Design Secure Architectures (saa_secure). Original, scenario-based
practice items for the four secure-design subtopics tracked in the engine:

  * saa_iam_access      - IAM users/roles/policies, least privilege, cross-account
                          roles and STS AssumeRole, IAM Identity Center (SSO), and
                          Service Control Policies (SCPs) as org guardrails.
  * saa_data_protection - encryption at rest (SSE-S3 vs SSE-KMS, KMS customer
                          managed keys), Secrets Manager vs Parameter Store, and
                          TLS certificates with ACM.
  * saa_network_security- security groups (stateful) vs network ACLs (stateless),
                          VPC endpoints / PrivateLink, and GuardDuty threat
                          detection.
  * saa_secure_workloads- AWS WAF, Shield Advanced, Amazon Inspector, Amazon
                          Macie, and Systems Manager Session Manager.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the answer authored here is not positionally
biased, every wrong option carries a distractor note, and each item names the
SAA-C03 exam-guide task statement it maps to. Items test durable "which design
BEST meets these requirements" judgement - not prices, region trivia, or any
real/memorized exam content.
"""

QUESTIONS = [
    # ===== saa_iam_access ===================================================
    {
        "id": "saa-sec-001", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_iam_access",
        "difficulty": 1, "type": "mcq",
        "stem": "An application running on EC2 instances must read objects from an S3 bucket. "
                "Following AWS security best practices, how should the application be granted access?",
        "options": [
            {"id": "A", "text": "Attach an IAM role (instance profile) to the EC2 instances with a policy allowing only the required S3 actions"},
            {"id": "B", "text": "Store an IAM user's long-term access keys in the application's configuration file"},
            {"id": "C", "text": "Embed the AWS account root user credentials in the application code"},
            {"id": "D", "text": "Make the S3 bucket public so no credentials are needed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IAM role attached via the instance profile supplies temporary, automatically "
                       "rotated credentials to the application, so there are no long-term keys to manage or leak.",
            "distractors": {
                "B": "Long-term access keys in a config file are a leak and rotation risk; roles are preferred for EC2.",
                "C": "Root user credentials must never be used by applications; they carry unrestricted privileges.",
                "D": "Making the bucket public exposes data to everyone and does not scope access to the app.",
            },
            "exam_pattern": "EC2 (or any AWS compute) needs AWS access -> attach an IAM role; never embed static keys.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (IAM roles)"],
    },
    {
        "id": "saa-sec-002", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_iam_access",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants an application in its production account to read a DynamoDB table in a "
                "separate security account, without creating any long-term credentials. Which approach BEST meets this?",
        "options": [
            {"id": "A", "text": "Create an IAM user in the security account and share its access keys with production"},
            {"id": "B", "text": "Enable a VPC peering connection between the two accounts"},
            {"id": "C", "text": "Create an IAM role in the security account that trusts the production account, and have the application assume it with STS"},
            {"id": "D", "text": "Make the DynamoDB table publicly accessible over the internet"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Cross-account access is granted with an IAM role in the resource account whose trust "
                       "policy allows the other account; the application calls sts:AssumeRole for temporary credentials.",
            "distractors": {
                "A": "Sharing long-term access keys across accounts is insecure and hard to rotate.",
                "B": "VPC peering is network connectivity; DynamoDB access is controlled by IAM, not peering.",
                "D": "Exposing the table publicly is a severe data exposure and is not how cross-account access works.",
            },
            "exam_pattern": "Cross-account access = IAM role in the target account + trust policy + STS AssumeRole.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (cross-account roles)"],
    },
    {
        "id": "saa-sec-003", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_iam_access",
        "difficulty": 2, "type": "mcq",
        "stem": "A security review finds many IAM policies that grant Action \"*\" on Resource \"*\". "
                "Which principle should the architect apply to remediate this?",
        "options": [
            {"id": "A", "text": "Grant broad permissions now and tighten them only after an incident occurs"},
            {"id": "B", "text": "Apply least privilege by scoping each policy to only the actions and resources required"},
            {"id": "C", "text": "Move all permissions to the AWS account root user"},
            {"id": "D", "text": "Replace the IAM policies with security group rules"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Least privilege means granting only the specific actions and resources a principal needs, "
                       "reducing blast radius if credentials are misused.",
            "distractors": {
                "A": "Reactive tightening leaves a wide exposure window; least privilege is applied proactively.",
                "C": "Concentrating permissions on the root user is the opposite of good practice.",
                "D": "Security groups filter network traffic; they do not replace IAM permission policies.",
            },
            "exam_pattern": "Over-broad */* policies -> apply least privilege (scope both actions and resources).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (least privilege)"],
    },
    {
        "id": "saa-sec-004", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_iam_access",
        "difficulty": 3, "type": "mcq",
        "stem": "An organization with dozens of AWS accounts under AWS Organizations wants workforce users "
                "to sign in once with their existing corporate directory and receive role-based access across "
                "accounts. Which service BEST meets this need?",
        "options": [
            {"id": "A", "text": "Create duplicate IAM users in every account"},
            {"id": "B", "text": "Issue a separate long-term access key for each user in each account"},
            {"id": "C", "text": "Use Amazon Cognito user pools for the workforce sign-in"},
            {"id": "D", "text": "Use AWS IAM Identity Center (successor to AWS SSO) with permission sets federated to the corporate directory"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "IAM Identity Center provides single sign-on with permission sets mapped to roles across "
                       "many accounts, federated to an external identity provider or directory.",
            "distractors": {
                "A": "Duplicating IAM users per account gives no single sign-on and is unmanageable at scale.",
                "B": "Per-account access keys are long-term credentials and provide no SSO.",
                "C": "Cognito is for application/customer (B2C) identity, not workforce SSO across AWS accounts.",
            },
            "exam_pattern": "Workforce SSO + role-based access across many accounts = IAM Identity Center + permission sets.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (IAM Identity Center)"],
    },
    {
        "id": "saa-sec-005", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_iam_access",
        "difficulty": 3, "type": "multi",
        "stem": "A platform team wants to use Service Control Policies (SCPs) in AWS Organizations as "
                "organization-wide guardrails. Which TWO statements about SCPs are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "SCPs set the maximum available permissions for accounts but do not themselves grant any permissions"},
            {"id": "B", "text": "SCPs grant permissions directly to IAM users and roles"},
            {"id": "C", "text": "SCPs can be attached to an organizational unit (OU) or an account to restrict what IAM principals in it can do"},
            {"id": "D", "text": "SCPs remove the need for identity-based IAM policies on users and roles"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "SCPs act as a permission ceiling: they define the maximum permissions available to an "
                       "OU or account, but actual access still requires identity-based IAM policies.",
            "distractors": {
                "B": "SCPs never grant permissions; they only bound the maximum that IAM policies can allow.",
                "D": "Because SCPs only set the ceiling, identity-based IAM policies are still required to grant access.",
            },
            "exam_pattern": "SCP = org/OU/account guardrail (permission ceiling); grants nothing, still need IAM policies.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (SCPs / Organizations)"],
    },

    # ===== saa_data_protection ==============================================
    {
        "id": "saa-sec-006", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_data_protection",
        "difficulty": 2, "type": "mcq",
        "stem": "A company must encrypt S3 objects at rest and needs an auditable record of every time the "
                "encryption key is used, plus control over key rotation and key access policies. Which option BEST fits?",
        "options": [
            {"id": "A", "text": "SSE-S3 with Amazon S3-managed keys"},
            {"id": "B", "text": "No encryption, relying on bucket policies only"},
            {"id": "C", "text": "Client-side hashing of the object names"},
            {"id": "D", "text": "SSE-KMS using an AWS KMS customer managed key"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SSE-KMS with a customer managed key gives key policies, rotation control, and a CloudTrail "
                       "audit trail of key usage - the control and auditability the scenario requires.",
            "distractors": {
                "A": "SSE-S3 encrypts at rest but gives no key policies, no rotation control, and no per-request key-usage audit.",
                "B": "Bucket policies control access, not encryption at rest.",
                "C": "Hashing object names does not encrypt object contents.",
            },
            "exam_pattern": "Need key control + usage audit -> SSE-KMS (customer managed key); plain at-rest -> SSE-S3.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (encryption at rest)"],
    },
    {
        "id": "saa-sec-007", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_data_protection",
        "difficulty": 2, "type": "mcq",
        "stem": "An application must store database credentials and automatically rotate them on a schedule, "
                "with built-in rotation integration for Amazon RDS. Which service is purpose-built for this?",
        "options": [
            {"id": "A", "text": "An S3 bucket secured with an object ACL"},
            {"id": "B", "text": "AWS Secrets Manager"},
            {"id": "C", "text": "Plaintext environment variables on the instance"},
            {"id": "D", "text": "Amazon CloudWatch Logs"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Secrets Manager stores secrets encrypted and provides built-in automatic rotation, including "
                       "native integration for RDS credentials.",
            "distractors": {
                "A": "Storing secrets in S3 is not purpose-built and lacks managed rotation.",
                "C": "Plaintext environment variables are neither encrypted nor rotated and are easily leaked.",
                "D": "CloudWatch Logs stores log data, not secrets.",
            },
            "exam_pattern": "Managed secret storage with built-in automatic rotation (esp. RDS) = Secrets Manager "
                            "(Parameter Store SecureString stores secrets but has no built-in rotation).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (secrets)"],
    },
    {
        "id": "saa-sec-008", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_data_protection",
        "difficulty": 2, "type": "mcq",
        "stem": "A company wants to serve its web application over HTTPS behind an Application Load Balancer and "
                "avoid manually renewing TLS certificates. Which service provides free public certificates with "
                "automatic renewal that integrate with the ALB?",
        "options": [
            {"id": "A", "text": "AWS Certificate Manager (ACM)"},
            {"id": "B", "text": "AWS KMS"},
            {"id": "C", "text": "AWS Secrets Manager"},
            {"id": "D", "text": "Amazon Route 53"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ACM issues free public TLS certificates, renews them automatically, and integrates with "
                       "ELB, CloudFront, and API Gateway.",
            "distractors": {
                "B": "KMS manages encryption keys, not public TLS certificates.",
                "C": "Secrets Manager stores secrets, not managed public TLS certificates for load balancers.",
                "D": "Route 53 is DNS; it does not issue or renew TLS certificates.",
            },
            "exam_pattern": "Public TLS certs with auto-renewal on ELB/CloudFront/API Gateway = ACM.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (TLS/ACM)"],
    },
    {
        "id": "saa-sec-009", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_data_protection",
        "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The AWS service used to create and control cryptographic keys (including "
                "customer managed keys) that encrypt data across services such as S3, EBS, and RDS is AWS ___ "
                "(three-letter acronym).",
        "correct": ["kms", "aws kms", "key management service"],
        "explanation": {
            "correct": "AWS KMS (Key Management Service) creates and manages encryption keys and integrates with "
                       "most AWS services for envelope encryption of data at rest.",
            "distractors": {},
            "exam_pattern": "Central creation/control of encryption keys across AWS services = AWS KMS.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (KMS)"],
    },
    {
        "id": "saa-sec-010", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_data_protection",
        "difficulty": 3, "type": "mcq",
        "stem": "A team has an existing unencrypted Amazon RDS database and must make its data encrypted at rest "
                "to meet a new compliance rule. Which approach achieves this?",
        "options": [
            {"id": "A", "text": "Toggle an \"encrypt\" setting on the running instance to encrypt it in place"},
            {"id": "B", "text": "Enable SSE-S3 on the RDS instance"},
            {"id": "C", "text": "Take a snapshot, copy the snapshot with encryption enabled (using a KMS key), and restore a new encrypted instance from it"},
            {"id": "D", "text": "Attach an AWS WAF web ACL to the database"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RDS encryption at rest is set at creation. To encrypt existing unencrypted data you snapshot "
                       "it, copy the snapshot with encryption enabled, and restore a new encrypted instance.",
            "distractors": {
                "A": "You cannot enable at-rest encryption in place on an already-unencrypted RDS instance.",
                "B": "SSE-S3 is an S3 feature and does not apply to RDS storage encryption.",
                "D": "WAF filters layer-7 web traffic and has nothing to do with encrypting data at rest.",
            },
            "exam_pattern": "Encrypt an existing unencrypted RDS/EBS resource = snapshot -> copy with encryption -> restore/create new.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (RDS encryption)"],
    },

    # ===== saa_network_security =============================================
    {
        "id": "saa-sec-011", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_network_security",
        "difficulty": 1, "type": "mcq",
        "stem": "An architect allows inbound HTTPS to EC2 instances with a security group. Return traffic for "
                "those established connections is automatically permitted without an explicit outbound rule. "
                "Which property explains this?",
        "options": [
            {"id": "A", "text": "Security groups are stateless"},
            {"id": "B", "text": "Security groups are stateful"},
            {"id": "C", "text": "Security groups evaluate rules in numbered order"},
            {"id": "D", "text": "Security groups deny all return traffic by default"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Security groups are stateful: if inbound traffic is allowed, the corresponding return "
                       "traffic is permitted automatically regardless of outbound rules.",
            "distractors": {
                "A": "Stateless describes network ACLs, which require explicit rules for return traffic.",
                "C": "Numbered, ordered rule evaluation describes NACLs; security groups evaluate all rules together.",
                "D": "Being stateful, security groups permit (not deny) return traffic for allowed connections.",
            },
            "exam_pattern": "Security groups = stateful (return traffic auto-allowed); NACLs = stateless (need explicit return rules).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (security groups)"],
    },
    {
        "id": "saa-sec-012", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_network_security",
        "difficulty": 2, "type": "mcq",
        "stem": "A company must explicitly block a single malicious IP address from reaching all instances in a "
                "subnet. Security groups cannot express this. Which control should be used?",
        "options": [
            {"id": "A", "text": "An IAM policy deny statement"},
            {"id": "B", "text": "A security group deny rule"},
            {"id": "C", "text": "A KMS key policy"},
            {"id": "D", "text": "A network ACL (NACL) deny rule on the subnet"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Network ACLs operate at the subnet level and support explicit deny rules, so they can block "
                       "a specific source IP for the whole subnet.",
            "distractors": {
                "A": "IAM controls API permissions, not packet filtering by source IP.",
                "B": "Security groups support allow rules only; they cannot express an explicit deny.",
                "C": "KMS key policies govern key usage, not network traffic.",
            },
            "exam_pattern": "Need an explicit deny / block an IP at the subnet level -> NACL (security groups can't deny).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (network ACLs)"],
    },
    {
        "id": "saa-sec-013", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_network_security",
        "difficulty": 3, "type": "multi",
        "stem": "An architect is contrasting security groups and network ACLs. Which TWO statements are correct? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "A security group operates at the instance (ENI) level, while a network ACL operates at the subnet level"},
            {"id": "B", "text": "Security groups support allow rules only, while network ACLs support both allow and deny rules"},
            {"id": "C", "text": "Security groups are stateless and network ACLs are stateful"},
            {"id": "D", "text": "Network ACLs can reference other security groups as a traffic source"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Security groups attach to the instance/ENI and allow only; NACLs sit at the subnet boundary "
                       "and support both allow and deny rules.",
            "distractors": {
                "C": "Reversed - security groups are stateful and NACLs are stateless.",
                "D": "NACLs match on CIDR ranges, not security group references; security groups can reference other security groups.",
            },
            "exam_pattern": "SG = instance-level, stateful, allow-only, can reference SGs; NACL = subnet-level, stateless, allow+deny, CIDR-based.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (SG vs NACL)"],
    },
    {
        "id": "saa-sec-014", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_network_security",
        "difficulty": 2, "type": "mcq",
        "stem": "A workload in a private subnet must call the Amazon SQS API without sending traffic over the "
                "public internet or through a NAT gateway. Which solution BEST meets this requirement?",
        "options": [
            {"id": "A", "text": "An internet gateway attached to the private subnet"},
            {"id": "B", "text": "A public IP address on each instance"},
            {"id": "C", "text": "An interface VPC endpoint (AWS PrivateLink) for SQS"},
            {"id": "D", "text": "An AWS WAF web ACL"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An interface VPC endpoint (PrivateLink) gives private connectivity to the SQS API from within "
                       "the VPC, so traffic never traverses the internet or a NAT gateway.",
            "distractors": {
                "A": "An internet gateway routes traffic over the public internet - the opposite of the requirement.",
                "B": "Public IPs send traffic over the internet.",
                "D": "WAF inspects inbound web requests; it does not provide private connectivity to an AWS service.",
            },
            "exam_pattern": "Reach an AWS service privately (no internet/NAT) -> VPC endpoint: interface/PrivateLink, or gateway endpoint for S3 & DynamoDB.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure access to AWS resources (VPC endpoints/PrivateLink)"],
    },
    {
        "id": "saa-sec-015", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_network_security",
        "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The AWS managed threat-detection service that continuously analyzes CloudTrail "
                "events, VPC Flow Logs, and DNS logs to identify malicious or unauthorized activity is Amazon ________.",
        "correct": ["guardduty", "guard duty", "amazon guardduty"],
        "explanation": {
            "correct": "Amazon GuardDuty is a managed threat-detection service that analyzes CloudTrail, VPC Flow "
                       "Logs, and DNS logs to surface suspicious or unauthorized behavior.",
            "distractors": {},
            "exam_pattern": "Continuous, log-based threat detection = GuardDuty (findings, not inline blocking).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure workloads and applications (GuardDuty)"],
    },

    # ===== saa_secure_workloads =============================================
    {
        "id": "saa-sec-016", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_secure_workloads",
        "difficulty": 2, "type": "mcq",
        "stem": "A public web application behind an Application Load Balancer is receiving SQL injection and "
                "cross-site scripting attempts. Which service can inspect HTTP(S) requests and block these "
                "layer-7 attacks?",
        "options": [
            {"id": "A", "text": "AWS WAF with a web ACL"},
            {"id": "B", "text": "Amazon GuardDuty"},
            {"id": "C", "text": "A network ACL"},
            {"id": "D", "text": "AWS Shield Standard only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AWS WAF inspects HTTP(S) requests and can block layer-7 exploits such as SQL injection and "
                       "XSS, and apply rate-based rules, on ALB, CloudFront, and API Gateway.",
            "distractors": {
                "B": "GuardDuty detects and reports threats from logs but does not inline-block web requests.",
                "C": "NACLs filter by IP/port at layers 3/4 and cannot parse HTTP payloads for SQLi/XSS.",
                "D": "Shield Standard mitigates common layer 3/4 DDoS, not application-layer injection.",
            },
            "exam_pattern": "Block layer-7 web exploits (SQLi/XSS, rate limiting) = AWS WAF (on ALB/CloudFront/API Gateway).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure workloads and applications (WAF)"],
    },
    {
        "id": "saa-sec-017", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_secure_workloads",
        "difficulty": 2, "type": "mcq",
        "stem": "A company running a high-profile application needs enhanced protection and 24/7 support against "
                "large, sophisticated DDoS attacks, plus cost protection for scaling triggered during an attack. "
                "Which service should it use?",
        "options": [
            {"id": "A", "text": "AWS Config"},
            {"id": "B", "text": "Amazon Inspector"},
            {"id": "C", "text": "AWS Trusted Advisor"},
            {"id": "D", "text": "AWS Shield Advanced"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Shield Advanced adds enhanced DDoS protections, access to the response team, and cost "
                       "protection for usage spikes caused by an attack (Shield Standard protects layers 3/4 automatically).",
            "distractors": {
                "A": "Config records and evaluates resource configuration compliance, not DDoS mitigation.",
                "B": "Inspector scans workloads for software vulnerabilities, not DDoS.",
                "C": "Trusted Advisor gives best-practice recommendations, not active DDoS defense.",
            },
            "exam_pattern": "Advanced DDoS protection + response team + cost protection = Shield Advanced.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure workloads and applications (Shield)"],
    },
    {
        "id": "saa-sec-018", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_secure_workloads",
        "difficulty": 2, "type": "mcq",
        "stem": "A security team wants automated, continuous scanning of EC2 instances and container images in "
                "Amazon ECR for software vulnerabilities (CVEs) and unintended network exposure. Which service is "
                "purpose-built for this?",
        "options": [
            {"id": "A", "text": "Amazon Macie"},
            {"id": "B", "text": "Amazon Inspector"},
            {"id": "C", "text": "AWS CloudTrail"},
            {"id": "D", "text": "Amazon SNS"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Amazon Inspector continuously scans EC2 instances and ECR container images for known CVEs and "
                       "unintended network reachability.",
            "distractors": {
                "A": "Macie discovers and protects sensitive data (e.g., PII) in S3, not software CVEs.",
                "C": "CloudTrail records API activity for audit; it does not scan for vulnerabilities.",
                "D": "SNS is a messaging/notification service.",
            },
            "exam_pattern": "Automated CVE/vulnerability scanning of EC2 & container images = Amazon Inspector.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure workloads and applications (Inspector)"],
    },
    {
        "id": "saa-sec-019", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_secure_workloads",
        "difficulty": 1, "type": "mcq",
        "stem": "A company must automatically discover and classify sensitive data such as personally identifiable "
                "information (PII) stored in its S3 buckets. Which service is designed for this?",
        "options": [
            {"id": "A", "text": "AWS WAF"},
            {"id": "B", "text": "Amazon GuardDuty"},
            {"id": "C", "text": "Amazon Macie"},
            {"id": "D", "text": "AWS KMS"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Amazon Macie uses machine learning to discover, classify, and protect sensitive data such "
                       "as PII in S3.",
            "distractors": {
                "A": "WAF filters web requests; it does not classify stored data.",
                "B": "GuardDuty detects threats from logs; it does not classify S3 object contents as PII.",
                "D": "KMS manages encryption keys; it does not discover or classify data.",
            },
            "exam_pattern": "Discover/classify sensitive data (PII) in S3 = Amazon Macie.",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Determine appropriate data security controls (Macie)"],
    },
    {
        "id": "saa-sec-020", "exam": "saa",
        "domain": "saa_secure", "subtopic": "saa_secure_workloads",
        "difficulty": 3, "type": "mcq",
        "stem": "An operations team needs shell access to EC2 instances in private subnets for administration, but "
                "security policy forbids opening inbound SSH (port 22) or assigning public IPs. Which solution BEST "
                "meets these requirements?",
        "options": [
            {"id": "A", "text": "AWS Systems Manager Session Manager"},
            {"id": "B", "text": "Open port 22 to 0.0.0.0/0 in the security group"},
            {"id": "C", "text": "Assign an Elastic IP to each instance and allow SSH"},
            {"id": "D", "text": "Place the instances in a public subnet with an internet gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session Manager provides browser/CLI shell access through the SSM agent and IAM, needing no "
                       "open inbound ports, no bastion host, and no public IPs.",
            "distractors": {
                "B": "Opening SSH to the world is exactly what the policy forbids and is high-risk.",
                "C": "Assigning public IPs and allowing SSH violates the no-public-IP and no-inbound-SSH requirements.",
                "D": "Moving instances to a public subnet exposes them, contrary to the requirement.",
            },
            "exam_pattern": "Admin shell access with no inbound ports/public IP = SSM Session Manager (SSM agent + IAM).",
        },
        "references": ["AWS SAA-C03 Exam Guide: Domain 1 - Design secure workloads and applications (Session Manager)"],
    },
]
