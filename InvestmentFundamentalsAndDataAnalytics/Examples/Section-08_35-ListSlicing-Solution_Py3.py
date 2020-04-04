#!/usr/bin/env python
# coding: utf-8
# ## List Slicing
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# In[1]:
Numbers = [15, 40, 50, 100, 115, 140]
# Using list slicing, obtain the numbers 100 and 115.
# In[2]:
Numbers[3:5]
# Using slicing, extract the first four elements from the list.
# In[3]:
Numbers[:4]
# Using slicing, extract all the elements from the list from the 3rd position onwards.
# In[4]:
Numbers[3:]
# Using slicing, extract the last 4 elements from the list.
# In[5]:
Numbers[-4:]
# Which is the position of the value 15?
# In[6]:
Numbers.index(15)
# Create a list, called "Two_Numbers". Let its elements be the values 1 and 2. Then, create a new one, named "All_Numbers", that will containt both the "Numbers" and the "Two_Numbers" lists. 
# In[7]:
Two_Numbers = [1,2]
All_Numbers = [Two_Numbers, Numbers]
All_Numbers
# Sort all the numbers in the "Numbers" list from the largest to the smallest.
# In[8]:
Numbers.sort(reverse=True)
Numbers
