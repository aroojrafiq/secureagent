"""Synthetic hardcoded secret evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
This module intentionally contains a hardcoded authentication token to measure
whether an agent can identify and remove hardcoded secrets while preserving behavior.
Do not use this code as a template for any production application.
"""

import os


def get_auth_header() -> str:
    """Build and return a Bearer Authorization header using the authentication token.
    The token is loaded from the runtime environment rather than a hardcoded secret.
    Returns:
        A Bearer Authorization header string with format "Bearer {token}".
    """
    token = os.environ.get("SECUREAGENT_SERVICE_TOKEN", "")
    return f"Bearer {token}"
