# Secure Enterprise Architecture & Zero Trust

Architecture is where security either succeeds or fails before an attacker ever
shows up. A SecurityX architect designs systems that assume breach: multiple
independent layers, a minimized attack surface, segmentation that contains blast
radius, and — the modern centerpiece — a **zero-trust** model that stops granting
trust based on network location. This lesson covers the design principles and the
zero-trust reference architecture.

## Core design principles

Good secure design is a handful of principles applied relentlessly.

- **Defense in depth (layered security)** — independent, overlapping controls so
  that bypassing one still leaves an attacker facing others. After the perimeter
  firewall falls, the intruder should still meet host hardening, segmentation,
  least privilege, and monitoring. No single control is a single point of failure.
- **Attack surface reduction** — remove everything an attacker could reach or
  exploit: disable unused services and ports, remove default accounts, uninstall
  unneeded software, close unnecessary interfaces. Less exposed means less to
  defend.
- **Least privilege** — every subject gets only the access its function requires,
  and no more.
- **Secure (fail-safe) defaults** — systems ship locked down; access is granted
  explicitly, not removed after the fact. A failure should **fail closed** for
  security-critical decisions.
- **Separation of duties** and **defense in breadth** round out the set.
- **Keep it simple** — complexity is the enemy of assurance. Simpler designs have
  fewer places to hide a flaw.

> Defense in depth assumes *every* control can fail. You design so that the failure
> of any one layer is survivable because another layer is still standing.

## Segmentation and the lateral-movement problem

The most expensive architectural mistake is a **flat network** — one large Layer 2
domain where every host can reach every other. Once an attacker lands anywhere,
they move freely between HR, finance, and OT systems. Breaches become enterprise-
wide instead of contained.

**Segmentation** breaks the network into zones with enforced boundaries so that
compromise in one zone does not grant the others:

- **Network segmentation / VLANs + firewalls** — separate trust zones (user, server,
  OT, guest) with filtered traffic between them.
- **Screened subnet (DMZ)** — isolates internet-facing services from the internal
  network.
- **Microsegmentation** — the finest grain: per-workload policy *inside* a subnet,
  so two VMs on the same segment cannot talk unless policy allows it. This is how
  you block east-west (lateral) movement between workloads.
- **Air gap** — physical isolation for the most sensitive systems, with controlled
  data transfer.

> A flat Layer 2 domain enables lateral movement; **segmentation** (and, finest-
> grained, **microsegmentation**) contains it. If a breach "spread freely because
> everything shared one broadcast domain," the fix is segmentation.

## Zero Trust: never trust, always verify

Zero trust abandons the old "hard shell, soft center" model. There is no trusted
inside. Every request is authenticated, authorized, and encrypted on its own
merits, regardless of where it originates.

**NIST SP 800-207** is the authoritative reference. Memorize its logical components
and their split:

- **Policy Engine (PE)** — makes the access *decision* by evaluating policy.
- **Policy Administrator (PA)** — executes the decision: establishes or tears down
  the session.
- Together, PE + PA form the **Policy Decision Point (PDP)** — the brain.
- **Policy Enforcement Point (PEP)** — sits in the data path and *enforces* the
  decision, allowing or blocking the actual connection.

> The decision and the enforcement are deliberately separated: the **PDP (Policy
> Engine + Policy Administrator) decides**; the **PEP enforces** in the traffic
> path. "Evaluates policy and decides" = PDP; "sits in the path and allows/blocks"
> = PEP.

NIST's tenets are worth knowing in spirit: all resources are accessed securely
regardless of location; access is granted **per-session** on **least privilege**;
decisions are driven by **dynamic policy** using identity, device health, and
context; and the enterprise monitors the integrity of all assets continuously.
Zero trust also distinguishes the **control plane** (where policy decisions and
administration happen) from the **data plane** (where approved traffic flows).

### Enablers: identity, device posture, and microsegmentation

Zero trust is realized through **strong identity** (phishing-resistant MFA),
continuous **device posture/health** checks, **adaptive/context-aware** policy
(step-up authentication for anomalous requests), and **microsegmentation** to
enforce identity-aware, per-workload rules even between VMs in the same subnet.

## SASE and SSE: zero trust for the distributed edge

With users and apps everywhere, backhauling traffic to a data-center firewall no
longer makes sense. Gartner's **SASE (Secure Access Service Edge)** converges
networking and security into one cloud-delivered service at the edge. Its security
subset is **SSE (Security Service Edge)**.

| Model | What it bundles |
|-------|-----------------|
| **SASE** | **SD-WAN (networking)** + security: SWG, CASB, FWaaS, **ZTNA** |
| **SSE** | The **security** services only: **SWG + CASB + ZTNA** (often FWaaS/DLP) |

Key members: **ZTNA** (Zero Trust Network Access — identity-and-context-based access
to *specific apps*, replacing broad VPN tunnels), **SWG** (Secure Web Gateway),
**CASB** (Cloud Access Security Broker), and **FWaaS**.

> The difference to remember: **SASE = SSE + SD-WAN networking.** SSE is the
> security half (SWG + CASB + ZTNA). **ZTNA** replaces the "VPN = full network
> access" model with per-application, identity-aware access.

## Exam focus

- **Defense in depth** = independent layers that survive one another's failure;
  **attack surface reduction** = disable unused services/ports, remove defaults.
- A **flat network** enables lateral movement; **segmentation** contains it, and
  **microsegmentation** enforces per-workload policy to stop east-west movement
  inside a subnet.
- **NIST SP 800-207**: **PE + PA = PDP** (decides); **PEP** (enforces in the data
  path). "Decides" vs "allows the traffic through" is the discriminator.
- Zero trust grants access **per-session**, on **least privilege**, via **dynamic,
  context-aware policy** — network location grants nothing.
- **SASE = SSE + SD-WAN**; **SSE = SWG + CASB + ZTNA**. **ZTNA** gives per-app,
  identity-aware access and replaces broad VPN network access.
- **Secure/fail-safe defaults** mean systems ship locked down and security-critical
  failures **fail closed**.
