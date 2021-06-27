# Bike Crash Analysis

The objectives of the present project were to describe the main characteristics of bicycle crashes with regard to the road environment, crash opponent, cyclist, and crash dynamics; compare individuals who describe their health after the crash as declined with those who describe their health as not affected; and compare the number of injured cyclists who describe their health as declined after the crash with the predicted number of permanent medical impairments within the same population.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike1.jpg)

## Goal
The goal of this project to analyze the dataset on various factors and depending on the various factors making of a prediction model which will predict the accident prone sights.

## Dataset
The dataset is collected from Kaggle website. Here is the link : https://www.kaggle.com/atharvaingle/bikepedcrash. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-26/Bike%20Crash%20Analysis/Dataset) folder too, you can access that!


## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Exploratory Data Analysis
    - Feature distribution using Barplot
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

## Data Visualization 
1. **Availability of ambulance at the sight of the accident**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike2.png)

2. **Age Group wise Analysis**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike3.png)

3. **License of the accidented bike**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike4.png)

4. **Position of the bikes at the time of the accident**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike5.png)

5. **Injuries due to bike accident**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-26/Bike%20Crash%20Analysis/Images/bike6.png)

:yellow_circle: For more Data Visualization on 20 more different factors, check out the [`Images`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-26/Bike%20Crash%20Analysis/Images) folder!

************************************************************

## Model Comparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|96.91%|
|Decision Tree Regressor|95.93%|
|Random Forest Regressor|97.04%|
|Lasso Regression|96.91%|
|Ridge Regression|96.91%|
|XgBoost Regressor|97.89%|
|MLP Regressor|0.03%|
|Gradient Boosting Regressor|97.90%|
|Support Vector Regressor|0.02%|

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Gradient Boosting Regression is having the upper hand in case of this dataset and after this, we can use  XgBoosting Regressor, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Gradient Boosting
2. XgBoosting Regressor
3. Random Forest
4. Linear Regression
5. Lasso Regressor
6. Ridge Regressor
7. Decision Tree Regressor
8. MLP Regressor
9. Support Vector Regressor


Hooray!! The models are deployed successfully!

**************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
