# OSPF, EIGRP & BGP

## OSPF (advanced)
### LSA types
| Type | Name | Originator | Scope |
|-----:|------|------------|-------|
| 1 | Router | every router | within an area (intra-area) |
| 2 | Network | the **DR** on multiaccess | within an area |
| 3 | Summary | **ABR** | into other areas (inter-area, O IA) |
| 4 | ASBR summary | ABR | locates the ASBR |
| 5 | External | **ASBR** | whole domain (O E1/E2) |
| 7 | NSSA external | ASBR in an NSSA | within NSSA, ABR translates 7→5 |

### Area types
- **Stub** — blocks Type 5; ABR injects a default. No ASBR allowed.
- **Totally stubby** — blocks Type 5 **and** Type 3; default only.
- **NSSA** — blocks ordinary Type 5 but allows a local ASBR via **Type 7**
  (ABR translates to Type 5 for the rest of the domain).

### Cost
`cost = reference-bw / interface-bw`, min 1; default reference 100 Mbps floors
Gig/10-Gig to 1. Set `auto-cost reference-bandwidth 10000` identically everywhere.

## EIGRP
Advanced distance-vector using **DUAL**. Metric (by default) is based on
**bandwidth and delay**. Terms:
- **Feasible Distance (FD)** — the best metric to a destination.
- **Reported Distance (RD)** — a neighbor's metric to that destination.
- **Successor** — the next hop with the lowest FD (installed route).
- **Feasible Successor (FS)** — a backup that satisfies the **Feasibility
  Condition: RD < FD**, guaranteeing a loop-free backup used instantly if the
  successor fails. No FS → the route goes **Active** and DUAL recomputes.

## BGP
Path-vector EPG between autonomous systems; **eBGP AD 20, iBGP AD 200**.
### Best-path order (top wins)
1. **Weight** (Cisco-only, highest, local to router)
2. **Local Preference** (highest, AS-wide)
3. Locally **originated** (network/aggregate/redistribute)
4. Shortest **AS-Path**
5. Lowest **Origin** (IGP < EGP < Incomplete)
6. Lowest **MED**
7. **eBGP over iBGP**
8. Lowest **IGP metric** to the next hop
9. Oldest eBGP / lowest **router-ID** / lowest neighbor IP

Mnemonic: **W**e **L**ove **O**ranges **A**S **O**ranges **M**ean **P**ure
**R**efreshment.

### iBGP next-hop gotcha
iBGP does **not** change the next-hop by default, so if the IGP can't reach that
next-hop the path is valid-but-not-best and marked inaccessible. Fix with
`neighbor x.x.x.x next-hop-self` or by advertising the link into the IGP. iBGP
also needs a full mesh (or route reflectors) because it won't re-advertise
iBGP-learned routes to other iBGP peers.

## Verify
```
show ip ospf database
show ip eigrp topology
show bgp ipv4 unicast
show ip route
```

## Exam cues
- ABR → Type 3; ASBR → Type 5; NSSA → Type 7 (7→5 at ABR).
- EIGRP FS: **RD < FD**.
- BGP: Weight→LocalPref→AS-Path…; iBGP next-hop must be IGP-reachable.
