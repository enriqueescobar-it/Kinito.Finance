import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture
from Common.InfoType.StockInfo import StockInfo

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

future_list: list = ['CL=F', 'GC=F', 'SI=F', 'ES=F', 'YM=F', 'NQ=F', 'RTY=F']
count: int = 0

for future_item in future_list:
    start_t = time.time()
    print('\n============   ', future_item + '_info', '   ============\n')
    a_stock_info: StockInfo = StockInfo(future_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
