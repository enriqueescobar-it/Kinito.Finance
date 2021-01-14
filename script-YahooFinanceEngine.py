from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine

a_ticker: str = 'GOOG'
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
