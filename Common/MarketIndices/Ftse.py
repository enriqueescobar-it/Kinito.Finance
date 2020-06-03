class Ftse(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Financial Times Stock Exchange 100 Index'
        self.ShortName = 'FTSE'
        self.YahooTicker = '^FTSE'
        self.CapType = 'L'
        self.Size = 100
