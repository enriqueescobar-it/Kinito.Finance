import json
from datetime import datetime

import yfinance as yf
from pandas import DataFrame, Series
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo
from Common.InfoType.YahooFinanceStockInfo import YahooFinanceStockInfo
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
    _y_finance_si: YahooFinanceStockInfo
    _quarter_info: QuarterInfo
    _company_name: str = 'NA'
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
    _q_balance_sheet_df: DataFrame = DataFrame()
    _q_earning_df: DataFrame = DataFrame()
    _stock_type: AbstractStock

    def __init__(self, a_ticker: str = 'AAPL', past_years: int = 5):
        self.__ticker = a_ticker
        self.__y_finance = yf.Ticker(a_ticker)
        self._y_finance_si = YahooFinanceStockInfo(a_ticker)
        self._past_years = past_years
        self.__get_info()
        self._action_df = self._y_finance_si.ActionDf
        self._balance_sheet_df = self._y_finance_si.BalanceSheetDf
        self._option_tuple = self._y_finance_si.OptionTuple
        self._split_series = self._y_finance_si.SplitSeries
        self._q_balance_sheet_df = self._y_finance_si.QBalanceSheetDf
        self._q_cashflow_df = self._y_finance_si.QCashflowDf
        self._q_earning_df = self._y_finance_si.QEarningDf
        self._q_financial_df = self._y_finance_si.QFinancialDf

    def __get_info(self):
        self.__y_fin_dic = self._y_finance_si.InfoDict
        self._company_name = self._y_finance_si.Company
        self._url = self._y_finance_si.URL
        self._url_logo = self._y_finance_si.URLlogo
        self._address1 = self._y_finance_si.Address1
        self._address2 = self._y_finance_si.Address2
        self._city = self._y_finance_si.City
        self._postal_code = self._y_finance_si.PostalCode
        self._state = self._y_finance_si.State
        self._country = self._y_finance_si.Country
        self._phone = self._y_finance_si.Phone
        self._fax = self._y_finance_si.Fax
        self._market = self._y_finance_si.Market
        self._currency = self._y_finance_si.Currency
        self._quote_type = self._y_finance_si.QuoteType
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
        s: str = pt.__str__()
        if self._y_finance_si.HasOptionTuple:
            s += "\n\nOPTION TUPLE\n" + str(self._y_finance_si.OptionTuple)
        if self._y_finance_si.HasSplitSeries:
            s += "\n\nSPLIT SERIES\n" + self._y_finance_si.SplitSeries.to_string(index=True)
        if self._y_finance_si.HasActionDf:
            s += "\n\nACTION DATAFRAME\n" + self._y_finance_si.ActionDf.head().to_string(index=True)
        if self._y_finance_si.HasBalanceSheetDf:
            s += "\n\nBALANCE SHEET DATAFRAME\n\n" + self._y_finance_si.BalanceSheetDf.to_string(index=True)
        if self._y_finance_si.HasQBalanceSheetDf:
            s += "\n\nQUARTER BALANCE SHEET DATAFRAME\n" + self._q_balance_sheet_df.to_string(index=True)
        if self._y_finance_si.HasQCashflowDf:
            s += "\n\nQUARTER CASHFLOW DATAFRAME\n" + self._y_finance_si.QCashflowDf.to_string(index=True)
        if self._y_finance_si.HasQEarningDf:
            s += "\n\nQUARTER EARNING DATAFRAME\n" + self._q_earning_df.to_string(index=True)
        if self._y_finance_si.HasQFinancialDf:
            s += "\n\nQUARTER FINANCIAL DATAFRAME\n" + self._y_finance_si.QFinancialDf.to_string(index=True)
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
            "quote_type": self._quote_type
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def ActionDataFrame(self):
        return self._y_finance_si.ActionDf

    @property
    def BalanceSheetDataFrame(self):
        return self._y_finance_si.BalanceSheetDf

    @property
    def CompanyName(self):
        return self._company_name

    @property
    def OptionTuple(self):
        return self._y_finance_si.OptionTuple

    @property
    def QuarterBalanceSheetDataFrame(self):
        return self._q_balance_sheet_df

    @property
    def QuarterCashflowDataFrame(self):
        return self._y_finance_si.QCashflowDf

    @property
    def QuarterEarningDataFrame(self):
        return self._q_earning_df

    @property
    def QuarterFinancialDataFrame(self):
        return self._y_finance_si.QFinancialDf

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def SplitSeries(self):
        return self._y_finance_si.SplitSeries

    @property
    def StockType(self):
        return self._stock_type
