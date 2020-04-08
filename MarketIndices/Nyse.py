class Nyse(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'NYSE Composite'
        self.ShortName = 'NYSE'
        self.YahooTicker = '^NYA'
        self.CapType = 'L'
        self.Size = 2000
