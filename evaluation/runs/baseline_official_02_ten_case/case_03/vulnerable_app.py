"""Synthetic hardcoded secret evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
This module intentionally contains a hardcoded authentication token to measure
whether an agent can identify and remove hardcoded secrets while preserving behavior.
Do not use this code as a template for any production application.
"""

# INTENTIONALLY VULNERABLE: Hardcoded synthetic authentication token.
# This is an obviously fake token created solely for evaluation purposes.
# Bandit will report B105 on this line due to the variable name "password".
PASSWORD = "SYNTHETIC_TOKEN_dev_12345_DO_NOT_USE"


def get_auth_header() -> str:
    """Build and return a Bearer Authorization header using the authentication token.
    In the vulnerable state, this function uses the hardcoded PASSWORD constant.
    After repair, it should use the SECUREAGENT_SERVICE_TOKEN environment variable.
    Returns:
        A Bearer Authorization header string with format "Bearer {token}".
    """
    token = PASSWORD
    return f"Bearer {token}"
