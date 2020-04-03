#!/usr/bin/env python
# coding: utf-8

# ## Diversifiable and Non-Diversifiable Risk of a Portfolio

# Import the same dataset we used in the previous lecture – Microsoft and Apple stock, downloaded from IEX. Timeframe – 1st of January 2015 until today. <br />
# *Hint: To save time, we have written the code you need!*

# In[ ]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['MSFT', 'AAPL']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['Close']
    
sec_data


# Then, calculate the diversifiable and the non-diversifiable risk of a portfolio, composed of these two stocks:

# a) with weights 0.5 and 0.5;

# In[ ]:





# ### Calculating Portfolio Variance

# Equal weightings scheme:

# In[ ]:





# Portfolio Variance:

# In[ ]:





# ### Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

# Diversifiable Risk:

# In[ ]:





# Or:

# In[ ]:





# Calculating Diversifiable Risk:

# In[ ]:





# Calculating Non-Diversifiable Risk:

# In[ ]:





# *****

# b)	With weights 0.2 for Microsoft and 0.8 for Apple.

# ### Calculating Portfolio Variance

# In[ ]:





# Portfolio Variance:

# In[ ]:





# ### Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

# Calculating Diversifiable Risk:

# In[ ]:





# Calculating Non-Diversifiable Risk:

# In[ ]:




