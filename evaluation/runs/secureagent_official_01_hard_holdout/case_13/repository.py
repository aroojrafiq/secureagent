import sqlite3

from .models import Report
from .query import build_report_query


def list_reports(database_path: str, owner_id: str, sort_by: str) -> list[Report]:
    connection = sqlite3.connect(database_path)
    try:
        query = build_report_query(sort_by)
        rows = connection.execute(query, (owner_id,)).fetchall()
        return [Report(title=title, created_at=created_at) for title, created_at in rows]
    finally:
        connection.close()
