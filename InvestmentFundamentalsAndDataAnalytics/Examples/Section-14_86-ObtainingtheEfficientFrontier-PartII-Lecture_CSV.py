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
pf_data = pd.read_csv('D:\Python\Markowitz_Data.csv', index_col = 'Date')


# In[3]:


pf_data.head()


# In[4]:


pf_data.tail()


# In[5]:


(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))


# In[6]:


log_returns = np.log(pf_data / pf_data.shift(1))


# In[7]:


log_returns.mean() * 250


# In[8]:


log_returns.cov() * 250


# In[9]:


log_returns.corr()


# In[10]:


num_assets = len(assets)


# In[11]:


num_assets


# In[12]:


arr = np.random.random(2)
arr


# In[13]:


arr[0] + arr[1]


# In[14]:


weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# In[15]:


weights[0] + weights[1]


# Expected Portfolio Return:

# In[16]:


np.sum(weights * log_returns.mean()) * 250


# Expected Portfolio Variance:

# In[17]:


np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))


# Expected Portfolio Volatility:

# In[18]:


np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))


# ***

# In[19]:


pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))

pfolio_returns, pfolio_volatilities


# In[20]:


pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities

