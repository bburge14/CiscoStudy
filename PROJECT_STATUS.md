# PROJECT_STATUS

_Last updated: 2026-11-06_

## What this is
**CertWize** — a Streamlit study & diagnostic platform for IT certifications. The
engine is data-driven by exam blueprints, so adding a cert = a new blueprint + a
question bank (no engine changes). Live tracks (all selectable in the picker):
**CCNA 200-301**, **CCNP ENCOR 350-401**, **CompTIA Security+ SY0-701**, **Network+
N10-009**, **A+ Core 1 (220-1101)** and **A+ Core 2 (220-1102)**. (The AWS Cloud
Practitioner catalog tile stays "coming soon" — no blueprint yet.) Core study logic
is a standalone, unit-tested Python package (`studyengine`); the UI is a Streamlit
multipage app driven by a native `st.navigation` router (`Home.py`) with one module
per page under `views/`.

The whole UI uses ONE cohesive custom glyph set (`ui_icons.py`) — no emoji / Material
defaults anywhere in the app body — and recolors per track (see "per-track accent").

## Current state — complete and working

| Area | Status |
|------|--------|
| Exam blueprints (domains + weights + sub-topics) | ✅ 6 live: CCNA, ENCOR, Security+, Network+, A+ Core 1, A+ Core 2 |
| Question bank | ✅ 1,230 original items — every track at CCNA depth: CCNA 205, ENCOR 205, Security+ 205, Network+ 205, A+ Core 1 205, A+ Core 2 205 (~30–41/domain). Built as per-domain/round expansion pools (`content_<track>_*.py`, `-r2-` ID segments) auto-merged by the build glob |
| Track picker | ✅ sidebar **dropdown** lists every track; unbuilt ones show "· coming soon" and are non-selectable (revert + notice) |
| Per-track accent theme | ✅ each track has its own accent (Cisco blue/violet, Security+ green, Network+ teal, A+ amber/rose); header glyphs, level card, progress bars, primary buttons recolor to the active track (`TRACK_ACCENT` + `_theme_css`) |
| Diagnostic baseline (30 Q, 5/domain) + focus recs | ✅ |
| Endless Drill (adaptive, Leitner miss-boost, remediation mode) | ✅ + per-domain focus filter + Skip |
| Structured Milestones (Read → Lesson Quiz → Milestone exam + PBQ, unit unlock) | ✅ all 6 tracks; lesson quiz = instant feedback; milestone exam = graded at end + full after-quiz review (missed-first); milestone unlock gated on a PBQ (Cisco CLI or CompTIA interactive) |
| Open-Book Practice (real open-book: find the answer yourself) | ✅ 3 help levels (Full book / General area / Pinpoint); correct earns less the more help you took (100/70/40%); a miss is free with the book shut, else costs — scaled up by help (Pinpoint worst); book resets per question |
| Lessons (Markdown) | ✅ 68 lessons across all 6 tracks (14 CCNA, 8 ENCOR, 13 Security+, 11 Network+, 11 A+ Core 1, 11 A+ Core 2); every blueprint sub-topic covered |
| CLI simulator (IOS subset + realistic `show` + IOS errors) | ✅ |
| PBQ engine — Cisco CLI | ✅ 11 real-state-validated scenarios (8 CCNA, 3 ENCOR) |
| PBQ engine — CompTIA interactive | ✅ `studyengine/perf.py`: categorize / match / order tasks, **32 authored (8 per CompTIA track)**, graded against the key; served in PBQ Lab and as milestone gates (`render_any_pbq` dispatches by pbq_id). Real **drag-and-drop** via a custom component (`components/dragdrop/`), with a dropdown fallback |
| PBQ topology diagrams | ✅ hand-drawn inline SVG from the live topology (router/switch/L3 device icons, down-link + console highlighting), no copyrighted art |
| Progress dashboard + persistence | ✅ per-account, auto-saved; mastery-by-domain chart on a fixed 0–100 axis |
| Accounts & login | ✅ username/password, PBKDF2-salted-hashed, per-account storage |
| Onboarding hub | ✅ login gate + "where to start?" Home with role-aware sidebar nav (`st.navigation` router) |
| Custom icon set | ✅ original monochrome SVG glyph set (`ui_icons.py`) used EVERYWHERE — nav (CSS mask), page headers, card/section headers, status chips, XP badges — via `ui_icons.inline()` / `ui_common.glyph()` / `section_header()`. No emoji or Material defaults in the app body (only inline ✓/● text marks survive in dropdown/dataframe cells where SVG can't render) |
| Sidebar layout | ✅ brand wordmark + track dropdown + rank card pinned ABOVE the nav links (CSS `order` on `stSidebarContent`), then the custom-glyph nav |
| Self-service account page | ✅ change your display name, login/username (keeps progress), and password; last-instructor guard |
| Personalized study plan | ✅ weakest-first, enforced order, read→drill→unlock (studyplan.py) |
| Exam simulation | ✅ timed (native per-second countdown), domain-weighted, one-at-a-time (no back), pass/fail report (exam.py) |
| Exam readiness estimate | ✅ weighted practice accuracy + coverage + verdict (on dashboard) |
| XP / leveling | ✅ 9 ranks, event-based XP (Profile.record_study): rewards getting better (improving/mastering items) + streaks; penalizes misses with per-question escalation — missing the SAME item again and again costs more (−6 → −9 → −12 → −15 floor), a correct answer resets the chain; no credit for mere attempts; steep curve (Level 2 ≈ 30–50 correct answers). Benchmark excluded (study_overall). Home card, sidebar badge, +/−XP + streak chip on each answer |
| Instructor view | ✅ first account = instructor; roster, per-learner drill-down, account management (create/edit name+login/reset password/role/delete), and reset a learner's status (benchmark only, or all progress); nav entry hidden from learners |
| Launchers | ✅ `run.sh`, `run.bat`, `run-shared.bat` (LAN), exe |
| Test suite | ✅ 1417 tests passing (+ router/page AppTest smoke) |

Run: `run.bat` (Windows) / `./run.sh` (macOS/Linux) / `streamlit run Home.py`.
Test: `python -m pytest -q`.

PBQ scenarios: native-VLAN mismatch, EtherChannel on/active, OSPF area mismatch,
STP root election, access-VLAN, trunk allowed-VLAN pruning, OSPF passive-interface,
OSPF wildcard/network mismatch (CCNA); OSPF MTU/EXSTART, EtherChannel LACP-vs-PAgP,
L3 routed-port uplink (ENCOR).

## How the content pipeline works
- Questions are **authored** in `tools/content_<track>.py` (ccna, encor, secplus,
  netplus, aplus1, aplus2; optional `_2` expansion pools) as Python dicts (safer
  than hand-written JSON, allows triple-quoted exhibits).
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
- Export/import of a profile's progress.
- **Internet-hosted multi-user**: the current per-profile JSON files work for a
  local or LAN-shared instance (each browser session picks a profile). For a
  public deployment (e.g. Streamlit Community Cloud, which has an ephemeral disk)
  this needs a real datastore (SQLite on an always-on server, or Postgres) and
  optional per-user authentication — a deliberate, larger change.
