"""CompTIA SecurityX (CAS-005) pool - Domain 1: Governance, Risk, and Compliance.

Original, objective-aligned practice items for the five GRC subtopics tracked in
CertLab (expert/CASP+-level reasoning - scenario-driven, trade-off focused):
  * scx_risk_management      - quantitative analysis (SLE/ARO/ALE), risk
                               appetite vs tolerance, inherent vs residual risk,
                               risk treatment (avoid/mitigate/transfer/accept),
                               the risk register.
  * scx_compliance_frameworks- ISO/IEC 27001, NIST CSF & SP 800-53, PCI DSS,
                               GDPR/CCPA, SOC 2 (Type I/II), FedRAMP.
  * scx_governance_policies  - policy/standard/procedure/guideline hierarchy,
                               separation of duties & compensating controls,
                               governance accountability/steering committee.
  * scx_third_party_risk     - SBOM, vendor/fourth-party assessment, SLAs and
                               agreement types, supply-chain risk, due diligence.
  * scx_data_governance      - classification, data sovereignty/residency,
                               data roles (controller/processor), retention and
                               privacy principles (minimization).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer key is NOT positionally
biased (keys are spread across A-D on purpose), every wrong option carries a
distractor note, and each item cites the public CAS-005 objective domain it
draws on so facts stay traceable. Expert depth (BEST-given-constraints,
architecture/risk trade-offs) - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== scx_risk_management ==============================================
    {
        "id": "securityx-grc-001", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A data center and its contents are valued at $2,000,000. A severe flood would "
                "destroy an estimated 25% of that value, and actuarial data indicates such a flood "
                "strikes roughly once every 20 years. Using quantitative risk analysis, what is the "
                "annualized loss expectancy (ALE)?",
        "options": [
            {"id": "A", "text": "$500,000"},
            {"id": "B", "text": "$400,000"},
            {"id": "C", "text": "$25,000"},
            {"id": "D", "text": "$100,000"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "SLE = asset value x exposure factor = $2,000,000 x 0.25 = $500,000. "
                       "ARO = 1 / 20 years = 0.05. ALE = SLE x ARO = $500,000 x 0.05 = $25,000.",
            "distractors": {
                "A": "$500,000 is the single loss expectancy (AV x EF) - the loss from one event, not yet annualized by the ARO.",
                "B": "$400,000 does not follow from SLE x ARO; it mis-multiplies the figures.",
                "D": "$100,000 would require an ARO of 0.2 (once every 5 years), which the scenario does not state.",
            },
            "exam_pattern": "Work it in order: SLE = AV x EF, then ALE = SLE x ARO. The SLE is the classic distractor for the ALE.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (quantitative analysis: SLE, ARO, ALE)"],
    },
    {
        "id": "securityx-grc-002", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise's board publishes a statement that the company is willing to accept a "
                "moderate amount of cybersecurity risk to pursue aggressive cloud-first growth. "
                "Separately, each system owner is given concrete, measurable thresholds - such as a "
                "maximum tolerable amount of unplanned downtime - that their system must never exceed. "
                "How are these two artifacts BEST characterized?",
        "options": [
            {"id": "A", "text": "The board statement is risk tolerance; the per-system thresholds are risk appetite."},
            {"id": "B", "text": "The board statement is risk appetite; the per-system thresholds are risk tolerance."},
            {"id": "C", "text": "Both are expressions of residual risk."},
            {"id": "D", "text": "Both are expressions of inherent risk."},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Risk appetite is the broad, strategic amount of risk leadership will pursue; "
                       "risk tolerance is the specific, measurable acceptable deviation for a given objective or system.",
            "distractors": {
                "A": "This reverses the terms - the broad strategic statement is appetite, and the concrete per-system thresholds are tolerance.",
                "C": "Residual risk is what remains after controls are applied; neither artifact describes leftover risk.",
                "D": "Inherent risk is risk before any controls; these artifacts express willingness to accept risk, not a pre-control measurement.",
            },
            "exam_pattern": "Appetite = broad/strategic 'how much risk overall'; tolerance = narrow/measurable 'acceptable variance for this objective.'",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (risk appetite vs risk tolerance)"],
    },
    {
        "id": "securityx-grc-003", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After deploying all cost-justified controls, a company still faces residual risk of a "
                "costly business-interruption event. Leadership chooses to purchase a cyber-insurance "
                "policy to cover the potential financial loss. Which risk-treatment strategy is this?",
        "options": [
            {"id": "A", "text": "Risk avoidance"},
            {"id": "B", "text": "Risk mitigation"},
            {"id": "C", "text": "Risk acceptance"},
            {"id": "D", "text": "Risk transference (sharing)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Buying insurance shifts the financial impact of the risk to a third party, which is risk transference (also called risk sharing).",
            "distractors": {
                "A": "Avoidance eliminates the risk by not performing the risky activity at all; the company continues operating.",
                "B": "Mitigation reduces likelihood or impact with controls; insurance does not lower the chance or severity of the event itself.",
                "C": "Acceptance means taking no further action and absorbing the loss; buying a policy is an action that offloads the loss.",
            },
            "exam_pattern": "Insurance/outsourcing the loss = transference; the four treatments are avoid, mitigate, transfer, accept.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (risk response/treatment strategies)"],
    },
    {
        "id": "securityx-grc-004", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_risk_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The level of risk that remains after security controls and "
                "mitigations have been applied is known as ______ risk.",
        "correct": ["residual", "residual risk"],
        "explanation": {
            "correct": "Residual risk is what is left after controls reduce the inherent risk; management must "
                       "formally accept it or apply further treatment, comparing it against the risk appetite.",
            "distractors": {},
            "exam_pattern": "Inherent risk (before controls) reduced by controls = residual risk; compare to appetite to decide acceptance.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Risk management (inherent vs residual risk)"],
    },

    # ===== scx_compliance_frameworks ========================================
    {
        "id": "securityx-grc-005", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "A multinational manufacturer wants a single, internationally recognized framework it "
                "can be formally certified against to establish, operate, and continually improve an "
                "information security management system (ISMS). Which framework BEST meets this?",
        "options": [
            {"id": "A", "text": "ISO/IEC 27001"},
            {"id": "B", "text": "NIST Cybersecurity Framework (CSF)"},
            {"id": "C", "text": "PCI DSS"},
            {"id": "D", "text": "SOC 2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ISO/IEC 27001 is the international standard for an ISMS and is certifiable by accredited "
                       "bodies, with continual improvement (Plan-Do-Check-Act) built in.",
            "distractors": {
                "B": "The NIST CSF is a voluntary, outcome-based framework for managing risk; organizations align to it but are not formally 'certified' against it as with ISO 27001.",
                "C": "PCI DSS is narrowly scoped to the protection of cardholder data, not a general enterprise ISMS.",
                "D": "SOC 2 produces an independent attestation report for a service organization, not an ISMS certification.",
            },
            "exam_pattern": "Certifiable international ISMS standard = ISO/IEC 27001; CSF = voluntary framework; SOC 2 = attestation; PCI DSS = cardholder data only.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (ISO/IEC 27001)"],
    },
    {
        "id": "securityx-grc-006", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise evaluating a SaaS provider needs independent assurance that the provider's "
                "security, availability, and confidentiality controls were not just suitably designed but "
                "operated effectively throughout a 12-month period. Which report BEST provides this?",
        "options": [
            {"id": "A", "text": "SOC 1 Type II"},
            {"id": "B", "text": "SOC 2 Type I"},
            {"id": "C", "text": "SOC 2 Type II"},
            {"id": "D", "text": "SOC 3"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A SOC 2 Type II report evaluates both the design AND the operating effectiveness of "
                       "controls (mapped to the Trust Services Criteria) over a period of time - exactly the assurance needed.",
            "distractors": {
                "A": "SOC 1 addresses controls relevant to financial reporting (ICFR), not the security/availability/confidentiality criteria in question.",
                "B": "A SOC 2 Type I attests only to the design of controls at a single point in time, not their operation over a period.",
                "D": "SOC 3 is a short, general-use public summary of a SOC 2 and lacks the detailed control testing the enterprise needs.",
            },
            "exam_pattern": "Type I = design at a point in time; Type II = design + operating effectiveness over a period. SOC 1 = financial; SOC 2 = TSC/security.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (SOC 2 Type I/II)"],
    },
    {
        "id": "securityx-grc-007", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "A cloud service provider wants to offer services to U.S. federal agencies and must obtain "
                "a standardized, government-wide authorization built on NIST SP 800-53 control baselines "
                "(Low/Moderate/High). Which program governs this authorization?",
        "options": [
            {"id": "A", "text": "HIPAA"},
            {"id": "B", "text": "FedRAMP"},
            {"id": "C", "text": "GDPR"},
            {"id": "D", "text": "PCI DSS"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "FedRAMP (Federal Risk and Authorization Management Program) standardizes security "
                       "assessment and authorization for cloud products used by U.S. federal agencies, using NIST SP 800-53 baselines.",
            "distractors": {
                "A": "HIPAA governs protected health information in the U.S. healthcare sector, not federal cloud authorization.",
                "C": "GDPR regulates personal data of EU data subjects, unrelated to U.S. federal cloud authorization.",
                "D": "PCI DSS protects payment-card data and is enforced by the card brands, not U.S. federal agencies.",
            },
            "exam_pattern": "U.S. federal cloud authorization on 800-53 baselines = FedRAMP.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (FedRAMP, NIST SP 800-53)"],
    },
    {
        "id": "securityx-grc-008", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_compliance_frameworks", "difficulty": 2, "type": "mcq",
        "stem": "Under the EU GDPR, after becoming aware of a personal-data breach that poses a risk to "
                "individuals, a data controller must notify the relevant supervisory authority without "
                "undue delay and, where feasible, within what maximum time?",
        "options": [
            {"id": "A", "text": "72 hours"},
            {"id": "B", "text": "24 hours"},
            {"id": "C", "text": "30 days"},
            {"id": "D", "text": "1 week"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GDPR Article 33 requires notification to the supervisory authority without undue delay "
                       "and, where feasible, not later than 72 hours after the controller becomes aware of the breach.",
            "distractors": {
                "B": "24 hours is stricter than GDPR requires; some sector rules use it, but GDPR's outer limit is 72 hours.",
                "C": "30 days is a common breach-notification window in some U.S. state laws, not GDPR's authority-notification limit.",
                "D": "One week does not correspond to GDPR's 72-hour requirement.",
            },
            "exam_pattern": "GDPR breach notice to the authority = 72 hours (where feasible); contrast with varied U.S. state timelines.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Compliance frameworks (GDPR breach notification)"],
    },

    # ===== scx_governance_policies ==========================================
    {
        "id": "securityx-grc-009", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 2, "type": "mcq",
        "stem": "A security team is organizing its documentation. They need to classify a mandatory, "
                "high-level management directive that states organizational intent - for example, 'all "
                "sensitive data must be encrypted' - without naming specific algorithms or steps. Which "
                "document type is this?",
        "options": [
            {"id": "A", "text": "A procedure"},
            {"id": "B", "text": "A guideline"},
            {"id": "C", "text": "A standard"},
            {"id": "D", "text": "A policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A policy is a high-level, mandatory statement of management intent and direction; it says what must be achieved, not the technical specifics of how.",
            "distractors": {
                "A": "A procedure is a detailed, step-by-step set of instructions to accomplish a task - far more granular than a high-level directive.",
                "B": "A guideline is a recommended, non-mandatory best practice, whereas the directive here is mandatory.",
                "C": "A standard is a mandatory but specific requirement (e.g., 'use AES-256'); the statement given is broad intent, not a specific rule.",
            },
            "exam_pattern": "Policy = mandatory intent (what/why); standard = mandatory specifics (which); procedure = steps (how); guideline = optional advice.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (policies, standards, procedures, guidelines)"],
    },
    {
        "id": "securityx-grc-010", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 3, "type": "mcq",
        "stem": "In a small finance team, one analyst can currently both create a new vendor record and "
                "approve payments to that vendor, creating fraud exposure. The team is too small to fully "
                "split these duties. Which combination BEST addresses the governance concern?",
        "options": [
            {"id": "A", "text": "Apply least privilege and require MFA for the analyst's account."},
            {"id": "B", "text": "Enforce separation of duties where possible and add compensating controls such as dual control for approvals, mandatory vacations, and independent transaction review."},
            {"id": "C", "text": "Implement job rotation and single sign-on across the finance apps."},
            {"id": "D", "text": "Rely on defense in depth by adding a network firewall rule."},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The core principle is separation of duties; when staffing prevents a full split, "
                       "compensating controls - dual control, mandatory vacations, and independent review/audit - reduce the fraud risk the conflict creates.",
            "distractors": {
                "A": "MFA and least privilege strengthen authentication and access scope but do not resolve one person performing two incompatible duties.",
                "C": "Job rotation and SSO do not stop one person from performing both incompatible actions during their tenure; SSO can even broaden access.",
                "D": "A network firewall rule addresses perimeter traffic, not the business-process conflict of duties.",
            },
            "exam_pattern": "Incompatible duties in one person -> separation of duties; if unachievable, layer compensating controls (dual control, mandatory vacation, independent review).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (separation of duties, compensating controls)"],
    },
    {
        "id": "securityx-grc-011", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_governance_policies", "difficulty": 2, "type": "mcq",
        "stem": "During an audit, the question arises of who is ultimately accountable for accepting "
                "enterprise information-security risk and owning the governance program. Which answer "
                "reflects sound security governance?",
        "options": [
            {"id": "A", "text": "Senior leadership and the board are ultimately accountable, typically acting through a security steering committee, with the CISO advising and executing."},
            {"id": "B", "text": "The SOC analysts, because they see the alerts first."},
            {"id": "C", "text": "Individual system administrators, because they configure the systems."},
            {"id": "D", "text": "The external auditor, because they assess the controls."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance and ultimate risk-acceptance accountability reside with senior leadership/the "
                       "board; they often work through a steering committee, and the CISO advises and carries out the program.",
            "distractors": {
                "B": "SOC analysts operate detection and response; they do not own enterprise risk acceptance or governance.",
                "C": "System administrators implement configurations but are not accountable for enterprise-level risk decisions.",
                "D": "External auditors provide independent assessment; owning or accepting the risk would impair their independence.",
            },
            "exam_pattern": "Accountability for risk acceptance and governance rolls up to senior management/the board; the CISO advises, not unilaterally owns the risk.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Governance (roles, accountability, steering committee)"],
    },

    # ===== scx_third_party_risk =============================================
    {
        "id": "securityx-grc-012", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Following a widespread open-source library vulnerability, a CISO wants the fastest reliable "
                "way to determine which of the company's purchased and in-house applications include the "
                "affected component and version. Which artifact BEST enables this?",
        "options": [
            {"id": "A", "text": "A service-level agreement (SLA)"},
            {"id": "B", "text": "A penetration-test report"},
            {"id": "C", "text": "A software bill of materials (SBOM)"},
            {"id": "D", "text": "A memorandum of understanding (MOU)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An SBOM is a machine-readable inventory of all components and dependencies (names and "
                       "versions) in a software product, enabling rapid identification of affected applications (e.g., via SPDX or CycloneDX formats).",
            "distractors": {
                "A": "An SLA defines service performance commitments, not a component inventory.",
                "B": "A penetration-test report describes findings from point-in-time testing, not a complete dependency inventory.",
                "D": "An MOU records a non-binding understanding between parties, unrelated to component inventories.",
            },
            "exam_pattern": "Need to find which products contain a vulnerable component fast = SBOM (SPDX/CycloneDX).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party/supply-chain risk (SBOM)"],
    },
    {
        "id": "securityx-grc-013", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 3, "type": "mcq",
        "stem": "A critical SaaS vendor subcontracts part of its data processing to another company (a "
                "'fourth party' from the enterprise's view). With a limited audit budget, the enterprise "
                "needs ongoing assurance covering both the vendor and its subprocessor. Which approach "
                "BEST balances assurance against cost?",
        "options": [
            {"id": "A", "text": "Accept the risk, since the subprocessor is outside the direct contract."},
            {"id": "B", "text": "Rely only on the vendor's completed self-assessment questionnaire."},
            {"id": "C", "text": "Conduct a full on-site audit of the vendor and every subprocessor each quarter."},
            {"id": "D", "text": "Require the vendor's SOC 2 Type II report that covers subservice organizations, plus a contractual right-to-audit and continuous monitoring (e.g., security ratings)."},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A SOC 2 Type II that addresses subservice organizations (inclusive or carve-out method), "
                       "combined with right-to-audit clauses and continuous monitoring, gives defensible ongoing assurance over the vendor and its subprocessor without the cost of constant on-site audits.",
            "distractors": {
                "A": "Ignoring fourth-party risk leaves a material supply-chain exposure unmanaged.",
                "B": "A self-assessment questionnaire is unverified self-attestation and is weak as sole assurance for a critical vendor.",
                "C": "Quarterly on-site audits of every party exceed the limited budget and do not scale.",
            },
            "exam_pattern": "Critical vendor + fourth-party risk + limited budget -> independent attestation (SOC 2 Type II covering subservice orgs) + right-to-audit + continuous monitoring.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (vendor/fourth-party assessment, continuous monitoring)"],
    },
    {
        "id": "securityx-grc-014", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Legal and procurement are mapping vendor agreement types. Which agreement specifically "
                "defines measurable service commitments - such as 99.95% monthly availability - along with "
                "the remedies or penalties if those targets are missed?",
        "options": [
            {"id": "A", "text": "Non-disclosure agreement (NDA)"},
            {"id": "B", "text": "Service-level agreement (SLA)"},
            {"id": "C", "text": "Memorandum of understanding (MOU)"},
            {"id": "D", "text": "Interconnection security agreement (ISA)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An SLA defines specific, measurable service levels (e.g., uptime, response times) and the remedies/credits owed when they are not met.",
            "distractors": {
                "A": "An NDA protects confidential information; it does not define service performance levels.",
                "C": "An MOU expresses a broad, often non-binding understanding of intent, without enforceable performance metrics.",
                "D": "An ISA governs the technical security requirements for connecting two systems/networks, not service performance targets.",
            },
            "exam_pattern": "Measurable performance + penalties = SLA; NDA = confidentiality; MOU = intent; ISA = secure interconnection.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (SLA and agreement types)"],
    },
    {
        "id": "securityx-grc-015", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_third_party_risk", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Before signing a contract, the up-front investigation of a prospective "
                "vendor's financial stability, security posture, and reputation is called due ______.",
        "correct": ["diligence", "due diligence"],
        "explanation": {
            "correct": "Due diligence is the investigative, pre-contract assessment of a vendor; due care is the ongoing, reasonable protection applied afterward.",
            "distractors": {},
            "exam_pattern": "Due diligence = investigate before (the homework); due care = act responsibly during/after (the ongoing effort).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Third-party risk (due diligence vs due care)"],
    },

    # ===== scx_data_governance ==============================================
    {
        "id": "securityx-grc-016", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 3, "type": "mcq",
        "stem": "A global firm stores EU residents' personal data in a U.S. cloud region. Regulators insist "
                "the data remain subject to EU legal jurisdiction and, ideally, physically within the EU. "
                "Which concept primarily drives the requirement to keep data within a specific country's or "
                "region's legal boundaries?",
        "options": [
            {"id": "A", "text": "Data sovereignty (with data residency/localization)"},
            {"id": "B", "text": "Data remanence"},
            {"id": "C", "text": "Data masking"},
            {"id": "D", "text": "Data deduplication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data sovereignty holds that data is subject to the laws of the jurisdiction in which it is "
                       "located; related concepts of data residency/localization drive storing it within specific borders.",
            "distractors": {
                "B": "Data remanence is residual data left on media after deletion - a sanitization concern, not jurisdiction.",
                "C": "Data masking obfuscates values to protect sensitive fields; it does not address legal jurisdiction over location.",
                "D": "Data deduplication is a storage-efficiency technique, unrelated to legal boundaries.",
            },
            "exam_pattern": "Which country's laws apply / must stay in-region = data sovereignty & residency; don't confuse with remanence or masking.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (data sovereignty, residency)"],
    },
    {
        "id": "securityx-grc-017", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 3, "type": "mcq",
        "stem": "An organization is assigning privacy roles for a new processing activity. Under GDPR "
                "terminology, the entity that determines the purposes and means of processing personal data, "
                "and the entity that processes the data on that entity's behalf, are respectively the:",
        "options": [
            {"id": "A", "text": "data custodian; data owner"},
            {"id": "B", "text": "data steward; data subject"},
            {"id": "C", "text": "data controller; data processor"},
            {"id": "D", "text": "data processor; data controller"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Under GDPR, the controller determines the purposes and means of processing; the processor processes personal data on the controller's behalf.",
            "distractors": {
                "A": "Owner/custodian are classic data-governance roles (accountable vs hands-on protection), not GDPR's controller/processor pairing.",
                "B": "The data subject is the individual the data is about, and a steward manages data quality/use - neither fits 'determines purposes.'",
                "D": "This reverses the two - the entity that determines purposes is the controller, not the processor.",
            },
            "exam_pattern": "GDPR: controller decides why/how; processor acts on the controller's instructions. Subject = the person; owner/custodian = governance roles.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (data roles; GDPR controller vs processor)"],
    },
    {
        "id": "securityx-grc-018", "exam": "securityx", "domain": "scx_grc",
        "subtopic": "scx_data_governance", "difficulty": 2, "type": "multi",
        "stem": "A privacy program deletes customer records once they are no longer needed for the business "
                "purpose for which they were collected. Which TWO privacy principles does this practice MOST "
                "directly support? (Choose two.)",
        "options": [
            {"id": "A", "text": "Data minimization"},
            {"id": "B", "text": "Storage (retention) limitation"},
            {"id": "C", "text": "Data maximization for future analytics"},
            {"id": "D", "text": "Indefinite retention to preserve optionality"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Collecting and keeping only what is needed reflects data minimization, and deleting data "
                       "once its purpose ends reflects storage (retention) limitation - both core privacy-by-design principles that also shrink breach impact.",
            "distractors": {
                "C": "Retaining data to maximize future analytics conflicts with minimization and increases risk.",
                "D": "Indefinite retention contradicts storage limitation and enlarges the attack surface and liability.",
            },
            "exam_pattern": "Keep only what's needed, only as long as needed = data minimization + storage limitation.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 1 — Data governance (privacy principles, retention)"],
    },
]
