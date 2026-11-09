"""EC-Council CEH v13 pool - Domain 6.0: Cloud Computing and Cryptography.

Original, objective-aligned practice items for CertLab's CEH track, covering the
two subtopics of the Cloud Computing and Cryptography domain:
  * ceh_cloud_computing - the shared responsibility model, containers vs VMs,
                          serverless (FaaS), storage misconfiguration, IAM least
                          privilege, exposed access keys, and CASB.
  * ceh_cryptography    - symmetric vs asymmetric encryption, hashing, digital
                          signatures, PKI / certificate authorities, TLS,
                          steganography vs cryptography, and collision (birthday)
                          attacks.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the concept, tool, or defense) - no working exploit
code, payloads, or step-by-step attack instructions, and never real or memorized
exam items.
"""

QUESTIONS = [
    # ===== ceh_cloud_computing ==============================================
    {
        "id": "ceh-cc-001", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 1, "type": "mcq",
        "stem": "In the cloud shared responsibility model, which element is always the customer's "
                "responsibility regardless of the service model (IaaS, PaaS, or SaaS)?",
        "options": [
            {"id": "A", "text": "The data the customer stores and its classification"},
            {"id": "B", "text": "The physical datacenter hardware"},
            {"id": "C", "text": "The hypervisor"},
            {"id": "D", "text": "The physical network fabric"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Customers always remain responsible for their own data (and their identities/access), in "
                       "every cloud service model.",
            "distractors": {
                "B": "Physical datacenter hardware is always the provider's responsibility.",
                "C": "The hypervisor is managed and secured by the cloud provider.",
                "D": "The physical network fabric is the provider's responsibility.",
            },
            "exam_pattern": "Customer always owns data and identities; provider always owns the physical layer and hypervisor.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-002", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "mcq",
        "stem": "A company exposes sensitive files because a cloud object-storage bucket was left publicly "
                "readable. This is an example of which issue?",
        "options": [
            {"id": "A", "text": "SQL injection"},
            {"id": "B", "text": "Cloud storage misconfiguration (excessive public access)"},
            {"id": "C", "text": "Rainbow table attack"},
            {"id": "D", "text": "ARP poisoning"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A publicly readable storage bucket is a misconfiguration; applying least privilege and "
                       "'block public access' settings prevents this common cloud exposure.",
            "distractors": {
                "A": "SQL injection manipulates database queries; it is not a storage-permission mistake.",
                "C": "A rainbow table attack cracks password hashes, unrelated to bucket permissions.",
                "D": "ARP poisoning is a local-network man-in-the-middle technique, not cloud storage.",
            },
            "exam_pattern": "Publicly readable storage bucket exposing data = misconfiguration (block public access / least privilege).",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-003", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "mcq",
        "stem": "To limit the blast radius if cloud credentials are stolen, which principle should govern the "
                "permissions assigned to each identity and role?",
        "options": [
            {"id": "A", "text": "Security through obscurity"},
            {"id": "B", "text": "Defense evasion"},
            {"id": "C", "text": "Least privilege"},
            {"id": "D", "text": "Fail-open access"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Least privilege grants each identity only the permissions it needs, so stolen credentials "
                       "unlock as little as possible.",
            "distractors": {
                "A": "Security through obscurity hides details; it is not an access-control principle.",
                "B": "Defense evasion is an attacker tactic, not a permissions principle.",
                "D": "Fail-open grants access when a check fails, which is unsafe.",
            },
            "exam_pattern": "Grant only the permissions needed = least privilege (core IAM control).",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-004", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "mcq",
        "stem": "Which cloud computing model runs event-driven functions where the provider fully manages the "
                "underlying servers and the customer never patches an operating system?",
        "options": [
            {"id": "A", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "B", "text": "Colocation"},
            {"id": "C", "text": "On-premises virtualization"},
            {"id": "D", "text": "Serverless (Function as a Service)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Serverless/FaaS runs event-driven functions on infrastructure the provider fully manages, "
                       "so the customer never patches or scales servers.",
            "distractors": {
                "A": "IaaS still requires the customer to manage and patch the guest operating system.",
                "B": "Colocation rents datacenter space for the customer's own hardware.",
                "C": "On-premises virtualization is entirely customer-managed.",
            },
            "exam_pattern": "Event-driven functions, no servers to manage/patch = serverless (FaaS).",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-005", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "mcq",
        "stem": "Which technology packages an application with its dependencies into a lightweight, portable "
                "unit that shares the host operating system's kernel rather than running a full guest OS?",
        "options": [
            {"id": "A", "text": "Containers"},
            {"id": "B", "text": "Type-1 hypervisor virtual machines"},
            {"id": "C", "text": "Rainbow tables"},
            {"id": "D", "text": "Honeypots"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Containers bundle an app and its dependencies and share the host kernel, making them "
                       "lighter and faster to start than full virtual machines.",
            "distractors": {
                "B": "Each hypervisor VM runs a full guest OS, which is heavier than a container.",
                "C": "Rainbow tables are a password-cracking data structure, not a packaging technology.",
                "D": "Honeypots are decoy systems, unrelated to application packaging.",
            },
            "exam_pattern": "Shares host kernel, packages app plus dependencies, lightweight = container (vs full VM).",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-006", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 3, "type": "mcq",
        "stem": "Which security solution sits between users and cloud services to enforce policy, provide "
                "visibility into cloud usage, and help detect unsanctioned 'shadow IT'?",
        "options": [
            {"id": "A", "text": "A web application firewall (WAF)"},
            {"id": "B", "text": "A cloud access security broker (CASB)"},
            {"id": "C", "text": "A rainbow table"},
            {"id": "D", "text": "A deauthentication tool"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A CASB brokers traffic between users and cloud services to enforce policy, give usage "
                       "visibility, and surface shadow IT.",
            "distractors": {
                "A": "A WAF filters web-application attacks; it does not broker cloud-service usage policy and visibility.",
                "C": "A rainbow table is a cracking data structure, not a cloud security control.",
                "D": "A deauthentication tool is a wireless attack utility, unrelated to cloud policy.",
            },
            "exam_pattern": "Policy plus visibility between users and cloud services, finds shadow IT = CASB.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-007", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In the cloud shared ______ model, the provider secures the cloud "
                "infrastructure while the customer secures their own data, identities, and configurations.",
        "correct": ["responsibility"],
        "explanation": {
            "correct": "The shared responsibility model divides duties between the provider (security OF the cloud) "
                       "and the customer (security IN the cloud); misreading it is a frequent cause of cloud breaches.",
            "distractors": {},
            "exam_pattern": "Provider secures the cloud, customer secures what's in it = shared responsibility model.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-008", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 3, "type": "multi",
        "stem": "Which TWO are common contributors to cloud data breaches that defenders should prioritize "
                "fixing? (Choose two.)",
        "options": [
            {"id": "A", "text": "Misconfigured storage and overly permissive IAM policies"},
            {"id": "B", "text": "Requiring multi-factor authentication on administrative accounts"},
            {"id": "C", "text": "Leaked or hard-coded access keys committed to code repositories"},
            {"id": "D", "text": "Enabling provider-side encryption at rest"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Storage/IAM misconfiguration and exposed access keys are leading causes of cloud breaches, "
                       "so they are priority fixes.",
            "distractors": {
                "B": "Requiring MFA is a defense that reduces breaches, not a cause of them.",
                "D": "Encryption at rest is a protective control, not a breach contributor.",
            },
            "exam_pattern": "Top cloud breach causes: misconfiguration, excessive IAM permissions, and exposed keys.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },

    # ===== ceh_cryptography =================================================
    {
        "id": "ceh-cc-009", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly describes symmetric encryption such as AES?",
        "options": [
            {"id": "A", "text": "The same secret key is used to encrypt and to decrypt"},
            {"id": "B", "text": "A public key encrypts and a separate private key decrypts"},
            {"id": "C", "text": "It is used only to create digital signatures"},
            {"id": "D", "text": "It requires no key at all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Symmetric encryption uses one shared secret key for both encryption and decryption, which "
                       "makes it fast but requires secure key distribution.",
            "distractors": {
                "B": "Using a public/private key pair describes asymmetric encryption.",
                "C": "Digital signatures rely on asymmetric keys, not symmetric encryption.",
                "D": "Encryption always requires a key.",
            },
            "exam_pattern": "One shared secret key for both directions = symmetric (AES); a key pair = asymmetric (RSA/ECC).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-010", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "Using asymmetric cryptography to send a confidential message that only the intended "
                "recipient can read, the sender encrypts the message with which key?",
        "options": [
            {"id": "A", "text": "The sender's private key"},
            {"id": "B", "text": "A shared symmetric key sent in the clear"},
            {"id": "C", "text": "The recipient's public key"},
            {"id": "D", "text": "A hash of the message"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Encrypting with the recipient's public key means only the recipient's matching private key "
                       "can decrypt it, providing confidentiality.",
            "distractors": {
                "A": "Encrypting with the sender's private key provides a signature, not confidentiality.",
                "B": "Sending a key in the clear exposes it and defeats confidentiality.",
                "D": "A hash is one-way and cannot be decrypted back into the message.",
            },
            "exam_pattern": "Confidentiality: encrypt with the recipient's public key (only their private key decrypts).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-011", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "Which property best characterizes a cryptographic hash function such as SHA-256?",
        "options": [
            {"id": "A", "text": "It is reversible when you have the right key"},
            {"id": "B", "text": "It is a one-way function producing a fixed-length digest"},
            {"id": "C", "text": "It encrypts data to provide confidentiality"},
            {"id": "D", "text": "It compresses files to save storage space"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A cryptographic hash is a one-way function that maps any input to a fixed-length digest, "
                       "used for integrity checking rather than reversible encryption.",
            "distractors": {
                "A": "Hashes are one-way and are not reversible with a key.",
                "C": "Hashing provides integrity, not confidentiality; it does not encrypt.",
                "D": "Hashing is not a storage-compression technique.",
            },
            "exam_pattern": "One-way, fixed-length digest for integrity = cryptographic hash (SHA-256).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-012", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "A sender signs a document by encrypting its hash with their private key. Verifying the "
                "signature with the sender's public key primarily assures the recipient of what?",
        "options": [
            {"id": "A", "text": "Confidentiality of the document's contents"},
            {"id": "B", "text": "That the file was compressed correctly"},
            {"id": "C", "text": "Faster transmission of the document"},
            {"id": "D", "text": "Integrity of the message and authenticity of the sender (non-repudiation)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A digital signature lets the recipient confirm the message was not altered (integrity) and "
                       "came from the holder of the private key (authenticity/non-repudiation).",
            "distractors": {
                "A": "Signing does not hide the contents; confidentiality requires encrypting the message itself.",
                "B": "Signatures say nothing about compression.",
                "C": "Signatures do not speed up transmission.",
            },
            "exam_pattern": "Sign hash with private key, verify with public key = integrity + authenticity (non-repudiation), not confidentiality.",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-013", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 1, "type": "mcq",
        "stem": "In a public key infrastructure (PKI), which entity issues and digitally signs the "
                "certificates that bind a public key to a verified identity?",
        "options": [
            {"id": "A", "text": "Certificate authority (CA)"},
            {"id": "B", "text": "Honeypot"},
            {"id": "C", "text": "Botnet controller"},
            {"id": "D", "text": "Packet sniffer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A certificate authority issues and signs digital certificates, vouching that a public key "
                       "belongs to the named identity - the trust anchor of PKI.",
            "distractors": {
                "B": "A honeypot is a decoy system, not a certificate issuer.",
                "C": "A botnet controller commands compromised hosts; it has no PKI role.",
                "D": "A packet sniffer captures traffic; it does not issue certificates.",
            },
            "exam_pattern": "Issues/signs certificates binding key to identity = certificate authority (CA).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-014", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 1, "type": "mcq",
        "stem": "Which protocol secures data in transit for HTTPS, providing encryption, integrity, and "
                "server authentication between a browser and a web server?",
        "options": [
            {"id": "A", "text": "FTP"},
            {"id": "B", "text": "TLS (Transport Layer Security)"},
            {"id": "C", "text": "SNMP"},
            {"id": "D", "text": "Telnet"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "TLS, the successor to SSL, encrypts and authenticates web traffic in transit, which is "
                       "what makes HTTP into HTTPS.",
            "distractors": {
                "A": "FTP transfers files without encryption by default.",
                "C": "SNMP manages network devices; it does not secure web traffic.",
                "D": "Telnet provides remote access in clear text, the opposite of secure transport.",
            },
            "exam_pattern": "Encrypts/authenticates web traffic in transit = TLS (successor to SSL).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-015", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Whereas cryptography scrambles a message so it cannot be read, ______ "
                "hides the very existence of the message inside a carrier such as an image or audio file.",
        "correct": ["steganography"],
        "explanation": {
            "correct": "Cryptography protects confidentiality by making data unreadable; steganography conceals "
                       "that a message exists at all by embedding it in a carrier file. The two can be combined.",
            "distractors": {},
            "exam_pattern": "Hide that a message exists = steganography; make it unreadable = cryptography.",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-016", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "An attacker searches for two different inputs that produce the same hash value, exploiting "
                "the mathematics behind the birthday paradox. Which attack is this?",
        "options": [
            {"id": "A", "text": "Brute-force key search"},
            {"id": "B", "text": "Phishing"},
            {"id": "C", "text": "Collision (birthday) attack"},
            {"id": "D", "text": "SYN flood"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Finding two inputs with the same hash is a collision attack; the birthday paradox makes "
                       "collisions far easier than intuition suggests, which is why MD5 and SHA-1 are deprecated.",
            "distractors": {
                "A": "Brute-force key search tries keys against ciphertext; it does not seek hash collisions.",
                "B": "Phishing is social engineering, not a cryptanalytic attack.",
                "D": "A SYN flood is a denial-of-service attack, unrelated to hashing.",
            },
            "exam_pattern": "Two inputs, same hash via birthday math = collision attack (why MD5/SHA-1 are deprecated).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
]
