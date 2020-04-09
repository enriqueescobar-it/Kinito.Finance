#!/usr/bin/env python
# coding: utf-8
## Monte Carlo - Forecasting Stock Prices - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.
# Download the data for Microsoft (‘MSFT’) from IEX for the period ‘2015-1-1’ until today.
# Forecasting Future Stock Prices – continued:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:
# ticker = 'PG'
# ticker = 'MSFT'
# data = pd.DataFrame()
# data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']
# data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1')['close']
data = pd.read_csv('Section-17_PG_2007_2017.csv', index_col = 'Date')
data = pd.read_csv('Section-17_MSFT_20000.csv', index_col = 'Date')
data.plot(figsize=(10, 6));
# Use the .pct_change() method to obtain the log returns of Microsoft for the designated period.
log_returns = np.log(1 + data.pct_change())
log_returns.tail()
log_returns.plot(figsize = (10, 6))
# Assign the mean value of the log returns to a variable, called “U”, and their variance to a variable, called “var”. 
u = log_returns.mean()
u
# In[7]:
var = log_returns.var()
var
# Calculate the drift, using the following formula: 
# $$
# drift = u - \frac{1}{2} \cdot var
# $$
drift = u - (0.5 * var)
drift
# Store the standard deviation of the log returns in a variable, called “stdev”.
stdev = log_returns.std()
stdev
# ******
# Use “.values” to transform the *drift* and the *stdev* objects into arrays. 
type(drift)
drift.values
# In[4]:
type(stdev)
# In[12]:
np.array(drift)
drift.values
# In[14]:
stdev.values
# Forecast future stock prices for every trading day a year ahead. So, assign 250 to “t_intervals”.
# Let’s examine 10 possible outcomes. Bind “iterations” to the value of 10.
t_intervals = 250
t_intervals = 1000
iterations = 10
# Use the formula we have provided and calculate daily returns.
# $$
# r = drift + stdev \cdot z
# $$
# $$
# daily\_returns = exp({drift} + {stdev} * z), 
# $$
# $$
# where\  z = norm.ppf(np.random.rand(t\_intervals, iterations)
# $$
# $$
# daily\_returns = e^{r}
# $$
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns
# $$
# S_t = S_0 \mathbin{\cdot} daily\_return_t
# $$
# $$
# S_{t+1} = S_t \mathbin{\cdot} daily\_return_{t+1}
# $$
# $$...$$
# $$
# S_{t+999} = S_{t+998} \mathbin{\cdot} daily\_return_{t+999}
# $$
# ***
# Create a variable S0 equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
S0 = data.iloc[-1]
S0
# Create a variable price_list with the same dimension as the daily_returns matrix. 
price_list = np.zeros_like(daily_returns)
price_list
price_list[0]
# Set the values on the first row of the price_list array equal to S0.
price_list[0] = S0
price_list
# Create a loop in the range (1, t_intervals) that reassigns to the price in time t the product of the price in day (t-1) with the value of the daily returns in t.
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
price_list
# Finally, plot the obtained price list data.
plt.figure(figsize=(10,6))
plt.plot(price_list);
