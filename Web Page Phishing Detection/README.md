# Web-Page-Phishing-Detection

###  GOAL: 
Many people get scammed by this Web page phishing technique. Detecting them can save people from getting scammed

### DATASET:
- [**Here**](https://github.com/kadatatlukishore/ML-ProjectKart/blob/web-page-phishing-detection/Web%20Page%20Phishing%20Detection/Dataset/dataset_phishing.csv)

### WHAT I HAD DONE:

1. Performed EDA 
2. Feature Selection using **RandomForestClassifier.feature_importances_** 
    - Considered top 15 features which contributes more to predict the target variable
3. Modelling 
4. Model Comparsion using ROC curve analysis

### MODELS USED: 
- LogisticRegression
- DecisionTreeClassifier
- RandomForestClassifier
- XGBClassifier

### LIBRARIES NEEDED:  
- Pandas 
- Seaborn
-  Matplotlib
- sklearn
  - sklearn.model_selection.train_test_split
  - sklearn.ensemble.RandomForestClassifier
  - sklearn.linear_model.LogisticRegression
  - sklearn.tree.DecisionTreeClassifier
   - sklearn.metrics importing classification_report,roc_curve, roc_auc_score, auc, confusion_matrix
- xgboost
  - xgboost.XGBClassifier

## MODEL COMPARSION 
![](https://github.com/kadatatlukishore/ML-ProjectKart/blob/web-page-phishing-detection/Web%20Page%20Phishing%20Detection/Images/Roc-curve.jpg)

### CONCLUSION
Seeing the above ROC Curve we can observe that RandomForestClassifier and XGBClassifier are best models but it may be due to overfitting also. So, we can conclude that **DecisionTreeClassifier** is the best model for our usecase.


### AUTHOR

[**K Kishore**](https://www.linkedin.com/in/kadatatlukishore/)
