"""CompTIA Network+ N10-009 — Domain 1.0 Networking Concepts EXPANSION pool.

Original, objective-aligned questions that deepen the base `networking_concepts`
items (netplus-nc-001..009) in content_netplus.py to real-exam depth. Same
authoring rules as the other pools: original content mapped to the public
N10-009 objectives, never real exam items. build_content.py shuffles option
order, so the keyed option below is correct on its merits, not by position.

IDs start at netplus-nc-101 to avoid colliding with the base pool. Coverage
spans all eight 1.0 subtopics: osi_model, network_appliances, cloud_concepts,
ports_protocols, traffic_types, ipv4_subnetting_np, ipv6_np, network_topologies.
"""

QUESTIONS = [
    # ===== osi_model ========================================================
    {
        "id": "netplus-nc-101", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 2, "type": "mcq",
        "stem": "As data is encapsulated moving down the OSI model on a sending host, the "
                "Transport layer hands a protocol data unit (PDU) to the Network layer. For a "
                "TCP connection, what is the Transport-layer PDU called?",
        "options": [
            {"id": "A", "text": "Segment"},
            {"id": "B", "text": "Packet"},
            {"id": "C", "text": "Frame"},
            {"id": "D", "text": "Bit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "At the Transport layer (L4), TCP data units are called segments (UDP uses "
                       "datagrams). The Network layer then wraps a segment into a packet.",
            "distractors": {
                "B": "A packet is the Network-layer (L3) PDU, formed when a segment is given IP addressing.",
                "C": "A frame is the Data Link-layer (L2) PDU, built when a packet gets MAC addresses and a trailer.",
                "D": "A bit is the Physical-layer (L1) unit — the raw signal placed on the medium.",
            },
            "exam_pattern": "PDU by layer: L4 segment/datagram, L3 packet, L2 frame, L1 bit.",
        },
    },
    {
        "id": "netplus-nc-102", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 2, "type": "mcq",
        "stem": "Which OSI layer is responsible for establishing, coordinating, and tearing down "
                "the dialog (session) between two communicating applications, including functions "
                "such as checkpointing for recovery?",
        "options": [
            {"id": "A", "text": "Layer 5 - Session"},
            {"id": "B", "text": "Layer 4 - Transport"},
            {"id": "C", "text": "Layer 6 - Presentation"},
            {"id": "D", "text": "Layer 7 - Application"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Session layer (L5) sets up, manages, and terminates sessions/dialogs "
                       "between applications and can insert checkpoints for recovery.",
            "distractors": {
                "B": "The Transport layer (L4) provides end-to-end delivery, segmentation, and TCP/UDP port multiplexing — not dialog control.",
                "C": "The Presentation layer (L6) translates, compresses, and encrypts data formats.",
                "D": "The Application layer (L7) provides network services directly to user programs (HTTP, SMTP, DNS).",
            },
            "exam_pattern": "L5 session/dialog control & checkpoints; L6 format/translate/encrypt; L7 app services.",
        },
    },
    {
        "id": "netplus-nc-103", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "osi_model", "difficulty": 3, "type": "mcq",
        "stem": "A developer must identify the OSI layer that handles data translation between "
                "application and network formats — character-set encoding (such as ASCII to "
                "Unicode), compression, and encryption/decryption formatting. Which layer is this?",
        "options": [
            {"id": "A", "text": "Layer 6 - Presentation"},
            {"id": "B", "text": "Layer 7 - Application"},
            {"id": "C", "text": "Layer 5 - Session"},
            {"id": "D", "text": "Layer 4 - Transport"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Presentation layer (L6) is the translator of the stack: it converts "
                       "character encodings, compresses, and handles encryption/decryption formatting "
                       "so the Application layer receives usable data.",
            "distractors": {
                "B": "The Application layer (L7) exposes network services to user programs (HTTP, FTP, DNS); it does not perform the format translation itself.",
                "C": "The Session layer (L5) manages the dialog between applications, not data representation.",
                "D": "The Transport layer (L4) handles segmentation and reliable/unreliable delivery with ports.",
            },
            "exam_pattern": "L6 Presentation = translate/compress/encrypt (data representation).",
        },
    },

    # ===== network_appliances ===============================================
    {
        "id": "netplus-nc-104", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_appliances", "difficulty": 2, "type": "mcq",
        "stem": "A security appliance is placed inline in the traffic path and is configured to "
                "automatically drop packets that match a known attack signature before they reach "
                "the target host. Which appliance is described?",
        "options": [
            {"id": "A", "text": "IPS (intrusion prevention system)"},
            {"id": "B", "text": "IDS (intrusion detection system)"},
            {"id": "C", "text": "Forward proxy"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IPS sits inline and can actively block/drop malicious traffic in real time, "
                       "not merely alert on it.",
            "distractors": {
                "B": "An IDS is passive and typically out-of-band (on a SPAN port or tap); it detects and alerts but cannot by itself drop the traffic.",
                "C": "A forward proxy fetches web content on behalf of internal clients; it is not an inline attack-blocking sensor.",
                "D": "A load balancer distributes client requests across a server pool; it does not inspect for and drop attacks.",
            },
            "exam_pattern": "Inline + blocks = IPS; passive/out-of-band + alerts only = IDS.",
        },
    },
    {
        "id": "netplus-nc-105", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_appliances", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise deploys 150 lightweight access points across a campus and needs to "
                "centrally push configuration, manage RF channel and power assignments, and "
                "coordinate client roaming. Which device provides this central control?",
        "options": [
            {"id": "A", "text": "Wireless LAN controller (WLC)"},
            {"id": "B", "text": "An autonomous (standalone) access point"},
            {"id": "C", "text": "A Layer 2 access switch"},
            {"id": "D", "text": "A load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A wireless LAN controller centrally manages many lightweight/thin APs — pushing "
                       "configuration and handling RF management (channel/power) and seamless roaming "
                       "from a single point.",
            "distractors": {
                "B": "An autonomous AP is configured individually and does not centrally control other APs, so it does not scale to coordinate 150 APs.",
                "C": "A Layer 2 switch forwards frames and can power APs via PoE, but it does not manage wireless RF or roaming.",
                "D": "A load balancer distributes server traffic and has no role in wireless AP management.",
            },
            "exam_pattern": "Central management of many lightweight APs (RF, roaming) = WLC.",
        },
    },
    {
        "id": "netplus-nc-106", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_appliances", "difficulty": 2, "type": "mcq",
        "stem": "All employee web browsing is directed through a server that fetches pages on the "
                "users' behalf, caches content, and enforces URL/content filtering on outbound "
                "requests. Which appliance is this?",
        "options": [
            {"id": "A", "text": "Forward proxy"},
            {"id": "B", "text": "Reverse proxy"},
            {"id": "C", "text": "Load balancer"},
            {"id": "D", "text": "CDN edge node"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A forward proxy sits between internal clients and the Internet, making outbound "
                       "requests on their behalf — enabling caching, content/URL filtering, and client anonymity.",
            "distractors": {
                "B": "A reverse proxy sits in front of internal servers and handles inbound client requests (e.g., TLS offload, hiding servers) — the opposite direction.",
                "C": "A load balancer spreads inbound traffic across a pool of servers; it is not a client-side web filter/cache.",
                "D": "A CDN edge node caches a provider's content near users but is operated by the content provider, not an enterprise's outbound web filter.",
            },
            "exam_pattern": "Forward proxy = on behalf of internal clients (outbound); reverse proxy = in front of servers (inbound).",
        },
    },

    # ===== cloud_concepts ===================================================
    {
        "id": "netplus-nc-107", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "cloud_concepts", "difficulty": 1, "type": "mcq",
        "stem": "A company wants to rent virtual machines, block storage, and virtual networking "
                "from a provider while retaining full control to install and manage its own "
                "operating systems, middleware, and applications. Which cloud service model fits?",
        "options": [
            {"id": "A", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "SaaS (Software as a Service)"},
            {"id": "D", "text": "DaaS (Desktop as a Service)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IaaS delivers the raw infrastructure (compute, storage, network); the customer "
                       "manages everything from the operating system upward.",
            "distractors": {
                "B": "With PaaS the provider manages the OS and runtime platform, so the customer cannot control the operating system — only the app and data.",
                "C": "SaaS delivers a finished application to end users with no OS or platform access.",
                "D": "DaaS provides hosted virtual desktops to users, not general-purpose infrastructure to build on.",
            },
            "exam_pattern": "IaaS = you manage OS and up; PaaS = app/data only; SaaS = just use the app.",
        },
    },
    {
        "id": "netplus-nc-108", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "cloud_concepts", "difficulty": 2, "type": "mcq",
        "stem": "An organization keeps regulated customer data on its own private cloud but "
                "automatically bursts extra workload to a public cloud provider during seasonal "
                "peaks, with the two environments integrated. Which cloud deployment model is this?",
        "options": [
            {"id": "A", "text": "Hybrid cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Private cloud"},
            {"id": "D", "text": "Community cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hybrid cloud combines private and public resources that are integrated so "
                       "workloads can move between them — cloud bursting to public during peaks is the classic example.",
            "distractors": {
                "B": "A purely public deployment would not keep the regulated data on a private cloud — the scenario uses both.",
                "C": "A purely private cloud has no public-cloud bursting component.",
                "D": "A community cloud is shared by several organizations with common requirements, which is not what is described.",
            },
            "exam_pattern": "Private + public integrated (cloud bursting) = hybrid.",
        },
    },
    {
        "id": "netplus-nc-109", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "cloud_concepts", "difficulty": 3, "type": "mcq",
        "stem": "A cloud platform automatically adds compute instances within minutes when load "
                "rises and removes them when load falls, so capacity continuously tracks real-time "
                "demand. Which cloud characteristic best describes this?",
        "options": [
            {"id": "A", "text": "Elasticity"},
            {"id": "B", "text": "Scalability"},
            {"id": "C", "text": "Multitenancy"},
            {"id": "D", "text": "Network function virtualization (NFV)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Elasticity is the automatic, dynamic scaling OUT and back IN to match demand in "
                       "near real time — provisioning and de-provisioning without manual intervention.",
            "distractors": {
                "B": "Scalability is the broader ability to grow capacity to handle more load, but it does not by itself imply automatic, real-time shrink-and-grow — elasticity is the automatic, bidirectional form.",
                "C": "Multitenancy means multiple customers share the same underlying resources in isolation — unrelated to auto-scaling.",
                "D": "NFV replaces dedicated network hardware with software-based functions on commodity servers — not demand-based auto-scaling.",
            },
            "exam_pattern": "Automatic scale out/in to match demand = elasticity; raw ability to grow = scalability.",
        },
    },

    # ===== ports_protocols ==================================================
    {
        "id": "netplus-nc-110", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 2, "type": "mcq",
        "stem": "A network management station periodically queries devices for interface counters "
                "and also receives unsolicited alert messages when a device event occurs. Which "
                "default ports carry the polling and the alert (trap) traffic, respectively?",
        "options": [
            {"id": "A", "text": "UDP 161 for polling and UDP 162 for traps"},
            {"id": "B", "text": "UDP 162 for polling and UDP 161 for traps"},
            {"id": "C", "text": "TCP 161 for polling and TCP 162 for traps"},
            {"id": "D", "text": "UDP 514 for polling and UDP 161 for traps"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SNMP managers poll agents on UDP 161 (get/set); agents send unsolicited "
                       "traps/informs to the manager on UDP 162.",
            "distractors": {
                "B": "The port roles are reversed — polling is 161 and traps are 162, not the other way around.",
                "C": "SNMP uses UDP, not TCP, for these operations.",
                "D": "UDP 514 is Syslog, not SNMP polling; SNMP polling is UDP 161.",
            },
            "exam_pattern": "SNMP: poll/get = UDP 161, trap = UDP 162.",
        },
    },
    {
        "id": "netplus-nc-111", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 2, "type": "mcq",
        "stem": "An application must authenticate users against a directory service over an "
                "encrypted (TLS-protected) connection. Which protocol and default port should be "
                "configured?",
        "options": [
            {"id": "A", "text": "LDAPS on TCP 636"},
            {"id": "B", "text": "LDAP on TCP 389"},
            {"id": "C", "text": "RDP on TCP 3389"},
            {"id": "D", "text": "HTTPS on TCP 443"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LDAPS is LDAP secured with SSL/TLS and listens on TCP 636 — the right choice "
                       "for an encrypted directory query.",
            "distractors": {
                "B": "Plain LDAP on TCP 389 is unencrypted (cleartext), so it does not meet the encrypted-connection requirement.",
                "C": "RDP (TCP 3389) is a remote desktop protocol, not a directory-access protocol.",
                "D": "HTTPS (TCP 443) secures web traffic, not LDAP directory queries.",
            },
            "exam_pattern": "LDAP = 389 (cleartext); LDAPS = 636 (TLS).",
        },
    },
    {
        "id": "netplus-nc-112", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ports_protocols", "difficulty": 2, "type": "multi",
        "stem": "A firewall rule set must permit two services from network devices to a management "
                "server: accurate time synchronization and centralized event logging. Which two "
                "default UDP ports must be allowed? (Choose two.)",
        "options": [
            {"id": "A", "text": "UDP 123 (NTP)"},
            {"id": "B", "text": "UDP 514 (Syslog)"},
            {"id": "C", "text": "UDP 161 (SNMP)"},
            {"id": "D", "text": "UDP 69 (TFTP)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Time synchronization uses NTP on UDP 123, and centralized logging commonly "
                       "uses Syslog on UDP 514.",
            "distractors": {
                "C": "UDP 161 is SNMP polling — monitoring, not time sync or logging.",
                "D": "UDP 69 is TFTP (trivial file transfer), used for firmware/config transfers, not time or logging.",
            },
            "exam_pattern": "NTP = UDP 123; Syslog = UDP 514.",
        },
    },

    # ===== traffic_types ====================================================
    {
        "id": "netplus-nc-113", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "traffic_types", "difficulty": 2, "type": "multi",
        "stem": "A technician is classifying IPv4 delivery methods. Which two delivery types can "
                "carry a single transmission to more than one recipient? (Choose two.)",
        "options": [
            {"id": "A", "text": "Multicast"},
            {"id": "B", "text": "Broadcast"},
            {"id": "C", "text": "Unicast"},
            {"id": "D", "text": "Anycast"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Multicast delivers one transmission to a group of subscribed hosts, and "
                       "broadcast delivers it to all hosts on the local subnet — both reach multiple recipients.",
            "distractors": {
                "C": "Unicast is strictly one-to-one — a single source to a single destination.",
                "D": "Anycast is addressed to a group but delivered to only the single, topologically nearest member, so just one recipient receives it.",
            },
            "exam_pattern": "Multiple recipients = multicast (group) or broadcast (all local); unicast = one; anycast = nearest one.",
        },
    },
    {
        "id": "netplus-nc-114", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "traffic_types", "difficulty": 3, "type": "mcq",
        "stem": "A content provider advertises the same IP address from many servers in different "
                "regions, and the routing system delivers each client's request to the single "
                "closest server instance. Which addressing/delivery method is this?",
        "options": [
            {"id": "A", "text": "Anycast"},
            {"id": "B", "text": "Multicast"},
            {"id": "C", "text": "Unicast"},
            {"id": "D", "text": "Broadcast"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anycast assigns one address to multiple nodes; the network routes each request "
                       "to the topologically nearest node — widely used for DNS root servers and CDNs.",
            "distractors": {
                "B": "Multicast delivers to all members of a subscribed group at once, not to a single nearest node.",
                "C": "Unicast uses a unique address per host, so it cannot share one address across many regional servers.",
                "D": "Broadcast floods all hosts on a local subnet and is not routed across regions.",
            },
            "exam_pattern": "One shared address, delivered to the nearest of many = anycast.",
        },
    },

    # ===== ipv4_subnetting_np ===============================================
    {
        "id": "netplus-nc-115", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 2, "type": "mcq",
        "stem": "A point-to-point WAN link between two routers needs exactly two usable host "
                "addresses (one per router) with no waste. Using the standard usable-host formula, "
                "which prefix length should be assigned?",
        "options": [
            {"id": "A", "text": "/30"},
            {"id": "B", "text": "/29"},
            {"id": "C", "text": "/28"},
            {"id": "D", "text": "/31"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "/30 (255.255.255.252) yields 2^2 - 2 = 2 usable host addresses — the traditional, "
                       "most efficient choice for a point-to-point link.",
            "distractors": {
                "B": "/29 provides 2^3 - 2 = 6 usable hosts — more than needed, wasting four addresses on a two-host link.",
                "C": "/28 provides 2^4 - 2 = 14 usable hosts — far more than required.",
                "D": "/31 yields 2^1 - 2 = 0 usable hosts under the standard formula; RFC 3021 repurposes a /31 for point-to-point links, but the exam's host-count math treats /30 as the standard two-host subnet.",
            },
            "exam_pattern": "Point-to-point, 2 usable hosts (2^n - 2) = /30.",
        },
    },
    {
        "id": "netplus-nc-116", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 1, "type": "mcq",
        "stem": "A Windows workstation set to obtain an address automatically shows an IPv4 address "
                "of 169.254.80.12 and can reach only other hosts on its own link. What does this "
                "most likely indicate?",
        "options": [
            {"id": "A", "text": "The client failed to reach a DHCP server and self-assigned an APIPA address"},
            {"id": "B", "text": "The DHCP server assigned a valid private (RFC 1918) address"},
            {"id": "C", "text": "The client received a public, Internet-routable address"},
            {"id": "D", "text": "The address is the IPv4 loopback"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "169.254.0.0/16 is the APIPA (link-local) range. A host self-assigns from it only "
                       "when it cannot obtain a lease from a DHCP server, which is why it reaches only the local link.",
            "distractors": {
                "B": "RFC 1918 private ranges are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 — 169.254.x.x is not one of them and is not DHCP-assigned.",
                "C": "169.254.x.x is reserved link-local space and is never a routable public address.",
                "D": "The IPv4 loopback is 127.0.0.1 (127.0.0.0/8), not 169.254.x.x.",
            },
            "exam_pattern": "169.254.x.x = APIPA = DHCP failure, local link only.",
        },
    },
    {
        "id": "netplus-nc-117", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv4_subnetting_np", "difficulty": 3, "type": "mcq",
        "stem": "A host is configured with the IPv4 address 172.16.20.75 /26. What is the network "
                "(subnet) address of the subnet this host belongs to?",
        "options": [
            {"id": "A", "text": "172.16.20.64"},
            {"id": "B", "text": "172.16.20.0"},
            {"id": "C", "text": "172.16.20.72"},
            {"id": "D", "text": "172.16.20.128"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A /26 (255.255.255.192) has a block size of 64 in the last octet, giving subnets "
                       ".0, .64, .128, .192. The host .75 falls in the .64-.127 range, so its network "
                       "address is 172.16.20.64 (broadcast .127).",
            "distractors": {
                "B": "172.16.20.0 is the first /26 subnet (.0-.63); .75 is beyond .63, so it is not in that subnet.",
                "C": "172.16.20.72 is a host address inside the .64 subnet, not the subnet/network address itself.",
                "D": "172.16.20.128 is the next /26 subnet (.128-.191), above the host's range.",
            },
            "exam_pattern": "/26 block size = 64; round the host down to the nearest multiple of the block size for the network address.",
        },
    },

    # ===== ipv6_np ==========================================================
    {
        "id": "netplus-nc-118", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv6_np", "difficulty": 3, "type": "mcq",
        "stem": "During stateless address autoconfiguration (SLAAC), an IPv6 host derives its "
                "64-bit interface identifier from its 48-bit MAC address by splitting the MAC, "
                "inserting FFFE in the middle, and inverting the universal/local (7th) bit. What "
                "is this process called?",
        "options": [
            {"id": "A", "text": "EUI-64"},
            {"id": "B", "text": "DHCPv6 (stateful)"},
            {"id": "C", "text": "Duplicate Address Detection (DAD)"},
            {"id": "D", "text": "NAT64"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EUI-64 expands a 48-bit MAC into a 64-bit interface ID by inserting FFFE between "
                       "the OUI and device portions and flipping the U/L bit; SLAAC can use it to build "
                       "the host portion of an address.",
            "distractors": {
                "B": "DHCPv6 (stateful) has a server assign the full address and options — it does not derive the interface ID from the MAC.",
                "C": "DAD checks whether a tentative address is already in use on the link; it does not generate the interface ID.",
                "D": "NAT64 translates between IPv6 and IPv4 addresses for interoperability — unrelated to building an interface ID.",
            },
            "exam_pattern": "MAC -> 64-bit interface ID (insert FFFE, flip U/L bit) = EUI-64 (used by SLAAC).",
        },
    },
    {
        "id": "netplus-nc-119", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv6_np", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following is the correct fully compressed form of the IPv6 address "
                "2001:0db8:0000:0000:0000:ff00:0042:8329?",
        "options": [
            {"id": "A", "text": "2001:db8::ff00:42:8329"},
            {"id": "B", "text": "2001:db8:0:0:0:ff00:42:8329"},
            {"id": "C", "text": "2001:0db8::ff00:042:8329"},
            {"id": "D", "text": "2001:db8::ff00::42:8329"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Remove the leading zeros in each group (0db8->db8, 0042->42) and replace the single "
                       "longest run of all-zero groups (the three 0000 groups) with one '::', giving "
                       "2001:db8::ff00:42:8329.",
            "distractors": {
                "B": "This correctly drops leading zeros but never applies '::' to the zero groups, so it is valid but not fully compressed.",
                "C": "This keeps leading zeros (0db8 and 042); leading zeros within each group must be removed.",
                "D": "'::' may appear only once in an address; using it twice is invalid and ambiguous.",
            },
            "exam_pattern": "Compression: strip leading zeros per group; replace one longest all-zero run with a single '::'.",
        },
    },
    {
        "id": "netplus-nc-120", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "ipv6_np", "difficulty": 1, "type": "mcq",
        "stem": "To migrate gradually, an enterprise configures its routers, switches, and hosts to "
                "run IPv4 and IPv6 simultaneously on the same interfaces so each application can use "
                "whichever protocol it supports. Which transition mechanism is this?",
        "options": [
            {"id": "A", "text": "Dual stack"},
            {"id": "B", "text": "6to4 tunneling"},
            {"id": "C", "text": "NAT64"},
            {"id": "D", "text": "SLAAC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dual stack runs IPv4 and IPv6 concurrently on the same devices/interfaces, letting "
                       "traffic use either protocol — the most common, straightforward transition approach.",
            "distractors": {
                "B": "6to4 (and similar tunneling) encapsulates IPv6 packets inside IPv4 to cross an IPv4-only network — not running both natively side by side.",
                "C": "NAT64 translates between IPv6-only and IPv4-only hosts; it is for interoperation, not running both stacks on every device.",
                "D": "SLAAC is an IPv6 address-assignment method, not an IPv4/IPv6 coexistence mechanism.",
            },
            "exam_pattern": "Run IPv4 and IPv6 at the same time on the same devices = dual stack.",
        },
    },

    # ===== network_topologies ===============================================
    {
        "id": "netplus-nc-121", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_topologies", "difficulty": 1, "type": "mcq",
        "stem": "In an office LAN, every workstation has its own cable running back to a single "
                "central switch. If one workstation's cable fails, only that workstation loses "
                "connectivity. Which physical topology is this?",
        "options": [
            {"id": "A", "text": "Star"},
            {"id": "B", "text": "Full mesh"},
            {"id": "C", "text": "Bus"},
            {"id": "D", "text": "Ring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In a star topology every node connects to a central device (switch); a single "
                       "node/cable failure affects only that node, although the central device itself "
                       "is a single point of failure.",
            "distractors": {
                "B": "In a full mesh every node links directly to every other node — far more cabling than one central connection per host.",
                "C": "A bus topology shares one backbone cable; a break in the backbone can take down the whole segment.",
                "D": "A ring connects each device to two neighbors in a loop, so a single break can disrupt the ring.",
            },
            "exam_pattern": "All nodes to one central device = star; central device = single point of failure.",
        },
    },
    {
        "id": "netplus-nc-122", "exam": "netplus", "domain": "networking_concepts",
        "subtopic": "network_topologies", "difficulty": 3, "type": "mcq",
        "stem": "A small campus network merges the core and distribution functions onto the same "
                "pair of switches instead of using three separate layers. What is this two-tier "
                "hierarchical design called?",
        "options": [
            {"id": "A", "text": "Collapsed core"},
            {"id": "B", "text": "Three-tier (core/distribution/access)"},
            {"id": "C", "text": "Spine-and-leaf"},
            {"id": "D", "text": "Full mesh"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A collapsed-core (two-tier) design combines the core and distribution layers into "
                       "one, leaving a collapsed-core layer and an access layer — common and cost-effective "
                       "for smaller networks.",
            "distractors": {
                "B": "The three-tier model keeps core, distribution, and access as three distinct layers — the opposite of collapsing them.",
                "C": "Spine-and-leaf is a data-center fabric (every leaf to every spine), not a campus core/distribution collapse.",
                "D": "Full mesh connects every node to every other node and is not a hierarchical campus tier model.",
            },
            "exam_pattern": "Core + distribution merged into one layer = collapsed core (two-tier).",
        },
    },
]
