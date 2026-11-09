"""CompTIA Linux+ (XK0-005) pool - Domain 1: System Management.

Original, objective-aligned practice items for the seven System Management
subtopics tracked in CertLab:
  * linuxp_filesystem        - FHS layout and core file operations (ls/cd/cp/mv/
                               find/df/du), /etc, /var, /proc.
  * linuxp_package_mgmt      - Debian (apt/apt-get/dpkg) and RHEL (dnf/yum/rpm)
                               package tooling plus flatpak/snap.
  * linuxp_processes_services- ps/top/kill/nice/renice and systemd (systemctl,
                               journalctl, targets), cron/at/systemd timers.
  * linuxp_users_groups      - useradd/usermod/passwd/groupadd and the account
                               databases /etc/passwd, /etc/shadow, /etc/group.
  * linuxp_storage_lvm       - partitioning, filesystems, fstab, and LVM
                               (pvcreate/vgcreate/lvcreate/lvextend), RAID/mdadm.
  * linuxp_networking_config - ip/ss/nmcli, /etc/hosts, resolv.conf, hostnamectl.
  * linuxp_boot_kernel       - GRUB2, /boot, kernel modules (lsmod/modprobe),
                               dmesg, and runtime kernel tuning via sysctl.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer key is not positionally
biased, every wrong option carries a distractor note, and each item cites the
public XK0-005 objective domain it draws on. Commands, flags, and file paths are
real and version-resilient across mainstream RHEL/Fedora and Debian/Ubuntu
systems (true across XK0-005/006); no memorized or real exam items are used.
"""

