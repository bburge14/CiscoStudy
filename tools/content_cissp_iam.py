"""(ISC)² CISSP pool - Domain 5: Identity and Access Management (IAM).

Original, CBK-aligned practice items for the four IAM subtopics:
  * cissp_identity_lifecycle     - provisioning/deprovisioning, access reviews
                                   (recertification), and identity proofing.
  * cissp_authentication_methods - factor types, multifactor authentication, and
                                   biometric error rates (FAR/FRR/CER).
  * cissp_access_control_models  - DAC, MAC, RBAC, and ABAC.
  * cissp_federated_identity     - SAML, OAuth 2.0 vs OpenID Connect, Kerberos.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_identity_lifecycle =========================================
    {
        "id": "cissp-iam-001", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An employee is being involuntarily terminated. From a security standpoint, what should "
                "happen to the employee's system access, and when?",
        "options": [
            {"id": "A", "text": "Delete the account a week later to allow a grace period"},
            {"id": "B", "text": "Leave the account active but move it to another department"},
            {"id": "C", "text": "Disable the account immediately, coordinated with the termination notification"},
            {"id": "D", "text": "Reduce the account to read-only access indefinitely"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Access should be disabled immediately and in step with the termination notification to "
                       "prevent retaliation; disabling (rather than deleting) preserves data and keys for continuity.",
            "distractors": {
                "A": "Delaying and deleting leaves an exploitable window and can destroy data/keys needed later.",
                "B": "Leaving the account active retains the risk the termination is meant to remove.",
                "D": "An indefinite read-only account is still a usable, exploitable account for a former employee.",
            },
            "exam_pattern": "On termination (especially involuntary), disable access immediately and in step with "
                            "notification; disable rather than delete to preserve data/keys.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Deprovisioning / offboarding"],
    },
    {
        "id": "cissp-iam-002", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Over years of transfers and promotions, several employees have accumulated access rights "
                "they no longer need. Which control is specifically DESIGNED to detect and remove this "
                "privilege creep?",
        "options": [
            {"id": "A", "text": "Periodic user access reviews (recertification)"},
            {"id": "B", "text": "Mandatory password rotation"},
            {"id": "C", "text": "Antivirus scanning"},
            {"id": "D", "text": "Network segmentation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Periodic access reviews (recertification) re-examine each user's entitlements against "
                       "current job needs, catching and removing accumulated, unneeded rights.",
            "distractors": {
                "B": "Password rotation changes credentials but does not review what entitlements a user holds.",
                "C": "Antivirus scanning addresses malware, not excess access rights.",
                "D": "Segmentation limits network reach but does not review individual user entitlements.",
            },
            "exam_pattern": "Privilege creep (aggregation) is caught by periodic access reviews/recertification "
                            "and enforced least privilege.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Access review and recertification"],
    },
    {
        "id": "cissp-iam-003", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Before issuing credentials, an organization must verify that a new user is who they claim "
                "to be, for example by validating government-issued identification. What is this step "
                "called?",
        "options": [
            {"id": "A", "text": "Authorization"},
            {"id": "B", "text": "Accounting"},
            {"id": "C", "text": "Federation"},
            {"id": "D", "text": "Identity proofing"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Identity proofing (registration/enrollment) establishes and verifies a person's "
                       "real-world identity before credentials are issued.",
            "distractors": {
                "A": "Authorization determines what an already-identified subject is permitted to do.",
                "B": "Accounting records a subject's actions after authentication.",
                "C": "Federation shares identities across organizations; it is not initial identity verification.",
            },
            "exam_pattern": "Identity proofing/registration verifies real-world identity before credentials are issued.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Identity proofing / registration"],
    },
    {
        "id": "cissp-iam-004", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The principle that each user, process, or system should be granted "
                "only the minimum access rights required to perform its function - and no more - is called "
                "least ________.",
        "correct": ["privilege"],
        "explanation": {
            "correct": "Least privilege restricts rights to the minimum necessary, limiting both the attack "
                       "surface and the damage a compromised account can do.",
            "exam_pattern": "Least privilege (with need-to-know) grants the minimum access required - nothing extra.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Least privilege"],
    },

    # ===== cissp_authentication_methods =====================================
    {
        "id": "cissp-iam-005", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 2, "type": "mcq",
        "stem": "A system requires users to enter a password and then approve a prompt on a registered "
                "hardware token. Why does this qualify as multifactor authentication, whereas a password "
                "plus a security question would not?",
        "options": [
            {"id": "A", "text": "Because two passwords are inherently stronger than one"},
            {"id": "B", "text": "Because it combines two different factor types - something you know and something you have"},
            {"id": "C", "text": "Because hardware tokens cannot be phished"},
            {"id": "D", "text": "Because a security question is not considered a credential"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Multifactor authentication requires factors from different categories; a password "
                       "(something you know) plus a hardware token (something you have) spans two categories.",
            "distractors": {
                "A": "The number of secrets is irrelevant; MFA requires different factor types, not more of one.",
                "C": "Resistance to phishing is a benefit of tokens but is not what makes authentication multifactor.",
                "D": "A password and a security question are both 'something you know' - the same factor type, so "
                     "together they are not multifactor.",
            },
            "exam_pattern": "MFA requires factors from different categories (know/have/are); two of the same type "
                            "is not MFA.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Multifactor authentication"],
    },
    {
        "id": "cissp-iam-006", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 3, "type": "mcq",
        "stem": "When tuning a biometric system, which error is the MOST serious from a security "
                "perspective, because it admits unauthorized individuals?",
        "options": [
            {"id": "A", "text": "A high false acceptance rate (FAR, a Type II error)"},
            {"id": "B", "text": "A high false rejection rate (FRR, a Type I error)"},
            {"id": "C", "text": "A low crossover error rate (CER)"},
            {"id": "D", "text": "A long enrollment time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A high false acceptance rate (FAR, Type II) means impostors are wrongly accepted, "
                       "which is the most serious failure for security.",
            "distractors": {
                "B": "A high false rejection rate (FRR, Type I) wrongly rejects legitimate users - an "
                     "inconvenience, not a breach.",
                "C": "A low crossover error rate indicates a more accurate system and is desirable.",
                "D": "Long enrollment time affects usability, not whether impostors are admitted.",
            },
            "exam_pattern": "FAR (Type II) admits impostors - the worst security error; FRR (Type I) rejects "
                            "valid users; lower CER = better.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Biometric error rates"],
    },
    {
        "id": "cissp-iam-007", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 1, "type": "mcq",
        "stem": "A smart card that a user must physically insert to log in represents which category of "
                "authentication factor?",
        "options": [
            {"id": "A", "text": "Something you know"},
            {"id": "B", "text": "Something you are"},
            {"id": "C", "text": "Something you have"},
            {"id": "D", "text": "Somewhere you are"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A smart card is a physical object the user possesses, which is the 'something you have' "
                       "factor.",
            "distractors": {
                "A": "Something you know is a secret such as a password or PIN.",
                "B": "Something you are is a biometric trait such as a fingerprint.",
                "D": "Somewhere you are is a location-based factor, not a physical object.",
            },
            "exam_pattern": "Token/smart card = something you have; password/PIN = know; biometric = are.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Authentication factor types"],
    },
    {
        "id": "cissp-iam-008", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: When comparing biometric systems, the error rate at the point where "
                "the false acceptance rate equals the false rejection rate - a key accuracy measure where "
                "lower is better - is the ________ error rate (give the term or its acronym).",
        "correct": ["crossover", "cer", "equal", "eer", "crossover error", "equal error"],
        "explanation": {
            "correct": "The crossover error rate (CER), also called the equal error rate (EER), is where FAR "
                       "and FRR intersect; a lower CER indicates a more accurate biometric system.",
            "exam_pattern": "CER/EER = point where FAR equals FRR; lower CER = more accurate biometric.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Crossover error rate"],
    },

    # ===== cissp_access_control_models ======================================
    {
        "id": "cissp-iam-009", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "A defense system enforces access by comparing a subject's security clearance to an "
                "object's classification label, and ordinary users cannot alter these labels or grant "
                "access to others. Which access control model is this?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Role-based access control (RBAC)"},
            {"id": "C", "text": "Rule-based access control (RuBAC)"},
            {"id": "D", "text": "Mandatory access control (MAC)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Mandatory access control is system-enforced using clearance-versus-classification "
                       "labels; subjects cannot change the labels or delegate access.",
            "distractors": {
                "A": "DAC lets data owners grant access at their discretion, the opposite of system-enforced labels.",
                "B": "RBAC assigns access by job role, not by clearance/classification labels.",
                "C": "RuBAC applies global rules (such as firewall rules), not clearance-based labeling.",
            },
            "exam_pattern": "System-enforced clearance vs classification labels, users cannot change = MAC "
                            "(military/high-security).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Mandatory access control"],
    },
    {
        "id": "cissp-iam-010", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "On a file server, the owner of each file decides which other users may read or modify it "
                "by editing the file's access control list. Which access control model is in use?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Mandatory access control (MAC)"},
            {"id": "C", "text": "Attribute-based access control (ABAC)"},
            {"id": "D", "text": "Role-based access control (RBAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Discretionary access control lets the resource owner decide, at their discretion, who "
                       "may access the object - typically implemented with access control lists.",
            "distractors": {
                "B": "MAC is system-enforced via labels and does not let owners set permissions at their discretion.",
                "C": "ABAC decides access from evaluated attributes and policies, not owner-set ACLs.",
                "D": "RBAC grants access through roles, not individual owner discretion.",
            },
            "exam_pattern": "Owner sets permissions via ACLs at their discretion = DAC (identity-based).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Discretionary access control"],
    },
    {
        "id": "cissp-iam-011", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "A hospital with high staff turnover wants to grant access by job function, so that "
                "onboarding a new nurse simply assigns the 'nurse' role with its predefined permissions. "
                "Which model BEST fits?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Role-based access control (RBAC)"},
            {"id": "C", "text": "Mandatory access control (MAC)"},
            {"id": "D", "text": "Rule-based access control (RuBAC)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Role-based access control assigns permissions to roles tied to job functions, so "
                       "high-turnover onboarding and offboarding is handled by assigning or removing a role.",
            "distractors": {
                "A": "DAC would require setting individual permissions per user, cumbersome with high turnover.",
                "C": "MAC uses clearance labels, not job-function roles, and is far more rigid than needed.",
                "D": "RuBAC applies uniform rules to everyone, not job-function role assignments.",
            },
            "exam_pattern": "Access by job function/role, ideal for high turnover = RBAC.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Role-based access control"],
    },
    {
        "id": "cissp-iam-012", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 3, "type": "mcq",
        "stem": "An organization needs access decisions that consider several attributes at once - the "
                "user's department, the resource's sensitivity, the time of day, and the device's security "
                "posture - evaluated against policies. Which model provides this fine-grained, dynamic "
                "control?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC)"},
            {"id": "B", "text": "Mandatory access control (MAC)"},
            {"id": "C", "text": "Attribute-based access control (ABAC)"},
            {"id": "D", "text": "Role-based access control (RBAC)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Attribute-based access control evaluates policies over multiple attributes of the "
                       "subject, resource, action, and environment, giving the most granular and dynamic control.",
            "distractors": {
                "A": "DAC relies on owner-set permissions, not multi-attribute policy evaluation.",
                "B": "MAC uses fixed clearance labels, not contextual attributes like time or device posture.",
                "D": "RBAC assigns access by role alone and is less granular than attribute-and-context evaluation.",
            },
            "exam_pattern": "Access decided from many attributes/context (user, resource, environment) via policy = ABAC.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Attribute-based access control"],
    },

    # ===== cissp_federated_identity =========================================
    {
        "id": "cissp-iam-013", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_federated_identity", "difficulty": 2, "type": "mcq",
        "stem": "A company wants employees to log in once at their identity provider and then reach "
                "multiple partner web applications without re-entering credentials, using XML-based "
                "assertions exchanged between an identity provider and service providers. Which standard "
                "is designed for this?",
        "options": [
            {"id": "A", "text": "SAML (Security Assertion Markup Language)"},
            {"id": "B", "text": "RADIUS"},
            {"id": "C", "text": "A Kerberos realm trust within a single domain"},
            {"id": "D", "text": "TACACS+"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SAML exchanges XML assertions between an identity provider (IdP) and service providers "
                       "(SPs) to enable cross-domain web browser single sign-on.",
            "distractors": {
                "B": "RADIUS centralizes network-access authentication (VPN/Wi-Fi), not cross-domain web SSO assertions.",
                "C": "Kerberos provides SSO within a realm/domain but is not the XML browser-federation standard "
                     "across organizations.",
                "D": "TACACS+ is a device-administration AAA protocol, not a web-federation standard.",
            },
            "exam_pattern": "XML assertions for cross-domain web SSO, IdP → SP = SAML.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Federated identity (SAML)"],
    },
    {
        "id": "cissp-iam-014", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_federated_identity", "difficulty": 3, "type": "mcq",
        "stem": "A mobile app lets a user grant it limited access to their photos held by another service "
                "WITHOUT sharing the user's password, and a separate layer is then used to actually "
                "confirm the user's identity. Which pairing is correct?",
        "options": [
            {"id": "A", "text": "OAuth 2.0 authenticates the user; SAML authorizes the app"},
            {"id": "B", "text": "OAuth 2.0 provides delegated authorization; OpenID Connect (OIDC) adds authentication on top of it"},
            {"id": "C", "text": "OpenID Connect handles delegated authorization; OAuth handles encryption"},
            {"id": "D", "text": "Kerberos provides the delegated authorization to the third-party app"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "OAuth 2.0 is a delegated authorization framework (granting limited access without "
                       "sharing the password); OpenID Connect is an authentication layer built on top of OAuth 2.0.",
            "distractors": {
                "A": "OAuth 2.0 is for authorization, not primarily authentication, and SAML is not what "
                     "authorizes the app in this OAuth scenario.",
                "C": "This reverses the roles: OIDC is the authentication layer and OAuth provides authorization; "
                     "neither is an encryption protocol.",
                "D": "Kerberos is an enterprise SSO protocol, not the mechanism for delegated third-party API access.",
            },
            "exam_pattern": "OAuth 2.0 = delegated authorization (access without sharing the password); OIDC = "
                            "authentication layer on OAuth.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - OAuth 2.0 and OpenID Connect"],
    },
    {
        "id": "cissp-iam-015", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_federated_identity", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise single sign-on system uses a trusted Key Distribution Center to issue "
                "time-stamped tickets, relies on symmetric-key cryptography, and requires synchronized "
                "clocks across hosts. Which protocol is this, and what is a notable weakness?",
        "options": [
            {"id": "A", "text": "SAML; its assertions cannot be encrypted"},
            {"id": "B", "text": "OAuth 2.0; it transmits passwords in clear text"},
            {"id": "C", "text": "RADIUS; it cannot support single sign-on"},
            {"id": "D", "text": "Kerberos; the KDC is a single point of failure and clock skew can break authentication"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Kerberos uses a Key Distribution Center, time-stamped tickets, and symmetric keys for "
                       "SSO; the KDC is a single point of failure, and it depends on synchronized clocks "
                       "(clock skew breaks authentication).",
            "distractors": {
                "A": "SAML uses XML assertions (which can be signed/encrypted) and does not use a KDC or tickets.",
                "B": "OAuth 2.0 uses tokens and does not transmit passwords in clear text as described.",
                "C": "RADIUS is a AAA protocol and does not use a KDC issuing time-stamped tickets.",
            },
            "exam_pattern": "KDC + time-stamped tickets + symmetric keys + clock sync = Kerberos; weaknesses: KDC "
                            "single point of failure and clock-skew sensitivity.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Kerberos"],
    },
]
