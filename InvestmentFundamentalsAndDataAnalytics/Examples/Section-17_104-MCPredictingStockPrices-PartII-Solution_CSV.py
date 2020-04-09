#!/usr/bin/env python
# coding: utf-8
## Monte Carlo - Forecasting Stock Prices - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Load the data for Microsoft (‘MSFT’) for the period ‘2000-1-1’ until today.
# Forecasting Future Stock Prices – continued:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
data = pd.read_csv('D:/Python/MSFT_2000.csv', index_col = 'Date')
log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
u
# In[7]:
var = log_returns.var()
var
# $$
# drift = u - \frac{1}{2} \cdot var
# $$
drift = u - (0.5 * var)
drift
# In[9]:
stdev = log_returns.std()
# ******
# Use “.values” to transform the *drift* and the *stdev* objects into arrays. 
# In[2]:
type(drift)
# In[3]:
drift.values
# In[4]:
type(stdev)
# In[5]:
stdev.values
# Forecast future stock prices for every trading day a year ahead. So, assign 250 to “t_intervals”. <br />
# Let’s examine 10 possible outcomes. Bind “iterations” to the value of 10.
# In[6]:
t_intervals = 250
iterations = 10
# Use the formula we have provided and calculate daily returns.
# $$
# daily\_returns = exp({drift} + {stdev} * z), 
# $$ 
# <br \>
# $$
# where\  z = norm.ppf(np.random.rand(t\_intervals, iterations)
# $$
# In[7]:
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns
