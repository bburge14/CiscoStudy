"""CompTIA Linux+ (XK0-006) pool - Domain 4: Troubleshooting.

Original, objective-aligned practice items for the six Troubleshooting subtopics
tracked in CertLab:
  * linuxp_ts_storage     - disk full vs inode exhaustion, du/df analysis, fsck
                            repair, mount issues, I/O load (iostat).
  * linuxp_ts_network     - connectivity vs DNS vs routing, ping/traceroute/dig,
                            listening sockets (ss), packet capture (tcpdump).
  * linuxp_ts_cpu_memory  - free/vmstat/uptime, the OOM killer, swap, load.
  * linuxp_ts_users_access- permission-denied, locked accounts, group membership.
  * linuxp_ts_services    - systemctl status, journalctl -u, failed units.
  * linuxp_ts_tools       - logs in /var/log, journalctl, strace, lsof.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased,
every wrong option carries a distractor note, and each item cites the public
XK0-006 objective domain it draws on. Commands, flags, and file paths are real
and version-resilient across mainstream RHEL/Fedora and Debian/Ubuntu systems;
no memorized or real exam items are used.
"""

QUESTIONS = [
    # ===== linuxp_ts_storage ================================================
    {
        "id": "linuxplus-ts-001", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "mcq",
        "stem": "A process fails with 'No space left on device', yet 'df -h' shows the filesystem has "
                "plenty of free space. Which command checks the most likely cause?",
        "options": [
            {"id": "A", "text": "free -h"},
            {"id": "B", "text": "lsblk"},
            {"id": "C", "text": "df -i"},
            {"id": "D", "text": "du -h"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "When bytes are free but writes still fail with ENOSPC, the filesystem has likely "
                       "run out of inodes. df -i shows inode totals, used, and free per filesystem.",
            "distractors": {
                "A": "free -h reports RAM and swap, not filesystem inodes.",
                "B": "lsblk lists block devices and mounts but not inode usage.",
                "D": "du -h sums file sizes in bytes; it does not reveal inode exhaustion (millions of tiny files).",
            },
            "exam_pattern": "'No space' but df -h shows free space => check df -i for inode exhaustion.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Storage troubleshooting (inodes)"],
    },
    {
        "id": "linuxplus-ts-002", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "mcq",
        "stem": "The / filesystem is nearly full. Which command best pinpoints which top-level "
                "directories under /var are consuming the most space?",
        "options": [
            {"id": "A", "text": "du -h --max-depth=1 /var | sort -h"},
            {"id": "B", "text": "df -h /var"},
            {"id": "C", "text": "ls -l /var"},
            {"id": "D", "text": "cat /proc/meminfo"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "du -h --max-depth=1 /var reports the size of each immediate subdirectory, and "
                       "'sort -h' orders them by human-readable size so the biggest stands out.",
            "distractors": {
                "B": "df -h /var confirms the filesystem is full but does not break usage down by directory.",
                "C": "ls -l shows entry sizes, not the recursive space consumed by each directory tree.",
                "D": "/proc/meminfo reports memory, which is unrelated to disk usage.",
            },
            "exam_pattern": "Find space hogs with du (per-directory totals); confirm fullness with df.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Storage troubleshooting (du)"],
    },
    {
        "id": "linuxplus-ts-003", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 3, "type": "mcq",
        "stem": "A secondary data filesystem on /dev/sdb1 reports corruption. What is the correct, safe "
                "way to check and repair it?",
        "options": [
            {"id": "A", "text": "Run 'fsck /dev/sdb1' while it is mounted read-write"},
            {"id": "B", "text": "Unmount /dev/sdb1 first, then run 'fsck /dev/sdb1'"},
            {"id": "C", "text": "Run 'mkfs.ext4 /dev/sdb1' to rebuild it"},
            {"id": "D", "text": "Run 'fdisk /dev/sdb1' to repair the filesystem"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "fsck must run on an unmounted (or read-only) filesystem; checking a mounted, "
                       "actively-written filesystem can worsen corruption. Unmount, then fsck.",
            "distractors": {
                "A": "Running fsck on a mounted read-write filesystem risks further corruption and is unsafe.",
                "C": "mkfs.ext4 creates a NEW filesystem, erasing all data rather than repairing it.",
                "D": "fdisk edits the PARTITION TABLE; it does not check or repair filesystem structures.",
            },
            "exam_pattern": "fsck only on unmounted/read-only filesystems; the root fs is checked at boot.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Filesystem repair (fsck)"],
    },
    {
        "id": "linuxplus-ts-004", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "fill",
        "stem": "Which command from the sysstat package reports CPU usage together with per-device disk "
                "I/O statistics (tps, kB_read/s, kB_wrtn/s), useful for spotting a disk I/O bottleneck? "
                "(command name only)",
        "correct": ["iostat", "/usr/bin/iostat"],
        "explanation": {
            "correct": "iostat (from sysstat) shows CPU utilization and per-device I/O throughput and "
                       "transfers per second; high %iowait plus busy devices points to an I/O bottleneck.",
            "distractors": {},
            "exam_pattern": "Disk I/O load: iostat (and iotop for per-process I/O); high %iowait = waiting on storage.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — I/O performance (iostat)"],
    },

    # ===== linuxp_ts_network ================================================
    {
        "id": "linuxplus-ts-005", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "A server reaches 8.8.8.8 by IP but cannot open http://example.com, failing to resolve "
                "the name. Which command best confirms the DNS resolution problem?",
        "options": [
            {"id": "A", "text": "ping 8.8.8.8"},
            {"id": "B", "text": "dig example.com"},
            {"id": "C", "text": "ip addr show"},
            {"id": "D", "text": "traceroute 8.8.8.8"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "dig example.com queries DNS directly and shows whether the name resolves and which "
                       "server answered; a failure here confirms a DNS problem (nslookup works similarly).",
            "distractors": {
                "A": "ping 8.8.8.8 tests IP reachability, which the scenario already says works.",
                "C": "ip addr show lists local interface addresses, not name resolution.",
                "D": "traceroute to an IP maps the path but does not test hostname resolution.",
            },
            "exam_pattern": "Works by IP but not by name => DNS issue. Test with dig/nslookup; check /etc/resolv.conf.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (DNS/dig)"],
    },
    {
        "id": "linuxplus-ts-006", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "After starting a web service you must confirm that something is actually listening on "
                "TCP port 443. Which command shows the listening sockets and their ports?",
        "options": [
            {"id": "A", "text": "ping localhost"},
            {"id": "B", "text": "dig localhost"},
            {"id": "C", "text": "ss -tlnp"},
            {"id": "D", "text": "ip route"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "ss -tlnp lists listening (-l) TCP (-t) sockets with numeric (-n) ports and the "
                       "owning process (-p); look for :443 to confirm the service is bound.",
            "distractors": {
                "A": "ping tests ICMP reachability to a host, not whether a port is open.",
                "B": "dig performs DNS lookups; it says nothing about listening ports.",
                "D": "ip route shows the routing table, unrelated to open sockets.",
            },
            "exam_pattern": "Confirm a service is bound/listening with ss -tlnp (modern netstat replacement).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (ss)"],
    },
    {
        "id": "linuxplus-ts-007", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "Traffic to a remote network fails somewhere in transit. Which command shows the "
                "hop-by-hop path packets take toward the destination to locate where it breaks?",
        "options": [
            {"id": "A", "text": "ss -s"},
            {"id": "B", "text": "arp -a"},
            {"id": "C", "text": "nmcli general status"},
            {"id": "D", "text": "traceroute 203.0.113.10"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "traceroute (or tracepath) lists each router hop toward the destination and the "
                       "latency to it, revealing where the path stops responding.",
            "distractors": {
                "A": "ss -s prints socket summary statistics, not a network path.",
                "B": "arp -a shows the local ARP cache (layer-2 neighbors), not the route to a remote host.",
                "C": "nmcli general status reports NetworkManager's overall state, not a hop-by-hop path.",
            },
            "exam_pattern": "Locate where routing/connectivity breaks along a path with traceroute/tracepath/mtr.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (traceroute)"],
    },
    {
        "id": "linuxplus-ts-008", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "fill",
        "stem": "Which command-line tool captures live network packets on an interface (for example "
                "'<tool> -i eth0 port 443') so traffic can be inspected during troubleshooting? "
                "(command name only)",
        "correct": ["tcpdump", "/usr/sbin/tcpdump"],
        "explanation": {
            "correct": "tcpdump captures and displays packets on a chosen interface with optional filters "
                       "(host, port, protocol), making it the standard CLI packet analyzer.",
            "distractors": {},
            "exam_pattern": "Packet capture: tcpdump (CLI) or Wireshark/tshark (GUI); filter with BPF expressions.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (tcpdump)"],
    },

    # ===== linuxp_ts_cpu_memory =============================================
    {
        "id": "linuxplus-ts-009", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 1, "type": "mcq",
        "stem": "Which command displays total, used, and available RAM and swap in human-readable units "
                "for a quick memory check?",
        "options": [
            {"id": "A", "text": "free -h"},
            {"id": "B", "text": "df -h"},
            {"id": "C", "text": "lscpu"},
            {"id": "D", "text": "uptime"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "free -h summarizes physical memory and swap (total/used/free/available) in "
                       "human-readable units.",
            "distractors": {
                "B": "df -h reports disk space, not memory.",
                "C": "lscpu prints CPU architecture details, not memory usage.",
                "D": "uptime shows load averages and how long the system has run, not memory figures.",
            },
            "exam_pattern": "Memory snapshot: free -h; watch the 'available' column, not just 'free'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Memory troubleshooting (free)"],
    },
    {
        "id": "linuxplus-ts-010", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 3, "type": "mcq",
        "stem": "A critical daemon was killed abruptly when the system ran out of memory. Where is the "
                "most direct evidence that the kernel's OOM killer terminated it?",
        "options": [
            {"id": "A", "text": "/etc/passwd"},
            {"id": "B", "text": "The kernel log, via 'dmesg' or 'journalctl -k' (look for 'Out of memory: Killed process')"},
            {"id": "C", "text": "The output of 'df -i'"},
            {"id": "D", "text": "The crontab of the process owner"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The OOM killer logs to the kernel ring buffer. dmesg or 'journalctl -k' shows "
                       "lines such as 'Out of memory: Killed process <pid> (<name>)' with a memory summary.",
            "distractors": {
                "A": "/etc/passwd lists user accounts and has nothing to do with OOM events.",
                "C": "df -i shows inode usage, unrelated to memory-driven process kills.",
                "D": "A crontab holds scheduled jobs, not kernel OOM records.",
            },
            "exam_pattern": "Process vanished + low memory => check dmesg/journalctl -k for OOM-killer messages.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Memory troubleshooting (OOM killer)"],
    },
    {
        "id": "linuxplus-ts-011", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 2, "type": "mcq",
        "stem": "Which command samples and reports system activity (processes, memory, paging, block "
                "I/O, and CPU) repeatedly at a set interval, e.g. every 2 seconds?",
        "options": [
            {"id": "A", "text": "uptime"},
            {"id": "B", "text": "ps aux"},
            {"id": "C", "text": "nproc"},
            {"id": "D", "text": "vmstat 2"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "vmstat 2 prints a new line every 2 seconds covering run queue, memory, swap in/out, "
                       "block I/O, and CPU split (us/sy/id/wa), good for spotting swapping or CPU pressure.",
            "distractors": {
                "A": "uptime gives a one-time load-average snapshot, not interval sampling of these metrics.",
                "B": "ps aux is a single-moment process listing, not a repeating system-activity report.",
                "C": "nproc just prints the number of processing units available.",
            },
            "exam_pattern": "vmstat <interval> for ongoing CPU/memory/paging trends; high 'wa' = I/O wait, high 'si/so' = swapping.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Performance troubleshooting (vmstat)"],
    },

    # ===== linuxp_ts_users_access ===========================================
    {
        "id": "linuxplus-ts-012", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 2, "type": "mcq",
        "stem": "A user reports 'Permission denied' when opening /data/report.txt. Which command should "
                "you run FIRST to diagnose the cause?",
        "options": [
            {"id": "A", "text": "cat /data/report.txt"},
            {"id": "B", "text": "chmod 777 /data/report.txt"},
            {"id": "C", "text": "ls -l /data/report.txt"},
            {"id": "D", "text": "whoami"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "ls -l shows the file's permission bits, owner, and group, letting you compare them "
                       "against the user's identity to find why access is denied before changing anything.",
            "distractors": {
                "A": "cat just reproduces the same 'Permission denied' error without diagnosing it.",
                "B": "chmod 777 recklessly opens the file to everyone before you understand the problem — a security risk.",
                "D": "whoami shows YOUR username but not the file's permissions or ownership.",
            },
            "exam_pattern": "Diagnose access issues with ls -l (perms/owner) and id (user's UID/groups) before editing perms.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Access troubleshooting (permissions)"],
    },
    {
        "id": "linuxplus-ts-013", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 2, "type": "mcq",
        "stem": "An account cannot log in and you suspect its password is locked. Which command displays "
                "the password/lock status of user 'jdoe'?",
        "options": [
            {"id": "A", "text": "passwd jdoe"},
            {"id": "B", "text": "usermod -L jdoe"},
            {"id": "C", "text": "id jdoe"},
            {"id": "D", "text": "passwd -S jdoe"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "passwd -S jdoe reports the account's status, including whether the password is "
                       "Locked (L), usable/Password set (P), or there is No Password (NP).",
            "distractors": {
                "A": "passwd jdoe starts CHANGING the user's password rather than reporting its status.",
                "B": "usermod -L LOCKS the account; it does not display status.",
                "C": "id jdoe shows UID, GID, and groups but nothing about the password lock state.",
            },
            "exam_pattern": "Check lock status with 'passwd -S' (or 'chage -l' for aging); lock/unlock with usermod -L/-U.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Account troubleshooting (passwd -S)"],
    },
    {
        "id": "linuxplus-ts-014", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 1, "type": "fill",
        "stem": "When an access problem may stem from group membership, which command displays a user's "
                "UID, primary GID, and all supplementary groups? (command name only)",
        "correct": ["id", "/usr/bin/id"],
        "explanation": {
            "correct": "id prints the user's UID, primary group, and every supplementary group; a missing "
                       "group here often explains why a user cannot access group-restricted resources.",
            "distractors": {},
            "exam_pattern": "Verify effective identity and groups with id; 'groups' lists just the group names.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Access troubleshooting (id/groups)"],
    },

    # ===== linuxp_ts_services ===============================================
    {
        "id": "linuxplus-ts-015", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 2, "type": "mcq",
        "stem": "A service will not come up. Which command shows whether its systemd unit is active or "
                "failed, along with its main PID and the most recent log lines?",
        "options": [
            {"id": "A", "text": "systemctl status nginx"},
            {"id": "B", "text": "systemctl list-unit-files"},
            {"id": "C", "text": "systemctl daemon-reload"},
            {"id": "D", "text": "systemctl isolate multi-user.target"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "systemctl status <unit> reports the active/failed state, whether it is enabled, "
                       "the main PID, and a tail of the unit's recent journal entries — the first stop in diagnosis.",
            "distractors": {
                "B": "list-unit-files lists all units and their enablement state, not one unit's live status/logs.",
                "C": "daemon-reload re-reads unit files after edits; it does not report a service's state.",
                "D": "isolate switches the system to a different target; it does not diagnose a unit.",
            },
            "exam_pattern": "First step for a failing service: systemctl status <unit>, then journalctl -u <unit> for detail.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (systemctl status)"],
    },
    {
        "id": "linuxplus-ts-016", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 2, "type": "mcq",
        "stem": "To read only the detailed log messages produced by the failing unit 'myapp.service', "
                "including errors from its last start attempt, which command is best?",
        "options": [
            {"id": "A", "text": "journalctl -k"},
            {"id": "B", "text": "dmesg"},
            {"id": "C", "text": "journalctl -u myapp.service"},
            {"id": "D", "text": "tail /var/log/syslog"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "journalctl -u myapp.service filters the journal to that unit's messages; add -e to "
                       "jump to the end or -f to follow new output as you reproduce the failure.",
            "distractors": {
                "A": "journalctl -k shows only KERNEL messages, not a service unit's logs.",
                "B": "dmesg prints the kernel ring buffer, which rarely contains an application service's errors.",
                "D": "tail /var/log/syslog shows mixed system messages, not an easily unit-filtered view.",
            },
            "exam_pattern": "journalctl -u <unit> isolates a service's logs; combine with --since / -b for time/boot scoping.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (journalctl -u)"],
    },
    {
        "id": "linuxplus-ts-017", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 2, "type": "mcq",
        "stem": "After a problematic update, you want a concise list of every systemd unit currently in "
                "the failed state. Which command produces it?",
        "options": [
            {"id": "A", "text": "systemctl --all"},
            {"id": "B", "text": "systemctl --failed"},
            {"id": "C", "text": "systemctl reboot"},
            {"id": "D", "text": "systemctl isolate rescue.target"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "systemctl --failed (equivalently 'systemctl list-units --failed') lists only the "
                       "units that have entered the failed state, narrowing the investigation quickly.",
            "distractors": {
                "A": "systemctl --all lists every unit regardless of state, burying the failed ones.",
                "C": "systemctl reboot restarts the machine rather than reporting failures.",
                "D": "isolate rescue.target switches to single-user rescue mode; it does not list failed units.",
            },
            "exam_pattern": "Quickly surface problems with systemctl --failed before drilling in with status/journalctl.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (failed units)"],
    },

    # ===== linuxp_ts_tools ==================================================
    {
        "id": "linuxplus-ts-018", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "On a Debian/Ubuntu system, which file is the traditional destination for general "
                "system log messages when reviewing recent events during troubleshooting?",
        "options": [
            {"id": "A", "text": "/var/log/syslog"},
            {"id": "B", "text": "/var/log/messages"},
            {"id": "C", "text": "/etc/rsyslog.conf"},
            {"id": "D", "text": "/var/log/btmp"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On Debian/Ubuntu, general system messages are written to /var/log/syslog; it is the "
                       "primary catch-all text log to review for recent events.",
            "distractors": {
                "B": "/var/log/messages is the RHEL/CentOS equivalent and is not the default on Debian/Ubuntu.",
                "C": "/etc/rsyslog.conf is the logging CONFIGURATION, not a log file of events.",
                "D": "/var/log/btmp records failed login attempts in binary form (read with lastb), not general messages.",
            },
            "exam_pattern": "General log: Debian /var/log/syslog, RHEL /var/log/messages; auth: auth.log vs secure.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Log analysis (/var/log)"],
    },
    {
        "id": "linuxplus-ts-019", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 3, "type": "mcq",
        "stem": "A program exits silently and you need to see which system calls it makes and exactly "
                "where it fails (for example, which file it cannot open). Which tool traces its system "
                "calls?",
        "options": [
            {"id": "A", "text": "top"},
            {"id": "B", "text": "nohup ./program"},
            {"id": "C", "text": "chmod +x ./program"},
            {"id": "D", "text": "strace ./program"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "strace runs the program and prints each system call with its arguments and return "
                       "value, so you can see the exact call that fails (e.g., openat returning ENOENT or EACCES).",
            "distractors": {
                "A": "top is a live resource monitor; it does not trace system calls.",
                "B": "nohup just detaches the program from hangup signals; it provides no tracing.",
                "C": "chmod +x makes a file executable and reveals nothing about runtime behavior.",
            },
            "exam_pattern": "Trace syscalls with strace (and library calls with ltrace) to find where a program fails.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Diagnostic tools (strace)"],
    },
    {
        "id": "linuxplus-ts-020", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "An attempt to unmount /mnt/data fails with 'target is busy'. Which command identifies "
                "the processes holding files open on that filesystem?",
        "options": [
            {"id": "A", "text": "ls -a /mnt/data"},
            {"id": "B", "text": "df -h /mnt/data"},
            {"id": "C", "text": "lsof +D /mnt/data"},
            {"id": "D", "text": "ps aux"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "lsof lists open files and the processes using them; 'lsof +D /mnt/data' (or "
                       "'fuser -m /mnt/data') reveals what is keeping the filesystem busy so it can be unmounted.",
            "distractors": {
                "A": "ls -a just lists directory contents; it does not show which processes have files open.",
                "B": "df -h reports space usage, not open file handles.",
                "D": "ps aux lists processes generally but does not tie them to open files on that mount.",
            },
            "exam_pattern": "'Device is busy' on umount => find holders with lsof or fuser, then stop/kill them.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Diagnostic tools (lsof)"],
    },
    {
        "id": "linuxplus-ts-021", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 1, "type": "fill",
        "stem": "Which command queries and displays the logs collected by the systemd journal, and is "
                "commonly used with options such as -u (unit), -b (boot), -k (kernel), and -f (follow)? "
                "(command name only)",
        "correct": ["journalctl", "/usr/bin/journalctl", "/bin/journalctl"],
        "explanation": {
            "correct": "journalctl reads the systemd journal and filters it by unit, boot, priority, time, "
                       "or kernel, and can follow entries live with -f — the central log tool on systemd systems.",
            "distractors": {},
            "exam_pattern": "On systemd hosts, journalctl centralizes logs (-u/-b/-k/-p/--since); text logs still live in /var/log.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Log analysis (journalctl)"],
    },
]
