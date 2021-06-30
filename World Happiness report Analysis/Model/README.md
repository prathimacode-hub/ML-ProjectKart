# World Happiness Report

## Goal

The aim of the project is to predict happiness scores and rankings and
perform a detailed analysis and visualization of the training dataset and create a model. 

## Dataset

You can download dataset [here](https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021)

## WHAT I HAD DONE

1. Loading Dataset
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Created Model
5. Predicted on Test data

The World Happiness Report uses markers to indicate the happiness of each country. 
It is collected to create a "Ladder Score" and then it is eventually changed to include a "Dystopia + residual" score. The main indicators include

![](https://github.com/Isha307/ML-ProjectKart/blob/main/World%20happiness%20report/Images/happiness.png)

* GDP per capita
* Social Support
* Life Expectancy
* Freedom of Life Choices
* Generosity
* Perception of Corruption

## MODELS USED

 - Linear Regression 
 - Support Vector Regression
 - Deep Neural Network
 
## LIBRARIES NEEDED

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- tensorflow
- os

## Conclusion

In this project we have performed  analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. 
Then we used different Regressors to predict the Ladder score. After performing the model comparative 
analysis we can conclude that Linear Regressor gave the best Result out of all.

```
Linear Regression
Score:  0.9999997816674735

SVM
Score:  0.6710844770804237
```
**Loss for DNN:**

![](https://github.com/Isha307/ML-ProjectKart/blob/main/World%20Happiness%20report%20Analysis/Images/accuracy.png)

## Author

This model is created by [Isha307](https://github.com/Isha307)
