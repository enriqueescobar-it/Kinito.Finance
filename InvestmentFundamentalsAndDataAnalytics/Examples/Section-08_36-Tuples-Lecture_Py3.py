#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = (40, 41, 42)
x


# In[2]:


y = 50, 51, 52
y


# In[3]:


a,b,c = 1,4,6
c


# In[4]:


x[0]


# In[5]:


List = [x, y]
List


# In[6]:


(age, years_of_school) = "30,17".split(',')
print (age)
print (years_of_school)


# In[7]:


def square_info(x):
    A = x ** 2
    P = 4 * x
    print ("Area and Perimeter:") 
    return A,P

square_info(3)

