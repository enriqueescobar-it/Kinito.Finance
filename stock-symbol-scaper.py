###

import pandas as pd
import datetime as dateTime

tgt_url_ = 'https://www.nasdaq.com/market-activity/stocks/screener?letter=A&render=download'
tgt_start = dateTime.datetime(2019, 1, 1)
tgt_stop_ = dateTime.datetime.now()

tgt_read = pd.read_csv(tgt_url_)
stock_symbol_list = tgt_read.Symbol.tolist()

###

import pandas as pd
import datetime as dateTime

tgt_website = r'https://ca.finance.yahoo.com/quote/WDC/key-statistics?p=WDC'
tgt_start = dateTime.datetime(2019, 1, 1)
tgt_stop_ = dateTime.datetime.now()

def get_key_stats(tgt_website):

    # The web page is make up of several html table. By calling read_html function.
    # all the tables are retrieved in dataframe format.
    # Next is to append all the table and transpose it to give a nice one row data.
    html_read = pd.read_html(tgt_website)
    html_head = html_read[0]

    for html_line in html_read[1:]:
        html_head = html_head.append(html_line)

    # The data is in column format.
    # Transpose the result to make all data in single row
    return html_head.set_index(0).T

# Save the result to csv
result_df = get_key_stats(tgt_website)

###

import string
import time
import pandas as pd

url_template = 'http://eoddata.com/stocklist/NASDAQ/{}.htm'

sym_df = pd.DataFrame()
for letter in list(string.ascii_uppercase):
    tempurl = url_template.format(letter)
    temp_data = pd.read_html(tempurl)
    temp_df = temp_data[4]
    if len(sym_df)==0:
        sym_df = temp_df
    else:
        sym_df = sym_df.append(temp_df)
    time.sleep(1)
stock_symbol_list = sym_df.Code.tolist()

###

all_result_df = pd.DataFrame()
url_prefix = 'https://ca.finance.yahoo.com/quote/{0}/key-statistics?p={0}'
for sym in stock_symbol_list:
    stock_url = url_prefix.format(sym)
    result_df = get_key_stats(stock_url)
    if len(all_result_df) ==0:
        all_result_df = result_df
    else:
        all_result_df = all_result_df.append(result_df)

# Save all results
all_result_df.to_csv('results.csv', index =False)

###

from google_screener_data_extract import GoogleStockDataExtract

hh = GoogleStockDataExtract()
hh.target_exchange = 'NASDAQ' #SGX, NYSE, NYSEMKT
hh.retrieve_all_stock_data()
hh.result_google_ext_df.to_csv(r'c:\data\temp.csv', index =False) #save filename


