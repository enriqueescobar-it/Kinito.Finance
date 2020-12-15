from datetime import datetime
import yfinance as yf
import datetime
import pandas as pd
from pandas import Series
from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinanceEngine(AbstractEngine):
    """description of class"""
    _info_list: list = list()
    _url: str = 'NA'
    _url_logo: str = 'NA'
    _address: str = 'NA'
    _city: str = 'NA'
    _state: str = 'NA'
    _postal_code: str = 'NA'
    _country: str = 'NA'
    _market: str = 'NA'
    _currency: str = 'NA'
    _quote_type: str = 'NA'
    _exchange: str = 'NA'
    _market_cap: str = 'NA'
    Beta: float = -1.1
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

    @property
    def InfoList(self):
        return self._info_list

    @property
    def Address(self):
        return self._address

    @property
    def City(self):
        return self._city

    @property
    def Country(self):
        return self._country

    @property
    def Currency(self):
        return self._currency

    @property
    def Exchange(self):
        return self._exchange

    @property
    def Market(self):
        return self._market

    @property
    def MarketCap(self):
        return self._market_cap

    @property
    def PostalCode(self):
        return self._postal_code

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def State(self):
        return self._state

    @property
    def Url(self):
        return self._url

    @property
    def UrlLogo(self):
        return self._url_logo

    def __setInfo(self):
        self.InfoDic = self.__yFinance.info
        print('InfoDic\r\n', self.InfoDic)
        self._url = self.__getValueString('website')
        self._info_list.append(self._url)
        self._url_logo = self.__getValueString('logo_url')
        self._info_list.append(self._url_logo)
        self._address = self.__getValueString('address1')
        self._info_list.append(self._address)
        self._city = self.__getValueString('city')
        self._info_list.append(self._city)
        self._postal_code = self.__getValueString('zip')
        self._info_list.append(self._postal_code)
        self._state = self.__getValueString('state')
        self._info_list.append(self._state)
        self._country = self.__getValueString('country')
        self._info_list.append(self._country)
        self._market = self.__getValueString('market')
        self._info_list.append(self._market)
        self._currency = self.__getValueString('currency')
        self._info_list.append(self._currency)
        self._quote_type = self.__getValueString('quoteType')
        self._info_list.append(self._quote_type)
        self._exchange = self.__getValueString('exchange')
        self._info_list.append(self._exchange)
        self._market_cap = self.__getValueString('marketCap')
        self._info_list.append(self._market_cap)
        self.Beta = self.__getFloat('beta')
        self.Low52 = self.__getValueString('fiftyTwoWeekLow')
        self.High52 = self.__getValueString('fiftyTwoWeekHigh')
        self.Average50 = self.__getValueString('fiftyDayAverage')
        self.Average200 = self.__getValueString('twoHundredDayAverage')
        self.PayoutRatio = self.__getValueString('payoutRatio')
        self.PegRatio = self.__getValueString('pegRatio')
        self.PEforward = self.__getValueString('forwardPE')
        self.PEtrailing = self.__getValueString('trailingPE')
        self.ShortRatio = self.__getValueString('shortRatio')
        self.BookValue = self.__getValueString('bookValue')
        self.PriceToBook = self.__getValueString('priceToBook')
        if type(self.InfoDic['exDividendDate']) == type(1.1):
            self.ExDividendDate = datetime.datetime.fromtimestamp(self.InfoDic['exDividendDate'] / 1e3)

    def __getValueString(self, a_key: str = 'NA') -> str:
        if a_key in self.InfoDic:
            return 'None' if self.InfoDic[a_key] is None else self.InfoDic[a_key]
        else:
            return 'NA'

    def __getFloat(self, a_key: str = 'NA') -> float:
        a_str = self.__getValueString(a_key)
        if a_str == 'NA' or a_str == '-' or a_str == 'None':
            return -1.0
        else:
            return float(a_str)
