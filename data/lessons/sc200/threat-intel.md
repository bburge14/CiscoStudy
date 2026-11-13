# Threat Intelligence in Microsoft Sentinel

**Threat intelligence (TI)** is curated knowledge about adversaries — the
infrastructure, tools, and artifacts they use — that you feed into your detections
so the SOC recognizes known-bad activity immediately. Microsoft Sentinel can
ingest, manage, and operationalize threat intelligence, and SC-200 expects you to
know the vocabulary, the connectors, and how indicators turn into detections.

## Indicators: the currency of TI

> An **indicator of compromise (IoC)** is an observable artifact that signals
> malicious activity — a **file hash**, **IP address**, **domain**, or **URL**
> known to be used by attackers. "Indicator of _______" → *compromise*.

Related terms: **indicators of attack (IoA)** describe adversary *behavior* rather
than static artifacts, and the richest intelligence also captures tactics,
techniques, and procedures (TTPs) mapped to **MITRE ATT&CK**. But the bread-and-
butter of TI matching is the IoC.

Indicators carry metadata you manage: a **confidence** score, a **validity period**
(an IP may be malicious this week and reassigned next month, so indicators expire),
**tags**, and a threat type. Curating this metadata keeps TI accurate and low-noise.

## Standards: STIX and TAXII

Threat intelligence is shared using open standards, and the exam likes to test the
difference:

| Standard | What it is |
|----------|------------|
| **STIX** (Structured Threat Information eXpression) | The **format** — how threat data is structured and described |
| **TAXII** (Trusted Automated eXchange of Indicator Information) | The **transport protocol** — how feeds are delivered/exchanged |

> **STIX is the language; TAXII is the delivery truck.** STIX structures the data;
> TAXII moves it between servers and clients.

## Getting TI into Sentinel

Sentinel offers several threat-intelligence connectors:

- **Threat Intelligence – TAXII** — subscribe to a **TAXII 2.x** server/feed
  (commercial or community) and pull indicators automatically.
- **Threat Intelligence Upload Indicators API** — push indicators from your own
  **threat intelligence platform (TIP)** into Sentinel programmatically.
- **Microsoft Defender Threat Intelligence (MDTI)** — bring Microsoft's own
  first-party intelligence feed into the workspace.

Once ingested, indicators are stored and queryable in the
**`ThreatIntelligenceIndicator`** table, and you manage them (view, search, add
manually, tag, or expire) on Sentinel's **Threat Intelligence** page. A built-in
**workbook** visualizes your indicators — counts, sources, and types.

## Curating indicators

Ingesting a feed is not the end — raw feeds are noisy, and stale indicators cause
false positives. Curation keeps TI useful:

- **Add indicators manually** for threats specific to your organization (a phishing
  domain seen only in your mail).
- **Tag** indicators so you can group a campaign and reference it in rules and
  hunts.
- **Set confidence and expiration** so low-quality or time-expired indicators stop
  generating alerts.
- **Relate** indicators and threat objects (actors, attack patterns) to build
  context, as modern STIX-object support allows.

> Treat threat intelligence as a *living* dataset. An indicator with no expiration
> and no confidence is a future false positive — curate confidence, validity, and
> tags, not just volume.

## Turning TI into detections

Ingesting indicators does nothing until you *match* them against your data. That is
the job of **threat intelligence analytics rules**.

> Sentinel ships **"TI map" analytics rule templates** that join your
> **`ThreatIntelligenceIndicator`** indicators against event tables — matching a
> malicious IP against firewall logs, a bad domain against DNS queries, a known-bad
> hash against file events — and raise an alert on any hit.

Conceptually a TI matching rule does exactly what you learned in the KQL lesson:

```kql
let iocDomains =
    ThreatIntelligenceIndicator
    | where Active == true and ExpirationDateTime > now()
    | where isnotempty(DomainName)
    | project DomainName, ThreatType, ConfidenceScore;
DeviceNetworkEvents
| where Timestamp > ago(1h)
| join kind=inner iocDomains on $left.RemoteUrl == $right.DomainName
| project Timestamp, DeviceName, RemoteUrl, ThreatType, ConfidenceScore
```

This is why TI sits in the hunting-and-intelligence unit: an indicator is just data
until a KQL join turns it into a detection. You can also use indicators
interactively while hunting — pivot on a suspicious hash to see whether it matches
known intelligence.

## Beyond Sentinel: threat analytics

Microsoft Defender XDR adds **threat analytics** — analyst-written reports on active
campaigns and threat actors, with detections and recommended mitigations mapped to
your environment. It is intelligence for *reading and acting*, complementary to the
indicator matching Sentinel does for *detecting*.

## Exam focus

- An **IoC (indicator of compromise)** is an artifact — **hash, IP, domain, URL**.
  Indicators carry **confidence**, **tags**, and a **validity/expiration** period.
- **STIX = format/language; TAXII = transport protocol.** Don't swap them.
- Sentinel ingests TI via the **TAXII** connector, the **Upload Indicators API**
  (from a TIP), and **Microsoft Defender Threat Intelligence (MDTI)**. Indicators
  live in the **`ThreatIntelligenceIndicator`** table and are managed on the
  **Threat Intelligence** page.
- **Threat intelligence ("TI map") analytics rules** match indicators against your
  logs (IP vs firewall, domain vs DNS, hash vs files) to raise alerts — a KQL
  **join** under the hood.
- **Defender XDR threat analytics** provides actor/campaign reports with mitigations
  — intelligence to read and act on, complementing Sentinel's indicator matching.
