from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency)
print(abstractCurrency.to_json())
print(abstractCurrency.SectorDataFrame)
print(abstractCurrency.HoldingDataFrame)

regularCurrency: RegularCurrency = RegularCurrency('a japan', 'JPY=X', 'UN_QUOTE')
print(regularCurrency)
print(regularCurrency.to_json())
print(regularCurrency.SectorDataFrame)
print(regularCurrency.HoldingDataFrame)

r_Currency: RegularCurrency = RegularCurrency('a canada', 'CDN=X', 'UNE_QUOTE')
print(r_Currency)
print(r_Currency.to_json())
print(regularCurrency.SectorDataFrame)
print(regularCurrency.HoldingDataFrame)
