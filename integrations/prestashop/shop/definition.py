from typing import Optional


class PrestaShopDefinition:
    def __init__(self, name: str, url: Optional[str] = None, auth: Optional[str] = None):
        self.name = name
        self.url = url
        self.auth = auth
