try:
    price = float(input("Enter market price: "))
    print("Market Price:", price)

except ValueError:
    print("Invalid price. Please enter a number.")