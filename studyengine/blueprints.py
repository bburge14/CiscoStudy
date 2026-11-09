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

# --- AWS Certified Cloud Practitioner (CLF-C02) -----------------------------
CLF = ExamBlueprint(
    code="clf",
    name="Cloud Practitioner (CLF-C02)",
    domains=(
        Domain("cloud_concepts", "1.0 Cloud Concepts", 0.24,
               ("cloud_benefits", "well_architected", "migration_caf", "cloud_economics")),
        Domain("security_compliance", "2.0 Security and Compliance", 0.30,
               ("shared_responsibility", "compliance_governance", "iam", "security_services")),
        Domain("cloud_technology", "3.0 Cloud Technology and Services", 0.34,
               ("global_infrastructure", "compute_services", "storage_services",
                "database_services", "networking_services", "deployment_access", "other_services")),
        Domain("billing_support", "4.0 Billing, Pricing, and Support", 0.12,
               ("pricing_models", "billing_cost_management", "support_plans", "technical_resources")),
    ),
)

# --- Microsoft Azure Fundamentals (AZ-900) ----------------------------------
AZ900 = ExamBlueprint(
    code="az900",
    name="Azure Fundamentals (AZ-900)",
    domains=(
        Domain("az_cloud_concepts", "1.0 Cloud Concepts", 0.28,
               ("az_cloud_models", "az_cloud_benefits", "az_service_types")),
        Domain("az_architecture_services", "2.0 Azure Architecture and Services", 0.38,
               ("az_core_architecture", "az_compute_networking", "az_storage", "az_identity")),
        Domain("az_management_governance", "3.0 Azure Management and Governance", 0.34,
               ("az_cost_management", "az_governance_compliance", "az_tools_monitoring")),
    ),
)

# --- CompTIA CySA+ (CS0-003) -------------------------------------------------
CYSA = ExamBlueprint(
    code="cysa",
    name="CySA+ CS0-003",
    domains=(
        Domain("cysa_security_operations", "1.0 Security Operations", 0.33,
               ("so_system_network_analysis", "so_threat_intel", "so_threat_hunting",
                "so_malicious_activity", "so_tools_automation")),
        Domain("cysa_vuln_management", "2.0 Vulnerability Management", 0.30,
               ("vm_scanning", "vm_assessment_tools", "vm_prioritization",
                "vm_mitigation", "vm_secure_coding")),
        Domain("cysa_incident_response", "3.0 Incident Response and Management", 0.20,
               ("ir_lifecycle", "ir_detection_analysis", "ir_containment_recovery")),
        Domain("cysa_reporting_comm", "4.0 Reporting and Communication", 0.17,
               ("rc_vuln_reporting", "rc_incident_reporting", "rc_metrics", "rc_stakeholder_comm")),
    ),
)

# --- CompTIA PenTest+ (PT0-003) ---------------------------------------------
PENTEST = ExamBlueprint(
    code="pentest",
    name="PenTest+ PT0-003",
    domains=(
        Domain("pt_engagement", "1.0 Engagement Management", 0.13,
               ("pt_scoping_roe", "pt_methodologies", "pt_grc_legal", "pt_reporting_comm")),
        Domain("pt_recon", "2.0 Reconnaissance and Enumeration", 0.21,
               ("pt_passive_recon", "pt_active_recon", "pt_enumeration", "pt_recon_tools")),
        Domain("pt_vuln_discovery", "3.0 Vulnerability Discovery and Analysis", 0.17,
               ("pt_vuln_scanning", "pt_vuln_analysis", "pt_vuln_types")),
        Domain("pt_attacks", "4.0 Attacks and Exploits", 0.35,
               ("pt_network_attacks", "pt_web_attacks", "pt_auth_attacks",
                "pt_wireless_social", "pt_cloud_specialized")),
        Domain("pt_post_exploit", "5.0 Post-exploitation and Lateral Movement", 0.14,
               ("pt_post_access", "pt_lateral_movement", "pt_persistence_stealth", "pt_cleanup_exfil")),
    ),
)

