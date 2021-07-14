# Board Game Review Prediction
The game market is an increasingly large industry. The board-game market, which is the most traditional in the game market, continues to show a steady growth. It is very important for both publishers and players to predict the propensity of users in this huge market and to recommend new games. Despite its importance, no study has been performed on board-game recommendation systems. In this study, we propose a method to build a deep-learning-based recommendation system using large-scale user data of an online community related to board games. Our study showed that new games can be effectively recommended for board-game users based on user big data accumulated for a long time. This is the first study to propose a personalized recommendation system for users in the board-game market and to introduce a provision of new large datasets for board-game users. The proposed dataset shares symmetric characteristics with other datasets and has shown its ability to be applied to various recommendation systems through experiments. Therefore, the dataset and recommendation system proposed in this study are expected to be applied for various studies in the field.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-27/Board%20Game%20Review%20Prediction/Images/game1.jpg)

## Dataset
The dataset is collected from Kaggle website. Here is the link : https://www.kaggle.com/gabrio/board-games-dataset

## Goal
The goal of this project are -
1. What are the categories of game that are the most popular?  
2. Can we build a model with the available data that predicts user rating? What factors make for the best "modern" board game.

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-27/Board%20Game%20Review%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization on different factors
4. Prediction Models -
    - Spliting the dataset into 85:15 ratio
    - Deploying the models
        - OLS Regression
        - Decision Tree Regression
        - Random Forest Regression
        - Lasso Regression
        - Ridge Regression
        - MLP Regression
        - XgBoost Regression
        - Gradient Boosting Regression
5. Comparing the accuracy of the models
6. Conclusion

## Data Visualization

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-27/Board%20Game%20Review%20Prediction/Images/game2.png)

## Model Comparison

We have deployed eight machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|R2 Score|Mean Squared Error|
|:---:|:---:|:---:|
|OLS Regression|0.35|2.34|
|Decision Tree Regressor|0.05|2.83|
|Random Forest Regressor|0.41|2.23|
|Lasso Regression|0.32|2.39|
|Ridge Regression|0.35|2.34|
|XgBoost Regressor|0.41|2.23|
|MLP Regressor|0.02|2.86|
|Gradient Boosting Regressor|0.41|2.23|


### Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Gradient Boosting Regression, XgBoosting Regression and Random Forest Regression are having the upper hand in case of this dataset and after this, we can use Ridge Regressor, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Gradient Boosting
2. XgBoosting Regressor
3. Random Forest
4. OLS Regression
5. Ridge Regressor
6. Lasso Regressor
7. Decision Tree Regressor
8. MLP Regressor

Hooray!! The models are deployed successfully!

*************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
