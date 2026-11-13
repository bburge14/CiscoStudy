# Security Monitoring & Physical/Environmental Controls

The last piece of protecting information assets has two faces. **Security
monitoring** is how an organization *detects* that something is wrong — the logs,
correlation, and alerts that turn raw events into awareness. **Physical and
environmental controls** protect the facilities and hardware that everything else
depends on. Both are heavily about *detective* and *protective* controls, and
both give the auditor concrete things to verify.

## Security monitoring

Monitoring is fundamentally a **detective** discipline — it finds events as or
after they happen so the organization can respond.

> Continuous review of security alerts and system logs to identify security events
> functions primarily as a **detective** control. It doesn't stop an attack by
> itself; it reveals one so responders can act.

### Logs are only as good as their integrity

Logs are the auditor's evidence and the investigator's timeline — but only if they
can be trusted.

> Before relying on system audit logs as evidence of user activity, the IS auditor
> must **first be satisfied that the logs are protected from unauthorized
> modification**, so their **integrity** can be trusted. A log that users (or
> administrators) could quietly edit proves nothing.

So the auditor checks that logs are write-protected, forwarded to a separate
secure store, and kept out of reach of the very people they record — the same
"independent custody of the audit trail" idea seen with operators and DBAs.

### Making sense of many logs: SIEM and synchronized time

Large environments generate overwhelming volumes of events from many sources. Two
capabilities make them usable.

> A **security information and event management (SIEM)** system **centrally
> collects, aggregates, and correlates** security event data from many sources,
> enabling monitoring, alerting, and investigation from one place.

> **Synchronized time** across systems — typically via **NTP** — lets log events
> from different devices be **accurately correlated and sequenced**. Without
> synchronized clocks, you cannot reliably reconstruct the order of events across
> systems during an investigation.

Rounding out monitoring: a **security operations center (SOC)** staffs the watch;
**alerting thresholds** and **use cases** reduce noise; and **continuous
monitoring** feeds ongoing assurance rather than point-in-time snapshots. The
auditor confirms that alerts are actually reviewed and acted upon — a SIEM nobody
watches is a false comfort.

## Physical access controls

If someone can walk up to a server, logical controls may not matter. Physical
security builds **layers of defense** around people and equipment:

- **Perimeter** — fences, gates, bollards, and lighting deter and delay intruders.
- **Entry controls** — badges and locks gate the doors and create an access log;
  **security guards** add human judgment; **CCTV** deters and records.
- **The access control vestibule (mantrap)** is the specific answer to one threat:

> A **vestibule/mantrap** — two interlocking doors where the second won't open
> until the first closes — is designed primarily to prevent **tailgating/
> piggybacking**, where an unauthorized person follows an authorized one through a
> door. It forces entry **one person at a time**.

The auditor looks for layered physical controls around sensitive areas (data
centers especially), logging of entry, and prompt revocation of physical access
when people leave — the physical twin of de-provisioning.

## Environmental controls

Computers are fussy about their surroundings. Environmental controls keep the
facility within the conditions equipment needs and protect it from fire, power
loss, and climate.

**Fire** detection and suppression is a favorite exam topic because water and
electronics don't mix:

> For a computer room, a **clean-agent (inert gas) suppression system** is most
> appropriate — it extinguishes fire **without the water damage** a sprinkler would
> inflict on electronic equipment. (Where water systems are used, a **pre-action**
> system reduces the risk of accidental discharge.)

**Power** must be clean and continuous:

> A **UPS (uninterruptible power supply)** provides **continuous short-term power
> during brief outages** and allows an **orderly shutdown** or a transfer to a
> **generator** for longer outages. The UPS bridges the gap; the generator
> sustains it.

**Climate** control protects hardware from heat and humidity extremes:

> **HVAC** must control **humidity** within a defined range: too **low** raises
> **static electricity (ESD)** that can damage components, while too **high** risks
> **condensation and corrosion**. Temperature must likewise be held in range to
> prevent overheating.

Finally, **water/flood detection** sensors (often under raised floors) warn of
leaks before they reach equipment. As with monitoring, these are the controls an
auditor can physically inspect and test — are the extinguishers charged, the UPS
batteries tested, the sensors functioning?

## Exam focus

- Log/alert **review is a detective control**; **verify log integrity (protection
  from modification) before relying on logs as evidence**.
- A **SIEM** centrally **collects and correlates** events; **synchronized time
  (NTP)** lets logs across systems be **correlated and sequenced**.
- A **vestibule/mantrap** prevents **tailgating/piggybacking** (one person at a
  time).
- Use **clean-agent (inert gas)** suppression in computer rooms to avoid water
  damage; a **UPS** gives short-term power and orderly shutdown, with a
  **generator** for longer outages.
- Keep **HVAC humidity in range**: too low = **static/ESD**, too high =
  **condensation/corrosion**.
