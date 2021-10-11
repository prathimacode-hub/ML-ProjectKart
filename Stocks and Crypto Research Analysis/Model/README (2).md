





![MIT License](https://miro.medium.com/max/1200/1*e8UBEaMt7Pw5d9gP0tLHjA.png)

  
# Project Title


Stocks and Crypto Research Analysis.




## GOAL
The goal of this project is to make a prediction model which will predict the future stock price based on the given dataset.


##  Problem Statement
We are going to use Time Series data to analysis of stock price.

  
## What have I done?

1.Importing all the required libraries.

2.Upload the dataset and the Jupyter Notebook file.

  
## Model  Used
* Long short-term memory (LSTM) 

* Linear Regression

* k-Nearest Neighbors


#  Long short-term memory (LSTM) 

Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can not only process single data points (e.g. images), but also entire sequences of data (such as speech or video inputs).
LSTM models are able to store information over a period of time.

### RMSE value -143.27

 # Linear Regression

 The most basic machine learning algorithm that can be implemented on this data is linear regression. The linear regression model returns an equation that determines the relationship between the independent variables and the dependent variable.

 ### RMSE value -50.57

# k-Nearest Neighbors
 kNN (k nearest neighbours). Based on the independent variables, kNN finds the similarity between new data points and old data points. 

 ### RMSE value -94.186

 ## Data Visualization
 
  # Orignal Data:
  
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Image/Orignal.png" width = "500">
### RMSE value -143.27

 #  Predicate Data by LSTM

<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Image/LSTM.png" width = "500">

 #  Predicate Data by Linear Regression
 
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Image/LR.png" width = "500">
### RMSE value -50.57

 #  Predicate Data by KNN
 
<img src = "https://github.com/tanvideshmukh29/ML-ProjectKart/blob/main/Stocks%20and%20Crypto%20Research%20Analysis/Image/KNN.png" width = "500">
 ### RMSE value -94.186


## Model Accuracy comparison
| Model           | RMSE Value                                                           |
| ----------------- | ------------------------------------------------------------------ |
| LSTM | 143.27 |
|Linear Regression | 50.57 |
| KNN |94.186  |

## LIBRARIES NEEDED

* numpy

* pandas

* matplotlib

* tensorflow

* keras

## Conclusion
* Here I have applied three different algorithms along with the Neural Networks.

* But the Long short-term memory (LSTM)  stand out to be the best model among all those implemented models based on the accuracy scores.


* Also dont select random data-sample as this is time series data , the model does not provides too much of accuracy if you select the random data sample for testing and training. 
* So, for this project, the best model is only LSTM .


## Authors

- Code Contributed by Tanvi Deshmukh.
  #Hacktoberfest2021

  





   ![MIT License](https://img.shields.io/badge/Made_With_Jupyter-2CA5E0?style=for-the-badge_Color=whit)

  




