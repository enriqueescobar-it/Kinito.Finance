#!/usr/bin/env python
# coding: utf-8

# In[1]:


for n in range(10):
    print (2 ** n),


# In[4]:


for x in range(20):
    if x % 2 == 0:
        print (x, end = " ")
    else:
        print ("Odd", end = " ")


# ********

# In[6]:


x = [0,1,2]


# In[7]:


for item in x:
    print (item, end = " ")


# In[8]:


for item in range(len(x)):
    print (x[item], end = " ")

