#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Data Reading

# In[74]:


red=pd.read_csv('D:/ML/Wine_Quality_Prediction/Dataset/wineQualityReds.csv')


# There are two datasets in kaggle which are for type of wine that is Red, White. Here We will work on Red Wine dataset.

# In[75]:


red.head(10)


# * volatile acidity :   Volatile acidity is the gaseous acids present in wine.
# 
# * fixed acidity :   Primary fixed acids found in wine are tartaric, succinic, citric, and malic
# 
# * residual sugar :   Amount of sugar left after fermentation.
# 
# * citric acid :    It is weak organic acid, found in citrus fruits naturally.
# 
# * chlorides :   Amount of salt present in wine.
# 
# * free sulfur dioxide :   So2 is used for prevention of wine by oxidation and microbial spoilage.
# 
# * total sulfur dioxide
# 
# * pH :   In wine pH is used for checking acidity
# * density
#   
# * sulphates :    Added sulfites preserve freshness and protect wine from oxidation, and bacteria.
# 
# * alcohol :   Percent of alcohol present in wine.

# # Data Exploration
# 
# * there are no categorical variables. each feature is a number. Regression problem. 
# * Given the set of values for features, we have to predict the quality of wine.
# * finding correlation of each feature with our target variable - quality

# In[76]:


red.info()


# In[77]:


red.isna().sum()


# In[78]:


red.dtypes


# **Visualization**

# In[82]:


ig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'fixed.acidity', data = red)


# Here we see that its quite a downing trend in the volatile acidity as we go higher the quality

# In[83]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'volatile.acidity', data = red)


# Composition of citric acid go higher as we go higher in the quality of the wine

# In[85]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'citric.acid', data = red)


# In[86]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'residual.sugar', data = red)


# Composition of chloride also go down as we go higher in the quality of the wine

# In[87]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'chlorides', data = red)


# In[88]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'free.sulfur.dioxide', data = red)


# In[90]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'total.sulfur.dioxide', data = red)


# Sulphates level goes higher with the quality of wine

# In[91]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'sulphates', data = red)


# Alcohol level also goes higher as te quality of wine increases

# In[93]:


fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'quality', y = 'alcohol', data = red)


# **PreProcessing of data**

# Making binary classificaion for the response variable.
# 
# Dividing wine as good and bad by giving the limit for the quality

# In[95]:


bins = (2, 6.5, 8)
group_names = ['bad', 'good']
red['quality'] = pd.cut(red['quality'], bins = bins, labels = group_names)


# In[96]:


#assign a labels to our quality variable
label_quality = LabelEncoder()


# In[98]:


red['quality'] = label_quality.fit_transform(red['quality'])


# In[99]:


red['quality'].value_counts()


# In[100]:


sns.countplot(red['quality'])


# Now seperate the dataset as response variable and feature variabes

# In[101]:


X = red.drop('quality', axis = 1)
y = red['quality']


# In[102]:


#Train and Test splitting of data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# In[103]:


#Applying Standard scaling to get optimized result
sc = StandardScaler()


# In[104]:


X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# **Model Building**
# 
# 1. **Random Forest**

# In[105]:


rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
pred_rfc = rfc.predict(X_test)


# In[106]:


print(classification_report(y_test, pred_rfc))


# In[107]:


#Confusion matrix for the random forest classification
print(confusion_matrix(y_test, pred_rfc))


# 2. **Support Vector Classifier**

# In[108]:


svc = SVC()
svc.fit(X_train, y_train)
pred_svc = svc.predict(X_test)


# In[109]:


print(classification_report(y_test, pred_svc))


# **Random Forest Classifier gives accuracy of 87%
#   While Support Vector Classifier gives accuracy of 86%**

# One can improve the accuracy by using Grid Search CV which will boost the accuracy by 3-4%.

# In[111]:


import pickle
file='wine Quality.pkl'
save=pickle.dump(rfc,open(file,'wb'))


# **Lets dive in for model creation**
