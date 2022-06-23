# import the necessary packages
import argparse

from Common.InfoType.QuarterInfo import QuarterInfo
from Common.InfoType.StockInfo import StockInfo
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))
# bonds: bond_funds = ['UDN', 'NEAR']
# tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD.TO', 'ATD-B.TO']#!
# bank_stocks = ['WFC', 'BAC', 'C']#~extend EQUITY
# cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']#! #~extend
# currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']#! #~extend
# commodity_futures = ['GC=F', 'SI=F', 'CL=F']#! #~extend
# funds: etf_stocks = ['VOO', 'VOOG', 'GINN', 'VGRO.TO', 'XIT.TO']#! #~extend
# funds: mutual_funds = ['PRLAX', 'QASGX', 'HISFX']#! #~extend
# funds: us_treasuries = ['^TNX', '^IRX', '^TYX', '^VIX']#! #~extend
# a_ticker: str = '^TNX'#
a_ticker: str = args["symbol"]
q_i: QuarterInfo = QuarterInfo()
print(q_i.to_json())
print(q_i)
exit(-1)
a_stock_info: StockInfo = StockInfo(a_ticker)
print(a_stock_info.to_json())
print(a_stock_info)
exit(1)
print(a_stock_info.CompanyName)
print(a_stock_info.QuoteType)
print(a_stock_info.StockType)
# a_stock_info.__set_actions()
#print(a_stock_info.ActionDataFrame.head())
print(a_stock_info.ActionDataFrame.info())
print(a_stock_info.ActionDataFrame.describe())
print(a_stock_info.ActionDataFrame.columns)
print(a_stock_info.ActionDataFrame.dtypes)
#print(a_stock_info.BalanceSheetDataFrame.head())
print(a_stock_info.BalanceSheetDataFrame.info())
print(a_stock_info.BalanceSheetDataFrame.describe())
print(a_stock_info.BalanceSheetDataFrame.columns)
print(a_stock_info.BalanceSheetDataFrame.dtypes)
#print(a_stock_info.QuarterCashflowDataFrame.head())
print(a_stock_info.QuarterCashflowDataFrame.info())
print(a_stock_info.QuarterCashflowDataFrame.describe())
print(a_stock_info.QuarterCashflowDataFrame.columns)
print(a_stock_info.QuarterCashflowDataFrame.dtypes)
#print(a_stock_info.QuarterBalanceSheetDataFrame.head())
print(a_stock_info.QuarterBalanceSheetDataFrame.info())
print(a_stock_info.QuarterBalanceSheetDataFrame.describe())
print(a_stock_info.QuarterBalanceSheetDataFrame.columns)
print(a_stock_info.QuarterBalanceSheetDataFrame.dtypes)
print(a_stock_info.OptionTuple)
# a_stock_info.__set_splits()
print(a_stock_info.SplitSeries)
print(a_stock_info.SplitSeries.dtypes)
