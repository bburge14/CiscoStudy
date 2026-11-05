# CiscoStudy

A local, self-hosted study & diagnostic platform for **CCNA 200-301** and
**CCNP Enterprise ENCOR 350-401**, built with Python + Streamlit.

It is designed around **authentic, blueprint-aligned content** — every item uses
real Cisco IOS/IOS-XE syntax, real `show` output, and real protocol metrics, and
every answer explains *why the key is right, why each distractor is a trap, and
how to spot the pattern on the real exam*. There are **no placeholder questions**.

> **Content note.** All questions, lessons and labs here are **original study
> material** written to match the public Cisco exam topic blueprints and genuine
> IOS behaviour. Nothing is copied from Cisco's proprietary exam item bank, NetAcad
> assessments, or any "braindump" — doing so would violate copyright and the Cisco
> exam agreement. The goal is exam-grade accuracy, authored cleanly.

---

## Features (mapped to the requirements)

### 1. Dual study modes
- **♾️ Endless Drill** — an infinite, adaptive question stream with **instant
  grading** and deep technical breakdowns (including `show` verification
  commands). Missed questions **dynamically resurface more often** via a
  Leitner-box weighting (a just-missed item is sampled ~8× a mastered one). A
  **remediation toggle** restricts the stream to your weak sub-topics.
