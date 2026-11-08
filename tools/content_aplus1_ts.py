"""CompTIA A+ Core 1 (220-1101) — Hardware & Network Troubleshooting expansion pool.

Original, objective-aligned questions that deepen domain 5.0 (the highest-weighted
A+ Core 1 domain) of the item bank in content_aplus1.py. Same authoring rules as the
Cisco and Security+ pools: original scenario-based content mapped to the public
220-1101 exam objectives, never real exam items. build_content.py shuffles option
order (seeded by id), so the answer key here is not positionally biased; each wrong
option carries its own distractor note.

IDs continue the aplus1-ts- series at 101+ so they never collide with the seed items
(aplus1-ts-001..006) already in content_aplus1.py.
"""

QUESTIONS = [
    # ===== 5.1 Troubleshooting methodology ==================================
    {
        "id": "aplus1-ts-101", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "mcq",
        "stem": "A technician is about to edit the registry and roll back a driver to resolve an "
                "issue on a user's workstation. Following CompTIA best practice, which precaution "
                "should be taken BEFORE implementing these changes?",
        "options": [
            {"id": "A", "text": "If applicable, perform a backup and consider corporate policies, procedures, and impact"},
            {"id": "B", "text": "Document the findings, actions, and outcomes"},
            {"id": "C", "text": "Verify full system functionality"},
            {"id": "D", "text": "Establish a new theory of probable cause"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Before implementing changes the methodology says to consider corporate policies, "
                       "procedures, and impact, and — if applicable — back up data so a failed change "
                       "cannot cause irreversible loss.",
            "distractors": {
                "B": "Documenting findings/actions/outcomes is the final step (step 6), performed after the fix.",
                "C": "Verifying full system functionality is step 5, which comes after the change is implemented.",
                "D": "Establishing a theory is step 2; the technician is already past it and ready to implement a fix.",
            },
            "exam_pattern": "Before changing anything: consider corporate policy/impact and back up data first.",
        },
    },
    {
        "id": "aplus1-ts-102", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "A technician is on step 1 of the CompTIA methodology, identifying the problem. Which "
                "TWO actions belong to this step? (Select TWO.)",
        "options": [
            {"id": "A", "text": "Gather information by questioning the user about the symptoms"},
            {"id": "B", "text": "Determine whether anything has recently changed on the system"},
            {"id": "C", "text": "Establish a plan of action to resolve the problem"},
            {"id": "D", "text": "Document the findings, actions, and outcomes"},
            {"id": "E", "text": "Verify full system functionality and implement preventive measures"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Identifying the problem (step 1) includes gathering information from the user, "
                       "identifying symptoms, questioning the user, and determining if anything has changed.",
            "distractors": {
                "C": "Establishing a plan of action is step 4, after a theory has been tested and confirmed.",
                "D": "Documenting findings/actions/outcomes is the final step (step 6).",
                "E": "Verifying functionality and adding preventive measures is step 5, performed after the fix.",
            },
            "exam_pattern": "Step 1 = gather info, question the user, note recent changes — not plan/verify/document.",
        },
    },
    {
        "id": "aplus1-ts-103", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 1, "type": "mcq",
        "stem": "A technician is establishing a theory of probable cause for a monitor that shows no "
                "image. Applying the 'question the obvious' principle, what should be suspected FIRST?",
        "options": [
            {"id": "A", "text": "A simple cause such as the monitor being powered off or the video cable unseated"},
            {"id": "B", "text": "A failed motherboard that must be replaced"},
            {"id": "C", "text": "Corrupt operating system files requiring a full reinstall"},
            {"id": "D", "text": "A faulty CPU that needs to be reseated"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'Question the obvious' means ruling out simple, common causes first — power, cables, "
                       "and settings — before moving on to complex or costly theories.",
            "distractors": {
                "B": "Replacing the motherboard is an expensive, invasive theory that skips the obvious simple checks.",
                "C": "Reinstalling the OS is a drastic action and would not explain a monitor with no image.",
                "D": "Reseating the CPU is invasive and is not the obvious first thing to check for a blank screen.",
            },
            "exam_pattern": "Question the obvious = check power/cables/settings before complex, invasive theories.",
        },
    },
    {
        "id": "aplus1-ts-104", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 2, "type": "mcq",
        "stem": "A technician has implemented a fix and the device is working again. According to step 5 "
                "of the methodology (verify full system functionality), what else should be done at this step?",
        "options": [
            {"id": "A", "text": "Confirm full functionality and, if applicable, implement preventive measures"},
            {"id": "B", "text": "Establish a new theory of probable cause"},
            {"id": "C", "text": "Question the user to gather information about symptoms"},
            {"id": "D", "text": "Immediately escalate the ticket to tier-2 support"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Step 5 is to verify full system functionality and, if applicable, implement preventive "
                       "measures so the same problem is less likely to recur.",
            "distractors": {
                "B": "Establishing a theory is step 2; the issue is already resolved, so a new theory is unnecessary.",
                "C": "Questioning the user to gather information is part of step 1, which happened at the start.",
                "D": "Escalation applies when a theory cannot be confirmed, not after a verified, working fix.",
            },
            "exam_pattern": "Step 5 = verify full functionality AND add preventive measures to stop a recurrence.",
        },
    },
    {
        "id": "aplus1-ts-105", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 1, "type": "mcq",
        "stem": "Why does the CompTIA troubleshooting methodology end with documenting the findings, "
                "actions, and outcomes?",
        "options": [
            {"id": "A", "text": "To build a reference that speeds up resolving similar issues in the future"},
            {"id": "B", "text": "To assign blame to the user who caused the original failure"},
            {"id": "C", "text": "Because documentation must be completed before a theory is tested"},
            {"id": "D", "text": "To remove the need to verify system functionality"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Documentation (step 6) creates a knowledge-base record so the same or a similar problem "
                       "can be diagnosed and resolved faster next time, and supports accountability and trends.",
            "distractors": {
                "B": "The purpose is knowledge capture and consistency, not assigning blame.",
                "C": "Documentation is the LAST step — it follows testing, the fix, and verification, not precedes testing.",
                "D": "Documentation never replaces verification; verifying functionality (step 5) still happens first.",
            },
            "exam_pattern": "Step 6 documentation = a future reference / knowledge base, performed last of all.",
        },
    },
    {
        "id": "aplus1-ts-106", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "troubleshooting_methodology_a1", "difficulty": 3, "type": "mcq",
        "stem": "After testing, a technician's theory of probable cause is NOT confirmed. According to the "
                "methodology, what are the technician's options at this point?",
        "options": [
            {"id": "A", "text": "Establish a new theory, or escalate the issue if necessary"},
            {"id": "B", "text": "Immediately document the findings and close the ticket"},
            {"id": "C", "text": "Verify full system functionality and add preventive measures"},
            {"id": "D", "text": "Implement the planned fix regardless of the test result"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Step 3 says that if the theory is not confirmed by testing, the technician re-establishes "
                       "a new theory of probable cause or escalates to a higher level of support.",
            "distractors": {
                "B": "Documenting and closing is premature — the root cause has not yet been found.",
                "C": "Verifying functionality is step 5 and only makes sense after a confirmed cause and a fix.",
                "D": "Implementing a fix built on an unconfirmed theory risks wasted effort or new damage.",
            },
            "exam_pattern": "Theory NOT confirmed → form a new theory or escalate; never force an unverified fix.",
        },
    },

    # ===== 5.2 Hardware troubleshooting =====================================
    {
        "id": "aplus1-ts-107", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A desktop is completely unresponsive — no fans spin, no LEDs light, and nothing happens "
                "when the power button is pressed. The technician has confirmed the wall outlet works. "
                "Which component is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The power supply unit (PSU)"},
            {"id": "B", "text": "The hard drive"},
            {"id": "C", "text": "A single bad RAM module"},
            {"id": "D", "text": "The sound card"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "No power at all — no fans, no lights — after confirming the outlet points to the PSU "
                       "(or its cabling/power button). Nothing in the system can start without it.",
            "distractors": {
                "B": "A dead hard drive still lets the system power on and POST; you'd get a 'no boot device' message.",
                "C": "Bad RAM lets the system power on (fans/lights) but fail POST, often with beep codes — not a dead box.",
                "D": "The sound card only affects audio; it has no bearing on whether the system powers on.",
            },
            "exam_pattern": "Dead box — no fans/lights at all = power problem (PSU/cabling), not a POST-level fault.",
        },
    },
    {
        "id": "aplus1-ts-108", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A computer has become very slow, some files fail to open, and a repetitive loud clicking "
                "sound comes from the drive bay. What is MOST likely happening?",
        "options": [
            {"id": "A", "text": "The mechanical hard drive is failing"},
            {"id": "B", "text": "The CMOS battery is dead"},
            {"id": "C", "text": "The RAM is overheating"},
            {"id": "D", "text": "The video driver is corrupt"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A repetitive clicking noise from a mechanical (HDD) drive, combined with slow performance "
                       "and unreadable files, is the classic 'click of death' of a failing hard drive — back it up now.",
            "distractors": {
                "B": "A dead CMOS battery resets the clock/BIOS settings; it makes no noise and doesn't corrupt files.",
                "C": "Overheating RAM causes crashes or no-POST, not a mechanical clicking sound from the drive bay.",
                "D": "A corrupt video driver causes display artifacts or black screens, not drive noise or unreadable files.",
            },
            "exam_pattern": "Loud repetitive clicking + unreadable files = failing mechanical HDD (back up immediately).",
        },
    },
    {
        "id": "aplus1-ts-109", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A desktop randomly reboots and locks up. Inspecting the motherboard, the technician sees "
                "several capacitors near the CPU socket are bulging on top and leaking. What should be concluded?",
        "options": [
            {"id": "A", "text": "The motherboard has failing (swollen) capacitors and should be replaced"},
            {"id": "B", "text": "The thermal paste simply needs to be reapplied"},
            {"id": "C", "text": "The RAM only needs to be reseated"},
            {"id": "D", "text": "The power button is physically stuck"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bulging or leaking (distended) capacitors can no longer filter power properly, causing "
                       "instability, random reboots, and lockups. The motherboard needs to be replaced.",
            "distractors": {
                "B": "Reapplying thermal paste addresses CPU heat; it does nothing for physically damaged capacitors.",
                "C": "Reseating RAM won't fix power delivery from blown capacitors, though it's a cheap thing to rule out.",
                "D": "A stuck power button might cause power issues, but visibly swollen capacitors are the clear fault here.",
            },
            "exam_pattern": "Bulging/leaking capacitors = failing motherboard → random reboots/lockups; replace the board.",
        },
    },
    {
        "id": "aplus1-ts-110", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "While a technician is using a desktop, a burning smell and a thin wisp of smoke rise from "
                "the case. What is the FIRST action the technician should take?",
        "options": [
            {"id": "A", "text": "Immediately power off the system and disconnect it from power"},
            {"id": "B", "text": "Keep working and watch the temperature readings"},
            {"id": "C", "text": "Open a browser on the PC to search the error online"},
            {"id": "D", "text": "Reinstall the operating system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A burning smell or smoke signals a component failure and a fire/shock hazard. Shut the "
                       "system down and unplug it immediately to prevent damage or injury before diagnosing.",
            "distractors": {
                "B": "Continuing to run a smoking system risks fire, further damage, and personal injury.",
                "C": "Using the smoking PC keeps it energized — the priority is to remove power, not to research online.",
                "D": "Reinstalling the OS does nothing for a physical/electrical fault and keeps the hazard powered.",
            },
            "exam_pattern": "Burning smell/smoke = power off and unplug first (safety), then diagnose the dead component.",
        },
    },
    {
        "id": "aplus1-ts-111", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "hardware_troubleshooting", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "A Windows PC has begun throwing frequent Blue Screen of Death (BSOD) STOP errors. Which "
                "TWO are the MOST common underlying causes to investigate? (Select TWO.)",
        "options": [
            {"id": "A", "text": "Faulty or failing RAM"},
            {"id": "B", "text": "A bad or incompatible device driver"},
            {"id": "C", "text": "An unplugged monitor cable"},
            {"id": "D", "text": "A full Recycle Bin"},
            {"id": "E", "text": "A disconnected network cable"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "BSOD STOP errors most often stem from bad memory or a faulty/incompatible driver (also "
                       "failing storage or overheating). Memory diagnostics and driver rollbacks are prime first checks.",
            "distractors": {
                "C": "An unplugged monitor cable causes no image — it does not crash the kernel with a STOP error.",
                "D": "A full Recycle Bin is harmless housekeeping and never triggers a kernel-level BSOD.",
                "E": "A disconnected network cable drops connectivity; it does not cause a Blue Screen crash.",
            },
            "exam_pattern": "BSOD = kernel-level fault → suspect RAM, drivers, failing disk, or overheating first.",
        },
    },

    # ===== 5.3 Display troubleshooting ======================================
    {
        "id": "aplus1-ts-112", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A new LCD monitor has one pixel that stays black no matter what image is displayed; it "
                "never shows any color. What is this defect called?",
        "options": [
            {"id": "A", "text": "A dead pixel"},
            {"id": "B", "text": "A stuck pixel"},
            {"id": "C", "text": "Burn-in"},
            {"id": "D", "text": "A display artifact"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A dead pixel receives no power and remains permanently black/unlit regardless of the image.",
            "distractors": {
                "B": "A stuck pixel is frozen ON showing a single fixed color (red, green, or blue), not black.",
                "C": "Burn-in is a faint permanent ghost of a long-displayed static image, not a single black dot.",
                "D": "Artifacts are transient glitches (blocks/shapes) usually from the GPU, not one permanent dead dot.",
            },
            "exam_pattern": "Dead pixel = always black/off; stuck pixel = frozen on one color; burn-in = ghost of static image.",
        },
    },
    {
        "id": "aplus1-ts-113", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "During gaming, a user sees stray colored blocks, flickering textures, and random shapes "
                "scattered across the screen, and they get worse as the system heats up. External monitors "
                "show the same glitches. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A failing or overheating graphics card (GPU)"},
            {"id": "B", "text": "A dead CMOS battery"},
            {"id": "C", "text": "A faulty keyboard"},
            {"id": "D", "text": "A disconnected speaker"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On-screen artifacts (colored blocks, corrupt textures, random shapes) that worsen with heat "
                       "and appear on any connected display point to a failing/overheating GPU or its video memory.",
            "distractors": {
                "B": "A dead CMOS battery resets BIOS settings/clock; it does not produce rendered graphics artifacts.",
                "C": "A faulty keyboard affects input only and cannot generate corrupt video output.",
                "D": "A disconnected speaker affects audio; it has no effect on what the display renders.",
            },
            "exam_pattern": "Rendered artifacts worsening with heat = failing/overheating GPU (or VRAM), not a cable/driver.",
        },
    },
    {
        "id": "aplus1-ts-114", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "An information kiosk shows the same static menu all day. A faint permanent outline of that "
                "menu is now visible even when other content is on screen. What is this phenomenon?",
        "options": [
            {"id": "A", "text": "Burn-in (image persistence)"},
            {"id": "B", "text": "A cluster of dead pixels"},
            {"id": "C", "text": "Backlight failure"},
            {"id": "D", "text": "An incorrect refresh rate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Displaying a static image for long periods can leave a permanent ghost — burn-in (image "
                       "persistence) — common on OLED and plasma and seen on older/always-on panels.",
            "distractors": {
                "B": "Dead pixels are isolated unlit dots, not a faint full-image ghost of previous content.",
                "C": "Backlight failure makes the whole panel dim or dark; it does not imprint a ghost image.",
                "D": "A wrong refresh rate causes flicker or no signal, not a persistent ghost of prior content.",
            },
            "exam_pattern": "Faint permanent ghost of a long-static image = burn-in / image persistence.",
        },
    },
    {
        "id": "aplus1-ts-115", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A desktop's monitor displays everything with a strong reddish tint, though the picture is "
                "otherwise sharp and correctly sized. What should the technician check FIRST?",
        "options": [
            {"id": "A", "text": "The video cable connection and its pins (and color settings)"},
            {"id": "B", "text": "The amount of installed system RAM"},
            {"id": "C", "text": "The hard drive's SMART health status"},
            {"id": "D", "text": "The power supply wattage rating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An overall color tint usually means a color channel is being lost — most often a loose or "
                       "damaged video cable, bent/broken connector pins (classic on VGA), or wrong color settings.",
            "distractors": {
                "B": "System RAM has no role in color reproduction; a shortage causes crashes or slowness, not tints.",
                "C": "Drive health affects storage reliability, not the color of the video signal on screen.",
                "D": "PSU wattage affects whether components get power, not the color balance of the display output.",
            },
            "exam_pattern": "Whole-screen color tint = check the video cable/pins/connector and color settings first.",
        },
    },
    {
        "id": "aplus1-ts-116", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "display_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A classroom projector runs for about 20 minutes, then suddenly shuts off with its "
                "temperature-warning indicator lit; after it cools it powers back on. What is the MOST "
                "likely cause?",
        "options": [
            {"id": "A", "text": "The projector is overheating — its air filter/vents are likely clogged or a fan is failing"},
            {"id": "B", "text": "The projector lamp (bulb) has completely burned out"},
            {"id": "C", "text": "The HDMI source cable was unplugged"},
            {"id": "D", "text": "The remote control battery is low"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Running for a while and then shutting off with a temperature warning — recovering after it "
                       "cools — is a thermal-protection shutdown, typically from a clogged filter/vents or a failing fan.",
            "distractors": {
                "B": "A burned-out lamp gives no image at all and will not light up again after cooling.",
                "C": "An unplugged source causes a 'no signal' screen but no temperature warning or thermal shutdown.",
                "D": "A low remote battery only affects remote control; it cannot power the projector off from overheating.",
            },
            "exam_pattern": "Projector shuts off after warming up + temp light = overheating (clean filter/vents, check fan).",
        },
    },

    # ===== 5.4 Network troubleshooting ======================================
    {
        "id": "aplus1-ts-117", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 3, "type": "mcq",
        "stem": "A workstation can ping other devices on its own LAN and reach a local file server, but it "
                "cannot reach any site on the internet by name OR by IP address. Which is the MOST likely problem?",
        "options": [
            {"id": "A", "text": "A misconfigured or unreachable default gateway"},
            {"id": "B", "text": "A completely failed network interface card"},
            {"id": "C", "text": "The Ethernet cable is unplugged"},
            {"id": "D", "text": "The access-layer switch has failed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Local traffic works but nothing off-subnet does — by name or by IP — which points to the "
                       "default gateway (the router that forwards traffic beyond the LAN) being wrong or unreachable.",
            "distractors": {
                "B": "A failed NIC would break local LAN access too; here the LAN works fine.",
                "C": "An unplugged cable would stop ALL connectivity, including the local file server it can reach.",
                "D": "A failed switch would cut off the local LAN as well, yet local hosts are reachable.",
            },
            "exam_pattern": "LAN works but no internet (even by IP) = default gateway problem; name-only failure = DNS.",
        },
    },
    {
        "id": "aplus1-ts-118", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 2, "type": "mcq",
        "stem": "A user cannot open any website by its URL, but when the technician types a site's raw IP "
                "address into the browser the page loads normally. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A DNS resolution problem"},
            {"id": "B", "text": "A failed default gateway"},
            {"id": "C", "text": "A damaged patch cable"},
            {"id": "D", "text": "An expired DHCP lease with no address"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Reaching a site by IP but not by name means routing/connectivity is fine and only name-to-IP "
                       "translation is broken — a DNS issue (wrong/unreachable DNS server or bad records).",
            "distractors": {
                "B": "A failed gateway would block the IP-address access too, yet loading by IP works.",
                "C": "A damaged cable would break all connectivity; here IP-based browsing succeeds.",
                "D": "With no DHCP lease the host would have an APIPA address and reach nothing — not even by IP.",
            },
            "exam_pattern": "Works by IP but not by name = DNS. Fails by name AND IP (off-subnet) = gateway.",
        },
    },
    {
        "id": "aplus1-ts-119", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 3, "type": "multi", "select_count": 2,
        "stem": "A user on a wired connection reports slow file transfers and intermittent drops. Which TWO "
                "are plausible causes a technician should investigate? (Select TWO.)",
        "options": [
            {"id": "A", "text": "A damaged or only partially seated Ethernet cable"},
            {"id": "B", "text": "A speed/duplex mismatch between the NIC and the switch port"},
            {"id": "C", "text": "The desktop wallpaper is set to a large image"},
            {"id": "D", "text": "The web browser's cache is full"},
            {"id": "E", "text": "The screen saver has been disabled"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Slow, intermittent wired links commonly trace to a bad/loose cable (or interference) or a "
                       "speed/duplex mismatch, which causes collisions/retransmits and poor throughput.",
            "distractors": {
                "C": "A large wallpaper image uses a little memory locally but has no effect on network throughput.",
                "D": "A full browser cache might slow page loads slightly but does not cause wired link drops or slow transfers.",
                "E": "The screen saver setting is unrelated to network performance or connectivity.",
            },
            "exam_pattern": "Slow/intermittent wired link = check cabling/interference and speed/duplex mismatch.",
        },
    },
    {
        "id": "aplus1-ts-120", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 3, "type": "mcq",
        "stem": "VoIP phone users complain of choppy audio and dropped words, although calls "
                "still connect and stay up. A technician measures high latency and jitter on the "
                "network. What is the MOST likely cause of the choppy audio?",
        "options": [
            {"id": "A", "text": "Latency and jitter are degrading the real-time voice traffic"},
            {"id": "B", "text": "The DHCP server has run out of addresses to lease"},
            {"id": "C", "text": "DNS is failing to resolve hostnames"},
            {"id": "D", "text": "The phones' batteries are dead"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Real-time voice is very sensitive to delay variation. High latency and especially jitter "
                       "(variation in packet delay) cause choppy, broken audio even when the call itself stays connected.",
            "distractors": {
                "B": "A depleted DHCP pool would stop devices from getting an address, not cause choppy audio on live calls.",
                "C": "DNS failures block name resolution; they don't make an already-connected call's audio choppy.",
                "D": "Desk VoIP phones are powered (often via PoE); dead batteries aren't the cause of jitter-based audio loss.",
            },
            "exam_pattern": "Choppy VoIP on connected calls = latency/jitter (prioritize voice with QoS).",
        },
    },
    {
        "id": "aplus1-ts-121", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "network_troubleshooting_a1", "difficulty": 3, "type": "mcq",
        "stem": "A switch port's link light repeatedly goes up and down, and the attached PC keeps losing and "
                "regaining its connection every few seconds. This behavior is BEST described as what?",
        "options": [
            {"id": "A", "text": "Port flapping, often caused by a faulty cable, connector, or NIC"},
            {"id": "B", "text": "APIPA addressing"},
            {"id": "C", "text": "A broadcast storm caused by a switching loop"},
            {"id": "D", "text": "Normal NIC power-saving behavior"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A link that repeatedly goes up and down is port flapping — the connection keeps resetting, "
                       "typically from a damaged cable/connector, a failing NIC, or an auto-negotiation problem.",
            "distractors": {
                "B": "APIPA (169.254.x.x) is a self-assigned address when DHCP fails — it does not cycle the link light.",
                "C": "A broadcast storm floods the network from a loop, slowing everything, but it isn't a single port's up/down link.",
                "D": "Power saving may idle a link but does not cause a steady few-second up/down cycle that drops the user.",
            },
            "exam_pattern": "Link light cycling up/down every few seconds = port flapping (cable/connector/NIC/negotiation).",
        },
    },

    # ===== 5.5 Printer troubleshooting ======================================
    {
        "id": "aplus1-ts-122", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 1, "type": "mcq",
        "stem": "A laser printer's output has become uniformly light and faded across the entire page. What "
                "is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The toner cartridge is low on toner"},
            {"id": "B", "text": "The fuser assembly has failed"},
            {"id": "C", "text": "The pickup roller is worn out"},
            {"id": "D", "text": "The network cable is unplugged"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Uniformly faded, light output across the whole page is the classic sign of low toner (or a "
                       "low density setting). Redistributing or replacing the toner cartridge restores density.",
            "distractors": {
                "B": "A failed fuser leaves toner unfused so it smears/rubs off — it does not make output uniformly faint.",
                "C": "A worn pickup roller causes misfeeds and jams, not faded print.",
                "D": "An unplugged network cable stops jobs from printing entirely; it cannot make a printed page faint.",
            },
            "exam_pattern": "Uniformly faded laser output = low toner; smears/rubs off = fuser.",
        },
    },
    {
        "id": "aplus1-ts-123", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "Every page from a laser printer shows the SAME vertical black line running down the sheet in "
                "the exact same position. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "A scratched or damaged imaging drum"},
            {"id": "B", "text": "A paper jam in the input tray"},
            {"id": "C", "text": "An incorrect print driver"},
            {"id": "D", "text": "A low ink cartridge"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A consistent vertical line/streak in the same place on every page indicates a scratched, "
                       "damaged, or contaminated imaging drum that deposits toner along that track each rotation.",
            "distractors": {
                "B": "A paper jam stops or crumples pages; it does not print a clean, repeating vertical line.",
                "C": "A wrong driver produces garbled/incorrect output, not a single consistent vertical streak.",
                "D": "Laser printers use toner, not ink — an 'ink cartridge' is the wrong technology for this device.",
            },
            "exam_pattern": "Repeating vertical line in the same spot on every laser page = damaged/dirty imaging drum.",
        },
    },
    {
        "id": "aplus1-ts-124", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 3, "type": "mcq",
        "stem": "A laser printer produces a faint second copy of the previous image repeated further down the "
                "same page. What is this effect called, and what is its likely cause?",
        "options": [
            {"id": "A", "text": "Ghosting, usually caused by a worn drum or a failing fuser"},
            {"id": "B", "text": "A simple paper jam"},
            {"id": "C", "text": "A clogged inkjet print-head nozzle"},
            {"id": "D", "text": "A duplex (two-sided) printing setting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ghost images — a faint repeat of content elsewhere on the page — come from residual charge or "
                       "heat retention, typically a worn imaging drum or a failing fuser that isn't clearing prior images.",
            "distractors": {
                "B": "A paper jam halts or crumples printing; it does not create a repeated ghost image.",
                "C": "Clogged nozzles are an inkjet fault (gaps/streaks), not relevant to a laser printer's ghosting.",
                "D": "Duplex printing puts content on both sides of the sheet; it does not create a faint repeat on one side.",
            },
            "exam_pattern": "Faint repeated 'ghost' image on a laser page = worn drum or failing fuser.",
        },
    },
    {
        "id": "aplus1-ts-125", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "A laser printer frequently grabs several sheets of paper at once, feeding multiple pages "
                "together and causing jams. Which component is the MOST likely culprit?",
        "options": [
            {"id": "A", "text": "Worn pickup/separation rollers (or separation pad)"},
            {"id": "B", "text": "The fuser assembly"},
            {"id": "C", "text": "The imaging drum"},
            {"id": "D", "text": "The print driver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Multiple sheets pulled at once (multi-feed) points to worn pickup/separation rollers or a worn "
                       "separation pad that can no longer isolate a single sheet from the stack.",
            "distractors": {
                "B": "The fuser bonds toner with heat/pressure; it has no role in how many sheets are picked up.",
                "C": "The imaging drum transfers the image; it does not control paper feeding from the tray.",
                "D": "The print driver formats the job on the PC; it cannot cause the hardware to grab extra sheets.",
            },
            "exam_pattern": "Multiple sheets pulled / misfeeds = worn pickup/separation rollers or separation pad.",
        },
    },
    {
        "id": "aplus1-ts-126", "exam": "aplus1", "domain": "hw_net_troubleshooting",
        "subtopic": "printer_troubleshooting", "difficulty": 2, "type": "mcq",
        "stem": "An inkjet printer that sat unused for months now prints with horizontal white gaps and "
                "missing streaks through text and images. What should the technician try FIRST?",
        "options": [
            {"id": "A", "text": "Run the printer's print-head cleaning utility to clear the clogged nozzles"},
            {"id": "B", "text": "Replace the fuser assembly"},
            {"id": "C", "text": "Replace the imaging drum"},
            {"id": "D", "text": "Reinstall the computer's operating system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On an inkjet, missing streaks/gaps — especially after long disuse — mean dried ink has clogged "
                       "nozzles. Running the built-in head-cleaning cycle clears them before any parts are replaced.",
            "distractors": {
                "B": "Inkjets have no fuser assembly — that is a laser-printer component.",
                "C": "Inkjets have no imaging drum — that too is a laser component, not part of an inkjet.",
                "D": "Reinstalling the OS is a drastic, unrelated step; the symptom is a mechanical ink-flow (nozzle) issue.",
            },
            "exam_pattern": "Inkjet gaps/missing streaks (often after disuse) = clogged nozzles → run head cleaning first.",
        },
    },
]
