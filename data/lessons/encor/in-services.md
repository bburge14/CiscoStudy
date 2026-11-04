# Multicast & QoS

## Multicast
Delivers one stream to many receivers efficiently. Addresses: **224.0.0.0/4**.
Reserved link-local: 224.0.0.1 (all hosts), 224.0.0.2 (all routers),
224.0.0.5/6 (OSPF). A multicast MAC maps as `01:00:5E` + 23 bits of the group.

### IGMP
Hosts signal group membership to the local router with **IGMP** (v2 = join/leave;
v3 adds source filtering for SSM). **IGMP snooping** lets a switch forward
multicast only to interested ports instead of flooding the VLAN.

### PIM
Builds the multicast distribution trees in the routed network:
- **PIM Dense Mode** — flood-and-prune (small/dense groups).
- **PIM Sparse Mode** — explicit joins toward a **Rendezvous Point (RP)**.
  - **(\*, G)** — **shared tree** rooted at the RP ("\*" = any source).
  - **(S, G)** — **source (shortest-path) tree** for a specific source.
  Receivers join the shared tree first, then may **SPT-switch** to (S, G).

```
show ip mroute
show ip pim rp mapping
show ip igmp groups
```

## QoS
### Models
- **Best-effort** — no QoS.
- **IntServ** — per-flow reservations (RSVP); doesn't scale.
- **DiffServ** — per-hop behaviors by class marking (**DSCP**); the practical model.

### Classification & marking
Mark as close to the source as trust allows. Layer 2 = **CoS** (3 bits); Layer 3
= **DSCP** (6 bits). Common DSCP: **EF (46)** voice media, **CS3 (24)** signaling,
**AF41 (34)** video, **CS1 (8)** scavenger, **0** best-effort.

### Tools
| Tool | What it does |
|------|--------------|
| **Policing** | enforces a rate by **dropping/re-marking** excess — no delay; in or out |
| **Shaping** | **buffers** excess to the rate — adds delay; outbound only |
| **Queuing (LLQ/CBWFQ)** | schedules at congestion; LLQ = strict priority for voice |
| **WRED** | congestion **avoidance** — selective early drops to prevent tail drop |

Trust boundaries: don't trust end-host markings beyond the access edge unless the
device is trusted (e.g., a Cisco IP phone via `mls qos trust device cisco-phone`).

## Exam cues
- (\*, G) = shared tree via RP; (S, G) = source tree.
- Policing drops (no delay); shaping buffers (adds delay, outbound).
- Voice = EF (46), priority/LLQ.
