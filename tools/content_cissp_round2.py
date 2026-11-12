"""(ISC)² CISSP pool - Round 2 (deepening expansion, all eight domains).

Round 1 (content_cissp_*.py, 130 items) established baseline coverage of every
CISSP CBK domain and subtopic. This round-2 pool adds ~70 ORIGINAL, NON-DUPLICATE
items that go deeper: harder scenarios and new angles that round 1 did not cover,
weighted toward the managerial, risk-based "think like a risk manager" judgment
(BEST / FIRST / MOST) the exam rewards.

New angles vs round 1 (no concept+scenario is repeated):
  * Domain 1 (srm):       compensating controls, senior-management accountability,
                          HIPAA, GDPR 72-hour breach notice, safeguard cost-benefit
                          (ALE), risk mitigation vs transfer/avoid, ISA/MOU/SLA,
                          guidelines, MTD = RTO + WRT, reciprocal sites, job rotation.
  * Domain 2 (asset):     PII definition, declassification review, NIST SP 800-88
                          Clear/Purge/Destroy, data masking, system owner,
                          anonymization vs pseudonymization (GDPR), crypto-shredding.
  * Domain 3 (arch_eng):  Common Criteria (EAL/TOE), MAC security modes, ECB
                          weakness, OCSP vs CRL, SHA-1/MD5 retirement, protection
                          rings, VM escape, covert timing channels, CPTED.
  * Domain 4 (comm_net):  NAC/802.1X, SDN control/data plane, WAF, bastion hosts,
                          WPA3/SAE, VPN hardening, VLAN hopping, DDoS amplification,
                          MAC flooding.
  * Domain 5 (iam):       PAM, automated deprovisioning (SCIM), FIDO2/passkeys,
                          TOTP vs HOTP, TACACS+ vs RADIUS, ACL vs capability list,
                          need-to-know, Kerberos TGT/TGS flow, OIDC vs OAuth tokens.
  * Domain 6 (assess):    red/blue/purple teams, credentialed scanning, SCA,
                          synthetic transactions, clipping levels, SOC 1 (ICFR),
                          risk acceptance of findings, KPI vs KRI.
  * Domain 7 (sec_ops):   evidence admissibility, legal hold/eDiscovery, SOAR,
                          threat hunting, event/incident/breach, eradication,
                          RAID 6, incremental restore, patch management.
  * Domain 8 (software):  dev/test/prod separation, software escrow, broken access
                          control (OWASP A01), secrets management, SSRF, insecure
                          deserialization, SBOM, container image scanning.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased
(round-2 keys are spread evenly across A/B/C/D before shuffling), every wrong
option carries a distractor note, and each item cites the CISSP CBK domain plus
the authoritative source where a fact is version-, number-, standard-, or
law-specific. Items are original, scenario-driven, and never reproduce real or
memorized exam questions. Ids reuse the round-1 prefixes with an "r2" segment.
"""

