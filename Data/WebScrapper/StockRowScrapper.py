import Data.Yahoo.YahooTicker as YahooTicker
from Data.StockRow.TermEnums import TermEnums


class StockRowScrapper(object):
    """description of class"""
    Link: str = "https://stockrow.com/api/companies/"
    BalanceSheetUrl: str
    BalanceSheetCsv: str

    def __init__(self, y_ticker: YahooTicker):
        self.__ticker = y_ticker
        self.__setUrl()

    def __setUrl(self):
        temp_term = "Q"
        self.BalanceSheetUrl = self.Link + self.__ticker.TickerName + "/financials.xlsx?dimension=" + temp_term + "&section=Income%20Statement&sort=desc"
        self.BalanceSheetCsv = "C:\\Temp\\StockRow_" + self.__ticker.TickerName + "_BalanceSheet_Quarterly.csv"
