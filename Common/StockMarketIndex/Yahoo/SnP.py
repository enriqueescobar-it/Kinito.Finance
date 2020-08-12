from Common.AssetTypes.Funds.ExchangeTradedFund import ExchangeTradedFund


class SnP(ExchangeTradedFund):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'S&P 500'
        self.ShortName = 'S&P'
        self.YahooTicker = '^GSPC'
        self.CapType = 'L'
        self.Size = 500
