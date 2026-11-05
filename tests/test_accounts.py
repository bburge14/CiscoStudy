"""Login/account storage: salted-hashed passwords, create/authenticate, claim."""
import json

import ui_common as U
from studyengine import load_bank
from studyengine.progress import Profile

_BANK = load_bank()


def _seed_learner(tmp_path, slug="learner1", exam="ccna"):
    """A learner with real study progress AND a diagnostic benchmark on disk."""
    ccna = [q for q in _BANK.all() if q.exam == exam]
    prof = Profile(exam=exam)
    # 3 benchmark questions (recorded + noted as baseline -> excluded from study)
    for q in ccna[:3]:
        prof.record(q, True)
        prof.note_baseline_answer(q, True)
    prof.baseline = {"overall": 50, "total": 3}
    # 5 study answers -> earns XP and counts toward study metrics
    for q in ccna[3:8]:
        prof.record_study(q, True)
    (tmp_path / slug).mkdir(parents=True, exist_ok=True)
    prof.save(tmp_path / slug / f"profile_{exam}.json")
    return prof


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


def test_admin_reset_progress_wipes_everything(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("learner1", "pw123456", "Learner One")
    seeded = _seed_learner(tmp_path)
    assert seeded.xp > 0 and seeded.study_overall()[0] > 0 and seeded.baseline

    assert U.admin_reset_progress("learner1", "ccna") is True
    fresh = U.load_user_profile("learner1", "ccna")
    assert fresh.xp == 0.0
    assert fresh.study_overall() == (0, 0)
    assert fresh.overall() == (0, 0)
    assert fresh.baseline is None
    assert fresh.q == {}

    # unknown account -> no-op, reported as failure
    assert U.admin_reset_progress("nobody", "ccna") is False


def test_admin_reset_benchmark_keeps_study_and_exclusion(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("learner1", "pw123456", "Learner One")
    seeded = _seed_learner(tmp_path)
    xp_before = seeded.xp
    study_before = seeded.study_overall()
    assert xp_before > 0 and study_before[0] == 5    # 5 study answers

    assert U.admin_reset_benchmark("learner1", "ccna") is True
    after = U.load_user_profile("learner1", "ccna")
    # benchmark result is gone -> diagnostic is re-takeable
    assert after.baseline is None
    # study progress untouched: XP and answered count preserved...
    assert after.xp == xp_before
    assert after.study_overall() == study_before
    # ...and the old benchmark answers are STILL excluded (not inflating study)
    assert after.baseline_stats is not None
    assert after.study_overall()[0] < after.overall()[0]

    assert U.admin_reset_benchmark("nobody", "ccna") is False


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


# --- self-service account editing -------------------------------------------
def test_rename_account_changes_login_keeps_role_and_data(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("default", "pw123456", "Default")      # instructor/admin
    (tmp_path / "default" / "profile_ccna.json").write_text('{"marker": 1}')
    new_slug, err = U.rename_account("default", "Brad Burge")
    assert err is None and new_slug == "brad-burge"
    assert "default" not in U.list_users()
    assert U.is_instructor("brad-burge") is True            # role carried over
    # saved progress moved with the login
    assert not (tmp_path / "default").exists()
    assert (tmp_path / "brad-burge" / "profile_ccna.json").read_text() == '{"marker": 1}'
    # sign in with the new username and the same password
    assert U.authenticate("Brad Burge", "pw123456") == "brad-burge"


def test_rename_rejects_taken_and_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    U.create_account("alice", "pw123456", "Alice")
    U.create_account("bob", "pw123456", "Bob")
    _, err = U.rename_account("alice", "Bob")
    assert err and "taken" in err.lower()
    _, err = U.rename_account("alice", "   ")
    assert err and "username" in err.lower()


def test_change_password_requires_current(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, _ = U.create_account("casey", "oldpw123", "Casey")
    ok, err = U.change_password(slug, "wrongpw", "newpw123")
    assert not ok and "incorrect" in err.lower()
    ok, err = U.change_password(slug, "oldpw123", "newpw123")
    assert ok and err is None
    assert U.authenticate("casey", "newpw123") == slug
    assert U.authenticate("casey", "oldpw123") is None


def test_change_password_min_length(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, _ = U.create_account("dana", "oldpw123", "Dana")
    ok, err = U.change_password(slug, "oldpw123", "no")
    assert not ok and "4 char" in err.lower()


def test_set_display_name(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, _ = U.create_account("erin", "pw123456", "Erin")
    assert U.set_display_name(slug, "Erin Q. Public")
    assert U.list_users()[slug]["name"] == "Erin Q. Public"
    assert U.set_display_name(slug, "   ") is False


def test_cannot_delete_or_demote_last_instructor(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "USERDATA", tmp_path)
    slug, _ = U.create_account("solo", "pw123456", "Solo")   # the only instructor
    assert U.is_instructor(slug)
    assert U.delete_account(slug) is False
    assert slug in U.list_users()
    assert U.set_role(slug, "learner") is False
    assert U.is_instructor(slug) is True
    # with a second instructor, demotion/deletion is allowed again
    U.create_account("second", "pw123456", "Second")
    U.set_role("second", "instructor")
    assert U.set_role(slug, "learner") is True
