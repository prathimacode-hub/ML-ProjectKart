***PROJECT NAME***
Income Classification Prediction Web App 

**GOAL**
The Main Goal of this project to find out whether a person earn more than 50K dollar(>50K) and less than or equal to 50K dollar (<=50K) based on the given presonal information about person like country, education, married or not, race etc.

**DATASET**
https://www.kaggle.com/overload10/adult-census-dataset

**WHAT I HAD DONE**

1. Data cleaning ,feature scaling on numerical data , binning of categorical data , remove white spaces and special characters from columns.
2. Perform data visulization to see the distribution of numerical data , frequency of categorical data with respect to target columns and to show the correlation among given information.
3. Split the dataset into train and test, perform model building techniques , do cross validation to check the scores of all machine learning model and perform oversampling to handle imbalanced data.

**MODELS USED**
1. LogisticRegression
2. DecisionTreeClassifier
3. XGBClassifier
4. GaussianNB
5. KNeighborsClassifier
6. RandomForestClassifier
7. SVC

These models works very well with respect to Binary Classification problem.


**LIBRARIES NEEDED**
1. pandas 1.2.1
2. numpy 1.20.0
3. seaborn 0.11.0
4. matplotlib 3.2.1
5. sklearn 0.24.1
6.  0.61.0

INCLUSION OF **SCREENSHOT** IS MUST FOR FRONT END DESIGNERS AND UI/UX DESIGNERS.
![Getting Started](./Scr1.png) ![Getting Started](./Scr2.png)

![Getting Started](./Scr3.png)

**CONCLUSION**
Accuracy of Machine learning Models **before** dealing with imbalanced data set as we see the xgboost shows the higher accuracy among them i.e., 87 % which is also too low for a model.
1. Logistic Regression 0.8323641800963615
2. Decision Tree Classifier 0.8154178434955973
3. XGBoost Classifier 0.8725701943844493
4. Naive Bayes Classifier 0.8041202857617544
5. KNeighbors Classifier 0.8488120950323974
6. Random Forest Classifier 0.8185745140388769

Accuracy of Machine learning Models **after** dealing with imbalanced data set as we see the decision tree classifier shows the higher accuracy among them i.e., 97 % which is better than previous model.

1. Logistic Regression 0.7956471174613723
2. Decision Tree Classifier 0.9720883867752118
3. XGBoost Classifier 0.8672536966273467
4. Naive Bayes Classifier 0.8363515534141884
5. KNeighbors Classifier 0.9709254028908456
6. Random Forest Classifier 0.7768732347566041