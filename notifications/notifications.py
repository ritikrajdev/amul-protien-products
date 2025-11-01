class BaseNotification:
    def send(self, title: str, body: str, uri: str) -> None:
        """Base function to send the notification

        Args:
            uri (str): uri that should be included in the notification
            title (str): title of the notification
            body (str): body of the notification
        """
