# Device, Path & Network Virtualization

**Virtualization** is one idea wearing many hats: take something physical and make
it act like several separate things, or carry one network invisibly over another.
One real server pretending to be ten; one router keeping a dozen customers' traffic
from ever mixing; one Ethernet network stretched across the globe over the
Internet. This lesson walks through three places it shows up — inside a device,
across a path, and over a whole network.

A picture to carry through it all: an **apartment building**. One physical building
(the hardware) holds many apartments (the virtual pieces). Each tenant has their
own locked door and never sees the others, even though they share the same walls,
foundation, and plumbing.

## Virtualizing a device: hypervisors and containers

To split one physical computer into several **virtual machines** (VMs — complete
pretend computers, each with its own operating system), you need a **hypervisor**:
software whose job is to create and run those VMs and keep them apart. There are
two kinds, and telling them apart is the thing to nail.

A **Type 1 hypervisor** (called *bare-metal*) installs **directly on the
hardware**, with no operating system beneath it — the hypervisor *is* the base
layer. **VMware ESXi, KVM, and Hyper-V** are Type 1, and this is the data-center
standard because nothing sits in the way. A **Type 2 hypervisor** (called
*hosted*) runs as an **app on top of a normal operating system**, the way any
other program does — **VirtualBox** and **VMware Workstation** are Type 2, the kind
you'd run on your own laptop.

> **Type 1 sits straight on the hardware. Type 2 sits on top of a regular
> operating system.**

**Containers** (think **Docker**) are a lighter trick. Instead of each carrying a
full operating system, they **share the host's OS kernel** — like apartments
sharing one set of building utilities instead of each installing their own.
They're much lighter than VMs, but note: containers are **not** hypervisors.
Finally, a **vSwitch** is a virtual switch living in software inside a host; it
connects the VMs to the physical network.

## Virtualizing the network: VRF

Now move up from one box to the paths through it. A single router normally keeps
one routing table — one master map of where everything is. **VRF** (*Virtual
Routing and Forwarding*) lets it keep **several independent routing tables at
once**, each walled off from the others. It's like one post office sorting mail
into completely separate banks of mailboxes that never mix. That lets you run
several customers or tenants on one physical router with total isolation — and
because each VRF is its own private world, two customers can even use the *same*
(overlapping) IP addresses without any clash.

The simplest flavor, with no MPLS behind it, is called **VRF-Lite**. You configure
it like this:

```
vrf definition RED
 address-family ipv4
interface Gi0/1
 vrf forwarding RED          ! bind the interface (clears its IP — re-add it)
 ip address 10.1.1.1 255.255.255.0
```

Watch the order, because it trips people up: the moment you bind an interface into
a VRF with `vrf forwarding RED`, the router **wipes that interface's IP address**.
That's deliberate — the IP belonged to the old routing world. So you re-add the
address *afterward*, as the last two lines show. Do it the other way around and
your address vanishes.

## Virtualizing the path: GRE and IPsec

Sometimes you need to carry traffic across a network that wasn't built for it —
say, link two offices over the public Internet. That's a job for a **tunnel**:
wrap your traffic in an outer packet, ship it across, unwrap it at the far end.

**GRE** (*Generic Routing Encapsulation*) is the flexible wrapper. It can
encapsulate almost **any protocol inside IP, including multicast** (traffic sent
to many receivers at once) — which matters because routing protocols often lean on
multicast. Its catch: GRE offers **no encryption** on its own. It's a plain
envelope — it'll carry anything, but anyone who intercepts it can read what's
inside.

**IPsec** (using **ESP**) is the opposite trade-off: it gives you strong
**encryption and integrity**, but in tunnel mode it **doesn't natively carry
multicast or multiple protocols**. It's a locked, tamper-evident box — secure, but
picky about what it'll hold.

So you combine them. **GRE over IPsec** puts the flexible plain envelope *inside*
the locked box: GRE carries the multicast and routing, IPsec encrypts the whole
thing. That pairing is the usual answer whenever you need encrypted routing or
multicast across the Internet.

## Virtualizing a whole LAN: VXLAN

The last and biggest overlay is **VXLAN** (*Virtual Extensible LAN*). It lets a
**Layer 2** network (an Ethernet segment) stretch across a **routed Layer 3**
network underneath — so two servers can act like they're on the same LAN even when
there are routers between them.

It works by **MAC-in-UDP**: the original Ethernet frame (MAC addresses and all) is
wrapped inside a **UDP** packet aimed at **destination port 4789**, which can then
be routed anywhere. The device that does the wrapping and unwrapping is a **VTEP**
(*VXLAN Tunnel Endpoint*). Here's a frame's journey, step by step: a PC sends an
ordinary Ethernet frame; its local VTEP wraps it in that UDP packet, stamps a
segment number on it, and routes it across the underlay; the far VTEP receives it,
strips the wrapper off, and hands the original frame to the destination as if
nothing happened.

That "segment number" is the real payoff. Old VLANs use the **802.1Q** tag, which
is only **12 bits** — a hard ceiling of **4094** VLANs, nowhere near enough for a
big cloud data center. VXLAN's segment number, the **VNI** (*VXLAN Network
Identifier*), is **24 bits**, giving about **16 million** segments.

### How the VTEPs find each other: BGP EVPN

Left to itself, VXLAN learns where things are by **flooding** — shouting a frame
everywhere to see who answers. That's wasteful at scale. So a control plane is
added: **BGP EVPN** (Border Gateway Protocol Ethernet VPN). It advertises, ahead
of time, which endpoint **MAC/IP lives behind which VTEP** (these are **Type-2**
routes) and which **VTEPs belong to which VNI** (**Type-3** routes), so there's
far less flooding. Underneath it all, the underlay still needs an ordinary **IGP**
(*Interior Gateway Protocol*, like **OSPF** or **IS-IS**) just so the VTEPs can
reach one another in the first place.

> **Split the roles: VXLAN = data plane (encapsulation), BGP EVPN = control plane
> (reachability), IGP underlay = VTEP transport.**

## The whole thing in one paragraph

Virtualization makes one physical thing serve many. On a single box, a
**hypervisor** runs virtual machines — **Type 1** installs straight on the
hardware (ESXi, KVM, Hyper-V), **Type 2** runs on top of a normal OS (VirtualBox,
Workstation) — while **containers** share the host kernel and aren't hypervisors
at all. **VRF** gives one router several isolated routing tables (just remember
that binding an interface clears its IP, so re-add it). For tunnels, **GRE**
carries anything including multicast but encrypts nothing, so it's paired with
**IPsec** for security. And **VXLAN** stretches Layer 2 across a routed Layer 3
underlay as MAC-in-UDP on port **4789**, using a **24-bit VNI** for ~**16 million**
segments, with **BGP EVPN** as its control plane keeping track of which endpoint
sits behind which VTEP.

### See it on a real device

```
show vrf
show ip route vrf RED
```
