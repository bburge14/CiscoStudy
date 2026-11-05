"""Progress dashboard: mastery by domain/sub-topic, remediation queue, milestones."""
from __future__ import annotations

import pandas as pd
import streamlit as st

from studyengine import exam_readiness, get_blueprint
from ui_common import (
    box_distribution,
    domain_mastery_table,
    get_curriculum,
    get_profile,
    page_header,
    page_setup,
    pct_bar,
    reset_profile,
)

exam = page_setup("Progress Dashboard", icon="📊")
bp = get_blueprint(exam)
prof = get_profile(exam)
cur = get_curriculum()

page_header("bars", "Progress Dashboard")

seen, correct = prof.overall()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Questions answered", seen)
c2.metric("Lifetime accuracy", f"{round(correct/seen*100)}%" if seen else "—")
mastered = sum(1 for s in prof.q.values() if s.box >= 4)
c3.metric("Items in mastery (box 4–5)", mastered)
c4.metric("Baseline", f"{prof.baseline['overall']}%" if prof.baseline else "not taken")

if seen == 0:
    st.info("No activity yet. Take the **Diagnostic Baseline** or run an **Endless Drill** to populate your stats.")
    st.stop()

st.divider()
st.subheader("🎯 Exam readiness")
r = exam_readiness(prof, bp)
rc1, rc2 = st.columns([1, 2])
rc1.metric("Estimated score", f"{r['estimate']}%" if r["estimate"] is not None else "—")
rc1.caption(f"Topics practiced: {r['coverage']}% of the exam")
with rc2:
    if r["ready"]:
        st.success(f"**{r['verdict']}** — estimated {r['estimate']}%, {r['coverage']}% of the exam practiced.")
    elif r["estimate"] is None:
        st.info(f"{r['verdict']} — practice a few more domains to get an estimate.")
    else:
        st.warning(f"**{r['verdict']}** — estimated {r['estimate']}%, {r['coverage']}% of the exam practiced.")
    st.caption("This is your practice accuracy weighted by the official domain weights — a study "
               "gauge, not a prediction. Cisco's real cut score is scaled and unpublished. For a "
               "fuller check, run a timed **Exam Simulation**.")

st.divider()
st.subheader("Mastery by domain")
rows = domain_mastery_table(exam)
chart = {}
for d in bp.domains:
    ds = prof.domain_stats().get(d.key)
    chart[d.name] = round(ds[2] * 100) if ds and ds[0] else 0
pct_bar(chart)
st.dataframe(rows, width="stretch", hide_index=True)

st.divider()
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🎯 Remediation queue")
    weak = prof.weak_subtopics()
    if weak:
        st.caption("Sub-topics below 80% (worst first). Target these in Endless Drill → remediation mode.")
        st.dataframe(
            [{"Sub-topic": s.replace("_", " "), "Accuracy": f"{round(a*100)}%", "Attempts": n}
             for s, a, n in weak],
            width="stretch", hide_index=True,
        )
    else:
        st.success("No sub-topics below 80%. Nice work.")

with col_b:
    st.subheader("Spaced-repetition boxes")
    st.caption("Box 1 = just missed (surfaces ~8× more often) → Box 5 = mastered.")
    dist = box_distribution(exam)
    st.bar_chart(pd.DataFrame({"Items": {f"Box {b}": dist[b] for b in sorted(dist)}}))

st.divider()
st.subheader("Milestone progress")
units = cur.units_for(exam)
st.dataframe(
    [{"Unit": f"{u.order}. {u.title}",
      "Lessons passed": f"{sum(1 for l in u.lessons if l.id in prof.completed_lessons)}/{len(u.lessons)}",
      "Milestone": "✅ passed" if u.id in prof.passed_milestones else "— open",
      "PBQ": (("✅" if st.session_state.get(f'pbq_passed_{u.pbq_id}') else "— ") + "required")
             if u.pbq_id else "n/a"}
     for u in units],
    width="stretch", hide_index=True,
)

st.divider()
with st.expander("⚠️ Reset progress for this profile + track"):
    st.warning("This permanently clears the CURRENT profile's answered-item history, "
               "mastery boxes, completed lessons, milestones and baseline for this exam "
               "track. Other profiles and the other exam track are untouched.")
    if st.button(f"Reset {exam.upper()} progress for this profile"):
        reset_profile(exam)
        for k in list(st.session_state):
            if k.startswith(("drill_", "dx_", "ms", "lq", "pbq_passed_", "lab_", "sched_")):
                st.session_state.pop(k, None)
        st.success("Progress reset.")
        st.rerun()
