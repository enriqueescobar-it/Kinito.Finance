# import the necessary packages
import argparse
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))

#
# bonds: bond_funds = ['UDN', 'NEAR']
# tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD.TO', 'ATD-B.TO']#!
# bank_stocks = ['WFC', 'BAC', 'C']#~extend EQUITY
# cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']#! #~extend
# currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']#! #~extend
# commodity_futures = ['GC=F', 'SI=F', 'CL=F']#! #~extend
# funds: us_treasuries = ['^TNX', '^IRX', '^TYX']#! #~extend
# funds: etf_stocks = ['VOO', 'VOOG', 'GINN', 'VGRO.TO', 'XIT.TO']#! #~extend
# funds: mutual_funds = ['PRLAX', 'QASGX', 'HISFX']#! #~extend
# a_ticker: str = '^TNX'#
a_ticker: str = args["symbol"]
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print('QuoteType: ' + abstractEngine.QuoteType)
print(abstractEngine.InfoLabels)
print(abstractEngine.InfoList)
print(abstractEngine)
print(abstractEngine.StockType)
print(abstractEngine.StockType.to_json())
print(abstractEngine.StockType.InfoLabels)
print(abstractEngine.StockType.InfoList)
print(abstractEngine.StockType.price_to_earnings)
print(abstractEngine.StockType.price_to_book)
print(abstractEngine.StockType.price_to_sales)
print(abstractEngine.StockType.PriceToCashflow)
print(abstractEngine.StockType.SectorDataFrame)
print(abstractEngine.StockType.HoldingDataFrame)
