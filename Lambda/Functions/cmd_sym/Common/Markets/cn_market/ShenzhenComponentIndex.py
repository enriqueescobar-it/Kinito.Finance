from Common.StockType.Funds.Index.IndexFund import IndexFund


class ShenzhenComponentIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "399001.SZ") -> None:
        ticker_name: str = "399001.SZ" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Shenzhen Component' if source == 'yahoo' else ticker
        a_to_usd: float = 0.15
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
