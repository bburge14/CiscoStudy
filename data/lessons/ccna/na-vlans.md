# VLANs & 802.1Q Trunking

Imagine one big open office. Everyone can overhear everyone else. Now imagine
putting up interior walls so the sales team and the finance team each get their
own room, even though they still share one building. A **VLAN** (Virtual LAN) is
one of those walls, built in software instead of out of drywall.

## What a VLAN really is

A VLAN is a separate **broadcast domain** living on one switch. A broadcast
domain is just a group of devices that hear each other's "shout to everyone"
messages. Put a device in VLAN 10 and it shares a conversation space with the
other VLAN 10 devices — and is walled off from VLAN 20.

> **One physical switch can pretend to be several separate switches. Each VLAN is
> its own little network, and devices in different VLANs cannot talk to each
> other on their own.**

Why can't they talk? Because they're in different broadcast domains, and a switch
only moves traffic *within* a domain. To get from one VLAN to another you need a
**router**, or an **SVI** (Switch Virtual Interface — a router function built into
the switch). That crossing is called **inter-VLAN routing**.

A port that belongs to just one VLAN, carrying that VLAN's traffic down to a
single endpoint like a PC or printer, is an **access port**. Its traffic is
**untagged** — the endpoint doesn't know or care what a VLAN is. Here's how you
create a VLAN and drop a port into it:

```
vlan 20
 name USERS
interface Gi0/5
 switchport mode access
 switchport access vlan 20
```

Read that top to bottom: `vlan 20` creates VLAN 20 and names it USERS. Then on
port Gi0/5 we say "you're an access port" and "you live in VLAN 20." Anything
plugged into Gi0/5 is now a member of VLAN 20.

## Trunks: carrying many VLANs down one cable

Here's the problem. VLANs usually span more than one switch. If VLAN 20 lives on
two switches, the single cable between them has to carry VLAN 20 traffic — plus
VLAN 10, plus VLAN 30 — all mixed together. When a frame arrives at the far
switch, how does it know which VLAN that frame belonged to?

The answer is **tagging**. A **trunk** is a link that carries many VLANs by
inserting a 4-byte **802.1Q tag** into each frame. Inside that tag is a 12-bit
**VLAN ID** — the number that says "this frame belongs to VLAN 20."

> The tag is a little sticky note the sending switch writes on every frame saying
> which VLAN it came from, so the switch at the other end can drop it into the
> right VLAN.

You turn a port into a trunk like this:

```
interface Gi0/1
 switchport trunk encapsulation dot1q   ! on switches that support ISL
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

The `encapsulation dot1q` line picks 802.1Q as the tagging method, and you only
need it on older switches that also understand Cisco's legacy ISL. `mode trunk`
makes the port a trunk, and `allowed vlan` lists which VLANs may cross it.

Let me walk a single frame across a trunk, slowly:

> A PC in VLAN 20 on SW1 sends a frame to a server in VLAN 20 on SW2.
>
> 1. SW1 receives the frame on an access port and knows it belongs to VLAN 20.
> 2. To send it over the trunk, SW1 writes an 802.1Q tag on it: "VLAN 20."
> 3. SW2 receives the tagged frame, reads "20," strips the tag off, and forwards
>    it only into VLAN 20.
>
> The tag is the whole reason VLAN 20 survived the trip between switches.

## The native VLAN (and why a mismatch bites)

There's one exception to all this tagging. On every trunk, one VLAN is sent
**untagged** — the **native VLAN**, which defaults to VLAN 1. It exists for older
gear that didn't understand tags. The catch: both ends of the trunk **must agree**
on which VLAN is native. If they disagree, you'll see a log like this:

```
%CDP-4-NATIVE_VLAN_MISMATCH: ... Gi0/1 (1), with SW2 Gi0/1 (99).
```

The sneaky part is that the trunk stays *up* — nothing goes down. But because one
switch thinks native is VLAN 1 and the other thinks it's VLAN 99, each one drops
its untagged frames into a *different* VLAN. Traffic quietly leaks from one VLAN
into another. That's both a bridging problem and a real security hole — it's the
basis of a VLAN-hopping attack. You fix it by matching the native VLAN on both
ends, for example `switchport trunk native vlan 99`.

## The `allowed vlan` trap

This one has caused real outages, so slow down:

```
switchport trunk allowed vlan 10,20,30      ! REPLACES the whole list
switchport trunk allowed vlan add 40        ! APPENDS 40
```

The first form *replaces* the entire allowed list. So if you meant to add VLAN 40
but you forget the word `add`, you wipe out 10, 20, and 30 and black-hole every
other VLAN on that trunk. The little word `add` is what appends instead of
replacing. Always ask yourself which one you mean.

## DTP: letting switches negotiate a trunk

Switches can decide between themselves whether a link becomes a trunk, using
**DTP** (Dynamic Trunking Protocol). The easiest way to understand it is to give
each mode a personality. An **access** port refuses to ever become a trunk. A
**trunk** port forces a trunk. A **dynamic desirable** port actively
asks the other side, "let's trunk." A **dynamic auto** port will only trunk if it
gets asked first — it never starts the conversation.

Once you see them that way, the outcomes follow. A desirable port forms a trunk
with anything except an access port. An auto port trunks only if the far side is
desirable or a forced trunk. A forced trunk facing an access port is a mismatch.
And the famous gotcha:

> **auto + auto = access.** Both sides are politely waiting to be asked, nobody
> asks, so no trunk ever forms.

Because negotiation is easy to get wrong, best practice is to hard-set the mode
yourself and switch negotiation off with `switchport nonegotiate`.

## The whole thing in one paragraph

A VLAN turns one switch into several separate networks, each its own broadcast
domain, and getting between them needs a router or an SVI. An access port carries
one VLAN untagged to an endpoint; a trunk carries many VLANs between switches by
writing a 4-byte 802.1Q tag (holding the 12-bit VLAN ID) onto each frame. One
VLAN per trunk rides untagged as the native VLAN (default VLAN 1), and both ends
must agree or untagged frames spill between VLANs. Remember that `allowed vlan`
without `add` replaces the whole list, and that two DTP auto ports never trunk.

### See it on a real device

```
show vlan brief
show interfaces trunk
show interfaces g0/1 switchport
```

Of these, `show interfaces trunk` is the fastest way to confirm a trunk's mode,
its native VLAN, and the allowed/active VLAN list all at once.
