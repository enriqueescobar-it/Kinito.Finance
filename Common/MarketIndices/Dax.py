class Dax(object):
    ShortName: str
    LongName: str
    YahooTicker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Deutscher Aktienindex'
        self.ShortName = 'DAX'
        self.YahooTicker = '^GDAXI'
        self.CapType = 'L'
        self.Size = 30
