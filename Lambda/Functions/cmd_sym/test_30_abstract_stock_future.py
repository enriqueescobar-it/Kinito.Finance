from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

future_list: list = ['CL=F', 'GC=F', 'SI=F', 'ES=F', 'YM=F', 'NQ=F', 'RTY=F']
count: int = 0

for future_item in future_list:
    future_title: str = "futureStock_" + future_item
    future_compa: str = "company " + str(count)
    future_quote: str = "quote_" + str(count)
    print('\n============   ', future_title, '   ============\n')
    future_stock: AbstractStockFuture = AbstractStockFuture(future_compa, future_item, future_quote)
    print(future_stock.to_json())
    print(future_stock)
    count = count + 1
