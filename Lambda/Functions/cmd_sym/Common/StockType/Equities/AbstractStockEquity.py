from prettytable import PrettyTable
from yahooquery import Ticker

from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockEquity(AbstractStock):
    __ticker: str = 'NA'
    __y_query: Ticker
    __yfsi: YahooFinStockInfo

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__()
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Equity'
        self._quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
        self.__yfsi = YahooFinStockInfo(t_name)
        self._set_info()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', 'StockInfo'])
        pt.add_row(['Ticker', self.__ticker])
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
            "Info": "StockInfo",
            "ticker": self.__ticker,
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
            "has_key_stat_dict": self._has_key_stat_dict,
            "has_financial_data_dict": self._has_financial_data_dict,
            "has_price_dict": self._has_price_dict,
            "has_quote_type_dict": self._has_quote_type_dict,
            "has_summary_detail_dict": self._has_summary_detail_dict,
            "has_summary_profile_dict": self._has_summary_profile_dict,
            "has_share_purchase_dict": self._has_share_purchase_dict
        }.items()

    def _set_info(self):
        self._set_sector_df(self.__y_query.fund_sector_weightings)
        self._set_holding_df(self.__y_query.fund_top_holdings, self.__ticker, self.__y_query.fund_sector_weightings)
        self._set_part_count(self.__y_query.fund_top_holdings, self.__y_query.fund_category_holdings)
        self._set_fund_holding_info_dict('topHoldings', self.__y_query.fund_holding_info, self.__ticker)
        self.__setInfo()
        self._set_fund_performance('fundPerformance', self.__y_query.fund_performance, self.__ticker)
        self._set_key_stat_dict('defaultKeyStatistics', self.__y_query.key_stats, self.__ticker)
        self._set_financial_data_dict('financialData', self.__y_query.financial_data, self.__ticker)
        self._set_price_dict('', self.__y_query.price, self.__ticker)
        self._set_quote_type_dict('', self.__y_query.quote_type, self.__ticker)
        self._set_summary_detail_dict('', self.__y_query.summary_detail, self.__ticker)
        self._set_summary_profile_dict('', self.__y_query.summary_profile, self.__ticker)
        self._set_share_purchase_dict('netSharePurchaseActivity', self.__y_query.share_purchase_activity, self.__ticker)

    def __setInfo(self):
        self._price_to_book = self.__yfsi.PriceToBook
        self._price_to_earn = self.__yfsi.PriceToEarnings
        self._price_to_sale = self.__yfsi.PriceToSales
        '''
        "maxAge": 1,
        "priceHint": 2,
        "enterpriseValue": 1672450801664,
        "forwardPE": 25.70207,
        "profitMargins": 0.21350001,
        "floatShares": 4329740605,
        "sharesOutstanding": 4334329856,
        "sharesShort": 35234606,
        "sharesShortPriorMonth": 34828293,
        "sharesShortPreviousMonthDate": "2020-06-15 00:00:00",
        "dateShortInterest": "2020-07-15 00:00:00",
        "sharesPercentSharesOut": 0.0081,
        "heldPercentInsiders": 0.00066,
        "heldPercentInstitutions": 0.62115,
        "shortRatio": 0.96,
        "shortPercentOfFloat": 0.0081,
        "beta": 1.182072,
        "category": null,
        "bookValue": 18.137,
        "priceToBook": 21.214094,
        "fundFamily": null,
        "legalType": null,
        "lastFiscalYearEnd": "2019-09-28 00:00:00",
        "nextFiscalYearEnd": "2021-09-28 00:00:00",
        "mostRecentQuarter": "2020-03-28 00:00:00",
        "earningsQuarterlyGrowth": -0.027,
        "netIncomeToCommon": 57215000576,
        "trailingEps": 12.728,
        "forwardEps": 14.97,
        "pegRatio": 2.78,
        "lastSplitFactor": "7:1",
        "lastSplitDate": "2014-06-09 00:00:00",
        "enterpriseToRevenue": 6.241,
        "enterpriseToEbitda": 21.634,
        "52WeekChange": 0.8239218,
        "SandP52WeekChange": 0.103224516
        '''
