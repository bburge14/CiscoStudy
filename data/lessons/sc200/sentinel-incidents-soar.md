# Incident Management, Automation & SOAR Playbooks

Detections are useless if no one works them and nothing responds. This lesson
covers the operational end of Microsoft Sentinel: **managing incidents** (triage,
investigation, and proactive hunting) and the **SOAR** layer that automates
response — **automation rules** for orchestration and **playbooks** built on Azure
**Logic Apps** for the actual work.

## The incident queue

When an analytics rule fires, Sentinel creates (or updates) an **incident** — a
container of related alerts and the entities they involve. The incident queue is
where the SOC lives.

Each incident carries:

- **Severity** (High/Medium/Low/Informational) and **status** — **New → Active →
  Closed**.
- **Owner** — assign to an analyst for accountability.
- **Classification on close** — **True Positive**, **Benign Positive**, **False
  Positive**, or **Undetermined**, with a reason. These verdicts feed tuning and
  reporting.
- **Tasks** — a checklist on the incident so responders follow a consistent
  playbook, and **comments** for an audit trail.

> Closing an incident is not just setting status to Closed — you record a
> **classification and reason** (e.g., *False Positive – inaccurate data*). Good
> classification is how a SOC measures detection quality over time.

## Investigating an incident

Open an incident and Sentinel gives you an **investigation graph**: a visual map of
the entities (users, hosts, IPs, files) and how they relate, which you can expand
to pull in connected activity. **Entity pages** go deeper on a single user or host,
showing a timeline and the **UEBA** behavioral insights (what is normal for this
entity, and how the current activity deviates). This is where entity mapping from
your analytics rules pays off.

## Proactive hunting

Not every threat sets off an alert. The **Hunting** page lets analysts run a
library of **hypothesis-driven KQL queries**, organized by **MITRE ATT&CK**
tactic, to search for suspicious patterns *before* anything fires.

> When a hunting query surfaces something worth keeping, save it as a
> **bookmark** — a preserved row of evidence you can attach to a new or existing
> incident. **Livestream** lets you run a query continuously to watch an unfolding
> situation in near real time.

## SOAR part 1: automation rules

**Automation rules** are the lightweight, no-code orchestration layer. An
automation rule **triggers** on an event (incident created, incident updated, or
alert created), checks **conditions**, and performs **actions** — all without
writing a workflow.

Typical uses:

- **Auto-triage noise.** A rule that matches incidents from a known-noisy analytics
  rule and automatically **changes status to Closed** with a classification —
  quieting the queue *without disabling the rule*.
- **Assign and tag.** Route incidents to a team by setting the owner and adding
  tags.
- **Sequence and schedule.** Run multiple actions in order, and apply the same
  automation across many rules centrally (so you manage response logic in one
  place).
- **Call a playbook.** When real work is needed, the automation rule's action is to
  **run a playbook**.

> Reach for an **automation rule** to *decide and orchestrate* (close, assign, tag,
> or trigger a playbook on a condition). Reach for a **playbook** to *do* the
> heavier, integrated work.

## SOAR part 2: playbooks (Logic Apps)

A **playbook** is an **Azure Logic Apps** workflow — a sequence of connected
actions across services. Playbooks are where Sentinel reaches out to the rest of
your environment.

Playbooks start from a **trigger**:

- **Incident trigger** — runs when an incident is created/updated (the common case,
  usually invoked by an automation rule).
- **Alert trigger** — runs per alert.
- **Entity trigger** — run on demand against a specific entity during
  investigation (e.g., "enrich this IP").

Common playbook actions:

- **Enrich** — look up an IP/file against threat intelligence or a geolocation
  service and post the result back as an incident comment.
- **Notify** — message a Microsoft **Teams** channel or email an on-call analyst.
- **Ticket** — open an incident in **ServiceNow** or Jira.
- **Respond** — isolate a device via Defender for Endpoint, disable a user in
  Microsoft Entra ID, or block an IP on the firewall.

> A playbook authenticates to the services it touches. It typically runs with a
> **managed identity** (or a connection) that must be granted the right
> permissions — including a Microsoft Sentinel role such as **Responder** if the
> playbook updates incidents.

## How it fits together

The end-to-end flow: an analytics rule creates an **incident** → an **automation
rule** matches it and either closes/assigns it or **triggers a playbook** → the
**playbook** enriches, notifies, opens a ticket, and takes a containment action.
Analysts handle what remains in the queue, investigate with the graph and entity
pages, and hunt proactively to find what never alerted. That loop — detect,
automate, investigate, hunt — is the SOC operating model Sentinel is built around.

## Exam focus

- Incidents move **New → Active → Closed**; on close you set a **classification**
  (**True Positive / Benign Positive / False Positive / Undetermined**) and reason.
  Use **owner**, **tasks**, **tags**, and **comments** to manage them.
- Investigate with the **investigation graph** and **entity pages** (with **UEBA**
  insights). The **Hunting** page runs **MITRE ATT&CK-mapped KQL** proactively;
  **bookmarks** preserve findings and attach to incidents; **livestream** watches
  in near real time.
- **Automation rules** = no-code trigger/condition/action orchestration (auto-close
  noisy incidents, assign, tag, or **run a playbook**). They can quiet a noisy rule
  **without disabling it**.
- **Playbooks** = **Azure Logic Apps** workflows triggered by **incident**,
  **alert**, or **entity** triggers; they enrich, notify (Teams/email), open
  tickets, and take containment actions (isolate device, disable user, block IP).
- Remember the division of labor: **automation rule decides/orchestrates; playbook
  does.** Playbooks need **permissions** (often a **managed identity** with a
  Sentinel **Responder** role to modify incidents).
