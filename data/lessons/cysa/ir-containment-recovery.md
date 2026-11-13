# Containment, Eradication & Recovery

Once an incident is confirmed and scoped, the mission shifts from *understanding*
to *acting*: stop the spread, remove the threat completely, and get the business
safely back to normal — in that order, and without destroying the evidence or the
lessons. This lesson walks the third NIST phase, where good judgment under
pressure separates a contained incident from a repeat breach.

## Containment: stop the bleeding

> **Containment** limits the damage of an active incident. Disconnecting an
> actively infected, spreading workstation from the network to stop the spread is
> a containment action.

Containment is rarely all-or-nothing. CySA+ wants you to pick the *right* level
and method for the situation:

- **Short-term containment** is the quick isolation you do *first* — stop the
  damage now, preserve evidence, and plan a fuller fix later.
- **Segmentation** contains malware spreading across a *flat* network **without
  taking critical servers fully offline** — you isolate the affected systems
  rather than pulling the plug on everything.
- **Isolate but keep powered on** when the host holds important **volatile
  evidence**: move it to a **quarantine VLAN** so you cut the attacker's access
  while the RAM-resident evidence survives for forensics. (Recall the order of
  volatility — don't power off and lose memory.)
- **DNS sinkholing** cuts command-and-control without immediately taking infected
  endpoints offline: redirect the known malicious **C2 domains** to a controlled
  address so beacons go nowhere.

The theme: contain *surgically*. Preserve evidence, protect uptime where you can,
and don't tip off the attacker by over-reacting.

## Eradication: remove every trace

> **Eradication** removes the threat: delete the malware, remove attacker-created
> accounts, and patch the exploited vulnerability so it can't be used again.

- **When in doubt, rebuild.** A host compromised by a **kernel-level rootkit**
  can't be trusted after a "clean" — the most reliable eradication is to **wipe
  and reimage from a known-good baseline**. You can never fully trust a system
  whose kernel the attacker owned.
- **Revoke stolen access.** When an attacker has stolen domain and service-account
  credentials, removing malware isn't enough — you must **invalidate active
  sessions and tokens**, and where domain-wide compromise is suspected, **reset
  the Kerberos `krbtgt` account** to break forged tickets. Credentials the attacker
  holds are a door that stays open until you change the locks.

## Recovery: back to normal, carefully

> **Recovery** restores systems to normal operation — from clean backups — and
> **closely monitors them for reinfection** before declaring business as usual.

Recovery is where impatience causes relapses. Three rules:

- **Fix the root cause first.** Restoring a system *without* patching the exploited
  vulnerability invites immediate reinfection — before reconnecting a rebuilt
  server to production, **confirm the exploited vulnerability is patched and the
  system is clean**.
- **Choose the backup carefully.** If the compromise is estimated to have occurred
  three weeks ago, restore from a **verified-clean backup taken *before* that date**,
  after confirming it is free of attacker artifacts. A backup taken *after* the
  intrusion may already contain the attacker's foothold.
- **Monitor before you declare victory.** Watch recovered systems closely for signs
  the threat returns. Declaring "normal operations" too early, while an attacker
  still has a toehold, restarts the whole incident.

## Returning to operations

Recovery isn't a single switch; it's a controlled return. A few practices
separate a clean return-to-operations from a premature one:

- **Define exit criteria up front.** Decide *in advance* what "clean" means — no
  attacker artifacts, root cause patched, credentials rotated — so the decision to
  reconnect is based on evidence, not optimism.
- **Reconnect in stages.** Bring systems back gradually rather than all at once, so
  if something was missed the blast radius stays small.
- **Harden against the same vector.** Recovery is the natural moment to close the
  door the attacker used — tighten the exploited configuration, add the detection
  that would have caught the intrusion sooner, and strengthen monitoring on the
  rebuilt hosts.
- **Elevate monitoring.** Keep enhanced logging and alerting on recovered systems
  for a defined period; an attacker who retained *any* foothold will often try to
  return, and heightened watch is how you catch the second attempt early.

> The order is deliberate: *restore from clean backups → validate against exit
> criteria → reconnect in stages → monitor closely*. Rushing any step reopens the
> incident you just closed.

## After recovery: learn from it

Containment and recovery close the operational emergency, but the incident isn't
truly "done" until you capture why it happened:

- **Root-cause analysis** identifies the underlying entry point (for example, an
  unpatched VPN appliance) so the same weakness can't be exploited again.
- A **lessons-learned meeting** and an **after-action report** record what worked
  and what didn't; the team then **updates its IR playbooks and response plan** so
  the next response is faster and smoother. The goal is always to **improve future
  response and prevent recurrence**, never to assign blame.

## Putting the phase together

A clean run reads like this: network-isolate the infected host to a quarantine
VLAN (contain while preserving memory), sinkhole its C2 so it goes quiet, wipe and
reimage from a trusted baseline and reset the compromised credentials (eradicate),
then restore remaining systems from a verified-clean pre-compromise backup, patch
the root cause, and watch closely before calling it normal (recover) — and finally
write it all up so the organization is stronger next time.

## Exam focus

- **Containment** stops active spread. **Short-term containment** = quick
  isolation first; **segmentation** isolates without downing critical servers;
  **quarantine-VLAN isolation (powered on)** preserves volatile evidence; **DNS
  sinkholing** kills C2 without pulling endpoints offline.
- **Eradication** = remove malware, delete attacker accounts, patch the exploited
  flaw. A **kernel rootkit** demands **wipe and reimage from a known-good
  baseline**. Stolen creds → **invalidate sessions/tokens** and **reset `krbtgt`**
  for domain-wide compromise.
- **Recovery** = restore from **clean backups** and **monitor for reinfection**.
  **Fix the root cause before restoring** or you'll be reinfected; pick a
  **verified-clean backup from before the compromise date**.
- Finish with **root-cause analysis**, a **lessons-learned / after-action report**,
  and **updated playbooks** to **prevent recurrence**.
