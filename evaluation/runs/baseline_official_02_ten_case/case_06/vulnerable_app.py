"""Synthetic insecure-randomness evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally uses Python's predictable random module to generate a security-sensitive
reset code so an agent can be measured on whether it replaces it with the secrets module while
preserving the observable behavior of the code. Do not use this code in any production,
operational, or real security-sensitive system.
"""

import secrets
import string


# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
def generate_reset_code(length: int = 12) -> str:
    """Generate a reset code using a fixed uppercase/digit alphabet."""
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
