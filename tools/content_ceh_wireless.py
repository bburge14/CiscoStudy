"""EC-Council CEH v13 pool - Domain 5.0: Wireless, Mobile, IoT and OT Hacking.

Original, objective-aligned practice items for CertLab's CEH track, covering the
three subtopics of the Wireless, Mobile, IoT and OT domain:
  * ceh_wireless         - Wi-Fi security standards (WEP, WPA/WPA2, WPA3/SAE),
                           WPS weakness, Aircrack-ng, evil twin / rogue AP, and
                           deauthentication attacks.
  * ceh_mobile_platforms - Android/iOS security, rooting/jailbreaking,
                           sideloading, the app sandbox, OWASP Mobile risks
                           (insecure data storage), and MDM.
  * ceh_iot_ot           - discovering exposed devices (Shodan), IoT/OT protocols
                           (MQTT, Modbus), ICS/SCADA, default-credential risk,
                           and network segmentation.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the standard, attack, tool, or defense) - no working
exploit code, payloads, or step-by-step attack instructions, and never real or
memorized exam items.
"""

QUESTIONS = [
    # ===== ceh_wireless =====================================================
    {
        "id": "ceh-wifi-001", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "mcq",
        "stem": "Which legacy wireless security protocol is considered broken because its use of RC4 with "
                "weak initialization vectors lets an attacker recover the key after capturing enough traffic?",
        "options": [
            {"id": "A", "text": "WEP"},
            {"id": "B", "text": "WPA2"},
            {"id": "C", "text": "WPA3"},
            {"id": "D", "text": "EAP-TLS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "WEP's RC4 stream cipher with short, reused initialization vectors leaks key material, so "
                       "captured traffic allows key recovery - WEP is deprecated.",
            "distractors": {
                "B": "WPA2 uses AES-CCMP and is far stronger than WEP.",
                "C": "WPA3 is the newest and strongest Wi-Fi security standard.",
                "D": "EAP-TLS is an enterprise authentication method, not the broken legacy encryption protocol.",
            },
            "exam_pattern": "RC4 plus weak IVs, recoverable key = WEP (deprecated).",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-002", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 3, "type": "mcq",
        "stem": "Which Wi-Fi security standard replaces the WPA2 pre-shared-key handshake with Simultaneous "
                "Authentication of Equals (SAE) to resist offline dictionary attacks?",
        "options": [
            {"id": "A", "text": "WEP"},
            {"id": "B", "text": "WPA3"},
            {"id": "C", "text": "WPA with TKIP"},
            {"id": "D", "text": "An open (no-authentication) network"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "WPA3 introduces SAE (the dragonfly handshake), which resists offline dictionary attacks "
                       "against the captured handshake, unlike WPA2's PSK exchange.",
            "distractors": {
                "A": "WEP has no such handshake and is fundamentally broken.",
                "C": "WPA with TKIP predates SAE and is also deprecated.",
                "D": "An open network provides no authentication or encryption at all.",
            },
            "exam_pattern": "SAE (dragonfly) handshake resisting offline cracking = WPA3.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-003", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 1, "type": "mcq",
        "stem": "Which tool suite is commonly used to capture wireless frames and crack WEP/WPA pre-shared "
                "keys during authorized wireless assessments?",
        "options": [
            {"id": "A", "text": "Nikto"},
            {"id": "B", "text": "sqlmap"},
            {"id": "C", "text": "Aircrack-ng"},
            {"id": "D", "text": "Burp Suite"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Aircrack-ng captures 802.11 frames and performs WEP/WPA key cracking, the standard suite "
                       "for authorized Wi-Fi testing.",
            "distractors": {
                "A": "Nikto scans web servers, not wireless networks.",
                "B": "sqlmap targets SQL injection in web apps.",
                "D": "Burp Suite is a web intercepting proxy, not a wireless cracking suite.",
            },
            "exam_pattern": "Capture Wi-Fi frames and crack WEP/WPA keys = Aircrack-ng.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-004", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "mcq",
        "stem": "An attacker sets up a rogue access point broadcasting the same SSID as a legitimate "
                "corporate network to lure clients into connecting through the attacker. Which attack is this?",
        "options": [
            {"id": "A", "text": "Evil twin"},
            {"id": "B", "text": "MAC flooding"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Smurf attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An evil twin is a rogue AP impersonating a legitimate SSID so victims associate with it, "
                       "enabling interception of their traffic.",
            "distractors": {
                "B": "MAC flooding overflows a switch's CAM table on a wired LAN, not a rogue Wi-Fi AP.",
                "C": "SQL injection is a web/database attack, unrelated to wireless association.",
                "D": "A Smurf attack is an ICMP amplification denial-of-service.",
            },
            "exam_pattern": "Rogue AP cloning a legitimate SSID to intercept clients = evil twin.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-005", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "mcq",
        "stem": "To force a client off the network so it reconnects - letting the attacker capture the WPA2 "
                "four-way handshake - an attacker floods it with spoofed 802.11 management frames. Which attack is this?",
        "options": [
            {"id": "A", "text": "ARP poisoning"},
            {"id": "B", "text": "Phishing"},
            {"id": "C", "text": "Rainbow table attack"},
            {"id": "D", "text": "Deauthentication attack"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A deauthentication attack sends spoofed 802.11 deauth management frames to disconnect "
                       "clients; the forced reconnection lets the attacker capture the handshake for offline cracking.",
            "distractors": {
                "A": "ARP poisoning is a wired-LAN man-in-the-middle technique, not an 802.11 frame attack.",
                "B": "Phishing is social engineering, not a wireless frame flood.",
                "C": "A rainbow table attack cracks hashes offline; it does not disconnect clients.",
            },
            "exam_pattern": "Spoofed 802.11 deauth frames to knock clients off / capture the handshake = deauthentication attack.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },
    {
        "id": "ceh-wifi-006", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_wireless", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Wi-Fi Protected Setup (______) is often disabled on access points because "
                "its 8-digit PIN can be brute-forced to recover the wireless passphrase.",
        "correct": ["wps"],
        "explanation": {
            "correct": "WPS was meant to simplify connecting devices, but its PIN is validated in two weak halves "
                       "and can be brute-forced, so disabling WPS is a common hardening step.",
            "distractors": {},
            "exam_pattern": "8-digit PIN brute-forceable - disable it = WPS weakness.",
        },
        "references": ["CEH v13 Module 16: Hacking Wireless Networks"],
    },

    # ===== ceh_mobile_platforms =============================================
    {
        "id": "ceh-wifi-007", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "mcq",
        "stem": "Removing the manufacturer's built-in restrictions on a mobile device to gain privileged "
                "(root/administrator) control is called jailbreaking on iOS and what on Android?",
        "options": [
            {"id": "A", "text": "Sideloading"},
            {"id": "B", "text": "Rooting"},
            {"id": "C", "text": "Tethering"},
            {"id": "D", "text": "Provisioning"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Gaining privileged control by stripping vendor restrictions is rooting on Android "
                       "(jailbreaking on iOS); it weakens the device's security model.",
            "distractors": {
                "A": "Sideloading installs apps from outside the official store - related risk, but a different action.",
                "C": "Tethering shares the device's connection with other devices.",
                "D": "Provisioning configures a device for enterprise management.",
            },
            "exam_pattern": "Remove vendor restrictions for privileged control: jailbreak (iOS) / root (Android).",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-008", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 1, "type": "mcq",
        "stem": "Which solution lets an enterprise enforce passcodes, push configuration profiles, and "
                "remotely wipe lost or stolen smartphones across its fleet?",
        "options": [
            {"id": "A", "text": "Mobile device management (MDM)"},
            {"id": "B", "text": "A rainbow table"},
            {"id": "C", "text": "A honeypot"},
            {"id": "D", "text": "A SIEM correlation rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MDM (part of broader MDM/UEM) centrally enforces device policy, pushes configuration, and "
                       "supports remote lock/wipe of managed devices.",
            "distractors": {
                "B": "A rainbow table is a password-cracking data structure, not a management platform.",
                "C": "A honeypot is a decoy system, not a device-management tool.",
                "D": "A SIEM rule detects and correlates events but cannot enforce device policy or wipe a phone.",
            },
            "exam_pattern": "Enforce policy / remote-wipe a device fleet = MDM.",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-009", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "mcq",
        "stem": "A user installs an app from an untrusted third-party source instead of the official app "
                "store, bypassing the store's vetting. Which practice (and risk) is this?",
        "options": [
            {"id": "A", "text": "Rooting"},
            {"id": "B", "text": "Tethering"},
            {"id": "C", "text": "Sideloading"},
            {"id": "D", "text": "Containerization"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Installing apps from outside the official store is sideloading, which skips store vetting "
                       "and raises the chance of installing malware.",
            "distractors": {
                "A": "Rooting removes OS restrictions; it is a different action from installing an outside app.",
                "B": "Tethering shares connectivity, not app installation.",
                "D": "Containerization separates work and personal data - a defensive control, not this risk.",
            },
            "exam_pattern": "Install apps outside the official store = sideloading (raises malware risk).",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-010", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "mcq",
        "stem": "A mobile app stores authentication tokens in clear text in a world-readable file on the "
                "device. Which OWASP Mobile risk category does this best illustrate?",
        "options": [
            {"id": "A", "text": "Reflected XSS"},
            {"id": "B", "text": "Weak wireless encryption"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Insecure data storage"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Saving sensitive data unprotected on the device is insecure data storage, a core OWASP "
                       "Mobile risk; secrets should use the platform keystore/keychain.",
            "distractors": {
                "A": "Reflected XSS is a web-application attack, not on-device storage.",
                "B": "Weak wireless encryption concerns the network link, not local file storage.",
                "C": "SQL injection targets server-side databases via untrusted input.",
            },
            "exam_pattern": "Sensitive data saved unprotected on the device = insecure data storage (OWASP Mobile).",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },
    {
        "id": "ceh-wifi-011", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_mobile_platforms", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Mobile operating systems isolate each app and its data from other apps "
                "using an application ______, limiting the damage a malicious app can do.",
        "correct": ["sandbox"],
        "explanation": {
            "correct": "The application sandbox confines each app to its own resources and data, so a compromised "
                       "or malicious app cannot freely reach other apps' data - a core mobile security control.",
            "distractors": {},
            "exam_pattern": "Per-app isolation of code and data = application sandbox.",
        },
        "references": ["CEH v13 Module 17: Hacking Mobile Platforms"],
    },

    # ===== ceh_iot_ot =======================================================
    {
        "id": "ceh-wifi-012", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 2, "type": "mcq",
        "stem": "An assessor wants to locate Internet-exposed IoT devices and industrial systems by their "
                "service banners without scanning them directly. Which resource is most associated with this?",
        "options": [
            {"id": "A", "text": "Shodan"},
            {"id": "B", "text": "John the Ripper"},
            {"id": "C", "text": "Aircrack-ng"},
            {"id": "D", "text": "Responder"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shodan indexes Internet-connected devices - including IoT and ICS/SCADA systems - so a "
                       "tester can find exposed devices passively by banner.",
            "distractors": {
                "B": "John the Ripper is an offline password cracker, not a device search engine.",
                "C": "Aircrack-ng is a wireless cracking suite, not an Internet device index.",
                "D": "Responder poisons LLMNR/NBT-NS on a local network; it does not discover Internet-exposed devices.",
            },
            "exam_pattern": "Find exposed IoT/ICS devices by banner = Shodan.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-013", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 3, "type": "mcq",
        "stem": "In operational technology (OT) environments, which legacy industrial protocol is known for "
                "lacking built-in authentication and encryption, making network segmentation essential?",
        "options": [
            {"id": "A", "text": "HTTPS"},
            {"id": "B", "text": "SSH"},
            {"id": "C", "text": "Modbus"},
            {"id": "D", "text": "TLS 1.3"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Modbus is a widely deployed ICS protocol that was designed without authentication or "
                       "encryption, so isolating it with segmentation is a primary compensating control.",
            "distractors": {
                "A": "HTTPS provides encrypted, authenticated web transport - the opposite of the stated weakness.",
                "B": "SSH provides authenticated, encrypted remote sessions.",
                "D": "TLS 1.3 is a modern secure transport protocol.",
            },
            "exam_pattern": "Legacy ICS protocol with no auth/encryption = Modbus (segment the OT network).",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-014", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 2, "type": "mcq",
        "stem": "Which lightweight publish/subscribe messaging protocol is widely used by IoT devices and, if "
                "its broker is left unauthenticated, can expose device data to anyone who connects?",
        "options": [
            {"id": "A", "text": "SMTP"},
            {"id": "B", "text": "MQTT"},
            {"id": "C", "text": "LDAP"},
            {"id": "D", "text": "NTP"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "MQTT is a lightweight publish/subscribe protocol common in IoT; an unauthenticated or "
                       "unencrypted broker can leak device data, so TLS and authentication are needed.",
            "distractors": {
                "A": "SMTP is an email transport protocol, not an IoT pub/sub protocol.",
                "C": "LDAP is a directory-access protocol.",
                "D": "NTP is a time-synchronization protocol.",
            },
            "exam_pattern": "Lightweight IoT pub/sub protocol = MQTT (secure the broker with TLS and auth).",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-015", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 1, "type": "mcq",
        "stem": "Large IoT botnets have historically spread by logging into devices with well-known factory "
                "default usernames and passwords. Which single hardening step most directly stops this?",
        "options": [
            {"id": "A", "text": "Change the default device credentials"},
            {"id": "B", "text": "Increase the Wi-Fi channel width"},
            {"id": "C", "text": "Enable UPnP"},
            {"id": "D", "text": "Shorten the DHCP lease time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IoT botnets like those that abused default logins are stopped at the source by replacing "
                       "factory default credentials with strong, unique ones.",
            "distractors": {
                "B": "Channel width is a performance setting and does not affect default logins.",
                "C": "Enabling UPnP can increase exposure, not reduce it.",
                "D": "DHCP lease time has no bearing on default-credential abuse.",
            },
            "exam_pattern": "IoT compromise via factory default logins = fix by changing default credentials.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
    {
        "id": "ceh-wifi-016", "exam": "ceh", "domain": "ceh_wireless_mobile",
        "subtopic": "ceh_iot_ot", "difficulty": 3, "type": "multi",
        "stem": "Which TWO controls most directly reduce risk in an environment full of hard-to-patch IoT and "
                "OT devices? (Choose two.)",
        "options": [
            {"id": "A", "text": "Network segmentation that isolates IoT/OT from general IT"},
            {"id": "B", "text": "Disabling all logging on the devices"},
            {"id": "C", "text": "Changing default credentials and disabling unused services"},
            {"id": "D", "text": "Exposing device management interfaces directly to the Internet"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Segmenting IoT/OT away from IT limits lateral movement, and removing default credentials "
                       "plus unused services shrinks the attack surface - both are core mitigations when patching is hard.",
            "distractors": {
                "B": "Disabling logging removes the visibility needed to detect attacks, helping attackers.",
                "D": "Exposing management interfaces to the Internet greatly increases risk.",
            },
            "exam_pattern": "Segment IoT/OT and remove default creds/unused services = core IoT/OT hardening.",
        },
        "references": ["CEH v13 Module 18: IoT and OT Hacking"],
    },
]
