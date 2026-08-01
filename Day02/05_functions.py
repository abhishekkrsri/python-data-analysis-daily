# Day 02 - Functions

# Example 1: Simple function
def greet():
    print("Welcome to Python")

greet()


# Example 2: Function with parameters
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition:", result)


# Example 3: Calculate candle range
def calculate_range(high, low):
    return high - low

candle_range = calculate_range(105, 98)
print("Candle Range:", candle_range)


# Example 4: Check High Break
def check_high_break(previous_high, current_high):
    if current_high > previous_high:
        return "High Break"
    else:
        return "No High Break"

result = check_high_break(100, 105)
print("Break Result:", result)