import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency
from Common.InfoType.stock_info import stock_info

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractCurrency', '   ============\n')
abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency.to_json())
print(abstractCurrency)

regular_currency_list: list = ['COP=X', 'CAD=X', 'JPY=X', 'RUB=X']
count: int = 0

for regular_currency_item in regular_currency_list:
    start_t = time.time()
    print('\n============   ', regular_currency_item + '_info', '   ============\n')
    a_stock_info: stock_info = stock_info(regular_currency_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
