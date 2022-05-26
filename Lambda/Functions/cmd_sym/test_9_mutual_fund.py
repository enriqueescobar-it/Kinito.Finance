from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'mf_0', '   ============\n')
mf_0: MutualFund = MutualFund('a mutual', 'QASGX', 'UN_QUOTE')
print(mf_0.to_json())
print(mf_0)

print('\n============   ', 'mf_1', '   ============\n')
mf_1: MutualFund = MutualFund('un mutual', 'HISFX', 'UNE_QUOTE')
print(mf_1.to_json())
print(mf_1)

print('\n============   ', 'mutual_stock_info', '   ============\n')
mutual_stock_info: stock_info = stock_info('QASGX')
print(mutual_stock_info.to_json())
print(mutual_stock_info)
print(mutual_stock_info.CompanyName)
print(mutual_stock_info.QuoteType)
print(mutual_stock_info.ActionDataFrame.info())
print(mutual_stock_info.ActionDataFrame.describe())
print(mutual_stock_info.ActionDataFrame.columns)
print(mutual_stock_info.ActionDataFrame.dtypes)
print(mutual_stock_info.BalanceSheetDataFrame.info())
print(mutual_stock_info.BalanceSheetDataFrame.describe())
print(mutual_stock_info.BalanceSheetDataFrame.columns)
print(mutual_stock_info.BalanceSheetDataFrame.dtypes)
print(mutual_stock_info.QuarterCashflowDataFrame.info())
print(mutual_stock_info.QuarterCashflowDataFrame.describe())
print(mutual_stock_info.QuarterCashflowDataFrame.columns)
print(mutual_stock_info.QuarterCashflowDataFrame.dtypes)
print(mutual_stock_info.QuarterFinancialDataFrame.head())
print(mutual_stock_info.QuarterBalanceSheetDataFrame.head())
print(mutual_stock_info.OptionTuple)
print(mutual_stock_info.SplitSeries)
print(mutual_stock_info.SplitSeries.dtypes)
