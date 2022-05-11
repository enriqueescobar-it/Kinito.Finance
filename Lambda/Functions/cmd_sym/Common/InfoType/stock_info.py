import json

import yfinance as yf
from pandas import DataFrame
from pandas import Series
from prettytable import PrettyTable

from Common.InfoType.abstract_info import abstract_info
from Common.StockType.AbstractStock import AbstractStock
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
    _quote_type: str = 'NA'
    _actions_df: DataFrame = DataFrame()
    _balance_sheet_df: DataFrame = DataFrame()
    _q_cashflow_df: DataFrame = DataFrame()
    _q_earning_df: DataFrame = DataFrame()
    _q_financial_df: DataFrame = DataFrame()
    _q_balance_sheet_df: DataFrame = DataFrame()
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

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self.__header
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['CompanyName', self._company_name])
        pt.add_row(['QuoteType', self._quote_type])
        return pt.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "company_name": self._company_name,
            "quote_type": self._quote_type
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def set_actions(self):
        if any(self.__yFinance.actions):
            self._actions_df = self.__yFinance.actions

    def set_splits(self):
        if any(self.__yFinance.splits):
            self._split_series = self.__yFinance.splits

    def __set_option_tuple(self):
        self._option_tuple = self.__yFinance.options

    def __get_info(self):
        if any(self.__yFinance.info):
            #print(self.__y_fin_dic)
            self.__y_fin_dic = self.__yFinance.info
            self._company_name = self.__get_str_from_key('shortName')
            self._quote_type = self.__get_str_from_key('quoteType')
            self.__get_stock_type(self._quote_type)

    def __set_balance_sheet(self):
        self._balance_sheet_df = self.__yFinance.balance_sheet

    def __set_quarterly_earnings(self):
        self._q_earning_df = self.__yFinance.quarterly_earnings

    def __set_quarterly_cashflow(self):
        self._q_cashflow_df = self.__yFinance.quarterly_cashflow

    def __set_quarterly_financials(self):
        self._q_financial_df = self.__yFinance.quarterly_financials

    def __set_quarterly_balance_sheet(self):
        self._q_balance_sheet_df = self.__yFinance.quarterly_balancesheet
        self._q_balance_sheet_df = self.__yFinance.quarterly_balance_sheet

    def __get_str_from_key(self, a_key: str = 'NA') -> str:
        if a_key in self.__y_fin_dic:
            return 'None' if self.__y_fin_dic[a_key] is None else self.__y_fin_dic[a_key]
        else:
            return 'NA'

    def __get_stock_type(self, s: str = ''):
        if s == 'ETF':
            self._stock_type = ExchangeTradedFund(self._company_name, self.__ticker)
        if s == 'INDEX':
            self._stock_type = IndexFund(self._company_name, self.__ticker)
        if s == 'MUTUALFUND':
            self._stock_type = MutualFund(self._company_name, self.__ticker)
        if s == 'CRYPTOCURRENCY':
            self._stock_type = CryptoCurrency(self._company_name, self.__ticker)
        if s == 'CURRENCY':
            self._stock_type = RegularCurrency(self._company_name, self.__ticker)
        if s == 'FUTURE':
            self._stock_type = AbstractStockFuture(self._company_name, self.__ticker)
        if s == 'EQUITY':
            self._stock_type = AbstractStockEquity(self._company_name, self.__ticker)
        #else:
        #    self._stock_type = AbstractStockOption(self.CompanyName, self.__ticker)
        #    self._stock_type = AbstractStockBond(self.CompanyName, self.__ticker)

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
