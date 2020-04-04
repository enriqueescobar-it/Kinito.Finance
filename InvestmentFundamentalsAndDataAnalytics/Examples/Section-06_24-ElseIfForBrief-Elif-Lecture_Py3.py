#!/usr/bin/env python
# coding: utf-8
# In[1]:
def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 5:
        return "Less"
    else:
        return "Equal"
# In[2]:
print (compare_to_five(10))
# In[3]:
print (compare_to_five(2))
# In[4]:
print (compare_to_five(5))
# In[5]:
def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 0:
        return "Negative"
    elif y < 5:          
        return "Less"
    else:
        return "Equal"
# In[6]:
print (compare_to_five(-3))
# In[7]:
print (compare_to_five(3))
# In[8]:
def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 5:
        return "Less"
    elif y < 0:          
        return "Negative"
    else:
        return "Equal"
# In[9]:
print (compare_to_five(-3))
# In[10]:
print (compare_to_five(3))
