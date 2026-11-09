"""(ISC)² CISSP pool - Domain 3: Security Architecture and Engineering.

Original, CBK-aligned practice items for the five Security Architecture and
Engineering subtopics:
  * cissp_security_models        - Bell-LaPadula, Biba, Clark-Wilson, Brewer-Nash
                                   and their read/write rules.
  * cissp_crypto                 - symmetric vs asymmetric, digital signatures,
                                   key usage for confidentiality, non-repudiation,
                                   and key exchange.
  * cissp_security_capabilities  - reference monitor, security kernel, TCB, TPM.
  * cissp_vuln_architectures     - TOCTOU race conditions, inference/aggregation,
                                   maintenance hooks/backdoors.
  * cissp_physical_security      - fire suppression, electrical power anomalies,
                                   and access control vestibules (mantraps).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Model read/write rules and cryptographic key usage were
verified against the CBK; items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_security_models ============================================
    {
        "id": "cissp-arch-001", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 2, "type": "mcq",
        "stem": "A multilevel secure system must prevent a user cleared only for Confidential data from "
                "reading Top Secret files, and must prevent a Top Secret process from writing data down "
                "into a Confidential file. Which model and properties enforce this?",
        "options": [
            {"id": "A", "text": "Biba, using no-read-down and no-write-up"},
            {"id": "B", "text": "Clark-Wilson, using well-formed transactions"},
            {"id": "C", "text": "Bell-LaPadula: no-read-up (simple security property) and no-write-down (* property)"},
            {"id": "D", "text": "Brewer-Nash, using dynamic conflict-of-interest rules"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Bell-LaPadula protects confidentiality. Its simple security property is 'no read up' "
                       "and its * (star) property is 'no write down', which exactly matches the requirement.",
            "distractors": {
                "A": "Biba protects integrity using the opposite rules (no read down, no write up), not confidentiality.",
                "B": "Clark-Wilson enforces integrity through transactions; it does not address multilevel "
                     "confidentiality clearances.",
                "D": "Brewer-Nash addresses conflicts of interest, not clearance-based read/write restrictions.",
            },
            "exam_pattern": "Bell-LaPadula = confidentiality; simple property = no read up, star (*) property = no write down.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Bell-LaPadula model"],
    },
    {
        "id": "cissp-arch-002", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 2, "type": "mcq",
        "stem": "A system must protect data integrity by ensuring a low-integrity process cannot corrupt "
                "high-integrity data, and that a high-integrity subject does not read lower-integrity "
                "(less trustworthy) data. Which model enforces this?",
        "options": [
            {"id": "A", "text": "Biba: simple integrity property (no read down) and * integrity property (no write up)"},
            {"id": "B", "text": "Bell-LaPadula, using no read up and no write down"},
            {"id": "C", "text": "Take-Grant protection model"},
            {"id": "D", "text": "Graham-Denning model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Biba protects integrity. Its simple integrity property is 'no read down' and its * "
                       "integrity property is 'no write up', preventing contamination of trusted data.",
            "distractors": {
                "B": "Bell-LaPadula protects confidentiality with the opposite read/write rules, not integrity.",
                "C": "Take-Grant models how access rights are transferred between subjects, not integrity flow.",
                "D": "Graham-Denning defines primitive rights-management operations, not these integrity axioms.",
            },
            "exam_pattern": "Biba = integrity; simple = no read down, star (*) = no write up (the opposite of Bell-LaPadula).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Biba model"],
    },
    {
        "id": "cissp-arch-003", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 3, "type": "mcq",
        "stem": "A commercial integrity model requires that users never manipulate critical data directly "
                "but only through validated programs, and it enforces separation of duties. Which model is "
                "described, and what is its core construct?",
        "options": [
            {"id": "A", "text": "Bell-LaPadula, using security labels"},
            {"id": "B", "text": "Biba, using integrity levels"},
            {"id": "C", "text": "Brewer-Nash, using conflict classes"},
            {"id": "D", "text": "Clark-Wilson, using the access control triple (subject - program/TP - object)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Clark-Wilson is a commercial integrity model built on well-formed transactions and "
                       "the access control triple (subject accesses a constrained data item only through a "
                       "transformation procedure), enforcing separation of duties.",
            "distractors": {
                "A": "Bell-LaPadula is a confidentiality model using labels, not a transaction-integrity model.",
                "B": "Biba enforces integrity with lattice levels but not the program-mediated transaction triple.",
                "C": "Brewer-Nash handles conflicts of interest, not well-formed transactions.",
            },
            "exam_pattern": "Clark-Wilson = commercial integrity via well-formed transactions and the access "
                            "triple (subject → TP → CDI).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Clark-Wilson model"],
    },
    {
        "id": "cissp-arch-004", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 2, "type": "mcq",
        "stem": "A consulting firm's analyst who has accessed files for one client must then be "
                "automatically blocked from accessing data belonging to a competing client, with "
                "permissions changing based on what the analyst has already viewed. Which model addresses "
                "this?",
        "options": [
            {"id": "A", "text": "Bell-LaPadula model"},
            {"id": "B", "text": "Brewer-Nash (Chinese Wall) model"},
            {"id": "C", "text": "Biba model"},
            {"id": "D", "text": "Clark-Wilson model"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Brewer-Nash (Chinese Wall) model dynamically changes a subject's access rights "
                       "based on prior access, specifically to prevent conflicts of interest.",
            "distractors": {
                "A": "Bell-LaPadula enforces confidentiality by fixed clearance levels, not dynamic "
                     "conflict-of-interest rules.",
                "C": "Biba is an integrity model and does not address conflicts of interest.",
                "D": "Clark-Wilson enforces transaction integrity, not conflict-of-interest separation.",
            },
            "exam_pattern": "Brewer-Nash (Chinese Wall) dynamically prevents conflicts of interest based on prior access.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Brewer-Nash model"],
    },

    # ===== cissp_crypto =====================================================
    {
        "id": "cissp-arch-005", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "mcq",
        "stem": "A business requires that the sender of an electronic contract cannot later deny having "
                "sent it. Which cryptographic capability provides this, and what kind of cryptography does "
                "it require?",
        "options": [
            {"id": "A", "text": "A message authentication code (MAC) using a shared symmetric key"},
            {"id": "B", "text": "Symmetric encryption with AES"},
            {"id": "C", "text": "A digital signature using asymmetric (public-key) cryptography"},
            {"id": "D", "text": "A one-way hash of the message alone"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Non-repudiation requires a digital signature produced with the sender's private key; "
                       "because only the sender holds that key, they cannot credibly deny the signature.",
            "distractors": {
                "A": "A MAC uses a shared symmetric key, so either party could have produced it - no non-repudiation.",
                "B": "Symmetric encryption provides confidentiality, not proof of a specific sender.",
                "D": "A hash alone provides integrity but cannot bind the message to a particular signer.",
            },
            "exam_pattern": "Non-repudiation requires asymmetric digital signatures (private-key signing), not "
                            "symmetric MACs or hashes.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Non-repudiation and digital signatures"],
    },
    {
        "id": "cissp-arch-006", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 3, "type": "mcq",
        "stem": "To digitally sign a document, which key does the sender use, and what assurance does the "
                "signature itself provide?",
        "options": [
            {"id": "A", "text": "The sender's private key; it provides integrity, origin authentication, and non-repudiation (but not confidentiality)"},
            {"id": "B", "text": "The recipient's public key; it provides confidentiality"},
            {"id": "C", "text": "The sender's public key; it provides confidentiality and integrity"},
            {"id": "D", "text": "The recipient's private key; it provides non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The sender signs (encrypts the message hash) with their own private key; anyone can "
                       "verify it with the sender's public key. This gives integrity, origin authentication, "
                       "and non-repudiation, but it does not conceal the message (no confidentiality).",
            "distractors": {
                "B": "Encrypting with the recipient's public key provides confidentiality, not a signature.",
                "C": "The sender cannot sign with a public key (everyone has it); this confuses signing with "
                     "encryption.",
                "D": "The sender never possesses the recipient's private key.",
            },
            "exam_pattern": "Sign with your private key (verify with your public key): integrity + authentication "
                            "+ non-repudiation; signing is not confidentiality.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Digital signatures"],
    },
    {
        "id": "cissp-arch-007", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "mcq",
        "stem": "Alice wants to send Bob a message that only Bob can read. Using public-key cryptography, "
                "which key should Alice use to encrypt the message?",
        "options": [
            {"id": "A", "text": "Alice's private key"},
            {"id": "B", "text": "Bob's public key"},
            {"id": "C", "text": "Alice's public key"},
            {"id": "D", "text": "Bob's private key"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "For confidentiality, Alice encrypts with Bob's public key; only Bob's matching "
                       "private key can decrypt it, so only Bob can read the message.",
            "distractors": {
                "A": "Encrypting with Alice's private key is signing; anyone with her public key could decrypt it.",
                "C": "Data encrypted with Alice's public key can only be decrypted by Alice's private key, not Bob's.",
                "D": "Alice does not have Bob's private key, and senders never use the recipient's private key.",
            },
            "exam_pattern": "Confidentiality to a recipient = encrypt with the recipient's public key; only their "
                            "private key decrypts.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Asymmetric key usage"],
    },
    {
        "id": "cissp-arch-008", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The asymmetric method designed specifically to let two parties "
                "establish a shared secret key over an insecure channel, without transmitting the key "
                "itself, is the ________ key-exchange algorithm.",
        "correct": ["diffie-hellman", "diffie hellman", "dh", "diffiehellman"],
        "explanation": {
            "correct": "Diffie-Hellman is a key-agreement algorithm that lets two parties derive a shared "
                       "secret over an insecure channel without sending the secret itself.",
            "exam_pattern": "Diffie-Hellman = key agreement/exchange (not bulk encryption); authenticate it to "
                            "resist man-in-the-middle.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Key exchange (Diffie-Hellman)"],
    },

    {
        "id": "cissp-arch-018", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The unique random value added to a password before it is hashed - so "
                "that identical passwords produce different hashes and precomputed rainbow-table attacks "
                "are defeated - is called a ________.",
        "correct": ["salt"],
        "explanation": {
            "correct": "A salt is unique random data concatenated with a password before hashing, making each "
                       "stored hash unique and defeating precomputed (rainbow-table) attacks.",
            "exam_pattern": "Salt = random per-password value added before hashing; it defeats rainbow tables "
                            "(pair with a slow KDF such as bcrypt/PBKDF2).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Password hashing and salting"],
    },

    # ===== cissp_security_capabilities ======================================
    {
        "id": "cissp-arch-009", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_capabilities", "difficulty": 3, "type": "mcq",
        "stem": "A security evaluation asks whether the component that mediates all access between "
                "subjects and objects is tamperproof, cannot be bypassed, and is small enough to be fully "
                "analyzed and verified. Which concept is being evaluated?",
        "options": [
            {"id": "A", "text": "The trusted platform module (TPM)"},
            {"id": "B", "text": "The security perimeter"},
            {"id": "C", "text": "The reference monitor"},
            {"id": "D", "text": "A covert channel"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The reference monitor is the abstract concept that mediates all subject-to-object "
                       "access; it must be always invoked (non-bypassable), tamperproof, and small enough to "
                       "be verifiable.",
            "distractors": {
                "A": "A TPM is a hardware chip for key storage and attestation, not the abstract access mediator.",
                "B": "The security perimeter is the boundary of the trusted computing base, not the mediator itself.",
                "D": "A covert channel is an unintended communication path (a vulnerability), not a protection "
                     "mechanism.",
            },
            "exam_pattern": "Reference monitor must be always invoked, tamperproof, and verifiable; the security "
                            "kernel implements it.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Reference monitor"],
    },
    {
        "id": "cissp-arch-010", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_capabilities", "difficulty": 2, "type": "mcq",
        "stem": "Which term describes the total combination of hardware, firmware, and software "
                "mechanisms within a system that are responsible for enforcing the security policy?",
        "options": [
            {"id": "A", "text": "Trusted computing base (TCB)"},
            {"id": "B", "text": "Security kernel"},
            {"id": "C", "text": "Reference monitor"},
            {"id": "D", "text": "Protection profile"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The trusted computing base (TCB) is the totality of protection mechanisms - hardware, "
                       "firmware, and software - that together enforce the security policy.",
            "distractors": {
                "B": "The security kernel is the core part of the TCB that implements the reference monitor, "
                     "not the entire set of mechanisms.",
                "C": "The reference monitor is the abstract access-mediation concept, not the full combination "
                     "of mechanisms.",
                "D": "A protection profile is a Common Criteria document of security requirements, not a "
                     "system's mechanisms.",
            },
            "exam_pattern": "TCB = all protection mechanisms enforcing the policy; the security kernel realizes "
                            "the reference monitor within it.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Trusted computing base"],
    },
    {
        "id": "cissp-arch-011", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_capabilities", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a hardware-based root of trust on each laptop that can securely "
                "store encryption keys and support measured/secure boot to detect tampering with the boot "
                "process. Which component provides this?",
        "options": [
            {"id": "A", "text": "A hardware security module (HSM) in the data center"},
            {"id": "B", "text": "A software password manager"},
            {"id": "C", "text": "A smart-card reader"},
            {"id": "D", "text": "A Trusted Platform Module (TPM)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A TPM is an on-board hardware chip that provides a root of trust: it stores keys, seals "
                       "data to platform state, and supports measured/secure boot attestation.",
            "distractors": {
                "A": "An HSM is a dedicated appliance for centralized key management, not an on-device boot root "
                     "of trust for each laptop.",
                "B": "A software password manager stores credentials but offers no hardware root of trust.",
                "C": "A smart-card reader supports user authentication tokens, not platform boot integrity.",
            },
            "exam_pattern": "TPM = on-device hardware root of trust: key storage, sealing, and secure/measured boot.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Trusted Platform Module"],
    },

    # ===== cissp_vuln_architectures =========================================
    {
        "id": "cissp-arch-012", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_vuln_architectures", "difficulty": 3, "type": "mcq",
        "stem": "An application checks that a user is authorized to access a file, but an attacker swaps "
                "the file for a sensitive one in the brief window between the authorization check and the "
                "actual read. Which class of vulnerability is this?",
        "options": [
            {"id": "A", "text": "Buffer overflow"},
            {"id": "B", "text": "Time-of-check to time-of-use (TOCTOU) race condition"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Cross-site scripting (XSS)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A TOCTOU race condition exploits the gap between when a condition is checked and when "
                       "the resource is actually used, allowing the state to change in between.",
            "distractors": {
                "A": "A buffer overflow writes beyond a buffer's boundary, a different class of flaw.",
                "C": "SQL injection manipulates database queries through untrusted input.",
                "D": "XSS injects scripts into web content rendered for other users.",
            },
            "exam_pattern": "A state change between the check and the use = TOCTOU (time-of-check/time-of-use) race condition.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Race conditions (TOCTOU)"],
    },
    {
        "id": "cissp-arch-013", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_vuln_architectures", "difficulty": 3, "type": "mcq",
        "stem": "A user without access to classified salary data is able to deduce an executive's "
                "approximate salary by reasoning over several unclassified figures and reports they can "
                "see. Which database security threat is this, and which control helps counter it?",
        "options": [
            {"id": "A", "text": "Inference; countered by polyinstantiation and controlling which data users can combine"},
            {"id": "B", "text": "Aggregation; countered by degaussing the database media"},
            {"id": "C", "text": "A covert storage channel; countered by TLS"},
            {"id": "D", "text": "SQL injection; countered by input validation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Inference is deducing restricted information from data the user is permitted to see; "
                       "polyinstantiation (and limiting combinable data) is a classic defense.",
            "distractors": {
                "B": "Aggregation is combining data so the whole becomes more sensitive; degaussing is media "
                     "sanitization, not an inference control.",
                "C": "A covert channel is an unintended communication path, and TLS protects data in transit, "
                     "not inference.",
                "D": "SQL injection manipulates queries via untrusted input, unrelated to deducing values from "
                     "permitted data.",
            },
            "exam_pattern": "Inference = deducing restricted data from permitted data; polyinstantiation is the "
                            "classic defense.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Inference and aggregation"],
    },
    {
        "id": "cissp-arch-014", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_vuln_architectures", "difficulty": 2, "type": "mcq",
        "stem": "During a code review, developers find an undocumented set of credentials left in the "
                "application that allows bypassing normal authentication for 'support' purposes. What is "
                "this, and what should be done?",
        "options": [
            {"id": "A", "text": "A covert timing channel; it should be throttled"},
            {"id": "B", "text": "A legitimate break-glass control; it should be kept as is"},
            {"id": "C", "text": "A maintenance hook (backdoor); it should be removed before production"},
            {"id": "D", "text": "A reference monitor; it should be expanded"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An undocumented authentication bypass left in code is a maintenance hook (backdoor); "
                       "it is a serious risk and should be removed before release.",
            "distractors": {
                "A": "A covert timing channel signals data by modulating timing; it is not an authentication bypass.",
                "B": "An undocumented hidden bypass is not a governed break-glass control; it must not be retained.",
                "D": "A reference monitor mediates access and is a protection mechanism, not a hidden bypass.",
            },
            "exam_pattern": "Undocumented bypass left in code = maintenance hook/backdoor - remove it before release.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Maintenance hooks/backdoors"],
    },

    # ===== cissp_physical_security ==========================================
    {
        "id": "cissp-arch-015", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_physical_security", "difficulty": 2, "type": "mcq",
        "stem": "A data center needs a fire-suppression approach for electrical (Class C) fires that will "
                "not damage energized electronic equipment the way water would. Which suppression agent is "
                "MOST appropriate?",
        "options": [
            {"id": "A", "text": "A wet-pipe water sprinkler system"},
            {"id": "B", "text": "A clean-agent gaseous system (for example, FM-200 or inert gas)"},
            {"id": "C", "text": "A deluge water system"},
            {"id": "D", "text": "A Class A foam system"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A non-conductive clean-agent gas (such as FM-200 or an inert-gas system) suppresses "
                       "the fire without the conductivity and water damage that would harm energized equipment.",
            "distractors": {
                "A": "Wet-pipe water conducts electricity and damages energized electronics.",
                "C": "A deluge system discharges large volumes of water, inappropriate for energized equipment.",
                "D": "Foam suits Class A/B fires and would also damage electronics.",
            },
            "exam_pattern": "Class C (electrical) fires in data centers → non-conductive clean-agent gas (FM-200/inert), not water.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Fire suppression"],
    },
    {
        "id": "cissp-arch-016", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_physical_security", "difficulty": 2, "type": "mcq",
        "stem": "During a prolonged period of reduced (but not absent) voltage, equipment in a facility "
                "behaves erratically. Which term describes this prolonged drop in electrical power?",
        "options": [
            {"id": "A", "text": "Brownout"},
            {"id": "B", "text": "Blackout"},
            {"id": "C", "text": "Spike"},
            {"id": "D", "text": "Surge"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A brownout is a prolonged drop in voltage (low power) that stops short of a complete "
                       "outage.",
            "distractors": {
                "B": "A blackout is a complete loss of power, not merely a reduction.",
                "C": "A spike is a momentary high-voltage event.",
                "D": "A surge is a prolonged high-voltage event, the opposite of a reduction.",
            },
            "exam_pattern": "Prolonged low = brownout; momentary low = sag/dip; prolonged high = surge; momentary "
                            "high = spike; total loss = blackout.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Electrical power protection"],
    },
    {
        "id": "cissp-arch-017", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_physical_security", "difficulty": 2, "type": "mcq",
        "stem": "To prevent an unauthorized person from slipping through a secure door immediately behind "
                "an authorized employee (tailgating), which physical control is MOST effective?",
        "options": [
            {"id": "A", "text": "A security awareness poster at the entrance"},
            {"id": "B", "text": "A CCTV camera recording the door"},
            {"id": "C", "text": "A deadbolt lock on the door"},
            {"id": "D", "text": "An access control vestibule (mantrap)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An access control vestibule (mantrap) physically allows only one person through at a "
                       "time, directly preventing tailgating/piggybacking.",
            "distractors": {
                "A": "A poster raises awareness but does not physically stop a second person from following in.",
                "B": "CCTV records the event but does not prevent the unauthorized entry.",
                "C": "A deadbolt secures a closed door but does nothing once the door is opened by an authorized user.",
            },
            "exam_pattern": "Tailgating/piggybacking is physically prevented by an access control vestibule (mantrap).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Physical access controls"],
    },
]
