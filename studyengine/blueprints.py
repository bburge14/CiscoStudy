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

# --- CompTIA Security+ SY0-701 ----------------------------------------------
SECPLUS = ExamBlueprint(
    code="secplus",
    name="Security+ SY0-701",
    domains=(
        Domain(
            "general_security_concepts", "1.0 General Security Concepts", 0.12,
            ("security_controls", "cia_aaa", "zero_trust", "physical_security",
             "change_management", "cryptographic_solutions", "pki"),
        ),
        Domain(
            "threats_vulns_mitigations", "2.0 Threats, Vulnerabilities & Mitigations", 0.22,
            ("threat_actors", "threat_vectors", "social_engineering", "vulnerability_types",
             "malware", "network_attacks", "application_attacks", "mitigation_techniques"),
        ),
        Domain(
            "security_architecture", "3.0 Security Architecture", 0.18,
            ("architecture_models", "cloud_virtualization_security", "secure_design",
             "data_protection", "resilience_recovery"),
        ),
        Domain(
            "security_operations", "4.0 Security Operations", 0.28,
            ("secure_baselines_hardening", "asset_management", "vulnerability_management",
             "security_monitoring", "identity_access_management", "automation_orchestration",
             "incident_response", "digital_forensics"),
        ),
        Domain(
            "security_program_mgmt", "5.0 Security Program Management & Oversight", 0.20,
            ("security_governance", "risk_management", "third_party_risk",
             "compliance_privacy", "audits_assessments", "security_awareness"),
        ),
    ),
)

# --- CompTIA Network+ N10-009 -----------------------------------------------
NETPLUS = ExamBlueprint(
    code="netplus",
    name="Network+ N10-009",
    domains=(
        Domain(
            "networking_concepts", "1.0 Networking Concepts", 0.23,
            ("osi_model", "network_appliances", "cloud_concepts", "ports_protocols",
             "traffic_types", "ipv4_subnetting_np", "ipv6_np", "network_topologies"),
        ),
        Domain(
            "network_implementation", "2.0 Network Implementation", 0.20,
            ("routing_technologies", "switching_technologies", "wireless_standards",
             "physical_installations"),
        ),
        Domain(
            "network_operations", "3.0 Network Operations", 0.19,
            ("network_documentation", "network_monitoring", "disaster_recovery",
             "dns_dhcp_services", "snmp_logging_np"),
        ),
        Domain(
            "network_security", "4.0 Network Security", 0.14,
            ("security_concepts_np", "network_hardening", "remote_access",
             "physical_security_np"),
        ),
        Domain(
            "network_troubleshooting", "5.0 Network Troubleshooting", 0.24,
            ("troubleshooting_methodology", "cabling_issues", "connectivity_tools",
             "network_service_issues", "performance_issues"),
        ),
    ),
)

# --- CompTIA A+ Core 1 (220-1101) -------------------------------------------
APLUS1 = ExamBlueprint(
    code="aplus1",
    name="A+ Core 1 (220-1101)",
    domains=(
        Domain("mobile_devices", "1.0 Mobile Devices", 0.15,
               ("laptop_hardware", "mobile_display", "mobile_ports_accessories",
                "mobile_connectivity", "mobile_apps_sync")),
        Domain("networking_a1", "2.0 Networking", 0.20,
               ("ports_protocols_a1", "networking_hardware", "wireless_a1",
                "network_services_a1", "internet_connection_types")),
        Domain("hardware", "3.0 Hardware", 0.25,
               ("cables_connectors", "memory_ram", "storage_devices",
                "motherboards_cpu", "power_supplies", "peripherals", "printers")),
        Domain("virtualization_cloud", "4.0 Virtualization & Cloud Computing", 0.11,
               ("cloud_models", "client_side_virtualization")),
        Domain("hw_net_troubleshooting", "5.0 Hardware & Network Troubleshooting", 0.29,
               ("troubleshooting_methodology_a1", "hardware_troubleshooting",
                "display_troubleshooting", "network_troubleshooting_a1", "printer_troubleshooting")),
    ),
)

# --- CompTIA A+ Core 2 (220-1102) -------------------------------------------
APLUS2 = ExamBlueprint(
    code="aplus2",
    name="A+ Core 2 (220-1102)",
    domains=(
        Domain("operating_systems", "1.0 Operating Systems", 0.31,
               ("windows_editions", "windows_tools", "command_line", "os_features",
                "os_installation", "networking_os", "macos_linux")),
        Domain("security_a2", "2.0 Security", 0.25,
               ("security_concepts_a2", "malware_a2", "social_engineering_a2",
                "windows_security", "workstation_hardening", "data_destruction")),
        Domain("software_troubleshooting", "3.0 Software Troubleshooting", 0.22,
               ("windows_troubleshooting", "os_security_troubleshooting",
                "mobile_os_troubleshooting")),
        Domain("operational_procedures", "4.0 Operational Procedures", 0.22,
               ("documentation_a2", "change_management_a2", "backup_recovery", "safety",
                "incident_response_a2", "communication_professionalism", "scripting_basics")),
    ),
)

EXAMS: dict[str, ExamBlueprint] = {
    bp.code: bp for bp in (CCNA, ENCOR, SECPLUS, NETPLUS, APLUS1, APLUS2)
}

# Tracks that have a real question bank and are selectable in the UI. Blueprints
# for the rest exist (objectives captured) but stay "coming soon" until built.
LIVE_EXAMS: tuple[str, ...] = ("ccna", "encor", "secplus")


def get_blueprint(code: str) -> ExamBlueprint:
    try:
        return EXAMS[code]
    except KeyError:
        raise KeyError(f"Unknown exam code {code!r}; expected one of {list(EXAMS)}") from None
