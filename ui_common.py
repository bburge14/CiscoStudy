"""Shared Streamlit helpers: data loading, profile persistence, question rendering.

Kept UI-only; all study logic lives in the `studyengine` package so it stays
testable without Streamlit.
"""
from __future__ import annotations

import binascii
import hashlib
import hmac
import json
import os
import random
import re
import sys
import time
from pathlib import Path

import streamlit as st

from studyengine import (
    DrillScheduler,
    Feedback,
    get_blueprint,
    grade,
    load_bank,
    load_curriculum,
    score_session,
)
from studyengine.cli_sim import Console, topology_dot
from studyengine.models import Question
from studyengine.progress import BOX_WEIGHT, Profile

ROOT = Path(__file__).resolve().parent
if getattr(sys, "frozen", False):
    # Packaged .exe: the bundle is extracted to a temp dir that is wiped on
    # exit, so keep learner progress in a stable, writable per-user folder.
    USERDATA = Path(os.environ.get("CISCOSTUDY_DATA") or (Path.home() / ".ciscostudy"))
else:
    USERDATA = ROOT / ".userdata"
EXAMS = {"ccna": "CCNA 200-301", "encor": "CCNP ENCOR 350-401"}
PASS_THRESHOLD = 0.8


# --- cached immutable resources --------------------------------------------
@st.cache_resource
def get_bank():
    return load_bank()


@st.cache_resource
def get_curriculum():
    return load_curriculum()


# --- learner profiles -------------------------------------------------------
# Each person gets their own profile folder under USERDATA, so one running
# instance (local or shared on a network) tracks every learner separately.
def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
    return s or "learner"


def _registry_path() -> Path:
    return USERDATA / "users.json"


def _save_registry(reg: dict) -> None:
    try:
        _registry_path().write_text(json.dumps(reg, indent=2), encoding="utf-8")
    except Exception:
        pass


def _load_registry() -> dict:
    USERDATA.mkdir(parents=True, exist_ok=True)
    reg: dict = {}
    p = _registry_path()
    if p.exists():
        try:
            reg = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            reg = {}
    # Back-compat: migrate legacy single-user profile_*.json into a "default" profile.
    legacy = list(USERDATA.glob("profile_*.json"))
    if legacy:
        d = USERDATA / "default"
        d.mkdir(exist_ok=True)
        for f in legacy:
            target = d / f.name
            try:
                f.rename(target) if not target.exists() else f.unlink()
            except Exception:
                pass
        reg.setdefault("default", {"name": "Default", "created": time.time()})
    # Register any profile folders that exist on disk but not yet in the registry.
    for sub in USERDATA.iterdir():
        if sub.is_dir():
            reg.setdefault(sub.name, {"name": sub.name, "created": time.time()})
    # Ensure a stable instructor: the "default" admin account is always the
    # instructor; otherwise promote the earliest-created real account.
    accounts = {s: e for s, e in reg.items() if e.get("hash")}
    if accounts.get("default") and accounts["default"].get("role") != "instructor":
        reg["default"]["role"] = "instructor"
    elif accounts and "default" not in accounts and not any(
            e.get("role") == "instructor" for e in accounts.values()):
        first = min(accounts.items(), key=lambda kv: kv[1].get("created", 0.0))[0]
        reg[first]["role"] = "instructor"
    _save_registry(reg)
    return reg


def list_users() -> dict:
    return _load_registry()


def create_user(name: str) -> str:
    slug = _slugify(name)
    reg = _load_registry()
    reg.setdefault(slug, {"name": str(name).strip() or slug, "created": time.time()})
    _save_registry(reg)
    (USERDATA / slug).mkdir(parents=True, exist_ok=True)
    return slug


# --- authentication (lightweight: separates each learner's saved progress) --
def _hash_pw(password: str, salt: bytes | None = None) -> tuple[str, str]:
    salt = salt or os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 120_000)
    return binascii.hexlify(salt).decode(), binascii.hexlify(dk).decode()


def _verify_pw(password: str, salt_hex: str, hash_hex: str) -> bool:
    try:
        salt = binascii.unhexlify(salt_hex)
    except Exception:
        return False
    _, calc = _hash_pw(password, salt)
    return hmac.compare_digest(calc, hash_hex)


def _any_instructor(reg: dict) -> bool:
    return any(e.get("role") == "instructor" for e in reg.values())


def is_instructor(slug: str) -> bool:
    return _load_registry().get(slug, {}).get("role") == "instructor"


