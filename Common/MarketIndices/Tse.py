class Tse(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'TSE 300 index'
        self.ShortName = 'TSE'
        self.YahooTicker = '^TSX'
        self.CapType = 'NA'
        self.Size = 300