# --- (ISC)² Certified in Cybersecurity (CC) ---------------------------------
ISC2CC = ExamBlueprint(
    code="isc2cc",
    name="(ISC)² Certified in Cybersecurity (CC)",
    domains=(
        Domain("cc_security_principles", "1.0 Security Principles", 0.26,
               ("cc_cia_triad", "cc_risk_management", "cc_security_controls",
                "cc_isc2_ethics", "cc_governance_policies")),
        Domain("cc_bcdr_ir", "2.0 BC, DR & Incident Response Concepts", 0.10,
               ("cc_incident_response", "cc_business_continuity", "cc_disaster_recovery")),
        Domain("cc_access_controls", "3.0 Access Controls Concepts", 0.22,
               ("cc_access_control_concepts", "cc_physical_access",
                "cc_logical_access", "cc_identity_management")),
        Domain("cc_network_security", "4.0 Network Security", 0.24,
               ("cc_network_concepts", "cc_network_threats_attacks",
                "cc_network_defense", "cc_secure_infrastructure")),
        Domain("cc_security_operations", "5.0 Security Operations", 0.18,
               ("cc_data_security", "cc_system_hardening", "cc_security_policies_ops",
                "cc_security_awareness", "cc_encryption_basics")),
    ),
)

# --- Cisco CyberOps Associate (CBROPS 200-201) ------------------------------
CBROPS = ExamBlueprint(
    code="cbrops",
    name="CyberOps Associate (CBROPS 200-201)",
    domains=(
        Domain("cbr_security_concepts", "1.0 Security Concepts", 0.20,
               ("cbr_cia_defense", "cbr_security_terms", "cbr_access_control_models",
                "cbr_cvss", "cbr_risk_terms", "cbr_soc_analysis_tools")),
        Domain("cbr_security_monitoring", "2.0 Security Monitoring", 0.25,
               ("cbr_data_types", "cbr_attack_surface_vectors", "cbr_network_telemetry",
                "cbr_detection_methods", "cbr_evasion_obfuscation", "cbr_certificates_crypto")),
        Domain("cbr_host_analysis", "3.0 Host-Based Analysis", 0.20,
               ("cbr_endpoint_technologies", "cbr_os_components", "cbr_logs_artifacts",
                "cbr_malware_analysis", "cbr_evidence_attribution")),
        Domain("cbr_network_intrusion", "4.0 Network Intrusion Analysis", 0.20,
               ("cbr_packet_session_analysis", "cbr_protocol_headers", "cbr_ids_ips_events",
                "cbr_firewall_filtering", "cbr_intrusion_artifacts")),
        Domain("cbr_policies_procedures", "5.0 Security Policies and Procedures", 0.15,
               ("cbr_incident_handling_nist", "cbr_attack_frameworks", "cbr_chain_of_custody",
                "cbr_csirt_metrics", "cbr_runbook_automation")),
    ),
)

# --- Microsoft Security, Compliance & Identity Fundamentals (SC-900) ---------
SC900 = ExamBlueprint(
    code="sc900",
    name="Security, Compliance & Identity Fundamentals (SC-900)",
    domains=(
        Domain("sc9_concepts", "1.0 Concepts of Security, Compliance & Identity", 0.13,
               ("sc9_security_methodologies", "sc9_identity_concepts",
                "sc9_encryption_hashing", "sc9_governance_concepts")),
        Domain("sc9_entra", "2.0 Capabilities of Microsoft Entra", 0.28,
               ("sc9_entra_identity_types", "sc9_entra_authentication",
                "sc9_entra_access_management", "sc9_entra_identity_protection")),
        Domain("sc9_security", "3.0 Capabilities of Microsoft Security Solutions", 0.37,
               ("sc9_azure_security", "sc9_defender_for_cloud", "sc9_sentinel",
                "sc9_defender_xdr", "sc9_security_baselines")),
        Domain("sc9_compliance", "4.0 Capabilities of Microsoft Compliance Solutions", 0.22,
               ("sc9_purview_governance", "sc9_purview_protection", "sc9_insider_ediscovery",
                "sc9_compliance_management", "sc9_priva_privacy")),
    ),
)

