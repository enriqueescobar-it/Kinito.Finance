#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as web  
from scipy.stats import norm 
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:
ticker = 'PG'  
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']
# In[3]:
log_returns = np.log(1 + data.pct_change())
# In[4]:
log_returns.tail()
# In[5]:
data.plot(figsize=(10, 6));
# In[6]:
r = 0.025
# In[7]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# In[8]:
type(stdev)
# In[9]:
stdev = stdev.values
stdev
# In[10]:
T = 1.0 
t_intervals = 250 
delta_t = T / t_intervals  
iterations = 10000  
# In[11]:
Z = np.random.standard_normal((t_intervals + 1, iterations))  
S = np.zeros_like(Z) 
S0 = data.iloc[-1]  
S[0] = S0 
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])
# In[12]:
S
# In[13]:
S.shape
# In[14]:
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
# ******
# In[15]:
p = np.maximum(S[-1] - 110, 0)
# In[16]:
p
# In[17]:
p.shape
# In[18]:
C = np.exp(-r * T) * np.sum(p) / iterations
C  
