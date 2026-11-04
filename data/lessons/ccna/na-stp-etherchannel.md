# Spanning Tree & EtherChannel

## Why STP exists
A Layer 2 loop has no TTL, so a broadcast storm melts the network. STP
(802.1D, and today Rapid-PVST+ / 802.1w) blocks redundant ports to leave one
loop-free active path, then re-opens them if a link fails.

## Root bridge election
Every switch has a **Bridge ID = Bridge Priority + VLAN (sys-id-ext) + MAC**.
The switch with the **lowest Bridge ID wins** the root election.

1. Compare **priority** first (default 32768; must be a multiple of 4096).
   Lower wins.
2. **Only if priorities tie**, compare the **MAC address** — lower wins.

> The #1 trap: a tiny MAC address dangled next to a switch that actually has a
> *higher priority*. Priority decides first; MAC is just the tiebreaker.

Influence the election:
```
spanning-tree vlan 10 root primary      ! macro → 24576 (or 4096 below current root)
spanning-tree vlan 10 root secondary    ! macro → 28672
spanning-tree vlan 10 priority 24576    ! explicit (multiples of 4096 only)
```

## Port roles (Rapid-PVST+)
- **Root port** — the one best path *toward* the root on each non-root switch
  (lowest root path cost). Forwards.
- **Designated port** — best path *away* from the root on each segment (one per
  segment, and all root-bridge ports are designated). Forwards.
- **Alternate port** — a blocked backup to the **root port** (alternate path to root).
- **Backup port** — a blocked backup for a **designated port** on the same segment.

Path cost is by link speed (10 Gb=2, 1 Gb=4, 100 Mb=19, 10 Mb=100 — long/legacy
values differ, know the relative order).

## STP protection on access ports
```
interface Gi0/5
 spanning-tree portfast             ! skip listening/learning on an access port
 spanning-tree bpduguard enable     ! err-disable if ANY BPDU arrives (rogue switch)
```
- **PortFast** — host ports go straight to forwarding.
- **BPDU Guard** — err-disables a PortFast port that receives a BPDU (stops a
  rogue switch hijacking the topology).
- **Root Guard** — on a designated port; a *superior* BPDU puts it in
  root-inconsistent (blocking) until the offender stops.

## EtherChannel
Bundles 2–8 links into one logical interface — one STP instance, full
bandwidth, fast failover. Negotiation protocols and modes:

| Protocol | Modes | Initiates? |
|----------|-------|------------|
| **LACP** (802.3ad, standard) | `active`, `passive` | active initiates; passive only responds |
| **PAgP** (Cisco) | `desirable`, `auto` | desirable initiates; auto only responds |
| Static | `on` | no negotiation at all |

### The mode-compatibility matrix
| Side A / Side B | Result |
|-----------------|--------|
| active / active | ✅ LACP |
| active / passive | ✅ LACP |
| **passive / passive** | ❌ nobody initiates |
| desirable / desirable | ✅ PAgP |
| desirable / auto | ✅ PAgP |
| **auto / auto** | ❌ nobody initiates |
| on / on | ✅ static |
| **on / active** (or any mix) | ❌ incompatible |

The two "dead" same-protocol pairs are **passive/passive** and **auto/auto**.
`on` works **only** with `on`.

```
interface range Gi0/1 - 2
 switchport mode trunk
 channel-group 1 mode active        ! LACP
```
Members must also match in speed, duplex, mode (access/trunk) and allowed VLANs,
or they won't bundle.

## Verify
```
show spanning-tree vlan 10
show spanning-tree root
show etherchannel summary          ! Po1(SU) + members (P) = bundled
show etherchannel load-balance
```
In `show etherchannel summary`, a member flag of `(P)` = bundled, `(I)` =
stand-alone/individual, `(s)` = suspended, `(D)` = down.

## Exam cues
- Root = lowest priority, then lowest MAC. Watch the MAC trap.
- `root primary` = 24576; `root secondary` = 28672.
- passive/passive and auto/auto never form; `on` pairs only with `on`.
