#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("articles.tsv")


# In[4]:


df.columns = ['']


# In[5]:


df = df[10:]


# In[6]:


article = list(df.index)


# In[7]:


articles = []
i = 1
for row,nan in article:
    articles.append((row ,"A"+"%04d"%i))
    i = i + 1


# In[8]:


df_article = pd.DataFrame(articles)


# In[9]:


df_article.to_csv (r'article-ids.csv', header = ["Article_Name", "Article_ID"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




