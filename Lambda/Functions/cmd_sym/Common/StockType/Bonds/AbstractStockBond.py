from matplotlib import pyplot as plt
from prettytable import PrettyTable
from yahooquery import Ticker

#
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockBond(AbstractStock):
    __ticker: str = 'NA'
    #
    #

    def __init__(self, c_name: str, t_name: str, q_type: str):
        super().__init__()
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Bond'
        self._quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
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
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
        s = pt.__str__()
        if self._has_sectors:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.to_string(index=True)
        if self._has_holdings:
            s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.to_string(index=True)
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
            "has_holdings": self._has_holdings
        }.items()

    def _setInfo(self):
        self._set_sector_df(self.__y_query.fund_sector_weightings)
        self._set_holding_df(self.__y_query.fund_top_holdings, self.__ticker, self.__y_query.fund_sector_weightings)
        self._set_part_count(self.__y_query.fund_top_holdings, self.__y_query.fund_category_holdings)
        self._set_fund_holding_info(self.__y_query.fund_holding_info, self.__ticker)
        self.__setPerformance()
        self.__plotSectorDf()#.show()

    def __plotSectorDf(self) -> plt:
        if (self._sector_df['Percent'] != self._sector_df['Percent'][0]).all():
            self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                    autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                    title='Sector Distribution ' + self.__ticker + ' ' + self.__class)
            return plt

    def __setPerformance(self):
        if not self._is_any_null(self.__y_query.fund_performance, self.__ticker):
            for key in self.__y_query.fund_performance.get(self.__ticker):
                print("+", self.__class__.__name__, ':', key)
