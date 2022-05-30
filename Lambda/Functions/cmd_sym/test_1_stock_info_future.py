from Common.InfoType.stock_info import stock_info

print('\n============   ', 'future_stock_info', '   ============\n')
future_stock_info: stock_info = stock_info('GC=F')
print(future_stock_info.to_json())
print(future_stock_info)

print('\n============   ', 'f_stock_info', '   ============\n')
f_stock_info: stock_info = stock_info('SI=F')
print(f_stock_info.to_json())
print(f_stock_info)

print('\n============   ', 'fstock_info', '   ============\n')
fstock_info: stock_info = stock_info('CL=F')
print(fstock_info.to_json())
print(fstock_info)
