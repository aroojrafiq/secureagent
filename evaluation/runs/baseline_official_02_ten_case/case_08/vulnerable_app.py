"""Synthetic path-traversal evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally builds a path by combining a synthetic export directory with a
caller-supplied filename without validating traversal attempts. Do not use this code in
any production, operational, or real security-sensitive system.
"""

from pathlib import Path


EXPORT_DIRECTORY = Path("synthetic-exports")


def build_export_path(filename: str) -> Path:
    """Return the export path for a provided filename without validation."""
    return EXPORT_DIRECTORY / filename
