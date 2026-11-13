# Permissions, Special Bits & ACLs

Linux security starts with a deceptively simple model: every file has an owner, a
group, and three sets of permission bits. Master the base model and its octal
math, then the three *special* bits and the ACL system that extends it, and you
can both read any `ls -l` line and remediate a dangerous one.

## The base model: user, group, other

Each file carries three permission triples — for the **owner (user)**, the owning
**group**, and everyone **else (other)** — and three permissions in each:

| Permission | Letter | Octal | On a file | On a directory |
|------------|--------|-------|-----------|----------------|
| Read | `r` | 4 | Read the contents | List the names inside |
| Write | `w` | 2 | Modify the contents | Create/rename/delete entries |
| Execute | `x` | 1 | Run it as a program | Enter/traverse it (`cd`) |

> The directory meanings trip people up. To *enter* a directory or reach anything
> inside it, you need **execute** on it. Read without execute lets you see the
> names but not use them; and because delete is a *write to the directory*, you
> can delete a file you don't own as long as you can write to its directory.

### Reading and writing the bits

`ls -l` shows the triples as nine characters: `rwxr-xr--` means owner `rwx`,
group `r-x`, other `r--`. Convert to octal by summing each triple: `7` `5` `4`.

Set permissions with **`chmod`**, either symbolically or in octal:

```
$ chmod u+x deploy.sh        # add execute for the owner
$ chmod go-w report.txt      # remove write from group and other
$ chmod a=r notes.txt        # set all three to read-only
$ chmod 640 secrets.env      # owner rw-, group r--, other ---
```

Change ownership with **`chown`** and **`chgrp`**:

```
$ sudo chown jordan:developers app.log   # set owner AND group
$ sudo chown -R jordan /srv/app          # recurse through a tree
```

### umask: the default

New files don't come out world-writable because the **umask** *masks off* bits
from the base default (666 for files, 777 for directories). A umask of `022`
leaves files at `644` and directories at `755`. Check it with `umask`; set it in a
shell or `/etc/profile`.

## The three special bits

Beyond `rwx`, a **fourth, leading octal digit** holds three special bits:

| Bit | Octal | Set on | Effect |
|-----|-------|--------|--------|
| **setuid** | 4 | executable | Runs with the **file owner's** identity, not the caller's |
| **setgid** | 2 | executable | Runs with the file's **group**; on a *directory*, new files inherit that group |
| **sticky** | 1 | directory | Only a file's **owner** (or root) may delete it, even in a shared, writable dir |

So `chmod 4755 program` sets setuid plus `755`; `chmod 2770 shared` sets setgid
plus `770`; `chmod 1777 /tmp` sets the sticky bit plus `777`.

The classic examples: `/usr/bin/passwd` is **setuid root** so an ordinary user can
update the root-owned `/etc/shadow`; a shared project directory is **setgid** so
every file created in it belongs to the team's group; and `/tmp` is **sticky** so
users can't delete each other's temporary files.

### Reading special bits in `ls -l`

They appear *in place of* the execute character:

- `-rwsr-xr-x` — lowercase **`s`** in the owner's execute slot = setuid *with*
  execute. A capital **`S`** means the bit is set but execute is **not** (usually
  a misconfiguration).
- `drwxrws---` — **`s`** in the group slot = setgid.
- `drwxrwxrwt` — **`t`** in the other slot = sticky *with* execute; capital **`T`**
  means sticky without execute.

```
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68208 ... /usr/bin/passwd      # setuid root
$ ls -ld /tmp
drwxrwxrwt 10 root root 4096 ... /tmp                 # sticky
```

## Access Control Lists (ACLs)

The owner/group/other model can only express one group. When you need to grant a
*specific* extra user or group different access, use **ACLs**.

- `getfacl file` displays the full ACL.
- `setfacl -m u:jordan:rw report.txt` grants user `jordan` read/write without
  changing the file's owner or group.
- `setfacl -m g:auditors:r report.txt` grants a named group read.
- `setfacl -x u:jordan report.txt` removes that entry; `setfacl -b` strips all
  ACLs.
- `setfacl -d -m u:jordan:rw /srv/shared` sets a **default** ACL on a directory so
  new files created inside inherit it.

A **`+`** at the end of the `ls -l` permission string (`-rw-r--r--+`) is the tell
that extra ACL entries exist beyond what the base triples show.

## Permission remediation

Fixing bad permissions is routine security work. Overly permissive files —
especially world-writable ones or stray setuid binaries — are findable with
`find`:

```
$ find /srv -perm -o+w -type f        # world-writable files
$ find / -perm -4000 -type f 2>/dev/null   # every setuid executable
```

Then tighten them: remove world write with `chmod o-w`, strip an unneeded setuid
bit with `chmod u-s`, and correct ownership with `chown`. The guiding principle is
**least privilege** — grant the narrowest access that still lets the work happen.

## Exam focus

- Read = 4, write = 2, execute = 1, summed per triple (owner/group/other). `rwx` =
  7, `r-x` = 5, `r--` = 4. On a **directory**, execute means traverse and write
  means create/delete entries.
- `chmod` takes symbolic (`u+x`, `go-w`, `a=r`) or octal (`640`). `chown
  user:group` sets both; `-R` recurses. **umask** subtracts from the default
  (022 → 644 files, 755 dirs).
- Special-bit octal values: **setuid = 4, setgid = 2, sticky = 1**, written as a
  leading fourth digit (`chmod 4755`, `2770`, `1777`).
- setuid/setgid make an executable run as the file's **owner/group**; **setgid on
  a directory** makes new files inherit its group; the **sticky bit** on a shared
  directory (like `/tmp`) stops users deleting others' files.
- In `ls -l`, `s`/`t` show the bit set *with* execute; capital `S`/`T` show it set
  *without* execute. A trailing **`+`** means an ACL is present.
- ACLs grant extra users/groups access: `setfacl -m u:name:rw`, read back with
  `getfacl`, inherit with a default ACL (`-d`).
- Remediate with `find -perm` to locate world-writable or setuid files, then
  tighten toward least privilege.
