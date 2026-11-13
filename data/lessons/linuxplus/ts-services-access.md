# Service, Boot & Access Failures

Two of the most common "it won't work" tickets are a **service that won't start**
(sometimes taking the whole boot with it) and a **user who can't get in or get at
a file**. Both are highly diagnosable once you know where systemd and the
permission stack record *why* they said no.

## Diagnosing a failed service

When a service misbehaves, `systemctl status` is the first stop — it shows the
state, the main PID, and the last few log lines:

```
$ systemctl status nginx
   Active: failed (Result: exit-code) since ...
  Process: 1203 ExecStart=/usr/sbin/nginx ... (code=exited, status=1/FAILURE)
```

Quick checks:

- `systemctl is-active sshd`, `is-enabled`, `is-failed` give one-word answers.
- **`systemctl --failed`** lists every unit in a failed state — a great overview.
- **`journalctl -u nginx -b`** shows that service's logs for this boot;
  **`journalctl -xe`** shows the latest entries with added explanations.

Then match the message to a cause:

| Symptom in the log | Likely cause |
|--------------------|--------------|
| "Address already in use" | Another process holds the port (`ss -tulpn` to find it) |
| "Permission denied" on a path | Wrong file ownership/mode, or an **SELinux** denial |
| "failed to parse" / config error | A typo in the config; test it (`nginx -t`, `sshd -t`) |
| Dependency job failed | A required unit didn't start |

> Two reflexes save time: after editing a **unit file**, run `systemctl
> daemon-reload` before restarting, or systemd runs the old definition. And if the
> service's own config changed, use the app's **config test** (`nginx -t`,
> `sshd -t`, `visudo -c`) to catch syntax errors before restarting.

## Boot failures

A failed service at boot can drop the system into **emergency** or **rescue**
mode. To investigate:

- **`systemctl --failed`** and `journalctl -b` identify which unit broke the boot.
- **`systemd-analyze blame`** and `systemd-analyze critical-chain` show what's slow
  or stalling startup.
- `rescue.target` gives a minimal single-user shell; `emergency.target` is even
  more minimal (root filesystem read-only).

For deeper problems you intervene at **GRUB**: press `e` to edit the boot entry and
append a kernel parameter. Adding `systemd.unit=rescue.target` boots to rescue;
`rd.break` drops into the initramfs for root-password recovery. If GRUB itself is
broken (missing config, reinstalled Windows), you regenerate it
(`grub2-mkconfig`/`update-grub`) or reinstall it. A corrupt or missing
**initramfs** is rebuilt with `dracut` (Red Hat) or `update-initramfs` (Debian).

## "Permission denied" on a file

When a user can't access a file, walk the permission stack in order:

1. **Base permissions and ownership** — `ls -l file`. Does the user's identity
   (owner? group? other?) have the needed bit? Remember a user needs **execute on
   every directory** in the path to even reach the file.
2. **ACLs** — a trailing **`+`** in `ls -l` means extra ACL entries; inspect with
   `getfacl file`. The ACL may be granting or *restricting* beyond the base mode.
3. **SELinux** — if permissions look correct but access is still denied on an
   SELinux system, suspect a **context** mismatch. Check with `ls -Z`, look for
   `avc: denied` messages in `/var/log/audit/audit.log` (via `ausearch`), and fix
   with `restorecon`. A quick test: setting SELinux to permissive
   (`setenforce 0`) temporarily — if the problem vanishes, it was SELinux.

## Login and access failures

A user who can't log in has a different checklist:

- **Locked account** — `passwd -l` locks it, and `pam_faillock` can lock it after
  failed attempts; check and clear with `faillock --user jordan --reset`.
- **Expired password or account** — `chage -l jordan` shows aging and the
  expiration date.
- **No valid shell** — if the login shell in `/etc/passwd` is
  `/usr/sbin/nologin` or `/bin/false`, interactive login is blocked by design.
- **Home directory** missing or wrong-permissioned can break login or leave the
  user in `/`.

### sudo and group problems

- "user is not in the sudoers file" means the account lacks a sudo rule — add it
  to the `wheel`/`sudo` group or a `/etc/sudoers.d/` entry (edited with
  `visudo`).
- A freshly added group membership **doesn't apply to existing sessions** — the
  user must **log out and back in** (or start a new login shell). Verify effective
  groups with `id`.

### SSH access specifically

Key-based SSH is strict about **permissions on the key files**: `~/.ssh` must be
`700` and `~/.ssh/authorized_keys` `600`, owned by the user. If they're too open,
`sshd` silently refuses the key. Check the server's `/var/log/auth.log`
(or `secure`), confirm `PubkeyAuthentication yes`, and remember that
`PermitRootLogin no` or `PasswordAuthentication no` can be exactly why a
particular login is rejected. `sshd -T` dumps the effective server config.

## Exam focus

- Start service problems with **`systemctl status`** and **`journalctl -u <unit>
  -b`**; **`systemctl --failed`** lists all failed units; `journalctl -xe` adds
  context. After editing a unit, **`daemon-reload`**; test app config with
  `nginx -t` / `sshd -t` / `visudo -c`.
- "Address already in use" → find the holder with `ss -tulpn`. Permission-denied
  on a correctly-permissioned path on Red Hat → suspect **SELinux**.
- Boot issues: inspect with `systemctl --failed`, `journalctl -b`,
  `systemd-analyze blame`; recover via **rescue/emergency** targets or by editing
  the **GRUB** kernel line (`rd.break` for root-password reset). Rebuild a broken
  initramfs with `dracut`/`update-initramfs`.
- File "permission denied": check **mode + ownership** (and **execute on every
  parent directory**), then **ACLs** (the `+` in `ls -l`, `getfacl`), then
  **SELinux** context (`ls -Z`, `avc: denied` in the audit log, `restorecon`).
- Login failures: **locked** account (`faillock`, `passwd -l`), **expired**
  password/account (`chage -l`), a **nologin** shell, or a bad home directory.
- A new **group** needs a fresh login to take effect (`id` to verify). sudo
  failures mean no sudoers/`wheel` membership.
- SSH keys require **`~/.ssh` = 700, `authorized_keys` = 600**; wrong modes make
  `sshd` reject the key. Check `auth.log`/`secure` and `sshd -T`.
