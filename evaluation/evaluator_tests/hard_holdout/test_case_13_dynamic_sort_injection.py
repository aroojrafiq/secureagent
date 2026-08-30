import importlib
import os
import sqlite3


package_name = os.environ.get("SECUREAGENT_HOLDOUT_PACKAGE")
if not package_name:
    raise RuntimeError("SECUREAGENT_HOLDOUT_PACKAGE environment variable is not set")

vulnerable_app_module = importlib.import_module(
    f"{package_name}.case_13.vulnerable_app"
)
list_report_titles = vulnerable_app_module.list_report_titles


def _create_database(tmp_path):
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
    return database_path


def _count_rows(database_path):
    connection = sqlite3.connect(database_path)
    try:
        return connection.execute("SELECT COUNT(*) FROM reports").fetchone()[0]
    finally:
        connection.close()


def test_created_at_sort_regression(tmp_path):
    database_path = _create_database(tmp_path)

    assert list_report_titles(
        str(database_path), "user-alice", "created_at"
    ) == ["Middle report", "Alpha report", "Zulu report"]


def test_injected_expression_is_rejected_and_data_remains(tmp_path):
    database_path = _create_database(tmp_path)
    value_error_raised = False

    try:
        list_report_titles(
            str(database_path), "user-alice", "CASE WHEN 1=1 THEN title END"
        )
    except ValueError:
        value_error_raised = True

    assert _count_rows(database_path) == 4
    assert value_error_raised


def test_unsupported_modifier_is_rejected_and_data_remains(tmp_path):
    database_path = _create_database(tmp_path)
    value_error_raised = False

    try:
        list_report_titles(str(database_path), "user-alice", "title COLLATE NOCASE")
    except ValueError:
        value_error_raised = True

    assert _count_rows(database_path) == 4
    assert value_error_raised
