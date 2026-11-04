# Wireless Architecture & Discovery Protocols

Wi-Fi can feel like magic, but underneath it's just radios following polite
rules. Let's build the picture up one piece at a time, starting with how devices
share the air.

## How Wi-Fi shares the air

Wi-Fi is **half-duplex** shared media. Half-duplex means only one device can talk
at a time on a channel, like a walkie-talkie — you talk, then I talk, never both
at once. "Shared media" means everyone is using the same airspace, the way a
group of people shares one room.

So how do they avoid talking over each other? With a rule called **CSMA/CA**
(Carrier Sense Multiple Access with Collision Avoidance). In plain words: before a
device transmits, it listens; if the air is busy it waits; and it works hard to
*avoid* two devices speaking at once. (Wired Ethernet can detect a collision after
it happens, but a radio can't hear itself transmit, so wireless has to avoid
collisions instead of detecting them.)

Wi-Fi runs on two main bands, and they trade off in opposite directions. The
**2.4 GHz** band travels farther and punches through walls better, but it's
crowded and interference-prone, and it has only **3 non-overlapping channels** in
the US: **1, 6, and 11**. Any other pair of channels bleeds into each other. The
**5 GHz** band has many more channels and far less congestion, but its range is
shorter. So think 2.4 GHz for reach, 5 GHz for clean, fast air.

A few names you'll meet constantly: an **SSID** (Service Set Identifier) is simply
the network name you pick from the Wi-Fi list, like "CoffeeShop-WiFi." A **BSS**
(Basic Service Set) is the coverage bubble of one single AP (Access Point — the
radio box on the ceiling), and that bubble is identified by the AP radio's MAC
address, called the **BSSID**. An **ESS** (Extended Service Set) is several APs
sharing one SSID so you can walk through a building while your phone hops between
them without dropping — that hopping is **roaming**.

## Two ways to run your APs

There are two architectures, and this is the big idea of the lesson. An
**autonomous AP** is self-contained — its own little boss. You configure each AP
one at a time. That's fine for three APs and miserable for three hundred.

The other way splits the work. You pair **lightweight APs** with a **WLC**
(Wireless LAN Controller), one central brain. The lightweight AP handles only the
real-time 802.11 radio jobs — **beaconing** (announcing the network), **ACKs**
(acknowledging frames), and **encryption**. Everything else — management, roaming,
security, and **RF** (radio frequency) tuning — is handled by the WLC. Splitting
the jobs this way is called **split-MAC**, and it's what lets one team run
hundreds of APs.

> In the controller model, the AP is just a radio and the WLC is the brain. You
> configure things once on the controller instead of touching every AP.

So how does a lightweight AP reach its controller? Over a tunnel called
**CAPWAP** (Control And Provisioning of Wireless Access Points) — a private pipe
running through the ordinary wired network. CAPWAP actually builds *two* tunnels:
a **control** tunnel on UDP port **5246**, encrypted with **DTLS**, and a **data**
tunnel on UDP port **5247** (encrypting that data is optional). Because client
traffic rides this tunnel back to the controller, the AP's VLANs and SSIDs are
defined centrally on the WLC rather than on each AP. (CAPWAP replaced an older
protocol called LWAPP.)

Let me walk through an AP coming to life, nice and slow:

> A new ceiling AP powers on in its default "local" mode.
>
> 1. It boots and finds its WLC on the network.
> 2. It builds the CAPWAP control tunnel to the WLC on UDP 5246, protected by
>    DTLS.
> 3. It builds the CAPWAP data tunnel on UDP 5247.
> 4. Now a laptop associates to the AP. Its traffic doesn't drop straight onto the
>    local wire — it rides the data tunnel all the way back to the WLC, which
>    places it on the correct VLAN.
>
> That last step is why it's called **central switching**: the WLC, not the AP,
> decides where client traffic goes.

## AP modes and WLC interfaces

A lightweight AP can run in several modes. The default is **Local**, the central
switching you just saw, where client traffic is tunneled back to the WLC.
**FlexConnect** is branch mode: the AP can switch client traffic **locally** —
dropping it straight onto the branch LAN instead of hauling it across the WAN to a
distant WLC — and if the link to the WLC fails it keeps serving already-
authenticated clients in **standalone** mode, so a branch office doesn't go dark
when the WAN hiccups. There are also specialized roles: **Monitor**, **Sniffer**,
**Rogue detector**, and **Bridge (mesh)**.

On the controller itself, a few interface types show up. The **management
interface** is used for in-band WLC management and for APs to join it. A
**dynamic (WLAN) interface** maps an SSID/WLAN to a VLAN. And the **virtual
interface** is used for client web-authentication and DHCP relay, often shown with
an address like 192.0.2.1.

## Knowing your neighbors: CDP vs LLDP

Finally, a switch or router can discover what's plugged into it, which is handy
for mapping a network. Two protocols do this, and both learn the same things about
a directly connected neighbor — its device ID, the port it connects through, its
platform, VLAN, and power info.

**CDP** (Cisco Discovery Protocol) is Cisco's own. It's **on by default**, it
sends a hello every **60 seconds**, and it holds a neighbor's info for **180
seconds**. **LLDP** (Link Layer Discovery Protocol) is the open **IEEE 802.1AB**
standard. It's **off by default** (turn it on with `lldp run`), sends a hello
every **30 seconds**, and holds for **120 seconds**. Both operate at Layer 2.
Reach for LLDP when you have gear from multiple vendors, since not everything
speaks Cisco's CDP.

## The whole thing in one paragraph

Wi-Fi is half-duplex shared media that uses CSMA/CA to take turns, on a 2.4 GHz
band with long range but only three clean channels (1, 6, 11) or a 5 GHz band
with more channels and shorter range. You can run APs autonomously, one config
each, or split the work: lightweight APs do the radio while a WLC is the brain,
joined by CAPWAP tunnels (control on UDP 5246 with DTLS, data on UDP 5247). Local
mode tunnels traffic back to the WLC while FlexConnect switches it locally and
survives a WLC outage. And to see your neighbors, CDP (Cisco, on by default) or
LLDP (IEEE 802.1AB, off by default) both report who's on the other end of a link.

### See it on a real device

```
show cdp neighbors detail
show lldp neighbors detail
```
