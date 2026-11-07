"""Shared Streamlit helpers: data loading, profile persistence, question rendering.

Kept UI-only; all study logic lives in the `studyengine` package so it stays
testable without Streamlit.
"""
from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import html
import json
import os
import random
import re
import sys
import time
from pathlib import Path

import streamlit as st

import ui_icons
from studyengine import (
    DrillScheduler,
    Feedback,
    get_blueprint,
    grade,
    load_bank,
    load_curriculum,
    profile_level,
    score_session,
)
from studyengine.blueprints import EXAMS as _BLUEPRINTS, LIVE_EXAMS
from studyengine.cli_sim import Console, topology_svg
from studyengine.models import Question
from studyengine.perf import get_perf_task, is_perf_task, perf_tasks_for  # noqa: F401
from studyengine.progress import BOX_WEIGHT, Profile

ROOT = Path(__file__).resolve().parent
# CISCOSTUDY_DATA wins everywhere so a hosted deploy can point progress at a
# persistent disk (e.g. CISCOSTUDY_DATA=/var/data); packaged .exe falls back to
# a stable per-user folder; local dev uses ./.userdata next to the code.
if os.environ.get("CISCOSTUDY_DATA"):
    USERDATA = Path(os.environ["CISCOSTUDY_DATA"])
elif getattr(sys, "frozen", False):
    USERDATA = Path.home() / ".ciscostudy"
else:
    USERDATA = ROOT / ".userdata"
# Display names for the tracks that are live (have a question bank). Derived from
# the blueprints so adding a track in one place lights it up across the UI.
EXAMS = {code: _BLUEPRINTS[code].name for code in LIVE_EXAMS}

# The certification catalog — the multi-track vision shown on the home landing.
# Tracks with status "active" have real content (keys match EXAMS); "soon" tracks
# render as coming-soon placeholders until their content is built.
CERT_CATALOG = [
    {"provider": "Cisco", "blurb": "Routing, switching & enterprise networking", "certs": [
        {"key": "ccna", "name": "CCNA 200-301", "status": "active"},
        {"key": "encor", "name": "CCNP ENCOR 350-401", "status": "active"},
    ]},
    {"provider": "CompTIA", "blurb": "Vendor-neutral IT foundations", "certs": [
        {"key": "secplus", "name": "Security+ SY0-701", "status": "active"},
        {"key": "netplus", "name": "Network+ N10-009", "status": "active"},
        {"key": "aplus1", "name": "A+ Core 1 (220-1101)", "status": "active"},
        {"key": "aplus2", "name": "A+ Core 2 (220-1102)", "status": "active"},
    ]},
    {"provider": "AWS", "blurb": "Cloud fundamentals & architecture", "certs": [
        {"key": "clf", "name": "Cloud Practitioner", "status": "soon"},
    ]},
]
PASS_THRESHOLD = 0.8

# --- per-track accent theming ----------------------------------------------
# Every track gets its own accent so the whole app recolors to the cert you're
# studying — primary buttons, progress bars, header glyphs and highlights all
# follow the track. The CertWize wordmark keeps its brand blue; everything
# contextual follows the selected certification.
TRACK_ACCENT = {
    "ccna":    "#4D8DFF",   # Cisco — blue
    "encor":   "#8B7CF6",   # Cisco pro — violet
    "secplus": "#22C58B",   # CompTIA Security+ — green
    "netplus": "#2BB6CC",   # CompTIA Network+ — teal
    "aplus1":  "#E8913A",   # CompTIA A+ Core 1 — amber
    "aplus2":  "#E86A8B",   # CompTIA A+ Core 2 — rose
}


def accent_for(exam: str) -> str:
    return TRACK_ACCENT.get(exam, ui_icons.BRAND)


def current_accent() -> str:
    return accent_for(st.session_state.get("exam", "ccna"))


def glyph(key: str, size: int = 18, color: str | None = None) -> str:
    """Inline custom-glyph markup, tinted to the current track accent by default."""
    return ui_icons.inline(key, size=size, color=color or current_accent())


