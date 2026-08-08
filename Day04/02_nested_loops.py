symbols = ["EURUSD", "GBPUSD", "XAUUSD"]

timeframes = ["5M", "15M", "1H"]

for symbol in symbols:
    for timeframe in timeframes:
        print(symbol, "-", timeframe)