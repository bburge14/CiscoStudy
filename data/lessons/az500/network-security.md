# Network Security Groups, ASGs & Azure Firewall

Azure networking defense is built in layers. Closest to the workload sit **network
security groups** that filter traffic to subnets and NICs; at the network edge
sits **Azure Firewall**, a managed, stateful firewall that inspects and controls
traffic for a whole virtual network. Knowing which tool does which job — and where
each is attached — is core AZ-500 material.

## The virtual network foundation

A **virtual network (VNet)** is your private network in Azure, carved into
**subnets**. Resources in a VNet can talk to each other by default, which is
exactly why you need filtering: without controls, a compromised VM can move freely
to its neighbors (lateral movement).

## Network security groups (NSGs)

> An **NSG** is a stateful packet filter containing a prioritized list of
> **security rules** that **allow or deny** traffic by source, destination, port,
> and protocol. Because it is **stateful**, you only write the rule for the
> initiating direction; return traffic is allowed automatically.

Each rule has a **priority** (100–4096, **lower number = evaluated first**), a
direction (inbound/outbound), source and destination, port range, protocol, and
an allow/deny action. Evaluation stops at the **first matching rule**.

Every NSG ships with **default rules** you can't delete (only override with
higher-priority rules):

- Inbound: allow traffic **within the VNet**, allow from the **Azure Load
  Balancer**, and **deny everything else**.
- Outbound: allow **within the VNet** and to the **internet**, deny the rest.

### Where an NSG attaches

An NSG can be associated to a **subnet**, to a **NIC**, or both. When both apply,
inbound traffic is filtered at the **subnet first, then the NIC**; outbound is
**NIC first, then subnet**. Because rules can stack, the **Effective security
rules** view (in Network Watcher) is how you see the real, combined result.

### Service tags and ASGs — writing rules that scale

Hardcoding IP ranges is brittle. Two features fix that:

- **Service tags** represent a whole Azure service's address space by name —
  `Storage`, `Sql`, `AzureKeyVault`, `Internet`, `VirtualNetwork` — and Microsoft
  keeps the ranges current. Write "allow outbound to `Storage`" instead of chasing
  IPs.
- **Application security groups (ASGs)** let you group VMs by **role**
  (`web`, `app`, `db`) and write rules between groups — "allow `web` → `app` on
  443" — regardless of the VMs' individual IPs. Membership is just a NIC setting,
  so autoscaled VMs inherit the right rules automatically.

## Azure Firewall

NSGs are great at coarse L3/L4 filtering close to workloads, but they don't do
centralized, application-aware control. **Azure Firewall** does.

> **Azure Firewall** is a managed, cloud-native, **stateful** firewall-as-a-service
> with built-in high availability and unrestricted scale. It sits at the VNet edge
> (typically in a hub) and enforces central rules for all spokes.

Its rule collections:

- **NAT rules** — DNAT inbound traffic (translate a public IP:port to an internal
  one).
- **Network rules** — allow/deny by IP, port, and protocol (L3/L4).
- **Application rules** — filter outbound HTTP/S and SQL by **FQDN** — e.g. allow
  only `*.windowsupdate.com`. This FQDN filtering is something NSGs can't do.

Extra capabilities: a **threat-intelligence** feed that can alert or deny traffic
to/from known-malicious IPs and domains; **FQDN tags** for common Microsoft
services; and **Azure Firewall Premium**, which adds **TLS inspection**, a full
**IDPS** (intrusion detection and prevention), URL filtering, and web categories.
Rules are managed centrally with **Azure Firewall Policy**, which can be shared
and inherited across firewalls.

To force spoke traffic *through* the firewall, you point subnets at it with a
**user-defined route (UDR)** whose next hop is the firewall's private IP — often
a `0.0.0.0/0` default route for **forced tunneling** of all internet-bound
traffic.

### NSG vs Azure Firewall — the key distinction

| | **NSG** | **Azure Firewall** |
|---|---|---|
| Scope | Subnet / NIC | VNet edge, central (hub) |
| Filtering | L3/L4 (IP, port, protocol) | L3/L4 **plus** FQDN/application, threat intel, IDPS (Premium) |
| Cost | Free | Billed (deployment + data) |
| Logging | NSG/VNet flow logs | Firewall logs to Log Analytics |

They are complementary: NSGs micro-segment close to workloads; the firewall gives
central, application-aware control and egress filtering.

## Seeing the traffic: flow logs

You can't secure what you can't see. **VNet flow logs** (the successor to NSG flow
logs) record allowed and denied flows to a storage account, and **Traffic
Analytics** turns them into a map of who's talking to whom — invaluable for
spotting exfiltration or misconfigured rules.

## Putting it together

Start inside the VNet with **NSGs** — stateful, prioritized allow/deny rules on
subnets and NICs, made maintainable with **service tags** and **application
security groups**. Add **Azure Firewall** at the hub for central, stateful control
including **FQDN/application filtering**, threat intelligence, and (Premium) TLS
inspection and IDPS, and force traffic through it with **UDRs**. Finally, turn on
**flow logs** so you can actually observe and tune what all those rules are doing.

## Exam focus

- **NSGs are stateful** L3/L4 filters with **prioritized rules (lower number
  first)**; evaluation stops at the first match. Default rules allow intra-VNet and
  load-balancer traffic and **deny all else** inbound.
- An NSG attaches to **subnet and/or NIC**; use **Effective security rules** to see
  the combined result. Use **service tags** for Azure services and **ASGs** to
  group VMs by role instead of hardcoding IPs.
- **Azure Firewall** is central and stateful and adds what NSGs can't: **FQDN /
  application-rule filtering**, **threat intelligence**, and (Premium) **TLS
  inspection + IDPS**. Managed via **Firewall Policy**.
- Route spoke traffic through the firewall with a **UDR** (next hop = firewall
  private IP); a `0.0.0.0/0` route gives **forced tunneling**.
- "Filter outbound by domain name/FQDN" ⇒ **Azure Firewall application rules**, not
  an NSG.
- **VNet/NSG flow logs + Traffic Analytics** give visibility into allowed and
  denied flows.
