# Web-Page-Phishing-Detection
**Wiki Definition** : Phishing is a type of social engineering where an attacker sends a fraudulent ("spoofed") message designed to trick a human victim into revealing sensitive information to the attacker or to deploy malicious software on the victim's infrastructure like ransomware. Phishing attacks have become increasingly sophisticated and often transparently mirror the site being targeted, allowing the attacker to observe everything while the victim is navigating the site, and transverse any additional security boundaries with the victim.

![](https://github.com/kadatatlukishore/ML-ProjectKart/blob/web-page-phishing-detection/Web%20Page%20Phishing%20Detection/Images/Phishing.jpg)

### Unique phishing reports by year
|Year|	Campaigns|
|:----|:----------|
|2005 | 173,063|
|2006 | 268,126 |
|2007 | 327,814|
|2008| 335,965|
|2009|	412,392|
|2010|	313,517|
|2011|	284,445|
|2012|	320,081|
|2013|	491,399|
|2014|	704,178|
|2015|	1,413,978|

###  GOAL: 

Many people get scammed by this Web page phishing technique. Detecting them can save people from getting scammed. Hackers usually blackmail the people to get their personal information back. Identifying this techniques can save millions.

### DATASET:
- [**In Repo**](https://github.com/kadatatlukishore/ML-ProjectKart/blob/web-page-phishing-detection/Web%20Page%20Phishing%20Detection/Dataset/dataset_phishing.csv)
- [**Kaggle**](https://www.kaggle.com/manishkc06/web-page-phishing-detection)

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

### CONCLUSION
#### Accuracies:- 

|| ALGORITHM | ACCURACY |
|:-|---------:|:----------|
|1|LogisticRegression|  0.65|
|2|DecisionTreeClassifier|0.93|
|3|RandomForestClassifier|0.95 |
|4|XGBClassifier|0.95 |


#### MODEL COMPARSION 
![](https://github.com/kadatatlukishore/ML-ProjectKart/blob/web-page-phishing-detection/Web%20Page%20Phishing%20Detection/Images/Roc-curve.jpg)


Seeing the above ROC Curve we can observe that RandomForestClassifier and XGBClassifier are best models but it may be due to overfitting also. So, we can conclude that **DecisionTreeClassifier** is the best model for our usecase.


### AUTHOR

[**K Kishore**](https://www.linkedin.com/in/kadatatlukishore/)
