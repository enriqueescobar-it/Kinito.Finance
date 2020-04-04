#!/usr/bin/env python
# coding: utf-8
# In[ ]:
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
# In[ ]:
def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
 
def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
# In[ ]:
norm.cdf(0)
# In[ ]:
norm.cdf(0.25)
# In[ ]:
norm.cdf(0.75)
# In[ ]:
norm.cdf(9)
# $$
# \textbf{C} = SN(d_1) - Ke^{-rt}N(d_2) 
# $$
# In[ ]:
def BSM(S, K, r, stdev, T):
        return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))
# In[ ]:
ticker = 'PG'  
data = pd.DataFrame()  
data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1', end='2017-3-21')['close']
# In[ ]:
S = data.iloc[-1]
S
# In[ ]:
log_returns = np.log(1 + data.pct_change())
# In[ ]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# In[ ]:
r = 0.025
K = 110.0
T = 1
# In[ ]:
d1(S, K, r, stdev, T)
# In[ ]:
d2(S, K, r, stdev, T)
# In[ ]:
BSM(S, K, r, stdev, T)
