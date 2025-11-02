from email import message
from venv import logger
from amul_request import AmulRequest
from config import PRODUCTS
from utils.notification import send_notification
from utils.logger import logger


def main():
    """Main function to check product availability and send notifications."""
    logger.info("Starting Amul product availability checker")

    try:
        logger.debug(f"Initializing AmulRequest instance")
        amul_request = AmulRequest()

        product_urls = [product["url"] for product in PRODUCTS]
        logger.info(
            f"Checking availability for {len(product_urls)} product(s)")

        status = amul_request.request_product_availability(product_urls)

        available_count = 0
        for product, is_available in zip(PRODUCTS, status):
            if is_available:
                available_count += 1
                logger.info(f"Product available: {product['name']}")
                send_notification(
                    product["name"], "is now available!", product["url"])
            else:
                logger.debug(f"Product unavailable: {product['name']}")

        logger.success(
            f"Availability check complete. {available_count}/{len(PRODUCTS)} product(s) available")
    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
