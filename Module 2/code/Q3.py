#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


article_id = pd.read_csv('article-ids.csv', header = None)


# In[3]:


del article_id[0]


# In[4]:


article1 = list(article_id[1])
article2 = list(article_id[2])

article_id = {article1[i] : article2[i] for i in range(len(article1))}


# In[5]:


category_id = pd.read_csv('category-ids.csv', header = None)


# In[6]:


del category_id[0]


# In[7]:


category1 = list(category_id[1])
category2 = list(category_id[2])

category_id = {category1[i] : category2[i] for i in range(len(category1))}


# In[ ]:





# In[ ]:





# In[8]:


categories = pd.read_csv("categories.tsv", delimiter = "\t", names = ["0","1"] )
categories = categories[12:]
articles = list(categories["0"])


# In[ ]:





# In[9]:


i = 0
article_categories = {}
for category in categories["1"]:
    article_category = [article_id[articles[i]]]
    if article_id[articles[i]] not in article_categories:
        article_categories[article_id[articles[i]]] = []
    article_categories[article_id[articles[i]]].append(category_id[category])
    
    i = i + 1


# In[10]:


for a in range(1,4605):
    article = "A"+"%04d"%a
    if article not in article_categories:
        article_categories[article] = ["C"+"%04d"%1]


# In[ ]:





# In[11]:


article_categories_combined = []
for article in article_categories:
    combined = []
    combined.append(article)
    for category in article_categories[article]:
        combined.append(category)
    article_categories_combined.append(combined)


# In[12]:


df_article = pd.DataFrame(article_categories_combined)


# In[15]:


df_article.to_csv (r'article-categories.csv', header = ["Article_ID", "Category_ID", "Category_ID", "Category_ID"]) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




