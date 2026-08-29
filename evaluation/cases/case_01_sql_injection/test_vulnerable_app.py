import sqlite3

import pytest

from .vulnerable_app import find_users_by_username


@pytest.fixture
def database_path(tmp_path):
    database_path = tmp_path / "synthetic_users.sqlite3"
    connection = sqlite3.connect(database_path)
    try:
        connection.execute(
            "CREATE TABLE users (username TEXT NOT NULL, display_name TEXT NOT NULL)"
        )
        connection.executemany(
            "INSERT INTO users (username, display_name) VALUES (?, ?)",
            [
                ("alice_synthetic", "Synthetic Alice"),
                ("bob_synthetic", "Synthetic Bob"),
            ],
        )
        connection.commit()
    finally:
        connection.close()
    return database_path


def test_ordinary_username_lookup_returns_matching_user(database_path):
    assert find_users_by_username(str(database_path), "alice_synthetic") == [
        {"username": "alice_synthetic", "display_name": "Synthetic Alice"}
    ]


def test_sql_injection_payload_returns_no_users(database_path):
    malicious_username = "' OR '1'='1"

    assert find_users_by_username(str(database_path), malicious_username) == []
