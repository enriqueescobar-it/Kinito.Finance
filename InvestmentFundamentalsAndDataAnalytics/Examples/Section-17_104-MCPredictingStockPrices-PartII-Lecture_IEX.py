#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
# In[ ]:
ticker = 'PG' 
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1')['close']
log_returns = np.log(1 + data.pct_change())
# In[ ]:
log_returns.tail()
# In[ ]:
data.plot(figsize=(10, 6));
# In[ ]:
log_returns.plot(figsize = (10, 6))
# In[ ]:
u = log_returns.mean()
u
# In[ ]:
var = log_returns.var()
var
# In[ ]:
drift = u - (0.5 * var)
drift
# In[ ]:
stdev = log_returns.std()
stdev
# ******
# In[ ]:
type(drift)
# In[ ]:
type(stdev)
# In[ ]:
np.array(drift)
# In[ ]:
drift.values
# In[ ]:
stdev.values
# In[ ]:
norm.ppf(0.95)
# In[ ]:
x = np.random.rand(10, 2)
x
# In[ ]:
norm.ppf(x)
# In[ ]:
Z = norm.ppf(np.random.rand(10,2))
Z
# In[ ]:
t_intervals = 1000
iterations = 10
# $$
# daily\_returns = e^{r}
# $$
# 
# $$
# r = drift + stdev \cdot z
# $$
# In[ ]:
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
# In[ ]:
daily_returns
