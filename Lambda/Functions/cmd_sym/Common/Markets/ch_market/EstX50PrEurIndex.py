from Common.StockType.Funds.Index.IndexFund import IndexFund


class EstX50PrEurIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^STOXX50E") -> None:
        ticker_name: str = "^STOXX50E" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'ESTX 50 PR.EUR' if source == 'yahoo' else ticker
        a_to_usd: float = 0.75
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
