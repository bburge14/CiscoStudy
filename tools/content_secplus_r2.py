"""CompTIA Security+ SY0-701 item pool — round 2 deepening (original items).

Same authoring rules as the base pool (tools/content_secplus.py): original
content mapped to the public exam objectives, never real exam items. Each item
keys ONE correct answer (or >=2 for multi), and every wrong option carries a
distractor note explaining the trap. build_content.py shuffles option order
(seeded by id), so the answer key here is not positionally biased.

IDs use the `-r2-` infix so they can never collide with the base pool or the
per-domain expansion pools. domabbrev matches the base file: gsc, tvm, arch,
ops, mgmt.
"""

QUESTIONS = [
    # ===== 1.0 General Security Concepts =====================================
    {
        "id": "secplus-gsc-r2-001", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "Running the annual security-awareness training and performing employee "
                "background checks are examples of which control CATEGORY?",
        "options": [
            {"id": "A", "text": "Operational"},
            {"id": "B", "text": "Managerial"},
            {"id": "C", "text": "Technical"},
            {"id": "D", "text": "Physical"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Operational controls are carried out primarily by PEOPLE as part of day-to-day "
                       "operations — awareness training, background checks, and access reviews are operational.",
            "distractors": {
                "B": "Managerial (administrative) controls are strategic — risk assessments, policies, "
                     "and security planning — not the hands-on execution.",
                "C": "Technical (logical) controls are implemented by technology (firewalls, encryption, MFA).",
                "D": "Physical controls are tangible barriers (locks, guards, fences, bollards).",
            },
            "exam_pattern": "Category = who/what implements it: managerial (policy/risk planning), "
                            "operational (people doing day-to-day), technical (tech enforces), physical (tangible barrier).",
        },
    },
    {
        "id": "secplus-gsc-r2-002", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A motion-activated camera records and sends the SOC an alert the moment someone "
                "enters a restricted area after hours. Which control TYPE is the camera acting as here?",
        "options": [
            {"id": "A", "text": "Detective"},
            {"id": "B", "text": "Preventive"},
            {"id": "C", "text": "Corrective"},
            {"id": "D", "text": "Compensating"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recording and alerting IDENTIFIES activity as it happens — a detective control. "
                       "(The camera's visible presence can also deter, but the record-and-alert function is detection.)",
            "distractors": {
                "B": "Preventive controls STOP an event before it happens (a locked door, a firewall rule); "
                     "the camera does not block entry.",
                "C": "Corrective controls act after an incident to restore/repair (e.g., restoring from backup).",
                "D": "Compensating controls are substitutes used when the primary control is not feasible.",
            },
            "exam_pattern": "Type = what it DOES vs the event: preventive/deterrent (before), detective "
                            "(identifies during/after), corrective (fixes after), compensating (stand-in), directive (instructs).",
        },
    },
    {
        "id": "secplus-gsc-r2-003", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 1, "type": "mcq",
        "stem": "An e-commerce site uses redundant servers and load balancing so it stays reachable "
                "even if one server crashes during a sale. Which part of the CIA triad does this protect?",
        "options": [
            {"id": "A", "text": "Availability"},
            {"id": "B", "text": "Confidentiality"},
            {"id": "C", "text": "Integrity"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Availability ensures authorized users can reach systems/data when needed; redundancy, "
                       "load balancing, and failover are classic availability controls.",
            "distractors": {
                "B": "Confidentiality keeps data secret from unauthorized parties (encryption, access control).",
                "C": "Integrity ensures data is accurate and unaltered (hashing, digital signatures).",
                "D": "Non-repudiation proves who performed an action and is not part of the CIA triad.",
            },
            "exam_pattern": "CIA: Confidentiality (secrecy), Integrity (unaltered), Availability (accessible). "
                            "Redundancy/backup/failover/load balancing → availability.",
        },
    },
    {
        "id": "secplus-gsc-r2-004", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 2, "type": "mcq",
        "stem": "A user types a username and then a password; the system confirms the password matches "
                "the stored credential for that account before any access is granted. Which step is the "
                "password check performing?",
        "options": [
            {"id": "A", "text": "Authentication"},
            {"id": "B", "text": "Identification"},
            {"id": "C", "text": "Authorization"},
            {"id": "D", "text": "Accounting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Authentication is PROVING a claimed identity — verifying the password (something you "
                       "know) matches the stored credential.",
            "distractors": {
                "B": "Identification is merely CLAIMING an identity (typing the username); it is not proof.",
                "C": "Authorization happens AFTER authentication and decides what the user may access.",
                "D": "Accounting records what the authenticated user did (an audit trail).",
            },
            "exam_pattern": "Identify (claim) -> Authenticate (prove) -> Authorize (permit) -> Account (log). "
                            "Verifying a credential = authentication.",
        },
    },
    {
        "id": "secplus-gsc-r2-005", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "In a Zero Trust architecture, a gateway sits in the traffic path to a protected "
                "resource and, acting on the decision relayed from the control plane, opens or drops "
                "each connection. Which component is this?",
        "options": [
            {"id": "A", "text": "Policy Enforcement Point (PEP)"},
            {"id": "B", "text": "Policy Engine (PE)"},
            {"id": "C", "text": "Policy Administrator (PA)"},
            {"id": "D", "text": "Subject"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Policy Enforcement Point, in the DATA plane, allows, monitors, and terminates "
                       "connections to the resource according to the control plane's decision.",
            "distractors": {
                "B": "The Policy Engine (control plane) MAKES the grant/deny decision; it does not sit in the traffic path.",
                "C": "The Policy Administrator (control plane) relays the decision and sets up/tears down the "
                     "session, but the PEP is the enforcement gateway.",
                "D": "The Subject is the user/device requesting access, not an enforcement component.",
            },
            "exam_pattern": "Control plane = Policy Engine (decides) + Policy Administrator (relays/sets up); "
                            "data plane = Policy Enforcement Point (allows/blocks/monitors the actual connection).",
        },
    },
    {
        "id": "secplus-gsc-r2-006", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "physical_security", "difficulty": 3, "type": "mcq",
        "stem": "A warehouse needs a motion sensor that covers a large open area and can detect movement "
                "even through thin, non-metallic partitions by emitting radio energy and measuring the "
                "reflection. Which sensor fits BEST?",
        "options": [
            {"id": "A", "text": "Microwave sensor"},
            {"id": "B", "text": "Infrared (PIR) sensor"},
            {"id": "C", "text": "Pressure sensor"},
            {"id": "D", "text": "Ultrasonic sensor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microwave sensors emit radio waves and detect motion from changes in the reflected "
                       "signal; they cover large areas and can sense through thin non-metal materials.",
            "distractors": {
                "B": "A passive infrared (PIR) sensor detects a moving body's HEAT within line of sight and cannot see through walls.",
                "C": "A pressure sensor triggers on weight/force applied to a surface (e.g., a floor mat), not open-area motion.",
                "D": "An ultrasonic sensor uses high-frequency SOUND waves and is typically shorter-range and more affected by obstacles.",
            },
            "exam_pattern": "Sensors: infrared (body heat, line of sight), microwave (radio reflection, large area/thin walls), "
                            "ultrasonic (sound), pressure (weight/force).",
        },
    },
    {
        "id": "secplus-gsc-r2-007", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "change_management", "difficulty": 1, "type": "mcq",
        "stem": "A core-switch upgrade is scheduled for 2:00 a.m. Sunday, the period of lowest business "
                "activity, so any disruption affects the fewest users. What is this pre-approved period called?",
        "options": [
            {"id": "A", "text": "Maintenance window"},
            {"id": "B", "text": "Backout plan"},
            {"id": "C", "text": "Change freeze"},
            {"id": "D", "text": "Service-level agreement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A maintenance window is a scheduled, approved time — usually during low activity — "
                       "for performing changes so impact is minimized.",
            "distractors": {
                "B": "A backout (rollback) plan is the documented way to UNDO the change if it fails, not the time it runs.",
                "C": "A change freeze is a period during which NO changes are allowed (e.g., end-of-quarter).",
                "D": "An SLA defines service commitments between parties, not a change's scheduled time.",
            },
            "exam_pattern": "Change-management terms: maintenance window (when), backout plan (how to undo), "
                            "impact analysis (what could break), approval/CAB (who signs off).",
        },
    },
    {
        "id": "secplus-gsc-r2-008", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise needs a dedicated, tamper-resistant appliance to GENERATE, store, and "
                "manage cryptographic keys for many servers and to offload bulk encryption operations. "
                "Which solution is designed for this?",
        "options": [
            {"id": "A", "text": "Hardware Security Module (HSM)"},
            {"id": "B", "text": "Trusted Platform Module (TPM)"},
            {"id": "C", "text": "Key Distribution Center (KDC)"},
            {"id": "D", "text": "Certificate Signing Request (CSR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An HSM is a dedicated, tamper-resistant device (appliance or card) for enterprise-scale "
                       "key generation, storage, management, and crypto acceleration across many systems.",
            "distractors": {
                "B": "A TPM is a chip bound to a SINGLE host (e.g., for that machine's disk-encryption keys), "
                     "not a multi-server enterprise key manager.",
                "C": "A KDC issues tickets in Kerberos authentication; it is not a key-storage appliance.",
                "D": "A CSR is a request sent to a CA to obtain a certificate, not a key-management device.",
            },
            "exam_pattern": "TPM = per-device chip (one machine's keys); HSM = enterprise, tamper-resistant key "
                            "manager/accelerator for many systems.",
        },
    },
    {
        "id": "secplus-gsc-r2-009", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 3, "type": "mcq",
        "stem": "To slow down offline brute-force cracking of stored password hashes, developers run each "
                "password through a deliberately slow, repeated hashing function such as bcrypt, PBKDF2, "
                "or Argon2. What is this technique called?",
        "options": [
            {"id": "A", "text": "Key stretching"},
            {"id": "B", "text": "Salting"},
            {"id": "C", "text": "Steganography"},
            {"id": "D", "text": "Key escrow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Key stretching repeatedly hashes (and salts) a low-entropy secret with a purposely "
                       "expensive function so each guess costs an attacker far more time — bcrypt/PBKDF2/Argon2 are built for it.",
            "distractors": {
                "B": "Salting adds a unique random value so identical passwords hash differently and defeats "
                     "precomputed (rainbow-table) attacks; it is often combined with stretching but does not add CPU cost per guess.",
                "C": "Steganography hides data inside other media (images, audio).",
                "D": "Key escrow stores a copy of keys with a third party for recovery.",
            },
            "exam_pattern": "Salt (unique value -> stops precomputation) + key stretching (slow, repeated hashing "
                            "-> raises per-guess cost). bcrypt/PBKDF2/Argon2 = key-stretching functions.",
        },
    },
    {
        "id": "secplus-gsc-r2-010", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "mcq",
        "stem": "A company wants ONE certificate that secures its main domain and ANY current or future "
                "subdomain under it (shop.example.com, mail.example.com, vpn.example.com, ...) without "
                "reissuing. Which certificate type fits BEST?",
        "options": [
            {"id": "A", "text": "Wildcard certificate (*.example.com)"},
            {"id": "B", "text": "Self-signed certificate"},
            {"id": "C", "text": "Code-signing certificate"},
            {"id": "D", "text": "Root CA certificate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A wildcard certificate (CN/SAN of *.example.com) secures the domain and all first-level "
                       "subdomains with a single cert, so new subdomains need no reissue.",
            "distractors": {
                "B": "A self-signed certificate is not issued by a trusted CA and browsers will not trust it by default.",
                "C": "A code-signing certificate signs software, not web hosts.",
                "D": "A root CA certificate is the trust anchor used to sign other certificates, not to secure a website's subdomains.",
            },
            "exam_pattern": "Wildcard (*.domain) = all first-level subdomains, one cert. SAN cert = several "
                            "specific, possibly DIFFERENT names/domains listed explicitly.",
        },
    },
    {
        "id": "secplus-gsc-r2-011", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "mcq",
        "stem": "A certificate authority periodically publishes a digitally signed file listing the serial "
                "numbers of all certificates it has revoked before their expiration, which clients can "
                "download and cache. What is this mechanism?",
        "options": [
            {"id": "A", "text": "Certificate Revocation List (CRL)"},
            {"id": "B", "text": "Online Certificate Status Protocol (OCSP)"},
            {"id": "C", "text": "Certificate Signing Request (CSR)"},
            {"id": "D", "text": "Key escrow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CRL is a CA-signed, periodically published list of revoked certificate serial numbers; "
                       "clients download it to check whether a certificate is still valid.",
            "distractors": {
                "B": "OCSP checks the status of a SINGLE certificate in REAL TIME via a responder query, rather "
                     "than downloading a whole list — lighter and more current than a CRL.",
                "C": "A CSR requests a new certificate from a CA.",
                "D": "Key escrow stores keys for recovery; it has nothing to do with revocation status.",
            },
            "exam_pattern": "Revocation: CRL (full signed list, periodically downloaded, can be stale) vs OCSP "
                            "(real-time, single-cert query); OCSP stapling has the server present a time-stamped status.",
        },
    },
    # ===== 2.0 Threats, Vulnerabilities & Mitigations =======================
    {
        "id": "secplus-tvm-r2-001", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_vectors", "difficulty": 2, "type": "mcq",
        "stem": "Sales staff routinely connect their laptops to free, open (unencrypted) Wi-Fi at airports "
                "and cafes. An attacker on the same network captures their unencrypted traffic. Which THREAT "
                "VECTOR does this exploit?",
        "options": [
            {"id": "A", "text": "Unsecure network"},
            {"id": "B", "text": "Supply chain"},
            {"id": "C", "text": "Default credentials"},
            {"id": "D", "text": "Removable media"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Connecting over an open, unencrypted wireless network is an unsecure-network vector — "
                       "nearby attackers can eavesdrop or run on-path attacks. Mitigate with a VPN and TLS everywhere.",
            "distractors": {
                "B": "A supply-chain vector is abuse via a trusted vendor/MSP or a tampered component, not public Wi-Fi.",
                "C": "Default credentials is leaving vendor-set logins (e.g., admin/admin) in place.",
                "D": "Removable media is a USB/external-drive vector.",
            },
            "exam_pattern": "Threat VECTOR = the path in. Open/rogue Wi-Fi = unsecure network -> VPN + TLS; "
                            "USB drop = removable media; vendor compromise = supply chain.",
        },
    },
    {
        "id": "secplus-tvm-r2-002", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker crafts a highly tailored email aimed specifically at a company's CFO, "
                "referencing a genuine pending acquisition, to trick that executive into authorizing a "
                "wire transfer. Which social-engineering attack is this?",
        "options": [
            {"id": "A", "text": "Whaling"},
            {"id": "B", "text": "Smishing"},
            {"id": "C", "text": "Shoulder surfing"},
            {"id": "D", "text": "Watering-hole attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Whaling is spear phishing aimed at a HIGH-VALUE executive ('big fish') such as a CEO or "
                       "CFO, using tailored, credible details to exploit their authority.",
            "distractors": {
                "B": "Smishing is phishing delivered by SMS text message.",
                "C": "Shoulder surfing is observing someone's screen/keypad to steal information.",
                "D": "A watering-hole attack compromises a website the target group is known to visit.",
            },
            "exam_pattern": "Phishing (broad) -> spear phishing (targeted) -> whaling (targeted at a senior "
                            "executive). Channel variants: vishing (voice), smishing (SMS).",
        },
    },
    {
        "id": "secplus-tvm-r2-003", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "malware", "difficulty": 2, "type": "mcq",
        "stem": "A disgruntled administrator inserts hidden code into a production server that will delete "
                "all payroll records automatically IF his own user account is ever disabled. Which type of "
                "malicious code is this?",
        "options": [
            {"id": "A", "text": "Logic bomb"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Ransomware"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A logic bomb is dormant code that triggers a malicious payload when a specific CONDITION "
                       "or time is met — here, the admin's account being disabled.",
            "distractors": {
                "B": "A worm self-propagates across hosts over a network; it is not a conditional trigger.",
                "C": "Ransomware encrypts data and demands payment.",
                "D": "A rootkit hides at a privileged level to maintain stealthy access.",
            },
            "exam_pattern": "Condition/time trigger = logic bomb; self-spread = worm; encrypt+extort = ransomware; "
                            "hide/privilege = rootkit; disguised installer = trojan.",
        },
    },
    {
        "id": "secplus-tvm-r2-004", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "In an airport, an attacker stands up a rogue Wi-Fi access point broadcasting the SAME SSID "
                "as the legitimate airport network, so victims associate to it and the attacker intercepts "
                "their traffic. Which attack is this?",
        "options": [
            {"id": "A", "text": "Evil twin"},
            {"id": "B", "text": "ARP poisoning"},
            {"id": "C", "text": "DNS cache poisoning"},
            {"id": "D", "text": "SYN flood"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An evil twin is a rogue access point impersonating a legitimate SSID to lure clients "
                       "into connecting, enabling eavesdropping and on-path attacks. WPA3, validating networks, and VPN use mitigate it.",
            "distractors": {
                "B": "ARP poisoning forges ARP replies on a local LAN to redirect traffic — not a rogue wireless AP.",
                "C": "DNS cache poisoning injects false records into a resolver's cache.",
                "D": "A SYN flood is a denial-of-service that exhausts half-open TCP connections.",
            },
            "exam_pattern": "Rogue AP with a spoofed/duplicate SSID = evil twin (wireless on-path). LAN redirect "
                            "via forged ARP = ARP poisoning.",
        },
    },
    {
        "id": "secplus-tvm-r2-005", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "application_attacks", "difficulty": 3, "type": "mcq",
        "stem": "A web form passes a user-supplied value straight into an operating-system shell command. "
                "An attacker enters '; cat /etc/passwd' and the server runs it, returning the file. Which "
                "attack is this?",
        "options": [
            {"id": "A", "text": "OS command injection"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Cross-site scripting (XSS)"},
            {"id": "D", "text": "Cross-site request forgery (CSRF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OS command injection occurs when unsanitized input is passed to a system shell, letting "
                       "the attacker run arbitrary OS commands. Fix with strict input validation/allow-listing and safe APIs (avoid shell calls).",
            "distractors": {
                "B": "SQL injection targets a DATABASE query (e.g., ' OR '1'='1), not the OS shell.",
                "C": "XSS injects script that runs in other users' BROWSERS.",
                "D": "CSRF tricks an authenticated user's browser into submitting an unwanted request; it does not run server-side OS commands.",
            },
            "exam_pattern": "Input reaches a shell = command injection; a SQL query = SQLi; a victim's browser = "
                            "XSS. Defense for all: validate/encode input, least privilege.",
        },
    },
    {
        "id": "secplus-tvm-r2-006", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "vulnerability_types", "difficulty": 2, "type": "mcq",
        "stem": "A review finds a public web server deployed with directory listing enabled, verbose error "
                "messages exposed, and the vendor's default admin account still active. Which category of "
                "vulnerability do these findings represent?",
        "options": [
            {"id": "A", "text": "Misconfiguration"},
            {"id": "B", "text": "Zero-day vulnerability"},
            {"id": "C", "text": "Race condition"},
            {"id": "D", "text": "Buffer overflow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "These are classic misconfigurations — insecure defaults and sloppy hardening that expose "
                       "the system. Remediate with secure baselines/hardening and by disabling defaults.",
            "distractors": {
                "B": "A zero-day is an unknown flaw with no patch available — these issues are known, avoidable settings.",
                "C": "A race condition (e.g., TOCTOU) exploits timing between a check and a use.",
                "D": "A buffer overflow overwrites memory via oversized input to a fixed buffer.",
            },
            "exam_pattern": "Default creds + unneeded features + exposed errors = misconfiguration -> apply a "
                            "secure baseline/hardening checklist.",
        },
    },
    {
        "id": "secplus-tvm-r2-007", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "mitigation_techniques", "difficulty": 2, "type": "multi",
        "stem": "A company wants to limit the damage if a single user's password is phished. Which TWO "
                "mitigations MOST directly reduce the impact of one compromised credential? (Choose two.)",
        "options": [
            {"id": "A", "text": "Require multifactor authentication (MFA)"},
            {"id": "B", "text": "Enforce least-privilege access"},
            {"id": "C", "text": "Increase the password maximum age"},
            {"id": "D", "text": "Disable the host firewall"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "MFA means a stolen password alone is not enough to log in (the attacker still lacks the "
                       "second factor), and least privilege limits what any one compromised account can reach or do.",
            "distractors": {
                "C": "Increasing the maximum password AGE lets passwords live LONGER before rotation, which does "
                     "not reduce the impact of a compromise.",
                "D": "Disabling the host firewall removes a protection and widens exposure.",
            },
            "exam_pattern": "Contain a single-credential compromise with MFA (blocks reuse) + least privilege "
                            "(limits blast radius). Segmentation and monitoring help too.",
        },
    },
    # ===== 3.0 Security Architecture ========================================
    {
        "id": "secplus-arch-r2-001", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 2, "type": "mcq",
        "stem": "A data-center network uses a central controller that computes forwarding decisions and "
                "pushes them to switches through APIs, separating the control plane from the data plane. "
                "Which architecture model is this?",
        "options": [
            {"id": "A", "text": "Software-defined networking (SDN)"},
            {"id": "B", "text": "Serverless computing"},
            {"id": "C", "text": "Microservices"},
            {"id": "D", "text": "Infrastructure as code (IaC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SDN decouples the control plane (a centralized controller making forwarding decisions) "
                       "from the data plane (switches forwarding traffic), programmed via APIs for agility and central policy.",
            "distractors": {
                "B": "Serverless runs event-driven functions without managing servers — a compute model, not network control.",
                "C": "Microservices decompose an APPLICATION into small services.",
                "D": "IaC provisions infrastructure from version-controlled files; it can configure SDN but is not the control/data-plane split itself.",
            },
            "exam_pattern": "SDN = centralized control plane + programmable data plane via APIs. Watch for "
                            "'controller' + 'separates control and data plane'.",
        },
    },
    {
        "id": "secplus-arch-r2-002", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "architecture_models", "difficulty": 2, "type": "mcq",
        "stem": "A smart-building controller is a system-on-chip device running a stripped-down real-time OS "
                "with limited memory; it cannot host an EDR agent and is difficult to patch. Which "
                "characteristic MOST increases its security risk?",
        "options": [
            {"id": "A", "text": "Limited compute and patchability of an embedded system"},
            {"id": "B", "text": "It is a Type 1 hypervisor"},
            {"id": "C", "text": "It is a serverless function"},
            {"id": "D", "text": "It is a container"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Embedded/IoT devices (SoC, RTOS) have constrained compute, often cannot run endpoint "
                       "protection, and are hard or slow to patch — so compensating controls (segmentation, network monitoring) are key.",
            "distractors": {
                "B": "A Type 1 hypervisor runs VMs on bare metal — not a resource-constrained embedded controller.",
                "C": "A serverless function is cloud event-driven code, not a physical SoC device.",
                "D": "A container packages an application to share a host OS kernel; it is not an embedded hardware device.",
            },
            "exam_pattern": "Embedded/IoT/ICS = constrained, weak patch/monitoring story -> isolate on segmented "
                            "networks + compensating controls.",
        },
    },
    {
        "id": "secplus-arch-r2-003", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "A company wants central visibility and policy enforcement (DLP, access rules, threat "
                "protection) between its users and the MANY SaaS applications they use. Which solution sits "
                "between users and cloud services to provide this?",
        "options": [
            {"id": "A", "text": "Cloud Access Security Broker (CASB)"},
            {"id": "B", "text": "Host-based IDS"},
            {"id": "C", "text": "Local disk encryption"},
            {"id": "D", "text": "Jump server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CASB sits between users and cloud/SaaS providers (inline or via API) to enforce "
                       "visibility, access policy, DLP, and threat protection across cloud usage.",
            "distractors": {
                "B": "A host-based IDS monitors a single host's activity, not cloud-service usage broadly.",
                "C": "Local disk encryption protects data at rest on a device, not SaaS policy enforcement.",
                "D": "A jump server is a hardened pivot host for administering internal systems.",
            },
            "exam_pattern": "'Policy/visibility between users and cloud/SaaS apps' = CASB. Often paired with SSO and DLP.",
        },
    },
    {
        "id": "secplus-arch-r2-004", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "Under the shared responsibility model for a Software-as-a-Service (SaaS) application, which "
                "task remains the CUSTOMER's responsibility?",
        "options": [
            {"id": "A", "text": "Managing user accounts, access, and data in the application"},
            {"id": "B", "text": "Patching the application code"},
            {"id": "C", "text": "Securing the hypervisor and physical hosts"},
            {"id": "D", "text": "Maintaining the underlying operating system"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With SaaS, the provider runs the app, OS, and infrastructure; the customer still owns "
                       "their DATA, user identities/access, and in-app configuration (plus their own endpoints).",
            "distractors": {
                "B": "Patching the application is the SaaS provider's job.",
                "C": "The hypervisor and physical data center are always the provider's responsibility.",
                "D": "The provider maintains the underlying OS in SaaS.",
            },
            "exam_pattern": "More 'as-a-service' = provider owns more. SaaS customer still owns data + "
                            "identity/access + configuration; IaaS adds OS/app/runtime to the customer.",
        },
    },
    {
        "id": "secplus-arch-r2-005", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "To protect a public web application specifically against layer-7 attacks such as SQL "
                "injection and cross-site scripting, a team deploys a device that inspects HTTP/HTTPS "
                "requests and blocks malicious payloads. Which control is this?",
        "options": [
            {"id": "A", "text": "Web Application Firewall (WAF)"},
            {"id": "B", "text": "Traditional stateful network firewall"},
            {"id": "C", "text": "Network IPS at the perimeter"},
            {"id": "D", "text": "Reverse proxy with no inspection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A WAF understands HTTP(S) and application-layer attacks (SQLi, XSS, etc.), filtering or "
                       "blocking malicious requests to a web app — protection a generic firewall cannot provide.",
            "distractors": {
                "B": "A stateful network firewall filters by IP/port/session at L3/L4 and does not parse application payloads for SQLi/XSS.",
                "C": "A network IPS inspects broadly for signatures but is not specialized for a web app's HTTP logic like a WAF.",
                "D": "A plain reverse proxy relays requests and may terminate TLS but, without inspection, does not block app-layer attacks.",
            },
            "exam_pattern": "'Protect a web app from SQLi/XSS at layer 7' = WAF. Generic firewall = L3/L4 ports; "
                            "IPS = network signatures.",
        },
    },
    {
        "id": "secplus-arch-r2-006", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 3, "type": "mcq",
        "stem": "An inline security appliance is configured so that if it loses power or crashes, network "
                "traffic continues to pass THROUGH uninterrupted. Which design is this, and its trade-off?",
        "options": [
            {"id": "A", "text": "Fail-open — favors availability over security"},
            {"id": "B", "text": "Fail-closed — favors security over availability"},
            {"id": "C", "text": "Fault tolerance via clustering"},
            {"id": "D", "text": "Air gap"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fail-open means a failure lets traffic keep flowing — prioritizing AVAILABILITY, at the "
                       "cost of security during the outage (traffic is uninspected/unfiltered).",
            "distractors": {
                "B": "Fail-closed (fail-secure) BLOCKS traffic on failure — prioritizing security over availability; the opposite of what is described.",
                "C": "Clustering adds redundant nodes for fault tolerance; it is not the behavior of a single device on failure.",
                "D": "An air gap physically isolates a network; it is not a failure mode.",
            },
            "exam_pattern": "Fail-open = keep flowing (availability first); fail-closed/fail-secure = block "
                            "(security first). Choose per the asset's priority.",
        },
    },
    {
        "id": "secplus-arch-r2-007", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 3, "type": "mcq",
        "stem": "Remote employees use an encrypted VPN to reach internal systems. Security wants ALL of "
                "their internet-bound traffic to also pass through the corporate gateway for inspection, "
                "not just traffic destined for internal resources. Which VPN configuration achieves this?",
        "options": [
            {"id": "A", "text": "Full tunnel"},
            {"id": "B", "text": "Split tunnel"},
            {"id": "C", "text": "Clientless reverse proxy"},
            {"id": "D", "text": "Site-to-site IPsec between two offices"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A full-tunnel VPN routes ALL client traffic (including internet-bound) through the "
                       "corporate gateway, so everything can be inspected and policy-enforced — at the cost of more bandwidth/latency.",
            "distractors": {
                "B": "A split tunnel sends only corporate-bound traffic through the VPN while internet traffic goes directly out — the opposite of the requirement.",
                "C": "A clientless reverse proxy brokers specific web apps, not all of a client's traffic.",
                "D": "A site-to-site IPsec tunnel connects two networks/offices, not a roaming remote user's full traffic.",
            },
            "exam_pattern": "Full tunnel = all traffic via gateway (max inspection). Split tunnel = only corp "
                            "traffic via VPN (better performance, less visibility).",
        },
    },
    {
        "id": "secplus-arch-r2-008", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "multi",
        "stem": "A security architect must protect sensitive data AT REST on servers and laptops. Which TWO "
                "technologies directly protect data at rest? (Choose two.)",
        "options": [
            {"id": "A", "text": "Full-disk encryption"},
            {"id": "B", "text": "Database (column-level) encryption"},
            {"id": "C", "text": "Transport Layer Security (TLS)"},
            {"id": "D", "text": "IPsec VPN tunnel"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Full-disk encryption protects everything stored on a drive, and database/column-level "
                       "encryption protects specific stored fields — both secure data AT REST.",
            "distractors": {
                "C": "TLS protects data IN TRANSIT across a network (HTTPS), not data sitting on disk.",
                "D": "An IPsec VPN also protects data IN TRANSIT between endpoints, not at rest.",
            },
            "exam_pattern": "At rest = FDE, file/database/record-level encryption. In transit = TLS, IPsec/VPN. "
                            "In use = secure enclave/memory encryption.",
        },
    },
    {
        "id": "secplus-arch-r2-009", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 3, "type": "mcq",
        "stem": "A hospital wants to release a dataset for public research. It PERMANENTLY strips and "
                "aggregates all direct and indirect identifiers so that no record can ever be traced back "
                "to an individual — with no key kept to reverse it. Which technique is this?",
        "options": [
            {"id": "A", "text": "Anonymization"},
            {"id": "B", "text": "Pseudonymization"},
            {"id": "C", "text": "Tokenization"},
            {"id": "D", "text": "Data masking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anonymization irreversibly removes/aggregates identifiers so individuals cannot be "
                       "re-identified; because there is no reversing key, truly anonymized data falls outside most privacy-law scope.",
            "distractors": {
                "B": "Pseudonymization replaces identifiers with REVERSIBLE pseudonyms (a separate key can re-identify), so it is not irreversible.",
                "C": "Tokenization swaps a value for a token with the mapping held in a vault — reversible by design.",
                "D": "Data masking hides parts of a value for display (e.g., ****-4417) but the underlying data still exists.",
            },
            "exam_pattern": "Irreversible, no key = anonymization. Reversible with a key/vault = "
                            "pseudonymization/tokenization. Display-only hiding = masking.",
        },
    },
    {
        "id": "secplus-arch-r2-010", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A full backup runs every Sunday. Each weeknight's job backs up everything changed SINCE "
                "SUNDAY'S full backup and does NOT clear the archive bit, so each nightly backup grows "
                "larger through the week. Which backup type is in use?",
        "options": [
            {"id": "A", "text": "Differential"},
            {"id": "B", "text": "Incremental"},
            {"id": "C", "text": "Full"},
            {"id": "D", "text": "Snapshot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A differential backup copies all data changed since the last FULL backup and leaves the "
                       "archive bit set, so it grows each day; restore needs only the full + the latest differential.",
            "distractors": {
                "B": "An incremental backup copies data changed since the last backup of ANY type and clears the "
                     "archive bit, so each is small; restore needs the full + every incremental in order.",
                "C": "A full backup copies everything every time.",
                "D": "A snapshot is a point-in-time image (often of a VM/volume), not this rotating file-backup scheme.",
            },
            "exam_pattern": "Differential = since last FULL (grows, archive bit kept; restore = full + last diff). "
                            "Incremental = since last ANY (small, archive bit cleared; restore = full + all increments).",
        },
    },
    {
        "id": "secplus-arch-r2-011", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 2, "type": "mcq",
        "stem": "To minimize disaster-recovery cost, a company leases a backup facility that has space, "
                "power, and network drops but NO installed servers and NO current data; bringing it online "
                "would take days. Which recovery site type is this?",
        "options": [
            {"id": "A", "text": "Cold site"},
            {"id": "B", "text": "Hot site"},
            {"id": "C", "text": "Warm site"},
            {"id": "D", "text": "Failover cluster"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A cold site provides only the basic facility (space/power/connectivity) with no ready "
                       "hardware or data — cheapest to maintain but the slowest to recover (days).",
            "distractors": {
                "B": "A hot site is fully equipped with hardware AND near-real-time data, ready almost immediately (most expensive).",
                "C": "A warm site has some hardware/connectivity but not current data, recovering in hours.",
                "D": "A failover cluster is same-site/near-real-time redundancy, not an alternate DR facility class.",
            },
            "exam_pattern": "Cold (empty shell, cheap, days) < Warm (some kit, hours) < Hot (ready + data, "
                            "minutes, costly). Cost and speed rise together.",
        },
    },
    # ===== 4.0 Security Operations ==========================================
    {
        "id": "secplus-ops-r2-001", "exam": "secplus", "domain": "security_operations",
        "subtopic": "asset_management", "difficulty": 1, "type": "mcq",
        "stem": "A security team argues that before any other control can be effective, the organization "
                "must first build and continuously maintain a complete, accurate record of every hardware "
                "device and software package it owns. Which asset-management practice is this?",
        "options": [
            {"id": "A", "text": "Maintaining an asset inventory"},
            {"id": "B", "text": "Performing a penetration test"},
            {"id": "C", "text": "Writing a data-classification policy"},
            {"id": "D", "text": "Keeping a change log"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An accurate, current asset inventory (enumeration) is foundational — you cannot patch, "
                       "monitor, or protect what you do not know you have.",
            "distractors": {
                "B": "A penetration test assesses exploitability; it presumes you already know your assets.",
                "C": "Data classification labels data by sensitivity — important, but not an inventory of hardware/software.",
                "D": "A change log records modifications over time, not a complete catalog of owned assets.",
            },
            "exam_pattern": "'Can't protect what you can't see' -> asset inventory/enumeration first. Feeds "
                            "vulnerability management, monitoring, and licensing.",
        },
    },
    {
        "id": "secplus-ops-r2-002", "exam": "secplus", "domain": "security_operations",
        "subtopic": "automation_orchestration", "difficulty": 2, "type": "mcq",
        "stem": "When HR marks a new hire active, a workflow automatically creates the user's accounts, "
                "assigns group memberships based on job role, and emails setup instructions — and on "
                "termination it automatically disables everything. Which automation use case does this BEST illustrate?",
        "options": [
            {"id": "A", "text": "Automated user provisioning and deprovisioning"},
            {"id": "B", "text": "Continuous integration/continuous deployment (CI/CD)"},
            {"id": "C", "text": "Dynamic vulnerability scanning"},
            {"id": "D", "text": "Security regression testing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Orchestrating account creation, role-based access, and timely deprovisioning is the user "
                       "provisioning/deprovisioning use case — it enforces consistency and ensures access is revoked promptly on offboarding.",
            "distractors": {
                "B": "CI/CD automates building, testing, and deploying SOFTWARE, not the user-account lifecycle.",
                "C": "Vulnerability scanning finds flaws in systems; it is not account management.",
                "D": "Security regression testing re-tests code for reintroduced flaws.",
            },
            "exam_pattern": "Automation use cases: user/account provisioning + deprovisioning (consistency, fast "
                            "offboarding), guard rails, ticket enrichment, resource provisioning, baseline enforcement.",
        },
    },
    {
        "id": "secplus-ops-r2-003", "exam": "secplus", "domain": "security_operations",
        "subtopic": "incident_response", "difficulty": 2, "type": "mcq",
        "stem": "After eliminating the malware and closing the exploited vulnerability, the team rebuilds "
                "the affected server from a known-good image, restores its data, validates it, and returns "
                "it to production under heightened monitoring. Which incident-response phase is this?",
        "options": [
            {"id": "A", "text": "Recovery"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Containment"},
            {"id": "D", "text": "Lessons learned"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recovery restores systems to normal operation — rebuild/restore, validate, and monitor "
                       "closely before and after return to service — following eradication.",
            "distractors": {
                "B": "Eradication is REMOVING the threat and root cause (the malware and the vulnerability) — already completed here.",
                "C": "Containment limits spread (e.g., isolating the host) and comes before eradication.",
                "D": "Lessons learned is the post-incident review conducted after recovery.",
            },
            "exam_pattern": "IR order: Preparation -> Detection/Analysis -> Containment -> Eradication -> "
                            "Recovery -> Lessons Learned. Rebuild/restore/validate/monitor = recovery.",
        },
    },
    {
        "id": "secplus-ops-r2-004", "exam": "secplus", "domain": "security_operations",
        "subtopic": "digital_forensics", "difficulty": 3, "type": "multi",
        "stem": "Responders arrive at a powered-ON, compromised workstation. Following the order of "
                "volatility, which TWO types of VOLATILE evidence should be captured BEFORE the machine is "
                "shut down? (Choose two.)",
        "options": [
            {"id": "A", "text": "Contents of RAM (memory)"},
            {"id": "B", "text": "Active network connections and running processes"},
            {"id": "C", "text": "Files on the hard-disk drive"},
            {"id": "D", "text": "Archived backups on tape"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "RAM contents and live state (network connections, running processes, ARP/routing tables) "
                       "are VOLATILE and lost at power-off, so they are collected first with proper tools.",
            "distractors": {
                "C": "Files on the hard drive are non-volatile and persist across a reboot, so they are imaged after volatile data.",
                "D": "Tape backups are among the LEAST volatile and are collected last (or already archived).",
            },
            "exam_pattern": "Order of volatility (most->least): CPU cache/registers -> RAM -> network/process "
                            "state -> disk -> remote logs -> backups/archives. Capture live memory/connections before shutdown.",
        },
    },
    {
        "id": "secplus-ops-r2-005", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 2, "type": "mcq",
        "stem": "In a hospital system, permissions are bundled into job functions — 'Nurse', 'Physician', "
                "'Billing Clerk' — and each user simply inherits the permissions of the role they are "
                "assigned. Which access-control MODEL is this?",
        "options": [
            {"id": "A", "text": "Role-Based Access Control (RBAC)"},
            {"id": "B", "text": "Discretionary Access Control (DAC)"},
            {"id": "C", "text": "Mandatory Access Control (MAC)"},
            {"id": "D", "text": "Attribute-Based Access Control (ABAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC grants permissions to ROLES that map to job functions; users get access by their "
                       "role assignment, which simplifies administration and enforces least privilege consistently.",
            "distractors": {
                "B": "DAC lets the data OWNER grant access at their discretion (e.g., file permissions).",
                "C": "MAC enforces access via system-set security LABELS/clearances (e.g., Confidential/Secret) that users cannot change.",
                "D": "ABAC decides access dynamically from ATTRIBUTES/policies (user dept, device, time, location), not a fixed role.",
            },
            "exam_pattern": "RBAC = by job role; DAC = owner's discretion; MAC = labels/clearance (most rigid); "
                            "ABAC = attribute/policy-driven (most granular).",
        },
    },
    {
        "id": "secplus-ops-r2-006", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "Network devices are configured to immediately send an unsolicited alert to the management "
                "server the instant an interface goes down, instead of waiting to be polled. Which "
                "mechanism is this?",
        "options": [
            {"id": "A", "text": "SNMP trap"},
            {"id": "B", "text": "SNMP polling (GET)"},
            {"id": "C", "text": "NetFlow"},
            {"id": "D", "text": "Syslog message"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SNMP trap is an unsolicited, event-driven notification sent by an agent to the SNMP "
                       "manager when a defined condition (like a link failure) occurs — no poll required.",
            "distractors": {
                "B": "SNMP polling (GET) is the manager REQUESTING values on an interval — the device waits to be asked, which the scenario rules out.",
                "C": "NetFlow exports traffic-FLOW statistics (who talked to whom), not device event alerts.",
                "D": "Syslog also forwards event messages, but the described SNMP agent-to-manager event notification driven by poll-vs-push is specifically a trap.",
            },
            "exam_pattern": "SNMP trap = device pushes an event alert (unsolicited). SNMP GET/poll = manager "
                            "pulls values. NetFlow = flow stats. Syslog = log messages.",
        },
    },
    {
        "id": "secplus-ops-r2-007", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 3, "type": "mcq",
        "stem": "A tester runs an automated tool that sends crafted and malicious inputs to a RUNNING web "
                "application from the outside — with no access to the source code — to uncover flaws such "
                "as injection and authentication bypass. Which testing technique is this?",
        "options": [
            {"id": "A", "text": "Dynamic application security testing (DAST)"},
            {"id": "B", "text": "Static application security testing (SAST)"},
            {"id": "C", "text": "A credentialed network vulnerability scan"},
            {"id": "D", "text": "Software composition analysis (SCA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DAST tests a running application from the outside (black-box), observing how it responds "
                       "to malicious input — good at finding runtime, injection, and auth flaws without source code.",
            "distractors": {
                "B": "SAST analyzes SOURCE CODE (or binaries) BEFORE execution — the opposite approach.",
                "C": "A credentialed vulnerability scan logs into hosts to check patch/config levels; it is not application-logic input testing of a running app.",
                "D": "SCA inventories third-party/open-source COMPONENTS and their known CVEs, not live input testing.",
            },
            "exam_pattern": "SAST = source, pre-run (white-box). DAST = running app, outside-in (black-box). "
                            "SCA = dependency/known-CVE analysis.",
        },
    },
    # ===== 5.0 Security Program Management & Oversight =======================
    {
        "id": "secplus-mgmt-r2-001", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 2, "type": "mcq",
        "stem": "A business manager OWNS a customer dataset and sets its classification and handling rules. "
                "The database administration team then implements the backups, access permissions, and "
                "encryption that enforce those rules day to day. What is the DBA team's governance ROLE?",
        "options": [
            {"id": "A", "text": "Data custodian"},
            {"id": "B", "text": "Data owner"},
            {"id": "C", "text": "Data controller"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A data custodian/steward is responsible for the day-to-day technical protection of data "
                       "— backups, access enforcement, encryption — per the owner's requirements.",
            "distractors": {
                "B": "The data owner (the business manager here) is accountable for the data and sets its classification and rules — not the hands-on implementer.",
                "C": "A data controller (privacy-law term) determines the purposes and means of processing personal data.",
                "D": "A data subject is the individual the personal data is about.",
            },
            "exam_pattern": "Owner = accountable, sets classification; Custodian/steward = implements/maintains "
                            "protection; Controller = decides processing (GDPR); Processor = processes on the controller's behalf.",
        },
    },
    {
        "id": "secplus-mgmt-r2-002", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 1, "type": "mcq",
        "stem": "A document lists the exact, numbered steps a help-desk technician must follow to disable "
                "accounts, collect assets, and revoke access when an employee is terminated. Which "
                "governance document TYPE is this?",
        "options": [
            {"id": "A", "text": "Procedure"},
            {"id": "B", "text": "Policy"},
            {"id": "C", "text": "Standard"},
            {"id": "D", "text": "Guideline"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A procedure is a detailed, step-by-step set of instructions for performing a specific "
                       "task — here, the offboarding steps.",
            "distractors": {
                "B": "A policy is the high-level, mandatory statement of intent ('accounts must be revoked promptly on termination'), not the steps.",
                "C": "A standard specifies mandatory specifics (e.g., required tools or settings), narrower than a policy but not a step list.",
                "D": "A guideline is a non-mandatory recommendation.",
            },
            "exam_pattern": "Policy (what/why, mandatory) -> Standard (specific requirements) -> Procedure "
                            "(how, exact steps) -> Guideline (recommended best practice).",
        },
    },
    {
        "id": "secplus-mgmt-r2-003", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After a company applies all the controls it has chosen, some risk still remains. The "
                "leftover risk that management reviews and chooses to live with is BEST described as?",
        "options": [
            {"id": "A", "text": "Residual risk"},
            {"id": "B", "text": "Inherent risk"},
            {"id": "C", "text": "Risk appetite"},
            {"id": "D", "text": "Transferred risk"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Residual risk is the risk that REMAINS after controls are applied; management must "
                       "evaluate and formally accept it (or add further treatment).",
            "distractors": {
                "B": "Inherent risk is the risk BEFORE any controls are applied.",
                "C": "Risk appetite is the amount/type of risk an organization is WILLING to pursue — a threshold, not the leftover amount.",
                "D": "Transferred risk is risk shifted to a third party (e.g., insurance), a treatment choice rather than the remaining risk.",
            },
            "exam_pattern": "Inherent (before controls) -> apply controls -> Residual (after controls); accept "
                            "residual only if within risk appetite/tolerance.",
        },
    },
    {
        "id": "secplus-mgmt-r2-004", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Under an existing master agreement with a consultancy, the two parties sign a document that "
                "lists the EXACT deliverables, milestones, timeline, and acceptance criteria for one "
                "specific security-assessment engagement. Which document is this?",
        "options": [
            {"id": "A", "text": "Statement of Work (SOW)"},
            {"id": "B", "text": "Master Service Agreement (MSA)"},
            {"id": "C", "text": "Service-Level Agreement (SLA)"},
            {"id": "D", "text": "Memorandum of Understanding (MOU)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SOW defines the specific work for a given project — deliverables, milestones, "
                       "schedule, acceptance criteria — typically executed under an overarching MSA.",
            "distractors": {
                "B": "The MSA is the overarching contract setting general legal/business terms that each SOW falls under — not the per-project specifics.",
                "C": "An SLA defines measurable service metrics (uptime/response) and penalties.",
                "D": "An MOU is a non-binding statement of intent between parties.",
            },
            "exam_pattern": "MSA = master terms (once) -> SOW = specific project work/deliverables (per "
                            "engagement). SLA = service metrics. MOU = intent.",
        },
    },
    {
        "id": "secplus-mgmt-r2-005", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Two partner agencies sign a NON-BINDING document expressing their shared intentions and "
                "broad expectations to cooperate on a project, with no enforceable obligations, metrics, or "
                "penalties. Which document is this?",
        "options": [
            {"id": "A", "text": "Memorandum of Understanding (MOU)"},
            {"id": "B", "text": "Service-Level Agreement (SLA)"},
            {"id": "C", "text": "Business Partners Agreement (BPA)"},
            {"id": "D", "text": "Non-Disclosure Agreement (NDA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An MOU (or MOA) is a generally non-binding document stating the parties' shared intent "
                       "and expectations to work together, without the enforceable specifics of a contract.",
            "distractors": {
                "B": "An SLA is a binding, measurable commitment (uptime/response) with consequences for misses.",
                "C": "A BPA defines the terms of a business partnership (roles, responsibilities, profit sharing).",
                "D": "An NDA is a binding agreement protecting the confidentiality of shared information.",
            },
            "exam_pattern": "MOU/MOA = intent, usually non-binding. SLA = measurable metrics + penalties. "
                            "BPA = partnership terms. NDA = confidentiality.",
        },
    },
    {
        "id": "secplus-mgmt-r2-006", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "mcq",
        "stem": "Under GDPR, a retailer decides what customer personal data to collect and why, then hires "
                "a cloud email-marketing company that stores and processes that data STRICTLY on the "
                "retailer's documented instructions. Which role does the cloud company play?",
        "options": [
            {"id": "A", "text": "Data processor"},
            {"id": "B", "text": "Data controller"},
            {"id": "C", "text": "Data owner"},
            {"id": "D", "text": "Supervisory authority"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A data processor processes personal data ON BEHALF of, and under the instructions of, "
                       "the controller — exactly the cloud email provider's role here.",
            "distractors": {
                "B": "The data controller (the retailer) determines the PURPOSES and MEANS of processing.",
                "C": "'Data owner' is an internal governance role, not the GDPR term for this relationship.",
                "D": "A supervisory authority is the regulator that enforces GDPR, not a party processing the data.",
            },
            "exam_pattern": "GDPR: Controller decides why/how (purposes/means); Processor acts on the "
                            "controller's instructions. Both carry obligations.",
        },
    },
    {
        "id": "secplus-mgmt-r2-007", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "mcq",
        "stem": "A retailer that stores, processes, and transmits payment-card data must comply with a "
                "security standard created and enforced by the major card brands through contracts — NOT "
                "by a government statute. Which framework is this?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "HIPAA"},
            {"id": "C", "text": "GDPR"},
            {"id": "D", "text": "SOX"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PCI DSS (Payment Card Industry Data Security Standard) is a contractual, "
                       "industry-mandated standard for organizations handling cardholder data; non-compliance brings fines or loss of card-processing privileges.",
            "distractors": {
                "B": "HIPAA is a U.S. LAW protecting health information.",
                "C": "GDPR is an EU LAW protecting personal data/privacy.",
                "D": "SOX is a U.S. LAW governing financial reporting and controls for public companies.",
            },
            "exam_pattern": "PCI DSS = industry/contractual (cards). HIPAA (health), GDPR (EU privacy), "
                            "SOX (financial reporting) = government laws/regulations.",
        },
    },
    {
        "id": "secplus-mgmt-r2-008", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "compliance_privacy", "difficulty": 2, "type": "multi",
        "stem": "A privacy policy states that the company will collect ONLY the personal data it genuinely "
                "needs for a stated purpose and will DELETE it once that purpose is fulfilled. Which TWO "
                "privacy principles are being applied? (Choose two.)",
        "options": [
            {"id": "A", "text": "Data minimization"},
            {"id": "B", "text": "Storage (retention) limitation"},
            {"id": "C", "text": "Data sovereignty"},
            {"id": "D", "text": "Non-repudiation"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Collecting only what is necessary is data minimization; deleting data once its purpose "
                       "is met is storage/retention limitation — both core data-privacy principles (e.g., under GDPR).",
            "distractors": {
                "C": "Data sovereignty concerns the JURISDICTION/location where data is stored and whose laws apply, not how little is collected or how long it is kept.",
                "D": "Non-repudiation is a security property (proof of an action's origin), unrelated to these privacy principles.",
            },
            "exam_pattern": "Privacy principles: minimization (collect the least needed), purpose limitation, "
                            "storage/retention limitation (keep no longer than needed). Sovereignty = location/jurisdiction.",
        },
    },
    {
        "id": "secplus-mgmt-r2-009", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "During an authorized penetration test, the tester directly interacts with the target — "
                "port-scanning its hosts and banner-grabbing running services to map the attack surface. "
                "Which reconnaissance type is this?",
        "options": [
            {"id": "A", "text": "Active reconnaissance"},
            {"id": "B", "text": "Passive reconnaissance"},
            {"id": "C", "text": "Pivoting"},
            {"id": "D", "text": "Privilege escalation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Active reconnaissance directly probes the target (scanning, enumeration, banner "
                       "grabbing), which is more informative but more detectable than passive methods.",
            "distractors": {
                "B": "Passive reconnaissance gathers information WITHOUT touching the target (OSINT, public records, DNS/WHOIS) and is stealthier.",
                "C": "Pivoting is using a compromised host to reach other systems — a post-exploitation move, not recon.",
                "D": "Privilege escalation gains higher rights after access, not information gathering.",
            },
            "exam_pattern": "Passive recon = no direct contact (OSINT, stealthy). Active recon = direct probing "
                            "(scans/enumeration, detectable). Both precede exploitation.",
        },
    },
    {
        "id": "secplus-mgmt-r2-010", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "To give customers INDEPENDENT assurance over its controls, a SaaS provider hires an outside "
                "accounting firm to examine those controls and issue a formal attestation report (such as "
                "SOC 2). Which type of assessment is this?",
        "options": [
            {"id": "A", "text": "External (independent third-party) audit"},
            {"id": "B", "text": "Internal audit"},
            {"id": "C", "text": "Self-assessment"},
            {"id": "D", "text": "Tabletop exercise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An external/third-party audit is performed by an independent outside party and yields an "
                       "attestation (e.g., SOC 2) that customers and regulators can trust more than a self-review.",
            "distractors": {
                "B": "An internal audit is conducted by the organization's OWN staff for self-checking and readiness.",
                "C": "A self-assessment is the organization grading itself (lowest independence).",
                "D": "A tabletop exercise is a discussion-based incident-response drill, not a controls attestation.",
            },
            "exam_pattern": "Independence ladder: self-assessment < internal audit < external/third-party "
                            "audit/attestation (SOC 2, ISO certification) — more independence = more trust.",
        },
    },
    {
        "id": "secplus-mgmt-r2-011", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 1, "type": "mcq",
        "stem": "An organization requires employees to lock their screens and to store all sensitive "
                "documents and removable media in locked drawers whenever they step away from their "
                "workstation. Which security-awareness practice is this?",
        "options": [
            {"id": "A", "text": "Clean desk policy"},
            {"id": "B", "text": "Acceptable use policy"},
            {"id": "C", "text": "Data-classification scheme"},
            {"id": "D", "text": "Separation of duties"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A clean desk policy requires sensitive materials to be secured (and screens locked) when "
                       "a workspace is unattended, reducing shoulder surfing, theft, and accidental exposure.",
            "distractors": {
                "B": "An acceptable use policy governs how employees may use company systems/resources, not desk tidiness.",
                "C": "Data classification labels data by sensitivity; it does not dictate securing a physical desk.",
                "D": "Separation of duties splits critical tasks among people to prevent fraud — unrelated to an unattended desk.",
            },
            "exam_pattern": "'Secure papers/media + lock screen when away' = clean desk policy (counters "
                            "shoulder surfing and opportunistic data exposure).",
        },
    },
]
