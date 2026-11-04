# Network Assurance: Diagnostics, NetFlow, IP SLA & Telemetry

A network can look fine and still be quietly broken. Assurance is the set of
tools that let you *see* what your network is really doing — so you can prove
it's healthy, or catch a problem before your users do.

Think of a car mechanic. The engine is sealed shut, so they plug in gauges and
sensors to watch what they can't see directly. Each tool in this lesson is one
of those gauges. They answer different questions, so let's take them one at a
time.

> **You can't fix what you can't see.** Every tool here exists to turn invisible
> network behavior into something you can watch, measure, or react to
> automatically.

## SPAN: making a copy of traffic so you can look at it

Sometimes you need to inspect the actual packets flowing through a switch —
maybe to chase down a problem or feed a security tool. But you can't read
traffic that isn't coming to you. So you ask the switch to make a *copy* and
send it to a port where your analyzer is plugged in. That copying feature is
called **SPAN** (Switched Port Analyzer). Think of it as a photocopier for
network traffic: the real mail keeps moving, and you get a duplicate to study.

There are three flavors, and the only thing that changes is *how far the copy
has to travel*.

Plain **Local SPAN** copies traffic between ports on the **same switch**. Your
source port and your analyzer port are on one box. Simple.

**RSPAN** (Remote SPAN) copies traffic **across switches**. The copied traffic
rides a dedicated **RSPAN VLAN** that is trunked between the switches, so an
analyzer on a *different* switch can receive it.

**ERSPAN** (Encapsulated Remote SPAN) goes even further — it copies traffic
**across a routed Layer 3 network**. To cross routers, each copied packet is
wrapped inside **GRE** (Generic Routing Encapsulation), a tunneling method, so
it can travel over IP to a far-away analyzer.

So the progression is just distance: same switch (Local), across switches on a
VLAN (RSPAN), across routers over GRE (ERSPAN). Here's the basic Local SPAN
setup — source port in, destination port out:

```
monitor session 1 source interface Gi0/1
monitor session 1 destination interface Gi0/24
show monitor session all
```

## IP SLA: sending test traffic to measure the path

How do you know a link is slow, lossy, or down *before* someone complains? You
send your own test traffic and measure what comes back. That's **IP SLA** (IP
Service Level Agreement). It fires off small synthetic probes — like an **ICMP
echo** (a ping), a **UDP jitter** test, or an **HTTP** request — and measures
reachability, latency, jitter, and loss.

On its own, IP SLA just measures. The powerful trick is wiring it to your
routing so the network *reacts* on its own. You do that with **object
tracking**. Walk through this slowly:

```
ip sla 1
 icmp-echo 203.0.113.2
 frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability
ip route 0.0.0.0 0.0.0.0 203.0.113.2 track 1   ! route withdrawn if the probe fails
```

Reading it top to bottom: SLA number 1 pings `203.0.113.2` every 5 seconds,
forever, starting now. Then `track 1` watches that probe's reachability.
Finally, the default route (`0.0.0.0 0.0.0.0`) is told to depend on `track 1`.
So if the pings stop coming back, the track goes **down**, and IOS **removes
that route**. That gives you a reliable static-route failover — often paired
with a *floating static* backup route (a spare route with a worse metric) that
quietly takes over once the main one disappears.

## Flexible NetFlow: a ledger of who talked to whom

SPAN shows you individual packets, which is a lot of detail. Often you'd rather
have a summary: which devices talked, to whom, and how much. That's **Flexible
NetFlow (FNF)** — a running ledger of conversations ("flows") on an interface.

FNF is built from four pieces, and each answers a plain question. The **flow
record** is the *what*: its `match` fields are the key fields that define a flow
(like source and destination IP), and its `collect` fields are the non-key
fields it counts up (like byte and packet totals). The **flow exporter** is the
*where*: the collector's IP, port, and version to send the data to. The **flow
monitor** is the glue — it *binds* a record to an exporter and is applied to an
**interface**, which is what actually turns collection on. And the optional
**sampler** controls *how often*: it grabs only 1 in every N packets to reduce
load on busy links.

Put plainly: record = what, exporter = where, monitor = bind-and-apply,
sampler = how often.

## SNMP vs telemetry: who does the asking?

There are two ways to get ongoing stats out of a device, and the difference is
simply *who starts the conversation*.

The old way is **SNMP** (Simple Network Management Protocol), which is
**pull**-based: a management station (NMS) repeatedly polls the device for
specific values called OIDs. It's like phoning someone every few minutes to ask
"anything new?" SNMP can also send alerts on its own: a **trap** is
fire-and-forget and **unacknowledged**, so it can be lost, while an **inform**
is **acknowledged** and retransmitted — more reliable, but heavier. Both traps
and informs use **UDP 162**.

The modern way is **model-driven telemetry (MDT)**, which is **push**-based:
instead of being polled, the device *streams* data on its own according to a
**subscription** — either **periodically** or **on-change** (only when
something actually changes). It sends over transports like gRPC/gNMI or NETCONF,
using structured **YANG** models. Because the device pushes only what you
subscribed to, it scales far better than polling one OID at a time. Short
version: SNMP pulls; telemetry pushes.

## Diagnostics: the quick hands-on checks

When you just need to look right now, reach for the classics: `ping` to test
reachability, `traceroute` to see the hop-by-hop path, and `debug` for live
detail. Because `debug` can flood you, use **conditional debugging** — `debug
condition interface ...` — to limit output to just the interface you care
about. Round it out with `show logging` to read the log buffer and `show
processes cpu` to see what's burdening the CPU.

## The whole thing in one paragraph

Network assurance is about seeing the invisible. SPAN copies real traffic so you
can inspect it — Local on the same switch, RSPAN across switches on an RSPAN
VLAN, and ERSPAN across routers inside GRE. IP SLA sends its own test probes to
measure reachability and delay, and when tied to object tracking and a static
route it becomes automatic failover. Flexible NetFlow keeps a ledger of
conversations using a record (what), an exporter (where), a monitor (bind and
apply to an interface), and an optional sampler (how often). For ongoing stats,
SNMP pulls — with lossy traps and reliable informs, both on UDP 162 — while
model-driven telemetry pushes a subscription of data on its own. And when you
just need answers now, ping, traceroute, conditional debug, and show commands
are right there.

### See it on a real device
```
show monitor session all
show processes cpu
```
