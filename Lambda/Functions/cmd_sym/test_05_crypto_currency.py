from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractCurrency', '   ============\n')
abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency.to_json())
print(abstractCurrency)

print('\n============   ', 'cryptoCurrency', '   ============\n')
cryptoCurrency: CryptoCurrency = CryptoCurrency('an ethereum', 'ETH-USD', 'UNE_QUOTE')
print(cryptoCurrency.to_json())
print(cryptoCurrency)

print('\n============   ', 'c_Currency', '   ============\n')
c_Currency: CryptoCurrency = CryptoCurrency('an xrp', 'XRP-USD', 'UN_QUOTE')
print(c_Currency.to_json())
print(c_Currency)
