# The Unified Incident Queue & Attack Disruption

Each Defender workload — Endpoint, Office 365, Identity, Cloud Apps — raises its
own alerts. The power of Microsoft Defender XDR is that it does not leave those
alerts scattered. It **correlates** related alerts from every workload into a
single **incident** and presents them in one **unified incident queue** inside the
Microsoft Defender portal (security.microsoft.com). This lesson is about living in
that queue: how incidents are built, how you triage and investigate them, and how
XDR can contain an attack on its own.

## From alerts to incidents

> An **alert** is a single detection. An **incident** is a correlated collection
> of alerts, assets (devices, users, mailboxes), and evidence that Defender XDR
> believes belong to the **same attack**. One incident can span endpoints, email,
> identities, and cloud apps.

Correlation is the feature that makes XDR more than the sum of its parts. Instead
of an analyst manually connecting a phishing alert, an endpoint malware alert, and
an identity recon alert, XDR links them by shared entities (the same user, the
same device, the same file hash) and timeline into one story. That both reduces
alert fatigue and reveals the *scope* of an intrusion at a glance.

## Triaging the queue

The incident queue is the SOC's worklist. Each incident carries attributes you use
to triage and manage it:

- **Severity** — High / Medium / Low / Informational.
- **Status** — New, In progress, Resolved.
- **Assignment** — the analyst who owns it.
- **Classification** — once investigated, you label an incident **true positive**,
  **false positive**, or **informational, expected activity** (benign-but-noticed).
  A sub-category of "determination" records *what* it was.
- **Tags** — free-form labels for grouping and routing.

> Classifying incidents is not just bookkeeping. The verdicts feed Defender XDR's
> tuning and, where enabled, help machine learning reduce similar noise — so
> accurate classification improves tomorrow's queue.

## Investigating an incident

Open an incident and you get a structured investigation surface rather than a raw
log dump:

- The **attack story** (incident graph) visualizes the entities involved and how
  they connect — the spread of the attack across assets.
- **Alerts** lists every correlated detection with its source workload.
- **Assets** enumerates affected devices, users, and mailboxes.
- **Evidence and response** collects the files, processes, IPs, and other
  artifacts, each with a verdict and the ability to take action.
- A unified **timeline** orders events so you can reconstruct sequence.

From here you pivot straight into **advanced hunting** (the shared KQL schema
across workloads) to answer questions the incident raises — "where else did this
file run?" — without leaving the investigation.

## Automatic attack disruption

Some attacks move too fast for human triage. **Automatic attack disruption** uses
high-confidence, cross-workload XDR signals to **contain an in-progress attack
automatically**, buying the SOC time.

> When XDR is highly confident an active attack is underway — human-operated
> ransomware, business email compromise, or adversary-in-the-middle — disruption
> can **contain the device**, **disable or suspend the compromised user**, or
> **contain the user** across the environment, without waiting for an analyst.

This is deliberately *high-precision*: it triggers only on strong, correlated
evidence, because the actions it takes (cutting a device off, disabling an account)
are disruptive by design. Disruption actions appear in the incident and can be
reverted by an analyst. Alongside it, **self-healing** reverses malicious changes
automated investigation finds, and **Microsoft Security Copilot** (where licensed)
can summarize an incident and guide response in natural language.

## Acting during an investigation

Investigation and response happen in the same place. From within an incident you
can take manual actions on its entities without hopping between consoles: isolate
an affected device, stop and quarantine a malicious file everywhere it appears,
suspend a compromised user, or submit a file for deep analysis. Each action is
recorded against the incident and, like the automated ones, tracked centrally so
there is a single history of what was done and by whom.

> The design goal is **triage, investigate, and respond in one incident**. If you
> find yourself exporting data to act elsewhere, you are usually missing a
> built-in action — check the entity's flyout and the evidence list first.

When Sentinel is onboarded to the Defender portal, its incidents join this same
queue, so an analyst works Defender XDR and Sentinel incidents side by side instead
of switching portals.

## Governing who can do what

Access to the queue and to response actions is controlled by **role-based access
control**. Microsoft Defender XDR supports **unified RBAC**, letting you define
granular permissions across the Defender workloads from one place, so a tier-1
analyst can triage while only senior responders can isolate devices or disable
accounts. **Microsoft Secure Score** (the configuration and posture score for your
Microsoft 365 and device estate) rounds out the portal by showing how your
*proactive* hardening is trending, not just your reactive response.

## Exam focus

- An **alert** is one detection; an **incident** is the **correlated** set of
  alerts/assets/evidence for a single attack. Correlation across **Endpoint,
  Office 365, Identity, and Cloud Apps** is the core XDR value.
- Triage attributes: **severity, status, assignment, classification** (true
  positive / false positive / informational-expected), and **tags**.
- Know the investigation surfaces: **attack story/incident graph, alerts, assets,
  evidence and response, timeline**, and the pivot to **advanced hunting**.
- **Automatic attack disruption** = high-confidence, automatic **containment**
  (contain device, disable/suspend user, contain user) of an *active* attack like
  human-operated ransomware — it is high-precision and reversible.
- **Self-healing** reverts malicious changes; **Microsoft Secure Score** tracks
  proactive posture; **unified RBAC** governs who can triage vs. take response
  actions. The queue lives in the Microsoft Defender portal.
