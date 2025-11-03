# Amul Protein Products Availability Monitor 🥛

A Python script that monitors the availability of Amul high-protein products and sends push notifications via ntfy when products become available in your area.

## 🚀 Quick Start (No Coding Required!)

Want to get notifications when Amul protein products are back in stock? Follow these simple steps:

### Step 1: Get the ntfy App
1. Install the [ntfy app](https://ntfy.sh/) on your Android/iPhone/iPad or use it in your browser
2. Choose a unique topic name for your notifications (e.g., `amul-alerts-yourname123`)
3. **Important:** Keep your topic name private! If you use a public/common topic name, others might spam your notifications. Feel free to contact if you want to use my channel instead (ritikrajdev.github.io)[https://ritikrajdev.github.io]

### Step 2: Fork This Repository
1. Click the **"Fork"** button at the top right of this page
2. This creates your own copy of the project

### Step 3: Add Your ntfy Topic
1. In your forked repository, go to **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Name it: `NFTY_SH_TOPIC`
4. Enter your unique topic name as the value (e.g., `amul-alerts-yourname123`)
5. Click **"Add secret"**
6. **Security Note:** Your topic name acts as a password. Keep it private to prevent spam notifications!

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
4. Subscribe to your topic in the ntfy app to receive notifications

**That's it!** You'll receive push notifications on your device whenever the products become available. 🎉

---

## Features

- 🔍 Monitors multiple Amul protein products simultaneously
- 📱 Sends push notifications via ntfy.sh (works on Android, iOS, and web)
- 🎯 Supports custom pincode-based availability checking
- ⚡ Easy configuration through JSON and environment variables
- 🔄 Automated headless browser checking using Playwright
- 🔒 Private notification channels to prevent spam

## Prerequisites

- Python 3.12 or higher
- Any device with [ntfy app](https://ntfy.sh/) installed or a web browser
- A unique ntfy topic name (keep it private!)

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

### 1. Choose Your ntfy Topic

1. Think of a unique topic name (e.g., `amul-alerts-yourname-randomstring`)
2. **Important Security Note:** Your topic name should be:
   - Unique and hard to guess
   - Kept private (don't share it publicly)
   - If you use a common/public topic name, anyone can send notifications to it, resulting in spam
3. Install the [ntfy app](https://ntfy.sh/) on your device or use the web interface
4. Subscribe to your chosen topic in the app

### 2. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
NFTY_SH_TOPIC=your-unique-topic-name
```

**Security Warning:** Never commit your `.env` file to version control or share your topic name publicly!

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
3. Send push notifications to your ntfy topic for available products

### Example Output

```
Amul High Protein Rose Lassi is now available!
Amul High Protein Plain Lassi is now available!
```

## Troubleshooting

### Notifications not working?
- Verify your ntfy topic is correctly set in the `.env` file
- Check that you're subscribed to the correct topic in the ntfy app
- Ensure your device has an internet connection
- Make sure your topic name doesn't contain special characters or spaces

### Products showing as unavailable?
- Verify your pincode is correctly set in `config.py`
- Check that the product URLs in `products.json` are valid
- The products might genuinely be out of stock in your area

### Playwright errors?
- Make sure you've installed the Chromium browser: `playwright install chromium`
- Check your internet connection

### Getting spam notifications?
- Your topic name might be too common or has been exposed
- Choose a new, more unique topic name with random characters
- Never share your topic name publicly or commit it to version control

## Contributing

Feel free to open issues or submit pull requests for improvements!

## License

MIT

## Author

Ritik Rajdev - [@ritikrajdev](https://github.com/ritikrajdev)
