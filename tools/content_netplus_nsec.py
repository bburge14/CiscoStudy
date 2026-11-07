"""CompTIA Network+ N10-009 — Domain 4.0 Network Security EXPANSION pool.

Original, objective-aligned items that deepen the base network_security bank
(netplus-nsec-001..006 in content_netplus.py) to real N10-009 exam depth.
Never real exam items. build_content.py shuffles option order, so the answer
key here is not positionally biased.

Coverage (all four 4.0 subtopics, ~5 each):
  security_concepts_np   -> RADIUS vs TACACS+, zero trust, evil twin,
                            VLAN hopping (double-tagging), screened subnet (DMZ)
  network_hardening      -> DHCP snooping, dynamic ARP inspection, SSH over
                            Telnet, new-device hardening, out-of-band mgmt
  remote_access          -> site-to-site VPN, split tunneling, IPsec ESP vs AH,
                            RDP 3389, jump box / bastion host
  physical_security_np   -> biometrics, security cameras, bollards, asset tags,
                            tamper detection
"""

QUESTIONS = [
    # ===== 4.0 Network Security — security_concepts_np ======================
    {
        "id": "netplus-nsec-101", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 3, "type": "mcq",
        "stem": "A network team needs a AAA protocol for device administration that encrypts the "
                "ENTIRE packet payload and separates authentication, authorization, and accounting "
                "so individual CLI commands can be authorized per administrator. Which protocol "
                "BEST fits?",
        "options": [
            {"id": "A", "text": "TACACS+"},
            {"id": "B", "text": "RADIUS"},
            {"id": "C", "text": "Kerberos"},
            {"id": "D", "text": "LDAP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TACACS+ (TCP 49) encrypts the full packet body and treats authentication, "
                       "authorization, and accounting as independent functions, which is why it is "
                       "preferred for device administration and granular per-command authorization.",
            "distractors": {
                "B": "RADIUS encrypts only the password in the Access-Request (not the whole packet), "
                     "combines authentication and authorization, and uses UDP; it is common for network "
                     "access (e.g., 802.1X) rather than per-command device admin.",
                "C": "Kerberos is a ticket-based SSO authentication system, not a device-administration "
                     "AAA protocol with per-command authorization.",
                "D": "LDAP queries a directory for identity/attribute lookups; it is not an AAA protocol "
                     "that authorizes administrative commands.",
            },
            "exam_pattern": "Encrypts the whole packet + separates A/A/A + per-command device admin = TACACS+ "
                            "(TCP 49). Encrypts only the password + combines authn/authz + UDP = RADIUS.",
        },
    },
    {
        "id": "netplus-nsec-102", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "A security architecture assumes NO device or user is trusted by default — even on the "
                "internal LAN — and continuously verifies identity and posture for every access request "
                "before granting the minimum access needed. Which concept is being described?",
        "options": [
            {"id": "A", "text": "Zero trust"},
            {"id": "B", "text": "Implicit trust based on network location"},
            {"id": "C", "text": "Defense in depth"},
            {"id": "D", "text": "Screened subnet (DMZ)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Zero trust removes implicit trust tied to network location and requires continuous "
                       "verification (identity, device posture, policy) for every request, granting only "
                       "least-privilege access — 'never trust, always verify.'",
            "distractors": {
                "B": "Trusting a host simply because it sits inside the perimeter is exactly the legacy model "
                     "zero trust replaces.",
                "C": "Defense in depth layers multiple controls, but it does not by itself mandate per-request "
                     "verification with no implicit trust; it is a complementary idea, not the one described.",
                "D": "A screened subnet (DMZ) is a segmentation zone for public-facing servers, not an "
                     "access-trust model.",
            },
            "exam_pattern": "'Never trust, always verify,' no trust by location, continuous verification + least "
                            "privilege = zero trust.",
        },
    },
    {
        "id": "netplus-nsec-103", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "Near a company office, an attacker stands up a wireless access point broadcasting the "
                "SAME SSID as the corporate WLAN, hoping employee devices associate to it so their "
                "traffic can be intercepted. Which attack is this?",
        "options": [
            {"id": "A", "text": "Evil twin"},
            {"id": "B", "text": "Deauthentication attack"},
            {"id": "C", "text": "Rogue DHCP server"},
            {"id": "D", "text": "DNS poisoning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An evil twin is a malicious access point that impersonates a legitimate SSID so "
                       "victims connect to it, letting the attacker capture or manipulate their traffic.",
            "distractors": {
                "B": "A deauthentication attack sends spoofed 802.11 deauth frames to knock clients off a "
                     "network; it can precede an evil twin but is not the impersonating AP itself.",
                "C": "A rogue DHCP server hands out malicious IP configuration on a wired/wireless segment; "
                     "it does not impersonate an SSID to lure associations.",
                "D": "DNS poisoning corrupts name-resolution responses to redirect by hostname, not by "
                     "spoofing a Wi-Fi SSID.",
            },
            "exam_pattern": "Malicious AP broadcasting a legitimate SSID to lure clients = evil twin.",
        },
    },
    {
        "id": "netplus-nsec-104", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 3, "type": "mcq",
        "stem": "From an access port in VLAN 10, an attacker crafts a frame with TWO stacked 802.1Q "
                "tags. The first switch strips the outer (native VLAN) tag and forwards the frame on a "
                "trunk; the inner tag then steers it into VLAN 20, which the attacker should not reach. "
                "Which attack is this?",
        "options": [
            {"id": "A", "text": "VLAN hopping via double tagging"},
            {"id": "B", "text": "MAC flooding"},
            {"id": "C", "text": "ARP spoofing"},
            {"id": "D", "text": "DHCP starvation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Double-tagging VLAN hopping abuses the native VLAN: the first switch removes the "
                       "outer tag and the remaining inner tag delivers the frame into a VLAN the attacker "
                       "is not a member of.",
            "distractors": {
                "B": "MAC flooding overwhelms the switch CAM table to force unknown-unicast flooding; it "
                     "does not use stacked tags to cross VLANs.",
                "C": "ARP spoofing forges IP-to-MAC bindings for on-path interception, operating within a "
                     "VLAN rather than hopping between VLANs via tagging.",
                "D": "DHCP starvation exhausts a DHCP scope with spoofed requests; it is an availability "
                     "attack on addressing, not VLAN traversal.",
            },
            "exam_pattern": "Stacked 802.1Q tags exploiting the native VLAN = double-tagging VLAN hopping. "
                            "Mitigate by assigning the native VLAN to an unused VLAN and disabling auto-trunking.",
        },
    },
    {
        "id": "netplus-nsec-105", "exam": "netplus", "domain": "network_security",
        "subtopic": "security_concepts_np", "difficulty": 2, "type": "mcq",
        "stem": "A company hosts public web and email servers that Internet users must reach, but it does "
                "NOT want inbound Internet traffic to touch the internal LAN. Where should these servers "
                "be placed?",
        "options": [
            {"id": "A", "text": "In a screened subnet (DMZ) between the Internet and the internal network"},
            {"id": "B", "text": "On the internal user LAN alongside workstations"},
            {"id": "C", "text": "Directly on the Internet with public IPs and no firewall"},
            {"id": "D", "text": "On the out-of-band management network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A screened subnet (DMZ) is an isolated segment for public-facing servers: firewall "
                       "policy permits the needed inbound traffic to the DMZ while blocking that traffic from "
                       "reaching the trusted internal LAN.",
            "distractors": {
                "B": "Placing public servers on the internal LAN exposes workstations and internal resources "
                     "to Internet-originated traffic — the opposite of the requirement.",
                "C": "Putting servers directly on the Internet with no firewall removes all protection and "
                     "segmentation.",
                "D": "The out-of-band management network is a protected admin-only path for managing devices, "
                     "not a place to publish public services.",
            },
            "exam_pattern": "Public-facing servers reachable from the Internet but isolated from the LAN = "
                            "screened subnet (DMZ).",
        },
    },

    # ===== 4.0 Network Security — network_hardening =========================
    {
        "id": "netplus-nsec-106", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Clients on an access switch intermittently receive IP addresses and a default gateway "
                "from an unauthorized device plugged into a user port. The admin wants the switch to "
                "accept DHCP server replies (OFFER/ACK) ONLY from the uplink toward the real DHCP server "
                "and drop them on all user ports. Which feature does this?",
        "options": [
            {"id": "A", "text": "DHCP snooping"},
            {"id": "B", "text": "Dynamic ARP inspection"},
            {"id": "C", "text": "Port security"},
            {"id": "D", "text": "BPDU guard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DHCP snooping marks ports as trusted or untrusted; DHCP server messages are permitted "
                       "only on trusted ports (the legitimate uplink) and dropped on untrusted user ports, "
                       "defeating rogue DHCP servers. It also builds a binding table of IP-to-MAC/port.",
            "distractors": {
                "B": "Dynamic ARP inspection validates ARP packets against the snooping binding table; it "
                     "mitigates ARP spoofing, not rogue DHCP replies.",
                "C": "Port security restricts which MAC addresses may use a port; it does not distinguish "
                     "legitimate from rogue DHCP server traffic.",
                "D": "BPDU guard protects spanning tree by disabling a port that receives unexpected BPDUs; "
                     "it is unrelated to DHCP.",
            },
            "exam_pattern": "Block rogue DHCP by trusting only the real server's port = DHCP snooping "
                            "(it also feeds the binding table used by DAI and IP Source Guard).",
        },
    },
    {
        "id": "netplus-nsec-107", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 3, "type": "mcq",
        "stem": "After an ARP spoofing incident, a network engineer wants switches to intercept ARP "
                "packets on untrusted ports and DROP any whose IP-to-MAC binding does not match a known-"
                "good table. Which feature provides this, and what does it depend on?",
        "options": [
            {"id": "A", "text": "Dynamic ARP inspection, using the DHCP snooping binding table"},
            {"id": "B", "text": "DHCP snooping alone"},
            {"id": "C", "text": "An extended ACL applied to the SVI"},
            {"id": "D", "text": "Port security with sticky MAC learning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dynamic ARP inspection (DAI) validates each ARP packet on untrusted ports against the "
                       "DHCP snooping binding table (or static ARP ACLs) and discards packets with a forged "
                       "IP-to-MAC mapping, stopping ARP spoofing/poisoning.",
            "distractors": {
                "B": "DHCP snooping builds the binding table DAI relies on but does not itself inspect or drop "
                     "ARP packets.",
                "C": "An ACL filters IP traffic by addresses/ports/protocols; ARP is a Layer 2 protocol that "
                     "standard/extended IP ACLs do not evaluate.",
                "D": "Port security limits MAC addresses per port; it does not verify the IP-to-MAC binding "
                     "carried inside ARP messages.",
            },
            "exam_pattern": "Drop forged ARP by checking the IP-to-MAC binding = Dynamic ARP Inspection, which "
                            "depends on the DHCP snooping binding table.",
        },
    },
    {
        "id": "netplus-nsec-108", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 1, "type": "mcq",
        "stem": "To remotely manage switches and routers over an ENCRYPTED session and eliminate "
                "clear-text credentials crossing the network, an administrator should disable Telnet "
                "and enable which protocol?",
        "options": [
            {"id": "A", "text": "SSH"},
            {"id": "B", "text": "HTTP"},
            {"id": "C", "text": "SNMPv2c"},
            {"id": "D", "text": "Telnet on a nonstandard port"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSH (TCP 22) encrypts the entire management session, including credentials, and is the "
                       "secure replacement for Telnet, which sends everything in clear text.",
            "distractors": {
                "B": "HTTP is a clear-text management/web protocol; HTTPS would be the encrypted option, not HTTP.",
                "C": "SNMPv2c is a monitoring protocol and uses clear-text community strings; it is not an "
                     "encrypted interactive management session and does not replace Telnet.",
                "D": "Changing Telnet's port does not add encryption — the session is still clear text and "
                     "credentials remain exposed.",
            },
            "exam_pattern": "Replace clear-text Telnet (TCP 23) with encrypted SSH (TCP 22) for device management.",
        },
    },
    {
        "id": "netplus-nsec-109", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "A technician is hardening a newly installed access switch before connecting it to the "
                "production network. Which TWO actions are hardening best practices? (Choose two.)",
        "options": [
            {"id": "A", "text": "Change the default administrator username and password"},
            {"id": "B", "text": "Administratively disable unused switchports"},
            {"id": "C", "text": "Enable Telnet so remote access is easier"},
            {"id": "D", "text": "Configure SNMPv1 with the community string 'public'"},
            {"id": "E", "text": "Leave every port in the default VLAN 1 for simplicity"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Replacing default credentials removes a well-known, easily guessed entry point, and "
                       "disabling unused ports shrinks the attack surface so an intruder cannot simply plug in "
                       "to an open live port.",
            "distractors": {
                "C": "Telnet is clear text; enabling it weakens the device — SSH should be used instead.",
                "D": "SNMPv1 with the default 'public' community sends clear-text, well-known credentials; "
                     "SNMPv3 (authenticated/encrypted) is the hardened choice.",
                "E": "Leaving hosts in VLAN 1 (the default/native VLAN) is discouraged; unused ports and the "
                     "native VLAN should be moved off VLAN 1 to limit exposure.",
            },
            "exam_pattern": "New-device hardening staples: change default credentials, disable unused ports, "
                            "use SSH/SNMPv3, and avoid default VLAN 1.",
        },
    },
    {
        "id": "netplus-nsec-110", "exam": "netplus", "domain": "network_security",
        "subtopic": "network_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A design requires that administrators can still reach device consoles to manage and "
                "recover equipment even when the production data network is saturated or down. "
                "Management traffic rides a separate, dedicated path via console/management ports. "
                "What is this approach called?",
        "options": [
            {"id": "A", "text": "Out-of-band (OOB) management"},
            {"id": "B", "text": "In-band management"},
            {"id": "C", "text": "Split tunneling"},
            {"id": "D", "text": "Port mirroring (SPAN)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Out-of-band management uses a separate, dedicated channel (console servers, dedicated "
                       "management ports, sometimes a cellular/modem path) so devices remain reachable even if "
                       "the production network is unavailable.",
            "distractors": {
                "B": "In-band management shares the production data network — exactly what fails when that "
                     "network is down or congested.",
                "C": "Split tunneling is a VPN client setting that sends only some traffic through the tunnel; "
                     "it is unrelated to a dedicated management path.",
                "D": "Port mirroring (SPAN) copies traffic to a monitoring port for analysis; it is not a "
                     "management access method.",
            },
            "exam_pattern": "Separate dedicated path that works when the data network is down = out-of-band "
                            "management; sharing the production network = in-band.",
        },
    },

    # ===== 4.0 Network Security — remote_access =============================
    {
        "id": "netplus-nsec-111", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to permanently link the LANs of its headquarters and a branch office "
                "across the Internet so hosts at both sites communicate as if on one network. The tunnel "
                "is terminated by each site's edge firewall/router, not by individual user devices. Which "
                "solution is this?",
        "options": [
            {"id": "A", "text": "A site-to-site VPN"},
            {"id": "B", "text": "A client-to-site (remote-access) VPN"},
            {"id": "C", "text": "A clientless SSL VPN portal"},
            {"id": "D", "text": "A host-to-host (transport-mode) tunnel between two servers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A site-to-site VPN joins two networks through a persistent tunnel between their edge "
                       "gateways; end hosts need no VPN software because the gateways encrypt/decrypt on their "
                       "behalf.",
            "distractors": {
                "B": "A client-to-site VPN connects a single user's device into the network, not two whole "
                     "LANs via their gateways.",
                "C": "A clientless SSL VPN gives an individual user browser-based access to specific apps — "
                     "it does not bridge two site LANs.",
                "D": "A host-to-host tunnel secures traffic between two specific endpoints, not the full LANs "
                     "behind two gateways.",
            },
            "exam_pattern": "Two whole sites joined gateway-to-gateway = site-to-site VPN; a single user's "
                            "device dialing in = client-to-site.",
        },
    },
    {
        "id": "netplus-nsec-112", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 3, "type": "multi", "select_count": 2,
        "stem": "A remote-access VPN is configured for SPLIT tunneling. Which TWO statements correctly "
                "describe its behavior? (Choose two.)",
        "options": [
            {"id": "A", "text": "Traffic destined for corporate subnets is sent through the encrypted VPN tunnel."},
            {"id": "B", "text": "Internet-bound traffic leaves the client's local connection without traversing the corporate gateway."},
            {"id": "C", "text": "All client traffic, including general web browsing, is forced through the corporate network for inspection."},
            {"id": "D", "text": "Split tunneling encrypts the client's traffic at the physical layer."},
            {"id": "E", "text": "Split tunneling blocks the client from reaching any local LAN device such as a home printer."},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "With split tunneling, only traffic bound for corporate resources is routed into the "
                       "encrypted tunnel; everything else (general Internet traffic) exits the client's local "
                       "connection directly, reducing load on the corporate gateway.",
            "distractors": {
                "C": "Forcing ALL traffic through the corporate gateway describes FULL tunneling, the opposite "
                     "of split tunneling.",
                "D": "VPNs protect traffic with encryption at Layer 3 (e.g., IPsec) or the session layer "
                     "(SSL/TLS), not at the physical layer.",
                "E": "Split tunneling actually allows reaching local LAN devices, since local/Internet traffic "
                     "is not pulled into the tunnel.",
            },
            "exam_pattern": "Split tunnel = corporate traffic in the tunnel, Internet traffic direct. "
                            "Full tunnel = everything through the corporate gateway.",
        },
    },
    {
        "id": "netplus-nsec-113", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 3, "type": "mcq",
        "stem": "In an IPsec VPN, which component provides CONFIDENTIALITY by encrypting the packet "
                "payload (in addition to integrity and authentication)?",
        "options": [
            {"id": "A", "text": "Encapsulating Security Payload (ESP)"},
            {"id": "B", "text": "Authentication Header (AH)"},
            {"id": "C", "text": "Internet Key Exchange (IKE)"},
            {"id": "D", "text": "Generic Routing Encapsulation (GRE)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ESP (IP protocol 50) encrypts the payload to provide confidentiality, and can also "
                       "provide integrity and authentication — it is the IPsec component that actually encrypts "
                       "the data.",
            "distractors": {
                "B": "AH (IP protocol 51) provides integrity and authentication only; it does NOT encrypt the "
                     "payload, so it offers no confidentiality.",
                "C": "IKE (UDP 500/4500) negotiates the security associations and keys; it sets up the tunnel "
                     "but is not what encrypts the ongoing data payload.",
                "D": "GRE is a tunneling/encapsulation protocol with no built-in encryption; it needs IPsec to "
                     "add confidentiality.",
            },
            "exam_pattern": "Encryption/confidentiality in IPsec = ESP. AH = integrity/authentication only "
                            "(no encryption). IKE = key exchange / SA negotiation.",
        },
    },
    {
        "id": "netplus-nsec-114", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 1, "type": "mcq",
        "stem": "A help-desk technician needs to connect to the full graphical desktop of a remote "
                "Windows server to run GUI management tools. Which native Microsoft protocol and port "
                "are used?",
        "options": [
            {"id": "A", "text": "RDP over TCP 3389"},
            {"id": "B", "text": "SSH over TCP 22"},
            {"id": "C", "text": "VNC over TCP 5900"},
            {"id": "D", "text": "Telnet over TCP 23"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Remote Desktop Protocol (RDP) is Microsoft's native remote-GUI protocol and listens on "
                       "TCP 3389.",
            "distractors": {
                "B": "SSH (TCP 22) provides an encrypted command-line session, typically to Linux/Unix hosts and "
                     "network devices — not a Windows graphical desktop.",
                "C": "VNC does offer a remote GUI and uses TCP 5900, but it is a cross-platform third-party "
                     "protocol, not Microsoft's native protocol, and it is not on 3389.",
                "D": "Telnet (TCP 23) is an unencrypted text/CLI protocol, not a graphical remote desktop.",
            },
            "exam_pattern": "Windows remote graphical desktop = RDP, TCP 3389. SSH 22 = secure CLI; VNC 5900 = "
                            "cross-platform GUI; Telnet 23 = clear-text CLI.",
        },
    },
    {
        "id": "netplus-nsec-115", "exam": "netplus", "domain": "network_security",
        "subtopic": "remote_access", "difficulty": 2, "type": "mcq",
        "stem": "To administer servers in a protected subnet, administrators must first connect to a "
                "single hardened host positioned between the admin network and the secure zone; all "
                "management sessions are funneled and logged through it. What is this host called?",
        "options": [
            {"id": "A", "text": "A jump box (bastion host)"},
            {"id": "B", "text": "A honeypot"},
            {"id": "C", "text": "A forward proxy server"},
            {"id": "D", "text": "A RADIUS server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A jump box (bastion host) is a single hardened, closely monitored system used as the "
                       "controlled entry point for administering devices in a secure zone, concentrating and "
                       "logging all management access.",
            "distractors": {
                "B": "A honeypot is a decoy system meant to attract and study attackers, not a sanctioned admin "
                     "gateway.",
                "C": "A forward proxy relays user requests (typically outbound web traffic) on their behalf; it "
                     "is not a hardened administrative pivot host.",
                "D": "A RADIUS server performs AAA for network access; it authenticates users but is not the "
                     "pivot host through which admins connect.",
            },
            "exam_pattern": "Single hardened pivot/entry host for reaching a secure zone = jump box / bastion host.",
        },
    },

    # ===== 4.0 Network Security — physical_security_np ======================
    {
        "id": "netplus-nsec-116", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "A server-room door is secured with a fingerprint scanner, so entry depends on a "
                "physical trait that cannot be lost, shared, or easily duplicated. This access control "
                "is BEST described as which authentication factor?",
        "options": [
            {"id": "A", "text": "Biometric — something you are"},
            {"id": "B", "text": "Proximity card — something you have"},
            {"id": "C", "text": "PIN/cipher lock — something you know"},
            {"id": "D", "text": "Asset tag — something you are assigned"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A fingerprint (or retina/face) scanner is biometric authentication — the 'something you "
                       "are' factor — tied to a unique physical trait that cannot be handed to someone else.",
            "distractors": {
                "B": "A proximity card is 'something you have'; it can be lost, stolen, or cloned, so it is not "
                     "the trait-based factor described.",
                "C": "A PIN or cipher-lock code is 'something you know' and can be shared or shoulder-surfed.",
                "D": "An asset tag labels equipment for inventory; it is not a personal authentication factor at "
                     "all.",
            },
            "exam_pattern": "Fingerprint/retina/face at a door = biometric, the 'something you are' factor.",
        },
    },
    {
        "id": "netplus-nsec-117", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "Management wants to continuously monitor and RECORD who is physically present at the "
                "data center entrances so any incident can be reviewed afterward. Which physical security "
                "control BEST meets this need?",
        "options": [
            {"id": "A", "text": "Security cameras (CCTV/video surveillance)"},
            {"id": "B", "text": "An access control vestibule (mantrap)"},
            {"id": "C", "text": "Motion-activated security lighting"},
            {"id": "D", "text": "Bollards at the entrance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Security cameras (CCTV) continuously capture and store video of entrances, providing a "
                       "detective record that can be reviewed after an incident (and a visible deterrent).",
            "distractors": {
                "B": "An access control vestibule prevents tailgating by admitting one person at a time, but it "
                     "does not create a reviewable visual record of who was present.",
                "C": "Motion-activated lighting improves visibility and deters intruders but records nothing for "
                     "later review.",
                "D": "Bollards block vehicles from an entrance; they neither monitor nor record people.",
            },
            "exam_pattern": "Continuously record/monitor who is present for later review = security cameras (CCTV).",
        },
    },
    {
        "id": "netplus-nsec-118", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 2, "type": "mcq",
        "stem": "A facility wants to stop a vehicle from being driven through the glass doors of its "
                "lobby entrance while still allowing pedestrians to walk through. Which physical control "
                "is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Bollards"},
            {"id": "B", "text": "Perimeter fencing"},
            {"id": "C", "text": "Security lighting"},
            {"id": "D", "text": "An access control vestibule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bollards are short, sturdy posts set in front of an entrance to physically block vehicles "
                       "from ramming through while still letting people walk between them.",
            "distractors": {
                "B": "Perimeter fencing marks and deters access at the property boundary but is not what protects "
                     "a specific pedestrian doorway from a vehicle.",
                "C": "Security lighting improves visibility and deters intruders; it provides no physical barrier "
                     "to a vehicle.",
                "D": "An access control vestibule controls people tailgating through a door — it is not designed "
                     "to stop a vehicle.",
            },
            "exam_pattern": "Stop a vehicle at an entrance while allowing foot traffic = bollards.",
        },
    },
    {
        "id": "netplus-nsec-119", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 1, "type": "mcq",
        "stem": "An IT department attaches scannable RFID/barcode labels to every switch, router, and "
                "laptop so equipment can be inventoried and, if it leaves the building, identified as "
                "company property. What are these labels called?",
        "options": [
            {"id": "A", "text": "Asset tags"},
            {"id": "B", "text": "Tamper-evident seals"},
            {"id": "C", "text": "Smart lockers"},
            {"id": "D", "text": "Proximity badges"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Asset tags are labels (often RFID or barcode) applied to equipment for inventory tracking "
                       "and to mark ownership, aiding accountability and theft identification.",
            "distractors": {
                "B": "Tamper-evident seals reveal whether a device has been opened or tampered with — a different "
                     "purpose from inventory/ownership tracking.",
                "C": "Smart lockers securely store or hand off devices/packages; they are not labels affixed to "
                     "equipment.",
                "D": "Proximity badges authenticate people at doors; they do not inventory equipment.",
            },
            "exam_pattern": "Labels for inventory and ownership tracking of equipment = asset tags.",
        },
    },
    {
        "id": "netplus-nsec-120", "exam": "netplus", "domain": "network_security",
        "subtopic": "physical_security_np", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to know whether anyone has physically OPENED the chassis of a deployed "
                "network appliance in a remote closet. Which control BEST provides this?",
        "options": [
            {"id": "A", "text": "Tamper detection (tamper-evident seals/sensors)"},
            {"id": "B", "text": "An asset tag"},
            {"id": "C", "text": "A cable lock"},
            {"id": "D", "text": "A proximity card reader on the closet door"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tamper detection — tamper-evident seals or tamper switches/sensors — makes unauthorized "
                       "opening of a device visible or logs it, so technicians can tell the chassis was accessed.",
            "distractors": {
                "B": "An asset tag identifies ownership and aids inventory; it does not indicate whether the "
                     "device was opened.",
                "C": "A cable lock deters theft of the device but does not reveal that the chassis was opened.",
                "D": "A card reader controls who enters the closet; it does not detect tampering with the device "
                     "itself once someone is inside.",
            },
            "exam_pattern": "Reveal that a device chassis was opened = tamper detection (seals/sensors).",
        },
    },
]
