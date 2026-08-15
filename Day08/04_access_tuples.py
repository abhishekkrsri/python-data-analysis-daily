# Day 08 - Access Tuples

prices = (100, 105, 110, 115, 120)

print("Complete Tuple:", prices)


# Access first item
print("First Price:", prices[0])


# Access second item
print("Second Price:", prices[1])


# Access last item
print("Last Price:", prices[-1])


# Access a range of items
print("First Three Prices:", prices[:3])


# Access middle items
print("Middle Prices:", prices[1:4])


# Get the number of items
print("Number of Prices:", len(prices))


# Check if an item exists
if 110 in prices:
    print("110 exists in the tuple")
else:
    print("110 does not exist in the tuple")