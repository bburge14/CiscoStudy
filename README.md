# CertStack

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

- **Login:** username + password, salted and hashed (PBKDF2-HMAC-SHA256, stdlib)
  in `.userdata/users.json`. Per-account progress lives under `.userdata/<user>/`
  (or `~/.ciscostudy/<user>/` for the exe). The signed-in user is per browser
  session, so one instance serves multiple users without mixing progress. The
  first account (or `default`) is the instructor/admin; see the Instructor view
  for the roster and account management.
- **Onboarding hub (Home):** after login, a "where to start?" screen linking to
  the diagnostic, study plan, lessons, drill, PBQ lab and exam simulation.
- **🧭 My Study Plan:** the diagnostic builds a weakest-first plan that walks you
  through weak sub-topics one at a time (read → drill → unlock at 80%+).

**Multi-user:** `run-shared.bat` (or `streamlit run Home.py
--server.address 0.0.0.0`) serves it on the LAN. Auth is lightweight (plain HTTP,
plaintext-JSON progress) — fine for a study tool, use throwaway passwords. For a
real internet deployment, move accounts/progress to a database behind HTTPS.

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
Home.py                    # Streamlit entry: login gate, account menu, nav router
views/                     # one module per page (st.navigation targets)
  home.py                  #   onboarding hub / dashboard
  diagnostic.py            #   30-question baseline
  study_plan.py            #   guided weakest-first plan
  drill.py                 #   endless adaptive drill
  exam_sim.py              #   timed pass/fail mock exam
  milestones.py            #   lessons + milestone exams + PBQ gate
  open_book.py             #   open-book practice (find the answer in the book; help level scales XP)
  pbq_lab.py               #   hands-on Cisco IOS CLI lab
  progress.py              #   mastery dashboards
  account.py               #   self-service account editing (login / name / password)
  instructor.py            #   roster + account management (instructors only)
ui_common.py               # shared Streamlit helpers (auth, rendering, quiz runner, PBQ terminal)
ui_icons.py                # original network-glyph SVG icon set (nav + page headers)

studyengine/               # testable core (no Streamlit dependency)
  blueprints.py            # official domain weightings & sub-topics
  models.py                # Question / Lesson / Unit + grading
  bank.py                  # question-bank loader + queries
  grading.py               # feedback + score aggregation
  scheduler.py             # adaptive endless-drill weighting
  progress.py              # Leitner boxes, accuracy, remediation, persistence
  diagnostic.py            # 30-question baseline + focus recommendations
  curriculum.py            # units/lessons/milestones + cumulative exams
  studyplan.py             # weakest-first study plan + mastery tracking
  exam.py                  # timed mock exam builder + readiness estimate
  leveling.py              # XP + rank levels derived from profile progress
  cli_sim/                 # IOS CLI simulator + PBQ engine
    netutils.py            #   IPv4 / wildcard math
    device.py              #   device/topology model (STP/OSPF/EtherChannel behaviour)
    parser.py              #   IOS command interpreter + show renderers
    pbq.py                 #   PBQ scenarios with real-state validation
    diagram.py             #   hand-drawn SVG topology diagrams

data/
  questions/ccna.json      # generated item banks (canonical, loaded at runtime)
  questions/encor.json
  curriculum/*.json        # unit/lesson/milestone structure
  lessons/**/*.md          # Markdown lessons for milestone "Read" step

tools/
  content_ccna.py          # authored CCNA item pool (edit here)
  content_ccna_2.py        # CCNA expansion pool (concatenated onto the above)
  content_encor.py         # authored ENCOR item pool (edit here)
  content_encor_2.py       # ENCOR expansion pool (concatenated onto the above)
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
