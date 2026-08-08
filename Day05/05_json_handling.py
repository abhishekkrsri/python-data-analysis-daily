import json

market = {
    "symbol": "EURUSD",
    "price": 1.1050,
    "timeframe": "15M"
}

json_data = json.dumps(market, indent=4)

print(json_data)