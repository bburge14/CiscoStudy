"""(ISC)2 SSCP pool - Domain 3: Risk Identification, Monitoring, and Analysis.

Original, objective-aligned practice items for the four Risk subtopics tracked
in CertLab:
  * sscp_risk_management   - risk fundamentals (threat/vulnerability/risk),
                             risk treatment (accept/avoid/transfer/mitigate),
                             quantitative risk (SLE/ARO/ALE), residual risk.
  * sscp_monitoring_analysis - vulnerability vs threat, continuous monitoring,
                             baselines/anomalies, false positive vs false
                             negative.
  * sscp_security_assessment - vulnerability assessment vs penetration testing
                             and interpreting results.
  * sscp_siem_logging      - SIEM aggregation/correlation, event vs incident,
                             log integrity/centralization, time synchronization.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_risk_management =============================================
    {
        "id": "sscp-risk-001", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 1, "type": "mcq",
        "stem": "Which expression best captures how information security risk arises?",
        "options": [
            {"id": "A", "text": "Risk is the intersection of a threat and a vulnerability (its likelihood and impact)"},
            {"id": "B", "text": "Risk equals the number of installed security controls"},
            {"id": "C", "text": "Risk equals system uptime multiplied by backup frequency"},
            {"id": "D", "text": "Risk equals the count of applied patches minus the threats"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Risk exists where a threat can exploit a vulnerability; it is assessed by the "
                       "likelihood of that happening and the impact if it does. No vulnerability (or no "
                       "threat) means little to no risk.",
            "distractors": {
                "B": "More controls generally reduce risk; a control count is not the definition of risk.",
                "C": "Uptime and backups relate to availability/recovery, not the definition of risk.",
                "D": "Patch counts influence vulnerability but do not define risk by subtraction.",
            },
            "exam_pattern": "Risk = Threat acting on a Vulnerability, measured by Likelihood x Impact.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Risk fundamentals"],
    },
    {
        "id": "sscp-risk-002", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After assessing a residual breach risk it cannot fully eliminate, a company purchases "
                "cyber-insurance to offset the potential financial loss. Which risk treatment is this?",
        "options": [
            {"id": "A", "text": "Risk avoidance"},
            {"id": "B", "text": "Risk acceptance"},
            {"id": "C", "text": "Risk transference"},
            {"id": "D", "text": "Risk mitigation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Buying insurance shifts the financial consequence of the risk to a third party, "
                       "which is risk transference (sharing).",
            "distractors": {
                "A": "Avoidance eliminates the risk by not performing the risky activity at all.",
                "B": "Acceptance means knowingly retaining the risk without further action.",
                "D": "Mitigation reduces likelihood or impact by applying controls, not by shifting the loss to an insurer.",
            },
            "exam_pattern": "Insurance / outsourcing the consequence = transference; controls = mitigation; do nothing = acceptance.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Risk treatment options"],
    },
    {
        "id": "sscp-risk-003", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 3, "type": "mcq",
        "stem": "An asset valued at $100,000 would lose 25% of its value in a single incident (exposure "
                "factor 0.25), and such incidents are expected about twice per year. What is the "
                "Annualized Loss Expectancy (ALE)?",
        "options": [
            {"id": "A", "text": "$25,000"},
            {"id": "B", "text": "$50,000"},
            {"id": "C", "text": "$100,000"},
            {"id": "D", "text": "$12,500"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SLE = Asset Value x Exposure Factor = $100,000 x 0.25 = $25,000. ALE = SLE x ARO "
                       "= $25,000 x 2 = $50,000.",
            "distractors": {
                "A": "$25,000 is the Single Loss Expectancy (SLE), not the annualized figure.",
                "C": "$100,000 is the full asset value, not the expected annual loss.",
                "D": "$12,500 would halve the SLE; it does not match the given exposure factor and ARO.",
            },
            "exam_pattern": "SLE = AV x EF; ALE = SLE x ARO. Watch the ARO when it is above 1.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Quantitative risk analysis (SLE/ARO/ALE)"],
    },
    {
        "id": "sscp-risk-004", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_risk_management", "difficulty": 2, "type": "mcq",
        "stem": "A team applies controls to reduce a risk but knows some exposure still remains. The "
                "risk left over after controls are in place is called:",
        "options": [
            {"id": "A", "text": "Inherent risk"},
            {"id": "B", "text": "Total risk"},
            {"id": "C", "text": "Residual risk"},
            {"id": "D", "text": "Transferred risk"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Residual risk is what remains after controls (safeguards) have been applied; "
                       "management must decide whether to accept it.",
            "distractors": {
                "A": "Inherent risk is the risk before any controls are applied.",
                "B": "Total risk is the full exposure without controls, essentially the inherent risk.",
                "D": "Transferred risk is the portion shifted to a third party (e.g., insurance), not what simply remains.",
            },
            "exam_pattern": "Before controls = inherent/total; after controls = residual; what management accepts.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Residual risk"],
    },

    # ===== sscp_monitoring_analysis =========================================
    {
        "id": "sscp-risk-005", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 1, "type": "mcq",
        "stem": "A critical server is missing a vendor security patch for a known flaw. In risk "
                "terminology, that missing patch is best classified as a:",
        "options": [
            {"id": "A", "text": "Threat"},
            {"id": "B", "text": "Vulnerability"},
            {"id": "C", "text": "Risk"},
            {"id": "D", "text": "Exploit"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A vulnerability is a weakness that can be exploited - here, an unpatched, "
                       "exploitable flaw in the system.",
            "distractors": {
                "A": "A threat is the potential source/actor (e.g., an attacker or malware) that could exploit the weakness.",
                "C": "Risk is the combination of the threat exploiting the vulnerability and its impact, not the weakness itself.",
                "D": "An exploit is the actual tool/technique used to take advantage of the vulnerability.",
            },
            "exam_pattern": "Weakness = vulnerability; actor/event = threat; code that abuses it = exploit.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Threats vs vulnerabilities"],
    },
    {
        "id": "sscp-risk-006", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Instead of relying on a once-a-year audit, an organization deploys tooling that "
                "continuously collects and evaluates control effectiveness and configuration state in "
                "near-real time. This approach is known as:",
        "options": [
            {"id": "A", "text": "Continuous monitoring"},
            {"id": "B", "text": "Penetration testing"},
            {"id": "C", "text": "A tabletop exercise"},
            {"id": "D", "text": "A business impact analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Continuous monitoring provides ongoing, near-real-time awareness of security "
                       "posture and control effectiveness, replacing reliance on infrequent point-in-"
                       "time checks.",
            "distractors": {
                "B": "A penetration test is a point-in-time, active assessment, not ongoing monitoring.",
                "C": "A tabletop exercise is a discussion-based drill of response plans, not continuous data collection.",
                "D": "A BIA analyzes impact of disruptions for continuity planning, not real-time control monitoring.",
            },
            "exam_pattern": "Ongoing, near-real-time posture visibility = continuous monitoring.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Continuous monitoring"],
    },
    {
        "id": "sscp-risk-007", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "mcq",
        "stem": "An intrusion detection system fails to raise any alert while an actual intrusion is "
                "taking place. How is this outcome classified?",
        "options": [
            {"id": "A", "text": "False positive"},
            {"id": "B", "text": "True positive"},
            {"id": "C", "text": "True negative"},
            {"id": "D", "text": "False negative"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A false negative is a real malicious event that the system fails to detect - "
                       "the most dangerous error type because the threat goes unnoticed.",
            "distractors": {
                "A": "A false positive is an alert on benign activity (no real attack).",
                "B": "A true positive is a correct alert on a genuine attack.",
                "C": "A true negative is correctly staying silent when nothing malicious is happening.",
            },
            "exam_pattern": "Missed real attack = false negative (most dangerous); benign alarm = false positive (noise).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - False positives and false negatives"],
    },
    {
        "id": "sscp-risk-008", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_monitoring_analysis", "difficulty": 2, "type": "fill",
        "stem": "An anomaly-based detection system flags activity that deviates from an established "
                "____ of normal behavior that was learned during a training period. Provide the "
                "one-word term for this reference profile of normal activity.",
        "correct": ["baseline"],
        "explanation": {
            "correct": "Anomaly (behavior-based) detection compares observed activity against a learned "
                       "baseline of normal behavior and alerts on significant deviations - good at "
                       "catching novel attacks but prone to false positives if the baseline is poor.",
            "distractors": {},
            "exam_pattern": "Anomaly detection = deviation from a learned baseline; signature detection = match to known patterns.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Anomaly vs signature detection"],
    },

    # ===== sscp_security_assessment =========================================
    {
        "id": "sscp-risk-009", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 2, "type": "mcq",
        "stem": "Which security assessment actively attempts to EXPLOIT discovered weaknesses in order "
                "to demonstrate real-world impact, rather than only identifying and listing them?",
        "options": [
            {"id": "A", "text": "Penetration testing"},
            {"id": "B", "text": "Vulnerability scanning"},
            {"id": "C", "text": "Log review"},
            {"id": "D", "text": "Patch management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A penetration test goes beyond detection and attempts to exploit findings "
                       "(within an agreed scope) to prove impact and chainable risk.",
            "distractors": {
                "B": "A vulnerability scan identifies and catalogs potential weaknesses but does not exploit them.",
                "C": "Log review analyzes recorded events; it is not an active exploitation test.",
                "D": "Patch management remediates vulnerabilities; it is not an assessment technique.",
            },
            "exam_pattern": "Scan = find/catalog; pen test = exploit to prove impact.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Security assessment and testing"],
    },
    {
        "id": "sscp-risk-010", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability scan reports a critical flaw, but on manual verification the flaw does "
                "not actually exist on the target. What is this scan result called?",
        "options": [
            {"id": "A", "text": "False negative"},
            {"id": "B", "text": "True positive"},
            {"id": "C", "text": "False positive"},
            {"id": "D", "text": "Zero-day finding"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A false positive is a reported finding that is not actually present; validating "
                       "scan output is essential to avoid wasting effort on phantom issues.",
            "distractors": {
                "A": "A false negative is a real flaw the scanner MISSED, the opposite of this case.",
                "B": "A true positive would be a reported flaw that genuinely exists.",
                "D": "A zero-day is a previously unknown vulnerability, not a mistaken scan report.",
            },
            "exam_pattern": "Reported-but-not-real = false positive; real-but-missed = false negative.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Interpreting assessment results"],
    },
    {
        "id": "sscp-risk-011", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_security_assessment", "difficulty": 3, "type": "mcq",
        "stem": "Which statement BEST distinguishes a vulnerability assessment from a penetration test?",
        "options": [
            {"id": "A", "text": "A vulnerability assessment requires fully exploiting every finding it discovers"},
            {"id": "B", "text": "They are identical in scope and methodology"},
            {"id": "C", "text": "A penetration test only reviews documentation and never touches systems"},
            {"id": "D", "text": "A vulnerability assessment identifies and catalogs weaknesses, while a penetration test exploits them to demonstrate impact"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A vulnerability assessment enumerates and prioritizes weaknesses; a penetration "
                       "test goes further by exploiting selected findings to show tangible, real-world "
                       "impact.",
            "distractors": {
                "A": "Exploiting findings is the pen test's role; a vulnerability assessment stops at identification.",
                "B": "They differ precisely in depth: identification versus exploitation.",
                "C": "A penetration test actively interacts with systems; it is not a documentation-only review.",
            },
            "exam_pattern": "Assessment = breadth of identification; pen test = depth via exploitation.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Vulnerability assessment vs penetration testing"],
    },

    # ===== sscp_siem_logging ================================================
    {
        "id": "sscp-risk-012", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 1, "type": "mcq",
        "stem": "Which technology aggregates, normalizes, and correlates log and event data from many "
                "sources to detect and alert on security incidents in near-real time?",
        "options": [
            {"id": "A", "text": "SIEM (Security Information and Event Management)"},
            {"id": "B", "text": "DLP (Data Loss Prevention)"},
            {"id": "C", "text": "VPN (Virtual Private Network)"},
            {"id": "D", "text": "DNS (Domain Name System)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM centralizes logs, normalizes different formats, and correlates events "
                       "across sources to surface and alert on potential incidents.",
            "distractors": {
                "B": "DLP focuses on preventing unauthorized data exfiltration, not broad log correlation.",
                "C": "A VPN provides an encrypted tunnel; it is not a log-analysis platform.",
                "D": "DNS resolves names to addresses; it is unrelated to event correlation.",
            },
            "exam_pattern": "Central aggregation + normalization + correlation + alerting = SIEM.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - SIEM and log management"],
    },
    {
        "id": "sscp-risk-013", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 2, "type": "mcq",
        "stem": "A single failed login attempt is recorded in a system log. In security operations "
                "terminology, this individual observable occurrence is best called a(n):",
        "options": [
            {"id": "A", "text": "Incident"},
            {"id": "B", "text": "Event"},
            {"id": "C", "text": "Breach"},
            {"id": "D", "text": "Disaster"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An event is any observable occurrence in a system or network. Only events that "
                       "actually harm or violate security policy are escalated to incidents.",
            "distractors": {
                "A": "An incident is an event (or series) that violates policy or causes harm - more than a single routine log entry.",
                "C": "A breach specifically involves confirmed unauthorized access/disclosure of data.",
                "D": "A disaster is a large-scale disruptive event handled by continuity/DR processes.",
            },
            "exam_pattern": "Every incident is an event; not every event is an incident (incident = harm/policy violation).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Event vs incident"],
    },
    {
        "id": "sscp-risk-014", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 2, "type": "mcq",
        "stem": "Why should hosts forward their logs to a centralized, access-restricted log server "
                "rather than retaining them only locally?",
        "options": [
            {"id": "A", "text": "To reduce the total volume of log data generated"},
            {"id": "B", "text": "To eliminate the need for clock synchronization"},
            {"id": "C", "text": "To preserve log integrity and availability, so an attacker who compromises a host cannot simply delete or alter the evidence"},
            {"id": "D", "text": "To make the logs easier to ignore during investigations"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Centralized, write-restricted logging protects the integrity and availability "
                       "of evidence: even if an endpoint is compromised, the forwarded copies remain "
                       "intact for detection and investigation.",
            "distractors": {
                "A": "Centralization does not reduce how much log data is produced.",
                "B": "Centralized logging actually increases the need for synchronized time across sources.",
                "D": "The goal is reliable analysis, not making logs easier to ignore.",
            },
            "exam_pattern": "Centralize logs off-host to protect integrity/availability against tampering.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Log management and integrity"],
    },
    {
        "id": "sscp-risk-015", "exam": "sscp", "domain": "sscp_risk",
        "subtopic": "sscp_siem_logging", "difficulty": 3, "type": "multi",
        "stem": "An analyst correlating events across several systems in a SIEM finds that timestamps "
                "do not line up, making the attack timeline unreliable. Which TWO practices most "
                "directly support accurate cross-system event correlation? (Choose two.)",
        "options": [
            {"id": "A", "text": "Synchronize all system clocks using a common NTP time source"},
            {"id": "B", "text": "Record timestamps in a consistent time standard such as UTC"},
            {"id": "C", "text": "Disable logging on the noisiest systems to simplify analysis"},
            {"id": "D", "text": "Keep each system's logs only on that system"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Synchronizing clocks with NTP and recording times in a consistent standard "
                       "(e.g., UTC) let events from different systems be ordered into a reliable, "
                       "accurate timeline for correlation.",
            "distractors": {
                "C": "Disabling logging removes evidence and creates blind spots; it does not aid correlation.",
                "D": "Keeping logs only locally hinders correlation and leaves them exposed to tampering on a compromised host.",
            },
            "exam_pattern": "Accurate correlation needs synchronized clocks (NTP) + a consistent time standard (UTC).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 3 - Time synchronization and correlation"],
    },
]
