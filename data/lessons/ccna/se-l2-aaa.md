# Layer 2 Security, AAA & VPN Concepts

## Port security
Limits which/how many MAC addresses may use an access port.
```
interface Gi0/5
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```
Violation modes:
| Mode | Drops traffic | Increments counter / alerts | Port state |
|------|---------------|-----------------------------|------------|
| `protect` | yes | **no** | stays up |
| `restrict` | yes | **yes** | stays up |
| `shutdown` (default) | yes | yes | **err-disabled** |

`sticky` learns MACs dynamically and saves them to the running config.

## DHCP snooping
Builds a trusted/untrusted boundary so rogue DHCP servers can't hand out
addresses. **All ports are untrusted by default**; trust only the ports toward
legitimate servers/uplinks:
```
ip dhcp snooping
ip dhcp snooping vlan 10
interface Gi0/1
 ip dhcp snooping trust          ! uplink toward the real DHCP server
```
Snooping also builds the **binding table** (IP↔MAC↔port) that DAI and IP Source
Guard rely on.

## Dynamic ARP Inspection (DAI)
Validates ARP against the DHCP snooping binding table, stopping ARP poisoning /
man-in-the-middle. Trust uplinks; inspect access ports.

## Mapping tool → attack
| Attack | Mitigation |
|--------|------------|
| MAC flooding (CAM overflow) | Port security |
| Rogue DHCP / starvation | DHCP snooping (+ port security) |
| ARP spoofing / MITM | Dynamic ARP Inspection |
| Rogue switch / STP takeover | BPDU Guard / Root Guard |
| VLAN hopping | Disable DTP, change native VLAN, prune VLANs |

## AAA & 802.1X
AAA = **Authentication, Authorization, Accounting**, usually via a RADIUS/TACACS+
server. **802.1X** controls port access with three roles:
- **Supplicant** — the endpoint (client software).
- **Authenticator** — the **switch/WLC** controlling the port; relays EAP to the server.
- **Authentication server** — RADIUS (e.g., Cisco ISE).

EAP runs between supplicant and authenticator (EAPoL); RADIUS carries it from the
authenticator to the server.

## VPN concepts
- **Site-to-site IPsec** joins two networks over the Internet.
- **ESP** provides encryption **and** integrity; **AH** provides integrity only
  (no encryption).
- **IKE/ISAKMP** negotiates keys. **GRE** adds multiprotocol/multicast tunneling
  but no encryption (often GRE-over-IPsec).

## Verify
```
show port-security interface g0/5
show ip dhcp snooping
show authentication sessions
```

## Exam cues
- restrict = drop + count + alert, stays up; protect = silent; shutdown = err-disable.
- Snooping untrusts everything by default — trust the server uplink.
- 802.1X: supplicant / authenticator (switch) / RADIUS server.
- ESP = encryption + integrity; AH = integrity only.
