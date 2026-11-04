# IPv6, the OSI Model, Transport & Switching

## IPv6 address format
128 bits written as eight 16-bit **hextets** in hex, separated by colons. Two
compression rules, applied together:
1. **Drop leading zeros** in each hextet (`00AB` → `AB`, `0000` → `0`).
2. Replace the **single longest run** of all-zero hextets with `::` — and `::`
   may appear **only once** in an address.

`2001:0DB8:0000:0000:0000:00AB:0000:1234` → `2001:DB8::AB:0:1234`.
Two `::` in one answer is always wrong (ambiguous).

## Key IPv6 address types
| Type | Prefix | Notes |
|------|--------|-------|
| Global unicast | 2000::/3 | Internet-routable, like public IPv4 |
| Unique local | FC00::/7 (FD00::/8 used) | Private, not Internet-routable |
| Link-local | FE80::/10 | Auto-created per interface; never routed; used by ND, OSPFv3, next-hops |
| Multicast | FF00::/8 | No broadcasts in IPv6; uses multicast instead |
| Solicited-node mcast | FF02::1:FFxx:xxxx | Used by Neighbor Discovery (replaces ARP) |

Well-known multicast: `FF02::1` all nodes, `FF02::2` all routers, `FF02::5/6` OSPFv3.

## EUI-64
Builds the 64-bit interface ID from a 48-bit MAC:
1. Split the MAC in half, insert **FFFE** in the middle.
2. **Flip the 7th bit** (the U/L bit) of the first byte.

`001A:2B`-MAC → insert FFFE → `001A2BFFFE3C4D5E` → flip bit 7 of `00`→`02` →
**`021A:2BFF:FE3C:4D5E`**. The 00→02 flip is the step distractors skip.

## SLAAC vs DHCPv6
- **SLAAC** (Stateless Address Autoconfiguration): the host learns the /64
  prefix from a Router Advertisement (RA) and builds its own address (EUI-64 or
  random). No server tracks it.
- **DHCPv6**: stateful (full address assignment) or stateless (other options
  like DNS only, with SLAAC doing the address).

## The OSI & TCP/IP models
Encapsulation **down** the stack creates: **Segment (L4) → Packet (L3) → Frame
(L2) → Bits (L1)**. De-encapsulation on receive reverses it. Know which PDU and
addressing lives where: ports at L4, IP at L3, MAC at L2.

## TCP vs UDP
| | TCP | UDP |
|--|-----|-----|
| Connection | 3-way handshake (SYN, SYN-ACK, ACK) | Connectionless |
| Reliability | Acknowledgements, retransmission, ordering | Best-effort |
| Overhead | Higher | Lower |
| Use | HTTP(S), FTP, SSH, SMTP | DNS, DHCP, TFTP, SNMP, NTP, syslog, voice/video (RTP) |

Common ports: FTP 20/21, SSH 22, Telnet 23, DNS 53, DHCP 67/68, HTTP 80,
HTTPS 443, SNMP 161/162, NTP 123, syslog 514.

## Switching basics
A switch **learns source MACs** to build its CAM table and **forwards by
destination MAC**. Behaviours:
- **Known unicast** → forwarded out the single mapped port.
- **Unknown unicast / broadcast / multicast** → **flooded** out all ports in the
  VLAN *except the ingress port*.
- Each switch port is its own **collision domain**; each VLAN is a **broadcast domain**.

## Cabling
- **Straight-through**: unlike devices (switch↔router, switch↔PC).
- **Crossover**: like devices (switch↔switch, router↔router, PC↔PC). Auto-MDIX
  makes the choice automatic when enabled.

## Verify
```
show ipv6 interface brief
show ipv6 neighbors
show mac address-table
```
