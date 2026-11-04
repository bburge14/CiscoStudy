# OSPF, EIGRP & BGP

Three routing protocols, three personalities. OSPF builds a full map of the
network and does math on it. EIGRP keeps a backup route ready so it can fail over
in a blink. BGP stitches whole networks together across the internet. Let's take
them in turn.

## OSPF: everybody shares the map

OSPF (Open Shortest Path First) is a *link-state* protocol: every router builds a
complete map of its area, then runs shortest-path math to pick routes. To build
that shared map, routers mail each other little map notes called LSAs (Link-State
Advertisements). There are several LSA *types* simply because different notes
describe different things, come from different routers, and travel different
distances. Keep asking "who wrote this note, and how far does it travel?" and the
types fall into place.

Every router writes a **Type 1 (Router) LSA** describing its own links; it stays
inside the area (intra-area). On a shared multiaccess segment like an Ethernet,
one router is elected the DR (Designated Router), and the DR writes a **Type 2
(Network) LSA** listing who's on that segment — again, staying within the area.
When a network needs to be known in *other* areas, the ABR (Area Border Router — a
router sitting on the edge of two areas) writes a **Type 3 (Summary) LSA** to carry
that news across; in the routing table these inter-area routes show as `O IA`. The
ABR also writes a **Type 4 LSA** whose only job is to tell routers how to reach the
ASBR.

The ASBR (Autonomous System Boundary Router) is the router that pulls routes in
from *outside* OSPF — from BGP, say, or another protocol. It writes **Type 5
(External) LSAs** that flood across the whole OSPF domain (shown as `O E1` or `O
E2`). There's one special case: inside a kind of area called an NSSA, a local ASBR
isn't allowed to use Type 5, so it uses a **Type 7 (NSSA External) LSA** that lives
only within the NSSA — and the ABR translates those 7s into 5s on the way out to
the rest of the domain.

> Tie the originator to the type: a router describes itself with Type 1, a DR
> describes its segment with Type 2, an **ABR** carries networks between areas with
> **Type 3**, an **ASBR** injects outside routes with **Type 5**, and inside an
> **NSSA** those become **Type 7** (translated 7→5 at the ABR).

Why would an area block some of those notes? To keep small routers' tables small. A
**stub** area blocks Type 5 externals and the ABR injects a default route instead;
no ASBR is allowed inside. A **totally stubby** area goes further and blocks Type 3
*and* Type 5 — nothing but a default route gets in. An **NSSA** (Not-So-Stubby
Area) is the compromise: it blocks ordinary Type 5 externals like a stub but *does*
let a local ASBR inject externals through Type 7 (which the ABR translates to Type
5 for everyone else) — the whole reason it exists, a stubby area with one door to
the outside.

One last OSPF detail: how it scores a path. The formula is `cost =
reference-bandwidth / interface-bandwidth`, with a minimum of 1. The default
reference bandwidth is 100 Mbps, and that's a problem on modern links: it floors
both Gigabit and 10-Gig interfaces to a cost of 1, so OSPF can't tell them apart.
The fix is to raise the reference everywhere, identically, with `auto-cost
reference-bandwidth 10000` — set it the same on every router or the costs won't
line up.

## EIGRP: keep a trustworthy backup ready

EIGRP (Enhanced Interior Gateway Routing Protocol) is an advanced distance-vector
protocol built around an algorithm called DUAL (Diffusing Update Algorithm). Its
claim to fame is keeping a pre-verified backup path ready, so it fails over the
instant the main one breaks. Its metric, by default, comes from bandwidth and
delay.

Four terms carry the idea. Your **Feasible Distance (FD)** is your own best
(lowest) metric to a destination. A neighbor's **Reported Distance (RD)** is how
far *that neighbor* says it is from the same destination. The **Successor** is the
next-hop with the lowest FD — that's the route EIGRP actually installs and uses.
And the **Feasible Successor (FS)** is a backup next-hop you can trust not to loop.