- **📚 Structured Milestones** — per unit:
  1. **Read** a clean Markdown lesson (architecture, definitions, syntax rules).
  2. **Lesson Quiz** (10–20 authentic items for that lesson, instant feedback).
  3. **Milestone Exam** — a cumulative 30-question exam drawn from the unit's
     (and prior units') item pool, **plus an interactive PBQ**, required to
     **unlock the next unit**.

### 2. Performance-Based Questions (PBQs) & CLI simulator
- A dedicated **🖥️ PBQ Lab** with broken topologies / troubleshooting tickets.
- A genuinely interactive **Cisco IOS CLI simulator** supporting `configure
  terminal`, `interface`, `router ospf`, `switchport trunk native vlan`,
  `channel-group … mode …`, `spanning-tree vlan … root primary`, and more — with
  realistic `show` output and authentic IOS error messages (`% Invalid input
  detected at '^' marker.`).
- **Validation checks the real resulting state** — does the EtherChannel bundle?
  is the OSPF neighbor FULL? is this switch the STP root? — so you can only pass
  by configuring the actual fix.

### 3. Diagnostic baseline & weakness remediation
- **🎯 Diagnostic Baseline**: a 30-question test (**5 per official domain**) that
  maps your starting score with a per-domain scorecard.
- An **automated remediation queue** targets every sub-topic you score **below
  80%**, feeding the Endless Drill's remediation mode.

### 4. UI & feedback loop
- Instant correct/incorrect status, **why the key is right**, **why each Cisco
  distractor is a trap**, the **exam pattern cue**, CLI verification commands, and
  a blueprint reference — on every question.
- A **📊 Progress Dashboard** with per-domain mastery, the remediation queue,
  spaced-repetition box distribution and milestone progress.

---

## Quick start

**Windows** — double-click **`run.bat`** (or run it from `cmd`). It picks up
Python, installs dependencies on first run, regenerates the question bank and
opens the app. To make a desktop shortcut, right-click `run.bat` →
*Send to* → *Desktop (create shortcut)*.

**macOS / Linux**:

```bash
./run.sh
```

**Any platform**, manually:

```bash
pip install -r requirements.txt
streamlit run Home.py
```

Then open <http://localhost:8501>, **create a login** (or sign in), and the
onboarding hub lets you take the diagnostic or jump straight into any mode. Your
progress saves to your account automatically (git-ignored, on the machine running
the app).

## Accounts, onboarding & personalized plan

- **Login:** each learner creates an account (username + password). Passwords are
  **salted and hashed** (PBKDF2-HMAC-SHA256, standard library) in
  `.userdata/users.json`; each account's progress lives under
  `.userdata/<user>/` (or `~/.ciscostudy/<user>/` for the exe). The signed-in user
  is per browser session, so several people can use one running instance at once
  without mixing progress.
- **Onboarding hub (Home):** after login, a "Where do you want to start?" screen
  links to the diagnostic, the study plan, lessons, drill and the PBQ lab.
- **🧭 My Study Plan:** the diagnostic builds a **personalized, weakest-first
  plan** — it walks you through your weak sub-topics one at a time (read the
  lesson → drill it → the next topic unlocks when you reach 80%+).

### Letting other people use it

- **Same network (no servers):** run **`run-shared.bat`** (Windows) — or
  `streamlit run Home.py --server.address 0.0.0.0` on macOS/Linux — then others on
  the same Wi-Fi/LAN open `http://<your-PC-IP>:8501` and sign in with their own
  account.
- **Separate machines:** hand each person the `.exe` or the repo.
- **Public web app:** for an internet-hosted deployment you'd move accounts and
  progress into a real database behind HTTPS (free hosts have ephemeral disks) —
  a larger change noted in PROJECT_STATUS.md.

> ⚠️ **Security note (please read if distributing).** The login is **lightweight
> auth for a study tool**, not a hardened system. `run-shared.bat` serves plain
> **HTTP** on your LAN, so passwords cross the network unencrypted. Tell users to
> pick a **throwaway password** (never a real / CAC / network password) and keep
> **no sensitive or CUI information** in the app — progress is stored in plaintext
> JSON. For anything beyond a trusted study group, put it behind HTTPS with a
> proper backend.

---

## Running the tests

The study engine is pure standard-library Python and fully unit-tested
independently of the UI:

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

This covers IP/wildcard math, data-bank integrity (every item is blueprint-tagged
and internally consistent, ≥5 per domain), grading, the adaptive scheduler, the
diagnostic baseline, the curriculum, the CLI simulator, and **every PBQ
(broken-on-build, passes only after the correct fix)**.

---

## Project layout

```
Home.py                    # Streamlit entry (login gate + onboarding hub)
pages/                     # Streamlit multipage UI
  1_Diagnostic_Baseline.py
  2_Endless_Drill.py
  3_Structured_Milestones.py
  4_PBQ_Lab.py
  5_Progress_Dashboard.py
ui_common.py               # shared Streamlit helpers (rendering, quiz runner, PBQ terminal)

studyengine/               # testable core (no Streamlit dependency)
  blueprints.py            # official domain weightings & sub-topics
  models.py                # Question / Lesson / Unit + grading
  bank.py                  # question-bank loader + queries
  grading.py               # feedback + score aggregation
  scheduler.py             # adaptive endless-drill weighting
  progress.py              # Leitner boxes, accuracy, remediation, persistence
  diagnostic.py            # 30-question baseline + focus recommendations
  curriculum.py            # units/lessons/milestones + cumulative exams
  cli_sim/                 # IOS CLI simulator + PBQ engine
    netutils.py            #   IPv4 / wildcard math
    device.py              #   device/topology model (STP/OSPF/EtherChannel behaviour)
    parser.py              #   IOS command interpreter + show renderers
    pbq.py                 #   PBQ scenarios with real-state validation

data/
  questions/ccna.json      # generated item banks (canonical, loaded at runtime)
  questions/encor.json
  curriculum/*.json        # unit/lesson/milestone structure
  lessons/**/*.md          # Markdown lessons for milestone "Read" step

tools/
  content_ccna.py          # authored CCNA item pool (edit here)
  content_encor.py         # authored ENCOR item pool (edit here)
  build_content.py         # validates + regenerates data/questions/*.json

tests/                     # pytest suite
```

---

## Extending the content

1. Add/edit questions in `tools/content_ccna.py` or `tools/content_encor.py`
   (each item follows the documented schema).
2. Regenerate and validate the banks:
   ```bash
   python tools/build_content.py
   ```
   It enforces blueprint tagging, option/key consistency, and ≥5 items per
   domain, failing loudly on a bad edit.
3. Add lessons as Markdown under `data/lessons/<exam>/` and reference them from
   `data/curriculum/<exam>.json`.
4. Add PBQ scenarios in `studyengine/cli_sim/pbq.py` (build a topology, write a
   ticket, and a validation function that inspects real resulting state).
5. `python -m pytest -q` to confirm everything still holds.
