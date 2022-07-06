# import the necessary packages
import argparse

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

a_stock_info: StockInfo = StockInfo(a_ticker)
print(a_stock_info.to_json())
print(a_stock_info)
exit(1)
print(a_stock_info.company_name)
print(a_stock_info.quote_type)
print(a_stock_info.stock_type)
# a_stock_info.__set_actions()
#print(a_stock_info.ActionDataFrame.head())
print(a_stock_info.dataframe_action.info())
print(a_stock_info.dataframe_action.describe())
print(a_stock_info.dataframe_action.columns)
print(a_stock_info.dataframe_action.dtypes)
#print(a_stock_info.BalanceSheetDataFrame.head())
print(a_stock_info.dataframe_balance_sheet.info())
print(a_stock_info.dataframe_balance_sheet.describe())
print(a_stock_info.dataframe_balance_sheet.columns)
print(a_stock_info.dataframe_balance_sheet.dtypes)
#print(a_stock_info.QuarterCashflowDataFrame.head())
#print(a_stock_info.QuarterBalanceSheetDataFrame.head())
print(a_stock_info.tuple_option)
# a_stock_info.__set_splits()
print(a_stock_info.series_split)
print(a_stock_info.series_split.dtypes)
