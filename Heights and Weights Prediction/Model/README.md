# Heights and Weights Prediction
Height and weight prediction has been a popular problem in ergonomics study. In this paper, we reduce the dimension by principal component analysis and choose the best regression equation using various statistical criterion such as Residual Mean Square (RMSq), Mallow Cp and Akaike information criterion (AIC). Finally, compared with the real value, we analyze the fitting accuracy of the regression equation we proposed.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-17/Heights%20and%20Weights%20Prediction/Images/ht1.webp)

## Goal
The goal of this project is to build the prediction model using the regression algorithms.

## Dataset
The dataset is collected from Kaggle website. Here is the link : https://www.kaggle.com/tmcketterick/heights-and-weights
*I have uploaded the same in the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-17/Heights%20and%20Weights%20Prediction/Dataset) folder, you can access that too!*

## What Have I done
1. Firstly import all the required libraries. Check [`requiremnts.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-17/Heights%20and%20Weights%20Prediction/requirements.txt).
2. Import the dataset and open the Jupyter Notebook file.
3. Process the data and visualize it.
4. Deploying various models for the prediction model -
    - Linear regression
    - Random forest regressor
    - Decision tree regressor
    - Lasso regressor
    - Ridge regressor
5. Checking the accuracy
6. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn

## Model Visualization
- Linear Regression model fitting :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-17/Heights%20and%20Weights%20Prediction/Images/ht1.png)

- Lasso regression model fitting :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-17/Heights%20and%20Weights%20Prediction/Images/ht2.png)

## Model Comparison
We have deployed five machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.96|
|Decision Tree Regressor|0.87|
|Random Forest Regressor|0.94|
|Lasso Regression|0.95|
|Ridge Regression|0.78|

## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Linear Regression is having the upper hand in case of this dataset and after this, we can use Lasso Regression, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Linear Regression
2. Lasso regression
3. Random forest regressor
4. Decision tree regressor
5. Ridge regressor

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
