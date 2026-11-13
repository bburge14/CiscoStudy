# Denial-of-Service

Confidentiality and integrity get most of the attention, but availability is a
target too. A denial-of-service attack does not steal data — it makes a service
*unusable*, which for an online business can be just as damaging. This lesson
sorts the attack classes by how they exhaust a victim and pairs each with the
control that absorbs or filters it.

## DoS vs DDoS

> **A Denial-of-Service (DoS) attack overwhelms a system so it cannot serve
> legitimate users. A Distributed Denial-of-Service (DDoS) attack does the same
> from many sources at once**, typically a **botnet** of compromised machines
> under command-and-control.

DoS attacks the **availability** leg of the CIA triad. Distribution matters
because it multiplies firepower and makes simple "block the one bad IP" defenses
useless — the traffic comes from thousands of addresses.

## The three attack classes

CEH groups DoS/DDoS techniques by *what resource they exhaust*.

| Class | Exhausts | Examples |
|-------|----------|----------|
| **Volumetric** | Bandwidth | UDP flood, ICMP flood, Smurf, amplification/reflection |
| **Protocol / state** | Connection tables, device state | SYN flood, teardrop, ping of death |
| **Application (Layer 7)** | Server CPU/threads | HTTP flood, Slowloris |

### Volumetric attacks

These simply fill the pipe. The most important concept is **amplification
(reflection)**:

> In an **amplification/reflection attack**, the attacker sends **small queries
> with the victim's IP spoofed as the source** to servers that reply with much
> **larger** responses — so the servers unwittingly flood the victim. DNS and NTP
> are classic amplifiers.

The "amplification factor" is why a modest attacker can generate an enormous flood:
a tiny request triggers a huge answer, all aimed at the spoofed victim.

The classic **Smurf** attack is ICMP amplification: the attacker sends an ICMP
echo to a network's **broadcast address** with the victim's IP spoofed as the
source, so every host on the segment replies to the victim at once.

### Protocol / state-exhaustion attacks

These abuse how protocols keep state. The headline example:

> A **SYN flood** sends a flood of TCP **SYN** packets with spoofed sources and
> **never completes the handshakes**, exhausting the server's table of half-open
> connections so it can no longer accept real ones.

Others are legacy malformed-packet attacks like **teardrop** and **ping of
death**, which crash or hang a target with malformed fragments rather than sheer
volume.

### Application-layer attacks

These are the stealthiest. **HTTP floods** send seemingly valid requests, and
**Slowloris**-style "low and slow" attacks hold many connections open by sending
data very slowly — tying up server workers with **very little bandwidth**, which
makes them hard to distinguish from real users.

## Defending against DoS/DDoS

No single box stops a large DDoS; defense is layered and often upstream:

- **SYN cookies** — defeat SYN floods by not allocating state until the handshake
  completes.
- **Rate limiting and connection limits** — cap abusive sources.
- **Upstream / ISP filtering and blackhole (sinkhole) routing** — drop attack
  traffic before it reaches your link.
- **DDoS scrubbing services and CDNs** — absorb and filter volumetric floods with
  massive capacity and **anycast** to spread the load across many sites.
- **Ingress/egress filtering (BCP 38)** — stops source-address **spoofing** at the
  network edge, cutting off reflection attacks at the source.
- **Disable or secure services that can be abused as amplifiers** (open DNS
  resolvers, exposed NTP `monlist`).
- **Web Application Firewall (WAF)** and behavioral analysis — for Layer 7 floods.
- **Over-provisioning and autoscaling** — buy headroom to ride out spikes.

> The defining idea: volumetric and protocol attacks are usually best handled
> **upstream** (scrubbing, filtering, anycast), while application-layer attacks need
> **smarter inspection** close to the app.

## Botnets: where the firepower comes from

A large DDoS is rarely one machine. Attackers assemble a **botnet** of compromised
devices — increasingly **IoT** gear with default credentials (the Mirai pattern) —
and direct them from a **command-and-control** server. The rise of **"booter" /
"stresser"** services has turned DDoS into a rentable commodity: someone with no
skill can pay to point thousands of bots at a target. Understanding this is itself a
defense, because it explains why blocking a single source never works and why
**upstream, capacity-based mitigation** is the only approach that scales.

A related variant, **permanent DoS (PDoS, or "phlashing")**, damages a device's
firmware so badly it must be replaced rather than rebooted — a reminder that
availability attacks can cross into physical harm.

## Spotting an attack in progress

Defenders distinguish a DDoS from a legitimate traffic spike by its signature:
traffic from an unusual geographic spread, one request type repeated endlessly,
protocol anomalies, or a sudden flood aimed at a single service. **Baseline
monitoring** is what makes the abnormal visible — you cannot recognize abnormal
traffic without first knowing what normal looks like.

## Exam focus

- **DoS vs DDoS**: distributed means **many sources**, usually a **botnet** under
  C2. DoS attacks **availability**.
- **SYN flood** = spoofed SYNs that never finish the handshake, exhausting the
  **half-open connection table**; the fix is **SYN cookies** (plus rate limiting).
- **Amplification/reflection** = small spoofed query → large reply aimed at the
  victim (**DNS, NTP**; **Smurf** = spoofed ICMP to a broadcast). The source-side
  fix is **anti-spoofing / BCP 38**;
  **scrubbing** absorbs it.
- Know the three classes: **volumetric** (bandwidth; UDP/ICMP flood, **Smurf**),
  **protocol/state** (SYN flood, teardrop), **application/Layer 7** (HTTP flood, **Slowloris** — low bandwidth, hard
  to spot).
- Upstream defenses (**scrubbing services, CDNs, anycast, ISP blackholing**) absorb
  large floods; a **WAF** helps with app-layer attacks.
