# Secure Cloud, Hybrid & Resilient Design

Enterprises run across their own data centers and several cloud providers at once.
The architect's job is to secure that sprawl consistently and to design it so that
a failure — an outage, a region loss, a ransomware event — does not become a
business-ending event. This lesson joins **secure cloud/hybrid architecture** with
**resilience and high availability**, because in practice you design them together.

## The shared responsibility model

Cloud security starts with knowing who secures what. The **shared responsibility
model** splits duties between provider and customer, and the line moves with the
service model.

| Model | Provider secures | Customer secures |
|-------|------------------|------------------|
| **IaaS** | Physical, hypervisor, network fabric | **OS, patching, apps, data, IAM, configuration** |
| **PaaS** | + OS and runtime | Apps, data, access, configuration |
| **SaaS** | + application | **Data, access, and configuration/usage** |

> The provider is always responsible for security **of** the cloud; the customer is
> always responsible for security **in** the cloud. On **IaaS** the customer still
> owns OS patching and hardening; even on **SaaS** the customer owns **data and
> access**. Misconfiguration — an open storage bucket, over-broad IAM — is the
> customer's fault, not the provider's.

## Tooling the cloud posture

Several consolidated platforms exist to enforce policy across providers:

- **CASB (Cloud Access Security Broker)** — a control point between users and cloud
  apps. It gives visibility into **shadow IT** (unsanctioned SaaS), enforces DLP,
  and applies access policy to both sanctioned and unsanctioned apps.
- **CNAPP (Cloud-Native Application Protection Platform)** — a single platform that
  unifies cloud security. It combines:
  - **CSPM** (Cloud Security Posture Management) — finds **misconfigurations** and
    compliance drift.
  - **CWPP** (Cloud Workload Protection Platform) — protects **workloads**
    (VMs, containers, serverless).
  - **CIEM** (Cloud Infrastructure Entitlement Management) — manages **identities
    and effective permissions** across providers.
- **SWG / secure landing zones / IaC guardrails** enforce standards at deployment.

> "One platform for posture + workload protection + entitlements across
> multicloud" = **CNAPP**. "Discover and control shadow-IT SaaS usage" = **CASB**.
> "Find misconfigurations" = **CSPM**.

## Hybrid and multicloud concerns

**Hybrid** (on-prem + cloud) and **multicloud** (several providers) add their own
risks: inconsistent policy across platforms, identity federation between
environments, secure interconnects (VPN/direct-connect), and avoiding **vendor
lock-in**. The architectural goal is a *consistent* control plane — centralized
identity, logging, and policy — so that each environment is governed the same way
rather than as a set of snowflakes.

## Resilience vocabulary: RPO, RTO, and friends

Resilience planning is driven by two targets that come straight out of a **Business
Impact Analysis (BIA)**:

- **RPO (Recovery Point Objective)** — the **maximum tolerable data loss**,
  expressed as *time*. "We can lose at most 15 minutes of transactions" is an RPO.
  RPO drives **backup/replication frequency**.
- **RTO (Recovery Time Objective)** — the **maximum tolerable downtime** before a
  function must be restored. RTO drives your **recovery strategy** choice.

Two reliability metrics accompany them: **MTBF (Mean Time Between Failures)** —
how reliable a component is — and **MTTR (Mean Time To Repair)** — how fast you
restore it. **MTD (Maximum Tolerable Downtime)** is the absolute ceiling.

> **RPO = data loss (how far back)**; **RTO = downtime (how long to recover)**. A
> very low RPO means replicate often; a very low RTO means pre-stage a fast
> recovery site.

## Disaster recovery sites and strategies

The DR strategy you pick is driven by RTO versus cost:

| Site type | Readiness | RTO | Cost |
|-----------|-----------|-----|------|
| **Hot site** | Fully running, data synced; near-instant failover | Minutes | Highest |
| **Warm site** | Hardware ready, partial data; needs work | Hours | Medium |
| **Cold site** | Space/power only; build from scratch | Days | Lowest |

For an extremely low RTO (resume in minutes, cost secondary), the answer is a **hot
site** or active-active cloud region. **Geographic dispersion** across regions
protects against a whole-site loss, and **active-active** vs **active-passive**
describes whether the standby is also serving traffic.

## Backups and the 3-2-1 rule

Backups are the last line against ransomware and corruption. The widely taught
baseline is the **3-2-1 rule**:

> Keep **3** copies of your data, on **2** different media/storage types, with **1**
> copy **off-site** (and ideally offline/**immutable**). The extended **3-2-1-1-0**
> adds **1 offline/air-gapped** copy and **0** verified errors (tested restores).

A ransomware tabletop that finds all backups on one NAS *in the same building* as
production fails 3-2-1 twice over — no off-site copy and no media diversity. The fix
is an off-site, and preferably **immutable/offline**, copy that malware cannot
encrypt. Always verify with **restore testing**; an untested backup is a hope, not
a control.

## High availability in the live system

Resilience is not only recovery after failure — it is avoiding downtime in the first
place. **Load balancing** spreads traffic and removes single points of failure;
**clustering** provides automatic failover; **redundancy** (N+1, RAID, dual power,
multiple ISPs) eliminates single components; and **auto-scaling** absorbs demand.
Design to remove **single points of failure** at every tier.

## Exam focus

- **Shared responsibility**: provider secures *of* the cloud, customer secures *in*
  it. On **IaaS** the customer still owns OS patching; even on **SaaS** the customer
  owns **data and access**. Misconfigurations are the customer's responsibility.
- **CASB** = shadow-IT visibility and SaaS policy; **CNAPP** = unified multicloud
  posture = **CSPM** (misconfig) + **CWPP** (workloads) + **CIEM** (entitlements).
- **RPO = tolerable data loss (time)** → backup frequency; **RTO = tolerable
  downtime** → recovery strategy. **MTTR** = repair time, **MTBF** = reliability.
- DR sites by RTO/cost: **hot** (minutes, costliest) → **warm** (hours) → **cold**
  (days, cheapest). Very low RTO → **hot site/active-active**.
- **3-2-1**: three copies, two media, one off-site; prefer **immutable/offline** so
  ransomware cannot reach it, and **test restores**.
- Remove **single points of failure** with load balancing, clustering, and
  redundancy for high availability.
