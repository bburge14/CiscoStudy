# Scheduling, IaC & CI/CD Automation

The point of automation is to make the machine do repetitive work on a schedule,
and to describe whole systems as code so they can be rebuilt identically. This
lesson covers time-based scheduling with **cron** and **systemd timers**, then the
higher-level worlds of **Infrastructure as Code** (with Ansible) and **CI/CD**
pipelines.

## cron: time-based jobs

**cron** runs commands on a recurring schedule. Each user edits their own
**crontab**:

```
$ crontab -e      # edit your crontab
$ crontab -l      # list it
$ crontab -r      # remove it
```

A crontab line has **five time fields** followed by the command:

```
┌ minute (0–59)
│ ┌ hour (0–23)
│ │ ┌ day of month (1–31)
│ │ │ ┌ month (1–12)
│ │ │ │ ┌ day of week (0–7, 0 and 7 = Sunday)
│ │ │ │ │
30 2 * * 1   /usr/local/bin/backup.sh
```

That example runs at **02:30 every Monday**. A `*` means "every"; you can use
lists (`1,15`), ranges (`1-5`) and steps (`*/10` = every 10). Shortcuts like
`@daily` and `@reboot` also work.

System-wide cron adds files: **`/etc/crontab`** and **`/etc/cron.d/`** have an
**extra field — the user** to run as — and the drop-in directories
`/etc/cron.hourly`, `cron.daily`, `cron.weekly` and `cron.monthly` run scripts
placed in them. For a **one-time** future job (not recurring), use **`at`**:
`echo "systemctl restart web" | at now + 1 hour` (serviced by `atd`).

## systemd timers

systemd offers a modern alternative: a **`.timer`** unit that activates a matching
**`.service`** unit. You create two files — `backup.service` (what to do) and
`backup.timer` (when) — then enable the timer:

```ini
# backup.timer
[Timer]
OnCalendar=Mon *-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

```
$ sudo systemctl enable --now backup.timer
$ systemctl list-timers            # see all timers and next run times
```

Timers key on `OnCalendar=` (wall-clock schedules), `OnBootSec=` (after boot) or
`OnUnitActiveSec=` (intervals). `Persistent=true` makes a missed run (machine was
off) fire at next boot — something plain cron can't do.

> Why choose a systemd timer over cron? Timers log to the **journal** (so
> `journalctl -u backup.service` shows exactly what happened), can depend on other
> units, and catch up on missed runs. cron is simpler and universal; timers are
> more powerful and observable.

## Infrastructure as Code (IaC)

**Infrastructure as Code** means describing servers and configuration in text
files kept under version control, rather than configuring boxes by hand. Two ideas
define good IaC:

- **Declarative**: you state the *desired end state* ("nginx installed and
  running"), and the tool figures out how to get there — as opposed to
  *imperative* scripts that list every step.
- **Idempotent**: running the same definition repeatedly converges on the same
  result and makes no further changes once the state matches. Re-running is safe.

### Ansible

**Ansible** is the IaC tool Linux+ emphasizes. Its defining traits:

- **Agentless** — it needs no software installed on the targets; it connects over
  **SSH** (a **push** model from a control node). This contrasts with Puppet and
  Chef, which install an agent that **pulls** config from a server.
- An **inventory** file lists the managed hosts (and groups of hosts).
- **Playbooks** are YAML files containing **plays** and **tasks**; each task calls
  a **module** (like `apt`, `service`, `copy`) that is written to be idempotent.

```yaml
- hosts: webservers
  become: true
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: nginx
        state: present
    - name: Ensure nginx is running
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

Run it with `ansible-playbook site.yml`. Because the modules are idempotent, a
second run reports "ok" instead of changing anything.

## CI/CD pipelines

**CI/CD** automates the path from a code change to running software:

- **Continuous Integration (CI)** — every push triggers an automated **build and
  test**, catching breakage early.
- **Continuous Delivery/Deployment (CD)** — successful builds are automatically
  prepared for release (delivery) or pushed all the way to production
  (deployment).

A **pipeline** is a series of **stages** (typically *build → test → deploy*)
defined as code in the repository. **Runners** (or agents) execute the stages.
Common systems: **GitLab CI** (`.gitlab-ci.yml`), **GitHub Actions** (workflow
YAML under `.github/workflows/`) and **Jenkins** (`Jenkinsfile`). The pipeline
usually lives beside the application in Git, so the build process is versioned
right alongside the code it builds.

## Exam focus

- cron's five fields are **minute, hour, day-of-month, month, day-of-week** (0/7 =
  Sunday). `crontab -e/-l/-r` manage a user crontab; **`/etc/crontab`** and
  `/etc/cron.d/` add a **user field**. `at` schedules a **one-time** job.
- A **systemd timer** (`.timer`) triggers a `.service`; schedule with
  `OnCalendar=`, see them with `systemctl list-timers`, and `Persistent=true`
  catches up missed runs. Timers log to the **journal**; cron is simpler but less
  observable.
- IaC is **declarative** (describe the end state) and **idempotent** (safe to
  re-run).
- **Ansible is agentless, uses SSH, and pushes** from a control node; **playbooks**
  are YAML, organized into tasks that call idempotent **modules**, run with
  `ansible-playbook`. Puppet/Chef are agent-based pull models.
- **CI** = automated build + test on every change; **CD** = automated delivery/
  deployment. Pipelines define **stages** (build → test → deploy) as code
  (GitLab CI, GitHub Actions, Jenkins) and run on **runners**.
