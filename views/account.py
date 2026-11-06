"""My Account: edit your own display name, login and password — one compact page."""
from __future__ import annotations

import streamlit as st

from ui_common import (
    _clear_session_study_state,
    change_password,
    current_user,
    is_instructor,
    list_users,
    page_header,
    page_setup,
    rename_account,
    section_header,
    set_display_name,
)

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

# --- instructor shortcut ----------------------------------------------------
if is_instructor(user):
    st.divider()
    st.info("You're an **instructor / admin** on this instance — create and manage other "
            "accounts from the Instructor page.")
    st.page_link("views/instructor.py", label="Go to Instructor tools",
                 icon=":material/supervisor_account:")
