**PROJECT TITLE - Solar Eclipse Classification**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Solar%20Eclipse%20Classification/Images/project_viz1.png" width="400">

**GOAL** - The aim of this project is to classify among the main types of Solar eclipses, which are : P = Partial Eclipse, A = Annular Eclipse, T = Total Eclipse, H = Hybrid or Annular/Total Eclipse.


**WHAT HAVE I DONE**

- Loading datasets
- Concatenating both the training and test set
- Handling null values
- Dealing with the target variable and extracting only the main types of eclipses
- Dealing with the Calender Date column
- Extracting the year, month and date values
- Dealing with the Eclipse Time column
- Changing into Datetime format
- Extracting the hour, minutes and seconds
- Dealing with Latitude and Longitude Column
- Extracting the longitude and latitude numeric value and direction
- Dealing with the Central Duration column
- Extracting the minutes and seconds
- Performing One Hot Encoding on the categorical columns
- Performing Label Encoding on the categorical columns
- Converting the object data types into numeric data types
- Visualization of the independent features
- Heatmap of the correlation matrix
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Solar%20Eclipse%20Classification/Images/heatmap.png" width="400">

- Performing Feature Scaling
- Visualization of the Target feature(Eclipse Type)
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Solar%20Eclipse%20Classification/Images/target_analysis.png" width="300">

- Splitting the data
- Using Logistic Regression
- Using Random Forest Algorithm
- Using Support Vector Machine(SVM)
- Using XGBoost
- Hyperparameter Tuning using RandomisedSearchCV and Random Forest
- Hyperparameter tuning using GridSearchCV and XGBoost





**MODELS USED**

- Logistic Regression - *A simple classification algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables.* 
- XGBoost - *Extreme Gradient Boost alsorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Support Vector Machine - *SVM is a supervised machine learning algorithm used for both classification and regression. The objective of SVM algorithm is to find a hyperplane in an N-dimensional space that distinctly classifies the data points.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- GridSearchCV/RandomisedSearchCV - *This is a hyperparameter optimistion algorithm that increases the model accuracy by tweaking the hyperparameters to their best values*


**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- datetime
- re
- scikit learn
- xgboost


**Conclusion**

In this project we have performed a exploratory data analysis of the given dataset to extract all the numeric values from the dataframe, preprocess them and lastly feed them to different classifier models. After performing the comaparative analysis we can conclude that Hypertuned XGBoost model performed best both on the training and testing set thus giving predictions with a test accuracy of 96.8%.