# --- (ISC)² CISSP -----------------------------------------------------------
CISSP = ExamBlueprint(
    code="cissp",
    name="(ISC)² CISSP",
    domains=(
        Domain("cissp_srm", "1.0 Security and Risk Management", 0.16,
               ("cissp_cia_governance", "cissp_compliance_legal", "cissp_risk_management",
                "cissp_security_policies", "cissp_bcp_dr", "cissp_ethics_personnel")),
        Domain("cissp_asset", "2.0 Asset Security", 0.10,
               ("cissp_data_classification", "cissp_data_lifecycle",
                "cissp_data_roles", "cissp_data_protection_methods")),
        Domain("cissp_arch_eng", "3.0 Security Architecture and Engineering", 0.13,
               ("cissp_security_models", "cissp_crypto", "cissp_security_capabilities",
                "cissp_vuln_architectures", "cissp_physical_security")),
        Domain("cissp_comm_net", "4.0 Communication and Network Security", 0.13,
               ("cissp_secure_network_design", "cissp_network_components",
                "cissp_secure_channels", "cissp_network_attacks")),
        Domain("cissp_iam", "5.0 Identity and Access Management (IAM)", 0.13,
               ("cissp_identity_lifecycle", "cissp_authentication_methods",
                "cissp_access_control_models", "cissp_federated_identity")),
        Domain("cissp_assess_test", "6.0 Security Assessment and Testing", 0.12,
               ("cissp_assessment_strategies", "cissp_security_testing",
                "cissp_audit_logging", "cissp_test_outputs")),
        Domain("cissp_sec_ops", "7.0 Security Operations", 0.13,
               ("cissp_investigations", "cissp_logging_monitoring", "cissp_incident_management",
                "cissp_dr_recovery", "cissp_change_config_mgmt")),
        Domain("cissp_software_dev", "8.0 Software Development Security", 0.10,
               ("cissp_sdlc_security", "cissp_secure_coding",
                "cissp_software_vulns", "cissp_devsecops")),
    ),
)

# --- ISACA CISM -------------------------------------------------------------
CISM = ExamBlueprint(
    code="cism",
    name="ISACA CISM",
    domains=(
        Domain("cism_governance", "1.0 Information Security Governance", 0.17,
               ("cism_governance_framework", "cism_strategy_alignment",
                "cism_roles_responsibilities", "cism_legal_regulatory")),
        Domain("cism_risk", "2.0 Information Security Risk Management", 0.20,
               ("cism_risk_assessment", "cism_risk_response", "cism_risk_monitoring",
                "cism_asset_classification")),
        Domain("cism_program", "3.0 Information Security Program", 0.33,
               ("cism_program_development", "cism_security_controls", "cism_program_frameworks",
                "cism_awareness_training", "cism_metrics_reporting", "cism_third_party_mgmt")),
        Domain("cism_incident", "4.0 Incident Management", 0.30,
               ("cism_incident_readiness", "cism_incident_response_plan", "cism_bcp_dr",
                "cism_containment_eradication", "cism_post_incident_review")),
    ),
)

# --- ISACA CISA -------------------------------------------------------------
CISA = ExamBlueprint(
    code="cisa",
    name="ISACA CISA",
    domains=(
        Domain("cisa_audit_process", "1.0 Information Systems Auditing Process", 0.18,
               ("cisa_audit_standards", "cisa_risk_based_audit", "cisa_audit_execution",
                "cisa_evidence_sampling", "cisa_audit_reporting")),
        Domain("cisa_governance", "2.0 Governance and Management of IT", 0.18,
               ("cisa_it_governance", "cisa_it_strategy_policies", "cisa_org_structure",
                "cisa_risk_management", "cisa_bcp")),
        Domain("cisa_acquisition_dev", "3.0 IS Acquisition, Development and Implementation", 0.12,
               ("cisa_project_management", "cisa_sdlc", "cisa_system_migration",
                "cisa_post_implementation")),
        Domain("cisa_operations_resilience", "4.0 IS Operations and Business Resilience", 0.26,
               ("cisa_it_operations", "cisa_system_interfaces", "cisa_data_backup_recovery",
                "cisa_disaster_recovery", "cisa_incident_problem_mgmt", "cisa_database_mgmt")),
        Domain("cisa_protection_assets", "5.0 Protection of Information Assets", 0.26,
               ("cisa_access_controls", "cisa_network_security", "cisa_data_classification",
                "cisa_encryption_pki", "cisa_security_monitoring", "cisa_physical_environmental")),
    ),
)

