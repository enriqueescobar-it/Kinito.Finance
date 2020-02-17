from finviz.screener import Screener as PanScreener
import datetime as PanDateTime
import os as PanOS
import os.path as PanOSPath
import pprint as PanPrint


def set_directory(yahoo_directory):
    if not PanOS.path.exists(yahoo_directory):
        print("+ " + yahoo_directory + "\tcreating new directory")
        PanOS.makedirs(yahoo_directory)


def set_file(yahoo_date, yahoo_stock_exchange, yahoo_orderby, yahoo_csv_stocks):
    set_directory(yahoo_date)
    yahoo_file = 'script-finviz-' + yahoo_stock_exchange + '-' + yahoo_orderby + '.csv'
    yahoo_file = PanOSPath.join(yahoo_date, yahoo_file)
    file_exists = PanOSPath.isfile(yahoo_file)
    if file_exists:
        print("+ " + yahoo_file + "\tskipping existing file")
    else:  # init file
        print("+ " + yahoo_file + "\tcreating new file")
        f = open(yahoo_file, "w")
        f.write(yahoo_csv_stocks)
        f.close()


##stock_filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
# stock_filters = ['exch_nyse']
stock_filters = 'exch_nyse'
# Get the first 50 results sorted by price ascending
stock_orderby = 'pe'  # 'price'
stock_datetim = str(PanDateTime.datetime.now().strftime('%Y%m%d'))
stock_list = PanScreener(filters=stock_filters, order=stock_orderby)
# Export the screener results to .csv
stock_csv_ = stock_list.to_csv()
# stock_csv_ = stock_csv_.replace(',-,', ',NA,')
PanPrint.pprint(stock_datetim)
set_file(stock_datetim, stock_filters, stock_orderby, stock_csv_)
# Create a SQLite database
# PanPrint.pprint(str(type(stock_list.to_sqlite('script-finviz.sqlite'))))
# Loop through 10th - 20th stocks
for stock in stock_list[9:19]:
    # Print symbol and price
    print(stock['Ticker'], stock['Price'])

# Add more stock_filters
# Show stocks with high dividend yield
# stock_list.add(stock_filters = ['fa_div_high'])
# or just stock_list(stock_filters=['fa_div_high'])

# Print the table into the console
# print(stock_list)