def section_header(key: str, text: str, size: float = 1.3) -> None:
    """A custom-glyph section heading — the cohesive replacement for an
    emoji-prefixed st.subheader()."""
    st.markdown(
        f"<div style='display:flex;align-items:center;margin:.55rem 0 .4rem;"
        f"font-weight:700;font-size:{size}rem;letter-spacing:-.01em'>"
        f"{ui_icons.inline(key, round(size * 17), current_accent())}"
        f"<span>{html.escape(text)}</span></div>",
        unsafe_allow_html=True,
    )


def _theme_css(accent: str) -> str:
    """Recolor Streamlit's primary-colored chrome (buttons, progress, links,
    sliders, toggles) to the active track's accent, via one injected style block."""
    return (
        "<style>"
        f":root{{--cw-accent:{accent};}}"
        # primary buttons
        'button[kind="primary"],[data-testid="stBaseButton-primary"]{'
        'background-color:var(--cw-accent)!important;border-color:var(--cw-accent)!important;}'
        'button[kind="primary"]:hover,[data-testid="stBaseButton-primary"]:hover{'
        'filter:brightness(1.08);}'
        # progress-bar fill
        '[data-testid="stProgress"] div[role="progressbar"]>div,'
        '.stProgress div[role="progressbar"]>div{background-color:var(--cw-accent)!important;}'
        # links
        '.stMarkdown a{color:var(--cw-accent);}'
        "</style>"
    )


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


def _count_instructors(reg: dict) -> int:
    return sum(1 for e in reg.values() if e.get("role") == "instructor")


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
    new_role = "instructor" if role == "instructor" else "learner"
    # Keep at least one instructor on the instance.
    if (new_role == "learner" and reg[slug].get("role") == "instructor"
            and _count_instructors(reg) <= 1):
        return False
    reg[slug]["role"] = new_role
    _save_registry(reg)
    return True


def rename_account(old_slug: str, new_username: str):
    """Change an account's login/username (its slug), carrying its saved progress.

    Returns (new_slug, None) on success or (None, error). Moves the on-disk
    profile directory and the registry entry; the caller updates auth_user."""
    import shutil
    new_username = (new_username or "").strip()
    if not new_username:
        return None, "Enter a username."
    reg = _load_registry()
    if old_slug not in reg:
        return None, "That account no longer exists."
    new_slug = _slugify(new_username)
    if new_slug == old_slug:  # casing-only tweak to the stored label
        reg[old_slug]["username"] = new_username
        _save_registry(reg)
        return old_slug, None
    if new_slug in reg:
        return None, "That username is already taken."
    old_dir, new_dir = USERDATA / old_slug, USERDATA / new_slug
    try:
        if new_dir.exists():  # orphan dir not referenced by any account
            shutil.rmtree(new_dir, ignore_errors=True)
        if old_dir.exists():
            old_dir.rename(new_dir)
    except Exception as e:  # pragma: no cover - filesystem edge
        return None, f"Could not move saved progress ({e})."
    entry = reg.pop(old_slug)
    entry["username"] = new_username
    reg[new_slug] = entry
    _save_registry(reg)
    return new_slug, None


def set_display_name(slug: str, name: str) -> bool:
    name = (name or "").strip()
    if not name:
        return False
    reg = _load_registry()
    if slug not in reg:
        return False
    reg[slug]["name"] = name
    _save_registry(reg)
    return True


def change_password(slug: str, old_password: str, new_password: str):
    """Self-service password change: verifies the current password first.
    Returns (True, None) or (False, error)."""
    if len(new_password or "") < 4:
        return False, "New password must be at least 4 characters."
    reg = _load_registry()
    entry = reg.get(slug)
    if not entry or not entry.get("hash"):
        return False, "No such account."
    if not _verify_pw(old_password or "", entry.get("salt", ""), entry["hash"]):
        return False, "Current password is incorrect."
    salt, h = _hash_pw(new_password)
    entry.update({"salt": salt, "hash": h})
    _save_registry(reg)
    return True, None


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
    if slug not in reg:
        return False
    # Never delete the instance's last instructor (it would lose its admin).
    if reg[slug].get("role") == "instructor" and _count_instructors(reg) <= 1:
        return False
    reg.pop(slug, None)
    _save_registry(reg)
    shutil.rmtree(USERDATA / slug, ignore_errors=True)
    return True


