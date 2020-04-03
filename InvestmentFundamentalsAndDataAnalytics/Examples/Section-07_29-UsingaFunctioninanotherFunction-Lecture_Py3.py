#!/usr/bin/env python
# coding: utf-8

# In[1]:


def wage(w_hours):
    return w_hours * 25

def with_bonus(w_hours):
    return wage(w_hours) + 50


# In[2]:


wage(8), with_bonus(8)

