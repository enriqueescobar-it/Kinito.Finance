from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractCurrency', '   ============\n')
abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency.to_json())
print(abstractCurrency)

print('\n============   ', 'regularCurrency', '   ============\n')
regularCurrency: RegularCurrency = RegularCurrency('a japan', 'JPY=X', 'UN_QUOTE')
print(regularCurrency.to_json())
print(regularCurrency)

print('\n============   ', 'r_Currency', '   ============\n')
r_Currency: RegularCurrency = RegularCurrency('a canada', 'CDN=X', 'UNE_QUOTE')
print(r_Currency.to_json())
print(r_Currency)

print('\n============   ', 'currency_stock_info', '   ============\n')
currency_stock_info: stock_info = stock_info('CDN=X')
print(currency_stock_info.to_json())
print(currency_stock_info)
exit(111)
print(currency_stock_info.CompanyName)
print(currency_stock_info.QuoteType)
print(currency_stock_info.ActionDataFrame.info())
#print(currency_stock_info.ActionDataFrame.describe())
print(currency_stock_info.ActionDataFrame.columns)
print(currency_stock_info.ActionDataFrame.dtypes)
print(currency_stock_info.BalanceSheetDataFrame.info())
print(currency_stock_info.BalanceSheetDataFrame.describe())
print(currency_stock_info.BalanceSheetDataFrame.columns)
print(currency_stock_info.BalanceSheetDataFrame.dtypes)
print(currency_stock_info.QuarterCashflowDataFrame.info())
print(currency_stock_info.QuarterCashflowDataFrame.describe())
print(currency_stock_info.QuarterCashflowDataFrame.columns)
print(currency_stock_info.QuarterCashflowDataFrame.dtypes)
print(currency_stock_info.QuarterFinancialDataFrame.head())
print(currency_stock_info.QuarterBalanceSheetDataFrame.head())
print(currency_stock_info.OptionTuple)
print(currency_stock_info.SplitSeries)
print(currency_stock_info.SplitSeries.dtypes)
