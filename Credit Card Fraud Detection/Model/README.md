**PROJECT TITLE - Credit Card Fraud Detection**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Credit%20Card%20Fraud%20Detection/Images/project_viz1.png" width="400">

**GOAL** - The aim of the project is to predict fraudulent credit card transactions using machine learning models.This analysis and prediction is important for a bank as each fraud trancastion is a loss of the bank as well as customer faith. The dataset contains transactions made by credit cardholders.

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Credit%20Card%20Fraud%20Detection/Images/heatmap.png" width="300">

**WHAT HAVE I DONE**
- Loading datasets
- Handling null values
- Checking the distribution of positive and nagetive classes
- Observing the distribution of classes with 'time' feature
- Observe the distribution of classes with 'amount' feature
- Splitting the data in training and test set
- Feature Scaling the 'Amount' column using Label Encoding
- Dealing with Skewness
- Using the Power Transformer module of sklearn to change the distribution of the data
- Building Logistic Regression, XGBoost, Decision Tree and Random Forest models on imbalanced data using various optimisation and hypertuning concepts.
- Since data is imbalanced accuracy will be very high always, therefore using the ROC-AUC score metric to get the actual efficiency of every algorithm and perform a comparative analysis.
- Visualizing the imbalanced data
- Handling the imbalanced data using different approaches like undersampling, oversampling and SMOTE and use the newly generated data to train the best fir model and perform predictions using it.
- Saving the models


**MODELS USED**
- Logistic Regression - *A simple classification algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables.* 
- XGBoost - *eXtreme Gradient Boost alsorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- GridSearchCV - *This is a hyperparameter optimistion algorithm that increases the model accuracy by tweaking the hyperparameters to their best values*


**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- imblearn
- xgboost

**Data Visualizations**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Credit%20Card%20Fraud%20Detection/Images/smote_xgboost.png" width="300">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Credit%20Card%20Fraud%20Detection/Images/smote_logistic.png" width="300">

**Conclusion**

In this project we have performed a detailed analysis of the given dataset and tried different approach to erradicate the imbalance in the data to build a better and more generalised training model which can give accurate predictions.In the end we get a 97% accurate XGBoost model and an 95% accurate Logistic Regression model as the best set of models.

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Credit%20Card%20Fraud%20Detection/Images/density_curve.png" width="400">
