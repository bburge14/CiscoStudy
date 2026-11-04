# NTP, SNMP, Syslog & QoS

This lesson gathers the tools that keep a network observable and well-behaved:
keeping clocks in sync, collecting log messages, monitoring devices, and making
sure important traffic gets through first. They're separate topics, so we'll take
them one at a time.

## NTP: keeping every clock in sync

Imagine trying to piece together what went wrong from the logs of three devices,
but each one thinks it's a different time. You'd never line the events up. That's
why network devices sync their clocks using NTP (Network Time Protocol), which runs
over UDP port 123. Accurate, matching time is needed for logs to make sense, for
certificates to validate, and for troubleshooting in general.

NTP describes how far a device is from the true source of time using a number
called stratum — and the smaller the number, the closer to the original and the
more trustworthy the time. Picture a photocopy of a photocopy: each copy is one
step further from the crisp original. Stratum 0 is the reference clock itself (an
atomic clock or GPS). A device attached directly to it is stratum 1. Every hop
away from there adds one to the number.

> **Lower stratum means closer to the real source of time, which means more
> authoritative.**

```
ntp server 10.1.1.1
ntp server 10.1.1.2 prefer
show ntp status            ! shows sync state + stratum
show ntp associations
```
You can list more than one server; the `prefer` keyword marks the one to use when
more than one is reachable.

## Syslog: log messages, sorted by how bad they are

Devices produce a constant stream of log messages, and Syslog tags each one with a
severity from 0 to 7. The thing to burn into memory is that lower numbers are more
severe — 0 is a five-alarm fire, 7 is harmless chatter. From most to least serious
they run 0 Emergency, 1 Alert, 2 Critical, 3 Error, 4 Warning, 5 Notice, 6
Informational, and 7 Debugging. The time-honored way to remember the order is the
sentence "Every Awesome Cisco Engineer Will Need Ice-cream Daily" — the first
letter of each word lines up with each level in turn.

When you tell a device which level to send, it sends that level and everything
numerically below it — that is, everything more severe. So this configuration:
```
logging host 10.1.1.9
logging trap 4             ! send levels 0-4 (warning and more severe) to the server
```
sends levels 0 through 4 — warnings and everything worse — to the log server at
`10.1.1.9`, while quietly dropping the chattier notice, informational, and
debugging messages.

## SNMP: monitoring your devices

SNMP (Simple Network Management Protocol) is how a monitoring station keeps an eye
on your gear, polling devices to ask how they're doing. The catch is security.
Versions 1 and 2c protect access with community strings, which are basically
passwords sent in clear text with no encryption — anyone watching the wire can read
them, like a password written on a postcard. Version 3 fixes this by adding
security levels you can dial up: `noAuthNoPriv` has no authentication and no
encryption, `authNoPriv` adds authentication only, and `authPriv` adds both
authentication and encryption. For anything real, use `authPriv`.

SNMP devices can also send alerts on their own, and there are two kinds. A trap is
fire-and-forget: the device sends it and never checks whether it arrived, so it can
be lost — like firing a flare and hoping someone's looking. An inform is
acknowledged and retransmitted until it's confirmed, so it's reliable but heavier,
more like sending certified mail. Both traps and informs travel over UDP port 162.

## QoS: letting the important traffic go first

When a link gets congested, something has to give — and you'd much rather drop a
background download than chop up a phone call. QoS (Quality of Service) is the set
of tools that decides who goes first. Think of priority boarding at an airport:
everyone gets on eventually, but some passengers board ahead of the queue.

The first step is classification and marking: you identify what kind of traffic a
packet is and stamp a value on it so every device down the line treats it the same
way. You can mark at Layer 2 (a field called CoS) or at Layer 3 (a field called
DSCP), and the rule of thumb is to mark as close to the source as possible, so the
tag is trusted everywhere after. A few DSCP values come up again and again: EF
(value 46) is voice media and rides the priority queue, CS3 (24) is call
signaling, the AF4x family is video, CS1 (8) is "scavenger" traffic you'd sacrifice
first, and 0 is plain best-effort with no special treatment.

Once traffic is marked, three more ideas handle it. Queuing is the scheduling that
kicks in during congestion — for example LLQ (Low Latency Queuing), a strict
priority queue used for voice so it never waits. Policing and shaping both deal
with traffic that exceeds a limit, but differently: policing drops or re-marks the
excess immediately with no delay, while shaping buffers the excess and sends it
later, which smooths the flow but adds delay and is used outbound. Finally,
congestion avoidance — the main example is WRED (Weighted Random Early Detection) —
drops a few packets selectively before the queue is completely full, to keep it
from overflowing all at once.

## The whole thing in one paragraph

These four tools keep a network observable and orderly. NTP (UDP 123) syncs every
clock to a common source, where a lower stratum means closer to the real reference
and more trustworthy. Syslog tags messages 0 through 7 where lower is more severe,
and asking for a level gives you that level and everything worse. SNMP monitors
devices — stick to v3 `authPriv` for real authentication and encryption, and prefer
informs over traps when you need the alert to actually arrive (both on UDP 162).
And QoS classifies and marks traffic near its source (DSCP at Layer 3, with EF/46
for voice), then uses queuing, policing or shaping, and congestion avoidance to
make sure the traffic that matters gets through when the link is full.

### See it on a real device
```
show ntp status
show logging
show policy-map interface g0/0
```
