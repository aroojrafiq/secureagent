"""Synthetic command-injection evaluation fixture.

INTENTIONALLY VULNERABLE: this is a synthetic evaluation fixture for security testing
and must never be used in production code.
"""

import subprocess


def lookup_hostname(hostname: str) -> str:
    """Perform a synthetic DNS lookup for the supplied hostname."""
    command = ["nslookup", hostname]
    completed = subprocess.run(
        command,
        shell=False,
        capture_output=True,
        text=True,
        check=False,
    )
    return completed.stdout
