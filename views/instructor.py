"""Instructor view: manage accounts and see every learner's progress.

Only an instructor account can see this page. Account management is always
available (even before any learners exist); the roster fills in as people join.
Laid out as two tabs — Roster & progress, and Manage accounts — to keep it tidy.
"""
from __future__ import annotations

import time

import pandas as pd
import streamlit as st

from studyengine import get_blueprint
from ui_common import (
    EXAMS,
    admin_create_account,
    admin_reset_benchmark,
    admin_reset_progress,
    current_user,
    delete_account,
    is_instructor,
    list_users,
    load_user_profile,
    page_header,
    page_setup,
    rename_account,
    roster_summary,
    section_header,
    set_display_name,
    set_password_admin,
    set_role,
)

exam = page_setup("Instructor")
bp = get_blueprint(exam)

page_header("people", "Instructor View")

if not is_instructor(current_user()):
    st.warning("This page is for the **instructor** account on this instance.")
    st.info("The first account created on an instance becomes its instructor. If you set this "
            "up, sign in with that first account; otherwise this is your personal study view.")
    st.stop()

st.caption(f"Manage accounts and track progress · **{EXAMS[exam]}** track "
           "(switch tracks in the sidebar).")

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

tab_roster, tab_accounts = st.tabs(["Roster & progress", "Manage accounts"])

