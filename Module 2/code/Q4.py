#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv("shortest-path-distance-matrix.txt", delimiter = '\t', header = None)


# In[5]:


df = df[16:]


# In[6]:


matrix = list(df[0])


# In[7]:


i = 1
edges = []
adj_list = {}
for row in matrix:
    j = 1
    for col in row:
        if(col == '1'):
            if "A"+"%04d"%i not in adj_list:
                adj_list["A"+"%04d"%i] = []
            if "A"+"%04d"%j not in adj_list:
                adj_list["A"+"%04d"%j] = []
                
            adj_list["A"+"%04d"%i].append("A"+"%04d"%j)
            adj_list["A"+"%04d"%j].append("A"+"%04d"%i)
            edges.append(("A"+"%04d"%i,"A"+"%04d"%j))
        j = j + 1
    i = i + 1 


# In[8]:


len(edges)


# In[9]:


df_edge = pd.DataFrame(edges)


# In[10]:


df_edge.to_csv (r'edges.csv', header = ["From_ArticleID", "To_ArticleID"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




