from Common.AssetTypes.Funds.ExchangeTradedFund import ExchangeTradedFund


class Nasdaq(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'NASDAQ Composite'
        self.ShortName = 'Nasdaq'
        self.Ticker = '^IXIC'
        self.Size = 30
