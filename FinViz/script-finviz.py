from finviz.screener import Screener as PanScreener
import datetime as PanDateTime
import os as PanOS
import os.path as PanOSPath
import pprint as PanPrint

def set_file(yahoo_date, yahoo_stock_exchange, yahoo_orderby, yahoo_csv_stocks):
	yahoo_file = 'script-finviz_' + yahoo_date + '-' + yahoo_stock_exchange + '-' + yahoo_orderby + '.csv'
	file_exists = PanOSPath.isfile(yahoo_file)
	if file_exists:
		print("+ " + yahoo_file + "\tskipping existing file")
	else: # init file
		print("+ " + yahoo_file + "\tcreating new file")
		f = open(yahoo_file, "w")
		f.write(yahoo_csv_stocks)
		f.close()

##stock_filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
#stock_filters = ['exch_nyse']
stock_filters = 'exch_nyse'
# Get the first 50 results sorted by price ascending
stock_orderby = 'price'
stock_datetim = str(PanDateTime.datetime.now().strftime('%Y%m%d'))
stock_list = PanScreener(filters = stock_filters, order = stock_orderby)
# Export the screener results to .csv
stock_csv_ = stock_list.to_csv()
PanPrint.pprint(stock_datetim)
set_file(stock_datetim, stock_filters, stock_orderby, stock_csv_)
# Create a SQLite database
#stock_list.to_sqlite()

'''for stock in stock_list[9:19]:  # Loop through 10th - 20th stocks
	print(stock['Ticker'], stock['Price']) # Print symbol and price

# Add more stock_filters
stock_list.add(stock_filters=['fa_div_high'])  # Show stocks with high dividend yield
# or just stock_list(stock_filters=['fa_div_high'])

# Print the table into the console
print(stock_list)'''
