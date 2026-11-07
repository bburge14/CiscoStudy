"""CompTIA Network+ N10-009 EXPANSION pool — Domain 5.0 Network Troubleshooting.

Original, objective-aligned questions that deepen the base netplus bank
(netplus-nt-001..006 in content_netplus.py) toward real exam depth. These are
original items mapped to the public exam objectives, never real exam items.
build_content.py shuffles option order, so the keyed answer below is not
positionally biased.

Subtopics covered (exact blueprint strings):
    troubleshooting_methodology, cabling_issues, connectivity_tools,
    network_service_issues, performance_issues

IDs start at netplus-nt-101 to avoid colliding with the base pool.
"""

QUESTIONS = [
    # ===== 5.0 troubleshooting_methodology ==================================
    {
        "id": "netplus-nt-101", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 1, "type": "mcq",
        "stem": "A ticket states only 'the internet is down.' Before changing anything, the "
                "technician interviews the user, asks what recently changed, and tries to "
                "reproduce the failure. Which step of the CompTIA methodology is this?",
        "options": [
            {"id": "A", "text": "Identify the problem"},
            {"id": "B", "text": "Establish a theory of probable cause"},
            {"id": "C", "text": "Test the theory to determine the cause"},
            {"id": "D", "text": "Verify full system functionality"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Step 1, identify the problem, is where you gather information, question users, "
                       "determine what changed, and duplicate the problem if possible.",
            "distractors": {
                "B": "Establishing a theory (step 2) comes only after you have identified and scoped the problem.",
                "C": "Testing the theory (step 3) requires a theory to test, which does not exist yet.",
                "D": "Verifying full functionality (step 6) happens after a fix is implemented.",
            },
            "exam_pattern": "Gather info / question users / ask what changed / duplicate = Step 1, Identify the problem.",
        },
    },
    {
        "id": "netplus-nt-102", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 2, "type": "mcq",
        "stem": "A technician has implemented a fix and the application now responds. According to "
                "the CompTIA methodology, what should be done BEFORE documenting the outcome?",
        "options": [
            {"id": "A", "text": "Verify full system functionality and, if applicable, implement preventive measures"},
            {"id": "B", "text": "Establish a theory of probable cause"},
            {"id": "C", "text": "Identify the problem and question users"},
            {"id": "D", "text": "Escalate the issue to the vendor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Step 6 is verify full system functionality and implement preventive measures; "
                       "documentation (step 7) is the final step, after verification.",
            "distractors": {
                "B": "Establishing a theory is step 2, long before a fix is implemented.",
                "C": "Identifying the problem is step 1, the very beginning of the process.",
                "D": "Escalation belongs to step 5 (implement the solution OR escalate), not after a successful fix.",
            },
            "exam_pattern": "After the fix, VERIFY (step 6) before you DOCUMENT (step 7).",
        },
    },
    {
        "id": "netplus-nt-103", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 3, "type": "mcq",
        "stem": "While testing a theory of probable cause, the technician proves the theory is "
                "wrong. According to the CompTIA methodology, what is the correct NEXT action?",
        "options": [
            {"id": "A", "text": "Establish a new theory or escalate"},
            {"id": "B", "text": "Implement the original solution anyway and watch for results"},
            {"id": "C", "text": "Document that the problem cannot be solved"},
            {"id": "D", "text": "Verify full system functionality"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "If testing does not confirm the theory, the methodology says to establish a new theory "
                       "(reattempt step 2) or escalate to someone with more expertise.",
            "distractors": {
                "B": "Implementing a fix for a disproven theory is premature; you have not found the cause.",
                "C": "A disproven theory does not mean the problem is unsolvable; you form another theory.",
                "D": "Verification occurs only after a solution has actually been implemented.",
            },
            "exam_pattern": "Theory confirmed -> plan/implement. Theory NOT confirmed -> new theory or escalate.",
        },
    },
    {
        "id": "netplus-nt-104", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 3, "type": "mcq",
        "stem": "When establishing a theory of probable cause, a technician deliberately begins at "
                "Layer 1 (check the cable and link) and works upward through the OSI model. What "
                "is this approach called?",
        "options": [
            {"id": "A", "text": "The bottom-to-top OSI approach"},
            {"id": "B", "text": "The top-to-bottom OSI approach"},
            {"id": "C", "text": "Divide and conquer"},
            {"id": "D", "text": "Escalation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Starting at the physical layer and moving up toward the application layer is the "
                       "bottom-to-top (bottom-up) OSI troubleshooting approach.",
            "distractors": {
                "B": "Top-to-bottom starts at the application layer and works DOWN toward the physical layer.",
                "C": "Divide and conquer starts at a middle layer and moves up or down based on results.",
                "D": "Escalation is handing the issue to higher-tier support, not an OSI testing strategy.",
            },
            "exam_pattern": "Layer 1 upward = bottom-to-top; Layer 7 downward = top-to-bottom; start in the middle = divide and conquer.",
        },
    },
    {
        "id": "netplus-nt-105", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "troubleshooting_methodology", "difficulty": 2, "type": "multi",
        "stem": "Which activities belong to Step 1, 'Identify the problem,' of the CompTIA "
                "troubleshooting methodology? (Choose two.)",
        "options": [
            {"id": "A", "text": "Question users and gather information about the symptoms"},
            {"id": "B", "text": "Determine whether anything has recently changed"},
            {"id": "C", "text": "Implement preventive measures"},
            {"id": "D", "text": "Submit a final root-cause report to management"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Step 1 includes gathering information, questioning users, identifying symptoms, "
                       "determining if anything changed, and duplicating the problem if possible.",
            "distractors": {
                "C": "Implementing preventive measures is part of step 6 (verify full system functionality).",
                "D": "Reporting/documenting findings and outcomes is step 7, the final step.",
            },
            "exam_pattern": "Identify the problem = ask users, find symptoms, ask what changed, duplicate the issue.",
        },
    },

    # ===== 5.0 cabling_issues ===============================================
    {
        "id": "netplus-nt-106", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 3, "type": "mcq",
        "stem": "A copper patch cable passes a basic wiremap/continuity test showing all eight pins "
                "connected end-to-end, yet gigabit links on it suffer excessive crosstalk and "
                "errors. Which wiring fault is MOST likely?",
        "options": [
            {"id": "A", "text": "Split pairs"},
            {"id": "B", "text": "An open on pin 1"},
            {"id": "C", "text": "A short between two conductors"},
            {"id": "D", "text": "Exceeding the 100-meter limit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Split pairs keep correct pin-to-pin continuity (so a basic wiremap tester passes) but "
                       "break the twisted-pair pairing, so near-end crosstalk (NEXT) rises and high-speed links fail. "
                       "A cable certifier is needed to detect it.",
            "distractors": {
                "B": "An open conductor breaks continuity on that pin, so a wiremap tester would flag it, not pass.",
                "C": "A short also fails the continuity test and typically shows as connected pins that should not be.",
                "D": "A distance problem is a loss/attenuation issue unrelated to a cable that tests continuous but has high crosstalk.",
            },
            "exam_pattern": "Continuity test PASSES but crosstalk is high = split pairs (only a certifier catches it).",
        },
    },
    {
        "id": "netplus-nt-107", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "An uplink between two switches uses single-mode (SMF) transceivers, but a technician "
                "patches it with multimode (MMF) fiber jumpers. The link will not come up or shows "
                "very high optical loss. What is the problem?",
        "options": [
            {"id": "A", "text": "Fiber type mismatch - single-mode optics require single-mode fiber"},
            {"id": "B", "text": "The jumpers are too short for the transceivers"},
            {"id": "C", "text": "Auto-MDIX is disabled on the switches"},
            {"id": "D", "text": "The transceivers need a crossover adapter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Single-mode optics are built for the ~9-micron SMF core; forcing their signal through a "
                       "50/62.5-micron multimode core causes severe loss and a failed link. Match fiber type to the optics.",
            "distractors": {
                "B": "Jumper length does not cause a type mismatch; a too-short cord simply would not reach.",
                "C": "Auto-MDIX concerns copper TX/RX crossover, not fiber-mode compatibility.",
                "D": "Crossover adapters relate to copper straight/crossover wiring, not single-mode vs multimode fiber.",
            },
            "exam_pattern": "SMF optics + MMF cord (or vice versa) = fiber type mismatch, huge loss or no link.",
        },
    },
    {
        "id": "netplus-nt-108", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "A UTP run is bundled tightly alongside fluorescent light ballasts and power conduit. "
                "The link shows intermittent errors that get worse whenever the lights are on. Which "
                "cabling issue is this?",
        "options": [
            {"id": "A", "text": "Electromagnetic interference (EMI)"},
            {"id": "B", "text": "Attenuation"},
            {"id": "C", "text": "An open circuit"},
            {"id": "D", "text": "A duplex mismatch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Power conduit and fluorescent ballasts emit electromagnetic fields that induce noise into "
                       "unshielded twisted pair. The correlation with the lights is the tell. Reroute with separation or use shielded cable.",
            "distractors": {
                "B": "Attenuation is signal loss over distance; it is constant and not tied to whether the lights are on.",
                "C": "An open circuit breaks the link entirely rather than causing intermittent, light-correlated errors.",
                "D": "A duplex mismatch causes collisions and CRC errors regardless of nearby lighting.",
            },
            "exam_pattern": "Errors that track with nearby power/lighting = EMI; separate cables or use STP.",
        },
    },
    {
        "id": "netplus-nt-109", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 2, "type": "mcq",
        "stem": "A fiber link that worked at install begins showing increased optical loss and "
                "intermittent errors after a patch cord was repeatedly unplugged and reseated. "
                "Inspection shows contamination on the ferrule end-face. What is the BEST action?",
        "options": [
            {"id": "A", "text": "Clean the fiber connector end-faces with proper fiber-cleaning tools"},
            {"id": "B", "text": "Replace the switch power supply"},
            {"id": "C", "text": "Increase the MTU on both ends"},
            {"id": "D", "text": "Force the interface to half-duplex"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A dirty fiber connector is one of the most common causes of optical loss. Inspecting and "
                       "cleaning the end-face with the correct tools restores the link before considering hardware swaps.",
            "distractors": {
                "B": "A power-supply fault would not produce localized contamination-related optical loss on one link.",
                "C": "MTU affects frame size, not optical signal level on a dirty connector.",
                "D": "Duplex settings are a copper/negotiation concept and do not fix a contaminated fiber end-face.",
            },
            "exam_pattern": "Rising fiber loss after reseating + visible contamination = dirty connector; clean it first.",
        },
    },
    {
        "id": "netplus-nt-110", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "cabling_issues", "difficulty": 3, "type": "mcq",
        "stem": "A patch cable was terminated with the T568A standard on one end and T568B on the "
                "other. On legacy equipment without Auto-MDIX, what is the effect of this cable?",
        "options": [
            {"id": "A", "text": "It behaves as a crossover cable, swapping the transmit and receive pairs"},
            {"id": "B", "text": "It creates a short across all four pairs"},
            {"id": "C", "text": "It automatically exceeds the 100-meter limit"},
            {"id": "D", "text": "It converts the copper link into single-mode fiber"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mixing T568A on one end with T568B on the other swaps pairs 2 and 3, which produces a "
                       "crossover cable - transmit and receive are crossed. Without Auto-MDIX that is wrong for a host-to-switch run.",
            "distractors": {
                "B": "Different termination standards do not short conductors together; each pin still maps to one pin.",
                "C": "Pinout has nothing to do with cable length or the 100-meter channel limit.",
                "D": "Termination standards apply to copper; they cannot turn a cable into fiber.",
            },
            "exam_pattern": "T568A on one end + T568B on the other = a crossover (TX/RX swapped).",
        },
    },

    # ===== 5.0 connectivity_tools ===========================================
    {
        "id": "netplus-nt-111", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "A long-haul fiber link has failed, and the technician needs to find the distance to "
                "a break or high-loss event along the fiber. Which tool is designed for this?",
        "options": [
            {"id": "A", "text": "An OTDR (optical time-domain reflectometer)"},
            {"id": "B", "text": "A tone generator and probe"},
            {"id": "C", "text": "A multimeter"},
            {"id": "D", "text": "A loopback plug"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An OTDR sends light pulses down the fiber and times the reflected light, mapping splices, "
                       "bends, and breaks and reporting the distance to each event.",
            "distractors": {
                "B": "A tone generator and probe traces copper cables, not faults on fiber.",
                "C": "A multimeter measures electrical values (voltage/resistance), not optical fiber faults.",
                "D": "A loopback plug tests a local port or interface; it cannot locate a fiber break by distance.",
            },
            "exam_pattern": "Distance-to-fault on fiber = OTDR.",
        },
    },
    {
        "id": "netplus-nt-112", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 3, "type": "mcq",
        "stem": "A technician suspects a fiber link's received signal is too weak and wants to "
                "measure the actual received optical power in dBm to compare against the "
                "transceiver's power budget. Which tool should be used?",
        "options": [
            {"id": "A", "text": "An optical power meter (light meter)"},
            {"id": "B", "text": "An OTDR"},
            {"id": "C", "text": "A copper cable certifier"},
            {"id": "D", "text": "A protocol analyzer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An optical power meter reads absolute received power in dBm at a point, which is exactly "
                       "what you compare to the transceiver's receive-sensitivity budget.",
            "distractors": {
                "B": "An OTDR characterizes the fiber and locates events via backscatter; it is not the simple end-to-end dBm power reading.",
                "C": "A copper cable certifier measures twisted-pair parameters and cannot read optical power.",
                "D": "A protocol analyzer decodes captured packets; it has no visibility into optical power levels.",
            },
            "exam_pattern": "Read received optical power in dBm = optical power/light meter; find the fault location = OTDR.",
        },
    },
    {
        "id": "netplus-nt-113", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 1, "type": "mcq",
        "stem": "Users in one area report slow, dropping Wi-Fi, and the technician suspects nearby "
                "access points are using overlapping 2.4 GHz channels. Which tool BEST confirms "
                "channel usage and overlap?",
        "options": [
            {"id": "A", "text": "A Wi-Fi analyzer"},
            {"id": "B", "text": "A tone generator and probe"},
            {"id": "C", "text": "A copper cable tester"},
            {"id": "D", "text": "A loopback plug"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Wi-Fi analyzer shows which channels nearby SSIDs occupy, their signal strength, and "
                       "overlap, letting you pick non-overlapping channels (1, 6, 11 in 2.4 GHz).",
            "distractors": {
                "B": "A tone generator and probe traces physical copper cables, not wireless channels.",
                "C": "A copper cable tester checks wired continuity/wiremap, irrelevant to RF channel overlap.",
                "D": "A loopback plug tests a wired port, not wireless spectrum usage.",
            },
            "exam_pattern": "Channel overlap / interference / signal strength survey = Wi-Fi analyzer.",
        },
    },
    {
        "id": "netplus-nt-114", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "An application intermittently fails, and the team must inspect the actual packets, "
                "TCP handshakes, and retransmissions on the wire to find the cause. Which tool is "
                "MOST appropriate?",
        "options": [
            {"id": "A", "text": "A protocol analyzer / packet capture (e.g., Wireshark or tcpdump)"},
            {"id": "B", "text": "ping"},
            {"id": "C", "text": "ipconfig /all"},
            {"id": "D", "text": "A copper cable certifier"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A protocol analyzer captures and decodes frames so you can inspect the three-way handshake, "
                       "retransmissions, resets, and application payloads to pinpoint the failure.",
            "distractors": {
                "B": "ping only confirms reachability and round-trip time; it does not decode application traffic.",
                "C": "ipconfig /all shows the local IP configuration, not packets on the wire.",
                "D": "A cable certifier validates physical cabling, not protocol-level conversations.",
            },
            "exam_pattern": "Need to see the actual packets / handshake / retransmissions = protocol analyzer (packet capture).",
        },
    },
    {
        "id": "netplus-nt-115", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "mcq",
        "stem": "Traffic to a remote site is slow, and a technician wants per-hop latency AND packet "
                "loss sampled over time to find which hop introduces delay. On Windows, which tool "
                "provides this combined per-hop data?",
        "options": [
            {"id": "A", "text": "pathping"},
            {"id": "B", "text": "nslookup"},
            {"id": "C", "text": "arp -a"},
            {"id": "D", "text": "netstat -r"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "pathping combines the functions of ping and tracert, sending probes over a sampling period "
                       "to report per-hop latency and packet-loss percentages along the path.",
            "distractors": {
                "B": "nslookup queries DNS name resolution; it does not measure per-hop latency or loss.",
                "C": "arp -a displays the local IP-to-MAC cache, not path statistics.",
                "D": "netstat -r prints the local routing table, not live per-hop latency and loss.",
            },
            "exam_pattern": "Per-hop latency + loss over time on Windows = pathping (ping + tracert combined).",
        },
    },
    {
        "id": "netplus-nt-116", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "connectivity_tools", "difficulty": 2, "type": "multi",
        "stem": "A technician needs to view a workstation's current IP address, subnet mask, and "
                "default gateway. Which commands display this LOCAL interface configuration? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "ipconfig /all on Windows"},
            {"id": "B", "text": "ip address (or ifconfig) on Linux"},
            {"id": "C", "text": "nslookup example.com"},
            {"id": "D", "text": "tracert to the default gateway"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "ipconfig /all (Windows) and ip address / ifconfig (Linux/Unix) print the adapter's IP, "
                       "mask, gateway, and DNS settings assigned to the local host.",
            "distractors": {
                "C": "nslookup queries DNS for name resolution; it does not show the local adapter's configuration.",
                "D": "tracert maps the path to a destination; it does not list the local IP/mask/gateway settings.",
            },
            "exam_pattern": "Show local IP config: ipconfig (Windows) and ip/ifconfig (Linux).",
        },
    },

    # ===== 5.0 network_service_issues =======================================
    {
        "id": "netplus-nt-117", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "After an employee plugged a consumer wireless router into a wall jack, some clients "
                "began leasing addresses in an unexpected range with a wrong default gateway and "
                "lost access to corporate resources. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A rogue DHCP server is handing out incorrect leases"},
            {"id": "B", "text": "DNS cache poisoning on the corporate DNS server"},
            {"id": "C", "text": "The clients fell back to APIPA"},
            {"id": "D", "text": "A duplex mismatch on the uplink"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The consumer router runs its own DHCP service; clients that lease from it get the router's "
                       "range and gateway instead of the corporate ones. DHCP snooping prevents rogue servers.",
            "distractors": {
                "B": "DNS poisoning corrupts name-to-IP answers; it does not change a client's leased IP/gateway range.",
                "C": "APIPA (169.254.x.x) only appears when NO DHCP answers; here clients did receive leases, just from the wrong server.",
                "D": "A duplex mismatch causes errors and slowness, not clients leasing addresses from the wrong range.",
            },
            "exam_pattern": "Unauthorized device leasing wrong IP/gateway = rogue DHCP; mitigate with DHCP snooping.",
        },
    },
    {
        "id": "netplus-nt-118", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 3, "type": "mcq",
        "stem": "A host is set to IP 10.1.5.20 with mask 255.255.255.0 and gateway 10.1.4.1. It can "
                "reach other hosts in 10.1.5.0/24 but cannot reach its gateway or any remote "
                "network. What is the cause?",
        "options": [
            {"id": "A", "text": "An incorrect subnet mask - the gateway is outside the host's configured subnet"},
            {"id": "B", "text": "A fully exhausted DHCP scope"},
            {"id": "C", "text": "An expired TLS certificate on the gateway"},
            {"id": "D", "text": "A rogue access point on the LAN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With a /24 mask the host treats only 10.1.5.0-10.1.5.255 as local, so gateway 10.1.4.1 looks "
                       "unreachable and all off-subnet traffic fails. A /23 mask (255.255.254.0) would include the gateway.",
            "distractors": {
                "B": "A statically or correctly leased address still works locally; an exhausted scope would stop new leases, not break routing like this.",
                "C": "A TLS certificate affects HTTPS trust, not IP-layer reachability of a gateway.",
                "D": "A rogue AP is a wireless security concern and does not explain a mask/gateway mismatch.",
            },
            "exam_pattern": "Local works, remote fails, gateway unreachable = wrong subnet mask putting the gateway off-subnet.",
        },
    },
    {
        "id": "netplus-nt-119", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "Two devices on the same LAN intermittently lose connectivity, and one displays an "
                "'IP address conflict' message. A static IP had been configured inside the active "
                "DHCP range. What is the cause?",
        "options": [
            {"id": "A", "text": "A duplicate IP address - the static address overlaps a DHCP-assigned lease"},
            {"id": "B", "text": "APIPA self-assignment"},
            {"id": "C", "text": "An MTU mismatch"},
            {"id": "D", "text": "A missing DNS SPF record"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Assigning a static IP inside the DHCP pool (without an exclusion or reservation) lets DHCP "
                       "hand the same address to another host, producing a duplicate-IP conflict and intermittent loss.",
            "distractors": {
                "B": "APIPA uses 169.254.x.x when no DHCP answers; it does not produce a conflict message between two devices.",
                "C": "An MTU mismatch causes drops of large frames, not an IP-address-conflict notification.",
                "D": "An SPF record is an email anti-spoofing DNS record, unrelated to IP conflicts.",
            },
            "exam_pattern": "Static IP inside the DHCP range = duplicate IP / address conflict; exclude or reserve it.",
        },
    },
    {
        "id": "netplus-nt-120", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "Users cannot reach internal servers by name, but connecting by IP address works. The "
                "technician finds the clients' configured DNS server is an address that was "
                "decommissioned last week. What is the correct fix?",
        "options": [
            {"id": "A", "text": "Point the clients at a valid DNS server (correct the DHCP option 6 or static entry)"},
            {"id": "B", "text": "Replace the Ethernet cabling to the clients"},
            {"id": "C", "text": "Increase the DHCP lease duration"},
            {"id": "D", "text": "Enable jumbo frames on the clients"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Working by IP but failing by name is a name-resolution (DNS) problem. The clients point at a "
                       "dead DNS server, so correct the DNS server address they are given (DHCP option 6 or static).",
            "distractors": {
                "B": "Cabling is fine - IP connectivity works - so re-cabling does not fix name resolution.",
                "C": "Lease duration governs how long an address is held; it does not repair a bad DNS server setting.",
                "D": "Jumbo frames change MTU; they have no effect on DNS name resolution.",
            },
            "exam_pattern": "Works by IP, fails by name = DNS; fix the DNS server the clients are configured to use.",
        },
    },
    {
        "id": "netplus-nt-121", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "network_service_issues", "difficulty": 2, "type": "mcq",
        "stem": "A new internal web app is unreachable on TCP 443 from a branch office, yet the same "
                "clients successfully ping the server by IP, and other internal sites work. What is "
                "the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A firewall or ACL along the path is blocking TCP 443"},
            {"id": "B", "text": "The server NIC is stuck in half-duplex"},
            {"id": "C", "text": "The DHCP scope is exhausted"},
            {"id": "D", "text": "The clients have APIPA addresses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ICMP ping succeeds (reachability and routing are fine) but the specific TCP port fails - the "
                       "classic signature of a firewall rule or ACL blocking that port/service along the path.",
            "distractors": {
                "B": "A duplex problem degrades all traffic with errors; it would not block only TCP 443 while ping works.",
                "C": "An exhausted DHCP scope prevents getting an address; these clients clearly have working IP connectivity.",
                "D": "With APIPA (169.254.x.x) the clients could not ping the server or reach other sites at all.",
            },
            "exam_pattern": "Ping works but a specific port/service fails = blocked port (firewall/ACL).",
        },
    },

    # ===== 5.0 performance_issues ===========================================
    {
        "id": "netplus-nt-122", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 2, "type": "mcq",
        "stem": "Users report choppy, robotic VoIP audio during busy periods, though data apps are "
                "fine. Monitoring shows highly variable packet delay on the voice stream. Which "
                "action BEST addresses this?",
        "options": [
            {"id": "A", "text": "Implement QoS to prioritize voice traffic (and use a jitter buffer)"},
            {"id": "B", "text": "Increase the DHCP lease time"},
            {"id": "C", "text": "Replace the DNS servers"},
            {"id": "D", "text": "Disable Auto-MDIX on the access switches"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Variable delay is jitter, which wrecks real-time voice. QoS prioritizes/queues voice ahead of "
                       "bulk data, and a jitter buffer smooths the variation, restoring clear audio.",
            "distractors": {
                "B": "DHCP lease time governs addressing, not real-time voice delay variation.",
                "C": "DNS resolves names; it does not affect jitter on an established call.",
                "D": "Auto-MDIX concerns cable TX/RX detection and has nothing to do with voice jitter.",
            },
            "exam_pattern": "Choppy VoIP + variable delay = jitter; fix with QoS prioritization and a jitter buffer.",
        },
    },
    {
        "id": "netplus-nt-123", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 2, "type": "mcq",
        "stem": "A switch interface counter shows a rising number of 'giants.' What does this "
                "counter indicate?",
        "options": [
            {"id": "A", "text": "Frames received that are larger than the maximum allowed frame size"},
            {"id": "B", "text": "Frames smaller than 64 bytes"},
            {"id": "C", "text": "The total count of broadcast frames"},
            {"id": "D", "text": "Jumbo frames that were successfully forwarded"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Giants are frames that exceed the maximum allowed size (e.g., beyond the configured MTU), "
                       "often from a faulty NIC/driver or an MTU/jumbo misconfiguration.",
            "distractors": {
                "B": "Frames smaller than 64 bytes are runts, usually from collisions or a bad NIC - the opposite of giants.",
                "C": "Broadcasts are tracked separately and are not what the giants counter measures.",
                "D": "The giants counter flags oversized/error frames, not successfully forwarded jumbo frames.",
            },
            "exam_pattern": "Giants = oversized frames; runts = undersized (<64 byte) frames.",
        },
    },
    {
        "id": "netplus-nt-124", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 1, "type": "mcq",
        "stem": "A WAN link's utilization graph sits at 100% every afternoon, and throughput-sensitive "
                "applications slow for all users during those hours. What does this MOST likely "
                "indicate?",
        "options": [
            {"id": "A", "text": "Bandwidth saturation (congestion) on the link"},
            {"id": "B", "text": "A duplicate IP address"},
            {"id": "C", "text": "A DNS misconfiguration"},
            {"id": "D", "text": "An expired DHCP scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sustained 100% utilization means the link is saturated; queued and dropped packets slow "
                       "everyone. Remedies include more bandwidth or QoS/traffic shaping to protect priority traffic.",
            "distractors": {
                "B": "A duplicate IP affects two specific hosts intermittently, not a time-of-day full-link saturation.",
                "C": "A DNS problem breaks name resolution; it does not peg a link at 100% utilization.",
                "D": "An expired/exhausted DHCP scope blocks new leases; it does not drive link utilization to 100%.",
            },
            "exam_pattern": "Link pinned at 100% utilization + slowness for all = bandwidth saturation/congestion.",
        },
    },
    {
        "id": "netplus-nt-125", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 3, "type": "mcq",
        "stem": "After jumbo frames (MTU 9000) were enabled on some servers and storage but an "
                "intermediate switch was left at 1500, large transfers fail or perform terribly "
                "while small pings succeed. What is the cause?",
        "options": [
            {"id": "A", "text": "An MTU (jumbo-frame) mismatch along the path"},
            {"id": "B", "text": "A duplex mismatch on the uplink"},
            {"id": "C", "text": "A rogue DHCP server"},
            {"id": "D", "text": "A dirty fiber connector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Jumbo frames must be enabled end-to-end. A device left at 1500 drops the oversized frames (or "
                       "forces fragmentation), so small packets pass but large transfers fail. Match MTU across the whole path.",
            "distractors": {
                "B": "A duplex mismatch produces collisions/CRC errors on all traffic, not a clean small-works/large-fails pattern.",
                "C": "A rogue DHCP server affects addressing, not frame-size handling of large transfers.",
                "D": "A dirty fiber connector raises optical loss for all traffic, not selectively for large frames.",
            },
            "exam_pattern": "Small packets fine, large fail across a path = MTU/jumbo-frame mismatch; set MTU consistently end-to-end.",
        },
    },
    {
        "id": "netplus-nt-126", "exam": "netplus", "domain": "network_troubleshooting",
        "subtopic": "performance_issues", "difficulty": 2, "type": "mcq",
        "stem": "A core router becomes sluggish, drops packets, and responds slowly to management "
                "sessions. Monitoring shows its CPU pegged near 100% during a traffic spike. Which "
                "performance issue is this?",
        "options": [
            {"id": "A", "text": "High device resource utilization (CPU/memory)"},
            {"id": "B", "text": "Attenuation on the uplink cable"},
            {"id": "C", "text": "An incorrect subnet mask on the clients"},
            {"id": "D", "text": "A split-pair wiring fault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When a device's CPU or memory is exhausted it cannot process or forward traffic promptly, so "
                       "it drops packets and responds slowly regardless of link health. Investigate the process/traffic, then offload or upgrade.",
            "distractors": {
                "B": "Attenuation is a cabling/signal-loss issue on one link; it would not peg the router's CPU.",
                "C": "An incorrect subnet mask breaks specific hosts' routing, not the router's CPU utilization.",
                "D": "A split-pair fault causes crosstalk on a cable run, not device-wide CPU exhaustion.",
            },
            "exam_pattern": "Device slow + drops + CPU/memory near 100% = resource exhaustion on the device itself.",
        },
    },
]
