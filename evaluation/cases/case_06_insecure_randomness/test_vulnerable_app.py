import string

from .vulnerable_app import generate_reset_code


def test_generate_reset_code_functional_properties():
    """Functional test: the reset code has the expected format and length."""
    code = generate_reset_code(length=12)
    allowed_characters = set(string.ascii_uppercase + string.digits)

    assert isinstance(code, str)
    assert len(code) == 12
    assert set(code).issubset(allowed_characters)


def test_generate_reset_code_uses_secure_random_source(monkeypatch):
    """Security test: a secure repair must use secrets.choice instead of random.choice."""
    monkeypatch.setattr("random.choice", lambda _alphabet: "R")
    monkeypatch.setattr("secrets.choice", lambda _alphabet: "S")

    code = generate_reset_code(length=8)

    assert code == "SSSSSSSS"
