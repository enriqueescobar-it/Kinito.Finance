from Common.StockType.Funds.Index.IndexFund import IndexFund


class SnPClxIpsaIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^IPSA") -> None:
        ticker_name: str = "^IPSA" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'S&P/CLX IPSA' if source == 'yahoo' else ticker
        a_to_usd: float = 0.0011
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
