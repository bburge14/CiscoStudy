"""Microsoft SC-900 pool - Round 2 expansion (all four domains).

Deepens the verified SC-900 bank with ~108 additional original, objective-aligned
items that go beyond the round-1 pools (content_sc900_concepts/entra/security/
compliance.py) without duplicating them. Distribution mirrors the published exam
weighting: Security solutions 37%, Microsoft Entra 28%, Compliance solutions 22%,
foundational Concepts 13%.

Ids follow sc900-<prefix>-r2-NNN, where the per-domain prefix matches round 1
(con / entra / sec / comp). build_content.py auto-discovers this file via its
content_sc900_*.py glob and shuffles option order (seeded by id), so a key
authored as "A" is not positionally biased; authored positions are rotated here
anyway. Every wrong option carries a distractor note, each item cites the
Microsoft Learn (SC-900) area, and current product names are used throughout
(Microsoft Entra ID, Microsoft Defender XDR, Microsoft Defender for Cloud,
Microsoft Sentinel, Microsoft Purview, Microsoft Priva). Fundamentals depth only
- which capability/tool fits a need, when-to-use, and concept definitions - with
no pricing, no numeric SKU limits, no preview-only trivia, and never real or
memorized exam items.
"""

QUESTIONS = [
    # =====================================================================
    # Domain 1 - Concepts of Security, Compliance & Identity (14 items)
    # =====================================================================

    # ----- sc9_security_methodologies ------------------------------------
    {
        "id": "sc900-con-r2-001", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft's Zero Trust model applies defenses across seven technology pillars. Which of the "
                "following is one of those pillars?",
        "options": [
            {"id": "A", "text": "Infrastructure"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Compliance"},
            {"id": "D", "text": "Encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The seven Zero Trust pillars are identities, endpoints (devices), applications, data, "
                       "infrastructure, networks, and security operations (SecOps). Infrastructure is one of them.",
            "distractors": {
                "B": "Governance is a GRC discipline, not one of the seven Zero Trust technology pillars.",
                "C": "Compliance is a GRC function, not a Zero Trust pillar.",
                "D": "Encryption is a protective control used within pillars, not itself a Zero Trust pillar.",
            },
            "exam_pattern": "Zero Trust pillars: identities, endpoints, apps, data, infrastructure, networks, SecOps.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Zero Trust model (pillars)"],
    },
    {
        "id": "sc900-con-r2-002", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "A system is designed to always authenticate and authorize every request using all available "
                "signals - identity, location, device health, and the resource requested - before granting "
                "access. Which Zero Trust guiding principle does this describe?",
        "options": [
            {"id": "A", "text": "Verify explicitly"},
            {"id": "B", "text": "Assume breach"},
            {"id": "C", "text": "Use least privilege access"},
            {"id": "D", "text": "Trust the internal network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Verify explicitly means always authenticating and authorizing based on all available data "
                       "points (identity, location, device health, service, workload, data classification).",
            "distractors": {
                "B": "Assume breach is about segmenting and minimizing blast radius on the assumption attackers are already present, not evaluating signals per request.",
                "C": "Least privilege limits each identity's access scope; it is not the signal-based verification principle.",
                "D": "Trusting the internal network is the legacy model Zero Trust replaces, not a Zero Trust principle.",
            },
            "exam_pattern": "Authenticate/authorize on all available signals every time = verify explicitly.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Zero Trust model (principles)"],
    },
    {
        "id": "sc900-con-r2-003", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft's defense-in-depth model, encrypting information at rest and in transit so it stays "
                "protected even if other layers are bypassed belongs to which layer?",
        "options": [
            {"id": "A", "text": "The data layer"},
            {"id": "B", "text": "The physical security layer"},
            {"id": "C", "text": "The perimeter layer"},
            {"id": "D", "text": "The network layer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The data layer is the innermost defense-in-depth layer; controls such as encryption and "
                       "access control protect the information itself.",
            "distractors": {
                "B": "The physical layer protects the datacenter and hardware from physical access, not the data's encryption.",
                "C": "The perimeter layer uses controls like DDoS protection and perimeter firewalls, not data encryption.",
                "D": "The network layer segments and limits communication between resources; encrypting the data itself is the data layer.",
            },
            "exam_pattern": "Defense-in-depth layers: physical, identity/access, perimeter, network, compute, application, data.",
        },
        "references": ["Microsoft Learn (SC-900): Describe defense in depth"],
    },
    {
        "id": "sc900-con-r2-004", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 3, "type": "mcq",
        "stem": "Compared with a SaaS offering, moving to an IaaS deployment shifts responsibility for which "
                "additional layer onto the customer under the shared responsibility model?",
        "options": [
            {"id": "A", "text": "The operating system (for example, patching and hardening the VM OS)"},
            {"id": "B", "text": "The physical datacenter"},
            {"id": "C", "text": "The physical network hardware"},
            {"id": "D", "text": "The physical host servers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In IaaS the customer manages the operating system, applications, and data; in SaaS the "
                       "provider manages the OS and application. So IaaS adds OS responsibility to the customer.",
            "distractors": {
                "B": "The physical datacenter is always the provider's responsibility in every model.",
                "C": "The physical network is always the provider's responsibility, not shifted to the customer in IaaS.",
                "D": "Physical host servers are always the provider's responsibility in every cloud model.",
            },
            "exam_pattern": "IaaS customer owns OS + apps + data; physical layers are always the provider's.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the shared responsibility model"],
    },
    {
        "id": "sc900-con-r2-005", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_security_methodologies", "difficulty": 2, "type": "mcq",
        "stem": "An organization encrypts a customer database so that only authorized staff can read its "
                "contents, preventing unauthorized disclosure. Which element of the CIA triad does this "
                "primarily support?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Authorization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Confidentiality is about keeping data private and preventing unauthorized viewing or "
                       "disclosure - exactly what restricting who can read the database achieves.",
            "distractors": {
                "B": "Integrity is about keeping data accurate and unaltered, not about preventing unauthorized reading.",
                "C": "Availability is about data and systems being accessible when needed, not about secrecy.",
                "D": "Authorization is an access-control process; it is not one of the three CIA-triad elements.",
            },
            "exam_pattern": "Prevent unauthorized disclosure / keep data private = confidentiality.",
        },
        "references": ["Microsoft Learn (SC-900): Describe common threats (CIA triad)"],
    },

    # ----- sc9_identity_concepts -----------------------------------------
    {
        "id": "sc900-con-r2-006", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Single sign-on improves user experience by reducing sign-in prompts. What is a corresponding "
                "security consideration that organizations address when using SSO?",
        "options": [
            {"id": "A", "text": "If the single credential is compromised, all connected apps are at risk, so SSO is typically paired with strong authentication such as MFA"},
            {"id": "B", "text": "SSO forces users to maintain a separate password for every application"},
            {"id": "C", "text": "SSO removes the need for an identity provider"},
            {"id": "D", "text": "SSO prevents federation between organizations"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With SSO one credential unlocks many apps, so protecting that credential is critical; "
                       "organizations commonly combine SSO with MFA and Conditional Access.",
            "distractors": {
                "B": "SSO does the opposite - it lets one authentication reach many apps, reducing separate passwords.",
                "C": "SSO relies on an identity provider to authenticate the user; it does not remove it.",
                "D": "SSO and federation work together; SSO does not prevent federation.",
            },
            "exam_pattern": "SSO concentrates risk on one credential -> pair with MFA/Conditional Access.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the concept of single sign-on"],
    },
    {
        "id": "sc900-con-r2-007", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 3, "type": "mcq",
        "stem": "Among the four pillars of identity, which pillar is concerned with collecting and reviewing "
                "events - such as sign-ins and changes - to monitor for suspicious activity and meet reporting "
                "requirements?",
        "options": [
            {"id": "A", "text": "Auditing"},
            {"id": "B", "text": "Administration"},
            {"id": "C", "text": "Authentication"},
            {"id": "D", "text": "Authorization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Auditing covers the tracking, logging, and review of identity events so organizations can "
                       "monitor activity and satisfy reporting and compliance needs.",
            "distractors": {
                "B": "Administration is about creating and managing identities and their lifecycle, not reviewing event logs.",
                "C": "Authentication is the process of proving who a user is, not monitoring events.",
                "D": "Authorization decides what an authenticated identity can access, not logging and reviewing activity.",
            },
            "exam_pattern": "Four pillars of identity: administration, authentication, authorization, auditing (events/monitoring).",
        },
        "references": ["Microsoft Learn (SC-900): Describe the four pillars of an identity infrastructure"],
    },
    {
        "id": "sc900-con-r2-008", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_identity_concepts", "difficulty": 3, "type": "mcq",
        "stem": "In a federated single sign-on flow, the application or service that trusts an identity provider "
                "to authenticate users and then consumes that authentication is known as the:",
        "options": [
            {"id": "A", "text": "Service provider (relying party)"},
            {"id": "B", "text": "Identity provider"},
            {"id": "C", "text": "Certificate authority"},
            {"id": "D", "text": "Domain controller"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The service provider (relying party) is the app/service that relies on the identity "
                       "provider's authentication to grant access.",
            "distractors": {
                "B": "The identity provider authenticates the user and issues tokens; the party that trusts and consumes them is the service provider.",
                "C": "A certificate authority issues digital certificates; it is not the relying app in a federation.",
                "D": "A domain controller authenticates within an on-premises Active Directory domain; it is not the relying party in a federation trust.",
            },
            "exam_pattern": "IdP authenticates; the app that trusts it = service provider / relying party.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the concept of federation"],
    },

    # ----- sc9_encryption_hashing ----------------------------------------
    {
        "id": "sc900-con-r2-009", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "A sender creates a value from a message using their private key; recipients verify it with the "
                "sender's public key, confirming the message truly came from the sender and was not altered. "
                "What is this technique?",
        "options": [
            {"id": "A", "text": "Digital signing (a digital signature)"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Hashing on its own"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Digital signing uses the sender's private key to sign and the public key to verify, "
                       "providing authenticity and integrity (and non-repudiation).",
            "distractors": {
                "B": "Symmetric encryption uses one shared key to keep data secret; it does not prove sender authenticity.",
                "C": "Hashing alone proves integrity but, without a signing key, does not prove who sent the message.",
                "D": "Single sign-on is an authentication convenience, not a cryptographic signing technique.",
            },
            "exam_pattern": "Private key signs, public key verifies -> authenticity + integrity = digital signing.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption, hashing, and signing"],
    },
    {
        "id": "sc900-con-r2-010", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 2, "type": "mcq",
        "stem": "Protecting data while it is actively being processed in a system's memory - for example using "
                "confidential computing - protects data in which state?",
        "options": [
            {"id": "A", "text": "In use"},
            {"id": "B", "text": "At rest"},
            {"id": "C", "text": "In transit"},
            {"id": "D", "text": "In archive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data in use is data being actively processed in memory; protecting it (e.g., with "
                       "confidential computing) secures this state.",
            "distractors": {
                "B": "Data at rest is stored data on disk or in a database, not data actively in memory.",
                "C": "Data in transit is data moving across a network, not data being processed.",
                "D": "'In archive' is not one of the three recognized data states (at rest, in transit, in use).",
            },
            "exam_pattern": "Data being processed in memory = data in use.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption (data states)"],
    },
    {
        "id": "sc900-con-r2-011", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_encryption_hashing", "difficulty": 1, "type": "fill",
        "stem": "Encryption applied to data that is stored on a disk or in a database - as opposed to data "
                "moving over a network - protects data at ___. Enter the missing one-word state.",
        "correct": ["rest"],
        "explanation": {
            "correct": "Data at rest is stored data (on a disk, in a database, or in storage); encrypting it "
                       "protects it if the media is lost or stolen.",
            "distractors": {},
            "exam_pattern": "Stored data = at rest; moving data = in transit; processing data = in use.",
        },
        "references": ["Microsoft Learn (SC-900): Describe encryption (data states)"],
    },

    # ----- sc9_governance_concepts ---------------------------------------
    {
        "id": "sc900-con-r2-012", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 2, "type": "mcq",
        "stem": "After assessing a threat, an organization decides how to treat it - choosing to mitigate, "
                "transfer, accept, or avoid the risk. Within risk management, this activity is called:",
        "options": [
            {"id": "A", "text": "Risk response (risk treatment)"},
            {"id": "B", "text": "Governance"},
            {"id": "C", "text": "Compliance"},
            {"id": "D", "text": "Authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk response (treatment) is deciding how to handle an assessed risk - typically "
                       "mitigate, transfer, accept, or avoid it.",
            "distractors": {
                "B": "Governance sets the directing policies and standards; it is not the act of treating a specific risk.",
                "C": "Compliance is adhering to external laws and regulations, not choosing how to treat a risk.",
                "D": "Authentication is an identity function, unrelated to risk treatment decisions.",
            },
            "exam_pattern": "Decide to mitigate/transfer/accept/avoid a risk = risk response (treatment).",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
    {
        "id": "sc900-con-r2-013", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 3, "type": "mcq",
        "stem": "An organization voluntarily adopts ISO/IEC 27001 to structure its security controls and must "
                "also meet the GDPR law. Which statement correctly categorizes these two?",
        "options": [
            {"id": "A", "text": "ISO/IEC 27001 is a standard (framework) an organization can adopt; GDPR is a regulation (law) it must comply with"},
            {"id": "B", "text": "Both ISO/IEC 27001 and GDPR are encryption algorithms"},
            {"id": "C", "text": "ISO/IEC 27001 is a law and GDPR is an optional framework"},
            {"id": "D", "text": "Both are identity providers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A standard/framework like ISO/IEC 27001 is adopted to organize controls, while a "
                       "regulation like GDPR is a legal requirement that compliance must satisfy.",
            "distractors": {
                "B": "Neither is an encryption algorithm; they are a standard and a regulation.",
                "C": "This reverses them - ISO/IEC 27001 is the voluntary standard and GDPR is the law.",
                "D": "Neither is an identity provider; they are governance/compliance frameworks and laws.",
            },
            "exam_pattern": "Standard/framework = adoptable (ISO 27001); regulation = legal obligation (GDPR).",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },
    {
        "id": "sc900-con-r2-014", "exam": "sc900", "domain": "sc9_concepts",
        "subtopic": "sc9_governance_concepts", "difficulty": 1, "type": "fill",
        "stem": "In the GRC acronym used across security and compliance, the three letters stand for governance, "
                "risk, and ___. Enter the missing one-word term.",
        "correct": ["compliance"],
        "explanation": {
            "correct": "GRC stands for governance, risk, and compliance - the three disciplines for directing, "
                       "protecting, and meeting obligations across an organization.",
            "distractors": {},
            "exam_pattern": "GRC = governance (direct/control) + risk (identify/treat threats) + compliance (meet laws/standards).",
        },
        "references": ["Microsoft Learn (SC-900): Describe governance, risk, and compliance (GRC)"],
    },

    # =====================================================================
    # Domain 2 - Capabilities of Microsoft Entra (30 items)
    # =====================================================================

    # ----- sc9_entra_identity_types --------------------------------------
    {
        "id": "sc900-entra-r2-001", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 3, "type": "mcq",
        "stem": "When an application is registered in Microsoft Entra ID, the local object created in a tenant "
                "to represent that app - so it can be granted permissions and sign in - is called a:",
        "options": [
            {"id": "A", "text": "Service principal"},
            {"id": "B", "text": "Security group"},
            {"id": "C", "text": "Administrative unit"},
            {"id": "D", "text": "Conditional Access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A service principal is the local representation (identity) of an application in a tenant, "
                       "used to assign the app access and permissions. (A managed identity is a special, "
                       "automatically managed service principal for Azure resources.)",
            "distractors": {
                "B": "A security group bundles users/devices for access assignment; it does not represent an application.",
                "C": "An administrative unit scopes administration over a subset of objects; it is not an app's identity.",
                "D": "A Conditional Access policy enforces sign-in conditions; it is not an application identity.",
            },
            "exam_pattern": "Local identity of a registered app in a tenant = service principal.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (workload identities)"],
    },
    {
        "id": "sc900-entra-r2-002", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "Employees use their personal phones and home laptops to reach some company resources. The "
                "organization wants these personal devices to have an identity in Microsoft Entra ID while it "
                "keeps only limited management of them. Which device identity state fits?",
        "options": [
            {"id": "A", "text": "Microsoft Entra registered"},
            {"id": "B", "text": "Microsoft Entra joined"},
            {"id": "C", "text": "Microsoft Entra hybrid joined"},
            {"id": "D", "text": "A managed identity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra registered is the bring-your-own-device (BYOD) / personal-device state: "
                       "the device gets an Entra identity while the organization retains limited management.",
            "distractors": {
                "B": "Microsoft Entra joined is for organization-owned devices joined only to the cloud, not personal BYOD devices.",
                "C": "Hybrid joined devices are organization-owned and joined to both on-premises AD and Entra ID, not personal BYOD.",
                "D": "A managed identity is an application identity for Azure resources, not a device state.",
            },
            "exam_pattern": "Personal/BYOD device with an Entra identity, limited management = Entra registered.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (device identities)"],
    },
    {
        "id": "sc900-entra-r2-003", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "A company-owned Windows laptop is joined directly to Microsoft Entra ID only (not to an "
                "on-premises Active Directory domain), and users sign in with their organizational account. "
                "What is this device state called?",
        "options": [
            {"id": "A", "text": "Microsoft Entra joined"},
            {"id": "B", "text": "Microsoft Entra hybrid joined"},
            {"id": "C", "text": "Microsoft Entra registered"},
            {"id": "D", "text": "Federated"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra joined devices are organization-owned and joined only to Microsoft Entra "
                       "ID, requiring an organizational account to sign in - no on-premises AD join.",
            "distractors": {
                "B": "Hybrid joined devices are joined to BOTH on-premises Active Directory and Entra ID; here there is no on-prem AD.",
                "C": "Registered is for personal/BYOD devices, not an organization-owned cloud-joined laptop.",
                "D": "'Federated' describes an identity trust relationship, not a device join state.",
            },
            "exam_pattern": "Org-owned, cloud-only join, org account to sign in = Microsoft Entra joined.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (device identities)"],
    },
    {
        "id": "sc900-entra-r2-004", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 3, "type": "mcq",
        "stem": "A retailer is building a customer-facing shopping app where consumers create their own accounts "
                "(or sign in with social identities like Google) to access the retailer's services. Which "
                "Microsoft Entra capability is designed for these customer/consumer identities?",
        "options": [
            {"id": "A", "text": "Microsoft Entra External ID for customers (CIAM)"},
            {"id": "B", "text": "B2B collaboration"},
            {"id": "C", "text": "Managed identities"},
            {"id": "D", "text": "Privileged Identity Management (PIM)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra External ID for customers (customer identity and access management, CIAM; "
                       "formerly Azure AD B2C) handles consumer sign-up and sign-in, including social identities.",
            "distractors": {
                "B": "B2B collaboration invites partner-organization employees as guests; it is not for consumer/customer accounts.",
                "C": "Managed identities are for Azure resources, not external customers.",
                "D": "PIM governs just-in-time privileged role activation, not customer identities.",
            },
            "exam_pattern": "Consumer/customer sign-up and sign-in to your apps = External ID for customers (CIAM).",
        },
        "references": ["Microsoft Learn (SC-900): Describe external identities"],
    },
    {
        "id": "sc900-entra-r2-005", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 3, "type": "mcq",
        "stem": "Which type of Microsoft Entra group is used to grant its members access to resources such as "
                "applications or Azure roles, as distinct from a group that mainly provides shared "
                "collaboration resources like a mailbox and calendar?",
        "options": [
            {"id": "A", "text": "A security group"},
            {"id": "B", "text": "A Microsoft 365 group"},
            {"id": "C", "text": "An administrative unit"},
            {"id": "D", "text": "A managed identity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security groups are used to assign access to resources (apps, roles, SharePoint, etc.) "
                       "for their members.",
            "distractors": {
                "B": "A Microsoft 365 group provides shared collaboration resources (mailbox, calendar, SharePoint site) for teamwork, not primarily resource-access assignment.",
                "C": "An administrative unit scopes administration over objects; it is not a membership group for access.",
                "D": "A managed identity is an application identity for Azure resources, not a group.",
            },
            "exam_pattern": "Grant members access to resources = security group; collaboration mailbox/site = Microsoft 365 group.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (groups)"],
    },
    {
        "id": "sc900-entra-r2-006", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants group membership to update automatically based on user attributes - for "
                "example, automatically including everyone whose department is 'Sales' - instead of adding and "
                "removing members by hand. Which membership type provides this?",
        "options": [
            {"id": "A", "text": "Dynamic membership (a dynamic group)"},
            {"id": "B", "text": "Assigned membership"},
            {"id": "C", "text": "An administrative unit"},
            {"id": "D", "text": "A service principal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dynamic membership groups use rules based on user or device attributes to add and remove "
                       "members automatically as those attributes change.",
            "distractors": {
                "B": "Assigned membership requires an administrator to add and remove each member manually.",
                "C": "An administrative unit restricts administrative scope; it is not an attribute-driven membership mechanism.",
                "D": "A service principal is an application identity, not a way to populate group membership.",
            },
            "exam_pattern": "Membership updates automatically from attributes = dynamic membership group.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (groups)"],
    },
    {
        "id": "sc900-entra-r2-007", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "fill",
        "stem": "Synchronizing on-premises Active Directory accounts to Microsoft Entra ID so users have a "
                "single identity across on-premises and cloud resources is known as ___ identity. Enter the "
                "missing one-word term.",
        "correct": ["hybrid"],
        "explanation": {
            "correct": "Hybrid identity links on-premises Active Directory with Microsoft Entra ID (via "
                       "synchronization), giving users one identity across on-premises and cloud.",
            "distractors": {},
            "exam_pattern": "One identity across on-prem AD + cloud (via sync) = hybrid identity.",
        },
        "references": ["Microsoft Learn (SC-900): Describe hybrid identity"],
    },

    # ----- sc9_entra_authentication --------------------------------------
    {
        "id": "sc900-entra-r2-008", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Entra authentication method is considered phishing-resistant because it uses "
                "public-key cryptography bound to the device and a user gesture, with no shared secret that can "
                "be stolen or replayed?",
        "options": [
            {"id": "A", "text": "FIDO2 security keys"},
            {"id": "B", "text": "SMS text-message codes"},
            {"id": "C", "text": "Security questions"},
            {"id": "D", "text": "A reusable password"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FIDO2 security keys use public-key cryptography with the private key held on the device, "
                       "making them phishing-resistant and passwordless.",
            "distractors": {
                "B": "SMS codes can be intercepted or phished (e.g., SIM swapping) and are not phishing-resistant.",
                "C": "Security questions are shared secrets that can be guessed or researched; they are weak, not phishing-resistant.",
                "D": "A reusable password is exactly the shared secret that phishing-resistant methods avoid.",
            },
            "exam_pattern": "Public-key, device-bound, no shared secret = phishing-resistant (FIDO2 / Windows Hello).",
        },
        "references": ["Microsoft Learn (SC-900): Describe passwordless authentication"],
    },
    {
        "id": "sc900-entra-r2-009", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "A fingerprint scan used to verify a user at sign-in satisfies which authentication factor "
                "category?",
        "options": [
            {"id": "A", "text": "Something you are (biometric / inherence)"},
            {"id": "B", "text": "Something you know"},
            {"id": "C", "text": "Something you have"},
            {"id": "D", "text": "Something you do"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A fingerprint is a biometric - the 'something you are' (inherence) factor category.",
            "distractors": {
                "B": "'Something you know' is a knowledge factor such as a password or PIN, not a fingerprint.",
                "C": "'Something you have' is a possession factor such as a phone or security key, not a biometric.",
                "D": "'Something you do' (behavioral) is not the category of a fingerprint, which is a physical biometric.",
            },
            "exam_pattern": "Biometric (fingerprint/face) = something you are.",
        },
        "references": ["Microsoft Learn (SC-900): Describe multifactor authentication (factor categories)"],
    },
    {
        "id": "sc900-entra-r2-010", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Entra capability helps prevent users from choosing weak or easily guessed "
                "passwords by enforcing a global banned-password list plus a custom list of terms?",
        "options": [
            {"id": "A", "text": "Microsoft Entra Password Protection"},
            {"id": "B", "text": "Self-service password reset (SSPR)"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Privileged Identity Management (PIM)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra Password Protection blocks known-weak and banned passwords (global and "
                       "custom lists), including for on-premises Active Directory when deployed there.",
            "distractors": {
                "B": "SSPR lets users reset their own passwords; it does not enforce banned-password lists.",
                "C": "Conditional Access evaluates sign-in conditions; it does not police password strength.",
                "D": "PIM manages privileged role activation, not password quality.",
            },
            "exam_pattern": "Block weak/banned passwords (global + custom list) = Microsoft Entra Password Protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe password protection and management capabilities"],
    },
    {
        "id": "sc900-entra-r2-011", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 3, "type": "mcq",
        "stem": "An administrator needs to give a new employee a time-limited passcode so they can register "
                "passwordless methods (or regain access) when they have no other credentials yet. Which "
                "Microsoft Entra feature provides this?",
        "options": [
            {"id": "A", "text": "A Temporary Access Pass (TAP)"},
            {"id": "B", "text": "A FIDO2 security key"},
            {"id": "C", "text": "A security question"},
            {"id": "D", "text": "Self-service password reset (SSPR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Temporary Access Pass is a time-limited passcode an admin issues so a user can onboard "
                       "or recover access and register stronger methods.",
            "distractors": {
                "B": "A FIDO2 key is a passwordless method the user registers; it is not the temporary bootstrap credential an admin issues.",
                "C": "A security question is a weak knowledge factor, not a time-limited onboarding passcode.",
                "D": "SSPR lets an existing user reset a forgotten password; it does not bootstrap a brand-new user with no credentials.",
            },
            "exam_pattern": "Time-limited passcode to onboard/recover and register methods = Temporary Access Pass.",
        },
        "references": ["Microsoft Learn (SC-900): Describe authentication methods"],
    },
    {
        "id": "sc900-entra-r2-012", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "What is the main security advantage of passwordless authentication over password-based "
                "sign-in?",
        "options": [
            {"id": "A", "text": "There is no password to phish, guess, or reuse, which reduces credential-based attacks"},
            {"id": "B", "text": "It removes the need for any user verification at all"},
            {"id": "C", "text": "It makes every sign-in anonymous"},
            {"id": "D", "text": "It eliminates the need for an identity provider"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Passwordless methods replace the password with a stronger factor (biometric/key), so "
                       "there is no password to steal, phish, guess, or reuse.",
            "distractors": {
                "B": "Passwordless still verifies the user (e.g., biometric, PIN, key) - it does not remove verification.",
                "C": "Passwordless sign-in still identifies and authenticates the user; it is not anonymous.",
                "D": "An identity provider still authenticates the user; passwordless does not remove it.",
            },
            "exam_pattern": "Passwordless benefit = no password to phish/guess/reuse.",
        },
        "references": ["Microsoft Learn (SC-900): Describe passwordless authentication"],
    },
    {
        "id": "sc900-entra-r2-013", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about SMS (text-message) one-time codes as a second authentication factor is "
                "accurate?",
        "options": [
            {"id": "A", "text": "They add a second factor but are considered less secure and less phishing-resistant than app-based or FIDO2 methods"},
            {"id": "B", "text": "They are a passwordless primary authentication method"},
            {"id": "C", "text": "They are more phishing-resistant than FIDO2 security keys"},
            {"id": "D", "text": "They are a 'something you are' biometric factor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SMS codes do strengthen sign-in as a possession-based second factor, but they are more "
                       "susceptible to interception/SIM-swap than Authenticator or FIDO2 methods.",
            "distractors": {
                "B": "SMS codes are a second factor added to a password, not a passwordless primary method.",
                "C": "FIDO2 security keys are more phishing-resistant than SMS, not the other way around.",
                "D": "An SMS code is a possession-based ('something you have') factor, not a biometric.",
            },
            "exam_pattern": "SMS = valid second factor but weaker/less phishing-resistant than app push or FIDO2.",
        },
        "references": ["Microsoft Learn (SC-900): Describe authentication methods"],
    },
    {
        "id": "sc900-entra-r2-014", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 1, "type": "multi",
        "stem": "Which TWO of the following are Microsoft Entra authentication methods that can satisfy a "
                "multifactor authentication requirement? (Choose two.)",
        "options": [
            {"id": "A", "text": "A Microsoft Authenticator push approval"},
            {"id": "B", "text": "A FIDO2 security key"},
            {"id": "C", "text": "A network security group"},
            {"id": "D", "text": "A sensitivity label"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Microsoft Authenticator (push/passwordless) and FIDO2 security keys are valid "
                       "authentication methods that can meet an MFA requirement.",
            "distractors": {
                "C": "A network security group filters network traffic; it is not an authentication method.",
                "D": "A sensitivity label classifies and protects content; it is not an authentication method.",
            },
            "exam_pattern": "MFA-capable methods: Authenticator, FIDO2 keys, Windows Hello, OATH/SMS/voice (NSGs/labels are not).",
        },
        "references": ["Microsoft Learn (SC-900): Describe authentication methods"],
    },
    {
        "id": "sc900-entra-r2-015", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "Before a user can use self-service password reset (SSPR) to reset a forgotten password, what "
                "must they typically do first?",
        "options": [
            {"id": "A", "text": "Register their authentication methods (such as a phone, email, or the Authenticator app)"},
            {"id": "B", "text": "Be assigned the Global Administrator role"},
            {"id": "C", "text": "Create a managed identity"},
            {"id": "D", "text": "Configure a Conditional Access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSPR relies on the user having registered authentication/contact methods so they can "
                       "verify their identity before resetting the password.",
            "distractors": {
                "B": "SSPR is for ordinary users; it does not require the Global Administrator role.",
                "C": "Managed identities are app identities for Azure resources, unrelated to a user's SSPR registration.",
                "D": "Conditional Access governs sign-in conditions; it is not a prerequisite the end user configures for SSPR.",
            },
            "exam_pattern": "SSPR prerequisite = user registers verification methods.",
        },
        "references": ["Microsoft Learn (SC-900): Describe self-service password reset"],
    },

    # ----- sc9_entra_access_management -----------------------------------
    {
        "id": "sc900-entra-r2-016", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "In a Conditional Access policy, requiring multifactor authentication or a compliant device "
                "before access is granted is an example of which part of the policy?",
        "options": [
            {"id": "A", "text": "Grant controls"},
            {"id": "B", "text": "Session controls"},
            {"id": "C", "text": "Assignments (conditions)"},
            {"id": "D", "text": "Signals"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Grant controls determine the requirements that must be met to allow access - such as "
                       "require MFA, require a compliant device, or block access.",
            "distractors": {
                "B": "Session controls limit what happens within an already-granted session (e.g., sign-in frequency), not the grant requirement.",
                "C": "Assignments/conditions define who and what the policy applies to (the 'if'), not the access requirement enforced.",
                "D": "Signals are the inputs evaluated (user, location, device, risk); the enforced requirement is a grant control.",
            },
            "exam_pattern": "Require MFA / compliant device / block = grant controls.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-r2-017", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 3, "type": "mcq",
        "stem": "Which Conditional Access capability limits what a user can do within an already-granted "
                "session - for example, forcing periodic re-authentication through a sign-in frequency setting?",
        "options": [
            {"id": "A", "text": "Session controls"},
            {"id": "B", "text": "Grant controls"},
            {"id": "C", "text": "Access reviews"},
            {"id": "D", "text": "Data connectors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session controls restrict the experience within a granted session - for example sign-in "
                       "frequency or app-enforced restrictions.",
            "distractors": {
                "B": "Grant controls decide whether access is allowed at sign-in; they do not govern the ongoing session.",
                "C": "Access reviews recertify who has access over time; they are not a Conditional Access session control.",
                "D": "Data connectors ingest data into Microsoft Sentinel; they have nothing to do with Conditional Access sessions.",
            },
            "exam_pattern": "Limit behavior within a granted session (sign-in frequency) = session controls.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-r2-018", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to stop all access to its apps from countries where it has no operations. Which "
                "Conditional Access configuration achieves this?",
        "options": [
            {"id": "A", "text": "A policy that uses a location condition with the Block access grant control"},
            {"id": "B", "text": "An access review on the app's users"},
            {"id": "C", "text": "Assigning a managed identity to the app"},
            {"id": "D", "text": "Applying a sensitivity label to the app"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access can use a named-location condition and the Block access control to deny "
                       "sign-ins from specified locations.",
            "distractors": {
                "B": "An access review recertifies existing access; it does not block sign-ins by location in real time.",
                "C": "A managed identity is an app identity for Azure resources; it does not block user access by location.",
                "D": "Sensitivity labels protect content, not block app sign-ins by geography.",
            },
            "exam_pattern": "Block by location = Conditional Access location condition + Block access.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-r2-019", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 3, "type": "mcq",
        "stem": "What is the difference between Microsoft Entra roles and Azure (resource) roles?",
        "options": [
            {"id": "A", "text": "Entra roles control access to Microsoft Entra / identity resources (like users and groups), while Azure roles control access to Azure resources (like VMs and storage)"},
            {"id": "B", "text": "They are identical and interchangeable"},
            {"id": "C", "text": "Entra roles apply only to on-premises servers; Azure roles apply only to printers"},
            {"id": "D", "text": "Azure roles manage identities while Entra roles manage billing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra (directory) roles manage identity resources; Azure RBAC roles manage "
                       "access to Azure resources such as virtual machines, storage, and networks.",
            "distractors": {
                "B": "They are not identical - they govern different resource planes (identity vs Azure resources).",
                "C": "This is incorrect; Entra roles govern directory/identity objects, not on-premises servers specifically.",
                "D": "This reverses the roles; Azure roles govern Azure resources and Entra roles govern identity, not billing.",
            },
            "exam_pattern": "Entra roles = identity/directory objects; Azure roles = Azure resources.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra role-based access control"],
    },
    {
        "id": "sc900-entra-r2-020", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "Assigning the limited Helpdesk Administrator role - rather than Global Administrator - to staff "
                "whose only task is resetting user passwords is an application of which security principle?",
        "options": [
            {"id": "A", "text": "Least privilege"},
            {"id": "B", "text": "Assume breach"},
            {"id": "C", "text": "Defense in depth"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Granting only the permissions needed for the job (and no more) is the principle of least "
                       "privilege, which RBAC supports through narrowly scoped roles.",
            "distractors": {
                "B": "Assume breach is a Zero Trust principle about segmenting on the assumption of compromise, not about scoping a role to a task.",
                "C": "Defense in depth is layering multiple controls, not choosing the least-privileged role.",
                "D": "Single sign-on is an authentication convenience, unrelated to role scope.",
            },
            "exam_pattern": "Grant only the permissions the job needs via a narrow role = least privilege.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra role-based access control"],
    },
    {
        "id": "sc900-entra-r2-021", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 3, "type": "mcq",
        "stem": "When the built-in Microsoft Entra roles do not match the exact set of permissions an "
                "organization needs, what can an administrator create to grant precisely the required "
                "permissions?",
        "options": [
            {"id": "A", "text": "A custom role"},
            {"id": "B", "text": "A security group"},
            {"id": "C", "text": "A managed identity"},
            {"id": "D", "text": "An access package"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A custom role lets administrators define a tailored set of permissions when no built-in "
                       "role fits the need.",
            "distractors": {
                "B": "A security group assigns access to members but does not define a new permission set.",
                "C": "A managed identity is an application identity for Azure resources, not a permission definition.",
                "D": "An access package bundles resources for request/approval in entitlement management; it does not define role permissions.",
            },
            "exam_pattern": "Built-in roles don't fit -> create a custom role with exact permissions.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra role-based access control"],
    },
    {
        "id": "sc900-entra-r2-022", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 3, "type": "mcq",
        "stem": "In a Conditional Access policy, which element specifies the users, target resources, and "
                "conditions (the 'if' part) that determine whether the policy applies to a sign-in?",
        "options": [
            {"id": "A", "text": "Assignments"},
            {"id": "B", "text": "Grant controls"},
            {"id": "C", "text": "Session controls"},
            {"id": "D", "text": "Playbooks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Assignments define the scope and conditions (users/groups, target resources, and "
                       "conditions like location, device, and risk) that determine when a policy applies.",
            "distractors": {
                "B": "Grant controls are the access requirements enforced once a policy applies (the 'then'), not the scope.",
                "C": "Session controls limit the granted session; they are not the policy's who/what/conditions scope.",
                "D": "Playbooks are Microsoft Sentinel automation workflows, not a Conditional Access element.",
            },
            "exam_pattern": "The 'if' (users + resources + conditions) = assignments; the 'then' = access controls.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },

    # ----- sc9_entra_identity_protection ---------------------------------
    {
        "id": "sc900-entra-r2-023", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 3, "type": "mcq",
        "stem": "In Microsoft Entra ID Protection, a risk that represents the probability a specific "
                "authentication request was not authorized by the identity's owner is called:",
        "options": [
            {"id": "A", "text": "Sign-in risk"},
            {"id": "B", "text": "User risk"},
            {"id": "C", "text": "Compliance risk"},
            {"id": "D", "text": "Residual risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sign-in risk estimates the likelihood that a given sign-in attempt is not from the "
                       "legitimate owner of the identity.",
            "distractors": {
                "B": "User risk is the probability that the identity itself is compromised, not the risk of one specific sign-in.",
                "C": "'Compliance risk' is not an ID Protection risk type.",
                "D": "Residual risk is a general risk-management term (risk remaining after controls), not an ID Protection signal.",
            },
            "exam_pattern": "Probability a specific sign-in isn't the real user = sign-in risk.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Protection"],
    },
    {
        "id": "sc900-entra-r2-024", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 3, "type": "mcq",
        "stem": "Microsoft Entra ID Protection finds a user's credentials posted in a known credential leak. "
                "This raises which kind of risk, indicating the identity itself may be compromised?",
        "options": [
            {"id": "A", "text": "User risk"},
            {"id": "B", "text": "Sign-in risk"},
            {"id": "C", "text": "Session risk"},
            {"id": "D", "text": "Posture risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leaked credentials indicate the identity may be compromised, which is user risk (the "
                       "probability an identity, not just one sign-in, is at risk).",
            "distractors": {
                "B": "Sign-in risk concerns a single authentication attempt; leaked credentials raise user risk for the identity overall.",
                "C": "'Session risk' is not an ID Protection risk type.",
                "D": "'Posture risk' relates to resource configuration (Defender for Cloud), not identity compromise.",
            },
            "exam_pattern": "Leaked credentials / compromised identity = user risk.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Protection"],
    },
    {
        "id": "sc900-entra-r2-025", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following is an example of a risk detection used by Microsoft Entra ID "
                "Protection?",
        "options": [
            {"id": "A", "text": "Atypical travel (sign-ins from distant locations in an impossible time frame)"},
            {"id": "B", "text": "A user updating their display name"},
            {"id": "C", "text": "A virtual machine reporting high CPU usage"},
            {"id": "D", "text": "A sensitivity label reaching its expiration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Atypical/impossible travel is a classic ID Protection risk detection, flagging sign-ins "
                       "from geographically distant locations too close together in time.",
            "distractors": {
                "B": "Changing a display name is a routine directory change, not an ID Protection risk detection.",
                "C": "High CPU is a performance metric handled by monitoring tools, not an identity risk signal.",
                "D": "Label expiration is a Microsoft Purview concept, not an ID Protection risk detection.",
            },
            "exam_pattern": "Risk detections: atypical travel, anonymous IP, leaked credentials, unfamiliar sign-in properties, etc.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Protection (risk detections)"],
    },
    {
        "id": "sc900-entra-r2-026", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 3, "type": "mcq",
        "stem": "How does Microsoft Entra ID Protection most commonly enforce automatic responses when it "
                "detects elevated identity risk?",
        "options": [
            {"id": "A", "text": "Through risk-based Conditional Access policies (for example, require MFA or a secure password change, or block access)"},
            {"id": "B", "text": "By encrypting the user's local files"},
            {"id": "C", "text": "By creating a managed identity for the user"},
            {"id": "D", "text": "By issuing the user a verifiable credential"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ID Protection integrates with Conditional Access: risk-based policies can require MFA or "
                       "a password change, or block access, when user or sign-in risk is elevated.",
            "distractors": {
                "B": "ID Protection does not encrypt local files; it responds to identity risk via access policies.",
                "C": "Managed identities are app identities for Azure resources, not a risk remediation action.",
                "D": "Issuing verifiable credentials is Microsoft Entra Verified ID, not an ID Protection remediation.",
            },
            "exam_pattern": "ID Protection remediates via risk-based Conditional Access (require MFA / password change / block).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Protection"],
    },
    {
        "id": "sc900-entra-r2-027", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Entra ID Governance feature automates joiner/mover/leaver tasks - such as "
                "granting access when an employee is hired, updating it when they change roles, and removing it "
                "when they leave?",
        "options": [
            {"id": "A", "text": "Lifecycle workflows"},
            {"id": "B", "text": "Entitlement management"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Privileged Identity Management (PIM)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Lifecycle workflows automate tasks tied to the employee lifecycle (joiner/mover/leaver), "
                       "such as provisioning and deprovisioning access.",
            "distractors": {
                "B": "Entitlement management governs access packages that users request and that expire; it is request-driven rather than lifecycle-event-driven automation.",
                "C": "Conditional Access enforces sign-in conditions; it does not automate the employee lifecycle.",
                "D": "PIM manages just-in-time privileged role activation, not joiner/mover/leaver automation.",
            },
            "exam_pattern": "Automate joiner/mover/leaver access tasks = lifecycle workflows.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Governance (lifecycle workflows)"],
    },
    {
        "id": "sc900-entra-r2-028", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "In Privileged Identity Management (PIM), an administrator is made 'eligible' for a privileged "
                "role rather than permanently assigned to it. What must they do to use the role's permissions?",
        "options": [
            {"id": "A", "text": "Activate the role just-in-time for a limited time, often requiring MFA or approval"},
            {"id": "B", "text": "Nothing - eligible assignment grants the permissions permanently"},
            {"id": "C", "text": "Create a new custom role each time"},
            {"id": "D", "text": "Register a FIDO2 security key for the tenant"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An eligible assignment requires the user to activate the role when needed (just-in-time), "
                       "typically with MFA and/or approval and for a limited duration.",
            "distractors": {
                "B": "Eligible assignment is not standing access; the user must activate the role to use it.",
                "C": "PIM activation uses the existing role; it does not require creating a new custom role each time.",
                "D": "Registering a security key is an authentication-method task, not how a PIM-eligible role is used.",
            },
            "exam_pattern": "PIM eligible -> activate just-in-time (time-bound, MFA/approval) to use the role.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Privileged Identity Management"],
    },
    {
        "id": "sc900-entra-r2-029", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "multi",
        "stem": "Access reviews in Microsoft Entra ID Governance can be used to periodically recertify which "
                "TWO of the following? (Choose two.)",
        "options": [
            {"id": "A", "text": "Membership in groups"},
            {"id": "B", "text": "Assignment of privileged roles"},
            {"id": "C", "text": "The CPU usage of a virtual machine"},
            {"id": "D", "text": "The encryption algorithm used by TLS"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Access reviews recertify whether users still need access - including group memberships, "
                       "application access, and privileged role assignments.",
            "distractors": {
                "C": "VM CPU usage is a performance metric, not an access assignment to recertify.",
                "D": "A TLS encryption algorithm is a cryptographic setting, not something access reviews recertify.",
            },
            "exam_pattern": "Access reviews recertify group membership, app access, and role assignments.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Governance (access reviews)"],
    },
    {
        "id": "sc900-entra-r2-030", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 3, "type": "mcq",
        "stem": "In Microsoft Entra Verified ID, an organization that issues a verifiable credential - for "
                "example, a university issuing a digital diploma to a graduate - plays which role?",
        "options": [
            {"id": "A", "text": "Issuer"},
            {"id": "B", "text": "Verifier"},
            {"id": "C", "text": "Holder"},
            {"id": "D", "text": "Identity provider"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In the verifiable-credential model, the issuer creates and issues the credential (e.g., "
                       "the university); the holder stores it and the verifier checks it.",
            "distractors": {
                "B": "The verifier is the party that later requests and validates the credential (e.g., an employer), not the one issuing it.",
                "C": "The holder is the user who receives and holds the credential in their wallet, not the issuing organization.",
                "D": "'Identity provider' is a general authentication term; the specific Verified ID role here is issuer.",
            },
            "exam_pattern": "Verified ID roles: issuer (issues), holder (stores), verifier (validates).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra Verified ID"],
    },

    # =====================================================================
    # Domain 3 - Capabilities of Microsoft Security Solutions (40 items)
    # =====================================================================

    # ----- sc9_azure_security --------------------------------------------
    {
        "id": "sc900-sec-r2-001", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about network segmentation using Azure virtual networks is correct?",
        "options": [
            {"id": "A", "text": "By default there are no access controls between subnets in a virtual network, so network security groups are used to segment and restrict traffic"},
            {"id": "B", "text": "Subnets are completely isolated from each other by default and cannot communicate at all"},
            {"id": "C", "text": "Traffic between subnets is always encrypted automatically and cannot be filtered"},
            {"id": "D", "text": "Segmentation can only be achieved with Azure Bastion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Within a virtual network, subnets can communicate by default; network security groups "
                       "(NSGs) are applied to segment and restrict that traffic.",
            "distractors": {
                "B": "Subnets in the same VNet can communicate by default; they are not fully isolated without added controls.",
                "C": "Inter-subnet traffic is not automatically encrypted, and it can be filtered with NSGs.",
                "D": "Azure Bastion provides secure VM access, not subnet segmentation; NSGs segment traffic.",
            },
            "exam_pattern": "No controls between subnets by default -> use NSGs to segment.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure network security (segmentation)"],
    },
    {
        "id": "sc900-sec-r2-002", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 3, "type": "mcq",
        "stem": "Which Azure capability lets you group virtual machines by workload or role and then write "
                "network security rules against those groups instead of individual IP addresses?",
        "options": [
            {"id": "A", "text": "Application security groups (ASGs)"},
            {"id": "B", "text": "Availability sets"},
            {"id": "C", "text": "Management groups"},
            {"id": "D", "text": "Resource groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Application security groups let you group VMs by application/role so NSG rules can "
                       "reference the group rather than specific IP addresses.",
            "distractors": {
                "B": "Availability sets improve VM resiliency across hardware; they are not a network-rule grouping.",
                "C": "Management groups organize subscriptions for governance, not VMs for NSG rules.",
                "D": "Resource groups are a management/organization container, not a network-security grouping for rules.",
            },
            "exam_pattern": "Group VMs by role for NSG rules (not by IP) = application security groups.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure network security"],
    },
    {
        "id": "sc900-sec-r2-003", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Azure Firewall is described as a 'stateful' firewall. What does stateful mean in this context?",
        "options": [
            {"id": "A", "text": "It tracks the state of active connections and makes filtering decisions using that connection context, not just isolated packets"},
            {"id": "B", "text": "It stores all application secrets and certificates"},
            {"id": "C", "text": "It keeps virtual machines powered on at all times"},
            {"id": "D", "text": "It only inspects the first packet and ignores the rest of a flow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A stateful firewall tracks the state of connections (e.g., established sessions) and uses "
                       "that context to allow related return traffic and make smarter filtering decisions.",
            "distractors": {
                "B": "Storing secrets and certificates is Azure Key Vault's role, not what 'stateful' means.",
                "C": "Keeping VMs powered on is unrelated to firewall statefulness.",
                "D": "Stateful means it tracks the whole connection, not just the first packet.",
            },
            "exam_pattern": "Stateful = tracks connection state/context across a flow.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Firewall"],
    },
    {
        "id": "sc900-sec-r2-004", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Azure DDoS Protection is primarily designed to mitigate which category of attack?",
        "options": [
            {"id": "A", "text": "Network-layer volumetric and protocol flooding attacks that exhaust resources"},
            {"id": "B", "text": "SQL injection attempts against a web application's database"},
            {"id": "C", "text": "Phishing emails sent to employees"},
            {"id": "D", "text": "Malware running on a laptop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure DDoS Protection defends against distributed denial-of-service attacks - large-scale "
                       "volumetric and protocol floods aimed at exhausting resources and causing outages.",
            "distractors": {
                "B": "SQL injection is an application-layer exploit handled by a Web Application Firewall, not DDoS Protection.",
                "C": "Phishing emails are addressed by Defender for Office 365, not DDoS Protection.",
                "D": "Endpoint malware is handled by Defender for Endpoint, not DDoS Protection.",
            },
            "exam_pattern": "Volumetric/protocol flooding to exhaust resources = DDoS Protection (vs WAF for app exploits).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure DDoS Protection"],
    },
    {
        "id": "sc900-sec-r2-005", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 3, "type": "mcq",
        "stem": "Azure DDoS Protection and a Web Application Firewall (WAF) protect against different threats. "
                "Which pairing correctly matches each service to the threat it addresses?",
        "options": [
            {"id": "A", "text": "DDoS Protection -> volumetric traffic floods; WAF -> application-layer exploits such as SQL injection and XSS"},
            {"id": "B", "text": "DDoS Protection -> SQL injection; WAF -> traffic floods"},
            {"id": "C", "text": "Both services only store encryption keys"},
            {"id": "D", "text": "Both services only provide RDP/SSH access to VMs"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DDoS Protection mitigates volumetric/network floods, while a WAF inspects HTTP traffic to "
                       "block application-layer exploits like SQL injection and cross-site scripting.",
            "distractors": {
                "B": "This reverses the roles; DDoS handles floods and WAF handles SQL injection/XSS.",
                "C": "Neither service stores encryption keys; that is Azure Key Vault.",
                "D": "Neither service provides VM remote access; that is Azure Bastion.",
            },
            "exam_pattern": "DDoS = floods (L3/L4); WAF = web exploits (L7, SQLi/XSS).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure DDoS Protection and Web Application Firewall"],
    },
    {
        "id": "sc900-sec-r2-006", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 3, "type": "mcq",
        "stem": "How can an Azure application retrieve a secret from Azure Key Vault without storing any "
                "credentials in its code or configuration?",
        "options": [
            {"id": "A", "text": "By using a managed identity to authenticate to Key Vault"},
            {"id": "B", "text": "By hardcoding the vault's access key in the app"},
            {"id": "C", "text": "By disabling all access policies on the vault"},
            {"id": "D", "text": "By connecting through Azure Bastion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A managed identity lets the app authenticate to Key Vault automatically, with no secret "
                       "stored in code - Azure manages the credential.",
            "distractors": {
                "B": "Hardcoding a key is exactly the credential-in-code problem managed identities remove, and it is insecure.",
                "C": "Disabling access policies would remove authorization, not provide secure credential-free access.",
                "D": "Azure Bastion provides VM remote access; it does not authenticate apps to Key Vault.",
            },
            "exam_pattern": "App reads Key Vault secret with no stored credential = use a managed identity.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Key Vault"],
    },
    {
        "id": "sc900-sec-r2-007", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "Azure Storage automatically encrypts data when it is written to the service, transparently and "
                "by default. This protects the stored data in which state?",
        "options": [
            {"id": "A", "text": "Data at rest"},
            {"id": "B", "text": "Data in transit only"},
            {"id": "C", "text": "Data in use only"},
            {"id": "D", "text": "It is not encrypted by default"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Storage Service Encryption encrypts data at rest automatically, protecting stored data if "
                       "the underlying media is compromised.",
            "distractors": {
                "B": "Encryption on write protects data at rest; in-transit protection is a separate (TLS) concern.",
                "C": "Data in use is data being processed in memory, not data written to storage.",
                "D": "Azure Storage does encrypt data at rest by default, so this is incorrect.",
            },
            "exam_pattern": "Automatic encryption of stored data = data at rest.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure encryption capabilities"],
    },
    {
        "id": "sc900-sec-r2-008", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs to securely connect to a virtual machine over SSH to manage it, without "
                "giving the VM a public IP address or opening inbound SSH to the internet. Which Azure service "
                "fits this need?",
        "options": [
            {"id": "A", "text": "Azure Bastion"},
            {"id": "B", "text": "Azure Firewall"},
            {"id": "C", "text": "A Web Application Firewall"},
            {"id": "D", "text": "Azure DDoS Protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Bastion brokers RDP/SSH to VMs through the portal over TLS, so the VM needs no "
                       "public IP and no exposed RDP/SSH ports.",
            "distractors": {
                "B": "Azure Firewall centrally filters network traffic; it is not the secure VM remote-access broker.",
                "C": "A WAF protects web applications from exploits; it does not provide SSH access.",
                "D": "DDoS Protection mitigates traffic floods; it does not provide secure VM administration.",
            },
            "exam_pattern": "Secure RDP/SSH without public IP or open ports = Azure Bastion.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Bastion"],
    },
    {
        "id": "sc900-sec-r2-009", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 2, "type": "multi",
        "stem": "Which TWO Azure services help protect the availability and security of a public-facing web "
                "application? (Choose two.)",
        "options": [
            {"id": "A", "text": "Azure DDoS Protection"},
            {"id": "B", "text": "A Web Application Firewall (WAF)"},
            {"id": "C", "text": "Azure Key Vault"},
            {"id": "D", "text": "Azure Bastion"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "DDoS Protection keeps the app available under traffic floods, and a WAF blocks "
                       "application-layer web exploits - together protecting a public web app.",
            "distractors": {
                "C": "Azure Key Vault secures secrets and keys; it does not directly protect a web app from floods or web exploits.",
                "D": "Azure Bastion provides secure VM administration, not protection of a public web application.",
            },
            "exam_pattern": "Public web app protection = DDoS Protection (availability) + WAF (web exploits).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure DDoS Protection and Web Application Firewall"],
    },
    {
        "id": "sc900-sec-r2-010", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_azure_security", "difficulty": 1, "type": "fill",
        "stem": "The Azure service that provides secure RDP and SSH connectivity to virtual machines through the "
                "Azure portal - without exposing their public IP addresses - is called Azure ___. Enter the "
                "missing one-word service name.",
        "correct": ["bastion"],
        "explanation": {
            "correct": "Azure Bastion delivers browser-based, TLS-secured RDP/SSH to VMs without public IP "
                       "exposure or open management ports.",
            "distractors": {},
            "exam_pattern": "Portal-based secure RDP/SSH, no public IP = Azure Bastion.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Azure Bastion"],
    },

    # ----- sc9_defender_for_cloud ----------------------------------------
    {
        "id": "sc900-sec-r2-011", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Defender for Cloud is a cloud-native application protection platform. Which TWO core "
                "capabilities does it provide? (Choose two.)",
        "options": [
            {"id": "A", "text": "Cloud security posture management (CSPM)"},
            {"id": "B", "text": "Cloud workload protection (CWPP)"},
            {"id": "C", "text": "Email anti-phishing filtering for mailboxes"},
            {"id": "D", "text": "Self-service password reset for users"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Defender for Cloud combines cloud security posture management (assess/harden) with cloud "
                       "workload protection (threat protection for resources).",
            "distractors": {
                "C": "Email anti-phishing is Microsoft Defender for Office 365, not Defender for Cloud.",
                "D": "Self-service password reset is a Microsoft Entra feature, not a Defender for Cloud capability.",
            },
            "exam_pattern": "Defender for Cloud = CSPM + CWPP.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud"],
    },
    {
        "id": "sc900-sec-r2-012", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "Besides Azure, Microsoft Defender for Cloud can assess and protect resources in which other "
                "environments after you connect their accounts or projects?",
        "options": [
            {"id": "A", "text": "Amazon Web Services (AWS) and Google Cloud, as well as on-premises"},
            {"id": "B", "text": "Only Azure resources"},
            {"id": "C", "text": "Only Microsoft 365 mailboxes"},
            {"id": "D", "text": "Only on-premises Windows desktops"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud provides multicloud protection, connecting AWS accounts and Google "
                       "Cloud projects (and on-premises machines) in addition to Azure.",
            "distractors": {
                "B": "Defender for Cloud is multicloud; it is not limited to Azure.",
                "C": "Mailbox protection is Defender for Office 365; Defender for Cloud protects infrastructure/workloads.",
                "D": "It covers more than on-premises desktops, including AWS, GCP, and Azure resources.",
            },
            "exam_pattern": "Defender for Cloud multicloud = Azure + AWS + GCP + on-premises.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (multicloud)"],
    },
    {
        "id": "sc900-sec-r2-013", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, the actionable items that tell you how to harden resources and "
                "that raise your secure score when you remediate them are called:",
        "options": [
            {"id": "A", "text": "Security recommendations"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "Access packages"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security recommendations identify misconfigurations and hardening steps; remediating them "
                       "improves your secure score.",
            "distractors": {
                "B": "Playbooks are Microsoft Sentinel automation workflows, not Defender for Cloud recommendations.",
                "C": "Sensitivity labels are a Microsoft Purview data-protection feature, not Defender for Cloud items.",
                "D": "Access packages belong to Entra entitlement management, not Defender for Cloud.",
            },
            "exam_pattern": "Hardening items that raise secure score = security recommendations.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (secure score)"],
    },
    {
        "id": "sc900-sec-r2-014", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Defender for Cloud capability reduces exposure to brute-force attacks by "
                "keeping virtual-machine management ports (such as RDP and SSH) closed and opening them only for "
                "approved, time-limited requests?",
        "options": [
            {"id": "A", "text": "Just-in-time (JIT) VM access"},
            {"id": "B", "text": "Azure Bastion"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Privileged Identity Management (PIM)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Just-in-time VM access (a Defender for Cloud feature) keeps management ports closed and "
                       "opens them only for approved requests for a limited time, shrinking the attack window.",
            "distractors": {
                "B": "Azure Bastion brokers secure RDP/SSH sessions; it does not time-box inbound port exposure the way JIT does.",
                "C": "Conditional Access governs identity sign-in, not VM port exposure.",
                "D": "PIM governs just-in-time privileged role activation for identities, not VM management ports.",
            },
            "exam_pattern": "Open VM management ports only on-demand, time-limited = just-in-time VM access (Defender for Cloud).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (workload protections)"],
    },
    {
        "id": "sc900-sec-r2-015", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "Microsoft Defender for Cloud's enhanced workload protections are enabled through "
                "resource-specific Defender plans. Which of the following is an example of such a plan?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Servers"},
            {"id": "B", "text": "Microsoft Defender for Office 365"},
            {"id": "C", "text": "Microsoft Sentinel"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud offers workload plans such as Defender for Servers, Storage, SQL, and "
                       "Containers to add advanced threat protection per resource type.",
            "distractors": {
                "B": "Defender for Office 365 is part of Microsoft Defender XDR (email/collaboration), not a Defender for Cloud workload plan.",
                "C": "Microsoft Sentinel is a separate SIEM/SOAR product, not a Defender for Cloud plan.",
                "D": "Conditional Access is an identity access control, not a Defender for Cloud workload plan.",
            },
            "exam_pattern": "Defender for Cloud plans: Servers, Storage, SQL, Containers, etc. (not Office 365).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (workload protections)"],
    },
    {
        "id": "sc900-sec-r2-016", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "What is the primary goal of cloud security posture management (CSPM)?",
        "options": [
            {"id": "A", "text": "To continuously assess cloud resources for misconfigurations and compliance gaps and recommend fixes"},
            {"id": "B", "text": "To automate incident-response playbooks"},
            {"id": "C", "text": "To issue verifiable credentials to users"},
            {"id": "D", "text": "To store and rotate application secrets and keys"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CSPM continuously evaluates resource configurations against best practices and standards, "
                       "surfacing misconfigurations and compliance gaps with recommended remediations.",
            "distractors": {
                "B": "Automating response playbooks is a SOAR function (Microsoft Sentinel), not the definition of CSPM.",
                "C": "Issuing verifiable credentials is Microsoft Entra Verified ID, not CSPM.",
                "D": "Storing and rotating secrets is Azure Key Vault, not CSPM.",
            },
            "exam_pattern": "Assess config for misconfig/compliance + recommend fixes = CSPM.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (CSPM)"],
    },
    {
        "id": "sc900-sec-r2-017", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "By default, which baseline/standard do Azure resources get assessed against in Microsoft "
                "Defender for Cloud's secure score and regulatory compliance views?",
        "options": [
            {"id": "A", "text": "The Microsoft cloud security benchmark (MCSB)"},
            {"id": "B", "text": "The GDPR regulation"},
            {"id": "C", "text": "The ISO 9001 quality standard"},
            {"id": "D", "text": "The CIA triad"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft cloud security benchmark is applied by default in Defender for Cloud; other "
                       "standards (e.g., ISO 27001, PCI DSS) can be added to the regulatory compliance dashboard.",
            "distractors": {
                "B": "GDPR is a privacy regulation that can be added, but it is not the default Azure security baseline in Defender for Cloud.",
                "C": "ISO 9001 is a quality-management standard, not a security benchmark used by Defender for Cloud.",
                "D": "The CIA triad is a set of security goals, not a measurable configuration benchmark.",
            },
            "exam_pattern": "Default Defender for Cloud baseline for Azure = Microsoft cloud security benchmark (MCSB).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud (regulatory compliance)"],
    },
    {
        "id": "sc900-sec-r2-018", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a single solution to see misconfigurations, get prioritized hardening "
                "recommendations with a secure score, and enable threat protection for its Azure, AWS, and "
                "on-premises servers. Which Microsoft solution fits?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Cloud"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "Microsoft Entra ID Protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud provides posture assessment (secure score, recommendations) and "
                       "workload threat protection across Azure, multicloud, and on-premises.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR for enterprise-wide detection and response, not a posture/secure-score tool.",
                "C": "Microsoft Purview is the compliance and data governance suite, not cloud posture management.",
                "D": "Entra ID Protection detects identity risk, not resource misconfigurations and workload threats.",
            },
            "exam_pattern": "Posture + secure score + workload protection across clouds = Microsoft Defender for Cloud.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud"],
    },

    # ----- sc9_sentinel --------------------------------------------------
    {
        "id": "sc900-sec-r2-019", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Sentinel component uses queries and logic to detect threats in the ingested "
                "data and generate alerts (which can become incidents)?",
        "options": [
            {"id": "A", "text": "Analytics rules"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Playbooks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Analytics rules run detection logic against ingested data and raise alerts/incidents when "
                       "suspicious patterns are found.",
            "distractors": {
                "B": "Workbooks visualize data; they do not run detections to generate alerts.",
                "C": "Data connectors ingest data into Sentinel; they are not the detection logic.",
                "D": "Playbooks automate responses after detection; they do not perform the detection.",
            },
            "exam_pattern": "Detection logic that raises alerts in Sentinel = analytics rules.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (analytics)"],
    },
    {
        "id": "sc900-sec-r2-020", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Sentinel, related alerts are grouped into a single case that an analyst "
                "investigates, assigns, and manages through to resolution. What is this case called?",
        "options": [
            {"id": "A", "text": "An incident"},
            {"id": "B", "text": "A workbook"},
            {"id": "C", "text": "A data connector"},
            {"id": "D", "text": "A playbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An incident groups related alerts into one investigable case, which is the primary unit "
                       "analysts triage and manage in Sentinel.",
            "distractors": {
                "B": "A workbook is a visualization dashboard, not a grouped case of alerts.",
                "C": "A data connector ingests data; it is not an investigation case.",
                "D": "A playbook automates response actions; it is not the case itself.",
            },
            "exam_pattern": "Grouped related alerts as an investigable case = incident.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (incidents)"],
    },
    {
        "id": "sc900-sec-r2-021", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Sentinel capability lets analysts proactively search across collected data for "
                "undetected threats using queries, before any alert has fired?",
        "options": [
            {"id": "A", "text": "Hunting (threat hunting)"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Access reviews"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Hunting provides queries and tools for analysts to proactively search for threats that "
                       "have not yet triggered an alert.",
            "distractors": {
                "B": "Playbooks automate responses to detected events; they are not proactive hunting.",
                "C": "Data connectors ingest data; they do not provide proactive hunting queries.",
                "D": "Access reviews are an Entra ID Governance feature, unrelated to Sentinel hunting.",
            },
            "exam_pattern": "Proactively search data for undetected threats = hunting.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (hunting)"],
    },
    {
        "id": "sc900-sec-r2-022", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Sentinel capability builds behavioral baselines for users and entities and uses "
                "machine learning to flag anomalous activity (such as a user suddenly behaving unusually)?",
        "options": [
            {"id": "A", "text": "User and Entity Behavior Analytics (UEBA)"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Sensitivity labels"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "UEBA profiles normal behavior for users and entities and uses machine learning to detect "
                       "anomalies that may indicate compromise or insider threats.",
            "distractors": {
                "B": "Workbooks visualize data; they do not build behavioral baselines.",
                "C": "Data connectors ingest data; they do not analyze behavior.",
                "D": "Sensitivity labels classify and protect content in Microsoft Purview, unrelated to behavior analytics.",
            },
            "exam_pattern": "Behavioral baselines + ML anomaly detection in Sentinel = UEBA.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (UEBA)"],
    },
    {
        "id": "sc900-sec-r2-023", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Sentinel can ingest threat intelligence to enrich detection and hunting. Which TWO "
                "of the following are examples of threat-intelligence indicators? (Choose two.)",
        "options": [
            {"id": "A", "text": "Known-malicious IP addresses"},
            {"id": "B", "text": "Known-bad file hashes"},
            {"id": "C", "text": "A user's display name"},
            {"id": "D", "text": "A virtual machine's CPU usage"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Threat-intelligence indicators of compromise include malicious IP addresses, domains, "
                       "URLs, and file hashes, which Sentinel uses to match against ingested data.",
            "distractors": {
                "C": "A display name is routine directory data, not a threat-intelligence indicator.",
                "D": "CPU usage is a performance metric, not an indicator of compromise.",
            },
            "exam_pattern": "Threat-intel indicators: malicious IPs/domains/URLs/file hashes.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (threat intelligence)"],
    },
    {
        "id": "sc900-sec-r2-024", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 3, "type": "mcq",
        "stem": "In Microsoft Sentinel, which feature lets you centrally orchestrate automation - for example, "
                "automatically assigning incidents, adding tags, or triggering playbooks based on conditions?",
        "options": [
            {"id": "A", "text": "Automation rules"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Analytics rules"},
            {"id": "D", "text": "Data connectors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation rules centrally manage and orchestrate Sentinel automation, including running "
                       "playbooks and handling incidents based on conditions.",
            "distractors": {
                "B": "Workbooks visualize data; they do not orchestrate automation.",
                "C": "Analytics rules detect threats and raise alerts; the orchestration layer is automation rules.",
                "D": "Data connectors ingest data; they do not orchestrate automated actions.",
            },
            "exam_pattern": "Centrally orchestrate automation/playbooks on conditions = automation rules.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel (SOAR)"],
    },
    {
        "id": "sc900-sec-r2-025", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 3, "type": "mcq",
        "stem": "Microsoft Sentinel stores and queries the security data it ingests using which underlying "
                "Azure service?",
        "options": [
            {"id": "A", "text": "An Azure Monitor Log Analytics workspace"},
            {"id": "B", "text": "Azure Key Vault"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "Microsoft Entra ID"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel is built on an Azure Monitor Log Analytics workspace, which stores ingested logs "
                       "and is queried (with KQL) for detection and hunting.",
            "distractors": {
                "B": "Azure Key Vault stores secrets and keys; it is not where Sentinel stores log data.",
                "C": "Azure Bastion provides secure VM access; it does not store Sentinel's data.",
                "D": "Microsoft Entra ID is the identity service; it is not Sentinel's log data store.",
            },
            "exam_pattern": "Sentinel is built on a Log Analytics workspace (Azure Monitor).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel"],
    },
    {
        "id": "sc900-sec-r2-026", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_sentinel", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Sentinel provides both SIEM and SOAR functions. Which description matches the SOAR "
                "part?",
        "options": [
            {"id": "A", "text": "Orchestrating and automating responses to threats (for example, via playbooks and automation rules)"},
            {"id": "B", "text": "Collecting and correlating security data to detect threats"},
            {"id": "C", "text": "Classifying and labeling sensitive documents"},
            {"id": "D", "text": "Issuing verifiable credentials to users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SOAR (security orchestration, automation, and response) is the automated-response side of "
                       "Sentinel, delivered through playbooks and automation rules.",
            "distractors": {
                "B": "Collecting and correlating data to detect threats describes the SIEM side, not SOAR.",
                "C": "Classifying/labeling documents is Microsoft Purview information protection, not Sentinel SOAR.",
                "D": "Issuing verifiable credentials is Entra Verified ID, not Sentinel SOAR.",
            },
            "exam_pattern": "SIEM = collect/correlate/detect; SOAR = orchestrate/automate response.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Sentinel"],
    },

    # ----- sc9_defender_xdr ----------------------------------------------
    {
        "id": "sc900-sec-r2-027", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "Where are Microsoft Defender XDR incidents, alerts, and the unified investigation experience "
                "primarily accessed?",
        "options": [
            {"id": "A", "text": "The Microsoft Defender portal"},
            {"id": "B", "text": "The Microsoft Entra admin center"},
            {"id": "C", "text": "The Microsoft Purview portal"},
            {"id": "D", "text": "The Azure Key Vault blade"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Defender portal is the unified console for Defender XDR incidents, alerts, "
                       "hunting, and investigation across the Defender workloads.",
            "distractors": {
                "B": "The Entra admin center manages identities, not Defender XDR incidents.",
                "C": "The Microsoft Purview portal is for compliance and data governance, not XDR security operations.",
                "D": "Azure Key Vault stores secrets and keys; it is not the Defender XDR console.",
            },
            "exam_pattern": "Unified Defender XDR console = Microsoft Defender portal.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR"],
    },
    {
        "id": "sc900-sec-r2-028", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "What is the main advantage of Microsoft Defender XDR correlating signals from endpoints, email, "
                "identities, and cloud apps?",
        "options": [
            {"id": "A", "text": "It groups related alerts across these domains into a single incident that tells the end-to-end attack story"},
            {"id": "B", "text": "It encrypts all corporate data automatically"},
            {"id": "C", "text": "It replaces the need for identity and access management"},
            {"id": "D", "text": "It guarantees 100% uptime for all services"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "By correlating cross-domain signals, Defender XDR assembles related alerts into one "
                       "incident, giving analysts the full attack narrative rather than isolated alerts.",
            "distractors": {
                "B": "XDR correlates and responds to threats; it does not automatically encrypt all data.",
                "C": "XDR complements identity and access management; it does not replace it.",
                "D": "Correlation improves detection/response; it does not guarantee uptime.",
            },
            "exam_pattern": "Cross-domain correlation -> single incident with the full attack story.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR"],
    },
    {
        "id": "sc900-sec-r2-029", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which capability measures an organization's security posture across its Microsoft 365 "
                "identities, devices, and apps and recommends actions to improve it - distinct from the secure "
                "score in Microsoft Defender for Cloud (which covers Azure/multicloud resources)?",
        "options": [
            {"id": "A", "text": "Microsoft Secure Score"},
            {"id": "B", "text": "Secure score in Microsoft Defender for Cloud"},
            {"id": "C", "text": "Compliance score in Compliance Manager"},
            {"id": "D", "text": "Sign-in risk in Entra ID Protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Secure Score (in the Defender portal) measures posture across Microsoft 365 "
                       "identities, devices, and apps with improvement actions; Defender for Cloud's secure score "
                       "covers Azure and multicloud resources.",
            "distractors": {
                "B": "Defender for Cloud's secure score measures the posture of Azure/multicloud resources, not the Microsoft 365 posture asked about here.",
                "C": "Compliance score (Compliance Manager, Purview) measures regulatory-compliance progress, not security posture.",
                "D": "Sign-in risk is an identity risk signal, not a posture score with improvement actions.",
            },
            "exam_pattern": "M365 posture across identity/devices/apps = Microsoft Secure Score (vs Defender for Cloud secure score for Azure).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Secure Score"],
    },
    {
        "id": "sc900-sec-r2-030", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Defender for Office 365 features open email attachments in a protected sandbox "
                "and check URLs at the moment a user clicks them, to block malicious content?",
        "options": [
            {"id": "A", "text": "Safe Attachments and Safe Links"},
            {"id": "B", "text": "Conditional Access and MFA"},
            {"id": "C", "text": "Data loss prevention and retention labels"},
            {"id": "D", "text": "Network security groups and a WAF"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Safe Attachments detonates attachments in a sandbox, and Safe Links checks URLs at "
                       "time-of-click - both are Microsoft Defender for Office 365 protections.",
            "distractors": {
                "B": "Conditional Access and MFA are identity access controls, not email attachment/URL protection.",
                "C": "DLP and retention labels are Microsoft Purview capabilities, not email threat detonation.",
                "D": "NSGs and a WAF are network/web protections, not email Safe Attachments/Safe Links.",
            },
            "exam_pattern": "Sandbox attachments + time-of-click URL checks = Safe Attachments and Safe Links (Defender for Office 365).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Office 365"],
    },
    {
        "id": "sc900-sec-r2-031", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which capability within Microsoft Defender for Endpoint continuously discovers and prioritizes "
                "software vulnerabilities and security misconfigurations on managed devices?",
        "options": [
            {"id": "A", "text": "Microsoft Defender Vulnerability Management"},
            {"id": "B", "text": "Safe Links"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "eDiscovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender Vulnerability Management discovers, assesses, and prioritizes device "
                       "vulnerabilities and misconfigurations for remediation.",
            "distractors": {
                "B": "Safe Links protects against malicious URLs in email; it does not manage device vulnerabilities.",
                "C": "Conditional Access governs sign-in; it does not assess software vulnerabilities.",
                "D": "eDiscovery is a Microsoft Purview legal-discovery tool, unrelated to device vulnerabilities.",
            },
            "exam_pattern": "Discover/prioritize device vulnerabilities and misconfigurations = Defender Vulnerability Management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc900-sec-r2-032", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 1, "type": "multi",
        "stem": "Microsoft Defender XDR unifies threat protection across which TWO of the following workloads? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Endpoints (devices)"},
            {"id": "B", "text": "Email and collaboration (Office 365)"},
            {"id": "C", "text": "Physical datacenter security"},
            {"id": "D", "text": "Azure resource billing"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Defender XDR spans endpoints, email/collaboration (Office 365), identities, and cloud "
                       "apps - endpoints and email are two of those workloads.",
            "distractors": {
                "C": "Physical datacenter security is the cloud provider's facilities responsibility, not a Defender XDR workload.",
                "D": "Azure resource billing is a cost-management concern, not a Defender XDR threat-protection workload.",
            },
            "exam_pattern": "Defender XDR workloads: Endpoint, Office 365, Identity, Cloud Apps.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR"],
    },
    {
        "id": "sc900-sec-r2-033", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Defender XDR capability automatically examines alerts and can take remediation "
                "steps, mimicking the actions a security analyst would take to investigate and respond?",
        "options": [
            {"id": "A", "text": "Automated investigation and response (AIR)"},
            {"id": "B", "text": "Data connectors"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "Access reviews"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automated investigation and response automatically investigates alerts and can remediate "
                       "threats, reducing analyst workload and response time.",
            "distractors": {
                "B": "Data connectors ingest data into Microsoft Sentinel; they are not an automated investigation feature.",
                "C": "Sensitivity labels classify and protect content in Purview, not investigate alerts.",
                "D": "Access reviews recertify access in Entra, unrelated to automated threat investigation.",
            },
            "exam_pattern": "Auto-investigate alerts and remediate like an analyst = automated investigation and response.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR"],
    },
    {
        "id": "sc900-sec-r2-034", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Defender XDR feature provides Microsoft threat-intelligence reports about "
                "active threats and campaigns, along with your organization's exposure and recommended "
                "mitigations?",
        "options": [
            {"id": "A", "text": "Threat analytics"},
            {"id": "B", "text": "Workbooks"},
            {"id": "C", "text": "Compliance Manager"},
            {"id": "D", "text": "Microsoft Secure Score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat analytics delivers Microsoft security-researcher reports on active threats, your "
                       "exposure, and recommended actions, inside the Defender portal.",
            "distractors": {
                "B": "Workbooks are a Microsoft Sentinel visualization feature, not Defender XDR threat reports.",
                "C": "Compliance Manager manages regulatory compliance in Purview, not threat intelligence.",
                "D": "Microsoft Secure Score measures posture with recommended actions, but the threat-campaign reports are threat analytics.",
            },
            "exam_pattern": "Researcher reports on active threats + your exposure + mitigations = threat analytics.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR (threat analytics)"],
    },
    {
        "id": "sc900-sec-r2-035", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "A user is downloading large volumes of corporate data to an unsanctioned personal cloud-storage "
                "app (shadow IT). Which Microsoft Defender XDR service is designed to discover and control such "
                "SaaS app usage?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Cloud Apps"},
            {"id": "B", "text": "Microsoft Defender for Endpoint"},
            {"id": "C", "text": "Microsoft Defender for Office 365"},
            {"id": "D", "text": "Microsoft Defender for Identity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Cloud Apps is a CASB that discovers and controls SaaS/cloud app "
                       "usage, including unsanctioned shadow IT.",
            "distractors": {
                "B": "Defender for Endpoint protects devices; it is not the CASB for SaaS app discovery.",
                "C": "Defender for Office 365 protects email and collaboration content, not SaaS app usage visibility.",
                "D": "Defender for Identity detects on-premises identity threats, not cloud app usage.",
            },
            "exam_pattern": "Discover/control SaaS usage and shadow IT = Microsoft Defender for Cloud Apps (CASB).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender for Cloud Apps"],
    },
    {
        "id": "sc900-sec-r2-036", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_defender_xdr", "difficulty": 3, "type": "mcq",
        "stem": "How do Microsoft Defender XDR and Microsoft Sentinel commonly work together?",
        "options": [
            {"id": "A", "text": "Defender XDR provides cross-domain detections and incidents that can be ingested into Sentinel (SIEM) for enterprise-wide correlation across all sources"},
            {"id": "B", "text": "They are the same product under two names"},
            {"id": "C", "text": "Sentinel replaces the need for any endpoint protection"},
            {"id": "D", "text": "Defender XDR stores Sentinel's billing information"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender XDR delivers deep cross-domain detection; Sentinel (SIEM/SOAR) can ingest those "
                       "signals and correlate them with data from the wider environment.",
            "distractors": {
                "B": "They are distinct products - Defender XDR (XDR) and Sentinel (SIEM/SOAR) - that integrate.",
                "C": "Sentinel is a SIEM; it does not replace endpoint protection (that is Defender for Endpoint).",
                "D": "Defender XDR does not store Sentinel's billing; they integrate at the security-data level.",
            },
            "exam_pattern": "Defender XDR signals feed Sentinel (SIEM) for enterprise-wide correlation.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Defender XDR and Microsoft Sentinel"],
    },

    # ----- sc9_security_baselines ----------------------------------------
    {
        "id": "sc900-sec-r2-037", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 2, "type": "mcq",
        "stem": "The Microsoft cloud security benchmark (MCSB) provides best-practice recommendations across "
                "control domains. Where are Azure resources automatically assessed against the MCSB?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Cloud"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "The Microsoft Purview portal"},
            {"id": "D", "text": "The Microsoft Entra admin center"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud assesses Azure resources against the Microsoft cloud security "
                       "benchmark by default and reflects the result in secure score and recommendations.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR; it does not assess Azure resources against the MCSB.",
                "C": "The Microsoft Purview portal manages compliance and data governance, not Azure benchmark assessment.",
                "D": "The Entra admin center manages identities, not resource benchmark compliance.",
            },
            "exam_pattern": "MCSB assessment of Azure resources happens in Microsoft Defender for Cloud.",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines for Azure"],
    },
    {
        "id": "sc900-sec-r2-038", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 2, "type": "mcq",
        "stem": "Why are security baselines valuable to a Zero Trust strategy?",
        "options": [
            {"id": "A", "text": "They enforce consistent, hardened configurations (secure defaults, least privilege) that reduce attack surface across resources"},
            {"id": "B", "text": "They remove the need to authenticate users"},
            {"id": "C", "text": "They guarantee that services never need patching"},
            {"id": "D", "text": "They make all cloud services free of charge"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Baselines apply consistent, hardened settings (secure defaults, least-privilege "
                       "configuration) that shrink the attack surface - reinforcing Zero Trust.",
            "distractors": {
                "B": "Baselines harden configuration; they do not remove the need to authenticate users (Zero Trust still verifies explicitly).",
                "C": "Baselines do not eliminate patching; keeping systems updated remains necessary.",
                "D": "Baselines concern security configuration, not pricing; they do not make services free.",
            },
            "exam_pattern": "Baselines = consistent hardening/secure defaults that reduce attack surface (supports Zero Trust).",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines"],
    },
    {
        "id": "sc900-sec-r2-039", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 1, "type": "fill",
        "stem": "A standardized group of recommended security configuration settings that resources should "
                "conform to in order to maintain a consistent, hardened posture is called a security ___. Enter "
                "the missing one-word term.",
        "correct": ["baseline"],
        "explanation": {
            "correct": "A security baseline is a standardized set of recommended configuration settings that "
                       "resources should meet for consistent hardening.",
            "distractors": {},
            "exam_pattern": "Standardized recommended hardening settings to conform to = a security baseline.",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines"],
    },
    {
        "id": "sc900-sec-r2-040", "exam": "sc900", "domain": "sc9_security",
        "subtopic": "sc9_security_baselines", "difficulty": 3, "type": "mcq",
        "stem": "How does a security baseline differ from meeting a regulatory standard such as GDPR?",
        "options": [
            {"id": "A", "text": "A baseline is a recommended technical hardening configuration, while regulatory compliance is about meeting legal obligations (often tracked in Compliance Manager)"},
            {"id": "B", "text": "They are the same thing with different names"},
            {"id": "C", "text": "A baseline is a law, while GDPR is only a technical setting"},
            {"id": "D", "text": "Both are identity authentication methods"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A security baseline is a technical configuration standard for hardening; regulatory "
                       "compliance is meeting legal/regulatory obligations, managed with tools like Compliance Manager.",
            "distractors": {
                "B": "They are different: one is a technical hardening standard, the other a legal obligation.",
                "C": "This reverses them - a baseline is a configuration standard and GDPR is a law, not the other way around.",
                "D": "Neither a baseline nor GDPR is an authentication method.",
            },
            "exam_pattern": "Baseline = technical hardening config; regulatory compliance = legal obligation (Compliance Manager).",
        },
        "references": ["Microsoft Learn (SC-900): Describe security baselines"],
    },

    # =====================================================================
    # Domain 4 - Capabilities of Microsoft Compliance Solutions (24 items)
    # =====================================================================

    # ----- sc9_purview_governance ----------------------------------------
    {
        "id": "sc900-comp-r2-001", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Purview classification method matches content against a specific uploaded table "
                "of known values (for example, your organization's actual customer or employee IDs) to minimize "
                "false positives?",
        "options": [
            {"id": "A", "text": "Exact Data Match (EDM)"},
            {"id": "B", "text": "A trainable classifier"},
            {"id": "C", "text": "A sensitivity label"},
            {"id": "D", "text": "A retention label"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Exact Data Match classifies content by matching it against a customer-supplied table of "
                       "exact known values, which greatly reduces false positives for well-defined records.",
            "distractors": {
                "B": "Trainable classifiers use machine learning for content with varied structure, not exact matching against a known table.",
                "C": "Sensitivity labels apply classification and protection; they are not a matching method against a value table.",
                "D": "Retention labels control how long content is kept; they do not detect sensitive data.",
            },
            "exam_pattern": "Match against a table of exact known values (low false positives) = Exact Data Match.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-002", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Purview classifier type detects complex, context-dependent entities such as a "
                "full person's name or a physical address, rather than a fixed pattern like a 16-digit card "
                "number?",
        "options": [
            {"id": "A", "text": "Named entity sensitive information types"},
            {"id": "B", "text": "Exact Data Match"},
            {"id": "C", "text": "Retention labels"},
            {"id": "D", "text": "Data loss prevention policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Named entity SITs detect complex entities (e.g., full names, physical addresses) using "
                       "context, beyond simple fixed-pattern matching.",
            "distractors": {
                "B": "Exact Data Match compares against a known value table; it is not the named-entity classifier.",
                "C": "Retention labels govern retention periods, not entity detection.",
                "D": "DLP policies act on classified data to prevent leakage; they are not themselves the named-entity classifier.",
            },
            "exam_pattern": "Detect complex entities (names/addresses) by context = named entity SITs.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-003", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "mcq",
        "stem": "An organization needs to detect documents containing 16-digit credit card numbers, which follow "
                "a consistent format. Which classification method is the most direct fit?",
        "options": [
            {"id": "A", "text": "A sensitive information type (pattern/keyword based)"},
            {"id": "B", "text": "A trainable classifier"},
            {"id": "C", "text": "A retention policy"},
            {"id": "D", "text": "A network security group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A sensitive information type uses patterns (and supporting evidence/keywords) to detect "
                       "well-structured data like credit card numbers.",
            "distractors": {
                "B": "Trainable classifiers are best for varied, hard-to-pattern content; a fixed 16-digit pattern is better matched by a sensitive information type.",
                "C": "A retention policy governs how long content is kept, not detection of card numbers.",
                "D": "A network security group filters network traffic; it does not classify document content.",
            },
            "exam_pattern": "Well-structured pattern (card/SSN) = sensitive information type; varied content = trainable classifier.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-004", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 3, "type": "mcq",
        "stem": "Which Microsoft Purview tool shows the actions taken on labeled content over time - such as "
                "label changes, downgrades, and sharing - as opposed to where classified content currently "
                "resides?",
        "options": [
            {"id": "A", "text": "Activity explorer"},
            {"id": "B", "text": "Content explorer"},
            {"id": "C", "text": "Compliance Manager"},
            {"id": "D", "text": "eDiscovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Activity explorer surfaces the activities performed on labeled/classified content over "
                       "time; content explorer shows where that content currently lives.",
            "distractors": {
                "B": "Content explorer shows where classified content resides, not the timeline of actions on it.",
                "C": "Compliance Manager manages regulatory compliance posture, not content activity.",
                "D": "eDiscovery supports legal discovery, not ongoing label-activity monitoring.",
            },
            "exam_pattern": "Actions on labeled content over time = activity explorer; where content is = content explorer.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-005", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Purview data classification supports which TWO outcomes? (Choose two.)",
        "options": [
            {"id": "A", "text": "Discovering where sensitive data resides across the data estate"},
            {"id": "B", "text": "Informing protection actions such as labeling and data loss prevention"},
            {"id": "C", "text": "Filtering network traffic by port and protocol"},
            {"id": "D", "text": "Granting just-in-time administrator roles"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Classification helps find sensitive data and drives downstream protection (sensitivity "
                       "labeling, DLP), so data is handled appropriately.",
            "distractors": {
                "C": "Filtering network traffic is a network-security function (NSG/firewall), not data classification.",
                "D": "Just-in-time admin roles are Privileged Identity Management, not data classification.",
            },
            "exam_pattern": "Classification = discover sensitive data + inform labeling/DLP protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },

    # ----- sc9_purview_protection ----------------------------------------
    {
        "id": "sc900-comp-r2-006", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants to prevent users from copying sensitive files to USB drives or uploading "
                "them to personal cloud storage from their Windows laptops. Which Microsoft Purview capability "
                "extends data loss prevention to these device activities?",
        "options": [
            {"id": "A", "text": "Endpoint data loss prevention (Endpoint DLP)"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Records management"},
            {"id": "D", "text": "Communication compliance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Endpoint DLP extends data loss prevention to device activities such as copying to USB, "
                       "printing, or uploading to unapproved cloud services on managed endpoints.",
            "distractors": {
                "B": "Sensitivity labels classify and protect content, but monitoring/blocking device actions is Endpoint DLP.",
                "C": "Records management governs record retention and disposition, not device-level DLP.",
                "D": "Communication compliance monitors messages for policy violations, not device file transfers.",
            },
            "exam_pattern": "Control sensitive-file actions on devices (USB/print/upload) = Endpoint DLP.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (DLP)"],
    },
    {
        "id": "sc900-comp-r2-007", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "Across which of the following can Microsoft Purview data loss prevention (DLP) policies protect "
                "sensitive content?",
        "options": [
            {"id": "A", "text": "Exchange email, SharePoint, OneDrive, Teams, and endpoints"},
            {"id": "B", "text": "Only on-premises file servers"},
            {"id": "C", "text": "Only Azure virtual machines"},
            {"id": "D", "text": "Only the Microsoft Entra directory"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DLP policies can apply across Microsoft 365 locations - Exchange email, SharePoint, "
                       "OneDrive, Teams - and to devices through Endpoint DLP.",
            "distractors": {
                "B": "DLP is not limited to on-premises file servers; it covers M365 services and endpoints.",
                "C": "DLP protects content in M365 and on endpoints, not just Azure VMs.",
                "D": "The Entra directory holds identities; DLP protects content across M365 workloads and endpoints.",
            },
            "exam_pattern": "DLP scope: Exchange, SharePoint, OneDrive, Teams, and endpoints.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (DLP)"],
    },
    {
        "id": "sc900-comp-r2-008", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "Besides users applying them manually, how else can sensitivity labels be applied to content "
                "that matches specified conditions (such as containing sensitive information types)?",
        "options": [
            {"id": "A", "text": "Automatically, through auto-labeling policies"},
            {"id": "B", "text": "Only by the Global Administrator, one file at a time"},
            {"id": "C", "text": "Only through a Conditional Access policy"},
            {"id": "D", "text": "Only by exporting the file through eDiscovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity labels can be applied automatically via auto-labeling (based on sensitive "
                       "info types/conditions), in addition to manual and default labeling.",
            "distractors": {
                "B": "Labeling is not restricted to the Global Administrator applying files one at a time; auto-labeling scales it.",
                "C": "Conditional Access governs sign-in; it does not apply sensitivity labels to content.",
                "D": "eDiscovery is for legal discovery; it is not how labels are applied.",
            },
            "exam_pattern": "Labels can be applied manually, by default, or automatically (auto-labeling).",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (sensitivity labels)"],
    },
    {
        "id": "sc900-comp-r2-009", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 3, "type": "mcq",
        "stem": "Sensitivity labels can be applied not only to individual files and emails but also to "
                "containers. Which of the following is an example of a container a sensitivity label can "
                "protect?",
        "options": [
            {"id": "A", "text": "A Microsoft Teams team, a Microsoft 365 group, or a SharePoint site"},
            {"id": "B", "text": "A network security group"},
            {"id": "C", "text": "An Azure subscription's billing account"},
            {"id": "D", "text": "A FIDO2 security key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity labels can be applied to containers such as Teams, Microsoft 365 groups, and "
                       "SharePoint sites to govern privacy and access at the container level.",
            "distractors": {
                "B": "A network security group is a traffic filter, not a content container a label protects.",
                "C": "A billing account is a cost-management construct, not a labelable content container.",
                "D": "A FIDO2 key is an authentication device, not a content container.",
            },
            "exam_pattern": "Label containers: Teams, Microsoft 365 groups, SharePoint sites.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (sensitivity labels)"],
    },
    {
        "id": "sc900-comp-r2-010", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "multi",
        "stem": "A Microsoft Purview retention policy can do which TWO of the following to content? (Choose "
                "two.)",
        "options": [
            {"id": "A", "text": "Retain content for a specified period so it cannot be permanently deleted"},
            {"id": "B", "text": "Delete content after a specified period"},
            {"id": "C", "text": "Encrypt content with a sensitivity label"},
            {"id": "D", "text": "Scan messages for harassing language"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Retention settings can retain content (prevent deletion) for a period and/or delete it "
                       "after a period, to meet record-keeping and minimization requirements.",
            "distractors": {
                "C": "Encrypting content via a label is sensitivity-label protection, not a retention policy function.",
                "D": "Scanning messages for harassment is communication compliance, not retention.",
            },
            "exam_pattern": "Retention policy = retain (prevent deletion) and/or delete after a period.",
        },
        "references": ["Microsoft Learn (SC-900): Describe retention policies and labels in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-011", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 3, "type": "mcq",
        "stem": "Compared with a normal retention label, what does declaring an item as a 'record' in Microsoft "
                "Purview records management typically add?",
        "options": [
            {"id": "A", "text": "Stricter controls such as restricting edits/deletion (immutability) and requiring disposition review at end of life"},
            {"id": "B", "text": "Automatic encryption of the entire network"},
            {"id": "C", "text": "Faster internet connectivity for the file"},
            {"id": "D", "text": "A requirement to store the file only on a USB drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Declaring content a record applies stricter regulatory controls - such as blocking edits "
                       "or deletion and requiring disposition review - beyond standard retention.",
            "distractors": {
                "B": "Records declaration governs the item's lifecycle, not network-wide encryption.",
                "C": "Records management is about retention/immutability, not connectivity speed.",
                "D": "There is no requirement to store records on USB; the point is immutability and controlled disposition.",
            },
            "exam_pattern": "Record = stricter controls (immutability, disposition review) vs ordinary retention.",
        },
        "references": ["Microsoft Learn (SC-900): Describe records management in Microsoft Purview"],
    },

    # ----- sc9_insider_ediscovery ----------------------------------------
    {
        "id": "sc900-comp-r2-012", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Purview Insider Risk Management uses policy templates to detect specific scenarios. "
                "Which of the following is an example of such a scenario?",
        "options": [
            {"id": "A", "text": "Data theft by a departing (leaving) employee"},
            {"id": "B", "text": "A SQL injection attempt against a public website"},
            {"id": "C", "text": "A distributed denial-of-service (DDoS) flood"},
            {"id": "D", "text": "Rotating an application's encryption keys"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Insider Risk Management templates target internal-user risks such as data theft by "
                       "departing employees, data leaks, and security-policy violations.",
            "distractors": {
                "B": "SQL injection against a website is an external application attack handled by a WAF, not insider risk.",
                "C": "A DDoS flood is an availability attack mitigated by DDoS Protection, not an insider-risk scenario.",
                "D": "Rotating encryption keys is a key-management task (Azure Key Vault), not an insider-risk scenario.",
            },
            "exam_pattern": "Insider risk templates: departing-employee data theft, leaks, policy violations.",
        },
        "references": ["Microsoft Learn (SC-900): Describe insider risk management in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-013", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "In eDiscovery, what is the purpose of placing a legal 'hold' on content?",
        "options": [
            {"id": "A", "text": "To preserve relevant content so it cannot be deleted or altered while a case is active"},
            {"id": "B", "text": "To permanently encrypt the content for all users"},
            {"id": "C", "text": "To immediately delete the content to save storage"},
            {"id": "D", "text": "To block the custodian's user account from signing in"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A legal hold preserves content relevant to a case, preventing its deletion or alteration "
                       "while the matter is active.",
            "distractors": {
                "B": "A hold preserves content; it does not encrypt it for all users.",
                "C": "A hold prevents deletion to preserve evidence - the opposite of deleting content.",
                "D": "A hold applies to content preservation, not blocking the custodian's sign-in.",
            },
            "exam_pattern": "Legal hold = preserve relevant content (no deletion/alteration) during a case.",
        },
        "references": ["Microsoft Learn (SC-900): Describe eDiscovery in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-014", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview tool lets an administrator search across Microsoft 365 (mailboxes and "
                "sites) to find content matching keywords and conditions, without the full case-management "
                "features of eDiscovery?",
        "options": [
            {"id": "A", "text": "Content search"},
            {"id": "B", "text": "eDiscovery (Premium)"},
            {"id": "C", "text": "Insider Risk Management"},
            {"id": "D", "text": "Compliance Manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Content search finds content across Microsoft 365 by keyword/condition and can export "
                       "results, without the custodian/hold/review-set case management of eDiscovery.",
            "distractors": {
                "B": "eDiscovery (Premium) adds advanced case management (custodians, legal holds, review sets) beyond simple search.",
                "C": "Insider Risk Management detects risky internal activity; it is not a content-search tool.",
                "D": "Compliance Manager manages regulatory compliance posture, not content search.",
            },
            "exam_pattern": "Search M365 content by keyword, no case management = content search.",
        },
        "references": ["Microsoft Learn (SC-900): Describe eDiscovery in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-015", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 3, "type": "mcq",
        "stem": "Compared with Audit (Standard), what does Audit (Premium) in Microsoft Purview generally add?",
        "options": [
            {"id": "A", "text": "Longer retention of audit logs and access to higher-value ('crucial') events for deeper investigations"},
            {"id": "B", "text": "The ability to block all outbound email"},
            {"id": "C", "text": "Automatic encryption of every mailbox"},
            {"id": "D", "text": "Just-in-time activation of admin roles"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Audit (Premium) extends audit-log retention and provides access to additional "
                       "high-value events, supporting more in-depth forensic investigations than Audit (Standard).",
            "distractors": {
                "B": "Blocking outbound email is a mail-flow/DLP action, not an Audit (Premium) capability.",
                "C": "Audit records activity; it does not encrypt mailboxes.",
                "D": "Just-in-time admin role activation is Privileged Identity Management, not an audit feature.",
            },
            "exam_pattern": "Audit (Premium) adds longer log retention + crucial events vs Audit (Standard).",
        },
        "references": ["Microsoft Learn (SC-900): Describe audit capabilities in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-r2-016", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Purview Communication Compliance can help detect which TWO types of issues in "
                "corporate communications? (Choose two.)",
        "options": [
            {"id": "A", "text": "Harassing or threatening language"},
            {"id": "B", "text": "Sharing of sensitive or confidential information"},
            {"id": "C", "text": "High CPU usage on a server"},
            {"id": "D", "text": "An expired TLS certificate"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Communication Compliance detects policy violations in messages, such as offensive/"
                       "harassing content and inappropriate sharing of sensitive information.",
            "distractors": {
                "C": "High CPU usage is a performance metric, not a communication-policy violation.",
                "D": "An expired TLS certificate is an infrastructure issue, not a message-content violation.",
            },
            "exam_pattern": "Communication Compliance: offensive/harassing language, sensitive-info sharing, regulatory violations.",
        },
        "references": ["Microsoft Learn (SC-900): Describe communication compliance in Microsoft Purview"],
    },

    # ----- sc9_compliance_management -------------------------------------
    {
        "id": "sc900-comp-r2-017", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Purview Compliance Manager, the specific recommended tasks you complete to improve "
                "compliance - such as 'turn on audit logging' - are called:",
        "options": [
            {"id": "A", "text": "Improvement actions"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Analytics rules"},
            {"id": "D", "text": "Access packages"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Improvement actions are the recommended tasks in Compliance Manager; completing them "
                       "raises your compliance score and reduces risk.",
            "distractors": {
                "B": "Sensitivity labels classify and protect content; they are not Compliance Manager's recommended tasks.",
                "C": "Analytics rules are a Microsoft Sentinel detection feature, not Compliance Manager actions.",
                "D": "Access packages belong to Entra entitlement management, not Compliance Manager.",
            },
            "exam_pattern": "Recommended compliance tasks that raise the score = improvement actions.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager"],
    },
    {
        "id": "sc900-comp-r2-018", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 3, "type": "mcq",
        "stem": "Compliance Manager distinguishes actions your organization must perform from actions that "
                "Microsoft performs in its cloud infrastructure. The latter are called:",
        "options": [
            {"id": "A", "text": "Microsoft actions"},
            {"id": "B", "text": "Your improvement actions"},
            {"id": "C", "text": "Custom assessments"},
            {"id": "D", "text": "Playbooks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft actions are the controls Microsoft manages in its cloud; their status also "
                       "counts toward your overall compliance score, alongside your own improvement actions.",
            "distractors": {
                "B": "Your improvement actions are the tasks your organization performs, not the ones Microsoft manages.",
                "C": "A custom assessment is a tailored set of controls, not the Microsoft-managed actions.",
                "D": "Playbooks are Microsoft Sentinel automation, unrelated to Compliance Manager actions.",
            },
            "exam_pattern": "Controls Microsoft manages in its cloud = Microsoft actions (vs your improvement actions).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager"],
    },
    {
        "id": "sc900-comp-r2-019", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 2, "type": "mcq",
        "stem": "What does an 'assessment' in Microsoft Purview Compliance Manager represent?",
        "options": [
            {"id": "A", "text": "A grouping of controls and improvement actions for meeting a specific standard or regulation, built from a template"},
            {"id": "B", "text": "A real-time block of a user's sign-in"},
            {"id": "C", "text": "A visualization dashboard of ingested security logs"},
            {"id": "D", "text": "A container for storing encryption keys"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An assessment groups the controls and improvement actions needed to measure and improve "
                       "compliance with a particular regulation or standard, based on a template.",
            "distractors": {
                "B": "Blocking a sign-in is a Conditional Access action, not a Compliance Manager assessment.",
                "C": "A log visualization dashboard is a Microsoft Sentinel workbook, not an assessment.",
                "D": "A key container is Azure Key Vault, not a compliance assessment.",
            },
            "exam_pattern": "Assessment = controls + improvement actions for a standard/regulation (from a template).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager"],
    },
    {
        "id": "sc900-comp-r2-020", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 3, "type": "mcq",
        "stem": "Where does an organization's initial compliance score in Compliance Manager come from, before "
                "any additional assessments are configured?",
        "options": [
            {"id": "A", "text": "The default Data Protection Baseline assessment provided to all organizations"},
            {"id": "B", "text": "The secure score in Microsoft Defender for Cloud"},
            {"id": "C", "text": "The number of users who have registered for MFA"},
            {"id": "D", "text": "The Microsoft 365 service uptime percentage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Compliance Manager calculates an initial compliance score from the default Data "
                       "Protection Baseline assessment that every tenant receives.",
            "distractors": {
                "B": "Secure score measures security posture for Azure resources in Defender for Cloud, not the Compliance Manager initial score.",
                "C": "MFA registration is an identity metric, not the basis of the initial compliance score.",
                "D": "Service uptime is an availability metric, unrelated to the compliance score.",
            },
            "exam_pattern": "Initial compliance score = default Data Protection Baseline assessment.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager (compliance score)"],
    },
    {
        "id": "sc900-comp-r2-021", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 3, "type": "mcq",
        "stem": "Which statement correctly distinguishes the Service Trust Portal from Compliance Manager?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal provides Microsoft's own audit reports and compliance documentation about its cloud; Compliance Manager helps you manage and score your organization's own compliance posture"},
            {"id": "B", "text": "The Service Trust Portal runs your risk-based Conditional Access policies"},
            {"id": "C", "text": "Compliance Manager hosts Microsoft's SOC and ISO audit reports for download"},
            {"id": "D", "text": "They are two names for the same dashboard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Service Trust Portal publishes Microsoft's audit reports/certifications about its "
                       "cloud, while Compliance Manager helps you track and improve your own compliance.",
            "distractors": {
                "B": "Risk-based Conditional Access is an Entra feature, not a Service Trust Portal function.",
                "C": "Microsoft's audit reports are hosted in the Service Trust Portal, not Compliance Manager.",
                "D": "They are different tools - one provides Microsoft's documentation, the other manages your posture.",
            },
            "exam_pattern": "Service Trust Portal = Microsoft's audit reports/docs; Compliance Manager = manage YOUR posture/score.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Service Trust Portal"],
    },

    # ----- sc9_priva_privacy ---------------------------------------------
    {
        "id": "sc900-comp-r2-022", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 2, "type": "mcq",
        "stem": "How does Microsoft Priva relate to Microsoft Purview's broader compliance solutions?",
        "options": [
            {"id": "A", "text": "Priva focuses specifically on privacy risk management and subject rights requests for personal data, complementing Purview's broader compliance and data-protection tools"},
            {"id": "B", "text": "Priva replaces all of Microsoft Purview"},
            {"id": "C", "text": "Priva is a SIEM/SOAR platform for security operations"},
            {"id": "D", "text": "Priva is an identity provider for customer sign-in"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Priva specializes in privacy - managing privacy risks and handling data-subject "
                       "requests - and works alongside Purview's wider compliance and protection capabilities.",
            "distractors": {
                "B": "Priva complements Purview; it does not replace the whole suite.",
                "C": "A SIEM/SOAR platform is Microsoft Sentinel, not Priva.",
                "D": "An identity provider for customer sign-in is Entra External ID, not Priva.",
            },
            "exam_pattern": "Priva = privacy specialization (privacy risk + subject rights) complementing Purview.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva"],
    },
    {
        "id": "sc900-comp-r2-023", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 3, "type": "mcq",
        "stem": "Microsoft Priva Privacy Risk Management uses policies to detect privacy risks involving "
                "personal data. Which of the following is an example of such a risk it can detect?",
        "options": [
            {"id": "A", "text": "Data overexposure (personal data accessible to too many people) or risky data transfers"},
            {"id": "B", "text": "A brute-force password attack against a server"},
            {"id": "C", "text": "An unpatched vulnerability on a virtual machine"},
            {"id": "D", "text": "A phishing email with a malicious attachment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Priva Privacy Risk Management detects privacy risks such as data overexposure, hoarding, "
                       "and risky transfers of personal data, and offers policies to mitigate them.",
            "distractors": {
                "B": "A brute-force password attack is an identity/security threat (Entra/Defender), not a Priva privacy risk.",
                "C": "An unpatched VM vulnerability is handled by Defender for Cloud, not Priva.",
                "D": "A phishing email is addressed by Defender for Office 365, not Priva privacy risk management.",
            },
            "exam_pattern": "Priva Privacy Risk Management: overexposure, hoarding, and risky transfers of personal data.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva (Privacy Risk Management)"],
    },
    {
        "id": "sc900-comp-r2-024", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A Subject Rights Request in Microsoft Priva helps an organization fulfill a data subject's "
                "request about their personal data. Which request types does it help manage?",
        "options": [
            {"id": "A", "text": "Requests to access (provide a copy of), export, and delete the individual's personal data"},
            {"id": "B", "text": "Requests to reset the user's corporate password"},
            {"id": "C", "text": "Requests to provision a new virtual machine"},
            {"id": "D", "text": "Requests to open a firewall port"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Priva Subject Rights Requests help manage and fulfill data-subject requests to access, "
                       "export, or delete their personal data at scale.",
            "distractors": {
                "B": "Resetting a corporate password is an identity task (SSPR), not a subject rights request.",
                "C": "Provisioning a VM is an infrastructure task, unrelated to subject rights requests.",
                "D": "Opening a firewall port is a network task, not a data-subject request.",
            },
            "exam_pattern": "Subject Rights Requests fulfill individuals' access/export/delete requests for their personal data.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva (Subject Rights Requests)"],
    },
]
