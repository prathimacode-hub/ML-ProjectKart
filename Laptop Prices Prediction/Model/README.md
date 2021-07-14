# Laptop Prices Prediction
Artificial Intelligence is an integral part of all major e-commerce companies today. With the evolution of the information industry and extensive research in the field of AI in the past two decades, businesses have started to explore the ways to automate various activities using state of the art Machine Learning algorithms and Deep Neural Networks. Many IT giants and start-ups have already taken a big leap in this field and have dedicated teams and resources for research and development of cutting edge AI applications. Online retail platforms today are extensively driven by AI-powered algorithms and applications. Activities ranging from inventory management and quality checking at the warehouse to product recommendation and sales demographics on the website, all employ machine learning at various scales.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/Images/lap1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/ionaskel/laptop-prices. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-42/Laptop%20Prices%20Prediction/Dataset) folder too, you can access that!


## Goal
The goal of this project is to make a Prediction model which will predict the prices of the laptops depending on various factors, such as size, company, set up and many more things!
***********************************

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization
4. Label Encoding
    - Encoding
    - Scalling
5. Prediction Models
    - Spliting the dataset into 75:25 ratio
    - Deploying the models
        - Linear Regression
        - Decision Tree Regression
        - Random Forest Regression
        - Lasso Regression
        - Ridge Regression
        - MLP Regression
        - XgBoost Regression
        - Gradient Boosting Regression
        - Support Vector Regression
6. Comparing the accuracy of the models
7. Conclusion

****************************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Seaborn
5. Sklearn
6. XgBoost

***************************************
## Data Visualization
- **Prices v/s Size of the Laptop - Jointplot**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/Images/lap2.png)

- **Most laptops size probability**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/Images/lap4.png)

- **Most laptops Price**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/Images/lap5.png)

- **Company vs Price of the Laptops in Euros**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-42/Laptop%20Prices%20Prediction/Images/lap6.png)
*****************************************
## Comparative analysis among the algorithms for this project

We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|78.47%|
|Decision Tree Regressor|87.57%|
|Random Forest Regressor|93.33%|
|Lasso Regression|78.47%|
|Ridge Regression|78.47%|
|XgBoost Regressor|92.71%|
|MLP Regressor|-36.17%|
|Gradient Boosting Regressor|93.43%|
|Support Vector Regressor|13.98%|

*****************************
## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Gradient Boosting Regression is having the upper hand in case of this dataset and after this, we can use  Random Forest Regressor, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Gradient Boosting
2. Random Forest Regressor
3. XgBoosting Regressor
4. Decision Tree Regressor
5. Lasso Regressor
6. Ridge Regressor
7. Linear Regression
8. Support Vector Regressor
9. MLP Regressor

**************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
