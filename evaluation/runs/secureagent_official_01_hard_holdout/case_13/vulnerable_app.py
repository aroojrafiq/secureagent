from .repository import list_reports


def list_report_titles(database_path: str, owner_id: str, sort_by: str) -> list[str]:
    reports = list_reports(database_path, owner_id, sort_by)
    return [report.title for report in reports]
