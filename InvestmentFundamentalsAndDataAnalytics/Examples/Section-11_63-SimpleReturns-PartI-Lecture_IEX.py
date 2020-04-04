#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[ ]:
PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')
# In[ ]:
PG.head()
# In[ ]:
PG.tail()
# ## Simple Rate of Return
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
# In[ ]:
PG['simple_return'] = (PG['close'] / PG['close'].shift(1)) - 1
print (PG['simple_return'])
