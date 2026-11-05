"""Login/account storage: salted-hashed passwords, create/authenticate, claim."""
import json

import ui_common as U


def test_create_and_authenticate(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, err = U.create_account("A1C Smith", "pass1234", "Airman Smith")
    assert err is None
    assert slug == "a1c-smith"
    # username match is slug-insensitive to spacing/case
    assert U.authenticate("A1C Smith", "pass1234") == slug
    assert U.authenticate("a1c-smith", "pass1234") == slug
    assert U.authenticate("A1C Smith", "wrong") is None
    assert U.authenticate("nobody", "pass1234") is None


def test_duplicate_username_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("bob", "secret12")
    slug, err = U.create_account("Bob", "another1")
    assert slug is None and "taken" in err.lower()


def test_short_password_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, err = U.create_account("carol", "ab")
    assert slug is None and "4 char" in err.lower()


def test_password_not_stored_in_clear(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("dave", "SuperSecret9", "Dave")
    reg = json.loads((tmp_path / "users.json").read_text())
    assert "SuperSecret9" not in json.dumps(reg)
    assert reg["dave"]["hash"] and reg["dave"]["salt"]
    # same password hashes differently thanks to a random salt
    salt2, hash2 = U._hash_pw("SuperSecret9")
    assert hash2 != reg["dave"]["hash"]


def test_first_account_is_instructor(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    s1, _ = U.create_account("sarge", "pw123456", "Sarge")
    s2, _ = U.create_account("airman1", "pw123456", "Airman One")
    assert U.is_instructor(s1) is True
    assert U.is_instructor(s2) is False


def test_claimed_first_profile_becomes_instructor(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    (tmp_path / "default").mkdir(parents=True)
    (tmp_path / "default" / "profile_ccna.json").write_text("{}")
    got, err = U.claim_profile("default", "pw123456")
    assert err is None and U.is_instructor("default") is True


def test_roster_summary_lists_accounts_with_roles(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("inst", "pw123456", "Inst")
    U.create_account("learner1", "pw123456", "Learner One")
    rows = U.roster_summary("ccna")
    roles = {r["name"]: r["role"] for r in rows}
    assert roles.get("Inst") == "instructor"
    assert roles.get("Learner One") == "learner"
    # every row has the summary fields the instructor table needs
    assert all({"answered", "accuracy", "baseline", "weak", "last_seen"} <= set(r) for r in rows)


def test_claim_legacy_profile_keeps_data(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    # a pre-existing, password-less profile folder with saved progress
    (tmp_path / "default").mkdir(parents=True)
    (tmp_path / "default" / "profile_ccna.json").write_text("{}")
    assert "default" in U.passwordless_profiles()
    got, err = U.claim_profile("default", "newpass1")
    assert err is None and got == "default"
    assert U.authenticate("default", "newpass1") == "default"
    assert "default" not in U.passwordless_profiles()
    # the data folder (and its file) is preserved
    assert (tmp_path / "default" / "profile_ccna.json").exists()
