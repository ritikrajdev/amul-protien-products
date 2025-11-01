from notifications import IOSNotification

def send_notification(title: str, body: str="", url: str=""):
    """Sends notification on any supported platform.

    Args:
        title (str): title of the notification.
        body (str, optional): body of the notification. Defaults to "".
        url (str, optional): URL to include in the notification. Defaults to "".
    """
    ios_handler = IOSNotification()
    ios_handler.send(title=title, body=body, url=url)
    

