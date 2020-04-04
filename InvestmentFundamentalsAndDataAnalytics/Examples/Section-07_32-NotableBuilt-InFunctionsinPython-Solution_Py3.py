#!/usr/bin/env python
# coding: utf-8
# ## Notable Built-In Functions in Python
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Obtain the maximum number among the values 25, 65, 890, and 15.
# In[1]:
max(25, 65, 890, 15)
# Obtain the minimum number among the values 25, 65, 890, and 15.
# In[2]:
min(25, 65, 890, 15)
# Find the absolute value of -100
# In[3]:
abs(-100)
# Round the value of 55.5. Did you obtain 56.0?
# In[4]:
round(55.5)
# Round 35.56789 to the third digit.
# In[5]:
round(35.56789, 3)
# Find the sum of all elements in the provided list, called "Numbers".
# In[6]:
Numbers = [1, 5, 64, 24.5]
# In[7]:
sum(Numbers)
# Use a built-in function to raise 10 to the power of 3.
# In[8]:
pow(10, 3)
# How many characters are there in the word "Elephant"?
# In[9]:
len("Elephant")
# Create a function, called "distance_from_zero", that returns the absolute value of a provided single argument and prints a statement "Not Possible" if the argument provided is not a number.
# Call the funtion with the values of -10 and "cat" to verify it works correctly.
# In[10]:
def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        print ("Not possible")
# In[11]:
distance_from_zero(-10)
# In[12]:
distance_from_zero("cat")
