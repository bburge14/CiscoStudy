# Security Metrics, KPIs & Stakeholder Communication

Leadership doesn't read packet captures — it reads *numbers* and *risk*. This
lesson covers the two skills that make a SOC's work legible to the rest of the
organization: the metrics and KPIs that measure how well security is performing,
and the art of tailoring each message to the audience that receives it. Say the
same thing to a board and to a server engineer and you'll fail both.

## The metrics that run a SOC

Several key metrics are "mean time to *something*," and they are easy to confuse.
Anchor each to the exact interval it measures.

| Metric | Measures the average time from… | …to |
|--------|-------------------------------|-----|
| **MTTD** (mean time to detect) | the compromise occurring | the team detecting it |
| **MTTR** (mean time to respond) | an alert firing | the first containment action |
| **MTTC** (mean time to contain) | detecting the incident | successfully stopping its spread |
| **Mean time to remediate** | a vulnerability's discovery | its fix being fully deployed |

> The trap is the word "respond." **MTTR as "respond"** is alert-to-first-action;
> **mean time to remediate** (sometimes also abbreviated MTTR) is the *vulnerability*
> metric, discovery-to-fix-deployed. Read the definition in the stem, not just the
> acronym.

Beyond the clock-based metrics:

- **Scan coverage** — the percentage of the asset inventory actually included in
  vulnerability scans. The CISO who suspects some assets are never scanned is
  asking for scan coverage.
- **Vulnerability aging against remediation SLAs** — grouping open vulnerabilities
  into 0–30, 31–60, and 60+ day buckets and flagging criticals past their
  remediation deadline. Aging shows whether you're keeping your remediation
  promises.
- **False-positive rate** — how many alerts turn out benign. A high rate means
  detections need tuning and analysts are drowning; tracking it drives
  improvement and fights alert fatigue.
- **Dwell time** — how long an attacker went undetected inside the environment
  before discovery. It is closely tied to MTTD, and driving it down is a headline
  goal of any detection program.
- **Alert volume** — the raw number of alerts over time. Paired with the
  false-positive rate, it tells you whether analysts are overwhelmed and whether
  tuning is working.

### Targets: SLA vs. SLO

Metrics need goals attached. Distinguish the two:

> An **SLA (service-level agreement)** is an external, often contractual
> commitment. An **SLO (service-level objective)** is an *internal* target you set
> to drive improvement — for example, "95% of critical vulnerabilities remediated
> within seven days."

When the stem describes a self-imposed internal goal, it's an **SLO**; when it's a
promise to a customer or partner, it's an **SLA**.

## Communicating to each audience

The same finding must be *retold* for each reader. The guiding question is always
"what does this person need to decide or do?"

### Executives and the board

> For a board or senior leadership, **summarize business risk, impact, and
> prioritized recommendations in concise, non-technical terms.** No CVE numbers,
> no packet details.

This is the **executive summary / management report** — a trend-focused view for
**strategic** decisions, not task-level remediation. When you have 1,000 findings
and need funding, **frame them by business risk, highlighting exploitable critical
issues on high-value assets first**. Leaders fund *risk reduction*, not raw counts.

### Technical teams

Hand the *same* findings to the server engineering team and the emphasis flips:
**specific affected hosts, CVE details, and exact remediation or patch steps.**
Engineers need precision to act, not a risk narrative.

### Collaborate with the team that owns the root cause

Fixing a recurring problem means talking to whoever controls its source:

- SQL injection that keeps recurring in a web app → collaborate with the
  **software development team** to fix the root cause in code.
- Publicly exposed cloud storage buckets created by infrastructure-as-code →
  collaborate with the **cloud/DevOps engineering team** that owns the IaC
  templates and pipeline.

### Who decides, and who audits

- **The business/system owner decides** on risk trade-offs that affect the
  business — for instance, whether to take a revenue-generating system offline to
  remediate a critical flaw. Security *advises* and legal is *consulted*; security
  does not unilaterally halt sales.
- For an **external auditor** asking for proof of timely remediation, provide
  **reports mapping remediation evidence — scan results, timelines, documented
  exceptions — to the relevant compliance requirement.**

## Why this closes the loop

Metrics and communication are how the SOC earns its budget and its mandate. Good
metrics prove whether detection and remediation are improving; good communication
turns those metrics into decisions — funding, staffing, accepted risks — made by
the people with the authority to make them. The analyst who can *measure* the work
and *explain* it to the right audience is the one whose program keeps growing.

## Exam focus

- **MTTD** = compromise → detection; **MTTR (respond)** = alert → first
  containment; **MTTC** = detection → spread stopped; **mean time to remediate** =
  vuln discovery → fix deployed. Read the definition, not just the acronym.
- **Scan coverage** = % of inventory scanned; **vulnerability aging** = open-vuln
  age buckets vs. SLA; **false-positive rate** drives detection tuning.
- **SLA** = external/contractual; **SLO** = internal improvement target (e.g., 95%
  of criticals in 7 days).
- Executives/board: **business risk, impact, prioritized recommendations, non-technical**
  (executive summary; strategic/trend view). Technical teams: **affected hosts,
  CVEs, exact patch steps.**
- Fix root causes with the owning team: **dev** for recurring SQLi, **cloud/DevOps**
  for IaC-created exposures.
- The **business/system owner** decides on taking systems offline (security
  advises); give **auditors** evidence mapped to the **compliance requirement**.
