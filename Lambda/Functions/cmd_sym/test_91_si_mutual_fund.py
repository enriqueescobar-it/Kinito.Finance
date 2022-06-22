import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund
from Common.InfoType.StockInfo import StockInfo

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

mutual_list: list = ['HISFX', 'QASGX', 'RYVYX', 'SCATX', 'SAGAX']
count: int = 0

for mutual_item in mutual_list:
    start_t = time.time()
    print('\n============   ', mutual_item + '_info', '   ============\n')
    a_stock_info: StockInfo = StockInfo(mutual_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
