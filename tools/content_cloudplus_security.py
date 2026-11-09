"""CompTIA Cloud+ (CV0-004) pool - Domain 4: Security.

Original, objective-aligned practice items for the four Security subtopics
tracked in CertLab:
  * cloudp_identity_access       - least privilege, RBAC, MFA, SSO, federation.
  * cloudp_data_security         - encryption in transit (TLS) and at rest, key
                                   management (KMS/HSM), tokenization.
  * cloudp_network_security      - WAF, zero trust, micro-segmentation, security
                                   groups / stateful virtual firewalls.
  * cloudp_compliance_hardening  - CIS Benchmarks, vulnerability management,
                                   standards/regulations, system hardening.

Cloud+ is vendor-NEUTRAL: a vendor is named only as an example, never as the sole
key. build_content.py shuffles option order (seeded by id), so no key is positionally
biased; every wrong option carries a distractor note, and each item cites the public
CV0-004 objective domain it draws on. Original items only, never real exam content.
"""

QUESTIONS = [
    # ===== cloudp_identity_access ===========================================
    {
        "id": "cloudplus-sec-001", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 1, "type": "mcq",
        "stem": "A policy grants each user only the permissions required to do their job and nothing more. Which "
                "security principle is being applied?",
        "options": [
            {"id": "A", "text": "Least privilege"},
            {"id": "B", "text": "Defense in depth"},
            {"id": "C", "text": "Security through obscurity"},
            {"id": "D", "text": "Separation of media"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Least privilege grants the minimum permissions necessary for a role or task, limiting the damage from "
                       "compromised or misused accounts.",
            "distractors": {
                "B": "Defense in depth layers multiple controls; it is a broader strategy, not specifically minimal permissions.",
                "C": "Security through obscurity relies on secrecy of design and is not the principle described.",
                "D": "'Separation of media' is not a standard access-control principle.",
            },
            "exam_pattern": "Minimum permissions needed for the job = least privilege.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (least privilege)"],
    },
    {
        "id": "cloudplus-sec-002", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 2, "type": "mcq",
        "stem": "Instead of assigning permissions to each user individually, administrators grant permissions to roles "
                "such as 'billing-admin' or 'read-only-auditor' and then assign users to those roles. Which "
                "access-control model is this?",
        "options": [
            {"id": "A", "text": "Mandatory access control (MAC)"},
            {"id": "B", "text": "Discretionary access control (DAC)"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "Rule-based packet filtering"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RBAC assigns permissions to roles and then places users into roles, simplifying administration and "
                       "consistently enforcing least privilege at scale.",
            "distractors": {
                "A": "MAC enforces access via system-wide labels/clearances set by policy, not job-function roles administrators define.",
                "B": "DAC lets resource owners grant access at their discretion; it is not the role-to-permission model described.",
                "D": "Rule-based packet filtering is a firewall concept, not an identity access-control model.",
            },
            "exam_pattern": "Permissions attached to roles, users placed in roles = RBAC.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (RBAC)"],
    },
    {
        "id": "cloudplus-sec-003", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 2, "type": "mcq",
        "stem": "To strengthen sign-in, a provider requires a password plus a one-time code from the user's phone app. "
                "Which control is this, and which principle does it embody?",
        "options": [
            {"id": "A", "text": "Single sign-on; it reduces the number of credentials"},
            {"id": "B", "text": "Multi-factor authentication; it combines something you know with something you have"},
            {"id": "C", "text": "Federation; it trusts an external identity provider"},
            {"id": "D", "text": "Tokenization; it substitutes sensitive data with tokens"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Requiring two different factor types — a password (something you know) plus a phone-generated code "
                       "(something you have) — is multi-factor authentication, which greatly reduces the risk from stolen passwords.",
            "distractors": {
                "A": "Single sign-on lets one authentication cover many apps; it is not the use of two factors.",
                "C": "Federation establishes trust with an external identity provider; it is not inherently two-factor.",
                "D": "Tokenization is a data-protection method, not an authentication-factor scheme.",
            },
            "exam_pattern": "Two different factor types (know/have/are) = MFA.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (MFA)"],
    },
    {
        "id": "cloudplus-sec-004", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_identity_access", "difficulty": 2, "type": "multi",
        "stem": "A company lets employees authenticate once at the corporate identity provider and then reach many "
                "external SaaS apps without re-entering credentials, using SAML/OIDC assertions the apps trust. Which "
                "TWO capabilities make this possible? (Choose two.)",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO)"},
            {"id": "B", "text": "Federated identity (trust via SAML/OIDC)"},
            {"id": "C", "text": "Network address translation (NAT)"},
            {"id": "D", "text": "RAID mirroring"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "SSO lets one authentication cover many applications; federated identity extends that trust to external "
                       "organizations/apps using standards like SAML or OIDC, so they accept the home IdP's assertions.",
            "distractors": {
                "C": "NAT translates network addresses; it has nothing to do with authenticating across apps.",
                "D": "RAID mirroring is disk redundancy, unrelated to identity federation.",
            },
            "exam_pattern": "One login across many apps = SSO; trust across orgs via SAML/OIDC = federation.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Identity and access (SSO/federation)"],
    },

    # ===== cloudp_data_security =============================================
    {
        "id": "cloudplus-sec-005", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 1, "type": "fill",
        "stem": "Fill in the acronym: Data in transit between a browser and a web application is most commonly "
                "protected by the ____ protocol, the successor to SSL (provide the three-letter acronym).",
        "correct": ["tls", "transport layer security"],
        "explanation": {
            "correct": "TLS (Transport Layer Security), the successor to SSL, encrypts data in transit between endpoints, "
                       "providing confidentiality and integrity for network traffic such as HTTPS.",
            "distractors": {},
            "exam_pattern": "Encrypt data in transit on the web = TLS (HTTPS); SSL is its deprecated predecessor.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (encryption in transit/TLS)"],
    },
    {
        "id": "cloudplus-sec-006", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A compliance rule requires that stored database files be unreadable if someone steals the physical "
                "disks or copies the raw volume. Which control satisfies this?",
        "options": [
            {"id": "A", "text": "A load balancer"},
            {"id": "B", "text": "Horizontal scaling"},
            {"id": "C", "text": "Encryption at rest"},
            {"id": "D", "text": "A CDN"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Encryption at rest encrypts stored data so that raw disks, volumes, or backup files are unreadable "
                       "without the keys, protecting against theft of the underlying media.",
            "distractors": {
                "A": "A load balancer distributes traffic and has no role in protecting stored data.",
                "B": "Horizontal scaling adds capacity; it does not render stored data unreadable.",
                "D": "A CDN caches content near users; it does not encrypt the database's stored files.",
            },
            "exam_pattern": "Make stored data unreadable without keys = encryption at rest.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (encryption at rest)"],
    },
    {
        "id": "cloudplus-sec-007", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants centralized creation, rotation, storage, and access control of its encryption "
                "keys, ideally backed by hardware security modules. Which service provides this?",
        "options": [
            {"id": "A", "text": "A WAF"},
            {"id": "B", "text": "A key management service (KMS)"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "A reverse proxy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A key management service centrally generates, stores, rotates, and controls access to cryptographic "
                       "keys — often HSM-backed — so applications encrypt/decrypt without exposing raw key material.",
            "distractors": {
                "A": "A WAF filters web application attacks; it does not manage encryption keys.",
                "C": "A SIEM correlates security events; it is not a key-lifecycle manager.",
                "D": "A reverse proxy forwards client requests to backends; it is not a key management system.",
            },
            "exam_pattern": "Central key generation/rotation/storage/access, HSM-backed = KMS.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (key management)"],
    },
    {
        "id": "cloudplus-sec-008", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A payment system replaces each credit-card number with a non-sensitive surrogate value that has no "
                "mathematical relationship to the original, so the real number is never stored in the application "
                "database. Which technique is this?",
        "options": [
            {"id": "A", "text": "Tokenization"},
            {"id": "B", "text": "Compression"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "Striping"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tokenization substitutes sensitive data with a non-sensitive token that maps back to the original only "
                       "inside a secure token vault, keeping real card data out of the application and reducing compliance scope.",
            "distractors": {
                "B": "Compression reduces data size; it does not protect or substitute sensitive values.",
                "C": "Load balancing distributes traffic; it is unrelated to protecting card numbers.",
                "D": "Striping spreads data across disks for performance; it is not a data-protection substitution method.",
            },
            "exam_pattern": "Replace a sensitive value with an unrelated surrogate held in a vault = tokenization.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Data security (tokenization)"],
    },

    # ===== cloudp_network_security ==========================================
    {
        "id": "cloudplus-sec-009", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "A web application is being hit with SQL injection and cross-site scripting attempts. Which control is "
                "specifically designed to inspect HTTP requests and block these application-layer attacks?",
        "options": [
            {"id": "A", "text": "A network ACL at Layer 3"},
            {"id": "B", "text": "A NAT gateway"},
            {"id": "C", "text": "A load-balancer health check"},
            {"id": "D", "text": "A Web Application Firewall (WAF)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A WAF inspects Layer 7 HTTP/S traffic and blocks application-layer attacks such as SQL injection and "
                       "XSS using signatures and rules, protecting the app where a network firewall cannot see.",
            "distractors": {
                "A": "A Layer 3 network ACL filters by IP/port and cannot parse HTTP payloads to catch SQL injection or XSS.",
                "B": "A NAT gateway translates addresses for outbound traffic; it provides no application-layer filtering.",
                "C": "A health check tests backend availability; it does not inspect request content for attacks.",
            },
            "exam_pattern": "Block SQLi/XSS by inspecting HTTP = WAF (Layer 7).",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (WAF)"],
    },
    {
        "id": "cloudplus-sec-010", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "A security model assumes no user or device is trusted by default — even inside the network — and "
                "verifies identity and device posture on every request. What is this model called?",
        "options": [
            {"id": "A", "text": "Perimeter-only (castle-and-moat) security"},
            {"id": "B", "text": "Zero trust"},
            {"id": "C", "text": "Security through obscurity"},
            {"id": "D", "text": "Open trust"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Zero trust removes implicit trust based on network location and continuously authenticates and "
                       "authorizes every request ('never trust, always verify'), using identity, device posture, and least privilege.",
            "distractors": {
                "A": "Castle-and-moat trusts whatever is inside the perimeter — the exact assumption zero trust rejects.",
                "C": "Security through obscurity hides design details; it is not the continuous-verification model described.",
                "D": "'Open trust' is not a recognized model and contradicts the scenario.",
            },
            "exam_pattern": "Never trust, always verify; no implicit trust by location = zero trust.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (zero trust)"],
    },
    {
        "id": "cloudplus-sec-011", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 3, "type": "mcq",
        "stem": "In a virtualized data center, an administrator applies fine-grained security policies between "
                "individual workloads — even those on the same subnet — so a compromised VM cannot freely talk to its "
                "neighbors. What is this called?",
        "options": [
            {"id": "A", "text": "Network address translation"},
            {"id": "B", "text": "Perimeter firewalling"},
            {"id": "C", "text": "Micro-segmentation"},
            {"id": "D", "text": "Port mirroring"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Micro-segmentation enforces granular, workload-to-workload policies (often identity- or tag-based) "
                       "inside the data center, limiting east-west/lateral movement even within the same subnet.",
            "distractors": {
                "A": "NAT rewrites addresses; it does not enforce per-workload security policy.",
                "B": "A perimeter firewall controls north-south traffic at the edge, not fine-grained traffic between peers on the same subnet.",
                "D": "Port mirroring copies traffic for monitoring; it does not restrict workload-to-workload communication.",
            },
            "exam_pattern": "Granular per-workload policy limiting east-west/lateral movement = micro-segmentation.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (micro-segmentation)"],
    },
    {
        "id": "cloudplus-sec-012", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_network_security", "difficulty": 2, "type": "mcq",
        "stem": "In an IaaS deployment, which construct acts as a stateful virtual firewall attached to instances, "
                "allowing only specified inbound/outbound traffic by port, protocol, and source?",
        "options": [
            {"id": "A", "text": "A security group"},
            {"id": "B", "text": "A CDN edge node"},
            {"id": "C", "text": "A snapshot policy"},
            {"id": "D", "text": "A golden image"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A security group is a stateful, instance-level virtual firewall that permits only the inbound/outbound "
                       "traffic you define (by port, protocol, and source/destination); return traffic is automatically allowed.",
            "distractors": {
                "B": "A CDN edge node caches content; it is not an instance firewall.",
                "C": "A snapshot policy schedules point-in-time backups; it has no traffic-filtering role.",
                "D": "A golden image is a deployment baseline, not a traffic filter.",
            },
            "exam_pattern": "Stateful instance-level virtual firewall by port/protocol/source = security group.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Network security (security groups/firewalls)"],
    },

    # ===== cloudp_compliance_hardening ======================================
    {
        "id": "cloudplus-sec-013", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Before deploying servers, a team applies a widely recognized set of prescriptive configuration "
                "recommendations to reduce attack surface by disabling unneeded services and enforcing secure settings. "
                "Which resource are they most likely following?",
        "options": [
            {"id": "A", "text": "An RFC 1918 address plan"},
            {"id": "B", "text": "CIS Benchmarks"},
            {"id": "C", "text": "A load-balancing algorithm"},
            {"id": "D", "text": "A RAID configuration guide"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "CIS Benchmarks are consensus-based, prescriptive hardening guides for operating systems, cloud "
                       "services, and applications that reduce attack surface via secure baseline settings.",
            "distractors": {
                "A": "RFC 1918 defines private IP ranges; it is not a security hardening standard.",
                "C": "A load-balancing algorithm distributes traffic; it is unrelated to OS hardening.",
                "D": "A RAID guide concerns disk redundancy, not secure configuration baselines.",
            },
            "exam_pattern": "Prescriptive secure-configuration baselines to harden systems = CIS Benchmarks.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Hardening (CIS Benchmarks)"],
    },
    {
        "id": "cloudplus-sec-014", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A team regularly scans its cloud systems for known weaknesses, ranks the findings by severity (e.g., "
                "CVSS), and schedules remediation. This ongoing cycle is best described as:",
        "options": [
            {"id": "A", "text": "Penetration testing"},
            {"id": "B", "text": "Tokenization"},
            {"id": "C", "text": "Vulnerability management"},
            {"id": "D", "text": "Load testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Vulnerability management is the continuous cycle of discovering, assessing/prioritizing (often by CVSS), "
                       "remediating, and verifying weaknesses across systems.",
            "distractors": {
                "A": "Penetration testing is a point-in-time simulated attack, not the continuous scan-prioritize-remediate cycle.",
                "B": "Tokenization protects sensitive data; it is not vulnerability discovery and remediation.",
                "D": "Load testing measures performance under load, not security weaknesses.",
            },
            "exam_pattern": "Continuous scan -> prioritize (CVSS) -> remediate -> verify = vulnerability management.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance/hardening (vulnerability management)"],
    },
    {
        "id": "cloudplus-sec-015", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "mcq",
        "stem": "An auditor asks a company to prove that its payment-processing environment meets an external standard "
                "that governs the handling of cardholder data. Which standard is this?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "RAID 6"},
            {"id": "C", "text": "TLS 1.3"},
            {"id": "D", "text": "NTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PCI DSS (Payment Card Industry Data Security Standard) prescribes controls for organizations that store, "
                       "process, or transmit cardholder data; compliance is demonstrated through assessments and evidence.",
            "distractors": {
                "B": "RAID 6 is a disk-redundancy level, not a compliance standard for card data.",
                "C": "TLS 1.3 is an encryption protocol that may help meet a standard but is not itself the cardholder-data standard.",
                "D": "NTP is a time-synchronization protocol, not a compliance framework.",
            },
            "exam_pattern": "Cardholder-data handling standard = PCI DSS; map the regulation/standard to the data it governs.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Compliance (standards/regulations)"],
    },
    {
        "id": "cloudplus-sec-016", "exam": "cloudplus", "domain": "cloudp_security",
        "subtopic": "cloudp_compliance_hardening", "difficulty": 2, "type": "fill",
        "stem": "Fill in the term: The process of reducing a system's attack surface by removing unnecessary services, "
                "closing unused ports, applying secure settings, and patching is called system ____ (one word).",
        "correct": ["hardening", "system hardening"],
        "explanation": {
            "correct": "Hardening reduces attack surface by disabling or removing unneeded components, enforcing secure "
                       "configuration baselines, closing unused ports, and keeping systems patched.",
            "distractors": {},
            "exam_pattern": "Shrink attack surface via secure baselines/removing unneeded services = hardening.",
        },
        "references": ["CompTIA Cloud+ CV0-004 Objectives: Domain 4 — Hardening"],
    },
]
