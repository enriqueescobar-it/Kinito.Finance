from Common.StockType.Funds.Index.IndexFund import IndexFund


class SnP500Index(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^GSPC") -> None:
        ticker_name: str = "^GSPC" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'S&P 500' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
