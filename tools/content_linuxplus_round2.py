"""CompTIA Linux+ (XK0-006) pool - Round 2 expansion (all four domains).

Deepening pool that extends the round-1 banks (content_linuxplus_system.py,
_security.py, _scripting.py, _ts.py). Every item here is ORIGINAL and NON-
DUPLICATE versus round 1: different commands, flags, files, and scenarios rather
than rewordings. The emphasis is on the hands-on detail Linux+ rewards —
less-common-but-real flags, config-file specifics, and RHEL/Fedora (dnf/rpm/
firewalld/SELinux) versus Debian/Ubuntu (apt/dpkg/ufw/AppArmor) differences.

Distribution mirrors the blueprint weighting (system_mgmt 32%, troubleshooting
28%, security 21%, scripting 19%): 39 system, 34 troubleshooting, 26 security,
23 scripting = 122 items. Ids use the <prefix>-r2-NNN scheme (sys/sec/scr/ts) so
they never collide with the round-1 ids.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored answer key is not positionally
biased, every wrong option carries a distractor note, and each item cites the
public XK0-006 objective domain it draws on. Commands, flags, directives, and
paths are real and version-resilient across mainstream RHEL/Fedora and Debian/
Ubuntu systems; no memorized or real exam items are used.
"""

QUESTIONS = [
    # ================= DOMAIN 1: SYSTEM MANAGEMENT (39) =================

    # ----- linuxp_filesystem (6) -------------------------------------------
    {
        "id": "linuxplus-sys-r2-001", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 2, "type": "mcq",
        "stem": "Which command creates a SYMBOLIC link named /usr/local/bin/python that points to "
                "/usr/bin/python3.11, so the target can live on a different filesystem?",
        "options": [
            {"id": "A", "text": "ln /usr/bin/python3.11 /usr/local/bin/python"},
            {"id": "B", "text": "ln -s /usr/bin/python3.11 /usr/local/bin/python"},
            {"id": "C", "text": "link /usr/bin/python3.11 /usr/local/bin/python"},
            {"id": "D", "text": "cp -s /usr/bin/python3.11 /usr/local/bin/python"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ln -s TARGET LINKNAME creates a symbolic (soft) link. Because it stores a path, "
                       "not an inode, it may cross filesystems and point at directories.",
            "distractors": {
                "A": "ln without -s makes a HARD link, which shares the inode and cannot span filesystems or link directories.",
                "C": "link (and the link() call) creates a HARD link only; it cannot make a symlink.",
                "D": "cp -s does exist in GNU cp but is non-portable and unusual; ln -s is the standard, expected tool.",
            },
            "exam_pattern": "Symlink = ln -s (path-based, cross-filesystem); hard link = ln (shared inode, same filesystem).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Manage files and directories (ln -s)"],
    },
    {
        "id": "linuxplus-sys-r2-002", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 1, "type": "fill",
        "stem": "Which command displays a file's inode number, size, permissions, and its access, "
                "modify, and change timestamps in one detailed report? (command name only)",
        "correct": ["stat", "/usr/bin/stat"],
        "explanation": {
            "correct": "stat FILE prints the inode, size, block count, permission bits (octal and symbolic), "
                       "owner/group, and the atime/mtime/ctime timestamps.",
            "distractors": {},
            "exam_pattern": "stat = full metadata/inode/timestamps for one file; ls -l = compact listing.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — File metadata (stat)"],
    },
    {
        "id": "linuxplus-sys-r2-003", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 2, "type": "mcq",
        "stem": "Which command creates a single gzip-compressed archive named backup.tar.gz from the "
                "directory /etc?",
        "options": [
            {"id": "A", "text": "tar -czf backup.tar.gz /etc"},
            {"id": "B", "text": "tar -xzf backup.tar.gz /etc"},
            {"id": "C", "text": "tar -tzf backup.tar.gz /etc"},
            {"id": "D", "text": "gzip -r /etc > backup.tar.gz"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "tar -c creates an archive, -z pipes it through gzip, and -f names the output file, "
                       "so -czf backup.tar.gz /etc builds the compressed tarball.",
            "distractors": {
                "A": "",
                "B": "-x EXTRACTS from an existing archive rather than creating one.",
                "C": "-t only LISTS the table of contents of an archive; it creates nothing.",
                "D": "gzip compresses individual files in place and does not bundle a directory tree into one tar archive.",
            },
            "exam_pattern": "tar: -c create, -x extract, -t list; add -z (gzip) or -j (bzip2); -f names the file.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Archiving/compression (tar)"],
    },
    {
        "id": "linuxplus-sys-r2-004", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 2, "type": "mcq",
        "stem": "Per the Filesystem Hierarchy Standard, which top-level directory is reserved for "
                "optional, self-contained add-on application software packages (for example a vendor "
                "that installs everything under one subdirectory)?",
        "options": [
            {"id": "A", "text": "/opt"},
            {"id": "B", "text": "/srv"},
            {"id": "C", "text": "/mnt"},
            {"id": "D", "text": "/proc"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "/opt holds optional/add-on software, typically each package in its own /opt/<vendor> "
                       "subtree, keeping third-party software separate from the distribution's files.",
            "distractors": {
                "A": "",
                "B": "/srv holds data served by the system (e.g., web or FTP content), not installed application binaries.",
                "C": "/mnt is a temporary mount point for manually mounted filesystems.",
                "D": "/proc is a virtual filesystem exposing kernel and process information, not software.",
            },
            "exam_pattern": "/opt = add-on packages; /srv = served data; /usr/local = locally compiled software; /mnt = temp mounts.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Filesystem Hierarchy Standard (/opt)"],
    },
    {
        "id": "linuxplus-sys-r2-005", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 2, "type": "mcq",
        "stem": "Which command recursively searches every file under /etc for lines containing the text "
                "'nameserver' and prints each match with its filename and line number?",
        "options": [
            {"id": "A", "text": "grep nameserver /etc"},
            {"id": "B", "text": "grep -rn nameserver /etc"},
            {"id": "C", "text": "find /etc -name nameserver"},
            {"id": "D", "text": "locate nameserver /etc"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "grep -r recurses into the directory tree and -n prefixes each match with its line "
                       "number; the filename is shown automatically when more than one file is searched.",
            "distractors": {
                "A": "Plain grep on a directory errors (or is skipped) without -r/-R; it does not recurse by default.",
                "C": "find -name matches file NAMES, not text inside files.",
                "D": "locate searches a prebuilt filename database for paths; it does not grep file contents.",
            },
            "exam_pattern": "Search file CONTENTS recursively with grep -r (add -n lines, -i ignore case, -l names only).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Searching text (grep -r)"],
    },
    {
        "id": "linuxplus-sys-r2-006", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_filesystem", "difficulty": 3, "type": "mcq",
        "stem": "You must mirror /data to /backup/data so the copy preserves permissions, ownership, "
                "symlinks, and timestamps and only transfers changed files on repeat runs. Which command "
                "is best?",
        "options": [
            {"id": "A", "text": "cp /data /backup/data"},
            {"id": "B", "text": "rsync -a /data/ /backup/data/"},
            {"id": "C", "text": "scp /data /backup/data"},
            {"id": "D", "text": "mv /data /backup/data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "rsync -a (archive mode) is recursive and preserves permissions, ownership, symlinks, "
                       "and times; on later runs it copies only the differences, making it ideal for mirroring.",
            "distractors": {
                "A": "Plain cp (without -a/-r) will not even recurse into the directory and preserves nothing special.",
                "C": "scp copies over SSH but is not delta-based and does not efficiently re-sync only changes.",
                "D": "mv MOVES the data (removing the source); it does not keep a maintained copy.",
            },
            "exam_pattern": "Efficient mirror preserving attributes = rsync -a; add --delete to remove extras, -z to compress.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — File synchronization (rsync)"],
    },

    # ----- linuxp_package_mgmt (6) -----------------------------------------
    {
        "id": "linuxplus-sys-r2-007", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "On a RHEL 9 host you have the path /usr/sbin/semanage but do not know which package "
                "supplies it. Which command identifies the package that PROVIDES that file, even if it "
                "is not yet installed?",
        "options": [
            {"id": "A", "text": "dnf provides /usr/sbin/semanage"},
            {"id": "B", "text": "rpm -qf /usr/sbin/semanage"},
            {"id": "C", "text": "dnf list installed semanage"},
            {"id": "D", "text": "dnf search semanage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "dnf provides <path> (alias 'dnf whatprovides') searches repository metadata for the "
                       "package that supplies a file or capability, whether or not it is installed.",
            "distractors": {
                "A": "",
                "B": "rpm -qf only works if the file is ALREADY installed on disk; it queries the local RPM DB, not repos.",
                "C": "dnf list installed reports installed packages by name; it does not map a file path to a package.",
                "D": "dnf search matches names and summaries by keyword, not a specific file path.",
            },
            "exam_pattern": "File path -> package: 'dnf provides <path>' (from repos) or 'rpm -qf <path>' (if installed).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Software management (dnf provides)"],
    },
    {
        "id": "linuxplus-sys-r2-008", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "An installed binary at /usr/bin/ss is misbehaving and you want to know which RPM owns "
                "it on a RHEL system. Which command answers that?",
        "options": [
            {"id": "A", "text": "rpm -ql /usr/bin/ss"},
            {"id": "B", "text": "rpm -qi ss"},
            {"id": "C", "text": "rpm -qf /usr/bin/ss"},
            {"id": "D", "text": "rpm -V /usr/bin/ss"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "rpm -qf <file> queries which installed package OWNS the given file path (here it "
                       "reports the iproute package).",
            "distractors": {
                "A": "rpm -ql lists the FILES in a named package; it expects a package name, not a path, and does the reverse lookup.",
                "B": "rpm -qi shows package INFO (description, version) for a named package, not file ownership.",
                "D": "rpm -V VERIFIES a package's files against the DB (size/mode/checksum); it does not report the owner.",
            },
            "exam_pattern": "rpm query flags: -qf file->package, -ql package->files, -qi info, -qa all, -V verify.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Software management (rpm -qf)"],
    },
    {
        "id": "linuxplus-sys-r2-009", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "On Debian/Ubuntu, which command refreshes the local package index from the configured "
                "repositories WITHOUT upgrading any installed packages?",
        "options": [
            {"id": "A", "text": "apt upgrade"},
            {"id": "B", "text": "apt update"},
            {"id": "C", "text": "apt full-upgrade"},
            {"id": "D", "text": "apt install --reinstall"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "apt update re-downloads the package lists so apt knows the latest available versions; "
                       "it changes no installed software. You then run 'apt upgrade' to apply updates.",
            "distractors": {
                "A": "apt upgrade installs newer versions of already-installed packages; it does not refresh the index itself.",
                "C": "apt full-upgrade upgrades and may add/remove packages to resolve changes; it also installs, not just indexes.",
                "D": "apt install --reinstall reinstalls a named package; it is unrelated to refreshing the index.",
            },
            "exam_pattern": "Debian flow: 'apt update' (refresh lists) THEN 'apt upgrade' (apply). Fedora's 'dnf upgrade' does both.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Software management (apt update vs upgrade)"],
    },
    {
        "id": "linuxplus-sys-r2-010", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 1, "type": "fill",
        "stem": "On Debian/Ubuntu, which command searches the APT package cache for available packages "
                "whose name or description mentions 'nginx'? (command and subcommand, two words)",
        "correct": ["apt search", "apt-cache search", "apt search nginx", "apt-cache search nginx"],
        "explanation": {
            "correct": "apt search <term> (or the older 'apt-cache search <term>') lists available packages "
                       "whose name or description matches the term, helping you find the right package to install.",
            "distractors": {},
            "exam_pattern": "Find a package: 'apt search' (Debian) / 'dnf search' (Fedora); install with apt/dnf install.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Software management (apt search)"],
    },
    {
        "id": "linuxplus-sys-r2-011", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 3, "type": "mcq",
        "stem": "A dnf upgrade on a RHEL host broke an application, and you need to roll back the most "
                "recent transaction. Which command set does this?",
        "options": [
            {"id": "A", "text": "dnf history, then dnf history undo <id>"},
            {"id": "B", "text": "dnf remove --all-versions"},
            {"id": "C", "text": "dnf downgrade --rollback"},
            {"id": "D", "text": "rpm -e --rollback yesterday"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "dnf history lists past transactions with their IDs, and 'dnf history undo <id>' "
                       "reverses that specific transaction (reinstalling/removing packages to the prior state).",
            "distractors": {
                "A": "",
                "B": "dnf remove --all-versions is not a rollback; it would uninstall packages, not restore prior versions.",
                "C": "dnf downgrade lowers a package to an earlier version but has no '--rollback' option tied to a transaction.",
                "D": "rpm -e erases packages and has no transaction-based '--rollback' (that depended on an unused rpm feature).",
            },
            "exam_pattern": "dnf/yum keep a transaction log: 'dnf history' to view, 'dnf history undo <id>' to reverse one.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Software management (dnf history)"],
    },
    {
        "id": "linuxplus-sys-r2-012", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_package_mgmt", "difficulty": 2, "type": "mcq",
        "stem": "Which command installs the sandboxed desktop application org.gimp.GIMP from the Flathub "
                "remote using the distribution-agnostic Flatpak system?",
        "options": [
            {"id": "A", "text": "flatpak install flathub org.gimp.GIMP"},
            {"id": "B", "text": "snap install org.gimp.GIMP"},
            {"id": "C", "text": "dnf flatpak org.gimp.GIMP"},
            {"id": "D", "text": "flatpak run flathub org.gimp.GIMP"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "flatpak install <remote> <app-id> pulls the application (and its runtime) from the "
                       "named remote; Flathub is the common community remote.",
            "distractors": {
                "A": "",
                "B": "snap is a different (Canonical) packaging system and uses snap names, not Flatpak app-IDs/remotes.",
                "C": "dnf has no 'flatpak' subcommand; Flatpak is managed by the flatpak tool, not dnf.",
                "D": "flatpak run LAUNCHES an already-installed app; it does not install it, and takes an app-id, not a remote.",
            },
            "exam_pattern": "Flatpak: 'flatpak install <remote> <app-id>' then 'flatpak run <app-id>'; Snap uses 'snap install'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Universal packages (Flatpak)"],
    },

    # ----- linuxp_processes_services (6) -----------------------------------
    {
        "id": "linuxplus-sys-r2-013", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 2, "type": "mcq",
        "stem": "Issuing 'kill 2200' with no signal option sends which signal, allowing the process to "
                "clean up before exiting?",
        "options": [
            {"id": "A", "text": "SIGKILL (9)"},
            {"id": "B", "text": "SIGTERM (15)"},
            {"id": "C", "text": "SIGHUP (1)"},
            {"id": "D", "text": "SIGSTOP (19)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The default signal for kill is SIGTERM (15): a polite request to terminate that a "
                       "process can trap to flush buffers and shut down cleanly.",
            "distractors": {
                "A": "SIGKILL (9) is the FORCEFUL kill that cannot be caught or ignored; it is sent only with 'kill -9'.",
                "C": "SIGHUP (1) traditionally means hangup and is often used to make daemons reload config, not the default.",
                "D": "SIGSTOP (19) only PAUSES a process (resumable with SIGCONT); it does not terminate it.",
            },
            "exam_pattern": "Default kill = SIGTERM (15, graceful). Use SIGKILL (9) only when SIGTERM is ignored.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Signals (kill/SIGTERM)"],
    },
    {
        "id": "linuxplus-sys-r2-014", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 2, "type": "mcq",
        "stem": "Several java processes are stuck and you want to terminate every process whose full "
                "command line contains 'oldapp.jar', without looking up PIDs. Which command does this?",
        "options": [
            {"id": "A", "text": "pkill -f oldapp.jar"},
            {"id": "B", "text": "kill oldapp.jar"},
            {"id": "C", "text": "pgrep -f oldapp.jar"},
            {"id": "D", "text": "killall -9 oldapp.jar"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "pkill -f matches the pattern against the FULL command line and signals all matches "
                       "(default SIGTERM), so processes launched as 'java ... oldapp.jar' are caught.",
            "distractors": {
                "A": "",
                "B": "kill takes a numeric PID, not a name/pattern, so 'kill oldapp.jar' fails.",
                "C": "pgrep -f only LISTS the matching PIDs; it sends no signal (pgrep finds, pkill kills).",
                "D": "killall matches the process NAME (e.g., 'java'), not arguments, so 'oldapp.jar' as a name won't match.",
            },
            "exam_pattern": "pgrep/pkill find/kill by name or, with -f, by full command line; killall matches the exact process name.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Process control (pkill -f)"],
    },
    {
        "id": "linuxplus-sys-r2-015", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 3, "type": "mcq",
        "stem": "On a systemd host, which command lists the active timer units along with when each last "
                "ran and when it is next scheduled to run (the systemd alternative to cron)?",
        "options": [
            {"id": "A", "text": "systemctl list-timers"},
            {"id": "B", "text": "crontab -l"},
            {"id": "C", "text": "systemctl list-units --type=service"},
            {"id": "D", "text": "systemd-analyze"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "systemctl list-timers shows each active .timer unit with NEXT and LAST run times and "
                       "the service it activates; timers are systemd's scheduling mechanism.",
            "distractors": {
                "A": "",
                "B": "crontab -l lists the invoking user's cron jobs, a separate scheduler, not systemd timers.",
                "C": "list-units --type=service shows services, not timer units or their schedule.",
                "D": "systemd-analyze reports boot performance; it does not list timers and their next runs.",
            },
            "exam_pattern": "systemd scheduling: a .timer unit activates a matching .service; inspect with 'systemctl list-timers'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Scheduling (systemd timers)"],
    },
    {
        "id": "linuxplus-sys-r2-016", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 2, "type": "mcq",
        "stem": "You start a long backup over SSH and need it to keep running after you log out, with "
                "its output saved to a file. Which invocation is correct?",
        "options": [
            {"id": "A", "text": "nohup ./backup.sh &"},
            {"id": "B", "text": "./backup.sh &"},
            {"id": "C", "text": "bg ./backup.sh"},
            {"id": "D", "text": "./backup.sh && exit"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "nohup makes the command ignore the SIGHUP sent at logout, '&' runs it in the "
                       "background, and output is redirected to nohup.out by default, so it survives the session.",
            "distractors": {
                "A": "",
                "B": "'&' alone backgrounds the job, but it can still receive SIGHUP and die when the shell exits (unless huponexit is off).",
                "C": "bg resumes an ALREADY-stopped job in the background; it does not launch a new command or protect from HUP.",
                "D": "'&& exit' just closes the shell after the script finishes in the FOREGROUND; it never detaches it.",
            },
            "exam_pattern": "Survive logout: 'nohup cmd &' or 'systemd-run'/disown; terminal multiplexers (tmux/screen) also work.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Background jobs (nohup)"],
    },
    {
        "id": "linuxplus-sys-r2-017", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 3, "type": "mcq",
        "stem": "After editing /etc/nginx/nginx.conf you want nginx to re-read its configuration WITHOUT "
                "dropping existing client connections. Which systemd action is appropriate?",
        "options": [
            {"id": "A", "text": "systemctl restart nginx"},
            {"id": "B", "text": "systemctl reload nginx"},
            {"id": "C", "text": "systemctl daemon-reload"},
            {"id": "D", "text": "systemctl stop nginx"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "systemctl reload triggers the unit's ExecReload (for nginx, a graceful config reload) "
                       "so the service applies new settings without a full restart or dropped connections.",
            "distractors": {
                "A": "restart fully stops and starts the service, briefly interrupting active connections.",
                "C": "daemon-reload reloads systemd's own UNIT files after you change a .service file; it does not reload nginx.conf.",
                "D": "stop shuts the service down entirely rather than reloading it.",
            },
            "exam_pattern": "reload = re-read app config in place; restart = stop+start; daemon-reload = re-read systemd unit files.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Manage services (systemctl reload)"],
    },
    {
        "id": "linuxplus-sys-r2-018", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_processes_services", "difficulty": 1, "type": "fill",
        "stem": "Which command displays running processes as a tree, showing the parent/child "
                "relationships (which process spawned which)? (command name only)",
        "correct": ["pstree", "/usr/bin/pstree"],
        "explanation": {
            "correct": "pstree draws the process hierarchy, visually linking each child to the parent that "
                       "forked it; 'pstree -p' adds PIDs.",
            "distractors": {},
            "exam_pattern": "pstree = parent/child tree view; 'ps --forest' (or ps axjf) shows a similar hierarchy.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Process hierarchy (pstree)"],
    },

    # ----- linuxp_users_groups (5) -----------------------------------------
    {
        "id": "linuxplus-sys-r2-019", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 3, "type": "mcq",
        "stem": "Security policy requires that user 'svc' must change its password at least every 60 "
                "days. Which command sets that maximum password age?",
        "options": [
            {"id": "A", "text": "chage -M 60 svc"},
            {"id": "B", "text": "chage -m 60 svc"},
            {"id": "C", "text": "chage -d 60 svc"},
            {"id": "D", "text": "usermod -e 60 svc"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chage -M 60 sets the MAXIMUM number of days a password is valid before a change is "
                       "forced; 'chage -l svc' shows the resulting aging fields.",
            "distractors": {
                "A": "",
                "B": "chage -m (lowercase) sets the MINIMUM days between changes, not the maximum lifetime.",
                "C": "chage -d sets the date of the LAST password change (used to force an immediate change), not the maximum age.",
                "D": "usermod -e sets an account EXPIRATION DATE (a calendar date), not the password change interval.",
            },
            "exam_pattern": "chage: -M max age, -m min age, -W warn days, -E account expiry date, -l list.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Password aging (chage -M)"],
    },
    {
        "id": "linuxplus-sys-r2-020", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 2, "type": "mcq",
        "stem": "A departing employee's account 'jsmith' must be removed together with its home directory "
                "and mail spool. Which single command does this?",
        "options": [
            {"id": "A", "text": "userdel jsmith"},
            {"id": "B", "text": "userdel -r jsmith"},
            {"id": "C", "text": "usermod -L jsmith"},
            {"id": "D", "text": "rm -rf /home/jsmith"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "userdel -r removes the account AND deletes its home directory and mail spool, leaving "
                       "no leftover files behind.",
            "distractors": {
                "A": "userdel without -r deletes the account entry but LEAVES the home directory and its files in place.",
                "C": "usermod -L only LOCKS the password; the account and files remain.",
                "D": "rm -rf deletes the home files but leaves the account defined in /etc/passwd and /etc/shadow.",
            },
            "exam_pattern": "userdel -r = account + home + mail spool; plain userdel keeps the home directory.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Manage users (userdel -r)"],
    },
    {
        "id": "linuxplus-sys-r2-021", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 2, "type": "fill",
        "stem": "Which directory holds the skeleton files (such as .bashrc and .profile) that useradd "
                "copies into a new user's home directory when it is created? (full path)",
        "correct": ["/etc/skel", "etc/skel"],
        "explanation": {
            "correct": "/etc/skel is the template: its contents are copied into each new home directory "
                       "created with 'useradd -m', giving new users a consistent starting environment.",
            "distractors": {},
            "exam_pattern": "New-home template = /etc/skel; account defaults = /etc/default/useradd and /etc/login.defs.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — User defaults (/etc/skel)"],
    },
    {
        "id": "linuxplus-sys-r2-022", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 3, "type": "mcq",
        "stem": "On a host joined to LDAP/SSSD, 'grep alice /etc/passwd' returns nothing, yet alice can "
                "log in. Which command correctly looks up her account through ALL configured name "
                "sources (local files plus directory services)?",
        "options": [
            {"id": "A", "text": "getent passwd alice"},
            {"id": "B", "text": "cat /etc/passwd | grep alice"},
            {"id": "C", "text": "id -u /etc/passwd"},
            {"id": "D", "text": "lsof -u alice"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "getent queries the NSS stack defined in /etc/nsswitch.conf, so 'getent passwd alice' "
                       "returns her entry whether it comes from local files, LDAP, or SSSD.",
            "distractors": {
                "A": "",
                "B": "Reading /etc/passwd only sees LOCAL accounts, missing directory-provided users like alice.",
                "C": "id -u expects a username and returns a UID; passing a file path is meaningless here.",
                "D": "lsof -u lists a user's open files; it does not resolve account database entries.",
            },
            "exam_pattern": "Resolve accounts across files + LDAP/SSSD with getent (passwd/group/hosts); it honors nsswitch.conf.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Name service lookups (getent)"],
    },
    {
        "id": "linuxplus-sys-r2-023", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_users_groups", "difficulty": 2, "type": "mcq",
        "stem": "What is the key difference when you switch to another user with 'su - bob' compared with "
                "'su bob'?",
        "options": [
            {"id": "A", "text": "'su - bob' starts a LOGIN shell: it loads bob's environment and changes to bob's home directory"},
            {"id": "B", "text": "'su - bob' keeps your current environment and directory; 'su bob' resets them"},
            {"id": "C", "text": "'su - bob' requires bob's password, while 'su bob' uses your own"},
            {"id": "D", "text": "There is no functional difference; the dash is cosmetic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The dash makes su start a LOGIN shell, so it reads bob's login profile, sets his "
                       "PATH/HOME, and moves to his home directory — as if bob had logged in directly.",
            "distractors": {
                "A": "",
                "B": "This is reversed: 'su bob' (no dash) keeps your environment; 'su - bob' resets it to bob's login environment.",
                "C": "Both forms prompt for the TARGET user's password (bob's); the dash does not change which password is required.",
                "D": "The dash is significant: it controls whether a login environment is loaded.",
            },
            "exam_pattern": "'su -' (or 'su -l') = full login environment + target's home; 'su' keeps your current env/cwd.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Switching users (su -)"],
    },

    # ----- linuxp_storage_lvm (6) ------------------------------------------
    {
        "id": "linuxplus-sys-r2-024", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 3, "type": "multi",
        "stem": "After 'lvextend -L +10G /dev/vg0/data' succeeds, the mounted filesystem still shows the "
                "old size. Which TWO commands can grow the filesystem onto the new space, depending on "
                "its type? (Choose two.)",
        "options": [
            {"id": "A", "text": "resize2fs /dev/vg0/data   (for ext2/3/4)"},
            {"id": "B", "text": "xfs_growfs /data   (for XFS, by mount point)"},
            {"id": "C", "text": "mkfs.ext4 /dev/vg0/data"},
            {"id": "D", "text": "fdisk /dev/vg0/data"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "An ext filesystem is grown with resize2fs on the device, while XFS is grown with "
                       "xfs_growfs given its MOUNT POINT; both can expand online to fill the enlarged LV.",
            "distractors": {
                "C": "mkfs.ext4 would CREATE a new filesystem on the LV, destroying all existing data.",
                "D": "fdisk edits partition tables on whole disks; it does not resize a filesystem on a logical volume.",
            },
            "exam_pattern": "After lvextend, grow the fs: resize2fs (ext) or xfs_growfs (XFS); 'lvextend -r' can do both in one step.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Grow filesystems (resize2fs/xfs_growfs)"],
    },
    {
        "id": "linuxplus-sys-r2-025", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 2, "type": "fill",
        "stem": "Which command prints block devices with their UUID, filesystem TYPE, and LABEL — the "
                "values you copy into /etc/fstab for persistent mounts? (command name only)",
        "correct": ["blkid", "/usr/sbin/blkid", "/sbin/blkid"],
        "explanation": {
            "correct": "blkid reports each block device's UUID, TYPE, and LABEL, so you can reference a "
                       "filesystem by UUID= in /etc/fstab instead of an unstable /dev name.",
            "distractors": {},
            "exam_pattern": "Get a UUID for fstab with blkid (or 'lsblk -f'); prefer UUID=/LABEL= over /dev/sdXN.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Identify filesystems (blkid)"],
    },
    {
        "id": "linuxplus-sys-r2-026", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 3, "type": "mcq",
        "stem": "You added a new partition /dev/sdb2 to use as additional swap. Which sequence formats "
                "it as swap and activates it immediately?",
        "options": [
            {"id": "A", "text": "mkswap /dev/sdb2 ; swapon /dev/sdb2"},
            {"id": "B", "text": "mkfs.swap /dev/sdb2 ; mount /dev/sdb2"},
            {"id": "C", "text": "swapon /dev/sdb2 ; mkswap /dev/sdb2"},
            {"id": "D", "text": "fallocate -l 2G /dev/sdb2 ; swapon -a"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "mkswap writes a swap signature to the device, then swapon enables it for paging; add "
                       "an entry to /etc/fstab (with 'swap' as the type) to make it persist across reboots.",
            "distractors": {
                "A": "",
                "B": "There is no mkfs.swap, and swap areas are activated with swapon, not mount.",
                "C": "The order is wrong: you must mkswap (format) BEFORE swapon (activate).",
                "D": "fallocate pre-allocates a file's size and is used for swap FILES, not to format a partition; swapon -a only re-reads fstab.",
            },
            "exam_pattern": "Swap partition: mkswap then swapon (add to fstab to persist); 'swapon --show' / 'free -h' to verify.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Swap space (mkswap/swapon)"],
    },
    {
        "id": "linuxplus-sys-r2-027", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 3, "type": "mcq",
        "stem": "Before a risky upgrade you want a point-in-time LVM snapshot named data_snap of the "
                "logical volume /dev/vg0/data so you can roll back. Which command creates it?",
        "options": [
            {"id": "A", "text": "lvcreate -L 5G -s -n data_snap /dev/vg0/data"},
            {"id": "B", "text": "lvcreate -L 5G -n data_snap vg0"},
            {"id": "C", "text": "lvconvert --snapshot /dev/vg0/data"},
            {"id": "D", "text": "vgcreate -s data_snap /dev/vg0/data"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "lvcreate -s (snapshot) -n names it, -L sizes the copy-on-write area, and the origin "
                       "LV is the final argument, producing /dev/vg0/data_snap for rollback or backup.",
            "distractors": {
                "A": "",
                "B": "Without -s this creates a brand-new ordinary logical volume, not a snapshot of the origin.",
                "C": "lvconvert changes volume types (e.g., mirror/thin) and is not the standard way to create a snapshot.",
                "D": "vgcreate creates a VOLUME GROUP; -s there sets the physical extent size, unrelated to snapshots.",
            },
            "exam_pattern": "LVM snapshot = 'lvcreate -s -n <name> -L <size> <origin-LV>'; merge back with lvconvert --merge.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — LVM snapshots (lvcreate -s)"],
    },
    {
        "id": "linuxplus-sys-r2-028", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 2, "type": "mcq",
        "stem": "A volume group vg0 is out of free extents. You have initialized a new physical volume "
                "/dev/sdd1 with pvcreate. Which command adds that PV's capacity to vg0?",
        "options": [
            {"id": "A", "text": "lvextend vg0 /dev/sdd1"},
            {"id": "B", "text": "vgextend vg0 /dev/sdd1"},
            {"id": "C", "text": "pvextend vg0 /dev/sdd1"},
            {"id": "D", "text": "vgmerge vg0 /dev/sdd1"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "vgextend adds one or more physical volumes to an existing volume group, increasing "
                       "the free extents available for logical volumes.",
            "distractors": {
                "A": "lvextend grows a LOGICAL VOLUME; it cannot add a PV to the group.",
                "C": "There is no pvextend command; pvresize exists but only re-reads a PV's own size.",
                "D": "vgmerge combines two existing VOLUME GROUPS, not a VG and a bare PV.",
            },
            "exam_pattern": "Grow a VG: pvcreate the disk, then 'vgextend <vg> <pv>'; then lvextend the LV into the new space.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Extend volume groups (vgextend)"],
    },
    {
        "id": "linuxplus-sys-r2-029", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_storage_lvm", "difficulty": 2, "type": "mcq",
        "stem": "You just added a new line to /etc/fstab for an extra data disk. Which command mounts "
                "ALL currently-unmounted fstab entries, letting you confirm the new entry works without "
                "rebooting?",
        "options": [
            {"id": "A", "text": "mount -a"},
            {"id": "B", "text": "mount -o remount /"},
            {"id": "C", "text": "systemctl daemon-reload"},
            {"id": "D", "text": "mount --bind /etc/fstab"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "mount -a reads /etc/fstab and mounts every entry not already mounted (and not marked "
                       "noauto), so a typo in the new line surfaces immediately instead of at the next boot.",
            "distractors": {
                "A": "",
                "B": "remount / only re-applies options to the already-mounted root; it does not process the new entry.",
                "C": "daemon-reload re-reads systemd units; although systemd generates mount units from fstab, 'mount -a' is the direct test.",
                "D": "mount --bind re-mounts an existing directory elsewhere; it does not process fstab entries.",
            },
            "exam_pattern": "Test a new fstab line safely with 'mount -a' (and 'findmnt --verify') before relying on it at boot.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Mounting filesystems (mount -a)"],
    },

    # ----- linuxp_networking_config (5) ------------------------------------
    {
        "id": "linuxplus-sys-r2-030", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "Which command persistently sets the system's static hostname to web01 on a modern "
                "systemd distribution, updating /etc/hostname?",
        "options": [
            {"id": "A", "text": "hostname web01"},
            {"id": "B", "text": "hostnamectl set-hostname web01"},
            {"id": "C", "text": "echo web01 > /proc/sys/kernel/hostname"},
            {"id": "D", "text": "sysctl kernel.hostname=web01"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "hostnamectl set-hostname web01 updates the static hostname in /etc/hostname (and the "
                       "live kernel value), so it persists across reboots.",
            "distractors": {
                "A": "The legacy 'hostname web01' changes the name only until the next reboot; it is not persistent.",
                "C": "Writing to /proc sets the running name temporarily and does not update the config file.",
                "D": "sysctl kernel.hostname sets the RUNNING kernel value only; it does not write /etc/hostname, so it is lost on reboot.",
            },
            "exam_pattern": "Persistent hostname = hostnamectl set-hostname (writes /etc/hostname); plain 'hostname' is temporary.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Hostname (hostnamectl)"],
    },
    {
        "id": "linuxplus-sys-r2-031", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "You need a host to resolve the name 'build.internal' to 10.0.5.20 locally, taking "
                "precedence over DNS and without running a DNS server. Which file do you edit?",
        "options": [
            {"id": "A", "text": "/etc/hosts"},
            {"id": "B", "text": "/etc/resolv.conf"},
            {"id": "C", "text": "/etc/hostname"},
            {"id": "D", "text": "/etc/networks"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "/etc/hosts maps names to IP addresses locally. With the default nsswitch order "
                       "(files before dns), an entry here is used before any DNS query.",
            "distractors": {
                "A": "",
                "B": "/etc/resolv.conf lists the DNS NAMESERVERS to query; it does not hold static name-to-IP entries.",
                "C": "/etc/hostname stores THIS machine's own hostname, not mappings for other hosts.",
                "D": "/etc/networks maps names to NETWORK numbers, not individual host addresses.",
            },
            "exam_pattern": "Static local name->IP = /etc/hosts (checked before DNS); DNS servers = /etc/resolv.conf.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Local name resolution (/etc/hosts)"],
    },
    {
        "id": "linuxplus-sys-r2-032", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 3, "type": "mcq",
        "stem": "A host has an IP but no default gateway. Using iproute2, which command adds a default "
                "route via the gateway 192.168.10.1 on interface eth0 for the current session?",
        "options": [
            {"id": "A", "text": "ip route add default via 192.168.10.1 dev eth0"},
            {"id": "B", "text": "ip addr add default 192.168.10.1 dev eth0"},
            {"id": "C", "text": "route default 192.168.10.1"},
            {"id": "D", "text": "ip route add 192.168.10.1 default"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ip route add default via <gateway> dev <iface> installs the default route (0.0.0.0/0) "
                       "pointing at the next-hop gateway, enabling traffic to other networks.",
            "distractors": {
                "A": "",
                "B": "ip addr manages interface ADDRESSES, not routes; 'default' is not valid syntax there.",
                "C": "'route default ...' is not valid; the legacy form was 'route add default gw <ip>', and route is deprecated.",
                "D": "The keyword order is wrong; the destination 'default' comes first, then 'via <gw> dev <iface>'.",
            },
            "exam_pattern": "Default gateway (runtime): 'ip route add default via <gw> dev <iface>'; persist via NetworkManager/netplan.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Routing (ip route add default)"],
    },
    {
        "id": "linuxplus-sys-r2-033", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "On a NetworkManager-managed system, which command lists the network devices and shows "
                "each one's type, state (connected/disconnected), and the connection in use?",
        "options": [
            {"id": "A", "text": "nmcli device status"},
            {"id": "B", "text": "nmcli radio all"},
            {"id": "C", "text": "ip -s link"},
            {"id": "D", "text": "nmcli connection reload"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "nmcli device status lists each interface with its DEVICE, TYPE, STATE, and the active "
                       "CONNECTION profile, the quick way to see what NetworkManager thinks is up.",
            "distractors": {
                "A": "",
                "B": "nmcli radio all reports the on/off state of WiFi/WWAN radios, not per-device status.",
                "C": "ip -s link shows interface statistics (packets/errors), not NetworkManager connection state.",
                "D": "nmcli connection reload re-reads profile files from disk; it displays nothing about device state.",
            },
            "exam_pattern": "nmcli device status (devices/state) vs nmcli connection show (profiles); 'nmcli con up <name>' activates.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — NetworkManager (nmcli device status)"],
    },
    {
        "id": "linuxplus-sys-r2-034", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_networking_config", "difficulty": 2, "type": "mcq",
        "stem": "An interface eth1 shows state DOWN in 'ip link'. Using iproute2, which command "
                "administratively brings the link up?",
        "options": [
            {"id": "A", "text": "ip link set eth1 up"},
            {"id": "B", "text": "ip addr up eth1"},
            {"id": "C", "text": "ifup eth1 --force"},
            {"id": "D", "text": "ip link eth1 enable"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ip link set <iface> up changes the interface's administrative state to UP; 'ip link "
                       "set eth1 down' takes it back down.",
            "distractors": {
                "A": "",
                "B": "ip addr manages addresses; 'up' is not an ip addr operation.",
                "C": "ifup is the older ifupdown/distro tool and may be absent; the iproute2 way is 'ip link set ... up'.",
                "D": "'ip link eth1 enable' is invalid syntax; the verb is 'set <dev> up'.",
            },
            "exam_pattern": "Toggle a link with 'ip link set <iface> up|down'; confirm with 'ip link show'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Interface state (ip link set)"],
    },

    # ----- linuxp_boot_kernel (5) ------------------------------------------
    {
        "id": "linuxplus-sys-r2-035", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 1, "type": "fill",
        "stem": "Which command prints just the version (release) string of the currently running kernel, "
                "for example 5.14.0-427.el9.x86_64? (command and flag)",
        "correct": ["uname -r", "uname --kernel-release"],
        "explanation": {
            "correct": "uname -r outputs the running kernel release string. ('uname -a' prints everything; "
                       "'uname -m' the machine architecture.)",
            "distractors": {},
            "exam_pattern": "Running kernel version = 'uname -r'; installed kernels (RHEL) via 'rpm -q kernel'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Kernel version (uname -r)"],
    },
    {
        "id": "linuxplus-sys-r2-036", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 2, "type": "mcq",
        "stem": "A server should boot to a full graphical desktop by default (the equivalent of the old "
                "runlevel 5). Which command sets that systemd default target?",
        "options": [
            {"id": "A", "text": "systemctl set-default graphical.target"},
            {"id": "B", "text": "systemctl set-default multi-user.target"},
            {"id": "C", "text": "systemctl isolate graphical.target"},
            {"id": "D", "text": "systemctl enable graphical.target"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "systemctl set-default graphical.target makes the graphical target (≈ runlevel 5) the "
                       "default at boot by relinking /etc/systemd/system/default.target.",
            "distractors": {
                "A": "",
                "B": "multi-user.target is the non-graphical, text/networked target (≈ runlevel 3) — the opposite request.",
                "C": "isolate switches to the target NOW for the current session but does not change the boot DEFAULT.",
                "D": "enable arranges a unit to start via its install dependencies; it does not set the default boot target.",
            },
            "exam_pattern": "Default boot target: 'systemctl set-default graphical.target' (RL5) or multi-user.target (RL3); isolate = now only.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — systemd targets (set-default)"],
    },
    {
        "id": "linuxplus-sys-r2-037", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 3, "type": "mcq",
        "stem": "A faulty driver module 'nouveau' must be UNLOADED from the running kernel right now "
                "(you will blacklist it separately). Which command removes the loaded module?",
        "options": [
            {"id": "A", "text": "modprobe -r nouveau"},
            {"id": "B", "text": "modprobe nouveau"},
            {"id": "C", "text": "insmod -r nouveau"},
            {"id": "D", "text": "depmod nouveau"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "modprobe -r unloads the module and any now-unused dependencies (equivalent to rmmod "
                       "but dependency-aware). To keep it from loading at boot, add it to /etc/modprobe.d/ with 'blacklist nouveau'.",
            "distractors": {
                "A": "",
                "B": "modprobe nouveau (no -r) LOADS the module, the opposite of unloading it.",
                "C": "insmod has no -r unload option; it only inserts a single .ko and ignores dependencies.",
                "D": "depmod rebuilds the modules.dep dependency map; it does not load or unload modules.",
            },
            "exam_pattern": "Unload now: 'modprobe -r <mod>' (or rmmod). Prevent at boot: 'blacklist <mod>' in /etc/modprobe.d/*.conf.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Kernel modules (modprobe -r)"],
    },
    {
        "id": "linuxplus-sys-r2-038", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 3, "type": "mcq",
        "stem": "After adding a storage driver to the module load list, a RHEL/Fedora system must "
                "rebuild its initramfs so the driver is available early in boot. Which command does this?",
        "options": [
            {"id": "A", "text": "dracut -f"},
            {"id": "B", "text": "update-initramfs -u"},
            {"id": "C", "text": "grub2-mkconfig -o /boot/grub2/grub.cfg"},
            {"id": "D", "text": "mkfs -t initramfs /boot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On RHEL/Fedora, dracut builds the initramfs; 'dracut -f' forces an overwrite of the "
                       "existing image for the current kernel so the new module is included at early boot.",
            "distractors": {
                "A": "",
                "B": "update-initramfs is the DEBIAN/Ubuntu tool; it is normally absent on RHEL/Fedora.",
                "C": "grub2-mkconfig regenerates the bootloader menu, not the initramfs image.",
                "D": "mkfs creates a filesystem; it has nothing to do with generating an initramfs.",
            },
            "exam_pattern": "Rebuild initramfs: dracut -f (RHEL/Fedora) vs update-initramfs -u (Debian/Ubuntu).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — initramfs (dracut)"],
    },
    {
        "id": "linuxplus-sys-r2-039", "exam": "linuxplus", "domain": "linuxp_system_mgmt",
        "subtopic": "linuxp_boot_kernel", "difficulty": 2, "type": "mcq",
        "stem": "A server crashed and rebooted. Which journalctl command shows the logs from the "
                "PREVIOUS boot (the one that ended in the crash), assuming persistent journaling is "
                "enabled?",
        "options": [
            {"id": "A", "text": "journalctl -b -1"},
            {"id": "B", "text": "journalctl -b"},
            {"id": "C", "text": "journalctl -k"},
            {"id": "D", "text": "journalctl --rotate"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "journalctl -b -1 selects the previous boot (-b 0 or -b is the current boot). "
                       "'journalctl --list-boots' enumerates the boots and their offsets.",
            "distractors": {
                "A": "",
                "B": "journalctl -b (or -b 0) shows the CURRENT boot, not the crashed prior one.",
                "C": "-k limits output to kernel messages for the current boot; it does not select a previous boot.",
                "D": "--rotate rotates the journal FILES; it displays no logs.",
            },
            "exam_pattern": "Previous boot logs: 'journalctl -b -1' (needs persistent journal: Storage=persistent / /var/log/journal).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 1 — Boot logs (journalctl -b -1)"],
    },

    # ================= DOMAIN 2: SECURITY (26) =================

    # ----- linuxp_permissions_acl (6) --------------------------------------
    {
        "id": "linuxplus-sec-r2-001", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 3, "type": "mcq",
        "stem": "A user's umask is 022. When that user creates a NEW regular file (before any later "
                "chmod), what permissions does it receive?",
        "options": [
            {"id": "A", "text": "rw-r--r-- (644)"},
            {"id": "B", "text": "rwxr-xr-x (755)"},
            {"id": "C", "text": "rw-rw-r-- (664)"},
            {"id": "D", "text": "rw------- (600)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "New files start from base 666; the umask masks off the bits, so 666 minus 022 = 644 "
                       "(rw-r--r--). (New directories start from 777, giving 755 under the same umask.)",
            "distractors": {
                "A": "",
                "B": "755 is the result for a new DIRECTORY (777 - 022), not a regular file, which never gets execute by default.",
                "C": "664 would come from umask 002, not 022.",
                "D": "600 would require a umask of 077, which masks all group/other bits.",
            },
            "exam_pattern": "File perms = 666 - umask; directory perms = 777 - umask. umask 022 -> 644 files / 755 dirs.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Default permissions (umask)"],
    },
    {
        "id": "linuxplus-sec-r2-002", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 3, "type": "mcq",
        "stem": "A shared project directory /srv/team must ensure every NEW file and subdirectory "
                "created inside it automatically belongs to the directory's group. Which command sets "
                "the bit that does this?",
        "options": [
            {"id": "A", "text": "chmod g+s /srv/team"},
            {"id": "B", "text": "chmod u+s /srv/team"},
            {"id": "C", "text": "chmod +t /srv/team"},
            {"id": "D", "text": "chmod g+w /srv/team"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The SGID bit on a directory (chmod g+s, or the 2 in 2775) makes new entries inherit "
                       "the directory's group instead of the creator's primary group — ideal for shared workspaces.",
            "distractors": {
                "A": "",
                "B": "SUID (u+s) on a directory has no group-inheritance effect; on files it runs them as the owner.",
                "C": "The sticky bit (+t) restricts deletion to file owners; it does not control group inheritance.",
                "D": "g+w merely grants group WRITE; it does not make new files inherit the directory's group.",
            },
            "exam_pattern": "Shared-group directory = SGID (chmod g+s / 2xxx); files then inherit the dir's group.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Special permissions (SGID directory)"],
    },
    {
        "id": "linuxplus-sec-r2-003", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 3, "type": "mcq",
        "stem": "During a security audit you must list every regular file on the system that has the "
                "SUID bit set (a common privilege-escalation review). Which command does this?",
        "options": [
            {"id": "A", "text": "find / -type f -perm -4000"},
            {"id": "B", "text": "find / -type f -perm -2000"},
            {"id": "C", "text": "find / -type f -perm 777"},
            {"id": "D", "text": "ls -lR / | grep rwx"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "-perm -4000 matches files that have (at least) the SUID bit set; the leading minus "
                       "means 'all of these bits present', so it finds set-user-ID binaries anywhere on /.",
            "distractors": {
                "A": "",
                "B": "-perm -2000 finds SGID (set-group-ID) files, not SUID.",
                "C": "-perm 777 matches files whose permissions are EXACTLY rwxrwxrwx, missing SUID files and catching unrelated ones.",
                "D": "Grepping ls output for 'rwx' is unreliable and does not isolate the SUID 's' bit.",
            },
            "exam_pattern": "Audit SUID/SGID: 'find / -perm -4000' (SUID) and 'find / -perm -2000' (SGID); -perm -1000 = sticky.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Special permissions (find -perm -4000)"],
    },
    {
        "id": "linuxplus-sec-r2-004", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "mcq",
        "stem": "Which single command changes BOTH the owner to 'bob' and the group to 'staff' on the "
                "file project.txt?",
        "options": [
            {"id": "A", "text": "chown bob:staff project.txt"},
            {"id": "B", "text": "chown bob staff project.txt"},
            {"id": "C", "text": "chmod bob:staff project.txt"},
            {"id": "D", "text": "chgrp bob:staff project.txt"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chown accepts owner:group in one argument, so 'chown bob:staff project.txt' sets the "
                       "owner to bob and the group to staff simultaneously.",
            "distractors": {
                "A": "",
                "B": "Without the colon, 'bob' and 'staff' are read as two separate path/user arguments and it fails.",
                "C": "chmod changes permission BITS, not ownership.",
                "D": "chgrp changes only the GROUP and does not take an owner:group pair.",
            },
            "exam_pattern": "chown owner:group sets both; chown owner sets owner only; chgrp or 'chown :group' sets group only.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Ownership (chown owner:group)"],
    },
    {
        "id": "linuxplus-sec-r2-005", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 3, "type": "mcq",
        "stem": "On the directory /shared you want the group 'devs' to automatically receive rwx on every "
                "file created there in the future, via a DEFAULT ACL. Which command sets it?",
        "options": [
            {"id": "A", "text": "setfacl -m g:devs:rwx /shared"},
            {"id": "B", "text": "setfacl -d -m g:devs:rwx /shared"},
            {"id": "C", "text": "setfacl -b g:devs:rwx /shared"},
            {"id": "D", "text": "chmod -R g+rwx /shared"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The -d flag sets a DEFAULT ACL on the directory, which is inherited by newly created "
                       "entries, so future files grant devs rwx automatically.",
            "distractors": {
                "A": "Without -d this sets an ACL on the directory itself only; existing/new files inside do not inherit it.",
                "C": "-b REMOVES all ACL entries rather than adding a default one.",
                "D": "chmod cannot create an inheritable default for a specific named group; it changes current bits only.",
            },
            "exam_pattern": "Inheritable ACL = 'setfacl -d -m ...' (default ACL on a directory); -m current, -x remove, -b clear.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Default ACLs (setfacl -d)"],
    },
    {
        "id": "linuxplus-sec-r2-006", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_permissions_acl", "difficulty": 2, "type": "mcq",
        "stem": "The command 'ls -l /usr/bin/passwd' shows -rwsr-xr-x. Why must /usr/bin/passwd have the "
                "SUID bit (the 's' in the owner's execute position)?",
        "options": [
            {"id": "A", "text": "So any user running it executes with the file owner's (root's) privileges, letting them update /etc/shadow"},
            {"id": "B", "text": "So the file inherits the group of its parent directory"},
            {"id": "C", "text": "So only root can execute the file"},
            {"id": "D", "text": "So the file cannot be deleted by non-owners"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SUID makes the program run with the privileges of its OWNER (root for passwd), so an "
                       "ordinary user can change their hashed password in the root-only /etc/shadow.",
            "distractors": {
                "A": "",
                "B": "That describes SGID on a directory, not SUID on an executable.",
                "C": "r-x for group/other means others CAN execute it; SUID is about the privilege it runs with, not who may run it.",
                "D": "Delete protection in a shared directory is the sticky bit, not SUID.",
            },
            "exam_pattern": "SUID (chmod u+s / 4xxx) = run as the file's owner; classic example is /usr/bin/passwd owned by root.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Special permissions (SUID)"],
    },

    # ----- linuxp_access_control (5) ---------------------------------------
    {
        "id": "linuxplus-sec-r2-007", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 2, "type": "mcq",
        "stem": "In /etc/sudoers, which line grants EVERY member of the 'wheel' group the ability to run "
                "any command as any user via sudo?",
        "options": [
            {"id": "A", "text": "%wheel ALL=(ALL) ALL"},
            {"id": "B", "text": "wheel ALL=(ALL) ALL"},
            {"id": "C", "text": "%wheel = ALL"},
            {"id": "D", "text": "@wheel ALL=(ALL) NOPASSWD"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The leading % marks a GROUP. '%wheel ALL=(ALL) ALL' lets wheel members run all "
                       "commands, as any target user, on all hosts.",
            "distractors": {
                "A": "",
                "B": "Without the %, 'wheel' is treated as a USER name, not the group, so it does not grant the group.",
                "C": "This is not valid sudoers syntax; a rule needs the host=(runas) command fields.",
                "D": "@ is not the group prefix (it is %), and NOPASSWD must precede a command list, so this line is malformed.",
            },
            "exam_pattern": "sudoers: %group for a group; user host=(runas) commands; 'NOPASSWD:' before commands skips the password.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Privilege delegation (sudoers %group)"],
    },
    {
        "id": "linuxplus-sec-r2-008", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 3, "type": "mcq",
        "stem": "Apache (httpd) needs to make outbound network connections, but SELinux is blocking it. "
                "Which command enables the relevant SELinux boolean PERSISTENTLY across reboots?",
        "options": [
            {"id": "A", "text": "setsebool httpd_can_network_connect on"},
            {"id": "B", "text": "setsebool -P httpd_can_network_connect on"},
            {"id": "C", "text": "getsebool httpd_can_network_connect"},
            {"id": "D", "text": "semanage boolean httpd_can_network_connect"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "setsebool -P writes the boolean to persistent policy so it survives reboots; here it "
                       "lets httpd open network connections.",
            "distractors": {
                "A": "Without -P the change is runtime-only and is lost at the next reboot.",
                "C": "getsebool READS a boolean's current value; it does not change it.",
                "D": "The syntax is incomplete/incorrect; booleans are toggled with setsebool (-P to persist), not 'semanage boolean <name>' alone.",
            },
            "exam_pattern": "SELinux booleans: 'getsebool -a' to view, 'setsebool -P <bool> on' to set persistently.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SELinux booleans (setsebool -P)"],
    },
    {
        "id": "linuxplus-sec-r2-009", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 2, "type": "mcq",
        "stem": "Which command shows the SELinux security context (user:role:type:level) of the files in "
                "the current directory?",
        "options": [
            {"id": "A", "text": "ls -Z"},
            {"id": "B", "text": "ls -l"},
            {"id": "C", "text": "ls -i"},
            {"id": "D", "text": "stat -c %a ."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ls -Z appends each file's SELinux context; the type field (e.g., httpd_sys_content_t) "
                       "is what SELinux checks. 'ps -Z' and 'id -Z' show process and user contexts.",
            "distractors": {
                "A": "",
                "B": "ls -l shows the standard DAC permissions, owner, and group but not the SELinux context.",
                "C": "ls -i shows inode numbers, not security contexts.",
                "D": "stat -c %a prints the octal permission bits, not the SELinux label.",
            },
            "exam_pattern": "View SELinux labels with -Z: 'ls -Z' (files), 'ps -Z' (processes), 'id -Z' (your context).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SELinux contexts (ls -Z)"],
    },
    {
        "id": "linuxplus-sec-r2-010", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 3, "type": "mcq",
        "stem": "You configured a web app to listen on TCP 8090, but with SELinux enforcing, httpd "
                "cannot bind to it. Which command adds 8090 to the allowed http port type so the service "
                "can bind?",
        "options": [
            {"id": "A", "text": "semanage port -a -t http_port_t -p tcp 8090"},
            {"id": "B", "text": "firewall-cmd --add-port=8090/tcp"},
            {"id": "C", "text": "setsebool -P http_port_t 8090"},
            {"id": "D", "text": "restorecon -v -p tcp 8090"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "semanage port -a -t http_port_t -p tcp 8090 labels TCP 8090 as an http port type, so "
                       "SELinux permits httpd to bind it. (If the port already has a type, use -m to modify.)",
            "distractors": {
                "A": "",
                "B": "firewall-cmd opens the port in the FIREWALL; it does not change the SELinux port label that is blocking the bind.",
                "C": "setsebool toggles boolean switches; it does not map a port number to a type.",
                "D": "restorecon relabels FILES to their default context; it does not manage port labels.",
            },
            "exam_pattern": "Nonstandard service port under SELinux: 'semanage port -a -t <type> -p tcp <port>' (then open the firewall).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SELinux port labeling (semanage port)"],
    },
    {
        "id": "linuxplus-sec-r2-011", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_access_control", "difficulty": 2, "type": "mcq",
        "stem": "On an Ubuntu host you want the AppArmor profile for nginx to actively BLOCK (not just "
                "log) policy violations. Which command puts that profile into enforce mode?",
        "options": [
            {"id": "A", "text": "aa-complain /etc/apparmor.d/usr.sbin.nginx"},
            {"id": "B", "text": "aa-enforce /etc/apparmor.d/usr.sbin.nginx"},
            {"id": "C", "text": "setenforce 1"},
            {"id": "D", "text": "aa-disable /etc/apparmor.d/usr.sbin.nginx"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "aa-enforce switches the named AppArmor profile to enforce mode, where violations are "
                       "denied and logged. aa-complain would only log them.",
            "distractors": {
                "A": "aa-complain puts the profile in COMPLAIN mode: it permits and merely logs violations — the opposite of blocking.",
                "C": "setenforce is an SELinux command; it has no effect on AppArmor profiles.",
                "D": "aa-disable UNLOADS the profile entirely, removing protection rather than enforcing it.",
            },
            "exam_pattern": "AppArmor modes: aa-enforce (block), aa-complain (log only), aa-disable (unload); check with aa-status.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — AppArmor enforcement (aa-enforce)"],
    },

    # ----- linuxp_firewall (5) ---------------------------------------------
    {
        "id": "linuxplus-sec-r2-012", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 3, "type": "mcq",
        "stem": "You added several firewalld rules in the RUNTIME configuration only (no --permanent) and "
                "they work. Which command saves the current runtime rules into the permanent "
                "configuration so they survive a reboot?",
        "options": [
            {"id": "A", "text": "firewall-cmd --reload"},
            {"id": "B", "text": "firewall-cmd --runtime-to-permanent"},
            {"id": "C", "text": "firewall-cmd --permanent --reload"},
            {"id": "D", "text": "systemctl restart firewalld"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "firewall-cmd --runtime-to-permanent copies the active runtime ruleset into the "
                       "permanent config, preserving changes you made without --permanent.",
            "distractors": {
                "A": "--reload REPLACES the runtime config with the permanent one, DISCARDING your unsaved runtime rules.",
                "C": "--permanent --reload is not a valid combination for saving; --reload always applies permanent over runtime.",
                "D": "Restarting firewalld reloads permanent rules and loses the runtime-only changes, just like --reload.",
            },
            "exam_pattern": "Save runtime rules: '--runtime-to-permanent'. '--reload' goes the other way (permanent -> runtime).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — firewalld persistence (runtime-to-permanent)"],
    },
    {
        "id": "linuxplus-sec-r2-013", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "mcq",
        "stem": "A custom service listens on TCP 8080. Which firewalld command permanently opens that "
                "specific port (not a predefined service name) in the default zone?",
        "options": [
            {"id": "A", "text": "firewall-cmd --permanent --add-port=8080/tcp"},
            {"id": "B", "text": "firewall-cmd --permanent --add-service=8080"},
            {"id": "C", "text": "firewall-cmd --add-port=8080"},
            {"id": "D", "text": "firewall-cmd --permanent --add-port=8080/all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "--add-port takes port/protocol, so '--permanent --add-port=8080/tcp' opens TCP 8080; "
                       "follow with 'firewall-cmd --reload' to activate it.",
            "distractors": {
                "A": "",
                "B": "--add-service expects a named service (like http), not a bare port number.",
                "C": "A port rule requires the protocol (8080/tcp or 8080/udp); '8080' alone is invalid, and without --permanent it is runtime-only.",
                "D": "'/all' is not a valid protocol; it must be tcp, udp, sctp, or dccp.",
            },
            "exam_pattern": "Open a raw port: '--add-port=<port>/<proto>'; open a known service: '--add-service=<name>'; then --reload.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — firewalld ports (--add-port)"],
    },
    {
        "id": "linuxplus-sec-r2-014", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 3, "type": "mcq",
        "stem": "Which firewalld command changes the DEFAULT zone (the zone applied to interfaces not "
                "explicitly assigned) to 'dmz'?",
        "options": [
            {"id": "A", "text": "firewall-cmd --set-default-zone=dmz"},
            {"id": "B", "text": "firewall-cmd --get-default-zone=dmz"},
            {"id": "C", "text": "firewall-cmd --zone=dmz --change-interface"},
            {"id": "D", "text": "firewall-cmd --permanent --new-zone=dmz"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "firewall-cmd --set-default-zone=dmz sets the default zone immediately and permanently "
                       "(it is one of the few settings applied to both at once).",
            "distractors": {
                "A": "",
                "B": "--get-default-zone READS the current default and takes no value; '=dmz' is invalid.",
                "C": "--change-interface reassigns a specific interface to a zone; it needs an interface and does not set the default.",
                "D": "--new-zone CREATES a new (empty) zone definition; it does not make it the default.",
            },
            "exam_pattern": "Zones: '--get-active-zones' to view, '--set-default-zone=<z>' to change the catch-all default.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — firewalld zones (--set-default-zone)"],
    },
    {
        "id": "linuxplus-sec-r2-015", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "mcq",
        "stem": "On Ubuntu with ufw, you want to set the baseline policy to DENY all inbound traffic by "
                "default (then selectively allow services). Which command sets that default?",
        "options": [
            {"id": "A", "text": "ufw default deny incoming"},
            {"id": "B", "text": "ufw deny incoming"},
            {"id": "C", "text": "ufw disable incoming"},
            {"id": "D", "text": "ufw reset incoming"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ufw default deny incoming sets the catch-all inbound policy to deny; specific "
                       "'ufw allow' rules then permit the services you choose.",
            "distractors": {
                "A": "",
                "B": "'ufw deny incoming' is not the default-policy syntax; the policy keyword is 'default'.",
                "C": "'ufw disable' turns the firewall OFF entirely; 'disable incoming' is not valid.",
                "D": "'ufw reset' wipes all rules back to defaults; it does not set a deny policy for inbound.",
            },
            "exam_pattern": "ufw baseline: 'ufw default deny incoming' + 'ufw default allow outgoing', then 'ufw allow <svc>'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — ufw default policy"],
    },
    {
        "id": "linuxplus-sec-r2-016", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_firewall", "difficulty": 2, "type": "fill",
        "stem": "Using the modern nftables tool, which command prints the ENTIRE active ruleset (all "
                "tables, chains, and rules) in one listing? (full command, three words)",
        "correct": ["nft list ruleset", "sudo nft list ruleset"],
        "explanation": {
            "correct": "nft list ruleset dumps every table, chain, and rule currently loaded in the kernel's "
                       "nftables engine — the nftables equivalent of 'iptables -S' for the whole system.",
            "distractors": {},
            "exam_pattern": "nftables: 'nft list ruleset' (everything), 'nft list table <family> <name>' (one table); add rules with 'nft add rule'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — nftables (nft list ruleset)"],
    },

    # ----- linuxp_ssh_hardening (5) ----------------------------------------
    {
        "id": "linuxplus-sec-r2-017", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 2, "type": "mcq",
        "stem": "After deploying SSH keys to all users, you want to FORCE key-based authentication by "
                "disabling password logins. Which sshd_config directive does this?",
        "options": [
            {"id": "A", "text": "PasswordAuthentication no"},
            {"id": "B", "text": "PermitEmptyPasswords no"},
            {"id": "C", "text": "ChallengeResponseAuthentication no"},
            {"id": "D", "text": "UsePAM no"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PasswordAuthentication no makes sshd reject password logins, so only key-based (or "
                       "other configured) authentication succeeds; restart sshd to apply.",
            "distractors": {
                "A": "",
                "B": "PermitEmptyPasswords no only blocks accounts with BLANK passwords; normal passwords still work.",
                "C": "ChallengeResponseAuthentication governs keyboard-interactive/OTP methods, not ordinary password auth by itself.",
                "D": "UsePAM no disables the PAM stack (affecting account/session handling) and is not the switch for password login.",
            },
            "exam_pattern": "Keys-only SSH: 'PasswordAuthentication no' (plus PermitRootLogin no); reload sshd after editing.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH hardening (PasswordAuthentication)"],
    },
    {
        "id": "linuxplus-sec-r2-018", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 3, "type": "mcq",
        "stem": "From your workstation you need to reach a database on the remote server's localhost:5432 "
                "by connecting to your own local port 5432, tunneled over SSH. Which command sets up that "
                "local port forward?",
        "options": [
            {"id": "A", "text": "ssh -L 5432:localhost:5432 user@server"},
            {"id": "B", "text": "ssh -R 5432:localhost:5432 user@server"},
            {"id": "C", "text": "ssh -D 5432 user@server"},
            {"id": "D", "text": "ssh -X user@server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ssh -L local_port:host:host_port forwards a LOCAL port through the SSH connection; "
                       "'-L 5432:localhost:5432' makes your localhost:5432 reach the server's own localhost:5432.",
            "distractors": {
                "A": "",
                "B": "-R is a REMOTE forward (opens a port on the server that tunnels back to you) — the opposite direction.",
                "C": "-D creates a SOCKS dynamic proxy, not a fixed port-to-host forward.",
                "D": "-X enables X11 forwarding for GUI apps, not a TCP port tunnel.",
            },
            "exam_pattern": "SSH tunnels: -L local forward, -R remote forward, -D dynamic SOCKS proxy.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH tunneling (ssh -L)"],
    },
    {
        "id": "linuxplus-sec-r2-019", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 2, "type": "mcq",
        "stem": "Which sshd_config directive restricts SSH logins so that ONLY the users alice and bob "
                "may authenticate (everyone else is refused)?",
        "options": [
            {"id": "A", "text": "AllowUsers alice bob"},
            {"id": "B", "text": "PermitUsers alice bob"},
            {"id": "C", "text": "AllowGroups alice bob"},
            {"id": "D", "text": "DenyUsers alice bob"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AllowUsers lists the only accounts permitted to log in via SSH; if present, any user "
                       "not listed is denied.",
            "distractors": {
                "A": "",
                "B": "PermitUsers is not a valid sshd_config directive.",
                "C": "AllowGroups restricts by GROUP membership, not by these specific usernames (alice/bob here are users, not groups).",
                "D": "DenyUsers would BLOCK alice and bob while allowing everyone else — the opposite of the requirement.",
            },
            "exam_pattern": "sshd access lists: AllowUsers/AllowGroups (whitelist) vs DenyUsers/DenyGroups (blacklist); Allow wins when set.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH access control (AllowUsers)"],
    },
    {
        "id": "linuxplus-sec-r2-020", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 2, "type": "mcq",
        "stem": "You frequently run 'ssh web' and want it to connect as user deploy to host 10.0.0.9 on "
                "port 2222 using a specific key. In which file do you define this per-host CLIENT alias?",
        "options": [
            {"id": "A", "text": "~/.ssh/config"},
            {"id": "B", "text": "/etc/ssh/sshd_config"},
            {"id": "C", "text": "~/.ssh/known_hosts"},
            {"id": "D", "text": "~/.ssh/authorized_keys"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The per-user client file ~/.ssh/config defines Host blocks with HostName, User, Port, "
                       "and IdentityFile, so 'ssh web' expands to the full connection details.",
            "distractors": {
                "A": "",
                "B": "/etc/ssh/sshd_config configures the SSH SERVER daemon, not the client's host aliases.",
                "C": "~/.ssh/known_hosts stores the host keys of servers you've connected to; it is not for aliases.",
                "D": "~/.ssh/authorized_keys lists public keys permitted to log IN to this account; it is server-side, not a client alias.",
            },
            "exam_pattern": "Client shortcuts/options = ~/.ssh/config (Host/HostName/User/Port/IdentityFile); server options = sshd_config.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH client config (~/.ssh/config)"],
    },
    {
        "id": "linuxplus-sec-r2-021", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_ssh_hardening", "difficulty": 3, "type": "mcq",
        "stem": "A user copied their public key to a server but key-based login still prompts for a "
                "password. The server's sshd has StrictModes on. What is the MOST likely cause?",
        "options": [
            {"id": "A", "text": "The ~/.ssh directory or authorized_keys file has overly open permissions (e.g., group/world-writable)"},
            {"id": "B", "text": "The private key was copied to the server instead of the public key"},
            {"id": "C", "text": "The server is missing /etc/ssh/ssh_config"},
            {"id": "D", "text": "PermitRootLogin is set to no"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "With StrictModes on, sshd refuses to use keys if ~/.ssh (should be 700) or "
                       "authorized_keys (should be 600) are too permissive, silently falling back to passwords.",
            "distractors": {
                "A": "",
                "B": "authorized_keys must contain the PUBLIC key; while copying the private key is wrong, sshd would still read a valid public key — permissions are the classic StrictModes failure.",
                "C": "ssh_config is the client file; its absence does not block server-side key auth, and sshd uses sshd_config.",
                "D": "PermitRootLogin only affects the root account, not an ordinary user's key login.",
            },
            "exam_pattern": "Key auth silently falls back to password => fix perms: chmod 700 ~/.ssh, chmod 600 authorized_keys (StrictModes).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — SSH key permissions (StrictModes)"],
    },

    # ----- linuxp_crypto_certs (5) -----------------------------------------
    {
        "id": "linuxplus-sec-r2-022", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 2, "type": "mcq",
        "stem": "You downloaded an ISO and the vendor published its SHA-256 checksum. Which command "
                "computes the ISO's hash so you can compare it against the published value for integrity?",
        "options": [
            {"id": "A", "text": "sha256sum distro.iso"},
            {"id": "B", "text": "openssl genrsa distro.iso"},
            {"id": "C", "text": "gpg --encrypt distro.iso"},
            {"id": "D", "text": "md5sum -c distro.iso"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "sha256sum distro.iso prints the file's SHA-256 digest; if it matches the vendor's "
                       "published value the download is intact. ('sha256sum -c FILE.sha256' checks it automatically.)",
            "distractors": {
                "A": "",
                "B": "openssl genrsa GENERATES an RSA private key; it does not hash a file.",
                "C": "gpg --encrypt protects CONFIDENTIALITY; it does not produce a verification checksum.",
                "D": "md5sum -c expects a checksum FILE as input and MD5 is weak; the task calls for computing a SHA-256 hash.",
            },
            "exam_pattern": "Integrity check: sha256sum <file> and compare, or 'sha256sum -c <file>.sha256'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Integrity verification (sha256sum)"],
    },
    {
        "id": "linuxplus-sec-r2-023", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 3, "type": "mcq",
        "stem": "To troubleshoot a TLS handshake, you need to connect to the live service at "
                "www.example.com:443 and view the certificate chain it presents. Which OpenSSL command "
                "does this?",
        "options": [
            {"id": "A", "text": "openssl x509 -in www.example.com:443"},
            {"id": "B", "text": "openssl s_client -connect www.example.com:443"},
            {"id": "C", "text": "openssl req -connect www.example.com:443"},
            {"id": "D", "text": "openssl verify www.example.com:443"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "openssl s_client -connect host:443 opens a TLS connection and prints the presented "
                       "certificate chain and handshake details, ideal for diagnosing a live endpoint.",
            "distractors": {
                "A": "openssl x509 parses a certificate FILE; it cannot take a host:port to connect to.",
                "C": "openssl req works with certificate signing REQUESTS and has no -connect option.",
                "D": "openssl verify checks a certificate FILE against a CA chain; it does not connect to a server.",
            },
            "exam_pattern": "Inspect a live TLS endpoint: 'openssl s_client -connect host:443'; inspect a cert file: 'openssl x509 -in file -text'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — TLS troubleshooting (openssl s_client)"],
    },
    {
        "id": "linuxplus-sec-r2-024", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 2, "type": "mcq",
        "stem": "A project ships release.tar.gz with a detached signature release.tar.gz.asc. After "
                "importing the maintainer's public key, which command verifies that the signature is "
                "valid for the file?",
        "options": [
            {"id": "A", "text": "gpg --verify release.tar.gz.asc release.tar.gz"},
            {"id": "B", "text": "gpg --decrypt release.tar.gz"},
            {"id": "C", "text": "gpg --sign release.tar.gz"},
            {"id": "D", "text": "sha256sum release.tar.gz.asc"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "gpg --verify <signature> <file> checks the detached signature against the file using "
                       "the signer's imported public key, confirming authenticity and integrity.",
            "distractors": {
                "A": "",
                "B": "--decrypt is for encrypted content; a detached signature is not an encrypted payload.",
                "C": "--sign CREATES a signature; it does not verify an existing one.",
                "D": "sha256sum only hashes the signature file; it does not validate a GPG signature.",
            },
            "exam_pattern": "Verify a detached signature: 'gpg --verify file.asc file' (import the signer's public key first).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Signature verification (gpg --verify)"],
    },
    {
        "id": "linuxplus-sec-r2-025", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 3, "type": "fill",
        "stem": "Which configuration file lists LUKS-encrypted block devices to be unlocked automatically "
                "early in boot (the encryption counterpart to /etc/fstab)? (full path)",
        "correct": ["/etc/crypttab", "etc/crypttab"],
        "explanation": {
            "correct": "/etc/crypttab maps each encrypted device (name, backing device, key file, and "
                       "options) so systemd unlocks it at boot; the resulting /dev/mapper device is then mounted via /etc/fstab.",
            "distractors": {},
            "exam_pattern": "LUKS auto-unlock at boot = /etc/crypttab; the decrypted mapper device is mounted via /etc/fstab.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Disk encryption (/etc/crypttab)"],
    },
    {
        "id": "linuxplus-sec-r2-026", "exam": "linuxplus", "domain": "linuxp_security",
        "subtopic": "linuxp_crypto_certs", "difficulty": 2, "type": "mcq",
        "stem": "A LUKS volume was unlocked as /dev/mapper/vault and has already been unmounted. Which "
                "command removes the decrypted mapping so the data is locked again?",
        "options": [
            {"id": "A", "text": "cryptsetup luksClose vault"},
            {"id": "B", "text": "cryptsetup luksOpen vault"},
            {"id": "C", "text": "umount /dev/mapper/vault"},
            {"id": "D", "text": "cryptsetup luksFormat vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "cryptsetup luksClose vault (equivalently 'cryptsetup close vault') tears down the "
                       "/dev/mapper/vault mapping, so the plaintext device disappears and the volume is locked.",
            "distractors": {
                "A": "",
                "B": "luksOpen UNLOCKS a device (creates the mapping) — the opposite of what is needed.",
                "C": "umount detaches a mounted filesystem but leaves the decrypted mapper device active.",
                "D": "luksFormat would REINITIALIZE the LUKS header, destroying the data.",
            },
            "exam_pattern": "LUKS lifecycle: luksOpen (unlock) -> mount -> umount -> luksClose (lock/remove mapping).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 2 — Disk encryption (cryptsetup luksClose)"],
    },

    # ================= DOMAIN 3: SCRIPTING, CONTAINERS & AUTOMATION (23) =================

    # ----- linuxp_bash_scripting (9) ---------------------------------------
    {
        "id": "linuxplus-scr-r2-001", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 1, "type": "mcq",
        "stem": "Inside a Bash script invoked as './deploy.sh prod', which variable expands to the first "
                "positional argument, 'prod'?",
        "options": [
            {"id": "A", "text": "$0"},
            {"id": "B", "text": "$1"},
            {"id": "C", "text": "$#"},
            {"id": "D", "text": "$*"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "$1 is the first positional parameter (here 'prod'); $2 would be the second, and so on.",
            "distractors": {
                "A": "$0 is the script's own name/path ('./deploy.sh'), not the first argument.",
                "C": "$# is the COUNT of arguments, not their values.",
                "D": "$* expands to ALL the positional parameters joined, not just the first.",
            },
            "exam_pattern": "$0 script name, $1..$9 positional args, $# count, $@/$* all args, 'shift' drops $1.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Positional parameters ($1)"],
    },
    {
        "id": "linuxplus-scr-r2-002", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "Which syntax captures the OUTPUT of the 'date +%F' command into the variable TODAY in a "
                "modern, nestable way?",
        "options": [
            {"id": "A", "text": "TODAY=$(date +%F)"},
            {"id": "B", "text": "TODAY=(date +%F)"},
            {"id": "C", "text": "TODAY=${date +%F}"},
            {"id": "D", "text": "TODAY=$[date +%F]"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "$(command) is command substitution: it runs the command and substitutes its stdout. "
                       "It is preferred over backticks because it nests cleanly.",
            "distractors": {
                "A": "",
                "B": "( ... ) without the leading $ creates an ARRAY from the words, not command output.",
                "C": "${ ... } is parameter/variable expansion, not command execution.",
                "D": "$[ ... ] is an obsolete ARITHMETIC form; it does not run commands (and is deprecated in favor of $(( )) ).",
            },
            "exam_pattern": "Command substitution = $(cmd) (preferred) or `cmd` (legacy backticks); arithmetic = $(( expr )).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Command substitution ($( ))"],
    },
    {
        "id": "linuxplus-scr-r2-003", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 3, "type": "mcq",
        "stem": "You want a command's error messages (stderr) to be written to the SAME place its normal "
                "output (stdout) already goes — a log file. Which redirection achieves this?",
        "options": [
            {"id": "A", "text": "myapp > app.log 2>&1"},
            {"id": "B", "text": "myapp > app.log 1>&2"},
            {"id": "C", "text": "myapp 2> app.log >&1"},
            {"id": "D", "text": "myapp > app.log 2>1"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "First '> app.log' points stdout (fd 1) at the file, then '2>&1' makes stderr (fd 2) "
                       "follow fd 1 to the same file. Order matters: redirect stdout before duplicating it.",
            "distractors": {
                "A": "",
                "B": "1>&2 sends stdout to wherever stderr points (the terminal), the reverse of the goal.",
                "C": "'>&1' here is evaluated before stdout is set to the file, so streams don't both land in app.log as intended.",
                "D": "'2>1' redirects stderr to a FILE literally named '1', not to file descriptor 1 (that needs the &).",
            },
            "exam_pattern": "Merge streams: 'cmd > file 2>&1' (stdout to file, then stderr to stdout). The & marks a descriptor.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Redirection (2>&1)"],
    },
    {
        "id": "linuxplus-scr-r2-004", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "Which Bash construct correctly assigns the integer SUM of 5 and 3 to the variable TOTAL?",
        "options": [
            {"id": "A", "text": "TOTAL=$((5 + 3))"},
            {"id": "B", "text": "TOTAL=5 + 3"},
            {"id": "C", "text": "TOTAL=$(5 + 3)"},
            {"id": "D", "text": "TOTAL='5 + 3'"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "$(( expression )) performs integer arithmetic and substitutes the result, so TOTAL "
                       "becomes 8.",
            "distractors": {
                "A": "",
                "B": "Bash would try to assign '5' and then run '+' and '3' as a command; it does not do math here.",
                "C": "$( ) is command substitution; it would try to EXECUTE '5' as a command and fail.",
                "D": "Quoting makes TOTAL the literal string '5 + 3', with no arithmetic performed.",
            },
            "exam_pattern": "Integer math: $(( expr )); also 'let x=5+3' or (( x = 5 + 3 )). Floating point needs bc/awk.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Arithmetic expansion ($(( )))"],
    },
    {
        "id": "linuxplus-scr-r2-005", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "Which test correctly checks, in an if statement, whether the regular file "
                "/etc/app.conf EXISTS before the script reads it?",
        "options": [
            {"id": "A", "text": "if [ -f /etc/app.conf ]; then"},
            {"id": "B", "text": "if [ -d /etc/app.conf ]; then"},
            {"id": "C", "text": "if [ -z /etc/app.conf ]; then"},
            {"id": "D", "text": "if [ -x /etc/app.conf ]; then"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "-f is true when the path exists AND is a regular file, the correct existence check "
                       "before reading a config file.",
            "distractors": {
                "A": "",
                "B": "-d tests for a DIRECTORY; a config file is not a directory.",
                "C": "-z tests whether a STRING is empty, not whether a file exists.",
                "D": "-x tests whether a file is EXECUTABLE; a config file need not be executable.",
            },
            "exam_pattern": "File tests: -e exists, -f regular file, -d directory, -r readable, -s non-empty, -x executable.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — File test operators ([ -f ])"],
    },
    {
        "id": "linuxplus-scr-r2-006", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 3, "type": "mcq",
        "stem": "Which loop reads the file hosts.txt one line at a time, placing each line in the "
                "variable 'line' for processing, and handles lines without a trailing newline safely?",
        "options": [
            {"id": "A", "text": "while read -r line; do echo \"$line\"; done < hosts.txt"},
            {"id": "B", "text": "for line in hosts.txt; do echo \"$line\"; done"},
            {"id": "C", "text": "while read -r line; do echo \"$line\"; done | hosts.txt"},
            {"id": "D", "text": "read hosts.txt | while line; do echo \"$line\"; done"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "'while read -r line; do ...; done < file' reads each line into 'line' (the -r keeps "
                       "backslashes literal) and the '< file' feeds the file on stdin, including a final unterminated line in most cases.",
            "distractors": {
                "A": "",
                "B": "for iterates over the single word 'hosts.txt' (the filename), not its contents.",
                "C": "A pipe sends the loop's OUTPUT to hosts.txt as a command; it does not feed the file INTO the loop.",
                "D": "'read hosts.txt' reads a line into a variable literally named hosts.txt; the syntax is wrong.",
            },
            "exam_pattern": "Read a file line-by-line: 'while IFS= read -r line; do ...; done < file' (redirect in, not pipe).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Reading input (while read)"],
    },
    {
        "id": "linuxplus-scr-r2-007", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "In the command 'mkdir /data && cd /data', what does the && operator guarantee?",
        "options": [
            {"id": "A", "text": "cd /data runs only if mkdir /data succeeded (exit status 0)"},
            {"id": "B", "text": "cd /data runs only if mkdir /data failed"},
            {"id": "C", "text": "Both commands always run regardless of outcome"},
            {"id": "D", "text": "The two commands run simultaneously in parallel"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "&& is logical AND: the right-hand command executes only when the left-hand command "
                       "exits 0 (success), so cd runs only if the directory was created.",
            "distractors": {
                "A": "",
                "B": "That describes ||  (logical OR), which runs the right side only when the left side FAILS.",
                "C": "';' separates commands to always run both; && conditions the second on the first's success.",
                "D": "&& is sequential, not parallel; '&' (single) is what backgrounds a command.",
            },
            "exam_pattern": "cmd1 && cmd2 (run cmd2 if cmd1 succeeds); cmd1 || cmd2 (run cmd2 if cmd1 fails); ';' = always.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Conditional execution (&&)"],
    },
    {
        "id": "linuxplus-scr-r2-008", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 3, "type": "mcq",
        "stem": "In a script, you want ${PORT} to use the value of the PORT variable if it is set, but "
                "fall back to 8080 when PORT is unset or empty — WITHOUT permanently assigning PORT. "
                "Which expansion does this?",
        "options": [
            {"id": "A", "text": "${PORT:-8080}"},
            {"id": "B", "text": "${PORT:=8080}"},
            {"id": "C", "text": "${PORT:+8080}"},
            {"id": "D", "text": "${PORT:?8080}"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "${PORT:-8080} substitutes 8080 when PORT is unset or empty but leaves PORT itself "
                       "unchanged — a read-only default.",
            "distractors": {
                "A": "",
                "B": ":= also ASSIGNS 8080 to PORT as a side effect, which the requirement forbids.",
                "C": ":+ returns 8080 only when PORT IS set (the opposite condition), otherwise nothing.",
                "D": ":? prints an error and exits if PORT is unset; it does not provide a usable default value.",
            },
            "exam_pattern": "Defaults: ${v:-x} use x if unset; ${v:=x} use AND assign x; ${v:+x} x only if set; ${v:?msg} error if unset.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Parameter expansion (${var:-default})"],
    },
    {
        "id": "linuxplus-scr-r2-009", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "Which redirection APPENDS a line to /var/log/app-custom.log without truncating the file, "
                "while discarding any error output?",
        "options": [
            {"id": "A", "text": "echo done >> /var/log/app-custom.log 2>/dev/null"},
            {"id": "B", "text": "echo done > /var/log/app-custom.log 2>/dev/null"},
            {"id": "C", "text": "echo done >> /var/log/app-custom.log 2>&1"},
            {"id": "D", "text": "echo done < /var/log/app-custom.log"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": ">> appends to the file (preserving existing contents), and '2>/dev/null' throws "
                       "away stderr by sending it to the null device.",
            "distractors": {
                "A": "",
                "B": "A single '>' TRUNCATES the log to just this line, losing prior entries.",
                "C": "This appends, but '2>&1' sends errors INTO the log rather than discarding them.",
                "D": "'<' redirects the file as INPUT to echo (which ignores stdin); it writes nothing to the log.",
            },
            "exam_pattern": ">> append, > overwrite/truncate; 2>/dev/null discards errors; /dev/null = the bit bucket.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Redirection (append, /dev/null)"],
    },

    # ----- linuxp_git_version (5) ------------------------------------------
    {
        "id": "linuxplus-scr-r2-010", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 2, "type": "mcq",
        "stem": "Which command creates a new branch named 'hotfix' AND immediately switches your working "
                "tree to it, in one step?",
        "options": [
            {"id": "A", "text": "git branch hotfix"},
            {"id": "B", "text": "git checkout -b hotfix"},
            {"id": "C", "text": "git switch hotfix"},
            {"id": "D", "text": "git merge -b hotfix"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "git checkout -b hotfix (modern equivalent: 'git switch -c hotfix') creates the branch "
                       "and checks it out together.",
            "distractors": {
                "A": "git branch hotfix only CREATES the branch; you remain on the current one until you check out.",
                "C": "git switch hotfix (without -c) tries to switch to an EXISTING branch and errors if it doesn't exist.",
                "D": "git merge integrates another branch's history; '-b' is not a merge option and it does not create branches.",
            },
            "exam_pattern": "Create+switch: 'git checkout -b <name>' or 'git switch -c <name>'; 'git branch <name>' only creates.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Branching (git checkout -b)"],
    },
    {
        "id": "linuxplus-scr-r2-011", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 2, "type": "mcq",
        "stem": "What is the key difference between 'git fetch' and 'git pull'?",
        "options": [
            {"id": "A", "text": "git fetch downloads remote commits but does NOT merge them; git pull fetches AND merges into your branch"},
            {"id": "B", "text": "git fetch merges immediately; git pull only downloads"},
            {"id": "C", "text": "They are identical aliases"},
            {"id": "D", "text": "git fetch uploads your commits; git pull downloads commits"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "git fetch updates your remote-tracking refs without changing your working branch; git "
                       "pull is essentially 'fetch then merge' (or rebase), so it also integrates the changes.",
            "distractors": {
                "A": "",
                "B": "Reversed: fetch does NOT merge; pull is the one that merges.",
                "C": "They differ: only pull modifies your current branch by merging.",
                "D": "Neither uploads; 'git push' uploads commits. Both fetch and pull download.",
            },
            "exam_pattern": "fetch = download only (safe); pull = fetch + merge/rebase (updates your branch); push = upload.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Remotes (git fetch vs pull)"],
    },
    {
        "id": "linuxplus-scr-r2-012", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 3, "type": "mcq",
        "stem": "A bad commit was already pushed to the shared main branch. Which command creates a NEW "
                "commit that undoes that commit's changes, preserving history (safe for shared branches)?",
        "options": [
            {"id": "A", "text": "git revert <commit>"},
            {"id": "B", "text": "git reset --hard <commit>"},
            {"id": "C", "text": "git rm <commit>"},
            {"id": "D", "text": "git checkout <commit>"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "git revert creates a new commit that applies the inverse of the target commit, undoing "
                       "it without rewriting history — the safe choice on a branch others have pulled.",
            "distractors": {
                "A": "",
                "B": "git reset --hard rewrites history by moving the branch pointer; on a shared branch this forces others into conflicts.",
                "C": "git rm removes FILES from the tree/index; it does not undo a specific commit.",
                "D": "git checkout <commit> just moves you to that commit (detached HEAD); it does not undo anything.",
            },
            "exam_pattern": "Undo a PUSHED commit safely = git revert (adds an inverse commit); git reset rewrites history (local only).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Undoing changes (git revert)"],
    },
    {
        "id": "linuxplus-scr-r2-013", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 1, "type": "fill",
        "stem": "Which file, placed in a Git repository, lists path patterns (such as *.log or build/) "
                "that Git should leave UNTRACKED and not stage? (file name only)",
        "correct": [".gitignore", "gitignore"],
        "explanation": {
            "correct": ".gitignore contains glob patterns for files/directories Git should ignore, keeping "
                       "build artifacts, logs, and secrets out of the repository.",
            "distractors": {},
            "exam_pattern": "Exclude files from tracking with .gitignore (patterns, one per line; '!' re-includes; 'dir/' a folder).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Ignoring files (.gitignore)"],
    },
    {
        "id": "linuxplus-scr-r2-014", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 2, "type": "mcq",
        "stem": "You have uncommitted changes but must quickly switch branches to fix something else. "
                "Which command shelves your changes away (reverting the working tree to a clean HEAD) so "
                "you can reapply them later?",
        "options": [
            {"id": "A", "text": "git stash"},
            {"id": "B", "text": "git commit -a"},
            {"id": "C", "text": "git clean -fd"},
            {"id": "D", "text": "git reset --hard"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "git stash saves your modified tracked files onto a stash stack and restores a clean "
                       "working tree; 'git stash pop' reapplies them afterward.",
            "distractors": {
                "A": "",
                "B": "git commit -a records the changes permanently instead of temporarily shelving them.",
                "C": "git clean -fd DELETES untracked files/directories; it does not preserve your changes.",
                "D": "git reset --hard DISCARDS your changes entirely, with no way to reapply them.",
            },
            "exam_pattern": "Temporarily shelve work = git stash; reapply with 'git stash pop' (or 'git stash apply').",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Stashing (git stash)"],
    },

    # ----- linuxp_containers (5) -------------------------------------------
    {
        "id": "linuxplus-scr-r2-015", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "mcq",
        "stem": "A container named 'web' is running and you need an interactive Bash shell inside it to "
                "investigate. Which command opens that shell?",
        "options": [
            {"id": "A", "text": "docker exec -it web bash"},
            {"id": "B", "text": "docker run -it web bash"},
            {"id": "C", "text": "docker attach web bash"},
            {"id": "D", "text": "docker start -it web bash"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "docker exec runs a new process in an ALREADY-running container; -i keeps stdin open "
                       "and -t allocates a TTY, giving you an interactive shell. (podman exec is identical.)",
            "distractors": {
                "A": "",
                "B": "docker run creates a NEW container from an image; it does not attach to the existing 'web' container.",
                "C": "docker attach connects to the container's main process stdio; it cannot launch a separate bash and can disrupt PID 1.",
                "D": "docker start restarts a stopped container and does not take a command to run interactively.",
            },
            "exam_pattern": "Shell into a RUNNING container: 'docker exec -it <name> bash' (or sh); 'run' is for new containers.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Containers (docker exec -it)"],
    },
    {
        "id": "linuxplus-scr-r2-016", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 1, "type": "mcq",
        "stem": "A container 'api' exited immediately after starting. Which command shows the stdout/"
                "stderr it produced so you can see why it crashed?",
        "options": [
            {"id": "A", "text": "docker logs api"},
            {"id": "B", "text": "docker inspect api"},
            {"id": "C", "text": "docker ps api"},
            {"id": "D", "text": "docker events api"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "docker logs <container> prints the captured stdout/stderr of the container's main "
                       "process, usually revealing the startup error; add -f to follow and --tail N to limit.",
            "distractors": {
                "A": "",
                "B": "docker inspect dumps configuration/metadata JSON, not the application's console output.",
                "C": "docker ps lists containers; it does not show a container's log output.",
                "D": "docker events streams the daemon's lifecycle events, not an individual container's stdout.",
            },
            "exam_pattern": "Diagnose a crashed container with 'docker logs <name>' (podman logs); -f follow, --tail to trim.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Containers (docker logs)"],
    },
    {
        "id": "linuxplus-scr-r2-017", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "mcq",
        "stem": "From a directory containing a Dockerfile, which command BUILDS an image and tags it "
                "myapp:1.0 using the current directory as the build context?",
        "options": [
            {"id": "A", "text": "docker build -t myapp:1.0 ."},
            {"id": "B", "text": "docker run -t myapp:1.0 ."},
            {"id": "C", "text": "docker create myapp:1.0"},
            {"id": "D", "text": "docker commit myapp:1.0 ."},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "docker build reads the Dockerfile in the context path ('.'), and -t myapp:1.0 names "
                       "and tags the resulting image. (podman build uses the same options.)",
            "distractors": {
                "A": "",
                "B": "docker run starts a CONTAINER from an existing image; it does not build one, and -t there allocates a TTY.",
                "C": "docker create makes a container (without starting it) from an image; it does not build an image.",
                "D": "docker commit snapshots a running container into an image; it is not the Dockerfile build workflow.",
            },
            "exam_pattern": "Build+tag: 'docker build -t name:tag <context>'; the final '.' is the build context directory.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Containers (docker build -t)"],
    },
    {
        "id": "linuxplus-scr-r2-018", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 3, "type": "mcq",
        "stem": "In a Dockerfile, which instruction sets the DEFAULT command that runs when the container "
                "starts and can be easily OVERRIDDEN by arguments passed to 'docker run'?",
        "options": [
            {"id": "A", "text": "CMD"},
            {"id": "B", "text": "RUN"},
            {"id": "C", "text": "EXPOSE"},
            {"id": "D", "text": "ENTRYPOINT"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "CMD provides the default command/arguments for a started container, and anything you "
                       "append to 'docker run <image> ...' replaces it.",
            "distractors": {
                "A": "",
                "B": "RUN executes commands at BUILD time to create image layers; it is not the container's start command.",
                "C": "EXPOSE merely documents which ports the container listens on; it runs nothing.",
                "D": "ENTRYPOINT sets a fixed executable that run-time arguments are APPENDED to (not replaced), so it is less easily overridden than CMD.",
            },
            "exam_pattern": "CMD = default, overridable command; ENTRYPOINT = fixed executable (args appended); RUN = build-time step.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Dockerfile (CMD vs ENTRYPOINT)"],
    },
    {
        "id": "linuxplus-scr-r2-019", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "mcq",
        "stem": "You removed a stopped container but the disk is still full of images. Which command "
                "deletes the IMAGE named 'oldimage:latest' (not a container)?",
        "options": [
            {"id": "A", "text": "docker rm oldimage:latest"},
            {"id": "B", "text": "docker rmi oldimage:latest"},
            {"id": "C", "text": "docker stop oldimage:latest"},
            {"id": "D", "text": "docker prune oldimage:latest"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "docker rmi (remove image) deletes an image; docker rm removes CONTAINERS. They are "
                       "distinct object types, which the exam loves to test.",
            "distractors": {
                "A": "docker rm removes a stopped CONTAINER, not an image.",
                "C": "docker stop halts a running container; it deletes nothing.",
                "D": "docker prune (e.g., 'docker image prune') removes UNUSED objects in bulk and does not take a specific image name like this.",
            },
            "exam_pattern": "rm = remove container; rmi = remove image; 'docker image prune' / 'system prune' bulk-cleans unused data.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Containers (docker rmi)"],
    },

    # ----- linuxp_automation (4) -------------------------------------------
    {
        "id": "linuxplus-scr-r2-020", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "mcq",
        "stem": "Which command runs the tasks defined in the Ansible playbook site.yml against the hosts "
                "listed in the inventory file 'hosts'?",
        "options": [
            {"id": "A", "text": "ansible-playbook -i hosts site.yml"},
            {"id": "B", "text": "ansible -i hosts site.yml"},
            {"id": "C", "text": "ansible-vault -i hosts site.yml"},
            {"id": "D", "text": "ansible-galaxy run site.yml"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ansible-playbook runs a playbook; -i names the inventory. 'ansible-playbook -i hosts "
                       "site.yml' executes site.yml's plays against the inventory hosts.",
            "distractors": {
                "A": "",
                "B": "The bare 'ansible' command runs AD-HOC modules (e.g., 'ansible all -m ping'); it does not execute a playbook file.",
                "C": "ansible-vault encrypts/decrypts secret files; it does not run playbooks.",
                "D": "ansible-galaxy installs roles/collections; 'run' is not how you execute a playbook.",
            },
            "exam_pattern": "Run a playbook: 'ansible-playbook -i <inventory> <playbook.yml>'; ad-hoc tasks use 'ansible <hosts> -m <module>'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Ansible (ansible-playbook)"],
    },
    {
        "id": "linuxplus-scr-r2-021", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 3, "type": "mcq",
        "stem": "In an Ansible playbook, you want nginx to restart ONLY when a task actually changes its "
                "config file. Which mechanism links the config task to the restart action?",
        "options": [
            {"id": "A", "text": "A handler that the config task triggers with 'notify'"},
            {"id": "B", "text": "A separate play that always runs 'service restart'"},
            {"id": "C", "text": "The 'when: always' conditional on the restart task"},
            {"id": "D", "text": "A loop over the service name"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Handlers run only when notified by a task that reports 'changed'. The config task uses "
                       "'notify: Restart nginx', and the handler runs once at the end of the play if a change occurred.",
            "distractors": {
                "A": "",
                "B": "An always-restart play defeats idempotency, restarting even when nothing changed.",
                "C": "'when: always' would run the restart every time, not only on change.",
                "D": "A loop repeats a task over items; it does not tie an action to a change event.",
            },
            "exam_pattern": "Change-triggered actions in Ansible = notify + handlers; handlers fire once, at end of play, only if notified.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Ansible (handlers/notify)"],
    },
    {
        "id": "linuxplus-scr-r2-022", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 3, "type": "mcq",
        "stem": "What distinguishes an entry in the system-wide /etc/crontab (or a file in /etc/cron.d) "
                "from a line created with 'crontab -e' for a user?",
        "options": [
            {"id": "A", "text": "The /etc/crontab line has an extra field naming the USER the job runs as, between the day-of-week and the command"},
            {"id": "B", "text": "The /etc/crontab line omits the minute field"},
            {"id": "C", "text": "The /etc/crontab line uses seconds instead of minutes"},
            {"id": "D", "text": "The /etc/crontab line must start with @reboot"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "System crontabs (/etc/crontab, /etc/cron.d/*) add a user field after the five time "
                       "fields, so the format is 'min hour dom mon dow USER command'. Per-user crontabs omit it (they already belong to a user).",
            "distractors": {
                "A": "",
                "B": "Both formats keep all five time fields including the minute; none is omitted.",
                "C": "Standard cron has no seconds field in either location.",
                "D": "@reboot is an optional special schedule available in both; it is not required in /etc/crontab.",
            },
            "exam_pattern": "System crontab = 6 fields incl. a USER column; 'crontab -e' user crontab = 5 time fields + command.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Scheduling (/etc/crontab user field)"],
    },
    {
        "id": "linuxplus-scr-r2-023", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "mcq",
        "stem": "A playbook needs to store a database password in version control safely. Which Ansible "
                "tool encrypts a variables file so its contents are not stored in plaintext?",
        "options": [
            {"id": "A", "text": "ansible-vault encrypt secrets.yml"},
            {"id": "B", "text": "ansible-playbook --encrypt secrets.yml"},
            {"id": "C", "text": "gpg --ansible secrets.yml"},
            {"id": "D", "text": "ansible-galaxy encrypt secrets.yml"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ansible-vault encrypt protects a file (e.g., secrets.yml) with a vault password; the "
                       "ciphertext can be committed, and playbooks decrypt it at runtime with --ask-vault-pass or a vault file.",
            "distractors": {
                "A": "",
                "B": "ansible-playbook has no --encrypt option; it RUNS playbooks (and can prompt for the vault password).",
                "C": "gpg has no --ansible mode; Ansible's own secret store is ansible-vault.",
                "D": "ansible-galaxy manages roles/collections, not secret encryption.",
            },
            "exam_pattern": "Encrypt Ansible secrets with ansible-vault (encrypt/decrypt/view/edit); run with --ask-vault-pass or --vault-id.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 3 — Ansible (ansible-vault)"],
    },

    # ================= DOMAIN 4: TROUBLESHOOTING (34) =================

    # ----- linuxp_ts_storage (6) -------------------------------------------
    {
        "id": "linuxplus-ts-r2-001", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 3, "type": "mcq",
        "stem": "After a filesystem error, the root filesystem was mounted READ-ONLY and services can't "
                "write. You have fixed the underlying issue. Which command remounts / as read-write "
                "without rebooting?",
        "options": [
            {"id": "A", "text": "mount -o remount,rw /"},
            {"id": "B", "text": "mount -o rw /dev/sda1"},
            {"id": "C", "text": "mount -a"},
            {"id": "D", "text": "remount / rw"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "mount -o remount,rw / changes the mount options of the already-mounted root "
                       "filesystem in place, switching it to read-write.",
            "distractors": {
                "A": "",
                "B": "A plain mount of the device without 'remount' fails because / is already mounted (busy).",
                "C": "mount -a mounts fstab entries that aren't mounted; it won't flip an already-mounted root from ro to rw.",
                "D": "'remount' is not a standalone command; remounting is 'mount -o remount,...'.",
            },
            "exam_pattern": "Flip a mounted fs's options live: 'mount -o remount,rw <mountpoint>' (common recovery for a ro root).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Storage troubleshooting (remount,rw)"],
    },
    {
        "id": "linuxplus-ts-r2-002", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 3, "type": "mcq",
        "stem": "A large log file was deleted to free space, but 'df' still shows the filesystem full. "
                "The space is not reclaimed because a process still holds the deleted file open. What is "
                "the correct next step?",
        "options": [
            {"id": "A", "text": "Identify the holding process (e.g., lsof | grep deleted) and restart/stop it so the file handle closes"},
            {"id": "B", "text": "Run 'sync' repeatedly until the space returns"},
            {"id": "C", "text": "Delete the file again with rm -f"},
            {"id": "D", "text": "Run 'df -i' to delete inodes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Space is freed only when the LAST open handle to a deleted file closes. Find the "
                       "holder with 'lsof | grep deleted' (or 'lsof +L1') and restart/stop it to release the space.",
            "distractors": {
                "A": "",
                "B": "sync flushes buffers to disk; it does not release a file still held open by a process.",
                "C": "The file is already gone from the directory; rm cannot act on it again and would not help.",
                "D": "df -i only REPORTS inode usage; it does not delete inodes or free the held blocks.",
            },
            "exam_pattern": "Deleted file but space not freed => a process holds it open. 'lsof | grep deleted', then restart that process.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Storage troubleshooting (open deleted files)"],
    },
    {
        "id": "linuxplus-ts-r2-003", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 3, "type": "mcq",
        "stem": "An XFS data filesystem on /dev/sdb1 is corrupt. It is unmounted. Which command checks "
                "and repairs an XFS filesystem (note that fsck.xfs does nothing on XFS)?",
        "options": [
            {"id": "A", "text": "xfs_repair /dev/sdb1"},
            {"id": "B", "text": "fsck.ext4 /dev/sdb1"},
            {"id": "C", "text": "e2fsck -f /dev/sdb1"},
            {"id": "D", "text": "mkfs.xfs /dev/sdb1"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "XFS is repaired with xfs_repair on an UNMOUNTED device; fsck.xfs intentionally does "
                       "nothing because XFS integrity is handled by log replay and xfs_repair.",
            "distractors": {
                "A": "",
                "B": "fsck.ext4 is for EXT filesystems; it cannot repair XFS.",
                "C": "e2fsck is the ext2/3/4 checker; wrong filesystem family for XFS.",
                "D": "mkfs.xfs REFORMATS the device, destroying all data rather than repairing it.",
            },
            "exam_pattern": "Repair by fs type: ext -> e2fsck/fsck.ext4; XFS -> xfs_repair (unmounted); fsck.xfs is a no-op.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Filesystem repair (xfs_repair)"],
    },
    {
        "id": "linuxplus-ts-r2-004", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "mcq",
        "stem": "A disk is throwing read errors and you suspect it is failing. Which command queries the "
                "drive's built-in SMART data to report its overall health?",
        "options": [
            {"id": "A", "text": "smartctl -H /dev/sda"},
            {"id": "B", "text": "fdisk -l /dev/sda"},
            {"id": "C", "text": "hdparm -T /dev/sda"},
            {"id": "D", "text": "blkid /dev/sda"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "smartctl -H (from smartmontools) reports the drive's SMART overall-health self-"
                       "assessment (PASSED/FAILED); 'smartctl -a' shows all attributes and error logs.",
            "distractors": {
                "A": "",
                "B": "fdisk -l lists partition tables, not drive health.",
                "C": "hdparm -T measures cached read SPEED; it does not read SMART health.",
                "D": "blkid shows UUID/filesystem type, not hardware health.",
            },
            "exam_pattern": "Disk health = SMART: 'smartctl -H' (summary) / 'smartctl -a' (full attributes), from smartmontools.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Disk health (smartctl)"],
    },
    {
        "id": "linuxplus-ts-r2-005", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "fill",
        "stem": "Which interactive tool gives a top-like, real-time view of disk I/O broken down BY "
                "PROCESS, so you can see which process is hammering the disk? (command name only)",
        "correct": ["iotop", "/usr/sbin/iotop", "/usr/bin/iotop"],
        "explanation": {
            "correct": "iotop shows per-process read/write throughput in real time (requires root), pinpointing "
                       "the specific process responsible for heavy disk I/O.",
            "distractors": {},
            "exam_pattern": "Per-process disk I/O = iotop; system/per-device I/O = iostat; high %iowait = storage bottleneck.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — I/O troubleshooting (iotop)"],
    },
    {
        "id": "linuxplus-ts-r2-006", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_storage", "difficulty": 2, "type": "mcq",
        "stem": "A partition is full and you must locate the individual files larger than 500 MB under "
                "/var so you can archive or remove them. Which command lists them?",
        "options": [
            {"id": "A", "text": "find /var -type f -size +500M"},
            {"id": "B", "text": "find /var -type f -size 500M"},
            {"id": "C", "text": "du -a /var -size +500M"},
            {"id": "D", "text": "ls -lR /var -size +500M"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "find /var -type f -size +500M matches regular files larger than 500 MiB; the leading "
                       "'+' means 'greater than'.",
            "distractors": {
                "A": "",
                "B": "'-size 500M' (no sign) matches files of EXACTLY 500M in the rounded unit, missing most large files.",
                "C": "du has no -size filter; it totals directory sizes, not individual files by threshold.",
                "D": "ls has no -size option; -size is a find predicate.",
            },
            "exam_pattern": "Big files: 'find <dir> -type f -size +<N>M'; +N greater than, -N less than, N exactly.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Storage troubleshooting (find -size)"],
    },

    # ----- linuxp_ts_network (7) -------------------------------------------
    {
        "id": "linuxplus-ts-r2-007", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 3, "type": "mcq",
        "stem": "A host can ping devices on its own subnet but cannot reach anything on other networks. "
                "Which command confirms whether a DEFAULT ROUTE (gateway) is even configured?",
        "options": [
            {"id": "A", "text": "ip route"},
            {"id": "B", "text": "ip addr"},
            {"id": "C", "text": "ss -tln"},
            {"id": "D", "text": "dig +short gateway"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ip route (or 'ip route show') prints the routing table. The absence of a 'default via "
                       "...' line explains why only the local subnet is reachable.",
            "distractors": {
                "A": "",
                "B": "ip addr shows interface addresses, confirming local IP but not the gateway/route.",
                "C": "ss -tln lists listening sockets, unrelated to routing.",
                "D": "dig queries DNS; it does not reveal the routing table or default gateway.",
            },
            "exam_pattern": "Local works, remote fails => check 'ip route' for a 'default via <gw>' entry; add with 'ip route add default via'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (ip route / default gateway)"],
    },
    {
        "id": "linuxplus-ts-r2-008", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "From a client, you must test whether TCP port 443 on 10.0.0.50 is reachable/open, "
                "without sending any data. Which command does a quick port check?",
        "options": [
            {"id": "A", "text": "nc -zv 10.0.0.50 443"},
            {"id": "B", "text": "ping -p 443 10.0.0.50"},
            {"id": "C", "text": "dig 10.0.0.50:443"},
            {"id": "D", "text": "ss -tlnp 10.0.0.50"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "nc (netcat) -z scans without sending data and -v prints the result, so 'nc -zv "
                       "10.0.0.50 443' reports whether the remote TCP port is open.",
            "distractors": {
                "A": "",
                "B": "ping uses ICMP and cannot test a specific TCP port; -p sets a pad pattern, not a port.",
                "C": "dig performs DNS lookups; it does not probe TCP ports.",
                "D": "ss shows sockets on the LOCAL machine; it cannot test a remote host's port.",
            },
            "exam_pattern": "Remote port reachability: 'nc -zv host port' (or 'nc -zvu' for UDP); confirms a service is open across the network.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (nc port test)"],
    },
    {
        "id": "linuxplus-ts-r2-009", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "You need to verify that a web server returns an HTTP 200 and inspect its response "
                "headers from the command line. Which command is best?",
        "options": [
            {"id": "A", "text": "curl -I http://localhost"},
            {"id": "B", "text": "ping http://localhost"},
            {"id": "C", "text": "ss -s http://localhost"},
            {"id": "D", "text": "dig http://localhost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "curl -I issues an HTTP HEAD request and prints just the status line and response "
                       "headers, confirming the server answers (and with what status). Use -v for the full handshake.",
            "distractors": {
                "A": "",
                "B": "ping tests ICMP reachability of a host and cannot take a URL or report HTTP status.",
                "C": "ss -s prints socket statistics; it does not make HTTP requests.",
                "D": "dig resolves DNS names; it does not retrieve HTTP responses.",
            },
            "exam_pattern": "Test a web endpoint from the CLI: 'curl -I <url>' (headers/status) or 'curl -v' (full detail); wget also works.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (curl)"],
    },
    {
        "id": "linuxplus-ts-r2-010", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 2, "type": "mcq",
        "stem": "A newly cabled server has no connectivity. 'ip link' shows eth0 in state DOWN. Which "
                "command administratively enables the interface?",
        "options": [
            {"id": "A", "text": "ip link set eth0 up"},
            {"id": "B", "text": "ifconfig eth0 promisc"},
            {"id": "C", "text": "ip route flush eth0"},
            {"id": "D", "text": "dhclient -r eth0"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ip link set eth0 up brings the interface administratively up; if it then shows "
                       "'state UP' (or at least NO-CARRIER clears), connectivity can proceed.",
            "distractors": {
                "A": "",
                "B": "ifconfig ... promisc enables promiscuous MODE (packet capture); it does not reliably bring a down link up and is legacy.",
                "C": "ip route flush removes routes; it does not change the link's admin state.",
                "D": "dhclient -r RELEASES a DHCP lease; it does not enable a downed interface.",
            },
            "exam_pattern": "Interface DOWN (admin) vs NO-CARRIER (cable): bring up with 'ip link set <if> up'; NO-CARRIER points to a physical/cable fault.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (ip link state)"],
    },
    {
        "id": "linuxplus-ts-r2-011", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 3, "type": "mcq",
        "stem": "A service is listening and the network path is fine, but remote clients are refused. You "
                "suspect the host firewall. On a RHEL/firewalld system, which command lists the currently "
                "allowed services and ports so you can confirm the port is open?",
        "options": [
            {"id": "A", "text": "firewall-cmd --list-all"},
            {"id": "B", "text": "firewall-cmd --reload"},
            {"id": "C", "text": "ufw status"},
            {"id": "D", "text": "iptables -F"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "firewall-cmd --list-all shows the active zone's services, ports, and rich rules, so "
                       "you can see whether the needed port/service is permitted.",
            "distractors": {
                "A": "",
                "B": "--reload re-applies permanent rules; it does not display the current ruleset.",
                "C": "ufw is the Ubuntu firewall front end, not used on a firewalld/RHEL host.",
                "D": "iptables -F FLUSHES all rules (dangerous) rather than listing them; use 'iptables -L -n -v' to view legacy rules.",
            },
            "exam_pattern": "Inspect the host firewall: firewalld 'firewall-cmd --list-all', ufw 'ufw status', legacy 'iptables -L -n', nftables 'nft list ruleset'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (firewall-cmd --list-all)"],
    },
    {
        "id": "linuxplus-ts-r2-012", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 3, "type": "mcq",
        "stem": "An interface is up but has no link. Which command reports the physical link status, "
                "negotiated speed, and duplex of eth0 to check for a cable or negotiation fault?",
        "options": [
            {"id": "A", "text": "ethtool eth0"},
            {"id": "B", "text": "ip addr show eth0"},
            {"id": "C", "text": "ss -i"},
            {"id": "D", "text": "nmcli radio all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ethtool eth0 shows 'Link detected: yes/no', the negotiated Speed and Duplex, and "
                       "supported modes — ideal for diagnosing a dead cable or a speed/duplex mismatch.",
            "distractors": {
                "A": "",
                "B": "ip addr shows the IP configuration and admin state but not the negotiated link speed/duplex or carrier detail.",
                "C": "ss -i prints internal TCP socket info, not NIC link status.",
                "D": "nmcli radio all reports WiFi/WWAN radio switches, not a wired link's speed/duplex.",
            },
            "exam_pattern": "Physical link/speed/duplex/cable = ethtool <iface> ('Link detected'); 'ip link' shows NO-CARRIER on a dead cable.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (ethtool)"],
    },
    {
        "id": "linuxplus-ts-r2-013", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_network", "difficulty": 3, "type": "mcq",
        "stem": "Two hosts on the same LAN cannot communicate though their IPs and subnet masks are "
                "correct. Which command displays the ARP/neighbor table so you can check for a failed "
                "layer-2 (MAC) resolution?",
        "options": [
            {"id": "A", "text": "ip neigh"},
            {"id": "B", "text": "ip route"},
            {"id": "C", "text": "ss -tn"},
            {"id": "D", "text": "traceroute -n"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ip neigh (the iproute2 ARP/neighbor table, replacing 'arp -n') shows each neighbor's "
                       "MAC and state; an INCOMPLETE/FAILED entry indicates layer-2 resolution is not happening.",
            "distractors": {
                "A": "",
                "B": "ip route shows layer-3 routing, not MAC/ARP resolution on the local segment.",
                "C": "ss -tn lists TCP connections, not the ARP table.",
                "D": "traceroute maps layer-3 hops to a remote host; on-LAN MAC resolution is not what it inspects.",
            },
            "exam_pattern": "Same-LAN failure with correct IPs => check ARP: 'ip neigh' (states REACHABLE/STALE/FAILED); legacy 'arp -n'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Network troubleshooting (ip neigh / ARP)"],
    },

    # ----- linuxp_ts_cpu_memory (6) ----------------------------------------
    {
        "id": "linuxplus-ts-r2-014", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 3, "type": "mcq",
        "stem": "'uptime' reports a 1-minute load average of 4.00. To judge whether the CPU is actually "
                "overloaded, which value must you compare that against?",
        "options": [
            {"id": "A", "text": "The number of CPU cores (e.g., from nproc)"},
            {"id": "B", "text": "The total RAM in GB"},
            {"id": "C", "text": "The amount of free swap"},
            {"id": "D", "text": "The system uptime in days"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Load average is runnable/uninterruptible processes; it must be read relative to CPU "
                       "count. A load of 4.00 is roughly fully-utilized on 4 cores but heavily overloaded on 1 core.",
            "distractors": {
                "A": "",
                "B": "RAM size is a memory metric and does not scale the meaning of a CPU run-queue load average.",
                "C": "Free swap relates to memory pressure, not to whether the load average indicates CPU saturation.",
                "D": "Uptime is just how long the system has run; it has no bearing on interpreting the load number.",
            },
            "exam_pattern": "Load average vs cores: load ≈ core count = busy; load >> cores = saturated. Get cores with nproc/lscpu.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — CPU troubleshooting (load average vs cores)"],
    },
    {
        "id": "linuxplus-ts-r2-015", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 2, "type": "mcq",
        "stem": "Which command lists running processes sorted so the TOP CPU consumers appear first, for "
                "a one-shot snapshot (non-interactive)?",
        "options": [
            {"id": "A", "text": "ps aux --sort=-%cpu"},
            {"id": "B", "text": "ps aux --sort=%cpu"},
            {"id": "C", "text": "ps -e --forest"},
            {"id": "D", "text": "free -h --sort cpu"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ps aux --sort=-%cpu sorts by CPU usage DESCENDING (the leading minus), so the "
                       "heaviest process is first; pipe to 'head' to see just the top few.",
            "distractors": {
                "A": "",
                "B": "--sort=%cpu (no minus) sorts ASCENDING, burying the top consumer at the bottom.",
                "C": "--forest shows a process tree, not a CPU-sorted list.",
                "D": "free reports memory totals and has no process sort; it does not list processes at all.",
            },
            "exam_pattern": "Top consumers non-interactively: 'ps aux --sort=-%cpu' or '--sort=-%mem' (lead '-' = descending).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — CPU troubleshooting (ps --sort)"],
    },
    {
        "id": "linuxplus-ts-r2-016", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 2, "type": "mcq",
        "stem": "While watching the interactive 'top' display, which single keypress re-sorts the process "
                "list by MEMORY usage so you can find the biggest memory consumer?",
        "options": [
            {"id": "A", "text": "M"},
            {"id": "B", "text": "P"},
            {"id": "C", "text": "k"},
            {"id": "D", "text": "q"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In top, pressing Shift+M sorts processes by resident memory (%MEM), bringing the "
                       "largest memory user to the top.",
            "distractors": {
                "A": "",
                "B": "P sorts by CPU usage (the default), not memory.",
                "C": "k prompts to KILL a process by PID; it does not sort.",
                "D": "q QUITS top.",
            },
            "exam_pattern": "top keys: M sort by memory, P sort by CPU, k kill, r renice, 1 per-CPU view, q quit.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Memory troubleshooting (top sort keys)"],
    },
    {
        "id": "linuxplus-ts-r2-017", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 2, "type": "mcq",
        "stem": "A server feels sluggish and you suspect it is swapping heavily. Which command shows how "
                "much swap is configured and currently in use, per swap area?",
        "options": [
            {"id": "A", "text": "swapon --show"},
            {"id": "B", "text": "mount -l"},
            {"id": "C", "text": "lsblk -f"},
            {"id": "D", "text": "df -h"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "swapon --show lists each swap device/file with its size and amount used; 'free -h' "
                       "also summarizes total swap used, and sustained si/so in vmstat confirms active swapping.",
            "distractors": {
                "A": "",
                "B": "mount -l lists mounted filesystems; swap areas are not shown as mounts.",
                "C": "lsblk -f shows block devices/filesystems but not live swap usage figures.",
                "D": "df -h reports disk space on filesystems, not swap utilization.",
            },
            "exam_pattern": "Swap usage: 'swapon --show' / 'free -h'; heavy si/so in 'vmstat' confirms the system is thrashing.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Memory troubleshooting (swapon --show)"],
    },
    {
        "id": "linuxplus-ts-r2-018", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 3, "type": "fill",
        "stem": "Which sysstat command displays HISTORICAL system-activity data (e.g., past CPU "
                "utilization collected throughout the day) rather than just a live snapshot? (command "
                "name only)",
        "correct": ["sar", "/usr/bin/sar"],
        "explanation": {
            "correct": "sar (System Activity Reporter, from sysstat) reads the archived activity files in "
                       "/var/log/sa/ to show past CPU, memory, I/O, and network statistics — useful for post-incident analysis.",
            "distractors": {},
            "exam_pattern": "Historical metrics = sar (sysstat; -u CPU, -r memory, -b I/O, -n network); live sampling = vmstat/iostat.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Performance history (sar)"],
    },
    {
        "id": "linuxplus-ts-r2-019", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_cpu_memory", "difficulty": 3, "type": "mcq",
        "stem": "A service fails intermittently with 'Too many open files'. Which command shows (and can "
                "raise, for the current shell) the per-process limit on open file descriptors?",
        "options": [
            {"id": "A", "text": "ulimit -n"},
            {"id": "B", "text": "free -m"},
            {"id": "C", "text": "sysctl vm.swappiness"},
            {"id": "D", "text": "nproc --all"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ulimit -n shows the soft limit on open file descriptors and can raise it for the "
                       "current shell/children; persistent limits are set in /etc/security/limits.conf or a systemd unit's LimitNOFILE.",
            "distractors": {
                "A": "",
                "B": "free -m reports memory, not file-descriptor limits.",
                "C": "vm.swappiness tunes swap tendency; it is unrelated to open-file limits.",
                "D": "nproc --all prints CPU count, not resource limits.",
            },
            "exam_pattern": "'Too many open files' => raise the fd limit: 'ulimit -n' (session), limits.conf or LimitNOFILE= (persistent).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Resource limits (ulimit -n)"],
    },

    # ----- linuxp_ts_users_access (5) --------------------------------------
    {
        "id": "linuxplus-ts-r2-020", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 2, "type": "mcq",
        "stem": "A user's credentials are correct but every interactive login is immediately closed. Their "
                "/etc/passwd entry ends in /sbin/nologin. What does this indicate?",
        "options": [
            {"id": "A", "text": "The account's login shell is /sbin/nologin, which refuses interactive logins by design"},
            {"id": "B", "text": "The password in /etc/shadow has expired"},
            {"id": "C", "text": "The account's UID is 0"},
            {"id": "D", "text": "The user is missing from /etc/group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A shell of /sbin/nologin (or /bin/false) is set on service accounts to prevent "
                       "interactive logins; change it with 'usermod -s /bin/bash <user>' if a real shell is intended.",
            "distractors": {
                "A": "",
                "B": "An expired password produces a change-password prompt, not an immediate logout tied to the shell field.",
                "C": "UID 0 would make the account root-equivalent, not block its login.",
                "D": "A missing group entry can cause other errors but is not what /sbin/nologin as the shell signifies.",
            },
            "exam_pattern": "Login opens then closes + shell is /sbin/nologin or /bin/false => intentional no-login account; fix with usermod -s.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Access troubleshooting (login shell /sbin/nologin)"],
    },
    {
        "id": "linuxplus-ts-r2-021", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 2, "type": "mcq",
        "stem": "A user suddenly cannot log in at all. You suspect the ACCOUNT itself has expired. Which "
                "command shows the account expiration date and password-aging details for user 'carol'?",
        "options": [
            {"id": "A", "text": "chage -l carol"},
            {"id": "B", "text": "passwd carol"},
            {"id": "C", "text": "id carol"},
            {"id": "D", "text": "finger carol"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "chage -l carol lists the account- and password-aging fields, including 'Account "
                       "expires'; a date in the past means the account is expired and logins are refused.",
            "distractors": {
                "A": "",
                "B": "passwd carol starts changing the password; it does not report the expiration date.",
                "C": "id carol shows UID/GID/groups, not aging or expiration.",
                "D": "finger (often not installed) shows limited user info and not the shadow aging fields.",
            },
            "exam_pattern": "Account/password aging: 'chage -l <user>'; set expiry with 'chage -E YYYY-MM-DD' or 'usermod -e'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Account troubleshooting (chage -l)"],
    },
    {
        "id": "linuxplus-ts-r2-022", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 2, "type": "mcq",
        "stem": "A new admin runs a command with sudo and gets 'user is not in the sudoers file. This "
                "incident will be reported.' What is the correct fix on a RHEL system?",
        "options": [
            {"id": "A", "text": "Add the user to the 'wheel' group (e.g., usermod -aG wheel <user>), which sudoers grants by default"},
            {"id": "B", "text": "Run 'chmod u+s /usr/bin/sudo'"},
            {"id": "C", "text": "Set the user's UID to 0"},
            {"id": "D", "text": "Add the user to the 'users' group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On RHEL the default sudoers rule grants the 'wheel' group sudo, so adding the user to "
                       "wheel (on Debian/Ubuntu it's the 'sudo' group) fixes the error. Edit custom rules with visudo.",
            "distractors": {
                "A": "",
                "B": "Setting SUID on the sudo binary is already the case and is not the problem; it would not grant this user authorization.",
                "C": "Making the UID 0 turns the account into another root, a dangerous misconfiguration, not the sudo fix.",
                "D": "The generic 'users' group has no sudo rights by default; wheel (RHEL) / sudo (Debian) is the privileged group.",
            },
            "exam_pattern": "'not in the sudoers file' => add to wheel (RHEL) or sudo (Debian/Ubuntu) group, or add a rule via visudo.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Access troubleshooting (sudoers/wheel)"],
    },
    {
        "id": "linuxplus-ts-r2-023", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 3, "type": "mcq",
        "stem": "You add user 'dev' to the 'docker' group with 'usermod -aG docker dev', but in dev's "
                "CURRENT shell 'id' still doesn't show docker and permission is denied. Why?",
        "options": [
            {"id": "A", "text": "Group membership changes apply to NEW login sessions; dev must log out and back in (or run 'newgrp docker')"},
            {"id": "B", "text": "usermod -aG does not actually modify group membership"},
            {"id": "C", "text": "The docker group must have a password set first"},
            {"id": "D", "text": "The change requires a full system reboot to take effect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A process's group credentials are fixed at login, so an existing shell doesn't see "
                       "the new group until a fresh login; 'newgrp docker' starts a subshell with the group applied immediately.",
            "distractors": {
                "A": "",
                "B": "usermod -aG DID update /etc/group; the issue is that the running session hasn't picked it up yet.",
                "C": "Group passwords are unrelated; membership does not require one.",
                "D": "A full reboot is unnecessary; a new login or 'newgrp' is enough.",
            },
            "exam_pattern": "New group not effective in current shell => re-login or 'newgrp <group>'; credentials are set at login time.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Access troubleshooting (group not effective)"],
    },
    {
        "id": "linuxplus-ts-r2-024", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_users_access", "difficulty": 3, "type": "mcq",
        "stem": "On a RHEL 9 host using pam_faillock, user 'ops' is locked out after several failed SSH "
                "attempts even though the password is now correct. Which command clears the failures and "
                "unlocks the account?",
        "options": [
            {"id": "A", "text": "faillock --user ops --reset"},
            {"id": "B", "text": "passwd -u ops"},
            {"id": "C", "text": "usermod -U ops"},
            {"id": "D", "text": "pam_tally2 --user ops"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "faillock --user ops --reset clears the recorded failed attempts so pam_faillock stops "
                       "blocking the account. Running 'faillock --user ops' (no --reset) shows the current count.",
            "distractors": {
                "A": "",
                "B": "passwd -u unlocks a password LOCKED with passwd -l (the '!' in shadow); it does not clear faillock tallies.",
                "C": "usermod -U unlocks a usermod/passwd password lock, not the pam_faillock failure counter.",
                "D": "pam_tally2 is the OLDER module (and merely querying it doesn't reset); modern RHEL uses faillock.",
            },
            "exam_pattern": "pam_faillock lockout => 'faillock --user <u> --reset'; distinct from passwd/usermod lock (-l/-U) and legacy pam_tally2.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Account lockout (faillock --reset)"],
    },

    # ----- linuxp_ts_services (5) ------------------------------------------
    {
        "id": "linuxplus-ts-r2-025", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 3, "type": "mcq",
        "stem": "A service fails to start and its journal shows 'bind: Address already in use' for port "
                "8080. Which command identifies the process currently holding that port?",
        "options": [
            {"id": "A", "text": "ss -tlnp | grep :8080"},
            {"id": "B", "text": "systemctl restart network"},
            {"id": "C", "text": "ping -p 8080 localhost"},
            {"id": "D", "text": "journalctl --vacuum-time=1d"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "ss -tlnp lists listening TCP sockets with the owning process; filtering for :8080 "
                       "reveals the PID/program already bound there, which you then stop or reconfigure.",
            "distractors": {
                "A": "",
                "B": "Restarting networking does not free an application-held port and disrupts connectivity.",
                "C": "ping cannot test or reveal a process holding a TCP port.",
                "D": "journalctl --vacuum-time trims old logs; it has nothing to do with port conflicts.",
            },
            "exam_pattern": "'Address already in use' => find the holder with 'ss -tlnp' (or 'lsof -i :<port>'), then stop/reassign it.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (port conflict / ss)"],
    },
    {
        "id": "linuxplus-ts-r2-026", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 3, "type": "multi",
        "stem": "You edited /etc/systemd/system/myapp.service, but 'systemctl restart myapp' still runs "
                "the old settings (systemd even warns the unit file changed on disk). Which TWO steps "
                "apply the edited unit correctly? (Choose two.)",
        "options": [
            {"id": "A", "text": "systemctl daemon-reload"},
            {"id": "B", "text": "systemctl restart myapp"},
            {"id": "C", "text": "systemctl mask myapp"},
            {"id": "D", "text": "systemctl enable myapp"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "systemd caches unit files, so you must 'systemctl daemon-reload' to re-read the "
                       "changed .service file, then 'systemctl restart myapp' to run with the new definition.",
            "distractors": {
                "C": "mask links the unit to /dev/null, making it impossible to start — the opposite of what you want.",
                "D": "enable only controls whether it starts at BOOT; it neither reloads the file nor restarts the running service.",
            },
            "exam_pattern": "Changed a unit file => 'systemctl daemon-reload' THEN restart; enable/disable only affect boot autostart.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (daemon-reload)"],
    },
    {
        "id": "linuxplus-ts-r2-027", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 2, "type": "mcq",
        "stem": "A unit just failed and you want the most recent journal entries at the END of the log, "
                "annotated with explanatory help text, to triage it quickly. Which command is designed "
                "for this?",
        "options": [
            {"id": "A", "text": "journalctl -xe"},
            {"id": "B", "text": "journalctl --since boot"},
            {"id": "C", "text": "journalctl -r -k"},
            {"id": "D", "text": "journalctl --disk-usage"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "journalctl -xe combines -e (jump to the end / most recent) with -x (add catalog "
                       "explanation text), the standard quick-triage view after a service fails.",
            "distractors": {
                "A": "",
                "B": "'--since boot' is not valid syntax (use -b or --since with a time); it also doesn't add explanations.",
                "C": "-r reverses order and -k limits to KERNEL messages, missing the service's own entries.",
                "D": "--disk-usage reports how much space the journal consumes, not log content.",
            },
            "exam_pattern": "Fast failure triage: 'journalctl -xe' (-e end, -x explanations); scope with -u <unit> and -b.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (journalctl -xe)"],
    },
    {
        "id": "linuxplus-ts-r2-028", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 2, "type": "mcq",
        "stem": "Before reloading nginx after editing its config, you want to VALIDATE the configuration "
                "syntax so a typo doesn't take the service down. Which command tests it?",
        "options": [
            {"id": "A", "text": "nginx -t"},
            {"id": "B", "text": "systemctl reload nginx"},
            {"id": "C", "text": "nginx -s reload"},
            {"id": "D", "text": "curl localhost"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "nginx -t parses the configuration and reports syntax errors (and the files checked) "
                       "WITHOUT applying it, so you catch mistakes before reloading. (Apache: 'httpd -t' / 'apachectl configtest'.)",
            "distractors": {
                "A": "",
                "B": "systemctl reload APPLIES the config immediately; a bad file could break the running service.",
                "C": "'nginx -s reload' also applies the new config right away rather than testing it first.",
                "D": "curl tests whether the server responds; it does not validate the config file syntax.",
            },
            "exam_pattern": "Validate before reload: 'nginx -t', 'httpd -t'/'apachectl configtest', 'sshd -t', 'visudo -c'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (config test)"],
    },
    {
        "id": "linuxplus-ts-r2-029", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_services", "difficulty": 3, "type": "mcq",
        "stem": "'systemctl start chronyd' fails with 'Unit chronyd.service is masked.' Which command "
                "must you run BEFORE it can be started again?",
        "options": [
            {"id": "A", "text": "systemctl unmask chronyd"},
            {"id": "B", "text": "systemctl enable chronyd"},
            {"id": "C", "text": "systemctl daemon-reload"},
            {"id": "D", "text": "systemctl reset-failed chronyd"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A masked unit is symlinked to /dev/null and cannot start. 'systemctl unmask chronyd' "
                       "removes that link so the service can be started (and then enabled) normally.",
            "distractors": {
                "A": "",
                "B": "enable sets boot autostart but cannot start or unmask a masked unit.",
                "C": "daemon-reload re-reads unit files; it does not clear a mask.",
                "D": "reset-failed clears a unit's FAILED state counter; it does not remove a mask.",
            },
            "exam_pattern": "'Unit is masked' => 'systemctl unmask <unit>' first; mask (-> /dev/null) is the strongest 'never start' state.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Service troubleshooting (unmask)"],
    },

    # ----- linuxp_ts_tools (5) ---------------------------------------------
    {
        "id": "linuxplus-ts-r2-030", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 3, "type": "mcq",
        "stem": "You need to review only ERROR-priority (and more severe) journal messages generated "
                "since 09:00 today. Which command filters the journal that way?",
        "options": [
            {"id": "A", "text": "journalctl -p err --since 09:00"},
            {"id": "B", "text": "journalctl -u err --since 09:00"},
            {"id": "C", "text": "journalctl --grep=err"},
            {"id": "D", "text": "journalctl -b err"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "-p err limits output to priority err (3) and higher severity (crit/alert/emerg), and "
                       "'--since 09:00' bounds the time window, isolating today's serious messages.",
            "distractors": {
                "A": "",
                "B": "-u expects a UNIT name (e.g., sshd.service), not a priority like 'err'.",
                "C": "--grep matches message TEXT containing 'err'; it does not select by syslog priority level.",
                "D": "-b selects a BOOT (e.g., -b 0); 'err' is not a valid boot identifier.",
            },
            "exam_pattern": "journalctl filters: -p <priority> (err/warning/...), --since/--until (time), -u (unit), -b (boot).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Log analysis (journalctl -p/--since)"],
    },
    {
        "id": "linuxplus-ts-r2-031", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "You want to know which process is using network port 80 on the local machine, including "
                "the program name and PID. Which lsof invocation shows this?",
        "options": [
            {"id": "A", "text": "lsof -i :80"},
            {"id": "B", "text": "lsof +D /80"},
            {"id": "C", "text": "lsof -u 80"},
            {"id": "D", "text": "lsof -p 80"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "lsof -i :80 lists the open INTERNET sockets on port 80 along with the owning command "
                       "and PID; it is the quick way to map a port to a process.",
            "distractors": {
                "A": "",
                "B": "+D searches open files under a DIRECTORY path; '/80' is not a port filter.",
                "C": "-u filters by USER name/UID, so '80' would be treated as a user, not a port.",
                "D": "-p filters by PID; here 80 is a port, not a process ID.",
            },
            "exam_pattern": "Port -> process: 'lsof -i :<port>' (or 'ss -tlnp'); 'lsof -p <pid>' lists a process's open files.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Diagnostic tools (lsof -i)"],
    },
    {
        "id": "linuxplus-ts-r2-032", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "To investigate a possible breach, you need a history of successful logins and reboots "
                "(from /var/log/wtmp). Which command displays it?",
        "options": [
            {"id": "A", "text": "last"},
            {"id": "B", "text": "lastb"},
            {"id": "C", "text": "who"},
            {"id": "D", "text": "w"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "last reads /var/log/wtmp and prints the history of user logins/logouts and system "
                       "reboots. (lastb reads /var/log/btmp for FAILED logins; who/w show only CURRENT sessions.)",
            "distractors": {
                "A": "",
                "B": "lastb shows FAILED login attempts (btmp), not the successful-login history requested.",
                "C": "who lists users currently logged in right now, not historical logins.",
                "D": "w shows who is on NOW and what they are doing, not a login history.",
            },
            "exam_pattern": "Login history: 'last' (wtmp, success/reboots) vs 'lastb' (btmp, failures); 'who'/'w' = current sessions.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Log analysis (last/wtmp)"],
    },
    {
        "id": "linuxplus-ts-r2-033", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "On a RHEL system you must review authentication events (sudo usage, SSH logins) in the "
                "traditional text logs. Which file holds them?",
        "options": [
            {"id": "A", "text": "/var/log/secure"},
            {"id": "B", "text": "/var/log/auth.log"},
            {"id": "C", "text": "/var/log/messages"},
            {"id": "D", "text": "/var/log/boot.log"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "On RHEL/Fedora, authentication and authorization events (sshd, sudo, PAM) are logged "
                       "to /var/log/secure. On Debian/Ubuntu the equivalent is /var/log/auth.log.",
            "distractors": {
                "A": "",
                "B": "/var/log/auth.log is the DEBIAN/Ubuntu auth log; it is not present by default on RHEL.",
                "C": "/var/log/messages holds general system messages on RHEL, not the dedicated auth stream.",
                "D": "/var/log/boot.log records boot-time service output, not authentication events.",
            },
            "exam_pattern": "Auth logs: RHEL /var/log/secure vs Debian /var/log/auth.log; general: messages (RHEL) vs syslog (Debian).",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Log analysis (/var/log/secure)"],
    },
    {
        "id": "linuxplus-ts-r2-034", "exam": "linuxplus", "domain": "linuxp_troubleshooting",
        "subtopic": "linuxp_ts_tools", "difficulty": 2, "type": "mcq",
        "stem": "You just plugged in a USB drive that didn't appear. Which command shows the kernel's "
                "most recent hardware/driver messages WITH human-readable timestamps to see how the "
                "device was detected?",
        "options": [
            {"id": "A", "text": "dmesg -T"},
            {"id": "B", "text": "lsof -T"},
            {"id": "C", "text": "journalctl --disk-usage"},
            {"id": "D", "text": "uptime -p"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "dmesg prints the kernel ring buffer (device detection, driver binding, I/O errors); "
                       "-T converts the timestamps to human-readable clock times so you can correlate the plug-in event.",
            "distractors": {
                "A": "",
                "B": "lsof lists open files; it has no -T hardware-log mode (and -T there toggles TCP info).",
                "C": "journalctl --disk-usage shows journal size, not kernel hardware messages.",
                "D": "uptime -p prints how long the system has been up, not device-detection logs.",
            },
            "exam_pattern": "Hardware/driver events = kernel ring buffer: 'dmesg -T' (human time) or 'journalctl -k'; watch live with 'dmesg -w'.",
        },
        "references": ["CompTIA Linux+ XK0-006 Objectives: Domain 4 — Diagnostic tools (dmesg -T)"],
    },
]