# --- (ISC)² SSCP ------------------------------------------------------------
SSCP = ExamBlueprint(
    code="sscp",
    name="(ISC)² SSCP",
    domains=(
        Domain("sscp_secops_admin", "1.0 Security Operations and Administration", 0.16,
               ("sscp_cia_ethics", "sscp_security_controls", "sscp_asset_change_mgmt",
                "sscp_security_awareness", "sscp_data_handling")),
        Domain("sscp_access_controls", "2.0 Access Controls", 0.15,
               ("sscp_authn_methods", "sscp_trust_architectures",
                "sscp_identity_lifecycle", "sscp_access_control_models")),
        Domain("sscp_risk", "3.0 Risk Identification, Monitoring, and Analysis", 0.15,
               ("sscp_risk_management", "sscp_monitoring_analysis",
                "sscp_security_assessment", "sscp_siem_logging")),
        Domain("sscp_incident_response", "4.0 Incident Response and Recovery", 0.14,
               ("sscp_incident_handling", "sscp_forensics", "sscp_bcp_dr")),
        Domain("sscp_cryptography", "5.0 Cryptography", 0.09,
               ("sscp_crypto_concepts", "sscp_pki", "sscp_key_management")),
        Domain("sscp_network_security", "6.0 Network and Communications Security", 0.16,
               ("sscp_network_models", "sscp_network_attacks", "sscp_network_defense",
                "sscp_wireless_cellular")),
        Domain("sscp_systems_app", "7.0 Systems and Application Security", 0.15,
               ("sscp_malware_endpoint", "sscp_cloud_security",
                "sscp_virtualization_security", "sscp_mobile_iot_security")),
    ),
)

# --- EC-Council CEH (Certified Ethical Hacker, v13) -------------------------
# Conceptual / exam-aligned only: identify the tool, phase, or technique in an
# AUTHORIZED-assessment framing. No weaponized payloads or working exploit code.
# The 9 official CEH domains are consolidated into 6 engine domains that respect
# the official groupings and weighting.
CEH = ExamBlueprint(
    code="ceh",
    name="EC-Council CEH v13",
    domains=(
        Domain("ceh_intro_recon", "1.0 Overview, Reconnaissance and Scanning", 0.22,
               ("ceh_ethics_overview", "ceh_footprinting", "ceh_scanning",
                "ceh_enumeration", "ceh_vuln_analysis")),
        Domain("ceh_system_malware", "2.0 System Hacking and Malware", 0.17,
               ("ceh_system_hacking", "ceh_malware_threats")),
        Domain("ceh_network_perimeter", "3.0 Network and Perimeter Hacking", 0.24,
               ("ceh_sniffing", "ceh_social_engineering", "ceh_dos_ddos",
                "ceh_session_hijacking", "ceh_evading_ids_fw")),
        Domain("ceh_web_hacking", "4.0 Web Application Hacking", 0.16,
               ("ceh_web_servers", "ceh_web_apps", "ceh_sql_injection")),
        Domain("ceh_wireless_mobile", "5.0 Wireless, Mobile, IoT and OT Hacking", 0.13,
               ("ceh_wireless", "ceh_mobile_platforms", "ceh_iot_ot")),
        Domain("ceh_cloud_crypto", "6.0 Cloud Computing and Cryptography", 0.08,
               ("ceh_cloud_computing", "ceh_cryptography")),
    ),
)

