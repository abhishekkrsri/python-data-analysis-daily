class Market:

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def display(self):
        print("Market Symbol:", self.symbol)
        print("Market Price:", self.price)


market1 = Market("EURUSD", 1.1050)

market1.display()