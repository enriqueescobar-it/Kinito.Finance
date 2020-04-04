#!/usr/bin/env python
# coding: utf-8
# ## Working with Arrays
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# In[1]:
import numpy as np
# In[7]:
a = np.array([[0, 1, 2, 3, 15.25, 6.15], [4.15, 5.65, 6.23, 7, 8.0, 81.5], [4, 5, 8.3, 7, 17.5, 20]])
a
# Check the dimension you have created is correct (use “*.shape*”)
# In[8]:
a.shape
# Substitute the 5th element from the 2nd row with 19.75.
# In[9]:
a[1,4] = 19.75
a
# Extract the 2nd and the 3rd row of the array you created. 
# In[10]:
a[1]
# In[11]:
a[2]
