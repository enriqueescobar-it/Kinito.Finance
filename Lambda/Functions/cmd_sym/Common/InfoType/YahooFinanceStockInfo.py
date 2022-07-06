import json
import requests

import numpy as np
import yfinance as yf
from pandas import DataFrame, Series
from prettytable import PrettyTable
from requests import Response

from Common.InfoType.AbstractInfo import AbstractInfo


class YahooFinanceStockInfo(AbstractInfo):
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _y_finance: yf.ticker.Ticker
    _ticker: str = 'AAPL'
    _has_info_dict: bool = False
    _has_option_tuple: bool = False
    _has_split_series: bool = False
    _has_action_df: bool = False
    _has_balance_sheet_df: bool = False
    _has_q_balance_sheets_df: bool = False
    _has_q_cashflows_df: bool = False
    _has_q_earnings_df: bool = False
    _has_q_financials_df: bool = False
    _company_name: str = 'NA'
    _url: str = "http://localhost"
    _url_logo: str = "http://localhost"
    _address1: str = "NA"
    _address2: str = "NA"
    _city: str = "Montreal"
    _postal_code: str = "G1Q 1Q9"
    _state: str = "Quebec"
    _country: str = "Canada"
    _phone: str = "+1-514-343-1514"
    _fax: str = "+1-514-343-1514"
    _market: str = "TSX"
    _currency: str = "$"
    _quote_type: str = "Bond"
    _info_dict: dict = {}
    _option_tuple: tuple = tuple()
    _split_series: Series = Series()
    _action_df: DataFrame = DataFrame()
    _balance_sheet_df: DataFrame = DataFrame()
    _q_balance_sheets_df: DataFrame = DataFrame()
    _q_cashflows_df: DataFrame = DataFrame()
    _q_earnings_df: DataFrame = DataFrame()
    _q_financials_df: DataFrame = DataFrame()

    def __int__(self):
        self.__init__(self._ticker)

    def __init__(self, ticker: str):
        self._ticker = ticker
        self._y_finance = yf.Ticker(ticker)
        self._set_info_dict()
        self._set_balance_sheet_df()
        self._set_option_tuple()
        self._set_q_balance_sheet_df()
        self._set_q_cashflow_df()
        self._set_q_earning_df()
        self._set_q_financial_df()
        self._set_action_df()
        self._set_split_series()

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['Company', self._company_name])
        self._pretty_table.add_row(['URL', self._url])
        self._pretty_table.add_row(['URLlogo', self._url_logo])
        self._pretty_table.add_row(['Address1', self._address1])
        self._pretty_table.add_row(['Address2', self._address2])
        self._pretty_table.add_row(['City', self._city])
        self._pretty_table.add_row(['PostalCode', self._postal_code])
        self._pretty_table.add_row(['State', self._state])
        self._pretty_table.add_row(['Country', self._country])
        self._pretty_table.add_row(['Phone', self._phone])
        self._pretty_table.add_row(['Fax', self._fax])
        self._pretty_table.add_row(['Market', self._market])
        self._pretty_table.add_row(['Currency', self._currency])
        self._pretty_table.add_row(['QuoteType', self._quote_type])
        self._pretty_table.add_row(['HasInfoDict', self._has_info_dict])
        self._pretty_table.add_row(['HasOptionTuple', self._has_option_tuple])
        self._pretty_table.add_row(['HasSplitSeries', self._has_split_series])
        self._pretty_table.add_row(['HasActionDf', self._has_action_df])
        self._pretty_table.add_row(['HasBalanceSheetDf', self._has_balance_sheet_df])
        self._pretty_table.add_row(['HasQBalanceSheetDf', self._has_q_balance_sheets_df])
        self._pretty_table.add_row(['HasQCashflowDf', self._has_q_cashflows_df])
        self._pretty_table.add_row(['HasQEarningDf', self._has_q_earnings_df])
        self._pretty_table.add_row(['HasQFinancialDf', self._has_q_financials_df])
        return self._pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "ticker": self._ticker,
            "company_name": self._company_name,
            "url": self._url,
            "url_logo": self._url_logo,
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
            "has_info_dict": self._has_info_dict,
            "has_option_tuple": self._has_option_tuple,
            "has_split_series": self._has_split_series,
            "has_action_df": self._has_action_df,
            "has_balance_sheet_df": self._has_balance_sheet_df,
            "has_q_balance_sheet_df": self._has_q_balance_sheets_df,
            "has_q_cashflow_df": self._has_q_cashflows_df,
            "has_q_earning_df": self._has_q_earnings_df,
            "has_q_financial_df": self._has_q_financials_df
        }.items()

    def __is_df_valid(self, a_df: DataFrame) -> bool:
        return any(a_df) and isinstance(a_df, DataFrame) and not a_df.empty and\
               not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0

    def __url_exists(self, url_str: str) -> bool:
        boo: bool = False
        get_response: int = 0
        try:
            # Get Url
            get: Response = requests.get(url_str)
            get_response = get.status_code
            # if the request succeeds
            if get_response == 200:
                boo = True
                print(f"{url_str}: is reachable")
            else:
                boo = False
                print(f"{url_str}: is Not reachable, status_code: {get.status_code}")
        # Exception
        except requests.exceptions.RequestException as e:
            # print URL with Errs
            raise SystemExit(f"{url_str}: is Not reachable \nErr: {e}")
        finally:
            print('FINALLY', get_response, boo)
        return boo

    def __get_str_from_key(self, a_dict: dict, a_key: str = 'NA') -> str:
        if a_key in a_dict:
            return 'None' if a_dict[a_key] is None else a_dict[a_key]
        else:
            return 'NA'

    def __set_info_dict(self):
        self._info_dict = self._y_finance.info
        self._company_name = self.__get_str_from_key(self._info_dict, 'shortName')
        a_str: str = self.__get_str_from_key(self._info_dict, 'website')
        if self.__url_exists(a_str):
            self._url = a_str
        a_str = self.__get_str_from_key(self._info_dict, 'logo_url')
        if self.__url_exists(a_str):
            self._url_logo = a_str
        self._address1 = self.__get_str_from_key(self._info_dict, 'address1')
        self._address2 = self.__get_str_from_key(self._info_dict, 'address2')
        self._city = self.__get_str_from_key(self._info_dict, 'city')
        self._postal_code = self.__get_str_from_key(self._info_dict, 'zip')
        self._state = self.__get_str_from_key(self._info_dict, 'state')
        self._country = self.__get_str_from_key(self._info_dict, 'country')
        self._phone = self.__get_str_from_key(self._info_dict, 'phone')
        self._fax = self.__get_str_from_key(self._info_dict, 'fax')
        self._market = self.__get_str_from_key(self._info_dict, 'market')
        self._currency = self.__get_str_from_key(self._info_dict, 'currency')
        self._quote_type = self.__get_str_from_key(self._info_dict, 'quoteType')

    def _set_info_dict(self):
        self._has_info_dict = ('_info' in self._y_finance.__dict__) or hasattr(self._y_finance, '_info') or\
                              any(self._y_finance.info) and isinstance(self._y_finance.info, dict)
        if self._has_info_dict:
            self.__set_info_dict()

    def _set_balance_sheet_df(self):
        self._has_balance_sheet_df = ('_balance_sheet' in self._y_finance.__dict__) or\
                                     hasattr(self._y_finance, '_balance_sheet') or\
                                     self.__is_df_valid(self._y_finance.balance_sheet)
        if self._has_balance_sheet_df:
            self._balance_sheet_df = self._y_finance.balance_sheet.fillna(value=np.nan, inplace=False)

    def _set_option_tuple(self):
        self._has_option_tuple = ('_options' in self._y_finance.__dict__) or hasattr(self._y_finance, '_options') or\
                                    any(self._y_finance.options) and isinstance(self._y_finance.options, tuple)
        if self._has_option_tuple:
            self._option_tuple = self._y_finance.options

    def _set_q_balance_sheet_df(self):
        self._has_q_balance_sheets_df = ('_quarterly_balancesheet' in self._y_finance.__dict__) and \
                                        hasattr(self._y_finance, '_quarterly_balancesheet') or \
                                        ('_quarterly_balance_sheet' in self._y_finance.__dict__) and \
                                        hasattr(self._y_finance, '_quarterly_balance_sheet') or \
                                        self.__is_df_valid(self._y_finance.quarterly_balance_sheet) and \
                                        self.__is_df_valid(self._y_finance.quarterly_balancesheet)
        if self._has_q_balance_sheets_df:
            self._q_balance_sheets_df = self._y_finance.quarterly_balance_sheet.fillna(value=np.nan, inplace=False)
            self._q_balance_sheets_df = self._y_finance.quarterly_balancesheet.fillna(value=np.nan, inplace=False)

    def _set_q_cashflow_df(self):
        self._has_q_cashflows_df = ('_quarterly_cashflow' in self._y_finance.__dict__) and \
                                   hasattr(self._y_finance, '_quarterly_cashflow') and \
                                   self.__is_df_valid(self._y_finance.quarterly_cashflow)
        if self._has_q_cashflows_df:
            self._q_cashflows_df = self._y_finance.quarterly_cashflow.fillna(value=np.nan, inplace=False)

    def _set_q_earning_df(self):
        self._has_q_earnings_df = ('_quarterly_earnings' in self._y_finance.__dict__) and \
                                  hasattr(self._y_finance, '_quarterly_earnings') and \
                                  self.__is_df_valid(self._y_finance.quarterly_earnings)
        if self._has_q_earnings_df:
            self._q_earnings_df = self._y_finance.quarterly_earnings.fillna(value=np.nan, inplace=False)

    def _set_q_financial_df(self):
        self._has_q_financials_df = ('_quarterly_financials' in self._y_finance.__dict__) and \
                                    hasattr(self._y_finance, '_quarterly_financials') and \
                                    self.__is_df_valid(self._y_finance.quarterly_financials)
        if self._has_q_financials_df:
            self._q_financials_df = self._y_finance.quarterly_financials.fillna(value=np.nan, inplace=False)

    def _set_action_df(self):
        self._has_action_df = self.__is_df_valid(self._y_finance.actions)
        if self._has_action_df:
            self._action_df = self._y_finance.actions.fillna(value=np.nan, inplace=False)

    def _set_split_series(self):
        self._has_split_series = any(self._y_finance.splits) and isinstance(self._y_finance.splits, Series)
        if self._has_split_series:
            self._split_series = self._y_finance.splits.fillna(value=np.nan, inplace=False)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def Ticker(self):
        return self._ticker

    @property
    def Company(self):
        return self._company_name

    @property
    def URL(self):
        return self._url

    @property
    def URLlogo(self):
        return self._url_logo

    @property
    def Address1(self):
        return self._address1

    @property
    def Address2(self):
        return self._address2

    @property
    def City(self):
        return self._city

    @property
    def PostalCode(self):
        return self._postal_code

    @property
    def State(self):
        return self._state

    @property
    def Country(self):
        return self._country

    @property
    def Phone(self):
        return self._phone

    @property
    def Fax(self):
        return self._fax

    @property
    def Market(self):
        return self._market

    @property
    def Currency(self):
        return self._currency

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def HasInfoDict(self):
        return self._has_info_dict

    @property
    def InfoDict(self):
        return self._info_dict

    @property
    def HasOptionTuple(self):
        return self._has_option_tuple

    @property
    def OptionTuple(self):
        return self._option_tuple

    @property
    def HasSplitSeries(self):
        return self._has_split_series

    @property
    def SplitSeries(self):
        return self._split_series

    @property
    def HasActionDf(self):
        return self._has_action_df

    @property
    def ActionDf(self):
        return self._action_df

    @property
    def HasBalanceSheetDf(self):
        return self._has_balance_sheet_df

    @property
    def BalanceSheetDf(self):
        return self._balance_sheet_df

    @property
    def HasQBalanceSheesDf(self):
        return self._has_q_balance_sheets_df

    @property
    def QBalanceSheetsDf(self):
        return self._q_balance_sheets_df

    @property
    def HasQCashflowsDf(self):
        return self._has_q_cashflows_df

    @property
    def QCashflowsDf(self):
        return self._q_cashflows_df

    @property
    def HasQEarningsDf(self):
        return self._has_q_earnings_df

    @property
    def QEarningsDf(self):
        return self._q_earnings_df

    @property
    def HasQFinancialsDf(self):
        return self._has_q_financials_df

    @property
    def QFinancialsDf(self):
        return self._q_financials_df
