# Forest Fire Prediction

# Goal:

To predict the area burned in the Forest Fire.

# DATASET

You can download dataset [here](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil)

# WHAT I HAD DONE 
- Uploaded Dataset
- EDA
- Cleaned data, but found no missing Values
- Checked for skew and kurtosis
- Feature columns with (high, +ve, or -ve) outliers, skewness and kurtosis are:
    - FFMC
    - ISI 
    - rain
    - area
- Removing outliers by zscore method.

# Models Used
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

I used different algorithms to predict the accuracy and create the model. The best Algorithm that fits this dataset was Xgbr with 0.9995011163171664 accuarcy. 
Linear Regression accuracy was 1.0 but it was overfitted, as the problem was regression problem.

![](https://github.com/Isha307/ML-ProjectKart/blob/main/Forest%20Fire%20Prediction/Images/xg.png)

```Linear Regression
Score:  1.0

KNN
Score:  -0.1195621200412591

SVM
Score:  -0.1165924503859108

[07:01:52] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
XGbr
Score:  0.9995011163171664

SGD
Score:  -4.263210271718731e+28

Decisiontree
Score:  0.9981339865437848

RandomForest
Score:  0.9150972569331404
```

# Author 

This model is created by [@Isha307](https://github.com/Isha307)
