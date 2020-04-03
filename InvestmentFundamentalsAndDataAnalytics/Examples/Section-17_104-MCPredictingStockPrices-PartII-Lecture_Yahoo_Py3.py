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

log_returns = np.log(1 + data.pct_change())


# In[3]:


log_returns.tail()


# In[4]:


data.plot(figsize=(10, 6));


# In[5]:


log_returns.plot(figsize = (10, 6))


# In[6]:


u = log_returns.mean()
u


# In[7]:


var = log_returns.var()
var


# In[8]:


drift = u - (0.5 * var)
drift


# In[9]:


stdev = log_returns.std()
stdev


# ******

# In[10]:


type(drift)


# In[11]:


type(stdev)


# In[12]:


np.array(drift)


# In[13]:


drift.values


# In[14]:


stdev.values


# In[15]:


norm.ppf(0.95)


# In[16]:


x = np.random.rand(10, 2)
x


# In[17]:


norm.ppf(x)


# In[18]:


Z = norm.ppf(np.random.rand(10,2))
Z


# In[19]:


t_intervals = 1000
iterations = 10


# $$
# daily\_returns = e^{r}
# $$
# 
# $$
# r = drift + stdev \cdot z
# $$

# In[20]:


daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))


# In[21]:


daily_returns

