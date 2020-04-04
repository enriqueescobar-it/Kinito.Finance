#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:
ticker = 'PG' 
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']
# In[3]:
log_returns = np.log(1 + data.pct_change())
# In[4]:
log_returns.tail()
# In[5]:
data.plot(figsize=(10, 6));
# In[6]:
log_returns.plot(figsize = (10, 6))
# In[7]:
u = log_returns.mean()
u
# In[8]:
var = log_returns.var()
var
# $$
# drift = u - \frac{1}{2} \cdot var
# $$
# In[9]:
drift = u - (0.5 * var)
drift
# In[10]:
stdev = log_returns.std()
stdev
