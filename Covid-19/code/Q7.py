#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 
import csv


# In[7]:


reader = csv.DictReader(open('district-id.csv'))

districtId = {}
for row in reader:
    key = row.pop('districtname')
    districtId[key] = list(row.values())[0]


# In[8]:


casesWeek = {}
reader = csv.DictReader(open('cases-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesWeek)):
        casesWeek[key] = {}
    casesWeek[key][list(row.values())[0]] = list(row.values())[1] 

casesMonth = {}
reader = csv.DictReader(open('cases-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (casesMonth)):
        casesMonth[key] = {}
    casesMonth[key][list(row.values())[0]] = list(row.values())[1] 
    
casesOverall = {}
reader = csv.DictReader(open('cases-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesOverall)):
        casesOverall[key] = {}
    casesOverall[key][list(row.values())[0]] = list(row.values())[1] 


# In[9]:


neighborWeek = {}
reader = csv.DictReader(open('neighbor-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (neighborWeek)):
        neighborWeek[key] = {}
    neighborWeek[key][list(row.values())[0]] = {'neighbormean':list(row.values())[1],'neighborstdev':list(row.values())[2]}
neighborMonth = {}
reader = csv.DictReader(open('neighbor-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (neighborMonth)):
        neighborMonth[key] = {}
    neighborMonth[key][list(row.values())[0]] = {'neighbormean':list(row.values())[1],'neighborstdev':list(row.values())[2]}
    
neighborOverall = {}
reader = csv.DictReader(open('neighbor-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (neighborOverall)):
        neighborOverall[key] = {}
    neighborOverall[key][list(row.values())[0]] = {'neighbormean':list(row.values())[1],'neighborstdev':list(row.values())[2]}


# In[10]:


stateWeek = {}
reader = csv.DictReader(open('state-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (stateWeek)):
        stateWeek[key] = {}
    stateWeek[key][list(row.values())[0]] = {'statemean':list(row.values())[1],'statestdev':list(row.values())[2]}

stateMonth = {}
reader = csv.DictReader(open('state-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (stateMonth)):
        stateMonth[key] = {}
    stateMonth[key][list(row.values())[0]] = {'statemean':list(row.values())[1],'statestdev':list(row.values())[2]}
    
stateOverall = {}
reader = csv.DictReader(open('state-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (stateOverall)):
        stateOverall[key] = {}
    stateOverall[key][list(row.values())[0]] = {'statemean':list(row.values())[1],'statestdev':list(row.values())[2]}


# In[58]:


hotcoldspotWeek = []
for week in range(1,26):
    week = str(week)
    for dId in districtId.values():
        if dId in neighborWeek and week in neighborWeek[dId]:
            if(float(casesWeek[dId][week]) > (float(neighborWeek[dId][week]['neighbormean']) + float(neighborWeek[dId][week]['neighborstdev']))):
                hotcoldspotWeek.append({'timeid':week ,'method': 'neighborhood' ,'spot': 'hot','districtid': dId})
            if(float(casesWeek[dId][week]) < (float(neighborWeek[dId][week]['neighbormean']) - float(neighborWeek[dId][week]['neighborstdev']))):
                hotcoldspotWeek.append({'timeid':week ,'method': 'neighborhood' ,'spot': 'cold','districtid': dId})
            
        if dId in stateWeek and week in stateWeek[dId]:
            if(float(casesWeek[dId][week]) > (float(stateWeek[dId][week]['statemean']) + float(stateWeek[dId][week]['statestdev']))):        
                hotcoldspotWeek.append({'timeid':week ,'method': 'state' ,'spot': 'hot','districtid': dId})
            if(float(casesWeek[dId][week]) < (float(stateWeek[dId][week]['statemean']) - float(stateWeek[dId][week]['statestdev']))):
                hotcoldspotWeek.append({'timeid':week ,'method': 'state' ,'spot': 'cold','districtid': dId})

            
hotcoldspotMonth = []
for month in range(1,8):
    month = str(month)
    for dId in districtId.values():
        if dId in neighborMonth and month in neighborMonth[dId]:
            if(float(casesMonth[dId][month]) > (float(neighborMonth[dId][month]['neighbormean']) + float(neighborMonth[dId][month]['neighborstdev']))):
                hotcoldspotMonth.append({'timeid':month ,'method': 'neighborhood' ,'spot': 'hot','districtid': dId})
            if(float(casesMonth[dId][month]) < (float(neighborMonth[dId][month]['neighbormean']) - float(neighborMonth[dId][month]['neighborstdev']))):
                hotcoldspotMonth.append({'timeid':month ,'method': 'neighborhood' ,'spot': 'cold','districtid': dId})
            
        if dId in stateMonth and month in stateMonth[dId]:
            if(float(casesMonth[dId][month]) > (float(stateMonth[dId][month]['statemean']) + float(stateMonth[dId][month]['statestdev']))):        
                hotcoldspotMonth.append({'timeid':month ,'method': 'state' ,'spot': 'hot','districtid': dId})
            if(float(casesMonth[dId][month]) < (float(stateMonth[dId][month]['statemean']) - float(stateMonth[dId][month]['statestdev']))):
                hotcoldspotMonth.append({'timeid':month ,'method': 'state' ,'spot': 'cold','districtid': dId})


hotcoldspotOverall = []
for overall in range(1,2):
    overall = str(overall)
    for dId in districtId.values():
        if dId in neighborOverall and overall in neighborOverall[dId]:
            if(float(casesOverall[dId][overall]) > (float(neighborOverall[dId][overall]['neighbormean']) + float(neighborOverall[dId][overall]['neighborstdev']))):
                hotcoldspotOverall.append({'timeid':overall ,'method': 'neighborhood' ,'spot': 'hot','districtid': dId})
            if(float(casesOverall[dId][overall]) < (float(neighborOverall[dId][overall]['neighbormean']) - float(neighborOverall[dId][overall]['neighborstdev']))):
                hotcoldspotOverall.append({'timeid':overall ,'method': 'neighborhood' ,'spot': 'cold','districtid': dId})
            
        if dId in stateOverall and overall in stateOverall[dId]:
            if(float(casesOverall[dId][overall]) > (float(stateOverall[dId][overall]['statemean']) + float(stateOverall[dId][overall]['statestdev']))):        
                hotcoldspotOverall.append({'timeid':overall ,'method': 'state' ,'spot': 'hot','districtid': dId})
            if(float(casesOverall[dId][overall]) < (float(stateOverall[dId][overall]['statemean']) - float(stateOverall[dId][overall]['statestdev']))):
                hotcoldspotOverall.append({'timeid':overall ,'method': 'state' ,'spot': 'cold','districtid': dId})


# In[ ]:





# In[59]:


dfWeek = pd.DataFrame(hotcoldspotWeek) 
dfWeek.to_csv (r'method-spot-week.csv', index = False, header=True)


# In[60]:


dfMonth = pd.DataFrame(hotcoldspotMonth) 
dfMonth.to_csv (r'method-spot-month.csv', index = False, header=True)


# In[61]:


dfOverall = pd.DataFrame(hotcoldspotOverall) 
dfOverall.to_csv (r'method-spot-overall.csv', index = False, header=True)


# In[62]:


hotcoldspotOverall


# In[ ]:




