"""Microsoft SC-200 pool - Domain 1: Mitigate threats with Microsoft Defender XDR.

Original, objective-aligned practice items for the five Defender XDR subtopics
tracked for SC-200. Uses current Microsoft product names: Microsoft Defender XDR
(formerly Microsoft 365 Defender), the unified Microsoft Defender portal
(security.microsoft.com), and Microsoft Entra ID (formerly Azure AD).

  * sc200_mde_endpoint   - Defender for Endpoint: onboarding, device groups/RBAC,
                           attack surface reduction (ASR) rules, automated
                           investigation & remediation (AIR), live response.
  * sc200_mdo_office365  - Defender for Office 365: Safe Attachments (incl.
                           Dynamic Delivery), Safe Links, anti-phishing /
                           impersonation, Threat Explorer.
  * sc200_mdi_identity   - Defender for Identity: on-prem AD sensors, attack
                           phases (recon, lateral movement, domain dominance),
                           honeytoken/sensitive tags, lateral movement paths.
  * sc200_mdca_cloudapps - Defender for Cloud Apps (CASB): Cloud Discovery,
                           Conditional Access App Control session policies,
                           app governance, anomaly detection policies.
  * sc200_xdr_incidents  - XDR incident/alert correlation, entity investigation,
                           incident classification, unified Sentinel + XDR queue.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Durable capabilities only
- no preview-only features, prices, or memorized exam items.
"""

