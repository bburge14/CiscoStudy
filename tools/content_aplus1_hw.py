"""CompTIA A+ Core 1 (220-1101) Hardware (3.0) expansion item pool.

Original, objective-aligned questions that deepen the existing 220-1101 Hardware
bank (the aplus1-hw-0xx items in content_aplus1.py) to real exam depth. Same
authoring rules as the Cisco and Security+ pools: original scenario-based content
mapped to the public 220-1101 exam objectives, never real exam items.
build_content.py shuffles option order (seeded by id), so the answer key here is
not positionally biased; each wrong option carries its own distractor note.

Coverage (all seven Hardware subtopics): cables_connectors, memory_ram,
storage_devices, motherboards_cpu, power_supplies, peripherals, printers.
IDs continue at aplus1-hw-101 so they never collide with the aplus1-hw-0xx items.
"""

QUESTIONS = [
    # ===== 3.0 Hardware :: cables_connectors =================================
    {
        "id": "aplus1-hw-101", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 2, "type": "mcq",
        "stem": "A technician needs a USB standard capable of 10 Gbps for an external "
                "NVMe enclosure. Which USB specification provides this data rate?",
        "options": [
            {"id": "A", "text": "USB 3.2 Gen 2"},
            {"id": "B", "text": "USB 3.2 Gen 1"},
            {"id": "C", "text": "USB 2.0"},
            {"id": "D", "text": "USB 1.1"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "USB 3.2 Gen 2 (formerly USB 3.1 Gen 2, SuperSpeed+) runs at 10 Gbps, "
                       "enough to approach NVMe speeds over an external enclosure.",
            "distractors": {
                "B": "USB 3.2 Gen 1 (the old USB 3.0 / 3.1 Gen 1, SuperSpeed) tops out at 5 Gbps.",
                "C": "USB 2.0 (Hi-Speed) is only 480 Mbps — far too slow for an NVMe enclosure.",
                "D": "USB 1.1 (Full-Speed) is a legacy 12 Mbps standard.",
            },
            "exam_pattern": "USB speeds: 2.0 = 480 Mbps, 3.2 Gen 1 = 5 Gbps, 3.2 Gen 2 = 10 Gbps, Gen 2x2 = 20 Gbps.",
        },
    },
    {
        "id": "aplus1-hw-102", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 3, "type": "mcq",
        "stem": "A workstation user wants ONE cable on the USB-C connector that carries 40 Gbps "
                "of data plus video. Which interface meets all of these requirements?",
        "options": [
            {"id": "A", "text": "Thunderbolt 3"},
            {"id": "B", "text": "USB 3.2 Gen 1"},
            {"id": "C", "text": "HDMI 1.4"},
            {"id": "D", "text": "eSATA"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Thunderbolt 3 (and 4) run at 40 Gbps over the USB-C connector and carry "
                       "data, video (DisplayPort), and power on a single cable.",
            "distractors": {
                "B": "USB 3.2 Gen 1 is only 5 Gbps and does not natively carry DisplayPort video on its own.",
                "C": "HDMI 1.4 is a video-only connector (about 10.2 Gbps) and is not a USB-C port.",
                "D": "eSATA carries only the SATA storage signal (about 6 Gbps) — no video and not USB-C.",
            },
            "exam_pattern": "Thunderbolt 3/4 = 40 Gbps over USB-C, carrying data + video + power.",
        },
    },
    {
        "id": "aplus1-hw-103", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 3, "type": "mcq",
        "stem": "An M.2 SSD has TWO notches on its edge connector (both a B key and an M key). "
                "What does this B+M keying indicate?",
        "options": [
            {"id": "A", "text": "It will physically fit either a B-keyed or an M-keyed M.2 socket"},
            {"id": "B", "text": "It supports PCIe x4 NVMe at full speed"},
            {"id": "C", "text": "It requires a separate 24-pin power connector"},
            {"id": "D", "text": "It only works in laptops, never in desktops"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A B+M (two-notch) module uses the pins common to both keys, so it drops into "
                       "either a B-key or an M-key socket; such modules are SATA or PCIe x2.",
            "distractors": {
                "B": "Full PCIe x4 NVMe needs an M-key-only module; a B+M module is limited to PCIe x2 or SATA.",
                "C": "M.2 draws power through its edge connector; there is no separate 24-pin feed (that is the ATX board connector).",
                "D": "M.2 sockets appear on both laptops and desktop motherboards.",
            },
            "exam_pattern": "M.2 keys: M-key = up to PCIe x4 (NVMe); B-key = PCIe x2/SATA; B+M (two notches) fits both sockets.",
        },
    },
    {
        "id": "aplus1-hw-104", "exam": "aplus1", "domain": "hardware",
        "subtopic": "cables_connectors", "difficulty": 2, "type": "multi",
        "stem": "A technician needs a single cable that carries BOTH digital video AND audio from "
                "a PC to a display. Which TWO interfaces do this? (Choose two.)",
        "options": [
            {"id": "A", "text": "HDMI"},
            {"id": "B", "text": "DisplayPort"},
            {"id": "C", "text": "VGA"},
            {"id": "D", "text": "DVI-D"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "HDMI and DisplayPort both carry digital video and audio over one cable, which "
                       "is why they are standard on modern GPUs, laptops, and TVs/monitors.",
            "distractors": {
                "C": "VGA is an analog, video-only connector (15-pin); it carries no audio and no digital signal.",
                "D": "DVI-D carries digital video only — standard DVI does not carry audio.",
            },
            "exam_pattern": "Video + audio on one cable = HDMI / DisplayPort; DVI = video only; VGA = analog video only.",
        },
    },

    # ===== 3.0 Hardware :: memory_ram ========================================
    {
        "id": "aplus1-hw-105", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 2, "type": "mcq",
        "stem": "A technician tries to install a DDR4 DIMM into a motherboard with DDR5 slots, "
                "but the module will not seat. What is the reason?",
        "options": [
            {"id": "A", "text": "The notch (key) on a DDR4 module is in a different position than a DDR5 slot's key"},
            {"id": "B", "text": "A DDR4 module has far more pins than a DDR5 slot can accept"},
            {"id": "C", "text": "DDR4 needs a higher voltage that physically melts the slot"},
            {"id": "D", "text": "The DDR4 module is physically much longer than the slot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Each DDR generation is keyed in a different notch position and is not physically "
                       "or electrically interchangeable, so a DDR4 stick will not seat in a DDR5 slot.",
            "distractors": {
                "B": "DDR4 and DDR5 desktop DIMMs both have 288 pins, so pin count is not the obstacle — the keying position differs.",
                "C": "Voltages differ (DDR3 1.5 V, DDR4 1.2 V, DDR5 1.1 V) but a mismatch does not 'melt' the slot; the key simply blocks seating.",
                "D": "Full-size desktop DIMMs are the same length across generations; length is not the issue.",
            },
            "exam_pattern": "DDR generations are notch-keyed and NOT interchangeable; voltages: DDR3 1.5 V, DDR4 1.2 V, DDR5 1.1 V.",
        },
    },
    {
        "id": "aplus1-hw-106", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 2, "type": "mcq",
        "stem": "To get the best memory bandwidth, a technician installs two identical sticks into the "
                "color-matched slots (A2 and B2). Which configuration does this create?",
        "options": [
            {"id": "A", "text": "Dual channel"},
            {"id": "B", "text": "Single channel"},
            {"id": "C", "text": "ECC"},
            {"id": "D", "text": "Triple parity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matched modules in the paired, color-coded slots enable dual-channel mode, "
                       "widening the path to memory and roughly doubling bandwidth versus one stick.",
            "distractors": {
                "B": "Single channel uses one module (or populates one channel), giving lower bandwidth.",
                "C": "ECC is an error-detection/correction feature of the modules, not a channel configuration.",
                "D": "'Triple parity' is not a memory channel mode (dual parity is RAID 6, a storage term).",
            },
            "exam_pattern": "Matched pairs in color-matched slots = dual channel; HEDT/server boards add triple/quad channel.",
        },
    },
    {
        "id": "aplus1-hw-107", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 1, "type": "mcq",
        "stem": "A Windows PC with little RAM is slow, and the OS is using an area on the storage drive "
                "to hold data that overflows physical memory. What is this disk-based area called?",
        "options": [
            {"id": "A", "text": "The pagefile (virtual memory)"},
            {"id": "B", "text": "The ReadyBoost cache"},
            {"id": "C", "text": "A shadow copy"},
            {"id": "D", "text": "The ECC buffer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Virtual memory uses a pagefile on the drive as overflow for physical RAM; heavy "
                       "paging ('thrashing') slows the system and signals that more RAM is needed.",
            "distractors": {
                "B": "ReadyBoost uses a USB flash drive as a supplemental cache — not the primary pagefile being described.",
                "C": "Shadow Copy (VSS) takes point-in-time snapshots for restore/backup, not memory overflow.",
                "D": "There is no 'ECC buffer' that extends RAM onto disk; ECC corrects bit errors within RAM.",
            },
            "exam_pattern": "RAM overflow spills to the pagefile on disk = virtual memory; constant paging means add physical RAM.",
        },
    },
    {
        "id": "aplus1-hw-108", "exam": "aplus1", "domain": "hardware",
        "subtopic": "memory_ram", "difficulty": 3, "type": "mcq",
        "stem": "A server board's documentation calls for 'registered (buffered)' memory. What does "
                "the register/buffer on an RDIMM actually do?",
        "options": [
            {"id": "A", "text": "Buffers address/command signals between the modules and the memory controller for stability with many modules"},
            {"id": "B", "text": "Doubles the rated clock speed of the RAM"},
            {"id": "C", "text": "Stores the system BIOS/UEFI firmware"},
            {"id": "D", "text": "Replaces the CPU's internal cache"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Registered (buffered) DIMMs place a register between the DRAM chips and the "
                       "controller, reducing electrical load so servers can run many high-capacity modules reliably.",
            "distractors": {
                "B": "Buffering improves signal integrity and capacity, not clock speed — RDIMMs are often slightly slower.",
                "C": "Firmware lives in the BIOS/UEFI flash chip, not on a DIMM's register.",
                "D": "CPU cache (L1/L2/L3) is separate on-die SRAM; buffering does not replace it.",
            },
            "exam_pattern": "Registered/buffered (RDIMM) = servers (more modules, stability); unbuffered (UDIMM) = desktops.",
        },
    },

    # ===== 3.0 Hardware :: storage_devices ===================================
    {
        "id": "aplus1-hw-109", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "mcq",
        "stem": "An older ultrabook holds a compact SSD on a card that carries the SATA signal in a "
                "slot predating M.2. Which legacy SSD form factor is this MOST likely?",
        "options": [
            {"id": "A", "text": "mSATA"},
            {"id": "B", "text": "M.2 NVMe"},
            {"id": "C", "text": "3.5-inch SATA"},
            {"id": "D", "text": "eMMC soldered storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "mSATA is a small SSD form factor (physically like Mini PCIe) that carries the SATA "
                       "signal; it was common in ultrabooks before M.2 replaced it.",
            "distractors": {
                "B": "M.2 NVMe is the newer, faster standard that superseded mSATA and can use the PCIe bus.",
                "C": "3.5-inch is the desktop hard-drive size, not a compact ultrabook SSD card.",
                "D": "eMMC is flash soldered to the board (phones, budget laptops), not a removable SATA card.",
            },
            "exam_pattern": "mSATA = legacy compact SATA SSD; M.2 = modern (SATA or NVMe/PCIe); eMMC = soldered flash.",
        },
    },
    {
        "id": "aplus1-hw-110", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "mcq",
        "stem": "A budget laptop drive combines a large spinning platter with a small NAND flash cache "
                "to speed up frequently used files in one unit. What is this drive called?",
        "options": [
            {"id": "A", "text": "SSHD (solid-state hybrid drive)"},
            {"id": "B", "text": "NVMe SSD"},
            {"id": "C", "text": "RAID 0 array"},
            {"id": "D", "text": "Optical drive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SSHD pairs a magnetic HDD with a small SSD cache, accelerating commonly used data "
                       "while keeping the high capacity and low cost of a spinning drive.",
            "distractors": {
                "B": "An NVMe SSD is pure flash on the PCIe bus — no spinning platter.",
                "C": "RAID 0 stripes across multiple separate drives; it is not a single hybrid device.",
                "D": "An optical drive reads/writes CDs, DVDs, or Blu-ray discs — not a hybrid storage device.",
            },
            "exam_pattern": "SSHD = HDD platter + small flash cache in one drive (capacity plus some speed).",
        },
    },
    {
        "id": "aplus1-hw-111", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 3, "type": "mcq",
        "stem": "A database server needs BOTH the speed of striping AND the redundancy of mirroring, "
                "and the budget allows at least four drives. Which RAID level BEST fits?",
        "options": [
            {"id": "A", "text": "RAID 10 (1+0)"},
            {"id": "B", "text": "RAID 0"},
            {"id": "C", "text": "RAID 5"},
            {"id": "D", "text": "RAID 1"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RAID 10 mirrors pairs of drives and stripes across them, giving both high performance "
                       "and fault tolerance; it requires a minimum of four drives.",
            "distractors": {
                "B": "RAID 0 stripes for speed only, with zero redundancy — one failure loses the whole array.",
                "C": "RAID 5 adds redundancy with single distributed parity but carries a write penalty, so writes are slower than RAID 10.",
                "D": "RAID 1 mirrors for redundancy but does not stripe, so it lacks the performance gain.",
            },
            "exam_pattern": "RAID 10 = stripe of mirrors (min 4, speed + redundancy); RAID 5 = striping with single distributed parity (min 3).",
        },
    },
    {
        "id": "aplus1-hw-112", "exam": "aplus1", "domain": "hardware",
        "subtopic": "storage_devices", "difficulty": 2, "type": "mcq",
        "stem": "A technician must connect an external drive enclosure to a shielded port that uses the "
                "SATA protocol and is rated for external cable runs up to about 2 meters. Which port is this?",
        "options": [
            {"id": "A", "text": "eSATA"},
            {"id": "B", "text": "Internal 7-pin SATA"},
            {"id": "C", "text": "Molex"},
            {"id": "D", "text": "RJ11"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "eSATA (external SATA) is the externally shielded variant with a sturdier connector "
                       "rated for longer runs (about 2 m); note that standard eSATA carries data only — no power.",
            "distractors": {
                "B": "The internal 7-pin SATA data connector is unshielded and intended for inside the case (about 1 m).",
                "C": "Molex is a legacy 4-pin DC power connector, not a data interface.",
                "D": "RJ11 is a 6-position telephone-line connector, unrelated to storage.",
            },
            "exam_pattern": "eSATA = external, shielded, data-only (no power), ~2 m; internal SATA data cable ~1 m.",
        },
    },

    # ===== 3.0 Hardware :: motherboards_cpu ==================================
    {
        "id": "aplus1-hw-113", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "mcq",
        "stem": "A technician handles an Intel desktop CPU and sees flat contact pads on its underside, "
                "while the delicate pins are in the motherboard socket. Which socket type is this?",
        "options": [
            {"id": "A", "text": "LGA (Land Grid Array)"},
            {"id": "B", "text": "PGA (Pin Grid Array)"},
            {"id": "C", "text": "BGA (Ball Grid Array)"},
            {"id": "D", "text": "SO-DIMM"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "LGA puts the pins in the socket and flat lands/pads on the CPU — the arrangement "
                       "Intel desktop processors have long used.",
            "distractors": {
                "B": "PGA places the pins on the CPU and the holes in the socket (traditionally AMD).",
                "C": "BGA solders the chip permanently to the board (laptops, phones); it is not a swappable socket.",
                "D": "SO-DIMM is a laptop RAM form factor, not a CPU socket.",
            },
            "exam_pattern": "LGA = pins on socket (Intel); PGA = pins on CPU (traditional AMD); BGA = soldered.",
        },
    },
    {
        "id": "aplus1-hw-114", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 1, "type": "mcq",
        "stem": "A technician installs a discrete graphics card. Which expansion slot provides the MOST "
                "lanes and is the standard choice for a modern GPU?",
        "options": [
            {"id": "A", "text": "PCIe x16"},
            {"id": "B", "text": "PCIe x1"},
            {"id": "C", "text": "PCIe x4"},
            {"id": "D", "text": "Legacy PCI (32-bit)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A PCIe x16 slot provides 16 lanes, the highest common bandwidth and the standard "
                       "slot for a graphics card.",
            "distractors": {
                "B": "PCIe x1 has a single lane, used for small cards (sound, NIC, capture) — too little bandwidth for a GPU.",
                "C": "PCIe x4 offers more than x1 but far fewer lanes than x16.",
                "D": "Legacy PCI is an older, slower parallel bus with no 'lanes' and is not used for modern GPUs.",
            },
            "exam_pattern": "GPU → PCIe x16; smaller add-in cards → x1/x4; more lanes = more bandwidth.",
        },
    },
    {
        "id": "aplus1-hw-115", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "mcq",
        "stem": "Every time a desktop is unplugged overnight, it boots with the wrong date/time and loses "
                "its saved BIOS/UEFI settings. Which component should be replaced?",
        "options": [
            {"id": "A", "text": "The CMOS battery (CR2032 coin cell)"},
            {"id": "B", "text": "The power supply"},
            {"id": "C", "text": "The CPU"},
            {"id": "D", "text": "A RAM module"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A coin-cell CMOS battery (typically CR2032) keeps the real-time clock and BIOS/UEFI "
                       "settings alive with no power; losing time/settings points to a dead CMOS battery.",
            "distractors": {
                "B": "A failed PSU would prevent the system from powering on, not merely reset the clock.",
                "C": "A failing CPU causes crashes or no-boot, not specifically a reset clock.",
                "D": "Bad RAM causes memory errors or no-boot, not loss of date/time settings.",
            },
            "exam_pattern": "Clock resets / BIOS settings lost after power-off = dead CMOS battery (CR2032).",
        },
    },
    {
        "id": "aplus1-hw-116", "exam": "aplus1", "domain": "hardware",
        "subtopic": "motherboards_cpu", "difficulty": 2, "type": "multi",
        "stem": "A technician must enable CPU hardware-assisted virtualization in firmware to run a "
                "hypervisor efficiently. Which TWO technologies are the CPU virtualization extensions? (Choose two.)",
        "options": [
            {"id": "A", "text": "Intel VT-x"},
            {"id": "B", "text": "AMD-V"},
            {"id": "C", "text": "TPM 2.0"},
            {"id": "D", "text": "Intel SpeedStep"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Intel VT-x and AMD-V are the hardware virtualization extensions; enabling them in "
                       "BIOS/UEFI lets a hypervisor run VMs with hardware acceleration.",
            "distractors": {
                "C": "TPM 2.0 is a security/crypto module (BitLocker, Windows 11), not a virtualization extension.",
                "D": "Intel SpeedStep is a CPU power/frequency-scaling feature, unrelated to virtualization.",
            },
            "exam_pattern": "Firmware virtualization = Intel VT-x / AMD-V; don't confuse with TPM (security) or SpeedStep (power).",
        },
    },

    # ===== 3.0 Hardware :: power_supplies ====================================
    {
        "id": "aplus1-hw-117", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 2, "type": "multi",
        "stem": "A high-end graphics card needs supplemental power directly from the PSU. Which TWO "
                "connectors are the standard PCIe power connectors for a GPU? (Choose two.)",
        "options": [
            {"id": "A", "text": "6-pin PCIe"},
            {"id": "B", "text": "8-pin (6+2) PCIe"},
            {"id": "C", "text": "24-pin ATX"},
            {"id": "D", "text": "15-pin SATA power"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "GPUs draw supplemental power through 6-pin and 8-pin (6+2) PCIe power connectors "
                       "from the power supply.",
            "distractors": {
                "C": "The 24-pin ATX connector powers the motherboard, not the graphics card directly.",
                "D": "The 15-pin SATA power connector feeds drives, not a GPU's PCIe power input.",
            },
            "exam_pattern": "GPU supplemental power = 6-pin / 8-pin (6+2) PCIe; 24-pin = motherboard; SATA power = drives.",
        },
    },
    {
        "id": "aplus1-hw-118", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 2, "type": "mcq",
        "stem": "Besides the 24-pin main connector, which connector supplies dedicated power to the CPU "
                "near the top of the motherboard?",
        "options": [
            {"id": "A", "text": "The 4/8-pin EPS (CPU / ATX12V) connector"},
            {"id": "B", "text": "A 15-pin SATA power connector"},
            {"id": "C", "text": "A 6-pin PCIe connector"},
            {"id": "D", "text": "A 4-pin Molex connector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 4-pin or 8-pin EPS connector (often labeled CPU or ATX12V) delivers dedicated "
                       "12 V power to the processor's voltage regulators near the top of the board.",
            "distractors": {
                "B": "A 15-pin SATA power connector feeds storage drives.",
                "C": "A 6-pin PCIe connector supplies graphics cards, not the CPU socket.",
                "D": "A 4-pin Molex is a legacy peripheral/fan power connector, not the CPU power feed.",
            },
            "exam_pattern": "24-pin = board; 4/8-pin EPS (ATX12V) = CPU; 6/8-pin PCIe = GPU; SATA/Molex = drives.",
        },
    },
    {
        "id": "aplus1-hw-119", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 1, "type": "mcq",
        "stem": "A technician wants a power supply that lets them attach ONLY the cables a build actually "
                "needs, improving airflow and cable management. Which PSU design provides this?",
        "options": [
            {"id": "A", "text": "Fully modular"},
            {"id": "B", "text": "Non-modular (fixed cables)"},
            {"id": "C", "text": "Semi-passive (fanless at low load)"},
            {"id": "D", "text": "Dual-rail"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A fully modular PSU has detachable cables, so only the required cables are connected, "
                       "reducing clutter and improving airflow.",
            "distractors": {
                "B": "A non-modular PSU has every cable permanently attached, so unused leads must be tucked away.",
                "C": "Semi-passive/fanless refers to cooling and noise behavior, not detachable cabling.",
                "D": "Dual-rail describes how the 12 V output is split across protected rails, not cable attachment.",
            },
            "exam_pattern": "Modular = detach unused cables; non-modular = fixed cables; semi-modular = some fixed, some detachable.",
        },
    },
    {
        "id": "aplus1-hw-120", "exam": "aplus1", "domain": "hardware",
        "subtopic": "power_supplies", "difficulty": 3, "type": "mcq",
        "stem": "A PSU has a red slide switch marked '115/230.' What is the risk of setting this "
                "switch to the wrong value for the region's mains voltage?",
        "options": [
            {"id": "A", "text": "Component damage or a no-power condition, because it selects the AC input voltage range"},
            {"id": "B", "text": "Changing the 80 PLUS efficiency rating"},
            {"id": "C", "text": "Converting the PSU's output from DC back to AC"},
            {"id": "D", "text": "Increasing the PSU's maximum wattage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 115/230 selector matches the PSU to the local mains (about 120 V in North America, "
                       "about 230 V in Europe). Set to 115 on 230 V mains it can be destroyed; set to 230 on 115 V it usually will not power on.",
            "distractors": {
                "B": "The switch selects input voltage; it does not alter the 80 PLUS efficiency certification.",
                "C": "A PSU converts AC to DC for the PC; this switch does not reverse that.",
                "D": "Maximum wattage is fixed by the PSU's design, not by the input-voltage switch.",
            },
            "exam_pattern": "115/230 selector matches mains; wrong setting = damage (115 on 230 V) or no power (230 on 115 V).",
        },
    },

    # ===== 3.0 Hardware :: peripherals =======================================
    {
        "id": "aplus1-hw-121", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 1, "type": "mcq",
        "stem": "An office must scan 50-page documents without placing each sheet on the glass by hand. "
                "Which scanner feature should the technician recommend?",
        "options": [
            {"id": "A", "text": "An automatic document feeder (ADF)"},
            {"id": "B", "text": "Flatbed glass only"},
            {"id": "C", "text": "A signature pad"},
            {"id": "D", "text": "A barcode wand"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An ADF pulls in a stack of pages and scans them one after another, ideal for "
                       "multi-page documents; many ADFs also support duplex (two-sided) scanning.",
            "distractors": {
                "B": "A flatbed-only scanner requires placing each page on the glass individually.",
                "C": "A signature pad captures handwritten signatures, not document pages.",
                "D": "A barcode wand/scanner reads barcodes, not full document pages.",
            },
            "exam_pattern": "Multi-page/batch scanning = ADF; single page, photos, or books = flatbed glass.",
        },
    },
    {
        "id": "aplus1-hw-122", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 1, "type": "mcq",
        "stem": "A retail checkout needs a device for customers to sign for credit-card purchases "
                "electronically. Which peripheral is purpose-built for this?",
        "options": [
            {"id": "A", "text": "A signature pad"},
            {"id": "B", "text": "A KVM switch"},
            {"id": "C", "text": "A flatbed scanner"},
            {"id": "D", "text": "A webcam"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A signature pad captures a handwritten signature electronically, commonly at "
                       "point-of-sale and for signing documents.",
            "distractors": {
                "B": "A KVM switch shares one keyboard/monitor/mouse among multiple PCs.",
                "C": "A flatbed scanner digitizes pages or photos, not a live signature at checkout.",
                "D": "A webcam captures video/images, not a pen-based signature.",
            },
            "exam_pattern": "Capture a handwritten signature at the point of sale = signature pad.",
        },
    },
    {
        "id": "aplus1-hw-123", "exam": "aplus1", "domain": "hardware",
        "subtopic": "peripherals", "difficulty": 2, "type": "mcq",
        "stem": "On a tablet, which component translates the user's finger touches and gestures into "
                "input coordinates the operating system can use?",
        "options": [
            {"id": "A", "text": "The digitizer (touchscreen sensor)"},
            {"id": "B", "text": "The inverter"},
            {"id": "C", "text": "The LCD backlight"},
            {"id": "D", "text": "The webcam"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The digitizer is the touch-sensitive layer over the display that converts physical "
                       "touch or pen contact into digital coordinates for the OS.",
            "distractors": {
                "B": "An inverter supplies high voltage to a CCFL backlight on older LCDs; it does not sense touch.",
                "C": "The backlight illuminates the LCD panel; it produces no input.",
                "D": "A webcam captures images/video, not touch input.",
            },
            "exam_pattern": "Touch input layer = digitizer; display output = LCD/backlight; older backlight power = inverter.",
        },
    },

    # ===== 3.0 Hardware :: printers ==========================================
    {
        "id": "aplus1-hw-124", "exam": "aplus1", "domain": "hardware",
        "subtopic": "printers", "difficulty": 3, "type": "mcq",
        "stem": "A laser printer's output smears when rubbed right after printing. Which step/component "
                "is responsible for permanently bonding the toner to the paper?",
        "options": [
            {"id": "A", "text": "Fusing (the fuser assembly's heat and pressure)"},
            {"id": "B", "text": "Charging"},
            {"id": "C", "text": "Developing"},
            {"id": "D", "text": "Cleaning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The fusing step uses the fuser's heated rollers and pressure to melt and bond toner "
                       "to the paper; smearing/unfused toner points to a fuser problem.",
            "distractors": {
                "B": "Charging applies a uniform charge to the drum before imaging — not where toner is bonded.",
                "C": "Developing coats the latent image on the drum with toner, before it ever reaches the paper.",
                "D": "Cleaning removes residual toner and charge from the drum at the end of the cycle.",
            },
            "exam_pattern": "Toner smears / won't bond = fusing step; order: processing, charging, exposing, developing, transferring, fusing, cleaning.",
        },
    },
    {
        "id": "aplus1-hw-125", "exam": "aplus1", "domain": "hardware",
        "subtopic": "printers", "difficulty": 2, "type": "mcq",
        "stem": "A warehouse must print on multipart carbon-copy (NCR) forms, where pins physically strike "
                "through several sheets at once. Which printer type is required?",
        "options": [
            {"id": "A", "text": "Impact (dot-matrix)"},
            {"id": "B", "text": "Laser"},
            {"id": "C", "text": "Inkjet"},
            {"id": "D", "text": "Direct thermal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An impact (dot-matrix) printer strikes pins against an inked ribbon and paper, the "
                       "only common type that can print through multipart carbon/NCR forms.",
            "distractors": {
                "B": "A laser printer uses toner and heat and cannot imprint through multipart forms.",
                "C": "An inkjet sprays ink droplets and cannot press through carbon copies.",
                "D": "A direct thermal printer heats special paper and also cannot create carbon copies.",
            },
            "exam_pattern": "Multipart/carbon-copy forms = impact (dot-matrix) printer (pins + ribbon).",
        },
    },
    {
        "id": "aplus1-hw-126", "exam": "aplus1", "domain": "hardware",
        "subtopic": "printers", "difficulty": 2, "type": "mcq",
        "stem": "A maker's 3D printer melts a spool of plastic filament and extrudes it layer by layer "
                "through a heated nozzle. Which 3D printing technology is this?",
        "options": [
            {"id": "A", "text": "FDM (fused deposition modeling) using filament"},
            {"id": "B", "text": "Resin (SLA / vat photopolymerization)"},
            {"id": "C", "text": "Laser toner fusing"},
            {"id": "D", "text": "Dye sublimation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FDM feeds a thermoplastic filament through a heated nozzle and deposits it layer by "
                       "layer — the most common consumer 3D printing method.",
            "distractors": {
                "B": "Resin (SLA) printing cures liquid photopolymer with light; there is no filament spool or heated nozzle.",
                "C": "Toner fusing is a 2D laser-printer process, not a 3D printing technology.",
                "D": "Dye sublimation is a 2D photo-printing method that heats dye onto media.",
            },
            "exam_pattern": "3D FDM = heated nozzle + filament spool; resin/SLA = UV-cured liquid resin.",
        },
    },
]
