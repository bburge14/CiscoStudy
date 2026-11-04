# Device, Path & Network Virtualization

## Device virtualization
- **Hypervisors**: **Type 1 (bare-metal)** installs directly on hardware
  (VMware ESXi, KVM, Hyper-V) — data-center standard. **Type 2 (hosted)** runs as
  an app on an OS (VirtualBox, VMware Workstation).
- **Containers** share the host OS kernel (Docker) — lighter than VMs, but **not**
  hypervisors.
- **vSwitch** connects VMs to the physical network inside a host.

## Network virtualization — VRF
**VRF (Virtual Routing and Forwarding)** gives a router multiple independent
routing tables, isolating tenants/customers on shared hardware. VRF-Lite (no MPLS):
```
vrf definition RED
 address-family ipv4
interface Gi0/1
 vrf forwarding RED          ! bind the interface (clears its IP — re-add it)
 ip address 10.1.1.1 255.255.255.0
```
Verify with `show vrf` and `show ip route vrf RED`. Each VRF has its own routes,
so overlapping address space between tenants is fine.

## Data-path virtualization — GRE & IPsec
- **GRE** encapsulates arbitrary protocols (and **multicast**) in IP. Flexible,
  but **no encryption** on its own.
- **IPsec** (ESP) provides encryption + integrity but doesn't natively carry
  multicast/multiprotocol in tunnel mode.
- **GRE over IPsec** combines both: GRE for flexibility, IPsec for security — the
  usual pairing when you need encrypted multicast/routing over the Internet.

## Overlays — VXLAN
**VXLAN** tunnels Layer 2 over a routed Layer 3 underlay (**MAC-in-UDP**, dest
port **4789**). It uses a **24-bit VNI** → ~**16 million** segments, smashing the
802.1Q 12-bit/4094 VLAN limit. The device that encaps/decaps is a **VTEP**.

### BGP EVPN control plane
Plain VXLAN floods to learn MACs. **BGP EVPN** is the control plane that
advertises endpoint **MAC/IP-to-VTEP** reachability (Type-2) and VTEP/VNI
membership (Type-3), minimizing flooding. The underlay still needs an IGP
(OSPF/IS-IS) so VTEPs can reach each other.

> Split the roles: **VXLAN = data plane (encapsulation)**, **BGP EVPN = control
> plane (reachability)**, **IGP underlay = VTEP transport**.

## Exam cues
- Type 1 = on hardware; Type 2 = on an OS; containers ≠ VMs.
- VRF binding clears the interface IP — re-add it.
- GRE = multiprotocol/multicast, no encryption → pair with IPsec.
- VXLAN = 24-bit VNI (16M), UDP 4789; EVPN = its BGP control plane.
