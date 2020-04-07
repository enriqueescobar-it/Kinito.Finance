#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part II
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# We are in the middle of a set of 3 Python lectures that will help you reproduce the Markowitz Efficient Frontier. Let’s split this exercise into 3 parts and cover the first part here. 
# Begin by loading data for Walmart and Facebook from the 1st of January 2014 until today.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['PG', '^GSPC']
pf_data = pd.read_csv('Section-14_Markowitz_Data.csv', index_col = 'Date')
pf_data.tail()
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()
# In[10]:
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1]
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
# Expected Portfolio Return:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# ***
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
pfolio_returns = []
pfolio_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns, pfolio_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns, pfolio_volatilities