"""Login/account storage: salted-hashed passwords, create/authenticate, claim."""
import json

import ui_common as U


def test_create_and_authenticate(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, err = U.create_account("Jordan Lee", "pass1234", "Jordan Lee")
    assert err is None
    assert slug == "jordan-lee"
    # username match is slug-insensitive to spacing/case
    assert U.authenticate("Jordan Lee", "pass1234") == slug
    assert U.authenticate("jordan-lee", "pass1234") == slug
    assert U.authenticate("Jordan Lee", "wrong") is None
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
    s2, _ = U.create_account("user1", "pw123456", "User One")
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


def test_default_is_always_instructor(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("sarge", "pw123456", "Sarge")        # first -> instructor
    U.create_account("default", "pw123456", "Default")    # would be a learner...
    assert U.is_instructor("default") is True             # ...but Default is forced instructor


def test_admin_create_reset_role_delete(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("default", "pw123456", "Default")    # instructor/admin
    slug, err = U.admin_create_account("user2", "temp1234", "learner")
    assert err is None and U.is_instructor(slug) is False
    U.set_role(slug, "instructor")
    assert U.is_instructor(slug) is True
    ok, err = U.set_password_admin(slug, "newpw123")
    assert ok and U.authenticate("user2", "newpw123") == slug
    U.delete_account(slug)
    assert slug not in U.list_users()
    assert not (tmp_path / slug).exists()


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
