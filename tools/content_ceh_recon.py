"""EC-Council CEH v13 pool - Domain 1.0: Overview, Reconnaissance and Scanning.

Original, objective-aligned practice items for CertLab's CEH track, mapped to
the public CEH v13 objectives for the five introductory/recon subtopics:
  * ceh_ethics_overview - the five hacking phases (reconnaissance, scanning,
                          gaining access, maintaining access, clearing tracks),
                          hacker classes (white/black/grey hat), and the
                          authorized/scope/rules-of-engagement framing.
  * ceh_footprinting    - passive OSINT: WHOIS, DNS, Google dorking, Shodan,
                          theHarvester; information gathering with little or no
                          target interaction.
  * ceh_scanning        - Nmap scan types (-sS SYN/half-open, -sT connect,
                          -sU UDP, -sV version, -O OS, -sn host discovery) and
                          TCP-flag scans (NULL/FIN/Xmas).
  * ceh_enumeration     - SMB/SNMP/LDAP/NetBIOS enumeration, community strings,
                          service ports, and banner grabbing.
  * ceh_vuln_analysis   - vulnerability scanners (Nessus, OpenVAS/GVM) and the
                          CVE / CVSS / CWE / CPE vocabulary.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored answer key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the tool, phase, technique, or defense) - no working
exploit code, payloads, or step-by-step attack instructions, and never real or
memorized exam items.
"""

