from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'i_0', '   ============\n')
i_0: IndexFund = IndexFund('an index', 'VFX', 'UN_QUOTE')
print(i_0.to_json())
print(i_0)

print('\n============   ', 'i_1', '   ============\n')
i_1: IndexFund = IndexFund('un index', 'TNX', 'UNE_QUOTE')
print(i_1.to_json())
print(i_1)

print('\n============   ', 'index_stock_info', '   ============\n')
index_stock_info: stock_info = stock_info('VFX')
print(index_stock_info.to_json())
print(index_stock_info)
exit(111)
print(index_stock_info.CompanyName)
print(index_stock_info.QuoteType)
print(index_stock_info.ActionDataFrame.info())
print(index_stock_info.ActionDataFrame.describe())
print(index_stock_info.ActionDataFrame.columns)
print(index_stock_info.ActionDataFrame.dtypes)
print(index_stock_info.BalanceSheetDataFrame.info())
print(index_stock_info.BalanceSheetDataFrame.describe())
print(index_stock_info.BalanceSheetDataFrame.columns)
print(index_stock_info.BalanceSheetDataFrame.dtypes)
print(index_stock_info.QuarterCashflowDataFrame.info())
print(index_stock_info.QuarterCashflowDataFrame.describe())
print(index_stock_info.QuarterCashflowDataFrame.columns)
print(index_stock_info.QuarterCashflowDataFrame.dtypes)
print(index_stock_info.QuarterFinancialDataFrame.head())
print(index_stock_info.QuarterBalanceSheetDataFrame.head())
print(index_stock_info.OptionTuple)
print(index_stock_info.SplitSeries)
print(index_stock_info.SplitSeries.dtypes)
