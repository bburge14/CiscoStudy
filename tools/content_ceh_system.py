"""EC-Council CEH v13 pool - Domain 2.0: System Hacking and Malware.

Original, objective-aligned practice items for CertLab's CEH track, covering the
two subtopics of the System Hacking and Malware domain:
  * ceh_system_hacking - password attacks (dictionary, brute force, rainbow
                         tables) and their defenses (salting), pass-the-hash,
                         privilege escalation, steganography, covering tracks,
                         and offline hash-cracking tools (John, Hashcat).
  * ceh_malware_threats - malware taxonomy (virus, worm, Trojan/RAT, rootkit,
                         ransomware, spyware, botnet), advanced persistent
                         threats (APT), and static vs dynamic malware analysis.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the tool, technique, malware class, or defense) - no
working exploit code, payloads, or step-by-step attack instructions, and never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== ceh_system_hacking ===============================================
    {
        "id": "ceh-sys-001", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 1, "type": "mcq",
        "stem": "An attacker tries every entry from a prepared list of likely passwords against a login "
                "prompt. Which password attack is this?",
        "options": [
            {"id": "A", "text": "Dictionary attack"},
            {"id": "B", "text": "Brute-force attack"},
            {"id": "C", "text": "Rainbow table attack"},
            {"id": "D", "text": "Pass-the-hash"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A dictionary attack tries candidates from a curated wordlist of likely passwords, "
                       "making it faster than exhausting every combination.",
            "distractors": {
                "B": "A brute-force attack systematically tries all possible character combinations, not a wordlist.",
                "C": "A rainbow table attack reverses captured hashes using precomputed tables, not live guessing.",
                "D": "Pass-the-hash reuses a stolen hash to authenticate; it does not guess plaintext passwords.",
            },
            "exam_pattern": "Curated wordlist of likely passwords = dictionary attack.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-002", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "Which password-cracking method relies on large precomputed tables that map hashes back to "
                "their plaintext, trading disk space for cracking speed?",
        "options": [
            {"id": "A", "text": "Dictionary attack"},
            {"id": "B", "text": "Rainbow table attack"},
            {"id": "C", "text": "Online brute-force"},
            {"id": "D", "text": "Password spraying"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A rainbow table attack uses precomputed hash-to-plaintext chains, so cracking a captured "
                       "hash becomes a fast lookup instead of hashing candidates at attack time.",
            "distractors": {
                "A": "A dictionary attack hashes each wordlist candidate during the attack; it stores no precomputed tables.",
                "C": "Online brute-force guesses against the live service and is slow and noisy.",
                "D": "Password spraying tries a few common passwords across many accounts to avoid lockout.",
            },
            "exam_pattern": "Precomputed hash-to-plaintext tables = rainbow tables (salting defeats them).",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-003", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "Which defensive technique adds a unique random value to each password before hashing, most "
                "directly defeating precomputed rainbow-table attacks?",
        "options": [
            {"id": "A", "text": "Account lockout threshold"},
            {"id": "B", "text": "A minimum password-length policy"},
            {"id": "C", "text": "Salting"},
            {"id": "D", "text": "Single sign-on"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Salting adds a unique random value per password, so identical passwords hash differently "
                       "and a single precomputed table cannot be reused - defeating rainbow tables.",
            "distractors": {
                "A": "Lockout slows online guessing but does nothing against offline precomputed-table lookups.",
                "B": "Length raises brute-force cost but does not stop a precomputed table from matching a given hash.",
                "D": "Single sign-on centralizes authentication; it does not protect stored hashes from rainbow tables.",
            },
            "exam_pattern": "Unique random value per password that breaks precomputed tables = salting.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-004", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "An attacker captures an NTLM password hash and authenticates to other systems using the "
                "hash itself, without ever cracking the plaintext password. What is this technique?",
        "options": [
            {"id": "A", "text": "Kerberoasting"},
            {"id": "B", "text": "Password spraying"},
            {"id": "C", "text": "Credential stuffing"},
            {"id": "D", "text": "Pass-the-hash"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Pass-the-hash reuses a captured NTLM hash directly to authenticate, so the attacker "
                       "never needs the cleartext password.",
            "distractors": {
                "A": "Kerberoasting requests service tickets to crack service-account passwords offline, a different flow.",
                "B": "Password spraying guesses a few common passwords across many accounts.",
                "C": "Credential stuffing replays leaked username/password pairs, not hashes, against logins.",
            },
            "exam_pattern": "Authenticate with the hash itself, no cracking = pass-the-hash.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-005", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "After gaining a standard-user shell, an attacker exploits a misconfiguration to obtain "
                "SYSTEM/root-level rights on the same host. What is this step called?",
        "options": [
            {"id": "A", "text": "Privilege escalation"},
            {"id": "B", "text": "Lateral movement"},
            {"id": "C", "text": "Footprinting"},
            {"id": "D", "text": "Banner grabbing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Raising one's rights from a limited account to administrative/root level is privilege "
                       "escalation (vertical escalation).",
            "distractors": {
                "B": "Lateral movement spreads to other hosts at a similar privilege, not higher rights on the same host.",
                "C": "Footprinting is early information gathering, not gaining higher rights.",
                "D": "Banner grabbing reads service versions; it does not elevate privileges.",
            },
            "exam_pattern": "Higher rights on the same host = (vertical) privilege escalation; other hosts = lateral movement.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-006", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 2, "type": "mcq",
        "stem": "An insider hides a confidential spreadsheet inside an ordinary-looking JPEG image so the "
                "data can leave the network without drawing attention. Which technique is this?",
        "options": [
            {"id": "A", "text": "Symmetric encryption"},
            {"id": "B", "text": "Steganography"},
            {"id": "C", "text": "Hashing"},
            {"id": "D", "text": "Tokenization"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Steganography conceals the existence of data by embedding it inside a carrier file such "
                       "as an image, so the hidden content is not obvious.",
            "distractors": {
                "A": "Encryption scrambles data but produces visible ciphertext, revealing that something is protected.",
                "C": "Hashing is a one-way digest; it cannot hide and later recover a file inside another.",
                "D": "Tokenization substitutes a surrogate value for sensitive data; it does not hide a file in a carrier.",
            },
            "exam_pattern": "Hide data's existence inside a carrier (image/audio) = steganography; scramble it = cryptography.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-007", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Deleting or altering a system's security and event ______ is a common way "
                "attackers cover their tracks and hide evidence of an intrusion.",
        "correct": ["logs", "log", "event logs"],
        "explanation": {
            "correct": "Clearing or tampering with logs removes the record of attacker activity; forwarding logs "
                       "to a secured, centralized server defends against this covering-tracks technique.",
            "distractors": {},
            "exam_pattern": "Hide intrusion evidence by clearing/altering logs = covering tracks.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },
    {
        "id": "ceh-sys-008", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_system_hacking", "difficulty": 3, "type": "multi",
        "stem": "Which TWO tools are primarily offline password-hash crackers used after the hashes have "
                "already been obtained? (Choose two.)",
        "options": [
            {"id": "A", "text": "Hashcat"},
            {"id": "B", "text": "Wireshark"},
            {"id": "C", "text": "John the Ripper"},
            {"id": "D", "text": "Nikto"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Hashcat and John the Ripper both crack captured password hashes offline using dictionary, "
                       "brute-force, and rule-based attacks.",
            "distractors": {
                "B": "Wireshark is a packet capture and analysis tool, not a hash cracker.",
                "D": "Nikto is a web-server vulnerability scanner, not a password cracker.",
            },
            "exam_pattern": "Crack captured hashes offline = Hashcat / John the Ripper.",
        },
        "references": ["CEH v13 Module 06: System Hacking"],
    },

    # ===== ceh_malware_threats ==============================================
    {
        "id": "ceh-sys-009", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Which type of malware self-replicates and spreads across networks on its own, without "
                "attaching to a host file or requiring a user to run it?",
        "options": [
            {"id": "A", "text": "Worm"},
            {"id": "B", "text": "Virus"},
            {"id": "C", "text": "Trojan"},
            {"id": "D", "text": "Rootkit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A worm is self-replicating and self-propagating; it spreads across networks without a "
                       "host file or user action.",
            "distractors": {
                "B": "A virus attaches to a host file and needs that file to be executed to spread.",
                "C": "A Trojan masquerades as legitimate software and does not self-replicate.",
                "D": "A rootkit hides presence on a system; it does not self-propagate across a network.",
            },
            "exam_pattern": "Self-spreading with no host file/user action = worm; needs a host file = virus.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-010", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 1, "type": "mcq",
        "stem": "A user installs a 'free game' that secretly opens a backdoor giving an attacker remote "
                "control of the machine. Which malware category best fits?",
        "options": [
            {"id": "A", "text": "Worm"},
            {"id": "B", "text": "Trojan (a remote access Trojan, RAT)"},
            {"id": "C", "text": "Ransomware"},
            {"id": "D", "text": "Adware"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Software disguised as something desirable that hides a malicious payload is a Trojan; one "
                       "that grants remote control is a RAT.",
            "distractors": {
                "A": "A worm self-propagates and is not disguised as a wanted application.",
                "C": "Ransomware encrypts files and demands payment; it is not primarily a hidden remote-control tool.",
                "D": "Adware displays unwanted advertisements rather than granting remote control.",
            },
            "exam_pattern": "Disguised-as-legit plus hidden payload = Trojan; remote-control backdoor = RAT.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-011", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Which malware is specifically designed to conceal its own presence and that of other "
                "malicious components, often by subverting the operating-system kernel?",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Keylogger"},
            {"id": "C", "text": "Rootkit"},
            {"id": "D", "text": "Worm"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A rootkit hides files, processes, and itself (sometimes at kernel level) to maintain "
                       "stealthy, privileged access.",
            "distractors": {
                "A": "Ransomware announces itself by encrypting files and demanding payment, the opposite of hiding.",
                "B": "A keylogger records keystrokes; concealment is not its defining purpose.",
                "D": "A worm spreads to other hosts rather than hiding on one.",
            },
            "exam_pattern": "Stealth and self-concealment, often kernel-level = rootkit.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-012", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 1, "type": "mcq",
        "stem": "Malware encrypts a victim's files and demands payment in exchange for the decryption key. "
                "Which category is this?",
        "options": [
            {"id": "A", "text": "Ransomware"},
            {"id": "B", "text": "Rootkit"},
            {"id": "C", "text": "Spyware"},
            {"id": "D", "text": "Logic bomb"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Ransomware encrypts data and extorts the victim for the key; offline, tested backups are "
                       "the primary defense.",
            "distractors": {
                "B": "A rootkit hides presence; it does not encrypt files for extortion.",
                "C": "Spyware covertly collects information rather than encrypting data for ransom.",
                "D": "A logic bomb triggers a payload when a condition is met; encryption-for-ransom is not its definition.",
            },
            "exam_pattern": "Encrypt files and demand payment = ransomware.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-013", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "A well-resourced group quietly maintains long-term access to a target network to steal data "
                "over many months while avoiding detection. This is best described as a(n)?",
        "options": [
            {"id": "A", "text": "Script kiddie attack"},
            {"id": "B", "text": "Opportunistic worm outbreak"},
            {"id": "C", "text": "Drive-by download"},
            {"id": "D", "text": "Advanced persistent threat (APT)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "An APT is a stealthy, well-resourced actor that maintains long-term, persistent access to "
                       "exfiltrate data over an extended period.",
            "distractors": {
                "A": "Script kiddies lack the sophistication and sustained persistence described.",
                "B": "A worm outbreak is noisy and automated, not quiet long-term access.",
                "C": "A drive-by download is a single infection vector, not a months-long campaign.",
            },
            "exam_pattern": "Stealthy, well-funded, long-term persistent access = APT.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-014", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 3, "type": "mcq",
        "stem": "An analyst runs a suspicious binary inside an isolated sandbox and observes the files, "
                "registry keys, and network connections it creates. Which malware-analysis approach is this?",
        "options": [
            {"id": "A", "text": "Static analysis"},
            {"id": "B", "text": "Dynamic (behavioral) analysis"},
            {"id": "C", "text": "Steganalysis"},
            {"id": "D", "text": "Differential cryptanalysis"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Dynamic analysis executes the sample in a controlled sandbox and observes its runtime "
                       "behavior - file, registry, and network activity.",
            "distractors": {
                "A": "Static analysis inspects the file without executing it (strings, headers, disassembly).",
                "C": "Steganalysis detects data hidden inside carrier files; it is not malware behavior analysis.",
                "D": "Differential cryptanalysis attacks ciphers, not the behavior of a program.",
            },
            "exam_pattern": "Run it and observe behavior = dynamic; inspect without running = static.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-015", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Examining a malware sample's strings, headers, imports, and disassembly "
                "without executing it is called ______ analysis.",
        "correct": ["static"],
        "explanation": {
            "correct": "Static analysis inspects the file's contents without running it, so the code never "
                       "executes and the examination carries no risk of infection.",
            "distractors": {},
            "exam_pattern": "Inspect the sample without executing it = static analysis.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
    {
        "id": "ceh-sys-016", "exam": "ceh", "domain": "ceh_system_malware",
        "subtopic": "ceh_malware_threats", "difficulty": 2, "type": "mcq",
        "stem": "Thousands of compromised 'zombie' hosts take orders from a command-and-control server to "
                "launch attacks on demand. This network of bots is called a?",
        "options": [
            {"id": "A", "text": "Honeynet"},
            {"id": "B", "text": "Rainbow table"},
            {"id": "C", "text": "Botnet"},
            {"id": "D", "text": "Faraday cage"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A botnet is a network of compromised hosts (bots/zombies) controlled through a "
                       "command-and-control channel to carry out coordinated attacks such as DDoS or spam.",
            "distractors": {
                "A": "A honeynet is a decoy network set up by defenders to study attackers.",
                "B": "A rainbow table is a password-cracking data structure, not a network of hosts.",
                "D": "A Faraday cage blocks radio signals; it is unrelated to compromised hosts.",
            },
            "exam_pattern": "Zombies plus command-and-control = botnet.",
        },
        "references": ["CEH v13 Module 07: Malware Threats"],
    },
]
