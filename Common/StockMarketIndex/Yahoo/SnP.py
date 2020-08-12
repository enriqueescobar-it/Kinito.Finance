from Common.AssetTypes.Funds.ExchangeTradedFund import ExchangeTradedFund


class SnP(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'S&P 500'
        self.ShortName = 'S&P'
        self.Ticker = '^GSPC'
        self.CapType = 'L'
        self.Size = 500
