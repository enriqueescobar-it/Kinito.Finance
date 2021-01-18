from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine


tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD-B.TO']
bank_stocks = ['WFC', 'BAC', 'C']
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
commodity_futures = ['GC=F', 'SI=F', 'CL=F']
etf_stocks = ['VOO', 'VOOG', 'GINN.TO', 'VGRO.TO', 'XIT.TO']
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
us_treasuries = ['^TNX', '^IRX', '^TYX']
a_ticker: str = 'PRLAX'
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
print(abstractEngine.StockType)
