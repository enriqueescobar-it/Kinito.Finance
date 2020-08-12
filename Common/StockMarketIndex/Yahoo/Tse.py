from Common.AssetTypes.Funds.ExchangeTradedFund import ExchangeTradedFund


class Tse(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'TSE 300 index'
        self.ShortName = 'TSE'
        self.Ticker = '^TSX'
        self.CapType = 'NA'
        self.Size = 300
