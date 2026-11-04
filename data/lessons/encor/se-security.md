# Security: AAA, CoPP, TrustSec, 802.1X & Wireless

## Device access control (management-plane AAA)
Centralize admin authentication/authorization/accounting on a server.
| | **TACACS+** | **RADIUS** |
|--|-------------|------------|
| Purpose | **device administration** | **network access** (802.1X) |
| Transport | **TCP 49** | UDP 1812/1813 |
| Encryption | **entire payload** | **password only** |
| AAA split | separates authN/authZ/acct | combines authN+authZ |
| Per-command authZ | **yes** | limited |

Use **TACACS+** for granular CLI command authorization and full command
accounting; **RADIUS** for authenticating endpoints onto the network.

## CoPP (Control Plane Policing)
Protects the **CPU** from floods/DoS by applying a QoS policy to traffic punted
to the control plane (management, routing, ICMP, exceptions). Transit data in
hardware is unaffected.
```
policy-map COPP
 class MGMT
  police 8000 conform-action transmit exceed-action drop
control-plane
 service-policy input COPP
show policy-map control-plane
```

## 802.1X / NAC
Roles: **supplicant** (endpoint) ↔ **authenticator** (switch/WLC) ↔
**authentication server** (Cisco ISE, RADIUS). EAP runs over LAN (EAPoL) to the
switch; the switch carries EAP inside **RADIUS** to ISE. Fallbacks: **MAB**
(MAC Authentication Bypass) for non-802.1X devices, and **web authentication**.

## Cisco TrustSec (SGT/SGACL)
Classifies traffic with a **Security Group Tag (SGT)** based on identity, and
enforces policy with **SGACLs** — so policy follows the *group*, not the IP or
subnet, decoupling it from topology. Tags propagate inline (in the CMD header) or
via **SXP**. ISE is the policy brain.
```
show cts role-based sgt-map all
show cts environment-data
```

## Wireless security
- **WPA2-Personal** (PSK, 4-way handshake) / **WPA2-Enterprise** (802.1X/EAP).
- **WPA3** adds **SAE** (Simultaneous Authentication of Equals, "Dragonfly") for
  Personal mode — forward secrecy and resistance to offline dictionary attacks —
  and a stronger 192-bit suite for Enterprise.
- **WEP** (RC4) and **Open** auth are insecure/legacy.

## Infrastructure protection extras
**uRPF** drops spoofed sources that fail a reverse-path check; **DAI**, **DHCP
snooping**, **port security** protect Layer 2; **CoPP** protects the CPU.

## Exam cues
- TACACS+ = device admin (TCP 49, full encryption, per-command authZ). RADIUS =
  network access (UDP).
- CoPP protects the CPU/control plane.
- WPA3-Personal = SAE. 802.1X: supplicant/authenticator/ISE with RADIUS.
- TrustSec = SGT classify + SGACL enforce (policy by group, not IP).
