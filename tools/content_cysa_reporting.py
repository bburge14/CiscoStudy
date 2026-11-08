"""CySA+ CS0-003 item pool — Domain 4.0 Reporting and Communication (17%).

Original, objective-aligned practice items for the CySA+ (CS0-003) track,
covering all four Domain-4 subtopics:

  * rc_vuln_reporting   — vulnerability-management reporting: report contents
                          (affected hosts, risk score, recommendations), compliance
                          drivers, action plans (patch / configuration / compensating
                          control / awareness), and inhibitors to remediation
                          (MOU, SLA, business process interruption, degrading
                          functionality, legacy / proprietary systems).
  * rc_incident_reporting — incident reporting & escalation: stakeholder
                          identification, legal / regulatory breach notification,
                          incident declaration & escalation, out-of-band
                          communications, and lessons-learned reporting.
  * rc_metrics          — metrics & KPIs: MTTD / MTTR (respond vs remediate),
                          scan coverage, vulnerability aging/trends, and SLOs vs SLAs.
  * rc_stakeholder_comm — communicating to the right audience: technical vs
                          executive tailoring, risk prioritization for leadership,
                          cross-team collaboration, and report purpose/audience.

Every item is an original scenario — never a real exam question. Facts are kept
defensible and current for CS0-003 (process, audience, and metrics knowledge).

build_content.py auto-discovers content_<exam>_*.py pools, shuffles each item's
A/B/C/D order seeded by its id, and re-keys the answer, so the keys authored here
(correct = ["A"], etc.) are not positionally biased in the delivered bank.
"""