QUESTIONS = [
    # ===== linuxp_filesystem ================================================
    {
        "id": "linuxplus-sys-001", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 1, "type": "fill",
        "stem": "According to the Filesystem Hierarchy Standard (FHS), which single top-level "
                "directory is the standard location for host-specific, system-wide configuration "
                "files such as fstab and passwd? (full path)",
        "correct": ["/etc", "etc"],
        "explanation": {
            "correct": "/etc holds host-specific, system-wide configuration files (for example "
                       "/etc/fstab, /etc/passwd, /etc/ssh/sshd_config). Per the FHS it must contain no "
                       "binaries.",
            "distractors": {},
            "exam_pattern": "System-wide config = /etc; variable data = /var; kernel/process view = /proc.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Filesystem Hierarchy Standard"],
    },
    {
        "id": "linuxplus-sys-002", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 2, "type": "mcq",
        "stem": "An administrator must list every file under /home that was modified within the last "
                "24 hours (less than one day ago). Which command does this?",
        "options": [
            {"id": "A", "text": "find /home -mtime +1"},
            {"id": "B", "text": "find /home -atime -1"},
            {"id": "C", "text": "find /home -mtime -1"},
            {"id": "D", "text": "find /home -ctime 1"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "-mtime -1 matches files whose data was last modified less than 1 day (24 hours) "
                       "ago. The leading minus means 'less than'.",
            "distractors": {
                "A": "-mtime +1 matches files modified MORE than one day ago, the opposite window.",
                "B": "-atime refers to last access time, not modification time.",
                "D": "-ctime 1 matches inode-change time exactly between 24 and 48 hours ago, not the last day.",
            },
            "exam_pattern": "find time tests: -mtime=modified, -atime=accessed, -ctime=inode change; "
                            "-N = within N days, +N = more than N days.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Manage files and directories (find)"],
    },
    {
        "id": "linuxplus-sys-003", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 1, "type": "mcq",
        "stem": "You need a quick, human-readable summary of how much space is used and still free on "
                "each mounted filesystem. Which command is best suited?",
        "options": [
            {"id": "A", "text": "du -sh /"},
            {"id": "B", "text": "df -h"},
            {"id": "C", "text": "df -i"},
            {"id": "D", "text": "lsblk -f"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "df reports per-filesystem disk space; -h prints sizes in human-readable units "
                       "(G/M/K) and shows used, available, and use% for each mount point.",
            "distractors": {
                "A": "du -sh / sums the size of files under a path (slow on /) and does not report free space per filesystem.",
                "C": "df -i reports inode counts, not space used/free in bytes.",
                "D": "lsblk -f shows filesystem type, label, UUID, and mountpoint but not used/free capacity.",
            },
            "exam_pattern": "df = free space per filesystem; du = size consumed by files/dirs.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Monitor storage (df/du)"],
    },

    # ===== linuxp_package_mgmt ==============================================
    {
        "id": "linuxplus-sys-004", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 1, "type": "mcq",
        "stem": "On an Ubuntu server, which command installs the nginx package from the configured "
                "repositories, automatically resolving and installing its dependencies?",
        "options": [
            {"id": "A", "text": "apt install nginx"},
            {"id": "B", "text": "rpm -i nginx"},
            {"id": "C", "text": "dpkg -i nginx"},
            {"id": "D", "text": "yum install nginx"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "apt (and apt-get) is the high-level Debian/Ubuntu package manager: it pulls the "
                       "package from configured repos and resolves dependencies automatically.",
            "distractors": {
                "B": "rpm is the RHEL-family low-level tool and is not used on Debian/Ubuntu.",
                "C": "dpkg installs a local .deb file and does NOT resolve repository dependencies (and nginx here is a repo name, not a file).",
                "D": "yum is the RHEL/CentOS package manager, not available on Ubuntu by default.",
            },
            "exam_pattern": "Debian/Ubuntu: apt/apt-get/dpkg. RHEL/Fedora: dnf/yum/rpm.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Software management (apt)"],
    },
    {
        "id": "linuxplus-sys-005", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "On a RHEL 9 host, which command queries the local RPM database to confirm whether the "
                "httpd package is installed and, if so, its version?",
        "options": [
            {"id": "A", "text": "dpkg -l httpd"},
            {"id": "B", "text": "apt list httpd"},
            {"id": "C", "text": "yum repoquery httpd"},
            {"id": "D", "text": "rpm -q httpd"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "rpm -q httpd queries the installed RPM database and prints the installed "
                       "package-version-release, or reports 'package httpd is not installed'.",
            "distractors": {
                "A": "dpkg is a Debian tool and its database does not exist on RHEL.",
                "B": "apt is a Debian/Ubuntu tool, not present on RHEL by default.",
                "C": "repoquery inspects what is AVAILABLE in repositories, not specifically what is installed locally.",
            },
            "exam_pattern": "rpm -q = query installed; -qa lists all; -ql lists a package's files; -qf finds the owning package.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Software management (rpm)"],
    },
    {
        "id": "linuxplus-sys-006", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "On a Debian system, which command lists every file that the already-installed "
                "coreutils package placed on the filesystem?",
        "options": [
            {"id": "A", "text": "dpkg -S coreutils"},
            {"id": "B", "text": "dpkg -L coreutils"},
            {"id": "C", "text": "dpkg -l coreutils"},
            {"id": "D", "text": "apt-cache show coreutils"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "dpkg -L <package> lists the files installed by that package (its file manifest).",
            "distractors": {
                "A": "dpkg -S searches for the package that OWNS a given file path, the reverse lookup.",
                "C": "dpkg -l (lowercase L) lists package status/version, not the installed files.",
                "D": "apt-cache show prints package metadata (description, dependencies), not the installed file list.",
            },
            "exam_pattern": "dpkg -L = list files of a package; dpkg -S = which package owns a file.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Software management (dpkg)"],
    },

    # ===== linuxp_processes_services ========================================
    {
        "id": "linuxplus-sys-007", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 2, "type": "mcq",
        "stem": "You need the sshd service to start automatically on every boot, but you do not need to "
                "start it in this moment. Which systemd command accomplishes exactly that?",
        "options": [
            {"id": "A", "text": "systemctl start sshd"},
            {"id": "B", "text": "systemctl mask sshd"},
            {"id": "C", "text": "systemctl enable sshd"},
            {"id": "D", "text": "systemctl status sshd"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "systemctl enable sshd creates the boot-time symlinks so the unit starts on every "
                       "boot; it does not start the service now (use enable --now to do both).",
            "distractors": {
                "A": "systemctl start sshd starts it immediately but does NOT persist across reboots.",
                "B": "systemctl mask sshd makes the unit impossible to start by linking it to /dev/null.",
                "D": "systemctl status sshd only reports the current state; it changes nothing.",
            },
            "exam_pattern": "enable = start at boot; start = start now; enable --now = both; mask = block entirely.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Manage services (systemctl)"],
    },
    {
        "id": "linuxplus-sys-008", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 2, "type": "mcq",
        "stem": "Which command displays only the journal log entries produced by the nginx.service "
                "systemd unit?",
        "options": [
            {"id": "A", "text": "journalctl -u nginx.service"},
            {"id": "B", "text": "journalctl -b"},
            {"id": "C", "text": "journalctl -k"},
            {"id": "D", "text": "tail -f /var/log/nginx.service"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "journalctl -u nginx.service filters the systemd journal to messages from that "
                       "specific unit; add -f to follow in real time.",
            "distractors": {
                "B": "journalctl -b shows all messages from the current boot, not one unit.",
                "C": "journalctl -k shows only kernel ring-buffer messages.",
                "D": "/var/log/nginx.service is not a real log file; journald stores unit logs, not a file by that name.",
            },
            "exam_pattern": "journalctl -u <unit> filters by unit; -b by boot; -k kernel; -f to follow.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Service logs (journalctl)"],
    },
    {
        "id": "linuxplus-sys-009", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 3, "type": "mcq",
        "stem": "A running process with PID 1450 is monopolizing the CPU. Which command lowers its "
                "scheduling priority (makes it 'nicer') while it continues to run?",
        "options": [
            {"id": "A", "text": "nice -n 10 -p 1450"},
            {"id": "B", "text": "kill -STOP 1450"},
            {"id": "C", "text": "renice -n -10 -p 1450"},
            {"id": "D", "text": "renice -n 10 -p 1450"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "renice changes the niceness of an EXISTING process. -n 10 raises the nice value "
                       "to 10 (a higher nice value means lower priority), and -p 1450 targets that PID.",
            "distractors": {
                "A": "nice launches a NEW command with a niceness; it does not accept a -p PID to adjust a running process.",
                "B": "kill -STOP suspends the process entirely rather than merely lowering its priority.",
                "C": "A negative nice value (-10) RAISES priority (needs root), the opposite of 'nicer'.",
            },
            "exam_pattern": "nice starts a process with a priority; renice changes a running one. Higher nice = lower priority.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Process priority (nice/renice)"],
    },
    {
        "id": "linuxplus-sys-010", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 1, "type": "fill",
        "stem": "Which command, present on virtually every Linux distribution by default, shows a "
                "real-time, continuously updating list of running processes with their CPU and memory "
                "usage? (command name only)",
        "correct": ["top", "/usr/bin/top"],
        "explanation": {
            "correct": "top provides a live, self-refreshing view of processes sorted by resource use and "
                       "is installed by default nearly everywhere. (htop is similar but often must be installed.)",
            "distractors": {},
            "exam_pattern": "top = built-in live process monitor; htop = enhanced but usually not preinstalled.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Monitor processes (top)"],
    },

    # ===== linuxp_users_groups ==============================================
    {
        "id": "linuxplus-sys-011", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 2, "type": "mcq",
        "stem": "Which command creates a new user named 'deploy', creates its home directory, and sets "
                "its login shell to /bin/bash?",
        "options": [
            {"id": "A", "text": "useradd -M -s /bin/bash deploy"},
            {"id": "B", "text": "useradd -m -s /bin/bash deploy"},
            {"id": "C", "text": "usermod -m -s /bin/bash deploy"},
            {"id": "D", "text": "groupadd -m deploy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "useradd -m creates the home directory and -s sets the login shell; this both "
                       "creates the account and configures its shell in one command.",
            "distractors": {
                "A": "-M (uppercase) explicitly tells useradd NOT to create the home directory.",
                "C": "usermod modifies an EXISTING user; it cannot create one, and -m there means move an existing home.",
                "D": "groupadd creates a group, not a user account.",
            },
            "exam_pattern": "useradd -m creates home; -s sets shell; -M suppresses home creation.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Manage users (useradd)"],
    },
    {
        "id": "linuxplus-sys-012", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 1, "type": "mcq",
        "stem": "In which file does a Linux system store users' hashed passwords and password-aging "
                "data, readable only by root?",
        "options": [
            {"id": "A", "text": "/etc/shadow"},
            {"id": "B", "text": "/etc/passwd"},
            {"id": "C", "text": "/etc/group"},
            {"id": "D", "text": "/etc/gshadow"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "/etc/shadow stores each account's hashed password and aging fields (last change, "
                       "min/max age, expiration) and is readable only by root.",
            "distractors": {
                "B": "/etc/passwd holds account attributes (UID, GID, home, shell) and shows 'x' where the hash used to be.",
                "C": "/etc/group defines groups and their members, not password hashes.",
                "D": "/etc/gshadow stores GROUP passwords and admins, not individual user password hashes.",
            },
            "exam_pattern": "passwd = account info (world-readable); shadow = hashes + aging (root-only).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Account databases (/etc/shadow)"],
    },
    {
        "id": "linuxplus-sys-013", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 3, "type": "mcq",
        "stem": "User 'maria' already exists and belongs to several groups. Which command adds her to "
                "the supplementary group 'docker' WITHOUT removing her from any of her current groups?",
        "options": [
            {"id": "A", "text": "usermod -G docker maria"},
            {"id": "B", "text": "useradd -G docker maria"},
            {"id": "C", "text": "usermod -aG docker maria"},
            {"id": "D", "text": "gpasswd -d maria docker"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "usermod -aG appends (-a) the user to the listed supplementary group(s) (-G), "
                       "preserving existing memberships.",
            "distractors": {
                "A": "usermod -G WITHOUT -a REPLACES all of maria's supplementary groups with just 'docker' — a classic trap.",
                "B": "useradd tries to CREATE a new account and fails because maria already exists.",
                "D": "gpasswd -d REMOVES maria from the docker group, the opposite of the goal.",
            },
            "exam_pattern": "Always use -aG together to add a user to a group; -G alone overwrites group membership.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Manage groups (usermod)"],
    },

    # ===== linuxp_storage_lvm ===============================================
    {
        "id": "linuxplus-sys-014", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 2, "type": "mcq",
        "stem": "An LVM logical volume /dev/vg0/data needs to grow by 5 GB using free space already in "
                "its volume group. Which command extends the logical volume itself?",
        "options": [
            {"id": "A", "text": "vgextend vg0 /dev/sdb1"},
            {"id": "B", "text": "lvcreate -L 5G vg0"},
            {"id": "C", "text": "lvextend -L +5G /dev/vg0/data"},
            {"id": "D", "text": "resize2fs /dev/vg0/data 5G"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "lvextend -L +5G adds 5 GB to the logical volume from free extents in the volume "
                       "group. Add -r (or follow with resize2fs/xfs_growfs) to grow the filesystem too.",
            "distractors": {
                "A": "vgextend adds a new physical volume to a volume group; it does not resize a logical volume.",
                "B": "lvcreate makes a NEW logical volume rather than extending the existing one.",
                "D": "resize2fs resizes the FILESYSTEM, and '5G' here would shrink it to 5 GB total, not add 5 GB.",
            },
            "exam_pattern": "LVM growth: lvextend -L +SIZE, then grow the filesystem (lvextend -r does both).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Logical Volume Manager (lvextend)"],
    },
    {
        "id": "linuxplus-sys-015", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 3, "type": "multi",
        "stem": "A new disk /dev/sdc will host an LVM logical volume. Which THREE commands, run in "
                "order, build the LVM stack from the raw disk up to a usable logical volume? (Choose three.)",
        "options": [
            {"id": "A", "text": "pvcreate /dev/sdc"},
            {"id": "B", "text": "vgcreate vg1 /dev/sdc"},
            {"id": "C", "text": "lvcreate -n lv1 -L 10G vg1"},
            {"id": "D", "text": "mkfs.ext4 /dev/sdc"},
        ],
        "correct": ["A", "B", "C"],
        "explanation": {
            "correct": "LVM is layered: pvcreate initializes the disk as a physical volume, vgcreate "
                       "groups it into a volume group, and lvcreate carves a logical volume out of that group.",
            "distractors": {
                "D": "Running mkfs.ext4 directly on /dev/sdc formats the RAW disk and bypasses LVM entirely; "
                     "you instead format the resulting logical volume (e.g., /dev/vg1/lv1).",
            },
            "exam_pattern": "LVM build order: pvcreate -> vgcreate -> lvcreate -> mkfs on the LV.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — LVM provisioning (pvcreate/vgcreate/lvcreate)"],
    },
    {
        "id": "linuxplus-sys-016", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 2, "type": "fill",
        "stem": "Which configuration file does the system read at boot to determine which filesystems "
                "to mount, where, and with which options? (full path)",
        "correct": ["/etc/fstab", "etc/fstab"],
        "explanation": {
            "correct": "/etc/fstab lists filesystems (by device, UUID, or label), their mount points, "
                       "filesystem type, options, and dump/fsck order used at boot and by 'mount -a'.",
            "distractors": {},
            "exam_pattern": "Persistent mounts live in /etc/fstab; prefer UUID= or LABEL= over device names.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Filesystem mounting (/etc/fstab)"],
    },

    # ===== linuxp_networking_config =========================================
    {
        "id": "linuxplus-sys-017", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "Using the modern iproute2 suite, which command displays the IP addresses assigned to "
                "all network interfaces?",
        "options": [
            {"id": "A", "text": "ss -tln"},
            {"id": "B", "text": "ip addr show"},
            {"id": "C", "text": "ifconfig -a"},
            {"id": "D", "text": "nmcli radio wifi"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ip addr show (iproute2; abbreviated 'ip a') lists every interface with its IPv4 "
                       "and IPv6 addresses, state, and MAC.",
            "distractors": {
                "A": "ss -tln lists listening TCP sockets, not interface addresses.",
                "C": "ifconfig is the deprecated net-tools command and may be absent on modern systems.",
                "D": "nmcli radio wifi only reports the Wi-Fi radio on/off state.",
            },
            "exam_pattern": "iproute2 replaces net-tools: ip addr (ifconfig), ip route (route), ss (netstat).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Network configuration (ip)"],
    },
    {
        "id": "linuxplus-sys-018", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "Which command shows all listening TCP sockets together with the processes that own "
                "them, serving as the modern replacement for netstat?",
        "options": [
            {"id": "A", "text": "ss -tlnp"},
            {"id": "B", "text": "ip route show"},
            {"id": "C", "text": "netstat -r"},
            {"id": "D", "text": "ping -c 4 localhost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ss -tlnp shows TCP (-t) listening (-l) sockets with numeric (-n) ports and the "
                       "owning process (-p); ss is the iproute2 successor to netstat.",
            "distractors": {
                "B": "ip route show prints the routing table, not open sockets.",
                "C": "netstat -r prints the routing table (and netstat is the older, deprecated tool).",
                "D": "ping tests reachability; it does not list listening sockets.",
            },
            "exam_pattern": "ss flags: -t TCP, -u UDP, -l listening, -n numeric, -p process.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Network sockets (ss)"],
    },
    {
        "id": "linuxplus-sys-019", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 1, "type": "fill",
        "stem": "Which file traditionally lists the DNS nameserver IP addresses that a Linux host uses "
                "to resolve hostnames? (full path)",
        "correct": ["/etc/resolv.conf", "etc/resolv.conf"],
        "explanation": {
            "correct": "/etc/resolv.conf contains 'nameserver' entries (and search/domain lines) the "
                       "resolver uses. On systemd-resolved or NetworkManager hosts it is often generated/"
                       "managed automatically.",
            "distractors": {},
            "exam_pattern": "DNS servers -> /etc/resolv.conf; static name-to-IP overrides -> /etc/hosts.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Name resolution (/etc/resolv.conf)"],
    },

    # ===== linuxp_boot_kernel ===============================================
    {
        "id": "linuxplus-sys-020", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 2, "type": "mcq",
        "stem": "Which command loads a kernel module AND automatically resolves and loads any modules "
                "it depends on?",
        "options": [
            {"id": "A", "text": "rmmod"},
            {"id": "B", "text": "insmod"},
            {"id": "C", "text": "modprobe"},
            {"id": "D", "text": "lsmod"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "modprobe loads a module by name and pulls in its dependencies using modules.dep, "
                       "making it the preferred loader.",
            "distractors": {
                "A": "rmmod UNLOADS a module and does not handle dependencies.",
                "B": "insmod loads a single .ko file directly and does NOT resolve dependencies.",
                "D": "lsmod only lists modules that are already loaded.",
            },
            "exam_pattern": "modprobe = dependency-aware load/unload; insmod/rmmod = raw single-module ops; lsmod = list.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Kernel modules (modprobe)"],
    },
    {
        "id": "linuxplus-sys-021", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 3, "type": "mcq",
        "stem": "An administrator must enable IP forwarding at runtime by setting the kernel parameter "
                "net.ipv4.ip_forward, which lives under /proc/sys. Which command reads and sets such "
                "kernel parameters?",
        "options": [
            {"id": "A", "text": "sysctl"},
            {"id": "B", "text": "dmesg"},
            {"id": "C", "text": "modinfo"},
            {"id": "D", "text": "lsmod"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "sysctl reads and modifies kernel parameters exposed under /proc/sys; e.g., "
                       "'sysctl -w net.ipv4.ip_forward=1' sets it now, and /etc/sysctl.conf (or /etc/sysctl.d/) persists it.",
            "distractors": {
                "B": "dmesg prints the kernel ring-buffer messages; it does not change tunables.",
                "C": "modinfo displays information about a kernel module, not sysctl parameters.",
                "D": "lsmod lists loaded modules and sets nothing.",
            },
            "exam_pattern": "Runtime kernel tunables: sysctl -w (now) + /etc/sysctl.d/*.conf (persistent).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Kernel parameters (sysctl)"],
    },
    {
        "id": "linuxplus-sys-022", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 3, "type": "mcq",
        "stem": "On a RHEL/Fedora system using GRUB2, after editing /etc/default/grub you must rebuild "
                "the bootloader configuration. Which command regenerates it?",
        "options": [
            {"id": "A", "text": "update-grub"},
            {"id": "B", "text": "grub2-mkconfig -o /boot/grub2/grub.cfg"},
            {"id": "C", "text": "grub2-install /dev/sda"},
            {"id": "D", "text": "systemctl daemon-reload"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "On RHEL/Fedora, grub2-mkconfig regenerates the GRUB2 config; -o writes it to "
                       "/boot/grub2/grub.cfg (BIOS) so the edits in /etc/default/grub take effect.",
            "distractors": {
                "A": "update-grub is the Debian/Ubuntu wrapper and is normally absent on RHEL/Fedora.",
                "C": "grub2-install writes the bootloader to a device's boot sector; it does not regenerate grub.cfg.",
                "D": "systemctl daemon-reload reloads systemd unit files, unrelated to GRUB.",
            },
            "exam_pattern": "RHEL: grub2-mkconfig -o /boot/grub2/grub.cfg. Debian: update-grub (wraps grub-mkconfig).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 1 — Boot process (GRUB2)"],
    },
]
