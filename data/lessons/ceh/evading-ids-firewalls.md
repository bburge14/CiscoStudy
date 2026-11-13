# Evading IDS, Firewalls & Honeypots

To understand how attackers slip past the perimeter, you first have to understand
what the perimeter *is*. This lesson covers the three defensive technologies —
intrusion detection, firewalls, and honeypots — and then the **classes** of
evasion an assessor must be aware of. We teach evasion conceptually: enough to
recognize the technique and, more importantly, to harden the defense against it.

## The perimeter technologies

### IDS and IPS

> An **IDS (Intrusion Detection System)** monitors traffic and **alerts** on
> suspicious activity. An **IPS (Intrusion Prevention System)** sits **inline** and
> can **block** it.

- **NIDS** watches the network; **HIDS** watches a single host.
- Detection methods: **signature-based** (matches known patterns — accurate for
  known attacks, blind to new ones) and **anomaly / behavior-based** (flags
  deviations from a baseline — can catch novel attacks but generates more false
  positives).

### Firewalls

Firewalls enforce a traffic policy. Know the progression:

| Type | What it inspects |
|------|------------------|
| **Packet filter** | Individual packets (IP, port, protocol) |
| **Stateful inspection** | Connection state, tracking sessions |
| **Proxy / application** | Full application-layer content on behalf of clients |
| **Next-Gen Firewall (NGFW)** | Adds app awareness, IPS, identity, threat intel |
| **WAF** | Specifically HTTP/S traffic to protect web applications |

### Honeypots

> **A honeypot is a decoy system deliberately exposed to attract and study
> attackers and to detect malicious activity, while holding no real production
> value.** Because nothing legitimate should ever touch it, *any* interaction is
> suspicious by definition.

Honeypots come in **low-interaction** (emulated services, safer, less insight) and
**high-interaction** (real systems, richer insight, higher risk) flavors. A network
of honeypots is a **honeynet**. They are a low-noise detective control — and
attackers, in turn, try to *detect and avoid* honeypots so they do not waste effort
or reveal themselves.

## Evasion, by class

Attackers aim to get malicious traffic past an IDS or firewall without triggering
it. The exam tests the *category*, not a recipe.

- **Fragmentation** — splitting attack traffic into many **tiny IP fragments**,
  hoping the IDS fails to reassemble and inspect them while the **target still
  reassembles** the full packet. *(Session splicing is the TCP-segment equivalent.)*
- **Obfuscation / encoding** — encoding a payload (e.g. alternate character
  encodings) so it no longer matches a signature.
- **Encryption and tunneling** — hiding traffic inside an encrypted or allowed
  channel the IDS cannot read.
- **Timing / "low and slow"** — pacing activity to stay under detection thresholds.
- **Spoofing and decoys** — forging source addresses or generating many fake source
  IPs so the real one is lost in the noise.
- **Polymorphism** — constantly changing the payload's form to defeat static
  signatures.

> The common thread: evasion exploits a *difference in interpretation* between the
> defender's sensor and the target host. If the IDS and the host do not reassemble
> and normalize traffic the same way, there is a gap to hide in.

## Hardening against evasion

- **Traffic normalization / reassembly at the IDS** — reassemble fragments and
  streams the same way the target will, closing the interpretation gap that
  fragmentation and splicing rely on.
- **Keep signatures current and tune the sensor** — reduce both false positives and
  the false *negatives* evasion seeks.
- **Decrypt-and-inspect where lawful and appropriate** (e.g. TLS inspection at the
  edge) so encryption is not a free pass.
- **Anomaly-based detection** alongside signatures — to catch obfuscated and novel
  traffic that no signature matches.
- **Defense-in-depth** — assume the perimeter can be evaded and layer endpoint
  detection, segmentation and logging behind it.
- **Deception technology** (honeypots, honeytokens) — turn the attacker's need to
  probe against them.

## Signature vs anomaly, in practice

The two detection philosophies trade off in a predictable way. **Signature-based**
detection is precise and low-noise for *known* attacks but blind to anything new —
it is only as current as its signature feed. **Anomaly-based** detection can catch
novel and obfuscated attacks because it flags deviation from a learned baseline, but
it produces more **false positives** and needs careful tuning. Serious deployments
run both, so each covers the other's blind spot.

## Placement and tuning matter

An IDS only sees what reaches it. Sensors are placed at **choke points** — the
network edge, segment boundaries, and in front of critical assets — and a **SPAN
port or network tap** feeds them a copy of the traffic. A poorly tuned sensor is
worse than none: alert fatigue from constant false positives trains analysts to
ignore it, which becomes its own kind of evasion.

The broader principle is to never treat the perimeter as a single wall. **Network
segmentation**, endpoint detection, and good logging behind the IDS mean that an
attacker who slips one sensor still meets another control — defense-in-depth turns a
single evasion into a dead end rather than a free pass.

## Exam focus

- **IDS alerts; IPS blocks (inline).** **NIDS** = network, **HIDS** = host.
  **Signature** detection catches known attacks; **anomaly** detection catches
  deviations from baseline.
- **Fragmentation** is the classic IDS-evasion technique: tiny IP fragments the IDS
  may not reassemble while the target does. The defense is **IDS traffic
  normalization/reassembly**.
- A **honeypot** is a **decoy with no production value**; any interaction is
  inherently suspicious. A **honeynet** is a network of them.
- Firewall types in order of sophistication: **packet filter → stateful → proxy →
  NGFW**; a **WAF** protects web apps specifically.
- Evasion classes to recognize: **fragmentation, obfuscation/encoding, encryption/
  tunneling, timing, spoofing/decoys, polymorphism** — all exploit a defender/host
  interpretation gap, closed by **normalization, updated signatures, anomaly
  detection, and defense-in-depth**.
