from email import message
from amul_request import AmulRequest
from config import PRODUCTS

from utils.notification import send_notification

def main():
    amul_request = AmulRequest()
    product_urls = []
    for product in PRODUCTS:
        product_urls.append(product["url"])
    status = amul_request.request_product_availability(product_urls)
    for product, is_available in zip(PRODUCTS, status):
        if is_available:
            print(f"{product['name']} is now available!")
            send_notification(product["name"], "is now available!", product["url"])

if __name__ == "__main__":
    main()
