#!/usr/bin/env python
# coding: utf-8
# # CAPM - Capital Asset Pricing Model
# Watch the video for the full overview.
# Portfolio Returns:
# ## $r_p(t) = \sum\limits_{i}^{n}w_i r_i(t)$
# Market Weights:
# ## $ w_i = \frac{MarketCap_i}{\sum_{j}^{n}{MarketCap_j}} $
# ### CAPM of a portfolio
# ## $ r_p(t) = \beta_pr_m(t) + \sum\limits_{i}^{n}w_i \alpha_i(t)$
# Model CAPM as a simple linear regression
from scipy import stats
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np

help(stats.linregress)
spy_etf = web.DataReader('SPY', 'yahoo')
# In[21]:
spy_etf.info()
# In[22]:
spy_etf.head()
# In[18]:
start = pd.to_datetime('2010-01-04')
end = pd.to_datetime('2017-07-18')
aapl = web.DataReader('AAPL', 'yahoo', start, end)
aapl.head()
# In[28]:
#get_ipython().run_line_magic('matplotlib', 'inline')
aapl['Close'].plot(label='AAPL', figsize=(10, 8))
spy_etf['Close'].plot(label='SPY Index')
plt.legend()
# ## Compare Cumulative Return
aapl['Cumulative'] = aapl['Close'] / aapl['Close'].iloc[0]
spy_etf['Cumulative'] = spy_etf['Close'] / spy_etf['Close'].iloc[0]
aapl['Cumulative'].plot(label='AAPL', figsize=(10, 8))
spy_etf['Cumulative'].plot(label='SPY Index')
plt.legend()
plt.title('Cumulative Return')
# ## Get Daily Return
aapl['Daily Return'] = aapl['Close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['Close'].pct_change(1)
plt.scatter(aapl['Daily Return'], spy_etf['Daily Return'], alpha=0.3)
# In[46]:
aapl['Daily Return'].hist_df(bins=100)
spy_etf['Daily Return'].hist_df(bins=100)
beta, alpha, r_value, p_value, std_err = stats.linregress(aapl['Daily Return'].iloc[1:],
                                                          spy_etf['Daily Return'].iloc[1:])
beta
# In[39]:
alpha
# In[40]:
r_value
# ## What if our stock was completely related to SP500?
spy_etf['Daily Return'].head()
noise = np.random.normal(0, 0.001, len(spy_etf['Daily Return'].iloc[1:]))
noise
# In[65]:
spy_etf['Daily Return'].iloc[1:] + noise
# In[66]:
beta, alpha, r_value, p_value, std_err = stats.linregress(spy_etf['Daily Return'].iloc[1:] + noise,
                                                          spy_etf['Daily Return'].iloc[1:])
beta
# In[68]:
alpha
# Looks like our understanding is correct!
