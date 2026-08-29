import json
import pickle


from .vulnerable_app import get_profile_name


def test_get_profile_name_with_synthetic_json_payload(monkeypatch):
    payload = b'{"name":"synthetic-user"}'

    monkeypatch.setattr(pickle, "loads", lambda _payload: {"name": "synthetic-user"})

    assert get_profile_name(payload) == "synthetic-user"


def test_get_profile_name_uses_json_not_pickle(monkeypatch):
    payload = b'{"name":"synthetic-user"}'
    pickle_calls = []
    json_calls = []

    def fake_pickle_loads(_payload):
        pickle_calls.append(_payload)
        return {"name": "pickle-path"}

    def fake_json_loads(_payload):
        json_calls.append(_payload)
        return {"name": "json-path"}

    monkeypatch.setattr(pickle, "loads", fake_pickle_loads)
    monkeypatch.setattr(json, "loads", fake_json_loads)

    assert get_profile_name(payload) == "json-path"
    assert json_calls
    assert not pickle_calls
