import json
from abc import *

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.Readers.Engine.YahooFinEngine import YahooFinEngine


class AbstractStock(ABC):
    _y_query: Ticker
    _y_fin_engine: YahooFinEngine
    _ticker: str = 'NA'
    _class_type: str = 'NA'
    _info_type: str = _class_type + 'Info'
    _header: list = ['Field', 'FieldInfo']
    _legal_type: str = 'NA'
    _quote_type: str = 'NA'
    _quote_src_name: str = 'NA'
    _uuid: str = '00000000-0000-0000-0000-000000000000'
    _underlying_s: str = 'NA'
    _symbol: str = 'NA'
    _currency: str = 'NA'
    _currency_symbol: str = '$'
    _exchange: str = 'NA'
    _exchange_name: str = 'NA'
    _exchange_str: str = '2001-09-11 00:00:00'
    _quarter_str: str = '2001-09-11 00:00:00'
    _fiscal_yend_last_str: str = '2001-09-11 00:00:00'
    _fiscal_yend_next_str: str = '2001-09-11 00:00:00'
    _fund_inception_str: str = '2001-09-11 00:00:00'
    _split_str: str = '2001-09-11 00:00:00'
    _format_dt: str = "%Y-%m-%d %H:%M:%S"
    _split_factor: str = '1:1'
    _t_z: str = 'GMT'
    _industry: str = 'NA'
    _sector: str = 'NA'
    _category: str = 'NA'
    _fund_family: str = 'NA'
    _name: str = 'NA'
    _stock_part_count: int = 0
    _bond_part_count: int = 0
    _cash_part_count: int = 0
    _other_part_count: int = 0
    _pref_part_count: int = 0
    _conv_part_count: int = 0
    _employee_count: int = 0
    _assets_total: int = 0
    _cashflow_free: int = 0
    _cashflow_operating: int = 0
    _beta: float = np.nan
    _beta_3y: float = np.nan
    _yield: float = np.nan
    _profit_margins: float = np.nan
    _gross_margins: float = np.nan
    _operating_margins: float = np.nan
    _ratio_current: float = np.nan
    _ratio_quick: float = np.nan
    _ratio_peg: float = np.nan
    _ratio_short: float = np.nan
    _pe_forward: float = np.nan
    _eps_forward: float = np.nan
    _eps_trailing: float = np.nan
    _quarterly_growth_earnings: float = np.nan
    _book_value: float = np.nan
    _annual_holdings_turnover: float = np.nan
    _annual_report_expense_ratio: float = np.nan
    _cap_gain: float = np.nan
    _dividend_value: float = np.nan
    _price_to_book: float = np.nan
    _price_to_cash: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sale: float = np.nan
    _median_market_cap: float = np.nan
    _rating_mean: float = np.nan
    _rating: str = 'NA'
    _rating_count: int = 0
    _rating_morning_star: int = 0
    _rating_risk_morning_star: int = 0
    _enterprise_value: int = 0
    _enterprise_to_revenue: float = np.nan
    _enterprise_to_ebitda: float = np.nan
    _ebitda: int = 0
    _ebitda_margins: float = np.nan
    _price: float = np.nan
    _open: float = np.nan
    _high: float = np.nan
    _low: float = np.nan
    _close: float = np.nan
    _high_52week: float = np.nan
    _low_52week: float = np.nan
    _mean_52week: float = np.nan
    _change_52week: float = np.nan
    _change_snp_52week: float = np.nan
    _mean_200day: float = np.nan
    _return_ytd: float = np.nan
    _return_mean_3y: float = np.nan
    _return_mean_5y: float = np.nan
    _return_on_assets: float = np.nan
    _return_on_equity: float = np.nan
    _revenue_growth: float = np.nan
    _earnings_growth_3y: float = np.nan
    _revenue: int = 0
    _revenue_per_share: float = np.nan
    _cash_per_share: float = np.nan
    _cash: int = 0
    _debt: int = 0
    _debt_to_equity: float = np.nan
    _has_sector_df: bool = False
    _has_holding_df: bool = False
    _has_fund_holding_info_dict: bool = False
    _has_fund_performance_dict: bool = False
    _has_key_stat_dict: bool = False
    _has_financial_data_dict: bool = False
    _has_price_dict: bool = False
    _has_quote_type_dict: bool = False
    _has_summary_detail_dict: bool = False
    _has_summary_profile_dict: bool = False
    _has_share_purchase_dict: bool = False
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _fund_holding_info_dict: dict = {}
    _fund_performance_dict: dict = {}
    _key_stat_dict: dict = {}
    _financial_data_dict: dict = {}
    _price_dict: dict = {}
    _quote_type_dict: dict = {}
    _summary_detail_dict: dict = {}
    _summary_profile_dict: dict = {}
    _share_purchase_dict: dict = {}

    def __init__(self):
        #self._info_type = self._class_type + 'Info'
        pass

    def __str__(self) -> str:
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', self._info_type])
        pt.add_row(['Ticker', self._ticker])
        pt.add_row(['ClassType', self._class_type])
        pt.add_row(['LegalType', self._legal_type])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['QuoteSourceName', self._quote_src_name])
        pt.add_row(['UUID', self._uuid])
        pt.add_row(['UnderlyingSymbol', self._underlying_s])
        pt.add_row(['Symbol', self._symbol])
        pt.add_row(['Currency', self._currency])
        pt.add_row(['CurrencySymbol', self._currency_symbol])
        pt.add_row(['Exchange', self._exchange])
        pt.add_row(['ExchangeName', self._exchange_name])
        pt.add_row(['ExchangeDateTime', self._exchange_str])
        pt.add_row(['QuarterDateTime', self._quarter_str])
        pt.add_row(['QuarterlyGrowthEarnings', self._quarterly_growth_earnings])
        pt.add_row(['YearEndLastDateTime', self._fiscal_yend_last_str])
        pt.add_row(['YearEndNextDateTime', self._fiscal_yend_next_str])
        pt.add_row(['SplitDateTime', self._split_str])
        pt.add_row(['SplitFactor', self._split_factor])
        pt.add_row(['FundInceptionDateTime', self._fund_inception_str])
        pt.add_row(['TZ', self._t_z])
        pt.add_row(['Industry', self._industry])
        pt.add_row(['Sector', self._sector])
        pt.add_row(['Category', self._category])
        pt.add_row(['FundFamily', self._fund_family])
        pt.add_row(['EmployeeCount', self._employee_count])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPercent', self._stock_part_count])
        pt.add_row(['BondPercent', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['OtherPercent', self._other_part_count])
        pt.add_row(['PreferredPercent', self._pref_part_count])
        pt.add_row(['ConvertiblePercent', self._conv_part_count])
        pt.add_row(['AssetsTotal', self._assets_total])
        pt.add_row(['CashflowFree', self._cashflow_free])
        pt.add_row(['CashflowOperating', self._cashflow_operating])
        pt.add_row(['Beta', self._beta])
        pt.add_row(['Beta3year', self._beta_3y])
        pt.add_row(['Yield', self._yield])
        pt.add_row(['ProfitMargins', self._profit_margins])
        pt.add_row(['GrossMargins', self._gross_margins])
        pt.add_row(['OperatingMargins', self._operating_margins])
        pt.add_row(['RatioCurrent', self._ratio_current])
        pt.add_row(['RatioQuick', self._ratio_quick])
        pt.add_row(['RatioPEG', self._ratio_peg])
        pt.add_row(['RatioShort', self._ratio_short])
        pt.add_row(['PEforward', self._pe_forward])
        pt.add_row(['EPSforward', self._eps_forward])
        pt.add_row(['EPStrailing', self._eps_trailing])
        pt.add_row(['BookValue', self._book_value])
        pt.add_row(['AnnualHoldingsTurnover', self._annual_holdings_turnover])
        pt.add_row(['AnnualReportExpanseRatio', self._annual_report_expense_ratio])
        pt.add_row(['CapGain', self._cap_gain])
        pt.add_row(['DividendValue', self._dividend_value])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['MedianMarketCap', self._median_market_cap])
        pt.add_row(['Rating', self._rating])
        pt.add_row(['RatingMean', self._rating_mean])
        pt.add_row(['RatingCount', self._rating_count])
        pt.add_row(['RatingMorningStar', self._rating_morning_star])
        pt.add_row(['RatingRiskMorningStar', self._rating_risk_morning_star])
        pt.add_row(['EnterpriseValue', self._enterprise_value])
        pt.add_row(['EnterpriseToRevenue', self._enterprise_to_revenue])
        pt.add_row(['EnterpriseToEBITDA', self._enterprise_to_ebitda])
        pt.add_row(['EBITDA', self._ebitda])
        pt.add_row(['EBITDAmargins', self._ebitda_margins])
        pt.add_row(['Price', self._price])
        pt.add_row(['Open', self._open])
        pt.add_row(['High', self._high])
        pt.add_row(['Low', self._low])
        pt.add_row(['Close', self._close])
        pt.add_row(['High52Week', self._high_52week])
        pt.add_row(['Low52Week', self._low_52week])
        pt.add_row(['Mean52Week', self._mean_52week])
        pt.add_row(['Change52Week', self._change_52week])
        pt.add_row(['ChangeSnP52Week', self._change_snp_52week])
        pt.add_row(['Mean200Days', self._mean_200day])
        pt.add_row(['ReturnYearToDate', self._return_ytd])
        pt.add_row(['ReturnMean3Year', self._return_mean_3y])
        pt.add_row(['ReturnMean5Year', self._return_mean_5y])
        pt.add_row(['ReturnOnAssets', self._return_on_assets])
        pt.add_row(['ReturnOnEquity', self._return_on_equity])
        pt.add_row(['RevenueGrowth', self._revenue_growth])
        pt.add_row(['EarningsGrowth3Year', self._earnings_growth_3y])
        pt.add_row(['Revenue', self._revenue])
        pt.add_row(['RevenuePerShare', self._revenue_per_share])
        pt.add_row(['CashPerShare', self._cash_per_share])
        pt.add_row(['Cash', self._cash])
        pt.add_row(['Debt', self._debt])
        pt.add_row(['DebtToEquity', self._debt_to_equity])
        pt.add_row(['HasSectorDf', self._has_sector_df])
        pt.add_row(['HasHoldingDf', self._has_holding_df])
        pt.add_row(['HasFundHoldingInfoDict', self._has_fund_holding_info_dict])
        pt.add_row(['HasFundPerformanceDict', self._has_fund_performance_dict])
        pt.add_row(['HasKeyStatDict', self._has_key_stat_dict])
        pt.add_row(['HasFinancialDataDict', self._has_financial_data_dict])
        pt.add_row(['HasPriceDict', self._has_price_dict])
        pt.add_row(['HasQuoteTypeDict', self._has_quote_type_dict])
        pt.add_row(['HasSummaryDetailDict', self._has_summary_detail_dict])
        pt.add_row(['HasSummaryProfileDict', self._has_summary_profile_dict])
        pt.add_row(['HasSharePurchaseDict', self._has_share_purchase_dict])
        s = pt.__str__()
        if self._has_sector_df:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.to_string(index=True)
        if self._has_holding_df:
            s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.to_string(index=True)
        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "Info": self._header[1],
            "info": self._info_type,
            "ticker": self._ticker,
            "class_type": self._class_type,
            "legal_type": self._legal_type,
            "quote_type": self._quote_type,
            "quote_src_name": self._quote_src_name,
            "uuid": self._uuid,
            "underlying_symbol": self._underlying_s,
            "symbol": self._symbol,
            "currency": self._currency,
            "currency_symbol": self._currency_symbol,
            "exchange": self._exchange,
            "exchange_name": self._exchange_name,
            "exchange_dt": self._exchange_str,
            "quarter_dt": self._quarter_str,
            "quarterly_growth_earnings": self._quarterly_growth_earnings,
            "fiscal_yend_last_dt": self._fiscal_yend_last_str,
            "fiscal_yend_next_dt": self._fiscal_yend_next_str,
            "split_dt": self._split_str,
            "split_factor": self._split_factor,
            "fund_inception_dt": self._fund_inception_str,
            "t_z": self._t_z,
            "industry": self._industry,
            "sector": self._sector,
            "category": self._category,
            "fund_family": self._fund_family,
            "employee_count": self._employee_count,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "cash_percent": self._cash_part_count,
            "other_percent": self._other_part_count,
            "preferred_percent": self._pref_part_count,
            "convertible_percent": self._conv_part_count,
            "assets_total": self._assets_total,
            "cashflow_free": self._cashflow_free,
            "cashflow_operating": self._cashflow_operating,
            "beta": self._beta,
            "beta_3y": self._beta_3y,
            "yield": self._yield,
            "profit_margins": self._profit_margins,
            "gross_margins": self._gross_margins,
            "operating_margins": self._operating_margins,
            "ratio_current": self._ratio_current,
            "ratio_quick": self._ratio_quick,
            "ratio_peg": self._ratio_peg,
            "ratio_short": self._ratio_short,
            "pe_forward": self._pe_forward,
            "eps_forward": self._eps_forward,
            "eps_trailing": self._eps_trailing,
            "book_value": self._book_value,
            "annual_holdings_turnover": self._annual_holdings_turnover,
            "annual_report_expense_ratio": self._annual_report_expense_ratio,
            "cap_gain": self._cap_gain,
            "dividend_value": self._dividend_value,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
            "median_market_cap": self._median_market_cap,
            "rating": self._rating,
            "rating_mean": self._rating_mean,
            "rating_count": self._rating_count,
            "rating_morning_star": self._rating_morning_star,
            "rating_risk_morning_star": self._rating_risk_morning_star,
            "enterprise_value": self._enterprise_value,
            "enterprise_to_revenue": self._enterprise_to_revenue,
            "enterprise_to_ebitda": self._enterprise_to_ebitda,
            "ebitda": self._ebitda,
            "ebitda_margins": self._ebitda_margins,
            "price": self._price,
            "open": self._open,
            "high": self._high,
            "low": self._low,
            "close": self._close,
            "high_52week": self._high_52week,
            "low_52week": self._low_52week,
            "mean_52week": self._mean_52week,
            "change_52week": self._change_52week,
            "change_snp_52week": self._change_snp_52week,
            "mean_200day": self._mean_200day,
            "return_ytd": self._return_ytd,
            "return_mean_3y": self._return_mean_3y,
            "return_mean_5y": self._return_mean_5y,
            "return_on_assets": self._return_on_assets,
            "return_on_equity": self._return_on_equity,
            "revenue_growth": self._revenue_growth,
            "earnings_growth_3y": self._earnings_growth_3y,
            "revenue": self._revenue,
            "revenue_per_share": self._revenue_per_share,
            "cash_per_share": self._cash_per_share,
            "cash": self._cash,
            "debt": self._debt,
            "debt_to_equity": self._debt_to_equity,
            "has_sector_df": self._has_sector_df,
            "has_holding_df": self._has_holding_df,
            "has_fund_holding_info_dict": self._has_fund_holding_info_dict,
            "has_fund_performance_dict": self._has_fund_performance_dict,
            "has_key_stat_dict": self._has_key_stat_dict,
            "has_financial_data_dict": self._has_financial_data_dict,
            "has_price_dict": self._has_price_dict,
            "has_quote_type_dict": self._has_quote_type_dict,
            "has_summary_detail_dict": self._has_summary_detail_dict,
            "has_summary_profile_dict": self._has_summary_profile_dict,
            "has_share_purchase_dict": self._has_share_purchase_dict
        }.items()

    def __is_key_null(self, a_any: any) -> bool:
        # or isinstance(a_any, NoneType)
        return a_any is None

    def __is_any_null(self, a_any: any, a_str: str) -> bool:
        boo: bool = any(a_any) and (len(a_any.get(a_str)) >= 38) and \
                    (not (("Quote not found for ticker symbol: " + a_str) in str(a_any)))
        if boo:
            print("+", self.__class__.__name__, 'dict:', a_str, type(a_any), 'size', len(a_any.get(a_str)))
        return boo

    def __is_dict_valid(self, a_key: str, a_dict: dict, a_str: str) -> (bool, dict):
        boo: bool = any(a_dict) and (isinstance(a_dict, dict)) and \
                    not (("summaryTypes=" + a_str) in str(a_dict)) and \
                    not ("Quote not found for ticker symbol: " in str(a_dict))
        return (boo, a_dict.get(a_key)) if boo else (boo, {})

    def __set_fund_holding_info_dict(self):
        if ('cashPosition' in self._fund_holding_info_dict.keys()) and (self._cash_part_count != 0):
            self._cash_part_count = round(self._fund_holding_info_dict.get('cashPosition') * 100)
        if ('stockPosition' in self._fund_holding_info_dict.keys()) and (self._stock_part_count != 0):
            self._stock_part_count = round(self._fund_holding_info_dict.get('stockPosition') * 100)
        if ('bondPosition' in self._fund_holding_info_dict.keys()) and (self._bond_part_count != 0):
            self._bond_part_count = round(self._fund_holding_info_dict.get('bondPosition') * 100)
        if ('otherPosition' in self._fund_holding_info_dict.keys()) and (self._other_part_count != 0):
            self._other_part_count = round(self._fund_holding_info_dict.get('otherPosition') * 100)
        if ('preferredPosition' in self._fund_holding_info_dict.keys()) and (self._pref_part_count != 0):
            self._pref_part_count = round(self._fund_holding_info_dict.get('preferredPosition') * 100)
        if ('convertiblePosition' in self._fund_holding_info_dict.keys()) and (self._conv_part_count != 0):
            self._conv_part_count = round(self._fund_holding_info_dict.get('convertiblePosition') * 100)

    def __set_price_to(self, a_dict: dict):
        if 'priceToEarnings' in a_dict.keys():
            self._price_to_earn = a_dict['priceToEarnings']
        if 'priceToBook' in a_dict.keys():
            self._price_to_book = a_dict['priceToBook']
        if 'priceToSales' in a_dict.keys():
            self._price_to_sale = a_dict['priceToSales']
        if 'priceToCashflow' in a_dict.keys():
            self._price_to_cash = a_dict['priceToCashflow']
        if 'medianMarketCap' in a_dict.keys():
            self._median_market_cap = a_dict['medianMarketCap']
        if 'threeYearEarningsGrowth' in a_dict.keys():
            self._earnings_growth_3y = a_dict['threeYearEarningsGrowth']

    def __set_price_dict(self):
        if 'quoteSourceName' in self._price_dict.keys():
            self._quote_src_name = self._price_dict.get('quoteSourceName')
        if 'exchangeName' in self._price_dict.keys():
            self._exchange_name = self._price_dict.get('exchangeName')
        if 'currency' in self._price_dict.keys():
            self._currency = self._price_dict.get('currency')
        if 'currencySymbol' in self._price_dict.keys():
            self._currency_symbol = self._price_dict.get('currencySymbol')
        if 'regularMarketTime' in self._price_dict.keys() and not(self.__is_key_null(self._price_dict.get('regularMarketTime'))):
            self._exchange_str = self._price_dict.get('regularMarketTime')

    def __set_quote_type_dict(self):
        if 'uuid' in self._quote_type_dict.keys():
            self._uuid = self._quote_type_dict.get('uuid')
        if 'underlyingSymbol' in self._quote_type_dict.keys():
            self._underlying_s = self._quote_type_dict.get('underlyingSymbol')
        if 'symbol' in self._quote_type_dict.keys():
            self._symbol = self._quote_type_dict.get('symbol')
        if 'exchange' in self._quote_type_dict.keys():
            self._exchange = self._quote_type_dict.get('exchange')
        if 'timeZoneShortName' in self._quote_type_dict.keys():
            self._t_z = self._quote_type_dict.get('timeZoneShortName')

    def __set_summary_profile_dict(self):
        if 'industry' in self._summary_profile_dict.keys():
            self._industry = self._summary_profile_dict.get('industry')
        if 'sector' in self._summary_profile_dict.keys():
            self._sector = self._summary_profile_dict.get('sector')
        if 'fullTimeEmployees' in self._summary_profile_dict.keys():
            self._employee_count = self._summary_profile_dict.get('fullTimeEmployees')

    def __set_summary_detail_dict(self):
        if 'open' in self._summary_detail_dict.keys():
            self._open = self._summary_detail_dict.get('open')
        if 'dayHigh' in self._summary_detail_dict.keys():
            self._low = self._summary_detail_dict.get('dayLow')
        if 'dayHigh' in self._summary_detail_dict.keys():
            self._high = self._summary_detail_dict.get('dayHigh')
        if 'previousClose' in self._summary_detail_dict.keys():
            self._close = self._summary_detail_dict.get('previousClose')
        if 'fiftyTwoWeekHigh' in self._summary_detail_dict.keys():
            self._high_52week = self._summary_detail_dict.get('fiftyTwoWeekHigh')
        if 'fiftyTwoWeekLow' in self._summary_detail_dict.keys():
            self._low_52week = self._summary_detail_dict.get('fiftyTwoWeekLow')
        if 'fiftyDayAverage' in self._summary_detail_dict.keys():
            self._mean_52week = self._summary_detail_dict.get('fiftyDayAverage')
        if 'twoHundredDayAverage' in self._summary_detail_dict.keys():
            self._mean_200day = self._summary_detail_dict.get('twoHundredDayAverage')

    def __set_financial_data_dict(self):
        if 'profitMargins' in self._financial_data_dict.keys() and np.isnan(self._profit_margins):
            self._profit_margins = self._financial_data_dict.get('profitMargins')
        if 'grossMargins' in self._financial_data_dict.keys():
            self._gross_margins = self._financial_data_dict.get('grossMargins')
        if 'operatingMargins' in self._financial_data_dict.keys():
            self._operating_margins = self._financial_data_dict.get('operatingMargins')
        if 'currentPrice' in self._financial_data_dict.keys():
            self._price = self._financial_data_dict.get('currentPrice')
        if 'ebitda' in self._financial_data_dict.keys():
            self._ebitda = self._financial_data_dict.get('ebitda')
        if 'ebitdaMargins' in self._financial_data_dict.keys():
            self._ebitda_margins = self._financial_data_dict.get('ebitdaMargins')
        if 'currentRatio' in self._financial_data_dict.keys():
            self._ratio_current = self._financial_data_dict.get('currentRatio')
        if 'quickRatio' in self._financial_data_dict.keys():
            self._ratio_quick = self._financial_data_dict.get('quickRatio')
        if 'recommendationMean' in self._financial_data_dict.keys():
            self._rating_mean = self._financial_data_dict.get('recommendationMean')
        if 'recommendationKey' in self._financial_data_dict.keys():
            self._rating = self._financial_data_dict.get('recommendationKey')
        if 'numberOfAnalystOpinions' in self._financial_data_dict.keys():
            self._rating_count = self._financial_data_dict.get('numberOfAnalystOpinions')
        if 'debtToEquity' in self._financial_data_dict.keys():
            self._debt_to_equity = self._financial_data_dict.get('debtToEquity')
        if 'returnOnAssets' in self._financial_data_dict.keys():
            self._return_on_assets = self._financial_data_dict.get('returnOnAssets')
        if 'returnOnEquity' in self._financial_data_dict.keys():
            self._return_on_equity = self._financial_data_dict.get('returnOnEquity')
        if 'freeCashflow' in self._financial_data_dict.keys():
            self._cashflow_free = self._financial_data_dict.get('freeCashflow')
        if 'operatingCashflow' in self._financial_data_dict.keys():
            self._cashflow_operating = self._financial_data_dict.get('operatingCashflow')
        if 'revenueGrowth' in self._financial_data_dict.keys():
            self._revenue_growth = self._financial_data_dict.get('revenueGrowth')
        if 'revenuePerShare' in self._financial_data_dict.keys():
            self._revenue_per_share = self._financial_data_dict.get('revenuePerShare')
        if 'totalCashPerShare' in self._financial_data_dict.keys():
            self._cash_per_share = self._financial_data_dict.get('totalCashPerShare')
        if 'totalCash' in self._financial_data_dict.keys():
            self._cash = self._financial_data_dict.get('totalCash')
        if 'totalRevenue' in self._financial_data_dict.keys():
            self._revenue = self._financial_data_dict.get('totalRevenue')
        if 'totalDebt' in self._financial_data_dict.keys():
            self._debt = self._financial_data_dict.get('totalDebt')

    def __set_key_stat_dict(self):
        if 'mostRecentQuarter' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('mostRecentQuarter'))):
            self._quarter_str = self._key_stat_dict.get('mostRecentQuarter')
        if 'lastSplitDate' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('lastSplitDate'))):
            self._split_str = self._key_stat_dict.get('lastSplitDate')
        if 'lastSplitFactor' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('lastSplitFactor'))):
            self._split_factor = self._key_stat_dict.get('lastSplitFactor')
        if 'lastFiscalYearEnd' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('lastFiscalYearEnd'))):
            self._fiscal_yend_last_str = self._key_stat_dict.get('lastFiscalYearEnd')
        if 'nextFiscalYearEnd' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('nextFiscalYearEnd'))):
            self._fiscal_yend_next_str = self._key_stat_dict.get('nextFiscalYearEnd')
        if 'category' in self._key_stat_dict.keys() and not(self.__is_key_null(self._key_stat_dict.get('category'))):
            self._category = self._key_stat_dict.get('category')
        if 'fundFamily' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('fundFamily'))):
            self._fund_family = self._key_stat_dict.get('fundFamily')
        if 'fundInceptionDate' in self._key_stat_dict.keys() and\
                not(self.__is_key_null(self._key_stat_dict.get('fundInceptionDate'))):
            self._fund_inception_str = self._key_stat_dict.get('fundInceptionDate')
        if 'legalType' in self._key_stat_dict.keys() and not(self.__is_key_null(self._key_stat_dict.get('legalType'))):
            self._legal_type = self._key_stat_dict.get('legalType')
        if 'beta' in self._key_stat_dict.keys():
            self._beta = self._key_stat_dict.get('beta')
        if 'beta3Year' in self._key_stat_dict.keys():
            self._beta_3y = self._key_stat_dict.get('beta3Year')
        if 'yield' in self._key_stat_dict.keys():
            self._yield = self._key_stat_dict.get('yield')
        if 'profitMargins' in self._key_stat_dict.keys():
            self._profit_margins = self._key_stat_dict.get('profitMargins')
        if 'totalAssets' in self._key_stat_dict.keys():
            self._assets_total = self._key_stat_dict.get('totalAssets')
        if 'pegRatio' in self._key_stat_dict.keys():
            self._ratio_peg = self._key_stat_dict.get('pegRatio')
        if 'shortRatio' in self._key_stat_dict.keys():
            self._ratio_short = self._key_stat_dict.get('shortRatio')
        if 'bookValue' in self._key_stat_dict.keys():
            self._book_value = self._key_stat_dict.get('bookValue')
        if 'annualHoldingsTurnover' in self._key_stat_dict.keys():
            self._annual_holdings_turnover = self._key_stat_dict.get('annualHoldingsTurnover')
        if 'annualReportExpenseRatio' in self._key_stat_dict.keys():
            self._annual_report_expense_ratio = self._key_stat_dict.get('annualReportExpenseRatio')
        if 'lastCapGain' in self._key_stat_dict.keys():
            self._cap_gain = self._key_stat_dict.get('lastCapGain')
        if 'lastDividendValue' in self._key_stat_dict.keys():
            self._dividend_value = self._key_stat_dict.get('lastDividendValue')
        if 'forwardEps' in self._key_stat_dict.keys():
            self._eps_forward = self._key_stat_dict.get('forwardEps')
        if 'trailingEps' in self._key_stat_dict.keys():
            self._eps_trailing = self._key_stat_dict.get('trailingEps')
        if 'forwardPE' in self._key_stat_dict.keys():
            self._pe_forward = self._key_stat_dict.get('forwardPE')
        if 'enterpriseValue' in self._key_stat_dict.keys():
            self._enterprise_value = self._key_stat_dict.get('enterpriseValue')
        if 'enterpriseToRevenue' in self._key_stat_dict.keys():
            self._enterprise_to_revenue = self._key_stat_dict.get('enterpriseToRevenue')
        if 'enterpriseToEbitda' in self._key_stat_dict.keys():
            self._enterprise_to_ebitda = self._key_stat_dict.get('enterpriseToEbitda')
        if 'earningsQuarterlyGrowth' in self._key_stat_dict.keys():
            self._quarterly_growth_earnings = self._key_stat_dict.get('earningsQuarterlyGrowth')
        if ('priceToBook' in self._key_stat_dict.keys()) and np.isnan(self._price_to_book):
            self._price_to_book = self._key_stat_dict.get('priceToBook')
        if '52WeekChange' in self._key_stat_dict.keys():
            self._change_52week = self._key_stat_dict.get('52WeekChange')
        if 'SandP52WeekChange' in self._key_stat_dict.keys():
            self._change_snp_52week = self._key_stat_dict.get('SandP52WeekChange')
        if 'ytdReturn' in self._key_stat_dict.keys():
            self._return_ytd = self._key_stat_dict.get('ytdReturn')
        if 'threeYearAverageReturn' in self._key_stat_dict.keys():
            self._return_mean_3y = self._key_stat_dict.get('threeYearAverageReturn')
        if 'fiveYearAverageReturn' in self._key_stat_dict.keys():
            self._return_mean_5y = self._key_stat_dict.get('fiveYearAverageReturn')
        if 'morningStarOverallRating' in self._key_stat_dict.keys():
            self._rating_morning_star = self._key_stat_dict.get('morningStarOverallRating')
        if 'morningStarRiskRating' in self._key_stat_dict.keys():
            self._rating_risk_morning_star = self._key_stat_dict.get('morningStarRiskRating')

    def _set_info(self):
        pass

    def _set_sector_df(self, a_any: any):
        is_any: bool = any(a_any)
        if not is_any:
            self._sector_df = DataFrame()
        else:
            is_df: bool = isinstance(a_any, DataFrame)
            if is_df:
                self._sector_df = a_any.reset_index()
                self._sector_df.columns = ['Sector', 'Percent']
                self._has_sector_df = True
            else:
                s: str = (list(a_any.values())[0]).split(' found ')[0]
                self._sector_df['Sector'] = s
                self._sector_df['Percent'] = 1.0
                self._sector_df.loc[0] = [s, 1.0]

    def _set_holding_df(self, any_top: any, str_ticker: str, any_sector: any):
        is_ok: bool = any(any_top) and any(any_sector)
        if is_ok:
            is_df: bool = isinstance(any_top, DataFrame)
            if is_df:
                self._holding_df = any_top
                self._holding_df.set_index('symbol', inplace=True)
                self._holding_df.reset_index(inplace=True)
                self._has_holding_df = True
            else:
                s: str = (list(any_sector.values())[0]).split(' found ')[0]
                self._holding_df['symbol'] = s
                self._holding_df['holdingName'] = 'a name'
                self._holding_df['holdingPercent'] = 1.0
                self._holding_df.loc[0] = [str_ticker, s, 1.0]

    def _set_part_count(self, any_top: any, any_category: any):
        is_df: bool = any(any_top) and isinstance(any_top, DataFrame)
        df: DataFrame = DataFrame()
        stock_int: int = 0
        bond_int: int = 0
        cash_int: int = 0
        other_int: int = 0
        pref_int: int = 0
        conv_int: int = 0
        if is_df and any(any_category) and isinstance(any_category, DataFrame):
            df = any_category.set_index('maxAge')
            df.reset_index(inplace=True)
            if 'stockPosition' in df.columns:
                stock_int = round(df['stockPosition'][0] * 100)
            if 'bondPosition' in df.columns:
                bond_int = round(df['bondPosition'][0] * 100)
            if 'cashPosition' in df.columns:
                cash_int = round(df['cashPosition'][0] * 100)
            if 'otherPosition' in df.columns:
                other_int = round(df['otherPosition'][0] * 100)
            if 'preferredPosition' in df.columns:
                pref_int = round(df['preferredPosition'][0] * 100)
            if 'convertiblePosition' in df.columns:
                conv_int = round(df['convertiblePosition'][0] * 100)
        else:
            df['maxAge'] = 1.0
            df['cashPosition'] = np.nan
            df['stockPosition'] = np.nan
            df['bondPosition'] = np.nan
            df['otherPosition'] = np.nan
            df['preferredPosition'] = np.nan
            df['convertiblePosition'] = np.nan
            df.loc[0] = [1.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            df = df.set_index('maxAge')
            df.reset_index(inplace=True)
            stock_int = round(np.nan_to_num(df['stockPosition'][0]) * 100)
            bond_int = round(np.nan_to_num(df['bondPosition'][0]) * 100)
            cash_int = round(np.nan_to_num(df['cashPosition'][0]) * 100)
            other_int = round(np.nan_to_num(df['otherPosition'][0]) * 100)
            pref_int = round(np.nan_to_num(df['preferredPosition'][0]) * 100)
            conv_int = round(np.nan_to_num(df['convertiblePosition'][0]) * 100)
        self._stock_part_count = stock_int
        self._bond_part_count = bond_int
        self._cash_part_count = cash_int
        self._other_part_count = other_int
        self._pref_part_count = pref_int
        self._conv_part_count = conv_int

    def _set_key_stat_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_key_stat_dict, self._key_stat_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_key_stat_dict:
            self.__set_key_stat_dict()

    def _set_financial_data_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_financial_data_dict, self._financial_data_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_financial_data_dict:
            self.__set_financial_data_dict()

    def _set_price_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_price_dict, self._price_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_price_dict:
            self.__set_price_dict()

    def _set_quote_type_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_quote_type_dict, self._quote_type_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_quote_type_dict:
            self.__set_quote_type_dict()

    def _set_summary_detail_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_summary_detail_dict, self._summary_detail_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_summary_detail_dict:
            self.__set_summary_detail_dict()

    def _set_summary_profile_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_summary_profile_dict, self._summary_profile_dict =\
            self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_summary_profile_dict:
            self.__set_summary_profile_dict()

    def _set_fund_holding_info_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_fund_holding_info_dict, self._fund_holding_info_dict =\
            self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_fund_holding_info_dict:
            self.__set_fund_holding_info_dict()
            for key in a_dict.get(str_ticker):
                if key == 'equityHoldings':
                    self.__set_price_to(a_dict.get(str_ticker)[key])

    def _set_fund_performance_dict(self, str_filter: str, a_dict: any, str_ticker: str):
        self._has_fund_performance_dict, self._fund_performance_dict =\
            self.__is_dict_valid(str_ticker, a_dict, str_filter)

    def _set_share_purchase_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_share_purchase_dict, self._share_purchase_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)

    def _plot_sector_df(self, class_str: str, tick_str: str):
        if (self._sector_df['Percent'] != self._sector_df['Percent'][0]).all():
            self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                     autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                     title='Sector Distribution ' + tick_str + ' ' + class_str)
            return plt

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def Name(self):
        return self._name

    @property
    def StockPartCount(self):
        return self._stock_part_count

    @property
    def BondPartCount(self):
        return self._bond_part_count

    @property
    def CashPartCount(self):
        return self._cash_part_count

    @property
    def PriceToBook(self):
        return self._price_to_book

    @property
    def PriceToCashflow(self):
        return self._price_to_cash

    @property
    def PriceToEarnings(self):
        return self._price_to_earn

    @property
    def PriceToSales(self):
        return self._price_to_sale

    @property
    def HasSectorDf(self):
        return self._has_sector_df

    @property
    def HasHoldingDf(self):
        return self._has_holding_df

    @property
    def HasKeyStatDict(self):
        return self._has_key_stat_dict

    @property
    def HasFinancialDataDict(self):
        return self._has_financial_data_dict

    @property
    def HasPriceDict(self):
        return self._has_price_dict

    @property
    def HasQuoteTypeDict(self):
        return self._has_quote_type_dict

    @property
    def HasSummaryDetailDict(self):
        return self._has_summary_detail_dict

    @property
    def HasSummaryProfileDict(self):
        return self._has_summary_profile_dict

    @property
    def HasSharePurchaseDict(self):
        return self._has_share_purchase_dict

    @property
    def SectorDataFrame(self):
        return self._sector_df

    @property
    def HoldingDataFrame(self):
        return self._holding_df
