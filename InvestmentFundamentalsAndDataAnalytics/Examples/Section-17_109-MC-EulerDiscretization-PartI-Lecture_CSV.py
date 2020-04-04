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
data = pd.read_csv('D:/Python/PG_2007_2017.csv', index_col = 'Date')
# In[3]:
log_returns = np.log(1 + data.pct_change())
# <br /><br />
# $$
# {\LARGE S_t = S_{t-1} \mathbin{\cdot} e^{((r - \frac{1}{2} \cdot stdev^2) \mathbin{\cdot} \delta_t + stdev \mathbin{\cdot} \sqrt{\delta_t} \mathbin{\cdot} Z_t)}  }
# $$
# <br /><br />
# In[4]:
r = 0.025
# In[5]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# In[6]:
type(stdev)
# In[7]:
stdev = stdev.values
stdev
# In[8]:
T = 1.0 
t_intervals = 250 
delta_t = T / t_intervals 
iterations = 10000  
# In[9]:
Z = np.random.standard_normal((t_intervals + 1, iterations))  
S = np.zeros_like(Z) 
S0 = data.iloc[-1]  
S[0] = S0
# <br /><br />
# $$
# {\LARGE S_t = S_{t-1} \mathbin{\cdot} e^{((r - \frac{1}{2} \cdot stdev^2) \mathbin{\cdot} \delta_t + stdev \mathbin{\cdot} \sqrt{\delta_t} \mathbin{\cdot} Z_t)}  }
# $$
# <br /><br />
# In[10]:
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])
# In[11]:
S
# In[12]:
S.shape
# In[13]:
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
