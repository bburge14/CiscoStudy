# Compliance Frameworks & Governance Policies

Governance is how leadership *directs* security; compliance is how you *prove* you
are doing what you said. An enterprise architect must know which external framework
answers which demand — "certify us," "assure our customers," "sell to the U.S.
government," "protect card data" — and must build the internal policy structure and
accountability that make those claims true. This lesson covers both halves.

## The major frameworks, and what each is *for*

The trap on this exam is treating all frameworks as interchangeable. They are not.
Pick by the business need in the stem.

| Framework | Nature | Use it when the goal is... |
|-----------|--------|----------------------------|
| **ISO/IEC 27001** | Certifiable ISMS standard (international) | A single, globally recognized certification you can be formally **audited and certified** against |
| **ISO/IEC 27002** | Guidance / control catalog | Implementation detail behind 27001's controls |
| **NIST CSF 2.0** | Voluntary risk framework | A flexible, outcome-based program structure (the six **Functions**) |
| **NIST SP 800-53** | Control catalog (U.S. federal) | A detailed control baseline for federal systems |
| **SOC 2 (Type I/II)** | AICPA attestation report | Giving **customers independent assurance** about a service provider's controls |
| **FedRAMP** | U.S. gov authorization (built on 800-53) | A CSP selling cloud services to **U.S. federal agencies** |
| **PCI DSS** | Industry mandate | Anyone **storing/processing/transmitting payment-card data** |

A few currency points worth carrying in:

- **ISO/IEC 27001:2022** restructured **Annex A to 93 controls** (down from 114)
  across four themes — *Organizational, People, Physical, Technological*.
- **NIST Cybersecurity Framework 2.0** (2024) has **six Functions**: **Govern,
  Identify, Protect, Detect, Respond, Recover.** *Govern* was added in 2.0.
- **SOC 2 Type II** differs from Type I by testing control **effectiveness over a
  period** (months), not just design at a point in time — that "over time" wording
  is the giveaway.
- **FedRAMP** is layered on **NIST SP 800-53** and is the standardized,
  government-wide authorization for cloud offerings.
- **PCI DSS v4.0.1** is the current version (v4.0 retired at the end of 2024, and
  the future-dated requirements became mandatory in 2025).

> Match the framework to the *demand*: "internationally certifiable" → **ISO
> 27001**; "give customers an independent report" → **SOC 2**; "sell cloud to
> federal agencies" → **FedRAMP**; "we take credit cards" → **PCI DSS**; "flexible
> outcome-based program" → **NIST CSF**.

## Benchmarks and configuration guides

Frameworks say *what* to achieve; **benchmarks** say *how to configure a specific
system* to get there. The **CIS Benchmarks** and **DISA STIGs** are consensus
hardening baselines for particular platforms (OS, browser, cloud service). They are
how a policy requirement like "harden all servers" becomes a checkable, automatable
configuration standard.

## The governance document hierarchy

Internal governance flows top-down through documents with different authority. The
level of a document tells you how binding and how detailed it is.

> **Policy** states management's intent (mandatory, high-level). **Standard** makes
> a requirement specific and mandatory. **Procedure** gives the exact ordered
> steps. **Guideline** is optional, recommended advice. A **baseline** is the
> mandatory minimum configuration.

- A **policy** says *what and why* — "we will protect confidential information." It
  rarely changes and names no products.
- A **standard** names the specific, mandatory rule — "all laptops use AES-256
  full-disk encryption."
- A **procedure** is the numbered recipe — "steps to deprovision a leaver."
- A **guideline** is advisory; the tells are *should*, *recommended*, *optional*.
- A **baseline** is the floor every system of a class must clear before it ships.

The single biggest discriminator: **guidelines are optional; policies, standards,
procedures, and baselines are mandatory.**

## Governance structures and accountability

Governance only works when someone is unambiguously accountable. SecurityX leans on
a few distinctions:

- **Board / senior executive management** holds **ultimate accountability** for the
  security program and for *accepting enterprise risk*. They approve the top-level
  policy; their sign-off is what gives it authority.
- A **steering committee** aligns security priorities with business strategy across
  departments.
- **Data owner** (accountable for a data set, sets classification) vs **data
  custodian/steward** (implements and maintains the controls day to day) vs **data
  processor** (acts on the owner's instructions). Owners decide; custodians do.
- A **RACI matrix** (Responsible, Accountable, Consulted, Informed) assigns roles
  per task — and there is exactly **one Accountable** party per activity.

### Separation of duties and least privilege

Governance encodes anti-fraud structure into process:

- **Separation of duties (SoD)** splits a sensitive transaction so no single person
  controls it end to end — e.g., the person who *creates* a vendor record cannot
  also *approve payments* to it. SoD defeats unilateral fraud and error.
- **Two-person control / dual control** requires two people to act together for one
  high-risk operation (think launch keys).
- When a team is too small for true SoD, **compensating controls** — mandatory
  **job rotation**, enforced **mandatory vacation**, and tight **detective logging
  with independent review** — stand in to surface abuse.
- **Least privilege** grants only the access a role needs; **need to know** limits
  it further to the specific data required for a task.

> If a stem describes one person able to both initiate *and* approve the same
> transaction, the control in question is **separation of duties**. If the team is
> too small to split the duty, the answer is a **compensating control** such as job
> rotation or mandatory vacation.

## Attestation, assessment, and the audit trail

Compliance is proven through **assessments** (you check yourself), **audits**
(independent examination against a standard), and **attestation** (a formal
statement, e.g., a SOC 2 report or a PCI **Attestation of Compliance**). Evidence
must be retained; **auditable logging** and clean **documentation** are what turn a
claim into a defensible position.

## Exam focus

- Map framework to need: **ISO 27001** = certifiable ISMS; **SOC 2 Type II** =
  customer assurance *over a period*; **FedRAMP** = cloud for U.S. federal (built on
  **NIST SP 800-53**); **PCI DSS** = payment-card data; **NIST CSF 2.0** = flexible
  outcome framework with six Functions (**Govern** added in 2.0).
- **CIS Benchmarks / STIGs** are *configuration* hardening baselines — the "how" for
  a specific platform, not a program framework.
- Document hierarchy: **policy** (intent) → **standard** (mandatory specific rule) →
  **procedure** (steps) → **guideline** (optional). **Guidelines are optional;
  everything else is mandatory.** A **baseline** is the minimum config.
- **Senior management/board** approves policy and **accepts enterprise risk**;
  **RACI** has exactly one **Accountable** party per task.
- **Separation of duties** stops one person owning a transaction end to end; when a
  team is too small, use **compensating controls** (job rotation, mandatory
  vacation).
- Distinguish **data owner** (accountable, classifies) from **custodian** (operates
  the controls).
