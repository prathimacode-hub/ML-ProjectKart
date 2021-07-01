# Test Score Prediction

## Goal

The aim of project is to build machine learning algorithms to predict the scores of the students.

## Dataset

You can download dataset [here](https://www.kaggle.com/kwadwoofosu/predict-test-scores-of-students)

## What I had done 

1. Load the dataset
2. Clean the dataset
3. EDA
4. checked the
 - Feature to Feature Correlations - Higher value indicates simillarity of both two features. Therefore, the less value the better.
 - Feature to Outcome Correlations - Higher value indicates the importance of feature
5. Feature Scaling
6. Created Model


## MODELS USED

1. Linear Regression
2. KNN
3. XGbr
4. SGD
5. Decisiontree
6. RandomForest
7. LogisticRegression

## LIBRARIES NEEDED
- pandas 
- numpy 
- seaborn 
- matplotlib
- sklearn
- xgboost

## CONCLUSION

I used different algorithms to predict the accuracy and create the model. The best Algorithm that fits this dataset was Xgbr with 95.09236604564064% accuarcy. 
Every algorithm gave the good accuracy except Logistic Regression with 10.46875% accuracy.
```
Linear Regression
Score:  0.9488917003203031
MAE: 2.53 
MSE: 10.16

KNN
Score:  0.9482671812584661
MAE: 2.50 
MSE: 10.29

[15:29:25] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
XGbr
Score:  0.9509236604564064
MAE: 2.47 
MSE: 9.76

SGD
Score:  0.9488402079776442
MAE: 2.53 
MSE: 10.17

Decisiontree
Score:  0.9272406533807277
MAE: 2.97 
MSE: 14.47

RandomForest
Score:  0.9492954064871557
MAE: 2.48 
MSE: 10.08

LogisticRegression
Score:  0.1046875
MAE: 3.48 
MSE: 20.36
```
## Author 

This model is created by [@Isha307](https://github.com/Isha307)
