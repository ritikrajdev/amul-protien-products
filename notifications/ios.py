from requests import post as http_post

from config import BARK_API_TOKEN
from .notifications import BaseNotification

class IOSNotification(BaseNotification):
    def __init__(self):
        if not BARK_API_TOKEN:
            raise ValueError("BARK_API_TOKEN is not set in the environment variables.")
        self.bark_api_token = BARK_API_TOKEN

    def send(self, title: str, body: str="", uri: str = ""):
        bark_url = f"https://api.day.app/{self.bark_api_token}/{title}"
        if body:
            bark_url += f"/{body}"
        if uri:
            bark_url += f"?url={uri}"
        response = http_post(bark_url)
        if response.status_code != 200:
            raise Exception(f"Failed to send iOS notification: {response.text}")
