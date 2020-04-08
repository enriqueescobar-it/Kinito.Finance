class Nasdaq(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'NASDAQ Composite'
        self.ShortName = 'Nasdaq'
        self.YahooTicker = '^IXIC'
        self.Size = 30
