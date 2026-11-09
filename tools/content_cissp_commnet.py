"""(ISC)² CISSP pool - Domain 4: Communication and Network Security.

Original, CBK-aligned practice items for the four Communication and Network
Security subtopics:
  * cissp_secure_network_design  - OSI layers, DMZ/segmentation, and zero trust.
  * cissp_network_components      - firewall types, IDS vs IPS, proxies, switches.
  * cissp_secure_channels         - IPsec (AH vs ESP, tunnel vs transport), TLS
                                    vs SSL, and S/MIME.
  * cissp_network_attacks         - SYN flood, ARP poisoning (MITM), DNS cache
                                    poisoning.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_secure_network_design ======================================
    {
        "id": "cissp-net-001", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 2, "type": "mcq",
        "stem": "A network engineer needs to identify the OSI layer at which routers forward traffic and "
                "IP addressing operates. Which layer is this?",
        "options": [
            {"id": "A", "text": "Layer 2 - Data Link"},
            {"id": "B", "text": "Layer 4 - Transport"},
            {"id": "C", "text": "Layer 3 - Network"},
            {"id": "D", "text": "Layer 7 - Application"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Routers forward packets using IP addresses at Layer 3, the Network layer.",
            "distractors": {
                "A": "The Data Link layer (2) uses MAC addresses and is where switches operate.",
                "B": "The Transport layer (4) handles TCP/UDP segments and port numbers.",
                "D": "The Application layer (7) hosts protocols such as HTTP and DNS.",
            },
            "exam_pattern": "Routers and IP = Layer 3 (Network); switches and MAC = Layer 2; TCP/UDP and ports = Layer 4.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - OSI model"],
    },
    {
        "id": "cissp-net-002", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to host public-facing web servers so that, even if a server is "
                "compromised, attackers cannot directly reach the internal corporate network. Which "
                "design BEST achieves this?",
        "options": [
            {"id": "A", "text": "Placing the web servers on the internal LAN with host firewalls"},
            {"id": "B", "text": "Placing the web servers in a DMZ (screened subnet) isolated from the internal network"},
            {"id": "C", "text": "Assigning the web servers public IPs with no segmentation"},
            {"id": "D", "text": "Putting the web servers and domain controllers on the same VLAN"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A DMZ (screened subnet) isolates internet-facing servers between boundary controls so "
                       "a compromise there does not grant direct access to the internal network.",
            "distractors": {
                "A": "Internal placement exposes the LAN directly if the public server is breached.",
                "C": "Removing segmentation provides no isolation at all.",
                "D": "Co-locating public servers with domain controllers dangerously exposes critical infrastructure.",
            },
            "exam_pattern": "Internet-facing systems belong in a DMZ/screened subnet, isolated from the internal network.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Network segmentation and DMZ"],
    },
    {
        "id": "cissp-net-003", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 3, "type": "mcq",
        "stem": "An organization adopts an architecture in which no user or device is trusted by default, "
                "every access request is authenticated and authorized based on identity and context, and "
                "being 'inside the perimeter' grants no implicit trust. Which model is this?",
        "options": [
            {"id": "A", "text": "Zero trust"},
            {"id": "B", "text": "Defense in depth, by itself"},
            {"id": "C", "text": "Flat network design"},
            {"id": "D", "text": "Implicit-trust perimeter (castle-and-moat) model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Zero trust removes implicit trust based on network location and verifies every request "
                       "by identity and context ('never trust, always verify').",
            "distractors": {
                "B": "Defense in depth layers controls but does not, by itself, remove implicit internal trust.",
                "C": "A flat network removes segmentation and increases trust, the opposite goal.",
                "D": "The implicit-trust perimeter model is exactly what zero trust is designed to replace.",
            },
            "exam_pattern": "Zero trust = never trust, always verify; no implicit trust from network location.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Zero trust architecture"],
    },
    {
        "id": "cissp-net-004", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_network_design", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: In the OSI reference model, TCP and UDP - which provide host-to-host "
                "segmentation and use port numbers - operate at Layer ___ (give the layer number).",
        "correct": ["4", "four", "layer 4"],
        "explanation": {
            "correct": "The Transport layer (Layer 4) is where TCP and UDP operate, using ports and providing "
                       "end-to-end segmentation.",
            "exam_pattern": "Transport = Layer 4 (TCP/UDP, ports); Network = Layer 3 (IP, routers); Data Link = "
                            "Layer 2 (MAC, switches).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - OSI model layers"],
    },

    # ===== cissp_network_components =========================================
    {
        "id": "cissp-net-005", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 2, "type": "mcq",
        "stem": "A firewall must track the state of active connections so that return traffic for a "
                "session a user initiated is allowed, while unsolicited inbound traffic is denied. Which "
                "firewall type provides this?",
        "options": [
            {"id": "A", "text": "A static packet-filtering firewall"},
            {"id": "B", "text": "A screening router with only an access control list"},
            {"id": "C", "text": "A Layer 1 hub with port filtering"},
            {"id": "D", "text": "A stateful inspection firewall"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A stateful inspection firewall maintains a state table of active connections, so it "
                       "can permit legitimate return traffic while blocking unsolicited inbound traffic.",
            "distractors": {
                "A": "Static packet filtering evaluates each packet independently, with no awareness of session state.",
                "B": "An ACL-only screening router likewise lacks connection-state tracking.",
                "C": "A hub is a Layer 1 device and cannot filter by connection state at all.",
            },
            "exam_pattern": "Tracking connection state to allow return traffic = stateful inspection (vs stateless packet filtering).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Firewall types"],
    },
    {
        "id": "cissp-net-006", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 2, "type": "mcq",
        "stem": "A security team deploys a sensor inline in the traffic path that can automatically drop "
                "packets matching known attack signatures in real time. Which technology is this?",
        "options": [
            {"id": "A", "text": "Intrusion prevention system (IPS)"},
            {"id": "B", "text": "Intrusion detection system (IDS)"},
            {"id": "C", "text": "A passive network tap"},
            {"id": "D", "text": "A SIEM correlation rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An IPS sits inline and can actively block or drop malicious traffic in real time, not "
                       "just alert on it.",
            "distractors": {
                "B": "An IDS detects and alerts but is typically passive/out-of-band and does not drop traffic.",
                "C": "A network tap only copies traffic for monitoring; it takes no action.",
                "D": "A SIEM correlates collected logs and alerts but does not inline-block packets.",
            },
            "exam_pattern": "Inline + actively blocks = IPS; passive + detects/alerts only = IDS.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - IDS vs IPS"],
    },
    {
        "id": "cissp-net-007", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants a device that terminates client connections, inspects full "
                "application-layer content (such as HTTP requests), and makes requests to the destination "
                "server on the client's behalf. Which component is this?",
        "options": [
            {"id": "A", "text": "A Layer 2 switch"},
            {"id": "B", "text": "A static packet filter"},
            {"id": "C", "text": "An application-level (proxy) gateway"},
            {"id": "D", "text": "A Layer 1 repeater"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An application-level (proxy) gateway operates at Layer 7, terminating connections and "
                       "inspecting full application content before forwarding requests on the client's behalf.",
            "distractors": {
                "A": "A Layer 2 switch forwards frames by MAC address and cannot inspect application content.",
                "B": "A static packet filter examines only header fields, not full application content.",
                "D": "A repeater regenerates signals at Layer 1 with no inspection.",
            },
            "exam_pattern": "Terminates and inspects full Layer 7 content on the client's behalf = application-level (proxy) gateway.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Proxy/application gateways"],
    },
    {
        "id": "cissp-net-008", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_components", "difficulty": 1, "type": "mcq",
        "stem": "Within a single LAN, which device forwards frames between hosts based on their MAC "
                "addresses, operating at the Data Link layer?",
        "options": [
            {"id": "A", "text": "Router"},
            {"id": "B", "text": "Switch"},
            {"id": "C", "text": "Firewall"},
            {"id": "D", "text": "Modem"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A switch forwards frames within a LAN by MAC address at Layer 2 (Data Link).",
            "distractors": {
                "A": "A router forwards packets between networks using IP addresses at Layer 3.",
                "C": "A firewall filters traffic according to policy and is not primarily a MAC-forwarding device.",
                "D": "A modem modulates/demodulates signals for transmission lines, not LAN frame switching.",
            },
            "exam_pattern": "Switch = Layer 2, forwards by MAC within a LAN; router = Layer 3, forwards by IP between networks.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Network devices"],
    },

    # ===== cissp_secure_channels ============================================
    {
        "id": "cissp-net-009", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 3, "type": "mcq",
        "stem": "A site-to-site VPN must provide both confidentiality (encryption) and integrity for the "
                "traffic between two gateways. Within IPsec, which component supplies the confidentiality "
                "that the Authentication Header (AH) alone cannot?",
        "options": [
            {"id": "A", "text": "Encapsulating Security Payload (ESP)"},
            {"id": "B", "text": "Authentication Header (AH) in transport mode"},
            {"id": "C", "text": "Internet Key Exchange (IKE) alone"},
            {"id": "D", "text": "The Security Association (SA) database"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IPsec ESP provides confidentiality (encryption) and optionally integrity and "
                       "authentication; AH provides only integrity and authentication, with no encryption.",
            "distractors": {
                "B": "AH provides integrity and authentication but no confidentiality, in any mode.",
                "C": "IKE negotiates keys and security associations but does not itself encrypt the data traffic.",
                "D": "The SA database stores connection parameters; it does not perform encryption.",
            },
            "exam_pattern": "IPsec ESP = confidentiality (+ optional integrity/auth); AH = integrity/authentication only, no encryption.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - IPsec AH vs ESP"],
    },
    {
        "id": "cissp-net-010", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 3, "type": "mcq",
        "stem": "Two network gateways establish an IPsec VPN that encrypts each entire original IP packet "
                "and encapsulates it within a new IP packet sent between the gateways. Which IPsec mode is "
                "in use?",
        "options": [
            {"id": "A", "text": "Transport mode"},
            {"id": "B", "text": "Tunnel mode"},
            {"id": "C", "text": "Aggressive mode"},
            {"id": "D", "text": "Null-encryption mode"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Tunnel mode encrypts the entire original packet and adds a new IP header, which is the "
                       "standard choice for gateway-to-gateway (site-to-site) VPNs.",
            "distractors": {
                "A": "Transport mode encrypts only the payload and keeps the original IP header, used host-to-host.",
                "C": "Aggressive mode is an IKE phase-1 negotiation option, not a data-protection mode.",
                "D": "Null encryption provides no confidentiality at all.",
            },
            "exam_pattern": "Tunnel mode encrypts the whole original packet (gateway-to-gateway); transport mode "
                            "protects only the payload (host-to-host).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - IPsec tunnel vs transport mode"],
    },
    {
        "id": "cissp-net-011", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 2, "type": "mcq",
        "stem": "An organization is hardening web traffic and is told to disable SSL entirely and use "
                "only modern protocol versions. Which protocol should secure the HTTPS connections instead?",
        "options": [
            {"id": "A", "text": "Telnet"},
            {"id": "B", "text": "Deprecated SSL 3.0"},
            {"id": "C", "text": "TLS (for example, 1.2 or 1.3)"},
            {"id": "D", "text": "Plain HTTP"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "TLS (1.2/1.3) is the modern successor to SSL and secures HTTPS with current, supported "
                       "cryptography.",
            "distractors": {
                "A": "Telnet is an unencrypted remote-access protocol, not a web transport-security protocol.",
                "B": "SSL 3.0 is exactly the deprecated, insecure protocol being disabled.",
                "D": "Plain HTTP provides no encryption at all.",
            },
            "exam_pattern": "TLS (1.2/1.3) supersedes deprecated SSL; disable SSL and legacy TLS versions.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - TLS/SSL"],
    },
    {
        "id": "cissp-net-012", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 2, "type": "mcq",
        "stem": "A company wants users to digitally sign and encrypt individual email messages using "
                "X.509 certificates. Which standard provides this directly for email?",
        "options": [
            {"id": "A", "text": "IPsec"},
            {"id": "B", "text": "SNMPv3"},
            {"id": "C", "text": "SSH"},
            {"id": "D", "text": "S/MIME"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "S/MIME uses X.509 certificates (PKI) to sign and encrypt email messages, providing "
                       "confidentiality, integrity, and sender authentication for mail.",
            "distractors": {
                "A": "IPsec secures IP traffic at the network layer, not individual email messages.",
                "B": "SNMPv3 secures network-management traffic.",
                "C": "SSH secures remote shell and file-transfer sessions, not email message signing/encryption.",
            },
            "exam_pattern": "S/MIME = certificate-based (X.509/PKI) email signing and encryption.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Secure email (S/MIME)"],
    },

    {
        "id": "cissp-net-016", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_secure_channels", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The protocol that provides encrypted remote command-line access and "
                "secure file transfer, and is used to replace the clear-text Telnet protocol, is ________ "
                "(give the acronym).",
        "correct": ["ssh", "secure shell"],
        "explanation": {
            "correct": "SSH (Secure Shell) encrypts remote shell sessions and file transfers, replacing "
                       "clear-text protocols such as Telnet and FTP.",
            "exam_pattern": "SSH = encrypted remote shell/file transfer, the secure replacement for Telnet.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Secure remote access (SSH)"],
    },

    # ===== cissp_network_attacks ============================================
    {
        "id": "cissp-net-013", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sends a flood of TCP connection requests but never completes the three-way "
                "handshake, exhausting the server's table of half-open connections so legitimate users "
                "cannot connect. Which attack is this?",
        "options": [
            {"id": "A", "text": "SYN flood (a denial-of-service attack)"},
            {"id": "B", "text": "Cross-site scripting"},
            {"id": "C", "text": "ARP cache poisoning"},
            {"id": "D", "text": "Password spraying"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SYN flood sends many SYN packets without completing the handshake, filling the "
                       "half-open connection table and denying service to legitimate clients.",
            "distractors": {
                "B": "Cross-site scripting injects scripts into web pages viewed by users, not a handshake attack.",
                "C": "ARP poisoning forges MAC-to-IP mappings for interception, not connection-table exhaustion.",
                "D": "Password spraying tries common passwords across accounts, an authentication attack.",
            },
            "exam_pattern": "Half-open TCP connections exhausting the backlog = SYN flood DoS; mitigate with SYN cookies.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - Denial-of-service attacks"],
    },
    {
        "id": "cissp-net-014", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "On a local network, an attacker sends forged ARP replies so that other hosts associate "
                "the attacker's MAC address with the default gateway's IP, letting the attacker intercept "
                "their traffic. Which attack is this, and what does it enable?",
        "options": [
            {"id": "A", "text": "DNS tunneling; data exfiltration"},
            {"id": "B", "text": "A smurf attack; ICMP amplification"},
            {"id": "C", "text": "ARP poisoning (spoofing); an on-path (man-in-the-middle) position"},
            {"id": "D", "text": "A SYN flood; resource exhaustion"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Forged ARP replies that bind the attacker's MAC to another host's IP (such as the "
                       "gateway) are ARP poisoning, placing the attacker on-path for a man-in-the-middle attack.",
            "distractors": {
                "A": "DNS tunneling encodes data within DNS queries for exfiltration, not MAC/IP spoofing.",
                "B": "A smurf attack uses ICMP broadcast amplification, not ARP replies.",
                "D": "A SYN flood exhausts connection tables and does not reposition traffic.",
            },
            "exam_pattern": "Forged ARP replies mapping the attacker's MAC to another IP = ARP poisoning, enabling "
                            "man-in-the-middle on the LAN.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - ARP poisoning / MITM"],
    },
    {
        "id": "cissp-net-015", "exam": "cissp", "domain": "cissp_comm_net",
        "subtopic": "cissp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "Users who type a legitimate bank URL are silently redirected to a fraudulent site "
                "because false records were injected into a DNS resolver's cache. Which attack is this, "
                "and which control BEST mitigates it?",
        "options": [
            {"id": "A", "text": "SQL injection; parameterized queries"},
            {"id": "B", "text": "DNS cache poisoning; DNSSEC"},
            {"id": "C", "text": "Buffer overflow; address space layout randomization"},
            {"id": "D", "text": "Clickjacking; frame-busting headers"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Injecting false records into a resolver's cache to redirect users is DNS cache "
                       "poisoning; DNSSEC cryptographically authenticates DNS responses to counter it.",
            "distractors": {
                "A": "SQL injection targets databases through untrusted input, not DNS resolution.",
                "C": "A buffer overflow corrupts memory and is unrelated to DNS caches.",
                "D": "Clickjacking tricks users into clicking hidden UI elements, not DNS redirection.",
            },
            "exam_pattern": "Forged records in a resolver's cache = DNS cache poisoning; DNSSEC authenticates DNS responses.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 4 - DNS attacks"],
    },
]
