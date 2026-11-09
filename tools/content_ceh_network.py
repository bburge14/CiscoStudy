"""EC-Council CEH v13 pool - Domain 3.0: Network and Perimeter Hacking.

Original, objective-aligned practice items for CertLab's CEH track, covering the
five subtopics of the Network and Perimeter Hacking domain:
  * ceh_sniffing          - active vs passive sniffing, ARP poisoning, MAC
                            flooding, packet analysis (Wireshark), and TLS as the
                            defense.
  * ceh_social_engineering - phishing/vishing/smishing, pretexting,
                            impersonation, tailgating, and other human-focused
                            attacks and defenses.
  * ceh_dos_ddos          - SYN floods, amplification/reflection, botnet-driven
                            DDoS, and DoS vs DDoS.
  * ceh_session_hijacking - stealing an authenticated session via its token and
                            the TLS/flag defenses against it.
  * ceh_evading_ids_fw    - fragmentation, encoding/obfuscation, protocol
                            tunneling, and honeypots.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the attack, tool, or defense) - no working exploit
code, payloads, or step-by-step attack instructions, and never real or memorized
exam items.
"""

QUESTIONS = [
    # ===== ceh_sniffing =====================================================
    {
        "id": "ceh-net-001", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "mcq",
        "stem": "On a switched network, an attacker must manipulate the switch's behavior to see traffic not "
                "destined for their own port. This makes sniffing on switches primarily which kind?",
        "options": [
            {"id": "A", "text": "Passive sniffing"},
            {"id": "B", "text": "Active sniffing"},
            {"id": "C", "text": "Out-of-band sniffing"},
            {"id": "D", "text": "Encrypted sniffing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Switches forward frames only to the destination port, so an attacker must actively inject "
                       "traffic (ARP poisoning, MAC flooding) to capture other hosts' data - active sniffing.",
            "distractors": {
                "A": "Passive sniffing works on hubs, where every frame is already broadcast to all ports.",
                "C": "'Out-of-band sniffing' is not a standard CEH sniffing category.",
                "D": "Encryption protects traffic from being read; it is not a mode of sniffing.",
            },
            "exam_pattern": "Hubs = passive (traffic already shared); switches = active (must poison/flood).",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-002", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sends forged ARP replies so victims associate the attacker's MAC address with "
                "the default gateway's IP, placing the attacker in the traffic path. Which attack is this?",
        "options": [
            {"id": "A", "text": "ARP poisoning (ARP spoofing)"},
            {"id": "B", "text": "DNS amplification"},
            {"id": "C", "text": "SYN flood"},
            {"id": "D", "text": "Cross-site scripting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ARP poisoning sends forged ARP replies that bind the attacker's MAC to another host's IP "
                       "(often the gateway), enabling a man-in-the-middle position on the LAN.",
            "distractors": {
                "B": "DNS amplification is a reflection-based DDoS technique, not LAN traffic redirection.",
                "C": "A SYN flood exhausts a server's connection table; it does not redirect LAN traffic.",
                "D": "Cross-site scripting injects script into web pages; it is unrelated to ARP.",
            },
            "exam_pattern": "Forged ARP replies to redirect LAN traffic = ARP poisoning (enables MITM).",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-003", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "mcq",
        "stem": "An attacker floods a switch with a huge number of bogus source MAC addresses to overflow its "
                "CAM table, forcing it to broadcast frames out all ports. Which attack is this?",
        "options": [
            {"id": "A", "text": "Smurf attack"},
            {"id": "B", "text": "Evil twin"},
            {"id": "C", "text": "MAC flooding"},
            {"id": "D", "text": "Session fixation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "MAC flooding overruns the switch's CAM/MAC address table; when it fails open, the switch "
                       "behaves like a hub and broadcasts frames, letting the attacker sniff them.",
            "distractors": {
                "A": "A Smurf attack is an ICMP amplification denial-of-service, not CAM-table abuse.",
                "B": "An evil twin is a rogue wireless access point, not a switch attack.",
                "D": "Session fixation is a web session attack, unrelated to switch CAM tables.",
            },
            "exam_pattern": "Overflow the switch CAM table to force fail-open flooding = MAC flooding.",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-004", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 1, "type": "mcq",
        "stem": "Which tool captures and inspects packets frame-by-frame and is commonly used to analyze "
                "traffic that a sniffer has collected?",
        "options": [
            {"id": "A", "text": "Hydra"},
            {"id": "B", "text": "Nikto"},
            {"id": "C", "text": "Aircrack-ng"},
            {"id": "D", "text": "Wireshark"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Wireshark is the standard packet analyzer, decoding captured frames protocol-by-protocol "
                       "for inspection.",
            "distractors": {
                "A": "Hydra is an online password-guessing tool, not a packet analyzer.",
                "B": "Nikto scans web servers for known issues; it does not analyze packets.",
                "C": "Aircrack-ng cracks wireless encryption keys; it is not a general packet analyzer.",
            },
            "exam_pattern": "Frame-level packet capture/analysis = Wireshark; encrypting traffic (TLS) defends against sniffing.",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },

    # ===== ceh_social_engineering ===========================================
    {
        "id": "ceh-net-005", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 1, "type": "mcq",
        "stem": "Employees receive an email that appears to come from IT urging them to click a link and "
                "'verify' their password on a lookalike site. Which social-engineering attack is this?",
        "options": [
            {"id": "A", "text": "Phishing"},
            {"id": "B", "text": "Tailgating"},
            {"id": "C", "text": "Dumpster diving"},
            {"id": "D", "text": "Shoulder surfing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Phishing uses a deceptive email and a lookalike site to trick users into revealing "
                       "credentials or clicking malicious links.",
            "distractors": {
                "B": "Tailgating is physically following someone through a secure door, not an email lure.",
                "C": "Dumpster diving searches discarded materials for useful information.",
                "D": "Shoulder surfing is watching a victim's screen or keyboard to capture data.",
            },
            "exam_pattern": "Deceptive email plus lookalike site to harvest credentials = phishing.",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-006", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker phones the help desk posing as a senior executive and invents an urgent story to "
                "pressure staff into resetting an account. Which technique is primarily at work?",
        "options": [
            {"id": "A", "text": "Smishing"},
            {"id": "B", "text": "Vishing with pretexting"},
            {"id": "C", "text": "Watering hole attack"},
            {"id": "D", "text": "SQL injection"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Voice-based deception is vishing, and the invented backstory used to justify the request "
                       "is pretexting; together they pressure the help desk into acting.",
            "distractors": {
                "A": "Smishing delivers the lure by SMS text message, not a phone call.",
                "C": "A watering hole compromises a website the target is known to visit, not a phone call.",
                "D": "SQL injection is a database attack, not social engineering.",
            },
            "exam_pattern": "Phone-based deception = vishing; the invented backstory = pretexting.",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-007", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An unauthorized person slips through a badge-controlled door by closely following an "
                "employee who just badged in. Which physical social-engineering technique is this?",
        "options": [
            {"id": "A", "text": "Phishing"},
            {"id": "B", "text": "Email impersonation"},
            {"id": "C", "text": "Tailgating (piggybacking)"},
            {"id": "D", "text": "Credential stuffing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Following an authorized person through a secure door without badging is tailgating "
                       "(piggybacking); mantraps and security awareness are common defenses.",
            "distractors": {
                "A": "Phishing is an electronic lure, not physical entry.",
                "B": "Email impersonation is remote deception, not walking through a door.",
                "D": "Credential stuffing replays leaked credentials online; it is not physical entry.",
            },
            "exam_pattern": "Follow someone through a secure door = tailgating/piggybacking (mantraps defend).",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },

    # ===== ceh_dos_ddos =====================================================
    {
        "id": "ceh-net-008", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sends a flood of TCP SYN packets with spoofed sources and never completes the "
                "handshakes, exhausting the server's half-open connection table. Which attack is this?",
        "options": [
            {"id": "A", "text": "SYN flood"},
            {"id": "B", "text": "ARP poisoning"},
            {"id": "C", "text": "Cross-site request forgery"},
            {"id": "D", "text": "DNS zone transfer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SYN flood leaves many half-open connections that consume the server's connection "
                       "table, denying service to legitimate clients; SYN cookies are a standard defense.",
            "distractors": {
                "B": "ARP poisoning redirects LAN traffic for interception, not connection-table exhaustion.",
                "C": "CSRF abuses a logged-in user's session on a web app; it is not a flooding DoS.",
                "D": "A DNS zone transfer copies DNS records; it is an enumeration issue, not a flood.",
            },
            "exam_pattern": "Half-open connection exhaustion via SYN packets = SYN flood (SYN cookies defend).",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-009", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 3, "type": "mcq",
        "stem": "An attacker sends small DNS or NTP queries with the victim's IP spoofed as the source, so "
                "servers send much larger replies to the victim. Which DDoS technique is this?",
        "options": [
            {"id": "A", "text": "Session hijacking"},
            {"id": "B", "text": "Rainbow table attack"},
            {"id": "C", "text": "Phishing"},
            {"id": "D", "text": "Amplification (reflection) attack"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An amplification/reflection attack spoofs the victim's source address so intermediary "
                       "servers reflect large responses to the victim, multiplying the attacker's bandwidth.",
            "distractors": {
                "A": "Session hijacking takes over an authenticated session; it is not a bandwidth flood.",
                "B": "A rainbow table attack cracks password hashes, unrelated to DDoS.",
                "C": "Phishing is social engineering, not a reflected-traffic flood.",
            },
            "exam_pattern": "Spoofed source plus large reflected replies = amplification/reflection DDoS (DNS, NTP, memcached).",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-010", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 1, "type": "mcq",
        "stem": "What primarily distinguishes a distributed denial-of-service (DDoS) attack from a basic "
                "denial-of-service (DoS) attack?",
        "options": [
            {"id": "A", "text": "DDoS targets only web applications"},
            {"id": "B", "text": "DDoS uses many distributed sources (often a botnet) instead of one"},
            {"id": "C", "text": "DDoS never uses spoofed addresses"},
            {"id": "D", "text": "DDoS only affects wireless networks"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A DDoS attack originates from many distributed systems (commonly a botnet), which makes it "
                       "harder to block and far higher in volume than a single-source DoS.",
            "distractors": {
                "A": "DDoS can target any service or protocol, not only web applications.",
                "C": "DDoS attacks frequently rely on spoofed source addresses.",
                "D": "DDoS is not limited to wireless networks.",
            },
            "exam_pattern": "Many distributed attacking sources (botnet) = DDoS; single source = DoS.",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },

    # ===== ceh_session_hijacking ============================================
    {
        "id": "ceh-net-011", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 2, "type": "mcq",
        "stem": "An attacker steals a valid session token after a user has logged in and uses it to take over "
                "the authenticated session without knowing the password. What is this called?",
        "options": [
            {"id": "A", "text": "Session hijacking"},
            {"id": "B", "text": "Privilege escalation"},
            {"id": "C", "text": "Password spraying"},
            {"id": "D", "text": "Banner grabbing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session hijacking takes over an already-authenticated session by capturing or predicting "
                       "its token, so the attacker need not know the credentials.",
            "distractors": {
                "B": "Privilege escalation raises an account's rights; it does not seize an existing session.",
                "C": "Password spraying guesses common passwords against many accounts.",
                "D": "Banner grabbing reads a service's version; it does not take over sessions.",
            },
            "exam_pattern": "Take over an active authenticated session via its token = session hijacking.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },
    {
        "id": "ceh-net-012", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 2, "type": "mcq",
        "stem": "Which control most directly reduces network-based session hijacking by preventing an attacker "
                "from reading session tokens as they travel the network?",
        "options": [
            {"id": "A", "text": "Disabling ICMP echo replies"},
            {"id": "B", "text": "Increasing the minimum password length"},
            {"id": "C", "text": "Encrypting the session with TLS/HTTPS"},
            {"id": "D", "text": "Enabling more verbose logging"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Encrypting the session end-to-end with TLS keeps the token unreadable in transit, so a "
                       "sniffer cannot capture and reuse it.",
            "distractors": {
                "A": "Disabling ICMP does nothing to protect session tokens.",
                "B": "Longer passwords do not help once a session token has been issued and is being stolen.",
                "D": "Verbose logging may aid detection but does not prevent token interception.",
            },
            "exam_pattern": "Encrypt the channel (TLS) so tokens can't be sniffed = core anti-hijacking defense.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },
    {
        "id": "ceh-net-013", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Web session hijacking typically targets the session ______ - the token a "
                "server issues after login to recognize the authenticated user on later requests.",
        "correct": ["cookie", "id", "identifier", "token"],
        "explanation": {
            "correct": "The session identifier (session cookie/token) is what the server trusts to recognize a "
                       "logged-in user; stealing it enables impersonation. Protect it with TLS and the HttpOnly/Secure flags.",
            "distractors": {},
            "exam_pattern": "Stolen session ID / cookie = hijacked session.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },

    # ===== ceh_evading_ids_fw ===============================================
    {
        "id": "ceh-net-014", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 3, "type": "mcq",
        "stem": "An attacker splits attack traffic into many tiny IP fragments, hoping the IDS fails to "
                "reassemble and inspect them while the target still reassembles the full payload. Which evasion is this?",
        "options": [
            {"id": "A", "text": "Fragmentation (IDS evasion)"},
            {"id": "B", "text": "Salting"},
            {"id": "C", "text": "Pass-the-hash"},
            {"id": "D", "text": "MAC flooding"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fragmentation evasion breaks the payload into small IP fragments so a sensor that does not "
                       "reassemble them the same way as the target misses the signature.",
            "distractors": {
                "B": "Salting protects stored password hashes; it is not an IDS evasion.",
                "C": "Pass-the-hash reuses a hash to authenticate; it does not evade signature inspection.",
                "D": "MAC flooding overflows a switch table; it is not fragmentation-based evasion.",
            },
            "exam_pattern": "Tiny fragments to defeat inspection/reassembly = fragmentation evasion.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-015", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: A ______ is a decoy system deliberately exposed to attract and study "
                "attackers and to detect malicious activity, while holding no real production data.",
        "correct": ["honeypot"],
        "explanation": {
            "correct": "A honeypot is an intentionally enticing decoy with no production value, so any interaction "
                       "with it is inherently suspicious - useful for detection and research. Many linked together form a honeynet.",
            "distractors": {},
            "exam_pattern": "Decoy to lure and observe attackers = honeypot (many = honeynet).",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-016", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 3, "type": "multi",
        "stem": "Which TWO techniques do attackers use to evade intrusion detection systems and firewalls "
                "while delivering a payload? (Choose two.)",
        "options": [
            {"id": "A", "text": "Encoding or obfuscating the payload to avoid signature matches"},
            {"id": "B", "text": "Submitting the payload to the IDS vendor for a new signature"},
            {"id": "C", "text": "Tunneling the traffic inside an allowed protocol such as HTTPS or DNS"},
            {"id": "D", "text": "Publicly announcing the attack in advance"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Encoding/obfuscation defeats signature matching, and tunneling inside an allowed protocol "
                       "(HTTPS, DNS) hides the traffic from perimeter controls - both are classic evasion techniques.",
            "distractors": {
                "B": "Submitting the payload for a signature would help the IDS detect it, the opposite of evasion.",
                "D": "Announcing the attack would alert defenders rather than evade them.",
            },
            "exam_pattern": "Encoding/obfuscation and protocol tunneling (HTTPS/DNS) = common IDS/firewall evasion.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
]