# ===========================================================================
# ROSTER & PROGRESS
# ===========================================================================
with tab_roster:
    if not learners:
        st.info("No learner accounts yet — add one under **Manage accounts**. Learners can "
                "also self-register from the sign-in screen, and they'll appear here.")
    else:
        def _last(ts: float) -> str:
            return "—" if not ts else time.strftime("%Y-%m-%d", time.localtime(ts))

        st.dataframe(pd.DataFrame([{
            "Learner": r["name"],
            "Baseline": f"{r['baseline']}%" if r["baseline"] is not None else "—",
            "Answered": r["answered"],
            "Accuracy": f"{r['accuracy']}%" if r["accuracy"] is not None else "—",
            "Milestones": r["milestones"],
            "Weak areas": ", ".join(s.replace("_", " ") for s in r["weak"]) or "—",
            "Last active": _last(r["last_seen"]),
        } for r in learners]), width="stretch", hide_index=True)

        section_header("gauge", "Inspect a learner", size=1.15)
        by_slug = {r["slug"]: r for r in learners}
        pick = st.selectbox("Learner", list(by_slug), format_func=lambda s: by_slug[s]["name"])
        prof = load_user_profile(pick, exam)

        seen, correct = prof.study_overall()
        d1, d2, d3 = st.columns(3)
        d1.metric("Answered", seen)
        d2.metric("Accuracy", f"{round(correct/seen*100)}%" if seen else "—")
        d3.metric("Baseline", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

        dstats = prof.domain_stats()
        st.markdown("**By domain**")
        st.dataframe(pd.DataFrame([{
            "Domain": d.name,
            "Answered": dstats.get(d.key, (0, 0, 0.0))[0],
            "Accuracy": f"{round(dstats.get(d.key, (0, 0, 0.0))[2]*100)}%" if dstats.get(d.key, (0, 0, 0.0))[0] else "—",
            "Exam weight": f"{round(d.weight*100)}%",
        } for d in bp.domains]), width="stretch", hide_index=True)

        weak = prof.weak_subtopics()
        if weak:
            st.markdown("**Weak sub-topics (below 80%)**")
            st.dataframe(pd.DataFrame([{"Sub-topic": s.replace("_", " "),
                                        "Accuracy": f"{round(a*100)}%", "Attempts": n}
                                       for s, a, n in weak]), width="stretch", hide_index=True)
        else:
            st.success("No sub-topics below 80% for this learner.")

        # --- reset this learner's status (compact, side by side) ------------
        st.markdown("**Reset this learner's status**  — clears progress only; the account, "
                    "login and role stay the same.")
        rb, rp = st.columns(2)
        with rb:
            st.caption("**Benchmark only** — clears the diagnostic so they can re-take it. "
                       "Mastery, XP and answered counts are kept.")
            ok_b = st.checkbox("Confirm reset benchmark", key=f"rb_{pick}")
            if st.button("Reset benchmark", key=f"rb_btn_{pick}", disabled=not ok_b):
                if admin_reset_benchmark(pick, exam):
                    st.success(f"Benchmark cleared for **{by_slug[pick]['name']}**.")
                    st.rerun()
                else:
                    st.error("Couldn't reset — account not found.")
        with rp:
            st.caption("**All progress** — wipes mastery, XP, streaks, answered counts, "
                       "milestones and the benchmark on this track. Cannot be undone.")
            ok_p = st.checkbox("Confirm reset everything", key=f"rp_{pick}")
            if st.button("Reset all progress", key=f"rp_btn_{pick}", disabled=not ok_p):
                if admin_reset_progress(pick, exam):
                    st.success(f"Progress reset for **{by_slug[pick]['name']}** on the "
                               f"{EXAMS[exam]} track.")
                    st.rerun()
                else:
                    st.error("Couldn't reset — account not found.")

# ===========================================================================
# MANAGE ACCOUNTS
# ===========================================================================
with tab_accounts:
    section_header("user_gear", "Create an account", size=1.15)
    with st.form("admin_create", border=False, clear_on_submit=True):
        cc = st.columns([2, 2, 1.2])
        nu = cc[0].text_input("Username (sign-in)")
        npw = cc[1].text_input("Temporary password", type="password")
        nrole = cc[2].selectbox("Role", ["learner", "instructor"])
        st.caption("Share the temporary password — they can change it from their own "
                   "**My Account** page.")
        if st.form_submit_button("Create account", type="primary"):
            slug, err = admin_create_account(nu, npw, nrole)
            if err:
                st.error(err)
            else:
                st.success(f"Created **{nu}** as a {nrole}. They can sign in now.")
                st.rerun()

    st.divider()
    section_header("people", "Edit an account", size=1.15)
    accounts = {s: e for s, e in list_users().items() if e.get("hash")}
    if not accounts:
        st.caption("No accounts to edit yet.")
    else:
        sel = st.selectbox(
            "Account", list(accounts),
            format_func=lambda s: f"{accounts[s].get('name', s)}  ·  {accounts[s].get('role', 'learner')}",
            key="edit_acct")
        meta = accounts[sel]
        st.caption(f"Role **{meta.get('role', 'learner')}**  ·  login `{meta.get('username', sel)}`  "
                   "·  the instance always keeps at least one instructor.")

        # identity (name + login) saved together
        with st.form(f"edit_identity_{sel}", border=False):
            ec = st.columns(2)
            nn = ec[0].text_input("Display name", value=meta.get("name", sel), key=f"edit_nn_{sel}")
            nlog = ec[1].text_input("Login (username)", value=meta.get("username", sel),
                                    key=f"edit_nlog_{sel}")
            if st.form_submit_button("Save changes"):
                err_any = False
                if nn.strip() and nn != meta.get("name", sel):
                    set_display_name(sel, nn)
                if nlog.strip() and nlog != meta.get("username", sel):
                    new_slug, err = rename_account(sel, nlog)
                    if err:
                        st.error(err); err_any = True
                    elif sel == current_user():
                        st.session_state["auth_user"] = new_slug
                if not err_any:
                    st.success("Saved.")
                    st.rerun()

        # password + role, side by side
        pc = st.columns(2)
        with pc[0]:
            with st.form(f"reset_pw_{sel}", border=False, clear_on_submit=True):
                rpw = st.text_input("Set a new password", type="password", key=f"rpw_{sel}")
                if st.form_submit_button("Reset password"):
                    ok, err = set_password_admin(sel, rpw)
                    st.error(err) if err else st.success("Password reset.")
        with pc[1]:
            target = "learner" if meta.get("role") == "instructor" else "instructor"
            st.caption(f"This account is currently a **{meta.get('role', 'learner')}**.")
            if st.button(f"Make {target}", key=f"toggle_role_{sel}"):
                if set_role(sel, target):
                    st.rerun()
                else:
                    st.error("The instance needs at least one instructor.")

        # danger zone
        if sel != current_user():
            st.divider()
            st.markdown("**Danger zone**")
            dz = st.columns([3, 1])
            sure = dz[0].checkbox(f"Permanently delete **{meta.get('name', sel)}** and all of "
                                  "their progress — this cannot be undone", key=f"del_sure_{sel}")
            if dz[1].button("Delete account", key=f"del_btn_{sel}", disabled=not sure):
                if delete_account(sel):
                    st.success("Account deleted.")
                    st.rerun()
                else:
                    st.error("Can't delete the instance's last instructor.")
        else:
            st.caption("You can't delete the account you're signed in with.")

st.caption("Learners can't see each other's progress. Accounts created or edited here take "
           "effect immediately.")
