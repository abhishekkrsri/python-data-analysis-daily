# Day 02 - Lists

# Example 1: Create a list
symbols = ["EURUSD", "GBPUSD", "XAUUSD"]

print(symbols)


# Example 2: Access list elements
print("First Symbol:", symbols[0])
print("Second Symbol:", symbols[1])
print("Last Symbol:", symbols[-1])


# Example 3: Add a new item
symbols.append("USDJPY")

print("After Adding:", symbols)


# Example 4: Remove an item
symbols.remove("GBPUSD")

print("After Removing:", symbols)


# Example 5: Loop through a list
for symbol in symbols:
    print("Analyzing:", symbol)