# Microsoft Defender for Cloud & JIT VM Access

Once resources are deployed, someone has to answer two ongoing questions: *How
secure is my configuration right now?* and *Is anything actively attacking my
workloads?* **Microsoft Defender for Cloud** answers both. It combines **posture
management** (finding and fixing misconfigurations) with **workload protection**
(detecting threats), and it is the home of **just-in-time VM access**.

> **Name note:** Defender for Cloud is the product formerly known as **Azure
> Security Center** (posture) and **Azure Defender** (workload protection), now
> unified under one name. Expect "Defender for Cloud" on the exam.

## Two halves: posture and protection

Defender for Cloud has two pillars, and you should be able to tell them apart:

- **Cloud Security Posture Management (CSPM)** — continuously assesses your
  configuration, scores it, and recommends fixes. Mostly about **prevention**.
- **Cloud Workload Protection (CWP)** — the paid **Defender plans** that watch
  running resources and raise **security alerts** on active threats. About
  **detection and response**.

## Posture management, secure score, and compliance

The free, built-in layer is **foundational CSPM**, and its centerpiece is the
**secure score**.

> **Secure score** is an aggregated percentage of how well your environment follows
> security recommendations. **Higher is better** — a higher score means lower
> assessed risk. Each recommendation is tied to controls and points you earn by
> remediating.

Foundational CSPM (free) gives you:

- **Security recommendations** mapped to the **Microsoft Cloud Security Benchmark
  (MCSB)** — the default policy initiative measuring your baseline.
- The **secure score** and asset inventory.
- A **regulatory compliance dashboard** mapping your posture to standards (ISO
  27001, PCI DSS, NIST, and more).

The paid **Defender CSPM** plan adds advanced posture tools: **agentless scanning**
of VMs, **attack path analysis** and the **cloud security graph** (which chains
findings into real attack routes an adversary could take), DevOps security, and
data-aware posture.

## Workload protection: the Defender plans

Turning on a **Defender plan** activates threat detection for that resource type.
The main ones:

| Plan | Protects |
|------|----------|
| **Defender for Servers** | VMs — EDR, vulnerability assessment, more (see below) |
| **Defender for Storage** | Storage accounts — malware scanning, sensitive-data threat detection |
| **Defender for SQL / Databases** | SQL and other databases — SQLi and anomaly alerts, vulnerability assessment |
| **Defender for Containers** | AKS/Kubernetes and container registries |
| **Defender for Key Vault** | Unusual vault access |
| **Defender for App Service** | Web apps |
| **Defender for Resource Manager / APIs** | Control-plane and API threats |

**Defender for Servers** comes in two plans you must distinguish:

- **Plan 1** — endpoint detection and response via integration with **Microsoft
  Defender for Endpoint**.
- **Plan 2** — Plan 1 **plus** premium **vulnerability management**, **agentless
  scanning**, **file integrity monitoring (FIM)**, OS baseline assessment against
  the MCSB, free log ingestion allowance, and — importantly — **just-in-time VM
  access**.

## Just-in-time (JIT) VM access

Management ports left open to the internet are a top attack vector. **JIT VM
access** (a Defender for Servers Plan 2 feature) closes them until you actually
need them.

> With **JIT**, inbound management ports (RDP 3389, SSH 22) are **blocked by
> default** via NSG/Azure Firewall rules. When an authorized user needs access they
> **request it**; Defender for Cloud opens the port **to their source IP for a
> limited time**, then **re-locks it automatically**.

Why it's powerful: the ports are closed to attackers almost always, access is
**time-boxed and audited**, and requesting it is governed by **RBAC**. It pairs
naturally with **Azure Bastion** (brokered access) for layered VM administration.

## Acting on findings

- **Security alerts** from the Defender plans flow to the Defender for Cloud
  portal and can be **exported to Sentinel** or a SIEM.
- **Workflow automation** triggers a **Logic App** when an alert or recommendation
  fires — for example, open a ticket or isolate a resource.
- **Multicloud** connectors extend posture and (some) protection to **AWS and GCP**
  accounts, so one console covers a hybrid estate.

## Putting it together

Defender for Cloud watches your estate from two angles. **CSPM** continuously
scores your configuration against the **Microsoft Cloud Security Benchmark**,
surfaces **recommendations**, drives the **secure score** (higher = safer), and
maps to **regulatory standards** — free at the foundational tier, with **Defender
CSPM** adding attack-path analysis and agentless scanning. The paid **Defender
plans** add threat detection per resource type, with **Defender for Servers Plan
2** unlocking vulnerability management, FIM, and **just-in-time VM access** that
keeps RDP/SSH closed until a time-boxed, audited request opens them. Alerts can
flow into **Sentinel** and trigger **Logic App** automation.

## Exam focus

- Defender for Cloud = **CSPM (posture)** + **CWP/Defender plans (threat
  detection)**. "Misconfiguration/posture/score" ⇒ CSPM; "active threat/alert" ⇒ a
  Defender plan.
- **Secure score**: aggregated posture percentage — **higher = lower risk**;
  improve it by remediating recommendations mapped to the **Microsoft Cloud
  Security Benchmark**. The **regulatory compliance dashboard** maps posture to
  standards.
- **Foundational CSPM is free** (recommendations, secure score, MCSB, compliance);
  **Defender CSPM** (paid) adds **agentless scanning**, **attack path analysis**,
  and the cloud security graph.
- **Defender for Servers Plan 1 = EDR** (Defender for Endpoint); **Plan 2** adds
  **vulnerability management, agentless scanning, FIM, and JIT VM access**.
- **JIT VM access** keeps **RDP/SSH closed by default** and opens them **to a
  requester's IP for a limited time**, then re-locks — reducing exposed management
  ports.
- Alerts can export to **Sentinel**; **workflow automation** uses **Logic Apps**;
  connectors extend to **AWS/GCP**.
