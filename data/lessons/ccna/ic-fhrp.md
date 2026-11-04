# First-Hop Redundancy Protocols (HSRP)

Here's a quiet weakness hiding in almost every network. Your PC knows exactly one
way out of its own subnet: its **default gateway**, the address of the nearby
router. Everything bound for the wider world goes there. So what happens if that
router dies? Even with a second, perfectly good router sitting right beside it,
your PC has no idea — it only knows the one gateway address, and it keeps sending
traffic into a dead end.

**First-Hop Redundancy Protocols (FHRPs)** fix this, and the idea is wonderfully
simple: let two or more routers *pretend to be a single router* by sharing one
**virtual IP address (vIP)** and one **virtual MAC address (vMAC)**. The hosts
point at that virtual address and never have to change it.

> **The hosts keep using one unchanging gateway address. Behind the scenes the
> routers quietly agree on who actually carries the traffic, and hand the job over
> if one of them fails — the host never notices.**

(A MAC address is a device's hardware address on the local network. A *virtual*
one is an address the routers can pass between themselves, and that is the key to
a failover the host can't see.)

## How HSRP works

**HSRP (Hot Standby Router Protocol)**, Cisco's version, picks one router to be
**Active** — it alone forwards traffic sent to the virtual IP. A second router
becomes **Standby**, watching and ready to step in. Any others simply **Listen**.
Here's a typical setup:

```
interface Vlan10
 ip address 10.0.0.2 255.255.255.0
 standby version 2
 standby 10 ip 10.0.0.1          ! the virtual IP (the hosts' gateway)
 standby 10 priority 110         ! default 100; higher wins
 standby 10 preempt              ! let a higher-priority router reclaim Active
```

Notice the router's own interface address is `10.0.0.2`, but the **virtual IP the
hosts actually use is `10.0.0.1`**. That shared `.1` is the gateway the PCs point
at. The `10` is the HSRP group number — the two routers must use the same group to
team up.

## Priority and preempt — the exam's favorite pair

How do the routers decide who is Active? By **priority**. The default is **100**,
and the **highest priority wins.** In the config above, this router's priority of
110 beats a neighbor left at the default 100, so it becomes Active.

But there's a subtlety the exam loves. Suppose the high-priority router reboots.
While it is down, the lower-priority router takes over as Active. When the first
router comes back, does it automatically reclaim the top job? Only if you turned on
**preempt**.

> Think of preempt as the right to take back the crown. **With `preempt`, a
> returning higher-priority router reclaims Active. Without it, whoever is
> currently Active simply keeps the role — even when a higher-priority router
> comes back online.**

There is also **tracking**, which makes priority smart. If the Active router's own
uplink fails, it is useless as a gateway even though it is still alive. Tracking
watches that uplink and *decrements* the priority when it goes down, so the
standby can take over:

```
standby 10 track 1 decrement 20
```

That line drops this router's priority by 20 if tracked object 1 fails — enough to
let the standby win and become Active.

## The virtual MAC address

When a host first sends to the virtual IP, it asks (via ARP) "what is the hardware
address for this gateway?" HSRP answers with a **virtual MAC**, not the real
router's MAC — and that is exactly what lets the role move between routers without
the host noticing. The virtual MAC follows a fixed pattern you should recognize:

- **HSRPv1** uses `0000.0C07.ACxx`, where `xx` is the group number in hexadecimal.
- **HSRPv2** uses `0000.0C9F.Fxxx`, where `xxx` is the group.

Version 2 is the more capable one: it supports group numbers all the way from **0
to 4095** and allows **millisecond timers** for faster failover.

## HSRP vs VRRP vs GLBP

HSRP isn't the only FHRP, and the exam expects you to tell three of them apart.
They all provide a redundant gateway, but they differ in who makes them and
whether they can spread traffic across the routers:

| | Vendor | Roles | Load balancing |
|--|--------|-------|----------------|
| HSRP | Cisco | Active/Standby | Only via multiple groups |
| VRRP | Open (IETF) | Master/Backup | Only via multiple groups |
| GLBP | Cisco | AVG + AVFs | **Native** (hands out different vMACs) |

The big distinction: with HSRP and VRRP only the one Active (or Master) router
forwards at a time — the standby just waits, so you can only balance load by
juggling multiple groups by hand. **GLBP (Gateway Load Balancing Protocol)** is
the only one that shares the load across gateways *by itself*. It elects an **AVG**
(Active Virtual Gateway) that answers ARP requests with **up to four different
virtual MACs**, quietly steering hosts to different forwarders (the **AVFs**,
Active Virtual Forwarders) so several routers carry traffic at once.

## The whole thing in one paragraph

A host knows only one default gateway, so a First-Hop Redundancy Protocol lets
several routers share one virtual IP and virtual MAC and present themselves as that
single gateway. In HSRP the highest **priority** (default 100) becomes the
**Active** router that forwards for the virtual IP, with a **Standby** waiting;
**preempt** decides whether a returning higher-priority router takes the role back
or lets the incumbent keep it, and **tracking** lowers priority when an uplink
fails. The virtual MAC is `0000.0C07.ACxx` in HSRPv1 and `0000.0C9F.Fxxx` in
HSRPv2, which also adds groups 0–4095 and millisecond timers. HSRP and VRRP keep
one forwarder at a time, while **GLBP** is the one that natively load-balances by
handing out up to four virtual MACs.

### See it on a real device
```
show standby brief
show standby
show glbp brief
```
