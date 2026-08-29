from .models import Report

_REPORTS: dict[str, Report] = {
    "report-alice": Report(
        report_id="report-alice",
        owner_id="user-alice",
        content="Synthetic quarterly summary",
    ),
    "report-bob": Report(
        report_id="report-bob",
        owner_id="user-bob",
        content="Synthetic incident summary",
    ),
}


def get_report(report_id: str) -> Report:
    try:
        return _REPORTS[report_id]
    except KeyError as exc:
        raise LookupError(f"Report '{report_id}' not found in the synthetic repository.") from exc
