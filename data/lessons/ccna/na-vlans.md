# VLANs & 802.1Q Trunking

## VLANs
A VLAN is a separate broadcast domain on a switch. Traffic between VLANs needs a
router or an SVI (inter-VLAN routing). Create and assign:
```
vlan 20
 name USERS
interface Gi0/5
 switchport mode access
 switchport access vlan 20
```
An **access port** carries exactly one VLAN, untagged, to an endpoint.

## 802.1Q trunking
A **trunk** carries many VLANs between switches by inserting a 4-byte **802.1Q
tag** (containing the 12-bit VLAN ID) into each frame.
```
interface Gi0/1
 switchport trunk encapsulation dot1q   ! on switches that support ISL
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

### The native VLAN
One VLAN on a trunk is sent **untagged** — the **native VLAN** (default VLAN 1).
Both ends **must agree** on the native VLAN. A mismatch produces:
```
%CDP-4-NATIVE_VLAN_MISMATCH: ... Gi0/1 (1), with SW2 Gi0/1 (99).
```
The trunk stays up, but each switch drops its untagged frames into a *different*
VLAN — a bridging/security problem (and the basis of a VLAN-hopping attack). Fix
by matching the native VLAN on both ends, e.g. `switchport trunk native vlan 99`.

### The `allowed vlan` trap
```
switchport trunk allowed vlan 10,20,30      ! REPLACES the whole list
switchport trunk allowed vlan add 40        ! APPENDS 40
```
Forgetting `add` replaces the entire allowed list and can black-hole every other
VLAN — a classic outage.

## DTP (Dynamic Trunking Protocol)
Ports can negotiate trunking with DTP. Mode behaviour:

| Local \ Remote | access | dynamic auto | dynamic desirable | trunk |
|----------------|--------|--------------|-------------------|-------|
| **access** | access | access | access | (mismatch) |
| **dynamic auto** | access | **access** | trunk | trunk |
| **dynamic desirable** | access | trunk | trunk | trunk |
| **trunk** | (mismatch) | trunk | trunk | trunk |

Key result: **auto + auto = access** (nobody initiates). Best practice is to hard
-set the mode and disable negotiation with `switchport nonegotiate`.

## Verify
```
show vlan brief
show interfaces trunk
show interfaces g0/1 switchport
```
`show interfaces trunk` is the fastest way to confirm the mode, native VLAN and
the allowed/active VLAN list on each trunk.

## Exam cues
- Native VLAN mismatch → CDP log, trunk up, untagged frames cross VLANs.
- `allowed vlan` without `add` wipes the list.
- auto/auto never trunks.
