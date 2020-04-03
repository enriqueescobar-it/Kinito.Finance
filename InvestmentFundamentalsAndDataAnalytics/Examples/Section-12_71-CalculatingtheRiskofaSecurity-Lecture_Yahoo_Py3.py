#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


# In[3]:


sec_data.tail()


# In[4]:


sec_returns = np.log(sec_data / sec_data.shift(1))


# In[5]:


sec_returns


# ## PG

# In[6]:


sec_returns['PG'].mean()


# In[7]:


sec_returns['PG'].mean() * 250


# In[8]:


sec_returns['PG'].std()


# In[9]:


sec_returns['PG'].std() * 250 ** 0.5


# ## Beiersdorf

# In[10]:


sec_returns['BEI.DE'].mean()


# In[11]:


sec_returns['BEI.DE'].mean() * 250


# In[12]:


sec_returns['BEI.DE'].std()


# In[13]:


sec_returns['BEI.DE'].std() * 250 ** 0.5


# Final Results:

# In[14]:


print (sec_returns['PG'].mean() * 250)
print (sec_returns['BEI.DE'].mean() * 250)


# In[15]:


sec_returns['PG', 'BEI.DE'].mean() * 250


# In[16]:


sec_returns[['PG', 'BEI.DE']].mean() * 250


# In[17]:


sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5

