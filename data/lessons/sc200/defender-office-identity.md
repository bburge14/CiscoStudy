# Defender for Office 365 & Defender for Identity

Two more workloads feed Microsoft Defender XDR, and both defend a channel
attackers love. **Microsoft Defender for Office 365** protects the collaboration
layer — email, Teams, SharePoint, and OneDrive — where phishing and malicious
attachments arrive. **Microsoft Defender for Identity** protects your on-premises
Active Directory, watching for the reconnaissance and lateral movement that turn a
single compromised account into domain-wide control. Their alerts land in the same
unified portal and correlate into shared incidents.

## Microsoft Defender for Office 365

Email is still the number-one delivery vehicle for attacks, so Defender for
Office 365 adds a layer of protection on top of the basic anti-spam and
anti-malware that Exchange Online Protection (EOP) already provides.

### The marquee protections

- **Safe Attachments** — before an attachment reaches the inbox, it is detonated
  in an isolated sandbox. If it behaves maliciously, it is stripped or the message
  is blocked. This catches *unknown* malware that signatures miss.
- **Safe Links** — rewrites URLs in mail (and in Teams and Office apps) so they are
  re-checked **at time of click**, not just at delivery. A link that was benign
  when the mail arrived but turns malicious later is still caught.
- **Anti-phishing policies** — use **mailbox intelligence** and impersonation
  protection to spot display-name and look-alike-domain spoofing of the people and
  domains you choose to protect.

> **Safe Attachments is about files; Safe Links is about URLs checked at click
> time.** Keep those two straight — the exam loves to swap them.

### Catch-up and cleanup

- **Zero-hour auto purge (ZAP)** retroactively removes mail that is found to be
  malicious or spam *after* it was already delivered, pulling it out of the inbox.
- **Threat Explorer** (Explorer) lets analysts hunt across email: search by sender,
  URL, or payload, see what was delivered, and take actions such as soft-delete or
  move to junk.
- **Attack simulation training** runs benign, controlled phishing campaigns against
  your own users and assigns training to those who fall for them.

Defender for Office 365 comes in **Plan 1** (the real-time protections — Safe
Attachments, Safe Links, anti-phishing) and **Plan 2** (adds the investigation and
hunting tooling — Threat Explorer, automated investigation and response, and attack
simulation training). **Preset security policies** (Standard and Strict) let you
apply Microsoft's recommended settings quickly instead of hand-tuning each policy.

### Quarantine and submissions

Messages blocked as malware, phishing, or high-confidence spam are held in
**quarantine**, where admins (and, within policy, users) can review and release
them. When something is misclassified, the **Submissions** portal is how you report
it to Microsoft — submit a missed phish (false negative) or a wrongly blocked
message (false positive) so Microsoft can tune its verdicts, and optionally create
a matching **tenant allow/block list** entry. On Plan 2, **automated investigation
and response** can kick off from an email alert and propose remediation such as
soft-deleting every copy of a malicious message across mailboxes.

## Microsoft Defender for Identity

Where Office 365 guards the inbox, Defender for Identity (MDI) guards the identity
fabric. It installs a lightweight **sensor** on your **domain controllers** (and
on AD FS, AD CS, and Entra Connect servers) and analyzes the authentication and
directory traffic flowing through them.

> MDI builds a behavioral baseline of users, devices, and resources, then flags
> deviations that map to the stages of an identity attack. Its alerts surface in
> the Microsoft Defender portal alongside endpoint and email signals.

### The kill-chain MDI watches for

MDI organizes its detections around the phases of a domain compromise:

- **Reconnaissance and discovery** — account, group, and resource enumeration
  (for example LDAP or SAMR queries mapping out the directory).
- **Compromised credentials** — brute force, suspected password spray, and
  abnormal sign-in behavior.
- **Lateral movement** — pass-the-hash, pass-the-ticket, and overpass-the-hash as
  an attacker hops between machines.
- **Domain dominance** — the end-game techniques: suspected **DCSync**,
  **golden ticket**, skeleton key, and malicious directory replication that give
  an attacker lasting control.

### Hardening the identity surface

Beyond detections, MDI contributes **identity security posture assessments** —
recommendations such as removing unconstrained Kerberos delegation, cleaning up
dormant privileged accounts, or fixing legacy protocols. A neat trick is the
**honeytoken account**: a decoy account that no legitimate user should ever touch,
so any authentication involving it is immediate evidence of snooping.

## How they reinforce each other

A realistic intrusion crosses both workloads. A user clicks a phishing link that
Safe Links missed because it was weaponized post-delivery; the endpoint runs the
payload (MDE); the attacker steals credentials and starts enumerating Active
Directory (MDI). Because all three report to Microsoft Defender XDR, these
separate alerts **correlate into a single incident** with one shared timeline,
rather than three disconnected tickets — the whole point of the XDR model.

## Exam focus

- **Safe Attachments** sandboxes/detonates *files*; **Safe Links** re-checks
  *URLs at time of click* (and covers Teams/Office apps). Don't confuse them.
- **Zero-hour auto purge (ZAP)** removes bad mail *after* delivery; **Threat
  Explorer** is the hunt-and-act surface; **Attack simulation training** phishes
  your own users for awareness.
- Defender for Office 365 **Plan 1** = protection; **Plan 2** = investigation,
  hunting, AIR, and attack simulation. **Preset policies** (Standard/Strict) apply
  Microsoft's recommended baselines.
- **Defender for Identity** sensors run on **domain controllers** (and AD FS, AD
  CS, Entra Connect) and detect **recon → compromised credentials → lateral
  movement → domain dominance** (DCSync, golden ticket, pass-the-hash/ticket).
- A **honeytoken account** is a decoy; any activity on it signals an intruder.
  **Identity security posture assessments** are proactive hardening recommendations.
- The payoff of the suite: endpoint, email, and identity alerts **correlate into
  one Defender XDR incident**.
