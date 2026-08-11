prices = [100, 105, 110, 115, 120]

print("Original List:", prices)

prices.remove(105)

print("After remove():", prices)

removed_price = prices.pop(1)

print("Removed Price using pop():", removed_price)
print("After pop():", prices)

del prices[0]

print("After del:", prices)

prices.clear()

print("After clear():", prices)