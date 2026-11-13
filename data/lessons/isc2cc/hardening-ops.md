# System Hardening & Operational Security Policies

Security operations is the day-to-day discipline of keeping systems safe after
they're built. Two habits anchor it: **hardening** each system so there's less for
an attacker to grab, and following the **operational policies** that keep the
organization consistent and accountable. This lesson covers both.

## System hardening

> **Hardening** is the process of reducing a system's **attack surface** by
> removing or disabling everything it doesn't need — unnecessary services,
> accounts, software, and open ports.

The "attack surface" is the sum of all the ways an attacker could get in. Every
service you don't run and every account you disable is one less door to force.

### The core hardening steps

- **Change default credentials first.** New routers, servers, and devices ship
  with widely published default admin usernames and passwords. Changing them to a
  strong, unique password is the very first hardening step — a default password is
  an open invitation.
- **Disable unneeded services and close unused ports.** Turn off every network
  service and close every port the system's role doesn't actually require. This
  directly shrinks the attack surface by removing unnecessary entry points.
- **Remove or disable unnecessary accounts.** Default, guest, and former-employee
  accounts that aren't needed should be disabled or removed so they can't be used
  as entry points.
- **Apply the principle of least functionality.** Configure each system to provide
  **only** the applications, services, and capabilities required for its specific
  role — nothing extra. (This is the system-level sibling of least privilege.)

### Patch management

> **Patch management** is the practice of regularly applying the vendor's software
> updates to fix known security vulnerabilities.

Unpatched systems are one of the most common ways attackers get in, because the
vulnerabilities (and the exploits for them) are publicly known. But there's a
discipline to it:

> Before rolling a new patch out to all production servers, **test it in a non-
> production (test) environment first** to catch problems. A patch that breaks a
> critical system can cause an outage as damaging as the vulnerability it fixes.

Hardening and patching are ongoing, not one-time: systems drift and new
vulnerabilities appear, so you re-check and re-apply over the system's whole life.

## Operational security policies

Technology alone doesn't keep an organization secure — disciplined, documented
operations do. These are the common operational practices and policies the exam
expects you to recognize.

### Configuration management

> **Configuration management** maintains a documented, known-good inventory of
> every system's approved settings and tracks any deviation from it.

If you know exactly how a system *should* be configured, you can detect when
something changes without authorization — a sign of either a mistake or an
attacker. It's closely tied to hardening: the hardened configuration becomes the
baseline you manage against.

### Change management

> **Change management** is a formal process to review, approve, test, and document
> any modification to systems **before** it is implemented.

Many outages and security holes come not from attackers but from well-meaning
changes that break something. Change management reduces that risk by making sure
changes are reviewed, tested, documented, and reversible — never made on a whim.

### Logging and monitoring

> **Logging and monitoring** means collecting logs from systems and network
> devices and regularly **reviewing** them to spot suspicious activity and support
> later investigations.

Logs are only useful if someone looks at them. Good monitoring turns a pile of log
entries into early warning of an attack and provides the evidence needed to
investigate an incident afterward.

### Common written policies

Several specific policies come up by name:

- **Acceptable Use Policy (AUP)** — defines the rules for how employees may use
  company computers, email, and internet access, and what uses are prohibited.
- **Password policy** — specifies requirements such as minimum length, complexity,
  and how often passwords must be changed.
- **Data retention policy** — states how long records must be kept (e.g., financial
  records for seven years) and when they must be securely destroyed. Retention
  balances legal requirements against the risk of hoarding data.
- **Clean desk policy** — requires employees to lock their screens and lock away
  sensitive documents whenever they leave their desks, so passers-by can't read or
  take confidential information.

### How these fit together

Hardening sets a system up securely; **configuration management** keeps it that
way; **change management** governs how it's modified; **logging and monitoring**
watches for trouble; and the written policies (**AUP**, **password**,
**retention**, **clean desk**) set the human rules around it. It's defense in
depth applied to operations.

## Exam focus

- **Hardening** = shrink the **attack surface** by removing/disabling unneeded
  services, ports, accounts, and software. **Least functionality** = only what the
  role requires.
- **Change default credentials first** on any new device; **disable/remove**
  default, guest, and ex-employee accounts.
- **Patch management** = apply vendor updates to fix known flaws; **test patches
  in a non-production environment first**.
- **Configuration management** = maintain a known-good baseline and track
  deviations. **Change management** = review/approve/test/document changes before
  they happen.
- **Logging and monitoring** = collect *and review* logs to detect and investigate.
- Know the policies: **AUP** (acceptable use), **password policy** (length/
  complexity/rotation), **data retention** (how long to keep, then destroy),
  **clean desk** (secure your desk when away).