How do you know a backup won't loop you? With the Feasibility Condition, and it's
the one rule to carry out of this section:

> A neighbor qualifies as a feasible successor only when its **RD < FD** — its
> reported distance is less than your own best distance. If the neighbor is already
> *closer* to the destination than you are, it can't possibly be routing back
> through you, so using it can't create a loop.

That backup is pre-approved, so if the successor fails EIGRP drops to the feasible
successor instantly, with no recalculation. Only if there's *no* feasible successor
does the route go **Active** — meaning EIGRP has to query its neighbors and let
DUAL compute a fresh path.

## BGP: connecting the big networks

BGP (Border Gateway Protocol) is how whole networks exchange routes — it's the
routing protocol that holds the internet together. A "whole network" here means an
autonomous system (AS): one organization's routing domain. BGP is an exterior
gateway protocol (EGP), meaning it routes
*between* those autonomous systems rather than inside one, and it's a *path-vector*
protocol because it tracks the list of autonomous systems a route has crossed (the
AS-Path). Routes learned from a different AS are eBGP (external) with an
administrative distance (AD) of 20; routes learned from a router in your own AS are
iBGP (internal) with an AD of 200 — lower distance means more trusted, so eBGP is
believed over iBGP.

BGP usually ignores hop count. When it has two ways to the same destination, it
walks down a fixed list of tie-breakers (attributes) until one wins — highest
priority first:

1. **Weight** — Cisco-only, local to this one router, highest wins — your personal
   thumb on the scale.
2. **Local Preference** — highest wins, shared across your whole AS — your AS's
   agreed exit.
3. Locally **originated** — a route this router injected itself (via `network`,
   aggregate, or redistribution).
4. Shortest **AS-Path** — fewest autonomous systems to cross.
5. Lowest **Origin** code — IGP (`i`) beats EGP (`e`) beats Incomplete (`?`).
6. Lowest **MED** (Multi-Exit Discriminator) — your hint to a neighbor AS about
   which entrance to use.
7. **eBGP over iBGP** — prefer a route learned from outside.
8. Lowest **IGP metric** to the next hop — the closest exit door.
9. The tie-breakers: oldest eBGP route, then lowest **router-ID**, then lowest
   neighbor IP.

A classic mnemonic for the order is **W**e **L**ove **O**ranges **A**S **O**ranges
**M**ean **P**ure **R**efreshment.

One gotcha bites almost everyone. When an iBGP router passes along a route, it does
**not** change the next-hop address by default — the next hop stays the original
external neighbor's IP. If your interior routing (the IGP) has no idea how to reach
that external IP, BGP treats the route as valid-but-not-best and marks it
inaccessible: real, but unusable. You fix it either with `neighbor x.x.x.x
next-hop-self` (the router substitutes its own address) or by advertising that
external link into the IGP. And because an iBGP router won't re-advertise
iBGP-learned routes to other iBGP peers (a loop-prevention rule), iBGP needs either
a full mesh of peerings or route reflectors to stand in for one.

## The whole thing in one paragraph

OSPF shares a full map through LSAs — routers write Type 1, DRs write Type 2, ABRs
carry Type 3 between areas and Type 4 to locate the ASBR, and ASBRs inject Type 5
externals (Type 7 inside an NSSA, translated 7→5 at the ABR) — while stub and
totally-stubby areas block externals to shrink tables. EIGRP uses DUAL to keep a
loop-free backup, the feasible successor, which qualifies only when a neighbor's
reported distance is less than your feasible distance (RD < FD); lose the successor
with no feasible successor and the route goes Active. BGP connects autonomous
systems and chooses a path by walking its attribute list — Weight, Local-Pref,
locally originated, AS-Path, Origin, MED, eBGP over iBGP, IGP metric, then
oldest/router-ID — and remember that iBGP leaves the next-hop unchanged, so that
next-hop must be reachable through your IGP.

### A few commands to see this on a real device

```
show ip ospf database
show ip eigrp topology
show bgp ipv4 unicast
```
