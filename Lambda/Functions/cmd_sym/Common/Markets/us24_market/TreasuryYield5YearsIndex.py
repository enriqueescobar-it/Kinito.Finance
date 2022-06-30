from Common.StockType.Funds.Index.IndexFund import IndexFund


class TreasuryYield5YearsIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^FVX") -> None:
        ticker_name: str = "^FVX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Treasury Yield 5 Years' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
