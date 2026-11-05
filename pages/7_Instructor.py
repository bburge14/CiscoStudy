"""Instructor view: see every account's progress on this instance.

Only the instructor account (the first account created on the instance) can see
the roster. Learner accounts get a polite notice instead.
"""
from __future__ import annotations

import time

import pandas as pd
import streamlit as st

from studyengine import get_blueprint
from ui_common import (
    EXAMS,
    admin_create_account,
    current_user,
    delete_account,
    is_instructor,
    list_users,
    load_user_profile,
    page_setup,
    roster_summary,
    set_password_admin,
    set_role,
)

exam = page_setup("Instructor", icon="🧑‍🏫")
bp = get_blueprint(exam)

st.title("🧑‍🏫 Instructor View")

if not is_instructor(current_user()):
    st.warning("This page is for the **instructor** account on this instance.")
    st.info("The first account created on an instance becomes its instructor. If you set this "
            "up, sign in with that first account; otherwise this is your personal study view.")
    st.stop()

st.caption(f"Progress for every account on this instance · **{EXAMS[exam]}** track. "
           "Switch tracks in the sidebar.")

rows = roster_summary(exam)
learners = [r for r in rows if r["role"] != "instructor"]

# --- headline metrics -------------------------------------------------------
took_baseline = sum(1 for r in learners if r["baseline"] is not None)
active = [r for r in learners if r["answered"] > 0]
avg_acc = round(sum(r["accuracy"] for r in active) / len(active)) if active else None
c1, c2, c3, c4 = st.columns(4)
c1.metric("Learner accounts", len(learners))
c2.metric("Took the diagnostic", took_baseline)
c3.metric("Active (answered ≥1)", len(active))
c4.metric("Avg accuracy (active)", f"{avg_acc}%" if avg_acc is not None else "—")

st.divider()
st.subheader("Roster")

if not learners:
    st.info("No learner accounts yet. Have your airmen open the app and create an account — "
            "they'll appear here. (On a shared instance, run `run-shared.bat` and give them "
            "your PC's `http://<ip>:8501` address.)")
    st.stop()


def _last(ts: float) -> str:
    return "—" if not ts else time.strftime("%Y-%m-%d", time.localtime(ts))


table = [{
    "Learner": r["name"],
    "Baseline": f"{r['baseline']}%" if r["baseline"] is not None else "—",
    "Answered": r["answered"],
    "Accuracy": f"{r['accuracy']}%" if r["accuracy"] is not None else "—",
    "Milestones": r["milestones"],
    "Weak areas": ", ".join(s.replace("_", " ") for s in r["weak"]) or "—",
    "Last active": _last(r["last_seen"]),
} for r in learners]
st.dataframe(pd.DataFrame(table), width="stretch", hide_index=True)

# --- per-learner drill-down -------------------------------------------------
st.divider()
st.subheader("Inspect a learner")
by_slug = {r["slug"]: r for r in learners}
pick = st.selectbox("Learner", list(by_slug), format_func=lambda s: by_slug[s]["name"])
prof = load_user_profile(pick, exam)

seen, correct = prof.overall()
d1, d2, d3 = st.columns(3)
d1.metric("Answered", seen)
d2.metric("Accuracy", f"{round(correct/seen*100)}%" if seen else "—")
d3.metric("Baseline", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

dstats = prof.domain_stats()
dom_rows = []
for d in bp.domains:
    s, c, acc = dstats.get(d.key, (0, 0, 0.0))
    dom_rows.append({
        "Domain": d.name,
        "Answered": s,
        "Accuracy": f"{round(acc*100)}%" if s else "—",
        "Exam weight": f"{round(d.weight*100)}%",
    })
st.markdown("**By domain**")
st.dataframe(pd.DataFrame(dom_rows), width="stretch", hide_index=True)

weak = prof.weak_subtopics()
if weak:
    st.markdown("**Weak sub-topics (below 80%)**")
    st.dataframe(
        pd.DataFrame([{"Sub-topic": s.replace("_", " "), "Accuracy": f"{round(a*100)}%", "Attempts": n}
                      for s, a, n in weak]),
        width="stretch", hide_index=True,
    )
else:
    st.success("No sub-topics below 80% for this learner.")

# --- account management -----------------------------------------------------
st.divider()
st.subheader("Manage accounts")

with st.expander("➕ Create an account (pre-provision a learner)"):
    with st.form("admin_create", clear_on_submit=True):
        nu = st.text_input("Username")
        npw = st.text_input("Temporary password", type="password")
        nrole = st.selectbox("Role", ["learner", "instructor"])
        if st.form_submit_button("Create"):
            slug, err = admin_create_account(nu, npw, nrole)
            if err:
                st.error(err)
            else:
                st.success(f"Created **{nu}**. Share the temporary password; they can keep it "
                           "or you can reset it here.")
                st.rerun()

accounts = {s: e for s, e in list_users().items() if e.get("hash")}
sel = st.selectbox("Edit an account", list(accounts),
                   format_func=lambda s: accounts[s].get("name", s), key="edit_acct")
meta = accounts[sel]
st.caption(f"Role: **{meta.get('role', 'learner')}**"
           + ("  ·  the Default admin account always stays instructor." if sel == "default" else ""))

ca, cb = st.columns(2)
with ca:
    with st.form("reset_pw", clear_on_submit=True):
        rpw = st.text_input("Set a new password", type="password")
        if st.form_submit_button("Reset password"):
            ok, err = set_password_admin(sel, rpw)
            (st.error(err) if err else st.success("Password reset."))
with cb:
    if sel != "default":
        target = "learner" if meta.get("role") == "instructor" else "instructor"
        if st.button(f"Make {target}", key="toggle_role"):
            set_role(sel, target)
            st.rerun()
    else:
        st.caption("The Default admin can't be demoted.")

if sel not in ("default", current_user()):
    with st.expander("🗑️ Delete this account"):
        st.warning(f"Permanently delete **{meta.get('name', sel)}** and all of their progress. "
                   "This cannot be undone.")
        sure = st.checkbox("I understand — delete it", key="del_sure")
        if st.button("Delete account", key="del_btn", disabled=not sure):
            delete_account(sel)
            st.success("Account deleted.")
            st.rerun()
elif sel == current_user():
    st.caption("You can't delete the account you're signed in with.")

st.caption("Read-only roster above; learners can't see each other's progress. The Default "
           "account is this instance's instructor/admin.")
