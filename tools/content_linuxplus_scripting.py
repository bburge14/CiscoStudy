"""CompTIA Linux+ (XK0-005) pool - Domain 3: Scripting, Containers, and Automation.

Original, objective-aligned practice items for the four subtopics tracked in
CertLab:
  * linuxp_bash_scripting - shebang, variables and special parameters ($?, $#,
                            $$), test/[ ] conditions, if/for/while/case, exit
                            codes, redirection/pipes, globbing, parameter expansion.
  * linuxp_git_version    - core Git workflow: clone/add/commit/push/pull/branch/
                            merge/status/log.
  * linuxp_containers     - Docker and Podman basics (run/ps/images/build),
                            Dockerfile instructions, and persistent volumes.
  * linuxp_automation     - Ansible playbook/inventory concepts and idempotency,
                            plus cron scheduling.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the authored key is not positionally biased,
every wrong option carries a distractor note, and each item cites the public
XK0-005 objective domain it draws on. Syntax (Bash, Git, Docker/Podman, Ansible,
cron) is real and version-resilient across mainstream distributions; no
memorized or real exam items are used.
"""

QUESTIONS = [
    # ===== linuxp_bash_scripting ============================================
    {
        "id": "linuxplus-scr-001", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 1, "type": "mcq",
        "stem": "What is the correct first line (the shebang) of a shell script to ensure it is "
                "executed by the Bash interpreter?",
        "options": [
            {"id": "A", "text": "#/bin/bash"},
            {"id": "B", "text": "#!/bin/bash"},
            {"id": "C", "text": "!#/bin/bash"},
            {"id": "D", "text": "# !/bin/bash"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The shebang is the two characters '#!' immediately followed by the interpreter "
                       "path: #!/bin/bash on the very first line.",
            "distractors": {
                "A": "#/bin/bash is just a comment; without the '!' the kernel ignores it as an interpreter directive.",
                "C": "!#/bin/bash reverses the characters and is not a valid shebang.",
                "D": "A space after '#' makes '# !/bin/bash' an ordinary comment, not a shebang.",
            },
            "exam_pattern": "Shebang = '#!' + interpreter path on line 1 (e.g., #!/bin/bash, #!/usr/bin/env python3).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Shell scripting (shebang)"],
    },
    {
        "id": "linuxplus-scr-002", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "mcq",
        "stem": "In a Bash script, which special parameter holds the exit status of the most recently "
                "executed command (0 on success, non-zero on failure)?",
        "options": [
            {"id": "A", "text": "$!"},
            {"id": "B", "text": "$#"},
            {"id": "C", "text": "$?"},
            {"id": "D", "text": "$$"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "$? expands to the exit status of the last command, the standard way to test "
                       "whether a command succeeded.",
            "distractors": {
                "A": "$! is the PID of the most recent background (asynchronous) command.",
                "B": "$# is the number of positional parameters passed to the script or function.",
                "D": "$$ is the process ID of the current shell.",
            },
            "exam_pattern": "$?=last exit code, $#=arg count, $$=shell PID, $!=last background PID, $0=script name.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Exit codes ($?)"],
    },
    {
        "id": "linuxplus-scr-003", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 3, "type": "mcq",
        "stem": "Which test expression correctly checks whether the value in variable COUNT is "
                "numerically greater than 10 inside a Bash 'if' statement?",
        "options": [
            {"id": "A", "text": "[ \"$COUNT\" -gt 10 ]"},
            {"id": "B", "text": "[ \"$COUNT\" > 10 ]"},
            {"id": "C", "text": "[ \"$COUNT\" -lt 10 ]"},
            {"id": "D", "text": "( \"$COUNT\" -gt 10 )"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "-gt is the NUMERIC greater-than operator for the test/[ ] builtin: "
                       "[ \"$COUNT\" -gt 10 ].",
            "distractors": {
                "B": "Inside single-bracket [ ], '>' is treated as output redirection (or a string compare), not numeric greater-than.",
                "C": "-lt is numeric LESS-than, the opposite comparison.",
                "D": "( ... ) starts a subshell; it is not a valid test condition.",
            },
            "exam_pattern": "Numeric tests: -eq -ne -lt -le -gt -ge. String tests: = != < > (the latter need [[ ]]).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Conditionals (test operators)"],
    },
    {
        "id": "linuxplus-scr-004", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 3, "type": "mcq",
        "stem": "Which Bash construct iterates once over every file ending in .log in the current "
                "directory, assigning each name to the variable f?",
        "options": [
            {"id": "A", "text": "for f in $(ls *.log); do echo \"$f\"; done"},
            {"id": "B", "text": "for f in *.log; do echo \"$f\"; done"},
            {"id": "C", "text": "foreach f (*.log); echo $f; end"},
            {"id": "D", "text": "while *.log; do echo \"$f\"; done"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "for f in *.log lets the shell glob-expand the pattern to the matching filenames, "
                       "handling names safely without parsing ls output.",
            "distractors": {
                "A": "Looping over $(ls *.log) parses command output and breaks on filenames with spaces or special characters.",
                "C": "foreach ... end is C-shell (csh/tcsh) syntax, not Bash.",
                "D": "while expects a condition/command, and '*.log' alone is not a loop condition.",
            },
            "exam_pattern": "Iterate files with a glob (for f in *.ext), never by parsing 'ls'.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Loops and globbing (for)"],
    },
    {
        "id": "linuxplus-scr-005", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_bash_scripting", "difficulty": 2, "type": "fill",
        "stem": "Which Bash keyword begins a multi-branch construct that matches a value against several "
                "patterns (a cleaner alternative to a long if/elif chain), and is closed with 'esac'? "
                "(keyword only)",
        "correct": ["case"],
        "explanation": {
            "correct": "The case statement matches a value against patterns ( case \"$x\" in pattern) ... "
                       ";; esac ), ideal when one variable has many possible values.",
            "distractors": {},
            "exam_pattern": "case ... in ... ) ... ;; esac — note it is terminated by 'esac' (case reversed).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Control flow (case)"],
    },

    # ===== linuxp_git_version ===============================================
    {
        "id": "linuxplus-scr-006", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 1, "type": "mcq",
        "stem": "Which Git command creates a complete local copy of a remote repository, including its "
                "full commit history and a working tree?",
        "options": [
            {"id": "A", "text": "git init https://example.com/app.git"},
            {"id": "B", "text": "git pull https://example.com/app.git"},
            {"id": "C", "text": "git clone https://example.com/app.git"},
            {"id": "D", "text": "git checkout https://example.com/app.git"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "git clone <url> downloads the entire repository (history and branches) and checks "
                       "out a working copy, setting the remote 'origin' automatically.",
            "distractors": {
                "A": "git init creates a brand-new empty repository locally; it does not take a URL to copy from.",
                "B": "git pull fetches and merges into an EXISTING repository; it is not how you first obtain one.",
                "D": "git checkout switches branches or restores files within a repo; it does not clone remotes.",
            },
            "exam_pattern": "clone = first copy of a remote; init = new empty repo; pull = update an existing repo.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Version control (git clone)"],
    },
    {
        "id": "linuxplus-scr-007", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 2, "type": "mcq",
        "stem": "You have modified and created several files in a Git working tree. Which command "
                "sequence stages ALL of those changes and records them as a commit with a message?",
        "options": [
            {"id": "A", "text": "git add -A && git commit -m \"update\""},
            {"id": "B", "text": "git commit -m \"update\""},
            {"id": "C", "text": "git push -m \"update\""},
            {"id": "D", "text": "git stash && git commit -m \"update\""},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "git add -A stages all modifications, additions, and deletions; git commit -m then "
                       "records them with the given message.",
            "distractors": {
                "B": "git commit alone commits only ALREADY-staged changes; newly created/unstaged files would be left out.",
                "C": "git push uploads existing commits to a remote and has no -m option to create a commit.",
                "D": "git stash shelves the changes away, leaving nothing staged for the following commit.",
            },
            "exam_pattern": "Typical flow: git add (stage) -> git commit -m (record) -> git push (publish).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Version control (git add/commit)"],
    },
    {
        "id": "linuxplus-scr-008", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 2, "type": "mcq",
        "stem": "While on the main branch, which command integrates the commits from a branch named "
                "'feature' into your current branch?",
        "options": [
            {"id": "A", "text": "git branch feature"},
            {"id": "B", "text": "git merge feature"},
            {"id": "C", "text": "git checkout feature"},
            {"id": "D", "text": "git clone feature"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "git merge feature joins the feature branch's history into the branch you currently "
                       "have checked out, creating a merge (or fast-forward) commit.",
            "distractors": {
                "A": "git branch feature only CREATES (or lists) the branch; it does not combine histories.",
                "C": "git checkout feature SWITCHES your working tree to that branch instead of merging it in.",
                "D": "git clone copies a whole remote repository; it is not used to combine local branches.",
            },
            "exam_pattern": "Checkout the target branch, then 'git merge <source>' to bring the source's work in.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Branching (git merge)"],
    },
    {
        "id": "linuxplus-scr-009", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_git_version", "difficulty": 1, "type": "fill",
        "stem": "Which Git subcommand shows the state of the working tree — which files are staged, "
                "modified but unstaged, or untracked? (subcommand word only)",
        "correct": ["status", "git status"],
        "explanation": {
            "correct": "git status summarizes the current branch, staged changes, unstaged modifications, "
                       "and untracked files — the go-to command before committing.",
            "distractors": {},
            "exam_pattern": "git status (current state) vs git log (commit history) vs git diff (line-level changes).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Version control (git status)"],
    },

    # ===== linuxp_containers ================================================
    {
        "id": "linuxplus-scr-010", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "mcq",
        "stem": "Which command starts a new container from the nginx image in the background (detached) "
                "and maps host port 8080 to container port 80?",
        "options": [
            {"id": "A", "text": "docker run -d -p 80:8080 nginx"},
            {"id": "B", "text": "docker run -d -p 8080:80 nginx"},
            {"id": "C", "text": "docker build -t nginx ."},
            {"id": "D", "text": "docker exec -d -p 8080:80 nginx"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "docker run -d runs detached; -p 8080:80 maps HOST:CONTAINER, so host 8080 forwards "
                       "to the container's port 80. (podman run uses the same syntax.)",
            "distractors": {
                "A": "-p 80:8080 reverses the mapping (host 80 to container 8080), which is not what nginx listens on.",
                "C": "docker build creates an IMAGE from a Dockerfile; it does not start a container.",
                "D": "docker exec runs a command in an ALREADY-RUNNING container and does not publish ports.",
            },
            "exam_pattern": "-p HOST:CONTAINER (host port first); -d detaches; run starts a new container.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Containers (docker/podman run)"],
    },
    {
        "id": "linuxplus-scr-011", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 1, "type": "mcq",
        "stem": "Which command lists the containers that are currently running (and only those)?",
        "options": [
            {"id": "A", "text": "docker images"},
            {"id": "B", "text": "docker ps"},
            {"id": "C", "text": "docker ls"},
            {"id": "D", "text": "docker start"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "docker ps (equivalently 'docker container ls', or 'podman ps') lists running "
                       "containers; add -a to include stopped ones.",
            "distractors": {
                "A": "docker images lists downloaded IMAGES, not running containers.",
                "C": "docker ls is not a valid command (the long form is 'docker container ls').",
                "D": "docker start launches a stopped container by name/ID; it does not list anything.",
            },
            "exam_pattern": "ps = running containers (-a for all); images = image list.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Containers (docker ps)"],
    },
    {
        "id": "linuxplus-scr-012", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "mcq",
        "stem": "In a Dockerfile, which instruction specifies the base image the new image is built "
                "from and normally appears as the first instruction?",
        "options": [
            {"id": "A", "text": "RUN"},
            {"id": "B", "text": "FROM"},
            {"id": "C", "text": "CMD"},
            {"id": "D", "text": "COPY"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "FROM <image> sets the base image and must be the first instruction (after any "
                       "optional ARG) in a Dockerfile.",
            "distractors": {
                "A": "RUN executes a command during the build, creating a new image layer.",
                "C": "CMD sets the default command/arguments run when a container starts, not the base image.",
                "D": "COPY copies files from the build context into the image; it does not define the base.",
            },
            "exam_pattern": "Dockerfile essentials: FROM (base) -> RUN (build steps) -> COPY/ADD -> CMD/ENTRYPOINT (default process).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Containers (Dockerfile FROM)"],
    },
    {
        "id": "linuxplus-scr-013", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_containers", "difficulty": 2, "type": "fill",
        "stem": "Which 'docker run' / 'podman run' flag (give the short single-letter form) mounts a "
                "host directory or named volume into a container so its data persists beyond the "
                "container's life?",
        "correct": ["-v", "--volume"],
        "explanation": {
            "correct": "-v (long form --volume) bind-mounts a host path or attaches a named volume, e.g. "
                       "'-v /data:/app/data' or '-v mydata:/app/data', keeping data after the container is removed.",
            "distractors": {},
            "exam_pattern": "Persistence: -v/--volume (or --mount). Without it, a container's writable layer is lost on removal.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Containers (volumes)"],
    },

    # ===== linuxp_automation ================================================
    {
        "id": "linuxplus-scr-014", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "mcq",
        "stem": "An Ansible playbook is run twice against the same hosts. The second run reports no "
                "changes because the systems already match the desired state. Which property does this "
                "demonstrate?",
        "options": [
            {"id": "A", "text": "Idempotency"},
            {"id": "B", "text": "Inventory"},
            {"id": "C", "text": "Privilege escalation"},
            {"id": "D", "text": "A rolling update"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Idempotency means applying the same configuration repeatedly yields the same end "
                       "state and makes changes only when something differs — a core Ansible design goal.",
            "distractors": {
                "B": "The inventory is the list of managed hosts/groups, not the no-change behavior.",
                "C": "Privilege escalation (become) is about running tasks as another user like root.",
                "D": "A rolling update is a deployment strategy that updates hosts in batches, a different concept.",
            },
            "exam_pattern": "Repeatable automation converges to desired state and only changes what is needed = idempotent.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Automation (idempotency)"],
    },
    {
        "id": "linuxplus-scr-015", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "mcq",
        "stem": "In Ansible, which component defines the set of managed hosts and groups that a playbook "
                "runs against?",
        "options": [
            {"id": "A", "text": "The playbook"},
            {"id": "B", "text": "The inventory"},
            {"id": "C", "text": "A handler"},
            {"id": "D", "text": "A module"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The inventory (a static file such as /etc/ansible/hosts, an INI/YAML file, or a "
                       "dynamic source) lists the hosts and groups targeted by plays.",
            "distractors": {
                "A": "A playbook defines the tasks/plays to run; it references hosts but does not itself define the host list.",
                "C": "A handler is a task triggered by 'notify', typically to restart a service after a change.",
                "D": "A module is a reusable unit of work (e.g., 'yum', 'copy') executed on the hosts.",
            },
            "exam_pattern": "Ansible pieces: inventory (hosts) + playbook (plays/tasks) + modules (actions) + handlers (notified tasks).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Automation (Ansible inventory)"],
    },
    {
        "id": "linuxplus-scr-016", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "mcq",
        "stem": "In a standard crontab entry, the five time-and-date fields appear in order as minute, "
                "hour, day-of-month, month, and which fifth field?",
        "options": [
            {"id": "A", "text": "Day of week"},
            {"id": "B", "text": "Second"},
            {"id": "C", "text": "Year"},
            {"id": "D", "text": "Day of year"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The five cron fields are minute, hour, day of month, month, and day of week "
                       "(0-7, where 0 and 7 both mean Sunday).",
            "distractors": {
                "B": "Standard cron has no seconds field; its finest granularity is one minute.",
                "C": "There is no year field in a standard crontab.",
                "D": "Cron uses day of week and day of month, not a day-of-year field.",
            },
            "exam_pattern": "cron order: min hour dom month dow <command>. '*' = every value.",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Scheduling (cron fields)"],
    },
    {
        "id": "linuxplus-scr-017", "exam": "linuxplus", "domain": "linuxp_scripting",
        "subtopic": "linuxp_automation", "difficulty": 2, "type": "fill",
        "stem": "Which command opens the current user's personal crontab in an editor so scheduled jobs "
                "can be added or changed (rather than editing a system file directly)? (command and flag)",
        "correct": ["crontab -e"],
        "explanation": {
            "correct": "crontab -e opens the invoking user's crontab in the default editor and installs it "
                       "safely on save. Use 'crontab -l' to list and 'crontab -r' to remove it.",
            "distractors": {},
            "exam_pattern": "crontab -e edit, -l list, -r remove; '-u user' targets another user's crontab (as root).",
        },
        "references": ["CompTIA Linux+ XK0-005 Objectives: Domain 3 — Scheduling (crontab)"],
    },
]
