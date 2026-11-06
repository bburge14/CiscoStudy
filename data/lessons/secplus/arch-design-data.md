# Secure Design, Data Protection & Resilience

This lesson is about building to survive. First we place security *appliances* and
*principles* into an enterprise so the infrastructure itself is defensible. Then
we classify and protect **data** wherever it lives. Finally we plan for the day
something fails — the **resilience and recovery** that keeps the business running.

## Secure design: building a defensible infrastructure

Good design starts with *where things sit*. Key infrastructure considerations:

- **Device placement** — put security devices where they can see and control the
  right traffic (e.g. a firewall at the network edge).
- **Security zones** — group systems by trust level (public, DMZ, internal) and
  control traffic between zones.
- **Attack surface** — keep it small; every exposed service is a target.
- **Connectivity** — how things link up, and securing each link.
- **Failure modes** — decide what happens when a control fails. **Fail-open**
  keeps traffic flowing (favors availability); **fail-closed** blocks traffic
  (favors security). Which is right depends on what you're protecting.

### Active vs. passive, inline vs. tap

A device can sit **inline** (traffic flows *through* it, so it can block) or as a
**tap/monitor** (it gets a *copy*, so it can only watch). Relatedly, a control can
be **active** (takes action) or **passive** (observes). An **IPS** is inline and
active — it blocks. An **IDS** is typically passive/tap — it alerts but doesn't
stop traffic.

### Network appliances you should know

| Appliance | Job |
|-----------|-----|
| **Firewall** | Allow/deny traffic by rules |
| **Proxy server** | Middleman for requests; can filter and hide clients |
| **Load balancer** | Spreads traffic across servers for availability |
| **Jump server** | A hardened gateway host for admins to reach secure zones |
| **IDS / IPS** | Detect (IDS) or detect-and-block (IPS) attacks |
| **Sensors** | Collect data/telemetry for monitoring |

### Firewall flavors

- **Layer 4** firewalls filter by IP and port (the classic packet filter).
- **Layer 7 / NGFW (Next-Generation Firewall)** understands *applications* and can
  make smarter decisions.
- **WAF (Web Application Firewall)** specifically protects web apps from attacks
  like SQLi and XSS.
- **UTM (Unified Threat Management)** bundles many security functions into one
  appliance.

### Port security and secure access

Control who connects at the port level with **802.1X** (port-based network access
control) and **EAP** (the authentication framework it uses). For remote and
site-to-site connectivity, use secure tunnels:

- **VPN** with **TLS** or **IPsec** tunneling for encrypted remote access.
- **SD-WAN** — software-defined WAN that intelligently routes and secures branch
  traffic.
- **SASE (Secure Access Service Edge)** — bundles networking and security
  (including zero-trust access) into a cloud-delivered service for a distributed
  workforce.

> When choosing a control, match it to the job: a **WAF** for web-app attacks, a
> **load balancer** for availability, a **jump server** for safe admin access,
> **802.1X** for who's allowed to plug in.

## Protecting data: classify it, then guard it

You can't protect data evenly — you protect it according to how sensitive it is.

### Data types and classifications

**Data types** include **regulated** data (governed by law), **trade secrets**,
**intellectual property (IP)**, **legal information**, **financial information**,
and the human/non-human-readable distinction.

**Data classifications** rank sensitivity. Common labels: **public**,
**private**, **sensitive**, **confidential**, **restricted**, and **critical**.
Classification drives everything else — who may see it, how it's stored, how it's
destroyed.

### The three states of data

> Data is always in one of three **states**, and each needs its own protection:
> **at rest** (stored), **in transit** (moving across a network), and **in use**
> (loaded in memory, being processed).

- **At rest** → disk/database encryption.
- **In transit** → TLS/IPsec.
- **In use** → the hardest; techniques like secure enclaves help.

### Where data lives matters

- **Data sovereignty** — data is subject to the laws of the country it physically
  resides in. Storing EU citizens' data may legally require keeping it in the EU.
- **Geolocation / geographic restrictions** — limiting where data can be stored or
  accessed from.

### Methods to secure data

