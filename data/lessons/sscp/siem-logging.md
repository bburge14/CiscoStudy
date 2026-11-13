# Logging & SIEM

Logs are the memory of your systems. Every login, connection, and file access can
leave a record, and those records are where you prove what happened, detect what's
happening, and reconstruct an incident after the fact. But raw logs scattered
across hundreds of machines are nearly useless. This lesson covers how to turn
them into security intelligence: sound logging practices, centralized collection,
and the **SIEM** that ties it all together.

## Events, alerts, and incidents

Precise vocabulary prevents fuzzy thinking. These three words are not
interchangeable:

> An **event** is any single observable occurrence in a system — a login, a
> connection, a file open. Most events are perfectly normal. An **alert** is a
> notification raised when something warrants attention. An **incident** is an
> event (or series of events) that actually harms, or threatens to harm, security.

A single failed login is an **event**. Fifty failed logins in a minute might
trigger an **alert**. A confirmed compromised account is an **incident**. Moving
left to right, the volume drops sharply and the significance rises — the whole job
of monitoring tooling is to promote the few meaningful events up that ladder while
filtering out the noise.

## Logging done right

What you log and how you protect it matters as much as that you log at all.

- **Log sources** are everywhere: operating systems, applications, firewalls,
  IDS/IPS, authentication servers, proxies, endpoints. Comprehensive coverage
  matters because attackers cross many systems.
- **Time synchronization** is essential. Without a common clock, you can't
  correlate events across systems or build a reliable timeline. Use **NTP
  (Network Time Protocol)** so every device shares the same time; this is a
  surprisingly common exam point.
- **Log integrity** must be protected. If an attacker can edit or delete logs,
  the evidence is worthless — this is exactly why logs should not stay only on
  the host that produced them.

> Hosts should **forward their logs to a centralized, access-restricted log
> server** so that an attacker who compromises a machine cannot simply erase the
> evidence of their intrusion. Centralization preserves both **integrity** (the
> attacker can't reach the copies) and **availability** (the logs survive the
> host). The classic protocol is **syslog**, typically on **UDP port 514**.

- **Retention** policy balances investigative value, storage cost, and legal or
  regulatory requirements (some regulations mandate keeping logs for a year or
  more). Keep logs long enough to investigate a breach that went undetected for
  months — but not forever.

## SIEM: making sense of it all

A handful of logs you can read by eye. Millions per day across hundreds of
sources, you cannot. A **SIEM (Security Information and Event Management)** system
is built for exactly this scale.

> A **SIEM** **aggregates** (collects logs from many sources), **normalizes**
> (converts them to a common format), and **correlates** (links related events
> across sources) to detect patterns and generate alerts for security analysts —
> all from a central console.

Its core functions, step by step:

| Function | What it does |
|----------|--------------|
| **Aggregation** | Pulls logs from across the environment into one place |
| **Normalization** | Reformats disparate logs into a consistent structure |
| **Correlation** | Applies rules to connect related events into a meaningful signal |
| **Alerting** | Notifies analysts when a correlation rule fires |
| **Dashboards & reporting** | Visualizes posture and supports compliance reporting |
| **Retention** | Stores logs centrally for investigation and audit |

The power of a SIEM is **correlation**: no single log says "breach," but a failed
VPN login, a successful one from a new country, and a burst of file access —
stitched together — tell the story. That's the difference between having logs and
*understanding* them.

### SIEM's partner: SOAR

A SIEM detects; a **SOAR (Security Orchestration, Automation, and Response)**
platform *acts*. SOAR uses **playbooks** to automate responses — automatically
isolating a host, disabling an account, or opening a ticket — so analysts aren't
doing repetitive work by hand. Think of SIEM as the alarm system and SOAR as the
automated first responder. Modern operations increasingly fold SIEM and SOAR
together, and many add **UEBA** (behavioral analytics) on top for insider-threat
and anomaly detection.

## The practitioner's payoff

For an SSCP working a security operations center, logging and SIEM are the daily
reality. They provide the **detective** control that spots trouble, the
**forensic** record that reconstructs it, and the **compliance** evidence that
proves the organization is watching. Garbage in, garbage out applies: a SIEM is
only as good as the log sources feeding it and the correlation rules you tune. An
untuned SIEM drowns analysts in false positives; a well-tuned one is the nerve
center of detection.

## Exam focus

- Keep the ladder straight: **event** (any observable occurrence) -> **alert**
  (worth attention) -> **incident** (actual/threatened harm). A single failed
  login is an **event**.
- Forward logs to a **centralized, access-restricted log server** so a compromised
  host can't delete the evidence — this protects log **integrity** and
  **availability**. **Syslog** is commonly **UDP 514**.
- **Time synchronization via NTP** is required to correlate events and build an
  accurate timeline.
- A **SIEM** **aggregates, normalizes, and correlates** logs from many sources to
  detect and alert; **correlation** across sources is its key strength.
- **SOAR** automates response via **playbooks** (isolate host, disable account);
  SIEM detects, SOAR acts.
- **Retention** policy is driven by investigation needs and legal/regulatory
  requirements.
