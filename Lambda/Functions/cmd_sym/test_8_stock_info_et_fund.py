from Common.InfoType.stock_info import stock_info

print('\n============   ', 'etf_stock_info', '   ============\n')
etf_stock_info: stock_info = stock_info('VOO')
print(etf_stock_info.to_json())
print(etf_stock_info)

print('\n============   ', 'e_stock_info', '   ============\n')
e_stock_info: stock_info = stock_info('VOOG')
print(e_stock_info.to_json())
print(e_stock_info)
