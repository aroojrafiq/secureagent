import importlib
import os

import pytest


package_name = os.environ.get("SECUREAGENT_HOLDOUT_PACKAGE")
if not package_name:
    raise RuntimeError("SECUREAGENT_HOLDOUT_PACKAGE environment variable is not set")

transport_module = importlib.import_module(f"{package_name}.case_12.transport")
vulnerable_app_module = importlib.import_module(f"{package_name}.case_12.vulnerable_app")

FakeTransport = transport_module.FakeTransport
fetch_allowed_resource = vulnerable_app_module.fetch_allowed_resource


def test_allowed_origin_regression_returns_response():
    transport = FakeTransport(response="Synthetic paged response")
    url = "https://api.synthetic.example/v2/items?page=2"

    result = fetch_allowed_resource(url, transport)

    assert result == "Synthetic paged response"
    assert transport.requested_urls == [url]


def test_deceptive_host_is_rejected():
    transport = FakeTransport()
    url = "https://api.synthetic.example.attacker.test/data"

    with pytest.raises(ValueError):
        fetch_allowed_resource(url, transport)

    assert transport.requested_urls == []


def test_user_information_confusion_is_rejected():
    transport = FakeTransport()
    url = "https://api.synthetic.example@attacker.test/data"

    with pytest.raises(ValueError):
        fetch_allowed_resource(url, transport)

    assert transport.requested_urls == []
