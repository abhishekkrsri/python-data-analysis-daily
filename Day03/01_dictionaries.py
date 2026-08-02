candle = {
    "symbol": "EURUSD",
    "open": 1.1000,
    "high": 1.1050,
    "low": 1.0980,
    "close": 1.1030
}

print("Symbol:", candle["symbol"])
print("Open:", candle["open"])
print("High:", candle["high"])
print("Low:", candle["low"])
print("Close:", candle["close"])

candle_range = candle["high"] - candle["low"]

print("Candle Range:", candle_range)