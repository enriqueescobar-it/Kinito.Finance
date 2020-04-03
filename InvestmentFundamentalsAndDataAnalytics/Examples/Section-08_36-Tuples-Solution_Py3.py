#!/usr/bin/env python
# coding: utf-8

# ## Tuples

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Create a tuple, called "Cars", with elements "BMW", "Dodge", and "Ford". 

# In[1]:


Cars = "BMW", "Dodge", "Ford"
Cars


# or:

# In[2]:


Cars = ("BMW", "Dodge", "Ford")
Cars


# Access the second element of this tuple.

# In[3]:


Cars[1]


# Call a method that would allow you to extract the provided name and age separately. Then print the "name" and "age" values to see if you worked correctly.

# In[4]:


name, age = 'Peter,24'


# In[5]:


name, age = 'Peter,24'.split(',')


# In[6]:


print (name)
print (age)


# Create a function that takes as arguments the two values of a rectangle and then returns the Area and the Perimeter of the rectangle.
# Call the function with arguments 2 and 10 to verify it worked correctly.

# In[7]:


def rectangle_info(x,y):
    A = x * y
    P = 2 * (x + y)
    print ("Area and Parameter:")
    return A, P


# In[8]:


rectangle_info(2, 10)

