from requests import post as http_post

from config import AMUL_ICON_URL, BARK_API_TOKENS
from .notifications import BaseNotification

class IOSNotification(BaseNotification):
    def __init__(self):
        if not BARK_API_TOKENS:
            raise ValueError("BARK_API_TOKENS is not set in the environment variables.")
        self.bark_api_tokens = BARK_API_TOKENS.split(",")

    def send(self, title: str, body: str="", url: str = "", icon_url: str=AMUL_ICON_URL):
        for token in self.bark_api_tokens:
            bark_url = f"https://api.day.app/{token}/{title}"
            if body:
                bark_url += f"/{body}"
            params = {}
            if icon_url:
                params['icon'] = icon_url
            if url:
                params['url'] = url
            http_post(bark_url, params=params)
