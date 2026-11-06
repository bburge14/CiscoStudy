"""CompTIA A+ Core 1 (220-1101) item pool — original, objective-aligned questions.

Same authoring rules as the Cisco and Security+ pools: original scenario-based
content mapped to the public 220-1101 exam objectives, never real exam items.
build_content.py shuffles option order (seeded by id), so the answer key here is
not positionally biased; each wrong option carries its own distractor note.
"""

QUESTIONS = [
    # ===== 1.0 Mobile Devices ================================================
    {
        "id": "aplus1-mob-001", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A technician is upgrading the system memory in a laptop. Which RAM "
                "form factor is designed for the laptop's smaller footprint?",
        "options": [
            {"id": "A", "text": "SO-DIMM"},
            {"id": "B", "text": "DIMM"},
            {"id": "C", "text": "DIP"},
            {"id": "D", "text": "SIMM"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SO-DIMM (Small Outline DIMM) is the short, compact memory module built "
                       "for the limited space inside laptops and small-form-factor PCs.",
            "distractors": {
                "B": "A full-size DIMM is the longer desktop/server module; it won't fit a laptop slot.",
                "C": "DIP is an individual chip package soldered to a board, not a user-replaceable module.",
                "D": "SIMM is a legacy 30/72-pin module from the 1990s, long replaced by DIMM/SO-DIMM.",
            },
            "exam_pattern": "Laptop RAM = SO-DIMM; desktop/server RAM = full-size DIMM.",
        },
    },
    {
        "id": "aplus1-mob-002", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "A laptop panel is advertised as low cost with very fast response times, but "
                "reviewers note washed-out colors and poor viewing angles. Which panel "
                "technology is it MOST likely using?",
        "options": [
            {"id": "A", "text": "TN (twisted nematic)"},
            {"id": "B", "text": "IPS (in-plane switching)"},
            {"id": "C", "text": "OLED"},
            {"id": "D", "text": "VA (vertical alignment)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TN panels are the cheapest and fastest LCDs, but they have narrow viewing "
                       "angles and weaker color reproduction — exactly the described trade-off.",
            "distractors": {
                "B": "IPS is known for wide viewing angles and accurate color, the opposite of this panel.",
                "C": "OLED lights each pixel individually, giving true blacks and excellent color/angles.",
                "D": "VA sits between TN and IPS, offering high contrast rather than washed-out color.",
            },
            "exam_pattern": "TN = cheap + fast + poor angles; IPS = best color/angles; OLED = per-pixel, true black.",
        },
    },
    {
        "id": "aplus1-mob-003", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 1, "type": "mcq",
        "stem": "A laptop has a single small, reversible port that can transfer data, charge the "
                "system, and output video using DisplayPort Alternate Mode. Which connector is this?",
        "options": [
            {"id": "A", "text": "USB-C"},
            {"id": "B", "text": "Micro-USB"},
            {"id": "C", "text": "Lightning"},
            {"id": "D", "text": "Mini-USB"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "USB-C is reversible and carries USB data, USB Power Delivery charging, and video "
                       "via DisplayPort Alt Mode — one connector for all three.",
            "distractors": {
                "B": "Micro-USB is an older, non-reversible connector used mainly for charging/data, not video.",
                "C": "Lightning is Apple's proprietary reversible connector; it is not the DisplayPort Alt Mode standard.",
                "D": "Mini-USB is a legacy non-reversible connector for data/charging on older peripherals.",
            },
            "exam_pattern": "USB-C = reversible, does data + Power Delivery + DisplayPort Alt Mode video.",
        },
    },
    {
        "id": "aplus1-mob-004", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A user taps their smartphone against a store's payment terminal to pay. Which "
                "short-range wireless technology enables this contactless transaction?",
        "options": [
            {"id": "A", "text": "NFC"},
            {"id": "B", "text": "Bluetooth"},
            {"id": "C", "text": "Infrared (IR)"},
            {"id": "D", "text": "Wi-Fi Direct"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NFC (Near Field Communication) works only at a few centimeters, which is what makes "
                       "tap-to-pay and tap-to-pair secure and intentional.",
            "distractors": {
                "B": "Bluetooth reaches roughly 10 m and is used for audio/peripherals, not tap-to-pay.",
                "C": "Infrared needs direct line of sight and is essentially obsolete on modern phones.",
                "D": "Wi-Fi Direct links two devices for networking/file transfer, not contactless payment.",
            },
            "exam_pattern": "Tap-to-pay at ~4 cm = NFC; peripherals/audio at ~10 m = Bluetooth.",
        },
    },
    {
        "id": "aplus1-mob-005", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants corporate email, contacts, and calendar to synchronize "
                "two-way and wirelessly between the mail server and employees' phones. Which "
                "protocol is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Microsoft Exchange ActiveSync"},
            {"id": "B", "text": "POP3"},
            {"id": "C", "text": "SMTP"},
            {"id": "D", "text": "FTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Exchange ActiveSync (EAS) pushes and two-way syncs mail, contacts, and calendar "
                       "to mobile devices, which is exactly what corporate mobile mail needs.",
            "distractors": {
                "B": "POP3 only downloads mail to one device (often deleting it from the server) and syncs no calendar/contacts.",
                "C": "SMTP only sends/relays outbound mail; it does not sync mailboxes, contacts, or calendars.",
                "D": "FTP transfers files between hosts and has nothing to do with mail synchronization.",
            },
            "exam_pattern": "Two-way push of mail + contacts + calendar to mobile = Exchange ActiveSync; POP3 = download mail only.",
        },
    },
    {
        "id": "aplus1-mob-006", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 3, "type": "mcq",
        "stem": "After a technician replaces a laptop's LCD panel, Wi-Fi reception becomes very weak "
                "even though it was strong before the repair. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The Wi-Fi antenna leads that route through the display lid were not reconnected to the wireless card"},
            {"id": "B", "text": "The SSD was reseated in the wrong M.2 slot"},
            {"id": "C", "text": "The system RAM is beginning to fail"},
            {"id": "D", "text": "The CPU is overheating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Laptop Wi-Fi antennas sit in the display bezel/lid, with thin leads routed through the "
                       "hinge to the wireless NIC. Leaving them unplugged after a screen swap cripples reception.",
            "distractors": {
                "B": "A misplaced SSD would cause boot/storage problems, not specifically weak Wi-Fi.",
                "C": "Failing RAM causes crashes or no-POST symptoms, not a drop in wireless signal strength.",
                "D": "An overheating CPU causes throttling or shutdowns, not a selective loss of Wi-Fi range.",
            },
            "exam_pattern": "Weak Wi-Fi right after a screen/lid repair → reconnect the antenna leads routed through the display.",
        },
    },

    # ===== 2.0 Networking ====================================================
    {
        "id": "aplus1-net-001", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 1, "type": "mcq",
        "stem": "A web administrator is writing a firewall rule to permit secure (encrypted) web "
                "traffic. Which TCP port must the rule allow?",
        "options": [
            {"id": "A", "text": "443"},
            {"id": "B", "text": "80"},
            {"id": "C", "text": "22"},
            {"id": "D", "text": "3389"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "HTTPS (HTTP over TLS) uses TCP port 443 for encrypted web traffic.",
            "distractors": {
                "B": "TCP 80 is plain HTTP — unencrypted web traffic, not the secure version.",
                "C": "TCP 22 is SSH, used for secure remote command-line access, not web browsing.",
                "D": "TCP 3389 is RDP, used for remote desktop sessions, not web traffic.",
            },
            "exam_pattern": "HTTPS = 443, HTTP = 80, SSH = 22, RDP = 3389.",
        },
    },
    {
        "id": "aplus1-net-002", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A small office needs a device that connects its internal LAN to the ISP and forwards "
                "traffic between the LAN and the internet based on IP addresses. Which device does this?",
        "options": [
            {"id": "A", "text": "Router"},
            {"id": "B", "text": "Unmanaged switch"},
            {"id": "C", "text": "Hub"},
            {"id": "D", "text": "Media converter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A router operates at Layer 3 and forwards packets between different networks "
                       "(LAN ↔ internet) using IP addressing.",
            "distractors": {
                "B": "A switch forwards frames within a single LAN using MAC addresses; it doesn't route between networks.",
                "C": "A hub is a Layer 1 repeater that blindly copies signals to all ports; it makes no forwarding decisions.",
                "D": "A media converter only changes the physical medium (e.g., copper to fiber); it does not route.",
            },
            "exam_pattern": "Between networks by IP = router (L3); within a LAN by MAC = switch (L2).",
        },
    },
    {
        "id": "aplus1-net-003", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "A user in a far bedroom gets a weak signal on the 5 GHz band. Moving the connection "
                "to which band will generally improve range and wall penetration, at the cost of speed?",
        "options": [
            {"id": "A", "text": "2.4 GHz"},
            {"id": "B", "text": "6 GHz"},
            {"id": "C", "text": "60 GHz"},
            {"id": "D", "text": "900 MHz cordless-phone band"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "2.4 GHz uses longer wavelengths that travel farther and pass through walls better than "
                       "5 GHz, though it is slower and more congested.",
            "distractors": {
                "B": "6 GHz (Wi-Fi 6E) offers more bandwidth but has even shorter range and weaker penetration than 5 GHz.",
                "C": "60 GHz (WiGig/802.11ad) is extremely high speed but only works across a room with line of sight.",
                "D": "The 900 MHz band is used by some cordless phones/IoT, not by standard client Wi-Fi.",
            },
            "exam_pattern": "2.4 GHz = farther + slower + crowded; 5/6 GHz = faster + shorter range.",
        },
    },
    {
        "id": "aplus1-net-004", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 2, "type": "mcq",
        "stem": "A workstation can reach websites when the user types their IP address directly, but "
                "not when the user types the domain name. Which network service is MOST likely at fault?",
        "options": [
            {"id": "A", "text": "DNS"},
            {"id": "B", "text": "DHCP"},
            {"id": "C", "text": "NTP"},
            {"id": "D", "text": "SMTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DNS resolves domain names to IP addresses. If it fails, raw IP access still works while "
                       "name-based access breaks — exactly the symptom described.",
            "distractors": {
                "B": "DHCP assigns IP configuration; the host clearly already has working IP connectivity.",
                "C": "NTP synchronizes clocks; it has no role in reaching websites.",
                "D": "SMTP sends email; it is unrelated to resolving or reaching web addresses.",
            },
            "exam_pattern": "Reachable by IP but not by name → DNS problem.",
        },
    },
    {
        "id": "aplus1-net-005", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "A residential ISP delivers internet over the same coaxial line used for cable TV, using "
                "the DOCSIS standard and a cable modem. Which internet connection type is this?",
        "options": [
            {"id": "A", "text": "Cable"},
            {"id": "B", "text": "DSL"},
            {"id": "C", "text": "Fiber to the home"},
            {"id": "D", "text": "Satellite"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cable internet runs over coaxial TV cabling and uses the DOCSIS standard through a cable modem.",
            "distractors": {
                "B": "DSL delivers internet over existing twisted-pair telephone lines, not coax.",
                "C": "Fiber to the home uses optical glass strands and an ONT, not coax/DOCSIS.",
                "D": "Satellite uses a dish for a wireless uplink to an orbiting satellite, with high latency.",
            },
            "exam_pattern": "Coax + DOCSIS + cable modem = cable internet; phone line = DSL; glass = fiber.",
        },
    },
    {
        "id": "aplus1-net-006", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 2, "type": "multi",
        "stem": "A technician is documenting default port-to-protocol mappings on a SOHO firewall. "
                "Which TWO pairings are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "TCP 3389 = RDP"},
            {"id": "B", "text": "UDP 53 = DNS"},
            {"id": "C", "text": "TCP 25 = DNS"},
            {"id": "D", "text": "TCP 23 = HTTPS"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "RDP uses TCP 3389 and DNS uses UDP (and TCP) 53 — both pairings are correct.",
            "distractors": {
                "C": "TCP 25 is SMTP (outbound mail), not DNS. DNS is port 53.",
                "D": "TCP 23 is Telnet (unencrypted remote CLI), not HTTPS. HTTPS is TCP 443.",
            },
            "exam_pattern": "RDP 3389, DNS 53, SMTP 25, Telnet 23, HTTPS 443.",
        },
    },

    # ===== 3.0 Hardware ======================================================
    {
        "id": "aplus1-hw-001", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 1, "type": "mcq",
        "stem": "A technician is terminating a Cat 6 cable to connect a desktop to a Gigabit Ethernet "
                "wall jack. Which connector belongs on the cable end?",
        "options": [
            {"id": "A", "text": "RJ45"},
            {"id": "B", "text": "RJ11"},
            {"id": "C", "text": "BNC"},
            {"id": "D", "text": "LC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RJ45 is the 8-position (8P8C) modular connector used for twisted-pair Ethernet such as Cat 5e/6.",
            "distractors": {
                "B": "RJ11 is the smaller 6-position connector used for analog telephone lines.",
                "C": "BNC is a bayonet-style connector for coaxial cable (legacy 10BASE2 / video).",
                "D": "LC is a small form-factor fiber-optic connector, used with glass cabling, not copper Ethernet.",
            },
            "exam_pattern": "Twisted-pair Ethernet = RJ45 (8P8C); telephone = RJ11; fiber = LC/SC.",
        },
    },
    {
        "id": "aplus1-hw-002", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 2, "type": "mcq",
        "stem": "A server administrator specifies ECC memory for a new database server. What is the "
                "PRIMARY benefit of ECC RAM?",
        "options": [
            {"id": "A", "text": "It detects and corrects single-bit memory errors to protect data integrity"},
            {"id": "B", "text": "It always runs at a much higher clock speed than non-ECC RAM"},
            {"id": "C", "text": "It eliminates the need for a page file / virtual memory"},
            {"id": "D", "text": "It lets the CPU be overclocked safely"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ECC (Error-Correcting Code) RAM adds parity bits that detect and correct single-bit errors, "
                       "which matters most on servers where silent data corruption is unacceptable.",
            "distractors": {
                "B": "ECC is about reliability, not speed; it often runs slightly slower than comparable non-ECC RAM.",
                "C": "A page file is an OS feature; ECC does not remove the need for virtual memory.",
                "D": "ECC has nothing to do with CPU overclocking headroom.",
            },
            "exam_pattern": "ECC = error detection/correction for servers; it is a reliability feature, not a speed feature.",
        },
    },
    {
        "id": "aplus1-hw-003", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "mcq",
        "stem": "A user wants the fastest possible boot and application drive. Which option delivers the "
                "HIGHEST sequential throughput?",
        "options": [
            {"id": "A", "text": "An M.2 NVMe SSD connected over the PCIe bus"},
            {"id": "B", "text": "A 2.5-inch SATA SSD"},
            {"id": "C", "text": "A 7,200 RPM SATA hard drive"},
            {"id": "D", "text": "A 5,400 RPM SATA hard drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NVMe SSDs communicate over the high-bandwidth PCIe bus, far exceeding SATA's limits and "
                       "crushing any mechanical drive on throughput and latency.",
            "distractors": {
                "B": "A SATA SSD is fast but capped by the SATA III interface at about 6 Gb/s (~550 MB/s).",
                "C": "A 7,200 RPM HDD has spinning platters and heads; it is far slower than any SSD.",
                "D": "A 5,400 RPM HDD is slower still, common in budget laptops and external drives.",
            },
            "exam_pattern": "Speed order: NVMe (PCIe/M.2) > SATA SSD > HDD; SATA III caps near 6 Gb/s.",
        },
    },
    {
        "id": "aplus1-hw-004", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "mcq",
        "stem": "A customer is building a compact home-theater PC and wants the SMALLEST of the standard "
                "ATX-family motherboard form factors. Which should they choose?",
        "options": [
            {"id": "A", "text": "Mini-ITX"},
            {"id": "B", "text": "MicroATX"},
            {"id": "C", "text": "ATX"},
            {"id": "D", "text": "Extended ATX (E-ATX)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mini-ITX (170 x 170 mm) is the smallest common form factor, typically with a single "
                       "expansion slot — ideal for a small HTPC build.",
            "distractors": {
                "B": "MicroATX is larger than Mini-ITX, with more expansion slots.",
                "C": "Full ATX is the standard desktop size, larger than MicroATX.",
                "D": "E-ATX is the largest, used for high-end workstation and server boards.",
            },
            "exam_pattern": "Size small → large: Mini-ITX < MicroATX < ATX < E-ATX.",
        },
    },
    {
        "id": "aplus1-hw-005", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 2, "type": "mcq",
        "stem": "A technician reads '80 PLUS Gold' on a power supply's label. What does this rating "
                "describe?",
        "options": [
            {"id": "A", "text": "The PSU's energy efficiency — how much drawn AC power is delivered as usable DC"},
            {"id": "B", "text": "The maximum wattage the PSU can supply"},
            {"id": "C", "text": "The number of SATA power connectors included"},
            {"id": "D", "text": "The physical dimensions of the PSU"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "80 PLUS tiers (White, Bronze, Silver, Gold, Platinum, Titanium) rate efficiency — the "
                       "percentage of AC input converted to DC output rather than wasted as heat.",
            "distractors": {
                "B": "Maximum wattage is a separate spec printed elsewhere on the label (e.g., 650 W).",
                "C": "Connector count is a separate detail and is not what the 80 PLUS badge measures.",
                "D": "Physical size (e.g., ATX vs SFX) is unrelated to the efficiency certification.",
            },
            "exam_pattern": "80 PLUS = efficiency tier; wattage is a separate rating entirely.",
        },
    },
    {
        "id": "aplus1-hw-006", "exam": "aplus1", "domain": "hardware",
        "subtopic": "printers", "difficulty": 3, "type": "mcq",
        "stem": "In the laser printer imaging process, which step comes IMMEDIATELY AFTER exposing, "
                "the stage where the laser writes the latent image onto the photosensitive drum?",
        "options": [
            {"id": "A", "text": "Developing"},
            {"id": "B", "text": "Charging"},
            {"id": "C", "text": "Fusing"},
            {"id": "D", "text": "Cleaning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The sequence is processing, charging, exposing, developing, transferring, fusing, cleaning. "
                       "After exposing writes the latent image, developing coats that image with toner.",
            "distractors": {
                "B": "Charging applies a uniform charge to the drum and happens BEFORE exposing, not after.",
                "C": "Fusing bonds toner to the paper with heat and pressure near the END of the process.",
                "D": "Cleaning wipes residual toner and charge from the drum as the final step.",
            },
            "exam_pattern": "Laser 7 steps: Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning.",
        },
    },
    {
        "id": "aplus1-hw-007", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 1, "type": "mcq",
        "stem": "An administrator wants to control three rack servers from a single keyboard, monitor, and "
                "mouse, switching between them with the press of a button. Which device provides this?",
        "options": [
            {"id": "A", "text": "KVM switch"},
            {"id": "B", "text": "USB hub"},
            {"id": "C", "text": "Docking station"},
            {"id": "D", "text": "Network switch"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A KVM (Keyboard, Video, Mouse) switch shares one set of peripherals across multiple "
                       "computers, toggling control between them.",
            "distractors": {
                "B": "A USB hub only adds extra USB ports to one computer; it doesn't switch between machines.",
                "C": "A docking station expands a single laptop's connectivity, not control of several servers.",
                "D": "A network switch connects devices on a LAN; it has nothing to do with sharing peripherals.",
            },
            "exam_pattern": "One keyboard/monitor/mouse controlling many PCs = KVM switch.",
        },
    },
    {
        "id": "aplus1-hw-008", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "multi",
        "stem": "A technician must pick a RAID level for a server that has to keep running if a single "
                "drive fails. Which TWO of the following RAID levels provide fault tolerance? (Choose two.)",
        "options": [
            {"id": "A", "text": "RAID 1 (mirroring)"},
            {"id": "B", "text": "RAID 5 (striping with distributed parity)"},
            {"id": "C", "text": "RAID 0 (striping)"},
            {"id": "D", "text": "JBOD (just a bunch of disks)"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "RAID 1 mirrors identical copies across drives, and RAID 5 stripes data with distributed "
                       "parity; both can survive the loss of a single drive.",
            "distractors": {
                "C": "RAID 0 stripes for speed/capacity with NO redundancy — losing any one drive loses the whole array.",
                "D": "JBOD simply concatenates disks with no parity or mirroring, so it offers no fault tolerance.",
            },
            "exam_pattern": "Fault tolerant: RAID 1 (mirror), 5 (parity), 10 (mirror+stripe). RAID 0 = speed only, NO redundancy.",
        },
    },

    # ===== 4.0 Virtualization & Cloud Computing ==============================
    {
        "id": "aplus1-virt-001", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 1, "type": "mcq",
        "stem": "A company uses a web-based office suite where the provider manages the servers, operating "
                "system, and the applications, and users just sign in through a browser. Which cloud "
                "service model is this?",
        "options": [
            {"id": "A", "text": "SaaS (Software as a Service)"},
            {"id": "B", "text": "PaaS (Platform as a Service)"},
            {"id": "C", "text": "IaaS (Infrastructure as a Service)"},
            {"id": "D", "text": "On-premises private datacenter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SaaS delivers finished applications over the web (webmail, online office suites); the provider "
                       "runs and maintains every layer beneath the app.",
            "distractors": {
                "B": "PaaS provides a development platform (runtime, OS, tools) for building apps, not a finished app.",
                "C": "IaaS provides raw compute, storage, and networking (VMs) that the customer configures and manages.",
                "D": "An on-premises datacenter is not a cloud service model at all.",
            },
            "exam_pattern": "SaaS = finished app; PaaS = dev platform; IaaS = raw VMs/infrastructure.",
        },
    },
    {
        "id": "aplus1-virt-002", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "An organization keeps sensitive records on its own private cloud but 'bursts' to a public "
                "cloud provider during peak demand. Which cloud DEPLOYMENT model is this?",
        "options": [
            {"id": "A", "text": "Hybrid cloud"},
            {"id": "B", "text": "Public cloud"},
            {"id": "C", "text": "Private cloud"},
            {"id": "D", "text": "Community cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hybrid cloud combines private and public clouds so workloads can move between them — "
                       "cloud bursting to public capacity at peak is a textbook example.",
            "distractors": {
                "B": "A public cloud alone is fully provider-owned and shared; it isn't the mix described.",
                "C": "A private cloud alone is dedicated to one organization with no public component.",
                "D": "A community cloud is shared by several organizations with common requirements, not this scenario.",
            },
            "exam_pattern": "Private + public working together = hybrid; shared by several orgs = community.",
        },
    },
    {
        "id": "aplus1-virt-003", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "A retailer's cloud platform automatically scales server capacity UP during a holiday spike "
                "and back DOWN afterward, appearing to offer unlimited resources on demand. Which essential "
                "cloud characteristic BEST describes this?",
        "options": [
            {"id": "A", "text": "Rapid elasticity"},
            {"id": "B", "text": "Measured service"},
            {"id": "C", "text": "Resource pooling"},
            {"id": "D", "text": "Broad network access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Rapid elasticity is the ability to scale resources out and back in quickly — often "
                       "automatically — to match changing demand.",
            "distractors": {
                "B": "Measured service is the metered, pay-per-use billing of what you consume, not the scaling itself.",
                "C": "Resource pooling is the provider serving many tenants from a shared pool of hardware.",
                "D": "Broad network access means the service is reachable over standard networks and devices.",
            },
            "exam_pattern": "Scale up/down on demand = rapid elasticity; metered pay-per-use = measured service.",
        },
    },
    {
        "id": "aplus1-virt-004", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A developer installs VirtualBox on top of their existing Windows 11 desktop to run several "
                "test virtual machines. Which TYPE of hypervisor is this?",
        "options": [
            {"id": "A", "text": "Type 2 (hosted) hypervisor"},
            {"id": "B", "text": "Type 1 (bare-metal) hypervisor"},
            {"id": "C", "text": "A container engine"},
            {"id": "D", "text": "A cross-architecture emulator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Type 2 (hosted) hypervisor runs as an application ON TOP of an existing host OS — "
                       "VirtualBox and VMware Workstation on Windows are classic examples.",
            "distractors": {
                "B": "A Type 1 (bare-metal) hypervisor installs directly on the hardware with no host OS (e.g., ESXi, Hyper-V).",
                "C": "A container engine shares the host kernel to run isolated apps, not full virtual machines.",
                "D": "An emulator translates a different CPU architecture; a hosted hypervisor runs same-architecture VMs natively.",
            },
            "exam_pattern": "Type 2 = runs on a host OS (VirtualBox); Type 1 = bare metal on the hardware (ESXi).",
        },
    },
    {
        "id": "aplus1-virt-005", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 1, "type": "mcq",
        "stem": "A technician plans to run four virtual machines at the same time on one workstation for "
                "testing. Which hardware resource is MOST important to have in sufficient quantity?",
        "options": [
            {"id": "A", "text": "System RAM to allocate to each VM"},
            {"id": "B", "text": "A higher-resolution display adapter"},
            {"id": "C", "text": "A faster optical (DVD) drive"},
            {"id": "D", "text": "Extra front-panel USB ports"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Every running VM is assigned its own memory (along with CPU cores and disk), so ample system "
                       "RAM is the key resource that limits how many VMs can run at once.",
            "distractors": {
                "B": "Display resolution affects what you see, not how many VMs the host can keep in memory.",
                "C": "Optical-drive speed is irrelevant to running VMs, which boot from virtual disks.",
                "D": "USB port count does not determine VM capacity.",
            },
            "exam_pattern": "More simultaneous VMs → more RAM and CPU cores (plus virtualization enabled in BIOS/UEFI).",
        },
    },

    # ===== 5.0 Hardware & Network Troubleshooting ============================
    {
        "id": "aplus1-ts-001", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "mcq",
        "stem": "A technician has just tested and CONFIRMED a theory about why a PC won't boot. According "
                "to the CompTIA six-step troubleshooting methodology, what is the NEXT step?",
        "options": [
            {"id": "A", "text": "Establish a plan of action to resolve the problem and implement the solution"},
            {"id": "B", "text": "Identify the problem"},
            {"id": "C", "text": "Document the findings, actions, and outcomes"},
            {"id": "D", "text": "Establish a theory of probable cause"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Once the theory is tested and confirmed (step 3), step 4 is to establish a plan of action "
                       "and implement the fix.",
            "distractors": {
                "B": "Identifying the problem is step 1 and has already happened.",
                "C": "Documenting findings/actions/outcomes is the final step (step 6), after verification.",
                "D": "Establishing a theory is step 2, which precedes testing the theory.",
            },
            "exam_pattern": "6 steps: Identify → Theory → Test theory → Plan & implement → Verify (+prevent) → Document.",
        },
    },
    {
        "id": "aplus1-ts-002", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A desktop powers on — fans spin and lights come on — but there is no video output and the "
                "motherboard emits a repeating POST beep code. Which component should the technician suspect FIRST?",
        "options": [
            {"id": "A", "text": "Memory (RAM) that has failed or is not seated correctly"},
            {"id": "B", "text": "A failed hard drive"},
            {"id": "C", "text": "A disconnected network cable"},
            {"id": "D", "text": "A weak CMOS battery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Power present but no video plus POST beep codes classically points to RAM (failed or unseated) "
                       "or the GPU; reseating/testing memory is the quick, cheap first move.",
            "distractors": {
                "B": "A bad hard drive still lets the system POST and show video — you'd see a 'no boot device' message instead.",
                "C": "A network cable has no effect on whether the system POSTs or produces video.",
                "D": "A weak CMOS battery typically just resets the clock/BIOS settings; it doesn't cause a no-video POST beep pattern.",
            },
            "exam_pattern": "Fans on, no video, beeping = POST failure → suspect RAM/GPU first; drive faults still POST.",
        },
    },
    {
        "id": "aplus1-ts-003", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A laptop screen is extremely dim, but you can faintly make out the desktop when you shine a "
                "flashlight at an angle on it. An external monitor works fine. What is the MOST likely faulty part?",
        "options": [
            {"id": "A", "text": "The display backlight (or its inverter on older CCFL panels)"},
            {"id": "B", "text": "The graphics driver"},
            {"id": "C", "text": "The system RAM"},
            {"id": "D", "text": "The hard drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A faint image visible under a flashlight means the LCD is still rendering but not lit — the "
                       "backlight (or the inverter that powers a CCFL backlight) has failed.",
            "distractors": {
                "B": "A driver fault usually produces artifacts, wrong resolution, or no image — not a dim-but-present picture.",
                "C": "RAM has no role in screen brightness; failing RAM causes crashes or no-POST symptoms.",
                "D": "The hard drive stores data and does not control the display backlight.",
            },
            "exam_pattern": "Image faintly visible with a flashlight = backlight/inverter failure, not the GPU/driver.",
        },
    },
    {
        "id": "aplus1-ts-004", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 3, "type": "mcq",
        "stem": "A Windows workstation that normally receives its address automatically now shows an IP of "
                "169.254.12.44 and cannot reach any other host. What does this MOST likely indicate?",
        "options": [
            {"id": "A", "text": "The client could not reach a DHCP server and self-assigned an APIPA address"},
            {"id": "B", "text": "The workstation obtained a valid public IP address"},
            {"id": "C", "text": "DNS is misconfigured but DHCP is working normally"},
            {"id": "D", "text": "The default gateway intentionally hands out 169.254 addresses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A 169.254.x.x address is APIPA (Automatic Private IP Addressing), which Windows self-assigns "
                       "ONLY when no DHCP server answers — so the host can't communicate beyond its local link.",
            "distractors": {
                "B": "169.254.x.x is a link-local private range, not a routable public address.",
                "C": "The symptom is a failed address assignment (DHCP), not name resolution (DNS).",
                "D": "Gateways/DHCP servers hand out usable addresses; the 169.254 range is a fallback, not a design choice.",
            },
            "exam_pattern": "169.254.x.x = APIPA → DHCP unreachable/failed; it's a self-assigned link-local address.",
        },
    },
    {
        "id": "aplus1-ts-005", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Pages from a laser printer come out with toner that smudges and rubs off the paper easily. "
                "Which component is MOST likely failing?",
        "options": [
            {"id": "A", "text": "The fuser assembly"},
            {"id": "B", "text": "The paper tray"},
            {"id": "C", "text": "The network interface"},
            {"id": "D", "text": "The scanner glass"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The fuser uses heat and pressure to bond toner permanently to the page. If it fails or can't "
                       "reach temperature, toner sits loose on the paper and smears.",
            "distractors": {
                "B": "The paper tray only feeds paper; it doesn't affect whether toner is bonded.",
                "C": "The network interface affects connectivity, not print quality or toner fusing.",
                "D": "The scanner glass only affects copy/scan quality, not printed toner adhesion.",
            },
            "exam_pattern": "Laser toner that smears/rubs off = fuser not bonding toner (the heat-and-pressure stage).",
        },
    },
    {
        "id": "aplus1-ts-006", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A desktop runs fine when idle but shuts itself off abruptly during intensive gaming. The "
                "interior is caked with dust. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The system is overheating and triggering a thermal shutdown"},
            {"id": "B", "text": "The DNS server is unreachable"},
            {"id": "C", "text": "The monitor cable is loose"},
            {"id": "D", "text": "The keyboard driver is corrupt"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Abrupt shutdowns only under heavy load, combined with dust blocking airflow, point to "
                       "overheating — the system powers off to protect the CPU/components.",
            "distractors": {
                "B": "An unreachable DNS server breaks name resolution; it never powers the machine off.",
                "C": "A loose monitor cable causes no display or flicker, not a full system shutdown.",
                "D": "A corrupt keyboard driver affects input only; it cannot shut the computer down under load.",
            },
            "exam_pattern": "Random shutdowns under load + dust/blocked airflow = overheating / thermal protection.",
        },
    },
]
