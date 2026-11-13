# Connecting Data Sources to Microsoft Sentinel

A SIEM is only as good as the data flowing into it. **Data connectors** are how
Microsoft Sentinel ingests logs from Microsoft services, third-party products, and
raw log sources. Choosing the right connector — and knowing which **table** the
data lands in — is foundational, because every analytics rule and hunting query in
later lessons runs against those tables.

## How connectors work

A connector configures a pipeline from a source into your workspace and, once
connected, populates one or more **tables** you can query with KQL. The connector
page shows its status, the data types it brings, and how recently data arrived, so
you can confirm ingestion is healthy. Most connectors ship inside **Content hub
solutions** alongside the rules and workbooks that make the data useful.

## The connector families

### Native / service-to-service connectors

Microsoft cloud sources connect directly, no agent required:

- **Microsoft Defender XDR** — brings endpoint, email, identity, and cloud-app
  alerts and raw advanced-hunting tables into Sentinel.
- **Microsoft Entra ID** — sign-in and audit logs (`SigninLogs`, `AuditLogs`).
- **Microsoft 365 / Office activity** and **Azure Activity** (control-plane logs).
- **Microsoft Defender for Cloud** — streams its security alerts into Sentinel.

These are the easiest to enable and should be your first connectors in a
Microsoft-heavy estate.

### Agent-based connectors: AMA and DCRs

For operating-system and many third-party logs, Sentinel uses the **Azure Monitor
Agent (AMA)**.

> **AMA is the current agent**, and it collects according to a **Data Collection
> Rule (DCR)** — a definition of *what* to collect and *where* to send it. The
> older **Log Analytics agent (MMA/OMS)** is **deprecated**; expect AMA + DCR as
> the right answer.

The headline example is **Windows Security Events**, collected by AMA. The DCR lets
you pick how much to ingest:

| Event set | Scope |
|-----------|-------|
| **All Security Events** | Every Windows security event (highest volume/cost) |
| **Common** | A curated, useful subset |
| **Minimal** | A small set for very constrained budgets |
| **Custom** | Your own **XPath** filter for exactly the events you want |

Windows security events land in the **`SecurityEvent`** table.

### Syslog and CEF

Linux and network/appliance logs arrive as **Syslog** or **Common Event Format
(CEF)**:

- **Syslog** messages → the **`Syslog`** table.
- **CEF** messages → the **`CommonSecurityLog`** table.

These are collected by **AMA running on a Linux log-forwarder** VM that your
firewalls, proxies, and appliances send to. Point your devices at the forwarder;
the forwarder's AMA (driven by a DCR) ships the events to the workspace.

### Custom and codeless ingestion

For sources without a prebuilt connector, use the **Logs Ingestion API** or a
**Codeless Connector Platform (CCP)** connector to push custom logs into a custom
table. **Threat intelligence** has its own connectors (TAXII and the upload
API), covered in the hunting-and-intelligence unit.

## Normalization with ASIM

Different sources describe the same thing in different fields. The **Advanced
Security Information Model (ASIM)** provides **normalized schemas and parsers** so a
single detection can run across many sources (for example, a normalized
authentication schema spanning Windows, Linux, and cloud sign-ins) without
rewriting the query per source.

> Normalize with **ASIM** when you want one rule to cover many log sources; it
> trades a little query-time overhead for portable, source-agnostic detections.

## Verifying ingestion

After enabling a connector, confirm data is actually arriving before you build
detections on it. The connector page shows a "last data received" timestamp, and
you can check directly with a quick KQL query against the expected table:

```kql
SecurityEvent
| where TimeGenerated > ago(1h)
| summarize Events = count(), Devices = dcount(Computer) by bin(TimeGenerated, 15m)
| sort by TimeGenerated desc
```

If the table is empty or the count is far lower than expected, the usual culprits
are a missing or misscoped **DCR**, the agent not installed or unhealthy on the
source, or (for Syslog/CEF) devices not pointed at the forwarder. Diagnosing "why
is there no data?" is a realistic SOC task — always trace it back from the table to
the DCR to the agent to the source.

## Exam focus

- **Data connectors** ingest data and populate **tables**; most come via **Content
  hub solutions**. Native Microsoft connectors (**Defender XDR, Entra ID, Office,
  Azure Activity, Defender for Cloud**) are agentless and easiest.
- OS/third-party logs use the **Azure Monitor Agent (AMA)** with a **Data
  Collection Rule (DCR)**. The legacy **Log Analytics agent (MMA)** is
  **deprecated** — pick AMA + DCR.
- **Windows Security Events** (via AMA/DCR) choose **All / Common / Minimal /
  custom XPath** and land in **`SecurityEvent`**.
- **Syslog → `Syslog`**, **CEF → `CommonSecurityLog`**, both via **AMA on a Linux
  forwarder**. Entra sign-ins → **`SigninLogs`**.
- Use the **Logs Ingestion API / codeless connectors** for custom sources, and
  **ASIM** normalized parsers/schemas to write one detection across many sources.
