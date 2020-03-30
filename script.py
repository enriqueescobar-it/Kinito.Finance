from datetime import date
from typing import List, Any, Union
import Data.DateTime.PyDateTimes as PyDays
import Data.Yahoo.TickerNameList as PyTickers
import Data.Yahoo.YahooTicker as PyTicker

from yahoofinancials import YahooFinancials

from pandas import DataFrame
from pprint import pprint
import pandas as pd
from pandas_datareader.data import get_data_yahoo

from Data.Yahoo.YahooTicker import YahooTicker

from alpha_vantage.timeseries import TimeSeries


def getYahooDataFrame(ticker: str, from_date: date, to_date: date):
    data = get_data_yahoo(ticker, from_date, to_date)
    data.dropna(inplace=True)
    return data


def getAvPdrDataFrame(a_key: str):
    data = TimeSeries(key=open(a_key, 'r').read(), output_format='pandas')
    return data


to_day: date = PyDays.DateTime1WeekAgo()
to_day_s: str = to_day.strftime('%Y-%m-%d')
ya_day: date = PyDays.DateTime52WeekAgo()
ya_day_s: str = ya_day.strftime('%Y-%m-%d')
alpha_key = "Data/alphavantage-key.txt"
alpha_ts = TimeSeries(key=open(alpha_key, 'r').read(), output_format='pandas')
alpha_df = alpha_ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')[0]
alpha_df.columns = ["open", "high", "low", "close", "volume"]
# extracting stock data (historical close price) for the stocks identified
ticker_list = PyTickers.FAGMAlist()
# ticker_list = PyTickers.NameList50()
counter: int = 0
pdr_adjclose_df: DataFrame = pd.DataFrame()
financial_df: DataFrame = pd.DataFrame()
alpha_close_df: DataFrame = pd.DataFrame()
drop_list: List[Union[str, Any]] = []
py_tickers: List[YahooTicker] = []
new_tickers = ticker_list
# removing stocks whose data has been extracted from the ticker list
while len(new_tickers) != 0 and counter <= 5:
    new_tickers = [j for j in new_tickers if
                   j not in drop_list]
    for new_ticker in new_tickers:
        try:
            # pdr
            # pdr_df = get_data_yahoo(new_ticker, ya_day, to_day)
            # pdr_df.dropna(inplace=True)
            pdr_df = getYahooDataFrame(new_ticker, ya_day, to_day)
            pdr_adjclose_df[new_ticker] = pdr_df["Adj Close"]
            # yahoo financial
            new_financial: YahooFinancials = YahooFinancials(new_ticker)
            new_dic = new_financial.get_historical_price_data(ya_day_s, to_day_s, "daily")[new_ticker]
            new_dic_field = new_dic['prices']
            new_data_frame = pd.DataFrame(new_dic_field)[["formatted_date", "adjclose"]]
            new_data_frame.set_index("formatted_date", inplace=True)
            first_data_frame = new_data_frame[~new_data_frame.index.duplicated(keep='first')]
            financial_df[new_ticker] = first_data_frame["adjclose"]
            # alpha vantage
            alpha_ts = getAvPdrDataFrame(alpha_key)
            alpha_df = alpha_ts.get_intraday(symbol=new_ticker, interval='1min', outputsize='full')[0]
            alpha_df.columns = ["open", "high", "low", "close", "volume"]
            alpha_close_df[new_ticker] = alpha_df["close"]
            #
            drop_list.append(new_ticker)
            py_tickers.append(PyTicker.YahooTicker("NYSE", new_ticker, pdr_df, new_dic, alpha_df))
            pprint(str(counter) + " " + new_ticker + " " + str(len(drop_list)))
        except:
            print(new_ticker, " :failed to fetch data...retrying")
            continue
    counter += 1
pprint(py_tickers[0].PdrDf)
