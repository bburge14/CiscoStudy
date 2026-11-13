# Advanced Hunting & Custom Detection Rules

With KQL in hand, you can hunt. **Advanced hunting** is the query-based threat
hunting experience in Microsoft Defender XDR, running over a rich, unified schema
of raw telemetry. And once a hunt reliably finds something bad, you promote it to a
**custom detection rule** so Defender runs it automatically and acts on the
results. This lesson covers both the hunting schema and the detection rules built
from it.

## Advanced hunting in Defender XDR

> **Advanced hunting** lets you write KQL against roughly **30 days** of raw event
> data collected across the Defender workloads, in one shared schema. It is
> proactive: you hunt for suspicious patterns before — or alongside — the alerts
> the product raises on its own.

The schema groups tables by the source workload. You don't need to memorize every
column, but you must know *which table holds which kind of event*:

| Prefix / table | Holds |
|----------------|-------|
| `DeviceProcessEvents` | Process creation on onboarded devices |
| `DeviceNetworkEvents` | Network connections from devices |
| `DeviceFileEvents` | File create/modify/delete on devices |
| `DeviceLogonEvents` | Logons observed on devices |
| `DeviceRegistryEvents` | Registry changes |
| `DeviceImageLoadEvents` | DLL/image loads |
| `EmailEvents`, `EmailAttachmentInfo`, `EmailUrlInfo`, `UrlClickEvents` | Defender for Office 365 mail flow, attachments, URLs, and clicks |
| `IdentityLogonEvents`, `IdentityQueryEvents`, `IdentityDirectoryEvents`, `IdentityInfo` | Defender for Identity authentication and AD activity |
| `CloudAppEvents` | Defender for Cloud Apps activity |
| `AlertInfo`, `AlertEvidence` | The alerts themselves and the entities tied to them |

So: hunting for a suspicious process → `DeviceProcessEvents`; a phishing URL that
was clicked → `UrlClickEvents`; LDAP reconnaissance → `IdentityQueryEvents`.

An example hunt for a classic living-off-the-land pattern — `rundll32` launched by
an Office application:

```kql
DeviceProcessEvents
| where Timestamp > ago(14d)
| where InitiatingProcessFileName in~ ("winword.exe", "excel.exe", "outlook.exe")
| where FileName =~ "rundll32.exe"
| project Timestamp, DeviceName, AccountName,
          InitiatingProcessFileName, FileName, ProcessCommandLine, ReportId
```

From the results you can **take action directly** — isolate a device, run an AV
scan, or collect an investigation package — and you can pivot from an incident or
entity straight into a scoped query with **go hunt**.

> **Advanced hunting in Microsoft Sentinel is similar but not identical.** Sentinel
> queries the Log Analytics tables filled by its *connectors* (`SigninLogs`,
> `SecurityEvent`, `CommonSecurityLog`, …), while Defender XDR advanced hunting
> queries the XDR schema above. Same language (KQL); different tables.

## Custom detection rules

Hunting is manual. A **custom detection rule** turns a saved advanced-hunting query
into a **scheduled detection** that runs on its own, raises **alerts/incidents**,
and can trigger **response actions** — the Defender XDR counterpart to a Sentinel
scheduled analytics rule.

### What the query must return

A custom detection query cannot be arbitrary — Defender needs specific columns to
know *when* each hit happened and *what* it impacts.

> A custom detection query must project a **`Timestamp`**, a **`ReportId`**, and at
> least one **entity column** (such as `DeviceId`/`DeviceName`, `AccountSid`/
> `AccountUpn`, or `Sha1`). Those columns tell the rule which entity to attach the
> alert to and which response actions become available.

### Configuring the rule

- **Frequency** — how often it runs: continuous (near real time), or every 1, 3,
  12, or 24 hours. Defender looks back over a matching window.
- **Alert details** — title, severity, category, description, and **MITRE ATT&CK**
  technique.
- **Impacted entities** — map the entity columns so the alert is investigable.
- **Actions** — what Defender does automatically on a hit. Device actions (isolate
  device, run AV scan, collect investigation package, restrict app execution), file
  actions (block/quarantine a file by hash), and user actions (mark user as
  compromised, disable user) — the available set depends on which entity your query
  returns.

Taking the hunt above and making it a detection means saving the query (it already
projects `Timestamp`, `DeviceName`, and `ReportId`), setting it to run every 3
hours, titling it, mapping *Execution* in ATT&CK, and attaching **Run antivirus
scan** as the device action.

### XDR custom detections vs Sentinel analytics rules

Both schedule a KQL query to create alerts and respond, but they live in different
places and query different data. Use a **custom detection rule** when your logic is
in the **Defender XDR schema** and you want XDR-native response; use a **scheduled
analytics rule** when the logic is in **Sentinel's workspace tables** and you want
Sentinel incidents and playbooks.

## Exam focus

- **Advanced hunting** = KQL over ~**30 days** of raw Defender XDR telemetry in a
  **unified schema**. Match events to tables: process → **`DeviceProcessEvents`**,
  network → **`DeviceNetworkEvents`**, clicked URL → **`UrlClickEvents`**, AD query
  → **`IdentityQueryEvents`**, alert entities → **`AlertEvidence`**.
- You can **take response actions from query results** and pivot via **go hunt**
  from incidents/entities.
- **Defender XDR advanced hunting** (XDR schema) vs **Sentinel advanced hunting**
  (Log Analytics connector tables) — same KQL, different tables.
- A **custom detection rule** promotes a saved hunting query to a **scheduled
  detection** that raises alerts/incidents and runs response actions.
- The query **must return `Timestamp`, `ReportId`, and at least one entity column**;
  you set **frequency** (continuous/1/3/12/24h), alert details with **MITRE**
  mapping, and **actions** (isolate device, AV scan, disable user, block file —
  depending on entity).
- The Sentinel equivalent is the **scheduled analytics rule**; pick by where the
  data and desired response live.
