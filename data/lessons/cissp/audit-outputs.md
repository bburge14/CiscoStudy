# Audits, Log Reviews & Reporting Results

Testing produces raw findings; logs produce raw events. Neither protects anything
until it is reviewed, trusted, and turned into action that management can see. This
lesson covers the audit reports a CISSP relies on (especially the SOC family), the
discipline of audit logging, and — the part many candidates underweight — what to
*do* with test and audit results.

## Audits and who performs them

Audits are classified by who runs them, and independence drives their credibility.

- **Internal (first-party)** audit — the organization audits itself; useful for
  continuous improvement, but least independent.
- **External / second-party** audit — a partner or customer audits you (or you
  audit a vendor) under a business relationship.
- **Independent third-party** audit — an outside firm with no stake renders an
  opinion others can trust. This is what customers and regulators want.

## The SOC reports

When a service provider (think SaaS) must prove its controls to customers, it
commissions **SOC (System and Organization Controls)** reports, performed by CPAs
under **SSAE 18**. Know the three types and the two "flavors."

> **SOC 1** covers controls relevant to a customer's **financial reporting**
> (ICFR). **SOC 2** reports on the **Trust Services Criteria** —
> **security, availability, processing integrity, confidentiality, and privacy** —
> and is **detailed and restricted-distribution** (shared under NDA). **SOC 3** is a
> **public, general-use summary** of the SOC 2, with no sensitive detail.

The flavors:

- **Type I** — evaluates whether controls are **suitably designed** at a **single
  point in time**.
- **Type II** — evaluates whether controls **operated effectively** over a **period**
  (typically 6–12 months). Type II is stronger because it proves the controls
  actually worked over time.

> Exam cue: a provider needs to give enterprise customers a **detailed, restricted**
> report on **security/availability/confidentiality** controls → **SOC 2**
> (Type II for operating effectiveness). A **public** marketing-grade attestation →
> **SOC 3**. **Financial** controls → **SOC 1**.

## Audit logging done right

Logs are the raw material of detection, investigation, and accountability — but
only if they are complete, trustworthy, and actually reviewed.

What to capture: authentication successes and failures, privilege use, access to
sensitive data, configuration changes, and administrative actions. Each entry needs
**who, what, when, where**.

Protecting log **integrity** is critical, because the first thing a capable attacker
does is erase their tracks:

- Send logs to a **centralized, write-once** store (a SIEM or dedicated log server)
  so local tampering doesn't destroy the record.
- Restrict who can modify or delete logs (separation of duties — admins shouldn't
  control the logs of their own actions).
- **Synchronize clocks with NTP** so events across systems can be correlated into a
  coherent timeline — without it, a cross-system investigation falls apart.

Other tested terms: a **clipping level** is a threshold that must be crossed before
an event is flagged (e.g., alert after N failed logins) to cut noise; **log
retention** must satisfy legal and investigative needs without hoarding
indefinitely. Logs should be **reviewed** — unread logs catch nothing, which is why
automated correlation and alerting matter.

## Turning results into action

This is where candidates lose points by picking a technical answer when the exam
wants a **management process** answer. Findings — from a pen test, an audit, or a
log review — are the *beginning* of the work.

> After testing reports high-risk findings, the MOST appropriate next step is to
> **prioritize and remediate by risk, then retest to confirm closure**, and report
> the results and residual risk to **management**. Results feed a risk-based,
> management-visible remediation cycle — not a filing cabinet.

Supporting practices and vocabulary:

- **Risk-based prioritization** — fix the findings that threaten the most valuable
  assets first; don't blindly chase every low-severity item.
- **Remediation tracking** — a **POA&M (Plan of Action and Milestones)** records
  each finding, owner, and due date so nothing is lost.
- **Retest / validate** — confirm the fix actually closed the gap; a finding isn't
  done until it's verified.
- **Metrics for management** — **KPIs (Key Performance Indicators)** show how well
  security is performing; **KRIs (Key Risk Indicators)** give early warning that
  risk is rising. Dashboards and periodic management reviews keep leadership
  engaged and accountable.
- Account **access reviews**, **backup verification**, and **DR test results** are
  all outputs that should roll up to management as evidence the program works.

The throughline: assessment exists to inform decisions. A technically perfect test
whose results no one acts on provides zero risk reduction.

## Certification vs attestation

Candidates confuse two ways an organization demonstrates assurance, and the exam
draws the line sharply.

- **Certification (e.g., ISO/IEC 27001)** — an accredited body certifies that the
  organization's information security management system (ISMS) **conforms to a
  standard**. It is effectively a pass/fail credential against defined
  requirements.
- **Attestation (e.g., SOC 2)** — an independent auditor expresses a professional
  **opinion** on whether specific controls are designed and operating effectively,
  delivered in a report for stakeholders.

Both build trust, but a certification says "we meet the standard," while an
attestation says "an independent auditor examined our controls and here is their
opinion."

## Exam focus

- Audits by independence: **internal (first-party)**, **external (second-party)**,
  **independent third-party** (most credible).
- **SOC 1 = financial** controls; **SOC 2 = Trust Services Criteria** (security,
  availability, processing integrity, confidentiality, privacy), **detailed and
  restricted**; **SOC 3 = public summary**. **Type I = design at a point in time**;
  **Type II = operating effectiveness over a period** (stronger).
- Protect log **integrity**: centralized **write-once** storage, restricted
  deletion, and **NTP time sync** for correlation. A **clipping level** is an
  alerting threshold; logs must actually be **reviewed**.
- After findings: **prioritize by risk → remediate → retest to confirm closure →
  report to management.** Track with a **POA&M**; measure with **KPIs/KRIs**.
- When answers compete, the exam usually wants the **management/process** step
  (prioritized remediation reported to leadership), not just a point fix.
- **Certification** (ISO 27001) says the ISMS **conforms to a standard**;
  **attestation** (SOC 2) is an **auditor's opinion** on control effectiveness.
