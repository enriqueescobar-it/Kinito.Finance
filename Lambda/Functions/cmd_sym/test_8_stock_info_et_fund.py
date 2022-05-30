from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'etf_0', '   ============\n')
etf_0: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOO', 'UN_QUOTE')
print(etf_0.to_json())
print(etf_0)

print('\n============   ', 'etf_1', '   ============\n')
etf_1: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOOG', 'UNE_QUOTE')
print(etf_1.to_json())
print(etf_1)

print('\n============   ', 'etf_stock_info', '   ============\n')
etf_stock_info: stock_info = stock_info('VOO')
print(etf_stock_info.to_json())
print(etf_stock_info)
exit(111)
print(etf_stock_info.CompanyName)
print(etf_stock_info.QuoteType)
print(etf_stock_info.ActionDataFrame.info())
print(etf_stock_info.ActionDataFrame.describe())
print(etf_stock_info.ActionDataFrame.columns)
print(etf_stock_info.ActionDataFrame.dtypes)
print(etf_stock_info.BalanceSheetDataFrame.info())
print(etf_stock_info.BalanceSheetDataFrame.describe())
print(etf_stock_info.BalanceSheetDataFrame.columns)
print(etf_stock_info.BalanceSheetDataFrame.dtypes)
print(etf_stock_info.QuarterCashflowDataFrame.info())
print(etf_stock_info.QuarterCashflowDataFrame.describe())
print(etf_stock_info.QuarterCashflowDataFrame.columns)
print(etf_stock_info.QuarterCashflowDataFrame.dtypes)
print(etf_stock_info.QuarterFinancialDataFrame.head())
print(etf_stock_info.QuarterBalanceSheetDataFrame.head())
print(etf_stock_info.OptionTuple)
print(etf_stock_info.SplitSeries)
print(etf_stock_info.SplitSeries.dtypes)