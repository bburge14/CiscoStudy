"""(ISC)2 SSCP pool - Round 2 expansion (all seven domains).

Original, objective-aligned practice items that DEEPEN the round-1 SSCP bank
(content_sscp_*.py, ids sscp-ops/acc/risk/ir/crypto/net/sys-NNN). Every item
here is new and non-duplicative: round 1 established the core terms, so round 2
pushes into the precise, practitioner-level facts the SSCP tests - control
functions, NIST SP 800-88 purge vs clear, biometric error types, OAuth/OIDC,
Bell-LaPadula/Biba, CVSS, NIST SP 800-61 and 800-86 process order, order of
volatility, block-cipher modes/ECB, perfect forward secrecy, IPsec AH/ESP
protocol numbers, VLAN double-tagging, WPA2 CCMP/EAP-TLS, container vs VM
isolation, and more.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===================================================================
    # Domain 1: Security Operations and Administration (sscp-ops-r2-*)
    # ===================================================================

    # ----- sscp_cia_ethics --------------------------------------------
    {
        "id": "sscp-ops-r2-001", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 2, "type": "mcq",
        "stem": "Security professionals sometimes refer to the 'DAD triad' as the inverse of the CIA "
                "triad - the three outcomes that security controls exist to prevent. Which set does "
                "DAD represent?",
        "options": [
            {"id": "A", "text": "Detection, Analysis, and Defense"},
            {"id": "B", "text": "Denial, Authentication, and Deterrence"},
            {"id": "C", "text": "Disclosure, Alteration, and Destruction"},
            {"id": "D", "text": "Data, Applications, and Devices"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DAD is the opposite of CIA: Disclosure defeats confidentiality, Alteration "
                       "defeats integrity, and Destruction (denial of access) defeats availability.",
            "distractors": {
                "A": "These are incident-analysis activities, not the recognized inverse of the CIA triad.",
                "B": "Denial relates to availability loss, but this is not the DAD set; authentication and deterrence are unrelated terms here.",
                "D": "These are asset categories, not the threat outcomes in the DAD model.",
            },
            "exam_pattern": "DAD = Disclosure (vs confidentiality), Alteration (vs integrity), Destruction/denial (vs availability).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - CIA and DAD triads"],
    },
    {
        "id": "sscp-ops-r2-002", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 2, "type": "mcq",
        "stem": "A digital signature lets a recipient prove that a specific sender created a message, so "
                "the sender cannot later credibly deny having sent it. Which security property does this "
                "provide?",
        "options": [
            {"id": "A", "text": "Availability"},
            {"id": "B", "text": "Non-repudiation"},
            {"id": "C", "text": "Confidentiality"},
            {"id": "D", "text": "Redundancy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Non-repudiation prevents a party from denying an action; a digital signature "
                       "(created with the sender's private key) binds the action to the signer. It is a "
                       "service beyond the core CIA triad.",
            "distractors": {
                "A": "Availability concerns timely access/uptime, not proof of origin.",
                "C": "Confidentiality is secrecy (achieved by encryption), not proof that a sender acted.",
                "D": "Redundancy is a technique that supports availability, not a proof-of-origin property.",
            },
            "exam_pattern": "Cannot deny having done it = non-repudiation (provided by digital signatures).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security services (non-repudiation)"],
    },
    {
        "id": "sscp-ops-r2-003", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 3, "type": "mcq",
        "stem": "An SSCP discovers that an employer is quietly shipping a product with a serious security "
                "flaw that endangers the public. Applying the (ISC)2 Code of Ethics, which consideration "
                "takes precedence when the canons appear to conflict?",
        "options": [
            {"id": "A", "text": "Advancing and protecting the profession above all"},
            {"id": "B", "text": "Loyalty to the employer regardless of consequences"},
            {"id": "C", "text": "The member's personal financial interest"},
            {"id": "D", "text": "Protecting society, the common good, and the public trust and infrastructure"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The canons are applied in listed order; the first and highest is to protect "
                       "society, the common good, necessary public trust and confidence, and the "
                       "infrastructure - which outranks duty to the principal/employer when they conflict.",
            "distractors": {
                "A": "Advancing and protecting the profession is the fourth (lowest-precedence) canon.",
                "B": "Diligent service to principals is the third canon and is subordinate to protecting society.",
                "C": "Personal financial gain is not an ethical consideration and conflicts with acting honorably.",
            },
            "exam_pattern": "Canon priority: society first, then act honorably, then principals, then profession.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - (ISC)2 Code of Ethics canons"],
    },

    # ----- sscp_security_controls -------------------------------------
    {
        "id": "sscp-ops-r2-004", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A security team reviews system audit logs and watches CCTV recordings after the fact to "
                "discover whether unauthorized activity has occurred. By FUNCTION, these are examples of "
                "which control type?",
        "options": [
            {"id": "A", "text": "Preventive"},
            {"id": "B", "text": "Deterrent"},
            {"id": "C", "text": "Detective"},
            {"id": "D", "text": "Compensating"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Detective controls identify and record that an event has occurred (audit logs, "
                       "CCTV review, IDS alerts); they do not stop the event but enable discovery and "
                       "investigation.",
            "distractors": {
                "A": "A preventive control stops an event before it happens; review after the fact does not.",
                "B": "A deterrent discourages a would-be attacker but does not itself detect activity.",
                "D": "A compensating control is an alternative safeguard used when a primary control is infeasible.",
            },
            "exam_pattern": "Finds/records events after they occur = detective (logs, IDS, CCTV review).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control functions"],
    },
    {
        "id": "sscp-ops-r2-005", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A company posts prominent 'this system is monitored and unauthorized access will be "
                "prosecuted' banners at logon. The PRIMARY control function of such a banner is:",
        "options": [
            {"id": "A", "text": "Deterrent"},
            {"id": "B", "text": "Detective"},
            {"id": "C", "text": "Corrective"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A deterrent control discourages a would-be attacker from attempting an action; "
                       "warning banners, visible cameras, and signage aim to dissuade rather than "
                       "physically block.",
            "distractors": {
                "B": "A detective control discovers events after they occur; a banner does not detect anything.",
                "C": "A corrective control remediates after an incident.",
                "D": "A recovery control restores operations or data after damage.",
            },
            "exam_pattern": "Discourages the attempt (banner, signage, visible guard) = deterrent.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control functions"],
    },
    {
        "id": "sscp-ops-r2-006", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "After ransomware encrypts a file server, the team restores the data from last night's "
                "clean backups to return the system to service. Restoring from backup is which control "
                "FUNCTION?",
        "options": [
            {"id": "A", "text": "Preventive"},
            {"id": "B", "text": "Detective"},
            {"id": "C", "text": "Deterrent"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Recovery controls restore systems and data to normal operation after an incident "
                       "or disaster (backups, system restoration, DR failover).",
            "distractors": {
                "A": "A preventive control stops the incident beforehand; it does not restore lost data.",
                "B": "A detective control identifies the incident; it does not restore operations.",
                "C": "A deterrent discourages the attacker and does nothing to restore service.",
            },
            "exam_pattern": "Restore operations/data after damage = recovery; fix the root cause during cleanup = corrective.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control functions"],
    },
    {
        "id": "sscp-ops-r2-007", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "Pre-employment background checks, written security policies, and mandatory security "
                "training are examples of which control CATEGORY?",
        "options": [
            {"id": "A", "text": "Physical controls"},
            {"id": "B", "text": "Technical (logical) controls"},
            {"id": "C", "text": "Administrative (managerial) controls"},
            {"id": "D", "text": "Compensating controls"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Administrative (managerial) controls are policies, procedures, standards, "
                       "screening, and training - the people-and-process safeguards that govern how "
                       "security is managed.",
            "distractors": {
                "A": "Physical controls are tangible barriers such as locks, guards, and fences.",
                "B": "Technical/logical controls are implemented in hardware or software (firewalls, encryption, ACLs).",
                "D": "'Compensating' is a role a control plays, not one of the three categories.",
            },
            "exam_pattern": "Policies/procedures/screening/training = administrative; hardware/software = technical; barriers = physical.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control categories"],
    },

    # ----- sscp_asset_change_mgmt -------------------------------------
    {
        "id": "sscp-ops-r2-008", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "In a formal change management process, what is the FIRST formal step that initiates a "
                "proposed modification and documents its scope, justification, risk, and rollback plan "
                "for review?",
        "options": [
            {"id": "A", "text": "Submitting a Request for Change (RFC / change request)"},
            {"id": "B", "text": "Executing the back-out plan"},
            {"id": "C", "text": "Closing the change record"},
            {"id": "D", "text": "Performing the post-implementation review"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A documented Request for Change (RFC) formally initiates the process; it captures "
                       "what/why/risk/rollback so the Change Advisory Board can assess and authorize it "
                       "before any implementation.",
            "distractors": {
                "B": "The back-out (rollback) plan is prepared earlier but executed later, only if the change fails.",
                "C": "Closing the change record happens at the end of the process.",
                "D": "The post-implementation review follows deployment, not initiation.",
            },
            "exam_pattern": "Change starts with a documented RFC/change request; the CAB reviews it before implementation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Change management"],
    },
    {
        "id": "sscp-ops-r2-009", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Which repository records the organization's configuration items (hardware, software, "
                "and their attributes and relationships) to support configuration and change "
                "management?",
        "options": [
            {"id": "A", "text": "Certificate Revocation List (CRL)"},
            {"id": "B", "text": "Configuration Management Database (CMDB)"},
            {"id": "C", "text": "Data Loss Prevention (DLP) console"},
            {"id": "D", "text": "Security Information and Event Management (SIEM)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A CMDB stores configuration items (CIs) and their relationships, giving change "
                       "and configuration management an authoritative inventory of what exists and how "
                       "components depend on one another.",
            "distractors": {
                "A": "A CRL lists revoked certificates in PKI.",
                "C": "DLP prevents unauthorized data exfiltration.",
                "D": "A SIEM aggregates and correlates security events and logs - it is not the CI repository.",
            },
            "exam_pattern": "Authoritative store of configuration items and relationships = CMDB.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Configuration management (CMDB)"],
    },
    {
        "id": "sscp-ops-r2-010", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Why does a well-run change management process require every significant change to include "
                "a documented back-out (rollback) plan before it is approved?",
        "options": [
            {"id": "A", "text": "To guarantee the change can never fail"},
            {"id": "B", "text": "To avoid having to test the change"},
            {"id": "C", "text": "To eliminate the need for Change Advisory Board approval"},
            {"id": "D", "text": "So operations can be restored to the prior known-good state if the change causes problems"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A back-out plan defines how to reverse the change and return to the last "
                       "known-good state if it fails or causes unexpected impact, limiting downtime and "
                       "risk.",
            "distractors": {
                "A": "No plan can guarantee a change never fails; that is precisely why a rollback exists.",
                "B": "A rollback plan complements testing; it does not replace it.",
                "C": "Changes still require CAB authorization; the rollback plan is part of that package.",
            },
            "exam_pattern": "Always plan how to undo a change (rollback/back-out) before deploying it.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Change management (back-out planning)"],
    },

    # ----- sscp_security_awareness ------------------------------------
    {
        "id": "sscp-ops-r2-011", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "In the awareness-training-education model, which level provides the broadest, long-term, "
                "concept-focused learning - for example, a degree program that develops the reasoning "
                "behind security decisions?",
        "options": [
            {"id": "A", "text": "Awareness"},
            {"id": "B", "text": "Training"},
            {"id": "C", "text": "Education"},
            {"id": "D", "text": "A phishing simulation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Education is the broad, long-term, theory-and-concept level that develops deep "
                       "understanding and decision-making (e.g., an academic degree), as opposed to "
                       "task-specific training or general awareness.",
            "distractors": {
                "A": "Awareness changes day-to-day behavior for all users; it is short and general, not deep.",
                "B": "Training builds specific job skills, narrower than broad education.",
                "D": "A phishing simulation is an awareness-measurement activity, not the education level.",
            },
            "exam_pattern": "Awareness = all users' behavior; Training = role skills; Education = broad, long-term concepts.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Awareness, training, and education"],
    },
    {
        "id": "sscp-ops-r2-012", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "An organization gives its software developers dedicated secure-coding instruction (input "
                "validation, avoiding injection flaws) that other staff do not receive. This is BEST "
                "described as:",
        "options": [
            {"id": "A", "text": "Role-based training targeted to a specific job function"},
            {"id": "B", "text": "General security awareness for all employees"},
            {"id": "C", "text": "A deterrent control"},
            {"id": "D", "text": "A background investigation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Role-based (role-specific) training delivers the specialized skills a particular "
                       "job needs - here, secure development practices for developers - rather than the "
                       "general content given to everyone.",
            "distractors": {
                "B": "General awareness is the baseline for all users and is not job-specialized.",
                "C": "A deterrent discourages attackers; it does not teach skills.",
                "D": "A background check is a personnel-screening control, not training.",
            },
            "exam_pattern": "Specialized, job-specific instruction = role-based training (e.g., secure coding for developers).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Role-based training"],
    },

    # ----- sscp_data_handling -----------------------------------------
    {
        "id": "sscp-ops-r2-013", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 3, "type": "mcq",
        "stem": "Under NIST SP 800-88 media sanitization, which category renders data recovery infeasible "
                "even against advanced laboratory techniques, yet may still leave the media reusable "
                "(e.g., cryptographic erase, verified secure-erase, or degaussing)?",
        "options": [
            {"id": "A", "text": "Clear"},
            {"id": "B", "text": "Purge"},
            {"id": "C", "text": "Destroy"},
            {"id": "D", "text": "Format"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Purge applies physical or logical techniques (cryptographic erase, ATA secure "
                       "erase/block erase, degaussing) that defeat state-of-the-art laboratory recovery; "
                       "the media can sometimes be reused afterward.",
            "distractors": {
                "A": "Clear uses basic overwrite and resists only simple, non-invasive recovery, not laboratory attacks.",
                "C": "Destroy (shred/incinerate/pulverize/melt) makes the media unusable afterward, whereas Purge may preserve it.",
                "D": "A format is not a defined 800-88 sanitization category and can leave recoverable remnants.",
            },
            "exam_pattern": "800-88: Clear (simple overwrite) < Purge (lab-resistant: crypto-erase/degauss/secure-erase) < Destroy (physical).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Media sanitization (NIST SP 800-88 Clear/Purge/Destroy)"],
    },
    {
        "id": "sscp-ops-r2-014", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 2, "type": "mcq",
        "stem": "Who is ACCOUNTABLE for classifying a data set and approving who may access it, as "
                "distinct from the IT staff who implement and maintain the protective controls day to "
                "day?",
        "options": [
            {"id": "A", "text": "The data custodian"},
            {"id": "B", "text": "The end user"},
            {"id": "C", "text": "The auditor"},
            {"id": "D", "text": "The data owner"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The data owner (typically a senior business manager) is accountable for the data: "
                       "assigning its classification and approving access. The data custodian (often IT) "
                       "implements and maintains the controls, backups, and access as directed.",
            "distractors": {
                "A": "The custodian implements and maintains controls but does not own or classify the data.",
                "B": "End users must follow handling rules but do not set classification or approve access.",
                "C": "An auditor independently reviews controls; the auditor does not own the data.",
            },
            "exam_pattern": "Owner = accountable, sets classification/access (business); Custodian = implements/maintains controls (IT).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Data roles (owner vs custodian)"],
    },
    {
        "id": "sscp-ops-r2-015", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 2, "type": "mcq",
        "stem": "A Data Loss Prevention (DLP) solution is configured to inspect and block sensitive "
                "records from leaving the organization through email and web uploads. Which data state is "
                "this egress inspection primarily protecting?",
        "options": [
            {"id": "A", "text": "Data at rest"},
            {"id": "B", "text": "Data in use"},
            {"id": "C", "text": "Data in transit (data in motion)"},
            {"id": "D", "text": "Data in archive"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Blocking sensitive data as it is transmitted out (email, web upload, network "
                       "transfer) protects data in transit/motion. DLP can also cover data at rest and in "
                       "use, but egress inspection targets data in motion.",
            "distractors": {
                "A": "Data at rest is stored data on disk/media, addressed by storage or endpoint DLP, not egress inspection.",
                "B": "Data in use is data actively processed in memory or on screen.",
                "D": "'Data in archive' is a form of data at rest, not the transmitting state.",
            },
            "exam_pattern": "Three data states: at rest (stored), in transit/motion (moving), in use (processing). Egress blocking = in transit.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Data states and DLP"],
    },

    # ===================================================================
    # Domain 2: Access Controls (sscp-acc-r2-*)
    # ===================================================================

    # ----- sscp_authn_methods -----------------------------------------
    {
        "id": "sscp-acc-r2-001", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_authn_methods", "difficulty": 3, "type": "mcq",
        "stem": "A user clicks 'Allow' so a photo-printing app can access their cloud photos without ever "
                "revealing the user's password. The app receives a scoped access token for just the "
                "photos. Which framework provides this delegated AUTHORIZATION?",
        "options": [
            {"id": "A", "text": "Kerberos"},
            {"id": "B", "text": "RADIUS"},
            {"id": "C", "text": "OAuth 2.0"},
            {"id": "D", "text": "WEP"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "OAuth 2.0 is a delegated authorization framework: a user authorizes a "
                       "third-party app to access specific resources via a scoped access token, without "
                       "sharing credentials. OpenID Connect (OIDC) adds an identity/authentication layer "
                       "on top of OAuth.",
            "distractors": {
                "A": "Kerberos is an internal SSO authentication protocol using tickets, not web delegated authorization.",
                "B": "RADIUS is an AAA protocol for network access, not user-consented resource delegation.",
                "D": "WEP is an obsolete wireless encryption scheme, unrelated to authorization delegation.",
            },
            "exam_pattern": "Delegated authorization with scoped tokens = OAuth 2.0; authentication layer on top = OpenID Connect (OIDC).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Federated authorization (OAuth/OIDC)"],
    },
    {
        "id": "sscp-acc-r2-002", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_authn_methods", "difficulty": 3, "type": "mcq",
        "stem": "When tuning a biometric system, which error is the most security-critical because it "
                "admits an impostor as if they were a legitimate user?",
        "options": [
            {"id": "A", "text": "False Rejection Rate (FRR), a Type I error"},
            {"id": "B", "text": "False Acceptance Rate (FAR), a Type II error"},
            {"id": "C", "text": "Crossover Error Rate (CER)"},
            {"id": "D", "text": "Failure to Enroll Rate (FER)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The False Acceptance Rate (FAR) - a Type II error - wrongly accepts an "
                       "unauthorized person, the worst outcome for security. The Crossover Error Rate "
                       "(CER/EER), where FAR equals FRR, is used to compare devices; a lower CER means a "
                       "more accurate system.",
            "distractors": {
                "A": "The FRR (Type I) wrongly rejects a legitimate user - an availability/usability nuisance, not an intrusion.",
                "C": "The CER is a comparison metric (where FAR=FRR), not an error event that admits an impostor.",
                "D": "The FER measures users who cannot enroll at all, not impostor acceptance.",
            },
            "exam_pattern": "FAR (Type II) = impostor accepted (worst for security); FRR (Type I) = valid user rejected; lower CER = better.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Biometric accuracy (FAR/FRR/CER)"],
    },
    {
        "id": "sscp-acc-r2-003", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_authn_methods", "difficulty": 3, "type": "mcq",
        "stem": "An authenticator app shows a 6-digit code that automatically changes every 30 seconds. "
                "Which one-time-password scheme is this, and what drives the code to change?",
        "options": [
            {"id": "A", "text": "HOTP - the code changes each time an event counter increments"},
            {"id": "B", "text": "WPS - the code is a static router PIN"},
            {"id": "C", "text": "CHAP - the code is a password-hash challenge"},
            {"id": "D", "text": "TOTP - the code is derived from the current time (a time step)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "TOTP (Time-based One-Time Password, RFC 6238) derives each code from a shared "
                       "secret and the current time divided into fixed steps (e.g., 30 seconds), so it "
                       "rotates automatically. HOTP (RFC 4226) is the counter/event-based variant.",
            "distractors": {
                "A": "HOTP is event/counter-based; it changes only when a counter advances, not on a timer.",
                "B": "WPS is a wireless setup method with a static PIN, not a rotating OTP.",
                "C": "CHAP is a challenge-response authentication protocol, not a rotating numeric token.",
            },
            "exam_pattern": "Rotates on a clock = TOTP (RFC 6238, time-based); rotates on a counter = HOTP (RFC 4226, event-based).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - One-time passwords (TOTP/HOTP)"],
    },
    {
        "id": "sscp-acc-r2-004", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_authn_methods", "difficulty": 3, "type": "mcq",
        "stem": "In Kerberos, after a user has obtained a Ticket-Granting Ticket (TGT), what does the "
                "client present to the Ticket-Granting Service (TGS) to gain access to a specific "
                "application server?",
        "options": [
            {"id": "A", "text": "The TGT, to request a service ticket for that resource"},
            {"id": "B", "text": "The user's cleartext password"},
            {"id": "C", "text": "A certificate revocation list"},
            {"id": "D", "text": "The application server's private key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The client presents its TGT to the TGS, which issues a service (session) ticket "
                       "for the specific resource. The user authenticates once to the Authentication "
                       "Server to obtain the TGT, then reuses it with the TGS - the basis of single "
                       "sign-on.",
            "distractors": {
                "B": "The password is never sent to the TGS; the TGT is exactly what avoids re-entering credentials.",
                "C": "A CRL is a PKI revocation construct and has no role in Kerberos ticketing.",
                "D": "The client never possesses the server's private key.",
            },
            "exam_pattern": "AS issues the TGT once; the client shows the TGT to the TGS to get per-service tickets (SSO).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Kerberos ticketing (TGT/TGS)"],
    },

    # ----- sscp_trust_architectures -----------------------------------
    {
        "id": "sscp-acc-r2-005", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_trust_architectures", "difficulty": 2, "type": "mcq",
        "stem": "In federated identity, which party AUTHENTICATES the user and issues the "
                "assertion/token that a separate application relies on to grant access?",
        "options": [
            {"id": "A", "text": "The Service Provider (SP) / relying party"},
            {"id": "B", "text": "The certificate revocation responder"},
            {"id": "C", "text": "The Identity Provider (IdP)"},
            {"id": "D", "text": "The DHCP server"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Identity Provider (IdP) authenticates the user and issues the "
                       "assertion/token; the Service Provider (SP, or relying party) consumes that "
                       "assertion to grant access without re-authenticating the user itself.",
            "distractors": {
                "A": "The SP/relying party trusts and consumes the assertion; it does not authenticate the user.",
                "B": "A revocation responder reports certificate status in PKI, not a federation role.",
                "D": "DHCP assigns IP addresses and has no identity-federation function.",
            },
            "exam_pattern": "IdP authenticates and asserts; SP/relying party trusts the assertion and grants access.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Federation (IdP vs SP)"],
    },
    {
        "id": "sscp-acc-r2-006", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_trust_architectures", "difficulty": 3, "type": "mcq",
        "stem": "What BEST distinguishes identity federation from ordinary single sign-on (SSO)?",
        "options": [
            {"id": "A", "text": "Federation and SSO are the same thing with different names"},
            {"id": "B", "text": "Federation extends trusted authentication ACROSS different organizations or security domains, while SSO typically lets a user reach many systems WITHIN one organization after a single login"},
            {"id": "C", "text": "SSO works only between separate companies, while federation works only inside one company"},
            {"id": "D", "text": "Federation requires sharing each user's password with every application"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SSO lets a user authenticate once and reach multiple applications within one "
                       "trust boundary/organization. Federation links identity across organizational or "
                       "domain boundaries so a user can use their home identity at a partner's services "
                       "(often via SAML/OIDC).",
            "distractors": {
                "A": "They are related but distinct - federation specifically spans separate trust domains.",
                "C": "This reverses the definitions; SSO is typically intra-organization and federation inter-organization.",
                "D": "Federation avoids sharing passwords by exchanging assertions/tokens, not credentials.",
            },
            "exam_pattern": "SSO = one login within a domain; federation = trusted identity across domains/organizations.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Federation vs single sign-on"],
    },

    # ----- sscp_identity_lifecycle ------------------------------------
    {
        "id": "sscp-acc-r2-007", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Periodically moving employees through different duties so that no one person "
                "indefinitely controls a sensitive function - and so irregularities surface when a new "
                "person takes over - is which control?",
        "options": [
            {"id": "A", "text": "Mandatory vacation"},
            {"id": "B", "text": "Least privilege"},
            {"id": "C", "text": "Single sign-on"},
            {"id": "D", "text": "Job rotation"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Job rotation cycles staff through roles; it cross-trains personnel and exposes "
                       "fraud or errors that a single long-term occupant could otherwise conceal.",
            "distractors": {
                "A": "Mandatory vacation forces time off to surface hidden misconduct but does not rotate duties.",
                "B": "Least privilege limits each user's access scope; it does not rotate assignments.",
                "C": "SSO is an authentication convenience, not a fraud-detection personnel control.",
            },
            "exam_pattern": "Rotate duties to detect/deter fraud and cross-train = job rotation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Personnel controls (job rotation)"],
    },
    {
        "id": "sscp-acc-r2-008", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A financial firm requires employees in sensitive positions to take at least five "
                "consecutive business days of leave each year, during which someone else performs their "
                "duties. What is the PRIMARY security purpose of this policy?",
        "options": [
            {"id": "A", "text": "To surface fraud or misuse that depends on the employee's continuous presence to stay hidden"},
            {"id": "B", "text": "To improve employee morale only"},
            {"id": "C", "text": "To reduce the company's payroll costs"},
            {"id": "D", "text": "To avoid the need for periodic access reviews"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mandatory vacation is a detective control: schemes that require constant hands-on "
                       "concealment (e.g., ongoing fraud) tend to be exposed when the perpetrator is away "
                       "and another person covers the role.",
            "distractors": {
                "B": "Morale may improve, but the security purpose is fraud detection.",
                "C": "It is not a cost-saving measure.",
                "D": "It complements, and does not replace, periodic access reviews.",
            },
            "exam_pattern": "Forced leave covered by someone else exposes continuity-dependent fraud = mandatory vacation (detective).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Personnel controls (mandatory vacation)"],
    },
    {
        "id": "sscp-acc-r2-009", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Which solution specifically secures highly privileged (administrator/root) accounts by "
                "vaulting their credentials, brokering check-out, enforcing just-in-time elevation, and "
                "recording privileged sessions?",
        "options": [
            {"id": "A", "text": "Mobile Device Management (MDM)"},
            {"id": "B", "text": "Data Loss Prevention (DLP)"},
            {"id": "C", "text": "Privileged Access Management (PAM)"},
            {"id": "D", "text": "Network Time Protocol (NTP)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Privileged Access Management (PAM) controls and monitors elevated accounts: it "
                       "stores admin credentials in a vault, grants time-limited/just-in-time access, and "
                       "records sessions to reduce the risk these powerful accounts pose.",
            "distractors": {
                "A": "MDM manages mobile devices, not privileged credentials.",
                "B": "DLP prevents data exfiltration.",
                "D": "NTP synchronizes clocks - none of these manages privileged access.",
            },
            "exam_pattern": "Vault + check-out + JIT elevation + session recording for admin accounts = PAM.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Privileged access management"],
    },
    {
        "id": "sscp-acc-r2-010", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Why are shared or generic accounts (for example, several admins all logging in as "
                "'admin') discouraged from a security standpoint?",
        "options": [
            {"id": "A", "text": "They make passwords easier to remember"},
            {"id": "B", "text": "They break individual accountability, so actions cannot be reliably traced to a specific person"},
            {"id": "C", "text": "They automatically enforce least privilege"},
            {"id": "D", "text": "They remove the need for logging"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Shared accounts destroy accountability: because multiple people use one identity, "
                       "audit logs cannot attribute an action to a specific individual, undermining "
                       "non-repudiation and investigations. Use a unique account per person.",
            "distractors": {
                "A": "Convenience is not a security benefit and does not justify the risk.",
                "C": "Shared accounts typically carry broad standing access, the opposite of least privilege.",
                "D": "Accountability makes logging more important, not less.",
            },
            "exam_pattern": "One identity per person preserves accountability; shared accounts break traceability.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Accountability (shared accounts)"],
    },

    # ----- sscp_access_control_models ---------------------------------
    {
        "id": "sscp-acc-r2-011", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_access_control_models", "difficulty": 2, "type": "mcq",
        "stem": "A firewall permits or denies traffic using global rules such as 'block all inbound "
                "Telnet' and 'allow web traffic only between 08:00 and 18:00,' applied uniformly "
                "regardless of the individual user. Which access control model is this?",
        "options": [
            {"id": "A", "text": "Discretionary Access Control (DAC)"},
            {"id": "B", "text": "Role-Based Access Control (RBAC)"},
            {"id": "C", "text": "Mandatory Access Control (MAC)"},
            {"id": "D", "text": "Rule-based access control (RuBAC)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Rule-based access control applies the same predefined rules/conditions (ports, "
                       "addresses, time-of-day) to all subjects; firewall ACLs are the classic example. "
                       "Decisions come from the rules, not from the specific user's identity or role.",
            "distractors": {
                "A": "DAC lets resource owners set per-object permissions at their discretion.",
                "B": "RBAC grants access by the user's job role, not global if-then rules.",
                "C": "MAC enforces access via classification labels and clearances.",
            },
            "exam_pattern": "Global if-condition-then-allow/deny rules applied to everyone (firewall, time limits) = rule-based (RuBAC).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Access control models (rule-based)"],
    },
    {
        "id": "sscp-acc-r2-012", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_access_control_models", "difficulty": 3, "type": "mcq",
        "stem": "An access control matrix can be stored by column or by row. An Access Control List (ACL) "
                "is the COLUMN view - bound to an object, listing which subjects may access it. What is "
                "the ROW view, bound to a subject and listing every object that subject may access?",
        "options": [
            {"id": "A", "text": "A capability list (capability table)"},
            {"id": "B", "text": "A certificate revocation list"},
            {"id": "C", "text": "A security classification label"},
            {"id": "D", "text": "A hash table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A capability list is the subject-centric (row) representation: for each subject "
                       "it enumerates the objects and rights that subject holds. An ACL is the "
                       "object-centric (column) representation.",
            "distractors": {
                "B": "A CRL lists revoked certificates in PKI, unrelated to the access matrix.",
                "C": "A security label marks an object's classification (MAC), not a subject's capability set.",
                "D": "A hash table is a generic data structure, not an access-matrix view.",
            },
            "exam_pattern": "ACL = per-object (column) list of who can access it; capability list = per-subject (row) list of what it can access.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Access control matrix (ACL vs capability)"],
    },
    {
        "id": "sscp-acc-r2-013", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_access_control_models", "difficulty": 3, "type": "mcq",
        "stem": "The Bell-LaPadula model protects CONFIDENTIALITY in multilevel systems. Which rule "
                "enforces 'no write down,' preventing a subject from writing data to a lower "
                "classification level?",
        "options": [
            {"id": "A", "text": "The Simple Security Property ('no read up')"},
            {"id": "B", "text": "The Simple Integrity Property ('no read down')"},
            {"id": "C", "text": "The Star (*) Security Property ('no write down')"},
            {"id": "D", "text": "The Star (*) Integrity Property ('no write up')"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Bell-LaPadula (confidentiality) has two main rules: the Simple Security Property "
                       "= no read up (cannot read a higher level), and the Star (*) Property = no write "
                       "down (cannot write to a lower level, which would leak sensitive data). The "
                       "integrity properties belong to the Biba model.",
            "distractors": {
                "A": "The Simple Security Property is 'no read up,' not the write rule.",
                "B": "'No read down' is a Biba (integrity) rule, not Bell-LaPadula.",
                "D": "'No write up' is a Biba (integrity) rule, not Bell-LaPadula.",
            },
            "exam_pattern": "Bell-LaPadula = confidentiality: no read up (simple), no write down (star). Biba = integrity.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Security models (Bell-LaPadula)"],
    },
    {
        "id": "sscp-acc-r2-014", "exam": "sscp", "domain": "sscp_access_controls",
        "subtopic": "sscp_access_control_models", "difficulty": 3, "type": "mcq",
        "stem": "The Biba model protects INTEGRITY. Which Biba rule prevents a low-integrity subject from "
                "writing to a higher-integrity object, so untrusted input cannot corrupt trusted data?",
        "options": [
            {"id": "A", "text": "The Simple Security Property ('no read up')"},
            {"id": "B", "text": "The Star (*) Security Property ('no write down')"},
            {"id": "C", "text": "Discretionary access control"},
            {"id": "D", "text": "The Star (*) Integrity Property ('no write up')"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Biba (integrity) uses the Star (*) Integrity Property = no write up (cannot write "
                       "to a higher integrity level) and the Simple Integrity Property = no read down. "
                       "This keeps low-integrity sources from corrupting high-integrity data. Biba is "
                       "effectively the inverse of Bell-LaPadula.",
            "distractors": {
                "A": "The Simple Security Property ('no read up') is a Bell-LaPadula confidentiality rule.",
                "B": "The Star (*) Security Property ('no write down') is a Bell-LaPadula confidentiality rule.",
                "C": "DAC is an access model, not a Biba integrity rule.",
            },
            "exam_pattern": "Biba integrity: no write up (star), no read down (simple) - the dual of Bell-LaPadula.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 2 - Security models (Biba)"],
    },

    # ===================================================================
    # Domain 3: Risk Identification, Monitoring, and Analysis
    #           (sscp-risk-r2-*)
    # ===================================================================

    # ----- sscp_risk_management ---------------------------------------
    {
        "id": "sscp-risk-r2-001", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A team rates risks on a High/Medium/Low matrix based on expert judgment of likelihood "
                "and impact, without assigning any dollar figures. Which type of risk analysis is this?",
        "options": [
            {"id": "A", "text": "Quantitative risk analysis"},
            {"id": "B", "text": "Qualitative risk analysis"},
            {"id": "C", "text": "Penetration testing"},
            {"id": "D", "text": "Business impact analysis"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Qualitative analysis uses subjective, descriptive ratings (High/Medium/Low, risk "
                       "matrices) based on judgment. Quantitative analysis assigns numeric/monetary "
                       "values (SLE, ARO, ALE).",
            "distractors": {
                "A": "Quantitative analysis would compute monetary values such as ALE, not High/Med/Low ratings.",
                "C": "A penetration test actively probes for exploitable weaknesses; it is not a rating method.",
                "D": "A BIA focuses on the impact of disruptions to business functions for continuity planning.",
            },
            "exam_pattern": "Subjective High/Med/Low ratings = qualitative; dollar values (SLE/ARO/ALE) = quantitative.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Qualitative vs quantitative risk analysis"],
    },
    {
        "id": "sscp-risk-r2-002", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "Senior leadership formally states the amount and type of risk the organization is willing "
                "to pursue or retain in order to meet its objectives. This statement is the "
                "organization's:",
        "options": [
            {"id": "A", "text": "Risk appetite"},
            {"id": "B", "text": "Residual risk"},
            {"id": "C", "text": "Single Loss Expectancy"},
            {"id": "D", "text": "Attack surface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk appetite is the broad level of risk leadership is willing to accept in "
                       "pursuit of objectives; it guides which risks to accept, mitigate, transfer, or "
                       "avoid. (Risk tolerance is the narrower acceptable variation around a specific "
                       "risk.)",
            "distractors": {
                "B": "Residual risk is what remains after controls are applied.",
                "C": "SLE is the monetary loss expected from a single incident.",
                "D": "The attack surface is the sum of exploitable entry points, not a risk-acceptance statement.",
            },
            "exam_pattern": "Leadership's overall willingness to accept risk = risk appetite; acceptable deviation on a specific risk = risk tolerance.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Risk appetite and tolerance"],
    },
    {
        "id": "sscp-risk-r2-003", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "A control costs $40,000 per year to operate. It reduces a risk's Annualized Loss "
                "Expectancy (ALE) from $100,000 to $30,000. From a cost-benefit standpoint, is the "
                "control justified?",
        "options": [
            {"id": "A", "text": "No - any control that costs money is never justified"},
            {"id": "B", "text": "No - because a control can never reduce ALE"},
            {"id": "C", "text": "Yes - it cuts ALE by $70,000 per year, which exceeds its $40,000 annual cost (net benefit about $30,000)"},
            {"id": "D", "text": "It cannot be evaluated without knowing the asset's color-coded label"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Value of a safeguard = ALE(before) - ALE(after) - annual cost of the control = "
                       "$100,000 - $30,000 - $40,000 = about $30,000 net benefit per year. Because the "
                       "loss reduction ($70,000) exceeds the control's cost ($40,000), it is "
                       "cost-justified. A control should generally not cost more than the loss it "
                       "prevents.",
            "distractors": {
                "A": "Controls are justified when their benefit exceeds their cost, as here.",
                "B": "Controls do reduce ALE by lowering likelihood or impact.",
                "D": "Cost-benefit depends on ALE and cost figures, not a color-coded label.",
            },
            "exam_pattern": "Safeguard value = ALE(before) - ALE(after) - annual control cost; justify when loss reduction > cost.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Safeguard cost-benefit analysis"],
    },
    {
        "id": "sscp-risk-r2-004", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After analysis shows a proposed online feature carries unacceptable legal risk, "
                "management decides not to build or offer the feature at all. Which risk treatment is "
                "this?",
        "options": [
            {"id": "A", "text": "Risk acceptance"},
            {"id": "B", "text": "Risk mitigation"},
            {"id": "C", "text": "Risk transference"},
            {"id": "D", "text": "Risk avoidance"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Risk avoidance eliminates the risk by not undertaking the risky activity - here, "
                       "cancelling the feature entirely so the exposure never exists.",
            "distractors": {
                "A": "Acceptance would proceed and knowingly retain the risk.",
                "B": "Mitigation would add controls to reduce likelihood/impact while still offering the feature.",
                "C": "Transference would shift the loss (e.g., insurance) while still doing the activity.",
            },
            "exam_pattern": "Don't do the risky activity at all = avoidance; add controls = mitigate; insure/outsource = transfer; do nothing = accept.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Risk treatment (avoidance)"],
    },

    # ----- sscp_monitoring_analysis -----------------------------------
    {
        "id": "sscp-risk-r2-005", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An IDS/antivirus engine detects threats by matching observed activity or files against a "
                "database of known-bad patterns. What is this detection method, and what is its main "
                "limitation?",
        "options": [
            {"id": "A", "text": "Signature-based detection - it cannot detect brand-new (zero-day) threats that have no existing signature"},
            {"id": "B", "text": "Anomaly-based detection - it cannot detect any known threats"},
            {"id": "C", "text": "Heuristic detection - it never produces false positives"},
            {"id": "D", "text": "Stateful inspection - it decrypts all traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Signature-based detection matches against known patterns; it is accurate and "
                       "low-noise for known threats but cannot catch novel/zero-day attacks that have no "
                       "signature yet. Anomaly-based detection complements it by flagging deviations from "
                       "a baseline.",
            "distractors": {
                "B": "That describes anomaly-based detection (good at novel threats, noisier), the opposite approach.",
                "C": "Heuristic detection does produce false positives; it is not error-free.",
                "D": "Stateful inspection tracks connection state in firewalls and does not inherently decrypt traffic.",
            },
            "exam_pattern": "Match to known patterns = signature-based (misses zero-days); deviation from baseline = anomaly-based (catches novel, more false positives).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Signature vs anomaly detection"],
    },
    {
        "id": "sscp-risk-r2-006", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability report lists each finding with a CVSS score. What does the CVSS score "
                "communicate?",
        "options": [
            {"id": "A", "text": "The unique catalog identifier for the specific vulnerability"},
            {"id": "B", "text": "A standardized severity rating (roughly 0 to 10) reflecting how serious/exploitable the vulnerability is"},
            {"id": "C", "text": "The exact dollar cost to remediate the vulnerability"},
            {"id": "D", "text": "The affected vendor's stock price"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Common Vulnerability Scoring System (CVSS) expresses vulnerability severity on "
                       "a 0.0-10.0 scale (higher = more severe), helping teams prioritize remediation. "
                       "The CVE identifier, by contrast, is the unique catalog ID for a specific "
                       "vulnerability.",
            "distractors": {
                "A": "That describes a CVE identifier, not the CVSS severity score.",
                "C": "CVSS measures severity, not remediation cost.",
                "D": "It has nothing to do with stock price.",
            },
            "exam_pattern": "CVSS = severity score 0-10 (prioritize by it); CVE = unique identifier for the vulnerability.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Vulnerability scoring (CVSS vs CVE)"],
    },
    {
        "id": "sscp-risk-r2-007", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An analyst wants to detect malicious activity by inspecting traffic flowing across a "
                "network segment, regardless of which host it targets. Which sensor placement is "
                "appropriate?",
        "options": [
            {"id": "A", "text": "A Host-based IDS (HIDS) installed on one workstation"},
            {"id": "B", "text": "A degausser on the switch"},
            {"id": "C", "text": "A Network-based IDS (NIDS) monitoring the segment"},
            {"id": "D", "text": "A Certificate Revocation List (CRL) on the router"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A NIDS monitors traffic on a network segment (via a SPAN/mirror port or tap), "
                       "seeing activity across many hosts. A HIDS runs on an individual host and sees "
                       "only that host's activity, files, and logs.",
            "distractors": {
                "A": "A HIDS is limited to the single host it is installed on, not the whole segment.",
                "B": "A degausser erases magnetic media and has no detection role.",
                "D": "A CRL is a PKI revocation list, not an intrusion-detection sensor.",
            },
            "exam_pattern": "Watch the network segment = NIDS; watch a single host (files/logs/processes) = HIDS.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - IDS placement (NIDS vs HIDS)"],
    },

    # ----- sscp_security_assessment -----------------------------------
    {
        "id": "sscp-risk-r2-008", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability scanner is given valid login credentials for the target systems before "
                "scanning. Compared with an unauthenticated scan, what is the main advantage of this "
                "credentialed (authenticated) scan?",
        "options": [
            {"id": "A", "text": "It is guaranteed to be completely undetectable"},
            {"id": "B", "text": "It removes the need to ever patch the systems"},
            {"id": "C", "text": "It only works against web applications"},
            {"id": "D", "text": "It sees installed patches, configuration, and local flaws from the inside, giving more accurate and complete results with fewer false positives"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A credentialed scan logs in and inspects the system from the inside - patch "
                       "levels, local configuration, installed software - yielding deeper, more accurate "
                       "findings and fewer false positives than an external, unauthenticated scan that "
                       "can only probe exposed surfaces.",
            "distractors": {
                "A": "Credentialed scans are not inherently stealthy; detectability is unrelated to the advantage.",
                "B": "Scanning finds flaws; it does not remove the need to remediate them.",
                "C": "Credentialed scanning applies broadly to hosts and systems, not only web apps.",
            },
            "exam_pattern": "Authenticated/credentialed scan = inside view (patches/config), deeper and fewer false positives than unauthenticated.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Credentialed vs non-credentialed scanning"],
    },
    {
        "id": "sscp-risk-r2-009", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 3, "type": "mcq",
        "stem": "Which application security testing approach analyzes the application's SOURCE CODE "
                "without executing it, allowing flaws to be found early in development?",
        "options": [
            {"id": "A", "text": "Static Application Security Testing (SAST)"},
            {"id": "B", "text": "Dynamic Application Security Testing (DAST)"},
            {"id": "C", "text": "A denial-of-service load test"},
            {"id": "D", "text": "Degaussing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SAST ('white-box') inspects source code, bytecode, or binaries without running "
                       "the application, so developers can catch issues early. DAST ('black-box') tests "
                       "the running application from the outside and finds runtime/configuration issues.",
            "distractors": {
                "B": "DAST executes and probes the running app from the outside; it does not analyze static source code.",
                "C": "A DoS/load test assesses availability under load, not code flaws.",
                "D": "Degaussing is a media-sanitization method, not application testing.",
            },
            "exam_pattern": "SAST = static, source code, no execution (early); DAST = dynamic, running app, black-box (runtime).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Application testing (SAST vs DAST)"],
    },
    {
        "id": "sscp-risk-r2-010", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 2, "type": "mcq",
        "stem": "Before any penetration test or vulnerability assessment begins, which step is ESSENTIAL "
                "to keep the testing lawful and within bounds?",
        "options": [
            {"id": "A", "text": "Immediately exploit any system reachable on the internet"},
            {"id": "B", "text": "Obtain written authorization defining the scope and rules of engagement from the asset owner"},
            {"id": "C", "text": "Delete the target's logs to avoid detection"},
            {"id": "D", "text": "Skip documentation to save time"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Testers must have explicit written authorization (scope, targets, timing, allowed "
                       "techniques - the rules of engagement) from the proper authority before starting. "
                       "Without it, the activity may be illegal and uncontrolled; the authorization also "
                       "protects the tester.",
            "distractors": {
                "A": "Attacking systems without authorization is illegal, regardless of reachability.",
                "C": "Destroying logs is tampering/anti-forensics and unethical.",
                "D": "Documentation is required for a defensible, repeatable assessment.",
            },
            "exam_pattern": "Always get written authorization + rules of engagement (scope) before testing - no scope, no test.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Assessment authorization and rules of engagement"],
    },

    # ----- sscp_siem_logging ------------------------------------------
    {
        "id": "sscp-risk-r2-011", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 2, "type": "mcq",
        "stem": "Network devices forward their event messages to a central collector using the syslog "
                "protocol. Over which transport and default port does classic syslog send these "
                "messages?",
        "options": [
            {"id": "A", "text": "TCP port 22"},
            {"id": "B", "text": "TCP port 443"},
            {"id": "C", "text": "UDP port 514"},
            {"id": "D", "text": "UDP port 53"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Traditional syslog uses UDP port 514 by default. Because UDP is connectionless "
                       "(no delivery guarantee), reliable deployments may use TCP, and syslog over TLS "
                       "uses TCP 6514 for confidentiality and integrity.",
            "distractors": {
                "A": "TCP 22 is SSH.",
                "B": "TCP 443 is HTTPS.",
                "D": "UDP 53 is DNS - none is the default syslog port.",
            },
            "exam_pattern": "Syslog default = UDP 514; syslog over TLS = TCP 6514.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Log transport (syslog UDP 514)"],
    },
    {
        "id": "sscp-risk-r2-012", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 3, "type": "mcq",
        "stem": "A SOC wants to automatically execute predefined response playbooks - enrich alerts, open "
                "tickets, and quarantine hosts - to reduce manual effort and speed reaction. Which "
                "technology is purpose-built for this orchestration and automation?",
        "options": [
            {"id": "A", "text": "A CRL distribution point"},
            {"id": "B", "text": "Network Time Protocol (NTP)"},
            {"id": "C", "text": "A KVM switch"},
            {"id": "D", "text": "SOAR (Security Orchestration, Automation, and Response)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SOAR platforms orchestrate tools and automate response via playbooks "
                       "(enrichment, ticketing, containment), reducing analyst workload and response "
                       "time. A SIEM detects/correlates; SOAR acts on those findings, often alongside the "
                       "SIEM.",
            "distractors": {
                "A": "A CRL distribution point serves certificate revocation data.",
                "B": "NTP synchronizes time.",
                "C": "A KVM switch shares a keyboard/monitor - none automates incident response.",
            },
            "exam_pattern": "Automated playbooks + tool orchestration for response = SOAR (works alongside the SIEM).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Security automation (SOAR)"],
    },
    {
        "id": "sscp-risk-r2-013", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 2, "type": "mcq",
        "stem": "An account-lockout rule triggers an alert only after five failed logins within ten "
                "minutes, so routine typos do not generate noise. The threshold of acceptable activity "
                "that must be exceeded before an alarm is raised is called the:",
        "options": [
            {"id": "A", "text": "Clipping level"},
            {"id": "B", "text": "Crossover error rate"},
            {"id": "C", "text": "Exposure factor"},
            {"id": "D", "text": "Recovery point objective"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A clipping level is a predefined threshold that must be crossed before an event "
                       "is flagged, filtering out normal/benign activity (e.g., a few failed logins) to "
                       "reduce noise while still catching abnormal patterns.",
            "distractors": {
                "B": "The crossover error rate is a biometric accuracy metric.",
                "C": "The exposure factor is the percentage of asset value lost in a single incident.",
                "D": "The RPO is a continuity metric for tolerable data loss.",
            },
            "exam_pattern": "Threshold that must be exceeded before alerting = clipping level (reduces noise).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Monitoring thresholds (clipping level)"],
    },
    {
        "id": "sscp-risk-r2-014", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 2, "type": "mcq",
        "stem": "To ensure collected security logs cannot be altered or deleted - even by an "
                "administrator or an attacker who gains access - an organization writes them to Write "
                "Once, Read Many (WORM) storage. Which log property does this primarily protect?",
        "options": [
            {"id": "A", "text": "Network bandwidth"},
            {"id": "B", "text": "Log integrity (tamper resistance)"},
            {"id": "C", "text": "Password complexity"},
            {"id": "D", "text": "CPU performance"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "WORM media allows data to be written once and thereafter only read, so records "
                       "cannot be modified or erased. This protects log integrity and preserves evidence, "
                       "defeating attempts to tamper with or wipe the audit trail.",
            "distractors": {
                "A": "WORM concerns immutability, not bandwidth.",
                "C": "It is unrelated to password policy.",
                "D": "It does not improve processing performance.",
            },
            "exam_pattern": "Immutable, append-only log storage (WORM) protects integrity/evidence against tampering.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Log integrity (WORM storage)"],
    },

    # ===================================================================
    # Domain 4: Incident Response and Recovery (sscp-ir-r2-*)
    # ===================================================================

    # ----- sscp_incident_handling -------------------------------------
    {
        "id": "sscp-ir-r2-001", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 3, "type": "mcq",
        "stem": "NIST SP 800-61 describes the incident response life cycle in four phases. Which phase "
                "groups together the hands-on work of stopping the spread, removing the threat, and "
                "restoring systems?",
        "options": [
            {"id": "A", "text": "Preparation"},
            {"id": "B", "text": "Detection and Analysis"},
            {"id": "C", "text": "Containment, Eradication, and Recovery"},
            {"id": "D", "text": "Post-Incident Activity"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "NIST SP 800-61 uses four phases: Preparation; Detection and Analysis; "
                       "Containment, Eradication, and Recovery (combined into one phase); and "
                       "Post-Incident Activity. The third phase bundles the active response steps that "
                       "other models often list separately.",
            "distractors": {
                "A": "Preparation is the readiness phase before an incident.",
                "B": "Detection and Analysis is identifying and scoping the incident.",
                "D": "Post-Incident Activity is the lessons-learned review after recovery.",
            },
            "exam_pattern": "NIST 800-61 four phases: Preparation -> Detection & Analysis -> Containment/Eradication/Recovery -> Post-Incident Activity.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Incident response life cycle (NIST SP 800-61)"],
    },
    {
        "id": "sscp-ir-r2-002", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 2, "type": "mcq",
        "stem": "After eradicating malware, the team returns cleaned systems to production, confirms they "
                "function normally, and heightens monitoring to watch for any signs of reinfection. "
                "Which incident response activity is this?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Recovery"},
            {"id": "C", "text": "Detection"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Recovery restores systems to normal operation, validates they are clean and "
                       "functioning, and increases monitoring to ensure the threat does not return before "
                       "standing down.",
            "distractors": {
                "A": "Containment earlier limited the spread; it does not restore service.",
                "C": "Detection identified the incident; it does not restore systems.",
                "D": "Preparation is pre-incident readiness.",
            },
            "exam_pattern": "Restore to production + validate + watch for recurrence = recovery.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Recovery phase"],
    },
    {
        "id": "sscp-ir-r2-003", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 2, "type": "mcq",
        "stem": "A SOC receives dozens of alerts at once. Before committing resources, responders assess "
                "and rank them by factors such as business impact and scope so the most serious are "
                "handled first. This prioritization step is called:",
        "options": [
            {"id": "A", "text": "Triage (incident prioritization)"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Chain of custody"},
            {"id": "D", "text": "Degaussing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Triage categorizes and prioritizes incidents by impact, urgency, and scope so "
                       "limited resources address the highest-severity events first. It is part of "
                       "detection and analysis.",
            "distractors": {
                "B": "Eradication removes the threat after containment.",
                "C": "Chain of custody tracks evidence handling, not alert prioritization.",
                "D": "Degaussing is a media-sanitization method.",
            },
            "exam_pattern": "Rank incidents by impact/scope to handle the worst first = triage/prioritization.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Incident triage"],
    },
    {
        "id": "sscp-ir-r2-004", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_incident_handling", "difficulty": 3, "type": "mcq",
        "stem": "During an intrusion, responders first quickly disconnect the affected server from the "
                "network to stop active damage, then later rebuild it on a clean, hardened replacement "
                "before returning it to service. The initial disconnect versus the later clean rebuild "
                "illustrate which pair of strategies?",
        "options": [
            {"id": "A", "text": "Eradication followed by preparation"},
            {"id": "B", "text": "Recovery followed by detection"},
            {"id": "C", "text": "Deterrence followed by avoidance"},
            {"id": "D", "text": "Short-term containment followed by long-term containment"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Short-term containment takes immediate action to limit damage (isolate/"
                       "disconnect), while long-term containment applies more durable measures (clean "
                       "rebuilds, hardened replacements, temporary fixes) that let operations continue "
                       "safely until full eradication and recovery.",
            "distractors": {
                "A": "Both steps are containment actions, not eradication then preparation.",
                "B": "The order and phases do not match recovery-then-detection.",
                "C": "Deterrence and avoidance are not containment strategies.",
            },
            "exam_pattern": "Immediate isolate = short-term containment; durable clean-rebuild/hardening = long-term containment.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Containment strategies"],
    },

    # ----- sscp_forensics ---------------------------------------------
    {
        "id": "sscp-ir-r2-005", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 3, "type": "mcq",
        "stem": "NIST SP 800-86 defines the forensic process as four steps. Which sequence is correct?",
        "options": [
            {"id": "A", "text": "Collection -> Examination -> Analysis -> Reporting"},
            {"id": "B", "text": "Analysis -> Collection -> Reporting -> Examination"},
            {"id": "C", "text": "Reporting -> Analysis -> Examination -> Collection"},
            {"id": "D", "text": "Examination -> Reporting -> Collection -> Analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NIST SP 800-86 orders the process: Collection (acquire data from sources), "
                       "Examination (process and extract relevant data, often filtering large volumes), "
                       "Analysis (derive findings using sound methods), and Reporting (document results "
                       "and actions).",
            "distractors": {
                "B": "You must first collect data before analyzing it; this order is scrambled.",
                "C": "Reporting is last, not first; collection comes first.",
                "D": "Examination cannot precede collection, and reporting is the final step.",
            },
            "exam_pattern": "NIST 800-86 forensics: Collection -> Examination -> Analysis -> Reporting.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Forensic process (NIST SP 800-86)"],
    },
    {
        "id": "sscp-ir-r2-006", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 2, "type": "mcq",
        "stem": "Following the order of volatility (RFC 3227), which of these evidence sources is the "
                "LEAST volatile and therefore typically collected LAST?",
        "options": [
            {"id": "A", "text": "CPU registers and cache"},
            {"id": "B", "text": "System RAM (running memory)"},
            {"id": "C", "text": "Backup tapes and archival media"},
            {"id": "D", "text": "The ARP cache and routing table"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The order of volatility collects the most volatile data first and the most stable "
                       "last. Backup tapes and archival media persist offline for long periods, so they "
                       "are gathered last; registers/cache and RAM are collected first because they "
                       "vanish on power loss.",
            "distractors": {
                "A": "CPU registers/cache are the MOST volatile and are collected first.",
                "B": "RAM is highly volatile and collected early.",
                "D": "The ARP cache and routing table are volatile network state collected before disk and archival media.",
            },
            "exam_pattern": "Most volatile first (registers/cache -> RAM -> network state -> disk); least volatile last (archival/backup media).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Order of volatility (RFC 3227)"],
    },
    {
        "id": "sscp-ir-r2-007", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 3, "type": "mcq",
        "stem": "A responder arrives at a running, compromised workstation that likely holds malware "
                "active only in memory. Why is capturing a live memory image BEFORE powering the system "
                "down often critical?",
        "options": [
            {"id": "A", "text": "Because powering down speeds up the investigation"},
            {"id": "B", "text": "Because volatile RAM (running processes, encryption keys, network connections, in-memory malware) is lost when power is removed"},
            {"id": "C", "text": "Because disk data disappears at shutdown"},
            {"id": "D", "text": "Because hashing is impossible on a running system"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RAM is volatile: running processes, open network connections, decrypted keys, and "
                       "fileless/in-memory malware disappear when the machine loses power. A live "
                       "acquisition captures this evidence first; a 'dead' (static) acquisition images "
                       "the powered-off disk afterward.",
            "distractors": {
                "A": "Rushing to power down destroys volatile evidence; speed is not the priority.",
                "C": "Disk (non-volatile) data persists across shutdown - it is RAM that is lost.",
                "D": "Hashing is still used to verify images; it is not the reason to capture memory.",
            },
            "exam_pattern": "Capture volatile RAM live before shutdown (processes/keys/in-memory malware vanish on power loss); image the disk dead afterward.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Live vs static acquisition"],
    },
    {
        "id": "sscp-ir-r2-008", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 3, "type": "mcq",
        "stem": "A forensic examiner recovers fragments of a deleted file from areas the operating system "
                "reports as empty or unused. The techniques that reconstruct such data from unallocated "
                "clusters and file slack are collectively known as:",
        "options": [
            {"id": "A", "text": "Degaussing"},
            {"id": "B", "text": "Key stretching"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "File carving / recovery from unallocated and slack space"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Deleting a file usually just removes its directory pointer; the underlying data "
                       "remains in unallocated space (and in file slack) until overwritten. File carving "
                       "reconstructs files from these remnants by recognizing file structures/headers.",
            "distractors": {
                "A": "Degaussing erases magnetic media, destroying such evidence.",
                "B": "Key stretching slows password hashing.",
                "C": "Load balancing distributes traffic - none recovers deleted data.",
            },
            "exam_pattern": "Deleted data lingers in unallocated space and file slack; reconstruct it via file carving.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Data recovery (unallocated/slack space)"],
    },
    {
        "id": "sscp-ir-r2-009", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_forensics", "difficulty": 2, "type": "mcq",
        "stem": "When litigation is anticipated, an organization must suspend routine deletion and "
                "preserve potentially relevant data. Improperly destroying evidence that should have been "
                "kept is known as:",
        "options": [
            {"id": "A", "text": "Spoliation (and the preservation duty is a legal hold)"},
            {"id": "B", "text": "Degaussing"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A legal hold suspends normal data-destruction schedules to preserve relevant "
                       "evidence once litigation is reasonably anticipated. Spoliation is the improper "
                       "destruction or alteration of such evidence, which can bring legal sanctions.",
            "distractors": {
                "B": "Degaussing is a sanitization technique, not a legal concept.",
                "C": "Load balancing is a network function.",
                "D": "Non-repudiation is a security service proving origin, not evidence preservation.",
            },
            "exam_pattern": "Preserve evidence under a legal hold; destroying it improperly = spoliation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Legal hold and spoliation"],
    },

    # ----- sscp_bcp_dr ------------------------------------------------
    {
        "id": "sscp-ir-r2-010", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "A backup scheme runs a full backup each Sunday and, on each weekday, backs up everything "
                "changed SINCE THE LAST FULL backup (without clearing the archive bit). To fully restore "
                "after a Thursday failure, which backups are needed?",
        "options": [
            {"id": "A", "text": "The Sunday full plus every weekday backup, in order"},
            {"id": "B", "text": "The Sunday full backup plus Thursday's differential backup only"},
            {"id": "C", "text": "Only Thursday's backup"},
            {"id": "D", "text": "Only the Sunday full backup"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "This is a differential scheme: each differential captures all changes since the "
                       "last full and does not clear the archive bit, so differentials grow over the "
                       "week. Restoration needs just the last full plus the most recent (Thursday) "
                       "differential - fast to restore, larger/slower to back up each day.",
            "distractors": {
                "A": "Needing every weekday backup describes an incremental scheme (changes since the last backup of any kind).",
                "C": "Thursday's differential alone lacks the unchanged baseline data from the full backup.",
                "D": "The full alone omits the week's changes.",
            },
            "exam_pattern": "Differential = since last full; restore = full + last differential (fast restore). Incremental = since last backup; restore = full + all incrementals.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Backup strategies (differential)"],
    },
    {
        "id": "sscp-ir-r2-011", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "Which alternate recovery site is the LEAST expensive to maintain but takes the LONGEST "
                "to bring online, because it provides only space, power, and environmental controls - no "
                "installed hardware or current data?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Mirrored site"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A cold site is just the facility (space, power, HVAC, connectivity). Hardware, "
                       "software, and data must be brought in and configured during a disaster, so it is "
                       "the cheapest to keep but slowest (days to weeks) to activate.",
            "distractors": {
                "A": "A hot site is fully equipped with near-live data for rapid failover (most expensive).",
                "B": "A warm site has some hardware/connectivity and needs hours to days to stand up.",
                "D": "A mirrored site is a fully redundant real-time duplicate, the fastest and costliest.",
            },
            "exam_pattern": "Cold = space/power only (cheap, slow); warm = partial; hot = ready with current data (fast, costly).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - Recovery site types (cold site)"],
    },
    {
        "id": "sscp-ir-r2-012", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "A DR team wants to validate recovery by actually bringing the alternate systems fully "
                "online and processing real workloads alongside production, WITHOUT shutting production "
                "down. Which test type is this?",
        "options": [
            {"id": "A", "text": "Full-interruption test"},
            {"id": "B", "text": "Checklist (read-through) review"},
            {"id": "C", "text": "Tabletop (walkthrough) exercise"},
            {"id": "D", "text": "Parallel test"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A parallel test runs the recovery systems live in parallel with production "
                       "(processing real transactions) to prove they work, while production keeps running "
                       "- more thorough than paper reviews but lower risk than a full interruption.",
            "distractors": {
                "A": "A full-interruption test actually shuts down production and fails over - most realistic but highest risk.",
                "B": "A checklist review only verifies documentation on paper.",
                "C": "A tabletop walks the team through the plan in discussion, without running systems.",
            },
            "exam_pattern": "Testing rigor/risk: checklist < tabletop/walkthrough < simulation < parallel (run alongside prod) < full-interruption (take prod down).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - DR plan testing"],
    },
    {
        "id": "sscp-ir-r2-013", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "A server uses RAID 5 across its disks. An administrator claims this means the data no "
                "longer needs to be backed up. Why is that claim WRONG?",
        "options": [
            {"id": "A", "text": "RAID 5 cannot survive any disk failure, so it is useless"},
            {"id": "B", "text": "RAID 5 provides fault tolerance/availability (surviving one disk failure via distributed parity), but it does not protect against deletion, corruption, ransomware, or site loss - backups still do"},
            {"id": "C", "text": "RAID 5 encrypts data, which replaces backups"},
            {"id": "D", "text": "RAID 5 automatically copies data to an offsite vault"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RAID 5 (block-level striping with distributed parity across 3+ disks) survives a "
                       "single drive failure, improving availability. But it does not guard against "
                       "accidental deletion, logical corruption, malware/ransomware, or disaster at the "
                       "site - RAID is not a backup. Independent backups are still required.",
            "distractors": {
                "A": "RAID 5 does survive one disk failure via parity - that is its purpose.",
                "C": "RAID 5 does not encrypt data.",
                "D": "RAID 5 is local redundancy, not offsite replication.",
            },
            "exam_pattern": "RAID = availability/fault tolerance, NOT a backup; you still need independent, offsite backups.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - RAID vs backup"],
    },
    {
        "id": "sscp-ir-r2-014", "exam": "sscp", "domain": "sscp_incident_response",
        "subtopic": "sscp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "How do a Business Continuity Plan (BCP) and a Disaster Recovery Plan (DRP) differ in "
                "scope?",
        "options": [
            {"id": "A", "text": "The BCP is the broad plan to keep the whole business operating during/after a disruption; the DRP is the narrower, IT-focused plan to restore systems and technology"},
            {"id": "B", "text": "They are identical documents with different titles"},
            {"id": "C", "text": "The DRP covers the whole business; the BCP covers only payroll"},
            {"id": "D", "text": "The BCP applies only to cyberattacks; the DRP applies only to fires"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The BCP is enterprise-wide: it keeps critical business functions running (people, "
                       "processes, facilities, communications) through a disruption. The DRP is a subset "
                       "focused on recovering IT systems, data, and infrastructure, and it supports the "
                       "broader BCP.",
            "distractors": {
                "B": "They are related but distinct in scope and focus.",
                "C": "This reverses their scope; the BCP is the broad business plan.",
                "D": "Neither is limited to a single hazard type.",
            },
            "exam_pattern": "BCP = keep the whole business running (broad); DRP = restore IT/technology (a subset of the BCP).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 4 - BCP vs DRP"],
    },

    # ===================================================================
    # Domain 5: Cryptography (sscp-crypto-r2-*)
    # ===================================================================

    # ----- sscp_crypto_concepts ---------------------------------------
    {
        "id": "sscp-crypto-r2-001", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 3, "type": "mcq",
        "stem": "An image encrypted with a block cipher in ECB (Electronic Codebook) mode still reveals "
                "the outline of the original picture. Why does ECB leak this pattern information?",
        "options": [
            {"id": "A", "text": "ECB encrypts each block with a different random key"},
            {"id": "B", "text": "Identical plaintext blocks always encrypt to identical ciphertext blocks, so repeating patterns remain visible"},
            {"id": "C", "text": "ECB adds a unique initialization vector to every block"},
            {"id": "D", "text": "ECB compresses the data, which exposes the image"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ECB encrypts each block independently with the same key, so equal plaintext "
                       "blocks produce equal ciphertext blocks. Repetition in the plaintext (like large "
                       "same-color regions) survives into the ciphertext, leaking structure. Use chaining "
                       "or counter modes (CBC, CTR) or authenticated modes (GCM) with an IV/nonce "
                       "instead.",
            "distractors": {
                "A": "ECB uses one key for all blocks, not a different random key per block.",
                "C": "ECB uses no IV - that lack is exactly the problem; CBC/CTR/GCM add one.",
                "D": "ECB does not compress data.",
            },
            "exam_pattern": "ECB: same plaintext block -> same ciphertext block (pattern leakage). Prefer CBC/CTR/GCM with an IV/nonce.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Block cipher modes (ECB weakness)"],
    },
    {
        "id": "sscp-crypto-r2-002", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 3, "type": "multi",
        "stem": "A system must store user passwords so that even if the hash database is stolen, the "
                "passwords resist rainbow-table precomputation and brute-force cracking. Which TWO "
                "techniques directly address this? (Choose two.)",
        "options": [
            {"id": "A", "text": "Add a unique random salt to each password before hashing"},
            {"id": "B", "text": "Use a deliberately slow key-stretching function (e.g., PBKDF2, bcrypt, scrypt, or Argon2)"},
            {"id": "C", "text": "Encrypt the passwords with ECB mode"},
            {"id": "D", "text": "Store the passwords using a fast, unsalted MD5 hash"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A unique per-user salt makes precomputed/rainbow tables useless (every hash "
                       "differs even for identical passwords) and forces attackers to attack each hash "
                       "separately. Key stretching (PBKDF2/bcrypt/scrypt/Argon2) makes each guess "
                       "computationally expensive, slowing brute force. Together they greatly strengthen "
                       "stored-password protection.",
            "distractors": {
                "C": "ECB is a block-cipher mode for encryption (and it leaks patterns); it is not how password hashes are protected.",
                "D": "A fast, unsalted MD5 is exactly what enables rainbow-table and rapid brute-force attacks.",
            },
            "exam_pattern": "Protect stored passwords with a unique salt (defeats rainbow tables) + slow key stretching (bcrypt/PBKDF2/Argon2).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Password storage (salting and key stretching)"],
    },
    {
        "id": "sscp-crypto-r2-003", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about hashing algorithms reflects current security guidance?",
        "options": [
            {"id": "A", "text": "MD5 is the most collision-resistant algorithm available"},
            {"id": "B", "text": "SHA-1 is preferred over SHA-256 for digital signatures"},
            {"id": "C", "text": "MD5 and SHA-1 are deprecated for security use because practical collisions have been demonstrated; use SHA-2 or SHA-3"},
            {"id": "D", "text": "A hash provides confidentiality by encrypting its input"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MD5 and SHA-1 are broken for security purposes - researchers have produced "
                       "practical collisions (two inputs with the same digest), so they must not be used "
                       "where collision resistance matters (signatures, certificates). SHA-2 (e.g., "
                       "SHA-256) and SHA-3 are the current recommendations.",
            "distractors": {
                "A": "MD5 is badly broken, not the most collision-resistant.",
                "B": "SHA-1 is weaker than SHA-256 and is being removed from signature use.",
                "D": "Hashing is one-way integrity, not encryption - it provides no confidentiality.",
            },
            "exam_pattern": "MD5/SHA-1 = collision-broken (avoid); use SHA-2/SHA-3. Hashing = integrity, not confidentiality.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Hash algorithm strength (SHA-2/SHA-3)"],
    },
    {
        "id": "sscp-crypto-r2-004", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_crypto_concepts", "difficulty": 3, "type": "mcq",
        "stem": "A protocol uses AES in GCM (Galois/Counter Mode) so each message is both encrypted and "
                "accompanied by an authentication tag. What does this authenticated encryption (AEAD) "
                "mode provide that a plain confidentiality-only mode does not?",
        "options": [
            {"id": "A", "text": "Non-repudiation via the sender's private key"},
            {"id": "B", "text": "A way to recover a lost symmetric key"},
            {"id": "C", "text": "Faster key exchange over an untrusted channel"},
            {"id": "D", "text": "Integrity and authenticity of the ciphertext in addition to confidentiality, so tampering is detected"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Authenticated encryption with associated data (AEAD) modes like AES-GCM provide "
                       "confidentiality AND built-in integrity/authenticity: the authentication tag lets "
                       "the receiver detect any modification of the ciphertext. A confidentiality-only "
                       "mode (e.g., CBC without a separate MAC) would not detect tampering by itself.",
            "distractors": {
                "A": "Non-repudiation requires an asymmetric digital signature, not a symmetric AEAD tag (both parties share the key).",
                "B": "AEAD does not recover lost keys.",
                "C": "AEAD encrypts and authenticates data; it does not perform key exchange.",
            },
            "exam_pattern": "AES-GCM/AEAD = confidentiality + integrity/authenticity (tamper detection) in one; symmetric, so not non-repudiation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Authenticated encryption (AES-GCM/AEAD)"],
    },

    # ----- sscp_pki ---------------------------------------------------
    {
        "id": "sscp-crypto-r2-005", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 2, "type": "mcq",
        "stem": "To obtain a TLS certificate, a server administrator generates a key pair and sends the "
                "Certificate Authority a Certificate Signing Request (CSR). What does the CSR contain, "
                "and what is kept private?",
        "options": [
            {"id": "A", "text": "The CSR contains the subject's PUBLIC key and identifying details; the matching PRIVATE key stays on the server and is never sent to the CA"},
            {"id": "B", "text": "The CSR contains the server's private key, which the CA copies"},
            {"id": "C", "text": "The CSR contains the CA's root private key"},
            {"id": "D", "text": "The CSR contains the symmetric session key for TLS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CSR carries the subject's public key plus identity information (e.g., common "
                       "name/SAN, organization), signed by the requester's private key to prove "
                       "possession. The CA validates it and issues a certificate binding that public key "
                       "to the identity. The private key never leaves the server.",
            "distractors": {
                "B": "The private key is never placed in a CSR or shared with the CA.",
                "C": "The CA's root private key is not part of a subject's CSR.",
                "D": "TLS session keys are negotiated per connection, not contained in a CSR.",
            },
            "exam_pattern": "CSR = public key + identity (private key stays with the requester); the CA signs it into a certificate.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Certificate signing request (CSR)"],
    },
    {
        "id": "sscp-crypto-r2-006", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_pki", "difficulty": 3, "type": "mcq",
        "stem": "In a well-designed PKI, the root CA is often kept OFFLINE and used only to sign a small "
                "number of intermediate (subordinate) CA certificates, which in turn issue end-entity "
                "certificates. What is the main security reason for this design?",
        "options": [
            {"id": "A", "text": "It makes certificates expire faster"},
            {"id": "B", "text": "If an issuing (intermediate) CA is compromised, only its branch must be revoked/replaced, while the highly trusted root key stays protected offline"},
            {"id": "C", "text": "It removes the need for certificate revocation"},
            {"id": "D", "text": "It lets end users sign their own root certificates"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Protecting the root is paramount because every trust chain anchors to it. Keeping "
                       "the root offline shrinks its exposure; day-to-day issuance is delegated to "
                       "intermediate CAs. If an intermediate is compromised, you revoke/replace that "
                       "intermediate without having to redistribute a new root to every client.",
            "distractors": {
                "A": "An offline root does not change certificate validity periods.",
                "C": "Revocation (CRL/OCSP) is still required for issued certificates.",
                "D": "End users do not sign root certificates; that would break the trust model.",
            },
            "exam_pattern": "Keep the root CA offline and issue via intermediates, so a compromise is contained to one branch, not the trust anchor.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - CA hierarchy (offline root and intermediates)"],
    },

    # ----- sscp_key_management ----------------------------------------
    {
        "id": "sscp-crypto-r2-007", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 3, "type": "mcq",
        "stem": "In a purely symmetric system where every pair of users needs its own unique shared key, "
                "how many keys are required for 10 users, and what does this illustrate?",
        "options": [
            {"id": "A", "text": "10 keys - symmetric key management scales linearly"},
            {"id": "B", "text": "100 keys - one key per user squared"},
            {"id": "C", "text": "45 keys - symmetric key distribution scales poorly as users grow, per n(n-1)/2"},
            {"id": "D", "text": "5 keys - one key is shared across everyone"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The number of pairwise symmetric keys is n(n-1)/2 = 10*9/2 = 45. This quadratic "
                       "growth is the key-management/scaling problem of symmetric cryptography, which "
                       "asymmetric key exchange (and PKI) helps solve.",
            "distractors": {
                "A": "Growth is quadratic, not linear; each new user adds many key pairs.",
                "B": "n squared (100) over-counts by double-counting pairs and including self-pairs.",
                "D": "A single shared key for everyone destroys confidentiality between individual pairs.",
            },
            "exam_pattern": "Pairwise symmetric keys = n(n-1)/2 (quadratic); asymmetric/PKI solves the key-distribution scaling problem.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Symmetric key scaling (n(n-1)/2)"],
    },
    {
        "id": "sscp-crypto-r2-008", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 3, "type": "mcq",
        "stem": "A TLS configuration uses ephemeral Diffie-Hellman (DHE/ECDHE) to negotiate a fresh key "
                "for every session. What security property does this provide?",
        "options": [
            {"id": "A", "text": "It eliminates the need for any server certificate"},
            {"id": "B", "text": "It makes all sessions share one static key for efficiency"},
            {"id": "C", "text": "It provides non-repudiation of the data"},
            {"id": "D", "text": "Perfect forward secrecy - later compromise of the server's long-term private key does not let an attacker decrypt previously recorded sessions"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Ephemeral keys are generated per session and discarded afterward, so each "
                       "session's secret is independent of the server's long-term key. Perfect forward "
                       "secrecy (PFS) means that even if the long-term private key is later stolen, "
                       "earlier recorded sessions remain protected.",
            "distractors": {
                "A": "A certificate is still needed to authenticate the server; ephemeral DH handles key agreement, not authentication.",
                "B": "PFS specifically avoids a shared static key - each session is unique.",
                "C": "Non-repudiation comes from digital signatures, not from key agreement.",
            },
            "exam_pattern": "Ephemeral DH (DHE/ECDHE) -> per-session keys -> perfect forward secrecy (past traffic safe if the long-term key leaks).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Perfect forward secrecy (ephemeral DH)"],
    },
    {
        "id": "sscp-crypto-r2-009", "exam": "sscp", "domain": "sscp_cryptography",
        "subtopic": "sscp_key_management", "difficulty": 2, "type": "mcq",
        "stem": "TLS and many secure systems combine asymmetric and symmetric cryptography: an asymmetric "
                "algorithm exchanges or protects a randomly generated symmetric key, which then encrypts "
                "the bulk data. Why use this hybrid approach?",
        "options": [
            {"id": "A", "text": "It combines asymmetric's easy key exchange with symmetric's speed for bulk encryption - the best of both"},
            {"id": "B", "text": "Because symmetric algorithms cannot encrypt data at all"},
            {"id": "C", "text": "Because asymmetric algorithms are faster than symmetric for large data"},
            {"id": "D", "text": "To avoid ever needing a symmetric key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hybrid cryptosystem uses slow asymmetric cryptography only to securely exchange "
                       "or wrap a symmetric session key, then uses fast symmetric encryption (e.g., AES) "
                       "for the actual data. This solves symmetric key distribution while keeping bulk "
                       "encryption efficient.",
            "distractors": {
                "B": "Symmetric algorithms are excellent at bulk encryption - that is why they handle the data.",
                "C": "Asymmetric operations are much slower than symmetric for large data, which is why symmetric does the bulk work.",
                "D": "The hybrid approach specifically relies on a symmetric session key.",
            },
            "exam_pattern": "Hybrid: asymmetric exchanges the symmetric session key; symmetric (AES) encrypts the bulk data (fast).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 5 - Hybrid cryptosystems"],
    },

    # ===================================================================
    # Domain 6: Network and Communications Security (sscp-net-r2-*)
    # ===================================================================

    # ----- sscp_network_models ----------------------------------------
    {
        "id": "sscp-net-r2-001", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 1, "type": "mcq",
        "stem": "An administrator must remotely manage a router's command line over an untrusted network. "
                "Which protocol provides an ENCRYPTED session that should replace Telnet, and on which "
                "default port?",
        "options": [
            {"id": "A", "text": "Telnet on TCP port 23"},
            {"id": "B", "text": "SSH on TCP port 22"},
            {"id": "C", "text": "HTTP on TCP port 80"},
            {"id": "D", "text": "SNMPv1 on UDP port 161"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SSH (Secure Shell) encrypts the management session - credentials and commands - "
                       "and listens on TCP 22. Telnet (TCP 23) sends everything in cleartext and must not "
                       "be used over untrusted networks.",
            "distractors": {
                "A": "Telnet is the insecure cleartext protocol being replaced, not the secure option.",
                "C": "HTTP is unencrypted web traffic, not a secure CLI.",
                "D": "SNMPv1 is an unencrypted management protocol, not a secure remote shell.",
            },
            "exam_pattern": "Encrypted remote CLI = SSH (TCP 22); cleartext = Telnet (TCP 23, avoid).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Secure protocols (SSH vs Telnet)"],
    },
    {
        "id": "sscp-net-r2-002", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 2, "type": "mcq",
        "stem": "Which port and transport does DNS primarily use, and when does it switch transport?",
        "options": [
            {"id": "A", "text": "Port 25 - TCP only"},
            {"id": "B", "text": "Port 443 - UDP only"},
            {"id": "C", "text": "Port 53 - UDP for ordinary name queries, switching to TCP for large responses and zone transfers"},
            {"id": "D", "text": "Port 161 - UDP for zone transfers"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DNS uses port 53. Standard lookups use UDP 53 (fast, low overhead); DNS falls "
                       "back to TCP 53 for responses too large for UDP and for zone transfers between "
                       "servers (AXFR).",
            "distractors": {
                "A": "Port 25 is SMTP, not DNS.",
                "B": "Port 443 is HTTPS, not DNS.",
                "D": "Port 161 is SNMP; DNS zone transfers use TCP 53, not UDP 161.",
            },
            "exam_pattern": "DNS = port 53: UDP for queries, TCP for zone transfers / large responses.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Ports and protocols (DNS 53)"],
    },
    {
        "id": "sscp-net-r2-003", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 2, "type": "mcq",
        "stem": "Which exchange correctly describes the TCP three-way handshake that establishes a "
                "connection?",
        "options": [
            {"id": "A", "text": "SYN -> SYN/ACK -> ACK"},
            {"id": "B", "text": "ACK -> SYN -> FIN"},
            {"id": "C", "text": "SYN -> FIN -> RST"},
            {"id": "D", "text": "PSH -> URG -> SYN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TCP opens a connection with SYN (client), SYN/ACK (server), ACK (client). This "
                       "synchronizes sequence numbers before data flows. A SYN flood abuses this by "
                       "sending many SYNs and never completing the handshake.",
            "distractors": {
                "B": "This uses the wrong flags/order; FIN is for closing, not opening.",
                "C": "FIN closes and RST resets a connection; neither opens one.",
                "D": "PSH and URG are data-flag controls, not part of the open handshake.",
            },
            "exam_pattern": "TCP open = SYN, SYN/ACK, ACK (three-way handshake).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - TCP three-way handshake"],
    },
    {
        "id": "sscp-net-r2-004", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 3, "type": "mcq",
        "stem": "A team needs encrypted file transfer. Which statement correctly distinguishes SFTP from "
                "FTPS?",
        "options": [
            {"id": "A", "text": "SFTP and FTPS are both just plaintext FTP"},
            {"id": "B", "text": "SFTP is FTP over TLS; FTPS is FTP over SSH"},
            {"id": "C", "text": "Neither provides any encryption"},
            {"id": "D", "text": "SFTP runs file transfer over an SSH connection (typically TCP 22); FTPS is traditional FTP wrapped in TLS/SSL"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SFTP (SSH File Transfer Protocol) tunnels file operations inside an SSH session, "
                       "usually on TCP 22. FTPS adds a TLS/SSL layer to the classic FTP protocol. Both "
                       "encrypt data, but they are different protocols - and neither is plain FTP (ports "
                       "20/21, cleartext).",
            "distractors": {
                "A": "Both SFTP and FTPS are encrypted, unlike plain FTP.",
                "B": "This reverses them: SFTP uses SSH, FTPS uses TLS.",
                "C": "Both do provide encryption.",
            },
            "exam_pattern": "SFTP = file transfer over SSH (22); FTPS = FTP over TLS; plain FTP (20/21) = cleartext.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Secure file transfer (SFTP vs FTPS)"],
    },

    # ----- sscp_network_attacks ---------------------------------------
    {
        "id": "sscp-net-r2-005", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "An attacker floods a switch with a huge number of frames bearing bogus source MAC "
                "addresses until the switch's MAC address table (CAM table) fills up. What happens, and "
                "which feature defends against it?",
        "options": [
            {"id": "A", "text": "The switch automatically encrypts all traffic; no defense is needed"},
            {"id": "B", "text": "The switch fails open and floods frames out all ports like a hub, letting the attacker sniff traffic; port security (limiting MACs per port) stops it"},
            {"id": "C", "text": "The switch powers off permanently; only a degausser helps"},
            {"id": "D", "text": "The attacker gains the router's private key; OCSP stops it"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "When the CAM table overflows, many switches 'fail open,' flooding "
                       "unknown-destination frames out every port (like a hub), which lets the attacker "
                       "capture traffic on the segment. Port security (limiting/locking the MAC addresses "
                       "allowed per port) mitigates MAC flooding.",
            "distractors": {
                "A": "Switches do not auto-encrypt traffic; the attack succeeds without a defense.",
                "C": "The switch does not permanently power off, and degaussing is unrelated.",
                "D": "No private key is exposed, and OCSP is a PKI revocation service.",
            },
            "exam_pattern": "CAM table overflow -> switch floods like a hub (sniffing); defend with port security (MAC limits).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - MAC flooding / CAM table overflow"],
    },
    {
        "id": "sscp-net-r2-006", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "In a VLAN double-tagging attack, a frame is crafted with two 802.1Q tags so it reaches a "
                "VLAN the attacker should not access. Which condition does the attack exploit, and how is "
                "it mitigated?",
        "options": [
            {"id": "A", "text": "It exploits the trunk's native VLAN (sent untagged); mitigate by using a dedicated, unused native VLAN and/or tagging the native VLAN, and keeping hosts off VLAN 1"},
            {"id": "B", "text": "It exploits WPA2 encryption; mitigate by switching to WEP"},
            {"id": "C", "text": "It exploits OCSP; mitigate with a CRL"},
            {"id": "D", "text": "It exploits DNS caching; mitigate with DNSSEC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Double-tagging abuses the native VLAN: the first (outer) tag matches the native "
                       "VLAN and is stripped by the first switch, leaving the inner tag to steer the "
                       "frame into the victim VLAN. It is typically one-way (blind). Mitigations: set the "
                       "native VLAN to an unused ID, avoid using VLAN 1 for hosts, and force tagging of "
                       "the native VLAN.",
            "distractors": {
                "B": "The attack is a Layer 2 VLAN issue, unrelated to Wi-Fi encryption (and WEP is insecure).",
                "C": "OCSP/CRL are PKI revocation mechanisms, unrelated to 802.1Q tagging.",
                "D": "DNS caching/DNSSEC concern name resolution, not VLAN tagging.",
            },
            "exam_pattern": "VLAN double-tagging exploits the untagged native VLAN (one-way); fix with a dedicated/tagged native VLAN and keep hosts off VLAN 1.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - VLAN hopping (double-tagging)"],
    },
    {
        "id": "sscp-net-r2-007", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "An attacker sends small requests with a SPOOFED source IP (the victim's) to open DNS or "
                "NTP servers, which then send much larger replies to the victim, overwhelming it. What "
                "class of DDoS is this?",
        "options": [
            {"id": "A", "text": "A SQL injection attack"},
            {"id": "B", "text": "An ARP poisoning attack"},
            {"id": "C", "text": "A reflection/amplification attack"},
            {"id": "D", "text": "A cross-site scripting (XSS) attack"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reflection uses third-party servers to bounce traffic at a spoofed victim; "
                       "amplification picks services whose responses are far larger than the requests "
                       "(DNS, NTP, memcached), multiplying the flood. It is a volumetric DDoS technique.",
            "distractors": {
                "A": "SQL injection manipulates database queries, not a traffic flood.",
                "B": "ARP poisoning redirects LAN traffic for interception, not volumetric DoS.",
                "D": "XSS injects script into web pages, unrelated to amplification.",
            },
            "exam_pattern": "Spoofed small request -> large reply from reflectors aimed at the victim = reflection/amplification DDoS.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - DDoS (reflection/amplification)"],
    },
    {
        "id": "sscp-net-r2-008", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sends a stream of TCP SYN packets but never completes the handshake with the "
                "final ACK, exhausting the server's table of half-open connections so legitimate clients "
                "cannot connect. Which attack is this, and a common defense?",
        "options": [
            {"id": "A", "text": "A man-in-the-middle; defense is HTTPS"},
            {"id": "B", "text": "A phishing attack; defense is awareness training"},
            {"id": "C", "text": "A brute-force password attack; defense is account lockout"},
            {"id": "D", "text": "A SYN flood; defenses include SYN cookies and connection rate limiting"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A SYN flood abuses the TCP three-way handshake by leaving many connections "
                       "half-open, consuming the backlog so real users are denied service. SYN cookies "
                       "(which avoid allocating state until the handshake completes) and rate limiting "
                       "mitigate it.",
            "distractors": {
                "A": "A MITM intercepts traffic rather than exhausting connection state.",
                "B": "Phishing targets people, not the TCP backlog.",
                "C": "A brute-force attack guesses credentials, a different goal.",
            },
            "exam_pattern": "Half-open TCP connections exhausting the backlog = SYN flood; defend with SYN cookies / rate limiting.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - SYN flood"],
    },

    # ----- sscp_network_defense ---------------------------------------
    {
        "id": "sscp-net-r2-009", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "Which capability distinguishes a Next-Generation Firewall (NGFW) from a traditional "
                "stateful firewall?",
        "options": [
            {"id": "A", "text": "It only filters by source/destination IP and port, with no awareness of applications"},
            {"id": "B", "text": "It inspects traffic at the application layer (deep packet inspection), identifies specific applications/users, and integrates IPS and threat intelligence"},
            {"id": "C", "text": "It is simply a Layer 2 switch"},
            {"id": "D", "text": "It replaces the need for any encryption"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An NGFW adds application awareness and deep packet inspection, user/identity-based "
                       "policy, integrated intrusion prevention, and threat intelligence on top of "
                       "stateful filtering, so it can allow/deny specific applications rather than just "
                       "ports.",
            "distractors": {
                "A": "Filtering only by IP/port describes a traditional stateful/stateless firewall, not an NGFW.",
                "C": "An NGFW is a security control, not a basic switch.",
                "D": "Firewalls do not replace encryption; they are complementary controls.",
            },
            "exam_pattern": "NGFW = stateful + application awareness/DPI + user identity + integrated IPS/threat intel.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Next-generation firewalls"],
    },
    {
        "id": "sscp-net-r2-010", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 3, "type": "mcq",
        "stem": "A device sits in front of INTERNAL CLIENTS, forwarding their outbound web requests so "
                "the organization can filter content, cache pages, and hide client addresses. Which type "
                "of proxy is this?",
        "options": [
            {"id": "A", "text": "A forward proxy"},
            {"id": "B", "text": "A reverse proxy"},
            {"id": "C", "text": "A honeypot"},
            {"id": "D", "text": "A load-balancing switch backplane"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A forward proxy represents the clients: it mediates their outbound requests, "
                       "enabling content filtering, caching, and client anonymity/egress control. A "
                       "reverse proxy represents servers - it sits in front of internal servers to handle "
                       "inbound requests (load balancing, TLS offload, hiding the back end).",
            "distractors": {
                "B": "A reverse proxy faces inbound traffic to protect/serve back-end servers - the opposite placement.",
                "C": "A honeypot is a decoy to attract attackers, not a request mediator.",
                "D": "A switch backplane is hardware, not a proxy.",
            },
            "exam_pattern": "Forward proxy = in front of clients (egress filtering/caching/anonymity); reverse proxy = in front of servers (inbound).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Proxies (forward vs reverse)"],
    },
    {
        "id": "sscp-net-r2-011", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "Where should an organization place its public-facing web and mail servers so that "
                "Internet users can reach them without being allowed directly into the internal LAN?",
        "options": [
            {"id": "A", "text": "On the same flat subnet as all internal workstations"},
            {"id": "B", "text": "Inside the domain controller's memory"},
            {"id": "C", "text": "In a DMZ (screened subnet) isolated between the Internet and the internal network by firewall rules"},
            {"id": "D", "text": "On the attacker's host"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A DMZ (demilitarized zone / screened subnet) is a buffer network for "
                       "Internet-facing services. Firewall policy lets outside users reach the DMZ hosts "
                       "but blocks direct access from the DMZ into the trusted internal LAN, so a "
                       "compromised public server does not immediately expose internal systems.",
            "distractors": {
                "A": "Putting public servers on the internal subnet lets a compromise pivot straight into internal systems.",
                "B": "Servers are not placed 'in memory' of a domain controller.",
                "D": "This is not a meaningful placement.",
            },
            "exam_pattern": "Public-facing servers go in a DMZ/screened subnet - reachable from outside, isolated from the internal LAN.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Network architecture (DMZ/screened subnet)"],
    },
    {
        "id": "sscp-net-r2-012", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 3, "type": "mcq",
        "stem": "Within IPsec, which statement about the AH and ESP protocols is correct?",
        "options": [
            {"id": "A", "text": "AH (protocol 50) encrypts the payload; ESP (protocol 51) only authenticates"},
            {"id": "B", "text": "Both AH and ESP provide only confidentiality, never integrity"},
            {"id": "C", "text": "AH and ESP are wireless encryption standards like WPA2"},
            {"id": "D", "text": "AH (IP protocol 51) provides integrity and authentication but no encryption; ESP (IP protocol 50) provides confidentiality (encryption) plus integrity/authentication"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Authentication Header (AH) is IP protocol 51 and provides data integrity, origin "
                       "authentication, and anti-replay, but NO encryption (so it offers no "
                       "confidentiality and breaks under NAT). Encapsulating Security Payload (ESP) is IP "
                       "protocol 50 and provides confidentiality via encryption plus "
                       "integrity/authentication - it is the one that actually encrypts the payload.",
            "distractors": {
                "A": "The numbers and roles are swapped: AH is 51 (no encryption), ESP is 50 (encrypts).",
                "B": "ESP (and AH) do provide integrity - the claim is false.",
                "C": "AH/ESP are IPsec protocols, not Wi-Fi standards.",
            },
            "exam_pattern": "IPsec: AH = proto 51, integrity/auth only (no encryption); ESP = proto 50, confidentiality + integrity/auth.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - IPsec (AH vs ESP)"],
    },

    # ----- sscp_wireless_cellular -------------------------------------
    {
        "id": "sscp-net-r2-013", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 3, "type": "mcq",
        "stem": "WPA2 (IEEE 802.11i) mandates a stronger encryption protocol than the original WPA. Which "
                "cipher/protocol does WPA2 require, and what did WPA rely on?",
        "options": [
            {"id": "A", "text": "WPA2 requires WEP; WPA required AES"},
            {"id": "B", "text": "WPA2 requires CCMP, which is based on the AES block cipher; WPA relied on TKIP, which uses the RC4 stream cipher"},
            {"id": "C", "text": "WPA2 requires RC4; WPA required CCMP"},
            {"id": "D", "text": "Both WPA and WPA2 use DES in ECB mode"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "WPA2 mandates CCMP (Counter Mode with CBC-MAC Protocol), built on AES, providing "
                       "strong confidentiality and integrity. The original WPA used TKIP (a patch over "
                       "WEP-era hardware) based on the RC4 stream cipher, now deprecated. WPA3 goes "
                       "further with SAE.",
            "distractors": {
                "A": "WEP is the obsolete original standard, not WPA2's cipher; this is reversed.",
                "C": "RC4 is TKIP/WEP's weak cipher; CCMP (AES) is WPA2's.",
                "D": "Neither WPA nor WPA2 uses DES-ECB.",
            },
            "exam_pattern": "WPA2 = CCMP/AES (mandatory); WPA = TKIP/RC4 (deprecated); WPA3 = SAE.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Wireless encryption (WPA2 CCMP/AES)"],
    },
    {
        "id": "sscp-net-r2-014", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 3, "type": "mcq",
        "stem": "In a WPA2/WPA3-Enterprise deployment, which EAP method provides the strongest "
                "authentication by requiring BOTH a server certificate and a client certificate for "
                "mutual authentication?",
        "options": [
            {"id": "A", "text": "EAP-TLS"},
            {"id": "B", "text": "Pre-shared key (PSK)"},
            {"id": "C", "text": "Open authentication"},
            {"id": "D", "text": "WPS PIN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EAP-TLS uses mutual certificate-based authentication: both the server and the "
                       "client present X.509 certificates, so neither a stolen password nor a rogue "
                       "server alone succeeds. It requires a PKI to issue client certificates, which is "
                       "its main operational cost. (PEAP/EAP-TTLS use only a server certificate plus a "
                       "tunneled password.)",
            "distractors": {
                "B": "A PSK is a single shared passphrase (WPA2-Personal), not per-user certificate authentication.",
                "C": "Open authentication provides no authentication at all.",
                "D": "A WPS PIN is a weak setup method vulnerable to brute force.",
            },
            "exam_pattern": "Mutual certificate auth (client + server certs) via PKI = EAP-TLS (strongest EAP).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Enterprise wireless (EAP-TLS)"],
    },
    {
        "id": "sscp-net-r2-015", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sets up a rogue access point broadcasting the same SSID as a legitimate "
                "corporate or coffee-shop network, hoping users connect to it so their traffic can be "
                "intercepted. What is this attack called?",
        "options": [
            {"id": "A", "text": "ARP poisoning"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Evil twin (rogue access point)"},
            {"id": "D", "text": "Degaussing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An evil twin is a rogue AP impersonating a legitimate SSID to lure clients into "
                       "connecting, enabling eavesdropping or credential capture (a wireless "
                       "man-in-the-middle). Defenses include 802.1X/EAP-TLS mutual authentication, "
                       "verifying networks, and using a VPN on untrusted Wi-Fi.",
            "distractors": {
                "A": "ARP poisoning is a wired-LAN Layer 2 interception technique, not a fake Wi-Fi AP.",
                "B": "SQL injection targets databases.",
                "D": "Degaussing erases magnetic media.",
            },
            "exam_pattern": "Fake AP mimicking a real SSID to capture traffic = evil twin / rogue AP (wireless MITM).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Wireless attacks (evil twin)"],
    },

    # ===================================================================
    # Domain 7: Systems and Application Security (sscp-sys-r2-*)
    # ===================================================================

    # ----- sscp_malware_endpoint --------------------------------------
    {
        "id": "sscp-sys-r2-001", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 3, "type": "mcq",
        "stem": "Which type of malware is specifically designed to gain and hide privileged (often "
                "kernel-level) access, concealing its own files, processes, and network activity from the "
                "operating system and standard tools?",
        "options": [
            {"id": "A", "text": "Adware"},
            {"id": "B", "text": "Ransomware"},
            {"id": "C", "text": "Rootkit"},
            {"id": "D", "text": "A macro virus"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A rootkit embeds deep in the system (sometimes the kernel or boot process) to "
                       "maintain stealthy privileged access and hides its presence by subverting OS "
                       "calls. Because it hides from the running OS, reliable detection often needs "
                       "offline/boot-time scanning, and full remediation may require reimaging.",
            "distractors": {
                "A": "Adware displays ads and is not primarily stealthy or privileged.",
                "B": "Ransomware encrypts data for extortion - overt, not hidden.",
                "D": "A macro virus spreads via document macros and is not defined by kernel-level stealth.",
            },
            "exam_pattern": "Stealthy, privileged, hides itself (often kernel-level) = rootkit; detect offline, often reimage.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Malware (rootkits)"],
    },
    {
        "id": "sscp-sys-r2-002", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "A disgruntled developer inserts code into an application that lies dormant until a "
                "specific date, at which point it deletes critical files. Which type of malicious code is "
                "this?",
        "options": [
            {"id": "A", "text": "Logic bomb"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Rootkit"},
            {"id": "D", "text": "Keylogger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A logic bomb is malicious code that stays inert until a trigger condition is met "
                       "(a date/time, an event, or a specific circumstance), then executes its payload. "
                       "Insider threats commonly plant them.",
            "distractors": {
                "B": "A worm self-replicates across networks; it is not defined by a trigger condition.",
                "C": "A rootkit hides privileged access rather than firing on a condition.",
                "D": "A keylogger captures keystrokes; it is not a condition-triggered payload by definition.",
            },
            "exam_pattern": "Dormant code that fires on a date/condition = logic bomb (often an insider).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Malware (logic bombs)"],
    },
    {
        "id": "sscp-sys-r2-003", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 3, "type": "mcq",
        "stem": "An attack runs entirely in memory by abusing built-in, trusted tools like PowerShell and "
                "WMI, writing little or nothing to disk. Why is this 'fileless' / living-off-the-land "
                "technique effective at evading traditional antivirus?",
        "options": [
            {"id": "A", "text": "It can only be stopped by degaussing the drive"},
            {"id": "B", "text": "There is no malicious file on disk to match against signatures, so defense relies on behavioral monitoring (EDR), logging, and least privilege"},
            {"id": "C", "text": "Signature antivirus always detects in-memory code easily"},
            {"id": "D", "text": "It requires the user to physically insert a USB key every time"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Fileless/living-off-the-land attacks execute in memory using legitimate system "
                       "binaries (LOLBins) and scripting, leaving few file artifacts for signature-based "
                       "AV to scan. Detection shifts to behavioral analytics (EDR), command-line/script "
                       "logging, and restricting scripting and privileges.",
            "distractors": {
                "A": "Degaussing erases media and is irrelevant to in-memory execution.",
                "C": "Signature AV struggles precisely because there is no on-disk file to match.",
                "D": "Fileless attacks do not depend on physical USB insertion.",
            },
            "exam_pattern": "In-memory abuse of PowerShell/WMI (LOLBins) = fileless; evades signatures, caught by behavior/EDR + logging.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Fileless / living-off-the-land malware"],
    },
    {
        "id": "sscp-sys-r2-004", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_malware_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "As part of hardening a server, an administrator removes unneeded software, disables "
                "unused services and ports, and deletes default accounts. Which security principle does "
                "this follow?",
        "options": [
            {"id": "A", "text": "Separation of duties"},
            {"id": "B", "text": "Non-repudiation"},
            {"id": "C", "text": "Maximum availability of all features"},
            {"id": "D", "text": "Least functionality (reduce the attack surface to only what is required)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Least functionality means a system runs only the services, software, and ports "
                       "needed for its purpose. Disabling or removing everything else shrinks the attack "
                       "surface and the number of potential vulnerabilities.",
            "distractors": {
                "A": "Separation of duties splits sensitive tasks among people, unrelated to disabling services.",
                "B": "Non-repudiation proves an action's origin.",
                "C": "Leaving all features enabled increases, not decreases, risk.",
            },
            "exam_pattern": "Run only what is needed; disable/remove the rest = least functionality (attack-surface reduction).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - System hardening (least functionality)"],
    },

    # ----- sscp_cloud_security ----------------------------------------
    {
        "id": "sscp-sys-r2-005", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 2, "type": "mcq",
        "stem": "Several hospitals jointly build and share a cloud environment tailored to their common "
                "regulatory and security requirements, available only to those organizations. Which "
                "cloud DEPLOYMENT model is this?",
        "options": [
            {"id": "A", "text": "Public cloud"},
            {"id": "B", "text": "Community cloud"},
            {"id": "C", "text": "Private cloud (single-tenant)"},
            {"id": "D", "text": "Standalone on-premises hosting"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A community cloud is shared by several organizations with common concerns "
                       "(mission, compliance, security), who pool and share the infrastructure. A public "
                       "cloud is open to any tenant; a private cloud serves one organization; "
                       "on-premises is not shared cloud infrastructure.",
            "distractors": {
                "A": "A public cloud is multi-tenant and open to the general public, not restricted to a specific group.",
                "C": "A private cloud is dedicated to a single organization.",
                "D": "On-premises hosting is not a shared cloud model.",
            },
            "exam_pattern": "Shared by several orgs with common needs = community cloud; one org = private; open to all = public; mix = hybrid.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud deployment models (community)"],
    },
    {
        "id": "sscp-sys-r2-006", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 3, "type": "mcq",
        "stem": "In a public (multi-tenant) cloud, multiple customers' workloads share the same "
                "underlying physical hardware. Which security concern does this multitenancy introduce?",
        "options": [
            {"id": "A", "text": "The risk that weak logical isolation could let one tenant access or affect another tenant's data (data commingling / isolation failure / 'noisy neighbor')"},
            {"id": "B", "text": "That tenants must share one administrator password"},
            {"id": "C", "text": "That encryption becomes impossible"},
            {"id": "D", "text": "That the Internet is no longer required"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multitenancy relies on logical isolation (hypervisors, network segmentation, "
                       "access controls) to keep tenants separate on shared hardware. If that isolation "
                       "is weak or flawed (e.g., a hypervisor vulnerability or misconfiguration), one "
                       "tenant could potentially access another's data or degrade their performance "
                       "(noisy neighbor).",
            "distractors": {
                "B": "Tenants have separate accounts and do not share one admin password.",
                "C": "Encryption is still fully possible and is a key tenant control.",
                "D": "Cloud services still require network/Internet connectivity.",
            },
            "exam_pattern": "Multitenancy = shared hardware with logical isolation; the risk is isolation failure / data commingling between tenants.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud multitenancy isolation"],
    },
    {
        "id": "sscp-sys-r2-007", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 2, "type": "mcq",
        "stem": "A frequent cause of cloud data breaches is a storage bucket left publicly accessible "
                "with sensitive data. Under the shared responsibility model, whose mistake is this, and "
                "what is the fix?",
        "options": [
            {"id": "A", "text": "The cloud provider's hardware failure; fix it by replacing disks"},
            {"id": "B", "text": "The ISP's routing error; fix it by changing DNS"},
            {"id": "C", "text": "The customer's misconfiguration; fix it by correcting access policies and enforcing least privilege / blocking public access"},
            {"id": "D", "text": "Nobody's - public buckets are always safe"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Access configuration of cloud storage is the customer's responsibility. Public "
                       "exposure stems from customer-set permissions, so the remedy is to correct the "
                       "bucket/IAM policies, apply least privilege, and enable 'block public access' "
                       "controls - not anything the provider patches.",
            "distractors": {
                "A": "This is a configuration error, not provider hardware failure.",
                "B": "It is not an ISP/DNS issue.",
                "D": "Exposing sensitive data publicly is a serious, common breach cause, not safe.",
            },
            "exam_pattern": "Misconfigured public cloud storage = customer responsibility; fix with least-privilege access policies / block public access.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud misconfiguration (storage exposure)"],
    },
    {
        "id": "sscp-sys-r2-008", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_cloud_security", "difficulty": 3, "type": "mcq",
        "stem": "In a Platform as a Service (PaaS) model, which split of responsibility is correct?",
        "options": [
            {"id": "A", "text": "The customer must patch the hypervisor and the physical hosts"},
            {"id": "B", "text": "The provider writes and secures the customer's application code"},
            {"id": "C", "text": "Neither party is responsible for the data"},
            {"id": "D", "text": "The provider manages the underlying OS, runtime, and middleware; the customer is responsible for their application code, configuration, and data"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "In PaaS the provider maintains and secures the platform stack (hardware, OS, "
                       "runtime, middleware), while the customer is responsible for the application they "
                       "deploy - its code, configuration, access, and data. (In IaaS the customer also "
                       "owns the guest OS; in SaaS the provider manages the app and the customer mainly "
                       "owns data and access.)",
            "distractors": {
                "A": "The provider patches the hypervisor and physical hosts in all cloud models.",
                "B": "The customer, not the provider, develops and secures their own application code.",
                "C": "The customer always remains responsible for their data.",
            },
            "exam_pattern": "PaaS: provider owns OS/runtime/middleware; customer owns app code/config/data.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Cloud shared responsibility (PaaS)"],
    },

    # ----- sscp_virtualization_security -------------------------------
    {
        "id": "sscp-sys-r2-009", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "How does a container (e.g., Docker) differ from a traditional virtual machine in terms "
                "of isolation?",
        "options": [
            {"id": "A", "text": "Containers share the host's OS kernel (OS-level virtualization), making them lightweight but giving a weaker isolation boundary than full VMs, which each run their own guest OS on a hypervisor"},
            {"id": "B", "text": "Containers each run a full separate guest OS, so they are heavier than VMs"},
            {"id": "C", "text": "Containers provide stronger hardware-level isolation than VMs"},
            {"id": "D", "text": "Containers and VMs are identical in every respect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Containers virtualize at the OS level and share the host kernel, so they start "
                       "fast and use fewer resources - but because they share the kernel, a kernel "
                       "exploit can affect the host and sibling containers, a weaker boundary than a VM's "
                       "hypervisor-enforced separation with its own guest OS.",
            "distractors": {
                "B": "Containers do NOT each run a full guest OS - that is a VM; containers are lighter.",
                "C": "Sharing the host kernel gives weaker, not stronger, isolation than VMs.",
                "D": "They differ materially in architecture and isolation.",
            },
            "exam_pattern": "Containers share the host kernel (light, weaker isolation); VMs run separate guest OSes on a hypervisor (heavier, stronger isolation).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Containers vs virtual machines"],
    },
    {
        "id": "sscp-sys-r2-010", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "Why is the hypervisor considered an especially critical component to patch and protect "
                "in a virtualized environment?",
        "options": [
            {"id": "A", "text": "The hypervisor stores the only copy of each VM's backups"},
            {"id": "B", "text": "Compromise of the hypervisor can expose or control every guest VM running on that host, collapsing the isolation all the VMs depend on"},
            {"id": "C", "text": "The hypervisor is the only component that never needs updates"},
            {"id": "D", "text": "Hypervisors cannot be attacked at all"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The hypervisor is the trusted layer that isolates and mediates all guest VMs. If "
                       "an attacker compromises it (or escapes a guest into it), they can potentially "
                       "access, alter, or control every VM on the host - so hardening and prompt patching "
                       "of the hypervisor are essential.",
            "distractors": {
                "A": "The hypervisor is not a backup store.",
                "C": "It requires security updates like any software.",
                "D": "Hypervisors can and do have vulnerabilities (e.g., enabling VM escape).",
            },
            "exam_pattern": "Hypervisor compromise = all guest VMs at risk (isolation collapses); harden and patch it as a priority.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Hypervisor security"],
    },
    {
        "id": "sscp-sys-r2-011", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_virtualization_security", "difficulty": 3, "type": "mcq",
        "stem": "A team routinely reverts VMs to older snapshots. Which security risk does rolling back "
                "to a snapshot introduce?",
        "options": [
            {"id": "A", "text": "It permanently encrypts the VM"},
            {"id": "B", "text": "It guarantees the VM is fully patched"},
            {"id": "C", "text": "It can reintroduce previously patched vulnerabilities and undo security changes, and snapshots may also store sensitive data (e.g., keys) that must be protected"},
            {"id": "D", "text": "It upgrades the hypervisor automatically"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reverting to an earlier snapshot can roll a VM back to a state before patches, "
                       "configuration hardening, or credential changes were applied - silently reopening "
                       "known vulnerabilities. Snapshots can also capture memory/disk contents (including "
                       "secrets), so they must be access-controlled and managed.",
            "distractors": {
                "A": "Reverting a snapshot does not encrypt the VM.",
                "B": "It can do the opposite - revert to an unpatched state.",
                "D": "It does not upgrade the hypervisor.",
            },
            "exam_pattern": "Snapshot rollback can reintroduce patched vulns / undo hardening; snapshots may hold secrets - manage and protect them.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - VM snapshot risks"],
    },

    # ----- sscp_mobile_iot_security -----------------------------------
    {
        "id": "sscp-sys-r2-012", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 3, "type": "mcq",
        "stem": "On employee-owned (BYOD) phones, a company wants to manage only its corporate apps and "
                "data - deploying them, applying policy, and wiping them if needed - WITHOUT taking "
                "control of the entire personal device. Which approach fits best?",
        "options": [
            {"id": "A", "text": "Full-device Mobile Device Management (MDM) enrollment of the whole phone"},
            {"id": "B", "text": "Degaussing the phone"},
            {"id": "C", "text": "Disabling the corporate VPN"},
            {"id": "D", "text": "Mobile Application Management (MAM)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "MAM governs specific managed apps and their data (deployment, policy, and "
                       "selective wipe of corporate content) without controlling the whole device - a "
                       "better fit for BYOD privacy than full MDM enrollment, which manages the entire "
                       "device.",
            "distractors": {
                "A": "Full MDM manages the entire personal device, which users often resist on BYOD and which raises privacy concerns.",
                "B": "Degaussing applies to magnetic media, not smartphones.",
                "C": "Disabling the VPN reduces security and does not manage apps.",
            },
            "exam_pattern": "Manage only corporate apps/data on BYOD = MAM; manage the whole device = MDM.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Mobile management (MAM vs MDM)"],
    },
    {
        "id": "sscp-sys-r2-013", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 2, "type": "mcq",
        "stem": "Why does jailbreaking (iOS) or rooting (Android) a mobile device create a significant "
                "security risk for enterprise data on that device?",
        "options": [
            {"id": "A", "text": "It removes the vendor's built-in security controls and app sandboxing, letting untrusted code run with elevated privileges and potentially bypassing MDM protections"},
            {"id": "B", "text": "It automatically encrypts all corporate data more strongly"},
            {"id": "C", "text": "It is required in order to enroll in MDM"},
            {"id": "D", "text": "It has no effect on security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Rooting/jailbreaking defeats the device's security model - removing sandbox "
                       "restrictions and granting privileged access - so malware or the user can bypass "
                       "OS protections and potentially MDM/containment controls. Enterprises typically "
                       "detect and block or wipe such devices.",
            "distractors": {
                "B": "It weakens, not strengthens, protections.",
                "C": "MDM does not require a rooted/jailbroken device - the opposite is true.",
                "D": "It materially undermines device security.",
            },
            "exam_pattern": "Root/jailbreak = removes sandbox + OS security controls (privileged untrusted code); block or wipe such devices.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - Mobile risks (rooting/jailbreaking)"],
    },
    {
        "id": "sscp-sys-r2-014", "exam": "sscp", "domain": "sscp_systems_app",
        "subtopic": "sscp_mobile_iot_security", "difficulty": 2, "type": "mcq",
        "stem": "When a BYOD employee leaves the company, the administrator wants to remove corporate "
                "email and apps from the personal phone while leaving the user's photos and personal data "
                "intact. Which capability accomplishes this?",
        "options": [
            {"id": "A", "text": "A full factory-reset wipe of the entire device"},
            {"id": "B", "text": "A selective (enterprise) wipe that removes only the managed corporate container/apps and data"},
            {"id": "C", "text": "Degaussing the phone's flash memory"},
            {"id": "D", "text": "Revoking the device's office Wi-Fi certificate, which deletes the apps"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A selective (enterprise) wipe removes only the managed corporate apps and data "
                       "(the work container), preserving the employee's personal content - the "
                       "appropriate offboarding action for BYOD. A full wipe would also erase personal "
                       "data.",
            "distractors": {
                "A": "A full wipe erases everything, including personal photos and data - inappropriate for a personal device.",
                "C": "Degaussing does not work on flash memory and would require physical destruction.",
                "D": "Revoking a Wi-Fi certificate blocks network access but does not remove the corporate apps/data.",
            },
            "exam_pattern": "BYOD offboarding = selective/enterprise wipe (corporate container only); full wipe erases personal data too.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 7 - BYOD offboarding (selective wipe)"],
    },
]
