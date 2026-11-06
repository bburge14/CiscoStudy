"""CompTIA Security+ SY0-701 — Domain 4.0 Security Operations expansion pool.

Original, objective-aligned items that DEEPEN the base `content_secplus.py`
bank for the heavily weighted Security Operations domain (0.28 of the exam).
Content is mapped to the public SY0-701 objectives, never copied from any real
exam. build_content.py shuffles option order, so the keyed id below is not
positionally biased.

Scope: all eight 4.0 subtopics — secure_baselines_hardening, asset_management,
vulnerability_management, security_monitoring, identity_access_management,
automation_orchestration, incident_response, digital_forensics. These items are
NEW and do not duplicate the base pool's secplus-ops-001..006.
"""

QUESTIONS = [
    # ===== 4.1 Secure baselines & hardening =================================
    {
        "id": "secplus-ops-101", "exam": "secplus", "domain": "security_operations",
        "subtopic": "secure_baselines_hardening", "difficulty": 2, "type": "mcq",
        "stem": "An administrator must apply one hardened configuration (password policy, "
                "disabled services, audit settings) to hundreds of domain-joined Windows "
                "workstations AND have it automatically reapplied if a user changes a "
                "setting. Which tool is BEST?",
        "options": [
            {"id": "A", "text": "Group Policy (GPO)"},
            {"id": "B", "text": "A one-time manual checklist run on each PC"},
            {"id": "C", "text": "A host-based firewall"},
            {"id": "D", "text": "Full-disk encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Group Policy centrally defines and continuously ENFORCES the baseline across "
                       "every domain-joined host, reapplying settings on refresh — the configuration "
                       "enforcement the objective calls for.",
            "distractors": {
                "B": "A manual checklist does not scale to hundreds of hosts and does not reapply "
                     "the setting if a user changes it.",
                "C": "A host firewall controls network traffic to/from the host, not the full set "
                     "of OS configuration settings.",
                "D": "Full-disk encryption protects data at rest; it does not enforce a configuration baseline.",
            },
            "exam_pattern": "Consistent, self-healing config across many hosts = baseline/config enforcement "
                            "via Group Policy (Windows) or similar config-management tooling.",
        },
    },
    {
        "id": "secplus-ops-102", "exam": "secplus", "domain": "security_operations",
        "subtopic": "secure_baselines_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Laptops issued to a travelling sales team are frequently lost. Which hardening "
                "control MOST directly protects the confidentiality of data on a stolen laptop's "
                "drive, even if the thief removes the drive?",
        "options": [
            {"id": "A", "text": "Full-disk encryption (FDE)"},
            {"id": "B", "text": "A host-based intrusion detection system"},
            {"id": "C", "text": "A screensaver password"},
            {"id": "D", "text": "Disabling unused USB ports"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FDE encrypts the entire volume, so data is unreadable without the key even if "
                       "the drive is pulled and attached to another machine.",
            "distractors": {
                "B": "A HIDS detects suspicious activity on a running system; it does nothing for a "
                     "powered-off drive removed by a thief.",
                "C": "A screensaver password is bypassed by removing the drive and reading it elsewhere.",
                "D": "Disabling USB ports reduces peripheral attack surface but does not protect data stored on the disk.",
            },
            "exam_pattern": "Lost/stolen device + protect data AT REST = full-disk encryption (often with a TPM).",
        },
    },
    {
        "id": "secplus-ops-103", "exam": "secplus", "domain": "security_operations",
        "subtopic": "secure_baselines_hardening", "difficulty": 3, "type": "mcq",
        "stem": "A plant runs legacy ICS/SCADA controllers that cannot be patched or run an EDR "
                "agent without voiding vendor support. Which hardening approach is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Place them on an isolated, segmented network with strict access controls"},
            {"id": "B", "text": "Expose them directly to the internet so the vendor can patch remotely"},
            {"id": "C", "text": "Install consumer desktop antivirus on each controller"},
            {"id": "D", "text": "Enable automatic operating-system feature updates"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When specialized/embedded systems can't be patched or protected directly, isolating "
                       "and segmenting them behind tight access controls is the standard compensating "
                       "hardening measure.",
            "distractors": {
                "B": "Exposing fragile OT controllers to the internet dramatically increases risk — the opposite of hardening.",
                "C": "These controllers often cannot run standard AV, and doing so is typically unsupported and can destabilize them.",
                "D": "Automatic updates can break fragile ICS/SCADA and are usually unsupported on such systems.",
            },
            "exam_pattern": "Unpatchable ICS/SCADA/embedded/RTOS → isolate + segment + restrict access (compensating control).",
        },
    },
    {
        "id": "secplus-ops-104", "exam": "secplus", "domain": "security_operations",
        "subtopic": "secure_baselines_hardening", "difficulty": 1, "type": "mcq",
        "stem": "Before deploying new IoT cameras and network switches, the FIRST item on the "
                "hardening checklist is to change the vendor-supplied admin credentials. Why is "
                "this so important?",
        "options": [
            {"id": "A", "text": "Default credentials are publicly documented and heavily targeted by attackers"},
            {"id": "B", "text": "Default passwords use weak hashing that slows the device down"},
            {"id": "C", "text": "Changing them automatically enables full-disk encryption"},
            {"id": "D", "text": "It is required before any host firewall port can open"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Vendor default usernames/passwords are listed in manuals and online databases and are "
                       "among the first things attackers and botnets (e.g., Mirai) try.",
            "distractors": {
                "B": "The risk is public knowledge of the credential, not hashing performance.",
                "C": "Credentials are unrelated to enabling disk encryption.",
                "D": "Changing a password has nothing to do with opening firewall ports.",
            },
            "exam_pattern": "Hardening always includes removing/changing DEFAULT accounts and passwords.",
        },
    },

    # ===== 4.2 Asset management =============================================
    {
        "id": "secplus-ops-105", "exam": "secplus", "domain": "security_operations",
        "subtopic": "asset_management", "difficulty": 2, "type": "mcq",
        "stem": "A hospital must dispose of FAILED SSDs that held patient records. The drives are "
                "dead (cannot be overwritten) and degaussing does not work on them. Which method "
                "ensures the data cannot be recovered?",
        "options": [
            {"id": "A", "text": "Physical destruction (shredding/pulverizing)"},
            {"id": "B", "text": "Degaussing with a magnetic wand"},
            {"id": "C", "text": "A single quick format"},
            {"id": "D", "text": "Sending the drives to the recycle bin and emptying it"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Flash/SSD media have no magnetic domains and the drives are unwriteable, so physical "
                       "destruction is the reliable sanitization method here.",
            "distractors": {
                "B": "Degaussing only affects magnetic media (HDD/tape); it has no effect on solid-state flash.",
                "C": "A format leaves the underlying data recoverable, and a dead drive may not format at all.",
                "D": "Emptying the recycle bin removes pointers, not the data itself.",
            },
            "exam_pattern": "Dead or flash media that can't be overwritten/degaussed → destroy (shred/pulverize/incinerate).",
        },
    },
    {
        "id": "secplus-ops-106", "exam": "secplus", "domain": "security_operations",
        "subtopic": "asset_management", "difficulty": 2, "type": "mcq",
        "stem": "An organization pays a third-party vendor to destroy decommissioned drives off-site. "
                "What should it obtain for each batch to prove destruction occurred for audit and "
                "compliance purposes?",
        "options": [
            {"id": "A", "text": "A certificate of destruction"},
            {"id": "B", "text": "A software license key"},
            {"id": "C", "text": "A penetration-test report"},
            {"id": "D", "text": "Only a verbal confirmation from the driver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A certificate of destruction documents what was destroyed, when, how, and by whom — the "
                       "evidence auditors expect for sanitized/decommissioned assets.",
            "distractors": {
                "B": "A license key is unrelated to media disposal.",
                "C": "A pentest report assesses exploitable weaknesses, not disposal.",
                "D": "A verbal confirmation is not auditable evidence.",
            },
            "exam_pattern": "Third-party disposal/decommissioning → require a certificate of destruction (certification).",
        },
    },
    {
        "id": "secplus-ops-107", "exam": "secplus", "domain": "security_operations",
        "subtopic": "asset_management", "difficulty": 3, "type": "multi", "select_count": 2,
        "stem": "A company is sanitizing HDDs that will be REUSED internally (not destroyed). Which "
                "TWO methods sanitize the data while keeping the drives usable? (Select TWO.)",
        "options": [
            {"id": "A", "text": "Overwriting/wiping the drive with a multi-pass pattern"},
            {"id": "B", "text": "Cryptographic erase (destroying the encryption keys on a self-encrypting drive)"},
            {"id": "C", "text": "Degaussing the drive"},
            {"id": "D", "text": "Physical shredding"},
            {"id": "E", "text": "Deleting the files and emptying the recycle bin"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Overwriting (NIST 'clear') and cryptographic erase (destroying the keys) both render the "
                       "old data unrecoverable while leaving the drive functional for reuse.",
            "distractors": {
                "C": "Degaussing erases a magnetic HDD's factory servo tracks, destroying the drive — it cannot be reused.",
                "D": "Shredding physically destroys the drive; reuse is impossible.",
                "E": "Deleting files and emptying the bin leaves the data fully recoverable — it is not sanitization.",
            },
            "exam_pattern": "Reuse → overwrite or crypto-erase. Dispose for good → degauss (HDD) or destroy (shred).",
        },
    },

    # ===== 4.3 Vulnerability management =====================================
    {
        "id": "secplus-ops-108", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 2, "type": "mcq",
        "stem": "A scan returns three findings with CVSS base scores of 9.8, 5.4, and 2.1. With limited "
                "time and all else equal, which should the team remediate FIRST?",
        "options": [
            {"id": "A", "text": "The 9.8 (Critical)"},
            {"id": "B", "text": "The 5.4 (Medium)"},
            {"id": "C", "text": "The 2.1 (Low)"},
            {"id": "D", "text": "Whichever finding was discovered first"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CVSS base scores rank severity (9.0–10.0 = Critical). Prioritizing the 9.8 addresses "
                       "the greatest risk first.",
            "distractors": {
                "B": "A 5.4 Medium is lower severity than a 9.8 Critical.",
                "C": "A 2.1 Low poses the least risk of the three.",
                "D": "Discovery order is not a measure of risk; severity (and exploitability/exposure) is.",
            },
            "exam_pattern": "CVSS: 0.1–3.9 Low, 4.0–6.9 Medium, 7.0–8.9 High, 9.0–10.0 Critical — remediate highest risk first.",
        },
    },
    {
        "id": "secplus-ops-109", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 3, "type": "mcq",
        "stem": "A scanner flags a server as vulnerable to a CVE based on its version string, but manual "
                "verification shows the vendor backported the fix and the server is NOT actually "
                "vulnerable. How should this result be classified?",
        "options": [
            {"id": "A", "text": "False positive"},
            {"id": "B", "text": "False negative"},
            {"id": "C", "text": "True positive"},
            {"id": "D", "text": "Zero-day"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The tool reported a vulnerability that does not actually exist — a false positive, a common "
                       "result of version-only checks against backported patches.",
            "distractors": {
                "B": "A false negative is a real vulnerability the scanner MISSED, not a phantom one it reported.",
                "C": "A true positive is a correctly reported, genuinely present vulnerability.",
                "D": "A zero-day is an unknown/unpatched flaw; here the issue is already fixed.",
            },
            "exam_pattern": "Reported-but-not-real = false positive; real-but-missed = false negative. Always validate before remediating.",
        },
    },
    {
        "id": "secplus-ops-110", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 3, "type": "mcq",
        "stem": "A security engineer analyzes an application's SOURCE CODE for flaws BEFORE it is compiled "
                "or executed, without running it. Which technique is this?",
        "options": [
            {"id": "A", "text": "Static application security testing (SAST)"},
            {"id": "B", "text": "Dynamic application security testing (DAST)"},
            {"id": "C", "text": "Fuzzing a running instance"},
            {"id": "D", "text": "A credentialed network vulnerability scan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SAST (static analysis) inspects source/bytecode without executing the program, catching "
                       "issues early in development.",
            "distractors": {
                "B": "DAST tests the running application from the outside, without source code.",
                "C": "Fuzzing feeds malformed input to a RUNNING app — it requires execution.",
                "D": "A network scan probes hosts/services, not application source code.",
            },
            "exam_pattern": "Static = analyze code at rest (SAST); Dynamic = test the app while it runs (DAST/fuzzing).",
        },
    },
    {
        "id": "secplus-ops-111", "exam": "secplus", "domain": "security_operations",
        "subtopic": "vulnerability_management", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "A critical vulnerability has been confirmed and patched on all affected servers. Which "
                "TWO actions CLOSE OUT the finding in a mature vulnerability-management process? "
                "(Select TWO.)",
        "options": [
            {"id": "A", "text": "Rescan/validate the hosts to confirm the vulnerability is remediated"},
            {"id": "B", "text": "Update reporting and metrics to reflect the remediation"},
            {"id": "C", "text": "Permanently disable all future vulnerability scanning"},
            {"id": "D", "text": "Reclassify the finding as a zero-day"},
            {"id": "E", "text": "Delete the affected servers from the asset inventory"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Validation by rescanning confirms the fix actually worked, and updating reporting/metrics "
                       "documents closure for stakeholders and audits.",
            "distractors": {
                "C": "Disabling scanning removes the visibility needed to catch new and recurring issues.",
                "D": "A patched flaw is not a zero-day; reclassifying it is simply incorrect.",
                "E": "Assets stay in inventory after patching; removing them would hide them from future scans.",
            },
            "exam_pattern": "Response lifecycle closeout = validation (rescan) + reporting. Never 'fix and forget.'",
        },
    },

    # ===== 4.4 Security monitoring ==========================================
    {
        "id": "secplus-ops-112", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to automatically detect and BLOCK outbound emails that contain credit-card "
                "or Social Security numbers. Which tool is purpose-built for this?",
        "options": [
            {"id": "A", "text": "Data loss prevention (DLP)"},
            {"id": "B", "text": "SIEM"},
            {"id": "C", "text": "NetFlow collector"},
            {"id": "D", "text": "SNMP trap receiver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DLP inspects content against patterns/classifications and can block or quarantine data "
                       "(like PII/PAN) before it leaves the organization.",
            "distractors": {
                "B": "A SIEM aggregates and correlates logs to alert; it is not an inline content-blocking control.",
                "C": "NetFlow records flow metadata (who/where/how much), not message content.",
                "D": "SNMP traps report device status/events, not sensitive-data egress.",
            },
            "exam_pattern": "Inspect content + stop sensitive data leaving = DLP (endpoint, network, and cloud/email).",
        },
    },
    {
        "id": "secplus-ops-113", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "An analyst needs to see which internal hosts talked to an external IP, over which ports, "
                "and how much data moved — WITHOUT capturing full packet payloads. Which data source "
                "is BEST?",
        "options": [
            {"id": "A", "text": "NetFlow records"},
            {"id": "B", "text": "Full packet capture of every byte"},
            {"id": "C", "text": "Antivirus quarantine logs"},
            {"id": "D", "text": "A password-vault access log"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NetFlow summarizes conversations (source/destination, ports, byte/packet counts) — exactly "
                       "the metadata asked for, without storing payloads.",
            "distractors": {
                "B": "Full packet capture includes payloads — more than requested, with far higher storage cost.",
                "C": "AV quarantine logs only record malware the AV handled, not general traffic flows.",
                "D": "A vault log tracks credential checkouts, not network conversations.",
            },
            "exam_pattern": "Flow metadata (talkers/ports/volume) without payload = NetFlow/IPFIX; full content = packet capture.",
        },
    },
    {
        "id": "secplus-ops-114", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 3, "type": "mcq",
        "stem": "An enterprise wants a standardized, automated way for different security tools to exchange "
                "configuration-compliance and vulnerability data — for example, checking hosts against a "
                "CIS benchmark. Which standard provides this interoperability?",
        "options": [
            {"id": "A", "text": "SCAP (Security Content Automation Protocol)"},
            {"id": "B", "text": "SNMP"},
            {"id": "C", "text": "NetFlow"},
            {"id": "D", "text": "SMTP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SCAP is a suite of specifications (CVE, CVSS, OVAL, XCCDF, CPE) that lets tools share and "
                       "automate compliance and vulnerability content consistently, e.g., evaluating CIS/DISA benchmarks.",
            "distractors": {
                "B": "SNMP monitors and manages device state; it is not a security-content exchange standard.",
                "C": "NetFlow describes traffic flows, not configuration compliance content.",
                "D": "SMTP is the email transport protocol.",
            },
            "exam_pattern": "Automated, tool-agnostic compliance/benchmark checking = SCAP (with its component specs).",
        },
    },
    {
        "id": "secplus-ops-115", "exam": "secplus", "domain": "security_operations",
        "subtopic": "security_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A SOC needs deep, continuous telemetry from laptops that frequently work remotely, off the "
                "corporate VPN. Which monitoring approach is MOST suitable?",
        "options": [
            {"id": "A", "text": "Agent-based monitoring with software installed on each endpoint"},
            {"id": "B", "text": "Agentless monitoring that only polls devices reachable on the LAN"},
            {"id": "C", "text": "Manual log review performed once a quarter"},
            {"id": "D", "text": "Disabling endpoint logging to conserve bandwidth"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An installed agent collects rich data locally and forwards it whenever the host has "
                       "connectivity, so remote/off-LAN laptops are still covered.",
            "distractors": {
                "B": "Agentless polling needs the device to be reachable over the network and gives shallower data — it fails for off-LAN laptops.",
                "C": "Quarterly manual review cannot provide continuous, near-real-time monitoring.",
                "D": "Disabling logging eliminates the visibility the SOC needs.",
            },
            "exam_pattern": "Remote/deep/continuous telemetry → agent-based. Lightweight, no-install, on-net checks → agentless.",
        },
    },

    # ===== 4.6 Identity & access management =================================
    {
        "id": "secplus-ops-116", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 3, "type": "mcq",
        "stem": "A user signs in to a third-party web application with their corporate identity; the identity "
                "provider sends an XML-based assertion to the app to establish the authenticated web-SSO "
                "session. Which protocol is in use?",
        "options": [
            {"id": "A", "text": "SAML"},
            {"id": "B", "text": "OAuth 2.0"},
            {"id": "C", "text": "OpenID Connect (OIDC)"},
            {"id": "D", "text": "LDAP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SAML exchanges XML-based assertions between an IdP and a service provider to federate "
                       "authentication for web SSO — exactly the flow described.",
            "distractors": {
                "B": "OAuth 2.0 is an AUTHORIZATION framework that delegates access via tokens; it is not an XML authentication assertion.",
                "C": "OIDC adds authentication on top of OAuth but uses JSON Web Tokens, not XML/SAML assertions.",
                "D": "LDAP is a directory-access protocol for querying an identity store, not a federation assertion.",
            },
            "exam_pattern": "XML assertion for web SSO = SAML. Token-based delegated authZ = OAuth. Identity layer on OAuth (JWT) = OIDC.",
        },
    },
    {
        "id": "secplus-ops-117", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 3, "type": "mcq",
        "stem": "In a system, access is decided by security LABELS (e.g., Confidential, Secret, Top Secret) "
                "assigned and enforced by the operating system, and users CANNOT change permissions on "
                "objects they own. Which access-control model is this?",
        "options": [
            {"id": "A", "text": "Mandatory access control (MAC)"},
            {"id": "B", "text": "Discretionary access control (DAC)"},
            {"id": "C", "text": "Role-based access control (RBAC)"},
            {"id": "D", "text": "Attribute-based access control (ABAC)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MAC enforces access via system-assigned classification labels and clearances; owners cannot "
                       "override them — common in government/military and SELinux.",
            "distractors": {
                "B": "DAC lets the data OWNER grant/change permissions at their discretion — the opposite of this scenario.",
                "C": "RBAC grants access based on job role, not classification labels.",
                "D": "ABAC makes dynamic decisions from attributes/policies (department, time, location), not fixed labels.",
            },
            "exam_pattern": "System-enforced labels/clearances, owner can't override = MAC. Owner-controlled = DAC.",
        },
    },
    {
        "id": "secplus-ops-118", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants administrators to receive elevated rights ONLY for the short window they "
                "need them, with the credential checked out from a vault and automatically expired "
                "afterward. Which capability provides this?",
        "options": [
            {"id": "A", "text": "Just-in-time (JIT) privileged access through a PAM solution"},
            {"id": "B", "text": "Permanent membership in the Domain Admins group"},
            {"id": "C", "text": "A shared admin password stored in a team wiki"},
            {"id": "D", "text": "Self-service password reset for standard users"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A PAM platform grants just-in-time, time-boxed elevation with password vaulting and "
                       "ephemeral credentials, minimizing standing privilege.",
            "distractors": {
                "B": "Permanent admin membership is standing privilege — the very thing JIT avoids.",
                "C": "A shared static password is untracked and insecure, defeating accountability.",
                "D": "Self-service reset helps normal users recover passwords; it is not privilege elevation.",
            },
            "exam_pattern": "Temporary, vaulted, auto-expiring elevated access = PAM with JIT and ephemeral credentials.",
        },
    },
    {
        "id": "secplus-ops-119", "exam": "secplus", "domain": "security_operations",
        "subtopic": "identity_access_management", "difficulty": 2, "type": "multi", "select_count": 2,
        "stem": "Which TWO of the following are examples of the 'something you HAVE' authentication factor? "
                "(Select TWO.)",
        "options": [
            {"id": "A", "text": "A hardware security key (FIDO2 token)"},
            {"id": "B", "text": "A one-time code generated by a TOTP authenticator app on a phone"},
            {"id": "C", "text": "A fingerprint scan"},
            {"id": "D", "text": "A memorized PIN"},
            {"id": "E", "text": "The user's typing rhythm (keystroke dynamics)"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "A physical security key and a phone generating a TOTP code are both possession factors — "
                       "'something you have.'",
            "distractors": {
                "C": "A fingerprint is a biometric — 'something you ARE.'",
                "D": "A memorized PIN is a knowledge factor — 'something you KNOW.'",
                "E": "Keystroke/typing rhythm is a behavioral factor — 'something you DO.'",
            },
            "exam_pattern": "Factors: know (password/PIN), have (token/phone/key), are (biometric), do (behavior), where (location).",
        },
    },

    # ===== 4.7 Automation & orchestration ===================================
    {
        "id": "secplus-ops-120", "exam": "secplus", "domain": "security_operations",
        "subtopic": "automation_orchestration", "difficulty": 2, "type": "mcq",
        "stem": "When a specific IOC is detected, a SOC wants to automatically enrich the alert, open a "
                "ticket, and isolate the host by following a predefined, repeatable workflow. Which "
                "technology and artifact enable this?",
        "options": [
            {"id": "A", "text": "SOAR executing a playbook"},
            {"id": "B", "text": "A SIEM dashboard with no automated actions"},
            {"id": "C", "text": "A shared spreadsheet of manual steps"},
            {"id": "D", "text": "A vulnerability scanner"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SOAR orchestrates tools and runs playbooks to execute a defined response sequence "
                       "automatically and consistently.",
            "distractors": {
                "B": "A SIEM alone correlates and alerts, but it does not orchestrate multi-tool response actions.",
                "C": "A manual spreadsheet is neither automated nor consistently repeatable at machine speed.",
                "D": "A scanner finds vulnerabilities; it does not orchestrate incident response.",
            },
            "exam_pattern": "Automated, repeatable, multi-step response = SOAR + playbooks/runbooks (often API integrations).",
        },
    },
    {
        "id": "secplus-ops-121", "exam": "secplus", "domain": "security_operations",
        "subtopic": "automation_orchestration", "difficulty": 3, "type": "mcq",
        "stem": "Before automating its entire provisioning pipeline, a team realizes that one flaw in the "
                "central automation script could simultaneously misconfigure EVERY new system it builds. "
                "Which consideration of automation does this illustrate?",
        "options": [
            {"id": "A", "text": "A single point of failure"},
            {"id": "B", "text": "Reduced reaction time"},
            {"id": "C", "text": "Consistent enforcement of baselines"},
            {"id": "D", "text": "Improved scalability"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Centralizing logic means a single defect can propagate everywhere at once — the automation "
                       "becomes a single point of failure, a key risk/consideration.",
            "distractors": {
                "B": "Faster reaction time is a BENEFIT of automation, not the risk described.",
                "C": "Consistent baseline enforcement is a benefit, not the concentrated-risk problem here.",
                "D": "Scalability is a benefit of automation, not the downside illustrated.",
            },
            "exam_pattern": "Automation considerations/risks: complexity, cost, technical debt, and single point of failure.",
        },
    },
    {
        "id": "secplus-ops-122", "exam": "secplus", "domain": "security_operations",
        "subtopic": "automation_orchestration", "difficulty": 1, "type": "mcq",
        "stem": "A team uses automation to apply the exact same hardened configuration to every server it "
                "provisions, eliminating manual configuration drift. Which BENEFIT of automation does this "
                "BEST demonstrate?",
        "options": [
            {"id": "A", "text": "Enforcing secure baselines consistently and at scale"},
            {"id": "B", "text": "Introducing technical debt"},
            {"id": "C", "text": "Creating a single point of failure"},
            {"id": "D", "text": "Slowing down the team's reaction time"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation applies the same baseline identically to every host, enforcing consistency and "
                       "removing human error/drift — a core benefit.",
            "distractors": {
                "B": "Technical debt is a drawback/consideration, not the benefit shown.",
                "C": "A single point of failure is a risk of automation, not this benefit.",
                "D": "Automation speeds reaction time; it does not slow it.",
            },
            "exam_pattern": "Benefits: efficiency, scale, consistent baseline enforcement, and faster reaction time.",
        },
    },

    # ===== 4.8 Incident response ============================================
    {
        "id": "secplus-ops-123", "exam": "secplus", "domain": "security_operations",
        "subtopic": "incident_response", "difficulty": 2, "type": "mcq",
        "stem": "After an incident is fully resolved, the team meets to document what happened, what worked, "
                "and what to improve, feeding the findings back into their plans. Which incident-response "
                "phase is this?",
        "options": [
            {"id": "A", "text": "Lessons learned"},
            {"id": "B", "text": "Containment"},
            {"id": "C", "text": "Detection"},
            {"id": "D", "text": "Eradication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The post-incident lessons-learned review captures improvements and feeds them back into "
                       "preparation — the final phase of the IR lifecycle.",
            "distractors": {
                "B": "Containment limits the spread/damage of an active incident.",
                "C": "Detection identifies that an incident is occurring.",
                "D": "Eradication removes the threat from affected systems.",
            },
            "exam_pattern": "IR order: Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned.",
        },
    },
    {
        "id": "secplus-ops-124", "exam": "secplus", "domain": "security_operations",
        "subtopic": "incident_response", "difficulty": 2, "type": "mcq",
        "stem": "An organization gathers stakeholders in a conference room to TALK THROUGH their response to "
                "a hypothetical ransomware scenario — no production systems are touched. Which type of "
                "exercise is this?",
        "options": [
            {"id": "A", "text": "Tabletop exercise"},
            {"id": "B", "text": "Full-scale simulation"},
            {"id": "C", "text": "Penetration test"},
            {"id": "D", "text": "Live failover test"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A tabletop is a discussion-based walkthrough of the plan against a scenario, with no systems "
                       "actually affected — ideal for validating roles and decisions cheaply.",
            "distractors": {
                "B": "A simulation actually executes/mimics the attack and response on systems, not just discussion.",
                "C": "A penetration test actively attacks systems to find exploitable weaknesses.",
                "D": "A failover test actually switches operations to backup systems.",
            },
            "exam_pattern": "Discussion-based = tabletop; hands-on execution against systems = simulation.",
        },
    },
    {
        "id": "secplus-ops-125", "exam": "secplus", "domain": "security_operations",
        "subtopic": "incident_response", "difficulty": 3, "type": "mcq",
        "stem": "Instead of waiting for alerts, analysts form a hypothesis (e.g., 'an attacker may be abusing "
                "living-off-the-land binaries') and proactively search historical data for signs of a "
                "compromise that evaded existing detections. What is this activity called?",
        "options": [
            {"id": "A", "text": "Threat hunting"},
            {"id": "B", "text": "Root cause analysis"},
            {"id": "C", "text": "Containment"},
            {"id": "D", "text": "Legal hold"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Threat hunting is proactive, hypothesis-driven searching for adversary activity that "
                       "automated alerting missed.",
            "distractors": {
                "B": "Root cause analysis determines WHY a known incident happened, after it is identified.",
                "C": "Containment limits damage from an already-detected incident.",
                "D": "A legal hold preserves data for litigation — unrelated to proactive searching.",
            },
            "exam_pattern": "Proactive, hypothesis-based search for undetected threats = threat hunting (not alert-driven).",
        },
    },

    # ===== 4.8 Digital forensics ============================================
    {
        "id": "secplus-ops-126", "exam": "secplus", "domain": "security_operations",
        "subtopic": "digital_forensics", "difficulty": 2, "type": "mcq",
        "stem": "To keep digital evidence admissible, investigators document every person who handled it, when, "
                "and why, from collection through presentation in court. Which concept does this "
                "documentation establish?",
        "options": [
            {"id": "A", "text": "Chain of custody"},
            {"id": "B", "text": "Order of volatility"},
            {"id": "C", "text": "Legal hold"},
            {"id": "D", "text": "E-discovery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Chain of custody is the unbroken, documented record of who controlled the evidence at every "
                       "step, proving it was not altered.",
            "distractors": {
                "B": "Order of volatility governs the SEQUENCE of collection (RAM before disk), not handling records.",
                "C": "A legal hold preserves data from deletion; it does not track handling.",
                "D": "E-discovery is identifying and producing electronically stored information for litigation.",
            },
            "exam_pattern": "Documented who/when/why handling of evidence for admissibility = chain of custody.",
        },
    },
    {
        "id": "secplus-ops-127", "exam": "secplus", "domain": "security_operations",
        "subtopic": "digital_forensics", "difficulty": 3, "type": "mcq",
        "stem": "Before analysis, a forensic examiner connects a suspect drive through a write blocker, creates "
                "a bit-for-bit image, and records a hash of BOTH the original and the copy. Why hash both?",
        "options": [
            {"id": "A", "text": "To prove the image is an exact, unaltered copy and to detect any later tampering"},
            {"id": "B", "text": "To encrypt the evidence so it stays confidential"},
            {"id": "C", "text": "To compress the image and save storage space"},
            {"id": "D", "text": "To speed up the imaging process"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Matching hashes of the source and the image prove the copy is identical (preservation/integrity); "
                       "re-hashing later detects any change. The write blocker ensures the original is never modified.",
            "distractors": {
                "B": "Hashing provides integrity, not confidentiality — it does not encrypt.",
                "C": "A hash is a fixed-length digest; it does not compress the data.",
                "D": "Hashing verifies integrity; it does not speed up acquisition.",
            },
            "exam_pattern": "Forensic acquisition = write blocker + bit-for-bit image + matching hashes (integrity/preservation).",
        },
    },
    {
        "id": "secplus-ops-128", "exam": "secplus", "domain": "security_operations",
        "subtopic": "digital_forensics", "difficulty": 2, "type": "mcq",
        "stem": "Anticipating litigation, a company issues a formal directive requiring staff and IT to preserve "
                "all relevant emails and documents and to suspend routine deletion. What is this directive "
                "called?",
        "options": [
            {"id": "A", "text": "Legal hold (litigation hold)"},
            {"id": "B", "text": "Chain of custody"},
            {"id": "C", "text": "Data minimization"},
            {"id": "D", "text": "Right to be forgotten"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A legal/litigation hold formally requires preservation of potentially relevant data and suspends "
                       "normal retention/deletion while litigation is anticipated or active.",
            "distractors": {
                "B": "Chain of custody documents evidence handling, not the organization-wide preservation order.",
                "C": "Data minimization limits how much data is collected/kept — not a litigation preservation order.",
                "D": "Right to be forgotten is a privacy right to ERASE data — the opposite of preserving it.",
            },
            "exam_pattern": "Preserve data + suspend deletion for anticipated litigation = legal hold; then e-discovery produces it.",
        },
    },
]
