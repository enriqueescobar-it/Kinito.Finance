from finviz.screener import Screener as PanScreener
from yahoofinancials import YahooFinancials as PanYahooFinancial
import datetime as PanDateTime
import os as PanOS
import os.path as PanOSPath
import pandas as Pan
import pprint as PanPrint

def set_directory(yahoo_directory):
    if not PanOS.path.exists(yahoo_directory):
        PanPrint.pprint("+ " + yahoo_directory + "\tcreating new directory")
        PanOS.makedirs(yahoo_directory)


def set_file(yahoo_date, yahoo_stock_exchange, yahoo_orderby, yahoo_csv_stocks):
    yahoo_date = PanOSPath.join('FinViz', yahoo_date)
    set_directory(yahoo_date)
    yahoo_file = 'script-FinViz-' + yahoo_stock_exchange + '-' + yahoo_orderby + '.csv'
    yahoo_file = PanOSPath.join(yahoo_date, yahoo_file)
    file_exists = PanOSPath.isfile(yahoo_file)
    if file_exists:
        PanPrint.pprint("+ " + yahoo_file + "\tskipping existing file")
    else:  # init file
        PanPrint.pprint("+ " + yahoo_file + "\tcreating new file")
        f = open(yahoo_file, "w")
        f.write(yahoo_csv_stocks.replace('\r\n', '\n'))
        f.close()
    return yahoo_file


##stock_filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
# stock_filters = ['exch_nyse']
stock_filters = 'exch_nyse'
# Get the first 50 results sorted by price ascending
stock_orderby = 'pe'  # 'pe'  'price'
stock_datetim = str(PanDateTime.datetime.now().strftime('%Y%m%d'))
stock_list = PanScreener(filters=stock_filters, order=stock_orderby)
stock_csv_ = stock_list.to_csv()
stock_file = set_file(stock_datetim, stock_filters, stock_orderby, stock_csv_)
PanPrint.pprint(stock_file)
dtype_dic= { 'No.':'int64', 'Ticker':'str', 'Company':'str', 'Sector':'str', 'Industry':'str', 'Country':'str',
             'Market Cap':'str', 'P/E':'float64', 'Price':'float64', 'Change':'str', 'Volume':'float64'}
myDf = Pan.read_csv(stock_file, keep_default_na = False, dtype = {'Volume' : 'str'})
myDf = myDf.loc[myDf['P/E'] != '-']
myDf = myDf.loc[myDf['Market Cap'] != '-']
myDf['Volume'] = myDf['Volume'].str.replace(',', '')
myDf['Market Cap'] = (myDf['Market Cap'].replace(r'[KMB]+$', '', regex=True).astype(float) * myDf['Market Cap'].str.extract(r'[\d\.]+([KMB]+)', expand=False).fillna(1).replace(['K','M', 'B'], [10**3, 10**6, 10**9]).astype(int))
myDf = myDf.astype({'Market Cap' : 'int64' , 'P/E':'float64', 'Price':'float64', 'Volume': 'int64'})
PanPrint.pprint(myDf.head())
PanPrint.pprint(myDf.dtypes)
PanPrint.pprint(myDf.info())
PanPrint.pprint(myDf['P/E'].describe(include='all'))
PanPrint.pprint(myDf['Price'].describe(include='all'))
PanPrint.pprint(myDf['Volume'].describe(include='all'))
PanPrint.pprint(str(type(myDf['Ticker'].tolist())))
#PanPrint.pprint(PanYahooFinancial(tickerList).get_exdividend_date())
#PanPrint.pprint(PanYahooFinancial('TUP').get_exdividend_date())
myDf.to_csv(stock_file, header=True, index=False, sep=';', mode='w+', encoding='utf-8')
exit(11)
# Create a SQLite database
# PanPrint.pprint(str(type(stock_list.to_sqlite('script-finviz.sqlite'))))
# Loop through 10th - 20th stocks
for stock in stock_list[9:19]:
    # Print symbol and price
    PanPrint.pprint(stock['Ticker'], stock['Price'])

# Add more stock_filters
# Show stocks with high dividend yield
#stock_list.add(stock_filters = ['fa_div_high'])
# or just
#stock_list(stock_filters=['fa_div_high'])
exit(12)
# Print the table into the console
# print(stock_list)
'''FUNDAMENTAL PEratio low < 15
DESCRIPTIVE Dividend Yield very high > 10%
			Average Volume > over 200K'''