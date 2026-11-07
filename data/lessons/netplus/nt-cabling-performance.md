# Cabling, Service & Performance Issues

This lesson takes the troubleshooting method from the last lesson and applies it to
the three kinds of fault you'll actually diagnose: physical cabling problems, broken
network *services* like DHCP and DNS, and performance complaints like "it's slow."
Each has a recognizable set of symptoms and causes.

## Cabling and physical-layer issues

When connectivity is intermittent, slow, or dead on one run, suspect Layer 1. The
common culprits:

- **Attenuation** — the signal weakens over distance. The usual cause is **exceeding
  the 100 m** copper limit. Symptom: a run works short but fails long.
- **Crosstalk** — signal from one pair bleeds into another (NEXT = near-end
  crosstalk). Caused by untwisting too much pair at termination or poor cable.
- **EMI / interference** — motors, fluorescent lights and power cables corrupt copper
  signals. Fix with shielded cable (STP) or by routing away from the source; fiber is
  immune.
- **Open / short** — a broken conductor (open) or two touching (short); a cable
  tester finds both.
- **Incorrect pinout / TX-RX reversed** — wired to the wrong standard, or a
  straight-through used where a crossover was needed (older gear without Auto-MDIX).
- **Split pairs** — wires paired wrong even though continuity "passes"; causes
  crosstalk at speed.
- **Bad connector / bad cable** — a poorly crimped RJ45 or a damaged cable.
- **Dirty or damaged fiber / wavelength mismatch** — contaminated fiber ends or
  mismatched optics; clean connectors and match transceiver wavelengths.
- **Bad SFP/transceiver** — the module, not the fiber, is dead.
- **PoE issues** — not enough power budget on the switch, or a cable too long/poor to
  carry power.

> **Duplex and speed mismatch** is a classic. If one side is forced to full duplex
> and the other auto-negotiates to half, you get **late collisions** and **CRC
> errors** and miserable throughput — the link "works" but crawls. Set both ends the
> same (auto/auto is usually best).

## Network service issues

Here the cabling is fine but a *service* is misbehaving. These are addressing,
naming, and policy problems.

### DHCP problems

- **No address (APIPA `169.254.x.x`)** — the client couldn't reach a DHCP server.
  Check the server, the scope, and the **relay/`ip helper-address`** if it's across a
  router.
- **Exhausted scope** — all addresses leased out; new clients get nothing. Enlarge the
  scope or shorten the lease.
- **Rogue DHCP server** — an unauthorized server hands out wrong addresses/gateways.
  **DHCP snooping** stops it.
- **Wrong scope options** — clients get an address but the wrong gateway or DNS, so
  they can't get out or can't resolve names.

### DNS problems

> **Can reach by IP but not by name = DNS.** The go-to test from the last lesson:
> `ping 8.8.8.8` works, `ping a-name` fails → the DNS server, the record, or the
> client's DNS setting is wrong.

Causes include a wrong or missing record (A/CNAME/MX), the client pointed at a dead
DNS server, or stale cache (flush it). DNS resolution failures look like "the whole
internet is down" to a user even though routing is perfect.

### Addressing and policy problems

- **Duplicate IP address** — two devices with the same IP; both get intermittent
  connectivity and the OS warns of a conflict. Often a static IP inside a DHCP scope
  (fix with an **exclusion**).
- **Incorrect subnet mask** — the host miscalculates who's local vs remote, so some
  destinations work and others don't.
- **Incorrect default gateway** — local traffic works, but nothing reaches *other*
  networks or the internet.
- **Blocked by firewall / ACL** — the path and names are fine but a rule drops the
  traffic; the tell is that one port/service fails while others work.
- **Expired certificate** or **time (NTP) drift** — TLS fails or Kerberos/logins
  break when clocks disagree.
- **Wrong VLAN assignment** — a port in the wrong VLAN lands the device on the wrong
  subnet entirely.

## Performance issues

Here everything "works" but it's slow or unreliable. Performance problems are about
*degradation*, and you quantify them with the metrics from the operations unit.

- **Latency** — too much delay. Traceroute shows which hop adds it.
- **Jitter** — variation in latency; wrecks VoIP and video (choppy calls) even when
  average latency looks fine.
- **Packet loss** — dropped packets force retransmits and stutter; check interface
  error counters and link quality.
- **Bandwidth saturation / congestion** — the link is simply full. Use **flow data**
  to find the top talker; fix with more bandwidth or **QoS** to prioritize important
  traffic.
- **Bottleneck** — one slow link or device throttles everything behind it.

> **Interface errors point at the cause.** **CRC errors** = corrupted frames, usually
> bad cabling, EMI, or a **duplex mismatch**. **Runts** = frames too small (often
> collisions); **giants** = oversized frames. **Input/output drops** = the interface
> is overrun (congestion). Reading `show interface` counters turns "it's slow" into a
> specific fault.

**Wireless performance** has its own list: **low signal (RSSI)** from distance or
obstructions, **interference** from other APs or non-Wi-Fi sources, **channel
overlap** (remember only **1/6/11** don't overlap on 2.4 GHz), **wrong band** (stuck
on crowded 2.4 GHz instead of 5 GHz), and **too many clients** on one AP. A **Wi-Fi
analyzer** finds overlap and weak coverage; a **spectrum analyzer** finds non-Wi-Fi
interference.

A note on **MTU**: if packets are too large for a link and fragmentation is blocked,
you get odd failures where small transfers work but large ones hang — an **MTU/MSS
mismatch**, common over tunnels and VPNs.

## On the exam

- Cabling: **attenuation** = too long (>100 m), **crosstalk/EMI** = interference,
  open/short/pinout from a cable tester; **duplex/speed mismatch → CRC errors + late
  collisions + slow link**; bad SFP, dirty fiber, PoE budget.
- DHCP: **APIPA = no server reached**, exhausted scope, **rogue server (use DHCP
  snooping)**, wrong options. DNS: **reach by IP but not name = DNS.**
- Addressing: **duplicate IP** (conflict), wrong **mask** (some destinations fail),
  wrong **gateway** (no remote/internet access), firewall/ACL block, cert/NTP time
  issues, wrong VLAN.
- Performance: latency, **jitter** (hurts voice), packet loss, saturation (find the
  top talker with flow data, fix with QoS). **CRC = bad cable/duplex; runts/giants/
  drops** tell the story in `show interface`.
- Wireless: low signal, interference, **channel overlap (1/6/11)**, wrong band; use a
  Wi-Fi/spectrum analyzer. Watch for **MTU/MSS** issues over tunnels/VPNs.
