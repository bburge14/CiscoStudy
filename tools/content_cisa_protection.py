"""ISACA CISA pool - Domain 5: Protection of Information Assets.

Original, objective-aligned practice items for the six Domain 5 subtopics
tracked in the study engine:
  * cisa_access_controls    - IAAA (identification/authentication/authorization/
                              accountability), least privilege, access reviews/
                              recertification, multi-factor authentication.
  * cisa_network_security   - firewall types (stateful inspection), IDS vs. IPS,
                              VPN/IPsec for data in transit.
  * cisa_data_classification - purpose of classification, data-owner
                              responsibility, aligning protection to sensitivity.
  * cisa_encryption_pki      - symmetric vs. asymmetric cryptography, digital
                              signatures, PKI and the certificate authority.
  * cisa_security_monitoring - log/evidence integrity, SIEM correlation,
                              monitoring as a detective control.
  * cisa_physical_environmental - fire suppression, UPS/power, mantraps and
                              physical entry controls.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's safeguards-assurance mindset. All items are ORIGINAL and aligned to
public exam objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cisa_access_controls =============================================
    {
        "id": "cisa-prot-001", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: In access control, the process of verifying that a user is who they "
                "claim to be - for example by checking a password or biometric - is called ______.",
        "correct": ["authentication"],
        "explanation": {
            "correct": "Authentication verifies a claimed identity (something you know, have, or are); it "
                       "follows identification and precedes authorization and accountability.",
            "distractors": {},
            "exam_pattern": "Identify (claim) -> Authenticate (prove) -> Authorize (permit) -> Account (log).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Identification and authentication (IAAA)"],
    },
    {
        "id": "cisa-prot-002", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 1, "type": "mcq",
        "stem": "A policy states that each user should be granted only the access rights strictly "
                "necessary to perform their job duties. This BEST describes which principle?",
        "options": [
            {"id": "A", "text": "Defense in depth"},
            {"id": "B", "text": "Separation of duties"},
            {"id": "C", "text": "Least privilege"},
            {"id": "D", "text": "Implicit allow"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Least privilege grants users only the minimum access needed for their job, limiting the "
                       "damage from error, misuse, or compromise.",
            "distractors": {
                "A": "Defense in depth layers multiple controls; it is not about minimal rights per user.",
                "B": "Separation of duties splits a task among people to prevent fraud - related but different.",
                "D": "Implicit allow (permitting anything not explicitly denied) is the opposite of least privilege.",
            },
            "exam_pattern": "Minimum access needed to do the job = least privilege.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Least privilege and need-to-know"],
    },
    {
        "id": "cisa-prot-003", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 2, "type": "mcq",
        "stem": "An IS auditor finds that user access rights are never reviewed after they are first "
                "granted. What is the GREATEST risk?",
        "options": [
            {"id": "A", "text": "Users will forget their passwords"},
            {"id": "B", "text": "Users accumulate excessive or inappropriate access over time (privilege creep), including access from former roles"},
            {"id": "C", "text": "The network will run more slowly"},
            {"id": "D", "text": "Backups will fail"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Without periodic access reviews/recertification, users keep access from prior roles and "
                       "transfers, accumulating excessive privileges (privilege creep), and terminated users' access "
                       "may never be removed.",
            "distractors": {
                "A": "Forgotten passwords are a help-desk matter unrelated to access reviews.",
                "C": "Access reviews do not affect network speed.",
                "D": "Backup success is unrelated to access recertification.",
            },
            "exam_pattern": "No periodic access review -> privilege creep and lingering access (terminated/transferred users).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Access provisioning and review"],
    },
    {
        "id": "cisa-prot-004", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_access_controls", "difficulty": 2, "type": "multi",
        "stem": "Multi-factor authentication requires two or more factors from DIFFERENT categories. "
                "Which TWO combinations qualify as true multi-factor authentication? (Choose two.)",
        "options": [
            {"id": "A", "text": "A password and the answer to a security question"},
            {"id": "B", "text": "A password and a one-time code from a hardware token"},
            {"id": "C", "text": "A PIN and a fingerprint scan"},
            {"id": "D", "text": "Two different passwords"},
        ],
        "correct": ["B", "C"],
        "explanation": {
            "correct": "Multi-factor requires factors from different categories: a password (knowledge) plus a "
                       "hardware token (possession), and a PIN (knowledge) plus a fingerprint (inherence), each "
                       "combine two distinct factors.",
            "distractors": {
                "A": "A password and a security-question answer are both 'something you know' - a single factor used twice.",
                "D": "Two passwords are both knowledge factors, still a single factor.",
            },
            "exam_pattern": "MFA needs different categories (know/have/are); two of the same category is still single-factor.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Authentication factors"],
    },

    # ===== cisa_network_security ============================================
    {
        "id": "cisa-prot-005", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 3, "type": "mcq",
        "stem": "Which type of firewall makes filtering decisions based on the state and context of a "
                "connection rather than inspecting each packet in isolation?",
        "options": [
            {"id": "A", "text": "Static packet-filtering firewall"},
            {"id": "B", "text": "Stateful inspection firewall"},
            {"id": "C", "text": "A simple network hub"},
            {"id": "D", "text": "A patch panel"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A stateful inspection firewall tracks the state of active connections and permits packets "
                       "that belong to an established, legitimate session, offering stronger control than stateless filtering.",
            "distractors": {
                "A": "A static packet filter examines each packet against rules without tracking connection state.",
                "C": "A hub is a basic repeater with no filtering capability.",
                "D": "A patch panel is a passive cabling device, not a firewall.",
            },
            "exam_pattern": "Tracks connection state/context = stateful inspection firewall.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Firewall types"],
    },
    {
        "id": "cisa-prot-006", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "mcq",
        "stem": "Which device sits inline in the traffic path and can automatically block malicious "
                "traffic in real time, rather than only alerting on it?",
        "options": [
            {"id": "A", "text": "Intrusion prevention system (IPS)"},
            {"id": "B", "text": "Passive intrusion detection system (IDS)"},
            {"id": "C", "text": "A syslog server"},
            {"id": "D", "text": "A network tap used only for monitoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IPS is placed inline and can actively block or drop malicious traffic as it passes, "
                       "whereas an IDS passively detects and alerts without stopping the traffic.",
            "distractors": {
                "B": "An IDS detects and alerts but does not block traffic.",
                "C": "A syslog server collects log data; it does not block traffic.",
                "D": "A passive tap only copies traffic for monitoring and cannot block it.",
            },
            "exam_pattern": "IPS = inline, blocks (prevention); IDS = passive, alerts (detection).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — IDS and IPS"],
    },
    {
        "id": "cisa-prot-007", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_network_security", "difficulty": 2, "type": "mcq",
        "stem": "To protect the confidentiality and integrity of data transmitted between two offices over "
                "the public internet, which solution is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Disabling the firewall to improve speed"},
            {"id": "B", "text": "Sending the data as plaintext email"},
            {"id": "C", "text": "A VPN using IPsec"},
            {"id": "D", "text": "Publishing the data on a public web server"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A VPN using IPsec creates an encrypted, authenticated tunnel over the public internet, "
                       "protecting the confidentiality and integrity of data in transit between sites.",
            "distractors": {
                "A": "Disabling the firewall weakens security and does nothing to protect data in transit.",
                "B": "Plaintext email exposes the data to interception.",
                "D": "Publishing on a public server exposes the data to anyone.",
            },
            "exam_pattern": "Protect site-to-site traffic over the internet = encrypted VPN tunnel (IPsec).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — VPNs and secure transmission"],
    },

    # ===== cisa_data_classification =========================================
    {
        "id": "cisa-prot-008", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a data classification scheme?",
        "options": [
            {"id": "A", "text": "To make all data publicly available"},
            {"id": "B", "text": "To ensure data receives a level of protection appropriate to its sensitivity and value"},
            {"id": "C", "text": "To delete old data automatically"},
            {"id": "D", "text": "To speed up database queries"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Classification assigns data to sensitivity levels so that protection controls (access, "
                       "encryption, handling) are applied commensurate with the data's value and risk, avoiding both "
                       "under- and over-protection.",
            "distractors": {
                "A": "Classification restricts access appropriately; it does not make everything public.",
                "C": "Retention/disposal is a related but separate process from classifying sensitivity.",
                "D": "Query performance is a database-design matter, not the purpose of classification.",
            },
            "exam_pattern": "Classify data so that the strength of protection matches its sensitivity/value.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Data classification"],
    },
    {
        "id": "cisa-prot-009", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "Who is PRIMARILY responsible for assigning the classification level to a set of data?",
        "options": [
            {"id": "A", "text": "The IS auditor"},
            {"id": "B", "text": "The help desk technician"},
            {"id": "C", "text": "The backup operator"},
            {"id": "D", "text": "The data owner"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The data owner, who understands the data's business value and sensitivity, is responsible "
                       "for assigning its classification; custodians then apply the matching controls.",
            "distractors": {
                "A": "The auditor evaluates whether classification is done appropriately but does not assign it.",
                "B": "The help desk provides support, not data classification.",
                "C": "The backup operator is a custodian who safeguards data per the owner's direction.",
            },
            "exam_pattern": "The data owner classifies; custodians protect according to that classification.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Data ownership and classification"],
    },
    {
        "id": "cisa-prot-010", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_data_classification", "difficulty": 3, "type": "mcq",
        "stem": "An IS auditor finds that highly sensitive customer data is stored without encryption "
                "while publicly available marketing data is heavily encrypted. This BEST indicates that:",
        "options": [
            {"id": "A", "text": "Protection controls are not aligned with the data classification"},
            {"id": "B", "text": "The encryption algorithm is too strong"},
            {"id": "C", "text": "The marketing team is the data owner of the customer data"},
            {"id": "D", "text": "No further action is ever needed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Protection should be proportional to classification; encrypting low-sensitivity data while "
                       "leaving highly sensitive data exposed shows controls are misaligned with the data's classification and risk.",
            "distractors": {
                "B": "Strong encryption on public data is wasteful, but the core finding is the unprotected sensitive data.",
                "C": "The storage pattern says nothing about who owns the customer data.",
                "D": "Unprotected sensitive data clearly requires corrective action.",
            },
            "exam_pattern": "Controls must track classification - sensitive data left under-protected is the red flag.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Aligning controls to classification"],
    },

    # ===== cisa_encryption_pki ==============================================
    {
        "id": "cisa-prot-011", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 1, "type": "mcq",
        "stem": "Which type of cryptography uses the SAME single shared key to both encrypt and decrypt "
                "data?",
        "options": [
            {"id": "A", "text": "Asymmetric (public-key) cryptography"},
            {"id": "B", "text": "A digital certificate"},
            {"id": "C", "text": "Symmetric cryptography"},
            {"id": "D", "text": "A cryptographic hash function"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Symmetric cryptography uses one shared secret key for both encryption and decryption; it "
                       "is fast but requires secure key distribution.",
            "distractors": {
                "A": "Asymmetric cryptography uses a key pair (public and private), not one shared key.",
                "B": "A digital certificate binds a public key to an identity; it is not an encryption method itself.",
                "D": "A hash function is one-way and does not decrypt anything.",
            },
            "exam_pattern": "One shared key for encrypt+decrypt = symmetric (fast, but key distribution is the challenge).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Symmetric vs. asymmetric encryption"],
    },
    {
        "id": "cisa-prot-012", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 3, "type": "mcq",
        "stem": "To create a digital signature, the sender encrypts the message's hash (digest) with which "
                "key?",
        "options": [
            {"id": "A", "text": "The recipient's public key"},
            {"id": "B", "text": "The sender's private key"},
            {"id": "C", "text": "The recipient's private key"},
            {"id": "D", "text": "A shared symmetric key"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A digital signature is formed by encrypting the message digest with the sender's private "
                       "key; anyone can verify it with the sender's public key, providing authentication, integrity, "
                       "and non-repudiation.",
            "distractors": {
                "A": "Encrypting with the recipient's public key provides confidentiality, not a signature.",
                "C": "The sender does not possess the recipient's private key.",
                "D": "A shared symmetric key cannot provide non-repudiation, since both parties hold it.",
            },
            "exam_pattern": "Sign with the sender's PRIVATE key (verify with the public key) -> integrity + authentication + non-repudiation.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Digital signatures"],
    },
    {
        "id": "cisa-prot-013", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_encryption_pki", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In a public key infrastructure (PKI), the trusted entity that issues, "
                "signs, and revokes digital certificates binding a public key to an identity is the "
                "certificate ______.",
        "correct": ["authority", "certificate authority", "ca"],
        "explanation": {
            "correct": "The certificate authority (CA) is the trusted third party that issues and digitally signs "
                       "certificates (and manages revocation), establishing trust in the binding between a public key and an identity.",
            "distractors": {},
            "exam_pattern": "The trusted issuer/signer of certificates in a PKI = certificate authority (CA).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — PKI and certificate authorities"],
    },

    # ===== cisa_security_monitoring =========================================
    {
        "id": "cisa-prot-014", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Before relying on system audit logs as evidence of user activity, what must the IS "
                "auditor FIRST be satisfied of?",
        "options": [
            {"id": "A", "text": "That the logs are printed on paper"},
            {"id": "B", "text": "That the logs are stored on the fastest available disk"},
            {"id": "C", "text": "That the logs are protected from unauthorized modification so their integrity can be trusted"},
            {"id": "D", "text": "That the logs are deleted every day"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Logs are reliable evidence only if their integrity is assured; the auditor must confirm "
                       "that logs are protected from unauthorized alteration or deletion before relying on them.",
            "distractors": {
                "A": "The medium (paper vs. electronic) does not establish integrity.",
                "B": "Storage speed is irrelevant to the reliability of log content.",
                "D": "Deleting logs daily would destroy the very evidence needed.",
            },
            "exam_pattern": "Logs are evidence only if protected from tampering - verify integrity before relying on them.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Log integrity and security monitoring"],
    },
    {
        "id": "cisa-prot-015", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Which technology centrally collects, aggregates, and correlates security event data from "
                "many sources to support monitoring and alerting?",
        "options": [
            {"id": "A", "text": "Security information and event management (SIEM)"},
            {"id": "B", "text": "A single-host antivirus scanner"},
            {"id": "C", "text": "A spreadsheet of passwords"},
            {"id": "D", "text": "An uninterruptible power supply (UPS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM aggregates and correlates logs and events from across the environment, enabling "
                       "centralized monitoring, alerting, and investigation of security incidents.",
            "distractors": {
                "B": "Host antivirus protects one endpoint; it does not centrally correlate events across sources.",
                "C": "A password spreadsheet is a security risk, not a monitoring technology.",
                "D": "A UPS provides backup power, unrelated to event correlation.",
            },
            "exam_pattern": "Central collection + correlation of security events = SIEM.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Security monitoring and SIEM"],
    },
    {
        "id": "cisa-prot-016", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Continuous review of security monitoring alerts and system logs to identify security "
                "events functions PRIMARILY as which type of control?",
        "options": [
            {"id": "A", "text": "Preventive control"},
            {"id": "B", "text": "Deterrent control"},
            {"id": "C", "text": "Compensating control"},
            {"id": "D", "text": "Detective control"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Monitoring and log review discover security events that have occurred or are occurring, "
                       "which makes them detective controls.",
            "distractors": {
                "A": "A preventive control stops an event before it happens (e.g., access restriction), unlike monitoring.",
                "B": "A deterrent discourages action but does not identify events.",
                "C": "A compensating control substitutes for a missing primary control; monitoring here is primarily detective.",
            },
            "exam_pattern": "Monitoring/log review finds events as/after they occur = detective control.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Monitoring as a detective control"],
    },

    # ===== cisa_physical_environmental ======================================
    {
        "id": "cisa-prot-017", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "Which fire-suppression approach is MOST appropriate for a computer room to extinguish "
                "fire while minimizing damage to the electronic equipment?",
        "options": [
            {"id": "A", "text": "An open bucket of water in each corner"},
            {"id": "B", "text": "A clean-agent (inert gas) suppression system"},
            {"id": "C", "text": "No suppression, relying on staff to unplug equipment"},
            {"id": "D", "text": "A wet-pipe sprinkler aimed directly at the servers"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A clean-agent / inert-gas suppression system extinguishes fire without leaving water or "
                       "residue, protecting electronic equipment - the preferred approach for computer-room areas.",
            "distractors": {
                "A": "Buckets of water are ineffective, and water damages electronics and poses a shock hazard.",
                "C": "No suppression leaves the facility exposed to catastrophic fire loss.",
                "D": "A wet-pipe sprinkler discharging water onto servers can destroy the equipment it is meant to coexist with.",
            },
            "exam_pattern": "Protect electronics from fire with clean-agent/inert-gas suppression (avoid water damage).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Fire suppression"],
    },
    {
        "id": "cisa-prot-018", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 1, "type": "mcq",
        "stem": "What is the PRIMARY purpose of an uninterruptible power supply (UPS) in a data center?",
        "options": [
            {"id": "A", "text": "To cool the servers"},
            {"id": "B", "text": "To filter network traffic"},
            {"id": "C", "text": "To provide continuous short-term power during brief outages and allow an orderly shutdown or transfer to a generator"},
            {"id": "D", "text": "To back up data to tape"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A UPS supplies immediate battery power during short outages or dips, keeping systems "
                       "running long enough for a graceful shutdown or for a generator to take over - protecting "
                       "availability and preventing data loss/corruption.",
            "distractors": {
                "A": "Cooling is provided by HVAC, not a UPS.",
                "B": "Filtering traffic is a firewall function.",
                "D": "Data backup is handled by backup systems, not a UPS.",
            },
            "exam_pattern": "UPS = bridge power for short outages + orderly shutdown / transfer to generator.",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Environmental and power controls"],
    },
    {
        "id": "cisa-prot-019", "exam": "cisa", "domain": "cisa_protection_assets",
        "subtopic": "cisa_physical_environmental", "difficulty": 2, "type": "mcq",
        "stem": "A physical access-control vestibule ('mantrap') with two interlocking doors is designed "
                "PRIMARILY to prevent:",
        "options": [
            {"id": "A", "text": "Tailgating/piggybacking (an unauthorized person following an authorized one through a door)"},
            {"id": "B", "text": "Power surges to the equipment"},
            {"id": "C", "text": "SQL injection attacks"},
            {"id": "D", "text": "Email phishing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A mantrap / access-control vestibule allows only one person through at a time via "
                       "interlocking doors, preventing tailgating or piggybacking into a secure area.",
            "distractors": {
                "B": "Power surges are handled by electrical protection, not a mantrap.",
                "C": "SQL injection is an application-layer attack unrelated to physical entry.",
                "D": "Phishing is a social-engineering email threat, not a physical access control.",
            },
            "exam_pattern": "Mantrap/vestibule stops tailgating/piggybacking into secure areas (one person at a time).",
        },
        "references": ["ISACA CISA Review Manual: Domain 5 — Physical access controls"],
    },
]
