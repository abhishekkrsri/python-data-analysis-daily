with open("market_data.txt", "w") as file:
    file.write("Symbol: EURUSD\n")
    file.write("Timeframe: 15 Minutes\n")
    file.write("High: 1.1050\n")
    file.write("Low: 1.0980\n")

print("Market data saved successfully.")

with open("market_data.txt", "r") as file:
    data = file.read()

print("\nSaved Data:")
print(data)