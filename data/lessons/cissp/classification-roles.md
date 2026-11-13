# Data Classification & Ownership Roles

You cannot protect everything equally — budgets and attention are finite. Asset
security starts by deciding *which data matters most* (classification) and *who is
responsible for it* (roles). Get these two right and the rest of the program can
spend its effort where the loss would hurt. This lesson covers both the schemes
used to label data and the people accountable for handling it.

## Why classify at all

Classification is a risk-management act: it sorts information by the damage its
compromise would cause, so that controls can be matched to sensitivity. A public
marketing brochure and a database of patient records should not get the same
protection. Classification drives **handling requirements** — who may access the
data, how it must be stored and transmitted, how long it is retained, and how it
is destroyed.

> **The data owner classifies data based on the impact of its compromise. The
> classification then dictates the mandatory handling, labeling, and protection
> rules that follow it everywhere the data goes.**

## Classification schemes

Two families appear on the exam. Know both, and know that the *number and names*
of levels differ.

**Government / military scheme**, defined by the damage unauthorized disclosure
would cause to national security:

| Level | Damage from disclosure |
|-------|------------------------|
| **Top Secret** | **Exceptionally grave** damage |
| **Secret** | **Serious** damage |
| **Confidential** | Damage |
| **Controlled Unclassified / Sensitive but Unclassified** | Needs protection but below Confidential |
| **Unclassified** | No damage; releasable |

> The high-yield mapping: **Top Secret = exceptionally grave damage; Secret =
> serious damage; Confidential = damage.** Memorize the three adjectives.

**Commercial / private-sector scheme** (names vary by organization, from most to
least sensitive): **Confidential / Proprietary → Private → Sensitive → Public.**
The exact words are less standardized than government levels; the exam cares that
you can rank them and understand that each organization defines its own tiers.

Once data is classified, it is **marked and labeled** so that automated and human
handlers enforce the right controls. Data can later be **declassified** when it no
longer warrants protection — but downgrading requires a deliberate, authorized
decision, never a default.

## The data roles

CISSP is precise about who does what. The exam repeatedly asks you to separate the
person who **decides** from the person who **implements** and the person the data
is **about**.

- **Data owner (information owner)** — a senior business official **ultimately
  accountable** for a data set. The owner **classifies** the data, **defines
  access requirements**, and sets protection policy. Decisions, not hands-on work.
- **Data custodian** — the hands-on role (often IT/operations) that **implements
  and maintains** the controls the owner specified: backups, access settings,
  patching, encryption configuration. The custodian carries out; it does not
  decide classification.
- **Data steward** — responsible for the **quality, context, and business meaning**
  of the data (metadata, fitness for use).
- **System owner** — accountable for a specific system (and its security plan) that
  processes the data.
- **Data controller** — (privacy/GDPR term) the entity that **determines the
  purposes and means** of processing personal data. It bears primary legal
  responsibility.
- **Data processor** — processes personal data **on behalf of** the controller,
  following the controller's instructions (e.g., a SaaS vendor).
- **Data subject** — the **individual** the personal data is about.
- **User** — accesses data to do their job, under least privilege and need to know.

> The reliable exam distinction: the **owner decides** (classifies, defines access);
> the **custodian implements and maintains** the protective controls. In privacy
> contexts, the **controller determines** why/how; the **processor acts on the
> controller's instructions**.

### Matching scenarios to roles

- A VP designates a dataset "Confidential" and states who may see it → **data
  owner**.
- IT configures nightly backups and sets the folder permissions → **data
  custodian**.
- A marketing firm processes customer emails under its client's instructions →
  **data processor** (the client is the **controller**).
- The customer whose email it is → **data subject**.

## Classification as a shared contract

A subtle but tested idea: classification is only useful if it travels with the
data and everyone honors it. A "Confidential" label is a contract — it tells a
custodian to encrypt, tells a user not to email it externally, and tells the
disposal process to destroy rather than recycle the drive. When a question asks
what should happen *first* with a new data set, the answer is almost always
"classify it (or identify its owner)," because nothing downstream — access,
encryption, retention — can be decided until you know how sensitive it is and who
owns it.

## From classification to an asset inventory

Classification is only enforceable if you know what you have. A current **asset
inventory** — of data stores, systems, and the information they hold — is the
prerequisite for applying classification consistently: you cannot protect, label,
or correctly dispose of data you don't know exists. Each asset should trace to an
**owner** and a **classification**, and its labels should carry any **handling
caveats** ("internal only — do not forward"). That inventory then feeds risk
management, incident response (knowing what's affected and how sensitive it is),
and secure disposal at end of life. When a question asks what underpins an
effective classification program, the answer is often "an accurate, maintained
inventory of assets."

## Exam focus

- **Classify by impact of compromise.** Government levels and their damage:
  **Top Secret = exceptionally grave, Secret = serious, Confidential = damage**,
  then CUI/SBU and Unclassified. Commercial schemes rank roughly **Confidential →
  Private → Sensitive → Public** with org-specific names.
- The **data owner** is a senior businessperson who **classifies** data and
  **defines access**; the **data custodian** (IT) **implements and maintains** the
  controls. Owner decides, custodian does.
- Privacy roles: **controller determines purpose/means**, **processor acts on its
  behalf**, **data subject is the individual**, **data steward** handles data
  quality/meaning.
- When a scenario asks the FIRST step for new data, it is usually **classify it /
  identify the owner** — classification drives every downstream control.
- **Declassification** is a deliberate, authorized downgrade, never automatic.
- Classification depends on a current **asset inventory** — you can't protect or
  label data you don't know you have; each asset ties to an **owner** and a
  **classification**.
