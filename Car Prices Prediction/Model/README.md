**Problem Statement**

- A Chinese automobile company Geely Auto aspires to enter the US market by setting up their manufacturing unit there and producing cars locally to give competition to their US and European counterparts.

- They have contracted an automobile consulting company to understand the factors on which the pricing of cars depends. Specifically, they want to understand the factors affecting the pricing of cars in the American market, since those may be very different from the Chinese market. The company wants to know:

- Which variables are significant in predicting the price of a car How well those variables describe the price of a car Based on various market surveys, the consulting firm has gathered a large data set of different types of cars across the America market.


**Project Title**

Car Prices Prediction


**GOAL**

We are required to model the price of cars with the available independent variables. It will be used by the management to understand how exactly the prices vary with the independent variables. They can accordingly manipulate the design of the cars, the business strategy etc. to meet certain price levels. Further, the model will be a good way for management to understand the pricing dynamics of a new market.




**WHAT I HAD DONE**

I have done the following operations on the given dataset

-  Data cleaning
-  Exploratory Data Analysis
-  Feature selection using Recursive Feature elimination(RFE)
-  Data Modelling and evaluation


**MODELS USED**

-  Linear Regression
-  Random Forest Regressor
-  Decision Tree Regressor

**LIBRARIES NEEDED**

- numpy
- pandas
- seaborn
- matplotlib
- Sklearn

**Accuracy**

By using Linear Regression I got 
 ```python
    Test set Accuracy:   0.7375029659751728
 ``` 
By using Random Forest Regressor I got 
 ```python
    Test set Accuracy:   0.9065838247336128
 ``` 
By using Decision Tree Regressor I got 
 ```python
    Test set Accuracy:   0.8839965378654326
 ``` 

**Conclusion**

- We applied three models Linear Regression Decision Tree Regressor,and RandomForest Regressor.
- As we can see random forest performing best (with accuracy ~ 0.90)
 
