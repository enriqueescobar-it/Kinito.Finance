import json

import numpy as np
import yahoo_fin.stock_info as si
from pandas import DataFrame
from prettytable import PrettyTable

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinEngine(AbstractEngine):
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _df: DataFrame = DataFrame()
    _ticker: str = 'CNI'
    _days_range_low: float = np.nan
    _days_range_high: float = np.nan
    _year_range_low: float = np.nan
    _year_range_high: float = np.nan
    _settlement_pre: str = 'NA'
    _settlement_date: str = 'NA'
    _start_date: str = 'NA'
    _market_cap: str = 'NA'
    _algorithm: str = 'NA'
    _supply_circulating: str = 'NA'
    _supply_max: str = 'NA'
    _inception_date: str = 'NA'
    _beta_5y_monthly: str = 'NA'
    _ratio_pe: float = np.nan
    _ratio_fpe: float = np.nan
    _ratio_peg: float = np.nan
    _price_to_book: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sales: float = np.nan

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self._set_quote_dict(si.get_quote_table(a_ticker))
        '''
        self._df = si.get_stats_valuation(a_ticker)
        self._df = self._df.iloc[:, :2]
        self._df.columns = ['Attribute', 'Recent']
        self._ratio_pe = float(self._df[self._df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._ratio_fpe = float(self._df[self._df.Attribute.str.contains('Forward P/E')].iloc[0, 1])
        self._ratio_peg = float(self._df[self._df.Attribute.str.contains('PEG')].iloc[0, 1])
        self._price_to_book = float(self._df[self._df.Attribute.str.contains('Price/Book')].iloc[0, 1])
        self._price_to_earn = float(self._df[self._df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._price_to_sales = float(self._df[self._df.Attribute.str.contains('Price/Sales')].iloc[0, 1])
        '''

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['DaysRangeLow', self._days_range_low])
        self._pretty_table.add_row(['DaysRangeHigh', self._days_range_high])
        self._pretty_table.add_row(['YearRangeLow', self._year_range_low])
        self._pretty_table.add_row(['YearRangeHigh', self._year_range_high])
        self._pretty_table.add_row(['SettlementPre', self._settlement_pre])
        self._pretty_table.add_row(['SettlementDate', self._settlement_date])
        self._pretty_table.add_row(['StartDate', self._start_date])
        self._pretty_table.add_row(['MarketCap', self._market_cap])
        self._pretty_table.add_row(['Algorithm', self._algorithm])
        self._pretty_table.add_row(['CirculatingSupply', self._supply_circulating])
        self._pretty_table.add_row(['MaxSupply', self._supply_max])
        self._pretty_table.add_row(['InceptionDate', self._inception_date])
        self._pretty_table.add_row(['Beta5yMonthly', self._beta_5y_monthly])
        self._pretty_table.add_row(['RatioPE', self._ratio_pe])
        self._pretty_table.add_row(['RatioFPE', self._ratio_fpe])
        self._pretty_table.add_row(['RatioPEG', self._ratio_peg])
        self._pretty_table.add_row(['PriceToBook', self._price_to_book])
        self._pretty_table.add_row(['PriceToEarnings', self._price_to_earn])
        self._pretty_table.add_row(['PriceToSales', self._price_to_sales])
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "ticker": self._ticker,
            "days_range_low": self._days_range_low,
            "days_range_high": self._days_range_high,
            "year_range_low": self._year_range_low,
            "year_range_high": self._year_range_high,
            "settlement_pre": self._settlement_pre,
            "settlement_date": self._settlement_date,
            "start_date": self._start_date,
            "market_cap": self._market_cap,
            "algorithm": self._algorithm,
            "supply_circulating": self._supply_circulating,
            "supply_max": self._supply_max,
            "inception_date": self._inception_date,
            "beta_5y_monthly": self._beta_5y_monthly,
            "ratio_pe": self._ratio_pe,
            "ratio_fpe": self._ratio_fpe,
            "ratio_peg": self._ratio_peg,
            "price_to_book": self._price_to_book,
            "price_to_earn": self._price_to_earn,
            "price_to_sales": self._price_to_sales
        }.items()

    def __split_range(self, range_str: str = "0.0 - 0.0") -> tuple:
        str_list: list = range_str.replace(',', '').split(" - ")
        return str_list[0], str_list[1]

    def _set_key_in_range(self, str_key: str, quote_dict: dict) -> tuple:
        str_tuple: tuple = ("0.0", "0.0")
        if isinstance(quote_dict, dict) and any(quote_dict) and str_key in quote_dict.keys():
            str_tuple = self.__split_range(quote_dict[str_key])
        return str_tuple

    def _set_quote_dict(self, quote_dict: dict) -> None:
        self._set_days_in_range(quote_dict)
        self._set_years_in_range(quote_dict)
        self._set_settlement_pre(quote_dict)
        self._set_settlement_date(quote_dict)
        self._set_market_cap(quote_dict)
        self._set_start_date(quote_dict)
        self._set_algorithm(quote_dict)
        self._set_supply_circulating(quote_dict)
        self._set_supply_max(quote_dict)
        self._set_inception_date(quote_dict)
        self._set_beta_5y_monthly(quote_dict)
        print(quote_dict)

    def _set_days_in_range(self, quote_dict: dict) -> None:
        str_tuple: tuple = self._set_key_in_range("Day's Range", quote_dict)
        self._days_range_low = float("{:.3f}".format(float(str_tuple[0])))
        self._days_range_high = float("{:.3f}".format(float(str_tuple[1])))

    def _set_years_in_range(self, quote_dict: dict) -> None:
        str_tuple: tuple = self._set_key_in_range('52 Week Range', quote_dict)
        self._year_range_low = float("{:.3f}".format(float(str_tuple[0])))
        self._year_range_high = float("{:.3f}".format(float(str_tuple[1])))

    def __get_str_from_dict(self, str_key: str, quote_dict: dict) -> str:
        a_str: str = 'NA'
        if isinstance(quote_dict, dict) and any(quote_dict) and str_key in quote_dict.keys():
            #print(type(quote_dict[str_key]), quote_dict[str_key])
            a_str = quote_dict[str_key]
        return a_str

    def _set_settlement_pre(self, quote_dict: dict) -> None:
        str_key: str = 'Pre. Settlement'
        self._settlement_pre = self.__get_str_from_dict(str_key, quote_dict)

    def _set_settlement_date(self, quote_dict: dict) -> None:
        str_key: str = 'Settlement Date'
        self._settlement_date = self.__get_str_from_dict(str_key, quote_dict)

    def _set_start_date(self, quote_dict: dict) -> None:
        str_key: str = 'Start Date'
        self._start_date = self.__get_str_from_dict(str_key, quote_dict)

    def _set_market_cap(self, quote_dict: dict) -> None:
        str_key: str = 'Market Cap'
        self._market_cap = self.__get_str_from_dict(str_key, quote_dict)

    def _set_algorithm(self, quote_dict: dict) -> None:
        str_key: str = 'Algorithm'
        self._algorithm = self.__get_str_from_dict(str_key, quote_dict)

    def _set_supply_circulating(self, quote_dict: dict) -> None:
        str_key: str = 'Circulating Supply'
        self._supply_circulating = self.__get_str_from_dict(str_key, quote_dict)

    def _set_supply_max(self, quote_dict: dict) -> None:
        str_key: str = 'Max Supply'
        self._supply_max = self.__get_str_from_dict(str_key, quote_dict)

    def _set_inception_date(self, quote_dict):
        str_key: str = 'Inception Date'
        self._inception_date = self.__get_str_from_dict(str_key, quote_dict)

    def _set_beta_5y_monthly(self, quote_dict):
        str_key: str = 'Beta (5Y Monthly)'
        self._beta_5y_monthly = self.__get_str_from_dict(str_key, quote_dict)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def price_to_book(self):
        return self._price_to_book

    @property
    def price_to_earnings(self):
        return self._price_to_earn

    @property
    def price_to_sales(self):
        return self._price_to_sales
