#!/usr/bin/env python
# coding: utf-8

# ## Else if, for Brief - ELIF

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Assign 200 to x.
# Create the following piece of code:
# If x > 200, print out "Big"; 
# If x > 100 and x <= 200, print out "Average"; 
# and If x <= 100, print out "Small".
# Use the If, Elif, and Else keywords in your code.
# 
# Change the initial value of x to see how your output will vary.

# In[1]:


x = 200

if x > 200: 
    print ("Big")
elif x > 100 and x <= 200:
    print ("Average")
else:
    print ("Small")    


# Keep the first two conditions of the previous code. Add a new ELIF statement, so that, eventually, the program prints "Small" if x >= 0 and x <= 100, and "Negative" if x < 0. 
# Let x carry the value of 50 and then of -50 to check if your code is correct.

# In[2]:


x = 200

if x > 200: 
    print ("Big")
elif x > 100 and x <= 200:
    print ("Average")
elif x >= 0 and x <= 100:
    print ("Small")  
else:
    print ("Negative")

