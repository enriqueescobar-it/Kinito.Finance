# one stock -> simple return is common but not for many
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
'''from AssetTypes.BaseAsset import BaseAsset
from AssetTypes.EquityShare import EquityShare
from AssetTypes.GovernmentBond import GovernmentBond'''
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
# with iex key`
# PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')
# csv
#PG = pd.read_csv('Section-11_PG_1995-03_23_2017.csv')
#PG = PG.set_index('Date')
# calculate simple return
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
# plot simple return
PG['simple_return'].plot(figsize=(8, 5))
# plt.show()
# Calculate the simple average daily return.
avg_returns_d = PG['simple_return'].mean()
# Estimate the simple average annual return.
avg_returns_a = PG['simple_return'].mean() * 250
# Print the simple percentage version of the result as a float with 2 digits after the decimal point.
print (str(round(avg_returns_a, 5) * 100) + ' %')
# calculate log return
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print (PG['log_return'])
# plot log return
PG['log_return'].plot(figsize=(8, 5))
# plt.show()
# Calculate the log average daily return.
avg_returns_d = PG['log_return'].mean()
# Estimate the log average annual return.
avg_returns_a = PG['log_return'].mean() * 250
# Print the log percentage version of the result as a float with 2 digits after the decimal point.
print (str(round(avg_returns_a, 5) * 100) + ' %')
#
import quandl
#
mydata_01 = quandl.get("FRED/GDP")
mydata_01.tail()
mydata_01.head()
mydata_01.to_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv')
mydata_01 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv', index_col='Date')
mydata_01.tail()
mydata_01 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_01.csv')
mydata_01.tail()
mydata_01.set_index('Date')
mydata_01.tail()
mydata_02 = pd.read_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_02.csv', index_col='Date')
mydata_02.head()
mydata_02.tail()
mydata_02.to_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_02.xlsx')
mydata_02.info()
mydata_03 = pd.read_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-Data_03.xlsx')
mydata_03.info()
mydata_03.set_index('Year')
mydata_03.info()
'''baseAsset: BaseAsset = EquityShare('PG')
print(baseAsset.ShortType)
print(baseAsset.AssetType)
print(baseAsset.AssetName)
print(baseAsset.getSimpleReturn(PG))'''
tickers = ['PG', 'MSFT', 'F', 'GE']
yahoo_df = pd.DataFrame()
iex_df = pd.DataFrame()
for t in tickers:
    yahoo_df[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
    # iex_df[t] = wb.DataReader(t, data_source='iex', start='2002-1-1')['Close']
    # yahoo_df = pd.read_csv('Section-11_67-4_stocks_1995_2017.csv', index_col='Date')
yahoo_df.tail()
yahoo_df.head()
# newDataFrame.to_csv('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-example_01.csv')
# newDataFrame.to_excel('Section-10_57-ImportingandOrganizingYourDatainPython-PartIII-example_01.xlsx')'''
yahoo_df.iloc[0]
(yahoo_df / yahoo_df.iloc[0] * 100).plot(figsize = (15, 6));
yahoo_df.plot(figsize=(15,6))
yahoo_df.loc['1995-01-03']
yahoo_df.iloc[0]
## Calculating the Return of a Portfolio of Securities
returns = (yahoo_df / yahoo_df.shift(1)) - 1
returns.head()
weights = np.array([0.25, 0.25, 0.25, 0.25])
np.dot(returns, weights)
annual_returns = returns.mean() * 250
annual_returns
np.dot(annual_returns, weights)
pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print (pfolio_1)
weights_2 = np.array([0.4, 0.4, 0.15, 0.05])
pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print (pfolio_2)
## Calculating the Risk of a Portfolio of Securities Section-11_MSFT_2000_2017.csv
returns = np.log(yahoo_df / yahoo_df.shift(1))
returns.head()
# MSFT
# Daily risk:
returns['MSFT'].std()
# Annual risk:
returns['MSFT'].std() * 250 ** 0.5
# Store the volatilities of the two stocks in an array called "vols".
volatilities = returns[['MSFT', 'AAPL']].std() * 250 ** 0.5
volatilities