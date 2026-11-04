"""CiscoStudy — a custom CCNA 200-301 & CCNP ENCOR 350-401 study platform.

Run locally with:  streamlit run app.py
"""
from __future__ import annotations

import streamlit as st

from studyengine import get_blueprint
from ui_common import EXAMS, domain_mastery_table, get_bank, get_profile, page_setup

exam = page_setup("Home", icon="🛜")
bank = get_bank()
bp = get_blueprint(exam)
prof = get_profile(exam)

st.title("🛜 CiscoStudy")
st.markdown(
    f"**Custom study & diagnostic platform for {EXAMS[exam]}.** "
    "Authentic, blueprint-aligned items with real IOS syntax, `show` output and "
    "performance-based labs — no placeholder questions."
)

seen, correct = prof.overall()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Item bank", f"{len(bank.query(exam=exam))} items")
c2.metric("Answered", seen)
c3.metric("Lifetime accuracy", f"{round(correct / seen * 100)}%" if seen else "—")
baseline_done = "✓ taken" if prof.baseline else "not taken"
c4.metric("Diagnostic", baseline_done)

st.divider()

# --- recommended next step --------------------------------------------------
st.subheader("Where to start")
if not prof.baseline:
    st.info(
        "👉 Begin with the **Diagnostic Baseline** (30 questions, 5 per official "
        "domain) to map your starting score and auto-build a remediation queue."
    )
else:
    weak = prof.weak_subtopics()
    if weak:
        names = ", ".join(s.replace("_", " ") for s, _, _ in weak[:4])
        st.warning(f"🎯 Remediation queue active. Weakest sub-topics: **{names}**. "
                   "Use **Endless Drill → remediation mode** to close the gaps.")
    else:
        st.success("No sub-topics below 80% yet. Keep drilling and work the "
                   "**Structured Milestones** to build exam coverage.")

st.divider()

# --- study modes guide ------------------------------------------------------
st.subheader("Study modes")
m1, m2 = st.columns(2)
with m1:
    st.markdown(
        "#### 🎯 Diagnostic Baseline\n"
        "30-question snapshot (5 per domain) → per-domain scorecard and an "
        "automatic sub-80% remediation queue.\n\n"
        "#### ♾️ Endless Drill\n"
        "Infinite adaptive stream with **instant grading** and deep breakdowns. "
        "Missed items resurface far more often; a remediation toggle targets your "
        "weak sub-topics."
    )
with m2:
    st.markdown(
        "#### 📚 Structured Milestones\n"
        "Per unit: **Read** a Markdown lesson → **Lesson Quiz** → cumulative "
        "**Milestone Exam** + an interactive **PBQ** to unlock the next unit.\n\n"
        "#### 🖥️ PBQ Lab\n"
        "Troubleshoot broken topologies in a real Cisco **IOS CLI simulator** "
        "(`conf t`, `router ospf`, `switchport…`). Validation checks the actual "
        "resulting protocol state."
    )

st.divider()
st.subheader(f"Domain coverage — {bp.name}")
st.dataframe(domain_mastery_table(exam), width="stretch", hide_index=True)

st.caption(
    "Use the sidebar to switch exam tracks or open a study mode. All content is "
    "original study material aligned to the public Cisco exam blueprints and real "
    "IOS behaviour."
)
