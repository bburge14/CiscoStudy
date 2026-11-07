"""CompTIA Security+ SY0-701 — Domain 5.0 EXPANSION pool.

Original, objective-aligned questions for "Security Program Management &
Oversight" (domain key ``security_program_mgmt``), authored to deepen the base
pool in tools/content_secplus.py to real exam depth. Never real exam items.

Coverage: all six subtopics (~4 each) — security_governance, risk_management,
third_party_risk, compliance_privacy, audits_assessments, security_awareness.
IDs continue at secplus-mgmt-101 so they never collide with the base pool
(secplus-mgmt-001..006). build_content.py shuffles option order, so the keyed
option is not positionally biased.
"""

QUESTIONS = [
    # ===== 5.0 Security Program Management & Oversight =======================

    # ----- security_governance ---------------------------------------------
    {
        "id": "secplus-mgmt-101", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 2, "type": "mcq",
        "stem": "A multinational corporation wants all security policies and standards to be "
                "set by one headquarters team and applied uniformly to every regional office, "
                "with no local deviation. Which governance model is this?",
        "options": [
            {"id": "A", "text": "Centralized governance"},
            {"id": "B", "text": "Decentralized governance"},
            {"id": "C", "text": "A security steering committee"},
            {"id": "D", "text": "A board of directors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Centralized governance concentrates decision-making in a single authority "
                       "(HQ), giving uniform, consistent policy across the whole organization.",
            "distractors": {
                "B": "Decentralized governance delegates decisions to regional/business units, which "
                     "produces local variation — the opposite of what is wanted here.",
                "C": "A steering committee is a body that reviews/advises on policy; it is not the "
                     "centralized-vs-decentralized structural model itself.",
                "D": "A board of directors provides top-level oversight; it is a governance body, not "
                     "the centralized/decentralized placement of authority.",
            },
            "exam_pattern": "Governance STRUCTURE axis: centralized (one authority, uniform) vs "
                            "decentralized (distributed, flexible but inconsistent).",
        },
    },
    {
        "id": "secplus-mgmt-102", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 2, "type": "mcq",
        "stem": "A business executive is formally accountable for a customer database: she assigns "
                "its data classification and approves who may access it, while the IT team performs "
                "backups and enforces the permissions she authorizes. Which role does the executive hold?",
        "options": [
            {"id": "A", "text": "Data owner"},
            {"id": "B", "text": "Data custodian / steward"},
            {"id": "C", "text": "Data processor"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The data owner is the senior individual accountable for a data set — setting its "
                       "classification and authorizing access. The role is about accountability, not hands-on work.",
            "distractors": {
                "B": "The custodian/steward implements and maintains the controls (backups, applying the "
                     "permissions) on the owner's behalf — that is the IT team here, not the executive.",
                "C": "A processor processes data on behalf of a controller (a third-party concept), not the "
                     "internal accountable owner.",
                "D": "A data subject is the individual the personal data is ABOUT, not a management role.",
            },
            "exam_pattern": "Owner = accountable, classifies & authorizes. Custodian/steward = implements & "
                            "maintains. Controller = decides why/how. Processor = acts on controller's behalf.",
        },
    },
    {
        "id": "secplus-mgmt-103", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 1, "type": "mcq",
        "stem": "Which policy defines the rules employees must follow when using company-issued "
                "computers, email, and internet access, including explicitly prohibited activities?",
        "options": [
            {"id": "A", "text": "Acceptable Use Policy (AUP)"},
            {"id": "B", "text": "Business Continuity Plan (BCP)"},
            {"id": "C", "text": "Incident Response Plan (IRP)"},
            {"id": "D", "text": "Service-Level Agreement (SLA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An AUP spells out acceptable and prohibited use of organizational systems and "
                       "resources by users — the document employees typically sign on hire.",
            "distractors": {
                "B": "A BCP keeps critical business functions running during/after a disruption.",
                "C": "An IRP defines how the organization detects and responds to security incidents.",
                "D": "An SLA is an agreement with a provider defining measurable service commitments.",
            },
            "exam_pattern": "Match the policy to its audience: AUP = end-user conduct, BCP/DRP = continuity, "
                            "IRP = incident handling, SDLC = secure development.",
        },
    },
    {
        "id": "secplus-mgmt-104", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 3, "type": "mcq",
        "stem": "A cross-functional group of managers from IT, legal, HR, and finance meets quarterly "
                "to review proposed security-policy changes, approve them, and advise executive "
                "leadership. Which governance structure is this?",
        "options": [
            {"id": "A", "text": "Security steering committee"},
            {"id": "B", "text": "Board of directors"},
            {"id": "C", "text": "Change advisory board (CAB)"},
            {"id": "D", "text": "Data protection officer (DPO)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A security steering committee is a cross-functional body that reviews and approves "
                       "security policy and advises leadership — exactly the described role.",
            "distractors": {
                "B": "A board of directors gives the highest-level organizational oversight and fiduciary "
                     "governance, not the quarterly operational policy-review function described.",
                "C": "A CAB reviews and approves proposed IT CHANGES (change management), not security "
                     "policy direction broadly.",
                "D": "A DPO is an individual role responsible for privacy/data-protection compliance, not a "
                     "cross-functional committee.",
            },
            "exam_pattern": "Governance bodies: board (top oversight) > steering committee (policy review/advise) "
                            "vs CAB (approves changes). Don't confuse a committee with the board.",
        },
    },

    # ----- risk_management --------------------------------------------------
    {
        "id": "secplus-mgmt-105", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A server is valued at $50,000. A specific fire is expected to destroy 40% of that "
                "value if it occurs. What is the single loss expectancy (SLE) for one such event?",
        "options": [
            {"id": "A", "text": "$20,000"},
            {"id": "B", "text": "$50,000"},
            {"id": "C", "text": "$30,000"},
            {"id": "D", "text": "$2,000"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SLE = Asset Value x Exposure Factor = $50,000 x 0.40 = $20,000. The exposure "
                       "factor is the percentage of the asset lost in a single event.",
            "distractors": {
                "B": "$50,000 is the full asset value (EF = 100%), not a 40% loss.",
                "C": "$30,000 is the value that SURVIVES (the remaining 60%), not the loss.",
                "D": "$2,000 misreads 40% as 4%.",
            },
            "exam_pattern": "SLE = AV x EF (single event). Then ALE = SLE x ARO (per year). Keep SLE and ALE separate.",
        },
    },
    {
        "id": "secplus-mgmt-106", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 2, "type": "mcq",
        "stem": "In business continuity planning, which metric defines the MAXIMUM amount of data — "
                "expressed as a period of time — that an organization can tolerate losing after an incident?",
        "options": [
            {"id": "A", "text": "Recovery Point Objective (RPO)"},
            {"id": "B", "text": "Recovery Time Objective (RTO)"},
            {"id": "C", "text": "Mean Time To Repair (MTTR)"},
            {"id": "D", "text": "Mean Time Between Failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RPO is how far back in time you can afford to lose data — it drives backup frequency "
                       "(a 1-hour RPO means backups at least hourly).",
            "distractors": {
                "B": "RTO is the maximum tolerable DOWNTIME — how fast service must be restored, not data loss.",
                "C": "MTTR is the average time to repair a failed component and restore it.",
                "D": "MTBF is the average time between failures of a repairable system (reliability), not data loss.",
            },
            "exam_pattern": "RPO = data loss (look back, backups). RTO = downtime (look forward, restore speed). "
                            "MTTR/MTBF = maintainability/reliability of components.",
        },
    },
    {
        "id": "secplus-mgmt-107", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A risk assessment rates each risk as High, Medium, or Low based on the judgment and "
                "experience of subject-matter experts, without assigning any monetary values. Which "
                "type of risk analysis is this?",
        "options": [
            {"id": "A", "text": "Qualitative"},
            {"id": "B", "text": "Quantitative"},
            {"id": "C", "text": "Business impact analysis"},
            {"id": "D", "text": "Residual risk calculation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Qualitative analysis uses subjective ratings (High/Medium/Low, 1-5) based on expert "
                       "judgment, with no dollar figures — fast but not precisely comparable.",
            "distractors": {
                "B": "Quantitative analysis assigns numeric/monetary values (AV, EF, SLE, ARO, ALE).",
                "C": "A BIA identifies critical functions and recovery objectives (RTO/RPO); it is not the "
                     "subjective-vs-numeric scoring method being asked about.",
                "D": "Residual risk is the risk REMAINING after controls are applied, not an analysis method.",
            },
            "exam_pattern": "Qualitative = words/ratings (judgment). Quantitative = numbers/dollars (SLE/ALE).",
        },
    },
    {
        "id": "secplus-mgmt-108", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 3, "type": "mcq",
        "stem": "A fast-growing startup deliberately accepts a high level of risk in order to enter new "
                "markets quickly and maximize growth. Which risk appetite BEST describes this posture?",
        "options": [
            {"id": "A", "text": "Expansionary"},
            {"id": "B", "text": "Conservative"},
            {"id": "C", "text": "Neutral"},
            {"id": "D", "text": "Risk avoidance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SY0-701 describes risk appetite as expansionary, conservative, or neutral. An "
                       "expansionary appetite is willing to take on MORE risk to pursue growth/reward.",
            "distractors": {
                "B": "A conservative appetite is risk-averse — it prioritizes protecting what exists over growth.",
                "C": "A neutral appetite balances risk and reward without leaning toward either.",
                "D": "Risk avoidance is a risk-TREATMENT strategy (stop the activity), not a category of appetite.",
            },
            "exam_pattern": "Risk appetite categories = expansionary / conservative / neutral. Don't confuse "
                            "appetite (how much risk is desired) with treatment (avoid/transfer/mitigate/accept).",
        },
    },

    # ----- third_party_risk -------------------------------------------------
    {
        "id": "secplus-mgmt-109", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "A company and a vendor sign a single overarching contract that sets the general legal "
                "and business terms governing their entire relationship; the specifics of each individual "
                "project will be defined separately later. What is the overarching contract?",
        "options": [
            {"id": "A", "text": "Master Service Agreement (MSA)"},
            {"id": "B", "text": "Statement of Work (SOW)"},
            {"id": "C", "text": "Memorandum of Understanding (MOU)"},
            {"id": "D", "text": "Service-Level Agreement (SLA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An MSA establishes the master/general terms for an ongoing relationship; individual "
                       "engagements are then scoped under it with separate SOWs.",
            "distractors": {
                "B": "A SOW defines the specific tasks, deliverables, and timeline for ONE engagement — the "
                     "'separate later' document, not the overarching one.",
                "C": "An MOU is a (usually non-binding) statement of mutual intent, not a master contract.",
                "D": "An SLA defines measurable service metrics and penalties, not the overarching legal terms.",
            },
            "exam_pattern": "MSA = master/general terms (umbrella). SOW/WO = specific work under it. "
                            "MOU/MOA = intent. SLA = measurable metrics.",
        },
    },
    {
        "id": "secplus-mgmt-110", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "A customer insists on a contract clause giving it the right to inspect and review the "
                "vendor's security controls, policies, and records during the term of the agreement. "
                "Which clause is this?",
        "options": [
            {"id": "A", "text": "Right-to-audit clause"},
            {"id": "B", "text": "Non-disclosure agreement (NDA)"},
            {"id": "C", "text": "Service-level agreement (SLA)"},
            {"id": "D", "text": "Memorandum of understanding (MOU)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A right-to-audit clause contractually grants the customer the ability to examine the "
                       "vendor's security posture and evidence during the relationship — key for ongoing vendor assurance.",
            "distractors": {
                "B": "An NDA governs confidentiality of shared information; it does not grant inspection rights.",
                "C": "An SLA defines service metrics/penalties, not the right to audit controls.",
                "D": "An MOU expresses intent between parties; it is not an inspection right.",
            },
            "exam_pattern": "Vendor assurance evidence: right-to-audit clause, independent assessments (SOC 2), "
                            "evidence of internal audits, penetration tests, supply-chain analysis.",
        },
    },
    {
        "id": "secplus-mgmt-111", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Before signing with a new hardware supplier, a company researches the supplier's financial "
                "stability, security practices, reputation, and its own sub-suppliers. During vendor "
                "selection, this activity is BEST described as:",
        "options": [
            {"id": "A", "text": "Due diligence"},
            {"id": "B", "text": "Conflict of interest"},
            {"id": "C", "text": "Rules of engagement"},
            {"id": "D", "text": "Right-to-audit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Due diligence is the investigative homework performed before engaging a vendor — assessing "
                       "finances, security, reputation, and the supply chain behind them.",
            "distractors": {
                "B": "A conflict of interest is a bias that could taint selection (e.g., a reviewer with a stake "
                     "in the vendor), not the investigative process itself.",
                "C": "Rules of engagement define the scope/constraints of a penetration test, not vendor vetting.",
                "D": "Right-to-audit is a later contract clause for ongoing oversight, not pre-selection research.",
            },
            "exam_pattern": "Vendor SELECTION = due diligence + watch for conflicts of interest. Supply-chain "
                            "analysis is part of due diligence.",
        },
    },
    {
        "id": "secplus-mgmt-112", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 3, "type": "multi",
        "stem": "A security team already works with a critical SaaS vendor and wants to establish ONGOING "
                "third-party risk MONITORING (as opposed to one-time onboarding checks). Which TWO of the "
                "following are forms of ongoing monitoring? (Choose two.)",
        "options": [
            {"id": "A", "text": "Sending the vendor periodic security questionnaires"},
            {"id": "B", "text": "Reviewing the vendor's recurring independent audit reports (e.g., annual SOC 2 Type II)"},
            {"id": "C", "text": "Performing the initial financial and background due-diligence check before signing"},
            {"id": "D", "text": "Negotiating the master service agreement terms"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Ongoing monitoring tracks a vendor's posture over time — periodic questionnaires and "
                       "reviewing their recurring independent audit/attestation reports are classic examples.",
            "distractors": {
                "C": "Initial due diligence happens once, during SELECTION/onboarding — it is not ongoing monitoring.",
                "D": "Negotiating the MSA is a one-time onboarding/contracting activity, not continuous monitoring.",
            },
            "exam_pattern": "Separate the vendor lifecycle: selection (due diligence) -> contracting (MSA/SLA) -> "
                            "ONGOING monitoring (questionnaires, recurring independent assessments, right-to-audit).",
        },
    },

    # ----- compliance_privacy ----------------------------------------------
    {
        "id": "secplus-mgmt-113", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Under GDPR, an online retailer decides what customer personal data to collect and why, "
                "then contracts a cloud email service to send marketing messages strictly on the retailer's "
                "instructions. What is the cloud email service's role?",
        "options": [
            {"id": "A", "text": "Data processor"},
            {"id": "B", "text": "Data controller"},
            {"id": "C", "text": "Data subject"},
            {"id": "D", "text": "Data owner"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A processor handles personal data on behalf of, and under the instructions of, the "
                       "controller. The cloud email service only acts as the retailer directs — it is the processor.",
            "distractors": {
                "B": "The controller determines the PURPOSES and MEANS of processing — that is the retailer, not the service.",
                "C": "A data subject is the individual the personal data is about (the customers).",
                "D": "'Data owner' is an internal accountability role, not the GDPR controller/processor distinction asked here.",
            },
            "exam_pattern": "Controller decides why/how (purposes & means); processor acts on the controller's "
                            "instructions. The one who decides is the controller.",
        },
    },
    {
        "id": "secplus-mgmt-114", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A customer submits a formal request under GDPR demanding that a company erase all personal "
                "data it holds about them. Which data-subject right is being exercised?",
        "options": [
            {"id": "A", "text": "Right to be forgotten (right to erasure)"},
            {"id": "B", "text": "Right to data portability"},
            {"id": "C", "text": "Data minimization"},
            {"id": "D", "text": "Right of rectification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The right to be forgotten (erasure) lets a data subject require deletion of their personal "
                       "data when there is no overriding reason to keep it.",
            "distractors": {
                "B": "Data portability is the right to receive one's data in a usable format and move it elsewhere, "
                     "not to delete it.",
                "C": "Data minimization is a principle (collect only what is needed), not a deletion request a subject files.",
                "D": "Rectification is the right to correct inaccurate data, not to erase it.",
            },
            "exam_pattern": "GDPR data-subject rights: erasure (be forgotten) = delete, portability = move, "
                            "rectification = correct, access = see.",
        },
    },
    {
        "id": "secplus-mgmt-115", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 1, "type": "mcq",
        "stem": "A healthcare provider is found to have violated HIPAA, and regulators impose a "
                "$1.5 million monetary penalty. Which consequence of non-compliance is this?",
        "options": [
            {"id": "A", "text": "Fines"},
            {"id": "B", "text": "Reputational damage"},
            {"id": "C", "text": "Loss of license"},
            {"id": "D", "text": "Contractual penalties"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A monetary penalty imposed by a regulator for breaking a law/regulation is a fine — a "
                       "direct financial consequence of non-compliance.",
            "distractors": {
                "B": "Reputational damage is lost trust/brand harm, which is indirect and not a monetary penalty.",
                "C": "Loss of license is revocation of the ability to operate, not a fine.",
                "D": "Contractual penalties arise from breaching an agreement between parties, not a regulator's fine.",
            },
            "exam_pattern": "Non-compliance consequences: fines/sanctions (regulatory $), reputational damage, "
                            "loss of license, contractual impacts. Match the SOURCE of the penalty.",
        },
    },
    {
        "id": "secplus-mgmt-116", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "mcq",
        "stem": "To demonstrate compliance, every employee must read the updated security policy and "
                "digitally sign a statement confirming they have read, understood, and agree to follow it. "
                "This compliance-monitoring practice is BEST called:",
        "options": [
            {"id": "A", "text": "Attestation and acknowledgement"},
            {"id": "B", "text": "Independent external audit"},
            {"id": "C", "text": "Due diligence"},
            {"id": "D", "text": "Data inventory"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Having users formally confirm (sign) that they have read and accept a policy is "
                       "attestation/acknowledgement — a common internal compliance-monitoring method.",
            "distractors": {
                "B": "An external audit is an independent outside party examining controls, not users signing a policy.",
                "C": "Due diligence is investigative homework (e.g., before a vendor engagement), not a signed acknowledgement.",
                "D": "A data inventory catalogs what data the organization holds; it is unrelated to policy sign-off.",
            },
            "exam_pattern": "Compliance monitoring includes attestation/acknowledgement, internal vs external review, "
                            "due care/diligence, and automation. Signed policy = attestation.",
        },
    },

    # ----- audits_assessments ----------------------------------------------
    {
        "id": "secplus-mgmt-117", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "An organization's own security staff periodically examine its controls for policy "
                "compliance and report the findings to the board's audit committee. This is BEST described as:",
        "options": [
            {"id": "A", "text": "An internal audit"},
            {"id": "B", "text": "An external regulatory examination"},
            {"id": "C", "text": "An independent third-party assessment"},
            {"id": "D", "text": "A penetration test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Work performed by the organization's OWN staff and reported to its audit committee is an "
                       "internal audit (internal compliance review / self-assessment).",
            "distractors": {
                "B": "A regulatory examination is conducted by an outside regulator (external), not internal staff.",
                "C": "An independent third-party assessment is performed by an outside firm for objectivity.",
                "D": "A penetration test actively attacks systems to find exploitable weaknesses — a different activity.",
            },
            "exam_pattern": "Internal (own staff, audit committee, self-assessment) vs external (regulators, "
                            "examinations, independent third-party). Who performs it decides the category.",
        },
    },
    {
        "id": "secplus-mgmt-118", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "Early in an authorized penetration test, the tester collects information about the target "
                "only from publicly available sources — WHOIS records, the company website, job postings, "
                "and social media — without sending any packets to the target's systems. This phase is:",
        "options": [
            {"id": "A", "text": "Passive reconnaissance"},
            {"id": "B", "text": "Active reconnaissance"},
            {"id": "C", "text": "Vulnerability scanning"},
            {"id": "D", "text": "Lateral movement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Passive reconnaissance gathers intelligence from third-party/public sources without "
                       "directly interacting with the target, so it leaves no trace on the target's systems.",
            "distractors": {
                "B": "Active reconnaissance DOES touch the target (pings, port scans, banner grabbing) and can be detected.",
                "C": "Vulnerability scanning actively probes systems for weaknesses — it is an active technique.",
                "D": "Lateral movement is pivoting between systems AFTER an initial compromise, not information gathering.",
            },
            "exam_pattern": "Passive recon = no contact with target (OSINT). Active recon = direct interaction "
                            "(scans/probes), potentially detectable.",
        },
    },
    {
        "id": "secplus-mgmt-119", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "A client provides a penetration-testing team with LIMITED information — standard user "
                "credentials and a partial network diagram — but withholds full architecture and source-code "
                "details. Which testing environment is this?",
        "options": [
            {"id": "A", "text": "Partially known (gray-box) environment"},
            {"id": "B", "text": "Unknown (black-box) environment"},
            {"id": "C", "text": "Known (white-box) environment"},
            {"id": "D", "text": "Credentialed vulnerability scan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Partial information up front = partially known (gray-box) testing, balancing realism with "
                       "efficiency by giving the tester a limited foothold of knowledge.",
            "distractors": {
                "B": "Unknown (black-box) gives the tester NO prior information — they must discover everything.",
                "C": "Known (white-box) provides FULL information (architecture, source, configs) up front.",
                "D": "A credentialed scan is automated scanning using valid logins, not an adversarial pen-test engagement.",
            },
            "exam_pattern": "Pen-test knowledge levels: known = white-box (full), partially known = gray-box "
                            "(some), unknown = black-box (none).",
        },
    },
    {
        "id": "secplus-mgmt-120", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 3, "type": "mcq",
        "stem": "An organization runs an exercise in which the offensive team and the defensive team "
                "collaborate and share information in real time to improve detection and response together. "
                "Which type of engagement is this?",
        "options": [
            {"id": "A", "text": "Integrated (purple team)"},
            {"id": "B", "text": "Offensive (red team) only"},
            {"id": "C", "text": "Defensive (blue team) only"},
            {"id": "D", "text": "Unknown-environment test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Integrated testing (purple team) has the attackers and defenders work TOGETHER, sharing "
                       "findings live so defenses improve faster than either side acting alone.",
            "distractors": {
                "B": "A red team (offensive) attacks independently to emulate an adversary, without collaborating with defenders.",
                "C": "A blue team (defensive) defends and responds; on its own it is not the combined exercise described.",
                "D": "Unknown-environment refers to how much INFORMATION the tester has, not to red/blue/purple collaboration.",
            },
            "exam_pattern": "Offensive = red, defensive = blue, integrated = purple (red + blue collaborating).",
        },
    },

    # ----- security_awareness ----------------------------------------------
    {
        "id": "secplus-mgmt-121", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "Security-awareness training teaches employees to notice and report a coworker who "
                "suddenly begins accessing and downloading large volumes of sensitive files unrelated to "
                "their role, often outside business hours. Recognizing this is BEST categorized under which "
                "awareness topic?",
        "options": [
            {"id": "A", "text": "Recognizing anomalous behavior (potential insider threat)"},
            {"id": "B", "text": "Phishing campaign recognition"},
            {"id": "C", "text": "Password management"},
            {"id": "D", "text": "Secure hybrid/remote work"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Unusual, out-of-pattern activity like bulk access to unrelated sensitive data is anomalous "
                       "behavior that may signal an insider threat — a core recognition goal of awareness programs.",
            "distractors": {
                "B": "Phishing recognition is about spotting malicious emails/messages, not a coworker's data-access pattern.",
                "C": "Password management covers strong, unique credentials and managers — unrelated to spotting insider activity.",
                "D": "Secure remote-work guidance covers VPN/device practices, not recognizing anomalous insider behavior.",
            },
            "exam_pattern": "Anomalous-behavior recognition (risky/unexpected/unintentional) trains users to spot and "
                            "report insider-threat indicators.",
        },
    },
    {
        "id": "secplus-mgmt-122", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "A training module instructs staff not to discuss unreleased project details in public, not "
                "to post photos of their access badges or screens on social media, and to consider what small "
                "pieces of information an adversary could aggregate. Which awareness topic does this cover?",
        "options": [
            {"id": "A", "text": "Operational security (OPSEC)"},
            {"id": "B", "text": "Password management"},
            {"id": "C", "text": "Secure disposal of media"},
            {"id": "D", "text": "Change-management procedure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OPSEC teaches users to protect seemingly harmless information that an adversary could piece "
                       "together to harm the organization — exactly the badge/social-media/project-detail guidance.",
            "distractors": {
                "B": "Password management is about credential hygiene, not controlling incidental information disclosure.",
                "C": "Secure media disposal covers destroying data on retired drives/paper, not social-media/OPSEC leakage.",
                "D": "Change management governs approving IT changes, unrelated to information-leakage awareness.",
            },
            "exam_pattern": "OPSEC = protect small, aggregable pieces of information adversaries could combine. A common "
                            "user-training topic alongside social engineering and insider threat.",
        },
    },
    {
        "id": "secplus-mgmt-123", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 2, "type": "mcq",
        "stem": "Employees are trained to stay alert to their physical surroundings — challenging unfamiliar "
                "people who lack a visible badge and never holding a secured door open for someone they do not "
                "recognize. Which user-training topic does this reinforce?",
        "options": [
            {"id": "A", "text": "Situational awareness"},
            {"id": "B", "text": "Password management"},
            {"id": "C", "text": "Phishing recognition"},
            {"id": "D", "text": "Change-management procedure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Being alert to one's surroundings and the people in them — and refusing to enable tailgating — "
                       "is situational awareness applied to physical security.",
            "distractors": {
                "B": "Password management concerns credential hygiene, not physical alertness.",
                "C": "Phishing recognition targets malicious messages, not in-person tailgating.",
                "D": "Change-management procedure governs IT change approval, not physical vigilance.",
            },
            "exam_pattern": "Situational awareness trains users to notice and respond to their physical environment "
                            "(e.g., stopping tailgating/piggybacking at secure doors).",
        },
    },
    {
        "id": "secplus-mgmt-124", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 2, "type": "multi",
        "stem": "An organization is building the hybrid/remote-work section of its security-awareness program. "
                "Which TWO practices SHOULD this module teach employees? (Choose two.)",
        "options": [
            {"id": "A", "text": "Connect through the company VPN when using untrusted or public Wi-Fi"},
            {"id": "B", "text": "Lock the screen when away and keep household members off work devices"},
            {"id": "C", "text": "Disable disk encryption on the laptop to improve performance"},
            {"id": "D", "text": "Share your VPN credentials with a teammate who forgot theirs"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Remote-work guidance should promote VPN use on untrusted networks and basic device discipline "
                       "(screen locking, keeping work devices restricted to the employee) to protect data off-site.",
            "distractors": {
                "C": "Disabling disk encryption removes protection for data at rest if the device is lost or stolen — the opposite of secure practice.",
                "D": "Sharing VPN credentials breaks accountability and authentication and must never be taught as acceptable.",
            },
            "exam_pattern": "Hybrid/remote-work awareness: VPN on untrusted networks, device locking, home-network "
                            "hygiene. Reject anything that weakens encryption or shares credentials.",
        },
    },
]
