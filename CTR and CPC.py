#!/usr/bin/env python
# coding: utf-8

# # CTR and CPC

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as ss


# In[2]:


df = pd.read_csv('conversion.csv')


# In[36]:


df.head()


# ### Here I want to see the distribution of impressions for each advertising company.
# 

# In[37]:


graph = df.groupby('fb_campaign_id').agg({'Impressions':'sum'})


# In[38]:


sns.distplot(graph, kde=False, bins=30)


# I see that the distribution is not normal.
# My distribution is not normal, I apply the logarithm and look at the result.

# In[39]:


df_log = np.log(df.groupby('fb_campaign_id').agg({'Impressions':'sum'}))


# In[40]:


sns.distplot(df_log, kde=False, bins=30)


# And now I calculate CTR.

# In[41]:


df['ctr'] = df.Clicks / df.Impressions


# In[42]:


df.head()


# I want to see which advertising company has which view distribution.
# I will look at the example of companies with the lowest and highest results.

# In[43]:


df.groupby('xyz_campaign_id').agg({'ad_id':'count'})


# In[44]:


df_916 = df.query('xyz_campaign_id == 916')


# In[45]:


sns.distplot(df_916.ctr, kde=False, bins=20)


# In[46]:


df_1178 = df.query('xyz_campaign_id == 1178')


# In[47]:


sns.distplot(df_1178.ctr, kde=False, bins=20)


# And now I calculate CPC.

# In[48]:


df['cpc'] = df.Spent / df.Clicks


# In[49]:


df.head()


# Now I want to calculate the Interquartile range.

# In[50]:


ss.iqr(df.cpc, nan_policy='omit')


# In[51]:


sns.distplot(df.cpc.dropna(), kde=False, bins=20)


# Now I want to see the gender distribution. I will plot two graphs and then compare them.

# In[52]:


df_gender = df.groupby('gender').agg({'cpc' : 'sum'}).dropna()


# In[53]:


df_gender


# In[54]:


df_m = df.query('gender == "M"')


# In[55]:


df_f = df.query('gender == "F"')


# In[56]:


sns.distplot(df_m.cpc.dropna(), kde=False, bins=20)


# In[57]:


sns.distplot(df_f.cpc.dropna(), kde=False, bins=20)


# In[58]:


sns.distplot(df_m.cpc.dropna(), kde=False, bins=20)
sns.distplot(df_f.cpc.dropna(), kde=False, bins=20)

