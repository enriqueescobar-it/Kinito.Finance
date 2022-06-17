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
        pt.add_row(['QuoteSourceName', self._quote_src_name])
        pt.add_row(['UUID', self._uuid])
        pt.add_row(['UnderlyingSymbol', self._underlying_s])
        pt.add_row(['Symbol', self._symbol])
        pt.add_row(['Currency', self._currency])
        pt.add_row(['CurrencySymbol', self._currency_symbol])
        pt.add_row(['Exchange', self._exchange])
        pt.add_row(['ExchangeName', self._exchange_name])
        pt.add_row(['ExchangeDateTime', self._exchange_dt])
        pt.add_row(['TZ', self._t_z])
        pt.add_row(['Industry', self._industry])
        pt.add_row(['Sector', self._sector])
        pt.add_row(['EmployeeCount', self._employee_count])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPartCount', self._stock_part_count])
        pt.add_row(['BondPartCount', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['Open', self._open])
        pt.add_row(['High', self._high])
        pt.add_row(['Low', self._low])
        pt.add_row(['Close', self._close])
        pt.add_row(['High52Week', self._high_52week])
        pt.add_row(['Low52Week', self._low_52week])
        pt.add_row(['Mean52Week', self._mean_52week])
        pt.add_row(['Mean200Days', self._mean_200day])
        pt.add_row(['HasSectorDf', self._has_sector_df])
        pt.add_row(['HasHoldingDf', self._has_holding_df])
        pt.add_row(['HasKeyStatDict', self._has_key_stat_dict])
        pt.add_row(['HasFinancialDataDict', self._has_financial_data_dict])
        pt.add_row(['HasPriceDict', self._has_price_dict])
        pt.add_row(['HasQuoteTypeDict', self._has_quote_type_dict])
        pt.add_row(['HasSummaryDetailDict', self._has_summary_detail_dict])
        pt.add_row(['HasSummaryProfileDict', self._has_summary_profile_dict])
        s = pt.__str__()
        if self._has_sector_df:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.head().to_string(index=True)
        if self._has_holding_df:
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
            "quote_src_name": self._quote_src_name,
            "uuid": self._uuid,
            "underlying_symbol": self._underlying_s,
            "symbol": self._symbol,
            "currency": self._currency,
            "currency_symbol": self._currency_symbol,
            "exchange": self._exchange,
            "exchange_name": self._exchange_name,
            "exchange_dt": self._exchange_dt,
            "t_z": self._t_z,
            "industry": self._industry,
            "sector": self._sector,
            "employee_count": self._employee_count,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "cash_percent": self._cash_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
            "open": self._open,
            "high": self._high,
            "low": self._low,
            "close": self._close,
            "high_52week": self._high_52week,
            "low_52week": self._low_52week,
            "mean_52week": self._mean_52week,
            "mean_200day": self._mean_200day,
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
