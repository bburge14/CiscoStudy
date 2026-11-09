"""(ISC)² Certified in Cybersecurity (CC) pool - Domain 3: Access Controls Concepts.

Original, objective-aligned practice items for the four Access Controls subtopics
CertLab tracks:
  * cc_access_control_concepts - subjects/objects, least privilege, separation of
                                 duties, need to know, and defense in depth.
  * cc_physical_access         - access control vestibules (mantraps), tailgating,
                                 CCTV, guards, badges, and other physical controls.
  * cc_logical_access          - the access control models DAC, MAC, RBAC, and ABAC.
  * cc_identity_management      - identification vs. authentication, authentication
                                 factors, MFA, and AAA/accounting.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased, every
wrong option carries a distractor note, and each item names the (ISC)² CC exam-outline
area it draws on. Entry-level depth only - core, well-established facts.
"""

QUESTIONS = [
    # ===== cc_access_control_concepts =======================================
    {
        "id": "isc2cc-acc-001", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts", "difficulty": 1, "type": "mcq",
        "stem": "A security baseline states that each employee should receive only the access rights "
                "needed to perform their specific job - nothing more. Which principle is this?",
        "options": [
            {"id": "A", "text": "Implicit allow"},
            {"id": "B", "text": "Separation of duties"},
            {"id": "C", "text": "Defense in depth"},
            {"id": "D", "text": "Least privilege"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Least privilege gives each subject only the minimum access necessary to perform "
                       "its function, limiting the damage from mistakes or compromise.",
            "distractors": {
                "A": "Implicit allow is the opposite of good practice; secure design uses implicit deny.",
                "B": "Separation of duties splits a critical task across people; it is not about minimizing one person's rights.",
                "C": "Defense in depth layers multiple controls; it does not define how much access a user gets.",
            },
            "exam_pattern": "Give only the minimum access needed to do the job = least privilege.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Access control concepts (least privilege)"],
    },
    {
        "id": "isc2cc-acc-002", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts", "difficulty": 2, "type": "mcq",
        "stem": "To reduce fraud, a company requires one employee to submit a payment request and a "
                "different employee to approve it, so no single person can do both. This is:",
        "options": [
            {"id": "A", "text": "Least privilege"},
            {"id": "B", "text": "Separation (segregation) of duties"},
            {"id": "C", "text": "Need to know"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Separation of duties divides a critical task among multiple people so that no one "
                       "individual can complete it alone, reducing fraud and error.",
            "distractors": {
                "A": "Least privilege limits how much access one person has; it does not require splitting a task across people.",
                "C": "Need to know restricts access to specific information, not the division of a transaction's steps.",
                "D": "Single sign-on is an authentication convenience, unrelated to splitting duties.",
            },
            "exam_pattern": "Split a critical task so no one person controls it end to end = separation of duties.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Access control concepts (separation of duties)"],
    },
    {
        "id": "isc2cc-acc-003", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts", "difficulty": 2, "type": "mcq",
        "stem": "In access control terminology, when a user runs a program that opens a document file, "
                "which element is the SUBJECT?",
        "options": [
            {"id": "A", "text": "The document file"},
            {"id": "B", "text": "The user (acting through the program)"},
            {"id": "C", "text": "The folder the file is stored in"},
            {"id": "D", "text": "The hard drive"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A subject is the active entity (a user or the process acting on their behalf) that "
                       "requests access to a resource.",
            "distractors": {
                "A": "The document file is the object - the passive resource being acted upon.",
                "C": "The folder is also an object (a container resource), not the active requester.",
                "D": "The hard drive is a storage object, not the active entity requesting access.",
            },
            "exam_pattern": "Active entity that acts = subject; passive resource acted upon = object.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Access control concepts (subjects and objects)"],
    },
    {
        "id": "isc2cc-acc-004", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts", "difficulty": 3, "type": "mcq",
        "stem": "An analyst holds a Secret clearance but is granted access only to the specific Secret "
                "case files for the project assigned to her - not every Secret file. Which principle "
                "most precisely governs this restriction?",
        "options": [
            {"id": "A", "text": "Need to know"},
            {"id": "B", "text": "Defense in depth"},
            {"id": "C", "text": "Separation of duties"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Need to know restricts access to only the specific information required for a "
                       "person's task, even when their clearance would technically permit more.",
            "distractors": {
                "B": "Defense in depth is about layering controls, not limiting which specific files a cleared user may see.",
                "C": "Separation of duties splits a task among people; it does not scope a single analyst's file access.",
                "D": "Non-repudiation proves who did an action; it is unrelated to limiting information access.",
            },
            "exam_pattern": "Cleared but limited to only the info the task requires = need to know (narrower than least privilege).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Access control concepts (need to know)"],
    },
    {
        "id": "isc2cc-acc-005", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts", "difficulty": 2, "type": "fill",
        "stem": "A security design uses several independent layers of controls - a firewall, then "
                "network segmentation, then host hardening - so that if one layer fails, others still "
                "protect the asset. This strategy of layering controls is called ___.",
        "correct": ["defense in depth", "defence in depth", "layered security", "layered defense", "layering"],
        "explanation": {
            "correct": "Defense in depth layers multiple, independent safeguards so the failure of any "
                       "single control does not expose the asset.",
            "exam_pattern": "Multiple overlapping layers of controls = defense in depth.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Access control concepts (defense in depth)"],
    },

    # ===== cc_physical_access ===============================================
    {
        "id": "isc2cc-acc-006", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_physical_access", "difficulty": 2, "type": "mcq",
        "stem": "To enter a secure area, a person steps into a small booth with two interlocking doors; "
                "the second door opens only after the first closes, admitting one person at a time. "
                "This control is a(n):",
        "options": [
            {"id": "A", "text": "Honeypot"},
            {"id": "B", "text": "Bollard"},
            {"id": "C", "text": "Faraday cage"},
            {"id": "D", "text": "Access control vestibule (mantrap)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An access control vestibule (mantrap) uses two interlocking doors to admit one "
                       "person at a time, preventing an unauthorized person from slipping in behind another.",
            "distractors": {
                "A": "A honeypot is a decoy system to lure attackers, not a physical entry control.",
                "B": "A bollard is a post that blocks vehicles; it does not control person-by-person entry.",
                "C": "A Faraday cage blocks electromagnetic signals; it is not an entry-control booth.",
            },
            "exam_pattern": "Two interlocking doors, one person at a time = access control vestibule / mantrap.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Physical access controls (vestibule/mantrap)"],
    },
    {
        "id": "isc2cc-acc-007", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_physical_access", "difficulty": 1, "type": "mcq",
        "stem": "An unauthorized person closely follows an employee through a badge-controlled door "
                "before it closes, never presenting their own credential. This technique is called:",
        "options": [
            {"id": "A", "text": "Tailgating (piggybacking)"},
            {"id": "B", "text": "Phishing"},
            {"id": "C", "text": "Spoofing"},
            {"id": "D", "text": "Sniffing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tailgating (piggybacking) is following an authorized person through a controlled "
                       "entry point to bypass physical access controls without valid credentials.",
            "distractors": {
                "B": "Phishing is a deceptive electronic message, not physically following someone through a door.",
                "C": "Spoofing is falsifying an identity or address in communications, not a physical entry trick.",
                "D": "Sniffing is capturing network traffic, unrelated to walking through a door.",
            },
            "exam_pattern": "Slipping through a door behind an authorized person = tailgating/piggybacking.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Physical access controls (tailgating)"],
    },
    {
        "id": "isc2cc-acc-008", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_physical_access", "difficulty": 2, "type": "mcq",
        "stem": "A building installs CCTV cameras that record everyone entering the lobby but do not "
                "physically stop anyone. By function, CCTV primarily acts as which kind of control?",
        "options": [
            {"id": "A", "text": "A preventive control"},
            {"id": "B", "text": "A detective control"},
            {"id": "C", "text": "A corrective control"},
            {"id": "D", "text": "A compensating control"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "CCTV records activity so events can be identified and investigated, making it "
                       "primarily a detective control (it also deters, but it does not prevent entry).",
            "distractors": {
                "A": "A preventive control would stop entry; cameras only observe and record.",
                "C": "A corrective control fixes or restores after an incident; cameras do not remediate.",
                "D": "A compensating control substitutes for another control; that is not CCTV's primary role here.",
            },
            "exam_pattern": "Records/monitors to spot events after the fact = detective control.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Physical access controls (surveillance/CCTV)"],
    },
    {
        "id": "isc2cc-acc-009", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_physical_access", "difficulty": 3, "type": "mcq",
        "stem": "A site wants a physical control that can verify visitor identities, exercise judgment "
                "about unusual situations, and actively respond to an intruder. Which control best "
                "provides this flexibility?",
        "options": [
            {"id": "A", "text": "A CCTV camera"},
            {"id": "B", "text": "A bollard"},
            {"id": "C", "text": "A security guard"},
            {"id": "D", "text": "A door lock"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A security guard is a flexible physical control: a human can check identities, "
                       "adapt to unexpected events, and intervene or respond to an intruder.",
            "distractors": {
                "A": "A CCTV camera records but cannot exercise judgment or physically intervene.",
                "B": "A bollard is a fixed barrier that only blocks vehicles; it cannot verify identity or respond.",
                "D": "A door lock only permits or denies based on a key/credential; it cannot assess a situation.",
            },
            "exam_pattern": "Need human judgment and active response among physical controls = security guard.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Physical access controls (guards)"],
    },

    # ===== cc_logical_access ================================================
    {
        "id": "isc2cc-acc-010", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_logical_access", "difficulty": 2, "type": "mcq",
        "stem": "When a worker is hired as an accountant, the system automatically grants them the "
                "permissions tied to the 'Accountant' job function. Which access control model is this?",
        "options": [
            {"id": "A", "text": "Role-Based Access Control (RBAC)"},
            {"id": "B", "text": "Discretionary Access Control (DAC)"},
            {"id": "C", "text": "Mandatory Access Control (MAC)"},
            {"id": "D", "text": "Attribute-Based Access Control (ABAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC assigns permissions to roles that map to job functions; users gain access by "
                       "being placed in the appropriate role, simplifying administration.",
            "distractors": {
                "B": "DAC lets the resource owner decide access case by case, not by predefined job roles.",
                "C": "MAC enforces access through system-assigned security labels and clearances, not job roles.",
                "D": "ABAC grants access by evaluating attributes/policies (user, resource, environment), not by role membership alone.",
            },
            "exam_pattern": "Access granted by job role/function = RBAC.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Logical access controls (RBAC)"],
    },
    {
        "id": "isc2cc-acc-011", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_logical_access", "difficulty": 2, "type": "mcq",
        "stem": "On a file server, each file's owner personally decides which other users may read or "
                "edit that file by setting its permissions. Which access control model is in use?",
        "options": [
            {"id": "A", "text": "Mandatory Access Control (MAC)"},
            {"id": "B", "text": "Discretionary Access Control (DAC)"},
            {"id": "C", "text": "Role-Based Access Control (RBAC)"},
            {"id": "D", "text": "Rule-Based Access Control"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DAC gives the owner of a resource discretion to grant or deny access to it, as with "
                       "standard file permissions set by the file's owner.",
            "distractors": {
                "A": "MAC removes owner discretion; the system enforces access by labels and clearances.",
                "C": "RBAC ties access to job roles, not to an owner's per-file choices.",
                "D": "Rule-based control applies global rules (e.g., firewall rules) to everyone, not owner-set file permissions.",
            },
            "exam_pattern": "Resource owner decides who gets access = discretionary (DAC).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Logical access controls (DAC)"],
    },
    {
        "id": "isc2cc-acc-012", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_logical_access", "difficulty": 2, "type": "mcq",
        "stem": "In a classified government system, every file carries a sensitivity label and every "
                "user a clearance; the operating system - not any user - decides access, and users "
                "cannot change these rules. Which model is this?",
        "options": [
            {"id": "A", "text": "Discretionary Access Control (DAC)"},
            {"id": "B", "text": "Role-Based Access Control (RBAC)"},
            {"id": "C", "text": "Mandatory Access Control (MAC)"},
            {"id": "D", "text": "Attribute-Based Access Control (ABAC)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MAC is system-enforced using security labels and clearances; users cannot alter "
                       "access decisions, which is why it is the most restrictive model and common in military/government settings.",
            "distractors": {
                "A": "DAC lets owners set access at their discretion, the opposite of system-enforced labels.",
                "B": "RBAC assigns access by job role, not by mandatory sensitivity labels and clearances.",
                "D": "ABAC uses flexible attribute policies; MAC specifically enforces fixed labels/clearances the user cannot change.",
            },
            "exam_pattern": "System-enforced labels/clearances, user cannot override, most restrictive = MAC.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Logical access controls (MAC)"],
    },
    {
        "id": "isc2cc-acc-013", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_logical_access", "difficulty": 3, "type": "mcq",
        "stem": "An access system grants or denies a request by evaluating multiple attributes together "
                "- the user's department, the device's security posture, the time of day, and the "
                "resource's sensitivity. Which model offers this fine-grained, policy-driven control?",
        "options": [
            {"id": "A", "text": "Role-Based Access Control (RBAC)"},
            {"id": "B", "text": "Discretionary Access Control (DAC)"},
            {"id": "C", "text": "Attribute-Based Access Control (ABAC)"},
            {"id": "D", "text": "Mandatory Access Control (MAC)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "ABAC makes access decisions by evaluating attributes of the subject, object, and "
                       "environment against policies, giving the most granular and dynamic control.",
            "distractors": {
                "A": "RBAC decides access by role membership alone, not by device posture, time, or other attributes.",
                "B": "DAC relies on the owner's discretion, not a combination of multiple attributes.",
                "D": "MAC uses fixed security labels and clearances, not a flexible blend of many attributes.",
            },
            "exam_pattern": "Access from many attributes (user/device/time/resource) + policies = ABAC.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Logical access controls (ABAC)"],
    },
    {
        "id": "isc2cc-acc-014", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_logical_access", "difficulty": 3, "type": "mcq",
        "stem": "A large enterprise with constant staff changes wants to simplify administration so that "
                "access automatically fits each person's job and updates when they change positions. "
                "Compared with DAC, why is RBAC better suited here?",
        "options": [
            {"id": "A", "text": "Permissions are tied to roles, so changing a user's role updates their access consistently"},
            {"id": "B", "text": "Each resource owner can set permissions individually for every file"},
            {"id": "C", "text": "The system labels every object with a classification the user cannot change"},
            {"id": "D", "text": "Access requires no authentication at all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC maps permissions to roles; moving a user between roles consistently grants and "
                       "revokes the right access, which scales well in large, fast-changing organizations.",
            "distractors": {
                "B": "Owner-by-owner, file-by-file permission setting describes DAC, which is exactly the hard-to-manage approach being replaced.",
                "C": "System-enforced classification labels describe MAC, not an advantage of RBAC over DAC.",
                "D": "No model removes authentication; access control still requires verifying identity first.",
            },
            "exam_pattern": "RBAC scales administration by job role; DAC's per-owner choices get unmanageable at scale.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Logical access controls (RBAC vs. DAC)"],
    },

    # ===== cc_identity_management ===========================================
    {
        "id": "isc2cc-acc-015", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_identity_management", "difficulty": 1, "type": "mcq",
        "stem": "A user types a username to claim who they are, then enters a password. What is the "
                "step of PROVING the claimed identity called?",
        "options": [
            {"id": "A", "text": "Identification"},
            {"id": "B", "text": "Authentication"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "Accounting"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Authentication verifies (proves) a claimed identity - for example, by checking the "
                       "password that goes with the username.",
            "distractors": {
                "A": "Identification is the claim of identity (typing the username), not the proof of it.",
                "C": "Authorization decides what an authenticated user may do, which comes after proving identity.",
                "D": "Accounting records what the user does; it is not the step that proves identity.",
            },
            "exam_pattern": "Claim identity = identification; prove it = authentication; then authorization.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Identity management (identification vs. authentication)"],
    },
    {
        "id": "isc2cc-acc-016", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_identity_management", "difficulty": 2, "type": "mcq",
        "stem": "A user logs in by inserting a physical hardware security key (a USB token) they carry. "
                "Which authentication factor category does this token represent?",
        "options": [
            {"id": "A", "text": "Something you know"},
            {"id": "B", "text": "Something you are"},
            {"id": "C", "text": "Something you have"},
            {"id": "D", "text": "Somewhere you are"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A hardware token/security key is a possession, so it is a 'something you have' "
                       "authentication factor.",
            "distractors": {
                "A": "'Something you know' is knowledge like a password or PIN, not a physical object.",
                "B": "'Something you are' is a biometric trait such as a fingerprint, not a carried device.",
                "D": "'Somewhere you are' is a location-based factor, not the possession of a token.",
            },
            "exam_pattern": "Token/smart card/phone = something you have; password/PIN = know; biometric = are.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Identity management (authentication factors)"],
    },
    {
        "id": "isc2cc-acc-017", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_identity_management", "difficulty": 2, "type": "mcq",
        "stem": "A bank requires customers to enter a password and then a one-time code from an "
                "authenticator app on their phone. Why does this qualify as multifactor authentication?",
        "options": [
            {"id": "A", "text": "It combines two different factor types (something you know + something you have)"},
            {"id": "B", "text": "It uses two separate passwords"},
            {"id": "C", "text": "The password is long and complex"},
            {"id": "D", "text": "It logs the user's location"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multifactor authentication requires two or more factors from DIFFERENT categories; "
                       "a password (know) plus a one-time code from a phone (have) meets that bar.",
            "distractors": {
                "B": "Two passwords are both 'something you know,' the same factor type, so that is not multifactor.",
                "C": "A strong password is still a single factor; complexity does not make it multifactor.",
                "D": "Logging location is not the reason; MFA requires combining different factor types, which this does.",
            },
            "exam_pattern": "MFA = two or more DIFFERENT factor types; two of the same type does not count.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Identity management (MFA)"],
    },
    {
        "id": "isc2cc-acc-018", "exam": "isc2cc", "domain": "cc_access_controls",
        "subtopic": "cc_identity_management", "difficulty": 2, "type": "fill",
        "stem": "In the AAA framework (authentication, authorization, and ___), the third 'A' is the "
                "process of recording and logging what an authenticated user does, creating an audit "
                "trail. Name that third 'A'. (one word)",
        "correct": ["accounting", "auditing", "accountability"],
        "explanation": {
            "correct": "Accounting (also called auditing) tracks and logs a user's actions, supporting "
                       "accountability and audit trails after identity and permissions are established.",
            "exam_pattern": "AAA = Authentication, Authorization, Accounting (logging/auditing user activity).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 3 - Identity management (AAA/accounting)"],
    },
]
