**PROJECT TITLE - Uber Fare Prediction**
  
 
 
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Uber%20Fare%20predictions/Images/project_viz2.png" width="400"> 
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Uber%20Fare%20predictions/Images/project_viz1.png" width="200">


**GOAL** - The main objective of project is to design an algorithm which will tell the fare to be charged for a passenger. Multiple machine learning algorithms have been used to develop a regression model.

**DATASET** - Download the data set from https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/data

**WHAT HAVE I DONE**
- Loading datasets
- Eliminating null values
- Changing required columns into Datetime format
- Extracting the year, month, date and week day of the ride
- Extracting the Hour, Minute and Second values
- Removing the Latitude values that are greater than 90 or lesser than -90
- Removing the Longitude values that are greater than 180 or lesser than -180
- Calculating the Haversine Distance
- Removing all the rows where passengers count is more than 6
- Preprocessing the target column -> Fare amount
- Visualizing the data using boxplots
- Dealing with Outliers
- Splitting the data
- Defining a model to pass any algorithm and to calculate the r2_score, MAE, MSE, RMSE.
- Using RandomForestRegressor
- Using Linear Regression
- Using KNNs
- Using Decision Tree
- Saving the model locally
- Using this saved model to perform predictions on the test data.


**MODELS USED**
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- KNNs - *algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.*
- RandomisedSearchCV - *This is a hyperparameter optimistion algorithm that increases the model accuracy by tweaking the hyperparameters to their best values*

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

**Data Visualizations**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Uber%20Fare%20predictions/Images/boxplot_3.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Uber%20Fare%20predictions/Images/final_outlier_plot.png" width="500">

**Conclusion**

We can conclude from this project that the Random Forest is a very powerful model to perform regression tasks using ensemble learning appraoch called as bagging or bootstrap aggregating to predict the fares with an accuracy of 81%.
 
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Uber%20Fare%20predictions/Images/RF_regressor.png" width="500">
