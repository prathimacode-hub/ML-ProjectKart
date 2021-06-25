**PROJECT TITLE - Flight Fare Prediction**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Flight%20Fare%20Prediction/Images/project_viz.png" width="400">

>

**GOAL** - The aim of the project is to predict the fare of different Airlines covering different routes

**WHAT HAVE I DONE**
- Loading datasets
- Data Preprocessing and Visualization
- Eliminating null values
- Change required columns into Datetime format
- Extracting day, month and year from columns
- Extracting Hours and Minutes from columns
- Processing the Duration column to get numerics values of hours and minutes
- Splitting the dataframe into Numerical and Categorical data
- Dealing with Outliers
- Performing One Hot Encoding on Destination column
- Extracting the useful data from Route column by splitting using '→' as delimiter
- Performing Label Encoding on extracted route data
- Mapping key values to Dictionary
- Concatinating all the new processed columns to form the training dataframe
- Data Splitting
- Getting the prority score of all the features wrt the Dependent feature
- Applying Train_Test_Split
- Model training
- Defining a model to pass any algorithm and to calculate the r2_score, MAE, MSE, RMSE
- Using RandomForestRegressor
- Using Linear Regression
- Using KNNs
- Using Decision Tree
- HyperParameter Tuning
- Saving the hypertuned model
- Using the saved model to perform predictions on the test set



**MODELS USED**
- Linear Regression - *A machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- KNNs - * An algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- RandomisedSearchCV - *This is a hyperparameter optimistion algorithm that increases the model accuracy by tweaking the hyperparameters to their best values*


**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- datetime
- pickle

**Comparing the models**

- Random Forest Regressor accuracy - 81%
- Linear Regressor accuracy - 63%
- KNN Regressor accuracy - 68%
- Decision Tree Regressor accuracy - 69%

*Here we can see that the Random Forest Regressor model gives the highest accuracy of 81%. Now we try to improve this accuracy by hypertuning the base model.*

Accuracy of Random Forest Regressor after Hyperparameter tuning - 84%

**Conclusion**

In this project we have performed a detailed analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comaprative analysis of different Regressons have been done to predict the flight fare predictions.After performing the model comparative analysis we can conclude that the hypertuned Random Forest regressor model performs best with an accuracy of 84%.   

