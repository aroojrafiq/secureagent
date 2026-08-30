import sqlite3

from .vulnerable_app import list_report_titles


def test_list_report_titles_sorts_alice_reports_by_title(tmp_path):
    database_path = tmp_path / "reports.sqlite3"
    connection = sqlite3.connect(database_path)
    try:
        connection.execute(
            """
            CREATE TABLE reports (
                title TEXT NOT NULL,
                created_at TEXT NOT NULL,
                owner_id TEXT NOT NULL
            )
            """
        )
        connection.executemany(
            "INSERT INTO reports (title, created_at, owner_id) VALUES (?, ?, ?)",
            [
                ("Zulu report", "2026-03-01", "user-alice"),
                ("Alpha report", "2026-02-01", "user-alice"),
                ("Middle report", "2026-01-01", "user-alice"),
                ("Synthetic Bob report", "2026-04-01", "user-bob"),
            ],
        )
        connection.commit()
    finally:
        connection.close()

    assert list_report_titles(str(database_path), "user-alice", "title") == [
        "Alpha report",
        "Middle report",
        "Zulu report",
    ]
