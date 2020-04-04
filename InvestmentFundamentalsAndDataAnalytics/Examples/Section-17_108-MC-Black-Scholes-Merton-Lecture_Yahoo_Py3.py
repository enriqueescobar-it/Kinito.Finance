#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
# $$
# d_1 = \frac{\ln(\frac{S}{K}) + (r + \frac{stdev^2}{2})t}{s \cdot \sqrt{t}}
# $$
# 
# $$
# d_2 = d_1 - s \cdot \sqrt{t} = \frac{\ln(\frac{S}{K}) + (r - \frac{stdev^2}{2})t}{s \cdot \sqrt{t}}
# $$
# In[2]:
def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
 
def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
# In[3]:
norm.cdf(0)
# In[4]:
norm.cdf(0.25)
# In[5]:
norm.cdf(0.75)
# In[6]:
norm.cdf(9)
# $$
# \textbf{C} = SN(d_1) - Ke^{-rt}N(d_2) 
# $$
# In[7]:
def BSM(S, K, r, stdev, T):
        return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))
# In[8]:
ticker = 'PG'  
data = pd.DataFrame()  
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']
# In[9]:
S = data.iloc[-1]
S
# In[10]:
log_returns = np.log(1 + data.pct_change())
# In[11]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# In[12]:
r = 0.025
K = 110.0
T = 1
# In[13]:
d1(S, K, r, stdev, T)
# In[14]:
d2(S, K, r, stdev, T)
# In[15]:
BSM(S, K, r, stdev, T)
