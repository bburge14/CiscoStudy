# Enterprise Design, High Availability & Fabric

A big campus network — a university, a hospital, a corporate HQ — can have
thousands of devices plugged in. If you wired them all together in a pile, nobody
could understand it, find a fault, or make it fast. So Cisco builds these networks
in **layers**, each with one clear job. Get the layers straight and everything
else in this lesson hangs off them.

## The three layers, like a road system

Think of how you drive across town. You pull out of your **driveway** onto a small
local street. That street feeds into a **main road** with traffic lights and signs
that decide where you can turn. The main road pours onto a wide-open **highway**
built for nothing but speed. A campus network is laid out the same way, in three
tiers.

The **access layer** is the driveway: it's where endpoints — PCs, phones, wireless
access points, cameras — actually plug in. This layer handles the things that
touch an end device directly: **VLANs** (which virtual network a port belongs to),
**port security**, **802.1X** (a login check at the port, so only authorized
devices get on), and **PoE** (*Power over Ethernet* — sending electrical power
down the same network cable, so a phone or camera needs no separate power brick).

The **distribution layer** is the main road with all the traffic lights. It's the
gathering point where many access switches come together, and it's where the
**decisions** happen: **routing** between networks, **policy**, **filtering**
(access lists), and **redistribution** between routing protocols. It sits right on
the boundary between the Layer 2 world of the access layer and the Layer 3 world
above it.

The **core layer** is the highway. Its only job is to move traffic between
distribution blocks as fast as possible. You deliberately keep it **simple** — no
access lists, no policy, nothing that stops to think, because every bit of
thinking adds delay (latency).

> **Rules and decisions belong in the distribution layer. The core is a highway —
> keep it empty of stoplights so it stays fast.**

Here's that in motion. A PC in one building wants a server in another. It plugs
into an **access** switch, which checks the port and tags its VLAN. The traffic
rises to **distribution**, which makes the routing decision and applies policy.
Distribution hands it to the **core**, which sprints it across campus to the far
distribution block, which routes it down to the **access** switch where the server
lives. Three layers, each doing its one job.

Not every site needs all three. In a smaller building you can merge the top two
into a **collapsed core**, where one set of switches does both core and
distribution. And in the data center a different shape, **spine-leaf**, is used:
every **leaf** switch connects to every **spine** switch, and leaves never connect
to each other. That guarantees any server is the same short, predictable hop from
any other — great for the heavy side-to-side ("east-west") traffic servers
generate.

## Keeping it running when hardware fails

A network people depend on can't go dark because one box died. Two separate ideas
guard against that, and the exam loves to blur them — so keep them apart.

The first is **chassis virtualization**. **StackWise**, **StackWise Virtual**, and
the older **VSS** glue physical switches together so they behave as **one logical
switch with a single control plane** — one brain running two bodies. Because a
downstream switch now sees just one neighbor, it can bundle its uplinks to *both*
chassis into a single **Multichassis EtherChannel (MEC)**. And since there's no
longer a loop to worry about, **Spanning Tree** stops blocking a redundant uplink,
so you actually get to use both links instead of letting one sit idle. (Features
with names like **NSF/SSO, GIR, and ISSU** go further, keeping traffic forwarding
even while the control plane fails over or the software is upgraded.)

The second idea is **gateway redundancy**, handled by a family of **FHRPs**
(*First Hop Redundancy Protocols*). Every device sends its off-network traffic to
a **default gateway** — a router. If that one router dies, everyone is stranded.
An FHRP lets two or more *separate* routers share a single virtual gateway
address, so if one fails another takes over without any device noticing. The three
to know compare like this:

| Protocol | Whose | Roles | Load-balances on its own? |
|--|--|--|--|
| HSRP | Cisco | Active / Standby | No — use multiple groups |
| VRRP | IETF (open) | Master / Backup | No — use multiple groups |
| GLBP | Cisco | AVG + up to 4 AVFs | **Yes** (multiple virtual MACs) |

HSRP and VRRP each pick one router to be live while the others wait, so to spread
load you build several groups. **GLBP** (one *Active Virtual Gateway* directing up
to four *Active Virtual Forwarders*) shares the load by itself. The key point:
stacking is **not** an FHRP. Stacking fuses boxes into one brain; an FHRP leaves
the routers as separate brains that merely share one gateway address.

## SD-Access: a smart network on top of a plain one

Cisco's modern campus design, **SD-Access** (Software-Defined Access), builds a
**VXLAN overlay** on top of an ordinary **routed underlay**. Picture two layers:
the underlay is the plain physical network that just moves packets (the roads),
and the overlay is a virtual network riding on top of it. The clever part is
splitting the work into three **planes**.

The **control plane is LISP** (Locator/ID Separation Protocol). A control-plane
node acts as the **Map-Server / Map-Resolver**, a directory holding **EID→RLOC**
mappings — it answers "this endpoint (its EID, *Endpoint Identifier*) can be
reached at that switch (its RLOC, *Routing Locator*)." The **data plane is VXLAN**,
which carries the actual user traffic (tagged with its VNI and SGT). And the
**policy plane is Cisco TrustSec**, which uses **SGTs** (*Scalable Group Tags*) to
decide who's allowed to talk to whom based on the user's group, not their IP
address.

The switches in a fabric take named roles: an **edge** node connects endpoints and
registers their EIDs, a **border** node is the exit to everything outside the
fabric, and a **control** node holds the LISP map database. A **WLC** (*Wireless
LAN Controller*) folds wireless clients into the same fabric.

Sitting over all of it, tools like **Catalyst Center** and **DNA/AI analytics**
learn what "normal" looks like and flag anything odd; "AI endpoint analytics" and
ML-driven **RRM** (*Radio Resource Management*) tune the wireless automatically. At
this level you just need the *purpose* — data-driven assurance and automation —
not the internals.

## The whole thing in one paragraph

A campus network is built in three layers like a road system: the **access** layer
is where endpoints plug in (VLANs, PoE, 802.1X, port security), the
**distribution** layer is where all the decisions live (routing, policy,
filtering, redistribution), and the **core** is a fast, simple highway you keep
free of policy. To survive hardware failure, **StackWise/VSS** fuses switches into
one logical switch (enabling a cross-chassis EtherChannel and freeing STP-blocked
links), while a separate idea — an **FHRP** such as HSRP, VRRP, or GLBP — lets
independent routers share one gateway address. And **SD-Access** overlays VXLAN on
a routed underlay, splitting the job into three planes: **LISP** for control,
**VXLAN** for data, and **TrustSec** for policy.