Many you've met already: **encryption**, **hashing**, **masking**,
**tokenization**, **obfuscation**, **segmentation**, **permission restrictions**,
and **geographic restrictions**. Pick by goal — **masking** to show part of a
value to a clerk, **tokenization** to keep real card numbers out of a system
entirely, **encryption** to protect stored or moving data.

### DLP: stopping data from leaking

**Data Loss Prevention (DLP)** tools watch for sensitive data trying to leave —
in email, uploads, or onto USB — and block or alert. DLP is the go-to answer for
"prevent exfiltration of classified data."

## Resilience and recovery: surviving failure

Security isn't only about attackers; it's about staying up when something breaks.

### High availability

- **Load balancing** spreads work across multiple active servers (also boosts
  capacity).
- **Clustering** groups servers so that if one fails, another takes over.
- **Platform diversity** and **multi-cloud** avoid a single vendor or technology
  being a single point of failure.

### Sites for recovery

If your primary site goes down, you fail over to an alternate site:

| Site | Readiness | Cost | Time to recover |
|------|-----------|------|-----------------|
| **Hot** | Fully running, live data | High | Minutes |
| **Warm** | Hardware ready, data stale | Medium | Hours |
| **Cold** | Empty space, power only | Low | Days |

**Geographic dispersion** — keeping sites far apart — ensures one disaster (flood,
quake) can't take out both.

### Backups and power

- **Backups** — copies to restore from. Consider **onsite vs. offsite**,
  **frequency**, **encryption**, **snapshots**, **replication**, and
  **journaling**. The classic guidance is the **3-2-1 rule**: three copies, two
  media types, one offsite.
- **Power** — **UPS** (battery) bridges short outages instantly; **generators**
  carry you through long ones.

### Testing your plans

A plan you've never tested is a guess. Methods, from cheapest to most realistic:

- **Tabletop exercise** — people talk through the plan in a room. No systems
  touched.
- **Simulation** — a practiced, more realistic drill.
- **Parallel processing** — bring the recovery site up *alongside* production to
  prove it works without disrupting live service.
- **Failover** — actually switch to the backup system. The most realistic, and
  the riskiest.

**Capacity planning** (people, technology, infrastructure) and **continuity of
operations (COOP)** round out the picture — making sure you've sized resources for
the load and can keep essential functions running through a disruption.

## The whole thing in one paragraph

Secure design places appliances and principles so infrastructure is defensible:
mind **device placement**, **security zones**, **attack surface**, and **failure
modes** (**fail-open** for availability vs. **fail-closed** for security), know
your appliances (firewall, proxy, load balancer, **jump server**, **IDS**
passive vs. **IPS** inline/active, **WAF**, **NGFW**, **UTM**), and secure access
with **802.1X/EAP**, **VPN** over **TLS/IPsec**, **SD-WAN**, and **SASE**. Protect
**data** by classifying it (public → critical), guarding it in its three **states**
(at rest, in transit, in use), respecting **data sovereignty**, and applying
encryption, masking, tokenization, segmentation, permissions, and **DLP** against
leaks. And plan for failure with **high availability** (load balancing,
clustering, platform diversity, multi-cloud), recovery **sites** (hot/warm/cold)
with **geographic dispersion**, solid **backups** (3-2-1), **UPS/generators**, and
**testing** from tabletop up to full failover.

## On the exam

- **IDS vs. IPS:** IDS **detects/alerts** (passive, tap); IPS **prevents/blocks**
  (active, inline). The word "block" or "inline" points to IPS.
- **Fail-open vs. fail-closed:** open = traffic keeps flowing (availability);
  closed = traffic stops (security). Choose by what the scenario values.
- **Hot/warm/cold sites:** hot = instant and expensive, cold = cheap and slow,
  warm = in between. Match cost vs. recovery time to the scenario.
- **Data states** are a favorite: **at rest** (encrypt the disk), **in transit**
  (TLS), **in use** (hardest to protect).
- **DLP** is the answer for "prevent sensitive data from leaving the
  organization."
- **Data sovereignty** = the law of the country where data physically sits.
- Testing order of realism: **tabletop < simulation < parallel < failover**. A
  tabletop touches no systems; a failover actually switches over.
- **Jump server** is the hardened hop admins use to reach a protected zone.
