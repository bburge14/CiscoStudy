# NTP, SNMP, Syslog & QoS

## NTP (Network Time Protocol)
Accurate, synchronized time is required for logs, certificates and
troubleshooting. NTP uses **UDP 123**. **Stratum** = distance from the reference
clock: stratum 0 is the reference (atomic/GPS), stratum 1 is directly attached,
and each hop adds one. **Lower stratum = more authoritative.**
```
ntp server 10.1.1.1
ntp server 10.1.1.2 prefer
show ntp status            ! shows sync state + stratum
show ntp associations
```

## Syslog severity levels
Messages carry a severity 0–7; **lower is more severe**. Setting a level logs
that level **and everything numerically below it**.

| # | Level | Mnemonic |
|--:|-------|----------|
| 0 | Emergency | **E**very |
| 1 | Alert | **A**wesome |
| 2 | Critical | **C**isco |
| 3 | Error | **E**ngineer |
| 4 | Warning | **W**ill |
| 5 | Notice | **N**eed |
| 6 | Informational | **I**ce-cream |
| 7 | Debugging | **D**aily |

```
logging host 10.1.1.9
logging trap 4             ! send levels 0-4 (warning and more severe) to the server
```

## SNMP
Polls/monitors devices. Versions:
- **v1 / v2c** — community strings in **clear text**; no encryption.
- **v3** — adds security **levels**:
  - `noAuthNoPriv` — no auth, no encryption
  - `authNoPriv` — authentication only
  - `authPriv` — **authentication + encryption** (use this)

**Traps vs informs:** a **trap** is fire-and-forget (can be lost); an **inform**
is acknowledged and retransmitted (reliable, heavier). Both use UDP 162.

## QoS concepts
- **Classification & marking** — identify traffic and set a value (CoS at L2,
  **DSCP** at L3). Mark as close to the source as possible.
- Key DSCP values: **EF (46)** voice media (priority queue), **CS3 (24)** call
  signaling, **AF4x** video, **CS1 (8)** scavenger, **0** best-effort.
- **Queuing** — scheduling at congestion (e.g., **LLQ** strict priority for voice).
- **Policing vs shaping** — policing drops/re-marks excess (no delay); shaping
  buffers excess (adds delay, outbound).
- **Congestion avoidance** — WRED drops selectively before the queue is full.

## Verify
```
show ntp status
show logging
show snmp user
show policy-map interface g0/0
```

## Exam cues
- Lower stratum and lower syslog number = more important.
- Need encryption of SNMP → v3 `priv` (authPriv).
- Reliable notification → **inform** (acknowledged), not trap.
- Voice = EF (46).
