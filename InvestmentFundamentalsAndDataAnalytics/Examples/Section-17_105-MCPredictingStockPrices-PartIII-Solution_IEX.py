#!/usr/bin/env python
# coding: utf-8
# ## Monte Carlo - Forecasting Stock Prices - Part III
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Forecasting Future Stock Prices – continued:
# In[1]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
ticker = 'MSFT' 
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1')['close']
log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()
drift.values
stdev.values
t_intervals = 250
iterations = 10
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
# ***
# Create a variable S0 equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
# In[2]:
S0 = data.iloc[-1]
S0
# Create a variable price_list with the same dimension as the daily_returns matrix. 
# In[3]:
price_list = np.zeros_like(daily_returns)
price_list
# In[4]:
price_list[0]
# Set the values on the first row of the price_list array equal to S0.
# In[5]:
price_list[0] = S0
price_list
# Create a loop in the range (1, t_intervals) that reassigns to the price in time t the product of the price in day (t-1) with the value of the daily returns in t.
# In[7]:
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
# In[8]:
price_list
# Finally, plot the obtained price list data.
# In[9]:
plt.figure(figsize=(10,6))
plt.plot(price_list);
