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

regular_currency_list: list = ['COP=X', 'CAD=X']
count: int = 0

for regular_currency_item in regular_currency_list:
    regular_currency_title: str = "regular_currency_stock_" + regular_currency_item
    regular_currency_compa: str = "company " + str(count)
    regular_currency_quote: str = "quote_" + str(count)
    print('\n============   ', regular_currency_title, '   ============\n')
    regular_currency_stock: RegularCurrency = RegularCurrency(regular_currency_compa, regular_currency_item, regular_currency_quote)
    print(regular_currency_stock.to_json())
    print(regular_currency_stock)
