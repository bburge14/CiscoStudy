"""PBQ Lab: hands-on performance-based questions.

Cisco tracks get the live IOS CLI simulator (troubleshoot a broken topology with
real commands). CompTIA tracks get interactive tasks — categorize, match and
order — like the drag-and-drop PBQs on the real exams.
"""
from __future__ import annotations

import streamlit as st

from studyengine.cli_sim import scenarios_for
from studyengine.perf import perf_tasks_for
from ui_common import EXAMS, page_header, page_setup, render_perf_task, render_pbq

exam = page_setup("PBQ Lab")
cli_scenarios = scenarios_for(exam)
perf_tasks = perf_tasks_for(exam)

page_header("terminal", "PBQ Lab")

# ===========================================================================
# Cisco: live IOS CLI simulator
# ===========================================================================
if cli_scenarios:
    st.caption("Each ticket is a broken topology. Configure the device(s) with real IOS "
               "commands, then **Validate** — the checks inspect the actual resulting "
               "protocol state (does the channel bundle? is the neighbor FULL? is this the root?).")

    def _label(s):
        done = st.session_state.get(f"pbq_passed_{s.id}")
        return ("✓ " if done else "") + s.title

    sid_to = {s.id: s for s in cli_scenarios}
    pick = st.selectbox("Choose a troubleshooting ticket", [s.id for s in cli_scenarios],
                        format_func=lambda sid: _label(sid_to[sid]))
    scen = sid_to[pick]

    st.markdown(f"### {scen.title}")
    with st.expander("Supported commands (quick reference)"):
        st.markdown(
            "- **Modes:** `enable`, `configure terminal`, `interface g0/1`, "
            "`interface range g0/1 - 2`, `router ospf 1`, `vlan 10`, `exit`, `end`\n"
            "- **Interface:** `ip address A M`, `no shutdown`, `mtu 1500`, `description …`, "
            "`channel-group 1 mode active|passive|on|desirable|auto`\n"
            "- **Switching:** `switchport mode access|trunk`, `switchport access vlan N`, "
            "`switchport trunk native vlan N`, `switchport trunk allowed vlan …`\n"
            "- **STP/OSPF:** `spanning-tree vlan N root primary|priority P`, "
            "`network A W area X`, `router-id X`, `passive-interface …`\n"
            "- **Show:** `show running-config`, `show ip interface brief`, `show ip ospf neighbor`, "
            "`show spanning-tree vlan N`, `show etherchannel summary`, `show interfaces trunk`, "
            "`show vlan brief`, `show cdp neighbors`, `ping X`"
        )

    passed = render_pbq(scen, skey_prefix=f"lab_{exam}_{scen.id}")
    if passed:
        st.toast("Ticket resolved", icon=":material/check_circle:")

    st.divider()
    st.subheader("All tickets")
    st.dataframe(
        [{"Ticket": s.title, "Domain": s.domain.replace("_", " "),
          "Status": "✓ resolved" if st.session_state.get(f"pbq_passed_{s.id}") else "— open"}
         for s in cli_scenarios],
        width="stretch", hide_index=True,
    )

# ===========================================================================
# CompTIA: interactive categorize / match / order tasks
# ===========================================================================
elif perf_tasks:
    st.caption("CompTIA-style performance-based questions — **categorize**, **match** and "
               "**order** tasks like the drag-and-drop items on the real exam. Arrange each "
               "one, then **Validate**.")

    _KIND = {"categorize": "Categorize", "match": "Match", "order": "Order"}

    def _plabel(t):
        done = st.session_state.get(f"pbq_passed_{t.id}")
        return ("✓ " if done else "") + f"{t.title}  ·  {_KIND.get(t.kind, '')}"

    tid_to = {t.id: t for t in perf_tasks}
    pick = st.selectbox("Choose a task", [t.id for t in perf_tasks],
                        format_func=lambda tid: _plabel(tid_to[tid]))
    task = tid_to[pick]

    st.markdown(f"### {task.title}")
    passed = render_perf_task(task, skey_prefix=f"lab_{exam}_{task.id}")
    if passed:
        st.toast("Task resolved", icon=":material/check_circle:")

    st.divider()
    st.subheader("All tasks")
    st.dataframe(
        [{"Task": t.title, "Type": _KIND.get(t.kind, t.kind),
          "Status": "✓ resolved" if st.session_state.get(f"pbq_passed_{t.id}") else "— open"}
         for t in perf_tasks],
        width="stretch", hide_index=True,
    )

# ===========================================================================
else:
    st.info(f"Performance-based questions for **{EXAMS.get(exam, exam)}** are on the way. "
            "In the meantime, **Diagnostic**, **Endless Drill** and **Exam Simulation** are "
            "fully stocked for this track.")
    st.stop()
