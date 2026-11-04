"""Official exam blueprints for CCNA 200-301 and CCNP ENCOR 350-401.

Domain weightings mirror the published Cisco exam topic blueprints. These
weights drive diagnostic baseline composition, drill sampling bias and the
weakness-remediation dashboard. Sub-topic lists are the handles the question
bank tags against; they are the vocabulary the whole engine shares.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Domain:
    key: str
    name: str
    weight: float  # fraction of the real exam (0..1)
    subtopics: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExamBlueprint:
    code: str
    name: str
    domains: tuple[Domain, ...]

    @property
    def domain_keys(self) -> list[str]:
        return [d.key for d in self.domains]

    def domain(self, key: str) -> Domain:
        for d in self.domains:
            if d.key == key:
                return d
        raise KeyError(f"{self.code}: unknown domain {key!r}")

    def weight_of(self, key: str) -> float:
        return self.domain(key).weight


# --- CCNA 200-301 -----------------------------------------------------------
CCNA = ExamBlueprint(
    code="ccna",
    name="CCNA 200-301",
    domains=(
        Domain(
            "network_fundamentals", "1.0 Network Fundamentals", 0.20,
            ("osi_tcpip", "cabling_media", "ipv4_addressing_subnetting",
             "ipv6_addressing", "switching_concepts", "tcp_udp", "wireless_fundamentals"),
        ),
        Domain(
            "network_access", "2.0 Network Access", 0.20,
            ("vlans_trunking", "stp_root_election", "etherchannel", "cdp_lldp",
             "wlan_architecture", "wlc_config"),
        ),
        Domain(
            "ip_connectivity", "3.0 IP Connectivity", 0.25,
            ("routing_table", "static_routing", "ospf", "wildcard_masks",
             "fhrp", "default_gateway"),
        ),
        Domain(
            "ip_services", "4.0 IP Services", 0.10,
            ("nat", "ntp", "dhcp", "dns", "snmp", "syslog", "qos_concepts"),
        ),
        Domain(
            "security_fundamentals", "5.0 Security Fundamentals", 0.15,
            ("acls", "port_security", "dhcp_snooping", "dai", "aaa_8021x",
             "vpn_concepts", "layer2_security"),
        ),
        Domain(
            "automation", "6.0 Automation and Programmability", 0.10,
            ("sdn_controllers", "rest_api", "json_data", "config_mgmt_tools",
             "netconf_restconf"),
        ),
    ),
)

# --- CCNP ENCOR 350-401 -----------------------------------------------------
ENCOR = ExamBlueprint(
    code="encor",
    name="CCNP ENCOR 350-401",
    domains=(
        Domain(
            "architecture", "1.0 Architecture", 0.15,
            ("enterprise_design", "high_availability", "wireless_deployment",
             "machine_learning_ai", "fabric_overview"),
        ),
        Domain(
            "virtualization", "2.0 Virtualization", 0.10,
            ("device_virtualization", "data_path_virtualization", "network_virtualization_vrf",
             "overlay_vxlan"),
        ),
        Domain(
            "infrastructure", "3.0 Infrastructure", 0.30,
            ("layer2_stp_advanced", "etherchannel_advanced", "ospf_advanced",
             "bgp", "eigrp", "multicast", "qos", "ip_services_encor"),
        ),
        Domain(
            "network_assurance", "4.0 Network Assurance", 0.10,
            ("diagnostics_tools", "flexible_netflow", "spans", "snmp_syslog",
             "ipsla", "debugs"),
        ),
        Domain(
            "security", "5.0 Security", 0.20,
            ("device_access_control", "infrastructure_security_acls", "cope_security",
             "wireless_security", "network_access_control_8021x"),
        ),
        Domain(
            "automation", "6.0 Automation", 0.15,
            ("python_data", "json_yaml_xml", "eem_scripting", "netconf_restconf_encor",
             "model_driven_telemetry", "controllers_apis"),
        ),
    ),
)

EXAMS: dict[str, ExamBlueprint] = {CCNA.code: CCNA, ENCOR.code: ENCOR}


def get_blueprint(code: str) -> ExamBlueprint:
    try:
        return EXAMS[code]
    except KeyError:
        raise KeyError(f"Unknown exam code {code!r}; expected one of {list(EXAMS)}") from None
