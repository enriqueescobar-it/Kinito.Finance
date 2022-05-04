from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractCurrency: AbstractCurrency = AbstractCurrency('a cy')
print(abstractCurrency)
print(abstractCurrency.to_json())

cryptoCurrency: CryptoCurrency = CryptoCurrency('an ethereum', 'ETH-USD')
print(cryptoCurrency)
print(cryptoCurrency.to_json())

c_Currency: CryptoCurrency = CryptoCurrency('an xrp', 'XRP-USD')
print(c_Currency)
print(c_Currency.to_json())
