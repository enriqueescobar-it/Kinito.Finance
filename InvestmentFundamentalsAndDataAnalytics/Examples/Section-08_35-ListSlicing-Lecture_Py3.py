#!/usr/bin/env python
# coding: utf-8

# In[1]:


Participants = ['John', 'Leila', 'Maria', 'Dwayne', 'George', 'Catherine']


# In[2]:


Participants


# In[3]:


Participants[1:3]


# In[4]:


Participants[:2]


# In[5]:


Participants[4:]


# In[6]:


Participants[-2:]


# ********

# In[7]:


Maria_ind = Participants.index("Maria")
Maria_ind


# *********

# In[8]:


Newcomers = ['Joshua', 'Brittany']
Newcomers


# In[9]:


Bigger_List = [Participants, Newcomers]
Bigger_List


# In[10]:


Participants.sort()
Participants


# In[11]:


Participants.sort(reverse=True)
Participants


# In[12]:


Numbers = [1,2,3,4,5]
Numbers.sort()
Numbers


# In[13]:


Numbers.sort(reverse = True)
Numbers

