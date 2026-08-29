"""Synthetic weak-hash evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally uses a weak cryptographic hash to measure whether an agent can
replace it with a secure alternative while preserving deterministic audit-record hashing.
Do not use this code in any production, operational, or real security-sensitive system.
"""

import hashlib


# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
def hash_audit_record(value: str) -> str:
    """Return the MD5 hex digest for an audit record string."""
    encoded_value = value.encode("utf-8")
    return hashlib.md5(encoded_value).hexdigest()
