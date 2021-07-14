# Social Network Influencer Prediction

## Goal

The discrete label represents a human judgement about which one of the two individuals is more influential. 
The goal of the challenge is to train a machine learning model which, for a pair of individuals, 
predicts the human judgement on who is more influential with high accuracy.

## Dataset

You can download dataset [here](https://www.kaggle.com/c/predict-who-is-more-influential-in-a-social-network/data)

**A Follower**

![](https://github.com/Isha307/ML-ProjectKart/blob/main/Social%20Network%20Influencer%20Prediction/Images/A_Follower.png)

**B Follower**

![](https://github.com/Isha307/ML-ProjectKart/blob/main/Social%20Network%20Influencer%20Prediction/Images/B_Follower.png)

# WHAT I HAD DONE

- Loaded the dataset
- Analyse the data
   - Cleaned the data and found No missing Values
   - visualizing each column distribution
- Divided the dataset into X and y
- Then splitted it into train and test data
- Predicting some of the value on test.csv

# MODELS USED
- Linear Regression
- KNN
- SVM
- XGbr
- SGD
- Random Forest
- Decision Tree

# LIBRARIES NEEDED
- numpy 
- pandas 
- matplotlib
- seaborn 
- scipy
- sklearn
- xgboost

# CONCLUSION 

I used different algorithms to predict the accuracy and create the model. The best Algorithm that fits this dataset was **LogisticRegression** with 0.76 accuarcy. 
KNN score was also 0.7536. Rest of Algorithm's accuracy was very bad.

```
Linear Regression
Score:  0.18322492060478335

KNN
Score:  0.7536363636363637

SVM
Score:  0.23731973613614032

XGbr
Score:  0.46248247015361643

SGD
Score:  -1.9580848666569655e+45

Decisiontree
Score:  -0.08376534066864139

RandomForest
Score:  0.4282916764558793

LogisticRegression
Score:  0.76
```

# Author 

This model is created by [@Isha307](https://github.com/Isha307)
