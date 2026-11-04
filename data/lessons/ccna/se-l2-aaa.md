# Layer 2 Security, AAA & VPN Concepts

A switch is trusting by nature. When something plugs into a port, the switch
happily learns about it and starts forwarding its traffic — no questions asked.
That trust is exactly what attackers abuse, and every tool in this lesson exists
to close one specific trick. Think of them as locks and ID checks on the doors
where devices plug in.

> **Most Layer 2 attacks work by abusing a switch's built-in trust, so most
> Layer 2 defenses work by making the switch stop trusting by default and trust
> only what you explicitly point it at.**

## Port security: only let known devices use a port

Every network card has a **MAC address** — a hardware "name tag" burned into it.
**Port security** lets an access port recognize only certain MAC addresses, or
only a certain *number* of them, and react when a stranger shows up.

```
interface Gi0/5
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

The interesting choice is what happens on a **violation** — when more or
different MACs appear than allowed. There are three modes, and they differ in two
ways: do they warn you, and do they shut the port. **`protect`** quietly drops
the offending traffic but never counts it or alerts you — the port stays up and
you hear nothing. **`restrict`** also drops the traffic, but it *does* increment a
counter and raise an alert, and the port stays up. **`shutdown`** — the default —
drops the traffic, counts it, *and* slams the port into an **err-disabled**
state, so nothing works on that port until someone fixes it. An easy way to
remember the chatty one: *restrict* restricts the traffic *and* tells you about
it.

That `sticky` line is a handy shortcut: instead of typing every allowed MAC by
hand, the port learns the MACs it actually sees and saves them into the running
config for you.

## DHCP snooping: stop a fake "front desk"

When a device joins a network, it usually asks a **DHCP** server for an address
and a gateway — like asking the front desk for your room key and directions. A
**rogue DHCP server** is an attacker pretending to be that front desk, handing
out wrong information to hijack your traffic. **DHCP snooping** stops this by
marking **every port as untrusted by default** and letting DHCP replies come
*only* from ports you explicitly trust — the ones facing your real server or
uplink.

```
ip dhcp snooping
ip dhcp snooping vlan 10
interface Gi0/1
 ip dhcp snooping trust          ! uplink toward the real DHCP server
```

While it watches, snooping also builds a **binding table** that records which
IP, MAC, and port belong together. That table is the foundation that both
Dynamic ARP Inspection and IP Source Guard build on.

## Dynamic ARP Inspection: catch the liars

**Dynamic ARP Inspection (DAI)** uses that snooping binding table to check **ARP**
messages — the little announcements that tie an IP address to a MAC address. If a
device claims an IP-to-MAC pairing that doesn't match the table, DAI drops it.
This stops **ARP poisoning** and the man-in-the-middle attacks built on it. As
with snooping, you trust the uplinks and inspect the access ports where users —
and attackers — sit.

## Which tool stops which attack

Each defense answers a specific attack, and matching them up is worth knowing by
heart:

| Attack | Mitigation |
|--------|------------|
| MAC flooding (CAM overflow) | Port security |
| Rogue DHCP / starvation | DHCP snooping (+ port security) |
| ARP spoofing / MITM | Dynamic ARP Inspection |
| Rogue switch / STP takeover | BPDU Guard / Root Guard |
| VLAN hopping | Disable DTP, change native VLAN, prune VLANs |

## AAA and 802.1X: checking ID at the port

**AAA** stands for three questions a network asks about a user: **Authentication**
(who are you?), **Authorization** (what are you allowed to do?), and
**Accounting** (what did you actually do?). These are usually answered by a
central **RADIUS** or **TACACS+** server rather than configured on each switch.

**802.1X** is the standard that puts that ID check right at the switch port, and
it has three roles worth picturing as people at a locked door. The **supplicant**
is the endpoint trying to get in — the client software on the laptop. The
**authenticator** is the **switch or WLC** holding the door: it doesn't decide
anything itself, it just relays the messages. The **authentication server** is
the **RADIUS** server (for example, Cisco ISE) that actually checks credentials
and says yes or no. The conversation between the supplicant and the authenticator
runs over **EAP** (specifically EAPoL, "EAP over LAN"); the authenticator then
carries that over **RADIUS** to the server.

## VPN concepts in brief

A **site-to-site IPsec** VPN joins two networks together securely across the
public Internet. Within IPsec, **ESP** gives you both encryption *and* integrity,
while **AH** gives integrity only — no encryption. **IKE** (also called
**ISAKMP**) is the part that negotiates the keys. Finally, **GRE** is a tunneling
method that can carry multiple protocols and multicast but adds *no* encryption on
its own, which is why it's often run as **GRE-over-IPsec** to get both.

## The whole thing in one paragraph

Switches trust by default, so Layer 2 security is about making them stop. Port
security limits which and how many MACs a port accepts, and its violation modes
are `protect` (silent drop), `restrict` (drop plus alert), and `shutdown` (drop
plus err-disable, the default). DHCP snooping distrusts every port until you trust
the one facing the real server, and it builds the IP-MAC-port binding table that
Dynamic ARP Inspection then uses to block ARP spoofing. AAA asks who you are, what
you may do, and what you did — usually through a RADIUS or TACACS+ server — and
802.1X enforces that at the port with a supplicant (the device), an authenticator
(the switch), and a RADIUS authentication server. For VPNs, remember site-to-site
IPsec joins two networks, ESP encrypts while AH only authenticates, IKE/ISAKMP
handles the keys, and GRE tunnels without encryption.

### See it on a real device
```
show port-security interface g0/5
show ip dhcp snooping
show authentication sessions
```
