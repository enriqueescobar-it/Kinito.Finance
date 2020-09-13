from datetime import datetime
import yfinance as yf
import datetime
import pandas as pd
from pandas import Series
from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinanceEngine(AbstractEngine):
    """description of class"""
    Url: str = 'NA'
    LogoUrl: str = 'NA'
    Address: str = 'NA'
    City: str = 'NA'
    State: str = 'NA'
    PostalCode: str = 'NA'
    Country: str = 'NA'
    Beta: float = -1.1
    Market: str = 'NA'
    Currency: str = 'NA'
    QuoteType: str = 'NA'
    Exchange: str = 'NA'
    High52: float = -1.1
    Low52: float = -1.1
    Average50: float = -1.1
    Average200: float = -1.1
    MarketCap: float = -1.1
    PayoutRatio: float = -1.1
    PEforward: float = -1.1
    PEtrailing: float = -1.1
    PegRatio: float = -1.1
    ShortRatio: float = -1.1
    BookValue: float = -1.1
    PriceToBook: float = -1.1
    ExDividendDate: datetime = datetime.date.min
    __ticker: str = 'NA'
    InfoDic: dict #= dict()
    ActionsDf: pd.DataFrame = pd.DataFrame()
    Balance_SheetDf: pd.DataFrame = pd.DataFrame()
    BalanceSheetDf: pd.DataFrame = pd.DataFrame()
    CalendarDf: pd.DataFrame = pd.DataFrame()
    CashFlowDf: pd.DataFrame = pd.DataFrame()
    EarningDf:pd.DataFrame = pd.DataFrame()
    FinancialDf: pd.DataFrame = pd.DataFrame()
    IsIn: str = 'NA'
    Balance_SheetQDf: pd.DataFrame = pd.DataFrame()
    BalanceSheetQDf: pd.DataFrame = pd.DataFrame()
    CashFlowQDf: pd.DataFrame = pd.DataFrame()
    EarningQDf: pd.DataFrame = pd.DataFrame()
    FinancialQDf: pd.DataFrame = pd.DataFrame()
    RecommendationDf: pd.DataFrame = pd.DataFrame()
    SplitSeries: Series
    SustainabilityDf: pd.DataFrame = pd.DataFrame()
    OptionTuple: tuple

    def __init__(self, a_ticker: str = 'AAPL'):
        self.__ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)
        if '_info' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_info'):
            #if self.__yFinance.__dict__['_info'] is not None:
            self.__setInfo()
        self.ActionsDf = self.__yFinance.actions
        if '_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_balance_sheet'):
            self.Balance_SheetDf = self.__yFinance.balance_sheet
        #self.BalanceSheetDf = self.__yFinance.balancesheet
        #self.CalendarDf = self.__yFinance.calendar
        #self.CashFlowDf = self.__yFinance.cashflow
        #self.EarningDf = self.__yFinance.earnings
        #self.FinancialDf = self.__yFinance.financials
        #self.IsIn = "NA" if self.__yFinance.isin == "-" else self.__yFinance.isin
        if '_options' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_options'):
            self.OptionTuple = self.__yFinance.options
        if '_quarterly_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_balance_sheet'):
            self.Balance_SheetQDf = self.__yFinance.quarterly_balance_sheet
        if '_quarterly_balancesheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_balancesheet'):
            self.BalanceSheetQDf = self.__yFinance.quarterly_balancesheet
        if '_quarterly_cashflow' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_cashflow'):
            self.CashFlowQDf = self.__yFinance.quarterly_cashflow
        if '_quarterly_earnings' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_earnings'):
            self.EarningQDf = self.__yFinance.quarterly_earnings
        if '_quarterly_financials' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_financials'):
            self.FinancialQDf = self.__yFinance.quarterly_financials
        #self.RecommendationDf = self.__yFinance.recommendations
        self.SplitSeries = self.__yFinance.splits
        #self.SustainabilityDf = self.__yFinance.sustainability

    def __setInfo(self):
        self.InfoDic = self.__yFinance.info
        print('InfoDic\r\n', self.InfoDic)
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
