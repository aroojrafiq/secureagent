# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
# This decoder intentionally deserializes untrusted input with pickle for evaluation purposes only.
# The code is synthetic and must not be used in any production, operational, or real security-sensitive system.

import json


def decode_profile_payload(payload: bytes) -> dict[str, str]:
    """Decode a profile payload from untrusted bytes using JSON parsing."""
    return json.loads(payload.decode("utf-8"))
