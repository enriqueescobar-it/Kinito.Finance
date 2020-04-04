#!/usr/bin/env python
# coding: utf-8
# ## Monte Carlo - Euler Discretization - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.
# In[ ]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as web  
from scipy.stats import norm 
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')
# In[ ]:
ticker = 'MSFT'  
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']
# Store the annual standard deviation of the log returns in a variable, called “stdev”.
# In[ ]:

# Set the risk free rate, r, equal to 2.5% (0.025).
# In[ ]:

# To transform the object into an array, reassign stdev.values to stdev.
# In[ ]:

# Set the time horizon, T, equal to 1 year, the number of time intervals equal to 250, the iterations equal to 10,000. Create a variable, delta_t, equal to the quotient of T divided by the number of time intervals.
# In[ ]:

# Let Z equal a random matrix with dimension (time intervals + 1) by the number of iterations. 
# In[ ]:

# Use the .zeros_like() method to create another variable, S, with the same dimension as Z. S is the matrix to be filled with future stock price data. 
# In[ ]:

# Create a variable S0 equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
# In[ ]:

# Use the following formula to create a loop within the range (1, t_intervals + 1) that reassigns values to S in time t.
# $$
# S_t = S_{t-1} \cdot exp((r - 0.5 \cdot stdev^2) \cdot delta_t + stdev \cdot delta_t^{0.5} \cdot Z_t)
# $$
# In[ ]:

# Plot the first 10 of the 10,000 generated iterations on a graph.
# In[ ]:

