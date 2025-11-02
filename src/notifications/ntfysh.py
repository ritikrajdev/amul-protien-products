from urllib import response
from requests import post as http_post
from config import AMUL_ICON_URL, NFTY_SH_TOPIC
from utils.logger import logger
from .notifications import BaseNotification

class NftyShNotification(BaseNotification):
    def __init__(self) -> None:
        """Initialize NftySh notification handler.

        Raises:
            ValueError: If Nfty.sh topic is not configured.
        """
        logger.debug("Initializing NftySh notification handler")
        if not NFTY_SH_TOPIC:
            logger.error("Nfty.sh topic is not configured")
            raise ValueError("Nfty.sh topic is not configured.")
        self.topic = NFTY_SH_TOPIC
    
    def send(self, title: str, body: str = "", url: str = "", icon_url: str = AMUL_ICON_URL) -> None:
        """Send notification via Nfty.sh API.

        Args:
            title: Notification title
            body: Notification body text (optional)
            url: URL to open when notification is tapped (optional)
            icon_url: URL of the notification icon (defaults to AMUL_ICON_URL)
        """
        ntfy_url = f"https://ntfy.sh/{self.topic}"
        headers = {
            "Title": title,
            "Message": body,
            "Icon": icon_url,
            "Click": url,
        }
        logger.debug(f"Sending Nfty.sh notification to topic: {self.topic}")
        response = http_post(ntfy_url, headers=headers)
        if response.status_code == 200:
            logger.info("Nfty.sh notification sent successfully")
        else:
            logger.error(f"Failed to send Nfty.sh notification: {response.text}")
