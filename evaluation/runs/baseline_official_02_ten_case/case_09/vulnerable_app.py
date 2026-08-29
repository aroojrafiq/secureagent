"""Synthetic missing-authorization evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.
This module intentionally returns a report without verifying whether the requesting user owns
that report. Do not use this code in any production, operational, or real security-sensitive
system.
"""

from .repository import get_report


def view_report(report_id: str, requester_id: str) -> str:
    report = get_report(report_id)
    return report.content
