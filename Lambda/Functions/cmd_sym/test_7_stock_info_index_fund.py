from Common.InfoType.stock_info import stock_info

print('\n============   ', 'index_stock_info', '   ============\n')
index_stock_info: stock_info = stock_info('VFX')
print(index_stock_info.to_json())
print(index_stock_info)

print('\n============   ', 'i_stock_info', '   ============\n')
i_stock_info: stock_info = stock_info('TNX')
print(i_stock_info.to_json())
print(i_stock_info)