QUESTIONS = [
    # ===== rc_vuln_reporting =================================================
    {
        "id": "cysa-rc-001", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability scan returns 600 unsorted findings. Which element should the "
                "report add so remediation teams know which findings to fix first?",
        "options": [
            {"id": "A", "text": "A risk score that weights each finding's severity by asset criticality and exposure"},
            {"id": "B", "text": "The scanner software's internal build number"},
            {"id": "C", "text": "The total elapsed run time of the scan job"},
            {"id": "D", "text": "An alphabetical list of every hostname scanned"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Prioritization is the core value of a vulnerability report. A risk score that "
                       "combines technical severity (e.g., CVSS) with business context — asset criticality "
                       "and exposure — tells teams what to remediate first.",
            "distractors": {
                "B": "The scanner build number is metadata; it does nothing to rank findings by business risk.",
                "C": "Scan duration is an operational detail with no bearing on which vulnerability is most dangerous.",
                "D": "Sorting hosts alphabetically ignores severity and impact, so it cannot drive prioritization.",
            },
            "exam_pattern": "'Which to fix first' = prioritize by risk score (severity + asset criticality), not raw counts or metadata.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Vulnerability management reporting", "Risk score / prioritization"],
    },
    {
        "id": "cysa-rc-002", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "multi",
        "stem": "A manager asks what every actionable finding in a vulnerability-management report "
                "must contain. Which TWO items are essential? (Choose two.)",
        "options": [
            {"id": "A", "text": "The specific affected hosts or assets"},
            {"id": "B", "text": "A recommended remediation or mitigation for the finding"},
            {"id": "C", "text": "The license tier of the scanning product"},
            {"id": "D", "text": "The desk phone number of the SOC manager"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "An actionable finding must identify the affected hosts/assets (what to fix and where) "
                       "and provide a remediation recommendation (how to fix it). Together with a risk score, "
                       "these let teams act and let leadership prioritize.",
            "distractors": {
                "C": "The scanner's license tier is procurement trivia, not part of an actionable finding.",
                "D": "A contact phone number is not a required report element and does not help remediate anything.",
            },
            "exam_pattern": "Actionable finding = affected host + risk + recommended fix. Pick the content that lets someone DO something.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Vulnerability management reporting", "Affected hosts / recommendations"],
    },
    {
        "id": "cysa-rc-003", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A revenue-critical application runs on an end-of-life OS the vendor no longer patches, "
                "and it cannot be replaced this year. Which remediation action plan best reduces the "
                "risk while keeping it running?",
        "options": [
            {"id": "A", "text": "Deploy a compensating control such as network segmentation plus virtual patching around the host"},
            {"id": "B", "text": "Apply the vendor's latest security patch to the operating system"},
            {"id": "C", "text": "Deliver phishing-awareness training to the application's users"},
            {"id": "D", "text": "Accept the risk and document it with no further action"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When a flaw cannot be directly remediated (no patch, cannot replace), a compensating "
                       "control — isolating the host via segmentation and shielding it with virtual "
                       "patching/WAF/IPS — reduces exposure while the system keeps running.",
            "distractors": {
                "B": "The OS is end-of-life, so no vendor patch exists to apply.",
                "C": "Awareness training addresses user behavior, not an unpatchable OS vulnerability.",
                "D": "Accepting the risk with no control leaves a critical system fully exposed; a compensating control is expected.",
            },
            "exam_pattern": "Can't patch / can't replace but must keep running → compensating control (segmentation, virtual patching).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Action plans", "Compensating control"],
    },
    {
        "id": "cysa-rc-004", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A scan finds the same weak setting — legacy TLS 1.0 enabled — on 200 servers all built "
                "from one gold image. Which action plan best corrects the root cause across the fleet?",
        "options": [
            {"id": "A", "text": "Update the hardened configuration baseline and image, then push it via configuration management"},
            {"id": "B", "text": "Open a separate emergency patch ticket for each of the 200 servers"},
            {"id": "C", "text": "Place a compensating firewall rule in front of all 200 servers"},
            {"id": "D", "text": "Add the finding to next year's risk-acceptance register"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The flaw is a misconfiguration, not missing code, and it stems from a shared baseline. "
                       "Correcting the hardening baseline/gold image and deploying it through configuration "
                       "management fixes every host and stops new builds from reintroducing it.",
            "distractors": {
                "B": "This is a configuration issue, not a software defect; patching per host is the wrong tool and ignores the image that keeps recreating it.",
                "C": "A firewall rule is a compensating control that treats the symptom; the setting itself should be corrected at the source.",
                "D": "Accepting the risk ignores an easily fixed, systemic misconfiguration.",
            },
            "exam_pattern": "Same insecure SETTING across many hosts from one image → configuration management / baseline change, not patching.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Action plans", "Configuration management"],
    },
    {
        "id": "cysa-rc-005", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 1, "type": "mcq",
        "stem": "A phishing simulation shows many employees still submit credentials to fake login "
                "pages. Which remediation action plan most directly targets this weakness?",
        "options": [
            {"id": "A", "text": "Security awareness, training, and education for employees"},
            {"id": "B", "text": "A patch to the email server's operating system"},
            {"id": "C", "text": "A new compensating control on the core router"},
            {"id": "D", "text": "A change to the vulnerability scanner's schedule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The vulnerability is human behavior — users falling for phishing — so awareness, "
                       "training, and education is the action plan that directly reduces susceptibility.",
            "distractors": {
                "B": "Patching the mail server OS does not change whether users click and submit credentials.",
                "C": "A router control does not address the human decision to enter credentials on a fake page.",
                "D": "Rescheduling scans has no effect on user susceptibility to phishing.",
            },
            "exam_pattern": "Human / behavioral weakness → awareness, training & education as the remediation.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Action plans", "Awareness, training, and education"],
    },
    {
        "id": "cysa-rc-006", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 2, "type": "mcq",
        "stem": "A critical patch requires a reboot, but a signed customer contract guarantees 99.99% "
                "uptime and forbids unscheduled outages. Which inhibitor to remediation does this represent?",
        "options": [
            {"id": "A", "text": "Service-level agreement (SLA)"},
            {"id": "B", "text": "Memorandum of understanding (MOU)"},
            {"id": "C", "text": "Proprietary system"},
            {"id": "D", "text": "Degrading functionality"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A contractual uptime guarantee with defined service levels is a service-level "
                       "agreement; the SLA constrains when the system may be taken down, inhibiting timely remediation.",
            "distractors": {
                "B": "An MOU is a broader, often non-binding statement of intent between parties, not the uptime guarantee described.",
                "C": "Nothing indicates the system is vendor-controlled or closed; the blocker is the contract, not the technology.",
                "D": "Degrading functionality is when the fix itself breaks a feature; here the patch works, but a contract blocks the downtime.",
            },
            "exam_pattern": "Contractual uptime/service guarantee blocking a maintenance window = SLA inhibitor.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Inhibitors to remediation", "SLA"],
    },
    {
        "id": "cysa-rc-007", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A server is jointly operated with a partner agency under a memorandum of understanding "
                "that bars either side from altering it without mutual sign-off, so the security team "
                "cannot patch it alone. Which inhibitor is this?",
        "options": [
            {"id": "A", "text": "Memorandum of understanding (MOU)"},
            {"id": "B", "text": "Service-level agreement (SLA)"},
            {"id": "C", "text": "Business process interruption"},
            {"id": "D", "text": "Legacy system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A memorandum of understanding is a mutual agreement defining how parties cooperate. "
                       "Here it forbids unilateral changes, so the MOU itself inhibits remediation until the partner agrees.",
            "distractors": {
                "B": "An SLA sets measurable service levels and penalties; this blocker is a cooperation agreement about who may make changes.",
                "C": "Business process interruption is about downtime disrupting operations; the obstacle here is needing the partner's consent, not an outage.",
                "D": "Nothing says the system is old or unsupported; the constraint is the inter-organizational agreement.",
            },
            "exam_pattern": "Cross-organization agreement that blocks unilateral change = MOU inhibitor (vs SLA's service metrics).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Inhibitors to remediation", "MOU"],
    },
    {
        "id": "cysa-rc-008", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_vuln_reporting", "difficulty": 3, "type": "mcq",
        "stem": "Lab testing shows the only available firmware update for a production robotic controller "
                "disables a motion feature the assembly line requires. Which inhibitor to remediation "
                "best describes this?",
        "options": [
            {"id": "A", "text": "Degrading functionality"},
            {"id": "B", "text": "Service-level agreement (SLA)"},
            {"id": "C", "text": "Memorandum of understanding (MOU)"},
            {"id": "D", "text": "Business process interruption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The fix exists and can be installed, but it removes a needed capability — the update "
                       "degrades functionality, which is why the team hesitates to apply it.",
            "distractors": {
                "B": "No contractual service level is described; the issue is the patch breaking a feature.",
                "C": "No inter-party agreement is involved here.",
                "D": "Business process interruption is the outage/downtime needed to apply a fix; here the problem is the lost feature after the fix, not the window.",
            },
            "exam_pattern": "Patch available but it BREAKS a needed feature = degrading functionality (distinct from downtime = business process interruption).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Inhibitors to remediation", "Degrading functionality"],
    },

    # ===== rc_incident_reporting =============================================
    {
        "id": "cysa-rc-009", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "mcq",
        "stem": "During a confirmed breach of customer personal data, which stakeholder should the "
                "incident team engage first to determine the organization's mandatory notification obligations?",
        "options": [
            {"id": "A", "text": "Legal / privacy counsel"},
            {"id": "B", "text": "The public relations team"},
            {"id": "C", "text": "The external news media"},
            {"id": "D", "text": "The company's advertising agency"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Legal/privacy counsel interprets contractual and regulatory breach-notification "
                       "requirements (who must be told, and by when) and guides what is disclosed, so they are engaged first.",
            "distractors": {
                "B": "PR crafts external messaging, but what and when you may disclose is a legal determination that must come first.",
                "C": "The media are not a stakeholder you consult to learn your obligations; premature contact can harm the response.",
                "D": "An advertising agency has no role in determining breach-notification obligations.",
            },
            "exam_pattern": "Breach notification 'what are we required to report' → Legal first; PR handles messaging afterward.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Stakeholder identification; legal/regulatory reporting", "Breach notification"],
    },
    {
        "id": "cysa-rc-010", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "multi",
        "stem": "While responding to a suspected compromise of corporate email and Active Directory, the "
                "team moves coordination to a separate encrypted phone bridge. Which TWO reasons justify "
                "out-of-band communications? (Choose two.)",
        "options": [
            {"id": "A", "text": "The attacker may be reading internal email and could monitor the response"},
            {"id": "B", "text": "The primary communication systems may be untrusted or unavailable during the incident"},
            {"id": "C", "text": "Out-of-band channels are generally cheaper than corporate email"},
            {"id": "D", "text": "It satisfies the vulnerability-scanning SLA"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Out-of-band comms keep response coordination confidential if the attacker is watching "
                       "normal channels, and they stay usable when the compromised/affected systems (email, AD) "
                       "are untrusted or down.",
            "distractors": {
                "C": "Cost is irrelevant; out-of-band comms are about confidentiality and availability, not savings.",
                "D": "Scanning SLAs have nothing to do with incident-response communication channels.",
            },
            "exam_pattern": "Out-of-band comms = assume the primary channel is compromised/unavailable → protect confidentiality and keep coordinating.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Communications during an incident", "Out-of-band communication"],
    },
    {
        "id": "cysa-rc-011", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "mcq",
        "stem": "An analyst confirms active exfiltration of regulated data well past the plan's severity "
                "threshold. According to incident-response best practice, what should happen next?",
        "options": [
            {"id": "A", "text": "Formally declare an incident and escalate per the incident-response plan"},
            {"id": "B", "text": "Keep investigating quietly until absolutely certain before telling anyone"},
            {"id": "C", "text": "Immediately reimage the affected host to stop the bleeding"},
            {"id": "D", "text": "Email the entire company to warn everyone at once"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Confirmed activity beyond the defined threshold triggers formal incident declaration "
                       "and escalation, activating the right stakeholders, authority, and resources under the IR plan.",
            "distractors": {
                "B": "Delaying escalation until 'certain' wastes critical response time; the threshold has already been crossed.",
                "C": "Reimaging destroys evidence and preempts containment decisions that should follow declaration/escalation.",
                "D": "Mass-emailing everyone is not controlled escalation and can tip off an attacker or cause panic.",
            },
            "exam_pattern": "Threshold crossed / confirmed → declare + escalate per plan (not investigate silently, not wipe, not mass-notify).",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Incident declaration and escalation", "Escalation"],
    },
    {
        "id": "cysa-rc-012", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 3, "type": "mcq",
        "stem": "A company subject to the EU GDPR confirms a breach of EU residents' personal data. Within "
                "what timeframe must it notify the relevant supervisory authority?",
        "options": [
            {"id": "A", "text": "Without undue delay and no later than 72 hours after becoming aware"},
            {"id": "B", "text": "Within 1 hour of detecting any anomaly"},
            {"id": "C", "text": "Within 30 calendar days of closing the incident"},
            {"id": "D", "text": "Only at the next annual compliance audit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GDPR Article 33 requires the controller to notify the supervisory authority without "
                       "undue delay and, where feasible, within 72 hours of becoming aware of a personal-data breach.",
            "distractors": {
                "B": "No GDPR rule sets a one-hour deadline, and reporting every anomaly immediately is impractical.",
                "C": "Thirty days after closure far exceeds the 72-hour obligation.",
                "D": "Waiting for an annual audit violates the mandatory, time-bound notification requirement.",
            },
            "exam_pattern": "GDPR personal-data breach → notify supervisory authority within 72 hours. Know common regulatory clocks.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Legal / regulatory reporting", "Breach notification (GDPR 72-hour)"],
    },
    {
        "id": "cysa-rc-013", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "mcq",
        "stem": "Mid-incident, an engineer wants to post technical breach details to their personal social "
                "media 'for transparency.' What is the correct handling under the communications plan?",
        "options": [
            {"id": "A", "text": "Route all external and media communications through PR and legal; staff must not disclose independently"},
            {"id": "B", "text": "Encourage the post so customers hear the news quickly"},
            {"id": "C", "text": "Ignore it, since personal accounts are outside company control"},
            {"id": "D", "text": "Have a SOC analyst brief reporters directly instead"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "External messaging during an incident must be controlled and consistent: PR and legal "
                       "own customer/media communications. Ad-hoc disclosures can be inaccurate, create legal "
                       "exposure, and undermine the response.",
            "distractors": {
                "B": "Encouraging an unvetted personal post risks leaking inaccurate or legally sensitive details.",
                "C": "Ignoring it abdicates control; staff must be directed not to disclose independently.",
                "D": "SOC analysts are not the designated spokespeople; media briefings go through PR/legal.",
            },
            "exam_pattern": "All external / media comms flow through PR + legal; no ad-hoc staff disclosure.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Communications (public relations, customer/media)", "Controlled external communication"],
    },
    {
        "id": "cysa-rc-014", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_incident_reporting", "difficulty": 2, "type": "mcq",
        "stem": "After a resolved incident, the team holds a post-incident review. What is the primary "
                "purpose of the lessons-learned report it produces?",
        "options": [
            {"id": "A", "text": "Identify what worked and what didn't so processes and controls can be improved to prevent recurrence"},
            {"id": "B", "text": "Assign personal blame to the analysts who missed the intrusion"},
            {"id": "C", "text": "Provide the attacker with feedback on their techniques"},
            {"id": "D", "text": "Close the incident ticket as fast as possible with no analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The lessons-learned report is a blameless, improvement-focused analysis: it captures "
                       "what went well and poorly across detection, response, and communication to strengthen future readiness.",
            "distractors": {
                "B": "Lessons learned are deliberately blameless; assigning personal blame discourages honest reporting.",
                "C": "The report is internal; it has nothing to do with informing the attacker.",
                "D": "Rushing to close with no analysis defeats the entire purpose of the review.",
            },
            "exam_pattern": "Lessons learned = blameless process improvement to prevent recurrence, not blame or ticket-closing.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Lessons learned", "Post-incident improvement"],
    },

    # ===== rc_metrics ========================================================
    {
        "id": "cysa-rc-015", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 1, "type": "mcq",
        "stem": "A SOC wants a single metric for the average time between a compromise occurring and the "
                "team actually detecting it. Which KPI is this?",
        "options": [
            {"id": "A", "text": "Mean time to detect (MTTD)"},
            {"id": "B", "text": "Mean time to respond (MTTR)"},
            {"id": "C", "text": "Mean time to remediate"},
            {"id": "D", "text": "Scan coverage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mean time to detect measures how long threats dwell before discovery; lowering MTTD "
                       "means faster detection and less attacker dwell time.",
            "distractors": {
                "B": "Mean time to respond starts after detection — it measures how fast you act, not how fast you notice.",
                "C": "Mean time to remediate measures how long until the issue is fully fixed, which comes after detection.",
                "D": "Scan coverage measures how much of the environment is scanned, not detection speed.",
            },
            "exam_pattern": "'How long until we notice' = MTTD (detection). Respond and remediate come after detection.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Metrics and KPIs", "Mean time to detect"],
    },
    {
        "id": "cysa-rc-016", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 3, "type": "mcq",
        "stem": "Leadership wants to track the average time from an alert firing to the SOC taking its "
                "first containment action. Which metric captures exactly this?",
        "options": [
            {"id": "A", "text": "Mean time to respond"},
            {"id": "B", "text": "Mean time to detect"},
            {"id": "C", "text": "Mean time to remediate"},
            {"id": "D", "text": "Mean time between failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mean time to respond measures the gap between detection/alert and the start of response "
                       "actions (e.g., containment); it gauges how quickly the team mobilizes once something is found.",
            "distractors": {
                "B": "Mean time to detect ends when the alert fires; this metric begins there.",
                "C": "Mean time to remediate runs until the threat is fully eradicated/fixed, not just to the first containment action.",
                "D": "MTBF is a reliability/availability measure for systems, not an incident-response timing metric.",
            },
            "exam_pattern": "Alert → first response action = mean time to respond; full fix/eradication = mean time to remediate.",
        },
        "references": ["CySA+ CS0-003 Obj 4.2 — Metrics and KPIs", "Mean time to respond vs remediate"],
    },
    {
        "id": "cysa-rc-017", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A vulnerability-management team reports the average number of days from a vulnerability's "
                "discovery to its fix being fully deployed. Which metric is this?",
        "options": [
            {"id": "A", "text": "Mean time to remediate"},
            {"id": "B", "text": "Mean time to detect"},
            {"id": "C", "text": "Scan coverage"},
            {"id": "D", "text": "Alert volume"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mean time to remediate measures the elapsed time from identifying a vulnerability to "
                       "completing its fix; it reflects how efficiently the program closes exposures.",
            "distractors": {
                "B": "Mean time to detect measures time until discovery, which precedes remediation.",
                "C": "Scan coverage measures breadth of scanning, not remediation speed.",
                "D": "Alert volume counts alerts generated, unrelated to remediation duration.",
            },
            "exam_pattern": "Discovery → fully fixed = mean time to remediate (vulnerability-management speed).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Metrics and KPIs", "Mean time to remediate"],
    },
    {
        "id": "cysa-rc-018", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 2, "type": "mcq",
        "stem": "A CISO suspects some assets are never scanned and asks for a metric showing the "
                "percentage of the asset inventory actually included in vulnerability scans. Which metric is this?",
        "options": [
            {"id": "A", "text": "Scan coverage"},
            {"id": "B", "text": "Mean time to remediate"},
            {"id": "C", "text": "False-positive rate"},
            {"id": "D", "text": "CVSS base score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scan coverage is the proportion of known assets actually scanned; low coverage reveals "
                       "blind spots where vulnerabilities go undiscovered, making it a key program-health metric.",
            "distractors": {
                "B": "Mean time to remediate measures remediation speed, not how much of the estate is scanned.",
                "C": "False-positive rate measures scan accuracy, not breadth of coverage.",
                "D": "A CVSS base score rates one vulnerability's severity, not inventory coverage.",
            },
            "exam_pattern": "'What % of assets are we actually scanning' = scan coverage (exposes blind spots).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Metrics and KPIs", "Scan coverage"],
    },
    {
        "id": "cysa-rc-019", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 3, "type": "mcq",
        "stem": "A monthly report groups open vulnerabilities into 0-30, 31-60, and 60+ day buckets and "
                "flags criticals past their remediation deadline. Which metric is being tracked?",
        "options": [
            {"id": "A", "text": "Vulnerability aging against remediation SLAs"},
            {"id": "B", "text": "Mean time to detect"},
            {"id": "C", "text": "Scan coverage"},
            {"id": "D", "text": "Total asset inventory count"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bucketing open findings by how long they have been unremediated — and comparing them to "
                       "remediation deadlines — is vulnerability aging; growing older buckets of criticals signal remediation isn't keeping pace with SLAs.",
            "distractors": {
                "B": "Mean time to detect concerns detection speed, not how long known vulnerabilities stay open.",
                "C": "Scan coverage measures how much is scanned, not the age of open findings.",
                "D": "An asset count is inventory size, unrelated to how long vulnerabilities remain unfixed.",
            },
            "exam_pattern": "Open vulns bucketed by age vs deadline = vulnerability aging (are we remediating fast enough?).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Metrics and KPIs", "Vulnerability trends / aging"],
    },
    {
        "id": "cysa-rc-020", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_metrics", "difficulty": 3, "type": "mcq",
        "stem": "To drive improvement, a security team sets an internal target that 95% of critical "
                "vulnerabilities be remediated within seven days. What does this internal, measurable target represent?",
        "options": [
            {"id": "A", "text": "A service-level objective (SLO)"},
            {"id": "B", "text": "A service-level agreement (SLA)"},
            {"id": "C", "text": "A memorandum of understanding (MOU)"},
            {"id": "D", "text": "A compensating control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A specific, measurable internal goal used to steer the program is a service-level "
                       "objective; SLOs are the targets an organization holds itself to, often underpinning (but distinct from) contractual SLAs.",
            "distractors": {
                "B": "An SLA is a contractual commitment to an external party with defined consequences; this is an internally set target, not a contract.",
                "C": "An MOU is a cooperative agreement between parties, not a performance target.",
                "D": "A compensating control mitigates a specific risk; it is not a performance metric or target.",
            },
            "exam_pattern": "Internal measurable target to drive the program = SLO; external contract with penalties = SLA.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Metrics and KPIs", "SLOs vs SLAs"],
    },

    # ===== rc_stakeholder_comm ===============================================
    {
        "id": "cysa-rc-021", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "An analyst must brief the board of directors on the quarter's vulnerability posture. "
                "How should the report be tailored for this audience?",
        "options": [
            {"id": "A", "text": "Summarize business risk, impact, and prioritized recommendations in concise, non-technical terms"},
            {"id": "B", "text": "List every CVE identifier with its full CVSS vector string"},
            {"id": "C", "text": "Attach the raw scanner output for all hosts"},
            {"id": "D", "text": "Include packet captures proving each finding"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Executives need business-relevant risk, impact, and clear prioritized recommendations "
                       "to make funding and strategy decisions; technical minutiae obscure the message for a non-technical audience.",
            "distractors": {
                "B": "Full CVE/CVSS vector lists are for technical remediation teams, not a board briefing.",
                "C": "Raw scanner output overwhelms executives and buries the decisions they must make.",
                "D": "Packet captures are deep technical evidence irrelevant to strategic leadership decisions.",
            },
            "exam_pattern": "Executive / board audience → business risk + impact + prioritized asks, not CVEs or raw data.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1/4.2 — Stakeholder communication", "Tailoring reporting to executives"],
    },
    {
        "id": "cysa-rc-022", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "The same findings are being handed to the server engineering team to fix. What should "
                "this version of the report emphasize?",
        "options": [
            {"id": "A", "text": "Specific affected hosts, CVE details, and exact remediation or patch steps"},
            {"id": "B", "text": "A one-line risk narrative with no technical detail"},
            {"id": "C", "text": "Projected return on investment for the security budget"},
            {"id": "D", "text": "A board-level summary of strategic posture"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Technical implementers need actionable specifics: which hosts, which vulnerabilities "
                       "(CVEs), and the precise remediation/patch steps so they can execute the fixes.",
            "distractors": {
                "B": "A detail-free narrative leaves engineers without the information needed to remediate.",
                "C": "ROI framing is for budget-owning leadership, not the team performing fixes.",
                "D": "A strategic board summary lacks the host- and patch-level detail engineers require.",
            },
            "exam_pattern": "Technical / implementer audience → hosts, CVEs, exact fix steps (the opposite of the executive view).",
        },
        "references": ["CySA+ CS0-003 Obj 4.1/4.2 — Stakeholder communication", "Tailoring technical reporting"],
    },
    {
        "id": "cysa-rc-023", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "A security team has 1,000 findings but limited budget and must present to leadership for "
                "funding. How should the findings be framed to best drive decisions?",
        "options": [
            {"id": "A", "text": "Prioritize by business risk, highlighting exploitable critical issues on high-value assets first"},
            {"id": "B", "text": "Present all 1,000 findings as equally urgent"},
            {"id": "C", "text": "List findings in the order the scanner happened to report them"},
            {"id": "D", "text": "Show only the findings that are cheapest and easiest to fix"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leadership funds the biggest risk reductions; framing findings by business risk — "
                       "exploitability and impact on crown-jewel assets — lets them allocate limited resources where they matter most.",
            "distractors": {
                "B": "Declaring everything equally urgent gives leadership no basis to allocate limited funds.",
                "C": "Scanner order is arbitrary and ignores business impact.",
                "D": "Leading with only the cheap/easy fixes can leave the most dangerous risks unfunded.",
            },
            "exam_pattern": "Limited budget + leadership audience → rank by business risk / exploitability on key assets.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Stakeholder communication; prioritization", "Risk prioritization for leadership"],
    },
    {
        "id": "cysa-rc-024", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 1, "type": "mcq",
        "stem": "Vulnerability reports keep showing SQL injection recurring in a company's web "
                "application. Which team should the analyst collaborate with to fix the root cause?",
        "options": [
            {"id": "A", "text": "The software development team"},
            {"id": "B", "text": "The physical facilities team"},
            {"id": "C", "text": "The public relations team"},
            {"id": "D", "text": "The accounts-payable team"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SQL injection is a code-level flaw; collaborating with developers to add input "
                       "validation / parameterized queries and bake security into the SDLC addresses the recurring root cause.",
            "distractors": {
                "B": "Facilities manages buildings and power, not application code.",
                "C": "PR handles communications, not code remediation.",
                "D": "Accounts payable handles finances and has no role in fixing application vulnerabilities.",
            },
            "exam_pattern": "Recurring code-level flaw (e.g., SQLi) → collaborate with developers / secure SDLC.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Collaboration with internal teams", "Working with development"],
    },
    {
        "id": "cysa-rc-025", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 2, "type": "mcq",
        "stem": "Which report type is designed mainly to give senior leadership a concise, trend-focused "
                "view for strategic decisions rather than task-level remediation detail?",
        "options": [
            {"id": "A", "text": "An executive summary / management report"},
            {"id": "B", "text": "A detailed technical vulnerability report"},
            {"id": "C", "text": "A change-management ticket"},
            {"id": "D", "text": "A raw packet-capture export"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Executive/management reports distill trends, posture, and prioritized risk for "
                       "strategic decision-making; they intentionally omit the task-level detail that operational teams need.",
            "distractors": {
                "B": "A detailed technical report targets implementers who must remediate specific findings.",
                "C": "A change ticket tracks a single operational change, not strategic trends.",
                "D": "A packet capture is low-level forensic evidence, not a leadership report.",
            },
            "exam_pattern": "Match report type to audience/purpose: executive summary = trends + strategy for leadership.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1/4.2 — Purpose and audience of report types", "Executive vs technical reporting"],
    },
    {
        "id": "cysa-rc-026", "exam": "cysa", "domain": "cysa_reporting_comm",
        "subtopic": "rc_stakeholder_comm", "difficulty": 3, "type": "mcq",
        "stem": "Security recommends taking a revenue-generating system offline to remediate a critical "
                "flaw, but that will halt sales for hours. Who should ultimately decide whether to accept that downtime?",
        "options": [
            {"id": "A", "text": "The business / system owner, with security advising and legal consulted as needed"},
            {"id": "B", "text": "The security analyst, acting unilaterally"},
            {"id": "C", "text": "The vulnerability-scanning vendor"},
            {"id": "D", "text": "End users, by an informal vote"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security identifies and advises on risk, but the business/system owner owns the asset "
                       "and the trade-off, so they make (and document) the decision to accept the downtime or defer; legal is consulted when obligations are implicated.",
            "distractors": {
                "B": "Analysts advise and recommend; unilaterally forcing a business-impacting outage is outside their authority.",
                "C": "The scanning vendor reports findings; it has no authority over the organization's risk decisions.",
                "D": "Risk-acceptance decisions are a management responsibility, not an informal user vote.",
            },
            "exam_pattern": "Security advises; the business / system owner accepts the risk and makes the call on business-impacting action.",
        },
        "references": ["CySA+ CS0-003 Obj 4.1 — Collaboration with management; organizational governance", "Risk ownership and acceptance"],
    },
]
