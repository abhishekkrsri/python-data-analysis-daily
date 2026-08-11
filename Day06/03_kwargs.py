def market_info(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


market_info(
    symbol="EURUSD",
    price=1.1050,
    timeframe="15M"
)