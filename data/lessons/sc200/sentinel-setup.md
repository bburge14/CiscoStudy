# Designing & Deploying a Sentinel Workspace

Microsoft Sentinel is Microsoft's cloud-native **SIEM** (security information and
event management) and **SOAR** (security orchestration, automation, and response)
platform. It collects security data at cloud scale, detects threats with analytics,
and automates response. But before any of that, you have to stand it up correctly —
and Sentinel's foundation is a **Log Analytics workspace**. Getting the workspace
design right up front is what this lesson is about, because it is hard to change
later.

## Sentinel sits on a Log Analytics workspace

> Microsoft Sentinel is **enabled on top of a Log Analytics workspace (LAW)**. The
> workspace is where all ingested logs are stored and where **Kusto Query Language
> (KQL)** runs. Enabling Sentinel adds the SIEM/SOAR features; the workspace
> provides the storage and query engine.

That means workspace decisions *are* Sentinel decisions. Every analytics rule,
hunting query, and workbook ultimately queries tables in this workspace.

## Workspace design decisions

- **Single vs multiple workspaces.** A **single workspace** is simplest: one place
  to query, correlate, and manage. You reach for **multiple** workspaces when you
  must satisfy **data residency** (logs pinned to a region), separate tenants (MSSP
  or conglomerate), or delegate control to business units. Cross-workspace queries
  are possible but add complexity, so prefer one workspace unless a requirement
  forces more.
- **Region.** The workspace region determines where data lives — a compliance
  consideration, and it affects some ingestion costs.
- **Access (RBAC).** Scope who can read, investigate, and configure Sentinel.
- **Cost.** Sentinel bills largely on **data ingested**. Choosing a **commitment
  tier** (a fixed daily volume at a discount) over **pay-as-you-go** can cut cost
  at scale, and routing high-volume, low-value logs to cheaper **Basic/Auxiliary
  logs** instead of full **Analytics logs** helps too.

## Roles: who can do what

Sentinel ships built-in Azure roles layered on the workspace:

| Role | Can |
|------|-----|
| **Microsoft Sentinel Reader** | View data, incidents, and workbooks (read-only) |
| **Microsoft Sentinel Responder** | The Reader rights **plus** manage incidents (assign, change status, add comments) |
| **Microsoft Sentinel Contributor** | The Responder rights **plus** create and edit analytics rules, workbooks, and other content |

> Grant the **least privilege** that fits the job: tier-1 analysts triage as
> **Responders**; content authors need **Contributor**. Playbook execution and
> automation often require additional Logic Apps / resource permissions.

## The Content hub

You rarely build Sentinel from scratch. The **Content hub** is a marketplace of
**solutions** — prepackaged bundles that install a data connector plus its matching
analytics rules, hunting queries, workbooks, and playbooks for a given product
(Microsoft Entra ID, AWS, Palo Alto, and hundreds more). Installing the right
solutions is usually step one after enabling Sentinel.

## Retention and visualization

- **Retention.** Each table has an **interactive retention** period (hot, fully
  queryable) that you can extend, and a cheaper **long-term/archive** tier for data
  you must keep but rarely query. You tune retention per table to balance cost and
  compliance.
- **Workbooks.** Sentinel **workbooks** are interactive dashboards built on KQL
  that visualize your ingested data — ingestion health, sign-in trends, incident
  metrics. Many solutions ship ready-made workbooks you can customize.

## The deployment sequence

Putting the pieces in order, a clean Sentinel rollout looks like this:

1. **Create or choose a Log Analytics workspace** in the right region, sized for
   your expected ingestion.
2. **Enable Microsoft Sentinel** on that workspace.
3. **Assign roles** (Reader / Responder / Contributor) to the SOC with least
   privilege.
4. **Install solutions from the Content hub** for the products you run.
5. **Enable data connectors** so data starts flowing into tables.
6. **Turn on analytics rules** (from templates) to generate incidents.
7. **Build automation rules and playbooks** to respond.
8. Optionally **onboard to the Defender portal** to unify the incident queue.

> Steps 1–2 are the foundation; everything after assumes the workspace exists.
> Connectors before rules before automation — you cannot detect data you are not
> ingesting, and you cannot automate a response to an incident that never fires.

## Running Sentinel in the Defender portal

Sentinel increasingly lives in the **unified Microsoft Defender portal** alongside
Defender XDR, not only in the Azure portal.

> When you onboard Sentinel to the Microsoft Defender portal, you connect **one
> primary workspace**, so the unified incident queue can merge Sentinel and
> Defender XDR incidents. Plan for this: after March 31, 2027, Microsoft Sentinel
> is slated to be available **only in the Defender portal**, not the Azure portal.

## Exam focus

- Sentinel is a cloud-native **SIEM + SOAR** built **on a Log Analytics
  workspace**; the workspace stores data and runs **KQL**.
- Prefer a **single workspace**; choose **multiple** for **data residency**,
  multi-tenant/MSSP, or delegated control. Region sets data location.
- Billing is driven by **data ingested**; **commitment tiers** discount at volume,
  and **Basic/Auxiliary logs** are cheaper than **Analytics logs** for high-volume
  sources.
- Roles: **Reader** (view) → **Responder** (+ manage incidents) → **Contributor**
  (+ author rules/content). Apply **least privilege**.
- The **Content hub** installs **solutions** (connector + rules + workbooks +
  playbooks). **Workbooks** visualize data; **retention** is tuned per table
  (interactive vs long-term/archive).
- Onboarding to the **Defender portal** uses **one primary workspace** and unifies
  the incident queue; the Azure portal experience retires after **March 31, 2027**.
