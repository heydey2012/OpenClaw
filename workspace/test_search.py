from duckduckgo_search import DDGS
import json

try:
    results = DDGS().text("current bitcoin price usd", max_results=3)
    print(json.dumps(results, indent=2))
except Exception as e:
    print(f"Error: {e}")
