from Common.AssetTypes.Funds.ExchangeTradedFund import ExchangeTradedFund


class Nyse(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'NYSE Composite'
        self.ShortName = 'NYSE'
        self.Ticker = '^NYA'
        self.CapType = 'L'
        self.Size = 2000
