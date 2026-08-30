from .config import ALLOWED_API_ORIGIN
from .transport import FakeTransport

# THIS IS AN INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE AND MUST NEVER BE USED IN PRODUCTION.
def fetch_allowed_resource(url: str, transport: FakeTransport) -> str:
    if not url.startswith(ALLOWED_API_ORIGIN):
        raise ValueError("URL is not on the allowed API origin")
    return transport.get(url)
