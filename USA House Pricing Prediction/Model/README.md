# USA House Pricing Prediction
With Covid encouraging city dwellers to move to the suburbs and families looking for home offices and bigger yards, prices for the American dream home have skyrocketed. Home prices surged in March, up 13.2% from the year prior, according to the S&P CoreLogic Case-Shiller National Home Price Index. “Everybody expected housing to really sort of dry up with the rest of the economy,” said National Association of Home Builders CEO Jerry Howard. “And in fact, the opposite has happened. People who have been sort of scared out of the cities by the pandemic.”

In this crisis, a prediction model is required for generating the prices for the houses.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-20/USA%20House%20Pricing%20Prediction/Images/us1.jpg)

## Goal
The goal of this project is to make a prediction model, which will predict the price of the houses at USA, depending on the given features.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/dmvreddy91/usahousing. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-20/USA%20House%20Pricing%20Prediction/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-20/USA%20House%20Pricing%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Exploratory Data Analysis
    - Distribution of data plotting using distplot
    - Feature distribution using Boxplot
    - Data Pre-processing
4. Regression Model creation
    - Linear regression
    - Random Forest regression
    - Lasso regression+
    - Ridge regression
    - Gradient Boosting regression
    - XGBoosting regression
    - MLP regression
    - Support vector regressor
5. Accuracy wise distribution
6. Conclusion


## Model Visualization
1. Average Area Income

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-20/USA%20House%20Pricing%20Prediction/Images/us2.png)

2. Area Population

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-20/USA%20House%20Pricing%20Prediction/Images/us4.png)

3. Price

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-20/USA%20House%20Pricing%20Prediction/Images/us3.png)

## Model Comaparison
We have deployed fifteen machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.
|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.92|
|Ridge Regression|0.92|
|Lasso Regression|0.92|
|Polynomial Linear Regression|0.92|
|Polynomial Ridge Regression|0.92|
|Polynomial Lasso Regression|0.92|
|Polynomial XgBoosting Regressor|0.91|
|Polynomial Decision Tree|0.91|
|Linear XgBooster|0.90|
|Linear Decision Tree|0.90|
|Linear MLP|0.49|
|Linear SVR|-0.00|
|Polynomial SVR|-0.00|
|Polynomial MLP Regressor|-13.97|

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Linear Regression is having the upper hand in case of this dataset and after this, we can use Lasso Regression, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. Polynomial Linear Regression
5. Polynomial Ridge Regression
6. Polynomial Lasso Regression
7. Polynomial XgBoosting Regression
8. Polynomial Decision Tree Regressor
9. linear XgBoosting regressor
10. linear MLP regressor
11. Linear SVR
12. Polynomial SVR
13. Polynomial MLP regressor

Hooray!! The models are deployed successfully!

***********************************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
