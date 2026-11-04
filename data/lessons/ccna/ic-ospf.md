# OSPFv2 Operation

OSPF can feel like a lot of moving parts — states, timers, elections — but
underneath it all sits one simple, almost human idea. Once that idea clicks, the
rest stops feeling like trivia to memorize.

## The one idea behind OSPF

Picture a town where every router is a person, and each person's job is to help
draw a map. No single person can see the whole town, so each one writes down only
what they know for certain: "here are the roads connected directly to me, and
here's how good each one is." Then everyone shares their notes with everyone else.
Once all the notes are in, each person glues them into the exact same complete
map — and then quietly works out their own best route to everywhere.

That is OSPF. OSPF stands for Open Shortest Path First. It is an IGP (Interior
Gateway Protocol — a protocol for sharing routes inside one organization), and its
administrative distance (AD), which is how much a router trusts a route when
sources compete, is 110.

> **Every router floods small descriptions of its own links to all the others, so
> they all end up holding one identical map, and then each router runs the same
> math on that map to find the shortest path.**

Those small descriptions are called LSAs (Link-State Advertisements). The shared
map they build is the link-state database, and there is one database per area (an
area is just a chunk of the network OSPF groups together). The "same math" is SPF
(Shortest Path First), using Dijkstra's algorithm — you don't need its inner
workings, just that it finds shortest paths. Because the whole scheme is built on
describing the state of each link, OSPF is called a link-state protocol.

## Turning OSPF on, and the network statement
```
router ospf 1                       ! process ID is LOCAL only — need not match neighbors
 router-id 1.1.1.1
 network 10.1.12.0 0.0.0.3 area 0   ! wildcard mask selects the interfaces
 passive-interface Gi0/2            ! form no neighbors here, still advertise it
```
The `1` after `router ospf` is a process ID. It is local only — just a label on
this one router — so it need not match the number your neighbors use.

The `network` line trips people up because it doesn't really mean "advertise this
network." What it actually does is pick interfaces: any interface whose IP matches
gets switched on for OSPF and placed in the area you named. It matches using a
wildcard mask (a subnet mask flipped around, where 0 means "this bit must match"),
and the matched interfaces are activated in the stated area. The
`passive-interface` line is handy too: it still advertises that interface's
network but forms no neighbors out of it — ideal for a port facing PCs, where
there's no other router to talk to.

## Who am I? The router-ID

Every router needs one unique name on the map, its router-ID (RID), and it chooses
one in a strict order. First, an explicit `router-id` command if you typed one. If
not, the highest IP address on an up loopback interface. If there's no loopback,
the highest IP on any up interface. A loopback wins when it's available because
it's virtual and never goes down, so it never "flaps" and your router keeps a
stable name. One gotcha: once OSPF has picked a RID, changing it only takes effect
after `clear ip ospf process`.

## How two routers become friends (the neighbor states)

When you troubleshoot, OSPF tells you exactly how far two routers got in becoming
friends. Think of a relationship forming step by step.

It starts at **Down** — silence, no hellos heard yet. When a router hears a hello
but hasn't been named back, it reaches **INIT**: it heard you, but the
conversation is still one-way. Once each side sees its own name in the other's
hello, the link is bidirectional and they reach **2-WAY**. Here's a fact worth
keeping: on a shared network, two ordinary routers (DROTHERs — more on that word
shortly) deliberately stop at 2-WAY with each other and go no further. That's on
purpose, not a fault.

If the pair is meant to go all the way, they move into **EXSTART** and
**EXCHANGE**, where they elect a master and slave and swap summaries of their
databases (Database Description packets, or DBDs). This stage is the famous one:
**if a pair gets stuck in EXSTART or EXCHANGE, the cause is an MTU mismatch** — MTU
(Maximum Transmission Unit) is the largest frame an interface will send, and the
two sides insist it match. Then comes **LOADING**, where each router requests any
LSAs it's still missing. And finally **FULL**: fully adjacent, holding identical
databases. FULL is what you want with your DR/BDR, or on a point-to-point link.

## What has to match (and what must not)

Two routers become neighbors only if a handful of things agree: the area, the
hello and dead timers, the subnet and mask on the link, any authentication, and
the stub flags. To go all the way to FULL, the MTU must be compatible too. Exactly
one thing must differ — the router-ID, which has to be unique. And one thing
genuinely doesn't matter: the process ID, that local label from `router ospf 1`.

## Elections: the DR and BDR

On a broadcast (multiaccess) network — say several routers on one switch — having
everyone flood updates to everyone else gets noisy fast. To calm it down, the
routers elect a DR (Designated Router) and a BDR (Backup Designated Router) as the
central point of contact. Everyone else is a DROTHER, and here's the key behavior:
a DROTHER forms a FULL adjacency only with the DR and BDR, and stays in 2-WAY with
the other DROTHERs. That's the normal 2-WAY from before — expected, not broken.
The election is simple: highest OSPF interface priority wins (default 1, and 0
means "never be DR"); if priorities tie, the highest router-ID wins.

## Cost: why OSPF prefers one path

OSPF measures "shortest" in cost, and lower cost wins. The formula is:
```
cost = reference-bandwidth / interface-bandwidth
```
with a minimum of 1. The reference bandwidth defaults to 100 Mbps (10^8). Divide
that by the speed of any fast link and you get a number below 1, which rounds up
to the floor of 1 — so FastEthernet, Gigabit, and 10-Gigabit all come out as cost
1, and OSPF can't tell them apart. The fix is to raise the reference bandwidth
everywhere so faster links earn a lower cost:
```
router ospf 1
 auto-cost reference-bandwidth 10000   ! 10 Gbps, in Mbps; set identically everywhere
```
Use the same value on every router, or your costs won't line up.

## When something's broken

Three patterns cover most OSPF problems. No neighbor at all means something that
"must match" doesn't — area, hello/dead timers, subnet, or authentication — or the
interface is passive or down. A pair stuck in EXSTART or EXCHANGE is an MTU
mismatch; check with `show ip ospf interface` and `show interfaces | include MTU`,
then fix the MTU or tell OSPF to stop caring with `ip ospf mtu-ignore`. And two
DROTHERs sitting in 2-WAY is expected behavior — leave it alone.

## The whole thing in one paragraph

OSPF is a link-state protocol (AD 110): every router describes its own links as
LSAs and floods them, so all routers in an area hold one identical link-state
database, then each runs SPF (Dijkstra) to pick the lowest-cost path. You switch
it on with `router ospf` and a `network` statement whose wildcard mask chooses
which interfaces join which area; the process ID is only a local label. Each
router names itself with a router-ID — explicit, else highest loopback IP, else
highest interface IP. Two routers climb through neighbor states as they get
acquainted: INIT is one-way, 2-WAY is two-way (and where DROTHERs happily stop
with each other), a stall at EXSTART/EXCHANGE means an MTU mismatch, and FULL means
finished. On shared segments they elect a DR and BDR (highest priority, then
highest RID) to keep flooding tidy. And cost — reference-bandwidth divided by
interface-bandwidth — decides the best path, so raise the reference bandwidth
everywhere if you want OSPF to favor your fastest links.

### See it on a real device
```
show ip ospf neighbor
show ip ospf interface g0/0
show ip route ospf
```
