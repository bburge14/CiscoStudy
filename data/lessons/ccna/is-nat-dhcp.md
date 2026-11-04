# NAT & DHCP

These two features quietly make a normal network usable on the internet. One lets
many devices share a single public address; the other hands out addresses
automatically so you don't have to type them in by hand. Let's take them one at a
time.

## NAT: one public address for a whole network

Your ISP usually gives you just one public IP address, but your office or home has
dozens of devices. NAT (Network Address Translation) is the trick that lets them
all share it. As a packet crosses the border between your network and the
internet, NAT rewrites the address on it — swapping the private inside address for
the public one on the way out, and swapping it back on the way in.

Think of a big office with one public phone number. Inside, everyone has a private
extension. When a call goes out, the outside world only ever sees the main number,
never the extension. NAT is the switchboard doing that swap.

> **NAT rewrites the IP address on a packet as it crosses the boundary between
> "inside" (your network) and "outside" (the internet), so private addresses can
> hide behind a public one.**

### The four names for an address

NAT gives the same device two names — one used inside, one used outside — and it
does the same for the server you're talking to. Two words carry all the meaning.
*Inside* means a device that lives in your network; *outside* means a device out on
the internet. *Local* means the address as it looks from inside your network;
*global* means the address as it looks from the outside world.

Put those together and you get four combinations. Your PC's private address (say
`10.0.0.5`) is its inside local address — the name it uses at home. After NAT
swaps it for the public address, that public address is its inside global address —
the name the world sees. Going the other way, the server you're visiting has an
outside local address (how it appears from inside) and an outside global address
(its real public address out on the internet). For most work the two that matter
are inside local and inside global — the private and public faces of your own
device. Here's the whole grid in one small box:

| | Local (seen inside) | Global (seen outside) |
|--|--------------------|----------------------|
| **Inside** | inside local (private host) | inside global (public, after NAT) |
| **Outside** | outside local | outside global (real public server) |

### Three flavors of NAT

There are three ways to do the swap. Static NAT is a fixed one-to-one mapping — one
private address always maps to the same public one, which is what you use for a
server that people on the internet need to reach at a steady address. Dynamic NAT
also maps one-to-one, but it hands out public addresses from a pool, and a given
mapping only lasts as long as it's in use.

The one you'll meet most is PAT (Port Address Translation), also called overload.
PAT is many-to-one: it squeezes a whole network behind a single public IP by also
tracking the Layer 4 source port of each conversation. Because every outbound
connection gets its own port number, the router can tell the replies apart even
though they all share one address — that's the office phone extension in our
analogy. PAT is what shares one public IP among a whole office.

Here's how you turn on PAT:
```
interface Gi0/0
 ip nat inside
interface Gi0/1
 ip nat outside
access-list 1 permit 10.0.0.0 0.0.0.255
ip nat inside source list 1 interface Gi0/1 overload   ! PAT
```
You mark one interface `ip nat inside` and the internet-facing one `ip nat
outside` so the router knows which way is which. The access list picks which
inside addresses get translated. And the giveaway that this is PAT rather than
plain dynamic NAT is the `overload` keyword at the end — whenever you see
`overload`, think PAT.

## DHCP: addresses handed out automatically

Nobody wants to type an IP address, gateway, and DNS server into every laptop by
hand. DHCP (Dynamic Host Configuration Protocol) does it for them. When a device
joins the network, it asks for its settings and a server hands them over on a
lease.

The conversation has four steps, and they spell **DORA**. Picture checking into a
hotel. First the client shouts **Discover** to the whole network — "is there a
DHCP server out there?" — as a broadcast, because it doesn't yet know who to ask. A
server answers with an **Offer**: "here's an address you can have." The client
replies with a **Request** (also a broadcast, so any other servers learn it chose
this one): "yes, I'll take that one." Finally the server sends an **Ack** to
confirm, and the address is leased. Discover, Offer, Request, Ack — DORA.

A router can be the DHCP server itself:
```
ip dhcp excluded-address 10.0.0.1 10.0.0.10   ! reserve gateway/servers
ip dhcp pool LAN
 network 10.0.0.0 255.255.255.0
 default-router 10.0.0.1
 dns-server 8.8.8.8
```
The `excluded-address` line sets aside addresses you don't want given out — like
the gateway and your servers, which need fixed addresses. The pool then defines
the network to lease from, the default gateway clients should use, and the DNS
server to tell them about.

### When the server is on another subnet

Here's a snag. The Discover and Request messages are broadcasts, and a router will
not forward a broadcast. So if the DHCP server sits on a different subnet from the
clients, their shouts never reach it. The fix is a DHCP relay. On the client-facing
interface you tell the router where the server really is, and the router quietly
repackages the broadcast as a unicast aimed straight at it:
```
interface Vlan10
 ip helper-address 10.9.9.9
```
As a bonus, `ip helper-address` also relays a handful of other important UDP
broadcasts a client might need — things like DNS, TFTP, and NTP.

## DNS, briefly

One more everyday helper: DNS (Domain Name System) turns names you can remember
into the IP addresses machines actually use. On a Cisco device you point it at a
name server and switch lookups on:
```
ip name-server 8.8.8.8
ip domain-lookup
```

## The whole thing in one paragraph

NAT rewrites addresses at the border between your network and the internet so many
private devices can share scarce public addresses; the same device is known by its
inside local (private) name at home and its inside global (public) name outside,
and the version you'll use most, PAT — flagged by the `overload` keyword — fits a
whole network behind one public IP by tracking Layer 4 ports. DHCP hands out
addresses automatically through the four-step DORA exchange (Discover, Offer,
Request, Ack), a router can host the pool itself, and when the server lives on
another subnet you add `ip helper-address` so the router relays the clients'
broadcasts to it as unicast. And DNS, the last piece, simply translates names into
IP addresses.

### See it on a real device
```
show ip nat translations
show ip dhcp binding
show ip interface g0/0 | include Helper
```
