"""Microsoft 365 Fundamentals (MS-900) pool - Domain 3: Security, Compliance, Privacy & Trust.

Original, objective-aligned practice items for the four subtopics tracked in CertLab:
  * ms9_identity_entra      - Microsoft Entra ID (formerly Azure AD) as cloud
                              identity and access management; MFA; single sign-on;
                              Conditional Access.
  * ms9_threat_protection   - Microsoft Defender for Office 365 (Safe Links / Safe
                              Attachments), Microsoft Defender XDR, Microsoft Secure Score.
  * ms9_compliance_purview  - Microsoft Purview: data loss prevention (DLP),
                              sensitivity labels, retention, and eDiscovery.
  * ms9_zero_trust_privacy  - Zero Trust principles, the Service Trust Portal, and
                              privacy management (Microsoft Priva).

Current Microsoft product names are used throughout: Microsoft Entra ID (not Azure
AD), Microsoft Defender XDR (not Microsoft 365 Defender), Microsoft Purview (not the
old Security & Compliance Center). build_content.py shuffles option order by id, so
the authored key is not positionally biased; every wrong option carries a distractor
note. Fundamentals depth only - no memorized exam items.
"""

QUESTIONS = [
    # ===== ms9_identity_entra ===============================================
    {
        "id": "ms900-sec-001", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 1, "type": "mcq",
        "stem": "An organization needs a cloud-based identity and access management service to store user "
                "accounts and let them sign in to Microsoft 365 and thousands of other apps. Which Microsoft "
                "service provides this (it was formerly called Azure Active Directory)?",
        "options": [
            {"id": "A", "text": "Microsoft Intune"},
            {"id": "B", "text": "Microsoft Purview"},
            {"id": "C", "text": "Microsoft Entra ID"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Entra ID (formerly Azure Active Directory) is the cloud identity and access "
                       "management service that authenticates users and controls access to Microsoft 365 and "
                       "other integrated applications.",
            "distractors": {
                "A": "Intune manages devices and apps, not the identity directory.",
                "B": "Purview is the compliance and data-governance suite, not an identity service.",
                "D": "Microsoft Bookings is appointment scheduling, unrelated to identity.",
            },
            "exam_pattern": "Cloud identity/access management (formerly Azure AD) = Microsoft Entra ID.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Entra ID"],
    },
    {
        "id": "ms900-sec-002", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 1, "type": "mcq",
        "stem": "To reduce the risk from stolen passwords, a company requires users to confirm each sign-in with "
                "both their password and an approval in an authenticator app on their phone. Which security "
                "method is this?",
        "options": [
            {"id": "A", "text": "Multifactor authentication (MFA)"},
            {"id": "B", "text": "Single sign-on (SSO)"},
            {"id": "C", "text": "Data loss prevention (DLP)"},
            {"id": "D", "text": "Co-authoring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multifactor authentication (MFA) requires two or more verification factors - such as "
                       "something you know (a password) plus something you have (a phone/authenticator) - so a "
                       "stolen password alone is not enough to sign in.",
            "distractors": {
                "B": "Single sign-on reduces how often users sign in; it does not add a second verification factor.",
                "C": "DLP prevents data oversharing, not sign-in verification.",
                "D": "Co-authoring is real-time document collaboration, unrelated to authentication.",
            },
            "exam_pattern": "Two or more verification factors at sign-in = MFA.",
        },
        "references": ["Microsoft Learn (MS-900): Multifactor authentication"],
    },
    {
        "id": "ms900-sec-003", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "Employees want to sign in once and then reach Microsoft 365 and several other connected "
                "applications without being prompted to enter their credentials again for each one. Which "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "Mobile device management"},
            {"id": "B", "text": "Sensitivity labels"},
            {"id": "C", "text": "A Service Level Agreement"},
            {"id": "D", "text": "Single sign-on (SSO)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Single sign-on (SSO) lets a user authenticate once with Microsoft Entra ID and then "
                       "access multiple connected apps without re-entering credentials for each one.",
            "distractors": {
                "A": "Mobile device management secures devices; it is not about the cross-app sign-in experience.",
                "B": "Sensitivity labels classify and protect content, unrelated to sign-in.",
                "C": "A Service Level Agreement is an uptime commitment, not an authentication feature.",
            },
            "exam_pattern": "Sign in once, reach many apps = single sign-on (SSO).",
        },
        "references": ["Microsoft Learn (MS-900): Single sign-on"],
    },
    {
        "id": "ms900-sec-004", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 2, "type": "mcq",
        "stem": "Security wants to allow or block sign-ins automatically based on signals such as the user, "
                "device compliance, location, and risk - for example, requiring MFA when a sign-in comes from an "
                "unfamiliar location. Which Microsoft Entra feature does this?",
        "options": [
            {"id": "A", "text": "Click-to-Run"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Retention labels"},
            {"id": "D", "text": "Microsoft Graph"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Conditional Access in Microsoft Entra ID evaluates sign-in signals (user, device, "
                       "location, risk) and enforces controls - grant, block, or require MFA - based on policy.",
            "distractors": {
                "A": "Click-to-Run installs Office apps, unrelated to access policy.",
                "C": "Retention labels manage how long content is kept, not sign-in decisions.",
                "D": "Microsoft Graph is a data/API layer, not an access-policy engine.",
            },
            "exam_pattern": "Policy-based sign-in decisions from signals (user/device/location/risk) = Conditional Access.",
        },
        "references": ["Microsoft Learn (MS-900): Conditional Access"],
    },
    {
        "id": "ms900-sec-005", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_identity_entra", "difficulty": 1, "type": "fill",
        "stem": "What is the current name of Microsoft's cloud identity and access management service that was "
                "previously known as Azure Active Directory (Azure AD)? Enter the product name.",
        "correct": ["microsoft entra id", "entra id", "entra"],
        "explanation": {
            "correct": "Azure Active Directory was renamed Microsoft Entra ID; it is Microsoft's cloud identity "
                       "and access management service.",
            "distractors": {},
            "exam_pattern": "Azure AD is now Microsoft Entra ID.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Entra ID"],
    },

    # ===== ms9_threat_protection ============================================
    {
        "id": "ms900-sec-006", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to protect email against malicious attachments and dangerous URLs - scanning "
                "attachments in a sandbox and checking links at the moment a user clicks them. Which service "
                "provides Safe Attachments and Safe Links?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Office 365"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Microsoft Bookings"},
            {"id": "D", "text": "Microsoft Entra ID"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Office 365 protects email and collaboration with features like Safe "
                       "Attachments (detonates attachments in a sandbox) and Safe Links (checks URLs at time of click).",
            "distractors": {
                "B": "Intune manages devices, not email threat protection.",
                "C": "Microsoft Bookings schedules appointments.",
                "D": "Microsoft Entra ID handles identity, not email attachment and link scanning.",
            },
            "exam_pattern": "Safe Links + Safe Attachments for email = Microsoft Defender for Office 365.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Defender for Office 365"],
    },
    {
        "id": "ms900-sec-007", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants one unified portal that correlates threat signals across endpoints, email, "
                "identities, and cloud apps so they can investigate an incident end to end. Which Microsoft "
                "solution provides this extended detection and response?",
        "options": [
            {"id": "A", "text": "Microsoft Forms"},
            {"id": "B", "text": "OneDrive"},
            {"id": "C", "text": "Click-to-Run"},
            {"id": "D", "text": "Microsoft Defender XDR"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Defender XDR (formerly Microsoft 365 Defender) unifies and correlates signals "
                       "across endpoints (Defender for Endpoint), email (Defender for Office 365), identities "
                       "(Defender for Identity), and cloud apps (Defender for Cloud Apps) into end-to-end incidents.",
            "distractors": {
                "A": "Microsoft Forms is for surveys and quizzes.",
                "B": "OneDrive is file storage.",
                "C": "Click-to-Run installs Office apps. None of these correlate cross-domain threat signals.",
            },
            "exam_pattern": "Unified cross-domain detection and response across endpoint, email, identity, apps = Microsoft Defender XDR.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Defender XDR"],
    },
    {
        "id": "ms900-sec-008", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants a single measurement of the organization's security posture, with "
                "prioritized recommended actions and points for improvements, tracked over time. Which Microsoft "
                "tool provides this?",
        "options": [
            {"id": "A", "text": "A sensitivity label"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "The Microsoft 365 roadmap"},
            {"id": "D", "text": "A calling plan"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Secure Score measures an organization's security posture, gives a numeric score, "
                       "and recommends prioritized improvement actions, letting you track progress over time.",
            "distractors": {
                "A": "A sensitivity label classifies and protects content; it is not a posture score.",
                "C": "The Microsoft 365 roadmap lists upcoming features, not security posture.",
                "D": "A calling plan enables PSTN calling, unrelated to security scoring.",
            },
            "exam_pattern": "A measured security-posture score with improvement actions = Microsoft Secure Score.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Secure Score"],
    },
    {
        "id": "ms900-sec-009", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_threat_protection", "difficulty": 2, "type": "fill",
        "stem": "In Microsoft Defender for Office 365, name the feature that opens unknown email attachments in "
                "an isolated sandbox to detect malicious behavior before the message is delivered. Enter the "
                "feature name (two words).",
        "correct": ["safe attachments", "safe attachment"],
        "explanation": {
            "correct": "Safe Attachments detonates unknown attachments in an isolated sandbox to catch malware "
                       "that signature scanning might miss, before the message reaches the user.",
            "distractors": {},
            "exam_pattern": "Sandbox detonation of email attachments = Safe Attachments; click-time URL checks = Safe Links.",
        },
        "references": ["Microsoft Learn (MS-900): Defender for Office 365 Safe Attachments"],
    },

    # ===== ms9_compliance_purview ===========================================
    {
        "id": "ms900-sec-010", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 1, "type": "mcq",
        "stem": "A healthcare company wants to automatically detect and prevent users from emailing or sharing "
                "documents that contain sensitive data such as credit-card or patient-record numbers to outsiders. "
                "Which Microsoft Purview capability does this?",
        "options": [
            {"id": "A", "text": "Single sign-on"},
            {"id": "B", "text": "Click-to-Run"},
            {"id": "C", "text": "Data loss prevention (DLP)"},
            {"id": "D", "text": "Teams channels"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Purview Data Loss Prevention (DLP) detects sensitive information (such as "
                       "credit-card or health identifiers) and enforces policies to block or warn when users try "
                       "to share it inappropriately.",
            "distractors": {
                "A": "Single sign-on is an identity feature, not data protection.",
                "B": "Click-to-Run installs Office apps.",
                "D": "Teams channels organize conversations. None of these detect or prevent sensitive-data sharing.",
            },
            "exam_pattern": "Detect and prevent oversharing of sensitive data = DLP (Microsoft Purview).",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Purview Data Loss Prevention"],
    },
    {
        "id": "ms900-sec-011", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to classify documents and emails as 'Public', 'Confidential', or 'Highly "
                "Confidential' and automatically apply encryption and visual markings based on the classification. "
                "Which Microsoft Purview feature provides this?",
        "options": [
            {"id": "A", "text": "Sensitivity labels"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Microsoft Bookings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sensitivity labels (Microsoft Purview Information Protection) classify content and can "
                       "enforce protection such as encryption, access restrictions, and watermarks or headers "
                       "based on the label.",
            "distractors": {
                "B": "Secure Score measures security posture; it does not classify documents.",
                "C": "Conditional Access controls sign-ins, not content classification.",
                "D": "Microsoft Bookings schedules appointments.",
            },
            "exam_pattern": "Classify and protect content (encryption, markings) = sensitivity labels.",
        },
        "references": ["Microsoft Learn (MS-900): Sensitivity labels"],
    },
    {
        "id": "ms900-sec-012", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "To meet regulations, a firm must keep certain records for a fixed number of years and then "
                "dispose of them, even if users try to delete them earlier. Which Microsoft Purview capability "
                "enforces this?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Retention labels and policies"},
            {"id": "C", "text": "Single sign-on"},
            {"id": "D", "text": "Click-to-Run"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Retention labels and policies (Microsoft Purview Data Lifecycle Management) keep content "
                       "for a required period and can delete it afterward, helping meet regulatory recordkeeping obligations.",
            "distractors": {
                "A": "Safe Links protects against malicious URLs, not record retention.",
                "C": "Single sign-on is an identity feature, unrelated to retention.",
                "D": "Click-to-Run installs Office apps.",
            },
            "exam_pattern": "Keep-then-dispose of content for compliance = retention labels/policies.",
        },
        "references": ["Microsoft Learn (MS-900): Retention in Microsoft Purview"],
    },
    {
        "id": "ms900-sec-013", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_compliance_purview", "difficulty": 2, "type": "mcq",
        "stem": "A legal team needs to identify, place on hold, collect, and export relevant emails and documents "
                "across Microsoft 365 for a lawsuit. Which Microsoft Purview solution is designed for this?",
        "options": [
            {"id": "A", "text": "Multifactor authentication"},
            {"id": "B", "text": "OneDrive sync"},
            {"id": "C", "text": "Teams Phone"},
            {"id": "D", "text": "eDiscovery"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Purview eDiscovery helps legal teams identify, place holds on, collect, review, "
                       "and export content across Microsoft 365 for legal and investigative cases.",
            "distractors": {
                "A": "MFA verifies sign-ins, unrelated to legal discovery.",
                "B": "OneDrive sync keeps files updated across devices, not legal collection.",
                "C": "Teams Phone is telephony, unrelated to eDiscovery.",
            },
            "exam_pattern": "Find / hold / collect / export content for legal cases = eDiscovery (Microsoft Purview).",
        },
        "references": ["Microsoft Learn (MS-900): eDiscovery"],
    },

    # ===== ms9_zero_trust_privacy ===========================================
    {
        "id": "ms900-sec-014", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A company adopts a security strategy summarized as 'verify explicitly, use least-privilege "
                "access, and assume breach,' trusting no request by default even from inside the corporate "
                "network. Which security model is this?",
        "options": [
            {"id": "A", "text": "Zero Trust"},
            {"id": "B", "text": "Perimeter-only (castle-and-moat) security"},
            {"id": "C", "text": "Open access with no controls"},
            {"id": "D", "text": "Perpetual licensing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Zero Trust model treats every access request as untrusted until verified, guided by "
                       "three principles: verify explicitly, use least-privilege access, and assume breach.",
            "distractors": {
                "B": "Castle-and-moat trusts anything already inside the network perimeter - the opposite of Zero Trust.",
                "C": "Open access applies no controls; it is not a security model.",
                "D": "Perpetual licensing is a purchasing model, unrelated to a security strategy.",
            },
            "exam_pattern": "'Never trust, always verify' - verify explicitly / least privilege / assume breach = Zero Trust.",
        },
        "references": ["Microsoft Learn (MS-900): Zero Trust principles"],
    },
    {
        "id": "ms900-sec-015", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A prospective customer's auditors want Microsoft's independent compliance reports and "
                "certifications - such as ISO 27001 and SOC audit reports - for its cloud services. Where can an "
                "organization obtain these documents?",
        "options": [
            {"id": "A", "text": "The Teams admin center"},
            {"id": "B", "text": "The Service Trust Portal"},
            {"id": "C", "text": "OneDrive"},
            {"id": "D", "text": "Microsoft Forms"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Service Trust Portal is Microsoft's hub for audit reports, certifications (ISO, SOC, "
                       "and more), and other compliance and trust documentation for its cloud services.",
            "distractors": {
                "A": "The Teams admin center manages Teams, not compliance reports.",
                "C": "OneDrive stores personal files, not Microsoft's audit documentation.",
                "D": "Microsoft Forms creates surveys and quizzes.",
            },
            "exam_pattern": "Microsoft's audit reports and compliance certifications = Service Trust Portal.",
        },
        "references": ["Microsoft Learn (MS-900): Service Trust Portal"],
    },
    {
        "id": "ms900-sec-016", "exam": "ms900", "domain": "ms9_security_compliance",
        "subtopic": "ms9_zero_trust_privacy", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to proactively manage privacy risks - such as identifying overexposed "
                "personal data - and automate responses to subject rights (data) requests from individuals. Which "
                "Microsoft solution is built for privacy management?",
        "options": [
            {"id": "A", "text": "Microsoft Teams"},
            {"id": "B", "text": "Click-to-Run"},
            {"id": "C", "text": "Microsoft Priva"},
            {"id": "D", "text": "Azure Virtual Desktop"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Priva (part of Microsoft Purview) helps organizations manage privacy risks for "
                       "personal data and automate subject rights (data subject) requests.",
            "distractors": {
                "A": "Teams is collaboration, not privacy management.",
                "B": "Click-to-Run installs Office apps.",
                "D": "Azure Virtual Desktop is desktop virtualization. None of these are privacy-risk solutions.",
            },
            "exam_pattern": "Privacy-risk management and subject rights requests = Microsoft Priva.",
        },
        "references": ["Microsoft Learn (MS-900): Microsoft Priva"],
    },
]
