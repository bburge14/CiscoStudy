"""Credential wallet: self-reported cert status + its one-time XP bonus."""
from studyengine.leveling import XP_PER_EARNED_CERT, compute_xp, profile_level
from studyengine.progress import Profile


def test_earned_cert_grants_fixed_bonus():
    base = compute_xp(Profile(exam="cissp"))
    p = Profile(exam="cissp")
    p.cert_status = "earned"
    assert compute_xp(p) - base == XP_PER_EARNED_CERT


def test_nonearned_statuses_grant_no_xp():
    base = compute_xp(Profile(exam="cissp"))
    for status in ("", "planned", "studying"):
        p = Profile(exam="cissp")
        p.cert_status = status
        assert compute_xp(p) == base, status


def test_earned_cert_can_raise_rank():
    plain = profile_level(Profile(exam="cissp"))
    earned = Profile(exam="cissp")
    earned.cert_status = "earned"
    assert profile_level(earned).level >= plain.level
    # +600 clears the first rank threshold (400) from zero
    assert profile_level(earned).level > plain.level


def test_cert_status_and_date_round_trip():
    p = Profile(exam="secplus")
    p.cert_status = "earned"
    p.cert_date = "2026-03-14"
    r = Profile.from_dict(p.to_dict())
    assert (r.cert_status, r.cert_date) == ("earned", "2026-03-14")
    assert compute_xp(r) == compute_xp(p)


def test_legacy_profile_defaults_empty_cert_fields():
    # a profile saved before the wallet existed has no cert_* keys
    r = Profile.from_dict({"exam": "ccna", "xp": 50.0, "q": {}})
    assert r.cert_status == ""
    assert r.cert_date == ""
    # and it still computes XP (no crash)
    assert compute_xp(r) == 50
