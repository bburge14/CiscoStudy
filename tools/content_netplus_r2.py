"""CompTIA Network+ N10-009 item pool (round 2) — original, objective-aligned questions.

Same authoring rules as the other pools: original content mapped to the public
N10-009 exam objectives, never real exam items. build_content.py shuffles option
order, so the answer key here is not positionally biased. Every item uses a
"-r2-" id segment to guarantee no collision with the base Network+ bank.
"""

QUESTIONS = [
    # ===== 1.0 Networking Concepts ==========================================
    {
        "id": "netplus-nc-r2-001", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 2, "type": "mcq",
        "stem": "A router forwards traffic between two subnets by examining the destination IP "
                "address of each packet. At which OSI layer does the router make this forwarding "
                "decision, and what is the PDU called there?",
        "options": [
            {"id": "A", "text": "Layer 3 (Network) — the PDU is a packet"},
            {"id": "B", "text": "Layer 2 (Data Link) — the PDU is a frame"},
            {"id": "C", "text": "Layer 4 (Transport) — the PDU is a segment"},
            {"id": "D", "text": "Layer 1 (Physical) — the PDU is a bit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Routing is a Layer 3 (Network) function: routers read the destination IP "
                       "address and consult the routing table. The Layer 3 PDU is the packet.",
            "distractors": {
                "B": "Layer 2 switches forward by MAC address and the PDU is a frame — that is "
                     "switching/bridging, not IP routing.",
                "C": "Layer 4 handles end-to-end segments (TCP/UDP ports); routers do not forward "
                     "on port numbers.",
                "D": "Layer 1 moves raw bits on the medium; no addressing decision happens there.",
            },
            "exam_pattern": "PDU by layer: L2 = frame (MAC), L3 = packet (IP, routers), L4 = "
                            "segment/datagram (ports). 'Forwards by IP' = Layer 3.",
        },
    },
    {
        "id": "netplus-nc-r2-002", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 1, "type": "mcq",
        "stem": "A technician installs a repeater that simply regenerates and retimes the electrical "
                "signal on a long cable run so bits travel farther. At which OSI layer does a "
                "repeater (or a basic hub) operate?",
        "options": [
            {"id": "A", "text": "Layer 1 (Physical)"},
            {"id": "B", "text": "Layer 2 (Data Link)"},
            {"id": "C", "text": "Layer 3 (Network)"},
            {"id": "D", "text": "Layer 7 (Application)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A repeater or passive hub works purely with the signal (bits) on the medium — "
                       "that is the Physical layer. It has no awareness of MAC or IP addresses.",
            "distractors": {
                "B": "Data Link devices (switches, bridges) read MAC addresses and build "
                     "frame-forwarding tables; a repeater does neither.",
                "C": "Network layer devices (routers) make decisions based on IP addresses.",
                "D": "The Application layer is where user-facing protocols like HTTP operate, far "
                     "above signal regeneration.",
            },
            "exam_pattern": "Hub/repeater = Layer 1 (bits). Switch/bridge = Layer 2 (frames). "
                            "Router = Layer 3 (packets).",
        },
    },
    {
        "id": "netplus-nc-r2-003", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_appliances", "difficulty": 2, "type": "mcq",
        "stem": "A popular website runs on a pool of identical web servers. The company wants "
                "incoming client requests spread evenly across the servers, with traffic "
                "automatically steered away from any server that fails a health check. Which "
                "appliance provides this?",
        "options": [
            {"id": "A", "text": "Load balancer"},
            {"id": "B", "text": "Proxy server"},
            {"id": "C", "text": "Intrusion prevention system (IPS)"},
            {"id": "D", "text": "VPN concentrator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A load balancer distributes client requests across a pool of servers and uses "
                       "health checks to stop sending traffic to a failed member — improving both "
                       "scalability and availability.",
            "distractors": {
                "B": "A proxy fetches content on behalf of clients (often for caching/filtering); it "
                     "does not distribute load across a server farm with health checks.",
                "C": "An IPS inspects traffic and blocks malicious packets; it is not a "
                     "traffic-distribution device.",
                "D": "A VPN concentrator terminates encrypted remote-access tunnels; it does not "
                     "balance web-server load.",
            },
            "exam_pattern": "Spread requests across a server pool + health checks = load balancer. "
                            "Fetch-on-behalf/caching = proxy.",
        },
    },
    {
        "id": "netplus-nc-r2-004", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "cloud_concepts", "difficulty": 1, "type": "mcq",
        "stem": "Employees use a web-based email and office suite entirely through their browsers. "
                "The provider owns and maintains the servers, operating systems, and the "
                "applications themselves; the company manages only its user accounts and data. "
                "Which cloud service model is this?",
        "options": [
            {"id": "A", "text": "Software as a Service (SaaS)"},
            {"id": "B", "text": "Platform as a Service (PaaS)"},
            {"id": "C", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "D", "text": "Desktop as a Service (DaaS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SaaS delivers a finished application the customer simply consumes (e.g., web "
                       "mail/office suites). The provider manages everything down to the app; the "
                       "customer manages only its data and user access.",
            "distractors": {
                "B": "PaaS gives developers a managed platform/runtime to deploy their OWN "
                     "applications — not a ready-made app.",
                "C": "IaaS rents raw compute/storage/network; the customer still installs and "
                     "manages the OS and apps.",
                "D": "DaaS delivers virtual desktops, not a web email/office application suite.",
            },
            "exam_pattern": "Ready-to-use app via browser = SaaS. Build/deploy your code = PaaS. "
                            "Rent VMs/storage = IaaS.",
        },
    },
    {
        "id": "netplus-nc-r2-005", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 1, "type": "mcq",
        "stem": "A help-desk technician must open a firewall rule to allow Remote Desktop Protocol "
                "(RDP) connections to a Windows server for remote graphical administration. Which "
                "transport protocol and port must be permitted?",
        "options": [
            {"id": "A", "text": "TCP 3389"},
            {"id": "B", "text": "TCP 22"},
            {"id": "C", "text": "UDP 161"},
            {"id": "D", "text": "TCP 443"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RDP listens on TCP 3389 and provides a full remote graphical session to a "
                       "Windows host.",
            "distractors": {
                "B": "TCP 22 is SSH — encrypted remote command-line access, not the Windows "
                     "graphical RDP session.",
                "C": "UDP 161 is SNMP, used to poll device statistics, not remote desktop.",
                "D": "TCP 443 is HTTPS; it secures web traffic and is not the default RDP port.",
            },
            "exam_pattern": "Memorize: RDP 3389, SSH 22, SNMP 161/162, HTTPS 443, Telnet 23. "
                            "RDP = graphical Windows remote.",
        },
    },
    {
        "id": "netplus-nc-r2-006", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 2, "type": "multi",
        "stem": "A security review requires removing legacy management protocols that transmit data "
                "and credentials in CLEAR TEXT. Which TWO protocols should be disabled in favor of "
                "encrypted replacements? (Choose two.)",
        "options": [
            {"id": "A", "text": "Telnet (TCP 23)"},
            {"id": "B", "text": "FTP (TCP 20/21)"},
            {"id": "C", "text": "SSH (TCP 22)"},
            {"id": "D", "text": "HTTPS (TCP 443)"},
            {"id": "E", "text": "SFTP (TCP 22)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Telnet and FTP send everything — including usernames and passwords — in "
                       "clear text. Replace Telnet with SSH and FTP with SFTP/FTPS.",
            "distractors": {
                "C": "SSH is the ENCRYPTED replacement for Telnet, not a plaintext protocol to remove.",
                "D": "HTTPS encrypts web traffic with TLS; it is a secure protocol you keep.",
                "E": "SFTP runs file transfer over the encrypted SSH channel — it is the secure "
                     "replacement for FTP.",
            },
            "exam_pattern": "Clear text (remove): Telnet 23, FTP 21, HTTP 80, SNMPv1/2c. Encrypted "
                            "(keep): SSH 22, SFTP 22, HTTPS 443, SNMPv3.",
        },
    },
    {
        "id": "netplus-nc-r2-007", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "traffic_types", "difficulty": 2, "type": "mcq",
        "stem": "A streaming application sends one copy of a video feed that is simultaneously "
                "delivered only to the set of hosts that have subscribed to the group. Which IPv4 "
                "address range is reserved for this multicast traffic?",
        "options": [
            {"id": "A", "text": "224.0.0.0 to 239.255.255.255"},
            {"id": "B", "text": "127.0.0.0 to 127.255.255.255"},
            {"id": "C", "text": "169.254.0.0 to 169.254.255.255"},
            {"id": "D", "text": "240.0.0.0 to 255.255.255.255"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IPv4 multicast uses the Class D range 224.0.0.0–239.255.255.255. A source "
                       "sends one stream to a group address and only subscribed receivers get it.",
            "distractors": {
                "B": "127.0.0.0/8 is the loopback range used for a host to reach itself.",
                "C": "169.254.0.0/16 is APIPA/link-local, auto-assigned when DHCP fails.",
                "D": "240.0.0.0 onward is Class E (experimental/reserved); 255.255.255.255 is the "
                     "limited broadcast address.",
            },
            "exam_pattern": "Class D 224–239 = multicast (one-to-group). 127 = loopback, 169.254 = "
                            "APIPA, 240+ = experimental.",
        },
    },
    {
        "id": "netplus-nc-r2-008", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 2, "type": "mcq",
        "stem": "An engineer assigns a subnet mask of 255.255.255.248 to several small subnets. "
                "How many USABLE host addresses does each such subnet provide?",
        "options": [
            {"id": "A", "text": "6"},
            {"id": "B", "text": "8"},
            {"id": "C", "text": "14"},
            {"id": "D", "text": "2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "255.255.255.248 is a /29: 3 host bits remain, so 2^3 = 8 total addresses "
                       "minus the network and broadcast addresses = 6 usable hosts.",
            "distractors": {
                "B": "8 is the TOTAL addresses in the block; you must subtract the network and "
                     "broadcast addresses.",
                "C": "14 usable hosts corresponds to a /28 (255.255.255.240), which has 4 host bits.",
                "D": "2 usable hosts corresponds to a /30 (255.255.255.252), used for "
                     "point-to-point links.",
            },
            "exam_pattern": "Usable hosts = 2^(host bits) − 2. /30=2, /29=6, /28=14, /27=30, /26=62.",
        },
    },
    {
        "id": "netplus-nc-r2-009", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 3, "type": "mcq",
        "stem": "A host is configured as 10.20.30.100 with a /28 mask (255.255.255.240). What is "
                "the BROADCAST address of the subnet this host belongs to?",
        "options": [
            {"id": "A", "text": "10.20.30.111"},
            {"id": "B", "text": "10.20.30.96"},
            {"id": "C", "text": "10.20.30.127"},
            {"id": "D", "text": "10.20.30.255"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A /28 has a block size of 16. Subnets increment 0, 16, 32 … 96, 112. The "
                       "host .100 falls in the 10.20.30.96 subnet, whose broadcast is one below the "
                       "next subnet boundary (112) = 10.20.30.111.",
            "distractors": {
                "B": "10.20.30.96 is the NETWORK (subnet) address, not the broadcast.",
                "C": "10.20.30.127 would be the broadcast of the .112 subnet, not the .96 subnet "
                     "that contains .100.",
                "D": "10.20.30.255 is the broadcast only for a /24; with a /28 the broadcast falls "
                     "on each 16-address block boundary.",
            },
            "exam_pattern": "Block size = 256 − mask octet (256−240=16). Broadcast = next subnet "
                            "boundary − 1.",
        },
    },
    {
        "id": "netplus-nc-r2-010", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv6_np", "difficulty": 2, "type": "mcq",
        "stem": "An organization needs IPv6 addresses for internal communication only — addresses "
                "that are routable within the site but must NOT be routed on the public Internet, "
                "serving the same purpose as RFC 1918 private IPv4 space. Which IPv6 address type "
                "fits?",
        "options": [
            {"id": "A", "text": "Unique local address (fc00::/7, commonly fd00::/8)"},
            {"id": "B", "text": "Global unicast address (2000::/3)"},
            {"id": "C", "text": "Link-local address (fe80::/10)"},
            {"id": "D", "text": "Multicast address (ff00::/8)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Unique local addresses (ULAs, fc00::/7 — in practice fd00::/8) are the IPv6 "
                       "equivalent of RFC 1918 private addresses: routable inside the organization "
                       "but not advertised on the public Internet.",
            "distractors": {
                "B": "Global unicast (2000::/3) addresses ARE globally routable on the public "
                     "Internet — the opposite of the requirement.",
                "C": "Link-local (fe80::/10) addresses work only on a single link and are not "
                     "routed between subnets at all.",
                "D": "ff00::/8 is multicast (one-to-many), not a unicast private-addressing scheme.",
            },
            "exam_pattern": "IPv6: GUA 2000::/3 (public), ULA fd00::/8 (private/internal), "
                            "link-local fe80::/10 (one link), multicast ff00::/8.",
        },
    },
    {
        "id": "netplus-nc-r2-011", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_topologies", "difficulty": 3, "type": "mcq",
        "stem": "A WAN designer wants every one of 5 sites to have a direct dedicated link to every "
                "other site so that no single link failure can isolate any pair. What topology is "
                "this, and how many links are required?",
        "options": [
            {"id": "A", "text": "Full mesh — 10 links"},
            {"id": "B", "text": "Full mesh — 5 links"},
            {"id": "C", "text": "Hub-and-spoke (star) — 4 links"},
            {"id": "D", "text": "Partial mesh — 20 links"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Connecting every node directly to every other node is a full mesh. The link "
                       "count is n(n−1)/2 = 5×4/2 = 10 links for 5 sites.",
            "distractors": {
                "B": "5 links is too few for a full mesh of 5 sites; it would leave many pairs "
                     "without a direct link.",
                "C": "Hub-and-spoke uses a central node (4 links for 5 sites), but every spoke's "
                     "traffic must pass through the hub — not a direct link between every pair.",
                "D": "A partial mesh connects only SOME pairs directly; and 20 double-counts each "
                     "link (n(n−1) counts every link twice).",
            },
            "exam_pattern": "Full-mesh links = n(n−1)/2. Full mesh = max redundancy/cost; "
                            "hub-and-spoke hub is a single point of failure.",
        },
    },
    # ===== 2.0 Network Implementation =======================================
    {
        "id": "netplus-ni-r2-001", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A routing protocol has every router build and flood information about its own "
                "links, so each router independently constructs a complete map of the topology and "
                "runs a shortest-path (Dijkstra) calculation. Which CATEGORY of routing protocol "
                "behaves this way?",
        "options": [
            {"id": "A", "text": "Link-state (e.g., OSPF)"},
            {"id": "B", "text": "Distance-vector (e.g., RIP)"},
            {"id": "C", "text": "Path-vector (e.g., BGP)"},
            {"id": "D", "text": "Static routing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Link-state protocols (OSPF, IS-IS) flood link-state advertisements so every "
                       "router has the full topology and runs SPF/Dijkstra to pick best paths.",
            "distractors": {
                "B": "Distance-vector protocols (RIP) share only their routing table with neighbors "
                     "('routing by rumor') and do not build a full topology map.",
                "C": "Path-vector (BGP) chooses paths based on a list of AS hops and policy, not a "
                     "flooded link-state map.",
                "D": "Static routes are manually configured; there is no protocol building a topology.",
            },
            "exam_pattern": "Link-state = full map + SPF (OSPF/IS-IS). Distance-vector = metric from "
                            "neighbors (RIP). Path-vector = AS path (BGP).",
        },
    },
    {
        "id": "netplus-ni-r2-002", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "multi",
        "stem": "A router receives a packet whose destination IP matches NO entry in its routing "
                "table, and the router has no default route configured. Which TWO things does the "
                "router do? (Choose two.)",
        "options": [
            {"id": "A", "text": "Drops (discards) the packet"},
            {"id": "B", "text": "Returns an ICMP Destination Unreachable message to the source"},
            {"id": "C", "text": "Floods the packet out every interface"},
            {"id": "D", "text": "Broadcasts the packet to the local subnet"},
            {"id": "E", "text": "Stores the packet until a matching route appears"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "With no matching route and no default route, the router cannot forward the "
                       "packet: it discards it and typically sends an ICMP 'Destination network "
                       "unreachable' message back to the source.",
            "distractors": {
                "C": "Routers do not flood unknown-destination packets out all interfaces — that is "
                     "unknown-unicast behavior on a Layer 2 switch, not a router.",
                "D": "Routers do not broadcast unroutable packets onto the local subnet.",
                "E": "Routers do not queue packets waiting for a future route; the packet is "
                     "dropped immediately.",
            },
            "exam_pattern": "No route + no default = drop + ICMP unreachable. A default route "
                            "(0.0.0.0/0) is the catch-all that prevents this.",
        },
    },
    {
        "id": "netplus-ni-r2-003", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 3, "type": "mcq",
        "stem": "An administrator configures a backup static route to the same destination as a "
                "primary OSPF-learned route, but gives the static route an administrative distance "
                "HIGHER than OSPF's so it is installed only if the OSPF route disappears. What is "
                "this backup route called?",
        "options": [
            {"id": "A", "text": "Floating static route"},
            {"id": "B", "text": "Default route"},
            {"id": "C", "text": "Summary (aggregate) route"},
            {"id": "D", "text": "Host route"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A floating static route is a static route with an administrative distance set "
                       "higher than the primary route's, so it 'floats' — unused until the preferred "
                       "dynamic route is withdrawn, then it takes over as a backup.",
            "distractors": {
                "B": "A default route (0.0.0.0/0) is the gateway of last resort for unknown "
                     "destinations, not a conditional backup to a specific route.",
                "C": "A summary route aggregates several subnets into one advertisement; it is "
                     "unrelated to AD-based failover.",
                "D": "A host route is a /32 route to a single address, not a backup mechanism.",
            },
            "exam_pattern": "Backup that activates only on primary failure = floating static (raise "
                            "its AD above the primary). Lowest AD wins.",
        },
    },
    {
        "id": "netplus-ni-r2-004", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 1, "type": "mcq",
        "stem": "An administrator divides one physical switch into several VLANs. What is the "
                "PRIMARY networking effect of placing hosts into separate VLANs?",
        "options": [
            {"id": "A", "text": "Each VLAN is a separate broadcast domain, so broadcasts stay within their VLAN"},
            {"id": "B", "text": "Each VLAN becomes its own collision domain for the first time"},
            {"id": "C", "text": "Hosts in different VLANs can communicate without any router"},
            {"id": "D", "text": "All VLANs share a single IP subnet automatically"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VLAN defines a separate broadcast domain. Broadcasts from a host are "
                       "confined to its VLAN, which reduces broadcast traffic and logically "
                       "segments the LAN.",
            "distractors": {
                "B": "Modern switches already place every individual port in its own collision "
                     "domain regardless of VLANs — that is not what VLANs add.",
                "C": "Inter-VLAN traffic requires a Layer 3 device (router or Layer 3 switch); "
                     "VLANs alone isolate, they do not route between themselves.",
                "D": "Each VLAN is normally mapped to its OWN IP subnet, not a shared one.",
            },
            "exam_pattern": "VLAN = one broadcast domain = (usually) one subnet. Moving between "
                            "VLANs needs routing (router-on-a-stick / L3 switch SVIs).",
        },
    },
    {
        "id": "netplus-ni-r2-005", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "mcq",
        "stem": "On an access switch, ports that connect to single end devices (PCs) take about 30 "
                "seconds to begin forwarding because of spanning-tree listening and learning. Which "
                "feature lets such an access port transition straight to forwarding to avoid that "
                "delay?",
        "options": [
            {"id": "A", "text": "PortFast"},
            {"id": "B", "text": "Root guard"},
            {"id": "C", "text": "802.1Q trunking"},
            {"id": "D", "text": "Storm control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PortFast lets an access port skip the STP listening/learning states and move "
                       "immediately to forwarding — appropriate only for ports connected to end "
                       "hosts, not to other switches.",
            "distractors": {
                "B": "Root guard prevents a port from accepting superior BPDUs to become the root "
                     "path; it does not speed up port startup.",
                "C": "802.1Q trunking tags frames to carry multiple VLANs; it is unrelated to STP "
                     "convergence delay on an access port.",
                "D": "Storm control rate-limits broadcast/multicast floods; it does not change STP "
                     "port transition timing.",
            },
            "exam_pattern": "End-device port slow to come up = enable PortFast. Pair PortFast with "
                            "BPDU Guard to shut the port if a switch is plugged in.",
        },
    },
    {
        "id": "netplus-ni-r2-006", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "mcq",
        "stem": "How does an Ethernet switch build and maintain the MAC address (CAM) table it uses "
                "to forward frames?",
        "options": [
            {"id": "A", "text": "It records the SOURCE MAC address and ingress port of each frame it receives"},
            {"id": "B", "text": "It records the DESTINATION MAC address of each frame it receives"},
            {"id": "C", "text": "It copies the ARP cache from the default gateway"},
            {"id": "D", "text": "It reads the source IP address of each packet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A switch learns by inspecting the SOURCE MAC address of incoming frames and "
                       "associating it with the port the frame arrived on. Unknown-destination "
                       "frames are flooded until the destination replies and is learned.",
            "distractors": {
                "B": "The destination MAC is used to FORWARD a frame (table look-up), but learning "
                     "is based on the source MAC.",
                "C": "A switch does not import the gateway's ARP cache; it learns independently from "
                     "frames it sees.",
                "D": "Switches operate at Layer 2 on MAC addresses, not Layer 3 IP addresses.",
            },
            "exam_pattern": "Switch LEARNS from source MAC (+ port), FORWARDS by destination MAC, "
                            "FLOODS unknown unicast/broadcast within the VLAN.",
        },
    },
    {
        "id": "netplus-ni-r2-007", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "mcq",
        "stem": "A vendor advertises new 'Wi-Fi 6E' access points as an extension of Wi-Fi 6 "
                "(802.11ax). What is the key difference that the 'E' designation adds?",
        "options": [
            {"id": "A", "text": "Operation in the newly opened 6 GHz frequency band"},
            {"id": "B", "text": "A new modulation that doubles range in the 2.4 GHz band"},
            {"id": "C", "text": "Mandatory WEP encryption for backward compatibility"},
            {"id": "D", "text": "Support for infrared line-of-sight links"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Wi-Fi 6E extends Wi-Fi 6 (802.11ax) into the 6 GHz band, adding a large "
                       "amount of new, less-congested spectrum alongside the existing 2.4 GHz and "
                       "5 GHz bands.",
            "distractors": {
                "B": "Wi-Fi 6E uses the same 802.11ax technology; the gain is new 6 GHz spectrum, "
                     "not a 2.4 GHz range-doubling modulation.",
                "C": "WEP is deprecated and insecure; Wi-Fi 6E uses WPA3 and certainly does not "
                     "mandate WEP.",
                "D": "Wi-Fi is radio-based; infrared line-of-sight is unrelated to 802.11ax/6E.",
            },
            "exam_pattern": "Wi-Fi 5 (ac)=5 GHz; Wi-Fi 6 (ax)=2.4+5 GHz; Wi-Fi 6E (ax)=adds 6 GHz. "
                            "WPA3 is the matching security.",
        },
    },
    {
        "id": "netplus-ni-r2-008", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 2, "type": "mcq",
        "stem": "An engineer needs a dedicated point-to-point wireless bridge between two buildings "
                "about 1 km apart, concentrating the signal in a narrow beam for maximum range. "
                "Which antenna type is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Directional (e.g., Yagi or parabolic dish)"},
            {"id": "B", "text": "Omnidirectional (dipole)"},
            {"id": "C", "text": "A chip/PCB antenna inside the AP"},
            {"id": "D", "text": "An isotropic reference antenna"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A directional antenna (Yagi, panel, or parabolic dish) focuses RF energy "
                       "into a narrow high-gain beam aimed at the far end — ideal for a long "
                       "point-to-point building-to-building link.",
            "distractors": {
                "B": "An omnidirectional antenna radiates 360° horizontally for area coverage, "
                     "wasting energy in all directions instead of toward one distant point.",
                "C": "A small internal chip antenna is low-gain and intended for nearby clients, "
                     "not a 1 km link.",
                "D": "An isotropic antenna is a theoretical point radiator used only as a gain "
                     "reference (dBi); it is not a real product.",
            },
            "exam_pattern": "Point-to-point/long distance = directional (Yagi/parabolic/panel). "
                            "Area coverage for many clients = omnidirectional.",
        },
    },
    {
        "id": "netplus-ni-r2-009", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 1, "type": "mcq",
        "stem": "A client adapter supports 802.11ac (Wi-Fi 5). In which frequency band does "
                "802.11ac operate?",
        "options": [
            {"id": "A", "text": "5 GHz only"},
            {"id": "B", "text": "2.4 GHz only"},
            {"id": "C", "text": "900 MHz only"},
            {"id": "D", "text": "6 GHz only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.11ac (Wi-Fi 5) operates exclusively in the 5 GHz band, which offers more "
                       "non-overlapping channels and higher throughput than 2.4 GHz.",
            "distractors": {
                "B": "2.4 GHz is used by 802.11b/g/n (and ax); 802.11ac does not operate there.",
                "C": "900 MHz is used by some IoT/legacy gear, not by 802.11ac Wi-Fi.",
                "D": "The 6 GHz band is used by Wi-Fi 6E/7, not by 802.11ac.",
            },
            "exam_pattern": "802.11b/g = 2.4; a/ac = 5 GHz; n/ax = both 2.4 & 5; 6E/be add 6 GHz.",
        },
    },
    {
        "id": "netplus-ni-r2-010", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "Inside a data center, 10 Gbps links run up to a few hundred meters between rows "
                "using inexpensive transceivers with an 850 nm VCSEL light source. Which fiber type "
                "is designed for these short-reach, lower-cost runs?",
        "options": [
            {"id": "A", "text": "Multimode fiber (e.g., OM3/OM4)"},
            {"id": "B", "text": "Single-mode fiber (OS1/OS2)"},
            {"id": "C", "text": "Category 6a UTP copper"},
            {"id": "D", "text": "RG-6 coaxial cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multimode fiber (OM3/OM4) with 850 nm VCSEL optics is the cost-effective "
                       "choice for short-to-medium data-center runs (hundreds of meters). Its larger "
                       "core suits inexpensive LED/VCSEL sources.",
            "distractors": {
                "B": "Single-mode fiber uses a narrow core and laser optics for very long distances "
                     "(km); it is more expensive and overkill for short in-row runs.",
                "C": "Cat 6a is copper, not fiber, and tops out at 100 m — not a fiber transceiver "
                     "medium.",
                "D": "RG-6 coax carries RF/video (e.g., cable TV), not 10 Gbps data-center optical "
                     "links.",
            },
            "exam_pattern": "Short reach, cheap, 850 nm VCSEL = multimode (OM3/OM4). Long haul, "
                            "laser, km = single-mode (OS2).",
        },
    },
    {
        "id": "netplus-ni-r2-011", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 1, "type": "mcq",
        "stem": "A technician plans a horizontal twisted-pair Ethernet run (e.g., Cat 6). To stay "
                "within TIA/EIA specification, what is the maximum total channel length the run "
                "must not exceed?",
        "options": [
            {"id": "A", "text": "100 meters (about 328 feet)"},
            {"id": "B", "text": "55 meters"},
            {"id": "C", "text": "185 meters"},
            {"id": "D", "text": "500 meters"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Balanced twisted-pair Ethernet is specified to a 100 m channel — typically "
                       "90 m of fixed horizontal cable plus up to 10 m of patch cords. Beyond that, "
                       "signal attenuation causes errors.",
            "distractors": {
                "B": "55 m is a reduced limit that can apply to 10GBASE-T over Cat 6 in "
                     "high-interference conditions, not the general copper maximum.",
                "C": "185 m is the legacy 10BASE2 'thinnet' coax distance, not a twisted-pair limit.",
                "D": "500 m is the legacy 10BASE5 'thicknet' coax distance — obsolete coax, not a "
                     "UTP channel length.",
            },
            "exam_pattern": "UTP Ethernet channel limit = 100 m (90 m horizontal + 10 m patch). "
                            "Need farther? Use fiber.",
        },
    },
    # ===== 3.0 Network Operations ===========================================
    {
        "id": "netplus-nops-r2-001", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 2, "type": "mcq",
        "stem": "A network architect produces a diagram that shows IP subnets, VLAN IDs, routing "
                "boundaries, and how data flows between segments — but deliberately omits which "
                "physical port or cable connects each device. Which type of documentation is this?",
        "options": [
            {"id": "A", "text": "Logical network diagram"},
            {"id": "B", "text": "Physical network diagram"},
            {"id": "C", "text": "Rack elevation diagram"},
            {"id": "D", "text": "Wiring (cut-sheet) schedule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A logical diagram depicts the network in terms of IP addressing, subnets, "
                       "VLANs, and routing/traffic relationships — the 'how it works' view — "
                       "independent of physical cabling.",
            "distractors": {
                "B": "A physical diagram shows the actual devices, ports, and cable runs — exactly "
                     "the detail this diagram omits.",
                "C": "A rack elevation shows the mounting position (RU) of equipment in a rack, not "
                     "IP/VLAN logic.",
                "D": "A wiring/cut-sheet schedule lists cable terminations and labels, which is "
                     "physical cabling detail.",
            },
            "exam_pattern": "Logical = IP/VLAN/routing/flow. Physical = devices/ports/cables/rack "
                            "positions.",
        },
    },
    {
        "id": "netplus-nops-r2-002", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 2, "type": "mcq",
        "stem": "Before investigating complaints that the network 'feels slow,' an engineer "
                "compares current throughput, latency, and utilization against measurements "
                "recorded months ago when performance was known to be healthy. What is that "
                "reference set of measurements called?",
        "options": [
            {"id": "A", "text": "A performance baseline"},
            {"id": "B", "text": "A service-level agreement (SLA)"},
            {"id": "C", "text": "A change log"},
            {"id": "D", "text": "An audit report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A baseline is a recorded snapshot of normal performance. Comparing current "
                       "metrics to the baseline reveals deviations (e.g., rising utilization or "
                       "latency) that point to the problem.",
            "distractors": {
                "B": "An SLA defines committed service levels/penalties with a provider — a contract "
                     "target, not a measured snapshot of normal behavior.",
                "C": "A change log records configuration changes over time; it does not capture "
                     "performance metrics.",
                "D": "An audit report evaluates compliance/controls, not day-to-day throughput and "
                     "latency norms.",
            },
            "exam_pattern": "'Compare to normal' = baseline. Deviation from baseline = where to "
                            "investigate. Capture baselines before problems occur.",
        },
    },
    {
        "id": "netplus-nops-r2-003", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "To let a protocol analyzer capture all traffic passing through a particular switch "
                "port, a technician configures the switch to copy that port's frames to the port "
                "where the analyzer is connected. What is this switch feature called?",
        "options": [
            {"id": "A", "text": "Port mirroring (SPAN)"},
            {"id": "B", "text": "Port security"},
            {"id": "C", "text": "Link aggregation (LACP)"},
            {"id": "D", "text": "Power over Ethernet (PoE)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Port mirroring (Cisco calls it SPAN) copies frames from one or more source "
                       "ports (or a VLAN) to a destination/monitor port so an analyzer or IDS can "
                       "inspect traffic without being inline.",
            "distractors": {
                "B": "Port security restricts which MAC addresses may use a port; it does not copy "
                     "traffic for capture.",
                "C": "Link aggregation bonds multiple links into one logical link for "
                     "bandwidth/redundancy; it is not a capture mechanism.",
                "D": "PoE delivers electrical power over the Ethernet cable; it has nothing to do "
                     "with mirroring traffic.",
            },
            "exam_pattern": "Feed an analyzer/IDS a copy of traffic = port mirroring/SPAN. A "
                            "hardware alternative is a passive network TAP.",
        },
    },
    {
        "id": "netplus-nops-r2-004", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "A service contract promises '99.999% (five nines) availability.' Approximately how "
                "much total downtime per year does that allow?",
        "options": [
            {"id": "A", "text": "About 5 minutes"},
            {"id": "B", "text": "About 8.8 hours"},
            {"id": "C", "text": "About 53 minutes"},
            {"id": "D", "text": "About 1 minute"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A year is about 525,600 minutes. 0.001% of that (100% − 99.999%) is roughly "
                       "5.26 minutes of allowed downtime per year — the well-known 'five nines' "
                       "figure.",
            "distractors": {
                "B": "About 8.8 hours/year corresponds to 99.9% (three nines), not five nines.",
                "C": "About 52.6 minutes/year corresponds to 99.99% (four nines).",
                "D": "About 1 minute/year would be roughly six nines (99.9999%), stricter than the "
                     "stated target.",
            },
            "exam_pattern": "Downtime/yr: 99.9% ≈ 8.8 h, 99.99% ≈ 52 min, 99.999% ≈ 5 min. Each "
                            "extra nine ≈ 10× less downtime.",
        },
    },
    {
        "id": "netplus-nops-r2-005", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A company's recovery plan designates an alternate facility that has floor space, "
                "power, and network connectivity but NO installed servers or current data; "
                "equipment must be delivered and configured before operations can resume, taking "
                "days. Which recovery site type is this?",
        "options": [
            {"id": "A", "text": "Cold site"},
            {"id": "B", "text": "Hot site"},
            {"id": "C", "text": "Warm site"},
            {"id": "D", "text": "Active-active cloud site"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cold site provides the environment (space, power, cooling, connectivity) "
                       "but no ready equipment or data. It is the cheapest option but has the "
                       "longest recovery time.",
            "distractors": {
                "B": "A hot site is fully equipped and continuously updated with near-real-time "
                     "data, enabling almost immediate failover — the opposite of this.",
                "C": "A warm site has some equipment pre-staged and only periodic data, so it "
                     "activates faster than a cold site.",
                "D": "An active-active cloud site serves live traffic already; there is no 'deliver "
                     "equipment' delay.",
            },
            "exam_pattern": "Cold = empty shell (cheap, slow). Warm = partial gear/stale data. "
                            "Hot = ready + live data (costly, fast).",
        },
    },
    {
        "id": "netplus-nops-r2-006", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A backup job captures all data that has changed since the last FULL backup, "
                "regardless of any backups taken on the nights in between. Which backup type is "
                "this?",
        "options": [
            {"id": "A", "text": "Differential backup"},
            {"id": "B", "text": "Incremental backup"},
            {"id": "C", "text": "Full backup"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A differential backup copies everything changed since the last FULL backup. "
                       "Differentials grow each day, but a restore needs only the last full plus the "
                       "latest differential.",
            "distractors": {
                "B": "An incremental backup copies only what changed since the last backup of ANY "
                     "type, so a restore needs the full plus EVERY incremental in order.",
                "C": "A full backup copies all data every time, independent of change tracking.",
                "D": "A snapshot is a point-in-time image (often at the storage/VM layer), not the "
                     "'since last full' change set described.",
            },
            "exam_pattern": "Differential = since last FULL (restore: full + last diff). Incremental "
                            "= since last ANY backup (restore: full + all increments).",
        },
    },
    {
        "id": "netplus-nops-r2-007", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A backup administrator wants to follow the widely recommended '3-2-1' backup "
                "strategy. Which practice does the 3-2-1 rule describe?",
        "options": [
            {"id": "A", "text": "Keep 3 copies of data, on 2 different media types, with 1 copy stored offsite"},
            {"id": "B", "text": "Run 3 full backups, 2 incrementals, and 1 differential each week"},
            {"id": "C", "text": "Retain backups for 3 years, test them 2 times, and encrypt 1 copy"},
            {"id": "D", "text": "Keep 3 offsite copies, 2 onsite copies, and 1 in the cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 3-2-1 rule means: maintain at least 3 copies of your data, store them on "
                       "2 different types of media, and keep 1 copy offsite — protecting against "
                       "device, media, and site-level loss.",
            "distractors": {
                "B": "3-2-1 is about copies/media/location, not a schedule of "
                     "full/incremental/differential jobs.",
                "C": "Retention periods, testing counts, and encryption are good practices but not "
                     "what 3-2-1 specifies.",
                "D": "The '1' refers to a single OFFSITE copy; the rule does not prescribe three "
                     "offsite copies.",
            },
            "exam_pattern": "3-2-1 = 3 copies, 2 media, 1 offsite. It guards against single points "
                            "of failure in storage and location.",
        },
    },
    {
        "id": "netplus-nops-r2-008", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 2, "type": "multi",
        "stem": "A mail server must deliver a message to user@example.com. Which TWO DNS record "
                "types does it rely on to find the destination mail host and its IP address? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "MX record"},
            {"id": "B", "text": "A (or AAAA) record"},
            {"id": "C", "text": "CNAME record"},
            {"id": "D", "text": "PTR record"},
            {"id": "E", "text": "TXT record"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "The sender first queries the MX record to learn the name of the domain's "
                       "mail exchanger, then resolves that hostname's A (IPv4) or AAAA (IPv6) record "
                       "to get the IP address to connect to.",
            "distractors": {
                "C": "A CNAME is an alias to another name; MX targets are supposed to point to real "
                     "A/AAAA records, and using CNAMEs for MX targets is discouraged.",
                "D": "A PTR record maps an IP back to a name (reverse DNS) — used for "
                     "verification/anti-spam, not to locate the mail host initially.",
                "E": "A TXT record holds text such as SPF/DKIM policy; it does not provide the mail "
                     "host's address.",
            },
            "exam_pattern": "Mail delivery: MX (which host) → A/AAAA (its IP). PTR = reverse "
                            "(IP→name). TXT = SPF/DKIM.",
        },
    },
    {
        "id": "netplus-nops-r2-009", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 2, "type": "mcq",
        "stem": "Newly arriving laptops on a subnet fail to obtain an address and end up "
                "self-assigning 169.254.x.x, while devices that connected earlier in the day keep "
                "working normally. The DHCP server and relay are reachable. What is the MOST likely "
                "cause?",
        "options": [
            {"id": "A", "text": "The DHCP scope has run out of available addresses (pool exhaustion)"},
            {"id": "B", "text": "DNS is misconfigured on the server"},
            {"id": "C", "text": "The switch uplink is using a crossover cable"},
            {"id": "D", "text": "The clients need a static default gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Earlier clients hold valid leases and work; new clients cannot get one and "
                       "fall back to APIPA (169.254). That pattern means the DHCP pool has no free "
                       "addresses left — scope exhaustion. Widen the scope or shorten lease times.",
            "distractors": {
                "B": "A DNS problem would break NAME resolution for everyone, not stop NEW clients "
                     "from getting an IP while existing ones keep working.",
                "C": "A crossover-vs-straight cabling issue would break the link entirely, not "
                     "selectively deny only new DHCP clients.",
                "D": "APIPA appears precisely because DHCP failed; manually setting a gateway is a "
                     "workaround, not the cause, and does not explain the pattern.",
            },
            "exam_pattern": "New clients get 169.254 while existing clients are fine = DHCP scope "
                            "exhausted. Fix: enlarge pool / lower lease time.",
        },
    },
    {
        "id": "netplus-nops-r2-010", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 2, "type": "mcq",
        "stem": "In SNMPv1/v2c, what controls whether a management station is allowed to read (or "
                "write) a device's data, and why is it a security concern?",
        "options": [
            {"id": "A", "text": "A community string, which is sent in clear text"},
            {"id": "B", "text": "A Kerberos ticket, which expires quickly"},
            {"id": "C", "text": "An X.509 certificate signed by a CA"},
            {"id": "D", "text": "A TACACS+ shared secret over TCP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SNMPv1/v2c use a community string as a simple shared password (commonly "
                       "'public'/'private'). It travels in clear text, so anyone who captures it can "
                       "query or alter the device — which is why SNMPv3 (authentication + "
                       "encryption) is preferred.",
            "distractors": {
                "B": "SNMPv1/v2c do not use Kerberos tickets.",
                "C": "Community-string SNMP does not use X.509 certificates; that is unrelated to "
                     "v2c access control.",
                "D": "TACACS+ is an AAA protocol for device administration, not the SNMP access "
                     "mechanism.",
            },
            "exam_pattern": "v2c = community string (plaintext, weak). v3 = usernames + "
                            "authentication + encryption. Harden by moving to v3.",
        },
    },
    {
        "id": "netplus-nops-r2-011", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 2, "type": "mcq",
        "stem": "An administrator configures every router, switch, and firewall to forward its logs "
                "to one central syslog server. Besides convenience, what is a KEY operational and "
                "security benefit of this design?",
        "options": [
            {"id": "A", "text": "Logs are aggregated for correlation and preserved even if a device is compromised or fails"},
            {"id": "B", "text": "It eliminates the need to synchronize device clocks"},
            {"id": "C", "text": "It automatically encrypts all production data in transit"},
            {"id": "D", "text": "It prevents devices from ever generating log messages locally"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Centralized logging lets you correlate events across devices in one place "
                       "and keeps a copy off the device, so logs survive a device failure or an "
                       "attacker who wipes local logs to cover their tracks.",
            "distractors": {
                "B": "Centralizing logs does NOT remove the need for time sync — accurate "
                     "correlation still depends on NTP keeping timestamps aligned.",
                "C": "Syslog forwarding is not automatic encryption of production data; plain syslog "
                     "is often sent in clear text (use TLS to protect it).",
                "D": "Devices can still log locally; forwarding adds a central copy, it does not "
                     "stop local logging.",
            },
            "exam_pattern": "Central syslog = correlation + tamper-resistant off-box copy. Still "
                            "requires NTP for consistent timestamps.",
        },
    },
    # ===== 4.0 Network Security =============================================
    {
        "id": "netplus-nsec-r2-001", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise needs an AAA protocol to authenticate users connecting through "
                "802.1X and VPNs. It wants an open, vendor-neutral standard that is widely "
                "interoperable. Which protocol fits — and what is one of its characteristics?",
        "options": [
            {"id": "A", "text": "RADIUS — an open standard that uses UDP and encrypts only the password in the access-request"},
            {"id": "B", "text": "TACACS+ — an open standard that encrypts the entire packet"},
            {"id": "C", "text": "RADIUS — a Cisco-proprietary protocol that uses TCP"},
            {"id": "D", "text": "Kerberos — a protocol that issues reusable clear-text tickets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RADIUS is the open (IETF) AAA standard typically used for network access "
                       "(802.1X, VPN, Wi-Fi). It runs over UDP and encrypts only the user's password "
                       "field, not the whole packet.",
            "distractors": {
                "B": "TACACS+ does encrypt the entire packet, but it is Cisco-developed and is used "
                     "mainly for device administration — not the open 802.1X network-access "
                     "standard described.",
                "C": "RADIUS is NOT Cisco-proprietary and uses UDP, not TCP (TACACS+ uses TCP).",
                "D": "Kerberos is ticket-based, but its tickets are encrypted, not clear text, and "
                     "it is not the 802.1X/VPN AAA protocol here.",
            },
            "exam_pattern": "RADIUS = open, UDP, encrypts only password, network access. TACACS+ = "
                            "Cisco, TCP, full-packet encryption, device admin, separates A/A/A.",
        },
    },
    {
        "id": "netplus-nsec-r2-002", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "A security team deploys a deliberately vulnerable-looking server that holds no "
                "real data, purely to lure attackers, observe their techniques, and divert them "
                "from production systems. What is this called?",
        "options": [
            {"id": "A", "text": "Honeypot"},
            {"id": "B", "text": "Jump box"},
            {"id": "C", "text": "Screened subnet (DMZ)"},
            {"id": "D", "text": "Proxy server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A honeypot is a decoy system designed to attract and study attackers and to "
                       "distract them from real assets. A larger decoy network is a honeynet.",
            "distractors": {
                "B": "A jump box is a hardened host administrators use to reach protected systems — "
                     "not a decoy for attackers.",
                "C": "A screened subnet (DMZ) hosts real, Internet-facing production services behind "
                     "layered firewalls; it is not a decoy.",
                "D": "A proxy forwards/filters client requests; it is not bait for attackers.",
            },
            "exam_pattern": "Decoy to attract/study attackers = honeypot (honeynet = multiple). "
                            "Distract + detect, not protect real data.",
        },
    },
    {
        "id": "netplus-nsec-r2-003", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 1, "type": "mcq",
        "stem": "A company's public web server suddenly becomes unreachable because it is "
                "overwhelmed by a massive flood of traffic coming simultaneously from tens of "
                "thousands of compromised devices around the world. Which attack is occurring?",
        "options": [
            {"id": "A", "text": "Distributed denial-of-service (DDoS)"},
            {"id": "B", "text": "On-path (man-in-the-middle) attack"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "ARP spoofing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Many compromised hosts (a botnet) flooding a target to exhaust its bandwidth "
                       "or resources and deny service is a DDoS. The 'distributed' part is the many "
                       "simultaneous sources.",
            "distractors": {
                "B": "An on-path attack intercepts/alters traffic between two parties; it does not "
                     "flood a server offline.",
                "C": "SQL injection manipulates database queries through input fields; it is not a "
                     "traffic flood.",
                "D": "ARP spoofing poisons the local ARP cache to redirect LAN traffic — a local "
                     "technique, not a global traffic flood.",
            },
            "exam_pattern": "Many sources + availability loss = DDoS (single source = DoS). Mitigate "
                            "with upstream scrubbing, rate limiting, and CDNs.",
        },
    },
    {
        "id": "netplus-nsec-r2-004", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 1, "type": "mcq",
        "stem": "During hardening of an access switch in a public lobby, a technician wants to stop "
                "anyone from plugging an unauthorized device into a wall jack and gaining network "
                "access. Which simple, effective measure addresses unused jacks?",
        "options": [
            {"id": "A", "text": "Administratively disable (shut down) all switch ports that are not in use"},
            {"id": "B", "text": "Enable the clear-text HTTP management interface on the switch"},
            {"id": "C", "text": "Leave every port assigned to the default VLAN 1"},
            {"id": "D", "text": "Increase the STP forwarding delay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shutting down unused ports means a device plugged into an idle jack gets no "
                       "link and no access. It is a core hardening step that shrinks the attack "
                       "surface at the access layer.",
            "distractors": {
                "B": "Enabling clear-text HTTP management WEAKENS security; it does nothing to "
                     "protect unused jacks.",
                "C": "Leaving ports on default VLAN 1 is discouraged and does nothing to block "
                     "unauthorized use of idle jacks.",
                "D": "STP forwarding delay affects loop-convergence timing, not whether an unused "
                     "jack grants access.",
            },
            "exam_pattern": "Idle jacks = disable the ports (and/or use 802.1X / port security). "
                            "Avoid default VLAN 1 and clear-text management.",
        },
    },
    {
        "id": "netplus-nsec-r2-005", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 3, "type": "mcq",
        "stem": "Access ports connecting to end-user PCs have PortFast enabled. To ensure that if "
                "someone plugs a rogue switch into one of these ports it cannot inject BPDUs and "
                "disrupt the spanning tree, which feature should be enabled on those ports?",
        "options": [
            {"id": "A", "text": "BPDU Guard"},
            {"id": "B", "text": "DHCP snooping"},
            {"id": "C", "text": "Dynamic ARP Inspection (DAI)"},
            {"id": "D", "text": "Port Aggregation Protocol (PAgP)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BPDU Guard err-disables a PortFast access port the instant it receives any "
                       "BPDU, so a rogue switch plugged into a user port is shut down rather than "
                       "allowed to influence STP (e.g., become root).",
            "distractors": {
                "B": "DHCP snooping blocks rogue DHCP servers; it does not react to spanning-tree "
                     "BPDUs.",
                "C": "DAI validates ARP packets to stop ARP spoofing; it is unrelated to BPDUs and "
                     "STP.",
                "D": "PAgP negotiates EtherChannel bundles; it does not protect against rogue BPDUs.",
            },
            "exam_pattern": "PortFast + BPDU Guard on user access ports: any BPDU received = port "
                            "err-disabled. Protects the STP root/topology from rogue switches.",
        },
    },
    {
        "id": "netplus-nsec-r2-006", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 1, "type": "mcq",
        "stem": "A technician racks several brand-new switches and APs, each shipping with the "
                "well-known factory login admin/admin. What is the FIRST hardening action before "
                "connecting them to the network?",
        "options": [
            {"id": "A", "text": "Change the default administrative credentials"},
            {"id": "B", "text": "Enable Telnet for easier remote access"},
            {"id": "C", "text": "Open all firewall ports to simplify setup"},
            {"id": "D", "text": "Leave SNMP set to the default 'public' community"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Default credentials are published and are among the first things attackers "
                       "try. Changing them (and disabling unused default accounts) is a basic, "
                       "essential hardening step on any new device.",
            "distractors": {
                "B": "Telnet sends credentials in clear text; enabling it weakens security — use "
                     "SSH instead.",
                "C": "Opening all firewall ports maximizes the attack surface — the opposite of "
                     "hardening.",
                "D": "Leaving SNMP at 'public' is a classic vulnerability that must be changed or "
                     "disabled, not kept.",
            },
            "exam_pattern": "New gear: change default passwords first, disable default/unused "
                            "accounts and clear-text services (Telnet, SNMP 'public').",
        },
    },
    {
        "id": "netplus-nsec-r2-007", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 2, "type": "mcq",
        "stem": "Remote users need access to a handful of internal WEB applications from any "
                "computer — including kiosks — without installing any VPN software. They connect to "
                "an HTTPS portal and reach the apps through the browser. Which remote-access "
                "solution is this?",
        "options": [
            {"id": "A", "text": "Clientless SSL/TLS VPN (browser-based portal)"},
            {"id": "B", "text": "Site-to-site IPsec VPN"},
            {"id": "C", "text": "A full-tunnel IPsec client VPN"},
            {"id": "D", "text": "A dial-up RAS connection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A clientless SSL VPN uses the browser's built-in TLS to present an HTTPS "
                       "portal to internal web resources, so no VPN client needs to be installed — "
                       "convenient for untrusted or shared machines.",
            "distractors": {
                "B": "A site-to-site VPN permanently links two networks' gateways; it is not a "
                     "per-user, browser-based access method.",
                "C": "A full-tunnel IPsec client VPN requires installed client software and sends "
                     "all traffic through the tunnel — the opposite of 'no install, web apps only.'",
                "D": "Dial-up RAS uses phone lines/modems and is obsolete; it is unrelated to a "
                     "browser HTTPS portal.",
            },
            "exam_pattern": "No client, browser to web apps over HTTPS = clientless SSL VPN. "
                            "Installed client, full network access = IPsec client VPN.",
        },
    },
    {
        "id": "netplus-nsec-r2-008", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 3, "type": "mcq",
        "stem": "Two offices build a site-to-site VPN across the public Internet. The requirement "
                "is that each original IP packet — including its ORIGINAL source and destination "
                "headers — be fully encrypted and encapsulated inside a new packet between the VPN "
                "gateways. Which IPsec mode accomplishes this?",
        "options": [
            {"id": "A", "text": "Tunnel mode"},
            {"id": "B", "text": "Transport mode"},
            {"id": "C", "text": "Aggressive mode"},
            {"id": "D", "text": "Split-tunnel mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IPsec tunnel mode encrypts the entire original IP packet (header and "
                       "payload) and wraps it in a new IP header addressed gateway-to-gateway — the "
                       "standard choice for site-to-site VPNs over the Internet.",
            "distractors": {
                "B": "Transport mode encrypts only the payload and keeps the original IP header; it "
                     "is used host-to-host, not for gateway-to-gateway tunnels that must hide "
                     "internal addresses.",
                "C": "Aggressive mode is an IKE phase-1 negotiation option (fewer messages), not a "
                     "data-encapsulation mode for packets.",
                "D": "Split tunneling is a client routing policy (some traffic in the tunnel, some "
                     "direct); it is not an IPsec encapsulation mode.",
            },
            "exam_pattern": "Tunnel mode = whole packet + new header (site-to-site). Transport mode "
                            "= payload only, original header kept (host-to-host).",
        },
    },
    {
        "id": "netplus-nsec-r2-009", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 2, "type": "multi",
        "stem": "A network team sets up out-of-band (OOB) management for its core devices. Which "
                "TWO statements correctly describe out-of-band management? (Choose two.)",
        "options": [
            {"id": "A", "text": "It uses a separate, dedicated path (e.g., a console server or cellular modem) independent of the production network"},
            {"id": "B", "text": "It remains usable to reach devices even when the production data network is down"},
            {"id": "C", "text": "It relies on the same production links that carry user traffic"},
            {"id": "D", "text": "It eliminates the need to authenticate administrators"},
            {"id": "E", "text": "It is only possible over the Internet, with no local option"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Out-of-band management reaches devices over a dedicated channel separate "
                       "from production traffic (console servers, dedicated management ports, "
                       "cellular/4G), so administrators retain access during an outage that has "
                       "taken the data network down.",
            "distractors": {
                "C": "Using the same production links is IN-band management — the opposite of "
                     "out-of-band.",
                "D": "OOB still requires authentication/authorization; it changes the PATH, not the "
                     "need for access control.",
                "E": "OOB is typically a local/dedicated path (serial console, management network); "
                     "it is not limited to the Internet.",
            },
            "exam_pattern": "OOB = separate path, works when the main network is down (console "
                            "server/cellular). In-band = rides production links.",
        },
    },
    {
        "id": "netplus-nsec-r2-010", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 2, "type": "mcq",
        "stem": "A data center door is opened when staff tap an issued proximity card against a "
                "reader, and the system records each entry against the specific badge used. Which "
                "physical security control is described?",
        "options": [
            {"id": "A", "text": "An electronic badge/proximity-card access control system"},
            {"id": "B", "text": "A biometric retina scanner"},
            {"id": "C", "text": "A bollard"},
            {"id": "D", "text": "A Faraday cage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A proximity-card/badge reader is an electronic access control: it grants "
                       "entry based on 'something you have' (the card) and logs who entered and "
                       "when, supporting auditing.",
            "distractors": {
                "B": "A biometric scanner authenticates 'something you are' (a physical trait), not "
                     "a tapped card.",
                "C": "A bollard is a sturdy post that blocks vehicles; it is not a door-access "
                     "credential system.",
                "D": "A Faraday cage blocks electromagnetic signals (RF shielding); it is not an "
                     "entry-control mechanism.",
            },
            "exam_pattern": "Tap card + per-badge logging = electronic access control (have). "
                            "Biometric = are. PIN pad = know.",
        },
    },
    {
        "id": "netplus-nsec-r2-011", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "Network switches are installed in an open equipment rack in a shared office area "
                "used by several tenants. Which simple physical control best prevents passersby "
                "from tampering with or stealing the devices?",
        "options": [
            {"id": "A", "text": "A lockable, enclosed equipment rack/cabinet"},
            {"id": "B", "text": "A longer DHCP lease time"},
            {"id": "C", "text": "A stronger Wi-Fi password"},
            {"id": "D", "text": "An additional VLAN for management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A locking, enclosed rack or cabinet physically denies casual access to the "
                       "equipment, preventing tampering, cable pulls, and theft in a shared space.",
            "distractors": {
                "B": "DHCP lease time is an addressing setting; it offers no physical protection for "
                     "the hardware.",
                "C": "A Wi-Fi password protects wireless access, not the physical switches in the "
                     "rack.",
                "D": "A management VLAN is a logical control; it does not stop someone from "
                     "physically touching or removing the devices.",
            },
            "exam_pattern": "Protect equipment in shared/open spaces = lock the rack/cabinet (and "
                            "the room). Logical controls don't stop physical tampering.",
        },
    },
    {
        "id": "netplus-nsec-r2-012", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "An organization installs tall anti-climb perimeter fencing around its facility "
                "grounds. What is the PRIMARY security purpose of this control?",
        "options": [
            {"id": "A", "text": "To deter and delay intruders at the property boundary"},
            {"id": "B", "text": "To encrypt data leaving the building"},
            {"id": "C", "text": "To authenticate employees entering the building"},
            {"id": "D", "text": "To detect malware on the network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Perimeter fencing is a physical boundary control that deters casual "
                       "intrusion and delays a determined intruder, buying time for detection and "
                       "response. Height and anti-climb features increase the delay.",
            "distractors": {
                "B": "Fencing is physical; it has nothing to do with encrypting data in transit.",
                "C": "Authenticating employees is done by badge readers/biometrics at entry points, "
                     "not by a perimeter fence.",
                "D": "Malware detection is a logical/endpoint control, unrelated to a physical fence.",
            },
            "exam_pattern": "Fencing/lighting/signage = deter + delay at the perimeter. Layer with "
                            "gates, guards, cameras (detect) and vestibules (prevent tailgating).",
        },
    },
    # ===== 5.0 Network Troubleshooting ======================================
    {
        "id": "netplus-nt-r2-001", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 2, "type": "mcq",
        "stem": "Using the CompTIA seven-step troubleshooting methodology, a technician has "
                "established AND confirmed a theory of probable cause. According to the model, what "
                "is the NEXT step?",
        "options": [
            {"id": "A", "text": "Establish a plan of action to resolve the problem"},
            {"id": "B", "text": "Document the findings and outcomes"},
            {"id": "C", "text": "Identify the problem"},
            {"id": "D", "text": "Verify full system functionality"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The order is: identify the problem → establish a theory → TEST the theory → "
                       "(once confirmed) establish a plan of action → implement → verify full "
                       "functionality + preventive measures → document. After confirming the theory, "
                       "you build the plan of action.",
            "distractors": {
                "B": "Documenting findings is the FINAL step, done after implementing, verifying, "
                     "and ensuring the fix holds.",
                "C": "Identifying the problem is the FIRST step, already completed before a theory "
                     "could be formed.",
                "D": "Verifying full functionality comes AFTER you implement the solution, not "
                     "immediately after confirming the theory.",
            },
            "exam_pattern": "7 steps: Identify → Theory → Test theory → Plan of action → Implement → "
                            "Verify (+ preventive) → Document.",
        },
    },
    {
        "id": "netplus-nt-r2-002", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 1, "type": "mcq",
        "stem": "A technician has fixed an outage and confirmed everything works. What is the final "
                "step of the CompTIA troubleshooting methodology, and why does it matter?",
        "options": [
            {"id": "A", "text": "Document the findings, actions, and outcomes — so the knowledge aids future troubleshooting"},
            {"id": "B", "text": "Escalate the ticket to a senior engineer for a second opinion"},
            {"id": "C", "text": "Immediately close the ticket with no notes to save time"},
            {"id": "D", "text": "Reboot every device on the network to be safe"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The last step is to document findings, actions, and outcomes. Good "
                       "documentation builds a knowledge base, speeds future diagnosis of similar "
                       "issues, and records what changed.",
            "distractors": {
                "B": "Escalation happens when YOU cannot resolve or verify a theory — not after the "
                     "problem is already fixed and verified.",
                "C": "Closing with no notes defeats the purpose; the methodology explicitly ends "
                     "with documentation.",
                "D": "Rebooting everything is unnecessary and risky after a verified fix; it is not "
                     "a methodology step.",
            },
            "exam_pattern": "Final step = document. Verify functionality (and implement preventive "
                            "measures) comes just before documenting.",
        },
    },
    {
        "id": "netplus-nt-r2-003", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "A technician terminates a new UTP cable and tests it with a wiremap tester. Seven "
                "pins show continuity, but pin 4 shows no connection from end to end. What fault "
                "does this indicate?",
        "options": [
            {"id": "A", "text": "An open (a broken or unterminated conductor on pin 4)"},
            {"id": "B", "text": "A short between two conductors"},
            {"id": "C", "text": "A split pair"},
            {"id": "D", "text": "Excessive crosstalk from EMI"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "No continuity on a single conductor from end to end is an 'open' — the wire "
                       "is broken, not seated in the jack/plug, or not punched down. Re-terminate or "
                       "replace the cable.",
            "distractors": {
                "B": "A short is when two conductors are connected to each other (continuity where "
                     "there should be none), which a tester flags differently — not as a missing "
                     "pin.",
                "C": "A split pair still shows continuity on all pins (the wiremap looks correct); "
                     "it is a pairing error detected by crosstalk/NEXT testing, not an open pin.",
                "D": "Crosstalk/EMI degrades signal quality but would not show a single pin with "
                     "zero end-to-end continuity on a wiremap test.",
            },
            "exam_pattern": "Wiremap: missing pin = open (break). Pins connected that shouldn't be = "
                            "short. All pins map but pairs mis-twisted = split pair.",
        },
    },
    {
        "id": "netplus-nt-r2-004", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "A technician directly connects two older switches (no Auto-MDIX) with a standard "
                "straight-through patch cable, and the link does not come up. What is the correct "
                "fix?",
        "options": [
            {"id": "A", "text": "Use a crossover cable so each device's transmit pair connects to the other's receive pair"},
            {"id": "B", "text": "Use a rollover (console) cable between the switches"},
            {"id": "C", "text": "Replace both cables with fiber regardless of distance"},
            {"id": "D", "text": "Shorten the cable to under 1 meter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Two like devices without Auto-MDIX both transmit on the same pins, so a "
                       "straight-through cable crosses TX-to-TX. A crossover cable swaps the "
                       "transmit and receive pairs so TX meets RX, bringing the link up. (Auto-MDIX, "
                       "where present, does this automatically.)",
            "distractors": {
                "B": "A rollover cable is for console/management serial access to a device, not for "
                     "an Ethernet data link between switches.",
                "C": "Fiber is unnecessary here and does not address a copper TX/RX pinout mismatch "
                     "on a short link.",
                "D": "Length is not the problem; the issue is TX/RX alignment, which a crossover "
                     "corrects.",
            },
            "exam_pattern": "Like-to-like (switch-switch, PC-PC) without Auto-MDIX = crossover. "
                            "Unlike devices = straight-through. Rollover = console.",
        },
    },
    {
        "id": "netplus-nt-r2-005", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "On a workstation, a technician wants to list the host's currently active TCP "
                "connections and which local ports are in a LISTENING state. Which command-line "
                "utility shows this?",
        "options": [
            {"id": "A", "text": "netstat"},
            {"id": "B", "text": "nslookup"},
            {"id": "C", "text": "tracert / traceroute"},
            {"id": "D", "text": "ipconfig / ifconfig"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "netstat (network statistics) displays active connections, listening ports, "
                       "and related socket/state information on the local host — useful for spotting "
                       "unexpected open ports or established sessions.",
            "distractors": {
                "B": "nslookup queries DNS to resolve names to addresses; it does not list local "
                     "sockets or connections.",
                "C": "traceroute maps the path and per-hop latency to a remote host; it does not "
                     "show local listening ports.",
                "D": "ipconfig/ifconfig displays and configures interface addressing (IP, mask, "
                     "gateway), not active connection/socket state.",
            },
            "exam_pattern": "Local connections + listening ports = netstat (or `ss`). Path = "
                            "traceroute. DNS = nslookup/dig. Interface config = ipconfig/ifconfig.",
        },
    },
    {
        "id": "netplus-nt-r2-006", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "Two hosts on the same LAN are experiencing an IP conflict. A technician wants to "
                "view the local table that maps known IP addresses to their MAC addresses to see "
                "which hardware address is answering for the disputed IP. Which command displays "
                "this table?",
        "options": [
            {"id": "A", "text": "arp -a"},
            {"id": "B", "text": "ping -t"},
            {"id": "C", "text": "route print"},
            {"id": "D", "text": "nslookup"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "arp -a displays the ARP cache — the mapping of IP addresses to MAC addresses "
                       "the host has learned. It reveals which MAC is bound to a given IP, helping "
                       "identify the conflicting device.",
            "distractors": {
                "B": "ping -t sends continuous echo requests to test reachability; it does not "
                     "display IP-to-MAC mappings.",
                "C": "route print shows the host's IP routing table (destinations/gateways), not "
                     "ARP's IP-to-MAC entries.",
                "D": "nslookup resolves DNS names to IP addresses; it has nothing to do with MAC "
                     "addresses.",
            },
            "exam_pattern": "IP-to-MAC mapping on the local host = ARP cache (`arp -a`). Routing "
                            "table = `route print` / `netstat -r`.",
        },
    },
    {
        "id": "netplus-nt-r2-007", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "After upgrading a WAN circuit, an engineer wants to MEASURE the actual throughput "
                "achievable between a client and a server by generating test traffic and reporting "
                "the data rate. Which tool is designed for this?",
        "options": [
            {"id": "A", "text": "iperf"},
            {"id": "B", "text": "nslookup"},
            {"id": "C", "text": "arp"},
            {"id": "D", "text": "ipconfig"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "iperf (iperf3) generates TCP/UDP test streams between a client and a server "
                       "endpoint and reports achievable throughput, jitter, and loss — the standard "
                       "tool for actively measuring bandwidth.",
            "distractors": {
                "B": "nslookup tests DNS name resolution; it does not measure throughput.",
                "C": "arp displays IP-to-MAC mappings; it has no throughput-measurement function.",
                "D": "ipconfig shows interface addressing; it cannot generate traffic or measure "
                     "bandwidth.",
            },
            "exam_pattern": "Actively measure throughput between two endpoints = iperf. Reachability "
                            "= ping. Path/latency = traceroute.",
        },
    },
    {
        "id": "netplus-nt-r2-008", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 3, "type": "mcq",
        "stem": "Users at one site suddenly cannot log in to the domain, and browsers report "
                "'certificate is not yet valid' for internal HTTPS sites that worked yesterday. A "
                "technician notices the affected server's clock is off by 45 minutes. What is the "
                "MOST likely root cause?",
        "options": [
            {"id": "A", "text": "Time synchronization failure (NTP) — skewed clocks break certificate validation and Kerberos authentication"},
            {"id": "B", "text": "A duplicate IP address on the server"},
            {"id": "C", "text": "An exhausted DHCP scope"},
            {"id": "D", "text": "A crossover cable on the uplink"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Certificate validity windows and Kerberos tickets are time-sensitive. A "
                       "clock that has drifted (NTP failure) makes valid certificates appear 'not "
                       "yet valid'/expired and causes Kerberos logins to fail. Correcting time sync "
                       "resolves it.",
            "distractors": {
                "B": "A duplicate IP causes intermittent connectivity and conflict warnings, not "
                     "time-based certificate/Kerberos errors.",
                "C": "An exhausted DHCP scope prevents new clients from getting addresses; it does "
                     "not cause certificate-validity errors on an already-addressed server.",
                "D": "A cabling/pinout problem would drop the link entirely, not produce "
                     "'certificate not yet valid' messages.",
            },
            "exam_pattern": "Certificate 'not yet valid'/expired + Kerberos login failures + wrong "
                            "clock = NTP/time-sync problem. Fix time, fix auth.",
        },
    },
    {
        "id": "netplus-nt-r2-009", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "A network printer was given a STATIC IP that happens to fall within the router's "
                "DHCP scope. Intermittently, a laptop and the printer both claim that address and "
                "lose connectivity. What is the BEST permanent fix?",
        "options": [
            {"id": "A", "text": "Exclude the printer's address from the DHCP scope (or use a DHCP reservation instead)"},
            {"id": "B", "text": "Shorten the DHCP lease time to one hour"},
            {"id": "C", "text": "Assign the printer an APIPA 169.254 address"},
            {"id": "D", "text": "Disable ARP on the printer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The conflict happens because DHCP can hand out an address that was also "
                       "statically assigned. Excluding that address from the scope (or converting to "
                       "a DHCP reservation) guarantees the DHCP server never leases it to another "
                       "host.",
            "distractors": {
                "B": "A shorter lease makes conflicts recur MORE often as addresses recycle faster; "
                     "it does not prevent the overlap.",
                "C": "A 169.254 APIPA address means no valid network connectivity at all — that is "
                     "not a fix.",
                "D": "Disabling ARP would break the printer's Layer 2 communication entirely; ARP is "
                     "how conflicts are even detected.",
            },
            "exam_pattern": "Static address inside the DHCP pool = conflicts. Fix: exclude it from "
                            "the scope or use a reservation (DHCP-assigned, always the same IP).",
        },
    },
    {
        "id": "netplus-nt-r2-010", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 2, "type": "mcq",
        "stem": "A switch interface shows a steadily rising count of CRC errors and runt frames, "
                "and users on that link report slow, unreliable transfers. Which category of "
                "problem is MOST likely?",
        "options": [
            {"id": "A", "text": "A physical-layer fault — bad cable/connector, EMI, or a duplex mismatch"},
            {"id": "B", "text": "An exhausted DHCP scope"},
            {"id": "C", "text": "A misconfigured DNS zone"},
            {"id": "D", "text": "An expired TLS certificate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CRC errors (corrupted frames) and runts (undersized frames) point to Layer "
                       "1/2 problems: a damaged or marginal cable, excessive EMI, a failing "
                       "transceiver, or a duplex mismatch. Inspect/replace cabling and verify "
                       "speed/duplex settings.",
            "distractors": {
                "B": "DHCP scope exhaustion prevents addressing; it does not generate CRC/runt frame "
                     "errors on an interface.",
                "C": "A DNS zone problem affects name resolution, not physical frame-integrity "
                     "counters.",
                "D": "A TLS certificate issue causes application trust errors, not interface-level "
                     "CRC/runt counters.",
            },
            "exam_pattern": "CRC errors + runts/giants on an interface = physical layer "
                            "(cabling/EMI/transceiver) or duplex mismatch. Check cables and "
                            "speed/duplex first.",
        },
    },
    {
        "id": "netplus-nt-r2-011", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 2, "type": "mcq",
        "stem": "A cloud application 'feels sluggish' for a branch office, yet the WAN link's "
                "utilization graphs stay low and there is no packet loss. A ping to the application "
                "server shows a consistent round-trip time of 320 ms. What is the MOST likely "
                "performance factor?",
        "options": [
            {"id": "A", "text": "High latency (round-trip delay), not a bandwidth shortage"},
            {"id": "B", "text": "Insufficient bandwidth on the WAN link"},
            {"id": "C", "text": "A duplex mismatch on the LAN switch"},
            {"id": "D", "text": "DNS resolution failure"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Low utilization and no loss rule out congestion; a 320 ms RTT is high "
                       "latency. Chatty or latency-sensitive applications feel slow when delay is "
                       "high even if bandwidth is plentiful (e.g., long-distance or satellite "
                       "paths).",
            "distractors": {
                "B": "Bandwidth is not the limit here — utilization is low and there is no loss, so "
                     "the pipe is not full.",
                "C": "A duplex mismatch produces errors/collisions and loss; the scenario explicitly "
                     "has no loss and points to delay.",
                "D": "DNS failure would stop the app from connecting by name at all, not merely make "
                     "an already-reachable server feel slow with a measurable 320 ms RTT.",
            },
            "exam_pattern": "Slow but low utilization + no loss + high RTT = latency-bound "
                            "(distance/path), not bandwidth. Bandwidth problem = high utilization + "
                            "loss.",
        },
    },
]
