"""Microsoft SC-200 pool - ROUND 2 expansion (all four domains).

Round-2 deepening of the SC-200 bank. Original, objective-aligned items that do
NOT duplicate round-1 (content_sc200_xdr/cloud/sentinel/hunting.py). Ids use the
round-1 prefixes (xdr/dfc/sent/hunt) with an `-r2-` segment so they stay unique.

Current product names throughout: Microsoft Defender XDR, Microsoft Sentinel,
Microsoft Entra ID, Microsoft Defender for Cloud, and the unified Microsoft
Defender portal (security.microsoft.com). Durable capabilities only - no
preview-only features, prices, or memorized exam items.

Distribution mirrors the blueprint weights: Microsoft Sentinel 38%, Defender XDR
30%, Defender for Cloud 17%, Threat Hunting & Intelligence (KQL) 15%.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on.
"""

QUESTIONS = [
    # =====================================================================
    # DOMAIN 1 - Mitigate threats with Microsoft Defender XDR (30%)
    # =====================================================================

    # ----- sc200_mde_endpoint ---------------------------------------------
    {
        "id": "sc200-xdr-r2-001", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "A SOC must onboard pooled, non-persistent virtual desktop (VDI) instances that are "
                "re-imaged frequently to Microsoft Defender for Endpoint. Which onboarding approach is "
                "designed for this scenario?",
        "options": [
            {"id": "A", "text": "The non-persistent VDI onboarding package (single-entry, per-device-name reuse)"},
            {"id": "B", "text": "The local onboarding script run once on the gold image only"},
            {"id": "C", "text": "Emailing each virtual desktop user the onboarding package"},
            {"id": "D", "text": "Enabling device discovery and waiting for the VMs to be found"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Endpoint provides a dedicated VDI onboarding package for non-persistent "
                       "virtual desktops so repeatedly re-imaged instances register consistently instead of "
                       "creating a new orphaned device object on every reboot.",
            "distractors": {
                "B": "Baking the generic local script into the gold image without the VDI package causes "
                     "duplicate/short-lived device entries as instances are recreated.",
                "C": "Onboarding is an administrative task; it is not performed by end users running packages.",
                "D": "Device discovery finds unmanaged devices on the network; it does not onboard VMs to the service.",
            },
            "exam_pattern": "Non-persistent VDI -> the dedicated VDI onboarding package; local script = small physical pilots.",
        },
        "references": ["Microsoft Learn (SC-200): Onboard non-persistent VDI devices to Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-r2-002", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "Security wants an attack surface reduction (ASR) rule enforced, but during rollout they "
                "want users to be able to bypass a block (and continue) while the team captures the events. "
                "Which ASR rule mode fits?",
        "options": [
            {"id": "A", "text": "Audit mode"},
            {"id": "B", "text": "Warn mode"},
            {"id": "C", "text": "Block mode"},
            {"id": "D", "text": "Disabled (Not configured)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Warn mode behaves like Block but lets the user unblock (bypass) the action, typically "
                       "for 24 hours, so disruption is captured without hard-stopping legitimate work during rollout.",
            "distractors": {
                "A": "Audit only records what would have happened; it never blocks, so users have nothing to bypass.",
                "C": "Block enforces with no user bypass - the opposite of allowing the user to continue.",
                "D": "Disabled/Not configured means the rule does nothing at all.",
            },
            "exam_pattern": "Enforce but allow user bypass = Warn; measure only = Audit; hard enforce = Block.",
        },
        "references": ["Microsoft Learn (SC-200): Attack surface reduction rules modes (Audit, Block, Warn)"],
    },
    {
        "id": "sc200-xdr-r2-003", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (two words): The Microsoft Defender for Endpoint feature that prevents "
                "malware and unauthorized users or apps from turning off antivirus/real-time protection or "
                "changing core security settings is called ______ ______.",
        "correct": ["tamper protection"],
        "explanation": {
            "correct": "Tamper protection locks critical Microsoft Defender Antivirus settings (real-time "
                       "protection, cloud-delivered protection, etc.) so they can't be disabled or altered by "
                       "attackers, malware, or local changes outside approved management.",
            "distractors": {},
            "exam_pattern": "Stop AV/security settings from being disabled or changed = tamper protection.",
        },
        "references": ["Microsoft Learn (SC-200): Protect security settings with tamper protection"],
    },
    {
        "id": "sc200-xdr-r2-004", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants onboarded devices to block outbound connections to known malicious "
                "or low-reputation IP addresses and domains at the network layer, for ALL processes (not just "
                "a browser). Which Defender for Endpoint capability provides this?",
        "options": [
            {"id": "A", "text": "Network protection"},
            {"id": "B", "text": "Controlled folder access"},
            {"id": "C", "text": "Web content filtering"},
            {"id": "D", "text": "Device control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Network protection blocks connections to dangerous/low-reputation domains and IPs "
                       "across the operating system (extending SmartScreen beyond Microsoft Edge to all processes).",
            "distractors": {
                "B": "Controlled folder access guards folders against unauthorized writes (ransomware), not outbound network connections.",
                "C": "Web content filtering blocks whole website categories for governance, not threat-reputation blocking for all processes.",
                "D": "Device control governs peripherals/removable media (e.g., USB), not network destinations.",
            },
            "exam_pattern": "Block malicious IP/domain connections for all processes = network protection (SmartScreen OS-wide).",
        },
        "references": ["Microsoft Learn (SC-200): Protect your network with network protection"],
    },
    {
        "id": "sc200-xdr-r2-005", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 1, "type": "mcq",
        "stem": "Management asks you to prevent employees from browsing to gambling and adult website "
                "categories on managed devices, for acceptable-use reasons. Which Defender for Endpoint feature "
                "is intended for this?",
        "options": [
            {"id": "A", "text": "Web content filtering"},
            {"id": "B", "text": "Attack surface reduction rules"},
            {"id": "C", "text": "Safe Links"},
            {"id": "D", "text": "Tamper protection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Web content filtering blocks access to websites by category (e.g., adult content, "
                       "gambling), reporting and enforcing acceptable-use policy on onboarded devices.",
            "distractors": {
                "B": "ASR rules block exploit/malware behaviors, not website categories.",
                "C": "Safe Links is a Defender for Office 365 time-of-click URL feature, not endpoint category filtering.",
                "D": "Tamper protection locks security settings; it has nothing to do with website categories.",
            },
            "exam_pattern": "Block website CATEGORIES (acceptable use) = web content filtering; malicious destinations = network protection.",
        },
        "references": ["Microsoft Learn (SC-200): Web content filtering in Microsoft Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-r2-006", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "To defend against ransomware, a team wants only trusted applications to be able to modify "
                "files in protected folders such as Documents, blocking untrusted processes from writing to them. "
                "Which Defender for Endpoint capability does this?",
        "options": [
            {"id": "A", "text": "Network protection"},
            {"id": "B", "text": "Controlled folder access"},
            {"id": "C", "text": "Live response"},
            {"id": "D", "text": "Automated investigation and remediation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Controlled folder access protects designated folders by allowing only trusted apps to "
                       "write to them, blocking untrusted/unknown processes - a key anti-ransomware control.",
            "distractors": {
                "A": "Network protection blocks malicious network destinations, not file writes to folders.",
                "C": "Live response is a manual remote shell for investigation, not a preventive folder guard.",
                "D": "AIR investigates and remediates alerts; it is not the folder write-protection control.",
            },
            "exam_pattern": "Allow only trusted apps to write to key folders (anti-ransomware) = controlled folder access.",
        },
        "references": ["Microsoft Learn (SC-200): Protect important folders with controlled folder access"],
    },
    {
        "id": "sc200-xdr-r2-007", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender Vulnerability Management, a security admin selects a recommendation "
                "and chooses 'Request remediation'. What does submitting the request actually do?",
        "options": [
            {"id": "A", "text": "It immediately patches the affected devices"},
            {"id": "B", "text": "It creates a remediation task that flows to IT as a Microsoft Intune ticket for action"},
            {"id": "C", "text": "It isolates all affected devices from the network"},
            {"id": "D", "text": "It permanently removes the vulnerable software"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A remediation request creates a tracked task that hands off to IT (as a Microsoft "
                       "Intune ticket) - bridging security and IT. Submitting it does not itself change devices; "
                       "the IT admin performs the remediation.",
            "distractors": {
                "A": "The request does not apply patches; it assigns work to IT to remediate.",
                "C": "Isolation is a response action on a device, not what a vulnerability remediation request does.",
                "D": "The request tracks remediation; it does not uninstall software on its own.",
            },
            "exam_pattern": "DVM 'Request remediation' = a tracked task to IT (Intune ticket); it doesn't auto-fix devices.",
        },
        "references": ["Microsoft Learn (SC-200): Remediate vulnerabilities with Defender Vulnerability Management"],
    },
    {
        "id": "sc200-xdr-r2-008", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 3, "type": "mcq",
        "stem": "A Defender Vulnerability Management recommendation cannot be acted on yet because a vendor "
                "patch is unavailable and a compensating third-party control is already in place. The team wants "
                "to stop it from skewing their exposure view for now, with a documented justification. What should they create?",
        "options": [
            {"id": "A", "text": "A remediation request"},
            {"id": "B", "text": "An exception on the recommendation (with a justification such as third-party control)"},
            {"id": "C", "text": "An alert suppression rule"},
            {"id": "D", "text": "A custom detection rule"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An exception excludes a specific security recommendation (with a justification like "
                       "third-party control, alternate mitigation, or risk accepted) so it stops affecting the "
                       "exposure view until it's revisited.",
            "distractors": {
                "A": "A remediation request assigns the fix to IT; it is not how you document a justified non-action.",
                "C": "Alert suppression stops alerts from firing; it does not manage vulnerability recommendations.",
                "D": "Custom detection rules generate alerts from queries; they are unrelated to recommendation exceptions.",
            },
            "exam_pattern": "Justified 'we won't act on this recommendation now' = DVM exception (recommendation or CVE level).",
        },
        "references": ["Microsoft Learn (SC-200): Create exceptions in Microsoft Defender Vulnerability Management"],
    },
    {
        "id": "sc200-xdr-r2-009", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 2, "type": "mcq",
        "stem": "A SOC notices unmanaged devices on the corporate network and wants Defender for Endpoint to "
                "actively probe discovered endpoints to enrich details (OS, open ports). Which device discovery "
                "mode should be configured?",
        "options": [
            {"id": "A", "text": "Basic discovery (passive observation only)"},
            {"id": "B", "text": "Standard discovery (active probing of discovered devices)"},
            {"id": "C", "text": "Disable device discovery"},
            {"id": "D", "text": "Cloud Discovery"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Standard discovery (the default) uses onboarded devices to actively probe discovered "
                       "endpoints, enriching inventory with richer details; Basic only passively observes traffic.",
            "distractors": {
                "A": "Basic discovery passively collects what it sees without active probing, so details are sparser.",
                "C": "Disabling discovery stops finding unmanaged devices entirely.",
                "D": "Cloud Discovery is a Defender for Cloud Apps feature that finds shadow-IT cloud apps from traffic logs, not endpoint device discovery.",
            },
            "exam_pattern": "Active probing to enrich unmanaged devices = Standard discovery; passive = Basic.",
        },
        "references": ["Microsoft Learn (SC-200): Device discovery (Standard vs Basic) in Defender for Endpoint"],
    },
    {
        "id": "sc200-xdr-r2-010", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mde_endpoint", "difficulty": 3, "type": "mcq",
        "stem": "A company runs a non-Microsoft antivirus as primary, so Microsoft Defender Antivirus is in "
                "passive mode. They still want Defender for Endpoint to remediate malicious artifacts it detects "
                "behind the scenes. Which capability must be enabled?",
        "options": [
            {"id": "A", "text": "EDR in block mode"},
            {"id": "B", "text": "Tamper protection"},
            {"id": "C", "text": "Controlled folder access"},
            {"id": "D", "text": "Attack surface reduction rules in Audit mode"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EDR in block mode lets Defender for Endpoint block and remediate malicious artifacts "
                       "found by EDR even when Microsoft Defender Antivirus is in passive mode (a third-party AV is primary).",
            "distractors": {
                "B": "Tamper protection locks AV settings; it does not enable post-breach remediation while AV is passive.",
                "C": "Controlled folder access guards folders from ransomware writes; it is not EDR-driven remediation.",
                "D": "ASR Audit only logs; it does not remediate anything.",
            },
            "exam_pattern": "Remediate EDR detections while a third-party AV is primary (Defender AV passive) = EDR in block mode.",
        },
        "references": ["Microsoft Learn (SC-200): Endpoint detection and response (EDR) in block mode"],
    },

    # ----- sc200_mdo_office365 --------------------------------------------
    {
        "id": "sc200-xdr-r2-011", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 1, "type": "mcq",
        "stem": "An organization wants URLs in email (and in Teams and Office apps) checked for malicious "
                "content at the moment a user clicks them, not just at delivery. Which Defender for Office 365 "
                "feature provides this time-of-click protection?",
        "options": [
            {"id": "A", "text": "Safe Attachments"},
            {"id": "B", "text": "Safe Links"},
            {"id": "C", "text": "Zero-hour auto purge (ZAP)"},
            {"id": "D", "text": "Anti-spam policy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Safe Links rewrites and checks URLs at time of click (and supports Teams and Office "
                       "apps), so a link that turns malicious after delivery is still caught when clicked.",
            "distractors": {
                "A": "Safe Attachments detonates file attachments in a sandbox; it does not do time-of-click URL checks.",
                "C": "ZAP retroactively removes already-delivered bad mail; it is not time-of-click URL protection.",
                "D": "Anti-spam filters unwanted bulk mail by reputation/content, not click-time URL verdicts.",
            },
            "exam_pattern": "Time-of-click URL protection (email/Teams/Office) = Safe Links; attachment detonation = Safe Attachments.",
        },
        "references": ["Microsoft Learn (SC-200): Safe Links in Microsoft Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-r2-012", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "A message that passed filtering at delivery is later determined to be malware or phishing. "
                "Which Defender for Office 365 capability automatically acts on the message AFTER delivery by "
                "moving it out of the mailbox to quarantine?",
        "options": [
            {"id": "A", "text": "Dynamic Delivery"},
            {"id": "B", "text": "Zero-hour auto purge (ZAP)"},
            {"id": "C", "text": "Safe Attachments"},
            {"id": "D", "text": "Outbound spam filtering"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Zero-hour auto purge (ZAP) retroactively detects and neutralizes malicious or spam "
                       "messages that were already delivered, moving them to quarantine based on updated verdicts.",
            "distractors": {
                "A": "Dynamic Delivery is a Safe Attachments option that cuts delivery latency; it acts before delivery, not after.",
                "C": "Safe Attachments detonates attachments at delivery time, not retroactively on delivered mail.",
                "D": "Outbound spam filtering limits what your users send; it does not remediate delivered inbound mail.",
            },
            "exam_pattern": "Retroactively remove already-delivered bad mail = ZAP.",
        },
        "references": ["Microsoft Learn (SC-200): Zero-hour auto purge (ZAP) in Microsoft Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-r2-013", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "A new tenant wants Microsoft's recommended baseline for anti-spam, anti-phishing, Safe "
                "Links, and Safe Attachments applied quickly and kept current automatically, without hand-tuning "
                "each policy. What should they enable?",
        "options": [
            {"id": "A", "text": "Preset security policies (Standard or Strict)"},
            {"id": "B", "text": "A single custom anti-spam policy"},
            {"id": "C", "text": "The Tenant Allow/Block List"},
            {"id": "D", "text": "Attack simulation training"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Preset security policies (Standard and Strict) apply Microsoft's recommended, "
                       "automatically maintained protection settings across EOP and Defender for Office 365 - you "
                       "just scope who they apply to.",
            "distractors": {
                "B": "A single custom policy must be hand-tuned and maintained; it is not the Microsoft-managed baseline.",
                "C": "The Tenant Allow/Block List overrides individual verdicts; it is not a full protection baseline.",
                "D": "Attack simulation training runs phishing drills; it does not configure mail protection policies.",
            },
            "exam_pattern": "Microsoft-recommended, auto-maintained baseline = preset security policies (Standard/Strict).",
        },
        "references": ["Microsoft Learn (SC-200): Preset security policies in Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-r2-014", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "A legitimate partner domain keeps getting filtered as spoofing, and separately the team "
                "wants to force-block a specific malicious sender and URL tenant-wide. Which Defender for Office "
                "365 feature lets you override the service's verdicts with explicit allow/block entries?",
        "options": [
            {"id": "A", "text": "Quarantine policies"},
            {"id": "B", "text": "The Tenant Allow/Block List"},
            {"id": "C", "text": "Safe Attachments policy"},
            {"id": "D", "text": "Configuration analyzer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Tenant Allow/Block List lets admins create explicit allow or block entries for "
                       "senders/domains, URLs, files, and spoofed senders, overriding the filtering verdicts.",
            "distractors": {
                "A": "Quarantine policies define what recipients can do with quarantined messages; they do not set allow/block verdicts.",
                "C": "Safe Attachments scans attachments; it is not the allow/block override list.",
                "D": "Configuration analyzer compares your settings to recommended baselines; it does not create allow/block entries.",
            },
            "exam_pattern": "Explicitly allow/block senders, URLs, files, spoof = Tenant Allow/Block List.",
        },
        "references": ["Microsoft Learn (SC-200): Manage allows and blocks in the Tenant Allow/Block List"],
    },
    {
        "id": "sc200-xdr-r2-015", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "Analysts find that a clean newsletter was wrongly quarantined (false positive) and, "
                "separately, a phish that slipped through (false negative). They want Microsoft to re-examine both "
                "and improve filtering. Which Defender for Office 365 tool should they use?",
        "options": [
            {"id": "A", "text": "Submissions (admin submission to Microsoft)"},
            {"id": "B", "text": "Threat Explorer only"},
            {"id": "C", "text": "Secure Score"},
            {"id": "D", "text": "Attack simulation training"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Submissions portal lets admins report false positives and false negatives (emails, "
                       "URLs, attachments) to Microsoft for analysis, which also helps tune filtering.",
            "distractors": {
                "B": "Threat Explorer investigates and remediates mail, but reporting items to Microsoft for review is done through Submissions.",
                "C": "Secure Score recommends posture improvements; it does not submit messages for Microsoft analysis.",
                "D": "Attack simulation training runs internal phishing drills; it is not a reporting channel to Microsoft.",
            },
            "exam_pattern": "Report false positive/negative mail to Microsoft = Submissions (admin submission).",
        },
        "references": ["Microsoft Learn (SC-200): Submit messages and files to Microsoft for analysis"],
    },
    {
        "id": "sc200-xdr-r2-016", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants to control what end users can do with their own quarantined messages - "
                "for example, allow them to request release of quarantined phish but never self-release malware. "
                "Which Defender for Office 365 construct governs these recipient capabilities?",
        "options": [
            {"id": "A", "text": "Anti-spam policy"},
            {"id": "B", "text": "Quarantine policies"},
            {"id": "C", "text": "Safe Links policy"},
            {"id": "D", "text": "Preset security policies"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Quarantine policies define what recipients can do with their quarantined messages "
                       "(view, release, request release, block sender). Messages quarantined as malware or "
                       "high-confidence phish can't be self-released by users regardless of the policy.",
            "distractors": {
                "A": "The anti-spam policy sets filtering verdicts/actions; the recipient's quarantine capabilities come from the quarantine policy it references.",
                "C": "Safe Links handles URL time-of-click protection, not quarantine permissions.",
                "D": "Preset security policies apply a baseline; the per-recipient quarantine capabilities are defined by quarantine policies.",
            },
            "exam_pattern": "What users may do with quarantined mail (release/request) = quarantine policies.",
        },
        "references": ["Microsoft Learn (SC-200): Quarantine policies in Microsoft Defender for Office 365"],
    },
    {
        "id": "sc200-xdr-r2-017", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdo_office365", "difficulty": 3, "type": "mcq",
        "stem": "Over time, several custom Defender for Office 365 policies have drifted from Microsoft's "
                "recommendations. Which tool compares your anti-spam, anti-phishing, Safe Links, and Safe "
                "Attachments settings against the Standard and Strict baselines and flags the gaps?",
        "options": [
            {"id": "A", "text": "Threat Explorer"},
            {"id": "B", "text": "Configuration analyzer"},
            {"id": "C", "text": "The Submissions portal"},
            {"id": "D", "text": "Attack simulation training"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Configuration analyzer compares your current policy settings to the Standard and Strict "
                       "recommended baselines and highlights where to adjust, helping keep policies aligned.",
            "distractors": {
                "A": "Threat Explorer hunts and remediates email; it does not audit policy settings against baselines.",
                "C": "Submissions reports messages to Microsoft; it does not compare policy configurations.",
                "D": "Attack simulation training runs phishing drills; it does not analyze policy drift.",
            },
            "exam_pattern": "Compare policies to Standard/Strict and flag drift = configuration analyzer.",
        },
        "references": ["Microsoft Learn (SC-200): Configuration analyzer for security policies"],
    },

    # ----- sc200_mdi_identity ---------------------------------------------
    {
        "id": "sc200-xdr-r2-018", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "mcq",
        "stem": "Early in an intrusion, Microsoft Defender for Identity detects an attacker enumerating "
                "accounts and group memberships in Active Directory (for example via LDAP or SAMR queries). This "
                "maps to which MDI attack phase?",
        "options": [
            {"id": "A", "text": "Reconnaissance"},
            {"id": "B", "text": "Domain dominance"},
            {"id": "C", "text": "Exfiltration"},
            {"id": "D", "text": "Lateral movement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Account, group, and security-principal enumeration (LDAP/SAMR recon) is classified "
                       "under the reconnaissance phase, where attackers map the environment before escalating.",
            "distractors": {
                "B": "Domain dominance covers domain-wide control (DCSync, Golden Ticket), not early enumeration.",
                "C": "Exfiltration is not one of MDI's named phases.",
                "D": "Lateral movement covers moving between hosts with stolen credentials (e.g., pass-the-hash), not initial enumeration.",
            },
            "exam_pattern": "Account/group enumeration (LDAP/SAMR) = reconnaissance phase.",
        },
        "references": ["Microsoft Learn (SC-200): Reconnaissance alerts in Microsoft Defender for Identity"],
    },
    {
        "id": "sc200-xdr-r2-019", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (two words): Microsoft Defender for Identity alerts on pass-the-hash and "
                "pass-the-ticket activity during the ______ ______ phase, where an attacker reuses stolen "
                "credentials to move between hosts toward higher-value targets.",
        "correct": ["lateral movement"],
        "explanation": {
            "correct": "Pass-the-hash and pass-the-ticket are lateral movement techniques - reusing stolen "
                       "credential material to pivot across machines within the environment.",
            "distractors": {},
            "exam_pattern": "Pass-the-hash / pass-the-ticket pivoting between hosts = lateral movement phase.",
        },
        "references": ["Microsoft Learn (SC-200): Lateral movement alerts in Microsoft Defender for Identity"],
    },
    {
        "id": "sc200-xdr-r2-020", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "mcq",
        "stem": "From the Microsoft Defender portal, an analyst investigating an MDI alert wants to contain a "
                "compromised on-premises Active Directory account by preventing it from signing in until "
                "re-enabled. Which Defender for Identity remediation action does this?",
        "options": [
            {"id": "A", "text": "Disable user (in Active Directory)"},
            {"id": "B", "text": "Add the user to a honeytoken tag"},
            {"id": "C", "text": "Lower the user's investigation priority"},
            {"id": "D", "text": "Create a lateral movement path"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Disable user action disables the account at the Active Directory level, blocking "
                       "sign-in and access to network resources until it is re-enabled (Suspend user disables the "
                       "corresponding account at the Microsoft Entra ID level).",
            "distractors": {
                "B": "Honeytoken tags mark decoy accounts; they do not contain a real compromised account.",
                "C": "Investigation priority is a UEBA scoring concept, not a containment action.",
                "D": "Lateral movement paths are a visualization of pivot routes, not a remediation action.",
            },
            "exam_pattern": "Contain on-prem AD account = Disable user (AD); cloud account = Suspend user (Entra ID).",
        },
        "references": ["Microsoft Learn (SC-200): Remediation actions in Microsoft Defender for Identity"],
    },
    {
        "id": "sc200-xdr-r2-021", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 3, "type": "mcq",
        "stem": "To let Microsoft Defender for Identity perform account remediation actions (such as forcing "
                "a password reset or disabling an account) in on-premises Active Directory with scoped, "
                "least-privilege rights, what should an administrator configure?",
        "options": [
            {"id": "A", "text": "A honeytoken account"},
            {"id": "B", "text": "An action account (for example, a group managed service account) with the needed AD permissions"},
            {"id": "C", "text": "A Microsoft Sentinel watchlist"},
            {"id": "D", "text": "A Conditional Access policy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An action account - commonly a group managed service account (gMSA) granted only the "
                       "specific AD permissions (e.g., reset password, modify userAccountControl) - lets MDI "
                       "execute remediation with least privilege instead of broad rights.",
            "distractors": {
                "A": "A honeytoken is a decoy account for detection, not a service identity that performs remediation.",
                "C": "Watchlists are Sentinel reference data; they do not grant MDI the rights to act in AD.",
                "D": "Conditional Access governs cloud sign-in; it does not give MDI permission to remediate on-prem AD accounts.",
            },
            "exam_pattern": "Let MDI remediate AD accounts with least privilege = an action account (gMSA) with scoped permissions.",
        },
        "references": ["Microsoft Learn (SC-200): Manage action accounts in Microsoft Defender for Identity"],
    },
    {
        "id": "sc200-xdr-r2-022", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "mcq",
        "stem": "Beyond detecting attacks, Microsoft Defender for Identity surfaces proactive "
                "recommendations to fix risky identity configurations (such as legacy protocols or unsecure "
                "account settings) to shrink the attack surface. What are these called?",
        "options": [
            {"id": "A", "text": "Lateral movement paths"},
            {"id": "B", "text": "Identity security posture assessments (recommendations)"},
            {"id": "C", "text": "Honeytoken tags"},
            {"id": "D", "text": "Custom detection rules"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Identity security posture assessments provide proactive recommendations (surfaced via "
                       "Microsoft Secure Score) to remediate risky AD configurations and reduce the identity attack surface.",
            "distractors": {
                "A": "Lateral movement paths show how attackers could pivot; they are not posture recommendations.",
                "C": "Honeytoken tags mark decoy accounts for detection, not configuration hardening guidance.",
                "D": "Custom detection rules generate alerts from queries; they are not MDI posture assessments.",
            },
            "exam_pattern": "Proactive 'fix risky identity configs' guidance = identity security posture assessments.",
        },
        "references": ["Microsoft Learn (SC-200): Identity security posture assessments in Defender for Identity"],
    },
    {
        "id": "sc200-xdr-r2-023", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdi_identity", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Defender for Identity organizes detections around an attack kill chain. Which TWO "
                "of the following are named MDI attack phases? (Choose two.)",
        "options": [
            {"id": "A", "text": "Reconnaissance"},
            {"id": "B", "text": "Domain dominance"},
            {"id": "C", "text": "Detonation"},
            {"id": "D", "text": "Data loss prevention"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "MDI phases are reconnaissance, compromised credentials, lateral movement, and domain "
                       "dominance; reconnaissance and domain dominance are two of them.",
            "distractors": {
                "C": "Detonation refers to Safe Attachments sandboxing in Defender for Office 365, not an MDI phase.",
                "D": "Data loss prevention is a Microsoft Purview capability, not an MDI attack phase.",
            },
            "exam_pattern": "MDI phases: reconnaissance -> compromised credentials -> lateral movement -> domain dominance.",
        },
        "references": ["Microsoft Learn (SC-200): Understand security alerts by attack phase in Defender for Identity"],
    },

    # ----- sc200_mdca_cloudapps -------------------------------------------
    {
        "id": "sc200-xdr-r2-024", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to outright block sign-in to a sanctioned cloud app from unmanaged devices "
                "in real time (not just limit actions during the session). Which Defender for Cloud Apps policy "
                "type, delivered through Conditional Access App Control, does this?",
        "options": [
            {"id": "A", "text": "An access policy"},
            {"id": "B", "text": "A session policy"},
            {"id": "C", "text": "A file policy"},
            {"id": "D", "text": "An anomaly detection policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Access policies use Conditional Access App Control to allow or block the sign-in/access "
                       "to an app in real time (e.g., block from unmanaged devices). Session policies instead "
                       "control actions WITHIN an allowed session (like blocking downloads).",
            "distractors": {
                "B": "Session policies monitor/limit activity inside an active session; they don't block the sign-in outright.",
                "C": "File policies inspect content in connected apps via API; they are not real-time access control.",
                "D": "Anomaly detection policies flag behavioral outliers after the fact; they don't block access inline.",
            },
            "exam_pattern": "Block/allow the access itself in real time = access policy; control the live session = session policy.",
        },
        "references": ["Microsoft Learn (SC-200): Access policies in Microsoft Defender for Cloud Apps"],
    },
    {
        "id": "sc200-xdr-r2-025", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "To gain deep visibility and governance over data and activities already stored in a "
                "sanctioned SaaS app (e.g., scan files for sensitive content, audit user activity), how should "
                "Defender for Cloud Apps be connected to that app?",
        "options": [
            {"id": "A", "text": "Using an app connector (API connection) for that app"},
            {"id": "B", "text": "Using Cloud Discovery traffic logs"},
            {"id": "C", "text": "Using a Conditional Access App Control session policy"},
            {"id": "D", "text": "Using a Microsoft Sentinel watchlist"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "App connectors use the app's APIs to give deep visibility and governance over "
                       "content and activities already in the sanctioned app (scan files, inspect activity logs, apply actions).",
            "distractors": {
                "B": "Cloud Discovery reveals which apps are used from traffic logs; it does not govern data inside an app.",
                "C": "Session policies control live sessions in real time; they do not scan data at rest via API.",
                "D": "Watchlists are Sentinel reference data; they are unrelated to connecting a SaaS app.",
            },
            "exam_pattern": "Deep API governance over data already in a sanctioned app = app connector (API connection).",
        },
        "references": ["Microsoft Learn (SC-200): Connect apps to get visibility with app connectors"],
    },
    {
        "id": "sc200-xdr-r2-026", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "Using an API-connected app, a SOC wants to continuously find files that contain credit-card "
                "numbers and are shared externally, then automatically remove external sharing. Which Defender "
                "for Cloud Apps policy type fits?",
        "options": [
            {"id": "A", "text": "A file policy"},
            {"id": "B", "text": "An access policy"},
            {"id": "C", "text": "A Cloud Discovery policy"},
            {"id": "D", "text": "An app governance policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File policies scan content in connected apps (e.g., for sensitive data and sharing "
                       "state) and can apply governance actions such as removing external sharing or quarantining the file.",
            "distractors": {
                "B": "Access policies allow/block sign-in in real time; they do not inspect file content or sharing.",
                "C": "Cloud Discovery policies watch for new/risky discovered apps, not file content.",
                "D": "App governance targets OAuth app permissions/behavior, not file content and sharing.",
            },
            "exam_pattern": "Find/act on sensitive or over-shared files in connected apps = file policy.",
        },
        "references": ["Microsoft Learn (SC-200): Create file policies in Microsoft Defender for Cloud Apps"],
    },
    {
        "id": "sc200-xdr-r2-027", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 3, "type": "mcq",
        "stem": "The SOC is worried about risky third-party OAuth apps that users have consented to, which "
                "hold broad Microsoft Graph permissions to mailboxes and files. Which Defender for Cloud Apps "
                "capability is designed to monitor and govern these OAuth-connected apps?",
        "options": [
            {"id": "A", "text": "Cloud Discovery"},
            {"id": "B", "text": "App governance (OAuth app monitoring)"},
            {"id": "C", "text": "Session policies"},
            {"id": "D", "text": "Web content filtering"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "App governance monitors OAuth-connected apps' permissions and behavior (e.g., unusual "
                       "data access, overprivileged consent) and can alert or remediate risky apps.",
            "distractors": {
                "A": "Cloud Discovery finds shadow-IT apps from traffic; it does not analyze OAuth app permissions/behavior.",
                "C": "Session policies control live user sessions, not consented OAuth app risk.",
                "D": "Web content filtering is a Defender for Endpoint category-blocking feature, unrelated to OAuth apps.",
            },
            "exam_pattern": "Risky consented OAuth apps / Graph permissions = app governance.",
        },
        "references": ["Microsoft Learn (SC-200): App governance in Microsoft Defender for Cloud Apps"],
    },
    {
        "id": "sc200-xdr-r2-028", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 2, "type": "mcq",
        "stem": "In the Defender for Cloud Apps cloud app catalog, each discovered app is assigned a risk "
                "score. What is the primary purpose of that score?",
        "options": [
            {"id": "A", "text": "To measure how much bandwidth the app consumes"},
            {"id": "B", "text": "To help decide whether to sanction or unsanction the app, based on security/compliance/legal factors"},
            {"id": "C", "text": "To set the app's Microsoft 365 license cost"},
            {"id": "D", "text": "To calculate the tenant's Secure Score"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The catalog scores each app (on a numeric scale) using dozens of security, "
                       "compliance, and legal risk factors, helping the SOC decide whether to sanction or unsanction it.",
            "distractors": {
                "A": "Bandwidth usage is shown elsewhere; the risk score reflects risk factors, not consumption.",
                "C": "The score is about risk, not licensing cost.",
                "D": "Secure Score is a separate Microsoft posture metric; the app risk score is specific to Cloud Discovery governance.",
            },
            "exam_pattern": "Discovered-app risk score (many factors) = decide sanction vs unsanction.",
        },
        "references": ["Microsoft Learn (SC-200): The cloud app catalog and risk scores in Defender for Cloud Apps"],
    },
    {
        "id": "sc200-xdr-r2-029", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_mdca_cloudapps", "difficulty": 3, "type": "fill",
        "stem": "Fill in the blank (two words): Conditional Access App Control enforces real-time session "
                "controls (such as blocking downloads) by routing a user's app traffic through a ______ ______ "
                "operated by Microsoft Defender for Cloud Apps, after Microsoft Entra Conditional Access directs the session to it.",
        "correct": ["reverse proxy"],
        "explanation": {
            "correct": "Conditional Access App Control works as a reverse proxy: Entra Conditional Access "
                       "routes the session to Defender for Cloud Apps, which then applies real-time monitoring and session controls.",
            "distractors": {},
            "exam_pattern": "Real-time session control mechanism = reverse proxy via Conditional Access App Control.",
        },
        "references": ["Microsoft Learn (SC-200): Protect apps with Conditional Access App Control"],
    },

    # ----- sc200_xdr_incidents --------------------------------------------
    {
        "id": "sc200-xdr-r2-030", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Defender XDR can automatically contain a high-confidence, in-progress attack "
                "(e.g., human-operated ransomware) by actions such as disabling a compromised account or "
                "isolating a device, before an analyst responds. What is this capability called?",
        "options": [
            {"id": "A", "text": "Automatic attack disruption"},
            {"id": "B", "text": "Automated investigation and remediation (AIR)"},
            {"id": "C", "text": "Advanced hunting"},
            {"id": "D", "text": "Secure Score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automatic attack disruption uses high-confidence XDR signals to contain an active "
                       "attack automatically (e.g., contain device, disable/suspend user) to limit spread while analysts investigate.",
            "distractors": {
                "B": "AIR investigates and remediates alerts on a device, but attack disruption is the cross-workload, high-confidence auto-containment capability.",
                "C": "Advanced hunting is proactive querying, not automatic containment.",
                "D": "Secure Score measures posture; it does not contain attacks.",
            },
            "exam_pattern": "Auto-contain an active high-confidence attack across workloads = automatic attack disruption.",
        },
        "references": ["Microsoft Learn (SC-200): Automatic attack disruption in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-r2-031", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "mcq",
        "stem": "A particular analytics detection generates frequent false positives from a known, benign "
                "internal tool, creating noisy alerts. In Microsoft Defender XDR, what is the appropriate way to "
                "reduce this noise without turning off protection broadly?",
        "options": [
            {"id": "A", "text": "Delete the alerts as they arrive"},
            {"id": "B", "text": "Tune the alert / create an alert-tuning (suppression) rule for that benign pattern"},
            {"id": "C", "text": "Offboard the affected devices"},
            {"id": "D", "text": "Lower the tenant's Secure Score target"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Alert tuning (suppression) rules let you automatically handle a specific, known-benign "
                       "alert pattern (suppress/resolve) while keeping the detection active for everything else.",
            "distractors": {
                "A": "Manually deleting alerts is reactive, unscalable, and loses tuning signal.",
                "C": "Offboarding devices removes protection; it does not tune a noisy detection.",
                "D": "Secure Score targets have nothing to do with alert generation.",
            },
            "exam_pattern": "Quiet a specific benign alert pattern = alert tuning / suppression rule, not blanket disablement.",
        },
        "references": ["Microsoft Learn (SC-200): Tune an alert and create alert-tuning rules in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-r2-032", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "mcq",
        "stem": "While reviewing an incident, an analyst wants to pivot a suspicious entity (such as a file "
                "hash or account) directly into advanced hunting to find everywhere it appears across the estate. "
                "Which capability in the Defender portal provides this one-click pivot?",
        "options": [
            {"id": "A", "text": "Go hunt (from the entity)"},
            {"id": "B", "text": "Secure Score recommendation"},
            {"id": "C", "text": "Content hub"},
            {"id": "D", "text": "Workflow automation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 'Go hunt' action takes an entity from an incident/alert and launches a prebuilt "
                       "advanced hunting query to find related activity across the environment.",
            "distractors": {
                "B": "Secure Score recommendations improve posture; they are not an entity-to-hunt pivot.",
                "C": "The Content hub is a Microsoft Sentinel content marketplace, not an entity pivot.",
                "D": "Workflow automation is a Defender for Cloud feature to trigger Logic Apps, not an incident hunting pivot.",
            },
            "exam_pattern": "Pivot an entity into advanced hunting = Go hunt.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate entities with Go hunt in advanced hunting"],
    },
    {
        "id": "sc200-xdr-r2-033", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 1, "type": "mcq",
        "stem": "A SOC lead wants to route an incident to a specific analyst and track who is working it, "
                "while keeping the queue organized by progress. In the Defender portal incident, what should be set?",
        "options": [
            {"id": "A", "text": "The incident assignment (owner) and status (e.g., In progress)"},
            {"id": "B", "text": "The incident's MITRE ATT&CK technique list"},
            {"id": "C", "text": "A Secure Score exception"},
            {"id": "D", "text": "A device group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Assigning an owner and setting the status (New / In progress / Resolved) routes and "
                       "tracks incident work; tags and comments add further organization.",
            "distractors": {
                "B": "The technique list describes the attack; it does not assign or track ownership.",
                "C": "Secure Score exceptions relate to posture recommendations, not incident ownership.",
                "D": "Device groups scope RBAC/automation for endpoints, not incident assignment.",
            },
            "exam_pattern": "Route/track incident work = assign owner + set status (plus tags/comments).",
        },
        "references": ["Microsoft Learn (SC-200): Manage incidents (assign, status, tags) in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-r2-034", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "mcq",
        "stem": "Automated investigation produced several remediation actions that are pending approval, and "
                "the team also wants to review the history of actions already taken across Microsoft Defender XDR. "
                "Which centralized hub shows and lets them approve/undo these actions?",
        "options": [
            {"id": "A", "text": "The Action center"},
            {"id": "B", "text": "The investigation graph"},
            {"id": "C", "text": "Secure Score"},
            {"id": "D", "text": "The Content hub"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Action center centralizes remediation actions - pending actions awaiting approval "
                       "and a history of completed actions - across Defender XDR, where analysts can approve, reject, or undo them.",
            "distractors": {
                "B": "The investigation graph (a Sentinel feature) visualizes entities; it is not the remediation-action hub.",
                "C": "Secure Score measures posture; it does not track remediation actions.",
                "D": "The Content hub installs Sentinel solutions; it is not the remediation action center.",
            },
            "exam_pattern": "Approve/track pending and completed remediation actions = Action center.",
        },
        "references": ["Microsoft Learn (SC-200): The Action center in Microsoft Defender XDR"],
    },
    {
        "id": "sc200-xdr-r2-035", "exam": "sc200", "domain": "sc200_defender_xdr",
        "subtopic": "sc200_xdr_incidents", "difficulty": 2, "type": "multi",
        "stem": "A SOC wants to continuously improve the quality and signal of its incident queue over time. "
                "Which TWO practices support this goal? (Choose two.)",
        "options": [
            {"id": "A", "text": "Resolve incidents with an accurate classification and determination (true/false/benign positive)"},
            {"id": "B", "text": "Tune or suppress alerts that are confirmed benign and noisy"},
            {"id": "C", "text": "Delete incidents to keep the queue short"},
            {"id": "D", "text": "Disable the Microsoft Defender XDR data connectors"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Classifying/closing incidents accurately feeds detection tuning and metrics, and "
                       "tuning/suppressing confirmed-benign noisy alerts raises signal - both improve queue quality over time.",
            "distractors": {
                "C": "Deleting incidents destroys context and the outcome signal; it does not improve detection quality.",
                "D": "Disabling connectors stops data flowing in - the opposite of a healthy queue.",
            },
            "exam_pattern": "Improve the queue = classify on close + tune/suppress confirmed-benign noise.",
        },
        "references": ["Microsoft Learn (SC-200): Classify incidents and tune detections in Microsoft Defender XDR"],
    },

    # =====================================================================
    # DOMAIN 2 - Mitigate threats with Microsoft Defender for Cloud (17%)
    # =====================================================================

    # ----- sc200_dfc_posture ----------------------------------------------
    {
        "id": "sc200-dfc-r2-001", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "A security team wants each open recommendation assigned to an owner with a remediation due "
                "date, and wants overdue items to drive accountability without instantly penalizing Secure Score. "
                "Which Microsoft Defender for Cloud feature provides this?",
        "options": [
            {"id": "A", "text": "Governance rules (assign owner, due date, grace period)"},
            {"id": "B", "text": "Alert suppression rules"},
            {"id": "C", "text": "Workflow automation"},
            {"id": "D", "text": "Just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Governance rules assign an owner and a remediation due date (e.g., 7/14/30/90 days) to "
                       "recommendations and can apply a grace period so a recommendation doesn't affect Secure "
                       "Score until it becomes overdue.",
            "distractors": {
                "B": "Alert suppression dismisses specific security alerts; it does not assign recommendation ownership or due dates.",
                "C": "Workflow automation triggers Logic Apps on alerts/recommendations; it does not set owners, due dates, or grace periods.",
                "D": "JIT VM access reduces port exposure; it is a control, not a remediation governance feature.",
            },
            "exam_pattern": "Owner + due date + grace period on recommendations = governance rules.",
        },
        "references": ["Microsoft Learn (SC-200): Drive remediation with governance rules in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-002", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to assess the operating systems and software on its Azure VMs for "
                "vulnerabilities and exposed secrets WITHOUT installing an agent on each machine. Which Defender "
                "for Cloud capability provides this?",
        "options": [
            {"id": "A", "text": "Agentless machine scanning"},
            {"id": "B", "text": "Just-in-time VM access"},
            {"id": "C", "text": "Adaptive network hardening"},
            {"id": "D", "text": "The Log Analytics agent (MMA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Agentless machine scanning (available with Defender CSPM or Defender for Servers Plan "
                       "2) inspects VM disks on a schedule for vulnerabilities, installed software, and secrets "
                       "without deploying an in-guest agent.",
            "distractors": {
                "B": "JIT VM access controls management-port exposure; it does not scan for vulnerabilities/secrets.",
                "C": "Adaptive network hardening recommends NSG rules; it is not a vulnerability/secrets scanner.",
                "D": "The legacy Log Analytics agent (MMA) is agent-based collection - the opposite of agentless - and is being retired.",
            },
            "exam_pattern": "Scan VM disks for vulns/secrets with no in-guest agent = agentless machine scanning.",
        },
        "references": ["Microsoft Learn (SC-200): Agentless machine scanning in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-003", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 3, "type": "mcq",
        "stem": "A security architect wants an outside-in view of the organization's internet-facing assets "
                "(domains, hosts, exposed services) to find unknown or unmanaged attack surface. Which capability, "
                "included with Defender CSPM, provides this discovery?",
        "options": [
            {"id": "A", "text": "External attack surface management (EASM)"},
            {"id": "B", "text": "Regulatory compliance dashboard"},
            {"id": "C", "text": "Just-in-time VM access"},
            {"id": "D", "text": "Workload protection plans"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "External attack surface management discovers internet-facing assets from an outside-in "
                       "(attacker) perspective, surfacing unknown/unmanaged exposure; it is included with Defender CSPM.",
            "distractors": {
                "B": "The regulatory compliance dashboard maps controls to standards; it does not discover external internet-facing assets.",
                "C": "JIT reduces management-port exposure on known VMs; it does not discover unknown external assets.",
                "D": "Workload protection plans provide threat detection for resource types, not external attack-surface discovery.",
            },
            "exam_pattern": "Outside-in discovery of internet-facing assets = external attack surface management (EASM).",
        },
        "references": ["Microsoft Learn (SC-200): External attack surface management in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-004", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 3, "type": "mcq",
        "stem": "Where do the security recommendations shown in Microsoft Defender for Cloud come from, by default?",
        "options": [
            {"id": "A", "text": "They are authored manually by each subscription owner"},
            {"id": "B", "text": "An Azure Policy initiative (the Microsoft Cloud Security Benchmark) assigned to the scope"},
            {"id": "C", "text": "Microsoft Sentinel analytics rules"},
            {"id": "D", "text": "Conditional Access policies"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Recommendations are generated by evaluating resources against a security policy - an "
                       "Azure Policy initiative, by default the Microsoft Cloud Security Benchmark (MCSB) - "
                       "assigned at the subscription/management-group scope. You can also add custom recommendations.",
            "distractors": {
                "A": "Recommendations are produced by policy evaluation, not hand-authored per subscription.",
                "C": "Sentinel analytics rules detect threats in logs; they do not generate Defender for Cloud posture recommendations.",
                "D": "Conditional Access governs identity sign-in, not cloud-resource posture recommendations.",
            },
            "exam_pattern": "Defender for Cloud recommendations = Azure Policy security initiative (MCSB by default).",
        },
        "references": ["Microsoft Learn (SC-200): Security policies and the Microsoft Cloud Security Benchmark"],
    },
    {
        "id": "sc200-dfc-r2-005", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "mcq",
        "stem": "Auditors require the environment to be measured against PCI DSS and NIST SP 800-53 in "
                "addition to the default benchmark. How does an analyst make Defender for Cloud track these?",
        "options": [
            {"id": "A", "text": "Add the standards to the Regulatory compliance dashboard (assign the compliance standards)"},
            {"id": "B", "text": "Create a Microsoft Sentinel workbook"},
            {"id": "C", "text": "Raise the Secure Score target to 100%"},
            {"id": "D", "text": "Enable just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "You add regulatory standards (PCI DSS, NIST, ISO, etc.) to the Regulatory compliance "
                       "dashboard; Defender for Cloud then continuously assesses resources against those controls alongside the default MCSB.",
            "distractors": {
                "B": "A workbook visualizes data; it does not add a compliance standard assessment.",
                "C": "Secure Score targets don't map resources to PCI/NIST controls.",
                "D": "JIT is a single hardening control, not a compliance-standard assessment.",
            },
            "exam_pattern": "Track PCI/NIST/ISO = add the standard(s) to the Regulatory compliance dashboard.",
        },
        "references": ["Microsoft Learn (SC-200): Add regulatory standards to the compliance dashboard"],
    },
    {
        "id": "sc200-dfc-r2-006", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 3, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, recommendations are grouped into 'security controls' for "
                "Secure Score. How are points earned for a control?",
        "options": [
            {"id": "A", "text": "Points are earned only when ALL recommendations in the control are remediated for a given resource"},
            {"id": "B", "text": "Each individual recommendation adds points independently as it is fixed"},
            {"id": "C", "text": "Points are based on the number of alerts generated"},
            {"id": "D", "text": "Points are fixed and cannot change with remediation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secure Score is calculated from security controls (groups of related recommendations); "
                       "a resource earns the control's points only when all of that control's recommendations are "
                       "remediated for it, encouraging complete hardening.",
            "distractors": {
                "B": "Points accrue at the control level (all recommendations satisfied), not per single recommendation.",
                "C": "Secure Score reflects posture/recommendations, not alert volume.",
                "D": "Points change as you remediate; the score rises with remediation.",
            },
            "exam_pattern": "Secure Score = per-control (all recommendations in a control remediated for a resource).",
        },
        "references": ["Microsoft Learn (SC-200): How Secure Score and security controls are calculated"],
    },
    {
        "id": "sc200-dfc-r2-007", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_posture", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (one word): When a specific recommendation does not apply to a resource "
                "(for example, an accepted risk or a mitigated-by-design case) and you want it excluded so it "
                "stops affecting Secure Score, you create an ______ in Microsoft Defender for Cloud.",
        "correct": ["exemption"],
        "explanation": {
            "correct": "An exemption excludes a recommendation from a resource/scope (with a justification such "
                       "as waiver or risk mitigated), so it no longer impacts Secure Score or the recommendation list.",
            "distractors": {},
            "exam_pattern": "Exclude a recommendation from a resource (accepted risk / mitigated) = exemption.",
        },
        "references": ["Microsoft Learn (SC-200): Exempt resources from recommendations in Defender for Cloud"],
    },

    # ----- sc200_dfc_workloads --------------------------------------------
    {
        "id": "sc200-dfc-r2-008", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "A team needs just-in-time VM access, file integrity monitoring, and integrated vulnerability "
                "assessment on their servers - not only the Defender for Endpoint integration. Which plan/tier is required?",
        "options": [
            {"id": "A", "text": "Defender for Servers Plan 1"},
            {"id": "B", "text": "Defender for Servers Plan 2"},
            {"id": "C", "text": "Foundational CSPM (free)"},
            {"id": "D", "text": "Defender for Resource Manager"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defender for Servers Plan 2 provides the full capability set - JIT VM access, file "
                       "integrity monitoring, integrated vulnerability assessment, agentless scanning, and more. "
                       "Plan 1 delivers only the Defender for Endpoint integration.",
            "distractors": {
                "A": "Plan 1 is limited to the Defender for Endpoint integration; it lacks JIT, FIM, and VA.",
                "C": "Foundational CSPM is free posture management; it is not a workload protection plan.",
                "D": "Defender for Resource Manager monitors ARM control-plane operations, not server guest protection.",
            },
            "exam_pattern": "JIT + FIM + VA on servers = Defender for Servers Plan 2 (Plan 1 = MDE integration only).",
        },
        "references": ["Microsoft Learn (SC-200): Defender for Servers plans (Plan 1 vs Plan 2)"],
    },
    {
        "id": "sc200-dfc-r2-009", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "A company hosts web applications on Azure App Service and wants threat detection for "
                "web-app attacks and suspicious behavior on those apps. Which plan should be enabled?",
        "options": [
            {"id": "A", "text": "Defender for App Service"},
            {"id": "B", "text": "Defender for Storage"},
            {"id": "C", "text": "Defender for Key Vault"},
            {"id": "D", "text": "Defender for DNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for App Service detects threats targeting web apps running on App Service "
                       "(e.g., web-attack patterns, suspicious operations) and surfaces related alerts.",
            "distractors": {
                "B": "Defender for Storage protects storage accounts (blob malware scanning, access anomalies), not App Service web apps.",
                "C": "Defender for Key Vault detects abnormal secret/key access, not web-app attacks.",
                "D": "Defender for DNS monitored DNS-layer threats and has since been consolidated; it is not the App Service plan.",
            },
            "exam_pattern": "Threat detection for Azure App Service web apps = Defender for App Service.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for App Service"],
    },
    {
        "id": "sc200-dfc-r2-010", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants alerts on suspicious control-plane operations - such as anomalous use of Azure "
                "Resource Manager to deploy or modify resources, or toolkit activity (e.g., from compromised "
                "credentials). Which plan detects these ARM-layer threats?",
        "options": [
            {"id": "A", "text": "Defender for Containers"},
            {"id": "B", "text": "Defender for Resource Manager"},
            {"id": "C", "text": "Defender for Servers Plan 1"},
            {"id": "D", "text": "Defender for Databases"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Defender for Resource Manager monitors the Azure Resource Manager control plane and "
                       "alerts on suspicious/malicious management operations (e.g., unusual resource deployment, exploitation toolkits).",
            "distractors": {
                "A": "Defender for Containers protects Kubernetes workloads, not the ARM control plane.",
                "C": "Defender for Servers protects VM guests via Defender for Endpoint, not ARM operations.",
                "D": "Defender for Databases detects database-layer threats (e.g., SQL injection), not control-plane operations.",
            },
            "exam_pattern": "Suspicious ARM control-plane / management operations = Defender for Resource Manager.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for Resource Manager"],
    },
    {
        "id": "sc200-dfc-r2-011", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "On protected servers, a team wants to be alerted when critical operating-system files, "
                "registry keys, or application binaries are changed, to catch tampering. Which Defender for Cloud "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "File integrity monitoring (FIM)"},
            {"id": "B", "text": "Just-in-time VM access"},
            {"id": "C", "text": "Adaptive application controls"},
            {"id": "D", "text": "Regulatory compliance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "File integrity monitoring (part of Defender for Servers Plan 2) tracks changes to "
                       "important OS files, registry keys, and application files, alerting on potentially suspicious modifications.",
            "distractors": {
                "B": "JIT controls management-port exposure; it does not watch file/registry changes.",
                "C": "Adaptive application controls allowlist known-good apps; they are not file-change monitoring.",
                "D": "Regulatory compliance maps controls to standards; it does not alert on file changes.",
            },
            "exam_pattern": "Alert on changes to OS/registry/app files = file integrity monitoring (FIM).",
        },
        "references": ["Microsoft Learn (SC-200): File integrity monitoring in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-012", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "An organization publishes REST APIs through Azure API Management and wants threat detection "
                "and security insights specifically for those APIs (e.g., anomalous or malicious API access). "
                "Which plan should be enabled?",
        "options": [
            {"id": "A", "text": "Defender for APIs"},
            {"id": "B", "text": "Defender for App Service"},
            {"id": "C", "text": "Defender for Storage"},
            {"id": "D", "text": "Foundational CSPM"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for APIs provides threat detection and security posture insights for APIs "
                       "published in Azure API Management, surfacing anomalous or malicious API usage.",
            "distractors": {
                "B": "Defender for App Service protects web apps hosted on App Service, not APIs managed by API Management.",
                "C": "Defender for Storage covers storage accounts, not API traffic.",
                "D": "Foundational CSPM provides posture recommendations, not API runtime threat detection.",
            },
            "exam_pattern": "Threat detection for APIs in Azure API Management = Defender for APIs.",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Defender for APIs"],
    },
    {
        "id": "sc200-dfc-r2-013", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 1, "type": "mcq",
        "stem": "Which statement best describes how Microsoft Defender for Cloud workload protection plans are enabled?",
        "options": [
            {"id": "A", "text": "They are enabled granularly - you turn on individual Defender plans per subscription (and some per resource) as needed"},
            {"id": "B", "text": "All plans are always on and cannot be turned off"},
            {"id": "C", "text": "Enabling any one plan automatically enables all other plans"},
            {"id": "D", "text": "Plans can only be enabled for the entire Azure tenant at once"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender plans are toggled individually (per subscription, and for some workloads per "
                       "resource), so you can protect exactly the resource types you need and manage cost.",
            "distractors": {
                "B": "Plans are optional and can be enabled or disabled; they are not always on.",
                "C": "Enabling one plan does not enable the others; each is separate.",
                "D": "Plans are enabled at the subscription (or resource) level, not only tenant-wide.",
            },
            "exam_pattern": "Defender plans = enabled per subscription/resource, individually (cost/scope control).",
        },
        "references": ["Microsoft Learn (SC-200): Enable Microsoft Defender for Cloud plans"],
    },
    {
        "id": "sc200-dfc-r2-014", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "multi",
        "stem": "To receive threat alerts for the following two resource types, an organization must enable "
                "the corresponding Defender plan for EACH. Which TWO pairings are correct? (Choose two.)",
        "options": [
            {"id": "A", "text": "Azure SQL databases -> Defender for Databases (Defender for SQL)"},
            {"id": "B", "text": "Azure Storage accounts -> Defender for Storage"},
            {"id": "C", "text": "Any resource -> Secure Score (free)"},
            {"id": "D", "text": "Any resource -> the Regulatory compliance dashboard"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Runtime threat alerts for SQL databases require Defender for Databases/SQL, and for "
                       "storage accounts require Defender for Storage - each resource type has its own workload plan.",
            "distractors": {
                "C": "Secure Score is free posture management; it does not provide resource threat alerts.",
                "D": "The Regulatory compliance dashboard maps controls to standards; it is not a threat-alert plan.",
            },
            "exam_pattern": "Threat alerts are per-plan: SQL -> Defender for Databases; Storage -> Defender for Storage.",
        },
        "references": ["Microsoft Learn (SC-200): Workload protection plans by resource type"],
    },
    {
        "id": "sc200-dfc-r2-015", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_workloads", "difficulty": 2, "type": "mcq",
        "stem": "With Defender for Servers Plan 2 enabled, where do the discovered CVEs/weaknesses on a "
                "protected virtual machine appear for the analyst to review and prioritize?",
        "options": [
            {"id": "A", "text": "As vulnerability assessment findings/recommendations (via the integrated Defender Vulnerability Management scanner)"},
            {"id": "B", "text": "As Microsoft Sentinel watchlists"},
            {"id": "C", "text": "As Conditional Access reports"},
            {"id": "D", "text": "As quarantine policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Servers integrates Microsoft Defender Vulnerability Management, so VM "
                       "software vulnerabilities (CVEs) surface as assessment findings and security recommendations to triage and remediate.",
            "distractors": {
                "B": "Watchlists are Sentinel reference data, not VM vulnerability findings.",
                "C": "Conditional Access reports cover sign-in policy, not VM CVEs.",
                "D": "Quarantine policies are a Defender for Office 365 construct, unrelated to VM vulnerabilities.",
            },
            "exam_pattern": "Server CVEs with Defender for Servers = integrated vulnerability assessment (MDVM) findings/recommendations.",
        },
        "references": ["Microsoft Learn (SC-200): Vulnerability assessment for machines in Defender for Cloud"],
    },

    # ----- sc200_dfc_alerts -----------------------------------------------
    {
        "id": "sc200-dfc-r2-016", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "A team wants Microsoft Defender for Cloud to continuously send its alerts and "
                "recommendations to a Log Analytics workspace and to an Event Hub (to feed a third-party SIEM). "
                "Which feature is designed for this?",
        "options": [
            {"id": "A", "text": "Continuous export"},
            {"id": "B", "text": "Just-in-time VM access"},
            {"id": "C", "text": "Secure Score"},
            {"id": "D", "text": "Alert suppression"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Continuous export streams Defender for Cloud alerts and recommendations to a Log "
                       "Analytics workspace or Event Hub, enabling downstream integration (e.g., a third-party SIEM).",
            "distractors": {
                "B": "JIT controls management-port exposure; it does not export alerts.",
                "C": "Secure Score measures posture; it is not an export pipeline.",
                "D": "Alert suppression quiets specific alerts; it does not export data.",
            },
            "exam_pattern": "Stream Defender for Cloud alerts/recommendations out (Log Analytics / Event Hub) = continuous export.",
        },
        "references": ["Microsoft Learn (SC-200): Continuously export Microsoft Defender for Cloud data"],
    },
    {
        "id": "sc200-dfc-r2-017", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "Before an incident occurs, a SOC wants to validate that their Defender for Cloud alert "
                "pipeline and automation (exports, playbooks) actually fire. What is the safe, supported way to produce test alerts?",
        "options": [
            {"id": "A", "text": "Generate sample alerts from Microsoft Defender for Cloud"},
            {"id": "B", "text": "Run real malware on a production VM"},
            {"id": "C", "text": "Delete a storage account"},
            {"id": "D", "text": "Lower the Secure Score target"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud can generate sample alerts, letting teams validate alert routing, "
                       "exports, and automation end to end without a real attack.",
            "distractors": {
                "B": "Running real malware is dangerous and unnecessary; sample alerts exist for safe testing.",
                "C": "Deleting resources is destructive and does not validate the alert pipeline.",
                "D": "Secure Score targets are unrelated to generating test alerts.",
            },
            "exam_pattern": "Safely test the alert/automation pipeline = generate sample alerts.",
        },
        "references": ["Microsoft Learn (SC-200): Generate sample security alerts in Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-018", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Defender for Cloud observes several related alerts on the same resources that "
                "appear to be stages of one attack. How does Defender for Cloud help the analyst see the bigger picture?",
        "options": [
            {"id": "A", "text": "It correlates related alerts into a security incident"},
            {"id": "B", "text": "It deletes the lower-severity alerts automatically"},
            {"id": "C", "text": "It converts the alerts into recommendations"},
            {"id": "D", "text": "It raises the Secure Score"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud correlates related alerts into a single security incident, grouping "
                       "the stages of an attack so analysts can respond to the whole story rather than isolated alerts.",
            "distractors": {
                "B": "Related alerts are grouped, not deleted; evidence is preserved.",
                "C": "Alerts are detected threats; they are not converted into posture recommendations.",
                "D": "Correlating alerts does not change Secure Score (which reflects recommendations).",
            },
            "exam_pattern": "Related Defender for Cloud alerts grouped into one attack view = a security incident.",
        },
        "references": ["Microsoft Learn (SC-200): Security alerts and incidents in Microsoft Defender for Cloud"],
    },
    {
        "id": "sc200-dfc-r2-019", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants the right people emailed automatically whenever a high-severity "
                "Microsoft Defender for Cloud alert fires on a subscription. Which setting enables this?",
        "options": [
            {"id": "A", "text": "Email notifications (configured per subscription by severity/role)"},
            {"id": "B", "text": "A Microsoft Sentinel watchlist"},
            {"id": "C", "text": "A quarantine policy"},
            {"id": "D", "text": "Just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud email notification settings let you choose who is emailed (by role "
                       "such as Owner, and by minimum alert severity) when alerts occur on a subscription.",
            "distractors": {
                "B": "Watchlists are Sentinel reference data; they do not send Defender for Cloud alert emails.",
                "C": "Quarantine policies are a Defender for Office 365 construct, unrelated to alert emails.",
                "D": "JIT reduces port exposure; it does not notify on alerts.",
            },
            "exam_pattern": "Email the right people on high-severity alerts = Defender for Cloud email notifications (by severity/role).",
        },
        "references": ["Microsoft Learn (SC-200): Configure email notifications for security alerts"],
    },
    {
        "id": "sc200-dfc-r2-020", "exam": "sc200", "domain": "sc200_defender_cloud",
        "subtopic": "sc200_dfc_alerts", "difficulty": 2, "type": "mcq",
        "stem": "After investigation, an analyst concludes a Defender for Cloud alert is a false positive. "
                "They set the alert status to 'Dismissed'. What does dismissing the alert signify?",
        "options": [
            {"id": "A", "text": "The alert is closed as not requiring action (e.g., false positive), without remediating a threat"},
            {"id": "B", "text": "The affected resource is deleted"},
            {"id": "C", "text": "The Defender plan is turned off"},
            {"id": "D", "text": "The alert is permanently prevented from ever recurring"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Dismissing marks the alert as not actionable (such as a false positive or benign), "
                       "closing it in the queue; it records the outcome but does not, by itself, stop similar future alerts.",
            "distractors": {
                "B": "Dismissing changes the alert status; it does not delete resources.",
                "C": "Dismissing one alert does not disable the plan.",
                "D": "To stop a recurring benign pattern you use a suppression rule; dismissing a single alert does not prevent recurrence.",
            },
            "exam_pattern": "Dismiss = close as not actionable; suppress = stop a recurring benign pattern.",
        },
        "references": ["Microsoft Learn (SC-200): Manage and respond to security alerts (alert status)"],
    },

    # =====================================================================
    # DOMAIN 3 - Mitigate threats with Microsoft Sentinel (38%)
    # =====================================================================

    # ----- sc200_sentinel_setup -------------------------------------------
    {
        "id": "sc200-sent-r2-001", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to manage Microsoft Sentinel together with Defender XDR in the "
                "unified Microsoft Defender portal. What is a key prerequisite/consideration for onboarding?",
        "options": [
            {"id": "A", "text": "You onboard a Log Analytics workspace that has Microsoft Sentinel enabled (one primary workspace to the unified portal)"},
            {"id": "B", "text": "You must delete the Log Analytics workspace first"},
            {"id": "C", "text": "Sentinel must be moved to an Azure Storage account"},
            {"id": "D", "text": "Every user needs the Global Administrator role"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel runs on a Log Analytics workspace with Sentinel enabled; onboarding to the "
                       "Defender portal connects that workspace (one primary workspace) so XDR and Sentinel share one incident queue.",
            "distractors": {
                "B": "Deleting the workspace would destroy all Sentinel data; the workspace is required.",
                "C": "Sentinel data stays in Log Analytics; it is not moved to a storage account.",
                "D": "Global Administrator is not required for every user; least-privilege roles are used.",
            },
            "exam_pattern": "Unified portal = onboard the Sentinel-enabled Log Analytics workspace (one primary workspace).",
        },
        "references": ["Microsoft Learn (SC-200): Connect Microsoft Sentinel to the Microsoft Defender portal"],
    },
    {
        "id": "sc200-sent-r2-002", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "An engineer needs to create and edit Microsoft Sentinel analytics rules and manage content, "
                "but should not be granted broad subscription Owner rights. Which built-in role is the least-privilege fit?",
        "options": [
            {"id": "A", "text": "Microsoft Sentinel Reader"},
            {"id": "B", "text": "Microsoft Sentinel Responder"},
            {"id": "C", "text": "Microsoft Sentinel Contributor"},
            {"id": "D", "text": "Subscription Owner"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Sentinel Contributor allows creating and editing analytics rules, workbooks, "
                       "and other content (on top of read and incident management) - the least-privilege role for authoring detections.",
            "distractors": {
                "A": "Reader can only view; it cannot create or edit rules.",
                "B": "Responder adds incident management but not rule authoring.",
                "D": "Subscription Owner is far broader than needed for authoring Sentinel content.",
            },
            "exam_pattern": "Author/edit analytics rules = Sentinel Contributor; triage only = Responder; view = Reader.",
        },
        "references": ["Microsoft Learn (SC-200): Roles and permissions in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-003", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 3, "type": "mcq",
        "stem": "A company keeps two Microsoft Sentinel workspaces (one per region) and needs a single KQL "
                "query that returns results from a table in BOTH workspaces. Which approach works?",
        "options": [
            {"id": "A", "text": "Use the workspace() expression to reference the other workspace and union the results (cross-workspace query)"},
            {"id": "B", "text": "It is impossible to query more than one workspace"},
            {"id": "C", "text": "Export both to a CSV and merge manually"},
            {"id": "D", "text": "Move all data into a single Azure SQL database"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Cross-workspace queries use the workspace(\"...\") expression (often with union) so a "
                       "single KQL query spans tables across multiple workspaces - useful for multi-region or multi-tenant SOCs.",
            "distractors": {
                "B": "Multi-workspace querying is supported via the workspace() expression.",
                "C": "Manual CSV merging is not a query mechanism and does not scale.",
                "D": "Sentinel data lives in Log Analytics; moving it to SQL is neither required nor how cross-workspace queries work.",
            },
            "exam_pattern": "Query across workspaces = workspace(\"name\").Table (+ union) cross-workspace query.",
        },
        "references": ["Microsoft Learn (SC-200): Query multiple workspaces in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-004", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 3, "type": "mcq",
        "stem": "A managed security service provider (MSSP) needs its analysts to manage many customers' "
                "Microsoft Sentinel workspaces from its own tenant, with delegated, auditable access. Which Azure "
                "capability is designed for this cross-tenant management?",
        "options": [
            {"id": "A", "text": "Azure Lighthouse (delegated resource management)"},
            {"id": "B", "text": "Microsoft Entra Connect"},
            {"id": "C", "text": "A Sentinel watchlist"},
            {"id": "D", "text": "Conditional Access App Control"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Lighthouse enables delegated, cross-tenant resource management, so an MSSP can "
                       "manage multiple customers' Sentinel workspaces from a single pane with scoped, auditable access.",
            "distractors": {
                "B": "Entra Connect syncs on-prem identities to Entra ID; it is not cross-tenant Azure resource delegation.",
                "C": "Watchlists are reference data in a workspace; they do not provide cross-tenant management.",
                "D": "Conditional Access App Control is a Defender for Cloud Apps session-control feature, not MSSP delegation.",
            },
            "exam_pattern": "MSSP managing many tenants' Sentinel workspaces = Azure Lighthouse (delegated management).",
        },
        "references": ["Microsoft Learn (SC-200): Manage multiple tenants with Azure Lighthouse and Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-005", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "A SOC ingests high-value security logs that must be available for real-time scheduled "
                "analytics rules and frequent interactive hunting. Which Log Analytics table plan should these tables use?",
        "options": [
            {"id": "A", "text": "Analytics logs"},
            {"id": "B", "text": "Basic logs"},
            {"id": "C", "text": "Auxiliary logs"},
            {"id": "D", "text": "Archive-only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Analytics table plan is for high-value data used in continuous monitoring, "
                       "real-time detection, and frequent analytics - and it is the plan scheduled analytics rules require.",
            "distractors": {
                "B": "Basic logs are for medium-touch, occasional troubleshooting data with limited query features; scheduled analytics rules can't run on Basic tables.",
                "C": "Auxiliary (data lake) logs are low-cost, low-touch data for verbose logs/compliance, not real-time detection.",
                "D": "Archive is long-term retention, not an interactive query plan for real-time detection.",
            },
            "exam_pattern": "Real-time detection + frequent hunting = Analytics tier; cheap/low-touch = Basic/Auxiliary.",
        },
        "references": ["Microsoft Learn (SC-200): Manage data tiers (Analytics, Basic, Auxiliary) in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-006", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "mcq",
        "stem": "Compliance requires keeping certain security logs for seven years, but analysts only query "
                "the last 90 days interactively. What is the cost-appropriate way to meet this in Log "
                "Analytics/Microsoft Sentinel?",
        "options": [
            {"id": "A", "text": "Set interactive retention short and configure long-term (archive) retention for the rest (up to 12 years total)"},
            {"id": "B", "text": "Keep all data in interactive retention for seven years"},
            {"id": "C", "text": "Export everything to email"},
            {"id": "D", "text": "Delete data after 90 days and hope it isn't needed"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Configure a shorter interactive retention and extend long-term (archive) retention for "
                       "the remainder - total retention can reach up to 12 years - meeting compliance cost-effectively.",
            "distractors": {
                "B": "Keeping everything hot for seven years is far more expensive than using archive retention.",
                "C": "Email is not a retention mechanism and cannot hold log volumes.",
                "D": "Deleting data needed for compliance fails the requirement.",
            },
            "exam_pattern": "Short interactive + long-term archive retention (up to 12 years) for compliance.",
        },
        "references": ["Microsoft Learn (SC-200): Configure interactive and long-term data retention"],
    },
    {
        "id": "sc200-sent-r2-007", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 3, "type": "mcq",
        "stem": "Within one Log Analytics workspace, a team should be able to read only ONE specific table "
                "(for example, a sensitive application log), not all tables. Which approach grants this?",
        "options": [
            {"id": "A", "text": "Table-level RBAC (Azure role scoped to the specific table)"},
            {"id": "B", "text": "Making everyone a Sentinel Reader on the workspace"},
            {"id": "C", "text": "A watchlist"},
            {"id": "D", "text": "A workbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Table-level RBAC grants access to specific tables within a workspace, so a group can "
                       "read only the designated table rather than all workspace data.",
            "distractors": {
                "B": "Sentinel Reader on the workspace grants read across its data - broader than one table.",
                "C": "Watchlists store reference data; they are not an access-control mechanism.",
                "D": "Workbooks visualize data the viewer can already access; they do not grant per-table permissions.",
            },
            "exam_pattern": "Restrict access to a single table within a workspace = table-level RBAC.",
        },
        "references": ["Microsoft Learn (SC-200): Manage access to Microsoft Sentinel data by table (table-level RBAC)"],
    },
    {
        "id": "sc200-sent-r2-008", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_setup", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (one word, plural): To satisfy EU data-residency rules while running a "
                "single SOC, an organization can deploy multiple Microsoft Sentinel ______, each created in the "
                "region where its data must stay.",
        "correct": ["workspaces", "workspace"],
        "explanation": {
            "correct": "Because a workspace's region determines where its data is stored, residency is met by "
                       "deploying multiple workspaces in the required regions (then querying across them when needed).",
            "distractors": {},
            "exam_pattern": "Residency across regions = multiple workspaces (region = data location).",
        },
        "references": ["Microsoft Learn (SC-200): Design Microsoft Sentinel workspace architecture for residency"],
    },

    # ----- sc200_sentinel_connectors --------------------------------------
    {
        "id": "sc200-sent-r2-009", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "To ingest Windows Security event logs from servers into Microsoft Sentinel and control "
                "exactly which events are collected (All, Common, or Minimal), which collection method is used?",
        "options": [
            {"id": "A", "text": "The Windows Security Events connector via the Azure Monitor Agent, configured by a data collection rule (DCR)"},
            {"id": "B", "text": "A watchlist CSV import"},
            {"id": "C", "text": "The TAXII connector"},
            {"id": "D", "text": "A Logic App recurrence trigger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Windows Security Events are collected by the Azure Monitor Agent (AMA); a data "
                       "collection rule (DCR) defines the event set (All, Common, Minimal, or custom XPath) and lands data in the SecurityEvent table.",
            "distractors": {
                "B": "Watchlists import reference data; they do not collect Windows event logs.",
                "C": "TAXII pulls STIX threat indicators, not Windows event logs.",
                "D": "A recurrence trigger runs a playbook on a timer; it is not the event-collection pipeline.",
            },
            "exam_pattern": "Windows Security Events = AMA + DCR (choose All/Common/Minimal) -> SecurityEvent table.",
        },
        "references": ["Microsoft Learn (SC-200): Collect Windows security events with the Azure Monitor Agent"],
    },
    {
        "id": "sc200-sent-r2-010", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "An appliance sends plain Syslog messages (not CEF) to a Linux forwarder running the Azure "
                "Monitor Agent. Into which Microsoft Sentinel table does this data land?",
        "options": [
            {"id": "A", "text": "The Syslog table"},
            {"id": "B", "text": "The CommonSecurityLog table"},
            {"id": "C", "text": "The SigninLogs table"},
            {"id": "D", "text": "The SecurityAlert table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Plain Syslog messages are stored in the Syslog table; CEF-formatted messages are parsed "
                       "into the CommonSecurityLog table. Both are collected via AMA on a Linux forwarder.",
            "distractors": {
                "B": "CommonSecurityLog holds CEF-formatted data, not plain Syslog.",
                "C": "SigninLogs holds Microsoft Entra sign-ins, not appliance Syslog.",
                "D": "SecurityAlert holds alerts from connected products, not raw Syslog.",
            },
            "exam_pattern": "Plain Syslog -> Syslog table; CEF -> CommonSecurityLog table.",
        },
        "references": ["Microsoft Learn (SC-200): Syslog and CEF data in Microsoft Sentinel (Syslog vs CommonSecurityLog)"],
    },
    {
        "id": "sc200-sent-r2-011", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 3, "type": "mcq",
        "stem": "A team needs a data connector for a SaaS product that exposes a REST API, but they want to "
                "avoid writing and hosting custom code. Which Microsoft Sentinel capability lets them build the connector declaratively?",
        "options": [
            {"id": "A", "text": "The Codeless Connector Platform (CCP)"},
            {"id": "B", "text": "A scheduled analytics rule"},
            {"id": "C", "text": "A watchlist"},
            {"id": "D", "text": "A workbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Codeless Connector Platform lets you define a data connector for a REST API "
                       "declaratively (via configuration), without writing or hosting custom collection code.",
            "distractors": {
                "B": "A scheduled analytics rule detects threats in already-ingested data; it is not a data connector.",
                "C": "A watchlist imports reference data, not a streaming API connector.",
                "D": "A workbook visualizes data; it does not ingest it.",
            },
            "exam_pattern": "Build a REST-API connector without code = Codeless Connector Platform (CCP).",
        },
        "references": ["Microsoft Learn (SC-200): Create a codeless connector for Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-012", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 3, "type": "mcq",
        "stem": "A custom in-house application writes JSON logs that a team wants to send into a custom table "
                "in their Log Analytics workspace for Microsoft Sentinel. Which mechanism is intended for sending such custom data?",
        "options": [
            {"id": "A", "text": "The Logs ingestion API (with a data collection rule to a custom table)"},
            {"id": "B", "text": "The TAXII connector"},
            {"id": "C", "text": "The Microsoft Defender XDR connector"},
            {"id": "D", "text": "A session policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Logs ingestion API sends custom application data into a custom table via a data "
                       "collection rule (and DCE), the supported path for arbitrary custom logs.",
            "distractors": {
                "B": "TAXII ingests STIX threat indicators, not arbitrary custom app logs.",
                "C": "The Defender XDR connector streams XDR data, not your custom app logs.",
                "D": "A session policy is a Defender for Cloud Apps control, unrelated to log ingestion.",
            },
            "exam_pattern": "Send custom app logs to a custom table = Logs ingestion API + DCR.",
        },
        "references": ["Microsoft Learn (SC-200): Send custom logs with the Logs ingestion API"],
    },
    {
        "id": "sc200-sent-r2-013", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to bring Amazon Web Services logs (for example CloudTrail) into "
                "Microsoft Sentinel. Which ingestion method does the AWS connector commonly use?",
        "options": [
            {"id": "A", "text": "Pulling logs from an AWS S3 bucket (S3-based connector)"},
            {"id": "B", "text": "Installing the Azure Monitor Agent on every EC2 instance"},
            {"id": "C", "text": "A TAXII feed"},
            {"id": "D", "text": "A watchlist import"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AWS connector for Sentinel commonly ingests logs (CloudTrail, GuardDuty, VPC Flow) "
                       "by reading them from an S3 bucket that AWS is configured to write to.",
            "distractors": {
                "B": "AMA on each EC2 instance is for OS logs, not the AWS service logs the connector pulls from S3.",
                "C": "TAXII is for STIX threat indicators, not AWS service logs.",
                "D": "Watchlists import small reference datasets, not streaming AWS logs.",
            },
            "exam_pattern": "AWS logs into Sentinel = S3-based AWS connector (CloudTrail/GuardDuty/VPC).",
        },
        "references": ["Microsoft Learn (SC-200): Connect Amazon Web Services to Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-014", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants to verify that its data connectors are healthy and ingesting, and be alerted if "
                "a connector stops sending data. Which capability surfaces connector health/status in Microsoft Sentinel?",
        "options": [
            {"id": "A", "text": "Health monitoring (the SentinelHealth table / connector health)"},
            {"id": "B", "text": "The investigation graph"},
            {"id": "C", "text": "Secure Score"},
            {"id": "D", "text": "A Safe Attachments policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel health monitoring (including the SentinelHealth table) reports data connector "
                       "status and errors, so teams can detect and alert on connectors that stop ingesting.",
            "distractors": {
                "B": "The investigation graph visualizes an incident's entities; it does not report connector health.",
                "C": "Secure Score is a Defender for Cloud posture metric, not Sentinel connector health.",
                "D": "Safe Attachments is a Defender for Office 365 feature, unrelated to connector health.",
            },
            "exam_pattern": "Monitor/alert on connector ingestion health = Sentinel health (SentinelHealth table).",
        },
        "references": ["Microsoft Learn (SC-200): Monitor the health of your data connectors in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-015", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "mcq",
        "stem": "After installing a solution from the Content hub, a new analyst notices no data is flowing "
                "and no detections are firing. What is typically still required?",
        "options": [
            {"id": "A", "text": "Connect/configure the solution's data connector and enable its analytics rule templates"},
            {"id": "B", "text": "Nothing - installing a solution automatically ingests data and enables all rules"},
            {"id": "C", "text": "Delete and reinstall the workspace"},
            {"id": "D", "text": "Disable the Content hub"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Installing a Content hub solution deploys its components, but you still typically "
                       "connect/configure the data connector and enable the included analytics rule templates for detections to run.",
            "distractors": {
                "B": "Solutions bundle content but do not auto-connect data sources or auto-enable every rule.",
                "C": "Reinstalling the workspace is destructive and unnecessary.",
                "D": "Disabling the Content hub does not make data flow; the connector must be configured.",
            },
            "exam_pattern": "Solution installed != data flowing; still connect the data connector + enable rule templates.",
        },
        "references": ["Microsoft Learn (SC-200): Deploy and manage out-of-the-box content from the Content hub"],
    },
    {
        "id": "sc200-sent-r2-016", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 3, "type": "mcq",
        "stem": "When configuring Syslog/CEF or Windows event collection today, which agent should be used, "
                "given the retirement of the legacy agent?",
        "options": [
            {"id": "A", "text": "The Azure Monitor Agent (AMA), with collection defined by data collection rules"},
            {"id": "B", "text": "The legacy Log Analytics agent (MMA/OMS)"},
            {"id": "C", "text": "Microsoft Entra Connect"},
            {"id": "D", "text": "The on-premises data gateway only"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Azure Monitor Agent (AMA) is the current agent; collection is controlled by data "
                       "collection rules. The legacy Log Analytics agent (MMA/OMS) has been retired and should not be used for new deployments.",
            "distractors": {
                "B": "The legacy Log Analytics agent (MMA) is retired; AMA replaces it.",
                "C": "Entra Connect syncs identities; it is not a log-collection agent.",
                "D": "The on-premises data gateway supports some integrations but is not the agent for Syslog/CEF/Windows event collection.",
            },
            "exam_pattern": "Current collection agent = AMA (DCR-driven); MMA/Log Analytics agent is retired.",
        },
        "references": ["Microsoft Learn (SC-200): Migrate to the Azure Monitor Agent for Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-017", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_connectors", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (one table name): Firewall logs forwarded in Common Event Format (CEF) and "
                "collected by the Azure Monitor Agent are stored in Microsoft Sentinel's ______ table.",
        "correct": ["CommonSecurityLog"],
        "explanation": {
            "correct": "CEF data parses into the CommonSecurityLog table, whereas plain Syslog lands in the Syslog table.",
            "distractors": {},
            "exam_pattern": "CEF -> CommonSecurityLog; plain Syslog -> Syslog.",
        },
        "references": ["Microsoft Learn (SC-200): CEF data and the CommonSecurityLog table in Microsoft Sentinel"],
    },

    # ----- sc200_sentinel_analytics ---------------------------------------
    {
        "id": "sc200-sent-r2-018", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants ML-driven detection of unusual behavior but needs to adjust the sensitivity "
                "(thresholds) of a built-in anomaly detection to fit their environment. What is true about "
                "Microsoft Sentinel anomaly rules?",
        "options": [
            {"id": "A", "text": "They are customizable ML templates - you can duplicate and tune their parameters/thresholds"},
            {"id": "B", "text": "They require you to write the detection KQL from scratch"},
            {"id": "C", "text": "They cannot be changed in any way"},
            {"id": "D", "text": "They only work on firewall data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Anomaly rules are built on Microsoft's ML models but are customizable: you can "
                       "duplicate a template and tune its parameters/thresholds, then run it in flighting or production.",
            "distractors": {
                "B": "The ML logic is provided; you tune parameters rather than author the detection query.",
                "C": "Anomaly rules are tunable (thresholds/parameters), not fixed.",
                "D": "Anomaly rules cover many behaviors/data types, not only firewall data.",
            },
            "exam_pattern": "Anomaly rules = tunable ML templates (adjust thresholds), not hand-written KQL.",
        },
        "references": ["Microsoft Learn (SC-200): Use customizable anomalies to detect threats in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-019", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "In a scheduled analytics rule, what is the purpose of entity mapping?",
        "options": [
            {"id": "A", "text": "To link query result columns (e.g., Account, IP, Host) to entity types so alerts/incidents are investigable and can be correlated"},
            {"id": "B", "text": "To set how often the query runs"},
            {"id": "C", "text": "To choose which chart renders the results"},
            {"id": "D", "text": "To export the data to storage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Entity mapping ties result columns to recognized entity types (Account, IP, Host, "
                       "etc.), so alerts carry identifiable entities for investigation, enrichment, and entity-based incident grouping (up to 10 entity mappings per rule).",
            "distractors": {
                "B": "Run frequency is set by the query scheduling, not entity mapping.",
                "C": "Chart selection is a visualization choice, unrelated to entity mapping.",
                "D": "Exporting data is not what entity mapping does.",
            },
            "exam_pattern": "Map columns to entities so alerts are investigable/correlatable = entity mapping (max 10 per rule).",
        },
        "references": ["Microsoft Learn (SC-200): Map data fields to entities in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-020", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 3, "type": "mcq",
        "stem": "A detection should raise a SEPARATE alert for each matching event (so every risky sign-in "
                "is tracked individually), rather than one alert summarizing the whole query run. Which analytics "
                "rule setting controls this?",
        "options": [
            {"id": "A", "text": "Event grouping (trigger an alert for each event vs. a single alert per rule run)"},
            {"id": "B", "text": "Entity mapping"},
            {"id": "C", "text": "The MITRE ATT&CK mapping"},
            {"id": "D", "text": "The lookback period"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Event grouping chooses whether the rule produces a single alert per run (default) or a "
                       "separate alert for each event returned - the latter tracks each matching row individually.",
            "distractors": {
                "B": "Entity mapping links fields to entities; it does not control alert-per-event behavior.",
                "C": "MITRE mapping tags tactics/techniques; it does not split results into per-event alerts.",
                "D": "The lookback period sets how far back the query reads, not how results become alerts.",
            },
            "exam_pattern": "One alert per run vs one per event = event grouping setting.",
        },
        "references": ["Microsoft Learn (SC-200): Event grouping in Microsoft Sentinel scheduled rules"],
    },
    {
        "id": "sc200-sent-r2-021", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 3, "type": "mcq",
        "stem": "A noisy rule creates a flood of separate incidents when the same account is involved. The "
                "SOC wants alerts that share the same mapped entities to be collapsed into a single incident. "
                "Which analytics rule setting achieves this?",
        "options": [
            {"id": "A", "text": "Incident settings - alert grouping (group alerts with matching entities into one incident)"},
            {"id": "B", "text": "Event grouping"},
            {"id": "C", "text": "Query scheduling frequency"},
            {"id": "D", "text": "Data connector health"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Alert grouping (under a rule's incident settings) can group related alerts into one "
                       "incident - for example, by matching entities/details within a time window - reducing duplicate incidents.",
            "distractors": {
                "B": "Event grouping controls alert creation per run/event, not how alerts become one incident.",
                "C": "Frequency sets how often the query runs, not incident grouping.",
                "D": "Connector health is unrelated to grouping alerts into incidents.",
            },
            "exam_pattern": "Collapse related alerts into one incident = alert grouping (incident settings).",
        },
        "references": ["Microsoft Learn (SC-200): Group alerts into incidents in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-022", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "When configuring a scheduled analytics rule, how do the 'run query every' and 'lookup data "
                "from the last' settings differ?",
        "options": [
            {"id": "A", "text": "'Run query every' is the frequency (how often it executes); 'lookup data from the last' is the lookback window of data each run examines"},
            {"id": "B", "text": "They are the same setting with two names"},
            {"id": "C", "text": "'Run query every' sets retention; 'lookup data from the last' sets severity"},
            {"id": "D", "text": "Both control only the alert title"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Frequency defines how often the rule runs; the lookback period defines how far back "
                       "each execution queries data. They are set independently (e.g., run every 5 minutes over the last 1 hour).",
            "distractors": {
                "B": "They are distinct settings - execution cadence vs. data window.",
                "C": "Neither sets retention or severity.",
                "D": "Neither controls the alert title.",
            },
            "exam_pattern": "Frequency (how often) vs lookback period (how far back each run reads) - set separately.",
        },
        "references": ["Microsoft Learn (SC-200): Schedule and scope scheduled analytics rules"],
    },
    {
        "id": "sc200-sent-r2-023", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 3, "type": "mcq",
        "stem": "After a scheduled rule fires, a team wants it to stop re-running for a set period to avoid "
                "repeated alerts on the same ongoing condition. Which rule option provides this?",
        "options": [
            {"id": "A", "text": "Suppression - 'Stop running query after alert is generated' for a chosen duration"},
            {"id": "B", "text": "Lowering the alert severity"},
            {"id": "C", "text": "Entity mapping"},
            {"id": "D", "text": "Changing the MITRE technique"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The rule's suppression setting ('Stop running query after alert is generated') pauses "
                       "the rule for a specified duration once it fires, preventing repeated alerts on the same condition.",
            "distractors": {
                "B": "Severity affects prioritization, not whether the rule keeps firing.",
                "C": "Entity mapping identifies entities; it does not suppress re-runs.",
                "D": "The MITRE technique is metadata; it does not control re-running.",
            },
            "exam_pattern": "Pause a rule after it fires (avoid repeats) = suppression ('stop running after alert').",
        },
        "references": ["Microsoft Learn (SC-200): Alert suppression in scheduled analytics rules"],
    },
    {
        "id": "sc200-sent-r2-024", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "mcq",
        "stem": "To report detection coverage against adversary techniques, a SOC tags each analytics rule "
                "with the tactics and techniques it detects. Which framework does Microsoft Sentinel use for this mapping?",
        "options": [
            {"id": "A", "text": "MITRE ATT&CK (tactics and techniques)"},
            {"id": "B", "text": "ISO/IEC 27001"},
            {"id": "C", "text": "PCI DSS"},
            {"id": "D", "text": "The Microsoft Cloud Security Benchmark"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel maps analytics rules to MITRE ATT&CK tactics and techniques, and the MITRE "
                       "ATT&CK coverage view shows which techniques your enabled rules cover.",
            "distractors": {
                "B": "ISO 27001 is a compliance standard, not an adversary technique taxonomy.",
                "C": "PCI DSS is a payment-card compliance standard, not ATT&CK.",
                "D": "MCSB is a Defender for Cloud posture benchmark, not detection-technique mapping.",
            },
            "exam_pattern": "Rule technique tagging / coverage = MITRE ATT&CK.",
        },
        "references": ["Microsoft Learn (SC-200): Understand security coverage by the MITRE ATT&CK framework"],
    },
    {
        "id": "sc200-sent-r2-025", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 1, "type": "mcq",
        "stem": "What is the fastest supported way to start detecting with proven logic in Microsoft "
                "Sentinel, rather than writing every scheduled rule from a blank query?",
        "options": [
            {"id": "A", "text": "Create rules from the built-in analytics rule templates (from the Content hub/Analytics)"},
            {"id": "B", "text": "Only write each KQL detection by hand"},
            {"id": "C", "text": "Import rules by email"},
            {"id": "D", "text": "Use a watchlist as a rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel provides analytics rule templates (via the Content hub/Analytics blade) that "
                       "you instantiate and tune, giving proven detection logic quickly without authoring from scratch.",
            "distractors": {
                "B": "Hand-writing every rule is slower and skips Microsoft's and vendors' tested templates.",
                "C": "Rules are not imported by email.",
                "D": "A watchlist is reference data, not an analytics rule.",
            },
            "exam_pattern": "Fast proven detections = instantiate analytics rule templates (then tune).",
        },
        "references": ["Microsoft Learn (SC-200): Create analytics rules from templates in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-026", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 3, "type": "mcq",
        "stem": "An analyst tries to create a scheduled analytics rule whose query references a table "
                "configured with the Basic logs plan, but Sentinel won't let the rule be created. Why?",
        "options": [
            {"id": "A", "text": "Scheduled analytics rules require Analytics-tier tables; Basic/Auxiliary logs can't back a scheduled rule"},
            {"id": "B", "text": "Scheduled rules can only query one table ever"},
            {"id": "C", "text": "Basic logs are encrypted and unqueryable"},
            {"id": "D", "text": "The rule needs a workbook first"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Scheduled analytics rules run on Analytics-tier data. Tables on the Basic (or "
                       "Auxiliary) plan are intended for lower-cost, limited querying and can't drive scheduled "
                       "analytics rules; switch the table to Analytics if continuous detection is required.",
            "distractors": {
                "B": "Scheduled rules can reference multiple tables; the blocker here is the Basic table plan.",
                "C": "Basic logs are queryable (with limits); they are not unqueryable due to encryption.",
                "D": "A workbook is not a prerequisite for creating analytics rules.",
            },
            "exam_pattern": "Scheduled rule needs Analytics tier; Basic/Auxiliary tables can't back it.",
        },
        "references": ["Microsoft Learn (SC-200): Table plans and analytics rules in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-027", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_analytics", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank (two words): In a scheduled analytics rule, the ______ ______ defines how "
                "far back in time each execution of the query reads data (for example, the last 1 hour).",
        "correct": ["lookback period", "look back period"],
        "explanation": {
            "correct": "The lookback period is the time window of data each run of the rule examines; it is set "
                       "independently of the run frequency.",
            "distractors": {},
            "exam_pattern": "Time window each run reads = lookback period (separate from run frequency).",
        },
        "references": ["Microsoft Learn (SC-200): Query scheduling and lookback in scheduled analytics rules"],
    },

    # ----- sc200_sentinel_soar --------------------------------------------
    {
        "id": "sc200-sent-r2-028", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 2, "type": "mcq",
        "stem": "A particular analytics rule reliably produces benign, low-value incidents that clutter the "
                "queue. Without disabling the rule, the SOC wants matching incidents automatically closed. What should they configure?",
        "options": [
            {"id": "A", "text": "An automation rule that sets the incident status to Closed for matching conditions"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A workbook"},
            {"id": "D", "text": "A near-real-time analytics rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An automation rule can match incidents by condition (e.g., from a specific rule or "
                       "with certain properties) and automatically change status to Closed with a classification - quieting noise without disabling detection.",
            "distractors": {
                "B": "Watchlists store reference data; they do not close incidents.",
                "C": "Workbooks visualize data; they do not act on incidents.",
                "D": "An NRT rule is a detection type; it does not auto-close noisy incidents.",
            },
            "exam_pattern": "Auto-close benign incidents from a rule = automation rule (set status Closed).",
        },
        "references": ["Microsoft Learn (SC-200): Automatically close incidents with automation rules"],
    },
    {
        "id": "sc200-sent-r2-029", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 3, "type": "mcq",
        "stem": "Several automation rules could apply to the same incident, and the SOC needs predictable "
                "behavior for which runs first. How is execution sequence determined among automation rules?",
        "options": [
            {"id": "A", "text": "By the order (priority number) assigned to each automation rule - they run in that sequence"},
            {"id": "B", "text": "Randomly each time"},
            {"id": "C", "text": "Alphabetically by playbook name"},
            {"id": "D", "text": "By the size of the Log Analytics workspace"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation rules run in the order defined by their assigned order/priority value, so you "
                       "control the sequence of actions applied to an incident.",
            "distractors": {
                "B": "Execution is deterministic by order, not random.",
                "C": "Ordering is by the rule's order value, not playbook name.",
                "D": "Workspace size does not determine automation rule order.",
            },
            "exam_pattern": "Automation rule sequence = the order/priority value you assign.",
        },
        "references": ["Microsoft Learn (SC-200): Automation rules order and execution in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-030", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 3, "type": "mcq",
        "stem": "An automation rule fails to run a playbook, with a permissions error. What is the usual cause/fix?",
        "options": [
            {"id": "A", "text": "Microsoft Sentinel must be granted permissions to run the playbook (e.g., the Microsoft Sentinel Automation Contributor role on the playbook's resource group)"},
            {"id": "B", "text": "The playbook must be rewritten as a watchlist"},
            {"id": "C", "text": "The workspace must be moved to another region"},
            {"id": "D", "text": "The analytics rule must be deleted"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "For an automation rule to run a Logic App playbook, Microsoft Sentinel needs explicit "
                       "permission on the playbook's resource group (the Microsoft Sentinel Automation Contributor role), otherwise it can't invoke it.",
            "distractors": {
                "B": "A playbook is a Logic App workflow; it cannot be a watchlist.",
                "C": "Region moves do not resolve a playbook-run permissions error.",
                "D": "Deleting the analytics rule removes the detection; it does not fix playbook permissions.",
            },
            "exam_pattern": "Playbook won't run from automation = grant Sentinel permission on the playbook resource group.",
        },
        "references": ["Microsoft Learn (SC-200): Grant Microsoft Sentinel permission to run playbooks"],
    },
    {
        "id": "sc200-sent-r2-031", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 2, "type": "mcq",
        "stem": "During an investigation, an analyst wants to run a playbook against a single IP-address "
                "entity (to enrich it with reputation data) on demand. Which playbook trigger supports running "
                "against an individual entity?",
        "options": [
            {"id": "A", "text": "The Microsoft Sentinel entity trigger"},
            {"id": "B", "text": "A blob-created trigger"},
            {"id": "C", "text": "A recurrence (timer) trigger"},
            {"id": "D", "text": "An FTP trigger"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Sentinel entity trigger lets a playbook take a single entity (such as an "
                       "IP, account, or host) as input, so analysts can run enrichment/response against that entity on demand.",
            "distractors": {
                "B": "A blob-created trigger fires on storage events, not entities.",
                "C": "A recurrence trigger runs on a timer, not against a chosen entity.",
                "D": "An FTP trigger is unrelated to Sentinel entities.",
            },
            "exam_pattern": "Run a playbook on one entity = entity trigger; on incidents = incident trigger; on alerts = alert trigger.",
        },
        "references": ["Microsoft Learn (SC-200): Entity triggers for playbooks in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-032", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 1, "type": "mcq",
        "stem": "An analyst reviewing an incident wants to immediately execute a specific response playbook "
                "themselves (not wait for an automated rule). Can this be done?",
        "options": [
            {"id": "A", "text": "Yes - a playbook can be run manually (on demand) from an incident, alert, or entity"},
            {"id": "B", "text": "No - playbooks only run on a timer"},
            {"id": "C", "text": "No - playbooks run only when the workspace is created"},
            {"id": "D", "text": "Yes - but only by deleting the incident"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Playbooks can be triggered manually (on demand) from an incident, alert, or entity, "
                       "letting analysts invoke response actions during an investigation in addition to automated runs.",
            "distractors": {
                "B": "Playbooks are not timer-only; they support manual and event-based triggers.",
                "C": "Playbooks are not limited to workspace creation.",
                "D": "Deleting the incident is unrelated to running a playbook.",
            },
            "exam_pattern": "Playbooks can be run on demand from an incident/alert/entity, not only automatically.",
        },
        "references": ["Microsoft Learn (SC-200): Run playbooks on demand in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-033", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 2, "type": "mcq",
        "stem": "Which statement about Microsoft Sentinel automation rules is correct?",
        "options": [
            {"id": "A", "text": "They can be triggered when an incident is created or updated (and when alerts are created), and can run playbooks or change incident properties"},
            {"id": "B", "text": "They can only run once per day on a fixed timer"},
            {"id": "C", "text": "They can only send email and nothing else"},
            {"id": "D", "text": "They replace the need for any analytics rules"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Automation rules can trigger on incident creation or update (and on alert creation), "
                       "and can set properties (status, severity, owner, tags) and/or run playbooks - centralizing incident handling.",
            "distractors": {
                "B": "Automation rules are event-driven (incident/alert), not a once-daily timer.",
                "C": "They do far more than email - assign, tag, close, run playbooks, etc.",
                "D": "They orchestrate response; detections still come from analytics rules.",
            },
            "exam_pattern": "Automation rules trigger on incident create/update (and alert create) and orchestrate handling.",
        },
        "references": ["Microsoft Learn (SC-200): Automation rules triggers and actions in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-034", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 3, "type": "mcq",
        "stem": "Inside a Logic App playbook, which Microsoft Sentinel connector actions let the workflow "
                "enrich and update the incident it was triggered by?",
        "options": [
            {"id": "A", "text": "Actions such as 'Get incident', 'Get entities', 'Add comment to incident', and 'Update incident' (status/severity)"},
            {"id": "B", "text": "Only 'Delete workspace'"},
            {"id": "C", "text": "Only Azure DevOps pipeline actions"},
            {"id": "D", "text": "Only storage-account file actions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Sentinel Logic Apps connector provides incident actions (get incident/"
                       "entities, add a comment, update status/severity, add tags), so playbooks can enrich and progress the incident.",
            "distractors": {
                "B": "Playbooks do not operate by deleting the workspace.",
                "C": "DevOps pipeline actions are unrelated to Sentinel incident handling.",
                "D": "Storage file actions are not how a playbook updates a Sentinel incident.",
            },
            "exam_pattern": "Playbook ↔ incident = Sentinel connector actions (get entities, add comment, update incident).",
        },
        "references": ["Microsoft Learn (SC-200): Microsoft Sentinel Logic Apps connector actions"],
    },
    {
        "id": "sc200-sent-r2-035", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_soar", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank (one word): In Microsoft Sentinel, a ______ is the automated, repeatable "
                "set of response actions (built on Azure Logic Apps) that you attach to an alert, incident, or "
                "entity to carry out SOAR response.",
        "correct": ["playbook"],
        "explanation": {
            "correct": "A playbook is the Logic Apps-based response workflow; automation rules decide when and "
                       "which playbooks run as part of Sentinel's SOAR capabilities.",
            "distractors": {},
            "exam_pattern": "Logic Apps response workflow = playbook; the orchestration layer = automation rule.",
        },
        "references": ["Microsoft Learn (SC-200): Automate threat response with playbooks in Microsoft Sentinel"],
    },

    # ----- sc200_sentinel_incidents ---------------------------------------
    {
        "id": "sc200-sent-r2-036", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "A threat hunter wants to proactively search for suspicious patterns BEFORE any alert "
                "fires, using a library of queries organized by MITRE ATT&CK tactic. Which Microsoft Sentinel "
                "capability is designed for this?",
        "options": [
            {"id": "A", "text": "Hunting queries (the Hunting page)"},
            {"id": "B", "text": "Automation rules"},
            {"id": "C", "text": "Data connectors"},
            {"id": "D", "text": "Watchlists"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Hunting page provides proactive, hypothesis-driven KQL hunting queries mapped to "
                       "MITRE ATT&CK tactics/techniques, letting analysts search for threats before alerts are generated.",
            "distractors": {
                "B": "Automation rules orchestrate incident response; they are not proactive hunting queries.",
                "C": "Data connectors ingest data; they do not provide hunting queries.",
                "D": "Watchlists are reference data used within queries, not the hunting capability itself.",
            },
            "exam_pattern": "Proactive, pre-alert searching by ATT&CK tactic = hunting queries (Hunting page).",
        },
        "references": ["Microsoft Learn (SC-200): Hunt for threats with Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-037", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 3, "type": "mcq",
        "stem": "While testing a hunting hypothesis, an analyst wants to watch a query against incoming data "
                "in real time and be notified as new matches arrive. Which Microsoft Sentinel hunting feature provides this?",
        "options": [
            {"id": "A", "text": "Livestream"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A workbook"},
            {"id": "D", "text": "A playbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Livestream runs a hunting query against live, incoming data and notifies the analyst of "
                       "new matches in near real time - useful to test a detection idea or watch an active threat.",
            "distractors": {
                "B": "Watchlists are static reference datasets, not live query sessions.",
                "C": "Workbooks visualize stored data; they are not live hunting sessions.",
                "D": "Playbooks automate response; they do not stream query results for hunting.",
            },
            "exam_pattern": "Watch a hunting query against live data = livestream.",
        },
        "references": ["Microsoft Learn (SC-200): Use hunting livestream in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-038", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "During hunting, an analyst finds notable rows worth preserving and escalating. They "
                "bookmark the results. What can be done with a Microsoft Sentinel hunting bookmark?",
        "options": [
            {"id": "A", "text": "Promote it to a new incident or add it to an existing incident as evidence"},
            {"id": "B", "text": "It only changes the chart color"},
            {"id": "C", "text": "It deletes the underlying data"},
            {"id": "D", "text": "It disables the connector"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Bookmarks preserve notable query findings (with their entities and context) and can be "
                       "promoted to a new incident or attached to an existing incident as evidence for investigation.",
            "distractors": {
                "B": "A bookmark saves findings; it is not a chart styling option.",
                "C": "Bookmarks preserve data references; they do not delete data.",
                "D": "Bookmarks are unrelated to connector state.",
            },
            "exam_pattern": "Save hunting findings as evidence -> create/add to an incident = bookmarks.",
        },
        "references": ["Microsoft Learn (SC-200): Keep track of data with hunting bookmarks"],
    },
    {
        "id": "sc200-sent-r2-039", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "A data-science-savvy analyst needs to run advanced, multi-step investigations - combining "
                "KQL results with Python, machine learning, and rich visualizations - over Microsoft Sentinel "
                "data. Which capability supports this?",
        "options": [
            {"id": "A", "text": "Notebooks (Jupyter notebooks, e.g., via Azure Machine Learning)"},
            {"id": "B", "text": "Watchlists"},
            {"id": "C", "text": "Automation rules"},
            {"id": "D", "text": "Data connectors"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Sentinel notebooks (Jupyter, often hosted in Azure Machine Learning) enable "
                       "advanced hunting/investigation with Python, ML, and custom visualizations beyond what KQL alone offers.",
            "distractors": {
                "B": "Watchlists are reference data, not an analysis notebook environment.",
                "C": "Automation rules orchestrate response; they are not interactive analysis notebooks.",
                "D": "Data connectors ingest data; they are not an investigation notebook tool.",
            },
            "exam_pattern": "Python/ML/advanced multi-step investigation over Sentinel data = notebooks (Jupyter/Azure ML).",
        },
        "references": ["Microsoft Learn (SC-200): Use Jupyter notebooks to hunt in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-040", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 1, "type": "mcq",
        "stem": "A SOC manager wants an interactive dashboard that visualizes sign-in trends and incident "
                "volumes from the Microsoft Sentinel workspace, with charts and filters. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Workbooks"},
            {"id": "B", "text": "Playbooks"},
            {"id": "C", "text": "Watchlists"},
            {"id": "D", "text": "Automation rules"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Workbooks provide interactive, customizable dashboards and visualizations over "
                       "workspace data (built on Azure Monitor workbooks), with charts, grids, and filters.",
            "distractors": {
                "B": "Playbooks automate response actions; they do not build dashboards.",
                "C": "Watchlists are reference datasets, not visualizations.",
                "D": "Automation rules orchestrate incidents; they do not visualize data.",
            },
            "exam_pattern": "Interactive dashboards/visualization in Sentinel = workbooks.",
        },
        "references": ["Microsoft Learn (SC-200): Visualize data with workbooks in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-041", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 3, "type": "mcq",
        "stem": "A SOC maintains a very large reference list of allowed IP ranges and wants analytics rules "
                "and hunting queries to join against it efficiently. Which Microsoft Sentinel feature and access "
                "method fits?",
        "options": [
            {"id": "A", "text": "A watchlist, referenced in KQL via the _GetWatchlist('name') function (large watchlists can be backed by Azure Storage)"},
            {"id": "B", "text": "A workbook referenced by _GetWorkbook()"},
            {"id": "C", "text": "A playbook referenced inline in KQL"},
            {"id": "D", "text": "A data connector queried with join kind=anti"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Watchlists hold reference data and are queried in KQL with _GetWatchlist('name'); large "
                       "watchlists can be backed by Azure Storage for scale, so rules/hunts can join against them.",
            "distractors": {
                "B": "There is no _GetWorkbook() reference function; workbooks visualize data, they aren't joined in KQL.",
                "C": "Playbooks are response workflows; they are not referenced inline in KQL.",
                "D": "A data connector ingests data; the reference-list pattern uses a watchlist, not a connector.",
            },
            "exam_pattern": "Join rules/hunts against a reference list = watchlist via _GetWatchlist() (large = Azure Storage-backed).",
        },
        "references": ["Microsoft Learn (SC-200): Build queries with watchlists and the _GetWatchlist function"],
    },
    {
        "id": "sc200-sent-r2-042", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 3, "type": "mcq",
        "stem": "After enabling UEBA in Microsoft Sentinel, which table should analysts query to hunt on "
                "behavioral anomalies and the per-entity investigation priority scores it produces?",
        "options": [
            {"id": "A", "text": "BehaviorAnalytics"},
            {"id": "B", "text": "CommonSecurityLog"},
            {"id": "C", "text": "Heartbeat"},
            {"id": "D", "text": "AzureActivity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "UEBA enriches activity into the BehaviorAnalytics table, including behavioral context "
                       "and investigation-priority scoring that analysts can hunt and build detections on.",
            "distractors": {
                "B": "CommonSecurityLog holds CEF appliance data, not UEBA output.",
                "C": "Heartbeat tracks agent connectivity, not user/entity behavior analytics.",
                "D": "AzureActivity records Azure control-plane operations, not UEBA scores.",
            },
            "exam_pattern": "UEBA output for hunting = BehaviorAnalytics table (with investigation priority).",
        },
        "references": ["Microsoft Learn (SC-200): Hunt with UEBA and the BehaviorAnalytics table"],
    },
    {
        "id": "sc200-sent-r2-043", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "mcq",
        "stem": "Investigating a suspicious account, an analyst wants a consolidated timeline of that user's "
                "activity, alerts, and enrichment in one place. Which Microsoft Sentinel capability provides this per-entity view?",
        "options": [
            {"id": "A", "text": "The entity page (entity behavior)"},
            {"id": "B", "text": "The Content hub"},
            {"id": "C", "text": "A data collection rule"},
            {"id": "D", "text": "The Tenant Allow/Block List"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Entity pages present a consolidated view for a user, host, or IP - a timeline of "
                       "activities, related alerts, and enrichment/insights - to speed investigation.",
            "distractors": {
                "B": "The Content hub installs solutions; it is not a per-entity investigation view.",
                "C": "A data collection rule governs ingestion, not entity investigation.",
                "D": "The Tenant Allow/Block List is a Defender for Office 365 feature, unrelated to Sentinel entity pages.",
            },
            "exam_pattern": "Consolidated per-entity timeline/insights = entity page.",
        },
        "references": ["Microsoft Learn (SC-200): Investigate entities with entity pages in Microsoft Sentinel"],
    },
    {
        "id": "sc200-sent-r2-044", "exam": "sc200", "domain": "sc200_sentinel",
        "subtopic": "sc200_sentinel_incidents", "difficulty": 2, "type": "multi",
        "stem": "Which TWO Microsoft Sentinel capabilities are intended for PROACTIVE threat hunting (before "
                "an alert or incident exists)? (Choose two.)",
        "options": [
            {"id": "A", "text": "Hunting queries (Hunting page)"},
            {"id": "B", "text": "Livestream"},
            {"id": "C", "text": "Automation rules"},
            {"id": "D", "text": "Quarantine policies"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Hunting queries and livestream are proactive hunting tools - searching for and "
                       "watching suspicious activity before alerts fire.",
            "distractors": {
                "C": "Automation rules react to incidents/alerts that already exist; they are not proactive hunting.",
                "D": "Quarantine policies are a Defender for Office 365 construct, not a Sentinel hunting tool.",
            },
            "exam_pattern": "Proactive hunting = hunting queries + livestream (bookmarks/notebooks support it too).",
        },
        "references": ["Microsoft Learn (SC-200): Proactive threat hunting tools in Microsoft Sentinel"],
    },

    # =====================================================================
    # DOMAIN 4 - Threat Hunting and Intelligence (KQL) (15%)
    # =====================================================================

    # ----- sc200_kql ------------------------------------------------------
    {
        "id": "sc200-hunt-r2-001", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 3, "type": "mcq",
        "stem": "A hunter wants, for each device, the single MOST RECENT sign-in row - keeping other "
                "columns from that row (not just the max timestamp). Which KQL aggregation function fits inside summarize?",
        "options": [
            {"id": "A", "text": "arg_max(Timestamp, *) by DeviceName"},
            {"id": "B", "text": "max(Timestamp) by DeviceName"},
            {"id": "C", "text": "count() by DeviceName"},
            {"id": "D", "text": "make_list(Timestamp) by DeviceName"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "arg_max(Timestamp, *) returns the row that has the maximum Timestamp per group and "
                       "keeps the other columns (the '*'), giving the latest full record per device.",
            "distractors": {
                "B": "max(Timestamp) returns only the maximum timestamp value, not the other columns of that row.",
                "C": "count() returns how many rows, not the latest row.",
                "D": "make_list() collects all values into an array; it does not pick the latest row.",
            },
            "exam_pattern": "Latest full row per group = arg_max(Timestamp, *); just the max value = max().",
        },
        "references": ["Microsoft Learn (SC-200): KQL aggregation - arg_max()"],
    },
    {
        "id": "sc200-hunt-r2-002", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 3, "type": "mcq",
        "stem": "A column contains a dynamic array of file hashes per event. A hunter wants one output row "
                "per individual hash so they can group/count by hash. Which KQL operator expands the array into rows?",
        "options": [
            {"id": "A", "text": "mv-expand"},
            {"id": "B", "text": "make_list"},
            {"id": "C", "text": "summarize"},
            {"id": "D", "text": "project-away"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "mv-expand expands each element of a dynamic array (or property bag) into its own row - "
                       "the inverse of summarize make_list() - so each hash becomes a separate record.",
            "distractors": {
                "B": "make_list does the opposite: it collects values into one array.",
                "C": "summarize aggregates rows; it does not expand an array into rows.",
                "D": "project-away removes columns; it does not expand arrays.",
            },
            "exam_pattern": "Array -> one row per element = mv-expand (inverse of make_list).",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the mv-expand operator"],
    },
    {
        "id": "sc200-hunt-r2-003", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "A hunter needs to pull structured fields (user, source IP) out of a free-text log message "
                "column into their own columns. Which KQL operator is designed to extract calculated columns from a string pattern?",
        "options": [
            {"id": "A", "text": "parse"},
            {"id": "B", "text": "summarize"},
            {"id": "C", "text": "sort"},
            {"id": "D", "text": "distinct"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "parse evaluates a string expression and produces one or more calculated columns from a "
                       "pattern (values are null where the pattern doesn't match; use parse-where to drop non-matching rows).",
            "distractors": {
                "B": "summarize aggregates rows; it does not extract fields from a string.",
                "C": "sort orders rows; it does not parse text into columns.",
                "D": "distinct returns unique combinations; it does not extract substrings into columns.",
            },
            "exam_pattern": "Extract fields from a text column = parse (parse-where to drop failures).",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the parse operator"],
    },
    {
        "id": "sc200-hunt-r2-004", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 2, "type": "mcq",
        "stem": "A hunter wants to define a reusable threshold value and a reusable subquery at the top of a "
                "KQL query, then reference them below. Which KQL statement does this?",
        "options": [
            {"id": "A", "text": "The let statement"},
            {"id": "B", "text": "The where operator"},
            {"id": "C", "text": "The render operator"},
            {"id": "D", "text": "The take operator"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "let binds a name to a scalar value, a list, or even a subquery/tabular expression, so "
                       "you can declare thresholds and reusable datasets once and reference them later in the query.",
            "distractors": {
                "B": "where filters rows; it does not declare reusable variables.",
                "C": "render selects a chart type for output.",
                "D": "take returns an arbitrary sample of rows; it does not define variables.",
            },
            "exam_pattern": "Declare reusable values/subqueries = let.",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the let statement"],
    },
    {
        "id": "sc200-hunt-r2-005", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank (one KQL function): To keep only events from the last 24 hours relative "
                "to now, a hunter writes `where Timestamp > ______(1d)`.",
        "correct": ["ago"],
        "explanation": {
            "correct": "ago(1d) returns the time 24 hours before now, so the predicate keeps events from the "
                       "last day; ago() is the standard relative-time function for filtering.",
            "distractors": {},
            "exam_pattern": "Relative time filter = ago(<timespan>); fixed window = between(..).",
        },
        "references": ["Microsoft Learn (SC-200): KQL - the ago() function"],
    },
    {
        "id": "sc200-hunt-r2-006", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_kql", "difficulty": 3, "type": "mcq",
        "stem": "A hunter needs accounts that appear in a sign-in table but have NO matching row in an "
                "alerts table (present in the left table, absent from the right). Which KQL join kind returns exactly these?",
        "options": [
            {"id": "A", "text": "join kind=leftanti"},
            {"id": "B", "text": "join kind=inner"},
            {"id": "C", "text": "join kind=fullouter"},
            {"id": "D", "text": "join kind=rightouter"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A leftanti join returns only the left-table rows that have no match in the right table "
                       "- exactly 'in A but not in B' - making it ideal for finding activity with no corresponding alert.",
            "distractors": {
                "B": "inner returns only matching rows (in both), the opposite of what's needed.",
                "C": "fullouter returns all rows from both sides, matched or not.",
                "D": "rightouter keeps all right-table rows; it does not isolate left-only rows.",
            },
            "exam_pattern": "'In A, not in B' = join kind=leftanti; 'in both' = inner.",
        },
        "references": ["Microsoft Learn (SC-200): KQL join flavors - leftanti and other kinds"],
    },

    # ----- sc200_advanced_hunting -----------------------------------------
    {
        "id": "sc200-hunt-r2-007", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "mcq",
        "stem": "To hunt for devices making outbound network connections to a suspected command-and-control "
                "IP address, which Microsoft Defender XDR advanced hunting table should be queried?",
        "options": [
            {"id": "A", "text": "DeviceNetworkEvents"},
            {"id": "B", "text": "DeviceFileEvents"},
            {"id": "C", "text": "EmailEvents"},
            {"id": "D", "text": "IdentityDirectoryEvents"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DeviceNetworkEvents records network connection telemetry from onboarded devices "
                       "(remote IPs/URLs, ports, process), ideal for hunting outbound connections to a C2 address.",
            "distractors": {
                "B": "DeviceFileEvents covers file create/modify/delete activity, not network connections.",
                "C": "EmailEvents covers email delivery, not device network connections.",
                "D": "IdentityDirectoryEvents covers on-prem AD/identity activity, not device network traffic.",
            },
            "exam_pattern": "Device outbound connections / C2 hunting = DeviceNetworkEvents.",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting schema - DeviceNetworkEvents"],
    },
    {
        "id": "sc200-hunt-r2-008", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 3, "type": "mcq",
        "stem": "A hunter wants authentication/logon activity captured by Microsoft Defender for Identity "
                "(on-premises AD and related sign-ins) within the Defender XDR advanced hunting schema. Which "
                "table is most appropriate?",
        "options": [
            {"id": "A", "text": "IdentityLogonEvents"},
            {"id": "B", "text": "DeviceProcessEvents"},
            {"id": "C", "text": "CloudAppEvents"},
            {"id": "D", "text": "AlertInfo"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IdentityLogonEvents contains logon/authentication events from identity providers "
                       "monitored by Defender for Identity (and related sources), supporting identity-centric hunting.",
            "distractors": {
                "B": "DeviceProcessEvents holds process creation on endpoints, not identity logons.",
                "C": "CloudAppEvents holds Defender for Cloud Apps activities, not AD logon events.",
                "D": "AlertInfo lists alerts, not raw identity logon telemetry.",
            },
            "exam_pattern": "Identity logon/auth telemetry (MDI) = IdentityLogonEvents; AD object changes = IdentityDirectoryEvents.",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting schema - IdentityLogonEvents"],
    },
    {
        "id": "sc200-hunt-r2-009", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "mcq",
        "stem": "To hunt across activities in SaaS apps monitored by Microsoft Defender for Cloud Apps "
                "(for example, mass file downloads or risky OAuth activity) using advanced hunting, which table holds these events?",
        "options": [
            {"id": "A", "text": "CloudAppEvents"},
            {"id": "B", "text": "DeviceRegistryEvents"},
            {"id": "C", "text": "EmailAttachmentInfo"},
            {"id": "D", "text": "DeviceImageLoadEvents"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CloudAppEvents contains activities from apps monitored by Defender for Cloud Apps, so "
                       "hunters can query cloud-app user actions across connected SaaS services.",
            "distractors": {
                "B": "DeviceRegistryEvents covers endpoint registry changes, not cloud-app activity.",
                "C": "EmailAttachmentInfo covers email attachments, not SaaS app activity.",
                "D": "DeviceImageLoadEvents covers DLL/image loads on endpoints, not cloud apps.",
            },
            "exam_pattern": "SaaS app activity hunting = CloudAppEvents (Defender for Cloud Apps).",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting schema - CloudAppEvents"],
    },
    {
        "id": "sc200-hunt-r2-010", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 2, "type": "mcq",
        "stem": "A hunter wants details about the FILE ATTACHMENTS carried by emails (such as file name and "
                "hash) to pivot on a malicious attachment across the tenant. Which advanced hunting table is most directly relevant?",
        "options": [
            {"id": "A", "text": "EmailAttachmentInfo"},
            {"id": "B", "text": "UrlClickEvents"},
            {"id": "C", "text": "DeviceLogonEvents"},
            {"id": "D", "text": "AzureActivity"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "EmailAttachmentInfo contains information about files attached to emails (name, hashes, "
                       "malware verdict), letting hunters trace a malicious attachment; join with EmailEvents for delivery context.",
            "distractors": {
                "B": "UrlClickEvents records Safe Links URL clicks, not attachment file details.",
                "C": "DeviceLogonEvents covers endpoint logons, not email attachments.",
                "D": "AzureActivity records Azure control-plane operations, not email attachments.",
            },
            "exam_pattern": "Email attachment file details = EmailAttachmentInfo; URLs in email = EmailUrlInfo; clicks = UrlClickEvents.",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting schema - EmailAttachmentInfo"],
    },
    {
        "id": "sc200-hunt-r2-011", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_advanced_hunting", "difficulty": 3, "type": "mcq",
        "stem": "In the unified Microsoft Defender portal, a hunter writes an advanced hunting query that "
                "returns both Microsoft Sentinel-sourced rows and Defender XDR device rows. For which results can "
                "they use the built-in 'take actions' (response) capability directly from the query output?",
        "options": [
            {"id": "A", "text": "Only for Microsoft Defender XDR data (take actions is supported on Defender data, not Sentinel-only results)"},
            {"id": "B", "text": "For all rows equally, including Sentinel-only rows"},
            {"id": "C", "text": "For neither - response actions are never available from hunting"},
            {"id": "D", "text": "Only for Microsoft Sentinel data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In unified advanced hunting, the guided mode and 'take actions' response capabilities "
                       "support Microsoft Defender XDR data only; you can query Sentinel tables alongside Defender "
                       "data, but direct response actions apply to Defender results.",
            "distractors": {
                "B": "Take actions does not apply to Sentinel-only results; it is a known Defender-data limitation.",
                "C": "Response actions ARE available from hunting - for Defender XDR data.",
                "D": "It is the reverse: take actions is for Defender data, not Sentinel-only data.",
            },
            "exam_pattern": "Unified hunting 'take actions' = Defender XDR data only (Sentinel tables are queryable but not actionable there).",
        },
        "references": ["Microsoft Learn (SC-200): Advanced hunting with Microsoft Sentinel data in the Defender portal"],
    },

    # ----- sc200_custom_detections ----------------------------------------
    {
        "id": "sc200-hunt-r2-012", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 2, "type": "mcq",
        "stem": "When creating a Microsoft Defender XDR custom detection rule, why must the query's results "
                "map impacted entities (such as DeviceId, AccountObjectId, or the recipient mailbox)?",
        "options": [
            {"id": "A", "text": "So the generated alerts are tied to the right assets and response actions can target those entities"},
            {"id": "B", "text": "So the rule runs faster"},
            {"id": "C", "text": "So the data is exported to storage"},
            {"id": "D", "text": "So the workspace retention increases"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Mapping impacted entities lets Defender XDR associate alerts with the correct devices/"
                       "users/mailboxes and apply response actions (isolate device, disable user, etc.) to those entities.",
            "distractors": {
                "B": "Entity mapping is about targeting alerts/actions, not query speed.",
                "C": "It does not export data to storage.",
                "D": "It does not change retention.",
            },
            "exam_pattern": "Custom detection must map impacted entities so alerts/actions hit the right assets.",
        },
        "references": ["Microsoft Learn (SC-200): Map impacted entities in custom detection rules"],
    },
    {
        "id": "sc200-hunt-r2-013", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_custom_detections", "difficulty": 3, "type": "mcq",
        "stem": "A SOC builds a custom detection rule whose query includes a Microsoft Sentinel table (in "
                "the unified portal). Which constraint applies to this rule?",
        "options": [
            {"id": "A", "text": "Near-real-time (continuous) frequency isn't available, and the Sentinel data must be in the Analytics tier"},
            {"id": "B", "text": "It must run only once per week"},
            {"id": "C", "text": "It cannot generate alerts at all"},
            {"id": "D", "text": "It requires the device to be isolated first"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "When a custom detection includes Microsoft Sentinel data, the near-real-time frequency "
                       "isn't offered, and the Sentinel tables must be Analytics-tier (not Basic/Auxiliary) for the rule to be created.",
            "distractors": {
                "B": "There is no fixed weekly-only requirement; periodic frequencies apply.",
                "C": "The rule still generates alerts; the constraint is on frequency and data tier.",
                "D": "Device isolation is a response action, not a creation constraint.",
            },
            "exam_pattern": "Custom detection with Sentinel data = no NRT frequency + Analytics-tier tables required.",
        },
        "references": ["Microsoft Learn (SC-200): Custom detections that include Microsoft Sentinel data"],
    },

    # ----- sc200_threat_intel ---------------------------------------------
    {
        "id": "sc200-hunt-r2-014", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "A SOC wants Microsoft Sentinel to automatically generate alerts when Microsoft-generated "
                "threat intelligence indicators match events in their logs (for example, a known-malicious IP "
                "seen in network data). Which analytics capability does this?",
        "options": [
            {"id": "A", "text": "The Microsoft Threat Intelligence matching analytics rule"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A workbook"},
            {"id": "D", "text": "An anomaly rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Threat Intelligence (matching) analytics rule correlates Microsoft's "
                       "threat intelligence indicators against your ingested logs and raises alerts on matches.",
            "distractors": {
                "B": "A watchlist is static reference data; it does not itself match TI and generate alerts.",
                "C": "A workbook visualizes data; it does not generate TI-match alerts.",
                "D": "An anomaly rule flags behavioral outliers via ML, not indicator matching.",
            },
            "exam_pattern": "Auto-alert on Microsoft TI indicator matches in your logs = TI matching analytics rule.",
        },
        "references": ["Microsoft Learn (SC-200): Use matching analytics to detect threats with threat intelligence"],
    },
    {
        "id": "sc200-hunt-r2-015", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 3, "type": "mcq",
        "stem": "In Microsoft Sentinel's threat intelligence, in what standardized format are indicators "
                "(and related objects) represented, including when adding an indicator manually with a validity "
                "period and confidence?",
        "options": [
            {"id": "A", "text": "STIX objects"},
            {"id": "B", "text": "YAML playbooks"},
            {"id": "C", "text": "Bicep templates"},
            {"id": "D", "text": "CSV watchlists"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel represents threat intelligence as STIX objects (indicators and other STIX "
                       "object types), and the threat intelligence management interface lets you add/curate indicators (with validity, confidence, tags) in that model.",
            "distractors": {
                "B": "YAML is used for some content definitions, not the TI indicator object model.",
                "C": "Bicep is for infrastructure-as-code deployments, not TI indicators.",
                "D": "A CSV watchlist is generic reference data, not the STIX TI object standard.",
            },
            "exam_pattern": "Sentinel threat intelligence objects = STIX (indicators, etc.).",
        },
        "references": ["Microsoft Learn (SC-200): Work with threat intelligence (STIX objects) in Microsoft Sentinel"],
    },
    {
        "id": "sc200-hunt-r2-016", "exam": "sc200", "domain": "sc200_hunting_intel",
        "subtopic": "sc200_threat_intel", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender for Endpoint, custom indicators (IoCs) can be assigned a response "
                "action and scoped to device groups. Which of the following is NOT a valid Defender for Endpoint "
                "indicator action?",
        "options": [
            {"id": "A", "text": "Quarantine the user's mailbox"},
            {"id": "B", "text": "Block (or Block and remediate)"},
            {"id": "C", "text": "Allow"},
            {"id": "D", "text": "Warn / Audit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Endpoint indicator actions include Allow, Audit, Warn, Block, and Block "
                       "and remediate (scopable to device groups). Quarantining a mailbox is a Defender for Office "
                       "365 action, not an endpoint indicator action.",
            "distractors": {
                "B": "Block / Block and remediate are valid endpoint indicator actions.",
                "C": "Allow is a valid indicator action (explicitly permit a known-good IoC).",
                "D": "Warn and Audit are valid indicator actions.",
            },
            "exam_pattern": "MDE indicator actions = Allow / Audit / Warn / Block / Block-and-remediate (scoped to device groups).",
        },
        "references": ["Microsoft Learn (SC-200): Create indicators and response actions in Defender for Endpoint"],
    },
]
