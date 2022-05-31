from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond

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
    print('\n============   ', bond_title, '   ============\n')
    bond_stock: AbstractStockBond = AbstractStockBond(bond_compa, bond_item, bond_quote)
    print(bond_stock.to_json())
    print(bond_stock)
