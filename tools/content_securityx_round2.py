"""CompTIA SecurityX (CAS-005) pool - ROUND 2 (deepening expansion).

Second-round, original, objective-aligned practice items spanning all four
SecurityX domains (expert/CASP+-level, scenario and trade-off driven). These
items are NEW and NON-DUPLICATE with respect to the round-1 pools
(content_securityx_grc.py / _arch.py / _eng.py / _ops.py): each explores a
fresh angle, technique, or trade-off not already asked, so the combined bank
(~200 items) broadens coverage rather than rewording existing questions.

Distribution mirrors the published CAS-005 domain weighting (Security
Engineering 31% largest, Security Architecture 27%, Security Operations 22%,
Governance/Risk/Compliance 20%):
  * scx_grc           (Domain 1) - 25 items, ids securityx-grc-r2-###
  * scx_architecture  (Domain 2) - 34 items, ids securityx-arch-r2-###
  * scx_engineering   (Domain 3) - 40 items, ids securityx-eng-r2-###
  * scx_operations    (Domain 4) - 28 items, ids securityx-ops-r2-###

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer key is NOT positionally
biased (keys are spread across A-D on purpose), every wrong option carries a
distractor note, and each item cites the public CAS-005 objective domain it
draws on so facts stay traceable. Version-specific facts (CVSS v4.0 metric
groups, NIST CSF 2.0 functions, FIPS 203/204/205 post-quantum standards,
NIST SP 800-207 zero trust, NIST AI RMF) were web-verified during authoring.
Expert depth (BEST-given-constraints, architecture/risk trade-offs) - never
real or memorized exam items.
"""

