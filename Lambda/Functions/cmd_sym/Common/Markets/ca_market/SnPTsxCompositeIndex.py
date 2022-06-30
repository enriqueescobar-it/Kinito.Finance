from Common.StockType.Funds.Index.IndexFund import IndexFund


class SnPTsxCompositeIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^GSPTSE") -> None:
        ticker_name: str = "^GSPTSE" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'S&P/TSX Composite index' if source == 'yahoo' else ticker
        a_to_usd: float = 1.15
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
