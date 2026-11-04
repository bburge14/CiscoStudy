"""Authentic CCNP ENCOR 350-401 item pool (original content, blueprint-aligned).

Same standard as the CCNA pool: real IOS-XE syntax, real protocol behaviour,
real show output, and full why-right / why-trap / exam-pattern feedback.
"""

QUESTIONS = [
    # ===================== 1.0 ARCHITECTURE =====================
    {
        "id": "encor-ar-001", "exam": "encor", "domain": "architecture",
        "subtopic": "fabric_overview", "difficulty": 3, "type": "mcq",
        "stem": "In a Cisco SD-Access fabric, which component is responsible for the "
                "control-plane mapping of endpoint IDs (EIDs) to routing locators (RLOCs)?",
        "options": [
            {"id": "A", "text": "The fabric edge node"},
            {"id": "B", "text": "The control-plane node running LISP (map-server/map-resolver)"},
            {"id": "C", "text": "The fabric border node"},
            {"id": "D", "text": "The wireless LAN controller"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SD-Access uses LISP for the control plane. The control-plane node acts "
                       "as the LISP Map-Server/Map-Resolver, holding the EID-to-RLOC mappings "
                       "that edge nodes query to reach endpoints.",
            "distractors": {
                "A": "Edge nodes register and query EIDs but do not hold the authoritative map "
                     "database themselves.",
                "B": "",
                "C": "Border nodes connect the fabric to external networks (the 'exit'), not the EID map.",
                "D": "The WLC integrates wireless into the fabric but is not the LISP control plane.",
            },
            "exam_pattern": "SD-Access planes: LISP=control (map-server/resolver), VXLAN=data "
                            "plane, Cisco TrustSec/SGT=policy. Match the node role: edge=endpoints, "
                            "border=exit, control=LISP DB.",
        },
        "verify_cli": ["show lisp site", "show lisp instance-id 4100 ipv4 map-cache"],
        "references": ["ENCOR 350-401 Topic 1.2 SD-Access"],
        "tags": ["sd-access", "lisp", "fabric"],
    },
    {
        "id": "encor-ar-002", "exam": "encor", "domain": "architecture",
        "subtopic": "high_availability", "difficulty": 2, "type": "mcq",
        "stem": "Two Catalyst switches are combined so they appear as a single logical switch "
                "with one control plane, allowing a downstream device to form a single "
                "cross-chassis EtherChannel. Which technology is this?",
        "options": [
            {"id": "A", "text": "StackWise Virtual (SVL)"},
            {"id": "B", "text": "HSRP"},
            {"id": "C", "text": "VRRP"},
            {"id": "D", "text": "GLBP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "StackWise Virtual (and VSS on older platforms) merges two chassis into "
                       "one logical switch with a single control plane, enabling a Multichassis "
                       "EtherChannel (MEC) and removing the need for STP blocking on the uplinks.",
            "distractors": {
                "A": "",
                "B": "HSRP is a first-hop gateway redundancy protocol; each switch keeps its own "
                     "control plane.",
                "C": "VRRP is also an FHRP (IETF standard), not a chassis-virtualization technology.",
                "D": "GLBP is an FHRP that load-balances gateways; it does not merge control planes.",
            },
            "exam_pattern": "StackWise Virtual/VSS = one logical device + MEC. FHRPs (HSRP/VRRP/"
                            "GLBP) = separate devices sharing a virtual gateway. Don't confuse chassis "
                            "virtualization with gateway redundancy.",
        },
        "verify_cli": ["show stackwise-virtual", "show switch virtual"],
        "references": ["ENCOR 350-401 Topic 1.3 high availability"],
        "tags": ["stackwise-virtual", "vss", "ha"],
    },
    {
        "id": "encor-ar-003", "exam": "encor", "domain": "architecture",
        "subtopic": "wireless_deployment", "difficulty": 2, "type": "mcq",
        "stem": "An AP is configured in FlexConnect mode at a branch. The CAPWAP tunnel to the "
                "central WLC goes down. What happens to clients on a locally-switched WLAN?",
        "options": [
            {"id": "A", "text": "All clients immediately disconnect because the WLC is unreachable"},
            {"id": "B", "text": "Locally-switched clients keep forwarding traffic locally (standalone mode)"},
            {"id": "C", "text": "The AP reboots and joins the nearest AP as a mesh node"},
            {"id": "D", "text": "Traffic is tunneled to a backup WLC over the Internet automatically"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "FlexConnect allows local switching of WLAN traffic at the branch. If the "
                       "WAN/CAPWAP to the WLC fails, the AP enters standalone mode and continues "
                       "switching already-authenticated clients locally.",
            "distractors": {
                "A": "That describes centrally-switched (local-mode) behaviour, not FlexConnect "
                     "local switching.",
                "B": "",
                "C": "FlexConnect APs do not convert to mesh nodes on WLC loss.",
                "D": "There is no automatic Internet-tunneled backup WLC behaviour implied here.",
            },
            "exam_pattern": "FlexConnect = branch APs, local switching + survivability (standalone "
                            "on WAN loss). Local mode = all traffic tunneled to WLC (central switching).",
        },
        "verify_cli": ["show ap config general", "show flexconnect"],
        "references": ["ENCOR 350-401 Topic 1.4 wireless deployment models"],
        "tags": ["flexconnect", "wireless"],
    },
    {
        "id": "encor-ar-004", "exam": "encor", "domain": "architecture",
        "subtopic": "enterprise_design", "difficulty": 2, "type": "mcq",
        "stem": "In a three-tier campus design, which layer's primary job is fast, high-"
                "capacity transport and interconnecting distribution blocks — with no policy, "
                "filtering, or CPU-intensive features?",
        "options": [
            {"id": "A", "text": "Access layer"},
            {"id": "B", "text": "Distribution layer"},
            {"id": "C", "text": "Core layer"},
            {"id": "D", "text": "Edge/WAN layer"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The core is built for speed and resilience — it switches packets between "
                       "distribution blocks as fast as possible and avoids anything that adds "
                       "latency (ACLs, policy, redistribution).",
            "distractors": {
                "A": "The access layer connects endpoints and applies port security, PoE, VLANs.",
                "B": "The distribution layer is where routing/policy/filtering/aggregation live.",
                "C": "",
                "D": "The WAN/edge layer handles external connectivity, not intra-campus core transport.",
            },
            "exam_pattern": "Access=connect endpoints, Distribution=aggregate+policy/routing, "
                            "Core=fast transport (keep it simple). Policy belongs at distribution, not core.",
        },
        "verify_cli": [],
        "references": ["ENCOR 350-401 Topic 1.1 enterprise network design"],
        "tags": ["campus", "three-tier", "design"],
    },
    {
        "id": "encor-ar-005", "exam": "encor", "domain": "architecture",
        "subtopic": "high_availability", "difficulty": 2, "type": "mcq",
        "stem": "Which first-hop redundancy protocol natively load-balances traffic across "
                "multiple active gateways by handing out different virtual MAC addresses in "
                "ARP replies?",
        "options": [
            {"id": "A", "text": "HSRP"},
            {"id": "B", "text": "VRRP"},
            {"id": "C", "text": "GLBP"},
            {"id": "D", "text": "StackWise"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "GLBP (Gateway Load Balancing Protocol) uses one AVG that replies to ARP "
                       "with different virtual MACs for up to four AVFs, so hosts spread their "
                       "traffic across multiple active gateways automatically.",
            "distractors": {
                "A": "HSRP has one active and one standby — only the active forwards (no native "
                     "per-flow balancing without multiple groups).",
                "B": "VRRP similarly has one master forwarding at a time.",
                "C": "",
                "D": "StackWise is chassis stacking, not an FHRP.",
            },
            "exam_pattern": "GLBP = Cisco, load-balances via multiple vMACs (AVG/AVF). HSRP/VRRP "
                            "= active/standby (balance only by using multiple groups). GLBP and "
                            "HSRP are Cisco; VRRP is the open standard.",
        },
        "verify_cli": ["show glbp brief", "show glbp"],
        "references": ["ENCOR 350-401 Topic 1.3 FHRP"],
        "tags": ["glbp", "fhrp", "load-balancing"],
    },

    # ===================== 2.0 VIRTUALIZATION =====================
    {
        "id": "encor-vi-001", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 3, "type": "mcq",
        "stem": "VXLAN is used as the data-plane encapsulation in modern fabrics. Which "
                "statement about VXLAN is correct?",
        "options": [
            {"id": "A", "text": "It adds a 24-bit VNI, allowing ~16 million segments, and encapsulates in UDP"},
            {"id": "B", "text": "It adds a 12-bit VLAN ID, allowing 4094 segments, over TCP"},
            {"id": "C", "text": "It is a Layer 2 protocol that cannot traverse a routed underlay"},
            {"id": "D", "text": "It replaces IP entirely in the underlay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VXLAN uses a 24-bit VXLAN Network Identifier (VNI) for ~16M segments and "
                       "encapsulates Ethernet frames in UDP (dest port 4789), so it tunnels L2 "
                       "over a routed L3 underlay (MAC-in-UDP).",
            "distractors": {
                "A": "",
                "B": "The 12-bit 4094-segment limit is exactly the 802.1Q VLAN constraint VXLAN "
                     "was designed to overcome; VXLAN uses UDP, not TCP.",
                "C": "VXLAN's whole point is to extend L2 ACROSS a routed L3 underlay.",
                "D": "VXLAN runs ON TOP of an IP underlay; it does not replace IP.",
            },
            "exam_pattern": "VXLAN = 24-bit VNI (16M), MAC-in-UDP port 4789, L2-over-L3. Contrast "
                            "with 802.1Q's 12-bit/4094 limit. Often paired with BGP EVPN as the control plane.",
        },
        "verify_cli": ["show nve vni", "show nve peers"],
        "references": ["ENCOR 350-401 Topic 2.1 overlay (VXLAN)"],
        "tags": ["vxlan", "vni", "overlay"],
    },
    {
        "id": "encor-vi-002", "exam": "encor", "domain": "virtualization",
        "subtopic": "network_virtualization_vrf", "difficulty": 2, "type": "mcq",
        "stem": "You configure VRF-Lite to separate two customers' routing on one router. "
                "Which command associates interface Gi0/1 with the customer VRF named RED?",
        "options": [
            {"id": "A", "text": "ip vrf forwarding RED (under interface Gi0/1)"},
            {"id": "B", "text": "vrf definition RED (under interface Gi0/1)"},
            {"id": "C", "text": "ip route vrf RED"},
            {"id": "D", "text": "switchport vrf RED"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Under the interface, 'vrf forwarding RED' (or legacy 'ip vrf forwarding "
                       "RED') binds the interface to the VRF. The VRF itself is created globally "
                       "with 'vrf definition RED'.",
            "distractors": {
                "A": "",
                "B": "'vrf definition RED' creates the VRF in global config; it is not the "
                     "interface-binding command.",
                "C": "'ip route vrf RED ...' adds a static route in the VRF table, not an "
                     "interface assignment.",
                "D": "There is no 'switchport vrf' command; VRF binding is a Layer 3 interface concept.",
            },
            "exam_pattern": "Two steps: (1) 'vrf definition NAME' globally, (2) 'vrf forwarding "
                            "NAME' on the interface. Assigning the VRF clears any existing IP — "
                            "readd the address after.",
        },
        "verify_cli": ["show vrf", "show ip route vrf RED"],
        "references": ["ENCOR 350-401 Topic 2.2 VRF"],
        "tags": ["vrf", "vrf-lite"],
    },
    {
        "id": "encor-vi-003", "exam": "encor", "domain": "virtualization",
        "subtopic": "device_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "Which hypervisor type runs directly on the physical hardware without a "
                "host operating system underneath it?",
        "options": [
            {"id": "A", "text": "Type 1 (bare-metal), e.g., VMware ESXi"},
            {"id": "B", "text": "Type 2 (hosted), e.g., VirtualBox"},
            {"id": "C", "text": "A container runtime like Docker"},
            {"id": "D", "text": "A Type 3 nested hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 1 'bare-metal' hypervisor (ESXi, Hyper-V, KVM) installs directly "
                       "on hardware for best performance and is standard in data centers.",
            "distractors": {
                "A": "",
                "B": "Type 2 hypervisors run as an application ON an existing OS (desktop virtualization).",
                "C": "Containers share the host OS kernel and are not hypervisors at all.",
                "D": "There is no standard 'Type 3' hypervisor category.",
            },
            "exam_pattern": "Type 1 = on hardware (ESXi/KVM/Hyper-V). Type 2 = on an OS "
                            "(VirtualBox/VMware Workstation). Containers ≠ VMs (shared kernel).",
        },
        "verify_cli": [],
        "references": ["ENCOR 350-401 Topic 2.3 device virtualization"],
        "tags": ["hypervisor", "virtualization"],
    },
    {
        "id": "encor-vi-004", "exam": "encor", "domain": "virtualization",
        "subtopic": "data_path_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "Which tunneling technology lets you carry multiple protocols and multicast "
                "across an IP core by encapsulating them in IP, but provides NO encryption by itself?",
        "options": [
            {"id": "A", "text": "GRE"},
            {"id": "B", "text": "IPsec ESP"},
            {"id": "C", "text": "MACsec"},
            {"id": "D", "text": "TLS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GRE encapsulates arbitrary protocols (and supports multicast) in IP but "
                       "offers no confidentiality — which is why it is frequently paired with "
                       "IPsec (GRE over IPsec) when security is needed.",
            "distractors": {
                "A": "",
                "B": "IPsec ESP encrypts but, in tunnel mode alone, does not natively carry "
                     "multicast/multiprotocol the way GRE does.",
                "C": "MACsec (802.1AE) encrypts at Layer 2 on a link, not a multiprotocol IP tunnel.",
                "D": "TLS secures application sessions, not a multiprotocol network tunnel.",
            },
            "exam_pattern": "GRE = flexible/multicast-capable, NO encryption. Need security → GRE "
                            "over IPsec. MACsec = L2 hop encryption. The 'no encryption' clue points to GRE.",
        },
        "verify_cli": ["show interfaces tunnel0", "show ip interface brief | include Tunnel"],
        "references": ["ENCOR 350-401 Topic 2.1 data-path virtualization (GRE/IPsec)"],
        "tags": ["gre", "tunneling"],
    },
    {
        "id": "encor-vi-005", "exam": "encor", "domain": "virtualization",
        "subtopic": "overlay_vxlan", "difficulty": 3, "type": "mcq",
        "stem": "In a BGP EVPN VXLAN fabric, what is the role of BGP EVPN (the control plane)?",
        "options": [
            {"id": "A", "text": "It encapsulates user frames into UDP for transport"},
            {"id": "B", "text": "It advertises MAC/IP reachability (and VTEP info) so flooding is minimized"},
            {"id": "C", "text": "It replaces the IP underlay routing protocol"},
            {"id": "D", "text": "It assigns IP addresses to endpoints via DHCP"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "BGP EVPN distributes endpoint MAC/IP-to-VTEP reachability (Type-2 routes) "
                       "and VTEP/VNI membership (Type-3), enabling control-plane learning that "
                       "cuts down the flood-and-learn behaviour of data-plane-only VXLAN.",
            "distractors": {
                "A": "Encapsulation into UDP is VXLAN's DATA plane, not EVPN's control-plane job.",
                "B": "",
                "C": "An IGP (OSPF/IS-IS) still provides underlay reachability for the VTEPs; "
                     "EVPN rides on top.",
                "D": "EVPN does not perform DHCP address assignment.",
            },
            "exam_pattern": "VXLAN = data plane (encap). BGP EVPN = control plane (MAC/IP "
                            "advertisement, reduces flooding). Underlay IGP still needed for VTEP reachability.",
        },
        "verify_cli": ["show bgp l2vpn evpn", "show nve peers"],
        "references": ["ENCOR 350-401 Topic 2.1 overlay control plane"],
        "tags": ["evpn", "vxlan", "bgp"],
    },

    # ===================== 3.0 INFRASTRUCTURE =====================
    {
        "id": "encor-in-001", "exam": "encor", "domain": "infrastructure",
        "subtopic": "bgp", "difficulty": 3, "type": "mcq",
        "stem": "A router has two eBGP paths to the same prefix, identical in weight, local-"
                "preference, AS-path length, origin, and MED. Which attribute is evaluated NEXT "
                "in the BGP best-path algorithm?",
        "options": [
            {"id": "A", "text": "Prefer the path learned via eBGP over iBGP"},
            {"id": "B", "text": "Prefer the highest router-id"},
            {"id": "C", "text": "Prefer the oldest (longest-established) eBGP path"},
            {"id": "D", "text": "Prefer the path with the highest MED"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "After weight, local-pref, locally-originated, AS-path, origin, and MED, "
                       "the next tiebreak is to prefer eBGP paths over iBGP paths.",
            "distractors": {
                "A": "",
                "B": "Lowest (not highest) router-id is used, and only much later in the list "
                     "after IGP metric and the oldest-eBGP check.",
                "C": "Oldest eBGP path is a later tiebreaker, after the eBGP-over-iBGP step.",
                "D": "BGP prefers the LOWEST MED, and MED was already stated to be equal here.",
            },
            "exam_pattern": "Order mnemonic: We Love Oranges AS Oranges Mean Pure Refreshment "
                            "(Weight, Local-pref, Originate/self, AS-path, Origin, MED, "
                            "eBGP>iBGP, IGP metric, oldest, Router-ID, neighbor IP). Lowest MED wins.",
        },
        "verify_cli": ["show bgp ipv4 unicast", "show ip bgp 203.0.113.0"],
        "references": ["ENCOR 350-401 Topic 3.4 BGP path selection"],
        "tags": ["bgp", "best-path"],
    },
    {
        "id": "encor-in-002", "exam": "encor", "domain": "infrastructure",
        "subtopic": "ospf_advanced", "difficulty": 3, "type": "mcq",
        "stem": "Which OSPF LSA type is generated by an ABR to describe networks in one area "
                "to other areas (inter-area routes)?",
        "options": [
            {"id": "A", "text": "Type 1 (Router LSA)"},
            {"id": "B", "text": "Type 2 (Network LSA)"},
            {"id": "C", "text": "Type 3 (Summary LSA)"},
            {"id": "D", "text": "Type 5 (External LSA)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Type 3 Summary LSAs are originated by Area Border Routers to advertise "
                       "prefixes from one area into another (inter-area/O IA routes).",
            "distractors": {
                "A": "Type 1 Router LSAs are flooded WITHIN an area, describing a router's links.",
                "B": "Type 2 Network LSAs are generated by the DR on multiaccess segments, within an area.",
                "C": "",
                "D": "Type 5 External LSAs are generated by an ASBR for routes redistributed "
                     "from outside OSPF (O E1/E2).",
            },
            "exam_pattern": "Type 1=router(intra), 2=network(DR), 3=ABR summary(inter-area), "
                            "4=ASBR locator, 5=ASBR external, 7=NSSA external. ABR→Type 3, ASBR→Type 5.",
        },
        "verify_cli": ["show ip ospf database", "show ip ospf database summary"],
        "references": ["ENCOR 350-401 Topic 3.2 OSPF LSAs"],
        "tags": ["ospf", "lsa", "abr"],
    },
    {
        "id": "encor-in-003", "exam": "encor", "domain": "infrastructure",
        "subtopic": "eigrp", "difficulty": 3, "type": "mcq",
        "stem": "In EIGRP, a route's successor has a feasible distance (FD) of 3072. A "
                "neighbor advertises the same prefix with a reported distance (RD) of 2560. "
                "Does that neighbor qualify as a feasible successor?",
        "options": [
            {"id": "A", "text": "Yes — its RD (2560) is less than the successor's FD (3072), meeting the feasibility condition"},
            {"id": "B", "text": "No — its RD must be greater than the FD to be loop-free"},
            {"id": "C", "text": "Yes — any neighbor is automatically a feasible successor"},
            {"id": "D", "text": "No — feasible successors require an equal FD"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Feasibility Condition: a neighbor is a feasible successor if its "
                       "Reported Distance is LESS than the current successor's Feasible Distance. "
                       "2560 < 3072, so it qualifies as a loop-free backup.",
            "distractors": {
                "A": "",
                "B": "That is backwards — RD must be LESS than FD (RD < FD) to guarantee loop-free.",
                "C": "Not every neighbor qualifies; only those meeting the feasibility condition.",
                "D": "Feasible successors do not need an equal FD; they need RD < FD.",
            },
            "exam_pattern": "Feasibility Condition: RD(neighbor) < FD(successor) → feasible "
                            "successor (instant backup, no recomputation). Otherwise DUAL goes active.",
        },
        "verify_cli": ["show ip eigrp topology", "show ip eigrp topology 10.0.0.0/24"],
        "references": ["ENCOR 350-401 Topic 3.3 EIGRP"],
        "tags": ["eigrp", "feasible-successor", "dual"],
    },
    {
        "id": "encor-in-004", "exam": "encor", "domain": "infrastructure",
        "subtopic": "etherchannel_advanced", "difficulty": 2, "type": "mcq",
        "stem": "An EtherChannel's members pass traffic for many flows, but one high-volume "
                "server conversation is not balancing across links. Which change is MOST likely "
                "to improve link utilization?",
        "options": [
            {"id": "A", "text": "Change the load-balancing hash to include Layer 4 ports (src-dst-port)"},
            {"id": "B", "text": "Add more VLANs to the trunk"},
            {"id": "C", "text": "Switch from LACP to static 'on' mode"},
            {"id": "D", "text": "Lower the STP priority of the port-channel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EtherChannel hashes each flow to ONE member link. A single src/dst IP "
                       "pair always hashes the same way; adding Layer 4 ports (src-dst-port) to "
                       "the hash gives more entropy so sub-flows spread across members.",
            "distractors": {
                "A": "",
                "B": "Adding VLANs does not change how a single conversation is hashed.",
                "C": "Static 'on' does not change load-balancing behaviour; the hash algorithm does.",
                "D": "STP priority affects root/forwarding, not intra-bundle load distribution.",
            },
            "exam_pattern": "EtherChannel never splits a single flow — it balances per-flow via a "
                            "hash. More hash inputs (add L4 ports, or src-dst vs dst-only) = better "
                            "spread. Set with 'port-channel load-balance'.",
        },
        "verify_cli": ["show etherchannel load-balance", "show etherchannel summary"],
        "references": ["ENCOR 350-401 Topic 3.1 EtherChannel load balancing"],
        "tags": ["etherchannel", "load-balance", "hash"],
    },
    {
        "id": "encor-in-005", "exam": "encor", "domain": "infrastructure",
        "subtopic": "multicast", "difficulty": 3, "type": "mcq",
        "stem": "In PIM Sparse Mode, what does the notation (*, G) represent in the multicast "
                "routing table?",
        "options": [
            {"id": "A", "text": "A source-specific tree rooted at a particular source for group G"},
            {"id": "B", "text": "A shared tree for group G rooted at the Rendezvous Point, for any source"},
            {"id": "C", "text": "A unicast route to the group's gateway"},
            {"id": "D", "text": "A pruned interface list only"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "(*, G) is the shared tree entry for group G rooted at the RP; the '*' "
                       "means 'any source'. Receivers first join the shared tree toward the RP, "
                       "then may switch to a source tree (S, G).",
            "distractors": {
                "A": "A source-specific tree is written (S, G), with a specific source S.",
                "B": "",
                "C": "Multicast state is not a unicast route; (*, G) is group forwarding state.",
                "D": "(*, G) includes incoming interface and an outgoing interface LIST, not just prunes.",
            },
            "exam_pattern": "(*, G) = shared tree via RP (any source). (S, G) = shortest-path/"
                            "source tree. PIM-SM joins shared first, then may SPT-switch to (S, G).",
        },
        "verify_cli": ["show ip mroute", "show ip pim rp mapping"],
        "references": ["ENCOR 350-401 Topic 3.5 multicast (PIM)"],
        "tags": ["multicast", "pim", "rp"],
    },
    {
        "id": "encor-in-006", "exam": "encor", "domain": "infrastructure",
        "subtopic": "ospf_advanced", "difficulty": 2, "type": "mcq",
        "stem": "Which OSPF area type blocks Type 5 external LSAs but still allows an ASBR "
                "within the area to inject externals as Type 7 LSAs?",
        "options": [
            {"id": "A", "text": "Stub area"},
            {"id": "B", "text": "Totally stubby area"},
            {"id": "C", "text": "NSSA (Not-So-Stubby Area)"},
            {"id": "D", "text": "Backbone area (area 0)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An NSSA blocks ordinary Type 5 externals but permits a local ASBR to "
                       "originate Type 7 LSAs, which the ABR translates back into Type 5 for the "
                       "rest of the OSPF domain.",
            "distractors": {
                "A": "A stub area blocks Type 5 and cannot contain an ASBR at all.",
                "B": "A totally stubby area blocks Type 5 AND Type 3, also no ASBR.",
                "C": "",
                "D": "The backbone carries all LSA types and connects areas; it is not a stub variant.",
            },
            "exam_pattern": "Stub=no Type5 (default route in). Totally stubby=no Type5/Type3. "
                            "NSSA=no Type5 but Type7 allowed (ABR translates 7→5). Totally NSSA adds no Type3.",
        },
        "verify_cli": ["show ip ospf", "show ip ospf database nssa-external"],
        "references": ["ENCOR 350-401 Topic 3.2 OSPF area types"],
        "tags": ["ospf", "nssa", "area-types"],
    },
    {
        "id": "encor-in-007", "exam": "encor", "domain": "infrastructure",
        "subtopic": "layer2_stp_advanced", "difficulty": 2, "type": "mcq",
        "stem": "Which feature, enabled on an access port, will err-disable the port if it "
                "receives a superior BPDU, protecting a configured STP topology from a rogue switch?",
        "options": [
            {"id": "A", "text": "Root Guard"},
            {"id": "B", "text": "BPDU Guard"},
            {"id": "C", "text": "Loop Guard"},
            {"id": "D", "text": "UDLD"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "BPDU Guard err-disables a PortFast-enabled access port the moment it "
                       "receives ANY BPDU — stopping a rogue switch from joining STP on that port.",
            "distractors": {
                "A": "Root Guard puts a port in root-inconsistent (blocking) state on a superior "
                     "BPDU but does not err-disable it; it is used on designated ports facing other switches.",
                "B": "",
                "C": "Loop Guard prevents a blocking port from erroneously moving to forwarding "
                     "when BPDUs STOP arriving — a different failure mode.",
                "D": "UDLD detects unidirectional fiber links, not rogue BPDUs.",
            },
            "exam_pattern": "BPDU Guard = any BPDU on PortFast port → err-disable. Root Guard = "
                            "superior BPDU → root-inconsistent (recovers automatically). Loop Guard "
                            "= missing BPDUs → loop-inconsistent.",
        },
        "verify_cli": ["show spanning-tree summary", "show errdisable recovery"],
        "references": ["ENCOR 350-401 Topic 3.1 STP protection"],
        "tags": ["stp", "bpdu-guard", "root-guard"],
    },
    {
        "id": "encor-in-008", "exam": "encor", "domain": "infrastructure",
        "subtopic": "bgp", "difficulty": 2, "type": "mcq",
        "stem": "An iBGP-learned prefix is in the BGP table but NOT installed in the routing "
                "table or advertised onward, and 'show ip bgp' shows it without a '>' best "
                "marker and flagged as inaccessible. What is the classic cause?",
        "options": [
            {"id": "A", "text": "The BGP next-hop is not reachable via the IGP (next-hop unresolved)"},
            {"id": "B", "text": "The prefix has too short an AS-path"},
            {"id": "C", "text": "Synchronization is disabled"},
            {"id": "D", "text": "The local-preference is too high"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "iBGP does not change the next-hop by default, so if the IGP cannot reach "
                       "that next-hop, the path is invalid and cannot become best. Fixing the IGP "
                       "or using 'next-hop-self' resolves it.",
            "distractors": {
                "A": "",
                "B": "A short AS-path would make a path MORE preferred, not invalid.",
                "C": "Synchronization is off by default on modern IOS and is unrelated to an "
                     "unreachable next-hop.",
                "D": "High local-pref would make the path preferred, not inaccessible.",
            },
            "exam_pattern": "iBGP next-hop stays the eBGP peer's address → must be IGP-reachable. "
                            "Symptom: valid-but-not-best, 'inaccessible'. Fix: redistribute the link "
                            "into IGP or 'neighbor x next-hop-self'.",
        },
        "verify_cli": ["show ip bgp", "show ip route <next-hop>"],
        "references": ["ENCOR 350-401 Topic 3.4 BGP next-hop"],
        "tags": ["bgp", "ibgp", "next-hop-self"],
    },
    {
        "id": "encor-in-009", "exam": "encor", "domain": "infrastructure",
        "subtopic": "qos", "difficulty": 2, "type": "mcq",
        "stem": "Which QoS mechanism DROPS or RE-MARKS traffic that exceeds a configured rate "
                "(rather than buffering it), and is therefore better suited to high-speed "
                "interfaces where delay must stay low?",
        "options": [
            {"id": "A", "text": "Policing"},
            {"id": "B", "text": "Shaping"},
            {"id": "C", "text": "WRED"},
            {"id": "D", "text": "LLQ"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Policing enforces a rate by dropping or re-marking excess traffic "
                       "immediately — no queuing/delay. It can be applied inbound or outbound and "
                       "produces a hard rate limit.",
            "distractors": {
                "A": "",
                "B": "Shaping BUFFERS excess traffic to smooth it to the rate, adding delay; it "
                     "is outbound only — the opposite trade-off.",
                "C": "WRED is a congestion-AVOIDANCE drop mechanism within queues, not a rate enforcer.",
                "D": "LLQ is a priority queuing method for real-time traffic, not a policer.",
            },
            "exam_pattern": "Policing = drop/re-mark excess (no delay, in or out). Shaping = buffer "
                            "excess (adds delay, outbound). WRED = selective drops to avoid tail drop. "
                            "LLQ = strict priority queue.",
        },
        "verify_cli": ["show policy-map interface g0/0", "show policy-map"],
        "references": ["ENCOR 350-401 Topic 3.6 QoS (policing vs shaping)"],
        "tags": ["qos", "policing", "shaping"],
    },
    {
        "id": "encor-in-010", "exam": "encor", "domain": "infrastructure",
        "subtopic": "ospf_advanced", "difficulty": 2, "type": "fill",
        "stem": "To make all OSPF Gigabit and 10-Gig links show distinct costs, you set a "
                "network-wide OSPF reference bandwidth of 10 Gbps. Enter the exact router-ospf "
                "command (values in Mbps).",
        "options": [],
        "correct": [
            "auto-cost reference-bandwidth 10000",
            "auto-cost reference-bandwidth 10000 ",
        ],
        "explanation": {
            "correct": "'auto-cost reference-bandwidth 10000' sets the reference to 10,000 Mbps "
                       "(10 Gbps), so a 1 Gbps link gets cost 10 and a 10 Gbps link cost 1 — "
                       "distinguishable instead of all flooring to 1.",
            "distractors": {},
            "exam_pattern": "Reference bandwidth is in Mbps. Must be set identically on ALL "
                            "routers or costs become inconsistent. Default is 100 (100 Mbps).",
        },
        "verify_cli": ["show ip ospf", "show ip ospf interface g0/0"],
        "references": ["ENCOR 350-401 Topic 3.2 OSPF cost"],
        "tags": ["ospf", "reference-bandwidth"],
    },

    # ===================== 4.0 NETWORK ASSURANCE =====================
    {
        "id": "encor-as-001", "exam": "encor", "domain": "network_assurance",
        "subtopic": "spans", "difficulty": 2, "type": "mcq",
        "stem": "You must capture traffic from a source switch and deliver it to an analyzer "
                "attached to a DIFFERENT switch across the campus. Which feature is required?",
        "options": [
            {"id": "A", "text": "Local SPAN"},
            {"id": "B", "text": "RSPAN (Remote SPAN)"},
            {"id": "C", "text": "A simple port mirror on the analyzer switch"},
            {"id": "D", "text": "NetFlow export"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "RSPAN carries mirrored traffic across switches using a dedicated RSPAN "
                       "VLAN trunked between them, so the analyzer can sit on a different switch "
                       "than the source.",
            "distractors": {
                "A": "Local SPAN only mirrors between ports on the SAME switch.",
                "B": "",
                "C": "A local mirror on the analyzer switch cannot see traffic on the remote source switch.",
                "D": "NetFlow exports flow STATISTICS, not a full packet copy for analysis.",
            },
            "exam_pattern": "Local SPAN=same switch. RSPAN=across switches via RSPAN VLAN. "
                            "ERSPAN=across an L3/routed network via GRE. NetFlow=stats, not packets.",
        },
        "verify_cli": ["show monitor session all", "show monitor"],
        "references": ["ENCOR 350-401 Topic 4.1 SPAN/RSPAN/ERSPAN"],
        "tags": ["span", "rspan", "capture"],
    },
    {
        "id": "encor-as-002", "exam": "encor", "domain": "network_assurance",
        "subtopic": "ipsla", "difficulty": 2, "type": "mcq",
        "stem": "An IP SLA ICMP-echo operation is tracked and tied to a static default route so "
                "the route is withdrawn if the next hop stops responding. Which object links the "
                "SLA result to the route?",
        "options": [
            {"id": "A", "text": "A 'track' object referencing the IP SLA, used in the ip route command"},
            {"id": "B", "text": "An EEM applet that deletes the route"},
            {"id": "C", "text": "A route-map with a match clause"},
            {"id": "D", "text": "A prefix-list"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "You create 'track <n> ip sla <id> reachability' and append the track to "
                       "the static route ('ip route ... track <n>'). When the SLA fails, the track "
                       "goes down and IOS removes the route.",
            "distractors": {
                "A": "",
                "B": "An EEM applet could script it, but the standard, purpose-built mechanism is "
                     "object tracking tied to IP SLA.",
                "C": "Route-maps filter/modify routes; they do not tie an SLA probe to a static route.",
                "D": "A prefix-list matches prefixes; it does not track reachability.",
            },
            "exam_pattern": "IP SLA + object tracking + static route = reliable static routing/"
                            "failover. 'ip route ... track N' is the glue. Often paired with a "
                            "floating static backup.",
        },
        "verify_cli": ["show ip sla statistics", "show track"],
        "references": ["ENCOR 350-401 Topic 4.2 IP SLA / object tracking"],
        "tags": ["ipsla", "tracking"],
    },
    {
        "id": "encor-as-003", "exam": "encor", "domain": "network_assurance",
        "subtopic": "flexible_netflow", "difficulty": 3, "type": "mcq",
        "stem": "In Flexible NetFlow, which component defines WHICH key and non-key fields are "
                "collected for a flow (e.g., match source/destination IP, collect byte counts)?",
        "options": [
            {"id": "A", "text": "The flow record"},
            {"id": "B", "text": "The flow exporter"},
            {"id": "C", "text": "The flow monitor"},
            {"id": "D", "text": "The sampler"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The flow record defines the fields: 'match' statements are the KEY fields "
                       "that define a unique flow, and 'collect' statements are the non-key fields "
                       "(counters/attributes) gathered.",
            "distractors": {
                "A": "",
                "B": "The flow exporter defines WHERE flow data is sent (collector IP, port, version).",
                "C": "The flow monitor ties a record + exporter together and is applied to an interface.",
                "D": "A sampler reduces load by sampling 1-in-N packets; it does not define fields.",
            },
            "exam_pattern": "FNF pieces: record (what: match=key, collect=non-key), exporter "
                            "(where to send), monitor (binds record+exporter to interface), sampler (how often).",
        },
        "verify_cli": ["show flow record", "show flow monitor"],
        "references": ["ENCOR 350-401 Topic 4.2 Flexible NetFlow"],
        "tags": ["netflow", "flexible-netflow"],
    },
    {
        "id": "encor-as-004", "exam": "encor", "domain": "network_assurance",
        "subtopic": "diagnostics_tools", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about SNMP vs model-driven telemetry (MDT) for network "
                "monitoring is correct?",
        "options": [
            {"id": "A", "text": "SNMP pull-polls at intervals; streaming telemetry pushes data continuously based on subscriptions"},
            {"id": "B", "text": "SNMP pushes data continuously; telemetry only polls on request"},
            {"id": "C", "text": "Both require the collector to poll each OID individually every second"},
            {"id": "D", "text": "Telemetry cannot use YANG models"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Traditional SNMP is pull-based (the NMS polls OIDs periodically). "
                       "Model-driven telemetry is push-based: the device streams data per a "
                       "subscription (periodic or on-change), scaling better with less overhead.",
            "distractors": {
                "A": "",
                "B": "This is reversed — SNMP polls, telemetry pushes.",
                "C": "Per-OID per-second polling is exactly the SNMP scalability problem telemetry solves.",
                "D": "MDT is built ON YANG models (via NETCONF/gRPC/gNMI); it absolutely uses them.",
            },
            "exam_pattern": "SNMP = pull/poll, OID-based, higher overhead at scale. MDT = push/"
                            "stream, YANG-based, periodic or on-change subscriptions (gRPC/gNMI).",
        },
        "verify_cli": ["show telemetry ietf subscription all", "show run | section telemetry"],
        "references": ["ENCOR 350-401 Topic 4.3 telemetry vs SNMP"],
        "tags": ["telemetry", "snmp", "mdt"],
    },

    {
        "id": "encor-as-005", "exam": "encor", "domain": "network_assurance",
        "subtopic": "snmp_syslog", "difficulty": 2, "type": "mcq",
        "stem": "Your NMS must be certain it received each SNMP notification from a router, "
                "even across a lossy WAN. Which notification type should the router send, and "
                "why?",
        "options": [
            {"id": "A", "text": "SNMP inform, because the NMS acknowledges it and the router retransmits if no ack arrives"},
            {"id": "B", "text": "SNMP trap, because traps are acknowledged by the NMS"},
            {"id": "C", "text": "SNMP trap, because traps use TCP for guaranteed delivery"},
            {"id": "D", "text": "Syslog level 7, because debugging messages are always reliable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SNMP inform is acknowledged by the receiver; if the router gets no "
                       "ack, it retransmits — giving reliable delivery at the cost of more memory "
                       "and bandwidth. Ideal when losing a notification is unacceptable.",
            "distractors": {
                "A": "",
                "B": "Traps are fire-and-forget: the NMS does NOT acknowledge them, so a dropped "
                     "trap is simply lost.",
                "C": "Both traps and informs ride over UDP (162); traps do not use TCP.",
                "D": "Syslog over UDP 514 is also unacknowledged, and severity 7 just means more "
                     "verbose messages, not reliability.",
            },
            "exam_pattern": "Trap = unacknowledged, lightweight, can be lost. Inform = "
                            "acknowledged + retransmitted, heavier but reliable. Both UDP/162; "
                            "the 'must be sure it arrived' clue = inform.",
        },
        "verify_cli": ["show snmp", "show snmp host"],
        "references": ["ENCOR 350-401 Topic 4.4 SNMP traps/informs"],
        "tags": ["snmp", "trap", "inform"],
    },

    # ===================== 5.0 SECURITY =====================
    {
        "id": "encor-se-001", "exam": "encor", "domain": "security",
        "subtopic": "device_access_control", "difficulty": 2, "type": "mcq",
        "stem": "Which Control Plane Policing (CoPP) use case best protects a router's CPU?",
        "options": [
            {"id": "A", "text": "Rate-limiting traffic destined to the device's control plane (e.g., excessive SSH/SNMP/ICMP to the router itself)"},
            {"id": "B", "text": "Blocking all transit user data through the router"},
            {"id": "C", "text": "Encrypting management sessions"},
            {"id": "D", "text": "Load-balancing routing updates"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CoPP applies a QoS policy to the control plane to rate-limit or drop "
                       "traffic punted to the CPU (management, routing, exceptions), shielding the "
                       "CPU from floods/DoS while leaving transit traffic in hardware.",
            "distractors": {
                "A": "",
                "B": "CoPP protects the device's own CPU, not a tool to block all transit traffic.",
                "C": "Encryption of sessions is SSH/TLS, not CoPP's function.",
                "D": "CoPP does not load-balance; it polices control-plane-bound traffic.",
            },
            "exam_pattern": "CoPP = protect the CPU/control plane with a policy-map applied under "
                            "'control-plane'. Classify management/routing/ICMP, then police. Transit "
                            "data is unaffected.",
        },
        "verify_cli": ["show policy-map control-plane", "show control-plane"],
        "references": ["ENCOR 350-401 Topic 5.1 device access/CoPP"],
        "tags": ["copp", "control-plane"],
    },
    {
        "id": "encor-se-002", "exam": "encor", "domain": "security",
        "subtopic": "network_access_control_8021x", "difficulty": 2, "type": "mcq",
        "stem": "Which protocol does a Cisco switch (authenticator) use to communicate with "
                "Cisco ISE (authentication server) in an 802.1X deployment, carrying the EAP "
                "exchange?",
        "options": [
            {"id": "A", "text": "RADIUS"},
            {"id": "B", "text": "TACACS+"},
            {"id": "C", "text": "LDAP"},
            {"id": "D", "text": "Kerberos"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.1X uses EAP over LAN (EAPoL) between supplicant and switch, and the "
                       "switch relays EAP to the server inside RADIUS (EAP-over-RADIUS). ISE is a "
                       "RADIUS server for authentication.",
            "distractors": {
                "A": "",
                "B": "TACACS+ is used for device ADMINISTRATION AAA (command authorization), not "
                     "802.1X network access authentication.",
                "C": "LDAP may be an identity store ISE queries, but it is not the switch-to-ISE "
                     "802.1X transport.",
                "D": "Kerberos is not the 802.1X authenticator-to-server protocol.",
            },
            "exam_pattern": "802.1X: EAPoL (supplicant↔switch) + RADIUS (switch↔ISE). RADIUS=network "
                            "access (UDP 1812/1813). TACACS+=device admin (TCP 49).",
        },
        "verify_cli": ["show authentication sessions interface g1/0/1", "show aaa servers"],
        "references": ["ENCOR 350-401 Topic 5.2 network access control"],
        "tags": ["dot1x", "radius", "ise"],
    },
    {
        "id": "encor-se-003", "exam": "encor", "domain": "security",
        "subtopic": "device_access_control", "difficulty": 2, "type": "mcq",
        "stem": "For administrative AAA, you need per-command authorization and full command "
                "accounting of what admins type on the CLI. Which protocol is the right choice "
                "and why?",
        "options": [
            {"id": "A", "text": "TACACS+, because it separates AAA functions and supports per-command authorization"},
            {"id": "B", "text": "RADIUS, because it encrypts the entire packet"},
            {"id": "C", "text": "SNMPv3, because it supports authPriv"},
            {"id": "D", "text": "RADIUS, because it uses TCP for reliability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TACACS+ separates authentication, authorization, and accounting, and "
                       "supports granular per-command authorization — ideal for device admin. It "
                       "runs over TCP 49 and encrypts the entire payload.",
            "distractors": {
                "A": "",
                "B": "RADIUS encrypts only the password field, not the whole packet, and lumps "
                     "authN/authZ together — weaker for per-command control.",
                "C": "SNMPv3 is for management data, not interactive admin command authorization.",
                "D": "RADIUS uses UDP, not TCP; the 'TCP reliability' claim actually describes TACACS+.",
            },
            "exam_pattern": "TACACS+ = device admin (TCP 49, full encryption, per-command authZ, "
                            "AAA separated). RADIUS = network access (UDP, password-only encryption, "
                            "authN+authZ combined).",
        },
        "verify_cli": ["show tacacs", "show aaa servers"],
        "references": ["ENCOR 350-401 Topic 5.1 TACACS+ vs RADIUS"],
        "tags": ["tacacs", "radius", "aaa"],
    },
    {
        "id": "encor-se-004", "exam": "encor", "domain": "security",
        "subtopic": "infrastructure_security_acls", "difficulty": 2, "type": "mcq",
        "stem": "Which feature uses Security Group Tags (SGTs) to enforce policy based on group "
                "membership rather than IP addresses, decoupling policy from the network topology?",
        "options": [
            {"id": "A", "text": "Cisco TrustSec"},
            {"id": "B", "text": "A standard numbered ACL"},
            {"id": "C", "text": "uRPF"},
            {"id": "D", "text": "Port security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cisco TrustSec classifies traffic with Security Group Tags and enforces "
                       "Security Group ACLs (SGACLs) based on group, so policy follows identity "
                       "instead of IP/subnet.",
            "distractors": {
                "A": "",
                "B": "Standard ACLs match source IP only — exactly the topology-coupled approach "
                     "TrustSec replaces.",
                "C": "uRPF validates source addresses against the routing table (anti-spoofing), not group policy.",
                "D": "Port security limits MAC addresses on a port; it is not group-based policy.",
            },
            "exam_pattern": "TrustSec = SGT classification + SGACL enforcement, policy by group "
                            "not IP. Tags propagate inline (CMD) or via SXP. Often tied to ISE.",
        },
        "verify_cli": ["show cts role-based sgt-map all", "show cts environment-data"],
        "references": ["ENCOR 350-401 Topic 5.4 TrustSec/SGACL"],
        "tags": ["trustsec", "sgt", "sgacl"],
    },
    {
        "id": "encor-se-005", "exam": "encor", "domain": "security",
        "subtopic": "wireless_security", "difficulty": 2, "type": "mcq",
        "stem": "Which wireless security standard introduces SAE (Simultaneous Authentication "
                "of Equals) to replace the WPA2 pre-shared-key 4-way-handshake weaknesses?",
        "options": [
            {"id": "A", "text": "WPA3"},
            {"id": "B", "text": "WPA2-Enterprise"},
            {"id": "C", "text": "WEP"},
            {"id": "D", "text": "Open authentication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "WPA3-Personal uses SAE (a.k.a. Dragonfly) for the handshake, providing "
                       "forward secrecy and resistance to offline dictionary attacks that plagued "
                       "WPA2-PSK.",
            "distractors": {
                "A": "",
                "B": "WPA2-Enterprise uses 802.1X/EAP (not PSK) but still relies on the older "
                     "handshake; SAE is a WPA3 feature.",
                "C": "WEP is the deprecated, broken legacy encryption (RC4) — the opposite of modern security.",
                "D": "Open authentication provides no encryption or authentication at all.",
            },
            "exam_pattern": "WPA3-Personal = SAE (replaces PSK 4-way handshake, adds forward "
                            "secrecy). WPA3-Enterprise = stronger 192-bit suite option. WEP/Open = insecure.",
        },
        "verify_cli": ["show wlan summary", "show wlan id 1"],
        "references": ["ENCOR 350-401 Topic 5.5 wireless security (WPA3)"],
        "tags": ["wpa3", "sae", "wireless-security"],
    },

    # ===================== 6.0 AUTOMATION =====================
    {
        "id": "encor-au-001", "exam": "encor", "domain": "automation",
        "subtopic": "eem_scripting", "difficulty": 3, "type": "mcq",
        "stem": "Which Embedded Event Manager (EEM) configuration will run a CLI action "
                "automatically when interface GigabitEthernet0/1 goes down?",
        "options": [
            {"id": "A", "text": "An applet with 'event syslog pattern \"%LINK-3-UPDOWN.*GigabitEthernet0/1.*down\"'"},
            {"id": "B", "text": "A route-map matching the interface"},
            {"id": "C", "text": "A static 'ip sla' probe with no track"},
            {"id": "D", "text": "A prefix-list referencing the interface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EEM applets fire on events; a 'event syslog pattern' that matches the "
                       "%LINK-3-UPDOWN down message for Gi0/1 triggers the applet, whose 'action' "
                       "lines then run CLI (e.g., 'cli command'). 'event none' allows manual runs.",
            "distractors": {
                "A": "",
                "B": "Route-maps filter routes; they cannot trigger actions on an interface event.",
                "C": "An IP SLA probe measures reachability but does not itself run CLI actions.",
                "D": "Prefix-lists match prefixes for routing policy, not event-driven scripting.",
            },
            "exam_pattern": "EEM = event detector (syslog/snmp/timer/interface/none) + actions "
                            "(cli/syslog/mail). Match on syslog patterns or track objects to automate reactions.",
        },
        "verify_cli": ["show event manager policy registered", "show event manager history events"],
        "references": ["ENCOR 350-401 Topic 6.3 EEM"],
        "tags": ["eem", "automation", "scripting"],
    },
    {
        "id": "encor-au-002", "exam": "encor", "domain": "automation",
        "subtopic": "json_yaml_xml", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about YAML (as used in Ansible) is correct?",
        "options": [
            {"id": "A", "text": "Indentation (spaces, not tabs) defines structure; lists use '- ' and maps use 'key: value'"},
            {"id": "B", "text": "YAML requires curly braces for every object like JSON"},
            {"id": "C", "text": "Tabs are the required indentation character in YAML"},
            {"id": "D", "text": "YAML cannot represent nested data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "YAML is whitespace-significant: consistent SPACE indentation defines "
                       "hierarchy, '- ' denotes list items, and 'key: value' defines mappings. It "
                       "is a superset of JSON but far more human-readable.",
            "distractors": {
                "A": "",
                "B": "YAML does not require braces; flow style (braces) is optional, block style "
                     "(indentation) is typical.",
                "C": "TABS are explicitly forbidden for indentation in YAML — a common breakage.",
                "D": "YAML represents arbitrarily nested maps and lists.",
            },
            "exam_pattern": "YAML: spaces only (no tabs), '-' for list items, 'key: value' maps, "
                            "indentation = hierarchy. JSON = braces/brackets. XML = tags. Know how each nests.",
        },
        "verify_cli": [],
        "references": ["ENCOR 350-401 Topic 6.5 data formats (YAML/JSON/XML)"],
        "tags": ["yaml", "ansible", "data-format"],
    },
    {
        "id": "encor-au-003", "exam": "encor", "domain": "automation",
        "subtopic": "netconf_restconf_encor", "difficulty": 3, "type": "mcq",
        "stem": "A NETCONF client must commit a change only if it validates, with the ability "
                "to roll back. Which NETCONF datastore feature supports this edit-then-commit "
                "workflow?",
        "options": [
            {"id": "A", "text": "The candidate datastore with <commit>/<discard-changes>"},
            {"id": "B", "text": "Writing directly to the running datastore only"},
            {"id": "C", "text": "The startup datastore via TFTP"},
            {"id": "D", "text": "SNMP SET operations"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NETCONF's candidate datastore lets you stage edits, validate, then apply "
                       "them atomically with <commit> (or throw them away with <discard-changes>), "
                       "enabling safe, roll-back-able changes.",
            "distractors": {
                "A": "",
                "B": "Editing running directly applies immediately with no staging/rollback window.",
                "C": "Startup is the saved boot config; TFTP is not a NETCONF commit workflow.",
                "D": "SNMP SET is not a NETCONF datastore operation and lacks this transactional model.",
            },
            "exam_pattern": "NETCONF datastores: running (active), candidate (staging for commit), "
                            "startup (boot). Candidate + <commit> = transactional config. RESTCONF "
                            "lacks candidate/commit semantics.",
        },
        "verify_cli": ["show netconf-yang sessions", "show running-config | section netconf"],
        "references": ["ENCOR 350-401 Topic 6.4 NETCONF datastores"],
        "tags": ["netconf", "candidate", "datastore"],
    },
    {
        "id": "encor-au-004", "exam": "encor", "domain": "automation",
        "subtopic": "python_data", "difficulty": 2, "type": "mcq",
        "stem": "In Python, you parse a RESTCONF JSON response into the variable 'data'. The "
                "interface list is at data['ietf-interfaces:interfaces']['interface']. What is "
                "the type of that value, and how do you get the first interface's name?",
        "options": [
            {"id": "A", "text": "A list of dicts; data['ietf-interfaces:interfaces']['interface'][0]['name']"},
            {"id": "B", "text": "A string; use .split() to get the name"},
            {"id": "C", "text": "An integer index into a tuple"},
            {"id": "D", "text": "A set; use .pop() to read the name"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "YANG 'interface' is a list, so JSON decodes it to a Python list of dicts. "
                       "Index [0] gives the first dict, and ['name'] reads its name key.",
            "distractors": {
                "A": "",
                "B": "It is structured data (list of objects), not a flat string to split.",
                "C": "JSON arrays map to Python lists, not tuples, and you index them by position.",
                "D": "JSON has no set type; arrays become ordered lists, not unordered sets.",
            },
            "exam_pattern": "JSON→Python: object→dict, array→list, string→str, true/false→bool, "
                            "null→None. Navigate nested data with ['key'] and [index].",
        },
        "verify_cli": [],
        "references": ["ENCOR 350-401 Topic 6.6 Python data handling"],
        "tags": ["python", "json", "restconf"],
    },
    {
        "id": "encor-au-005", "exam": "encor", "domain": "automation",
        "subtopic": "controllers_apis", "difficulty": 2, "type": "mcq",
        "stem": "A script authenticates to Cisco Catalyst Center (DNA Center) and receives a "
                "token to include in subsequent API calls. In which HTTP header is that token "
                "typically placed for later requests?",
        "options": [
            {"id": "A", "text": "X-Auth-Token"},
            {"id": "B", "text": "Content-Length"},
            {"id": "C", "text": "User-Agent"},
            {"id": "D", "text": "Host"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Catalyst Center issues a token from POST /dna/system/api/v1/auth/token; "
                       "clients send it back in the 'X-Auth-Token' header on subsequent REST calls "
                       "to prove they are authenticated.",
            "distractors": {
                "A": "",
                "B": "Content-Length describes the body size, not authentication.",
                "C": "User-Agent identifies the client software, not the auth token.",
                "D": "Host names the target server; it carries no credentials.",
            },
            "exam_pattern": "Token-based REST auth: POST credentials → get token → send token in "
                            "an auth header (X-Auth-Token for Catalyst Center; often 'Authorization: "
                            "Bearer' elsewhere) on each call.",
        },
        "verify_cli": [],
        "references": ["ENCOR 350-401 Topic 6.2 controllers/APIs"],
        "tags": ["dnac", "catalyst-center", "api-token"],
    },
]
