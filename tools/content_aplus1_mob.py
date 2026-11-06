"""CompTIA A+ Core 1 (220-1101) EXPANSION pool — Domain 1.0 Mobile Devices.

Original, objective-aligned questions that deepen the existing ``mobile_devices``
bank (ids ``aplus1-mob-001..006`` live in ``content_aplus1.py``) toward real
220-1101 exam depth. Same authoring rules as the other pools: original
scenario-based content mapped to the public exam objectives, never real exam
items. ``build_content.py`` shuffles option order (seeded by id), so the answer
key here is not positionally biased; every wrong option carries its own
distractor note.

Coverage (24 items, ~5 per subtopic): laptop_hardware, mobile_display,
mobile_ports_accessories, mobile_connectivity, mobile_apps_sync.
"""

QUESTIONS = [
    # ===== laptop_hardware ===================================================
    {
        "id": "aplus1-mob-101", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A laptop has an empty 2.5-inch SATA bay and an empty M.2 slot wired for PCIe. "
                "A technician wants the drive with the HIGHEST sequential throughput. Which "
                "option should they install?",
        "options": [
            {"id": "A", "text": "A 2.5-inch SATA SSD"},
            {"id": "B", "text": "An M.2 NVMe SSD"},
            {"id": "C", "text": "A 2.5-inch 7200 RPM hard drive"},
            {"id": "D", "text": "An M.2 SATA SSD"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An M.2 NVMe SSD talks over PCIe lanes, so it easily exceeds 2,000-7,000 MB/s "
                       "and blows past anything on the SATA bus.",
            "distractors": {
                "A": "A 2.5-inch SATA SSD is fast but capped by the SATA III bus at about 6 Gb/s (~550 MB/s).",
                "C": "A mechanical 7200 RPM hard drive is the slowest choice by far (~100-160 MB/s).",
                "D": "An M.2 SATA SSD uses the same small slot but still rides the SATA bus, so it hits the same ~550 MB/s ceiling — M.2 is only the form factor.",
            },
            "exam_pattern": "M.2 is a form factor, not a speed. NVMe (PCIe) = fastest; SATA (2.5\" or M.2) is capped ~6 Gb/s.",
        },
    },
    {
        "id": "aplus1-mob-102", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 2, "type": "mcq",
        "stem": "A user's laptop no longer sits flat and the trackpad is bulging upward from "
                "underneath. What has MOST likely happened, and how should the technician respond?",
        "options": [
            {"id": "A", "text": "The lithium-ion battery is swelling; power it down, avoid puncturing it, and replace it with the correct part"},
            {"id": "B", "text": "A SO-DIMM has come loose; reseat the memory modules"},
            {"id": "C", "text": "The system board warped from heat; replace the motherboard"},
            {"id": "D", "text": "The SSD is full; delete files to free space"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A swelling (puffed) lithium-ion battery expands and pushes the case and trackpad "
                       "outward. It is a fire/injury hazard: stop using it, do not puncture it, and swap in the correct replacement.",
            "distractors": {
                "B": "A loose SO-DIMM causes no-boot or memory errors, not physical bulging of the chassis.",
                "C": "A warped board is not what lifts the trackpad, and replacing it ignores the obvious swollen battery underneath.",
                "D": "A full SSD slows the system or blocks saves; it cannot deform the case.",
            },
            "exam_pattern": "Case/trackpad bulging = swollen Li-ion battery. Do not puncture; replace it safely.",
        },
    },
    {
        "id": "aplus1-mob-103", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 3, "type": "mcq",
        "stem": "While replacing the wireless card in an older laptop, a technician finds a half-size "
                "card with a 52-pin edge connector that seats at an angle under two retention clips — "
                "it is not an M.2 card. Which interface is this WLAN card using?",
        "options": [
            {"id": "A", "text": "M.2"},
            {"id": "B", "text": "Conventional PCI"},
            {"id": "C", "text": "Mini-PCIe"},
            {"id": "D", "text": "ExpressCard"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Older laptop Wi-Fi/Bluetooth modules use Mini PCI Express (Mini-PCIe): a small "
                       "52-pin card that inserts at an angle and clips down.",
            "distractors": {
                "A": "M.2 is the newer, smaller keyed edge-connector standard that replaced Mini-PCIe for WLAN — the stem rules it out.",
                "B": "Conventional PCI is a legacy desktop expansion bus with long slots, not used for internal laptop WLAN modules.",
                "D": "ExpressCard is a user-accessible slot on the side of a laptop for external add-in cards, not the internal WLAN card interface.",
            },
            "exam_pattern": "52-pin angled WLAN card = Mini-PCIe (older); the newer equivalent is a keyed M.2 card.",
        },
    },
    {
        "id": "aplus1-mob-104", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 1, "type": "mcq",
        "stem": "A company wants staff to unlock their laptops by touch instead of typing a password. "
                "Which built-in laptop component provides this?",
        "options": [
            {"id": "A", "text": "Fingerprint reader"},
            {"id": "B", "text": "TPM chip"},
            {"id": "C", "text": "Smart card reader"},
            {"id": "D", "text": "NFC sensor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A fingerprint reader is a biometric scanner that authenticates the user from a "
                       "body characteristic — a touch instead of a typed password.",
            "distractors": {
                "B": "A TPM securely stores encryption keys and measurements; it does not read fingerprints.",
                "C": "A smart card reader authenticates from a physical card the user inserts/taps, not from a body trait.",
                "D": "An NFC sensor handles contactless tap (pay/pair); it is not a biometric reader.",
            },
            "exam_pattern": "Unlock 'by touch' / body trait = biometric (fingerprint reader). TPM stores keys; smart card = possession.",
        },
    },
    {
        "id": "aplus1-mob-105", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "laptop_hardware", "difficulty": 3, "type": "mcq",
        "stem": "A laptop has two SO-DIMM slots and supports dual-channel memory. To give the user "
                "16 GB with the BEST memory bandwidth, how should the technician install it?",
        "options": [
            {"id": "A", "text": "Install one 16 GB SO-DIMM and leave the second slot empty"},
            {"id": "B", "text": "Install two matched 8 GB SO-DIMMs, one in each slot, to enable dual-channel mode"},
            {"id": "C", "text": "Install a 16 GB and a 4 GB SO-DIMM together"},
            {"id": "D", "text": "Install the single fastest SO-DIMM available and ignore the second slot"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Dual-channel needs a matched module in each channel. Two identical 8 GB SO-DIMMs "
                       "populate both channels, roughly doubling memory bandwidth over a single stick.",
            "distractors": {
                "A": "One 16 GB module fills only one channel, so the system runs in single-channel mode.",
                "C": "Mismatched capacities break symmetric dual-channel (best case a slower flex mode), so it is not optimal.",
                "D": "A single module — however fast — still runs single-channel; dual-channel requires two populated channels.",
            },
            "exam_pattern": "Best laptop RAM bandwidth = a MATCHED pair, one per channel (dual-channel). One stick = single-channel.",
        },
    },

    # ===== mobile_display ====================================================
    {
        "id": "aplus1-mob-106", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 3, "type": "mcq",
        "stem": "An older laptop uses a CCFL-backlit LCD. One component converts the laptop's "
                "low-voltage DC into the high-voltage AC the CCFL tube needs, and its failure is a "
                "common cause of a dim or flickering screen. Which component is it?",
        "options": [
            {"id": "A", "text": "The GPU"},
            {"id": "B", "text": "The digitizer"},
            {"id": "C", "text": "The polarizing layer"},
            {"id": "D", "text": "The inverter"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The inverter steps the laptop's low-voltage DC up to the high-voltage AC a CCFL "
                       "backlight tube requires. A failing inverter commonly causes a dim, flickering, or dark screen.",
            "distractors": {
                "A": "The GPU renders the image but does not supply backlight power.",
                "B": "The digitizer senses touch input; it has nothing to do with powering the backlight.",
                "C": "The polarizer is a passive optical layer in the LCD stack, not a power-conversion component.",
            },
            "exam_pattern": "CCFL backlight needs an inverter (DC->high-voltage AC). Dim/flicker on a CCFL screen -> suspect the inverter.",
        },
    },
    {
        "id": "aplus1-mob-107", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "A newer laptop LCD uses LED backlighting rather than CCFL. Which statement about "
                "the LED backlight is ACCURATE?",
        "options": [
            {"id": "A", "text": "It is more energy-efficient and allows a thinner panel, with no high-voltage inverter required"},
            {"id": "B", "text": "Each pixel emits its own light, so the panel needs no backlight at all"},
            {"id": "C", "text": "It removes the need for an LCD layer entirely"},
            {"id": "D", "text": "It still requires a CCFL inverter to operate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LED backlights are driven directly from low-voltage DC, so they drop the inverter, "
                       "run cooler and more efficiently, and let panels be thinner than CCFL designs.",
            "distractors": {
                "B": "Per-pixel self-emission describes OLED. An LED-backlit LCD still shines light through a shared backlight and LCD layer.",
                "C": "An LED-backlit display still uses an LCD layer to form the image; the LEDs only light it.",
                "D": "The point of LED backlighting is that it needs no high-voltage inverter at all.",
            },
            "exam_pattern": "LED-backlit LCD still has a backlight + LCD layer (no inverter). Per-pixel self-lit = OLED.",
        },
    },
    {
        "id": "aplus1-mob-108", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "On a touchscreen laptop the image displays perfectly, but taps and swipes no longer "
                "register anywhere on the screen. Which component has MOST likely failed?",
        "options": [
            {"id": "A", "text": "The LCD panel"},
            {"id": "B", "text": "The inverter"},
            {"id": "C", "text": "The digitizer"},
            {"id": "D", "text": "The GPU"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The digitizer is the touch-sensing layer bonded over the display. If touch is dead "
                       "but the picture is fine, the digitizer (or its cable) is the suspect.",
            "distractors": {
                "A": "A failed LCD panel would show a bad or missing image — but the stem says the image is perfect.",
                "B": "An inverter powers a CCFL backlight; its failure dims the screen, it does not kill touch input.",
                "D": "A GPU fault corrupts or blanks the rendered image; it does not selectively disable touch while the image is fine.",
            },
            "exam_pattern": "Image good + touch dead = digitizer. Image bad + touch fine = LCD panel.",
        },
    },
    {
        "id": "aplus1-mob-109", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 1, "type": "mcq",
        "stem": "An executive works on confidential data on flights and wants to stop the passengers "
                "beside them from reading the laptop screen. Which accessory BEST addresses this?",
        "options": [
            {"id": "A", "text": "A privacy filter"},
            {"id": "B", "text": "An anti-glare (matte) screen protector"},
            {"id": "C", "text": "A blue-light filter"},
            {"id": "D", "text": "A webcam cover"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A privacy filter narrows the viewing angle so the screen looks dark to anyone off to "
                       "the side, blocking shoulder-surfing while staying readable head-on.",
            "distractors": {
                "B": "An anti-glare protector cuts reflections; it does nothing to hide the screen from a neighbor.",
                "C": "A blue-light filter reduces eye strain and does not restrict who can see the screen.",
                "D": "A webcam cover blocks the camera lens, not the view of the display.",
            },
            "exam_pattern": "Stop side viewing / shoulder-surfing = privacy filter (narrows viewing angle). Anti-glare only cuts reflections.",
        },
    },
    {
        "id": "aplus1-mob-110", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_display", "difficulty": 2, "type": "mcq",
        "stem": "A graphic designer needs a laptop whose LCD gives the most accurate, consistent color "
                "across wide viewing angles. Which LCD panel type should the technician recommend?",
        "options": [
            {"id": "A", "text": "TN (twisted nematic)"},
            {"id": "B", "text": "IPS (in-plane switching)"},
            {"id": "C", "text": "VA (vertical alignment)"},
            {"id": "D", "text": "E-ink (electrophoretic)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "IPS panels are prized for accurate, color-consistent reproduction that holds up across "
                       "wide viewing angles — the standard pick for color-critical work.",
            "distractors": {
                "A": "TN panels are cheap and fast but have the weakest color and narrowest viewing angles.",
                "C": "VA panels give strong contrast, but colors shift more off-axis than on an IPS panel.",
                "D": "E-ink is a low-power reflective technology for e-readers, not a color-accurate laptop display.",
            },
            "exam_pattern": "Color accuracy + wide angles among LCDs = IPS. TN = cheap/fast/poor angles; VA = high contrast.",
        },
    },

    # ===== mobile_ports_accessories ==========================================
    {
        "id": "aplus1-mob-111", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 3, "type": "multi",
        "stem": "A laptop advertises a Thunderbolt 3 port. Which TWO statements about Thunderbolt 3 "
                "are correct? (Choose TWO.)",
        "options": [
            {"id": "A", "text": "It can carry PCIe and DisplayPort data over a single cable"},
            {"id": "B", "text": "It is limited to 5 Gbps, the same as USB 3.0"},
            {"id": "C", "text": "It supports speeds up to 40 Gbps"},
            {"id": "D", "text": "It uses a proprietary rectangular connector that is incompatible with USB-C"},
        ],
        "correct": ["A", "C"],
        "select_count": 2,
        "explanation": {
            "correct": "Thunderbolt 3 runs up to 40 Gbps and tunnels both PCIe and DisplayPort over one cable, "
                       "which is why it can drive docks, external GPUs, and high-res monitors.",
            "distractors": {
                "B": "5 Gbps is USB 3.0 (USB 3.2 Gen 1). Thunderbolt 3 is eight times that at 40 Gbps.",
                "D": "Thunderbolt 3 uses the USB-C connector; a USB-C device plugs into a TB3 port (the port is backward-compatible with USB-C).",
            },
            "exam_pattern": "Thunderbolt 3/4 = USB-C connector, up to 40 Gbps, tunnels PCIe + DisplayPort.",
        },
    },
    {
        "id": "aplus1-mob-112", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 2, "type": "mcq",
        "stem": "At their desk a user wants one connection to the laptop that adds Gigabit Ethernet, "
                "drives two external monitors, and delivers charging power — going beyond simply "
                "mirroring the laptop's built-in ports. Which accessory is this?",
        "options": [
            {"id": "A", "text": "A port replicator"},
            {"id": "B", "text": "A docking station"},
            {"id": "C", "text": "A USB hub"},
            {"id": "D", "text": "A KVM switch"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A docking station adds capabilities the laptop may not have on its own — extra video "
                       "outputs, wired networking, more ports, and power delivery — through a single connection.",
            "distractors": {
                "A": "A port replicator essentially duplicates the ports the laptop already has; it does not add video outputs or charging beyond that.",
                "C": "A USB hub only fans out additional USB ports; it does not drive monitors or supply laptop charging.",
                "D": "A KVM switch shares one keyboard, video, and mouse among multiple computers — a different purpose entirely.",
            },
            "exam_pattern": "Adds NEW capabilities (video, Ethernet, charging) = docking station. Just mirrors existing ports = port replicator.",
        },
    },
    {
        "id": "aplus1-mob-113", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 1, "type": "mcq",
        "stem": "A technician needs a charge-and-sync cable for an older iPhone made before Apple "
                "moved to USB-C. Which proprietary connector does that phone use?",
        "options": [
            {"id": "A", "text": "USB-C"},
            {"id": "B", "text": "Micro-USB"},
            {"id": "C", "text": "Lightning"},
            {"id": "D", "text": "Thunderbolt"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Lightning is Apple's small, reversible proprietary connector used on iPhones (and many "
                       "iPads) before the switch to USB-C.",
            "distractors": {
                "A": "USB-C is the later, industry-standard reversible connector Apple moved to; the stem specifies a device from before that change.",
                "B": "Micro-USB is the older Android/peripheral connector, never used as the iPhone charge port.",
                "D": "Thunderbolt is a high-speed interface (on USB-C connectors), not the iPhone's proprietary charge/sync port.",
            },
            "exam_pattern": "Pre-USB-C iPhone charge/sync = Lightning (Apple proprietary).",
        },
    },
    {
        "id": "aplus1-mob-114", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 1, "type": "mcq",
        "stem": "A user wants to add removable flash storage to an Android phone that has an expansion "
                "slot. Which memory card format is designed for that slot?",
        "options": [
            {"id": "A", "text": "microSD"},
            {"id": "B", "text": "CompactFlash (CF)"},
            {"id": "C", "text": "Full-size SD"},
            {"id": "D", "text": "MMC (MultiMediaCard)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "microSD is the tiny flash card format built for phones and other small mobile devices; "
                       "an adapter lets it also fit full-size SD slots.",
            "distractors": {
                "B": "CompactFlash is a large, thick card used in professional cameras, far too big for a phone slot.",
                "C": "Full-size SD cards are used in cameras and laptops; they do not fit a phone's microSD slot.",
                "D": "MMC is a legacy card format largely superseded by SD/microSD and not used in modern phone slots.",
            },
            "exam_pattern": "Phone removable storage = microSD. Full-size SD = cameras/laptops; CF = pro cameras.",
        },
    },
    {
        "id": "aplus1-mob-115", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_ports_accessories", "difficulty": 2, "type": "mcq",
        "stem": "A technician notices a rectangular USB Type-A port on a laptop has a blue plastic "
                "insert. By common convention, what does the blue color indicate?",
        "options": [
            {"id": "A", "text": "It is a USB 2.0 Hi-Speed port (480 Mbps)"},
            {"id": "B", "text": "It is a USB 3.0 (USB 3.2 Gen 1) SuperSpeed port (5 Gbps)"},
            {"id": "C", "text": "It supplies no power and is data-only"},
            {"id": "D", "text": "It is a Thunderbolt 4 port"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "By convention a blue insert marks a USB 3.0 (USB 3.2 Gen 1) SuperSpeed port rated at 5 Gbps.",
            "distractors": {
                "A": "USB 2.0 Hi-Speed ports are conventionally black (and run 480 Mbps), not blue.",
                "C": "USB-A ports still provide power; color coding signals speed, not a lack of power.",
                "D": "Thunderbolt uses the USB-C connector, not a blue Type-A port.",
            },
            "exam_pattern": "Blue USB-A insert = USB 3.0 SuperSpeed (5 Gbps); black = USB 2.0 (480 Mbps).",
        },
    },

    # ===== mobile_connectivity ===============================================
    {
        "id": "aplus1-mob-116", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "multi",
        "stem": "A user with no Wi-Fi wants to get their laptop online through their smartphone's "
                "cellular data. Which TWO of the following are valid ways to share that connection? "
                "(Choose TWO.)",
        "options": [
            {"id": "A", "text": "Connect the phone to the laptop with a USB cable and enable USB tethering"},
            {"id": "B", "text": "Hold the phone against the laptop to transfer the connection over NFC"},
            {"id": "C", "text": "Turn on the phone's Wi-Fi hotspot and join it from the laptop"},
            {"id": "D", "text": "Enable airplane mode on the phone"},
        ],
        "correct": ["A", "C"],
        "select_count": 2,
        "explanation": {
            "correct": "USB tethering shares cellular data over the cable (and charges the phone), while a Wi-Fi "
                       "hotspot broadcasts it as an SSID the laptop joins. (Bluetooth tethering is a third valid method, not listed here.)",
            "distractors": {
                "B": "NFC works only at a few centimeters for tap-to-pay/tap-to-pair; it does not carry an internet session.",
                "D": "Airplane mode disables the phone's radios, which would cut off the cellular data you are trying to share.",
            },
            "exam_pattern": "Share phone data = USB tethering, Wi-Fi hotspot, or Bluetooth tethering. NFC/airplane mode do not apply.",
        },
    },
    {
        "id": "aplus1-mob-117", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 1, "type": "mcq",
        "stem": "A flight crew asks a passenger to disable all of their phone's wireless radios at once "
                "before takeoff. Which single setting does this?",
        "options": [
            {"id": "A", "text": "Airplane mode"},
            {"id": "B", "text": "Do Not Disturb"},
            {"id": "C", "text": "Turning off Bluetooth only"},
            {"id": "D", "text": "Turning off the mobile hotspot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Airplane mode turns off the device's radios together — cellular, Wi-Fi, Bluetooth, and NFC — "
                       "in one action (Wi-Fi/Bluetooth can be re-enabled separately if allowed).",
            "distractors": {
                "B": "Do Not Disturb silences notifications and calls but leaves the radios transmitting.",
                "C": "Disabling Bluetooth alone leaves cellular and Wi-Fi active.",
                "D": "Turning off the hotspot stops sharing data but does not disable the phone's own radios.",
            },
            "exam_pattern": "Disable ALL radios at once = airplane mode. Do Not Disturb only silences alerts.",
        },
    },
    {
        "id": "aplus1-mob-118", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A user cannot get a new Bluetooth speaker to connect to their phone. Which step is "
                "specifically required to establish the initial Bluetooth link between the two devices?",
        "options": [
            {"id": "A", "text": "Assign the speaker a static IP address"},
            {"id": "B", "text": "Join both devices to the same Wi-Fi SSID"},
            {"id": "C", "text": "Insert a SIM card into the speaker"},
            {"id": "D", "text": "Put the devices in pairing/discoverable mode and confirm the passkey"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Bluetooth requires pairing: make the accessory discoverable, select it on the phone, and "
                       "confirm the passkey/PIN so the two devices trust each other.",
            "distractors": {
                "A": "Bluetooth devices do not use IP addressing; no static IP is involved in pairing.",
                "B": "Bluetooth is its own short-range link and does not depend on sharing a Wi-Fi SSID.",
                "C": "A SIM identifies a phone to a cellular carrier; a Bluetooth speaker has no SIM.",
            },
            "exam_pattern": "Bluetooth = discoverable/pairing mode + confirm passkey. No IP, SSID, or SIM needed.",
        },
    },
    {
        "id": "aplus1-mob-119", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A hiking app needs precise outdoor positioning even when there is no cellular signal "
                "and no nearby Wi-Fi. Which technology provides this?",
        "options": [
            {"id": "A", "text": "GPS (satellite positioning)"},
            {"id": "B", "text": "Cellular tower triangulation"},
            {"id": "C", "text": "Wi-Fi-based positioning"},
            {"id": "D", "text": "NFC"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "GPS receives signals from navigation satellites, so it gives precise location outdoors "
                       "independent of any cell or Wi-Fi network.",
            "distractors": {
                "B": "Cellular triangulation needs cell towers in range and is far less precise — exactly what is missing here.",
                "C": "Wi-Fi positioning relies on known nearby access points, which the scenario rules out.",
                "D": "NFC is a few-centimeter tap technology and provides no geographic location at all.",
            },
            "exam_pattern": "Precise location with no cell/Wi-Fi = GPS (satellites). Tower/Wi-Fi methods need that infrastructure.",
        },
    },
    {
        "id": "aplus1-mob-120", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A user upgrades to a new phone on the same carrier and wants to move their phone number "
                "and subscriber identity over by swapping a removable card. Which component stores that "
                "subscriber identity?",
        "options": [
            {"id": "A", "text": "The microSD card"},
            {"id": "B", "text": "The SIM card"},
            {"id": "C", "text": "The baseband modem"},
            {"id": "D", "text": "The eMMC internal storage"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The SIM (Subscriber Identity Module) card stores the subscriber identity (IMSI) and carrier "
                       "credentials, so moving it to a compatible phone carries the service over.",
            "distractors": {
                "A": "A microSD card holds user files and media; it does not identify the subscriber to the carrier.",
                "C": "The baseband modem processes the cellular radio signal but does not store the subscriber identity.",
                "D": "eMMC is soldered internal storage for the OS and data, not a removable subscriber-identity card.",
            },
            "exam_pattern": "Removable card that identifies you to the carrier = SIM. microSD/eMMC are storage, not identity.",
        },
    },

    # ===== mobile_apps_sync ==================================================
    {
        "id": "aplus1-mob-121", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 2, "type": "mcq",
        "stem": "A user reads the same email account on a phone, a tablet, and a laptop and wants "
                "messages and folders to stay in sync, remaining stored on the mail server. Which "
                "standard retrieval protocol should be configured?",
        "options": [
            {"id": "A", "text": "IMAP"},
            {"id": "B", "text": "POP3"},
            {"id": "C", "text": "SMTP"},
            {"id": "D", "text": "FTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IMAP keeps mail on the server and syncs read state and folders across every device, which "
                       "is exactly what multi-device access needs.",
            "distractors": {
                "B": "POP3 typically downloads mail to a single device (often removing it from the server) and does not sync folders across devices.",
                "C": "SMTP only sends/relays outgoing mail; it does not retrieve or sync a mailbox.",
                "D": "FTP transfers files between hosts and has nothing to do with email retrieval.",
            },
            "exam_pattern": "Multi-device, server-stored, synced mail = IMAP. POP3 = download to one device.",
        },
    },
    {
        "id": "aplus1-mob-122", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 2, "type": "mcq",
        "stem": "A technician is configuring a mobile mail client to retrieve mail using IMAP secured "
                "with SSL/TLS. Which port should the incoming-mail setting use?",
        "options": [
            {"id": "A", "text": "110"},
            {"id": "B", "text": "143"},
            {"id": "C", "text": "993"},
            {"id": "D", "text": "995"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Secure IMAP (IMAP over SSL/TLS, IMAPS) uses TCP port 993.",
            "distractors": {
                "A": "Port 110 is unencrypted POP3.",
                "B": "Port 143 is plain (unencrypted) IMAP.",
                "D": "Port 995 is secure POP3 (POP3S), not IMAP.",
            },
            "exam_pattern": "IMAP 143 / IMAPS 993; POP3 110 / POP3S 995. 'Secure IMAP' = 993.",
        },
    },
    {
        "id": "aplus1-mob-123", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 3, "type": "mcq",
        "stem": "Under a BYOD policy, a company must be able to control and remotely wipe ONLY its "
                "corporate email and apps on an employee-owned phone, without touching the employee's "
                "personal photos and accounts. Which approach BEST meets this requirement?",
        "options": [
            {"id": "A", "text": "Mobile Application Management (MAM) that containerizes corporate apps and allows a selective wipe of just that data"},
            {"id": "B", "text": "Full Mobile Device Management (MDM) enrollment that manages the whole device and wipes it entirely"},
            {"id": "C", "text": "Performing a full factory reset whenever an employee leaves"},
            {"id": "D", "text": "Enabling full-device encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MAM manages at the application level, placing corporate apps and data in a container the "
                       "company can configure and selectively wipe while leaving personal data untouched — ideal for BYOD.",
            "distractors": {
                "B": "Full MDM manages the entire device; a full wipe would also erase the user's personal data, which the policy forbids.",
                "C": "A factory reset erases everything on the device, personal data included — the opposite of selective separation.",
                "D": "Full-device encryption protects data at rest but does not separate or selectively wipe corporate vs personal data.",
            },
            "exam_pattern": "Separate/selectively wipe corporate data on a personal device = MAM (containerization). MDM manages the whole device.",
        },
    },
    {
        "id": "aplus1-mob-124", "exam": "aplus1", "domain": "mobile_devices",
        "subtopic": "mobile_apps_sync", "difficulty": 2, "type": "mcq",
        "stem": "To sign in to a corporate app, a user enters their password and then a one-time code "
                "generated by an authenticator app on their phone. What does this describe?",
        "options": [
            {"id": "A", "text": "Single sign-on (SSO) that replaces the password with one login for many apps"},
            {"id": "B", "text": "Multi-factor authentication, where the app code adds a 'something you have' factor to the password"},
            {"id": "C", "text": "Multi-factor authentication, where the code adds a second 'something you know' factor"},
            {"id": "D", "text": "Biometric authentication, a 'something you are' factor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Using a password plus a code from an authenticator app combines two different factor types: "
                       "'something you know' (password) and 'something you have' (the phone/app that generates the code) = MFA.",
            "distractors": {
                "A": "SSO lets one authentication cover many apps; it does not describe adding a second factor at login.",
                "C": "The one-time code is tied to a device you possess, so it is a 'something you have' factor, not another 'something you know'.",
                "D": "No fingerprint, face, or other body trait is used here, so it is not a biometric ('something you are') factor.",
            },
            "exam_pattern": "Password + authenticator-app code = MFA (know + have). Authenticator/token code = 'something you have'.",
        },
    },
]
