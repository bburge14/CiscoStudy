# Storage, LVM & Network Configuration

Two kinds of resource turn a bare kernel into a useful server: **storage** that
holds data and a **network** that connects it to the world. This lesson covers how
Linux names disks, carves them into filesystems, layers LVM on top for
flexibility, and then how the modern `ip`/`nmcli` toolset configures the network.

## Disks, partitions and filesystems

Storage devices appear under `/dev`. SATA/SCSI disks are `/dev/sda`, `/dev/sdb`;
NVMe SSDs are `/dev/nvme0n1`. Partitions append a number: `/dev/sda1`,
`/dev/nvme0n1p1`.

A disk is first divided using a **partition table**:

- **MBR** (msdos) is the legacy scheme — limited to four primary partitions and
  2 TiB disks.
- **GPT** is the modern scheme — effectively unlimited partitions and huge disks,
  required for UEFI booting.

Partition editors include `fdisk` and `gdisk` (interactive) and `parted`
(scriptable). `lsblk` draws the block-device tree; `blkid` prints each device's
UUID and filesystem type.

A partition becomes usable only after you put a **filesystem** on it. The common
choices: **ext4** (the dependable general-purpose default), **XFS** (Red Hat's
default, strong with large files and parallelism), and **Btrfs** (copy-on-write
with built-in snapshots). Create one with `mkfs`:

```
$ sudo mkfs.ext4 /dev/sdb1
$ sudo mkfs.xfs  /dev/sdc1
```

### Mounting

To attach a filesystem into the tree, **mount** it onto a directory:

```
$ sudo mount /dev/sdb1 /mnt/data
$ sudo umount /mnt/data
```

Manual mounts vanish on reboot. For permanence, add a line to **`/etc/fstab`**,
whose six fields are: device, mount point, filesystem type, options, dump flag,
and fsck pass order.

```
UUID=1b9e...  /data   ext4   defaults   0  2
```

> Reference a filesystem by its **UUID** (from `blkid`) rather than `/dev/sdb1`.
> Device names can change when disks are added or reordered, but a UUID always
> follows its filesystem — a bad fstab entry can stop the system from booting.

**Swap** space extends RAM: `mkswap /dev/sdb2` formats it, `swapon`/`swapoff`
enable and disable it, and an fstab entry activates it at boot.

## Logical Volume Manager (LVM)

Raw partitions are rigid — resizing them is painful. **LVM** inserts a flexible
layer between physical disks and the filesystems you mount, in three tiers:

1. **Physical Volume (PV)** — a whole disk or partition handed to LVM
   (`pvcreate /dev/sdb1`).
2. **Volume Group (VG)** — a pool that aggregates one or more PVs
   (`vgcreate data_vg /dev/sdb1 /dev/sdc1`).
3. **Logical Volume (LV)** — a virtual "partition" carved from the VG that you
   format and mount (`lvcreate -L 50G -n web_lv data_vg`).

The payoff is **online flexibility**: a VG can span multiple disks, LVs can grow
while mounted, and LVM supports snapshots. To enlarge a volume you extend the LV
and then grow the filesystem to fill it:

```
$ sudo lvextend -L +20G /dev/data_vg/web_lv
$ sudo resize2fs /dev/data_vg/web_lv     # ext4; use xfs_growfs for XFS
```

Inspect each layer with `pvs`, `vgs` and `lvs` (or the verbose `pvdisplay`,
`vgdisplay`, `lvdisplay`). Add a new disk to a running pool with `vgextend`.

## Configuring the network

The old `ifconfig`, `route` and `netstat` tools are deprecated. The current
**iproute2** suite is the standard, and on most distributions **NetworkManager**
manages connections.

### The `ip` command

```
$ ip addr show                    # IP addresses on every interface (was ifconfig)
$ ip -brief addr                  # condensed one-line-per-interface view
$ sudo ip link set dev eth0 up    # bring an interface up/down
$ ip route show                   # the routing table (was route -n)
$ sudo ip route add default via 192.168.1.1   # set a default gateway
```

Changes made with `ip` are **not persistent** — they vanish on reboot. For a
lasting configuration, go through NetworkManager.

### Sockets with `ss`

`ss` replaces `netstat` for listing sockets. The classic invocation is
`ss -tulpn`: **t**cp, **u**dp, **l**istening, **p**rocess, **n**umeric — "what is
listening on this host, and which program owns each port."

### Persistent configuration with NetworkManager

`nmcli` is the scriptable front end:

```
$ nmcli device status                         # interfaces and their state
$ nmcli connection show                       # saved connection profiles
$ sudo nmcli connection modify eth0 ipv4.addresses 192.168.1.50/24 \
        ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1 ipv4.method manual
$ sudo nmcli connection up eth0               # apply the profile
```

`nmtui` offers the same thing in a text menu. Ubuntu layers **Netplan** (YAML in
`/etc/netplan/`) on top, while older Debian systems used
`/etc/network/interfaces`.

### Names and resolution

Set the hostname with `hostnamectl set-hostname web01` (writes `/etc/hostname`).
Name resolution reads `/etc/hosts` for static mappings first, then DNS servers;
`/etc/nsswitch.conf` decides that order and `/etc/resolv.conf` lists the DNS
servers (often managed by `systemd-resolved`). Test connectivity and DNS with
`ping`, `traceroute`/`tracepath`, and `dig`/`host` (`dig example.com`).

## Exam focus

- Disks live under `/dev` (`sda`, `nvme0n1`); partitions add a number. **GPT**
  supersedes **MBR** (which caps at four primary partitions and 2 TiB) and is
  required for UEFI.
- A partition needs a filesystem (`mkfs.ext4`, `mkfs.xfs`) before it can be
  mounted. `mount`/`umount` are temporary; `/etc/fstab` makes mounts persistent.
- In `/etc/fstab`, use the **UUID** (`blkid`), not the device name, so renumbered
  disks don't break the boot. Know the six fields.
- LVM stack, bottom to top: **PV → VG → LV** (`pvcreate` → `vgcreate` →
  `lvcreate`). Grow with `lvextend` *then* `resize2fs`/`xfs_growfs`. LVM's value is
  online resizing, spanning disks and snapshots.
- Modern networking uses **iproute2**: `ip addr`, `ip link`, `ip route` (replacing
  `ifconfig`/`route`) and `ss -tulpn` (replacing `netstat`). `ip` changes are not
  persistent.
- Make network settings stick with **NetworkManager** (`nmcli`/`nmtui`); Ubuntu
  adds Netplan. `hostnamectl` sets the hostname; `/etc/hosts`, `/etc/resolv.conf`
  and `/etc/nsswitch.conf` govern resolution.
