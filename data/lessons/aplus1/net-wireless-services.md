# Wireless, Network Services & Internet Links

This lesson covers the three things that turn a pile of hardware into a working
internet connection: the Wi-Fi standards that carry traffic through the air, the
services (DNS, DHCP, and friends) that make a network usable, and the physical
links that reach your ISP. We will go air → services → the wire to the world.

## Wi-Fi: the 802.11 family

All Wi-Fi follows the **802.11** standards, and each new letter is faster than
the last. You need the generations and, just as important, the **frequency bands**
they use.

| Standard | Also called | Band(s) | Rough speed |
|----------|-------------|---------|-------------|
| 802.11a  | —           | 5 GHz   | 54 Mbps |
| 802.11b  | —           | 2.4 GHz | 11 Mbps |
| 802.11g  | —           | 2.4 GHz | 54 Mbps |
| 802.11n  | Wi-Fi 4     | 2.4 & 5 GHz | 600 Mbps |
| 802.11ac | Wi-Fi 5     | 5 GHz   | ~1.3+ Gbps |
| 802.11ax | Wi-Fi 6/6E  | 2.4, 5, & 6 GHz | several Gbps |

The two classic bands trade **range for speed**, and the exam loves this
trade-off:

> **2.4 GHz** travels **farther** and through more walls, but is **slower** and
> crowded (microwaves, Bluetooth, neighbors). **5 GHz** is **faster** with more
> clear channels, but **shorter range**. **Wi-Fi 6E / 6 GHz** adds a brand-new,
> wide-open band for the newest devices.

### Channels, and the 2.4 GHz rule

Each band is divided into **channels**. In the crowded 2.4 GHz band, channels
overlap, and only three do **not** overlap:

> **In 2.4 GHz, use channels 1, 6, and 11** — they are the only non-overlapping
> set. Neighboring access points should use different ones from {1, 6, 11} to
> avoid interference.

5 GHz has many more non-overlapping channels, which is part of why it is less
congested. Wider channels (40/80/160 MHz) give more speed but leave fewer clear
channels — a speed-versus-crowding trade again.

### Other short-range wireless

Not everything is Wi-Fi. For the exam, recognize:

- **Bluetooth** — short-range accessory links (covered earlier).
- **NFC** — centimeter-range tap-to-pay.
- **RFID** — radio tags for badges, inventory, and access cards.
- **Zigbee** and **Z-Wave** — low-power mesh protocols for **smart-home / IoT**
  devices (bulbs, sensors, locks). Z-Wave uses sub-GHz radio for better range;
  Zigbee uses 2.4 GHz. Both are built for many tiny battery devices, not laptops.
- **Long-range fixed wireless** — a directional link beamed between two fixed
  points, used to bridge buildings or reach rural sites.

## Network services: the servers that make a network useful

A network is just plumbing until services run on it. Each service is a role a
server (or appliance) plays:

- **DNS server** — translates names (`example.com`) to IP addresses. Without it,
  nothing by name works.
- **DHCP server** — automatically hands clients an IP address, subnet mask,
  gateway, and DNS server. Without it you would configure every device by hand.
- **File server** — central shared storage.
- **Print server** — shares printers to many users.
- **Web server** — hosts websites (HTTP/HTTPS).
- **Mail server** — sends and stores email (SMTP/IMAP/POP3).
- **Proxy server** — sits between clients and the internet, fetching pages on
  their behalf; used for caching, content filtering, and privacy.
- **Authentication server** — verifies logins (often AAA / Active Directory).
- **Syslog server** — collects log messages from many devices in one place.
- **SIEM** — Security Information and Event Management: aggregates and correlates
  logs to spot security incidents.

### Internet appliances

Some services come as dedicated boxes:

- **Spam gateway** — filters junk and malicious email before it reaches users.
- **UTM** (Unified Threat Management) — an all-in-one security box combining
  firewall, antivirus, IDS/IPS, content filtering, and more.
- **Load balancer** — spreads incoming traffic across several servers so no one
  server is overwhelmed.
- **IDS / IPS** — an **IDS** *detects* and alerts on suspicious traffic; an
  **IPS** *prevents* it by actively blocking. (Detect vs prevent — an easy point.)

