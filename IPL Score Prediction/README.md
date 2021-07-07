# TITLE : IPL SCORE PREDICTION

### A glimpse of the web app:
 ![GIF](readme_resources/j.gif)

# How to run the project
Just download the project and expand the frontend, backend, dataset and Model folder and run the app.py file in the jupyter notebook.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/laxmena/ipl-dataset-2020-season-included. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/Dataset) folder too, you can access that!

## Goal
The goal of this project is to predict the score of an innings in an IPL match. I have implemented an end to end project. Its frontend is implemented using html5 and css3. Its backend is designed using flask. This project has a practical application , it can be used to predict the score of innings of IPL match in advance so users can use it.

******************************************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Data Visualization
5. Prediction Models
    - Spliting the dataset into 75:25 ratio
    - Deploying the models
        - Linear Regression
        - Decision Tree Regression
        - Random Forest Regression
        - Huber Regression
        - Ridge Regression
        - Support Vector Regression
        - TheilSen_Regression
        - Gamma_regreesor 
        - KNN 
        - Linear_SVR
6. Comparing the accuracy of the models
7. Conclusion

****************************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost
*******************************************************
## Comparative analysis among the algorithms for this project

We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.74|
|Decision Tree Regressor|0.63|
|Random Forest Regressor|0.60|
|Huber Regression|0.64|
|Ridge Regression|0.74|
|TheilSen Regressor|0.71|
|Gamma Regressor|0.63|
|Linear_SVR Regressor|0.66|
|Support Vector Regressor|0.62|
|KNN|0.65|
************************************************
## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Linear Regressor is having the upper hand in case of this dataset and after this, we can use Linear Regressor which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1) Linear Regression
2) Decision Tree Regression
3) Random Forest Regression
4) Huber Regression
5) Ridge Regression
6) Support Vector Regression
7) TheilSen_Regression
8) Gamma_regreesor 
9) KNN
10) Linear_SVR

Hooray!! The models are deployed successfully!

*****************************************************

## Author
Code Contributed by, Suryansh Naugraiya, 2021 @SuryanshNaugraiya #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
