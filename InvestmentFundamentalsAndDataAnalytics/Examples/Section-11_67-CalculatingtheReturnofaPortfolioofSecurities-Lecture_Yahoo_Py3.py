#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']


# In[3]:


mydata.info()


# In[4]:


mydata.head()


# In[5]:


mydata.tail()


# ### Normalization to 100:
# 
# $$
# \frac {P_t}{P_0} * 100
# $$

# In[6]:


mydata.iloc[0]


# In[7]:


(mydata / mydata.iloc[0] * 100).plot(figsize = (15, 6));
plt.show()


# In[8]:


mydata.plot(figsize=(15,6))
plt.show()


# In[9]:


mydata.loc['1995-01-03']


# In[10]:


mydata.iloc[0]


# ## Calculating the Return of a Portfolio of Securities

# In[11]:


returns = (mydata / mydata.shift(1)) - 1
returns.head()


# In[12]:


weights = np.array([0.25, 0.25, 0.25, 0.25])


# In[13]:


np.dot(returns, weights)


# ***

# In[14]:


annual_returns = returns.mean() * 250
annual_returns


# In[15]:


np.dot(annual_returns, weights)


# In[15]:


pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print (pfolio_1)


# ***

# In[16]:


weights_2 = np.array([0.4, 0.4, 0.15, 0.05])


# In[17]:


pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print (pfolio_1)
print (pfolio_2)

