#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part III
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Ok, let’s continue the exercise from the last lecture.
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['WMT', 'FB']
pf_data = pd.read_csv('D:/Python/Walmart_FB_2014_2017.csv', index_col='Date')
# In[ ]:
log_returns = np.log(pf_data / pf_data.shift(1))
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
# Expected Portfolio Return:
# In[ ]:
np.sum(weights * log_returns.mean()) * 250
# Expected Portfolio Variance:
# In[ ]:
np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
# Expected Portfolio Volatility:
# In[ ]:
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
# ***
# The rest of this exercise will be a reproduction of what we did in the previous video.
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.
# In[ ]:
pf_returns = []
pf_volatilities = []
# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.
# In[ ]:
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pf_returns, pf_volatilities
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once you have done that, the two objects will be NumPy arrays. 
# In[ ]:
pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)
pf_returns, pf_volatilities
# Now, create a dictionary, called portfolios, whose keys are the strings “Return” and “Volatility” and whose values are the NumPy arrays pf_returns and pf_volatilities. 
# In[ ]:

# Finally, plot the data from the portfolios dictionary on a graph. Let the x-axis represent the volatility data from the portfolios dictionary and the y-axis – the data about rates of return. <br />
# Organize your chart well and make sure you have labeled both the x- and the y- axes.
# In[ ]:

# ******
# What do you think would happen if you re-created the Markowitz Efficient Frontier for 3 stocks? The code you have created is supposed to accommodate easily the addition of a third stock, say British Petroleum (‘BP’). Insert it in your data and re-run the code (you can expand the “Cell” list from the Jupyter menu and click on “Run All” to execute all the cells at once!). <br />
# 
# How would you interpret the obtained graph? 
# 
# In[ ]:

# Expected Portfolio Return:
# In[ ]:

# Expected Portfolio Variance:
# In[ ]:

# Expected Portfolio Volatility:
# In[ ]:

# *****
# In[ ]:

# In[ ]:

# In[ ]:
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
