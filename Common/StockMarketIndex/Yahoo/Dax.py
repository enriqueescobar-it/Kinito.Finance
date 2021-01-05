from Common.StockType.Funds.ExchangeTradedFund import ExchangeTradedFund


class Dax(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Deutscher Aktienindex'
        self.ShortName = 'DAX'
        self.Ticker = '^GDAXI'
        self.CapType = 'L'
        self.Size = 30
