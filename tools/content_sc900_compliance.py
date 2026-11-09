"""Microsoft SC-900 pool - Domain 4: Capabilities of Microsoft Compliance Solutions.

Original, objective-aligned practice items for the five compliance-solutions
subtopics tracked in CertLab:
  * sc9_purview_governance    - Microsoft Purview data classification: sensitive
                                information types, trainable classifiers, and
                                content/activity explorer.
  * sc9_purview_protection    - sensitivity labels, data loss prevention (DLP),
                                retention labels/policies, and records
                                management.
  * sc9_insider_ediscovery    - insider risk management, communication
                                compliance, eDiscovery (Standard/Premium), and
                                audit.
  * sc9_compliance_management - Compliance Manager and compliance score; the
                                Service Trust Portal; the Microsoft Purview suite.
  * sc9_priva_privacy         - Microsoft Priva: Privacy Risk Management and
                                Subject Rights Requests.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the key authored as "A" is not positionally
biased, every wrong option carries a distractor note, and each item cites the
Microsoft Learn (SC-900) area. Current product names are used throughout:
Microsoft Purview (formerly the Microsoft 365 compliance center) and Microsoft
Priva. Fundamentals depth only - which solution fits a need; no numeric limits
or preview trivia, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== sc9_purview_governance ===========================================
    {
        "id": "sc900-comp-001", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to discover and categorize data that contains sensitive content such as "
                "credit card or passport numbers across its Microsoft 365 data. Which Microsoft Purview "
                "capability identifies and categorizes such data?",
        "options": [
            {"id": "A", "text": "Data classification"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Microsoft Sentinel"},
            {"id": "D", "text": "Azure Bastion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Purview data classification discovers and categorizes data, including "
                       "sensitive content, so it can be labeled and protected appropriately.",
            "distractors": {
                "B": "Conditional Access governs identity sign-in decisions, not data discovery and classification.",
                "C": "Microsoft Sentinel is a SIEM/SOAR platform, not a data-classification capability.",
                "D": "Azure Bastion provides secure VM access; it has nothing to do with classifying data.",
            },
            "exam_pattern": "Discover and categorize sensitive data in Microsoft 365 = Purview data classification.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-002", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview feature uses built-in and custom, pattern-based definitions (for "
                "example, for a social security number or a bank account number) to detect specific kinds of "
                "sensitive data?",
        "options": [
            {"id": "A", "text": "Sensitive information types"},
            {"id": "B", "text": "Retention labels"},
            {"id": "C", "text": "Microsoft Sentinel playbooks"},
            {"id": "D", "text": "Access reviews"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitive information types are pattern-based classifiers (built-in or custom) that "
                       "detect specific data such as credit card, passport, or account numbers.",
            "distractors": {
                "B": "Retention labels control how long content is kept, not pattern-based detection of sensitive data.",
                "C": "Sentinel playbooks automate security response; they are not Purview data classifiers.",
                "D": "Access reviews recertify user access in Entra; they do not detect sensitive data patterns.",
            },
            "exam_pattern": "Pattern-based detection of specific sensitive data = sensitive information types.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-003", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "mcq",
        "stem": "To identify categories of content that are hard to define with simple patterns (such as "
                "resumes or source code), Microsoft Purview can be trained using example documents. Which "
                "capability is this?",
        "options": [
            {"id": "A", "text": "Trainable classifiers"},
            {"id": "B", "text": "Sensitive information types"},
            {"id": "C", "text": "Data loss prevention (DLP) policies"},
            {"id": "D", "text": "Sensitivity labels"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Trainable classifiers learn from example content to recognize categories that are not "
                       "easily captured by simple patterns, such as resumes or source code.",
            "distractors": {
                "B": "Sensitive information types rely on patterns/keywords, not machine-learning from examples.",
                "C": "DLP policies act on classified data to prevent leakage; they are not the classification-training method.",
                "D": "Sensitivity labels apply classification and protection; they do not learn categories from examples.",
            },
            "exam_pattern": "Recognize hard-to-pattern content by training on examples = trainable classifiers.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-004", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "mcq",
        "stem": "After data is classified, where in Microsoft Purview can an administrator see what sensitive "
                "content exists and how it is being used or labeled?",
        "options": [
            {"id": "A", "text": "Content explorer and activity explorer"},
            {"id": "B", "text": "Microsoft Sentinel workbooks"},
            {"id": "C", "text": "The Microsoft Entra admin center"},
            {"id": "D", "text": "Azure Key Vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Content explorer shows where classified/sensitive content resides, and activity explorer "
                       "shows actions taken on labeled content over time.",
            "distractors": {
                "B": "Sentinel workbooks visualize security operations data, not Purview data classification results.",
                "C": "The Entra admin center manages identities, not sensitive-content discovery.",
                "D": "Azure Key Vault stores secrets and keys; it does not surface classified content.",
            },
            "exam_pattern": "See where classified content is and how it's used = content explorer and activity explorer.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },
    {
        "id": "sc900-comp-005", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_governance", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Purview data classification can identify sensitive content using which TWO of the "
                "following methods? (Choose two.)",
        "options": [
            {"id": "A", "text": "Built-in and custom sensitive information types (pattern matching)"},
            {"id": "B", "text": "Trainable classifiers (machine learning from example content)"},
            {"id": "C", "text": "Measuring each server's CPU temperature"},
            {"id": "D", "text": "Counting the number of user licenses purchased"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Purview classifies content using sensitive information types (patterns) and trainable "
                       "classifiers (machine learning), among other methods.",
            "distractors": {
                "C": "CPU temperature is a hardware metric with no role in classifying data content.",
                "D": "License counts relate to billing, not to identifying sensitive content.",
            },
            "exam_pattern": "Classification methods: sensitive information types (patterns) + trainable classifiers (ML).",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data classification capabilities of Microsoft Purview"],
    },

    # ===== sc9_purview_protection ===========================================
    {
        "id": "sc900-comp-006", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to classify and protect documents and emails by applying labels such as "
                "'Confidential' that can enforce encryption and add visual markings like headers or watermarks. "
                "Which Microsoft Purview feature provides this?",
        "options": [
            {"id": "A", "text": "Sensitivity labels"},
            {"id": "B", "text": "Retention labels"},
            {"id": "C", "text": "Sensitive information types"},
            {"id": "D", "text": "eDiscovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity labels classify and protect content; they can enforce encryption, add "
                       "markings (headers, footers, watermarks), and restrict access.",
            "distractors": {
                "B": "Retention labels govern how long content is kept and when it is deleted, not encryption/markings.",
                "C": "Sensitive information types detect data; they do not apply protective labels and encryption.",
                "D": "eDiscovery finds and holds content for legal cases; it does not classify and protect with labels.",
            },
            "exam_pattern": "Classify and protect with encryption/markings that travel with the file = sensitivity labels.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (sensitivity labels)"],
    },
    {
        "id": "sc900-comp-007", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to prevent users from accidentally sharing documents that contain credit card "
                "numbers outside the organization through email or Microsoft Teams. Which Microsoft Purview "
                "capability should it use?",
        "options": [
            {"id": "A", "text": "Data loss prevention (DLP)"},
            {"id": "B", "text": "Access reviews"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Trainable classifiers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data loss prevention policies detect sensitive content and prevent or warn against its "
                       "risky sharing across locations such as email and Teams.",
            "distractors": {
                "B": "Access reviews recertify user access in Entra; they do not stop sensitive data from being shared.",
                "C": "Conditional Access controls sign-in to apps; it does not inspect content to block oversharing.",
                "D": "Trainable classifiers help identify content, but blocking risky sharing is done by DLP policies.",
            },
            "exam_pattern": "Prevent accidental sharing/leak of sensitive data = data loss prevention (DLP).",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (DLP)"],
    },
    {
        "id": "sc900-comp-008", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "An organization must keep certain financial records for a set number of years and then delete "
                "them, applying this consistently across content. Which Microsoft Purview capability enforces "
                "how long content is kept and when it is removed?",
        "options": [
            {"id": "A", "text": "Retention labels and retention policies"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "Data loss prevention (DLP) policies"},
            {"id": "D", "text": "Insider risk management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Retention labels and policies govern how long content is retained and when it is deleted, "
                       "helping meet regulatory and business record-keeping requirements.",
            "distractors": {
                "B": "Sensitivity labels classify and protect content; they do not primarily control retention periods.",
                "C": "DLP prevents risky sharing of sensitive data; it does not manage retention and deletion schedules.",
                "D": "Insider risk management detects risky user activity; it is not a retention mechanism.",
            },
            "exam_pattern": "Control how long content is kept and when it's deleted = retention labels/policies.",
        },
        "references": ["Microsoft Learn (SC-900): Describe retention policies and labels in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-009", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview capability lets an organization formally declare items as 'records' to "
                "meet legal and regulatory obligations, including immutability and disposition review at the end "
                "of their lifecycle?",
        "options": [
            {"id": "A", "text": "Records management"},
            {"id": "B", "text": "Communication compliance"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "Secure score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Records management lets organizations declare content as records with controls like "
                       "immutability and disposition review to satisfy regulatory retention obligations.",
            "distractors": {
                "B": "Communication compliance detects policy violations in messages; it is not records declaration.",
                "C": "Sensitivity labels protect and classify content, but formal records declaration is records management.",
                "D": "Secure score measures security posture in Defender for Cloud, not records retention.",
            },
            "exam_pattern": "Declare formal records with immutability/disposition = records management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe records management in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-010", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 3, "type": "mcq",
        "stem": "When a 'Highly Confidential' sensitivity label is applied to a document, the label can "
                "automatically encrypt the file and restrict who can open it, even after the file leaves the "
                "organization. This demonstrates sensitivity labels providing which outcome?",
        "options": [
            {"id": "A", "text": "Protection that travels with the data (persistent encryption and access control)"},
            {"id": "B", "text": "Network traffic filtering between subnets"},
            {"id": "C", "text": "Just-in-time activation of administrator roles"},
            {"id": "D", "text": "Threat detection on device endpoints"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity labels can embed protection (encryption and usage restrictions) that stays "
                       "with the file wherever it goes, so access controls persist outside the organization.",
            "distractors": {
                "B": "Network traffic filtering is a function of NSGs/firewalls, not sensitivity labels.",
                "C": "Just-in-time admin role activation is Privileged Identity Management, not labeling.",
                "D": "Endpoint threat detection is Microsoft Defender for Endpoint, not a sensitivity-label outcome.",
            },
            "exam_pattern": "Encryption/access control that stays with the file = sensitivity-label protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview (sensitivity labels)"],
    },
    {
        "id": "sc900-comp-011", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_purview_protection", "difficulty": 2, "type": "fill",
        "stem": "Microsoft Purview labels that classify and protect content - applying encryption and markings "
                "such as a 'Confidential' header or watermark - are called ___ labels. Enter the missing "
                "one-word term.",
        "correct": ["sensitivity"],
        "explanation": {
            "correct": "Sensitivity labels classify and protect content with encryption, markings, and access "
                       "restrictions; retention labels, by contrast, control how long content is kept.",
            "distractors": {},
            "exam_pattern": "Classify + protect (encrypt/mark) = sensitivity labels; retain/delete = retention labels.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the data protection capabilities of Microsoft Purview"],
    },

    # ===== sc9_insider_ediscovery ===========================================
    {
        "id": "sc900-comp-012", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview solution helps detect, investigate, and act on risky activities by "
                "internal users - such as potential data theft by a departing employee - while using "
                "pseudonymization to help protect user privacy during investigation?",
        "options": [
            {"id": "A", "text": "Insider Risk Management"},
            {"id": "B", "text": "eDiscovery"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Microsoft Defender for Endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Insider Risk Management identifies and helps investigate risky internal activity (like "
                       "data exfiltration by a departing employee) with privacy controls such as pseudonymization.",
            "distractors": {
                "B": "eDiscovery finds and holds content for legal cases; it is not focused on detecting risky insider behavior.",
                "C": "Conditional Access governs sign-in decisions; it does not analyze insider risk activity.",
                "D": "Defender for Endpoint protects devices from threats; it is not the insider-risk solution.",
            },
            "exam_pattern": "Detect/investigate risky internal-user activity (e.g., departing-employee data theft) = Insider Risk Management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe insider risk management in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-013", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants to detect inappropriate or non-compliant messages - such as harassment, "
                "sharing of sensitive information, or regulatory violations - within its corporate "
                "communications like email and Microsoft Teams chats. Which Microsoft Purview solution fits?",
        "options": [
            {"id": "A", "text": "Communication Compliance"},
            {"id": "B", "text": "Insider Risk Management"},
            {"id": "C", "text": "eDiscovery (Premium)"},
            {"id": "D", "text": "Records management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Communication Compliance detects and helps remediate policy violations in corporate "
                       "communications, such as offensive language, sensitive-data sharing, or regulatory breaches.",
            "distractors": {
                "B": "Insider Risk Management focuses on risky user activities and data handling, not scanning message content for policy violations.",
                "C": "eDiscovery (Premium) supports legal investigations and holds, not ongoing communication-policy monitoring.",
                "D": "Records management governs retention of records; it does not monitor messages for violations.",
            },
            "exam_pattern": "Monitor message content for policy violations (harassment, leaks) = Communication Compliance.",
        },
        "references": ["Microsoft Learn (SC-900): Describe communication compliance in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-014", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "A legal team must identify, place holds on, collect, and review electronic content across "
                "Microsoft 365 that is relevant to a lawsuit. Which Microsoft Purview capability supports this?",
        "options": [
            {"id": "A", "text": "eDiscovery"},
            {"id": "B", "text": "Data loss prevention (DLP)"},
            {"id": "C", "text": "Sensitivity labels"},
            {"id": "D", "text": "Compliance Manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "eDiscovery lets organizations identify, hold, collect, and review content for legal and "
                       "investigative purposes.",
            "distractors": {
                "B": "DLP prevents risky sharing of sensitive data; it is not a legal discovery tool.",
                "C": "Sensitivity labels classify and protect content; they do not run legal holds and reviews.",
                "D": "Compliance Manager helps manage compliance posture and improvement actions, not legal discovery.",
            },
            "exam_pattern": "Identify/hold/collect/review content for legal cases = eDiscovery.",
        },
        "references": ["Microsoft Learn (SC-900): Describe eDiscovery in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-015", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 3, "type": "mcq",
        "stem": "A company needs advanced legal workflows for complex litigation - including custodian "
                "management, legal hold notifications, and review sets - beyond basic search and export. Which "
                "option provides these advanced capabilities?",
        "options": [
            {"id": "A", "text": "eDiscovery (Premium)"},
            {"id": "B", "text": "eDiscovery (Standard)"},
            {"id": "C", "text": "Content search only"},
            {"id": "D", "text": "Audit (Standard)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "eDiscovery (Premium) adds advanced capabilities such as custodian management, legal hold "
                       "notifications, and review sets for complex cases, beyond the Standard tier's search/hold/export.",
            "distractors": {
                "B": "eDiscovery (Standard) provides core search, hold, and export, but not the advanced custodian/review-set workflows.",
                "C": "Content search can find content but lacks case management, holds, and review sets.",
                "D": "Audit (Standard) provides activity logging, not legal eDiscovery workflows.",
            },
            "exam_pattern": "Advanced custodian/legal-hold/review-set workflows = eDiscovery (Premium) vs Standard.",
        },
        "references": ["Microsoft Learn (SC-900): Describe eDiscovery in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-016", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview capability records user and administrator activities - such as file "
                "access, sign-ins, and mailbox actions - so investigators can search those logs during an "
                "investigation?",
        "options": [
            {"id": "A", "text": "Audit"},
            {"id": "B", "text": "eDiscovery"},
            {"id": "C", "text": "Data loss prevention (DLP)"},
            {"id": "D", "text": "Trainable classifiers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The audit capability logs user and admin activities across services, and investigators "
                       "can search those audit logs during investigations.",
            "distractors": {
                "B": "eDiscovery collects and reviews content for cases; the activity logging itself is the audit capability.",
                "C": "DLP prevents sensitive-data leakage; it is not an activity-logging and search tool.",
                "D": "Trainable classifiers categorize content; they do not record activity logs.",
            },
            "exam_pattern": "Log and search user/admin activities for investigations = Audit.",
        },
        "references": ["Microsoft Learn (SC-900): Describe audit capabilities in Microsoft Purview"],
    },
    {
        "id": "sc900-comp-017", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_insider_ediscovery", "difficulty": 2, "type": "fill",
        "stem": "The Microsoft Purview process used to identify, place on hold, collect, and review content for "
                "legal cases is known by a term that begins with a lowercase 'e'. Enter that one-word term.",
        "correct": ["ediscovery", "e-discovery"],
        "explanation": {
            "correct": "eDiscovery (electronic discovery) identifies, holds, collects, and reviews electronic "
                       "content for legal and investigative purposes.",
            "distractors": {},
            "exam_pattern": "Find/hold/collect/review electronic content for legal cases = eDiscovery.",
        },
        "references": ["Microsoft Learn (SC-900): Describe eDiscovery in Microsoft Purview"],
    },

    # ===== sc9_compliance_management ========================================
    {
        "id": "sc900-comp-018", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Purview tool helps an organization manage compliance requirements by providing "
                "prebuilt assessments for standards (such as GDPR or ISO 27001), recommended improvement "
                "actions, and an overall score?",
        "options": [
            {"id": "A", "text": "Compliance Manager"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "Secure score in Microsoft Defender for Cloud"},
            {"id": "D", "text": "The Service Trust Portal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Compliance Manager helps manage regulatory compliance with prebuilt assessments, "
                       "improvement actions, and a compliance score that reflects progress.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR platform, not a compliance-management tool.",
                "C": "Secure score measures security posture in Defender for Cloud, not regulatory compliance progress.",
                "D": "The Service Trust Portal hosts Microsoft audit reports and documentation; it does not run your assessments or score.",
            },
            "exam_pattern": "Assessments + improvement actions + compliance score = Compliance Manager.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager"],
    },
    {
        "id": "sc900-comp-019", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Purview Compliance Manager, what does the compliance score represent?",
        "options": [
            {"id": "A", "text": "A measurement of progress in completing recommended actions that reduce compliance risk"},
            {"id": "B", "text": "The percentage of CPU used by compliance tools"},
            {"id": "C", "text": "The number of users who have enabled MFA"},
            {"id": "D", "text": "The guaranteed uptime of Microsoft 365"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The compliance score reflects progress toward completing recommended improvement actions "
                       "that help reduce risk related to data protection and regulatory requirements.",
            "distractors": {
                "B": "The score measures compliance progress, not CPU usage.",
                "C": "MFA adoption is an identity metric, not what the compliance score measures.",
                "D": "Uptime is a service-availability metric, unrelated to the compliance score.",
            },
            "exam_pattern": "Compliance score = progress on improvement actions that reduce compliance risk.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Compliance Manager (compliance score)"],
    },
    {
        "id": "sc900-comp-020", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 2, "type": "mcq",
        "stem": "Where can customers obtain Microsoft's independent audit reports, certifications, and "
                "compliance documentation (such as SOC and ISO reports) for its cloud services?",
        "options": [
            {"id": "A", "text": "The Service Trust Portal"},
            {"id": "B", "text": "The Microsoft Defender portal"},
            {"id": "C", "text": "The Microsoft Entra admin center"},
            {"id": "D", "text": "Azure Key Vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Service Trust Portal publishes Microsoft's audit reports, certifications, and other "
                       "compliance and security documentation for its cloud services.",
            "distractors": {
                "B": "The Microsoft Defender portal is for security operations, not Microsoft's compliance audit reports.",
                "C": "The Entra admin center manages identities, not Microsoft's compliance documentation.",
                "D": "Azure Key Vault stores secrets and keys; it is not a source of audit reports.",
            },
            "exam_pattern": "Microsoft's audit reports/certifications for its cloud = Service Trust Portal.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Service Trust Portal"],
    },
    {
        "id": "sc900-comp-021", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_compliance_management", "difficulty": 1, "type": "mcq",
        "stem": "Microsoft's integrated suite of solutions for data governance, data protection, risk, and "
                "compliance - formerly known as the Microsoft 365 compliance center - is now called what?",
        "options": [
            {"id": "A", "text": "Microsoft Purview"},
            {"id": "B", "text": "Microsoft Priva"},
            {"id": "C", "text": "Microsoft Entra"},
            {"id": "D", "text": "Microsoft Intune"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Purview is the integrated compliance, data protection, and governance suite, "
                       "formerly branded as the Microsoft 365 compliance center.",
            "distractors": {
                "B": "Microsoft Priva focuses specifically on privacy management, not the whole compliance suite.",
                "C": "Microsoft Entra is the identity and access product family, not the compliance suite.",
                "D": "Microsoft Intune manages devices and apps; it is not the compliance suite.",
            },
            "exam_pattern": "Integrated compliance/governance suite, formerly M365 compliance center = Microsoft Purview.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the Microsoft Purview compliance solutions"],
    },

    # ===== sc9_priva_privacy ================================================
    {
        "id": "sc900-comp-022", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft solution helps organizations manage privacy risks - such as data overexposure "
                "and oversharing of personal data - and automate privacy operations, distinct from the broader "
                "compliance tooling?",
        "options": [
            {"id": "A", "text": "Microsoft Priva"},
            {"id": "B", "text": "Microsoft Purview Compliance Manager"},
            {"id": "C", "text": "Microsoft Sentinel"},
            {"id": "D", "text": "Microsoft Defender XDR"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Priva helps organizations identify and manage privacy risks involving personal "
                       "data and automate privacy operations.",
            "distractors": {
                "B": "Compliance Manager measures and manages regulatory compliance posture, not privacy risk operations specifically.",
                "C": "Microsoft Sentinel is a SIEM/SOAR security platform, not a privacy-management solution.",
                "D": "Microsoft Defender XDR is a threat-protection suite, not a privacy solution.",
            },
            "exam_pattern": "Manage personal-data privacy risk and operations = Microsoft Priva.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva"],
    },
    {
        "id": "sc900-comp-023", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Under privacy regulations like GDPR, individuals can ask an organization to provide or delete "
                "the personal data held about them. Which Microsoft Priva capability helps manage and fulfill "
                "these requests at scale?",
        "options": [
            {"id": "A", "text": "Subject Rights Requests"},
            {"id": "B", "text": "Insider Risk Management"},
            {"id": "C", "text": "eDiscovery (Standard)"},
            {"id": "D", "text": "Retention policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Priva Subject Rights Requests helps organizations manage and fulfill individuals' "
                       "requests to access, correct, or delete their personal data.",
            "distractors": {
                "B": "Insider Risk Management detects risky internal activity; it does not fulfill data-subject requests.",
                "C": "eDiscovery supports legal investigations, not privacy subject-rights fulfillment workflows.",
                "D": "Retention policies manage how long data is kept; they do not process subject rights requests.",
            },
            "exam_pattern": "Fulfill individuals' requests to access/delete their personal data = Subject Rights Requests (Priva).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva (Subject Rights Requests)"],
    },
    {
        "id": "sc900-comp-024", "exam": "sc900", "domain": "sc9_compliance",
        "subtopic": "sc9_priva_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Priva capability gives an organization visibility into the personal data it "
                "stores and detects privacy risks such as data transfers and overexposure, with policies to "
                "help mitigate them?",
        "options": [
            {"id": "A", "text": "Privacy Risk Management"},
            {"id": "B", "text": "Communication Compliance"},
            {"id": "C", "text": "Records management"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Priva Privacy Risk Management provides visibility into personal data and detects risks "
                       "(like overexposure and data transfers), offering policies to help mitigate them.",
            "distractors": {
                "B": "Communication Compliance monitors messages for policy violations; it is not a privacy-risk visibility tool.",
                "C": "Records management governs record retention, not personal-data privacy risk.",
                "D": "Conditional Access controls identity sign-in; it does not assess personal-data privacy risk.",
            },
            "exam_pattern": "Visibility into personal data + privacy-risk detection/mitigation = Priva Privacy Risk Management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Priva (Privacy Risk Management)"],
    },
]
