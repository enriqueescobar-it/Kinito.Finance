import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.InfoType.stock_info import stock_info

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

equity_list: list = ['AAPL', 'AMZN', 'MSFT', 'GOOG']
count: int = 0

for equity_item in equity_list:
    start_t = time.time()
    print('\n============   ', equity_item + '_info', '   ============\n')
    a_stock_info: stock_info = stock_info(equity_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