QUESTIONS = [
    # ===================================================================
    # Domain 1 - Security and Risk Management (cissp_srm)
    # ===================================================================
    # ----- cissp_cia_governance --------------------------------------------
    {
        "id": "cissp-srm-r2-001", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_cia_governance", "difficulty": 2, "type": "mcq",
        "stem": "A regulation requires multifactor authentication on a legacy application, but the vendor "
                "cannot add MFA for six months. In the interim the company places the application behind a "
                "hardened jump host with restricted access and enhanced logging to achieve comparable "
                "protection. The jump-host arrangement BEST represents which kind of control?",
        "options": [
            {"id": "A", "text": "A compensating control"},
            {"id": "B", "text": "A deterrent control"},
            {"id": "C", "text": "A corrective control"},
            {"id": "D", "text": "A recovery control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A compensating control is an alternative safeguard put in place when the primary "
                       "required control is not currently feasible, providing a comparable level of protection "
                       "so the requirement is still effectively met.",
            "distractors": {
                "B": "A deterrent control discourages a would-be attacker (e.g., warning banners); the jump "
                     "host actively limits and monitors access rather than merely discouraging it.",
                "C": "A corrective control restores systems after an incident (e.g., restoring from backup); "
                     "the jump host is in place beforehand as an alternative safeguard.",
                "D": "A recovery control restores capability after damage; this control substitutes for a "
                     "missing preventive control, it does not recover from an incident.",
            },
            "exam_pattern": "An alternative safeguard used when the primary/required control isn't feasible = "
                            "compensating control (categorize by function: preventive/detective/corrective/"
                            "deterrent/compensating, and by type: administrative/technical/physical).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Security control categories and types"],
    },
    {
        "id": "cissp-srm-r2-002", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_cia_governance", "difficulty": 2, "type": "mcq",
        "stem": "A serious residual risk must be formally accepted before a new system goes live. In a "
                "well-governed program, who holds ULTIMATE accountability for that acceptance and for the "
                "organization's overall security posture, even though execution is delegated to a CISO and "
                "IT staff?",
        "options": [
            {"id": "A", "text": "The SOC analysts who monitor the environment"},
            {"id": "B", "text": "The data custodian who maintains the controls"},
            {"id": "C", "text": "Senior (executive) management, and ultimately the board of directors"},
            {"id": "D", "text": "The external penetration-testing firm"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Senior management (ultimately the board) is accountable for the security program and "
                       "must formally accept residual risk; accountability cannot be delegated even though the "
                       "work of implementing and operating controls can be.",
            "distractors": {
                "A": "SOC analysts carry out monitoring duties; they do not own enterprise risk-acceptance decisions.",
                "B": "The custodian implements and maintains controls on data; it is not the enterprise "
                     "risk-acceptance authority.",
                "D": "An external tester provides independent findings; it has no authority or accountability "
                     "to accept the organization's risk.",
            },
            "exam_pattern": "Accountability for security and formal risk acceptance rests with senior "
                            "management/board ('tone at the top') and cannot be delegated; execution can be.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Security governance and accountability"],
    },

    # ----- cissp_compliance_legal ------------------------------------------
    {
        "id": "cissp-srm-r2-003", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_compliance_legal", "difficulty": 2, "type": "mcq",
        "stem": "A U.S. hospital network is selecting the regulatory requirement that most directly governs "
                "the administrative, physical, and technical safeguards it must apply to electronic protected "
                "health information (ePHI). Which law's Security Rule applies?",
        "options": [
            {"id": "A", "text": "The EU General Data Protection Regulation (GDPR)"},
            {"id": "B", "text": "The Health Insurance Portability and Accountability Act (HIPAA)"},
            {"id": "C", "text": "The Sarbanes-Oxley Act (SOX)"},
            {"id": "D", "text": "The Payment Card Industry Data Security Standard (PCI DSS)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "HIPAA governs protected health information in the U.S.; its Security Rule mandates "
                       "administrative, physical, and technical safeguards for electronic PHI held by covered "
                       "entities and their business associates.",
            "distractors": {
                "A": "GDPR protects the personal data of individuals in the EU; it may apply to EU patients but "
                     "is not the U.S. health-specific safeguard statute being asked about.",
                "C": "SOX governs financial reporting and internal controls for public companies, not health information.",
                "D": "PCI DSS is a contractual payment-card security standard, not a health-information law.",
            },
            "exam_pattern": "U.S. health data (PHI/ePHI) safeguards = HIPAA Security Rule; EU personal data = "
                            "GDPR; payment cards = PCI DSS (contractual); financial reporting = SOX.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Legal and regulatory compliance",
                       "HIPAA Security Rule (45 CFR Part 164, Subpart C)"],
    },
    {
        "id": "cissp-srm-r2-004", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_compliance_legal", "difficulty": 3, "type": "mcq",
        "stem": "A data controller subject to the GDPR confirms a personal-data breach that is likely to "
                "pose a risk to affected individuals. What is the controller's PRIMARY obligation regarding "
                "notifying the supervisory authority?",
        "options": [
            {"id": "A", "text": "Notify the authority within 30 calendar days of the breach"},
            {"id": "B", "text": "No notification is ever required if the data was encrypted at rest"},
            {"id": "C", "text": "Notify only the affected individuals, never the supervisory authority"},
            {"id": "D", "text": "Notify the supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware of it"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "GDPR Article 33 requires the controller to notify the supervisory authority without "
                       "undue delay and, where feasible, not later than 72 hours after becoming aware of a "
                       "breach that poses a risk; a delay beyond 72 hours must be justified with reasons.",
            "distractors": {
                "A": "Thirty days is not the GDPR deadline; the obligation is tied to a 72-hour target from awareness.",
                "B": "Strong encryption may reduce the duty to notify affected individuals, but the authority "
                     "notification and the documentation duty still apply based on the risk assessment.",
                "C": "The authority must be notified for risky breaches; high-risk breaches additionally require "
                     "notifying the data subjects (Art. 34) - it is not an either/or that excludes the authority.",
            },
            "exam_pattern": "GDPR breach: notify the supervisory authority without undue delay, within 72 hours "
                            "of awareness (Art. 33); also notify high-risk-affected individuals (Art. 34).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Privacy and breach notification",
                       "GDPR Articles 33-34 (breach notification)"],
    },

    # ----- cissp_risk_management -------------------------------------------
    {
        "id": "cissp-srm-r2-005", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "Before a control is added, an asset's annualized loss expectancy (ALE) is $90,000. A "
                "proposed safeguard is expected to reduce the ALE to $20,000 and costs $40,000 per year to "
                "operate. What is the net annual value (benefit) of the safeguard, and is it justified?",
        "options": [
            {"id": "A", "text": "$70,000 net benefit"},
            {"id": "B", "text": "$30,000 net benefit, so it is cost-justified"},
            {"id": "C", "text": "$50,000 net benefit"},
            {"id": "D", "text": "-$20,000 (a net loss), so it is not justified"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Value of a safeguard = (ALE before - ALE after) - annual cost of the safeguard = "
                       "($90,000 - $20,000) - $40,000 = $70,000 - $40,000 = $30,000 net benefit, so the control "
                       "is cost-justified.",
            "distractors": {
                "A": "$70,000 is the gross risk reduction (ALE before - ALE after) before subtracting the "
                     "$40,000 annual operating cost.",
                "C": "$50,000 subtracts the wrong figure (e.g., $90,000 - $40,000) and ignores the post-control ALE.",
                "D": "The safeguard is actually net positive; -$20,000 misapplies the numbers.",
            },
            "exam_pattern": "Safeguard value = (ALE_before - ALE_after) - annual safeguard cost; a positive "
                            "result means the control is cost-justified.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Cost-benefit analysis of safeguards"],
    },
    {
        "id": "cissp-srm-r2-006", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_risk_management", "difficulty": 2, "type": "multi",
        "stem": "An organization is choosing how to respond to several identified risks. Which TWO of the "
                "following actions are examples of risk MITIGATION (reduction)? (Choose two.)",
        "options": [
            {"id": "A", "text": "Deploying intrusion prevention and MFA to lower the chance of compromise"},
            {"id": "B", "text": "Purchasing a cyber-insurance policy to cover financial losses"},
            {"id": "C", "text": "Applying hardening baselines to reduce the attack surface"},
            {"id": "D", "text": "Declining to launch a risky new product line at all"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Mitigation reduces the likelihood or impact of a risk by applying controls; deploying "
                       "IPS/MFA and applying hardening baselines both lower likelihood and/or impact.",
            "distractors": {
                "B": "Buying insurance is risk transfer (sharing the financial impact with a third party), not mitigation.",
                "D": "Declining the risky activity entirely is risk avoidance, not mitigation.",
            },
            "exam_pattern": "Mitigation = reduce likelihood/impact with controls; transfer = insurance/outsourcing; "
                            "avoidance = don't do the activity; acceptance = absorb the residual risk.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Risk treatment options"],
    },

    # ----- cissp_security_policies -----------------------------------------
    {
        "id": "cissp-srm-r2-007", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_security_policies", "difficulty": 2, "type": "mcq",
        "stem": "Two organizations are connecting their networks to exchange data and need a document that "
                "specifies the technical and security requirements for establishing, operating, and "
                "maintaining that interconnection. Which agreement BEST fits?",
        "options": [
            {"id": "A", "text": "A service level agreement (SLA)"},
            {"id": "B", "text": "A memorandum of understanding (MOU)"},
            {"id": "C", "text": "An interconnection security agreement (ISA)"},
            {"id": "D", "text": "A non-disclosure agreement (NDA)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An ISA specifically documents the technical and security requirements for establishing, "
                       "operating, and maintaining a connection between two organizations' systems.",
            "distractors": {
                "A": "An SLA defines service levels, metrics, and penalties for a delivered service, not the "
                     "security of a system interconnection.",
                "B": "An MOU is a broad, often non-binding statement of intent to cooperate; it lacks the "
                     "technical interconnection-security detail.",
                "D": "An NDA protects confidential information shared between parties; it does not specify "
                     "interconnection security controls.",
            },
            "exam_pattern": "ISA = technical/security terms of a system interconnection; SLA = service levels; "
                            "MOU = informal intent; NDA = confidentiality.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Agreements (SLA/MOU/ISA)"],
    },
    {
        "id": "cissp-srm-r2-008", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_security_policies", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Within the policy framework, a document that provides recommended but "
                "optional (non-mandatory) best-practice advice to help personnel meet standards is called a "
                "________.",
        "correct": ["guideline", "guidelines"],
        "explanation": {
            "correct": "A guideline offers discretionary, recommended guidance; unlike policies, standards, and "
                       "baselines (which are mandatory), a guideline is not compulsory.",
            "exam_pattern": "Policy (intent) and standard (mandatory specifics), baseline (mandatory minimum), "
                            "and procedure (mandatory steps) are required; a guideline is optional advice.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Policy document hierarchy"],
    },

    # ----- cissp_bcp_dr ----------------------------------------------------
    {
        "id": "cissp-srm-r2-009", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_bcp_dr", "difficulty": 3, "type": "mcq",
        "stem": "During BCP planning, a critical function is assigned a maximum tolerable downtime (MTD) of "
                "8 hours. Which statement CORRECTLY constrains the recovery time objective (RTO) and work "
                "recovery time (WRT) for that function?",
        "options": [
            {"id": "A", "text": "The RTO plus the WRT must not exceed the MTD (RTO + WRT <= 8 hours)"},
            {"id": "B", "text": "The RTO alone may exceed the MTD as long as the WRT is short"},
            {"id": "C", "text": "The RPO must equal the MTD"},
            {"id": "D", "text": "The MTD is the sum of the RPO and the ARO"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MTD is the total outage a function can tolerate and equals RTO (time to restore "
                       "systems) plus WRT (time to validate and resume normal work); therefore RTO + WRT must "
                       "stay within the MTD.",
            "distractors": {
                "B": "If the RTO alone exceeded the MTD, the function would already be down longer than "
                     "tolerable; RTO must leave room for WRT within the MTD.",
                "C": "RPO addresses acceptable DATA loss (a point in time), a separate dimension from the "
                     "downtime measured by MTD.",
                "D": "The MTD is not RPO + ARO; ARO is an annualized rate of occurrence from risk analysis and "
                     "is unrelated to this sum.",
            },
            "exam_pattern": "MTD = RTO + WRT; keep RTO + WRT within the MTD. RPO (acceptable data loss) is a "
                            "separate axis from downtime.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Recovery metrics (MTD/RTO/WRT/RPO)"],
    },
    {
        "id": "cissp-srm-r2-010", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_bcp_dr", "difficulty": 2, "type": "mcq",
        "stem": "A small company is considering a reciprocal (mutual-aid) agreement with a partner firm as "
                "its disaster-recovery strategy. Which is the MOST significant drawback of relying on this "
                "arrangement?",
        "options": [
            {"id": "A", "text": "It is the most expensive recovery option available"},
            {"id": "B", "text": "It guarantees capacity because it is contractually enforced like a hot site"},
            {"id": "C", "text": "It provides near-instant failover with real-time data replication"},
            {"id": "D", "text": "During a regional disaster the partner may lack spare capacity, and hosting each other's data raises confidentiality concerns"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A reciprocal agreement is cheap but unreliable: in a shared or regional disaster the "
                       "partner may have no spare capacity, such agreements are hard to enforce, and housing "
                       "each other's systems and data raises confidentiality concerns.",
            "distractors": {
                "A": "Reciprocal agreements are typically the CHEAPEST option; a hot/mirrored site is the most expensive.",
                "B": "They are notoriously difficult to enforce and do not guarantee capacity the way a "
                     "contracted hot site does.",
                "C": "They offer no inherent real-time replication or instant failover; that describes a hot or "
                     "mirrored site.",
            },
            "exam_pattern": "Reciprocal/mutual-aid = low cost but unreliable capacity, weak enforceability, and "
                            "confidentiality concerns.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Recovery site strategies"],
    },

    # ----- cissp_ethics_personnel ------------------------------------------
    {
        "id": "cissp-srm-r2-011", "exam": "cissp", "domain": "cissp_srm",
        "subtopic": "cissp_ethics_personnel", "difficulty": 2, "type": "mcq",
        "stem": "In addition to deterring fraud, a company rotates employees through different roles every "
                "few months. Besides making ongoing fraud harder to conceal, which ADDITIONAL benefit does "
                "job rotation PRIMARILY provide?",
        "options": [
            {"id": "A", "text": "It enforces clearance-based access labels on data"},
            {"id": "B", "text": "It cross-trains staff and reduces dependence on any single employee"},
            {"id": "C", "text": "It encrypts data at rest on the affected systems"},
            {"id": "D", "text": "It eliminates the need for separation of duties"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Job rotation both detects fraud (another person performs the role and may notice "
                       "irregularities) and cross-trains personnel, reducing single-person dependency and "
                       "improving resilience and continuity.",
            "distractors": {
                "A": "Clearance-based labeling is mandatory access control, unrelated to rotating job assignments.",
                "C": "Job rotation is an administrative personnel control; it does not perform encryption.",
                "D": "Rotation complements, and does not replace, separation of duties; they are used together.",
            },
            "exam_pattern": "Job rotation = fraud detection + cross-training/reduced single-person dependency "
                            "(complements separation of duties and mandatory vacation).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 1 - Personnel security controls"],
    },

    # ===================================================================
    # Domain 2 - Asset Security (cissp_asset)
    # ===================================================================
    # ----- cissp_data_classification ---------------------------------------
    {
        "id": "cissp-asset-r2-001", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "A company is scoping which fields in a customer database require privacy protections. "
                "Which definition should the team use to decide whether a field holds personally "
                "identifiable information (PII)?",
        "options": [
            {"id": "A", "text": "Any data stored in the production database"},
            {"id": "B", "text": "Only a person's full legal name"},
            {"id": "C", "text": "Any data field that is encrypted"},
            {"id": "D", "text": "Information that can identify a specific individual, alone or combined with other data"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "PII is any information that can distinguish or trace an individual's identity, either "
                       "by itself (e.g., SSN) or when linked with other data (e.g., name + date of birth + ZIP); "
                       "scoping should follow this identifiability definition.",
            "distractors": {
                "A": "Where data is stored does not determine whether it is PII; non-personal data also lives "
                     "in production.",
                "B": "A name is one identifier, but PII is broader - it includes linkable combinations and "
                     "identifiers such as SSN, biometric, and account numbers.",
                "C": "Encryption is a control applied to data; it does not define whether the underlying data is PII.",
            },
            "exam_pattern": "PII = data that identifies an individual alone or in combination; scope by "
                            "identifiability, not by storage location or format.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - PII and data classification"],
    },
    {
        "id": "cissp-asset-r2-002", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 3, "type": "mcq",
        "stem": "An agency labeled a report Top Secret ten years ago, but the sensitivity of its contents "
                "has since diminished. What process should determine whether the report's classification can "
                "be lowered, and who authorizes it?",
        "options": [
            {"id": "A", "text": "Any user who can read the report may relabel it at their discretion"},
            {"id": "B", "text": "The data custodian automatically lowers labels on a fixed schedule"},
            {"id": "C", "text": "A formal declassification review, authorized by the data owner (or designated classification authority)"},
            {"id": "D", "text": "Classification can never be changed once it is assigned"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Classification is reviewed across the data lifecycle; lowering a label "
                       "(declassification) requires a formal review and the authorization of the data owner or "
                       "a designated classification authority, not an automatic or arbitrary change.",
            "distractors": {
                "A": "Ordinary users cannot change classification labels; in MAC environments this is "
                     "explicitly prohibited.",
                "B": "The custodian implements controls but does not hold authority to reclassify or declassify "
                     "data on its own.",
                "D": "Classifications can change (reclassification or declassification) through a controlled, "
                     "authorized process as sensitivity changes over time.",
            },
            "exam_pattern": "Declassification/reclassification is a controlled, owner-authorized review over the "
                            "data lifecycle - never automatic or user-driven.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Classification lifecycle and declassification"],
    },

    # ----- cissp_data_lifecycle --------------------------------------------
    {
        "id": "cissp-asset-r2-003", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 3, "type": "multi",
        "stem": "Per NIST SP 800-88 (Guidelines for Media Sanitization), which TWO sanitization levels "
                "still leave the media FUNCTIONAL so it can be reused afterward? (Choose two.)",
        "options": [
            {"id": "A", "text": "Clear (logical techniques such as overwriting user-addressable space)"},
            {"id": "B", "text": "Purge (e.g., cryptographic erase, block erase, or degaussing of magnetic media)"},
            {"id": "C", "text": "Destroy (shredding or pulverizing the media)"},
            {"id": "D", "text": "Incineration of the media"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Clear and Purge sanitize media while leaving it usable: Clear uses logical overwriting "
                       "(resists simple recovery), and Purge uses stronger methods (cryptographic/secure erase, "
                       "degauss) that defeat laboratory recovery - both permit reuse.",
            "distractors": {
                "C": "Destroy physically ruins the media (shred/pulverize), so it cannot be reused.",
                "D": "Incineration is a form of destruction; the media is consumed and cannot be reused.",
            },
            "exam_pattern": "NIST 800-88 - Clear and Purge allow reuse (Purge defeats lab recovery); Destroy "
                            "(shred/incinerate/pulverize) does not. Match the level to data sensitivity and reuse plans.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Media sanitization",
                       "NIST SP 800-88 Rev. 1 (Guidelines for Media Sanitization)"],
    },
    {
        "id": "cissp-asset-r2-004", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "Developers need realistic data to test an application but must not expose real customer "
                "records in the lower (non-production) environment. Which technique BEST meets this need?",
        "options": [
            {"id": "A", "text": "Apply data masking (obfuscation) so the test data is realistic but not the real sensitive values"},
            {"id": "B", "text": "Copy the live production database unchanged into the test environment"},
            {"id": "C", "text": "Grant the developers production administrator rights"},
            {"id": "D", "text": "Disable logging in the test environment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data masking replaces sensitive values with realistic but fictional or obfuscated data, "
                       "letting teams test with representative data while protecting real customer information "
                       "in less-protected environments.",
            "distractors": {
                "B": "Copying live data unchanged exposes real sensitive records in a lower-trust environment, "
                     "increasing breach risk.",
                "C": "Granting production admin rights violates least privilege and does nothing to protect the "
                     "real data being used in test.",
                "D": "Disabling logging reduces visibility and does not protect the sensitive data.",
            },
            "exam_pattern": "Use masking/obfuscation (or synthetic data) so non-production environments never "
                            "hold real sensitive values.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data protection in non-production environments"],
    },

    # ----- cissp_data_roles ------------------------------------------------
    {
        "id": "cissp-asset-r2-005", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_roles", "difficulty": 2, "type": "mcq",
        "stem": "Within an agency's governance model, one role is accountable for a specific information "
                "SYSTEM - maintaining its system security plan and ensuring it is operated with the agreed "
                "controls - as distinct from the person accountable for the data the system processes. Which "
                "role is this?",
        "options": [
            {"id": "A", "text": "Data subject"},
            {"id": "B", "text": "Data processor"},
            {"id": "C", "text": "System (or mission/business) owner"},
            {"id": "D", "text": "Data custodian"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The system owner (sometimes mission or business owner) is accountable for a particular "
                       "system, including keeping its system security plan current and ensuring it is deployed "
                       "and operated with the agreed controls - distinct from the data owner, who is "
                       "accountable for the information itself.",
            "distractors": {
                "A": "The data subject is the individual the personal data describes, not an accountable "
                     "governance role.",
                "B": "A processor handles personal data on a controller's behalf; it is not the internal "
                     "system-accountability role.",
                "D": "The custodian implements and maintains protective controls but is not the accountable "
                     "owner of the system or its security plan.",
            },
            "exam_pattern": "Data owner = accountable for the data/classification; system (mission) owner = "
                            "accountable for the system and its security plan; custodian = implements controls.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data and system ownership roles"],
    },

    # ----- cissp_data_protection_methods -----------------------------------
    {
        "id": "cissp-asset-r2-006", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_protection_methods", "difficulty": 3, "type": "mcq",
        "stem": "To reduce privacy risk while retaining the ability to RE-LINK records for authorized "
                "analytics, a team replaces direct identifiers with reversible tokens held under a "
                "separately protected key. Under the GDPR, how is this data treated, and what is the term?",
        "options": [
            {"id": "A", "text": "Anonymization; the data is no longer personal data and falls outside the GDPR"},
            {"id": "B", "text": "Pseudonymization; it is still personal data because it can be re-identified using the separate key"},
            {"id": "C", "text": "Encryption; it is therefore exempt from all breach-notification rules"},
            {"id": "D", "text": "Aggregation; it automatically raises the classification"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Pseudonymization replaces identifiers with tokens that can be reversed using separately "
                       "held additional information; because re-identification remains possible, the GDPR still "
                       "treats pseudonymized data as personal data (Recital 26).",
            "distractors": {
                "A": "True anonymization is irreversible and would place data outside the GDPR; the described "
                     "method is reversible, so it is pseudonymization, not anonymization.",
                "C": "Encryption is a protective control and does not by itself exempt data from breach "
                     "analysis; the data remains personal data.",
                "D": "Aggregation combines records into a more sensitive whole; it is unrelated to the "
                     "reversible-token technique described.",
            },
            "exam_pattern": "Pseudonymization (reversible with a key) = still personal data under GDPR; only "
                            "irreversible anonymization leaves GDPR scope.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Anonymization vs pseudonymization",
                       "GDPR Recital 26 and Art. 4(5) (pseudonymization)"],
    },
    {
        "id": "cissp-asset-r2-007", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_protection_methods", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Securely destroying data by deleting or destroying the encryption keys "
                "that protect it - rendering the still-encrypted data unrecoverable without wiping the media "
                "itself - is called cryptographic ________ (also known as crypto-shredding).",
        "correct": ["erase", "erasure", "shredding", "shred"],
        "explanation": {
            "correct": "Cryptographic erase (crypto-shredding) destroys the keys needed to decrypt the data, "
                       "making the ciphertext permanently unrecoverable; it is especially useful for cloud "
                       "storage and self-encrypting drives where physical destruction is impractical.",
            "exam_pattern": "Destroy the keys, not the media = cryptographic erase / crypto-shredding (ideal "
                            "for cloud and self-encrypting drives).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Cryptographic erase",
                       "NIST SP 800-88 Rev. 1 (cryptographic erase)"],
    },

    # ===================================================================
    # Domain 3 - Security Architecture and Engineering (cissp_arch_eng)
    # ===================================================================
    # ----- cissp_security_models -------------------------------------------
    {
        "id": "cissp-arch-r2-001", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 3, "type": "mcq",
        "stem": "A product is submitted to an accredited lab for an internationally recognized security "
                "evaluation under ISO/IEC 15408. Evaluators assess the product (the Target of Evaluation) "
                "against stated requirements and assign a rating of EAL1 through EAL7. Which framework is "
                "this, and what does the EAL represent?",
        "options": [
            {"id": "A", "text": "Common Criteria; the Evaluation Assurance Level reflects the depth and rigor of the evaluation, not inherent security strength"},
            {"id": "B", "text": "TCSEC (Orange Book); the EAL is the network trust level"},
            {"id": "C", "text": "Common Criteria; the EAL is the number of vulnerabilities discovered"},
            {"id": "D", "text": "ITSEC; the EAL measures the encryption key length used"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Common Criteria (ISO/IEC 15408) evaluates a Target of Evaluation (TOE) against a "
                       "Protection Profile/Security Target; the Evaluation Assurance Level (EAL1-EAL7) "
                       "expresses HOW rigorously the product was evaluated, not how 'secure' it inherently is.",
            "distractors": {
                "B": "TCSEC (Orange Book) is the older U.S. standard and does not use EAL ratings or TOE "
                     "terminology; the EAL is not a network trust level.",
                "C": "The EAL reflects assurance/evaluation rigor, not a count of vulnerabilities found.",
                "D": "ITSEC is a separate European predecessor; the EAL does not measure key length.",
            },
            "exam_pattern": "Common Criteria (ISO/IEC 15408): TOE evaluated vs a PP/ST; EAL1-7 = assurance/rigor "
                            "of the evaluation, not absolute security.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Common Criteria",
                       "ISO/IEC 15408 (Common Criteria)"],
    },
    {
        "id": "cissp-arch-r2-002", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_models", "difficulty": 3, "type": "mcq",
        "stem": "On a classified system, every user holds a clearance for ALL information on the system and "
                "formal access approval for all of it, but each user has a valid need-to-know for only SOME "
                "of the data (the portion their job requires). Which security mode of operation is this?",
        "options": [
            {"id": "A", "text": "Dedicated security mode"},
            {"id": "B", "text": "System high security mode"},
            {"id": "C", "text": "Compartmented security mode"},
            {"id": "D", "text": "Multilevel (MLS) security mode"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In system high mode, all users have the clearance AND formal access approval for all "
                       "information on the system, but need-to-know applies to only the subset of data each "
                       "user actually requires.",
            "distractors": {
                "A": "Dedicated mode additionally requires need-to-know for ALL data on the system; here "
                     "need-to-know is for only some, so it is system high, not dedicated.",
                "C": "Compartmented mode limits formal access approval (and need-to-know) to specific "
                     "compartments; here approval covers all data, so it is not compartmented.",
                "D": "Multilevel mode supports users who are NOT cleared for all data on the system; here every "
                     "user is cleared for all data.",
            },
            "exam_pattern": "Modes - Dedicated (clearance+approval+need-to-know for ALL), System High (all but "
                            "need-to-know for some), Compartmented (approval/need-to-know limited), Multilevel "
                            "(users not cleared for all data).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Security modes of operation"],
    },

    # ----- cissp_crypto ----------------------------------------------------
    {
        "id": "cissp-arch-r2-003", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 3, "type": "mcq",
        "stem": "A developer encrypts a bitmap image with AES in Electronic Code Book (ECB) mode and is "
                "alarmed that outlines of the original image remain visible in the ciphertext. Why does ECB "
                "leak this pattern, and what should be used instead?",
        "options": [
            {"id": "A", "text": "ECB uses too short a key; simply use a longer key in ECB mode"},
            {"id": "B", "text": "ECB adds a random IV to every block, which corrupts the image; disable the IV"},
            {"id": "C", "text": "ECB is an asymmetric mode; switch to RSA for bulk encryption"},
            {"id": "D", "text": "ECB encrypts identical plaintext blocks to identical ciphertext blocks, revealing patterns; use a chaining/authenticated mode such as CBC, CTR, or GCM"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "ECB encrypts each block independently, so identical plaintext blocks always produce "
                       "identical ciphertext blocks, leaking structure and patterns. Use a mode that diffuses "
                       "patterns and ideally authenticates, such as CBC, CTR, or GCM (AEAD).",
            "distractors": {
                "A": "Key length is not the issue; the pattern leakage is inherent to ECB's block-independent "
                     "design regardless of key size.",
                "B": "ECB does NOT use an IV; the absence of an IV/chaining is exactly why patterns persist.",
                "C": "ECB is a mode of a symmetric block cipher (e.g., AES), not an asymmetric algorithm; RSA "
                     "is not a drop-in bulk-encryption replacement.",
            },
            "exam_pattern": "ECB leaks patterns (same block -> same ciphertext); avoid it - use CBC/CTR, or GCM "
                            "for authenticated encryption.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Block cipher modes",
                       "NIST SP 800-38A (block cipher modes of operation)"],
    },
    {
        "id": "cissp-arch-r2-004", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The PKI protocol a relying party uses to check, in real time, whether a "
                "single X.509 certificate has been revoked before its expiry - avoiding the latency of a "
                "periodically published revocation list - is ________ (give the acronym).",
        "correct": ["ocsp", "online certificate status protocol"],
        "explanation": {
            "correct": "OCSP (Online Certificate Status Protocol) returns the real-time revocation status of "
                       "an individual certificate, avoiding the delay of downloading a periodically published "
                       "certificate revocation list (CRL).",
            "exam_pattern": "OCSP = real-time, per-certificate revocation status; CRL = periodically published "
                            "list of revoked certificates (higher latency).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - PKI certificate revocation"],
    },
    {
        "id": "cissp-arch-r2-005", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_crypto", "difficulty": 2, "type": "mcq",
        "stem": "A team is choosing a hashing algorithm for NEW digital signatures and file-integrity "
                "checks. Which choice reflects CURRENT best practice given known cryptographic weaknesses?",
        "options": [
            {"id": "A", "text": "Use MD5 because it is fast and widely available"},
            {"id": "B", "text": "Use SHA-1 because it is still universally mandated"},
            {"id": "C", "text": "Avoid MD5 and SHA-1 (both have practical collision weaknesses) and use SHA-256 (SHA-2) or SHA-3"},
            {"id": "D", "text": "Use a CRC32 checksum, which is sufficient for signatures and integrity"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MD5 and SHA-1 are broken against collision attacks (NIST is retiring SHA-1 for all "
                       "uses by 2030); new designs should use SHA-2 (e.g., SHA-256) or SHA-3 for collision resistance.",
            "distractors": {
                "A": "MD5 is cryptographically broken (practical collisions) and must not be used for security; "
                     "its speed is irrelevant to that weakness.",
                "B": "SHA-1 is deprecated and being retired due to demonstrated collisions; it is not a sound "
                     "choice for new signatures.",
                "D": "CRC32 is an error-detection checksum, not a cryptographic hash; it provides no collision "
                     "resistance against intentional tampering.",
            },
            "exam_pattern": "MD5/SHA-1 are collision-broken (SHA-1 retired by NIST ~2030); use SHA-256/SHA-3. "
                            "CRCs detect accidental errors, not malicious tampering.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Hashing and collision resistance",
                       "NIST SP 800-131A / NIST SHA-1 retirement (by Dec 31, 2030)"],
    },

    # ----- cissp_security_capabilities -------------------------------------
    {
        "id": "cissp-arch-r2-006", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_security_capabilities", "difficulty": 3, "type": "mcq",
        "stem": "In a CPU protection-ring architecture, where does the operating-system kernel execute, and "
                "why does user application code run in a less privileged ring?",
        "options": [
            {"id": "A", "text": "The kernel runs in Ring 0 (most privileged) and applications in Ring 3 (least privileged), to isolate critical functions and limit the damage faulty or malicious code can do"},
            {"id": "B", "text": "The kernel runs in Ring 3 and applications in Ring 0, to give applications full hardware access"},
            {"id": "C", "text": "All code runs in a single ring for maximum performance"},
            {"id": "D", "text": "Applications run in Ring 0 so they can bypass the reference monitor when needed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Protection rings order privilege from Ring 0 (most privileged - the OS kernel) outward "
                       "to Ring 3 (least privileged - user applications). Running applications in an outer ring "
                       "isolates the trusted kernel and limits the harm untrusted code can cause.",
            "distractors": {
                "B": "This reverses the model; the kernel is Ring 0 (most privileged) and applications are "
                     "Ring 3 (least), not the other way around.",
                "C": "Collapsing all code into one ring removes process/kernel isolation and defeats the "
                     "protection the rings provide.",
                "D": "Letting applications run in Ring 0 would let them bypass isolation and the reference "
                     "monitor - the opposite of the design's intent.",
            },
            "exam_pattern": "Ring 0 = kernel (most privileged); Ring 3 = user apps (least); rings enforce "
                            "isolation so untrusted code cannot reach trusted functions.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Protection rings and process isolation"],
    },

    # ----- cissp_vuln_architectures ----------------------------------------
    {
        "id": "cissp-arch-r2-007", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_vuln_architectures", "difficulty": 3, "type": "mcq",
        "stem": "In a multi-tenant virtualized data center, a security architect is MOST concerned about an "
                "attack in which malicious code breaks out of a guest virtual machine and executes on the "
                "underlying hypervisor or against other tenants' VMs. What is this threat, and which control "
                "most directly reduces it?",
        "options": [
            {"id": "A", "text": "VM sprawl; solved by buying more hardware"},
            {"id": "B", "text": "VM escape; reduced by hardening and promptly patching the hypervisor and maintaining strong VM isolation"},
            {"id": "C", "text": "A covert channel; eliminated by requiring longer passwords"},
            {"id": "D", "text": "Data remanence; solved by degaussing the storage array"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "VM escape is when code breaks out of a guest VM to reach the hypervisor or sibling VMs, "
                       "undermining tenant isolation; the primary defenses are hardening and promptly patching "
                       "the hypervisor and enforcing strong isolation and segmentation.",
            "distractors": {
                "A": "VM sprawl is uncontrolled growth of unmanaged VMs - a management/attack-surface issue, "
                     "not a break of tenant isolation; adding hardware does not address escape.",
                "C": "A covert channel is an unintended signaling path; password length is irrelevant to "
                     "hypervisor breakout.",
                "D": "Data remanence concerns residual data left on media; degaussing does not address runtime "
                     "VM isolation.",
            },
            "exam_pattern": "Guest code breaking out to the hypervisor/other tenants = VM escape; patch and "
                            "harden the hypervisor and preserve strong isolation.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Virtualization and hypervisor security"],
    },
    {
        "id": "cissp-arch-r2-008", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_vuln_architectures", "difficulty": 3, "type": "mcq",
        "stem": "Two processes that are forbidden by policy to communicate nonetheless pass information: "
                "one process varies how long it holds the CPU while the other measures those delays to read "
                "the signal. Which flaw is this, and which specific type?",
        "options": [
            {"id": "A", "text": "A buffer overflow; a stack-based type"},
            {"id": "B", "text": "A covert channel; specifically a covert storage channel"},
            {"id": "C", "text": "A race condition; a TOCTOU type"},
            {"id": "D", "text": "A covert channel; specifically a covert timing channel"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A covert channel is an unauthorized communication path that bypasses the security "
                       "policy; signaling information through the TIMING of events (CPU scheduling delays here) "
                       "is a covert timing channel.",
            "distractors": {
                "A": "A buffer overflow overwrites memory beyond a buffer; it is not a policy-bypassing "
                     "signaling path.",
                "B": "A covert storage channel signals by writing to a shared storage location the other "
                     "process reads; here the signal is carried by timing, not stored data.",
                "C": "A TOCTOU race exploits a check-to-use gap; this scenario is covert signaling via timing, "
                     "not a check/use ordering flaw.",
            },
            "exam_pattern": "Covert channel = unauthorized signaling path; timing channel (modulate event "
                            "timing) vs storage channel (write/read a shared location).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - Covert channels"],
    },

    # ----- cissp_physical_security -----------------------------------------
    {
        "id": "cissp-arch-r2-009", "exam": "cissp", "domain": "cissp_arch_eng",
        "subtopic": "cissp_physical_security", "difficulty": 2, "type": "mcq",
        "stem": "A campus is redesigned so that lighting and sightlines naturally expose intruders to "
                "observation, walkways funnel visitors past a staffed reception, and landscaping and signage "
                "clearly mark private areas. Which physical-security approach is being applied?",
        "options": [
            {"id": "A", "text": "Crime Prevention Through Environmental Design (CPTED)"},
            {"id": "B", "text": "Defense in depth at the network layer"},
            {"id": "C", "text": "Mandatory access control (MAC)"},
            {"id": "D", "text": "A clean-desk policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CPTED uses the built environment - natural surveillance (lighting/sightlines), natural "
                       "access control (channeling movement past staffed points), and territorial "
                       "reinforcement (signage/landscaping) - to deter crime before technical controls are needed.",
            "distractors": {
                "B": "Network-layer defense in depth concerns logical controls, not the physical environment described.",
                "C": "MAC is a logical access-control model using clearance labels, unrelated to site and "
                     "landscape design.",
                "D": "A clean-desk policy protects information left on desks; it does not shape the environment "
                     "to deter intruders.",
            },
            "exam_pattern": "CPTED = natural surveillance + natural access control + territorial reinforcement "
                            "to deter crime through environmental design.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 3 - CPTED and physical security design"],
    },

    # ===================================================================
    # Domain 4 - Communication and Network Security (cissp_comm_net)
    # ===================================================================
    # ----- cissp_secure_network_design -------------------------------------
    {
        "id": "cissp-net-r2-001", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise wants every device to authenticate and pass a health/posture check (patch "
                "level, antivirus status) BEFORE it is admitted to the production network, placing "
                "non-compliant devices into a quarantine VLAN for remediation. Which technology provides this?",
        "options": [
            {"id": "A", "text": "Network Access Control (NAC), commonly enforced with 802.1X"},
            {"id": "B", "text": "A wet-pipe fire-sprinkler system"},
            {"id": "C", "text": "A single static ACL on the core router"},
            {"id": "D", "text": "A password manager"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NAC authenticates devices and evaluates endpoint posture/health before admitting them, "
                       "placing non-compliant or unknown devices into a quarantine/remediation segment; 802.1X "
                       "port-based control is a common enforcement mechanism.",
            "distractors": {
                "B": "A sprinkler system is a fire-suppression control, unrelated to network admission.",
                "C": "A static ACL filters by address/port but cannot authenticate a device or assess its posture.",
                "D": "A password manager stores credentials; it does not gate network admission based on device health.",
            },
            "exam_pattern": "Authenticate + posture-check endpoints before admission, quarantine the "
                            "non-compliant = NAC (commonly via 802.1X).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Network access control (NAC/802.1X)"],
    },
    {
        "id": "cissp-net-r2-002", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 3, "type": "mcq",
        "stem": "In a software-defined network (SDN), a central controller programs the forwarding behavior "
                "of switches. Architecturally, what fundamental change does SDN introduce, and what new "
                "security concern follows?",
        "options": [
            {"id": "A", "text": "It merges the control and data planes onto each switch; the concern is slower routing"},
            {"id": "B", "text": "It encrypts all user data by default; the concern is key storage"},
            {"id": "C", "text": "It decouples the control plane from the data plane into a central controller; the controller (and its APIs) becomes a high-value single point of attack and failure"},
            {"id": "D", "text": "It removes the need for any firewalls; the concern is cost"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "SDN separates the control plane (decision-making) from the data plane (forwarding) and "
                       "centralizes control in a controller. That centralization improves agility but makes the "
                       "controller and its northbound/southbound APIs a high-value target and potential single "
                       "point of failure.",
            "distractors": {
                "A": "SDN separates, rather than merges, the control and data planes; the key issue is "
                     "centralization risk, not routing speed.",
                "B": "SDN is about programmable control, not default data encryption; key storage is not its "
                     "defining concern.",
                "D": "SDN does not remove the need for firewalls or other controls; segmentation and policy "
                     "enforcement are still required.",
            },
            "exam_pattern": "SDN decouples the control plane from the data plane (central controller); secure "
                            "the controller and its APIs - a prime single point of attack.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Software-defined networking"],
    },

    # ----- cissp_network_components ----------------------------------------
    {
        "id": "cissp-net-r2-003", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 2, "type": "mcq",
        "stem": "A company's public web application keeps getting hit with SQL injection and cross-site "
                "scripting attempts that a traditional network firewall allows through because they ride on "
                "permitted HTTPS. Which control is PURPOSE-BUILT to inspect and filter these Layer 7 web "
                "attacks?",
        "options": [
            {"id": "A", "text": "A Layer 3 packet-filtering router ACL"},
            {"id": "B", "text": "A web application firewall (WAF)"},
            {"id": "C", "text": "A network time (NTP) server"},
            {"id": "D", "text": "A load balancer configured for round-robin"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A WAF operates at the application layer and inspects HTTP/HTTPS requests for "
                       "web-specific attacks (SQLi, XSS, etc.), blocking malicious payloads that a network "
                       "firewall - which only sees permitted ports/protocols - lets pass.",
            "distractors": {
                "A": "A packet-filtering ACL works on addresses/ports and cannot parse HTTP payloads to catch SQLi/XSS.",
                "C": "A time server synchronizes clocks; it provides no attack filtering.",
                "D": "A load balancer distributes traffic for availability/performance; round-robin does not "
                     "inspect for web attacks.",
            },
            "exam_pattern": "Filter Layer 7 web attacks (SQLi/XSS) riding on allowed HTTPS = web application "
                            "firewall (WAF), complementing the network firewall.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Web application firewalls"],
    },
    {
        "id": "cissp-net-r2-004", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 2, "type": "mcq",
        "stem": "Administrators must manage servers in a sensitive, segmented zone. Security wants all "
                "administrative sessions to pass through a single hardened, heavily monitored system that "
                "brokers and logs the access rather than letting admins connect to each server directly. "
                "Which component is this?",
        "options": [
            {"id": "A", "text": "A honeynet"},
            {"id": "B", "text": "A content delivery network (CDN) edge node"},
            {"id": "C", "text": "A DHCP relay agent"},
            {"id": "D", "text": "A bastion host (jump server)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A bastion host (jump server) is a hardened, closely monitored chokepoint through which "
                       "administrative access to a protected segment is funneled and logged, reducing exposure "
                       "and centralizing control of privileged access.",
            "distractors": {
                "A": "A honeynet is a decoy network to attract and study attackers, not a sanctioned admin "
                     "access path.",
                "B": "A CDN edge node caches and serves public content near users; it is not an internal admin gateway.",
                "C": "A DHCP relay forwards address-assignment requests; it plays no role in brokering admin sessions.",
            },
            "exam_pattern": "Single hardened, logged chokepoint for admin access into a sensitive zone = "
                            "bastion host / jump server.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Bastion hosts / jump servers"],
    },

    # ----- cissp_secure_channels -------------------------------------------
    {
        "id": "cissp-net-r2-005", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 2, "type": "mcq",
        "stem": "A company upgrades its wireless to resist offline password-guessing (dictionary) attacks "
                "against the Wi-Fi passphrase and to provide forward secrecy on its personal (pre-shared-key) "
                "networks. Which standard and handshake should it adopt?",
        "options": [
            {"id": "A", "text": "WEP with a 128-bit key"},
            {"id": "B", "text": "Open (unauthenticated) Wi-Fi with a captive portal"},
            {"id": "C", "text": "WPA3-Personal, which uses Simultaneous Authentication of Equals (SAE) to replace the WPA2 pre-shared-key handshake"},
            {"id": "D", "text": "WPA2 with TKIP"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "WPA3-Personal replaces WPA2's pre-shared-key (4-way) handshake with SAE (Simultaneous "
                       "Authentication of Equals, a Dragonfly handshake), which resists offline dictionary "
                       "attacks against the passphrase and provides forward secrecy.",
            "distractors": {
                "A": "WEP is thoroughly broken and provides no meaningful protection.",
                "B": "Open Wi-Fi provides no cryptographic authentication of a passphrase at all.",
                "D": "WPA2 with TKIP is legacy and remains vulnerable to offline dictionary attacks against a "
                     "weak PSK, and it lacks SAE's protections.",
            },
            "exam_pattern": "Resist offline Wi-Fi dictionary attacks + forward secrecy on personal networks = "
                            "WPA3-Personal with SAE (replaces the WPA2 PSK handshake).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Wireless security (WPA3)",
                       "Wi-Fi Alliance WPA3 / IEEE 802.11 SAE"],
    },
    {
        "id": "cissp-net-r2-006", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 2, "type": "multi",
        "stem": "A remote-access VPN must be hardened and legacy protocols retired. Which TWO choices are "
                "appropriate, CURRENT options for the tunnel protocol? (Choose two.)",
        "options": [
            {"id": "A", "text": "IPsec with IKEv2"},
            {"id": "B", "text": "PPTP (Point-to-Point Tunneling Protocol)"},
            {"id": "C", "text": "A TLS-based (SSL) VPN"},
            {"id": "D", "text": "Plain L2TP with no IPsec"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "A hardened remote-access VPN uses modern, strongly authenticated encryption such as "
                       "IPsec with IKEv2 or a TLS-based (SSL) VPN, both of which use current cryptography.",
            "distractors": {
                "B": "PPTP relies on broken/weak mechanisms (MS-CHAPv2, RC4) and should be retired, not used "
                     "for new deployments.",
                "D": "L2TP by itself provides no encryption; it must be paired with IPsec (L2TP/IPsec) to be secure.",
            },
            "exam_pattern": "Use IPsec/IKEv2 or TLS VPNs; avoid PPTP, and never run L2TP without IPsec.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - VPN protocols and hardening"],
    },

    # ----- cissp_network_attacks -------------------------------------------
    {
        "id": "cissp-net-r2-007", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "On a switched network, an attacker crafts frames carrying two stacked 802.1Q tags "
                "(double-tagging) so that traffic leaks from the attacker's VLAN into a target VLAN it "
                "should not reach. Which attack is this, and a key mitigation?",
        "options": [
            {"id": "A", "text": "ARP poisoning; mitigated by DNSSEC"},
            {"id": "B", "text": "A SYN flood; mitigated by SYN cookies"},
            {"id": "C", "text": "MAC flooding; mitigated by longer passwords"},
            {"id": "D", "text": "VLAN hopping; mitigated by disabling automatic trunking (DTP) and not using the native VLAN for user access"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Double-tagging is a VLAN-hopping technique. Mitigations include disabling Dynamic "
                       "Trunking Protocol (set access ports to not negotiate), avoiding use of the native VLAN "
                       "for user data, and explicitly configuring trunk ports.",
            "distractors": {
                "A": "ARP poisoning forges MAC-to-IP mappings on a LAN; DNSSEC addresses DNS integrity, not "
                     "802.1Q tag abuse.",
                "B": "A SYN flood exhausts TCP connection tables; SYN cookies are unrelated to 802.1Q tag handling.",
                "C": "MAC flooding overflows the switch's CAM table; password length is irrelevant, and it is a "
                     "different attack from tag-based VLAN hopping.",
            },
            "exam_pattern": "Double-tagged frames crossing VLANs = VLAN hopping; disable DTP/auto-trunk and "
                            "don't use the native VLAN for users.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - VLAN hopping"],
    },
    {
        "id": "cissp-net-r2-008", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "Attackers send small spoofed requests (with the victim's source address) to open DNS and "
                "NTP servers, which reply with much larger responses directed at the victim, overwhelming "
                "its bandwidth. Which attack technique is this?",
        "options": [
            {"id": "A", "text": "A phishing campaign"},
            {"id": "B", "text": "A reflection/amplification distributed denial-of-service (DDoS) attack"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Privilege escalation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Reflection/amplification DDoS spoofs the victim's source address toward open services "
                       "(DNS, NTP, memcached) whose large replies flood the victim; the amplification factor "
                       "multiplies the attacker's effective bandwidth.",
            "distractors": {
                "A": "Phishing tricks users into revealing data or running malware; it is not a bandwidth-flooding technique.",
                "C": "SQL injection manipulates database queries, unrelated to volumetric flooding.",
                "D": "Privilege escalation gains higher rights on a system; it does not describe reflected traffic floods.",
            },
            "exam_pattern": "Small spoofed requests to open resolvers/servers returning large replies at a "
                            "victim = reflection/amplification DDoS; mitigate with source-address validation "
                            "(BCP 38) and closing open services.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - DDoS (reflection/amplification)"],
    },
    {
        "id": "cissp-net-r2-009", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker floods a switch with thousands of frames bearing bogus source MAC addresses, "
                "overflowing its CAM (MAC address) table. What is the attacker's goal, and the standard "
                "mitigation?",
        "options": [
            {"id": "A", "text": "To exhaust the DHCP address pool; mitigated by a longer lease time"},
            {"id": "B", "text": "To poison the DNS resolver cache; mitigated by DNSSEC"},
            {"id": "C", "text": "To force the switch to flood frames out all ports (fail-open) so the attacker can sniff traffic; mitigated by port security limiting MACs per port"},
            {"id": "D", "text": "To crash the router's Layer 3 routing table; mitigated by BGP route dampening"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When the CAM table overflows, many switches 'fail open' and flood frames out all ports, "
                       "letting the attacker sniff traffic intended for others. Port security (limiting and "
                       "pinning the MAC addresses allowed per port) is the standard mitigation.",
            "distractors": {
                "A": "MAC flooding targets the switch's CAM table, not the DHCP pool; exhausting DHCP is a "
                     "separate 'DHCP starvation' attack.",
                "B": "It does not inject DNS records; DNSSEC addresses DNS response integrity, not CAM-table overflow.",
                "D": "It affects a Layer 2 switch's MAC table, not a router's Layer 3 routing table or BGP.",
            },
            "exam_pattern": "Overflow the CAM table so the switch floods (fail-open) and the attacker sniffs = "
                            "MAC flooding; mitigate with port security.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - MAC flooding / CAM-table overflow"],
    },

    # ===================================================================
    # Domain 5 - Identity and Access Management (cissp_iam)
    # ===================================================================
    # ----- cissp_identity_lifecycle ----------------------------------------
    {
        "id": "cissp-iam-r2-001", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 3, "type": "mcq",
        "stem": "A security team wants to control, vault, and record all use of highly privileged "
                "administrator and root accounts, issuing their credentials just-in-time and capturing "
                "session activity for later review. Which capability provides this?",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO) for end users"},
            {"id": "B", "text": "A password-expiration policy"},
            {"id": "C", "text": "Privileged access management (PAM)"},
            {"id": "D", "text": "A guest Wi-Fi captive portal"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "PAM secures elevated accounts by vaulting their credentials, brokering just-in-time "
                       "access through approval workflows, and recording privileged sessions so their use can "
                       "be monitored and audited.",
            "distractors": {
                "A": "SSO streamlines everyday user authentication; it does not vault or record privileged "
                     "administrator credentials.",
                "B": "Password expiration rotates secrets but does not control, broker, or record privileged-session use.",
                "D": "A guest portal governs visitor internet access, unrelated to privileged-account control.",
            },
            "exam_pattern": "Vault + just-in-time + session recording for admin/root accounts = privileged "
                            "access management (PAM).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Privileged access management"],
    },
    {
        "id": "cissp-iam-r2-002", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_identity_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "A company uses dozens of SaaS applications and keeps finding active accounts belonging to "
                "employees who left months ago. Which approach BEST prevents these orphaned accounts going "
                "forward?",
        "options": [
            {"id": "A", "text": "Automate provisioning and deprovisioning from the authoritative identity source to the apps (e.g., via SCIM), so a departure immediately disables downstream accounts"},
            {"id": "B", "text": "Ask each application owner to manually check for ex-employees once a year"},
            {"id": "C", "text": "Share one administrator login across all SaaS applications"},
            {"id": "D", "text": "Lengthen the password-complexity requirements"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automated identity-lifecycle provisioning/deprovisioning (commonly via SCIM) driven by "
                       "the authoritative HR/identity source ensures that when a user is disabled centrally, "
                       "their downstream SaaS accounts are promptly removed, preventing orphaned accounts.",
            "distractors": {
                "B": "Annual manual checks leave long windows in which orphaned accounts remain exploitable; "
                     "timely automation is needed.",
                "C": "A shared admin login destroys accountability and worsens access risk; it does not address "
                     "orphaned user accounts.",
                "D": "Stronger passwords do not remove accounts that should no longer exist.",
            },
            "exam_pattern": "Prevent orphaned accounts with automated deprovisioning from the authoritative "
                            "source (e.g., SCIM), not periodic manual review.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Provisioning/deprovisioning (SCIM)"],
    },

    # ----- cissp_authentication_methods ------------------------------------
    {
        "id": "cissp-iam-r2-003", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 3, "type": "mcq",
        "stem": "To stop credential phishing, an organization replaces passwords with FIDO2/WebAuthn "
                "authenticators (passkeys and security keys). Why are these considered PHISHING-RESISTANT?",
        "options": [
            {"id": "A", "text": "They use a longer, more complex shared password that is harder to guess"},
            {"id": "B", "text": "They email the user a one-time code to copy into the site"},
            {"id": "C", "text": "They rely on SMS codes, which cannot be intercepted"},
            {"id": "D", "text": "They use public-key cryptography bound to the legitimate site's origin, so the private key never leaves the device and no reusable secret can be replayed on a look-alike site"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "FIDO2/WebAuthn uses origin-bound public-key credentials: the authenticator signs a "
                       "challenge for the specific registered domain, the private key never leaves the device, "
                       "and nothing reusable is transmitted - so a phishing site at a different origin cannot "
                       "obtain or replay a usable credential.",
            "distractors": {
                "A": "A stronger password is still a shared secret that can be phished or replayed; FIDO2's "
                     "strength is that there is no phishable shared secret.",
                "B": "Emailed one-time codes can be relayed to an attacker through a phishing proxy; they are "
                     "not cryptographically bound to the site origin.",
                "C": "SMS codes are phishable and subject to SIM-swap/interception; they are not origin-bound.",
            },
            "exam_pattern": "FIDO2/passkeys are phishing-resistant because credentials are origin-bound "
                            "public-key pairs with no shared secret to phish or replay.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Phishing-resistant authentication (FIDO2)",
                       "FIDO2 / W3C WebAuthn; NIST SP 800-63B (phishing resistance)"],
    },
    {
        "id": "cissp-iam-r2-004", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 2, "type": "mcq",
        "stem": "A soft-token app shows a 6-digit code that automatically changes every 30 seconds. Which "
                "one-time-password scheme is this, and how does it differ from the counter-based alternative?",
        "options": [
            {"id": "A", "text": "HOTP; it changes only when the user presses a button (event/counter based)"},
            {"id": "B", "text": "TOTP; it derives the code from a shared secret and the current time, expiring on a fixed interval, whereas HOTP is event/counter based"},
            {"id": "C", "text": "A static PIN; it never changes"},
            {"id": "D", "text": "A CAPTCHA; it proves the user is human"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A code that rotates on a time interval is a Time-based One-Time Password (TOTP), "
                       "computed from a shared secret and the current time. HOTP (HMAC-based OTP) instead "
                       "increments a counter with each use (event-based).",
            "distractors": {
                "A": "The button/counter description is HOTP, not the time-interval code in the scenario.",
                "C": "A static PIN does not change; the scenario's code rotates every 30 seconds.",
                "D": "A CAPTCHA distinguishes humans from bots and is not a one-time password.",
            },
            "exam_pattern": "Time-interval code = TOTP; event/counter code = HOTP (both derive from a shared seed/secret).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - One-time passwords",
                       "RFC 6238 (TOTP); RFC 4226 (HOTP)"],
    },
    {
        "id": "cissp-iam-r2-005", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_authentication_methods", "difficulty": 3, "type": "mcq",
        "stem": "A network team needs an AAA protocol for administrator logins to routers and switches that "
                "encrypts the ENTIRE packet payload and SEPARATES authentication, authorization, and "
                "accounting (to support per-command authorization). Which protocol BEST fits?",
        "options": [
            {"id": "A", "text": "TACACS+"},
            {"id": "B", "text": "RADIUS"},
            {"id": "C", "text": "SNMPv2c"},
            {"id": "D", "text": "HTTP Basic authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TACACS+ runs over TCP (port 49), encrypts the full packet payload, and cleanly "
                       "separates authentication, authorization, and accounting - enabling the granular "
                       "per-command authorization favored for device administration.",
            "distractors": {
                "B": "RADIUS encrypts only the password in its packets and combines authentication with "
                     "authorization, making per-command control harder; it is typically used for network "
                     "access (Wi-Fi/VPN/802.1X).",
                "C": "SNMPv2c is a network-management protocol using clear-text community strings; it is not an "
                     "AAA protocol.",
                "D": "HTTP Basic sends base64-encoded credentials with no payload encryption of its own and "
                     "provides no AAA separation.",
            },
            "exam_pattern": "Full-payload encryption + separated AAA + per-command authz for device admin = "
                            "TACACS+ (TCP/49); RADIUS = network access, password-only encryption, combined authn/authz.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - AAA protocols (TACACS+ vs RADIUS)",
                       "RFC 8907 (TACACS+); RFC 2865 (RADIUS)"],
    },

    # ----- cissp_access_control_models -------------------------------------
    {
        "id": "cissp-iam-r2-006", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 3, "type": "mcq",
        "stem": "An access control matrix can be stored by column or by row. A list bound to a SUBJECT that "
                "enumerates every object the subject may access and the allowed operations is which structure?",
        "options": [
            {"id": "A", "text": "An access control list (ACL) - the object's column of the matrix (the subjects permitted to an object)"},
            {"id": "B", "text": "A security clearance label"},
            {"id": "C", "text": "A capability list (capability table) - the subject's row of the matrix"},
            {"id": "D", "text": "A firewall rule base"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A capability list is organized by SUBJECT (a row of the access matrix): it lists the "
                       "objects that subject can access and the allowed operations. An ACL, by contrast, is "
                       "organized by object (a column), listing which subjects may access that object.",
            "distractors": {
                "A": "An ACL is bound to the OBJECT and lists the subjects permitted to it (the object's "
                     "column) - the opposite orientation of the subject-bound list described.",
                "B": "A security label expresses classification/clearance for MAC decisions; it is not the "
                     "matrix row/column storage structure.",
                "D": "A firewall rule base filters network traffic; it is not a representation of the "
                     "subject/object access matrix.",
            },
            "exam_pattern": "Access matrix stored by subject (row) = capability list; stored by object (column) = ACL.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Access control matrix (ACLs vs capability lists)"],
    },
    {
        "id": "cissp-iam-r2-007", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_access_control_models", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Holding a sufficient clearance is necessary but NOT sufficient to access "
                "classified data; access is further restricted by the ________ principle, which limits a "
                "user to only the specific information their duties require.",
        "correct": ["need to know", "need-to-know", "need to know principle"],
        "explanation": {
            "correct": "Need-to-know limits access to only the information required for one's duties, even when "
                       "the user's clearance level would otherwise permit broader access; clearance plus "
                       "need-to-know together gate access to classified data.",
            "exam_pattern": "Clearance >= classification is necessary but NOT sufficient; need-to-know further "
                            "restricts access to job-required data.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Need-to-know and least privilege"],
    },

    # ----- cissp_federated_identity ----------------------------------------
    {
        "id": "cissp-iam-r2-008", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_federated_identity", "difficulty": 3, "type": "mcq",
        "stem": "In Kerberos, after a user authenticates, which sequence CORRECTLY describes how the user "
                "gains access to a specific application server?",
        "options": [
            {"id": "A", "text": "The user sends their password to the application server, which validates it directly"},
            {"id": "B", "text": "The application server issues the user a long-term secret key to reuse for all services"},
            {"id": "C", "text": "The user requests a new password from the KDC for each service they access"},
            {"id": "D", "text": "The Authentication Server issues a Ticket-Granting Ticket (TGT); the user presents the TGT to the Ticket-Granting Service to obtain a service ticket, which is then presented to the application server"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Kerberos flow: the Authentication Server (AS) in the KDC issues a TGT after initial "
                       "authentication; the client presents the TGT to the Ticket-Granting Service (TGS) to "
                       "obtain a service (session) ticket for a specific service; the client then presents that "
                       "service ticket to the target server. Passwords are not sent to each service.",
            "distractors": {
                "A": "Kerberos specifically avoids sending the password to each application server; tickets "
                     "(not passwords) authenticate the user to services.",
                "B": "The application server does not hand out long-term secret keys to users; session keys are "
                     "distributed via tickets from the KDC.",
                "C": "The KDC issues tickets, not new passwords, for each service request.",
            },
            "exam_pattern": "Kerberos: AS -> TGT; present TGT to TGS -> service ticket; present service ticket "
                            "to the server (KDC = AS + TGS; tickets, not passwords, authenticate to services).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - Kerberos ticketing (AS/TGS)"],
    },
    {
        "id": "cissp-iam-r2-009", "exam": "cissp", "domain": "cissp_iam",
        "subtopic": "cissp_federated_identity", "difficulty": 2, "type": "mcq",
        "stem": "A modern mobile app needs to (1) confirm WHO the user is and (2) obtain delegated "
                "permission to call an API on the user's behalf. Which statement CORRECTLY pairs the tokens "
                "involved?",
        "options": [
            {"id": "A", "text": "OpenID Connect issues an ID token to assert the user's identity (authentication); OAuth 2.0 issues an access token to authorize the API calls"},
            {"id": "B", "text": "OAuth 2.0's access token proves the user's identity for login"},
            {"id": "C", "text": "SAML issues an ID token used to call REST APIs from mobile apps"},
            {"id": "D", "text": "The ID token is sent to the API as the bearer credential for authorization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OpenID Connect (built on OAuth 2.0) provides an ID token that asserts the "
                       "authenticated user's identity, while OAuth 2.0 provides an access token used to "
                       "authorize calls to protected APIs. The two tokens serve distinct purposes.",
            "distractors": {
                "B": "An OAuth access token conveys authorization (scopes), not verified user identity; using "
                     "it as proof of login is a known anti-pattern that OIDC was created to fix.",
                "C": "SAML uses XML assertions (not an OIDC 'ID token') and is oriented to browser SSO, not "
                     "typically mobile REST-API calls.",
                "D": "The ID token is for the client to learn who the user is; the ACCESS token (not the ID "
                     "token) is the bearer credential presented to the API.",
            },
            "exam_pattern": "OIDC ID token = who the user is (authn); OAuth access token = permission to call "
                            "APIs (authz). Don't use an access token as proof of identity.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 5 - OAuth 2.0 and OpenID Connect tokens"],
    },

    # ===================================================================
    # Domain 6 - Security Assessment and Testing (cissp_assess_test)
    # ===================================================================
    # ----- cissp_assessment_strategies -------------------------------------
    {
        "id": "cissp-assess-r2-001", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 2, "type": "mcq",
        "stem": "In a security exercise, one group emulates adversary tactics to attack, another defends "
                "and detects, and a coordinating function has them share findings in real time so defenses "
                "improve. What are these three roles called?",
        "options": [
            {"id": "A", "text": "Red team (attack), blue team (defend), and purple team (collaboration between them)"},
            {"id": "B", "text": "White team, gray team, and black team"},
            {"id": "C", "text": "SOC 1, SOC 2, and SOC 3 teams"},
            {"id": "D", "text": "Owner, custodian, and steward"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The red team emulates attackers, the blue team defends and detects, and the purple "
                       "team is the collaborative function that ensures the red team's findings feed directly "
                       "into blue-team improvements (a white team/cell often controls the exercise).",
            "distractors": {
                "B": "These are not the standard exercise roles; the recognized trio is red/blue/purple (with "
                     "a white team as controllers).",
                "C": "SOC 1/2/3 are AICPA attestation report types, not exercise teams.",
                "D": "Owner/custodian/steward are data-governance roles, unrelated to offensive/defensive teams.",
            },
            "exam_pattern": "Red = offense, blue = defense, purple = collaboration that turns attack findings "
                            "into defensive gains.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Red/blue/purple team exercises"],
    },
    {
        "id": "cissp-assess-r2-002", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability team finds that their scans miss missing patches and misconfigurations "
                "that are actually present on hosts. Which change will MOST improve the accuracy and depth of "
                "the results, and why?",
        "options": [
            {"id": "A", "text": "Run the scans less frequently to reduce noise"},
            {"id": "B", "text": "Scan only from the internet with no credentials, to stay realistic"},
            {"id": "C", "text": "Use credentialed (authenticated) scans, which log into hosts to read patch levels and configurations, yielding deeper and more accurate results with fewer false positives"},
            {"id": "D", "text": "Disable the scanner's plugin/signature updates"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Authenticated (credentialed) scans log into the target to inspect installed patches, "
                       "configurations, and OS details directly, producing deeper, more accurate findings and "
                       "fewer false positives than unauthenticated scans that only see the network-exposed surface.",
            "distractors": {
                "A": "Reducing scan frequency does not improve per-scan accuracy and leaves issues undetected longer.",
                "B": "Unauthenticated external scanning is exactly what is missing internal detail; it cannot "
                     "read on-host patch/config state.",
                "D": "Disabling plugin/signature updates makes the scanner blind to newer vulnerabilities, "
                     "reducing accuracy.",
            },
            "exam_pattern": "Credentialed (authenticated) scans see on-host patch/config state -> deeper, more "
                            "accurate, fewer false positives than uncredentialed scans.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Credentialed vs uncredentialed scanning"],
    },

    # ----- cissp_security_testing ------------------------------------------
    {
        "id": "cissp-assess-r2-003", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 2, "type": "mcq",
        "stem": "After a widely exploited flaw in a popular open-source logging library, a team wants to "
                "continuously inventory and flag vulnerable THIRD-PARTY and open-source components in their "
                "applications. Which testing approach addresses this directly?",
        "options": [
            {"id": "A", "text": "Fuzzing the application's own input parsers"},
            {"id": "B", "text": "Software composition analysis (SCA) of third-party/open-source dependencies"},
            {"id": "C", "text": "A physical penetration test of the data center"},
            {"id": "D", "text": "Load testing for peak traffic"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Software composition analysis (SCA) inventories an application's third-party and "
                       "open-source components and flags those with known vulnerabilities or problematic "
                       "licenses - the control that surfaces risks like a vulnerable logging library.",
            "distractors": {
                "A": "Fuzzing probes the application's own input handling for crashes; it does not inventory "
                     "third-party component versions against vulnerability databases.",
                "C": "A physical penetration test assesses facility security, not software dependencies.",
                "D": "Load testing measures performance under traffic, not component vulnerability exposure.",
            },
            "exam_pattern": "Inventory and flag vulnerable third-party/open-source components = software "
                            "composition analysis (SCA); central to software supply-chain risk.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Software composition analysis"],
    },
    {
        "id": "cissp-assess-r2-004", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 3, "type": "mcq",
        "stem": "To verify a customer-facing service works correctly and meets performance targets BEFORE "
                "real users complain, operations runs scripted interactions that mimic typical user actions "
                "on a schedule and alerts on failures. What is this monitoring technique?",
        "options": [
            {"id": "A", "text": "Fuzz testing"},
            {"id": "B", "text": "Static application security testing (SAST)"},
            {"id": "C", "text": "A black-box penetration test"},
            {"id": "D", "text": "Synthetic transactions (synthetic monitoring)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Synthetic transactions are scripted, automated interactions that emulate real user "
                       "activity against a system on a schedule to proactively verify availability, "
                       "correctness, and performance - catching issues before actual users are affected.",
            "distractors": {
                "A": "Fuzzing sends malformed input to find crashes/flaws; it is not scheduled emulation of "
                     "normal user workflows.",
                "B": "SAST analyzes source code without running the app; it does not exercise a live service's "
                     "transactions.",
                "C": "A penetration test attempts to exploit weaknesses; it is not routine scripted "
                     "health/performance monitoring.",
            },
            "exam_pattern": "Scripted, scheduled emulation of real user actions to verify availability/"
                            "performance = synthetic transactions (contrast with real-user monitoring).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Synthetic transactions"],
    },

    # ----- cissp_audit_logging ---------------------------------------------
    {
        "id": "cissp-assess-r2-005", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The predefined threshold below which routine, benign events (such as a "
                "few failed logins) are not alerted on - so that an alarm is raised only when activity "
                "exceeds it - is called a ________ level.",
        "correct": ["clipping"],
        "explanation": {
            "correct": "A clipping level suppresses routine, low-level events and triggers alerting only when a "
                       "defined threshold is exceeded, reducing noise while still catching anomalies such as "
                       "excessive failed logins.",
            "exam_pattern": "Threshold that suppresses routine events and alerts only above it = clipping level.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Audit thresholds (clipping levels)"],
    },
    {
        "id": "cissp-assess-r2-006", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 2, "type": "mcq",
        "stem": "A payroll service provider's clients need assurance, for their own financial-statement "
                "audits, about the provider's controls that affect the clients' internal control over "
                "financial reporting (ICFR). Which report is designed for this purpose?",
        "options": [
            {"id": "A", "text": "A SOC 2 report"},
            {"id": "B", "text": "A SOC 3 report"},
            {"id": "C", "text": "A SOC 1 report"},
            {"id": "D", "text": "A penetration-test report"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A SOC 1 report addresses a service organization's controls relevant to its clients' "
                       "internal control over financial reporting (ICFR), which is exactly what the clients' "
                       "financial auditors need.",
            "distractors": {
                "A": "A SOC 2 report covers the Trust Services Criteria (security, availability, etc.), not "
                     "financial-reporting controls specifically.",
                "B": "A SOC 3 is a short, general-use summary of SOC 2 subject matter; it is not the ICFR-focused report.",
                "D": "A penetration-test report evaluates exploitable technical weaknesses, not controls over "
                     "financial reporting.",
            },
            "exam_pattern": "Service-provider controls affecting clients' financial reporting (ICFR) = SOC 1; "
                            "Trust Services Criteria = SOC 2; public summary = SOC 3.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - SOC report types",
                       "AICPA SSAE 18 (SOC 1 - ICFR)"],
    },

    # ----- cissp_test_outputs ----------------------------------------------
    {
        "id": "cissp-assess-r2-007", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_test_outputs", "difficulty": 2, "type": "mcq",
        "stem": "An assessment flags a vulnerability that cannot be remediated before a deadline because "
                "the fix requires a vendor upgrade scheduled next quarter. What is the MOST appropriate way "
                "to handle the finding in the interim?",
        "options": [
            {"id": "A", "text": "Quietly close the finding and move on"},
            {"id": "B", "text": "Document a formal, time-bound risk acceptance approved by the appropriate risk owner, apply any compensating controls, and track it to remediation"},
            {"id": "C", "text": "Delete the asset from the inventory so it is no longer scanned"},
            {"id": "D", "text": "Grant everyone administrator rights to speed the eventual fix"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "When a finding cannot be fixed immediately, the risk should be formally and temporarily "
                       "accepted by the accountable risk owner, documented (ideally with compensating controls "
                       "and an expiry/review date), and tracked until remediated - preserving accountability "
                       "and visibility.",
            "distractors": {
                "A": "Silently closing a real finding hides risk and removes accountability.",
                "C": "Removing the asset from inventory to avoid scanning conceals risk rather than managing it.",
                "D": "Granting broad admin rights violates least privilege and increases risk without addressing "
                     "the finding.",
            },
            "exam_pattern": "Findings that can't be fixed now -> formal, time-bound risk acceptance by the risk "
                            "owner (with compensating controls) and tracked, never silently closed.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Remediation and risk acceptance of findings"],
    },
    {
        "id": "cissp-assess-r2-008", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_test_outputs", "difficulty": 3, "type": "mcq",
        "stem": "Management wants a metric that shows how WELL the vulnerability-remediation process is "
                "meeting its targets - for example, the percentage of critical vulnerabilities patched "
                "within the agreed SLA. Which metric type is this?",
        "options": [
            {"id": "A", "text": "A key risk indicator (KRI)"},
            {"id": "B", "text": "A single loss expectancy (SLE)"},
            {"id": "C", "text": "An annualized rate of occurrence (ARO)"},
            {"id": "D", "text": "A key performance indicator (KPI)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A KPI measures how effectively a process is achieving its objectives (e.g., percent of "
                       "critical vulnerabilities patched within SLA); it is a performance/effectiveness metric, "
                       "in contrast to a KRI, which signals rising risk exposure.",
            "distractors": {
                "A": "A KRI is a forward-looking early-warning signal of increasing risk, not a measure of "
                     "process performance against targets.",
                "B": "SLE is the monetary loss expected from a single event, a risk-analysis figure, not a "
                     "process metric.",
                "C": "ARO is the expected annual frequency of a loss event, also a risk-analysis input, not a "
                     "performance measure.",
            },
            "exam_pattern": "KPI = how well a process performs against targets; KRI = early warning of rising "
                            "risk (pair them, don't confuse them).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Security metrics (KPI vs KRI)"],
    },

    # ===================================================================
    # Domain 7 - Security Operations (cissp_sec_ops)
    # ===================================================================
    # ----- cissp_investigations --------------------------------------------
    {
        "id": "cissp-ops-r2-001", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_investigations", "difficulty": 3, "type": "mcq",
        "stem": "During an investigation, a manager searches an employee's personal, password-protected "
                "cloud account WITHOUT authorization and finds incriminating files. A court is MOST likely "
                "to EXCLUDE this evidence because it fails which requirement for admissibility?",
        "options": [
            {"id": "A", "text": "It is not relevant to the case"},
            {"id": "B", "text": "It is not material to the matter"},
            {"id": "C", "text": "It was not obtained in a lawful, authorized manner (admissible evidence must be legally permissible, in addition to relevant and reliable)"},
            {"id": "D", "text": "It was not compressed before being stored"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "To be admissible, evidence must generally be relevant, reliable (competent/authentic), "
                       "AND lawfully obtained. Evidence gathered through an unauthorized search of a protected "
                       "personal account can be excluded because it was not legally/properly obtained - "
                       "regardless of how incriminating it is.",
            "distractors": {
                "A": "The files are clearly relevant (they bear on the case); relevance is not the failing here.",
                "B": "Materiality is not the problem; the content is pertinent - the issue is how it was collected.",
                "D": "Compression has nothing to do with the legal admissibility of evidence.",
            },
            "exam_pattern": "Admissible evidence must be relevant, reliable, AND legally/properly obtained; "
                            "unlawfully obtained evidence can be excluded no matter how damning.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Evidence admissibility"],
    },
    {
        "id": "cissp-ops-r2-002", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_investigations", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: When litigation is anticipated, an organization issues a ________ (two "
                "words) that suspends routine deletion so potentially relevant electronically stored "
                "information is preserved for eDiscovery.",
        "correct": ["legal hold", "litigation hold"],
        "explanation": {
            "correct": "A legal (litigation) hold suspends normal retention/destruction so that relevant "
                       "electronically stored information (ESI) is preserved for discovery; failing to issue "
                       "one can lead to spoliation sanctions.",
            "exam_pattern": "Suspend deletion to preserve relevant ESI for litigation = legal/litigation hold "
                            "(part of the eDiscovery process).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - eDiscovery and legal hold"],
    },

    # ----- cissp_logging_monitoring ----------------------------------------
    {
        "id": "cissp-ops-r2-003", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_logging_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A SOC is overwhelmed by repetitive alert triage. The team wants to automatically enrich "
                "alerts, execute predefined response playbooks, and orchestrate actions across their tools "
                "(firewall, EDR, ticketing) with minimal analyst effort. Which capability provides this?",
        "options": [
            {"id": "A", "text": "A single endpoint antivirus scanner"},
            {"id": "B", "text": "Security orchestration, automation, and response (SOAR)"},
            {"id": "C", "text": "An uninterruptible power supply (UPS)"},
            {"id": "D", "text": "A CRL distribution point"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SOAR integrates security tools and executes automated, repeatable playbooks to enrich, "
                       "triage, and respond to alerts across the environment, reducing manual workload and "
                       "speeding consistent response.",
            "distractors": {
                "A": "A single antivirus scanner detects malware on endpoints; it does not orchestrate "
                     "cross-tool response workflows.",
                "C": "A UPS provides backup power; it is unrelated to alert automation.",
                "D": "A CRL distribution point serves certificate-revocation data; it has nothing to do with "
                     "SOC automation.",
            },
            "exam_pattern": "Automated, orchestrated playbook-driven response across security tools = SOAR "
                            "(complements the SIEM).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Security orchestration and automation (SOAR)"],
    },
    {
        "id": "cissp-ops-r2-004", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_logging_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "Rather than waiting for alerts, analysts proactively form hypotheses (for example, 'an "
                "attacker is abusing legitimate admin tools to move laterally') and search telemetry for "
                "supporting evidence, operating on an assumption that a breach may already exist. What is "
                "this activity?",
        "options": [
            {"id": "A", "text": "Signature-based antivirus scanning"},
            {"id": "B", "text": "Automated patch deployment"},
            {"id": "C", "text": "A business impact analysis (BIA)"},
            {"id": "D", "text": "Threat hunting"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Threat hunting is a proactive, hypothesis-driven search through telemetry for signs of "
                       "undetected compromise, operating on an 'assume breach' mindset rather than waiting for "
                       "automated alerts to fire.",
            "distractors": {
                "A": "Signature-based antivirus reacts to known patterns; it is not proactive, hypothesis-driven investigation.",
                "B": "Automated patch deployment remediates vulnerabilities; it does not hunt for active intrusions.",
                "C": "A BIA assesses the impact of disruptions to business functions; it is a continuity "
                     "activity, not active intrusion hunting.",
            },
            "exam_pattern": "Proactive, hypothesis-driven, assume-breach search of telemetry = threat hunting "
                            "(vs reactive alerting).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Threat hunting"],
    },

    # ----- cissp_incident_management ---------------------------------------
    {
        "id": "cissp-ops-r2-005", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 2, "type": "mcq",
        "stem": "A monitoring tool records thousands of routine 'events' every day. Which statement "
                "CORRECTLY distinguishes a security INCIDENT from an event?",
        "options": [
            {"id": "A", "text": "An incident is an event (or series of events) that actually or potentially harms, or violates the security policy protecting, an organization's assets"},
            {"id": "B", "text": "An incident is any observable occurrence, while an event always involves confirmed data loss"},
            {"id": "C", "text": "An incident and an event are identical, interchangeable terms"},
            {"id": "D", "text": "An incident exists only after regulators have been formally notified"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An event is any observable occurrence; an incident is an event (or set of events) that "
                       "negatively affects or threatens the confidentiality, integrity, or availability of "
                       "assets, or violates policy. (A breach specifically involves confirmed unauthorized "
                       "disclosure/loss of protected data.)",
            "distractors": {
                "B": "This reverses the terms: an event is the observable occurrence, and confirmed data loss "
                     "describes a breach, not the definition of an event.",
                "C": "Events and incidents are not identical; every incident is an event, but most events are "
                     "benign and are not incidents.",
                "D": "Incident status depends on harm or a policy violation, not on whether regulators have "
                     "been notified.",
            },
            "exam_pattern": "Event = any observable occurrence; incident = event that harms/threatens CIA or "
                            "violates policy; breach = confirmed unauthorized disclosure/loss of protected data.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Event vs incident vs breach"],
    },
    {
        "id": "cissp-ops-r2-006", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_incident_management", "difficulty": 3, "type": "mcq",
        "stem": "After an incident is contained, the team removes the malware, deletes attacker-created "
                "accounts, closes the exploited vulnerability, and rebuilds affected systems from known-good "
                "images. In the common incident-response lifecycle, which phase is this?",
        "options": [
            {"id": "A", "text": "Preparation"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Eradication"},
            {"id": "D", "text": "Lessons learned"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Eradication removes the root cause and attacker artifacts (malware, backdoors, rogue "
                       "accounts) and closes the exploited weakness, typically producing clean systems before "
                       "the recovery phase restores normal operations.",
            "distractors": {
                "A": "Preparation establishes the plan, tools, and team BEFORE any incident occurs.",
                "B": "Containment limits the spread/damage first; the described removal of artifacts and root "
                     "cause is the subsequent eradication step.",
                "D": "Lessons learned is the final review phase after recovery, focused on improvement, not "
                     "technical cleanup.",
            },
            "exam_pattern": "Remove malware/artifacts and close the root cause after containment = eradication "
                            "(then recovery restores operations).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Incident response lifecycle (eradication)"],
    },

    # ----- cissp_dr_recovery -----------------------------------------------
    {
        "id": "cissp-ops-r2-007", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A storage team needs an array that can survive the SIMULTANEOUS failure of TWO drives (for "
                "example, a second drive failing during a lengthy rebuild). Which RAID level provides this "
                "using double distributed parity?",
        "options": [
            {"id": "A", "text": "RAID 0 (striping, no parity)"},
            {"id": "B", "text": "RAID 6 (striping with dual distributed parity)"},
            {"id": "C", "text": "RAID 1 with a single mirror"},
            {"id": "D", "text": "RAID 5 (striping with single distributed parity)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RAID 6 uses two independent distributed parity blocks, so the array can tolerate the "
                       "concurrent failure of any two drives - valuable when large-drive rebuild times raise "
                       "the chance of a second failure during recovery.",
            "distractors": {
                "A": "RAID 0 stripes with no parity; a single drive failure loses all data.",
                "C": "A single two-disk mirror (RAID 1) tolerates one disk failure; if the second (mirror) disk "
                     "fails, the data is lost.",
                "D": "RAID 5 has single distributed parity and survives only one drive failure, not two.",
            },
            "exam_pattern": "Survive TWO simultaneous drive failures with dual parity = RAID 6 (RAID 5 = one "
                            "failure; a single RAID 1 mirror = one failure).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - RAID levels and fault tolerance"],
    },
    {
        "id": "cissp-ops-r2-008", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_dr_recovery", "difficulty": 3, "type": "mcq",
        "stem": "An organization runs a full backup every Sunday and an INCREMENTAL backup each "
                "subsequent night (Monday through Saturday). A failure occurs Thursday morning. Which "
                "backups are required for a full restore, and why?",
        "options": [
            {"id": "A", "text": "Only Wednesday night's incremental, because incrementals are cumulative"},
            {"id": "B", "text": "Only Sunday's full backup"},
            {"id": "C", "text": "Sunday's full plus only Wednesday's incremental"},
            {"id": "D", "text": "Sunday's full plus EVERY incremental from Monday, Tuesday, and Wednesday, because each incremental holds only the changes since the previous backup"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An incremental backup captures only the data changed since the last backup of ANY type, "
                       "so a full restore requires the last full backup plus every incremental taken since it "
                       "(Mon, Tue, Wed). Incrementals are fast to create but slower to restore.",
            "distractors": {
                "A": "Incrementals are not cumulative; each holds only changes since the prior backup, so one "
                     "alone is insufficient (cumulative behavior describes differentials).",
                "B": "The full backup alone omits all changes made Monday through Wednesday.",
                "C": "Needing only the full plus one latest backup describes a DIFFERENTIAL scheme, not incremental.",
            },
            "exam_pattern": "Incremental restore = last full + ALL subsequent incrementals (fast backup, slow "
                            "restore); differential = last full + the single latest differential.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Backup strategies (incremental vs differential)"],
    },

    # ----- cissp_change_config_mgmt ----------------------------------------
    {
        "id": "cissp-ops-r2-009", "exam": "cissp", "domain": "cissp_sec_ops",
        "subtopic": "cissp_change_config_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "A newly released critical security patch must be deployed across production servers. "
                "Following sound operations practice, what should happen BEFORE wide deployment?",
        "options": [
            {"id": "A", "text": "Test the patch in a non-production/staging environment and deploy it through change management with a rollback plan"},
            {"id": "B", "text": "Push it to all production servers immediately with no testing, to minimize exposure time"},
            {"id": "C", "text": "Install it only on developer laptops and consider the fleet patched"},
            {"id": "D", "text": "Wait indefinitely until the next annual maintenance window"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Patch management balances urgency with stability: critical patches are tested in a "
                       "representative staging environment, scheduled through change management with a rollback "
                       "plan, then deployed - avoiding both unpatched exposure and untested-change outages.",
            "distractors": {
                "B": "Deploying untested patches fleet-wide risks mass outages; even emergency changes warrant "
                     "at least minimal testing and a rollback plan.",
                "C": "Patching only developer laptops leaves the production servers (the actual risk) exposed.",
                "D": "Delaying a critical patch for up to a year leaves a known, exploitable exposure open far too long.",
            },
            "exam_pattern": "Patch management = test in staging -> change-managed deployment with rollback; "
                            "balance exposure vs stability (use the emergency path for truly urgent fixes).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 7 - Patch and change management"],
    },

    # ===================================================================
    # Domain 8 - Software Development Security (cissp_software_dev)
    # ===================================================================
    # ----- cissp_sdlc_security ---------------------------------------------
    {
        "id": "cissp-sw-r2-001", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 2, "type": "mcq",
        "stem": "A developer wants to debug a problem by editing code directly on the live production "
                "server and testing with real customer data. Why should an organization PROHIBIT this under "
                "secure SDLC practice?",
        "options": [
            {"id": "A", "text": "Because production servers are faster, which makes testing there unfair"},
            {"id": "B", "text": "Because development, testing, and production must be separated - changes are built and validated in lower environments and promoted through change control, and real customer data should not be exposed in dev/test"},
            {"id": "C", "text": "Because developers should never fix bugs"},
            {"id": "D", "text": "Because it would reduce the code-coverage metric"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Secure SDLC requires separating development, test, and production environments: changes "
                       "are built and validated in lower environments and promoted through change control, "
                       "which protects production stability and prevents exposing real sensitive data in dev/test.",
            "distractors": {
                "A": "Relative server speed is irrelevant; the issue is environment separation and change "
                     "control, not fairness.",
                "C": "Developers do fix bugs - but through controlled promotion across environments, not by "
                     "editing live production directly.",
                "D": "The concern is production integrity and data protection, not a coverage metric.",
            },
            "exam_pattern": "Keep dev/test/prod separate; promote changes via change control; never debug on "
                            "live production with real sensitive data.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Separation of development/test/production"],
    },
    {
        "id": "cissp-sw-r2-002", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 3, "type": "mcq",
        "stem": "A company licenses critical business software in COMPILED form from a small vendor and "
                "worries it could be stranded if the vendor goes bankrupt and can no longer maintain the "
                "product. Which arrangement BEST mitigates this risk?",
        "options": [
            {"id": "A", "text": "A software escrow agreement, in which a trusted third party holds the source code and releases it to the licensee under defined conditions (e.g., vendor failure)"},
            {"id": "B", "text": "Buying additional user licenses for the software"},
            {"id": "C", "text": "Disabling automatic updates on the software"},
            {"id": "D", "text": "Requiring the vendor's staff to use longer passwords"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A software escrow agreement places the source code (and often build instructions) with "
                       "a neutral third party that releases it to the licensee if agreed trigger conditions "
                       "occur (such as vendor bankruptcy), letting the licensee maintain the software it depends on.",
            "distractors": {
                "B": "Additional licenses do not provide access to source code or protect against the vendor's "
                     "failure to maintain the product.",
                "C": "Disabling updates does not address the vendor going out of business or the need to "
                     "maintain the code.",
                "D": "Vendor password hygiene is unrelated to continuity of source-code maintenance.",
            },
            "exam_pattern": "Protect against vendor failure for critical software = software escrow (a third "
                            "party holds source and releases it on defined triggers).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Software acquisition and escrow"],
    },

    # ----- cissp_secure_coding ---------------------------------------------
    {
        "id": "cissp-sw-r2-003", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "A web app returns ANY user's invoice if the attacker simply changes the numeric invoice ID "
                "in the URL, because the server never checks that the invoice belongs to the logged-in user. "
                "This is an instance of the OWASP Top 10's long-standing #1 category. What is the flaw, and "
                "the correct fix?",
        "options": [
            {"id": "A", "text": "Security misconfiguration; fix it by hiding/obscuring the URL"},
            {"id": "B", "text": "A cryptographic failure; fix it by hashing the invoice ID"},
            {"id": "C", "text": "Broken access control (an insecure direct object reference); fix it by enforcing server-side authorization that verifies the requester may access each specific object"},
            {"id": "D", "text": "Denial of service; fix it by rate limiting"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Returning another user's object by changing an identifier is broken access control "
                       "(here an insecure direct object reference). The fix is server-side authorization that "
                       "verifies, on every request, that the authenticated user is permitted to access the "
                       "specific object - never relying on the client to enforce it.",
            "distractors": {
                "A": "This is an authorization flaw, not a general misconfiguration; hiding or obscuring the "
                     "URL (security by obscurity) does not enforce access control.",
                "B": "No cryptographic weakness is involved; hashing the ID still fails if the server never "
                     "checks ownership.",
                "D": "The issue is unauthorized data access, not availability; rate limiting does not prevent "
                     "reading others' records.",
            },
            "exam_pattern": "Changing an ID to reach others' data = broken access control / IDOR (OWASP A01); "
                            "fix with server-side, per-object authorization checks.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Access control in applications",
                       "OWASP Top 10 (A01 Broken Access Control)"],
    },
    {
        "id": "cissp-sw-r2-004", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "A code review finds a database password and a cloud API key hard-coded in the application "
                "source, which is stored in a shared Git repository. What is the BEST remediation?",
        "options": [
            {"id": "A", "text": "Add a comment warning others not to copy the credentials"},
            {"id": "B", "text": "Rename the variables so the secrets are less obvious"},
            {"id": "C", "text": "Base64-encode the secrets in the source to 'hide' them"},
            {"id": "D", "text": "Remove the secrets from source, rotate the exposed credentials, and load them at runtime from a secrets manager/vault (keeping them out of version control)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Hard-coded secrets in source (especially in a shared repo) must be removed and the "
                       "exposed credentials rotated/revoked, with secrets injected at runtime from a dedicated "
                       "secrets manager/vault and excluded from version control (e.g., via ignore rules and "
                       "secret scanning).",
            "distractors": {
                "A": "A warning comment leaves the secret exposed to anyone with repo access and removes none of the risk.",
                "B": "Renaming variables does not remove the secret from the code or its history.",
                "C": "Base64 is encoding, not encryption; it is trivially reversible and still exposes the secret.",
            },
            "exam_pattern": "Never hard-code secrets; remove + rotate exposed credentials and load them at "
                            "runtime from a secrets manager/vault, out of version control.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Secrets management"],
    },

    # ----- cissp_software_vulns --------------------------------------------
    {
        "id": "cissp-sw-r2-005", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 3, "type": "mcq",
        "stem": "An attacker supplies a URL to a web app's 'fetch image from link' feature and makes the "
                "SERVER request http://169.254.169.254/ (the cloud metadata endpoint), retrieving instance "
                "credentials. Which vulnerability class is this, and a key mitigation?",
        "options": [
            {"id": "A", "text": "Cross-site scripting; mitigated by output encoding"},
            {"id": "B", "text": "Server-side request forgery (SSRF); mitigated by validating/allow-listing outbound destinations and blocking access to internal and metadata addresses"},
            {"id": "C", "text": "Buffer overflow; mitigated by ASLR"},
            {"id": "D", "text": "Clickjacking; mitigated by frame-busting headers"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Coercing the server into making attacker-controlled requests (here to the internal "
                       "cloud metadata service) is server-side request forgery. Mitigations include "
                       "allow-listing permitted outbound destinations, blocking requests to "
                       "internal/link-local/metadata addresses, and restricting the fetcher's network egress.",
            "distractors": {
                "A": "XSS executes scripts in a victim's browser; here the SERVER is tricked into making "
                     "requests, which is SSRF, not XSS.",
                "C": "A buffer overflow overwrites memory; this attack abuses request handling, not memory bounds.",
                "D": "Clickjacking tricks users into clicking hidden UI; it does not make the server issue "
                     "internal requests.",
            },
            "exam_pattern": "Server tricked into making attacker-chosen requests (e.g., to cloud metadata) = "
                            "SSRF; allow-list destinations and block internal/metadata addresses.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Server-side request forgery"],
    },
    {
        "id": "cissp-sw-r2-006", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 3, "type": "mcq",
        "stem": "An application accepts serialized objects from clients and reconstructs them without "
                "validation, allowing a crafted object to trigger arbitrary code execution during "
                "reconstruction. Which vulnerability is this, and the BEST defense?",
        "options": [
            {"id": "A", "text": "Insecure deserialization; avoid deserializing untrusted data, and where unavoidable enforce integrity checks (signing), strict allow-listed types, and sandboxing"},
            {"id": "B", "text": "SQL injection; use parameterized queries"},
            {"id": "C", "text": "Weak password storage; use bcrypt"},
            {"id": "D", "text": "Open redirect; validate redirect targets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reconstructing attacker-supplied serialized objects without validation is insecure "
                       "deserialization, which can lead to remote code execution or object injection. The best "
                       "defense is not to deserialize untrusted data; where necessary, use integrity checks "
                       "(signing), strict allow-listed types, and isolation/sandboxing.",
            "distractors": {
                "B": "SQL injection manipulates database queries via input; this flaw is in object "
                     "reconstruction, not query building.",
                "C": "Weak password storage concerns credential hashing, not object deserialization.",
                "D": "An open redirect sends users to attacker URLs; it does not execute code via deserialized objects.",
            },
            "exam_pattern": "Reconstructing untrusted serialized objects -> insecure deserialization (RCE "
                            "risk); avoid it, or sign/verify, allow-list types, and sandbox.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Insecure deserialization"],
    },

    # ----- cissp_devsecops -------------------------------------------------
    {
        "id": "cissp-sw-r2-007", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_devsecops", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A formal, often machine-readable inventory of all the components and "
                "their versions that make up an application - used to quickly determine exposure when a "
                "component vulnerability is disclosed - is a software ________ of materials (SBOM).",
        "correct": ["bill"],
        "explanation": {
            "correct": "A software bill of materials (SBOM) inventories an application's components and their "
                       "versions, enabling rapid identification of where a newly disclosed vulnerable component "
                       "is used (software supply-chain visibility).",
            "exam_pattern": "SBOM = component/version inventory for software supply-chain impact analysis.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Software bill of materials (SBOM)"],
    },
    {
        "id": "cissp-sw-r2-008", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_devsecops", "difficulty": 3, "type": "mcq",
        "stem": "A team deploys applications as container images built from public base images. To avoid "
                "shipping known-vulnerable OS packages and libraries, WHERE should automated image "
                "vulnerability scanning be integrated?",
        "options": [
            {"id": "A", "text": "Only after a breach is reported in production"},
            {"id": "B", "text": "Nowhere - container images cannot be scanned for vulnerabilities"},
            {"id": "C", "text": "Only manually, once per year"},
            {"id": "D", "text": "Into the CI/CD pipeline and the image registry, so images are scanned on build and flagged or blocked before and during deployment"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Container image scanning should run automatically in the CI/CD pipeline and at the "
                       "registry, checking base images and dependencies for known vulnerabilities on every "
                       "build so vulnerable images are flagged or blocked before they reach production "
                       "(shift-left for containers).",
            "distractors": {
                "A": "Waiting until a breach is reactive and defeats the purpose of preventing vulnerable deployments.",
                "B": "Container images can and should be scanned (their layers, packages, and libraries) with standard tools.",
                "C": "An annual manual scan cannot keep pace with frequent container builds and newly disclosed vulnerabilities.",
            },
            "exam_pattern": "Scan container images automatically in CI/CD and the registry (on build), blocking "
                            "vulnerable images before deployment.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Container image scanning in CI/CD"],
    },
]

