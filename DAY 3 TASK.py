#!/usr/bin/env python
# coding: utf-8

# # DAY 3

# In[4]:


def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1={'hello','world','the','10'}
dict2={'welcome','2','my','an'}
print(Merge(dict1, dict2))
print(dict2)


# In[9]:


test_dict = {"Maths" : 34, "English" : 65, "Hindi" : 67, "SST" : 56} 
print (str(test_dict)) 
del test_dict['Hindi'] 
print (str(test_dict)) 


# In[10]:


keys = ['red', 'green', 'blue']
values = ['0','8','6']
color_dictionary = dict(zip(keys, values))
print(color_dictionary) 


# In[12]:


seta =set([5,10,3,15,2,20])
print(len(seta))


# In[11]:


sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)

