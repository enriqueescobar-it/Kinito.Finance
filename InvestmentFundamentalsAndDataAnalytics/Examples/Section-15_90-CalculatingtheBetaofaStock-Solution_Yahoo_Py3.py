#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Beta of a Stock

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Obtain data for Microsoft and S&P 500 for the period 1st of January 2012 – 31st of December 2016 from Yahoo Finance. 

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['MSFT', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']   


# Let S&P 500 act as the market. 

# *****

# Calculate the beta of Microsoft.

# In[2]:


sec_returns = np.log( data / data.shift(1) )


# In[3]:


cov = sec_returns.cov() * 250
cov


# In[4]:


cov_with_market = cov.iloc[0,1]
cov_with_market


# In[5]:


market_var = sec_returns['^GSPC'].var() * 250
market_var


# ** Beta: **
# ### $$ 
# \beta_{pg} = \frac{\sigma_{pg,m}}{\sigma_{m}^2}
# $$

# In[6]:


MSFT_beta = cov_with_market / market_var
MSFT_beta

