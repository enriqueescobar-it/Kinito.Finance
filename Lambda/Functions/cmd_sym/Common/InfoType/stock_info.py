import json

import yfinance as yf
from pandas import DataFrame
from pandas import Series
from prettytable import PrettyTable

from Common.InfoType.abstract_info import abstract_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund
from Common.StockType.Funds.Index.IndexFund import IndexFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class stock_info(abstract_info):
    __ticker: str = 'NA'
    __yFinance: yf.ticker.Ticker
    __y_fin_dic: dict = {}
    __header: list = ['Info', 'StockInfo']
    _company_name: str = 'NA'
    _has_options: bool = False
    _has_splits: bool = False
    _has_actions: bool = False
    _has_balance_sheet: bool = False
    _has_q_balance_sheet: bool = False
    _has_q_cashflow: bool = False
    _has_q_earnings: bool = False
    _has_q_financials: bool = False
    _url: str = 'NA'
    _url_logo: str = "http://localhost"
    _address1: str = 'NA'
    _address2: str = 'NA'
    _city: str = 'NA'
    _postal_code: str = 'NA'
    _state: str = 'NA'
    _country: str = 'NA'
    _phone: str = 'NA'
    _fax: str = 'NA'
    _market: str = 'NA'
    _currency: str = 'NA'
    _actions_df: DataFrame = DataFrame()
    _balance_sheet_df: DataFrame = DataFrame()
    _q_balance_sheet_df: DataFrame = DataFrame()
    _q_cashflow_df: DataFrame = DataFrame()
    _q_earning_df: DataFrame = DataFrame()
    _q_financial_df: DataFrame = DataFrame()
    _split_series: Series = Series()
    _option_tuple: tuple = tuple()
    _stock_type: AbstractStock

    def __init__(self, a_ticker: str = 'AAPL'):
        self.__ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)

        if '_info' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_info') or any(self.__yFinance.info):
            # if self.__yFinance.__dict__['_info'] is not None:
            self.__get_info()

        if '_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_balance_sheet') or any(self.__yFinance.balance_sheet):
            self.__set_balance_sheet()

        if '_options' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_options') or any(self.__yFinance.options):
            self.__set_option_tuple()

        if '_quarterly_earnings' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_earnings') or any(self.__yFinance.quarterly_earnings):
            self.__set_quarterly_earnings()

        if '_quarterly_cashflow' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_cashflow') or any(self.__yFinance.quarterly_cashflow):
            self.__set_quarterly_cashflow()

        if '_quarterly_financials' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_financials') or any(self.__yFinance.quarterly_financials):
            self.__set_quarterly_financials()

        if '_quarterly_balancesheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_balancesheet') or any(self.__yFinance.quarterly_balancesheet)\
            or '_quarterly_balance_sheet' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_quarterly_balance_sheet') or any(self.__yFinance.quarterly_balance_sheet):
            self.__set_quarterly_balance_sheet()

        self.__set_actions()
        self.__set_splits()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self.__header
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['CompanyName', self._company_name])
        pt.add_row(['URL', self._url])
        pt.add_row(['LogoURL', self._url_logo])
        pt.add_row(['Address1', self._address1])
        pt.add_row(['Address2', self._address2])
        pt.add_row(['City', self._city])
        pt.add_row(['PostalCode', self._postal_code])
        pt.add_row(['State', self._state])
        pt.add_row(['Country', self._country])
        pt.add_row(['Phone', self._phone])
        pt.add_row(['Fax', self._fax])
        pt.add_row(['Market', self._market])
        pt.add_row(['Currency', self._currency])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['HasOptions', self._has_options])
        pt.add_row(['HasSplits', self._has_splits])
        pt.add_row(['HasActions', self._has_actions])
        pt.add_row(['HasBalanceSheet', self._has_balance_sheet])
        pt.add_row(['HasQuarterBalanceSheet', self._has_q_balance_sheet])
        pt.add_row(['HasQuarterCashflow', self._has_q_cashflow])
        pt.add_row(['HasQuarterEarnings', self._has_q_earnings])
        pt.add_row(['HasQuarterFinancials', self._has_q_financials])
        s: str = pt.__str__()
        if self._has_options:
            s += "\n\nOPTION TUPLE\n" + str(self._option_tuple)
        if self._has_splits:
            s += "\n\nSPLIT SERIES\n" + self._split_series.to_string(index=True)
        if self._has_actions:
            s += "\n\nACTION DATAFRAME\n" + self._actions_df.head().to_string(index=True) + "\n" + str(self._actions_df.describe())
        if self._has_balance_sheet:
            s += "\n\nBALANCE SHEET\n\n" + self._balance_sheet_df.to_string(index=True)
        if self._has_q_balance_sheet:
            s += "\n\nQUARTER BALANCESHEET\n" + self._q_balance_sheet_df.to_string(index=True)
        if self._has_q_cashflow:
            s += "\n\nQUARTER CASHFLOW\n" + self._q_cashflow_df.to_string(index=True)
        if self._has_q_earnings:
            s += "\n\nQUARTER EARNINGS\n" + self._q_earning_df.to_string(index=True)
        if self._has_q_financials:
            s += "\n\nQUARTER FINANCIALS\n" + self._q_financial_df.to_string(index=True)
        s += "\n\nSTOCK TYPE\n" + str(self._stock_type)
        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "ticker": self.__ticker,
            "company_name": self._company_name,
            "url": self._url,
            "logo_url": self._url_logo,
            "address1": self._address1,
            "address2": self._address2,
            "city": self._city,
            "postal_code": self._postal_code,
            "state": self._state,
            "country": self._country,
            "phone": self._phone,
            "fax": self._fax,
            "market": self._market,
            "currency": self._currency,
            "quote_type": self._quote_type,
            "has_options": self._has_options,
            "has_splits": self._has_splits,
            "has_actions": self._has_actions,
            "has_balance_sheet": self._has_balance_sheet,
            "has_q_balance_sheet": self._has_q_balance_sheet,
            "has_q_cashflow": self._has_q_cashflow,
            "has_q_earnings": self._has_q_earnings,
            "has_q_financials": self._has_q_financials
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __set_actions(self):
        if any(self.__yFinance.actions):
            self._actions_df = self.__yFinance.actions
            self._has_actions = True

    def __set_splits(self):
        if any(self.__yFinance.splits):
            self._split_series = self.__yFinance.splits
            self._has_splits = True

    def __set_option_tuple(self):
        self._option_tuple = self.__yFinance.options
        self._has_options = self.__yFinance.options == ()

    def __get_info(self):
        if any(self.__yFinance.info):
            #print(self.__y_fin_dic)
            self.__y_fin_dic = self.__yFinance.info
            self._company_name = self.__get_str_from_key('shortName')
            self._url = self.__get_str_from_key('website')
            self._url_logo = self.__get_str_from_key('logo_url')
            self._address1 = self.__get_str_from_key('address1')
            self._address2 = self.__get_str_from_key('address2')
            self._city = self.__get_str_from_key('city')
            self._postal_code = self.__get_str_from_key('zip')
            self._state = self.__get_str_from_key('state')
            self._country = self.__get_str_from_key('country')
            self._phone = self.__get_str_from_key('phone')
            self._fax = self.__get_str_from_key('fax')
            self._market = self.__get_str_from_key('market')
            self._currency = self.__get_str_from_key('currency')
            self._quote_type = self.__get_str_from_key('quoteType')
            self.__get_stock_type(self._quote_type)

    def __set_balance_sheet(self):
        self._balance_sheet_df = self.__yFinance.balance_sheet
        self._has_balance_sheet = any(self._balance_sheet_df) and self._balance_sheet_df.shape[0] > 0

    def __set_quarterly_balance_sheet(self):
        self._q_balance_sheet_df = self.__yFinance.quarterly_balancesheet
        self._q_balance_sheet_df = self.__yFinance.quarterly_balance_sheet
        self._has_q_balance_sheet = any(self._q_balance_sheet_df) and self._q_balance_sheet_df.shape[0] > 0

    def __set_quarterly_cashflow(self):
        self._q_cashflow_df = self.__yFinance.quarterly_cashflow
        self._has_q_cashflow = any(self._q_cashflow_df) and self._q_cashflow_df.shape[0] > 0

    def __set_quarterly_earnings(self):
        self._q_earning_df = self.__yFinance.quarterly_earnings
        self._has_q_earnings = any(self._q_earning_df) and self._q_earning_df.shape[0] > 0

    def __set_quarterly_financials(self):
        self._q_financial_df = self.__yFinance.quarterly_financials
        self._has_q_financials = any(self._q_financial_df) and self._q_financial_df.shape[0] > 0

    def __get_str_from_key(self, a_key: str = 'NA') -> str:
        if a_key in self.__y_fin_dic:
            return 'None' if self.__y_fin_dic[a_key] is None else self.__y_fin_dic[a_key]
        else:
            return 'NA'

    def __get_stock_type(self, s: str = ''):
        if s == 'ETF':
            self._stock_type = ExchangeTradedFund(self._company_name, self.__ticker, s)
        elif s == 'INDEX':
            self._stock_type = IndexFund(self._company_name, self.__ticker, s)
        elif s == 'MUTUALFUND':
            self._stock_type = MutualFund(self._company_name, self.__ticker, s)
        elif s == 'CRYPTOCURRENCY':
            self._stock_type = CryptoCurrency(self._company_name, self.__ticker, s)
        elif s == 'CURRENCY':
            self._stock_type = RegularCurrency(self._company_name, self.__ticker, s)
        elif s == 'FUTURE':
            self._stock_type = AbstractStockFuture(self._company_name, self.__ticker, s)
        elif s == 'EQUITY':
            self._stock_type = AbstractStockEquity(self._company_name, self.__ticker, s)
        else:
        #    self._stock_type = AbstractStockOption(self._company_name, self.__ticker)
            self._stock_type = AbstractStockBond(self._company_name, self.__ticker, s)

    @property
    def ActionDataFrame(self):
        return self._actions_df

    @property
    def BalanceSheetDataFrame(self):
        return self._balance_sheet_df

    @property
    def CompanyName(self):
        return self._company_name

    @property
    def OptionTuple(self):
        return self._option_tuple

    @property
    def QuarterBalanceSheetDataFrame(self):
        return self._q_balance_sheet_df

    @property
    def QuarterCashflowDataFrame(self):
        return self._q_cashflow_df

    @property
    def QuarterEarningDataFrame(self):
        return self._q_earning_df

    @property
    def QuarterFinancialDataFrame(self):
        return self._q_financial_df

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def SplitSeries(self):
        return self._split_series

    @property
    def StockType(self):
        return self._stock_type

    @property
    def HasOptions(self):
        return self._has_options

    @property
    def HasSplits(self):
        return self._has_splits

    @property
    def HasActions(self):
        return self._has_actions

    @property
    def HasBalanceSheet(self):
        return self._has_balance_sheet

    @property
    def HasQuarterBalanceSheet(self):
        return self._has_q_balance_sheet

    @property
    def HasQuarterCashflow(self):
        return self._has_q_cashflow

    @property
    def HasQuarterEarnings(self):
        return self._has_q_earnings

    @property
    def HasQuarterFinancials(self):
        return self._has_q_financials
