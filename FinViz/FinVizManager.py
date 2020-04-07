from typing import List

import Yahoo.YahooTicker as YahooTicker
import finviz as FinViz


class FinVizManager(object):
    """description of class"""
    StockName: str
    PeRatio: float
    EpsTtm: float
    Dividend: str
    DividendPcnt: str
    Beta: float
    Price: float
    ShsOutstand: int
    MarketCap: int
    High52Prcnt: str
    Low52Prcnt: str
    Range52: List[float]
    SalesQqPcnt: str
    EpsQqPcnt: str
    Sma20: str
    Sma50: str
    Sma200: str
    EarningDate: str
    PayoutPcnt: str
    RelVolume: float
    AvgVolume: int
    Volume: int
    ChangePcnt: str

    def __init__(self, yahoo_ticker: YahooTicker):
        self.__yFinViz = FinViz.get_stock(yahoo_ticker.TickerName)
        print(self.__yFinViz.keys())
        print(self.__yFinViz.values())
        self.__setStockName()
        self.__setPeRatio()
        self.__setEpsTtm()
        self.__setDividend()
        self.__setDividendPcnt()
        self.__setBeta()
        self.__setPrice()
        self.__setShOutstand()
        self.__setMarketCap()
        self.__set52wHight()
        self.__set52wLow()
        self.__set52wRange()
        self.__setSalesQq()
        self.__setEpsQq()
        self.__setSma20()
        self.__setSma50()
        self.__setSma200()
        self.__setEarning()
        self.__setPayout()
        self.__setRelVolume()
        self.__setAvgVolume()
        self.__setVolume()
        self.__setChangePcnt()

    @staticmethod
    def __stringToFloat(s: str):
        return float(s)

    @staticmethod
    def __stringToInt(s: str):
        return int(s.replace(',', ''))

    @staticmethod
    def __unitsToInt(s: str):
        f: float = float(s[:-1])
        string = s[-1]
        long: float = 1
        if string == "K":
            long = 10 ** 3
        elif string == "M":
            long = 10 ** 6
        elif string in ["G", "B"]:
            long = 10 ** 9
        return int(f * long)

    def __setStockName(self):
        self.StockName = self.__yFinViz['Index']

    def __setPeRatio(self):
        self.PeRatio = self.__stringToFloat(str(self.__yFinViz['P/E']))

    def __setEpsTtm(self):
        self.EpsTtm = self.__stringToFloat(str(self.__yFinViz['EPS (ttm)']))

    def __setDividend(self):
        self.Dividend = "NA" if self.__yFinViz['Dividend'] == "-" else self.__yFinViz['Dividend']

    def __setDividendPcnt(self):
        self.DividendPcnt = "NA" if self.__yFinViz['Dividend %'] == "-" else self.__yFinViz['Dividend %']

    def __setBeta(self):
        self.Beta = float(str(self.__yFinViz['Beta']))

    def __setPrice(self):
        self.Price = self.__stringToFloat(str(self.__yFinViz['Price']))

    def __setShOutstand(self):
        s: str = str(self.__yFinViz['Shs Outstand'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.ShsOutstand = self.__unitsToInt(s)
        else:
            self.ShsOutstand = self.__stringToInt(s)

    def __setMarketCap(self):
        s: str = str(self.__yFinViz['Market Cap'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.MarketCap = self.__unitsToInt(s)
        else:
            self.MarketCap = self.__stringToInt(s)

    def __set52wHight(self):
        self.High52Prcnt = str(self.__yFinViz['52W High'])

    def __set52wLow(self):
        self.High52Prcnt = str(self.__yFinViz['52W Low'])

    def __set52wRange(self):
        li = str(self.__yFinViz['52W Range']).split()
        self.Range52 = [float(li[0]), float(li[2])]

    def __setSalesQq(self):
        self.SalesQqPcnt = str(self.__yFinViz['Sales Q/Q'])

    def __setEpsQq(self):
        self.EpsQqPcnt = str(self.__yFinViz['EPS Q/Q'])

    def __setSma20(self):
        self.Sma20 = str(self.__yFinViz['SMA20'])

    def __setSma50(self):
        self.Sma50 = str(self.__yFinViz['SMA50'])

    def __setSma200(self):
        self.Sma200 = str(self.__yFinViz['SMA200'])

    def __setEarning(self):
        self.EarningDate = str(self.__yFinViz['Earnings'])

    def __setPayout(self):
        self.PayoutPcnt = str(self.__yFinViz['Payout'])

    def __setRelVolume(self):
        self.RelVolume = self.__stringToFloat(str(self.__yFinViz['Rel Volume']))

    def __setAvgVolume(self):
        s: str = str(self.__yFinViz['Avg Volume'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.AvgVolume = self.__unitsToInt(s)
        else:
            self.AvgVolume = self.__stringToInt(s)

    def __setVolume(self):
        self.Volume = self.__stringToInt(str(self.__yFinViz['Volume']))

    def __setChangePcnt(self):
        self.ChangePcnt = str(self.__yFinViz['Change'])
