# Digital Forensics

When an incident might end up in court — or even just in a serious internal
investigation — how you collect and handle evidence determines whether it can be
trusted. **Digital forensics** is the discipline of acquiring, preserving,
analyzing, and presenting digital evidence in a way that keeps it intact and
admissible. For an SSCP, the goal usually isn't to be the expert examiner; it's to
not *destroy* the evidence during a response. This lesson gives you the rules that
protect it.

## The guiding principle: preserve, don't contaminate

Digital evidence is fragile. Simply turning a computer off can erase memory;
simply opening a file changes its timestamps. Everything in forensics flows from
one mandate:

> Collect evidence in a way that **does not alter it**, and document every step so
> you can later **prove** it wasn't altered.

Two concepts make this concrete: the **order of volatility** (what to grab first)
and the **chain of custody** (how to prove integrity over time).

## Order of volatility: collect the fragile stuff first

Some evidence vanishes the instant power is lost or the system changes state;
other evidence sits patiently on a disk. Collect from **most volatile to least
volatile**:

> **Order of volatility (most to least):** CPU registers and cache -> RAM
> (memory) and running state (network connections, running processes) -> temporary
> / swap files -> data on disk -> remote logs and archives -> physical backups and
> printouts.

The headline rule: **capture volatile memory (RAM) before powering down**, because
RAM holds encryption keys, running malware, open network connections, and
unsaved data that disappear forever when the machine is turned off. A responder
who yanks the power cord "to be safe" may have just destroyed the most valuable
evidence in the case.

## Forensic acquisition: imaging and write blockers

You never investigate the original. You make an exact copy and work on that.

> A **forensic image** is a **bit-for-bit (bit-stream) copy** of the entire
> storage medium — every sector, including deleted-but-not-overwritten data and
> slack space — not just the visible files.

To make that copy without changing the source, use a **write blocker**:

> A **write blocker** is a hardware (or software) device placed between the
> suspect drive and the analysis system that **allows reads but physically
> prevents any write** to the original media, so the act of imaging cannot alter
> the evidence.

After imaging, you prove the copy is faithful with **hashing**: compute a
cryptographic hash (e.g., SHA-256) of the original and of the image. If the hashes
match, the copy is **identical**; if even one bit differed, the hash would change
completely. You re-hash later to show the evidence hasn't been tampered with since
acquisition. Hashing is the mathematical backbone of evidence **integrity**.

## Chain of custody: proving integrity over time

Collecting evidence cleanly is only half the battle; you must also account for it
every moment thereafter.

> The **chain of custody** is the documented, unbroken record of **everyone who
> collected, handled, transferred, or stored** a piece of evidence — with
> timestamps — so its integrity can be demonstrated in court.

A gap in the chain ("the drive sat unlogged in a drawer over the weekend") lets
opposing counsel argue the evidence could have been altered, and it may be thrown
out. Supporting practices include tamper-evident **evidence bags**, secure
storage, and detailed documentation of *who*, *what*, *when*, *where*, and *why*
for every transfer.

## From acquisition to presentation

A full forensic process runs: **identification -> collection/acquisition ->
examination -> analysis -> reporting/presentation.** A few more terms worth
knowing:

| Term | Meaning |
|------|---------|
| **Locard's exchange principle** | Every contact leaves a trace — attackers leave artifacts behind |
| **e-Discovery** | The legal process of identifying and producing electronically stored information for litigation |
| **Legal hold** | A duty to preserve relevant data once litigation is anticipated (no routine deletion) |
| **Admissibility** | Evidence must be relevant, reliable, and lawfully obtained to be used in court |
| **Data integrity** | Proven via hashing before and after handling |

Two practical cautions for the responder: know your **jurisdiction and authority**
before seizing anything (collecting evidence you have no legal right to can taint
the whole case), and remember that forensics and *fast* incident response can
conflict — containment may need to preserve evidence rather than wipe a machine,
so decide early whether a case is likely to be prosecuted.

## Types of evidence and live acquisition

Courts weigh different kinds of evidence differently, and a few terms come up:

- **Real evidence** — physical objects (a seized hard drive).
- **Documentary evidence** — logs, files, records (most digital evidence).
- **Best evidence rule** — courts prefer the original (or a verified forensic image
  that faithfully represents it) over a summary or copy of unknown fidelity.
- **Hearsay** — generally inadmissible, though business records like logs often
  qualify for an exception.

A practical collection choice is **live vs. dead acquisition**:

> **Live acquisition** captures data from a **running** system — essential when
> evidence is in RAM, or when the disk is **encrypted** and powering off would lose
> the decrypted state. **Dead (static) acquisition** images a **powered-off** disk,
> which is cleaner and more repeatable but loses all volatile data.

The tension is real: encryption and memory-resident malware push you toward live
acquisition even though touching a running system inevitably changes it. The
responder documents every action taken so the unavoidable changes are accounted
for — transparency, not perfection, is what keeps live evidence defensible.

## Exam focus

- The prime directive: **preserve evidence without altering it**, and **document**
  everything to prove it.
- **Order of volatility**: collect the most volatile first — **CPU cache/registers
  and RAM before powering down**, then disk, then archives. Pulling power first
  can destroy memory-resident evidence.
- Work from a **bit-for-bit forensic image**, never the original; use a **write
  blocker** to allow reads but block any write to the source; verify fidelity with
  **hashing** (matching hashes = identical copy).
- The **chain of custody** is the unbroken, timestamped record of who handled
  evidence; a gap can make it **inadmissible**.
- Know **legal hold**, **e-discovery**, **Locard's principle**, and that
  admissible evidence must be relevant, reliable, and lawfully obtained — confirm
  **authority/jurisdiction** before seizing.
