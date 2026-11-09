"""(ISC)² Certified in Cybersecurity (CC) pool - Domain 4: Network Security.

Original, objective-aligned practice items for the four Network Security subtopics
CertLab tracks:
  * cc_network_concepts        - OSI/TCP-IP basics, TCP vs. UDP, well-known ports,
                                 IPv4/IPv6 addressing, and the TCP handshake.
  * cc_network_threats_attacks - malware types (virus/worm/Trojan/ransomware),
                                 DoS/DDoS, man-in-the-middle, and phishing.
  * cc_network_defense         - firewalls, IDS vs. IPS, VPNs, segmentation, and
                                 zero trust.
  * cc_secure_infrastructure   - cloud service models, DMZ/screened subnet design,
                                 and data-center environmental controls.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased, every
wrong option carries a distractor note, and each item names the (ISC)² CC exam-outline
area it draws on. Entry-level depth only - core, well-established facts.
"""

QUESTIONS = [
    # ===== cc_network_concepts ==============================================
    {
        "id": "isc2cc-net-001", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_concepts", "difficulty": 2, "type": "mcq",
        "stem": "A router forwards packets between networks using IP addresses to decide the path. At "
                "which layer of the OSI model does this routing operate?",
        "options": [
            {"id": "A", "text": "Layer 2 - Data Link"},
            {"id": "B", "text": "Layer 3 - Network"},
            {"id": "C", "text": "Layer 4 - Transport"},
            {"id": "D", "text": "Layer 7 - Application"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Network layer (Layer 3) handles logical addressing (IP) and routing of packets "
                       "between different networks - the job of a router.",
            "distractors": {
                "A": "Layer 2 (Data Link) uses MAC addresses and is where switches forward frames within a network.",
                "C": "Layer 4 (Transport) manages end-to-end delivery with TCP/UDP, not packet routing between networks.",
                "D": "Layer 7 (Application) is where user-facing protocols like HTTP operate, not IP routing.",
            },
            "exam_pattern": "IP addressing and routing = Layer 3 (Network); MAC/switching = Layer 2.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network concepts (OSI model)"],
    },
    {
        "id": "isc2cc-net-002", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_concepts", "difficulty": 2, "type": "mcq",
        "stem": "An application needs reliable delivery with acknowledgments and will set up a "
                "connection before sending data. Which transport-layer protocol fits this requirement?",
        "options": [
            {"id": "A", "text": "UDP"},
            {"id": "B", "text": "TCP"},
            {"id": "C", "text": "ICMP"},
            {"id": "D", "text": "ARP"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "TCP is connection-oriented and reliable: it establishes a connection and uses "
                       "acknowledgments and retransmission to guarantee ordered delivery.",
            "distractors": {
                "A": "UDP is connectionless and does not guarantee delivery; it trades reliability for speed.",
                "C": "ICMP carries control/diagnostic messages (like ping); it is not a reliable data-transport protocol.",
                "D": "ARP maps IP addresses to MAC addresses on a local network; it does not transport application data.",
            },
            "exam_pattern": "Reliable, connection-oriented, acknowledged = TCP; fast, connectionless = UDP.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network concepts (TCP vs. UDP)"],
    },
    {
        "id": "isc2cc-net-003", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_concepts", "difficulty": 1, "type": "mcq",
        "stem": "A firewall administrator needs to allow secure, encrypted web (HTTPS) traffic to a "
                "server. Which well-known TCP port must be permitted?",
        "options": [
            {"id": "A", "text": "80"},
            {"id": "B", "text": "22"},
            {"id": "C", "text": "443"},
            {"id": "D", "text": "25"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "HTTPS (HTTP over TLS) uses well-known TCP port 443 for encrypted web traffic.",
            "distractors": {
                "A": "Port 80 is used by unencrypted HTTP, not HTTPS.",
                "B": "Port 22 is used by SSH for secure remote administration, not web traffic.",
                "D": "Port 25 is used by SMTP for sending email, not HTTPS.",
            },
            "exam_pattern": "HTTPS = 443, HTTP = 80, SSH = 22, SMTP = 25.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network concepts (ports/protocols)"],
    },
    {
        "id": "isc2cc-net-004", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_concepts", "difficulty": 1, "type": "mcq",
        "stem": "How many bits are in a standard IPv4 address?",
        "options": [
            {"id": "A", "text": "128 bits"},
            {"id": "B", "text": "48 bits"},
            {"id": "C", "text": "64 bits"},
            {"id": "D", "text": "32 bits"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An IPv4 address is 32 bits long, usually written as four decimal octets (e.g., "
                       "192.168.1.10).",
            "distractors": {
                "A": "128 bits is the length of an IPv6 address, not IPv4.",
                "B": "48 bits is the length of a MAC (hardware) address, not an IPv4 address.",
                "C": "64 bits is not the size of either common IP address version.",
            },
            "exam_pattern": "IPv4 = 32 bits; IPv6 = 128 bits; MAC = 48 bits.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network concepts (IPv4/IPv6 addressing)"],
    },
    {
        "id": "isc2cc-net-005", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_concepts", "difficulty": 2, "type": "fill",
        "stem": "Before any data is exchanged, TCP establishes a connection by exchanging SYN, SYN-ACK, "
                "and ACK messages. This setup sequence is known as the three-way ___. (one word)",
        "correct": ["handshake", "handshaking"],
        "explanation": {
            "correct": "The TCP three-way handshake (SYN, SYN-ACK, ACK) establishes a reliable connection "
                       "between two hosts before data transfer begins.",
            "exam_pattern": "SYN -> SYN-ACK -> ACK = the TCP three-way handshake (connection setup).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network concepts (TCP handshake)"],
    },

    # ===== cc_network_threats_attacks =======================================
    {
        "id": "isc2cc-net-006", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks", "difficulty": 2, "type": "mcq",
        "stem": "A piece of malware spreads by itself from computer to computer across the network, "
                "needing no host file and no user action to propagate. Which type of malware is this?",
        "options": [
            {"id": "A", "text": "Spyware"},
            {"id": "B", "text": "Virus"},
            {"id": "C", "text": "Trojan horse"},
            {"id": "D", "text": "Worm"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A worm is self-replicating malware that spreads across networks on its own, without "
                       "attaching to a host file or requiring the user to run it.",
            "distractors": {
                "A": "Spyware secretly gathers information; its defining trait is surveillance, not self-propagation.",
                "B": "A virus attaches to a host file and typically needs user action (opening/running) to spread.",
                "C": "A Trojan horse hides inside something that looks legitimate and relies on the user to run it; it does not self-propagate.",
            },
            "exam_pattern": "Self-spreading, no host/no user action = worm; needs a host + user action = virus.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (malware types)"],
    },
    {
        "id": "isc2cc-net-007", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks", "difficulty": 1, "type": "mcq",
        "stem": "Malware encrypts all of a hospital's files and displays a message demanding payment in "
                "cryptocurrency for the decryption key. This is an example of:",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Adware"},
            {"id": "C", "text": "A rootkit"},
            {"id": "D", "text": "A logic bomb"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ransomware encrypts or locks a victim's data and demands payment (ransom) in "
                       "exchange for restoring access.",
            "distractors": {
                "B": "Adware displays unwanted advertisements; it does not encrypt data for ransom.",
                "C": "A rootkit hides an attacker's presence and maintains stealthy access; it is not defined by demanding ransom.",
                "D": "A logic bomb triggers a malicious action when a condition is met; it is not specifically about ransom demands.",
            },
            "exam_pattern": "Encrypts data and demands payment to restore it = ransomware.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (ransomware)"],
    },
    {
        "id": "isc2cc-net-008", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker directs thousands of compromised devices to flood a company's web server "
                "with traffic until legitimate customers can no longer connect. This attack is a:",
        "options": [
            {"id": "A", "text": "Man-in-the-middle attack"},
            {"id": "B", "text": "Distributed denial-of-service (DDoS) attack"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Phishing campaign"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A DDoS attack uses many distributed, compromised devices (a botnet) to overwhelm a "
                       "target with traffic, denying service to legitimate users - an attack on availability.",
            "distractors": {
                "A": "A man-in-the-middle attack intercepts communications between two parties; it does not flood a server offline.",
                "C": "SQL injection manipulates database queries through input fields; it is not a traffic flood.",
                "D": "Phishing tricks users via deceptive messages; it does not overwhelm a server with traffic.",
            },
            "exam_pattern": "Flood from many sources to knock a service offline = DDoS (availability attack).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (DoS/DDoS)"],
    },
    {
        "id": "isc2cc-net-009", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks", "difficulty": 1, "type": "mcq",
        "stem": "Employees receive a deceptive email that appears to come from the IT department, urging "
                "them to click a link and 'verify' their login credentials. This social-engineering "
                "attack is called:",
        "options": [
            {"id": "A", "text": "Smishing"},
            {"id": "B", "text": "Vishing"},
            {"id": "C", "text": "Phishing"},
            {"id": "D", "text": "Tailgating"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Phishing uses fraudulent emails impersonating a trusted source to trick recipients "
                       "into revealing credentials or clicking malicious links.",
            "distractors": {
                "A": "Smishing is phishing carried out through SMS/text messages, not email.",
                "B": "Vishing is voice phishing conducted over phone calls, not email.",
                "D": "Tailgating is a physical attack - following someone through a secured door - not a deceptive email.",
            },
            "exam_pattern": "Deceptive email for credentials = phishing; by phone = vishing; by text = smishing.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (phishing)"],
    },
    {
        "id": "isc2cc-net-010", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks", "difficulty": 3, "type": "mcq",
        "stem": "On an unsecured public Wi-Fi network, an attacker secretly positions themselves between "
                "a user and a banking website, silently reading and relaying the traffic between them. "
                "Which attack is this?",
        "options": [
            {"id": "A", "text": "Denial-of-service attack"},
            {"id": "B", "text": "Man-in-the-middle (on-path) attack"},
            {"id": "C", "text": "Brute-force attack"},
            {"id": "D", "text": "Privilege escalation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A man-in-the-middle (on-path) attack secretly intercepts and relays communication "
                       "between two parties, letting the attacker read or alter the traffic.",
            "distractors": {
                "A": "A denial-of-service attack disrupts availability; it does not quietly intercept and relay traffic.",
                "C": "A brute-force attack guesses credentials by trying many combinations, not intercepting a live session.",
                "D": "Privilege escalation gains higher rights on a system already accessed; it is not traffic interception.",
            },
            "exam_pattern": "Attacker secretly sits between two parties, reading/altering traffic = man-in-the-middle (on-path).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (man-in-the-middle)"],
    },

    # ===== cc_network_defense ===============================================
    {
        "id": "isc2cc-net-011", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_defense", "difficulty": 1, "type": "mcq",
        "stem": "A device is placed at the boundary between a company's internal network and the "
                "internet to allow or block traffic according to a set of rules. This device is a:",
        "options": [
            {"id": "A", "text": "Firewall"},
            {"id": "B", "text": "Network switch"},
            {"id": "C", "text": "Network hub"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A firewall enforces an access-control policy on network traffic, permitting or "
                       "denying packets based on rules, typically at the network boundary.",
            "distractors": {
                "B": "A switch forwards frames within a LAN based on MAC addresses; it does not filter by a security policy.",
                "C": "A hub simply repeats traffic to all ports; it makes no filtering decisions.",
                "D": "A load balancer distributes traffic across servers for performance; it is not primarily a traffic-filtering control.",
            },
            "exam_pattern": "Allows/blocks traffic by rules at a boundary = firewall.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network defense (firewalls)"],
    },
    {
        "id": "isc2cc-net-012", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_defense", "difficulty": 3, "type": "mcq",
        "stem": "A security team wants a device that sits inline in the traffic path and can "
                "automatically BLOCK malicious packets in real time, not merely raise an alert. Which "
                "technology should they deploy?",
        "options": [
            {"id": "A", "text": "Intrusion Detection System (IDS)"},
            {"id": "B", "text": "Intrusion Prevention System (IPS)"},
            {"id": "C", "text": "Syslog server"},
            {"id": "D", "text": "Network tap"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An IPS sits inline and can actively block or drop malicious traffic as it passes, "
                       "going beyond detection to prevention.",
            "distractors": {
                "A": "An IDS only monitors and alerts on suspicious activity; it does not block traffic by itself.",
                "C": "A syslog server collects and stores log messages; it does not inspect or block live traffic.",
                "D": "A network tap passively copies traffic for monitoring; it cannot block anything.",
            },
            "exam_pattern": "Inline + automatically blocks = IPS; monitors + only alerts = IDS.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network defense (IDS vs. IPS)"],
    },
    {
        "id": "isc2cc-net-013", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "A remote employee needs to connect to the corporate network over the public internet "
                "with their traffic encrypted inside a secure tunnel. Which technology provides this?",
        "options": [
            {"id": "A", "text": "DHCP (Dynamic Host Configuration Protocol)"},
            {"id": "B", "text": "VLAN (Virtual Local Area Network)"},
            {"id": "C", "text": "DNS (Domain Name System)"},
            {"id": "D", "text": "VPN (Virtual Private Network)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A VPN creates an encrypted tunnel across an untrusted network (the internet), "
                       "protecting the confidentiality and integrity of the remote user's traffic.",
            "distractors": {
                "A": "DHCP automatically assigns IP addresses to hosts; it does not secure remote connections.",
                "B": "A VLAN logically segments a LAN into broadcast domains; it does not encrypt traffic over the internet.",
                "C": "DNS resolves domain names to IP addresses; it provides no encrypted tunnel.",
            },
            "exam_pattern": "Encrypted tunnel over the internet for remote access = VPN.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network defense (VPN)"],
    },
    {
        "id": "isc2cc-net-014", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_defense", "difficulty": 2, "type": "fill",
        "stem": "Dividing a network into smaller, isolated zones - so that a compromise in one zone "
                "cannot easily spread to the others - is called network ___. (one word)",
        "correct": ["segmentation", "segment", "segmenting", "segregation"],
        "explanation": {
            "correct": "Network segmentation separates a network into isolated zones (using VLANs, "
                       "subnets, or firewalls), containing threats and limiting lateral movement.",
            "exam_pattern": "Isolating network zones to contain threats = segmentation.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network defense (segmentation)"],
    },
    {
        "id": "isc2cc-net-015", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_network_defense", "difficulty": 2, "type": "mcq",
        "stem": "A modern security model assumes no user or device is trustworthy by default - even "
                "inside the corporate network - and verifies every access request explicitly. This "
                "approach is known as:",
        "options": [
            {"id": "A", "text": "Zero trust"},
            {"id": "B", "text": "Implicit trust"},
            {"id": "C", "text": "Perimeter-only security"},
            {"id": "D", "text": "Open access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Zero trust operates on 'never trust, always verify': no user or device is trusted "
                       "by default, and every request is authenticated and authorized, regardless of location.",
            "distractors": {
                "B": "Implicit trust is the opposite - trusting entities automatically once inside the network.",
                "C": "Perimeter-only security trusts everything inside the boundary, which zero trust explicitly rejects.",
                "D": "Open access applies no meaningful access restrictions at all.",
            },
            "exam_pattern": "Never trust, always verify, no implicit trust inside the network = zero trust.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Network defense (zero trust)"],
    },

    # ===== cc_secure_infrastructure =========================================
    {
        "id": "isc2cc-net-016", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure", "difficulty": 2, "type": "mcq",
        "stem": "A small business subscribes to a web-based email application that the provider fully "
                "manages; the business runs no servers and maintains no operating system. Which cloud "
                "service model is this?",
        "options": [
            {"id": "A", "text": "Infrastructure as a Service (IaaS)"},
            {"id": "B", "text": "Platform as a Service (PaaS)"},
            {"id": "C", "text": "Software as a Service (SaaS)"},
            {"id": "D", "text": "On-premises hosting"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "SaaS delivers complete, provider-managed software over the internet; the customer "
                       "just uses the application and manages only its data and accounts.",
            "distractors": {
                "A": "IaaS provides raw infrastructure (VMs, storage) that the customer must configure and manage.",
                "B": "PaaS provides a managed platform for developers to build and deploy their own apps, not a finished email app.",
                "D": "On-premises hosting means the business runs the servers and software itself, which it does not here.",
            },
            "exam_pattern": "Ready-to-use, provider-managed application = SaaS.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (cloud service models)"],
    },
    {
        "id": "isc2cc-net-017", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure", "difficulty": 3, "type": "mcq",
        "stem": "A company must host a public-facing web server reachable from the internet while keeping "
                "the internal network isolated from that exposure. Where should the web server be placed?",
        "options": [
            {"id": "A", "text": "On the database administrator's laptop"},
            {"id": "B", "text": "On the internal LAN alongside employee workstations"},
            {"id": "C", "text": "In a DMZ (screened subnet) between the internet and the internal network"},
            {"id": "D", "text": "Inside the internal finance VLAN"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A DMZ (screened subnet) is an isolated network segment for public-facing servers; "
                       "internet users reach the server there without gaining a path into the internal network.",
            "distractors": {
                "A": "Hosting it on an administrator's laptop is insecure and inappropriate for a public server.",
                "B": "Placing a public server on the internal LAN exposes internal systems to internet-facing risk.",
                "D": "Putting a public web server inside the internal finance VLAN exposes sensitive internal resources.",
            },
            "exam_pattern": "Public-facing servers belong in a DMZ/screened subnet, isolated from the internal network.",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (DMZ/segmentation)"],
    },
    {
        "id": "isc2cc-net-018", "exam": "isc2cc", "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure", "difficulty": 2, "type": "mcq",
        "stem": "In planning a secure data center, which environmental control is essential for keeping "
                "equipment within safe temperature and humidity ranges to preserve availability?",
        "options": [
            {"id": "A", "text": "HVAC (heating, ventilation, and air conditioning)"},
            {"id": "B", "text": "A host-based firewall"},
            {"id": "C", "text": "A VPN concentrator"},
            {"id": "D", "text": "Antivirus software"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "HVAC systems regulate temperature and humidity so servers do not overheat or fail, "
                       "directly supporting the availability of data-center infrastructure.",
            "distractors": {
                "B": "A host-based firewall filters network traffic; it does nothing for temperature or humidity.",
                "C": "A VPN concentrator terminates encrypted tunnels; it is not an environmental control.",
                "D": "Antivirus software detects malware; it has no role in cooling the data center.",
            },
            "exam_pattern": "Data-center temperature/humidity control = HVAC (an environmental/availability control).",
        },
        "references": ["(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (data-center environmental controls)"],
    },
]