def create_account(username: str, password: str, display_name: str | None = None):
    """Return (slug, None) on success, or (None, error_message).

    The first account created on an instance becomes its instructor; the rest
    are learners."""
    username = (username or "").strip()
    if not username:
        return None, "Enter a username."
    if len(password or "") < 4:
        return None, "Password must be at least 4 characters."
    slug = _slugify(username)
    reg = _load_registry()
    if reg.get(slug, {}).get("hash"):
        return None, "That username is already taken."
    salt, h = _hash_pw(password)
    entry = reg.setdefault(slug, {})
    role = entry.get("role") or ("instructor" if not _any_instructor(reg) else "learner")
    entry.update({
        "name": (display_name or username).strip() or slug,
        "username": username, "salt": salt, "hash": h, "role": role,
        "created": entry.get("created", time.time()),
    })
    _save_registry(reg)
    (USERDATA / slug).mkdir(parents=True, exist_ok=True)
    return slug, None


def authenticate(username: str, password: str):
    slug = _slugify(username or "")
    entry = _load_registry().get(slug)
    if entry and entry.get("hash") and _verify_pw(password or "", entry.get("salt", ""), entry["hash"]):
        return slug
    return None


def passwordless_profiles() -> dict:
    """Legacy profiles (e.g. 'default') that hold data but have no password yet."""
    return {s: e for s, e in _load_registry().items() if not e.get("hash")}


def claim_profile(slug: str, password: str, display_name: str | None = None):
    """Set a password on an existing password-less profile, keeping its data."""
    if len(password or "") < 4:
        return None, "Password must be at least 4 characters."
    reg = _load_registry()
    if slug not in reg:
        return None, "That profile no longer exists."
    if reg[slug].get("hash"):
        return None, "That profile already has a password."
    salt, h = _hash_pw(password)
    reg[slug].update({"salt": salt, "hash": h})
    if "role" not in reg[slug]:
        reg[slug]["role"] = "instructor" if not _any_instructor(reg) else "learner"
    if display_name:
        reg[slug]["name"] = display_name.strip() or reg[slug].get("name", slug)
    _save_registry(reg)
    return slug, None


# --- instructor account management -------------------------------------------
def set_role(slug: str, role: str) -> bool:
    reg = _load_registry()
    if slug not in reg:
        return False
    reg[slug]["role"] = "instructor" if role == "instructor" else "learner"
    _save_registry(reg)
    return True


def admin_create_account(username: str, password: str, role: str = "learner"):
    """Instructor creates an account for someone else (no auto-login)."""
    slug, err = create_account(username, password)
    if err:
        return None, err
    set_role(slug, role)
    return slug, None


def set_password_admin(slug: str, password: str):
    if len(password or "") < 4:
        return False, "Password must be at least 4 characters."
    reg = _load_registry()
    if slug not in reg:
        return False, "No such account."
    salt, h = _hash_pw(password)
    reg[slug].update({"salt": salt, "hash": h})
    _save_registry(reg)
    return True, None


def delete_account(slug: str) -> bool:
    import shutil
    reg = _load_registry()
    reg.pop(slug, None)
    _save_registry(reg)
    shutil.rmtree(USERDATA / slug, ignore_errors=True)
    return True


def current_user() -> str:
    return st.session_state.get("auth_user") or "default"


def load_user_profile(slug: str, exam: str) -> Profile:
    return Profile.load(USERDATA / slug / f"profile_{exam}.json", exam)


def roster_summary(exam: str) -> list[dict]:
    """Per-account progress snapshot for the instructor view."""
    reg = _load_registry()
    rows: list[dict] = []
    for slug, meta in reg.items():
        prof = load_user_profile(slug, exam)
        seen, correct = prof.overall()
        weak = prof.weak_subtopics()
        last = max((s.last_seen for s in prof.q.values()), default=0.0)
        rows.append({
            "slug": slug,
            "name": meta.get("name", slug),
            "role": meta.get("role", "learner"),
            "baseline": prof.baseline["overall"] if prof.baseline else None,
            "answered": seen,
            "accuracy": round(correct / seen * 100) if seen else None,
            "milestones": len(prof.passed_milestones),
            "weak": [s for s, _, _ in weak[:3]],
            "last_seen": last,
        })
    rows.sort(key=lambda r: (r["role"] != "learner", -r["answered"]))
    return rows


# --- profile persistence (per learner) --------------------------------------
def _profile_path(exam: str) -> Path:
    return USERDATA / current_user() / f"profile_{exam}.json"


def _profile_key(exam: str) -> str:
    return f"profile_{current_user()}_{exam}"


def get_profile(exam: str) -> Profile:
    key = _profile_key(exam)
    if key not in st.session_state:
        st.session_state[key] = Profile.load(_profile_path(exam), exam)
    return st.session_state[key]


