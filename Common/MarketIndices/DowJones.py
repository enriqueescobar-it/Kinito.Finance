class DowJones(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Dow Jones Industrial Average'
        self.ShortName = 'DowJones'
        self.YahooTicker = '^DJI'
        self.CapType = 'L'
        self.Size = 30
