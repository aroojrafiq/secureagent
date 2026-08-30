"""Synthetic path-traversal evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally builds a path by combining a synthetic export directory with a
caller-supplied filename without validating traversal attempts. Do not use this code in
any production, operational, or real security-sensitive system.
"""

from pathlib import Path


EXPORT_DIRECTORY = Path("synthetic-exports")


def build_export_path(filename: str) -> Path:
    """Return the export path for a provided filename after validating traversal attempts."""
    candidate_path = Path(filename)
    if candidate_path.is_absolute() or ".." in candidate_path.parts:
        raise ValueError("Path traversal attempts are not allowed")
    return EXPORT_DIRECTORY / candidate_path
