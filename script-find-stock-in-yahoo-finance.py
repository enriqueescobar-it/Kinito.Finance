import pandas_datareader as panDR
import datetime as dateTime
panDRAPPL = panDR.get_data_yahoo('AAPL', 
                          start=dateTime.datetime(2019, 1, 1), 
                          end=dateTime.datetime(2020, 1, 1))

import quandl 
quanAPPL = quandl.get("WIKI/AAPL",
                      start_date="2019-01-01",
                      end_date="2020-01-01")

import yfinance as yahooFin
yAAPL = yahooFin.Ticker("AAPL")
yAAPL.get_info()
# get stock info
yAAPL.info
# get historical market data
hist = yAAPL.history(period="max")
# show actions (dividends, splits)
yAAPL.actions
# show dividends
yAAPL.dividends
# show splits
yAAPL.splits
# show financials
yAAPL.financials
yAAPL.quarterly_financials
# show major holders
#stock.major_holders
# show institutional holders
#stock.institutional_holders
# show balance heet
yAAPL.balance_sheet
yAAPL.quarterly_balance_sheet
# show cashflow
yAAPL.cashflow
yAAPL.quarterly_cashflow
# show earnings
yAAPL.earnings
yAAPL.quarterly_earnings
# show sustainability
yAAPL.sustainability
# show analysts recommendations
yAAPL.recommendations
# show next event (earnings, etc)
yAAPL.calendar
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
yAAPL.isin
# show options expirations
yAAPL.options
# get option chain for specific expiration
opt = yAAPL.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts