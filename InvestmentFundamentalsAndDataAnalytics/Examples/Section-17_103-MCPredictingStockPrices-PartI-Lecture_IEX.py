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


# In[ ]:


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


# $$
# drift = u - \frac{1}{2} \cdot var
# $$

# In[ ]:


drift = u - (0.5 * var)
drift


# In[ ]:


stdev = log_returns.std()
stdev