def admin_reset_progress(slug: str, exam: str) -> bool:
    """Instructor: wipe a learner's progress for one exam back to a clean slate.

    Everything the learner earned goes — mastery boxes, XP, streaks, answered
    counts, completed lessons/milestones AND the diagnostic benchmark: a fresh
    empty Profile replaces the saved one. The account itself (login, role,
    password) is untouched.
    """
    reg = _load_registry()
    if slug not in reg:
        return False
    Profile(exam=exam).save(USERDATA / slug / f"profile_{exam}.json")
    st.session_state.pop(f"profile_{slug}_{exam}", None)
    return True


def admin_reset_benchmark(slug: str, exam: str) -> bool:
    """Instructor: clear ONLY a learner's diagnostic benchmark so they can take
    it again. Study progress (boxes, XP, answered counts) is kept.

    The benchmark's recorded answers stay excluded from study metrics: we clear
    ``baseline`` (the score/"taken" flag) but keep ``baseline_stats`` (the
    accumulator ``study_overall`` subtracts). Dropping that accumulator would
    make those old benchmark answers suddenly count as study and inflate the
    answered total, accuracy and XP — exactly what the diagnostic split avoids.
    """
    reg = _load_registry()
    if slug not in reg:
        return False
    path = USERDATA / slug / f"profile_{exam}.json"
    prof = Profile.load(path, exam)
    prof.baseline = None
    prof.save(path)
    st.session_state.pop(f"profile_{slug}_{exam}", None)
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
        seen, correct = prof.study_overall()   # benchmark excluded
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
    # Responsive centering: cap + center the login on desktop, let it fill the
    # width on a phone / portrait screen (no wasted empty side columns).
    st.markdown(
        "<style>"
        "[data-testid='stMainBlockContainer'], section.main .block-container"
        "{max-width:460px;margin-left:auto;margin-right:auto;}"
        "</style>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align:center;margin:0.75rem 0 0.25rem'>"
        "<div style='font-size:2.5rem;font-weight:800;letter-spacing:-0.02em;line-height:1'>"
        "Cert<span style='color:#4D8DFF'>Wize</span></div>"
        "<div style='color:#9AA4B2;font-size:0.98rem;margin-top:0.4rem'>"
        "Your IT certification trainer — practice, labs &amp; realistic exam sims</div></div>",
        unsafe_allow_html=True,
    )
    st.caption("<div style='text-align:center'>Sign in so your progress saves to your own account.</div>",
               unsafe_allow_html=True)
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
            name = st.text_input("Display name", placeholder="e.g. Jordan Lee")
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

    st.caption("Passwords are salted + hashed and stored locally. Lightweight auth for a "
               "study tool — use a throwaway password, not a real one.")


def ensure_login() -> bool:
    """Login gate for the router. Returns True if signed in, else renders the
    login screen and returns False (the router then st.stop()s)."""
    if "exam" not in st.session_state:
        st.session_state["exam"] = "ccna"
    user = st.session_state.get("auth_user")
    if user and user in _load_registry():
        return True
    st.session_state.pop("auth_user", None)
    _render_login()
    return False


def render_account_bar() -> None:
    """Top-right account menu (name, role, instructor tools, log out)."""
    user = current_user()
    name = _load_registry().get(user, {}).get("name", user)
    inst = is_instructor(user)
    # width="content" sizes the chip to the name so it's never clipped to "Brad…";
    # margin-left:auto on its wrapper floats it flush-right; nowrap keeps the name
    # on one line. (The app's only popover, scoped via :has to be safe.)
    st.markdown(
        "<style>"
        "[data-testid='stLayoutWrapper']:has(> [data-testid='stPopover']){margin-left:auto;}"
        "[data-testid='stPopoverButton'] p{white-space:nowrap;}"
        "</style>",
        unsafe_allow_html=True,
    )
    with st.popover(name, width="content"):
            st.markdown(f"**{name}**")
            st.caption("Instructor" if inst else "Learner")
            st.page_link("views/account.py", label="My account",
                         icon=":material/manage_accounts:")
            if inst:
                st.page_link("views/instructor.py", label="Instructor tools",
                             icon=":material/supervisor_account:")
            if st.button("Log out", key="logout_top", width="stretch"):
                _clear_session_study_state()
                st.session_state.pop("auth_user", None)
                st.rerun()


def _render_track_picker() -> None:
    """The 'Active track' dropdown. Lists every known certification; tracks whose
    content isn't built yet show as 'coming soon' and are non-selectable — picking
    one snaps the dropdown back to your current track and explains why."""
    all_tracks = list(_BLUEPRINTS)          # ccna, encor, secplus, netplus, aplus1, aplus2
    live = set(LIVE_EXAMS)
    st.session_state.setdefault("track_select", st.session_state.get("exam", "ccna"))

    def _label(k: str) -> str:
        name = _BLUEPRINTS[k].name
        return name if k in live else f"{name}   ·   coming soon"

    def _on_change() -> None:
        choice = st.session_state["track_select"]
        if choice in live:
            st.session_state["exam"] = choice
        else:   # not built yet — revert the widget and flag a note
            st.session_state["track_select"] = st.session_state.get("exam", "ccna")
            st.session_state["_track_soon"] = _BLUEPRINTS[choice].name

    st.selectbox("Active track", all_tracks, key="track_select",
                 format_func=_label, on_change=_on_change)
    soon = st.session_state.pop("_track_soon", None)
    if soon:
        st.caption(f"**{soon}** isn't ready yet — its question bank is still being built. "
                   "Live tracks switch instantly.")


def render_sidebar_chrome() -> None:
    """Sidebar: CertWize brand + track dropdown on top, the nav links below, then a
    compact rank card. Injects the custom-glyph nav icons, the per-track accent
    theme, and the centered content-width layout, and reorders the sidebar so the
    brand leads (Streamlit renders user content below the nav by default)."""
    accent = current_accent()
    st.markdown(
        "<style>"
        # a comfortable, centered main column
        "[data-testid='stMainBlockContainer'], section.main .block-container"
        "{max-width:960px;margin-left:auto;margin-right:auto;}"
        # brand + track picker + rank card ABOVE the auto-generated nav links
        "[data-testid='stSidebarContent']{display:flex;flex-direction:column;}"
        "[data-testid='stSidebarUserContent']{order:1;}"
        "[data-testid='stSidebarNav']{order:2;margin-top:.15rem;}"
        # hairline rule between the brand block and the nav
        "[data-testid='stSidebarNav']::before{content:'';display:block;height:1px;"
        "background:rgba(255,255,255,.08);margin:.1rem .25rem .5rem;}"
        "</style>",
        unsafe_allow_html=True,
    )
    st.markdown(ui_icons.nav_css(), unsafe_allow_html=True)
    st.markdown(_theme_css(accent), unsafe_allow_html=True)

    with st.sidebar:
        st.markdown(
            "<div style='font-size:1.5rem;font-weight:800;letter-spacing:-0.02em;"
            "padding:0.05rem 0 0'>Cert<span style='color:#4D8DFF'>Wize</span></div>"
            "<div style='color:#8A94A6;font-size:0.66rem;text-transform:uppercase;"
            "letter-spacing:0.12em;margin:0 0 0.6rem'>IT Certification Trainer</div>",
            unsafe_allow_html=True,
        )
        _render_track_picker()
        render_level_card(get_profile(st.session_state.get("exam", "ccna")), compact=True)


def render_level_card(prof, *, compact: bool = False) -> None:
    """Show the learner's rank + XP progress. compact=True for the sidebar."""
    li = profile_level(prof)
    if li.is_max:
        bar_text = f"Max rank · {li.xp} XP"
    else:
        bar_text = f"{li.into}/{li.span} XP → {li.next_title}"
    if compact:
        st.markdown(
            f"<div style='font-weight:700;margin:.15rem 0 .2rem'>"
            f"<span style='color:{current_accent()}'>Lvl {li.level}</span> · {html.escape(li.title)}</div>",
            unsafe_allow_html=True,
        )
        st.progress(li.pct, text=bar_text)
        return
    with st.container(border=True):
        left, right = st.columns([1, 3])
        with left:
            st.markdown(
                f"<div style='font-size:2.6rem;font-weight:800;line-height:1;color:{current_accent()}'>"
                f"{li.level}</div><div style='font-size:.7rem;letter-spacing:.08em;"
                f"opacity:.6'>LEVEL</div>",
                unsafe_allow_html=True,
            )
        with right:
            st.markdown(f"#### {li.title}")
            st.progress(li.pct, text=bar_text)
    st.caption("XP rewards getting answers **right**, building **streaks**, and **mastering** "
               "topics — missing costs you (more if you had it down), and the diagnostic doesn't "
               "count. Your rank reflects how much you've actually learned, not how many "
               "questions you've clicked.")


