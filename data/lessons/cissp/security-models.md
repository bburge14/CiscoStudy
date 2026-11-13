# Security Models & Trusted System Capabilities

Before engineers build a secure system, theorists give them rules that *provably*
enforce a security goal. Security models are those rules expressed formally, and
trusted-system capabilities are the architectural pieces that make enforcement
trustworthy. CISSP expects you to recognize each model by what it protects and by
its signature properties — and to know the components that make a system worthy of
trust. These are among the most memorizable (and most tested) facts in the CBK.

## Security models

A **security model** is a formal description of how a system enforces a policy.
The two you must know cold are Bell-LaPadula and Biba — opposites by design.

### Bell-LaPadula (BLP) — confidentiality

Built for the military to stop secrets from leaking downward.

> **Bell-LaPadula protects confidentiality** with two rules:
> **Simple Security Property = "no read up"** (a subject cannot read data above its
> clearance) and the **\* (star) Property = "no write down"** (a subject cannot
> write data to a lower level, where it might leak).

So a Confidential user cannot read Top Secret files (no read up), and a Top Secret
process cannot write into a Confidential file (no write down). Mnemonic: BLP is
about keeping secrets, so you **read down, write up**.

### Biba — integrity

Biba is BLP flipped, and it protects **integrity** — keeping trusted data from
being corrupted by lower-integrity sources.

> **Biba protects integrity** with: **Simple Integrity Property = "no read down"**
> (don't read lower-integrity data that could taint you) and the **\* Integrity
> Property = "no write up"** (don't write to a higher-integrity level you might
> corrupt).

Mnemonic: Biba = integrity, so you **read up, write down** — the exact mirror of
BLP.

### Clark-Wilson — commercial integrity

Where Biba is abstract, **Clark-Wilson** is a practical integrity model for
business. It enforces integrity through **well-formed transactions** and the
**access control triple**: a subject may touch a **constrained data item (CDI)**
only through an authorized **program (transformation procedure)**, never directly.
It builds in **separation of duties** and auditing. Think of a banking app where a
clerk can only change a balance by running approved transactions, not by editing
the database by hand.

### The others worth recognizing

- **Brewer-Nash (Chinese Wall)** — prevents **conflicts of interest** by
  dynamically blocking access to data in a competing company once you've accessed a
  rival's; access rights change based on your history.
- **Lattice-based** — assigns upper/lower bounds to subjects and objects; the
  mathematical backbone of mandatory access control.
- **Graham-Denning / Harrison-Ruzzo-Ullman (HRU)** — model how rights are
  **created, assigned, and revoked**.
- **Take-Grant** — uses directed graphs to show how permissions can be passed.
- **Noninterference** — actions at a high level must not be observable at a low
  level (a defense against covert channels).

| Model | Protects | Signature rule |
|-------|----------|----------------|
| Bell-LaPadula | Confidentiality | No read up, no write down |
| Biba | Integrity | No read down, no write up |
| Clark-Wilson | Integrity | Access triple, well-formed transactions |
| Brewer-Nash | Conflict of interest | Dynamic "Chinese Wall" |

## Trusted system capabilities

A system you can trust isn't trusted by faith — it's built from components whose
security can be reasoned about.

> The **Trusted Computing Base (TCB)** is the totality of hardware, software, and
> firmware responsible for enforcing security. Keep it **small and simple** so it
> can be analyzed and trusted.

- **Reference monitor** — the abstract concept of mediating **every** access
  between subjects and objects. It must be **always invoked (non-bypassable),
  tamperproof, and small enough to be fully verified.** Those three properties are
  a favorite exam item.
- **Security kernel** — the actual hardware/software/firmware that **implements**
  the reference monitor. (Reference monitor = the idea; security kernel = the
  implementation.)
- **Security perimeter** — the boundary separating the TCB from the rest of the
  system.
- **Protection rings** — concentric privilege levels, with the kernel at **Ring 0**
  (most privileged) and user applications at **Ring 3**. Inner rings are protected
  from outer ones.
- **Abstraction, layering, and data hiding** — design principles that reduce
  complexity and keep lower-level details out of reach.
- **Open vs closed systems** — open systems use published standards and
  interoperate; "security through obscurity" (closed, secret design) is not a
  reliable control on its own.

## Evaluating trust: the Common Criteria

How do you *prove* a product meets a security target? Through independent
evaluation. The modern standard is the **Common Criteria (ISO/IEC 15408)**.

- The product under review is the **Target of Evaluation (TOE)**.
- A **Protection Profile (PP)** states the security requirements a customer wants.
- A **Security Target (ST)** is the vendor's claim of what the TOE does.
- The result is an **Evaluation Assurance Level (EAL) from 1 to 7** — EAL1
  (functionally tested) up to **EAL7** (formally verified design and tested). A
  higher EAL means more rigorous *assurance*, not necessarily more features.

Older schemes you only need to recognize as legacy: **TCSEC (the "Orange Book,"**
U.S., confidentiality-focused, levels D through A1) and the European **ITSEC**.
Common Criteria superseded them.

## Exam focus

- **Bell-LaPadula = confidentiality**: **no read up (simple), no write down
  (\*).** **Biba = integrity**: **no read down (simple), no write up (\*).** They
  are mirror images — this is the most tested fact in Domain 3.
- **Clark-Wilson** = commercial integrity via the **access control triple**
  (subject → program → object) and well-formed transactions. **Brewer-Nash /
  Chinese Wall** = conflict-of-interest, dynamic access.
- The **reference monitor** must be **always invoked, tamperproof, and
  verifiable**; the **security kernel implements** it; the **TCB** is everything
  enforcing security (keep it small). Kernel runs at **Ring 0**.
- **Common Criteria (ISO 15408)**: **TOE, Protection Profile, Security Target**,
  and **EAL1–EAL7** assurance levels. TCSEC (Orange Book) and ITSEC are the legacy
  predecessors.
