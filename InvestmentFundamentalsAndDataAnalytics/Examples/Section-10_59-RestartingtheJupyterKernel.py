#!/usr/bin/env python
# coding: utf-8
# In[5]:
import pandas as pd
# In[6]:
mydata_01.to_csv('D:/Python/New_Files/example_01.csv')
# In[7]:
mydata_02 = pd.read_csv('D:/Python/Data_Files/Data_02.csv')
# In[8]:
mydata_02.head()
# In[9]:
mydata_02.tail()
# In[10]:
mydata_02 = pd.read_csv('D:/Python/Data_Files/Data_02.csv', index_col='Date')
# In[11]:
mydata_02
# In[12]:
mydata_03 = pd.read_excel('D:/Python/Data_Files/Data_03.xlsx')
# In[13]:
mydata_03
# In[14]:
mydata_03.set_index('Year')
# In[15]:
mydata_03
# In[16]:
mydata_03 = mydata_03.set_index('Year')
# In[17]:
mydata_03
# In[ ]:

