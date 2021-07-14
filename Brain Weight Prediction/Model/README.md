# Brain Weight Prediction
Brain morphology varies across the ageing trajectory and the prediction of a person's age using brain features can aid the detection of abnormalities in the ageing process. Existing studies on such “brain weight prediction” vary widely in terms of their methods and type of data, so at present the most accurate and generalisable methodological approach is unclear. Therefore, we used the UK Biobank data set (N = 10,824, age range 47–73) to compare the performance of the machine learning models support vector regression, relevance vector regression and Gaussian process regression on whole-brain region-based or voxel-based structural magnetic resonance imaging data with or without dimensionality reduction through principal component analysis. Performance was assessed in the validation set through cross-validation as well as an independent test set. The models achieved mean absolute errors between 3.7 and 4.7 years, with those trained on voxel-level data with principal component analysis performing best. Overall, we observed little difference in performance between models trained on the same data type, indicating that the type of input data had greater impact on performance than model choice. All code is provided online in the hope that this will aid future research.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-34/Brain%20Weight%20Prediction/Images/brain5.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/anubhabswain/brain-weight-in-humans. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-34/Brain%20Weight%20Prediction/Dataset) folder too, you can access that!

## Goal
The goal of this project is to make a prediction model which will predict the weight of the human brain depending on the head size.

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-34/Brain%20Weight%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data preprocessing
4. Prediction Models
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
5. Comparing the accuracy of the models
6. Conclusion
***********************************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost

***************************************
## Model Visualization

1. **Linear Regression Model** :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-34/Brain%20Weight%20Prediction/Images/brain1.png)

2. **Lasso Regression Model** :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-34/Brain%20Weight%20Prediction/Images/brain2.png)

3. **Ridge Regression Model** :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-34/Brain%20Weight%20Prediction/Images/brain3.png)

*****************************
## Comparative analysis among the algorithms for this project

We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.49|
|Decision Tree Regressor|0.29|
|Random Forest Regressor|0.39|
|Lasso Regression|0.49|
|Ridge Regression|0.49|
|XgBoost Regressor|0.45|
|MLP Regressor|0.32|
|Gradient Boosting Regressor|0.44|
|Support Vector Regressor|0.23|
*******************************************
## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Linear Regression, Lasso Regression and Ridge Regression are having the upper hand in case of this dataset and after this, we can use XgBoost regressor which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. XgBoost Regression
5. Gradient Boosting Regression
6. Random Forest Regression
7. MLP Regressor
8. Decision Tree Regression
9. Support Vector Machine Regression

Hooray!! The models are deployed successfully!

*************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
