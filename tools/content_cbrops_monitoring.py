"""Cisco CyberOps Associate (CBROPS 200-201) pool - Domain 2: Security Monitoring.

Original, objective-aligned practice items for the six Security Monitoring
subtopics tracked in CertLab:
  * cbr_data_types            - the five categories of monitored data: full
                               packet capture, session data, transaction data,
                               statistical data, and alert data.
  * cbr_attack_surface_vectors- attack surface vs vulnerability, attack vectors,
                               and reducing the attack surface.
  * cbr_network_telemetry     - what NetFlow, tcpdump and next-gen firewall /
                               application visibility and control reveal, and
                               NetFlow vs full capture trade-offs.
  * cbr_detection_methods     - rule/signature detection vs behavioral, anomaly
                               and statistical detection.
  * cbr_evasion_obfuscation   - encryption, fragmentation, tunneling, proxies
                               and other techniques that defeat inspection.
  * cbr_certificates_crypto   - PKI/certificate components: CA, CSR, X.509
                               fields and the chain of trust.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item cites the public Cisco 200-201 exam topic it draws on. Blue-team /
analyst depth only, and never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cbr_data_types ===================================================
    {
        "id": "cbrops-mon-001", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "An analyst needs to reconstruct the exact bytes of a file an attacker transferred, "
                "including the full application payload. Which category of monitored data is required?",
        "options": [
            {"id": "A", "text": "Session data"},
            {"id": "B", "text": "Full packet capture"},
            {"id": "C", "text": "Statistical data"},
            {"id": "D", "text": "Alert data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Full packet capture records entire frames, headers and payload, so the complete "
                       "content of a transfer can be reconstructed - at the cost of heavy storage.",
            "distractors": {
                "A": "Session data (e.g., NetFlow) summarizes the conversation (5-tuple, bytes, timing) but holds no payload.",
                "C": "Statistical data describes traffic trends and baselines, not individual payloads.",
                "D": "Alert data is the notifications a sensor raises, not the raw content of the transfer.",
            },
            "exam_pattern": "Need the actual payload/content = full packet capture.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-002", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 1, "type": "mcq",
        "stem": "A record summarizes a single conversation between two hosts - source and destination "
                "IP and port, protocol, byte and packet counts, and start/stop times - but contains no "
                "payload. Which data type is this?",
        "options": [
            {"id": "A", "text": "Session data"},
            {"id": "B", "text": "Full packet capture"},
            {"id": "C", "text": "Alert data"},
            {"id": "D", "text": "Transaction data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session (connection) data summarizes a flow between two endpoints with metadata such "
                       "as the 5-tuple, counts and timestamps; NetFlow is the classic example.",
            "distractors": {
                "B": "Full packet capture includes the payload, which this record explicitly lacks.",
                "C": "Alert data is generated when a rule matches, not a per-conversation summary.",
                "D": "Transaction data records application-level requests/responses (e.g., an HTTP GET), not a flow summary.",
            },
            "exam_pattern": "Per-conversation summary (5-tuple + counts + times, no payload) = session data.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },
    {
        "id": "cbrops-mon-003", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_data_types", "difficulty": 2, "type": "mcq",
        "stem": "An IDS writes an entry only when traffic matches one of its rules and flags it as "
                "suspicious. These IDS-generated entries are an example of which monitored data type?",
        "options": [
            {"id": "A", "text": "Alert data"},
            {"id": "B", "text": "Statistical data"},
            {"id": "C", "text": "Session data"},
            {"id": "D", "text": "Full packet capture"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Alert data is produced by detection tools (IDS/IPS, antivirus) when a signature or "
                       "rule matches; it tells the analyst something notable was seen.",
            "distractors": {
                "B": "Statistical data is aggregated trend/baseline information, not per-match notifications.",
                "C": "Session data summarizes conversations regardless of whether they are suspicious.",
                "D": "Full packet capture stores all traffic content, not just rule matches.",
            },
            "exam_pattern": "Output of a sensor/rule match = alert data.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.4 Describe the uses of data types in security monitoring"],
    },

    # ===== cbr_attack_surface_vectors =======================================
    {
        "id": "cbrops-mon-004", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "How is an organization's 'attack surface' best described, as distinct from a single "
                "vulnerability?",
        "options": [
            {"id": "A", "text": "The sum of all points where an attacker could try to enter or extract data"},
            {"id": "B", "text": "A single specific weakness in one application"},
            {"id": "C", "text": "The code an attacker runs to exploit a flaw"},
            {"id": "D", "text": "The probability that an attack succeeds"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The attack surface is the total set of exposed entry and exit points (services, "
                       "ports, interfaces, accounts) an attacker could attempt to use; a vulnerability is one weakness within it.",
            "distractors": {
                "B": "A single weakness is a vulnerability, a component of the surface, not the surface itself.",
                "C": "Code that exploits a flaw is an exploit.",
                "D": "The probability an attack succeeds relates to risk, not the definition of the attack surface.",
            },
            "exam_pattern": "All exposed entry/exit points together = attack surface; one weakness = vulnerability.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.1 Compare attack surface and vulnerability"],
    },
    {
        "id": "cbrops-mon-005", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 1, "type": "mcq",
        "stem": "A phishing email carrying a malicious attachment is used to gain an initial foothold "
                "on a workstation. In this intrusion, the phishing email is best described as the ______.",
        "options": [
            {"id": "A", "text": "Attack vector"},
            {"id": "B", "text": "Attack surface"},
            {"id": "C", "text": "Vulnerability"},
            {"id": "D", "text": "Payload"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An attack vector is the path or means an attacker uses to reach and compromise a "
                       "target; a phishing email is a common vector for initial access.",
            "distractors": {
                "B": "The attack surface is the set of all possible entry points, not the one path used here.",
                "C": "A vulnerability is the weakness being exploited (e.g., a user tricked into opening a file), not the delivery path.",
                "D": "The payload is the malicious code that executes after delivery, not the delivery method itself.",
            },
            "exam_pattern": "The path/means of attack (phishing, USB, exposed service) = attack vector.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.1 Compare attack surface and vulnerability"],
    },
    {
        "id": "cbrops-mon-006", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_attack_surface_vectors", "difficulty": 2, "type": "mcq",
        "stem": "To harden a server, an administrator disables unused services, closes listening ports "
                "that are not needed, and removes default accounts. What is the primary security effect "
                "of these actions?",
        "options": [
            {"id": "A", "text": "It reduces the server's attack surface"},
            {"id": "B", "text": "It increases the server's attack surface"},
            {"id": "C", "text": "It eliminates all risk to the server"},
            {"id": "D", "text": "It converts vulnerabilities into exploits"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Each disabled service, closed port, and removed account is one fewer exposed entry "
                       "point, so the overall attack surface shrinks.",
            "distractors": {
                "B": "Removing exposure lowers the surface; it does not raise it.",
                "C": "Reducing exposure lowers risk but cannot eliminate all of it - avoid absolute claims.",
                "D": "Hardening removes weaknesses; it does not turn them into exploits.",
            },
            "exam_pattern": "Disable/close/remove unneeded exposure = smaller attack surface.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.1 Compare attack surface and vulnerability"],
    },

    # ===== cbr_network_telemetry ============================================
    {
        "id": "cbrops-mon-007", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 2, "type": "mcq",
        "stem": "A SOC uses NetFlow for network visibility. Which information does a standard NetFlow "
                "record provide to the analyst?",
        "options": [
            {"id": "A", "text": "Source/destination IP and port, protocol, and byte/packet counts for a flow"},
            {"id": "B", "text": "The full application-layer payload of each packet"},
            {"id": "C", "text": "The private key used in each TLS session"},
            {"id": "D", "text": "The plaintext of encrypted file transfers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NetFlow exports metadata about IP conversations - addresses, ports, protocol, "
                       "counters and timestamps - which scales well and reveals who talked to whom, when, and how much.",
            "distractors": {
                "B": "NetFlow does not capture payload; full packet capture is needed for that.",
                "C": "NetFlow never contains cryptographic keys.",
                "D": "NetFlow cannot decrypt traffic or reveal plaintext of encrypted transfers.",
            },
            "exam_pattern": "NetFlow = flow metadata (5-tuple + counts + times), no payload.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-008", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 2, "type": "mcq",
        "stem": "An application runs over a non-standard port to avoid detection, yet a next-generation "
                "firewall with application visibility and control still identifies it correctly. How is "
                "this possible?",
        "options": [
            {"id": "A", "text": "It identifies applications by inspecting traffic content/behavior, not just the port number"},
            {"id": "B", "text": "It assumes every flow on a non-standard port is that application"},
            {"id": "C", "text": "It reads the application name from the TCP port field"},
            {"id": "D", "text": "It decrypts and stores every packet payload permanently"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Application visibility and control on an NGFW identifies apps from traffic "
                       "characteristics and deep inspection, so it recognizes an app even when it moves to an unexpected port.",
            "distractors": {
                "B": "It does not guess from the port; that is exactly the port-based assumption AVC avoids.",
                "C": "There is no application-name field in a TCP header; the port alone does not name the app.",
                "D": "AVC classifies applications; it does not require permanently storing every decrypted payload.",
            },
            "exam_pattern": "Identifies apps regardless of port via inspection = NGFW application visibility and control.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },
    {
        "id": "cbrops-mon-009", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_network_telemetry", "difficulty": 3, "type": "mcq",
        "stem": "An analyst must retain months of connection history to spot slow beaconing but cannot "
                "afford to store full packets for that period. Compared with full packet capture, what "
                "is the main advantage of relying on NetFlow/session data here?",
        "options": [
            {"id": "A", "text": "It needs far less storage while still showing who talked to whom, when, and how much"},
            {"id": "B", "text": "It records the complete payload of every connection"},
            {"id": "C", "text": "It decrypts TLS so content is always visible"},
            {"id": "D", "text": "It guarantees zero false positives in detection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Session data is compact metadata, so it can be retained far longer than full packet "
                       "capture and is well suited to spotting long-term patterns like beaconing.",
            "distractors": {
                "B": "Recording full payloads is the strength of full capture, not of NetFlow.",
                "C": "NetFlow does not decrypt traffic.",
                "D": "No data source guarantees zero false positives.",
            },
            "exam_pattern": "Long retention of 'who/when/how much' with low storage = session data/NetFlow over full capture.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.2 Identify the types of data provided by these technologies"],
    },

    # ===== cbr_detection_methods ============================================
    {
        "id": "cbrops-mon-010", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 1, "type": "mcq",
        "stem": "A detection engine matches traffic against a database of known-bad patterns and alerts "
                "only when an incoming packet matches one. What is a key limitation of this "
                "signature/rule-based approach?",
        "options": [
            {"id": "A", "text": "It cannot detect new or unknown attacks that have no existing signature"},
            {"id": "B", "text": "It cannot detect any known attacks"},
            {"id": "C", "text": "It requires a baseline of normal behavior to work"},
            {"id": "D", "text": "It only works on encrypted traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Signature/rule-based detection is precise for known threats but blind to novel or "
                       "zero-day attacks for which no signature yet exists.",
            "distractors": {
                "B": "It is specifically good at catching known attacks; that is its purpose.",
                "C": "Needing a baseline of 'normal' describes behavioral/anomaly detection, not signature matching.",
                "D": "Signature matching works on readable traffic; encryption actually hinders it.",
            },
            "exam_pattern": "Known patterns only, misses zero-days = signature/rule-based detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },
    {
        "id": "cbrops-mon-011", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 2, "type": "mcq",
        "stem": "A monitoring system first learns a profile of each user's normal activity, then alerts "
                "when an account suddenly behaves very differently (for example, logging in at 3 a.m. "
                "and accessing servers it never touches). Which detection method is this?",
        "options": [
            {"id": "A", "text": "Behavioral / anomaly-based detection"},
            {"id": "B", "text": "Signature-based detection"},
            {"id": "C", "text": "Blocklist-based detection"},
            {"id": "D", "text": "Hash-based detection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Behavioral (anomaly) detection builds a baseline of normal behavior and flags "
                       "deviations, which lets it catch novel activity that no signature describes.",
            "distractors": {
                "B": "Signature-based detection matches known patterns and would not learn a per-user baseline.",
                "C": "A blocklist matches specific known-bad indicators, not deviations from learned behavior.",
                "D": "Hash-based detection identifies known files by their hash, not behavioral deviation.",
            },
            "exam_pattern": "Baseline 'normal' then flag deviations = behavioral/anomaly detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },
    {
        "id": "cbrops-mon-012", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_detection_methods", "difficulty": 3, "type": "mcq",
        "stem": "A system computes the normal mean and variance of traffic volume per hour and raises an "
                "alert when the current rate is several standard deviations above that norm. This is the "
                "clearest example of which detection approach?",
        "options": [
            {"id": "A", "text": "Statistical detection"},
            {"id": "B", "text": "Signature-based detection"},
            {"id": "C", "text": "Rule-based ACL filtering"},
            {"id": "D", "text": "Allowlist enforcement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Statistical detection uses mathematical measures of normal (means, variances, "
                       "thresholds) and flags values that deviate significantly, such as a sudden traffic spike.",
            "distractors": {
                "B": "Signature-based detection matches fixed known patterns, not statistical deviation.",
                "C": "A rule-based ACL permits/denies by fixed header criteria; it does no statistical analysis.",
                "D": "Allowlisting permits only approved items; it is not a statistical measure of traffic.",
            },
            "exam_pattern": "Means/variance/thresholds and deviation = statistical detection.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 1.11 Compare rule-based detection vs. behavioral and statistical detection"],
    },

    # ===== cbr_evasion_obfuscation ==========================================
    {
        "id": "cbrops-mon-013", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 2, "type": "mcq",
        "stem": "Malware communicates with its command-and-control server over TLS. Why does this "
                "encryption reduce the visibility of a signature-based IDS that only sees the wire "
                "traffic?",
        "options": [
            {"id": "A", "text": "The payload is ciphertext, so content signatures cannot match the hidden data"},
            {"id": "B", "text": "Encryption changes the destination IP address on every packet"},
            {"id": "C", "text": "Encrypted packets are never logged by any device"},
            {"id": "D", "text": "TLS removes the TCP/IP headers from the packets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encryption hides the payload as ciphertext, so an IDS inspecting content cannot "
                       "match signatures against it unless the traffic is first decrypted (e.g., via TLS inspection).",
            "distractors": {
                "B": "Encryption protects payload content; it does not rewrite the destination IP each packet.",
                "C": "Encrypted flows are still logged (NetFlow, firewall, proxy); only their content is opaque.",
                "D": "TLS encrypts the application data but leaves the IP/TCP headers readable for routing.",
            },
            "exam_pattern": "Encryption blinds content inspection (payload is ciphertext) while headers remain visible.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.3 Describe the impact of these technologies on data visibility"],
    },
    {
        "id": "cbrops-mon-014", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 2, "type": "mcq",
        "stem": "An attacker splits a malicious payload across many small IP fragments hoping the IDS "
                "evaluates each fragment alone and never reassembles the complete signature. Which "
                "evasion technique is this?",
        "options": [
            {"id": "A", "text": "Fragmentation"},
            {"id": "B", "text": "Symmetric encryption"},
            {"id": "C", "text": "Load balancing"},
            {"id": "D", "text": "Port security"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fragmentation-based evasion breaks an attack across packet fragments so a sensor "
                       "that does not fully reassemble traffic fails to see the whole malicious pattern.",
            "distractors": {
                "B": "Encryption hides content but does not rely on splitting the payload across fragments.",
                "C": "Load balancing distributes traffic for performance/availability; it is not an IDS-evasion method.",
                "D": "Port security is a switch feature limiting MAC addresses per port, not a packet-splitting evasion.",
            },
            "exam_pattern": "Split attack across fragments to defeat reassembly/signatures = fragmentation evasion.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.9 Describe evasion and obfuscation techniques"],
    },
    {
        "id": "cbrops-mon-015", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_evasion_obfuscation", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Encapsulating one protocol's traffic inside another - for example, "
                "smuggling command-and-control data inside DNS queries or ICMP packets to slip past "
                "inspection - is an evasion technique called ______.",
        "correct": ["tunneling", "tunnelling", "protocol tunneling"],
        "explanation": {
            "correct": "Tunneling hides traffic by wrapping it inside an allowed protocol (such as DNS or "
                       "ICMP), so inspection that trusts the outer protocol may miss the smuggled payload.",
            "exam_pattern": "Hiding traffic inside an allowed protocol (DNS/ICMP/HTTP) = tunneling.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.9 Describe evasion and obfuscation techniques"],
    },

    # ===== cbr_certificates_crypto ==========================================
    {
        "id": "cbrops-mon-016", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "mcq",
        "stem": "Before a web server can obtain a TLS certificate, it generates a request that contains "
                "its public key and identifying information and submits it to a certificate authority "
                "for signing. What is this request called?",
        "options": [
            {"id": "A", "text": "A certificate signing request (CSR)"},
            {"id": "B", "text": "A certificate revocation list (CRL)"},
            {"id": "C", "text": "A pre-shared key (PSK)"},
            {"id": "D", "text": "A session ticket"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CSR carries the applicant's public key and identity details to the CA, which "
                       "validates them and issues a signed certificate.",
            "distractors": {
                "B": "A CRL is the CA's published list of certificates it has revoked, not a request for one.",
                "C": "A pre-shared key is a shared secret for symmetric authentication, unrelated to requesting a certificate.",
                "D": "A session ticket resumes a prior TLS session; it is not a certificate request.",
            },
            "exam_pattern": "Public key + identity sent to the CA to be signed = CSR.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.11 Identify the certificate components in a given scenario"],
    },
    {
        "id": "cbrops-mon-017", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 3, "type": "mcq",
        "stem": "While inspecting a server's X.509 certificate, which of the following is a standard "
                "field an analyst should expect to find?",
        "options": [
            {"id": "A", "text": "The issuer's distinguished name and the validity period (Not Before / Not After)"},
            {"id": "B", "text": "The server's private key"},
            {"id": "C", "text": "The symmetric session key used for the connection"},
            {"id": "D", "text": "The certificate owner's account password"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An X.509 certificate contains the issuer and subject names, serial number, validity "
                       "dates, the subject's public key, and the CA's signature - the issuer DN and validity period are standard fields.",
            "distractors": {
                "B": "A certificate never contains the private key; the private key is kept secret by the owner.",
                "C": "The symmetric session key is negotiated per connection and is not stored in the certificate.",
                "D": "Passwords are not part of a certificate.",
            },
            "exam_pattern": "X.509 holds issuer/subject, validity, serial, public key, CA signature - never the private key.",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.11 Identify the certificate components in a given scenario"],
    },
    {
        "id": "cbrops-mon-018", "exam": "cbrops", "domain": "cbr_security_monitoring",
        "subtopic": "cbr_certificates_crypto", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In a public key infrastructure (PKI), the trusted entity that "
                "validates identities and issues and digitally signs digital certificates is called a "
                "______ (two words, or its abbreviation).",
        "correct": ["certificate authority", "certification authority", "ca"],
        "explanation": {
            "correct": "A certificate authority (CA) is the trusted PKI entity that verifies a requester's "
                       "identity and signs its certificate; clients trust the certificate because they trust the CA that signed it.",
            "exam_pattern": "Trusted issuer/signer of certificates in PKI = certificate authority (CA).",
        },
        "references": ["Cisco 200-201 CBROPS Exam Topics: 2.10 Describe the impact of certificates on security"],
    },
]
