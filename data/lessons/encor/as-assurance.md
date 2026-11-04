# Network Assurance: Diagnostics, NetFlow, IP SLA & Telemetry

## Packet capture: SPAN family
| Feature | Scope |
|---------|-------|
| **Local SPAN** | mirror between ports on the **same** switch |
| **RSPAN** | mirror **across switches** via a dedicated RSPAN VLAN trunked between them |
| **ERSPAN** | mirror across a **routed L3** network (encapsulated in GRE) |

```
monitor session 1 source interface Gi0/1
monitor session 1 destination interface Gi0/24
show monitor session all
```

## IP SLA + object tracking
IP SLA generates synthetic probes (ICMP echo, UDP jitter, HTTP) to measure
reachability, latency, jitter and loss. Tie a probe to routing with **object
tracking**:
```
ip sla 1
 icmp-echo 203.0.113.2
 frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability
ip route 0.0.0.0 0.0.0.0 203.0.113.2 track 1   ! route withdrawn if the probe fails
```
When the SLA fails, `track 1` goes down and IOS removes the route — a reliable
static-route failover, often paired with a floating static backup.

## Flexible NetFlow (FNF)
Exports flow statistics (who talked to whom, how much). Components:
| Component | Role |
|-----------|------|
| **Flow record** | **what** to collect — `match` = key fields (define the flow), `collect` = non-key fields (counters) |
| **Flow exporter** | **where** to send it (collector IP/port/version) |
| **Flow monitor** | binds record + exporter and is applied to an **interface** |
| **Sampler** | optional 1-in-N sampling to reduce load |

## SNMP, syslog & streaming telemetry
- **SNMP** is **pull**-based (the NMS polls OIDs). **Traps** are unacknowledged
  (can be lost); **informs** are acknowledged + retransmitted (reliable, heavier).
  Both use UDP 162.
- **Model-driven telemetry (MDT)** is **push**-based: the device *streams* data
  per a subscription (periodic or **on-change**) over gRPC/gNMI/NETCONF, using
  YANG models. It scales far better than per-OID polling.

## Diagnostics
`ping`, `traceroute`, `debug` (use **conditional debugging** — `debug condition
interface ...` — to limit output), `show logging`, `show processes cpu`.

## Exam cues
- Local SPAN = same switch; RSPAN = across switches (RSPAN VLAN); ERSPAN = over L3 (GRE).
- FNF: record=what, exporter=where, monitor=bind+apply, sampler=how often.
- SNMP polls; telemetry pushes. Trap=lossy, inform=reliable.
- IP SLA + `track` + static route = failover.