def save_profile(exam: str) -> None:
    prof = st.session_state.get(_profile_key(exam))
    if prof is not None:
        prof.save(_profile_path(exam))


def reset_profile(exam: str) -> None:
    st.session_state[_profile_key(exam)] = Profile(exam=exam)
    p = _profile_path(exam)
    if p.exists():
        p.unlink()


_STUDY_STATE_PREFIXES = ("drill_", "dx_", "ms", "lq", "lqids_", "msids_",
                         "mspbq_", "pbq_passed_", "lab_", "sched_", "profile_",
                         "plandrill_")


def _clear_session_study_state() -> None:
    for k in list(st.session_state):
        if k.startswith(_STUDY_STATE_PREFIXES):
            st.session_state.pop(k, None)


# --- shared page chrome -----------------------------------------------------
def _render_login() -> None:
    _, mid, _ = st.columns([3, 2, 3])   # centered, ~25%-width card
    with mid:
        st.title("🔐 CiscoStudy")
        st.caption("CCNA 200-301 & CCNP ENCOR 350-401 study and diagnostic tool. "
                   "Sign in so your progress saves to your own account.")
        tab_in, tab_new = st.tabs(["Sign in", "Create account"])
        with tab_in:
            with st.form("login_form"):
                u = st.text_input("Username")
                p = st.text_input("Password", type="password")
                if st.form_submit_button("Sign in", type="primary"):
                    slug = authenticate(u, p)
                    if slug:
                        _clear_session_study_state()
                        st.session_state["auth_user"] = slug
                        st.rerun()
                    else:
                        st.error("Wrong username or password.")
        with tab_new:
            with st.form("signup_form"):
                name = st.text_input("Display name", placeholder="e.g. A1C Smith")
                u = st.text_input("Username", key="su_user")
                p = st.text_input("Password", type="password", key="su_pw")
                p2 = st.text_input("Confirm password", type="password", key="su_pw2")
                if st.form_submit_button("Create account", type="primary"):
                    if p != p2:
                        st.error("Passwords don't match.")
                    else:
                        slug, err = create_account(u, p, name)
                        if err:
                            st.error(err)
                        else:
                            _clear_session_study_state()
                            st.session_state["auth_user"] = slug
                            st.rerun()

        legacy = passwordless_profiles()
        if legacy:
            with st.expander("Keep progress from an existing local profile"):
                st.caption("These profiles already have data on this machine but no password. "
                           "Set one to turn a profile into your account and keep its progress.")
                with st.form("claim_form"):
                    slug = st.selectbox("Profile", sorted(legacy),
                                        format_func=lambda s: legacy[s].get("name", s))
                    p = st.text_input("New password", type="password", key="claim_pw")
                    if st.form_submit_button("Secure & sign in"):
                        got, err = claim_profile(slug, p)
                        if err:
                            st.error(err)
                        else:
                            _clear_session_study_state()
                            st.session_state["auth_user"] = got
                            st.rerun()

        st.caption("⚠️ Lightweight login for a study tool: passwords are salted + hashed and "
                   "stored locally. Don't reuse a real / CAC / network password, and don't store "
                   "any sensitive or CUI information here.")


def _account_bar(user: str) -> None:
    """Top-right account menu (name, role, instructor tools, log out)."""
    name = _load_registry().get(user, {}).get("name", user)
    inst = is_instructor(user)
    _, acct = st.columns([6, 1])
    with acct:
        with st.popover(f"👤 {name}", use_container_width=True):
            st.markdown(f"**{name}**")
            st.caption("🧑‍🏫 Instructor" if inst else "Learner")
            if inst:
                st.page_link("pages/7_Instructor.py", label="Instructor tools", icon="🧑‍🏫")
            if st.button("Log out", key="logout_top", use_container_width=True):
                _clear_session_study_state()
                st.session_state.pop("auth_user", None)
                st.rerun()


def page_setup(title: str, icon: str = "🛜") -> str:
    st.set_page_config(page_title=f"CiscoStudy · {title}", page_icon=icon, layout="wide")
    if "exam" not in st.session_state:
        st.session_state["exam"] = "ccna"

    # --- login gate: no page renders until signed in ---
    user = st.session_state.get("auth_user")
    if not user or user not in _load_registry():
        st.session_state.pop("auth_user", None)
        _render_login()
        st.stop()

    _account_bar(user)   # account menu in the top-right

    with st.sidebar:
        st.markdown("### CiscoStudy")
        exam = st.radio(
            "Exam track",
            list(EXAMS),
            format_func=lambda e: EXAMS[e],
            index=list(EXAMS).index(st.session_state["exam"]),
            key="exam_selector",
        )
        if exam != st.session_state["exam"]:
            st.session_state["exam"] = exam
            st.rerun()

        prof = get_profile(exam)
        seen, correct = prof.overall()
        acc = f"{round(correct / seen * 100)}%" if seen else "—"
        st.metric("Questions answered", seen)
        st.metric("Lifetime accuracy", acc)
        st.caption("Progress auto-saves to your account after every answer.")
    return st.session_state["exam"]


