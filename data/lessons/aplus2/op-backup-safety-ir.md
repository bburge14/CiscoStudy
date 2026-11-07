# Backup & Recovery, Safety & Incident Response

Three practical duties sit under operational procedures: making sure data survives
a disaster (**backup & recovery**), making sure *you and the equipment* survive the
workday (**safety**), and handling the moment something goes legally or security
wrong (**incident response**). Each is a set of definitions and "what do you do
first" calls the exam loves.

## Backup & recovery

### The backup types (and the archive bit)

Every file has an **archive bit** that Windows sets whenever the file changes. The
backup types differ in **what they copy** and **whether they clear that bit**:

| Type | Copies | Clears archive bit? | Restore needs |
|------|--------|:-------------------:|---------------|
| **Full** | everything | yes | just the full set |
| **Incremental** | changes since the **last backup of any type** | **yes** | the full **+ every** incremental |
| **Differential** | changes since the **last full** | **no** | the full **+ one** differential |

The exam distinguishes incremental from differential by two words — *"since the
last backup of any type"* and *"clears the archive bit."*

> A **full every Sunday**, then each weekday backing up **only what changed since
> the last backup of any type and clearing the archive bit** = **incremental**. If
> instead it backed up everything since the last **full** and left the bit alone,
> that's **differential**.

Incremental backups are **fast to create** (small daily sets) but **slower to
restore** (you replay the full plus every increment). Differentials are the
opposite — bigger each day, but restore is just the full plus one.

### The 3-2-1 rule

The industry rule of thumb for *where* copies live:

> **3-2-1:** keep **3** copies of your data, on **2** different types of media, with
> **1** copy stored **offsite**.

That guards against a single device failing, a media type failing, and a
site-level disaster (fire/flood/theft) all at once.

### Test your restores

A backup you've never restored is a hope, not a backup. A company that has run
nightly backups for a year but **never confirmed they can actually be restored**
needs **regular restore testing** — periodically restoring from backup to prove the
data comes back intact.

### Rotation schemes

**Grandfather-Father-Son (GFS)** keeps **daily (son), weekly (father), and monthly
(grandfather)** sets, promoting certain backups to **longer retention** as they age.
A stem describing separate daily/weekly/monthly sets with escalating retention is
**GFS**.

## Safety

### ESD — the invisible component killer

**Electrostatic discharge (ESD)** can fry chips with a spark you can't even feel.
Before handling RAM or expansion cards, prevent it:

- Wear an **anti-static wrist strap** clipped to the chassis/ground.
- Work on an **anti-static (ESD) mat**.
- Store parts in **anti-static bags**; keep humidity up; avoid carpet.

> Two ESD practices that protect components: an **anti-static wrist strap** and an
> **anti-static mat**. (Don't wear a strap inside a **CRT monitor or power supply**
> — those hold lethal voltage.)

### Electrical fire

If a **power supply catches fire while still energized**, grab a **Class C** fire
extinguisher — the class rated for **electrical** fires. The classes: **A** =
ordinary combustibles, **B** = flammable liquids, **C** = **electrical**, **K** =
kitchen grease.

### Hazardous materials and disposal

Some gear is **regulated/toxic waste** and must go to an approved recycler, never
the trash: **batteries**, **toner/ink cartridges**, **CRT monitors** (lead), and
**chemical solvents/aerosols**. Before handling a chemical, read its **Safety Data
Sheet (SDS)** — the document that lists its **hazards, required PPE, and proper
disposal**.

> "I need the hazards, protective equipment, and disposal rules for a cleaning
> solvent" → consult the **SDS** (Safety Data Sheet).

### Lifting

To move something heavy like a UPS from the floor to a rack, use proper **lifting
technique**: **bend at the knees, keep your back straight, lift with your legs**,
hold the load close, and don't twist — get a **team lift** if it's too heavy.

## Incident response

### First response

If you're the **first to discover a possible security incident**, follow
first-response best practice: **identify** the issue, **report it through proper
channels**, and **preserve the data/scene** — don't start "fixing" or altering
things, because you may be destroying evidence.

### Chain of custody

When something becomes **potential legal evidence** (for example, illegal content
found on a company PC), you must **document every person who handles the drive —
when, why, and what they did**. That documentation is the **chain of custody**, and
it's what keeps the evidence admissible.

> Documenting **everyone who touched the evidence and when** = **chain of custody**.

### Order of volatility

When collecting digital evidence from a **running** computer, capture the data
that's **lost soonest first**. That's the **order of volatility**: **RAM / live
system state** vanishes the instant you power off, so it's collected **before** the
disk.

### Regulated data

Know the data categories, because handling rules depend on them:

- **PII** — personally identifiable information.
- **PHI** — protected **health** information. A healthcare provider's **patient
  medical histories** are **PHI** (HIPAA-regulated).
- **PCI** — payment card data.

### Licensing

Software is governed by its **license (EULA)**. Installing **one single-seat
(personal) license on 15 computers** when the license forbids it is a violation; the
concept is **software licensing** — a **per-seat** license covers a set number of
installs, while a **site/enterprise** license covers many.

## The whole thing in one paragraph

Back up with **full/incremental/differential** — incremental copies changes *since
any last backup* and **clears the archive bit**, differential copies changes *since
the last full* and **doesn't** — follow **3-2-1** (3 copies, 2 media, 1 offsite),
**test your restores**, and rotate with **GFS**. Stay safe by preventing **ESD**
(wrist strap + mat), using a **Class C** extinguisher on electrical fires, recycling
**batteries/toner/CRTs** as regulated waste, reading the **SDS** before handling
chemicals, and **lifting with your legs**. For incidents, **identify and report**
first and **preserve** evidence, keep the **chain of custody**, collect the **most
volatile data (RAM) first**, recognize **PHI** and other regulated data, and respect
software **licensing**.

## On the exam

- **Incremental** = since the last backup of *any* type, **clears** the archive bit
  (fast backup, slow restore). **Differential** = since the last *full*, **doesn't**
  clear it (restore = full + one). **Full** = everything.
- **3-2-1** = 3 copies / 2 media / 1 offsite; **test restores** to validate backups;
  **GFS** = daily/weekly/monthly rotation with escalating retention.
- ESD: **wrist strap + anti-static mat**. Electrical fire: **Class C**. Chemical
  info: **SDS**. Regulated waste: **batteries, toner, CRTs**. Heavy lift: **bend
  the knees, lift with the legs**.
- Incident response: **identify → report → preserve**; **chain of custody**
  documents who handled evidence; **order of volatility** = capture **RAM first**;
  healthcare records = **PHI**; installing a single-seat license on many PCs is a
  **licensing** violation.
