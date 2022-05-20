from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund)
print(abstractStockFund.to_json())
print(abstractStockFund.SectorDataFrame)
print(abstractStockFund.HoldingDataFrame)

print('\n============   ', 'i_0', '   ============\n')
i_0: IndexFund = IndexFund('an index', 'VFX', 'UN_QUOTE')
print(i_0)
print(i_0.to_json())
print(i_0.SectorDataFrame)
print(i_0.HoldingDataFrame)

print('\n============   ', 'i_1', '   ============\n')
i_1: IndexFund = IndexFund('un index', 'TNX', 'UNE_QUOTE')
print(i_1)
print(i_1.to_json())
print(i_1.SectorDataFrame)
print(i_1.HoldingDataFrame)

print('\n============   ', 'index_stock_info', '   ============\n')
index_stock_info: stock_info = stock_info('VFX')
print(index_stock_info)
print(index_stock_info.to_json())
print(index_stock_info.CompanyName)
print(index_stock_info.QuoteType)
print(index_stock_info.StockType)
index_stock_info.set_actions()
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
index_stock_info.set_splits()
print(index_stock_info.SplitSeries)
print(index_stock_info.SplitSeries.dtypes)
