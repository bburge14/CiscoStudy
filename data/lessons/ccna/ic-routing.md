# The Routing Table & Static Routing

A router sits where networks meet, like a clerk at a busy mail-sorting counter.
Every packet that arrives is a letter with a destination written on it, and the
router's one job is to decide which road to send it down. It makes that decision
by reading its **routing table** — its address book of known destinations.
Learning how it reads that table is most of this topic.

## How a router chooses a route

Often several routes in the table could match one destination. The router doesn't
pick at random or just trust the "fastest" protocol — it follows a strict
three-step order.

**Step one is longest prefix match.** The router looks for the *most specific*
route that still contains the destination. "Most specific" means the longest mask
— the route describing the smallest, most precise neighborhood. This is like a
mail clerk choosing "123 Main St, Apartment 4" over a note that just says "Main
Street." The more detailed address wins, every time.

> **Longest prefix match is decided first — before anything about which protocol
> taught the route or how trusted it is. The most specific matching route always
> wins.**

Let me walk one through. Say a packet is headed for **10.1.1.50**, and the table
holds three routes that could match:

- an OSPF route for `10.1.1.0/24`
- a static route for `10.1.1.0/25`
- an EIGRP route for `10.1.1.48/29`

Which wins? Check how specific each one is. The `/29` covers only `.48` through
`.55`, and `.50` falls right inside it — that is the tightest match. So the router
uses the EIGRP `/29`, and it never even considers how trusted the sources are,
because the three routes describe *different* neighborhoods. Specificity settled
it.

**Step two, administrative distance, only matters when two routes describe the
exact same neighborhood** but were learned from different sources (more on that
next). **Step three, metric,** is the final tiebreaker *within* a single protocol
— when, say, OSPF knows two equally specific ways to the same place, it keeps the
one with the lower metric (its own measure of cost).

## Administrative distance: how much do you trust the source?

A router can learn about the same network from several sources at once — a
hand-typed static route, OSPF, EIGRP, and so on. When those sources describe the
*identical* prefix, the router needs a way to decide whom to believe. That is
**administrative distance (AD)**: a trust score where **lower means more
trusted.**

Think of it as ranking your sources of directions. A road sign you posted
yourself (a static route) you trust almost completely. A rumor passed along from a
far-off office (a routing protocol) you trust a little less. Here is the full
ranking, from most trusted to least:

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

Don't agonize over every row, but burn four into memory because they come up
constantly: **static is 1, EIGRP is 90, OSPF is 110, and RIP is 120.** A connected
network (a link the router is physically part of) is 0 — nothing is more
trustworthy than a cable you can see — and 255 means "unusable," a route the
router refuses to install.

## Static routes: directions you write by hand

A **static route** is a destination you type in yourself instead of letting a
protocol learn it. The command is `ip route`, followed by the destination
network, its mask, and where to send the traffic:

```
ip route 10.2.0.0 255.255.0.0 203.0.113.2       ! next-hop
ip route 10.2.0.0 255.255.0.0 Gi0/1 203.0.113.2 ! interface + next-hop (best on multiaccess)
ip route 0.0.0.0 0.0.0.0 203.0.113.2            ! default route
```

The first line says "to reach 10.2.0.0/16, hand the packet to the neighbor at
203.0.113.2" — that neighbor is the **next hop**. The second line names both an
outgoing interface *and* the next hop, which is best on a multiaccess link (a
shared segment with many neighbors) so the router doesn't have to lean on
proxy-ARP to find the next hop. As a rule, give the next-hop IP, and add the
interface on those shared links.

The third line is special. `0.0.0.0 0.0.0.0` matches *everything*, so it is the
**default route** — the catch-all used when no more specific route matches.

### The floating static route

Sometimes you want a static route as a *backup* that only kicks in if the main
path dies. The trick is administrative distance. Remember a static route's default
AD is 1, which beats almost everything — so a plain static route would be used
*all the time*, not just in an emergency. To make it a true backup, you raise its
AD above the source it is protecting:

```
ip route 0.0.0.0 0.0.0.0 203.0.113.2 120    ! backs up an OSPF default (AD 110)
```

Here OSPF's default route has AD 110. By giving this static route AD 120, you tell
the router "ignore this unless OSPF's version disappears." The moment the OSPF
route is gone, the floating static floats up and takes over. Had you left it at
the default AD 1, it would have beaten OSPF and been used constantly — not a
backup at all.

## Default gateway vs default route

These sound alike but describe two different devices. A **host** — your PC — knows
only its own subnet, so to reach anything beyond it the host sends the packet to
its **default gateway**, the nearby router. A **router** has no "gateway"; instead
it has a **default route** (`0.0.0.0/0`, also called the *gateway of last resort*)
for any destination it has no more specific match for. Same idea — "when in doubt,
send it this way" — just at two different points in the journey.

## The whole thing in one paragraph

When a packet arrives, a router first picks the route with the **longest prefix
match** — the most specific matching network — no matter which protocol taught it
or how trusted it is. Only when two routes describe the exact same prefix does
**administrative distance** break the tie (lower is more trusted: static 1, EIGRP
90, OSPF 110, RIP 120), and only within one protocol does **metric** decide. You
can add routes by hand with `ip route`, including a catch-all default route to
`0.0.0.0 0.0.0.0`, and you can turn a static route into a backup — a **floating
static** — by setting its AD higher than the path it protects. Hosts leave their
subnet through a default gateway; routers fall back on a default route.

### See it on a real device
```
show ip route
show ip route 10.1.1.50
show ip route 0.0.0.0
```
