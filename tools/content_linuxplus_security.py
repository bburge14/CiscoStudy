"""CompTIA Linux+ (XK0-006) pool - Domain 2: Security.

Original, objective-aligned practice items for the five Security subtopics
tracked in CertLab:
  * linuxp_permissions_acl - chmod (symbolic + octal), chown/chgrp, umask, the
                             SUID/SGID/sticky special bits, ACLs (getfacl/
                             setfacl), and file attributes (chattr/lsattr).
  * linuxp_access_control  - sudo/visudo and /etc/sudoers, PAM, SELinux
                             (enforcing/permissive, getenforce/setenforce,
                             restorecon/semanage), and AppArmor.
  * linuxp_firewall        - firewalld (firewall-cmd, zones), ufw, and the
                             iptables -> nftables packet-filter frameworks.
  * linuxp_ssh_hardening   - sshd_config directives, key-based authentication,
                             disabling root login, ssh-keygen/ssh-copy-id.
  * linuxp_crypto_certs    - GnuPG, OpenSSL certificate handling, and LUKS
                             full-disk/block-device encryption (cryptsetup).

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased,
every wrong option carries a distractor note, and each item cites the public
XK0-006 objective domain it draws on. Commands, flags, directives, and file
paths are real and version-resilient across mainstream RHEL/Fedora and Debian/
Ubuntu systems; no memorized or real exam items are used.
"""

