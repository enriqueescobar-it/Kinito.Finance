from datetime import datetime
import yfinance as yf
import datetime
import pandas as pd
from pandas import Series
from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinanceEngine(AbstractEngine):
    """description of class"""
    Url: str
    LogoUrl: str
    Address: str
    City: str
    State: str
    PostalCode: str
    Country: str
    Beta: float
    Market: str
    Currency: str
    QuoteType: str
    Exchange: str
    High52: float
    Low52: float
    Average50: float
    Average200: float
    MarketCap: float
    PayoutRatio: float
    PegRatio: float
    ShortRatio: float
    BookValue: float
    PriceToBook: float
    ExDividendDate: datetime
    __ticker: str
    InfoDic: dict
    '''ActionsDf: pd.DataFrame
    Balance_SheetDf: pd.DataFrame
    Balance_SheetQDf: pd.DataFrame
    BalanceSheetDf: pd.DataFrame
    BalanceSheetQDf: pd.DataFrame
    CalendarDf: pd.DataFrame
    CashFlowDf: pd.DataFrame
    CashFlowQDf: pd.DataFrame
    EarningDf: pd.DataFrame
    EarningQDf: pd.DataFrame
    FinancialDf: pd.DataFrame
    FinancialQDf: pd.DataFrame
    IsIn: str
    OptionTuple: tuple
    RecommendationDf: pd.DataFrame
    SplitSeries: Series
    SustainabilityDf: pd.DataFrame'''

    def __init__(self, a_ticker: str = 'CNI'):
        self.__ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)
        self.InfoDic = self.__yFinance.info
        print(self.InfoDic)
        self.__setInfo()
        self.ActionsDf = self.__yFinance.actions
        self.Balance_SheetDf = self.__yFinance.balance_sheet
        self.BalanceSheetDf = self.__yFinance.balancesheet
        self.CalendarDf = self.__yFinance.calendar
        self.CashFlowDf = self.__yFinance.cashflow
        self.EarningDf = self.__yFinance.earnings
        self.FinancialDf = self.__yFinance.financials
        self.IsIn = "NA" if self.__yFinance.isin == "-" else self.__yFinance.isin
        self.OptionTuple = self.__yFinance.options
        self.Balance_SheetQDf = self.__yFinance.quarterly_balance_sheet
        self.BalanceSheetQDf = self.__yFinance.quarterly_balancesheet
        self.CashFlowQDf = self.__yFinance.quarterly_cashflow
        self.EarningQDf = self.__yFinance.quarterly_earnings
        self.FinancialQDf = self.__yFinance.quarterly_financials
        self.RecommendationDf = self.__yFinance.recommendations
        self.SplitSeries = self.__yFinance.splits
        self.SustainabilityDf = self.__yFinance.sustainability

    def __setInfo(self):
        self.Url = self.InfoDic['website']
        self.LogoUrl = self.InfoDic['logo_url']
        self.Address = self.InfoDic['address1']
        self.City = self.InfoDic['city']
        self.PostalCode = self.InfoDic['zip']
        self.State = self.InfoDic['state']
        self.Country = self.InfoDic['country']
        self.Beta = float(str(self.InfoDic['beta']))
        self.Market = self.InfoDic['market']
        self.Currency = self.InfoDic['currency']
        self.QuoteType = self.InfoDic['quoteType']
        self.Exchange = self.InfoDic['exchange']
        self.Low52 = self.InfoDic['fiftyTwoWeekLow']
        self.High52 = self.InfoDic['fiftyTwoWeekHigh']
        self.Average50 = self.InfoDic['fiftyDayAverage']
        self.Average200 = self.InfoDic['twoHundredDayAverage']
        self.MarketCap = self.InfoDic['marketCap']
        self.PayoutRatio = self.InfoDic['payoutRatio']
        self.PegRatio = self.InfoDic['pegRatio']
        self.ShortRatio = self.InfoDic['shortRatio']
        self.BookValue = self.InfoDic['bookValue']
        self.PriceToBook = self.InfoDic['priceToBook']
        self.ExDividendDate = datetime.datetime.fromtimestamp(self.InfoDic['exDividendDate'] / 1e3)
