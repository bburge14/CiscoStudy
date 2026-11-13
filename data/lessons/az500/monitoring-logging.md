# Azure Monitor, Log Analytics & KQL

Detection and investigation are only as good as the telemetry underneath them.
**Azure Monitor** is the platform that collects metrics and logs across Azure,
**Log Analytics** is where logs are stored and queried, and **KQL (Kusto Query
Language)** is how you ask questions of that data. Sentinel, Defender for Cloud,
and your own alerts all sit on this foundation — so a security engineer has to
know how the logs get there and how to query them.

## Azure Monitor and the data it collects

Azure Monitor gathers two broad kinds of telemetry:

- **Metrics** — lightweight, numeric, time-series values (CPU %, request count)
  sampled frequently; good for dashboards and fast metric alerts.
- **Logs** — richer, structured event records stored in a **Log Analytics
  workspace** and queried with KQL.

The log sources a security engineer cares about most:

| Source | What it tells you | How you get it |
|--------|-------------------|----------------|
| **Activity log** | **Control-plane** events — *who did what* to a resource (created, deleted, changed roles) at the subscription level | Built in; route to a workspace with a diagnostic setting |
| **Resource (diagnostic) logs** | **Data-plane** operations inside a resource (Key Vault accesses, storage requests, NSG events) | **Enable a diagnostic setting** per resource |
| **Platform metrics** | Performance/health numbers | Built in |
| **Guest OS / agent data** | Events and performance from inside VMs | **Azure Monitor Agent (AMA)** |

> Two distinctions the exam tests: **Activity log = control plane ("who changed
> what"); resource/diagnostic logs = data plane ("what happened inside").** And
> the **Azure Monitor Agent (AMA)** is the current agent, replacing the legacy Log
> Analytics agent (MMA/OMS).

## Diagnostic settings: the routing switch

A resource doesn't send its logs anywhere until you create a **diagnostic
setting**. That setting routes logs and metrics to one or more of three
destinations, each for a purpose:

- **Log Analytics workspace** — to **query and alert** with KQL (and feed
  Sentinel).
- **Storage account** — cheap **long-term archive/retention**.
- **Event Hubs** — **stream** to a third-party SIEM or external pipeline.

Designing where the workspace lives, who has **RBAC** on it, and how long data is
**retained** is part of secure logging — logs themselves are sensitive and must be
access-controlled and tamper-resistant.

## Alerts and action groups

**Alert rules** watch for conditions and fire when they're met:

- **Metric alerts** — threshold on a metric (CPU > 90%).
- **Log alerts** — a **KQL** query returns results (e.g. "more than 5 failed
  sign-ins in 5 minutes").
- **Activity log alerts** — a control-plane event occurs (someone deletes an NSG,
  assigns Owner).

When an alert fires, an **action group** defines the response — email/SMS, a
webhook, a Logic App, an ITSM ticket, or an Azure Function.

## KQL basics

**Kusto Query Language (KQL)** is read-only and reads top to bottom, piping a table
through operators with the `|` symbol. The shape is: start with a table, then
filter, shape, and aggregate.

```kusto
SigninLogs
| where TimeGenerated > ago(1h)
| where ResultType != 0            // failed sign-ins
| summarize Failures = count() by UserPrincipalName, IPAddress
| where Failures > 5
| sort by Failures desc
```

The operators you must recognize:

- **`where`** — filter rows by a condition.
- **`project`** / **`project-away`** — choose (or drop) columns.
- **`summarize`** — aggregate: `count()`, `sum()`, `avg()`, `dcount()`, grouped
  `by` one or more columns.
- **`extend`** — add a calculated column.
- **`sort`/`order by`** and **`top`** — rank and limit.
- **`join`** / **`union`** — combine tables.
- **`bin()`** and **`ago()`** — bucket and bound by time (e.g. `bin(TimeGenerated,
  1h)`, `ago(7d)`).

The same KQL you write for a log alert is the language behind **Sentinel analytics
rules and hunting** and behind **Defender for Cloud** queries — learn it once, use
it everywhere.

## Network and flow visibility

**Network Watcher** complements log data with network diagnostics — **flow logs**
(allowed/denied traffic), **connection troubleshoot**, **IP flow verify** (does an
NSG allow this flow?), and **NSG diagnostics** — which you'll use to confirm that
your networking controls behave as intended.

## Putting it together

**Azure Monitor** collects **metrics** and **logs**; logs land in a **Log Analytics
workspace** you query with **KQL**. The **Activity log** records control-plane "who
did what," while **resource/diagnostic logs** (switched on with a **diagnostic
setting**) record data-plane activity — route them to a **workspace** to query, to
**storage** to archive, or to **Event Hubs** to stream out. Build **metric, log,
and activity-log alerts** that notify through **action groups**, use **KQL**'s
`where`/`summarize`/`project`/`join` pipeline to investigate, and lean on **Network
Watcher** for traffic-level visibility. This telemetry is the bedrock Sentinel and
Defender for Cloud are built on.

## Exam focus

- **Azure Monitor** = metrics + logs; **Log Analytics workspace** stores logs for
  **KQL** queries (and Sentinel).
- **Activity log** = **control-plane**, "who created/changed/deleted" at the
  subscription level. **Resource/diagnostic logs** = **data-plane**; you must
  **enable a diagnostic setting** to collect them.
- Diagnostic-setting destinations: **Log Analytics** (query/alert), **Storage**
  (long-term archive), **Event Hubs** (stream to external SIEM).
- The **Azure Monitor Agent (AMA)** replaces the legacy Log Analytics/MMA agent for
  guest data.
- Alert types: **metric**, **log (KQL)**, and **activity-log** alerts; responses run
  through **action groups**.
- KQL core operators: **`where`, `project`, `summarize ... by`, `extend`, `join`,
  `sort/top`, `ago()`/`bin()`**. The same language powers **Sentinel rules and
  hunting**.
