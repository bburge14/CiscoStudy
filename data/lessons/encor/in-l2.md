# Advanced Layer 2 & EtherChannel

Two jobs in this lesson, and they're cousins. The first is guarding the loop-free
switched network that Spanning Tree already built for you. The second is bundling
several cables into one with EtherChannel. Both are about making a network of
switches sturdy — one keeps loops from ever forming, the other adds bandwidth and
a safety net. Take them one at a time.

## Keeping Spanning Tree honest

Quick refresher: switches can't have loops, because a loop makes a frame circle
forever and melts the network. Spanning Tree Protocol (STP) prevents that by
having switches talk to each other with little heartbeat messages called BPDUs
(Bridge Protocol Data Units), then blocking just enough links so there's exactly
one path between any two points.

That works great — until something unexpected happens on a port. The STP
protection features are watchdogs. Each one watches a single port for one specific
kind of "that shouldn't happen," and reacts instantly. The trick to remembering
them is to ask: *what surprised the watchdog?*

**BPDU Guard** lives on your PortFast access ports. A PortFast port is one where
you've told the switch "a PC or printer lives here, skip the slow loop checks and
come up right away." But a PC never sends BPDUs — only switches do. So if *any*
BPDU shows up on that port, it means somebody plugged a switch in where only an
end device belongs. BPDU Guard's answer is blunt: shut the port down into the
err-disable state. Better a dead port than a surprise loop.

**Root Guard** lives on the ports facing other switches (the designated ports).
You carefully chose which switch is the root — the center of the tree. You don't
want some random switch in a closet suddenly claiming to be a better root. A
switch making that claim sends a *superior* BPDU (one that looks better than your
current root's). When Root Guard sees a superior BPDU, it refuses to believe it
and parks the port in a root-inconsistent (blocking) state until the superior
BPDUs stop.

**Loop Guard** is the mirror image, and this is the part people mix up. It lives
on the ports that are safely blocked precisely *because* they keep hearing BPDUs
(the non-designated root and alternate ports). Those BPDUs are what tell the port
"stay blocked, the path is covered." The danger is a link that quietly goes
one-way (a unidirectional failure): the BPDUs stop arriving, STP thinks the path
is gone, and it opens the port to forwarding — creating a loop. Loop Guard watches
for exactly that: if the BPDUs it was relying on *stop* coming, it holds the port
in a loop-inconsistent (blocking) state instead of opening it.

Here's the one distinction worth burning in, because the exam loves it:

> **BPDU Guard reacts to a BPDU *arriving* where none should (→ err-disable). Loop
> Guard reacts to BPDUs that *stopped* arriving where they should keep coming (→
> block). Root Guard reacts to a *superior* BPDU (→ root-inconsistent).** One is a
> surprise guest, one is a guest who vanished, one is a guest claiming the throne.

Two smaller helpers round it out. **BPDU Filter** on PortFast ports simply
suppresses sending and receiving BPDUs on that port. And **UDLD** (UniDirectional
Link Detection) watches fiber links for that same one-way failure at the physical
level, and will err-disable or warn when it finds a link that only carries traffic
in one direction.

## Two flavors of Spanning Tree

Cisco runs **Rapid-PVST+**, which stands up one fast Spanning Tree (RSTP, Rapid
Spanning Tree Protocol) instance for *every* VLAN. It converges quickly and is the
default on many Cisco platforms. Its port states are simpler than old STP:
discarding, learning, forwarding. The upside is you can tune each VLAN's tree on
its own. The downside is cost: a thousand VLANs means a thousand instances, and
that burns CPU and floods BPDUs.

**MST** (Multiple Spanning Tree, standard 802.1s) is the fix. Instead of one tree
per VLAN, it maps many VLANs onto just a few instances — so those thousand VLANs
might share two or three trees, cutting the CPU and BPDU load sharply. The catch:
switches only share instances if they're in the same MST *region*, and they're
only in the same region if they agree on three things exactly — the region name,
the revision number, and the VLAN-to-instance mapping. Miss any one and a switch
quietly ends up in its own region.

## EtherChannel: many cables, one link

EtherChannel bundles several physical links between two switches into one logical
link. Picture a store opening several checkout lanes that ring up as a single
register: more throughput, and if one lane closes the others keep serving. STP
sees the bundle as a single link, so there's no loop to block, and you get the
full combined bandwidth.

For the bundle to form, both ends have to agree, and there are three ways to set
that up. The insight that makes the mode matrix click is simple: **a bundle forms
only if at least one side actively asks.** With LACP (Link Aggregation Control
Protocol, the open standard), the modes are *active* (I'll ask) and *passive*
(I'll answer if asked) — so active/active works, active/passive works, but
passive/passive fails because nobody ever asks. With PAgP (Port Aggregation
Protocol, Cisco's own), the modes are *desirable* (asks) and *auto* (answers) — so
desirable/desirable and desirable/auto work, but auto/auto fails for the same
reason. And static mode **on** does no negotiating at all, so **on** only pairs
with **on**.

Once bundled, how does traffic spread across the links? EtherChannel hashes each
*flow* — one conversation, one source/destination pair — onto exactly **one**
member link, and keeps it there. It never splits a single conversation across
links, because that would reorder the packets. The consequence trips people up: if
one heavy source/destination pair is swamping a single link, adding more links or
more VLANs won't help that one conversation. The fix is to give the hash more to
chew on — more entropy — so flows spread out:

```
port-channel load-balance src-dst-port     ! include L4 ports
show etherchannel load-balance
```

For links to bundle at all, the members must match in speed, duplex, trunk mode,
and allowed VLANs. If one doesn't line up, it won't join — and `show etherchannel
summary` will flag it as `(I)` for individual or `(s)` for suspended.

A couple of LACP extras are worth knowing. A bundle can have at most 8 active
links; if you cable up more than that, the system priority and port priority
values decide which links are active and which sit as hot standby. And `lacp rate
fast` tells LACP to send its LACPDUs every 1 second instead of the default 30
seconds, so a failed link is noticed much sooner.

## The whole thing in one paragraph

Spanning Tree keeps a switched network loop-free, and the protection features are
watchdogs on top of it: BPDU Guard err-disables a PortFast port the moment any
BPDU arrives there, Root Guard blocks (root-inconsistent) a port that hears a
superior BPDU trying to steal the root, and Loop Guard blocks (loop-inconsistent)
a port whose expected BPDUs suddenly stop — a surprise guest, a pretender, and a
vanished guest. Rapid-PVST+ runs one fast tree per VLAN while MST bundles many
VLANs into a few instances for switches that share a region name, revision, and
mapping. EtherChannel then ties several links into one, forming only when at least
one side actively asks (LACP active/passive, PAgP desirable/auto, or static
on/on), and balancing each conversation onto a single link — so you widen the
hash, not the VLAN list, when one link runs hot.

### A couple of commands to see this on a real device

```
show etherchannel summary
show etherchannel load-balance
```
