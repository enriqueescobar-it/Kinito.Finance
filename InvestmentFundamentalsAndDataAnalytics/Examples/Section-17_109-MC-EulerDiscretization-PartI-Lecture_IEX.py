#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np  
import pandas as pd  
from pandas_datareader import data as web  
from scipy.stats import norm 
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')
# In[ ]:
ticker = 'PG'  
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='iex', start='2015-1-1', end='2017-3-21')['close']
# In[ ]:
log_returns = np.log(1 + data.pct_change())
# <br /><br />
# $$
# {\LARGE S_t = S_{t-1} \mathbin{\cdot} e^{((r - \frac{1}{2} \cdot stdev^2) \mathbin{\cdot} \delta_t + stdev \mathbin{\cdot} \sqrt{\delta_t} \mathbin{\cdot} Z_t)}  }
# $$
# <br /><br />
# In[ ]:
r = 0.025
# In[ ]:
stdev = log_returns.std() * 250 ** 0.5
stdev
# In[ ]:
type(stdev)
# In[ ]:
stdev = stdev.values
stdev
# In[ ]:
T = 1.0 
t_intervals = 250 
delta_t = T / t_intervals 
iterations = 10000  
# In[ ]:
Z = np.random.standard_normal((t_intervals + 1, iterations))  
S = np.zeros_like(Z) 
S0 = data.iloc[-1]  
S[0] = S0
# <br /><br />
# $$
# {\LARGE S_t = S_{t-1} \mathbin{\cdot} e^{((r - \frac{1}{2} \cdot stdev^2) \mathbin{\cdot} \delta_t + stdev \mathbin{\cdot} \sqrt{\delta_t} \mathbin{\cdot} Z_t)}  }
# $$
# <br /><br />
# In[ ]:
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])
# In[ ]:
S
# In[ ]:
S.shape
# In[ ]:
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
