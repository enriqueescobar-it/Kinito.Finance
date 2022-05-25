from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

print('\n============   ', 'abstractCurrency', '   ============\n')
abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency)
print(abstractCurrency.to_json())

print('\n============   ', 'cryptoCurrency', '   ============\n')
cryptoCurrency: CryptoCurrency = CryptoCurrency('an ethereum', 'ETH-USD', 'UNE_QUOTE')
print(cryptoCurrency)
print(cryptoCurrency.to_json())

print('\n============   ', 'c_Currency', '   ============\n')
c_Currency: CryptoCurrency = CryptoCurrency('an xrp', 'XRP-USD', 'UN_QUOTE')
print(c_Currency)
print(c_Currency.to_json())

print('\n============   ', 'crypto_stock_info', '   ============\n')
crypto_stock_info: stock_info = stock_info('ETH-USD')
print(crypto_stock_info)
print(crypto_stock_info.to_json())
print(crypto_stock_info.CompanyName)
print(crypto_stock_info.QuoteType)
print(crypto_stock_info.StockType)
print(crypto_stock_info.ActionDataFrame.info())
print(crypto_stock_info.ActionDataFrame.describe())
print(crypto_stock_info.ActionDataFrame.columns)
print(crypto_stock_info.ActionDataFrame.dtypes)
print(crypto_stock_info.BalanceSheetDataFrame.info())
print(crypto_stock_info.BalanceSheetDataFrame.describe())
print(crypto_stock_info.BalanceSheetDataFrame.columns)
print(crypto_stock_info.BalanceSheetDataFrame.dtypes)
print(crypto_stock_info.QuarterCashflowDataFrame.info())
print(crypto_stock_info.QuarterCashflowDataFrame.describe())
print(crypto_stock_info.QuarterCashflowDataFrame.columns)
print(crypto_stock_info.QuarterCashflowDataFrame.dtypes)
print(crypto_stock_info.QuarterFinancialDataFrame.head())
print(crypto_stock_info.QuarterBalanceSheetDataFrame.head())
print(crypto_stock_info.OptionTuple)
print(crypto_stock_info.SplitSeries)
print(crypto_stock_info.SplitSeries.dtypes)
