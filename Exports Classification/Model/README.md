# Exports Classification
Canadian exports of goods and services combined reached $729 billion in 2019, up 2.2% goods exports alone were up 1.7%, while services exports were up 4.4%. This overall growth in goods and services exports was weak compared to the last decade when goods and services exports grew annually on average 4.6%. Although services exports account for 18% of Canadian exports, they averaged 5.7% annual growth between 2010 and 2019, outpacing the 4.4% annual growth in goods exports, which account for the much larger share (82%) of Canadian exports. Growth in services exports has also been less volatile than growth in goods exports: annual growth for services exports ranged between 1.4% and 6.9% during the decade while for goods exports it ranged between -1.0% and 13%.

Now using the dataset I am going to create a classification model, which can predict the capita of export with respect to the years.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-19/Exports%20Classification/Images/ex2.jpg)

## Goal
The goal of this project is to build a classification model, using regression algorithms, such as, linear regression, random forest regression, decision tree regressor and many more algorithms. After that the models are going to be evaluated using the accuracy scores.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/balakrishcodes/others?select=canada_per_capita.csv. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-19/Exports%20Classification/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-19/Exports%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Plotting the year v/s capita curve for the dataset
4. Regression Model Creation
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

## Libraries used
1. Numpy
2. Seaborn
3. Pandas
4. Matplotlib
5. Sklearn
6. XgBoost

## Model Visualization
- Year v/s Capital graph for Canada

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-19/Exports%20Classification/Images/ex3.png)

## Model Comparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.64|
|Decision Tree Regressor|0.94|
|Random Forest Regressor|0.95|
|Lasso Regression|0.64|
|Ridge Regression|0.64|
|XgBoost Regressor|0.94|
|MLP Regressor|-1.75|
|Gradient Boosting Regressor|0.94|
|Support Vector Regressor|-0.02|


### Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Regressor is having the upper hand in case of this dataset and after this, we can use Decision Tree, XgBoost and Gradient Boosting, which are also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Random Forest Regressor
2. Decision Tree Regressor
3. Gradient Boosting
4. XgBoost
5. Lasso
6. Ridge
7. Linear regression
8. Support Vector regressor
9. MLP regressor

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
