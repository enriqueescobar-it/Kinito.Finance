#!/usr/bin/env python
# coding: utf-8

# ## Simple Returns - Part II

# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$

# In[ ]:


import numpy as np
from pandas_datareader import data as wb
MSFT = wb.DataReader('MSFT', data_source='yahoo', start='2000-1-1')
MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print (MSFT['simple_return'])


# Plot the simple returns on a graph.

# In[ ]:





# Calculate the average daily return.

# In[ ]:





# Estimate the average annual return.

# In[ ]:





# Print the percentage version of the result as a float with 2 digits after the decimal point.

# In[ ]:




