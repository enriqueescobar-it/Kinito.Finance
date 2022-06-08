from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock


class AbstractCurrency(AbstractStock):
    __ticker: str = 'NA'

    def __init__(self, c_name: str, q_type: str):
        super().__init__()
        self._name = c_name.replace(' ', '')
        #
        self.__class = 'Currency'
        self._quote_type = q_type
        #

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['Type', self.__class])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPartCount', self._stock_part_count])
        pt.add_row(['BondPartCount', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
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
            "name": self._name
        }.items()
