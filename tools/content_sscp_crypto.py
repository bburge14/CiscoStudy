"""(ISC)2 SSCP pool - Domain 5: Cryptography.

Original, objective-aligned practice items for the three Cryptography subtopics
tracked in CertLab:
  * sscp_crypto_concepts - symmetric vs asymmetric ciphers, hashing, HMAC,
                           digital signatures, non-repudiation, and the security
                           services each provides.
  * sscp_pki             - certificate authorities, registration authorities,
                           CRL vs OCSP, X.509 certificates, and chains of trust.
  * sscp_key_management  - key distribution, Diffie-Hellman key exchange, key
                           lifecycle/rotation, and secure key storage (HSM).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_crypto_concepts =============================================
    {
        "id": "sscp-crypto-001", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 1, "type": "mcq",
        "stem": "A technician needs a fast symmetric block cipher to encrypt large volumes of data at "
                "rest on company servers. Which algorithm is the appropriate modern choice?",
        "options": [
            {"id": "A", "text": "RSA"},
            {"id": "B", "text": "AES (Advanced Encryption Standard)"},
            {"id": "C", "text": "Diffie-Hellman"},
            {"id": "D", "text": "SHA-256"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AES is the current standard symmetric block cipher - fast and strong (128/192/"
                       "256-bit keys) - well suited to bulk data-at-rest encryption.",
            "distractors": {
                "A": "RSA is an asymmetric algorithm, far slower and used for key exchange and signatures, not bulk encryption.",
                "C": "Diffie-Hellman is a key-exchange method, not a bulk data cipher.",
                "D": "SHA-256 is a hashing algorithm; it provides integrity, not encryption/confidentiality.",
            },
            "exam_pattern": "Bulk symmetric encryption = AES; asymmetric (RSA/DH) is for key exchange and signatures.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Symmetric cryptography"],
    },
    {
        "id": "sscp-crypto-002", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Alice wants to send Bob a confidential message using asymmetric cryptography so that "
                "only Bob can read it. Which key does Alice use to encrypt the message?",
        "options": [
            {"id": "A", "text": "Bob's private key"},
            {"id": "B", "text": "Alice's private key"},
            {"id": "C", "text": "Bob's public key"},
            {"id": "D", "text": "Alice's public key"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "For confidentiality, the sender encrypts with the recipient's PUBLIC key; only "
                       "the recipient's matching PRIVATE key can decrypt it, so only Bob can read the "
                       "message.",
            "distractors": {
                "A": "Bob's private key is secret to Bob; Alice does not have it and could not use it to encrypt.",
                "B": "Encrypting with Alice's private key provides a signature (authenticity), not confidentiality - anyone with her public key could decrypt.",
                "D": "Alice's public key cannot be paired for decryption by Bob; it would not give Bob exclusive access.",
            },
            "exam_pattern": "Confidentiality: encrypt with the RECIPIENT's public key; they decrypt with their private key.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Asymmetric cryptography"],
    },
    {
        "id": "sscp-crypto-003", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 1, "type": "mcq",
        "stem": "Which property fundamentally distinguishes a cryptographic hash function from "
                "encryption?",
        "options": [
            {"id": "A", "text": "A hash is reversible back to the original with the correct key"},
            {"id": "B", "text": "A hash always compresses data for storage efficiency"},
            {"id": "C", "text": "A hash requires a matching public/private key pair"},
            {"id": "D", "text": "A hash is a one-way function that cannot be reversed to recover the input"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A cryptographic hash is a one-way function: it produces a fixed-length digest "
                       "and cannot be reversed to reveal the original input, which is why it is used "
                       "for integrity and password storage rather than for recovering data.",
            "distractors": {
                "A": "Reversibility with a key describes encryption; hashing has no key to reverse it.",
                "B": "Hashing produces a fixed-length digest for integrity; data compression is a different purpose.",
                "C": "Hashing uses no key pair; that describes asymmetric encryption.",
            },
            "exam_pattern": "Encryption is reversible (with a key); hashing is one-way and keyless (integrity).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Hashing"],
    },
    {
        "id": "sscp-crypto-004", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 3, "type": "mcq",
        "stem": "To create a digital signature on a document, the sender first hashes the document and "
                "then encrypts that hash with which key?",
        "options": [
            {"id": "A", "text": "The recipient's public key"},
            {"id": "B", "text": "The recipient's private key"},
            {"id": "C", "text": "A shared symmetric key"},
            {"id": "D", "text": "The sender's private key"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A digital signature is the message hash encrypted with the SENDER's private "
                       "key. Anyone can verify it using the sender's public key, which provides "
                       "integrity, authentication, and non-repudiation.",
            "distractors": {
                "A": "Encrypting with the recipient's public key provides confidentiality, not a signature.",
                "B": "The sender does not possess the recipient's private key.",
                "C": "A shared symmetric key cannot provide non-repudiation because both parties hold it.",
            },
            "exam_pattern": "Sign with the SENDER's private key; verify with the sender's public key -> integrity + authenticity + non-repudiation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Digital signatures and non-repudiation"],
    },
    {
        "id": "sscp-crypto-005", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 3, "type": "mcq",
        "stem": "Two systems protect each message with an HMAC computed using a shared secret key. "
                "Which security service does the HMAC provide that a plain (unkeyed) hash does not - "
                "and what does it NOT provide?",
        "options": [
            {"id": "A", "text": "It adds integrity plus data-origin authentication, but it does NOT provide non-repudiation"},
            {"id": "B", "text": "It provides non-repudiation between the two parties"},
            {"id": "C", "text": "It encrypts the message body for confidentiality"},
            {"id": "D", "text": "It guarantees availability of the message"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Because an HMAC mixes a shared secret into the hash, it proves the message was "
                       "not altered AND came from a party holding the key (data-origin authentication). "
                       "It cannot provide non-repudiation, since both parties share the same key and "
                       "either could have produced it.",
            "distractors": {
                "B": "Non-repudiation needs a signer-unique private key (a digital signature), not a shared secret.",
                "C": "An HMAC authenticates integrity/origin; it does not encrypt or hide the message contents.",
                "D": "Availability is unrelated to what an HMAC provides.",
            },
            "exam_pattern": "HMAC = integrity + origin authentication (shared key) but NOT non-repudiation; signatures give non-repudiation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - HMAC vs digital signatures"],
    },

    # ===== sscp_pki =========================================================
    {
        "id": "sscp-crypto-006", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 1, "type": "mcq",
        "stem": "In a public key infrastructure (PKI), which entity is responsible for issuing and "
                "digitally signing X.509 digital certificates?",
        "options": [
            {"id": "A", "text": "The Registration Authority (RA)"},
            {"id": "B", "text": "The OCSP responder"},
            {"id": "C", "text": "The Certificate Authority (CA)"},
            {"id": "D", "text": "The Certificate Revocation List (CRL)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Certificate Authority issues, signs, and manages certificates, binding a "
                       "subject's identity to its public key with the CA's own signature.",
            "distractors": {
                "A": "The RA verifies identities and forwards requests, but it does not issue certificates itself.",
                "B": "An OCSP responder answers real-time revocation-status queries; it does not issue certificates.",
                "D": "A CRL is a list of revoked certificates, not an issuing entity.",
            },
            "exam_pattern": "CA issues/signs certs; RA vets identity; CRL/OCSP handle revocation status.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - PKI components (CA)"],
    },
    {
        "id": "sscp-crypto-007", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 2, "type": "mcq",
        "stem": "Which PKI component verifies the identity of a certificate requester and forwards "
                "approved requests to the issuer, but does NOT issue certificates itself?",
        "options": [
            {"id": "A", "text": "Registration Authority (RA)"},
            {"id": "B", "text": "Certificate Authority (CA)"},
            {"id": "C", "text": "Key escrow agent"},
            {"id": "D", "text": "Validation Authority"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Registration Authority offloads identity vetting: it authenticates "
                       "requesters and passes validated requests to the CA, which performs the actual "
                       "issuance.",
            "distractors": {
                "B": "The CA is the issuer; the question specifically asks for the component that does NOT issue.",
                "C": "A key escrow agent stores copies of keys for recovery; it does not vet certificate requests.",
                "D": "A Validation Authority answers status/validation queries; it is not the identity-vetting registrar.",
            },
            "exam_pattern": "RA = identity vetting front end; CA = issuing authority.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - PKI components (RA)"],
    },
    {
        "id": "sscp-crypto-008", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 2, "type": "mcq",
        "stem": "A relying party needs to check whether a single certificate has been revoked, in real "
                "time, without downloading and parsing a large revocation list. Which mechanism "
                "provides this?",
        "options": [
            {"id": "A", "text": "Certificate Revocation List (CRL)"},
            {"id": "B", "text": "Online Certificate Status Protocol (OCSP)"},
            {"id": "C", "text": "Certificate Signing Request (CSR)"},
            {"id": "D", "text": "Common Name (CN) field"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "OCSP lets a client query the status of a specific certificate on demand and get "
                       "a real-time good/revoked/unknown answer, avoiding the overhead of a full CRL "
                       "download.",
            "distractors": {
                "A": "A CRL is the periodically published list of revoked certificates the client must download and search - the approach OCSP improves on.",
                "C": "A CSR is the request a subject sends to obtain a certificate, not a revocation-check method.",
                "D": "The CN is a field inside a certificate (the subject name), not a revocation mechanism.",
            },
            "exam_pattern": "OCSP = real-time per-certificate status; CRL = downloaded list of revoked certs.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Certificate revocation (CRL/OCSP)"],
    },
    {
        "id": "sscp-crypto-009", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 2, "type": "mcq",
        "stem": "An X.509 digital certificate primarily binds a public key to which of the following?",
        "options": [
            {"id": "A", "text": "The subject's corresponding private key"},
            {"id": "B", "text": "The verified identity of the subject (the key's owner)"},
            {"id": "C", "text": "A symmetric session key"},
            {"id": "D", "text": "The issuing CA's private key"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A certificate cryptographically binds a public key to the validated identity of "
                       "its owner (the subject), attested by the CA's signature, so relying parties can "
                       "trust that the key belongs to that entity.",
            "distractors": {
                "A": "The private key is kept secret by the owner and is never placed in the certificate.",
                "C": "Certificates carry asymmetric public keys and identity, not symmetric session keys.",
                "D": "The CA signs the certificate with its private key, but the certificate binds the key to the SUBJECT's identity, not to the CA's private key.",
            },
            "exam_pattern": "X.509 cert = public key + owner identity, signed by a trusted CA.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - X.509 certificates"],
    },
    {
        "id": "sscp-crypto-010", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 2, "type": "fill",
        "stem": "A browser trusts a web server's certificate because it can validate the certificate "
                "up a chain of trust to a trusted ____ CA whose certificate is preinstalled in the "
                "client's trust store. Provide the one-word term for the anchor of the chain.",
        "correct": ["root", "root ca", "root certificate authority"],
        "explanation": {
            "correct": "The chain of trust terminates at a trusted root CA (the trust anchor) stored in "
                       "the client; intermediate CAs link the end-entity certificate up to that root.",
            "distractors": {},
            "exam_pattern": "Trust anchors the chain at a preinstalled root CA; intermediates bridge to the leaf cert.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Chain of trust / root CA"],
    },

    # ===== sscp_key_management ==============================================
    {
        "id": "sscp-crypto-011", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 2, "type": "mcq",
        "stem": "What is the principal challenge of purely symmetric encryption that asymmetric "
                "cryptography was designed to help solve?",
        "options": [
            {"id": "A", "text": "Securely distributing and exchanging the shared secret key between parties"},
            {"id": "B", "text": "It is too slow to encrypt bulk data"},
            {"id": "C", "text": "It is unable to encrypt large files at all"},
            {"id": "D", "text": "It can only produce a fixed-length digest"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Symmetric encryption needs both parties to share the same secret key; "
                       "distributing that key securely (and managing many keys) is the core challenge "
                       "that asymmetric key exchange addresses.",
            "distractors": {
                "B": "Symmetric encryption is actually fast; speed is a strength, not the key-management problem.",
                "C": "Symmetric ciphers handle large files well; capacity is not the issue.",
                "D": "Producing a fixed-length digest describes hashing, not symmetric encryption.",
            },
            "exam_pattern": "Symmetric weakness = secure key distribution/scaling; asymmetric solves key exchange.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Key distribution"],
    },
    {
        "id": "sscp-crypto-012", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 2, "type": "mcq",
        "stem": "Two parties need to agree on a shared secret key over an untrusted network without "
                "ever transmitting the secret itself. Which algorithm is purpose-built for this key "
                "exchange?",
        "options": [
            {"id": "A", "text": "AES"},
            {"id": "B", "text": "SHA-3"},
            {"id": "C", "text": "Diffie-Hellman"},
            {"id": "D", "text": "MD5"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Diffie-Hellman allows two parties to derive a shared secret over a public "
                       "channel without transmitting the secret, forming the basis of secure key "
                       "exchange.",
            "distractors": {
                "A": "AES is a symmetric cipher that uses a key; it does not negotiate one over an untrusted channel.",
                "B": "SHA-3 is a hashing algorithm, not a key-exchange protocol.",
                "D": "MD5 is a (now broken) hash function, unrelated to key agreement.",
            },
            "exam_pattern": "Agree on a shared secret over a public channel = Diffie-Hellman key exchange.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Diffie-Hellman key exchange"],
    },
    {
        "id": "sscp-crypto-013", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 2, "type": "mcq",
        "stem": "Why should cryptographic keys be assigned a defined crypto-period and rotated "
                "periodically?",
        "options": [
            {"id": "A", "text": "To make the encryption algorithm run faster"},
            {"id": "B", "text": "To remove the need to back up keys"},
            {"id": "C", "text": "Because encryption algorithms expire every month"},
            {"id": "D", "text": "To limit the amount of data exposed if a key is compromised and reduce the window for cryptanalysis"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Rotating keys on a defined schedule limits how much data a single key protects "
                       "(and thus how much is exposed if it is compromised) and reduces the time an "
                       "attacker has to attack that key.",
            "distractors": {
                "A": "Rotation does not speed up the algorithm.",
                "B": "Keys still require secure backup/escrow for recovery; rotation does not remove that need.",
                "C": "Algorithms do not expire monthly; it is the keys that have crypto-periods.",
            },
            "exam_pattern": "Key rotation limits blast radius and cryptanalysis time; it does not affect algorithm speed.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Key lifecycle and rotation"],
    },
    {
        "id": "sscp-crypto-014", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 2, "type": "mcq",
        "stem": "Which dedicated, tamper-resistant hardware device is designed to securely generate, "
                "store, and manage cryptographic keys and perform crypto operations?",
        "options": [
            {"id": "A", "text": "Hardware Security Module (HSM)"},
            {"id": "B", "text": "Network interface card (NIC)"},
            {"id": "C", "text": "An ordinary USB flash drive"},
            {"id": "D", "text": "Certificate Revocation List (CRL)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An HSM is a hardened, tamper-resistant device that generates, stores, and "
                       "protects keys and performs cryptographic operations, keeping private keys out "
                       "of general-purpose memory.",
            "distractors": {
                "B": "A NIC handles network connectivity; it is not a key-protection device.",
                "C": "A plain USB drive offers no tamper resistance or secure key handling.",
                "D": "A CRL is a PKI revocation list, not a hardware key store.",
            },
            "exam_pattern": "Tamper-resistant hardware key storage/operations = HSM.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Secure key storage (HSM)"],
    },
    {
        "id": "sscp-crypto-015", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 3, "type": "multi",
        "stem": "An architect is choosing where to use symmetric versus asymmetric cryptography. Which "
                "TWO statements correctly compare them? (Choose two.)",
        "options": [
            {"id": "A", "text": "Symmetric encryption is generally much faster and is well suited to encrypting bulk data"},
            {"id": "B", "text": "Asymmetric cryptography enables secure key exchange and digital signatures"},
            {"id": "C", "text": "Symmetric encryption provides non-repudiation between two parties who share the key"},
            {"id": "D", "text": "Asymmetric encryption is faster than symmetric encryption for large files"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Symmetric ciphers are fast and ideal for bulk data; asymmetric cryptography "
                       "solves key exchange and provides digital signatures. A common hybrid uses "
                       "asymmetric methods to exchange a symmetric session key.",
            "distractors": {
                "C": "A shared symmetric key cannot provide non-repudiation because either party could have produced the output.",
                "D": "Asymmetric operations are significantly SLOWER than symmetric ones, which is why symmetric is used for bulk data.",
            },
            "exam_pattern": "Symmetric = fast/bulk; asymmetric = key exchange + signatures (slower). Hybrid combines both.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Symmetric vs asymmetric cryptography"],
    },
]