def get_scheduler(exam: str) -> DrillScheduler:
    key = f"sched_{exam}"
    if key not in st.session_state:
        st.session_state[key] = DrillScheduler(get_bank(), exam, get_blueprint(exam),
                                               rng=random.Random())
    return st.session_state[key]


# --- question rendering -----------------------------------------------------
def render_exhibit(q: Question) -> None:
    if q.exhibit:
        st.code(q.exhibit, language="text")


def answer_widget(q: Question, key: str):
    """Render the input for a question and return the current selection."""
    render_exhibit(q)
    st.markdown(f"**{q.stem}**")
    if q.is_fill:
        return st.text_input("Your answer", key=key, placeholder="type your answer…")
    labels = {o.id: f"{o.id}.  {o.text}" for o in q.options}
    if q.type == "multi":
        st.caption(f"Select {q.select_count}.")
        return st.multiselect("Choose all that apply", options=[o.id for o in q.options],
                              format_func=lambda i: labels[i], key=key)
    return st.radio("Choose one", options=[o.id for o in q.options],
                    format_func=lambda i: labels[i], index=None, key=key)


def render_feedback(q: Question, fb: Feedback) -> None:
    key_txt = ", ".join(fb.correct_ids)
    if fb.correct:
        st.success("✅  Correct")
    else:
        st.error(f"❌  Incorrect — correct answer: **{key_txt}**")

    st.markdown("**Why the correct answer is right**")
    st.markdown(fb.why_correct)

    traps = {k: v for k, v in fb.distractor_notes.items() if v}
    if traps:
        with st.expander("Why the Cisco distractors are traps", expanded=not fb.correct):
            for oid, note in traps.items():
                st.markdown(f"- **{oid}** — {note}")

    if fb.exam_pattern:
        st.info(f"🎯  **Spot it on the exam:** {fb.exam_pattern}")

    if fb.verify_cli:
        st.markdown("**Verify on the device**")
        st.code("\n".join(fb.verify_cli), language="text")

    if fb.references:
        st.caption("Reference: " + " · ".join(fb.references))


def grade_and_record(exam: str, q: Question, selection) -> Feedback:
    fb = grade(q, selection)
    prof = get_profile(exam)
    prof.record(q, fb.correct)
    save_profile(exam)
    return fb


# --- small analytics widgets ------------------------------------------------
def domain_mastery_table(exam: str):
    prof = get_profile(exam)
    bp = get_blueprint(exam)
    stats = prof.domain_stats()
    rows = []
    for d in bp.domains:
        seen, corr, acc = stats.get(d.key, (0, 0, 0.0))
        rows.append({
            "Domain": d.name,
            "Exam weight": f"{round(d.weight * 100)}%",
            "Answered": seen,
            "Accuracy": f"{round(acc * 100)}%" if seen else "—",
        })
    return rows


def box_distribution(exam: str) -> dict[int, int]:
    prof = get_profile(exam)
    dist = {b: 0 for b in BOX_WEIGHT}
    for st_ in prof.q.values():
        dist[st_.box] = dist.get(st_.box, 0) + 1
    return dist


# --- reusable quiz runner ---------------------------------------------------
def reset_quiz(skey: str) -> None:
    st.session_state.pop(skey, None)


