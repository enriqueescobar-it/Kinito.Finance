import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond
from Common.InfoType.stock_info import stock_info

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

bond_list: list = ['BOND', 'BAND']
count: int = 0

for bond_item in bond_list:
    bond_title: str = "bond_stock_" + bond_item
    bond_compa: str = "company " + str(count)
    bond_quote: str = "quote_" + str(count)
    start_t = time.time()
    print('\n============   ', bond_title, '   ============\n')
    bond_stock: AbstractStockBond = AbstractStockBond(bond_compa, bond_item, bond_quote)
    print(bond_stock.to_json())
    print(bond_stock)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)

print('\n============   ', bond_list[0] + "_info", '   ============\n')
stock_info: stock_info = stock_info(bond_list[0])
print(stock_info.to_json())
print(stock_info)