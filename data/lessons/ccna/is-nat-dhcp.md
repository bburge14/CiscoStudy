# NAT & DHCP

## NAT (Network Address Translation)
NAT rewrites IP addresses as packets cross the inside/outside boundary. Address
terminology (memorize the 2×2 grid):

| | Local (as seen inside) | Global (as seen outside) |
|--|------------------------|--------------------------|
| **Inside** | inside local (private host) | inside global (public, after NAT) |
| **Outside** | outside local | outside global (real public server) |

Types:
- **Static NAT** — fixed one-to-one (used for inbound servers).
- **Dynamic NAT** — one-to-one from a pool, while a mapping lasts.
- **PAT / "overload"** — **many-to-one**, multiplexing on L4 source ports. This
  is what shares one public IP among a whole office.

```
interface Gi0/0
 ip nat inside
interface Gi0/1
 ip nat outside
access-list 1 permit 10.0.0.0 0.0.0.255
ip nat inside source list 1 interface Gi0/1 overload   ! PAT
```
The **`overload`** keyword is the signal for PAT.

## DHCP — the DORA exchange
1. **Discover** (client broadcast)
2. **Offer** (server)
3. **Request** (client broadcast)
4. **Ack** (server)

Router as a DHCP server:
```
ip dhcp excluded-address 10.0.0.1 10.0.0.10   ! reserve gateway/servers
ip dhcp pool LAN
 network 10.0.0.0 255.255.255.0
 default-router 10.0.0.1
 dns-server 8.8.8.8
```

### DHCP relay (cross-subnet)
Clients broadcast; a broadcast won't cross a router. When the DHCP server is on
another subnet, configure a **relay** on the client-facing interface so the
router forwards the request as a unicast to the server:
```
interface Vlan10
 ip helper-address 10.9.9.9
```
`ip helper-address` also relays a handful of other key UDP broadcasts (DNS, TFTP,
NTP, etc.).

## DNS
Resolves names to IPs. On IOS: `ip name-server 8.8.8.8` and `ip domain-lookup`.

## Verify
```
show ip nat translations
show ip nat statistics
show ip dhcp binding
show ip interface g0/0 | include Helper
```

## Exam cues
- `overload` = PAT = many hosts behind one public IP.
- Cross-subnet DHCP → `ip helper-address` on the clients' gateway.
- Order is **DORA**.