def run_quiz(exam: str, skey: str, question_ids: list[str], instant: bool = False):
    """Drive a quiz/exam stored in session_state[skey].

    Records each answered item into the profile exactly once. Returns
    ("empty"|"in_progress"|"done", SessionScore|None). With instant=True the
    learner gets per-question feedback (lesson quizzes); with instant=False
    answers are graded at the end (milestone exams).
    """
    bank = get_bank()
    prof = get_profile(exam)
    bp = get_blueprint(exam)
    state = st.session_state.setdefault(
        skey, {"idx": 0, "answers": {}, "phase": "answering", "done": False, "fb": None}
    )
    total = len(question_ids)
    if total == 0:
        st.info("No questions available for this selection yet.")
        return ("empty", None)

    if state["done"]:
        attempts = [(qid, bank.get(qid).check(state["answers"].get(qid))) for qid in question_ids]
        return ("done", score_session(attempts, bank))

    idx = state["idx"]
    q = bank.get(question_ids[idx])
    st.progress(idx / total, text=f"Question {idx + 1} of {total}")
    st.caption(f"Domain: {bp.domain(q.domain).name}  ·  {q.subtopic.replace('_', ' ')}")

    if instant and state["phase"] == "feedback":
        render_feedback(q, state["fb"])
        label = "See results ▶" if idx == total - 1 else "Next ▶"
        if st.button(label, key=f"{skey}_next", type="primary"):
            if idx + 1 >= total:
                state["done"] = True
            else:
                state["idx"] += 1
                state["phase"] = "answering"
            st.rerun()
        return ("in_progress", None)

    sel = answer_widget(q, key=f"{skey}_ans_{idx}")
    submit_label = "Submit" if instant else ("Finish" if idx == total - 1 else "Next ▶")
    if st.button(submit_label, key=f"{skey}_submit", type="primary"):
        state["answers"][q.id] = sel
        fb = grade(q, sel)
        prof.record(q, fb.correct)
        save_profile(exam)
        if instant:
            state["fb"] = fb
            state["phase"] = "feedback"
        elif idx + 1 >= total:
            state["done"] = True
        else:
            state["idx"] += 1
        st.rerun()
    return ("in_progress", None)


# --- reusable PBQ terminal --------------------------------------------------
def render_pbq(scenario, skey_prefix: str) -> bool:
    """Render a scenario's ticket, CLI terminal and validation. Returns True
    once all checks pass (also sets a cross-page flag pbq_passed_<id>)."""
    topo_key = f"{skey_prefix}_topo"
    tx_key = f"{skey_prefix}_tx"
    dev_key = f"{skey_prefix}_dev"
    cons_key = f"{skey_prefix}_cons"

    if topo_key not in st.session_state:
        st.session_state[topo_key] = scenario.build()
        st.session_state[tx_key] = []
        st.session_state[dev_key] = scenario.device
        st.session_state[cons_key] = {}

    topo = st.session_state[topo_key]
    consoles = st.session_state[cons_key]

    st.markdown(scenario.ticket)

    st.markdown("**Topology**")
    try:
        st.graphviz_chart(topology_dot(topo, scenario.device))
        st.caption("Live from the scenario — the console device is highlighted; a down link "
                   "shows red/dashed. The diagram updates as you configure.")
    except Exception:
        st.caption("(Topology diagram unavailable.)")

    with st.expander("Hints"):
        for h in scenario.hints:
            st.markdown(f"- {h}")

    devices = list(topo.devices)
    dev = st.selectbox("Console device", devices,
                       index=devices.index(st.session_state[dev_key]),
                       key=f"{skey_prefix}_devsel",
                       help="You may inspect peer devices; fix the one named in the ticket.")
    st.session_state[dev_key] = dev
    if dev not in consoles:
        consoles[dev] = Console(topo, dev)
    con = consoles[dev]

    # transcript
    lines = []
    for p, c, o in st.session_state[tx_key]:
        lines.append(f"{p} {c}")
        if o:
            lines.append(o)
    lines.append(con.prompt)
    st.code("\n".join(lines) or con.prompt, language="text")

    with st.form(f"{skey_prefix}_form", clear_on_submit=True):
        cmd = st.text_input("Enter IOS command", placeholder="e.g. configure terminal",
                            label_visibility="collapsed")
        cols = st.columns([1, 1, 6])
        run = cols[0].form_submit_button("Run ▶", type="primary")
        clear = cols[1].form_submit_button("Reset lab")
    if run and cmd.strip():
        prompt_before = con.prompt
        out = con.execute(cmd)
        st.session_state[tx_key].append((prompt_before, cmd, out))
        st.rerun()
    if clear:
        for k in (topo_key, tx_key, dev_key, cons_key):
            st.session_state.pop(k, None)
        st.session_state.pop(f"pbq_passed_{scenario.id}", None)
        st.rerun()

    passed = False
    if st.button("Validate ticket ✔", key=f"{skey_prefix}_validate"):
        checks = scenario.validate(topo)
        for c in checks:
            (st.success if c.passed else st.error)(
                f"{'✅' if c.passed else '❌'}  {c.description}")
        if all(c.passed for c in checks):
            passed = True
            st.session_state[f"pbq_passed_{scenario.id}"] = True
            st.success(f"🎉  {scenario.success}")
            st.balloons()
        else:
            st.warning("Not resolved yet — review the failed checks above and the hints.")
    return passed or st.session_state.get(f"pbq_passed_{scenario.id}", False)
