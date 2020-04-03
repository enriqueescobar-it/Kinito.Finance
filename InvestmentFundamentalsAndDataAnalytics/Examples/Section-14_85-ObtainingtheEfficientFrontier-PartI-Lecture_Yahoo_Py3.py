#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


assets = ['PG', '^GSPC']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']


# In[3]:


pf_data.tail()


# In[4]:


(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))


# In[5]:


log_returns = np.log(pf_data / pf_data.shift(1))


# In[6]:


log_returns.mean() * 250


# In[7]:


log_returns.cov() * 250


# In[8]:


log_returns.corr()


# In[9]:


num_assets = len(assets)


# In[10]:


num_assets


# In[11]:


arr = np.random.random(2)
arr


# In[12]:


arr[0] + arr[1]


# In[13]:


weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# In[14]:


weights[0] + weights[1]

