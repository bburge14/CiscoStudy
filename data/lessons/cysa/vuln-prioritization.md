# Prioritizing Vulnerabilities: CVSS, EPSS & KEV

A scan can return hundreds of findings; your team can fix only a handful this
week. Prioritization is the skill that decides *which* ones — and on CySA+ it is
tested in detail, especially the mechanics of CVSS. This lesson teaches you to
read a CVSS vector, read the severity it produces, and then temper it with the
real-world signals (EPSS, KEV, asset value) that CVSS alone ignores.

## CVSS v3.1: the base metric groups

The **Common Vulnerability Scoring System (CVSS) v3.1** base score, 0.0–10.0, is
built from two metric groups. CySA+ tests version **3.1**, so learn it precisely.

> The **Exploitability** metrics describe *how hard the flaw is to reach and
> trigger*; the **Impact** metrics describe *what you lose if it's triggered*.

### Exploitability metrics

| Metric | Values | Which value *raises* the score |
|--------|--------|-------------------------------|
| **Attack Vector (AV)** | Network / Adjacent / Local / Physical | **Network** (remotely reachable) |
| **Attack Complexity (AC)** | Low / High | **Low** (no special conditions) |
| **Privileges Required (PR)** | None / Low / High | **None** |
| **User Interaction (UI)** | None / Required | **None** |
| **Scope (S)** | Unchanged / Changed | **Changed** |

Read those "which value raises the score" entries as a checklist of worst cases:
a vulnerability that is reachable over the **Network**, needs **Low** complexity,
**No** privileges, and **No** user interaction is about as easy to exploit as it
gets.

- **Attack Vector** separates a flaw exploitable remotely across the internet
  (AV:Network, higher score) from one needing local console access (AV:Local).
- **Attack Complexity: Low** means no special conditions — which *raises* the
  score relative to a flaw that works only if the attacker first wins a timing
  race (AC:High).
- **User Interaction: Required** (the victim must open a malicious document)
  *lowers* the score relative to UI:None.
- **Scope: Changed** means the impact escapes the vulnerable component's own
  security authority — a hypervisor guest breaking out to affect the host and
  other VMs is the textbook example, and it *raises* the score.

### Impact metrics

Each of **Confidentiality**, **Integrity**, and **Availability** is rated None /
Low / High. A flaw that lets an attacker read every record in a customer database
but not alter data or cause downtime scores **High on Confidentiality**, None on
the others.

## Reading the severity

The numeric base score maps to a qualitative rating — memorize the bands:

| Score | Severity |
|-------|----------|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | **Critical** |

So a published CVSS v3.1 base score of **9.8** is **Critical**.

## Beyond the base: Temporal and Environmental

The base score is deliberately *static*. Two more groups adjust it:

- **Temporal** metrics move the score over time as the real-world situation
  changes — **Exploit Code Maturity** (a working, weaponized exploit becomes
  public → score rises) and **Remediation Level** (a vendor patch ships → score
  falls), plus Report Confidence.
- **Environmental** metrics tailor the score to *your* organization — modified
  base values plus Confidentiality/Integrity/Availability **requirements** that
  reflect **asset criticality and data sensitivity**. Two hosts with an identical
  base score of 7.5 are not equal if one is an empty sandbox and the other stores
  regulated financial records; environmental context is how you capture that.

## Signals CVSS doesn't carry

CVSS measures *severity*, not *likelihood of attack*. Modern prioritization adds:

> **EPSS (Exploit Prediction Scoring System)** estimates the **probability** that
> a vulnerability will be exploited in the wild (in the near term). **CISA's KEV
> (Known Exploited Vulnerabilities) catalog** lists vulnerabilities **known to be
> actively exploited right now**.

- When two vulns share a base score but you can patch only one first, **EPSS**
  estimates which is more likely to be exploited.
- **KEV** is a priority flag you cannot ignore: an internet-facing server whose
  vuln is in the KEV catalog (even at CVSS 7.5) outranks an isolated internal host
  with an unexploited 9.0, because *active exploitation plus exposure* is real-world
  risk, not theoretical severity.
- A **zero-day** — exploited before a patch exists — jumps the queue for the same
  reason: there is no vendor fix and attackers already have the advantage.

The durable rule: **prioritize by real-world risk**, which blends CVSS severity,
EPSS/KEV exploitation signals, exposure, and **asset criticality** — not by raw
CVSS score alone.

### One more trap: false negatives

Prioritization assumes your findings are real. A scan that reports a server as
**clean** while it actually runs an exploitable, unpatched service is a **false
negative** — the most dangerous result, because a genuine vulnerability goes
undetected and therefore unprioritized and unfixed.

## A note on currency: CVSS v4.0

FIRST released **CVSS v4.0** in November 2023. CySA+ (CS0-003) still assesses
**v3.1**, so that is what you score on the exam, but be aware v4.0 **retired the
Scope metric**, added finer-grained metrics (including a more granular Attack
Requirements/User Interaction model and separate impact on the Vulnerable vs.
Subsequent System), and introduced the **CVSS-B / BT / BE / BTE** nomenclature to
show which metric groups a given score includes. If a question specifies v3.1,
answer with the v3.1 model above.

## Exam focus

- CVSS v3.1 base = **Exploitability** (AV, AC, PR, UI, Scope) + **Impact** (C, I,
  A). Values that **raise** the base score: **AV:Network, AC:Low, PR:None,
  UI:None, Scope:Changed**, and higher C/I/A.
- **Scope:Changed** = impact escapes the component's authority (hypervisor
  guest-to-host breakout). **UI:Required** and **AC:High** *lower* the score.
- Severity bands: 0.1–3.9 **Low**, 4.0–6.9 **Medium**, 7.0–8.9 **High**, 9.0–10.0
  **Critical** (so 9.8 = Critical).
- **Temporal** adjusts for exploit maturity and patch availability;
  **Environmental** adjusts for **asset criticality / data sensitivity** — the tie-breaker
  between two equal base scores.
- **EPSS** = probability of exploitation; **KEV** = actively exploited now. An
  **internet-facing KEV** vuln outranks an isolated internal higher-CVSS one.
- A **false negative** (missed real vuln) is the worst scan error.
- CySA+ scores **v3.1**; know that **v4.0** (2023) dropped **Scope** as a currency note.
