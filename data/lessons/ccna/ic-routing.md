# The Routing Table & Static Routing

## How a router chooses a route
When a packet arrives, the router picks the best matching route in this order:

1. **Longest prefix match** — the most specific route (longest mask) that
   contains the destination wins, *regardless of protocol or AD*.
2. **Administrative distance (AD)** — breaks ties between routes to the **same
   prefix** learned from different sources. Lower AD is more trusted.
3. **Metric** — breaks ties within the same protocol.

### Longest-prefix example
For destination **10.1.1.50** with three routes:
- OSPF `10.1.1.0/24`
- static `10.1.1.0/25`
- EIGRP `10.1.1.48/29`

The **/29** (covers .48–.55) is the most specific and is used — AD never enters
the decision because the prefixes differ.

## Administrative distance (defaults)
| Source | AD |
|--------|---:|
| Connected | 0 |
| Static | 1 |
| eBGP | 20 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| RIP | 120 |
| EIGRP (external) | 170 |
| iBGP | 200 |
| Unusable | 255 |

## Static routes
```
ip route 10.2.0.0 255.255.0.0 203.0.113.2       ! next-hop
ip route 10.2.0.0 255.255.0.0 Gi0/1 203.0.113.2 ! interface + next-hop (best on multiaccess)
ip route 0.0.0.0 0.0.0.0 203.0.113.2            ! default route
```
Prefer specifying the **next-hop IP** (and interface on multiaccess links) so the
router doesn't rely on proxy-ARP.

### Floating static route
A backup route that activates only when the primary is gone — set its AD
**higher** than the primary source:
```
ip route 0.0.0.0 0.0.0.0 203.0.113.2 120    ! backs up an OSPF default (AD 110)
```
If you used the default AD 1, the static would beat OSPF and be used all the
time — not a backup.

## Default gateway vs default route
- A **host** uses a *default gateway* to leave its subnet.
- A **router** uses a *default route* (`0.0.0.0/0`, the "gateway of last
  resort") for destinations with no more specific match.

## Verify
```
show ip route
show ip route 10.1.1.50
show ip route static
show ip route 0.0.0.0
```

## Exam cues
- Longest prefix first, **then** AD, **then** metric.
- Floating static = AD above the primary.
- Know the AD defaults cold (static 1, EIGRP 90, OSPF 110, RIP 120).
