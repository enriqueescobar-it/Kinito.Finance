from prettytable import PrettyTable
from yahooquery import Ticker

#
from Common.StockType.AbstractStock import AbstractStock


#

class AbstractStockBond(AbstractStock):
    #_ticker: str = 'NA'
    #_y_query: Ticker
    #

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__()
        self._name = c_name.replace(' ', '')
        self._ticker = t_name
        self._class_type = 'Bond'
        self._info_type = self._class_type + 'Info'
        self._quote_type = q_type
        #
        self._y_query = Ticker(t_name)
        #
        self._set_info()

    def __str__(self) -> str:
        return super(AbstractStockBond, self).__str__()

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
            "has_fund_performance_dict": self._has_fund_performance_dict,
            "has_key_stat_dict": self._has_key_stat_dict,
            "has_financial_data_dict": self._has_financial_data_dict,
            "has_price_dict": self._has_price_dict,
            "has_quote_type_dict": self._has_quote_type_dict,
            "has_summary_detail_dict": self._has_summary_detail_dict,
            "has_summary_profile_dict": self._has_summary_profile_dict,
            "has_share_purchase_dict": self._has_share_purchase_dict
        }.items()

    def _set_info(self):
        self._set_sector_df(self._y_query.fund_sector_weightings)
        self._set_holding_df(self._y_query.fund_top_holdings, self._ticker, self._y_query.fund_sector_weightings)
        self._set_part_count(self._y_query.fund_top_holdings, self._y_query.fund_category_holdings)
        self._set_fund_holding_info_dict('topHoldings', self._y_query.fund_holding_info, self._ticker)
        self._set_fund_performance_dict('fundPerformance', self._y_query.fund_performance, self._ticker)
        self._set_key_stat_dict('defaultKeyStatistics', self._y_query.key_stats, self._ticker)
        self._set_financial_data_dict('financialData', self._y_query.financial_data, self._ticker)
        self._set_price_dict('', self._y_query.price, self._ticker)
        self._set_quote_type_dict('', self._y_query.quote_type, self._ticker)
        self._set_summary_detail_dict('', self._y_query.summary_detail, self._ticker)
        self._set_summary_profile_dict('', self._y_query.summary_profile, self._ticker)
        self._set_share_purchase_dict('netSharePurchaseActivity', self._y_query.share_purchase_activity, self._ticker)
