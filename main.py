from email import message
from amul_request import AmulRequest
from config import PRODUCTS

from utils.notification import send_notification

def main():
    amul_request = AmulRequest()
    for product in PRODUCTS:
        is_available = amul_request.request_product_availability(product["url"])
        if is_available:
            send_notification(title=product["name"], body="is now available", url=product["url"])

if __name__ == "__main__":
    main()
