"""CompTIA A+ Core 1 (220-1101) networking expansion pool — Domain 2.0.

Original, objective-aligned questions that DEEPEN the existing ``networking_a1``
bank (which ships ``aplus1-net-001``..``006`` in content_aplus1.py). Same
authoring rules as the Cisco and Security+ pools: original scenario-based
content mapped to the public 220-1101 objectives, never real exam items.

build_content.py shuffles option order (seeded by id), so the answer key here is
not positionally biased; every wrong option carries its own distractor note. IDs
start at ``aplus1-net-101`` to stay clear of the original six items.
"""

QUESTIONS = [
    # ===== 2.1 Ports & protocols =============================================
    {
        "id": "aplus1-net-101", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 2, "type": "mcq",
        "stem": "A user wants their email to stay stored on the mail server and remain in sync whether "
                "they read it from a phone or a laptop. Which protocol, and its default TCP port, supports "
                "this server-side mailbox access?",
        "options": [
            {"id": "A", "text": "IMAP, TCP 143"},
            {"id": "B", "text": "POP3, TCP 110"},
            {"id": "C", "text": "SMTP, TCP 25"},
            {"id": "D", "text": "HTTPS, TCP 443"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IMAP (TCP 143) keeps messages on the server and synchronizes mailbox state across "
                       "multiple devices.",
            "distractors": {
                "B": "POP3 (TCP 110) typically downloads mail and removes it from the server, so it does not "
                     "keep multiple devices in sync.",
                "C": "SMTP (TCP 25) sends/relays outbound mail between servers; it does not retrieve a mailbox.",
                "D": "HTTPS (TCP 443) carries secure web traffic (e.g., a webmail front-end), not the mail "
                     "retrieval protocol itself.",
            },
            "exam_pattern": "IMAP 143 = server-side multi-device sync; POP3 110 = download-and-remove; SMTP 25 = send.",
        },
    },
    {
        "id": "aplus1-net-102", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 1, "type": "mcq",
        "stem": "To replace insecure Telnet for remote command-line management of a switch, an administrator "
                "enables an encrypted protocol. Which port must the firewall allow?",
        "options": [
            {"id": "A", "text": "TCP 22"},
            {"id": "B", "text": "TCP 23"},
            {"id": "C", "text": "TCP 3389"},
            {"id": "D", "text": "TCP 80"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSH uses TCP 22 to provide an encrypted remote command-line session, the secure "
                       "replacement for Telnet.",
            "distractors": {
                "B": "TCP 23 is Telnet itself — the unencrypted protocol being replaced.",
                "C": "TCP 3389 is RDP, a graphical remote-desktop protocol, not a command-line one.",
                "D": "TCP 80 is HTTP web traffic, unrelated to remote CLI management.",
            },
            "exam_pattern": "SSH 22 = encrypted CLI; Telnet 23 = plaintext CLI; RDP 3389 = graphical remote desktop.",
        },
    },
    {
        "id": "aplus1-net-103", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 2, "type": "multi",
        "stem": "Classic (active-mode) FTP uses two separate TCP ports by default — one for commands and one "
                "for data. Which TWO ports are these? (Choose two.)",
        "options": [
            {"id": "A", "text": "TCP 21"},
            {"id": "B", "text": "TCP 20"},
            {"id": "C", "text": "TCP 22"},
            {"id": "D", "text": "TCP 25"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "FTP uses TCP 21 for the control/command channel and TCP 20 for the active-mode data channel.",
            "distractors": {
                "C": "TCP 22 is SSH, which also carries SFTP/SCP — a different, encrypted transfer method, not FTP.",
                "D": "TCP 25 is SMTP for outbound email, not file transfer.",
            },
            "exam_pattern": "FTP = TCP 21 (control) + TCP 20 (data); SFTP rides SSH on TCP 22.",
        },
    },
    {
        "id": "aplus1-net-104", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 2, "type": "mcq",
        "stem": "Windows file and printer sharing needs to work directly over TCP/IP without legacy NetBIOS. "
                "Which port carries this SMB/CIFS traffic?",
        "options": [
            {"id": "A", "text": "TCP 445"},
            {"id": "B", "text": "TCP 139"},
            {"id": "C", "text": "TCP 143"},
            {"id": "D", "text": "TCP 389"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SMB/CIFS runs directly over TCP 445 (direct hosting), the modern file- and "
                       "printer-sharing port.",
            "distractors": {
                "B": "TCP 139 is the legacy NetBIOS Session Service that older SMB used before direct hosting "
                     "(part of the 137-139 NetBIOS range).",
                "C": "TCP 143 is IMAP email retrieval.",
                "D": "TCP 389 is LDAP directory lookups.",
            },
            "exam_pattern": "SMB/CIFS direct over TCP 445; NetBIOS 137-139 is the legacy path.",
        },
    },
    {
        "id": "aplus1-net-105", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 3, "type": "mcq",
        "stem": "A monitoring server must RECEIVE unsolicited trap notifications sent by SNMP agents on "
                "network devices. Which UDP port does the manager listen on for those traps?",
        "options": [
            {"id": "A", "text": "UDP 162"},
            {"id": "B", "text": "UDP 161"},
            {"id": "C", "text": "TCP 389"},
            {"id": "D", "text": "UDP 67"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SNMP managers receive agent-initiated traps/informs on UDP 162.",
            "distractors": {
                "B": "UDP 161 is where the SNMP AGENT listens for the manager's polling (GET/SET) requests — "
                     "not where traps are received.",
                "C": "TCP/UDP 389 is LDAP for directory services, unrelated to SNMP.",
                "D": "UDP 67 is the DHCP server port, unrelated to SNMP.",
            },
            "exam_pattern": "SNMP agent polled on UDP 161; manager receives traps on UDP 162.",
        },
    },

    # ===== 2.2 Networking hardware ===========================================
    {
        "id": "aplus1-net-106", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A growing office must segment its network into VLANs and prioritize voice traffic with QoS. "
                "Which device supports this configuration?",
        "options": [
            {"id": "A", "text": "Managed switch"},
            {"id": "B", "text": "Unmanaged switch"},
            {"id": "C", "text": "Ethernet hub"},
            {"id": "D", "text": "Wireless access point"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A managed switch exposes a configuration interface for VLANs, QoS, port security, and "
                       "monitoring.",
            "distractors": {
                "B": "An unmanaged switch is plug-and-play with no VLAN, QoS, or management interface.",
                "C": "A hub is a Layer 1 repeater that copies signals to all ports with no intelligence at all.",
                "D": "An access point bridges wireless clients onto the LAN but does not provide switch VLAN/QoS "
                     "configuration.",
            },
            "exam_pattern": "Need VLANs/QoS/management = managed switch; plug-and-play with no config = unmanaged.",
        },
    },
    {
        "id": "aplus1-net-107", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 2, "type": "mcq",
        "stem": "An existing non-PoE switch must deliver power over Ethernet to a single ceiling access point "
                "at the end of one cable run, as cheaply as possible. Which device fits?",
        "options": [
            {"id": "A", "text": "PoE injector"},
            {"id": "B", "text": "PoE switch"},
            {"id": "C", "text": "Patch panel"},
            {"id": "D", "text": "Media converter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A PoE injector adds power to a single Ethernet link between a non-PoE switch and one "
                       "powered device — the cheapest fix for one endpoint.",
            "distractors": {
                "B": "A PoE switch powers every port but means replacing the whole switch just to power one device.",
                "C": "A patch panel only terminates and organizes cabling; it passes no power.",
                "D": "A media converter changes the physical medium (e.g., copper to fiber); it does not supply power.",
            },
            "exam_pattern": "Power one link off a non-PoE switch = PoE injector; power many ports = PoE switch "
                            "(802.3af ~15 W, 802.3at ~30 W at the port).",
        },
    },
    {
        "id": "aplus1-net-108", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 3, "type": "mcq",
        "stem": "An IP phone needs roughly 25 W delivered over its Ethernet cable. Which standard must the "
                "switch support to provide that power?",
        "options": [
            {"id": "A", "text": "802.3at (PoE+)"},
            {"id": "B", "text": "802.3af (PoE)"},
            {"id": "C", "text": "802.11ac"},
            {"id": "D", "text": "802.3ad (LACP)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.3at (PoE+) supplies about 30 W at the port (~25.5 W at the device), enough for a "
                       "25 W load.",
            "distractors": {
                "B": "802.3af (standard PoE) supplies only ~15.4 W at the port (~12.95 W at the device) — not enough.",
                "C": "802.11ac is a Wi-Fi standard and has nothing to do with power delivery.",
                "D": "802.3ad is link aggregation (LACP) — bonding links for bandwidth, not supplying power.",
            },
            "exam_pattern": "802.3af ~15 W, 802.3at (PoE+) ~30 W at the port; a higher draw needs PoE+.",
        },
    },
    {
        "id": "aplus1-net-109", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A fiber-to-the-home ISP installs a box where the incoming optical fiber terminates and is "
                "converted to an Ethernet handoff for the customer's router. What is this device?",
        "options": [
            {"id": "A", "text": "ONT (optical network terminal)"},
            {"id": "B", "text": "Cable modem"},
            {"id": "C", "text": "DSL modem"},
            {"id": "D", "text": "NIC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An ONT terminates the fiber at the premises and converts the optical signal to an "
                       "electrical/Ethernet handoff.",
            "distractors": {
                "B": "A cable modem connects over coaxial DOCSIS, not fiber.",
                "C": "A DSL modem connects over twisted-pair telephone lines, not fiber.",
                "D": "A NIC is the network adapter inside a host, not the ISP's fiber demarcation device.",
            },
            "exam_pattern": "Fiber termination/handoff at the premises = ONT; coax = cable modem; phone line = DSL modem.",
        },
    },
    {
        "id": "aplus1-net-110", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 3, "type": "mcq",
        "stem": "In which networking approach is the control plane (which makes forwarding decisions) "
                "decoupled from the data plane and managed centrally by programmable software?",
        "options": [
            {"id": "A", "text": "Software-defined networking (SDN)"},
            {"id": "B", "text": "A traditional router"},
            {"id": "C", "text": "An unmanaged switch"},
            {"id": "D", "text": "A patch panel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SDN separates the control plane from the data plane and centralizes control in "
                       "programmable software/controllers.",
            "distractors": {
                "B": "A traditional router keeps the control and data planes together inside each box.",
                "C": "An unmanaged switch forwards frames with no programmable control plane at all.",
                "D": "A patch panel is passive cabling hardware with no planes to separate.",
            },
            "exam_pattern": "Control plane separated from data plane + centrally programmable = SDN.",
        },
    },

    # ===== 2.3 Wireless ======================================================
    {
        "id": "aplus1-net-111", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "Which 802.11 wireless standard operates ONLY in the 5 GHz band?",
        "options": [
            {"id": "A", "text": "802.11ac"},
            {"id": "B", "text": "802.11b"},
            {"id": "C", "text": "802.11g"},
            {"id": "D", "text": "802.11n"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.11ac (Wi-Fi 5) operates only in the 5 GHz band and delivers multi-gigabit throughput.",
            "distractors": {
                "B": "802.11b operates only in 2.4 GHz (up to 11 Mbps).",
                "C": "802.11g operates only in 2.4 GHz (up to 54 Mbps).",
                "D": "802.11n is dual-band, working in both 2.4 and 5 GHz (up to 600 Mbps).",
            },
            "exam_pattern": "a/ac = 5 GHz; b/g = 2.4 GHz; n = both; ac is 5 GHz-only and multi-gigabit.",
        },
    },
    {
        "id": "aplus1-net-112", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "Three access points cover the same area on the 2.4 GHz band. Which channel assignment avoids "
                "overlapping, interfering channels?",
        "options": [
            {"id": "A", "text": "1, 6, and 11"},
            {"id": "B", "text": "1, 2, and 3"},
            {"id": "C", "text": "2, 5, and 9"},
            {"id": "D", "text": "1, 6, and 12"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In the 2.4 GHz band, channels 1, 6, and 11 are the standard non-overlapping set (each "
                       "20 MHz channel is spaced far enough apart to avoid overlap).",
            "distractors": {
                "B": "Channels 1, 2, and 3 are adjacent and overlap heavily, so the APs would interfere.",
                "C": "Channels 2, 5, and 9 still overlap and are not the recognized non-overlapping set.",
                "D": "Channel 12 is not usable in North America, and 1/6/12 is not the standard set.",
            },
            "exam_pattern": "2.4 GHz non-overlapping channels = 1, 6, 11.",
        },
    },
    {
        "id": "aplus1-net-113", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "A wireless standard reaches theoretical throughput near 9.6 Gbps and, in its 6E variant, "
                "adds use of the 6 GHz band. Which standard is this?",
        "options": [
            {"id": "A", "text": "802.11ax (Wi-Fi 6/6E)"},
            {"id": "B", "text": "802.11ac (Wi-Fi 5)"},
            {"id": "C", "text": "802.11n (Wi-Fi 4)"},
            {"id": "D", "text": "802.11g"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.11ax (Wi-Fi 6) peaks near 9.6 Gbps and works in 2.4 and 5 GHz; the 6E designation "
                       "adds the 6 GHz band.",
            "distractors": {
                "B": "802.11ac (Wi-Fi 5) is 5 GHz only and tops out well below 9.6 Gbps, with no 6 GHz support.",
                "C": "802.11n peaks around 600 Mbps across 2.4/5 GHz.",
                "D": "802.11g peaks at 54 Mbps in 2.4 GHz.",
            },
            "exam_pattern": "802.11ax = Wi-Fi 6 (~9.6 Gbps); Wi-Fi 6E adds the 6 GHz band.",
        },
    },
    {
        "id": "aplus1-net-114", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 1, "type": "mcq",
        "stem": "A customer taps a smartphone within a few centimeters of a payment terminal to pay. Which "
                "short-range wireless technology is in use?",
        "options": [
            {"id": "A", "text": "NFC"},
            {"id": "B", "text": "Bluetooth"},
            {"id": "C", "text": "Long-range active RFID"},
            {"id": "D", "text": "Infrared"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NFC is a 13.56 MHz technology with a range of only about 4 cm, used for contactless "
                       "tap-to-pay.",
            "distractors": {
                "B": "Bluetooth pairs devices over roughly 10 meters — far beyond a tap and not the standard here.",
                "C": "General/active RFID can be read from centimeters to meters; NFC is the specific ~4 cm, "
                     "tap-to-pay branch of RFID.",
                "D": "Infrared needs line of sight and is used for legacy remotes/data links, not payments.",
            },
            "exam_pattern": "Tap-to-pay at ~4 cm = NFC (a 13.56 MHz, very-short-range form of RFID).",
        },
    },
    {
        "id": "aplus1-net-115", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "A company links two buildings about 3 km apart using directional antennas with clear line of "
                "sight, instead of trenching cable. Which wireless solution is this?",
        "options": [
            {"id": "A", "text": "Long-range fixed wireless"},
            {"id": "B", "text": "Bluetooth"},
            {"id": "C", "text": "NFC"},
            {"id": "D", "text": "A single omnidirectional 2.4 GHz access point"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Long-range fixed wireless uses directional (point-to-point) antennas with line of sight "
                       "to bridge sites kilometers apart.",
            "distractors": {
                "B": "Bluetooth is a personal-area technology effective for only about 10 meters.",
                "C": "NFC works only within a few centimeters.",
                "D": "A single omnidirectional AP radiates in all directions over a small area and cannot bridge "
                     "a multi-kilometer point-to-point link.",
            },
            "exam_pattern": "Multi-kilometer point-to-point with directional antennas + line of sight = long-range "
                            "fixed wireless.",
        },
    },

    # ===== 2.4 Network services ==============================================
    {
        "id": "aplus1-net-116", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 2, "type": "mcq",
        "stem": "A company routes all employee web requests through a server that caches frequently visited "
                "pages and blocks access to disallowed sites. Which server role is this?",
        "options": [
            {"id": "A", "text": "Proxy server"},
            {"id": "B", "text": "Load balancer"},
            {"id": "C", "text": "DNS server"},
            {"id": "D", "text": "Print server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A proxy server sits between clients and the internet to cache content and filter/allow "
                       "outbound web access.",
            "distractors": {
                "B": "A load balancer spreads incoming traffic across multiple back-end servers; it is not for "
                     "caching or filtering user web access.",
                "C": "A DNS server resolves names to IP addresses.",
                "D": "A print server manages shared printers.",
            },
            "exam_pattern": "Caches + filters outbound user web traffic = proxy server.",
        },
    },
    {
        "id": "aplus1-net-117", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 2, "type": "mcq",
        "stem": "A popular website runs on a farm of identical web servers. Which device distributes incoming "
                "client requests across those servers so no single one is overwhelmed?",
        "options": [
            {"id": "A", "text": "Load balancer"},
            {"id": "B", "text": "Proxy server"},
            {"id": "C", "text": "Spam gateway"},
            {"id": "D", "text": "DHCP server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A load balancer distributes inbound requests across a pool of identical servers for "
                       "capacity and availability.",
            "distractors": {
                "B": "A proxy forwards and filters outbound client requests; it is not for distributing inbound "
                     "load across a server pool.",
                "C": "A spam gateway filters inbound email for junk and malware.",
                "D": "A DHCP server leases IP configuration to clients.",
            },
            "exam_pattern": "Spreads inbound load across many identical servers = load balancer.",
        },
    },
    {
        "id": "aplus1-net-118", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 2, "type": "mcq",
        "stem": "A network administrator wants routers, switches, and firewalls to forward their event logs "
                "to one central collector for retention and review. Which server role does this?",
        "options": [
            {"id": "A", "text": "Syslog server"},
            {"id": "B", "text": "Authentication server"},
            {"id": "C", "text": "File server"},
            {"id": "D", "text": "Spam gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A syslog server centrally collects and stores event/log messages forwarded by network "
                       "devices.",
            "distractors": {
                "B": "An authentication server validates credentials (e.g., RADIUS/Active Directory); it is not a "
                     "log collector.",
                "C": "A file server stores user files and shares, not device event logs specifically.",
                "D": "A spam gateway filters inbound email.",
            },
            "exam_pattern": "Centralized collection of device event logs = syslog server.",
        },
    },
    {
        "id": "aplus1-net-119", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 3, "type": "mcq",
        "stem": "A utility uses a specialized system to supervise and collect data from remote industrial "
                "equipment such as pumps and sensors across a facility. This system is BEST described as?",
        "options": [
            {"id": "A", "text": "SCADA"},
            {"id": "B", "text": "UTM"},
            {"id": "C", "text": "Load balancer"},
            {"id": "D", "text": "Proxy server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SCADA (supervisory control and data acquisition) monitors and controls industrial "
                       "processes and equipment as part of an ICS.",
            "distractors": {
                "B": "UTM is an all-in-one security appliance, not an industrial control/monitoring system.",
                "C": "A load balancer distributes network traffic across servers.",
                "D": "A proxy server forwards and filters web requests.",
            },
            "exam_pattern": "Supervisory control + data acquisition for industrial/ICS equipment = SCADA.",
        },
    },
    {
        "id": "aplus1-net-120", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are security appliances whose main purpose is to inspect or filter "
                "traffic, rather than general-purpose server roles? (Choose two.)",
        "options": [
            {"id": "A", "text": "Unified threat management (UTM) appliance"},
            {"id": "B", "text": "Spam gateway"},
            {"id": "C", "text": "Print server"},
            {"id": "D", "text": "File server"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "A UTM combines multiple security functions (firewall, IPS, antivirus, content filtering) "
                       "in one appliance, and a spam gateway inspects/filters inbound email — both are security "
                       "appliances that filter traffic.",
            "distractors": {
                "C": "A print server shares printers; it performs no traffic inspection or filtering.",
                "D": "A file server stores and serves files; it is not a security-filtering device.",
            },
            "exam_pattern": "UTM (multi-function security) and spam gateway (email filtering) are security "
                            "appliances, not general server roles.",
        },
    },

    # ===== 2.5 Internet connection types =====================================
    {
        "id": "aplus1-net-121", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "A remote research cabin has no wired service and connects to the internet through a dish "
                "aimed at an orbiting satellite. Users notice a long delay on video calls. Which connection "
                "type is this?",
        "options": [
            {"id": "A", "text": "Satellite"},
            {"id": "B", "text": "Fiber"},
            {"id": "C", "text": "Cable"},
            {"id": "D", "text": "DSL"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Satellite reaches remote sites via a dish to an orbiting satellite, but the long signal "
                       "path adds high latency — exactly the delay described.",
            "distractors": {
                "B": "Fiber is a wired optical service with very low latency, not a dish link.",
                "C": "Cable uses coaxial DOCSIS over a wired plant, not a satellite.",
                "D": "DSL uses twisted-pair phone lines, which are also wired.",
            },
            "exam_pattern": "Dish to orbit + high latency + remote availability = satellite.",
        },
    },
    {
        "id": "aplus1-net-122", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "A home uses existing twisted-pair telephone wiring for internet, and the ISP warns that "
                "throughput drops the farther the home is from the provider's central office. Which "
                "connection type is this?",
        "options": [
            {"id": "A", "text": "DSL"},
            {"id": "B", "text": "Cable"},
            {"id": "C", "text": "Fiber"},
            {"id": "D", "text": "Cellular"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DSL runs over twisted-pair phone lines and is distance-limited: speed degrades as the "
                       "distance from the central office/DSLAM increases.",
            "distractors": {
                "B": "Cable runs over coaxial lines and shares neighborhood bandwidth; its speed is not tied to "
                     "central-office distance this way.",
                "C": "Fiber maintains high speed over long distances.",
                "D": "Cellular is wireless over carrier towers, not phone wiring.",
            },
            "exam_pattern": "Phone-line copper + speed limited by distance from the CO = DSL.",
        },
    },
    {
        "id": "aplus1-net-123", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 1, "type": "mcq",
        "stem": "A business wants the highest available speeds with the lowest latency and symmetric "
                "upload/download, delivered over strands of glass. Which connection type should it choose?",
        "options": [
            {"id": "A", "text": "Fiber"},
            {"id": "B", "text": "Satellite"},
            {"id": "C", "text": "DSL"},
            {"id": "D", "text": "Cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fiber uses optical glass strands to deliver the highest speeds and lowest latency, and "
                       "can offer symmetric upload/download.",
            "distractors": {
                "B": "Satellite has high latency and generally lower throughput.",
                "C": "DSL speeds are limited and degrade with distance from the CO.",
                "D": "Cable is fast but typically asymmetric and shares bandwidth among subscribers in an area.",
            },
            "exam_pattern": "Glass + top speed + lowest latency + symmetric = fiber.",
        },
    },
    {
        "id": "aplus1-net-124", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "A field technician needs internet on a laptop anywhere there is carrier coverage, with no "
                "fixed antenna and no wired drop. Which connection type best fits?",
        "options": [
            {"id": "A", "text": "Cellular (4G/5G)"},
            {"id": "B", "text": "Fixed wireless"},
            {"id": "C", "text": "DSL"},
            {"id": "D", "text": "Cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cellular (4G LTE/5G) provides mobile broadband anywhere a carrier has coverage, with no "
                       "fixed installation.",
            "distractors": {
                "B": "Fixed wireless needs a stationary antenna aimed with line of sight at the ISP's tower — "
                     "it is not mobile.",
                "C": "DSL requires a wired phone-line drop at a fixed location.",
                "D": "Cable requires a wired coaxial drop at a fixed location.",
            },
            "exam_pattern": "Mobile, anywhere-with-coverage = cellular (4G/5G); fixed wireless needs a fixed, "
                            "line-of-sight antenna.",
        },
    },
]
