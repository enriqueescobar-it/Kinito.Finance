from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'futureStock', '   ============\n')
futureStock: AbstractStockFuture = AbstractStockFuture('una cia', 'GC=F', 'A_QUOTE')
print(futureStock.to_json())
print(futureStock)

print('\n============   ', 'fStock', '   ============\n')
fStock: AbstractStockFuture = AbstractStockFuture('une cie', 'SI=F', 'UNA_QUOTE')
print(fStock.to_json())
print(fStock)

print('\n============   ', 'f_Stock', '   ============\n')
f_Stock: AbstractStockFuture = AbstractStockFuture('a cy', 'CL=F', 'UNE_QUOTE')
print(f_Stock.to_json())
print(f_Stock)
