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
    PEforward: float
    PEtrailing: float
    PegRatio: float
    ShortRatio: float
    BookValue: float
    PriceToBook: float
    ExDividendDate: datetime = datetime.date.min
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

    def __init__(self, a_ticker: str = 'AAPL'):
        self.__ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)
        self.InfoDic = self.__yFinance.info
        print('InfoDic\r\n', self.InfoDic)
        self.__setInfo()
        self.ActionsDf = self.__yFinance.actions
        self.Balance_SheetDf = self.__yFinance.balance_sheet
        self.BalanceSheetDf = self.__yFinance.balancesheet
        self.CalendarDf = self.__yFinance.calendar
        self.CashFlowDf = self.__yFinance.cashflow
        self.EarningDf = self.__yFinance.earnings
        self.FinancialDf = self.__yFinance.financials
        self.IsIn = "NA" if self.__yFinance.isin == "-" else self.__yFinance.isin
        #self.OptionTuple = self.__yFinance.options#
        self.Balance_SheetQDf = self.__yFinance.quarterly_balance_sheet
        self.BalanceSheetQDf = self.__yFinance.quarterly_balancesheet
        self.CashFlowQDf = self.__yFinance.quarterly_cashflow
        self.EarningQDf = self.__yFinance.quarterly_earnings
        self.FinancialQDf = self.__yFinance.quarterly_financials
        self.RecommendationDf = self.__yFinance.recommendations
        self.SplitSeries = self.__yFinance.splits
        self.SustainabilityDf = self.__yFinance.sustainability

    def __setInfo(self):
        self.Url = self.__getValue('website')
        self.LogoUrl = self.__getValue('logo_url')
        self.Address = self.__getValue('address1')
        self.City = self.__getValue('city')
        self.PostalCode = self.__getValue('zip')
        self.State = self.__getValue('state')
        self.Country = self.__getValue('country')
        self.Beta = self.__getFloat('beta')
        self.Market = self.__getValue('market')
        self.Currency = self.__getValue('currency')
        self.QuoteType = self.__getValue('quoteType')
        self.Exchange = self.__getValue('exchange')
        self.Low52 = self.__getValue('fiftyTwoWeekLow')
        self.High52 = self.__getValue('fiftyTwoWeekHigh')
        self.Average50 = self.__getValue('fiftyDayAverage')
        self.Average200 = self.__getValue('twoHundredDayAverage')
        self.MarketCap = self.__getValue('marketCap')
        self.PayoutRatio = self.__getValue('payoutRatio')
        self.PegRatio = self.__getValue('pegRatio')
        self.PEforward = self.__getValue('forwardPE')
        self.PEtrailing = self.__getValue('trailingPE')
        self.ShortRatio = self.__getValue('shortRatio')
        self.BookValue = self.__getValue('bookValue')
        self.PriceToBook = self.__getValue('priceToBook')
        if type(self.InfoDic['exDividendDate']) == type(1.1):
            self.ExDividendDate = datetime.datetime.fromtimestamp(self.InfoDic['exDividendDate'] / 1e3)

    def __getValue(self, a_key: str = 'NA'):
        if a_key in self.InfoDic:
            return 'None' if self.InfoDic[a_key] is None else self.InfoDic[a_key]
        else:
            return 'NA'

    def __getFloat(self, a_key: str = 'NA'):
        a_str = self.__getValue(a_key)
        if a_str == 'NA' or a_str == '-' or a_str == 'None':
            return -1.0
        else:
            return float(a_str)
