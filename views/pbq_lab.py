"""PBQ Lab: troubleshoot broken topologies in an interactive Cisco IOS simulator."""
from __future__ import annotations

import streamlit as st

from studyengine.cli_sim import scenarios_for
from ui_common import EXAMS, page_header, page_setup, render_pbq

exam = page_setup("PBQ Lab", icon="🖥️")
scenarios = scenarios_for(exam)

page_header("terminal", "PBQ Lab — CLI Simulator")
st.caption("Each ticket is a broken topology. Configure the device(s) with real IOS "
           "commands, then **Validate** — the checks inspect the actual resulting "
           "protocol state (does the channel bundle? is the neighbor FULL? is this the root?).")

if not scenarios:
    st.info(f"🖥️ The PBQ Lab is a live Cisco IOS CLI simulator, so it powers the Cisco "
            f"tracks. **{EXAMS[exam]}** uses CompTIA-style performance tasks "
            "(drag-and-drop, matching, ordering, sims) — those labs are on the roadmap. "
            "For now, **Diagnostic**, **Endless Drill**, and **Exam Simulation** are fully "
            "stocked for this track.")
    st.stop()

# scenario picker with completion status
def label(s):
    done = st.session_state.get(f"pbq_passed_{s.id}")
    return ("✅ " if done else "") + s.title

sid_to_scen = {s.id: s for s in scenarios}
pick = st.selectbox("Choose a troubleshooting ticket", [s.id for s in scenarios],
                    format_func=lambda sid: label(sid_to_scen[sid]))
scen = sid_to_scen[pick]

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
    st.toast("Ticket resolved ✔", icon="✅")

# overview of all tickets
st.divider()
st.subheader("All tickets")
st.dataframe(
    [{"Ticket": s.title,
      "Domain": s.domain.replace("_", " "),
      "Status": "✅ resolved" if st.session_state.get(f"pbq_passed_{s.id}") else "— open"}
     for s in scenarios],
    width="stretch", hide_index=True,
)
