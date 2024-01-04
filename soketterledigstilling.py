#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn import metrics
sns.set()
import numpy as np


# In[13]:


df=pd.read_csv('ledigstillinglonn.csv',skiprows=1)
df.head()


# In[14]:


df.info()


# In[15]:


df.columns=['Månad','ledig_stilling','Lønn']
df.head()


# In[17]:


df['Månad']=pd.to_datetime(df['Månad'])
df.info()


# In[21]:


df.set_index('Månad',inplace=True)
df.head()


# In[22]:


df.plot(figsize=(20,10))


# In[23]:


df[['ledig_stilling']].rolling(12).mean().plot(figsize=(20,10))


# In[25]:


df[['Lønn']].rolling(12).mean().plot(figsize=(20,10))


# In[30]:


df[['ledig_stilling','Lønn']].rolling(12).mean().plot(figsize=(20,10))


# In[33]:


pd.concat([df[['ledig_stilling']].rolling(12).mean(),df[['Lønn']].rolling(12).mean()],axis=1).plot(figsize=(20,10))


# In[ ]:




