# Multicast & QoS

Two topics here, both about treating some traffic differently from the rest.
Multicast is about sending one stream to many people without making a separate
copy for each. QoS is about deciding whose traffic goes first when the road gets
crowded. They're separate ideas, so we'll do multicast first, then QoS.

## Multicast: one stream, many listeners

Imagine a live video going out to 500 employees. You could send 500 separate
copies — that's unicast, and it would crush your bandwidth. You could blast it to
everyone on the network whether they want it or not — that's broadcast, and it
wastes effort and annoys everyone. Multicast is the smart middle: the source sends
*one* copy, and the network duplicates it only where paths split, delivering only
to the people who actually asked. It's like a radio station — one broadcast goes
out, and only the radios tuned to that frequency listen.

Multicast has its own address range, **224.0.0.0/4** (that's everything from 224
through 239 in the first number). A handful are reserved as link-local, meaning
they stay on the local wire and are never routed: **224.0.0.1** reaches all hosts,
**224.0.0.2** reaches all routers, and **224.0.0.5** and **224.0.0.6** are used by
OSPF. When a multicast packet needs a MAC address to ride on at Layer 2, it's
built in a fixed way: the prefix `01:00:5E` followed by 23 bits taken from the
group address.

So how does a device say "I want this stream"? It tells its local router using
IGMP (Internet Group Management Protocol). In IGMPv2 that's a simple pair of
messages — join and leave. IGMPv3 adds source filtering, so a host can say "I want
this group, but only *from this specific source*," which is what powers SSM
(Source-Specific Multicast). There's a catch down at the switch, though: a plain
switch floods multicast to every port in the VLAN, which undoes the whole point.
**IGMP snooping** fixes that — the switch quietly listens to the IGMP join
messages and forwards the stream only to the ports that actually asked for it.

Out in the routed network, routers still have to build the delivery paths — the
*trees* the traffic flows along. That's the job of PIM (Protocol Independent
Multicast); it's called "independent" because it doesn't run its own routing, it
just borrows whatever unicast routing table is already there. PIM has two modes.
**Dense Mode** assumes everybody wants the stream: it floods it everywhere, then
prunes back the branches that don't want it — fine for small, dense groups.
**Sparse Mode** assumes nobody wants it unless they ask: receivers send explicit
joins toward a meeting point called the Rendezvous Point (RP).

Sparse mode builds two kinds of trees, and telling them apart is the thing to lock
in:

> **(\*, G)** is the **shared tree**, rooted at the RP — the `*` means "any
> source," so it's the path for group G coming from wherever, by way of the RP.
> **(S, G)** is the **source tree** (also called the shortest-path tree), built for
> one specific source S. Receivers join the shared tree first, then may
> **SPT-switch** over to the (S, G) tree to take the more direct path straight from
> the source.

## QoS: deciding who goes first

When a link gets congested, something has to give — and QoS (Quality of Service)
is how you decide *whose* packets go first and whose wait or get dropped. Think of
it as a priority lane. A phone call can't wait; a voice packet that shows up a
moment late is useless. A file backup, on the other hand, won't mind waiting a few
milliseconds. QoS lets you say so.

There are three overall approaches. **Best-effort** is no QoS at all — every packet
equal, which is the plain default. **IntServ** (Integrated Services) has each flow
reserve its bandwidth in advance using RSVP (Resource Reservation Protocol); it's
precise but it doesn't scale, because every router has to track every single flow.
**DiffServ** (Differentiated Services) is the practical model: don't reserve
anything, just *mark* each packet with a class, and have every router apply a
per-hop behavior based on that mark.

The marking should happen as close to the source as trust allows. At Layer 2 the
marking is called CoS (Class of Service), 3 bits carried in the VLAN tag. At Layer
3 it's DSCP (Differentiated Services Code Point), 6 bits in the IP header — this is
the one that travels end to end. A few DSCP values come up constantly: **EF
(Expedited Forwarding) = 46** for voice media, **CS3 = 24** for call signaling,
**AF41 = 34** for video, **CS1 = 8** for scavenger (bulk traffic you're happy to
starve), and **0** for best-effort. If you remember one, remember voice media = EF
= 46.

Four tools do the actual work, and the pair people confuse is policing versus
shaping. **Policing** enforces a rate by *dropping or re-marking* anything over the
limit; because it never holds packets, it adds no delay, and it can run inbound or
outbound. **Shaping** also enforces a rate, but instead of dropping the excess it
*buffers* it and releases it smoothly — which does add delay, and it only works
outbound.

> **Policing drops (or re-marks) excess and adds no delay; shaping buffers excess
> and adds delay, outbound only.** Same goal, opposite method: one throws the extra
> away, the other holds it back.

The other two tools handle congestion itself. **Queuing** decides the order packets
leave a congested interface: CBWFQ (Class-Based Weighted Fair Queuing) gives each
class a guaranteed share, and LLQ (Low-Latency Queuing) adds a strict-priority
queue that always jumps to the front — which is exactly where voice belongs.
**WRED** (Weighted Random Early Detection) is congestion *avoidance*: it starts
dropping a few packets early and selectively as a queue fills, to head off tail
drop — the nasty situation where a totally full queue drops everything at once and
every TCP sender backs off together.

One safety rule ties it together: the trust boundary. Don't trust the QoS markings
coming from end hosts past the access edge — a user's PC could mark its game
traffic as voice to jump the line. The exception is a device you actually trust,
like a Cisco IP phone, which you tell the switch to trust with `mls qos trust
device cisco-phone`.

## The whole thing in one paragraph

Multicast sends one stream that the network copies only where it must, reaching
just the receivers who asked; hosts ask with IGMP (and IGMP snooping keeps a switch
from flooding the VLAN), while routers build the paths with PIM — a shared tree
(\*, G) rooted at the Rendezvous Point for any source, or a source tree (S, G)
straight from one specific source after an SPT switch. QoS then decides who goes
first on a busy link: mark traffic with DSCP (voice media is EF, 46) under the
scalable DiffServ model, and treat it with the right tool — policing drops the
excess with no delay, shaping buffers it and adds delay outbound, LLQ gives voice
strict priority, and WRED drops a little early to avoid tail drop — all while
trusting host markings only inside your access-edge boundary.

### A few commands to see this on a real device

```
show ip mroute
show ip pim rp mapping
show ip igmp groups
```
