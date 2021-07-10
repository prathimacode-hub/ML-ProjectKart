#!/usr/bin/env python
# coding: utf-8

# # Solar Radiation Prediction

# 
# ## Importing the Libraries 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mtp
import seaborn as sns
import sklearn


# 
# ## Reading the Data 

# In[2]:


sun = pd.read_csv('SolarPrediction.csv')
sun


# 
# ## Understanding the Data 

# In[3]:


sun.dtypes


# In[4]:


sun.shape


# In[5]:


sun.size


# In[6]:


sun.columns


# In[7]:


sun.info()


# In[8]:


sun.describe()


# In[9]:


sun.nunique()


# In[10]:


sun.corr()


# In[11]:


sun.isnull().any()


# 
# ## Visualization 

# In[12]:


sns.heatmap(sun.isnull(), yticklabels = 'False', cmap = 'Reds')


# In[13]:


sns.distplot(sun['Temperature'], color = 'orange')


# In[14]:


sns.distplot(sun['Pressure'], color = 'blue')


# In[15]:


sns.distplot(sun['Humidity'], color = 'green')


# In[16]:


sns.pairplot(sun)


# In[17]:


mtp.figure(figsize=(15,10))
sns.heatmap(sun.corr(), yticklabels = 'auto', annot = True)
mtp.show()


# 
# ## Splitting the Data into Dependent and Independent Variables 

# In[18]:


x = sun.drop(['Data', 'Time', 'Radiation', 'TimeSunRise', 'TimeSunSet'], axis = 1)
y = sun['Radiation']


# In[19]:


x.shape


# In[20]:


y.shape


# 
# ## Feature Importance 

# In[21]:


from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
model.fit(x,y)
print(model.feature_importances_)


# In[22]:


feat_imp = pd.Series(model.feature_importances_, index = x.columns)


# In[23]:


feat_imp.nlargest(5).plot(kind = 'barh')


# 
# ## Training and Testing the Data 

# In[24]:


features = ['Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)', 'Speed']
label = ['Radiation']
x = sun[features]
y = sun[label]


# In[25]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x = scaler.fit_transform(x)


# In[26]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 30)


# 
# # 1. Linear Regression 

# In[27]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)


# 
# ### Prediction 

# In[28]:


ypred_train = lr.predict(x_train)
ypred_test = lr.predict(x_test)


# 
# ### Accuracy

# In[29]:


from sklearn import metrics
print('Accuracy of Training Data: ', metrics.r2_score(y_train, ypred_train)*100)
ac1 = metrics.r2_score(y_test, ypred_test)*100
print('Accuracy of Testing Data: ', ac1)


# 
# ### Error 

# In[30]:


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, ypred_test)*100
print('Mean Square Error: ', mse)


# 
# # 2. Decision Tree Regressor

# In[31]:


from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth = 5)
dt.fit(x_train, y_train)


# 
# ### Prediction 

# In[32]:


ypred_train = dt.predict(x_train)
ypred_test = dt.predict(x_test)


# 
# ### Accuracy

# In[33]:


print('Accuracy of Training Data: ', metrics.r2_score(y_train, ypred_train)*100)
ac2 = metrics.r2_score(y_test, ypred_test)*100
print('Accuracy of Testing Data: ', ac2)


# 
# ### Error 

# In[34]:


mse = mean_squared_error(y_test, ypred_test)
print('Mean Square Error: ', mse)


# 
# # 3. KNN Regressor 

# In[35]:


from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors = 10)
knn.fit(x_train, y_train)


# 
# ### Prediction 

# In[36]:


ypred_train = knn.predict(x_train)
ypred_test = knn.predict(x_test)


# 
# ### Accuracy 

# In[37]:


print('Accuracy of Training Data: ', metrics.r2_score(y_train, ypred_train)*100)
ac3 = metrics.r2_score(y_test, ypred_test)*100
print('Accuracy of Testing Data: ', ac3)


# 
# ### Error  

# In[38]:


mse = mean_squared_error(y_test, ypred_test)
print('Mean Sqaure Error: ', mse)


# 
# # Comparing the Accuracy 

# In[39]:


accuracy = {ac1:'Linear Regression', ac2:'Decision Tree Regressor', ac3:'KNN Regressor'}


# In[40]:


sns.set_style('darkgrid')
mtp.figure(figsize=(15,10))
model_accuracies = list(accuracy.values())
model_names = list(accuracy.keys())
sns.barplot(x = model_accuracies, y = model_names, palette = 'plasma')


# Hence, **KNN Regressor** has the Highest Accuracy i.e., **72.79%**.
# 

# Therefore, we will save the model. 

# 
# # Saving the Model 

# In[41]:


import pickle
pickle.dump(knn, open('model.pkl', 'wb'))

