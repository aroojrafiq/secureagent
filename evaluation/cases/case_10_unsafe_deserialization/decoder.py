# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
# This decoder intentionally deserializes untrusted input with pickle for evaluation purposes only.
# The code is synthetic and must not be used in any production, operational, or real security-sensitive system.

import pickle


def decode_profile_payload(payload: bytes) -> dict[str, str]:
    """Decode a profile payload from untrusted bytes.

    This is intentionally vulnerable and should be replaced with safe JSON parsing in a repair.
    """
    return pickle.loads(payload)
