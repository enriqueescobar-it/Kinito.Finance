class Nikkei(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Nikkei 225'
        self.ShortName = 'Nikkei'
        self.YahooTicker = 'NA'
        self.CapType = 'L'
        self.Size = 225
