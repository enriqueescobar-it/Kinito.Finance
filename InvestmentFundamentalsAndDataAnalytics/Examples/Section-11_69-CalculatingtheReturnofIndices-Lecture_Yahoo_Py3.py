#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['^GSPC', '^IXIC', '^GDAXI']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start='1997-1-1')['Adj Close']


# In[3]:


ind_data.head()


# In[4]:


ind_data.tail()


# In[5]:


(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()


# In[6]:


ind_returns = (ind_data / ind_data.shift(1)) - 1

ind_returns.tail()


# In[7]:


annual_ind_returns = ind_returns.mean() * 250
annual_ind_returns


# ***

# In[8]:


tickers = ['PG', '^GSPC', '^DJI']

data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']    


# In[9]:


data_2.tail()


# In[10]:


(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()