def page_setup(title: str | None = None, icon: str | None = None) -> str:
    """Pages call this for the selected exam track. The login gate, account bar,
    sidebar and page config are rendered once by the router (Home.py)."""
    return st.session_state.get("exam", "ccna")


def page_header(icon_key: str, title: str) -> None:
    """Render a page title with a custom glyph, tinted to the active track accent."""
    st.html(ui_icons.header_html(icon_key, title, current_accent()))


def get_scheduler(exam: str) -> DrillScheduler:
    key = f"sched_{exam}"
    if key not in st.session_state:
        st.session_state[key] = DrillScheduler(get_bank(), exam, get_blueprint(exam),
                                               rng=random.Random())
    return st.session_state[key]


# --- question rendering -----------------------------------------------------
def _svg_img_tag(svg: str, max_width: int = 720) -> str:
    """Wrap an SVG string as a base64 data-URI <img> tag.

    st.html() and st.markdown() both run their input through an HTML sanitizer
    that strips raw <svg> markup, so a diagram passed directly would silently
    vanish (no error — just a blank gap). A data-URI <img> sidesteps the
    sanitizer entirely: the browser's image engine renders the SVG, which stays
    responsive and inline (no fixed-height iframe)."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b64}" alt="Network topology diagram" '
            f'style="width:100%;max-width:{max_width}px;height:auto;display:block;margin:0.25rem 0"/>')


def render_svg(svg: str, *, max_width: int = 720) -> None:
    """Render an inline SVG string reliably (see _svg_img_tag for why)."""
    st.html(_svg_img_tag(svg, max_width))


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
        st.success("Correct")
    else:
        st.error(f"Incorrect — correct answer: **{key_txt}**")

    st.markdown("**Why the correct answer is right**")
    st.markdown(fb.why_correct)

    traps = {k: v for k, v in fb.distractor_notes.items() if v}
    if traps:
        with st.expander("Why the wrong answers are traps", expanded=not fb.correct):
            for oid, note in traps.items():
                st.markdown(f"- **{oid}** — {note}")

    if fb.exam_pattern:
        st.info(f"**Spot it on the exam:** {fb.exam_pattern}")

    if fb.verify_cli:
        st.markdown("**Verify on the device**")
        st.code("\n".join(fb.verify_cli), language="text")

    if fb.references:
        st.caption("Reference: " + " · ".join(fb.references))


def _format_selection(q: Question, sel) -> str:
    """Human-readable version of what the learner actually chose."""
    if sel in (None, "", [], ()):
        return "_(skipped / left blank)_"
    if q.is_fill:
        return f"“{sel}”"
    ids = sel if isinstance(sel, (list, tuple, set)) else [sel]
    out = []
    for oid in ids:
        try:
            out.append(f"{oid}. {q.option(oid).text}")
        except KeyError:
            out.append(str(oid))
    return "; ".join(out) if out else "_(skipped / left blank)_"


def render_quiz_review(exam: str, question_ids: list[str], answers: dict) -> None:
    """After-quiz review for a test-mode quiz (one graded at the end with no
    feedback as you go). Shows every question you missed with your answer, the
    correct answer and the explanation, then recaps the ones you got right — so
    a learner without the inline 'remediation' feedback can still learn from it.
    """
    bank = get_bank()
    items = [(qid, bank.get(qid)) for qid in question_ids]
    missed = [(qid, q) for qid, q in items if not q.check(answers.get(qid))]
    correct = [(qid, q) for qid, q in items if q.check(answers.get(qid))]

    section_header("clipboard", "Review every question", size=1.15)
    if not missed:
        st.success("You got every question right — nothing to remediate.")
    else:
        st.caption(f"This quiz didn't give feedback as you went, so here's the breakdown. "
                   f"The **{len(missed)}** you missed are first, with the correct answer "
                   "and why.")
        for qid, q in missed:
            with st.container(border=True):
                st.markdown(f"{glyph('cross', 18, '#E06C6C')} **{html.escape(q.stem)}**",
                            unsafe_allow_html=True)
                st.caption(f"Your answer: {_format_selection(q, answers.get(qid))}")
                render_feedback(q, grade(q, answers.get(qid)))

    if correct:
        with st.expander(f"Questions you got right ({len(correct)})"):
            for qid, q in correct:
                st.markdown(f"- **{q.stem}**  →  correct: **{', '.join(q.correct)}**")


def grade_and_record(exam: str, q: Question, selection, *,
                     xp_scale: float = 1.0, miss_scale: float = 1.0) -> Feedback:
    fb = grade(q, selection)
    prof = get_profile(exam)
    st.session_state["_xp_event"] = prof.record_study(
        q, fb.correct, xp_scale=xp_scale, miss_scale=miss_scale)
    save_profile(exam)
    return fb


def last_xp_event() -> dict:
    """The XP result of the most recent grade_and_record (delta, streak, flags)."""
    return st.session_state.get("_xp_event") or {}


def render_xp_event(info: dict) -> None:
    """Render a +/- XP chip with streak + mastery/regression context."""
    if not info:
        return
    delta = info.get("delta", 0)
    acc = current_accent()
    bits = [f"<b style='color:{acc}'>+{delta} XP</b>" if delta >= 0 else f"<b>{delta} XP</b>"]
    if info.get("mastered"):
        bits.append(f"{ui_icons.inline('trophy', 16, acc)}mastered!")
    elif info.get("learned"):
        bits.append(f"{ui_icons.inline('trend_up', 16, acc)}improving")
    elif info.get("regressed"):
        m = info.get("misses", 0)
        bits.append(ui_icons.inline("warn", 16, "#E0A96C")
                    + (f"missed {m}× in a row — stings more" if m >= 2 else "missed"))
    streak = info.get("streak", 0)
    if streak >= 3:
        bits.append(f"{ui_icons.inline('flame', 16, '#E8913A')}{streak} in a row")
    st.markdown(
        "<div style='display:flex;flex-wrap:wrap;align-items:center;gap:.15rem 1.1rem'>"
        + "".join(f"<span style='display:inline-flex;align-items:center'>{b}</span>" for b in bits)
        + "</div>",
        unsafe_allow_html=True,
    )


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


def pct_bar(data: dict, value_label: str = "Accuracy %") -> None:
    """Horizontal percentage bar chart on a FIXED 0–100 axis (not auto-scaled)."""
    import altair as alt
    import pandas as pd
    df = pd.DataFrame({"Domain": list(data.keys()), value_label: list(data.values())})
    chart = (
        alt.Chart(df)
        .mark_bar(color="#1BA0D7")
        .encode(
            x=alt.X(f"{value_label}:Q", scale=alt.Scale(domain=[0, 100]), title=value_label),
            y=alt.Y("Domain:N", sort=None, title=None),
            tooltip=["Domain", value_label],
        )
        .properties(height=max(120, 34 * len(df)))
    )
    st.altair_chart(chart, width="stretch")


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
    csub, cskip = st.columns(2)
    with csub:
        do_submit = st.button(submit_label, key=f"{skey}_submit", type="primary")
    with cskip:
        if st.button("Skip ▶", key=f"{skey}_skip",
                     help="Leave this one unanswered and move on (counts as incorrect)."):
            if idx + 1 >= total:
                state["done"] = True
            else:
                state["idx"] += 1
                state["phase"] = "answering"
            st.rerun()
    if do_submit:
        state["answers"][q.id] = sel
        fb = grade(q, sel)
        prof.record_study(q, fb.correct)
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


# --- interactive CompTIA PBQ (categorize / match / order) -------------------
def render_perf_task(task, skey_prefix: str) -> bool:
    """Render a CompTIA performance task and grade it. Returns True once every
    row is correct (also stores a cross-page flag pbq_passed_<id>)."""
    import random as _random
    passed_flag = f"pbq_passed_{task.id}"
    _KIND_HINT = {
        "categorize": "Choose the category each item belongs in.",
        "match": "Pick the correct match for each item.",
        "order": "Choose which item belongs in each position.",
    }
    st.markdown(task.prompt)
    st.caption(_KIND_HINT.get(task.kind, ""))
    rows = task.rows()
    with st.form(f"{skey_prefix}_form"):
        picks = {}
        for key, label, choices, _correct in rows:
            opts = list(choices)
            _random.Random(f"{task.id}:{key}").shuffle(opts)   # no positional hint
            picks[key] = st.selectbox(label, ["— choose —"] + opts, key=f"{skey_prefix}_{key}")
        submitted = st.form_submit_button("Validate", type="primary")
    if submitted:
        answer = {k: (v if v != "— choose —" else None) for k, v in picks.items()}
        checks = task.grade(answer)
        st.markdown(
            "".join(
                f"<div style='display:flex;align-items:center;margin:.12rem 0'>"
                f"{ui_icons.inline('check' if c.passed else 'cross', 16, '#22C58B' if c.passed else '#E06C6C')}"
                f"<span>{html.escape(c.description)}</span></div>"
                for c in checks),
            unsafe_allow_html=True,
        )
        if all(c.passed for c in checks):
            st.session_state[passed_flag] = True
            st.success(task.success)
            st.balloons()
        else:
            n = sum(1 for c in checks if c.passed)
            st.warning(f"{n}/{len(checks)} correct — fix the flagged rows and validate again.")
            if task.explain:
                with st.expander("Need a hint?"):
                    st.markdown(task.explain)
    return st.session_state.get(passed_flag, False)


def render_any_pbq(pbq_id: str, skey_prefix: str) -> bool:
    """Dispatch a unit's pbq_id to the right renderer: an interactive CompTIA
    performance task, or the Cisco CLI scenario."""
    if is_perf_task(pbq_id):
        return render_perf_task(get_perf_task(pbq_id), skey_prefix)
    from studyengine.cli_sim import get_scenario
    return render_pbq(get_scenario(pbq_id), skey_prefix)


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
        render_svg(topology_svg(topo, scenario.device))
        st.caption("Live from the scenario — the console device is ringed; a down link shows "
                   "red/dashed. The diagram updates as you configure.")
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

    from studyengine.cli_sim.clihelp import complete
    input_key = f"{skey_prefix}_cmd"
    pend_key = f"{skey_prefix}_pending"
    if pend_key in st.session_state:                 # apply a queued auto-finish / clear
        st.session_state[input_key] = st.session_state.pop(pend_key)
    with st.form(f"{skey_prefix}_form", clear_on_submit=False):
        cmd = st.text_input("Enter IOS command", key=input_key,
                            placeholder="e.g. configure terminal", label_visibility="collapsed")
        cols = st.columns([1, 1, 1])
        run = cols[0].form_submit_button("Run", type="primary", width="stretch")
        tab = cols[1].form_submit_button("Complete", width="stretch")
        clear = cols[2].form_submit_button("Reset lab", width="stretch")
    st.caption("Type **?** for the commands valid here (`?`, `show ?`, `switchport ?`), "
               "**Complete** to auto-finish the current word, or **help** for how it works.")
    if tab:
        st.session_state[pend_key] = complete(con.mode, cmd)
        st.rerun()
    if run and cmd.strip():
        prompt_before = con.prompt
        out = con.execute(cmd)
        st.session_state[tx_key].append((prompt_before, cmd, out))
        st.session_state[pend_key] = ""             # clear the box next run
        st.rerun()
    if clear:
        for k in (topo_key, tx_key, dev_key, cons_key, input_key, pend_key):
            st.session_state.pop(k, None)
        st.session_state.pop(f"pbq_passed_{scenario.id}", None)
        st.rerun()

    passed = False
    if st.button("Validate ticket", key=f"{skey_prefix}_validate", type="primary"):
        checks = scenario.validate(topo)
        for c in checks:
            (st.success if c.passed else st.error)(c.description)
        if all(c.passed for c in checks):
            passed = True
            st.session_state[f"pbq_passed_{scenario.id}"] = True
            st.success(scenario.success)
            st.balloons()
        else:
            st.warning("Not resolved yet — review the failed checks above and the hints.")
    return passed or st.session_state.get(f"pbq_passed_{scenario.id}", False)
