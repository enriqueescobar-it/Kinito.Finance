#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part II
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Ok, let’s continue the exercise from the last lecture.
# You already downloaded the data and generated two random weightings. 
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['WMT', 'FB']
pf_data = pd.read_csv('D:/Python/Walmart_FB_2014_2017.csv', index_col='Date')
# In[2]:
log_returns = np.log(pf_data / pf_data.shift(1))
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
# Expected Portfolio Return:
# In[12]:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
# In[14]:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# In[15]:
log_returns.cov()
# In[16]:
weights
# In[17]:
weights.T
# In[24]:
a = np.dot(log_returns.cov() * 250, weights)
a
# In[22]:
np.dot (weights, a)
# In[ ]:

# Expected Portfolio Volatility:
# In[ ]:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# ***
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
# In[ ]:
pfolio_returns = []
pfolio_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
# In[ ]:
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns, pfolio_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
# In[ ]:
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities
