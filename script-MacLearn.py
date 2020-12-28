from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('KO')
print(yahooStockOption.DataFrame.describe(include='all'))

sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
#yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)

### LSTM are sensitive to the scale of the data. so we apply MinMax scaler
import numpy as np
from numpy import ndarray
import pandas as pd
print(yahooStockOption.DataFrame.head(3))
##splitting dataset into train and test split
print(type(yahooStockOption.ColumnSeries))
print(len(yahooStockOption.ColumnSeries))
print(type(yahooStockOption.ColumnArray))
print(yahooStockOption.ColumnArray.shape)
print(len(yahooStockOption.ColumnArray))
print('TrainSize', yahooStockOption.TrainSize)
print(type(yahooStockOption.ColumnTrainArray))
print(yahooStockOption.ColumnTrainArray.shape)
print(len(yahooStockOption.ColumnTrainArray))
print('TestSize', yahooStockOption.TestSize)
print(type(yahooStockOption.ColumnTestArray))
print(yahooStockOption.ColumnTestArray.shape)
print(len(yahooStockOption.ColumnTestArray))

### Create the Stacked LSTM model
import tensorflow as tf
from sklearn.svm import SVR
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from datetime import datetime as dt
import matplotlib as plt

day_list = list()
days = yahooStockOption.DataFrame.index
adj_close_price_list = list()
adj_close_prices = yahooStockOption.DataFrame.loc[:, 'Adj Close']
# independent data set -> dates
for day in days:
    day_list.append(int(str(day.date()).split('-')[2]))
# dependent data set -> adj_close_prices
for adj_close_price in adj_close_prices:
    adj_close_price_list.append(adj_close_price)
# 3 models
lin_svr = SVR(kernel='linear', C=1000.00)
lin_svr.fit(days.reshape(-1, 1), adj_close_prices.reshape(-1, 1))
pol_svr = SVR(kernel='poly', C=1000.00, degree=2)
pol_svr.fit(days.reshape(-1, 1), adj_close_prices.reshape(-1, 1))
rbf_svr = SVR(kernel='rbf', C=1000.00, gamma=0.85)
rbf_svr.fit(days.reshape(-1, 1), adj_close_prices.reshape(-1, 1))
# plot
plt.figure(figsize=(8, 4))
plt.scatter(days, adj_close_prices, color='black', label=yahooStockOption.Column)
