#!/usr/bin/env python
# coding: utf-8

# ## Iterating over Dictionaries

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# In this exercise you will use the same dictionaries as the ones we used in the lesson - "prices" and "quantity". This time, don't just calculate all the money Jan spent. Calculate how much she spent on products with a price of 5 dollars or more.

# In[1]:


prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0


# In[2]:


for i in quantity:
    if prices[i]>=5:
        money_spent += prices[i]*quantity[i] 
    else:
        money_spent = money_spent

print (money_spent)


# And how much did Jan spent on products that cost less than 5 dollars?

# In[3]:


prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0


# In[4]:


for i in quantity:
    if prices[i]<5:
        money_spent += prices[i]*quantity[i] 
    else:
        money_spent = money_spent

print (money_spent)

