from urllib.parse import urlsplit

from .config import ALLOWED_API_ORIGIN
from .transport import FakeTransport


def fetch_allowed_resource(url: str, transport: FakeTransport) -> str:
    requested = urlsplit(url)
    allowed = urlsplit(ALLOWED_API_ORIGIN)

    if requested.username is not None or requested.password is not None:
        raise ValueError("URL is not on the allowed API origin")
    if requested.scheme != allowed.scheme:
        raise ValueError("URL is not on the allowed API origin")
    if requested.hostname != allowed.hostname:
        raise ValueError("URL is not on the allowed API origin")

    request_port = requested.port
    allowed_port = allowed.port
    if request_port is None:
        request_port = 443 if requested.scheme == "https" else 80 if requested.scheme == "http" else None
    if allowed_port is None:
        allowed_port = 443 if allowed.scheme == "https" else 80 if allowed.scheme == "http" else None
    if request_port != allowed_port:
        raise ValueError("URL is not on the allowed API origin")

    return transport.get(url)
