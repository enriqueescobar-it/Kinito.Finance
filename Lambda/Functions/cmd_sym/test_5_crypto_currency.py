from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency)
print(abstractCurrency.to_json())
cryptoCurrency: CryptoCurrency = CryptoCurrency('an ethereum', 'ETH-USD', 'UNE_QUOTE')
print(cryptoCurrency)
print(cryptoCurrency.to_json())

c_Currency: CryptoCurrency = CryptoCurrency('an xrp', 'XRP-USD', 'UN_QUOTE')
print(c_Currency)
print(c_Currency.to_json())
