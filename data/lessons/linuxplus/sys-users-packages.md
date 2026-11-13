# Users, Groups & Package Management

Two routine administrative jobs share this lesson: deciding *who* may log in and
what identity they carry, and getting *software* onto the machine safely. Both
come down to a few authoritative text files and the command families that edit
them for you.

## Who the system knows: users and groups

Every account the system recognizes is recorded in flat, colon-delimited files.

### `/etc/passwd`

Despite the name, it no longer holds passwords. Each line is one account:

```
jordan:x:1000:1000:Jordan Lee:/home/jordan:/bin/bash
  [1]  [2] [3]  [4]    [5]         [6]         [7]
```

1. **Username.**
2. Password placeholder — the `x` means "the real hash is in `/etc/shadow`."
3. **UID** (user ID). `0` is always **root**; low numbers are system accounts;
   regular users typically start at **1000**.
4. **GID** of the user's primary group.
5. **GECOS** — a comment field, usually the full name.
6. **Home directory.**
7. **Login shell** (`/bin/bash`, or `/usr/sbin/nologin` to block interactive
   login).

### `/etc/shadow` and `/etc/group`

The password hashes live in `/etc/shadow`, readable only by root, along with
**password-aging** fields (last change, minimum/maximum age, warning and
expiration). Groups are defined in `/etc/group`, where each line lists the group
name, GID and the members who have it as a *supplementary* group.

> A user has exactly **one primary group** (from the GID field in `/etc/passwd`)
> and any number of **supplementary groups** (listed in `/etc/group`). New files
> they create are owned by their primary group.

### Managing accounts

Edit these files with purpose-built tools, never by hand in production:

- `useradd -m -s /bin/bash -G sudo,developers jordan` creates the account, makes
  the home directory (`-m`, populated from the `/etc/skel` template), sets the
  shell and adds supplementary groups.
- `passwd jordan` sets or changes the password.
- `usermod -aG docker jordan` **appends** a group — the `-a` is critical, because
  `usermod -G` *alone* replaces the whole supplementary list and can silently drop
  a user out of groups.
- `userdel -r jordan` removes the account and its home directory.
- `groupadd`, `groupmod`, `groupdel` manage groups; `chage` tunes password aging.

To check identity: `id` prints your UID, GID and all groups; `whoami` prints the
current username; `groups` lists your group memberships.

## Getting software: two package ecosystems

Linux software comes in packages, and there are two dominant families. In each,
there is a **low-level** tool that installs a single package file and a
**high-level** tool that talks to online **repositories** and resolves
dependencies automatically.

| Family | Low-level (single file) | High-level (repos + deps) | Package |
|--------|------------------------|---------------------------|---------|
| Debian / Ubuntu | `dpkg` | `apt` (and `apt-get`) | `.deb` |
| RHEL / Fedora / SUSE | `rpm` | `dnf` (successor to `yum`) | `.rpm` |

> The key distinction: **low-level tools do not resolve dependencies.** If you
> `dpkg -i` or `rpm -i` a package whose libraries are missing, it fails and tells
> you what is absent. The high-level tools (`apt`, `dnf`) pull the dependencies
> from configured repositories for you.

### Debian/Ubuntu with `apt` and `dpkg`

```
$ sudo apt update                 # refresh the package index from repositories
$ sudo apt upgrade                # apply available updates
$ sudo apt install nginx          # install, resolving dependencies
$ sudo apt remove nginx           # remove (purge also deletes config)
$ apt search "web server"         # find packages
```

Repositories are listed in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`.
Drop to `dpkg` to inspect: `dpkg -l` lists installed packages, `dpkg -L nginx`
shows which files a package installed, and `dpkg -S /usr/sbin/nginx` tells you
which package owns a file.

### RHEL/Fedora with `dnf` and `rpm`

```
$ sudo dnf install httpd          # install with dependency resolution
$ sudo dnf remove httpd           # remove
$ sudo dnf upgrade                # update everything
$ dnf info httpd                  # show package details
```

Repositories live in `/etc/yum.repos.d/`. The low-level `rpm` queries mirror
`dpkg`'s: `rpm -qa` lists all installed packages, `rpm -ql httpd` lists a
package's files, `rpm -qf /usr/sbin/httpd` finds the owning package, and
`rpm -e` erases one. Install a standalone file with `rpm -i package.rpm` (or,
better, `dnf install ./package.rpm` so dependencies are handled).

### Distribution-agnostic packaging

Newer formats bundle an app with its dependencies so it runs anywhere:
**Flatpak** and **Snap** deliver sandboxed desktop and server apps from their own
stores, and an **AppImage** is a single self-contained executable file. They trade
disk space for not fighting system library versions.

## A quick mental model

Think of package management as a two-layer stack. The **high-level** layer (`apt`,
`dnf`) is where you normally work: it knows about remote repositories, signs and
verifies downloads, and untangles the dependency graph. The **low-level** layer
(`dpkg`, `rpm`) is the engine underneath — it actually unpacks files and records
what is installed, but it trusts you to have supplied every dependency. When a
high-level command misbehaves, dropping to the low-level query commands
(`dpkg -l`, `rpm -qa`) is how you see the ground truth of what is really on disk.

## Exam focus

- `/etc/passwd` has seven colon-separated fields; memorize them in order
  (name, `x`, UID, GID, GECOS, home, shell). **UID 0 = root.** Password hashes and
  aging data live in `/etc/shadow`.
- A user has one **primary group** (the `/etc/passwd` GID) and many
  **supplementary groups** (`/etc/group`).
- `usermod -aG group user` adds a group; forgetting `-a` **replaces** the
  supplementary groups and can lock a user out of others.
- `useradd -m` creates the home directory from `/etc/skel`; `userdel -r` removes
  the home directory too.
- Pair the tools: Debian uses `.deb` with `dpkg` (low-level) and `apt`
  (high-level); RHEL uses `.rpm` with `rpm` (low-level) and `dnf` (high-level).
- **Low-level tools (`dpkg -i`, `rpm -i`) do not resolve dependencies; high-level
  tools (`apt`, `dnf`) do** by talking to repositories.
- Know the query verbs: list files in a package (`dpkg -L`, `rpm -ql`), find the
  owning package of a file (`dpkg -S`, `rpm -qf`), list all installed
  (`dpkg -l`, `rpm -qa`).
- `apt update` refreshes the index; `apt upgrade` installs updates — two different
  steps.
