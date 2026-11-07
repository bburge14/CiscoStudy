"""CCNP ENCOR 350-401 item pool — depth expansion round 2 (original, blueprint-aligned).

Same schema and authenticity contract as content_encor.py / content_encor_2.py:
real IOS/IOS-XE syntax, real protocol behavior, and an explanation that says why
the key is right, why each distractor is a trap, and the exam-pattern cue. All
original content mapped to the public exam blueprint — never real exam items.

This round deepens the lighter domains toward CCNA-level coverage, concentrating
on 2.0 Virtualization (device/data-path/VRF/VXLAN overlay) plus fresh angles in
Architecture, Network Assurance, Security, and Automation. IDs carry a `-r2-`
segment so they can never collide with the base or `_2` pools.

build_content.py auto-discovers every tools/content_encor_*.py pool (name-sorted)
and concatenates it onto content_encor.QUESTIONS; shuffle_options() then randomises
A/B/C/D order, so the authored 'A' key here is not positionally biased.
"""

QUESTIONS = [
    # ======================= 2.0 VIRTUALIZATION =======================
    # ---- device_virtualization ----
    {
        "id": "encor-vi-r2-001", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 1, "type": "mcq",
        "stem": "Which of the following is an example of a Type 1 (bare-metal) hypervisor?",
        "options": [
            {"id": "A", "text": "VMware ESXi"},
            {"id": "B", "text": "Oracle VirtualBox"},
            {"id": "C", "text": "VMware Workstation"},
            {"id": "D", "text": "Parallels Desktop"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 1 hypervisor installs directly on the physical hardware with no "
                       "underlying host OS. VMware ESXi — like Microsoft Hyper-V, KVM, and Xen — "
                       "is bare-metal, the type used for production data-center virtualization.",
            "distractors": {
                "B": "Oracle VirtualBox is a Type 2 (hosted) hypervisor — it runs as an application on top of a host OS.",
                "C": "VMware Workstation is a Type 2 hypervisor that runs on top of Windows/Linux, mainly on desktops.",
                "D": "Parallels Desktop is a Type 2 hypervisor that runs as an app on macOS.",
            },
            "exam_pattern": "Type 1 = bare-metal (ESXi, Hyper-V, KVM, Xen), for servers. Type 2 = hosted "
                            "app on an OS (VirtualBox, Workstation, Fusion, Parallels), for desktops.",
        },
    },
    {
        "id": "encor-vi-r2-002", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A service provider replaces dedicated router, firewall, and load-balancer appliances "
                "with software instances running on commodity x86 servers. Which concept does this describe?",
        "options": [
            {"id": "A", "text": "Network Functions Virtualization (NFV)"},
            {"id": "B", "text": "Spanning Tree Protocol"},
            {"id": "C", "text": "Control Plane Policing (CoPP)"},
            {"id": "D", "text": "Power over Ethernet (PoE)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NFV decouples network functions (routing, firewalling, load balancing) from "
                       "purpose-built hardware and runs them as virtualized network functions (VNFs) on "
                       "standard servers, improving flexibility and cost.",
            "distractors": {
                "B": "STP is a Layer 2 loop-prevention protocol, unrelated to virtualizing network functions.",
                "C": "CoPP rate-limits traffic to the control plane to protect the CPU; it is not about running functions as software.",
                "D": "PoE delivers electrical power over Ethernet cabling to devices like APs and phones.",
            },
            "exam_pattern": "NFV = network functions as software VNFs on generic hardware. Often paired with "
                            "SDN (centralized control), but a distinct idea.",
        },
    },
    {
        "id": "encor-vi-r2-003", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 3, "type": "mcq",
        "stem": "Two Catalyst 9500 switches form a StackWise Virtual pair joined by a StackWise Virtual "
                "Link (SVL). What is the specific purpose of the separate Dual-Active Detection (DAD) link?",
        "options": [
            {"id": "A", "text": "To detect when the SVL fails so both chassis do not simultaneously become "
                               "active (a split-brain / dual-active condition)"},
            {"id": "B", "text": "To carry all data-plane traffic between the two chassis"},
            {"id": "C", "text": "To synchronize the VLAN database using VTP"},
            {"id": "D", "text": "To provide Power over Ethernet to downstream access points"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "If the SVL goes down, each member could assume the peer failed and become active with "
                       "the same addresses — a dual-active (split-brain) state. The DAD link (fast-hello or "
                       "enhanced PAgP) lets them detect this and keep only one chassis active.",
            "distractors": {
                "B": "Carrying inter-chassis control and data traffic is the role of the SVL itself, not the DAD link.",
                "C": "StackWise Virtual presents one logical control plane; VTP/VLAN synchronization is not what DAD does.",
                "D": "PoE is unrelated; DAD is a detection mechanism, not a power source.",
            },
            "exam_pattern": "SVL = the bundle that makes two chassis one logical switch. DAD = the backup "
                            "detector that prevents dual-active/split-brain if the SVL fails.",
        },
    },
    {
        "id": "encor-vi-r2-004", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "In a virtualized data center, an administrator moves a RUNNING virtual machine from one "
                "physical host to another with essentially no downtime by copying its active memory state. "
                "What is this called?",
        "options": [
            {"id": "A", "text": "Live migration (e.g., VMware vMotion)"},
            {"id": "B", "text": "Snapshotting"},
            {"id": "C", "text": "Thin provisioning"},
            {"id": "D", "text": "PXE booting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Live migration (vMotion in VMware, Live Migration in Hyper-V) transfers a running VM's "
                       "memory and state to another host transparently, with no perceptible interruption — "
                       "used for maintenance and load balancing.",
            "distractors": {
                "B": "A snapshot captures a VM's disk/memory at a point in time for rollback; it does not move a running VM.",
                "C": "Thin provisioning allocates storage on demand rather than up front — a disk-efficiency feature, not a migration.",
                "D": "PXE boot loads an OS over the network at startup; it is not a running-VM move.",
            },
            "exam_pattern": "Live migration/vMotion = move a running VM host-to-host with no downtime. "
                            "Snapshot = point-in-time save. Different problems.",
        },
    },
    {
        "id": "encor-vi-r2-005", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 3, "type": "mcq",
        "stem": "To give latency-sensitive VMs near-line-rate throughput, an engineer configures the physical "
                "NIC to present multiple Virtual Functions (VFs) that attach DIRECTLY to the VMs, bypassing "
                "the hypervisor's virtual switch. Which technology provides this?",
        "options": [
            {"id": "A", "text": "SR-IOV (Single-Root I/O Virtualization)"},
            {"id": "B", "text": "NAT64"},
            {"id": "C", "text": "802.1Q trunking"},
            {"id": "D", "text": "GLBP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SR-IOV lets one physical NIC expose several lightweight Virtual Functions that the "
                       "hypervisor maps straight to VMs, bypassing the software vSwitch for near-native I/O "
                       "performance and lower latency.",
            "distractors": {
                "B": "NAT64 translates between IPv6 and IPv4; it has nothing to do with NIC virtualization.",
                "C": "802.1Q is VLAN tagging on a trunk — not a method for giving VMs direct NIC access.",
                "D": "GLBP is a first-hop gateway redundancy/load-balancing protocol, unrelated to VM I/O.",
            },
            "exam_pattern": "SR-IOV = physical NIC → multiple Virtual Functions → direct-to-VM, bypassing the vSwitch for performance.",
        },
    },
    # ---- data_path_virtualization ----
    {
        "id": "encor-vi-r2-006", "exam": "encor", "domain": "virtualization",
        "subtopic": "data_path_virtualization", "difficulty": 2, "type": "multi",
        "stem": "An engineer must run OSPF and forward multicast video over an ENCRYPTED site-to-site tunnel "
                "across the Internet, and deploys GRE over IPsec. Which TWO statements explain why BOTH "
                "technologies are used together? (Choose two.)",
        "options": [
            {"id": "A", "text": "GRE encapsulates multicast and routing-protocol traffic, which IPsec tunnel "
                               "mode does not transport by itself."},
            {"id": "B", "text": "IPsec supplies the confidentiality (encryption) and integrity that GRE does not provide."},
            {"id": "C", "text": "GRE already encrypts the payload, so IPsec is only needed to authenticate the peers."},
            {"id": "D", "text": "IPsec transport mode can carry OSPF and PIM multicast on its own, so GRE is optional."},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "GRE can tunnel multicast and routing protocols but offers no encryption; IPsec encrypts "
                       "and protects integrity but natively carries only unicast IP. GRE-over-IPsec combines "
                       "them: GRE wraps OSPF/multicast, IPsec encrypts the result.",
            "distractors": {
                "C": "GRE provides NO encryption — that is precisely why IPsec is added on top.",
                "D": "Native IPsec does not forward multicast/routing-protocol traffic on its own; that gap is exactly what GRE fills.",
            },
            "exam_pattern": "GRE = multiprotocol/multicast, no encryption. IPsec = encryption, unicast only. "
                            "Encrypted dynamic routing → GRE over IPsec.",
        },
    },
    {
        "id": "encor-vi-r2-007", "exam": "encor", "domain": "virtualization",
        "subtopic": "data_path_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "In an IPsec site-to-site VPN, what is the difference between tunnel mode and transport mode?",
        "options": [
            {"id": "A", "text": "Tunnel mode encrypts the entire original IP packet and adds a new outer IP "
                               "header; transport mode encrypts only the payload and keeps the original IP header."},
            {"id": "B", "text": "Tunnel mode encrypts only the payload; transport mode encrypts the whole packet "
                               "and adds a new header."},
            {"id": "C", "text": "Both modes add a new outer IP header; they differ only in the UDP port used."},
            {"id": "D", "text": "Tunnel mode is for IPv6 only; transport mode is for IPv4 only."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IPsec tunnel mode protects the whole original packet and prepends a new IP header "
                       "(standard for site-to-site VPNs across the Internet). Transport mode protects just the "
                       "payload and keeps the original header (typically host-to-host).",
            "distractors": {
                "B": "This reverses the two — tunnel mode is the one that encrypts the entire packet and adds a new header.",
                "C": "They differ in what is encrypted and whether a new IP header is added, not merely a UDP port.",
                "D": "Both modes work with IPv4 and IPv6; the distinction is not address family.",
            },
            "exam_pattern": "Tunnel mode = new outer IP header, whole packet protected (site-to-site). "
                            "Transport mode = original header kept, payload only (host-to-host).",
        },
    },
    {
        "id": "encor-vi-r2-008", "exam": "encor", "domain": "virtualization",
        "subtopic": "data_path_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "On a DMVPN hub, a SINGLE tunnel interface accepts connections from dozens of spokes. "
                "Which tunnel interface type makes this possible?",
        "options": [
            {"id": "A", "text": "Multipoint GRE (mGRE)"},
            {"id": "B", "text": "A point-to-point GRE tunnel per spoke"},
            {"id": "C", "text": "An 802.1Q subinterface"},
            {"id": "D", "text": "A loopback interface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DMVPN uses a multipoint GRE (mGRE) interface on the hub so one interface serves all "
                       "spokes; NHRP then maps each spoke's tunnel (overlay) address to its real NBMA (public) address.",
            "distractors": {
                "B": "A separate point-to-point GRE per spoke is exactly what mGRE avoids — it would not scale and defeats dynamic spoke-to-spoke.",
                "C": "An 802.1Q subinterface creates VLAN subinterfaces on a trunk; it is not a DMVPN tunnel construct.",
                "D": "A loopback is a virtual local interface (often the tunnel source), but it does not terminate the multipoint tunnel itself.",
            },
            "exam_pattern": "DMVPN hub = mGRE + NHRP. mGRE = one interface, many endpoints. "
                            "NHRP = overlay-to-NBMA address resolution for dynamic spoke-to-spoke.",
        },
    },
    {
        "id": "encor-vi-r2-009", "exam": "encor", "domain": "virtualization",
        "subtopic": "data_path_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "An IPsec VPN must provide confidentiality (encryption), integrity, and authentication of the "
                "traffic. Which IPsec protocol provides encryption, and how does it differ from AH?",
        "options": [
            {"id": "A", "text": "ESP encrypts and authenticates the payload; AH provides only integrity/"
                               "authentication with no encryption."},
            {"id": "B", "text": "AH encrypts the payload; ESP only authenticates it."},
            {"id": "C", "text": "Both ESP and AH encrypt the payload identically; they differ only in IP protocol number."},
            {"id": "D", "text": "ESP provides integrity only; encryption is handled separately by IKE."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encapsulating Security Payload (ESP, IP protocol 50) provides confidentiality "
                       "(encryption) plus integrity/authentication. Authentication Header (AH, IP protocol 51) "
                       "provides integrity and origin authentication but NO encryption, so ESP is used where "
                       "data must be encrypted.",
            "distractors": {
                "B": "This is backwards — ESP is the one that encrypts; AH never encrypts.",
                "C": "They are not identical: AH does not encrypt at all, while ESP does.",
                "D": "ESP itself performs the encryption; IKE negotiates keys/SAs but does not encrypt the data traffic.",
            },
            "exam_pattern": "ESP = encryption + integrity (use for VPN confidentiality). AH = integrity/"
                            "authentication only, no encryption. IKE = key exchange / SA setup.",
        },
    },
    # ---- network_virtualization_vrf ----
    {
        "id": "encor-vi-r2-010", "exam": "encor", "domain": "virtualization",
        "subtopic": "network_virtualization_vrf", "difficulty": 3, "type": "mcq",
        "stem": "In an MPLS L3VPN, two customers both use the 10.0.0.0/8 address space. Which component "
                "ensures these OVERLAPPING prefixes remain unique in the provider's MP-BGP table?",
        "options": [
            {"id": "A", "text": "The Route Distinguisher (RD), prepended to the IPv4 prefix to form a unique 96-bit VPNv4 route"},
            {"id": "B", "text": "The Route Target (RT), which prepends the prefix to make it unique"},
            {"id": "C", "text": "The MPLS label, which rewrites the customer IP address"},
            {"id": "D", "text": "The OSPF process ID configured on the PE"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An 8-byte Route Distinguisher is prepended to each IPv4 prefix to create a unique 96-bit "
                       "VPNv4 prefix, so identical customer subnets do not collide in MP-BGP. The RD only "
                       "disambiguates; it does not control VPN membership.",
            "distractors": {
                "B": "The RT is an extended community that controls which VRFs import/export a route — it determines membership, not uniqueness.",
                "C": "The MPLS label switches the packet through the core; it does not make overlapping prefixes unique in BGP.",
                "D": "An OSPF process ID is locally significant to an IGP and plays no role in VPNv4 uniqueness.",
            },
            "exam_pattern": "RD = make overlapping prefixes unique (VPNv4). RT = control import/export into VRFs "
                            "(membership). Two different jobs — a classic trap.",
        },
    },
    {
        "id": "encor-vi-r2-011", "exam": "encor", "domain": "virtualization",
        "subtopic": "network_virtualization_vrf", "difficulty": 3, "type": "mcq",
        "stem": "A shared DNS server in a 'Services' VRF must be reachable from a 'Guest' VRF on the same "
                "router, WITHOUT merging the two VRFs. Which mechanism accomplishes this controlled sharing?",
        "options": [
            {"id": "A", "text": "Route leaking using MP-BGP route-target import/export between the VRFs"},
            {"id": "B", "text": "Disabling CEF so the global table is used for both"},
            {"id": "C", "text": "Configuring both interfaces as 802.1Q trunks"},
            {"id": "D", "text": "Enabling proxy ARP on the guest interface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Selectively importing/exporting the relevant route-targets (route leaking) lets specific "
                       "prefixes be shared between VRFs while keeping the rest of each customer's routing "
                       "isolated — the standard way to publish shared services.",
            "distractors": {
                "B": "Disabling CEF would break hardware forwarding and does not merge VRF routing tables in a controlled way.",
                "C": "802.1Q trunks carry VLANs on a link; they do not leak routes between VRF routing tables.",
                "D": "Proxy ARP answers ARP for remote hosts on one segment; it does not share routes across separate VRFs.",
            },
            "exam_pattern": "Share specific routes between VRFs = route leaking via RT import/export (or static "
                            "route leaking). Isolation is preserved for everything else.",
        },
    },
    {
        "id": "encor-vi-r2-012", "exam": "encor", "domain": "virtualization",
        "subtopic": "network_virtualization_vrf", "difficulty": 2, "type": "mcq",
        "stem": "In a LISP deployment, which device receives EID-to-RLOC registrations from egress tunnel "
                "routers and answers map-requests from ingress tunnel routers?",
        "options": [
            {"id": "A", "text": "The Map-Server / Map-Resolver (MS/MR)"},
            {"id": "B", "text": "The ingress tunnel router (ITR) only"},
            {"id": "C", "text": "The DHCP server"},
            {"id": "D", "text": "The spanning-tree root bridge"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ETRs register their EID-to-RLOC mappings with the Map-Server; the Map-Resolver receives "
                       "Map-Requests from ITRs and forwards them. The MS/MR is the LISP control-plane mapping "
                       "system (in SD-Access, the fabric control-plane node).",
            "distractors": {
                "B": "The ITR queries the mapping system and encapsulates traffic — it does not hold the registrations itself.",
                "C": "DHCP assigns IP addresses to hosts; it has no role in LISP EID/RLOC mapping.",
                "D": "An STP root bridge is a Layer 2 concept, unrelated to the LISP mapping database.",
            },
            "exam_pattern": "LISP roles: ITR (encaps, queries), ETR (registers, decaps), MS/MR (mapping "
                            "database/resolver). SD-Access control-plane node = MS/MR.",
        },
    },
    {
        "id": "encor-vi-r2-013", "exam": "encor", "domain": "virtualization",
        "subtopic": "network_virtualization_vrf", "difficulty": 1, "type": "mcq",
        "stem": "A router carries several VRFs. Which command displays the routing table for ONLY the VRF named RED?",
        "options": [
            {"id": "A", "text": "show ip route vrf RED"},
            {"id": "B", "text": "show ip route"},
            {"id": "C", "text": "show vrf RED route"},
            {"id": "D", "text": "show running-config | section RED"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'show ip route vrf RED' displays the routing table of the RED VRF specifically. Each VRF "
                       "has its own RIB, so you must name the VRF to see its routes.",
            "distractors": {
                "B": "'show ip route' with no vrf keyword shows only the global routing table, not a specific VRF's RIB.",
                "C": "'show vrf RED route' is not valid syntax; 'show vrf' lists VRFs and their interfaces, not the route table in that form.",
                "D": "Piping the running-config shows configuration lines, not the computed routing table for the VRF.",
            },
            "exam_pattern": "Per-VRF verification: add 'vrf <name>' to show/ping/traceroute "
                            "(show ip route vrf RED, ping vrf RED x.x.x.x).",
        },
    },
    # ---- overlay_vxlan ----
    {
        "id": "encor-vi-r2-014", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 2, "type": "mcq",
        "stem": "VXLAN encapsulates the original Layer 2 frame inside which outer transport, and on what "
                "standard destination port?",
        "options": [
            {"id": "A", "text": "UDP, destination port 4789"},
            {"id": "B", "text": "TCP, destination port 179"},
            {"id": "C", "text": "UDP, destination port 500"},
            {"id": "D", "text": "GRE (IP protocol 47), no port"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VXLAN wraps the original Ethernet frame in UDP/IP; the IANA-assigned VXLAN destination "
                       "port is UDP 4789. Using UDP lets the outer 5-tuple hash across ECMP paths in the underlay.",
            "distractors": {
                "B": "TCP/179 is BGP — a control-plane protocol — and the VXLAN data plane is UDP, not TCP.",
                "C": "UDP/500 is ISAKMP/IKE for IPsec, not VXLAN.",
                "D": "GRE is a different encapsulation (used by ERSPAN, for example); VXLAN specifically uses UDP.",
            },
            "exam_pattern": "VXLAN = MAC-in-UDP, dest port 4789, 24-bit VNI. Contrast ERSPAN (GRE) and Geneve (UDP 6081).",
        },
    },
    {
        "id": "encor-vi-r2-015", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 3, "type": "mcq",
        "stem": "In a BGP EVPN VXLAN fabric, what is the difference between an L2VNI and an L3VNI?",
        "options": [
            {"id": "A", "text": "An L2VNI maps to a Layer 2 bridge domain/VLAN for intra-subnet traffic; an "
                               "L3VNI is tied to a VRF and carries inter-subnet (routed) traffic between VTEPs."},
            {"id": "B", "text": "An L2VNI is used for routing and an L3VNI is used for bridging."},
            {"id": "C", "text": "An L2VNI identifies the underlay link; an L3VNI identifies the management VLAN."},
            {"id": "D", "text": "They are identical; the names are interchangeable."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Layer 2 VNIs extend a VLAN/bridge domain across the fabric (same-subnet switching). A "
                       "Layer 3 VNI is associated with a VRF and is used for symmetric IRB routing between "
                       "subnets across VTEPs.",
            "distractors": {
                "B": "This reverses the roles — L2VNI = bridging within a subnet, L3VNI = routing between subnets.",
                "C": "Neither identifies an underlay link or a management VLAN; both are overlay segment identifiers.",
                "D": "They serve distinct bridging vs routing roles and are not interchangeable.",
            },
            "exam_pattern": "L2VNI = per-VLAN bridge domain (intra-subnet). L3VNI = per-VRF routing instance "
                            "(inter-subnet, symmetric IRB).",
        },
    },
    {
        "id": "encor-vi-r2-016", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 3, "type": "mcq",
        "stem": "In an EVPN VXLAN fabric, every leaf switch is configured with the SAME gateway IP and the SAME "
                "virtual MAC for a given subnet. What does this 'distributed anycast gateway' achieve?",
        "options": [
            {"id": "A", "text": "A host's default gateway is always the directly attached leaf, giving optimal "
                               "first-hop routing and seamless mobility as hosts move between leaves"},
            {"id": "B", "text": "It forces all inter-subnet traffic to hairpin through a single central router"},
            {"id": "C", "text": "It disables routing so the fabric is purely Layer 2"},
            {"id": "D", "text": "It assigns a unique gateway IP per leaf so hosts must be reconfigured when they move"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With a distributed anycast gateway, each leaf is the local default gateway (same IP/MAC "
                       "everywhere), so routing happens at the ingress leaf and a workload keeps the same gateway "
                       "after moving to another leaf — no traffic tromboning, no reconfiguration.",
            "distractors": {
                "B": "The whole point is to AVOID hairpinning to a central router — routing is distributed to every leaf.",
                "C": "It enables distributed Layer 3 routing at the edge; it does not disable routing.",
                "D": "The gateway IP/MAC is intentionally identical on all leaves, so hosts never need reconfiguration when they move.",
            },
            "exam_pattern": "Distributed anycast gateway = same gateway IP+MAC on all VTEPs → optimal edge "
                            "routing + seamless workload mobility.",
        },
    },
    {
        "id": "encor-vi-r2-017", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 2, "type": "multi",
        "stem": "Before deploying a VXLAN overlay, an engineer builds the underlay. Which TWO are requirements "
                "of the VXLAN underlay? (Choose two.)",
        "options": [
            {"id": "A", "text": "IP reachability between VTEP loopbacks, typically provided by an IGP such as OSPF or IS-IS"},
            {"id": "B", "text": "An increased MTU on underlay links to absorb roughly 50 bytes of VXLAN/UDP/IP encapsulation overhead"},
            {"id": "C", "text": "A single Layer 2 VLAN stretched end-to-end across every switch"},
            {"id": "D", "text": "Spanning Tree Protocol running across all fabric links to break loops"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "VTEPs must reach each other's loopbacks over a routed underlay (IGP, often with PIM/ECMP), "
                       "and the underlay MTU must be raised (~50 bytes, or jumbo) so encapsulated frames are not fragmented.",
            "distractors": {
                "C": "VXLAN exists specifically to avoid stretching Layer 2 everywhere — the underlay is routed (Layer 3).",
                "D": "A routed underlay uses ECMP, not STP, across the fabric; large STP domains are what fabrics eliminate.",
            },
            "exam_pattern": "VXLAN underlay = routed IP reachability (loopback-to-loopback via IGP) + raised MTU "
                            "for the ~50B overhead. No stretched VLAN / big STP domain.",
        },
    },

    # ======================= 1.0 ARCHITECTURE =======================
    {
        "id": "encor-ar-r2-001", "exam": "encor", "domain": "architecture",
        "subtopic": "wireless_deployment", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants a lightweight AP dedicated full-time to scanning the RF for rogues and "
                "wireless intrusions (wIPS), WITHOUT serving any client traffic. Which AP mode should be configured?",
        "options": [
            {"id": "A", "text": "Monitor mode"},
            {"id": "B", "text": "Local mode"},
            {"id": "C", "text": "FlexConnect mode"},
            {"id": "D", "text": "Bridge mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Monitor-mode AP is a dedicated sensor — it does not transmit client data but scans all "
                       "channels for rogues, interference, and attacks (location / wIPS). It is the mode for "
                       "full-time RF monitoring.",
            "distractors": {
                "B": "Local mode is the default client-serving mode; it serves WLANs and only scans off-channel briefly.",
                "C": "FlexConnect switches client traffic locally at a branch and still serves clients — it is not a dedicated sensor.",
                "D": "Bridge mode is for mesh / point-to-point bridging between sites, not RF monitoring.",
            },
            "exam_pattern": "AP modes: Local (serve clients, default), Monitor (dedicated sensor/wIPS), Sniffer "
                            "(capture to analyzer), FlexConnect (branch local switching), Bridge/Flex+Bridge (mesh), SE-Connect (spectrum).",
        },
    },
    {
        "id": "encor-ar-r2-002", "exam": "encor", "domain": "architecture",
        "subtopic": "high_availability", "difficulty": 2, "type": "mcq",
        "stem": "A network must use a first-hop redundancy protocol that is an open IETF standard so it can run "
                "across routers from multiple vendors. Which protocol fits, and how does it differ from HSRP?",
        "options": [
            {"id": "A", "text": "VRRP — an open standard (RFC 5798) using master/backup roles, unlike Cisco-proprietary HSRP"},
            {"id": "B", "text": "GLBP — an open standard that load-balances by default"},
            {"id": "C", "text": "HSRP version 2 — the only multivendor FHRP"},
            {"id": "D", "text": "STP — the standard first-hop gateway redundancy protocol"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VRRP is the IETF-standard FHRP (RFC 5798), so it interoperates across vendors; it elects "
                       "a master and one or more backups. HSRP and GLBP are both Cisco-proprietary.",
            "distractors": {
                "B": "GLBP does load-balance, but it is Cisco-proprietary, not an open standard.",
                "C": "HSRP (v1 and v2) is Cisco-proprietary, so it is not the multivendor choice.",
                "D": "STP prevents Layer 2 loops; it is not a first-hop gateway redundancy protocol.",
            },
            "exam_pattern": "FHRPs: HSRP & GLBP = Cisco-proprietary (GLBP load-balances); VRRP = open standard "
                            "(master/backup). Need multivendor → VRRP.",
        },
    },
    {
        "id": "encor-ar-r2-003", "exam": "encor", "domain": "architecture",
        "subtopic": "fabric_overview", "difficulty": 2, "type": "mcq",
        "stem": "In an SD-Access fabric, which node is the one that endpoints (hosts, APs) directly connect to "
                "and that performs VXLAN encapsulation/decapsulation and hosts the anycast default gateway for them?",
        "options": [
            {"id": "A", "text": "Fabric edge node"},
            {"id": "B", "text": "Fabric border node"},
            {"id": "C", "text": "Fabric control-plane node"},
            {"id": "D", "text": "Catalyst Center (DNA Center) appliance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The fabric edge node is the access switch endpoints attach to; it registers endpoints with "
                       "the control plane, provides the anycast gateway, and encapsulates/decapsulates fabric (VXLAN) traffic.",
            "distractors": {
                "B": "The border node connects the fabric to the outside (WAN, data center, Internet) — the fabric's egress/ingress to external networks, not the endpoint's access switch.",
                "C": "The control-plane node runs the LISP map-server/map-resolver (EID-to-RLOC database); endpoints do not connect to it directly.",
                "D": "Catalyst Center / DNA Center is the management/automation controller, not a forwarding fabric node.",
            },
            "exam_pattern": "SD-Access nodes: Edge (endpoints attach, anycast GW, VXLAN encap), Border (to "
                            "outside), Control-plane (LISP MS/MR mapping).",
        },
    },
    {
        "id": "encor-ar-r2-004", "exam": "encor", "domain": "architecture",
        "subtopic": "machine_learning_ai", "difficulty": 3, "type": "mcq",
        "stem": "An assurance platform is trained on historical data to PREDICT a continuous value — next hour's "
                "WAN link utilization in Mbps. Which machine-learning technique is this?",
        "options": [
            {"id": "A", "text": "Regression (a supervised technique for predicting continuous values)"},
            {"id": "B", "text": "Clustering (an unsupervised technique)"},
            {"id": "C", "text": "Classification into discrete labeled categories"},
            {"id": "D", "text": "Reinforcement learning driven by trial-and-error rewards"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Predicting a continuous numeric output from labeled historical data is regression — a "
                       "supervised learning method (the model learns from known input/output pairs).",
            "distractors": {
                "B": "Clustering groups unlabeled data by similarity (unsupervised); it does not predict a specific numeric value.",
                "C": "Classification predicts a discrete category (e.g., 'anomalous' vs 'normal'), not a continuous number.",
                "D": "Reinforcement learning optimizes actions via rewards from an environment; it is not how a utilization forecast is trained here.",
            },
            "exam_pattern": "Supervised = learn from labels: classification (discrete) vs regression (continuous). "
                            "Unsupervised = clustering / anomaly detection on unlabeled data.",
        },
    },

    # ======================= 4.0 NETWORK ASSURANCE =======================
    {
        "id": "encor-as-r2-001", "exam": "encor", "domain": "network_assurance",
        "subtopic": "snmp_syslog", "difficulty": 2, "type": "mcq",
        "stem": "A router logs a message at syslog severity level 3. What severity NAME is that, and how does it "
                "compare with level 6 (informational)?",
        "options": [
            {"id": "A", "text": "Level 3 is 'Error', and a LOWER number is MORE severe, so level 3 is more severe than level 6"},
            {"id": "B", "text": "Level 3 is 'Debugging', the most severe level"},
            {"id": "C", "text": "Level 3 is 'Warning', and it is less severe than level 6"},
            {"id": "D", "text": "Severity numbers have no ordering; 3 and 6 are equally important"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Syslog severities run 0 Emergency, 1 Alert, 2 Critical, 3 Error, 4 Warning, 5 Notice, "
                       "6 Informational, 7 Debugging. Lower = more severe, so level 3 (Error) is more severe than "
                       "level 6 (Informational). 'logging trap 3' sends levels 0-3.",
            "distractors": {
                "B": "Debugging is level 7 and is the LEAST severe, not level 3 and not the most severe.",
                "C": "Warning is level 4, not 3; and level 3 is MORE severe than level 6, not less.",
                "D": "Severities are strictly ordered 0 (most severe) to 7 (least); they are not equal.",
            },
            "exam_pattern": "Syslog 0-7: Emergency/Alert/Critical/Error/Warning/Notice/Informational/Debugging. "
                            "Lower number = more severe; 'logging trap N' sends levels 0..N.",
        },
    },
    {
        "id": "encor-as-r2-002", "exam": "encor", "domain": "network_assurance",
        "subtopic": "ipsla", "difficulty": 2, "type": "mcq",
        "stem": "You want an IP SLA operation that simply measures round-trip time and reachability to a remote "
                "server's IP, and the remote device is a generic host you cannot configure. Which operation fits, "
                "and what does it require on the target?",
        "options": [
            {"id": "A", "text": "icmp-echo — it needs no IP SLA Responder on the target"},
            {"id": "B", "text": "udp-jitter — it needs no Responder on the target"},
            {"id": "C", "text": "icmp-echo — it requires the IP SLA Responder enabled on the target"},
            {"id": "D", "text": "http — it requires the Responder enabled on the target"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An ICMP-echo operation measures RTT/availability using plain ICMP, so the target only has "
                       "to answer pings — no IP SLA Responder is required. That makes it ideal for third-party or "
                       "non-Cisco targets.",
            "distractors": {
                "B": "udp-jitter measures jitter/latency/loss and relies on the IP SLA Responder on the target for accurate timestamps — it is not a plain ping.",
                "C": "icmp-echo does NOT require a Responder; that requirement applies to udp-jitter / udp-echo style operations.",
                "D": "The http operation tests web-server response, not basic RTT, and is unnecessary for a simple reachability/latency check.",
            },
            "exam_pattern": "icmp-echo = RTT/reachability, no Responder (any pingable host). udp-jitter = VoIP "
                            "metrics (latency/jitter/loss), needs the IP SLA Responder for accuracy.",
        },
    },
    {
        "id": "encor-as-r2-003", "exam": "encor", "domain": "network_assurance",
        "subtopic": "diagnostics_tools", "difficulty": 3, "type": "mcq",
        "stem": "To find the largest packet that can cross a path without fragmentation, you issue extended pings "
                "that increase in size with the Don't-Fragment (DF) bit set. A 1500-byte ping fails but 1400 bytes "
                "succeeds. What does the failure indicate?",
        "options": [
            {"id": "A", "text": "A link along the path has an MTU smaller than 1500 bytes, so the DF-set packet is dropped instead of fragmented"},
            {"id": "B", "text": "The destination host is powered off"},
            {"id": "C", "text": "ICMP is globally disabled on every router in the path"},
            {"id": "D", "text": "The routing table has no route to the destination"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With DF set, a router that would need to fragment the oversize packet must drop it (ideally "
                       "sending 'fragmentation needed'). Failure at 1500 but success at 1400 means the path MTU is "
                       "between those sizes — a smaller-MTU link (often a tunnel) is in the path.",
            "distractors": {
                "B": "If the host were off, the smaller 1400-byte ping would also fail — but it succeeds, so the host is reachable.",
                "C": "If ICMP were fully blocked everywhere, no ping size would succeed; the 1400-byte success disproves that.",
                "D": "A missing route would fail at every size; selective failure by size points to MTU, not reachability.",
            },
            "exam_pattern": "DF-bit ping sweep = discover path MTU. Fails only above a size → a lower-MTU link "
                            "(commonly a GRE/IPsec tunnel) on the path; fix with MTU / TCP MSS adjustment.",
        },
    },
    {
        "id": "encor-as-r2-004", "exam": "encor", "domain": "network_assurance",
        "subtopic": "spans", "difficulty": 2, "type": "mcq",
        "stem": "An ERSPAN session carries mirrored traffic from a source switch to an analyzer that is several "
                "ROUTED hops away. How is the mirrored traffic transported across the Layer 3 network?",
        "options": [
            {"id": "A", "text": "It is encapsulated in GRE and routed as IP to the destination's IP address"},
            {"id": "B", "text": "It is carried in a dedicated reserved VLAN across trunks"},
            {"id": "C", "text": "It is sent as raw Layer 2 frames flooded to all ports"},
            {"id": "D", "text": "It is tunneled inside an SNMP inform message"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ERSPAN (Encapsulated Remote SPAN) wraps the copied frames in GRE and routes them over IP "
                       "to the destination, so the analyzer can sit anywhere reachable at Layer 3 — unlike RSPAN, "
                       "which needs a Layer 2 reserved VLAN end to end.",
            "distractors": {
                "B": "Carrying the copy in a reserved VLAN across trunks describes RSPAN, which is confined to Layer 2 — exactly what ERSPAN overcomes.",
                "C": "SPAN/ERSPAN delivers to a specific destination, not by flooding raw frames everywhere.",
                "D": "SNMP informs carry management notifications, not mirrored packet captures.",
            },
            "exam_pattern": "Local SPAN = same switch. RSPAN = reserved VLAN across L2. ERSPAN = GRE-over-IP, "
                            "works across routed L3 networks.",
        },
    },

    # ======================= 5.0 SECURITY =======================
    {
        "id": "encor-se-r2-001", "exam": "encor", "domain": "security",
        "subtopic": "device_access_control", "difficulty": 2, "type": "mcq",
        "stem": "A router is configured with: 'aaa authentication login default group tacacs+ local'. "
                "What does the 'local' keyword provide?",
        "options": [
            {"id": "A", "text": "A fallback to the local username database if the TACACS+ servers are UNREACHABLE"},
            {"id": "B", "text": "A fallback to local only after TACACS+ actively REJECTS the credentials"},
            {"id": "C", "text": "Local logging of all TACACS+ transactions"},
            {"id": "D", "text": "Encryption of the TACACS+ shared secret using the local key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In a method list, methods are tried in order. 'local' is the backup method used only if "
                       "the TACACS+ servers do not respond (are unreachable). This prevents lockout if the AAA "
                       "servers are down.",
            "distractors": {
                "B": "Fallback does NOT trigger on an active reject — if TACACS+ responds and denies, the user is denied; the next method runs only when the prior method is unavailable.",
                "C": "'local' is an authentication method (local user DB), not a logging/accounting directive.",
                "D": "The shared secret is set per server (and can be masked with type 6 / 'service password-encryption'); 'local' does not encrypt it.",
            },
            "exam_pattern": "AAA method list = ordered fallbacks. A later method runs only when the earlier one is "
                            "UNREACHABLE, not when it rejects. Keep a 'local'/'enable' backup to avoid lockout.",
        },
    },
    {
        "id": "encor-se-r2-002", "exam": "encor", "domain": "security",
        "subtopic": "network_access_control_8021x", "difficulty": 3, "type": "mcq",
        "stem": "A company deploys 802.1X but does not want to install client certificates on every endpoint. "
                "They choose an EAP method that builds a TLS tunnel using ONLY a server-side certificate, then "
                "authenticates the user with MSCHAPv2 inside it. Which EAP method is this?",
        "options": [
            {"id": "A", "text": "PEAP (Protected EAP)"},
            {"id": "B", "text": "EAP-TLS"},
            {"id": "C", "text": "EAP-MD5"},
            {"id": "D", "text": "PAP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PEAP requires a certificate only on the RADIUS/authentication server; it forms a TLS tunnel "
                       "and runs an inner method (commonly MSCHAPv2) to authenticate the user — avoiding per-client certificates.",
            "distractors": {
                "B": "EAP-TLS requires digital certificates on BOTH the supplicant and the server (mutual) — the very per-client certificate burden they want to avoid.",
                "C": "EAP-MD5 sends a weak hashed challenge, provides no server authentication or tunnel, and is unsuitable for secure 802.1X/wireless.",
                "D": "PAP sends credentials in cleartext and is not an EAP tunneling method for 802.1X.",
            },
            "exam_pattern": "EAP-TLS = certs on BOTH sides (strongest, most work). PEAP / EAP-TTLS / EAP-FAST = "
                            "server-side cert + protected tunnel for an inner credential (e.g., MSCHAPv2).",
        },
    },
    {
        "id": "encor-se-r2-003", "exam": "encor", "domain": "security",
        "subtopic": "wireless_security", "difficulty": 2, "type": "mcq",
        "stem": "Which data-confidentiality cipher does WPA2 use, replacing the weak TKIP used by the original WPA?",
        "options": [
            {"id": "A", "text": "AES-CCMP"},
            {"id": "B", "text": "WEP with a 128-bit key"},
            {"id": "C", "text": "RC4 with per-packet keying (TKIP)"},
            {"id": "D", "text": "3DES in CBC mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "WPA2 mandates CCMP, which uses the AES block cipher (counter mode with CBC-MAC) for "
                       "confidentiality and integrity — far stronger than WPA's TKIP/RC4. WPA3 extends this to "
                       "CCMP-128 / GCMP-256.",
            "distractors": {
                "B": "WEP (any key length) is the obsolete, broken original Wi-Fi encryption that WPA/WPA2 replaced.",
                "C": "TKIP (built on RC4) is exactly the weak WPA method that WPA2's AES-CCMP replaced.",
                "D": "3DES is used in some VPNs, not as the Wi-Fi data cipher for WPA2.",
            },
            "exam_pattern": "WEP (broken) → WPA/TKIP(RC4) → WPA2/AES-CCMP → WPA3/CCMP-128+GCMP-256 with SAE. "
                            "'WPA2 data cipher' = AES-CCMP.",
        },
    },
    {
        "id": "encor-se-r2-004", "exam": "encor", "domain": "security",
        "subtopic": "infrastructure_security_acls", "difficulty": 3, "type": "mcq",
        "stem": "An engineer must filter traffic between hosts that are IN THE SAME VLAN on a switch (intra-VLAN), "
                "dropping some flows that a routed ACL would never see. Which feature does this?",
        "options": [
            {"id": "A", "text": "A VLAN ACL (VACL), applied via a VLAN access-map to all traffic in the VLAN"},
            {"id": "B", "text": "A standard router ACL applied inbound on the SVI"},
            {"id": "C", "text": "Control Plane Policing (CoPP)"},
            {"id": "D", "text": "A time-based ACL on the uplink trunk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VACL (VLAN access-map) filters traffic switched WITHIN a VLAN as well as routed traffic — "
                       "it acts on every packet in the VLAN, so it can drop intra-VLAN flows that an SVI/router "
                       "ACL (which only sees traffic leaving the VLAN) cannot.",
            "distractors": {
                "B": "A router ACL on the SVI only inspects traffic routed in/out of the VLAN, not traffic switched between hosts in the same VLAN.",
                "C": "CoPP protects the control-plane CPU from excessive traffic; it does not filter host-to-host data within a VLAN.",
                "D": "A time-based ACL on the uplink filters by schedule on that link; it still does not see intra-VLAN switched traffic.",
            },
            "exam_pattern": "Intra-VLAN (switched, same subnet) filtering = VACL or Private VLANs. A router/SVI ACL "
                            "only sees inter-VLAN (routed) traffic.",
        },
    },

    # ======================= 6.0 AUTOMATION =======================
    {
        "id": "encor-au-r2-001", "exam": "encor", "domain": "automation",
        "subtopic": "json_yaml_xml", "difficulty": 1, "type": "mcq",
        "stem": "A RESTCONF reply contains: {\"ietf-interfaces:interface\": [ {\"name\": \"GigabitEthernet1\"}, "
                "{\"name\": \"GigabitEthernet2\"} ] }. In JSON, what do the square brackets [ ] denote, versus "
                "the curly braces { }?",
        "options": [
            {"id": "A", "text": "Square brackets denote an ordered array (list); curly braces denote an object of key:value pairs"},
            {"id": "B", "text": "Square brackets denote an object; curly braces denote an array"},
            {"id": "C", "text": "Both denote the same thing and are interchangeable in JSON"},
            {"id": "D", "text": "Square brackets denote a comment; curly braces denote a string"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In JSON, [ ] is an array (an ordered list you index by position), and { } is an object "
                       "(unordered key:value pairs). Here 'interface' is a list of two objects, so in Python you "
                       "would access data['ietf-interfaces:interface'][0]['name'].",
            "distractors": {
                "B": "This reverses them — [ ] is the array and { } is the object, not the other way around.",
                "C": "Arrays and objects are distinct JSON types with different access patterns (index vs key); they are not interchangeable.",
                "D": "JSON has no comment syntax, and strings are wrapped in double quotes, not brackets or braces.",
            },
            "exam_pattern": "JSON: {} = object (dict / key:value), [] = array (list). Maps to Python dict and list "
                            "after json.loads() / response.json().",
        },
    },
    {
        "id": "encor-au-r2-002", "exam": "encor", "domain": "automation",
        "subtopic": "netconf_restconf_encor", "difficulty": 3, "type": "mcq",
        "stem": "Using RESTCONF, you must change ONLY one interface's description without replacing the entire "
                "interface configuration resource. Which HTTP method should you use?",
        "options": [
            {"id": "A", "text": "PATCH (merges / partially modifies the target resource)"},
            {"id": "B", "text": "PUT (replaces the entire target resource)"},
            {"id": "C", "text": "GET (retrieves the resource)"},
            {"id": "D", "text": "DELETE (removes the resource)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RESTCONF maps CRUD to HTTP: PATCH performs a merge, changing only the specified leaf (the "
                       "description) and leaving the rest of the resource intact. PUT would replace the whole resource.",
            "distractors": {
                "B": "PUT replaces the entire target resource with the payload, which could wipe out other interface settings you did not send.",
                "C": "GET only reads data; it cannot modify the description.",
                "D": "DELETE removes the resource entirely rather than modifying one field.",
            },
            "exam_pattern": "RESTCONF methods: GET (read), POST (create), PUT (replace/create), PATCH (merge/"
                            "partial change), DELETE (remove).",
        },
    },
    {
        "id": "encor-au-r2-003", "exam": "encor", "domain": "automation",
        "subtopic": "eem_scripting", "difficulty": 2, "type": "mcq",
        "stem": "An EEM applet must run automatically every day at 02:00 to archive the configuration. Which EEM "
                "event detector triggers the applet on that schedule?",
        "options": [
            {"id": "A", "text": "The timer (cron) event detector, e.g., 'event timer cron cron-entry \"0 2 * * *\"'"},
            {"id": "B", "text": "The syslog event detector matching a %SYS pattern"},
            {"id": "C", "text": "The interface event detector watching a line-protocol change"},
            {"id": "D", "text": "The none event detector that only runs on a manual 'event manager run'"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EEM's timer event detector supports a cron-style schedule, so the applet fires at the "
                       "specified time (02:00 daily). It is the standard way to schedule recurring EEM actions.",
            "distractors": {
                "B": "A syslog event detector fires when a log message matches a pattern — it is event-driven, not time-scheduled.",
                "C": "An interface event detector fires on interface/line-protocol state changes, not at a set clock time.",
                "D": "The 'none' detector requires a manual trigger ('event manager run'); it does not fire on a schedule.",
            },
            "exam_pattern": "EEM event detectors: syslog (pattern), interface/counter (state), snmp, timer "
                            "(watchdog/countdown/cron for schedules), none (manual run).",
        },
    },
    {
        "id": "encor-au-r2-004", "exam": "encor", "domain": "automation",
        "subtopic": "python_data", "difficulty": 2, "type": "mcq",
        "stem": "A Python script has a dictionary 'payload' that it must send as a JSON-formatted STRING in a REST "
                "API request body. Which call produces that JSON string?",
        "options": [
            {"id": "A", "text": "json.dumps(payload)"},
            {"id": "B", "text": "json.loads(payload)"},
            {"id": "C", "text": "payload.json()"},
            {"id": "D", "text": "str(payload).upper()"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "json.dumps() serializes a Python object (dict/list) into a JSON-formatted string "
                       "(dump-to-string). Its inverse, json.loads(), parses a JSON string back into a Python object.",
            "distractors": {
                "B": "json.loads() does the opposite — it parses a JSON STRING into a Python object; it expects a string input, not a dict to serialize.",
                "C": "'.json()' is a method on a requests Response object (to parse a reply), not a method on a plain dict.",
                "D": "str().upper() produces an uppercased Python repr, not valid JSON (it would break keys and True/False/None).",
            },
            "exam_pattern": "json.dumps = dict → JSON string (serialize / out). json.loads = JSON string → dict "
                            "(parse / in). requests resp.json() parses a response body.",
        },
    },
]
