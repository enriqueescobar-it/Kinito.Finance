import pandas_datareader as pdr
from pandas import DataFrame, Series
import datetime as dt
import quandl


quanKey: str = 'A_KEY'
#quanAPPL: DataFrame = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2021-01-01")
#print(quanAPPL.columns)

stock_ticker: str = 'AAPL'#ESTC
panDRAPPL: DataFrame = pdr.get_data_yahoo(stock_ticker, start=dt.datetime(2019, 1, 1), end=dt.datetime(2020, 1, 1))
print(panDRAPPL.head(1))

import yfinance as yf

yahooTicker: yf.ticker.Ticker = yf.Ticker(stock_ticker)
print(yahooTicker.isin)
print(yahooTicker.get_info()) # get stock info print(yAAPL.info)
# get historical market data
hist_df: DataFrame = yahooTicker.history(period="max")
print(hist_df.columns)
# show actions (dividends, splits)
actions_df: DataFrame = yahooTicker.actions
print('a', actions_df[['Stock Splits']].shape)
# show dividends
dividend_series: Series = yahooTicker.dividends
print('d', dividend_series.shape)
# show splits
split_series: Series = yahooTicker.splits
print('s', split_series.shape)
# show financials
financials_df = yahooTicker.financials
print('f', financials_df.shape)
financial_q_df: DataFrame = yahooTicker.quarterly_financials
print('f', financial_q_df.shape)
# show major holders
# stock.major_holders
# show institutional holders
# stock.institutional_holders
# show balance heet
bs_df: DataFrame = yahooTicker.balance_sheet
print('bs', bs_df.shape)
bs_q_df: DataFrame = yahooTicker.quarterly_balance_sheet
print('bsq', bs_q_df.shape)
# show cashflow
cf_df: DataFrame = yahooTicker.cashflow
print('cf', cf_df)
cf_q_df: DataFrame = yahooTicker.quarterly_cashflow
print('cfq', cf_q_df)
# show earnings
print(yahooTicker.earnings.shape)
print(yahooTicker.quarterly_earnings.shape)
# show sustainability
yahooTicker.sustainability
# show analysts recommendations
yahooTicker.recommendations
# show next event (earnings, etc)
cal_df: DataFrame = yahooTicker.calendar
print('cal', cal_df.shape)
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
yahooTicker.isin
# show options expirations
# CNR.TO yAAPL.options
# get option chain for specific expiration
# opt = yAAPL.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
