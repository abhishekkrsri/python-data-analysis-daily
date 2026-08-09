def calculate_total(*args):
    total = 0

    for price in args:
        total = total + price

    return total


result = calculate_total(100, 200, 300, 400)

print("Total:", result)