import pytest

from .vulnerable_app import get_auth_header


def test_get_auth_header_uses_configured_token(monkeypatch):
    """Functional test: confirm expected Bearer header is returned when env var matches hardcoded value.

    This test should pass in both the vulnerable state and after a correct repair.
    """
    expected_token = "SYNTHETIC_TOKEN_dev_12345_DO_NOT_USE"
    monkeypatch.setenv("SECUREAGENT_SERVICE_TOKEN", expected_token)

    header = get_auth_header()

    assert header == f"Bearer {expected_token}"


def test_get_auth_header_respects_environment_token(monkeypatch):
    """Security test: confirm the function uses the environment variable, not hardcoded value.

    This test should fail in the vulnerable state because the function ignores the environment.
    After repair, it should pass because the function respects the environment variable.
    """
    runtime_token = "RUNTIME_SYNTHETIC_TOKEN_test_67890_DIFFERENT"
    monkeypatch.setenv("SECUREAGENT_SERVICE_TOKEN", runtime_token)

    header = get_auth_header()

    assert header == f"Bearer {runtime_token}", (
        "Function must use SECUREAGENT_SERVICE_TOKEN environment variable, "
        "not hardcoded value"
    )
