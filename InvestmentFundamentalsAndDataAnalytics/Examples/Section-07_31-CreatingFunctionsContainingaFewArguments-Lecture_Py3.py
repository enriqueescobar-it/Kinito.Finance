#!/usr/bin/env python
# coding: utf-8

# In[1]:


def subtract_bc(a,b,c):
    result = a - b*c
    print ('Parameter a equals', a)
    print ('Parameter b equals', b)
    print ('Parameter c equals', c)
    return result


# In[2]:


subtract_bc(10,3,2)


# In[3]:


subtract_bc(b=3,a=10,c=2)

