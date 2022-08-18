#!/usr/bin/env python
# coding: utf-8

# In[130]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 
import csv
import operator


# In[138]:


zscoreWeek = {}
reader = csv.DictReader(open('zscore-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (zscoreWeek)):
        zscoreWeek[key] = {}
    zscoreWeek[key][list(row.values())[0]] = {'neighborhoodzscore':list(row.values())[1],'statezscore':list(row.values())[2]}
    
zscoreMonth = {}
reader = csv.DictReader(open('zscore-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (zscoreMonth)):
        zscoreMonth[key] = {}
    zscoreMonth[key][list(row.values())[0]] = {'neighborhoodzscore':list(row.values())[1],'statezscore':list(row.values())[2]}
    
zscoreOverall = {}
reader = csv.DictReader(open('zscore-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (zscoreOverall)):
        zscoreOverall[key] = {}
    zscoreOverall[key][list(row.values())[0]] = {'neighborhoodzscore':list(row.values())[1],'statezscore':list(row.values())[2]}
    


# In[139]:


spotWeek = {}
reader = csv.DictReader(open('method-spot-week.csv')) 
for row in reader:
    key = row.pop('timeid')
    if(key not in (spotWeek)):
        spotWeek[key] = {}
    if list(row.values())[0] not in spotWeek[key]:
        spotWeek[key][list(row.values())[0]] = []
    spotWeek[key][list(row.values())[0]].append({'spot':list(row.values())[1],'districtid':list(row.values())[2]})
    
spotMonth = {}
reader = csv.DictReader(open('method-spot-month.csv')) 
for row in reader:
    key = row.pop('timeid')
    if(key not in (spotMonth)):
        spotMonth[key] = {}
    if list(row.values())[0] not in spotMonth[key]:
        spotMonth[key][list(row.values())[0]] = []
    spotMonth[key][list(row.values())[0]].append({'spot':list(row.values())[1],'districtid':list(row.values())[2]})
    
spotOverall = {}
reader = csv.DictReader(open('method-spot-overall.csv')) 
for row in reader:
    key = row.pop('timeid')
    if(key not in (spotOverall)):
        spotOverall[key] = {}
    if list(row.values())[0] not in spotOverall[key]:
        spotOverall[key][list(row.values())[0]] = []
    spotOverall[key][list(row.values())[0]].append({'spot':list(row.values())[1],'districtid':list(row.values())[2]})
    


# In[ ]:





# In[144]:


topWeek = []
for week in range(1,26):
    week = str(week)
    #neighborhood
    hot = {}
    cold = {}
    for spot in spotWeek[week]['neighborhood']:
        dId = (spot['districtid'])
        if(spot['spot'] == 'hot'):
            hot[zscoreWeek[dId][week]['neighborhoodzscore']] = dId
        if(spot['spot'] == 'cold'):
            cold[zscoreWeek[dId][week]['neighborhoodzscore']] = dId
    districtHot = [None for _ in range(10)]
    districtCold = [None for _ in range(10)]
    
    hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
    i = 0
    for value in hot.values():
        districtHot[i] = value
        i = i+1
        if(i > 5):
            break
            
    cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
    i = 0
    for value in cold.values():
        districtCold[i] = value
        i = i+1
        if(i > 5):
            break
            
    topWeek.append({'timeid':week ,'method': 'neighborhood' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
    topWeek.append({'timeid':week ,'method': 'neighborhood' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})
    
    
    #state
    hot = {}
    cold = {}
    for spot in spotWeek[week]['state']:
        dId = (spot['districtid'])
        if(spot['spot'] == 'hot'):
            hot[zscoreWeek[dId][week]['statezscore']] = dId
        if(spot['spot'] == 'cold'):
            cold[zscoreWeek[dId][week]['statezscore']] = dId
    districtHot = [None for _ in range(10)]
    districtCold = [None for _ in range(10)]
    
    hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
    i = 0
    for value in hot.values():
        districtHot[i] = value
        i = i+1
        if(i > 5):
            break
            
    cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
    i = 0
    for value in cold.values():
        districtCold[i] = value
        i = i+1
        if(i > 5):
            break
            
    topWeek.append({'timeid':week ,'method': 'state' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
    topWeek.append({'timeid':week ,'method': 'state' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})
    
    
        
topMonth = []
for month in range(1,8):
    month = str(month)
    #neighborhood
    hot = {}
    cold = {}
    for spot in spotMonth[month]['neighborhood']:
        dId = (spot['districtid'])
        if(spot['spot'] == 'hot'):
            hot[zscoreMonth[dId][month]['neighborhoodzscore']] = dId
        if(spot['spot'] == 'cold'):
            cold[zscoreMonth[dId][month]['neighborhoodzscore']] = dId
    districtHot = [None for _ in range(10)]
    districtCold = [None for _ in range(10)]
    
    hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
    i = 0
    for value in hot.values():
        districtHot[i] = value
        i = i+1
        if(i > 5):
            break
            
    cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
    i = 0
    for value in cold.values():
        districtCold[i] = value
        i = i+1
        if(i > 5):
            break
            
    topMonth.append({'timeid':month ,'method': 'neighborhood' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
    topMonth.append({'timeid':month ,'method': 'neighborhood' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})
    
    
    #state
    hot = {}
    cold = {}
    for spot in spotMonth[month]['state']:
        dId = (spot['districtid'])
        if(spot['spot'] == 'hot'):
            hot[zscoreMonth[dId][month]['statezscore']] = dId
        if(spot['spot'] == 'cold'):
            cold[zscoreMonth[dId][month]['statezscore']] = dId
    districtHot = [None for _ in range(10)]
    districtCold = [None for _ in range(10)]
    
    hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
    i = 0
    for value in hot.values():
        districtHot[i] = value
        i = i+1
        if(i > 5):
            break
            
    cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
    i = 0
    for value in cold.values():
        districtCold[i] = value
        i = i+1
        if(i > 5):
            break
            
    topMonth.append({'timeid':month ,'method': 'state' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
    topMonth.append({'timeid':month ,'method': 'state' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})
    


topOverall = []
for overall in range(1,2):
    overall = str(overall)
    #neighborhood
    hot = {}
    cold = {}
    if 'neighborhood' in spotOverall[overall]:
        for spot in spotOverall[overall]['neighborhood']:
            dId = (spot['districtid'])
            if(spot['spot'] == 'hot'):
                hot[zscoreOverall[dId][overall]['neighborhoodzscore']] = dId
            if(spot['spot'] == 'cold'):
                cold[zscoreOverall[dId][overall]['neighborhoodzscore']] = dId
        districtHot = [None for _ in range(10)]
        districtCold = [None for _ in range(10)]

        hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
        i = 0
        for value in hot.values():
            districtHot[i] = value
            i = i+1
            if(i > 5):
                break

        cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
        i = 0
        for value in cold.values():
            districtCold[i] = value
            i = i+1
            if(i > 5):
                break

        topOverall.append({'timeid':overall ,'method': 'neighborhood' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
        topOverall.append({'timeid':overall ,'method': 'neighborhood' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})


    #state
    hot = {}
    cold = {}
    if 'state' in spotOverall[overall]:
        for spot in spotOverall[overall]['state']:
            dId = (spot['districtid'])
            if(spot['spot'] == 'hot'):
                hot[zscoreOverall[dId][overall]['statezscore']] = dId
            if(spot['spot'] == 'cold'):
                cold[zscoreOverall[dId][overall]['statezscore']] = dId
        districtHot = [None for _ in range(10)]
        districtCold = [None for _ in range(10)]

        hot = dict(sorted(hot.items(), key=operator.itemgetter(0),reverse=True))
        i = 0
        for value in hot.values():
            districtHot[i] = value
            i = i+1
            if(i > 5):
                break

        cold = dict(sorted(cold.items(), key=operator.itemgetter(0),reverse=False))
        i = 0
        for value in cold.values():
            districtCold[i] = value
            i = i+1
            if(i > 5):
                break

        topOverall.append({'timeid':overall ,'method': 'state' ,'spot': 'hot','districtid1': districtHot[0], 'districtid2': districtHot[1], 'districtid3': districtHot[2], 'districtid4': districtHot[3], 'districtid5': districtHot[4]})
        topOverall.append({'timeid':overall ,'method': 'state' ,'spot': 'cold','districtid1': districtCold[0], 'districtid2': districtCold[1], 'districtid3': districtCold[2], 'districtid4': districtCold[3], 'districtid5': districtCold[4]})


# In[141]:


dfWeek = pd.DataFrame(topWeek) 
dfWeek.to_csv (r'top-week.csv', index = False, header=True)


# In[142]:


dfMonth = pd.DataFrame(topMonth)
dfMonth.to_csv (r'top-month.csv', index = False, header=True)


# In[143]:


dfOverall = pd.DataFrame(topOverall) 
dfOverall.to_csv (r'top-overall.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




