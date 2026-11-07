"""Security+ SY0-701 expansion pool — Domain 2.0 Threats, Vulnerabilities & Mitigations.

Original, objective-aligned items that DEEPEN the base `threats_vulns_mitigations`
pool in content_secplus.py (which already covers nation-state APTs, help-desk
pretexting, ransomware, SQL injection, an IoT DDoS, and the zero-day/compensating-
control pattern). These add new angles across all eight subtopics — threat_actors,
threat_vectors, social_engineering, vulnerability_types, malware, network_attacks,
application_attacks, mitigation_techniques — never real exam items.

build_content.py auto-discovers this file (content_secplus_*.py), shuffles each
item's A/B/C/D order seeded by id, and re-keys the answer, so the key below is not
positionally biased.
"""

QUESTIONS = [
    # ===== threat_actors ====================================================
    {
        "id": "secplus-tvm-101", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_actors", "difficulty": 2, "type": "mcq",
        "stem": "A criminal syndicate runs a ransomware-as-a-service operation, renting its "
                "malware to affiliates and splitting the extortion profits. Which threat actor "
                "type and primary motivation does this describe?",
        "options": [
            {"id": "A", "text": "Organized crime — financial gain"},
            {"id": "B", "text": "Nation-state — espionage"},
            {"id": "C", "text": "Hacktivist — ideology"},
            {"id": "D", "text": "Unskilled attacker — curiosity/notoriety"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Profit-driven, structured criminal groups that run RaaS businesses to "
                       "extort money are organized crime; their defining motivation is financial gain.",
            "distractors": {
                "B": "Nation-state actors are government-sponsored and motivated by espionage or "
                     "strategic advantage, not renting malware for revenue.",
                "C": "Hacktivists act on a political/social cause and seek publicity, not subscription profit.",
                "D": "An unskilled attacker lacks the resources and organization to run a RaaS business.",
            },
            "exam_pattern": "RaaS / extortion for money / a 'business' = organized crime (financial). "
                            "Match the actor to its motivation.",
        },
    },
    {
        "id": "secplus-tvm-102", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_actors", "difficulty": 2, "type": "mcq",
        "stem": "A systems administrator who was just told they are being terminated copies the "
                "customer database to a personal cloud account before their access is revoked. "
                "Which threat actor BEST fits, and what makes this actor especially dangerous?",
        "options": [
            {"id": "A", "text": "Insider threat — already holds authorized access and knows where valuable data resides"},
            {"id": "B", "text": "Nation-state — virtually unlimited funding"},
            {"id": "C", "text": "Unskilled attacker — relies on prebuilt tools"},
            {"id": "D", "text": "Shadow IT — deploys unsanctioned systems"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An insider threat is a current or former employee/contractor who misuses "
                       "legitimate access; the danger is that they already have authorized access and "
                       "know exactly where the valuable data is, bypassing perimeter defenses.",
            "distractors": {
                "B": "Funding is the hallmark of nation-states, but this is an internal employee abusing "
                     "access, not an externally funded operation.",
                "C": "An unskilled attacker is an external, low-skill actor using others' tools — not a trusted admin.",
                "D": "Shadow IT is unsanctioned technology adopted without approval; here the admin is "
                     "exfiltrating data, not deploying rogue systems.",
            },
            "exam_pattern": "Trusted/authorized access from inside = insider threat; their edge is "
                            "legitimate access + knowledge, not money or tools.",
        },
    },
    {
        "id": "secplus-tvm-103", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_actors", "difficulty": 1, "type": "mcq",
        "stem": "A loosely organized group defaces a corporation's website and leaks internal "
                "emails to protest the company's environmental record, posting a political "
                "manifesto alongside the leak. Which threat actor is this?",
        "options": [
            {"id": "A", "text": "Hacktivist"},
            {"id": "B", "text": "Organized crime"},
            {"id": "C", "text": "Nation-state (APT)"},
            {"id": "D", "text": "Insider threat"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Attacks driven by a political/social cause and aimed at publicity — defacement, "
                       "doxxing, manifestos — are the signature of hacktivists; the motivation is ideological.",
            "distractors": {
                "B": "Organized crime is profit-driven; leaking emails for a cause yields no financial return.",
                "C": "Nation-states favor long-term stealth and espionage, not loud public protest.",
                "D": "An insider threat acts from within using authorized access; this is an external ideological group.",
            },
            "exam_pattern": "Ideology + publicity (defacement/leaks/manifesto) for a cause = hacktivist.",
        },
    },
    {
        "id": "secplus-tvm-104", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_actors", "difficulty": 2, "type": "mcq",
        "stem": "A teenager downloads a point-and-click DDoS tool and launches it against a game "
                "server without understanding how it works. Which description of this threat "
                "actor's ATTRIBUTES is MOST accurate?",
        "options": [
            {"id": "A", "text": "External actor with low sophistication and few resources"},
            {"id": "B", "text": "Internal actor with high sophistication and large resources"},
            {"id": "C", "text": "External actor, government-sponsored, with advanced capabilities"},
            {"id": "D", "text": "Internal actor with authorized administrative access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An unskilled attacker (script kiddie) is external, low in skill/sophistication, "
                       "and has minimal resources, relying on tools others built.",
            "distractors": {
                "B": "High sophistication and large resources describe APTs or organized crime, not a script kiddie.",
                "C": "Government sponsorship and advanced capability describe a nation-state actor.",
                "D": "Authorized internal access describes an insider threat, not an external hobbyist.",
            },
            "exam_pattern": "Score actors on internal/external, resources, and sophistication: "
                            "unskilled attacker = external, low, low.",
        },
    },

    # ===== threat_vectors ===================================================
    {
        "id": "secplus-tvm-105", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_vectors", "difficulty": 2, "type": "mcq",
        "stem": "An attacker scatters USB flash drives labeled 'Executive Salaries' in the company "
                "parking lot, hoping an employee plugs one into a workstation. Which threat vector "
                "is being exploited?",
        "options": [
            {"id": "A", "text": "Removable device"},
            {"id": "B", "text": "Watering-hole site"},
            {"id": "C", "text": "Open service port"},
            {"id": "D", "text": "Default credentials"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Seeding malicious USB media for a victim to insert exploits the removable-device "
                       "vector (and human curiosity); it rides on hardware the user physically connects.",
            "distractors": {
                "B": "A watering hole compromises a website the target group already visits — no physical media.",
                "C": "An open service port is a listening network service, unrelated to dropped USB media.",
                "D": "Default credentials are unchanged factory passwords, not a planted USB drive.",
            },
            "exam_pattern": "Dropped/rogue USB left to be found = removable-device vector (often paired with 'baiting').",
        },
    },
    {
        "id": "secplus-tvm-106", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_vectors", "difficulty": 1, "type": "mcq",
        "stem": "A company deploys dozens of IP cameras but never changes the vendor's built-in "
                "'admin/admin' login, and an attacker on the internet logs straight in. Which "
                "threat vector did the attacker use, and the correct fix?",
        "options": [
            {"id": "A", "text": "Default credentials — change them during provisioning"},
            {"id": "B", "text": "Zero-day — wait for a vendor patch"},
            {"id": "C", "text": "Supply-chain compromise — audit the vendor's source code"},
            {"id": "D", "text": "VM escape — isolate the hypervisor"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Leaving factory default usernames/passwords in place is the default-credentials "
                       "vector; the fix is changing defaults (and disabling default accounts) during secure provisioning.",
            "distractors": {
                "B": "A zero-day is an unknown, unpatched flaw — not a known factory password the admin failed to change.",
                "C": "Supply-chain compromise taints the product before delivery; here the product is fine but was misconfigured.",
                "D": "VM escape is a virtualization attack breaking out of a guest — irrelevant to a camera login.",
            },
            "exam_pattern": "Unchanged factory password = default-credentials vector → change defaults at deployment.",
        },
    },
    {
        "id": "secplus-tvm-107", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_vectors", "difficulty": 3, "type": "mcq",
        "stem": "An attacker compromises a managed service provider (MSP) that holds remote "
                "administrative access into hundreds of client networks, then pivots into those "
                "clients. Which threat vector does this BEST illustrate?",
        "options": [
            {"id": "A", "text": "Supply-chain (third-party/MSP) vector"},
            {"id": "B", "text": "Watering-hole attack"},
            {"id": "C", "text": "On-path attack"},
            {"id": "D", "text": "Directory traversal"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Abusing a trusted third party — MSP, vendor, or supplier — that has privileged "
                       "access in order to reach downstream victims is the supply-chain vector; the provider's "
                       "broad trust multiplies the blast radius.",
            "distractors": {
                "B": "A watering hole lures victims to a booby-trapped website; here the attacker rides an existing trusted channel.",
                "C": "An on-path attack intercepts traffic between two parties, not a trust-relationship pivot through a provider.",
                "D": "Directory traversal is a web-application file-access flaw, unrelated to third-party trust.",
            },
            "exam_pattern": "Trusted vendor/MSP/supplier abused to reach its customers = supply-chain vector.",
        },
    },
    {
        "id": "secplus-tvm-108", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "threat_vectors", "difficulty": 2, "type": "multi",
        "stem": "A security team wants to shrink an internet-facing server's attack surface. Which "
                "TWO conditions should they treat as exposures to REMOVE? (Choose two.)",
        "options": [
            {"id": "A", "text": "Unnecessary open service ports listening to the internet"},
            {"id": "B", "text": "An unsupported, end-of-life operating system"},
            {"id": "C", "text": "Full-disk encryption enabled on the server"},
            {"id": "D", "text": "Multifactor authentication required for administrators"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Every reachable listening service (open port) and every unsupported/EOL system "
                       "(no security patches) enlarges the attack surface and should be closed or replaced.",
            "distractors": {
                "C": "Full-disk encryption protects data at rest and REDUCES risk — it is not an exposure to remove.",
                "D": "Requiring MFA strengthens access control; it shrinks risk rather than expanding the attack surface.",
            },
            "exam_pattern": "Attack surface grows with open ports, unused services, EOL/unpatched software, and "
                            "default accounts — not with added security controls.",
        },
    },

    # ===== social_engineering ===============================================
    {
        "id": "secplus-tvm-109", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 1, "type": "mcq",
        "stem": "Employees receive a TEXT MESSAGE claiming to be from the bank's fraud department, "
                "with a link to 'verify your account.' What is this attack called?",
        "options": [
            {"id": "A", "text": "Smishing"},
            {"id": "B", "text": "Vishing"},
            {"id": "C", "text": "Whaling"},
            {"id": "D", "text": "Pharming"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Phishing delivered by SMS/text message is smishing.",
            "distractors": {
                "B": "Vishing is voice/phone-call phishing, not text.",
                "C": "Whaling is phishing that specifically targets senior executives; the medium isn't the defining trait, and no exec is targeted here.",
                "D": "Pharming redirects victims via poisoned DNS/hosts to a fake site without sending a lure message.",
            },
            "exam_pattern": "Channel names the attack: email = phishing, voice = vishing, SMS/text = smishing.",
        },
    },
    {
        "id": "secplus-tvm-110", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 3, "type": "mcq",
        "stem": "An accounts-payable clerk receives an email that appears to come from the CEO's "
                "address, urgently instructing them to change a vendor's bank account and wire a "
                "payment. No malware or link is involved. Which term BEST describes this attack?",
        "options": [
            {"id": "A", "text": "Business email compromise (BEC)"},
            {"id": "B", "text": "Whaling"},
            {"id": "C", "text": "Credential replay"},
            {"id": "D", "text": "Typosquatting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Impersonating a trusted executive by email to trick staff into a fraudulent "
                       "transfer — no payload, relying on authority and urgency — is business email compromise.",
            "distractors": {
                "B": "Whaling targets the executive as the VICTIM; here the exec is impersonated to victimize a subordinate, which is BEC.",
                "C": "Credential replay reuses captured authentication material; no credentials are replayed here.",
                "D": "Typosquatting registers look-alike domains to catch mistyped URLs — not an impersonated internal email.",
            },
            "exam_pattern": "Spoofed-exec email telling staff to pay/wire = BEC. The exec as the target = whaling.",
        },
    },
    {
        "id": "secplus-tvm-111", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 2, "type": "mcq",
        "stem": "An attacker registers 'paypa1.com' and 'gooogle.com' so that users who mistype the "
                "real address land on a malicious look-alike page. What is this technique called?",
        "options": [
            {"id": "A", "text": "Typosquatting (URL hijacking)"},
            {"id": "B", "text": "Pharming"},
            {"id": "C", "text": "Watering-hole attack"},
            {"id": "D", "text": "On-path attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Registering misspelled or look-alike domains to catch users who mistype a URL is "
                       "typosquatting (URL hijacking).",
            "distractors": {
                "B": "Pharming sends a correctly-typed request to a fake site by poisoning DNS or the hosts file — the user doesn't mistype.",
                "C": "A watering hole compromises a legitimate site the target already visits, not a misspelled domain.",
                "D": "An on-path attack intercepts traffic in transit; typosquatting relies on the user's typo, with no interception.",
            },
            "exam_pattern": "Misspelled look-alike domain registered for typos = typosquatting; DNS redirect of "
                            "the correct name = pharming.",
        },
    },
    {
        "id": "secplus-tvm-112", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "social_engineering", "difficulty": 1, "type": "mcq",
        "stem": "An unauthorized person carrying a coffee and a stack of boxes slips through a "
                "badge-controlled door right behind an employee who holds it open. Which technique "
                "is this, and the BEST control?",
        "options": [
            {"id": "A", "text": "Tailgating — deploy an access-control vestibule (mantrap)"},
            {"id": "B", "text": "Shoulder surfing — apply a privacy screen"},
            {"id": "C", "text": "Dumpster diving — shred documents"},
            {"id": "D", "text": "Pretexting — enforce callback verification"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Following an authorized person through a secure door without presenting credentials "
                       "is tailgating/piggybacking; an access-control vestibule (mantrap) physically stops a second person slipping through.",
            "distractors": {
                "B": "Shoulder surfing is observing someone's screen or keypad; a privacy filter addresses that, not door entry.",
                "C": "Dumpster diving recovers sensitive material from trash; shredding counters it, but no trash is involved here.",
                "D": "Pretexting invents a false scenario in conversation; the attacker here says nothing, they just follow.",
            },
            "exam_pattern": "Following someone through a secure door = tailgating → access-control vestibule/mantrap.",
        },
    },

    # ===== vulnerability_types ==============================================
    {
        "id": "secplus-tvm-113", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "vulnerability_types", "difficulty": 3, "type": "mcq",
        "stem": "A C program copies attacker-supplied input into a fixed-size stack buffer without "
                "checking its length, letting the attacker overwrite the saved return address and "
                "redirect execution. Which vulnerability class is this?",
        "options": [
            {"id": "A", "text": "Buffer overflow"},
            {"id": "B", "text": "Race condition"},
            {"id": "C", "text": "Cross-site scripting"},
            {"id": "D", "text": "Resource reuse"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Writing past the bounds of a fixed-size buffer to overwrite adjacent memory "
                       "(such as the return address) is a buffer overflow; the fix is bounds checking, safe "
                       "functions, or memory-safe languages.",
            "distractors": {
                "B": "A race condition is a timing flaw between concurrent operations, not an out-of-bounds write.",
                "C": "XSS injects script into web pages viewed by others — a web-app flaw, not memory corruption.",
                "D": "Resource reuse is a virtualization issue where leftover data persists in reallocated memory/storage.",
            },
            "exam_pattern": "Input longer than the buffer + overwritten return address = buffer overflow (a memory-based vulnerability).",
        },
    },
    {
        "id": "secplus-tvm-114", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "vulnerability_types", "difficulty": 3, "type": "mcq",
        "stem": "A program checks that a user is authorized to open a file and then opens it a moment "
                "later. An attacker swaps the file for a symbolic link in the gap between the check "
                "and the open. Which vulnerability is being exploited?",
        "options": [
            {"id": "A", "text": "Race condition (time-of-check to time-of-use)"},
            {"id": "B", "text": "Buffer overflow"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Default-credential misuse"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Exploiting the timing window between validating a condition and acting on it is a "
                       "time-of-check to time-of-use (TOCTOU) race condition.",
            "distractors": {
                "B": "A buffer overflow overwrites memory beyond a buffer — no timing window is involved.",
                "C": "SQL injection manipulates database queries through input, unrelated to a check/use timing gap.",
                "D": "This is a timing flaw, not reuse of an unchanged factory password.",
            },
            "exam_pattern": "A gap between 'check' and 'use' that an attacker slips into = TOCTOU race condition.",
        },
    },
    {
        "id": "secplus-tvm-115", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "vulnerability_types", "difficulty": 3, "type": "mcq",
        "stem": "A penetration tester running code inside a guest virtual machine is able to break "
                "out and execute commands directly on the underlying hypervisor host. Which "
                "virtualization vulnerability does this demonstrate?",
        "options": [
            {"id": "A", "text": "VM escape"},
            {"id": "B", "text": "VLAN hopping"},
            {"id": "C", "text": "Resource exhaustion"},
            {"id": "D", "text": "Jailbreaking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Breaking out of a guest VM to reach the hypervisor/host is a VM escape — one of the "
                       "most serious virtualization flaws because it collapses guest isolation.",
            "distractors": {
                "B": "VLAN hopping crosses network VLAN boundaries, not the guest-to-host boundary.",
                "C": "Resource exhaustion denies availability by consuming CPU/RAM; it doesn't break isolation.",
                "D": "Jailbreaking removes vendor restrictions on a mobile device, not a hypervisor breakout.",
            },
            "exam_pattern": "Guest breaks out to the hypervisor/host = VM escape (a virtualization vulnerability).",
        },
    },
    {
        "id": "secplus-tvm-116", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "vulnerability_types", "difficulty": 2, "type": "mcq",
        "stem": "An industrial control system runs Windows Server 2008, which the vendor no longer "
                "issues security updates for, and it cannot be replaced soon. How is this "
                "vulnerability BEST classified, and what is the right interim response?",
        "options": [
            {"id": "A", "text": "End-of-life/legacy system — isolate it and apply compensating controls until replacement"},
            {"id": "B", "text": "Zero-day — report it to the vendor for a patch"},
            {"id": "C", "text": "Misconfiguration — reset the server to default settings"},
            {"id": "D", "text": "Cryptographic vulnerability — rotate the TLS certificate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Software past vendor support that no longer receives patches is an end-of-life/legacy "
                       "vulnerability; when immediate replacement isn't possible, segment/isolate it and wrap it in compensating controls.",
            "distractors": {
                "B": "A zero-day is an unknown flaw with no patch yet; EOL software is known to be unsupported, and the vendor won't patch it.",
                "C": "Resetting to defaults doesn't make an unsupported OS supported and usually weakens security.",
                "D": "The problem is the absence of patches, not one expired certificate or weak cipher.",
            },
            "exam_pattern": "No more vendor patches = EOL/legacy → segment + compensating controls; distinct from an unpatched zero-day.",
        },
    },

    # ===== malware ==========================================================
    {
        "id": "secplus-tvm-117", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "malware", "difficulty": 1, "type": "mcq",
        "stem": "A user downloads what looks like a free PDF-converter utility; it works as "
                "advertised but silently installs a backdoor. Which malware type is this?",
        "options": [
            {"id": "A", "text": "Trojan"},
            {"id": "B", "text": "Worm"},
            {"id": "C", "text": "Virus"},
            {"id": "D", "text": "Bloatware"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Malware disguised as legitimate, desirable software that hides a malicious payload "
                       "(here a backdoor) is a trojan.",
            "distractors": {
                "B": "A worm self-propagates across systems on its own; it isn't a disguised app the user chooses to install.",
                "C": "A virus attaches to a host file and needs that file executed to spread; the key trait here is disguise, not host-file infection.",
                "D": "Bloatware is unwanted but non-malicious pre-installed software; it isn't a hidden backdoor.",
            },
            "exam_pattern": "Looks legit, hides a payload the user installs = trojan. Self-spreads on its own = worm.",
        },
    },
    {
        "id": "secplus-tvm-118", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "malware", "difficulty": 2, "type": "mcq",
        "stem": "Malware spreads automatically from host to host across the network by exploiting a "
                "service vulnerability, requiring no user interaction and attaching to no host file. "
                "Which malware type is this?",
        "options": [
            {"id": "A", "text": "Worm"},
            {"id": "B", "text": "Virus"},
            {"id": "C", "text": "Trojan"},
            {"id": "D", "text": "Logic bomb"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Self-replicating malware that propagates on its own across networks without user "
                       "action or a host file is a worm.",
            "distractors": {
                "B": "A virus needs a host file and user execution to spread — it is not self-propagating on its own.",
                "C": "A trojan masquerades as legitimate software and does not self-replicate.",
                "D": "A logic bomb stays dormant until a trigger condition; it isn't defined by network self-spread.",
            },
            "exam_pattern": "Self-propagating, no user action, no host file = worm; needs a host file + user to run = virus.",
        },
    },
    {
        "id": "secplus-tvm-119", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "malware", "difficulty": 3, "type": "mcq",
        "stem": "After a breach, investigators find malware operating at the kernel level that hides "
                "its own processes and files, so the installed antivirus reports a clean system. "
                "Which malware type is this, and how is it BEST detected?",
        "options": [
            {"id": "A", "text": "Rootkit — scan from trusted external/offline boot media"},
            {"id": "B", "text": "Keylogger — review browser history"},
            {"id": "C", "text": "Ransomware — look for an encryption ransom note"},
            {"id": "D", "text": "Adware — clear the ad cache"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Kernel-level malware that conceals its presence and subverts the OS so AV can't see "
                       "it is a rootkit; because it hides from the running OS, detection is best done by booting from "
                       "trusted external/offline media (or boot/integrity attestation).",
            "distractors": {
                "B": "A keylogger captures keystrokes; it doesn't hook the kernel to hide the whole system, and browser history wouldn't reveal it.",
                "C": "Ransomware announces itself with encryption and a ransom demand — the opposite of stealthy hiding.",
                "D": "Adware shows unwanted ads and is not a kernel-level stealth component.",
            },
            "exam_pattern": "Hides at kernel level so AV sees nothing = rootkit → scan from trusted offline/boot media.",
        },
    },

    # ===== network_attacks ==================================================
    {
        "id": "secplus-tvm-120", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "On a switched LAN, an attacker sends forged ARP replies so that traffic between a "
                "victim and the default gateway flows through the attacker's machine, where it can "
                "be read or altered. Which attack is this?",
        "options": [
            {"id": "A", "text": "On-path attack (formerly man-in-the-middle)"},
            {"id": "B", "text": "Distributed denial-of-service"},
            {"id": "C", "text": "VLAN hopping"},
            {"id": "D", "text": "Credential replay"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Inserting yourself into the traffic path between two parties — here via ARP "
                       "spoofing — to intercept or modify data is an on-path (man-in-the-middle) attack.",
            "distractors": {
                "B": "A DDoS floods a target to deny availability; it doesn't quietly relay traffic to eavesdrop.",
                "C": "VLAN hopping crosses VLAN boundaries via trunk abuse or double tagging, not ARP-based interception on one segment.",
                "D": "Credential replay reuses captured authentication data; an on-path position may enable it, but the attack described is the interception itself.",
            },
            "exam_pattern": "ARP spoofing to sit between host and gateway = on-path (MITM).",
        },
    },
    {
        "id": "secplus-tvm-121", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "network_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker injects a forged record into a DNS resolver's cache so that users who "
                "type the correct bank URL are sent to the attacker's server. Which attack is this?",
        "options": [
            {"id": "A", "text": "DNS cache poisoning (DNS spoofing)"},
            {"id": "B", "text": "Typosquatting"},
            {"id": "C", "text": "Buffer overflow"},
            {"id": "D", "text": "SQL injection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Corrupting a resolver's cache so a legitimate domain name resolves to an "
                       "attacker-controlled IP is DNS cache poisoning/spoofing; DNSSEC validation is the primary defense.",
            "distractors": {
                "B": "Typosquatting relies on the user mistyping the name; here the user types it correctly but DNS lies.",
                "C": "A buffer overflow overwrites memory in a program, not DNS records.",
                "D": "SQL injection manipulates database queries, unrelated to name resolution.",
            },
            "exam_pattern": "Correct name but wrong IP because the resolver's cache was tampered with = DNS poisoning (counter with DNSSEC).",
        },
    },
    {
        "id": "secplus-tvm-122", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "network_attacks", "difficulty": 3, "type": "mcq",
        "stem": "An attacker sends small DNS queries with the victim's spoofed source address to many "
                "open resolvers, which each reply with a much larger response aimed at the victim. "
                "Which attack technique is this?",
        "options": [
            {"id": "A", "text": "Reflected, amplified DDoS"},
            {"id": "B", "text": "On-path attack"},
            {"id": "C", "text": "Credential replay"},
            {"id": "D", "text": "VLAN hopping"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Spoofing the victim's address so third-party servers 'reflect' responses, chosen "
                       "because each reply is far larger than the query ('amplification'), is a reflected/amplified "
                       "DDoS — classic DNS/NTP amplification.",
            "distractors": {
                "B": "An on-path attack intercepts traffic between two parties; this instead drowns the victim in reflected volume.",
                "C": "Credential replay reuses captured authentication data, not spoofed queries for volume.",
                "D": "VLAN hopping is a LAN segmentation-bypass attack, not a volumetric flood.",
            },
            "exam_pattern": "Spoofed source + small request → big reply from third parties = reflected/amplified DDoS.",
        },
    },

    # ===== application_attacks ==============================================
    {
        "id": "secplus-tvm-123", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "application_attacks", "difficulty": 2, "type": "mcq",
        "stem": "An attacker posts a forum comment containing a <script> tag that then runs in the "
                "browser of every user who later views the thread, stealing their session cookies. "
                "Which attack is this, and the BEST fix?",
        "options": [
            {"id": "A", "text": "Stored cross-site scripting (XSS) — output-encode and validate input"},
            {"id": "B", "text": "SQL injection — use parameterized queries"},
            {"id": "C", "text": "Cross-site request forgery — add anti-CSRF tokens"},
            {"id": "D", "text": "Directory traversal — canonicalize file paths"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Persisting attacker script on the server so it executes in other users' browsers is "
                       "stored (persistent) XSS; defenses are context-aware output encoding, input validation, and a Content Security Policy.",
            "distractors": {
                "B": "SQL injection targets the database via input; this payload runs in victims' browsers, not the DB.",
                "C": "CSRF tricks an authenticated user's browser into making a request; here script executes in the victim's page (XSS), not a forged cross-site request.",
                "D": "Directory traversal reads files outside the web root using ../; no file path is being traversed.",
            },
            "exam_pattern": "<script> stored and run in other users' browsers = stored XSS → output encoding + input validation + CSP.",
        },
    },
    {
        "id": "secplus-tvm-124", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "application_attacks", "difficulty": 3, "type": "mcq",
        "stem": "While logged in to her bank in one tab, a user clicks a link on another site that "
                "silently submits a funds-transfer request to the bank using her active session. "
                "Which attack is this, and the standard defense?",
        "options": [
            {"id": "A", "text": "Cross-site request forgery (CSRF) — require per-request anti-CSRF tokens"},
            {"id": "B", "text": "Stored XSS — encode output"},
            {"id": "C", "text": "Replay attack — add timestamps/nonces to tokens"},
            {"id": "D", "text": "Privilege escalation — enforce least privilege"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Abusing a victim's already-authenticated session to submit an unwanted state-changing "
                       "request is CSRF; synchronizer (anti-CSRF) tokens, plus SameSite cookies, are the standard defenses.",
            "distractors": {
                "B": "XSS runs attacker script in the victim's page; CSRF needs no injected script on the target site, only the victim's valid session.",
                "C": "A replay attack resends captured valid data; CSRF forges a new request rather than replaying a captured one.",
                "D": "Privilege escalation gains higher rights; here the user's own normal rights are abused through her session.",
            },
            "exam_pattern": "Victim's logged-in session abused to make a request they didn't intend = CSRF → anti-CSRF tokens + SameSite.",
        },
    },
    {
        "id": "secplus-tvm-125", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "application_attacks", "difficulty": 2, "type": "mcq",
        "stem": "A web application serves files by name, and an attacker requests "
                "'../../../../etc/passwd' to read a file outside the web root. Which attack is this?",
        "options": [
            {"id": "A", "text": "Directory (path) traversal"},
            {"id": "B", "text": "Cross-site scripting"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Buffer overflow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Using ../ sequences to escape the intended directory and read arbitrary files is "
                       "directory/path traversal; fix it with input validation and canonicalizing/constraining the resolved path.",
            "distractors": {
                "B": "XSS injects script into pages viewed by users; it doesn't read server files by path.",
                "C": "SQL injection manipulates database queries, not filesystem paths.",
                "D": "A buffer overflow corrupts memory; this request abuses path handling, not memory bounds.",
            },
            "exam_pattern": "../ sequences to climb out of the web root and read files = directory/path traversal.",
        },
    },

    # ===== mitigation_techniques ============================================
    {
        "id": "secplus-tvm-126", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "mitigation_techniques", "difficulty": 2, "type": "mcq",
        "stem": "A hardened kiosk must run only a short, known set of programs, and the team wants to "
                "block all unauthorized or unknown executables — including never-before-seen malware "
                "— from running. Which mitigation BEST achieves this?",
        "options": [
            {"id": "A", "text": "Application allow listing (only approved executables run)"},
            {"id": "B", "text": "Signature-based antivirus (block known-bad files)"},
            {"id": "C", "text": "A longer password policy"},
            {"id": "D", "text": "Full-disk encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Application allowlisting permits only explicitly approved programs to execute and "
                       "denies everything else by default, so unknown or unauthorized code — including novel malware — can't run.",
            "distractors": {
                "B": "Signature-based AV blocks only known-bad files and misses never-before-seen malware — a default-allow approach, the opposite of what's needed.",
                "C": "Password length protects authentication, not which programs may execute.",
                "D": "Disk encryption protects data at rest; it does not control program execution.",
            },
            "exam_pattern": "Run only an approved set and deny all else (default-deny) = application allowlisting; a blocklist/AV is default-allow.",
        },
    },
    {
        "id": "secplus-tvm-127", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "mitigation_techniques", "difficulty": 2, "type": "mcq",
        "stem": "After ransomware spread laterally across a flat network and reached every server, "
                "the team wants to limit how far a future infection can move. Which mitigation "
                "DIRECTLY addresses lateral movement?",
        "options": [
            {"id": "A", "text": "Network segmentation"},
            {"id": "B", "text": "Longer password rotation intervals"},
            {"id": "C", "text": "Enabling verbose logging"},
            {"id": "D", "text": "Replacing the antivirus product"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Segmenting the network into isolated zones with filtered boundaries contains an "
                       "infection to one segment and blocks lateral movement across the environment.",
            "distractors": {
                "B": "Password rotation affects credential freshness, not how malware traverses a flat network.",
                "C": "Verbose logging improves detection and forensics but does not by itself stop lateral spread.",
                "D": "Swapping AV products may catch more samples but doesn't constrain movement the way segmentation does.",
            },
            "exam_pattern": "Stop lateral movement / limit the blast radius = segmentation (isolation).",
        },
    },
    {
        "id": "secplus-tvm-128", "exam": "secplus", "domain": "threats_vulns_mitigations",
        "subtopic": "mitigation_techniques", "difficulty": 2, "type": "multi",
        "stem": "A technician is hardening a new server before deployment. Which TWO actions are "
                "legitimate host-hardening steps? (Choose two.)",
        "options": [
            {"id": "A", "text": "Disable unused services and close unnecessary ports"},
            {"id": "B", "text": "Change the default administrative credentials"},
            {"id": "C", "text": "Grant all users local administrator rights for convenience"},
            {"id": "D", "text": "Leave remote management open to the entire internet"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Disabling unused services/ports and replacing default credentials both shrink the "
                       "attack surface and are core host-hardening steps, alongside patching, EDR, a host firewall, and least privilege.",
            "distractors": {
                "C": "Granting everyone local admin violates least privilege and WIDENS risk — the opposite of hardening.",
                "D": "Exposing remote management to the whole internet enlarges the attack surface rather than reducing it.",
            },
            "exam_pattern": "Hardening = remove/disable the unnecessary and change defaults; adding broad rights or exposure is anti-hardening.",
        },
    },
]
