
# Amazon Books Analysis

# Goal:

Prediction on book to be fiction and non-fiction using Goodreads

## Dataset
 
You can download Dataset [here](https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019)
 
## Dataset Info:

![](https://github.com/Isha307/ML-ProjectKart/blob/main/Amazon%20Books%20Analysis/Images/info.png)

# What I had done:

- Load the Dataset
- EDA
- Checked for missing data
- Created different model using different algo
- Created model which give best accuracy among them.

## MODELS USED

- Linear Regression
- KNN
- XGbr
- SGD
- Decisiontree
- RandomForest
- LogisticRegression


## LIBRARIES
- pandas
- numpy
- seaborn
- matplotlib
- sklearn
- xgboost

## CONCLUSION 

I used different algorithms to predict the accuracy and create the model. The best Algorithm that fits this dataset was RandomForest with 0.8 accuarcy. Every algorithm gave the good accuracy except Linear Regression with 0.04689495748663619 and k-means with -2347875940.807313 accuracy.
```
Linear Regression
Score:  0.04689495748663475

KNN
Score:  0.7272727272727273

SVC
Score:  0.6363636363636364

kmeans
Score:  -2347875940.807313

XGbr
Score:  0.7818181818181819

SGD
Score:  0.6727272727272727

Decisiontree
Score:  0.7090909090909091

RandomF
Score:  0.8

LogisticRegression
Score:  0.6
```

## Author 

This model is created by [@Isha307](https://github.com/Isha307)
