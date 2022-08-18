#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:


df = pd.read_csv("paths_finished.tsv", delimiter = '\n', header = None)


# In[16]:


df = df[15:]
df = df[0]


# In[17]:


article_id = pd.read_csv('article-ids.csv', header = None)
del article_id[0]
article1 = list(article_id[1])
article2 = list(article_id[2])

article_id = {article1[i] : article2[i] for i in range(len(article1))}


# In[18]:


df_short = pd.read_csv("shortest-path-distance-matrix.txt", delimiter = '\t', header = None)


# In[19]:


df_short = df_short[16:]


# In[20]:


matrix = list(df_short[0])


# In[ ]:





# In[ ]:





# In[21]:


finished_paths_noback = []
finished_paths_back = []
for info in df:
    info = info.split()
    article = info[3].replace(";", " ")
    back = (article.count('<'))
    article = article.replace("< ", "")
    article = list(article.split(" "))
    
    shortest_path = matrix[int(article_id[article[0]][1:])-1][ int(article_id[article[-1]][1:])-1]
    if shortest_path == '_' or int(shortest_path) == 0:
        finished_paths_noback.append((len(article)-1, 0, 0))
        finished_paths_back.append((len(article)+back-1, 0, 0))
    else:
        finished_paths_noback.append((len(article)-1,int(shortest_path),(len(article)-1)/int(shortest_path)))
        finished_paths_back.append((len(article)+back-1,int(shortest_path),(len(article)+back-1)/int(shortest_path)))


# In[22]:


finished_paths_noback


# In[23]:


finished_paths_back


# In[24]:


df_finished_paths_back = pd.DataFrame(finished_paths_back)
df_finished_paths_back.to_csv (r'finished-paths-back.csv', header = ["Human_Path_Length", "Shortest_Path_Length", "Ratio"])


# In[25]:


df_finished_paths_noback = pd.DataFrame(finished_paths_noback)
df_finished_paths_noback.to_csv (r'finished-paths-no-back.csv', header = ["Human_Path_Length", "Shortest_Path_Length", "Ratio"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




