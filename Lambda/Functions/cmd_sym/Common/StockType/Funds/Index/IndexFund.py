import json

import matplotlib.pyplot as plt
from prettytable import PrettyTable
from yahooquery import Ticker

#
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class IndexFund(AbstractStockFund):
    #
    __y_query: Ticker

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__(c_name.replace(' ', ''), q_type)
        self.__ticker = t_name
        self.__class = 'IndexFund'
        #self.__quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
        #
        self._set_info()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', 'StockInfo'])
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['Type', self.__class])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPercent', self._stock_part_count])
        pt.add_row(['BondPercent', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
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

    def __iter__(self):
        yield from {
            "Info": "StockInfo",
            "ticker": self.__ticker,
            "type": self.__class,
            "quote_type": self._quote_type,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "cash_percent": self._cash_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
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

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
        #return super().to_json() self.__dict__ dict(self)

    def _set_info(self):
        self._set_sector_df(self.__y_query.fund_sector_weightings)
        self._set_holding_df(self.__y_query.fund_top_holdings, self.__ticker, self.__y_query.fund_sector_weightings)
        self._set_part_count(self.__y_query.fund_top_holdings, self.__y_query.fund_category_holdings)
        self._set_fund_holding_info(self.__y_query.fund_holding_info, self.__ticker)
        self._set_fund_performance(self.__y_query.fund_performance, self.__ticker)
        self._set_key_stat_dict('defaultKeyStatistics', self.__y_query.key_stats, self.__ticker)
        self._set_financial_data_dict('financialData', self.__y_query.financial_data, self.__ticker)
        self._set_price_dict('', self.__y_query.price, self.__ticker)
        self._set_quote_type_dict('', self.__y_query.quote_type, self.__ticker)
        self._set_summary_detail_dict('', self.__y_query.summary_detail, self.__ticker)
        self._set_summary_profile_dict('', self.__y_query.summary_profile, self.__ticker)
        self._set_share_purchase_dict('', self.__y_query.share_purchase_activity, self.__ticker)
