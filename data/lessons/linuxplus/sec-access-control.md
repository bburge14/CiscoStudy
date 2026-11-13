# Access Control: sudo, PAM, SELinux & AppArmor

File permissions decide what an identity may touch. This lesson covers the layers
*around* that: how users borrow elevated privilege with **sudo**, how
authentication itself is assembled from **PAM** modules, and how **SELinux** and
**AppArmor** add a mandatory policy that even root must obey.

## Elevating privilege: sudo and su

Logging in as root directly is discouraged. Instead, ordinary users borrow
privilege:

- **`su`** switches to another user (root by default), prompting for *that user's*
  password. `su -` also loads the target's login environment — a crucial
  difference from a bare `su`.
- **`sudo`** runs a *single* command as root (or another user with `-u`),
  prompting for *your own* password, and logs every invocation. This is the
  preferred model because privilege is granular and auditable.

Who may run what is defined in **`/etc/sudoers`**, always edited with
**`visudo`** (it syntax-checks before saving, so a typo can't lock everyone out).
A rule reads *who*, on *which hosts*, *as whom*, may run *which commands*:

```
jordan   ALL=(ALL:ALL) ALL                       # jordan may run anything
%wheel   ALL=(ALL)     ALL                        # members of group wheel (note %)
deploy   ALL=(root)    NOPASSWD: /usr/bin/systemctl restart web
```

Drop-in rules go in `/etc/sudoers.d/`. The `%` prefix denotes a group.

## PAM: how authentication is assembled

Most programs don't implement authentication themselves — they call **PAM
(Pluggable Authentication Modules)**. Each service has a config in `/etc/pam.d/`
(for example `/etc/pam.d/sshd`) built from stacked modules.

A PAM line has a **type**, a **control flag**, and a **module**:

- **Types**: `auth` (verify identity), `account` (is the account allowed/valid
  right now), `password` (change credentials), `session` (set up/tear down the
  session).
- **Control flags**: `required` (must pass, but keep going), `requisite` (must
  pass, fail immediately), `sufficient` (pass here is enough), `optional`.

Common modules worth recognizing: `pam_unix` (the classic `/etc/shadow` check),
`pam_faillock` (lock accounts after repeated failures), `pam_pwquality` (enforce
password complexity), and `pam_limits`, which applies the resource limits in
`/etc/security/limits.conf`.

> PAM is *stacked and ordered*: a login succeeds only if the module stack as a
> whole says yes. This is how one change — say, adding `pam_faillock` — can add
> lockout to every service that authenticates through PAM.

## DAC vs. MAC

The permission and ACL model you already know is **Discretionary Access Control
(DAC)**: the *owner* decides who gets access. **Mandatory Access Control (MAC)**
adds a second gate — a system-wide policy, set by the administrator, that
processes cannot override no matter what the file permissions say. Even root is
constrained by it. Linux has two MAC implementations.

## SELinux (label-based)

**SELinux** labels every process and object with a **security context** and allows
an action only if policy permits that pairing. It runs in one of three **modes**:

| Mode | Behavior |
|------|----------|
| **Enforcing** | Policy is applied; violations are blocked *and* logged |
| **Permissive** | Policy is *not* enforced; violations are only logged (ideal for debugging) |
| **Disabled** | SELinux off entirely |

Check the mode with `getenforce`; toggle *temporarily* with `setenforce 1`
(enforcing) or `setenforce 0` (permissive). You **cannot disable** SELinux with
`setenforce` — persistent changes, including disabling, are made in
`/etc/selinux/config` (`SELINUX=enforcing`, `SELINUXTYPE=targeted`) and take
effect at the next boot.

A context has four colon-separated fields — `user:role:type:level`, e.g.
`system_u:object_r:httpd_sys_content_t:s0`:

> The **type** field is the one that matters most. SELinux's default `targeted`
> policy works mainly through **type enforcement** — matching a process's type
> (its *domain*) against an object's type.

View contexts with the `-Z` flag: `ls -Z`, `ps -Z`, `id -Z`. Managing them:

- `restorecon -Rv /var/www` resets files to the **default** context defined by
  policy — the usual fix after files are moved or restored.
- `chcon -t httpd_sys_content_t file` sets a context *temporarily* (lost on the
  next relabel).
- `semanage fcontext -a -t httpd_sys_content_t "/web(/.*)?"` records a
  **persistent** default; follow it with `restorecon`.
- **Booleans** toggle optional policy behavior: `getsebool -a` lists them,
  `setsebool -P httpd_can_network_connect on` sets one permanently (`-P`).

Denials are logged to `/var/log/audit/audit.log`; `ausearch` and `sealert` help
interpret them.

## AppArmor (path-based)

Debian, Ubuntu and SUSE favor **AppArmor**, which confines programs by **file
path** rather than by label. Each confined program has a **profile** under
`/etc/apparmor.d/` that lists the paths and capabilities it may use. A profile
runs in one of two modes:

- **enforce** — violations are blocked.
- **complain** — violations are only logged (the counterpart to SELinux
  permissive, good for building a profile).

Manage it with `aa-status` (what's loaded and in which mode), `aa-enforce` and
`aa-complain` to switch a profile's mode.

> The headline distinction for the exam: **SELinux is label/context-based**
> (and the Red Hat default); **AppArmor is path-based** (and the Ubuntu/SUSE
> default). Both provide MAC on top of ordinary DAC permissions.

## Exam focus

- `su -` loads the target user's login environment; a bare `su` does not. `sudo`
  runs one command as root using *your own* password and logs it — prefer it over
  a root login.
- Always edit sudo rules with **`visudo`**; it validates syntax. Rule form:
  `user host=(runas) commands`; `%group` targets a group; `NOPASSWD:` skips the
  prompt. Drop-ins live in `/etc/sudoers.d/`.
- PAM configs live in `/etc/pam.d/`. Know the four types (`auth`, `account`,
  `password`, `session`) and the control flags (`required`, `requisite`,
  `sufficient`, `optional`). `pam_pwquality` = complexity, `pam_faillock` =
  lockout, `pam_limits` + `/etc/security/limits.conf` = resource limits.
- **DAC** = owner decides; **MAC** = system policy decides, binding even root.
- SELinux modes: **enforcing** (block + log), **permissive** (log only),
  **disabled**. `getenforce`/`setenforce 0|1`; `setenforce` cannot *disable* it —
  use `/etc/selinux/config` for a persistent change.
- SELinux context = `user:role:type:level`; the **type** drives enforcement. View
  with `-Z`; `restorecon` resets to policy default, `chcon` is temporary,
  `semanage fcontext` is persistent; booleans via `setsebool -P`.
- **SELinux = label-based (Red Hat default); AppArmor = path-based (Ubuntu/SUSE),
  with enforce vs. complain modes** (`aa-status`, `aa-enforce`, `aa-complain`).
