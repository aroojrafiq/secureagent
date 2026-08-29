"""Synthetic service layer for profile-name decoding.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module deliberately delegates to an unsafe decoder for evaluation purposes only.
"""

from .decoder import decode_profile_payload


def get_profile_name(payload: bytes) -> str:
    decoded = decode_profile_payload(payload)
    return decoded["name"]
