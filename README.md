# OSRS Price Tracker

![OSRS Price Tracker](https://img.shields.io/badge/OSRS-Price%20Tracker-brightgreen)
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A real-time Old School RuneScape (OSRS) Grand Exchange price tracking tool that utilizes the official OSRS Wiki Prices API. This tool provides accurate, up-to-date pricing information for all tradeable items in OSRS.

## 🌟 Features

- **Real-time Price Tracking**: Get current Grand Exchange prices for any OSRS item
- **Detailed Item Information**: Access comprehensive item data including:
  - Current high/low prices
  - Last trade timestamps
  - Buy limits
  - Item examine text
  - Members/F2P status
- **Easy-to-use Python Interface**: Simple and intuitive API
- **Proper Rate Limiting**: Follows OSRS Wiki API guidelines
- **Error Handling**: Robust error handling for API requests

## 📋 Prerequisites

- Python 3.7 or higher
- `requests` library

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/valkarinc/osrs-price-tracker.git
cd osrs-price-tracker
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```python
from price_tracker import PriceTracker

# Initialize the tracker
tracker = PriceTracker()

# Get price information for a single item
whip_info = tracker.get_item_price("Abyssal whip")
print(whip_info)

# Track multiple items
items = ["Dragon bones", "Old school bond", "Twisted bow"]
for item in items:
    price_info = tracker.get_item_price(item)
    print(f"\nItem: {price_info['name']}")
    print(f"High Price: {price_info['high_price']:,} gp")
    print(f"Low Price: {price_info['low_price']:,} gp")
```

### Example Output

```
Item: Abyssal whip
Buy Limit: 70
High Price: 2,456,789 gp
Low Price: 2,445,678 gp
Last High Trade: 2024-12-23T10:30:15
Last Low Trade: 2024-12-23T10:28:45
Members Item: True
Description: A weapon from the Abyss.
```

## 🔧 Configuration

The tool uses default configuration for API requests, including:

- Base URL: https://prices.runescape.wiki/api/v1/osrs
- User Agent: Set according to OSRS Wiki requirements
- Automatic rate limiting to prevent API abuse

## 📈 Advanced Features

### Item Mapping Cache

The tool maintains a local cache of item mappings to reduce API calls:

```python
tracker = PriceTracker()
item_mapping = tracker.item_mapping  # Access the complete item database
```

### Error Handling

The tool includes robust error handling for common issues:

```python
try:
    price_info = tracker.get_item_price("Non-existent Item")
except ValueError as e:
    print(f"Error: {e}")
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR follows the project's coding standards and includes appropriate tests.

## 📝 API Reference

This project uses the OSRS Wiki Prices API. For more information, visit:

[OSRS Wiki Prices API Documentation](https://prices.runescape.wiki/)

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the OSRS Wiki team for providing the Prices API
- All contributors to this project
- The OSRS community

## 📬 Contact

Created by @valkarinc - feel free to contact me!
