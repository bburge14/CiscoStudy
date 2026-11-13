# Network Defense & Wireless Security

Having seen how networks are attacked, we now build the defenses: the devices that
filter and inspect traffic, the architecture that contains a breach, the tunnels
that protect data in transit, and the special controls that wireless demands.
These are the bread-and-butter tools an SSCP configures and monitors every day.

## Firewalls: controlling what gets through

A **firewall** enforces a traffic policy between network zones. They've evolved
through generations, and the exam expects you to tell them apart:

| Type | How it decides |
|------|----------------|
| **Packet filter** | Allows/blocks by IP, port, protocol — **stateless**, no connection awareness |
| **Stateful inspection** | Tracks active connections in a **state table**; permits return traffic only for sessions it already saw |
| **Proxy (application) firewall** | Terminates and inspects traffic at the application layer on behalf of clients |
| **Next-Generation Firewall (NGFW)** | Adds deep packet inspection, application awareness, and integrated IPS/identity |
| **WAF (Web Application Firewall)** | Specifically filters HTTP(S) to block web attacks like SQLi and XSS |

> A **stateful inspection firewall** maintains a **state table** of active
> connections and permits inbound return traffic only if it belongs to a session
> that was already established from inside. That connection awareness is the key
> difference from a stateless packet filter.

## IDS and IPS: detecting and blocking intrusions

> An **IDS (Intrusion Detection System)** monitors traffic and **alerts** on
> suspicious activity but does **not** block it — it sits *out of band*. An **IPS
> (Intrusion Prevention System)** sits **inline** and actively **blocks or drops**
> malicious traffic in real time, before it reaches the target.

The one-word difference is **inline**: an IPS is placed directly in the traffic
path so it can stop an attack, whereas an IDS only watches a copy and raises an
alarm. Both detect using **signatures** (known patterns) and/or **anomaly/
behavioral** analysis (deviation from a baseline), with the trade-offs you saw in
the monitoring lesson.

## Segmentation: containing the blast radius

You don't want one compromised host to mean a compromised network. **Network
segmentation** divides the network into isolated zones:

> Separating systems into **VLANs/subnets** provides two security benefits:
> it **reduces the size and scope of broadcast domains**, and it **limits an
> attacker's lateral movement**, containing a breach to a single segment.

Key constructs:

- **DMZ (demilitarized zone / screened subnet)** — a buffer segment for
  internet-facing servers (web, mail), isolated from the internal LAN so a
  compromised public server can't directly reach internal systems.
- **Microsegmentation** — fine-grained isolation down to individual workloads, a
  cornerstone of **zero trust** ("never trust, always verify," no implicit trust
  from network location).
- **NAC (Network Access Control)** — checks a device's identity and health posture
  before admitting it to the network.

## VPNs and secure tunnels

A **VPN (Virtual Private Network)** protects **data in transit** across untrusted
networks by encrypting it in a tunnel. The two workhorses:

> **IPsec** secures IP traffic and is the basis of most site-to-site VPNs. It has
> two protocols: **AH (Authentication Header) = IP protocol 51**, providing
> integrity and authentication but **no encryption**; and **ESP (Encapsulating
> Security Payload) = IP protocol 50**, providing **confidentiality** (encryption)
> plus integrity. Keys are negotiated by **IKE**.

Note those are **IP protocol numbers**, not TCP/UDP ports (ESP = 50, AH = 51).
IPsec runs in **transport mode** (protects the payload, host-to-host) or **tunnel
mode** (protects the entire original packet, gateway-to-gateway — the usual VPN
mode). The other common tunnel is **TLS** (SSL VPNs and HTTPS), which secures
traffic at the transport/application layer and is what the padlock in your browser
represents.

## Wireless security

Wi-Fi broadcasts into the air, so anyone nearby can listen — encryption and
authentication are essential. Know the protocol lineage:

| Standard | Status |
|----------|--------|
| **WEP** | Badly broken (RC4, weak IV) — never use |
| **WPA** | Interim fix (TKIP) — deprecated |
| **WPA2** | AES-**CCMP**; strong but the PSK 4-way handshake is vulnerable to offline cracking of captured handshakes |
| **WPA3** | Current standard — replaces PSK with **SAE** and mandates **PMF** |

> **WPA3** replaces WPA2's pre-shared-key handshake with **SAE (Simultaneous
> Authentication of Equals)**, which resists **offline dictionary attacks** and
> adds **forward secrecy**. WPA3 also makes **Protected Management Frames (PMF)**
> mandatory, blocking forged deauthentication attacks. WPA3-Personal still uses
> AES-CCMP; WPA3-Enterprise offers an optional 192-bit (GCMP-256) mode.

For enterprise Wi-Fi, don't share one passphrase — authenticate each user:

> **IEEE 802.1X** is **port-based network access control** that authenticates each
> device/user (often via certificates) against a central **RADIUS** server using
> **EAP**. This is "WPA2/WPA3-Enterprise," versus the single shared passphrase of
> "Personal" mode.

Other wireless concerns: disabling or not relying on **SSID** hiding (it's not
security), watching for **rogue APs / evil twins**, **OWE** (Opportunistic
Wireless Encryption) for open networks, and the attack surface of **Bluetooth**
(bluejacking/bluesnarfing) and **cellular** (rogue base stations / IMSI
catchers in 4G/5G).

## Exam focus

- **Stateful firewall** tracks connections in a **state table** (permits return
  traffic for established sessions); a **packet filter** is stateless. Know
  **proxy**, **NGFW**, and **WAF** (web attacks).
- **IDS detects/alerts out of band; IPS blocks inline.** The differentiator is
  **inline**.
- **Segmentation (VLANs/subnets)** shrinks broadcast domains and **limits lateral
  movement**. A **DMZ** isolates internet-facing servers; **microsegmentation**
  and **zero trust** push isolation to the workload.
- **IPsec: ESP = IP protocol 50 (encryption + integrity), AH = IP protocol 51
  (integrity/auth, no encryption)**; **tunnel mode** for gateway VPNs, **transport
  mode** host-to-host; **IKE** negotiates keys. **TLS** secures HTTPS/SSL VPNs.
- Wireless: **WEP broken**; **WPA2 = AES-CCMP**; **WPA3 = SAE + mandatory PMF**,
  resisting offline dictionary attacks. **802.1X** with **EAP/RADIUS** = enterprise
  per-user authentication.
