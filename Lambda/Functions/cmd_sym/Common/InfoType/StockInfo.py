import json
from datetime import datetime

import numpy as np
import yfinance as yf
from pandas import DataFrame
from pandas import Series
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund
from Common.StockType.Funds.Index.IndexFund import IndexFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class StockInfo(AbstractInfo):
    __ticker: str = 'NA'
    __y_finance: yf.ticker.Ticker
    __y_fin_dic: dict = {}
    __header: list = ['Info', 'StockInfo']
    _past_years: int = 5
    _date_time: datetime = datetime.now()
    _date_time_zone: str = "GMT"
    _date_time_format: str = "%Y-%m-%d %H:%M:%S"
    _quarter_info: QuarterInfo = QuarterInfo()
    _company_name: str = 'NA'
    _has_option_tuple: bool = False
    _has_split_series: bool = False
    _has_action_df: bool = False
    _has_balance_sheet_df: bool = False
    _has_q_balance_sheet_df: bool = False
    _has_q_cashflow_df: bool = False
    _has_q_earning_df: bool = False
    _has_q_financial_df: bool = False
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
    _action_df: DataFrame = DataFrame()
    _balance_sheet_df: DataFrame = DataFrame()
    _q_balance_sheet_df: DataFrame = DataFrame()
    _q_cashflow_df: DataFrame = DataFrame()
    _q_earning_df: DataFrame = DataFrame()
    _q_financial_df: DataFrame = DataFrame()
    _split_series: Series = Series()
    _option_tuple: tuple = tuple()
    _stock_type: AbstractStock

    def __init__(self, a_ticker: str = 'AAPL', past_years: int = 5):
        self.__ticker = a_ticker
        self.__y_finance = yf.Ticker(a_ticker)
        self._past_years = past_years

        if '_info' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_info') or any(self.__y_finance.info):
            # if self.__yFinance.__dict__['_info'] is not None:
            self.__get_info()

        if '_balance_sheet' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_balance_sheet') or\
                any(self.__y_finance.balance_sheet):
            self.__set_balance_sheet_df()

        if '_options' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_options') or\
                any(self.__y_finance.options):
            self.__set_option_tuple()

        if '_quarterly_earnings' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_quarterly_earnings') or\
                any(self.__y_finance.quarterly_earnings):
            self.__set_q_earning_df()

        if '_quarterly_cashflow' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_quarterly_cashflow') or\
                any(self.__y_finance.quarterly_cashflow):
            self.__set_q_cashflow_df()

        if '_quarterly_financials' in self.__y_finance.__dict__ or hasattr(self.__y_finance, '_quarterly_financials')\
                or any(self.__y_finance.quarterly_financials):
            self.__set_q_financial_df()

        if '_quarterly_balancesheet' in self.__y_finance.__dict__ or\
                hasattr(self.__y_finance, '_quarterly_balancesheet') or any(self.__y_finance.quarterly_balancesheet) or\
                '_quarterly_balance_sheet' in self.__y_finance.__dict__ or\
                hasattr(self.__y_finance, '_quarterly_balance_sheet') or any(self.__y_finance.quarterly_balance_sheet):
            self.__set_q_balance_sheet_df()

        self.__set_action_df()
        self.__set_split_series()

    def __is_df_valid(self, a_df: any) -> bool:
        return any(a_df) and isinstance(a_df, DataFrame) and not a_df.empty and\
               not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0

    def __get_str_from_key(self, a_key: str = 'NA') -> str:
        if a_key in self.__y_fin_dic:
            return 'None' if self.__y_fin_dic[a_key] is None else self.__y_fin_dic[a_key]
        else:
            return 'NA'

    def __get_info(self):
        if any(self.__y_finance.info):
            #print(self.__y_fin_dic)
            self.__y_fin_dic = self.__y_finance.info
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
        #    self._stock_type = AbstractStock()

    def __set_action_df(self):
        self._has_action_df = self.__is_df_valid(self.__y_finance.actions)
        if self._has_action_df:
            self._action_df = self.__y_finance.actions.fillna(value=np.nan, inplace=False)

    def __set_split_series(self):
        self._has_split_series = any(self.__y_finance.splits) and isinstance(self.__y_finance.splits, Series)
        if self._has_split_series:
            self._split_series = self.__y_finance.splits

    def __set_balance_sheet_df(self):
        self._has_balance_sheet_df = self.__is_df_valid(self.__y_finance.balance_sheet)
        if self._has_balance_sheet_df:
            self._balance_sheet_df = self.__y_finance.balance_sheet.fillna(value=np.nan, inplace=False)

    def __set_option_tuple(self):
        self._has_option_tuple = self.__y_finance.options == ()
        if self._has_option_tuple:
            self._option_tuple = self.__y_finance.options

    def __set_q_balance_sheet_df(self):
        self._has_q_balance_sheet_df = self.__is_df_valid(self.__y_finance.quarterly_balancesheet) or \
                                       self.__is_df_valid(self.__y_finance.quarterly_balance_sheet)
        if self._has_q_balance_sheet_df:
            self._q_balance_sheet_df = self.__y_finance.quarterly_balancesheet.fillna(value=np.nan, inplace=False)
            self._q_balance_sheet_df = self.__y_finance.quarterly_balance_sheet.fillna(value=np.nan, inplace=False)

    def __set_q_cashflow_df(self):
        self._has_q_cashflow_df = self.__is_df_valid(self.__y_finance.quarterly_cashflow)
        if self._has_q_cashflow_df:
            self._q_cashflow_df = self.__y_finance.quarterly_cashflow.fillna(value=np.nan, inplace=False)

    def __set_q_earning_df(self):
        self._has_q_earning_df = self.__is_df_valid(self.__y_finance.quarterly_earnings)
        if self._has_q_earning_df:
            self._q_earning_df = self.__y_finance.quarterly_earnings.fillna(value=np.nan, inplace=False)

    def __set_q_financial_df(self):
        self._has_q_financial_df = self.__is_df_valid(self.__y_finance.quarterly_financials)
        if self._has_q_financial_df:
            self._q_financial_df = self.__y_finance.quarterly_financials.fillna(value=np.nan, inplace=False)

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
        pt.add_row(['HasOptionTuple', self._has_option_tuple])
        pt.add_row(['HasSplitSeries', self._has_split_series])
        pt.add_row(['HasActionDf', self._has_action_df])
        pt.add_row(['HasBalanceSheetDf', self._has_balance_sheet_df])
        pt.add_row(['HasQuarterBalanceSheetDf', self._has_q_balance_sheet_df])
        pt.add_row(['HasQuarterCashflowDf', self._has_q_cashflow_df])
        pt.add_row(['HasQuarterEarningDf', self._has_q_earning_df])
        pt.add_row(['HasQuarterFinancialDf', self._has_q_financial_df])
        s: str = pt.__str__()
        if self._has_option_tuple:
            s += "\n\nOPTION TUPLE\n" + str(self._option_tuple)
        if self._has_split_series:
            s += "\n\nSPLIT SERIES\n" + self._split_series.to_string(index=True)
        if self._has_action_df:
            s += "\n\nACTION DATAFRAME\n" + self._action_df.head().to_string(index=True)
        if self._has_balance_sheet_df:
            s += "\n\nBALANCE SHEET DATAFRAME\n\n" + self._balance_sheet_df.to_string(index=True)
        if self._has_q_balance_sheet_df:
            s += "\n\nQUARTER BALANCE SHEET DATAFRAME\n" + self._q_balance_sheet_df.to_string(index=True)
        if self._has_q_cashflow_df:
            s += "\n\nQUARTER CASHFLOW DATAFRAME\n" + self._q_cashflow_df.to_string(index=True)
        if self._has_q_earning_df:
            s += "\n\nQUARTER EARNING DATAFRAME\n" + self._q_earning_df.to_string(index=True)
        if self._has_q_financial_df:
            s += "\n\nQUARTER FINANCIAL DATAFRAME\n" + self._q_financial_df.to_string(index=True)
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
            "has_option_tuple": self._has_option_tuple,
            "has_split_series": self._has_split_series,
            "has_action_df": self._has_action_df,
            "has_balance_sheet_df": self._has_balance_sheet_df,
            "has_q_balance_sheet_df": self._has_q_balance_sheet_df,
            "has_q_cashflow_df": self._has_q_cashflow_df,
            "has_q_earning_df": self._has_q_earning_df,
            "has_q_financial_df": self._has_q_financial_df
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def ActionDataFrame(self):
        return self._action_df

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
        return self._has_option_tuple

    @property
    def HasSplits(self):
        return self._has_split_series

    @property
    def HasActions(self):
        return self._has_action_df

    @property
    def HasBalanceSheet(self):
        return self._has_balance_sheet_df

    @property
    def HasQuarterBalanceSheet(self):
        return self._has_q_balance_sheet_df

    @property
    def HasQuarterCashflow(self):
        return self._has_q_cashflow_df

    @property
    def HasQuarterEarnings(self):
        return self._has_q_earning_df

    @property
    def HasQuarterFinancials(self):
        return self._has_q_financial_df
