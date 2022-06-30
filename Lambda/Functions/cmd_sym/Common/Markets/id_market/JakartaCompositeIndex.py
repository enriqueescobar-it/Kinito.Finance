from Common.StockType.Funds.Index.IndexFund import IndexFund


class JakartaCompositeIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^JKSE") -> None:
        ticker_name: str = "^JKSE" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Jakarta Composite Index' if source == 'yahoo' else ticker
        a_to_usd: float = 0.000067
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
