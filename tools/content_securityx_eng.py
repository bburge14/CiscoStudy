"""CompTIA SecurityX (CAS-005) pool - Domain 3: Security Engineering.

Original, objective-aligned practice items for the seven Security Engineering
subtopics tracked in CertLab (expert/CASP+-level, scenario and trade-off driven):
  * scx_cryptography       - password hashing/salting, symmetric vs asymmetric,
                             ECC, post-quantum migration (ML-KEM/ML-DSA),
                             forward secrecy, cipher modes, HMAC.
  * scx_pki                - CA hierarchy / offline root, OCSP/CRL/OCSP stapling,
                             mutual TLS, certificate pinning, key escrow.
  * scx_secure_integration - OAuth 2.0 delegated authorization, API gateways,
                             forward secrecy in transit (ECDHE), REST/SOAP.
  * scx_endpoint_security  - EDR/XDR vs signature AV, application allowlisting,
                             TPM / secure & measured boot, hardening.
  * scx_emerging_tech      - AI/ML security (prompt injection, data poisoning),
                             deepfake-enabled fraud, quantum threat.
  * scx_secure_coding      - SAST/DAST/IAST, SCA/SBOM, CI/CD and IaC security,
                             OWASP, secrets management.
  * scx_automation         - SOAR/playbooks, Infrastructure as Code / policy as
                             code, risk-tiered automation with guardrails.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so authored keys are spread across A-D (not
positionally biased), every wrong option carries a distractor note, and each
item cites the public CAS-005 objective domain it draws on. Expert depth with
BEST-given-constraints framing - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== scx_cryptography =================================================
    {
        "id": "securityx-eng-001", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "A developer must store user passwords so that a database breach does not reveal them and so "
                "that two users with the same password produce different stored values. Which approach is BEST?",
        "options": [
            {"id": "A", "text": "Encrypt the passwords with AES-256 using a shared application key"},
            {"id": "B", "text": "Hash each password with a slow, salted algorithm such as bcrypt, scrypt, or Argon2 (unique salt per user)"},
            {"id": "C", "text": "Store the passwords after Base64 encoding"},
            {"id": "D", "text": "Hash the passwords with a single round of unsalted SHA-1"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Passwords should be stored using a slow, memory-hard, salted password-hashing function "
                       "(bcrypt/scrypt/Argon2). A unique per-user salt makes identical passwords hash differently and defeats precomputed (rainbow-table) attacks; the work factor slows brute force.",
            "distractors": {
                "A": "Reversible encryption means anyone with the key recovers all passwords; passwords should be hashed, not encrypted.",
                "C": "Base64 is encoding, not protection - it is trivially reversed.",
                "D": "Unsalted single-round SHA-1 is fast and broken: identical passwords collide and it is highly vulnerable to brute-force and rainbow-table attacks.",
            },
            "exam_pattern": "Password storage = salted, slow hash (bcrypt/scrypt/Argon2), never reversible encryption or fast/unsalted hashes.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (hashing, salting, password storage)"],
    },
    {
        "id": "securityx-eng-002", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "An IoT vendor needs public-key cryptography on battery-powered sensors with very limited CPU "
                "and memory, while keeping strong security. Which algorithm family BEST meets the constraint of "
                "strong security at the smallest key size and lowest compute cost?",
        "options": [
            {"id": "A", "text": "Elliptic curve cryptography (ECC)"},
            {"id": "B", "text": "RSA with 3072-bit keys"},
            {"id": "C", "text": "Triple DES (3DES)"},
            {"id": "D", "text": "Finite-field Diffie-Hellman with 4096-bit groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ECC provides equivalent security to RSA at far smaller key sizes (e.g., a 256-bit ECC key "
                       "is comparable to a 3072-bit RSA key), reducing computation, memory, and power - ideal for constrained IoT devices.",
            "distractors": {
                "B": "RSA reaches comparable strength only with much larger keys, costing more compute/power than ECC on constrained hardware.",
                "C": "3DES is a legacy symmetric cipher (deprecated), not public-key cryptography, and is slow and weak by modern standards.",
                "D": "4096-bit finite-field Diffie-Hellman is computationally heavy for tiny devices compared with elliptic-curve equivalents.",
            },
            "exam_pattern": "Strong asymmetric security + tiny keys / low power (IoT) = ECC (256-bit ECC approx. 3072-bit RSA).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (ECC, asymmetric key sizes)"],
    },
    {
        "id": "securityx-eng-003", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "A security architect is worried about 'harvest-now, decrypt-later' attacks, in which "
                "adversaries capture today's encrypted traffic to decrypt once large-scale quantum computers "
                "exist. For data that must stay confidential for decades, which action BEST addresses this "
                "long-term threat?",
        "options": [
            {"id": "A", "text": "Increase AES symmetric keys from 128-bit to 256-bit only and take no other action"},
            {"id": "B", "text": "Switch all hashing to MD5 for speed"},
            {"id": "C", "text": "Begin migrating key establishment and signatures to NIST-standardized post-quantum algorithms (e.g., ML-KEM / FIPS 203, ML-DSA / FIPS 204), using crypto-agility and hybrid schemes"},
            {"id": "D", "text": "Disable encryption to avoid the overhead"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The quantum threat most severely affects asymmetric algorithms (RSA/ECC, via Shor's "
                       "algorithm). Migrating key establishment and signatures to NIST-standardized post-quantum algorithms - ML-KEM (FIPS 203) and ML-DSA (FIPS 204) - with crypto-agility and hybrid (classical + PQC) deployments addresses harvest-now-decrypt-later.",
            "distractors": {
                "A": "Doubling the AES key length strengthens symmetric security against Grover's algorithm but does nothing for the vulnerable asymmetric key exchange that protects the session.",
                "B": "MD5 is a broken hash and irrelevant to the quantum key-exchange problem.",
                "D": "Disabling encryption removes all protection - the opposite of the goal.",
            },
            "exam_pattern": "Harvest-now-decrypt-later targets asymmetric crypto -> migrate key exchange/signatures to PQC (ML-KEM/ML-DSA) with crypto-agility/hybrid.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography / emerging tech (post-quantum: FIPS 203 ML-KEM, FIPS 204 ML-DSA)"],
    },

    # ===== scx_pki ==========================================================
    {
        "id": "securityx-eng-004", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 3, "type": "mcq",
        "stem": "A high-traffic web platform wants clients to verify certificate revocation status with minimal "
                "latency, without each client generating heavy real-time load on the CA's responder, and without "
                "the privacy leak of clients contacting the CA for every visit. Which mechanism BEST meets these goals?",
        "options": [
            {"id": "A", "text": "Distributing a full certificate revocation list (CRL) to every client on each connection"},
            {"id": "B", "text": "Disabling revocation checking entirely"},
            {"id": "C", "text": "Relying only on certificate expiration dates"},
            {"id": "D", "text": "OCSP stapling (the server attaches a time-stamped, CA-signed OCSP response to the TLS handshake)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "OCSP stapling has the web server obtain and 'staple' a signed, time-stamped OCSP response "
                       "during the TLS handshake, so clients get fresh revocation status without each contacting the CA - cutting latency, offloading the responder, and avoiding the client-privacy leak.",
            "distractors": {
                "A": "CRLs can be large and grow over time; downloading and parsing them per connection adds latency and bandwidth overhead.",
                "B": "Disabling revocation checking leaves clients trusting revoked (possibly compromised) certificates.",
                "C": "Expiration dates do not reflect early revocation of a compromised certificate.",
            },
            "exam_pattern": "Fresh revocation, low latency, less CA load, better privacy = OCSP stapling (vs bulky CRLs or per-client OCSP).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (certificate revocation: OCSP, OCSP stapling, CRL)"],
    },
    {
        "id": "securityx-eng-005", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 3, "type": "mcq",
        "stem": "When designing an internal PKI, a security engineer wants to minimize the impact if an issuing "
                "CA's signing key is compromised, while strongly protecting the trust anchor. Which design is BEST?",
        "options": [
            {"id": "A", "text": "A single online root CA that issues all end-entity certificates directly"},
            {"id": "B", "text": "A tiered hierarchy: an offline root CA that signs one or more subordinate (issuing) CAs, which issue the end-entity certificates"},
            {"id": "C", "text": "Issue all certificates from a shared public CA with no internal hierarchy"},
            {"id": "D", "text": "Use self-signed certificates on every server with no CA"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A tiered PKI keeps the root CA offline (air-gapped) as the protected trust anchor and uses "
                       "subordinate/issuing CAs for day-to-day issuance. If an issuing CA is compromised, only its subtree must be revoked/replaced; the root remains safe.",
            "distractors": {
                "A": "A single online root that issues directly exposes the trust anchor to compromise, and a root compromise invalidates the entire PKI.",
                "C": "Using a public CA for everything doesn't address internal hierarchy/containment and may not suit internal naming or controls.",
                "D": "Self-signed certificates everywhere provide no scalable trust, revocation, or containment.",
            },
            "exam_pattern": "Offline root CA + subordinate issuing CAs = protect the trust anchor and contain an issuing-CA compromise.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (CA hierarchy, offline root, subordinate CAs)"],
    },
    {
        "id": "securityx-eng-006", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 2, "type": "mcq",
        "stem": "In a zero-trust microservices environment, each service must cryptographically authenticate BOTH "
                "ends of every connection using certificates, not just the server. Which mechanism provides this?",
        "options": [
            {"id": "A", "text": "Mutual TLS (mTLS), where client and server each present and validate certificates"},
            {"id": "B", "text": "Standard one-way TLS, where only the server presents a certificate"},
            {"id": "C", "text": "A shared static API key in each request header"},
            {"id": "D", "text": "HTTP Basic authentication over plaintext"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mutual TLS has both the client and the server present and validate X.509 certificates, "
                       "giving strong bidirectional authentication for service-to-service communication - a common zero-trust pattern.",
            "distractors": {
                "B": "One-way TLS authenticates only the server; the client is not certificate-authenticated.",
                "C": "A shared static API key is a bearer secret that can be stolen or replayed and does not cryptographically authenticate both endpoints.",
                "D": "HTTP Basic over plaintext exposes credentials and provides no certificate-based mutual authentication.",
            },
            "exam_pattern": "Both endpoints authenticate with certificates = mutual TLS (mTLS).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI / secure integration (mTLS, certificate-based authentication)"],
    },

    # ===== scx_secure_integration ===========================================
    {
        "id": "securityx-eng-007", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "A web app must let users grant a third-party analytics service limited, revocable access to "
                "specific data in the app's API - without ever sharing the users' passwords with the third "
                "party. Which framework is designed for this delegated authorization?",
        "options": [
            {"id": "A", "text": "SAML 2.0 used for web SSO"},
            {"id": "B", "text": "LDAP bind authentication"},
            {"id": "C", "text": "OAuth 2.0 (issuing scoped, revocable access tokens to the third party)"},
            {"id": "D", "text": "WPA3-Enterprise"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "OAuth 2.0 is a delegated-authorization framework: the user authorizes the third party, which "
                       "receives a scoped, revocable access token to call the API - without the user's credentials being shared.",
            "distractors": {
                "A": "SAML handles federated authentication/SSO (who you are), not fine-grained delegated API authorization with scoped tokens.",
                "B": "LDAP bind authenticates a user against a directory; it is not a delegated third-party authorization framework.",
                "D": "WPA3-Enterprise secures wireless network access, unrelated to API authorization delegation.",
            },
            "exam_pattern": "Delegated, scoped, revocable third-party API access without sharing passwords = OAuth 2.0 (authorization).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (OAuth 2.0, API authorization)"],
    },
    {
        "id": "securityx-eng-008", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise exposes dozens of internal microservice APIs to partners. It wants ONE enforcement "
                "point for authentication, authorization, TLS termination, rate limiting/throttling, and request "
                "validation. Which component BEST provides this?",
        "options": [
            {"id": "A", "text": "A reverse-proxy cache with no security features"},
            {"id": "B", "text": "A client-side JavaScript SDK"},
            {"id": "C", "text": "A spreadsheet of allowed IP addresses"},
            {"id": "D", "text": "An API gateway"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An API gateway is a centralized ingress control point that enforces authentication and "
                       "authorization, terminates TLS, applies rate limiting/throttling and quotas, validates requests, and routes to backend services.",
            "distractors": {
                "A": "A plain cache improves performance but doesn't centrally enforce auth, throttling, and validation.",
                "B": "A client-side SDK runs in the untrusted client and cannot be a trusted enforcement point.",
                "C": "A static IP spreadsheet is neither automated nor capable of auth, throttling, or validation.",
            },
            "exam_pattern": "Central API auth + rate limiting + validation/routing = API gateway.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (API gateway)"],
    },
    {
        "id": "securityx-eng-009", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "A compliance requirement states that if a server's long-term private key is ever compromised, "
                "previously recorded TLS sessions must NOT become decryptable. Which TLS configuration choice "
                "achieves this 'perfect forward secrecy'?",
        "options": [
            {"id": "A", "text": "Static RSA key exchange (the client encrypts the premaster secret to the server's RSA public key)"},
            {"id": "B", "text": "Ephemeral key exchange such as ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)"},
            {"id": "C", "text": "Disabling TLS and using a shared VPN tunnel password"},
            {"id": "D", "text": "Reusing a single session key across all connections"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Ephemeral Diffie-Hellman (DHE/ECDHE) generates a unique, short-lived key per session that is "
                       "not derived from the server's long-term private key, so compromising that key cannot decrypt past sessions - perfect forward secrecy.",
            "distractors": {
                "A": "With static RSA key exchange the session keys are protected by the server's long-term key; stealing it lets an attacker decrypt all previously captured sessions - no forward secrecy.",
                "C": "Abandoning TLS for a shared VPN password does not provide per-session forward secrecy and weakens security.",
                "D": "Reusing one session key across connections is insecure and the opposite of forward secrecy.",
            },
            "exam_pattern": "Forward secrecy = ephemeral key exchange (DHE/ECDHE); static RSA key exchange has none.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography / secure integration (forward secrecy, ECDHE, TLS)"],
    },

    # ===== scx_endpoint_security ============================================
    {
        "id": "securityx-eng-010", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 2, "type": "mcq",
        "stem": "A SOC needs endpoint protection that goes beyond signature antivirus: continuous behavioral "
                "monitoring, detection of fileless / living-off-the-land techniques, and the ability to isolate "
                "a host and roll back changes during response. Which capability BEST fits?",
        "options": [
            {"id": "A", "text": "Endpoint detection and response (EDR), extensible to XDR"},
            {"id": "B", "text": "Traditional signature-only antivirus"},
            {"id": "C", "text": "A network load balancer"},
            {"id": "D", "text": "A password vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR continuously records and analyzes endpoint behavior, detects fileless / living-off-the-land "
                       "activity that signatures miss, and supports response actions such as host isolation and remediation/rollback; XDR extends this correlation across endpoints, identity, email, and cloud.",
            "distractors": {
                "B": "Signature-only antivirus detects known malware by hashes/patterns and misses behavioral, fileless, and novel attacks.",
                "C": "A load balancer distributes traffic; it is not an endpoint threat-detection tool.",
                "D": "A password vault protects credentials, not endpoint behavioral detection and response.",
            },
            "exam_pattern": "Behavioral detection + fileless coverage + host isolation/rollback = EDR (XDR correlates across domains).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (EDR/XDR vs signature AV)"],
    },
    {
        "id": "securityx-eng-011", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 3, "type": "mcq",
        "stem": "To stop unauthorized and unknown executables on hardened kiosks that run a fixed set of "
                "applications, which control provides the STRONGEST preventive posture?",
        "options": [
            {"id": "A", "text": "A blocklist (denylist) of known-bad file hashes"},
            {"id": "B", "text": "Scheduled signature antivirus scans only"},
            {"id": "C", "text": "User training to avoid risky downloads"},
            {"id": "D", "text": "Application allowlisting (only explicitly approved applications may run; everything else is denied by default)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Application allowlisting enforces default-deny: only explicitly approved applications execute, "
                       "which is ideal for fixed-purpose/kiosk systems and blocks unknown or novel malware that a blocklist would miss.",
            "distractors": {
                "A": "A blocklist only stops known-bad items and cannot block novel or unknown executables.",
                "B": "Periodic AV scans are detective and signature-bound, not a strong preventive execution control.",
                "C": "Training reduces risky behavior but does not technically prevent unauthorized code from running.",
            },
            "exam_pattern": "Fixed-function host + strongest prevention = application allowlisting (default-deny), not blocklisting.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (application allowlisting/hardening)"],
    },
    {
        "id": "securityx-eng-012", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the acronym: A dedicated secure cryptoprocessor on a device's motherboard "
                "that stores keys and platform-integrity measurements (used for full-disk-encryption key protection "
                "and measured boot) is a Trusted Platform Module, abbreviated ______.",
        "correct": ["tpm"],
        "explanation": {
            "correct": "A TPM is a hardware root of trust that stores cryptographic keys and platform configuration "
                       "register (PCR) measurements, supporting full-disk-encryption key sealing, secure/measured boot attestation, and device integrity.",
            "distractors": {},
            "exam_pattern": "On-board secure cryptoprocessor storing keys + boot measurements = TPM (enables measured boot, FDE key sealing).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (TPM, secure/measured boot, hardware root of trust)"],
    },

    # ===== scx_emerging_tech ================================================
    {
        "id": "securityx-eng-013", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise deploys an LLM-based assistant that can call internal tools and read documents. A "
                "tester hides instructions inside a document that, when summarized, cause the model to exfiltrate "
                "data. Which attack is this, and which mitigation is MOST appropriate?",
        "options": [
            {"id": "A", "text": "SQL injection; mitigate with parameterized queries"},
            {"id": "B", "text": "Cross-site scripting; mitigate with output encoding in the browser"},
            {"id": "C", "text": "Prompt injection (indirect); mitigate by isolating/validating untrusted content, least-privilege tool access, output filtering, and human approval for sensitive actions"},
            {"id": "D", "text": "Buffer overflow; mitigate with stack canaries"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Malicious instructions embedded in content the model ingests is (indirect) prompt injection. "
                       "Defenses include treating retrieved content as untrusted, constraining the model's tool permissions to least privilege, filtering/validating outputs, and requiring human approval for sensitive or destructive actions.",
            "distractors": {
                "A": "SQL injection targets database query construction, not LLM prompt handling; parameterized queries don't address model instruction-following.",
                "B": "XSS is browser script injection; output encoding addresses web rendering, not an LLM following embedded instructions.",
                "D": "Buffer overflows are memory-safety bugs; stack canaries are irrelevant to prompt manipulation.",
            },
            "exam_pattern": "Embedded malicious instructions in model-ingested content = prompt injection; defend with untrusted-content isolation, least-privilege tools, output filtering, human-in-the-loop.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (AI/ML security, prompt injection)"],
    },
    {
        "id": "securityx-eng-014", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "An adversary submits carefully crafted training samples to a continuously retrained "
                "fraud-detection model so that, over time, the model learns to classify the attacker's "
                "fraudulent transactions as legitimate. Which AI/ML threat is this?",
        "options": [
            {"id": "A", "text": "Model inversion (reconstructing training data)"},
            {"id": "B", "text": "Data (training) poisoning"},
            {"id": "C", "text": "Prompt injection"},
            {"id": "D", "text": "Membership inference"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Injecting manipulated samples into the training data to corrupt what the model learns is "
                       "data/training poisoning; defenses include training-data validation, provenance/integrity controls, input anomaly detection, and robust/aggregated learning.",
            "distractors": {
                "A": "Model inversion tries to reconstruct sensitive training data from model outputs, not to corrupt training.",
                "C": "Prompt injection manipulates an LLM's instruction-following at inference time, not the training set.",
                "D": "Membership inference determines whether a record was in the training set; it does not alter model behavior.",
            },
            "exam_pattern": "Corrupting the training set to bias the model = data poisoning (an integrity attack on ML).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (adversarial ML, data poisoning)"],
    },
    {
        "id": "securityx-eng-015", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "Finance receives a video call that looks and sounds like the CFO authorizing an urgent $5M wire. "
                "The 'CFO' is an AI-generated deepfake. Which control set BEST reduces the risk of such "
                "deepfake-enabled fraud?",
        "options": [
            {"id": "A", "text": "Out-of-band verification and multi-person approval using pre-established channels and code words for high-value transactions (process controls)"},
            {"id": "B", "text": "Relying on the employee's visual recognition of the executive on the call"},
            {"id": "C", "text": "Allowing single-approver wires if the caller sounds authoritative"},
            {"id": "D", "text": "Posting executives' travel schedules publicly to confirm availability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Deepfakes defeat voice/video recognition, so controls must be process-based: out-of-band "
                       "verification through a known channel, multi-person authorization, pre-agreed verification phrases, and callback procedures for high-value transfers.",
            "distractors": {
                "B": "Visual/audio recognition is exactly what a convincing deepfake defeats.",
                "C": "Single-approver wires based on perceived authority is the weakness attackers exploit.",
                "D": "Publicizing schedules aids attackers and does not verify the transaction request.",
            },
            "exam_pattern": "Deepfake-enabled BEC -> defend with out-of-band, multi-party, pre-shared verification process controls, not sensory recognition.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (deepfakes, social-engineering defenses)"],
    },

    # ===== scx_secure_coding ================================================
    {
        "id": "securityx-eng-016", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A DevSecOps lead wants to catch vulnerabilities by analyzing source code WITHOUT executing it, "
                "early in development and integrated into the IDE and pull requests. Which testing type fits this "
                "requirement?",
        "options": [
            {"id": "A", "text": "DAST (dynamic application security testing)"},
            {"id": "B", "text": "Penetration testing in production"},
            {"id": "C", "text": "Fuzzing a running binary"},
            {"id": "D", "text": "SAST (static application security testing)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SAST analyzes source code, bytecode, or binaries without executing them (white-box), so it fits "
                       "early-SDLC, IDE, and pull-request integration ('shift left').",
            "distractors": {
                "A": "DAST tests a running application from the outside (black-box) and needs a deployed/running target, so it runs later.",
                "B": "Production penetration testing happens late and is not an automated, in-IDE source analysis.",
                "C": "Fuzzing requires executing a running target with malformed inputs, not static source analysis.",
            },
            "exam_pattern": "Analyze code without running it, shift-left/IDE = SAST (white-box); DAST = running app (black-box); IAST = instrumented during runtime tests.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (SAST vs DAST vs IAST)"],
    },
    {
        "id": "securityx-eng-017", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "A build pipeline pulls hundreds of open-source libraries. The team needs to automatically flag "
                "known-vulnerable (CVE) dependencies and risky licenses in those third-party components. Which tool "
                "category is designed for this?",
        "options": [
            {"id": "A", "text": "Software composition analysis (SCA)"},
            {"id": "B", "text": "A web application firewall (WAF)"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "A load tester"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SCA inventories third-party/open-source components and their versions, flags known "
                       "vulnerabilities (CVEs) and license risks, and pairs well with an SBOM for supply-chain visibility.",
            "distractors": {
                "B": "A WAF filters malicious web traffic at runtime; it does not analyze your dependency tree for CVEs.",
                "C": "A SIEM correlates security events/logs; it is not a dependency-vulnerability scanner.",
                "D": "A load tester measures performance under load, not component vulnerabilities.",
            },
            "exam_pattern": "Find vulnerable/risky open-source dependencies = software composition analysis (SCA) + SBOM.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (SCA, dependency/supply-chain security)"],
    },
    {
        "id": "securityx-eng-018", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "multi",
        "stem": "A team is hardening its CI/CD pipeline against supply-chain compromise. Which TWO practices MOST "
                "directly reduce the risk of malicious code or secrets entering builds? (Choose two.)",
        "options": [
            {"id": "A", "text": "Scan infrastructure-as-code and container images, and run SCA on dependencies, failing the build on critical findings"},
            {"id": "B", "text": "Store cloud credentials in plaintext environment files committed to the repository for convenience"},
            {"id": "C", "text": "Use short-lived, scoped pipeline credentials (secrets management) and enforce signed commits/artifacts with least-privilege pipeline permissions"},
            {"id": "D", "text": "Grant every developer standing administrator access to the production pipeline"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Scanning IaC/images and dependencies (with gating) catches vulnerable or malicious components "
                       "before release, and using short-lived, scoped secrets with signed commits/artifacts and least-privilege pipeline permissions limits credential theft and tampering.",
            "distractors": {
                "B": "Committing plaintext credentials exposes them to anyone with repo access - a top supply-chain risk, not a mitigation.",
                "D": "Standing admin access for all developers violates least privilege and widens the blast radius of a compromise.",
            },
            "exam_pattern": "Pipeline security = shift-left scanning + gating, secrets management (short-lived/scoped), signing, and least privilege.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (CI/CD security, IaC scanning, secrets management)"],
    },

    # ===== scx_automation ===================================================
    {
        "id": "securityx-eng-019", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the acronym: A platform that integrates security tools and executes "
                "automated, repeatable response playbooks to accelerate incident handling - Security "
                "Orchestration, Automation, and Response - is abbreviated ______.",
        "correct": ["soar"],
        "explanation": {
            "correct": "SOAR integrates disparate tools and runs automated playbooks (enrichment, triage, "
                       "containment) to reduce manual effort and shorten response times, often working alongside a SIEM.",
            "distractors": {},
            "exam_pattern": "Orchestrate tools + automated playbooks to speed response = SOAR (complements SIEM).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation/orchestration (SOAR)"],
    },
    {
        "id": "securityx-eng-020", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants every cloud environment deployed identically with security baselines "
                "enforced, and any drift corrected automatically, by defining the environment declaratively in "
                "version-controlled templates. Which practice provides this?",
        "options": [
            {"id": "A", "text": "Manual console configuration documented in a wiki"},
            {"id": "B", "text": "Ad hoc shell commands run by whoever is on call"},
            {"id": "C", "text": "Infrastructure as Code (IaC) with policy as code and automated drift detection"},
            {"id": "D", "text": "Emailing configuration screenshots for review"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "IaC defines infrastructure declaratively in version-controlled templates, enabling "
                       "consistent, repeatable, peer-reviewed deployments; policy as code enforces baselines and automated drift detection remediates deviations.",
            "distractors": {
                "A": "Manual console changes are inconsistent, error-prone, and hard to audit or reproduce.",
                "B": "Ad hoc commands produce configuration drift and lack review, versioning, and repeatability.",
                "D": "Emailing screenshots provides no automation, enforcement, or drift correction.",
            },
            "exam_pattern": "Consistent, version-controlled, drift-corrected environments = IaC + policy as code.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation/orchestration (IaC, policy as code)"],
    },
    {
        "id": "securityx-eng-021", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 3, "type": "mcq",
        "stem": "A SOC automates containment so a confirmed-malware alert can automatically isolate the host. "
                "Leadership worries that automation could mistakenly isolate critical servers. Which design BEST "
                "balances speed with safety?",
        "options": [
            {"id": "A", "text": "Fully automate all response actions with no human review and no exceptions"},
            {"id": "B", "text": "Use risk-tiered automation: auto-contain low-risk endpoints, but require human-in-the-loop approval for high-impact assets, with guardrails, allowlists, and rollback"},
            {"id": "C", "text": "Disable all automation and handle everything manually"},
            {"id": "D", "text": "Automate only after disabling logging to reduce noise"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mature SOAR design tiers actions by risk: low-risk, high-confidence responses run "
                       "automatically, while high-impact actions (e.g., isolating critical servers) require human approval, backed by guardrails (allowlists of protected assets), testing, and rollback plans.",
            "distractors": {
                "A": "Blanket automation with no review risks outages on critical systems - exactly leadership's concern.",
                "C": "Disabling all automation sacrifices the speed needed to contain fast-moving threats.",
                "D": "Disabling logging undermines detection, investigation, and accountability.",
            },
            "exam_pattern": "Balance speed vs safety with risk-tiered automation: auto for low-risk, human-in-the-loop + guardrails for high-impact.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation/orchestration (guardrails, human-in-the-loop)"],
    },
]
