close_prices = [95, 102, 98, 110, 105, 90]

high_prices = [price for price in close_prices if price > 100]

print("All Prices:", close_prices)
print("Prices Above 100:", high_prices)