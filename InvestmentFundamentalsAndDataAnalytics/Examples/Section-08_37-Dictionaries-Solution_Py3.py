#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# This is the menu of a close-by restaurant:

# In[1]:


Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}


# What is the second meal in the list?

# In[2]:


Menu['meal_2']


# or:

# In[3]:


print (Menu['meal_2'])


# Add a new meal - "Soup".

# In[4]:


Menu['meal_5'] = "Soup"
Menu


# Replace the Hamburger with a Cheeseburger.

# In[5]:


Menu['meal_3'] = 'Cheesburger'
Menu


# Attach the Desserts list in the form of a sixth meal.

# In[6]:


Dessert = ['Pancakes', 'Ice-cream', 'Tiramisu']


# In[7]:


Menu['meal_6'] = Dessert
Menu


# Create a new dictionary that contains the first five meals as keys and assign the following five values as prices (in dollars):
# 10, 5, 8, 12, 5. 
# Start by *Price_list = {}*.

# In[8]:


Price_list = {}
Price_list['Spaghetti'] = 10
Price_list['Fries'] = 5
Price_list['Cheesburger'] = 8
Price_list['Lasagna'] = 12
Price_list['Soup'] = 5
Price_list


# or:

# In[9]:


Price_list = {}
Price_list[Menu['meal_1']] = 10
Price_list[Menu['meal_2']] = 5
Price_list[Menu['meal_3']] = 8
Price_list[Menu['meal_4']] = 12
Price_list[Menu['meal_5']] = 5
Price_list


# Use the *.get()* method to check the price of the Spaghetti.

# In[10]:


Price_list.get('Spaghetti')


# or:

# In[11]:


Price_list.get(Menu['meal_1'])

