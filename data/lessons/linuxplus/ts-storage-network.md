# Storage & Network Diagnostics

Storage and network faults share a diagnostic style: work in layers, and let each
tool rule out one possibility before moving to the next. This lesson pairs the two
because the method is the same — isolate the failing layer, confirm it, then fix
it.

## Storage: "no space left on device"

The classic storage incident is a full disk, but the message can lie in two ways.
Start with the obvious check:

```
$ df -h               # free space per filesystem
$ du -sh /var/* | sort -rh | head      # which directories are eating it
```

If `df -h` shows a filesystem at 100%, hunt down the culprit with `du` and clear
it. But if `df -h` shows **free space** and you *still* get "No space left on
device," suspect one of two subtler causes:

- **Inode exhaustion.** A filesystem can run out of **inodes** (the records that
  track files) while bytes remain — typical when something created millions of
  tiny files. Check with **`df -i`**; if `IUse%` is 100%, you're out of inodes,
  not space.
- **A deleted-but-open file.** If a process is still writing to a file that was
  `rm`'d, the space isn't freed until the process closes it. Find it with
  `lsof | grep deleted`, then restart the offending process.

> `df` says a filesystem is full but you can't see the files? Check **`df -i`**
> (inodes) and **`lsof | grep deleted`** (space held open by a process) before you
> start deleting things at random.

### Mount and filesystem problems

- `findmnt` and `mount` show what's mounted where. After editing `/etc/fstab`,
  test it with **`mount -a`** *before* rebooting — a bad fstab entry can leave the
  system unbootable.
- A filesystem that hits errors often **remounts read-only** to protect itself;
  you'll see "Read-only file system" and I/O errors in **`dmesg`**.
- Repair an **unmounted** filesystem with **`fsck`** (ext family) or
  **`xfs_repair`** (XFS). Never run `fsck` on a mounted filesystem.
- Check the physical disk's health with **`smartctl -a /dev/sda`**; SMART
  attributes and a "FAILING_NOW" flag warn of a dying drive before it dies.

For LVM, confirm the stack with `pvs`, `vgs`, `lvs`; a volume that's full can often
be grown with `lvextend` followed by `resize2fs`/`xfs_growfs`.

## Network: isolate by layer

Network troubleshooting is most reliable when you climb the stack in order, from
the local link outward.

### 1. Do I have a working interface and address?

```
$ ip link show        # is the interface UP? (state UP vs DOWN)
$ ip addr show        # do I have an IP address on it?
```

No IP usually means a DHCP or configuration problem. An interface in state `DOWN`
needs `ip link set dev eth0 up` (or a NetworkManager fix).

### 2. Can I reach the gateway, then the internet?

```
$ ip route show                 # is there a default gateway?
$ ping -c3 192.168.1.1          # the gateway (local reachability)
$ ping -c3 1.1.1.1              # an outside IP (routing / NAT)
```

The logic: if you **can't ping the gateway**, the problem is local (cable, switch,
interface, VLAN). If you **can ping the gateway but not an outside IP**, it's
routing, NAT or an upstream issue.

### 3. Is it DNS?

```
$ ping -c3 1.1.1.1             # works (IP reachable)
$ ping -c3 example.com        # fails ("Name or service not known")
```

That pattern — **IP works, name doesn't** — is the signature of a **DNS problem**.
Confirm by resolving directly with **`dig example.com`** (or `host`/`nslookup`) and
check `/etc/resolv.conf` for the configured servers. `traceroute`/`tracepath` (or
`mtr`) map the hops along the path when routing is in doubt.

### 4. Is the service actually listening — and reachable?

Even with a perfect network, the application may not be up or may be firewalled:

- **`ss -tulpn`** shows what's **listening**, on which port and interface, and
  which process owns it. If your service isn't there, it isn't running or didn't
  bind.
- Watch the bind address: a service listening on `127.0.0.1` is reachable only
  locally, not from other hosts — bind to `0.0.0.0` for external access.
- Test a port from a client with **`nc -zv host 443`**, `curl`, or `telnet host
  443`. If the port is open locally (`ss`) but unreachable remotely, suspect a
  **firewall** (firewalld/nftables/ufw) dropping it.

> A port that `ss` shows listening locally but that a remote client can't reach is
> almost always a **firewall rule** or a **bind-address** issue — not the service
> itself.

## Exam focus

- "No space left on device": start with **`df -h`**. If space looks free, check
  **`df -i`** (inode exhaustion) and **`lsof | grep deleted`** (space held by a
  process that has an open deleted file).
- Find big consumers with **`du -sh ... | sort -rh`**. Test `/etc/fstab` with
  **`mount -a`** before rebooting. A filesystem with errors remounts **read-only**
  (see `dmesg`).
- Repair filesystems **unmounted** with **`fsck`** / **`xfs_repair`**; check disk
  health with **`smartctl`**.
- Troubleshoot the network **in layers**: interface up + IP (`ip link`,
  `ip addr`) → gateway reachable (`ping` gateway) → internet (`ping` an outside
  IP) → DNS → service.
- **Can ping an IP but not a hostname = DNS.** Confirm with **`dig`**/`host`; check
  `/etc/resolv.conf`.
- **`ss -tulpn`** shows listening ports and owning processes; `nc`/`curl`/`telnet`
  test reachability. A locally-listening port that's remotely unreachable points
  to a **firewall** or a **127.0.0.1 bind address**.
