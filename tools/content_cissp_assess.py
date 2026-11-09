"""(ISC)² CISSP pool - Domain 6: Security Assessment and Testing.

Original, CBK-aligned practice items for the four Security Assessment and
Testing subtopics:
  * cissp_assessment_strategies - vulnerability assessment vs penetration test,
                                  independence, and test-knowledge levels.
  * cissp_security_testing      - SAST vs DAST, fuzzing, and manual code review.
  * cissp_audit_logging         - SOC 1/2/3, Type I vs Type II, and log integrity.
  * cissp_test_outputs          - remediation/retest, account reviews, KRIs.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_assessment_strategies ======================================
    {
        "id": "cissp-assess-001", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 2, "type": "mcq",
        "stem": "Management asks for an assessment that not only identifies vulnerabilities but also "
                "safely demonstrates their real-world impact by actually exploiting them to gain access. "
                "Which type of assessment is this?",
        "options": [
            {"id": "A", "text": "A vulnerability assessment (scan only)"},
            {"id": "B", "text": "A penetration test"},
            {"id": "C", "text": "A configuration baseline review"},
            {"id": "D", "text": "A policy gap analysis"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A penetration test goes beyond identification and actively exploits vulnerabilities to "
                       "demonstrate the impact an attacker could achieve.",
            "distractors": {
                "A": "A vulnerability assessment identifies and reports weaknesses but does not exploit them.",
                "C": "A baseline review compares configurations against a standard, without exploitation.",
                "D": "A gap analysis compares controls/documentation against requirements, not hands-on exploitation.",
            },
            "exam_pattern": "Vulnerability assessment = find/report; penetration test = actively exploit to show impact.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Vulnerability assessment vs penetration testing"],
    },
    {
        "id": "cissp-assess-002", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 2, "type": "mcq",
        "stem": "A business partner requires objective assurance that a service provider's controls are "
                "effective. Why is an independent third-party assessment generally preferred over the "
                "provider's internal self-assessment?",
        "options": [
            {"id": "A", "text": "It is always cheaper than internal testing"},
            {"id": "B", "text": "It can skip scoping and planning"},
            {"id": "C", "text": "It provides greater objectivity and independence, reducing conflicts of interest"},
            {"id": "D", "text": "It removes the need for any management involvement"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An independent third party has no stake in the outcome, so its assessment carries "
                       "greater objectivity and credibility than a self-assessment.",
            "distractors": {
                "A": "Third-party assessments are often more expensive, not cheaper.",
                "B": "Any credible assessment still requires proper scoping and planning.",
                "D": "Management still defines scope and must act on the findings regardless of who performs the test.",
            },
            "exam_pattern": "Independence/objectivity is why third-party assessments carry more weight than self-assessment.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Internal, external, and third-party assessments"],
    },
    {
        "id": "cissp-assess-003", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 2, "type": "mcq",
        "stem": "An organization hires testers and provides them NO prior information about the "
                "environment, to simulate an external attacker who must discover everything independently. "
                "Which penetration-test approach is this?",
        "options": [
            {"id": "A", "text": "Black-box (zero-knowledge) testing"},
            {"id": "B", "text": "White-box (full-knowledge) testing"},
            {"id": "C", "text": "Gray-box (partial-knowledge) testing"},
            {"id": "D", "text": "A static source-code review"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Black-box (zero-knowledge) testing gives the tester no inside information, simulating "
                       "an outside attacker who must perform their own reconnaissance.",
            "distractors": {
                "B": "White-box testing provides full knowledge (source, architecture, credentials).",
                "C": "Gray-box testing provides partial knowledge, more than black box but less than white box.",
                "D": "A static source-code review analyzes code and is not a knowledge level of external testing.",
            },
            "exam_pattern": "No knowledge = black box (external-attacker simulation); full = white box; partial = gray box.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Penetration test knowledge levels"],
    },
    {
        "id": "cissp-assess-004", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_assessment_strategies", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Unlike a vulnerability scan, which only identifies and reports "
                "weaknesses, a ________ test goes further by actively exploiting vulnerabilities to "
                "demonstrate what an attacker could actually achieve.",
        "correct": ["penetration", "pen", "pentest", "penetration test"],
        "explanation": {
            "correct": "A penetration test actively exploits weaknesses to prove real impact, whereas a "
                       "vulnerability scan only finds and lists them.",
            "exam_pattern": "Penetration testing exploits to show impact; a vulnerability scan only identifies and reports.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Penetration testing"],
    },

    # ===== cissp_security_testing ===========================================
    {
        "id": "cissp-assess-005", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 3, "type": "mcq",
        "stem": "A development team wants to analyze an application's source code for security flaws early "
                "in the SDLC, WITHOUT executing the program. Which testing technique is this?",
        "options": [
            {"id": "A", "text": "Dynamic application security testing (DAST)"},
            {"id": "B", "text": "Fuzzing"},
            {"id": "C", "text": "A black-box penetration test"},
            {"id": "D", "text": "Static application security testing (SAST)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SAST examines source code (or binaries) without running the program, so it can be "
                       "applied early in development to catch flaws before deployment.",
            "distractors": {
                "A": "DAST tests a running application from the outside, which requires execution.",
                "B": "Fuzzing feeds malformed input to a running program, also requiring execution.",
                "C": "A black-box penetration test probes a running system and does not use the source code.",
            },
            "exam_pattern": "SAST = analyze source without executing (white box, early in SDLC); DAST = test the running app.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Static application security testing"],
    },
    {
        "id": "cissp-assess-006", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 3, "type": "mcq",
        "stem": "A security tester evaluates a deployed, running web application from the outside - "
                "sending crafted requests and observing responses - without access to its source code. "
                "Which technique is this?",
        "options": [
            {"id": "A", "text": "Dynamic application security testing (DAST)"},
            {"id": "B", "text": "Static application security testing (SAST)"},
            {"id": "C", "text": "Manual source-code review"},
            {"id": "D", "text": "Software composition analysis of the source tree"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DAST tests the running application from the outside (black box), observing behavior "
                       "without needing the source code.",
            "distractors": {
                "B": "SAST inspects source code without running the application.",
                "C": "Source-code review requires reading the code, which the tester does not have here.",
                "D": "Software composition analysis inspects source components/dependencies, not black-box runtime behavior.",
            },
            "exam_pattern": "DAST = test the running app from outside, no source needed (black box); SAST = analyze source.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Dynamic application security testing"],
    },
    {
        "id": "cissp-assess-007", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 2, "type": "mcq",
        "stem": "To find flaws such as crashes and input-handling errors, a tester automatically submits "
                "large volumes of malformed, unexpected, or random data to an application's inputs. Which "
                "technique is this?",
        "options": [
            {"id": "A", "text": "Regression testing"},
            {"id": "B", "text": "Fuzz testing (fuzzing)"},
            {"id": "C", "text": "Unit testing"},
            {"id": "D", "text": "User acceptance testing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Fuzzing supplies malformed, unexpected, or random input to an application to uncover "
                       "crashes and input-handling weaknesses.",
            "distractors": {
                "A": "Regression testing checks that changes have not broken existing functionality.",
                "C": "Unit testing verifies individual components against their expected behavior.",
                "D": "User acceptance testing confirms the software meets business requirements, not input robustness.",
            },
            "exam_pattern": "Feeding malformed/random/unexpected input to find faults = fuzzing.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Fuzz testing"],
    },
    {
        "id": "cissp-assess-008", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_security_testing", "difficulty": 2, "type": "mcq",
        "stem": "Which security-testing activity relies on human reviewers manually reading application "
                "source code to identify logic flaws and insecure coding patterns that automated tools may "
                "miss?",
        "options": [
            {"id": "A", "text": "Automated DAST scanning"},
            {"id": "B", "text": "Fuzzing"},
            {"id": "C", "text": "Manual (peer) code review"},
            {"id": "D", "text": "Load testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Manual code review has people read the source to find logic and security flaws, "
                       "complementing automated SAST tools.",
            "distractors": {
                "A": "DAST is automated and tests the running application, not manual code reading.",
                "B": "Fuzzing is automated malformed-input testing, not human review of code.",
                "D": "Load testing measures performance under load, not code-level security.",
            },
            "exam_pattern": "Humans reading source for logic/security flaws = manual code review (complements automated SAST).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Code review"],
    },

    # ===== cissp_audit_logging ==============================================
    {
        "id": "cissp-assess-009", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 3, "type": "mcq",
        "stem": "A SaaS provider must give enterprise customers a detailed, restricted-distribution "
                "report on the design and operating effectiveness of its controls for security, "
                "availability, and confidentiality. Which report is appropriate?",
        "options": [
            {"id": "A", "text": "SOC 1"},
            {"id": "B", "text": "SOC 2"},
            {"id": "C", "text": "SOC 3"},
            {"id": "D", "text": "A PCI self-assessment questionnaire (SAQ)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A SOC 2 report addresses the Trust Services Criteria (security, availability, "
                       "processing integrity, confidentiality, privacy) in detail and is restricted to "
                       "intended recipients under NDA.",
            "distractors": {
                "A": "SOC 1 covers controls relevant to financial reporting (ICFR), not security/availability.",
                "C": "SOC 3 covers the same criteria as SOC 2 but is a short, general-use public report lacking "
                     "the detail enterprise customers need.",
                "D": "A PCI SAQ is a payment-card self-assessment, not a controls-assurance attestation report.",
            },
            "exam_pattern": "SOC 1 = financial controls; SOC 2 = Trust Services Criteria (detailed, restricted); "
                            "SOC 3 = public summary.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - SOC reports"],
    },
    {
        "id": "cissp-assess-010", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 3, "type": "mcq",
        "stem": "An auditor's report evaluates not just whether controls are suitably designed, but "
                "whether they actually operated effectively throughout a 12-month period. Which report "
                "type is this?",
        "options": [
            {"id": "A", "text": "A SOC 2 Type I report"},
            {"id": "B", "text": "A design-only attestation"},
            {"id": "C", "text": "A SOC 2 Type II report"},
            {"id": "D", "text": "A point-in-time vulnerability scan"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A Type II report tests the operating effectiveness of controls over a period of time "
                       "(commonly 6-12 months), not just their design at a single moment.",
            "distractors": {
                "A": "A Type I report assesses control design at a single point in time, not effectiveness over time.",
                "B": "A design-only attestation likewise does not test operating effectiveness over a period.",
                "D": "A point-in-time scan is a technical snapshot, not a controls-effectiveness attestation.",
            },
            "exam_pattern": "Type I = design at a point in time; Type II = operating effectiveness over a period.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - SOC Type I vs Type II"],
    },
    {
        "id": "cissp-assess-011", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 2, "type": "multi",
        "stem": "To ensure audit logs can be trusted as evidence and correlated accurately across systems "
                "during an investigation, which TWO measures are MOST important? (Choose two.)",
        "options": [
            {"id": "A", "text": "Protect log integrity so entries cannot be altered"},
            {"id": "B", "text": "Synchronize system clocks using a reliable time source (such as NTP)"},
            {"id": "C", "text": "Delete logs weekly to save disk space"},
            {"id": "D", "text": "Grant all users write access to the central log server"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Trustworthy audit trails require integrity protection (so records cannot be tampered "
                       "with) and synchronized time via NTP (so events across systems can be correlated accurately).",
            "distractors": {
                "C": "Deleting logs frequently destroys the evidence trail and can violate retention requirements.",
                "D": "Broad write access undermines integrity and lets attackers tamper with the records.",
            },
            "exam_pattern": "Trustworthy logs need integrity protection and synchronized time (NTP) for accurate correlation.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Log management and audit trails"],
    },
    {
        "id": "cissp-assess-012", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_audit_logging", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The AICPA service-organization report that covers the same Trust "
                "Services Criteria as a SOC 2 but is a short, general-use report intended for public "
                "distribution (for example, posting on a website) is a SOC ___ report (give the number).",
        "correct": ["3", "three", "soc 3"],
        "explanation": {
            "correct": "A SOC 3 report is a general-use, public summary of the same subject matter as a SOC 2, "
                       "without the detailed control testing a SOC 2 contains.",
            "exam_pattern": "SOC 3 = general-use/public summary; SOC 2 = detailed and restricted distribution.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - SOC 3"],
    },

    # ===== cissp_test_outputs ===============================================
    {
        "id": "cissp-assess-013", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_test_outputs", "difficulty": 2, "type": "mcq",
        "stem": "After a penetration test reports several high-risk findings, what is the MOST appropriate "
                "next step for the security program?",
        "options": [
            {"id": "A", "text": "Archive the report and take no action until the next annual test"},
            {"id": "B", "text": "Immediately publish the full report to all employees"},
            {"id": "C", "text": "Delete the vulnerable systems without further analysis"},
            {"id": "D", "text": "Prioritize and remediate the findings by risk, then retest to confirm closure"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Test results should drive risk-based remediation; findings are prioritized, fixed, and "
                       "then retested to verify the issues are actually closed, with results reported to management.",
            "distractors": {
                "A": "Ignoring findings until the next cycle leaves known risks unaddressed.",
                "B": "Broadly publishing detailed vulnerability findings increases exposure and mishandles sensitive results.",
                "C": "Deleting systems without analysis is disruptive and skips proper risk-based remediation.",
            },
            "exam_pattern": "Test results feed prioritized, risk-based remediation and retesting, reported to management.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Remediation and reporting"],
    },
    {
        "id": "cissp-assess-014", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_test_outputs", "difficulty": 2, "type": "mcq",
        "stem": "As part of ongoing review, an organization periodically verifies that user accounts, "
                "their privileges, and especially privileged/admin accounts are still appropriate, and "
                "that terminated users retain no access. What is this activity?",
        "options": [
            {"id": "A", "text": "An account management (access) review"},
            {"id": "B", "text": "A denial-of-service test"},
            {"id": "C", "text": "A fuzzing campaign"},
            {"id": "D", "text": "A firewall rule backup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An account management (access) review periodically confirms that accounts and "
                       "entitlements remain appropriate and removes stale or terminated access.",
            "distractors": {
                "B": "A denial-of-service test assesses availability under attack, not account appropriateness.",
                "C": "Fuzzing tests input handling, not account entitlements.",
                "D": "Backing up firewall rules preserves configuration but does not review accounts.",
            },
            "exam_pattern": "Periodic account/access reviews confirm entitlements remain appropriate and remove stale access.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Account management review"],
    },
    {
        "id": "cissp-assess-015", "exam": "cissp", "domain": "cissp_assess_test",
        "subtopic": "cissp_test_outputs", "difficulty": 3, "type": "mcq",
        "stem": "Management wants a metric that acts as an early-warning signal of rising risk exposure - "
                "for example, a climbing count of unpatched critical vulnerabilities - rather than a "
                "measure of how well a process performed. Which metric type is this?",
        "options": [
            {"id": "A", "text": "Key performance indicator (KPI)"},
            {"id": "B", "text": "Key risk indicator (KRI)"},
            {"id": "C", "text": "Service-level agreement (SLA)"},
            {"id": "D", "text": "Return on investment (ROI)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A key risk indicator (KRI) is a forward-looking metric that signals increasing risk "
                       "exposure before it materializes into an incident.",
            "distractors": {
                "A": "A KPI measures how well a process performs against objectives, not future risk exposure.",
                "C": "An SLA defines agreed service levels, not a risk early-warning signal.",
                "D": "ROI measures financial return, not risk indication.",
            },
            "exam_pattern": "KRI = forward-looking early warning of risk; KPI = how well a process is performing.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 6 - Security metrics (KRI/KPI)"],
    },
]
