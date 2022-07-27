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
    _category: str = 'NA'
    _category_mean: str = 'NA'
    _holdings_turnover: str = 'NA'
    _days_range_low: float = np.nan
    _days_range_high: float = np.nan
    _year_range_low: float = np.nan
    _year_range_high: float = np.nan
    _year_target_estimate: float = np.nan
    _settlement_pre: str = 'NA'
    _settlement_date: str = 'NA'
    _earnings_date: str = 'NA'
    _start_date: str = 'NA'
    _market_cap: str = 'NA'
    _eps: str = 'NA'
    _net_assets: str = 'NA'
    _nav: str = 'NA'
    _algorithm: str = 'NA'
    _supply_circulating: str = 'NA'
    _supply_max: str = 'NA'
    _date_inception: str = 'NA'
    _beta_5y_monthly: str = 'NA'
    _dividend_last: str = 'NA'
    _cap_gain_last: str = 'NA'
    _yield: str = 'NA'
    _daily_total_return_ytd: str = 'NA'
    _return_ytd: str = 'NA'
    _return_mean_5y: str = 'NA'
    _ratio_expense_net: str = 'NA'
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
        self._pretty_table.add_row(['Category', self._category])
        self._pretty_table.add_row(['CategoryMean', self._category_mean])
        self._pretty_table.add_row(['HoldingsTurnover', self._holdings_turnover])
        self._pretty_table.add_row(['DaysRangeLow', self._days_range_low])
        self._pretty_table.add_row(['DaysRangeHigh', self._days_range_high])
        self._pretty_table.add_row(['YearRangeLow', self._year_range_low])
        self._pretty_table.add_row(['YearRangeHigh', self._year_range_high])
        self._pretty_table.add_row(['YearTargetEstimate', self._year_target_estimate])
        self._pretty_table.add_row(['SettlementPre', self._settlement_pre])
        self._pretty_table.add_row(['SettlementDate', self._settlement_date])
        self._pretty_table.add_row(['EarningsDate', self._earnings_date])
        self._pretty_table.add_row(['LastDividend', self._dividend_last])
        self._pretty_table.add_row(['LastCapGain', self._cap_gain_last])
        self._pretty_table.add_row(['StartDate', self._start_date])
        self._pretty_table.add_row(['MarketCap', self._market_cap])
        self._pretty_table.add_row(['EarningsPerShare', self._eps])
        self._pretty_table.add_row(['NetAssets', self._net_assets])
        self._pretty_table.add_row(['NAV', self._nav])
        self._pretty_table.add_row(['Algorithm', self._algorithm])
        self._pretty_table.add_row(['SupplyCirculating', self._supply_circulating])
        self._pretty_table.add_row(['SupplyMax', self._supply_max])
        self._pretty_table.add_row(['DateInception', self._date_inception])
        self._pretty_table.add_row(['Beta5yMonthly', self._beta_5y_monthly])
        self._pretty_table.add_row(['Yield', self._yield])
        self._pretty_table.add_row(['DailyTotalReturnYTD', self._daily_total_return_ytd])
        self._pretty_table.add_row(['ReturnYTD', self._return_ytd])
        self._pretty_table.add_row(['ReturnMean5Y', self._return_mean_5y])
        self._pretty_table.add_row(['RatioExpenseNet', self._ratio_expense_net])
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
            "category": self._category,
            "category_mean": self._category_mean,
            "holdings_turnover": self._holdings_turnover,
            "days_range_low": self._days_range_low,
            "days_range_high": self._days_range_high,
            "year_range_low": self._year_range_low,
            "year_range_high": self._year_range_high,
            "year_target_estimate": self._year_target_estimate,
            "settlement_pre": self._settlement_pre,
            "settlement_date": self._settlement_date,
            "dividend_last": self._dividend_last,
            "cap_gain_last": self._cap_gain_last,
            "earnings_date": self._earnings_date,
            "start_date": self._start_date,
            "market_cap": self._market_cap,
            "eps": self._eps,
            "net_assets": self._net_assets,
            "nav": self._nav,
            "algorithm": self._algorithm,
            "supply_circulating": self._supply_circulating,
            "supply_max": self._supply_max,
            "date_inception": self._date_inception,
            "beta_5y_monthly": self._beta_5y_monthly,
            "yield": self._yield,
            "daily_total_return_ytd": self._daily_total_return_ytd,
            "return_ytd": self._return_ytd,
            "return_mean_5y": self._return_mean_5y,
            "ratio_expense_net": self._ratio_expense_net,
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
        self.__set_category(quote_dict)
        self.__set_category_mean(quote_dict)
        self.__set_holdings_turnover(quote_dict)
        self.__set_days_in_range(quote_dict)
        self.__set_years_in_range(quote_dict)
        self.__set_year_target_estimate(quote_dict)
        self.__set_settlement_pre(quote_dict)
        self.__set_settlement_date(quote_dict)
        self.__set_earnings_date(quote_dict)
        self.__set_dividend_last(quote_dict)
        self.__set_cap_gain_last(quote_dict)
        self.__set_market_cap(quote_dict)
        self.__set_eps(quote_dict)
        self.__set_net_assets(quote_dict)
        self.__set_nav(quote_dict)
        self.__set_start_date(quote_dict)
        self.__set_algorithm(quote_dict)
        self.__set_supply_circulating(quote_dict)
        self.__set_supply_max(quote_dict)
        self.__set_inception_date(quote_dict)
        self.__set_beta_5y_monthly(quote_dict)
        self.__set_return_ytd(quote_dict)
        self.__set_yield(quote_dict)
        self.__set_ratio_expense_net(quote_dict)
        self.__set_daily_total_return_ytd(quote_dict)
        self.__set_return_mean_5y(quote_dict)
        self.__set_ratio_pe(quote_dict)
        print(quote_dict)

    def __set_days_in_range(self, quote_dict: dict) -> None:
        str_tuple: tuple = self._set_key_in_range("Day's Range", quote_dict)
        self._days_range_low = float("{:.3f}".format(float(str_tuple[0])))
        self._days_range_high = float("{:.3f}".format(float(str_tuple[1])))

    def __set_years_in_range(self, quote_dict: dict) -> None:
        str_tuple: tuple = self._set_key_in_range('52 Week Range', quote_dict)
        self._year_range_low = float("{:.3f}".format(float(str_tuple[0])))
        self._year_range_high = float("{:.3f}".format(float(str_tuple[1])))

    def __get_str_from_dict(self, str_key: str, quote_dict: dict) -> str:
        a_str: str = 'NA'
        if isinstance(quote_dict, dict) and any(quote_dict) and str_key in quote_dict.keys():
            print('???', type(quote_dict[str_key]), quote_dict[str_key])
            if not isinstance(quote_dict[str_key], str):
                a_str = str(quote_dict[str_key])
            else:
                a_str = quote_dict[str_key]
        return a_str

    def __set_year_target_estimate(self, quote_dict: dict) -> None:
        str_key: str = '1y Target Est'
        self._year_target_estimate = np.nan
        if not self.__get_str_from_dict(str_key, quote_dict) == 'NA':
            self._year_target_estimate = float("{:.3f}".format(float(self.__get_str_from_dict(str_key, quote_dict))))

    def __set_category(self, quote_dict: dict) -> None:
        str_key: str = 'Category'
        self._category = self.__get_str_from_dict(str_key, quote_dict)

    def __set_category_mean(self, quote_dict: dict) -> None:
        str_key: str = 'Average for Category'
        self._category_mean = self.__get_str_from_dict(str_key, quote_dict)

    def __set_holdings_turnover(self, quote_dict: dict) -> None:
        str_key: str = 'Holdings Turnover'
        self._holdings_turnover = self.__get_str_from_dict(str_key, quote_dict)

    def __set_settlement_pre(self, quote_dict: dict) -> None:
        str_key: str = 'Pre. Settlement'
        self._settlement_pre = self.__get_str_from_dict(str_key, quote_dict)

    def __set_settlement_date(self, quote_dict: dict) -> None:
        str_key: str = 'Settlement Date'
        self._settlement_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_earnings_date(self, quote_dict: dict) -> None:
        str_key: str = 'Earnings Date'
        self._earnings_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_dividend_last(self, quote_dict: dict) -> None:
        str_key: str = 'Last Dividend'
        self._dividend_last = self.__get_str_from_dict(str_key, quote_dict)

    def __set_cap_gain_last(self, quote_dict: dict) -> None:
        str_key: str = 'Last Cap Gain'
        self._cap_gain_last = self.__get_str_from_dict(str_key, quote_dict)

    def __set_start_date(self, quote_dict: dict) -> None:
        str_key: str = 'Start Date'
        self._start_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_market_cap(self, quote_dict: dict) -> None:
        str_key: str = 'Market Cap'
        self._market_cap = self.__get_str_from_dict(str_key, quote_dict)

    def __set_eps(self, quote_dict: dict) -> None:
        str_key: str = 'EPS (TTM)'
        self._eps = self.__get_str_from_dict(str_key, quote_dict)

    def __set_net_assets(self, quote_dict: dict) -> None:
        str_key: str = 'Net Assets'
        self._net_assets = self.__get_str_from_dict(str_key, quote_dict)

    def __set_nav(self, quote_dict: dict) -> None:
        str_key: str = 'NAV'
        self._nav = self.__get_str_from_dict(str_key, quote_dict)

    def __set_algorithm(self, quote_dict: dict) -> None:
        str_key: str = 'Algorithm'
        self._algorithm = self.__get_str_from_dict(str_key, quote_dict)

    def __set_supply_circulating(self, quote_dict: dict) -> None:
        str_key: str = 'Circulating Supply'
        self._supply_circulating = self.__get_str_from_dict(str_key, quote_dict)

    def __set_supply_max(self, quote_dict: dict) -> None:
        str_key: str = 'Max Supply'
        self._supply_max = self.__get_str_from_dict(str_key, quote_dict)

    def __set_inception_date(self, quote_dict: dict) -> None:
        str_key: str = 'Inception Date'
        self._date_inception = self.__get_str_from_dict(str_key, quote_dict)

    def __set_beta_5y_monthly(self, quote_dict: dict) -> None:
        str_key: str = 'Beta (5Y Monthly)'
        self._beta_5y_monthly = self.__get_str_from_dict(str_key, quote_dict)

    def __set_yield(self, quote_dict: dict) -> None:
        str_key: str = 'Yield'
        self._yield = self.__get_str_from_dict(str_key, quote_dict)

    def __set_daily_total_return_ytd(self, quote_dict: dict) -> None:
        str_key: str = 'YTD Daily Total Return'
        self._daily_total_return_ytd = self.__get_str_from_dict(str_key, quote_dict)

    def __set_return_ytd(self, quote_dict: dict) -> None:
        str_key: str = 'YTD Return'
        self._return_ytd = self.__get_str_from_dict(str_key, quote_dict)

    def __set_return_mean_5y(self, quote_dict: dict) -> None:
        str_key: str = '5y Average Return'
        self._return_mean_5y = self.__get_str_from_dict(str_key, quote_dict)

    def __set_ratio_expense_net(self, quote_dict: dict) -> None:
        str_key: str = 'Expense Ratio (net)'
        self._ratio_expense_net = self.__get_str_from_dict(str_key, quote_dict)

    def __set_ratio_pe(self, quote_dict: dict) -> None:
        str_key: str = 'PE Ratio (TTM)'
        s: str = self.__get_str_from_dict(str_key, quote_dict)
        self._ratio_pe = 0.0 if s == 'NA' else float("{:.3f}".format(float(s)))

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
