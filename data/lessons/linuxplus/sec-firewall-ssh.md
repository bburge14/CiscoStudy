# Host Firewalls & SSH Hardening

A server exposed to a network needs two defenses working together: a **firewall**
that controls which packets reach it, and a hardened **SSH** service, since SSH is
almost always the way administrators get in — and the first thing attackers probe.

## The firewall stack

All Linux firewalling happens in the kernel's **netfilter** framework. What
changes is the tool you use to write rules into it:

- **iptables** — the long-standing but **legacy** tool. Separate commands exist
  for IPv4 (`iptables`) and IPv6 (`ip6tables`), plus more for ARP and bridging.
- **nftables** — the modern replacement that **supersedes iptables**. A single
  `nft` tool and syntax handle IPv4, IPv6, ARP and bridge rules together, with
  better performance. Major distributions now default to the nftables backend; on
  many systems the familiar `iptables` command is actually a compatibility
  shim (`iptables-nft`) that writes nftables rules underneath.

Most administrators don't touch either directly, using a higher-level manager
instead — **firewalld** on Red Hat family systems, **ufw** on Ubuntu.

### iptables essentials

iptables organizes rules into **tables** (the common one is `filter`) made of
**chains**. The filter table has three built-in chains:

| Chain | Traffic it sees |
|-------|-----------------|
| `INPUT` | Packets destined for this host |
| `OUTPUT` | Packets this host sends |
| `FORWARD` | Packets routed *through* this host |

Each rule ends in a **target**: `ACCEPT`, `DROP` (discard silently) or `REJECT`
(discard with an error reply). `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
appends a rule allowing SSH; `-L` lists rules, `-D` deletes one. Each chain also
has a default **policy** applied when no rule matches.

### firewalld (zones)

**firewalld** is dynamic and organized around **zones** — named trust levels
(`public`, `home`, `trusted`, `drop`, …) that you assign to interfaces. It uses
the nftables backend. Changes are runtime-only unless you add `--permanent`, then
reload:

```
$ sudo firewall-cmd --get-active-zones
$ sudo firewall-cmd --zone=public --add-service=https --permanent
$ sudo firewall-cmd --zone=public --add-port=8443/tcp --permanent
$ sudo firewall-cmd --reload           # apply permanent rules
```

> A classic firewalld mistake: adding a rule without `--permanent`, which works
> until the next reload/reboot and then vanishes. Add `--permanent`, then
> `--reload`.

### ufw (Ubuntu)

**ufw** ("uncomplicated firewall") is a thin, friendly front end:

```
$ sudo ufw allow 22/tcp
$ sudo ufw allow OpenSSH
$ sudo ufw enable
$ sudo ufw status verbose
```

## SSH: the service you must harden

**OpenSSH** provides encrypted remote login. The client is `ssh`; the server
daemon is `sshd`, configured in **`/etc/ssh/sshd_config`**. (Don't confuse it with
`ssh_config`, the *client* config.) After any change, reload or restart:
`sudo systemctl restart sshd`.

### Key-based authentication

The single biggest hardening step is replacing passwords with **key pairs**. You
generate a pair, keep the private key secret, and install the public key on the
server:

```
$ ssh-keygen -t ed25519 -C "jordan@laptop"     # ed25519 is modern and compact
$ ssh-copy-id jordan@web01                      # append pubkey to the server
```

The server stores authorized public keys in each user's
`~/.ssh/authorized_keys`. The client's `~/.ssh/config` can store per-host
settings, and `~/.ssh/known_hosts` records server host keys so the client can
detect a server being impersonated.

### Hardening directives in `sshd_config`

| Directive | Hardened value | Why |
|-----------|----------------|-----|
| `PermitRootLogin` | `no` | Force admins to log in as themselves, then `sudo` |
| `PasswordAuthentication` | `no` | Keys only — defeats brute-force and credential stuffing |
| `PubkeyAuthentication` | `yes` | Enable key auth |
| `Port` | e.g. `2222` | Moving off 22 cuts automated noise (obscurity, not real security) |
| `AllowUsers` / `AllowGroups` | explicit list | Only named users/groups may connect |
| `MaxAuthTries` | low (e.g. `3`) | Limit guesses per connection |
| `ClientAliveInterval` | e.g. `300` | Disconnect idle sessions |

> The highest-value pair is **`PermitRootLogin no`** plus **`PasswordAuthentication
> no`**. Together they stop the two most common attacks at once: guessing the root
> password and brute-forcing any password. Make sure your key works *before* you
> disable passwords, or you can lock yourself out.

To slow brute-force attempts further, tools like **fail2ban** watch the auth logs
and temporarily firewall-ban IPs that fail repeatedly.

## Exam focus

- All firewalling runs in the kernel's **netfilter**. **nftables supersedes
  iptables**; `nft` is one tool for IPv4/IPv6/ARP/bridge, and `iptables` is often
  a compatibility shim over the nftables backend.
- iptables filter chains: **INPUT** (to host), **OUTPUT** (from host), **FORWARD**
  (through host). Targets: **ACCEPT**, **DROP** (silent), **REJECT** (with reply).
- **firewalld** uses **zones**; changes need `--permanent` then
  `firewall-cmd --reload` to persist. **ufw** is Ubuntu's simple front end
  (`ufw allow 22/tcp`, `ufw enable`).
- SSH server config is **`/etc/ssh/sshd_config`**; restart `sshd` after edits.
  `ssh-keygen` makes a key pair (prefer **ed25519**); `ssh-copy-id` installs the
  public key into `~/.ssh/authorized_keys`.
- Top hardening: **`PermitRootLogin no`** and **`PasswordAuthentication no`**
  (keys only); also `AllowUsers`/`AllowGroups`, `MaxAuthTries`, idle timeouts, and
  optionally a non-standard port. Confirm key login works before disabling
  passwords.
