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

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))


# In[ ]:


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

# In[ ]:


S0 = data.iloc[-1]
S0


# In[ ]:


price_list = np.zeros_like(daily_returns)


# In[ ]:


price_list


# In[ ]:


price_list[0]


# In[ ]:


price_list[0] = S0
price_list


# In[ ]:


for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]


# In[ ]:


price_list


# In[ ]:


plt.figure(figsize=(10,6))
plt.plot(price_list);

