import json
from datetime import datetime

import numpy as np
import yahoo_fin.stock_info as si
from pandas import DataFrame
from prettytable import PrettyTable

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinEngine(AbstractEngine):
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _ticker: str = 'CNI'
    _category: str = 'NA'
    _category_mean: float = np.nan
    _holdings_turnover_pcnt: float = np.nan
    _days_range_low: float = np.nan
    _days_range_high: float = np.nan
    _year_range_low: float = np.nan
    _year_range_high: float = np.nan
    _year_target_estimate: float = np.nan
    _settlement_pre: str = 'NA'
    _settlement_date: str = 'NA'
    _earnings_date: str = 'NA'
    _dividend_date: str = 'NA'
    _ex_dividend_date: datetime = datetime(2001, 9, 11)
    _start_date: str = 'NA'
    _market_cap: str = 'NA'
    _eps: float = np.nan
    _net_assets: str = 'NA'
    _nav: float = np.nan
    _algorithm: str = 'NA'
    _supply_circulating: str = 'NA'
    _supply_max: str = 'NA'
    _date_inception: str = 'NA'
    _beta_5y_monthly: float = np.nan
    _dividend_forward: float = np.nan
    _dividend_last: float = np.nan
    _cap_gain_last: float = np.nan
    _yield_pcnt: float = np.nan
    _daily_total_return_ytd: str = 'NA'
    _return_ytd_pcnt: float = np.nan
    _return_mean_5y: float = np.nan
    _ratio_expense_net_pcnt: float = np.nan
    _ratio_pe: float = np.nan
    _ratio_fpe: float = np.nan
    _ratio_peg: float = np.nan
    _ratio_payout_pcnt: float = np.nan
    _ratio_ent_value_revenue: float = np.nan
    _ratio_ent_value_ebitda: float = np.nan
    _ebitda: str = 'NA'
    _profit_margin_pcnt: float = np.nan
    _enterprise_value: str = 'NA'
    _price_to_book: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sales: float = np.nan

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self._set_quote_dict(si.get_quote_table(a_ticker))
        try:
            print('Exception: get_stats_valuation(', a_ticker, ')')
            self._get_stats_valuation(a_ticker)
            self._get_stats(a_ticker)
        except IndexError as e:
            print('Exception: get_stats_valuation(', a_ticker, '):', e)
        finally:
            print('Finally')
        # combined_extra_stats[combined_extra_stats.Attribute.str.contains("Return on Equity")]
        # combined_extra_stats[combined_extra_stats.Attribute.str.contains("Return on Assets")]
        # combined_extra_stats[combined_extra_stats.Attribute.str.contains("Profit Margin")]
        print(si.get_stats(a_ticker))
        # ***
        # sheet.loc["cash"]
        # sheet.loc["totalStockholderEquity"]
        # sheet.loc["totalAssets"]
        # combined_sheets[combined_sheets.Breakdown == "totalAssets"]
        #print(si.get_balance_sheet(a_ticker))
        # ***
        # income.loc["totalRevenue"]
        # income.loc["grossProfit"]
        # combined_income[combined_income.Breakdown == "totalRevenue"]
        #print(si.get_income_statement(a_ticker))
        # ***
        # combined_cash_flows[combined_cash_flows.Breakdown == "dividendsPaid"]
        # combined_cash_flows[combined_cash_flows.Breakdown == "issuanceOfStock"]
        #print(si.get_cash_flow(a_ticker))

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['Category', self._category])
        self._pretty_table.add_row(['CategoryMean', self._category_mean])
        self._pretty_table.add_row(['HoldingsTurnover', self._holdings_turnover_pcnt])
        self._pretty_table.add_row(['DaysRangeLow', self._days_range_low])
        self._pretty_table.add_row(['DaysRangeHigh', self._days_range_high])
        self._pretty_table.add_row(['YearRangeLow', self._year_range_low])
        self._pretty_table.add_row(['YearRangeHigh', self._year_range_high])
        self._pretty_table.add_row(['YearTargetEstimate', self._year_target_estimate])
        self._pretty_table.add_row(['SettlementPre', self._settlement_pre])
        self._pretty_table.add_row(['SettlementDate', self._settlement_date])
        self._pretty_table.add_row(['EarningsDate', self._earnings_date])
        self._pretty_table.add_row(['DividendDate', self._dividend_date])
        self._pretty_table.add_row(['ExDividendDate', self._ex_dividend_date])
        self._pretty_table.add_row(['ForwardDividend', self._dividend_forward])
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
        self._pretty_table.add_row(['Yield', self._yield_pcnt])
        self._pretty_table.add_row(['DailyTotalReturnYTD', self._daily_total_return_ytd])
        self._pretty_table.add_row(['ReturnYTD', self._return_ytd_pcnt])
        self._pretty_table.add_row(['ReturnMean5Y', self._return_mean_5y])
        self._pretty_table.add_row(['RatioExpenseNet', self._ratio_expense_net_pcnt])
        self._pretty_table.add_row(['RatioPE', self._ratio_pe])
        self._pretty_table.add_row(['RatioFPE', self._ratio_fpe])
        self._pretty_table.add_row(['RatioPEG', self._ratio_peg])
        self._pretty_table.add_row(['RatioPayout', self._ratio_payout_pcnt])
        self._pretty_table.add_row(['RatioEnterpriseValueRevenue', self._ratio_ent_value_revenue])
        self._pretty_table.add_row(['RatioEnterpriseValueEBITDA', self._ratio_ent_value_ebitda])
        self._pretty_table.add_row(['EBITDA', self._ebitda])
        self._pretty_table.add_row(['ProfitMargin', self._profit_margin_pcnt])
        self._pretty_table.add_row(['EnterpriseValue', self._enterprise_value])
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
            "holdings_turnover": self._holdings_turnover_pcnt,
            "days_range_low": self._days_range_low,
            "days_range_high": self._days_range_high,
            "year_range_low": self._year_range_low,
            "year_range_high": self._year_range_high,
            "year_target_estimate": self._year_target_estimate,
            "settlement_pre": self._settlement_pre,
            "settlement_date": self._settlement_date,
            "dividend_forward": self._dividend_forward,
            "dividend_last": self._dividend_last,
            "dividend_date": self._dividend_date,
            "ex_dividend_date": str(self._ex_dividend_date),
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
            "yield": self._yield_pcnt,
            "daily_total_return_ytd": self._daily_total_return_ytd,
            "return_ytd": self._return_ytd_pcnt,
            "return_mean_5y": self._return_mean_5y,
            "ratio_expense_net": self._ratio_expense_net_pcnt,
            "ratio_pe": self._ratio_pe,
            "ratio_fpe": self._ratio_fpe,
            "ratio_peg": self._ratio_peg,
            "ratio_payout": self._ratio_payout_pcnt,
            "ratio_ent_value_revenue": self._ratio_ent_value_revenue,
            "ratio_ent_value_ebitda": self._ratio_ent_value_ebitda,
            "ebitda": self._ebitda,
            "profit_margin": self._profit_margin_pcnt,
            "enterprise_value": self._enterprise_value,
            "price_to_book": self._price_to_book,
            "price_to_earn": self._price_to_earn,
            "price_to_sales": self._price_to_sales
        }.items()

    def __split_range(self, range_str: str = "0.0 - 0.0") -> tuple:
        s: str = range_str if isinstance(range_str, str) else 'nan - nan'
        str_list: list = s.replace(',', '').split(" - ")
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
        self.__set_ex_dividend_date(quote_dict)
        self.__set_dividend_forward(quote_dict)
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

    def __get_percent_from_str(self, a_str: str = 'NA') -> float:
        a_float: float = np.nan
        print('%%%', a_str)
        if '%' in a_str:
            a_float = round((float(a_str.strip('%')) / 100), 5)
        return a_float

    def __get_str_from_dict(self, str_key: str, quote_dict: dict) -> str:
        a_str: str = 'NA'
        if isinstance(quote_dict, dict) and any(quote_dict) and str_key in quote_dict.keys():
            print('???', str_key, type(quote_dict[str_key]), quote_dict[str_key])
            if isinstance(quote_dict[str_key], float):
                a_float: float = float("{:.3f}".format(float(quote_dict[str_key])))
                a_str = str(a_float)
            elif isinstance(quote_dict[str_key], str) and ('%' in quote_dict[str_key]):
                quote_dict_key: str = quote_dict[str_key]
                print('%%%', str_key, type(quote_dict_key), quote_dict_key)
                #a_str = str(round((float(quote_dict_key.strip('%')) / 100), 5))
                if not(' (' in quote_dict_key):
                    print('```_', str_key, type(quote_dict_key), quote_dict_key)
                    a_str = str(self.__get_percent_from_str(quote_dict_key))
                else:
                    print('```+', str_key, type(quote_dict_key), quote_dict_key)
                    a_str = quote_dict_key
            #if not isinstance(quote_dict[str_key], str):
            #    a_str = str(quote_dict[str_key])
            else:
            #    a_str = quote_dict[str_key]
                a_str = str(quote_dict[str_key])
        return a_str

    def __set_year_target_estimate(self, quote_dict: dict) -> None:
        str_key: str = '1y Target Est'
        self._year_target_estimate = np.nan
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if not key_from_quote_dict == 'NA':
            self._year_target_estimate = float("{:.3f}".format(float(key_from_quote_dict)))

    def __set_category(self, quote_dict: dict) -> None:
        str_key: str = 'Category'
        self._category = self.__get_str_from_dict(str_key, quote_dict)

    def __set_category_mean(self, quote_dict: dict) -> None:
        str_key: str = 'Average for Category'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._category_mean = float(key_from_quote_dict)

    def __set_holdings_turnover(self, quote_dict: dict) -> None:
        str_key: str = 'Holdings Turnover'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        self._holdings_turnover_pcnt = self.__get_percent_from_str(key_from_quote_dict)
        #    float(key_from_quote_dict) if key_from_quote_dict != 'NA' else np.nan

    def __set_settlement_pre(self, quote_dict: dict) -> None:
        str_key: str = 'Pre. Settlement'
        self._settlement_pre = self.__get_str_from_dict(str_key, quote_dict)

    def __set_settlement_date(self, quote_dict: dict) -> None:
        str_key: str = 'Settlement Date'
        self._settlement_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_earnings_date(self, quote_dict: dict) -> None:
        str_key: str = 'Earnings Date'
        self._earnings_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_ex_dividend_date(self, quote_dict: dict) -> None:
        str_key: str = 'Ex-Dividend Date'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'nan':
            #self._ex_dividend_date = datetime(self.__get_str_from_dict(str_key, quote_dict))
            print(key_from_quote_dict)

    def __set_dividend_forward(self, quote_dict: dict) -> None:
        str_key: str = 'Forward Dividend & Yield'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        print('```', type(key_from_quote_dict), key_from_quote_dict)
        if not key_from_quote_dict == 'NA':
            a_list: list = key_from_quote_dict.split(' ')
            a_list[0] = a_list[0].replace('/', '')
            a_list[1] = a_list[1].replace('/', '').replace('(', '').replace(')', '')
            print('```?', a_list[0], type(a_list[0]))
            self._dividend_forward = float(a_list[0]) if a_list[0] != 'NA' else np.nan
            print('```!', a_list[1], type(a_list[1]))
            self._yield_pcnt = self.__get_percent_from_str(a_list[1])
            #    round((float(a_list[1].strip('%')) / 100), 5) if a_list[1] != 'NA' else np.nan

    def __set_dividend_last(self, quote_dict: dict) -> None:
        str_key: str = 'Last Dividend'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._dividend_last = float(key_from_quote_dict)

    def __set_cap_gain_last(self, quote_dict: dict) -> None:
        str_key: str = 'Last Cap Gain'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._cap_gain_last = float(key_from_quote_dict)

    def __set_start_date(self, quote_dict: dict) -> None:
        str_key: str = 'Start Date'
        self._start_date = self.__get_str_from_dict(str_key, quote_dict)

    def __set_market_cap(self, quote_dict: dict) -> None:
        str_key: str = 'Market Cap'
        self._market_cap = self.__get_str_from_dict(str_key, quote_dict)

    def __set_eps(self, quote_dict: dict) -> None:
        str_key: str = 'EPS (TTM)'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._eps = float(key_from_quote_dict)

    def __set_net_assets(self, quote_dict: dict) -> None:
        str_key: str = 'Net Assets'
        self._net_assets = self.__get_str_from_dict(str_key, quote_dict)

    def __set_nav(self, quote_dict: dict) -> None:
        str_key: str = 'NAV'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._nav = float(key_from_quote_dict)

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
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._beta_5y_monthly = float(key_from_quote_dict)

    def __set_yield(self, quote_dict: dict) -> None:
        str_key: str = 'Yield'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        print('%%% isnan', str_key, np.isnan(self._yield_pcnt), self._yield_pcnt, key_from_quote_dict)
        if np.isnan(self._yield_pcnt):
            self._yield_pcnt = float(key_from_quote_dict) if key_from_quote_dict != 'NA' else np.nan

    def __set_daily_total_return_ytd(self, quote_dict: dict) -> None:
        str_key: str = 'YTD Daily Total Return'
        self._daily_total_return_ytd = self.__get_str_from_dict(str_key, quote_dict)

    def __set_return_ytd(self, quote_dict: dict) -> None:
        str_key: str = 'YTD Return'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        self._return_ytd_pcnt = float(key_from_quote_dict) if key_from_quote_dict != 'NA' else np.nan

    def __set_return_mean_5y(self, quote_dict: dict) -> None:
        str_key: str = '5y Average Return'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        if key_from_quote_dict != 'NA':
            self._return_mean_5y = float(key_from_quote_dict)

    def __set_ratio_expense_net(self, quote_dict: dict) -> None:
        str_key: str = 'Expense Ratio (net)'
        key_from_quote_dict = self.__get_str_from_dict(str_key, quote_dict)
        self._ratio_expense_net_pcnt = float(key_from_quote_dict) if key_from_quote_dict != 'NA' else np.nan

    def __set_ratio_pe(self, quote_dict: dict) -> None:
        str_key: str = 'PE Ratio (TTM)'
        s: str = self.__get_str_from_dict(str_key, quote_dict)
        self._ratio_pe = np.nan if s == 'NA' else float("{:.3f}".format(float(s)))

    def _get_stats_valuation(self, a_ticker: str) -> None:
        print('_set_stats_valuation')
        df: DataFrame = si.get_stats_valuation(a_ticker)
        df = df.iloc[:, :2]
        df.columns = ['Attribute', 'Recent']
        self._ratio_pe = float(df[df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._ratio_fpe = float(df[df.Attribute.str.contains('Forward P/E')].iloc[0, 1])
        self._ratio_peg = float(df[df.Attribute.str.contains('PEG')].iloc[0, 1])
        print('~~~', df[df.Attribute.str.contains('Enterprise Value/Revenue')].iloc[0, 1])
        self._ratio_ent_value_revenue = float(df[df.Attribute.str.contains('Enterprise Value/Revenue')].iloc[0, 1])
        self._ratio_ent_value_ebitda = float(df[df.Attribute.str.contains('Enterprise Value/EBITDA')].iloc[0, 1])
        self._enterprise_value = df[df.Attribute.str.contains('Enterprise Value')].iloc[0, 1]
        self._price_to_book = float(df[df.Attribute.str.contains('Price/Book')].iloc[0, 1])
        self._price_to_sales = float(df[df.Attribute.str.contains('Price/Sales')].iloc[0, 1])
        '''
        self._price_to_earn = float(self._df[self._df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        '''

    def _get_stats(self, a_ticker: str) -> None:
        print('_get_stats')
        df: DataFrame = si.get_stats(a_ticker)
        df = df.iloc[:, :2]
        #.columns = ['Attribute', 'Value']
        self._ebitda = df[df.Attribute.str.contains('EBITDA')].iloc[0, 1]
        another_pcnt: str = df[df.Attribute.str.contains('Payout Ratio')].iloc[0, 1]
        print('%%%', another_pcnt)
        self._ratio_payout_pcnt = self.__get_percent_from_str(another_pcnt)
        #    round((float(another_pcnt.strip('%')) / 100), 5) if another_pcnt != 'NA' else np.nan
        self._dividend_date = df[df.Attribute.str.contains('Dividend Date')].iloc[0, 1]
        a_pcnt: str = df[df.Attribute.str.contains('Profit Margin')].iloc[0, 1]
        print('%%%', a_pcnt)
        self._profit_margin_pcnt = self.__get_percent_from_str(a_pcnt)
        #    round((float(a_pcnt.strip('%')) / 100), 5) if a_pcnt != 'NA' else np.nan
        print('***', df[df.Attribute.str.contains('EBITDA')].iloc[0, 1])

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
