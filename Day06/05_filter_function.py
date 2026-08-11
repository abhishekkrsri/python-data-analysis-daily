prices = [95, 102, 98, 110, 105, 90, 120]


def greater_than_100(price):
    return price > 100


result = filter(greater_than_100, prices)

high_prices = list(result)

print("All Prices:", prices)
print("Prices Above 100:", high_prices)