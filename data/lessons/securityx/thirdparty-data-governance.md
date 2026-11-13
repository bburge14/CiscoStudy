# Third-Party Risk & Data Governance

Modern enterprises run on other people's software and other people's data centers,
and they hold data that other people have legal rights over. Two of the GRC
domain's hardest problems live here: managing the **supply chain and third
parties** you depend on, and governing **data** across jurisdictions and privacy
law. SecurityX tests both at the level of someone who negotiates contracts and
designs a privacy program.

## Why third-party risk is its own discipline

When you outsource a function, you outsource the work but not the accountability. A
vendor breach is your breach to your customers and regulators. Supply-chain
compromise — poisoning an upstream component so the attack rides in through a
trusted update — has become a top-tier enterprise threat precisely because it
bypasses your perimeter entirely.

> You can delegate a task to a vendor, but you cannot delegate the **risk** or the
> **accountability**. Third-party risk management (TPRM) extends your control
> expectations across the contract boundary.

### Fourth-party and nth-party risk

Your vendors have vendors. A critical SaaS provider that subcontracts data
processing introduces a **fourth party** from your vantage point — a dependency you
did not choose and may not even see. With a limited audit budget, you manage this by
*contractually requiring* the vendor to assess and flow down controls to its own
subprocessors, and by demanding visibility into that chain, rather than trying to
audit everyone yourself.

## The vendor lifecycle and its agreements

Third-party risk is a lifecycle: **due diligence** before onboarding, **contractual
controls** at signing, **ongoing monitoring** during the relationship, and secure
**offboarding** (revoke access, return/destroy data) at the end. The agreement types
are heavily tested — know what each one *is for*.

| Agreement | What it defines |
|-----------|-----------------|
| **MSA** (Master Service Agreement) | The overarching terms governing the whole relationship |
| **SOW** (Statement of Work) | The specific deliverables, timeline, and scope for one engagement |
| **SLA** (Service Level Agreement) | **Measurable** service commitments (e.g., 99.95% uptime) and penalties |
| **MOU/MOA** | A (often non-binding) statement of intent to cooperate |
| **BPA** (Business Partner Agreement) | Terms between partners sharing in a venture |
| **NDA** | Confidentiality obligations |
| **ISA** (Interconnection Security Agreement) | Security terms for a technical system-to-system connection |

> If the stem asks which document pins down a **measurable, enforceable** metric
> like "99.95% monthly availability," the answer is the **SLA**.

### Assessing and monitoring vendors

Due diligence tools: security questionnaires (e.g., **SIG**), independent **SOC 2**
reports, penetration-test summaries, financial health checks, and **right-to-audit**
clauses in the contract. Because a point-in-time review goes stale, mature programs
add **continuous monitoring** — security-rating services and automated alerts on a
vendor's external posture.

### Software supply chain and the SBOM

For software specifically, the key artifact is the **SBOM (Software Bill of
Materials)** — a complete inventory of every component and dependency in a product.
When the next widespread open-source library flaw lands, the SBOM is the *fastest
reliable* way to answer "are we affected and where?" Pair it with **provenance**
and **code signing** to verify a build has not been tampered with, and with
**vendor/third-party assessments** of the suppliers themselves.

## Data governance: owning data responsibly

**Data governance** is the overall management of data's availability, integrity,
usability, and security across its lifecycle. It starts with **classification** —
labeling data by sensitivity (e.g., Public, Internal, Confidential, Restricted) so
controls can be applied proportionally — and with assigning **data owners** who are
accountable for each category.

### Privacy roles and principles

Privacy law adds precise roles the exam expects verbatim, drawn from GDPR:

- **Data subject** — the individual the data is about.
- **Data controller** — the entity that **determines the purposes and means** of
  processing. The controller decides *why* and *how*.
- **Data processor** — processes data **on the controller's behalf and
  instructions**. A cloud provider is typically a processor.
- **DPO (Data Protection Officer)** — required for certain organizations to oversee
  compliance.

Core privacy principles show up as scenarios:

- **Data minimization** — collect only what you need for the stated purpose.
- **Purpose limitation** — use data only for the purpose it was collected for.
- **Storage limitation / retention** — keep data only as long as needed, then
  dispose of it. Deleting records once the business purpose ends satisfies both
  **data minimization** and **storage limitation**.
- **Right to erasure ("right to be forgotten")**, **data portability**, and
  **consent** round out individual rights under GDPR.

### Residency, sovereignty, and cross-border transfer

- **Data sovereignty** — data is subject to the laws of the country in which it is
  *located*. Storing EU residents' data in a U.S. region can expose it to foreign
  jurisdiction.
- **Data residency** — a requirement that data physically reside in a specific
  geography. When regulators insist EU data remain under EU jurisdiction, the
  architectural answer is to keep it in an **in-region** data store and apply the
  appropriate **transfer mechanisms** (e.g., standard contractual clauses).
- Know the big regimes by scope: **GDPR** (EU personal data, extraterritorial),
  **CCPA/CPRA** (California consumers), **HIPAA** (U.S. health data / **PHI**), and
  that **PII**/**PHI** are the sensitive categories these laws protect.

> Data location determines which laws apply (**sovereignty**); a rule forcing a
> physical location is **residency**. If regulators demand EU data stay under EU
> law, keep it in-region — do not just encrypt it in a foreign cloud.

### Disposal and the lifecycle

Governing data to the end means secure **destruction**: cryptographic erase,
degaussing magnetic media, or physical shredding, with a **certificate of
destruction** as evidence. Classification, retention schedules, and disposal
together form the data lifecycle a governance program must document.

## Exam focus

- You can outsource the task but not the **accountability**; a vendor/supply-chain
  breach is still yours. **Fourth-party** risk = your vendor's subprocessors —
  manage it by contract and flow-down, not by auditing everyone.
- Agreements: **SLA** = measurable service metrics (uptime); **MSA** = overarching
  terms; **SOW** = specific deliverables; **MOU** = (often non-binding) intent;
  **BPA** = partner terms; **ISA** = system interconnection security.
- An **SBOM** is the fastest way to find which products use a newly vulnerable
  open-source component; pair with code signing/provenance.
- **Controller** determines purpose and means of processing; **processor** acts on
  the controller's instructions (cloud providers are usually processors).
- **Data minimization** (collect only what's needed) and **storage limitation**
  (retain only as long as needed) justify deleting data once its purpose ends.
- **Data sovereignty** = data obeys the laws where it sits; **data residency** =
  a requirement to keep data in a geography. For EU-jurisdiction demands, store
  **in-region**.
- **PII/PHI** are the protected categories; **GDPR, CCPA/CPRA, HIPAA** map to EU
  personal data, California consumers, and U.S. health data respectively.