QUESTIONS = [
    # ===== sc200_mde_endpoint ==============================================
    {
        "id": "sc200-xdr-001", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 1, "type": "mcq",
        "stem": "A SOC must onboard 500 Windows devices that are already enrolled in Microsoft Intune "
                "to Microsoft Defender for Endpoint with the least manual effort. Which approach fits?",
        "options": [
            {"id": "A", "text": "Run the local onboarding script interactively on each device"},
            {"id": "B", "text": "Deploy the Defender for Endpoint onboarding profile through Microsoft Intune"},
            {"id": "C", "text": "Email users the onboarding package to run themselves"},
            {"id": "D", "text": "Enable the trial and wait for devices to be discovered automatically"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Devices already managed by Intune are onboarded at scale by pushing the Defender "
                       "for Endpoint onboarding profile from Intune - no per-device work.",
            "distractors": {
                "A": "The local script is meant for a small number of devices (pilots) and must run on each machine.",
                "C": "Onboarding is an administrative task; relying on users to run packages is unmanaged and inconsistent.",
                "D": "Devices are never onboarded automatically; a supported onboarding method must be deployed.",
            },
            "exam_pattern": "Already managed by Intune/Configuration Manager/GPO -> onboard through that tool; local script = small pilots only.",
        },
        "references": ["Microsoft Learn (SC-200): Onboard devices to Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-002", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants its EU endpoints visible only to the EU SOC team and set to a "
                "specific automated remediation level. Which Defender for Endpoint construct does this?",
        "options": [
            {"id": "A", "text": "A device group scoped to an Entra ID user group, with the chosen automation level"},
            {"id": "B", "text": "A device tag applied to each EU device"},
            {"id": "C", "text": "An antivirus exclusion list for the EU devices"},
            {"id": "D", "text": "An alert-suppression rule for the EU devices"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Device groups assign members by rule, set the members' automated remediation level, "
                       "and (via role-based access control) restrict visibility to chosen Entra ID user groups.",
            "distractors": {
                "B": "Tags help filter and organize devices but do not scope RBAC access or set an automation level.",
                "C": "Exclusions tell Defender Antivirus what not to scan; they have nothing to do with team visibility.",
                "D": "Suppression rules stop specific alerts from being raised; they do not control visibility or remediation level.",
            },
            "exam_pattern": "Scope device visibility + set the automation level = device groups with RBAC.",
        },
        "references": ["Microsoft Learn (SC-200): Create and manage device groups in Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-003", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "Security wants to stop Office apps from spawning child processes (a macro-malware "
                "technique) but must first measure impact before enforcing. What should they configure?",
        "options": [
            {"id": "A", "text": "A Safe Links policy"},
            {"id": "B", "text": "Controlled folder access in Block mode"},
            {"id": "C", "text": "An attack surface reduction (ASR) rule in Block mode"},
            {"id": "D", "text": "An attack surface reduction (ASR) rule in Audit mode"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "ASR rules control behaviors such as Office apps creating child processes. Audit mode "
                       "records what would have been blocked so you can gauge impact before enforcing with Block.",
            "distractors": {
                "A": "Safe Links is a Defender for Office 365 time-of-click URL feature, not an endpoint behavior control.",
                "B": "Controlled folder access guards folders against unauthorized writes (ransomware), not Office child-process creation.",
                "C": "Block enforces immediately; the team wants to measure impact first, so Audit precedes Block.",
            },
            "exam_pattern": "'Measure before enforcing' a behavior = Audit mode; ASR requires Defender Antivirus as the active AV.",
        },
        "references": ["Microsoft Learn (SC-200): Attack surface reduction (ASR) rules"],
    },
    {
        "id": "sc200-xdr-004", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "The SOC wants Defender for Endpoint to automatically investigate and remediate threats "
                "on application servers, but require analyst approval on domain controllers. What governs this?",
        "options": [
            {"id": "A", "text": "Live response sessions"},
            {"id": "B", "text": "Microsoft Secure Score for Devices"},
            {"id": "C", "text": "The automation level set on each device group (automated investigation and remediation)"},
            {"id": "D", "text": "Web content filtering"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Automated investigation and remediation (AIR) acts according to each device group's "
                       "automation level - e.g., Full (remediate automatically) for servers and a level that requires approval for sensitive devices.",
            "distractors": {
                "A": "Live response is a manual remote shell for investigation, not automatic remediation.",
                "B": "Secure Score for Devices measures configuration posture; it does not run or approve remediation.",
                "D": "Web content filtering blocks categories of websites; it is unrelated to investigation and remediation.",
            },
            "exam_pattern": "AIR behavior (auto vs. requires approval) is controlled per device group's automation level.",
        },
        "references": ["Microsoft Learn (SC-200): Automated investigation and remediation in Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-022", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "multi",
        "stem": "A device shows signs of active compromise. Which TWO immediate response actions can an "
                "analyst take from the device page in Microsoft Defender for Endpoint? (Choose two.)",
        "options": [
            {"id": "A", "text": "Isolate the device from the network"},
            {"id": "B", "text": "Run an antivirus scan"},
            {"id": "C", "text": "Lower the device's Secure Score"},
            {"id": "D", "text": "Permanently delete the device owner's Entra ID account"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Defender for Endpoint device response actions include isolating the device, running "
                       "an antivirus scan, restricting app execution, collecting an investigation package, and starting live response.",
            "distractors": {
                "C": "Secure Score for Devices reflects configuration posture; it is not a response action you trigger on a device.",
                "D": "Deleting a user's identity account is not a device response action and would not contain the compromised host.",
            },
            "exam_pattern": "MDE device response = isolate, AV scan, restrict app execution, collect investigation package, live response.",
        },
        "references": ["Microsoft Learn (SC-200): Take response actions on a device in Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-005", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (two words): To open a remote command-line shell to one onboarded "
                "device - running commands, collecting forensic files, and executing library scripts - "
                "an analyst starts a ______ ______ session from the device page in the Defender portal.",
        "correct": ["live response"],
        "explanation": {
            "correct": "Live response gives a remote shell to a single onboarded device for real-time "
                       "investigation and response (collect files, run library scripts, remediate).",
            "distractors": {},
            "exam_pattern": "Remote investigative shell to one device = live response; fleet-wide behavior control = ASR; auto-remediation = AIR.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate entities on devices using live response"],
    },

    # ===== sc200_mdo_office365 =============================================
    {
        "id": "sc200-xdr-006", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 1, "type": "mcq",
        "stem": "Users receive emails with never-before-seen malicious attachments that signature-based "
                "filtering misses. Which Defender for Office 365 feature detonates attachments in a sandbox?",
        "options": [
            {"id": "A", "text": "Safe Links"},
            {"id": "B", "text": "Safe Attachments"},
            {"id": "C", "text": "The anti-spam policy"},
            {"id": "D", "text": "Zero-hour auto purge (ZAP)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Safe Attachments opens attachments in a virtual sandbox (detonation / dynamic "
                       "analysis) to catch unknown malware before the message reaches the mailbox.",
            "distractors": {
                "A": "Safe Links protects URLs at time of click, not file attachments.",
                "C": "Anti-spam filters bulk or unwanted mail by reputation and content; it does not detonate attachments.",
                "D": "ZAP retroactively removes mail already delivered; it is not the pre-delivery sandbox.",
            },
            "exam_pattern": "Sandbox/detonate unknown attachments = Safe Attachments; time-of-click URL = Safe Links.",
        },
        "references": ["Microsoft Learn (SC-200): Safe Attachments in Microsoft Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-007", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "Security wants Safe Attachments scanning but is concerned about delivery delay while "
                "attachments detonate. Which option delivers the body immediately and attaches the file once cleared?",
        "options": [
            {"id": "A", "text": "Dynamic Delivery"},
            {"id": "B", "text": "Monitor"},
            {"id": "C", "text": "Block"},
            {"id": "D", "text": "Safe Documents"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dynamic Delivery sends the email body right away with a placeholder, then delivers "
                       "the attachment once sandboxing clears it (Exchange Online mailboxes), avoiding delivery delay.",
            "distractors": {
                "B": "Monitor delivers the message and only tracks detections; it does not separate body and attachment to cut latency.",
                "C": "Block holds the whole message until scanning completes (and blocks malicious ones) - the opposite of reducing delay.",
                "D": "Safe Documents verifies documents opened in Office/Protected View; it is not a Safe Attachments delivery option.",
            },
            "exam_pattern": "Avoid delivery delay while still detonating = Dynamic Delivery.",
        },
        "references": ["Microsoft Learn (SC-200): Safe Attachments policies and Dynamic Delivery"],
    },
    {
        "id": "sc200-xdr-008", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "Executives are targeted by emails from look-alike sender names and domains that mimic "
                "them. Which Defender for Office 365 policy setting best addresses this?",
        "options": [
            {"id": "A", "text": "Safe Attachments Dynamic Delivery"},
            {"id": "B", "text": "Outbound spam filtering"},
            {"id": "C", "text": "Anti-phishing impersonation protection (user and domain impersonation)"},
            {"id": "D", "text": "Connection filtering (IP allow/block)"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Defender for Office 365 anti-phishing policies add impersonation protection - protect "
                       "specific users (e.g., executives) and domains, backed by mailbox intelligence - to catch look-alike senders.",
            "distractors": {
                "A": "Dynamic Delivery addresses attachment latency, not sender impersonation.",
                "B": "Outbound spam policies limit what your users send; they do not stop inbound impersonation.",
                "D": "Connection filtering allows/blocks by source IP; look-alike impersonation is not tied to a fixed bad IP.",
            },
            "exam_pattern": "Look-alike / display-name spoofing of VIPs = anti-phishing impersonation protection (plus mailbox intelligence).",
        },
        "references": ["Microsoft Learn (SC-200): Anti-phishing policies in Microsoft Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-009", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "A phishing campaign was delivered minutes ago. An analyst must hunt the affected messages "
                "across the tenant and soft-delete them from mailboxes. Which Defender for Office 365 (Plan 2) tool fits?",
        "options": [
            {"id": "A", "text": "The anti-spam policy page"},
            {"id": "B", "text": "Microsoft Secure Score"},
            {"id": "C", "text": "Attack simulation training"},
            {"id": "D", "text": "Threat Explorer (Explorer)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Threat Explorer (Explorer), a Plan 2 capability, lets analysts search delivered email "
                       "across the tenant, filter by campaign/sender/URL, and take remediation actions such as soft-delete.",
            "distractors": {
                "A": "The anti-spam policy page configures filtering; it is not an investigation/remediation surface.",
                "B": "Secure Score recommends posture improvements; it does not hunt or remove email.",
                "C": "Attack simulation training runs benign phishing drills on your users; it does not remediate real messages.",
            },
            "exam_pattern": "Investigate + remediate real email across the tenant = Threat Explorer (Plan 2); Plan 1 has Real-time detections.",
        },
        "references": ["Microsoft Learn (SC-200): Threat Explorer and real-time detections"],
    },

    # ===== sc200_mdi_identity ==============================================
    {
        "id": "sc200-xdr-010", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 1, "type": "mcq",
        "stem": "An organization wants to detect on-premises Active Directory attacks such as "
                "pass-the-hash and DCSync. Where are Microsoft Defender for Identity sensors installed?",
        "options": [
            {"id": "A", "text": "On domain controllers (and supported AD FS, AD CS, and Entra Connect servers)"},
            {"id": "B", "text": "On every end-user workstation"},
            {"id": "C", "text": "On the Microsoft Entra ID tenant in the cloud"},
            {"id": "D", "text": "On the organization's perimeter firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Identity sensors run on domain controllers (and supported AD FS, AD CS, "
                       "and Entra Connect servers) to monitor authentication traffic and Windows events for AD-based attacks.",
            "distractors": {
                "B": "MDI monitors identity infrastructure, not every workstation; endpoint signals come from Defender for Endpoint.",
                "C": "MDI protects on-premises AD; it is not installed on the cloud tenant (Entra ID Protection covers cloud identity risk).",
                "D": "Sensors analyze domain-controller traffic and events, not perimeter firewall traffic.",
            },
            "exam_pattern": "On-prem AD attack detection = MDI sensors on domain controllers; cloud identity risk = Entra ID Protection.",
        },
        "references": ["Microsoft Learn (SC-200): Plan and deploy Microsoft Defender for Identity sensors"],
    },
    {
        "id": "sc200-xdr-011", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "mcq",
        "stem": "Defender for Identity alerts are organized around the attack kill chain. An alert for an "
                "attacker performing DCSync or forging a Golden Ticket belongs to which phase?",
        "options": [
            {"id": "A", "text": "Reconnaissance"},
            {"id": "B", "text": "Domain dominance"},
            {"id": "C", "text": "Lateral movement"},
            {"id": "D", "text": "Exfiltration"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "DCSync and Golden Ticket represent attacker control over the whole domain, which MDI "
                       "classifies under the domain dominance phase.",
            "distractors": {
                "A": "Reconnaissance alerts cover enumeration (account, SMB, or LDAP recon), not domain-wide control.",
                "C": "Lateral movement covers techniques such as pass-the-hash / overpass-the-hash to move between hosts.",
                "D": "MDI's phases are reconnaissance, compromised credentials, lateral movement, and domain dominance; exfiltration is not one of its named phases.",
            },
            "exam_pattern": "MDI phases: reconnaissance -> compromised credentials -> lateral movement -> domain dominance (DCSync, Golden Ticket).",
        },
        "references": ["Microsoft Learn (SC-200): Investigate Microsoft Defender for Identity security alerts"],
    },
    {
        "id": "sc200-xdr-012", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants Defender for Identity to alert whenever a normally dormant decoy account is "
                "used, because any activity on it is suspicious. Which configuration supports this?",
        "options": [
            {"id": "A", "text": "Add the account to a device group"},
            {"id": "B", "text": "Exclude the account from monitoring"},
            {"id": "C", "text": "Tag the account as a honeytoken account"},
            {"id": "D", "text": "Tag the account as a sensitive account"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Honeytoken entity tags mark decoy accounts that should never be used; MDI treats any "
                       "authentication or activity involving them as suspicious and alerts on it.",
            "distractors": {
                "A": "Device groups organize endpoints in Defender for Endpoint, not AD decoy accounts in MDI.",
                "B": "Excluding the account would suppress alerts - the opposite of the goal.",
                "D": "The sensitive tag flags high-value accounts to prioritize them, but does not make any use of the account inherently suspicious like a decoy.",
            },
            "exam_pattern": "Decoy/trap account = honeytoken tag; high-value account prioritization = sensitive tag.",
        },
        "references": ["Microsoft Learn (SC-200): Configure entity tags (sensitive and honeytoken) in Defender for Identity"],
    },
    {
        "id": "sc200-xdr-013", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank (three words): Defender for Identity can visualize a ______ ______ "
                "______ (abbreviated LMP) - a graph showing how an attacker could pivot from an exposed, "
                "non-sensitive account to a sensitive account using shared local-admin credentials.",
        "correct": ["lateral movement path", "lateral movement paths"],
        "explanation": {
            "correct": "Lateral movement paths (LMPs) graphically show how an attacker could move from an "
                       "exposed, non-sensitive account to a sensitive account via shared credentials.",
            "distractors": {},
            "exam_pattern": "MDI's graph of pivot routes to sensitive accounts = lateral movement paths (LMPs).",
        },
        "references": ["Microsoft Learn (SC-200): Understand lateral movement paths in Defender for Identity"],
    },

    # ===== sc200_mdca_cloudapps ============================================
    {
        "id": "sc200-xdr-014", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 1, "type": "mcq",
        "stem": "Leadership asks which unsanctioned cloud apps ('shadow IT') employees use, based on "
                "network traffic. Which Microsoft Defender for Cloud Apps capability provides this?",
        "options": [
            {"id": "A", "text": "Cloud Discovery"},
            {"id": "B", "text": "Conditional Access App Control session policies"},
            {"id": "C", "text": "OAuth app governance"},
            {"id": "D", "text": "File policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cloud Discovery analyzes traffic logs (e.g., from Defender for Endpoint or firewalls) "
                       "to reveal which cloud apps are used and their risk, exposing shadow IT.",
            "distractors": {
                "B": "Session policies control actions within an already-sanctioned app's session; they do not discover unknown apps.",
                "C": "App governance monitors OAuth-connected apps' permissions and behavior, not network-based discovery.",
                "D": "File policies scan content in connected apps; they do not reveal which apps are in use from traffic.",
            },
            "exam_pattern": "Find shadow IT from traffic = Cloud Discovery; control a live session = session policy.",
        },
        "references": ["Microsoft Learn (SC-200): Discover and manage shadow IT with Defender for Cloud Apps"],
    },
    {
        "id": "sc200-xdr-015", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "A company allows SharePoint Online access from unmanaged devices but must block file "
                "downloads during those sessions in real time. Which Defender for Cloud Apps control does this?",
        "options": [
            {"id": "A", "text": "A Cloud Discovery policy"},
            {"id": "B", "text": "An activity policy"},
            {"id": "C", "text": "A session policy (via Conditional Access App Control)"},
            {"id": "D", "text": "An OAuth app policy"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Session policies, delivered through Conditional Access App Control (a reverse proxy "
                       "that Entra Conditional Access routes sessions to), enforce real-time controls such as blocking downloads on unmanaged devices.",
            "distractors": {
                "A": "Cloud Discovery surfaces app usage; it cannot block an action inside a live session.",
                "B": "Activity policies alert or act on logged activities after the fact via API, not inline during the session.",
                "D": "OAuth app policies govern third-party app consent and permissions, not in-session downloads.",
            },
            "exam_pattern": "Real-time in-session control (block download/copy) = session policy + Conditional Access App Control.",
        },
        "references": ["Microsoft Learn (SC-200): Create session policies with Conditional Access App Control"],
    },
    {
        "id": "sc200-xdr-016", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "After discovering a risky app, the SOC tags it 'Unsanctioned' and wants that block "
                "automatically enforced on managed endpoints. Which integration enforces the block on devices?",
        "options": [
            {"id": "A", "text": "Microsoft Purview"},
            {"id": "B", "text": "Defender for Cloud Apps integration with Defender for Endpoint"},
            {"id": "C", "text": "Microsoft Sentinel playbooks"},
            {"id": "D", "text": "Microsoft Entra Conditional Access"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "When Defender for Cloud Apps is integrated with Defender for Endpoint, tagging an app "
                       "Unsanctioned pushes the block to onboarded devices (via network protection), enforcing it even off the corporate network.",
            "distractors": {
                "A": "Purview handles data governance and compliance, not endpoint network blocking of apps.",
                "C": "Sentinel playbooks automate SOAR responses but are not the mechanism that pushes app blocks to endpoints.",
                "D": "Conditional Access governs sign-in to apps, not blocking an unsanctioned domain on the endpoint itself.",
            },
            "exam_pattern": "Unsanctioned-app enforcement on endpoints = Defender for Cloud Apps + Defender for Endpoint integration.",
        },
        "references": ["Microsoft Learn (SC-200): Govern discovered apps using Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-017", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 3, "type": "mcq",
        "stem": "The SOC wants out-of-the-box detection of 'impossible travel' and activity from "
                "infrequent countries for connected cloud apps, with minimal setup. Which policy type provides this?",
        "options": [
            {"id": "A", "text": "A file policy"},
            {"id": "B", "text": "An access policy"},
            {"id": "C", "text": "A Cloud Discovery policy"},
            {"id": "D", "text": "An anomaly detection policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Anomaly detection policies use built-in behavioral/ML baselines to flag behaviors such "
                       "as impossible travel and activity from an infrequent country - enabled by default with little configuration.",
            "distractors": {
                "A": "File policies inspect content (e.g., sensitive data in files), not behavioral anomalies like impossible travel.",
                "B": "Access policies allow or block sign-ins in real time; they do not model behavioral baselines.",
                "C": "Cloud Discovery policies watch for new or risky discovered apps, not user-behavior anomalies in connected apps.",
            },
            "exam_pattern": "Impossible travel / behavioral anomalies out of the box = anomaly detection policies.",
        },
        "references": ["Microsoft Learn (SC-200): Anomaly detection policies in Defender for Cloud Apps"],
    },

    # ===== sc200_xdr_incidents =============================================
    {
        "id": "sc200-xdr-018", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 1, "type": "mcq",
        "stem": "In the Microsoft Defender portal, related alerts from endpoints, email, identities, and "
                "cloud apps that belong to the same attack are automatically grouped into a single what?",
        "options": [
            {"id": "A", "text": "Incident"},
            {"id": "B", "text": "Advanced hunting query"},
            {"id": "C", "text": "Custom detection rule"},
            {"id": "D", "text": "Secure Score recommendation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender XDR correlates related alerts across endpoints, email, identities, and cloud "
                       "apps that share entities into a single incident representing the full attack story.",
            "distractors": {
                "B": "Advanced hunting queries proactively search raw data; they are not the automatic grouping of alerts.",
                "C": "Custom detection rules generate alerts from queries; they do not aggregate alerts across products.",
                "D": "Secure Score recommendations improve posture; they are unrelated to alert correlation.",
            },
            "exam_pattern": "Auto-grouped cross-workload alerts = one XDR incident (the attack story).",
        },
        "references": ["Microsoft Learn (SC-200): Incidents and alerts in the Microsoft Defender portal"],
    },
    {
        "id": "sc200-xdr-019", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "multi",
        "stem": "An analyst triages a multistage incident in the Defender portal. Which TWO are appropriate "
                "FIRST steps to understand its full scope? (Choose two.)",
        "options": [
            {"id": "A", "text": "Review the incident's attack story / alert timeline across all assets"},
            {"id": "B", "text": "Delete the incident to clear the queue"},
            {"id": "C", "text": "Open the impacted user and device entity pages for context"},
            {"id": "D", "text": "Immediately reset the passwords of every user in the tenant"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Start by reading the incident's correlated attack story / timeline and pivoting into "
                       "the affected user and device entity pages to understand scope before taking action.",
            "distractors": {
                "B": "Deleting or clearing an active incident destroys context and does not investigate scope.",
                "D": "Resetting every user is disproportionate and is not a triage step; scope the affected entities first.",
            },
            "exam_pattern": "Triage first = understand scope via the attack story + entity pages, then targeted response.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate incidents in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-020", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "mcq",
        "stem": "After confirming an incident is a real breach and remediating it, how should the analyst "
                "close it in the Defender portal so detection quality is tracked correctly?",
        "options": [
            {"id": "A", "text": "Leave it open indefinitely"},
            {"id": "B", "text": "Resolve it and set the classification to True positive with the appropriate determination"},
            {"id": "C", "text": "Create a Secure Score exception for it"},
            {"id": "D", "text": "Delete the underlying alerts"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Resolving the incident and classifying it (True positive, with a determination) feeds "
                       "back into tuning and reporting on detection accuracy.",
            "distractors": {
                "A": "Leaving it open skews the queue and loses the outcome signal.",
                "C": "Secure Score exceptions relate to posture recommendations, not incident closure.",
                "D": "Deleting alerts removes evidence and still does not record a classification.",
            },
            "exam_pattern": "Close incidents with a classification (true/false/benign positive) to improve tuning and metrics.",
        },
        "references": ["Microsoft Learn (SC-200): Manage and classify incidents in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-021", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 3, "type": "mcq",
        "stem": "An organization has onboarded Microsoft Sentinel to Microsoft Defender XDR in the unified "
                "portal. Where do analysts now manage a single, correlated incident queue spanning both?",
        "options": [
            {"id": "A", "text": "Only in the Azure portal's Microsoft Sentinel blade"},
            {"id": "B", "text": "Only in the Microsoft Purview portal"},
            {"id": "C", "text": "In the Microsoft Defender portal (security.microsoft.com), which now hosts Sentinel"},
            {"id": "D", "text": "In the Microsoft Entra admin center"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The Microsoft Defender portal now hosts Microsoft Sentinel, giving a single unified "
                       "incident queue that correlates Defender XDR and Sentinel data.",
            "distractors": {
                "A": "With the unified experience, incidents are managed in the Defender portal, not restricted to the Azure Sentinel blade.",
                "B": "Purview is for compliance and data governance, not the SOC incident queue.",
                "D": "The Entra admin center manages identities, not the unified incident queue.",
            },
            "exam_pattern": "Unified SOC = Sentinel onboarded into the Defender portal; one incident queue.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Sentinel in the Microsoft Defender portal"],
    },
]
