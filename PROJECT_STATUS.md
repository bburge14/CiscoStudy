# PROJECT_STATUS

_Last updated: 2026-11-04_

## What this is
A local Streamlit study & diagnostic platform for CCNA 200-301 and CCNP ENCOR
350-401. Core study logic is a standalone, unit-tested Python package
(`studyengine`); the UI is a Streamlit multipage app.

## Current state — complete and working

| Area | Status |
|------|--------|
| Exam blueprints (domains + weights + sub-topics) | ✅ CCNA & ENCOR |
| Question bank | ✅ 82 original items (CCNA 47, ENCOR 35), all domains ≥5 |
| Diagnostic baseline (30 Q, 5/domain) + focus recs | ✅ |
| Endless Drill (adaptive, Leitner miss-boost, remediation mode) | ✅ |
| Structured Milestones (Read → Lesson Quiz → Milestone exam + PBQ, unit unlock) | ✅ |
| Lessons (Markdown) | ✅ 22 lessons (14 CCNA, 8 ENCOR) |
| CLI simulator (IOS subset + realistic `show` + IOS errors) | ✅ |
| PBQ engine with real-state validation | ✅ 11 scenarios (8 CCNA, 3 ENCOR) |
| PBQ topology diagrams | ✅ generated from the live topology (Graphviz), no copyrighted art |
| Progress dashboard + persistence | ✅ per-account, auto-saved |
| Accounts & login | ✅ username/password, PBKDF2-salted-hashed, per-account storage |
| Onboarding hub | ✅ login gate + "where to start?" Home (Home.py) with page links |
| Personalized study plan | ✅ weakest-first, enforced order, read→drill→unlock (studyplan.py) |
| Instructor view | ✅ first account = instructor; roster + per-learner drill-down (gated) |
| Launchers | ✅ `run.sh`, `run.bat`, `run-shared.bat` (LAN), exe |
| Test suite | ✅ 171 tests passing |

Run: `run.bat` (Windows) / `./run.sh` (macOS/Linux) / `streamlit run Home.py`.
Test: `python -m pytest -q`.

PBQ scenarios: native-VLAN mismatch, EtherChannel on/active, OSPF area mismatch,
STP root election, access-VLAN, trunk allowed-VLAN pruning, OSPF passive-interface,
OSPF wildcard/network mismatch (CCNA); OSPF MTU/EXSTART, EtherChannel LACP-vs-PAgP,
L3 routed-port uplink (ENCOR).

## How the content pipeline works
- Questions are **authored** in `tools/content_ccna.py` / `tools/content_encor.py`
  as Python dicts (safer than hand-written JSON, allows triple-quoted exhibits).
- `python tools/build_content.py` **validates** them (blueprint tags,
  option/key/distractor consistency, ≥5 per domain) and **emits** the canonical
  `data/questions/*.json` that the engine loads at runtime.
- `tests/test_data_integrity.py` re-checks the generated banks in CI/pytest, so a
  bad edit fails there too.

## Design decisions / gotchas
- **Authenticity, not braindumps.** All items/lessons/labs are original content
  aligned to the public blueprints and real IOS behaviour. Do **not** paste in
  real exam items — it's a copyright/NDA violation and defeats the point.
- **Engine ↔ UI split.** `studyengine` has **no Streamlit import**, so it's fully
  testable with pytest. UI-only helpers live in `ui_common.py`. Keep it that way.
- **Adaptive frequency** = Leitner boxes in `progress.py`. A miss drops the box to
  1 (weight 8); correct answers climb toward box 5 (weight 1). The scheduler also
  multiplies by domain blueprint weight and a sub-topic weakness factor.
- **Milestone exams are cumulative** (`curriculum.milestone_exam`) and capped at
  `min(size, pool)`, so early units don't fail for lack of a 30-item pool.
- **PBQ validation inspects real state** (adjacency/bundle/root election), not
  keystrokes — see `cli_sim/device.py` for the protocol logic and `pbq.py` for
  scenarios. When adding a PBQ, add a matching entry to `tests/test_pbq.py`
  (`FIXES`) proving broken-on-build → passes-after-fix.
- **CLI simulator scope is bounded** on purpose (VLAN/trunk/STP/EtherChannel/OSPF
  essentials). Unknown input returns an authentic IOS caret error rather than
  silently passing. Extend handlers in `cli_sim/parser.py` and model state in
  `cli_sim/device.py` together.
- **Persistence** is per-exam JSON under `.userdata/` (git-ignored). Streamlit
  session_state holds the live profile; it saves after each answer.
- **Streamlit version**: pinned `>=1.66,<2.0`. Uses `width="stretch"` (not the
  deprecated `use_container_width`).

## Possible next steps (not yet done)
- Grow the item banks further (the architecture scales — just add to the `tools/`
  content modules and rebuild). Some sub-topics have blueprint entries but no
  items yet (e.g. CCNA `dns`, ENCOR `machine_learning_ai`).
- More PBQ scenarios (HSRP failover, ACL placement, BGP next-hop) — note these
  need new state/commands in the simulator (HSRP, `ip route`, BGP are not modelled yet).
- Timed exam mode and a weak-area "exam readiness" score.
- Export/import of a profile's progress.
- **Internet-hosted multi-user**: the current per-profile JSON files work for a
  local or LAN-shared instance (each browser session picks a profile). For a
  public deployment (e.g. Streamlit Community Cloud, which has an ephemeral disk)
  this needs a real datastore (SQLite on an always-on server, or Postgres) and
  optional per-user authentication — a deliberate, larger change.
