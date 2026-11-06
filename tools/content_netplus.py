"""CompTIA Network+ N10-009 item pool — original, objective-aligned questions.

Same authoring rules as the Cisco and Security+ pools: original content mapped
to the public N10-009 exam objectives, never real exam items. build_content.py
shuffles option order, so the answer key here is not positionally biased.
"""

QUESTIONS = [
    # ===== 1.0 Networking Concepts ==========================================
    {
        "id": "netplus-nc-001", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 2, "type": "mcq",
        "stem": "A technician examines a captured frame and notes that forwarding within the "
                "local LAN is based on the source and destination MAC addresses. Which OSI "
                "layer is responsible for MAC addressing and framing?",
        "options": [
            {"id": "A", "text": "Layer 2 - Data Link"},
            {"id": "B", "text": "Layer 3 - Network"},
            {"id": "C", "text": "Layer 1 - Physical"},
            {"id": "D", "text": "Layer 4 - Transport"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MAC addresses and frames live at the Data Link layer (Layer 2); switches "
                       "use them to forward traffic within a broadcast domain.",
            "distractors": {
                "B": "The Network layer handles logical IP addressing and routing BETWEEN networks, not MAC addressing.",
                "C": "The Physical layer transmits raw bits over the medium (cabling, connectors, signaling).",
                "D": "The Transport layer handles end-to-end segmentation and TCP/UDP port numbers.",
            },
            "exam_pattern": "MAC/frames/switches = L2; IP/routing = L3; bits/cabling = L1; ports/TCP-UDP = L4.",
        },
    },
    {
        "id": "netplus-nc-002", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 1, "type": "mcq",
        "stem": "A user needs to securely administer a Linux server's command line over the "
                "network. Which protocol and default port should be used?",
        "options": [
            {"id": "A", "text": "SSH - TCP 22"},
            {"id": "B", "text": "Telnet - TCP 23"},
            {"id": "C", "text": "RDP - TCP 3389"},
            {"id": "D", "text": "FTP - TCP 21"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSH provides an encrypted remote command-line session and listens on TCP 22 "
                       "by default.",
            "distractors": {
                "B": "Telnet (TCP 23) is also a remote CLI but sends everything in cleartext, so it is not secure.",
                "C": "RDP (TCP 3389) delivers a remote GRAPHICAL desktop (Windows), not a secure shell.",
                "D": "FTP (TCP 21) transfers files in cleartext and is not a management shell.",
            },
            "exam_pattern": "Secure CLI = SSH 22; cleartext CLI = Telnet 23; graphical remote desktop = RDP 3389.",
        },
    },
    {
        "id": "netplus-nc-003", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 2, "type": "multi",
        "stem": "A DHCP client is obtaining an IPv4 address from a server. Which two UDP ports "
                "are used by the DHCP exchange? (Choose two.)",
        "options": [
            {"id": "A", "text": "UDP 67 (server)"},
            {"id": "B", "text": "UDP 68 (client)"},
            {"id": "C", "text": "UDP 53"},
            {"id": "D", "text": "UDP 69"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "DHCP uses UDP 67 on the server side and UDP 68 on the client side to carry "
                       "the Discover/Offer/Request/Acknowledge messages.",
            "distractors": {
                "C": "UDP 53 is DNS (name resolution), not DHCP.",
                "D": "UDP 69 is TFTP (trivial file transfer), not DHCP.",
            },
            "exam_pattern": "DHCP = UDP 67 (server) + 68 (client); DNS = 53; TFTP = 69.",
        },
    },
    {
        "id": "netplus-nc-004", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 3, "type": "mcq",
        "stem": "A network engineer must divide 192.168.10.0/24 into subnets that each support "
                "at least 50 usable hosts, while maximizing the number of subnets. Which subnet "
                "mask should be used?",
        "options": [
            {"id": "A", "text": "/26 (255.255.255.192)"},
            {"id": "B", "text": "/25 (255.255.255.128)"},
            {"id": "C", "text": "/27 (255.255.255.224)"},
            {"id": "D", "text": "/28 (255.255.255.240)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "/26 yields 2^6 - 2 = 62 usable hosts per subnet (meets the 50 requirement) and "
                       "creates four subnets from a /24 - the smallest block that still fits 50 hosts, "
                       "which maximizes the subnet count.",
            "distractors": {
                "B": "/25 gives 126 usable hosts but only two subnets - it wastes addresses and yields fewer subnets.",
                "C": "/27 gives only 2^5 - 2 = 30 usable hosts, which is below the 50 required.",
                "D": "/28 gives only 2^4 - 2 = 14 usable hosts, far below the 50 required.",
            },
            "exam_pattern": "Usable hosts = 2^(host bits) - 2. The smallest mask that still fits the host count gives the most subnets.",
        },
    },
    {
        "id": "netplus-nc-005", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv6_np", "difficulty": 2, "type": "mcq",
        "stem": "An IPv6 host autoconfigures an address that begins with fe80::. What is the "
                "scope of this address?",
        "options": [
            {"id": "A", "text": "Link-local - valid only on the local link and not routed"},
            {"id": "B", "text": "Global unicast - routable on the public Internet"},
            {"id": "C", "text": "Unique local - private addressing routable within a site"},
            {"id": "D", "text": "Multicast - one-to-many delivery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "fe80::/10 is the IPv6 link-local range. Every IPv6 interface has one; it is used "
                       "for on-link communication (such as neighbor discovery) and is never forwarded by a router.",
            "distractors": {
                "B": "Global unicast addresses come from the 2000::/3 range and ARE Internet-routable.",
                "C": "Unique local addresses (fc00::/7, commonly fd00::/8) are the IPv6 'private' range, routable within a site.",
                "D": "Multicast uses the ff00::/8 range for one-to-many delivery, not a single host's autoconfigured address.",
            },
            "exam_pattern": "fe80:: = link-local (not routed); 2000::/3 = global; fd00:: = unique local; ff00:: = multicast.",
        },
    },
    {
        "id": "netplus-nc-006", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_appliances", "difficulty": 2, "type": "mcq",
        "stem": "A company wants a single managed device at the network edge that combines "
                "firewalling, intrusion prevention, antimalware, and content filtering. Which "
                "appliance best fits?",
        "options": [
            {"id": "A", "text": "A UTM / next-generation firewall (NGFW)"},
            {"id": "B", "text": "A Layer 2 switch"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A forward proxy server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Unified Threat Management (UTM), often delivered as a next-generation firewall, "
                       "consolidates firewalling, IPS, antimalware, URL/content filtering and more into one appliance.",
            "distractors": {
                "B": "A Layer 2 switch forwards frames by MAC within a LAN and provides no security services.",
                "C": "A load balancer distributes traffic across servers for availability and scale, not integrated threat prevention.",
                "D": "A forward proxy caches and filters web requests but does not provide the full firewall/IPS/antimalware stack.",
            },
            "exam_pattern": "All-in-one security stack at the edge = UTM / NGFW.",
        },
    },
    {
        "id": "netplus-nc-007", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "cloud_concepts", "difficulty": 2, "type": "mcq",
        "stem": "A startup wants to run its custom application without managing the underlying "
                "servers, storage, or virtualization, but still control the application code and "
                "its data. Which cloud service model is this?",
        "options": [
            {"id": "A", "text": "PaaS (Platform as a Service)"},
            {"id": "B", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "DaaS (Desktop as a Service)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PaaS provides a managed platform (OS, runtime, middleware) on which customers deploy "
                       "their own applications and data, without managing the underlying infrastructure.",
            "distractors": {
                "B": "IaaS provides the VMs, storage and network, but the customer still manages the OS and everything above it.",
                "C": "SaaS delivers a finished application (for example webmail) with no development platform exposed.",
                "D": "DaaS delivers virtual desktops to end users, not a platform for hosting an application.",
            },
            "exam_pattern": "IaaS = you manage OS and up; PaaS = you manage app/data only; SaaS = vendor manages everything.",
        },
    },
    {
        "id": "netplus-nc-008", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "traffic_types", "difficulty": 1, "type": "mcq",
        "stem": "A host sends an IPv4 packet to destination 255.255.255.255. What type of traffic "
                "is this?",
        "options": [
            {"id": "A", "text": "Broadcast - delivered to all hosts on the local subnet"},
            {"id": "B", "text": "Unicast - one-to-one delivery"},
            {"id": "C", "text": "Multicast - one-to-group delivery"},
            {"id": "D", "text": "Anycast - delivery to the nearest member of a group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "255.255.255.255 is the limited (all-ones) IPv4 broadcast address; it reaches every "
                       "host in the local broadcast domain and is not forwarded by routers.",
            "distractors": {
                "B": "Unicast targets a single specific host address, not every host.",
                "C": "Multicast uses the 224.0.0.0/4 range to reach a subscribed group, not an all-ones address.",
                "D": "Anycast (common in IPv6 and DNS) routes to the topologically nearest member of a group.",
            },
            "exam_pattern": "255.255.255.255 or all-ones host bits = broadcast; 224.0.0.0/4 = multicast; single host = unicast.",
        },
    },
    {
        "id": "netplus-nc-009", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_topologies", "difficulty": 2, "type": "mcq",
        "stem": "In a data center, every leaf switch connects to every spine switch, but leaf "
                "switches do not connect directly to one another. Which topology is described?",
        "options": [
            {"id": "A", "text": "Spine-and-leaf"},
            {"id": "B", "text": "Full mesh"},
            {"id": "C", "text": "Bus"},
            {"id": "D", "text": "Ring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spine-and-leaf is a two-tier design where each leaf (access) switch uplinks to every "
                       "spine switch, giving predictable, low-latency east-west paths; leaves do not interconnect directly.",
            "distractors": {
                "B": "In a full mesh EVERY node connects to every other node - here the leaves do not connect to each other.",
                "C": "A bus topology shares a single backbone cable and collision domain - a legacy design, not a switched fabric.",
                "D": "A ring connects each device to two neighbors to form a closed loop.",
            },
            "exam_pattern": "Each leaf to every spine, no leaf-to-leaf = spine-and-leaf; every node to every node = full mesh.",
        },
    },

    # ===== 2.0 Network Implementation =======================================
    {
        "id": "netplus-ni-001", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A router learns a path to the same destination network from OSPF, EIGRP, and a "
                "static route. Using default administrative distances, which route does the "
                "router install in its routing table?",
        "options": [
            {"id": "A", "text": "The static route (AD 1)"},
            {"id": "B", "text": "The EIGRP route (AD 90)"},
            {"id": "C", "text": "The OSPF route (AD 110)"},
            {"id": "D", "text": "Whichever route has the highest metric"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When multiple sources offer the same prefix, the router prefers the lowest "
                       "administrative distance. Defaults: connected 0, static 1, EIGRP 90, OSPF 110 - so the static route (1) wins.",
            "distractors": {
                "B": "EIGRP's AD is 90 - lower than OSPF but higher than the static route's 1.",
                "C": "OSPF's AD is 110 - the highest of the three choices, so it loses.",
                "D": "Metric only breaks ties WITHIN a single protocol; AD is compared first, and the LOWEST AD (not the highest metric) wins.",
            },
            "exam_pattern": "Lowest AD wins: connected 0 < static 1 < EIGRP 90 < OSPF 110 < RIP 120. Metric breaks ties within a protocol.",
        },
    },
    {
        "id": "netplus-ni-002", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "routing_technologies", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise connects to two different ISPs and must exchange routing "
                "information with them across the public Internet. Which routing protocol is "
                "designed for this role?",
        "options": [
            {"id": "A", "text": "BGP"},
            {"id": "B", "text": "OSPF"},
            {"id": "C", "text": "EIGRP"},
            {"id": "D", "text": "RIPv2"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BGP is the path-vector exterior gateway protocol that exchanges routes between "
                       "autonomous systems - the standard choice for multihoming to ISPs on the Internet.",
            "distractors": {
                "B": "OSPF is a link-state INTERIOR gateway protocol used for routing within an autonomous system, not between ISPs.",
                "C": "EIGRP is an interior gateway protocol used inside a single administrative domain.",
                "D": "RIPv2 is a legacy interior distance-vector protocol limited to 15 hops - unsuitable for Internet peering.",
            },
            "exam_pattern": "Between autonomous systems / ISP peering = BGP (an EGP). Inside your own network = OSPF or EIGRP (IGPs).",
        },
    },
    {
        "id": "netplus-ni-003", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 2, "type": "mcq",
        "stem": "A switch port must carry traffic for multiple VLANs to another switch over a "
                "single link. Which port type and tagging standard are required?",
        "options": [
            {"id": "A", "text": "An 802.1Q trunk port"},
            {"id": "B", "text": "An access port assigned to one VLAN"},
            {"id": "C", "text": "A port-mirroring (SPAN) destination port"},
            {"id": "D", "text": "A routed port with no VLAN awareness"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A trunk carries multiple VLANs over one link; IEEE 802.1Q inserts a VLAN tag into "
                       "each frame so the far-end switch can separate the VLANs.",
            "distractors": {
                "B": "An access port belongs to a single VLAN and carries untagged traffic for only that VLAN.",
                "C": "A SPAN/mirror port copies traffic to a monitor port for analysis - it does not carry production VLAN traffic between switches.",
                "D": "A routed port operates at Layer 3 for a single subnet and does not tag/trunk multiple VLANs.",
            },
            "exam_pattern": "Multiple VLANs over one link = 802.1Q trunk; one VLAN, untagged = access port.",
        },
    },
    {
        "id": "netplus-ni-004", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "switching_technologies", "difficulty": 3, "type": "mcq",
        "stem": "After a new switch is cabled with redundant links, users report intermittent "
                "outages and the network floods with broadcast traffic. The cause is a Layer 2 "
                "loop. Which protocol is designed to prevent Layer 2 loops?",
        "options": [
            {"id": "A", "text": "STP (Spanning Tree Protocol)"},
            {"id": "B", "text": "VTP (VLAN Trunking Protocol)"},
            {"id": "C", "text": "HSRP"},
            {"id": "D", "text": "CDP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "STP (802.1D and successors such as RSTP) builds a loop-free logical topology by "
                       "electing a root bridge and placing redundant ports into a blocking state, preventing broadcast storms.",
            "distractors": {
                "B": "VTP propagates the VLAN database between switches - it does nothing to prevent loops.",
                "C": "HSRP is a first-hop redundancy protocol for default-gateway failover at Layer 3, not loop prevention.",
                "D": "CDP is a Layer 2 neighbor-discovery protocol - informational only, not loop prevention.",
            },
            "exam_pattern": "Layer 2 loop prevention / broadcast-storm control = STP (RSTP). Gateway redundancy = HSRP/VRRP.",
        },
    },
    {
        "id": "netplus-ni-005", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "wireless_standards", "difficulty": 1, "type": "mcq",
        "stem": "A company is deploying Wi-Fi 6 access points. Which IEEE 802.11 standard does "
                "Wi-Fi 6 correspond to?",
        "options": [
            {"id": "A", "text": "802.11ax"},
            {"id": "B", "text": "802.11ac"},
            {"id": "C", "text": "802.11n"},
            {"id": "D", "text": "802.11g"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Wi-Fi 6 is the Wi-Fi Alliance name for IEEE 802.11ax, which operates in 2.4 and 5 GHz "
                       "(and 6 GHz for Wi-Fi 6E) and adds OFDMA for greater efficiency.",
            "distractors": {
                "B": "802.11ac is Wi-Fi 5 (5 GHz only).",
                "C": "802.11n is Wi-Fi 4 (2.4 and 5 GHz).",
                "D": "802.11g is a legacy 2.4 GHz standard topping out at 54 Mbps.",
            },
            "exam_pattern": "Wi-Fi 6 = 802.11ax; Wi-Fi 5 = 802.11ac; Wi-Fi 4 = 802.11n.",
        },
    },
    {
        "id": "netplus-ni-006", "exam": "netplus", "domain": "network_implementation",
        "subtopic": "physical_installations", "difficulty": 2, "type": "mcq",
        "stem": "A technician must run cable through a drop ceiling that is also used to "
                "circulate HVAC air between rooms. Which cable rating does fire code require "
                "for this space?",
        "options": [
            {"id": "A", "text": "Plenum-rated (CMP)"},
            {"id": "B", "text": "Riser-rated (CMR)"},
            {"id": "C", "text": "General-purpose PVC (CM)"},
            {"id": "D", "text": "Direct-burial outdoor cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Air-handling (plenum) spaces require plenum-rated cable (CMP), whose jacket produces "
                       "less smoke and fewer toxic fumes when burning, meeting fire-safety code.",
            "distractors": {
                "B": "Riser-rated (CMR) cable is for vertical runs between floors (non-plenum shafts) and carries a lower fire rating than plenum.",
                "C": "General-purpose PVC (CM) cable is only for single-floor, non-plenum runs and is not permitted in plenums.",
                "D": "Direct-burial cable is hardened for underground outdoor use, not indoor plenum fire rating.",
            },
            "exam_pattern": "Air-handling space = plenum (CMP); vertical floor-to-floor shaft = riser (CMR).",
        },
    },

    # ===== 3.0 Network Operations ===========================================
    {
        "id": "netplus-nops-001", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 2, "type": "mcq",
        "stem": "An administrator needs a domain's DNS to specify which servers are authorized "
                "to receive email for that domain. Which DNS record type provides this?",
        "options": [
            {"id": "A", "text": "MX"},
            {"id": "B", "text": "A"},
            {"id": "C", "text": "CNAME"},
            {"id": "D", "text": "PTR"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The MX (Mail Exchanger) record lists the mail servers responsible for accepting "
                       "email for a domain, each with a priority value.",
            "distractors": {
                "B": "An A record maps a hostname to an IPv4 address.",
                "C": "A CNAME is an alias that points one name to another canonical name.",
                "D": "A PTR record maps an IP address back to a name (reverse DNS lookup).",
            },
            "exam_pattern": "MX = mail servers; A = name to IPv4; AAAA = name to IPv6; CNAME = alias; PTR = reverse lookup.",
        },
    },
    {
        "id": "netplus-nops-002", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 1, "type": "mcq",
        "stem": "Which sequence correctly describes the DHCP lease process a client follows to "
                "obtain an IPv4 address?",
        "options": [
            {"id": "A", "text": "Discover, Offer, Request, Acknowledge"},
            {"id": "B", "text": "Request, Offer, Discover, Acknowledge"},
            {"id": "C", "text": "Offer, Discover, Acknowledge, Request"},
            {"id": "D", "text": "Discover, Request, Offer, Acknowledge"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DHCP follows DORA: the client broadcasts a Discover, the server returns an Offer, "
                       "the client sends a Request for the offered address, and the server sends an Acknowledge.",
            "distractors": {
                "B": "The client cannot Request before it has Discovered servers and received an Offer.",
                "C": "An Offer cannot precede the client's Discover, and the Request must come before the Acknowledge.",
                "D": "The server's Offer must come before the client's Request - this ordering swaps those two steps.",
            },
            "exam_pattern": "DHCP = DORA: Discover then Offer then Request then Acknowledge.",
        },
    },
    {
        "id": "netplus-nops-003", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 3, "type": "mcq",
        "stem": "On a device using standard syslog severity levels, which level represents the "
                "MOST severe condition?",
        "options": [
            {"id": "A", "text": "0 - Emergency"},
            {"id": "B", "text": "7 - Debug"},
            {"id": "C", "text": "5 - Notice"},
            {"id": "D", "text": "4 - Warning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Syslog severities run from 0 (Emergency, most severe - the system is unusable) to "
                       "7 (Debug, least severe). A lower number means a higher-priority event.",
            "distractors": {
                "B": "Level 7 (Debug) is the LEAST severe - verbose diagnostic detail.",
                "C": "Level 5 (Notice) is a normal but significant condition, well below Emergency.",
                "D": "Level 4 (Warning) is a mid-range condition, less severe than Emergency.",
            },
            "exam_pattern": "Syslog: 0 Emergency is worst, 7 Debug is least. Lower number = higher severity.",
        },
    },
    {
        "id": "netplus-nops-004", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A network team wants to see which applications and hosts consume the most "
                "bandwidth by collecting metadata about each IP conversation (source, "
                "destination, ports, and byte counts). Which technology provides this data?",
        "options": [
            {"id": "A", "text": "NetFlow (or IPFIX/sFlow)"},
            {"id": "B", "text": "SNMP polling of interface counters"},
            {"id": "C", "text": "Syslog"},
            {"id": "D", "text": "A full packet capture of all payloads"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NetFlow (and IPFIX/sFlow) exports flow records summarizing conversations - source and "
                       "destination IPs, ports, protocol, and byte/packet counts - ideal for identifying top talkers and application usage.",
            "distractors": {
                "B": "SNMP polling of interface counters shows total throughput per interface but not a per-conversation or per-application breakdown.",
                "C": "Syslog carries event and log messages, not traffic-volume flow records.",
                "D": "A full packet capture does contain everything but is storage-heavy and excessive for simple bandwidth-by-conversation accounting.",
            },
            "exam_pattern": "Who is talking to whom and how much = flow data (NetFlow/IPFIX/sFlow). Device health = SNMP. Events = syslog.",
        },
    },
    {
        "id": "netplus-nops-005", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "During disaster-recovery planning, management states that the business can "
                "tolerate losing at most 15 minutes of data in an outage. Which metric does this "
                "statement define?",
        "options": [
            {"id": "A", "text": "RPO (Recovery Point Objective)"},
            {"id": "B", "text": "RTO (Recovery Time Objective)"},
            {"id": "C", "text": "MTTR (Mean Time To Repair)"},
            {"id": "D", "text": "MTBF (Mean Time Between Failures)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RPO is the maximum acceptable amount of data loss measured in time - how far back the "
                       "last usable recovery point may be. '15 minutes of data' is an RPO.",
            "distractors": {
                "B": "RTO is the maximum tolerable time to restore SERVICE (downtime), not the amount of data lost.",
                "C": "MTTR is the average time required to repair a failed component.",
                "D": "MTBF is the average time between failures, a reliability measure rather than a recovery target.",
            },
            "exam_pattern": "RPO = how much DATA you can lose (time); RTO = how long until you are back UP.",
        },
    },
    {
        "id": "netplus-nops-006", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 1, "type": "mcq",
        "stem": "A technician needs to see how devices are physically connected - which switch "
                "port each wall jack terminates to and the cable runs between the MDF and the "
                "IDFs. Which document provides this?",
        "options": [
            {"id": "A", "text": "A physical / wiring diagram"},
            {"id": "B", "text": "A logical network diagram"},
            {"id": "C", "text": "A service-level agreement (SLA)"},
            {"id": "D", "text": "A baseline configuration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A physical/wiring diagram documents the actual cable runs, patch-panel and switch-port "
                       "terminations, and MDF/IDF connections - the physical-layer layout.",
            "distractors": {
                "B": "A logical diagram shows IP subnets, VLANs and routing relationships, not physical cable runs.",
                "C": "An SLA defines agreed service metrics (uptime, response times) with a provider, not cabling.",
                "D": "A baseline configuration records a known-good device config for comparison, not physical connectivity.",
            },
            "exam_pattern": "Physical/wiring diagram = cables and ports; logical diagram = IPs, VLANs and routing.",
        },
    },

    # ===== 4.0 Network Security =============================================
    {
        "id": "netplus-nsec-001", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 2, "type": "mcq",
        "stem": "To stop unauthorized devices from connecting through access-layer switch ports, "
                "an administrator wants each port limited to a specific MAC address and shut down "
                "if a different device connects. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Port security"},
            {"id": "B", "text": "DHCP snooping"},
            {"id": "C", "text": "Spanning Tree PortFast"},
            {"id": "D", "text": "802.1Q tagging"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Switch port security restricts a port to specific learned or allowed MAC addresses and "
                       "can take a violation action (such as err-disable/shutdown) when an unauthorized MAC appears.",
            "distractors": {
                "B": "DHCP snooping blocks rogue DHCP servers and builds a binding table - it does not lock a port to a MAC address.",
                "C": "PortFast moves an access port to forwarding quickly for end hosts; it is not an access-control feature.",
                "D": "802.1Q is VLAN tagging on trunks, unrelated to MAC-based port lockdown.",
            },
            "exam_pattern": "Lock a port to specific MAC(s) with a violation action = port security. Stop rogue DHCP = DHCP snooping.",
        },
    },
    {
        "id": "netplus-nsec-002", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 3, "type": "mcq",
        "stem": "A company wants devices to authenticate before being granted access to any "
                "VLAN, using a central RADIUS server at the point of connection. Which standard "
                "provides this port-based network access control?",
        "options": [
            {"id": "A", "text": "802.1X"},
            {"id": "B", "text": "802.11ax"},
            {"id": "C", "text": "802.3af"},
            {"id": "D", "text": "802.1Q"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IEEE 802.1X provides port-based network access control: the supplicant authenticates "
                       "through an authenticator (switch or AP) to a RADIUS server before the port is opened.",
            "distractors": {
                "B": "802.11ax is the Wi-Fi 6 radio standard, not an access-control framework.",
                "C": "802.3af is Power over Ethernet (PoE), which delivers power, not authentication.",
                "D": "802.1Q is VLAN tagging, not an authentication mechanism.",
            },
            "exam_pattern": "Authenticate before network access (supplicant / authenticator / RADIUS) = 802.1X.",
        },
    },
    {
        "id": "netplus-nsec-003", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "An attacker on the LAN sends forged ARP replies so that traffic between a host "
                "and its default gateway flows through the attacker's machine. Which attack is "
                "this?",
        "options": [
            {"id": "A", "text": "ARP spoofing enabling an on-path (man-in-the-middle) attack"},
            {"id": "B", "text": "DNS poisoning"},
            {"id": "C", "text": "SYN flood"},
            {"id": "D", "text": "VLAN hopping"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Forging ARP replies to bind the attacker's MAC to the gateway's IP lets the attacker "
                       "intercept and relay traffic - ARP spoofing used to set up an on-path (MITM) position.",
            "distractors": {
                "B": "DNS poisoning corrupts name-resolution records to redirect by hostname; it does not forge ARP at Layer 2.",
                "C": "A SYN flood exhausts a server's half-open connections (an availability/DoS attack), not traffic interception.",
                "D": "VLAN hopping crosses VLAN boundaries using tagging tricks, not ARP-based interception.",
            },
            "exam_pattern": "Forged ARP replies to sit in the middle = ARP spoofing / on-path (MITM).",
        },
    },
    {
        "id": "netplus-nsec-004", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 2, "type": "mcq",
        "stem": "A remote employee needs encrypted access to internal company resources as "
                "though directly connected to the corporate LAN. Which solution provides this?",
        "options": [
            {"id": "A", "text": "A client-to-site (remote-access) VPN using IPsec or SSL/TLS"},
            {"id": "B", "text": "A port forward on the edge router to each internal host"},
            {"id": "C", "text": "A Telnet session to an internal jump host"},
            {"id": "D", "text": "An open guest Wi-Fi SSID"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A remote-access (client-to-site) VPN builds an encrypted tunnel from the user's device "
                       "to the corporate network, giving secure access to internal resources over the Internet.",
            "distractors": {
                "B": "Port forwarding exposes individual internal hosts directly to the Internet with no unified encrypted tunnel - insecure and limited.",
                "C": "Telnet is unencrypted and reaches only one host's CLI, not the whole LAN.",
                "D": "Open guest Wi-Fi is unencrypted and provides no path into internal resources.",
            },
            "exam_pattern": "Secure remote user to corporate LAN tunnel = client-to-site (remote-access) VPN.",
        },
    },
    {
        "id": "netplus-nsec-005", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "A data center wants to prevent tailgating, where an unauthorized person follows "
                "an authorized employee through a secure door. Which physical control is MOST "
                "effective?",
        "options": [
            {"id": "A", "text": "An access control vestibule (mantrap)"},
            {"id": "B", "text": "A SIEM system"},
            {"id": "C", "text": "A host-based firewall"},
            {"id": "D", "text": "A syslog server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An access control vestibule (mantrap) uses interlocking doors to admit only one person "
                       "at a time, directly defeating tailgating.",
            "distractors": {
                "B": "A SIEM aggregates and correlates logs - a detective, logical control, not a physical barrier.",
                "C": "A host-based firewall filters network traffic on a device and does nothing for physical entry.",
                "D": "A syslog server stores event logs and is unrelated to controlling door access.",
            },
            "exam_pattern": "Stop tailgating at a door = access control vestibule (mantrap).",
        },
    },
    {
        "id": "netplus-nsec-006", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to permit or deny packets entering a router interface "
                "based on source/destination IP address, protocol, and port. Which tool does "
                "this?",
        "options": [
            {"id": "A", "text": "An access control list (ACL)"},
            {"id": "B", "text": "A VLAN trunk"},
            {"id": "C", "text": "An SNMP community string"},
            {"id": "D", "text": "Spanning-tree BPDU guard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ACLs permit or deny traffic based on criteria such as source/destination IP address, "
                       "protocol, and port, applied to an interface in a chosen direction.",
            "distractors": {
                "B": "A trunk carries multiple VLANs over a link; it does not filter traffic by IP or port.",
                "C": "An SNMP community string is a management credential for monitoring, not a traffic filter.",
                "D": "BPDU guard protects STP by disabling a port that unexpectedly receives BPDUs - it is not IP/port filtering.",
            },
            "exam_pattern": "Permit/deny by IP, protocol and port on an interface = ACL.",
        },
    },

    # ===== 5.0 Network Troubleshooting ======================================
    {
        "id": "netplus-nt-001", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 2, "type": "mcq",
        "stem": "Following the CompTIA seven-step troubleshooting methodology, which step comes "
                "immediately AFTER 'establish a theory of probable cause'?",
        "options": [
            {"id": "A", "text": "Test the theory to determine the cause"},
            {"id": "B", "text": "Identify the problem"},
            {"id": "C", "text": "Implement the solution"},
            {"id": "D", "text": "Document findings, actions, and outcomes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The order is identify the problem, establish a theory, TEST the theory, establish a plan "
                       "of action, implement the solution (or escalate), verify full functionality, and document. "
                       "Testing the theory immediately follows establishing it.",
            "distractors": {
                "B": "Identifying the problem is step 1 - it comes before establishing a theory, not after.",
                "C": "Implementing the solution comes later, after you have tested the theory and built a plan of action.",
                "D": "Documenting findings is the final step of the methodology.",
            },
            "exam_pattern": "Seven steps: Identify, Theory, Test, Plan, Implement, Verify, Document.",
        },
    },
    {
        "id": "netplus-nt-002", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "A technician can ping a remote server by its IP address but not by its hostname. "
                "Which command best confirms whether DNS is resolving the name?",
        "options": [
            {"id": "A", "text": "nslookup (or dig)"},
            {"id": "B", "text": "ping -t"},
            {"id": "C", "text": "ipconfig /release"},
            {"id": "D", "text": "tracert to the IP address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "nslookup (or dig) queries DNS directly to show whether the hostname resolves to an IP - "
                       "exactly the failure when IP works but the name does not.",
            "distractors": {
                "B": "ping -t simply pings the target continuously; it does not isolate name resolution.",
                "C": "ipconfig /release drops the DHCP lease, which is unrelated to testing name resolution.",
                "D": "tracert to an IP maps the path while bypassing DNS entirely, so it cannot reveal a name-resolution problem.",
            },
            "exam_pattern": "Works by IP but fails by name = DNS problem; test with nslookup or dig.",
        },
    },
    {
        "id": "netplus-nt-003", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "A newly installed copper Ethernet run of roughly 120 meters shows an "
                "intermittent or failing link. Based on structured-cabling guidance, what is the "
                "MOST likely cause?",
        "options": [
            {"id": "A", "text": "The run exceeds the 100-meter maximum for twisted-pair Ethernet"},
            {"id": "B", "text": "The cable is Cat6 instead of Cat5e"},
            {"id": "C", "text": "A duplex mismatch on the switch port"},
            {"id": "D", "text": "The switch port is assigned to the wrong VLAN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Twisted-pair Ethernet is limited to a 100-meter total channel (about 90 m horizontal plus "
                       "patch cords). At ~120 m, attenuation degrades the signal, causing an intermittent or dead link.",
            "distractors": {
                "B": "Cat6 exceeds Cat5e specifications, so using it is not a fault; both still share the 100 m distance limit.",
                "C": "A duplex mismatch produces collisions and CRC errors on a working link, not a distance-related failure on a long new run.",
                "D": "A wrong VLAN changes which network the port joins; it does not prevent the physical link from establishing at distance.",
            },
            "exam_pattern": "Copper twisted-pair limit = 100 m; longer distances need fiber or an intermediate switch/repeater.",
        },
    },
    {
        "id": "netplus-nt-004", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "Several clients on a subnet have received 169.254.x.x addresses and cannot reach "
                "other networks. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The DHCP server is unreachable, so the clients fell back to APIPA"},
            {"id": "B", "text": "The DNS server is down"},
            {"id": "C", "text": "The default gateway has a duplex mismatch"},
            {"id": "D", "text": "An expired TLS certificate on the web server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "169.254.0.0/16 is APIPA (Automatic Private IP Addressing). A client self-assigns an "
                       "address from this range only when it cannot reach a DHCP server, so DHCP failure is the cause.",
            "distractors": {
                "B": "A down DNS server breaks name resolution, but clients would still receive a proper DHCP-assigned address, not APIPA.",
                "C": "A gateway duplex mismatch causes errors and slowness, not a 169.254 self-assigned address.",
                "D": "An expired TLS certificate affects HTTPS trust for one service and has nothing to do with IP addressing.",
            },
            "exam_pattern": "169.254.x.x = APIPA = the client could not reach a DHCP server.",
        },
    },
    {
        "id": "netplus-nt-005", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 3, "type": "mcq",
        "stem": "Users on a gigabit link report very slow transfers, and the switch shows many "
                "late collisions and CRC errors on the port. Which issue is the MOST likely "
                "cause?",
        "options": [
            {"id": "A", "text": "A duplex mismatch between the switch and the host"},
            {"id": "B", "text": "An oversized MTU configured on the DNS server"},
            {"id": "C", "text": "An incorrect DNS MX record"},
            {"id": "D", "text": "A fully exhausted DHCP scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Late collisions together with CRC/alignment errors on a link are the classic signature of "
                       "a duplex mismatch (one side full-duplex, the other half-duplex), which severely degrades throughput.",
            "distractors": {
                "B": "An MTU setting on a DNS server does not generate switch-port collisions or CRC errors.",
                "C": "An MX record problem affects email delivery, not link-layer errors or throughput.",
                "D": "A full DHCP scope prevents new address leases but does not cause collisions or CRC errors on an established link.",
            },
            "exam_pattern": "Late collisions + CRC errors + slow link = duplex mismatch.",
        },
    },
    {
        "id": "netplus-nt-006", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 1, "type": "mcq",
        "stem": "A technician must identify which of 48 unlabeled cables in a patch panel "
                "corresponds to a specific wall jack. Which tool is designed for this?",
        "options": [
            {"id": "A", "text": "A tone generator and probe (toner)"},
            {"id": "B", "text": "A protocol analyzer"},
            {"id": "C", "text": "A loopback plug"},
            {"id": "D", "text": "A Wi-Fi analyzer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A tone generator places a signal on the wire at one end, and the inductive probe detects "
                       "that tone at the other end, letting the technician trace and locate a specific cable among many.",
            "distractors": {
                "B": "A protocol analyzer captures and decodes traffic; it cannot physically trace a cable.",
                "C": "A loopback plug tests a port or NIC by looping transmit to receive - it does not locate cables.",
                "D": "A Wi-Fi analyzer surveys wireless signals and channels, which is irrelevant to tracing a wired cable.",
            },
            "exam_pattern": "Find or trace a specific cable in a bundle = tone generator and probe (toner).",
        },
    },
]
