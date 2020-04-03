#!/usr/bin/env python
# coding: utf-8

# ## Logarithmic Returns

# In[ ]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
MSFT = wb.DataReader('MSFT', data_source='yahoo', start='2000-1-1')
MSFT


# ### Log Returns

# $$
# ln(\frac{P_t}{P_{t-1}})
# $$

# Calculate the Log returns for Microsoft.

# In[ ]:





# Plot the results on a graph.

# In[ ]:





# Estimate the daily and the annual mean of the obtained log returns.

# In[ ]:





# In[ ]:





# Print the result in a presentable form.

# In[ ]:





# ****

# Repeat this exercise for any stock of interest to you. :)
