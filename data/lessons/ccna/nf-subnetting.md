# IPv4 Addressing, Subnetting & Wildcards

## Why this matters
Subnetting questions are the fastest points on the exam **if** you work the block
size, and the slowest if you try to think in binary under pressure. Build the
mechanical habit below and you can answer in ~20 seconds.

## The anatomy of an address
A 32-bit IPv4 address is split by the **subnet mask** into a *network* portion
(the 1-bits) and a *host* portion (the 0-bits).

| Prefix | Mask | Block size (interesting octet) | Usable hosts |
|-------:|------|-------------------------------:|-------------:|
| /24 | 255.255.255.0   | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64  | 62  |
| /27 | 255.255.255.224 | 32  | 30  |
| /28 | 255.255.255.240 | 16  | 14  |
| /29 | 255.255.255.248 | 8   | 6   |
| /30 | 255.255.255.252 | 4   | 2   |

**Usable hosts = 2^(host bits) − 2** (subtract the network and broadcast
addresses). Exceptions: a **/31** has 2 usable hosts (RFC 3021, point-to-point),
and a **/32** is a single host route.

## The block-size method (memorize this)
1. **Block size** = 256 − (mask value in the interesting octet).
2. List the subnet boundaries by counting up by the block size: 0, block, 2×block, …
3. The host's subnet is the **largest boundary ≤ the host's octet**.
4. **Broadcast** = next boundary − 1. **Network** = the boundary itself.
5. **Usable range** = network+1 through broadcast−1.

### Worked example — 172.16.20.75 /26
- Block size = 256 − 192 = **64** → boundaries .0, .64, .128, .192
- .75 falls in the **.64** subnet
- Network **172.16.20.64**, Broadcast **172.16.20.127**, usable **.65–.126**

## VLSM: size each subnet to its need
Variable Length Subnet Masking assigns the *smallest mask that still fits*.
A point-to-point WAN link needs only 2 hosts → **/30** (or /31). A 50-user VLAN
needs ≥50 hosts → 6 host bits (62 usable) → **/26**. Always round the host
requirement **up** to the next power of two, then subtract 2.

## Wildcard masks
ACLs and OSPF `network` statements use a **wildcard mask**, which is the
*inverse* of a subnet mask: a **0 bit = "must match"**, a **1 bit = "don't care."**

> Wildcard = 255.255.255.255 − subnet mask (octet by octet).

| Subnet mask | Prefix | Wildcard |
|-------------|-------:|----------|
| 255.255.255.0   | /24 | 0.0.0.255 |
| 255.255.255.192 | /26 | 0.0.0.63  |
| 255.255.252.0   | /22 | 0.0.3.255 |
| 255.255.255.255 | /32 | 0.0.0.0 (`host`) |

`access-list 10 permit 10.1.0.0 0.0.3.255` matches 10.1.0.0–10.1.3.255. The
classic trap is handing you the **subnet mask** where a **wildcard** is required
(or vice-versa) — they are mirror images.

## Verify on the device
```
show ip interface brief
show running-config interface g0/1
show ip route connected
```

## Exam cues
- "How many usable hosts?" → 2^(host bits) − 2.
- "Which subnet / broadcast?" → block-size method.
- A wildcard of `0.0.0.0` = `host`; `255.255.255.255` = `any`.
