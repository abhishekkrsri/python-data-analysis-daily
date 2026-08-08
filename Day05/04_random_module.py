import random

symbols = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "XAUUSD"
]

random_symbol = random.choice(symbols)

print("Today's Market Symbol:", random_symbol)