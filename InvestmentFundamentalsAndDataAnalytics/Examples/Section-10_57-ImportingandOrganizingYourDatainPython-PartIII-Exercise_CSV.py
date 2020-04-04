#!/usr/bin/env python
# coding: utf-8
# ## Importing and Organizing Your Data in Python - Part III
# Save the data obtained in the previous exercise as a csv file. Then, save it in an excel format. <br /> 
# Do you remember which library can help you do that? Don’t forget to import it first!
# In[ ]:

# In[ ]:
tickers = ['AAPL', 'MSFT', 'XOM', 'BP']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['close']
# In[ ]:

# In[ ]:

