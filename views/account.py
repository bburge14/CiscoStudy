"""My Account: edit your display name/login/password and your certification
wallet (the certs you hold / are studying / plan to take) — one compact page."""
from __future__ import annotations

import datetime as _dt

import streamlit as st

from studyengine.leveling import XP_PER_EARNED_CERT
from ui_common import (
    CERT_CATALOG,
    CERT_STATUS_LABEL,
    LIVE_EXAMS,
    _clear_session_study_state,
    change_password,
    credential_counts,
    current_user,
    get_cert_status,
    is_instructor,
    list_users,
    page_header,
    page_setup,
    provider_logo_img,
    render_earned_badges,
    rename_account,
    section_header,
    set_cert_status,
    set_display_name,
    track_name,
)


def _persist_cert_status(exam: str) -> None:
    """on_change for the per-track status selectbox — persists immediately, and
    stamps today's date the first time a track is marked Earned."""
    val = st.session_state.get(f"certsel_{exam}", "")
    _, cur_date = get_cert_status(exam)
    date = cur_date
    if val == "earned" and not date:
        date = _dt.date.today().isoformat()
    set_cert_status(exam, val, date)


def _persist_cert_date(exam: str) -> None:
    """on_change for the Earned-on date picker."""
    d = st.session_state.get(f"certdate_{exam}")
    if d is not None:
        set_cert_status(exam, "earned", d.isoformat())

page_setup("My Account")
user = current_user()
meta = list_users().get(user, {})

page_header("user_gear", "My Account")
st.caption(
    f"Signed in as **{meta.get('name', user)}**  ·  login `{meta.get('username', user)}`  ·  "
    + ("Instructor / admin" if is_instructor(user) else "Learner")
    + ".  Everything here keeps all of your saved progress."
)
st.write("")

col_profile, col_pw = st.columns(2, gap="large")

# --- profile: display name + login, saved together -------------------------
with col_profile:
    section_header("user_gear", "Profile", size=1.15)
    with st.form("acct_profile", border=False):
        nn = st.text_input("Display name", value=meta.get("name", user),
                           help="Shown on the dashboard and the instructor roster.")
        nu = st.text_input("Login (username)", value=meta.get("username", user),
                           help="What you type to sign in — change it to anything you like.")
        if st.form_submit_button("Save profile", type="primary"):
            errors, changed = [], False
            if nn.strip() and nn != meta.get("name", user):
                if set_display_name(user, nn):
                    st.toast("Display name updated.", icon=":material/check_circle:")
                    changed = True
                else:
                    errors.append("Enter a valid display name.")
            if nu.strip() and nu != meta.get("username", user):
                new_slug, err = rename_account(user, nu)
                if err:
                    errors.append(err)
                else:
                    st.session_state["auth_user"] = new_slug
                    _clear_session_study_state()
                    st.toast(f"Login changed to “{nu}”.", icon=":material/check_circle:")
                    changed = True
            for e in errors:
                st.error(e)
            if changed and not errors:
                st.rerun()
            elif not changed and not errors:
                st.info("Nothing to save — you didn't change anything.")

# --- password ---------------------------------------------------------------
with col_pw:
    section_header("lock", "Password", size=1.15)
    with st.form("acct_pw", border=False, clear_on_submit=True):
        curpw = st.text_input("Current password", type="password")
        new = st.text_input("New password", type="password")
        new2 = st.text_input("Confirm new password", type="password")
        if st.form_submit_button("Change password", type="primary"):
            if new != new2:
                st.error("New passwords don't match.")
            else:
                ok, err = change_password(user, curpw, new)
                st.error(err) if err else st.success("Password changed.")

# --- certifications (credential wallet) -------------------------------------
st.divider()
section_header("trophy", "My Certifications", size=1.15)
_counts = credential_counts()
st.caption(
    f"**{_counts['earned']}** earned &middot; **{_counts['studying']}** studying "
    f"&middot; **{_counts['planned']}** planned.  Marking a cert **Earned** adds a "
    f"one-time **+{XP_PER_EARNED_CERT} XP** to that track's level."
)
if not render_earned_badges():
    st.caption("No certifications marked yet — set your first one below.")
st.write("")

with st.expander("Set / update your certifications",
                 expanded=sum(_counts.values()) == 0):
    _live = set(LIVE_EXAMS)
    _opts = ["", "planned", "studying", "earned"]
    for _prov in CERT_CATALOG:
        _certs = [c for c in _prov.get("certs", []) if c.get("key") in _live]
        if not _certs:
            continue
        _logo = provider_logo_img(_prov["provider"], height=15)
        st.markdown(
            "<div style='display:flex;align-items:center;gap:.4rem;margin:.7rem 0 .2rem;"
            "font-size:.7rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;"
            "color:#8A94A6;border-top:1px solid rgba(255,255,255,.07);padding-top:.5rem'>"
            f"{_logo}<span>{_prov['provider']}</span></div>",
            unsafe_allow_html=True)
        for _cert in _certs:
            _k = _cert["key"]
            _skey = f"certsel_{_k}"
            if _skey not in st.session_state:
                st.session_state[_skey] = get_cert_status(_k)[0]
            _row = st.columns([4, 3, 3])
            _row[0].markdown(f"**{track_name(_k)}**")
            _row[1].selectbox(
                "Status", options=_opts, key=_skey,
                format_func=lambda v: CERT_STATUS_LABEL[v],
                label_visibility="collapsed",
                on_change=_persist_cert_status, args=(_k,))
            if get_cert_status(_k)[0] == "earned":
                _cur = get_cert_status(_k)[1]
                try:
                    _default = _dt.date.fromisoformat(_cur) if _cur else _dt.date.today()
                except Exception:
                    _default = _dt.date.today()
                _row[2].date_input(
                    "Earned on", value=_default, key=f"certdate_{_k}",
                    label_visibility="collapsed",
                    on_change=_persist_cert_date, args=(_k,))

# --- instructor shortcut ----------------------------------------------------
if is_instructor(user):
    st.divider()
    st.info("You're an **instructor / admin** on this instance — create and manage other "
            "accounts from the Instructor page.")
    st.page_link("views/instructor.py", label="Go to Instructor tools",
                 icon=":material/supervisor_account:")
