#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Risk of a Security

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Load the data for Microsoft (‘MSFT’) for the period ‘2000-1-1’ until today. <br />
# Assess the daily and the annual risk of ‘MSFT’. Repeat the exercise for Apple for the same timeframe. 

# In[ ]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[ ]:


data = pd.read_csv('D:/Python/MSFT_AAPL_2000_2017.csv', index_col='Date')


# In[ ]:


returns = np.log(data / data.shift(1))
returns


# ### MSFT

# Daily risk:

# In[ ]:


returns['MSFT'].std()


# Annual risk:

# In[ ]:


returns['MSFT'].std() * 250 ** 0.5


# ### Apple

# Daily risk:

# In[ ]:


returns['AAPL'].std()


# Annual risk:

# In[ ]:


returns['AAPL'].std() * 250 ** 0.5


# ******

# Store the volatilities of the two stocks in an array called "vols".

# In[ ]:


vols = returns[['MSFT', 'AAPL']].std() * 250 ** 0.5
vols


# How are the two risk values different?
