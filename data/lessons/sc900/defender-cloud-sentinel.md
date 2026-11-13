# Microsoft Defender for Cloud & Microsoft Sentinel

The last lesson covered the building-block services that *prevent* problems. This
one covers the two platforms that help you *manage posture* and *detect and
respond* at scale: **Microsoft Defender for Cloud** (continuously harden your
cloud) and **Microsoft Sentinel** (collect signals from everywhere and hunt for
threats). Together they are the management and monitoring brain of Microsoft's
security stack.

## Microsoft Defender for Cloud

> **Microsoft Defender for Cloud** is a **cloud-native application protection
> platform (CNAPP)**. Its two core capabilities are **cloud security posture
> management (CSPM)** — continuously assessing and hardening your configuration —
> and **cloud workload protection (CWPP)** — detecting and responding to threats
> against running resources.

Keep those two pillars straight:

- **CSPM** is about **posture**: "Are my resources configured securely?" It finds
  misconfigurations and gives you recommendations to fix them.
- **CWPP** (the **Defender plans**) is about **threats**: real-time protection and
  alerts for workloads like servers, databases, storage and containers.

### Secure score and recommendations

Defender for Cloud assesses your resources (against the Microsoft cloud security
benchmark from the last lesson) and produces **security recommendations** — the
actionable items that tell you how to harden a resource.

> **Secure score** is a single measurement of your security posture. Remediating
> recommendations **raises your secure score**, giving you a simple number to
> track and improve over time.

### Multicloud and hybrid

Defender for Cloud is not Azure-only. After you connect the accounts, it can
assess and protect resources in **Amazon Web Services (AWS)** and **Google
Cloud**, as well as **on-premises** — one posture view across clouds.

### Just-in-time VM access

A practical CWPP feature worth knowing: **just-in-time (JIT) VM access** keeps VM
management ports (RDP, SSH) **closed** and opens them only for **approved,
time-limited** requests — shrinking exposure to brute-force attacks.

### Regulatory compliance

Defender for Cloud also includes a **regulatory compliance** dashboard that maps
your posture against standards (such as ISO 27001 or PCI DSS), showing where you
meet them and where you have gaps.

## Microsoft Sentinel

Defender for Cloud focuses on cloud posture and workloads. **Microsoft Sentinel**
takes a broader view: collect security data from *everything* — cloud, on-prem,
other clouds, apps, devices — and find the threats hiding in it.

> **Microsoft Sentinel** is a **cloud-native SIEM and SOAR** solution.
> - **SIEM** (Security Information and Event Management) **collects and analyzes**
>   log data from across the enterprise to **detect** threats.
> - **SOAR** (Security Orchestration, Automation and Response) **automates the
>   response** to those threats.

Being cloud-native, Sentinel scales elastically without you managing
infrastructure. Its key components:

### Data connectors

**Data connectors** are how Sentinel ingests data. There are hundreds — for
Microsoft services, other clouds, firewalls, and third-party products — so you can
bring signals from your whole estate into one place.

### Analytics rules and incidents

> **Analytics rules** use queries and logic to detect threats in the ingested
> data and raise **alerts**. Related alerts are correlated into an **incident** —
> a single case an analyst investigates, assigns and manages to resolution.

### Workbooks

**Workbooks** are interactive dashboards that visualize your ingested data —
monitoring and reporting at a glance.

### Hunting

> **Hunting** (threat hunting) lets analysts **proactively search** across
> collected data for undetected threats using queries, **before any alert has
> fired** — getting ahead of attackers instead of waiting for an alarm.

### UEBA

**User and Entity Behavior Analytics (UEBA)** builds behavioral **baselines** for
users and entities and uses machine learning to flag **anomalies** — e.g. a user
account suddenly behaving very differently from normal.

### Playbooks (the SOAR part)

> **Playbooks** are automated response workflows (built on Azure Logic Apps) that
> run when an alert or incident fires — for example, automatically disabling a
> compromised account or opening a ticket. This is Sentinel's **SOAR**
> automation.

### Where Sentinel lives

Sentinel has traditionally been managed in the Azure portal, and Microsoft is
bringing it into the **Microsoft Defender portal** as part of a **unified security
operations** experience, so analysts can work SIEM, SOAR and XDR signals in one
place.

| | Defender for Cloud | Microsoft Sentinel |
|---|-------------------|--------------------|
| Category | CNAPP (CSPM + CWPP) | SIEM + SOAR |
| Focus | Secure **posture** of cloud/hybrid/multicloud resources | **Collect, detect, hunt, automate** across the whole enterprise |
| Signature feature | **Secure score** + recommendations | **Analytics rules → incidents**, hunting, playbooks |

## The whole thing in one paragraph

**Microsoft Defender for Cloud** is a **CNAPP** whose two pillars are **CSPM**
(posture — recommendations that raise your **secure score**) and **CWPP** (the
Defender plans — threat protection for workloads, plus features like **JIT VM
access**); it works across Azure, **AWS, Google Cloud and on-premises**.
**Microsoft Sentinel** is a cloud-native **SIEM + SOAR** that ingests data via
**connectors**, detects threats with **analytics rules** that create **incidents**,
visualizes with **workbooks**, enables proactive **hunting** and **UEBA**, and
automates response with **playbooks** — increasingly managed in the unified
**Microsoft Defender portal**.

## Exam focus

- **Microsoft Defender for Cloud = CNAPP** with two core capabilities: **CSPM**
  (posture) and **CWPP** (workload threat protection). It covers **Azure + AWS +
  GCP + on-premises**.
- **Secure score** measures posture; remediating **recommendations** raises it.
  **JIT VM access** opens management ports only briefly for approved requests.
- **Microsoft Sentinel = cloud-native SIEM + SOAR.** SIEM = collect/analyze/
  detect; SOAR = automate response.
- Sentinel terms: **data connectors** (ingest), **analytics rules** (detect →
  alerts), **incidents** (correlated alerts), **hunting** (proactive search
  before alerts), **UEBA** (behavioral anomalies), **playbooks** (automated
  response = SOAR).
- Don't swap them: **Defender for Cloud = posture/workload protection**;
  **Sentinel = enterprise-wide SIEM/SOAR**.
