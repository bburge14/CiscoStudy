# Security Alerts in Microsoft Defender for Cloud

When a Defender plan detects something malicious or suspicious on a protected
workload, it raises a **security alert**. Alerts are the reactive output of
Defender for Cloud, and operating them — triaging, responding, suppressing noise,
and routing them onward — is a core SOC task. This lesson pins down what an alert
is, how it differs from a recommendation, and what you do with it.

## Alert vs recommendation: don't blur them

> A **recommendation** is **proactive** — a hardening action that improves posture
> and drives secure score ("enable MFA," "restrict this port"). A **security
> alert** is **reactive** — a notification that Defender detected suspicious or
> malicious activity that is *happening or has happened* ("suspected brute-force
> against this VM").

Recommendations prevent; alerts respond. The exam tests this constantly, so fix it
firmly: if the stem describes *detecting an attack*, it's an alert; if it describes
*fixing a weakness to prevent one*, it's a recommendation.

## Anatomy of an alert

Open an alert and you get a structured record built for triage:

- **Severity** — High / Medium / Low / Informational, reflecting confidence and
  potential impact.
- **Affected resource** — the VM, storage account, database, or cluster involved.
- **MITRE ATT&CK mapping** — the tactic and technique the activity corresponds to,
  so you understand *where in an attack* you are (initial access, execution,
  exfiltration…).
- **Description and alert timeline** — what was seen and when.
- **Related entities** — the accounts, IPs, processes, and resources involved, so
  you can pivot quickly during investigation.
- **Remediation / response steps** — suggested actions to contain and investigate.

Many alerts also carry an **intent** (the kill-chain stage) and, where relevant,
**threat intelligence** enrichment such as the reputation of an IP involved.

Alerts move through **statuses** — **Active → In Progress → Dismissed / Resolved** —
so a team can track who is working what and close the loop.

### A triage flow

A practical way to work an alert, and a useful mental model for the exam:

1. **Read the severity and resource.** A High-severity alert on a
   production-facing SQL server outranks a Low-severity one on a dev VM.
2. **Use the MITRE mapping to place it.** An *Initial Access* alert is early; an
   *Exfiltration* alert means act now.
3. **Confirm or dismiss.** Check the evidence and the affected resource's recent
   activity. If it is a known scanner or test, dismiss (or better, suppress the
   pattern); if it is real, move to In Progress and respond.
4. **Contain and remediate**, then record the outcome by setting status to
   Resolved so the metrics stay honest.

> Severity plus the MITRE tactic together drive **prioritization**: *how bad* and
> *how far along* an attack is. Don't triage on severity alone.

## Security incidents in Defender for Cloud

Like Defender XDR, Defender for Cloud can **correlate related alerts** on the same
resource or attack sequence into a **security incident**, so a multi-step attack
(recon, then lateral movement, then exfiltration) reads as one story rather than
three disconnected alerts.

## Responding to and taming alerts

You have several levers:

- **Investigate and respond** directly on the alert, following its guidance.
- **Suppression rules** — silence known-benign alert patterns (for example, a
  vulnerability scanner that always trips a "port scan" detection) by criteria,
  instead of dismissing the same alert forever by hand.
- **Workflow automation** — trigger a **Logic App** when an alert (or
  recommendation) of a given type fires: open a ticket, post to Teams, email an
  owner, or run a containment action automatically.
- **Sample alerts** — generate benign test alerts to validate that your pipelines,
  automation, and exports actually work before a real one hits.

> Prefer a **suppression rule** over repeatedly dismissing the same false positive:
> one rule handles the pattern going forward and documents *why* it is benign.

## Getting alerts where they need to be

Alerts rarely stay in Defender for Cloud alone. You route them with:

- **Continuous export** — stream alerts and recommendations to a **Log Analytics
  workspace** or **Azure Event Hub** for retention, dashboards, or downstream tools.
- The **Microsoft Sentinel connector** — bring Defender for Cloud alerts into
  Sentinel so they become **incidents** there, correlate with other sources, and
  can drive SOAR playbooks.
- **Email notifications** — alert subscription owners or a security contact when
  high-severity alerts fire.

This export path is why Defender for Cloud and Sentinel are taught together: the
cloud workload detections you learned here become raw material for the SIEM
analytics and automation in the next unit.

## Exam focus

- **Recommendation = proactive hardening (drives secure score); security alert =
  reactive detection of suspicious/malicious activity.** This distinction is
  heavily tested.
- Alerts carry **severity**, **affected resource**, a **MITRE ATT&CK** tactic/
  technique mapping, and **remediation steps**; they move through **Active → In
  Progress → Dismissed/Resolved**.
- Related alerts can correlate into a **security incident** within Defender for
  Cloud.
- Use **suppression rules** to quiet known-benign patterns (better than repeated
  dismissal) and **workflow automation** (Logic Apps) to respond automatically.
  **Sample alerts** validate your pipeline.
- Route alerts out via **continuous export** (Log Analytics / Event Hub) and the
  **Microsoft Sentinel connector**, where they become Sentinel incidents.
