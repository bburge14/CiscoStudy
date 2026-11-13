# Fieldwork: Testing Controls, Evidence & Sampling

Planning tells you *where* to look. Fieldwork is where you actually look — you
test controls, gather evidence, and draw conclusions you can defend. This is the
heart of the audit, and it is where the auditor's discipline about *reliable
evidence* and *representative samples* earns the opinion its credibility.

## Control types: the auditor's vocabulary

Every control an auditor examines can be classified by *when* and *how* it acts.
CISA questions constantly ask you to name the type.

> - A **preventive** control stops an incident *before* it happens (a firewall,
>   an input edit check, segregation of duties, a locked door).
> - A **detective** control finds an incident *after* it occurs (log review,
>   reconciliations, an intrusion detection system, exception reports).
> - A **corrective** control fixes or reverses the damage once an incident is
>   found (restoring from backup, a business continuity plan, patching).

Three more types round out the set:

- **Deterrent** — discourages an actor from even trying (warning banners, visible
  cameras, "under surveillance" signage).
- **Compensating** — an alternative control used when the preferred one is not
  practical (extra supervision and log review where full segregation of duties
  is impossible).
- **Directive** — directs behavior toward compliance (policies, procedures,
  mandates).

A clean test: *reconciling audit logs each week to spot unauthorized changes
after they occur* is **detective** — it finds things after the fact. The same
action done to *block* a change in real time would be preventive.

## Compliance vs. substantive testing

Auditors run two broad kinds of tests, and knowing which is which keeps answers
straight.

> A **compliance test** checks whether a **control** is operating as intended
> (e.g., did every purchase order get the required approval?). A **substantive
> test** checks the **data or balances themselves** for accuracy and
> completeness (e.g., recomputing a total, confirming a balance).

If compliance testing shows controls are strong and reliable, the auditor can
reduce — though never entirely eliminate — substantive testing. Weak controls
push the auditor toward more substantive work.

### Control self-assessment (CSA)

> In a **control self-assessment**, the **business process owners assess their
> own controls**, and the IS auditor acts as a **facilitator** — guiding the
> workshop, not owning the controls or the conclusions.

CSA spreads control awareness into the business and surfaces issues early. But it
does not replace independent audit: the owners are assessing themselves, so the
auditor's independent testing still matters.

### Computer-assisted audit techniques (CAATs)

> **CAATs** let the auditor analyze **entire populations** of data efficiently
> and independently, rather than relying on a small manual sample.

When an auditor wants to test *every* transaction in a large payment file — re-
performing calculations, finding duplicates, or flagging exceptions across
millions of rows — CAATs are the answer. Their value is full-population analysis
done independently of the auditee's own tools.

## Audit evidence and its reliability

A finding is only as strong as the evidence behind it. Not all evidence is equal.

> Evidence is **more reliable** when it is: obtained **directly by the auditor**
> rather than supplied by the auditee; from an **independent, external** source
> rather than internal; **written/original** rather than oral or copied; and
> produced under **strong controls** rather than weak ones.

So a confirmation the auditor obtains *directly from an independent external
party* outranks a photocopy handed over by the department under review. When you
compare evidence options, rank them on those dimensions and pick the most
independent, auditor-obtained, original item.

The auditor also prefers **sufficient** (enough) and **relevant** (bearing on
the objective) evidence, and documents it so another competent auditor could
follow the trail — these working papers support the eventual report.

## Sampling: testing a slice, concluding about the whole

Auditors rarely test 100% of a population by hand (that is what CAATs are for).
Instead they examine a **sample** and infer a conclusion about the whole. The
method must fit the question being asked.

| Sampling type | Use it to… | Typical pairing |
|---------------|-----------|-----------------|
| **Attribute sampling** | Estimate the **rate of occurrence** of a condition (did the control happen or not?) | **Compliance** testing |
| **Variable sampling** | Estimate a **numeric amount or value** (how much?) | **Substantive** testing |

> **Attribute sampling** answers *how often* — it tests the presence or absence
> of a control, such as whether a required approval was performed. **Variable
> sampling** answers *how much* — it estimates monetary or quantitative amounts.

Two more distinctions worth knowing:

- **Statistical sampling** uses probability so results can be projected to the
  population with a measurable confidence level; **non-statistical (judgmental)
  sampling** relies on the auditor's judgment and cannot be projected
  statistically.
- **Stop-or-go** and **discovery** sampling are specialized attribute methods;
  discovery sampling aims to find at least one instance of a critical
  (often fraud-related) condition.

### Sampling risk

> **Sampling risk** is the risk that the auditor's conclusion from the **sample**
> differs from the conclusion that testing the **entire population** would have
> reached — the sample simply might not represent the whole.

Larger, well-chosen samples reduce sampling risk. Note how this connects back to
the audit risk model: sampling risk is one reason detection risk is never zero,
which is why auditors express *reasonable* assurance, not absolute certainty.

## Exam focus

- Classify controls by action: **preventive** (before), **detective** (after/
  find), **corrective** (fix/reverse); plus **deterrent**, **compensating**, and
  **directive**. Weekly log reconciliation = **detective**.
- **Compliance tests** check the control; **substantive tests** check the data.
  Strong compliance results let the auditor reduce substantive testing.
- In **CSA**, process owners assess their own controls and the auditor
  **facilitates**. **CAATs** analyze **entire populations** efficiently.
- The **most reliable evidence** is **auditor-obtained, independent/external,
  and original/written**. A direct external confirmation beats auditee-supplied
  copies.
- **Attribute sampling** = rate of occurrence / compliance ("how often");
  **variable sampling** = amounts / substantive ("how much").
- **Sampling risk** = the sample may not represent the population; it never
  reaches zero, so auditors give reasonable, not absolute, assurance.
