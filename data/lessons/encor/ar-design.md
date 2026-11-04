# Enterprise Design, High Availability & Fabric

## Hierarchical campus design
- **Access** — connects endpoints; port security, PoE, VLANs, 802.1X.
- **Distribution** — aggregation point for **routing, policy, filtering, and
  redistribution**; the boundary between L2 access and L3 core.
- **Core** — high-speed transport between distribution blocks. Keep it **simple
  and fast** — no policy/ACLs that add latency.

A **collapsed core** merges core and distribution for smaller sites. **Spine-leaf**
(every leaf connects to every spine, no leaf-to-leaf) gives predictable,
low-latency east-west paths in the data center.

## High availability
- **StackWise / StackWise Virtual (and legacy VSS)** combine chassis into **one
  logical switch** with a single control plane, enabling a **Multichassis
  EtherChannel (MEC)** to a downstream device and removing STP-blocked uplinks.
- **NSF/SSO, GIR, ISSU** keep forwarding alive across control-plane switchovers
  and upgrades.

### FHRPs (gateway redundancy)
| | Vendor | Roles | Native load balancing |
|--|--------|-------|-----------------------|
| HSRP | Cisco | Active/Standby | No (use multiple groups) |
| VRRP | IETF (open) | Master/Backup | No (use multiple groups) |
| **GLBP** | Cisco | AVG + up to 4 AVFs | **Yes** (multiple vMACs) |

Chassis virtualization (StackWise/VSS) is **not** the same as a gateway FHRP —
one merges control planes, the other shares a virtual gateway between separate
routers.

## Cisco SD-Access fabric
A VXLAN overlay on a routed underlay, with planes:
- **Control plane = LISP** — the control-plane node is the LISP
  **Map-Server/Map-Resolver** holding **EID→RLOC** mappings.
- **Data plane = VXLAN** — carries user traffic (with the VNI and SGT).
- **Policy = Cisco TrustSec / SGTs**.

Fabric node roles: **edge** (connects endpoints, registers EIDs), **border**
(fabric-to-external exit), **control** (LISP map database). The **WLC** integrates
wireless into the fabric.

## AI/ML in assurance
Catalyst Center and DNA/AI analytics baseline normal behaviour and flag
anomalies; "AI endpoint analytics" and ML-driven RRM tune wireless. At this
level, know the *purpose* (data-driven assurance/automation), not internals.

## Exam cues
- Policy belongs at **distribution**, not the core.
- StackWise Virtual/VSS = one logical switch + MEC (not an FHRP).
- SD-Access: LISP=control, VXLAN=data, TrustSec=policy; edge/border/control nodes.
