"""(ISC)2 SSCP pool - Domain 1: Security Operations and Administration.

Original, objective-aligned practice items for the five Security Operations and
Administration subtopics tracked in CertLab:
  * sscp_cia_ethics         - the CIA triad (confidentiality, integrity,
                              availability) and the (ISC)2 Code of Ethics canons.
  * sscp_security_controls  - control categories (administrative / technical /
                              physical) and functions (preventive, detective,
                              corrective, deterrent, recovery, compensating,
                              directive).
  * sscp_asset_change_mgmt  - asset inventory, configuration/baseline
                              management, and change management (RFC, CAB).
  * sscp_security_awareness - awareness vs training vs education; resistance to
                              social engineering.
  * sscp_data_handling      - classification, labeling, retention, DLP, and
                              secure destruction (degaussing, crypto-erase).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_cia_ethics ==================================================
    {
        "id": "sscp-ops-001", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 1, "type": "fill",
        "stem": "The three core goals of information security are confidentiality, integrity, and "
                "____ - the property that ensures authorized users have timely, reliable access to "
                "data and systems. Name the missing goal.",
        "correct": ["availability"],
        "explanation": {
            "correct": "Availability completes the CIA triad; it ensures systems and data are "
                       "accessible to authorized users when needed, and is supported by redundancy, "
                       "backups, fault tolerance, and denial-of-service protection.",
            "distractors": {},
            "exam_pattern": "CIA triad = Confidentiality (secrecy), Integrity (accuracy), Availability (uptime).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - CIA triad"],
    },
    {
        "id": "sscp-ops-002", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 2, "type": "mcq",
        "stem": "A file-integrity monitoring tool recomputes the SHA-256 hash of critical system files "
                "and alerts when a stored value changes unexpectedly. Which element of the CIA triad "
                "does this control primarily support?",
        "options": [
            {"id": "A", "text": "Confidentiality"},
            {"id": "B", "text": "Integrity"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Detecting unauthorized or unexpected modification of data protects integrity - "
                       "the assurance that information has not been altered. Hashing is the classic "
                       "integrity mechanism.",
            "distractors": {
                "A": "Confidentiality is about preventing disclosure (e.g., encryption), not detecting change.",
                "C": "Availability concerns uptime and access, which hashing does not address.",
                "D": "Non-repudiation (tied to digital signatures) is not part of the CIA triad and is not what a bare hash provides.",
            },
            "exam_pattern": "Hashing / file-integrity monitoring maps to the Integrity goal.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - CIA triad"],
    },
    {
        "id": "sscp-ops-003", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_cia_ethics", "difficulty": 3, "type": "mcq",
        "stem": "The (ISC)2 Code of Ethics states that when its canons appear to conflict, they are "
                "resolved in the order they are listed. Which canon has the HIGHEST precedence?",
        "options": [
            {"id": "A", "text": "Act honorably, honestly, justly, responsibly, and legally"},
            {"id": "B", "text": "Advance and protect the profession"},
            {"id": "C", "text": "Protect society, the common good, necessary public trust and confidence, and the infrastructure"},
            {"id": "D", "text": "Provide diligent and competent service to principals"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The first and highest-precedence canon is to protect society, the common good, "
                       "public trust, and the infrastructure. The canons are applied in listed order "
                       "when they conflict.",
            "distractors": {
                "A": "'Act honorably...' is the second canon, not the first.",
                "B": "'Advance and protect the profession' is the fourth (lowest-precedence) canon.",
                "D": "'Provide diligent and competent service to principals' is the third canon.",
            },
            "exam_pattern": "Canon order: (1) society, (2) act honorably, (3) principals, (4) profession - applied in that priority.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - (ISC)2 Code of Ethics canons"],
    },

    # ===== sscp_security_controls ===========================================
    {
        "id": "sscp-ops-004", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 1, "type": "mcq",
        "stem": "A data center protects its entrance with bollards, a mantrap, and security guards. "
                "Into which control CATEGORY do these safeguards fall?",
        "options": [
            {"id": "A", "text": "Administrative (managerial) controls"},
            {"id": "B", "text": "Technical (logical) controls"},
            {"id": "C", "text": "Directive controls"},
            {"id": "D", "text": "Physical controls"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Bollards, mantraps, locks, and guards are physical controls - tangible "
                       "safeguards that protect facilities, people, and hardware.",
            "distractors": {
                "A": "Administrative controls are policies, procedures, and training, not physical barriers.",
                "B": "Technical/logical controls are implemented in hardware or software (e.g., firewalls, encryption).",
                "C": "'Directive' is a control function (guidance/instruction), not the category for a physical barrier.",
            },
            "exam_pattern": "Control categories: Administrative, Technical/logical, Physical.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control categories"],
    },
    {
        "id": "sscp-ops-005", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 2, "type": "mcq",
        "stem": "An intrusion prevention system (IPS) inspects traffic inline and drops malicious "
                "packets before they reach a host. By FUNCTION, this control is best classified as:",
        "options": [
            {"id": "A", "text": "Preventive"},
            {"id": "B", "text": "Detective"},
            {"id": "C", "text": "Corrective"},
            {"id": "D", "text": "Recovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Stopping an attack before it succeeds is a preventive control function - it "
                       "keeps the unwanted event from occurring.",
            "distractors": {
                "B": "A detective control (e.g., a plain IDS or log review) identifies events after they occur, without blocking.",
                "C": "A corrective control fixes or restores a system after an incident.",
                "D": "A recovery control restores operations/data (e.g., backups, DR) following damage.",
            },
            "exam_pattern": "Blocks before it happens = preventive; alerts after = detective; fixes after = corrective.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security control functions"],
    },
    {
        "id": "sscp-ops-006", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_controls", "difficulty": 3, "type": "mcq",
        "stem": "A legacy medical device cannot support the multi-factor authentication that policy "
                "requires. To meet the control objective another way, the team isolates it on a "
                "restricted VLAN with heightened monitoring. The VLAN isolation is acting as which "
                "type of control?",
        "options": [
            {"id": "A", "text": "Directive control"},
            {"id": "B", "text": "Deterrent control"},
            {"id": "C", "text": "Corrective control"},
            {"id": "D", "text": "Compensating control"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A compensating control is an alternative safeguard used when the primary "
                       "required control is not feasible, satisfying the same objective by other means.",
            "distractors": {
                "A": "A directive control instructs behavior (e.g., policy or signage), which the VLAN does not.",
                "B": "A deterrent control discourages an attacker (e.g., warning banners); isolation is not primarily a deterrent.",
                "C": "A corrective control remediates after an incident; here the control is applied proactively as a substitute.",
            },
            "exam_pattern": "Required control not possible -> an alternative that meets the objective = compensating control.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Compensating controls"],
    },

    # ===== sscp_asset_change_mgmt ===========================================
    {
        "id": "sscp-ops-007", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Before a configuration change is deployed to production, a cross-functional board "
                "formally reviews its risk, impact, and rollback plan and approves or rejects it. "
                "What is this body called?",
        "options": [
            {"id": "A", "text": "Computer Security Incident Response Team (CSIRT)"},
            {"id": "B", "text": "Change Advisory Board (CAB)"},
            {"id": "C", "text": "Data Loss Prevention committee"},
            {"id": "D", "text": "Business Impact Analysis team"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Change Advisory Board (CAB) evaluates and authorizes proposed changes, "
                       "weighing risk, impact, scheduling, and back-out plans before deployment.",
            "distractors": {
                "A": "A CSIRT responds to security incidents, not routine change approvals.",
                "C": "A DLP committee would govern data-leak controls, not change authorization.",
                "D": "A BIA team analyzes business impact for continuity planning, not individual change requests.",
            },
            "exam_pattern": "Formal review/approval of changes before production = CAB within change management.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Change management"],
    },
    {
        "id": "sscp-ops-008", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 2, "type": "fill",
        "stem": "The approved, documented standard configuration that systems are measured against so "
                "that unauthorized deviation (configuration drift) can be detected is called a "
                "security ____. Provide the one-word term.",
        "correct": ["baseline", "security baseline", "configuration baseline"],
        "explanation": {
            "correct": "A baseline is the documented, approved secure configuration used as the "
                       "reference point; comparing live systems against it reveals drift and "
                       "unauthorized changes.",
            "distractors": {},
            "exam_pattern": "Reference 'known-good' config for detecting drift = a (security/configuration) baseline.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Configuration management and baselines"],
    },
    {
        "id": "sscp-ops-009", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_asset_change_mgmt", "difficulty": 1, "type": "mcq",
        "stem": "Why is maintaining an accurate, complete asset inventory considered a foundational "
                "security practice?",
        "options": [
            {"id": "A", "text": "It eliminates the need for access controls on those assets"},
            {"id": "B", "text": "It guarantees automatic compliance with every regulation"},
            {"id": "C", "text": "You cannot reliably protect, patch, or account for assets you do not know exist"},
            {"id": "D", "text": "It removes the need for a change management process"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Asset management underpins nearly every other control: unknown systems cannot "
                       "be patched, monitored, scoped, or assigned an owner, so they become blind spots.",
            "distractors": {
                "A": "Knowing an asset exists does not replace the need to control access to it.",
                "B": "An inventory supports compliance but does not by itself guarantee it.",
                "D": "Inventory and change management are complementary; one does not remove the other.",
            },
            "exam_pattern": "'You can't protect what you don't know you have' - inventory enables all other controls.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Asset management"],
    },

    # ===== sscp_security_awareness ==========================================
    {
        "id": "sscp-ops-010", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "A program teaches administrators the specific, job-related skills to securely harden "
                "and patch the servers they manage. In the awareness-training-education hierarchy, "
                "this is best classified as:",
        "options": [
            {"id": "A", "text": "Training"},
            {"id": "B", "text": "Awareness"},
            {"id": "C", "text": "Education"},
            {"id": "D", "text": "Certification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Training builds the specific skills needed to perform a role or task - here, "
                       "secure server hardening - and is role-based and practical.",
            "distractors": {
                "B": "Awareness reinforces general secure behavior for all users; it does not teach job-specific skills.",
                "C": "Education is broad, long-term, concept-focused development (e.g., a degree), not task-specific skills.",
                "D": "Certification validates knowledge; it is an outcome, not the instructional level in this model.",
            },
            "exam_pattern": "Awareness = behavior for all; Training = skills for a role; Education = broad, long-term knowledge.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security awareness, training, and education"],
    },
    {
        "id": "sscp-ops-011", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_awareness", "difficulty": 1, "type": "mcq",
        "stem": "An organization periodically sends simulated phishing emails to its staff and tracks "
                "who clicks. What is the PRIMARY purpose of this exercise?",
        "options": [
            {"id": "A", "text": "To replace the email gateway spam filter"},
            {"id": "B", "text": "To satisfy data-at-rest encryption requirements"},
            {"id": "C", "text": "To measure and reinforce user awareness and resistance to social engineering"},
            {"id": "D", "text": "To test server failover and recovery time"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Simulated phishing measures susceptibility and reinforces awareness, directing "
                       "follow-up training to those who need it most.",
            "distractors": {
                "A": "A simulation complements, but does not replace, technical email filtering.",
                "B": "Phishing tests have nothing to do with encrypting stored data.",
                "D": "Failover and recovery testing is a continuity/DR activity, unrelated to phishing awareness.",
            },
            "exam_pattern": "Phishing simulations = measure + reinforce the human layer against social engineering.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Security awareness"],
    },
    {
        "id": "sscp-ops-012", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "Social-engineering attacks such as pretexting and phishing target people rather than "
                "systems. Which measure is the BEST first line of defense against them?",
        "options": [
            {"id": "A", "text": "A stateful inspection firewall at the perimeter"},
            {"id": "B", "text": "Ongoing security awareness training for users"},
            {"id": "C", "text": "Full-disk encryption on all endpoints"},
            {"id": "D", "text": "A network load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Because social engineering exploits human behavior, an informed, skeptical user "
                       "base built through ongoing awareness training is the most effective first defense.",
            "distractors": {
                "A": "A firewall filters network traffic but cannot stop a user from being deceived into an action.",
                "C": "Disk encryption protects data at rest; it does nothing against manipulation of a user.",
                "D": "A load balancer distributes traffic and has no bearing on social-engineering resistance.",
            },
            "exam_pattern": "People-targeted attacks are best countered first by educating people.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Social engineering and awareness"],
    },

    # ===== sscp_data_handling ===============================================
    {
        "id": "sscp-ops-013", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary purpose of implementing a data classification scheme (e.g., "
                "Public, Internal, Confidential, Restricted)?",
        "options": [
            {"id": "A", "text": "To increase total storage capacity"},
            {"id": "B", "text": "To speed up the corporate network"},
            {"id": "C", "text": "To eliminate the need for backups of sensitive data"},
            {"id": "D", "text": "To ensure data receives protection commensurate with its sensitivity and value"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Classification lets an organization apply the right level of protection and "
                       "handling to each category of data based on its sensitivity, value, and "
                       "regulatory exposure.",
            "distractors": {
                "A": "Classification governs protection, not storage capacity.",
                "B": "Labeling data does not affect network throughput.",
                "C": "Sensitive data still requires backups; classification may in fact mandate stronger ones.",
            },
            "exam_pattern": "Classification drives handling: match control strength to data sensitivity/value.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Data classification and handling"],
    },
    {
        "id": "sscp-ops-014", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 2, "type": "mcq",
        "stem": "A technician must sanitize magnetic hard disk drives for internal reuse so that the "
                "data they held cannot be recovered. Which method uses a strong magnetic field to "
                "render the data unrecoverable?",
        "options": [
            {"id": "A", "text": "Reformatting the file system"},
            {"id": "B", "text": "Degaussing"},
            {"id": "C", "text": "Deleting the files and emptying the recycle bin"},
            {"id": "D", "text": "Renaming the partition"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Degaussing exposes magnetic media to a powerful magnetic field that erases the "
                       "stored data (and typically renders the drive unusable). It applies to magnetic "
                       "media such as HDDs and tapes - not to flash-based SSDs.",
            "distractors": {
                "A": "A format rewrites file-system metadata but can leave recoverable data remnants.",
                "C": "Deleting files only removes pointers; the underlying data remains recoverable.",
                "D": "Renaming a partition changes a label and removes nothing.",
            },
            "exam_pattern": "Degaussing = magnetic media only; it does NOT work on SSDs/flash (use crypto-erase or destruction there).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Media sanitization and data destruction"],
    },
    {
        "id": "sscp-ops-015", "exam": "sscp", "domain": "sscp_secops_admin",
        "subtopic": "sscp_data_handling", "difficulty": 3, "type": "multi",
        "stem": "An organization is disposing of solid-state drives (SSDs) that stored sensitive data. "
                "Because SSDs are flash-based, which TWO sanitization methods are appropriate to "
                "ensure the data cannot be recovered? (Choose two.)",
        "options": [
            {"id": "A", "text": "Degaussing the SSD with a magnetic field"},
            {"id": "B", "text": "Cryptographic erase (destroying the drive's encryption key on a self-encrypting drive)"},
            {"id": "C", "text": "Physical destruction (shredding, pulverizing, or incinerating the drive)"},
            {"id": "D", "text": "Performing a single quick format of the volume"},
        ],
        "correct": ["B", "C"],
        "explanation": {
            "correct": "Crypto-erase (purging the media encryption key so ciphertext is unrecoverable) "
                       "and physical destruction are effective for flash media. These align with NIST "
                       "SP 800-88 Purge and Destroy approaches for SSDs.",
            "distractors": {
                "A": "Degaussing affects only magnetic domains; SSDs store data in flash cells, so a magnetic field does not erase them.",
                "D": "A quick format leaves data recoverable and does not reliably reach all flash cells (wear leveling may preserve copies).",
            },
            "exam_pattern": "SSD sanitization = crypto-erase or physical destruction; degaussing and quick format do not work.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 1 - Media sanitization (NIST SP 800-88 clear/purge/destroy)"],
    },
]
