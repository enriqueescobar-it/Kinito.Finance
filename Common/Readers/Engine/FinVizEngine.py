from typing import List
import finviz as FinViz
from Common.Readers.Engine.AbstractEngine import AbstractEngine


class FinVizEngine(AbstractEngine):
    """description of class"""
    AvgVolume: int
    Beta: float
    ChangePcnt: str
    Dividend: str
    DividendPcnt: str
    EarningDate: str
    EpsTtm: float
    EpsQqPcnt: str
    High52: str
    Low52: str
    MarketCap: int
    PayoutPcnt: str
    PeRatio: float
    Price: float
    Range52: List[float]
    RelVolume: float
    Rsi14: str
    StockName: str
    StockSector: str
    StockIndustry: str
    StockCountry: str
    SalesQqPcnt: str
    ShsOutstand: int
    Sma20: str
    Sma50: str
    Sma200: str
    Volume: int
    Volatility: str
    _ticker: str
    _fin_viz: FinViz

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self._fin_viz = FinViz.get_stock(a_ticker)
        print(self._fin_viz.keys())
        self.__setStockName()
        self.__setStockSector()
        self.__setStockIndustry()
        self.__setStockCountry()
        self.__setPeRatio()
        self.__setEarning()
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
        self.__setRsi14()
        self.__setVolatility()
        self.__setPayout()
        self.__setVolume()
        self.__setChangePcnt()
        self.__setPrice()
        '''
        self.__setSalesQq()
        self.__setEpsQq()
        self.__setSma20()
        self.__setSma50()
        self.__setSma200()
        self.__setRelVolume()
        self.__setAvgVolume()'''

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
        self.StockName = self._fin_viz['Company']

    def __setStockSector(self):
        self.StockSector = self._fin_viz['Sector']

    def __setStockIndustry(self):
        self.StockIndustry = self._fin_viz['Industry']

    def __setStockCountry(self):
        self.StockCountry = self._fin_viz['Country']

    def __setPeRatio(self):
        self.PeRatio = self.__stringToFloat(str(self._fin_viz['P/E']))

    def __setEpsTtm(self):
        self.EpsTtm = self.__stringToFloat(str(self._fin_viz['EPS (ttm)']))

    def __setDividend(self):
        self.Dividend = "NA" if self._fin_viz['Dividend'] == "-" else self._fin_viz['Dividend']

    def __setDividendPcnt(self):
        self.DividendPcnt = "NA" if self._fin_viz['Dividend %'] == "-" else self._fin_viz['Dividend %']

    def __setBeta(self):
        self.Beta = -1.1 if self._fin_viz['Beta'] == "-" else float(str(self._fin_viz['Beta']))

    def __setPrice(self):
        self.Price = self.__stringToFloat(str(self._fin_viz['Price']))

    def __setShOutstand(self):
        s: str = str(self._fin_viz['Shs Outstand'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.ShsOutstand = self.__unitsToInt(s)
        else:
            self.ShsOutstand = self.__stringToInt(s)

    def __setMarketCap(self):
        s: str = str(self._fin_viz['Market Cap'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.MarketCap = self.__unitsToInt(s)
        else:
            self.MarketCap = self.__stringToInt(s)

    def __set52wHight(self):
        self.High52 = str(self._fin_viz['52W High'])

    def __set52wLow(self):
        self.Low52 = str(self._fin_viz['52W Low'])

    def __set52wRange(self):
        li = str(self._fin_viz['52W Range']).split()
        self.Range52 = [float(li[0]), float(li[2])]

    def __setSalesQq(self):
        self.SalesQqPcnt = str(self._fin_viz['Sales Q/Q'])

    def __setEpsQq(self):
        self.EpsQqPcnt = str(self._fin_viz['EPS Q/Q'])

    def __setSma20(self):
        self.Sma20 = str(self._fin_viz['SMA20'])

    def __setSma50(self):
        self.Sma50 = str(self._fin_viz['SMA50'])

    def __setSma200(self):
        self.Sma200 = str(self._fin_viz['SMA200'])

    def __setEarning(self):
        self.EarningDate = str(self._fin_viz['Earnings'])

    def __setPayout(self):
        self.PayoutPcnt = str(self._fin_viz['Payout'])

    def __setRelVolume(self):
        self.RelVolume = self.__stringToFloat(str(self._fin_viz['Rel Volume']))

    def __setAvgVolume(self):
        s: str = str(self._fin_viz['Avg Volume'])
        if "K" in s or "M" in s or "G" in s or "B" in s:
            self.AvgVolume = self.__unitsToInt(s)
        else:
            self.AvgVolume = self.__stringToInt(s)

    def __setVolume(self):
        self.Volume = self.__stringToInt(str(self._fin_viz['Volume']))

    def __setChangePcnt(self):
        self.ChangePcnt = str(self._fin_viz['Change'])

    def __setRsi14(self):
        self.Rsi14 = str(self._fin_viz['RSI (14)'])

    def __setVolatility(self):
        self.Volatility = str(self._fin_viz['Volatility'])
