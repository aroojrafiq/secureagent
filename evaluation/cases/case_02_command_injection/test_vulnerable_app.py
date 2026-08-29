import subprocess
from types import SimpleNamespace

import pytest

from .vulnerable_app import lookup_hostname


def test_ordinary_hostname_lookup_returns_mocked_stdout(monkeypatch):
    expected_stdout = "Server: example.test\nAddress: 192.0.2.10\n"

    def fake_run(command, **kwargs):
        return SimpleNamespace(stdout=expected_stdout)

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert lookup_hostname("example.test") == expected_stdout


def test_hostname_with_shell_operator_uses_safe_subprocess_call(monkeypatch):
    malicious_hostname = "example.test; echo OWNED"
    observed = {}

    def fake_run(command, **kwargs):
        observed["command"] = command
        observed["kwargs"] = kwargs
        return SimpleNamespace(stdout="safe output")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert lookup_hostname(malicious_hostname) == "safe output"
    assert observed["kwargs"].get("shell") is False
    assert isinstance(observed["command"], list)
    assert observed["command"] == ["nslookup", malicious_hostname]
