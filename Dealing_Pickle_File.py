
# coding: utf-8

# In[58]:


# print current working directory
import os
print(os.getcwd()) #현재 작업경로 보기


# In[59]:


# load pickle file
import pickle

a = open('pk_idx2pos.pkl', 'rb')
idx_and_pos = pickle.load(a)

print("type : ", type(idx_and_pos))
print("------------------------")
idx_and_pos


# In[60]:


with open('pk_idx2pos.pkl', 'rb') as f:
    d = pickle.load(f, encoding='latin1')

v = list(d.values())
k = list(d.keys())

[k[1:5], v[1:5]]

