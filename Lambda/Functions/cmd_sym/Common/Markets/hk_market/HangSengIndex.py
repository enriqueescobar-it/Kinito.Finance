from Common.StockType.Funds.Index.IndexFund import IndexFund


class HangSengIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^HSI") -> None:
        ticker_name: str = "^HSI" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'HANG SENG INDEX' if source == 'yahoo' else ticker
        a_to_usd: float = 0.13
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
