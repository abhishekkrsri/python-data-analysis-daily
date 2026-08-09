prices = [100, 105, 110, 115, 120]


def add_ten(price):
    return price + 10


result = map(add_ten, prices)

new_prices = list(result)

print("Original Prices:", prices)
print("New Prices:", new_prices)