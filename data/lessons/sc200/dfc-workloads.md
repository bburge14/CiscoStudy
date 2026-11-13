# Defender for Cloud Workload Protection Plans

Posture management tells you where you are weak; **workload protection** watches
for attacks happening *now*. In Microsoft Defender for Cloud this is delivered by
the paid **Defender plans**, which together form a **Cloud Workload Protection
Platform (CWPP)**. Each plan is enabled per subscription and protects a specific
resource type — servers, storage, databases, containers, and more — providing
threat detection and security alerts tailored to that workload.

## CSPM vs CWPP: the one distinction to anchor

> **CSPM** (free, foundational) is about **posture** — recommendations and secure
> score that harden your configuration. **CWPP** (the paid **Defender plans**) is
> about **protection** — real-time threat detection and alerts for running
> workloads. CSPM finds the unlocked door; CWPP catches the burglar.

You turn plans on individually from the **Environment settings** of a subscription,
so you can protect your crown-jewel SQL servers without paying to protect every
resource type. Pricing is per resource (per server, per storage account, and so
on).

## The major Defender plans

| Plan | Protects | Representative capabilities |
|------|----------|------------------------------|
| **Defender for Servers** | Windows/Linux VMs (Azure, AWS, GCP, on-prem via Arc) | Integrates **Microsoft Defender for Endpoint**, agentless and agent-based vulnerability scanning, **just-in-time VM access**, file integrity monitoring |
| **Defender for Storage** | Azure Storage accounts | Detects malicious uploads, **malware scanning** of blobs, sensitive-data threat detection |
| **Defender for Databases** | Azure SQL, SQL on machines, open-source relational DBs, Cosmos DB | Detects SQL injection, anomalous access, brute force |
| **Defender for Containers** | Kubernetes / AKS, EKS, GKE | Container image vulnerability scanning, runtime threat detection, Kubernetes hardening |
| **Defender for App Service** | Azure App Service web apps | Detects web-app attacks, suspicious processes, dangling DNS |
| **Defender for Key Vault** | Azure Key Vault | Detects unusual secret/key access patterns |
| **Defender for Resource Manager** | The Azure control plane | Detects suspicious management operations (ARM) |
| **Defender for APIs** | Azure API Management | Detects API abuse and discovers sensitive data exposure |

You do not need to memorize every alert, but you should be able to **match a
workload to its plan**: a threat against a storage blob → Defender for Storage; a
suspicious `kubectl`/pod event → Defender for Containers; a malicious ARM
deployment → Defender for Resource Manager.

## Agentless and agent-based protection

Plans gather signal two ways, and knowing the difference helps you reason about
coverage:

- **Agent-based** protection runs software on the workload — the Defender for
  Endpoint sensor on a server, for example — giving real-time, in-OS detection.
- **Agentless scanning** takes a point-in-time snapshot of a VM's disk (or scans a
  container registry) from outside the machine, with nothing installed. It is great
  for broad vulnerability and malware coverage without deployment friction, but it
  is periodic, not live.

> Use both: **agent-based** for real-time endpoint detection, **agentless** for
> wide, low-friction posture and vulnerability coverage. Many environments run
> agentless scanning everywhere and reserve the agent for high-value servers.

## Defender for Servers in depth

Servers are the most exam-relevant plan because of its two tiers:

- **Plan 1** focuses on endpoint protection: it deploys and integrates **Microsoft
  Defender for Endpoint** so your VMs get the same EDR your workstations do.
- **Plan 2** adds the broader server toolkit: vulnerability assessment,
  **just-in-time (JIT) VM access**, **file integrity monitoring**, adaptive
  application controls, agentless disk scanning, and free data ingestion
  allowances.

> **Just-in-time VM access** keeps management ports (RDP/SSH) closed by default and
> opens them only on approved request, for a limited time, from a specific IP —
> shrinking the window an attacker can brute-force those ports.

Because Defender for Servers *is* how MDE reaches your servers, this is the bridge
back to Unit 1: server EDR alerts flow into the same Defender XDR experience.

## Enabling and operating plans

Plans are toggled per subscription under **Environment settings** — select the
subscription (or AWS/GCP connector), and switch each plan On or Off. Because
billing follows the resources a plan protects, you right-size cost by enabling only
the plans that matter for a given subscription. A few operational points worth
remembering:

- Enabling a plan is near-instant for posture, but detections need telemetry, so
  give it time to baseline before expecting alerts.
- Some plans deploy components automatically (the MDE extension, the Azure Monitor
  Agent, or a Defender sensor for containers); review what each plan provisions.
- You can start workloads at the free posture tier and turn on the paid plan later
  once you have validated the recommendations — posture first, protection second.

## Where the alerts go

Every plan produces **security alerts**, which appear in Defender for Cloud and can
be **streamed to Microsoft Sentinel** (via the Defender for Cloud connector) and,
for workloads with XDR integration, correlated in the Microsoft Defender portal.
That continuity — posture in CSPM, detection in CWPP, response in Sentinel/XDR — is
the Microsoft SecOps story you are being tested on.

Each plan also deepens the **recommendations** you met in the posture lesson: a
plan's threat-detection features often come paired with hardening guidance specific
to that workload (container registry scanning findings, SQL vulnerability
assessment results), so turning on a plan improves both your detection coverage and
your posture signal at once.

## Exam focus

- **Defender plans = CWPP = paid workload protection** (threat detection and
  alerts), distinct from **free foundational CSPM = posture**. Plans are enabled
  **per subscription, per resource type**.
- Be able to **map workload → plan**: storage blob malware → **Defender for
  Storage**; SQL injection → **Defender for Databases**; AKS/pod threat →
  **Defender for Containers**; malicious ARM operation → **Defender for Resource
  Manager**; Key Vault anomaly → **Defender for Key Vault**.
- **Defender for Servers Plan 1** = **Defender for Endpoint** integration; **Plan
  2** adds vulnerability assessment, **JIT VM access**, **file integrity
  monitoring**, and agentless scanning.
- **Just-in-time VM access** opens RDP/SSH only on approved, time-boxed request —
  it reduces brute-force exposure.
- Plan alerts can be **exported to Microsoft Sentinel** and correlated in Defender
  XDR, tying posture → protection → response together.
