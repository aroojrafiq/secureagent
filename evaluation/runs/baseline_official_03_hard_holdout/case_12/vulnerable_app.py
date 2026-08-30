from urllib.parse import urlsplit

from .config import ALLOWED_API_ORIGIN
from .transport import FakeTransport


def fetch_allowed_resource(url: str, transport: FakeTransport) -> str:
    parsed_url = urlsplit(url)
    allowed_url = urlsplit(ALLOWED_API_ORIGIN)

    if (
        parsed_url.scheme != allowed_url.scheme
        or parsed_url.hostname != allowed_url.hostname
        or parsed_url.port != allowed_url.port
    ):
        raise ValueError("URL is not on the allowed API origin")

    return transport.get(url)
