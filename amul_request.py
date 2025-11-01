from time import sleep

from requests import head
from config import DEFAULT_PIN_CODE, ENTER_KEY, ENTER_YOUR_PINCODE_PLACEHOLDER, PINCODE_SEARCH_ITEM_CLASS, RETRY_LIMIT, SOLD_OUT_TEXT
from playwright.sync_api import sync_playwright


class AmulRequest:    
    def __init__(self):
        pass

    def request_product_availability(self, product_uri: str) -> bool:
        """Check the availability of a product.

        Args:
            product_uri (str): The URI of the product to check. Uri must be of the form "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"

        Returns:
            bool: True if the product is available, False otherwise.
        """
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(product_uri)
            # fill and click enter
            page.wait_for_selector(f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]')
            page.fill(f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]', DEFAULT_PIN_CODE)
            page.wait_for_selector(f".{PINCODE_SEARCH_ITEM_CLASS}")
            page.keyboard.press(ENTER_KEY)
            page.wait_for_selector('[title="Add to Cart"]')
            availability_status = page.evaluate(f"document.body.innerText.includes('{SOLD_OUT_TEXT}')")
            browser.close()
        return not availability_status

