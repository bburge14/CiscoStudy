# IPv6, the OSI Model, Transport & Switching

This lesson bundles four foundations: the new address format (IPv6), the map
networking uses to organize itself (the OSI model), the two ways data travels
(TCP and UDP), and how a switch actually moves traffic. Take them one at a time
and none of them is hard.

## Why IPv6, and how to read one

The old addresses, IPv4, give the world only about 4 billion addresses, and we
ran out. **IPv6** is the replacement, with a space so large we won't run out
again. An IPv6 address is **128 bits** — four times the size of IPv4's 32. We
write it as **eight groups of 16 bits each**, in **hexadecimal** (base-16, using
digits 0–9 and letters A–F), separated by colons. Each group is called a
**hextet**.

Written out in full, an address is long and full of zeros, so there are two
compression rules, used together. First, **drop the leading zeros** in each
hextet: `00AB` becomes `AB`, and `0000` becomes `0`. Second, replace the **single
longest run of all-zero hextets** with a double colon `::`.

> The `::` stands in for "a bunch of zero groups." Because a reader has to work
> out how many zeros it's hiding, you may use it **only once** in an address. Two
> of them would be ambiguous, so an answer with two `::` is always wrong.

Let me compress one all the way through:

> Compress `2001:0DB8:0000:0000:0000:00AB:0000:1234`.
>
> 1. Drop the leading zeros in each group: `2001 DB8 0 0 0 AB 0 1234`.
> 2. Find the longest run of zero groups. Positions three, four, and five are
>    three zeros in a row — longer than the lone zero near the end. Replace that
>    run with `::`.
> 3. Result: `2001:DB8::AB:0:1234`.
>
> Notice the single `0` near the end stays a `0`. The `::` was already spent on
> the longer run, and you only get one.

## The main address types

IPv6 has a few address flavors, and each has a job. A **global unicast** address
starts in the `2000::/3` range and is public and Internet-routable — it's the
IPv6 version of a public IPv4 address. A **unique local** address (`FC00::/7`,
with `FD00::/8` the part actually used) is private: it works inside your network
but is not routed on the Internet, like the old IPv4 private ranges.

A **link-local** address (`FE80::/10`) is created automatically on every
interface the moment IPv6 comes on. It's never routed off the local link, but
it's quietly essential — Neighbor Discovery (ND), OSPFv3, and router next-hops all
rely on it.

Finally, **multicast** (`FF00::/8`) matters because IPv6 has **no broadcast at
all**; the whole "send to a group" job is done by multicast instead. A few
well-known ones are worth knowing: `FF02::1` reaches all nodes, `FF02::2` reaches
all routers, and `FF02::5`/`FF02::6` are OSPFv3. One special form, the
**solicited-node multicast** address (`FF02::1:FFxx:xxxx`), is how Neighbor
Discovery finds a neighbor's MAC — the job ARP did back in IPv4.

## EUI-64: building the host part from a MAC

