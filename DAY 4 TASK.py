#!/usr/bin/env python
# coding: utf-8

# # DAY 4

# In[5]:


list1 = [1, 2, 3, 4, 5]

list1.insert(4,10)
print(list1)

list2=['a', 'b', 'c', 'd']
list2.insert(0, 'z')
print(list2)


# In[6]:


list2=['a', 'b', 'c', 'd']
list2.remove('a')
print(list2)


# In[7]:


a=[18, 52, 23, 41, 32]
a.sort()
ln=a[-1]
print("Largest element is:",ln)


# In[8]:


list1=[10, 20, 4, 45, 99]
list1.sort()
print("smallest element is:", *list1[:1])


# In[9]:


def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup    
tuples = ('e','t','g','t','m','v','w')
Reverse(tuples)


# In[10]:


import itertools
tuple = [(1, 2), (3, 4),(5, 6)]
out = list(itertools.chain(*tuple))
print(out)

