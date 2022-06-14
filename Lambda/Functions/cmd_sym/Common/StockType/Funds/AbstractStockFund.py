from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFund(AbstractStock):
    __ticker: str = 'NA'

    def __init__(self, c_name: str, q_type: str):
        super().__init__()
        self.__class = 'Fund'
        self._quote_type = q_type
        #
        self._name = c_name.replace(' ', '')

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
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
        pt.add_row(['HasKeyStatDict', self._has_key_stat_dict])
        pt.add_row(['HasFinancialDataDict', self._has_financial_data_dict])
        pt.add_row(['HasPriceDict', self._has_price_dict])
        pt.add_row(['HasQuoteTypeDict', self._has_quote_type_dict])
        pt.add_row(['HasSummaryDetailDict', self._has_summary_detail_dict])
        pt.add_row(['HasSummaryProfileDict', self._has_summary_profile_dict])
        pt.add_row(['HasSharePurchaseDict', self._has_share_purchase_dict])
        s = pt.__str__()
        if self._has_sectors:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.head().to_string(index=True)
        if self._has_holdings:
            s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.head().to_string(index=True)
        return s

    def __repr__(self):
        return self.__str__()

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
            "has_sectors": self._has_sectors,
            "has_holdings": self._has_holdings,
            "has_key_stat_dict": self._has_key_stat_dict,
            "has_financial_data_dict": self._has_financial_data_dict,
            "has_price_dict": self._has_price_dict,
            "has_quote_type_dict": self._has_quote_type_dict,
            "has_summary_detail_dict": self._has_summary_detail_dict,
            "has_summary_profile_dict": self._has_summary_profile_dict,
            "has_share_purchase_dict": self._has_share_purchase_dict
        }.items()