QUESTIONS = [
    # ================= DOMAIN 1: GOVERNANCE, RISK, AND COMPLIANCE ============
    # ===== scx_risk_management ==============================================
    {
        "id": "securityx-grc-r2-001", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "A control is being evaluated against a risk whose single loss expectancy is $50,000 and whose "
                "annualized rate of occurrence is 2.0 (ALE = $100,000). The proposed control would cut the ARO to "
                "0.5 (ALE = $25,000) but costs $40,000 per year to run. Using cost-benefit analysis, what is the "
                "net annual value of deploying the control?",
        "options": [
            {"id": "A", "text": "$75,000"},
            {"id": "B", "text": "$35,000"},
            {"id": "C", "text": "$60,000"},
            {"id": "D", "text": "$25,000"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Value of a safeguard = (ALE before - ALE after) - annual cost of the control = "
                       "($100,000 - $25,000) - $40,000 = $75,000 - $40,000 = $35,000 net benefit, so the control is cost-justified.",
            "distractors": {
                "A": "$75,000 is the gross risk reduction (ALE before - ALE after) before subtracting the $40,000 annual cost of the control.",
                "C": "$60,000 would be ALE-before minus the control cost ($100,000 - $40,000); it ignores the $25,000 of residual ALE that remains.",
                "D": "$25,000 is the residual ALE after the control, not the net value of deploying it.",
            },
            "exam_pattern": "Safeguard value = (ALE_before - ALE_after) - annual control cost; a positive result means the control is cost-justified.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (cost-benefit analysis, ALE reduction vs safeguard cost)"],
    },
    {
        "id": "securityx-grc-r2-002", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A startup must assess risk to a brand-new product line for which no historical loss data, asset "
                "valuations, or occurrence rates exist. Leadership needs a defensible way to rank risks quickly for "
                "a board meeting next week. Which assessment approach is MOST appropriate given these constraints?",
        "options": [
            {"id": "A", "text": "A fully quantitative analysis computing SLE, ARO, and ALE for each risk"},
            {"id": "B", "text": "A qualitative assessment using a likelihood-versus-impact risk matrix (heat map) with defined rating scales"},
            {"id": "C", "text": "Skip assessment and accept all risks until data accumulates"},
            {"id": "D", "text": "An actuarial Monte Carlo simulation of financial loss distributions"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "With no reliable numeric data and a short timeline, a qualitative likelihood x impact matrix "
                       "with agreed rating scales lets stakeholders rank and communicate risks quickly without inventing false precision.",
            "distractors": {
                "A": "Quantitative analysis needs credible asset values and occurrence rates, which do not exist for a brand-new product line.",
                "C": "Blanket acceptance abdicates risk management and gives the board nothing to decide on.",
                "D": "Monte Carlo simulation requires probability distributions derived from data the startup does not have, and is heavier than the timeline allows.",
            },
            "exam_pattern": "No reliable numeric data + need speed -> qualitative (heat map); quantitative needs defensible $ and ARO figures.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (qualitative vs quantitative assessment)"],
    },
    {
        "id": "securityx-grc-r2-003", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A bank evaluates launching a cryptocurrency custody service. Analysis shows the regulatory and "
                "security risk exceeds the firm's risk appetite and cannot be sufficiently mitigated at acceptable "
                "cost, so leadership decides not to offer the service at all. Which risk-treatment strategy is this?",
        "options": [
            {"id": "A", "text": "Risk acceptance"},
            {"id": "B", "text": "Risk transference"},
            {"id": "C", "text": "Risk avoidance"},
            {"id": "D", "text": "Risk mitigation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Choosing not to engage in the risky activity at all - eliminating the exposure by not launching "
                       "the service - is risk avoidance.",
            "distractors": {
                "A": "Acceptance means proceeding and absorbing the risk; here the firm declines to proceed.",
                "B": "Transference shifts financial impact to a third party (e.g., insurance) while still performing the activity.",
                "D": "Mitigation reduces likelihood or impact with controls while still undertaking the activity; the firm instead forgoes it entirely.",
            },
            "exam_pattern": "Don't do the risky activity at all = avoidance; proceed-with-controls = mitigation; proceed-and-absorb = acceptance; offload loss = transference.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (risk response: avoidance)"],
    },
    {
        "id": "securityx-grc-r2-004", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "A CISO wants a structured, quantitative model to express cyber risk to executives in financial "
                "terms by decomposing it into factors such as loss event frequency and loss magnitude, rather than "
                "using ordinal high/medium/low ratings. Which framework is purpose-built for this?",
        "options": [
            {"id": "A", "text": "FAIR (Factor Analysis of Information Risk)"},
            {"id": "B", "text": "The MITRE ATT&CK framework"},
            {"id": "C", "text": "The OWASP Application Security Verification Standard"},
            {"id": "D", "text": "The Cyber Kill Chain"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FAIR is a quantitative risk-analysis model that decomposes risk into loss event frequency and "
                       "loss magnitude (and their sub-factors), expressing risk as a probable financial loss range for better executive decision-making.",
            "distractors": {
                "B": "MITRE ATT&CK catalogs adversary tactics and techniques; it is not a financial risk-quantification model.",
                "C": "OWASP ASVS defines application security verification requirements, not enterprise risk quantification.",
                "D": "The Cyber Kill Chain models intrusion phases, not financial risk factoring.",
            },
            "exam_pattern": "Quantify risk in dollars via loss frequency x magnitude = FAIR; ATT&CK/Kill Chain = adversary behavior, not risk math.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (quantitative risk models, FAIR)"],
    },
    {
        "id": "securityx-grc-r2-005", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the three-letter acronym: A metric that acts as an early-warning signal "
                "that risk exposure is increasing (for example, a rising percentage of unpatched critical systems "
                "trending toward a defined threshold) is called a key risk indicator, abbreviated ______.",
        "correct": ["kri"],
        "explanation": {
            "correct": "A KRI (key risk indicator) is a forward-looking metric that signals changing risk exposure "
                       "against a threshold, letting leadership act before a KPI (performance outcome) degrades or a loss occurs.",
            "distractors": {},
            "exam_pattern": "Leading signal that risk is rising = KRI; KPI measures performance/outcome achieved.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (key risk indicators, risk monitoring)"],
    },

    # ===== scx_compliance_frameworks ========================================
    {
        "id": "securityx-grc-r2-006", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise adopting NIST Cybersecurity Framework (CSF) 2.0 notices it adds a function absent "
                "from the original five (Identify, Protect, Detect, Respond, Recover). Which function did CSF 2.0 "
                "add, and what is its purpose?",
        "options": [
            {"id": "A", "text": "Govern - establishing and monitoring the organization's cybersecurity risk-management strategy, expectations, roles, and policy"},
            {"id": "B", "text": "Encrypt - mandating cryptographic controls for all data"},
            {"id": "C", "text": "Audit - requiring annual third-party certification"},
            {"id": "D", "text": "Automate - requiring SOAR for all response actions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CSF 2.0 (published February 2024) added the Govern function, which sets and oversees the "
                       "cyber-risk strategy, roles/responsibilities, policy, and oversight that inform the other five functions; it also broadened the framework's scope to all organizations, not just critical infrastructure.",
            "distractors": {
                "B": "'Encrypt' is not a CSF function; cryptography appears as outcomes within Protect, not a top-level function.",
                "C": "CSF is a voluntary outcome-based framework; it adds no mandatory certification function.",
                "D": "'Automate' is not a CSF function; CSF 2.0 added Govern, not an automation mandate.",
            },
            "exam_pattern": "CSF 2.0 = 6 functions; the new one is Govern (strategy/oversight wrapping Identify-Protect-Detect-Respond-Recover).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (NIST CSF 2.0, Govern function)"],
    },
    {
        "id": "securityx-grc-r2-007", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "A retailer wants to shrink the cost and scope of its annual PCI DSS assessment. Most of its "
                "corporate network never stores, processes, or transmits cardholder data, yet it currently sits in "
                "the same flat network as the point-of-sale systems. Which action MOST effectively reduces PCI DSS scope?",
        "options": [
            {"id": "A", "text": "Encrypt all corporate email"},
            {"id": "B", "text": "Network segmentation that isolates the cardholder data environment (CDE) from out-of-scope systems"},
            {"id": "C", "text": "Purchase cyber-liability insurance covering card-breach fines"},
            {"id": "D", "text": "Increase the password length policy company-wide"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "PCI DSS scope includes all systems in or connected to the cardholder data environment. "
                       "Effective network segmentation that isolates the CDE removes properly separated systems from scope, reducing assessment effort and cost (segmentation is explicitly recognized by PCI DSS as a scope-reduction method).",
            "distractors": {
                "A": "Encrypting corporate email does not isolate the CDE or remove systems from PCI scope.",
                "C": "Insurance transfers some financial impact but does not reduce the technical assessment scope.",
                "D": "Longer passwords strengthen one control but do not segment the network or reduce the set of in-scope systems.",
            },
            "exam_pattern": "Shrink PCI DSS scope -> segment/isolate the CDE so unrelated systems are provably out of scope.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (PCI DSS scope reduction via segmentation)"],
    },
    {
        "id": "securityx-grc-r2-008", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "A defense contractor must demonstrate it protects Controlled Unclassified Information (CUI) to win "
                "U.S. Department of Defense contracts, with security requirements drawn from NIST SP 800-171 and "
                "verified through tiered, independent assessment. Which program governs this requirement?",
        "options": [
            {"id": "A", "text": "FedRAMP"},
            {"id": "B", "text": "PCI DSS"},
            {"id": "C", "text": "CMMC (Cybersecurity Maturity Model Certification)"},
            {"id": "D", "text": "SOC 2"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "CMMC is the DoD program that verifies defense-industrial-base contractors protect CUI (and FCI) "
                       "using NIST SP 800-171-based requirements, assessed at tiered maturity levels with third-party or government verification.",
            "distractors": {
                "A": "FedRAMP authorizes cloud service providers for federal agency use (NIST SP 800-53), not DIB contractor CUI protection.",
                "B": "PCI DSS protects payment-card data, unrelated to DoD CUI.",
                "D": "SOC 2 is a service-organization attestation against the Trust Services Criteria, not the DoD's CUI certification program.",
            },
            "exam_pattern": "DoD contractors + CUI + NIST 800-171 + tiered certification = CMMC; FedRAMP = federal cloud authorization (800-53).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (CMMC, NIST SP 800-171, CUI)"],
    },
    {
        "id": "securityx-grc-r2-009", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "A U.S. hospital network must comply with the HIPAA Security Rule for electronic protected health "
                "information (ePHI). The Security Rule requires safeguards in which three categories?",
        "options": [
            {"id": "A", "text": "Administrative, physical, and technical safeguards"},
            {"id": "B", "text": "Preventive, detective, and corrective safeguards"},
            {"id": "C", "text": "Confidentiality, integrity, and availability safeguards"},
            {"id": "D", "text": "Strategic, operational, and tactical safeguards"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The HIPAA Security Rule organizes required and addressable safeguards for ePHI into three "
                       "categories: administrative (e.g., risk analysis, workforce training), physical (e.g., facility access), and technical (e.g., access control, audit, encryption).",
            "distractors": {
                "B": "Preventive/detective/corrective are general control-function types, not the HIPAA Security Rule's safeguard categories.",
                "C": "CIA is the security objective triad, not the Security Rule's safeguard structure (though safeguards support CIA).",
                "D": "Strategic/operational/tactical describe planning levels, not HIPAA safeguard categories.",
            },
            "exam_pattern": "HIPAA Security Rule safeguards = administrative + physical + technical (for ePHI).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (HIPAA Security Rule safeguards)"],
    },
    {
        "id": "securityx-grc-r2-010", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "A publicly traded U.S. company must ensure the integrity and accuracy of its financial reporting, "
                "including IT general controls over the systems that produce financial statements, with executive "
                "sign-off on control effectiveness. Which regulation is the primary driver?",
        "options": [
            {"id": "A", "text": "GLBA (Gramm-Leach-Bliley Act)"},
            {"id": "B", "text": "SOX (Sarbanes-Oxley Act)"},
            {"id": "C", "text": "GDPR"},
            {"id": "D", "text": "FERPA"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Sarbanes-Oxley (SOX) mandates accurate financial reporting and internal controls over "
                       "financial reporting for U.S. public companies, including IT general controls, with executive (CEO/CFO) certification of their effectiveness.",
            "distractors": {
                "A": "GLBA governs the privacy and protection of consumers' financial information at financial institutions, not financial-statement reporting integrity.",
                "C": "GDPR regulates personal data of EU data subjects, not corporate financial reporting controls.",
                "D": "FERPA protects the privacy of student education records, unrelated to financial reporting.",
            },
            "exam_pattern": "Public-company financial-reporting integrity + ITGC + executive certification = SOX.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (SOX, IT general controls)"],
    },

    # ===== scx_governance_policies ==========================================
    {
        "id": "securityx-grc-r2-011", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a single signed document that tells employees what they may and may not do with "
                "corporate systems, email, and internet access - and that it can point to when disciplining misuse. "
                "Which document BEST fills this need?",
        "options": [
            {"id": "A", "text": "A business impact analysis (BIA)"},
            {"id": "B", "text": "An acceptable use policy (AUP)"},
            {"id": "C", "text": "A service-level agreement (SLA)"},
            {"id": "D", "text": "A disaster recovery plan (DRP)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An acceptable use policy defines permitted and prohibited use of organizational systems and "
                       "resources; employees typically acknowledge it, giving the organization a basis to enforce consequences for misuse.",
            "distractors": {
                "A": "A BIA identifies critical processes and impacts of disruption; it is not a user-conduct policy.",
                "C": "An SLA sets service performance commitments between parties, not employee usage rules.",
                "D": "A DRP details how to recover IT after a disaster, not acceptable user behavior.",
            },
            "exam_pattern": "Rules for how users may use IT resources, signed/acknowledged = AUP.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (acceptable use policy)"],
    },
    {
        "id": "securityx-grc-r2-012", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 3, "type": "mcq",
        "stem": "A business unit cannot meet a mandatory encryption standard for a legacy system before a hard "
                "deadline. Which governance mechanism is the CORRECT way to proceed while maintaining accountability?",
        "options": [
            {"id": "A", "text": "Quietly ignore the standard until the system is retired"},
            {"id": "B", "text": "A formal policy exception/waiver documenting the gap, compensating controls, a remediation timeline, and risk-owner acceptance sign-off"},
            {"id": "C", "text": "Permanently lower the organization-wide encryption standard so nothing is non-compliant"},
            {"id": "D", "text": "Delete the audit finding from the risk register"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A documented exception/waiver records the deviation, the compensating controls reducing interim "
                       "risk, a remediation plan with dates, and formal risk acceptance by the accountable owner - preserving governance and auditability.",
            "distractors": {
                "A": "Silently ignoring a standard removes accountability and oversight and likely breaches policy/audit requirements.",
                "C": "Lowering the standard for everyone to mask one system's gap weakens security broadly and is not a targeted, time-bound exception.",
                "D": "Deleting the finding conceals risk and undermines the integrity of the risk register.",
            },
            "exam_pattern": "Can't meet a standard -> formal, time-bound exception with compensating controls + risk-owner sign-off, not silent non-compliance.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (policy exceptions/waivers, risk acceptance)"],
    },
    {
        "id": "securityx-grc-r2-013", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 3, "type": "mcq",
        "stem": "After selecting a vendor, an organization continues to apply ongoing, reasonable security measures "
                "and monitoring expected of a prudent operator to protect the data it is responsible for. Which "
                "principle does this ongoing, prudent-person effort represent?",
        "options": [
            {"id": "A", "text": "Due diligence"},
            {"id": "B", "text": "Due care"},
            {"id": "C", "text": "Separation of duties"},
            {"id": "D", "text": "Least privilege"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Due care is the ongoing exercise of reasonable, prudent protection and oversight (the "
                       "'prudent person' standard) once a decision is made; due diligence is the up-front investigation that informs the decision.",
            "distractors": {
                "A": "Due diligence is the prior investigative homework (e.g., vetting the vendor), not the ongoing protective effort afterward.",
                "C": "Separation of duties splits incompatible tasks among people to curb fraud, a different control.",
                "D": "Least privilege limits access rights to the minimum needed, not the standard of ongoing prudent care.",
            },
            "exam_pattern": "Due diligence = investigate before (homework); due care = act prudently/continuously after (the ongoing effort).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (due care vs due diligence)"],
    },
    {
        "id": "securityx-grc-r2-014", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 3, "type": "mcq",
        "stem": "A bank requires finance employees to take at least five consecutive business days of vacation each "
                "year, during which another employee performs their duties. From a controls standpoint, this practice "
                "functions primarily as which type of control?",
        "options": [
            {"id": "A", "text": "A preventive control that stops fraud from occurring"},
            {"id": "B", "text": "A detective control that surfaces fraud or errors concealed by ongoing activity"},
            {"id": "C", "text": "A physical control protecting the facility"},
            {"id": "D", "text": "A deterrent control that only discourages policy violations"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mandatory vacation is chiefly a detective control: when someone else must cover the role, "
                       "schemes that require the perpetrator's continuous presence to hide (e.g., rolling fraud) tend to surface. It also has deterrent value, but its primary control function is detection.",
            "distractors": {
                "A": "It does not technically prevent fraud from happening; it reveals concealed activity after the fact.",
                "C": "It is an administrative/personnel control, not a physical one.",
                "D": "Deterrence is a secondary effect; the recognized primary purpose is detecting concealed fraud/errors.",
            },
            "exam_pattern": "Mandatory vacation / job rotation = primarily detective (uncovers hidden fraud), with deterrent side effect.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (personnel controls, control functions)"],
    },
    {
        "id": "securityx-grc-r2-015", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 2, "type": "mcq",
        "stem": "An auditor asks the security team to classify its controls by the CompTIA control-category model. "
                "A security guard at the lobby, a visitor sign-in log, and bollards outside the entrance are BEST "
                "categorized as which control category?",
        "options": [
            {"id": "A", "text": "Technical controls"},
            {"id": "B", "text": "Managerial controls"},
            {"id": "C", "text": "Physical controls"},
            {"id": "D", "text": "Operational controls"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Guards, sign-in logs at a physical entrance, and bollards act on the physical environment to "
                       "protect people and facilities, so they are physical controls (by category). Note a control's category - what it acts on - is distinct from its function (deterrent/preventive/detective/etc.).",
            "distractors": {
                "A": "Technical (logical) controls are implemented in hardware/software/firmware (e.g., firewalls, encryption), not guards or bollards.",
                "B": "Managerial controls are administrative/policy and risk-management activities (policies, risk assessments), not physical barriers.",
                "D": "Operational controls are processes executed by people (e.g., awareness training, change management), distinct from physical barriers.",
            },
            "exam_pattern": "Category = what the control acts on: managerial (policy), operational (people/process), technical (tech), physical (world).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (control categories: managerial/operational/technical/physical)"],
    },

    # ===== scx_third_party_risk =============================================
    {
        "id": "securityx-grc-r2-016", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 3, "type": "mcq",
        "stem": "A company and a strategic supplier expect many projects over several years. They want to negotiate "
                "overarching legal terms (liability, IP, security requirements, confidentiality) ONCE, then define "
                "each project's specific deliverables, timelines, and prices in separate, lightweight documents. "
                "Which pairing of agreement types BEST fits?",
        "options": [
            {"id": "A", "text": "A master service agreement (MSA) for the overarching terms, with per-project statements of work (SOWs)"},
            {"id": "B", "text": "A non-disclosure agreement (NDA) for the overarching terms, with per-project MOUs"},
            {"id": "C", "text": "A service-level agreement (SLA) for the overarching terms, with per-project NDAs"},
            {"id": "D", "text": "A business partnership agreement (BPA) for the overarching terms, with per-project SLAs"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An MSA establishes the master legal/commercial terms that govern the whole relationship, while "
                       "each engagement's specific scope, deliverables, schedule, and price are captured in a statement of work (SOW) that references the MSA - exactly the negotiate-once, execute-many pattern.",
            "distractors": {
                "B": "An NDA only covers confidentiality, not the full commercial terms; an MOU is typically non-binding intent, not enforceable deliverables.",
                "C": "An SLA defines service-performance metrics, not the master legal framework; NDAs do not define deliverables.",
                "D": "A BPA governs a partnership's profit/responsibility sharing; SLAs define performance metrics, not per-project deliverables/scope.",
            },
            "exam_pattern": "Negotiate master terms once (MSA) + define each project's scope/deliverables (SOW).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (agreement types: MSA, SOW)"],
    },
    {
        "id": "securityx-grc-r2-017", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 3, "type": "mcq",
        "stem": "After a software supplier's build system was compromised and shipped a trojanized update to "
                "customers, a security team wants assurance that future vendor artifacts are authentic and built from "
                "the expected source with a tamper-evident record of how they were produced. Which combination BEST "
                "addresses this supply-chain integrity goal?",
        "options": [
            {"id": "A", "text": "Rely on the vendor's marketing claims of security"},
            {"id": "B", "text": "Verify code-signing signatures on artifacts plus build provenance/attestations (e.g., SLSA) and an SBOM for each release"},
            {"id": "C", "text": "Scan the vendor's public website with a vulnerability scanner"},
            {"id": "D", "text": "Require the vendor to carry more cyber-insurance"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Authenticity and build integrity come from verifying code-signing signatures, consuming signed "
                       "build provenance/attestations (e.g., the SLSA framework) that prove what source and pipeline produced the artifact, and reviewing an SBOM - together making tampering detectable.",
            "distractors": {
                "A": "Marketing claims are not verifiable assurance of artifact integrity.",
                "C": "Scanning the website does not attest to how shipped software artifacts were built or whether they were tampered with.",
                "D": "Insurance transfers some financial loss but does nothing to verify artifact authenticity or build provenance.",
            },
            "exam_pattern": "Trojanized-update/build compromise -> code signing + build provenance/attestation (SLSA) + SBOM to verify authenticity and integrity.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party/supply-chain risk (code signing, build provenance/SLSA, SBOM)"],
    },
    {
        "id": "securityx-grc-r2-018", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 3, "type": "mcq",
        "stem": "Before signing with a SaaS vendor, legal and security want to ensure the company can retrieve its "
                "data in a usable, standard format and migrate away if the vendor fails, raises prices, or is "
                "acquired - avoiding being trapped. Which contractual consideration MOST directly addresses this?",
        "options": [
            {"id": "A", "text": "A right-to-audit clause"},
            {"id": "B", "text": "A data portability and exit (off-boarding) strategy addressing vendor lock-in"},
            {"id": "C", "text": "A mutual non-disclosure agreement"},
            {"id": "D", "text": "A uptime service-level agreement"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defining data portability (export in standard formats), transition assistance, and an exit "
                       "strategy up front mitigates vendor lock-in, so the organization can move providers or bring the service in-house without being held hostage.",
            "distractors": {
                "A": "A right-to-audit clause enables inspecting the vendor's controls, but does not ensure data retrievability or a clean exit.",
                "C": "An NDA protects confidentiality; it does not guarantee data portability or migration.",
                "D": "An uptime SLA governs availability performance, not the ability to exit and take your data.",
            },
            "exam_pattern": "Avoid being trapped by a vendor -> plan data portability + exit strategy (lock-in mitigation) before signing.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (vendor lock-in, data portability, exit strategy)"],
    },
    {
        "id": "securityx-grc-r2-019", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "A vendor announces that a widely used appliance has reached end-of-service-life (EOSL): no more "
                "security patches will ever be released, but the business still depends on it. Which statement BEST "
                "captures the risk and the appropriate governance response?",
        "options": [
            {"id": "A", "text": "EOSL is purely a budgeting concern with no security impact"},
            {"id": "B", "text": "Newly discovered vulnerabilities will go unpatched forever, so the organization must plan replacement and, in the interim, isolate/compensate and formally accept the residual risk"},
            {"id": "C", "text": "The appliance becomes more secure after EOSL because attackers lose interest"},
            {"id": "D", "text": "A support contract renewal will automatically restore patches"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "After EOSL the vendor issues no further security fixes, so any new vulnerability is permanently "
                       "exposed. Governance requires a replacement/migration plan and, until then, compensating controls (isolation, monitoring, restricted access) with documented risk acceptance.",
            "distractors": {
                "A": "Unpatched, internet-reachable or critical systems carry real and growing security risk, not just cost.",
                "C": "Lack of patches makes systems more vulnerable over time; attacker interest in widely deployed legacy gear often rises.",
                "D": "EOSL means support/patching has ended; renewal is generally unavailable or does not restore security updates.",
            },
            "exam_pattern": "EOL/EOSL = no more patches -> plan replacement + isolate/compensate + formal risk acceptance in the interim.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (end-of-life/EOSL unsupported software)"],
    },
    {
        "id": "securityx-grc-r2-020", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 3, "type": "multi",
        "stem": "A manufacturer of safety-critical hardware is worried about counterfeit or tampered components "
                "entering its product through the hardware supply chain. Which TWO controls MOST directly reduce "
                "hardware supply-chain tampering/counterfeiting risk? (Choose two.)",
        "options": [
            {"id": "A", "text": "Source components only through authorized/trusted suppliers and verify provenance (anti-counterfeit authentication, tamper-evident packaging)"},
            {"id": "B", "text": "Buy the cheapest components available on open gray markets to cut costs"},
            {"id": "C", "text": "Validate device integrity with hardware roots of trust and signed/attested firmware before deployment"},
            {"id": "D", "text": "Disable all logging on the manufacturing line to improve throughput"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Buying from authorized suppliers with verified provenance and tamper-evident controls reduces "
                       "the chance counterfeit/tampered parts enter, and validating integrity via hardware roots of trust and signed/attested firmware detects tampering before devices are trusted and deployed.",
            "distractors": {
                "B": "Gray-market sourcing is a primary vector for counterfeit and tampered components - it increases risk.",
                "D": "Disabling manufacturing-line logging removes the visibility needed to detect and investigate tampering.",
            },
            "exam_pattern": "Hardware supply chain -> trusted/authorized sourcing + provenance/tamper-evidence + hardware root-of-trust/firmware attestation.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party/supply-chain risk (hardware provenance, counterfeit, root of trust)"],
    },

    # ===== scx_data_governance ==============================================
    {
        "id": "securityx-grc-r2-021", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 2, "type": "mcq",
        "stem": "An organization is rolling out a four-tier data classification scheme (Public, Internal, "
                "Confidential, Restricted). When a new dataset is created, who is responsible for assigning its "
                "classification level?",
        "options": [
            {"id": "A", "text": "The data custodian who runs the storage systems"},
            {"id": "B", "text": "The data owner (the accountable business leader for that data)"},
            {"id": "C", "text": "The end users who read the data"},
            {"id": "D", "text": "The external auditor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The data owner - the senior/business role accountable for a data asset - determines its "
                       "classification and the protection requirements; custodians then implement the controls that the classification demands.",
            "distractors": {
                "A": "The custodian maintains and protects the data per the owner's direction (implements backups, access, encryption) but does not set the classification.",
                "C": "End users consume data within granted permissions; they do not assign classification.",
                "D": "Auditors assess whether classification and controls are applied correctly; they do not own or assign the classification.",
            },
            "exam_pattern": "Owner (accountable) classifies and sets requirements; custodian (hands-on) implements protection.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (classification, data owner responsibilities)"],
    },
    {
        "id": "securityx-grc-r2-022", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 3, "type": "mcq",
        "stem": "A research team wants to analyze customer datasets while reducing privacy risk. In Technique X, "
                "direct identifiers are replaced with reversible tokens so records can be re-linked via a separately "
                "held key; in Technique Y, identifiers are irreversibly removed so individuals can no longer be "
                "re-identified. Under GDPR, which statement is correct?",
        "options": [
            {"id": "A", "text": "Technique X is anonymization and falls outside GDPR; Technique Y is pseudonymization and remains personal data"},
            {"id": "B", "text": "Technique X is pseudonymization and remains personal data under GDPR; Technique Y is anonymization and, if truly irreversible, falls outside GDPR's scope"},
            {"id": "C", "text": "Both are anonymization and both fall outside GDPR"},
            {"id": "D", "text": "Both are pseudonymization and both fall outside GDPR"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Reversible replacement with a separately held key is pseudonymization; because re-identification "
                       "is still possible, GDPR treats pseudonymized data as personal data. Truly irreversible anonymization removes the ability to re-identify, so genuinely anonymized data is outside GDPR's scope.",
            "distractors": {
                "A": "This reverses the definitions - reversible-with-key is pseudonymization, not anonymization.",
                "C": "Reversible tokenization keyed to a secret is pseudonymization and stays in scope; it is not anonymization.",
                "D": "Irreversible removal is anonymization, not pseudonymization; the two differ in reversibility and legal scope.",
            },
            "exam_pattern": "Pseudonymization = reversible (keyed) -> still personal data under GDPR; anonymization = irreversible -> outside GDPR (if truly non-re-identifiable).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (pseudonymization vs anonymization, GDPR)"],
    },
    {
        "id": "securityx-grc-r2-023", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 2, "type": "mcq",
        "stem": "In a data-governance RACI, one role is accountable for data quality, definitions, and appropriate "
                "use within a business domain - acting as the liaison between business and IT - without necessarily "
                "owning or operating the storage. Which role is this?",
        "options": [
            {"id": "A", "text": "Data steward"},
            {"id": "B", "text": "Data custodian"},
            {"id": "C", "text": "Data processor"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A data steward manages data quality, metadata/definitions, and appropriate use within a domain, "
                       "bridging business and technical teams and enforcing the owner's policies day to day.",
            "distractors": {
                "B": "A custodian provides technical safekeeping (storage, backups, access enforcement), not business-level quality/definition stewardship.",
                "C": "A processor (GDPR) processes personal data on a controller's behalf - a legal/privacy role, not internal data-quality stewardship.",
                "D": "A data subject is the individual the personal data is about, not a governance role.",
            },
            "exam_pattern": "Steward = data quality/definitions/appropriate-use liaison; custodian = technical safekeeping; owner = accountable classifier.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (data roles: steward vs custodian)"],
    },
    {
        "id": "securityx-grc-r2-024", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 3, "type": "mcq",
        "stem": "A retention schedule requires that customer records be irrecoverably destroyed at end of life. The "
                "data is spread across multi-tenant cloud storage and SSDs where physical destruction and reliable "
                "overwriting are impractical. Which method BEST assures the data is rendered unrecoverable?",
        "options": [
            {"id": "A", "text": "Move the records to an archive bucket and delete the index"},
            {"id": "B", "text": "Crypto-shredding: encrypt the data at rest and then securely destroy the encryption keys so the ciphertext is unrecoverable"},
            {"id": "C", "text": "Degauss the cloud provider's drives"},
            {"id": "D", "text": "A single-pass overwrite of the logical file"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Crypto-shredding (cryptographic erasure) destroys the keys that decrypt the data, so the "
                       "remaining ciphertext is computationally unrecoverable - ideal where physical destruction, degaussing, or reliable overwrite are impractical (SSD wear-leveling, multi-tenant cloud).",
            "distractors": {
                "A": "Deleting an index leaves the underlying data recoverable; it is not secure destruction.",
                "C": "Degaussing applies to magnetic media and is not an option you can perform on a cloud provider's drives (and is ineffective on SSDs).",
                "D": "SSD wear-leveling and over-provisioning mean a single logical overwrite may not touch all physical cells, so data can persist.",
            },
            "exam_pattern": "Cloud/SSD secure destruction when physical/overwrite is impractical = crypto-shredding (destroy the keys).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (retention/disposal, cryptographic erasure)"],
    },
    {
        "id": "securityx-grc-r2-025", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 3, "type": "mcq",
        "stem": "A European subsidiary needs to transfer EU residents' personal data to its U.S.-based parent for "
                "processing. Following the invalidation of a prior framework (Schrems II), which mechanism do "
                "organizations MOST commonly rely on to legitimize such cross-border transfers, often paired with a "
                "transfer impact assessment and supplementary safeguards?",
        "options": [
            {"id": "A", "text": "Standard Contractual Clauses (SCCs)"},
            {"id": "B", "text": "A service-level agreement (SLA)"},
            {"id": "C", "text": "A software bill of materials (SBOM)"},
            {"id": "D", "text": "A non-disclosure agreement (NDA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Standard Contractual Clauses are EU-approved contractual terms that provide a lawful basis for "
                       "transferring personal data to third countries; after Schrems II, organizations commonly use SCCs together with a transfer impact assessment and supplementary technical/organizational safeguards (adequacy decisions or BCRs are alternatives).",
            "distractors": {
                "B": "An SLA sets service-performance commitments, not a lawful basis for cross-border personal-data transfer.",
                "C": "An SBOM is a software component inventory, unrelated to data-transfer legality.",
                "D": "An NDA protects confidentiality between parties but is not a recognized GDPR cross-border transfer mechanism.",
            },
            "exam_pattern": "EU-to-third-country transfer, post-Schrems II -> SCCs (+ transfer impact assessment/safeguards); adequacy decision or BCRs as alternatives.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (cross-border transfers, SCCs, data sovereignty)"],
    },

    # ================= DOMAIN 3: SECURITY ENGINEERING =======================
    # ===== scx_cryptography =================================================
    {
        "id": "securityx-eng-r2-001", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "An application must encrypt large files and deliver them to many recipients efficiently, giving "
                "each recipient the ability to decrypt without sharing a secret key out-of-band. Which cryptographic "
                "design BEST meets both the performance and key-distribution needs?",
        "options": [
            {"id": "A", "text": "Encrypt the entire file separately with each recipient's RSA public key"},
            {"id": "B", "text": "Encrypt the file once with a single shared symmetric key manually distributed to all recipients"},
            {"id": "C", "text": "A hybrid cryptosystem: encrypt the file with a random symmetric key (e.g., AES), then encrypt that symmetric key to each recipient's public key"},
            {"id": "D", "text": "Publish a SHA-256 hash of the file to each recipient"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Hybrid encryption uses fast symmetric crypto for the bulk data and asymmetric crypto only to "
                       "wrap the small symmetric key for each recipient - combining symmetric speed with asymmetric key distribution (no out-of-band secret sharing).",
            "distractors": {
                "A": "Asymmetric encryption is slow and size-limited; encrypting large files directly with RSA per recipient is impractical and inefficient.",
                "B": "A single manually distributed shared key creates the classic key-distribution/revocation problem and risks exposure to all if leaked.",
                "D": "A hash provides integrity verification, not confidentiality - it does not encrypt the file.",
            },
            "exam_pattern": "Bulk data + multiple recipients -> hybrid: symmetric key encrypts data, asymmetric wraps the key per recipient.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (hybrid cryptosystem, symmetric vs asymmetric roles)"],
    },
    {
        "id": "securityx-eng-r2-002", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "A developer needs a single symmetric cipher mode that provides BOTH confidentiality and built-in "
                "integrity/authenticity (authenticated encryption), so a tampered ciphertext is detected on "
                "decryption without bolting on a separate MAC. Which choice is BEST?",
        "options": [
            {"id": "A", "text": "AES in ECB mode"},
            {"id": "B", "text": "AES in GCM mode (an AEAD mode)"},
            {"id": "C", "text": "AES in CBC mode with no additional MAC"},
            {"id": "D", "text": "AES in CTR mode with no additional MAC"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "AES-GCM is an AEAD (authenticated encryption with associated data) mode: it provides "
                       "confidentiality and an integrity/authenticity tag in one construction, so tampering is detected on decryption.",
            "distractors": {
                "A": "ECB provides neither integrity nor good confidentiality - identical plaintext blocks yield identical ciphertext, leaking structure.",
                "C": "CBC alone provides confidentiality but no integrity; without a MAC it is vulnerable to tampering/padding-oracle attacks.",
                "D": "CTR alone is a confidentiality-only stream mode; without a MAC it offers no integrity/authenticity.",
            },
            "exam_pattern": "Confidentiality + integrity in one mode = AEAD (AES-GCM / ChaCha20-Poly1305); CBC/CTR need a separate MAC; ECB is unsafe.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (cipher modes, authenticated encryption/AEAD)"],
    },
    {
        "id": "securityx-eng-r2-003", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "A review finds that an application encrypts structured records with AES in ECB mode. The security "
                "engineer flags it as unsafe. What is the PRIMARY weakness of ECB that justifies this?",
        "options": [
            {"id": "A", "text": "Identical plaintext blocks always produce identical ciphertext blocks, revealing patterns/structure in the data"},
            {"id": "B", "text": "ECB uses keys that are too long, slowing performance"},
            {"id": "C", "text": "ECB automatically transmits the key with the ciphertext"},
            {"id": "D", "text": "ECB can only encrypt data smaller than one block"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ECB encrypts each block independently with no IV/chaining, so identical plaintext blocks map to "
                       "identical ciphertext blocks - leaking patterns (the classic 'ECB penguin'). Use a chaining/AEAD mode with a unique IV/nonce instead.",
            "distractors": {
                "B": "Key length is unrelated to ECB's weakness; the flaw is deterministic block mapping, not key size.",
                "C": "ECB does not transmit the key; keys are never embedded by the mode.",
                "D": "ECB handles data of many blocks; its problem is per-block determinism, not a size limit.",
            },
            "exam_pattern": "ECB leaks structure (same plaintext block -> same ciphertext block); prefer AEAD/chaining modes with unique IV/nonce.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (ECB weakness, cipher modes)"],
    },
    {
        "id": "securityx-eng-r2-004", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "A recipient must be able to verify that a message truly came from the claimed sender, was not "
                "altered, and that the sender cannot later deny sending it. Which mechanism provides all three "
                "(authentication, integrity, and non-repudiation)?",
        "options": [
            {"id": "A", "text": "Encrypting the message with the sender's public key"},
            {"id": "B", "text": "An HMAC computed with a key shared between sender and recipient"},
            {"id": "C", "text": "Symmetric encryption of the message with a shared key"},
            {"id": "D", "text": "A digital signature: the sender signs a hash of the message with their private key, and anyone verifies it with the sender's public key"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A digital signature (sign the message hash with the sender's private key; verify with the "
                       "sender's public key) proves authenticity and integrity and provides non-repudiation, since only the holder of the private key could have produced it.",
            "distractors": {
                "A": "Encrypting with the sender's public key is nonsensical for authentication - anyone has that public key, and only the sender's private key could decrypt, providing confidentiality to the sender, not a signature.",
                "B": "HMAC gives integrity and authentication but NOT non-repudiation, because both parties share the same secret key and either could have produced it.",
                "C": "Symmetric encryption with a shared key provides confidentiality (and some integrity with AEAD) but no non-repudiation - the key is shared.",
            },
            "exam_pattern": "Authentication + integrity + non-repudiation = digital signature (sign hash with private key). Shared-secret schemes (HMAC/symmetric) give no non-repudiation.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (digital signatures, non-repudiation)"],
    },
    {
        "id": "securityx-eng-r2-005", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "Two internal services share a secret key and need a fast way to verify that messages between them "
                "are authentic and unmodified. Non-repudiation to outside third parties is explicitly NOT required. "
                "Which mechanism is the BEST fit for these constraints?",
        "options": [
            {"id": "A", "text": "RSA digital signatures on every message"},
            {"id": "B", "text": "An HMAC (hash-based message authentication code) using the shared secret"},
            {"id": "C", "text": "Base64 encoding of each message"},
            {"id": "D", "text": "A CRC32 checksum appended to each message"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "HMAC uses a shared secret with a hash function to provide fast integrity and authenticity "
                       "between parties that already share the key - appropriate when non-repudiation is not needed and signature overhead is undesirable.",
            "distractors": {
                "A": "Digital signatures add non-repudiation and public-key overhead that the scenario explicitly does not need, making them heavier than required.",
                "C": "Base64 is encoding, providing neither integrity nor authenticity.",
                "D": "CRC32 detects accidental transmission errors but is not cryptographic - an attacker can forge messages with matching CRCs.",
            },
            "exam_pattern": "Shared secret + integrity/authenticity, no non-repudiation needed = HMAC; need non-repudiation -> digital signature.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (HMAC vs digital signatures)"],
    },
    {
        "id": "securityx-eng-r2-006", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "A security engineer is selecting NIST-standardized post-quantum algorithms to replace RSA/ECDSA "
                "digital signatures. They want a primary lattice-based signature algorithm plus a conservative "
                "hash-based alternative as a backup in case the lattice assumption is weakened. Which pairing is correct?",
        "options": [
            {"id": "A", "text": "Primary: ML-DSA (FIPS 204); backup: SLH-DSA (FIPS 205, hash-based)"},
            {"id": "B", "text": "Primary: ML-KEM (FIPS 203); backup: AES-256"},
            {"id": "C", "text": "Primary: RSA-4096; backup: ECDSA P-384"},
            {"id": "D", "text": "Primary: SHA-3; backup: HMAC-SHA-256"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ML-DSA (FIPS 204, from CRYSTALS-Dilithium) is NIST's primary post-quantum signature standard; "
                       "SLH-DSA (FIPS 205, from SPHINCS+) is a stateless hash-based signature standard used as a conservative backup that does not rely on lattice assumptions.",
            "distractors": {
                "B": "ML-KEM (FIPS 203) is a key-encapsulation mechanism for key exchange, not a signature algorithm; AES-256 is symmetric encryption, not a signature.",
                "C": "RSA-4096 and ECDSA are classical algorithms broken by Shor's algorithm on a large quantum computer - the very thing being replaced.",
                "D": "SHA-3 and HMAC are hashing/MAC primitives, not digital-signature algorithms.",
            },
            "exam_pattern": "PQC signatures: ML-DSA (FIPS 204) primary (lattice) + SLH-DSA (FIPS 205) hash-based backup; ML-KEM (FIPS 203) is for key exchange.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (post-quantum signatures: FIPS 204 ML-DSA, FIPS 205 SLH-DSA)"],
    },
    {
        "id": "securityx-eng-r2-007", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_cryptography", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Designing systems so that cryptographic algorithms and key sizes can be swapped "
                "out with minimal disruption - essential for migrating to post-quantum algorithms - is known as "
                "cryptographic ______.",
        "correct": ["agility", "crypto-agility", "cryptographic agility"],
        "explanation": {
            "correct": "Cryptographic agility is the ability to replace algorithms, parameters, and keys with minimal "
                       "code/architecture disruption, letting an organization respond quickly as algorithms are deprecated or broken (central to post-quantum migration).",
            "distractors": {},
            "exam_pattern": "Swap crypto algorithms/keys with minimal disruption = crypto-agility (key enabler of PQC migration).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Cryptography (crypto-agility)"],
    },

    # ===== scx_pki ==========================================================
    {
        "id": "securityx-eng-r2-008", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 2, "type": "mcq",
        "stem": "An administrator is requesting a TLS certificate from an internal CA for a new web server. Which "
                "statement correctly describes the certificate-signing request (CSR) process and key handling?",
        "options": [
            {"id": "A", "text": "The CA generates the server's private key and emails it to the administrator"},
            {"id": "B", "text": "The administrator sends the server's private key to the CA so the CA can sign it"},
            {"id": "C", "text": "The server generates a key pair locally; the CSR contains the public key and identity and is signed by the matching private key, which never leaves the server; the CA validates and issues the certificate"},
            {"id": "D", "text": "The administrator creates a self-signed certificate and the CA simply counts it as trusted"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The requester generates the key pair locally, builds a CSR containing the public key and subject "
                       "identity (proving possession by signing it with the private key), and submits it; the CA validates and issues the signed certificate. The private key never leaves the server.",
            "distractors": {
                "A": "A CA generating and emailing private keys defeats key confidentiality; private keys should be generated and kept by the owner.",
                "B": "Private keys must never be sent to the CA - only the public key (in the CSR) is shared.",
                "D": "A self-signed certificate is not CA-validated trust; the CA must actually sign the CSR for the certificate to chain to the CA.",
            },
            "exam_pattern": "CSR carries the PUBLIC key + identity; the private key stays with the requester; the CA validates and signs.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (certificate enrollment, CSR, key handling)"],
    },
    {
        "id": "securityx-eng-r2-009", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 3, "type": "mcq",
        "stem": "A mobile banking app wants to ensure it will only trust its own backend's specific certificate/public "
                "key, so that a fraudulently issued certificate from ANY otherwise-trusted CA cannot enable a "
                "man-in-the-middle attack. Which technique achieves this, and what is its main operational trade-off?",
        "options": [
            {"id": "A", "text": "OCSP stapling; the trade-off is higher CA load"},
            {"id": "B", "text": "Certificate (public-key) pinning; the trade-off is that routine certificate rotation/renewal breaks the app unless pins are updated and managed carefully"},
            {"id": "C", "text": "Enabling HSTS; the trade-off is slower TLS handshakes"},
            {"id": "D", "text": "Using a wildcard certificate; the trade-off is weaker encryption"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Certificate/public-key pinning hard-codes trust in a specific cert or key, so even a rogue "
                       "certificate from a trusted CA is rejected - defeating many MITM scenarios. The trade-off is operational brittleness: when the legitimate certificate/key is rotated, the pins must be updated or clients break.",
            "distractors": {
                "A": "OCSP stapling conveys revocation status efficiently; it does not restrict trust to a specific pinned certificate.",
                "C": "HSTS forces HTTPS and prevents downgrade, but does not pin a specific certificate/key.",
                "D": "A wildcard certificate covers subdomains; it does not pin trust and does not weaken the encryption strength.",
            },
            "exam_pattern": "Trust only our specific cert/key (defeat rogue-CA MITM) = pinning; cost = brittle on rotation/renewal.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (certificate pinning, trade-offs)"],
    },
    {
        "id": "securityx-eng-r2-010", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise encrypts employee laptops and files with per-user keys. Management requires the "
                "ability to recover encrypted business data if an employee leaves abruptly or loses their key. Which "
                "PKI capability provides this while keeping keys protected?",
        "options": [
            {"id": "A", "text": "Key escrow with a designated recovery agent (securely storing a protected copy of the decryption key)"},
            {"id": "B", "text": "Perfect forward secrecy on all sessions"},
            {"id": "C", "text": "Certificate pinning in the email client"},
            {"id": "D", "text": "Shortening certificate validity periods"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Key escrow stores a protected copy of decryption keys (or uses a key-recovery agent) so the "
                       "organization can recover encrypted data when a user is unavailable or a key is lost - balanced with strict controls (e.g., M-of-N) to prevent abuse.",
            "distractors": {
                "B": "Perfect forward secrecy deliberately prevents recovery of past session keys - the opposite of a data-recovery capability.",
                "C": "Certificate pinning restricts which certificate is trusted; it does not recover lost decryption keys.",
                "D": "Shorter validity periods limit exposure of certificates but do not enable recovery of encrypted data.",
            },
            "exam_pattern": "Recover encrypted data when a key/user is lost = key escrow / recovery agent (guard with split-knowledge/M-of-N).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (key escrow, key recovery)"],
    },
    {
        "id": "securityx-eng-r2-011", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 3, "type": "mcq",
        "stem": "A domain owner wants to detect whether ANY certificate authority has mis-issued a certificate for "
                "its domains (for example, a rogue or compromised CA issuing a cert the owner never requested). Which "
                "mechanism is designed to make such mis-issuance publicly detectable?",
        "options": [
            {"id": "A", "text": "A certificate revocation list (CRL)"},
            {"id": "B", "text": "The Online Certificate Status Protocol (OCSP)"},
            {"id": "C", "text": "HTTP Strict Transport Security (HSTS)"},
            {"id": "D", "text": "Certificate Transparency (CT) logs, which publicly record issued certificates for monitoring"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Certificate Transparency requires CAs to publish issued certificates to public, append-only "
                       "logs; domain owners (and monitors) watch these logs to detect certificates issued for their domains that they never requested, exposing mis-issuance.",
            "distractors": {
                "A": "A CRL lists already-revoked certificates; it does not proactively reveal that an unauthorized certificate was issued.",
                "B": "OCSP checks the revocation status of a given certificate; it does not enumerate or surface unexpected issuances.",
                "C": "HSTS forces browsers to use HTTPS; it does not detect certificate mis-issuance.",
            },
            "exam_pattern": "Detect rogue/mis-issued certs for your domain = Certificate Transparency (public append-only logs + monitoring).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (Certificate Transparency, mis-issuance detection)"],
    },
    {
        "id": "securityx-eng-r2-012", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 2, "type": "mcq",
        "stem": "A software company distributes a desktop application and wants users' systems to verify that the "
                "installer genuinely came from the company and has not been modified since it was built. Which type "
                "of certificate is purpose-built for this?",
        "options": [
            {"id": "A", "text": "A TLS/SSL server certificate"},
            {"id": "B", "text": "A code-signing certificate"},
            {"id": "C", "text": "An S/MIME email certificate"},
            {"id": "D", "text": "A client authentication certificate"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A code-signing certificate lets the publisher digitally sign executables/installers; the OS or "
                       "installer verifies the signature to confirm publisher identity and that the binary was not tampered with after signing.",
            "distractors": {
                "A": "A TLS server certificate authenticates a web server for an encrypted session; it does not sign distributed software.",
                "C": "An S/MIME certificate signs/encrypts email, not software binaries.",
                "D": "A client authentication certificate proves a client's identity to a server, not the integrity/authorship of distributed software.",
            },
            "exam_pattern": "Verify software publisher + integrity of a binary = code-signing certificate.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (code-signing certificates)"],
    },
    {
        "id": "securityx-eng-r2-013", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_pki", "difficulty": 3, "type": "mcq",
        "stem": "An architect must choose between a single wildcard certificate (*.example.com) and a multi-SAN "
                "certificate listing specific hostnames, to secure many subdomains. Which statement accurately "
                "captures the security trade-off?",
        "options": [
            {"id": "A", "text": "A wildcard certificate encrypts more strongly than a SAN certificate"},
            {"id": "B", "text": "A SAN certificate cannot be used for more than one hostname"},
            {"id": "C", "text": "A wildcard covers all first-level subdomains with one key, but compromise of that single private key exposes every subdomain; a multi-SAN certificate explicitly lists names, limiting blast radius but requiring reissuance to add names"},
            {"id": "D", "text": "Wildcard certificates cannot be revoked"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A wildcard is convenient - one certificate/key secures all first-level subdomains - but that "
                       "shared private key becomes a single point of compromise affecting every subdomain. A multi-SAN certificate names each host explicitly, containing exposure, at the cost of reissuing when hostnames change.",
            "distractors": {
                "A": "Encryption strength depends on the key/cipher, not whether the certificate is wildcard or SAN.",
                "B": "SAN (subject alternative name) certificates are specifically designed to cover multiple hostnames.",
                "D": "Wildcard certificates can be revoked like any other certificate.",
            },
            "exam_pattern": "Wildcard = convenience but one key, broad blast radius; multi-SAN = explicit names, contained exposure, reissue to change.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — PKI (wildcard vs SAN certificates, blast radius)"],
    },

    # ===== scx_secure_integration ===========================================
    {
        "id": "securityx-eng-r2-014", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "A stateless REST API authenticates requests with JSON Web Tokens (JWTs). Which practice is MOST "
                "critical to prevent token forgery and privilege abuse?",
        "options": [
            {"id": "A", "text": "Verify the token's signature with the expected algorithm/key, reject 'alg: none' and algorithm-confusion, and validate issuer, audience, and expiration claims server-side"},
            {"id": "B", "text": "Trust the algorithm specified in the token's own header so clients can choose what they prefer"},
            {"id": "C", "text": "Issue long-lived tokens with no expiration to reduce re-authentication"},
            {"id": "D", "text": "Store the signing secret in the client application for convenience"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The server must cryptographically verify the JWT signature using the algorithm/key it expects "
                       "(never honoring attacker-controlled 'alg: none' or RS/HS confusion) and validate iss/aud/exp (and scopes) - otherwise tokens can be forged or misused.",
            "distractors": {
                "B": "Trusting the token's own 'alg' header enables 'alg: none' and algorithm-confusion forgery; the server must pin the expected algorithm.",
                "C": "Non-expiring tokens cannot be revoked by expiry and greatly extend the window of abuse if stolen.",
                "D": "Placing the signing secret in the client exposes it, letting anyone mint valid tokens.",
            },
            "exam_pattern": "JWT security = verify signature with expected alg/key, reject alg:none, validate iss/aud/exp, short lifetimes, protect signing keys.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (JWT/token validation, API authentication)"],
    },

    {
        "id": "securityx-eng-r2-015", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "A SaaS platform sends event notifications to customers' public webhook URLs. A customer wants to be "
                "sure an incoming webhook genuinely originated from the SaaS platform and was not forged or replayed "
                "by an attacker who found the URL. Which approach does the platform MOST commonly provide for this?",
        "options": [
            {"id": "A", "text": "Rely on the secrecy of the webhook URL alone"},
            {"id": "B", "text": "Check that the request came over HTTP"},
            {"id": "C", "text": "Sign each payload with an HMAC using a shared secret (plus a timestamp/nonce); the receiver recomputes and compares the signature and rejects stale timestamps"},
            {"id": "D", "text": "Trust any request whose body matches the expected JSON schema"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The sender computes an HMAC of the payload (and a timestamp/nonce) with a shared secret and "
                       "includes it in a header; the receiver recomputes the HMAC to verify authenticity/integrity and rejects stale or replayed timestamps - proving the webhook is genuine.",
            "distractors": {
                "A": "A 'secret URL' is easily leaked (logs, referrers) and provides no cryptographic authenticity or replay protection.",
                "B": "Plain HTTP offers no authentication and exposes traffic; it does not prove origin.",
                "D": "Matching a schema only checks shape; an attacker can craft well-formed JSON, so it proves nothing about origin.",
            },
            "exam_pattern": "Verify webhook authenticity/integrity = HMAC-signed payload + timestamp/nonce for replay protection; not URL secrecy or schema shape.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (webhook security, HMAC signatures)"],
    },
    {
        "id": "securityx-eng-r2-016", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "In a microservices platform, dozens of services call each other's APIs. Security wants to eliminate "
                "long-lived static API keys embedded in config and reduce the damage if one service is compromised. "
                "Which approach BEST secures this service-to-service (machine) authentication?",
        "options": [
            {"id": "A", "text": "Give every service the same shared static API key stored in a config file"},
            {"id": "B", "text": "Issue each workload a short-lived, automatically rotated identity/credential (e.g., mTLS certificates or signed service tokens from an identity provider) scoped with least privilege"},
            {"id": "C", "text": "Allow unauthenticated internal calls since they are behind the firewall"},
            {"id": "D", "text": "Hard-code credentials into each container image"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Short-lived, automatically rotated workload identities (mTLS certificates or signed service "
                       "tokens) scoped to least privilege limit the window and blast radius if a service is compromised, and remove brittle static secrets from configuration.",
            "distractors": {
                "A": "A shared static key means a single leak compromises everything and cannot distinguish or revoke individual services.",
                "C": "Implicit trust of internal traffic violates zero trust and enables free lateral movement after any foothold.",
                "D": "Hard-coded image credentials are easily extracted from images/registries and are hard to rotate.",
            },
            "exam_pattern": "Service-to-service auth -> short-lived, rotated workload identities (mTLS/signed tokens), least privilege; avoid static shared/hard-coded keys.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (machine/workload identity, secrets management)"],
    },
    {
        "id": "securityx-eng-r2-017", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 2, "type": "mcq",
        "stem": "An API aggregates data submitted by multiple partners and passes fields into backend queries and "
                "downstream services. To prevent injection and malformed-data attacks across this integration, which "
                "control is MOST fundamental at the API boundary?",
        "options": [
            {"id": "A", "text": "Rigorous server-side input validation (allowlist/schema validation, type/length/range checks) with proper output encoding/parameterization downstream"},
            {"id": "B", "text": "Relying on the partner's client-side JavaScript validation"},
            {"id": "C", "text": "Increasing the API's rate limit"},
            {"id": "D", "text": "Returning verbose stack traces to help partners debug"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Never trust external input: enforce strict server-side validation (allowlist/schema, type, "
                       "length, range) and use parameterization/encoding when passing data to queries or downstream systems - the foundational defense against injection across integrations.",
            "distractors": {
                "B": "Client-side validation is easily bypassed and cannot be trusted as a security control.",
                "C": "Rate limiting mitigates abuse/DoS but does not stop malicious content in otherwise-allowed requests.",
                "D": "Verbose stack traces leak internal details to attackers and aid exploitation.",
            },
            "exam_pattern": "Integration boundary against injection = server-side allowlist/schema validation + parameterization/encoding; client-side checks are not security.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (input validation at API boundaries)"],
    },
    {
        "id": "securityx-eng-r2-018", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_integration", "difficulty": 3, "type": "mcq",
        "stem": "A message travels through several intermediaries (API gateways, message brokers) before reaching "
                "its destination, and it must remain confidential and integrity-protected end to end - not readable "
                "or alterable by any intermediary. Transport-layer TLS alone is insufficient here. Which approach "
                "BEST meets the requirement?",
        "options": [
            {"id": "A", "text": "Enable TLS 1.3 on each hop and consider it end-to-end"},
            {"id": "B", "text": "Compress the message before sending"},
            {"id": "C", "text": "Encode the message in Base64"},
            {"id": "D", "text": "Apply message-level security: sign and encrypt the payload itself (e.g., JWS/JWE or WS-Security) so protection persists across every intermediary"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "TLS protects each transport hop but is terminated and re-originated at every intermediary, which "
                       "can read/alter the plaintext. Message-level security encrypts and signs the payload itself (JWS/JWE, WS-Security), so confidentiality and integrity persist end to end regardless of the intermediaries.",
            "distractors": {
                "A": "Hop-by-hop TLS leaves the message in plaintext at each intermediary where TLS terminates - not true end-to-end protection.",
                "B": "Compression affects size, not confidentiality or integrity.",
                "C": "Base64 is reversible encoding and provides no protection.",
            },
            "exam_pattern": "Protection must survive intermediaries -> message-level (payload) encryption/signing, not just transport TLS (which is hop-by-hop).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure integration (message-level vs transport-level security)"],
    },

    # ===== scx_endpoint_security ============================================
    {
        "id": "securityx-eng-r2-019", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 3, "type": "mcq",
        "stem": "A zero-trust program wants a remote server to cryptographically verify that a laptop booted only "
                "trusted, unmodified firmware and OS components before granting it access to sensitive resources. "
                "Which capability BEST provides this remote attestation of boot integrity?",
        "options": [
            {"id": "A", "text": "UEFI Secure Boot alone, which blocks unsigned bootloaders locally"},
            {"id": "B", "text": "Measured boot, where each boot component is hashed into the TPM's platform configuration registers (PCRs) and the signed measurements are sent to a verifier for remote attestation"},
            {"id": "C", "text": "A host-based firewall rule set"},
            {"id": "D", "text": "BIOS password protection"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Measured boot records cryptographic hashes of each boot stage into TPM PCRs; the TPM can produce "
                       "a signed quote of these measurements that a remote verifier evaluates (remote attestation) to confirm the platform booted a known-good state.",
            "distractors": {
                "A": "Secure Boot enforces signature checks locally and blocks unsigned components, but by itself it does not produce signed measurements for a remote verifier to attest to.",
                "C": "A host firewall controls network traffic; it does not attest to boot integrity.",
                "D": "A BIOS password restricts local configuration access but provides no cryptographic boot attestation.",
            },
            "exam_pattern": "Remote proof of boot integrity = measured boot (TPM PCRs) + remote attestation; Secure Boot = local enforcement of signed components.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (measured boot vs Secure Boot, TPM attestation)"],
    },
    {
        "id": "securityx-eng-r2-020", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 2, "type": "mcq",
        "stem": "A hardened server must alert the SOC whenever critical system binaries or configuration files are "
                "modified, since attackers often tamper with these for persistence. Which control MOST directly "
                "detects such unauthorized changes?",
        "options": [
            {"id": "A", "text": "File integrity monitoring (FIM) that baselines cryptographic hashes and alerts on deviations"},
            {"id": "B", "text": "A faster CPU to process logs"},
            {"id": "C", "text": "Disabling the system's audit logs to reduce noise"},
            {"id": "D", "text": "A longer password policy for administrators"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File integrity monitoring establishes a trusted baseline (hashes/attributes) of critical files "
                       "and alerts when they change unexpectedly, surfacing tampering, rootkits, or unauthorized configuration changes.",
            "distractors": {
                "B": "CPU speed does not detect file changes.",
                "C": "Disabling audit logs removes evidence and visibility - the opposite of detection.",
                "D": "Stronger passwords reduce credential compromise but do not detect modifications to files.",
            },
            "exam_pattern": "Detect unauthorized changes to critical files/config = FIM (baseline hashes + alert on deviation).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (file integrity monitoring)"],
    },
    {
        "id": "securityx-eng-r2-021", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 3, "type": "mcq",
        "stem": "A company allows BYOD smartphones to access corporate email and apps. Security must keep corporate "
                "data separate from personal data and be able to remove ONLY corporate data if the employee leaves or "
                "the device is lost, without wiping the user's personal photos. Which approach BEST achieves this?",
        "options": [
            {"id": "A", "text": "Full-device wipe on any policy violation"},
            {"id": "B", "text": "Ask employees to manually delete corporate data when they leave"},
            {"id": "C", "text": "MDM/UEM containerization that isolates managed corporate apps/data and supports selective (corporate-only) wipe"},
            {"id": "D", "text": "Block all mobile access to corporate resources"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Containerization (via MDM/UEM) separates managed corporate apps and data from personal content "
                       "and enables a selective wipe that removes only the corporate container - balancing security with employee privacy on BYOD devices.",
            "distractors": {
                "A": "A full-device wipe destroys personal data, raising privacy and legal concerns on BYOD.",
                "B": "Relying on manual user deletion is unenforceable and unreliable.",
                "D": "Blocking all mobile access defeats the BYOD goal and is more restrictive than needed.",
            },
            "exam_pattern": "BYOD data separation + remove only corporate data = MDM/UEM containerization with selective wipe.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (MDM/UEM, BYOD containerization, selective wipe)"],
    },
    {
        "id": "securityx-eng-r2-022", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 3, "type": "mcq",
        "stem": "Analysis shows that most malware and ransomware damage on workstations is amplified because users "
                "run with standing local administrator rights. Which control MOST directly reduces this blast radius "
                "while still allowing occasional legitimate elevation?",
        "options": [
            {"id": "A", "text": "Give users two admin accounts instead of one"},
            {"id": "B", "text": "Install signature antivirus and nothing else"},
            {"id": "C", "text": "Allow local admin but require a longer password"},
            {"id": "D", "text": "Remove standing local-admin rights and use endpoint privilege management to broker just-in-time, approved elevation for specific tasks (least privilege)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Removing standing local admin and brokering just-in-time, task-scoped elevation (endpoint "
                       "privilege management) enforces least privilege, so malware running as the user cannot trivially gain full control of the host.",
            "distractors": {
                "A": "A second admin account still leaves standing privileges available to malware running in the user's session.",
                "B": "Signature AV alone misses novel/fileless threats and does not address excessive standing privilege.",
                "C": "A longer password does not reduce the privileges malware inherits when the user already has standing admin rights.",
            },
            "exam_pattern": "Reduce malware blast radius on endpoints = remove standing local admin + just-in-time least-privilege elevation (EPM).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (least privilege, endpoint privilege management)"],
    },
    {
        "id": "securityx-eng-r2-023", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 2, "type": "mcq",
        "stem": "To protect data on laptops that are frequently lost or stolen, a company wants full-disk encryption "
                "whose key cannot be trivially extracted and that resists offline attacks if the drive is removed. "
                "Which configuration is STRONGEST?",
        "options": [
            {"id": "A", "text": "Full-disk encryption with the key sealed to the TPM and a required pre-boot authentication factor (PIN/password)"},
            {"id": "B", "text": "Full-disk encryption with the key stored in a plaintext file on the same disk"},
            {"id": "C", "text": "Encrypting only the Documents folder"},
            {"id": "D", "text": "Relying on the operating-system login password with no disk encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sealing the FDE key to the TPM binds it to the specific platform and keeps it out of general "
                       "storage, while a pre-boot PIN/password adds a factor so a stolen drive (or a device powered off) cannot be decrypted by simply removing the disk or capturing the key.",
            "distractors": {
                "B": "Storing the key in plaintext on the same disk defeats the encryption - an attacker reads the key and decrypts.",
                "C": "Encrypting one folder leaves the OS, temp files, and other data exposed.",
                "D": "An OS login password without disk encryption is bypassed by booting another OS or removing the drive.",
            },
            "exam_pattern": "Strong laptop data-at-rest protection = FDE + TPM-sealed key + pre-boot auth (resists drive removal/offline attack).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (full-disk encryption, TPM key sealing, pre-boot auth)"],
    },
    {
        "id": "securityx-eng-r2-024", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_endpoint_security", "difficulty": 3, "type": "mcq",
        "stem": "A firm wants to let staff browse the web and open links freely while preventing web-borne malware "
                "and malicious scripts from executing on their endpoints, without maintaining massive URL blocklists. "
                "Which technique BEST meets this goal?",
        "options": [
            {"id": "A", "text": "Disabling the corporate firewall to speed up browsing"},
            {"id": "B", "text": "Letting users install their own browser extensions"},
            {"id": "C", "text": "Remote browser isolation (sandboxing web sessions off-endpoint and streaming only safe rendering to the user)"},
            {"id": "D", "text": "Turning off endpoint antivirus to avoid conflicts"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Remote browser isolation executes web content in an isolated/sandboxed environment away from the "
                       "endpoint and streams only a safe visual rendering, so active web content/malware never runs on the user's device - independent of blocklists.",
            "distractors": {
                "A": "Disabling the firewall removes protection and increases exposure.",
                "B": "Unmanaged browser extensions expand the attack surface and can be malicious.",
                "D": "Turning off antivirus reduces endpoint defenses - the opposite of the goal.",
            },
            "exam_pattern": "Browse freely but keep web content off the endpoint = remote browser isolation / sandboxing (not blocklists).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Endpoint security (browser isolation, sandboxing)"],
    },

    # ===== scx_emerging_tech ================================================
    {
        "id": "securityx-eng-r2-025", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "At inference time, an attacker submits inputs with small, carefully crafted perturbations - often "
                "imperceptible to humans - that cause a deployed image classifier to confidently misclassify them "
                "(e.g., a stop sign read as a speed-limit sign). Which attack is this, and what is a sound mitigation?",
        "options": [
            {"id": "A", "text": "Data poisoning; mitigate by validating training-data provenance"},
            {"id": "B", "text": "Adversarial example (evasion) attack; mitigate with adversarial training, input preprocessing/robust models, and ensembles/monitoring"},
            {"id": "C", "text": "Prompt injection; mitigate by constraining tool permissions"},
            {"id": "D", "text": "SQL injection; mitigate with parameterized queries"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Perturbing inputs at inference to fool a model is an adversarial-example (evasion) attack. "
                       "Defenses include adversarial training, input transformation/preprocessing, robust/ensemble models, and anomaly monitoring of inputs and confidence.",
            "distractors": {
                "A": "Data poisoning corrupts the training set beforehand; here the training data is untouched and the manipulation happens at inference.",
                "C": "Prompt injection targets LLM instruction-following via malicious text, not perturbed image inputs to a classifier.",
                "D": "SQL injection targets database query construction, not ML model inference.",
            },
            "exam_pattern": "Perturbed inputs fooling a model at inference = adversarial example/evasion; poisoning corrupts training beforehand.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (adversarial ML, evasion attacks)"],
    },
    {
        "id": "securityx-eng-r2-026", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "A company exposes a public machine-learning prediction API. A competitor systematically sends large "
                "numbers of queries and uses the responses to train a functionally equivalent copy of the proprietary "
                "model. Which threat is this, and which control set BEST mitigates it?",
        "options": [
            {"id": "A", "text": "Model extraction/stealing; mitigate with rate limiting/quotas, anomaly detection on query patterns, limiting returned confidence detail, and output watermarking"},
            {"id": "B", "text": "Membership inference; mitigate with TLS on the API"},
            {"id": "C", "text": "Prompt injection; mitigate with input encoding"},
            {"id": "D", "text": "Denial of service; mitigate with a bigger server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Harvesting outputs to reconstruct the model is model extraction/stealing. Mitigations include "
                       "rate limiting/quotas, monitoring for extraction-like query patterns, returning less granular confidence data, and watermarking outputs to prove theft.",
            "distractors": {
                "B": "Membership inference tries to determine whether a specific record was in the training set, not to clone the whole model; TLS does not stop query-based extraction.",
                "C": "Prompt injection manipulates an LLM's instructions, not API-query-based model cloning.",
                "D": "This is not a denial-of-service attack; the goal is to copy the model, and more compute does not prevent extraction.",
            },
            "exam_pattern": "Query-and-clone an ML model via its API = model extraction/stealing -> rate limits, query anomaly detection, reduced confidence output, watermarking.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (model extraction/theft, ML API protection)"],
    },
    {
        "id": "securityx-eng-r2-027", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 2, "type": "mcq",
        "stem": "An organization deploying AI systems wants a voluntary, widely recognized framework specifically for "
                "managing AI-related risks (including trustworthiness characteristics) organized around the functions "
                "Govern, Map, Measure, and Manage. Which framework is this?",
        "options": [
            {"id": "A", "text": "The NIST Cybersecurity Framework (CSF)"},
            {"id": "B", "text": "PCI DSS"},
            {"id": "C", "text": "The NIST AI Risk Management Framework (AI RMF)"},
            {"id": "D", "text": "The OWASP Top 10"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The NIST AI Risk Management Framework (AI RMF 1.0) is purpose-built for managing AI risks and "
                       "trustworthiness, organized around the Govern, Map, Measure, and Manage functions.",
            "distractors": {
                "A": "The NIST CSF manages general cybersecurity risk (Govern/Identify/Protect/Detect/Respond/Recover), not AI-specific risk.",
                "B": "PCI DSS protects payment-card data, unrelated to AI risk management.",
                "D": "The OWASP Top 10 ranks web-application risks, not an AI risk-management framework.",
            },
            "exam_pattern": "Manage AI risk/trustworthiness via Govern-Map-Measure-Manage = NIST AI RMF.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (AI governance, NIST AI RMF)"],
    },
    {
        "id": "securityx-eng-r2-028", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "When planning for the quantum threat, which statement MOST accurately describes the differing impact "
                "of quantum algorithms on symmetric versus asymmetric cryptography?",
        "options": [
            {"id": "A", "text": "Quantum computers break symmetric ciphers completely but leave RSA/ECC fully secure"},
            {"id": "B", "text": "Quantum computing has no effect on any current cryptography"},
            {"id": "C", "text": "Both symmetric and asymmetric algorithms are equally and completely broken, so encryption is pointless"},
            {"id": "D", "text": "Shor's algorithm breaks asymmetric crypto (RSA/ECC), requiring migration to post-quantum algorithms; Grover's gives only a quadratic speedup against symmetric/hash search, effectively halving security, which is countered by doubling key/output lengths (e.g., AES-256, SHA-384/512)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Shor's algorithm efficiently solves the problems underpinning RSA and ECC, breaking asymmetric "
                       "crypto and driving the move to PQC (ML-KEM/ML-DSA). Grover's algorithm only quadratically speeds up brute-force search, roughly halving effective symmetric/hash strength, which is mitigated by using larger keys/outputs (AES-256, SHA-384/512).",
            "distractors": {
                "A": "This is reversed: asymmetric (RSA/ECC) is the severely affected class; symmetric is only weakened, not broken.",
                "B": "Quantum computing does threaten current asymmetric cryptography - this is why PQC standards exist.",
                "C": "Symmetric crypto is not completely broken; doubling key length restores its security margin against Grover.",
            },
            "exam_pattern": "Shor -> breaks RSA/ECC (migrate to PQC); Grover -> halves symmetric strength (use AES-256 / larger hashes).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (quantum threat: Shor vs Grover)"],
    },

    {
        "id": "securityx-eng-r2-029", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "A developer builds an LLM feature that takes the model's raw text output and passes it directly into "
                "a system shell command and also into an SQL query, and grants the model broad API permissions. A "
                "reviewer warns this is dangerous. Which mitigation set BEST addresses the risk (insecure output "
                "handling and excessive agency)?",
        "options": [
            {"id": "A", "text": "Treat LLM output as untrusted input: validate/encode/parameterize it before any downstream use, and scope the model's tools/permissions to least privilege with human approval for consequential actions"},
            {"id": "B", "text": "Trust the model output because it came from the organization's own AI"},
            {"id": "C", "text": "Increase the model's temperature setting"},
            {"id": "D", "text": "Give the model full administrative API access to reduce errors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LLM output must be treated like any untrusted input - validated, encoded, or parameterized "
                       "before it reaches shells, queries, or browsers - and the model's agency (tools/permissions) must be least-privilege with human approval for high-impact actions, limiting damage from manipulated output.",
            "distractors": {
                "B": "Trusting model output enables command/SQL injection via manipulated or hallucinated content; provenance does not make it safe.",
                "C": "Temperature changes output randomness, not safety of how output is handled.",
                "D": "Granting full admin access maximizes excessive agency - exactly the risk to avoid.",
            },
            "exam_pattern": "LLM output -> untrusted: validate/encode/parameterize downstream + least-privilege tools + human-in-the-loop (insecure output handling & excessive agency, OWASP LLM risks).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (LLM insecure output handling, excessive agency)"],
    },
    {
        "id": "securityx-eng-r2-030", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_emerging_tech", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise deploys a retrieval-augmented generation (RAG) assistant over internal documents. "
                "Testing shows it will summarize any document in the index for any employee who asks, including HR and "
                "legal files the asker is not authorized to read. Which control MOST directly fixes this data-exposure problem?",
        "options": [
            {"id": "A", "text": "Lower the model temperature so it answers more conservatively"},
            {"id": "B", "text": "Add a disclaimer telling users not to ask about restricted documents"},
            {"id": "C", "text": "Enforce the requesting user's existing access controls at the retrieval layer (document-level authorization / per-user filtering) so RAG can only retrieve content the user is entitled to see"},
            {"id": "D", "text": "Encrypt the vector database at rest"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "RAG must honor existing authorization: filter retrieval by the requesting user's permissions "
                       "(document-level access control) so the model can only ground its answer on content that user is allowed to see - preventing cross-user data exposure.",
            "distractors": {
                "A": "Temperature affects phrasing/randomness, not who is authorized to see which documents.",
                "B": "A disclaimer is not an access control and does not stop unauthorized retrieval.",
                "D": "Encryption at rest protects stored data from theft but does not restrict which indexed documents an authorized-to-query user can retrieve.",
            },
            "exam_pattern": "RAG data exposure -> enforce per-user document-level authorization at retrieval, not model settings or disclaimers.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Emerging technology (RAG/LLM data exposure, access control on retrieval)"],
    },

    # ===== scx_secure_coding ================================================
    {
        "id": "securityx-eng-r2-031", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A security team must test a deployed third-party web application for which they have NO source code, "
                "looking for runtime vulnerabilities such as authentication flaws, injection, and misconfigurations "
                "as an external attacker would see them. Which testing approach fits BEST?",
        "options": [
            {"id": "A", "text": "SAST (static application security testing)"},
            {"id": "B", "text": "DAST (dynamic application security testing) against the running application"},
            {"id": "C", "text": "Software composition analysis (SCA) of the source dependencies"},
            {"id": "D", "text": "A code linter run in the IDE"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DAST tests a running application from the outside (black-box) without needing source code, "
                       "finding runtime issues like injection, auth flaws, and misconfigurations - ideal for a deployed third-party app.",
            "distractors": {
                "A": "SAST requires access to source/bytecode to analyze statically, which the team does not have for this third-party app.",
                "C": "SCA inspects declared dependencies in source/manifests for known-vulnerable components - not available without the codebase, and it does not test runtime behavior.",
                "D": "A linter needs source code and checks style/basic issues, not runtime vulnerabilities of a deployed app.",
            },
            "exam_pattern": "No source + running app + attacker's-eye view = DAST (black-box); SAST/SCA/linters need the codebase.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (DAST vs SAST, black-box runtime testing)"],
    },
    {
        "id": "securityx-eng-r2-032", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A team wants vulnerability findings with both code-level context (file/line, data flow) AND runtime "
                "confirmation, produced while automated functional/QA tests exercise the application - aiming for high "
                "accuracy and fewer false positives than pure static analysis. Which approach provides this?",
        "options": [
            {"id": "A", "text": "SAST alone"},
            {"id": "B", "text": "DAST alone"},
            {"id": "C", "text": "A software bill of materials (SBOM)"},
            {"id": "D", "text": "IAST (interactive application security testing), which instruments the running app during tests to combine static code visibility with runtime observation"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "IAST instruments the application from within while tests run, correlating code-level context "
                       "with actual runtime execution/data flow - yielding confirmed findings with precise code locations and typically fewer false positives than SAST alone.",
            "distractors": {
                "A": "SAST provides code context but no runtime confirmation, tending to more false positives.",
                "B": "DAST confirms exploitability at runtime but lacks code-level location/data-flow context.",
                "C": "An SBOM inventories components; it is not a vulnerability-testing technique that correlates code and runtime.",
            },
            "exam_pattern": "Code context + runtime confirmation during tests = IAST (instrumented/interactive), bridging SAST and DAST.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (IAST)"],
    },
    {
        "id": "securityx-eng-r2-033", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A tester changes the numeric account ID in the URL /api/accounts/1001 to /api/accounts/1002 and "
                "receives another customer's data. What is the vulnerability class and the correct remediation?",
        "options": [
            {"id": "A", "text": "Broken access control (insecure direct object reference); enforce server-side, per-request object-level authorization that verifies the requester owns/has rights to the referenced object"},
            {"id": "B", "text": "Cross-site scripting; fix with output encoding"},
            {"id": "C", "text": "Buffer overflow; fix with stack canaries"},
            {"id": "D", "text": "Weak cryptography; fix by upgrading to AES-256"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Accessing another user's object by manipulating an identifier is an insecure direct object "
                       "reference, a form of broken access control. The fix is server-side authorization on every request that confirms the authenticated user is entitled to the specific object - not merely obscuring IDs.",
            "distractors": {
                "B": "XSS is script injection into pages; output encoding does not address missing object-level authorization.",
                "C": "A buffer overflow is a memory-safety bug; canaries are irrelevant to authorization logic.",
                "D": "The issue is missing authorization, not weak encryption; stronger ciphers do not grant/deny access.",
            },
            "exam_pattern": "Change an ID -> get someone else's data = IDOR / broken access control; fix = enforce server-side object-level authz per request.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (broken access control, IDOR, OWASP)"],
    },
    {
        "id": "securityx-eng-r2-034", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "A code review finds SQL statements built by concatenating user input directly into query strings. "
                "Which remediation MOST reliably eliminates the SQL injection risk at its root?",
        "options": [
            {"id": "A", "text": "Add a web application firewall and consider the code safe"},
            {"id": "B", "text": "Blocklist the word 'SELECT' in user inputs"},
            {"id": "C", "text": "Use parameterized queries/prepared statements (or safe ORM/stored procedures) so input is treated strictly as data, with least-privilege database accounts as defense in depth"},
            {"id": "D", "text": "Escape only single-quote characters in inputs"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Parameterized queries/prepared statements separate code from data so user input can never alter "
                       "query structure - the root-cause fix for SQL injection. Least-privilege DB accounts and input validation add defense in depth.",
            "distractors": {
                "A": "A WAF is a helpful compensating layer but can be bypassed; it does not fix the vulnerable code.",
                "B": "Keyword blocklists are incomplete and easily evaded (encodings, alternate syntax).",
                "D": "Ad hoc escaping of one character is error-prone and bypassable; parameterization is the reliable fix.",
            },
            "exam_pattern": "SQL injection root fix = parameterized queries/prepared statements (data != code); WAF/escaping/blocklists are weaker add-ons.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (SQL injection, parameterized queries)"],
    },
    {
        "id": "securityx-eng-r2-035", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A cloud web app accepts a user-supplied URL and fetches it server-side to generate link previews. An "
                "attacker supplies a URL pointing to the cloud instance metadata endpoint (169.254.169.254) and "
                "retrieves temporary credentials. Which vulnerability is this, and what is the BEST mitigation?",
        "options": [
            {"id": "A", "text": "Cross-site request forgery; fix with anti-CSRF tokens"},
            {"id": "B", "text": "Server-side request forgery (SSRF); mitigate by allowlisting destinations, blocking link-local/internal ranges, and enforcing IMDSv2 (session-based, with hardened metadata access)"},
            {"id": "C", "text": "Clickjacking; fix with X-Frame-Options"},
            {"id": "D", "text": "Open redirect; fix by validating the Referer header"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Coercing the server to make attacker-chosen requests (including to internal/metadata endpoints) "
                       "is SSRF. Mitigations: allowlist permitted destinations, block requests to link-local/internal IP ranges, require IMDSv2 (session-oriented metadata access), and avoid fetching raw user-supplied URLs.",
            "distractors": {
                "A": "CSRF tricks a victim's browser into sending authenticated requests; here the server itself is coerced to make the request (SSRF).",
                "C": "Clickjacking frames a site to trick user clicks; it is unrelated to server-side URL fetching.",
                "D": "An open redirect bounces users to attacker URLs; it does not describe the server fetching the metadata endpoint.",
            },
            "exam_pattern": "Server fetches attacker-chosen URL -> hits internal/metadata endpoint = SSRF; mitigate with destination allowlists, block internal ranges, IMDSv2.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (SSRF, cloud metadata protection)"],
    },
    {
        "id": "securityx-eng-r2-036", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A build pulls an internally named package (e.g., 'acme-internal-utils'). An attacker publishes a "
                "package of the SAME name with a higher version number to the PUBLIC registry, and the build tool "
                "resolves to the attacker's malicious public package. Which supply-chain attack is this, and what "
                "mitigates it?",
        "options": [
            {"id": "A", "text": "Cross-site scripting; mitigate with a content security policy"},
            {"id": "B", "text": "Cryptographic downgrade; mitigate by disabling TLS 1.0"},
            {"id": "C", "text": "Password spraying; mitigate with account lockout"},
            {"id": "D", "text": "Dependency confusion (substitution); mitigate by using scoped/namespaced private registries, reserving internal names publicly, pinning/verifying sources, and configuring the resolver to never fetch internal names from public registries"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Dependency confusion exploits resolvers that prefer a higher-version public package over the "
                       "intended internal one. Mitigations: scoped/namespaced private registries, reserving internal package names publicly, source pinning/verification, and configuring tooling so internal names never resolve to public registries.",
            "distractors": {
                "A": "XSS is a web output-handling vulnerability, not a package-resolution attack.",
                "B": "A cryptographic downgrade forces weaker crypto; it is unrelated to package name resolution.",
                "C": "Password spraying is a credential attack, not dependency substitution.",
            },
            "exam_pattern": "Internal package name resolves to a malicious public one = dependency confusion; fix via private/scoped registries, name reservation, source pinning.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Secure coding (dependency confusion, supply-chain/package security)"],
    },

    # ===== scx_automation ===================================================
    {
        "id": "securityx-eng-r2-037", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 3, "type": "mcq",
        "stem": "A platform team wants to eliminate configuration drift and make attacker persistence harder by never "
                "patching running servers in place; instead, every change is baked into a new, version-controlled "
                "image and the old instances are replaced. Which practice is this, and what is a key security benefit?",
        "options": [
            {"id": "A", "text": "Immutable infrastructure; redeploying from known-good images removes drift and wipes any attacker-installed persistence on each replacement"},
            {"id": "B", "text": "Snowflake servers; each server is uniquely hand-tuned for resilience"},
            {"id": "C", "text": "Shadow IT; teams self-provision outside central control"},
            {"id": "D", "text": "Manual patching; administrators log in to each host to update"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Immutable infrastructure replaces instances with new images rather than modifying them in place. "
                       "Because each deployment starts from a known-good, version-controlled image, configuration drift is eliminated and any persistence an attacker planted is removed when the instance is replaced.",
            "distractors": {
                "B": "'Snowflake' servers are uniquely hand-modified and drift-prone - the opposite of immutable infrastructure.",
                "C": "Shadow IT is unsanctioned provisioning, a governance risk, not a drift-elimination practice.",
                "D": "Manual in-place patching is exactly what immutable infrastructure avoids and is a source of drift.",
            },
            "exam_pattern": "Replace, don't patch, from version-controlled images = immutable infrastructure (no drift, persistence wiped on redeploy).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation (immutable infrastructure)"],
    },
    {
        "id": "securityx-eng-r2-038", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 3, "type": "mcq",
        "stem": "A security team wants infrastructure-as-code changes that would create a publicly exposed storage "
                "bucket or an overly permissive security group to be automatically BLOCKED in the CI/CD pipeline "
                "before deployment, using machine-readable rules kept in version control. Which approach provides this?",
        "options": [
            {"id": "A", "text": "A quarterly manual architecture review"},
            {"id": "B", "text": "A post-deployment email notification to the security team"},
            {"id": "C", "text": "Policy as code (e.g., OPA/Rego or equivalent) evaluated as a pipeline gate that fails non-compliant IaC before it is applied"},
            {"id": "D", "text": "A wiki page documenting the rules for developers to remember"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Policy as code expresses guardrails as machine-readable, version-controlled rules evaluated "
                       "automatically in the pipeline; non-compliant infrastructure definitions fail the gate and are blocked before deployment - consistent, auditable prevention.",
            "distractors": {
                "A": "Quarterly manual reviews are point-in-time and too slow to block every risky change at deploy time.",
                "B": "A post-deployment notification is detective and too late - the misconfiguration is already live.",
                "D": "A wiki relies on humans remembering rules; it enforces nothing automatically.",
            },
            "exam_pattern": "Automatically block non-compliant IaC pre-deploy = policy as code gate (OPA/Rego) in CI/CD.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation (policy as code, compliance as code, pipeline gating)"],
    },
    {
        "id": "securityx-eng-r2-039", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 2, "type": "mcq",
        "stem": "To ensure every new server starts in a consistent, hardened state, a team builds a single pre-hardened "
                "'golden image' (patched, CIS-benchmark-configured, agents installed) through an automated, scanned "
                "pipeline, then provisions all instances from it. Which benefit BEST describes this practice?",
        "options": [
            {"id": "A", "text": "It guarantees applications are bug-free"},
            {"id": "B", "text": "It provides consistent, repeatable secure baselines and reduces configuration drift and manual hardening errors across all deployments"},
            {"id": "C", "text": "It removes the need for any further patching ever"},
            {"id": "D", "text": "It eliminates the need for network segmentation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A golden (hardened baseline) image produces consistent, repeatable, known-good configurations "
                       "for every instance, reducing drift and the human errors of manually hardening each host; images are rebuilt/rescanned as updates are needed.",
            "distractors": {
                "A": "A hardened OS image does not make the applications running on it bug-free.",
                "C": "Images must still be updated/rebuilt as new patches are released; it does not end patching.",
                "D": "A baseline image does not replace network segmentation, which addresses a different control layer.",
            },
            "exam_pattern": "Provision from a scanned, hardened golden image = consistent secure baselines, less drift/manual error (rebuild to update).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation (golden images, hardened baselines)"],
    },
    {
        "id": "securityx-eng-r2-040", "exam": "securityx", "domain": "scx_engineering",
        "subtopic": "scx_automation", "difficulty": 3, "type": "mcq",
        "stem": "A federal-aligned enterprise must continuously and automatically assess thousands of endpoints "
                "against a standardized hardening benchmark, using machine-readable checklists so results are "
                "consistent and tool-interoperable. Which standard/protocol suite is designed for this automated "
                "configuration and compliance assessment?",
        "options": [
            {"id": "A", "text": "SNMP"},
            {"id": "B", "text": "NetFlow"},
            {"id": "C", "text": "Syslog"},
            {"id": "D", "text": "SCAP (Security Content Automation Protocol), using components such as OVAL, XCCDF, and CVE/CPE"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SCAP is a suite of standards (e.g., XCCDF checklists, OVAL definitions, CVE/CPE identifiers) that "
                       "lets tools automatically and consistently assess systems against hardening/compliance baselines in a machine-readable, interoperable way.",
            "distractors": {
                "A": "SNMP monitors/manages device metrics and state; it is not a configuration-compliance checklist standard.",
                "B": "NetFlow records network flow data for traffic analysis, not host configuration compliance.",
                "C": "Syslog transports log messages; it does not evaluate hardening baselines.",
            },
            "exam_pattern": "Automated, standardized, interoperable config/compliance scanning = SCAP (XCCDF/OVAL/CVE/CPE).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 3 — Automation (SCAP, automated compliance assessment)"],
    },

    # ================= DOMAIN 2: SECURITY ARCHITECTURE ======================
    # ===== scx_secure_architecture ==========================================
    {
        "id": "securityx-arch-r2-001", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 2, "type": "mcq",
        "stem": "An organization hosts internet-facing web and mail servers. It wants these public services reachable "
                "from the internet, but if one is compromised, the attacker should NOT be able to reach the internal "
                "corporate LAN directly. Which network architecture BEST accomplishes this?",
        "options": [
            {"id": "A", "text": "Place the public servers directly on the internal LAN behind one firewall"},
            {"id": "B", "text": "Place the public servers in a screened subnet (DMZ) isolated by firewalls between the internet and the internal network, with strict rules limiting DMZ-to-internal traffic"},
            {"id": "C", "text": "Expose the servers directly on the internet with public IPs and no firewall"},
            {"id": "D", "text": "Put all servers and workstations in one flat subnet for simplicity"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A screened subnet (DMZ) isolates internet-facing services between the external and internal "
                       "boundaries; firewall rules tightly restrict traffic from the DMZ to the internal network, so a compromised public server cannot pivot directly into the LAN.",
            "distractors": {
                "A": "Placing public servers on the internal LAN means a compromise lands the attacker directly inside the trusted network.",
                "C": "Exposing servers with no firewall removes all filtering and containment.",
                "D": "A flat subnet gives the attacker free lateral movement to every host after any compromise.",
            },
            "exam_pattern": "Public services + contain compromise = screened subnet (DMZ) with restricted DMZ->internal rules.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (screened subnet/DMZ, segmentation)"],
    },
    {
        "id": "securityx-arch-r2-002", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 3, "type": "mcq",
        "stem": "A mature security team wants high-fidelity, low-false-positive early warning that an attacker is "
                "performing reconnaissance or lateral movement INSIDE the network - since any interaction with the "
                "decoy is inherently suspicious. Which architectural control BEST provides this?",
        "options": [
            {"id": "A", "text": "A louder perimeter firewall logging policy"},
            {"id": "B", "text": "Longer log retention on all servers"},
            {"id": "C", "text": "Deception technology: honeypots, honeynets, and honeytokens placed as decoys that legitimate users never touch"},
            {"id": "D", "text": "A faster internet circuit"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Deception assets (honeypots/honeynets/honeytokens) are decoys with no legitimate business use, "
                       "so any access is almost certainly malicious - yielding high-fidelity, low-false-positive alerts on internal reconnaissance and lateral movement.",
            "distractors": {
                "A": "More perimeter logging increases volume/noise and does not specifically flag internal attacker interaction.",
                "B": "Longer retention aids investigation after the fact but does not provide high-fidelity early detection.",
                "D": "Bandwidth is unrelated to detecting attacker activity.",
            },
            "exam_pattern": "High-fidelity early warning of intruders inside = deception (honeypots/honeytokens); any interaction with a decoy is suspicious.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (deception technology, honeypots/honeytokens)"],
    },
    {
        "id": "securityx-arch-r2-003", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 3, "type": "mcq",
        "stem": "A network security enforcement point (e.g., an inline inspection device) protects a high-security "
                "segment where confidentiality and integrity are explicitly prioritized over availability. If the "
                "device can no longer enforce its security policy, which failure mode is appropriate, and what is the "
                "trade-off?",
        "options": [
            {"id": "A", "text": "Fail-closed (fail-secure): block traffic that cannot be inspected/authorized, accepting a potential availability outage to preserve security"},
            {"id": "B", "text": "Fail-open: allow all traffic through uninspected to preserve availability"},
            {"id": "C", "text": "Randomly allow half of the traffic"},
            {"id": "D", "text": "Disable logging and continue forwarding"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When confidentiality/integrity outrank availability, the control should fail-closed (fail-secure): "
                       "deny traffic it can no longer vet. The trade-off is a possible loss of availability, which is acceptable given the stated priorities.",
            "distractors": {
                "B": "Fail-open preserves availability but lets unvetted/unauthorized traffic through - a security gap, contrary to the stated priority.",
                "C": "Randomly allowing traffic is neither a sound security posture nor predictable.",
                "D": "Continuing to forward while disabling logging removes enforcement and visibility - the worst of both.",
            },
            "exam_pattern": "Security > availability -> fail-closed (deny on failure), accepting an availability trade-off; availability-critical may choose fail-open.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (fail-open vs fail-closed/fail-secure)"],
    },
    {
        "id": "securityx-arch-r2-004", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 3, "type": "mcq",
        "stem": "An industrial control (OT) network must send telemetry OUT to an IT monitoring system, but must be "
                "physically incapable of receiving ANY inbound connection from IT, even if a firewall is "
                "misconfigured or compromised. Which control enforces this strictly one-way flow?",
        "options": [
            {"id": "A", "text": "A stateful firewall rule permitting only outbound connections"},
            {"id": "B", "text": "A site-to-site VPN between OT and IT"},
            {"id": "C", "text": "A full air gap with no connection at all"},
            {"id": "D", "text": "A data diode (unidirectional security gateway) that physically allows data to travel in only one direction"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A data diode enforces one-way communication at the hardware level, so telemetry can leave the OT "
                       "network while inbound traffic is physically impossible - robust even against firewall misconfiguration or compromise.",
            "distractors": {
                "A": "A stateful firewall rule is software-enforced and can be misconfigured or bypassed; it is not a physical guarantee.",
                "B": "A VPN provides an encrypted bidirectional tunnel - it does not enforce strict one-way flow.",
                "C": "A full air gap blocks the required outbound telemetry too, defeating the monitoring goal.",
            },
            "exam_pattern": "Physically guaranteed one-way (OT telemetry out, nothing in) = data diode / unidirectional gateway; firewalls are software-enforced only.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (OT/ICS, data diode/unidirectional gateway)"],
    },
    {
        "id": "securityx-arch-r2-005", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 2, "type": "mcq",
        "stem": "Before any device is allowed onto the corporate network, security wants to verify it is managed, "
                "patched, and running required endpoint protection, and to quarantine devices that fail these checks. "
                "Which technology BEST enforces this at connection time?",
        "options": [
            {"id": "A", "text": "A web application firewall (WAF)"},
            {"id": "B", "text": "Network access control (NAC) with endpoint posture/health assessment (e.g., 802.1X plus posture checks)"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A password manager"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "NAC authenticates devices/users at connection and performs posture assessment (patch level, "
                       "AV/EDR presence, configuration), granting, denying, or quarantining access accordingly - enforcing admission control at the point of connection.",
            "distractors": {
                "A": "A WAF filters web-application traffic; it does not control device admission to the network.",
                "C": "A load balancer distributes traffic and does not assess endpoint posture.",
                "D": "A password manager stores credentials; it does not perform network admission/posture control.",
            },
            "exam_pattern": "Admit only compliant devices (posture check) at connection = NAC (802.1X + posture), quarantine on failure.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (network access control, posture assessment)"],
    },
    {
        "id": "securityx-arch-r2-006", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 3, "type": "mcq",
        "stem": "A manufacturer is converging its IT and OT environments. It must protect Level 0-2 control systems "
                "(PLCs, SCADA) from threats originating on the IT network while still allowing controlled data "
                "exchange. Which architectural approach aligns with industrial best practice?",
        "options": [
            {"id": "A", "text": "Merge IT and OT into one flat network for easier management"},
            {"id": "B", "text": "Give OT devices public internet addresses for remote vendor support"},
            {"id": "C", "text": "Segment per the Purdue model with an intermediary IT/OT DMZ (industrial DMZ) that brokers and inspects all traffic between enterprise IT and the control-system zones"},
            {"id": "D", "text": "Rely solely on the OT vendors' default passwords and obscurity"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Industrial best practice (Purdue/IEC 62443-aligned) segments the environment into levels and "
                       "inserts an IT/OT DMZ that brokers and inspects traffic, preventing direct IT-to-control-system access while permitting controlled, monitored data exchange.",
            "distractors": {
                "A": "A flat converged network removes isolation and exposes fragile control systems to IT-borne threats.",
                "B": "Directly internet-exposing OT devices dramatically increases attack surface for safety-critical systems.",
                "D": "Default passwords and obscurity are not a protective architecture and are commonly exploited.",
            },
            "exam_pattern": "IT/OT convergence -> segment per Purdue model with an industrial IT/OT DMZ brokering/inspecting traffic to protect control zones.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (OT/ICS segmentation, Purdue model, IT/OT DMZ)"],
    },

    # ===== scx_zero_trust ===================================================
    {
        "id": "securityx-arch-r2-007", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "Contractors need access to exactly two internal web applications. The current full-tunnel VPN places "
                "them on the internal network, where a compromised contractor laptop could scan and reach many other "
                "systems. Which approach BEST provides least-privilege access without network-level exposure?",
        "options": [
            {"id": "A", "text": "Zero Trust Network Access (ZTNA): broker per-application access based on verified identity and device posture, with no network-level connectivity and default-deny to everything else"},
            {"id": "B", "text": "Give contractors split-tunnel VPN so only some traffic uses the tunnel"},
            {"id": "C", "text": "Add the contractors to the site-to-site VPN mesh"},
            {"id": "D", "text": "Place the two apps on the internet with only a shared password"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ZTNA grants access to specific applications after verifying identity and device posture, without "
                       "putting the user on the network - so a compromised endpoint cannot scan or reach other systems. Everything not explicitly allowed is denied.",
            "distractors": {
                "B": "Split-tunnel VPN still grants network-level access to internal resources through the tunnel; it does not limit access to just two apps.",
                "C": "A site-to-site VPN mesh connects whole networks, broadening reachability - the opposite of least privilege.",
                "D": "A shared password on internet-exposed apps is weak authentication and offers no device posture or per-user control.",
            },
            "exam_pattern": "App-specific least-privilege remote access, no network exposure = ZTNA; VPNs grant network-level reach enabling lateral movement.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (ZTNA vs VPN, least-privilege access)"],
    },
    {
        "id": "securityx-arch-r2-008", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "In a zero trust architecture, on what basis should the policy decision point grant or deny each "
                "access request, consistent with NIST SP 800-207?",
        "options": [
            {"id": "A", "text": "Solely on whether the source IP address is inside the corporate network range"},
            {"id": "B", "text": "On a one-time authentication at login that is trusted for the rest of the session"},
            {"id": "C", "text": "On possession of a static long-lived API key alone"},
            {"id": "D", "text": "On a dynamic, per-request evaluation of multiple signals - verified identity, device health/posture, resource sensitivity, and behavioral/contextual risk - re-evaluated continuously"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Zero trust makes access decisions dynamically per request using many signals (identity, device "
                       "posture, resource sensitivity, context/behavior) and continuously re-evaluates them, rather than trusting network location or a single prior authentication.",
            "distractors": {
                "A": "Trusting source IP/network location is exactly the implicit trust zero trust eliminates.",
                "B": "A one-time login trusted for the whole session contradicts continuous verification and 'assume breach.'",
                "C": "A static long-lived key is a single stealable factor and provides no continuous, context-aware evaluation.",
            },
            "exam_pattern": "ZT access decision = dynamic, per-request, multi-signal (identity + device posture + context), continuously re-evaluated.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (trust algorithm, continuous evaluation; NIST SP 800-207)"],
    },
    {
        "id": "securityx-arch-r2-009", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise wants to extend zero trust to unmanaged/BYOD and partner devices that cannot run a "
                "client-side agent. It routes all access through a single gateway/portal that authenticates and "
                "authorizes users before exposing any resource. Which NIST SP 800-207 deployment model does this reflect?",
        "options": [
            {"id": "A", "text": "The device agent/gateway-based deployment (agent required on each endpoint)"},
            {"id": "B", "text": "The resource portal-based deployment (a gateway/portal is the PEP; no endpoint agent needed)"},
            {"id": "C", "text": "A flat trusted-network deployment"},
            {"id": "D", "text": "A perimeter-only firewall deployment"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In the resource portal-based model (NIST SP 800-207), the policy enforcement point is a "
                       "gateway/portal that users reach to authenticate and gain access, requiring no software on the client - well suited to BYOD/unmanaged and partner devices.",
            "distractors": {
                "A": "The agent/gateway model requires an agent on each device, which unmanaged/BYOD endpoints cannot run.",
                "C": "A flat trusted network is the antithesis of zero trust.",
                "D": "A perimeter-only firewall is classic perimeter security, not an 800-207 ZTA deployment model.",
            },
            "exam_pattern": "No agent possible (BYOD/partner) -> resource portal-based ZTA (gateway/portal is the PEP); managed devices can use agent/gateway model.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (NIST SP 800-207 deployment models)"],
    },
    {
        "id": "securityx-arch-r2-010", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "A design goal is to make internal application servers completely invisible and unreachable to any "
                "client until that client's identity is cryptographically verified - so unauthenticated attackers "
                "cannot even scan or discover the services. Which architecture achieves this 'deny-by-default, "
                "authenticate-before-connect' model?",
        "options": [
            {"id": "A", "text": "A traditional VLAN with an open port range"},
            {"id": "B", "text": "A public-facing reverse proxy with no authentication"},
            {"id": "C", "text": "A software-defined perimeter (SDP), where resources are hidden until authorized clients authenticate (e.g., single-packet authorization) before any connection is permitted"},
            {"id": "D", "text": "Port forwarding on the edge router"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A software-defined perimeter hides resources (a 'dark' network): clients must authenticate - often "
                       "via single-packet authorization - before any connection is allowed, so unauthenticated attackers cannot discover or scan the services.",
            "distractors": {
                "A": "A VLAN with open ports is discoverable and scannable by anyone with network access.",
                "B": "An unauthenticated reverse proxy exposes the service to everyone.",
                "D": "Port forwarding exposes a reachable listening service that attackers can find and probe.",
            },
            "exam_pattern": "Hide resources until identity verified (authenticate-before-connect) = software-defined perimeter (SDP), often with single-packet authorization.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (software-defined perimeter)"],
    },
    {
        "id": "securityx-arch-r2-011", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 2, "type": "multi",
        "stem": "A CISO says that in their zero trust program, 'identity is the new perimeter.' Which TWO statements "
                "accurately reflect this principle? (Choose two.)",
        "options": [
            {"id": "A", "text": "Access decisions are anchored on strongly verified user/device identity and context rather than on source IP address or network zone"},
            {"id": "B", "text": "Being connected to the corporate LAN should automatically grant broad trust"},
            {"id": "C", "text": "Strong, phishing-resistant authentication and least-privilege authorization become central, continuously enforced controls"},
            {"id": "D", "text": "Once a perimeter firewall is in place, internal identity controls are unnecessary"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "When identity is the control plane, decisions hinge on verified identity and context (not network "
                       "location), and robust authentication (phishing-resistant MFA) plus least-privilege authorization become the primary, continuously enforced controls.",
            "distractors": {
                "B": "Granting trust for being on the LAN is implicit network-location trust, which zero trust rejects.",
                "D": "A perimeter firewall does not remove the need for identity-centric controls; internal trust must still be verified.",
            },
            "exam_pattern": "Identity-as-perimeter = decisions on verified identity/context + strong authN + least privilege, not network location.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (identity as the control plane)"],
    },

    # ===== scx_cloud_hybrid_arch ============================================
    {
        "id": "securityx-arch-r2-012", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "Security must block uploads of regulated data to unsanctioned cloud apps in REAL TIME, as the user "
                "attempts them, and apply conditional controls inline. A colleague notes that one CASB deployment mode "
                "only scans data already at rest in sanctioned apps after the fact. Which CASB deployment mode meets "
                "the real-time inline requirement?",
        "options": [
            {"id": "A", "text": "API-based (out-of-band) mode"},
            {"id": "B", "text": "Inline mode via forward/reverse proxy, which intercepts traffic and enforces policy in real time"},
            {"id": "C", "text": "A log-only passive collector"},
            {"id": "D", "text": "A monthly manual export review"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Inline CASB (forward or reverse proxy) sits in the traffic path and enforces policy in real time, "
                       "so it can block a risky upload as it happens. API-based mode connects out-of-band to sanctioned apps and inspects data at rest/after the fact.",
            "distractors": {
                "A": "API-based mode is out-of-band and retrospective - it inspects data already in sanctioned apps, not live upload attempts.",
                "C": "A passive log collector only observes; it cannot block in real time.",
                "D": "A monthly manual review is far from real time and cannot prevent an upload in progress.",
            },
            "exam_pattern": "Real-time inline enforcement = proxy-mode CASB; API/out-of-band mode = retrospective inspection of data at rest.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (CASB deployment modes: inline proxy vs API)"],
    },

    {
        "id": "securityx-arch-r2-013", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "A team deploys a web application onto a managed Platform as a Service (PaaS) that provides the "
                "runtime and operating system. Under the shared responsibility model, which security task clearly "
                "REMAINS the customer's responsibility in PaaS?",
        "options": [
            {"id": "A", "text": "Patching the underlying operating system and runtime"},
            {"id": "B", "text": "Maintaining the physical data-center and hypervisor"},
            {"id": "C", "text": "Securing the application code, its data, and the identity/access (IAM) configuration for the app"},
            {"id": "D", "text": "Replacing failed server hardware"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "In PaaS the provider manages the OS, runtime, and infrastructure, while the customer remains "
                       "responsible for their own application code, the data they put in it, and how they configure identity/access to the application.",
            "distractors": {
                "A": "In PaaS the provider patches the OS and runtime - that is not the customer's task (unlike IaaS).",
                "B": "Physical facilities and the hypervisor are always the provider's responsibility.",
                "D": "Hardware replacement is handled by the cloud provider.",
            },
            "exam_pattern": "PaaS: provider owns OS/runtime/infra; customer owns app code + data + IAM configuration.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (shared responsibility in PaaS)"],
    },
    {
        "id": "securityx-arch-r2-014", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "A security review of a large multicloud estate finds thousands of IAM roles and identities with "
                "excessive, unused permissions and risky privilege-escalation paths. The team wants a tool category "
                "focused specifically on discovering and right-sizing cloud ENTITLEMENTS to enforce least privilege "
                "for identities. Which category fits BEST?",
        "options": [
            {"id": "A", "text": "Cloud Infrastructure Entitlement Management (CIEM)"},
            {"id": "B", "text": "A web application firewall (WAF)"},
            {"id": "C", "text": "A SIEM"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CIEM specializes in analyzing cloud identities and their entitlements, finding excessive/unused "
                       "permissions and escalation paths, and recommending least-privilege right-sizing across clouds (often a component of a broader CNAPP).",
            "distractors": {
                "B": "A WAF filters web-application traffic; it does not manage cloud identity entitlements.",
                "C": "A SIEM correlates logs/events; it is not purpose-built to right-size IAM entitlements.",
                "D": "A load balancer distributes traffic, unrelated to entitlement management.",
            },
            "exam_pattern": "Right-size cloud identity permissions / least privilege for entitlements = CIEM (vs CSPM = misconfigurations).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (CIEM, least privilege)"],
    },
    {
        "id": "securityx-arch-r2-015", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "A cloud application needs database passwords and third-party API keys at runtime. Developers have "
                "been hardcoding these in config files committed to source control. Which approach BEST remediates "
                "this while providing central control, rotation, and auditing?",
        "options": [
            {"id": "A", "text": "Base64-encode the secrets in the config files"},
            {"id": "B", "text": "Move the secrets into environment variables baked into the container image"},
            {"id": "C", "text": "Email the secrets to developers who need them"},
            {"id": "D", "text": "Use a managed secrets manager/KMS: store secrets centrally, fetch them at runtime via workload identity, protect them with envelope encryption (DEK wrapped by a KEK in the KMS/HSM), and enable rotation and audit logging"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A secrets manager/KMS centralizes secrets, serves them to workloads at runtime via identity, "
                       "supports rotation and audit, and protects data keys with envelope encryption (DEK encrypted by a KEK held in the KMS/HSM) - removing secrets from source and images.",
            "distractors": {
                "A": "Base64 is trivially reversible; the secrets remain exposed in source control.",
                "B": "Baking secrets into images still ships them with the artifact and makes rotation/auditing hard.",
                "C": "Emailing secrets scatters them into uncontrolled channels with no rotation or audit.",
            },
            "exam_pattern": "Runtime secrets -> managed secrets manager/KMS (central, rotated, audited) + envelope encryption (DEK/KEK); never hardcode/encode in source or images.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (secrets management, KMS, envelope encryption)"],
    },
    {
        "id": "securityx-arch-r2-016", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "A company moves logic to serverless functions (FaaS). There are no servers for the customer to "
                "patch, but a review warns that an over-permissioned function could be abused to access unrelated "
                "cloud resources if compromised. Which customer-side control is MOST important here?",
        "options": [
            {"id": "A", "text": "Choosing a larger memory allocation for each function"},
            {"id": "B", "text": "Scoping each function's execution role to least-privilege permissions (only the specific resources/actions it needs), plus validating event input and securing dependencies"},
            {"id": "C", "text": "Running an antivirus agent inside the function runtime"},
            {"id": "D", "text": "Leaving broad permissions to avoid runtime errors"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Because the provider patches the underlying platform, the customer's key control is least "
                       "privilege: give each function only the permissions it needs, so a compromised function cannot pivot to other resources. Input validation and secure dependencies round out the posture.",
            "distractors": {
                "A": "Memory sizing affects performance/cost, not the blast radius of an over-permissioned function.",
                "C": "There is no persistent server to run a traditional AV agent on; the control is scoping permissions and securing code/deps.",
                "D": "Leaving broad permissions is exactly the risk; it maximizes what a compromised function can reach.",
            },
            "exam_pattern": "Serverless customer control = least-privilege function execution role (+ input validation, secure deps); provider patches the platform.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (serverless security, least privilege)"],
    },
    {
        "id": "securityx-arch-r2-017", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise with dozens of cloud accounts wants to PREVENT any account - regardless of local admin "
                "rights - from disabling audit logging or deploying resources in unapproved regions, enforced "
                "centrally and preventively. Which capability BEST provides these organization-wide guardrails?",
        "options": [
            {"id": "A", "text": "Organization-wide preventive guardrails (e.g., service control policies) applied across all accounts in a governed landing zone"},
            {"id": "B", "text": "A detective alert emailed after a violation occurs"},
            {"id": "C", "text": "Asking each account owner to follow a written policy"},
            {"id": "D", "text": "A single shared root account used by everyone"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Organization-level guardrails (such as service control policies in a landing zone) set "
                       "preventive maximum-permission boundaries that even account administrators cannot exceed - centrally blocking actions like disabling logging or using unapproved regions.",
            "distractors": {
                "B": "A post-violation email is detective and too late; the goal is prevention.",
                "C": "Relying on written policy depends on each owner's compliance and enforces nothing automatically.",
                "D": "A shared root account is a severe security anti-pattern with no separation or guardrails.",
            },
            "exam_pattern": "Preventive, org-wide boundaries no account can exceed = service control policies/guardrails in a landing zone.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (cloud governance, landing zone, guardrails/SCPs)"],
    },

    # ===== scx_resilience_ha ================================================
    {
        "id": "securityx-arch-r2-018", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 3, "type": "mcq",
        "stem": "A business system is assigned an RPO of 1 hour and an RTO of 4 hours. Cost efficiency matters, so "
                "the design should MEET these targets without gold-plating. Which recovery design is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Continuous synchronous replication to an always-on hot site (near-zero RPO/RTO)"},
            {"id": "B", "text": "Nightly full backups shipped offsite, restored to newly procured hardware after an event"},
            {"id": "C", "text": "Asynchronous replication/backups at least hourly to a warm standby that can be brought online within a few hours"},
            {"id": "D", "text": "Weekly backups retained on the same production array"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Hourly (or more frequent) asynchronous replication/backups satisfy a 1-hour RPO, and a warm "
                       "standby that can be activated within a few hours satisfies a 4-hour RTO - matching the targets cost-effectively without the expense of a continuously synchronized hot site.",
            "distractors": {
                "A": "A synchronous hot site far exceeds (and over-spends on) a 1-hour/4-hour requirement - that is gold-plating.",
                "B": "Nightly backups can lose up to ~24 hours of data (violating the 1-hour RPO), and procuring/restoring hardware likely blows the 4-hour RTO.",
                "D": "Weekly backups on the production array violate the RPO and offer no site resilience.",
            },
            "exam_pattern": "Match design to RTO/RPO: ~hourly async + warm standby meets 1h/4h without over-provisioning a hot site.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (matching recovery design to RTO/RPO)"],
    },
    {
        "id": "securityx-arch-r2-019", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 2, "type": "mcq",
        "stem": "A reliability engineer is documenting availability metrics. Which metric expresses the AVERAGE time "
                "required to repair a failed component and restore it to service?",
        "options": [
            {"id": "A", "text": "Mean time between failures (MTBF)"},
            {"id": "B", "text": "Mean time to repair/recover (MTTR)"},
            {"id": "C", "text": "Mean time to failure (MTTF)"},
            {"id": "D", "text": "Recovery point objective (RPO)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "MTTR (mean time to repair/recover) is the average time to fix a failed component and return it "
                       "to operation; lowering MTTR improves availability.",
            "distractors": {
                "A": "MTBF is the average time between failures of a repairable system - reliability between outages, not repair duration.",
                "C": "MTTF is the average lifespan to failure of a non-repairable component, not the time to repair it.",
                "D": "RPO is the maximum tolerable data loss (a recovery objective), not a repair-time metric.",
            },
            "exam_pattern": "MTTR = time to repair/restore; MTBF = time between failures (repairable); MTTF = lifespan (non-repairable).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (MTTR, MTBF, MTTF)"],
    },
    {
        "id": "securityx-arch-r2-020", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 3, "type": "mcq",
        "stem": "A high-traffic service wants to use ALL of its redundant nodes to share production load AND survive "
                "the loss of a node with no failover delay, and the team can manage the added complexity of keeping "
                "state consistent. Which high-availability model BEST fits?",
        "options": [
            {"id": "A", "text": "Active-passive, where the standby node sits idle until the primary fails"},
            {"id": "B", "text": "A single oversized server with a bigger power supply"},
            {"id": "C", "text": "Cold standby hardware kept powered off"},
            {"id": "D", "text": "Active-active, where all nodes serve traffic simultaneously and the loss of one is absorbed by the others without a failover switchover"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Active-active runs all nodes serving traffic at once, so capacity is fully utilized and the loss "
                       "of a node is absorbed immediately with no failover delay - at the cost of greater complexity (state/session consistency, data synchronization).",
            "distractors": {
                "A": "Active-passive leaves the standby idle (wasted capacity) and incurs a failover switchover delay when the primary fails.",
                "B": "A single larger server is still a single point of failure, not a redundant HA design.",
                "C": "Cold standby must be powered on and prepared after a failure, introducing significant downtime.",
            },
            "exam_pattern": "Use all nodes + instant absorption of a node loss = active-active (more complex state sync); active-passive = idle standby + failover delay.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (active-active vs active-passive)"],
    },
    {
        "id": "securityx-arch-r2-021", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 2, "type": "mcq",
        "stem": "To build a business continuity and disaster recovery program, an organization first needs to "
                "identify its critical business processes, the impact of their disruption over time, their "
                "dependencies, and the resulting recovery objectives (RTO/RPO) and maximum tolerable downtime. Which "
                "activity produces this?",
        "options": [
            {"id": "A", "text": "A business impact analysis (BIA)"},
            {"id": "B", "text": "A penetration test"},
            {"id": "C", "text": "A code review"},
            {"id": "D", "text": "A firewall rule audit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A BIA identifies critical processes, quantifies the impact of disruption over time, maps "
                       "dependencies, and derives recovery objectives (RTO/RPO) and maximum tolerable downtime - the foundation of BC/DR planning.",
            "distractors": {
                "B": "A penetration test assesses exploitable weaknesses, not business-process criticality and recovery objectives.",
                "C": "A code review examines software quality/security, not continuity priorities.",
                "D": "A firewall rule audit checks network controls, not critical-process impact and recovery targets.",
            },
            "exam_pattern": "Identify critical processes + impact-over-time + RTO/RPO/MTD = business impact analysis (BIA), the basis of BC/DR.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (business impact analysis)"],
    },
    {
        "id": "securityx-arch-r2-022", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 3, "type": "mcq",
        "stem": "A backup strategy uses a weekly full backup. The team debates nightly incremental versus nightly "
                "differential backups. Which statement correctly captures the trade-off?",
        "options": [
            {"id": "A", "text": "Incremental backups are larger each night but restore fastest; differentials are smaller but restore slowest"},
            {"id": "B", "text": "Both incremental and differential require only the latest backup file to fully restore"},
            {"id": "C", "text": "Incrementals back up only changes since the last backup (small, fast backups) but a full restore needs the full plus every incremental in order; differentials back up changes since the last full (growing nightly) but restore from only the full plus the latest differential"},
            {"id": "D", "text": "Differential backups cannot be combined with a full backup"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Incrementals capture changes since the last backup of any type - small, quick to create - but "
                       "restoring requires the full plus every incremental in sequence (slower restore). Differentials capture changes since the last full - larger each night - but restore needs only the full plus the most recent differential (faster restore).",
            "distractors": {
                "A": "This is reversed: incrementals are the smallest to create but slowest to restore; differentials grow but restore faster.",
                "B": "Only a full backup alone restores from one file; incrementals/differentials also need the base full.",
                "D": "Differentials are specifically designed to be combined with a full backup for restoration.",
            },
            "exam_pattern": "Incremental = smallest/fastest backup, slowest restore (full + all increments); differential = larger backup, faster restore (full + latest differential).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (backup types: full/incremental/differential trade-offs)"],
    },
    {
        "id": "securityx-arch-r2-023", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 3, "type": "mcq",
        "stem": "A company replicates a transactional database to a disaster-recovery region on another continent. "
                "The application is highly sensitive to write latency, and the business can tolerate losing a few "
                "seconds of recent transactions in a disaster. Which replication approach is MOST appropriate, and why?",
        "options": [
            {"id": "A", "text": "Synchronous replication, because it guarantees zero data loss regardless of distance"},
            {"id": "B", "text": "Asynchronous replication, because long-distance synchronous replication would add round-trip latency to every write; async accepts a small RPO (seconds) while preserving write performance"},
            {"id": "C", "text": "No replication; rely on weekly tape backups"},
            {"id": "D", "text": "Synchronous replication with the DR site in the same rack as production"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Over intercontinental distances, synchronous replication forces each write to wait for the remote "
                       "commit, badly hurting a latency-sensitive app. Asynchronous replication preserves local write performance and accepts a small RPO (seconds of potential loss) - matching the stated tolerance.",
            "distractors": {
                "A": "Synchronous does give near-zero RPO, but across a continent its added write latency would cripple a latency-sensitive application - and the business accepts a few seconds of loss anyway.",
                "C": "Weekly tape backups violate a seconds-level RPO and provide no timely DR.",
                "D": "Placing the DR site in the same rack defeats the purpose of geographic disaster recovery (a single local disaster takes out both).",
            },
            "exam_pattern": "Long-distance + latency-sensitive + small RPO tolerable -> async replication; sync = zero RPO but latency/distance-limited.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (synchronous vs asynchronous replication, RPO/latency trade-off)"],
    },

    # ===== scx_data_security_arch ===========================================
    {
        "id": "securityx-arch-r2-024", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 2, "type": "mcq",
        "stem": "A company must prevent employees from exfiltrating classified data via email, USB drives, and cloud "
                "uploads, enforcing policy based on the content and classification of the data in motion and at rest. "
                "Which technology is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Data loss prevention (DLP) across network, endpoint, and cloud channels using content and context inspection"},
            {"id": "B", "text": "A hardware security module (HSM)"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A certificate authority (CA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DLP inspects content and context to detect and block unauthorized movement of sensitive/classified "
                       "data across channels (email, web/cloud uploads, USB, endpoints), enforcing policy aligned to data classification.",
            "distractors": {
                "B": "An HSM protects cryptographic keys; it does not inspect data flows for exfiltration.",
                "C": "A load balancer distributes traffic and does not enforce data-handling policy.",
                "D": "A CA issues certificates; it is unrelated to detecting/blocking sensitive-data exfiltration.",
            },
            "exam_pattern": "Detect/block exfiltration of classified data across channels = DLP (content + context inspection), driven by classification.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (data loss prevention)"],
    },
    {
        "id": "securityx-arch-r2-025", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A team needs to give developers a realistic COPY of production data for lower environments, but every "
                "sensitive field (names, SSNs, card numbers) must be permanently replaced with realistic but fake "
                "values in that copy, so the real data never exists in non-production. Which technique fits BEST?",
        "options": [
            {"id": "A", "text": "Dynamic data masking applied at query time on the production database"},
            {"id": "B", "text": "Transparent data encryption (TDE) on the production database"},
            {"id": "C", "text": "Static data masking: create a sanitized copy in which sensitive values are irreversibly replaced before the data lands in non-production"},
            {"id": "D", "text": "Row-level security on the production database"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Static data masking produces a sanitized dataset in which sensitive values are permanently "
                       "substituted, so non-production environments never contain real sensitive data - ideal for dev/test copies.",
            "distractors": {
                "A": "Dynamic masking obfuscates results on the fly while the underlying production data stays real and in place; it does not create a sanitized copy for lower environments.",
                "B": "TDE encrypts data at rest but decrypts transparently for authorized users; a copy would still contain the real values once accessed.",
                "D": "Row-level security filters which rows a principal sees; it does not replace sensitive field values in a dev copy.",
            },
            "exam_pattern": "Sanitized non-prod copy with sensitive values permanently replaced = static data masking; dynamic masking = real-time, data unchanged.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (static vs dynamic data masking)"],
    },
    {
        "id": "securityx-arch-r2-026", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A regulation requires that stored card numbers remain unreadable even to database administrators and "
                "other privileged database users - not just protected against theft of the physical storage. Which "
                "encryption approach BEST meets this requirement?",
        "options": [
            {"id": "A", "text": "Transparent data encryption (TDE) at the database/storage level only"},
            {"id": "B", "text": "Application-layer or column/field-level encryption, where data is encrypted before it reaches the database and the DBMS/DBAs only ever see ciphertext"},
            {"id": "C", "text": "Full-disk encryption on the database server"},
            {"id": "D", "text": "Enabling TLS between the app and the database"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Encrypting at the application layer (or column/field level) so values are already ciphertext when "
                       "stored means the database engine and DBAs never see plaintext - protecting against privileged insiders, at the cost of some query/functionality limits on encrypted fields.",
            "distractors": {
                "A": "TDE protects data at rest from media theft but decrypts transparently for authorized DB sessions, so DBAs/privileged users can still read plaintext.",
                "C": "Full-disk encryption protects against stolen disks, not against authorized database users reading data.",
                "D": "TLS protects data in transit between app and DB; it does not keep stored values unreadable to DBAs.",
            },
            "exam_pattern": "Hide data from DBAs/privileged DB users -> application/column-level encryption (DB sees only ciphertext); TDE/FDE protect media, not from authorized users.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (database encryption: TDE vs application/column-level)"],
    },
    {
        "id": "securityx-arch-r2-027", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A regulated customer stores data with a public cloud provider but must ensure the provider is "
                "TECHNICALLY unable to decrypt that data - the customer must retain exclusive control of the "
                "encryption keys outside the provider's reach. Which key-management model BEST satisfies this?",
        "options": [
            {"id": "A", "text": "Provider-managed keys in the provider's default KMS"},
            {"id": "B", "text": "Bring Your Own Key (BYOK), importing the customer's key into the provider's KMS"},
            {"id": "C", "text": "Letting the provider generate and fully manage all keys with rotation"},
            {"id": "D", "text": "Hold Your Own Key (HYOK): keys are generated and retained in a customer-controlled HSM/key store and never released to the provider, so the provider cannot decrypt"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "HYOK keeps key material entirely within the customer's own HSM/key management, so the provider "
                       "never possesses the keys and is technically unable to decrypt the data - the strongest control for provider-exclusion requirements.",
            "distractors": {
                "A": "Provider-managed keys mean the provider holds the keys and can technically decrypt the data.",
                "B": "With BYOK the customer supplies key material, but it is imported into and used by the provider's KMS, so the provider can still perform decryption.",
                "C": "Provider-generated and -managed keys leave the provider fully able to decrypt.",
            },
            "exam_pattern": "Provider must be unable to decrypt -> HYOK (keys stay in customer HSM); BYOK/provider-managed still let the provider's KMS use the key.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (key management: HYOK vs BYOK vs provider-managed)"],
    },
    {
        "id": "securityx-arch-r2-028", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A company shares sensitive design documents with external partners and must retain control AFTER the "
                "file leaves its network - restricting who can open, print, or forward it, enforcing expiration, and "
                "revoking access even on the recipient's device. Which technology provides this persistent protection?",
        "options": [
            {"id": "A", "text": "Information rights management (IRM)/digital rights management (DRM), which embeds persistent, policy-enforced usage controls that travel with the file"},
            {"id": "B", "text": "A network firewall rule"},
            {"id": "C", "text": "Full-disk encryption on the company's own servers"},
            {"id": "D", "text": "A one-time DLP block at the email gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IRM/DRM applies persistent, policy-based controls (open/print/forward/expire/revoke) that remain "
                       "attached to the document wherever it goes, so protection and revocation work even after the file leaves the network and reaches a partner's device.",
            "distractors": {
                "B": "A firewall rule controls network traffic, not usage of a document after delivery.",
                "C": "Full-disk encryption protects data on the company's servers, not a copy sitting on a partner's device.",
                "D": "A DLP block can stop the file from leaving but provides no control once a file is legitimately shared.",
            },
            "exam_pattern": "Control a document after it leaves (open/print/forward/expire/revoke) = IRM/DRM (protection travels with the file).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (IRM/DRM, persistent protection)"],
    },
    {
        "id": "securityx-arch-r2-029", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants protection controls (encryption requirements, access restrictions, and DLP "
                "handling) to be applied AUTOMATICALLY based on how sensitive a file is, rather than relying on users "
                "to remember each rule. Which approach BEST enables this?",
        "options": [
            {"id": "A", "text": "Give every file the same baseline protection regardless of content"},
            {"id": "B", "text": "Train users annually and hope they apply the right controls manually"},
            {"id": "C", "text": "Apply data classification/sensitivity labels to content so downstream controls (encryption, access, DLP) are enforced automatically according to the label"},
            {"id": "D", "text": "Store everything in a single shared drive with open permissions"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Classification/sensitivity labeling tags data by sensitivity, and downstream systems enforce the "
                       "right protection (encryption, access restrictions, DLP policy) automatically based on the label - making protection consistent and proportional to sensitivity.",
            "distractors": {
                "A": "Uniform baseline protection either over-protects low-sensitivity data or under-protects high-sensitivity data.",
                "B": "Relying on users to manually apply controls is inconsistent and error-prone.",
                "D": "Open permissions on a shared drive ignore sensitivity entirely and expose data.",
            },
            "exam_pattern": "Protection proportional to sensitivity, applied automatically = classification/sensitivity labels driving downstream controls.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (classification/sensitivity labeling driving controls)"],
    },

    # ===== scx_iam_architecture =============================================
    {
        "id": "securityx-arch-r2-030", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise needs access decisions that depend on MULTIPLE dynamic attributes at request time - "
                "user department and clearance, data classification, device posture, location, and time of day - and "
                "it finds that creating a static role for every combination has caused unmanageable 'role explosion.' "
                "Which access-control model BEST fits?",
        "options": [
            {"id": "A", "text": "Discretionary access control (DAC) based on resource-owner discretion"},
            {"id": "B", "text": "Attribute-based access control (ABAC), where policies evaluate subject, resource, action, and environment attributes dynamically"},
            {"id": "C", "text": "Pure role-based access control (RBAC) with one role per combination"},
            {"id": "D", "text": "Rule-based ACLs on each switch port"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ABAC evaluates policies over many attributes (subject, resource, action, environment/context) at "
                       "request time, expressing fine-grained, dynamic rules without exploding the number of static roles - ideal for context-dependent access.",
            "distractors": {
                "A": "DAC lets owners grant access at their discretion; it does not centrally evaluate dynamic context attributes.",
                "C": "RBAC's static roles are exactly what causes role explosion when access depends on many dynamic attributes.",
                "D": "Switch-port ACLs control network access by port/address, not fine-grained, attribute-based application authorization.",
            },
            "exam_pattern": "Dynamic, multi-attribute, context-aware access without role explosion = ABAC; RBAC = static roles.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (ABAC vs RBAC)"],
    },
    {
        "id": "securityx-arch-r2-031", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "mcq",
        "stem": "Despite MFA, employees keep getting compromised: attackers phish one-time codes on fake login pages "
                "and spam push notifications until a user approves (MFA fatigue). Security needs phishing-RESISTANT "
                "authentication. Which option BEST meets this?",
        "options": [
            {"id": "A", "text": "FIDO2/WebAuthn security keys or passkeys, which use origin-bound public-key cryptography that will not authenticate to a spoofed domain"},
            {"id": "B", "text": "SMS one-time passcodes"},
            {"id": "C", "text": "Time-based one-time passwords (TOTP) from an authenticator app"},
            {"id": "D", "text": "Simple approve/deny push notifications"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FIDO2/WebAuthn (security keys/passkeys) bind the credential to the legitimate site's origin and "
                       "use public-key cryptography, so an attacker's phishing site cannot elicit a usable response - defeating both credential phishing and push-fatigue attacks.",
            "distractors": {
                "B": "SMS OTPs can be phished (entered on a fake page) and are also vulnerable to SIM swapping.",
                "C": "TOTP codes can be phished in real time on a spoofed login page; they are not origin-bound.",
                "D": "Approve/deny push prompts are susceptible to MFA-fatigue/push-bombing and accidental approvals.",
            },
            "exam_pattern": "Phishing-resistant MFA = FIDO2/WebAuthn/passkeys (origin-bound, public-key); OTP/TOTP/push are phishable.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (phishing-resistant MFA, FIDO2/WebAuthn)"],
    },
    {
        "id": "securityx-arch-r2-032", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise wants accounts in its many SaaS applications to be automatically created, updated, and "
                "DEPROVISIONED as employees join, change roles, or leave - driven from the central identity provider "
                "and HR source. Which standard is designed to automate this cross-domain user provisioning?",
        "options": [
            {"id": "A", "text": "SAML"},
            {"id": "B", "text": "OAuth 2.0"},
            {"id": "C", "text": "RADIUS"},
            {"id": "D", "text": "SCIM (System for Cross-domain Identity Management)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SCIM standardizes automated provisioning/deprovisioning of identities across applications, so "
                       "joiner/mover/leaver changes propagate from the IdP/HR source to SaaS apps - critical for timely deprovisioning when someone leaves.",
            "distractors": {
                "A": "SAML handles federated authentication/SSO (asserting who a user is), not lifecycle account provisioning.",
                "B": "OAuth 2.0 handles delegated authorization (access tokens), not user account provisioning.",
                "C": "RADIUS provides AAA for network access, not SaaS account provisioning.",
            },
            "exam_pattern": "Automate create/update/deprovision accounts across apps (joiner/mover/leaver) = SCIM; SAML/OAuth = authN/authZ, not provisioning.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (SCIM, identity lifecycle/provisioning)"],
    },
    {
        "id": "securityx-arch-r2-033", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "mcq",
        "stem": "Security wants low-friction logins for users on managed devices from expected locations, but wants to "
                "automatically require step-up MFA or block access when risk signals appear (impossible travel, an "
                "unmanaged device, or anomalous behavior). Which capability BEST delivers this?",
        "options": [
            {"id": "A", "text": "A fixed rule that always requires a password only"},
            {"id": "B", "text": "Conditional access with risk-based adaptive authentication that evaluates identity, device, location, and behavior signals and adjusts requirements dynamically"},
            {"id": "C", "text": "Disabling MFA entirely to reduce friction"},
            {"id": "D", "text": "Allowing access from any device as long as the password is correct"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Conditional access / risk-based adaptive authentication evaluates signals (user/device/location/"
                       "behavior risk) per sign-in and dynamically adjusts - allowing low friction when risk is low and requiring step-up MFA or blocking when risk is high.",
            "distractors": {
                "A": "A static password-only rule neither reduces friction safely nor responds to risk signals.",
                "C": "Disabling MFA removes a critical control and increases account-takeover risk.",
                "D": "Password-only from any device ignores device posture and risk, enabling easy compromise.",
            },
            "exam_pattern": "Adjust auth requirements by real-time risk (step-up/block) = conditional access / risk-based adaptive authentication.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (conditional access, adaptive/risk-based authentication)"],
    },
    {
        "id": "securityx-arch-r2-034", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "mcq",
        "stem": "An audit finds long-tenured employees have accumulated access rights from past roles they no longer "
                "need (privilege creep). Leadership wants a recurring process where managers and resource owners "
                "review and attest to each user's entitlements, removing what is no longer justified. Which IAM "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "Identity governance and administration (IGA) access certification/recertification campaigns"},
            {"id": "B", "text": "Single sign-on (SSO)"},
            {"id": "C", "text": "A password-complexity policy"},
            {"id": "D", "text": "A network intrusion prevention system (IPS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IGA access certification (recertification) campaigns periodically require managers/owners to "
                       "review and attest to users' entitlements, revoking access that is no longer justified - the direct remedy for privilege creep.",
            "distractors": {
                "B": "SSO simplifies authentication across apps; it does not review or remove accumulated entitlements.",
                "C": "Password complexity strengthens credentials but does nothing about excessive accumulated access.",
                "D": "An IPS blocks network attacks; it does not govern user entitlements.",
            },
            "exam_pattern": "Fix privilege creep via periodic review/attestation of entitlements = IGA access certification/recertification.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (identity governance, access recertification)"],
    },

    # ================= DOMAIN 4: SECURITY OPERATIONS ========================
    # ===== scx_threat_hunting ===============================================
    {
        "id": "securityx-ops-r2-001", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "An analyst wants to model an intrusion as a sequence of stages - reconnaissance, weaponization, "
                "delivery, exploitation, installation, command-and-control, and actions on objectives - so defenders "
                "can intervene as EARLY in the sequence as possible to break it. Which framework is this?",
        "options": [
            {"id": "A", "text": "The Diamond Model of Intrusion Analysis"},
            {"id": "B", "text": "The Lockheed Martin Cyber Kill Chain"},
            {"id": "C", "text": "The NIST SP 800-61 incident-response lifecycle"},
            {"id": "D", "text": "The OWASP Top 10"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Cyber Kill Chain models an attack as sequential phases; defenders aim to detect and disrupt "
                       "the chain as early as possible (e.g., at delivery/exploitation) to stop the adversary before they reach their objective.",
            "distractors": {
                "A": "The Diamond Model analyzes a single intrusion event by relating adversary, capability, infrastructure, and victim - it is not a linear phase sequence.",
                "C": "NIST SP 800-61 describes the defender's incident-response lifecycle, not the attacker's intrusion phases.",
                "D": "The OWASP Top 10 ranks web-application risks, not intrusion phases.",
            },
            "exam_pattern": "Sequential attack phases, break it early = Cyber Kill Chain; Diamond Model = event feature relationships (adversary/capability/infrastructure/victim).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (Cyber Kill Chain)"],
    },
    {
        "id": "securityx-ops-r2-002", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "An intelligence analyst wants a model that relates the four core features of any intrusion event - "
                "the adversary, their capability (malware/tools), the infrastructure they use, and the victim - to "
                "pivot from one known feature to discover the others. Which model is this?",
        "options": [
            {"id": "A", "text": "The Cyber Kill Chain"},
            {"id": "B", "text": "The MITRE ATT&CK matrix"},
            {"id": "C", "text": "The Diamond Model of Intrusion Analysis"},
            {"id": "D", "text": "The STRIDE threat model"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Diamond Model represents each intrusion event as adversary, capability, infrastructure, and "
                       "victim, with relationships that let analysts pivot (e.g., from infrastructure to other victims or capabilities) during analysis.",
            "distractors": {
                "A": "The Cyber Kill Chain models sequential attack phases, not the four related event features.",
                "B": "ATT&CK is a knowledge base of tactics/techniques; it is not the four-feature event model.",
                "D": "STRIDE categorizes software threat types (spoofing, tampering, etc.) during design, not intrusion-event feature analysis.",
            },
            "exam_pattern": "Adversary + capability + infrastructure + victim with pivoting = Diamond Model.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (Diamond Model of Intrusion Analysis)"],
    },
    {
        "id": "securityx-ops-r2-003", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A board asks the CISO for high-level, non-technical analysis of threat trends, adversary "
                "motivations, and geopolitical risk to guide multi-year security investment. Which category of threat "
                "intelligence BEST serves this need?",
        "options": [
            {"id": "A", "text": "Strategic threat intelligence"},
            {"id": "B", "text": "Technical threat intelligence (atomic IOCs)"},
            {"id": "C", "text": "Tactical threat intelligence (adversary TTPs)"},
            {"id": "D", "text": "Operational threat intelligence (specific imminent campaigns)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Strategic threat intelligence is high-level and non-technical, covering trends, motivations, and "
                       "geopolitical/industry risk to inform long-term strategy and investment for executives and boards.",
            "distractors": {
                "B": "Technical intelligence consists of atomic indicators (hashes, IPs, domains) consumed by tools - too granular for board strategy.",
                "C": "Tactical intelligence describes adversary TTPs for defenders tuning detections, not executive strategy.",
                "D": "Operational intelligence concerns specific impending attacks/campaigns, not long-horizon strategic planning.",
            },
            "exam_pattern": "Board/long-term/non-technical = strategic intel; TTPs = tactical; IOCs = technical; imminent campaigns = operational.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (threat intelligence levels)"],
    },
    {
        "id": "securityx-ops-r2-004", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 2, "type": "mcq",
        "stem": "An ISAC wants members to exchange machine-readable cyber threat intelligence automatically, using a "
                "standardized data format for the intelligence and a standardized protocol for transporting it "
                "between systems. Which pairing provides this?",
        "options": [
            {"id": "A", "text": "SCAP and OVAL"},
            {"id": "B", "text": "SNMP and NetFlow"},
            {"id": "C", "text": "SAML and SCIM"},
            {"id": "D", "text": "STIX (structured data format) and TAXII (transport protocol)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "STIX provides a standardized, structured language for representing threat intelligence, and TAXII "
                       "defines how to transport/exchange that STIX data between systems - together enabling automated intel sharing.",
            "distractors": {
                "A": "SCAP/OVAL standardize configuration and vulnerability assessment content, not threat-intel exchange.",
                "B": "SNMP and NetFlow handle device management and network flow data, not threat-intel sharing.",
                "C": "SAML and SCIM handle federation and identity provisioning, unrelated to threat-intel exchange.",
            },
            "exam_pattern": "Automated threat-intel sharing = STIX (format) + TAXII (transport).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (STIX/TAXII, intel sharing)"],
    },
    {
        "id": "securityx-ops-r2-005", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_threat_hunting", "difficulty": 3, "type": "mcq",
        "stem": "A successful threat hunt uncovers a repeatable malicious pattern in log data. The team wants to turn "
                "it into a DURABLE, automated detection that is vendor-agnostic and can be shared and translated "
                "across different SIEM platforms. Which approach BEST accomplishes this?",
        "options": [
            {"id": "A", "text": "Keep re-running the manual hunt query every week by hand"},
            {"id": "B", "text": "Codify the logic as a Sigma rule (a generic, shareable SIEM log-detection format) and deploy it as an automated detection"},
            {"id": "C", "text": "Write a YARA rule to scan files on disk"},
            {"id": "D", "text": "Add a Snort signature for raw network packets"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Sigma is a generic, vendor-neutral rule format for log-based SIEM detections; codifying the hunt "
                       "as a Sigma rule makes it durable, automated, and translatable across SIEMs (detection engineering).",
            "distractors": {
                "A": "Manually re-running the query is not durable or automated and does not scale or share.",
                "C": "YARA matches patterns in files/memory (malware identification), not log-based SIEM detection of this pattern.",
                "D": "Snort signatures inspect network packets; the pattern here is in log data, so a log-detection rule (Sigma) is the right abstraction.",
            },
            "exam_pattern": "Turn a hunt into a portable, automated log detection = Sigma rule; YARA = files, Snort/Suricata = network packets.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Threat hunting (detection engineering, Sigma rules)"],
    },

    # ===== scx_incident_response ============================================
    {
        "id": "securityx-ops-r2-006", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 3, "type": "mcq",
        "stem": "During an incident, many internal hosts are beaconing to a set of known malicious command-and-control "
                "domains. Responders need to cut off C2 and identify every infected host, while keeping the hosts "
                "running for live analysis. Which containment technique BEST accomplishes this?",
        "options": [
            {"id": "A", "text": "Immediately power off every host that might be infected"},
            {"id": "B", "text": "Do nothing until the full investigation finishes"},
            {"id": "C", "text": "DNS sinkholing: redirect the malicious C2 domains to a controlled sinkhole, severing C2 while logging which internal hosts attempt to resolve/connect (revealing the infected population)"},
            {"id": "D", "text": "Publicly post the C2 domains and ask the internet to block them"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DNS sinkholing points the malicious domains to a controlled server, cutting command-and-control "
                       "and simultaneously surfacing which internal hosts try to reach them - enabling identification of infected systems without immediately destroying live evidence.",
            "distractors": {
                "A": "Powering off hosts destroys volatile evidence and may not be necessary for containment that a sinkhole already achieves.",
                "B": "Waiting lets the malware continue operating and spreading - containment must be prompt.",
                "D": "Public posting tips off the adversary and does nothing to sever your internal hosts' C2 or identify them.",
            },
            "exam_pattern": "Sever C2 + enumerate infected hosts while preserving live state = DNS sinkholing.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (containment: DNS sinkholing)"],
    },
    {
        "id": "securityx-ops-r2-007", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 3, "type": "mcq",
        "stem": "After containing an intrusion in which the attacker gained domain-admin rights and installed "
                "multiple backdoors, the team moves to eradication. Which approach is MOST thorough and appropriate?",
        "options": [
            {"id": "A", "text": "Remove all identified malware and persistence (rogue accounts, scheduled tasks, services, implants), reset/rotate all potentially compromised credentials and keys, and rebuild affected systems from known-good media"},
            {"id": "B", "text": "Delete only the single malware file that triggered the alert and return the host to service"},
            {"id": "C", "text": "Restore the systems from a backup taken after the compromise occurred"},
            {"id": "D", "text": "Apply the missing patch and consider the host clean without further action"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With admin-level compromise and multiple backdoors, eradication must remove all malware and "
                       "persistence mechanisms, rotate all credentials/keys the attacker could have captured, and rebuild affected systems from known-good media - since trust in the compromised systems cannot be assured.",
            "distractors": {
                "B": "Deleting one visible file leaves other backdoors, accounts, and persistence in place for re-entry.",
                "C": "A backup taken after the compromise likely contains the attacker's implants/persistence, reintroducing them.",
                "D": "Patching the entry point does not remove established backdoors or compromised credentials.",
            },
            "exam_pattern": "Eradicate deep compromise = remove all persistence + rotate credentials/keys + rebuild from known-good media (don't trust the box).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (eradication, persistence removal, rebuild)"],
    },
    {
        "id": "securityx-ops-r2-008", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "Following eradication, the team is ready to restore services. Which recovery approach BEST balances "
                "returning to operations with avoiding reinfection?",
        "options": [
            {"id": "A", "text": "Reconnect every system to production at once with no additional monitoring"},
            {"id": "B", "text": "Return systems but skip patching the exploited vulnerability to save time"},
            {"id": "C", "text": "Restore from backups taken before the compromise without verifying integrity"},
            {"id": "D", "text": "Restore from clean/known-good backups, patch the exploited weakness, validate integrity, and bring systems back in a phased manner with heightened monitoring for signs of reinfection or the attacker's return"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Sound recovery restores from clean backups, remediates the exploited weakness, verifies integrity, "
                       "and returns systems in phases with enhanced monitoring - so any recurrence or attacker return is caught quickly before full normal operations resume.",
            "distractors": {
                "A": "A simultaneous, unmonitored return risks silent reinfection spreading again with no early warning.",
                "B": "Skipping the patch leaves the original entry point open for immediate re-exploitation.",
                "C": "Unverified pre-compromise backups may still be vulnerable or tampered; integrity must be validated.",
            },
            "exam_pattern": "Recovery = clean backups + patch the root cause + verify integrity + phased return with heightened monitoring for reinfection.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (recovery, validation, monitoring for reinfection)"],
    },
    {
        "id": "securityx-ops-r2-009", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 3, "type": "mcq",
        "stem": "A confirmed breach likely exposed regulated personal data. Which approach to legal/communications "
                "coordination during the response is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Have any available employee speak to the press with technical details as they emerge"},
            {"id": "B", "text": "Engage legal counsel early (often directing the investigation to preserve privilege), meet regulatory breach-notification obligations and timelines, coordinate with law enforcement as appropriate, and make controlled, accurate disclosures without tipping off the attacker"},
            {"id": "C", "text": "Publicly publish full technical indicators and the investigation's live findings immediately, before scoping is complete"},
            {"id": "D", "text": "Avoid notifying regulators to prevent reputational harm"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Breach response must coordinate through legal/comms: involve counsel early (which can preserve "
                       "attorney-client privilege over the investigation), satisfy regulatory notification duties and timelines, work with law enforcement where appropriate, and issue controlled, accurate communications that do not alert the adversary.",
            "distractors": {
                "A": "Uncontrolled employee statements risk inaccuracy, legal exposure, and tipping off the attacker.",
                "C": "Premature public disclosure before scoping can be inaccurate, aid the attacker, and create legal/regulatory problems.",
                "D": "Failing to notify regulators when required violates law and worsens liability.",
            },
            "exam_pattern": "Breach comms = counsel early (privilege) + meet regulatory notification duties + coordinate LE + controlled disclosure; don't tip off the attacker or go rogue publicly.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (legal coordination, breach notification, communications)"],
    },
    {
        "id": "securityx-ops-r2-010", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "A SOC is flooded with simultaneous alerts of varying seriousness and limited responders. Which "
                "practice MOST directly ensures the most damaging incidents receive resources and escalation first?",
        "options": [
            {"id": "A", "text": "Triage: classify incidents by severity and business impact to prioritize response and trigger appropriate escalation/notification"},
            {"id": "B", "text": "Handle alerts strictly in the order they arrived (first in, first out)"},
            {"id": "C", "text": "Work whichever alert is easiest to close first"},
            {"id": "D", "text": "Wait until all alerts stop before acting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Triage classifies incidents by severity and business impact so limited responders focus first on "
                       "the highest-impact events and escalate/notify appropriately - the core of effective incident prioritization.",
            "distractors": {
                "B": "FIFO ignores impact and may leave a catastrophic incident waiting behind trivial ones.",
                "C": "Closing the easiest alerts first optimizes convenience, not risk reduction.",
                "D": "Waiting for alerts to stop allows the most damaging incidents to progress unchecked.",
            },
            "exam_pattern": "Prioritize response under load = triage/classify by severity + business impact (not FIFO or easiest-first).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (triage, severity classification)"],
    },
    {
        "id": "securityx-ops-r2-011", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_incident_response", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to validate its incident-response plan and the team's decision-making through a "
                "low-cost, discussion-based walkthrough of a hypothetical scenario, WITHOUT touching or disrupting "
                "production systems. Which exercise type is this?",
        "options": [
            {"id": "A", "text": "A full-scale (full-interruption) exercise with real failover"},
            {"id": "B", "text": "A functional exercise that actually executes some response actions on live systems"},
            {"id": "C", "text": "A tabletop exercise"},
            {"id": "D", "text": "An unannounced red-team engagement against production"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A tabletop exercise is a discussion-based, scenario-driven walkthrough where participants talk "
                       "through roles and decisions - low-cost and non-disruptive, with no impact on production systems.",
            "distractors": {
                "A": "A full-scale exercise actually interrupts/fails over real systems - high cost and disruptive.",
                "B": "A functional exercise executes some real response actions on systems, beyond a discussion.",
                "D": "A red-team engagement actively attacks production and is not a discussion-based plan validation.",
            },
            "exam_pattern": "Discussion-based, no production impact, low cost = tabletop; functional = some live actions; full-scale = real failover.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Incident response (exercise types: tabletop/functional/full-scale)"],
    },

    # ===== scx_vuln_management ==============================================
    {
        "id": "securityx-ops-r2-012", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability-management lead is updating scoring guidance to CVSS v4.0. Which statement accurately "
                "describes a change introduced in CVSS v4.0 relative to v3.1?",
        "options": [
            {"id": "A", "text": "CVSS v4.0 removed the Base metric group entirely"},
            {"id": "B", "text": "CVSS v4.0 made the Environmental metrics mandatory and eliminated Base scoring"},
            {"id": "C", "text": "CVSS v4.0 abolished severity ratings and uses only a pass/fail flag"},
            {"id": "D", "text": "CVSS v4.0 retired the single Scope metric and replaced it with distinct impact metrics for the Vulnerable System (VC/VI/VA) and Subsequent System (SC/SI/SA), renamed the Temporal group to Threat, expanded User Interaction to None/Passive/Active, and added optional Supplemental metrics that do not change the numeric score (nomenclature CVSS-B/BT/BE/BTE)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "CVSS v4.0 replaced the often-misused Scope metric with explicit Vulnerable System (VC/VI/VA) and "
                       "Subsequent System (SC/SI/SA) impact metrics, renamed Temporal to the Threat metric group, refined User Interaction to None/Passive/Active, and introduced optional Supplemental metrics (which do not affect the score), with scores named CVSS-B/BT/BE/BTE.",
            "distractors": {
                "A": "The Base metric group remains central in CVSS v4.0; it was not removed.",
                "B": "Environmental metrics stay optional (for tailoring), and Base scoring remains - neither change is real.",
                "C": "CVSS v4.0 still produces a 0.0-10.0 numeric severity score, not a pass/fail flag.",
            },
            "exam_pattern": "CVSS v4.0: Scope -> Vulnerable + Subsequent System impacts; Temporal -> Threat; UI None/Passive/Active; Supplemental (no score change); CVSS-B/BT/BE/BTE.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (CVSS v4.0 changes)"],
    },
    {
        "id": "securityx-ops-r2-013", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 2, "type": "mcq",
        "stem": "A report references several standardized identifiers. Which statement correctly distinguishes a CVE "
                "from a CWE?",
        "options": [
            {"id": "A", "text": "A CVE identifies a specific, publicly disclosed vulnerability in a particular product/version, while a CWE identifies the underlying class/type of software weakness (e.g., CWE-89 SQL injection)"},
            {"id": "B", "text": "A CVE is a product-naming scheme and a CWE is a transport protocol"},
            {"id": "C", "text": "A CVE is a configuration setting identifier and a CWE is an encryption standard"},
            {"id": "D", "text": "CVE and CWE are two names for the same identifier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CVE is a unique identifier for a specific, publicly known vulnerability instance in a product; "
                       "a CWE names the underlying weakness category/type (e.g., CWE-79 cross-site scripting) that such vulnerabilities belong to.",
            "distractors": {
                "B": "Product naming is CPE, and CWE is not a transport protocol - this conflates unrelated schemes.",
                "C": "Configuration identifiers are CCE; CWE is not an encryption standard.",
                "D": "CVE (specific vulnerability) and CWE (weakness class) are distinct, complementary identifiers.",
            },
            "exam_pattern": "CVE = specific vulnerability instance; CWE = weakness class/type; CPE = product name; CCE = configuration.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (CVE vs CWE vs CPE vs CCE)"],
    },
    {
        "id": "securityx-ops-r2-014", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A manager debates which scan-result error type to worry about more. Which statement BEST captures the "
                "risk and the appropriate response regarding false negatives versus false positives in vulnerability scanning?",
        "options": [
            {"id": "A", "text": "False positives are the more dangerous because they always indicate a breach"},
            {"id": "B", "text": "A false negative is the more insidious risk - a real vulnerability goes undetected, leaving exposure the team does not even know about; validating findings and using multiple/authenticated scan techniques helps reduce them, while false positives mainly waste analyst effort"},
            {"id": "C", "text": "Neither matters because scanners are always accurate"},
            {"id": "D", "text": "False negatives are harmless because the vulnerability was not reported"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A false negative means a genuine vulnerability was missed, so the exposure persists unknown and "
                       "unaddressed - the more dangerous error. Mitigate with authenticated and multiple scanning techniques and validation; false positives chiefly consume analyst time.",
            "distractors": {
                "A": "A false positive is a reported issue that is not actually present - it does not indicate a breach.",
                "C": "Scanners are not always accurate; both false positives and negatives occur and must be managed.",
                "D": "A false negative is dangerous precisely because the real, exploitable vulnerability remains and is unknown to defenders.",
            },
            "exam_pattern": "False negative = missed real vuln (dangerous, hidden exposure) -> authenticated/multiple scans + validation; false positive = wasted effort.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (false positives vs false negatives)"],
    },

    {
        "id": "securityx-ops-r2-015", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A critical vulnerability in an internet-facing application is being actively exploited in the wild, "
                "and a vendor patch is available. The normal patch cycle is a quarterly maintenance window weeks away. "
                "Which response BEST balances urgency with operational stability?",
        "options": [
            {"id": "A", "text": "Deploy the patch to all production servers immediately with no testing"},
            {"id": "B", "text": "Wait for the scheduled quarterly maintenance window"},
            {"id": "C", "text": "Invoke an emergency/expedited change: quickly validate the patch in a representative test environment, deploy in a staged/canary rollout with a rollback plan, and prioritize the exposed internet-facing systems first"},
            {"id": "D", "text": "Do nothing and rely on the perimeter firewall"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Active exploitation of an internet-facing system warrants an emergency change: validate quickly in "
                       "a representative environment, roll out in stages (canary) with a rollback plan, and patch the most exposed systems first - fast but controlled.",
            "distractors": {
                "A": "Patching all production at once with zero testing risks a mass outage from a bad patch.",
                "B": "Waiting weeks while the flaw is actively exploited leaves a critical exposure open far too long.",
                "D": "A firewall alone will not stop exploitation of the exposed, actively targeted service.",
            },
            "exam_pattern": "Actively exploited + patch available -> emergency change: quick validation + staged/canary rollout + rollback, exposed systems first.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (patch management, emergency change)"],
    },
    {
        "id": "securityx-ops-r2-016", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 3, "type": "mcq",
        "stem": "A cloud-native environment auto-scales containers and VMs that frequently appear and disappear "
                "within minutes. Traditional scheduled external network scans keep missing these short-lived assets. "
                "Which assessment approach provides the BEST continuous vulnerability coverage?",
        "options": [
            {"id": "A", "text": "Agent-based and pipeline-integrated scanning: scan container images in CI/CD before deployment and use lightweight agents or cloud-API/agentless assessment for continuous coverage of ephemeral instances"},
            {"id": "B", "text": "A single unauthenticated external network scan once per month"},
            {"id": "C", "text": "Scanning only a static list of fixed IP addresses"},
            {"id": "D", "text": "A yearly manual review of the architecture diagram"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ephemeral cloud assets need continuous, build-time and runtime coverage: scan images in the CI/CD "
                       "pipeline before deployment and use agents or cloud-API/agentless assessment to continuously evaluate running instances - so short-lived assets are not missed.",
            "distractors": {
                "B": "A monthly external scan cannot see instances that exist for only minutes.",
                "C": "A static IP list does not match dynamically assigned, ephemeral cloud resources.",
                "D": "An annual diagram review is point-in-time and detects nothing about live vulnerabilities.",
            },
            "exam_pattern": "Ephemeral cloud assets -> shift-left image scanning in CI/CD + agent/cloud-API continuous assessment; scheduled external scans miss them.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (scan types for cloud/ephemeral assets)"],
    },
    {
        "id": "securityx-ops-r2-017", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_vuln_management", "difficulty": 2, "type": "mcq",
        "stem": "An external security researcher privately emails a company detailing an exploitable vulnerability in "
                "its product and offers to withhold public details until it is fixed. Which response reflects mature "
                "vulnerability-management practice?",
        "options": [
            {"id": "A", "text": "Threaten the researcher with legal action for probing the product"},
            {"id": "B", "text": "Ignore the report and hope the issue stays secret"},
            {"id": "C", "text": "Demand the researcher publicly disclose everything immediately"},
            {"id": "D", "text": "Follow a coordinated vulnerability disclosure process: acknowledge the report, triage and validate it, remediate within an agreed timeline, and credit the researcher (ideally via a published disclosure policy or bug-bounty program)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Coordinated vulnerability disclosure acknowledges and triages the report, fixes the issue within "
                       "an agreed timeframe, and credits the researcher - typically formalized through a disclosure policy or bug-bounty program, improving security and goodwill.",
            "distractors": {
                "A": "Legal threats against good-faith researchers discourage reporting and can push findings to full public disclosure.",
                "B": "Ignoring the report leaves users exposed and risks uncoordinated public release.",
                "C": "Forcing immediate public disclosure before a fix endangers users.",
            },
            "exam_pattern": "Researcher reports a bug -> coordinated disclosure (acknowledge, triage, fix on agreed timeline, credit); bug bounty formalizes it.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Vulnerability management (coordinated disclosure, bug bounty)"],
    },

    # ===== scx_monitoring_detection =========================================
    {
        "id": "securityx-ops-r2-018", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 3, "type": "mcq",
        "stem": "A SOC must detect threats on devices that CANNOT run an endpoint agent - unmanaged IoT, OT, and BYOD "
                "systems - by analyzing their behavior on the network (lateral movement, beaconing, anomalous flows). "
                "Which capability is designed for this?",
        "options": [
            {"id": "A", "text": "Endpoint detection and response (EDR)"},
            {"id": "B", "text": "Network detection and response (NDR), which analyzes network traffic/metadata to detect threats without an endpoint agent"},
            {"id": "C", "text": "A host-based file integrity monitor"},
            {"id": "D", "text": "A local antivirus agent on each device"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "NDR inspects network traffic and metadata (flows, protocol behavior) to detect malicious activity "
                       "such as lateral movement and beaconing - ideal for agentless/unmanaged devices where EDR cannot be installed.",
            "distractors": {
                "A": "EDR requires an agent on the endpoint, which these unmanaged devices cannot run.",
                "C": "A host-based FIM runs on a host and watches files; it cannot cover agentless network devices.",
                "D": "A local AV agent also must be installed on the device, which is not possible here.",
            },
            "exam_pattern": "Detect threats on agentless/unmanaged devices via network behavior = NDR; EDR needs an endpoint agent; XDR correlates across sources.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (NDR vs EDR/XDR)"],
    },
    {
        "id": "securityx-ops-r2-019", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 3, "type": "mcq",
        "stem": "A SOC is overwhelmed by a high volume of false-positive alerts, and analysts are suffering alert "
                "fatigue and missing real incidents. Which approach BEST improves signal quality WITHOUT simply "
                "blinding the team to genuine threats?",
        "options": [
            {"id": "A", "text": "Tune detection rules and thresholds, suppress/aggregate known-benign patterns, enrich and risk-rank alerts, and continuously measure that true positives are still caught after tuning"},
            {"id": "B", "text": "Disable the noisiest detection rules entirely and move on"},
            {"id": "C", "text": "Ignore all alerts below 'critical' permanently with no analysis"},
            {"id": "D", "text": "Turn off the SIEM to stop the noise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Thoughtful tuning - refining rules/thresholds, suppressing known-benign noise, enriching and "
                       "risk-ranking alerts, and verifying that true positives are still detected - reduces false positives while preserving detection of real threats.",
            "distractors": {
                "B": "Disabling noisy rules wholesale can blind the team to the real attacks those rules would have caught (false negatives).",
                "C": "Permanently ignoring sub-critical alerts without analysis risks missing early stages of serious incidents.",
                "D": "Turning off the SIEM removes detection entirely - the opposite of the goal.",
            },
            "exam_pattern": "Fix alert fatigue by tuning/enriching/risk-ranking AND verifying true positives remain caught - not by blindly disabling detections.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (alert tuning, false positives, alert fatigue)"],
    },
    {
        "id": "securityx-ops-r2-020", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 3, "type": "mcq",
        "stem": "A network security team debates deploying full packet capture (PCAP) versus relying on flow records "
                "(NetFlow/IPFIX). Which statement correctly characterizes the trade-off?",
        "options": [
            {"id": "A", "text": "Flow records contain full payloads, while packet capture contains only metadata"},
            {"id": "B", "text": "Both capture identical data; the choice is arbitrary"},
            {"id": "C", "text": "Full packet capture records complete content/payloads enabling deep forensic reconstruction but is storage-intensive and typically short-retention; flow records are lightweight metadata (who talked to whom, when, how much) that support long-term retention and trend analysis but lack payload detail"},
            {"id": "D", "text": "Flow records are more storage-intensive than full packet capture"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Full packet capture stores complete payloads for deep forensic analysis but consumes large storage "
                       "and is usually retained only briefly; flow data (NetFlow/IPFIX) is compact metadata enabling long retention and traffic-trend analysis, at the cost of no payload content.",
            "distractors": {
                "A": "This is reversed - packet capture holds payloads; flow records hold metadata only.",
                "B": "They capture very different data (full content vs metadata); the choice has real trade-offs.",
                "D": "Flow records are far less storage-intensive than full packet capture, not more.",
            },
            "exam_pattern": "PCAP = full content, deep analysis, storage-heavy/short retention; flow (NetFlow/IPFIX) = metadata, lightweight, long retention/trends.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (full packet capture vs flow data)"],
    },
    {
        "id": "securityx-ops-r2-021", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 2, "type": "mcq",
        "stem": "After an intrusion, responders find the attacker deleted local event logs on compromised hosts to "
                "cover their tracks. Which control would MOST effectively preserve an authoritative, tamper-resistant "
                "record for future incidents?",
        "options": [
            {"id": "A", "text": "Keep logs only on each local host with longer retention"},
            {"id": "B", "text": "Grant local administrators permission to edit logs for convenience"},
            {"id": "C", "text": "Reduce logging to cut storage costs"},
            {"id": "D", "text": "Forward logs in near-real time to a separate, access-controlled central store (e.g., SIEM) with write-once/immutable storage, so a host compromise cannot alter the authoritative copy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Centralized, real-time log forwarding to an access-controlled, write-once/immutable store means "
                       "that even if an attacker wipes local logs, the authoritative copy off the host remains intact for investigation.",
            "distractors": {
                "A": "Logs kept only locally are exactly what the attacker deleted; local retention does not protect them.",
                "B": "Letting admins edit logs undermines integrity and aids tampering.",
                "C": "Reducing logging removes the very evidence needed to detect and investigate incidents.",
            },
            "exam_pattern": "Protect log integrity against tampering = forward to a separate, immutable/write-once central store (SIEM), not local-only logs.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (log integrity, centralized immutable logging)"],
    },
    {
        "id": "securityx-ops-r2-022", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 2, "type": "mcq",
        "stem": "A SOC metrics report wants to express how long an attacker typically remained active in the "
                "environment BEFORE being discovered. Which metric captures this attacker 'time to detection'?",
        "options": [
            {"id": "A", "text": "Mean time to repair (MTTR)"},
            {"id": "B", "text": "Dwell time (closely related to mean time to detect, MTTD)"},
            {"id": "C", "text": "Mean time between failures (MTBF)"},
            {"id": "D", "text": "Recovery time objective (RTO)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Dwell time is how long an adversary is present and undetected before discovery; it is closely "
                       "tied to mean time to detect (MTTD). Shrinking dwell time/MTTD limits how much damage an intruder can do.",
            "distractors": {
                "A": "MTTR measures how long it takes to repair/recover after detection, not the undetected residence time.",
                "C": "MTBF is a reliability metric for time between failures, unrelated to attacker detection.",
                "D": "RTO is a recovery objective for restoring service after disruption, not a detection-time metric.",
            },
            "exam_pattern": "Attacker's undetected residence time = dwell time (~MTTD); MTTR = time to recover after detection.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (SOC metrics: dwell time, MTTD, MTTR)"],
    },
    {
        "id": "securityx-ops-r2-023", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_monitoring_detection", "difficulty": 3, "type": "mcq",
        "stem": "A SIEM is failing to detect attacks that its correlation rules are capable of catching, because key "
                "telemetry (endpoint process creation, PowerShell logging, and cloud audit logs) is never ingested. "
                "Which principle and action BEST address this gap?",
        "options": [
            {"id": "A", "text": "'You cannot detect what you do not collect' - expand log-source coverage by onboarding the missing telemetry (process/command-line logging, cloud audit logs) so detections have the data they need"},
            {"id": "B", "text": "Buy a second SIEM and send it the same incomplete data"},
            {"id": "C", "text": "Increase alert thresholds so fewer alerts fire"},
            {"id": "D", "text": "Shorten log retention to improve performance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Detection depends on visibility: without ingesting the right telemetry, even good rules cannot "
                       "fire. Closing the coverage gap by onboarding process/command-line and cloud audit logs gives the SIEM the data its detections require.",
            "distractors": {
                "B": "A second SIEM fed the same incomplete data inherits the same blind spots.",
                "C": "Raising thresholds reduces alerts further and worsens detection, not the coverage gap.",
                "D": "Shortening retention reduces available evidence and does nothing to add missing sources.",
            },
            "exam_pattern": "Detections fail without data -> expand log-source/telemetry coverage (you can't detect what you don't collect).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Monitoring/detection (log-source coverage, detection visibility)"],
    },

    # ===== scx_forensics ====================================================
    {
        "id": "securityx-ops-r2-024", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 3, "type": "mcq",
        "stem": "An investigator suspects injected code, hidden processes, and encryption keys that exist only in a "
                "running system's RAM, with no corresponding files on disk. Which forensic activity is MOST likely to "
                "recover this evidence?",
        "options": [
            {"id": "A", "text": "Imaging only the disk and ignoring memory"},
            {"id": "B", "text": "Running an on-demand antivirus scan on the live host"},
            {"id": "C", "text": "Capturing a volatile memory image from the live system and analyzing it with a memory-forensics framework (e.g., to enumerate processes, injected code, network connections, and keys)"},
            {"id": "D", "text": "Rebooting the machine to clear any malware first"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Evidence that lives only in RAM (injected code, hidden processes, keys, live connections) is "
                       "recovered by capturing a memory image from the running system and analyzing it with memory-forensics tooling - respecting the order of volatility.",
            "distractors": {
                "A": "Disk imaging alone misses memory-resident artifacts, which is where the evidence is.",
                "B": "Running AV alters system state and may remove artifacts without preserving them for analysis.",
                "D": "Rebooting destroys the volatile memory that holds the only copy of the evidence.",
            },
            "exam_pattern": "Memory-only artifacts (fileless/injected/keys) = capture and analyze a RAM image before shutdown (order of volatility).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (memory forensics, volatile evidence)"],
    },
    {
        "id": "securityx-ops-r2-025", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 3, "type": "mcq",
        "stem": "A legal team asks what must be true for digital evidence to be ADMISSIBLE and to withstand challenge "
                "in court. Which answer BEST summarizes the core requirements?",
        "options": [
            {"id": "A", "text": "The evidence only needs to be technically interesting to the investigators"},
            {"id": "B", "text": "The evidence must be relevant to the case, authentic and reliable (its integrity provable via hashing and an unbroken chain of custody), and lawfully/properly obtained under appropriate authority"},
            {"id": "C", "text": "The evidence must simply have been collected as quickly as possible"},
            {"id": "D", "text": "The evidence must be encrypted so no one can read it"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Admissible digital evidence must be relevant, authentic/reliable (integrity demonstrable through "
                       "cryptographic hashing and an unbroken, documented chain of custody), and obtained lawfully under proper authority - otherwise it may be excluded.",
            "distractors": {
                "A": "Being interesting is irrelevant to admissibility; legal and integrity standards govern it.",
                "C": "Speed alone does not make evidence admissible; integrity and lawful collection matter.",
                "D": "Encrypting evidence does not establish admissibility and could impede its use; integrity and provenance are what count.",
            },
            "exam_pattern": "Admissible evidence = relevant + authentic/reliable (hash + chain of custody) + lawfully obtained.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (evidence admissibility, integrity, legality)"],
    },
    {
        "id": "securityx-ops-r2-026", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 3, "type": "mcq",
        "stem": "An incident spans several auto-scaling cloud instances that may be terminated at any time. Which "
                "approach to cloud forensic acquisition is MOST sound given the environment's constraints?",
        "options": [
            {"id": "A", "text": "Physically seize the cloud provider's drives from their data center"},
            {"id": "B", "text": "Assume the instances will persist indefinitely and acquire them next quarter"},
            {"id": "C", "text": "Ignore cloud provider audit logs since you control the instances"},
            {"id": "D", "text": "Promptly capture evidence using provider snapshot/APIs (memory and volume snapshots) before instances are terminated, preserve the provider's audit/control-plane logs, and coordinate legal process and the shared-responsibility boundary with the provider"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Cloud instances are ephemeral and physically inaccessible, so acquire evidence quickly via "
                       "provider snapshot/APIs (memory and disk), preserve the provider's audit/control-plane logs, and work within legal process and the shared-responsibility model - the practical, defensible method.",
            "distractors": {
                "A": "Customers cannot seize a provider's physical drives in a multi-tenant data center; acquisition is done through provider mechanisms.",
                "B": "Auto-scaled instances can be terminated at any moment, destroying evidence - acquisition must be prompt.",
                "C": "Provider audit/control-plane logs are often crucial cloud evidence and must be preserved.",
            },
            "exam_pattern": "Cloud forensics -> snapshot/API acquisition promptly (ephemeral), preserve provider audit logs, coordinate legal + shared responsibility; no physical seizure.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (cloud forensics, ephemeral instances, provider logs)"],
    },
    {
        "id": "securityx-ops-r2-027", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 3, "type": "mcq",
        "stem": "An attacker used anti-forensic techniques, including altering file MAC timestamps (timestomping) to "
                "make a malicious file appear old and benign. Which investigative approach BEST counters this "
                "timestamp manipulation?",
        "options": [
            {"id": "A", "text": "Cross-correlate multiple independent evidence sources that are harder to forge in lockstep - e.g., NTFS $MFT $STANDARD_INFORMATION ($SI) vs $FILE_NAME ($FN) timestamps, $LogFile/$UsnJrnl journals, centralized logs, and other artifacts - rather than trusting a single displayed timestamp"},
            {"id": "B", "text": "Trust the file's displayed modified timestamp as authoritative"},
            {"id": "C", "text": "Conclude the file is benign because it looks old"},
            {"id": "D", "text": "Abandon the timeline since timestamps can be changed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Timestomping typically alters the easily changed timestamps, but corroborating artifacts "
                       "(filesystem journals, $MFT $STANDARD_INFORMATION vs $FILE_NAME discrepancies, centralized/external logs) are harder to alter consistently; cross-correlating independent sources exposes the manipulation and reconstructs the true timeline.",
            "distractors": {
                "B": "Trusting the displayed timestamp is exactly what the attacker's timestomping exploits.",
                "C": "Appearing old is the deception; corroboration is needed, not assumption of benignity.",
                "D": "Abandoning the timeline concedes to the attacker; multiple sources can still reveal the truth.",
            },
            "exam_pattern": "Counter anti-forensics/timestomping = corroborate across independent artifacts ($MFT/journal vs $SI, central logs); never trust one timestamp.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (anti-forensics, timeline corroboration)"],
    },
    {
        "id": "securityx-ops-r2-028", "exam": "securityx", "domain": "scx_operations",
        "subtopic": "scx_forensics", "difficulty": 2, "type": "mcq",
        "stem": "To forensically acquire a suspect hard drive so that deleted and hidden data is preserved and the "
                "evidence is defensible, which acquisition method is BEST?",
        "options": [
            {"id": "A", "text": "Copy only the visible files with the operating system's file explorer"},
            {"id": "B", "text": "Work directly on the original drive and modify it as needed during analysis"},
            {"id": "C", "text": "Create a bit-for-bit (physical) image using a write blocker, verify it with cryptographic hashes, and analyze the verified copy - capturing unallocated and slack space where deleted/hidden data resides"},
            {"id": "D", "text": "Compress the drive contents into an archive without hashing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A bit-for-bit physical image taken through a write blocker preserves the entire drive - including "
                       "unallocated and slack space containing deleted/hidden artifacts - and cryptographic hashes prove the image matches the original and was not altered; analysis is performed on the verified copy.",
            "distractors": {
                "A": "A logical copy of visible files misses deleted data, slack/unallocated space, and alters metadata.",
                "B": "Analyzing the original risks modifying evidence and breaks defensibility; a write-blocked image is required.",
                "D": "Compressing without hashing provides no integrity proof and a logical archive may omit deleted/hidden data.",
            },
            "exam_pattern": "Forensic disk acquisition = bit-for-bit image + write blocker + hash verification (captures slack/unallocated); never work on the original or copy only visible files.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 4 — Digital forensics (bit-for-bit imaging, write blocker, hashing, slack space)"],
    },
]
