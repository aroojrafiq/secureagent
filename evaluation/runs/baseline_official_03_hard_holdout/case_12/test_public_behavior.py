from .transport import FakeTransport
from .vulnerable_app import fetch_allowed_resource


def test_fetch_allowed_resource_accepts_allowed_origin():
    transport = FakeTransport(response="Synthetic allowed response")
    url = "https://api.synthetic.example/v1/report?format=summary"

    result = fetch_allowed_resource(url, transport)

    assert result == "Synthetic allowed response"
    assert transport.requested_urls == [url]
