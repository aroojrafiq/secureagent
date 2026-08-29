"""Synthetic SQL-injection evaluation fixture."""

import sqlite3


# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
def find_users_by_username(database_path: str, username: str) -> list[dict[str, str]]:
    """Return users matching username from the supplied SQLite database."""
    connection = sqlite3.connect(database_path)
    try:
        query = f"SELECT username, display_name FROM users WHERE username = '{username}'"
        rows = connection.execute(query).fetchall()
        return [
            {"username": row[0], "display_name": row[1]}
            for row in rows
        ]
    finally:
        connection.close()
