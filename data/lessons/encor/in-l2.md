# Advanced Layer 2 & EtherChannel

## STP protection features
| Feature | Where | Trigger | Action |
|---------|-------|---------|--------|
| **BPDU Guard** | PortFast access ports | **any** BPDU received | err-disable the port |
| **Root Guard** | designated ports to other switches | a **superior** BPDU | root-inconsistent (blocking) until it stops |
| **Loop Guard** | non-designated (root/alternate) ports | BPDUs **stop** arriving | loop-inconsistent (blocking) |
| **BPDU Filter** | PortFast ports | — | suppresses sending/receiving BPDUs |
| **UDLD** | fiber links | unidirectional link detected | err-disable / warn |

Key distinction: **BPDU Guard** reacts to a BPDU *arriving* where none should;
**Loop Guard** reacts to a BPDU that *stopped* arriving where it should keep
coming (a failing unidirectional link that could open a loop).

## Rapid-PVST+ and MST
- **Rapid-PVST+** — one RSTP instance per VLAN (fast convergence, Cisco default
  on many platforms). States: discarding, learning, forwarding.
- **MST (802.1s)** — maps many VLANs to a few instances, cutting CPU/BPDU load in
  large VLAN counts. Switches in the same MST **region** must agree on region
  name, revision and VLAN-to-instance mapping.

## EtherChannel (advanced)
Mode matrix (same as CCNA, worth over-learning):
- LACP: **active/active**, **active/passive** form; **passive/passive** fails.
- PAgP: **desirable/desirable**, **desirable/auto** form; **auto/auto** fails.
- Static **on** only pairs with **on**.

### Load balancing
EtherChannel hashes each **flow** to exactly **one** member link — it never
splits a single conversation. If one heavy src/dst pair overloads a link, add
more entropy to the hash:
```
port-channel load-balance src-dst-port     ! include L4 ports
show etherchannel load-balance
```
Members must match in speed, duplex, trunk mode and allowed VLANs or they won't
bundle (you'll see `(I)` individual or `(s)` suspended in
`show etherchannel summary`).

## LACP extras
- **System priority + port priority** choose which links are active vs hot-standby
  when more than 8 links exist (max 8 active).
- `lacp rate fast` sends LACPDUs every 1 s (default 30 s) for faster detection.

## Exam cues
- BPDU Guard = BPDU arrives → err-disable; Loop Guard = BPDU disappears → block;
  Root Guard = superior BPDU → root-inconsistent.
- EtherChannel balances per-flow; fix skew with a richer hash, not more VLANs.
- MST region = same name + revision + VLAN-to-instance map.
