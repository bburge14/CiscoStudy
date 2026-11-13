# Roles, Responsibilities & the Legal/Regulatory Landscape

Governance only works when everyone knows their part. A strategy no one owns is a
wish. In this lesson we map the cast of characters in a security program — who is
*accountable*, who is *responsible*, and who merely *operates* — and then we step
outside the organization to the laws and regulations that set the floor the
manager must build above. Both topics reward the same instinct the exam loves:
think about ownership and obligation, not technology.

## Accountability vs. responsibility

These two words look like synonyms in everyday speech. On the CISM exam they are
not, and the difference decides many questions.

> **Accountability** is ultimate answerability for an outcome — it cannot be
> delegated. **Responsibility** is the duty to actually do the work, and it can
> be delegated and shared.

A manager can delegate the *task* of encrypting a database to an engineer
(responsibility), but if the data leaks, the owner is still *accountable*. The
line you must be able to give instantly:

> **The board of directors and senior management are ultimately accountable for
> information security.** They can delegate responsibility, but never
> accountability.

This is why, after a breach, regulators and the exam point to the **board and
executives** — not the firewall admin — as the ones answerable for the state of
security.

## The roles, from the top down

| Role | What they own |
|------|---------------|
| **Board of directors** | Ultimate accountability; sets risk appetite and oversees |
| **Senior / executive management** | Approves strategy and policy; provides resources; accountable |
| **Steering committee** | Aligns and prioritizes security with business objectives |
| **CISO / information security manager** | Develops, runs, and reports on the program |
| **Data / information owner** | Classifies data, decides who may access it, accepts residual risk |
| **Data custodian** | Implements and maintains the controls the owner specifies |
| **Data steward** | Manages data quality, meaning, and proper business use |
| **Users** | Follow policy; handle information per their training |

Three distinctions the exam tests relentlessly:

- The **data owner** is a *business* leader, not IT. The owner **determines the
  classification level** of a set of information and **decides who may access
  it**, and typically **accepts the residual risk** on behalf of the business.
- The **data custodian** (often IT/operations) merely *carries out* the owner's
  wishes — backups, access provisioning, encryption. Custodians protect data;
  owners decide how it must be protected.
- The **security manager** does **not** own the data and does **not** accept its
  risk. The manager advises, builds the program, and reports — but ownership and
  risk acceptance belong to the business.

> If a question asks *who decides a data set's classification or who may access
> it*, the answer is the **data (information) owner** — every time.

### RACI: making ownership explicit

To stop responsibilities from falling through the cracks, managers use a **RACI
chart**, which labels each task:

- **R**esponsible — does the work.
- **A**ccountable — answerable for it (exactly one per task).
- **C**onsulted — gives input.
- **I**nformed — kept in the loop.

RACI is the practical tool behind the accountability/responsibility distinction.
Expect it as the "best way to clarify who does what" answer.

## Due care and due diligence

Two more terms that sound alike and are constantly swapped in distractors:

> **Due care** is doing what a reasonable, prudent person would do to protect the
> organization — taking the right actions. **Due diligence** is the ongoing
> homework that informs those actions — investigating, assessing, and verifying.

Due diligence is *knowing*; due care is *doing*. A manager who researches a
vendor's security posture before signing is exercising due diligence; a manager
who then implements the agreed safeguards is exercising due care. Demonstrating
both is how an organization shows it acted responsibly if something goes wrong.

## The legal and regulatory landscape

Some obligations come from *outside* the organization and carry legal force.
Internal policy is self-imposed; a law or regulation is imposed on you, and
breaking it brings fines, lawsuits, or sanctions. Managers treat external
requirements as a **floor** — the minimum you must meet — not the ceiling.

Regulations you should recognize by what they protect:

- **GDPR** — personal data of individuals in the EU; strict consent, rights, and
  breach-notification duties, with large fines.
- **HIPAA** — protected health information in the U.S.
- **PCI DSS** — cardholder data (a contractual standard enforced by the card
  brands, not a government law, but mandatory for anyone handling card data).
- **SOX** — financial reporting integrity for U.S. public companies.

You do not need to memorize statute text. You need the manager's posture toward
all of them.

> The **BEST reason to comply** with laws and regulations is to **demonstrate due
> diligence and reduce legal and financial liability** — not merely "to avoid
> fines." Compliance is evidence that the organization acted responsibly.

Two more management truths the exam rewards:

- **Compliance is necessary but not sufficient.** Meeting a regulation does not
  mean you are *secure*; it means you cleared a legal minimum. A strategy driven
  only by compliance leaves real risks unaddressed.
- When operating across borders, you must account for **multiple, sometimes
  conflicting jurisdictions.** Data-sovereignty and cross-border transfer rules
  can decide where data may even be stored.

### When a new regulation appears: what to do FIRST

A classic CISM scenario: a new data-protection law will soon apply. The tempting
answers are "buy a tool" or "write a new policy." The manager's first move is to
find out *where you stand*.

> When a new legal or regulatory requirement will apply, the information security
> manager should **FIRST perform a gap analysis** — compare current controls
> against the new requirements. You cannot plan remediation until you know the
> gap.

Gap analysis first, remediation roadmap second, specific controls third. That
ordering — understand before you act — is the governance reflex in miniature.

## The manager's reflex

For roles and legal questions, run this check:

1. Is the question about *ultimate answerability*? → **board / senior
   management** are accountable.
2. Is it about *deciding* classification or access, or *accepting* risk? → **data
   owner** (the business), never IT or the security manager.
3. Is it about a *new external requirement*? → **gap analysis first.**
4. Is it about *why* we comply? → **due diligence and reduced liability**, and
   remember compliance is a floor, not proof of security.

## Exam focus

- **Accountability can't be delegated; responsibility can.** The **board and
  senior management are ultimately accountable** for information security.
- The **data (information) owner** — a business leader — **classifies data,
  decides access, and accepts residual risk.** The **custodian** (IT) implements
  the controls. The **security manager owns neither the data nor its risk.**
- **RACI** clarifies who is Responsible, Accountable, Consulted, Informed — one
  Accountable per task.
- **Due diligence = investigating/knowing; due care = acting/doing.** Together
  they show the organization behaved reasonably.
- Know regulations by what they protect: **GDPR** (EU personal data), **HIPAA**
  (U.S. health), **PCI DSS** (card data), **SOX** (financial reporting).
- The **BEST reason to comply** is to **demonstrate due diligence and reduce
  legal/financial liability.** **Compliance is a floor, not proof of security.**
- A **new regulation → perform a gap analysis FIRST**, then build the remediation
  roadmap.
