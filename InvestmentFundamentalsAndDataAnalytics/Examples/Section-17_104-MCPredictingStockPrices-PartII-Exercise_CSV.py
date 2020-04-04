#!/usr/bin/env python
# coding: utf-8
# ## Monte Carlo - Forecasting Stock Prices - Part II 
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Forecasting Future Stock Prices – continued:
# In[ ]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
data = pd.read_csv('D:/Python/MSFT_2000.csv', index_col = 'Date')
log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()
# ******
# Use “.values” to transform the *drift* and the *stdev* objects into arrays. 
# In[ ]:

# Forecast future stock prices for every trading day a year ahead. So, assign 250 to “t_intervals”. <br />
# Let’s examine 10 possible outcomes. Bind “iterations” to the value of 10.
# In[ ]:

# Use the formula we have provided and calculate daily returns.
# $$
# daily\_returns = exp({drift} + {stdev} * z), 
# $$ 
# <br \>
# $$
# where\  z = norm.ppf(np.random.rand(t\_intervals, iterations)
# $$
# In[ ]:

