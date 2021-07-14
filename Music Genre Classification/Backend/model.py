import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
import catboost as cb
import xgboost as xgb

seed = 12
df = pd.read_csv('data.csv')
df['class_name'] = df['class_name'].astype('category')
df['class_label'] = df['class_name'].cat.codes

lookup_genre_name = dict(zip(df.class_label.unique(), df.class_name.unique()))

cols = list(df.columns)
cols.remove('label')
cols.remove('class_label')
cols.remove('class_name')

X = df.iloc[:,1:28]
y = df['class_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
# we must apply the scaling to the test set that we computed for the training set
X_test_scaled = scaler.transform(X_test)

pickle.dump(scaler,open('scaler.pkl','wb'))

#XGBoost
xgbc = xgb.XGBClassifier(n_estimators=100, random_state=seed)
xgbc.fit(X_train_scaled, y_train)
pickle.dump(xgbc, open('xgbc.pkl','wb'))

