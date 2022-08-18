#!/usr/bin/env python
# coding: utf-8

# In[74]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 
import csv


# In[75]:


reader = csv.DictReader(open('district-id.csv'))

districtId = {}
for row in reader:
    key = row.pop('districtname')
    districtId[key] = list(row.values())[0]


# In[76]:


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
    


# In[77]:


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


# In[78]:


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


# In[79]:


zscoreWeek = []
for dId in districtId.values():
    if dId in neighborWeek:
        for week in neighborWeek[dId]:
            neighborzscore = 0
            statezscore = 0
            
            if float(neighborWeek[dId][week]['neighborstdev']):
                neighborzscore = (float(casesWeek[dId][week]) - float(neighborWeek[dId][week]['neighbormean']))/float(neighborWeek[dId][week]['neighborstdev'])
                
            if float(stateWeek[dId][week]['statestdev']):  
                statezscore = (float(casesWeek[dId][week]) - float(stateWeek[dId][week]['statemean']))/float(stateWeek[dId][week]['statestdev'])
                
            zscoreWeek.append({'districtid':dId ,'timeid': week,'neighborhoodzscore':  round(neighborzscore,2),'statezscore': round(statezscore,2)})
            
            
zscoreMonth = []
for dId in districtId.values():
    if dId in neighborMonth:
        for month in neighborMonth[dId]:
            neighborzscore = 0
            statezscore = 0
            
            if float(neighborMonth[dId][month]['neighborstdev']):
                neighborzscore = (float(casesMonth[dId][month]) - float(neighborMonth[dId][month]['neighbormean']))/float(neighborMonth[dId][month]['neighborstdev'])
                
            if float(stateMonth[dId][month]['statestdev']):  
                statezscore = (float(casesMonth[dId][month]) - float(stateMonth[dId][month]['statemean']))/float(stateMonth[dId][month]['statestdev'])
                
            zscoreMonth.append({'districtid':dId ,'timeid': month,'neighborhoodzscore':  round(neighborzscore,2),'statezscore': round(statezscore,2)})
            

zscoreOverall = []
for dId in districtId.values():
    if dId in neighborOverall:
        for overall in neighborOverall[dId]:
            neighborzscore = 0
            statezscore = 0
            
            if float(neighborOverall[dId][overall]['neighborstdev']):
                neighborzscore = (float(casesOverall[dId][overall]) - float(neighborOverall[dId][overall]['neighbormean']))/float(neighborOverall[dId][overall]['neighborstdev'])
                
            if float(stateOverall[dId][overall]['statestdev']):  
                statezscore = (float(casesOverall[dId][overall]) - float(stateOverall[dId][overall]['statemean']))/float(stateOverall[dId][overall]['statestdev'])
                
            zscoreOverall.append({'districtid':dId ,'timeid': overall,'neighborhoodzscore': round(neighborzscore,2),'statezscore': round(statezscore,2)})
            


# In[80]:


dfWeek = pd.DataFrame(zscoreWeek) 
dfWeek.to_csv (r'zscore-week.csv', index = False, header=True)


# In[81]:


dfMonth = pd.DataFrame(zscoreMonth) 
dfMonth.to_csv (r'zscore-month.csv', index = False, header=True)


# In[82]:


dfOverall = pd.DataFrame(zscoreOverall) 
dfOverall.to_csv (r'zscore-overall.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




