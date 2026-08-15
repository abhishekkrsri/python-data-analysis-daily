# Day 08 - Update Tuples

prices = (100, 105, 110, 115)

print("Original Tuple:", prices)


# Convert tuple into a list
price_list = list(prices)

print("Converted to List:", price_list)


# Change an item
price_list[1] = 200

print("List After Change:", price_list)


# Add a new item
price_list.append(120)

print("List After Adding:", price_list)


# Convert the list back into a tuple
prices = tuple(price_list)

print("Updated Tuple:", prices)