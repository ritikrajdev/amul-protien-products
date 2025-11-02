from os import getenv
from dotenv import load_dotenv
from json import load
load_dotenv()

DEFAULT_PIN_CODE = "560037"
RETRY_LIMIT = 3
with open("products.json", "r") as f:
    PRODUCTS = load(f)
BARK_API_TOKENS = getenv("BARK_API_TOKENS", None)
AMUL_SHOP_URL = "https://shop.amul.com/en/"
AMUL_ICON_URL = "https://shop.amul.com/s/62fa94df8c13af2e242eba16/683693f8d8088fe70feaba1b/logo-36x36-c.png"


# Programmatic constants
ENTER_YOUR_PINCODE_PLACEHOLDER = "Enter Your Pincode"
PINCODE_SEARCH_ITEM_CLASS = "searchitem-name"
ENTER_KEY = "Enter"
SOLD_OUT_TEXT = "Sold Out"
