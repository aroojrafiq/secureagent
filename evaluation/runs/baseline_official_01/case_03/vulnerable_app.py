"""Synthetic hardcoded secret evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
This module intentionally contains a hardcoded authentication token to measure
whether an agent can identify and remove hardcoded secrets while preserving behavior.
Do not use this code as a template for any production application.
"""

import os


def get_auth_header() -> str:
    """Build and return a Bearer Authorization header using the authentication token.
    In the vulnerable state, this function uses the hardcoded PASSWORD constant.
    After repair, it should use the SECUREAGENT_SERVICE_TOKEN environment variable.
    Returns:
        A Bearer Authorization header string with format "Bearer {token}".
    """
    token = os.environ.get("SECUREAGENT_SERVICE_TOKEN", "")
    return f"Bearer {token}"
