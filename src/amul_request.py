from config import AMUL_SHOP_URL, DEFAULT_PIN_CODE, ENTER_KEY, ENTER_YOUR_PINCODE_PLACEHOLDER, PINCODE_SEARCH_ITEM_CLASS, SOLD_OUT_TEXT
from playwright.sync_api import sync_playwright, Page
from utils.logger import logger


class AmulRequest:
    def __init__(self):
        logger.debug("AmulRequest instance initialized")

    def _set_pincode(self, page: Page) -> None:
        """Set the pincode for product availability check.

        Args:
            page: Playwright page object
        """
        try:
            logger.info(f"Navigating to {AMUL_SHOP_URL}")
            page.goto(AMUL_SHOP_URL)

            logger.debug(
                f"Waiting for pincode input field with placeholder: {ENTER_YOUR_PINCODE_PLACEHOLDER}")
            page.wait_for_selector(
                f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]')

            logger.info(f"Setting pincode to: {DEFAULT_PIN_CODE}")
            page.fill(
                f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]', DEFAULT_PIN_CODE)

            logger.debug(
                f"Waiting for pincode search results with class: {PINCODE_SEARCH_ITEM_CLASS}")
            page.wait_for_selector(f".{PINCODE_SEARCH_ITEM_CLASS}")

            logger.debug("Pressing Enter key to confirm pincode")
            page.keyboard.press(ENTER_KEY)

            logger.info("Pincode set successfully")
        except Exception as e:
            logger.error(f"Failed to set pincode: {e}", exc_info=True)
            raise e

    def request_product_availability(self, product_urls: list[str]) -> list[bool]:
        """Check the availability of a product.

        Args:
            product_urls (list[str]): The URLs of the products to check. Each URL must be of the form "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"

        Returns:
            list[bool]: List of availability status for each product URL.
        """
        logger.info(
            f"Starting product availability check for {len(product_urls)} product(s)")
        status = []

        try:
            with sync_playwright() as p:
                logger.debug("Launching Chromium browser")
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()

                self._set_pincode(page)

                for idx, product_url in enumerate(product_urls, 1):
                    try:
                        logger.info(
                            f"Checking product {idx}/{len(product_urls)}: {product_url}")
                        page.goto(product_url)

                        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure page loads
                        logger.debug(page.content())

                        logger.debug("Waiting for 'Add to Cart' button")
                        page.wait_for_selector('[title="Add to Cart"]')

                        availability_status = not page.evaluate(
                            f"document.body.innerText.includes('{SOLD_OUT_TEXT}')")
                        status.append(availability_status)

                        logger.info(
                            f"Product {idx} availability: {'Available' if availability_status else 'Sold Out'}")
                    except Exception as e:
                        logger.error(
                            f"Error checking product at {product_url}: {e}", exc_info=True)
                        status.append(False)

                logger.debug("Closing browser")
                browser.close()
        except Exception as e:
            logger.error(
                f"Critical error in product availability check: {e}", exc_info=True)
            raise e

        logger.info(
            f"Completed availability check. Results: {sum(status)}/{len(product_urls)} product(s) available")
        return status
