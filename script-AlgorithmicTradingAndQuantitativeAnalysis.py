from datetime import date
from pprint import pprint
from typing import List, Any, Union

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

import Data.DateTime.PyDateTimes as PyDays
import Data.Yahoo.TickerNameList as PyTickers
import Data.Yahoo.YahooTicker as PyTicker
from Data.WebScrapper.StockRowScrapper import StockRowScrapper
from Data.Yahoo.YahooPdrManager import YahooPdrManager
from Data.YahooFinancial.FinancialManager import FinancialManager
from Data.TimeSerie.AlphaVantageManager import AlphaVantageManager
from Data.Yahoo.YahooTicker import YahooTicker
from Data.WebScrapper.YahooScrapper import YahooScrapper
from Data.WebScrapper.FmpScrapper import FmpScrapper

to_day: date = PyDays.DateTimeNow()
to_day_s: str = to_day.strftime('%Y-%m-%d')
ya_day: date = PyDays.DateTime52WeekAgo()
ya_day_s: str = ya_day.strftime('%Y-%m-%d')
alpha_key = "Data/alphavantage-key.txt"
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
            y_ticker = PyTicker.YahooTicker('NYSE', new_ticker, 26, 0)
            # pdr
            # pdr_df = get_data_yahoo(new_ticker, ya_day, to_day)
            # pdr_df.dropna(inplace=True)
            # pdr_df = getPdrDataFrame(new_ticker, ya_day, to_day)
            # pdr_df = y_ticker.PdrDf
            # pdr_adjclose_df[new_ticker] = pdr_df["Adj Close"]
            pdr_adjclose_df[new_ticker] = y_ticker.PdrDf["Adj Close"]
            # yahoo financial
            # new_financial: YahooFinancials = YahooFinancials(new_ticker)
            # new_financial: YahooFinancials = getYfDic(new_ticker)
            # new_financial: YahooFinancials = y_ticker.FinancialDf
            # new_dic = new_financial.get_historical_price_data(ya_day_s, to_day_s, "daily")[new_ticker]
            # new_dic = y_ticker.FinancialDf.get_historical_price_data(ya_day_s, to_day_s, "daily")[new_ticker]
            fm = FinancialManager(y_ticker)
            new_dic_field = fm.GetDailyHistoricalDataPrices(ya_day, to_day)
            new_data_frame = pd.DataFrame(new_dic_field)[["formatted_date", "adjclose"]].set_index("formatted_date", inplace=True)
            first_data_frame = new_data_frame[~new_data_frame.index.duplicated(keep='first')]
            financial_df[new_ticker] = first_data_frame["adjclose"]
            # alpha vantage
            # alpha_ts = TimeSeries(key=open(alpha_key, 'r').read(), output_format='pandas')
            # alpha_ts = getAvDay1MinPdrDataFrame(alpha_key, new_ticker)
            # alpha_df = alpha_ts.get_intraday(symbol=new_ticker, interval='1min', outputsize='full')[0]
            # alpha_df.columns = ["open", "high", "low", "close", "volume"]
            # alpha_df = getAvDay1MinPdrDataFrame(alpha_key, new_ticker)
            avm: AlphaVantageManager = AlphaVantageManager(alpha_key, y_ticker)
            alpha_close_df[new_ticker] = avm.GetIntraDayMinuteSparse(1)["close"]
            #
            drop_list.append(new_ticker)
            py_tickers.append(y_ticker)
            pprint(str(counter) + " " + new_ticker + " " + str(len(drop_list)))
        except:
            print(new_ticker, "_".ljust(20) + "failed to fetch data...retrying -> " + str(counter))
            continue
    counter += 1
pprint(py_tickers[0].TickerName)
pprint(str(py_tickers[0].PdrDf.shape))
ys: YahooScrapper = YahooScrapper(py_tickers[0])
pprint(ys.BalanceSheetUrl)
pprint(ys.CashFlowUrl)
pprint(ys.FinancialUrl)
pprint(ys.KeyStatsUrl)
fs: FmpScrapper = FmpScrapper(py_tickers[0])
pprint(fs.BalanceSheetUrl)
pprint(fs.CashFlowUrl)
pprint(fs.FinancialUrl)
pprint(fs.KeyStatsUrl)
pprint(fs.IncomeUrl)
sr: StockRowScrapper = StockRowScrapper(py_tickers[0])
pprint(sr.BalanceSheetUrl)
pprint(sr.BalanceSheetCsv)
# Replaces NaN values with the next valid value along the column
yPdr = YahooPdrManager(py_tickers[0], py_tickers[0].DateTimeFrom, py_tickers[0].DateTimeTo)
yPdr.FillNaWithNextValue()
py_tickers[0].PdrDf.fillna(method='bfill', axis=0, inplace=True)
# Deletes any row where NaN value exists
yPdr.DropRowsWithNan()
py_tickers[0].PdrDf.dropna(how='any', axis=0, inplace=True)
# Mean, Median, Standard Deviation, daily return
# prints mean stock price for each stock
print("mean")
pprint(py_tickers[0].PdrDf.mean())
# prints median stock price for each stock
print("median")
pprint(py_tickers[0].PdrDf.median())
# prints standard deviation of stock price for each stock
print("std")
# Creates dataframe with daily return for each stock
daily_return = py_tickers[0].PdrDf.pct_change()
pprint(py_tickers[0].PdrDf.std())
# prints mean daily return for each stock
print("mean daily")
pprint(daily_return.mean().tail())
# prints standard deviation of daily returns for each stock
print("std daily")
pprint(daily_return.std().tail())
# Rolling mean and standard deviation
# simple moving average
print("mean daily simple moving average")
pprint(daily_return.rolling(window=20).mean().tail())
print("std daily simple moving average")
pprint(daily_return.rolling(window=20).std().tail())
# exponential moving average
print("mean daily exponential moving average")
pprint(daily_return.ewm(span=20, min_periods=20).mean().tail())
print("std daily exponential moving average")
pprint(daily_return.ewm(span=20, min_periods=20).std().tail())
exit(7)
# Handling NaN Values
# Replaces NaN values with the next valid value along the column
pdr_adjclose_df.fillna(method='bfill',axis=0,inplace=True)

