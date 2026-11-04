# First-Hop Redundancy Protocols (HSRP)

## The problem
A host has **one** default gateway. If that router dies, the host is cut off
even when a second router exists. FHRPs let two or more routers share a single
**virtual IP (vIP)** and **virtual MAC (vMAC)** so the hosts never have to change
their gateway.

## HSRP (Cisco)
One router is **Active** (forwards for the vIP), one is **Standby**, the rest
**Listen**.
```
interface Vlan10
 ip address 10.0.0.2 255.255.255.0
 standby version 2
 standby 10 ip 10.0.0.1          ! the virtual IP (the hosts' gateway)
 standby 10 priority 110         ! default 100; higher wins
 standby 10 preempt              ! let a higher-priority router reclaim Active
```

### Priority and preempt — the exam's favorite
- Highest **priority** becomes Active (default 100).
- **Preempt** lets a higher-priority router *take back* Active when it returns.
  **Without preempt**, whoever is Active stays Active even if a higher-priority
  router comes back online.
- **Interface/object tracking** can decrement priority when an uplink fails, so
  the standby takes over:
  `standby 10 track 1 decrement 20`.

### Virtual MAC
- HSRPv1 vMAC: `0000.0C07.ACxx` (xx = group in hex).
- HSRPv2 vMAC: `0000.0C9F.Fxxx` (xxx = group). v2 also supports groups 0–4095
  and millisecond timers.

## HSRP vs VRRP vs GLBP
| | Vendor | Roles | Load balancing |
|--|--------|-------|----------------|
| HSRP | Cisco | Active/Standby | Only via multiple groups |
| VRRP | Open (IETF) | Master/Backup | Only via multiple groups |
| GLBP | Cisco | AVG + AVFs | **Native** (hands out different vMACs) |

Only **GLBP** load-balances across gateways by default (the AVG answers ARP with
up to four different virtual MACs).

## Verify
```
show standby brief
show standby
show glbp brief
```

## Exam cues
- Higher priority + **preempt** = reclaims Active; no preempt = incumbent keeps it.
- vMAC HSRPv2 = 0000.0C9F.Fxxx.
- Native load balancing → GLBP.
