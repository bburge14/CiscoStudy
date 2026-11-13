# Analytics Rules & Threat Detection

Raw logs do not detect anything on their own. **Analytics rules** are what turn
ingested data into **alerts** and group those alerts into **incidents** for the
SOC. Microsoft Sentinel offers several rule types for different jobs, and the
workhorse — the **scheduled** rule — is built from a KQL query you control. This
lesson covers the rule types and how to build and tune a scheduled rule.

## The analytics rule types

| Rule type | How it detects | Use it for |
|-----------|----------------|------------|
| **Scheduled** | Runs a **KQL query** on a schedule | The flexible default — your custom detections |
| **Near-real-time (NRT)** | Runs about **every minute** (limited query shape) | Time-critical detections needing minimal delay |
| **Microsoft security** | Auto-creates Sentinel incidents from **another Microsoft product's alerts** (Defender XDR, Defender for Cloud) | Promoting product alerts into Sentinel incidents |
| **Fusion** | **ML** correlation of low-fidelity signals across sources into **multistage attack** incidents | Catching attack chains humans would miss (on by default) |
| **Anomaly** | Built-in **ML** behavioral models | Flagging unusual behavior with tunable sensitivity |
| **Threat intelligence** | Matches **TI indicators** against your logs | IOC-based detection |

> **Fusion** and **Anomaly** rules are **machine-learning** based. Fusion
> correlates weak signals into multistage-attack incidents; anomaly rules flag
> deviations and are **customizable** — duplicate a template, tune its thresholds,
> run it in **flighting** (test) mode, then promote it to **production**.

## Building a scheduled rule

Most SC-200 analytics questions are really about the **scheduled** rule, so know
its anatomy.

**1. The query.** A KQL statement that returns the suspicious rows. For example, a
rule to catch repeated failed sign-ins followed by a success (a possible
brute-force that worked):

```kql
SigninLogs
| where ResultType == 0 or ResultType == 50126   // success or bad password
| summarize Failures = countif(ResultType == 50126),
            Successes = countif(ResultType == 0),
            FirstSeen = min(TimeGenerated),
            LastSeen  = max(TimeGenerated)
          by UserPrincipalName, IPAddress
| where Failures >= 10 and Successes >= 1
```

**2. Query scheduling.** How often the rule **runs** (frequency) and how far back it
looks each run (**lookback period**). These usually match — run every hour, look
back one hour — so events are evaluated exactly once.

**3. Alert threshold.** Generate an alert only when the query returns more than N
results, to avoid firing on a single benign hit.

**4. Entity mapping.** Map query columns to **entities** — `UserPrincipalName` →
*Account*, `IPAddress` → *IP*, a device name → *Host*. Entity mapping is what makes
alerts investigable: it drives the incident graph, entity pages, and correlation.

**5. MITRE ATT&CK mapping.** Tag the rule with the tactic/technique it detects
(e.g., *Credential Access*), so coverage is visible and incidents carry context.

**6. Incident settings.** Decide whether alerts **create incidents** and whether to
**group** related alerts (by entity, within a time window) into one incident
instead of many.

**7. Automated response.** Attach **automation rules** or **playbooks** that run
when the rule produces an alert/incident — the bridge to SOAR in the next lesson.

## Which rule type should I use?

A quick decision guide:

- Need **custom logic** over your data? → **Scheduled** rule (the default).
- Need the **fastest possible** detection and your logic fits the constraints? →
  **NRT** (runs about every minute; limited to a single table, no joins across the
  pipeline the way scheduled rules allow).
- Want **Defender XDR or Defender for Cloud alerts to become Sentinel incidents**?
  → **Microsoft security** rule.
- Want Microsoft's ML to **catch multistage attacks** you didn't write a rule for?
  → leave **Fusion** enabled.
- Want behavioral outliers with a dial you can **tune**? → **Anomaly** rule.

> Don't reinvent what Microsoft ships. Keep **Fusion** on, enable the **Microsoft
> security** rules for your products, and spend your custom-rule effort on
> **scheduled** detections that encode knowledge specific to your environment.

## Templates, tuning, and UEBA

Don't start from a blank query. The **Content hub** and the Analytics **rule
templates** gallery provide ready detections you enable and adjust. When a rule is
too noisy, tune the query, raise the threshold, add **alert suppression** (pause
re-firing for a set period after an alert), or refine entity grouping rather than
disabling it outright.

> **User and Entity Behavior Analytics (UEBA)** builds behavioral baselines for
> users and hosts and writes anomalies to the **`BehaviorAnalytics`** table. You
> can reference that enrichment in scheduled queries — for example, scoring a
> sign-in higher when UEBA marks the action as uncommon for that user.

Finally, validate before you trust a rule. When authoring a scheduled rule you can
preview the query's recent results and the simulated alert count, so you can see
whether the threshold is sensible and the entity mapping resolves correctly *before*
the rule goes live and starts filling the queue.

## Exam focus

- Know the rule types and when each applies: **Scheduled** (custom KQL),
  **NRT** (~1-minute, near-real-time), **Microsoft security** (promote product
  alerts to incidents), **Fusion** (ML multistage attacks, on by default),
  **Anomaly** (tunable ML), **Threat intelligence** (IOC matching).
- A **scheduled rule** has a **query**, **scheduling** (frequency + **lookback**),
  **threshold**, **entity mapping**, **MITRE ATT&CK** mapping, **incident/grouping**
  settings, and **automated response**.
- **Entity mapping** is essential — it powers investigation, entity pages, and
  correlation.
- Tune noise with **thresholds**, **alert suppression**, and **grouping**; start
  from **rule templates** in the Content hub.
- **Fusion/Anomaly = ML**; anomaly rules run in **flighting** then **production**.
  **UEBA** writes to **`BehaviorAnalytics`** and enriches detections.