A host can build the back half of its address — the 64-bit **interface ID** — out
of its own MAC address. But a MAC is only 48 bits and we need 64, so **EUI-64** is
the recipe that stretches one into the other. Split the 48-bit MAC in half and
insert `FFFE` in the middle (that's the extra 16 bits), then **flip the 7th bit**
(the U/L, universal/local, bit) of the first byte.

> Start with MAC `001A2B-3C4D5E`.
>
> 1. Split it and insert `FFFE` in the middle:
>    `001A2B` + `FFFE` + `3C4D5E` = `001A2BFFFE3C4D5E`.
> 2. Flip the 7th bit of the first byte: `00` becomes `02`.
> 3. Result: `021A:2BFF:FE3C:4D5E`.
>
> That `00` → `02` flip is the step people forget — and it's exactly the one the
> wrong exam answers leave out.

## SLAAC vs DHCPv6: two ways to get an address

A host gets its address one of two ways. With **SLAAC** (Stateless Address
Autoconfiguration), the host listens for a **Router Advertisement (RA)** — a
message routers send announcing the `/64` prefix (the network part) for the link.
The host takes that prefix and builds the back half itself, using EUI-64 or a
random value. "Stateless" means no server keeps a record of who got what.

With **DHCPv6**, a server hands out addressing, much like IPv4's DHCP. It comes in
two flavors: **stateful**, where the server assigns the full address and tracks
it, and **stateless**, where SLAAC builds the address and DHCPv6 only supplies
extra options like DNS.

## The OSI model: data in nested boxes

Sending data is like shipping a gift in nested boxes. Each layer of the network
wraps your data in its own box with its own label, and the receiver unwraps them
in reverse. As data heads **down** the stack, this wrapping — called
**encapsulation** — adds a header at each step, and the unit (its **PDU**, or
Protocol Data Unit) gets a new name each time:

> **Segment (Layer 4) → Packet (Layer 3) → Frame (Layer 2) → Bits (Layer 1).**

On the receiving side, **de-encapsulation** unwraps the boxes in the reverse
order. The reason to know the layers is to know where each kind of address lives:
**port numbers at Layer 4, IP addresses at Layer 3, and MAC addresses at Layer
2.**

## TCP vs UDP: a phone call or a postcard

Two protocols carry your data at Layer 4, and they have opposite personalities.
**TCP** (Transmission Control Protocol) is like a phone call. It sets up a
connection first with a **three-way handshake** — **SYN**, then **SYN-ACK**, then
**ACK**, roughly "can you hear me? / yes, can you hear me? / yes." Then it
guarantees delivery: it acknowledges what arrived, retransmits what got lost, and
puts the pieces back in order. All that care costs **higher overhead**. TCP is
used where every byte must arrive: **HTTP(S), FTP, SSH, SMTP**.

**UDP** (User Datagram Protocol) is like dropping postcards in the mail. It's
**connectionless** and **best-effort** — fire and forget, with no acknowledgements
and no reordering. That means **lower overhead**, so it's fast and light. UDP is
used where speed beats perfection or a little loss is fine: **DNS, DHCP, TFTP,
SNMP, NTP, syslog**, and live voice/video (**RTP**).

Each service waits on a known **port number** — think of it as the apartment
number inside the building at an IP address. The ones worth memorizing: FTP
**20/21**, SSH **22**, Telnet **23**, DNS **53**, DHCP **67/68**, HTTP **80**,
HTTPS **443**, SNMP **161/162**, NTP **123**, and syslog **514**.

## How a switch moves frames

A switch is like a receptionist who learns where everyone sits. Every time a
frame comes in, the switch notes "this sender's MAC is on this port" — it
**learns source MACs** and records them in its **CAM table** (its MAC-address
table). Then it **forwards by destination MAC**: it looks up where the
destination sits and sends the frame only there.

That gives three cases. If the switch already knows the destination (a **known
unicast**), it sends the frame out the single port mapped to that MAC. If it
doesn't know the destination, or the frame is a broadcast or a multicast (an
**unknown unicast, broadcast, or multicast**), it **floods** the frame out every
port in that VLAN *except* the one it arrived on (the ingress port). Two bits of
vocabulary tie this off: each switch port is its own **collision domain** (its own
private lane, so no two devices fight over it), and each VLAN is one **broadcast
domain**.

## Cabling, quickly

Which cable you need comes down to whether the two devices are alike. A
**straight-through** cable connects **unlike** devices (switch to router, switch
to PC). A **crossover** cable connects **like** devices (switch to switch, router
to router, PC to PC). On modern gear, **Auto-MDIX** makes this a non-issue: when
it's enabled, the port works out the correct wiring itself.

## The whole thing in one paragraph

IPv6 stretches addresses to 128 bits written as eight hex hextets, shrunk by
dropping leading zeros and collapsing the longest zero run to a single `::`;
addresses come as global (public), unique local (private), link-local, or
multicast (there is no broadcast), and a host either builds its own from a Router
Advertisement (SLAAC, optionally via EUI-64 from its MAC) or gets one from a
DHCPv6 server. The OSI model wraps data layer by layer — Segment, Packet, Frame,
Bits — with ports at Layer 4, IP at Layer 3, and MAC at Layer 2. TCP is the
careful, acknowledged connection while UDP is fast fire-and-forget. And a switch
learns source MACs into its CAM table, forwards a known unicast out one port, and
floods everything else within the VLAN.

### See it on a real device

```
show ipv6 interface brief
show ipv6 neighbors
show mac address-table
```
