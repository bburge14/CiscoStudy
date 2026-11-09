"""CompTIA SecurityX (CAS-005) pool - Domain 2: Security Architecture.

Original, objective-aligned practice items for the six Security Architecture
subtopics tracked in CertLab (expert/CASP+-level, scenario and trade-off driven):
  * scx_secure_architecture - defense in depth, attack-surface/secure-by-design,
                              network segmentation (east-west containment).
  * scx_zero_trust          - ZTA principles (never trust/assume breach), the
                              policy engine/administrator (PDP) and PEP,
                              microsegmentation, SASE/SSE and ZTNA.
  * scx_cloud_hybrid_arch   - CASB, CSPM/CWPP/CIEM/CNAPP, the shared
                              responsibility model across IaaS/PaaS/SaaS.
  * scx_resilience_ha       - RTO vs RPO, 3-2-1 backup, DR site types
                              (hot/warm/cold) and active-active failover.
  * scx_data_security_arch  - tokenization vs encryption, data states
                              (rest/transit/in use, confidential computing), HSM.
  * scx_iam_architecture    - SAML/OAuth 2.0/OIDC, federation and SSO, PAM.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so authored keys are spread across A-D (not
positionally biased), every wrong option carries a distractor note, and each
item cites the public CAS-005 objective domain it draws on. Expert depth with
BEST-given-constraints framing - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== scx_secure_architecture ==========================================
    {
        "id": "securityx-arch-001", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 2, "type": "mcq",
        "stem": "A security architect designs a system so that even if an attacker bypasses the perimeter "
                "firewall, they still face host hardening, network segmentation, least-privilege access, and "
                "monitoring before reaching sensitive data. Which design principle is MOST directly illustrated?",
        "options": [
            {"id": "A", "text": "Security through obscurity"},
            {"id": "B", "text": "Defense in depth (layered security)"},
            {"id": "C", "text": "A single point of failure"},
            {"id": "D", "text": "Implicit trust"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defense in depth layers independent controls so the failure or bypass of any one control does not compromise the whole system.",
            "distractors": {
                "A": "Security through obscurity relies on secrecy of design and is not a layered-control strategy.",
                "C": "A single point of failure is a weakness to avoid, the opposite of layered resilience.",
                "D": "Implicit trust is what layered security (and zero trust) seek to remove, not a design goal here.",
            },
            "exam_pattern": "Multiple independent layers so one failure isn't fatal = defense in depth.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure enterprise architecture (defense in depth)"],
    },
    {
        "id": "securityx-arch-002", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 3, "type": "mcq",
        "stem": "A product team is finalizing a new service and wants to minimize what an external attacker "
                "can reach or exploit. Disabling unused services and ports, removing default accounts, and "
                "exposing only required APIs most directly accomplishes which objective?",
        "options": [
            {"id": "A", "text": "Increasing cyclomatic complexity"},
            {"id": "B", "text": "Improving mean time to detect (MTTD)"},
            {"id": "C", "text": "Reducing the attack surface"},
            {"id": "D", "text": "Achieving nonrepudiation"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Turning off unneeded services, ports, accounts, and interfaces reduces the number of "
                       "exposed entry points - the attack surface - a core secure-by-design/secure-by-default practice.",
            "distractors": {
                "A": "Cyclomatic complexity is a code-complexity metric; these hardening steps do not aim to change it.",
                "B": "MTTD measures detection speed; reducing exposure is prevention, not detection timing.",
                "D": "Nonrepudiation ensures actions cannot be denied (via signing/logging), unrelated to removing exposed services.",
            },
            "exam_pattern": "Disable/remove what isn't needed = attack-surface reduction (secure by design/default).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (attack surface reduction, secure by design)"],
    },
    {
        "id": "securityx-arch-003", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_secure_architecture", "difficulty": 2, "type": "mcq",
        "stem": "After a breach, investigators found that once inside, the attacker moved freely between the "
                "HR, finance, and OT networks because they shared one flat Layer 2 domain. Which architectural "
                "change BEST limits such lateral (east-west) movement in the future?",
        "options": [
            {"id": "A", "text": "Increase internet bandwidth to the sites"},
            {"id": "B", "text": "Deploy a single larger perimeter firewall only"},
            {"id": "C", "text": "Enable full-disk encryption on servers"},
            {"id": "D", "text": "Implement network segmentation (and microsegmentation) to isolate zones"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Segmenting the network into isolated zones (and microsegmenting critical workloads) "
                       "constrains east-west movement so a foothold in one zone does not grant free access to others.",
            "distractors": {
                "A": "More bandwidth has no bearing on containing lateral movement.",
                "B": "A bigger perimeter firewall addresses north-south traffic but not east-west movement within a flat internal network.",
                "C": "Full-disk encryption protects data at rest on stolen media; it does not stop an authenticated attacker pivoting across a flat network.",
            },
            "exam_pattern": "Flat network enabling lateral movement -> segmentation/microsegmentation to contain east-west traffic.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Secure architecture (segmentation, east-west traffic)"],
    },

    # ===== scx_zero_trust ===================================================
    {
        "id": "securityx-arch-004", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 2, "type": "mcq",
        "stem": "An enterprise adopts an architecture where no user or device is trusted by default based on "
                "network location, every request is authenticated and authorized continuously, and the design "
                "assumes the environment is already compromised. Which model is this?",
        "options": [
            {"id": "A", "text": "Zero trust (never trust, always verify; assume breach)"},
            {"id": "B", "text": "Classic castle-and-moat perimeter security"},
            {"id": "C", "text": "Discretionary access control only"},
            {"id": "D", "text": "Air-gapped isolation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Zero trust removes implicit trust based on network location, verifies every request "
                       "explicitly and continuously, enforces least privilege, and assumes breach.",
            "distractors": {
                "B": "Castle-and-moat trusts anything inside the perimeter - the very assumption zero trust rejects.",
                "C": "DAC is an access-control model about owner-granted permissions, not an enterprise trust architecture.",
                "D": "An air gap physically isolates a network; it is not the continuous-verification model described.",
            },
            "exam_pattern": "No location-based trust + verify every request + assume breach = zero trust.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust architecture (NIST SP 800-207 principles)"],
    },
    {
        "id": "securityx-arch-005", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "In a NIST SP 800-207 zero trust architecture, one logical component evaluates policy and "
                "decides whether to grant access, while a separate component sits in the data path and "
                "actually enforces that decision for each connection. These are BEST described as the:",
        "options": [
            {"id": "A", "text": "Certificate authority and the registration authority"},
            {"id": "B", "text": "SIEM and the SOAR platform"},
            {"id": "C", "text": "Policy decision point (policy engine + policy administrator) and the policy enforcement point (PEP)"},
            {"id": "D", "text": "Intrusion detection system and the intrusion prevention system"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "In 800-207, the policy engine (PE) makes the grant/deny decision and the policy "
                       "administrator (PA) executes it - together the policy decision point (PDP) - while the policy enforcement point (PEP) sits in the path and enforces access per request.",
            "distractors": {
                "A": "CA/RA are PKI roles for issuing and registering certificates, not ZTA access-decision/enforcement components.",
                "B": "SIEM/SOAR handle analytics and automated response, not the per-request access decision/enforcement split.",
                "D": "IDS/IPS detect or block known attack patterns; they are not the ZTA PDP/PEP policy components.",
            },
            "exam_pattern": "ZTA: policy engine + policy administrator = PDP (decides); PEP enforces in the data path.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (policy engine/administrator/PDP, PEP)"],
    },
    {
        "id": "securityx-arch-006", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "A zero-trust initiative needs to enforce identity-aware, per-workload policies between "
                "individual virtual machines in the same data-center subnet - including blocking east-west "
                "traffic that a traditional VLAN would permit. Which technique is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Adding more entries to the perimeter firewall ruleset"},
            {"id": "B", "text": "Microsegmentation (software-defined, per-workload policy)"},
            {"id": "C", "text": "Widening the subnet mask to merge VLANs"},
            {"id": "D", "text": "Enabling jumbo frames on the switches"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsegmentation applies fine-grained, identity/workload-aware policy down to individual "
                       "hosts or workloads, controlling east-west traffic that coarse VLAN/subnet boundaries would otherwise allow.",
            "distractors": {
                "A": "Perimeter firewall rules govern north-south traffic and cannot granularly control VM-to-VM traffic inside the same subnet.",
                "C": "Merging VLANs reduces isolation - the opposite of the goal.",
                "D": "Jumbo frames affect packet size/throughput, not segmentation policy.",
            },
            "exam_pattern": "Per-workload east-west control inside a subnet = microsegmentation, not VLANs/perimeter rules.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (microsegmentation)"],
    },
    {
        "id": "securityx-arch-007", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_zero_trust", "difficulty": 3, "type": "mcq",
        "stem": "A company with a fully remote workforce wants to retire its VPN concentrator and deliver "
                "security controls (secure web gateway, CASB, ZTNA, firewall-as-a-service) from a "
                "cloud-delivered service that converges networking and security at the edge, close to users. "
                "Which model BEST describes this?",
        "options": [
            {"id": "A", "text": "A traditional DMZ"},
            {"id": "B", "text": "A host-based IDS deployment"},
            {"id": "C", "text": "A site-to-site IPsec mesh"},
            {"id": "D", "text": "SASE (Secure Access Service Edge), whose security stack is the SSE component"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SASE converges SD-WAN networking with cloud-delivered security (SWG, CASB, ZTNA, FWaaS) "
                       "at the edge; the security portion alone (SWG, CASB, ZTNA, FWaaS, DLP) is Security Service Edge (SSE), and ZTNA replaces implicit-trust VPN access.",
            "distractors": {
                "A": "A DMZ is a perimeter network segment, not a cloud-delivered converged networking+security service.",
                "B": "A host-based IDS monitors a single host; it does not deliver converged edge security for a remote workforce.",
                "C": "A site-to-site IPsec mesh connects sites but doesn't provide the converged, identity-aware cloud security stack or replace user VPN with ZTNA.",
            },
            "exam_pattern": "Cloud-delivered SWG+CASB+ZTNA+FWaaS converged with networking = SASE; the security-only slice = SSE; ZTNA supersedes VPN.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Zero trust (SASE/SSE, ZTNA)"],
    },

    # ===== scx_cloud_hybrid_arch ============================================
    {
        "id": "securityx-arch-008", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 2, "type": "mcq",
        "stem": "Security leadership wants visibility and policy enforcement over employees' use of sanctioned "
                "and unsanctioned SaaS apps - including detecting shadow IT, enforcing DLP, and controlling data "
                "sharing - as a control point between users and cloud services. Which technology fits BEST?",
        "options": [
            {"id": "A", "text": "A cloud access security broker (CASB)"},
            {"id": "B", "text": "A hardware security module (HSM)"},
            {"id": "C", "text": "A host-based firewall"},
            {"id": "D", "text": "A jump box (bastion host)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A CASB sits between users and cloud services as a policy-enforcement point, providing "
                       "visibility (including shadow-IT discovery), data security/DLP, compliance, and threat protection for SaaS usage.",
            "distractors": {
                "B": "An HSM safeguards cryptographic keys; it does not broker or monitor SaaS usage.",
                "C": "A host-based firewall filters traffic on one host, not enterprise-wide SaaS governance.",
                "D": "A jump box provides controlled administrative access to systems, not SaaS visibility/DLP.",
            },
            "exam_pattern": "Visibility + DLP + shadow-IT control for SaaS = CASB (its four pillars: visibility, compliance, data security, threat protection).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (CASB)"],
    },
    {
        "id": "securityx-arch-009", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 3, "type": "mcq",
        "stem": "A multicloud enterprise wants one platform that unifies cloud security posture management, "
                "workload protection, and entitlement management across its providers - correlating "
                "misconfigurations, vulnerabilities, and identity risk into a single view. Which category "
                "BEST describes this?",
        "options": [
            {"id": "A", "text": "CSPM only (posture/misconfiguration management)"},
            {"id": "B", "text": "CWPP only (workload protection)"},
            {"id": "C", "text": "CNAPP (cloud-native application protection platform, converging CSPM, CWPP, CIEM, and more)"},
            {"id": "D", "text": "A WAF (web application firewall)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A CNAPP converges capabilities - CSPM (posture/misconfiguration), CWPP (workload protection), "
                       "and CIEM (entitlements) - into one platform spanning development and runtime across clouds.",
            "distractors": {
                "A": "CSPM alone covers posture/misconfiguration but not workload protection or entitlement management.",
                "B": "CWPP alone protects workloads (VMs, containers) but doesn't cover posture or identity entitlements across clouds.",
                "D": "A WAF filters web application traffic; it is not a converged cloud-native protection platform.",
            },
            "exam_pattern": "Unified posture + workload + entitlement across clouds = CNAPP (umbrella over CSPM + CWPP + CIEM).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (CNAPP, CSPM, CWPP, CIEM)"],
    },
    {
        "id": "securityx-arch-010", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_cloud_hybrid_arch", "difficulty": 2, "type": "mcq",
        "stem": "Under the cloud shared responsibility model, a team deploys applications on an IaaS virtual "
                "machine. Which task remains the CUSTOMER's responsibility under IaaS that would instead shift "
                "to the provider under SaaS?",
        "options": [
            {"id": "A", "text": "Securing the physical data-center facility"},
            {"id": "B", "text": "Patching and hardening the guest operating system"},
            {"id": "C", "text": "Maintaining the hypervisor host hardware"},
            {"id": "D", "text": "Securing the underlying storage area network fabric"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "In IaaS the customer manages the guest OS (patching, hardening) and everything above it; "
                       "under SaaS the provider manages the OS and application, so that responsibility shifts to the provider.",
            "distractors": {
                "A": "Physical facility security is always the provider's responsibility in IaaS, PaaS, and SaaS.",
                "C": "The hypervisor host hardware is the provider's responsibility across cloud service models.",
                "D": "The underlying storage fabric is provider-managed infrastructure, not a customer IaaS duty.",
            },
            "exam_pattern": "IaaS: customer owns guest OS and up; moving toward SaaS shifts OS/app to the provider; physical/host/fabric always provider.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Cloud/hybrid architecture (shared responsibility model)"],
    },

    # ===== scx_resilience_ha ================================================
    {
        "id": "securityx-arch-011", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the three-letter acronym: The maximum tolerable amount of data loss, "
                "expressed as a period of time (e.g., 'up to 15 minutes of transactions'), is the recovery "
                "point objective, abbreviated ______.",
        "correct": ["rpo"],
        "explanation": {
            "correct": "RPO (recovery point objective) is the maximum tolerable data loss measured in time and "
                       "drives backup/replication frequency; RTO is the maximum tolerable time to restore service.",
            "distractors": {},
            "exam_pattern": "RPO = how much data you can lose (points back in time -> backup frequency); RTO = how long to recover (downtime).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (RPO vs RTO)"],
    },
    {
        "id": "securityx-arch-012", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 2, "type": "mcq",
        "stem": "A ransomware tabletop exercise reveals that all backups are stored on a single NAS in the same "
                "building as production. To align with the widely recommended backup rule, which change should "
                "the team make?",
        "options": [
            {"id": "A", "text": "Keep 3 copies of data on 2 different media types with 1 copy off-site (3-2-1), ideally adding an offline/immutable copy"},
            {"id": "B", "text": "Keep a single encrypted copy on the same NAS"},
            {"id": "C", "text": "Replicate synchronously to a second LUN on the same NAS"},
            {"id": "D", "text": "Increase backup frequency on the existing NAS only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 3-2-1 rule - three copies, on two different media, with one off-site (often extended "
                       "with one offline/air-gapped or immutable copy) - protects against site loss and ransomware that targets reachable backups.",
            "distractors": {
                "B": "A single copy on the same device fails every part of 3-2-1 and is destroyed with the site or by ransomware reaching the NAS.",
                "C": "Replicating within the same NAS keeps all copies in one failure domain and still on-site.",
                "D": "More frequent backups to the same device add no media diversity and no off-site/offline copy.",
            },
            "exam_pattern": "3-2-1: 3 copies, 2 media, 1 off-site (add 1 offline/immutable for ransomware resilience).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (backup strategy, 3-2-1)"],
    },
    {
        "id": "securityx-arch-013", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_resilience_ha", "difficulty": 3, "type": "mcq",
        "stem": "A payment platform has an extremely low RTO: it must resume processing within minutes of a "
                "regional outage. Cost is secondary to meeting this target. Which disaster-recovery approach "
                "BEST fits?",
        "options": [
            {"id": "A", "text": "A cold site with backups shipped in after a disaster"},
            {"id": "B", "text": "A warm site with periodic data replication and partial equipment"},
            {"id": "C", "text": "Restore from off-site tape to newly procured hardware after an event"},
            {"id": "D", "text": "A hot site (or active-active multi-region) with real-time replication and near-immediate failover"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "A hot site - or an active-active multi-region design - with real-time data replication "
                       "supports near-immediate failover, meeting a very low RTO when cost is secondary.",
            "distractors": {
                "A": "A cold site has no ready systems or current data; recovery takes days, far exceeding a minutes-level RTO.",
                "B": "A warm site shortens recovery versus cold, but its periodic replication and partial readiness can't meet a minutes-level RTO.",
                "C": "Restoring from tape to new hardware is among the slowest options and cannot meet a minutes-level RTO.",
            },
            "exam_pattern": "Lowest RTO, cost secondary -> hot site / active-active with real-time replication; cold = cheapest but slowest.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Resilience/HA (DR site types, RTO)"],
    },

    # ===== scx_data_security_arch ===========================================
    {
        "id": "securityx-arch-014", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A retailer wants to remove stored credit-card numbers from its order-history database to shrink "
                "PCI DSS scope, while still letting staff reference a stand-in value that has no mathematical "
                "relationship to the original PAN and can be mapped back only through a separate secured vault. "
                "Which technique BEST fits?",
        "options": [
            {"id": "A", "text": "Format-preserving encryption applied in place"},
            {"id": "B", "text": "Tokenization (replace the PAN with a non-sensitive token mapped in a secure vault)"},
            {"id": "C", "text": "Base64 encoding of the PAN"},
            {"id": "D", "text": "Hashing the PAN with unsalted MD5"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Tokenization substitutes the sensitive value with a token that has no algorithmic "
                       "relationship to the original; the mapping lives in a secured token vault, removing the real PAN from the database and reducing PCI scope.",
            "distractors": {
                "A": "Encryption (even format-preserving) keeps a reversible ciphertext derived from the data and its keys in scope, rather than removing the value via a separate vault lookup.",
                "C": "Base64 is reversible encoding, not protection - anyone can decode it.",
                "D": "Unsalted MD5 is a broken one-way hash, unsuitable for a value that must be referenced/mapped back and easily attacked.",
            },
            "exam_pattern": "No mathematical relationship + vault lookup + reduce PCI scope = tokenization; encryption keeps reversible ciphertext in scope.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (tokenization vs encryption)"],
    },
    {
        "id": "securityx-arch-015", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 3, "type": "mcq",
        "stem": "A research consortium must run analytics on highly sensitive data in an untrusted cloud without "
                "ever exposing the plaintext to the cloud provider - protecting the data even while it is being "
                "processed (data in use). Which approach MOST directly addresses protecting data in use?",
        "options": [
            {"id": "A", "text": "Confidential computing (trusted execution environments / secure enclaves) and/or homomorphic encryption"},
            {"id": "B", "text": "TLS 1.3 for all connections"},
            {"id": "C", "text": "AES-256 full-disk encryption on the storage volumes"},
            {"id": "D", "text": "A firewall rule restricting source IP addresses"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Protecting data in use requires computing on protected data - confidential computing with "
                       "hardware trusted execution environments (secure enclaves) keeps data encrypted/isolated during processing, and homomorphic encryption allows computation directly on ciphertext.",
            "distractors": {
                "B": "TLS protects data in transit, not while it is being processed in memory.",
                "C": "Full-disk encryption protects data at rest; the data is decrypted when processed.",
                "D": "An IP firewall rule controls network access, not protection of data during computation.",
            },
            "exam_pattern": "Three states: at rest (disk/FDE), in transit (TLS), in use (confidential computing/enclaves, homomorphic).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (encryption states; data in use)"],
    },
    {
        "id": "securityx-arch-016", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_data_security_arch", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank with the acronym: A dedicated, tamper-resistant hardware appliance that "
                "generates, stores, and protects cryptographic keys and performs crypto operations - often "
                "validated to FIPS 140-2/140-3 - is a hardware security module, abbreviated ______.",
        "correct": ["hsm"],
        "explanation": {
            "correct": "An HSM is a hardened, tamper-resistant device for key generation, storage, and cryptographic "
                       "operations, keeping keys out of general-purpose memory and commonly FIPS 140-2/140-3 validated.",
            "distractors": {},
            "exam_pattern": "Tamper-resistant key storage/crypto hardware, FIPS 140 validated = HSM (keys never leave in plaintext).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — Data security architecture (HSM, key protection)"],
    },

    # ===== scx_iam_architecture =============================================
    {
        "id": "securityx-arch-017", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "mcq",
        "stem": "An architect is choosing identity protocols. They need (1) browser-based SSO to an enterprise "
                "SaaS app using XML assertions, and (2) a modern delegated-authorization protocol plus an "
                "identity layer on top of it for a mobile app's API access. Which pairing is correct?",
        "options": [
            {"id": "A", "text": "(1) OAuth 2.0; (2) SAML with OpenID Connect"},
            {"id": "B", "text": "(1) RADIUS; (2) Kerberos"},
            {"id": "C", "text": "(1) OpenID Connect; (2) SAML"},
            {"id": "D", "text": "(1) SAML; (2) OAuth 2.0 with OpenID Connect (OIDC)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "SAML uses XML assertions and is widely used for enterprise web SSO; OAuth 2.0 is a "
                       "delegated-authorization framework, and OpenID Connect adds an identity (authentication) layer on top of OAuth 2.0 - ideal for mobile/API scenarios.",
            "distractors": {
                "A": "This reverses the roles - OAuth 2.0 is not the XML-assertion web-SSO protocol, and SAML is not layered on OAuth.",
                "B": "RADIUS and Kerberos are authentication protocols for network/enterprise access, not the XML-SSO and delegated-authorization roles described.",
                "C": "OIDC is not XML-assertion SSO, and SAML is not a delegated-authorization framework with an identity layer added.",
            },
            "exam_pattern": "SAML = XML web SSO; OAuth 2.0 = authorization (delegated access); OIDC = authentication layer on OAuth 2.0.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (SAML, OAuth 2.0, OIDC/federation)"],
    },
    {
        "id": "securityx-arch-018", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the risk of standing administrative access, an enterprise wants to vault privileged "
                "credentials, broker just-in-time elevation with approval, and record privileged sessions. "
                "Which solution category is this?",
        "options": [
            {"id": "A", "text": "A CASB"},
            {"id": "B", "text": "A SIEM"},
            {"id": "C", "text": "Privileged access management (PAM)"},
            {"id": "D", "text": "A consumer password manager for end users"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "PAM secures privileged accounts via credential vaulting, just-in-time / least-privilege "
                       "elevation with approvals, session brokering, and session recording - directly reducing standing-admin risk.",
            "distractors": {
                "A": "A CASB governs cloud/SaaS usage, not privileged-credential vaulting and JIT elevation.",
                "B": "A SIEM aggregates and analyzes logs; it monitors but does not broker or vault privileged access.",
                "D": "A consumer password manager stores personal passwords but lacks JIT elevation, approval workflows, and session recording.",
            },
            "exam_pattern": "Vault + JIT elevation + session recording for admins = PAM (privileged access management).",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (PAM)"],
    },
    {
        "id": "securityx-arch-019", "exam": "securityx", "domain": "scx_architecture",
        "subtopic": "scx_iam_architecture", "difficulty": 3, "type": "multi",
        "stem": "An organization implements federated identity so partners' users can access its applications "
                "using the partners' home identity providers. Which TWO statements accurately describe "
                "federation? (Choose two.)",
        "options": [
            {"id": "A", "text": "Authentication is performed by the user's home identity provider (IdP), and the relying party (service provider) trusts the resulting assertion/token."},
            {"id": "B", "text": "Each application must store and manage the partner users' passwords locally."},
            {"id": "C", "text": "It enables single sign-on across organizational boundaries via trust relationships and standards such as SAML or OIDC."},
            {"id": "D", "text": "It eliminates the need for any trust configuration between the parties."},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "In federation the home IdP authenticates the user and issues an assertion/token the service "
                       "provider trusts, enabling cross-domain SSO through standards like SAML or OIDC.",
            "distractors": {
                "B": "Federation's benefit is that the relying party does NOT store partner credentials - the home IdP holds them.",
                "D": "Federation fundamentally depends on an explicit, configured trust relationship between IdP and relying party; it does not remove that need.",
            },
            "exam_pattern": "Federation = home IdP authenticates, relying party trusts the token; enables cross-domain SSO; requires a configured trust.",
        },
        "references": ["CompTIA SecurityX CAS-005 Objectives: Domain 2 — IAM architecture (federation, SSO, SAML/OIDC)"],
    },
]
