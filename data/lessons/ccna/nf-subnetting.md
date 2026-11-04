# IPv4 Addresses & Subnetting

Take this slowly — it's the one topic that unlocks half of networking. If you get
the single idea in the next section, the rest is just counting.

## What an IP address actually is

An IP address is like a mailing address for a device. If a switch or router is
going to send your traffic somewhere, it needs an address to send it *to*.

An IPv4 address is four numbers separated by dots, like `192.168.1.10`. Each of
those four numbers can be anywhere from 0 to 255. That's it — four numbers, each
0–255.

Here is the idea everything else depends on, so read it twice:

> **Part of the address names the *neighborhood*, and the rest names the
> *specific house* in that neighborhood.**

The "neighborhood" is called the **network**. The "house" is called the **host**
(your PC, phone, server — any single device). Devices in the same neighborhood
can talk to each other directly. To reach a device in a *different* neighborhood,
your traffic has to go through a **router** — think of the router as the road out
of your street.

So every address is really two things glued together: *which network* + *which
host on it*.

## The subnet mask is just the dividing line

If an address is "network part + host part," something has to say **where one
part ends and the other begins**. That's the whole job of the **subnet mask**.
It's a line drawn through the address.

You'll see the mask written two ways, and they mean the exact same thing:

- the long way: `255.255.255.0`
- the short way (a "prefix" or "slash"): `/24`

`/24` is just shorthand for "the first **24** pieces of the address belong to the
network; whatever's left belongs to the hosts." (An IPv4 address is made of 32
tiny on/off switches called *bits* — 8 per number — so `/24` means the first 24
switches are the network and the last 8 are free for hosts.)

One rule of thumb to hold onto:

> A **bigger** slash number means **more** of the address is locked to the
> network, which leaves **fewer** addresses for hosts. A **smaller** slash means
> a bigger neighborhood with more room.

So `/30` is a tiny neighborhood, and `/16` is a huge one.

## How many devices fit in a network?

The leftover "host" bits decide how many devices you can have. Here's the only
math you need: **each leftover bit doubles the number of addresses.**

A `/24` leaves 8 host bits, and 8 doublings is 256. So a `/24` has 256 total
addresses. But you don't get to use all 256 — **two of them are always reserved**
in every single network:

- the very **first** address is the network's own name (the *network address*)
- the very **last** address is the "announce to everyone here" address (the
  *broadcast address*)

You can't hand either of those to a device, so the real count is always **total
minus 2**. A `/24` gives you 256 − 2 = **254 usable** addresses.

You'll naturally memorize the common ones over time, but don't force it — here are
the ones you'll actually meet:

| Prefix | Total addresses | Usable (−2) |
|-------:|----------------:|------------:|
| /24    | 256             | 254         |
| /25    | 128             | 126         |
| /26    | 64              | 62          |
| /27    | 32              | 30          |
| /28    | 16              | 14          |
| /30    | 4               | 2           |

Notice the pattern: every time the slash goes **up by one**, the size gets **cut
in half**. `/30` is the one you'll see constantly for the link between two
routers, because such a link only ever needs 2 usable addresses.

## Finding which network an address belongs to (without binary)

Most subnet questions are secretly asking the same thing: *"Which neighborhood
does this address live in, and where are that neighborhood's edges?"* You can
answer that by counting — no binary conversions needed. Here's the trick:

**Step 1 — find the block size.** Look at the subnet mask and find the one number
that isn't 0 or 255 (the "interesting" number). Subtract it from 256. That's how
wide each neighborhood is.

> Example: a `/26` is mask `255.255.255.192`. The interesting number is 192.
> 256 − 192 = **64**. So neighborhoods are 64 addresses wide.

**Step 2 — count the neighborhood edges.** Start at 0 and keep adding the block
size: 0, 64, 128, 192. Your address falls between two of those marks.

**Step 3 — read off the answer.** The lower mark is the **network address**. One
less than the *next* mark is the **broadcast**. Everything in between is usable.

Let me walk one all the way through, nice and slow.

> **Question: what network does `172.16.20.75 /26` belong to?**
>
> 1. Block size = 256 − 192 = **64**.
> 2. Edges in that last number: **0, 64, 128, 192** (each 64 apart).
> 3. Where does **75** fall? It's bigger than 64 but smaller than 128, so it
>    lives in the **64 block** (the range .64 to .127).
> 4. So:
>    - Network address: `172.16.20.64`
>    - Broadcast address: `172.16.20.127` (one below the next edge, 128)
>    - Usable for devices: `172.16.20.65` through `172.16.20.126`
>
> Done — and we never touched binary.

If you can run those three steps, you can handle the large majority of subnetting
questions you'll ever see.

## Going the other way: "I need room for N devices"

Sometimes you're not handed a mask — you're asked to *choose* one. The question
sounds like *"I have about 50 computers on this floor; what size network do I
need?"*

Work it backwards: how many host bits give you at least 50 usable? Remember each
bit doubles, and don't forget the −2.

- 5 host bits → 32 total → 30 usable → not enough for 50.
- 6 host bits → 64 total → 62 usable → ✅ covers 50 comfortably.

6 host bits used for hosts means 32 − 6 = **/26**. So a `/26` is your answer.

And for a link between just two routers? That needs only 2 usable addresses, so a
`/30` (4 total, 2 usable) is perfect — no sense wasting a big block on a cable
with two ends. Right-sizing each network like this has a fancy name, **VLSM**
(Variable Length Subnet Masking), but all it means is *"use a block that fits
instead of one giant block for everything."*

## Wildcard masks: the subnet mask's mirror image

A bit later — when you configure access lists or OSPF — you'll run into a
**wildcard mask**, and it confuses almost everyone. So here it is as one simple
idea:

> **A wildcard mask is the subnet mask flipped around.**

A subnet mask says "these bits are the network, locked in place." A wildcard mask
answers the *opposite* question that a router asks when it's matching addresses:
*"which bits do I actually need to check, and which can I ignore?"* In a wildcard,
a **0 means "this bit must match"** and a **1 means "I don't care about this
bit."**

To turn a subnet mask into its wildcard, just subtract each of the four numbers
from 255:

- `255.255.255.0` (a /24) → `0.0.0.255`
- `255.255.255.192` (a /26) → `0.0.0.63`

So any time a command wants a "wildcard" and all you have is the subnet mask, flip
it: 255 minus each number. The single most common mistake here is typing the
subnet mask where a wildcard was wanted (or the reverse) — they look alike but
they're opposites, so always double-check which one the command is asking for.

## The whole thing in one paragraph

An IP address is split into a network part (the neighborhood) and a host part (the
specific device), and the subnet mask — written long like `255.255.255.0` or
short like `/24` — is simply *where* that split happens. The host bits that are
left over decide how many devices fit, and you always lose two addresses per
network (the network address and the broadcast). To find which network an address
belongs to, get the block size (256 minus the interesting mask number), count up
in those steps to find the edges, and read off the network (the lower edge) and
broadcast (one below the next edge). And a wildcard mask, which you'll meet soon,
is nothing more than the subnet mask flipped so a device knows which bits to pay
attention to.

### A couple of commands to see this on a real device
When you're ready to look at it live, these show an interface's address and the
networks a router knows about:

```
show ip interface brief
show ip route connected
```
