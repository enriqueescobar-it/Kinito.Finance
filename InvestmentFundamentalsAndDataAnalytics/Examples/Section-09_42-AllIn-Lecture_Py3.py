#!/usr/bin/env python
# coding: utf-8
# In[1]:
def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total
# In[2]:
list_1 = [1,3,7,15,23,43,56,98]
# In[3]:
count(list_1)
# In[4]:
list_2 = [1,3,7,15,23,43,56,98,17]
# In[5]:
count(list_2)
