"""CompTIA A+ Core 1 (220-1101) round-2 expansion item pool.

Original, objective-aligned questions that deepen every 220-1101 domain to match
the CCNA bank's depth (~205 items). Same authoring rules as the Cisco, Security+,
Network+ and existing A+ pools: original scenario-based content mapped to the
public 220-1101 exam objectives, never real exam items. build_content.py shuffles
option order (seeded by id), so the answer key here is not positionally biased;
each wrong option carries its own distractor note.

Coverage deepens all five Core 1 domains: Mobile Devices, Networking, Hardware,
Virtualization & Cloud, and Hardware & Network Troubleshooting. IDs carry an
`-r2-` infix (aplus1-<mob|net|hw|virt|ts>-r2-0xx) so they never collide with the
existing aplus1-*-0xx / aplus1-*-1xx items.
"""

QUESTIONS = [
    # ===== 1.0 Mobile Devices ===============================================
    # ----- laptop_hardware --------------------------------------------------
    {
        "id": "aplus1-mob-r2-001", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 1, "type": "mcq",
        "stem": "A presenter connects their laptop to a conference-room projector, but the "
                "laptop screen stays on while the projector shows nothing. Which laptop "
                "keyboard action toggles output to the external display?",
        "options": [
            {"id": "A", "text": "Press the Fn key together with the display-toggle function key (often a monitor icon)"},
            {"id": "B", "text": "Press the Num Lock key"},
            {"id": "C", "text": "Press Caps Lock twice"},
            {"id": "D", "text": "Press the Fn key with the volume-up key"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Laptops map screen/projector switching to a special function key reached "
                       "by holding Fn; it cycles laptop-only / duplicate / extend / projector-only.",
            "distractors": {
                "B": "Num Lock toggles the embedded numeric keypad; it has nothing to do with video output.",
                "C": "Caps Lock changes letter case only.",
                "D": "That Fn combo adjusts audio volume, not the display output.",
            },
            "exam_pattern": "Fn + the key with a display icon = toggle/extend to an external screen. "
                            "Other Fn keys handle brightness, volume, wireless, keyboard backlight.",
        },
    },
    {
        "id": "aplus1-mob-r2-002", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 2, "type": "mcq",
        "stem": "Before quoting a memory upgrade, a technician finds the ultrabook's RAM chips "
                "are soldered directly to the system board with no SO-DIMM slots. What does "
                "this mean for the upgrade?",
        "options": [
            {"id": "A", "text": "The memory cannot be upgraded; the needed capacity must be chosen at purchase"},
            {"id": "B", "text": "A standard SO-DIMM can still be added in a hidden slot"},
            {"id": "C", "text": "The RAM can be pried off and replaced with a desktop DIMM"},
            {"id": "D", "text": "The RAM will auto-expand using the SSD as more physical memory"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Many thin laptops use soldered (non-upgradeable) memory, so capacity is "
                       "fixed; plan for it when specifying the machine.",
            "distractors": {
                "B": "There are no SO-DIMM slots on a soldered-memory board.",
                "C": "Soldered BGA chips are not user-replaceable like a DIMM.",
                "D": "The pagefile/swap uses the SSD, but that is virtual memory, not added physical RAM.",
            },
            "exam_pattern": "Soldered RAM = fixed capacity, buy what you need up front. Only SO-DIMM-slot "
                            "laptops are user-upgradeable.",
        },
    },
    # ----- mobile_display ---------------------------------------------------
    {
        "id": "aplus1-mob-r2-003", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "A flagship phone's screen renders perfect blacks by switching individual "
                "pixels completely off and needs no separate backlight. Which display "
                "technology is this?",
        "options": [
            {"id": "A", "text": "OLED"},
            {"id": "B", "text": "IPS LCD"},
            {"id": "C", "text": "TN LCD"},
            {"id": "D", "text": "CCFL-backlit LCD"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OLED pixels emit their own light and turn fully off for true black, giving "
                       "high contrast and thinner panels with no backlight layer.",
            "distractors": {
                "B": "IPS LCD has accurate wide-angle color but relies on a backlight, so blacks are never fully off.",
                "C": "TN LCD is fast and cheap but also backlit, with poor viewing angles.",
                "D": "CCFL is an older LCD backlight type — definitely not self-emissive.",
            },
            "exam_pattern": "Self-emissive, no backlight, true blacks = OLED. All LCD types (TN/IPS/VA) need a backlight.",
        },
    },
    {
        "id": "aplus1-mob-r2-004", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "After replacing a laptop's entire display assembly, the picture is perfect but "
                "the built-in webcam and microphone no longer work. What is the MOST likely "
                "reason?",
        "options": [
            {"id": "A", "text": "The webcam/microphone cable in the display bezel was not reconnected"},
            {"id": "B", "text": "The CPU needs a firmware update"},
            {"id": "C", "text": "The trackpad driver is corrupt"},
            {"id": "D", "text": "The laptop battery is swollen"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The webcam and microphone are integrated into the top of the display panel/bezel; "
                       "their connector routes through the hinge and must be reseated after a display swap.",
            "distractors": {
                "B": "The CPU is unrelated to a camera that worked before the panel swap.",
                "C": "The trackpad is a separate device in the palm rest.",
                "D": "A swollen battery causes physical bulging, not a dead camera.",
            },
            "exam_pattern": "Webcam/microphone live in the display assembly — suspect their connector after any "
                            "lid/panel replacement.",
        },
    },
    # ----- mobile_ports_accessories ----------------------------------------
    {
        "id": "aplus1-mob-r2-005", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 1, "type": "mcq",
        "stem": "An illustrator wants to draw on a 2-in-1 laptop's touchscreen with pressure "
                "sensitivity and palm rejection. Which accessory should the technician recommend?",
        "options": [
            {"id": "A", "text": "An active stylus (digitizer pen)"},
            {"id": "B", "text": "A passive capacitive stylus"},
            {"id": "C", "text": "A signature pad"},
            {"id": "D", "text": "A trackpad"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An active stylus/digitizer pen communicates with the screen's digitizer to report "
                       "pressure levels and support palm rejection — ideal for drawing.",
            "distractors": {
                "B": "A passive capacitive stylus just mimics a fingertip: no pressure sensitivity or palm rejection.",
                "C": "A signature pad is a separate peripheral for capturing signatures, not drawing on the screen.",
                "D": "A trackpad is a pointing surface, not a pen for the display.",
            },
            "exam_pattern": "Pressure + palm rejection on a touchscreen = active stylus. Passive stylus = finger substitute only.",
        },
    },
    {
        "id": "aplus1-mob-r2-006", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 2, "type": "mcq",
        "stem": "A laptop has only an HDMI output, but the only available projector accepts a "
                "15-pin VGA cable. Which accessory will let the laptop drive the projector?",
        "options": [
            {"id": "A", "text": "An active HDMI-to-VGA converter"},
            {"id": "B", "text": "A passive HDMI-to-DVI adapter"},
            {"id": "C", "text": "A DisplayPort cable"},
            {"id": "D", "text": "A longer VGA-to-VGA cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "VGA is analog and HDMI is digital, so an ACTIVE converter is needed to translate the "
                       "digital signal into analog VGA for the projector.",
            "distractors": {
                "B": "HDMI-to-DVI is digital-to-digital and cannot feed an analog VGA input.",
                "C": "A DisplayPort cable needs a DisplayPort on both ends — the laptop has HDMI.",
                "D": "A VGA cable can't plug into an HDMI port at all.",
            },
            "exam_pattern": "Digital->analog (HDMI/DP -> VGA) requires an ACTIVE converter; digital->digital "
                            "(HDMI<->DVI) can be a passive adapter.",
        },
    },
    # ----- mobile_connectivity ---------------------------------------------
    {
        "id": "aplus1-mob-r2-007", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A user enables their phone's mobile hotspot at a coffee shop. Which setting MOST "
                "directly prevents strangers from using the user's cellular data?",
        "options": [
            {"id": "A", "text": "Set a WPA2/WPA3 password on the hotspot"},
            {"id": "B", "text": "Turn on Airplane Mode"},
            {"id": "C", "text": "Disable Bluetooth"},
            {"id": "D", "text": "Shorten the screen timeout"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The hotspot broadcasts a Wi-Fi SSID; requiring a WPA2/WPA3 passphrase keeps "
                       "unauthorized devices from associating and consuming data.",
            "distractors": {
                "B": "Airplane Mode disables the radios and would turn the hotspot off entirely.",
                "C": "Bluetooth is a separate radio and doesn't secure the Wi-Fi hotspot.",
                "D": "Screen timeout affects the display, not who can join the hotspot.",
            },
            "exam_pattern": "Secure a hotspot like any Wi-Fi AP: strong WPA2/WPA3 passphrase (and change the "
                            "default SSID/password).",
        },
    },
    {
        "id": "aplus1-mob-r2-008", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "On a flight offering onboard Wi-Fi, a passenger turns on Airplane Mode but still "
                "wants to use the paid Wi-Fi. What can they do?",
        "options": [
            {"id": "A", "text": "Leave Airplane Mode on and re-enable Wi-Fi by itself"},
            {"id": "B", "text": "Nothing — Airplane Mode permanently blocks all radios until disabled"},
            {"id": "C", "text": "Airplane Mode only turns off Wi-Fi, so cellular is already available"},
            {"id": "D", "text": "Remove the SIM card to allow Wi-Fi"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Airplane Mode disables all radios at once, but Wi-Fi (and Bluetooth) can be switched "
                       "back on individually afterward while cellular stays off.",
            "distractors": {
                "B": "Radios can be toggled back on individually after enabling Airplane Mode.",
                "C": "Airplane Mode disables cellular, Wi-Fi, Bluetooth, and NFC — not just Wi-Fi.",
                "D": "Pulling the SIM is unnecessary and doesn't enable Wi-Fi.",
            },
            "exam_pattern": "Airplane Mode kills all radios together; you can re-enable Wi-Fi/Bluetooth selectively "
                            "while cellular remains off.",
        },
    },
    # ----- mobile_apps_sync -------------------------------------------------
    {
        "id": "aplus1-mob-r2-009", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 2, "type": "mcq",
        "stem": "A technician is configuring the OUTGOING mail settings on a smartphone's email "
                "client with secure submission. Which protocol and port should be used to SEND mail?",
        "options": [
            {"id": "A", "text": "SMTP on port 587"},
            {"id": "B", "text": "IMAP on port 143"},
            {"id": "C", "text": "POP3 on port 110"},
            {"id": "D", "text": "SMTP on port 161"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Outgoing mail uses SMTP; the modern secure submission port is 587 (STARTTLS), with 465 "
                       "the implicit-TLS alternative. Port 25 is the legacy unencrypted relay port.",
            "distractors": {
                "B": "IMAP (143, or 993 secure) RETRIEVES mail and keeps it on the server — it doesn't send.",
                "C": "POP3 (110, or 995 secure) also retrieves mail, not sends.",
                "D": "Port 161 is SNMP, unrelated to email.",
            },
            "exam_pattern": "Send = SMTP (587/465, or 25 unencrypted). Receive = IMAP (143/993) or POP3 (110/995).",
        },
    },
    {
        "id": "aplus1-mob-r2-010", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 1, "type": "mcq",
        "stem": "A user activates a new phone, signs in with the same account used on their old "
                "phone, and their contacts, calendar, and photos reappear automatically. Which "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "Cloud-based synchronization"},
            {"id": "B", "text": "USB tethering"},
            {"id": "C", "text": "A local Bluetooth transfer"},
            {"id": "D", "text": "NFC tap-to-pay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The data was synchronized to the provider's cloud; signing in on a new device pulls it "
                       "back down automatically — no cables or local pairing needed.",
            "distractors": {
                "B": "Tethering shares an internet connection; it doesn't restore account data.",
                "C": "Bluetooth transfer is a manual, device-to-device push, not an automatic account restore.",
                "D": "NFC tap-to-pay is a contactless payment feature, unrelated to data sync.",
            },
            "exam_pattern": "Same-account sign-in restoring data across devices = cloud synchronization "
                            "(contacts/calendar/mail/photos).",
        },
    },

    # ===== 2.0 Networking ===================================================
    # ----- ports_protocols_a1 ----------------------------------------------
    {
        "id": "aplus1-net-r2-001", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 2, "type": "mcq",
        "stem": "A help-desk technician needs to take a full graphical remote-desktop session to "
                "a Windows server. Which protocol and default port must be allowed?",
        "options": [
            {"id": "A", "text": "RDP on TCP 3389"},
            {"id": "B", "text": "SSH on TCP 22"},
            {"id": "C", "text": "Telnet on TCP 23"},
            {"id": "D", "text": "VNC on TCP 443"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Remote Desktop Protocol (RDP) provides Windows graphical remote control over TCP 3389.",
            "distractors": {
                "B": "SSH (TCP 22) is an encrypted command-line/remote-shell protocol, not a Windows GUI.",
                "C": "Telnet (TCP 23) is an insecure text-based remote CLI.",
                "D": "VNC offers a remote GUI but its default port is 5900, not 443.",
            },
            "exam_pattern": "Windows GUI remote = RDP 3389. CLI remote = SSH 22 (secure) / Telnet 23 (insecure).",
        },
    },
    {
        "id": "aplus1-net-r2-002", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "ports_protocols_a1", "difficulty": 1, "type": "mcq",
        "stem": "Which protocol and default port translate a hostname such as www.example.com "
                "into its IP address?",
        "options": [
            {"id": "A", "text": "DNS on port 53"},
            {"id": "B", "text": "DHCP on port 67"},
            {"id": "C", "text": "HTTP on port 80"},
            {"id": "D", "text": "LDAP on port 389"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DNS resolves names to IP addresses using port 53 (UDP for lookups, TCP for zone "
                       "transfers and large responses).",
            "distractors": {
                "B": "DHCP (UDP 67/68) hands out IP configuration; it doesn't resolve names.",
                "C": "HTTP (80) serves unencrypted web pages.",
                "D": "LDAP (389) queries a directory service such as Active Directory.",
            },
            "exam_pattern": "Name-to-IP resolution = DNS 53. IP auto-assignment = DHCP 67/68.",
        },
    },
    # ----- networking_hardware ---------------------------------------------
    {
        "id": "aplus1-net-r2-003", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 1, "type": "mcq",
        "stem": "An enterprise already has a wired LAN and a central wireless LAN controller. "
                "Which device actually broadcasts the Wi-Fi signal that client devices "
                "associate with?",
        "options": [
            {"id": "A", "text": "Access point"},
            {"id": "B", "text": "Patch panel"},
            {"id": "C", "text": "Layer 2 switch"},
            {"id": "D", "text": "Media converter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An access point bridges wireless clients onto the wired LAN; in a controller-based "
                       "design these 'thin' APs are centrally managed by the WLC.",
            "distractors": {
                "B": "A patch panel is a passive cable-termination board with no radio.",
                "C": "A switch forwards wired frames between ports; it has no Wi-Fi radio.",
                "D": "A media converter changes one physical medium to another (e.g., fiber to copper).",
            },
            "exam_pattern": "Broadcasts Wi-Fi and bridges to the wired LAN = access point (thin AP + WLC in "
                            "enterprises; SOHO combines AP+router+switch).",
        },
    },
    {
        "id": "aplus1-net-r2-004", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "networking_hardware", "difficulty": 2, "type": "mcq",
        "stem": "In a wiring closet, the permanent cable runs from each wall jack terminate on a "
                "passive board, and short patch cords then jumper from that board to the switch "
                "ports. What is the passive board?",
        "options": [
            {"id": "A", "text": "Patch panel"},
            {"id": "B", "text": "Managed switch"},
            {"id": "C", "text": "PoE injector"},
            {"id": "D", "text": "Firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A patch panel is a passive punch-down termination point for horizontal cabling, letting "
                       "technicians connect runs to switch ports with short, swappable patch cords.",
            "distractors": {
                "B": "A switch is an active device that forwards frames; the panel itself is passive.",
                "C": "A PoE injector adds power to an Ethernet run, not a termination board.",
                "D": "A firewall filters traffic; it isn't a cabling termination panel.",
            },
            "exam_pattern": "Passive termination of permanent cable runs + patch cords to the switch = patch panel.",
        },
    },
    # ----- wireless_a1 ------------------------------------------------------
    {
        "id": "aplus1-net-r2-005", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "A wireless standard operates ONLY in the 5 GHz band, introduced downlink MU-MIMO "
                "and channel widths up to 80/160 MHz, and is marketed as Wi-Fi 5. Which standard "
                "is it?",
        "options": [
            {"id": "A", "text": "802.11ac"},
            {"id": "B", "text": "802.11n"},
            {"id": "C", "text": "802.11g"},
            {"id": "D", "text": "802.11b"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "802.11ac (Wi-Fi 5) is 5 GHz only and adds MU-MIMO and wide 80/160 MHz channels for "
                       "gigabit-class throughput.",
            "distractors": {
                "B": "802.11n (Wi-Fi 4) works in BOTH 2.4 and 5 GHz and introduced MIMO, not MU-MIMO.",
                "C": "802.11g is a 2.4 GHz-only standard up to 54 Mbps.",
                "D": "802.11b is an early 2.4 GHz standard up to 11 Mbps.",
            },
            "exam_pattern": "5 GHz only + MU-MIMO + wide channels = 802.11ac (Wi-Fi 5). Dual-band MIMO = 802.11n. "
                            "6 GHz = 802.11ax/6E.",
        },
    },
    {
        "id": "aplus1-net-r2-006", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "wireless_a1", "difficulty": 2, "type": "mcq",
        "stem": "A warehouse tags every pallet with a small chip that handheld and gateway readers "
                "energize and read by radio from across the dock to track inventory. Which "
                "technology is this?",
        "options": [
            {"id": "A", "text": "RFID"},
            {"id": "B", "text": "NFC"},
            {"id": "C", "text": "Bluetooth"},
            {"id": "D", "text": "Infrared (IR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RFID uses radio to read (often unpowered) tags at a distance, which is ideal for "
                       "inventory and asset tracking.",
            "distractors": {
                "B": "NFC is a short-range (a few centimeters) subset of RFID aimed at two-way transactions "
                     "like tap-to-pay, not across-the-room reads.",
                "C": "Bluetooth pairs devices for data/audio, not passive tag reads.",
                "D": "IR needs line of sight and very short range, used for remotes.",
            },
            "exam_pattern": "Distance tag reads for inventory = RFID. Centimeter two-way taps (pay/pair) = NFC.",
        },
    },
    # ----- network_services_a1 ---------------------------------------------
    {
        "id": "aplus1-net-r2-007", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 1, "type": "mcq",
        "stem": "Which server role automatically leases IP addresses, subnet masks, default "
                "gateways, and DNS server addresses to client devices as they join the network?",
        "options": [
            {"id": "A", "text": "DHCP server"},
            {"id": "B", "text": "DNS server"},
            {"id": "C", "text": "Syslog server"},
            {"id": "D", "text": "Proxy server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A DHCP server automates IP configuration (address, mask, gateway, DNS) via leases, "
                       "removing manual static setup.",
            "distractors": {
                "B": "A DNS server resolves names to IPs; it doesn't hand out IP configuration.",
                "C": "A syslog server collects log messages from devices.",
                "D": "A proxy server forwards, caches, and filters client web requests.",
            },
            "exam_pattern": "Auto IP configuration = DHCP. Name resolution = DNS. Log collection = syslog.",
        },
    },
    {
        "id": "aplus1-net-r2-008", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "network_services_a1", "difficulty": 3, "type": "mcq",
        "stem": "A company wants VPN and wireless logins validated against one central credential "
                "store, with accounting of who connected and when. Which server role provides this?",
        "options": [
            {"id": "A", "text": "Authentication (AAA/RADIUS) server"},
            {"id": "B", "text": "Print server"},
            {"id": "C", "text": "File server"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An AAA server (commonly RADIUS or TACACS+) centralizes Authentication, Authorization, "
                       "and Accounting for network access such as VPN and 802.1X Wi-Fi.",
            "distractors": {
                "B": "A print server queues and shares printers.",
                "C": "A file server hosts shared files and folders.",
                "D": "A load balancer spreads client traffic across multiple servers.",
            },
            "exam_pattern": "Central login + authorization + accounting for network access = AAA (RADIUS/TACACS+) server.",
        },
    },
    # ----- internet_connection_types ---------------------------------------
    {
        "id": "aplus1-net-r2-009", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "A rural office with no cable or fiber mounts a small antenna on the roof aimed at "
                "a line-of-sight tower a few miles away run by a local provider. Latency is much "
                "lower than satellite. Which internet connection type is this?",
        "options": [
            {"id": "A", "text": "Fixed wireless (WISP)"},
            {"id": "B", "text": "Satellite"},
            {"id": "C", "text": "Cellular"},
            {"id": "D", "text": "DSL"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fixed wireless uses a stationary directional antenna with line of sight to a ground "
                       "tower, offering lower latency than orbiting satellite and reaching areas with no wired service.",
            "distractors": {
                "B": "Satellite links a dish to an orbiting satellite and suffers high latency from the long path.",
                "C": "Cellular uses a mobile device on carrier towers with no fixed aimed antenna.",
                "D": "DSL rides existing telephone copper, which this site is not using.",
            },
            "exam_pattern": "Fixed roof antenna + line-of-sight ground tower = fixed wireless (low latency). "
                            "Orbiting dish + high latency = satellite.",
        },
    },
    {
        "id": "aplus1-net-r2-010", "exam": "aplus1", "domain": "networking_a1",
        "subtopic": "internet_connection_types", "difficulty": 2, "type": "mcq",
        "stem": "At a very remote site the only service is a standard analog telephone line. A "
                "modem connects at up to 56 kbps and the voice line is busy whenever someone is "
                "online. Which connection type is this?",
        "options": [
            {"id": "A", "text": "Dial-up"},
            {"id": "B", "text": "DSL"},
            {"id": "C", "text": "Cable"},
            {"id": "D", "text": "Fiber"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dial-up uses an analog modem over the PSTN at up to 56 kbps and ties up the phone line "
                       "during use — the slowest, most basic option, but available anywhere there is a phone line.",
            "distractors": {
                "B": "DSL is also over phone wiring but is always-on broadband that coexists with voice calls.",
                "C": "Cable uses coaxial TV lines and DOCSIS, not an analog modem.",
                "D": "Fiber uses optical strands for very high symmetric speeds.",
            },
            "exam_pattern": "Analog modem, 56 kbps, ties up the phone = dial-up. Phone wiring but broadband + "
                            "simultaneous voice = DSL.",
        },
    },

    # ===== 3.0 Hardware =====================================================
    # ----- cables_connectors -----------------------------------------------
    {
        "id": "aplus1-hw-r2-001", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 1, "type": "mcq",
        "stem": "Which cable connects a 3.5-inch hard drive's DATA interface to the motherboard, "
                "using a flat connector with 7 conductors?",
        "options": [
            {"id": "A", "text": "A 7-pin SATA data cable"},
            {"id": "B", "text": "A 15-pin SATA power cable"},
            {"id": "C", "text": "A 24-pin ATX cable"},
            {"id": "D", "text": "An RJ45 patch cable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Internal SATA uses a slim 7-pin data cable to the motherboard's SATA port; the drive's "
                       "power comes separately from the PSU's 15-pin SATA power connector.",
            "distractors": {
                "B": "The 15-pin SATA connector carries POWER from the PSU, not data to the board.",
                "C": "The 24-pin ATX connector powers the motherboard itself.",
                "D": "RJ45 is for Ethernet networking, not drive data.",
            },
            "exam_pattern": "SATA data = 7-pin (to motherboard). SATA power = 15-pin (from PSU). Don't confuse the two.",
        },
    },
    {
        "id": "aplus1-hw-r2-002", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 2, "type": "mcq",
        "stem": "A technician must run copper cabling that supports 10GBASE-T for the full "
                "100-meter channel. Which cable category should they choose?",
        "options": [
            {"id": "A", "text": "Cat 6a"},
            {"id": "B", "text": "Cat 5e"},
            {"id": "C", "text": "Cat 6"},
            {"id": "D", "text": "Cat 3"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cat 6a supports 10 Gbps Ethernet over the full 100 m with improved shielding against "
                       "alien crosstalk.",
            "distractors": {
                "B": "Cat 5e supports only 1 Gbps at 100 m.",
                "C": "Cat 6 can do 10 Gbps but only to about 55 m (less with interference), not the full 100 m.",
                "D": "Cat 3 is legacy 10 Mbps / telephone-grade wiring.",
            },
            "exam_pattern": "10GBASE-T to 100 m = Cat 6a. Cat 6 = 10G only ~55 m. Cat 5e = 1 Gbps.",
        },
    },
    # ----- memory_ram -------------------------------------------------------
    {
        "id": "aplus1-hw-r2-003", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 2, "type": "mcq",
        "stem": "A technician installs one DDR4-3200 module alongside an existing DDR4-2666 module "
                "in a system that supports both. At what speed will the memory operate?",
        "options": [
            {"id": "A", "text": "At 2666 (the speed of the slowest module)"},
            {"id": "B", "text": "At 3200 (the speed of the fastest module)"},
            {"id": "C", "text": "At 2933 (the average of the two)"},
            {"id": "D", "text": "Neither module will work together"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mixed-speed memory runs at the slowest module's rated speed (the highest common JEDEC "
                       "speed all sticks support) so every module stays stable.",
            "distractors": {
                "B": "The faster stick is down-clocked to match the slower one; it won't run at 3200.",
                "C": "Memory doesn't average speeds; it clocks to a common supported value.",
                "D": "Different speeds are generally compatible and will run — just at the slower rate.",
            },
            "exam_pattern": "Mixed RAM speeds = everything runs at the slowest stick's speed. For rated speed, "
                            "match all modules.",
        },
    },
    {
        "id": "aplus1-hw-r2-004", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 3, "type": "mcq",
        "stem": "A workstation board and CPU support QUAD-channel memory. To actually use "
                "quad-channel bandwidth, how should the technician populate it?",
        "options": [
            {"id": "A", "text": "Install four identical DIMMs, one per channel"},
            {"id": "B", "text": "Install a single large DIMM"},
            {"id": "C", "text": "Install two DIMMs in the same channel"},
            {"id": "D", "text": "Install eight DIMMs regardless of specification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Quad-channel needs one matched module in each of the four channels (four identical DIMMs "
                       "in the specified slots) to multiply bandwidth.",
            "distractors": {
                "B": "One DIMM runs single-channel, wasting the extra channels.",
                "C": "Two sticks in one channel don't populate the other three channels.",
                "D": "Four matched modules across the four channels enable quad-channel; stuffing eight without "
                     "matching doesn't guarantee it.",
            },
            "exam_pattern": "Channel mode = one matched module per channel: dual = 2, quad = 4, in the color/slot "
                            "layout the manual specifies.",
        },
    },
    # ----- storage_devices --------------------------------------------------
    {
        "id": "aplus1-hw-r2-005", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "mcq",
        "stem": "A video editor wants to combine two SSDs into one volume for maximum capacity and "
                "the fastest throughput, and accepts that losing either drive loses all data. "
                "Which RAID level fits?",
        "options": [
            {"id": "A", "text": "RAID 0"},
            {"id": "B", "text": "RAID 1"},
            {"id": "C", "text": "RAID 5"},
            {"id": "D", "text": "RAID 10"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RAID 0 stripes data across drives for maximum speed and full combined capacity but has "
                       "NO redundancy — any drive failure loses the whole array.",
            "distractors": {
                "B": "RAID 1 mirrors for redundancy but gives only one drive's capacity.",
                "C": "RAID 5 uses parity for fault tolerance and sacrifices one drive of capacity.",
                "D": "RAID 10 mirrors and stripes, needing at least four drives and giving only half capacity.",
            },
            "exam_pattern": "Speed + full capacity + zero redundancy = RAID 0. Any fault tolerance = 1/5/6/10.",
        },
    },
    {
        "id": "aplus1-hw-r2-006", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 3, "type": "multi",
        "stem": "An M.2 slot can accept SSDs that communicate over which TWO different interfaces? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "SATA"},
            {"id": "B", "text": "PCIe (NVMe)"},
            {"id": "C", "text": "USB"},
            {"id": "D", "text": "SAS"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "An M.2 slot may be wired for SATA, for PCIe (used by NVMe drives), or both — so the "
                       "keying and board support determine which M.2 SSDs work.",
            "distractors": {
                "C": "USB is an external peripheral bus, not an M.2 storage interface.",
                "D": "SAS is an enterprise drive interface used with backplanes/HBAs, not M.2 slots.",
            },
            "exam_pattern": "M.2 SSDs run over SATA or PCIe/NVMe. Check the slot's keying (B/M) and the board "
                            "manual for which it supports.",
        },
    },
    # ----- motherboards_cpu -------------------------------------------------
    {
        "id": "aplus1-hw-r2-007", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "mcq",
        "stem": "A technician removes a CPU and sees an array of delicate pins on the UNDERSIDE of "
                "the processor itself, which insert into holes in the socket. Which socket design "
                "is this?",
        "options": [
            {"id": "A", "text": "PGA (Pin Grid Array)"},
            {"id": "B", "text": "LGA (Land Grid Array)"},
            {"id": "C", "text": "BGA (Ball Grid Array)"},
            {"id": "D", "text": "ZIF (the lever mechanism is the socket 'type')"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In Pin Grid Array (PGA), the pins are on the CPU and drop into holes in the socket "
                       "(long used by many AMD desktop chips such as AM4).",
            "distractors": {
                "B": "LGA puts the pins in the SOCKET and flat contact pads on the CPU — the opposite arrangement.",
                "C": "BGA chips are soldered to the board with balls of solder and are not removable.",
                "D": "ZIF describes the zero-insertion-force locking mechanism, not where the pins are.",
            },
            "exam_pattern": "Pins on the CPU = PGA. Pins in the socket (pads on CPU) = LGA. Soldered = BGA.",
        },
    },
    {
        "id": "aplus1-hw-r2-008", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "mcq",
        "stem": "A technician installs a simple add-in card — a basic wired network adapter — that "
                "needs very little bandwidth. Which expansion slot is the appropriate choice?",
        "options": [
            {"id": "A", "text": "PCIe x1"},
            {"id": "B", "text": "PCIe x16"},
            {"id": "C", "text": "A legacy PCI slot is required"},
            {"id": "D", "text": "An M.2 slot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Low-bandwidth cards (NICs, sound cards, capture cards) use a short PCIe x1 slot, which "
                       "provides plenty of bandwidth for a gigabit NIC.",
            "distractors": {
                "B": "PCIe x16 is the long, high-lane slot reserved for graphics cards; using it for a NIC wastes it.",
                "C": "Modern boards use PCIe, not legacy PCI; a NIC does not REQUIRE PCI.",
                "D": "M.2 slots are for SSDs/Wi-Fi modules, not a standard add-in NIC.",
            },
            "exam_pattern": "GPU = PCIe x16 (most lanes). Small cards (NIC/sound) = PCIe x1. Storage/Wi-Fi modules = M.2.",
        },
    },
    # ----- power_supplies ---------------------------------------------------
    {
        "id": "aplus1-hw-r2-009", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 2, "type": "multi",
        "stem": "When selecting a power supply for a new high-end gaming PC, which TWO "
                "specifications are MOST important to verify so it can safely power the build? "
                "(Choose two.)",
        "options": [
            {"id": "A", "text": "Sufficient total wattage with headroom for the components"},
            {"id": "B", "text": "The correct PCIe power connectors for the graphics card (e.g., 8-pin / 12VHPWR)"},
            {"id": "C", "text": "The number of USB ports on the case"},
            {"id": "D", "text": "The color of the RGB lighting"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Match the PSU's total wattage (with headroom) to the system's draw AND confirm it has "
                       "the PCIe power connectors the GPU requires.",
            "distractors": {
                "C": "Case USB ports connect to a motherboard header, not to the PSU selection.",
                "D": "RGB lighting is cosmetic and irrelevant to whether the PSU can power the system.",
            },
            "exam_pattern": "Size a PSU by adequate wattage/efficiency AND the right connector set (ATX 24-pin, "
                            "EPS CPU, PCIe GPU, SATA).",
        },
    },
    # ----- peripherals ------------------------------------------------------
    {
        "id": "aplus1-hw-r2-010", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 1, "type": "mcq",
        "stem": "A warehouse clerk needs to quickly enter each product's ID by reading the striped "
                "label on the box instead of typing. Which input peripheral does this?",
        "options": [
            {"id": "A", "text": "Barcode/QR scanner"},
            {"id": "B", "text": "Signature pad"},
            {"id": "C", "text": "KVM switch"},
            {"id": "D", "text": "Webcam"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A barcode/QR scanner reads printed codes and inputs the encoded data as if typed — fast, "
                       "accurate entry for inventory and point of sale.",
            "distractors": {
                "B": "A signature pad captures handwritten signatures, not product codes.",
                "C": "A KVM switch shares one keyboard/monitor/mouse among computers.",
                "D": "A webcam captures video; it isn't a dedicated barcode input device.",
            },
            "exam_pattern": "Reading printed product labels into a system = barcode/QR scanner (an input device).",
        },
    },
    {
        "id": "aplus1-hw-r2-011", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 1, "type": "mcq",
        "stem": "A training department wants employees to practice equipment repair in an immersive "
                "3D environment that tracks head movement and fills their field of view. Which "
                "peripheral is required?",
        "options": [
            {"id": "A", "text": "VR headset"},
            {"id": "B", "text": "Document scanner"},
            {"id": "C", "text": "KVM switch"},
            {"id": "D", "text": "Line printer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A VR (virtual reality) headset provides a head-tracked, immersive stereoscopic display "
                       "for simulation and training.",
            "distractors": {
                "B": "A document scanner digitizes paper.",
                "C": "A KVM switch controls multiple computers from one console.",
                "D": "A line printer is a fast impact printer for high-volume text.",
            },
            "exam_pattern": "Immersive, head-tracked 3D display = VR headset (an output peripheral).",
        },
    },
    # ----- printers ---------------------------------------------------------
    {
        "id": "aplus1-hw-r2-012", "exam": "aplus1", "domain": "hardware",
        "subtopic": "printers", "difficulty": 2, "type": "mcq",
        "stem": "A retail point-of-sale station prints receipts by applying heat to specially "
                "coated paper — it uses no ink ribbon and no toner. Which printer type is this?",
        "options": [
            {"id": "A", "text": "Thermal printer"},
            {"id": "B", "text": "Inkjet printer"},
            {"id": "C", "text": "Laser printer"},
            {"id": "D", "text": "Impact (dot-matrix) printer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A (direct) thermal printer darkens heat-sensitive paper with a heating element — common "
                       "for receipts and shipping labels, with few moving parts and no ink/toner.",
            "distractors": {
                "B": "Inkjet sprays liquid ink droplets onto plain paper.",
                "C": "Laser fuses toner powder using a drum and fuser.",
                "D": "Impact printers strike an inked ribbon against paper.",
            },
            "exam_pattern": "Heat on special coated paper, no ink/toner = thermal printer (receipts/labels). "
                            "Ribbon strike = impact.",
        },
    },

    # ===== 4.0 Virtualization & Cloud Computing =============================
    # ----- cloud_models -----------------------------------------------------
    {
        "id": "aplus1-virt-r2-001", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A cloud provider serves many different customers from one large shared collection "
                "of physical servers and storage, dynamically assigning and reassigning capacity "
                "as tenants need it. Which essential cloud characteristic is this?",
        "options": [
            {"id": "A", "text": "Resource pooling (shared, multitenant resources)"},
            {"id": "B", "text": "Rapid elasticity"},
            {"id": "C", "text": "Measured service"},
            {"id": "D", "text": "Broad network access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Resource pooling means the provider's physical resources are shared across multiple "
                       "tenants and dynamically allocated, with customers abstracted from the exact hardware.",
            "distractors": {
                "B": "Rapid elasticity is the ability to scale capacity up and down quickly with demand.",
                "C": "Measured service is metered, pay-for-what-you-use billing.",
                "D": "Broad network access means services are reachable over the network from varied client devices.",
            },
            "exam_pattern": "Shared multitenant hardware pool = resource pooling. Scale with demand = elasticity. "
                            "Metered billing = measured service.",
        },
    },
    {
        "id": "aplus1-virt-r2-002", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A developer provisions a new virtual server instantly through the provider's web "
                "portal at 2 a.m., without opening a ticket or waiting for provider staff. Which "
                "cloud characteristic does this illustrate?",
        "options": [
            {"id": "A", "text": "On-demand self-service"},
            {"id": "B", "text": "Resource pooling"},
            {"id": "C", "text": "Measured service"},
            {"id": "D", "text": "High availability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On-demand self-service lets customers provision resources themselves, automatically, "
                       "whenever they need them — no human interaction with the provider.",
            "distractors": {
                "B": "Resource pooling is about shared multitenant hardware behind the scenes.",
                "C": "Measured service is metered billing.",
                "D": "High availability is about staying up through failures, not self-provisioning.",
            },
            "exam_pattern": "Self-provision anytime via a portal/API with no provider involvement = on-demand self-service.",
        },
    },
    {
        "id": "aplus1-virt-r2-003", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "A company hosts its application in the cloud across multiple availability zones so "
                "that if one datacenter fails, the service keeps running with no outage. Which "
                "cloud benefit is this?",
        "options": [
            {"id": "A", "text": "High availability"},
            {"id": "B", "text": "Measured service"},
            {"id": "C", "text": "Rapid elasticity"},
            {"id": "D", "text": "On-demand self-service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spreading workloads across zones/regions so a single failure doesn't take the service "
                       "down provides high availability (resilience/uptime).",
            "distractors": {
                "B": "Measured service is metered billing.",
                "C": "Rapid elasticity is scaling capacity with demand, not surviving failures.",
                "D": "On-demand self-service is self-provisioning resources.",
            },
            "exam_pattern": "Survive component/site failure with continued uptime = high availability. Scale with "
                            "load = elasticity.",
        },
    },
    {
        "id": "aplus1-virt-r2-004", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 3, "type": "mcq",
        "stem": "A business forecasts steady user growth over the next three years and plans to add "
                "cloud capacity in planned stages to match that long-term growth. Which "
                "characteristic BEST describes this planned growth capability?",
        "options": [
            {"id": "A", "text": "Scalability"},
            {"id": "B", "text": "Rapid elasticity"},
            {"id": "C", "text": "Measured service"},
            {"id": "D", "text": "Resource pooling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scalability is the ability to grow (or shrink) capacity to meet changing needs over time "
                       "— here, planned long-term expansion.",
            "distractors": {
                "B": "Rapid elasticity is automatic, near-real-time scaling up and down with short-term demand "
                     "spikes, not multi-year planning.",
                "C": "Measured service is metered billing.",
                "D": "Resource pooling is shared multitenant hardware.",
            },
            "exam_pattern": "Planned long-term growth = scalability. Automatic short-term burst up/down = rapid elasticity.",
        },
    },
    {
        "id": "aplus1-virt-r2-005", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "cloud_models", "difficulty": 2, "type": "mcq",
        "stem": "Employees connect from anywhere to Windows desktops that are hosted and fully "
                "managed by a cloud provider and billed per user each month, with no desktop "
                "servers in the company's own datacenter. What is this called?",
        "options": [
            {"id": "A", "text": "Desktop as a Service (cloud-hosted VDI)"},
            {"id": "B", "text": "On-premises VDI"},
            {"id": "C", "text": "Software as a Service (SaaS)"},
            {"id": "D", "text": "A local Type 2 hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Desktop as a Service delivers virtual desktops from the provider's cloud (cloud-hosted "
                       "VDI), managed by the provider and billed per user — no on-prem infrastructure.",
            "distractors": {
                "B": "On-premises VDI runs the virtual desktops on the company's OWN datacenter servers.",
                "C": "SaaS delivers finished applications, not full managed desktops.",
                "D": "A Type 2 hypervisor runs VMs locally on one workstation, not streamed desktops from the cloud.",
            },
            "exam_pattern": "Provider-hosted managed virtual desktops = DaaS (cloud VDI). Same thing in your own "
                            "datacenter = on-prem VDI.",
        },
    },
    # ----- client_side_virtualization --------------------------------------
    {
        "id": "aplus1-virt-r2-006", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "A technician wants a VM to reach the internet through the host's IP address but "
                "NOT be directly reachable from other devices on the office LAN. Which virtual "
                "network mode should be configured?",
        "options": [
            {"id": "A", "text": "NAT"},
            {"id": "B", "text": "Bridged"},
            {"id": "C", "text": "Host-only"},
            {"id": "D", "text": "Internal/isolated"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In NAT mode the VM shares the host's IP for outbound connections (the hypervisor "
                       "translates addresses), so it can reach the internet but isn't directly addressable from the LAN.",
            "distractors": {
                "B": "Bridged mode puts the VM directly on the physical LAN with its own IP, making it reachable "
                     "by other hosts.",
                "C": "Host-only connects the VM only to the host, with no internet.",
                "D": "Internal/isolated connects VMs to each other only, with no host or internet access.",
            },
            "exam_pattern": "Outbound via host IP, not reachable from LAN = NAT. Own LAN IP, fully reachable = "
                            "bridged. No external = host-only/internal.",
        },
    },
    {
        "id": "aplus1-virt-r2-007", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 2, "type": "mcq",
        "stem": "For a malware test lab, several VMs must communicate with each other and the host "
                "but must have NO access to the physical network or internet. Which virtual "
                "network mode achieves this?",
        "options": [
            {"id": "A", "text": "Host-only"},
            {"id": "B", "text": "Bridged"},
            {"id": "C", "text": "NAT"},
            {"id": "D", "text": "External"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Host-only networking creates an isolated virtual network among the VMs and the host, with "
                       "no path to the physical LAN or internet — ideal for safely containing malware.",
            "distractors": {
                "B": "Bridged exposes the VMs directly on the physical LAN — the opposite of isolation.",
                "C": "NAT would give the VMs outbound internet access via the host.",
                "D": "'External' would connect them outward, breaking isolation.",
            },
            "exam_pattern": "Isolate VMs (lab/sandbox) with host+VM-only reachability = host-only/internal. Any "
                            "internet path defeats containment.",
        },
    },
    {
        "id": "aplus1-virt-r2-008", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 1, "type": "mcq",
        "stem": "Before applying a risky update inside a VM, a technician captures the VM's exact "
                "current state so they can roll back instantly if the update fails. What is this "
                "capture called?",
        "options": [
            {"id": "A", "text": "A snapshot"},
            {"id": "B", "text": "A clone"},
            {"id": "C", "text": "A disk defragmentation"},
            {"id": "D", "text": "A hardware reset"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A snapshot saves the VM's state (disk, and optionally memory) at a point in time, letting "
                       "you revert to it if a change goes wrong.",
            "distractors": {
                "B": "A clone creates a separate copy/new VM; it isn't a quick point-in-time revert of the same VM.",
                "C": "Defragmentation reorganizes files on disk — unrelated to saving VM state.",
                "D": "A hardware reset restarts the machine and saves nothing.",
            },
            "exam_pattern": "Point-in-time VM state you can revert to = snapshot. Independent duplicate VM = clone.",
        },
    },
    {
        "id": "aplus1-virt-r2-009", "exam": "aplus1", "domain": "virtualization_cloud",
        "subtopic": "client_side_virtualization", "difficulty": 3, "type": "mcq",
        "stem": "A host has 16 GB of RAM, with the host OS using about 4 GB. When assigning RAM to "
                "several guest VMs, what rule should the technician follow?",
        "options": [
            {"id": "A", "text": "The total RAM assigned to running guests should not exceed the host's physical RAM minus the host OS's needs"},
            {"id": "B", "text": "Guests can be assigned unlimited RAM because paging makes it free"},
            {"id": "C", "text": "Only CPU cores matter; RAM can be over-assigned with no effect"},
            {"id": "D", "text": "Each guest must be given all 16 GB"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Running VMs draw on real host resources, so the sum allocated to active guests must stay "
                       "within the physical RAM left after the host OS — over-committing forces heavy paging and "
                       "degrades everything.",
            "distractors": {
                "B": "Paging to disk is far slower than RAM; over-committing memory cripples performance, it isn't free.",
                "C": "Over-assigning RAM causes thrashing; it is not harmless.",
                "D": "Giving every guest all 16 GB over-commits the host many times over.",
            },
            "exam_pattern": "Size a host so running guests' CPU/RAM/disk stay within physical capacity (minus host "
                            "overhead); over-commitment = thrashing.",
        },
    },

    # ===== 5.0 Hardware & Network Troubleshooting ===========================
    # ----- troubleshooting_methodology_a1 ----------------------------------
    {
        "id": "aplus1-ts-r2-001", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "mcq",
        "stem": "A technician suspects a failing RAM module is causing random crashes, so they "
                "remove and test each stick one at a time to see whether the crashes stop. Which "
                "step of the CompTIA six-step methodology is this?",
        "options": [
            {"id": "A", "text": "Test the theory to determine the cause"},
            {"id": "B", "text": "Establish a theory of probable cause"},
            {"id": "C", "text": "Establish a plan of action"},
            {"id": "D", "text": "Document the findings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Actively testing a suspected cause (swapping/removing the RAM to confirm it's the culprit) "
                       "is step 3, testing the theory.",
            "distractors": {
                "B": "Establishing the theory (step 2) is forming the suspicion, not yet testing it.",
                "C": "The plan of action (step 4) comes AFTER the cause is confirmed.",
                "D": "Documentation is the final step (step 6).",
            },
            "exam_pattern": "Order: 1 identify, 2 theory, 3 TEST theory, 4 plan+implement, 5 verify+prevent, 6 document.",
        },
    },
    {
        "id": "aplus1-ts-r2-002", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "mcq",
        "stem": "Which sequence correctly lists the FIRST three steps of the CompTIA "
                "troubleshooting methodology, in order?",
        "options": [
            {"id": "A", "text": "Identify the problem -> establish a theory of probable cause -> test the theory"},
            {"id": "B", "text": "Establish a theory -> identify the problem -> document findings"},
            {"id": "C", "text": "Test the theory -> identify the problem -> establish a plan"},
            {"id": "D", "text": "Identify the problem -> implement the solution -> establish a theory"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The method begins: (1) identify the problem, (2) establish a theory of probable cause, "
                       "(3) test the theory to determine the cause.",
            "distractors": {
                "B": "You must identify the problem before theorizing, and documentation is last.",
                "C": "You can't test a theory before identifying the problem and forming the theory.",
                "D": "Implementing a solution comes only after a theory is confirmed and a plan is made.",
            },
            "exam_pattern": "Memorize the six steps in order; the exam often asks 'what comes next' or to sequence them.",
        },
    },
    {
        "id": "aplus1-ts-r2-003", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 1, "type": "mcq",
        "stem": "A monitor shows no image. The technician has gathered information and now lists "
                "the possible causes — loose cable, no power, failed backlight, or bad GPU — to "
                "investigate. Which step is the technician performing?",
        "options": [
            {"id": "A", "text": "Establish a theory of probable cause"},
            {"id": "B", "text": "Verify full system functionality"},
            {"id": "C", "text": "Document findings and outcomes"},
            {"id": "D", "text": "Implement preventive measures"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Forming the set of likely causes (and starting with the most probable/obvious) is step 2, "
                       "establishing a theory of probable cause.",
            "distractors": {
                "B": "Verifying functionality (step 5) happens after the fix.",
                "C": "Documentation is the final step.",
                "D": "Preventive measures are part of step 5, after resolution.",
            },
            "exam_pattern": "Brainstorming likely causes = establish a theory (step 2); 'question the obvious' first.",
        },
    },
    # ----- hardware_troubleshooting ----------------------------------------
    {
        "id": "aplus1-ts-r2-004", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A desktop's front-panel USB ports do nothing, but the rear ports built into the "
                "motherboard work normally. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The front-panel USB header cable is disconnected or loose on the motherboard"},
            {"id": "B", "text": "The USB controller driver is missing"},
            {"id": "C", "text": "USB is disabled in UEFI/BIOS"},
            {"id": "D", "text": "The power supply is failing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Front ports connect to a motherboard USB header via an internal cable; if only the front "
                       "ports are dead, that header cable is unplugged or loose (common after a case or board service).",
            "distractors": {
                "B": "A missing USB driver would typically affect ALL USB ports, not just the front ones.",
                "C": "Disabling USB in firmware would also kill the working rear ports.",
                "D": "A failing PSU causes broad instability, not selectively dead front ports.",
            },
            "exam_pattern": "Only the FRONT ports dead = internal front-panel header cable issue. All ports dead = "
                            "driver/firmware/controller.",
        },
    },
    {
        "id": "aplus1-ts-r2-005", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A PC powers on with normal fans and lights, completes POST, then displays 'No boot "
                "device found / Operating system not found.' Which should the technician check FIRST?",
        "options": [
            {"id": "A", "text": "The boot order and that the boot drive is detected/connected in UEFI"},
            {"id": "B", "text": "The CMOS battery, since the clock is wrong"},
            {"id": "C", "text": "The RAM, by reseating it"},
            {"id": "D", "text": "The CPU cooler for dust"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The system POSTs but can't find an OS, so check the firmware boot order and whether the "
                       "boot drive is detected — a wrong boot order, loose SATA/power cable, or failed drive is the usual cause.",
            "distractors": {
                "B": "A dead CMOS battery resets time/settings, but this symptom is specifically a missing boot device.",
                "C": "Bad RAM usually prevents POST entirely (beeps/no video), not a 'no boot device' message.",
                "D": "A dusty cooler causes overheating, not a missing-OS error.",
            },
            "exam_pattern": "POST OK but 'no OS / no boot device' = boot order or the boot drive (cable/detection/"
                            "failure), not RAM/CPU.",
        },
    },
    {
        "id": "aplus1-ts-r2-006", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A PC boots but crashes at random times. A memory diagnostic (such as the built-in "
                "Windows Memory Diagnostic) reports thousands of errors on one pass. What is the "
                "BEST fix?",
        "options": [
            {"id": "A", "text": "Replace the faulty RAM module (after identifying which stick)"},
            {"id": "B", "text": "Replace the power supply"},
            {"id": "C", "text": "Reinstall the GPU driver"},
            {"id": "D", "text": "Defragment the hard drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Consistent memory-diagnostic errors point to a defective RAM module; identify the bad "
                       "stick (test individually) and replace it.",
            "distractors": {
                "B": "A PSU fault causes shutdowns/no-power symptoms, not memory-test errors.",
                "C": "A GPU driver issue causes display artifacts/crashes in graphics, not RAM errors.",
                "D": "Defragmenting addresses disk layout, unrelated to RAM faults.",
            },
            "exam_pattern": "Memory-diagnostic errors = bad RAM -> replace the module. Match the diagnostic to the component.",
        },
    },
    # ----- display_troubleshooting -----------------------------------------
    {
        "id": "aplus1-ts-r2-007", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A monitor displays 'No Signal' while the attached PC is clearly powered on and "
                "running. Which should the technician check FIRST?",
        "options": [
            {"id": "A", "text": "The monitor's selected input source and that the video cable is seated on both ends"},
            {"id": "B", "text": "Replace the monitor as a dead panel"},
            {"id": "C", "text": "Reinstall the operating system"},
            {"id": "D", "text": "Degauss the monitor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'No Signal' with a running PC usually means the monitor is on the wrong input (HDMI vs "
                       "DisplayPort) or the video cable is loose/disconnected — verify the input selection and cabling first.",
            "distractors": {
                "B": "Replacing the monitor is premature before checking input/cable.",
                "C": "Reinstalling the OS won't fix a missing video signal from wrong input/cabling.",
                "D": "Degaussing applies to old CRTs for color distortion, not an LCD 'No Signal'.",
            },
            "exam_pattern": "'No Signal' + PC on = wrong input source or loose/wrong video cable. Check the simple things first.",
        },
    },
    {
        "id": "aplus1-ts-r2-008", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Everything on a new flat-panel monitor looks slightly blurry and stretched, though "
                "it is sharp on another computer. What should the technician set?",
        "options": [
            {"id": "A", "text": "The display to the monitor's native resolution"},
            {"id": "B", "text": "A lower screen brightness"},
            {"id": "C", "text": "A higher audio bitrate"},
            {"id": "D", "text": "The monitor's degauss option"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LCD/LED panels are sharpest at their native (physical) resolution; a non-native resolution "
                       "is scaled and looks fuzzy/stretched — set the OS to the native resolution.",
            "distractors": {
                "B": "Brightness changes luminance, not sharpness.",
                "C": "Audio bitrate is unrelated to picture clarity.",
                "D": "Degaussing is a CRT function, irrelevant to LCD sharpness.",
            },
            "exam_pattern": "Fuzzy/stretched LCD image = not at native resolution -> set native resolution in display settings.",
        },
    },
    {
        "id": "aplus1-ts-r2-009", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A user reports their LCD image noticeably flickers/strobes and causes eye strain. "
                "The video cable is firmly seated. Which setting should the technician verify?",
        "options": [
            {"id": "A", "text": "The display refresh rate (set it to a supported value such as 60 Hz or higher)"},
            {"id": "B", "text": "The mouse polling rate"},
            {"id": "C", "text": "The speaker balance"},
            {"id": "D", "text": "The keyboard repeat delay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A refresh rate set too low or to an unsupported value causes visible flicker; set it to a "
                       "rate the panel supports (e.g., 60 Hz or higher) in display settings.",
            "distractors": {
                "B": "Mouse polling rate affects cursor responsiveness, not screen flicker.",
                "C": "Speaker balance is audio.",
                "D": "Keyboard repeat delay is a typing setting.",
            },
            "exam_pattern": "Flicker with a good cable = wrong/low refresh rate -> set a supported refresh rate.",
        },
    },
    # ----- network_troubleshooting_a1 --------------------------------------
    {
        "id": "aplus1-ts-r2-010", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 2, "type": "mcq",
        "stem": "Two computers on the LAN both pop up an 'IP address conflict — another device is "
                "using this address' warning, and one keeps losing connectivity. What is the MOST "
                "likely cause?",
        "options": [
            {"id": "A", "text": "Two devices are configured with the same IP address"},
            {"id": "B", "text": "The DNS server is offline"},
            {"id": "C", "text": "The default gateway is wrong"},
            {"id": "D", "text": "The cable is the wrong category"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The explicit conflict message means two hosts share one IP — often a static address that "
                       "overlaps the DHCP scope, or two statics set the same — causing one to drop off.",
            "distractors": {
                "B": "A down DNS server breaks name resolution, not an IP-conflict warning.",
                "C": "A wrong gateway blocks off-subnet traffic but doesn't trigger a duplicate-IP message.",
                "D": "Cable category affects speed/link, not an address conflict.",
            },
            "exam_pattern": "'Another device is using this IP' = duplicate IP address (static overlap / outside-scope "
                            "static). Fix the addressing.",
        },
    },
    {
        "id": "aplus1-ts-r2-011", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 1, "type": "multi",
        "stem": "A workstation shows 'Network cable unplugged / media disconnected' and has no link "
                "light. Which TWO physical-layer items should the technician check FIRST? (Choose two.)",
        "options": [
            {"id": "A", "text": "That the patch cable is firmly seated (and undamaged) at both ends"},
            {"id": "B", "text": "The link/activity LED on the NIC and the switch port"},
            {"id": "C", "text": "Flush the DNS resolver cache"},
            {"id": "D", "text": "Renew the DHCP lease"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "'Media disconnected'/no link is a physical-layer symptom: confirm the cable is seated and "
                       "intact at both ends and check the link LEDs on the NIC and switch port (try another cable/port).",
            "distractors": {
                "C": "Flushing the DNS cache addresses name resolution, which is irrelevant when there is no link at all.",
                "D": "Renewing a DHCP lease can't succeed while the link is physically down.",
            },
            "exam_pattern": "No link light / 'media disconnected' = physical layer: cable, connector, port. Fix link "
                            "before IP/DNS steps.",
        },
    },
    {
        "id": "aplus1-ts-r2-012", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 2, "type": "mcq",
        "stem": "Several users near the break room get slow, intermittent 2.4 GHz Wi-Fi that "
                "worsens when the microwave runs and when nearby APs are busy. Which action BEST "
                "addresses this?",
        "options": [
            {"id": "A", "text": "Move the AP to a non-overlapping channel (1, 6, or 11) or shift clients to 5 GHz"},
            {"id": "B", "text": "Disable SSID broadcast on the AP"},
            {"id": "C", "text": "Replace all patch cables with Cat 6"},
            {"id": "D", "text": "Shorten the DHCP lease time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The symptoms are classic 2.4 GHz interference/congestion; using a clean non-overlapping "
                       "channel (1/6/11) or moving clients to the less-crowded 5 GHz band resolves it.",
            "distractors": {
                "B": "Hiding the SSID is a weak security tweak and does nothing for interference.",
                "C": "Patch-cable category is a wired concern, irrelevant to Wi-Fi interference.",
                "D": "DHCP lease time affects addressing, not RF interference.",
            },
            "exam_pattern": "2.4 GHz slow/intermittent near microwaves/other APs = interference -> non-overlapping "
                            "channel (1/6/11) or 5 GHz.",
        },
    },
    # ----- printer_troubleshooting -----------------------------------------
    {
        "id": "aplus1-ts-r2-013", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A printer that worked yesterday now spits out pages of random characters and "
                "symbols instead of the document. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A wrong or corrupted print driver"},
            {"id": "B", "text": "An empty toner cartridge"},
            {"id": "C", "text": "A worn pickup roller"},
            {"id": "D", "text": "A failed fuser assembly"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Garbage/garbled output usually means the print driver is corrupted or the wrong driver/"
                       "printer language is selected; reinstall the correct driver.",
            "distractors": {
                "B": "An empty toner cartridge yields faded/blank pages, not random characters.",
                "C": "A worn pickup roller causes feed/jam problems, not gibberish.",
                "D": "A failed fuser causes smearing/unfused toner, not random characters.",
            },
            "exam_pattern": "Garbled/gibberish pages = wrong or corrupt driver (or wrong page-description language). "
                            "Reinstall/select the correct driver.",
        },
    },
    {
        "id": "aplus1-ts-r2-014", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A laser printer pulls and ejects paper normally, but every sheet comes out "
                "completely blank. Which is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The toner cartridge is empty or the transfer process is failing"},
            {"id": "B", "text": "The fuser is overheating"},
            {"id": "C", "text": "The wrong paper size is selected"},
            {"id": "D", "text": "The network cable is unplugged"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Blank pages from a laser printer point to no toner reaching the page — an empty/defective "
                       "toner cartridge, a protective seal left in place, or a failed transfer roller/corona.",
            "distractors": {
                "B": "An overheating/failed fuser causes smearing or unfused toner, not blank pages.",
                "C": "Wrong paper size causes jams or misprints, not blank output.",
                "D": "A disconnected network cable would stop printing entirely, not feed blank pages.",
            },
            "exam_pattern": "Laser prints blank = toner not transferring (empty cartridge, seal left on, failed "
                            "transfer). Smearing = fuser.",
        },
    },
    {
        "id": "aplus1-ts-r2-015", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A laser printer has started jamming frequently, often crumpling or skewing a "
                "single sheet in the paper path. Which is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "Worn or dirty pickup/feed rollers, or damp/incorrect-weight paper"},
            {"id": "B", "text": "A corrupt print driver"},
            {"id": "C", "text": "An empty toner cartridge"},
            {"id": "D", "text": "An incorrect IP address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Repeated single-sheet jams usually come from worn/dirty feed rollers that can't grip or "
                       "align paper, or from damp, curled, or wrong-weight media; clean/replace rollers and use proper paper.",
            "distractors": {
                "B": "A corrupt driver garbles output; it doesn't physically jam paper.",
                "C": "An empty toner cartridge causes faded/blank pages, not jams.",
                "D": "A wrong IP affects connectivity, not paper feeding.",
            },
            "exam_pattern": "Frequent jams/misfeeds = worn/dirty rollers or bad media (damp/wrong weight). Separation "
                            "pad issues pull multiple sheets.",
        },
    },
]
