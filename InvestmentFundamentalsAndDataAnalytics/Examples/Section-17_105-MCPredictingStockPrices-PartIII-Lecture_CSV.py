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


data = pd.read_csv('D:/Python/PG_2007_2017.csv', index_col = 'Date')

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

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))


# In[20]:


daily_returns


# ***

# $$
# S_t = S_0 \mathbin{\cdot} daily\_return_t
# $$
# <br />

# $$
# S_{t+1} = S_t \mathbin{\cdot} daily\_return_{t+1}
# $$
# 
# <br /> 
# $$...$$
# <br />  
# 
# $$
# S_{t+999} = S_{t+998} \mathbin{\cdot} daily\_return_{t+999}
# $$
# 
# 

# In[21]:


S0 = data.iloc[-1]
S0


# In[22]:


price_list = np.zeros_like(daily_returns)


# In[23]:


price_list


# In[24]:


price_list[0]


# In[25]:


price_list[0] = S0
price_list


# In[26]:


for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]


# In[27]:


price_list


# In[28]:


plt.figure(figsize=(10,6))
plt.plot(price_list);

