# Communication, Professionalism & Scripting

The last stretch of operational procedures is about **people** and **automation** —
how a technician behaves with a customer, and how a technician saves time with small
scripts. Both are tested the same way: a short scenario, and the professional (or
correct) choice among tempting wrong ones.

## Communication and professionalism

Most of this is common courtesy made explicit. The exam rewards the **calm,
respectful, customer-first** answer every time.

### Dealing with a frustrated customer

When a customer is **venting at length**, the professional move is **active
listening**: **let them finish without interrupting**, acknowledge the frustration,
and restate the problem to confirm you understood. You do **not** talk over them,
argue, get defensive, or dismiss the complaint.

> Angry customer mid-rant → **listen, don't interrupt, empathize, then clarify.**
> Interrupting or arguing is always the wrong answer.

### Speak the customer's language

When explaining a repair to a **non-technical** person, **avoid jargon, acronyms,
and slang** — use plain language they can follow. Talking over someone's head isn't
impressive; it's poor communication.

### Conduct at the customer's workspace

Professional on-site behavior includes:

- **Be on time**; if you'll be late, **contact the customer**.
- **Avoid distractions** — no personal calls, texting, social media, or chatting
  with coworkers while working.
- **Maintain a positive attitude** and project confidence.
- **Set and meet expectations**, communicate status, and **follow up** afterward.
- **Respect the customer's property and space**; clean up when done.

> Two behaviors that reflect professional conduct on site: **avoiding distractions
> (no personal calls)** and **being punctual / respecting the customer's property.**

### Confidential and private materials

If, while fixing a manager's laptop, you notice **personal financial documents or
private emails open on screen**, the appropriate response is to **respect privacy
and confidentiality** — don't read, copy, or share them, and keep the matter
confidential. Dealing appropriately with **confidential/private materials** is an
explicit professionalism objective.

## Scripting basics

Technicians automate repetitive work with small scripts. You don't have to *write*
them for the exam, but you must **recognize the file types and weigh the risks**.

### Know the extensions

| Extension | Script type / environment |
|-----------|---------------------------|
| **`.bat`** / `.cmd` | Windows **batch** file (Command Prompt) |
| **`.ps1`** | **PowerShell** script |
| **`.vbs`** | **VBScript** (legacy Windows logon scripts) |
| **`.sh`** | **shell** script (Linux/Unix, e.g. bash) |
| **`.py`** | **Python** script |
| **`.js`** | **JavaScript** |

Two direct matches: a script saved as **`.ps1`** is for **PowerShell**, and a
legacy Microsoft **VBScript** uses the **`.vbs`** extension.

### What scripting is good for

Scripts shine at repetitive, fleet-wide tasks:

- **Remapping network drives** at logon (a logon script that reconnects
  `\\server\share` for every user) — a classic, legitimate use.
- Restarting machines, **installing/updating applications**, automating **backups**,
  and **gathering information** across many PCs.

> "Automatically reconnect a shared network drive at each logon for everyone" → a
> perfect job for a **logon script**.

### The risks — weigh them before you deploy

Automation scales your mistakes as fast as your wins. Before pushing a script to
many machines, consider:

- **Unintentionally changing system settings** — a bad line can misconfigure every
  target at once.
- **Introducing malware** — running an untrusted or tampered script can spread it.
- **Browser or system crashes** from mishandled resources/variables.
- The sheer **blast radius** of a fleet-wide change.

Because of that, **test on one machine first**, review the script's source, and run
it with the **least privilege** that gets the job done.

> Two legitimate risks of mass-deploying a script: **inadvertently changing system
> settings** and **introducing malware** (or crashing systems through mishandled
> resources).

## The whole thing in one paragraph

Professional communication means **active listening** (let a frustrated customer
finish, don't interrupt or argue), **plain language** with non-technical users,
on-site discipline (**be punctual, avoid distractions, respect property**), and
treating **private materials as confidential**. Scripting means recognizing the
extensions — **`.bat`** batch, **`.ps1`** PowerShell, **`.vbs`** VBScript, **`.sh`**
shell, **`.py`** Python — knowing scripts are great for **logon drive mapping** and
other repetitive fleet tasks, and respecting the risks: scripts can **change
settings unintentionally, introduce malware, or crash systems**, so **test first**
and run with least privilege.

## On the exam

- With an upset customer, the right answer is to **listen without interrupting** and
  stay professional; with a non-technical customer, **avoid jargon**.
- Professional on-site conduct = **be on time, avoid distractions (no personal
  calls), respect the customer's property**, and **keep private materials
  confidential** (don't read or share them).
- Extensions: **`.ps1` = PowerShell**, **`.vbs` = VBScript**, **`.bat`/`.cmd` =
  batch**, **`.sh` = shell**, **`.py` = Python**.
- Scripting is ideal for **repetitive tasks** like **logon drive remapping**; the
  tested risks are **unintentionally changing settings**, **introducing malware**,
  and **crashing systems** — so **test before fleet-wide deployment**.