QUESTIONS = [
    # ===== linuxp_permissions_acl ===========================================
    {
        "id": "linuxplus-sec-001", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "mcq",
        "stem": "Which command sets a file's permissions to read/write/execute for the owner and "
                "read/execute for both the group and others (rwxr-xr-x)?",
        "options": [
            {"id": "A", "text": "chmod 644 script.sh"},
            {"id": "B", "text": "chmod 755 script.sh"},
            {"id": "C", "text": "chmod 775 script.sh"},
            {"id": "D", "text": "chmod 750 script.sh"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Octal 755 = owner rwx (7), group r-x (5), others r-x (5), exactly rwxr-xr-x.",
            "distractors": {
                "A": "644 is rw-r--r-- (no execute for anyone) — wrong for an executable script.",
                "C": "775 is rwxrwxr-x, which grants the group write access too.",
                "D": "750 is rwxr-x--- , which denies 'others' any access.",
            },
            "exam_pattern": "Octal: r=4, w=2, x=1 per digit (owner/group/other). 7=rwx, 5=r-x, 6=rw-, 4=r--.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — File permissions (chmod octal)"],
    },
    {
        "id": "linuxplus-sec-002", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "mcq",
        "stem": "Using symbolic mode, which command adds execute permission for the file's OWNER only, "
                "leaving the group and other bits unchanged?",
        "options": [
            {"id": "A", "text": "chmod u+x file"},
            {"id": "B", "text": "chmod +x file"},
            {"id": "C", "text": "chmod o+x file"},
            {"id": "D", "text": "chmod u-x file"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "u+x adds (+) the execute (x) bit for the user/owner (u) class only, without "
                       "touching group or other.",
            "distractors": {
                "B": "+x (equivalent to a+x) adds execute for all classes (owner, group, other), subject to umask.",
                "C": "o+x adds execute for OTHERS, not the owner.",
                "D": "u-x REMOVES the owner's execute bit, the opposite action.",
            },
            "exam_pattern": "Symbolic classes: u=user/owner, g=group, o=others, a=all; +add, -remove, =set.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — File permissions (chmod symbolic)"],
    },
    {
        "id": "linuxplus-sec-003", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 3, "type": "mcq",
        "stem": "A long listing of /tmp shows permissions drwxrwxrwt. What does the trailing 't' in the "
                "'others' execute position indicate?",
        "options": [
            {"id": "A", "text": "The sticky bit is set, so a user may delete or rename only files they own within the directory"},
            {"id": "B", "text": "The SUID bit is set, so programs run as the file owner"},
            {"id": "C", "text": "The SGID bit is set, so new files inherit the directory's group"},
            {"id": "D", "text": "The directory is actually a symbolic link"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A trailing 't' marks the sticky bit on a directory. On a world-writable directory "
                       "like /tmp it restricts deletion/renaming so users can only remove their own files.",
            "distractors": {
                "B": "SUID appears as 's' in the OWNER execute position and applies to executables, not this directory bit.",
                "C": "SGID appears as 's' in the GROUP execute position; it is what makes new files inherit the group.",
                "D": "A symbolic link is shown by a leading 'l' in the type field, not a trailing 't'.",
            },
            "exam_pattern": "Special bits in the x column: SUID=s (owner), SGID=s (group), sticky=t (other).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Special permissions (sticky bit)"],
    },
    {
        "id": "linuxplus-sec-004", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "mcq",
        "stem": "Beyond the standard owner/group/other bits, you must grant user 'alice' read and write "
                "access to report.txt via an access control list. Which command does this?",
        "options": [
            {"id": "A", "text": "getfacl report.txt"},
            {"id": "B", "text": "setfacl -x u:alice report.txt"},
            {"id": "C", "text": "setfacl -m u:alice:rw report.txt"},
            {"id": "D", "text": "chmod u+rw report.txt"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "setfacl -m modifies/adds an ACL entry; u:alice:rw grants alice read+write "
                       "independently of the file's owner, group, or other bits.",
            "distractors": {
                "A": "getfacl only DISPLAYS existing ACL entries; it changes nothing.",
                "B": "setfacl -x REMOVES alice's ACL entry rather than granting access.",
                "D": "chmod u+rw changes the OWNER's bits, which affects whoever owns the file, not alice specifically.",
            },
            "exam_pattern": "setfacl -m to add/modify, -x to remove, -b to clear all; getfacl to view.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Access control lists (setfacl)"],
    },
    {
        "id": "linuxplus-sec-005", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "fill",
        "stem": "Which command changes special file attributes on ext4/xfs filesystems — for example, "
                "setting the immutable (+i) attribute so a file cannot be modified or deleted even by "
                "root? (command name only)",
        "correct": ["chattr", "/usr/bin/chattr"],
        "explanation": {
            "correct": "chattr changes file attributes; 'chattr +i file' makes a file immutable (no "
                       "modify, delete, rename, or link) until removed with 'chattr -i'. View attributes with lsattr.",
            "distractors": {},
            "exam_pattern": "chattr sets attributes (+i immutable, +a append-only); lsattr lists them.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — File attributes (chattr)"],
    },

    # ===== linuxp_access_control ============================================
    {
        "id": "linuxplus-sec-006", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 1, "type": "mcq",
        "stem": "Which command should be used to edit the /etc/sudoers file safely, because it locks the "
                "file and validates syntax before saving?",
        "options": [
            {"id": "A", "text": "vi /etc/sudoers"},
            {"id": "B", "text": "visudo"},
            {"id": "C", "text": "sudo -l"},
            {"id": "D", "text": "usermod -aG sudo bob"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "visudo opens /etc/sudoers with a lock and runs a syntax check on save, preventing "
                       "a broken file that could lock everyone out of sudo.",
            "distractors": {
                "A": "Editing /etc/sudoers directly with vi skips the syntax check and risks a parse error that disables sudo.",
                "C": "sudo -l lists the current user's allowed sudo commands; it does not edit the file.",
                "D": "usermod -aG sudo adds a user to the sudo group but does not edit sudoers rules.",
            },
            "exam_pattern": "Always edit sudoers with visudo (or files in /etc/sudoers.d/ via visudo -f).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Privilege escalation (visudo/sudoers)"],
    },
    {
        "id": "linuxplus-sec-007", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 2, "type": "mcq",
        "stem": "On a RHEL system you suspect SELinux is involved in a failure. Which command reports "
                "the current SELinux mode (Enforcing, Permissive, or Disabled)?",
        "options": [
            {"id": "A", "text": "getenforce"},
            {"id": "B", "text": "setenforce 1"},
            {"id": "C", "text": "restorecon -R /var/www"},
            {"id": "D", "text": "semodule -l"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "getenforce prints the current mode: Enforcing, Permissive, or Disabled. "
                       "(sestatus gives the same plus more detail.)",
            "distractors": {
                "B": "setenforce 1 CHANGES the running mode to Enforcing; it does not report it.",
                "C": "restorecon resets file security contexts; it does not show the mode.",
                "D": "semodule -l lists installed SELinux policy modules, not the mode.",
            },
            "exam_pattern": "getenforce reads mode; setenforce 0|1 toggles Permissive/Enforcing at runtime; "
                            "persist in /etc/selinux/config.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SELinux modes (getenforce)"],
    },
    {
        "id": "linuxplus-sec-008", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 3, "type": "mcq",
        "stem": "After restoring files into /var/www/html from a backup, Apache returns 403 errors and "
                "SELinux is Enforcing. The DAC permissions look correct. Which command fixes the most "
                "likely cause by resetting the files to their default SELinux contexts?",
        "options": [
            {"id": "A", "text": "setenforce 0"},
            {"id": "B", "text": "chmod -R 755 /var/www/html"},
            {"id": "C", "text": "restorecon -Rv /var/www/html"},
            {"id": "D", "text": "chown -R apache:apache /var/www/html"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Restored files often carry the wrong SELinux type. restorecon -Rv recursively "
                       "relabels them to the default context defined for that path, which Apache can serve.",
            "distractors": {
                "A": "setenforce 0 only disables enforcement, masking the problem instead of fixing the labels (and is poor practice).",
                "B": "chmod changes standard (DAC) permissions, which the scenario says are already correct.",
                "D": "chown fixes ownership, not the SELinux security context causing the denial.",
            },
            "exam_pattern": "403/AVC denials after moving files usually mean wrong SELinux context — fix with restorecon.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SELinux contexts (restorecon)"],
    },
    {
        "id": "linuxplus-sec-009", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 2, "type": "mcq",
        "stem": "On an Ubuntu host that uses AppArmor for mandatory access control, which command "
                "reports which profiles are loaded and whether each is in enforce or complain mode?",
        "options": [
            {"id": "A", "text": "getenforce"},
            {"id": "B", "text": "aa-status"},
            {"id": "C", "text": "aa-complain /etc/apparmor.d/usr.sbin.nginx"},
            {"id": "D", "text": "setenforce 0"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "aa-status (also called apparmor_status) lists loaded AppArmor profiles and counts "
                       "those in enforce versus complain mode.",
            "distractors": {
                "A": "getenforce is an SELinux tool; AppArmor and SELinux are different MAC systems.",
                "C": "aa-complain switches a single profile INTO complain mode; it does not report overall status.",
                "D": "setenforce is an SELinux command and has no effect on AppArmor.",
            },
            "exam_pattern": "AppArmor (Debian/Ubuntu default) uses aa-status / aa-enforce / aa-complain; "
                            "SELinux (RHEL default) uses getenforce / setenforce.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Mandatory access control (AppArmor)"],
    },

    # ===== linuxp_firewall ==================================================
    {
        "id": "linuxplus-sec-010", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "mcq",
        "stem": "On a RHEL server running firewalld, which command permanently allows HTTPS traffic in "
                "the default zone (persisting across reloads and reboots)?",
        "options": [
            {"id": "A", "text": "firewall-cmd --add-service=https"},
            {"id": "B", "text": "firewall-cmd --permanent --remove-service=https"},
            {"id": "C", "text": "ufw allow https"},
            {"id": "D", "text": "firewall-cmd --permanent --add-service=https"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "firewall-cmd --permanent --add-service=https writes the rule to the permanent "
                       "configuration; follow with 'firewall-cmd --reload' to apply it to the running firewall.",
            "distractors": {
                "A": "Without --permanent the rule is runtime-only and is lost on reload or reboot.",
                "B": "--remove-service REMOVES the HTTPS allowance instead of adding it.",
                "C": "ufw is the Ubuntu firewall front end, not used to manage firewalld on RHEL.",
            },
            "exam_pattern": "firewalld changes are runtime-only unless --permanent; then --reload to activate.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Host firewall (firewalld)"],
    },
    {
        "id": "linuxplus-sec-011", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "mcq",
        "stem": "On Ubuntu, which command uses the Uncomplicated Firewall (ufw) to allow incoming SSH "
                "connections?",
        "options": [
            {"id": "A", "text": "ufw allow 22/tcp"},
            {"id": "B", "text": "ufw deny 22/tcp"},
            {"id": "C", "text": "firewall-cmd --add-port=22/tcp"},
            {"id": "D", "text": "iptables -F"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ufw allow 22/tcp (equivalently 'ufw allow ssh') permits inbound TCP port 22 "
                       "through the firewall.",
            "distractors": {
                "B": "ufw deny 22/tcp BLOCKS SSH, the opposite of the goal.",
                "C": "firewall-cmd manages firewalld (RHEL), not ufw.",
                "D": "iptables -F FLUSHES all rules, removing protections rather than allowing SSH specifically.",
            },
            "exam_pattern": "ufw allow/deny <port>/<proto> or a service name; enable with 'ufw enable'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Host firewall (ufw)"],
    },
    {
        "id": "linuxplus-sec-012", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "fill",
        "stem": "Which packet-filtering framework is the modern successor to iptables in the Linux "
                "kernel and is managed with the 'nft' command? (framework name)",
        "correct": ["nftables", "nft"],
        "explanation": {
            "correct": "nftables replaces the iptables/ip6tables/arptables/ebtables family with a single "
                       "framework and the 'nft' tool. firewalld and ufw can both use it as their back end.",
            "distractors": {},
            "exam_pattern": "iptables -> nftables (nft); higher-level managers firewalld/ufw sit on top.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Packet filtering (nftables)"],
    },

    # ===== linuxp_ssh_hardening =============================================
    {
        "id": "linuxplus-sec-013", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 1, "type": "mcq",
        "stem": "To harden SSH, an administrator wants to stop the root account from logging in directly "
                "over SSH. Which sshd_config directive accomplishes this?",
        "options": [
            {"id": "A", "text": "PermitRootLogin no"},
            {"id": "B", "text": "AllowRootLogin no"},
            {"id": "C", "text": "PermitRootLogin yes"},
            {"id": "D", "text": "RootLogin deny"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PermitRootLogin no in /etc/ssh/sshd_config blocks direct root SSH logins; restart "
                       "sshd for it to take effect. Admins then log in as a normal user and escalate with sudo.",
            "distractors": {
                "B": "AllowRootLogin is not a valid sshd_config directive.",
                "C": "PermitRootLogin yes explicitly ALLOWS root login, the opposite of hardening.",
                "D": "RootLogin deny is not a real directive and would be ignored or cause an error.",
            },
            "exam_pattern": "Key sshd_config hardening: PermitRootLogin no, PasswordAuthentication no, use keys.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH hardening (sshd_config)"],
    },
    {
        "id": "linuxplus-sec-014", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Which command installs your SSH public key into a remote server's ~/.ssh/authorized_keys "
                "file so you can use key-based authentication?",
        "options": [
            {"id": "A", "text": "ssh-keygen -t ed25519"},
            {"id": "B", "text": "ssh-copy-id user@server"},
            {"id": "C", "text": "scp ~/.ssh/id_ed25519 user@server:"},
            {"id": "D", "text": "ssh-add ~/.ssh/id_ed25519"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ssh-copy-id appends your PUBLIC key to the remote account's authorized_keys with "
                       "correct permissions, enabling passwordless key-based login.",
            "distractors": {
                "A": "ssh-keygen GENERATES a local key pair; it does not copy anything to the server.",
                "C": "This copies your PRIVATE key (id_ed25519) to the server — insecure and not how key auth works.",
                "D": "ssh-add loads a private key into the local ssh-agent; it does not touch the server.",
            },
            "exam_pattern": "Key auth flow: ssh-keygen (create) -> ssh-copy-id (publish public key) -> ssh in.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Key-based auth (ssh-copy-id)"],
    },
    {
        "id": "linuxplus-sec-015", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 1, "type": "fill",
        "stem": "Which file holds the configuration for the OpenSSH server daemon — the file where "
                "directives such as PermitRootLogin and PasswordAuthentication are set? (full path)",
        "correct": ["/etc/ssh/sshd_config", "etc/ssh/sshd_config"],
        "explanation": {
            "correct": "/etc/ssh/sshd_config configures the SSH server (sshd). Do not confuse it with "
                       "/etc/ssh/ssh_config, which configures the SSH CLIENT.",
            "distractors": {},
            "exam_pattern": "Server = sshd_config (with the 'd'); client = ssh_config. Restart sshd after edits.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH server config (sshd_config)"],
    },

    # ===== linuxp_crypto_certs ==============================================
    {
        "id": "linuxplus-sec-016", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 2, "type": "mcq",
        "stem": "A LUKS-encrypted block device /dev/sdb1 must be unlocked and exposed as "
                "/dev/mapper/secure so it can be mounted. Which command does this?",
        "options": [
            {"id": "A", "text": "cryptsetup luksFormat /dev/sdb1"},
            {"id": "B", "text": "mount /dev/sdb1 /mnt/secure"},
            {"id": "C", "text": "cryptsetup luksOpen /dev/sdb1 secure"},
            {"id": "D", "text": "gpg --decrypt /dev/sdb1"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "cryptsetup luksOpen /dev/sdb1 secure (also 'cryptsetup open') prompts for the "
                       "passphrase and creates the decrypted mapping /dev/mapper/secure, which you then mount.",
            "distractors": {
                "A": "luksFormat INITIALIZES a new LUKS header on the device, destroying any existing data.",
                "B": "You cannot mount a LUKS device directly; it must be unlocked first.",
                "D": "gpg encrypts/decrypts files, not LUKS block devices.",
            },
            "exam_pattern": "LUKS flow: luksFormat (once) -> luksOpen (unlock to /dev/mapper) -> mount; luksClose to lock.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Disk encryption (LUKS/cryptsetup)"],
    },
    {
        "id": "linuxplus-sec-017", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 2, "type": "mcq",
        "stem": "Which command uses GnuPG to encrypt report.pdf with public-key cryptography so that "
                "only the recipient alice@example.com can decrypt it?",
        "options": [
            {"id": "A", "text": "gpg --encrypt --recipient alice@example.com report.pdf"},
            {"id": "B", "text": "gpg --symmetric report.pdf"},
            {"id": "C", "text": "gpg --decrypt report.pdf"},
            {"id": "D", "text": "openssl enc -aes-256-cbc -in report.pdf -out report.enc"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "gpg --encrypt --recipient alice@example.com (short: gpg -e -r) encrypts to alice's "
                       "PUBLIC key, so only her matching private key can decrypt it.",
            "distractors": {
                "B": "gpg --symmetric uses a shared passphrase, not the recipient's public key.",
                "C": "gpg --decrypt reverses encryption; it does not protect the file.",
                "D": "openssl enc performs passphrase-based SYMMETRIC encryption, not recipient public-key encryption.",
            },
            "exam_pattern": "gpg -e -r <recipient> = asymmetric (public key); gpg -c / openssl enc = symmetric (passphrase).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Encryption tools (GnuPG)"],
    },
    {
        "id": "linuxplus-sec-018", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 3, "type": "mcq",
        "stem": "An administrator needs to inspect the subject, issuer, and validity dates of an X.509 "
                "certificate stored in server.crt. Which OpenSSL command displays those details?",
        "options": [
            {"id": "A", "text": "openssl genrsa -out server.key 2048"},
            {"id": "B", "text": "openssl x509 -in server.crt -noout -text"},
            {"id": "C", "text": "openssl req -in server.crt -noout -text"},
            {"id": "D", "text": "openssl s_client -connect server.crt:443"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "openssl x509 parses an X.509 certificate; -in names the file, -text prints the "
                       "human-readable fields (subject, issuer, validity, SAN), and -noout suppresses the raw PEM.",
            "distractors": {
                "A": "openssl genrsa GENERATES a private key; it does not read a certificate.",
                "C": "openssl req parses a certificate signing request (CSR), not a finished certificate.",
                "D": "openssl s_client connects to a live TLS server host:port; server.crt is a file, not a host.",
            },
            "exam_pattern": "Inspect a cert file: openssl x509 -in <file> -noout -text; a CSR: openssl req ...",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Certificates (OpenSSL x509)"],
    },
]
