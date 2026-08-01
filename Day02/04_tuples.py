# Day 02 - Tuples

# Example 1: Create a tuple
timeframes = ("M5", "M15", "H1", "H4")

print("Timeframes:", timeframes)


# Example 2: Access tuple elements
print("First Timeframe:", timeframes[0])
print("Second Timeframe:", timeframes[1])
print("Last Timeframe:", timeframes[-1])


# Example 3: Loop through tuple
for timeframe in timeframes:
    print("Timeframe:", timeframe)


# Example 4: Tuple length
print("Total Timeframes:", len(timeframes))