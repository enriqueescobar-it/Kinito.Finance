#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[ ]:
ind_data = pd.read_csv('D:\Python\Indices_Data_01.csv', index_col='Date')
# In[ ]:
ind_data.head()
# In[ ]:
ind_data.tail()
# In[ ]:
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()
# In[ ]:
ind_returns = (ind_data / ind_data.shift(1)) - 1
ind_returns.tail()
# In[ ]:
annual_ind_returns = ind_returns.mean() * 250
annual_ind_returns
# ***
# In[ ]:
data_2 = pd.read_csv('D:\Python\Indices_Data_02.csv', index_col='Date')
# In[ ]:
data_2.tail()
# In[ ]:
(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()
