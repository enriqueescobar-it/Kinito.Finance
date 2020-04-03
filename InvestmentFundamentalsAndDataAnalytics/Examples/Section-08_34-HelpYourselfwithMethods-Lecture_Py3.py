#!/usr/bin/env python
# coding: utf-8

# In[1]:


Participants = ['John', 'Leila', 'Gregory', 'Cate']
Participants


# In[2]:


print (Participants[1])


# In[3]:


Participants[-1]


# In[4]:


Participants[-2]


# In[5]:


Participants[3]='Maria'
Participants


# In[6]:


del Participants[2]
Participants


# In[7]:


Participants[2]


# In[8]:


Participants.append("Dwayne")
Participants


# In[9]:


Participants.extend(['George', 'Catherine'])
Participants


# In[10]:


print ('The first participant is ' + Participants[0] + '.')


# In[11]:


len('Dolphin')


# In[12]:


len(Participants)

