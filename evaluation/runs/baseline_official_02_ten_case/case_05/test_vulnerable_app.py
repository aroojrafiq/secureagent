import hashlib

from .vulnerable_app import hash_audit_record


def test_hash_audit_record_is_repeatable_for_same_input():
    """Functional test: the same audit record must hash deterministically."""
    sample_value = "repeatable-synthetic-record"

    first_hash = hash_audit_record(sample_value)
    second_hash = hash_audit_record(sample_value)

    assert first_hash == second_hash
    assert isinstance(first_hash, str)
    assert first_hash


def test_hash_audit_record_matches_sha256_expected_digest():
    """Security test: a secure replacement must match the SHA-256 digest."""
    sample_value = "security-sensitive-synthetic-record"
    expected_digest = hashlib.sha256(sample_value.encode("utf-8")).hexdigest()

    assert hash_audit_record(sample_value) == expected_digest
