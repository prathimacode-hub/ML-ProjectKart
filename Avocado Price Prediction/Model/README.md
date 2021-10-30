# Avocado Price Prediction

In this project we will be working with an avocado sales dataset, indicating and predciting on how does Avocado sales will take place and doing the visualization of the dataset to understand the sales of avocado.We used various methods for getting a detailed visualization like boxplots , distplots , 

**GOAL**

The goal is to predict Avocado Prices.

Dataset can be downloaded from [here](https://www.kaggle.com/neuromusic/avocado-prices)

**WHAT I HAD DONE**
- Discussed some major columns on which Avocado Prices maybe dependent
- We optimized our data before modelling using encoder to make it useful to implement Regression models
- Then I used different regression models present in sklearn to train the model.
- Used data visualization methods to understand the past sales

**MODELS USED**
-  Linear Regression : linear regression is a linear approach for modelling the relationship between a scalar response and one or more explanatory variables
-  Ridge Regression : Ridge regression is a method of estimating the coefficients of multiple-regression models in scenarios where independent variables are highly correlated.
-  Random Forest Regressor : A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**CONCLUSION**
In this model , we worked upon the avocado past sales dataset . We first performed an Exploratory Data Analysis on the given dataset , following which , we used Encoding to make classification data more useful to work for prediction using regression models.We saw , overall Random Forest Model , is the best fitted model and gives us with the best accuracy scores.The implemented 3 regression models , and the accuracies of which are mentioned below :
By using Linear Regression I got 
 ```
      Accuracy of testing data: 85.05
 ``` 

 
  By using Ridge Regression I got 
 ```
    Accuracy of testing data: 85.07
 ``` 
 
 By using Random Forest I got 
 ```
    Accuracy of testing data: 93.46
 ``` 



<a href="https://github.com/photon149">Shiwansh Raj</a>

