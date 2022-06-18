import json
from abc import *

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _header: list = ['Info', 'TypeInfo']
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
    _exchange_dt: str = 'NA'
    _quarter_dt: str = 'NA'
    _fiscal_yend_last_dt: str = 'NA'
    _fiscal_yend_next_dt: str = 'NA'
    _fund_inception_dt: str = 'NA'
    _split_dt: str = 'NA'
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
    _beta: float = np.nan
    _beta_3y: float = np.nan
    _yield: float = np.nan
    _profit_margins: float = np.nan
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
    _rating_morning_star: int = 0
    _rating_risk_morning_star: int = 0
    _enterprise_value: int = 0
    _enterprise_to_revenue: float = np.nan
    _enterprise_to_ebitda: float = np.nan
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
    _has_sector_df: bool = False
    _has_holding_df: bool = False
    _has_key_stat_dict: bool = False
    _has_financial_data_dict: bool = False
    _has_price_dict: bool = False
    _has_quote_type_dict: bool = False
    _has_summary_detail_dict: bool = False
    _has_summary_profile_dict: bool = False
    _has_share_purchase_dict: bool = False
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _key_stat_dict: dict = {}
    _financial_data_dict: dict = {}
    _price_dict: dict = {}
    _quote_type_dict: dict = {}
    _summary_detail_dict: dict = {}
    _summary_profile_dict: dict = {}
    _share_purchase_dict: dict = {}

    def __init__(self):
        self.__class = 'TypeInfo'

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Type', self.__class])
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
        pt.add_row(['ExchangeDateTime', self._exchange_dt])
        pt.add_row(['QuarterDateTime', self._quarter_dt])
        pt.add_row(['QuarterlyGrowthEarnings', self._quarterly_growth_earnings])
        pt.add_row(['YearEndLastDateTime', self._fiscal_yend_last_dt])
        pt.add_row(['YearEndNextDateTime', self._fiscal_yend_next_dt])
        pt.add_row(['SplitDateTime', self._split_dt])
        pt.add_row(['SplitFactor', self._split_factor])
        pt.add_row(['FundInceptionDateTime', self._fund_inception_dt])
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
        pt.add_row(['AssetsTotal', self._assets_total])
        pt.add_row(['Beta', self._beta])
        pt.add_row(['Beta3year', self._beta_3y])
        pt.add_row(['Yield', self._yield])
        pt.add_row(['ProfitMargins', self._profit_margins])
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
        pt.add_row(['RatingMorningStar', self._rating_morning_star])
        pt.add_row(['RatingRiskMorningStar', self._rating_risk_morning_star])
        pt.add_row(['EnterpriseValue', self._enterprise_value])
        pt.add_row(['EnterpriseToRevenue', self._enterprise_to_revenue])
        pt.add_row(['EnterpriseToEBITDA', self._enterprise_to_ebitda])
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
        pt.add_row(['HasSectorDf', self._has_sector_df])
        pt.add_row(['HasHoldingDf', self._has_holding_df])
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
            "Info": self.__class,
            "type": self.__class,
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
            "exchange_dt": self._exchange_dt,
            "quarter_dt": self._quarter_dt,
            "quarterly_growth_earnings": self._quarterly_growth_earnings,
            "fiscal_yend_last_dt": self._fiscal_yend_last_dt,
            "fiscal_yend_next_dt": self._fiscal_yend_next_dt,
            "split_dt": self._split_dt,
            "split_factor": self._split_factor,
            "fund_inception_dt": self._fund_inception_dt,
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
            "assets_total": self._assets_total,
            "beta": self._beta,
            "beta_3y": self._beta_3y,
            "yield": self._yield,
            "profit_margins": self._profit_margins,
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
            "rating_morning_star": self._rating_morning_star,
            "rating_risk_morning_star": self._rating_risk_morning_star,
            "enterprise_value": self._enterprise_value,
            "enterprise_to_revenue": self._enterprise_to_revenue,
            "enterprise_to_ebitda": self._enterprise_to_ebitda,
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
            "has_sector_df": self._has_sector_df,
            "has_holding_df": self._has_holding_df,
            "has_key_stat_dict": self._has_key_stat_dict,
            "has_financial_data_dict": self._has_financial_data_dict,
            "has_price_dict": self._has_price_dict,
            "has_quote_type_dict": self._has_quote_type_dict,
            "has_summary_detail_dict": self._has_summary_detail_dict,
            "has_summary_profile_dict": self._has_summary_profile_dict,
            "has_share_purchase_dict": self._has_share_purchase_dict
        }.items()

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

    def __set_price_to(self, a_dict: dict):
        if 'priceToEarnings' in a_dict.keys():
            self._price_to_earn = a_dict['priceToEarnings']
        if 'priceToBook' in a_dict.keys():
            self._price_to_book = a_dict['priceToBook']
        if 'priceToSales' in a_dict.keys():
            self._price_to_sale = a_dict['priceToSales']
        if 'priceToCashflow' in a_dict.keys():
            self._price_to_cash = a_dict['priceToCashflow']

    def __set_price_dict(self):
        if 'quoteSourceName' in self._price_dict.keys():
            self._quote_src_name = self._price_dict.get('quoteSourceName')
        if 'exchangeName' in self._price_dict.keys():
            self._exchange_name = self._price_dict.get('exchangeName')
        if 'currency' in self._price_dict.keys():
            self._currency = self._price_dict.get('currency')
        if 'currencySymbol' in self._price_dict.keys():
            self._currency_symbol = self._price_dict.get('currencySymbol')
        if 'regularMarketTime' in self._price_dict.keys():
            self._exchange_dt = self._price_dict.get('regularMarketTime')

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
        print('+++++++++++++++++', self._financial_data_dict)
        # print('regularMarketTime', self._key_stat_dict.get('regularMarketTime'))
        # print('exchangeName', self._key_stat_dict.get('exchangeName'))
        # print('currencySymbol', self._key_stat_dict.get('currencySymbol'))
        # print('quoteSourceName', self._key_stat_dict.get('quoteSourceName'))

    def __set_key_stat_dict(self):
        if 'mostRecentQuarter' in self._key_stat_dict.keys():
            self._quarter_dt = self._key_stat_dict.get('mostRecentQuarter')
        if 'lastSplitDate' in self._key_stat_dict.keys():
            self._split_dt = self._key_stat_dict.get('lastSplitDate')
        if 'lastSplitFactor' in self._key_stat_dict.keys():
            self._split_factor = self._key_stat_dict.get('lastSplitFactor')
        if 'lastFiscalYearEnd' in self._key_stat_dict.keys():
            self._fiscal_yend_last_dt = self._key_stat_dict.get('lastFiscalYearEnd')
        if 'nextFiscalYearEnd' in self._key_stat_dict.keys():
            self._fiscal_yend_next_dt = self._key_stat_dict.get('nextFiscalYearEnd')
        if 'category' in self._key_stat_dict.keys():
            self._category = self._key_stat_dict.get('category')
        if 'fundFamily' in self._key_stat_dict.keys():
            self._fund_family = self._key_stat_dict.get('fundFamily')
        if 'fundInceptionDate' in self._key_stat_dict.keys():
            self._fund_inception_dt = self._key_stat_dict.get('fundInceptionDate')
        if 'legalType' in self._key_stat_dict.keys():
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

    def _set_fund_holding_info(self, holding_info_dict: dict, ticker_str: str):
        if not self.__is_any_null(holding_info_dict, ticker_str):
            for key in holding_info_dict.get(ticker_str):
                if key == 'equityHoldings':
                    self.__set_price_to(holding_info_dict.get(ticker_str)[key])

    def _set_fund_performance(self, a_any: any, a_str: str):
        print('^^^^^^^^^^^^^^^^^^^^^', a_any) # 'No fundamentals data found for any of the summaryTypes=fundPerformance'
        if not self.__is_any_null(a_any, a_str):
            for key in a_any.get(a_str):
                print("+", self.__class__.__name__, ':', key)

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
        self._has_summary_profile_dict, self._summary_profile_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        if self._has_summary_profile_dict:
            self.__set_summary_profile_dict()

    def _set_share_purchase_dict(self, str_filter: str, a_dict: dict, str_ticker: str):
        self._has_share_purchase_dict, self._share_purchase_dict = self.__is_dict_valid(str_ticker, a_dict, str_filter)
        # if self._has_share_purchase_dict:
        #    print('------------------', self._share_purchase_dict)

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
