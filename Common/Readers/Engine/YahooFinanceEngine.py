import pandas as pd
import numpy as np
import yfinance as yf
from pandas import Series
from prettytable import PrettyTable
from Common.Readers.Engine.AbstractEngine import AbstractEngine
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Funds.ExchangeTradedFund import ExchangeTradedFund
from Common.StockType.Funds.IndexFund import IndexFund
from Common.StockType.Funds.MutualFund import MutualFund
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class YahooFinanceEngine(AbstractEngine):
    __pretty_table: PrettyTable = PrettyTable()
    _info_labels: list = list()
    _info_list: list = list()
    __ticker: str = 'NA'
    _stock_type: AbstractStock
    _url: str = 'NA'
    _url_logo: str = 'NA'
    _address1: str = 'NA'
    _address2: str = 'NA'
    _city: str = 'NA'
    _company_name: str = 'NA'
    _country: str = 'NA'
    _currency: str = 'NA'
    _exchange: str = 'NA'
    _fax: str = 'NA'
    _state: str = 'NA'
    _phone: str = 'NA'
    _postal_code: str = 'NA'
    _market: str = 'NA'
    _market_cap: str = 'NA'
    _quote_type: str = 'NA'
    _beta: float = -1.1
    _high52: float = -1.1
    _low52: float = -1.1
    _high_today: float = -1.1
    _low_today: float = -1.1
    _avg50: float = -1.1
    _avg200: float = -1.1
    _ratio_payout: float = -1.1
    _ratio_peg: float = -1.1
    _ratio_short: float = -1.1
    _pe_forward: float = -1.1
    _pe_trailing: float = -1.1
    _book_value: float = -1.1
    _book_price_to: float = -1.1
    _ent_value: int = -1
    _ent2revenue: float = -1.1
    _ent2ebitda: float = -1.1
    _div_rate: float = -1.1
    _div_5y_avg_yield: float = -1.1
    _div_yield: float = -1.1
    _div_last_value: float = -1.1
    _div_last_date: int = -1
    _div_ex_date: int = -1
    _div_last_date: int = -1
    _split_date: int = -1
    _fiscal_year_end_last: int = -1
    _fiscal_year_end_next: int = -1
    _last_quarter: int = -1
    InfoDic: dict  # = dict()
    ActionsDf: pd.DataFrame = pd.DataFrame()
    Balance_SheetDf: pd.DataFrame = pd.DataFrame()
    BalanceSheetDf: pd.DataFrame = pd.DataFrame()
    CalendarDf: pd.DataFrame = pd.DataFrame()
    CashFlowDf: pd.DataFrame = pd.DataFrame()
    EarningDf: pd.DataFrame = pd.DataFrame()
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
            # if self.__yFinance.__dict__['_info'] is not None:
            self.__setInfo()
        self.ActionsDf = self.__yFinance.actions
        if '_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_balance_sheet'):
            self.Balance_SheetDf = self.__yFinance.balance_sheet
        # self.BalanceSheetDf = self.__yFinance.balancesheet
        # self.CalendarDf = self.__yFinance.calendar
        # self.CashFlowDf = self.__yFinance.cashflow
        # self.EarningDf = self.__yFinance.earnings
        # self.FinancialDf = self.__yFinance.financials
        # self.IsIn = "NA" if self.__yFinance.isin == "-" else self.__yFinance.isin
        if '_options' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_options'):
            self.OptionTuple = self.__yFinance.options
        if '_quarterly_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance,
                                                                             '_quarterly_balance_sheet'):
            self.Balance_SheetQDf = self.__yFinance.quarterly_balance_sheet
        if '_quarterly_balancesheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_balancesheet'):
            self.BalanceSheetQDf = self.__yFinance.quarterly_balancesheet
        if '_quarterly_cashflow' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_cashflow'):
            self.CashFlowQDf = self.__yFinance.quarterly_cashflow
        if '_quarterly_earnings' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_earnings'):
            self.EarningQDf = self.__yFinance.quarterly_earnings
        if '_quarterly_financials' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_financials'):
            self.FinancialQDf = self.__yFinance.quarterly_financials
        # self.RecommendationDf = self.__yFinance.recommendations
        self.SplitSeries = self.__yFinance.splits
        # self.SustainabilityDf = self.__yFinance.sustainability
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column('Type', self.InfoList)

    def __str__(self):
        return self.__pretty_table.__str__()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def AddressFirst(self):
        return self._address1

    @property
    def AddressSecond(self):
        return self._address2

    @property
    def Average50(self):
        return self._avg50

    @property
    def Average200(self):
        return self._avg200

    @property
    def Beta(self):
        return self._beta

    @property
    def BookValue(self):
        return self._book_value

    @property
    def BookPriceTo(self):
        return self._book_price_to

    @property
    def City(self):
        return self._city

    @property
    def CompanyName(self):
        return self._company_name

    @property
    def Country(self):
        return self._country

    @property
    def Currency(self):
        return self._currency

    @property
    def DateExDividend(self):
        return self._div_ex_date

    @property
    def DateLastQuarter(self):
        return self._last_quarter

    @property
    def DateSplit(self):
        return self._split_date

    @property
    def DividendRate(self):
        return self._div_rate

    @property
    def DividendLastDate(self):
        return self._div_last_date

    @property
    def DividendLastValue(self):
        return self._div_last_value

    @property
    def DividendYield(self):
        return self._div_yield

    @property
    def Dividend5yAvgYield(self):
        return self._div_5y_avg_yield

    @property
    def EntValue(self):
        return self._ent_value

    @property
    def EntToRevenue(self):
        return self._ent2revenue

    @property
    def EntToEbitda(self):
        return self._ent2ebitda

    @property
    def Exchange(self):
        return self._exchange

    @property
    def Fax(self):
        return self._fax

    @property
    def FiscalYearEndLastDate(self):
        return self._fiscal_year_end_last

    @property
    def FiscalYearEndNextDate(self):
        return self._fiscal_year_end_next

    @property
    def High52(self):
        return self._high52

    @property
    def HighToday(self):
        return self._high_today

    @property
    def Low52(self):
        return self._low52

    @property
    def LowToday(self):
        return self._low_today

    @property
    def Market(self):
        return self._market

    @property
    def MarketCap(self):
        return self._market_cap

    @property
    def PeForward(self):
        return self._pe_forward

    @property
    def PeTrailing(self):
        return self._pe_trailing

    @property
    def Phone(self):
        return self._phone

    @property
    def PostalCode(self):
        return self._postal_code

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def RatioPayout(self):
        return self._ratio_payout

    @property
    def RatioPeg(self):
        return self._ratio_peg

    @property
    def RatioShort(self):
        return self._ratio_short

    @property
    def State(self):
        return self._state

    @property
    def StockType(self):
        return self._stock_type

    @property
    def Url(self):
        return self._url

    @property
    def UrlLogo(self):
        return self._url_logo

    def __setInfo(self):
        self.InfoDic = self.__yFinance.info
        print('InfoDic\r\n', self.InfoDic)
        self._url = self.__getValueFromKey('website')
        self._info_labels.append('website')
        self._info_list.append(self._url)
        self._url_logo = self.__getValueFromKey('logo_url')
        self._info_labels.append('logo_url')
        self._info_list.append(self._url_logo)
        self._company_name = self.__getValueFromKey('shortName')
        self._info_labels.append('shortName')
        self._info_list.append(self._company_name)
        self._address1 = self.__getValueFromKey('address1')
        self._info_labels.append('address1')
        self._info_list.append(self._address1)
        self._address2 = self.__getValueFromKey('address2')
        self._info_labels.append('address2')
        self._info_list.append(self._address2)
        self._city = self.__getValueFromKey('city')
        self._info_labels.append('city')
        self._info_list.append(self._city)
        self._postal_code = self.__getValueFromKey('zip')
        self._info_labels.append('zip')
        self._info_list.append(self._postal_code)
        self._state = self.__getValueFromKey('state')
        self._info_labels.append('state')
        self._info_list.append(self._state)
        self._country = self.__getValueFromKey('country')
        self._info_labels.append('country')
        self._info_list.append(self._country)
        self._phone = self.__getValueFromKey('phone')
        self._info_labels.append('phone')
        self._info_list.append(self._phone)
        self._fax = self.__getValueFromKey('fax')
        self._info_labels.append('fax')
        self._info_list.append(self._fax)
        self._market = self.__getValueFromKey('market')
        self._info_labels.append('market')
        self._info_list.append(self._market)
        self._currency = self.__getValueFromKey('currency')
        self._info_labels.append('currency')
        self._info_list.append(self._currency)
        self._quote_type = self.__getValueFromKey('quoteType')
        self.__setStockType(self._quote_type)
        self._info_labels.append('quoteType')
        self._info_list.append(self._quote_type)
        self._exchange = self.__getValueFromKey('exchange')
        self._info_labels.append('exchange')
        self._info_list.append(self._exchange)
        self._market_cap = self.__getValueFromKey('marketCap')
        self._info_labels.append('marketCap')
        self._info_list.append(self._market_cap)
        self._ent_value = self.__getValueFromKey('enterpriseValue')
        self._info_labels.append('enterpriseValue')
        self._info_list.append(self._ent_value)
        self._ent2revenue = self.__getValueFromKey('enterpriseToRevenue')
        self._info_labels.append('enterpriseToRevenue')
        self._info_list.append(self._ent2revenue)
        self._ent2ebitda = self.__getValueFromKey('enterpriseToEbitda')
        self._info_labels.append('enterpriseToEbitda')
        self._info_list.append(self._ent2ebitda)
        self._beta = self.__getFloatFromString('beta')
        self._info_labels.append('beta')
        self._info_list.append(self._beta)
        self._low52 = self.__getValueFromKey('fiftyTwoWeekLow')
        self._info_labels.append('fiftyTwoWeekLow')
        self._info_list.append(self._low52)
        self._high52 = self.__getValueFromKey('fiftyTwoWeekHigh')
        self._info_labels.append('fiftyTwoWeekHigh')
        self._info_list.append(self._high52)
        self._low_today = self.__getValueFromKey('dayLow')
        self._info_labels.append('dayLow')
        self._info_list.append(self._low_today)
        self._high_today = self.__getValueFromKey('dayHigh')
        self._info_labels.append('dayHigh')
        self._info_list.append(self._high_today)
        self._avg50 = self.__getValueFromKey('fiftyDayAverage')
        self._info_labels.append('fiftyDayAverage')
        self._info_list.append(self._avg50)
        self._avg200 = self.__getValueFromKey('twoHundredDayAverage')
        self._info_labels.append('twoHundredDayAverage')
        self._info_list.append(self._avg200)
        self._ratio_payout = self.__getValueFromKey('payoutRatio')
        self._info_labels.append('payoutRatio')
        self._info_list.append(self._ratio_payout)
        self._ratio_peg = self.__getValueFromKey('pegRatio')
        self._info_labels.append('pegRatio')
        self._info_list.append(self._ratio_peg)
        self._ratio_short = self.__getValueFromKey('shortRatio')
        self._info_labels.append('shortRatio')
        self._info_list.append(self._ratio_short)
        self._pe_forward = self.__getValueFromKey('forwardPE')
        self._info_labels.append('forwardPE')
        self._info_list.append(self._pe_forward)
        self._pe_trailing = self.__getValueFromKey('trailingPE')
        self._info_labels.append('trailingPE')
        self._info_list.append(self._pe_trailing)
        self._book_value = self.__getValueFromKey('bookValue')
        self._info_labels.append('bookValue')
        self._info_list.append(self._book_value)
        self._book_price_to = self.__getValueFromKey('priceToBook')
        self._info_labels.append('priceToBook')
        self._info_list.append(self._book_price_to)
        self._div_ex_date = self.__getValueFromKey('exDividendDate')
        self._info_labels.append('exDividendDate')
        self._info_list.append(self._div_ex_date)
        self._split_date = self.__getValueFromKey('lastSplitDate')
        self._info_labels.append('lastSplitDate')
        self._info_list.append(self._split_date)
        self._div_last_date = self.__getValueFromKey('lastDividendDate')
        self._info_labels.append('lastDividendDate')
        self._info_list.append(self._div_last_date)
        self._div_rate = self.__getValueFromKey('dividendRate')
        self._info_labels.append('dividendRate')
        self._info_list.append(self._div_rate)
        self._div_5y_avg_yield = self.__getValueFromKey('fiveYearAvgDividendYield')
        self._info_labels.append('fiveYearAvgDividendYield')
        self._info_list.append(self._div_5y_avg_yield)
        self._div_yield = self.__getValueFromKey('dividendYield')
        self._info_labels.append('dividendYield')
        self._info_list.append(self._div_yield)
        self._div_last_value = self.__getValueFromKey('lastDividendValue')
        self._info_labels.append('lastDividendValue')
        self._info_list.append(self._div_last_value)
        self._div_last_date = self.__getValueFromKey('lastDividendDate')
        self._info_labels.append('lastDividendDate')
        self._info_list.append(self._div_last_date)
        self._fiscal_year_end_last = self.__getValueFromKey('lastFiscalYearEnd')
        self._info_labels.append('lastFiscalYearEnd')
        self._info_list.append(self._fiscal_year_end_last)
        self._fiscal_year_end_next = self.__getValueFromKey('nextFiscalYearEnd')
        self._info_labels.append('nextFiscalYearEnd')
        self._info_list.append(self._fiscal_year_end_next)
        self._last_quarter = self.__getValueFromKey('mostRecentQuarter')
        self._info_labels.append('mostRecentQuarter')
        self._info_list.append(self._last_quarter)

    def __getValueFromKey(self, a_key: str = 'NA') -> str:
        if a_key in self.InfoDic:
            return 'None' if self.InfoDic[a_key] is None else self.InfoDic[a_key]
        else:
            return 'NA'

    def __getFloatFromString(self, a_key: str = 'NA') -> float:
        a_str = self.__getValueFromKey(a_key)
        if a_str == 'NA' or a_str == '-' or a_str == 'None':
            return np.nan
        else:
            return float(a_str)

    def __setStockType(self, s: str = ''):
        if s == 'ETF':
            self._stock_type = ExchangeTradedFund(self.CompanyName, self.__ticker)
        if s == 'INDEX':
            self._stock_type = IndexFund()
        if s == 'MUTUALFUND':
            self._stock_type = MutualFund(self.CompanyName, self.__ticker)
        if s == 'CRYPTOCURRENCY':
            self._stock_type = CryptoCurrency()
        if s == 'CURRENCY':
            self._stock_type = RegularCurrency()
        if s == 'FUTURE':
            self._stock_type = AbstractStockFuture()
        if s == 'EQUITY':
            self._stock_type = AbstractStockEquity()