# --- Microsoft SC-200 (Security Operations Analyst) -------------------------
# Organized by the durable product/skill areas the exam tests (Defender XDR,
# Defender for Cloud, Microsoft Sentinel, KQL hunting & threat intelligence).
SC200 = ExamBlueprint(
    code="sc200",
    name="Security Operations Analyst (SC-200)",
    domains=(
        Domain("sc200_defender_xdr", "1.0 Mitigate threats with Microsoft Defender XDR", 0.30,
               ("sc200_mde_endpoint", "sc200_mdo_office365", "sc200_mdi_identity",
                "sc200_mdca_cloudapps", "sc200_xdr_incidents")),
        Domain("sc200_defender_cloud", "2.0 Mitigate threats with Microsoft Defender for Cloud", 0.17,
               ("sc200_dfc_posture", "sc200_dfc_workloads", "sc200_dfc_alerts")),
        Domain("sc200_sentinel", "3.0 Mitigate threats with Microsoft Sentinel", 0.38,
               ("sc200_sentinel_setup", "sc200_sentinel_connectors", "sc200_sentinel_analytics",
                "sc200_sentinel_soar", "sc200_sentinel_incidents")),
        Domain("sc200_hunting_intel", "4.0 Threat Hunting and Intelligence (KQL)", 0.15,
               ("sc200_kql", "sc200_advanced_hunting", "sc200_custom_detections",
                "sc200_threat_intel")),
    ),
)

# --- Microsoft AZ-500 (Azure Security Engineer) -----------------------------
AZ500 = ExamBlueprint(
    code="az500",
    name="Azure Security Engineer (AZ-500)",
    domains=(
        Domain("az500_identity_access", "1.0 Manage Identity and Access", 0.28,
               ("az500_entra_identities", "az500_entra_authn_authz",
                "az500_rbac_pim", "az500_app_identity")),
        Domain("az500_networking", "2.0 Secure Networking", 0.22,
               ("az500_network_security", "az500_private_connectivity", "az500_edge_protection")),
        Domain("az500_compute_storage_db", "3.0 Secure Compute, Storage, and Databases", 0.25,
               ("az500_compute_security", "az500_storage_security",
                "az500_database_security", "az500_key_vault")),
        Domain("az500_security_operations", "4.0 Manage Security Operations", 0.25,
               ("az500_defender_for_cloud", "az500_sentinel_ops",
                "az500_monitoring_logging", "az500_governance_policy")),
    ),
)

# --- CompTIA SecurityX (CAS-005, formerly CASP+) ----------------------------
SECURITYX = ExamBlueprint(
    code="securityx",
    name="CompTIA SecurityX (CAS-005)",
    domains=(
        Domain("scx_grc", "1.0 Governance, Risk, and Compliance", 0.20,
               ("scx_risk_management", "scx_compliance_frameworks", "scx_governance_policies",
                "scx_third_party_risk", "scx_data_governance")),
        Domain("scx_architecture", "2.0 Security Architecture", 0.27,
               ("scx_secure_architecture", "scx_zero_trust", "scx_cloud_hybrid_arch",
                "scx_resilience_ha", "scx_data_security_arch", "scx_iam_architecture")),
        Domain("scx_engineering", "3.0 Security Engineering", 0.31,
               ("scx_cryptography", "scx_pki", "scx_secure_integration", "scx_endpoint_security",
                "scx_emerging_tech", "scx_secure_coding", "scx_automation")),
        Domain("scx_operations", "4.0 Security Operations", 0.22,
               ("scx_threat_hunting", "scx_incident_response", "scx_vuln_management",
                "scx_monitoring_detection", "scx_forensics")),
    ),
)

EXAMS: dict[str, ExamBlueprint] = {
    bp.code: bp for bp in (CCNA, ENCOR, SECPLUS, NETPLUS, APLUS1, APLUS2, CLF, AZ900, CYSA,
                           PENTEST, ISC2CC, CBROPS, SC900, CISSP, CISM, CISA, SSCP, CEH,
                           SC200, AZ500, SECURITYX)
}

# Tracks that have a real question bank and are selectable in the UI. Blueprints
# for the rest exist (objectives captured) but stay "coming soon" until built.
LIVE_EXAMS: tuple[str, ...] = (
    "ccna", "encor", "secplus", "netplus", "aplus1", "aplus2", "clf", "az900", "cysa", "pentest",
)


def get_blueprint(code: str) -> ExamBlueprint:
    try:
        return EXAMS[code]
    except KeyError:
        raise KeyError(f"Unknown exam code {code!r}; expected one of {list(EXAMS)}") from None
