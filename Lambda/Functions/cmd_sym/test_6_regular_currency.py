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
