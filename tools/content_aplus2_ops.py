"""CompTIA A+ Core 2 (220-1102) EXPANSION pool — Domain 4.0 Operational Procedures.

Original, objective-aligned questions that deepen the existing operational_procedures
items (aplus2-ops-001..007) in content_aplus2.py to real exam depth. Same authoring
rules as the other pools: original content mapped to the public 220-1102 objectives,
never real exam items. build_content.py shuffles option order, so the answer key here
is not positionally biased. IDs begin at aplus2-ops-101 to avoid collisions.
"""

QUESTIONS = [
    # ===== 4.0 Operational Procedures : documentation_a2 ====================
    {
        "id": "aplus2-ops-101", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 2, "type": "mcq",
        "stem": "While working a help-desk ticket, a technician records a running, timestamped "
                "account of each action taken as the issue is being resolved. Which ticket field "
                "is being filled in?",
        "options": [
            {"id": "A", "text": "Progress notes"},
            {"id": "B", "text": "Problem description"},
            {"id": "C", "text": "Severity"},
            {"id": "D", "text": "Categories"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Progress notes capture the ongoing, step-by-step actions taken while the "
                       "ticket is being worked, keeping a clear record for hand-offs and audits.",
            "distractors": {
                "B": "The problem description is the initial statement of the reported issue, written when the ticket is opened.",
                "C": "Severity rates how urgent/impactful the issue is; it does not record the work performed.",
                "D": "Categories classify the type of issue (e.g., hardware, email) for routing and reporting.",
            },
            "exam_pattern": "Ticket fields: problem description (initial) -> progress notes (ongoing work) -> problem resolution (final fix); severity/categories classify it.",
        },
    },
    {
        "id": "aplus2-ops-102", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 2, "type": "mcq",
        "stem": "An organization attaches a unique barcoded label to every laptop and records its "
                "serial number, purchase date, and warranty status in a central database. This "
                "practice is BEST described as what?",
        "options": [
            {"id": "A", "text": "Asset management using asset tags and an inventory database"},
            {"id": "B", "text": "Maintaining a network topology diagram"},
            {"id": "C", "text": "Writing a standard operating procedure"},
            {"id": "D", "text": "Enforcing an acceptable use policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Asset tags/barcodes plus an inventory database that tracks procurement, "
                       "warranty, and assignment are the core of asset management.",
            "distractors": {
                "B": "A topology diagram maps how devices connect on the network, not an inventory of owned equipment.",
                "C": "An SOP documents the repeatable steps for performing a task.",
                "D": "An AUP defines how employees may use company resources; it is not an inventory record.",
            },
            "exam_pattern": "Asset tags/barcodes + inventory database (serial, procurement, warranty) = asset management.",
        },
    },
    {
        "id": "aplus2-ops-103", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 1, "type": "mcq",
        "stem": "Which organizational policy specifies the minimum length, required complexity, and "
                "how often users must change their sign-in credentials?",
        "options": [
            {"id": "A", "text": "Password policy"},
            {"id": "B", "text": "Acceptable use policy (AUP)"},
            {"id": "C", "text": "Mobile device management (MDM) policy"},
            {"id": "D", "text": "Incident response policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A password policy defines credential rules — minimum length, complexity, "
                       "history, and rotation/expiration intervals.",
            "distractors": {
                "B": "An AUP states how employees may use company systems and data, not password rules.",
                "C": "An MDM policy governs enrollment and control of mobile devices (encryption, remote wipe, app restrictions).",
                "D": "An incident response policy defines how security incidents are reported and handled.",
            },
            "exam_pattern": "Credential length/complexity/rotation rules = password policy; resource-use rules = AUP.",
        },
    },
    {
        "id": "aplus2-ops-104", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "documentation_a2", "difficulty": 1, "type": "mcq",
        "stem": "After solving an unusual printer error, a technician writes up the symptoms and the "
                "fix and adds it to a shared, searchable repository so colleagues can reuse the "
                "solution later. What is this repository called?",
        "options": [
            {"id": "A", "text": "A knowledge base (KB) of articles"},
            {"id": "B", "text": "A standard operating procedure (SOP)"},
            {"id": "C", "text": "A network topology diagram"},
            {"id": "D", "text": "A change request"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A knowledge base is a searchable collection of articles documenting known "
                       "issues and their resolutions so solutions can be reused.",
            "distractors": {
                "B": "An SOP lists the agreed, repeatable steps for performing a task, not a record of a specific solved issue.",
                "C": "A topology diagram maps the network's connections.",
                "D": "A change request is a formal proposal to modify a system.",
            },
            "exam_pattern": "Searchable repository of known issues + fixes = knowledge base/articles.",
        },
    },

    # ===== 4.0 Operational Procedures : change_management_a2 ================
    {
        "id": "aplus2-ops-105", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "In a formal change-management process, which group reviews a proposed change and "
                "formally approves or rejects it before it is implemented?",
        "options": [
            {"id": "A", "text": "The change advisory board (CAB)"},
            {"id": "B", "text": "The end users who will be affected"},
            {"id": "C", "text": "The incident response team"},
            {"id": "D", "text": "The vendor's technical support line"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The change advisory board (change board) evaluates the request, weighs the "
                       "risk, and gives the formal approve/reject decision before implementation.",
            "distractors": {
                "B": "Affected end users provide acceptance and feedback, but they do not formally authorize the change.",
                "C": "The incident response team handles security incidents, not change approvals.",
                "D": "Vendor support may advise, but it is not the organization's change-approval authority.",
            },
            "exam_pattern": "Formal body that approves/rejects a change = change advisory board (CAB).",
        },
    },
    {
        "id": "aplus2-ops-106", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 2, "type": "mcq",
        "stem": "Before rolling a configuration change out to production, a team first applies and "
                "tests it in an isolated environment that mirrors production but cannot affect live "
                "systems. What is this environment called?",
        "options": [
            {"id": "A", "text": "A sandbox (test environment)"},
            {"id": "B", "text": "The backout plan"},
            {"id": "C", "text": "The change request"},
            {"id": "D", "text": "The production baseline"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sandbox testing applies the change in an isolated, production-like "
                       "environment first, so problems are found without risking live systems.",
            "distractors": {
                "B": "A backout plan is the documented steps to revert if the change fails — not the place you test it.",
                "C": "A change request is the formal proposal document that describes the change.",
                "D": "A production baseline is the documented known-good production configuration, not a test area.",
            },
            "exam_pattern": "Isolated, test-before-deploy environment = sandbox testing.",
        },
    },
    {
        "id": "aplus2-ops-107", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "change_management_a2", "difficulty": 3, "type": "mcq",
        "stem": "A change plan is technically ready, but before scheduling the rollout the project "
                "lead confirms that the affected department has reviewed the change, agrees with it, "
                "and is prepared for it. Which change-management element does this satisfy?",
        "options": [
            {"id": "A", "text": "End-user acceptance"},
            {"id": "B", "text": "Risk analysis"},
            {"id": "C", "text": "Sandbox testing"},
            {"id": "D", "text": "The backout plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "End-user acceptance confirms the people affected have reviewed and agreed to "
                       "the change and are ready for it before it goes live.",
            "distractors": {
                "B": "Risk analysis evaluates the likelihood and impact of problems to assign a risk level.",
                "C": "Sandbox testing validates the change in an isolated environment, not with the users.",
                "D": "The backout plan describes how to revert the change if it fails.",
            },
            "exam_pattern": "Affected users review and agree before rollout = end-user acceptance.",
        },
    },

    # ===== 4.0 Operational Procedures : backup_recovery ====================
    {
        "id": "aplus2-ops-108", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A consultant recommends following the 3-2-1 backup rule. What does this rule "
                "require?",
        "options": [
            {"id": "A", "text": "Keep 3 copies of the data, on 2 different media types, with 1 copy off-site"},
            {"id": "B", "text": "Keep 3 full backups, 2 incrementals, and 1 differential each week"},
            {"id": "C", "text": "Retain backups for 3 years, test 2 of them, and encrypt 1"},
            {"id": "D", "text": "Run 3 daily, 2 weekly, and 1 monthly backup job"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 3-2-1 rule means keep at least 3 copies of your data, store them on 2 "
                       "different media/storage types, and keep 1 copy off-site.",
            "distractors": {
                "B": "This mixes up backup types; the rule is about copies, media, and location, not a weekly type schedule.",
                "C": "Retention, testing, and encryption are good practices but are not what 3-2-1 defines.",
                "D": "This invents a job frequency; the numbers in 3-2-1 refer to copies/media/off-site, not jobs per period.",
            },
            "exam_pattern": "3-2-1 = 3 copies, 2 different media types, 1 copy off-site.",
        },
    },
    {
        "id": "aplus2-ops-109", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A company has run nightly backups for a year but has never confirmed that the "
                "backups can actually be restored. Which practice directly addresses this gap?",
        "options": [
            {"id": "A", "text": "Regularly test and verify restores from the backups"},
            {"id": "B", "text": "Increase the backup frequency to hourly"},
            {"id": "C", "text": "Switch from full to incremental backups"},
            {"id": "D", "text": "Move all backups onto the same server as the production data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Backups are only useful if they restore. Periodically performing test "
                       "restores verifies the media and the backup chain are actually recoverable.",
            "distractors": {
                "B": "More frequent backups still prove nothing about whether a restore will succeed.",
                "C": "Changing the backup type does not demonstrate recoverability.",
                "D": "Co-locating backups with the production data violates off-site/3-2-1 and risks losing both at once.",
            },
            "exam_pattern": "A backup you've never restored isn't proven — test/verify restores on a schedule.",
        },
    },
    {
        "id": "aplus2-ops-110", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "backup_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A backup scheme keeps separate daily, weekly, and monthly backup sets, promoting "
                "certain backups to longer retention as they age. This rotation scheme is known as "
                "what?",
        "options": [
            {"id": "A", "text": "Grandfather-father-son (GFS)"},
            {"id": "B", "text": "The 3-2-1 rule"},
            {"id": "C", "text": "A synthetic full backup"},
            {"id": "D", "text": "Chain of custody"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Grandfather-father-son rotates media across daily (son), weekly (father), and "
                       "monthly (grandfather) sets, balancing retention against the number of tapes/media.",
            "distractors": {
                "B": "The 3-2-1 rule governs how many copies, how many media types, and off-site storage — not a retention rotation.",
                "C": "A synthetic full is a full backup assembled on the backup server from earlier backups; it is a type, not a rotation scheme.",
                "D": "Chain of custody is an evidence-handling record in incident response, unrelated to backup rotation.",
            },
            "exam_pattern": "Daily/weekly/monthly retention rotation = Grandfather-Father-Son (GFS).",
        },
    },

    # ===== 4.0 Operational Procedures : safety =============================
    {
        "id": "aplus2-ops-111", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 2, "type": "mcq",
        "stem": "A power supply bursts into flames while it is still plugged in and energized. Which "
                "class of fire extinguisher is designed for electrical equipment fires?",
        "options": [
            {"id": "A", "text": "Class C"},
            {"id": "B", "text": "Class A"},
            {"id": "C", "text": "Class B"},
            {"id": "D", "text": "Class D"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Class C extinguishers are rated for energized electrical equipment; they use "
                       "a non-conductive agent so the operator isn't shocked.",
            "distractors": {
                "B": "Class A is for ordinary combustibles like wood, paper, and cloth.",
                "C": "Class B is for flammable liquids and gases.",
                "D": "Class D is for combustible metals such as magnesium or lithium.",
            },
            "exam_pattern": "Energized electrical fire = Class C (A=ordinary combustibles, B=liquids, D=metals).",
        },
    },
    {
        "id": "aplus2-ops-112", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 2, "type": "multi",
        "stem": "A technician is decommissioning old gear. Which TWO items must be handled as "
                "regulated/toxic waste and taken to an approved recycling or disposal facility "
                "rather than placed in the regular trash? (Choose two.)",
        "options": [
            {"id": "A", "text": "A swollen lithium-ion laptop battery"},
            {"id": "B", "text": "A used laser printer toner cartridge"},
            {"id": "C", "text": "An empty anti-static bag"},
            {"id": "D", "text": "A plastic drive-bay blank"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Batteries and toner are regulated/hazardous materials; both must be recycled "
                       "or disposed of per the SDS and local regulations, not thrown in the trash.",
            "distractors": {
                "C": "An anti-static bag is ordinary plastic packaging with no hazardous content.",
                "D": "A plastic drive-bay blank is inert plastic and is not regulated waste.",
            },
            "exam_pattern": "Regulated/toxic waste: batteries, toner, and CRTs -> recycle/dispose per the SDS and local regulations.",
        },
    },
    {
        "id": "aplus2-ops-113", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 2, "type": "mcq",
        "stem": "Before handling and disposing of a chemical cleaning solvent, a technician needs to "
                "know its hazards, required protective equipment, and proper disposal steps. Which "
                "document provides this information?",
        "options": [
            {"id": "A", "text": "The safety data sheet (SDS/MSDS)"},
            {"id": "B", "text": "A standard operating procedure"},
            {"id": "C", "text": "An end-user license agreement (EULA)"},
            {"id": "D", "text": "An acceptable use policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A safety data sheet (SDS, formerly MSDS) documents a substance's hazards, "
                       "safe-handling and PPE requirements, storage, and disposal instructions.",
            "distractors": {
                "B": "An SOP lists repeatable task steps; it is not the authoritative source for a chemical's hazards.",
                "C": "A EULA states the legal terms for using software.",
                "D": "An AUP defines how employees may use company resources.",
            },
            "exam_pattern": "Chemical hazards/handling/PPE/disposal info = SDS (formerly MSDS).",
        },
    },
    {
        "id": "aplus2-ops-114", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "safety", "difficulty": 1, "type": "mcq",
        "stem": "A technician must move a heavy UPS from the floor up to a rack. Which lifting "
                "technique is safest?",
        "options": [
            {"id": "A", "text": "Bend at the knees and lift with the legs, keeping the back straight and the load close"},
            {"id": "B", "text": "Bend at the waist and lift using the back muscles"},
            {"id": "C", "text": "Hold the load at arm's length to keep it away from the body"},
            {"id": "D", "text": "Twist at the waist while carrying the load to set it down"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Lift with the legs, keep the back straight and the load close to the body to "
                       "avoid back injury; get help or a cart for heavy items.",
            "distractors": {
                "B": "Lifting with the back rather than the legs is the classic cause of lifting injuries.",
                "C": "Holding the load away from the body greatly increases strain on the back.",
                "D": "Twisting while loaded is a common way to injure the back; turn with your feet instead.",
            },
            "exam_pattern": "Personal safety: lift with the legs, back straight, load close, don't twist; observe weight limits.",
        },
    },

    # ===== 4.0 Operational Procedures : incident_response_a2 ===============
    {
        "id": "aplus2-ops-115", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A technician is the first to discover a possible security incident on a user's PC. "
                "Following first-response best practice, what should they do?",
        "options": [
            {"id": "A", "text": "Report it through the proper channels and preserve the data/device"},
            {"id": "B", "text": "Immediately wipe the drive to stop the threat from spreading"},
            {"id": "C", "text": "Post a warning in the company chat so everyone is aware"},
            {"id": "D", "text": "Keep using the PC to investigate the problem on their own"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "First response is to identify the incident, report it through the proper "
                       "channels, and preserve the affected data/device so evidence stays intact.",
            "distractors": {
                "B": "Wiping the drive destroys the very evidence an investigation needs.",
                "C": "Broadcasting the incident can violate policy and tip off a malicious insider; use proper channels.",
                "D": "Continuing to use the device can alter or destroy evidence and should be avoided.",
            },
            "exam_pattern": "First response: identify -> report through proper channels -> preserve the data/device (don't alter/destroy).",
        },
    },
    {
        "id": "aplus2-ops-116", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 3, "type": "mcq",
        "stem": "When collecting digital evidence from a running computer, which data should be "
                "captured FIRST because it is lost soonest?",
        "options": [
            {"id": "A", "text": "The contents of RAM and the list of running processes"},
            {"id": "B", "text": "Files stored on the hard drive"},
            {"id": "C", "text": "Data on backup tapes"},
            {"id": "D", "text": "Printed documents in a filing cabinet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The order of volatility says to collect the most volatile data first — CPU "
                       "cache and RAM (running processes, network connections) vanish when power is lost.",
            "distractors": {
                "B": "Disk data is far more persistent than memory, so it is collected after volatile memory.",
                "C": "Backup tapes are archival and change least often — among the last to collect.",
                "D": "Printed documents are the least volatile of all and are not time-sensitive to capture.",
            },
            "exam_pattern": "Order of volatility: capture most volatile first (CPU cache/RAM) before disk, then backups/archives/printouts.",
        },
    },
    {
        "id": "aplus2-ops-117", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A healthcare provider stores patients' medical histories and treatment records. "
                "Which category of regulated data is this, requiring special handling and "
                "protection?",
        "options": [
            {"id": "A", "text": "PHI (protected health information)"},
            {"id": "B", "text": "PCI (payment card data)"},
            {"id": "C", "text": "Application source code"},
            {"id": "D", "text": "Public marketing brochures"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Medical and treatment records are protected health information (PHI), a "
                       "regulated data class (e.g., under HIPAA) with strict handling requirements.",
            "distractors": {
                "B": "PCI covers cardholder/payment card data governed by PCI DSS, not medical records.",
                "C": "Source code is intellectual property but is not one of the regulated-data categories (PII/PCI/GDPR/PHI).",
                "D": "Public marketing material is not sensitive or regulated data.",
            },
            "exam_pattern": "Regulated data: medical = PHI, card data = PCI, personal identifiers = PII, EU personal data = GDPR.",
        },
    },
    {
        "id": "aplus2-ops-118", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "incident_response_a2", "difficulty": 2, "type": "mcq",
        "stem": "A user wants to install one purchased, single-seat copy of a program on 15 office "
                "computers, but the license forbids it. Which concept governs how many installations "
                "and what use are permitted?",
        "options": [
            {"id": "A", "text": "The software license / EULA (enforced by DRM)"},
            {"id": "B", "text": "Chain of custody"},
            {"id": "C", "text": "The acceptable use policy"},
            {"id": "D", "text": "The change advisory board"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The end-user license agreement (EULA) and the license type define how many "
                       "installs and what usage are allowed; digital rights management (DRM) enforces it. "
                       "Installing a single-seat license on 15 PCs violates it.",
            "distractors": {
                "B": "Chain of custody is the documented handling of evidence in an investigation.",
                "C": "An AUP governs how employees may use resources, not software license counts.",
                "D": "The change advisory board approves changes; it does not set license terms.",
            },
            "exam_pattern": "How many installs / what use is allowed = software license/EULA (personal vs enterprise, open-source vs commercial); DRM enforces it.",
        },
    },

    # ===== 4.0 Operational Procedures : communication_professionalism ======
    {
        "id": "aplus2-ops-119", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 1, "type": "mcq",
        "stem": "While explaining a repair to a non-technical customer, which communication practice "
                "is MOST professional?",
        "options": [
            {"id": "A", "text": "Avoid jargon, acronyms, and slang and explain in plain language"},
            {"id": "B", "text": "Use as many technical acronyms as possible to show expertise"},
            {"id": "C", "text": "Tell the customer the details are too complex to explain"},
            {"id": "D", "text": "Rush through the explanation so the customer isn't bored"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matching your language to the audience — avoiding jargon, acronyms, and slang "
                       "— keeps a non-technical customer informed and respected.",
            "distractors": {
                "B": "Piling on acronyms confuses a non-technical customer and signals poor communication.",
                "C": "Dismissing the customer as unable to understand is condescending and unhelpful.",
                "D": "Rushing fails to confirm understanding and to set/meet expectations.",
            },
            "exam_pattern": "Professionalism: avoid jargon/acronyms/slang; speak to the customer's level.",
        },
    },
    {
        "id": "aplus2-ops-120", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 2, "type": "multi",
        "stem": "Which TWO behaviors reflect professional conduct while working at a customer's "
                "workspace? (Choose two.)",
        "options": [
            {"id": "A", "text": "Arrive on time, and contact the customer if you will be delayed"},
            {"id": "B", "text": "Silence your phone and avoid personal calls, texting, and social media"},
            {"id": "C", "text": "Post the customer's problem on social media to crowdsource a fix"},
            {"id": "D", "text": "Take personal calls at the desk so you stay reachable"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Being on time (or calling ahead) and avoiding personal distractions are core "
                       "professional behaviors on site.",
            "distractors": {
                "C": "Posting a customer's issue on social media discloses private information and breaches confidentiality.",
                "D": "Taking personal calls is a distraction that undermines professionalism and focus.",
            },
            "exam_pattern": "Professionalism: be on time (or call), avoid distractions, and never disclose customer info on social media.",
        },
    },
    {
        "id": "aplus2-ops-121", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "communication_professionalism", "difficulty": 2, "type": "mcq",
        "stem": "While repairing a manager's laptop, a technician notices personal financial "
                "documents and private emails open on the screen. What is the appropriate action?",
        "options": [
            {"id": "A", "text": "Keep the materials confidential — do not access, copy, or share them"},
            {"id": "B", "text": "Read through them to check whether they relate to the repair"},
            {"id": "C", "text": "Mention the interesting ones to coworkers afterward"},
            {"id": "D", "text": "Copy them in case they are needed later as evidence"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Confidential and private materials must be left alone — a technician should "
                       "not access, copy, or share a customer's private data.",
            "distractors": {
                "B": "Reading private documents that aren't relevant to the task violates the customer's privacy.",
                "C": "Gossiping about a customer's private information is a serious breach of professionalism.",
                "D": "Copying private materials without authorization is inappropriate and a privacy violation.",
            },
            "exam_pattern": "Deal appropriately with confidential/private materials: don't access, copy, or share them.",
        },
    },

    # ===== 4.0 Operational Procedures : scripting_basics ===================
    {
        "id": "aplus2-ops-122", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "mcq",
        "stem": "A legacy Windows logon script is written in Microsoft's VBScript language. Which "
                "file extension identifies it?",
        "options": [
            {"id": "A", "text": ".vbs"},
            {"id": "B", "text": ".js"},
            {"id": "C", "text": ".py"},
            {"id": "D", "text": ".sh"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VBScript files use the .vbs extension.",
            "distractors": {
                "B": ".js identifies a JavaScript file.",
                "C": ".py identifies a Python script.",
                "D": ".sh identifies a Linux/Unix Bash shell script.",
            },
            "exam_pattern": ".vbs VBScript | .js JavaScript | .py Python | .sh Bash | .ps1 PowerShell | .bat/.cmd batch.",
        },
    },
    {
        "id": "aplus2-ops-123", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs every workstation to automatically reconnect a shared network "
                "drive at each user logon. Which is the BEST use of scripting here?",
        "options": [
            {"id": "A", "text": "A logon script that remaps the network drive automatically"},
            {"id": "B", "text": "Manually mapping the drive on each PC every morning"},
            {"id": "C", "text": "Emailing users instructions to map the drive themselves"},
            {"id": "D", "text": "Replacing the file server with a cloud storage subscription"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Remapping network drives is a classic scripting use case — a logon script does "
                       "it automatically and consistently for every user.",
            "distractors": {
                "B": "Manually mapping each PC daily does not scale and is error-prone.",
                "C": "Relying on users to follow emailed steps is inconsistent and generates support calls.",
                "D": "Swapping out the file server is an unrelated infrastructure change, not the automation requested.",
            },
            "exam_pattern": "Scripting use cases: remap drives, restart machines, install apps, automate backups, gather info, push updates.",
        },
    },
    {
        "id": "aplus2-ops-124", "exam": "aplus2", "domain": "operational_procedures",
        "subtopic": "scripting_basics", "difficulty": 2, "type": "multi",
        "stem": "Before deploying a script across many machines, which TWO are legitimate risks a "
                "technician should weigh? (Choose two.)",
        "options": [
            {"id": "A", "text": "Unintentionally introducing malware"},
            {"id": "B", "text": "Inadvertently changing system settings or crashing the system/browser"},
            {"id": "C", "text": "Permanently voiding the device's hardware warranty"},
            {"id": "D", "text": "Making the script impossible to edit once it is saved"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Scripts can carry or fetch malware, and a flawed script can inadvertently "
                       "change system settings or exhaust resources and crash the system or browser.",
            "distractors": {
                "C": "Running a script does not void a device's hardware warranty.",
                "D": "Scripts are plain text and remain freely editable after they are saved.",
            },
            "exam_pattern": "Script risks: introducing malware, inadvertently changing system settings, and system/browser crashes from mishandling resources.",
        },
    },
]
