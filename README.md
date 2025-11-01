# Amul Protein Products Availability Monitor 🥛

A Python script that monitors the availability of Amul high-protein products and sends iOS push notifications via Bark when products become available in your area.

## 🚀 Quick Start (No Coding Required!)

Want to get notifications when Amul protein products are back in stock? Follow these simple steps:

### Step 1: Get the Bark App
1. Install the [Bark app](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) on your iPhone/iPad
2. Open the app and copy your API key (it's shown on the main screen)

### Step 2: Fork This Repository
1. Click the **"Fork"** button at the top right of this page
2. This creates your own copy of the project

### Step 3: Add Your Bark API Key
1. In your forked repository, go to **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Name it: `BARK_API_TOKENS`
4. Paste your Bark API key as the value
5. Click **"Add secret"**

### Step 4: (Optional) Add More Products to Monitor
1. In your repository, click on the `products.json` file
2. Click the pencil icon (✏️) to edit the file (or press `.` to open in github.dev)
3. Add your products in this format:
   ```json
   {
       "name": "Product Name Here",
       "url": "https://shop.amul.com/en/product/product-url-here"
   }
   ```
4. Commit your changes

### Step 5: (Optional) Change Your Pincode
1. Click on the `config.py` file
2. Click the pencil icon (✏️) to edit
3. Change `DEFAULT_PIN_CODE = "560037"` to your pincode
4. Commit your changes

### Step 6: Enable GitHub Actions
1. Go to the **Actions** tab in your repository
2. Click **"I understand my workflows, go ahead and enable them"**
3. The script will now run automatically and check product availability!

**That's it!** You'll receive push notifications on your iPhone/iPad whenever the products become available. 🎉

---

## Features

- 🔍 Monitors multiple Amul protein products simultaneously
- 📱 Sends iOS push notifications via Bark API
- 🎯 Supports custom pincode-based availability checking
- ⚡ Easy configuration through JSON and environment variables
- 🔄 Automated headless browser checking using Playwright

## Prerequisites

- Python 3.12 or higher
- iOS device with [Bark app](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) installed
- Bark API token(s)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ritikrajdev/amul-protien-products.git
   cd amul-protien-products
   ```

2. **Install dependencies**
   
   Using pip:
   ```bash
   pip install requirements.txt
   ```
   
   Or using poetry:
   ```bash
   poetry install
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

## Configuration

### 1. Get Your Bark API Token

1. Download and install the [Bark app](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) on your iOS device
2. Open the Bark app
3. Copy your API token (it looks like a long string of characters)
4. You can add multiple devices by separating tokens with commas

### 2. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
BARK_API_TOKENS=your_bark_token_here
```

For multiple devices, separate tokens with commas:
```bash
BARK_API_TOKENS=token1,token2,token3
```

### 3. Configure Products to Monitor

Edit `products.json` to add or modify products you want to monitor:

```json
[
    {
        "name": "Amul High Protein Rose Lassi",
        "url": "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
    },
    {
        "name": "Amul High Protein Plain Lassi",
        "url": "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30"
    }
]
```

### 4. Set Your Pincode (Optional)

By default, the script checks availability for pincode `560037`. To change this, edit `config.py`:

```python
DEFAULT_PIN_CODE = "560037"  # Change to your pincode
```

## Usage

Run the script to check product availability:

```bash
python main.py
```

The script will:
1. Check each product's availability on the Amul website
2. Print availability status to the console
3. Send iOS push notifications for available products

### Example Output

```
Amul High Protein Rose Lassi is now available!
Amul High Protein Plain Lassi is now available!
```

## Troubleshooting

### Notifications not working?
- Verify your Bark API token is correct in the `.env` file
- Check that the Bark app is installed and running on your iOS device
- Ensure your device has an internet connection

### Products showing as unavailable?
- Verify your pincode is correctly set in `config.py`
- Check that the product URLs in `products.json` are valid
- The products might genuinely be out of stock in your area

### Playwright errors?
- Make sure you've installed the Chromium browser: `playwright install chromium`
- Check your internet connection

## Contributing

Feel free to open issues or submit pull requests for improvements!

## License

MIT

## Author

Ritik Rajdev - [@ritikrajdev](https://github.com/ritikrajdev)
