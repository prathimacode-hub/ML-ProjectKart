# Airbnb Price Prediction
Pricing a rental property on Airbnb is a challenging task for the owner as it determines the number of customers for the place. On the other hand, customers have to evaluate an offered price with minimal knowledge of an optimal value for the property. This paper aims to develop a reliable price prediction model using machine learning, deep learning, and natural language processing techniques to aid both the property owners and the customers with price evaluation given minimal available information about the property. Features of the rentals, owner characteristics, and the customer reviews will comprise the predictors, and a range of methods from linear regression to tree-based models, support-vector regression (SVR), K-means Clustering (KMC), and neural networks (NNs) will be used for creating the prediction model.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/stevezhenghp/airbnb-price-prediction.

## Goal
The goal of this project is to make a prediction model which will predict the prices of the Airbnb hotels using different parameters.
***************************************

## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Exploratory Data Analysis
4. Data Processing
5. Prediction Models
    - Linear Regression
    - Random Forest Regression
    - Gradient Boosting Regression
    - Dense Neural Networks
    - Model Comparison
6. tf-idf Transformer
7. Stacked Regression
8. Validation Process
9. Conclusion

********************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. tfidf
7. stack_regression

**********************************
## Exploratory Data Analysis
1. **Price Distribution**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air2.png)

2. **Years of first review and price**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air3..png)

3. **Price distribution for na and notna values in first_review column**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air4.png)
**************************************
## Model Visualization
- **Random Forest Regressor Model**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air8.png)   ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-46/Airbnb%20Price%20Prediction/Images/air9.png)
**************************************
## Model comparison
Here I have deployed four algorithms to deploy the models, now let's check the accuracy scores for these models.

|Models|Accuray Score|
|-|-|
|Linear Regression|0.68|
|Random Forest Regression|0.73|
|Gradient Boosting Regressor|0.68|
|Dense Neural Networks|0.69|
***************************************
## Conclusion
* Here I have applied four different algorithms along with the Neural Networks.
* But the Random Forest Regressor stand out to be the best model among all those implemented models based on the accuracy scores.
* After the tf-idf transformation on Random Forest Regressor, the models accuracy decreased, so, I will suggest rather not to use the transformation on Random Forest.
* Also after the stacked regression process, the model does not provides too much of accuracy.
* So, for this project, the best model is only **Random forest regressor** without any kind of transformation or stacked regression.

******************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
