#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part III
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# We are in the middle of a set of 3 Python lectures that will help you reproduce the Markowitz Efficient Frontier. Let’s split this exercise into 3 parts and cover the first part here. 
# Begin by loading data for Walmart and Facebook from the 1st of January 2014 until today.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['WMT', 'FB']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
# In[2]:
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
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
# In[6]:
pf_returns = []
pf_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
# In[7]:
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pf_returns, pf_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
# In[8]:
pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)
pf_returns, pf_volatilities
# Now, create a dictionary, called portfolios, whose keys are the strings “Return” and “Volatility” and whose values are the NumPy arrays pf_returns and pf_volatilities. 
# In[9]:
portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_volatilities})
# In[10]:
portfolios.head()
portfolios.tail()
# Finally, plot the data from the portfolios dictionary on a graph. Let the x-axis represent the volatility data from the portfolios dictionary and the y-axis – the data about rates of return. <br />
# Organize your chart well and make sure you have labeled both the x- and the y- axes.
# In[11]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
# ******
# What do you think would happen if you re-created the Markowitz Efficient Frontier for 3 stocks? The code you have created is supposed to accommodate easily the addition of a third stock, say British Petroleum (‘BP’). Insert it in your data and re-run the code (you can expand the “Cell” list from the Jupyter menu and click on “Run All” to execute all the cells at once!). <br />
# 
# How would you interpret the obtained graph? 
# 
# In[12]:
assets = ['WMT', 'FB', 'BP']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
# In[13]:
pf_data.head()
# In[14]:
log_returns = np.log(pf_data / pf_data.shift(1))
# In[15]:
num_assets = len(assets)
num_assets
# In[16]:
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# In[17]:
weights[0] + weights[1] + weights[2]
# Expected Portfolio Return:
# In[18]:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
# In[19]:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
# In[20]:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# *****
# In[21]:
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
# In[21]:
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()
# In[24]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')