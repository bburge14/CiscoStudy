# Azure Infrastructure Security & Baselines

Domain 3 is the biggest slice of SC-900, and it starts with the foundations:
the built-in network security services of Azure, plus the **baselines** that
define a hardened, consistent configuration. This lesson walks the core Azure
security services you must recognize — segmentation, firewalls, DDoS protection,
secure management and secrets — and then explains security baselines and the
Microsoft cloud security benchmark.

## Network segmentation with virtual networks

An Azure **virtual network (VNet)** is your private network in the cloud, and you
carve it into **subnets**. Segmentation is a defense-in-depth staple: break the
network into zones so a compromise in one cannot freely reach the others.

> Important default: **within a VNet there are no access controls between subnets
> by default** — traffic flows freely until you add rules. Segmentation is
> something you must deliberately configure.

### Network security groups (NSGs)

> A **network security group (NSG)** is a basic, stateful packet filter. It
> holds **allow/deny rules** based on source/destination IP, port and protocol,
> and you attach it to a subnet or a network interface to control what traffic is
> permitted.

NSGs are how you actually enforce segmentation between subnets.

### Application security groups (ASGs)

Writing NSG rules against raw IP addresses is brittle. **Application security
groups** let you group VMs by **workload or role** (e.g. "web servers",
"database servers") and write rules against those groups instead of individual
IPs. As VMs come and go, the rules keep working.

## Azure Firewall

For centralized, intelligent filtering across VNets, you use **Azure Firewall**.

> **Azure Firewall** is a managed, cloud-based, **stateful** network firewall. It
> protects your Azure virtual network resources with built-in high availability
> and scalability, and supports rules based on network traffic, applications
> (FQDNs) and threat intelligence.

**Stateful** means it tracks the state of active connections and makes filtering
decisions using that connection context — if it allowed an outbound request, it
knows to allow the matching reply, rather than evaluating each packet in
isolation. An NSG is a lightweight filter; Azure Firewall is a full, centralized
firewall-as-a-service.

## Web Application Firewall (WAF)

NSGs and Azure Firewall work at the network level. A **Web Application Firewall
(WAF)** works at the *application* level, specifically for web apps.

- A WAF protects web applications from common exploits like **SQL injection** and
  **cross-site scripting (XSS)** — the OWASP Top 10 class of attacks.
- In Azure it is provided through services like **Application Gateway** and
  **Azure Front Door**.

## Azure DDoS Protection

A **distributed denial-of-service (DDoS)** attack floods a service with traffic
until it collapses — an **availability** attack.

> **Azure DDoS Protection** defends against **network-layer volumetric and
> protocol flooding attacks** that try to exhaust a resource's capacity, keeping
> your applications available.

Remember the category: DDoS Protection is about **availability**, countering
high-volume network/protocol floods — not application exploits (that is the WAF)
and not malware.

## Azure Bastion and Just-in-Time access

Exposing RDP (3389) or SSH (22) ports to the internet is an open invitation to
brute-force attacks. **Azure Bastion** fixes this.

> **Azure Bastion** provides secure **RDP and SSH** connectivity to your VMs
> **directly through the Azure portal over TLS**, so the VMs **do not need public
> IP addresses** and their management ports stay closed to the internet.

(Defender for Cloud's **just-in-time VM access**, covered next lesson, complements
this by opening management ports only briefly, for approved requests.)

## Azure Key Vault

Secrets — passwords, API keys, certificates, encryption keys — must never live in
code or config files.

> **Azure Key Vault** is a centralized cloud service for securely **storing and
> managing secrets, keys and certificates**, with access controlled and audited.

Pair it with **managed identities** (from Unit 2) and an app can retrieve a secret
from Key Vault with no credentials stored anywhere in the app.

## Security baselines and the Microsoft cloud security benchmark

With dozens of services and settings, how do you know a resource is configured
*securely*? You compare it against a **baseline**.

> A **security baseline** is a standardized set of **recommended security
> configuration settings** that resources should conform to in order to maintain
> a consistent, **hardened** posture — secure defaults and least privilege applied
> the same way everywhere.

Baselines matter to **Zero Trust** because they enforce consistent, hardened
configurations that reduce an attacker's opportunities — every resource starts
from a known-good, locked-down state instead of a risky default.

Microsoft's authoritative set of recommendations is the **Microsoft cloud
security benchmark (MCSB)** — best-practice guidance organized by control domains
(network security, identity management, data protection, logging, and more).

> **Where are Azure resources automatically assessed against the MCSB? In
> Microsoft Defender for Cloud.** Defender for Cloud continuously checks your
> resources against the benchmark and turns gaps into recommendations.

One crucial distinction the exam tests: a **baseline is a recommended technical
hardening configuration**, whereas meeting a **regulatory standard** such as GDPR
is a **legal/compliance obligation**. A baseline hardens how a system is set up;
a regulation is a law you must satisfy. They are related but not the same thing.

## The whole thing in one paragraph

Azure's core infrastructure security services include **VNets and subnets** for
segmentation (which has **no controls between subnets by default**), **NSGs**
(stateful allow/deny filters) and **ASGs** (group VMs by role), **Azure Firewall**
(managed stateful firewall), **WAF** (protects web apps from SQLi/XSS), **Azure
DDoS Protection** (guards availability against network floods), **Azure Bastion**
(secure RDP/SSH with no public IPs) and **Azure Key Vault** (central secrets/keys/
certificates). A **security baseline** is a recommended hardened configuration;
the **Microsoft cloud security benchmark (MCSB)** is Microsoft's benchmark, and
resources are assessed against it automatically in **Microsoft Defender for
Cloud** — distinct from meeting a legal regulation like GDPR.

## Exam focus

- **NSG** = stateful **allow/deny** filter on subnet/NIC; enforces segmentation
  (subnets have **no controls between them by default**). **ASG** = group VMs by
  role and write rules against the group.
- **Azure Firewall** = managed, **stateful** firewall ("stateful" = tracks
  connection state). **WAF** = protects **web apps** (SQL injection, XSS).
- **Azure DDoS Protection** = mitigates **network-layer volumetric/protocol
  floods** (an **availability** defense).
- **Azure Bastion** = secure **RDP/SSH via the portal**, VMs need **no public
  IP**. **Azure Key Vault** = centralized **secrets, keys, certificates**.
- **Security baseline** = recommended **hardened configuration**; **MCSB** is
  assessed in **Microsoft Defender for Cloud**. A baseline (hardening) is **not**
  the same as a regulatory standard (legal compliance).
