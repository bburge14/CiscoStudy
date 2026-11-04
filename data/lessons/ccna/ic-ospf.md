# OSPFv2 Operation

OSPF is a **link-state** IGP (AD 110). Routers flood LSAs, build an identical
link-state database per area, and run SPF (Dijkstra) to compute shortest paths.

## Enabling OSPF
```
router ospf 1                       ! process ID is LOCAL only — need not match neighbors
 router-id 1.1.1.1
 network 10.1.12.0 0.0.0.3 area 0   ! wildcard mask selects the interfaces
 passive-interface Gi0/2            ! form no neighbors here, still advertise it
```
The `network` statement uses a **wildcard mask** to match interface IPs; the
matched interfaces are activated in the stated area.

## Router-ID selection
1. Explicit `router-id` command, else
2. Highest IP on an **up loopback**, else
3. Highest IP on any **up interface**.

Loopbacks win because they never flap. Changing the RID needs
`clear ip ospf process` to take effect.

## Neighbor states (the troubleshooting goldmine)
| State | Meaning / stuck-here cause |
|-------|----------------------------|
| Down | No hellos yet |
| **INIT** | Hellos received but not yet bidirectional (one-way) |
| **2-WAY** | Bidirectional; **DROTHER↔DROTHER stays here on purpose** |
| EXSTART / EXCHANGE | Electing master/slave + exchanging DBDs — **stuck here = MTU mismatch** |
| LOADING | Requesting missing LSAs |
| **FULL** | Fully adjacent (with DR/BDR, or on point-to-point) |

**Must match to form a neighbor:** area, hello/dead timers, subnet + mask,
authentication, stub flags, and compatible MTU (to reach FULL). **Must differ:**
router-id (unique). **Don't care:** process ID.

## DR / BDR on broadcast networks
To cut flooding on multiaccess segments, routers elect a **DR** and **BDR**.
Non-DR/BDR routers (**DROTHERs**) form FULL adjacencies only with the DR/BDR and
stay in **2-WAY** with each other — that is normal, not a fault. Election:
highest **OSPF interface priority** (default 1; `0` = never DR), tiebreak highest
router-id.

## OSPF cost
`cost = reference-bandwidth / interface-bandwidth`, minimum 1. Default reference
is **100 Mbps (10^8)**, so FastEthernet, Gig and 10-Gig all floor to cost 1.
Raise it network-wide so faster links are preferred:
```
router ospf 1
 auto-cost reference-bandwidth 10000   ! 10 Gbps, in Mbps; set identically everywhere
```

## Troubleshooting map
- **No neighbor at all** → mismatched area / hello-dead / subnet / auth, or
  interface is passive or down.
- **Stuck EXSTART/EXCHANGE** → MTU mismatch (`show ip ospf interface`,
  `show interfaces | include MTU`); fix MTU or `ip ospf mtu-ignore`.
- **2-WAY between DROTHERs** → expected behaviour.

## Verify
```
show ip ospf neighbor
show ip ospf interface g0/0
show ip protocols
show ip route ospf
```

## Exam cues
- Process ID local; router-id unique; area/timers/subnet/MTU must match.
- EXSTART = MTU. INIT = one-way hello. 2-WAY DROTHER = normal.
- Gig/10Gig both cost 1 at default reference — raise `auto-cost`.
