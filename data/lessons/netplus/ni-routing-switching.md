# Routing & Switching Technologies

Routing moves traffic *between* networks; switching moves it *within* one. This
lesson covers both halves of how a packet actually gets from end to end — the
Layer 3 decisions a router makes and the Layer 2 features a switch provides.

## How a router chooses a path

A router keeps a **routing table** — a list of known destination networks and how to
reach each. When a packet arrives, the router finds the table entry that matches the
destination and forwards it there. The matching rule is important:

> **Longest prefix match wins.** If both `10.1.1.0/24` and `10.0.0.0/8` could reach a
> destination, the router uses the **more specific** (longer prefix) route. A
> `/32` beats a `/24` beats a `/8`.

Routes get into the table three ways: **connected** (a network on an interface the
router owns), **static** (typed in by hand), and **dynamic** (learned from a routing
protocol). A **default route** (`0.0.0.0/0`) is the catch-all used when nothing more
specific matches — the "if you don't know where it goes, send it this way" route.

### Static vs dynamic routing

- **Static** routing is manual. It's simple, uses no bandwidth or CPU to advertise,
  and is predictable — but it doesn't adapt when a link fails, and it's a lot of
  work on a big network. Good for small or stub networks and default routes.
- **Dynamic** routing uses a protocol so routers learn and share routes
  automatically and reroute around failures. More overhead, far less manual work.

## Routing protocols and metrics

Dynamic protocols fall into two families. **IGPs (Interior Gateway Protocols)** run
*inside* one organization: OSPF, EIGRP, RIP. **EGPs** run *between* organizations —
and the one that matters is **BGP**, the protocol that holds the internet together
by exchanging routes between autonomous systems.

| Protocol | Type | Metric | Notes |
|----------|------|--------|-------|
| RIP | IGP, distance-vector | Hop count (max 15) | Old, simple, small nets |
| OSPF | IGP, link-state | Cost (based on bandwidth) | Open standard, scales well with areas |
| EIGRP | IGP, hybrid | Bandwidth + delay | Cisco; fast convergence |
| BGP | EGP, path-vector | Path attributes | The routing protocol of the internet |

A **metric** is how a protocol ranks competing routes *within* itself — lower is
better. RIP counts hops; OSPF uses **cost**, which is derived from bandwidth, so it
naturally prefers faster links over shorter-but-slower ones.

### Administrative distance: trusting one protocol over another

When two *different* sources offer a route to the same network, the router can't
compare their metrics (hops vs cost mean nothing to each other). Instead it uses
**administrative distance (AD)** — a trust rating where **lower is more trusted**.

| Source | AD |
|--------|---:|
| Connected | 0 |
| Static | 1 |
| eBGP (external) | 20 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| RIP | 120 |
| iBGP (internal) | 200 |
| Unreachable | 255 |

> **AD breaks ties between protocols; metric breaks ties within one protocol.** So a
> static route (AD 1) beats an OSPF route (AD 110) to the same network, even if OSPF
> "knows a better way," because the router trusts the static entry more.

## NAT: many private hosts, one public address

Private addresses can't go on the internet, so a router rewrites them with **NAT
(Network Address Translation)**. The common form is **PAT (Port Address
Translation)**, also called **NAT overload**: many inside hosts share *one* public
IP, and the router tells their conversations apart by assigning each a different
source **port number**. This is why a whole house full of devices reaches the
internet through a single public address.

## Switching: moving frames inside a LAN

A switch learns which **MAC address** lives on which port by watching the source
address of incoming frames, and stores that in its **MAC address table**. After
that it forwards each frame only out the one port where the destination lives —
unless it's a broadcast or an unknown destination, which it floods out every port.

### VLANs: many logical LANs on one switch

A **VLAN (Virtual LAN)** splits one physical switch into several separate broadcast
domains. Ports in VLAN 10 can't talk to ports in VLAN 20 without a router or Layer 3
switch, even on the same box. VLANs give you segmentation (for security and to
shrink broadcast domains) without buying more switches.

- An **access port** carries exactly one VLAN and connects to an end device.
- A **trunk port** carries **many** VLANs between switches, tagging each frame so the
  far end knows which VLAN it belongs to. The tagging standard is **802.1Q**, which
  inserts a 4-byte VLAN tag into the Ethernet frame.
- The **native VLAN** on a trunk is the one VLAN sent **untagged**; it must match on
  both ends or you get strange cross-VLAN leaks.

> **Access port = one VLAN to a device; trunk = many VLANs between switches, tagged
> with 802.1Q.** The native VLAN rides a trunk untagged.

### Spanning Tree: loops are deadly at Layer 2

Switches flood broadcasts, and an Ethernet frame has no "time to live" to kill it.
So if you wire two switches together with two cables, a broadcast circles forever and
multiplies — a **broadcast storm** that melts the network in seconds. **STP (Spanning
Tree Protocol, 802.1D)** prevents this by electing one switch as the **root bridge**
and then *blocking* just enough redundant links to leave a single loop-free path. If
an active link fails, STP unblocks a standby link to restore connectivity.

- The switch with the lowest **bridge ID** (priority + MAC) becomes the **root**.
- Other switches pick their lowest-cost path to the root (the **root port**).
- Redundant links are put into a **blocking** state.
- **RSTP (802.1w)** is the faster modern version, converging in a second or two
  instead of the original's 30–50 seconds.

### More switch features

- **Link aggregation (LACP, 802.3ad)** bundles several physical links into one
  logical link for more bandwidth and redundancy.
- **PoE (Power over Ethernet)** delivers power *and* data over one cable to APs,
  phones and cameras (PoE 802.3af ~15 W, PoE+ 802.3at ~30 W, PoE++ 802.3bt up to
  ~90 W).
- **Port mirroring (SPAN)** copies traffic from one port to another so a sniffer can
  watch it.
- **Jumbo frames** raise the payload above the normal 1500-byte MTU (to ~9000) for
  efficient storage and backup traffic.

## On the exam

- **Longest prefix match** picks the route; a **default route** is `0.0.0.0/0`.
- Know route sources (connected, static, dynamic) and static vs dynamic trade-offs.
- Classify protocols: **OSPF** (link-state, cost), **BGP** (the internet's EGP,
  path-vector), RIP (hop count, max 15), EIGRP (Cisco). IGP vs EGP.
- Memorize **administrative distance**: connected 0, static 1, eBGP 20, EIGRP 90,
  **OSPF 110**, RIP 120, iBGP 200. AD chooses between protocols; metric within one.
- **PAT/NAT overload** lets many hosts share one public IP via port numbers.
- VLANs = separate broadcast domains; **access = one VLAN, trunk = many via 802.1Q**;
  native VLAN is untagged.
- **STP** stops Layer 2 loops by electing a root bridge and blocking redundant links;
  **RSTP** is the fast version. Know LACP, PoE tiers, port mirroring, jumbo frames.
