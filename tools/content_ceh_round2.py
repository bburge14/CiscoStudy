"""EC-Council CEH v13 pool - Round 2 (deepening expansion).

Original, objective-aligned practice items that DEEPEN the verified round-1 CEH
bank (content_ceh_recon/system/network/web/wireless/cloudcrypto.py). All items
here are NEW and NON-DUPLICATE with respect to round 1: they probe different
tools, flags, attacks, and defenses, or the same concept from a distinctly
different angle. ids use the ``ceh-<prefix>-r2-NNN`` scheme so they never clash
with round-1 ids.

Distribution follows the engine domain weights (network_perimeter 24%,
intro_recon 22%, system_malware 17%, web_hacking 16%, wireless_mobile 13%,
cloud_crypto 8%) -> 25/23/18/16/13/8 = 103 items.

Authoring rules match every other content_*.py pool: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the tool, phase, technique, attack, or defense) - no
working exploit code, payloads, or step-by-step attack instructions, and never
real or memorized exam items.
"""

QUESTIONS = [
    # ====================================================================
    # Domain 1.0 - Overview, Reconnaissance and Scanning  (recon, 23)
    # ====================================================================

    # ----- ceh_ethics_overview (4) -------------------------------------
    {
        "id": "ceh-recon-r2-001", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "mcq",
        "stem": "During an authorized assessment, which team emulates real-world adversaries - their "
                "tools, tactics, and procedures - to test how well the defenders detect and respond?",
        "options": [
            {"id": "A", "text": "Blue team"},
            {"id": "B", "text": "Red team"},
            {"id": "C", "text": "Purple team"},
            {"id": "D", "text": "White team"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The red team plays the attacker, emulating adversary TTPs to test the organization's "
                       "detection and response capabilities.",
            "distractors": {
                "A": "The blue team is the defender - it monitors, detects, and responds, rather than attacking.",
                "C": "The purple team is a function that helps red and blue share findings; it is not the attacking side.",
                "D": "The white team referees the exercise and sets the rules; it does not emulate the adversary.",
            },
            "exam_pattern": "Emulate the adversary = red team; defend = blue team; bridge the two = purple team.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-r2-002", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "mcq",
        "stem": "A tester is given no internal documentation, source, or credentials and must work only from "
                "what an outside attacker could discover. Which testing approach is this?",
        "options": [
            {"id": "A", "text": "White-box testing"},
            {"id": "B", "text": "Gray-box testing"},
            {"id": "C", "text": "Black-box testing"},
            {"id": "D", "text": "Crystal-box testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Black-box testing gives the tester no prior internal knowledge, simulating an external "
                       "attacker who must discover everything.",
            "distractors": {
                "A": "White-box testing provides full internal knowledge (source, architecture, credentials).",
                "B": "Gray-box testing provides partial knowledge, such as a standard user account.",
                "D": "'Crystal-box' is just another name for white-box (full visibility), the opposite of this scenario.",
            },
            "exam_pattern": "No internal knowledge = black-box; full knowledge = white-box; partial = gray-box.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-r2-003", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The fourth phase of the hacking methodology, in which an attacker installs "
                "backdoors or rootkits so they can return to the system later, is called ______ access.",
        "correct": ["maintaining", "maintaining access"],
        "explanation": {
            "correct": "Maintaining access is the fourth phase; after gaining access the attacker ensures future "
                       "re-entry (backdoors, rootkits, trojans) before clearing tracks.",
            "distractors": {},
            "exam_pattern": "Install backdoors to keep returning = maintaining access (phase 4 of 5).",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },
    {
        "id": "ceh-recon-r2-004", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_ethics_overview", "difficulty": 2, "type": "mcq",
        "stem": "A tester directly probes the target - pinging hosts and scanning ports - rather than gathering "
                "data only from third-party sources. Which kind of reconnaissance is this?",
        "options": [
            {"id": "A", "text": "Passive reconnaissance"},
            {"id": "B", "text": "Active reconnaissance"},
            {"id": "C", "text": "Anonymous footprinting"},
            {"id": "D", "text": "Open-source intelligence (OSINT)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Active reconnaissance interacts directly with the target (ping, port scan, banner grab), "
                       "which can be detected, unlike passive collection.",
            "distractors": {
                "A": "Passive reconnaissance gathers information without touching the target's systems.",
                "C": "Anonymous footprinting hides the source of passive collection; it still avoids direct probing.",
                "D": "OSINT uses publicly available data and is a passive technique, not direct probing.",
            },
            "exam_pattern": "Directly probe the target (ping/scan) = active recon; no interaction = passive recon.",
        },
        "references": ["CEH v13 Module 01: Introduction to Ethical Hacking"],
    },

    # ----- ceh_footprinting (6) ----------------------------------------
    {
        "id": "ceh-recon-r2-005", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 3, "type": "mcq",
        "stem": "An attacker queries a misconfigured DNS name server and successfully pulls a full copy of all "
                "the zone's records (hosts, mail servers, aliases). Which technique succeeded?",
        "options": [
            {"id": "A", "text": "DNS zone transfer (AXFR)"},
            {"id": "B", "text": "Reverse DNS lookup"},
            {"id": "C", "text": "WHOIS query"},
            {"id": "D", "text": "DNS amplification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A zone transfer (AXFR) is meant for replication between authoritative servers; if allowed "
                       "to anyone, it hands an attacker the entire DNS record set. Restrict AXFR to known secondaries.",
            "distractors": {
                "B": "A reverse lookup resolves a single IP to a name; it does not dump the whole zone.",
                "C": "WHOIS returns registration data (registrar, dates), not the internal host records.",
                "D": "DNS amplification is a DDoS reflection technique, not a records-disclosure method.",
            },
            "exam_pattern": "Dump all DNS records from a server = zone transfer (AXFR); restrict it to secondaries.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-r2-006", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "A tester uses advanced search-engine operators such as site:, filetype:, and intitle: to find "
                "exposed documents and login pages for a target. What is this technique commonly called?",
        "options": [
            {"id": "A", "text": "Google dorking (Google hacking)"},
            {"id": "B", "text": "Banner grabbing"},
            {"id": "C", "text": "Zone transfer"},
            {"id": "D", "text": "Port knocking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Google dorking uses advanced search operators to surface sensitive files and pages that "
                       "search engines have indexed; the Google Hacking Database (GHDB) catalogs such queries.",
            "distractors": {
                "B": "Banner grabbing reads a service's version from an open port, not search-engine results.",
                "C": "A zone transfer pulls DNS records; it does not use search operators.",
                "D": "Port knocking is an access-control technique that opens a port after a secret sequence.",
            },
            "exam_pattern": "Advanced search operators (site:/filetype:) to find exposed data = Google dorking (GHDB).",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-r2-007", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "Which OSINT tool graphically maps the relationships among people, email addresses, domains, and "
                "infrastructure by running 'transforms' against public data sources?",
        "options": [
            {"id": "A", "text": "Wireshark"},
            {"id": "B", "text": "Maltego"},
            {"id": "C", "text": "Hydra"},
            {"id": "D", "text": "Nessus"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Maltego runs transforms to gather and visually link entities (people, emails, domains, IPs) "
                       "into a relationship graph for reconnaissance.",
            "distractors": {
                "A": "Wireshark analyzes captured packets; it does not build OSINT relationship graphs.",
                "C": "Hydra performs online password guessing against services.",
                "D": "Nessus is a vulnerability scanner, not an OSINT link-analysis tool.",
            },
            "exam_pattern": "Graph relationships among people/domains/IPs via transforms = Maltego.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-r2-008", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "Which modular, menu-driven reconnaissance framework (with a feel similar to Metasploit) uses "
                "pluggable modules to automate web-based OSINT and store results in a workspace database?",
        "options": [
            {"id": "A", "text": "Recon-ng"},
            {"id": "B", "text": "Aircrack-ng"},
            {"id": "C", "text": "John the Ripper"},
            {"id": "D", "text": "Burp Suite"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recon-ng is a full-featured, module-based web reconnaissance framework whose workflow "
                       "resembles Metasploit, automating OSINT collection into a workspace.",
            "distractors": {
                "B": "Aircrack-ng cracks Wi-Fi keys; the '-ng' name is unrelated to OSINT.",
                "C": "John the Ripper is an offline password cracker.",
                "D": "Burp Suite is a web intercepting proxy, not an OSINT framework.",
            },
            "exam_pattern": "Modular, Metasploit-style web OSINT framework = Recon-ng.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-r2-009", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "mcq",
        "stem": "While footprinting a target domain's DNS, which record type reveals the organization's mail "
                "servers - a useful target list for later phishing or relay testing?",
        "options": [
            {"id": "A", "text": "A record"},
            {"id": "B", "text": "CNAME record"},
            {"id": "C", "text": "MX record"},
            {"id": "D", "text": "PTR record"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The MX (Mail eXchanger) record lists the mail servers responsible for a domain, so it maps "
                       "the organization's email infrastructure.",
            "distractors": {
                "A": "An A record maps a hostname to an IPv4 address, not specifically the mail servers.",
                "B": "A CNAME record is an alias pointing one name at another; it does not denote mail servers.",
                "D": "A PTR record supports reverse lookups (IP to name), not mail-server identification.",
            },
            "exam_pattern": "Mail servers for a domain = MX record; host-to-IP = A; alias = CNAME; reverse = PTR.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },
    {
        "id": "ceh-recon-r2-010", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_footprinting", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Using a tool such as HTTrack to download an entire website for offline study "
                "of its structure, comments, and hidden files is called website ______.",
        "correct": ["mirroring", "cloning"],
        "explanation": {
            "correct": "Website mirroring (cloning) copies a whole site locally so the attacker can inspect pages, "
                       "comments, and directory structure offline without repeatedly hitting the live server.",
            "distractors": {},
            "exam_pattern": "Download a whole site for offline analysis (HTTrack) = website mirroring.",
        },
        "references": ["CEH v13 Module 02: Footprinting and Reconnaissance"],
    },

    # ----- ceh_scanning (5) --------------------------------------------
    {
        "id": "ceh-recon-r2-011", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 2, "type": "mcq",
        "stem": "A tester needs to find open UDP services such as SNMP, DNS, and TFTP. Which Nmap scan, slower "
                "and less reliable because there is no handshake to confirm state, is required?",
        "options": [
            {"id": "A", "text": "-sS (TCP SYN scan)"},
            {"id": "B", "text": "-sT (TCP connect scan)"},
            {"id": "C", "text": "-sU (UDP scan)"},
            {"id": "D", "text": "-sn (host discovery)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "-sU scans UDP ports. Because UDP is connectionless, open ports often simply stay silent, so "
                       "the scan is slower and must infer state from ICMP unreachable messages.",
            "distractors": {
                "A": "-sS is a TCP half-open scan and does not test UDP services.",
                "B": "-sT completes a TCP handshake; it also does not scan UDP.",
                "D": "-sn only discovers live hosts and scans no ports at all.",
            },
            "exam_pattern": "Find open UDP services (SNMP/DNS/TFTP) = Nmap -sU (slow, no handshake).",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-r2-012", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 2, "type": "mcq",
        "stem": "To scan as slowly and quietly as possible and reduce the chance of tripping an IDS, which Nmap "
                "option family would a tester adjust (for example choosing -T0/-T1 over -T4)?",
        "options": [
            {"id": "A", "text": "The -O OS-detection option"},
            {"id": "B", "text": "The -T timing templates"},
            {"id": "C", "text": "The -p port-range option"},
            {"id": "D", "text": "The -sV version-detection option"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The -T0 through -T5 timing templates set scan speed/aggressiveness; lower values (paranoid/"
                       "sneaky) slow probes to evade rate-based IDS detection, higher values finish faster but noisier.",
            "distractors": {
                "A": "-O fingerprints the OS; it does not control scan timing.",
                "C": "-p selects which ports to scan, not how fast or stealthily.",
                "D": "-sV detects service versions; it is unrelated to timing/stealth tuning.",
            },
            "exam_pattern": "Tune scan speed/stealth = Nmap -T0..-T5 timing templates (-T0 slowest/quietest).",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-r2-013", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 3, "type": "mcq",
        "stem": "Which Nmap capability runs Lua scripts to extend scanning into advanced discovery, richer "
                "version detection, and even vulnerability checks (invoked with --script)?",
        "options": [
            {"id": "A", "text": "The Nmap Scripting Engine (NSE)"},
            {"id": "B", "text": "The -sn ping sweep"},
            {"id": "C", "text": "The -O OS-detection engine"},
            {"id": "D", "text": "The decoy option (-D)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Nmap Scripting Engine (NSE) runs Lua scripts (invoked with --script) for discovery, "
                       "version and vuln checks, brute forcing, and more, greatly extending Nmap.",
            "distractors": {
                "B": "-sn only performs host discovery and runs no scripts.",
                "C": "-O fingerprints the operating system; it is not the scripting engine.",
                "D": "-D adds decoy source addresses to obscure the scanner; it is not a scripting feature.",
            },
            "exam_pattern": "Lua scripts for advanced/vuln checks (--script) = Nmap Scripting Engine (NSE).",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-r2-014", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 3, "type": "mcq",
        "stem": "A tester wants to learn which ports a firewall filters versus lets through, rather than which "
                "are open. Which Nmap scan is designed to map firewall rules by marking ports filtered/unfiltered?",
        "options": [
            {"id": "A", "text": "-sV (version detection)"},
            {"id": "B", "text": "-O (OS detection)"},
            {"id": "C", "text": "-sA (TCP ACK scan)"},
            {"id": "D", "text": "-sn (host discovery)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The ACK scan (-sA) sends bare ACK packets; it cannot tell open from closed, but a RST reply "
                       "versus no reply reveals whether a firewall is filtering the port - so it maps rulesets.",
            "distractors": {
                "A": "-sV identifies service versions on open ports, not firewall filtering behavior.",
                "B": "-O fingerprints the OS; it does not classify ports as filtered/unfiltered.",
                "D": "-sn only finds live hosts and scans no ports.",
            },
            "exam_pattern": "Map firewall filtered/unfiltered (not open/closed) = Nmap -sA ACK scan.",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },
    {
        "id": "ceh-recon-r2-015", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_scanning", "difficulty": 3, "type": "mcq",
        "stem": "Which highly stealthy Nmap scan bounces probes off an idle third-party 'zombie' host and reads "
                "that host's predictable IP ID sequence, so the scan never originates from the attacker's real IP?",
        "options": [
            {"id": "A", "text": "TCP connect scan (-sT)"},
            {"id": "B", "text": "Idle (zombie) scan (-sI)"},
            {"id": "C", "text": "SYN scan (-sS)"},
            {"id": "D", "text": "Version scan (-sV)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The idle/zombie scan (-sI) infers the target's port state from changes in an idle host's "
                       "IP ID counter, so probes appear to come from the zombie, not the attacker - maximum stealth.",
            "distractors": {
                "A": "A connect scan comes straight from the attacker's IP and completes full handshakes.",
                "C": "A SYN scan is stealthier than connect but still originates from the attacker's address.",
                "D": "-sV actively probes services from the attacker's host to read versions.",
            },
            "exam_pattern": "Scan via an idle zombie's IP ID so it's not your IP = idle/zombie scan (-sI).",
        },
        "references": ["CEH v13 Module 03: Scanning Networks"],
    },

    # ----- ceh_enumeration (5) -----------------------------------------
    {
        "id": "ceh-recon-r2-016", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "mcq",
        "stem": "An attacker queries TCP port 389 to enumerate users, groups, and organizational units from an "
                "Active Directory server. Which protocol is being used for this directory enumeration?",
        "options": [
            {"id": "A", "text": "SMB"},
            {"id": "B", "text": "SNMP"},
            {"id": "C", "text": "LDAP"},
            {"id": "D", "text": "SMTP"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "LDAP (TCP 389, or 636 for LDAPS) serves directory data; if it allows anonymous or weak "
                       "binds, an attacker can enumerate users, groups, and OUs from the directory.",
            "distractors": {
                "A": "SMB (445) enumerates shares and sessions, not directory objects over 389.",
                "B": "SNMP (161/UDP) enumerates device MIB data via community strings, not directory objects.",
                "D": "SMTP (25) is for email; its VRFY/EXPN can enumerate mailboxes but it is not port 389.",
            },
            "exam_pattern": "Directory objects (users/groups/OUs) over port 389/636 = LDAP enumeration.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-r2-017", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "mcq",
        "stem": "Against an SMTP server, which pair of commands can an attacker abuse to confirm whether specific "
                "email accounts or mailing lists exist (user enumeration)?",
        "options": [
            {"id": "A", "text": "VRFY and EXPN"},
            {"id": "B", "text": "GET and POST"},
            {"id": "C", "text": "AXFR and IXFR"},
            {"id": "D", "text": "PUT and DELETE"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SMTP VRFY verifies a username and EXPN expands a mailing list, so if left enabled they let "
                       "an attacker enumerate valid accounts. Disabling or restricting them is the fix.",
            "distractors": {
                "B": "GET and POST are HTTP methods, not SMTP commands.",
                "C": "AXFR and IXFR are DNS zone-transfer requests, not SMTP commands.",
                "D": "PUT and DELETE are HTTP methods used against web servers.",
            },
            "exam_pattern": "Enumerate mailboxes over SMTP = VRFY / EXPN (disable them).",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-r2-018", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "mcq",
        "stem": "On a legacy Windows network an attacker uses a utility to read the NetBIOS name table and active "
                "sessions over ports 137-139. Which command-line tool fits this NetBIOS enumeration?",
        "options": [
            {"id": "A", "text": "showmount"},
            {"id": "B", "text": "nbtstat"},
            {"id": "C", "text": "dig"},
            {"id": "D", "text": "ldapsearch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "nbtstat queries NetBIOS over TCP/IP (ports 137-139), listing the remote name table and "
                       "sessions - classic NetBIOS enumeration on legacy Windows.",
            "distractors": {
                "A": "showmount lists NFS exports (port 2049), not NetBIOS data.",
                "C": "dig queries DNS records, not NetBIOS name tables.",
                "D": "ldapsearch queries LDAP directories on port 389/636.",
            },
            "exam_pattern": "NetBIOS name table/sessions over 137-139 = nbtstat.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-r2-019", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 3, "type": "mcq",
        "stem": "A tester runs 'showmount -e' against TCP port 2049 to list a server's exported file systems and "
                "who may mount them. Which service is being enumerated?",
        "options": [
            {"id": "A", "text": "SMB/CIFS"},
            {"id": "B", "text": "FTP"},
            {"id": "C", "text": "NFS (Network File System)"},
            {"id": "D", "text": "SNMP"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "NFS uses port 2049, and showmount -e lists its exports and allowed clients - revealing "
                       "shares that may be mountable, sometimes with weak host-based access control.",
            "distractors": {
                "A": "SMB/CIFS uses port 445 (and legacy 137-139); showmount does not target it.",
                "B": "FTP (21) transfers files but is not enumerated with showmount over 2049.",
                "D": "SNMP (161/UDP) exposes device MIBs via community strings, not NFS exports.",
            },
            "exam_pattern": "showmount -e on 2049 lists exports = NFS enumeration.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },
    {
        "id": "ceh-recon-r2-020", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_enumeration", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Unlike SNMP v1 and v2c, which send community strings in clear text, SNMP "
                "version ______ adds authentication and encryption and should be used to resist enumeration.",
        "correct": ["3", "v3", "snmpv3", "snmp v3"],
        "explanation": {
            "correct": "SNMPv3 introduces user-based authentication and privacy (encryption), closing the clear-text "
                       "community-string exposure of v1/v2c that makes SNMP easy to enumerate.",
            "distractors": {},
            "exam_pattern": "SNMP with auth + encryption (no clear-text community string) = SNMPv3.",
        },
        "references": ["CEH v13 Module 04: Enumeration"],
    },

    # ----- ceh_vuln_analysis (3) ---------------------------------------
    {
        "id": "ceh-recon-r2-021", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 2, "type": "mcq",
        "stem": "A team needs a free, open-source vulnerability scanner as an alternative to commercial Nessus. "
                "Which scanner (the engine behind the Greenbone/GVM framework) fits?",
        "options": [
            {"id": "A", "text": "OpenVAS"},
            {"id": "B", "text": "Metasploit"},
            {"id": "C", "text": "sqlmap"},
            {"id": "D", "text": "Aircrack-ng"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OpenVAS (the scanning engine within Greenbone Vulnerability Management/GVM) is a widely used "
                       "open-source vulnerability scanner comparable to Nessus.",
            "distractors": {
                "B": "Metasploit is an exploitation framework, not primarily a scan-and-report vulnerability scanner.",
                "C": "sqlmap automates SQL injection; it is not a general vulnerability scanner.",
                "D": "Aircrack-ng is a wireless key-cracking suite.",
            },
            "exam_pattern": "Free/open-source vuln scanner (Greenbone/GVM engine) = OpenVAS.",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },
    {
        "id": "ceh-recon-r2-022", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 3, "type": "mcq",
        "stem": "To get the most accurate results with the fewest false positives, a scanner is given valid login "
                "credentials so it can assess patch levels and settings from the inside. Which scan type is this?",
        "options": [
            {"id": "A", "text": "Unauthenticated (network) scan"},
            {"id": "B", "text": "Authenticated (credentialed) scan"},
            {"id": "C", "text": "Passive scan"},
            {"id": "D", "text": "External scan"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An authenticated/credentialed scan logs in to each host, so it reads actual installed "
                       "patches and configuration - more accurate and with fewer false positives than probing from outside.",
            "distractors": {
                "A": "An unauthenticated scan only probes from the network and infers state, producing more false positives.",
                "C": "A passive scan observes traffic without logging in, so it cannot read local patch state.",
                "D": "'External' describes the vantage point (outside the perimeter), not whether credentials are used.",
            },
            "exam_pattern": "Scanner logs in to read real patch/config state = authenticated (credentialed) scan.",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },
    {
        "id": "ceh-recon-r2-023", "exam": "ceh", "domain": "ceh_intro_recon",
        "subtopic": "ceh_vuln_analysis", "difficulty": 3, "type": "multi",
        "stem": "In CVSS v3.1, besides the mandatory Base metric group, which TWO optional metric groups let an "
                "organization refine a score for exploit maturity over time and for its own environment? (Choose two.)",
        "options": [
            {"id": "A", "text": "Temporal metrics"},
            {"id": "B", "text": "Environmental metrics"},
            {"id": "C", "text": "Base metrics"},
            {"id": "D", "text": "Kinetic metrics"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "CVSS v3.1 has three metric groups: Base (intrinsic, constant), Temporal (changes over time, "
                       "e.g., exploit code maturity and remediation level), and Environmental (tailored to one organization).",
            "distractors": {
                "C": "Base is the mandatory intrinsic group the question excludes, not an optional refinement.",
                "D": "'Kinetic' is not a CVSS metric group.",
            },
            "exam_pattern": "CVSS groups = Base (constant) + Temporal (over time) + Environmental (your context).",
        },
        "references": ["CEH v13 Module 05: Vulnerability Analysis"],
    },

    # ====================================================================
    # Domain 2.0 - System Hacking and Malware  (sys, 18)
    # ====================================================================

    # ----- ceh_system_hacking (9) --------------------------------------
    {
        "id": "ceh-sys-r2-001", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "Which post-exploitation tool is best known for extracting plaintext passwords, NTLM hashes, and "
                "Kerberos tickets from the memory of the Windows LSASS process?",
        "options": [
            {"id": "A", "text": "Nikto"},
            {"id": "B", "text": "Mimikatz"},
            {"id": "C", "text": "theHarvester"},
            {"id": "D", "text": "Wireshark"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Mimikatz reads credential material (plaintext, hashes, tickets) from LSASS memory, enabling "
                       "pass-the-hash and pass-the-ticket; protecting LSASS (Credential Guard) is the defense.",
            "distractors": {
                "A": "Nikto scans web servers for known issues; it does not touch LSASS memory.",
                "C": "theHarvester gathers public OSINT (emails, subdomains), not in-memory credentials.",
                "D": "Wireshark captures network packets; it does not extract credentials from process memory.",
            },
            "exam_pattern": "Dump passwords/hashes/tickets from LSASS memory = Mimikatz.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-002", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 3, "type": "mcq",
        "stem": "Any authenticated domain user requests Kerberos service tickets for accounts that have a service "
                "principal name (SPN), then cracks those tickets offline to recover service-account passwords. "
                "Which attack is this?",
        "options": [
            {"id": "A", "text": "Pass-the-hash"},
            {"id": "B", "text": "LLMNR poisoning"},
            {"id": "C", "text": "Kerberoasting"},
            {"id": "D", "text": "Credential stuffing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Kerberoasting requests TGS tickets for SPN-bound accounts; the tickets are encrypted with "
                       "the service account's password-derived key, so they can be brute-forced offline with no account lockout.",
            "distractors": {
                "A": "Pass-the-hash reuses a captured hash to authenticate; it does not request and crack TGS tickets.",
                "B": "LLMNR/NBT-NS poisoning captures hashes from broadcast name resolution, not Kerberos SPN tickets.",
                "D": "Credential stuffing replays leaked username/password pairs against logins.",
            },
            "exam_pattern": "Request SPN service tickets, crack offline for the service password = Kerberoasting.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-003", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "To avoid triggering account lockouts, an attacker tries just one or two very common passwords "
                "against many different user accounts. Which password attack is this?",
        "options": [
            {"id": "A", "text": "Password spraying"},
            {"id": "B", "text": "Brute-force attack"},
            {"id": "C", "text": "Dictionary attack"},
            {"id": "D", "text": "Rainbow table attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Password spraying tries a few common passwords across many accounts, staying under lockout "
                       "thresholds that would trip if one account were hammered repeatedly.",
            "distractors": {
                "B": "Brute force tries many passwords against one account and tends to trigger lockout.",
                "C": "A dictionary attack runs a whole wordlist against an account, not one password across many.",
                "D": "A rainbow table reverses captured hashes offline; it is not live guessing across accounts.",
            },
            "exam_pattern": "One/two common passwords across MANY accounts to dodge lockout = password spraying.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-004", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "An attacker takes username/password pairs leaked from one website's breach and replays them "
                "against a different site, relying on users reusing the same password. Which attack is this?",
        "options": [
            {"id": "A", "text": "Password spraying"},
            {"id": "B", "text": "Credential stuffing"},
            {"id": "C", "text": "Pass-the-hash"},
            {"id": "D", "text": "Rainbow table attack"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Credential stuffing replays known-valid credential pairs from prior breaches against other "
                       "services, exploiting password reuse; MFA and breached-password checks are key defenses.",
            "distractors": {
                "A": "Password spraying guesses a few common passwords; it does not replay specific leaked pairs.",
                "C": "Pass-the-hash reuses a hash, not a leaked plaintext username/password pair.",
                "D": "A rainbow table cracks hashes offline; it is not credential replay across sites.",
            },
            "exam_pattern": "Replay leaked username/password pairs on other sites = credential stuffing (MFA defends).",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-005", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 3, "type": "mcq",
        "stem": "On a Windows LAN, which tool answers LLMNR and NBT-NS name-resolution broadcasts with spoofed "
                "replies to capture authentication hashes from clients looking for a mistyped or missing host?",
        "options": [
            {"id": "A", "text": "Responder"},
            {"id": "B", "text": "Mimikatz"},
            {"id": "C", "text": "Maltego"},
            {"id": "D", "text": "Hydra"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Responder poisons LLMNR/NBT-NS (and mDNS) broadcasts, tricking clients into authenticating "
                       "to the attacker and leaking NetNTLM hashes; disabling LLMNR/NBT-NS is the defense.",
            "distractors": {
                "B": "Mimikatz extracts credentials from local memory; it does not poison name-resolution broadcasts.",
                "C": "Maltego is an OSINT link-analysis tool, not a LAN poisoning utility.",
                "D": "Hydra performs online password guessing against services, not LLMNR poisoning.",
            },
            "exam_pattern": "Poison LLMNR/NBT-NS to capture hashes = Responder (disable LLMNR/NBT-NS).",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-006", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 3, "type": "mcq",
        "stem": "On an NTFS volume, which feature lets an attacker hide the contents of a malicious file behind a "
                "legitimate-looking file so the hidden data does not appear in a normal directory listing?",
        "options": [
            {"id": "A", "text": "Steganography"},
            {"id": "B", "text": "NTFS Alternate Data Streams (ADS)"},
            {"id": "C", "text": "Symbolic links"},
            {"id": "D", "text": "File compression"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "NTFS Alternate Data Streams let data be attached to a file in a secondary stream that a "
                       "standard directory listing does not show, a classic data-hiding technique on Windows.",
            "distractors": {
                "A": "Steganography hides data inside a carrier such as an image; it is not an NTFS filesystem feature.",
                "C": "Symbolic links point to another path; they do not hide a file's contents in a secondary stream.",
                "D": "Compression shrinks file size; it does not conceal a file behind another in a hidden stream.",
            },
            "exam_pattern": "Hide data in a hidden NTFS stream behind a normal file = Alternate Data Streams (ADS).",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-007", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Gaining the access rights of another user at the SAME privilege level - for "
                "example, one standard user reaching another standard user's data - is called ______ privilege escalation.",
        "correct": ["horizontal", "lateral"],
        "explanation": {
            "correct": "Horizontal (lateral) privilege escalation moves sideways to a peer account's access at the "
                       "same level, versus vertical escalation which rises to administrator/root.",
            "distractors": {},
            "exam_pattern": "Same-level access to a peer account = horizontal; rise to admin/root = vertical.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-008", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "Which type of keylogger is a physical device plugged in between the keyboard and the computer, "
                "so OS-based anti-malware scanning the file system cannot detect it?",
        "options": [
            {"id": "A", "text": "Hardware keylogger"},
            {"id": "B", "text": "Kernel (software) keylogger"},
            {"id": "C", "text": "API-hooking keylogger"},
            {"id": "D", "text": "Form-grabbing keylogger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hardware keylogger is a physical inline device (or built into the keyboard); because it "
                       "is not software on the OS, host anti-malware cannot see it - physical inspection catches it.",
            "distractors": {
                "B": "A kernel keylogger is software running in the OS and is at least potentially detectable by host tools.",
                "C": "An API-hooking keylogger is software intercepting input APIs within the OS.",
                "D": "A form-grabbing keylogger is software that captures browser form data, not a physical device.",
            },
            "exam_pattern": "Physical inline device, invisible to OS anti-malware = hardware keylogger.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-r2-009", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 3, "type": "multi",
        "stem": "Which TWO measures best protect stored password hashes against offline cracking if the hash "
                "database is stolen? (Choose two.)",
        "options": [
            {"id": "A", "text": "Hash with a slow, salted key-derivation function such as bcrypt, scrypt, or PBKDF2"},
            {"id": "B", "text": "Require long, high-entropy passphrases"},
            {"id": "C", "text": "Store passwords as fast, unsalted MD5 digests"},
            {"id": "D", "text": "Reuse one global salt value for every account"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A slow, salted KDF (bcrypt/scrypt/PBKDF2) makes each guess expensive and defeats precomputed "
                       "tables, and long high-entropy passphrases enlarge the search space - together they blunt offline cracking.",
            "distractors": {
                "C": "Fast, unsalted MD5 is trivially cracked and vulnerable to rainbow tables - the opposite of a defense.",
                "D": "A single global salt lets one precomputed table attack all accounts; salts must be unique per password.",
            },
            "exam_pattern": "Slow salted KDF + long passphrases defend hashes; fast/unsalted/shared-salt do not.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },

    # ----- ceh_malware_threats (9) -------------------------------------
    {
        "id": "ceh-sys-r2-010", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 3, "type": "mcq",
        "stem": "Which malware runs almost entirely in memory and abuses built-in tools like PowerShell and WMI, "
                "writing little or nothing to disk so signature-based antivirus has no file to scan?",
        "options": [
            {"id": "A", "text": "Boot-sector virus"},
            {"id": "B", "text": "Fileless malware"},
            {"id": "C", "text": "Macro virus"},
            {"id": "D", "text": "Ransomware"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Fileless malware lives in memory and leverages legitimate interpreters (PowerShell, WMI), "
                       "leaving minimal on-disk artifacts; behavior-based EDR, not file signatures, is needed to catch it.",
            "distractors": {
                "A": "A boot-sector virus writes itself to the disk's boot area - very much on disk.",
                "C": "A macro virus lives in document macros stored in files on disk.",
                "D": "Ransomware writes encrypted files to disk and announces itself; it is not defined by being fileless.",
            },
            "exam_pattern": "In-memory, abuses PowerShell/WMI, little on disk = fileless malware (needs behavior-based detection).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-011", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 3, "type": "mcq",
        "stem": "An attacker carries out malicious actions using signed, built-in operating-system binaries (such "
                "as certutil, mshta, or regsvr32) so the activity blends in with normal administration. This is called?",
        "options": [
            {"id": "A", "text": "Living off the land (using LOLBins)"},
            {"id": "B", "text": "Packing"},
            {"id": "C", "text": "Sideloading"},
            {"id": "D", "text": "Steganography"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Living off the land abuses legitimate, signed OS binaries (LOLBins) to evade allow-lists and "
                       "blend with normal activity, reducing the attacker's own tooling footprint.",
            "distractors": {
                "B": "Packing compresses/obfuscates a malicious executable; it does not mean abusing built-in binaries.",
                "C": "Sideloading installs apps from outside an official store - a different concept.",
                "D": "Steganography hides data in a carrier file; it is not about using built-in system tools.",
            },
            "exam_pattern": "Abuse built-in signed binaries to blend in = living off the land (LOLBins).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-012", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 3, "type": "mcq",
        "stem": "Which virus completely rewrites its own code on each propagation - without using encryption - so "
                "that no two copies share the same byte pattern, defeating simple signature detection?",
        "options": [
            {"id": "A", "text": "Polymorphic virus"},
            {"id": "B", "text": "Metamorphic virus"},
            {"id": "C", "text": "Boot-sector virus"},
            {"id": "D", "text": "Stealth virus"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A metamorphic virus rewrites its entire code body each time (re-ordering and substituting "
                       "instructions) with no encryption, so copies differ structurally and signatures fail.",
            "distractors": {
                "A": "A polymorphic virus keeps the same body but encrypts it under a changing key with a mutating decryptor.",
                "C": "A boot-sector virus infects the boot area; that does not describe self-rewriting code.",
                "D": "A stealth virus hides its changes from inspection tools; it does not rewrite its own code each time.",
            },
            "exam_pattern": "Rewrites its whole code, no encryption = metamorphic; encrypts body with mutating decryptor = polymorphic.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-013", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Malware authors compress and obfuscate an executable with a tool that restores the original code "
                "in memory at runtime, so static signatures see only the wrapper. What is this tool called?",
        "options": [
            {"id": "A", "text": "A debugger"},
            {"id": "B", "text": "A packer (or crypter)"},
            {"id": "C", "text": "A disassembler"},
            {"id": "D", "text": "A sandbox"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A packer/crypter compresses or encrypts the payload and unpacks it in memory at runtime, so "
                       "on-disk static analysis sees only the stub - analysts must unpack it or observe it dynamically.",
            "distractors": {
                "A": "A debugger steps through code during analysis; it does not obfuscate the executable.",
                "C": "A disassembler translates machine code to assembly for analysis; it is a defender's tool.",
                "D": "A sandbox is an isolated environment for dynamic analysis, not an obfuscation wrapper.",
            },
            "exam_pattern": "Compress/obfuscate an EXE, unpack in memory = packer/crypter (defeats static signatures).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-014", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Malicious code lies dormant until a specific condition is met - a particular date, or an "
                "employee's account being disabled - and only then executes its payload. Which malware is this?",
        "options": [
            {"id": "A", "text": "Worm"},
            {"id": "B", "text": "Logic bomb"},
            {"id": "C", "text": "Rootkit"},
            {"id": "D", "text": "Trojan"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A logic bomb stays inert until its trigger condition (a date, event, or state) is satisfied, "
                       "then detonates - often planted by a disgruntled insider.",
            "distractors": {
                "A": "A worm self-propagates immediately; it does not wait for a trigger condition.",
                "C": "A rootkit hides presence to maintain access; concealment, not conditional triggering, defines it.",
                "D": "A Trojan is disguised malicious software; being disguised is its trait, not condition-based triggering.",
            },
            "exam_pattern": "Dormant until a trigger condition, then fires = logic bomb.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-015", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Malware silently uses a victim's CPU/GPU to mine cryptocurrency for the attacker; the main "
                "symptoms are sluggish performance, high resource use, and overheating. Which threat is this?",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Cryptojacking (cryptomining malware)"},
            {"id": "C", "text": "Keylogger"},
            {"id": "D", "text": "Adware"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cryptojacking hijacks a victim's compute resources to mine cryptocurrency; it seeks to stay "
                       "hidden and persistent, so degraded performance is the main sign.",
            "distractors": {
                "A": "Ransomware encrypts files and demands payment; it does not quietly mine coins.",
                "C": "A keylogger records keystrokes; it does not consume compute to mine currency.",
                "D": "Adware displays unwanted ads; its goal is ad revenue, not mining.",
            },
            "exam_pattern": "Secretly mine cryptocurrency on the victim's hardware = cryptojacking.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-016", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Which malware is designed to irreversibly destroy or corrupt data and systems, with no intent of "
                "ransom or recovery - typically deployed for sabotage?",
        "options": [
            {"id": "A", "text": "Wiper"},
            {"id": "B", "text": "Ransomware"},
            {"id": "C", "text": "Spyware"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A wiper destroys data permanently; unlike ransomware, there is no key or recovery path, so "
                       "its purpose is disruption and sabotage.",
            "distractors": {
                "B": "Ransomware encrypts data for extortion and can (in principle) be reversed with the key.",
                "C": "Spyware covertly collects information rather than destroying it.",
                "D": "A rootkit hides to maintain access; destruction is not its defining purpose.",
            },
            "exam_pattern": "Permanent data destruction, no ransom/recovery = wiper (sabotage).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-017", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Forensic artifacts such as malicious file hashes, attacker IP addresses, and "
                "command-and-control domains that signal a system may be compromised are collectively called "
                "indicators of ______.",
        "correct": ["compromise", "compromise (ioc)", "ioc"],
        "explanation": {
            "correct": "Indicators of compromise (IOCs) are observable artifacts (hashes, IPs, domains, registry "
                       "keys) that malware analysis and threat hunting use to detect intrusions and scope incidents.",
            "distractors": {},
            "exam_pattern": "Hashes/IPs/domains that reveal an intrusion = indicators of compromise (IOCs).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-r2-018", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 3, "type": "mcq",
        "stem": "Some malware checks for signs that it is running inside an analysis environment (very few CPU "
                "cores, no mouse movement, known VM artifacts) and stays dormant when it detects them. This behavior is?",
        "options": [
            {"id": "A", "text": "Privilege escalation"},
            {"id": "B", "text": "Sandbox (VM) evasion"},
            {"id": "C", "text": "Polymorphism"},
            {"id": "D", "text": "Packing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Sandbox/VM evasion makes malware detect analysis environments and withhold its payload, "
                       "defeating automated dynamic analysis; analysts counter it by hardening the sandbox to look real.",
            "distractors": {
                "A": "Privilege escalation raises access rights; it is not about detecting an analysis environment.",
                "C": "Polymorphism changes the malware's appearance to evade signatures, not to detect a sandbox.",
                "D": "Packing obfuscates the executable; it does not sense whether it runs in a VM.",
            },
            "exam_pattern": "Detect the analysis VM and stay dormant = sandbox/VM evasion (counters dynamic analysis).",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },

    # ====================================================================
    # Domain 3.0 - Network and Perimeter Hacking  (net, 25)
    # ====================================================================

    # ----- ceh_sniffing (6) --------------------------------------------
    {
        "id": "ceh-net-r2-001", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "mcq",
        "stem": "An attacker floods a DHCP server with lease requests using many spoofed MAC addresses until the "
                "server's address pool is exhausted and legitimate clients can no longer get an IP. Which attack?",
        "options": [
            {"id": "A", "text": "DHCP starvation"},
            {"id": "B", "text": "MAC flooding"},
            {"id": "C", "text": "ARP poisoning"},
            {"id": "D", "text": "SYN flood"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DHCP starvation exhausts the DHCP scope with spoofed requests, denying leases; it often "
                       "precedes standing up a rogue DHCP server. DHCP snooping with rate limits is the defense.",
            "distractors": {
                "B": "MAC flooding overflows a switch's CAM table to force flooding, not the DHCP pool.",
                "C": "ARP poisoning redirects LAN traffic by forging ARP replies, not by exhausting DHCP leases.",
                "D": "A SYN flood exhausts a server's TCP connection table, unrelated to DHCP leases.",
            },
            "exam_pattern": "Exhaust the DHCP pool with spoofed MAC requests = DHCP starvation.",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-r2-002", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "mcq",
        "stem": "An attacker places a rogue DHCP server on the LAN to hand clients a malicious default gateway "
                "and DNS. Which switch security feature blocks DHCP offers from untrusted ports?",
        "options": [
            {"id": "A", "text": "DHCP snooping"},
            {"id": "B", "text": "Port mirroring (SPAN)"},
            {"id": "C", "text": "Spanning Tree Protocol"},
            {"id": "D", "text": "Quality of Service (QoS)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DHCP snooping classifies switch ports as trusted/untrusted and drops DHCP server messages "
                       "from untrusted ports, defeating rogue DHCP servers (and building the binding table DAI uses).",
            "distractors": {
                "B": "SPAN copies traffic to a monitor port; it does not filter rogue DHCP offers.",
                "C": "STP prevents Layer 2 loops; it has no role in validating DHCP messages.",
                "D": "QoS prioritizes traffic; it does not block rogue DHCP servers.",
            },
            "exam_pattern": "Block rogue DHCP offers on untrusted ports = DHCP snooping.",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-r2-003", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 3, "type": "mcq",
        "stem": "Which switch feature inspects ARP packets against the DHCP snooping binding table and drops "
                "those with a forged IP-to-MAC mapping, directly stopping ARP poisoning?",
        "options": [
            {"id": "A", "text": "Dynamic ARP Inspection (DAI)"},
            {"id": "B", "text": "BPDU Guard"},
            {"id": "C", "text": "Storm control"},
            {"id": "D", "text": "Port mirroring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dynamic ARP Inspection validates each ARP packet against the trusted IP-MAC bindings (from "
                       "DHCP snooping) and discards spoofed ones, blocking ARP-poisoning man-in-the-middle attacks.",
            "distractors": {
                "B": "BPDU Guard protects the spanning-tree topology from rogue BPDUs, not ARP spoofing.",
                "C": "Storm control rate-limits broadcast/multicast floods; it does not validate ARP bindings.",
                "D": "Port mirroring copies traffic for analysis; it does not inspect or drop forged ARP packets.",
            },
            "exam_pattern": "Validate ARP vs DHCP-snooping bindings to stop ARP poisoning = Dynamic ARP Inspection (DAI).",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-r2-004", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 3, "type": "mcq",
        "stem": "From a man-in-the-middle position, which technique downgrades a victim's HTTPS connections to "
                "plaintext HTTP so credentials and cookies can be read in the clear?",
        "options": [
            {"id": "A", "text": "ARP poisoning"},
            {"id": "B", "text": "SSLstrip"},
            {"id": "C", "text": "DNS amplification"},
            {"id": "D", "text": "Session fixation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "SSLstrip sits in the middle and rewrites HTTPS links to HTTP, stripping TLS so traffic is "
                       "readable; HSTS (which forces HTTPS) is the primary defense.",
            "distractors": {
                "A": "ARP poisoning establishes the MITM position but does not itself downgrade HTTPS to HTTP.",
                "C": "DNS amplification is a DDoS reflection method, not a TLS-downgrade technique.",
                "D": "Session fixation forces a known session ID; it does not strip TLS.",
            },
            "exam_pattern": "Downgrade HTTPS to HTTP in a MITM to read traffic = SSLstrip (HSTS defends).",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-r2-005", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 3, "type": "mcq",
        "stem": "An attacker injects a forged record into a DNS resolver's cache so that everyone using that "
                "resolver is sent to a malicious IP when they request a legitimate domain. Which attack is this?",
        "options": [
            {"id": "A", "text": "ARP poisoning"},
            {"id": "B", "text": "DNS cache poisoning (DNS spoofing)"},
            {"id": "C", "text": "MAC flooding"},
            {"id": "D", "text": "SYN flood"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DNS cache poisoning plants a bogus record in a resolver's cache, redirecting many users to "
                       "an attacker-controlled IP; DNSSEC, which signs records, is a key defense.",
            "distractors": {
                "A": "ARP poisoning operates at Layer 2 on the local segment, not on DNS resolver caches.",
                "C": "MAC flooding targets a switch's CAM table, not DNS caches.",
                "D": "A SYN flood is a denial-of-service technique, not DNS record manipulation.",
            },
            "exam_pattern": "Forged record in a resolver cache redirecting users = DNS cache poisoning (DNSSEC defends).",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },
    {
        "id": "ceh-net-r2-006", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_sniffing", "difficulty": 2, "type": "multi",
        "stem": "Which TWO protocols transmit credentials in clear text, making them prime targets for a sniffer "
                "on the path? (Choose two.)",
        "options": [
            {"id": "A", "text": "Telnet"},
            {"id": "B", "text": "FTP"},
            {"id": "C", "text": "SSH"},
            {"id": "D", "text": "HTTPS"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Telnet and FTP send usernames and passwords in clear text, so a sniffer can read them; "
                       "replace them with encrypted equivalents (SSH and SFTP/FTPS).",
            "distractors": {
                "C": "SSH encrypts the session, so credentials are not exposed to a passive sniffer.",
                "D": "HTTPS encrypts web traffic with TLS, protecting credentials in transit.",
            },
            "exam_pattern": "Clear-text credentials = Telnet/FTP/HTTP; encrypted = SSH/SFTP/HTTPS.",
        },
        "references": ["CEH v13 Module 08: Sniffing"],
    },

    # ----- ceh_social_engineering (5) ----------------------------------
    {
        "id": "ceh-net-r2-007", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "A crafted email addresses a company's CFO by name, references a real pending acquisition, and "
                "pressures them to approve a wire transfer. Which term most precisely describes this targeting?",
        "options": [
            {"id": "A", "text": "Whaling"},
            {"id": "B", "text": "Generic (bulk) phishing"},
            {"id": "C", "text": "Smishing"},
            {"id": "D", "text": "Vishing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Whaling is spear phishing aimed at a senior, high-value executive (a 'big fish') with highly "
                       "tailored content - exactly the CFO-targeted lure described.",
            "distractors": {
                "B": "Generic phishing is untargeted bulk email, not a tailored lure for one executive.",
                "C": "Smishing delivers the lure by SMS text, not a tailored executive email.",
                "D": "Vishing is voice/phone-based social engineering, not an email to an executive.",
            },
            "exam_pattern": "Spear phishing aimed at a senior executive = whaling.",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-r2-008", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker spoofs or compromises an executive's email account and instructs the finance team "
                "to pay a fraudulent invoice to a new bank account. Which fraud scheme is this?",
        "options": [
            {"id": "A", "text": "Business email compromise (BEC)"},
            {"id": "B", "text": "Watering hole attack"},
            {"id": "C", "text": "Pharming"},
            {"id": "D", "text": "Tailgating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Business email compromise impersonates a trusted executive or vendor by email to trick "
                       "finance staff into wiring money or paying fake invoices; out-of-band verification is the defense.",
            "distractors": {
                "B": "A watering hole compromises a site the target frequents; it is not invoice fraud via email.",
                "C": "Pharming redirects users to fake sites via DNS/hosts tampering, not invoice fraud.",
                "D": "Tailgating is physical entry behind an authorized person, not email fraud.",
            },
            "exam_pattern": "Spoof/compromise an exec's email to redirect payments = BEC (verify out-of-band).",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-r2-009", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker scatters malware-laden USB drives labeled 'Executive Salaries' in a company parking "
                "lot, counting on an employee's curiosity to plug one in. Which social-engineering technique is this?",
        "options": [
            {"id": "A", "text": "Baiting"},
            {"id": "B", "text": "Quid pro quo"},
            {"id": "C", "text": "Pretexting"},
            {"id": "D", "text": "Tailgating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Baiting dangles an enticing object (a labeled USB drive) that delivers malware when the "
                       "curious victim uses it, exploiting curiosity and greed.",
            "distractors": {
                "B": "Quid pro quo offers a service or benefit in exchange for information or access.",
                "C": "Pretexting invents a believable backstory to justify a request, not a dropped physical lure.",
                "D": "Tailgating is following someone through a secure door, not leaving bait.",
            },
            "exam_pattern": "Leave tempting malware-laden media for a victim to use = baiting.",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-r2-010", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker phones staff posing as support and offers 'free help fixing a slow computer' in "
                "return for the user's login details. Which social-engineering technique relies on offering a service?",
        "options": [
            {"id": "A", "text": "Baiting"},
            {"id": "B", "text": "Quid pro quo"},
            {"id": "C", "text": "Shoulder surfing"},
            {"id": "D", "text": "Phishing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Quid pro quo ('something for something') trades a supposed benefit or service for credentials "
                       "or access - here, bogus tech support in exchange for the login.",
            "distractors": {
                "A": "Baiting leaves a tempting item (e.g., a USB drive); it does not offer a service in a call.",
                "C": "Shoulder surfing is watching a victim enter data; no service is offered.",
                "D": "Phishing is a deceptive message/link; this scenario centers on a service-for-credentials trade.",
            },
            "exam_pattern": "Offer a service/benefit in exchange for access = quid pro quo.",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },
    {
        "id": "ceh-net-r2-011", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_social_engineering", "difficulty": 3, "type": "mcq",
        "stem": "Even though a user types their bank's correct address, a poisoned hosts file or DNS record "
                "silently sends them to a fraudulent lookalike site. Which attack is this?",
        "options": [
            {"id": "A", "text": "Pharming"},
            {"id": "B", "text": "Phishing"},
            {"id": "C", "text": "Vishing"},
            {"id": "D", "text": "Whaling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Pharming redirects a correctly typed address to a malicious site by tampering with name "
                       "resolution (hosts file or DNS), so the victim never clicks a bad link.",
            "distractors": {
                "B": "Phishing depends on luring the victim to click a malicious link or attachment.",
                "C": "Vishing is voice/phone-based deception, not DNS/hosts redirection.",
                "D": "Whaling is spear phishing aimed at an executive, still lure-based rather than redirection.",
            },
            "exam_pattern": "Correct URL but redirected via DNS/hosts tampering = pharming (vs link-based phishing).",
        },
        "references": ["CEH v13 Module 09: Social Engineering"],
    },

    # ----- ceh_dos_ddos (5) --------------------------------------------
    {
        "id": "ceh-net-r2-012", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 3, "type": "mcq",
        "stem": "Which low-bandwidth, application-layer DoS opens many connections to a web server and holds them "
                "open by trickling partial HTTP headers, exhausting its connection pool?",
        "options": [
            {"id": "A", "text": "Slowloris"},
            {"id": "B", "text": "SYN flood"},
            {"id": "C", "text": "Smurf attack"},
            {"id": "D", "text": "UDP flood"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Slowloris is an application-layer attack that ties up a server's worker/connection slots with "
                       "many slow, never-finished HTTP requests, needing very little bandwidth.",
            "distractors": {
                "B": "A SYN flood exhausts the TCP half-open table at the transport layer, not HTTP connection slots via slow headers.",
                "C": "A Smurf attack is an ICMP amplification flood, high-volume rather than slow and low-bandwidth.",
                "D": "A UDP flood sends high-volume UDP packets; it is not the slow partial-request technique.",
            },
            "exam_pattern": "Slow partial HTTP requests exhausting connection slots = Slowloris (app-layer, low bandwidth).",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-r2-013", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 2, "type": "mcq",
        "stem": "Which classic denial-of-service attack sends a malformed or oversized ICMP packet to crash a "
                "vulnerable host's packet-reassembly code?",
        "options": [
            {"id": "A", "text": "Ping of Death"},
            {"id": "B", "text": "Smurf attack"},
            {"id": "C", "text": "Slowloris"},
            {"id": "D", "text": "LAND attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Ping of Death sends an oversized/malformed ICMP packet that overflows reassembly buffers "
                       "on unpatched stacks, crashing the target; it is largely historical now.",
            "distractors": {
                "B": "A Smurf attack is ICMP amplification via a broadcast address, not a single malformed oversized ping.",
                "C": "Slowloris is a slow HTTP attack, not an ICMP malformed-packet crash.",
                "D": "A LAND attack uses a spoofed packet whose source equals the destination, a different mechanism.",
            },
            "exam_pattern": "Oversized/malformed ICMP crashing reassembly = Ping of Death.",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-r2-014", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 3, "type": "mcq",
        "stem": "Which amplification attack sends ICMP echo requests to a network's broadcast address with the "
                "victim's spoofed source IP, so every host on that network replies to the victim at once?",
        "options": [
            {"id": "A", "text": "Smurf attack"},
            {"id": "B", "text": "Teardrop attack"},
            {"id": "C", "text": "SYN flood"},
            {"id": "D", "text": "Slowloris"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Smurf attack abuses directed broadcast with ICMP echo and a spoofed victim source, so many "
                       "hosts flood the victim; Fraggle is the UDP echo/chargen variant. Disable directed broadcasts to defend.",
            "distractors": {
                "B": "A Teardrop attack sends overlapping IP fragments to crash reassembly; it is not broadcast amplification.",
                "C": "A SYN flood exhausts the connection table; it does not use ICMP broadcast reflection.",
                "D": "Slowloris is a slow HTTP attack, not ICMP amplification.",
            },
            "exam_pattern": "ICMP to broadcast with spoofed victim source = Smurf; UDP echo variant = Fraggle.",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-r2-015", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 3, "type": "mcq",
        "stem": "Which attack sends a crafted packet whose source IP and port are set equal to the destination IP "
                "and port of the target, causing the machine to reply to itself and lock up?",
        "options": [
            {"id": "A", "text": "Teardrop attack"},
            {"id": "B", "text": "LAND attack"},
            {"id": "C", "text": "Smurf attack"},
            {"id": "D", "text": "Ping of Death"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A LAND attack spoofs the packet so source = destination (same IP/port) on the victim, making "
                       "it respond to itself and consume resources - a malformed-packet attack against buggy stacks.",
            "distractors": {
                "A": "A Teardrop attack uses overlapping fragment offsets to crash reassembly, not identical src/dst.",
                "C": "A Smurf attack is ICMP broadcast amplification, not a self-referential packet.",
                "D": "A Ping of Death uses an oversized ICMP packet, not matching source and destination addresses.",
            },
            "exam_pattern": "Spoofed packet with source = destination = LAND attack.",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },
    {
        "id": "ceh-net-r2-016", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_dos_ddos", "difficulty": 2, "type": "mcq",
        "stem": "To absorb a large volumetric DDoS, an organization routes inbound traffic through a high-capacity "
                "service that filters out malicious packets and forwards only clean traffic. What is this service called?",
        "options": [
            {"id": "A", "text": "A DDoS scrubbing (mitigation) service"},
            {"id": "B", "text": "A honeypot"},
            {"id": "C", "text": "A rainbow table"},
            {"id": "D", "text": "A jump box"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DDoS scrubbing centers absorb and clean attack traffic at scale, passing only legitimate "
                       "requests to the origin; this is a core volumetric-DDoS defense.",
            "distractors": {
                "B": "A honeypot is a decoy to lure attackers, not a high-capacity traffic filter.",
                "C": "A rainbow table is a password-cracking structure, unrelated to DDoS mitigation.",
                "D": "A jump box is a hardened pivot host for administration, not DDoS filtering.",
            },
            "exam_pattern": "Route traffic through high-capacity filtering to absorb a flood = DDoS scrubbing service.",
        },
        "references": ["CEH v13 Module 10: Denial-of-Service"],
    },

    # ----- ceh_session_hijacking (4) -----------------------------------
    {
        "id": "ceh-net-r2-017", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: In a blind TCP session hijack, where the attacker cannot see the traffic, "
                "they must correctly predict the next TCP ______ number so the server will accept their injected packets.",
        "correct": ["sequence", "sequence number", "seq"],
        "explanation": {
            "correct": "TCP uses sequence numbers to order bytes; to inject accepted data into a session they cannot "
                       "observe, the attacker must guess the next valid sequence number (TCP sequence prediction).",
            "distractors": {},
            "exam_pattern": "Blind TCP hijack requires predicting the next = sequence number.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },
    {
        "id": "ceh-net-r2-018", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 3, "type": "mcq",
        "stem": "Malware infects a victim's browser and silently alters transactions or injects extra form "
                "fields as the user banks online - operating after TLS has already decrypted the page. Which attack?",
        "options": [
            {"id": "A", "text": "Man-in-the-browser"},
            {"id": "B", "text": "Network man-in-the-middle"},
            {"id": "C", "text": "Session fixation"},
            {"id": "D", "text": "Cross-site request forgery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A man-in-the-browser attack uses a browser-resident Trojan to modify requests/responses "
                       "inside the browser, so TLS does not help because tampering occurs after decryption.",
            "distractors": {
                "B": "A network MITM intercepts traffic on the wire, where TLS does protect the data in transit.",
                "C": "Session fixation forces a known session ID before login; it does not modify transactions in the browser.",
                "D": "CSRF tricks the browser into sending a forged request; it does not sit inside the browser altering pages.",
            },
            "exam_pattern": "Browser-resident Trojan altering transactions after TLS decrypts = man-in-the-browser.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },
    {
        "id": "ceh-net-r2-019", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 3, "type": "mcq",
        "stem": "An attacker sets a known session ID in a victim's browser before the victim logs in, then reuses "
                "that same ID once the victim has authenticated. Which attack is this, and what defeats it?",
        "options": [
            {"id": "A", "text": "Session fixation; regenerate the session ID at login"},
            {"id": "B", "text": "Session sniffing; disable ICMP"},
            {"id": "C", "text": "Cross-site scripting; add more RAM"},
            {"id": "D", "text": "Brute force; shorten the session timeout only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session fixation plants a known session identifier so it is already valid after the victim "
                       "logs in; issuing a fresh session ID upon authentication defeats it.",
            "distractors": {
                "B": "This is fixation, not sniffing, and disabling ICMP does nothing to protect session IDs.",
                "C": "XSS can steal tokens but is a different attack; adding RAM is irrelevant to it.",
                "D": "The victim already authenticates legitimately, so this is not brute force of a password.",
            },
            "exam_pattern": "Pre-set a session ID reused after login = session fixation (regenerate ID at login).",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },
    {
        "id": "ceh-net-r2-020", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_session_hijacking", "difficulty": 3, "type": "multi",
        "stem": "Which TWO cookie attributes most directly protect a session cookie from being stolen by "
                "client-side script and from being sent over an unencrypted HTTP connection? (Choose two.)",
        "options": [
            {"id": "A", "text": "HttpOnly"},
            {"id": "B", "text": "Secure"},
            {"id": "C", "text": "Domain"},
            {"id": "D", "text": "Max-Age"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "HttpOnly blocks JavaScript from reading the cookie (mitigating XSS theft), and Secure ensures "
                       "the cookie is only sent over HTTPS, so it is not exposed on plaintext HTTP.",
            "distractors": {
                "C": "Domain scopes which hosts receive the cookie; it does not stop script access or plaintext exposure.",
                "D": "Max-Age sets the cookie's lifetime; it does not protect it from script theft or HTTP transmission.",
            },
            "exam_pattern": "Protect a session cookie = HttpOnly (no script) + Secure (HTTPS only); SameSite adds CSRF defense.",
        },
        "references": ["CEH v13 Module 11: Session Hijacking"],
    },

    # ----- ceh_evading_ids_fw (5) --------------------------------------
    {
        "id": "ceh-net-r2-021", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 3, "type": "mcq",
        "stem": "An IDS that learns a baseline of normal behavior and flags deviations from it can catch "
                "previously unknown attacks, at the cost of more false positives. Which detection method is this?",
        "options": [
            {"id": "A", "text": "Signature-based detection"},
            {"id": "B", "text": "Anomaly-based detection"},
            {"id": "C", "text": "Honeypot deployment"},
            {"id": "D", "text": "Stateful packet inspection"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Anomaly (behavior) based detection compares activity to a learned baseline, so it can detect "
                       "novel/zero-day attacks but produces more false positives than signature matching.",
            "distractors": {
                "A": "Signature-based detection matches known patterns and misses novel attacks it has no signature for.",
                "C": "A honeypot is a decoy host, not an IDS detection method.",
                "D": "Stateful inspection tracks connection state in a firewall; it is not baseline-deviation detection.",
            },
            "exam_pattern": "Baseline deviation, catches unknown attacks, more false positives = anomaly-based detection.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-r2-022", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 2, "type": "mcq",
        "stem": "Which intrusion-detection sensor is installed on an individual endpoint and watches that host's "
                "own logs, file integrity, and processes rather than network traffic?",
        "options": [
            {"id": "A", "text": "Network IDS (NIDS)"},
            {"id": "B", "text": "Host-based IDS (HIDS)"},
            {"id": "C", "text": "Proxy firewall"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A host-based IDS runs on the endpoint and monitors local activity (logs, file changes, "
                       "processes), seeing things a network sensor cannot, such as host-local or encrypted-then-decrypted activity.",
            "distractors": {
                "A": "A NIDS monitors traffic on a network segment, not a single host's internal logs and files.",
                "C": "A proxy firewall mediates connections at the application layer; it is not an endpoint IDS.",
                "D": "A load balancer distributes traffic; it is not an intrusion-detection sensor.",
            },
            "exam_pattern": "Sensor on the endpoint watching local logs/files/processes = HIDS; on the wire = NIDS.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-r2-023", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 2, "type": "mcq",
        "stem": "Which firewall type tracks the state of active connections so it can automatically permit the "
                "return traffic of a session it already allowed, instead of judging each packet in isolation?",
        "options": [
            {"id": "A", "text": "Stateless packet filter"},
            {"id": "B", "text": "Stateful inspection firewall"},
            {"id": "C", "text": "A hub"},
            {"id": "D", "text": "A repeater"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A stateful inspection firewall maintains a connection/state table, so return packets of an "
                       "established, permitted session are allowed without a separate inbound rule.",
            "distractors": {
                "A": "A stateless packet filter evaluates each packet independently and keeps no connection state.",
                "C": "A hub repeats frames to all ports; it performs no filtering at all.",
                "D": "A repeater regenerates signals on a segment; it is not a firewall.",
            },
            "exam_pattern": "Tracks connection state to allow return traffic = stateful inspection firewall.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-r2-024", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 3, "type": "mcq",
        "stem": "To slip past a firewall rule that only trusts a specific internal source address, an attacker "
                "forges the source IP of their packets to impersonate that trusted host. Which technique is this?",
        "options": [
            {"id": "A", "text": "IP address spoofing"},
            {"id": "B", "text": "Payload encoding"},
            {"id": "C", "text": "Protocol tunneling"},
            {"id": "D", "text": "Packet fragmentation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IP spoofing forges the source address to masquerade as a trusted host, defeating source-based "
                       "ACLs; ingress/egress filtering (e.g., BCP 38) is a core defense.",
            "distractors": {
                "B": "Encoding obfuscates the payload to dodge signatures; it does not impersonate a trusted source IP.",
                "C": "Tunneling hides traffic inside an allowed protocol; it is not source-address forgery.",
                "D": "Fragmentation splits packets to confuse reassembly; it does not spoof the source address.",
            },
            "exam_pattern": "Forge the source IP to impersonate a trusted host = IP spoofing (ingress filtering defends).",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },
    {
        "id": "ceh-net-r2-025", "exam": "ceh", "domain": "ceh_network_perimeter",
        "subtopic": "ceh_evading_ids_fw", "difficulty": 2, "type": "multi",
        "stem": "Which TWO are legitimate defensive benefits of deploying a honeypot? (Choose two.)",
        "options": [
            {"id": "A", "text": "It detects and studies attacker techniques with very few false positives"},
            {"id": "B", "text": "It can divert attackers away from real production systems"},
            {"id": "C", "text": "It serves as the organization's primary production database"},
            {"id": "D", "text": "It removes the need to patch production systems"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A honeypot has no production use, so almost any interaction is suspicious (low false positives), "
                       "and it can lure and delay attackers away from real assets while defenders observe their methods.",
            "distractors": {
                "C": "A honeypot must hold no real production data; using it as a production database defeats its purpose and is dangerous.",
                "D": "Honeypots aid detection and research; they never replace patching real systems.",
            },
            "exam_pattern": "Honeypot value = low-false-positive detection + diversion/study; never production data or a patch substitute.",
        },
        "references": ["CEH v13 Module 12: Evading IDS, Firewalls, and Honeypots"],
    },

    # ====================================================================
    # Domain 4.0 - Web Application Hacking  (web, 16)
    # ====================================================================

    # ----- ceh_web_servers (5) -----------------------------------------
    {
        "id": "ceh-web-r2-001", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "mcq",
        "stem": "Attackers alter the visual content of an organization's public home page to display their own "
                "message, primarily to embarrass the victim and damage its reputation. Which web-server attack is this?",
        "options": [
            {"id": "A", "text": "Website defacement"},
            {"id": "B", "text": "Directory traversal"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Denial-of-service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Website defacement replaces or modifies the site's visible content to push the attacker's "
                       "message, usually for notoriety or hacktivism, harming the owner's reputation.",
            "distractors": {
                "B": "Directory traversal reads files outside the web root; it is not about changing the home page's appearance.",
                "C": "SQL injection manipulates database queries; defacement is about altering displayed content.",
                "D": "A denial-of-service makes the site unavailable; it does not rewrite the page's content.",
            },
            "exam_pattern": "Replace the visible page to send a message = website defacement.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-r2-002", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "multi",
        "stem": "Which TWO HTTP methods, if left unnecessarily enabled on a web server, can let an attacker "
                "upload or delete files on the server? (Choose two.)",
        "options": [
            {"id": "A", "text": "PUT"},
            {"id": "B", "text": "DELETE"},
            {"id": "C", "text": "GET"},
            {"id": "D", "text": "HEAD"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "PUT can write/upload a file and DELETE can remove one; if these methods are enabled without "
                       "strict controls, an attacker may place a web shell or destroy content. Disable unneeded methods.",
            "distractors": {
                "C": "GET retrieves a resource; it is a standard, expected read method, not a file-write primitive.",
                "D": "HEAD returns only headers (no body); it is low-risk and does not modify files.",
            },
            "exam_pattern": "Risky write methods to disable = PUT/DELETE; GET/HEAD are normal read methods.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-r2-003", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "mcq",
        "stem": "Requesting a folder with no index page, an attacker receives the server's full list of files and "
                "subfolders, revealing scripts and backups. Which misconfiguration caused this?",
        "options": [
            {"id": "A", "text": "Directory listing (directory browsing) enabled"},
            {"id": "B", "text": "Directory traversal"},
            {"id": "C", "text": "Default administrative credentials"},
            {"id": "D", "text": "Cross-site scripting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When directory listing/browsing is enabled and no index file exists, the server returns the "
                       "folder's contents, leaking structure and files; disable auto-indexing to fix it.",
            "distractors": {
                "B": "Directory traversal uses ../ sequences to escape the web root; here the server simply lists a folder it serves.",
                "C": "Default admin credentials are a login weakness, not the cause of an exposed file listing.",
                "D": "XSS runs script in a victim's browser; it does not enumerate server folders.",
            },
            "exam_pattern": "Server lists folder contents when no index page = directory listing/browsing enabled.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-r2-004", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "mcq",
        "stem": "A web application returns detailed stack traces and raw database error text to end users. Beyond "
                "being untidy, why is this a security concern?",
        "options": [
            {"id": "A", "text": "It is information disclosure that helps attackers fingerprint and target the stack"},
            {"id": "B", "text": "It encrypts traffic too strongly for clients"},
            {"id": "C", "text": "It forces all users to use HTTPS"},
            {"id": "D", "text": "It is a denial-of-service against the database"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Verbose errors leak internal details (software versions, file paths, SQL structure) - "
                       "information disclosure that lets an attacker tailor further attacks. Return generic error pages instead.",
            "distractors": {
                "B": "Verbose errors have nothing to do with encryption strength.",
                "C": "Showing errors does not force HTTPS; it exposes internals over whatever transport is used.",
                "D": "Leaking error text is disclosure, not a denial-of-service on the database.",
            },
            "exam_pattern": "Detailed stack traces/DB errors to users = information disclosure (use generic error pages).",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-r2-005", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Hardening a web server by removing sample applications, default accounts, and "
                "unused modules shrinks its attack ______, giving an attacker fewer things to target.",
        "correct": ["surface", "attack surface"],
        "explanation": {
            "correct": "Reducing the attack surface - the sum of exposed features and entry points - by stripping "
                       "samples, defaults, and unused components is a foundational web-server hardening practice.",
            "distractors": {},
            "exam_pattern": "Remove samples/defaults/unused modules to shrink the attack = surface.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },

    # ----- ceh_web_apps (6) --------------------------------------------
    {
        "id": "ceh-web-r2-006", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "An attacker abuses a vulnerable feature to make the server itself fetch a URL of the attacker's "
                "choosing, reaching internal-only services or a cloud metadata endpoint. Which OWASP Top 10 attack is this?",
        "options": [
            {"id": "A", "text": "Server-Side Request Forgery (SSRF)"},
            {"id": "B", "text": "Cross-Site Request Forgery (CSRF)"},
            {"id": "C", "text": "Reflected XSS"},
            {"id": "D", "text": "Insecure direct object reference"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSRF tricks the server into making attacker-chosen requests, so it can reach internal systems "
                       "or cloud metadata that the attacker cannot hit directly; allow-list outbound destinations to defend.",
            "distractors": {
                "B": "CSRF makes the victim's browser (not the server) send a forged request using the user's session.",
                "C": "Reflected XSS runs script in the victim's browser; it does not make the server fetch URLs.",
                "D": "IDOR reaches other users' objects via reference tampering; it is not server-side URL fetching.",
            },
            "exam_pattern": "Make the SERVER fetch an attacker URL (internal/metadata) = SSRF; browser-side forged request = CSRF.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-r2-007", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "A web form passes user input unsanitized into a server-side operating-system shell call, letting "
                "an attacker run arbitrary system commands on the host. Which vulnerability class is this?",
        "options": [
            {"id": "A", "text": "OS command injection"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Cross-site scripting"},
            {"id": "D", "text": "Directory traversal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Command injection occurs when untrusted input is concatenated into an OS command, so the "
                       "attacker executes system commands; avoid shelling out and use safe APIs with strict input validation.",
            "distractors": {
                "B": "SQL injection alters database queries, not OS shell commands.",
                "C": "XSS runs script in the browser; command injection runs commands on the server OS.",
                "D": "Directory traversal reads files via path manipulation; it does not execute OS commands.",
            },
            "exam_pattern": "Untrusted input into an OS shell call = command injection (runs system commands).",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-r2-008", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "A 'page=' parameter lets an attacker make the application load and execute a script hosted on "
                "the attacker's own remote server. Which attack is this, specifically?",
        "options": [
            {"id": "A", "text": "Local File Inclusion (LFI)"},
            {"id": "B", "text": "Remote File Inclusion (RFI)"},
            {"id": "C", "text": "Reflected XSS"},
            {"id": "D", "text": "Clickjacking"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Remote File Inclusion makes the app include and run a file fetched from a remote (attacker) "
                       "URL, often leading to code execution; disable remote includes and validate the parameter.",
            "distractors": {
                "A": "LFI includes a file already present on the local server, not one fetched from a remote URL.",
                "C": "Reflected XSS executes script in the browser, not a server-side remote include.",
                "D": "Clickjacking tricks a user into clicking a hidden element; it does not include remote files.",
            },
            "exam_pattern": "Include/execute a file from a REMOTE URL = RFI; from the LOCAL server = LFI.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-r2-009", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "A web app parses attacker-supplied XML that declares an external entity pointing at a local "
                "server file, causing the parser to read and return that file's contents. Which attack is this?",
        "options": [
            {"id": "A", "text": "XML External Entity (XXE) injection"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Cross-site request forgery"},
            {"id": "D", "text": "Clickjacking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "XXE abuses an XML parser that resolves external entities, letting an attacker read local "
                       "files or reach internal systems; disable external entity/DTD processing to prevent it.",
            "distractors": {
                "B": "SQL injection targets database queries, not XML entity resolution.",
                "C": "CSRF forces a state-changing request via the victim's session; it is not XML parsing abuse.",
                "D": "Clickjacking manipulates UI layering; it does not involve XML external entities.",
            },
            "exam_pattern": "Malicious XML external entity reading server files = XXE (disable external entities).",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-r2-010", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "An attacker overlays an invisible frame of a target site on top of harmless-looking decoy "
                "content so the victim's clicks are hijacked into actions on the target. Which header best defends this?",
        "options": [
            {"id": "A", "text": "X-Frame-Options (or CSP frame-ancestors) - the attack is clickjacking"},
            {"id": "B", "text": "Content-Length - the attack is SQL injection"},
            {"id": "C", "text": "Accept-Encoding - the attack is a SYN flood"},
            {"id": "D", "text": "User-Agent - the attack is ARP poisoning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Clickjacking frames the target invisibly to steal clicks; X-Frame-Options or the CSP "
                       "frame-ancestors directive tells browsers to refuse framing the page, defeating it.",
            "distractors": {
                "B": "Content-Length is a size header and does not defend against clickjacking; SQLi is unrelated here.",
                "C": "Accept-Encoding negotiates compression; a SYN flood is a network DoS, not a framing attack.",
                "D": "User-Agent identifies the client; ARP poisoning is a LAN attack unrelated to framing.",
            },
            "exam_pattern": "Invisible frame stealing clicks = clickjacking; defend with X-Frame-Options / CSP frame-ancestors.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-r2-011", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "An application rebuilds objects from untrusted serialized data without validating it, letting a "
                "crafted object trigger remote code execution. Which flaw is this?",
        "options": [
            {"id": "A", "text": "Insecure deserialization"},
            {"id": "B", "text": "Broken access control"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Security misconfiguration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Insecure deserialization trusts attacker-controlled serialized data; a malicious object can "
                       "execute code or tamper with logic. Validate/sign serialized data or avoid native deserialization.",
            "distractors": {
                "B": "Broken access control is about missing authorization checks, not reconstructing malicious objects.",
                "C": "SQL injection manipulates queries; it is not object deserialization.",
                "D": "Security misconfiguration covers insecure settings/defaults, a different root cause.",
            },
            "exam_pattern": "Rebuild untrusted serialized objects -> code execution = insecure deserialization.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },

    # ----- ceh_sql_injection (5) ---------------------------------------
    {
        "id": "ceh-web-r2-012", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 3, "type": "mcq",
        "stem": "Malicious input is safely stored on first submission but is later used unsafely by a different "
                "query, so the injection fires during a subsequent operation rather than at input time. Which SQLi type?",
        "options": [
            {"id": "A", "text": "Second-order (stored) SQL injection"},
            {"id": "B", "text": "UNION-based in-band SQL injection"},
            {"id": "C", "text": "Error-based SQL injection"},
            {"id": "D", "text": "Classic reflected SQL injection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Second-order SQL injection stores tainted input that a later, different query executes "
                       "unsafely, so the payload triggers on a subsequent action - harder to spot in testing.",
            "distractors": {
                "B": "UNION-based injection returns data directly in the immediate response (in-band).",
                "C": "Error-based injection leaks data through database error messages in the same response.",
                "D": "'Reflected' is an XSS concept; classic in-band SQLi fires on the same request, not later.",
            },
            "exam_pattern": "Stored input exploited by a LATER query = second-order (stored) SQL injection.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-r2-013", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 3, "type": "mcq",
        "stem": "When results cannot be returned in the HTTP response, an attacker makes the database send the "
                "stolen data to an attacker-controlled server over DNS or HTTP. Which SQL injection category is this?",
        "options": [
            {"id": "A", "text": "Out-of-band SQL injection"},
            {"id": "B", "text": "In-band (classic) SQL injection"},
            {"id": "C", "text": "Boolean-based blind SQL injection"},
            {"id": "D", "text": "UNION-based SQL injection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Out-of-band SQLi exfiltrates data through a separate channel (DNS/HTTP callbacks) when the "
                       "app does not return results or respond timingly in-band - useful against blind, quiet endpoints.",
            "distractors": {
                "B": "In-band SQLi returns data in the same response channel, the opposite of out-of-band.",
                "C": "Boolean-based blind infers data from true/false response differences, still in the same channel.",
                "D": "UNION-based returns data directly in the response (in-band).",
            },
            "exam_pattern": "Exfiltrate via a separate channel (DNS/HTTP) = out-of-band SQL injection.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-r2-014", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 3, "type": "mcq",
        "stem": "Beyond using parameterized queries, which configuration most limits the damage of a successful "
                "SQL injection by ensuring the application's database account cannot drop tables or read system data?",
        "options": [
            {"id": "A", "text": "Grant the app's database account only least-privilege permissions"},
            {"id": "B", "text": "Enforce client-side input length limits"},
            {"id": "C", "text": "Hide the database version banner"},
            {"id": "D", "text": "Increase user password length"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Running the application under a least-privilege database account means even a successful "
                       "injection cannot drop tables or reach system catalogs, containing the blast radius (defense in depth).",
            "distractors": {
                "B": "Client-side limits are trivially bypassed by sending requests directly to the server.",
                "C": "Hiding the banner is obscurity; it does not limit what a successful injection can do.",
                "D": "User password length does not constrain the database account's privileges.",
            },
            "exam_pattern": "Limit SQLi blast radius = least-privilege DB account (plus parameterized queries).",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-r2-015", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 2, "type": "mcq",
        "stem": "Which control inspects incoming HTTP requests for malicious patterns such as SQL injection and "
                "XSS and can block them before they reach the application, acting as a compensating defense?",
        "options": [
            {"id": "A", "text": "A Web Application Firewall (WAF)"},
            {"id": "B", "text": "A traditional network firewall (port/IP filtering)"},
            {"id": "C", "text": "A load balancer"},
            {"id": "D", "text": "A DNS resolver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A WAF inspects HTTP(S) request content at the application layer and can block SQLi/XSS "
                       "patterns, serving as a compensating control while code is fixed (not a replacement for secure coding).",
            "distractors": {
                "B": "A network firewall filters by port/IP/state; it does not parse HTTP payloads for SQLi/XSS.",
                "C": "A load balancer distributes traffic; it does not inspect for web-attack payloads.",
                "D": "A DNS resolver maps names to IPs; it has no role in blocking web-app attacks.",
            },
            "exam_pattern": "Inspect/block SQLi/XSS in HTTP requests = Web Application Firewall (WAF).",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-r2-016", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank: A ______ query injection appends a second complete statement after a "
                "semicolon (for example a SELECT followed by a separate DROP), when the database driver allows multiple "
                "statements in one call.",
        "correct": ["stacked", "stacked queries", "batched", "piggybacked"],
        "explanation": {
            "correct": "Stacked (batched) queries chain a second standalone statement after a semicolon; if the "
                       "driver executes multiple statements, this lets an attacker run entirely new commands.",
            "distractors": {},
            "exam_pattern": "Second full statement after a semicolon = stacked (batched) queries.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },

    # ====================================================================
    # Domain 5.0 - Wireless, Mobile, IoT and OT Hacking  (wifi, 13)
    # ====================================================================

    # ----- ceh_wireless (5) --------------------------------------------
    {
        "id": "ceh-wifi-r2-001", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 3, "type": "mcq",
        "stem": "Which WPA2 attack manipulates the 4-way handshake to force a client to reinstall an "
                "already-in-use key (an all-zero key), allowing decryption of traffic - without recovering the Wi-Fi password?",
        "options": [
            {"id": "A", "text": "KRACK (key reinstallation attack)"},
            {"id": "B", "text": "WPS PIN brute force"},
            {"id": "C", "text": "Evil twin"},
            {"id": "D", "text": "Deauthentication flood"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "KRACK replays handshake message 3 so the client reinstalls a used key (resetting nonces), "
                       "enabling traffic decryption/forgery; it is a flaw in the WPA2 standard, fixed by patching clients.",
            "distractors": {
                "B": "WPS PIN brute force recovers the passphrase via the weak WPS PIN, a different weakness.",
                "C": "An evil twin is a rogue AP impersonating an SSID, not a handshake key-reinstallation flaw.",
                "D": "A deauth flood disconnects clients; KRACK instead abuses the handshake to reinstall a key.",
            },
            "exam_pattern": "WPA2 handshake key reinstallation (all-zero key), no password recovery = KRACK.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-r2-002", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "mcq",
        "stem": "Driving around an area with a Wi-Fi adapter and GPS to discover, locate, and map wireless "
                "networks and their security settings is known as?",
        "options": [
            {"id": "A", "text": "Wardriving"},
            {"id": "B", "text": "War dialing"},
            {"id": "C", "text": "Bluesnarfing"},
            {"id": "D", "text": "Evil twin"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Wardriving surveys and maps Wi-Fi networks (often with GPS) while moving through an area, "
                       "building a picture of SSIDs, locations, and encryption in use.",
            "distractors": {
                "B": "War dialing scans ranges of phone numbers for modems/systems, not Wi-Fi mapping.",
                "C": "Bluesnarfing steals data over Bluetooth; it is not Wi-Fi discovery by driving around.",
                "D": "An evil twin is a rogue AP impersonating a legitimate SSID, not a mapping technique.",
            },
            "exam_pattern": "Drive around mapping Wi-Fi networks with GPS = wardriving.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-r2-003", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "mcq",
        "stem": "Which Bluetooth attack involves stealing data - contacts, messages, or files - from a vulnerable "
                "device over its Bluetooth connection?",
        "options": [
            {"id": "A", "text": "Bluejacking"},
            {"id": "B", "text": "Bluesnarfing"},
            {"id": "C", "text": "Bluebugging"},
            {"id": "D", "text": "Evil twin"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Bluesnarfing is the unauthorized theft of data (contacts, messages, files) from a device "
                       "over Bluetooth, exploiting weak pairing or implementation flaws.",
            "distractors": {
                "A": "Bluejacking sends unsolicited messages to a device; it does not steal data from it.",
                "C": "Bluebugging takes control of a device's functions (e.g., calls); its hallmark is control, not data theft.",
                "D": "An evil twin is a rogue Wi-Fi access point, not a Bluetooth attack.",
            },
            "exam_pattern": "Steal data over Bluetooth = bluesnarfing; send spam = bluejacking; control the device = bluebugging.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-r2-004", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 3, "type": "mcq",
        "stem": "Which Wi-Fi deployment authenticates each user individually against a RADIUS server using "
                "802.1X/EAP, instead of everyone sharing one pre-shared key?",
        "options": [
            {"id": "A", "text": "WPA2-Personal (PSK)"},
            {"id": "B", "text": "WPA2-Enterprise"},
            {"id": "C", "text": "WEP"},
            {"id": "D", "text": "An open network"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "WPA2-Enterprise uses 802.1X/EAP with a RADIUS server so each user authenticates with unique "
                       "credentials; revoking one user does not require changing a shared key for everyone.",
            "distractors": {
                "A": "WPA2-Personal uses a single shared pre-shared key for all clients, not per-user RADIUS auth.",
                "C": "WEP is broken legacy encryption with no per-user 802.1X authentication of this kind.",
                "D": "An open network provides no authentication or encryption at all.",
            },
            "exam_pattern": "Per-user 802.1X/EAP via RADIUS = WPA2-Enterprise; shared key = WPA2-Personal.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-r2-005", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Hiding a wireless network by disabling ______ broadcast provides only weak "
                "security, because the network name is still revealed in client probe and association frames.",
        "correct": ["ssid", "the ssid"],
        "explanation": {
            "correct": "Disabling SSID broadcast merely stops beacon advertisement; the SSID still appears in probe "
                       "requests/responses and association frames, so a sniffer recovers it - it is obscurity, not security.",
            "distractors": {},
            "exam_pattern": "Hiding the network name (disable SSID broadcast) is weak obscurity, not real security.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },

    # ----- ceh_mobile_platforms (4) ------------------------------------
    {
        "id": "ceh-wifi-r2-006", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 3, "type": "mcq",
        "stem": "Which mobile-app defense hard-codes the expected server certificate or public key so that a "
                "man-in-the-middle presenting a different (even validly signed) certificate is rejected?",
        "options": [
            {"id": "A", "text": "Certificate pinning"},
            {"id": "B", "text": "Jailbreaking"},
            {"id": "C", "text": "Sideloading"},
            {"id": "D", "text": "Rooting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Certificate (or public-key) pinning makes the app trust only a specific certificate/key, so "
                       "an interception proxy with a different cert is refused - a strong anti-MITM control for mobile apps.",
            "distractors": {
                "B": "Jailbreaking removes iOS restrictions; it weakens security rather than defending against MITM.",
                "C": "Sideloading installs apps outside the official store - a risk, not a TLS defense.",
                "D": "Rooting removes Android restrictions; it does not pin certificates.",
            },
            "exam_pattern": "App trusts only a specific pinned cert/key to stop MITM = certificate pinning.",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-r2-007", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "mcq",
        "stem": "An attacker takes a legitimate Android app, inserts malicious code, and redistributes the "
                "modified package through third-party stores. Which mobile threat is this?",
        "options": [
            {"id": "A", "text": "App repackaging"},
            {"id": "B", "text": "Certificate pinning"},
            {"id": "C", "text": "Mobile device management"},
            {"id": "D", "text": "Containerization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "App repackaging rebuilds a trusted app with added malware and distributes it (often via "
                       "third-party stores), tricking users who think they are installing the legitimate app.",
            "distractors": {
                "B": "Certificate pinning is a defensive control, not an attack that trojanizes an app.",
                "C": "MDM is an enterprise management platform, not a repackaging attack.",
                "D": "Containerization separates work and personal data - a defense, not this threat.",
            },
            "exam_pattern": "Trojanize a legit app and redistribute it = app repackaging.",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-r2-008", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "mcq",
        "stem": "A hidden app secretly installed on a target's phone to monitor their location, messages, and "
                "calls (sometimes sold as 'stalkerware') is best classified as which type of mobile malware?",
        "options": [
            {"id": "A", "text": "Spyware"},
            {"id": "B", "text": "Ransomware"},
            {"id": "C", "text": "Adware"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Such stalkerware is spyware: it covertly collects personal data (location, messages, calls) "
                       "and reports it to the attacker, violating the victim's privacy.",
            "distractors": {
                "B": "Ransomware encrypts data and demands payment; it does not quietly monitor the user.",
                "C": "Adware pushes unwanted advertisements rather than covertly surveilling the user.",
                "D": "A rootkit hides presence to maintain access; covert data collection defines spyware here.",
            },
            "exam_pattern": "Covertly monitor location/messages/calls = mobile spyware (stalkerware).",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-r2-009", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: On employee-owned (BYOD) phones, enterprises separate corporate apps and data "
                "from personal data using ______, so a remote wipe can remove only the company's data.",
        "correct": ["containerization", "a container", "containers"],
        "explanation": {
            "correct": "Containerization creates an isolated, managed 'work profile' on the device, letting the "
                       "organization enforce policy and selectively wipe corporate data without touching personal content.",
            "distractors": {},
            "exam_pattern": "Separate work and personal data for selective wipe on BYOD = containerization.",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },

    # ----- ceh_iot_ot (4) ----------------------------------------------
    {
        "id": "ceh-wifi-r2-010", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 2, "type": "mcq",
        "stem": "Which infamous IoT botnet spread by scanning the Internet for devices with open Telnet and "
                "trying a built-in list of factory-default logins, then used them to launch massive DDoS attacks?",
        "options": [
            {"id": "A", "text": "Mirai"},
            {"id": "B", "text": "Stuxnet"},
            {"id": "C", "text": "WannaCry"},
            {"id": "D", "text": "Heartbleed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mirai enslaved IoT devices (cameras, routers) by trying default Telnet credentials, then "
                       "launched record DDoS attacks; changing default credentials and disabling Telnet are the fixes.",
            "distractors": {
                "B": "Stuxnet was a targeted ICS/SCADA worm against centrifuges, not a Telnet-default IoT botnet.",
                "C": "WannaCry was ransomware spread via an SMB exploit, not an IoT default-credential botnet.",
                "D": "Heartbleed was an OpenSSL memory-disclosure vulnerability, not a botnet.",
            },
            "exam_pattern": "IoT botnet via default Telnet logins for DDoS = Mirai.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-r2-011", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 3, "type": "mcq",
        "stem": "Which lightweight, RESTful IoT protocol runs over UDP for constrained devices and, lacking "
                "built-in authentication, relies on DTLS for security when exposed?",
        "options": [
            {"id": "A", "text": "CoAP (Constrained Application Protocol)"},
            {"id": "B", "text": "MQTT"},
            {"id": "C", "text": "Modbus"},
            {"id": "D", "text": "Zigbee"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CoAP is a RESTful, HTTP-like protocol over UDP for constrained IoT devices; it has no "
                       "built-in authentication, so DTLS is used to secure it, and exposed CoAP servers can leak resources.",
            "distractors": {
                "B": "MQTT is a TCP-based publish/subscribe protocol using a broker, not a RESTful UDP protocol.",
                "C": "Modbus is a legacy industrial (OT) protocol, not a RESTful UDP IoT protocol.",
                "D": "Zigbee is a low-power mesh radio standard, not a RESTful UDP application protocol.",
            },
            "exam_pattern": "RESTful UDP protocol for constrained IoT, secured by DTLS = CoAP.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-r2-012", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 3, "type": "mcq",
        "stem": "Which reference model segments industrial control system (OT) networks into hierarchical levels "
                "- from the physical process up to enterprise IT - to guide where security zones and conduits belong?",
        "options": [
            {"id": "A", "text": "The Purdue model (Purdue Enterprise Reference Architecture)"},
            {"id": "B", "text": "The OSI model"},
            {"id": "C", "text": "The Cyber Kill Chain"},
            {"id": "D", "text": "The STRIDE model"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Purdue model organizes ICS/OT into hierarchical levels (physical process up to enterprise), "
                       "guiding segmentation into zones and conduits between IT and OT.",
            "distractors": {
                "B": "The OSI model describes seven networking layers generally; it is not an ICS segmentation model.",
                "C": "The Cyber Kill Chain describes attack phases, not OT network segmentation.",
                "D": "STRIDE is a threat-modeling taxonomy, not an ICS reference architecture.",
            },
            "exam_pattern": "Hierarchical ICS/OT segmentation model (process up to enterprise) = the Purdue model.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-r2-013", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 3, "type": "mcq",
        "stem": "In an OT environment, which device directly controls physical equipment such as motors, pumps, "
                "and valves, making it a prime target because compromising it affects the physical process itself?",
        "options": [
            {"id": "A", "text": "Programmable logic controller (PLC)"},
            {"id": "B", "text": "Human-machine interface (HMI) display"},
            {"id": "C", "text": "Data historian"},
            {"id": "D", "text": "Enterprise router"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A PLC executes control logic that drives field equipment (motors, valves), so compromising it "
                       "can directly disrupt or damage the physical process - a high-impact OT target.",
            "distractors": {
                "B": "An HMI is the operator's screen for monitoring/control; it does not itself drive the equipment logic.",
                "C": "A historian stores process data for analysis; it does not control field devices.",
                "D": "An enterprise router forwards IT traffic; it is not the controller of physical OT equipment.",
            },
            "exam_pattern": "Device executing control logic that drives physical equipment = PLC (prime OT target).",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },

    # ====================================================================
    # Domain 6.0 - Cloud Computing and Cryptography  (cc, 8)
    # ====================================================================

    # ----- ceh_cloud_computing (4) -------------------------------------
    {
        "id": "ceh-cc-r2-001", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 3, "type": "mcq",
        "stem": "An attacker exploits an SSRF flaw in a cloud virtual machine to query the instance metadata "
                "service and steal the VM's temporary IAM credentials. Which component was the target?",
        "options": [
            {"id": "A", "text": "The cloud instance metadata service"},
            {"id": "B", "text": "The hypervisor"},
            {"id": "C", "text": "A cloud access security broker (CASB)"},
            {"id": "D", "text": "A web application firewall (WAF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The instance metadata service returns a VM's identity and temporary role credentials; an "
                       "SSRF that reaches it can exfiltrate those credentials. Enforcing the hardened/session-token metadata mode mitigates it.",
            "distractors": {
                "B": "The hypervisor is provider-managed infrastructure, not the endpoint an SSRF queries for VM credentials.",
                "C": "A CASB brokers user-to-cloud access policy; it is not the metadata endpoint being abused.",
                "D": "A WAF filters inbound web attacks; it is a control, not the component that stores VM role credentials.",
            },
            "exam_pattern": "SSRF -> instance metadata service -> steal temporary IAM credentials.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-r2-002", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability lets a process break out of its container and gain access to the host operating "
                "system or other containers on the same host. Which risk is this?",
        "options": [
            {"id": "A", "text": "Container escape (breakout)"},
            {"id": "B", "text": "A collision attack"},
            {"id": "C", "text": "DNS poisoning"},
            {"id": "D", "text": "Credential stuffing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A container escape breaks the isolation boundary, giving the attacker the host or neighboring "
                       "containers; it is a top container-security concern, mitigated by least privilege, no --privileged, and patching the runtime.",
            "distractors": {
                "B": "A collision attack finds two inputs with the same hash; it is a cryptographic attack, not container breakout.",
                "C": "DNS poisoning corrupts resolver caches; it is unrelated to container isolation.",
                "D": "Credential stuffing replays leaked credentials; it is not a container-isolation failure.",
            },
            "exam_pattern": "Break out of a container to the host/other containers = container escape.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-r2-003", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 3, "type": "mcq",
        "stem": "Which class of tool continuously scans cloud accounts for misconfigurations - public storage "
                "buckets, open security groups, overly broad IAM - and checks them against security benchmarks?",
        "options": [
            {"id": "A", "text": "Cloud Security Posture Management (CSPM)"},
            {"id": "B", "text": "Cloud Access Security Broker (CASB)"},
            {"id": "C", "text": "Web Application Firewall (WAF)"},
            {"id": "D", "text": "Security Information and Event Management (SIEM)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CSPM continuously assesses cloud configuration against best-practice benchmarks and flags "
                       "misconfigurations (public buckets, open ports, risky IAM), which are leading causes of cloud breaches.",
            "distractors": {
                "B": "A CASB governs user-to-cloud access and visibility (shadow IT); it is not primarily a config-posture scanner.",
                "C": "A WAF filters web-application attacks; it does not audit cloud account configuration.",
                "D": "A SIEM aggregates and correlates logs; posture misconfiguration scanning is CSPM's role.",
            },
            "exam_pattern": "Continuously audit cloud config for misconfiguration = CSPM (vs CASB for access/visibility).",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },
    {
        "id": "ceh-cc-r2-004", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cloud_computing", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The open-source platform ______ automates the deployment, scaling, and "
                "management of containers, and its exposed API server or dashboard is a common cloud attack target.",
        "correct": ["kubernetes", "k8s"],
        "explanation": {
            "correct": "Kubernetes (K8s) orchestrates containers at scale; a misconfigured or exposed API server, "
                       "kubelet, or dashboard can let an attacker deploy workloads or access secrets, so it must be locked down.",
            "distractors": {},
            "exam_pattern": "Container orchestration platform (exposed API server is a target) = Kubernetes.",
        },
        "references": ["CEH v13 Module 19: Cloud Computing"],
    },

    # ----- ceh_cryptography (4) ----------------------------------------
    {
        "id": "ceh-cc-r2-005", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "Which algorithm lets two parties who have never met securely agree on a shared secret over an "
                "untrusted channel, without ever transmitting the secret itself?",
        "options": [
            {"id": "A", "text": "Diffie-Hellman key exchange"},
            {"id": "B", "text": "AES"},
            {"id": "C", "text": "SHA-256"},
            {"id": "D", "text": "MD5"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Diffie-Hellman lets two parties derive a shared secret from exchanged public values, so the "
                       "secret itself never crosses the wire - the basis of key exchange in many secure protocols.",
            "distractors": {
                "B": "AES is a symmetric cipher that uses a key both sides already share; it does not negotiate one.",
                "C": "SHA-256 is a one-way hash for integrity; it cannot establish a shared secret.",
                "D": "MD5 is a (now weak) hash function, not a key-agreement algorithm.",
            },
            "exam_pattern": "Agree on a shared secret over an untrusted channel = Diffie-Hellman key exchange.",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-r2-006", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "Which technique deliberately makes password hashing slow and resource-intensive (using many "
                "iterations or memory-hard functions like bcrypt, scrypt, or PBKDF2) to make brute-force and "
                "rainbow-table attacks far costlier?",
        "options": [
            {"id": "A", "text": "Key stretching"},
            {"id": "B", "text": "Salting"},
            {"id": "C", "text": "Tokenization"},
            {"id": "D", "text": "Steganography"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Key stretching applies a slow or memory-hard function (bcrypt/scrypt/PBKDF2) so each guess "
                       "costs much more, blunting brute-force and precomputed attacks; it is typically combined with per-password salts.",
            "distractors": {
                "B": "Salting adds uniqueness to defeat precomputed tables but does not by itself make each guess slow.",
                "C": "Tokenization substitutes a surrogate value for sensitive data; it is not a password-hashing hardener.",
                "D": "Steganography hides data in a carrier; it is unrelated to slowing password hashing.",
            },
            "exam_pattern": "Make hashing deliberately slow/memory-hard (bcrypt/scrypt/PBKDF2) = key stretching (pair with salt).",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-r2-007", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 2, "type": "mcq",
        "stem": "Which of the following is an ASYMMETRIC algorithm, used for key exchange or digital signatures "
                "rather than bulk symmetric encryption?",
        "options": [
            {"id": "A", "text": "RSA"},
            {"id": "B", "text": "AES"},
            {"id": "C", "text": "3DES"},
            {"id": "D", "text": "RC4"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RSA is an asymmetric algorithm (public/private key pair) used for key transport and digital "
                       "signatures; ECC and Diffie-Hellman are other asymmetric examples.",
            "distractors": {
                "B": "AES is a symmetric block cipher using one shared key.",
                "C": "3DES is a symmetric block cipher (triple DES), not asymmetric.",
                "D": "RC4 is a symmetric stream cipher, now deprecated.",
            },
            "exam_pattern": "Asymmetric = RSA/ECC/Diffie-Hellman; symmetric = AES/3DES/RC4/Blowfish.",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
    {
        "id": "ceh-cc-r2-008", "exam": "ceh", "domain": "ceh_cloud_crypto",
        "subtopic": "ceh_cryptography", "difficulty": 3, "type": "mcq",
        "stem": "Which PKI mechanism lets a client check, in real time, whether a single specific certificate has "
                "been revoked, instead of downloading and searching a full list of revoked certificates?",
        "options": [
            {"id": "A", "text": "Online Certificate Status Protocol (OCSP)"},
            {"id": "B", "text": "Certificate Revocation List (CRL)"},
            {"id": "C", "text": "Certificate Signing Request (CSR)"},
            {"id": "D", "text": "Certificate Authority (CA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OCSP queries the responder for the status of one certificate in real time, avoiding the "
                       "overhead of downloading a whole CRL; OCSP stapling lets the server present a signed status to clients.",
            "distractors": {
                "B": "A CRL is the full, periodically published list of revoked certificates the client must download and search.",
                "C": "A CSR is the request submitted to obtain a certificate; it does not check revocation.",
                "D": "The CA issues and signs certificates; checking revocation status is done via OCSP or a CRL.",
            },
            "exam_pattern": "Real-time status of ONE cert = OCSP; the full downloaded list = CRL.",
        },
        "references": ["CEH v13 Module 20: Cryptography"],
    },
]
