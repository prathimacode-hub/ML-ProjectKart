#  WALMART SALES PREDICTION 

**GOAL** 
- The main purpose of this project is to predict the future sales at walmart.

**DATASET**
- The data used in this project can be downloaded from [here](https://www.kaggle.com/divyajeetthakur/walmart-sales-prediction).

**WHAT I HAD DONE**
- I have used TIME SERIES FORECASTING approach for this project.
- I collected and mereged the dataset and prepared it for analysis.
- Created data visualisations to understand the data in a better way.
- Found strong relationships between independent features and dependent feature using correlation.
- Performed Time series Analysis on data.
- Check if data was stationary or not to make it ready for forecasting.
- Visualised Time series components
- Handled missing values using strong correlations,dropping unnecessary ones.
- Used different forecasting Models like Naive approach,Moving average model,Holt's linear trend,Holt winter's model,ARIMA to predict the dependent feature in most suitable manner.
- Visualized all of the performance using matplotlib and seaborn library.
- Compared various models and used best performance model to make predictions.
- Used Mean Squared Error and Mean Absolute Error for evaluating model's performance.


**MODELS USED**
- 
 Model | Mean Absolute Error| 
  -------- | ---------- | 
 Naive Approach | 132.66 | 
 Moving Average Model | 123.13 | 
 Holt's Linear trend Model | 19863.62| 
 Holt Winter's Model | 11637.95 |
 ARIMA | 23660.23
 
 
 **TIME SERIES ANALYSIS METHODS USED**
 - Stationarity of time series
 - Rolling Mean & Standard deviation
 - Auto Correlation & Partial Correlation
 - Lag scatter plot
 - Differencing in Time series
 - Time series components
 - Moving Average
 - Exponential Smoothing 

**LIBRARIES NEEDED**
- pandas
- NumPy
- matplotlib
- seaborn
- statsmodels


**CONCLUSION**
- Time series analysis give better insights with time related data.
- we can consider Mean Absolute Error for evaluating models.
- By Using Naive Approach model, We can get the minimum Mean Absolute Error value possible.
- Here, Naive approach model can predict most accurate results for predicting future walmart sales which is highest model performance in comparison with other Models.
