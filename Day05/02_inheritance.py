class Market:

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def display(self):
        print("Symbol:", self.symbol)
        print("Price:", self.price)


class Forex(Market):

    def market_type(self):
        print("Market Type: Forex")


forex = Forex("EURUSD", 1.1050)

forex.display()

forex.market_type()