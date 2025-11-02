class BaseNotification:
    def send(self, title: str, body: str, url: str, icon_url: str) -> None:
        """Base function to send the notification

        Args:
            url (str): url that should be included in the notification
            title (str): title of the notification
            body (str): body of the notification
        """
