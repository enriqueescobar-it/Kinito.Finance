from Common.InfoType.stock_info import stock_info

print('\n============   ', 'mutual_stock_info', '   ============\n')
mutual_stock_info: stock_info = stock_info('QASGX')
print(mutual_stock_info.to_json())
print(mutual_stock_info)

print('\n============   ', 'm_stock_info', '   ============\n')
m_stock_info: stock_info = stock_info('HISFX')
print(m_stock_info.to_json())
print(m_stock_info)
