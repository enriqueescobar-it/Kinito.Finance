#!/usr/bin/env python
# coding: utf-8

# ## Monte Carlo - Forecasting Stock Prices - Part I

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Download the data for Microsoft (‘MSFT’) from IEX for the period ‘2015-1-1’ until today.

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


# Use the .pct_change() method to obtain the log returns of Microsoft for the designated period.

# In[2]:


log_returns = np.log(1 + data.pct_change())


# In[3]:


log_returns.tail()


# In[4]:


data.plot(figsize=(10, 6));


# In[5]:


log_returns.plot(figsize = (10, 6))


# Assign the mean value of the log returns to a variable, called “U”, and their variance to a variable, called “var”. 

# In[6]:


u = log_returns.mean()
u


# In[7]:


var = log_returns.var()
var


# Calculate the drift, using the following formula: 
# 
# $$
# drift = u - \frac{1}{2} \cdot var
# $$

# In[8]:


drift = u - (0.5 * var)
drift


# Store the standard deviation of the log returns in a variable, called “stdev”.

# In[9]:


stdev = log_returns.std()
stdev


# ******

# Repeat this exercise for any stock of interest to you. :)
