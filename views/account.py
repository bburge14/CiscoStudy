"""My Account: edit your own login, display name and password."""
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
    set_display_name,
)

page_setup("My Account", icon="👤")
user = current_user()
meta = list_users().get(user, {})

page_header("user_gear", "My Account")
st.caption(
    f"Signed in as **{meta.get('name', user)}**  ·  login `{meta.get('username', user)}`  ·  "
    + ("Instructor / admin" if is_instructor(user) else "Learner")
)
st.caption("Everything you change here keeps all of your saved progress.")
st.divider()

# --- display name -----------------------------------------------------------
st.subheader("Display name")
with st.form("acct_name"):
    nn = st.text_input("Shown on the dashboard and roster", value=meta.get("name", user))
    if st.form_submit_button("Save name", type="primary"):
        if set_display_name(user, nn):
            st.success("Display name updated.")
            st.rerun()
        else:
            st.error("Enter a name.")

st.divider()

# --- login / username -------------------------------------------------------
st.subheader("Login (username)")
st.caption("What you type to sign in. Change it to anything you like — e.g. from "
           "`default` to your own name.")
with st.form("acct_login"):
    nu = st.text_input("Username", value=meta.get("username", user))
    if st.form_submit_button("Change login", type="primary"):
        new_slug, err = rename_account(user, nu)
        if err:
            st.error(err)
        else:
            st.session_state["auth_user"] = new_slug
            _clear_session_study_state()
            st.success(f"Login changed to `{nu}`. Use it next time you sign in.")
            st.rerun()

st.divider()

# --- password ---------------------------------------------------------------
st.subheader("Password")
with st.form("acct_pw", clear_on_submit=True):
    cur = st.text_input("Current password", type="password")
    new = st.text_input("New password", type="password")
    new2 = st.text_input("Confirm new password", type="password")
    if st.form_submit_button("Change password", type="primary"):
        if new != new2:
            st.error("New passwords don't match.")
        else:
            ok, err = change_password(user, cur, new)
            if err:
                st.error(err)
            else:
                st.success("Password changed.")

# --- instructor shortcut ----------------------------------------------------
if is_instructor(user):
    st.divider()
    st.info("You're an **instructor/admin** on this instance — you can create and manage "
            "other accounts.")
    st.page_link("views/instructor.py", label="Go to Instructor tools",
                 icon=":material/supervisor_account:")
