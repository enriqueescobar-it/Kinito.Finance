#!/usr/bin/env python
# coding: utf-8
# In[1]:
import quandl
# In[2]:
mydata_01 = quandl.get("FRED/GDP")
# In[3]:
mydata_01.tail()
# In[4]:
mydata_01.head()
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
mydata_02.to_excel('D:/Python/New_Files/example_02.xlsx')
# In[11]:
mydata_03 = pd.read_excel('D:/Python/Data_Files/Data_03.xlsx')
# In[12]:
mydata_03
