**PROJECT TITLE - Gold Price Prediction**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Gold%20Price%20Prediction/Images/project_viz.png">

**Dataset**  -   https://www.kaggle.com/shikhnu/gold-price


**GOAL** - The aim of this project is to perform analysis the gold price using different EDA techniques, and eventually train different model to predict the price of gold.

**WHAT HAVE I DONE**
- Loading datasets
- Exploratory Data Analysis
    - Explore price development
    - Relative changes distribution
    - Non-Stationary time series of Gold
    - Box and Whisker Plots:
    - Plotting the Stationarity
    - Analysing the Stationarity using Autocorrelation and Partial Autocorrelation functions
    - Plotting Rolling Statistics
    - Perfroming Augmented Dickey-Fuller Test
    - Making Time Series Stationary using Log Scale Transformation
    - Using multiple techniques to remove Trend - Smoothing
- Splitting the data
- Defining a model to pass any algorithm and to calculate the r2_score, MAE, MSE, RMSE.
- Using RandomForestRegressor
- Using Linear Regression
- Using KNNs
- Using Decision Tree
- Using XGBoost
- Using ARIMA model
- Saving the predictions


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Gold%20Price%20Prediction/Images/plot1.png" width = "800">


**MODELS USED**
- Linear Regression - *A machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting.*
- XGBoost - *eXtreme Gradient Boost algorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- KNNs - *An algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- ARIMA - *An autoregressive integrated moving average, or ARIMA, is a statistical analysis model that uses time series datato either better understand the data set or to predict future trends. A statistical model is autoregressive if it predicts future values based on past values.*


**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- statsmodel
- math
- random
- scikit-learn
- datetime
- xgboost


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Gold%20Price%20Prediction/Images/plot2.png" width = "800">


**Comparing the models**

- **Random Forest Regressor model**
    - *r2_score is:0.9952514739788453*
    - *MAE: 5.0527881656804645*
    - *MSE: 151.6229191950689*
    - *RMSE: 12.313525863661834*

- **Linear Regressor model**
    - *r2_score is:0.9814723124509989*
    - *MAE: 14.06129297282011*
    - *MSE: 591.5987528758583*
    - *RMSE: 24.322803145934028*
    
- **KNN Regressor model**
    - *r2_score is:0.9790869008282281*
    - *MAE: 12.115404339250498*
    - *MSE: 667.7661934911242*
    - *RMSE: 25.84117244807449*
    
- **Decision Tree Regressor**
    - *r2_score is:0.9930578616056049*
    - *MAE: 6.093984220907291*
    - *MSE: 221.66610946745544*
    - *RMSE: 14.888455576971557*
    
- **XGBoost Regressor model**
    - *r2_score is:0.9953626669278454*
    - *MAE: 5.208056544317059*
    - *MSE: 148.07247018285284*
    - *RMSE: 12.16850320223703*

- **ARIMA model**
    - *MAE: 522.071*
    - *RMSE: 624.9156*


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Gold%20Price%20Prediction/Images/arima.png" width = "800">


**Conclusion**

In this project we have performed a detailed analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comaprative analysis of different Regressors have been done to predict the gold price. After performing the model comparative analysis we can conclude that almost all the models had an accuracy above 99% except the ARIMA model, which did not perform well. The Random Forest Regressor and XGBoost regressor gave best results with 99.52% and 99.53% accuracy respectively.  

