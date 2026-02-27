import requests
import json

def get_prices():
    # CoinGecko API is free for simple requests
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,dogecoin,hyperlane-2", # 'hyperlane-2' is a guess, I need to search for it first or just try 'hyperlane'
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    
    # First, let's try to find the correct ID for Hyperlane if it exists
    # If HYPE is not listed or has a different ID, this part is crucial.
    # For now, I'll just try to get BTC, ETH, DOGE first to ensure the script works.
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    get_prices()
