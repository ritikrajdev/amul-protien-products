from requests import post as http_post

from config import AMUL_ICON_URL, BARK_API_TOKENS
from .notifications import BaseNotification
from utils.logger import logger


class IOSNotification(BaseNotification):
    """iOS notification handler using Bark API."""

    def __init__(self):
        """Initialize IOSNotification with Bark API tokens.

        Raises:
            ValueError: If BARK_API_TOKENS is not set in environment variables.
        """
        logger.debug("Initializing IOSNotification")
        if not BARK_API_TOKENS:
            logger.error("BARK_API_TOKENS is not set in environment variables")
            raise EnvironmentError(
                "BARK_API_TOKENS is not set in the environment variables.")

        self.bark_api_tokens = BARK_API_TOKENS.split(",")
        logger.info(
            f"IOSNotification initialized with {len(self.bark_api_tokens)} token(s)")

    def send(self, title: str, body: str = "", url: str = "", icon_url: str = AMUL_ICON_URL) -> None:
        """Send iOS notification via Bark API.

        Args:
            title: Notification title
            body: Notification body text (optional)
            url: URL to open when notification is tapped (optional)
            icon_url: URL of the notification icon (defaults to AMUL_ICON_URL)
        """
        logger.info(
            f"Sending iOS notification: '{title}' to {len(self.bark_api_tokens)} device(s)")

        for idx, token in enumerate(self.bark_api_tokens, start=1):
            try:
                bark_url = f"https://api.day.app/{token}/{title}"
                if body:
                    bark_url += f"/{body}"

                params = {}
                if icon_url:
                    params['icon'] = icon_url
                if url:
                    params['url'] = url

                logger.debug(f"Sending notification to device {idx}")
                response = http_post(bark_url, params=params)
                response.raise_for_status()

                logger.success(
                    f"Successfully sent notification to device {idx}")
            except Exception as e:
                logger.error(
                    f"Failed to send notification to device {idx}: {e}", exc_info=True)
