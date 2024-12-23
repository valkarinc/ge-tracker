import requests
from typing import Dict, Optional, List
import time
from datetime import datetime

class OSRSAPIClient:
    """
    Client for interacting with the OSRS Wiki Prices API
    """
    def __init__(self):
        self.base_url = "https://prices.runescape.wiki/api/v1/osrs"
        self.headers = {
            'User-Agent': 'OSRS Price Tracker - github.com/valkarinc/osrs-price-tracker'
        }

    def get_latest_prices(self, item_id: Optional[int] = None) -> Dict:
        """
        Get latest prices for all items or a specific item
        
        Args:
            item_id (Optional[int]): Specific item ID to look up
            
        Returns:
            Dict: Latest price data
        """
        endpoint = f"{self.base_url}/latest"
        params = {"id": item_id} if item_id else None
        
        response = requests.get(endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_item_mapping(self) -> List[Dict]:
        """
        Get mapping of all items with their IDs and additional information
        
        Returns:
            List[Dict]: List of items with their details
        """
        endpoint = f"{self.base_url}/mapping"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

class PriceTracker:
    """
    Tracks and analyzes OSRS item prices
    """
    def __init__(self):
        self.api_client = OSRSAPIClient()
        self.item_mapping = None
        self._load_item_mapping()

    def _load_item_mapping(self):
        """Load and cache item mapping data"""
        self.item_mapping = {item['id']: item for item in self.api_client.get_item_mapping()}

    def get_item_price(self, item_name: str) -> Dict:
        """
        Get current price data for an item by its name
        
        Args:
            item_name (str): Name of the item to look up
            
        Returns:
            Dict: Price data for the item
        """
        # Find item ID from mapping
        item_id = None
        for id, item_data in self.item_mapping.items():
            if item_data['name'].lower() == item_name.lower():
                item_id = id
                break

        if not item_id:
            raise ValueError(f"Item '{item_name}' not found")

        # Get price data
        price_data = self.api_client.get_latest_prices(item_id)
        
        # Format the response
        if str(item_id) in price_data['data']:
            item_prices = price_data['data'][str(item_id)]
            return {
                'name': item_name,
                'id': item_id,
                'high_price': item_prices['high'],
                'low_price': item_prices['low'],
                'high_time': datetime.fromtimestamp(item_prices['highTime']).isoformat() if item_prices['highTime'] else None,
                'low_time': datetime.fromtimestamp(item_prices['lowTime']).isoformat() if item_prices['lowTime'] else None,
                'examine': self.item_mapping[item_id]['examine'],
                'members': self.item_mapping[item_id]['members'],
                'buy_limit': self.item_mapping[item_id].get('limit')
            }
        return None

# Example usage
if __name__ == "__main__":
    tracker = PriceTracker()
    
    # Example items to track
    items_to_track = ["Abyssal whip", "Dragon bones", "Old school bond"]
    
    print("Current OSRS Grand Exchange Prices:")
    print("-" * 50)
    
    for item_name in items_to_track:
        try:
            price_info = tracker.get_item_price(item_name)
            if price_info:
                print(f"\nItem: {price_info['name']}")
                print(f"Buy Limit: {price_info['buy_limit']}")
                print(f"High Price: {price_info['high_price']:,} gp")
                print(f"Low Price: {price_info['low_price']:,} gp")
                print(f"Last High Trade: {price_info['high_time']}")
                print(f"Last Low Trade: {price_info['low_time']}")
                print(f"Members Item: {price_info['members']}")
                print(f"Description: {price_info['examine']}")
        except Exception as e:
            print(f"Error fetching price for {item_name}: {str(e)}")
