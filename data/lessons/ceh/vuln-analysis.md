# Vulnerability Analysis

Scanning and enumeration tell you what is running. **Vulnerability analysis** asks
the next question: which of those things are *weak*, how bad is each weakness, and
what do you fix first? This is the bridge between discovery and action. It is also
where a lot of exam vocabulary lives — CVE, CVSS, and the names of the scanners —
so this lesson is about speaking that language precisely.

## The vocabulary of weakness

People use these four words loosely; the exam does not.

> A **vulnerability** is a weakness. A **threat** is something that could exploit
> it. An **exploit** is the actual code or technique that takes advantage of it.
> **Risk** is the combination of likelihood and impact if it happens.

A vulnerability with no threat and no exploit is still worth fixing, but risk is
what drives *priority*. Vulnerability analysis produces the raw material — a list
of weaknesses with severities — that risk decisions are built on.

### How weaknesses are catalogued

- **CVE (Common Vulnerabilities and Exposures)** — a unique ID for a *specific*
  publicly known vulnerability (for example, a flaw in one product version).
- **CWE (Common Weakness Enumeration)** — a catalogue of weakness *types* (such as
  "improper input validation") that CVEs are instances of.
- **NVD (National Vulnerability Database)** — the U.S. government feed that enriches
  CVEs with scores and references.
- **CPE** — a naming scheme for products, so a scanner can match "this software" to
  "these CVEs."

## CVSS: scoring severity

> **CVSS (Common Vulnerability Scoring System) produces a numeric severity rating
> from 0.0 to 10.0, so teams can prioritize which vulnerabilities to remediate
> first.** It measures severity — not your business risk directly.

The qualitative bands are the same across the current versions:

| Score | Rating |
|-------|--------|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

CVSS **v3.1** organizes metrics into **Base**, **Temporal** and **Environmental**
groups; the Base score covers things like attack vector, attack complexity,
privileges required, user interaction, scope and the impact to confidentiality,
integrity and availability. The newer **CVSS v4.0** (published by FIRST in late
2023) refines this and renames the scoring nomenclature to **CVSS-B / BT / BE /
BTE** (Base, plus Threat and Environmental combinations). Either way, a higher
number means a more severe flaw — and remediation starts at the top.

## The scanners (by name and role)

Vulnerability scanners compare what they find against a database of known flaws and
output a **prioritized findings report**. They *identify* weaknesses; they are not
exploitation frameworks.

- **Nessus** — a widely used commercial scanner that reports and ranks findings.
- **OpenVAS / Greenbone** — an open-source scanner in the same role.
- **Qualys** and **Rapid7 Nexpose / InsightVM** — enterprise scanning platforms.
- **Nikto** — focused specifically on *web server* misconfigurations and known
  issues.

> A scanner that "scans hosts against a database of known flaws and outputs a
> prioritized report, but is not itself an exploitation framework" is describing a
> vulnerability scanner such as **Nessus**.

### Scan choices that change results

- **Authenticated (credentialed) scans** log in to the host and see far more
  (missing patches, local config) than **unauthenticated** network-only scans.
- **Agent-based** scans run software on the host; **network-based** scans probe
  from across the network.
- Scanners produce **false positives** (reported but not real) and **false
  negatives** (real but missed), so results need human validation.

## The vulnerability management lifecycle

Analysis is one step in a loop that never really ends:

1. **Discover / identify** — inventory assets and scan them.
2. **Assess and prioritize** — apply CVSS plus business context.
3. **Remediate** — patch, reconfigure, or compensate with another control.
4. **Verify** — re-scan to confirm the fix actually worked.
5. **Report** — communicate status and trends to stakeholders.

The defensive payoff is a disciplined **patch management** and **hardening**
program driven by evidence, plus the re-scan that proves a remediation closed the
hole instead of just filing a ticket.

## Prioritizing beyond the raw score

A CVSS score measures *severity in the abstract*; it does not know your environment
or whether anyone is actually exploiting the flaw. Mature programs layer two more
signals on top:

- **EPSS (Exploit Prediction Scoring System)** — estimates the probability a
  vulnerability will be exploited in the near term, so you can focus on the flaws
  attackers actually use.
- **CISA KEV (Known Exploited Vulnerabilities) catalog** — a list of vulnerabilities
  with confirmed real-world exploitation; anything on it is a drop-everything fix.

Combine those with **business context** — is the asset Internet-facing? does it hold
regulated data? — and you move from "patch everything, impossibly" to "patch what
matters first."

## Exam focus

- **CVSS** = a **0.0–10.0** numeric severity score used to **prioritize**
  remediation. Know the bands (Critical 9.0–10.0, High 7.0–8.9, Medium 4.0–6.9,
  Low 0.1–3.9, None 0.0) and that **v4.0** is the current version (v3.1 still
  widely used).
- **CVE** = one specific named vulnerability; **CWE** = a weakness *type*; **NVD**
  is the database that scores CVEs.
- **Nessus / OpenVAS / Qualys** *identify and rank* vulnerabilities; they are
  **scanners, not exploitation frameworks**. **Nikto** targets web servers.
- **Authenticated (credentialed)** scans find more than unauthenticated ones.
- Watch for **false positives vs false negatives** and the need to validate.
- The lifecycle is **identify → prioritize → remediate → verify (re-scan) →
  report**, feeding patch management and hardening.
