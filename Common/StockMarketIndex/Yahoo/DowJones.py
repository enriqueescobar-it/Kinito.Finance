from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund


class DowJones(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Dow Jones Industrial Average'
        self.ShortName = 'DowJones'
        self.Ticker = '^DJI'
        self.CapType = 'L'
        self.Size = 30
