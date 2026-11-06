"""CompTIA Security+ SY0-701 item pool — original, objective-aligned questions.

Same authoring rules as the Cisco pools: original content mapped to the public
exam objectives, never real exam items. build_content.py shuffles option order,
so the answer key here is not positionally biased.
"""

QUESTIONS = [
    # ===== 1.0 General Security Concepts =====================================
    {
        "id": "secplus-gsc-001", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "A security guard checks badges at the lobby entrance. Which control "
                "CATEGORY best describes the guard?",
        "options": [
            {"id": "A", "text": "Physical"},
            {"id": "B", "text": "Technical"},
            {"id": "C", "text": "Managerial"},
            {"id": "D", "text": "Operational"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SY0-701 groups controls into four CATEGORIES — technical, managerial, "
                       "operational, and physical. A guard, fence, or lock is a physical control.",
            "distractors": {
                "B": "Technical (logical) controls are implemented by technology — firewalls, "
                     "encryption, MFA — not a person at a door.",
                "C": "Managerial controls are policies, risk assessments, and planning.",
                "D": "Operational controls are carried out by people day-to-day (e.g., awareness "
                     "training), but the guard specifically is a physical barrier.",
            },
            "exam_pattern": "Separate control CATEGORY (technical/managerial/operational/physical) "
                            "from control TYPE (preventive/detective/corrective/deterrent/compensating/directive).",
        },
    },
    {
        "id": "secplus-gsc-002", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "security_controls", "difficulty": 2, "type": "mcq",
        "stem": "After an outage, a company restores systems from backup to return to normal "
                "operation. Which control TYPE is the restore process?",
        "options": [
            {"id": "A", "text": "Corrective"},
            {"id": "B", "text": "Preventive"},
            {"id": "C", "text": "Detective"},
            {"id": "D", "text": "Deterrent"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A corrective control acts AFTER an incident to fix damage and restore "
                       "operations — restoring from backup is the classic example.",
            "distractors": {
                "B": "Preventive controls stop an incident before it happens (e.g., a firewall rule).",
                "C": "Detective controls identify an incident in progress or after the fact (e.g., logs, IDS).",
                "D": "Deterrent controls discourage an attacker (e.g., warning banners, visible cameras).",
            },
            "exam_pattern": "Timing tells the type: before = preventive/deterrent, during/after-detection "
                            "= detective, after-to-fix = corrective, substitute = compensating.",
        },
    },
    {
        "id": "secplus-gsc-003", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cia_aaa", "difficulty": 1, "type": "mcq",
        "stem": "A digital signature on an email lets the recipient prove the sender actually "
                "sent it and cannot later deny it. Which security property is this?",
        "options": [
            {"id": "A", "text": "Non-repudiation"},
            {"id": "B", "text": "Confidentiality"},
            {"id": "C", "text": "Availability"},
            {"id": "D", "text": "Accounting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Non-repudiation means the originator cannot deny the action. A digital "
                       "signature (signing with a private key) provides it along with integrity.",
            "distractors": {
                "B": "Confidentiality is about keeping data secret (encryption), not proving authorship.",
                "C": "Availability is about systems/data being accessible when needed.",
                "D": "Accounting (the third A in AAA) tracks what a user did, but the signature's "
                     "specific property here is non-repudiation.",
            },
            "exam_pattern": "Digital signature → integrity + non-repudiation. Encryption → confidentiality.",
        },
    },
    {
        "id": "secplus-gsc-004", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "In a Zero Trust architecture, which component makes the allow/deny decision "
                "for an access request based on policy?",
        "options": [
            {"id": "A", "text": "Policy Engine"},
            {"id": "B", "text": "Policy Enforcement Point"},
            {"id": "C", "text": "Policy Administrator"},
            {"id": "D", "text": "Data plane"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Policy Engine (in the control plane) evaluates the request against policy "
                       "and decides grant or deny; the Policy Administrator then executes it and the "
                       "Policy Enforcement Point allows/blocks the session.",
            "distractors": {
                "B": "The PEP sits in the data plane and enforces the decision — it doesn't make it.",
                "C": "The Policy Administrator establishes/tears down the connection per the decision.",
                "D": "The data plane is where traffic flows and enforcement happens, not where policy is decided.",
            },
            "exam_pattern": "Zero Trust control plane = Policy Engine (decides) + Policy Administrator; "
                            "data plane = Policy Enforcement Point (enforces).",
        },
    },
    {
        "id": "secplus-gsc-005", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "cryptographic_solutions", "difficulty": 2, "type": "mcq",
        "stem": "Two parties need to exchange a large volume of data quickly with a single "
                "shared secret key. Which algorithm fits?",
        "options": [
            {"id": "A", "text": "AES (symmetric)"},
            {"id": "B", "text": "RSA (asymmetric)"},
            {"id": "C", "text": "SHA-256 (hash)"},
            {"id": "D", "text": "ECC (asymmetric)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AES is a symmetric cipher — one shared key, very fast — ideal for bulk data "
                       "encryption. Asymmetric is typically used only to exchange that symmetric key.",
            "distractors": {
                "B": "RSA is asymmetric (key pair) and far slower; it's used for key exchange/signatures, not bulk data.",
                "C": "SHA-256 is a one-way hash for integrity — it doesn't encrypt and can't be reversed.",
                "D": "ECC is asymmetric; strong with small keys, but still used for key exchange/signing, not bulk speed.",
            },
            "exam_pattern": "Symmetric (AES) = fast, same key, bulk data. Asymmetric (RSA/ECC) = key pair, "
                            "slow, used to exchange keys and sign.",
        },
    },
    {
        "id": "secplus-gsc-006", "exam": "secplus", "domain": "general_security_concepts",
        "subtopic": "pki", "difficulty": 2, "type": "mcq",
        "stem": "In PKI, a client needs to check in real time whether a web server's certificate "
                "has been revoked. Which mechanism provides that?",
        "options": [
            {"id": "A", "text": "OCSP"},
            {"id": "B", "text": "A self-signed certificate"},
            {"id": "C", "text": "A certificate signing request (CSR)"},
            {"id": "D", "text": "Key escrow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "OCSP (Online Certificate Status Protocol) lets a client query the CA for a "
                       "single certificate's status in real time — lighter than downloading the full CRL.",
            "distractors": {
                "B": "A self-signed cert isn't issued by a trusted CA and has nothing to do with revocation checks.",
                "C": "A CSR is what you send to a CA to REQUEST a certificate, not to check revocation.",
                "D": "Key escrow stores a copy of keys for recovery; it's unrelated to revocation status.",
            },
            "exam_pattern": "Revocation checks = CRL (full list, downloaded) or OCSP (real-time, single cert). "
                            "OCSP stapling has the server present the status to save the client a lookup.",
        },
    },
    # ===== 2.0 Threats, Vulnerabilities & Mitigations =======================
    {
        "id": "secplus-tvm-001", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_actors", "difficulty": 2, "type": "mcq",
        "stem": "A sophisticated, well-funded group maintains long-term covert access to a "
                "government network to exfiltrate data over months. Which threat actor is this?",
        "options": [
            {"id": "A", "text": "Nation-state (APT)"},
            {"id": "B", "text": "Script kiddie"},
            {"id": "C", "text": "Hacktivist"},
            {"id": "D", "text": "Shadow IT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "High resources + long-term stealthy persistence + espionage motive is the "
                       "signature of a nation-state Advanced Persistent Threat.",
            "distractors": {
                "B": "A script kiddie has low skill/resources and uses others' tools opportunistically.",
                "C": "A hacktivist is driven by ideology and usually seeks visibility (defacement, leaks), not months of stealth.",
                "D": "Shadow IT is unsanctioned internal tech, not an external attacker.",
            },
            "exam_pattern": "Match actor by resources + motivation: nation-state = high/espionage, "
                            "organized crime = financial, hacktivist = ideology, insider = access/revenge.",
        },
    },
    {
        "id": "secplus-tvm-002", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 2, "type": "multi",
        "stem": "An attacker calls the help desk pretending to be a panicked executive and "
                "pressures the agent to reset a password immediately. Which techniques are MOST "
                "in play? (Choose two.)",
        "options": [
            {"id": "A", "text": "Pretexting"},
            {"id": "B", "text": "Urgency"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "RAID failure"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "The attacker invents a scenario/role (pretexting) and leans on urgency "
                       "(and authority) to rush the agent past normal verification.",
            "distractors": {
                "C": "SQL injection is a technical application attack, not social engineering.",
                "D": "A RAID failure is a hardware/availability issue, unrelated to the phone call.",
            },
            "exam_pattern": "Social-engineering 'principles': authority, urgency, intimidation, "
                            "scarcity, familiarity/liking, trust, consensus.",
        },
    },
    {
        "id": "secplus-tvm-003", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "malware", "difficulty": 1, "type": "mcq",
        "stem": "Users' files are encrypted and a message demands payment in cryptocurrency for "
                "the decryption key. Which malware is this?",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Rootkit"},
            {"id": "D", "text": "Keylogger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encrypting data and extorting payment for recovery is the definition of ransomware.",
            "distractors": {
                "B": "A worm self-propagates across hosts but doesn't inherently encrypt-for-ransom.",
                "C": "A rootkit hides at a privileged level to maintain stealthy access.",
                "D": "A keylogger records keystrokes to steal credentials.",
            },
            "exam_pattern": "Map behavior to malware: encrypt+extort = ransomware, self-spread = worm, "
                            "disguised installer = trojan, hide/privilege = rootkit, time/condition trigger = logic bomb.",
        },
    },
    {
        "id": "secplus-tvm-004", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "application_attacks", "difficulty": 3, "type": "mcq",
        "stem": "A login form lets an attacker submit ' OR '1'='1 and bypass authentication. "
                "What is the vulnerability, and the BEST fix?",
        "options": [
            {"id": "A", "text": "SQL injection — use parameterized queries / input validation"},
            {"id": "B", "text": "Cross-site scripting — enable a longer session timeout"},
            {"id": "C", "text": "Buffer overflow — add more RAM"},
            {"id": "D", "text": "On-path attack — install antivirus"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Injecting SQL through input is SQL injection; the durable fix is parameterized "
                       "(prepared) statements plus server-side input validation, not just escaping.",
            "distractors": {
                "B": "XSS injects script into pages viewed by other users; session timeout doesn't address injection.",
                "C": "A buffer overflow overwrites memory; more RAM is irrelevant to input-validation flaws.",
                "D": "An on-path (MITM) attack intercepts traffic; antivirus doesn't fix an injectable query.",
            },
            "exam_pattern": "' OR '1'='1 / UNION SELECT = SQLi → parameterized queries. <script> in input = XSS → output encoding + input validation.",
        },
    },
    {
        "id": "secplus-tvm-005", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "Thousands of compromised IoT devices flood a company's web server with traffic "
                "until it is unreachable. Which attack is this?",
        "options": [
            {"id": "A", "text": "Distributed denial-of-service (DDoS)"},
            {"id": "B", "text": "Privilege escalation"},
            {"id": "C", "text": "Pass-the-hash"},
            {"id": "D", "text": "Watering hole"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Many distributed sources (a botnet) overwhelming a target to deny availability "
                       "is a DDoS. IoT botnets are a classic source.",
            "distractors": {
                "B": "Privilege escalation gains higher rights on a host, not a traffic flood.",
                "C": "Pass-the-hash reuses captured credential hashes to authenticate.",
                "D": "A watering-hole attack compromises a site the target group visits.",
            },
            "exam_pattern": "Many sources + availability loss = DDoS. Single source = DoS. Amplification/reflection "
                            "(DNS/NTP) multiplies the volume.",
        },
    },
    {
        "id": "secplus-tvm-006", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "mitigation_techniques", "difficulty": 2, "type": "mcq",
        "stem": "A vendor announces a critical flaw being exploited in the wild before any patch "
                "exists. Which term describes this, and the BEST immediate mitigation?",
        "options": [
            {"id": "A", "text": "Zero-day — apply compensating controls (segmentation, IPS, monitoring)"},
            {"id": "B", "text": "Legacy system — buy new hardware"},
            {"id": "C", "text": "False positive — ignore the alert"},
            {"id": "D", "text": "Misconfiguration — reset to defaults"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An exploited flaw with no available patch is a zero-day. Until a patch ships you "
                       "reduce exposure with compensating controls — segmentation, virtual patching/IPS, "
                       "tightened monitoring.",
            "distractors": {
                "B": "'Legacy' means unsupported/old; not necessarily this freshly-announced flaw.",
                "C": "It's actively exploited — treating a real threat as a false positive is dangerous.",
                "D": "Resetting to defaults usually WEAKENS security and doesn't patch an unknown flaw.",
            },
            "exam_pattern": "No patch yet + active exploit = zero-day → compensating controls now, patch when available.",
        },
    },
    # ===== 3.0 Security Architecture ========================================
    {
        "id": "secplus-arch-001", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 2, "type": "mcq",
        "stem": "A database stores credit-card numbers. The team replaces each number with a "
                "random surrogate value kept in a separate secure vault, so the app never holds "
                "the real number. Which technique is this?",
        "options": [
            {"id": "A", "text": "Tokenization"},
            {"id": "B", "text": "Hashing"},
            {"id": "C", "text": "Steganography"},
            {"id": "D", "text": "Full-disk encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tokenization swaps sensitive data for a non-sensitive token, with the mapping "
                       "held in a protected vault — common for PCI card data so systems never store the PAN.",
            "distractors": {
                "B": "Hashing is one-way; you can't retrieve the original value, so it can't be used where the number must be recovered.",
                "C": "Steganography hides data inside other media; it isn't a card-data substitution scheme.",
                "D": "Full-disk encryption protects data at rest on the drive but the app still handles the real number in use.",
            },
            "exam_pattern": "Tokenization = reversible swap via a vault (no math on the data). Encryption = reversible with a key. Hashing = one-way.",
        },
    },
    {
        "id": "secplus-arch-002", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "data_protection", "difficulty": 1, "type": "mcq",
        "stem": "Which term describes data being actively processed in a system's memory/CPU "
                "(not stored on disk and not moving across the network)?",
        "options": [
            {"id": "A", "text": "Data in use"},
            {"id": "B", "text": "Data at rest"},
            {"id": "C", "text": "Data in transit"},
            {"id": "D", "text": "Data remanence"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Data in use is data loaded in memory/registers being processed. It's the hardest "
                       "to protect — approaches include secure enclaves and memory encryption.",
            "distractors": {
                "B": "Data at rest is stored (disk, backup, DB) — protected by encryption at rest.",
                "C": "Data in transit moves across a network — protected by TLS/IPsec.",
                "D": "Data remanence is residual data left after supposed deletion.",
            },
            "exam_pattern": "Three states: at rest (stored), in transit (moving), in use (being processed).",
        },
    },
    {
        "id": "secplus-arch-003", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A business can tolerate losing at most 1 hour of data if a system fails. Which "
                "metric does '1 hour of acceptable data loss' define?",
        "options": [
            {"id": "A", "text": "Recovery Point Objective (RPO)"},
            {"id": "B", "text": "Recovery Time Objective (RTO)"},
            {"id": "C", "text": "Mean Time To Repair (MTTR)"},
            {"id": "D", "text": "Mean Time Between Failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RPO is the maximum acceptable amount of DATA loss, measured as time — it drives "
                       "how frequently you must back up/replicate (here, at least hourly).",
            "distractors": {
                "B": "RTO is how long you can be DOWN before recovery — a time-to-restore target, not data loss.",
                "C": "MTTR is the average time to repair a failed component.",
                "D": "MTBF is the average time between failures (reliability), not a recovery target.",
            },
            "exam_pattern": "RPO = data loss tolerance (backup frequency). RTO = downtime tolerance (how fast you must be back).",
        },
    },
    {
        "id": "secplus-arch-004", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "resilience_recovery", "difficulty": 2, "type": "mcq",
        "stem": "A server needs to survive a single disk failure with no data loss while keeping "
                "usable capacity high across 4+ disks. Which RAID level is the common choice?",
        "options": [
            {"id": "A", "text": "RAID 5 (striping with parity)"},
            {"id": "B", "text": "RAID 0 (striping)"},
            {"id": "C", "text": "JBOD"},
            {"id": "D", "text": "RAID 1 (mirroring) across 4 disks for capacity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RAID 5 stripes data with distributed parity: it tolerates one disk failure and "
                       "only 'costs' one disk of capacity, so usable space stays high on 4+ disks.",
            "distractors": {
                "B": "RAID 0 has no redundancy — one disk failure loses everything.",
                "C": "JBOD is just independent disks with no fault tolerance.",
                "D": "Mirroring protects data but halves capacity; it's not the high-capacity choice here.",
            },
            "exam_pattern": "RAID 0 = speed/no redundancy, 1 = mirror, 5 = single-parity (1 disk loss), "
                            "6 = double-parity (2 disk loss), 10 = mirror+stripe.",
        },
    },
    {
        "id": "secplus-arch-005", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "cloud_virtualization_security", "difficulty": 2, "type": "mcq",
        "stem": "In an IaaS cloud model, who is responsible for patching the GUEST operating "
                "system and applications on a virtual machine?",
        "options": [
            {"id": "A", "text": "The customer"},
            {"id": "B", "text": "The cloud provider"},
            {"id": "C", "text": "Neither — IaaS is fully managed"},
            {"id": "D", "text": "The ISP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Under the shared responsibility model for IaaS, the provider secures the physical "
                       "infrastructure and hypervisor; the customer owns the OS, apps, data, and config.",
            "distractors": {
                "B": "The provider handles the hardware/hypervisor layer, not your guest OS.",
                "C": "IaaS is NOT fully managed — that's closer to SaaS.",
                "D": "The ISP provides connectivity, not OS patching.",
            },
            "exam_pattern": "Shared responsibility: more 'as-a-service' (SaaS) = provider owns more; "
                            "IaaS leaves OS/app/data to the customer.",
        },
    },
    {
        "id": "secplus-arch-006", "exam": "secplus", "domain": "security_architecture",
        "subtopic": "secure_design", "difficulty": 2, "type": "mcq",
        "stem": "A network places web servers in a screened subnet, with separate firewall rules "
                "between the Internet, the screened subnet, and the internal LAN. Which principle "
                "is being applied?",
        "options": [
            {"id": "A", "text": "Network segmentation / defense in depth"},
            {"id": "B", "text": "Security through obscurity"},
            {"id": "C", "text": "Single point of failure"},
            {"id": "D", "text": "Implicit allow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Isolating exposed services in a screened subnet (DMZ) with layered firewall rules "
                       "is segmentation and defense in depth — a breach of the web tier doesn't reach the LAN.",
            "distractors": {
                "B": "Obscurity hides details hoping no one finds them; that's not what segmentation is.",
                "C": "This design REDUCES single points of failure/exposure rather than creating one.",
                "D": "Good firewall design uses implicit DENY, not implicit allow.",
            },
            "exam_pattern": "Screened subnet/DMZ + layered rules = segmentation + defense in depth.",
        },
    },
    # ===== 4.0 Security Operations ==========================================
    {
        "id": "secplus-ops-001", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 2, "type": "mcq",
        "stem": "A login requires a password PLUS a one-time code from an app on the user's "
                "phone. Which two authentication FACTORS are combined?",
        "options": [
            {"id": "A", "text": "Something you know + something you have"},
            {"id": "B", "text": "Something you are + somewhere you are"},
            {"id": "C", "text": "Something you know + something you are"},
            {"id": "D", "text": "Two of the same factor (knowledge)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A password is 'something you know'; the phone generating the code is 'something you "
                       "have'. Two DIFFERENT factors = true MFA.",
            "distractors": {
                "B": "No biometric or location is used here.",
                "C": "There's no biometric ('something you are') in a password + OTP app.",
                "D": "They are different factors, which is the point — two passwords would NOT be MFA.",
            },
            "exam_pattern": "MFA requires two DIFFERENT factors: know (password), have (token/phone), "
                            "are (biometric), plus somewhere-you-are / something-you-do.",
        },
    },
    {
        "id": "secplus-ops-002", "exam": "secplus", "domain": "security_operations",
        "subtopic": "incident_response", "difficulty": 2, "type": "mcq",
        "stem": "During a malware incident, responders isolate the infected host from the network "
                "to stop the spread. Which incident-response phase is this?",
        "options": [
            {"id": "A", "text": "Containment"},
            {"id": "B", "text": "Eradication"},
            {"id": "C", "text": "Recovery"},
            {"id": "D", "text": "Preparation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Isolating the affected system to limit damage/spread is containment — it comes "
                       "before removing the malware (eradication) and restoring service (recovery).",
            "distractors": {
                "B": "Eradication removes the threat (wipe/clean) AFTER it's contained.",
                "C": "Recovery restores systems to normal and validates them.",
                "D": "Preparation is the up-front readiness work before any incident.",
            },
            "exam_pattern": "IR order: Preparation → Detection/Analysis → Containment → Eradication → "
                            "Recovery → Lessons Learned. 'Isolate' = containment.",
        },
    },
    {
        "id": "secplus-ops-003", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to aggregate logs from many systems, correlate events, and "
                "alert on suspicious patterns from one console. Which tool provides this?",
        "options": [
            {"id": "A", "text": "SIEM"},
            {"id": "B", "text": "DLP"},
            {"id": "C", "text": "VPN concentrator"},
            {"id": "D", "text": "Load balancer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM (Security Information and Event Management) centralizes log collection, "
                       "correlation, alerting, and reporting — the single pane for monitoring.",
            "distractors": {
                "B": "DLP prevents sensitive data from leaving; it isn't a log-correlation platform.",
                "C": "A VPN concentrator terminates remote-access tunnels.",
                "D": "A load balancer distributes traffic across servers.",
            },
            "exam_pattern": "Aggregate + correlate + alert on logs = SIEM. Add automated response playbooks = SOAR.",
        },
    },
    {
        "id": "secplus-ops-004", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 3, "type": "mcq",
        "stem": "A vulnerability scan run WITHOUT login credentials reports far fewer findings than "
                "one run WITH credentials. Why is the credentialed scan more thorough?",
        "options": [
            {"id": "A", "text": "It can log in and inspect patch levels/config from the inside"},
            {"id": "B", "text": "It encrypts the scan traffic end to end"},
            {"id": "C", "text": "It runs faster so it finds more by luck"},
            {"id": "D", "text": "It automatically patches what it finds"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A credentialed scan authenticates to the host and reads installed software, patch "
                       "levels, and settings directly — seeing far more than an outside-in view.",
            "distractors": {
                "B": "Credentials give deeper inspection, not traffic encryption.",
                "C": "Thoroughness comes from the inside view, not speed.",
                "D": "Scanners identify issues; they don't patch them.",
            },
            "exam_pattern": "Credentialed/authenticated scan = deeper, fewer false negatives. "
                            "Non-credentialed = attacker's external view.",
        },
    },
    {
        "id": "secplus-ops-005", "exam": "secplus", "domain": "security_operations",
        "subtopic": "digital_forensics", "difficulty": 3, "type": "mcq",
        "stem": "When collecting evidence from a running system, which data should be captured "
                "FIRST according to the order of volatility?",
        "options": [
            {"id": "A", "text": "Contents of CPU cache/registers and RAM"},
            {"id": "B", "text": "Files on the hard drive"},
            {"id": "C", "text": "Archived backups on tape"},
            {"id": "D", "text": "Printed documentation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Order of volatility: capture the most fleeting data first — CPU cache/registers, "
                       "then RAM, then disk, then remote/archival logs — because volatile data vanishes on power loss.",
            "distractors": {
                "B": "Disk is less volatile than memory and is collected after RAM.",
                "C": "Backups/tape are among the least volatile — collected last.",
                "D": "Static documentation isn't volatile system state at all.",
            },
            "exam_pattern": "Most → least volatile: cache/registers → RAM → disk → remote logs → backups/archives. "
                            "Maintain chain of custody throughout.",
        },
    },
    {
        "id": "secplus-ops-006", "exam": "secplus", "domain": "security_operations",
        "subtopic": "secure_baselines_hardening", "difficulty": 2, "type": "mcq",
        "stem": "A hardening standard says to turn off unused services and close unneeded ports on "
                "every new server. Which principle does this support?",
        "options": [
            {"id": "A", "text": "Reducing the attack surface"},
            {"id": "B", "text": "Increasing availability through redundancy"},
            {"id": "C", "text": "Non-repudiation"},
            {"id": "D", "text": "Key rotation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Every running service or open port is a potential entry point; disabling the "
                       "unneeded ones shrinks the attack surface the server exposes.",
            "distractors": {
                "B": "Redundancy improves availability, but that's not what disabling services does.",
                "C": "Non-repudiation is about proving actions, unrelated to service hardening.",
                "D": "Key rotation is a crypto-hygiene task, not port/service reduction.",
            },
            "exam_pattern": "Disable unused services/ports, remove default accounts, apply baselines = attack-surface reduction.",
        },
    },
    # ===== 5.0 Security Program Management & Oversight =======================
    {
        "id": "secplus-mgmt-001", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 3, "type": "mcq",
        "stem": "A single flood is expected to cause $200,000 of damage to a warehouse, and such a "
                "flood is expected once every 20 years. What is the annualized loss expectancy (ALE)?",
        "options": [
            {"id": "A", "text": "$10,000"},
            {"id": "B", "text": "$200,000"},
            {"id": "C", "text": "$4,000,000"},
            {"id": "D", "text": "$20,000"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ALE = SLE × ARO. SLE is the single-event loss ($200,000); ARO is the annual rate "
                       "(once per 20 years = 0.05). 200,000 × 0.05 = $10,000.",
            "distractors": {
                "B": "$200,000 is the SLE (one event), not annualized.",
                "C": "Multiplying by 20 instead of dividing is the classic trap.",
                "D": "$20,000 would be a 1-in-10 rate; here it's 1-in-20 (0.05).",
            },
            "exam_pattern": "SLE = Asset Value × Exposure Factor. ALE = SLE × ARO. Watch the ARO as a fraction (1/years).",
        },
    },
    {
        "id": "secplus-mgmt-002", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "risk_management", "difficulty": 2, "type": "mcq",
        "stem": "After assessing a risk, the company buys cyber-insurance to cover the financial "
                "impact if it occurs. Which risk-management strategy is this?",
        "options": [
            {"id": "A", "text": "Transfer"},
            {"id": "B", "text": "Avoid"},
            {"id": "C", "text": "Accept"},
            {"id": "D", "text": "Mitigate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Shifting the financial impact to a third party (insurance) is risk transference.",
            "distractors": {
                "B": "Avoidance stops the risky activity entirely.",
                "C": "Acceptance means acknowledging the risk and doing nothing further.",
                "D": "Mitigation reduces likelihood/impact with controls.",
            },
            "exam_pattern": "Four responses: avoid (stop it), transfer (insure/outsource), mitigate (add controls), accept (live with it).",
        },
    },
    {
        "id": "secplus-mgmt-003", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "third_party_risk", "difficulty": 2, "type": "mcq",
        "stem": "Two organizations sign an agreement that defines the specific uptime and response "
                "times a vendor must meet, with penalties for missing them. Which document is this?",
        "options": [
            {"id": "A", "text": "Service-Level Agreement (SLA)"},
            {"id": "B", "text": "Memorandum of Understanding (MOU)"},
            {"id": "C", "text": "Non-Disclosure Agreement (NDA)"},
            {"id": "D", "text": "Business Partners Agreement (BPA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An SLA specifies measurable service commitments (uptime, response time) and the "
                       "consequences for not meeting them.",
            "distractors": {
                "B": "An MOU is a non-binding statement of intent/expectations between parties.",
                "C": "An NDA governs confidentiality of shared information.",
                "D": "A BPA defines the terms of a business partnership (roles, profit, responsibilities).",
            },
            "exam_pattern": "SLA = measurable service metrics + penalties. MOU = intent. MSA = master terms. "
                            "SOW = specific work/deliverables. BPA = partnership terms.",
        },
    },
    {
        "id": "secplus-mgmt-004", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_governance", "difficulty": 2, "type": "mcq",
        "stem": "Which governance document is a HIGH-LEVEL, mandatory statement of management's "
                "intent (e.g., 'all data must be protected'), as opposed to the step-by-step "
                "instructions for doing it?",
        "options": [
            {"id": "A", "text": "Policy"},
            {"id": "B", "text": "Procedure"},
            {"id": "C", "text": "Guideline"},
            {"id": "D", "text": "Standard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A policy is the high-level, mandatory statement of intent/direction. Procedures "
                       "give the exact steps; standards set specific requirements; guidelines are recommendations.",
            "distractors": {
                "B": "A procedure is the detailed, step-by-step 'how', not the high-level 'what/why'.",
                "C": "A guideline is a non-mandatory recommendation.",
                "D": "A standard specifies mandatory specifics (e.g., 'AES-256'), narrower than a policy.",
            },
            "exam_pattern": "Hierarchy: Policy (what/why, mandatory) → Standard (specific requirements) → "
                            "Procedure (how, steps) → Guideline (recommendations).",
        },
    },
    {
        "id": "secplus-mgmt-005", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "audits_assessments", "difficulty": 2, "type": "mcq",
        "stem": "A hired tester is given NO prior knowledge of the target environment and must "
                "discover everything as a real external attacker would. Which assessment is this?",
        "options": [
            {"id": "A", "text": "Unknown-environment (black-box) penetration test"},
            {"id": "B", "text": "Known-environment (white-box) penetration test"},
            {"id": "C", "text": "Credentialed vulnerability scan"},
            {"id": "D", "text": "Tabletop exercise"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "No prior knowledge = unknown-environment (black-box) testing, simulating an outside "
                       "attacker who must perform reconnaissance first.",
            "distractors": {
                "B": "Known-environment (white-box) gives the tester full information up front.",
                "C": "A vuln scan is automated detection, not an adversarial pen test.",
                "D": "A tabletop exercise is a discussion-based IR drill, not active testing.",
            },
            "exam_pattern": "Known = white-box (full info), partially known = gray-box, unknown = black-box (no info).",
        },
    },
    {
        "id": "secplus-mgmt-006", "exam": "secplus", "domain": "security_program_mgmt",
        "subtopic": "security_awareness", "difficulty": 1, "type": "mcq",
        "stem": "A company periodically sends fake phishing emails to staff and enrolls those who "
                "click into extra training. What is the PRIMARY goal of this program?",
        "options": [
            {"id": "A", "text": "Build users' ability to recognize and report phishing"},
            {"id": "B", "text": "Punish employees publicly for mistakes"},
            {"id": "C", "text": "Replace technical email filtering"},
            {"id": "D", "text": "Collect employees' personal data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Simulated phishing + targeted follow-up training measures and improves users' "
                       "recognition and reporting — reducing human risk, the hardest attack surface.",
            "distractors": {
                "B": "The aim is education, not public punishment (which harms reporting culture).",
                "C": "Awareness complements, not replaces, technical email filtering.",
                "D": "It's a training exercise, not a data-collection scheme.",
            },
            "exam_pattern": "Security awareness = recognize + report (phishing sims, anomalous-behavior "
                            "recognition); people are the top attack vector.",
        },
    },
]
