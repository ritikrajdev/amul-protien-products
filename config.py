from os import getenv
from dotenv import load_dotenv
load_dotenv()

DEFAULT_PIN_CODE = "560037"
RETRY_LIMIT = 3
PRODUCTS = [
    # {
    #     "name": "Amul High Protein Rose Lassi",
    #     "url": "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
    # },
    {
        "name": "Amul High Protein Blueberry Shake",
        "url": "https://shop.amul.com/en/product/amul-high-protein-blueberry-shake-200-ml-or-pack-of-8"
    }
]
BARK_API_TOKEN = getenv("BARK_API_TOKEN", None)



# Programmatic constants
ENTER_YOUR_PINCODE_PLACEHOLDER = "Enter Your Pincode"
PINCODE_SEARCH_ITEM_CLASS = "searchitem-name"
ENTER_KEY = "Enter"
SOLD_OUT_TEXT = "Sold Out"
