# Microsoft Sentinel: Analytics, Incidents & Automation

When alerts come from dozens of sources — Entra ID, Defender for Cloud, firewalls,
Microsoft 365 — someone needs one place to collect, correlate, investigate, and
respond. That is a **SIEM** (security information and event management) with
**SOAR** (security orchestration, automation, and response) bolted on, and in
Azure it is **Microsoft Sentinel**.

> **Microsoft Sentinel** is a cloud-native **SIEM + SOAR** that collects security
> data at scale, uses analytics to turn that data into **incidents**, and
> automates response. It is built on top of a **Log Analytics workspace**, so the
> data it analyzes lives in the same store you query with KQL.

## Getting data in: connectors

Sentinel starts by ingesting logs through **data connectors** — pre-built
integrations for **Microsoft Entra ID**, **Azure Activity**, **Microsoft Defender
XDR**, Office 365, third-party firewalls, and non-Microsoft clouds like **AWS**.
Connected data lands in tables in the workspace, ready for analytics and hunting.
Choosing the right connectors (and managing ingestion cost) is a real operational
skill.

## Analytics rules: from events to incidents

**Analytics rules** are the detection logic. When a rule's condition matches, it
raises an **alert**, and alerts are grouped into **incidents** — the unit an
analyst actually works. The rule types:

- **Scheduled** — custom **KQL** queries that run on a schedule; the workhorse for
  tailored detections.
- **Microsoft security** — automatically create Sentinel incidents from alerts in
  Microsoft security products (e.g. Defender for Cloud).
- **Fusion** — machine-learning correlation that stitches low-fidelity signals
  into high-fidelity **multistage attack** detections.
- **Anomaly** and **near-real-time (NRT)** — behavioral baselines and
  low-latency detections.

Detections are commonly mapped to the **MITRE ATT&CK** framework so you can see
which tactics and techniques your coverage addresses.

## Incidents: investigate and respond

An **incident** bundles related alerts and the **entities** involved (users,
hosts, IPs, files). Analysts:

- Triage by **severity** and **status**, and **assign** ownership.
- Use the **investigation graph** to pivot visually across related entities and
  alerts.
- Enrich with **threat intelligence** and **UEBA** (User and Entity Behavior
  Analytics), which flags anomalous behavior like a user suddenly accessing
  resources they never touch.

## Proactive hunting

You don't wait for alerts. **Hunting** lets analysts run **KQL** queries against
the data to look for threats that no rule caught, save interesting findings as
**bookmarks**, and use **notebooks** for deeper, repeatable investigations.
**Watchlists** bring in reference data (VIP users, known-bad IPs, asset lists) to
enrich both hunting and analytics.

## SOAR: automating the response

The SOAR side is what turns a detection into action without waiting for a human:

- **Playbooks** are **Azure Logic Apps** that perform response steps — disable a
  user, isolate a host, post to a channel, open a ticket, block an IP.
- **Automation rules** govern *when* playbooks run and handle incident
  housekeeping at scale — assigning, tagging, changing severity, suppressing
  noise, and triggering playbooks on incident creation or update.

Together they let common responses happen in seconds and consistently.

## Visualization

**Workbooks** are interactive dashboards built on workspace data for monitoring and
reporting — think an executive view of incident trends or a SOC operations board.

## Content and access control

You rarely build detections from scratch. The **Content hub** installs **solutions**
— bundled connectors, analytics rules, workbooks, hunting queries, and playbooks for
a given product or use case — so coverage can be deployed as a package.

Access to Sentinel uses purpose-built Azure RBAC roles layered on the workspace:

- **Microsoft Sentinel Reader** — view data, incidents, and workbooks.
- **Microsoft Sentinel Responder** — the above **plus** manage incidents (assign,
  change status, add comments).
- **Microsoft Sentinel Contributor** — create and edit analytics rules, workbooks,
  and other content.

Granting the narrowest of these keeps analysts from, say, editing detection logic
when all they need is to work the incident queue.

## The unified security operations platform

Sentinel is converging with **Microsoft Defender XDR** (the extended detection and
response suite covering endpoints, identities, email, and apps) in the **Microsoft
Defender portal**. This **unified security operations platform** gives analysts a
**single incident queue** and shared hunting across SIEM (Sentinel) and XDR
(Defender) signals, rather than switching consoles. Expect the exam to treat
Sentinel and Defender XDR as parts of one SecOps experience.

## Putting it together

Microsoft Sentinel is Azure's **SIEM + SOAR**, built on a **Log Analytics
workspace**. **Connectors** pull in security data; **analytics rules** (especially
**scheduled KQL** and ML-driven **Fusion**) turn that data into **incidents**;
analysts investigate incidents through the **investigation graph**, **entities**,
**UEBA**, and **threat intelligence**, and **hunt** proactively with KQL. **SOAR**
automates response through **playbooks (Logic Apps)** orchestrated by **automation
rules**, while **workbooks** visualize it all. Sentinel and **Defender XDR** now
share one **unified** console in the Defender portal.

## Exam focus

- Sentinel is a **cloud-native SIEM + SOAR** built on a **Log Analytics
  workspace**; **data connectors** ingest Entra, Azure, Defender XDR, and
  third-party/AWS logs.
- **Analytics rules** create **alerts → incidents**. Know the types: **scheduled
  (KQL)**, **Microsoft security**, **Fusion** (ML **multistage attack**
  correlation), anomaly, NRT. Detections map to **MITRE ATT&CK**.
- An **incident** groups alerts and **entities**; investigate with the
  **investigation graph**, **UEBA**, and **threat intelligence**.
- **Hunting** = proactive **KQL** queries with **bookmarks/notebooks**;
  **watchlists** add reference data.
- **SOAR = playbooks (Logic Apps) + automation rules.** Playbooks *do* the
  response; automation rules decide *when* and handle incidents at scale.
- Sentinel + **Defender XDR** are unified in the **Microsoft Defender portal**
  (unified security operations platform) with a single incident queue.
