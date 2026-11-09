"""(ISC)² Certified in Cybersecurity (CC) pool - Domain 5: Security Operations.

Original, objective-aligned practice items for the five Security Operations
subtopics CertLab tracks:
  * cc_data_security        - data states (at rest/in transit/in use), data
                              classification, protecting stored data, and secure
                              data destruction.
  * cc_system_hardening     - reducing the attack surface, patch management, and
                              changing default credentials.
  * cc_security_policies_ops - acceptable use policy (AUP), change management, and
                              password policy.
  * cc_security_awareness   - the purpose of awareness training, phishing
                              simulations, and resisting social engineering.
  * cc_encryption_basics    - symmetric vs. asymmetric encryption, hashing, and what
                              each protects (confidentiality vs. integrity).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased, every
wrong option carries a distractor note, and each item names the (ISC)² CC exam-outline
area it draws on. Entry-level depth only - core, well-established facts.
"""

QUESTIONS = [
    # ===== cc_data_security =================================================
    {
        "id": "isc2cc-ops-001", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A file is being uploaded from an employee's laptop across the network to a cloud "
                "server. While it is moving over the network, the data is in which state?",
        "options": [
            {"id": "A", "text": "Data at rest"},
            {"id": "B", "text": "Data in transit (in motion)"},
            {"id": "C", "text": "Data in use"},
            {"id": "D", "text": "Data archived"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Data in transit (in motion) is data actively moving across a network; it is "
                       "typically protected with transport encryption such as TLS.",
            "distractors": {
                "A": "Data at rest is stored data sitting on a disk or in a database, not data moving across the network.",
                "C": "Data in use is data being actively processed in memory/CPU, not data traversing the network.",
                "D": "'Archived' is a storage situation (a form of at rest), not the in-motion state.",
            },
            "exam_pattern": "Moving over the network = in transit; stored = at rest; being processed = in use.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Data security (data states)"],
    },
    {
        "id": "isc2cc-ops-002", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_data_security", "difficulty": 1, "type": "mcq",
        "stem": "An organization assigns labels such as 'Public,' 'Internal,' and 'Confidential' to its "
                "information so each category receives the appropriate level of protection. This "
                "practice is called:",
        "options": [
            {"id": "A", "text": "Data masking"},
            {"id": "B", "text": "Data mining"},
            {"id": "C", "text": "Data classification"},
            {"id": "D", "text": "Data normalization"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Data classification categorizes information by sensitivity so that handling, access, "
                       "and protection requirements can be applied consistently to each level.",
            "distractors": {
                "A": "Data masking hides portions of data (e.g., showing only the last 4 digits); it is a protection technique, not classification.",
                "B": "Data mining discovers patterns in large datasets; it does not assign sensitivity labels.",
                "D": "Data normalization organizes database structure to reduce redundancy, unrelated to sensitivity labeling.",
            },
            "exam_pattern": "Labeling data by sensitivity (Public/Internal/Confidential) = data classification.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Data security (classification)"],
    },
    {
        "id": "isc2cc-ops-003", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_data_security", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to protect the confidentiality of sensitive files stored on laptops in "
                "case a device is lost or stolen. Which control best protects this data AT REST?",
        "options": [
            {"id": "A", "text": "A login warning banner"},
            {"id": "B", "text": "A TLS/HTTPS certificate on the web server"},
            {"id": "C", "text": "A network intrusion detection system"},
            {"id": "D", "text": "Full-disk encryption on the laptops"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Full-disk encryption renders stored data unreadable without the key, protecting the "
                       "confidentiality of data at rest even if the laptop is physically stolen.",
            "distractors": {
                "A": "A warning banner is a deterrent/notice; it does not keep stored data confidential.",
                "B": "TLS/HTTPS protects data in transit over the network, not data sitting on a stolen disk.",
                "C": "An IDS detects network attacks; it does nothing to protect files on a lost laptop.",
            },
            "exam_pattern": "Protect stored data on a device = encryption at rest (e.g., full-disk encryption).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Data security (protecting data at rest)"],
    },
    {
        "id": "isc2cc-ops-004", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_data_security", "difficulty": 2, "type": "mcq",
        "stem": "Before disposing of old magnetic hard drives, a company wants to erase them by exposing "
                "them to a powerful magnetic field that scrambles the stored data. This method is:",
        "options": [
            {"id": "A", "text": "Reformatting the drive"},
            {"id": "B", "text": "Degaussing"},
            {"id": "C", "text": "Encrypting the drive"},
            {"id": "D", "text": "Defragmenting the drive"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Degaussing uses a strong magnetic field to destroy the data on magnetic media such "
                       "as hard drives and tapes, rendering it unrecoverable.",
            "distractors": {
                "A": "Reformatting does not truly erase data; much of it can be recovered with forensic tools.",
                "C": "Encrypting protects data in use/storage but does not destroy it for disposal.",
                "D": "Defragmenting reorganizes files for performance; it does not erase or destroy data.",
            },
            "exam_pattern": "Strong magnetic field to wipe magnetic media = degaussing (a sanitization/destruction method).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Data security (secure destruction)"],
    },

    # ===== cc_system_hardening ==============================================
    {
        "id": "isc2cc-ops-005", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening", "difficulty": 2, "type": "mcq",
        "stem": "An administrator 'hardens' a new server before deployment. What is the primary goal of "
                "system hardening?",
        "options": [
            {"id": "A", "text": "To install as many optional features as possible"},
            {"id": "B", "text": "To maximize the server's graphics performance"},
            {"id": "C", "text": "To reduce the attack surface by removing unnecessary services, accounts, and software"},
            {"id": "D", "text": "To make the server reachable from the public internet"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Hardening reduces the attack surface: disable unneeded services, remove default/"
                       "unused accounts and software, close unused ports, and apply secure configurations.",
            "distractors": {
                "A": "Adding more features increases the attack surface - the opposite of hardening.",
                "B": "Graphics performance is unrelated to security hardening.",
                "D": "Needlessly exposing a server to the internet increases risk rather than reducing it.",
            },
            "exam_pattern": "Hardening = shrink the attack surface (fewer services/accounts/ports, secure config, patches).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - System hardening (attack surface)"],
    },
    {
        "id": "isc2cc-ops-006", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening", "difficulty": 1, "type": "mcq",
        "stem": "Regularly applying the vendor's software updates to fix known security vulnerabilities "
                "on systems is known as:",
        "options": [
            {"id": "A", "text": "Penetration testing"},
            {"id": "B", "text": "Load balancing"},
            {"id": "C", "text": "Data classification"},
            {"id": "D", "text": "Patch management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Patch management is the process of acquiring, testing, and applying updates to "
                       "remediate known vulnerabilities and keep systems secure.",
            "distractors": {
                "A": "Penetration testing finds weaknesses by simulating attacks; it does not itself apply the fixes.",
                "B": "Load balancing distributes traffic across servers for performance/availability, not vulnerability fixes.",
                "C": "Data classification labels information by sensitivity; it does not apply software updates.",
            },
            "exam_pattern": "Applying updates to close known vulnerabilities = patch management.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - System hardening (patch management)"],
    },
    {
        "id": "isc2cc-ops-007", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A new network router ships with a widely published default administrator username and "
                "password. Which hardening step should be performed first?",
        "options": [
            {"id": "A", "text": "Change the default administrator credentials to a strong, unique password"},
            {"id": "B", "text": "Leave the defaults in place to save setup time"},
            {"id": "C", "text": "Share the default password with all staff for convenience"},
            {"id": "D", "text": "Write the default password on a label attached to the router"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Default credentials are publicly known and are among the first things attackers try, "
                       "so changing them to a strong, unique password is a critical hardening step.",
            "distractors": {
                "B": "Leaving defaults in place leaves a well-known, easily exploited entry point open.",
                "C": "Sharing the password broadly destroys accountability and increases exposure.",
                "D": "Labeling the device with its password exposes the credential to anyone nearby.",
            },
            "exam_pattern": "Always change well-known default credentials when hardening a new device.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - System hardening (default credentials)"],
    },

    # ===== cc_security_policies_ops =========================================
    {
        "id": "isc2cc-ops-008", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops", "difficulty": 1, "type": "mcq",
        "stem": "Which document defines the rules for how employees may use company computers, email, "
                "and internet access, and what uses are prohibited?",
        "options": [
            {"id": "A", "text": "Disaster Recovery Plan (DRP)"},
            {"id": "B", "text": "Business Continuity Plan (BCP)"},
            {"id": "C", "text": "Acceptable Use Policy (AUP)"},
            {"id": "D", "text": "Incident Response Plan (IRP)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An Acceptable Use Policy (AUP) defines the permitted and prohibited uses of an "
                       "organization's systems and assets by employees.",
            "distractors": {
                "A": "A DRP covers restoring IT systems after a disaster, not day-to-day acceptable use.",
                "B": "A BCP describes how to keep essential functions running during a disruption, not acceptable use.",
                "D": "An IRP defines how to respond to security incidents, not general computer-use rules.",
            },
            "exam_pattern": "Rules for how staff may use company IT and assets = Acceptable Use Policy (AUP).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security policies (acceptable use policy)"],
    },
    {
        "id": "isc2cc-ops-009", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops", "difficulty": 2, "type": "mcq",
        "stem": "An organization uses a formal process to review, approve, test, and document any "
                "modification to its systems before it is implemented, reducing the risk of outages. "
                "This process is called:",
        "options": [
            {"id": "A", "text": "Incident response"},
            {"id": "B", "text": "Change management"},
            {"id": "C", "text": "Risk acceptance"},
            {"id": "D", "text": "Data classification"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Change management is the formal process of requesting, reviewing, approving, "
                       "testing, and documenting changes so modifications do not introduce unexpected risk.",
            "distractors": {
                "A": "Incident response handles security incidents after they occur, not planned system changes.",
                "C": "Risk acceptance is a decision to tolerate a risk, not a process for controlling changes.",
                "D": "Data classification labels information by sensitivity; it is unrelated to managing changes.",
            },
            "exam_pattern": "Formal review/approve/test/document of system changes = change management.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security policies (change management)"],
    },
    {
        "id": "isc2cc-ops-010", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops", "difficulty": 2, "type": "mcq",
        "stem": "Which policy specifies requirements such as minimum length, required complexity, and how "
                "often users must change their account passwords?",
        "options": [
            {"id": "A", "text": "Separation-of-duties policy"},
            {"id": "B", "text": "Acceptable Use Policy"},
            {"id": "C", "text": "Data retention policy"},
            {"id": "D", "text": "Password policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A password policy sets the rules for credentials - minimum length, complexity, "
                       "expiration/change frequency, reuse limits - to strengthen authentication.",
            "distractors": {
                "A": "A separation-of-duties policy splits critical tasks among people; it is not about password rules.",
                "B": "An AUP governs acceptable use of systems, not the specific rules for password construction.",
                "C": "A data retention policy specifies how long records are kept, not password requirements.",
            },
            "exam_pattern": "Rules for password length/complexity/expiration = password policy.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security policies (password policy)"],
    },

    # ===== cc_security_awareness ============================================
    {
        "id": "isc2cc-ops-011", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary purpose of a security-awareness program for employees?",
        "options": [
            {"id": "A", "text": "To help employees recognize and respond appropriately to security threats, reducing human-related risk"},
            {"id": "B", "text": "To replace all technical security controls"},
            {"id": "C", "text": "To guarantee that no security incident will ever happen"},
            {"id": "D", "text": "To speed up the company's internet connection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security awareness aims to change behavior so employees can recognize and respond to "
                       "threats (like phishing), reducing risk from the human element.",
            "distractors": {
                "B": "Awareness complements technical controls; it does not replace firewalls, encryption, and the like.",
                "C": "No program can guarantee zero incidents; awareness reduces, not eliminates, risk.",
                "D": "Awareness training has nothing to do with network speed.",
            },
            "exam_pattern": "Goal of awareness = change human behavior to recognize/resist threats (people are the weakest link).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security awareness (purpose)"],
    },
    {
        "id": "isc2cc-ops-012", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "An organization periodically sends its own staff realistic but fake 'phishing' emails "
                "and provides coaching to anyone who clicks. What is the main goal of this exercise?",
        "options": [
            {"id": "A", "text": "To punish and publicly shame employees who fail"},
            {"id": "B", "text": "To test whether the email server can handle load"},
            {"id": "C", "text": "To measure and improve employees' ability to recognize phishing"},
            {"id": "D", "text": "To meet a marketing campaign quota"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Simulated phishing campaigns assess how well staff spot social-engineering attempts "
                       "and reinforce training for those who need it, strengthening the human firewall.",
            "distractors": {
                "A": "Effective programs coach rather than shame; punishment undermines a healthy security culture.",
                "B": "The exercise targets human behavior, not email-server load testing.",
                "D": "Phishing simulations are a security-awareness activity, not a marketing effort.",
            },
            "exam_pattern": "Fake phishing emails + coaching = awareness training to build phishing resistance.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security awareness (phishing simulations)"],
    },
    {
        "id": "isc2cc-ops-013", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "An unknown caller claims to be from the IT help desk and asks an employee to read back "
                "their account password so IT can 'fix an issue.' What should a security-aware employee do?",
        "options": [
            {"id": "A", "text": "Provide a coworker's password rather than their own"},
            {"id": "B", "text": "Read the password aloud, since IT needs it to help"},
            {"id": "C", "text": "Email the password instead of saying it out loud"},
            {"id": "D", "text": "Refuse to share the password and verify the request through a known, official channel"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Legitimate IT staff never need your password; this is a social-engineering attempt, "
                       "so the employee should refuse and verify through a trusted, official channel.",
            "distractors": {
                "A": "Disclosing any password, including a coworker's, is a serious security violation.",
                "B": "Sharing a password - even with supposed IT - defeats authentication and accountability and is exactly what the attacker wants.",
                "C": "Emailing the password still discloses it to a potential attacker and leaves it exposed in transit/storage.",
            },
            "exam_pattern": "Never share passwords; verify unsolicited requests through official channels (resist social engineering).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security awareness (social engineering)"],
    },
    {
        "id": "isc2cc-ops-014", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness", "difficulty": 1, "type": "fill",
        "stem": "Because attackers so often target people rather than technology, employees are commonly "
                "described as the weakest ___ in the security chain. (one word)",
        "correct": ["link"],
        "explanation": {
            "correct": "People are frequently called the weakest link because human error and manipulation "
                       "(e.g., falling for phishing) are leading causes of breaches - the reason awareness training matters.",
            "exam_pattern": "Humans = the weakest link; awareness training targets this risk.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Security awareness (human risk)"],
    },

    # ===== cc_encryption_basics =============================================
    {
        "id": "isc2cc-ops-015", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics", "difficulty": 2, "type": "mcq",
        "stem": "An encryption scheme uses a single shared secret key to both encrypt and decrypt data, "
                "and is fast enough for large volumes. Which type of encryption is this?",
        "options": [
            {"id": "A", "text": "Asymmetric encryption"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Steganography"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Symmetric encryption uses the same secret key to encrypt and decrypt; it is fast "
                       "and well suited to bulk data (e.g., AES, 3DES).",
            "distractors": {
                "A": "Asymmetric encryption uses a public/private key pair, not a single shared key, and is slower.",
                "C": "Hashing is a one-way function with no key and cannot be decrypted; it is not encryption.",
                "D": "Steganography hides the existence of a message; it is not key-based encryption.",
            },
            "exam_pattern": "One shared key, fast, bulk data = symmetric; key pair = asymmetric.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Encryption basics (symmetric)"],
    },
    {
        "id": "isc2cc-ops-016", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics", "difficulty": 3, "type": "mcq",
        "stem": "Using asymmetric (public-key) cryptography, which key do you publish so that others can "
                "encrypt a confidential message that only you are able to decrypt?",
        "options": [
            {"id": "A", "text": "Your public key (you decrypt with your matching private key)"},
            {"id": "B", "text": "Your private key (you keep it secret but share it for this)"},
            {"id": "C", "text": "A single shared symmetric key"},
            {"id": "D", "text": "A one-way hash value"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In public-key cryptography, senders encrypt with your freely published public key, "
                       "and only your closely held private key can decrypt - providing confidentiality.",
            "distractors": {
                "B": "The private key must never be shared; sharing it defeats the entire scheme.",
                "C": "A shared symmetric key is used in symmetric encryption, not asymmetric public-key encryption.",
                "D": "A hash is one-way and cannot be used to decrypt a message; it is not an encryption key.",
            },
            "exam_pattern": "Encrypt-to-you with your PUBLIC key; only your PRIVATE key decrypts (confidentiality).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Encryption basics (asymmetric/public key)"],
    },
    {
        "id": "isc2cc-ops-017", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics", "difficulty": 2, "type": "mcq",
        "stem": "A technique produces a fixed-length, irreversible 'fingerprint' of a file so that any "
                "later change to the file can be detected. It uses no key and cannot be reversed. What "
                "is it?",
        "options": [
            {"id": "A", "text": "Asymmetric encryption"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Base64 encoding"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Hashing applies a one-way function (e.g., SHA-256) to produce a fixed-length digest; "
                       "comparing hashes detects any change, which is how it verifies integrity.",
            "distractors": {
                "A": "Asymmetric encryption is reversible with the matching key; it is not a one-way, keyless digest.",
                "B": "Symmetric encryption is reversible with the key and is used for confidentiality, not a one-way fingerprint.",
                "D": "Base64 is reversible encoding for safe data transport, not a one-way integrity check.",
            },
            "exam_pattern": "One-way, fixed-length, keyless fingerprint for integrity = hashing.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Encryption basics (hashing)"],
    },
    {
        "id": "isc2cc-ops-018", "exam": "isc2cc", "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics", "difficulty": 2, "type": "fill",
        "stem": "Encryption's primary security goal is to protect the ___ of data (keeping it secret "
                "from unauthorized parties), whereas hashing is used to protect integrity. Fill in the "
                "missing CIA element. (one word)",
        "correct": ["confidentiality", "confidential"],
        "explanation": {
            "correct": "Encryption keeps data unreadable to unauthorized parties, so its primary goal is "
                       "confidentiality; hashing, by contrast, is used to verify integrity.",
            "exam_pattern": "Encryption -> confidentiality; hashing -> integrity.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 5 - Encryption basics (confidentiality vs. integrity)"],
    },
]
