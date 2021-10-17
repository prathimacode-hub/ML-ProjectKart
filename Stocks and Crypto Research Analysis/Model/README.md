





![MIT License](https://miro.medium.com/max/1200/1*e8UBEaMt7Pw5d9gP0tLHjA.png)

  
## Project Title


Stocks and Crypto Research Analysis.


***************************************


## GOAL
The goal of this project is to make a prediction model which will predict the future stock price based on the given dataset.
***************************************


##  Problem Statement
We are going to use Time Series data to analysis of stock price(Apple company dataset).

Time series forecasting is a technique for the prediction of events through a sequence of time. The technique is used across many fields of study, from geology to behavior to economics. The techniques predict future events by analyzing the trends of the past, on the assumption that future trends will hold similar to historical trends.

***************************************

  
## What have I done?

In here,I have made stock price prediction model using Time Series data  analysis.In which I have used Long short-term memory (LSTM), Linear Regression,  k-Nearest Neighbors for  prediction.
   
***************************************
## Contents
1.Importing all the required libraries.

2.Upload the dataset .

3.Exploratory Data Analysis.

4.Data Processing
 
5.Prediction Models
   - Long short-term memory (LSTM)
   -  Linear Regression
   -  k-Nearest Neighbors
    

6.Model Comparison


7.Conclusion

***************************************

  
## Model  Used
* Long short-term memory (LSTM) 

* Linear Regression

* k-Nearest Neighbors

***************************************

##  Long short-term memory (LSTM) 

Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can not only process single data points (e.g. images), but also entire sequences of data (such as speech or video inputs).
LSTM models are able to store information over a period of time.


In implementation Long Short Term Memory (LSTM) model gives the Root-mean-square error (RMSE) value 143.27


 ## Linear Regression

 The most basic machine learning algorithm that can be implemented on this data is linear regression. The linear regression model returns an equation that determines the relationship between the independent variables and the dependent variable.
 
In implementation Linear Regression model gives the Root-mean-square error (RMSE) value 50.57


## k-Nearest Neighbors
 kNN (k nearest neighbours). Based on the independent variables, kNN finds the similarity between new data points and old data points. 


In implementation KNN model gives the Root-mean-square error (RMSE) value 94.18.


***************************************

 ## Exploratory Data Analysis
 **1. Original Data:**
 
  
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Images/Orignal.png" width = "700">


  **2. Predicated Data by LSTM**

<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Images/LSTM.png" width = "700">


 **3. Predicated Data by Linear Regression**
 
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Images/LR.png" width = "700">

 **4. Predicated Data by KNN**
 
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Images/KNN.png" width = "700">


***************************************


## Model Accuracy comparison
| Model           | RMSE Value                                                           |
| ----------------- | ------------------------------------------------------------------ |
| LSTM | 143.27 |
|Linear Regression | 50.57 |
| KNN |94.186  |
***************************************

## LIBRARIES NEEDED

* numpy

* pandas

* matplotlib

* tensorflow

* Seaborn

* keras
***************************************

## Conclusion
* Here I have applied three different algorithms along with the Neural Networks.

*  Long Short Term Memory (LSTM) model gives  Root-mean-square error (RMSE) value 143.27

*  Linear Regression model gives Root-mean-square error (RMSE) value 50.57

*  KNN model gives Root-mean-square error (RMSE) value 94.18.

* But the Long short-term memory (LSTM)  stand out to be the best model among all those implemented models based on the accuracy scores.


* Also dont select random data-sample as this is time series data , the model does not provides too much of accuracy if you select the random data sample for testing and training. 
* So, for this project, the best model is LSTM gives more accuracy .
***************************************


## Authors

- Code Contributed by Tanvi Deshmukh.
  #Hacktoberfest2021

  





   ![MIT License](https://img.shields.io/badge/Made_With_Jupyter-2CA5E0?style=for-the-badge_Color=whit)

  




