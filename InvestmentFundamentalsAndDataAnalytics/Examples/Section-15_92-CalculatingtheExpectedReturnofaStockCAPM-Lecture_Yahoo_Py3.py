#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']   


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


# 

# **Beta:**
# ### $$            
# \beta_{pg} = \frac{\sigma_{pg,m}}{\sigma_{m}^2}
# $$

# In[6]:


PG_beta = cov_with_market / market_var
PG_beta


# **Calculate the expected return of P&G (CAPM):**
# ### $$
# \overline{r_{pg}} = r_f + \beta_{pg}(\overline{r_{m}} - r_f) 
# $$

# In[7]:


PG_er = 0.025 + PG_beta * 0.05
PG_er

