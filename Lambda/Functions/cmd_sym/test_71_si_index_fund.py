import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund
from Common.InfoType.StockInfo import StockInfo

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

index_list: list = ['^SOX', '^GSPC', '^VIX', '^SKEW', '^GSPTSE', '^IXIC', '^NDX', '^NYA', '^DJI', '^TNX', '^TYX', '^W5000']
count: int = 0

for index_item in index_list:
    start_t = time.time()
    print('\n============   ', index_item + '_info', '   ============\n')
    a_stock_info: StockInfo = StockInfo(index_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
