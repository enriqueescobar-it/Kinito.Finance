import json
from prettytable import PrettyTable

from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class IndexFund(AbstractStockFund):

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__(c_name.replace(' ', ''), q_type)
        self.__ticker = t_name
        self.__class = 'Index'
        #self.__quote_type = q_type
        #
        #
        self._setInfo()

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
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
        s = pt.__str__() + "\n\nSECTOR DATAFRAME\n" + self._sector_df.head().to_string(index=True)
        s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.head().to_string(index=True)
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
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
            "has_sectors": self._has_sectors,
            "has_holdings": self._has_holdings
        }.items()
    
    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
        #return super().to_json() self.__dict__ dict(self)

    def _setInfo(self):
        pass
