# Day 08 - Copy Lists

prices = [100, 105, 110, 115]

print("Original List:", prices)


# Copy using copy()
copied_prices = prices.copy()

print("Copied List:", copied_prices)


# Change the copied list
copied_prices.append(120)

print("Original List After Copy Changed:", prices)
print("Copied List After Change:", copied_prices)


# Another way to copy using list()
another_copy = list(prices)

print("Another Copy:", another_copy)