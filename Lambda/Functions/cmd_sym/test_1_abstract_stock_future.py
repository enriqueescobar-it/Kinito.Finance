from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

futureStock: AbstractStockFuture = AbstractStockFuture('una cia', 'GC=F', 'A_QUOTE')
print(futureStock)
print(futureStock.to_json())

fStock: AbstractStockFuture = AbstractStockFuture('une cie', 'SI=F', 'UNA_QUOTE')
print(fStock)
print(fStock.to_json())

f_Stock: AbstractStockFuture = AbstractStockFuture('a cy', 'CL=F', 'UNE_QUOTE')
print(f_Stock)
print(f_Stock.to_json())
