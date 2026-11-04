# Spanning Tree & EtherChannel

Networks use backup cables so that if one link breaks, a spare keeps traffic
flowing. But spare cables between switches hide a real danger, and Spanning Tree
is what makes them safe. Let's start with the danger — once you see it,
everything Spanning Tree does makes sense.

## Why loops are dangerous

Picture two switches joined by two cables instead of one, for safety. A PC sends
a broadcast — a message meant for *everybody* on the network. The first switch
floods it out every port, including both cables to the second switch, which
floods it back, and the first floods it again. The copies circle forever.

Why forever? A Layer 2 frame — the Ethernet envelope a switch forwards — has no
TTL. TTL ("Time To Live") is the countdown a Layer 3 packet carries so it
eventually dies, but a switched frame has none. Nothing stops the loop, so within
seconds the copies pile into a **broadcast storm** that eats all the bandwidth
and freezes the network.

> **STP's whole job is to leave exactly one working path between any two
> switches and quietly block the spare — then turn the spare back on the instant
> the main path fails.**

STP stands for **Spanning Tree Protocol**. The original is 802.1D; today Cisco
switches run Rapid-PVST+, based on the faster 802.1w standard. "Spanning tree" is
just a math term for "connect everything with no loops." So STP finds the
redundant links, blocks enough ports to kill every loop, and keeps one path
alive — re-opening a blocked port if a link ever dies.

## Electing the root bridge

To agree on which paths to keep, the switches first elect one switch as the
center of the map: the **root bridge**. Think of it as electing the town hall —
once everyone agrees where it is, each switch keeps its single best road toward
it and blocks the rest.

How do they vote? Each switch has a **Bridge ID**, made of **Bridge Priority +
the VLAN number (called sys-id-ext) + its MAC address**. The switch with the
**lowest Bridge ID wins** and becomes root. Here is exactly how they compare, and
it is the single most tested idea in the whole topic:

> **Compare the priority first — lowest priority wins. Only if two switches have
> the *same* priority do you fall back to the MAC address, where again the lower
> one wins.**

The default priority is **32768**, and you may only set it in steps of **4096**.
The classic trap is a switch with a tiny MAC address sitting next to a switch
with a *higher* priority number — and people pick the small MAC. Don't. Priority
is checked first every time; the MAC is only the tiebreaker.

You usually don't leave the root to chance, so you nudge the election:

```
spanning-tree vlan 10 root primary      ! macro → 24576 (or 4096 below current root)
spanning-tree vlan 10 root secondary    ! macro → 28672
spanning-tree vlan 10 priority 24576    ! explicit (multiples of 4096 only)
```

The `root primary` macro sets priority to **24576**, and `root secondary` sets
**28672** — low enough to win, with the secondary ready as runner-up.

## Port roles: which door stays open

Once the root is chosen, every switch labels its ports. On each non-root switch,
the one port with the best (lowest-cost) path *toward* the root is the **root
port**, and it forwards traffic. On every network segment, the port with the best
path *away* from the root is the **designated port** — there is one per segment,
and every port on the root bridge itself is designated. Designated ports forward
too.

The blocked ports get names as well. An **alternate port** is a blocked backup to
the root port — a spare way to reach the root. A **backup port** is a blocked
backup for a designated port on the same segment. Those are the spares STP holds
in reserve.

"Best path" is measured by **path cost**, based on link speed: faster links cost
less. A 10 Gb link is **2**, 1 Gb is **4**, 100 Mb is **19**, and 10 Mb is
**100**. (Older "long" cost values differ, but the relative order is the same —
faster always costs less.) A switch adds up the cost to the root and keeps the
cheapest way there as its root port.

## Protecting the edge ports

Ports where a PC or printer plugs in don't need the slow STP dance, and they
shouldn't be trusted to reshape the network. Two features handle that:

```
interface Gi0/5
 spanning-tree portfast             ! skip listening/learning on an access port
 spanning-tree bpduguard enable     ! err-disable if ANY BPDU arrives (rogue switch)
```

**PortFast** lets a host port skip the waiting stages and go straight to
forwarding, so a PC gets a working link right away. **BPDU Guard** watches that
same port: BPDUs (Bridge Protocol Data Units — the "hello" messages switches send
each other) should never arrive on a port meant for a PC, so if one does, someone
has plugged in a rogue switch. BPDU Guard shuts the port down (err-disables it)
to stop that switch from hijacking the topology.

A related guard, **Root Guard**, goes on a *designated* port. If a *superior* BPDU
shows up there — one claiming to be a better root — Root Guard puts the port into
a root-inconsistent (blocking) state until the offender goes quiet — stopping a
switch you don't control from stealing the root role.

## EtherChannel: turning many cables into one

Here's the happier side of redundant links. **EtherChannel** bundles **2 to 8**
physical links into one logical interface. STP treats the bundle as a single link
(one STP instance), so it never blocks the spares — you get the full combined
bandwidth, and if one cable fails the others carry on instantly.

For two switches to agree to bundle, they negotiate using one of two protocols —
or you skip negotiation entirely. One rule ties it all together: **at least one
side has to actively start the conversation.**

**LACP** (802.3ad, the vendor-neutral standard) uses the modes `active` and
`passive`; `active` starts the conversation, `passive` only answers. **PAgP**
(Cisco's own) uses `desirable` and `auto`; `desirable` starts, `auto` only
answers. **Static** uses `on`, which does no negotiating at all.

Now apply "someone must start." An LACP bundle forms with **active/active** or
**active/passive**, but **passive/passive fails** because neither side ever
begins. PAgP has the same shape: **desirable/desirable** and **desirable/auto**
form, but **auto/auto fails**. And `on` is the loner — **on/on** works, but
mixing `on` with `active` (or any other mode) **fails**. So the two dead
same-protocol pairs to remember are **passive/passive** and **auto/auto**, and
`on` only ever pairs with `on`.

```
interface range Gi0/1 - 2
 switchport mode trunk
 channel-group 1 mode active        ! LACP
```

One last catch: the member links must also match in speed, duplex, switchport
mode (access vs trunk), and allowed VLANs. If any of those differ, the links
won't bundle no matter which mode you picked.

## The whole thing in one paragraph

Redundant links would loop forever because a Layer 2 frame has no TTL, so
Spanning Tree blocks the spares to leave one loop-free path and re-opens them if
a link fails. Switches elect the root bridge by lowest Bridge ID — priority first
(default 32768, steps of 4096), MAC only as a tiebreaker. Each switch then
forwards on its lowest-cost root port and each segment's designated port, while
alternate and backup ports wait in blocking, and PortFast with BPDU Guard and
Root Guard protects the edge. EtherChannel bundles 2–8 links into one, forming
only when a side initiates (active or desirable) — never passive/passive or
auto/auto, and `on` only with `on`.

### See it on a real device
```
show spanning-tree vlan 10
show spanning-tree root
show etherchannel summary          ! Po1(SU) + members (P) = bundled
```
In `show etherchannel summary`, a member flag of `(P)` means bundled, `(I)`
stand-alone/individual, `(s)` suspended, and `(D)` down.
