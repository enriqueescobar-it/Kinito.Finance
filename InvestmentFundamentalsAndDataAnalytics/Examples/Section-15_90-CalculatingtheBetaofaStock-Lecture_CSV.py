#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
data = pd.read_csv('D:\Python\CAPM_data.csv', index_col = 'Date') 
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
PG_beta = cov_with_market / market_var
PG_beta
