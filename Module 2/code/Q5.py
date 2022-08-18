#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import collections
import networkx as nx


# In[2]:


df = pd.read_csv("edges.csv", header = None)


# In[3]:


node1 = df[1]
node2 = df[2]


# In[4]:


i = 0
adj_list = {}
for node in node1:
    if node not in adj_list:
                adj_list[node] = []
    if node2[i] not in adj_list:
                adj_list[node2[i]] = []
    adj_list[node].append(node2[i])
    adj_list[node2[i]].append(node)
    
    i = i + 1


# In[ ]:





# In[5]:


for node in adj_list:
    adj_list[node] = list(set(adj_list[node]))


# In[ ]:





# In[6]:


adj_list = dict(collections.OrderedDict(sorted(adj_list.items())))


# In[7]:


def bfs(visited, queue, graph, node):
    visited.append(node)
    queue.append(node)
    component = []
    diameter = {}
    dia = 0
    target = ""
    while queue:
        s = queue.pop(0) 
        component.append(s) 
        if s not in diameter:
            diameter[s] = 0
        if s in graph:
            for neighbour in graph[s]:
                  if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    diameter[neighbour] = diameter[s] + 1 
        target = s
    return component, diameter[target], target


# In[8]:


def diameter(component,graph):
    visited = [] 
    queue = []  
    
    adj_list = {}
    for node in component:
        adj_list[node] = []
        if node in graph:
            adj_list[node] = graph[node]
    
    component, dia, target = bfs(visited, queue, adj_list, component[0])
    
    visited = [] 
    queue = []  
    
    component, dia, target = bfs(visited, queue, adj_list, target)
    
    return dia


# In[9]:


def findConnected(graph):
    graph_components = []
    components = []
    visited = [] 
    queue = []  
    node = 0
    for i in range(1,4605):
        if(("A"+"%04d"%i) not in visited):
            component, length, target = bfs(visited, queue, graph, "A"+"%04d"%i)
            components.append(component)
            dia = diameter(component, graph)
            edge = 0
            for node in component:
                if node in graph:
                    edge = edge + len(graph[node])
                    
            graph_components.append((len(component), int(edge/2), dia))
    return graph_components


# In[10]:


graph_components = findConnected(adj_list)


# In[11]:


df_components = pd.DataFrame(graph_components)
df_components.to_csv (r'graph-components.csv', header= ["Nodes", "Edges", "Diameter"])


# In[ ]:





# In[ ]:





# In[12]:


graph_components


# In[13]:


G = nx.DiGraph()
for node1 in adj_list:
    for node2 in adj_list[node1]:
        G.add_edge(node1, node2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




