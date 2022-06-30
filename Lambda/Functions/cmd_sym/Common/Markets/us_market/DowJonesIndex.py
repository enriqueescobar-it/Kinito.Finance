from Common.StockType.Funds.Index.IndexFund import IndexFund


class DowJonesIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^DJI") -> None:
        ticker_name: str = "^DJI" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Dow Jones Industrial Average' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
