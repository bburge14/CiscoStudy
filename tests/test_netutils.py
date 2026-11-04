from studyengine.cli_sim import netutils as nu


def test_ip_int_roundtrip():
    for ip in ("10.1.1.1", "192.168.0.255", "0.0.0.0", "255.255.255.255"):
        assert nu.int_to_ip(nu.ip_to_int(ip)) == ip


def test_mask_to_prefix_contiguous():
    assert nu.mask_to_prefix("255.255.255.0") == 24
    assert nu.mask_to_prefix("255.255.255.192") == 26
    assert nu.mask_to_prefix("255.255.255.252") == 30
    assert nu.mask_to_prefix("255.255.255.255") == 32
    assert nu.mask_to_prefix("0.0.0.0") == 0


def test_mask_to_prefix_noncontiguous_is_none():
    assert nu.mask_to_prefix("255.255.0.255") is None


def test_prefix_helpers():
    assert nu.prefix_to_mask(26) == "255.255.255.192"
    assert nu.prefix_to_wildcard(26) == "0.0.0.63"
    assert nu.prefix_to_wildcard(22) == "0.0.3.255"
    assert nu.mask_to_wildcard("255.255.252.0") == "0.0.3.255"


def test_network_and_broadcast():
    assert nu.network_of("172.16.20.75", "255.255.255.192") == "172.16.20.64"
    assert nu.broadcast_of("172.16.20.75", "255.255.255.192") == "172.16.20.127"
    assert nu.same_subnet("10.1.12.1", "10.1.12.2", "255.255.255.252")
    assert not nu.same_subnet("10.1.12.1", "10.1.12.5", "255.255.255.252")


def test_wildcard_match():
    # /22 block 10.1.0.0 - 10.1.3.255
    assert nu.wildcard_match("10.1.3.255", "10.1.0.0", "0.0.3.255")
    assert not nu.wildcard_match("10.1.4.0", "10.1.0.0", "0.0.3.255")
    # host match
    assert nu.wildcard_match("10.1.1.17", "10.1.1.17", "0.0.0.0")
    assert not nu.wildcard_match("10.1.1.18", "10.1.1.17", "0.0.0.0")


def test_usable_hosts():
    assert nu.usable_hosts(24) == 254
    assert nu.usable_hosts(26) == 62
    assert nu.usable_hosts(30) == 2
    assert nu.usable_hosts(31) == 2
    assert nu.usable_hosts(32) == 0


def test_is_valid_ipv4():
    assert nu.is_valid_ipv4("10.0.0.1")
    assert not nu.is_valid_ipv4("10.0.0.256")
    assert not nu.is_valid_ipv4("10.0.0")
    assert not nu.is_valid_ipv4("10.0.0.01")  # leading zero rejected
