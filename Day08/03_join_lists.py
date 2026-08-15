# Day 08 - Join Lists

forex_symbols = ["EURUSD", "GBPUSD", "USDJPY"]

metal_symbols = ["XAUUSD", "XAGUSD"]


# Join using +
all_symbols = forex_symbols + metal_symbols

print("Using +:", all_symbols)


# Join using extend()
forex_copy = forex_symbols.copy()

forex_copy.extend(metal_symbols)

print("Using extend():", forex_copy)