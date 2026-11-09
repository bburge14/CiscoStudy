"""Microsoft SC-900 pool - Domain 1: Concepts of Security, Compliance & Identity.

Original, objective-aligned practice items for the four foundational-concepts
subtopics tracked in CertLab:
  * sc9_security_methodologies - the shared responsibility model; defense in
                                 depth (layered security); the Zero Trust model
                                 (verify explicitly, least privilege, assume
                                 breach) and its pillars; the CIA triad.
  * sc9_identity_concepts      - identity as the primary security perimeter;
                                 authentication vs authorization; identity
                                 providers and directory services; single
                                 sign-on and federation; the four pillars of
                                 identity.
  * sc9_encryption_hashing     - symmetric vs asymmetric encryption; data at
                                 rest / in transit / in use; hashing and signing.
  * sc9_governance_concepts    - governance, risk, and compliance (GRC) basics.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the answer key authored here as "A" is not
positionally biased, every wrong option carries a distractor note, and each item
names the Microsoft Learn (SC-900) area it draws on so facts stay traceable.
Fundamentals depth only (concepts, when-to-use, which-principle) - no numeric
limits, no preview-feature trivia, and never real or memorized exam items. Uses
current Microsoft product names (Microsoft Entra ID, formerly Azure AD).
"""

QUESTIONS = [
    # ===== sc9_security_methodologies =======================================
    {
        "id": "sc900-con-001", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 1, "type": "mcq",
        "stem": "Under the cloud shared responsibility model, which responsibility always remains the "
                "customer's regardless of whether the service is IaaS, PaaS, or SaaS?",
        "options": [
            {"id": "A", "text": "Its information, data, accounts, and identities"},
            {"id": "B", "text": "The physical datacenter and its security"},
            {"id": "C", "text": "The physical network hardware"},
            {"id": "D", "text": "The physical host servers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Information and data, plus accounts and identities (and devices), always stay the "
                       "customer's responsibility in every cloud service model.",
            "distractors": {
                "B": "The physical datacenter and its security are always the cloud provider's responsibility.",
                "C": "The physical network is always owned and secured by the provider.",
                "D": "Physical host servers are always the provider's responsibility, never the customer's.",
            },
            "exam_pattern": "Always-customer: data, accounts/identities, devices. Always-provider: physical "
                            "hosts, network, datacenter.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the shared responsibility model"],
    },
    {
        "id": "sc900-con-002", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 1, "type": "mcq",
        "stem": "A security team layers controls across physical, identity, perimeter, network, compute, "
                "application, and data so that if one layer is bypassed, others still protect the asset. "
                "Which strategy is this?",
        "options": [
            {"id": "A", "text": "Defense in depth"},
            {"id": "B", "text": "The shared responsibility model"},
            {"id": "C", "text": "Single sign-on"},
            {"id": "D", "text": "Federation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defense in depth uses multiple layers of protection so no single failure exposes "
                       "the asset; Microsoft describes layers from physical up through data.",
            "distractors": {
                "B": "The shared responsibility model divides duties between provider and customer; it is not a layered-defense strategy.",
                "C": "Single sign-on is an authentication convenience, not a layered security model.",
                "D": "Federation establishes trust between identity systems; it does not describe layered defenses.",
            },
            "exam_pattern": "Multiple protective layers (physical...data), no single point of failure = defense in depth.",
        },
        "references": ["Microsoft Learn (SC-900): Describe defense in depth"],
    },
    {
        "id": "sc900-con-003", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are guiding principles of the Zero Trust model? (Choose two.)",
        "options": [
            {"id": "A", "text": "Verify explicitly"},
            {"id": "B", "text": "Use least privilege access"},
            {"id": "C", "text": "Automatically trust any traffic that originates inside the corporate network"},
            {"id": "D", "text": "Rely on a strong network perimeter as the main line of defense"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Zero Trust's guiding principles are verify explicitly, use least privilege access, "
                       "and assume breach - two of which are listed here.",
            "distractors": {
                "C": "Zero Trust never trusts a request based on network location alone; it verifies every request.",
                "D": "Depending on a perimeter is the legacy model Zero Trust replaces, since the perimeter is assumed breached.",
            },
            "exam_pattern": "Zero Trust = verify explicitly + least privilege + assume breach; it does not trust the internal network by default.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Zero Trust model"],
    },
    {
        "id": "sc900-con-004", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "A security architect designs the environment on the assumption that attackers may already "
                "be present, so access is segmented to minimize blast radius and every request is verified. "
                "Which Zero Trust principle is being applied?",
        "options": [
            {"id": "A", "text": "Assume breach"},
            {"id": "B", "text": "Verify explicitly"},
            {"id": "C", "text": "Use least privilege access"},
            {"id": "D", "text": "Trust but verify the internal network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Assume breach' means operating as though an attacker is already inside: segment access, "
                       "minimize blast radius, and verify end-to-end rather than trusting the network.",
            "distractors": {
                "B": "Verify explicitly is about authenticating and authorizing on all available signals, not about assuming compromise and segmenting.",
                "C": "Least privilege limits each identity's access scope; the scenario's focus on assuming compromise and limiting blast radius is 'assume breach'.",
                "D": "'Trust but verify' is not a Zero Trust principle; Zero Trust is 'never trust, always verify'.",
            },
            "exam_pattern": "Segment access / minimize blast radius / assume attacker is inside = assume breach.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Zero Trust model"],
    },
    {
        "id": "sc900-con-005", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "A hospital must ensure that patient records cannot be altered by unauthorized parties and "
                "remain accurate and trustworthy. Which element of the CIA triad does this primarily address?",
        "options": [
            {"id": "A", "text": "Integrity"},
            {"id": "B", "text": "Confidentiality"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Integrity is about keeping data accurate and unaltered, ensuring it is not tampered "
                       "with by unauthorized parties.",
            "distractors": {
                "B": "Confidentiality is about preventing unauthorized viewing of data, not preventing unauthorized changes.",
                "C": "Availability is about data and systems being accessible when needed, not about preventing tampering.",
                "D": "Authentication verifies identity; it is not one of the three elements of the CIA triad.",
            },
            "exam_pattern": "Accurate / unaltered / not tampered with = integrity (the 'I' in CIA).",
        },
        "references": ["Microsoft Learn (SC-900): Describe common threats (CIA triad)"],
    },
    {
        "id": "sc900-con-006", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 1, "type": "fill",
        "stem": "A ransomware attack encrypts a company's files so that legitimate users can no longer open "
                "them, even though the data is unchanged and still private. Which element of the CIA triad is "
                "most directly compromised? Enter the one-word element.",
        "correct": ["availability"],
        "explanation": {
            "correct": "Availability means authorized users can access data and systems when needed. Ransomware "
                       "that blocks access to otherwise intact, private files directly attacks availability.",
            "distractors": {},
            "exam_pattern": "Data exists and stays private but users cannot reach it = availability loss.",
        },
        "references": ["Microsoft Learn (SC-900): Describe common threats (CIA triad)"],
    },

    # ===== sc9_identity_concepts ============================================
    {
        "id": "sc900-con-007", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 1, "type": "mcq",
        "stem": "With employees working from many locations and devices beyond the office network, modern "
                "security treats which of the following as the primary security perimeter?",
        "options": [
            {"id": "A", "text": "Identity"},
            {"id": "B", "text": "The corporate firewall"},
            {"id": "C", "text": "The on-premises network boundary"},
            {"id": "D", "text": "The physical office building"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "As resources and users move outside the traditional network, identity becomes the "
                       "primary security perimeter - the consistent control point for access.",
            "distractors": {
                "B": "A firewall protects a network boundary that users increasingly work outside of; it is no longer the primary perimeter.",
                "C": "The on-premises network boundary is exactly what cloud and remote work dissolve as the main perimeter.",
                "D": "Physical building security does not control access for remote, cloud-based work.",
            },
            "exam_pattern": "Cloud + remote work means 'identity is the new perimeter'.",
        },
        "references": ["Microsoft Learn (SC-900): Define identity as the primary security perimeter"],
    },
    {
        "id": "sc900-con-008", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 2, "type": "mcq",
        "stem": "After a user proves who they are during sign-in, the system then determines which files and "
                "applications they are permitted to use. This second step is known as:",
        "options": [
            {"id": "A", "text": "Authorization"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Auditing"},
            {"id": "D", "text": "Administration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authorization (AuthZ) decides what an already-authenticated identity is allowed to do "
                       "or access.",
            "distractors": {
                "B": "Authentication (AuthN) is the first step - proving who you are - not deciding what you can access.",
                "C": "Auditing records what happened; it does not grant access rights.",
                "D": "Administration is managing identities and resources, not the per-request access decision.",
            },
            "exam_pattern": "AuthN = who you are; AuthZ = what you're allowed to do.",
        },
        "references": ["Microsoft Learn (SC-900): Describe authentication and authorization"],
    },
    {
        "id": "sc900-con-009", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 2, "type": "mcq",
        "stem": "What is the primary role of an identity provider (IdP) such as Microsoft Entra ID?",
        "options": [
            {"id": "A", "text": "To create, store, and manage identities and provide authentication services to applications"},
            {"id": "B", "text": "To encrypt all network traffic between company sites"},
            {"id": "C", "text": "To physically secure datacenter hardware"},
            {"id": "D", "text": "To store and compile application source code"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An identity provider manages identity information and offers authentication (and often "
                       "authorization) services that apps can rely on.",
            "distractors": {
                "B": "Encrypting network traffic is a network-security function, not the role of an identity provider.",
                "C": "Physical datacenter security is the cloud provider's facilities responsibility, not an IdP function.",
                "D": "Storing source code describes a developer tool or repository, not an identity provider.",
            },
            "exam_pattern": "IdP = manages identities and authenticates them for relying apps (e.g., Microsoft Entra ID).",
        },
        "references": ["Microsoft Learn (SC-900): Describe identity providers"],
    },
    {
        "id": "sc900-con-010", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Users want to authenticate once and then reach many different applications without being "
                "prompted to sign in again for each one. Which capability delivers this experience?",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO)"},
            {"id": "B", "text": "Multifactor authentication (MFA)"},
            {"id": "C", "text": "Self-service password reset (SSPR)"},
            {"id": "D", "text": "Hashing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Single sign-on lets a user authenticate once and then access multiple applications "
                       "without re-entering credentials for each.",
            "distractors": {
                "B": "MFA adds verification factors to a sign-in; it does not reduce the number of sign-ins across apps.",
                "C": "SSPR lets users reset their own passwords; it is unrelated to signing in once for many apps.",
                "D": "Hashing is a cryptographic technique, not an authentication convenience.",
            },
            "exam_pattern": "Authenticate once, access many apps = single sign-on.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the concept of single sign-on"],
    },
    {
        "id": "sc900-con-011", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 3, "type": "mcq",
        "stem": "Two separate organizations establish a trust relationship so that users authenticated by one "
                "organization's identity system can access resources in the other using their home credentials. "
                "Which concept enables this cross-organization trust?",
        "options": [
            {"id": "A", "text": "Federation"},
            {"id": "B", "text": "Single sign-on within one directory"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "Symmetric encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Federation is a trust relationship between two identity systems that lets users of one "
                       "access resources in the other without a separate account.",
            "distractors": {
                "B": "SSO lets one identity reach many apps, but the cross-organization trust itself is provided by federation.",
                "C": "RBAC assigns permissions via roles inside a system; it does not establish trust between separate organizations.",
                "D": "Symmetric encryption protects data; it has nothing to do with inter-organization identity trust.",
            },
            "exam_pattern": "Trust between two separate identity systems so home credentials work across them = federation.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the concept of federation"],
    },
    {
        "id": "sc900-con-012", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft describes a modern identity infrastructure in terms of four pillars. Which option "
                "lists those four pillars of identity?",
        "options": [
            {"id": "A", "text": "Administration, authentication, authorization, and auditing"},
            {"id": "B", "text": "Confidentiality, integrity, availability, and accountability"},
            {"id": "C", "text": "Identities, devices, applications, and data"},
            {"id": "D", "text": "Prevention, detection, response, and recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The four pillars of identity are administration, authentication, authorization, and "
                       "auditing.",
            "distractors": {
                "B": "This is the CIA triad plus accountability - a security-goals model, not the identity pillars.",
                "C": "These are several of the Zero Trust pillars, not the four pillars of identity.",
                "D": "These are phases of incident handling, not identity pillars.",
            },
            "exam_pattern": "Four pillars of identity: administration, authentication, authorization, auditing.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the four pillars of an identity infrastructure"],
    },

    # ===== sc9_encryption_hashing ===========================================
    {
        "id": "sc900-con-013", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "An encryption method uses the same single secret key to both encrypt and decrypt the data. "
                "Which type of encryption is this?",
        "options": [
            {"id": "A", "text": "Symmetric encryption"},
            {"id": "B", "text": "Asymmetric encryption"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Digital signing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Symmetric encryption uses one shared secret key for both encryption and decryption.",
            "distractors": {
                "B": "Asymmetric encryption uses a key pair (public and private), not a single shared key.",
                "C": "Hashing is a one-way function that uses no key and cannot be reversed to the original data.",
                "D": "Digital signing proves authenticity and integrity; it is not a symmetric-vs-asymmetric encryption type.",
            },
            "exam_pattern": "Same key encrypts and decrypts = symmetric.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption and hashing"],
    },
    {
        "id": "sc900-con-014", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "A system encrypts data with the recipient's public key, and only the matching private key can "
                "decrypt it. Which type of encryption is this?",
        "options": [
            {"id": "A", "text": "Asymmetric encryption"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Tokenization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Asymmetric encryption uses a public/private key pair: one key encrypts and the other "
                       "decrypts.",
            "distractors": {
                "B": "Symmetric encryption uses a single shared key, not a public/private pair.",
                "C": "Hashing is one-way and keyless; it does not decrypt back to the original.",
                "D": "Tokenization substitutes a value with a token; it is not public/private key cryptography.",
            },
            "exam_pattern": "Public key encrypts, private key decrypts (a key pair) = asymmetric.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption and hashing"],
    },
    {
        "id": "sc900-con-015", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "To store passwords safely, a system converts each password into a fixed-length value using a "
                "one-way function that cannot be reversed back to the original text. What is this technique?",
        "options": [
            {"id": "A", "text": "Hashing"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Asymmetric encryption"},
            {"id": "D", "text": "Digital signing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Hashing is a one-way function that produces a fixed-length value and cannot be reversed, "
                       "which makes it suitable for storing passwords and verifying integrity.",
            "distractors": {
                "B": "Symmetric encryption is reversible with the key, so it is not a one-way function.",
                "C": "Asymmetric encryption is also reversible with the private key; it is two-way, not one-way.",
                "D": "Digital signing uses hashing plus keys to prove authenticity, but the one-way transform itself is hashing.",
            },
            "exam_pattern": "One-way, fixed-length, not reversible, no key = hashing.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption and hashing"],
    },
    {
        "id": "sc900-con-016", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "Encrypting data while it moves between a user's browser and a web server (for example, with "
                "TLS) is an example of protecting data in which state?",
        "options": [
            {"id": "A", "text": "In transit"},
            {"id": "B", "text": "At rest"},
            {"id": "C", "text": "In use"},
            {"id": "D", "text": "In archive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data in transit is data moving across a network between locations; encrypting it (e.g., "
                       "with TLS) protects it while in motion.",
            "distractors": {
                "B": "Data at rest is stored data (on a disk or in a database), not data moving over the network.",
                "C": "Data in use is data being actively processed in memory, not data in motion.",
                "D": "'In archive' is not one of the recognized data states (at rest, in transit, in use).",
            },
            "exam_pattern": "Data states: at rest (stored), in transit (moving), in use (processing).",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption and hashing"],
    },
    {
        "id": "sc900-con-017", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "fill",
        "stem": "Unlike encryption, this cryptographic technique is one-way: it converts input into a "
                "fixed-length value that is not meant to be reversed, and it is commonly used to verify "
                "integrity or to store passwords. Name the technique (one word).",
        "correct": ["hashing", "hash"],
        "explanation": {
            "correct": "Hashing is a one-way transform producing a fixed-length value; it is not reversible, "
                       "unlike encryption which is designed to be decrypted.",
            "distractors": {},
            "exam_pattern": "One-way and not reversible = hashing; two-way and reversible with a key = encryption.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption and hashing"],
    },

    # ===== sc9_governance_concepts ==========================================
    {
        "id": "sc900-con-018", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 2, "type": "mcq",
        "stem": "An organization defines the policies, standards, roles, and processes that direct and control "
                "how it manages and protects its data and resources. Within governance, risk, and compliance "
                "(GRC), this activity is which function?",
        "options": [
            {"id": "A", "text": "Governance"},
            {"id": "B", "text": "Risk"},
            {"id": "C", "text": "Compliance"},
            {"id": "D", "text": "Authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance is the system of policies, standards, roles, and processes that direct and "
                       "control how an organization manages and secures its data and resources.",
            "distractors": {
                "B": "Risk is about identifying and mitigating threats, not setting the governing policies.",
                "C": "Compliance is about adhering to external laws and regulations, not defining internal governing policy.",
                "D": "Authentication is an identity function and is not one of the three GRC pillars.",
            },
            "exam_pattern": "Setting policies/standards/processes that direct and control the org = governance.",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
    {
        "id": "sc900-con-019", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Identifying potential threats, assessing their likelihood and impact, and deciding how to "
                "treat or mitigate them is which GRC function?",
        "options": [
            {"id": "A", "text": "Risk management"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Compliance"},
            {"id": "D", "text": "Encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk management is the process of identifying, assessing, and responding to threats to "
                       "the organization.",
            "distractors": {
                "B": "Governance sets the directing policies; it is not the act of assessing and treating specific threats.",
                "C": "Compliance is about meeting legal and regulatory obligations, not evaluating threat likelihood and impact.",
                "D": "Encryption is a protective control, not a GRC discipline.",
            },
            "exam_pattern": "Identify, assess, and mitigate threats = risk management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
    {
        "id": "sc900-con-020", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 2, "type": "mcq",
        "stem": "An organization must adhere to external laws and regulations such as GDPR and HIPAA. Meeting "
                "these legal and regulatory obligations falls under which GRC function?",
        "options": [
            {"id": "A", "text": "Compliance"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Risk"},
            {"id": "D", "text": "Availability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Compliance is adhering to the laws, regulations, and standards (such as GDPR or HIPAA) "
                       "that apply to the organization.",
            "distractors": {
                "B": "Governance defines internal direction and control; meeting external regulations specifically is compliance.",
                "C": "Risk is about evaluating and mitigating threats, not conforming to specific regulations.",
                "D": "Availability is a CIA-triad element, not a GRC function.",
            },
            "exam_pattern": "Adhering to external laws/regulations/standards (GDPR, HIPAA...) = compliance.",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
    {
        "id": "sc900-con-021", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 3, "type": "mcq",
        "stem": "A compliance officer confirms the company's controls satisfy GDPR, while leadership sets the "
                "policies and standards that direct how security is run. Mapping these to GRC, verifying GDPR "
                "adherence is compliance, and leadership setting the directing policy is which function?",
        "options": [
            {"id": "A", "text": "Governance"},
            {"id": "B", "text": "Risk"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Federation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leadership defining the policies and standards that direct and control the organization "
                       "is the governance function of GRC.",
            "distractors": {
                "B": "Risk is identifying and mitigating threats, not setting the directing policy.",
                "C": "Hashing is a cryptographic technique, unrelated to GRC functions.",
                "D": "Federation is an identity-trust concept, not a GRC function.",
            },
            "exam_pattern": "Leadership setting directing policy = governance; meeting GDPR/HIPAA = compliance; threat handling = risk.",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
]
