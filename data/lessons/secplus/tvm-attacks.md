# Network & Application Attacks and Mitigations

This lesson is where threats turn into action. We'll walk through the attacks that
hit the network and the ones that hit applications, learn the **indicators** that
reveal them, and finish with the **mitigation techniques** that blunt them. The
exam phrases many of these as "you see X in the logs — what's happening, and what
do you do?"

## Network attacks

These target the wires, protocols, and services that move your data.

- **DDoS (Distributed Denial of Service)** — many compromised machines flood a
  target until it can't serve legitimate users. Two flavors to know:
  **amplified** (a small request triggers a huge response aimed at the victim) and
  **reflected** (the attacker spoofs the victim's address so responses bounce back
  to it). Both abuse third parties to multiply traffic.
- **DNS attacks** — poisoning or hijacking name resolution. **DNS poisoning**
  (cache poisoning) feeds a resolver false records so users are sent to attacker
  sites; **domain hijacking** steals control of the domain itself.
- **On-path attack** (formerly "man-in-the-middle") — the attacker secretly sits
  between two parties, reading or altering traffic while both think they're
  talking directly.
- **Credential replay** — capturing a valid credential or token and *replaying* it
  later to authenticate as the victim.
- **Wireless attacks** — rogue access points, evil twins, and deauthentication
  floods that knock clients off so they reconnect to the attacker.
- **Malicious code** — scripts or payloads delivered over the network to run on a
  target.

## Password attacks

Credentials are a constant target:

- **Brute force** — trying every possible combination until one works. Slow, and
  noisy (lots of failed logins).
- **Password spraying** — the clever inverse: try *one* common password against
  *many* accounts, staying under lockout thresholds so it's quiet.
- **Dictionary attack** — trying likely words and known-common passwords.

> **Brute force** hammers one account with many passwords (and trips lockouts).
> **Spraying** tries one password across many accounts to *avoid* lockouts. The
> direction of the attack is the whole distinction.

## Application attacks

These exploit flaws in software, often over the web:

- **Injection** — slipping commands into input, most famously **SQL injection**
  (database commands) and **cross-site scripting / XSS** (scripts that run in
  other users' browsers).
- **Buffer overflow** — overrunning a memory buffer to crash the app or run code.
- **Replay** — resending captured legitimate requests (e.g. a session token) to
  impersonate a user.
- **Privilege escalation** — turning low-level access into higher privileges;
  **vertical** (user → admin) or **horizontal** (one user → another user's data).
- **Forgery** — tricking a system or user into an unintended action. **CSRF**
  (Cross-Site Request Forgery) rides a logged-in user's session to perform actions
  they didn't intend; **SSRF** (Server-Side Request Forgery) tricks the *server*
  into making requests on the attacker's behalf.
- **Directory traversal** — using paths like `../../etc/passwd` to escape the web
  root and read files the app never meant to expose.

## Cryptographic attacks

- **Downgrade** — forcing a connection to use a weaker, older protocol or cipher
  that's easier to break (e.g. pushing TLS down to SSL).
- **Collision** — finding two different inputs that produce the *same* hash, which
  breaks the integrity guarantee. (Why MD5/SHA-1 are retired.)
- **Birthday attack** — the statistical trick that makes collisions far easier to
  find than intuition suggests, named after the "birthday paradox."

## Reading the room: indicators of malicious activity

Attacks leave fingerprints. Security+ expects you to recognize these
**indicators**:

| Indicator | What it often means |
|-----------|---------------------|
| **Account lockout** | Brute-force or spraying against that account |
| **Concurrent session usage** | A stolen credential used in two places |
| **Impossible travel** | Logins from two far-apart places minutes apart — stolen credentials |
| **Blocked content** | A control is catching something malicious |
| **Resource consumption** | Spikes in CPU/bandwidth — DDoS, crypto-mining, malware |
| **Resource inaccessibility** | A service is down — DoS or ransomware |
| **Out-of-cycle logging** | Log entries at odd times — tampering or automated attack |
| **Missing logs** | An attacker covering their tracks |
| **Published / documented** | The attack is a known, reported technique |

> **Impossible travel** is a favorite: the same account logs in from New York and
> then from overseas ten minutes later. No human can do that, so the credential is
> compromised.

## Mitigation techniques: how you push back

Knowing the attacks is half the job; the exam equally tests the **mitigations**.
These are the enterprise techniques to secure systems:

- **Segmentation** — divide the network so a breach in one zone can't spread.
  Limits an attacker's lateral movement.
- **Access control** — **ACLs** and **permissions** that enforce who can reach
  what.
- **Least privilege** — give every user and process only the access it needs,
  nothing more. Shrinks the blast radius of any compromise.
- **Application allow list** — only approved programs may run; everything else is
  blocked by default (stronger than a deny list).
- **Isolation** — quarantine a risky or infected system away from everything else.
- **Patching** — close known vulnerabilities before they're exploited. The single
  most effective routine defense.
- **Encryption** — protect data so that stealing it yields nothing usable.
- **Monitoring** — watch continuously so you *detect* what you couldn't prevent.
- **Configuration enforcement** — make systems conform to a secure baseline and
  stay there.
- **Decommissioning** — properly retire and wipe systems you no longer need, so
  they don't linger as forgotten attack surface.

### Hardening techniques

**Hardening** is the specific act of reducing a single system's attack surface:

- Install **endpoint protection** (antivirus/EDR).
- Enable a **host-based firewall** and **HIPS** (host intrusion prevention).
- **Disable unused ports and protocols**.
- **Change default passwords** immediately.
- **Remove unnecessary software** and services.
- Apply **encryption** (e.g. full-disk).

> The golden rule of hardening: **turn off, remove, or lock down everything you
> don't actively need.** Every service you don't run is a door that can't be
> kicked in.

## The whole thing in one paragraph

Network attacks include **DDoS** (amplified and reflected), **DNS** poisoning/
hijacking, **on-path** interception, **credential replay**, and **wireless**
attacks, while password attacks split into **brute force** (many passwords, one
account) and **spraying** (one password, many accounts). Application attacks cover
**injection** (SQLi, XSS), **buffer overflow**, **replay**, **privilege
escalation**, **forgery** (CSRF/SSRF), and **directory traversal**; cryptographic
attacks include **downgrade**, **collision**, and **birthday**. You detect all of
these through **indicators** like account lockouts, impossible travel, concurrent
sessions, resource spikes, and missing logs — and you push back with
**mitigations**: segmentation, access control, least privilege, allow lists,
isolation, patching, encryption, monitoring, configuration enforcement,
decommissioning, and system **hardening**.

## On the exam

- **Brute force vs. spraying:** many passwords against one account (lockouts) vs.
  one password across many accounts (avoids lockouts). Memorize the direction.
- **Amplified vs. reflected DDoS:** amplification = small request, huge response;
  reflection = spoofed source so replies hit the victim. Many attacks do both.
- **Impossible travel** and **concurrent session usage** both point to a
  **compromised credential**.
- **Allow list beats deny list**: an allow list blocks everything not explicitly
  approved, which is the stronger default.
- **Least privilege** and **segmentation** are the classic answers for "limit how
  far an attacker can spread."
- **Directory traversal** shows `../` sequences; **SQLi** shows `' OR 1=1--`-style
  input; **XSS** shows `<script>` in a field.
- When asked for the *most effective* routine mitigation for known
  vulnerabilities, **patching** is usually right.
