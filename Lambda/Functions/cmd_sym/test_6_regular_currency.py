from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractCurrency: AbstractCurrency = AbstractCurrency('a cy')
print(abstractCurrency)
print(abstractCurrency.to_json())

regularCurrency: RegularCurrency = RegularCurrency('a japan', 'JPY=X')
print(regularCurrency)
print(regularCurrency.to_json())

r_Currency: RegularCurrency = RegularCurrency('a canada', 'CDN=X')
print(r_Currency)
print(r_Currency.to_json())
