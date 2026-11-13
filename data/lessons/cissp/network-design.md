# Secure Network Design & Components

Communication and network security is a big, concrete domain, but CISSP tests it at
the level of a *designer and overseer*, not a packet jockey. You need the layered
mental model (OSI and TCP/IP), the principles of segmenting and defending a
network, and the role each component plays. This lesson builds that map; the next
covers the secure protocols and the attacks.

## The OSI model

The **OSI model** is the seven-layer reference every network question leans on.
Learn what *operates* at each layer, because the exam identifies attacks and
devices by layer.

| Layer | Name | Operates here | Data unit |
|-------|------|---------------|-----------|
| 7 | Application | HTTP, DNS, SMTP | Data |
| 6 | Presentation | Encryption, formatting (TLS often placed here) | Data |
| 5 | Session | Session setup/teardown | Data |
| 4 | Transport | **TCP/UDP, ports** | Segment |
| 3 | Network | **IP addressing, routers** | Packet |
| 2 | Data Link | **MAC addresses, switches** | Frame |
| 1 | Physical | Cabling, hubs, signals | Bits |

> The highest-yield mapping: **routers and IP = Layer 3 (Network)**; **switches and
> MAC addresses = Layer 2 (Data Link)**; **TCP/UDP and port numbers = Layer 4
> (Transport)**. If a stem says "forwards based on IP," it's Layer 3.

As data moves down the stack it is **encapsulated** (each layer adds its header);
it is de-encapsulated on the way up. The **TCP/IP model** collapses OSI into four
layers (Application, Transport, Internet, Link) but maps onto the same ideas.

## Addressing and ports

**Private IP ranges (RFC 1918)** — 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 — are
not routable on the internet and are translated by **NAT** to conserve public
addresses and hide internal structure. **IPv6** removes the address shortage and
builds in features NAT once provided.

A handful of **well-known ports** recur on the exam:

| Port | Service | Port | Service |
|------|---------|------|---------|
| 22 | SSH / SFTP | 443 | HTTPS |
| 23 | Telnet (insecure) | 389 / 636 | LDAP / LDAPS |
| 25 | SMTP | 3389 | RDP |
| 53 | DNS | 500 | IKE (IPsec) |
| 80 | HTTP | 161/162 | SNMP |

## Principles of secure network design

Design the network so that a single breach doesn't become a free-for-all.

- **Defense in depth** — layer independent controls so no single failure is fatal.
- **Segmentation** — divide the network into zones (by sensitivity or function) so
  compromise in one doesn't spread. **VLANs** segment at Layer 2; subnets and
  firewalls enforce boundaries.
- **DMZ / screened subnet** — a buffer zone for internet-facing services (web,
  mail) between the untrusted internet and the trusted internal network.
- **Zero trust and microsegmentation** — never trust by location; verify every
  request and segment down to the workload. This limits **east-west** (internal)
  movement, not just **north-south** (in/out) traffic.
- **Network Access Control (NAC)** — checks device posture (patch level, identity)
  before admitting it to the network.
- **Software-Defined Networking (SDN)** — separates the control plane from the data
  plane for centralized, policy-driven management.

> A risk-manager framing shows up here: the BEST network defense is usually
> **segmentation plus least privilege between zones**, so that a compromised host
> can't reach the crown jewels — not a single bigger firewall at the edge.

## Network components

Know what each device does and, for firewalls, how they differ.

**Firewalls**, from simplest to smartest:

- **Packet filter (stateless)** — allows/denies by IP, port, protocol; no memory of
  connections.
- **Stateful inspection** — **tracks the state of active connections**, so return
  traffic for a session a user initiated is allowed while unsolicited inbound is
  denied. This is the default enterprise firewall.
- **Proxy / application-layer** — terminates and inspects traffic at Layer 7 on
  behalf of clients.
- **Next-Generation Firewall (NGFW)** — adds application awareness, IPS, and
  identity.
- **Web Application Firewall (WAF)** — specifically filters HTTP to block web
  attacks (injection, XSS).

> If a stem describes allowing return traffic for a connection the user started
> while blocking unsolicited inbound, the answer is a **stateful inspection
> firewall** — not a stateless packet filter.

**Detection and other components:**

- **IDS** detects and alerts; **IPS** detects and **blocks** inline. Each can be
  **signature-based** (known patterns, misses novel attacks) or **anomaly/behavior-
  based** (flags deviations, more false positives). **NIDS** watches the network;
  **HIDS** watches a host.
- **Router** (Layer 3 forwarding), **switch** (Layer 2), **proxy**, **load
  balancer** (distributes traffic, adds resilience), **VPN concentrator**.

**Wireless** security has a clear hierarchy: **WEP** is broken, **WPA** is weak,
**WPA2** is acceptable, and **WPA3** (with SAE replacing the pre-shared-key
handshake) is current and preferred. Enterprise Wi-Fi uses **802.1X** for per-user
authentication rather than a shared passphrase.

## Exam focus

- OSI layer mapping: **L3 = IP/routers, L2 = MAC/switches, L4 = TCP/UDP/ports.**
  Data is **encapsulated** going down the stack.
- **RFC 1918** private ranges are translated by **NAT**. Know the well-known ports
  (22 SSH, 443 HTTPS, 53 DNS, 389/636 LDAP/LDAPS, 3389 RDP).
- Secure design = **defense in depth + segmentation**. **VLANs** segment at L2; a
  **DMZ/screened subnet** isolates internet-facing services; **zero trust /
  microsegmentation** limits **east-west** movement; **NAC** checks posture before
  admission.
- A **stateful inspection firewall** tracks connections to allow return traffic
  (vs stateless packet filtering). **IDS alerts, IPS blocks**;
  **signature** (known) vs **anomaly** (behavioral) detection.
- Wireless: **WEP < WPA < WPA2 < WPA3**; use **WPA3** / **802.1X** for enterprise.