QUESTIONS = [
    # ===== ceh_ethics_overview ==============================================
    {
        "id": "ceh-recon-001", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 1, "type": "mcq",
        "stem": "In the five-phase ethical hacking methodology, which phase comes first - gathering "
                "information about the target before any active probing?",
        "options": [
            {"id": "A", "text": "Scanning"},
            {"id": "B", "text": "Reconnaissance"},
            {"id": "C", "text": "Gaining access"},
            {"id": "D", "text": "Clearing tracks"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Reconnaissance (information gathering) is the first phase; the tester collects data "
                       "about the target before scanning or attempting access.",
            "distractors": {
                "A": "Scanning is the second phase, performed after reconnaissance gathers initial information.",
                "C": "Gaining access is the third phase, after the target has been scanned.",
                "D": "Clearing tracks is the final phase, performed after access is gained and maintained.",
            },
            "exam_pattern": "Order: reconnaissance -> scanning -> gaining access -> maintaining access -> clearing tracks.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-002", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "mcq",
        "stem": "A professional is hired under a signed contract to find security weaknesses in a company's "
                "systems and report them so they can be fixed. Which category best describes this person?",
        "options": [
            {"id": "A", "text": "Black hat hacker"},
            {"id": "B", "text": "Hacktivist"},
            {"id": "C", "text": "White hat hacker (ethical hacker)"},
            {"id": "D", "text": "Script kiddie"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A white hat (ethical) hacker tests systems with explicit authorization and reports "
                       "findings so they can be remediated.",
            "distractors": {
                "A": "A black hat acts maliciously and without authorization, the opposite of this scenario.",
                "B": "A hacktivist attacks to promote a political or social cause, not under a client contract.",
                "D": "A script kiddie runs others' tools with little skill and typically without authorization.",
            },
            "exam_pattern": "Authorized plus reports findings = white hat; malicious plus unauthorized = black hat.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-003", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The fifth and final phase of the hacking methodology, in which the "
                "attacker deletes logs and hides evidence to avoid detection, is called ______.",
        "correct": ["clearing tracks", "covering tracks"],
        "explanation": {
            "correct": "Clearing tracks (also called covering tracks) is the last phase, where the attacker "
                       "removes or alters logs and artifacts to evade detection and preserve deniability.",
            "distractors": {},
            "exam_pattern": "Deleting logs / hiding evidence as the last step = clearing (covering) tracks.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-004", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "mcq",
        "stem": "Before an authorized penetration test begins, which document most directly defines which "
                "targets are in scope and the limits the testers must observe?",
        "options": [
            {"id": "A", "text": "The scope and rules of engagement (RoE)"},
            {"id": "B", "text": "The final vulnerability report"},
            {"id": "C", "text": "The CVSS scoring guide"},
            {"id": "D", "text": "The exploit module source code"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scope and the rules of engagement define authorized targets, permitted techniques, "
                       "timing, and limits, keeping the assessment legal and bounded.",
            "distractors": {
                "B": "The final report documents results after testing; it does not set boundaries beforehand.",
                "C": "CVSS scores the severity of findings; it does not define the engagement's scope.",
                "D": "Exploit source code is a tool, not the authorization that bounds the test.",
            },
            "exam_pattern": "Authorized targets plus limits agreed up front = scope / rules of engagement.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },

    # ===== ceh_footprinting =================================================
    {
        "id": "ceh-recon-005", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 1, "type": "mcq",
        "stem": "A tester needs a target domain's registrar, creation and expiry dates, and authoritative "
                "name servers without sending traffic to the organization's own hosts. Which lookup fits?",
        "options": [
            {"id": "A", "text": "SNMP walk"},
            {"id": "B", "text": "Reverse ARP request"},
            {"id": "C", "text": "Nmap -O OS scan"},
            {"id": "D", "text": "WHOIS query"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "WHOIS queries registry/registrar databases and returns the registrar, registration "
                       "dates, and name servers, so it never touches the target's own systems.",
            "distractors": {
                "A": "SNMP walk actively queries a device's management data and needs a community string.",
                "B": "ARP maps IP to MAC on the local link; it does not return domain registration data.",
                "C": "An Nmap OS scan actively probes a live host, which is not passive footprinting.",
            },
            "exam_pattern": "Registrar / dates / name servers with no target interaction = WHOIS.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-006", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "During footprinting, which tool is built to collect email addresses, employee names, and "
                "subdomains for a target by querying public search engines and data sources?",
        "options": [
            {"id": "A", "text": "theHarvester"},
            {"id": "B", "text": "Aircrack-ng"},
            {"id": "C", "text": "John the Ripper"},
            {"id": "D", "text": "Responder"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "theHarvester automates OSINT collection of emails, names, subdomains, and hosts from "
                       "public search engines and databases.",
            "distractors": {
                "B": "Aircrack-ng cracks WEP/WPA wireless keys; it is not an OSINT collector.",
                "C": "John the Ripper is an offline password cracker, not a footprinting tool.",
                "D": "Responder poisons LLMNR/NBT-NS on a local network to capture hashes, not public OSINT.",
            },
            "exam_pattern": "Harvest emails / subdomains / names from public sources = theHarvester.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-007", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "An assessor wants to find Internet-exposed devices such as routers, cameras, and industrial "
                "controllers by their service banners, without scanning them directly. Which resource fits?",
        "options": [
            {"id": "A", "text": "Wireshark"},
            {"id": "B", "text": "Shodan"},
            {"id": "C", "text": "Hydra"},
            {"id": "D", "text": "Hashcat"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Shodan continuously indexes Internet-connected devices and their banners, letting a "
                       "tester discover exposed systems passively.",
            "distractors": {
                "A": "Wireshark captures and analyzes traffic you can already see; it does not index the Internet.",
                "C": "Hydra performs online password guessing against services, not device discovery.",
                "D": "Hashcat cracks password hashes offline; it is unrelated to device discovery.",
            },
            "exam_pattern": "Search Internet-connected devices by banner = Shodan (Censys is similar).",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },

    # ===== ceh_scanning =====================================================
    {
        "id": "ceh-recon-008", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 2, "type": "mcq",
        "stem": "Which Nmap scan sends a SYN, waits for SYN/ACK, then replies with RST instead of completing "
                "the three-way handshake, making it the default stealthy 'half-open' scan?",
        "options": [
            {"id": "A", "text": "-sS (TCP SYN scan)"},
            {"id": "B", "text": "-sT (TCP connect scan)"},
            {"id": "C", "text": "-sU (UDP scan)"},
            {"id": "D", "text": "-sn (host discovery)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The SYN (half-open) scan never finishes the handshake, so it is faster and less likely "
                       "to be logged than a full connect scan.",
            "distractors": {
                "B": "-sT completes the full TCP handshake, which is more likely to be logged by the target.",
                "C": "-sU scans UDP ports and does not use the TCP handshake at all.",
                "D": "-sn only discovers live hosts and scans no ports.",
            },
            "exam_pattern": "Half-open SYN then RST = -sS; full handshake = -sT.",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-009", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 1, "type": "mcq",
        "stem": "A tester wants to learn which hosts in a /24 are alive but deliberately scans no ports. "
                "Which Nmap option performs this host-discovery-only sweep?",
        "options": [
            {"id": "A", "text": "-sV"},
            {"id": "B", "text": "-O"},
            {"id": "C", "text": "-sn"},
            {"id": "D", "text": "-sS"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "-sn (formerly -sP) performs host discovery only, reporting which hosts respond without "
                       "scanning their ports.",
            "distractors": {
                "A": "-sV probes open ports to detect service versions, which requires port scanning.",
                "B": "-O fingerprints the operating system of a host and does scan it.",
                "D": "-sS scans TCP ports via half-open SYN probes, not a discovery-only sweep.",
            },
            "exam_pattern": "Find live hosts, scan no ports = -sn ping sweep.",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-010", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 3, "type": "mcq",
        "stem": "A stateless firewall only drops inbound TCP packets that have the SYN flag set. Which scan "
                "sets the FIN, PSH, and URG flags so its probes can slip past that rule?",
        "options": [
            {"id": "A", "text": "TCP connect scan (-sT)"},
            {"id": "B", "text": "Xmas scan (-sX)"},
            {"id": "C", "text": "SYN scan (-sS)"},
            {"id": "D", "text": "UDP scan (-sU)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Xmas scan lights the FIN, PSH, and URG flags; with no SYN set, it can pass a "
                       "stateless filter that only blocks SYN packets.",
            "distractors": {
                "A": "A connect scan uses SYN to open a full handshake, exactly what the firewall blocks.",
                "C": "A SYN scan also sets the SYN flag, so the rule drops it.",
                "D": "A UDP scan tests UDP ports and does not manipulate TCP flags.",
            },
            "exam_pattern": "FIN+PSH+URG set = Xmas (-sX); no flags = NULL (-sN); FIN only = FIN (-sF).",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-011", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The Nmap option ______ performs service and version detection, probing "
                "open ports to identify the application and version behind each one.",
        "correct": ["-sv", "sv"],
        "explanation": {
            "correct": "-sV (service/version detection) sends probes to open ports and matches the responses "
                       "against a database to report each service's name and version.",
            "distractors": {},
            "exam_pattern": "Identify service and version on open ports = Nmap -sV.",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },

    # ===== ceh_enumeration ==================================================
    {
        "id": "ceh-recon-012", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "mcq",
        "stem": "An attacker reads a device's full configuration and interface list by querying it with the "
                "default read community string 'public'. Which protocol is being abused for enumeration?",
        "options": [
            {"id": "A", "text": "SNMP"},
            {"id": "B", "text": "SMTP"},
            {"id": "C", "text": "HTTP"},
            {"id": "D", "text": "NTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SNMP enumeration abuses default or guessable community strings (like 'public') to read "
                       "a device's management information base (MIB).",
            "distractors": {
                "B": "SMTP moves email; its VRFY/EXPN commands enumerate users, not device configs via community strings.",
                "C": "HTTP serves web content and does not use SNMP community strings.",
                "D": "NTP synchronizes time; it is not queried with community strings for configuration.",
            },
            "exam_pattern": "Community strings (public/private) = SNMP enumeration.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-013", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "mcq",
        "stem": "A tester uses enum4linux to list Windows shares, users, and groups over SMB. Which TCP port "
                "is most associated with this SMB enumeration on modern Windows?",
        "options": [
            {"id": "A", "text": "161"},
            {"id": "B", "text": "389"},
            {"id": "C", "text": "25"},
            {"id": "D", "text": "445"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SMB on modern Windows uses TCP 445 (direct host), the port enum4linux and similar tools "
                       "target for share, user, and group enumeration.",
            "distractors": {
                "A": "UDP 161 is SNMP, not SMB.",
                "B": "TCP 389 is LDAP, used for directory enumeration, not SMB shares.",
                "C": "TCP 25 is SMTP for email, unrelated to SMB.",
            },
            "exam_pattern": "SMB share/user enumeration = TCP 445 (legacy NetBIOS 137-139).",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-014", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 1, "type": "mcq",
        "stem": "Connecting to an open port (for example with Netcat or Telnet) and reading the service's "
                "reply to identify its software and version is called what?",
        "options": [
            {"id": "A", "text": "Banner grabbing"},
            {"id": "B", "text": "ARP spoofing"},
            {"id": "C", "text": "Pass-the-hash"},
            {"id": "D", "text": "Session fixation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Banner grabbing reads a service's self-identifying response to determine the product "
                       "and version running on a port.",
            "distractors": {
                "B": "ARP spoofing poisons the local ARP cache to intercept traffic; it does not read banners.",
                "C": "Pass-the-hash reuses captured password hashes to authenticate; it is not port identification.",
                "D": "Session fixation forces a known session ID on a victim; it is a web attack, not banner reading.",
            },
            "exam_pattern": "Read a service's version reply from an open port = banner grabbing.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },

    # ===== ceh_vuln_analysis ================================================
    {
        "id": "ceh-recon-015", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 1, "type": "mcq",
        "stem": "Which tool scans hosts against a database of known flaws and outputs a prioritized findings "
                "report, but is not itself an exploitation framework?",
        "options": [
            {"id": "A", "text": "Metasploit"},
            {"id": "B", "text": "Nessus"},
            {"id": "C", "text": "Hydra"},
            {"id": "D", "text": "Netcat"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Nessus is a vulnerability scanner: it checks systems against known-flaw signatures and "
                       "reports prioritized findings, without exploiting them.",
            "distractors": {
                "A": "Metasploit is an exploitation framework used to launch and manage exploits, not a scanner.",
                "C": "Hydra is an online password-guessing tool, not a vulnerability scanner.",
                "D": "Netcat is a general-purpose networking utility, not a vulnerability scanner.",
            },
            "exam_pattern": "Scan-and-report known flaws = vulnerability scanner (Nessus, OpenVAS/GVM).",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },
    {
        "id": "ceh-recon-016", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 2, "type": "mcq",
        "stem": "Which framework produces a 0.0 to 10.0 numeric severity rating to help teams prioritize "
                "which vulnerabilities to remediate first?",
        "options": [
            {"id": "A", "text": "CVSS"},
            {"id": "B", "text": "CVE"},
            {"id": "C", "text": "CPE"},
            {"id": "D", "text": "CWE"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CVSS (Common Vulnerability Scoring System) yields a 0.0-10.0 severity score reflecting "
                       "exploitability and impact, used to prioritize remediation.",
            "distractors": {
                "B": "CVE is a unique identifier for a specific vulnerability, not a severity score.",
                "C": "CPE is a structured naming scheme for platforms and products, not a score.",
                "D": "CWE is a catalog of weakness types (e.g., buffer overflow), not a numeric severity rating.",
            },
            "exam_pattern": "0-10 severity number = CVSS; unique vuln ID = CVE.",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },
    {
        "id": "ceh-recon-017", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 3, "type": "multi",
        "stem": "Which TWO statements correctly distinguish a CVE identifier from a CVSS score? (Choose two.)",
        "options": [
            {"id": "A", "text": "A CVE is a unique identifier for a specific, publicly disclosed vulnerability"},
            {"id": "B", "text": "A CVSS score rates a vulnerability's severity on a 0.0-10.0 scale"},
            {"id": "C", "text": "A CVE is itself the numeric severity rating from 0.0 to 10.0"},
            {"id": "D", "text": "A CVSS string is the unique catalog ID assigned to each disclosed vulnerability"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "CVE uniquely names a specific vulnerability; CVSS separately expresses its severity as "
                       "a 0.0-10.0 score. They answer 'which vuln' and 'how severe.'",
            "distractors": {
                "C": "This swaps the terms: the 0.0-10.0 severity number is CVSS, not CVE.",
                "D": "This also swaps them: the unique per-vulnerability identifier is CVE, not CVSS.",
            },
            "exam_pattern": "CVE = identity (which vuln); CVSS = severity (how bad).",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },
]
