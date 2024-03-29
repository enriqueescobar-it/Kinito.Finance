from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund


class Nikkei(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Nikkei 225'
        self.ShortName = 'Nikkei'
        self.Ticker = 'NA'
        self.CapType = 'L'
        self.Size = 225
