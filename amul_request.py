from config import AMUL_SHOP_URL, DEFAULT_PIN_CODE, ENTER_KEY, ENTER_YOUR_PINCODE_PLACEHOLDER, PINCODE_SEARCH_ITEM_CLASS, SOLD_OUT_TEXT
from playwright.sync_api import sync_playwright


class AmulRequest:    
    def __init__(self):
        pass

    def _set_pincode(self, page) -> None:
        page.goto(AMUL_SHOP_URL)
        page.wait_for_selector(f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]')
        page.fill(f'input[placeholder="{ENTER_YOUR_PINCODE_PLACEHOLDER}"]', DEFAULT_PIN_CODE)
        page.wait_for_selector(f".{PINCODE_SEARCH_ITEM_CLASS}")
        page.keyboard.press(ENTER_KEY)


    def request_product_availability(self, product_urls: list[str]) -> list[bool]:
        """Check the availability of a product.
    
        Args:
            product_urls (list[str]): The URLs of the products to check. Each URL must be of the form "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"

        Returns:
            bool: True if any product is available, False otherwise.
        """
        status = []
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            self._set_pincode(page)
            for product_url in product_urls:
                try:
                    page.goto(product_url)
                    page.wait_for_selector('[title="Add to Cart"]')
                    availability_status = not page.evaluate(f"document.body.innerText.includes('{SOLD_OUT_TEXT}')")
                    status.append(availability_status)
                except Exception as e:
                    print(f"Error checking product at {product_url}: {e}")
                    status.append(False)
            browser.close()
        return status