### Legacy and embedded systems

You will also see **legacy/embedded** systems: **SCADA/ICS** gear running factory
and utility equipment, and **IoT** devices (thermostats, cameras, doorbells).
They often cannot be patched easily, so they are usually isolated on their own
network segment.

## Configuring a SOHO network

A **SOHO** (Small Office / Home Office) network is built around that one all-in-
one wireless router. Common setup tasks:

- Give the Wi-Fi a clear **SSID** (network name) and a strong **WPA2/WPA3**
  passphrase; disable WPS if security matters.
- Let the router run **DHCP** for clients, or set reservations for servers.
- Open **port-forwarding** rules only for services you truly expose.
- Change the **default admin password** and keep firmware updated.

> A SOHO router *is* a router + switch + Wi-Fi AP + firewall + DHCP server + DNS
> forwarder in one box. Most "home networking" questions are really about one of
> those built-in roles.

## Reaching the internet: connection types

Finally, the link to your ISP. Know each type and its headline trait:

- **Fiber** — light through glass. **Fastest**, very low latency, symmetrical
  speeds possible. Terminates at an **ONT**.
- **Cable** — rides the coax of the cable-TV network via a **cable modem**. Fast
  and widely available; bandwidth is shared with the neighborhood, so it can slow
  at peak times.
- **DSL** — runs over the existing **telephone line** via a DSL modem. Slower
  than cable/fiber, and speed drops the farther you are from the phone exchange.
- **Satellite** — reaches remote areas via a dish to orbit. Works almost
  anywhere, but traditional satellite has **high latency** (the signal travels to
  space and back) and weather can disrupt it.
- **Cellular (4G/5G)** — the phone network as home/mobile internet; great for
  mobility, subject to signal strength and data caps.
- **WISP / fixed wireless** — a Wireless ISP beams a signal to an antenna on your
  building; common in rural areas without wired options.

> **If a question stresses highest speed and lowest latency, the answer is
> fiber.** If it stresses "available even in the remote countryside" with a
> latency downside, think **satellite**.

## The whole thing in one paragraph

Wi-Fi follows the **802.11** standards (a/b/g/n/ac=Wi-Fi 5/ax=Wi-Fi 6/6E), where
**2.4 GHz** reaches farther but is slower and crowded — use non-overlapping
channels **1, 6, 11** — while **5 GHz** (and new **6 GHz**) is faster but
shorter-range; short-range cousins include **Bluetooth, NFC, RFID,** and
**Zigbee/Z-Wave** for IoT. On top of the network run **services**: **DNS**
(names→IPs), **DHCP** (automatic addressing), plus file, print, web, mail, proxy,
authentication, and **syslog/SIEM** servers, and appliances like spam gateways,
**UTM**, load balancers, and **IDS (detect) / IPS (prevent)**. A **SOHO** router
bundles router, switch, AP, firewall, and DHCP into one box. The link to the ISP
is one of **fiber** (fastest, low latency, via an ONT), **cable** (coax modem,
shared), **DSL** (phone line, distance-limited), **satellite** (anywhere but high
latency), **cellular**, or **fixed wireless/WISP**.

## On the exam

- **2.4 GHz** = longer range, slower, crowded, channels **1/6/11**; **5 GHz** =
  faster, shorter range, more channels; **6 GHz** = Wi-Fi 6E.
- Map standards to speed/band: **ac (Wi-Fi 5) = 5 GHz**, **ax (Wi-Fi 6/6E) = all
  three bands**, **n = 2.4 and 5**.
- **Zigbee/Z-Wave** = smart-home/IoT mesh; **RFID** = tags/badges; **NFC** =
  tap-to-pay.
- **DNS** resolves names; **DHCP** hands out IP settings — the two services a
  client cannot live without.
- **IDS detects, IPS prevents.** **Proxy** = fetch/cache/filter on behalf of
  clients. **SIEM** = aggregate and correlate logs.
- Connection types: **fiber** fastest/lowest latency, **cable** shared coax,
  **DSL** phone-line/distance-sensitive, **satellite** everywhere but high
  latency.
- A **SOHO** router is many devices in one — most home-network questions target
  its DHCP, Wi-Fi, firewall, or port-forwarding role.
