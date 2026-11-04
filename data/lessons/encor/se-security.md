# Security: AAA, CoPP, TrustSec, 802.1X & Wireless

Most network security boils down to two everyday questions: *Who are you?* and
*What are you allowed to do?* Get those right, protect the device itself from
being overwhelmed, and you've covered most of this topic.

Picture a secure office building. There's a front desk that checks your ID, a
badge that opens only certain doors, and a logbook recording where you went.
Networks do the same thing — just for laptops, phones, and admins instead of
people.

> **Authentication** asks *"who are you?"*, **authorization** asks *"what are you
> allowed to do?"*, and **accounting** records *"what did you actually do?"*
> These three — together called **AAA** — are the backbone of access control.

## Two AAA servers: TACACS+ and RADIUS

When you centralize AAA on a server instead of configuring passwords on every
box, you'll use one of two protocols, and they're built for different jobs.

**TACACS+** is for **device administration** — controlling humans who log into
the switch or router itself. Think of it as a strict concierge who checks *every
single command* you type and writes it all down. It runs over **TCP port 49**,
encrypts the **entire payload** (not just the password), and keeps the three A's
separate. Because it separates authorization from authentication, it can do
**per-command authorization**: deciding command by command what an admin may
run, with full command accounting.

**RADIUS** is for **network access** — deciding whether an endpoint (a laptop, a
phone) is even allowed onto the network, and it's what 802.1X uses. It's the
bouncer at the front door. RADIUS runs over **UDP** (ports 1812/1813), encrypts
**only the password** (leaving the rest readable), and **combines**
authentication and authorization into one step, so its per-command control is
limited.

So the rule of thumb: reach for **TACACS+** when you want granular CLI command
authorization and full command logs for your admins, and **RADIUS** when you're
authenticating endpoints onto the network.

## CoPP: a bodyguard for the device's brain

A switch or router has two "planes." The **data plane** forwards ordinary
traffic in hardware, very fast. The **control plane** is the device's brain —
the CPU that handles management sessions, routing updates, ICMP, and odd
exceptions. Here's the danger: a flood of junk aimed *at the device itself* can
swamp that CPU and take the whole box down, even though normal forwarding would
have been fine.

**CoPP** (Control Plane Policing) is the fix. It applies a **QoS**
(quality-of-service) rate-limit policy to traffic that gets *punted* up to the
control plane, so a flood gets capped before it can exhaust the CPU. Transit
traffic that's just passing through in hardware is untouched.

```
policy-map COPP
 class MGMT
  police 8000 conform-action transmit exceed-action drop
control-plane
 service-policy input COPP
show policy-map control-plane
```

Reading it: traffic matching class `MGMT` is policed to 8000 — anything within
the limit is transmitted, anything over is dropped — and that policy is attached
inbound to the `control-plane`. In one line: CoPP protects the CPU.

## 802.1X: showing your ID at the port

**802.1X** is how a network makes a device prove its identity *before* the
switch port will carry its traffic. There are three roles. The **supplicant** is
the endpoint (your laptop) — the person showing ID. The **authenticator** is the
switch or WLC (wireless LAN controller) — the guard at the door, who relays the
request but doesn't decide. The **authentication server** is **Cisco ISE** (a
RADIUS server) — the records office that actually says yes or no.

The handshake uses **EAP** (Extensible Authentication Protocol). EAP runs over
the LAN — called **EAPoL** (EAP over LAN) — between the supplicant and the
switch; then the switch carries that EAP exchange inside **RADIUS** up to ISE.
If a device can't do 802.1X (say, a printer), there are fallbacks: **MAB** (MAC
Authentication Bypass), which admits it based on its MAC address, and **web
authentication**, a login web page.

## Cisco TrustSec: policy by group, not by address

Traditional rules are tied to IP addresses and subnets, which breaks the moment
a device moves or re-addresses. **Cisco TrustSec** fixes that by tagging traffic
with a **Security Group Tag (SGT)** based on *who* the user or device is, then
enforcing rules with **SGACLs** (Security Group ACLs) that reference those tags.

The analogy is a wristband at a festival. When you arrive, you're classified and
given a colored wristband (your SGT). The rules at each stage are written about
*wristband colors*, not about where you happen to be standing — so the policy
follows the **group**, not the IP or subnet, which decouples it from the
topology. Tags travel either **inline** (carried in the **CMD** header on the
frame) or via **SXP** (SGT Exchange Protocol) where inline isn't possible.
**ISE** is the policy brain that hands out the tags and rules.

```
show cts role-based sgt-map all
show cts environment-data
```

## Wireless security: why WPA3 is better

Wi-Fi comes in a **Personal** flavor (a shared password, or PSK, confirmed by a
4-way handshake) and an **Enterprise** flavor (full 802.1X/EAP, so each user
authenticates individually). **WPA2** supports both.

**WPA3** is the upgrade, and its headline feature for Personal mode is **SAE**
(Simultaneous Authentication of Equals, nicknamed "Dragonfly"). SAE matters for
two concrete reasons: it gives **forward secrecy** (capturing today's traffic
won't let an attacker decrypt it later even if they learn the password), and it
resists **offline dictionary attacks** (an attacker can't grab the handshake and
grind through password guesses at leisure). WPA3-Enterprise also offers a
stronger **192-bit** security suite. Meanwhile **WEP** (which used the weak RC4
cipher) and **Open** authentication are insecure and legacy — don't use them.

## A few more Layer 2 and Layer 3 protectors

Several smaller features guard specific attack surfaces. **uRPF** (Unicast
Reverse Path Forwarding) drops spoofed sources that fail a reverse-path check —
if a packet claims an address the router wouldn't route back out that way, it's
bogus. At Layer 2, **DAI** (Dynamic ARP Inspection), **DHCP snooping**, and
**port security** stop ARP spoofing, rogue DHCP servers, and MAC floods. And as
you just saw, **CoPP** protects the CPU.

## The whole thing in one paragraph

Security here is mostly identity and permission. AAA — authentication,
authorization, accounting — is centralized on a server using either TACACS+ (TCP
49, full-payload encryption, per-command authorization, for device admins) or
RADIUS (UDP, password-only encryption, for getting endpoints onto the network).
CoPP rate-limits traffic headed to the control plane so a flood can't crush the
CPU. 802.1X has a supplicant (endpoint), an authenticator (switch/WLC), and an
authentication server (ISE), with EAPoL to the switch and RADIUS onward, plus
MAB and web auth as fallbacks. TrustSec tags traffic with an SGT and enforces
with SGACLs so policy follows the group instead of the IP. And on wireless,
WPA3's SAE brings forward secrecy and resistance to offline guessing, leaving
WEP and Open in the past.

### See it on a real device
```
show policy-map control-plane
show cts role-based sgt-map all
```
