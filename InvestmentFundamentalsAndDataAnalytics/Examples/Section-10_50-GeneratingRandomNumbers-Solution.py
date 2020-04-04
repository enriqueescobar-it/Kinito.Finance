#!/usr/bin/env python
# coding: utf-8
# ## Generating Random Numbers
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Import the random module and generate a random probability. 
# In[1]:
import random
# In[2]:
prob = random.random()
print (prob)
# Then, generate a random integer within the range of 1 and 20. 
# In[3]:
number = random.randint(1, 20)
print (number)
# Finally, import NumPy and create a 3 x 5-dimensional array, filled with random integers within the range of 1 and 20.
# In[4]:
import numpy as np
# In[5]:
np.random.randint(1,20,(3,5))
