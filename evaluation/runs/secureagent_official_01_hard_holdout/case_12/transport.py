class FakeTransport:
    def __init__(self, response: str = "Synthetic API response"):
        self.response = response
        self.requested_urls = []

    def get(self, url: str) -> str:
        self.requested_urls.append(url)
        return self.response
