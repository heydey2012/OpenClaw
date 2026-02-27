from duckduckgo_search import DDGS
import json

try:
    with DDGS() as ddgs:
        results = {}
        # Bitcoin
        results["btc"] = [r for r in ddgs.text("Bitcoin price USD CoinMarketCap", region="us-en", timelimit="d", max_results=2)]
        # Ethereum
        results["eth"] = [r for r in ddgs.text("Ethereum price USD CoinMarketCap", region="us-en", timelimit="d", max_results=2)]
        # Dogecoin
        results["doge"] = [r for r in ddgs.text("Dogecoin price USD CoinMarketCap", region="us-en", timelimit="d", max_results=2)]
        # Hyperlane (HYPE)
        results["hype"] = [r for r in ddgs.text("Hyperlane HYPE token price USD CoinGecko", region="us-en", timelimit="w", max_results=2)]
        
        print(json.dumps(results, ensure_ascii=False, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))
