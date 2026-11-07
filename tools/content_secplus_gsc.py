"""CompTIA Security+ SY0-701 expansion pool — Domain 1.0 General Security Concepts.

Original, objective-aligned items that DEEPEN the base `general_security_concepts`
set in content_secplus.py (ids secplus-gsc-001..006). These start at id 101 so they
never collide with the base pool, and they deliberately take NEW angles/scenarios:
control TYPE vs CATEGORY traps (compensating/directive/deterrent, operational), the
AAA split (authorization/accounting) and CIA integrity, the Zero Trust control-plane
roles beyond the Policy Engine (Policy Administrator, adaptive identity, implicit
trust), physical controls (vestibule, bollards, IR/microwave/pressure sensors),
change management (backout plan, impact analysis, version control), cryptography
(Diffie-Hellman, perfect forward secrecy, TPM vs HSM, salting + key stretching,
steganography) and PKI (CSR, chain of trust, OCSP stapling, wildcard vs SAN).

Same authoring rules as the other pools: original content mapped to the public exam
objectives, never real exam items. build_content.py shuffles option order, so the
answer key here is not positionally biased.
"""

QUESTIONS = [
    # ===== security_controls ================================================
    {
        "id": "secplus-gsc-101", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A security policy requires multifactor authentication on every application, "
                "but a critical legacy system cannot support MFA. As an approved alternative, "
                "the team restricts that system to a hardened jump host on an isolated network "
                "segment and logs all access. Which control TYPE best describes this arrangement?",
        "options": [
            {"id": "A", "text": "Compensating"},
            {"id": "B", "text": "Preventive"},
            {"id": "C", "text": "Corrective"},
            {"id": "D", "text": "Directive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A compensating control is an alternative measure put in place to satisfy "
                       "the intent of a required control that cannot be implemented as specified — "
                       "here, standing in for the mandated MFA on a system that can't do it.",
            "distractors": {
                "B": "The measure does reduce risk, but the defining point is that it SUBSTITUTES for "
                     "a required control (MFA) that cannot be implemented — that is a compensating control.",
                "C": "Corrective controls act after an incident to restore operations; nothing here is "
                     "responding to or repairing an incident.",
                "D": "Directive controls instruct people what to do through policy; this is a technical "
                     "substitute, not an instruction to personnel.",
            },
            "exam_pattern": "Compensating = an alternative that meets the intent of a required control "
                            "you cannot implement as written (e.g., legacy system can't do MFA).",
        },
    },
    {
        "id": "secplus-gsc-102", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "An organization publishes an acceptable use policy that requires employees to label "
                "every new document with its data classification. Considered as a security control, "
                "the policy's instruction is which control TYPE?",
        "options": [
            {"id": "A", "text": "Directive"},
            {"id": "B", "text": "Managerial"},
            {"id": "C", "text": "Preventive"},
            {"id": "D", "text": "Detective"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A directive control tells people what they must do — policies, procedures, and "
                       "standards that mandate behavior (such as classifying/labeling documents) are directive.",
            "distractors": {
                "B": "Managerial is a control CATEGORY (policies, risk planning), not a control TYPE; the "
                     "question specifically asks for the TYPE — a classic category-vs-type trap.",
                "C": "Preventive controls actively stop an action from occurring; a policy that instructs "
                     "behavior directs rather than technically enforces it.",
                "D": "Detective controls identify incidents after they happen; a labeling instruction "
                     "detects nothing.",
            },
            "exam_pattern": "CATEGORY (technical/managerial/operational/physical) vs TYPE "
                            "(preventive/deterrent/detective/corrective/compensating/directive). A policy "
                            "that mandates behavior is a DIRECTIVE control.",
        },
    },
    {
        "id": "secplus-gsc-103", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 1, "type": "mcq",
        "stem": "A company mounts large signs at its perimeter reading 'Area under 24/7 recorded video "
                "surveillance' mainly to discourage trespassers from attempting entry. The SIGN itself "
                "is which control TYPE?",
        "options": [
            {"id": "A", "text": "Deterrent"},
            {"id": "B", "text": "Detective"},
            {"id": "C", "text": "Preventive"},
            {"id": "D", "text": "Compensating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A deterrent control discourages an attacker from acting. A warning sign relies on "
                       "psychological discouragement, so it is a deterrent.",
            "distractors": {
                "B": "The cameras that record and later help identify an intruder are detective; the sign's "
                     "job is to discourage, which is deterrent.",
                "C": "A sign does not physically stop entry — it only discourages — so it is not preventive.",
                "D": "A compensating control substitutes for a missing required control; the sign is not "
                     "standing in for anything.",
            },
            "exam_pattern": "Deterrent = discourages (signs, warning banners, visible guards/cameras). "
                            "Detective = records/identifies. Preventive = physically blocks.",
        },
    },

    # ===== cia_aaa ==========================================================
    {
        "id": "secplus-gsc-104", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 2, "type": "mcq",
        "stem": "A user has just proven their identity with a password and a hardware token. The system "
                "now checks the user's group membership to decide whether they may open the finance "
                "folder. Which AAA function is this check?",
        "options": [
            {"id": "A", "text": "Authorization"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Accounting"},
            {"id": "D", "text": "Identification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authorization determines what an already-authenticated user is permitted to do — "
                       "here, whether their group may open the finance folder.",
            "distractors": {
                "B": "Authentication already happened when the password and token proved who the user is; "
                     "this step decides what they may access.",
                "C": "Accounting records what the user does once access is granted; it is not the "
                     "permission decision.",
                "D": "Identification is merely claiming an identity (e.g., entering a username); it "
                     "precedes authentication.",
            },
            "exam_pattern": "Identify (claim) -> Authenticate (prove) -> Authorize (what you may do) -> "
                            "Account (record what you did).",
        },
    },
    {
        "id": "secplus-gsc-105", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 1, "type": "mcq",
        "stem": "A file is downloaded, and the recipient computes its SHA-256 hash and compares it to the "
                "hash published by the source. The values match. Which security goal has this MOST "
                "directly verified?",
        "options": [
            {"id": "A", "text": "Integrity"},
            {"id": "B", "text": "Confidentiality"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A matching hash shows the file was not altered in transit — that is integrity, the "
                       "assurance that data has not been modified.",
            "distractors": {
                "B": "Confidentiality means keeping data secret; a hash comparison reveals nothing about "
                     "secrecy, and the file was not encrypted here.",
                "C": "Availability concerns whether data/systems are accessible when needed, not whether "
                     "content changed.",
                "D": "Non-repudiation requires a key-based signature binding an identity to the data; a bare "
                     "hash anyone can recompute does not prove origin.",
            },
            "exam_pattern": "Hash match = INTEGRITY (data unchanged). Add a private-key signature to also "
                            "get authenticity/non-repudiation.",
        },
    },
    {
        "id": "secplus-gsc-106", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 2, "type": "mcq",
        "stem": "To satisfy an audit, a manager must produce a record of exactly which administrator "
                "changed each firewall rule and when, so individuals can be held accountable. Which AAA "
                "component supplies this?",
        "options": [
            {"id": "A", "text": "Accounting"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "Availability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Accounting is the logging/audit-trail function of AAA — it records what an "
                       "authenticated, authorized user actually did (who, what, when) for accountability.",
            "distractors": {
                "B": "Authentication verifies identity at login; by itself it does not produce the ongoing "
                     "record of actions.",
                "C": "Authorization grants or denies access rights; it is not the log of what was done.",
                "D": "Availability is a CIA property about uptime/access — it is not one of the AAA "
                     "functions at all.",
            },
            "exam_pattern": "Accounting (the third A) = the audit trail of actions. Distinguish from "
                            "authentication (prove identity) and authorization (grant rights).",
        },
    },

    # ===== zero_trust =======================================================
    {
        "id": "secplus-gsc-107", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "A Zero Trust system evaluates contextual signals for each access attempt — device "
                "posture, geolocation, time of day, and behavior — and raises authentication requirements "
                "(for example, a step-up MFA prompt) when the risk looks higher. Which Zero Trust concept "
                "is this?",
        "options": [
            {"id": "A", "text": "Adaptive identity"},
            {"id": "B", "text": "Implicit trust zones"},
            {"id": "C", "text": "Threat scope reduction"},
            {"id": "D", "text": "Policy-driven access control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Adaptive identity means authentication strength adjusts dynamically to real-time "
                       "context and risk rather than being a one-time static check.",
            "distractors": {
                "B": "Implicit trust zones are areas where traffic is trusted once inside; Zero Trust aims "
                     "to SHRINK these, and the term does not describe risk-based authentication.",
                "C": "Threat scope reduction limits the blast radius of a compromise (least privilege, "
                     "segmentation); it is not about varying authentication.",
                "D": "Policy-driven access control means access is governed by centralized policy; adaptive "
                     "identity is the specific idea of auth strength varying with context/risk.",
            },
            "exam_pattern": "Adaptive identity = authentication that tightens or relaxes based on real-time "
                            "risk/context signals, not a static trust decision.",
        },
    },
    {
        "id": "secplus-gsc-108", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "zero_trust", "difficulty": 2, "type": "mcq",
        "stem": "In the Zero Trust control plane, after a decision is made, which component actually "
                "establishes and later tears down the communication path and generates any "
                "session-specific credentials, then configures the enforcement point to allow it?",
        "options": [
            {"id": "A", "text": "Policy Administrator"},
            {"id": "B", "text": "Policy Engine"},
            {"id": "C", "text": "Policy Enforcement Point"},
            {"id": "D", "text": "The subject (requesting user/device)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Policy Administrator executes the Policy Engine's decision — it sets up or tears "
                       "down the session, issues any session credentials/tokens, and instructs the PEP.",
            "distractors": {
                "B": "The Policy Engine DECIDES grant or deny based on policy; it does not itself open or "
                     "close the connection.",
                "C": "The Policy Enforcement Point sits in the data plane and allows/monitors/blocks the "
                     "session as instructed — it enforces, it does not administer.",
                "D": "The subject is the user or device requesting access, not a control-plane component.",
            },
            "exam_pattern": "Policy Engine DECIDES; Policy Administrator EXECUTES (sets up/tears down "
                            "sessions, issues credentials); PEP ENFORCES in the data plane.",
        },
    },
    {
        "id": "secplus-gsc-109", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "zero_trust", "difficulty": 2, "type": "mcq",
        "stem": "A traditional 'castle-and-moat' network trusts any device once it is inside the "
                "perimeter. Which Zero Trust principle MOST directly rejects this model?",
        "options": [
            {"id": "A", "text": "Implicit trust is removed; every request is authenticated and authorized "
                               "regardless of the requester's network location"},
            {"id": "B", "text": "Any device located inside the corporate LAN is automatically trusted"},
            {"id": "C", "text": "A strong perimeter firewall is sufficient to establish trust for internal "
                               "traffic"},
            {"id": "D", "text": "Once a remote user completes VPN login, they receive full, unrestricted "
                               "network access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Zero Trust's core tenet is 'never trust, always verify' — no request is trusted "
                       "based on network location; each is authenticated and authorized on its own.",
            "distractors": {
                "B": "Automatically trusting inside-LAN devices IS the implicit-trust model Zero Trust "
                     "eliminates.",
                "C": "Relying on a perimeter firewall for internal trust is the castle-and-moat assumption "
                     "Zero Trust rejects.",
                "D": "Granting broad access after a single VPN login is exactly the implicit trust Zero "
                     "Trust avoids; access stays least-privilege and continuously verified.",
            },
            "exam_pattern": "Zero Trust = never trust, always verify. Location on the network grants no "
                            "implicit trust; verify every request.",
        },
    },

    # ===== physical_security ================================================
    {
        "id": "secplus-gsc-110", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "physical_security", "difficulty": 1, "type": "mcq",
        "stem": "To stop an unauthorized person from slipping in behind an employee (tailgating), a "
                "facility builds a small two-door chamber: the outer door must close and the person must "
                "authenticate before the inner door will open, admitting one person at a time. What is "
                "this?",
        "options": [
            {"id": "A", "text": "Access control vestibule (mantrap)"},
            {"id": "B", "text": "Bollard"},
            {"id": "C", "text": "Faraday cage"},
            {"id": "D", "text": "Proximity card reader"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An access control vestibule (mantrap) uses two interlocking doors so only one "
                       "authenticated person passes at a time, defeating tailgating/piggybacking.",
            "distractors": {
                "B": "A bollard is a post that blocks vehicles; it does nothing about people tailgating "
                     "through a door.",
                "C": "A Faraday cage blocks radio/electromagnetic signals; it is not an entry-control "
                     "structure.",
                "D": "A card reader authenticates a person but by itself does not physically prevent a "
                     "second person from following through the door.",
            },
            "exam_pattern": "Access control vestibule (mantrap) = two interlocking doors admitting one "
                            "authenticated person at a time -> defeats tailgating.",
        },
    },
    {
        "id": "secplus-gsc-111", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "physical_security", "difficulty": 2, "type": "mcq",
        "stem": "A ground-floor data center with a glass lobby wants to prevent an attacker from driving "
                "a vehicle through the entrance (a ram-raid). Which physical control MOST directly "
                "addresses this?",
        "options": [
            {"id": "A", "text": "Bollards"},
            {"id": "B", "text": "Access control vestibule"},
            {"id": "C", "text": "Motion-activated lighting"},
            {"id": "D", "text": "A security guard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bollards are sturdy short posts installed to stop vehicles from ramming or "
                       "approaching a building — the standard anti-ram-raid control.",
            "distractors": {
                "B": "A vestibule controls people entering on foot; it is not built to stop a moving "
                     "vehicle.",
                "C": "Lighting deters and aids detection at night but will not physically stop a vehicle.",
                "D": "A guard controls and observes access but cannot physically halt a vehicle driven at "
                     "the building.",
            },
            "exam_pattern": "Bollards = posts that physically block vehicles (ram-raids / vehicle-borne "
                            "threats). Vestibules handle people, not cars.",
        },
    },
    {
        "id": "secplus-gsc-112", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "physical_security", "difficulty": 2, "type": "mcq",
        "stem": "A secure, unlit server room must detect an intruder at night specifically by sensing the "
                "body heat they emit. Which sensor type is designed for this?",
        "options": [
            {"id": "A", "text": "Infrared sensor"},
            {"id": "B", "text": "Pressure sensor"},
            {"id": "C", "text": "Microwave sensor"},
            {"id": "D", "text": "Ultrasonic sensor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A passive infrared (PIR) sensor detects the infrared heat radiated by a human body, "
                       "making it ideal for sensing a person in a dark room.",
            "distractors": {
                "B": "A pressure sensor triggers on weight/force applied to a floor mat or surface, not on "
                     "heat.",
                "C": "A microwave sensor emits microwaves and detects movement from the reflected signal "
                     "(Doppler); it senses motion, not body heat.",
                "D": "An ultrasonic sensor uses high-frequency sound waves to detect movement, not thermal "
                     "emissions.",
            },
            "exam_pattern": "Infrared (PIR) = body heat. Microwave/ultrasonic = motion via emitted waves. "
                            "Pressure = weight/contact.",
        },
    },

    # ===== change_management ================================================
    {
        "id": "secplus-gsc-113", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "change_management", "difficulty": 2, "type": "mcq",
        "stem": "A change ticket for a core-router firmware upgrade includes a documented, tested "
                "procedure to restore the previous firmware image quickly if the upgrade causes problems. "
                "What is this element of the change called?",
        "options": [
            {"id": "A", "text": "Backout plan"},
            {"id": "B", "text": "Impact analysis"},
            {"id": "C", "text": "Maintenance window"},
            {"id": "D", "text": "Test plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A backout (rollback) plan is the predefined set of steps to return to the last "
                       "known-good state if a change fails — here, restoring the prior firmware.",
            "distractors": {
                "B": "Impact analysis assesses what a change could affect BEFORE approval; it is not the "
                     "revert procedure.",
                "C": "The maintenance window is WHEN the change runs, not HOW to undo it.",
                "D": "A test plan validates that the change works (often in a lab); the revert steps are a "
                     "separate deliverable.",
            },
            "exam_pattern": "Backout/rollback plan = how to revert to the last good state if a change goes "
                            "wrong. Prepared BEFORE implementation.",
        },
    },
    {
        "id": "secplus-gsc-114", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "change_management", "difficulty": 2, "type": "mcq",
        "stem": "A change advisory board will not approve any proposed change until the submitter "
                "documents which systems, services, and users it could affect and the risk if it fails. "
                "Which change-management step is this?",
        "options": [
            {"id": "A", "text": "Impact analysis"},
            {"id": "B", "text": "Backout plan"},
            {"id": "C", "text": "Maintenance window"},
            {"id": "D", "text": "Standard operating procedure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Impact analysis is the up-front evaluation of a change's scope, dependencies, and "
                       "risk — what it affects and what happens if it fails — done before approval.",
            "distractors": {
                "B": "The backout plan is the revert procedure, not the assessment of what is affected.",
                "C": "A maintenance window is the scheduled implementation time slot, not an analysis of "
                     "consequences.",
                "D": "An SOP is a repeatable documented process; here the board specifically wants an "
                     "assessment of scope and risk.",
            },
            "exam_pattern": "Impact analysis = evaluate scope, dependencies, and risk of a change BEFORE "
                            "it is approved/implemented.",
        },
    },
    {
        "id": "secplus-gsc-115", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "change_management", "difficulty": 2, "type": "mcq",
        "stem": "After a firewall rule set is changed, the team commits the new configuration file to a "
                "repository that records every revision with its author and timestamp, letting them "
                "compare revisions and revert to an exact earlier one. Which change-management practice is "
                "this?",
        "options": [
            {"id": "A", "text": "Version control"},
            {"id": "B", "text": "Impact analysis"},
            {"id": "C", "text": "Maintenance window"},
            {"id": "D", "text": "Backout plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Version control systematically tracks successive revisions of configs/documents "
                       "(author, time, diff), making changes auditable and precisely reversible.",
            "distractors": {
                "B": "Impact analysis is the pre-change risk/scope assessment, not revision tracking of the "
                     "config.",
                "C": "A maintenance window is the scheduled implementation time, unrelated to tracking file "
                     "revisions.",
                "D": "A backout plan describes how to revert one specific change; version control is the "
                     "ongoing system that records all revisions and makes such reverts precise.",
            },
            "exam_pattern": "Version control = track every revision of configs/docs so changes are "
                            "auditable and reversible.",
        },
    },

    # ===== cryptographic_solutions ==========================================
    {
        "id": "secplus-gsc-116", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 2, "type": "mcq",
        "stem": "Two parties on an insecure network need to agree on a shared symmetric key without ever "
                "transmitting the key itself across the wire. Which method accomplishes this?",
        "options": [
            {"id": "A", "text": "Diffie-Hellman key exchange"},
            {"id": "B", "text": "SHA-256"},
            {"id": "C", "text": "AES"},
            {"id": "D", "text": "Steganography"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Diffie-Hellman lets both sides independently derive the same shared secret over a "
                       "public channel without the secret ever being sent.",
            "distractors": {
                "B": "SHA-256 is a one-way hash for integrity; it neither establishes nor transports a key.",
                "C": "AES is a symmetric cipher that USES a shared key to encrypt data; it does not "
                     "negotiate the key over an insecure channel.",
                "D": "Steganography conceals data within other media; it has nothing to do with key "
                     "agreement.",
            },
            "exam_pattern": "Diffie-Hellman (and ECDHE) = derive a shared secret over a public channel "
                            "without sending the key; it underpins perfect forward secrecy.",
        },
    },
    {
        "id": "secplus-gsc-117", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 3, "type": "mcq",
        "stem": "A security architect wants to ensure that if a web server's long-term private key is "
                "ever stolen, an attacker who recorded past TLS sessions still cannot decrypt them. Which "
                "property provides this?",
        "options": [
            {"id": "A", "text": "Perfect forward secrecy"},
            {"id": "B", "text": "Key escrow"},
            {"id": "C", "text": "Full-disk encryption"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Perfect forward secrecy uses a unique ephemeral key per session (e.g., ECDHE), so "
                       "compromising the server's long-term private key cannot retroactively decrypt earlier "
                       "recorded sessions.",
            "distractors": {
                "B": "Key escrow intentionally stores copies of keys for recovery; it increases exposure of "
                     "past data if those keys leak — the opposite of the goal.",
                "C": "Full-disk encryption protects data at rest on a device; it is irrelevant to "
                     "decrypting previously captured network sessions.",
                "D": "Non-repudiation proves who performed an action; it does not protect the "
                     "confidentiality of past sessions.",
            },
            "exam_pattern": "PFS = ephemeral per-session keys, so one stolen long-term key can't decrypt "
                            "recorded past sessions.",
        },
    },
    {
        "id": "secplus-gsc-118", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 2, "type": "mcq",
        "stem": "A laptop needs a dedicated chip soldered to its motherboard to securely store the "
                "BitLocker full-disk-encryption keys and to measure and attest the integrity of the boot "
                "process for that single device. Which component is this?",
        "options": [
            {"id": "A", "text": "TPM (Trusted Platform Module)"},
            {"id": "B", "text": "HSM (Hardware Security Module)"},
            {"id": "C", "text": "KMS (Key Management Service)"},
            {"id": "D", "text": "Secure enclave"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A TPM is the discrete chip on a device's motherboard that stores keys (e.g., "
                       "BitLocker) and measures boot integrity for that one machine.",
            "distractors": {
                "B": "An HSM is a dedicated, often network-attached or plug-in appliance for high-volume key "
                     "generation/storage across many servers — not the on-board chip tied to one device's "
                     "boot.",
                "C": "A KMS is software/cloud tooling that manages key lifecycle; it is not the physical "
                     "motherboard chip verifying this laptop's boot.",
                "D": "A secure enclave is an isolated coprocessor (common in smartphones / Apple silicon) "
                     "for protecting keys and biometrics; the standard PC-motherboard chip for BitLocker and "
                     "boot attestation is specifically the TPM.",
            },
            "exam_pattern": "TPM = per-device motherboard chip (disk keys, boot integrity). HSM = dedicated "
                            "high-volume key appliance. KMS = key-management service. Secure enclave = "
                            "mobile/SoC coprocessor.",
        },
    },
    {
        "id": "secplus-gsc-119", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 2, "type": "multi",
        "stem": "A developer must store user passwords so that, even if the hash database is stolen, the "
                "hashes resist offline brute-force and precomputed (rainbow table) attacks. Which TWO "
                "techniques should be applied together? (Choose two.)",
        "options": [
            {"id": "A", "text": "Add a unique random salt to each password before hashing"},
            {"id": "B", "text": "Use a key-stretching algorithm such as PBKDF2 or bcrypt"},
            {"id": "C", "text": "Encode the passwords with Base64 before storing them"},
            {"id": "D", "text": "Store a single-pass, unsalted MD5 hash"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A unique salt defeats precomputed rainbow tables and ensures identical passwords "
                       "hash differently; key stretching (PBKDF2/bcrypt/scrypt/Argon2) deliberately makes "
                       "each guess computationally expensive. Together they harden stored hashes.",
            "distractors": {
                "C": "Base64 is reversible encoding, not a security control — it provides no protection to "
                     "stored hashes.",
                "D": "A single-pass, unsalted MD5 hash is fast to compute and highly vulnerable to rainbow "
                     "tables and brute force.",
            },
            "exam_pattern": "Salt (unique per password) defeats rainbow tables; key stretching multiplies "
                            "the cost of each guess. Use BOTH for password storage.",
        },
    },
    {
        "id": "secplus-gsc-120", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 2, "type": "mcq",
        "stem": "An insider hides a confidential spreadsheet's contents inside the pixels of an "
                "ordinary-looking image file so that the data's very existence is concealed. Which "
                "technique is this?",
        "options": [
            {"id": "A", "text": "Steganography"},
            {"id": "B", "text": "Encryption"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Tokenization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Steganography conceals data WITHIN other data (such as an image) so that an "
                       "observer does not even know hidden data is present.",
            "distractors": {
                "B": "Encryption scrambles the data's meaning, but the encrypted file's existence is still "
                     "obvious; steganography hides that anything is there.",
                "C": "Hashing is a one-way integrity function; it cannot carry or hide the original data for "
                     "later recovery.",
                "D": "Tokenization replaces sensitive values with surrogate tokens inside a system; it does "
                     "not embed data inside an image.",
            },
            "exam_pattern": "Steganography = hide data within other media (image/audio/video) so its "
                            "presence is hidden; encryption hides meaning, not existence.",
        },
    },

    # ===== pki ==============================================================
    {
        "id": "secplus-gsc-121", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "mcq",
        "stem": "An admin generates a key pair on a web server, then creates a file containing the "
                "server's public key and identifying details (common name, organization) and submits it "
                "to a CA to be signed. What is this file?",
        "options": [
            {"id": "A", "text": "Certificate signing request (CSR)"},
            {"id": "B", "text": "Certificate revocation list (CRL)"},
            {"id": "C", "text": "Root certificate"},
            {"id": "D", "text": "The server's private key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CSR contains the subject's public key plus identifying information and is sent to "
                       "the CA, which signs it to produce the certificate.",
            "distractors": {
                "B": "A CRL is a list of revoked certificates published by the CA — not something you submit "
                     "to request a certificate.",
                "C": "A root certificate is the CA's own self-signed trust anchor; the admin does not create "
                     "it to request a server certificate.",
                "D": "The private key must never leave the server or be sent to the CA; only the public key "
                     "(inside the CSR) is submitted.",
            },
            "exam_pattern": "CSR carries the PUBLIC key + identity to the CA for signing; the matching "
                            "PRIVATE key stays secret on the server.",
        },
    },
    {
        "id": "secplus-gsc-122", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 3, "type": "mcq",
        "stem": "A browser trusts a website's certificate because it was signed by an intermediate CA, "
                "which was in turn signed by a root CA already present in the browser's trust store. What "
                "is this root-to-leaf validation path called?",
        "options": [
            {"id": "A", "text": "Certificate chaining (chain of trust)"},
            {"id": "B", "text": "Key escrow"},
            {"id": "C", "text": "Certificate pinning"},
            {"id": "D", "text": "A self-signed certificate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Certificate chaining (the chain of trust) links the leaf certificate to an "
                       "intermediate CA and up to a trusted root, letting the client validate it.",
            "distractors": {
                "B": "Key escrow is the storage of key copies for recovery; it is unrelated to how trust is "
                     "validated.",
                "C": "Certificate pinning hardcodes an expected certificate or public key in an app to "
                     "resist fraudulent certs; it is not the normal root-to-leaf validation path.",
                "D": "A self-signed certificate is signed by its own key with no external CA, so it forms no "
                     "external chain and is not trusted by default.",
            },
            "exam_pattern": "Chain of trust = leaf -> intermediate CA -> trusted root. Roots stay offline; "
                            "intermediates do day-to-day issuing.",
        },
    },
    {
        "id": "secplus-gsc-123", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "mcq",
        "stem": "To cut client-side revocation lookups and improve privacy and performance, a web server "
                "periodically obtains a CA-signed, time-stamped status for its own certificate and "
                "attaches it directly to the TLS handshake it sends to clients. What is this technique?",
        "options": [
            {"id": "A", "text": "OCSP stapling"},
            {"id": "B", "text": "A CRL distribution point"},
            {"id": "C", "text": "Key escrow"},
            {"id": "D", "text": "Certificate pinning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With OCSP stapling, the server fetches a CA-signed OCSP response and 'staples' it to "
                       "its TLS handshake, so each client does not have to query the CA itself.",
            "distractors": {
                "B": "A CRL distribution point only tells clients where to download the full revocation "
                     "list; the client still does the fetching, unlike stapling.",
                "C": "Key escrow is recovery storage of keys; it has nothing to do with delivering "
                     "revocation status.",
                "D": "Certificate pinning binds a client to an expected cert/key; it does not deliver "
                     "revocation status in the handshake.",
            },
            "exam_pattern": "OCSP stapling: the SERVER obtains and attaches the signed status to the "
                            "handshake, sparing each client its own OCSP query.",
        },
    },
    {
        "id": "secplus-gsc-124", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "multi",
        "stem": "An organization needs a single certificate to secure three hostnames: www.example.com, "
                "mail.example.com, and shop.example.com. Which certificate options could satisfy this "
                "requirement? (Choose two.)",
        "options": [
            {"id": "A", "text": "A wildcard certificate for *.example.com"},
            {"id": "B", "text": "A Subject Alternative Name (SAN) certificate listing all three hostnames"},
            {"id": "C", "text": "A self-signed certificate issued for www.example.com"},
            {"id": "D", "text": "A single-domain certificate (one FQDN per CSR)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A wildcard certificate (*.example.com) matches all first-level subdomains of "
                       "example.com, covering www, mail, and shop; a SAN (multi-domain) certificate can "
                       "explicitly list several specific hostnames in one cert.",
            "distractors": {
                "C": "A self-signed certificate for www.example.com covers only that one name and is not "
                     "trusted by clients by default.",
                "D": "A single-domain certificate secures just one FQDN, so it cannot cover all three "
                     "hostnames at once.",
            },
            "exam_pattern": "Wildcard (*.domain) secures many subdomains at one level; SAN cert lists "
                            "multiple specific FQDNs (even across different domains).",
        },
    },
]
