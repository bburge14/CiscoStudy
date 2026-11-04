"""Authentic CCNA 200-301 item pool (original content, blueprint-aligned).

Each item uses real IOS syntax, real protocol metrics and real `show` output,
and explains why the key is correct, why each distractor is a trap, and the
pattern cue for the real exam. Edit here, then run tools/build_content.py.
"""

QUESTIONS = [
    # ===================== 1.0 NETWORK FUNDAMENTALS =====================
    {
        "id": "ccna-nf-001", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "ipv4_addressing_subnetting", "difficulty": 2, "type": "mcq",
        "stem": "A host is configured with 172.16.20.75/26. Which address is the "
                "broadcast address of the subnet the host belongs to?",
        "options": [
            {"id": "A", "text": "172.16.20.63"},
            {"id": "B", "text": "172.16.20.64"},
            {"id": "C", "text": "172.16.20.127"},
            {"id": "D", "text": "172.16.20.128"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A /26 is a 255.255.255.192 mask, so subnets step by 64 in the "
                       "4th octet: .0, .64, .128, .192. The host .75 falls in the .64 "
                       "subnet (range .64–.127); the broadcast is the last address, .127.",
            "distractors": {
                "A": "172.16.20.63 is the broadcast of the .0 subnet, one block too low.",
                "B": "172.16.20.64 is the network (subnet) address of this block, not the broadcast.",
                "D": "172.16.20.128 is the next subnet's network address.",
            },
            "exam_pattern": "Find the block size (256 − mask octet = 256 − 192 = 64), list "
                            "the subnet boundaries, then the broadcast is one less than the next boundary.",
        },
        "verify_cli": ["show ip interface brief", "show running-config interface g0/1"],
        "references": ["CCNA 200-301 Topic 1.6 IPv4 subnetting"],
        "tags": ["subnetting"],
    },
    {
        "id": "ccna-nf-002", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "ipv4_addressing_subnetting", "difficulty": 2, "type": "fill",
        "stem": "You need subnets with at least 50 usable hosts each, using the fewest "
                "host bits. Enter the prefix length (e.g. 24) you would use.",
        "options": [],
        "correct": ["26", "/26"],
        "explanation": {
            "correct": "6 host bits give 2^6 − 2 = 62 usable hosts (≥50); 5 host bits give "
                       "only 30. 32 − 6 = /26.",
            "distractors": {},
            "exam_pattern": "Usable hosts = 2^(host bits) − 2. Find the smallest host-bit "
                            "count that still covers the requirement, then prefix = 32 − host bits.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 1.6 IPv4 subnetting"],
        "tags": ["subnetting", "vlsm"],
    },
    {
        "id": "ccna-nf-003", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "ipv6_addressing", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about the IPv6 address 2001:0DB8:0000:0000:0000:00AB:0000:1234 "
                "and its correct compressed form is true?",
        "options": [
            {"id": "A", "text": "2001:DB8::AB:0:1234"},
            {"id": "B", "text": "2001:DB8::AB::1234"},
            {"id": "C", "text": "2001:DB8:0:0:0:AB::1234"},
            {"id": "D", "text": "21:DB8::AB:0:1234"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leading zeros in each hextet are dropped and the single longest run "
                       "of all-zero hextets is replaced by one ::. That collapses the three "
                       "0000 hextets to ::, giving 2001:DB8::AB:0:1234.",
            "distractors": {
                "A": "",
                "B": ":: may appear only ONCE in an address; two :: is ambiguous and invalid.",
                "C": "This still shows the zero hextets explicitly AND a :: — you cannot mix "
                     "the two for the same run.",
                "D": "2001 was wrongly shortened to 21; you remove leading zeros per hextet, "
                     "not digits across the address.",
            },
            "exam_pattern": "Only one :: allowed, and it replaces the LONGEST zero run. Watch "
                            "for answers with two :: or with digits (not leading zeros) removed.",
        },
        "verify_cli": ["show ipv6 interface brief"],
        "references": ["CCNA 200-301 Topic 1.8 IPv6 address types"],
        "tags": ["ipv6"],
    },
    {
        "id": "ccna-nf-004", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "ipv6_addressing", "difficulty": 2, "type": "mcq",
        "stem": "An interface has MAC address 00:1A:2B:3C:4D:5E and derives its interface ID "
                "with EUI-64. What is the resulting 64-bit interface ID?",
        "options": [
            {"id": "A", "text": "021A:2BFF:FE3C:4D5E"},
            {"id": "B", "text": "001A:2BFF:FE3C:4D5E"},
            {"id": "C", "text": "021A:2BFE:FF3C:4D5E"},
            {"id": "D", "text": "001A:2BFF:FF3C:4D5E"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EUI-64 inserts FFFE in the middle of the MAC and flips the 7th bit "
                       "(U/L bit) of the first byte. 00 (0000 0000) becomes 02 (0000 0010), "
                       "then 001A2B + FFFE + 3C4D5E → 021A:2BFF:FE3C:4D5E.",
            "distractors": {
                "A": "",
                "B": "The U/L bit was not flipped; 00 must become 02.",
                "C": "The inserted value must be FFFE, not FFFE split as FE/FF, and the 7th "
                     "bit flip is on the first byte only.",
                "D": "FFFF was inserted instead of FFFE.",
            },
            "exam_pattern": "EUI-64 = split MAC, insert FFFE, flip the 7th bit of byte 1. The "
                            "flip usually turns 00→02; answers that skip the flip are traps.",
        },
        "verify_cli": ["show ipv6 interface g0/0"],
        "references": ["CCNA 200-301 Topic 1.9 IPv6 (EUI-64)"],
        "tags": ["ipv6", "eui-64"],
    },
    {
        "id": "ccna-nf-005", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "tcp_udp", "difficulty": 1, "type": "multi", "select_count": 2,
        "stem": "Which TWO protocols/applications rely on UDP for transport by default?",
        "options": [
            {"id": "A", "text": "TFTP"},
            {"id": "B", "text": "HTTP"},
            {"id": "C", "text": "SNMP"},
            {"id": "D", "text": "FTP (control)"},
            {"id": "E", "text": "Telnet"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "TFTP (UDP/69) and SNMP (UDP/161,162) are UDP-based — lightweight, no "
                       "connection setup. FTP, HTTP and Telnet all use TCP for reliability.",
            "distractors": {
                "B": "HTTP uses TCP/80 — reliable, ordered delivery for web traffic.",
                "D": "FTP uses TCP/21 (control) and TCP/20 (data).",
                "E": "Telnet uses TCP/23.",
            },
            "exam_pattern": "Remember the small UDP club: DNS(53 usually), DHCP(67/68), "
                            "TFTP(69), SNMP(161/162), NTP(123), syslog(514), plus voice/video (RTP).",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 1.5 TCP vs UDP"],
        "tags": ["ports", "transport"],
    },
    {
        "id": "ccna-nf-006", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "switching_concepts", "difficulty": 2, "type": "mcq",
        "stem": "A frame arrives on a switch for a destination MAC that is NOT in the MAC "
                "address table. What does the switch do?",
        "options": [
            {"id": "A", "text": "Drops the frame and sends an ICMP unreachable"},
            {"id": "B", "text": "Floods the frame out all ports in the VLAN except the ingress port"},
            {"id": "C", "text": "Floods the frame out every port including the ingress port"},
            {"id": "D", "text": "Forwards the frame to the default gateway"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An unknown unicast is flooded out all ports in the same VLAN except "
                       "the port it arrived on. When the real host replies, the switch learns "
                       "its MAC and future frames are forwarded, not flooded.",
            "distractors": {
                "A": "Switches do not generate ICMP for Layer 2 forwarding; that is a router behaviour.",
                "C": "The ingress port is always excluded from flooding (split-horizon of flooding).",
                "D": "Layer 2 switches do not consult a gateway; that is Layer 3 routing.",
            },
            "exam_pattern": "Unknown unicast, broadcast and multicast are flooded within the "
                            "VLAN, never out the ingress port. Learning is based on SOURCE MAC.",
        },
        "verify_cli": ["show mac address-table", "show mac address-table dynamic"],
        "references": ["CCNA 200-301 Topic 1.1 switching"],
        "tags": ["switching", "flooding"],
    },
    {
        "id": "ccna-nf-007", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "osi_tcpip", "difficulty": 1, "type": "mcq",
        "stem": "As data is encapsulated for transmission, in which order are the PDUs created "
                "moving DOWN the TCP/IP stack from the application?",
        "options": [
            {"id": "A", "text": "Segment → Packet → Frame → Bits"},
            {"id": "B", "text": "Packet → Segment → Frame → Bits"},
            {"id": "C", "text": "Frame → Packet → Segment → Bits"},
            {"id": "D", "text": "Bits → Frame → Packet → Segment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Transport adds the L4 header (Segment), the network layer adds the IP "
                       "header (Packet), the data-link layer adds the frame header/trailer "
                       "(Frame), and the physical layer transmits Bits.",
            "distractors": {
                "A": "",
                "B": "Segmentation (L4) happens before the packet (L3) header is added.",
                "C": "This is reversed — framing is not first on the way down.",
                "D": "This is the de-encapsulation (receive) order, moving up the stack.",
            },
            "exam_pattern": "Down the stack = Segment, Packet, Frame, Bits (SPFB). Up the stack "
                            "reverses it. Watch whether the question asks about sending or receiving.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 1.2 encapsulation"],
        "tags": ["osi", "encapsulation"],
    },
    {
        "id": "ccna-nf-008", "exam": "ccna", "domain": "network_fundamentals",
        "subtopic": "cabling_media", "difficulty": 1, "type": "mcq",
        "stem": "You are directly connecting two Cisco switches that do NOT support "
                "Auto-MDIX. Which cable is required between their FastEthernet ports?",
        "options": [
            {"id": "A", "text": "Straight-through (TIA-568B on both ends)"},
            {"id": "B", "text": "Crossover (568B on one end, 568A on the other)"},
            {"id": "C", "text": "Rollover (console) cable"},
            {"id": "D", "text": "Coaxial cable"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Switch-to-switch is a 'like device' connection, which requires a "
                       "crossover cable when Auto-MDIX is unavailable, so TX on one side maps "
                       "to RX on the other.",
            "distractors": {
                "A": "Straight-through is for unlike devices (switch↔router, switch↔PC).",
                "C": "Rollover cables connect a PC's serial/USB to a device console port.",
                "D": "Coax is not used for modern switched Ethernet access links.",
            },
            "exam_pattern": "Like devices (switch-switch, router-router, PC-PC, PC-router) → "
                            "crossover. Unlike devices → straight-through. Auto-MDIX makes it moot if enabled.",
        },
        "verify_cli": ["show interfaces status"],
        "references": ["CCNA 200-301 Topic 1.3 cabling"],
        "tags": ["cabling"],
    },

    # ===================== 2.0 NETWORK ACCESS =====================
    {
        "id": "ccna-na-001", "exam": "ccna", "domain": "network_access",
        "subtopic": "stp_root_election", "difficulty": 2, "type": "mcq",
        "stem": "Four switches run Rapid-PVST+ for VLAN 10. Their VLAN 10 bridge priorities "
                "and MAC addresses are shown. Which switch becomes the root bridge?",
        "exhibit": "SW-A  priority 32768  MAC 0012.3f00.aa00\n"
                   "SW-B  priority 32768  MAC 0012.3f00.0b00\n"
                   "SW-C  priority 24576  MAC 0012.3f00.cc00\n"
                   "SW-D  priority 28672  MAC 0012.3f00.0d00",
        "options": [
            {"id": "A", "text": "SW-A"},
            {"id": "B", "text": "SW-B (lowest MAC)"},
            {"id": "C", "text": "SW-C"},
            {"id": "D", "text": "SW-D"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The root is the lowest Bridge ID = priority (incl. the VLAN sys-id-ext) "
                       "THEN MAC as tiebreaker. SW-C has the lowest priority (24576), so it wins "
                       "outright — MAC is never consulted because priority already decides it.",
            "distractors": {
                "A": "SW-A uses the default 32768, higher than SW-C and SW-D.",
                "B": "Lowest MAC only breaks a tie when priorities are EQUAL. SW-C's lower "
                     "priority settles it before MAC matters.",
                "D": "SW-D's 28672 is lower than the defaults but still higher than SW-C's 24576.",
            },
            "exam_pattern": "Compare priority FIRST (lower wins); only if two match do you fall "
                            "to the lower MAC. The classic trap dangles a tiny MAC to lure you "
                            "past a lower-priority switch.",
        },
        "verify_cli": ["show spanning-tree vlan 10", "show spanning-tree root"],
        "references": ["CCNA 200-301 Topic 2.5 STP"],
        "tags": ["stp", "root-bridge"],
    },
    {
        "id": "ccna-na-002", "exam": "ccna", "domain": "network_access",
        "subtopic": "stp_root_election", "difficulty": 2, "type": "mcq",
        "stem": "You run 'spanning-tree vlan 1 root primary' on a switch where the current "
                "root has priority 32769 (32768 + VLAN 1). What priority does the local "
                "switch set for VLAN 1?",
        "options": [
            {"id": "A", "text": "0"},
            {"id": "B", "text": "4096"},
            {"id": "C", "text": "24576"},
            {"id": "D", "text": "28672"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The 'root primary' macro sets priority to 24576 when the existing root's "
                       "priority is greater than 24576. (If the current root were already ≤24576, "
                       "it would instead set 4096 below that root.)",
            "distractors": {
                "A": "0 is a valid manual priority but not what the macro chooses here.",
                "B": "4096 is the step size and what 'root primary' would pick only if the "
                     "current root were already at/below 24576.",
                "D": "28672 is what 'root secondary' configures.",
            },
            "exam_pattern": "root primary → 24576 (or 4096 under the current root if it's already "
                            "low). root secondary → 28672. These are macros, not fixed priorities.",
        },
        "verify_cli": ["show spanning-tree vlan 1", "show run | include priority"],
        "references": ["CCNA 200-301 Topic 2.5 STP"],
        "tags": ["stp", "root-primary"],
    },
    {
        "id": "ccna-na-003", "exam": "ccna", "domain": "network_access",
        "subtopic": "etherchannel", "difficulty": 3, "type": "mcq",
        "stem": "SW1 ports are set to 'channel-group 1 mode desirable'. SW2's matching ports "
                "are set to 'channel-group 1 mode auto'. What is the result?",
        "options": [
            {"id": "A", "text": "The channel forms using LACP"},
            {"id": "B", "text": "The channel forms using PAgP"},
            {"id": "C", "text": "The channel does not form; both sides are passive"},
            {"id": "D", "text": "The channel does not form; mismatched protocols"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "desirable and auto are PAgP modes. desirable actively initiates PAgP; "
                       "auto responds but does not initiate. desirable/auto forms a PAgP channel "
                       "because at least one side (desirable) initiates.",
            "distractors": {
                "A": "LACP uses active/passive, not desirable/auto. desirable/auto is PAgP.",
                "B": "",
                "C": "auto/auto would fail (neither initiates), but desirable DOES initiate.",
                "D": "Both sides are PAgP here, so there is no protocol mismatch.",
            },
            "exam_pattern": "PAgP = desirable/auto; LACP = active/passive. The only non-forming "
                            "same-protocol combos are auto/auto and passive/passive (nobody "
                            "initiates). 'on' only works with 'on'.",
        },
        "verify_cli": ["show etherchannel summary", "show etherchannel 1 port-channel"],
        "references": ["CCNA 200-301 Topic 2.4 EtherChannel"],
        "tags": ["etherchannel", "pagp"],
    },
    {
        "id": "ccna-na-004", "exam": "ccna", "domain": "network_access",
        "subtopic": "etherchannel", "difficulty": 2, "type": "mcq",
        "stem": "Which EtherChannel mode combination will FAIL to form a bundle?",
        "options": [
            {"id": "A", "text": "active / passive"},
            {"id": "B", "text": "active / active"},
            {"id": "C", "text": "passive / passive"},
            {"id": "D", "text": "on / on"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "passive/passive fails because LACP passive only responds to LACP "
                       "packets — neither side sends the first LACP frame, so negotiation never starts.",
            "distractors": {
                "A": "active/passive works: active initiates, passive responds.",
                "B": "active/active works: both initiate LACP.",
                "D": "on/on forms a static channel with no negotiation at all.",
            },
            "exam_pattern": "The two 'dead' pairs are passive/passive (LACP) and auto/auto "
                            "(PAgP). Also remember 'on' must pair only with 'on' — on/active "
                            "or on/desirable fail.",
        },
        "verify_cli": ["show etherchannel summary"],
        "references": ["CCNA 200-301 Topic 2.4 EtherChannel"],
        "tags": ["etherchannel", "lacp"],
    },
    {
        "id": "ccna-na-005", "exam": "ccna", "domain": "network_access",
        "subtopic": "vlans_trunking", "difficulty": 2, "type": "mcq",
        "stem": "A trunk between SW1 (native VLAN 1) and SW2 (native VLAN 99) logs "
                "%CDP-4-NATIVE_VLAN_MISMATCH. Which statement is correct?",
        "options": [
            {"id": "A", "text": "Traffic in the native VLAN of each switch can leak between VLANs 1 and 99"},
            {"id": "B", "text": "The trunk is administratively shut down automatically"},
            {"id": "C", "text": "All tagged VLAN traffic stops crossing the trunk"},
            {"id": "D", "text": "The mismatch has no effect because native VLAN traffic is tagged"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Each switch sends its native VLAN untagged and assumes untagged frames "
                       "belong to its own native VLAN. With a mismatch, SW1's VLAN 1 untagged "
                       "frames land in SW2's VLAN 99 — a security/bridging problem (VLAN hopping risk).",
            "distractors": {
                "A": "",
                "B": "The trunk stays up; only a log message is generated (CDP detects it).",
                "C": "Tagged VLANs still cross fine; only the untagged native VLAN is affected.",
                "D": "The native VLAN is UNtagged by default — that is exactly why the mismatch matters.",
            },
            "exam_pattern": "Native VLAN mismatch = untagged frames cross into the wrong VLAN, "
                            "flagged by CDP, trunk stays up. Fix by matching native VLANs on both ends.",
        },
        "verify_cli": ["show interfaces trunk", "show interfaces g0/1 switchport"],
        "references": ["CCNA 200-301 Topic 2.1/2.2 VLANs and trunking"],
        "tags": ["vlan", "trunk", "native-vlan"],
    },
    {
        "id": "ccna-na-006", "exam": "ccna", "domain": "network_access",
        "subtopic": "vlans_trunking", "difficulty": 2, "type": "mcq",
        "stem": "Two switches both default their ports to 'switchport mode dynamic auto'. "
                "What will the link between them become?",
        "options": [
            {"id": "A", "text": "A trunk, via DTP negotiation"},
            {"id": "B", "text": "An access port in VLAN 1"},
            {"id": "C", "text": "An 802.1Q trunk only if encapsulation is set to negotiate"},
            {"id": "D", "text": "A routed port"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "dynamic auto only trunks if the other side actively asks (dynamic "
                       "desirable or trunk). auto/auto means neither side initiates DTP, so the "
                       "link stays an access port in VLAN 1.",
            "distractors": {
                "A": "DTP needs at least one 'desirable' or 'trunk' side to form a trunk; "
                     "auto/auto does not negotiate up.",
                "C": "Encapsulation choice is irrelevant when no trunk is negotiated at all.",
                "D": "Switchports do not auto-become routed ports; that requires 'no switchport'.",
            },
            "exam_pattern": "DTP table: auto/auto and (auto or access)/access stay access; "
                            "desirable or trunk on one side pulls auto up to a trunk. Best "
                            "practice is to hard-set mode and 'switchport nonegotiate'.",
        },
        "verify_cli": ["show interfaces trunk", "show dtp interface g0/1"],
        "references": ["CCNA 200-301 Topic 2.2 trunking/DTP"],
        "tags": ["vlan", "dtp"],
    },
    {
        "id": "ccna-na-007", "exam": "ccna", "domain": "network_access",
        "subtopic": "stp_root_election", "difficulty": 2, "type": "mcq",
        "stem": "On a non-root switch running Rapid-PVST+, which port role is placed in the "
                "forwarding state and is the single best path toward the root bridge?",
        "options": [
            {"id": "A", "text": "Designated port"},
            {"id": "B", "text": "Root port"},
            {"id": "C", "text": "Alternate port"},
            {"id": "D", "text": "Backup port"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The root port is the one port on a non-root bridge with the lowest cost "
                       "to the root; it forwards and is the upstream path to the root.",
            "distractors": {
                "A": "Designated ports forward too, but they face AWAY from the root on each "
                     "segment (one per segment), not toward it.",
                "C": "An alternate port is a blocked backup to the ROOT port (an alternate path "
                     "to the root); it does not forward unless the root port fails.",
                "D": "A backup port is a blocked backup for a DESIGNATED port on the same "
                     "segment (seen with hubs); it does not forward.",
            },
            "exam_pattern": "Root port = best path TOWARD root (one per non-root switch). "
                            "Designated = best path on a segment AWAY from root. Alternate/Backup "
                            "= blocked (RSTP terms).",
        },
        "verify_cli": ["show spanning-tree vlan 1", "show spanning-tree interface g0/1 detail"],
        "references": ["CCNA 200-301 Topic 2.5 STP port roles"],
        "tags": ["stp", "port-roles"],
    },
    {
        "id": "ccna-na-008", "exam": "ccna", "domain": "network_access",
        "subtopic": "wlan_architecture", "difficulty": 2, "type": "mcq",
        "stem": "In a split-MAC (lightweight AP + WLC) deployment, which protocol tunnels "
                "both control and data traffic between a lightweight AP and the WLC?",
        "options": [
            {"id": "A", "text": "CAPWAP"},
            {"id": "B", "text": "LWAPP only"},
            {"id": "C", "text": "GRE without encryption"},
            {"id": "D", "text": "802.1Q"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CAPWAP builds two tunnels between the AP and WLC: a control tunnel "
                       "(UDP 5246, encrypted via DTLS) and a data tunnel (UDP 5247). It is the "
                       "modern standard that replaced the older LWAPP.",
            "distractors": {
                "A": "",
                "B": "LWAPP is the legacy predecessor; CAPWAP superseded it (RFC 5415).",
                "C": "GRE is not the AP-to-WLC tunneling protocol in split-MAC designs.",
                "D": "802.1Q is VLAN tagging on wired trunks, not an AP-to-WLC tunnel.",
            },
            "exam_pattern": "CAPWAP ports: 5246 control (DTLS encrypted), 5247 data. Split-MAC "
                            "means the AP does real-time 802.11, the WLC does management/auth.",
        },
        "verify_cli": ["show capwap client rcb", "show ap join stats"],
        "references": ["CCNA 200-301 Topic 2.7/2.8 WLAN architecture"],
        "tags": ["wireless", "capwap"],
    },
    {
        "id": "ccna-na-009", "exam": "ccna", "domain": "network_access",
        "subtopic": "cdp_lldp", "difficulty": 1, "type": "multi", "select_count": 2,
        "stem": "Which TWO statements correctly distinguish LLDP from CDP?",
        "options": [
            {"id": "A", "text": "LLDP is an IEEE (802.1AB) open standard; CDP is Cisco-proprietary"},
            {"id": "B", "text": "CDP is enabled globally by default on Cisco devices; LLDP is disabled by default"},
            {"id": "C", "text": "LLDP cannot discover non-Cisco neighbors"},
            {"id": "D", "text": "CDP uses TCP port 179 to exchange information"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "LLDP (IEEE 802.1AB) is vendor-neutral, useful in multivendor networks; "
                       "CDP is Cisco-proprietary and is ON by default, while LLDP must be enabled "
                       "with 'lldp run'.",
            "distractors": {
                "C": "LLDP's whole purpose is multivendor discovery — it DOES see non-Cisco devices.",
                "D": "Both CDP and LLDP are Layer 2 protocols; they do not use TCP/179 (that's BGP).",
            },
            "exam_pattern": "CDP = Cisco, on by default, L2. LLDP = open standard (802.1AB), off "
                            "by default ('lldp run'), L2. Default CDP timers: 60s hello, 180s hold.",
        },
        "verify_cli": ["show cdp neighbors", "show lldp neighbors", "show cdp"],
        "references": ["CCNA 200-301 Topic 2.3 discovery protocols"],
        "tags": ["cdp", "lldp"],
    },
    {
        "id": "ccna-na-010", "exam": "ccna", "domain": "network_access",
        "subtopic": "vlans_trunking", "difficulty": 2, "type": "fill",
        "stem": "On interface Gi0/1 you must allow ONLY VLANs 10, 20, and 30 across the trunk "
                "(replacing the default allowed list). Enter the exact interface command.",
        "options": [],
        "correct": [
            "switchport trunk allowed vlan 10,20,30",
            "switchport trunk allowed vlan 10,20,30 ",
        ],
        "explanation": {
            "correct": "'switchport trunk allowed vlan 10,20,30' sets the allowed list to "
                       "exactly those VLANs. Use the 'add' keyword later to append without "
                       "overwriting the list.",
            "distractors": {},
            "exam_pattern": "Without 'add', the command REPLACES the whole allowed list — a "
                            "classic outage trap when you forget 'add' and knock off every other VLAN.",
        },
        "verify_cli": ["show interfaces trunk", "show running-config interface g0/1"],
        "references": ["CCNA 200-301 Topic 2.2 trunking"],
        "tags": ["vlan", "trunk", "allowed-vlan"],
    },

    # ===================== 3.0 IP CONNECTIVITY =====================
    {
        "id": "ccna-ic-001", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "ospf", "difficulty": 3, "type": "mcq",
        "stem": "Two OSPF routers on an Ethernet segment are stuck with their neighbor in the "
                "2-WAY state and never reach FULL. Which explanation is MOST likely correct?",
        "options": [
            {"id": "A", "text": "This is normal between two DROTHER routers on a broadcast segment"},
            {"id": "B", "text": "There is an OSPF area mismatch on the link"},
            {"id": "C", "text": "The MTU values do not match on the two interfaces"},
            {"id": "D", "text": "The OSPF process IDs do not match between the routers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On a broadcast network, DROTHER routers intentionally stay in 2-WAY "
                       "with each other — they only go FULL with the DR and BDR. 2-WAY between "
                       "two DROTHERs is expected, not a fault.",
            "distractors": {
                "A": "",
                "B": "An area mismatch prevents the adjacency from forming at all (stuck in "
                     "INIT/EXSTART or no neighbor), not a clean 2-WAY.",
                "C": "An MTU mismatch sticks the neighbor in EXSTART/EXCHANGE, not 2-WAY.",
                "D": "OSPF process IDs are locally significant and do NOT need to match between neighbors.",
            },
            "exam_pattern": "Map the stuck state to the cause: INIT=one-way hello; 2-WAY=normal "
                            "DROTHER-DROTHER; EXSTART/EXCHANGE=MTU mismatch; stuck forming=hello/dead, "
                            "area, subnet, or auth mismatch.",
        },
        "verify_cli": ["show ip ospf neighbor", "show ip ospf interface g0/0"],
        "references": ["CCNA 200-301 Topic 3.4 OSPF neighbor states"],
        "tags": ["ospf", "neighbor-states", "dr-bdr"],
    },
    {
        "id": "ccna-ic-002", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "ospf", "difficulty": 3, "type": "mcq",
        "stem": "Review the output. Why is the OSPF adjacency not reaching FULL?",
        "exhibit": "R2# show ip ospf neighbor\n"
                   "Neighbor ID     Pri   State      Dead Time   Address      Interface\n"
                   "10.1.1.1          1   EXSTART/DR 00:00:33    10.0.12.1    GigabitEthernet0/0",
        "options": [
            {"id": "A", "text": "The routers have mismatched OSPF hello/dead timers"},
            {"id": "B", "text": "The interface MTU differs between the two routers"},
            {"id": "C", "text": "The two routers are in different OSPF areas"},
            {"id": "D", "text": "Authentication keys do not match"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A neighbor stuck in EXSTART/EXCHANGE that never advances to FULL is the "
                       "textbook symptom of an MTU mismatch: the DBD packets are exchanged but "
                       "the larger-MTU side's DBD is dropped, so the exchange loops.",
            "distractors": {
                "B": "",
                "A": "Mismatched hello/dead timers stop the neighbor from forming at all — you "
                     "would not even see it reach EXSTART.",
                "C": "An area mismatch likewise prevents neighborship; the neighbor would not appear.",
                "D": "Auth mismatch prevents the adjacency from forming (no neighbor), not an "
                     "EXSTART hang.",
            },
            "exam_pattern": "EXSTART/EXCHANGE + 'stuck' = MTU mismatch. Verify with 'show ip "
                            "ospf interface' (look at the MTU) and fix with 'mtu'/'ip mtu' or "
                            "'ip ospf mtu-ignore' as a workaround.",
        },
        "verify_cli": ["show ip ospf interface g0/0", "show interfaces g0/0 | include MTU"],
        "references": ["CCNA 200-301 Topic 3.4 OSPF troubleshooting"],
        "tags": ["ospf", "mtu", "exstart"],
    },
    {
        "id": "ccna-ic-003", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "wildcard_masks", "difficulty": 3, "type": "fill",
        "stem": "You must write a single OSPF network statement that matches ONLY the subnet "
                "192.168.8.0/22 (the whole /22). Enter the wildcard mask to use after "
                "'network 192.168.8.0'.",
        "options": [],
        "correct": ["0.0.3.255"],
        "explanation": {
            "correct": "A /22 mask is 255.255.252.0. The wildcard is the inverse: "
                       "255.255.255.255 − 255.255.252.0 = 0.0.3.255. So 'network 192.168.8.0 "
                       "0.0.3.255 area 0'.",
            "distractors": {},
            "exam_pattern": "Wildcard = inverse of the subnet mask (255 − each octet). /22 → "
                            "252 in the 3rd octet → wildcard 3 there. The trap is writing "
                            "0.0.255.255 (/16) or 0.0.0.255 (/24) instead of 0.0.3.255.",
        },
        "verify_cli": ["show ip ospf interface brief", "show ip protocols"],
        "references": ["CCNA 200-301 Topic 3.4 wildcard masks"],
        "tags": ["wildcard", "ospf"],
    },
    {
        "id": "ccna-ic-004", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "wildcard_masks", "difficulty": 2, "type": "mcq",
        "stem": "Which wildcard mask, used with 'access-list 10 permit 10.1.0.0 <wildcard>', "
                "matches every host in 10.1.0.0 through 10.1.3.255 and NO other addresses?",
        "options": [
            {"id": "A", "text": "0.0.3.255"},
            {"id": "B", "text": "0.0.255.255"},
            {"id": "C", "text": "0.0.0.255"},
            {"id": "D", "text": "255.255.252.0"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "10.1.0.0–10.1.3.255 is a /22 (four /24 blocks: .0,.1,.2,.3). The /22 "
                       "wildcard is 0.0.3.255 — the low two bits of the third octet are 'don't care'.",
            "distractors": {
                "A": "",
                "B": "0.0.255.255 matches 10.1.0.0–10.1.255.255 (a /16) — far too broad.",
                "C": "0.0.0.255 matches only 10.1.0.0–10.1.0.255 (a single /24).",
                "D": "255.255.252.0 is a subnet MASK, not a wildcard — it is backwards.",
            },
            "exam_pattern": "Range size 4 in the third octet → wildcard 3 there. Beware answers "
                            "that hand you the subnet mask (contiguous 1s then 0s) instead of the "
                            "wildcard (0s then 1s).",
        },
        "verify_cli": ["show access-lists 10", "show ip access-lists"],
        "references": ["CCNA 200-301 Topic 5.1 ACL wildcards"],
        "tags": ["wildcard", "acl"],
    },
    {
        "id": "ccna-ic-005", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "routing_table", "difficulty": 2, "type": "mcq",
        "stem": "A router has these routes to 10.1.1.50: an OSPF route 10.1.1.0/24, a static "
                "route 10.1.1.0/25, and an EIGRP route 10.1.1.48/29. Which is used to forward "
                "the packet to 10.1.1.50?",
        "options": [
            {"id": "A", "text": "The OSPF /24 route (lowest administrative distance among IGPs)"},
            {"id": "B", "text": "The static /25 route (lowest administrative distance)"},
            {"id": "C", "text": "The EIGRP /29 route (longest prefix match)"},
            {"id": "D", "text": "It load-balances across all three"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The routing table chooses the LONGEST PREFIX MATCH first. 10.1.1.48/29 "
                       "(covers .48–.55) is the most specific route containing .50, so it wins "
                       "regardless of administrative distance.",
            "distractors": {
                "A": "AD only breaks ties between routes to the SAME prefix; it is not consulted "
                     "when prefixes differ in length.",
                "B": "Static has the lowest AD, but AD is irrelevant here because the prefixes differ.",
                "C": "",
                "D": "Load-balancing happens only across equal-cost routes to the same prefix.",
            },
            "exam_pattern": "Order of operations: (1) longest prefix match, then (2) AD to break "
                            "ties for identical prefixes, then (3) metric within the same protocol.",
        },
        "verify_cli": ["show ip route 10.1.1.50", "show ip route longer-prefixes"],
        "references": ["CCNA 200-301 Topic 3.1 routing decisions"],
        "tags": ["routing", "longest-prefix", "administrative-distance"],
    },
    {
        "id": "ccna-ic-006", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "static_routing", "difficulty": 2, "type": "mcq",
        "stem": "You want a backup default route via 203.0.113.2 that is used ONLY if the "
                "OSPF-learned default route (AD 110) disappears. Which command creates it?",
        "options": [
            {"id": "A", "text": "ip route 0.0.0.0 0.0.0.0 203.0.113.2 120"},
            {"id": "B", "text": "ip route 0.0.0.0 0.0.0.0 203.0.113.2 90"},
            {"id": "C", "text": "ip route 0.0.0.0 0.0.0.0 203.0.113.2"},
            {"id": "D", "text": "ip route 0.0.0.0 0.0.0.0 203.0.113.2 1 permanent"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A floating static route needs an AD HIGHER than the protocol it backs "
                       "up. OSPF is AD 110, so 120 keeps the static out of the table until the "
                       "OSPF route is gone.",
            "distractors": {
                "A": "",
                "B": "AD 90 is lower than OSPF's 110, so this static would WIN and be used all "
                     "the time — not a backup.",
                "C": "No AD means the default AD of 1, which beats OSPF and is always active.",
                "D": "AD 1 (even with 'permanent') also beats OSPF and would be used immediately.",
            },
            "exam_pattern": "Floating static = set AD ABOVE the primary source's AD. Know the "
                            "defaults: connected 0, static 1, EIGRP 90, OSPF 110, RIP 120.",
        },
        "verify_cli": ["show ip route static", "show ip route 0.0.0.0"],
        "references": ["CCNA 200-301 Topic 3.1/3.3 static routing"],
        "tags": ["static", "floating-static", "administrative-distance"],
    },
    {
        "id": "ccna-ic-007", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "ospf", "difficulty": 2, "type": "mcq",
        "stem": "How does an OSPFv2 router choose its router-id if no 'router-id' command is "
                "configured and OSPF is started after interfaces are up?",
        "options": [
            {"id": "A", "text": "Highest IP address on any active loopback; otherwise highest IP on any active interface"},
            {"id": "B", "text": "Lowest IP address on any active interface"},
            {"id": "C", "text": "The MAC address of the first interface"},
            {"id": "D", "text": "Always 0.0.0.0 until manually set"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RID selection order: (1) explicit 'router-id', (2) highest IP on an "
                       "up loopback, (3) highest IP on any up physical interface. Loopbacks win "
                       "because they are stable.",
            "distractors": {
                "A": "",
                "B": "OSPF uses the HIGHEST interface IP, not the lowest.",
                "C": "OSPF RIDs are 32-bit values in dotted-decimal, derived from IPs, not MACs.",
                "D": "A RID is always chosen at process start if addresses exist; it is not left at 0.",
            },
            "exam_pattern": "router-id > highest loopback > highest active interface. Changing it "
                            "later needs 'clear ip ospf process' to take effect.",
        },
        "verify_cli": ["show ip ospf", "show ip protocols"],
        "references": ["CCNA 200-301 Topic 3.4 OSPF router-id"],
        "tags": ["ospf", "router-id"],
    },
    {
        "id": "ccna-ic-008", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "fhrp", "difficulty": 2, "type": "mcq",
        "stem": "Two routers run HSRPv2 for gateway 10.0.0.1. R1 has priority 110 with "
                "preempt; R2 has priority 100. R1 reloads, R2 becomes active, then R1 comes "
                "back. What happens?",
        "options": [
            {"id": "A", "text": "R1 becomes active again because preempt is configured"},
            {"id": "B", "text": "R2 stays active; R1 becomes standby because it lacks preempt"},
            {"id": "C", "text": "Both routers become active, causing a conflict"},
            {"id": "D", "text": "The virtual IP changes to R2's physical address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Preempt lets a higher-priority router reclaim the active role when it "
                       "returns. R1 (110, preempt) will take the active role back from R2 (100).",
            "distractors": {
                "A": "",
                "B": "Without preempt R1 would stay standby — but R1 DOES have preempt here, so "
                     "it reclaims active.",
                "C": "HSRP elects exactly one active router; there is no dual-active in normal operation.",
                "D": "The virtual IP and virtual MAC (0000.0c07.acXX) are owned by whichever "
                     "router is active; they do not change to a physical address.",
            },
            "exam_pattern": "Higher HSRP priority + preempt = reclaims active. No preempt = the "
                            "incumbent keeps active even if a higher-priority router returns. "
                            "HSRPv2 vMAC = 0000.0C9F.FXXX.",
        },
        "verify_cli": ["show standby brief", "show standby"],
        "references": ["CCNA 200-301 Topic 3.5 FHRP/HSRP"],
        "tags": ["hsrp", "fhrp", "preempt"],
    },
    {
        "id": "ccna-ic-009", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "ospf", "difficulty": 2, "type": "fill",
        "stem": "On a 1 Gbps interface with the default OSPF reference bandwidth (100 Mbps), "
                "what is the OSPF cost of the interface? Enter the number.",
        "options": [],
        "correct": ["1"],
        "explanation": {
            "correct": "OSPF cost = reference bandwidth / interface bandwidth = 100 Mbps / 1000 "
                       "Mbps = 0.1, rounded UP to a minimum of 1. So Gigabit, 10 Gig, etc. all "
                       "show cost 1 by default — which is why you raise the reference bandwidth.",
            "distractors": {},
            "exam_pattern": "Default reference = 10^8 (100 Mbps). FastEthernet=1, Gig=1, "
                            "10Gig=1 (all floor to 1) — the reason to set "
                            "'auto-cost reference-bandwidth' consistently network-wide.",
        },
        "verify_cli": ["show ip ospf interface g0/0", "show ip ospf"],
        "references": ["CCNA 200-301 Topic 3.4 OSPF cost"],
        "tags": ["ospf", "cost", "reference-bandwidth"],
    },
    {
        "id": "ccna-ic-010", "exam": "ccna", "domain": "ip_connectivity",
        "subtopic": "ospf", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "Which TWO parameters MUST match for two OSPFv2 routers to form a neighbor "
                "adjacency on a link?",
        "options": [
            {"id": "A", "text": "Hello and dead timers"},
            {"id": "B", "text": "OSPF area ID on the link"},
            {"id": "C", "text": "OSPF process ID"},
            {"id": "D", "text": "Router IDs"},
            {"id": "E", "text": "Interface bandwidth"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "To become neighbors, routers must agree on hello/dead timers and be in "
                       "the same area (also same subnet/mask, matching auth, matching stub flags, "
                       "and compatible MTU to go FULL).",
            "distractors": {
                "C": "Process IDs are locally significant — they can differ freely.",
                "D": "Router IDs must be UNIQUE, not matching; duplicate RIDs break OSPF.",
                "E": "Bandwidth affects cost/metric, not whether an adjacency forms.",
            },
            "exam_pattern": "Must-match for adjacency: area, hello/dead, subnet+mask, auth, "
                            "stub flag, MTU (for FULL). Must DIFFER: router-id. Don't-care: process ID.",
        },
        "verify_cli": ["show ip ospf neighbor", "show ip ospf interface g0/0"],
        "references": ["CCNA 200-301 Topic 3.4 OSPF adjacency requirements"],
        "tags": ["ospf", "adjacency"],
    },

    # ===================== 4.0 IP SERVICES =====================
    {
        "id": "ccna-is-001", "exam": "ccna", "domain": "ip_services",
        "subtopic": "nat", "difficulty": 2, "type": "mcq",
        "stem": "Which NAT type lets many inside hosts share a single public IP by "
                "multiplexing on Layer 4 port numbers?",
        "options": [
            {"id": "A", "text": "Static NAT (one-to-one)"},
            {"id": "B", "text": "Dynamic NAT (pool, one-to-one)"},
            {"id": "C", "text": "PAT / NAT overload"},
            {"id": "D", "text": "Twice NAT"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "PAT (Port Address Translation), configured with the 'overload' keyword, "
                       "maps many inside addresses to one outside address by tracking unique "
                       "source ports — the basis of typical home/office Internet access.",
            "distractors": {
                "A": "Static NAT is a fixed one-to-one mapping, often for inbound servers.",
                "B": "Dynamic NAT assigns from a pool but is still one-to-one while a mapping lasts.",
                "D": "Twice NAT translates both source and destination; it is not the many-to-one sharing mechanism.",
            },
            "exam_pattern": "Keyword 'overload' = PAT = many-to-one using ports. 'inside/outside' "
                            "and 'local/global' terminology is the other favorite NAT trap.",
        },
        "verify_cli": ["show ip nat translations", "show ip nat statistics"],
        "references": ["CCNA 200-301 Topic 4.1 NAT"],
        "tags": ["nat", "pat"],
    },
    {
        "id": "ccna-is-002", "exam": "ccna", "domain": "ip_services",
        "subtopic": "dhcp", "difficulty": 2, "type": "mcq",
        "stem": "Clients on a subnet with no local DHCP server receive no addresses. The "
                "server is on another subnet. Which command on the clients' gateway SVI fixes this?",
        "options": [
            {"id": "A", "text": "ip helper-address <DHCP server IP>"},
            {"id": "B", "text": "ip dhcp excluded-address <range>"},
            {"id": "C", "text": "ip dhcp pool LOCAL"},
            {"id": "D", "text": "service dhcp"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'ip helper-address' turns the router/SVI into a DHCP relay: it converts "
                       "the client broadcast DISCOVER into a unicast to the server across subnets "
                       "(and relays other key UDP broadcasts).",
            "distractors": {
                "A": "",
                "B": "excluded-address reserves addresses within a LOCAL pool; it does not relay "
                     "to a remote server.",
                "C": "Creating a local pool would make this router the server, not relay to the "
                     "existing one.",
                "D": "'service dhcp' just enables the DHCP feature globally (on by default); it "
                     "does not forward across subnets.",
            },
            "exam_pattern": "Cross-subnet DHCP = relay via 'ip helper-address' on the interface "
                            "facing the clients. Remember DORA: Discover, Offer, Request, Ack.",
        },
        "verify_cli": ["show ip interface g0/0 | include Helper", "show running-config interface vlan10"],
        "references": ["CCNA 200-301 Topic 4.3 DHCP relay"],
        "tags": ["dhcp", "relay", "helper-address"],
    },
    {
        "id": "ccna-is-003", "exam": "ccna", "domain": "ip_services",
        "subtopic": "ntp", "difficulty": 1, "type": "mcq",
        "stem": "An NTP server shows 'stratum 2'. What does the stratum value indicate?",
        "options": [
            {"id": "A", "text": "The number of clients synchronized to it"},
            {"id": "B", "text": "Its distance (hop count) from an authoritative reference clock"},
            {"id": "C", "text": "The polling interval in seconds"},
            {"id": "D", "text": "The NTP version number"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Stratum measures distance from the reference clock. Stratum 0 is the "
                       "reference (atomic/GPS), stratum 1 is directly attached, stratum 2 syncs "
                       "to a stratum-1 server, and so on. Lower stratum = more authoritative.",
            "distractors": {
                "A": "Stratum has nothing to do with how many clients use the server.",
                "B": "",
                "C": "Polling interval is a separate NTP parameter, not the stratum.",
                "D": "NTP version (e.g., v3/v4) is unrelated to the stratum number.",
            },
            "exam_pattern": "Lower stratum = closer to the true time source. A device syncing to "
                            "a stratum-N server becomes stratum N+1.",
        },
        "verify_cli": ["show ntp status", "show ntp associations"],
        "references": ["CCNA 200-301 Topic 4.2 NTP"],
        "tags": ["ntp", "stratum"],
    },
    {
        "id": "ccna-is-004", "exam": "ccna", "domain": "ip_services",
        "subtopic": "syslog", "difficulty": 2, "type": "mcq",
        "stem": "A logging policy says to capture messages of severity 'warning' and more "
                "severe. Which 'logging trap' level and numeric value is correct?",
        "options": [
            {"id": "A", "text": "logging trap 4 (warnings)"},
            {"id": "B", "text": "logging trap 7 (debugging)"},
            {"id": "C", "text": "logging trap 2 (critical)"},
            {"id": "D", "text": "logging trap 0 (emergencies)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Syslog severities run 0 (emergency) to 7 (debug); LOWER is more severe. "
                       "'logging trap 4' captures level 4 (warning) and everything numerically "
                       "below it (0–4), i.e., warning and more severe.",
            "distractors": {
                "A": "",
                "B": "Level 7 (debugging) captures EVERYTHING 0–7, far more than warnings-and-above.",
                "C": "Level 2 (critical) would miss levels 3 (error) and 4 (warning).",
                "D": "Level 0 captures only emergencies.",
            },
            "exam_pattern": "Mnemonic 0–7: Every Awesome Cisco Engineer Will Need Icecream Daily "
                            "(Emergency, Alert, Critical, Error, Warning, Notice, Info, Debug). "
                            "Setting level N logs 0..N.",
        },
        "verify_cli": ["show logging", "show running-config | include logging"],
        "references": ["CCNA 200-301 Topic 4.5 syslog"],
        "tags": ["syslog", "severity"],
    },
    {
        "id": "ccna-is-005", "exam": "ccna", "domain": "ip_services",
        "subtopic": "snmp", "difficulty": 2, "type": "mcq",
        "stem": "Security requires authentication AND encryption of SNMP management traffic. "
                "Which SNMP configuration meets both requirements?",
        "options": [
            {"id": "A", "text": "SNMPv2c with a complex community string"},
            {"id": "B", "text": "SNMPv3 with the 'auth' security level"},
            {"id": "C", "text": "SNMPv3 with the 'priv' security level"},
            {"id": "D", "text": "SNMPv1 with an ACL"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Only SNMPv3 offers encryption, and the 'priv' level provides BOTH "
                       "authentication (authPriv) and privacy/encryption of the payload.",
            "distractors": {
                "A": "SNMPv2c sends community strings in clear text — no encryption at all.",
                "B": "'auth' (authNoPriv) authenticates but does NOT encrypt the data.",
                "D": "SNMPv1 with an ACL limits who can connect but still sends data in clear text.",
            },
            "exam_pattern": "SNMPv3 levels: noAuthNoPriv < authNoPriv < authPriv. Only 'priv' "
                            "(authPriv) encrypts. v1/v2c never encrypt.",
        },
        "verify_cli": ["show snmp user", "show snmp group"],
        "references": ["CCNA 200-301 Topic 4.4 SNMP"],
        "tags": ["snmp", "snmpv3"],
    },
    {
        "id": "ccna-is-006", "exam": "ccna", "domain": "ip_services",
        "subtopic": "qos_concepts", "difficulty": 2, "type": "mcq",
        "stem": "Which DSCP marking is the standard recommendation for latency-sensitive VoIP "
                "media (RTP) traffic placed in a priority queue?",
        "options": [
            {"id": "A", "text": "EF (Expedited Forwarding, DSCP 46)"},
            {"id": "B", "text": "CS1 (DSCP 8)"},
            {"id": "C", "text": "AF11 (DSCP 10)"},
            {"id": "D", "text": "Default / Best Effort (DSCP 0)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EF (DSCP 46) is the per-hop behavior reserved for low-latency, "
                       "low-jitter traffic like voice media, typically serviced by a priority "
                       "(LLQ) queue.",
            "distractors": {
                "A": "",
                "B": "CS1 (8) is 'scavenger'-class, the LOWEST priority — the opposite of voice.",
                "C": "AF11 is a low-drop assured-forwarding class, used for some data, not voice media.",
                "D": "DSCP 0 is best-effort with no QoS guarantee, unsuitable for real-time voice.",
            },
            "exam_pattern": "Voice media = EF (46), priority queue. Call signaling = CS3 (24). "
                            "Scavenger = CS1 (8). Best effort = 0.",
        },
        "verify_cli": ["show policy-map interface g0/0", "show mls qos"],
        "references": ["CCNA 200-301 Topic 4.7 QoS"],
        "tags": ["qos", "dscp", "voip"],
    },

    # ===================== 5.0 SECURITY FUNDAMENTALS =====================
    {
        "id": "ccna-se-001", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "acls", "difficulty": 3, "type": "mcq",
        "stem": "An extended ACL is applied to deny host 10.1.1.10 from reaching web server "
                "203.0.113.5. Where should it be placed, per Cisco best practice?",
        "options": [
            {"id": "A", "text": "Inbound, closest to the source (10.1.1.10's router interface)"},
            {"id": "B", "text": "Outbound, closest to the destination server"},
            {"id": "C", "text": "Inbound on every interface in the path"},
            {"id": "D", "text": "It does not matter where an extended ACL is placed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Extended ACLs match source AND destination, so place them close to the "
                       "SOURCE to drop unwanted traffic early and save bandwidth across the network.",
            "distractors": {
                "A": "",
                "B": "That is the rule for STANDARD ACLs (match source only → place near "
                     "destination to avoid over-blocking).",
                "C": "Applying it everywhere wastes resources and risks unintended drops.",
                "D": "Placement absolutely matters for efficiency and correctness.",
            },
            "exam_pattern": "Extended → near SOURCE. Standard → near DESTINATION. Remember the "
                            "implicit 'deny any' at the end of every ACL.",
        },
        "verify_cli": ["show ip access-lists", "show ip interface g0/0 | include access list"],
        "references": ["CCNA 200-301 Topic 5.6 ACLs"],
        "tags": ["acl", "placement"],
    },
    {
        "id": "ccna-se-002", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "port_security", "difficulty": 2, "type": "mcq",
        "stem": "A port-security violation occurs. The port should DROP offending frames and "
                "increment a counter but remain up (no err-disable). Which violation mode is this?",
        "options": [
            {"id": "A", "text": "protect"},
            {"id": "B", "text": "restrict"},
            {"id": "C", "text": "shutdown"},
            {"id": "D", "text": "shutdown vlan"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "'restrict' drops violating frames, increments the violation counter, and "
                       "sends an SNMP trap/syslog — while keeping the port up.",
            "distractors": {
                "A": "'protect' also drops frames but does NOT increment the counter or alert.",
                "B": "",
                "C": "'shutdown' (the default) err-disables the port entirely on violation.",
                "D": "'shutdown vlan' err-disables only the offending VLAN on the port, not the standard counting behaviour described.",
            },
            "exam_pattern": "protect = silent drop; restrict = drop + count + alert; shutdown = "
                            "err-disable (default). The counter + stays-up combo points to restrict.",
        },
        "verify_cli": ["show port-security interface g0/1", "show port-security"],
        "references": ["CCNA 200-301 Topic 5.7 port security"],
        "tags": ["port-security", "violation"],
    },
    {
        "id": "ccna-se-003", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "dhcp_snooping", "difficulty": 2, "type": "mcq",
        "stem": "After enabling DHCP snooping, clients connected through the uplink to the "
                "real DHCP server stop getting addresses. What is the MOST likely fix?",
        "options": [
            {"id": "A", "text": "Configure the uplink toward the DHCP server as a trusted port"},
            {"id": "B", "text": "Configure the client access ports as trusted"},
            {"id": "C", "text": "Disable DHCP snooping on the server VLAN"},
            {"id": "D", "text": "Add 'ip dhcp snooping information option' on client ports"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DHCP snooping treats all ports as UNtrusted by default, dropping "
                       "server-sourced messages (OFFER/ACK) on them. The port toward the "
                       "legitimate DHCP server must be marked trusted with 'ip dhcp snooping trust'.",
            "distractors": {
                "A": "",
                "B": "Access ports facing clients should stay UNtrusted — trusting them defeats "
                     "the protection against rogue servers.",
                "C": "Disabling snooping removes the security entirely rather than fixing the trust boundary.",
                "D": "Option-82 insertion is unrelated to the server replies being dropped; and "
                     "it often must be managed carefully across relays.",
            },
            "exam_pattern": "Snooping default = untrusted everywhere. Trust only the ports toward "
                            "real DHCP servers/uplinks. Client ports stay untrusted (rate-limited).",
        },
        "verify_cli": ["show ip dhcp snooping", "show ip dhcp snooping binding"],
        "references": ["CCNA 200-301 Topic 5.7 DHCP snooping"],
        "tags": ["dhcp-snooping", "trust"],
    },
    {
        "id": "ccna-se-004", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "acls", "difficulty": 2, "type": "mcq",
        "stem": "Which line correctly permits ONLY the single host 192.168.1.17 in a "
                "standard numbered ACL?",
        "options": [
            {"id": "A", "text": "access-list 1 permit host 192.168.1.17"},
            {"id": "B", "text": "access-list 1 permit 192.168.1.17 255.255.255.255"},
            {"id": "C", "text": "access-list 1 permit 192.168.1.17 0.0.0.255"},
            {"id": "D", "text": "access-list 1 permit 192.168.1.0 0.0.0.0"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'host 192.168.1.17' is shorthand for the wildcard 0.0.0.0 (match exactly "
                       "this address). It is the correct, idiomatic single-host match.",
            "distractors": {
                "A": "",
                "B": "255.255.255.255 as a wildcard means 'match ANY address' — the opposite of one host.",
                "C": "0.0.0.255 matches the whole 192.168.1.0/24, not a single host.",
                "D": "0.0.0.0 wildcard is right, but the base address is .0 (the network), not .17.",
            },
            "exam_pattern": "host X == X 0.0.0.0. any == 0.0.0.0 255.255.255.255. Watch for the "
                            "classic swap of subnet mask vs wildcard.",
        },
        "verify_cli": ["show access-lists 1", "show ip access-lists"],
        "references": ["CCNA 200-301 Topic 5.6 ACLs"],
        "tags": ["acl", "wildcard", "host"],
    },
    {
        "id": "ccna-se-005", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "aaa_8021x", "difficulty": 2, "type": "mcq",
        "stem": "In an 802.1X deployment, which device plays the role of the 'authenticator'?",
        "options": [
            {"id": "A", "text": "The end-user PC running the 802.1X client"},
            {"id": "B", "text": "The access switch controlling port access"},
            {"id": "C", "text": "The RADIUS server validating credentials"},
            {"id": "D", "text": "The Active Directory domain controller"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The authenticator is the switch (or WLC): it sits between the supplicant "
                       "and the authentication server, controlling the port and relaying EAP to "
                       "RADIUS.",
            "distractors": {
                "A": "The PC/software is the SUPPLICANT.",
                "B": "",
                "C": "The RADIUS server (e.g., ISE) is the AUTHENTICATION SERVER.",
                "D": "AD is an identity store the auth server queries, not an 802.1X role itself.",
            },
            "exam_pattern": "Three roles: Supplicant (client) ↔ Authenticator (switch/WLC) ↔ "
                            "Authentication Server (RADIUS). EAP between supplicant/authenticator; "
                            "RADIUS between authenticator/server.",
        },
        "verify_cli": ["show authentication sessions", "show dot1x all"],
        "references": ["CCNA 200-301 Topic 5.8 802.1X/AAA"],
        "tags": ["dot1x", "aaa", "radius"],
    },
    {
        "id": "ccna-se-006", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "layer2_security", "difficulty": 2, "type": "mcq",
        "stem": "Which Layer 2 attack is directly mitigated by enabling BPDU Guard on access "
                "(PortFast) ports?",
        "options": [
            {"id": "A", "text": "A rogue switch injecting superior BPDUs to become root"},
            {"id": "B", "text": "A CAM/MAC flooding attack"},
            {"id": "C", "text": "A DHCP starvation attack"},
            {"id": "D", "text": "ARP cache poisoning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BPDU Guard err-disables a PortFast port the instant it receives ANY BPDU, "
                       "stopping an unauthorized switch from participating in STP or hijacking the "
                       "root role on an access port.",
            "distractors": {
                "A": "",
                "B": "MAC flooding is mitigated by port security, not BPDU Guard.",
                "C": "DHCP starvation is handled by DHCP snooping + port security.",
                "D": "ARP poisoning is mitigated by Dynamic ARP Inspection (DAI).",
            },
            "exam_pattern": "Match the tool to the attack: BPDU Guard→rogue STP/BPDUs; Port "
                            "security→MAC flooding; DHCP snooping→rogue DHCP/starvation; DAI→ARP spoofing.",
        },
        "verify_cli": ["show spanning-tree summary", "show spanning-tree interface g0/1 detail"],
        "references": ["CCNA 200-301 Topic 5.7 Layer 2 security"],
        "tags": ["bpdu-guard", "stp-security"],
    },
    {
        "id": "ccna-se-007", "exam": "ccna", "domain": "security_fundamentals",
        "subtopic": "vpn_concepts", "difficulty": 1, "type": "mcq",
        "stem": "Which pair of IPsec protocols/services provides BOTH confidentiality "
                "(encryption) and data integrity for a site-to-site VPN?",
        "options": [
            {"id": "A", "text": "ESP"},
            {"id": "B", "text": "AH only"},
            {"id": "C", "text": "GRE only"},
            {"id": "D", "text": "HSRP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ESP (Encapsulating Security Payload) provides encryption AND integrity/"
                       "authentication of the payload. AH provides integrity/authentication but "
                       "NO encryption.",
            "distractors": {
                "A": "",
                "B": "AH authenticates but does not encrypt, so it fails the confidentiality requirement.",
                "C": "GRE is a tunneling protocol with no encryption by itself (often paired with IPsec).",
                "D": "HSRP is a first-hop redundancy protocol, unrelated to VPN security.",
            },
            "exam_pattern": "ESP = encryption + integrity. AH = integrity only (no encryption). "
                            "IKE/ISAKMP negotiates the keys. GRE adds multiprotocol tunneling, not security.",
        },
        "verify_cli": ["show crypto ipsec sa", "show crypto isakmp sa"],
        "references": ["CCNA 200-301 Topic 5.0 VPN concepts"],
        "tags": ["vpn", "ipsec", "esp"],
    },

    # ===================== 6.0 AUTOMATION & PROGRAMMABILITY =====================
    {
        "id": "ccna-au-001", "exam": "ccna", "domain": "automation",
        "subtopic": "netconf_restconf", "difficulty": 3, "type": "mcq",
        "stem": "Which statement correctly contrasts NETCONF and RESTCONF?",
        "options": [
            {"id": "A", "text": "NETCONF uses SSH (port 830) and XML; RESTCONF uses HTTPS and XML or JSON"},
            {"id": "B", "text": "NETCONF uses HTTP verbs on port 443; RESTCONF uses SNMP"},
            {"id": "C", "text": "Both use SNMPv3 as their transport"},
            {"id": "D", "text": "RESTCONF uses SSH port 22; NETCONF uses Telnet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NETCONF runs over SSH (TCP 830) and encodes data in XML, with explicit "
                       "datastores and RPCs. RESTCONF is a REST/HTTPS interface to the same YANG "
                       "models and supports XML or JSON encoding.",
            "distractors": {
                "A": "",
                "B": "NETCONF does not use HTTP verbs; RESTCONF (not NETCONF) is the HTTP/REST one, and neither uses SNMP.",
                "C": "Neither protocol uses SNMP as transport; both are model-driven (YANG) alternatives to SNMP.",
                "D": "RESTCONF uses HTTPS (443), not SSH/22; NETCONF uses SSH/830, not Telnet.",
            },
            "exam_pattern": "NETCONF = SSH 830, XML, datastores (running/candidate/startup), RPCs. "
                            "RESTCONF = HTTPS 443, XML/JSON, HTTP verbs (GET/POST/PUT/PATCH/DELETE). "
                            "Both driven by YANG models.",
        },
        "verify_cli": ["show netconf-yang sessions", "show running-config | include netconf|restconf"],
        "references": ["CCNA 200-301 Topic 6.5/6.6 NETCONF/RESTCONF"],
        "tags": ["netconf", "restconf", "yang"],
    },
    {
        "id": "ccna-au-002", "exam": "ccna", "domain": "automation",
        "subtopic": "rest_api", "difficulty": 2, "type": "mcq",
        "stem": "A RESTCONF client sends an HTTP PUT and receives '201 Created'. What does this "
                "status code indicate?",
        "options": [
            {"id": "A", "text": "The request was malformed and rejected"},
            {"id": "B", "text": "The resource was successfully created"},
            {"id": "C", "text": "Authentication failed"},
            {"id": "D", "text": "The server encountered an internal error"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "2xx codes indicate success; 201 specifically means a new resource was "
                       "created as a result of the request.",
            "distractors": {
                "A": "A malformed request returns 4xx, typically 400 Bad Request.",
                "B": "",
                "C": "Authentication failure returns 401 Unauthorized (or 403 Forbidden).",
                "D": "A server-side error returns 5xx, e.g., 500 Internal Server Error.",
            },
            "exam_pattern": "HTTP ranges: 2xx success (200 OK, 201 Created, 204 No Content), 3xx "
                            "redirect, 4xx client error (400/401/403/404), 5xx server error.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 6.6 REST APIs"],
        "tags": ["rest", "http-status"],
    },
    {
        "id": "ccna-au-003", "exam": "ccna", "domain": "automation",
        "subtopic": "json_data", "difficulty": 2, "type": "mcq",
        "stem": "In the JSON below, what is the data type of the value associated with the key "
                "\"interfaces\"?",
        "exhibit": '{\n  "hostname": "R1",\n  "uptime": 3600,\n  "enabled": true,\n'
                   '  "interfaces": ["Gi0/0", "Gi0/1", "Lo0"]\n}',
        "options": [
            {"id": "A", "text": "Object (dictionary)"},
            {"id": "B", "text": "Array (list)"},
            {"id": "C", "text": "String"},
            {"id": "D", "text": "Boolean"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Square brackets [ ] denote a JSON array (an ordered list). Here "
                       "\"interfaces\" maps to a list of three strings.",
            "distractors": {
                "A": "Objects use curly braces { } with key:value pairs.",
                "B": "",
                "C": "A string would be in double quotes with no brackets, e.g., \"Gi0/0\".",
                "D": "Booleans are the literals true/false (like \"enabled\" here), not a bracketed list.",
            },
            "exam_pattern": "JSON types: {} object, [] array, \"\" string, numbers, true/false, "
                            "null. Count brackets to identify the structure.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 6.7 data formats (JSON)"],
        "tags": ["json", "data-format"],
    },
    {
        "id": "ccna-au-004", "exam": "ccna", "domain": "automation",
        "subtopic": "config_mgmt_tools", "difficulty": 2, "type": "mcq",
        "stem": "Which configuration-management tool is AGENTLESS and pushes configuration to "
                "devices over SSH using YAML 'playbooks'?",
        "options": [
            {"id": "A", "text": "Ansible"},
            {"id": "B", "text": "Puppet"},
            {"id": "C", "text": "Chef"},
            {"id": "D", "text": "SaltStack (with minions)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ansible is agentless (uses SSH/NETCONF), uses a push model, and defines "
                       "automation in YAML playbooks — a good fit for network devices that can't "
                       "run agents.",
            "distractors": {
                "A": "",
                "B": "Puppet is agent-based (pull model) and uses its own declarative DSL "
                     "(manifests), typically over TCP 8140.",
                "C": "Chef is agent-based (pull), uses Ruby-based 'recipes'/'cookbooks'.",
                "D": "SaltStack commonly uses minions (agents), though it has an agentless SSH mode.",
            },
            "exam_pattern": "Ansible = agentless, push, YAML, SSH. Puppet/Chef = agent, pull "
                            "(manifests/recipes). This push/pull + agent distinction is the usual question.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 6.4 config management tools"],
        "tags": ["ansible", "automation-tools"],
    },
    {
        "id": "ccna-au-005", "exam": "ccna", "domain": "automation",
        "subtopic": "sdn_controllers", "difficulty": 2, "type": "mcq",
        "stem": "In an SDN controller-based architecture, which interface does the controller "
                "use to communicate DOWN to the network devices (the forwarding plane)?",
        "options": [
            {"id": "A", "text": "The northbound interface (NBI)"},
            {"id": "B", "text": "The southbound interface (SBI)"},
            {"id": "C", "text": "The management plane VLAN"},
            {"id": "D", "text": "The east-west interface"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Southbound interfaces (e.g., NETCONF, OpenFlow, Cisco OnePK) connect the "
                       "controller DOWN to the devices it programs. Northbound APIs face UP toward "
                       "applications/orchestration.",
            "distractors": {
                "A": "Northbound faces UP to apps/scripts (often REST), not down to devices.",
                "B": "",
                "C": "A management VLAN is not an SDN controller interface concept.",
                "D": "East-west is controller-to-controller communication, not controller-to-device.",
            },
            "exam_pattern": "Northbound = up to apps (REST). Southbound = down to devices "
                            "(NETCONF/OpenFlow). Think of the controller in the middle of the sandwich.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 6.1 SDN/controllers"],
        "tags": ["sdn", "controller", "apis"],
    },
    {
        "id": "ccna-au-006", "exam": "ccna", "domain": "automation",
        "subtopic": "config_mgmt_tools", "difficulty": 2, "type": "mcq",
        "stem": "What is the primary benefit of using a controller-based network with "
                "'intent-based' automation compared to traditional per-device CLI?",
        "options": [
            {"id": "A", "text": "It removes the need for any IP addressing"},
            {"id": "B", "text": "Centralized, consistent policy with reduced configuration drift and human error"},
            {"id": "C", "text": "It eliminates the need for routing protocols entirely"},
            {"id": "D", "text": "It makes all links automatically faster"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Controller-based/intent-based automation translates business intent into "
                       "consistent device configuration centrally, reducing drift, speeding "
                       "changes, and minimizing manual per-box errors.",
            "distractors": {
                "A": "Devices still need IP addressing; automation does not remove it.",
                "B": "",
                "C": "Underlay routing is still required (often automated), not eliminated.",
                "D": "Automation does not change physical link speeds.",
            },
            "exam_pattern": "Automation benefits = consistency, speed, scalability, fewer errors, "
                            "less drift. Watch for 'eliminates X entirely' distractors — automation "
                            "manages, it doesn't abolish fundamentals.",
        },
        "verify_cli": [],
        "references": ["CCNA 200-301 Topic 6.2 controller-based networking"],
        "tags": ["automation", "intent-based"],
    },
]
