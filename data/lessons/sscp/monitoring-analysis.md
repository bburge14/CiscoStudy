# Security Monitoring & Analysis

Prevention buys you time; monitoring buys you knowledge. No set of controls holds
forever, so a mature security program watches continuously for the moment a
control fails or an attacker slips through — and then *analyzes* what it sees to
separate real threats from noise. This lesson is about that watching and
interpreting: continuous monitoring, the language of detection outcomes, and how
to tell a genuine signal from a false alarm.

## Why continuous monitoring

The old model — audit once a year, hope for the best in between — leaves enormous
gaps. Systems change daily, new vulnerabilities appear constantly, and attackers
don't wait for audit season.

> **Continuous monitoring** is the ongoing, often automated collection and
> evaluation of security information to maintain real-time (or near-real-time)
> awareness of an organization's security posture and control effectiveness.

Instead of a yearly snapshot, continuous monitoring gives you a live feed: Are
controls still working? Did a new vulnerability appear? Is a system drifting from
its baseline? It underpins frameworks like NIST's and is a core expectation of
modern operations. A missing vendor patch on a critical server, for instance, is
exactly the kind of thing continuous monitoring surfaces — and in risk terms,
**that missing patch is a vulnerability**, a weakness waiting for a threat.

## Baselines and anomaly detection

You can only recognize "abnormal" if you know "normal." A **baseline** is a
recorded profile of normal activity — typical traffic volumes, normal login
times, usual process behavior.

- **Anomaly-based (behavioral) detection** compares live activity to the baseline
  and flags deviations. Its strength is catching **novel/zero-day** attacks that
  have no known signature; its weakness is a higher **false-positive** rate,
  because unusual-but-legitimate activity also trips it.
- **Signature-based detection** matches activity against a database of known-bad
  patterns. It's accurate for known threats but **blind to anything new** — if
  there's no signature, there's no alert.

Good monitoring usually combines both: signatures for the known, anomaly
detection for the unknown.

## The language of detection outcomes

When any detection system (IDS, scanner, SIEM rule) makes a judgment, there are
four possible outcomes. The exam tests these constantly, so anchor them firmly:

| Outcome | Meaning | Good or bad? |
|---------|---------|--------------|
| **True positive** | Alerted, and it was a real attack | Correct |
| **True negative** | Stayed quiet, and nothing was happening | Correct |
| **False positive** | Alerted, but nothing was actually wrong | Wrong — wastes analyst time |
| **False negative** | Stayed quiet while a real attack occurred | Wrong — and the **most dangerous** |

> A **false positive** is a false alarm (the IDS cried wolf). A **false negative**
> is a *missed* intrusion — the system failed to alert while an attack was
> genuinely happening. False negatives are worse because the attack proceeds
> unnoticed.

An **IDS (Intrusion Detection System)** detects and alerts but does not block; an
**IPS (Intrusion Prevention System)** sits inline and actively blocks. Tuning
either is a balancing act: make it too sensitive and false positives bury your
analysts in noise (leading to **alert fatigue**, where real alerts get ignored);
make it too lax and false negatives let attacks through. This is the same
threshold trade-off you saw with biometrics, applied to detection.

## From data to decisions: the analysis part

Monitoring produces mountains of data; **analysis** turns it into decisions. Key
practices:

- **Correlation** — combining signals from many sources to reveal a pattern no
  single log shows (a failed VPN login, then a success, then mass file access).
- **Trend analysis** — watching metrics over time to spot slow-building problems.
- **Threat intelligence** — external feeds of known-malicious indicators (IP
  addresses, file hashes, domains) that sharpen detection. **Indicators of
  Compromise (IoCs)** are the concrete artifacts that suggest a breach.
- **Metrics and KPIs** — measurable indicators of program health, such as **mean
  time to detect (MTTD)** and **mean time to respond (MTTR)**. You manage what you
  measure.

### Egress and user monitoring

Don't only watch what comes *in*. **Egress monitoring** — inspecting outbound
traffic — catches data exfiltration and malware calling home to its
command-and-control server, which inbound-only monitoring misses entirely.
**User and Entity Behavior Analytics (UEBA)** baselines each user's normal
behavior to flag insider threats and compromised accounts (an account suddenly
downloading gigabytes at 3 a.m.).

## Tuning: clipping levels and who watches

Raw thresholds decide what rises to human attention. A **clipping level** is a
baseline threshold below which routine events are ignored and above which they
generate an alert — for example, "alert only after five failed logins," so a
single fat-fingered password doesn't page an analyst. Set clipping levels too low
and you drown in noise; too high and real attacks slip under the bar.

The people side matters as much as the tooling. In a **Security Operations Center
(SOC)**, analysts typically work in tiers:

- **Tier 1** triages incoming alerts, filters false positives, and escalates what's
  real.
- **Tier 2** investigates escalated incidents in depth.
- **Tier 3** handles advanced threats, threat hunting, and forensics.

> **Threat hunting** flips the model from reactive to proactive: instead of waiting
> for an alert, hunters form a hypothesis ("an attacker may be using this
> technique") and go looking through the data for evidence of it. It's how you find
> the intruder your automated tools missed — a direct answer to the false-negative
> problem.

The common thread across this lesson: monitoring is only as useful as the analysis
and human judgment applied to it. Collecting data is easy; deciding what matters is
the skill.

## Exam focus

- **Continuous monitoring** = ongoing, automated awareness of posture and control
  effectiveness — the modern replacement for once-a-year audits. A **missing
  patch** is a **vulnerability**.
- **Signature-based** detection catches **known** threats (blind to new);
  **anomaly/behavioral** detection catches **novel/zero-day** threats but yields
  more false positives. Both need a **baseline** of "normal."
- Memorize the four outcomes. **False positive = false alarm; false negative =
  missed real attack (the dangerous one).**
- **IDS detects/alerts; IPS blocks inline.** Over-tuning causes **alert fatigue**;
  under-tuning causes false negatives.
- **Correlation**, **threat intelligence / IoCs**, and metrics like **MTTD/MTTR**
  turn raw monitoring into decisions. **Egress monitoring** catches exfiltration
  and C2; **UEBA** catches insider/compromised-account behavior.
