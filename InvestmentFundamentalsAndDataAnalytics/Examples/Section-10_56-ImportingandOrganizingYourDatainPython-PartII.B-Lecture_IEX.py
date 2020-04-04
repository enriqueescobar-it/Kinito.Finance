#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
# In[2]:
ser = pd.Series(np.random.random(5), name = "Column 01")
# In[3]:
ser
# In[4]:
ser[2]
# In[ ]:
from pandas_datareader import data as wb
# In[ ]:
PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')
# In[ ]:
PG
# In[ ]:
PG.info()
# In[ ]:
PG.head()
# In[ ]:
PG.tail()
# In[ ]:
PG.head(20)
# In[ ]:
PG.tail(20)
# In[ ]:
tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['close']
# In[ ]:
new_data.tail()
# In[ ]:
new_data.head()
