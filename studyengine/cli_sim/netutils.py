"""IPv4 / wildcard math used by the simulator and the wildcard-mask drills."""
from __future__ import annotations

MAX32 = 0xFFFFFFFF


def is_valid_ipv4(s: str) -> bool:
    parts = str(s).split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        if not (0 <= int(p) <= 255):
            return False
        if len(p) > 1 and p[0] == "0":  # reject 01, 001 etc.
            return False
    return True


def ip_to_int(ip: str) -> int:
    a, b, c, d = (int(x) for x in ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def int_to_ip(n: int) -> str:
    n &= MAX32
    return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"


def mask_to_prefix(mask: str) -> int | None:
    """Return prefix length for a *contiguous* dotted mask, else None."""
    m = ip_to_int(mask)
    # Contiguous ones followed by zeros: m | (m-1 of the ones) ...
    # Validate: the complement+1 must be a power of two.
    inv = (~m) & MAX32
    if inv & (inv + 1):  # not all-ones in the low bits -> non-contiguous
        return None
    return bin(m).count("1")


def prefix_to_mask(prefix: int) -> str:
    if not (0 <= prefix <= 32):
        raise ValueError("prefix must be 0..32")
    m = (MAX32 << (32 - prefix)) & MAX32 if prefix else 0
    return int_to_ip(m)


def prefix_to_wildcard(prefix: int) -> str:
    return int_to_ip((~ip_to_int(prefix_to_mask(prefix))) & MAX32)


def mask_to_wildcard(mask: str) -> str:
    return int_to_ip((~ip_to_int(mask)) & MAX32)


def wildcard_to_mask(wild: str) -> str:
    return int_to_ip((~ip_to_int(wild)) & MAX32)


def network_of(ip: str, mask: str) -> str:
    return int_to_ip(ip_to_int(ip) & ip_to_int(mask))


def broadcast_of(ip: str, mask: str) -> str:
    return int_to_ip(ip_to_int(ip) | ((~ip_to_int(mask)) & MAX32))


def same_subnet(ip1: str, ip2: str, mask: str) -> bool:
    return network_of(ip1, mask) == network_of(ip2, mask)


def wildcard_match(ip: str, network: str, wildcard: str) -> bool:
    """True if `ip` is permitted by an ACL/OSPF `network wildcard` clause.

    Only bits where the wildcard bit is 0 ("care" bits) must match.
    """
    care = (~ip_to_int(wildcard)) & MAX32
    return (ip_to_int(ip) & care) == (ip_to_int(network) & care)


def wildcard_specificity(wildcard: str) -> int:
    """Number of 'care' bits (wildcard 0 bits). Higher = more specific match."""
    return bin((~ip_to_int(wildcard)) & MAX32).count("1")


def usable_hosts(prefix: int) -> int:
    if prefix >= 31:
        return 0 if prefix == 32 else 2  # /31 = 2 usable (RFC 3021), /32 = host route
    return (1 << (32 - prefix)) - 2
