from yahoofinancials import YahooFinancials
import DataReaders.YahooTicker as YahooTicker
from datetime import date


class FinancialManager(object):
    """description of class"""
    StockName: str
    PeRatio: float
    FromDate: date
    FromDateStr: str
    ToDate: date
    ToDateStr: str
    Financial: YahooFinancials
    HistoricalPriceDic: dict
    FinancialTypeDic: dict

    def __init__(self, yahoo_ticker: YahooTicker):
        self.__dateFormat: str = '%Y-%m-%d'
        self.__ticker = yahoo_ticker
        self.__setFrom(yahoo_ticker.DateTimeFrom)
        self.__setTo(yahoo_ticker.DateTimeTo)
        self.Financial = YahooFinancials(self.__ticker.TickerName)
        self.HistoricalPriceDic = self.Financial.get_historical_price_data(self.FromDateStr, self.ToDateStr, 'daily')[self.__ticker.TickerName]
        self.__setStockName()
        self.__setPeRatio()
        self.FinancialTypeDic = self.Financial.YAHOO_FINANCIAL_TYPES

    def __setStockName(self):
        self.StockName = (
            'NA'
            if self.Financial.get_stock_exchange() is None
            else self.Financial.get_stock_exchange()
        )

    def __setPeRatio(self):
        self.PeRatio = (
            0.0
            if self.Financial.get_pe_ratio() is None
            else self.Financial.get_pe_ratio()
        )

    def __setFrom(self, from_date: date):
        self.FromDate = from_date
        self.FromDateStr = from_date.strftime(self.__dateFormat)

    def __setTo(self, to_date: date):
        self.ToDate = to_date
        self.ToDateStr = to_date.strftime(self.__dateFormat)

    def GetDailyHistoricalDataPrices(self, from_date: date, to_date: date):
        self.__setFrom(from_date)
        self.__setTo(to_date)
        return self.HistoricalPriceDic['prices']
