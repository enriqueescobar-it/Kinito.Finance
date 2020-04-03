#!/usr/bin/env python
# coding: utf-8

# ## Importing and Organizing Your Data in Python - Part III

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Save the data obtained in the previous exercise as a csv file. Then, save it in an excel format. <br /> 
# Do you remember which library can help you do that? Don’t forget to import it first!

# In[ ]:


import pandas as pd
from pandas_datareader import data as wb 


# In[ ]:


tickers = ['AAPL', 'MSFT', 'XOM', 'BP']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['close']


# In[ ]:


new_data.to_csv('D:/Python/New_Files/example_01.csv')


# In[ ]:


new_data.to_excel('D:/Python/New_Files/example_01.xlsx')

