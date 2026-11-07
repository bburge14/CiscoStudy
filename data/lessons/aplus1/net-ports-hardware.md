# Ports, Protocols & Network Hardware

Two devices on a network find each other with an IP address, but a single
computer runs many programs at once — a browser, a mail client, a file share — so
it needs a second number to say *which program* a message is for. That number is
a **port**, and each common service listens on a well-known one. Learning the
port list is the single most reliable mark you can earn on this exam, so this
lesson front-loads it, then covers the boxes that move the traffic around.

## Ports and protocols: the list you must memorize

Think of the IP address as the street address of a building and the **port
number** as the apartment inside it. The protocol is the language spoken in that
apartment. CompTIA expects you to recall these cold:

| Port | Protocol | What it does |
|-----:|----------|--------------|
| 20/21 | **FTP** | File Transfer Protocol — move files (21 control, 20 data) |
| 22 | **SSH** | Secure shell — encrypted remote command line |
| 23 | **Telnet** | Remote command line, **unencrypted** (avoid) |
| 25 | **SMTP** | Send email |
| 53 | **DNS** | Resolve names to IP addresses |
| 67/68 | **DHCP** | Hand out IP addresses automatically |
| 80 | **HTTP** | Web, **unencrypted** |
| 110 | **POP3** | Download email to one device |
| 137–139 | **NetBIOS/NetBT** | Legacy Windows name service |
| 143 | **IMAP** | Email synced on the server |
| 161/162 | **SNMP** | Monitor/manage network devices |
| 389 | **LDAP** | Directory lookups (e.g. Active Directory) |
| 443 | **HTTPS** | Web, **encrypted (TLS)** |
| 445 | **SMB/CIFS** | Windows file & printer sharing |
| 3389 | **RDP** | Remote Desktop — control a Windows GUI |

A few pairings are worth burning in because they appear constantly:

> **Secure vs insecure twins:** **SSH 22** replaces Telnet 23; **HTTPS 443**
> replaces HTTP 80. If a question wants the *secure* option, pick 22 or 443.
>
> **RDP is 3389** — "remote into a Windows desktop" is almost always RDP/3389.

### TCP versus UDP

Protocols ride on one of two transports:

- **TCP** (Transmission Control Protocol) is the **reliable** one. It sets up a
  connection, numbers the pieces, and resends anything lost — like a phone call
  where you confirm you heard each other. Web, email, file transfer, and RDP use
  TCP.
- **UDP** (User Datagram Protocol) is **fire-and-forget**: no setup, no resend,
  just send and hope — like dropping a postcard in the mail. It is faster and
  suits streaming, voice, DNS lookups, and DHCP, where a little loss beats delay.

> TCP = reliable, ordered, acknowledged. UDP = fast, connectionless, no
> guarantees.

## The boxes that build a network

Now the hardware. Each device works at a certain "layer," which is just a fancy
way of saying *how smart it is about addresses*.

### Hubs, switches, and routers — the core three

- A **hub** is the dumbest: it repeats every signal out *every* port, so all
  devices share the bandwidth and collide. Obsolete, but it appears as the
  "wrong answer" on exams.
- A **switch** is smart about **MAC addresses**. It learns which device is on
  which port and sends each frame *only* to the correct port. This is the
  backbone of a wired LAN.
  - An **unmanaged switch** just works out of the box — no configuration.
  - A **managed switch** can be configured: VLANs, port speeds, security, and
    monitoring. You buy managed when you need control.
- A **router** connects *different* networks and makes decisions on **IP
  addresses**. Your home router is really a router + switch + access point +
  firewall in one plastic box, and it is what joins your LAN to the internet.

> Climbing the ladder: a **hub** repeats blindly, a **switch** forwards by **MAC
> address** inside one network, and a **router** forwards by **IP address**
> between networks.

### Getting onto the internet: modems and ONTs

- A **modem** converts between your ISP's signal and Ethernet. A **cable modem**
  rides the coax of a cable-TV line; a **DSL modem** rides the telephone line.
- An **ONT** (Optical Network Terminal) is the "modem" for **fiber** — it
  converts the light on the fiber to Ethernet where it enters the building. This
  is the demarcation point on a fiber install.
- A **NIC** (Network Interface Card) is the adapter in a computer that gives it a
  network port (wired RJ45 or a wireless radio) and its MAC address.

### Access points, firewalls, and the rest

- An **access point (AP)** adds Wi-Fi to a wired network — it bridges wireless
  clients onto the LAN.
- A **firewall** inspects traffic and allows or blocks it by rules. It is the
  guard at the border between your network and the internet (or between network
  zones).
- A **patch panel** is the tidy termination point in a wiring closet: cables from
  the walls land on the back, and short patch cords jump the front to a switch.
  It organizes cabling; it is not "smart."

### Power over Ethernet (PoE)

**PoE** sends electrical power *and* data over one Ethernet cable, so a device
like a Wi-Fi access point, IP camera, or VoIP phone needs no separate power
outlet. You supply it one of two ways:

- a **PoE switch**, which powers devices from its ports directly, or
- a **PoE injector**, which adds power to the cable for one device when the
  switch itself is not PoE-capable.

> If an access point on the ceiling has only one Ethernet cable and no power
> brick, it is being fed by **PoE** — either a PoE switch or an injector.

### Software-defined networking

**SDN** (Software-Defined Networking) splits the "brain" (the control plane that
decides where traffic goes) from the "muscle" (the data plane that forwards it),
and lets a central controller program many devices at once. You do not configure
SDN on the A+, but you should recognize the term as *centralized, programmable
network control*.

## The whole thing in one paragraph

Every service listens on a **port**: file transfer **FTP 20/21**, secure shell
**SSH 22** (replacing **Telnet 23**), mail **SMTP 25 / POP3 110 / IMAP 143**,
name resolution **DNS 53**, address handout **DHCP 67/68**, the web on **HTTP 80**
and secure **HTTPS 443**, device monitoring **SNMP 161/162**, directory **LDAP
389**, Windows sharing **SMB 445**, and remote desktop **RDP 3389** — riding on
reliable **TCP** or fast, connectionless **UDP**. Those messages flow through
hardware that gets smarter up the ladder: a dumb **hub** repeats everything, a
**switch** forwards by **MAC** within a network (unmanaged = plug-and-play,
managed = configurable), and a **router** forwards by **IP** between networks. A
**modem** or fiber **ONT** reaches the ISP, a **NIC** connects a host, an **access
point** adds Wi-Fi, a **firewall** filters by rules, a **patch panel** terminates
cabling, and **PoE** (via a PoE switch or an injector) powers APs and cameras
over the same Ethernet cable.

## On the exam

- Memorize the port table. Highest-value: **22 SSH, 23 Telnet, 25 SMTP, 53 DNS,
  67/68 DHCP, 80 HTTP, 110 POP3, 143 IMAP, 443 HTTPS, 445 SMB, 3389 RDP, 161/162
  SNMP, 389 LDAP, 20/21 FTP.**
- **Secure twins:** SSH 22 over Telnet 23; HTTPS 443 over HTTP 80. "Remote into a
  Windows GUI" → **RDP 3389**.
- **TCP** = reliable/ordered (web, email, file transfer); **UDP** = fast/
  connectionless (streaming, voice, DNS, DHCP).
- A **switch** uses MAC addresses within one network; a **router** uses IP to join
  networks. **Managed** switches can be configured, **unmanaged** cannot.
- **Cable modem** = coax, **DSL modem** = phone line, **ONT** = fiber. A **NIC**
  carries the host's MAC address.
- **PoE** carries power + data on one cable; supply it with a **PoE switch** or a
  **PoE injector**. A ceiling AP with one cable and no power brick → PoE.
