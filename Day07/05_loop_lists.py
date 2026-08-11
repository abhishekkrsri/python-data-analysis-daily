prices = [100, 105, 110, 115]

print("Using a for loop:")

for price in prices:
    print(price)


print("\nUsing indexes:")

for i in range(len(prices)):
    print("Index:", i, "Price:", prices[i])


print("\nUsing enumerate():")

for index, price in enumerate(prices):
    print("Index:", index, "Price:", price)