from Common.StockType.Funds.Index.IndexFund import IndexFund


class DaxPerformanceIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^GDAXI") -> None:
        ticker_name: str = "^GDAXI" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'DAXPERFORMANCE_INDEX' if source == 'yahoo' else ticker
        a_to_usd: float = 0.75
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
