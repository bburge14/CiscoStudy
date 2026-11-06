# IPv4 Subnetting & IPv6

Addressing is where a lot of people slow down, so we'll go gently. The IPv4 half is
mostly counting; the IPv6 half is mostly new vocabulary. Get comfortable with both
and the rest of the exam's addressing questions fall into place.

## What an IPv4 address is made of

An IPv4 address is four numbers (0–255 each) separated by dots, like `192.168.1.10`.
Under the hood it's 32 on/off switches called **bits**, eight per number. Part of
the address names the **network** (the neighborhood) and the rest names the **host**
(the specific device). The line between the two is the **subnet mask**.

The mask is written two equivalent ways:

- long form: `255.255.255.0`
- CIDR / "slash" form: `/24`

`/24` means "the first 24 bits are the network; the last 8 belong to hosts." A
**bigger** slash locks more bits to the network and leaves **fewer** hosts.

> Each host bit **doubles** the number of addresses. And every subnet loses **two**
> addresses that can't go on a device: the **network address** (the first) and the
> **broadcast address** (the last). So usable hosts = 2^(host bits) − 2.

| Prefix | Mask | Total | Usable |
|-------:|------|------:|-------:|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /30 | 255.255.255.252 | 4 | 2 |

Every time the slash goes up one, the size halves. A `/30` gives exactly two usable
addresses, which is why it's the classic choice for a link between two routers.

## Finding the network an address lives in

Most subnet questions are really asking "which neighborhood, and where are its
edges?" You can answer by counting — no binary needed:

1. **Block size** = 256 − the interesting mask number (the one that's not 0 or 255).
2. **Count the edges** in that octet: start at 0 and add the block size repeatedly.
3. The **lower edge** is the network address; **one below the next edge** is the
   broadcast; everything between is usable.

> **Example — `172.16.20.75 /26`:** mask is `255.255.255.192`, so block size =
> 256 − 192 = **64**. Edges: 0, 64, 128, 192. The host `.75` sits in the **.64**
> block. Network = `172.16.20.64`, broadcast = `172.16.20.127`, usable = `.65`–`.126`.

### Special IPv4 ranges to recognize

The exam expects you to know the reserved ranges on sight:

- **Private (RFC 1918)** — not routable on the internet, used behind NAT:
  `10.0.0.0/8`, `172.16.0.0/12` (that's `172.16`–`172.31`), and `192.168.0.0/16`.
- **APIPA** — `169.254.0.0/16`. A host assigns itself one of these automatically when
  it wanted DHCP but got **no answer**. An APIPA address is a giant clue that the
  DHCP server is unreachable.
- **Loopback** — `127.0.0.0/8`, usually `127.0.0.1`. Pinging it tests the local
  TCP/IP stack without touching the wire.
- **CGNAT** — `100.64.0.0/10`, used by ISPs for carrier-grade NAT.

## IPv6: why, and how it's written

IPv4 ran out of addresses. IPv6 uses **128 bits** instead of 32, which is enough
addresses to never worry again. It's written as eight groups of four hex digits
separated by colons:

```
2001:0db8:0000:0000:0000:ff00:0042:8329
```

Two shortening rules make that readable:

1. **Drop leading zeros** in each group: `0db8` → `db8`, `0042` → `42`.
2. **Replace one run of all-zero groups with `::`** — but only **once** per address.

Applying both:

```
2001:db8::ff00:42:8329
```

> The `::` can appear **only once**, because a second one would make it impossible to
> know how many zero groups each stood for. Expect a question that asks you to spot
> the validly-abbreviated address.

### IPv6 address types

IPv6 has no broadcast at all — its jobs are done by multicast and anycast instead.
The types you must know:

| Type | Prefix | What it's for |
|------|--------|---------------|
| Global unicast | `2000::/3` | Public, internet-routable (like a public IPv4) |
| Unique local | `fc00::/7` (usually `fd00::/8`) | Private, internal-only (like RFC 1918) |
| Link-local | `fe80::/10` | Auto-configured, valid on one link only |
| Multicast | `ff00::/8` | One-to-group |
| Loopback | `::1` | The local host (like 127.0.0.1) |
| Unspecified | `::` | "No address yet" |

> **Every IPv6 interface always has a link-local `fe80::` address**, generated
> automatically, even if nothing else is configured. It's used for neighbor
> discovery and as the next-hop for routing on the local link.

### How IPv6 hosts get addresses

- **SLAAC (Stateless Address Autoconfiguration)** — the router advertises the
  network prefix (a Router Advertisement), and the host builds its own address by
  tacking on an interface ID. No DHCP server needed.
- **EUI-64** — one way to build that interface ID from the 48-bit MAC: split the MAC,
  insert `FFFE` in the middle, and flip the 7th bit. It makes a 64-bit host portion
  out of the hardware address.
- **DHCPv6** — a server can still hand out addresses (stateful) or just extra options
  like DNS (stateless), much as DHCP does for IPv4.

### Running both: dual stack and tunneling

Migrations rarely happen overnight, so devices often run **dual stack** — IPv4 and
IPv6 at the same time, choosing whichever the destination supports. Where only one
protocol exists in the middle, **tunneling** (such as 6to4 or GRE) wraps IPv6
packets inside IPv4 to carry them across. Neighbor Discovery Protocol (**NDP**) is
IPv6's replacement for ARP — it uses multicast to find neighbors' link-layer
addresses rather than broadcasting.

## On the exam

- Compute usable hosts with **2^(host bits) − 2**, and know the common prefixes
  (/24=254, /26=62, /30=2) cold.
- Use the **block size method** (256 − interesting octet) to find network, broadcast,
  and usable range for a given address and mask.
- Recognize reserved ranges instantly: **private 10/8, 172.16/12, 192.168/16;
  APIPA 169.254/16; loopback 127/8.** An APIPA address means DHCP failed.
- IPv6 is **128-bit hex**; shorten by dropping leading zeros and using `::` **once**.
- Match IPv6 types to prefixes: global `2000::/3`, unique local `fc00::/7`,
  **link-local `fe80::/10`** (always present), multicast `ff00::/8`, loopback `::1`.
- IPv6 has **no broadcast**. Know **SLAAC**, **EUI-64**, **DHCPv6**, **dual stack**,
  and that **NDP** replaces ARP.
