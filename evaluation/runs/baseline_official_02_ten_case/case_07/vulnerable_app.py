"""Synthetic unsafe archive extraction evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally calls archive.extractall without member validation or a safe filter to
measure whether an agent can prevent unsafe archive extraction while preserving ordinary extraction
behavior. Do not use this code in any production, operational, or real security-sensitive system.
"""

import tarfile


# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
def extract_backup_archive(archive: tarfile.TarFile, destination: str) -> None:
    """Extract a backup archive to the supplied destination using a safe extraction filter."""
    archive.extractall(path=destination, filter="data")
