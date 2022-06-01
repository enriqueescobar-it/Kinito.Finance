from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture
from Common.InfoType.stock_info import stock_info

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)
#'CL=F', 'GC=F', 'SI=F', 'ES=F',
future_list: list = ['YM=F', 'NQ=F', 'RTY=F']
count: int = 0

for future_item in future_list:
    print("==========", count, "==========")
    future_title: str = "futureStock_" + future_item
    future_compa: str = "company " + str(count)
    future_quote: str = "quote_" + str(count)
    print('\n============   ', future_title, '   ============\n')
    future_stock: AbstractStockFuture = AbstractStockFuture(future_compa, future_item, future_quote)
    print(future_stock.to_json())
    print(future_stock)
    print('\n============   ', future_title + "_info", '   ============\n')
    stock_info: stock_info = stock_info(future_item)
    print(stock_info.to_json())
    print(stock_info)
    count = count + 1
