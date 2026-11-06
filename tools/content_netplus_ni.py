"""CompTIA Network+ N10-009 — Domain 2.0 Network Implementation EXPANSION pool.

Original, objective-aligned questions that deepen the Network Implementation
bank (routing, switching, wireless standards, physical installations) to real
exam depth. Auto-discovered and merged by build_content.py via the
content_netplus_*.py glob. Same authoring rules as the other pools: original
content mapped to the public exam objectives, never real exam items.
build_content.py shuffles option order (seeded by id), so the answer key here
is not positionally biased.

IDs continue from the base pool's netplus-ni-006 at netplus-ni-101+.
"""

QUESTIONS = [
    # ===== routing_technologies =============================================
    {
        "id": "netplus-ni-101", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A branch router must forward any traffic for which it has no more specific "
                "entry to its ISP. Which route accomplishes this?",
        "options": [
            {"id": "A", "text": "A default route (0.0.0.0/0) pointing at the ISP next hop"},
            {"id": "B", "text": "A host route (0.0.0.0/32) for the unspecified address"},
            {"id": "C", "text": "A summary route for 10.0.0.0/8"},
            {"id": "D", "text": "A route to 255.255.255.255/32"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A default route (0.0.0.0/0) — the gateway of last resort — matches every "
                       "destination not covered by a more specific route and forwards it to the ISP.",
            "distractors": {
                "B": "0.0.0.0/32 is a single-host route for the unspecified address, not a catch-all for all networks.",
                "C": "A 10.0.0.0/8 summary only matches that private range, not 'everything else.'",
                "D": "255.255.255.255 is the limited broadcast address; a /32 route to it is not a default route.",
            },
            "exam_pattern": "Default route = 0.0.0.0/0 (IPv4) or ::/0 (IPv6) = gateway of last resort for unknown destinations.",
        },
    },
    {
        "id": "netplus-ni-102", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 3, "type": "mcq",
        "stem": "A routing table contains 10.1.1.0/24 via R1, 10.1.0.0/16 via R2, and "
                "0.0.0.0/0 via R3. A packet is destined for 10.1.1.55. Which next hop is used?",
        "options": [
            {"id": "A", "text": "R1, because 10.1.1.0/24 is the longest-prefix match"},
            {"id": "B", "text": "R2, because 10.1.0.0/16 covers a larger range"},
            {"id": "C", "text": "R3, the default route"},
            {"id": "D", "text": "The packet is load-balanced across all three paths"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When several routes match, the router always uses the most specific (longest) "
                       "prefix. 10.1.1.55 matches /24, /16, and /0, and the /24 is longest, so R1 wins.",
            "distractors": {
                "B": "The /16 matches but is less specific than the /24; longest-prefix match prefers the /24.",
                "C": "The default (/0) is the least specific and is used only when nothing more specific matches.",
                "D": "Equal-cost load balancing applies only to multiple routes of the SAME prefix length and metric, not routes of different lengths.",
            },
            "exam_pattern": "Longest (most specific) prefix always wins — evaluated before administrative distance or metric.",
        },
    },
    {
        "id": "netplus-ni-103", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A company has a single public IPv4 address but hundreds of internal hosts that "
                "must reach the Internet at the same time. Which technology lets them all share "
                "that one public address?",
        "options": [
            {"id": "A", "text": "PAT (NAT overload), which distinguishes sessions by source port"},
            {"id": "B", "text": "Static one-to-one NAT"},
            {"id": "C", "text": "DHCP reservations"},
            {"id": "D", "text": "Assigning each host a public /24 address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PAT (Port Address Translation, also called NAT overload) maps many private "
                       "addresses to one public address, using a unique source port per session to keep them apart.",
            "distractors": {
                "B": "Static NAT maps one private address to one public address, so it cannot share a single public address among many hosts.",
                "C": "DHCP hands out internal addresses; it performs no address translation to the public Internet.",
                "D": "The scenario provides only one public address, so a per-host public /24 is not available.",
            },
            "exam_pattern": "Many private hosts behind ONE public IP = PAT / NAT overload (port-based). One-to-one = static NAT.",
        },
    },
    {
        "id": "netplus-ni-104", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A single router interface must route between several VLANs that arrive from a "
                "switch over one 802.1Q trunk. How is this configured?",
        "options": [
            {"id": "A", "text": "One subinterface per VLAN, each with an 802.1Q tag and gateway IP (router-on-a-stick)"},
            {"id": "B", "text": "The physical interface configured as a single access port"},
            {"id": "C", "text": "Spanning Tree enabled on the router interface"},
            {"id": "D", "text": "All VLANs sharing one IP subnet on the physical interface"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Router-on-a-stick splits one physical interface into logical subinterfaces, one "
                       "per VLAN, each tagged with 802.1Q and given the gateway IP for that VLAN's subnet.",
            "distractors": {
                "B": "An access port carries a single untagged VLAN and cannot route among multiple VLANs.",
                "C": "STP is a Layer 2 loop-prevention protocol on switches; it does nothing for inter-VLAN routing.",
                "D": "Each VLAN must be its own subnet with its own gateway; one shared subnet defeats the separation VLANs provide.",
            },
            "exam_pattern": "One router interface + trunk + multiple VLANs = 802.1Q subinterfaces (router-on-a-stick).",
        },
    },
    {
        "id": "netplus-ni-105", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A network requires default-gateway redundancy using a protocol that is an open "
                "IETF standard rather than vendor-proprietary. Which first-hop redundancy "
                "protocol fits?",
        "options": [
            {"id": "A", "text": "VRRP"},
            {"id": "B", "text": "HSRP"},
            {"id": "C", "text": "GLBP"},
            {"id": "D", "text": "STP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VRRP (Virtual Router Redundancy Protocol) is the open IETF-standard FHRP: it "
                       "presents a virtual IP as the default gateway with a master router and backups.",
            "distractors": {
                "B": "HSRP provides the same gateway redundancy but is Cisco-proprietary, not an open standard.",
                "C": "GLBP is also Cisco-proprietary (and adds load balancing across gateways), so it is not an open standard.",
                "D": "STP prevents Layer 2 switching loops; it is not a gateway-redundancy protocol.",
            },
            "exam_pattern": "FHRP gateway redundancy: VRRP = open standard; HSRP and GLBP = Cisco proprietary.",
        },
    },
    {
        "id": "netplus-ni-106", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly describes the metric a routing protocol uses to choose "
                "the best path?",
        "options": [
            {"id": "A", "text": "OSPF uses a cost derived from interface bandwidth"},
            {"id": "B", "text": "RIP selects paths by the lowest administrative distance"},
            {"id": "C", "text": "OSPF counts the number of router hops"},
            {"id": "D", "text": "BGP always chooses the path with the highest bandwidth"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OSPF is a link-state protocol whose metric is cost, calculated inversely from "
                       "interface bandwidth, so the lower-cost (higher-bandwidth) path is preferred.",
            "distractors": {
                "B": "RIP's metric is hop count (max 15). Administrative distance chooses BETWEEN protocols, it is not RIP's path metric.",
                "C": "Hop count is RIP's metric; OSPF uses bandwidth-based cost, not hops.",
                "D": "BGP selects paths using attributes such as AS-path length and local preference, not raw bandwidth.",
            },
            "exam_pattern": "RIP = hop count; OSPF = cost (bandwidth); EIGRP = bandwidth+delay composite; BGP = path attributes.",
        },
    },

    # ===== switching_technologies ===========================================
    {
        "id": "netplus-ni-107", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 3, "type": "mcq",
        "stem": "In a spanning-tree topology, how is the root bridge elected?",
        "options": [
            {"id": "A", "text": "The switch with the lowest bridge ID (priority, then lowest MAC address) becomes root"},
            {"id": "B", "text": "The switch with the highest IP address becomes root"},
            {"id": "C", "text": "The switch with the most active ports becomes root"},
            {"id": "D", "text": "The switch that booted most recently becomes root"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "STP elects the root bridge as the switch with the lowest bridge ID — priority "
                       "first, with the lowest MAC address breaking ties.",
            "distractors": {
                "B": "STP operates at Layer 2 and does not use IP addresses in the election.",
                "C": "Port count has no bearing on which switch becomes root.",
                "D": "Boot order does not decide the root; the lowest bridge ID does.",
            },
            "exam_pattern": "Root bridge = lowest bridge ID (priority + MAC). Lower priority wins; tie broken by lowest MAC.",
        },
    },
    {
        "id": "netplus-ni-108", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "mcq",
        "stem": "On an 802.1Q trunk, frames for one VLAN cross the link untagged. What is that "
                "VLAN called, and what is the key hardening recommendation for it?",
        "options": [
            {"id": "A", "text": "The native VLAN; change it from the default VLAN 1 and do not use it for user data"},
            {"id": "B", "text": "The voice VLAN; it must always remain VLAN 1"},
            {"id": "C", "text": "The management VLAN; by definition it is always tagged"},
            {"id": "D", "text": "The default VLAN; it can never be changed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The native VLAN carries untagged frames on a trunk. Best practice is to move it "
                       "off the default VLAN 1 and keep user traffic out of it to reduce VLAN-hopping risk.",
            "distractors": {
                "B": "A voice VLAN carries tagged IP-phone traffic; it is not the untagged native VLAN and need not be VLAN 1.",
                "C": "The native VLAN is untagged by definition, so describing it as always tagged is incorrect.",
                "D": "VLAN 1 is the default native VLAN, but it can and should be changed for security.",
            },
            "exam_pattern": "Native VLAN = the untagged VLAN on an 802.1Q trunk; change it off VLAN 1 to harden against VLAN hopping.",
        },
    },
    {
        "id": "netplus-ni-109", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 1, "type": "mcq",
        "stem": "An administrator wants a switch access port to accept only one known MAC address "
                "and to disable itself if a different device connects. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Port security"},
            {"id": "B", "text": "DHCP snooping"},
            {"id": "C", "text": "Port mirroring (SPAN)"},
            {"id": "D", "text": "Spanning Tree PortFast"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Port security restricts which and how many MAC addresses may use a port and can "
                       "take a violation action such as err-disabling (shutting down) the port.",
            "distractors": {
                "B": "DHCP snooping blocks rogue DHCP server replies; it does not lock a port to a specific MAC.",
                "C": "SPAN copies traffic to a monitor port for analysis; it enforces no MAC restrictions.",
                "D": "PortFast skips STP listening/learning to speed up access-port startup; it is not a security control.",
            },
            "exam_pattern": "Lock a port to specific/limited MACs = port security (violation modes: shutdown, restrict, protect).",
        },
    },
    {
        "id": "netplus-ni-110", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 3, "type": "mcq",
        "stem": "An installer must power a pan-tilt-zoom camera that draws about 45 W at the "
                "device. Which PoE standard is required?",
        "options": [
            {"id": "A", "text": "802.3bt (PoE++ / 4PPoE), up to 60-100 W"},
            {"id": "B", "text": "802.3af (PoE), 15.4 W"},
            {"id": "C", "text": "802.3at (PoE+), 30 W"},
            {"id": "D", "text": "802.3ab (1000BASE-T)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "45 W exceeds both PoE (15.4 W) and PoE+ (30 W), so 802.3bt (PoE++/4PPoE) is "
                       "required; it supplies up to 60 W (Type 3) or ~100 W (Type 4) at the source.",
            "distractors": {
                "B": "802.3af (PoE) provides only 15.4 W at the source (~12.95 W at the device) — far short of 45 W.",
                "C": "802.3at (PoE+) provides 30 W at the source (~25.5 W at the device) — still insufficient.",
                "D": "802.3ab is the 1000BASE-T Gigabit-over-copper standard, not a power-delivery standard.",
            },
            "exam_pattern": "PoE 802.3af = 15.4 W; PoE+ 802.3at = 30 W; PoE++ 802.3bt = 60 W (Type 3) / up to 100 W (Type 4).",
        },
    },
    {
        "id": "netplus-ni-111", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "multi",
        "stem": "A team bonds four physical links between two switches into one logical link using "
                "LACP. Which two benefits does this provide? (Choose two.)",
        "options": [
            {"id": "A", "text": "Increased aggregate bandwidth between the switches"},
            {"id": "B", "text": "Redundancy if one member link fails"},
            {"id": "C", "text": "Automatic routing between VLANs"},
            {"id": "D", "text": "Removal of the need to run STP on any port"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Link aggregation (LACP / 802.3ad) combines links so their bandwidth adds up, and "
                       "traffic shifts to the surviving members if one link in the bundle fails.",
            "distractors": {
                "C": "Inter-VLAN routing is a Layer 3 function; aggregation is a Layer 2/physical bonding of links.",
                "D": "The bundle appears to STP as a single logical link, but STP still runs and protects all other ports.",
            },
            "exam_pattern": "LACP/LAG = more bandwidth + link redundancy between two devices; it is not routing and does not replace STP.",
        },
    },
    {
        "id": "netplus-ni-112", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "mcq",
        "stem": "To raise throughput on an iSCSI storage network, an administrator enables jumbo "
                "frames. What MTU is typically used, and where must it be set?",
        "options": [
            {"id": "A", "text": "An MTU of 9000 bytes, configured consistently on every device in the path"},
            {"id": "B", "text": "An MTU of 1500 bytes, on the server only"},
            {"id": "C", "text": "An MTU of 576 bytes, end to end"},
            {"id": "D", "text": "An MTU of 68 bytes, on the switch only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Jumbo frames use an MTU of about 9000 bytes to carry more payload per frame; the "
                       "value must match on all devices in the path (NICs and switches) or fragmentation/drops occur.",
            "distractors": {
                "B": "1500 bytes is the standard Ethernet MTU, not a jumbo frame, and MTU must be consistent end-to-end rather than on the server alone.",
                "C": "576 bytes is a minimum IPv4 datagram guideline, far smaller than a jumbo frame.",
                "D": "68 bytes is the IPv4 minimum MTU; it is not a jumbo frame, and setting one device alone creates a mismatch.",
            },
            "exam_pattern": "Jumbo frames ≈ 9000-byte MTU, enabled consistently on all devices in the path.",
        },
    },

    # ===== wireless_standards ===============================================
    {
        "id": "netplus-ni-113", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 1, "type": "mcq",
        "stem": "In the 2.4 GHz band (North America), which set of 20 MHz channels is "
                "non-overlapping and recommended for adjacent access points?",
        "options": [
            {"id": "A", "text": "1, 6, and 11"},
            {"id": "B", "text": "1, 2, and 3"},
            {"id": "C", "text": "36, 40, and 44"},
            {"id": "D", "text": "1, 5, and 9"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In 2.4 GHz, 20 MHz channels overlap, and only channels 1, 6, and 11 do not "
                       "overlap, so they are used for neighboring APs to avoid co-channel interference.",
            "distractors": {
                "B": "Channels 1, 2, and 3 are adjacent and overlap heavily, causing interference.",
                "C": "36, 40, and 44 are 5 GHz channels, not 2.4 GHz.",
                "D": "1, 5, and 9 still overlap; 2.4 GHz channels need five channels of separation, which 1/6/11 provides.",
            },
            "exam_pattern": "2.4 GHz non-overlapping = 1, 6, 11. The 5 GHz band offers many more non-overlapping channels.",
        },
    },
    {
        "id": "netplus-ni-114", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "mcq",
        "stem": "An engineer combines two adjacent 20 MHz Wi-Fi channels into one wider channel "
                "to increase throughput. What is this called, and what width results?",
        "options": [
            {"id": "A", "text": "Channel bonding, producing a 40 MHz channel"},
            {"id": "B", "text": "Band steering, producing a 20 MHz channel"},
            {"id": "C", "text": "MU-MIMO, producing a 160 MHz channel"},
            {"id": "D", "text": "Frequency hopping, producing an 80 MHz channel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Channel bonding joins adjacent channels; two 20 MHz channels bond into 40 MHz "
                       "(further bonding yields 80 and 160 MHz in 5/6 GHz).",
            "distractors": {
                "B": "Band steering nudges dual-band clients toward 5 GHz; it does not widen a channel.",
                "C": "MU-MIMO serves multiple clients using spatial streams; although 160 MHz is a valid bonded width, MU-MIMO is not the bonding mechanism.",
                "D": "Frequency hopping is a legacy spread-spectrum technique, not channel bonding.",
            },
            "exam_pattern": "Channel-bonding widths: 20 → 40 → 80 → 160 MHz. Wider = more throughput but fewer non-overlapping channels.",
        },
    },
    {
        "id": "netplus-ni-115", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 3, "type": "mcq",
        "stem": "An audit requires the WLAN to use the strongest standard personal authentication "
                "available, replacing the older pre-shared-key handshake that is vulnerable to "
                "offline cracking. Which should be deployed?",
        "options": [
            {"id": "A", "text": "WPA3-Personal, which uses SAE (Simultaneous Authentication of Equals)"},
            {"id": "B", "text": "WPA2-Personal with TKIP"},
            {"id": "C", "text": "WEP with a 128-bit key"},
            {"id": "D", "text": "An open network fronted by a captive portal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "WPA3-Personal replaces the WPA2 four-way PSK handshake with SAE, which resists "
                       "offline dictionary/brute-force attacks and adds forward secrecy.",
            "distractors": {
                "B": "The WPA2-Personal PSK handshake is exactly the mechanism susceptible to offline cracking, and TKIP is deprecated.",
                "C": "WEP is cryptographically broken and must never be used.",
                "D": "An open network provides no encryption; a captive portal only gates access, it does not encrypt traffic.",
            },
            "exam_pattern": "WPA3-Personal = SAE (stronger than WPA2-PSK). WPA2/WPA3-Enterprise = 802.1X/RADIUS.",
        },
    },
    {
        "id": "netplus-ni-116", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "mcq",
        "stem": "A company wants each wireless user to authenticate with their own domain "
                "credentials against a RADIUS server instead of a shared Wi-Fi password. Which "
                "mode provides this?",
        "options": [
            {"id": "A", "text": "WPA2/WPA3-Enterprise (802.1X)"},
            {"id": "B", "text": "WPA2-Personal (PSK)"},
            {"id": "C", "text": "WPS push-button"},
            {"id": "D", "text": "MAC address filtering"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Enterprise mode uses 802.1X with a RADIUS server (and EAP) so each user "
                       "authenticates individually rather than sharing one pre-shared key.",
            "distractors": {
                "B": "Personal/PSK mode uses one shared passphrase for everyone — the opposite of per-user credentials.",
                "C": "WPS is a simplified setup method (PIN/push-button) and is considered insecure; it is not per-user authentication.",
                "D": "MAC filtering allows/denies by hardware address, which is easily spoofed and is not credential-based authentication.",
            },
            "exam_pattern": "Per-user wireless login via RADIUS = Enterprise/802.1X; shared passphrase = Personal/PSK.",
        },
    },
    {
        "id": "netplus-ni-117", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "mcq",
        "stem": "A campus deploys 300 access points that must be configured and managed "
                "centrally with coordinated channels and seamless roaming. Which design fits?",
        "options": [
            {"id": "A", "text": "Lightweight APs controlled by a wireless LAN controller (WLC)"},
            {"id": "B", "text": "Autonomous APs each configured individually"},
            {"id": "C", "text": "A single AP with a high-gain omnidirectional antenna"},
            {"id": "D", "text": "A wireless range extender on each floor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Lightweight (thin) APs offload configuration and control to a WLC, giving central "
                       "management, coordinated channel/power, and seamless roaming across hundreds of APs.",
            "distractors": {
                "B": "Autonomous (fat) APs each hold their own configuration and must be managed one by one — impractical at 300 units.",
                "C": "A single AP, however powerful, cannot cover a campus or serve that many clients.",
                "D": "Range extenders repeat an existing signal (roughly halving throughput) and are a SOHO fix, not enterprise central management.",
            },
            "exam_pattern": "Many centrally managed APs = lightweight APs + WLC; standalone self-contained config = autonomous APs.",
        },
    },
    {
        "id": "netplus-ni-118", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "multi",
        "stem": "Compared with the 5 GHz band, which two statements about the 2.4 GHz band are "
                "true? (Choose two.)",
        "options": [
            {"id": "A", "text": "It generally provides longer range and better obstacle penetration"},
            {"id": "B", "text": "It has only three non-overlapping 20 MHz channels (1, 6, 11)"},
            {"id": "C", "text": "It offers more non-overlapping channels than 5 GHz"},
            {"id": "D", "text": "It is immune to interference from microwaves and Bluetooth"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "2.4 GHz propagates farther and penetrates walls better than 5 GHz, but it is "
                       "crowded — only channels 1, 6, and 11 are non-overlapping.",
            "distractors": {
                "C": "5 GHz has many more non-overlapping channels than 2.4 GHz, not fewer.",
                "D": "2.4 GHz is in fact prone to interference from microwaves, Bluetooth, and cordless phones.",
            },
            "exam_pattern": "2.4 GHz = longer range, only 3 non-overlapping channels, more interference; 5 GHz = shorter range, more channels, higher speed.",
        },
    },

    # ===== physical_installations ===========================================
    {
        "id": "netplus-ni-119", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "A data-center run must support 10GBASE-T over copper across the full 100 m "
                "channel. Which cabling category is the minimum that guarantees 10 Gbps at 100 m?",
        "options": [
            {"id": "A", "text": "Cat6a"},
            {"id": "B", "text": "Cat5e"},
            {"id": "C", "text": "Cat6"},
            {"id": "D", "text": "Cat3"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cat6a supports 10GBASE-T to the full 100 m, so it is the minimum category for a "
                       "100 m 10 Gbps copper channel.",
            "distractors": {
                "B": "Cat5e is specified for 1GBASE-T (1 Gbps), not 10GBASE-T.",
                "C": "Cat6 can carry 10G but only to about 55 m (less with alien crosstalk), not the full 100 m.",
                "D": "Cat3 is legacy voice/10BASE-T cabling — far too slow for 10 Gbps.",
            },
            "exam_pattern": "10G copper distances: Cat6 ≈ 55 m, Cat6a = 100 m; Cat5e is 1G only.",
        },
    },
    {
        "id": "netplus-ni-120", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "A carrier link must span 40 km between two cities. Which media and light source "
                "are appropriate?",
        "options": [
            {"id": "A", "text": "Single-mode fiber (SMF) with a laser source"},
            {"id": "B", "text": "Multimode fiber (MMF) with an LED source"},
            {"id": "C", "text": "Cat6a shielded twisted-pair copper"},
            {"id": "D", "text": "Multimode fiber with a larger connector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Single-mode fiber has a very small core carrying one light path from a laser, "
                       "giving the low attenuation and dispersion needed for long-haul links of tens of kilometers.",
            "distractors": {
                "B": "Multimode fiber is for short runs (hundreds of meters); over 40 km modal dispersion makes it unusable.",
                "C": "Copper Ethernet is limited to 100 m — impossible for a 40 km link.",
                "D": "Changing the connector does not overcome multimode's distance limit; the fiber type is the constraint.",
            },
            "exam_pattern": "Long distance = single-mode fiber (laser); short/in-building = multimode fiber (LED/VCSEL).",
        },
    },
    {
        "id": "netplus-ni-121", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "A patch cable is terminated to T568A on one end and T568B on the other. What "
                "kind of cable is this, and what is its traditional use?",
        "options": [
            {"id": "A", "text": "A crossover cable, historically used to connect two like devices (e.g., switch-to-switch) without auto-MDIX"},
            {"id": "B", "text": "A straight-through cable for PC-to-switch connections"},
            {"id": "C", "text": "A rollover (console) cable for a router's console port"},
            {"id": "D", "text": "A loopback plug for testing a single NIC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Different standards on each end (T568A on one, T568B on the other) make a "
                       "crossover cable, which swaps the transmit and receive pairs to join similar devices when auto-MDIX is absent.",
            "distractors": {
                "B": "A straight-through cable uses the SAME standard on both ends (B/B or A/A).",
                "C": "A rollover/console cable reverses all eight conductors for a device's console port; it is not the A/B pin pairing.",
                "D": "A loopback plug jumpers transmit back to receive on one connector; it is not a two-ended crossover cable.",
            },
            "exam_pattern": "Same standard on both ends = straight-through; T568A on one end + T568B on the other = crossover.",
        },
    },
    {
        "id": "netplus-ni-122", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "A switch needs a single-port, hot-swappable optical module supporting 10 Gbps. "
                "Which transceiver form factor fits?",
        "options": [
            {"id": "A", "text": "SFP+"},
            {"id": "B", "text": "SFP"},
            {"id": "C", "text": "QSFP28"},
            {"id": "D", "text": "An RJ45 keystone jack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SFP+ is the enhanced small form-factor pluggable rated for 10 Gbps on a single "
                       "port and is hot-swappable into a switch cage.",
            "distractors": {
                "B": "A standard SFP tops out at about 1 Gbps, not 10 Gbps.",
                "C": "QSFP28 is a quad module for 100 Gbps (4x25G) — more than a single 10G port and a different cage.",
                "D": "An RJ45 keystone is a copper jack, not a pluggable optical transceiver.",
            },
            "exam_pattern": "Transceiver speeds: SFP = 1G, SFP+ = 10G, SFP28 = 25G, QSFP+ = 40G, QSFP28 = 100G.",
        },
    },
    {
        "id": "netplus-ni-123", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "In a multi-floor building, the central equipment room holds the provider demarc "
                "and core switching, and a wiring closet on each floor serves nearby work areas "
                "and connects back to that room. What are these two spaces called, respectively?",
        "options": [
            {"id": "A", "text": "MDF (main distribution frame) and IDF (intermediate distribution frame)"},
            {"id": "B", "text": "IDF (central room) and MDF (per-floor closet)"},
            {"id": "C", "text": "Demarc and smartjack"},
            {"id": "D", "text": "Patch panel and punchdown block"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The central room is the MDF (main distribution frame); each floor's closet is an "
                       "IDF (intermediate distribution frame) that backhauls to the MDF over backbone cabling.",
            "distractors": {
                "B": "The naming is reversed — the central room is the MDF and the floor closets are IDFs.",
                "C": "The demarc is the provider handoff point and a smartjack is a demarc device; neither names the building's distribution frames.",
                "D": "Patch panels and punchdown blocks are components mounted inside the frames, not the rooms themselves.",
            },
            "exam_pattern": "MDF = central main frame; IDF = per-floor/area closet backhauled to the MDF.",
        },
    },
    {
        "id": "netplus-ni-124", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 1, "type": "multi",
        "stem": "A technician is terminating fiber-optic patch cords. Which two connectors are "
                "designed for fiber-optic cabling? (Choose two.)",
        "options": [
            {"id": "A", "text": "LC"},
            {"id": "B", "text": "ST"},
            {"id": "C", "text": "RJ45"},
            {"id": "D", "text": "BNC"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "LC (little/Lucent connector) and ST (straight tip) are both fiber-optic "
                       "connectors; other fiber connectors include SC and MTRJ.",
            "distractors": {
                "C": "RJ45 is the 8P8C modular connector for twisted-pair copper Ethernet, not fiber.",
                "D": "BNC is a bayonet connector used with coaxial cable, not fiber.",
            },
            "exam_pattern": "Fiber connectors: LC, SC, ST, MTRJ. Copper = RJ45; coax = BNC/F-type.",
        },
    },
]
