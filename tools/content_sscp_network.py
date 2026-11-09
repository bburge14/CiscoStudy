"""(ISC)2 SSCP pool - Domain 6: Network and Communications Security.

Original, objective-aligned practice items for the four Network and
Communications Security subtopics tracked in CertLab:
  * sscp_network_models    - the OSI and TCP/IP models, where devices operate,
                             well-known ports, and TCP vs UDP.
  * sscp_network_attacks   - MITM, DoS/DDoS, ARP poisoning, DNS cache poisoning,
                             and spoofing.
  * sscp_network_defense   - stateful firewalls, IDS vs IPS, segmentation/VLANs,
                             and VPNs.
  * sscp_wireless_cellular - WEP/WPA2/WPA3, SAE, and 802.1X/EAP enterprise
                             authentication.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is never positionally biased,
every wrong option carries a distractor note, and each item cites the (ISC)2
SSCP CBK domain it draws on. Practitioner depth, public objectives only, never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== sscp_network_models ==============================================
    {
        "id": "sscp-net-001", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 2, "type": "mcq",
        "stem": "Logical IP addressing and the routing of packets between networks operate at which "
                "layer of the OSI model?",
        "options": [
            {"id": "A", "text": "Layer 2 - Data Link"},
            {"id": "B", "text": "Layer 3 - Network"},
            {"id": "C", "text": "Layer 4 - Transport"},
            {"id": "D", "text": "Layer 7 - Application"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "IP addressing and routing are Layer 3 (Network) functions; routers operate here "
                       "to forward packets between different networks.",
            "distractors": {
                "A": "Layer 2 (Data Link) uses MAC addresses within a local segment, not routable IP addresses.",
                "C": "Layer 4 (Transport) handles segmentation and end-to-end delivery (TCP/UDP ports), not IP routing.",
                "D": "Layer 7 (Application) is where applications interface with the network, not where routing occurs.",
            },
            "exam_pattern": "IP/routing = Layer 3 (Network); MAC/switching = Layer 2; ports/TCP-UDP = Layer 4.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - OSI model"],
    },
    {
        "id": "sscp-net-002", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 2, "type": "mcq",
        "stem": "A traditional Ethernet switch forwards frames based on MAC addresses it learns on each "
                "port. At which OSI layer does this switching primarily operate?",
        "options": [
            {"id": "A", "text": "Layer 1 - Physical"},
            {"id": "B", "text": "Layer 3 - Network"},
            {"id": "C", "text": "Layer 2 - Data Link"},
            {"id": "D", "text": "Layer 4 - Transport"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MAC addressing and frame forwarding are Layer 2 (Data Link) functions, where a "
                       "traditional switch builds its MAC address table and forwards frames.",
            "distractors": {
                "A": "Layer 1 (Physical) moves raw bits/signals; it has no concept of MAC addresses.",
                "B": "Layer 3 (Network) uses IP addresses and is where routers, not basic switches, operate.",
                "D": "Layer 4 (Transport) manages TCP/UDP sessions, not MAC-based frame switching.",
            },
            "exam_pattern": "Switch/MAC/frames = Layer 2; router/IP/packets = Layer 3.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - OSI model and devices"],
    },
    {
        "id": "sscp-net-003", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 1, "type": "mcq",
        "stem": "Which well-known TCP port does HTTPS (HTTP over TLS) use by default?",
        "options": [
            {"id": "A", "text": "443"},
            {"id": "B", "text": "80"},
            {"id": "C", "text": "22"},
            {"id": "D", "text": "25"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "HTTPS uses TCP port 443 by default, carrying HTTP traffic inside a TLS-encrypted "
                       "session.",
            "distractors": {
                "B": "Port 80 is plaintext HTTP, not the encrypted HTTPS service.",
                "C": "Port 22 is SSH (secure remote administration/file transfer), not HTTPS.",
                "D": "Port 25 is SMTP for mail transfer, not HTTPS.",
            },
            "exam_pattern": "HTTPS=443, HTTP=80, SSH=22, SMTP=25, DNS=53, RDP=3389.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Ports and protocols"],
    },
    {
        "id": "sscp-net-004", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_models", "difficulty": 1, "type": "mcq",
        "stem": "An application requires reliable, connection-oriented delivery with sequencing, "
                "acknowledgments, and retransmission of lost data. Which transport-layer protocol "
                "provides these guarantees?",
        "options": [
            {"id": "A", "text": "UDP"},
            {"id": "B", "text": "ICMP"},
            {"id": "C", "text": "ARP"},
            {"id": "D", "text": "TCP"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "TCP is connection-oriented and reliable: it establishes a session (three-way "
                       "handshake), sequences data, acknowledges receipt, and retransmits lost segments.",
            "distractors": {
                "A": "UDP is connectionless and best-effort - fast but with no acknowledgments or retransmission.",
                "B": "ICMP is used for diagnostics and error messaging (e.g., ping), not reliable data transport.",
                "C": "ARP resolves IP addresses to MAC addresses at Layer 2; it is not a transport protocol.",
            },
            "exam_pattern": "Reliable/connection-oriented = TCP; fast/connectionless = UDP.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - TCP vs UDP"],
    },

    # ===== sscp_network_attacks =============================================
    {
        "id": "sscp-net-005", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker on the local LAN broadcasts forged ARP replies that map their own MAC "
                "address to the default gateway's IP address, causing hosts to send their traffic "
                "through the attacker. Which attack is this?",
        "options": [
            {"id": "A", "text": "DNS cache poisoning"},
            {"id": "B", "text": "ARP poisoning (ARP spoofing)"},
            {"id": "C", "text": "SYN flood"},
            {"id": "D", "text": "Smurf attack"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ARP poisoning sends forged ARP replies so victims associate the attacker's MAC "
                       "with another host's IP (often the gateway), letting the attacker intercept "
                       "traffic - a common precursor to a man-in-the-middle attack.",
            "distractors": {
                "A": "DNS cache poisoning corrupts name-to-IP mappings in a resolver, a different layer and mechanism.",
                "C": "A SYN flood exhausts a server's connection table to cause denial of service, not traffic interception.",
                "D": "A Smurf attack uses spoofed ICMP broadcast amplification for DoS, not ARP-based interception.",
            },
            "exam_pattern": "Forged ARP replies mapping attacker MAC to a victim IP = ARP poisoning (enables MITM).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - ARP poisoning"],
    },
    {
        "id": "sscp-net-006", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "After ARP poisoning, an attacker silently relays and can read or modify the traffic "
                "between two hosts that still believe they are communicating directly with each other. "
                "What broader category of attack is this?",
        "options": [
            {"id": "A", "text": "Denial of service"},
            {"id": "B", "text": "Phishing"},
            {"id": "C", "text": "Man-in-the-middle (on-path) attack"},
            {"id": "D", "text": "Privilege escalation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Secretly intercepting and relaying traffic between two parties who believe they "
                       "talk directly is a man-in-the-middle (on-path) attack, enabling eavesdropping "
                       "or tampering.",
            "distractors": {
                "A": "Denial of service aims to make a resource unavailable, not to intercept communications.",
                "B": "Phishing deceives users via fraudulent messages; it does not relay live traffic between hosts.",
                "D": "Privilege escalation raises an attacker's access level on a system, a different objective.",
            },
            "exam_pattern": "Secretly sitting between two parties and relaying traffic = man-in-the-middle / on-path.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Man-in-the-middle attacks"],
    },
    {
        "id": "sscp-net-007", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 1, "type": "mcq",
        "stem": "A public web server becomes unreachable after being overwhelmed by a flood of traffic "
                "originating simultaneously from thousands of compromised hosts in a botnet. Which "
                "attack is this?",
        "options": [
            {"id": "A", "text": "Distributed Denial of Service (DDoS)"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Cross-site scripting (XSS)"},
            {"id": "D", "text": "Man-in-the-middle"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A DDoS attack uses many distributed, compromised hosts (a botnet) to exhaust a "
                       "target's resources or bandwidth, denying service to legitimate users.",
            "distractors": {
                "B": "SQL injection manipulates database queries via input, not a traffic flood.",
                "C": "XSS injects malicious script into web pages viewed by other users; it is not a volumetric flood.",
                "D": "A man-in-the-middle intercepts traffic; it does not aim primarily to deny availability.",
            },
            "exam_pattern": "Many distributed sources flooding one target = DDoS (availability attack).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - DoS/DDoS"],
    },
    {
        "id": "sscp-net-008", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "Users who type the correct URL for their bank are silently redirected to a malicious "
                "look-alike site because forged records were injected into a DNS resolver's cache. "
                "Which attack is this?",
        "options": [
            {"id": "A", "text": "ARP poisoning"},
            {"id": "B", "text": "SYN flood"},
            {"id": "C", "text": "DNS cache poisoning"},
            {"id": "D", "text": "Session fixation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DNS cache poisoning injects falsified name-to-IP mappings into a resolver's "
                       "cache, so correct domain names resolve to attacker-controlled addresses "
                       "(a form of pharming).",
            "distractors": {
                "A": "ARP poisoning operates at Layer 2 with MAC/IP mappings on a LAN, not DNS name resolution.",
                "B": "A SYN flood is a denial-of-service technique, not a redirection via name resolution.",
                "D": "Session fixation forces a known session identifier on a victim; it does not alter DNS resolution.",
            },
            "exam_pattern": "Correct name resolving to a malicious IP via corrupted cache = DNS cache poisoning.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - DNS poisoning"],
    },

    # ===== sscp_network_defense =============================================
    {
        "id": "sscp-net-009", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "Which firewall type maintains a state table of active connections and permits inbound "
                "return traffic only if it belongs to a session that was legitimately initiated from "
                "inside?",
        "options": [
            {"id": "A", "text": "A simple stateless packet filter"},
            {"id": "B", "text": "A stateful inspection firewall"},
            {"id": "C", "text": "An unmanaged network hub"},
            {"id": "D", "text": "A basic Layer 2 switch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A stateful inspection firewall tracks the state of connections and allows return "
                       "traffic only for established sessions, providing stronger control than static "
                       "rules alone.",
            "distractors": {
                "A": "A stateless packet filter evaluates each packet in isolation against rules, with no awareness of session state.",
                "C": "A hub simply repeats signals to all ports and performs no filtering.",
                "D": "A basic switch forwards frames by MAC address and does not inspect or track connection state.",
            },
            "exam_pattern": "Tracks connection state, allows return traffic for established sessions = stateful firewall.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Firewalls"],
    },
    {
        "id": "sscp-net-010", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "A security appliance sits inline, detects malicious traffic in real time, and actively "
                "BLOCKS or drops it before it reaches the protected host. Is this an IDS or an IPS?",
        "options": [
            {"id": "A", "text": "An IDS, which detects and alerts only"},
            {"id": "B", "text": "A DLP system"},
            {"id": "C", "text": "An IPS, which detects and blocks inline"},
            {"id": "D", "text": "A caching proxy"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "An intrusion PREVENTION system (IPS) sits inline and can actively block or drop "
                       "malicious traffic, not merely alert on it.",
            "distractors": {
                "A": "An intrusion DETECTION system (IDS) only detects and alerts; it does not block traffic inline.",
                "B": "DLP focuses on preventing data exfiltration, not inline intrusion blocking.",
                "D": "A caching proxy improves performance/filtering of requests; it is not an inline intrusion blocker.",
            },
            "exam_pattern": "Inline + blocks = IPS; passive + alerts only = IDS.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - IDS vs IPS"],
    },
    {
        "id": "sscp-net-011", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 2, "type": "multi",
        "stem": "A network engineer separates departments into isolated VLANs/subnets. Which TWO "
                "security benefits does this network segmentation provide? (Choose two.)",
        "options": [
            {"id": "A", "text": "It limits an attacker's lateral movement, containing a breach to one segment"},
            {"id": "B", "text": "It reduces the size and scope of broadcast domains"},
            {"id": "C", "text": "It eliminates the need for any firewall or access control"},
            {"id": "D", "text": "It guarantees that all traffic is automatically encrypted"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Segmentation confines a compromise to a single segment (limiting lateral "
                       "movement) and shrinks broadcast domains, improving both security and "
                       "performance. Inter-segment traffic can then be filtered.",
            "distractors": {
                "C": "Segmentation complements but does not replace firewalls and access controls between segments.",
                "D": "Separating traffic into VLANs does not encrypt it; encryption is a separate control.",
            },
            "exam_pattern": "Segmentation = contain lateral movement + smaller broadcast domains (not encryption, not a firewall replacement).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Segmentation and VLANs"],
    },
    {
        "id": "sscp-net-012", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_network_defense", "difficulty": 1, "type": "mcq",
        "stem": "A remote employee needs a secure, encrypted tunnel across the public internet to "
                "reach internal corporate resources as if on the local network. Which technology "
                "provides this?",
        "options": [
            {"id": "A", "text": "Telnet"},
            {"id": "B", "text": "FTP"},
            {"id": "C", "text": "SNMPv1"},
            {"id": "D", "text": "A VPN (e.g., IPsec or TLS)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A VPN builds an encrypted tunnel over an untrusted network (using IPsec or "
                       "TLS/SSL), protecting confidentiality and integrity for remote access.",
            "distractors": {
                "A": "Telnet transmits data, including credentials, in cleartext and provides no tunnel security.",
                "B": "Standard FTP is unencrypted and is a file-transfer protocol, not a secure remote-access tunnel.",
                "C": "SNMPv1 is an unencrypted network-management protocol, not a VPN.",
            },
            "exam_pattern": "Encrypted tunnel over the internet for remote access = VPN (IPsec/TLS).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - VPNs"],
    },

    # ===== sscp_wireless_cellular ===========================================
    {
        "id": "sscp-net-013", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 3, "type": "mcq",
        "stem": "Which Wi-Fi security standard replaces the pre-shared-key 4-way handshake used in its "
                "predecessor with SAE (Simultaneous Authentication of Equals) to resist offline "
                "dictionary attacks and add forward secrecy?",
        "options": [
            {"id": "A", "text": "WEP"},
            {"id": "B", "text": "WPA (original)"},
            {"id": "C", "text": "WPA2"},
            {"id": "D", "text": "WPA3"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "WPA3 introduces SAE (the Dragonfly handshake) in place of WPA2's PSK handshake, "
                       "resisting offline dictionary attacks on captured handshakes and providing "
                       "forward secrecy.",
            "distractors": {
                "A": "WEP is obsolete and insecure (weak RC4/IV usage); it has no SAE.",
                "B": "The original WPA used TKIP and still relied on a PSK handshake, not SAE.",
                "C": "WPA2 (CCMP/AES) uses the 4-way PSK handshake that WPA3's SAE was designed to replace.",
            },
            "exam_pattern": "SAE / Dragonfly and forward secrecy = WPA3; WPA2 = CCMP/AES with PSK handshake.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Wireless security (WPA3/SAE)"],
    },
    {
        "id": "sscp-net-014", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 3, "type": "mcq",
        "stem": "A corporate WLAN authenticates each individual user against a central RADIUS server "
                "(often using certificates) rather than a single shared passphrase. Which standard "
                "provides this port-based network access control?",
        "options": [
            {"id": "A", "text": "IEEE 802.1X (port-based access control using EAP)"},
            {"id": "B", "text": "WPS (Wi-Fi Protected Setup)"},
            {"id": "C", "text": "WEP"},
            {"id": "D", "text": "Static MAC address filtering"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IEEE 802.1X provides port-based access control; it uses EAP methods and a RADIUS "
                       "authentication server to authenticate each user/device (WPA2/WPA3-Enterprise).",
            "distractors": {
                "B": "WPS simplifies device onboarding with a PIN/button and is itself a known security weakness, not enterprise per-user auth.",
                "C": "WEP is an obsolete, broken encryption scheme, not a per-user authentication framework.",
                "D": "MAC filtering is easily spoofed and does not authenticate users to a central server.",
            },
            "exam_pattern": "Per-user WLAN auth via EAP + RADIUS = 802.1X (Enterprise mode).",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - 802.1X / EAP"],
    },
    {
        "id": "sscp-net-015", "exam": "sscp", "domain": "sscp_network_security",
        "subtopic": "sscp_wireless_cellular", "difficulty": 2, "type": "fill",
        "stem": "The original 1990s Wi-Fi security protocol, now deprecated because its weak RC4 "
                "implementation and short initialization vectors make it trivially crackable, is known "
                "by which three-letter acronym? Provide the acronym.",
        "correct": ["wep", "wired equivalent privacy"],
        "explanation": {
            "correct": "WEP (Wired Equivalent Privacy) is obsolete and insecure; its RC4 key/IV weaknesses "
                       "allow keys to be recovered quickly, so WPA2 or WPA3 should be used instead.",
            "distractors": {},
            "exam_pattern": "WEP = broken legacy Wi-Fi security (RC4/weak IVs); never use it - prefer WPA2/WPA3.",
        },
        "references": ["(ISC)2 SSCP CBK: Domain 6 - Wireless security (WEP weaknesses)"],
    },
]
